#!/usr/bin/env python3
"""Align data model folders with the Smart Data Models contribution manual, so
they pass the official validator (smart-data-models/data-models test_data_model).

For each folder holding schema.json and examples/example-normalized.jsonld:
  1. schema.json: $schema set to draft 2020-12; every NGSI-LD definition
     ({type: Property|Relationship|GeoProperty, value|object}) becomes
     anyOf [keyValues form, normalized form], so both payload shapes validate.
     QuantityProperty ranges move inside value: {"value": {"minValue", "maxValue"}}.
  2. examples/example-normalized.jsonld: an unreachable @context (internal host,
     placeholder or missing) is replaced by the public platform context, and
     minValue/maxValue are moved inside value.
  3. examples/example.json (NGSI-v2 keyValues), example.jsonld (NGSI-LD
     keyValues) and example-normalized.json (NGSI-v2 normalized) are derived
     from example-normalized.jsonld.
  4. notes.yaml and ADOPTERS.yaml stubs are added when missing.

Safe to rerun: every step is idempotent.

Usage:
    python3 sdm_align.py ../openCallSpecific/ecoffee/ECoffeeObservation
    python3 sdm_align.py --all ..
"""
import argparse
import copy
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_RAW = "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/"
PLATFORM_CONTEXT = [
    REPO_RAW + "utils/circuloos_data_platform.jsonld",
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld",
]
UNREACHABLE_CONTEXT = ("circuloos-ld-context", "TOBELater")
SCHEMA_DRAFT = "https://json-schema.org/draft/2020-12/schema"
NGSI_TYPES = {"Property", "Relationship", "GeoProperty"}
DATE_TIME = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
RANGE_KEYS = ("minValue", "maxValue")

NOTES = "notesReadme: []\nnotesSpec: []\nnotesContext: []\n"
ADOPTERS = """currentAdopters:
  - adopter: CIRCULOOS
    description: CIRCULOOS circular economy data platform
    mail: ''
    organization: CIRCULOOS consortium
    project: CIRCULOOS (Horizon Europe, grant agreement No. 101092295)
    comments: ''
    startDate: ''
"""


def load(path):
    """Return (data, indent, trailing newline) so files are rewritten in their own style."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"\n( +)\S", text)
    return json.loads(text), len(m.group(1)) if m else 2, text.endswith("\n")


def save(path, data, indent=2, newline=True):
    text = json.dumps(data, indent=indent, ensure_ascii=False) + ("\n" if newline else "")
    try:
        with open(path, encoding="utf-8") as f:
            if f.read() == text:
                return False
    except FileNotFoundError:
        pass
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True


def ngsi_type(definition):
    return set(definition.get("properties", {}).get("type", {}).get("enum", [])) & NGSI_TYPES


def align_definition(d):
    """Normalized-only definition -> anyOf [keyValues, normalized]. Already aligned ones pass through."""
    if not ngsi_type(d):
        return d
    props = d["properties"]
    if any(k in props for k in RANGE_KEYS):
        bounds = {k: props.pop(k) for k in RANGE_KEYS if k in props}
        d.pop("anyOf", None)  # the old "one of value/minValue/maxValue is required" rule
        d["required"] = list(dict.fromkeys(d.get("required", []) + ["value"]))
        exact = props.get("value", {"type": "number"})
        props["value"] = {
            "description": "Exact value as a number, or a range as an object with minValue and/or maxValue.",
            "anyOf": [
                exact,
                {"type": "object", "properties": bounds, "minProperties": 1, "additionalProperties": False},
            ],
        }
    key_values = copy.deepcopy(props["object"] if "object" in props else props["value"])
    return {"anyOf": [key_values, d]}


def align_schema(path):
    schema, indent, nl = load(path)
    schema["$schema"] = SCHEMA_DRAFT
    for name, d in schema.get("definitions", {}).items():
        schema["definitions"][name] = align_definition(d)
    return save(path, schema, indent, nl), schema


def top_properties(schema):
    """Attribute schemas from the model's own properties and allOf branches (local $refs to CIRCULOOS files included)."""
    props = dict(schema.get("properties", {}))
    for part in schema.get("allOf", []):
        ref = part.get("$ref", "")
        if ref.startswith(REPO_RAW):
            file, _, pointer = ref[len(REPO_RAW):].partition("#")
            target = json.load(open(os.path.join(REPO, file), encoding="utf-8"))
            for key in filter(None, pointer.split("/")):
                target = target[key]
            part = target
        props.update(top_properties(part))
    return props


def key_value(attr, prop):
    t = attr.get("type")
    if t == "Relationship":
        return attr["object"]
    if t == "LanguageProperty":
        return attr["languageMap"]
    if t == "ListProperty":
        return attr["valueList"]
    if prop.get("type") == "object" and "value" in prop.get("properties", {}):
        # material/ convention: measured values keep their unit, {value, unitCode}
        return {k: attr[k] for k in ("value", "unitCode") if k in attr}
    return attr["value"]


def v2_type(value):
    if isinstance(value, bool):
        return "Boolean"
    if isinstance(value, (int, float)):
        return "Number"
    if isinstance(value, str):
        return "DateTime" if DATE_TIME.match(value) else "Text"
    return "StructuredValue"


def v2_attribute(attr):
    t = attr.get("type")
    # NGSI-v2 has no Relationship type (the SDM validator rejects it): a link is a URN Text, or a list of them
    value = attr["object"] if t == "Relationship" else attr.get("value", attr.get("languageMap"))
    out = {"type": "geo:json" if t == "GeoProperty" else v2_type(value), "value": value}
    metadata = {}
    for k, v in attr.items():
        if k in ("type", "value", "object", "languageMap"):
            continue
        v = v.get("value", v) if isinstance(v, dict) else v
        metadata[k] = {"type": "DateTime" if k == "observedAt" else v2_type(v), "value": v}
    if metadata:
        out["metadata"] = metadata
    return out


def align_examples(folder, schema):
    path = os.path.join(folder, "examples", "example-normalized.jsonld")
    entity, indent, nl = load(path)
    context = entity.get("@context")
    if not context or any(u in json.dumps(context) for u in UNREACHABLE_CONTEXT):
        entity["@context"] = PLATFORM_CONTEXT
    for k, attr in entity.items():
        if isinstance(attr, dict) and "value" not in attr and any(r in attr for r in RANGE_KEYS):
            rest = {k2: v for k2, v in attr.items() if k2 not in RANGE_KEYS}
            entity[k] = {"type": rest.pop("type", "Property"), "value": {r: attr[r] for r in RANGE_KEYS if r in attr}, **rest}
    changed = [save(path, entity, indent, nl)]

    props = top_properties(schema)
    head = {"id": entity["id"], "type": entity["type"]}
    attrs = {k: v for k, v in entity.items() if k not in ("id", "type", "@context")}
    kv = {**head, **{k: key_value(v, props.get(k, {})) for k, v in attrs.items()}}
    examples = os.path.join(folder, "examples")
    changed.append(save(os.path.join(examples, "example.json"), kv))
    changed.append(save(os.path.join(examples, "example.jsonld"), {**kv, "@context": entity["@context"]}))
    changed.append(save(os.path.join(examples, "example-normalized.json"),
                        {**head, **{k: v2_attribute(v) for k, v in attrs.items()}}))
    return any(changed)


def add_stubs(folder):
    added = False
    for name, text in (("notes.yaml", NOTES), ("ADOPTERS.yaml", ADOPTERS)):
        path = os.path.join(folder, name)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            added = True
    return added


def align(folder):
    schema_changed, schema = align_schema(os.path.join(folder, "schema.json"))
    examples_changed = align_examples(folder, schema)
    stubs_added = add_stubs(folder)
    print(f"{os.path.relpath(folder, REPO)}: schema {'updated' if schema_changed else 'ok'}, "
          f"examples {'updated' if examples_changed else 'ok'}, stubs {'added' if stubs_added else 'ok'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folders", nargs="+", help="model folder(s), or a root with --all")
    ap.add_argument("--all", action="store_true", help="process every model folder under the given root(s)")
    args = ap.parse_args()
    folders = args.folders
    if args.all:
        folders = sorted(
            dirpath for root in args.folders for dirpath, _, files in os.walk(root)
            if "schema.json" in files and os.path.exists(os.path.join(dirpath, "examples", "example-normalized.jsonld"))
        )
    for folder in folders:
        align(os.path.abspath(folder))


if __name__ == "__main__":
    main()
