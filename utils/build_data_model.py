#!/usr/bin/env python3
"""Run the "Create a new Data model" steps from Readme.md for one model folder.

The four generator scripts in this folder each expect a hardcoded URL to be
edited by hand before every run (10_model.yaml_v10.py line 131, 20_create_spec
line 232, 25_create_subject_context line 323). This driver serves the model
folder over HTTP, patches those lines in a temporary copy of each script, runs
them, and files the outputs back into the model folder. The original scripts
are never modified.

Readme steps covered:
    1  edit schema.json / examples        -- yours, done before running this
    2  publish the folder                 -- served locally by --serve
    3  generate model.yaml                -- 10_model.yaml_v10.py
    4  move model.yaml into the folder    -- done here
    5  generate spec.md                   -- 20_create_spec_v11.0.py
    6  copy spec.md into <folder>/doc     -- done here
    7  generate context.jsonld            -- 25_create_subject_context_V7.py
    8  rewrite property URLs              -- update_urls_to_show_smart_data_model.py

Usage:
    python3 build_data_model.py ../openCallSpecific/yeast/YeastBatch
    python3 build_data_model.py ../material/leather --steps yaml,context
    python3 build_data_model.py ../material/leather --base-url https://raw.githubusercontent.com/<org>/<repo>/main/material/leather/
    python3 build_data_model.py --all ../openCallSpecific/islopol

Run from the utils directory (the scripts resolve ./credentials.json and
./datamodels_to_publish.json relative to the working directory).
"""
import argparse
import functools
import http.server
import json
import os
import re
import shutil
import socket
import socketserver
import subprocess
import sys
import tempfile
import threading

UTILS = os.path.dirname(os.path.abspath(__file__))
PUBLISH_CONFIG = os.path.join(UTILS, "datamodels_to_publish.json")

# script -> (filename, regex matching the hardcoded line, replacement template)
# The regex is anchored at line start so the commented-out example URLs above
# each assignment are left alone.
STEPS = {
    "yaml": {
        "script": "10_model.yaml_v10.py",
        "pattern": re.compile(r'^schemaUrl\s*=.*$', re.M),
        "replace": 'schemaUrl="{base}schema.json"',
        "produces": "model.yaml",
        "dest": ".",
        "readme": "step 3-4",
    },
    "spec": {
        "script": "20_create_spec_v11.0.py",
        "pattern": re.compile(r'^customRepository\s*=.*$', re.M),
        "replace": 'customRepository="{base}"',
        "produces": "spec.md",
        "dest": "doc",
        "readme": "step 5-6",
    },
    "context": {
        "script": "25_create_subject_context_V7.py",
        "pattern": re.compile(r'^customRepository\s*=.*$', re.M),
        "replace": 'customRepository="{base}"',
        "produces": "context.jsonld",
        "dest": ".",
        "readme": "step 7",
    },
    "urls": {
        "script": "update_urls_to_show_smart_data_model.py",
        "pattern": None,          # no hardcoded URL to patch
        "produces": "new_data_model.jsonld",
        # It reads ./context.jsonld from utils/ and rewrites each property URL,
        # so its output is the final context for the model folder.
        "needs": "context.jsonld",
        "install_as": "context.jsonld",
        "dest": ".",
        "readme": "step 8",
    },
}
ORDER = ["yaml", "spec", "context", "urls"]


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(directory, port):
    """Serve `directory` on `port`; returns (httpd, actual_port). Port 0 picks a free one."""
    handler = functools.partial(QuietHandler, directory=directory)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", port), handler)
    actual = httpd.socket.getsockname()[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, actual


def port_is_free(port):
    with socket.socket() as s:
        try:
            s.bind(("127.0.0.1", port))
            return True
        except OSError:
            return False


def patch_script(name, base_url):
    """Copy a script into utils/ with its hardcoded URL replaced. Returns the temp path."""
    step = STEPS[name]
    src = os.path.join(UTILS, step["script"])
    source = open(src).read()

    if step["pattern"] is not None:
        replacement = step["replace"].format(base=base_url)
        source, hits = step["pattern"].subn(replacement.replace("\\", "\\\\"), source)
        if hits == 0:
            raise SystemExit(
                f"{step['script']}: no line matching {step['pattern'].pattern!r}. "
                "The script changed; update STEPS in this driver."
            )

    # Written into utils/ so the script's relative paths (./credentials.json,
    # ./datamodels_to_publish.json, fiware-context.jsonld) still resolve.
    fd, tmp = tempfile.mkstemp(prefix=f"_auto_{name}_", suffix=".py", dir=UTILS)
    with os.fdopen(fd, "w") as f:
        f.write(source)
    return tmp


def run_step(name, base_url, model_dir, dry_run):
    step = STEPS[name]
    produced = os.path.join(UTILS, step["produces"])
    if os.path.exists(produced):
        os.remove(produced)

    # Some scripts read a file an earlier step already filed into the model
    # folder; stage it back into utils/ where the script expects to find it.
    staged = None
    needs = step.get("needs")
    if needs and not dry_run:
        have = os.path.join(model_dir, needs)
        if not os.path.exists(have):
            print(f"  [{name}] skipped: needs {needs}, which no earlier step produced")
            return True
        staged = os.path.join(UTILS, needs)
        if not os.path.exists(staged):
            shutil.copy(have, staged)
        else:
            staged = None

    tmp = patch_script(name, base_url)
    try:
        if dry_run:
            line = [l for l in open(tmp) if l.startswith(("schemaUrl", "customRepository"))]
            print(f"  [{name}] would run {step['script']} with {''.join(line).strip() or '(no URL to patch)'}")
            return True

        proc = subprocess.run([sys.executable, os.path.basename(tmp)],
                              cwd=UTILS, capture_output=True, text=True)
        if proc.returncode != 0:
            tail = (proc.stderr or proc.stdout).strip().splitlines()[-4:]
            print(f"  [{name}] FAILED ({step['script']}, exit {proc.returncode})")
            for l in tail:
                print(f"        {l}")
            return False

        if not os.path.exists(produced):
            print(f"  [{name}] ran but produced no {step['produces']}")
            tail = (proc.stdout or "").strip().splitlines()[-3:]
            for l in tail:
                print(f"        {l}")
            return False

        dest_dir = os.path.join(model_dir, step["dest"])
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, step.get("install_as", step["produces"]))
        shutil.move(produced, dest)
        label = step["produces"]
        if step.get("install_as"):
            label += f" as {step['install_as']}"
        print(f"  [{name}] {label} -> {os.path.relpath(dest)}  ({step['readme']})")
        return True
    finally:
        os.remove(tmp)
        if staged and os.path.exists(staged):
            os.remove(staged)


def entity_name(model_dir):
    """NGSI type declared by the schema, used to name the generated artefacts."""
    schema = json.load(open(os.path.join(model_dir, "schema.json")))
    for branch in schema.get("allOf", []):
        enum = branch.get("properties", {}).get("type", {}).get("enum")
        if enum:
            return enum[0]
    enum = schema.get("properties", {}).get("type", {}).get("enum")
    if enum:
        return enum[0]
    return os.path.basename(model_dir)


class publish_config:
    """Point datamodels_to_publish.json at one entity, then restore it.

    The generator scripts read the entity name from this file; it ships
    hardcoded to "leather", which would otherwise label every artefact.
    """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.original = open(PUBLISH_CONFIG).read()
        cfg = json.loads(self.original)
        cfg["dataModels"] = [self.name]
        with open(PUBLISH_CONFIG, "w") as f:
            json.dump(cfg, f, indent=4)
        return self

    def __exit__(self, *exc):
        with open(PUBLISH_CONFIG, "w") as f:
            f.write(self.original)


def model_dirs(target, recurse):
    """A model folder is one containing schema.json."""
    target = os.path.abspath(target)
    if os.path.isfile(os.path.join(target, "schema.json")):
        return [target]
    if not recurse:
        raise SystemExit(f"{target}: no schema.json here. Use --all to walk subfolders.")
    found = sorted(
        os.path.dirname(p)
        for p in (os.path.join(r, "schema.json") for r, _, fs in os.walk(target) for _ in [0])
        if os.path.exists(p)
    )
    if not found:
        raise SystemExit(f"{target}: no schema.json found in any subfolder.")
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("model", help="folder holding schema.json (or a parent, with --all)")
    ap.add_argument("--all", action="store_true", help="process every schema.json under the folder")
    ap.add_argument("--steps", default=",".join(ORDER),
                    help=f"comma-separated subset of: {','.join(ORDER)}")
    ap.add_argument("--base-url", help="published URL of the model folder; default serves it locally")
    ap.add_argument("--port", type=int, default=8085, help="local server port (default 8085, as in docker-compose.yml)")
    ap.add_argument("--dry-run", action="store_true", help="show what would run, change nothing")
    args = ap.parse_args()

    steps = [s.strip() for s in args.steps.split(",") if s.strip()]
    unknown = [s for s in steps if s not in STEPS]
    if unknown:
        raise SystemExit(f"unknown step(s): {', '.join(unknown)}. Known: {', '.join(ORDER)}")
    steps = [s for s in ORDER if s in steps]

    targets = model_dirs(args.model, args.all)
    print(f"{len(targets)} model folder(s); steps: {', '.join(steps)}")

    failures = []
    for model_dir in targets:
        rel = os.path.relpath(model_dir)
        print(f"\n== {rel}")

        httpd = None
        if args.base_url:
            base = args.base_url if args.base_url.endswith("/") else args.base_url + "/"
        else:
            port = args.port
            if not port_is_free(port):
                print(f"  port {port} busy (docker-compose nginx?); picking a free port")
                port = 0
            httpd, port = serve(model_dir, port)
            base = f"http://127.0.0.1:{port}/"
            print(f"  serving {rel} at {base}")

        entity = entity_name(model_dir)
        print(f"  entity name: {entity}")
        try:
            if args.dry_run:
                for name in steps:
                    run_step(name, base, model_dir, True)
            else:
                with publish_config(entity):
                    for name in steps:
                        if not run_step(name, base, model_dir, False):
                            failures.append(f"{rel}:{name}")
        finally:
            if httpd:
                httpd.shutdown()
                httpd.server_close()

    print()
    if failures:
        print(f"FAILED: {len(failures)} step(s): {', '.join(failures)}")
        return 1
    print("all steps completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
