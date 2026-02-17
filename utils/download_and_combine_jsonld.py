#!/usr/bin/env python3
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


def sanitize_filename_from_url(url: str) -> str:
    parsed = urlparse(url)
    combined = f"{parsed.netloc}{parsed.path}"
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", combined).strip("_")
    if not sanitized.endswith(".jsonld"):
        sanitized = f"{sanitized}.jsonld"
    return sanitized


def load_context(source_path: Path):
    with source_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get("@context", data)


def combine_contexts(local_files: list[Path]) -> dict:
    combined = {}
    for local_file in local_files:
        context = load_context(local_file)
        if isinstance(context, dict):
            combined.update(context)
        elif isinstance(context, list):
            for item in context:
                if isinstance(item, dict):
                    combined.update(item)
    return {"@context": combined}


def download_file(url: str, destination: Path, timeout: int):
    request = urllib.request.Request(url, headers={"User-Agent": "CIRCULOOS-jsonld-downloader/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read()
    destination.write_bytes(raw)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download .jsonld files from a config JSON and combine them into a single JSON-LD file."
    )
    parser.add_argument(
        "--config",
        default=str(Path(__file__).parent / "merge_subjects_config.json"),
        help="Path to JSON config file with name -> URL mappings.",
    )
    parser.add_argument(
        "--download-dir",
        default=str(Path(__file__).parent / "downloaded_jsonld"),
        help="Folder where .jsonld files will be downloaded.",
    )
    parser.add_argument(
        "--output",
        default=str(Path(__file__).parent / "combined_subjects_context.jsonld"),
        help="Path of the combined JSON-LD output file.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Timeout in seconds for each download request.",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    download_dir = Path(args.download_dir)
    output_path = Path(args.output)

    if not config_path.exists():
        print(f"Config file not found: {config_path}")
        return 1

    with config_path.open("r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)

    if not isinstance(config_data, dict):
        print("Config format error: expected a JSON object with name -> URL mappings.")
        return 1

    download_dir.mkdir(parents=True, exist_ok=True)

    downloaded_files = []
    skipped_entries = []
    failed_entries = []

    for name, url in config_data.items():
        if not isinstance(url, str):
            skipped_entries.append((name, str(url), "non-string URL"))
            continue

        if not url.lower().endswith(".jsonld"):
            skipped_entries.append((name, url, "not a .jsonld URL"))
            continue

        filename = sanitize_filename_from_url(url)
        destination = download_dir / filename

        try:
            download_file(url, destination, args.timeout)
            downloaded_files.append(destination)
            print(f"Downloaded {name}: {url} -> {destination}")
        except Exception as exc:
            failed_entries.append((name, url, str(exc)))
            print(f"Failed {name}: {url} ({exc})")

    if not downloaded_files:
        print("No .jsonld files were downloaded successfully. Nothing to combine.")
        if skipped_entries:
            print(f"Skipped entries: {len(skipped_entries)}")
        if failed_entries:
            print(f"Failed entries: {len(failed_entries)}")
        return 1

    combined = combine_contexts(downloaded_files)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(combined, output_file, indent=2, ensure_ascii=False)
        output_file.write("\n")

    print("\nSummary")
    print(f"Downloaded files: {len(downloaded_files)}")
    print(f"Skipped entries: {len(skipped_entries)}")
    print(f"Failed entries: {len(failed_entries)}")
    print(f"Combined context written to: {output_path}")

    if skipped_entries:
        print("\nSkipped (first 10):")
        for name, url, reason in skipped_entries[:10]:
            print(f"- {name}: {url} ({reason})")

    if failed_entries:
        print("\nFailed (first 10):")
        for name, url, reason in failed_entries[:10]:
            print(f"- {name}: {url} ({reason})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
