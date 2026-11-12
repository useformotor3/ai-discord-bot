#!/usr/bin/env python3
"""Extract review candidates from CRA research archives. This is NOT a legal verifier.
The generated report is committed to the working branch by its dedicated workflow."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

URL_RE = re.compile(r"https?://\S+", re.I)
ARTICLE_RE = re.compile(r"\bArticles?\s+\d+(?:\s*\(\s*\d+\s*\))?(?:\s*(?:-|–|to)\s*\d+)?", re.I)
ANNEX_RE = re.compile(r"\bAnnex\s+[IVX]+(?:\s*,?\s*Part\s+[IVX]+)?(?:\s*,?\s*points?\s*\(?\d+\)?)?", re.I)
CLAIM_RE = re.compile(r"shall|must|required|obligat|mandatory|prohibit|무상|의무|필수|금지|반드시|제공해야|수립해야|구축해야|적용해야|신고해야|보고해야", re.I)
QUOTE_RE = re.compile(r"raw\s*text\s*quote|원문|직접\s*인용|인용문|source quote", re.I)

RISK_PATTERNS = {
    "SBOM_SCOPE_OVERSTATEMENT": r"(?:SBOM.{0,100}(?:모든|all|mandatory|의무|must|shall)|(?:모든|all).{0,80}SBOM)",
    "FREE_UPDATE_SEPARATION_OVERSTATEMENT": r"(?:(?:기능|feature).{0,50}(?:분리|separat).{0,80}(?:CRA|의무|shall|must)|(?:CRA|Annex).{0,100}(?:분리|separat).{0,60}(?:의무|shall|must))",
    "SUPPORT_PERIOD_FIXED_5Y": r"(?:최소\s*5년|minimum\s+of\s+5\s+years|at least\s+five\s+years)",
    "ARTICLE_13_8_SUPPORT": r"(?:Article\s*13\s*\(\s*8\s*\)|제13조.{0,15}제?8항)",
    "ARTICLE_14_REPORTING": r"(?:Article\s*14|제14조)",
    "ARTICLE_11_REPORTING_MISATTRIBUTION": r"(?:(?:report(?:ing)?|신고|보고).{0,80}Article\s*11|Article\s*11.{0,80}(?:report(?:ing)?|신고|보고))",
    "ANNEX_PART_CONFUSION": r"(?:Annex\s+II.{0,30}Vulnerability Handling|Annex\s+I.{0,30}Technical Documentation)",
    "SERVO_PRODUCT_CLASS_ASSERTION": r"(?:(?:Class\s*[I1]|Class\s*II|중요\s*제품|critical product).{0,120}(?:servo|서보|drive|드라이브))",
    "CRA_CERTIFICATION_MISCLAIM": r"(?:(?:CRA\s*)?(?:인증|certification).{0,70}(?:필수|mandatory|의무|must|shall))",
}
COMPILED_RISKS = {k: re.compile(v, re.I | re.S) for k, v in RISK_PATTERNS.items()}

def extract_file(path: Path, root: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    lines = text.splitlines()
    title = next((x.lstrip("# ").strip() for x in lines if x.startswith("#")), "")
    # Keep legacy string arrays for compatibility, and add line-addressable records.
    paragraph_records = []
    cursor = 0
    for block in re.split(r"\n\s*\n", text):
        start = text.find(block, cursor)
        end = start + len(block)
        cursor = end
        if CLAIM_RE.search(block) and len(block.strip()) > 60:
            paragraph_records.append({
                "line_start": text.count("\n", 0, start) + 1,
                "line_end": text.count("\n", 0, end) + 1,
                "text": block.strip()[:1800],
            })
    claims = [item["text"] for item in paragraph_records[:20]]
    quote_records = []
    for item in paragraph_records:
        if QUOTE_RE.search(item["text"]):
            quote_records.append(item)
    quotes = [item["text"][:1500] for item in quote_records[:10]]
    # Source sections often contain only a long document title and no canonical URL.
    source_sections = []
    for i, line in enumerate(lines):
        if re.search(r"(?:source|출처\s*자료|참고\s*자료|references?)", line, re.I):
            section = [line.strip()]
            for following in lines[i + 1:i + 9]:
                if re.match(r"^\s*(?:#{1,6}\s+|\*\*\d+\.|\d+\.)", following):
                    break
                if following.strip():
                    section.append(following.strip())
            source_sections.append("\n".join(section)[:1800])
    urls = sorted({u.rstrip(".,;:'\"") for u in URL_RE.findall(text)})
    articles = sorted(set(ARTICLE_RE.findall(text)), key=str.lower)
    annexes = sorted(set(ANNEX_RE.findall(text)), key=str.lower)
    flags = [k for k, rx in COMPILED_RISKS.items() if rx.search(text)]
    risk_evidence = {}
    for name, rx in COMPILED_RISKS.items():
        matches = []
        for match in rx.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            snippet = text[max(0, match.start() - 160):min(len(text), match.end() + 160)].replace("\n", " ")
            matches.append({"line": line_no, "snippet": snippet[:500]})
            if len(matches) == 3:
                break
        if matches:
            risk_evidence[name] = matches
    date_match = re.search(r"(?:Date|날짜)\s*[:：]\s*([^\n]+)", text, re.I)
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "title": title[:300],
        "date_candidate": date_match.group(1).strip() if date_match else None,
        "article_reference_candidates": articles,
        "annex_reference_candidates": annexes,
        "source_url_candidates": urls,
        "source_section_candidates": source_sections[:10],
        "source_section_count": len(source_sections),
        "claim_candidates": claims,
        "claim_candidate_records": paragraph_records[:20],
        "quote_section_candidates": quotes,
        "quote_candidate_records": quote_records[:10],
        "heuristic_risk_evidence": risk_evidence,
        "heuristic_risk_flags": flags,
        "verification_status": "UNVERIFIED_AI_ARCHIVE",
    }

def build(root: Path) -> dict:
    root = root.resolve()
    archive = root / "research_archive"
    if not archive.is_dir():
        raise FileNotFoundError("research_archive directory not found")
    files = sorted(p for p in archive.rglob("*.md") if p.is_file())
    records = [extract_file(p, root) for p in files]
    counts = Counter(flag for record in records for flag in record["heuristic_risk_flags"])
    return {
        "schema_version": "1.1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_branch": os.environ.get("GITHUB_REF_NAME", "local"),
        "source_commit": os.environ.get("GITHUB_SHA"),
        "archive_file_count": len(records),
        "claim_candidate_block_count": sum(len(r["claim_candidates"]) for r in records),
        "source_url_candidate_count": sum(len(r["source_url_candidates"]) for r in records),
        "article_reference_candidate_count": sum(len(r["article_reference_candidates"]) for r in records),
        "heuristic_risk_flag_file_counts": dict(sorted(counts.items())),
        "limitations": [
            "This is heuristic extraction, not legal or factual verification.",
            "A URL candidate does not prove reachability, authority, currency, or support for the adjacent claim.",
            "Article/Annex strings are candidates; exact paragraph and legal context require primary-source review.",
            "Direct-quote candidates are not authenticated quotations until compared with the cited original.",
            "Source sections are extracted heuristically; a document title is not a canonical source URL.",
            "Claim and risk snippets include approximate source line numbers for human review.",
            "Every record remains UNVERIFIED_AI_ARCHIVE.",
        ],
        "records": records,
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = build(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
