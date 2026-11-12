#!/usr/bin/env python3
"""Build a heuristic inventory of CRA research archives; never treats AI text as verified."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

URL_RE = re.compile(r"https?://[^\s<>\])}]+", re.IGNORECASE)
ARTICLE_RE = re.compile(r"\bArticles?\s+\d+(?:\s*\(\s*\d+\s*\))?(?:\s*(?:-|–|to)\s*\d+)?", re.IGNORECASE)
ANNEX_RE = re.compile(r"\bAnnex\s+[IVX]+(?:\s*,?\s*Part\s+[IVX]+)?(?:\s*,?\s*points?\s*\(?\d+\)?)?", re.IGNORECASE)

TOPICS = {
    "sbom_supply_chain": ("sbom", "software bill of materials", "supply chain", "third-party component"),
    "vulnerability_handling": ("vulnerability", "coordinated vulnerability", "cvd", "security advisory", "disclosure"),
    "security_updates": ("security update", "free of charge", "firmware update", "patch", "secure update"),
    "product_scope_classification": ("important product", "class i", "class ii", "annex iii", "core functionality", "scope"),
    "risk_threat_model": ("risk assessment", "threat model", "attack surface", "risk analysis"),
    "secure_boot_hardware": ("secure boot", "debug", "root of trust", "key storage", "hardware security"),
    "identity_access_crypto": ("authentication", "access control", "cryptography", "encryption", "credential"),
    "incident_reporting": ("article 14", "actively exploited", "severe incident", "24 hours", "72 hours"),
    "technical_documentation": ("technical documentation", "annex vii", "conformity assessment", "declaration of conformity"),
    "support_lifecycle": ("support period", "expected lifetime", "article 13(8)", "end of support"),
    "standards_testing": ("harmonised standard", "harmonized standard", "testing", "penetration test", "etsi", "cen-cenelec"),
    "manufacturers_st_ti": ("stmicroelectronics", "stm32", "stm32", "texas instruments", "\bti\b"),
}


def clean_url(url: str) -> str:
    return url.rstrip(".,;:'\"")


def classify(text: str) -> list[str]:
    low = text.lower()
    found = []
    for topic, needles in TOPICS.items():
        if any((re.search(n, low) if n.startswith("\\b") else n in low) for n in needles):
            found.append(topic)
    return found or ["unclassified"]


def inventory(root: Path) -> dict[str, Any]:
    archive = root / "research_archive"
    history_path = root / "history.json"
    if not archive.is_dir() or not history_path.is_file():
        raise FileNotFoundError("Expected research_archive/ and history.json in repository root")

    history = json.loads(history_path.read_text(encoding="utf-8"))
    history_by_file = {}
    for item in history if isinstance(history, list) else []:
        if isinstance(item, dict) and isinstance(item.get("file"), str):
            history_by_file[item["file"].replace("\\", "/").removeprefix("./")] = item

    records = []
    topic_counts: Counter[str] = Counter()
    for path in sorted(p for p in archive.rglob("*.md") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        content = path.read_text(encoding="utf-8", errors="replace")
        lines = content.splitlines()
        title = next((line.lstrip("# ").strip() for line in lines if line.startswith("#")), "")
        headings = [line.lstrip("# ").strip() for line in lines if re.match(r"^#{1,6}\s+", line)][:30]
        urls = sorted({clean_url(x) for x in URL_RE.findall(content)})
        articles = sorted({m.group(0) for m in ARTICLE_RE.finditer(content)}, key=str.lower)
        annexes = sorted({m.group(0) for m in ANNEX_RE.finditer(content)}, key=str.lower)
        topics = classify(content)
        topic_counts.update(topics)
        history_item = history_by_file.get(rel, {})
        records.append({
            "path": rel,
            "filename_date_prefix": path.stem[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", path.stem) else None,
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "title": title,
            "headings": headings,
            "topic_candidates": topics,
            "article_reference_candidates": articles,
            "annex_reference_candidates": annexes,
            "source_url_candidates": urls,
            "history_date": history_item.get("date"),
            "history_time": history_item.get("time"),
            "history_count": history_item.get("count"),
            "verification_status": "UNVERIFIED_AI_ARCHIVE",
        })

    return {
        "schema_version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository_root": str(root),
        "archive_file_count": len(records),
        "history_entry_count": len(history) if isinstance(history, list) else None,
        "topic_candidate_counts": dict(sorted(topic_counts.items())),
        "records": records,
        "limitations": [
            "Keyword topics, article references, URLs and headings are heuristic candidates only.",
            "This inventory does not verify legal accuracy, source authority, URL reachability or quotation fidelity.",
            "Every source record remains UNVERIFIED_AI_ARCHIVE until reviewed against the cited primary source.",
            "One file may be counted in multiple topic categories."
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    report = inventory(args.root.resolve())
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
