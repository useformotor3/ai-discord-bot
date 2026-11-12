#!/usr/bin/env python3
"""Extract review candidates from CRA research archives. This is NOT a legal verifier."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

URL_RE = re.compile(r"https?://[^\\s<>\\])}]+", re.I)
ARTICLE_RE = re.compile(r"\\bArticles?\\s+\\d+(?:\\s*\\(\\s*\\d+\\s*\\))?(?:\\s*(?:-|–|to)\\s*\\d+)?", re.I)
ANNEX_RE = re.compile(r"\\bAnnex\\s+[IVX]+(?:\\s*,?\\s*Part\\s+[IVX]+)?(?:\\s*,?\\s*points?\\s*\\(?\\d+\\)?)?", re.I)
CLAIM_RE = re.compile(r"shall|must|required|obligat|mandatory|prohibit|무상|의무|필수|금지|반드시|제공해야|수립해야|구축해야|적용해야|신고해야|보고해야", re.I)
QUOTE_RE = re.compile(r"raw\\s*text\\s*quote|원문|직접\\s*인용|인용문|source quote", re.I)

RISK_PATTERNS = {
 "SBOM_SCOPE_OVERSTATEMENT": r"(?:SBOM.{0,100}(?:모든|all|mandatory|의무|must|shall)|(?:모든|all).{0,80}SBOM)",
 "FREE_UPDATE_SEPARATION_OVERSTATEMENT": r"(?:(?:기능|feature).{0,50}(?:분리|separat).{0,80}(?:CRA|의무|shall|must)|(?:CRA|Annex).{0,100}(?:분리|separat).{0,60}(?:의무|shall|must))",
 "SUPPORT_PERIOD_FIXED_5Y": r"(?:최소\\s*5년|minimum\\s+of\\s+5\\s+years|at least\\s+five\\s+years)",
 "ARTICLE_13_8_SUPPORT": r"(?:Article\\s*13\\s*\\(\\s*8\\s*\\)|제13조.{0,15}제?8항)",
 "ARTICLE_14_REPORTING": r"(?:Article\\s*14|제14조)",
 "ARTICLE_11_REPORTING_MISATTRIBUTION": r"(?:(?:report(?:ing)?|신고|보고).{0,80}Article\\s*11|Article\\s*11.{0,80}(?:report(?:ing)?|신고|보고))",
 "ANNEX_PART_CONFUSION": r"(?:Annex\\s+II.{0,30}Vulnerability Handling|Annex\\s+I.{0,30}Technical Documentation)",
 "SERVO_PRODUCT_CLASS_ASSERTION": r"(?:(?:Class\\s*[I1]|Class\\s*II|중요\\s*제품|critical product).{0,120}(?:servo|서보|drive|드라이브))",
 "CRA_CERTIFICATION_MISCLAIM": r"(?:(?:CRA\\s*)?(?:인증|certification).{0,70}(?:필수|mandatory|의무|must|shall))",
}
COMPILED_RISKS = {k: re.compile(v, re.I | re.S) for k,v in RISK_PATTERNS.items()}

def _unique(pattern, text):
    return sorted(set(pattern.findall(text)), key=str.lower)

def extract_file(path: Path, root: Path) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    blocks = [b.strip() for b in re.split(r"\\n\\s*\\n", text) if b.strip()]
    lines = text.splitlines()
    title = next((x.lstrip("# ").strip() for x in lines if x.startswith("#")), "")
    claims = [b[:1800] for b in blocks if CLAIM_RE.search(b) and len(b) > 60][:20]
    quotes = [b[:1500] for b in blocks if QUOTE_RE.search(b)][:10]
    urls = sorted({u.rstrip(".,;:'\\\"") for u in URL_RE.findall(text)})
    articles = _unique(ARTICLE_RE, text)
    annexes = _unique(ANNEX_RE, text)
    flags = [k for k,rx in COMPILED_RISKS.items() if rx.search(text)]
    return {
      "path": path.relative_to(root).as_posix(),
      "sha256": hashlib.sha256(raw).hexdigest(),
      "bytes": len(raw),
      "title": title[:300],
      "date_candidate": (re.search(r"(?:Date|날짜)\\s*[:：]\\s*([^\\n]+)", text, re.I).group(1).strip() if re.search(r"(?:Date|날짜)\\s*[:：]\\s*([^\\n]+)", text, re.I) else None),
      "article_reference_candidates": articles,
      "annex_reference_candidates": annexes,
      "source_url_candidates": urls,
      "claim_candidates": claims,
      "quote_section_candidates": quotes,
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
    counts = Counter(flag for r in records for flag in r["heuristic_risk_flags"])
    return {
      "schema_version": "1.0",
      "generated_at_utc": datetime.now(timezone.utc).isoformat(),
      "source_branch": __import__("os").environ.get("GITHUB_REF_NAME", "local"),
      "source_commit": __import__("os").environ.get("GITHUB_SHA"),
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
        "Every record remains UNVERIFIED_AI_ARCHIVE.",
      ],
      "records": records,
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path.cwd())
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    report = build(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in report.items() if k != "records"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
