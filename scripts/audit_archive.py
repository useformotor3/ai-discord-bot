#!/usr/bin/env python3
"""Audit research_archive Markdown files against history.json without modifying data."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def audit_repository(root: Path) -> dict[str, Any]:
    archive_dir = root / "research_archive"
    history_path = root / "history.json"
    state_path = root / "state.json"

    if not archive_dir.is_dir():
        raise FileNotFoundError(f"Missing archive directory: {archive_dir}")
    if not history_path.is_file():
        raise FileNotFoundError(f"Missing history file: {history_path}")

    archive_files = sorted(p for p in archive_dir.rglob("*.md") if p.is_file())
    archive_rel = [p.relative_to(root).as_posix() for p in archive_files]
    archive_set = set(archive_rel)

    history = load_json(history_path)
    if not isinstance(history, list):
        raise ValueError("history.json must contain a JSON array")

    history_paths: list[str] = []
    malformed_entries: list[int] = []
    for index, item in enumerate(history):
        if not isinstance(item, dict) or not isinstance(item.get("file"), str) or not item["file"].strip():
            malformed_entries.append(index)
            continue
        history_paths.append(item["file"].replace("\\", "/").removeprefix("./"))

    counts = Counter(history_paths)
    duplicate_history_paths = sorted(path for path, count in counts.items() if count > 1)
    history_set = set(history_paths)
    archive_missing_history = sorted(archive_set - history_set)
    history_orphans = sorted(history_set - archive_set)

    digest_groups: dict[str, list[str]] = defaultdict(list)
    for path in archive_files:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        digest_groups[digest].append(path.relative_to(root).as_posix())
    duplicate_content = [sorted(paths) for paths in digest_groups.values() if len(paths) > 1]

    state: dict[str, Any] | None = None
    state_warning = None
    if state_path.is_file():
        loaded_state = load_json(state_path)
        if isinstance(loaded_state, dict):
            state = loaded_state
            state_warning = (
                "state.count is treated as a daily counter, not an archive total; "
                "it is intentionally not compared with archive/history counts."
            )
        else:
            state_warning = "state.json exists but is not a JSON object."

    return {
        "archive_count": len(archive_rel),
        "history_entry_count": len(history),
        "history_valid_path_count": len(history_paths),
        "history_unique_path_count": len(history_set),
        "archive_missing_history": archive_missing_history,
        "history_orphans": history_orphans,
        "duplicate_history_paths": duplicate_history_paths,
        "malformed_history_entry_indexes": malformed_entries,
        "duplicate_content_groups": duplicate_content,
        "state": state,
        "state_warning": state_warning,
        "consistent": not any((archive_missing_history, history_orphans, duplicate_history_paths, malformed_entries)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root (default: current directory)")
    parser.add_argument("--json-out", type=Path, help="Optional path to write the JSON report")
    parser.add_argument("--strict", action="store_true", help="Exit with status 1 if archive/history paths are inconsistent")
    args = parser.parse_args()

    try:
        report = audit_repository(args.root.resolve())
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"AUDIT_ERROR: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered + "\n", encoding="utf-8")
    if args.strict and not report["consistent"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
