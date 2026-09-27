#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""
@file build_index.py
@brief ELI5: scans the content library's folders, collects every preset, kit,
       sample, loop, and demo project, and writes a tidy, searchable index.json
       catalog. Also checks that every asset has an entry in CONTENT_LICENSES.md.

Usage:
    python tools/build_index.py          # Builds and writes index.json
    python tools/build_index.py --check  # Verifies index.json is up-to-date and valid (CI mode)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Categories recognized in the library
CATEGORIES: Tuple[str, ...] = (
    "presets",
    "kits",
    "one-shots",
    "loops",
    "demo-projects",
)

# Supported content file extensions
CONTENT_EXTENSIONS: Set[str] = {
    ".nebpatch",
    ".nebpreset",
    ".nebkit",
    ".nebproj",
    ".nebz",
    ".wav",
}


def get_repo_root() -> Path:
    """ELI5: returns the repository root directory (one level above tools/)."""
    return Path(__file__).resolve().parent.parent


def parse_asset_ledger(ledger_path: Path) -> Set[str]:
    """
    ELI5: reads CONTENT_LICENSES.md and extracts the list of audited asset file paths
    from the markdown table.
    """
    if not ledger_path.is_file():
        return set()

    recorded_paths: Set[str] = set()
    content = ledger_path.read_text(encoding="utf-8")
    table_pattern = re.compile(r"^\|\s*`([^`]+)`\s*\|", re.MULTILINE)
    for match in table_pattern.finditer(content):
        raw_path = match.group(1).strip().replace("\\", "/")
        recorded_paths.add(raw_path)

    return recorded_paths


def scan_category(repo_root: Path, category: str) -> Dict[str, Dict[str, Any]]:
    """
    ELI5: walks one category directory (e.g. presets/) and builds a dictionary
    of item metadata.
    """
    cat_dir = repo_root / category
    if not cat_dir.is_dir():
        return {}

    items: Dict[str, Dict[str, Any]] = {}

    for root, _, files in os.walk(cat_dir):
        for fname in sorted(files):
            file_path = Path(root) / fname
            suffix = file_path.suffix.lower()

            if suffix not in CONTENT_EXTENSIONS:
                continue

            rel_path = file_path.relative_to(repo_root).as_posix()
            item_key = file_path.stem

            name = item_key.replace("_", " ").title()
            license_str = "CC0-1.0"
            tags: List[str] = [category.rstrip("s")]

            # Inspect JSON files for embedded metadata
            if suffix in {".nebpatch", ".nebpreset", ".nebkit", ".nebproj"}:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    if isinstance(data, dict):
                        if "name" in data and isinstance(data["name"], str):
                            name = data["name"]
                        if "license" in data and isinstance(data["license"], str):
                            license_str = data["license"]
                        if "tags" in data and isinstance(data["tags"], list):
                            for tag in data["tags"]:
                                if isinstance(tag, str) and tag not in tags:
                                    tags.append(tag.lower())

                        if "_placeholder_notice" in data or "sample_" in item_key or "[SAMPLE]" in name:
                            if "sample" not in tags:
                                tags.append("sample")
                            if "placeholder" not in tags:
                                tags.append("placeholder")

                        if "category" in data and isinstance(data["category"], str):
                            cat_tag = data["category"].lower()
                            if cat_tag not in tags:
                                tags.append(cat_tag)
                except Exception as exc:
                    print(f"Warning: could not parse JSON in {rel_path}: {exc}", file=sys.stderr)

            # Audio files metadata deduction
            elif suffix == ".wav":
                if "sample_" in item_key or "placeholder" in item_key:
                    tags.extend(["sample", "placeholder"])
                # Extract BPM if present in filename, e.g. 120bpm
                bpm_match = re.search(r"(\d+)bpm", item_key, re.IGNORECASE)
                if bpm_match:
                    tags.append(f"{bpm_match.group(1)}bpm")

            # Clean and deduplicate tags while preserving order
            cleaned_tags: List[str] = []
            for t in tags:
                t_clean = t.strip().lower()
                if t_clean and t_clean not in cleaned_tags:
                    cleaned_tags.append(t_clean)

            items[item_key] = {
                "files": [rel_path],
                "license": license_str,
                "name": name,
                "tags": sorted(cleaned_tags),
            }

    # Sort items deterministically by key
    return {k: items[k] for k in sorted(items.keys())}


def build_index_data(repo_root: Path) -> Dict[str, Dict[str, Any]]:
    """
    ELI5: assembles the complete index data across all library categories.
    Returns: category -> item_key -> {name, license, tags, files}.
    """
    index: Dict[str, Dict[str, Any]] = {}
    for cat in CATEGORIES:
        index[cat] = scan_category(repo_root, cat)
    return index


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Build or verify the Nebula Content Library machine-readable index.json."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check whether index.json is up-to-date and all assets are recorded in CONTENT_LICENSES.md without modifying files.",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        default=True,
        help="Write updated index.json to repository root (default action if --check is not specified).",
    )
    args = parser.parse_args()

    repo_root = get_repo_root()
    index_file = repo_root / "index.json"
    licenses_file = repo_root / "CONTENT_LICENSES.md"

    generated_index = build_index_data(repo_root)
    generated_text = json.dumps(generated_index, indent=2, sort_keys=True) + "\n"

    # 1. Audit ledger check
    recorded_assets = parse_asset_ledger(licenses_file)
    unrecorded_assets: List[str] = []

    for cat, items in generated_index.items():
        for item_key, item_data in items.items():
            for fpath in item_data.get("files", []):
                if fpath not in recorded_assets:
                    unrecorded_assets.append(fpath)

    if unrecorded_assets:
        print("ERROR: The following assets are not recorded in CONTENT_LICENSES.md:", file=sys.stderr)
        for missing in sorted(unrecorded_assets):
            print(f"  - {missing}", file=sys.stderr)
        if args.check:
            return 1

    # 2. Check mode
    if args.check:
        if not index_file.is_file():
            print(f"ERROR: {index_file} does not exist. Run python tools/build_index.py to create it.", file=sys.stderr)
            return 1

        existing_text = index_file.read_text(encoding="utf-8")
        if existing_text != generated_text:
            print("ERROR: index.json is out of date. Run python tools/build_index.py to update it.", file=sys.stderr)
            return 1

        print("OK: index.json is up to date and all assets are audited in CONTENT_LICENSES.md.")
        return 0

    # 3. Write mode
    index_file.write_text(generated_text, encoding="utf-8")
    print(f"Successfully generated {index_file.relative_to(repo_root)}.")
    total_items = sum(len(items) for items in generated_index.values())
    print(f"Total items indexed: {total_items}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
