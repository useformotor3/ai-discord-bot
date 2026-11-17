"""Official-source retrieval and conservative validation for CRA research drafts."""
from html.parser import HTMLParser
import re
from urllib.parse import urlparse

import requests


CRA_SOURCE_URL = (
    "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120"
)
SOURCE_TIMEOUT = (3.05, 20)


class _VisibleText(HTMLParser):
    """Extract visible text while ignoring scripts, styles, and navigation noise."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data):
        if not self.hidden_depth:
            value = data.strip()
            if value:
                self.parts.append(value)


def normalize_source_text(value):
    """Normalize whitespace only; preserve words and punctuation for quote matching."""
    return re.sub(r"\s+", " ", str(value or "")).strip()


def fetch_official_cra_source():
    """Fetch the official EUR-Lex act directly; no paid search-grounding service."""
    response = requests.get(
        CRA_SOURCE_URL,
        headers={"User-Agent": "CRA-Research-Bot/1.0 (+https://eur-lex.europa.eu/)"},
        timeout=SOURCE_TIMEOUT,
    )
    response.raise_for_status()
    final_url = getattr(response, "url", CRA_SOURCE_URL)
    parsed_url = urlparse(final_url)
    if parsed_url.scheme != "https" or parsed_url.hostname != "eur-lex.europa.eu":
        raise RuntimeError("EUR-Lex 이외의 도메인으로 리디렉션되어 원문 수집을 중단합니다.")
    parser = _VisibleText()
    parser.feed(response.text)
    source_text = normalize_source_text(" ".join(parser.parts))
    if len(source_text) < 10000:
        raise RuntimeError("EUR-Lex 응답이 비어 있거나 공식 법령 본문으로 보기에는 너무 짧습니다.")
    return {"url": CRA_SOURCE_URL, "text": source_text}


def validate_research_report(report, source):
    """Check structure, official URL, clause locator, and one verbatim source excerpt.

    This is a minimum provenance gate, not a full legal or semantic correctness review.
    """
    if not isinstance(report, str):
        return False, "응답이 문자열이 아닙니다."
    if not isinstance(source, dict) or not source.get("text") or not source.get("url"):
        return False, "검증 가능한 공식 원문이 없습니다."

    text = report.strip()
    lowered = text.lower()
    if len(text) < 250:
        return False, "응답 길이가 최소 기준(250자)에 미달합니다."

    required_sections = (
        ("주제 요약",),
        ("규격 근거", "상세 내용"),
        ("출처 자료", "source:"),
        ("출처 원문", "raw text quote"),
    )
    for alternatives in required_sections:
        if not any(marker in lowered for marker in alternatives):
            return False, f"필수 보고서 항목 누락: {' / '.join(alternatives)}"

    if source["url"] not in text:
        return False, "출처 자료에 수집한 EUR-Lex 공식 URL이 없습니다."

    source_text = normalize_source_text(source["text"]).casefold()
    article_refs = re.findall(r"\bArticle\s+\d+\b", text, flags=re.IGNORECASE)
    annex_refs = re.findall(r"\bAnnex\s+[IVX]+\b", text, flags=re.IGNORECASE)
    if not article_refs and not annex_refs:
        return False, "확인 가능한 CRA Article 또는 Annex 번호가 없습니다."
    if article_refs and not any(ref.casefold() in source_text for ref in article_refs):
        return False, "보고서의 Article 번호가 수집한 공식 원문에서 확인되지 않습니다."
    if annex_refs and not any(ref.casefold() in source_text for ref in annex_refs):
        return False, "보고서의 Annex 번호가 수집한 공식 원문에서 확인되지 않습니다."

    quote_match = re.search(
        r"출처 원문(?: 텍스트)?\s*(?:\(raw text quote\))?\s*[:：]?\s*(?:\n|$)(.*)$",
        text, flags=re.IGNORECASE | re.DOTALL,
    )
    if not quote_match:
        return False, "원문 인용 구역을 구분할 수 없습니다."
    quote_text = quote_match.group(1)
    quoted = re.findall(r"“([^”]{50,})”|\"([^\"]{50,})\"", quote_text)
    quote_candidates = [part for match in quoted for part in match if part]
    if not quote_candidates:
        return False, "50자 이상의 직접 인용문이 큰따옴표로 표시되지 않았습니다."
    if not any(normalize_source_text(candidate).casefold() in source_text for candidate in quote_candidates):
        return False, "보고서의 직접 인용문이 수집한 EUR-Lex 원문과 일치하지 않습니다."

    error_markers = (
        "시스템 긴급 경고", "모든 ai 모델", "temporarily unavailable",
        "quota exceeded", "rate limit exceeded", "internal server error",
        "resource_exhausted", "permission_denied", "service unavailable",
        "요청 처리에 실패", "응답 생성에 실패", "조사를 완료하지 못했습니다",
    )
    if any(marker.casefold() in lowered for marker in error_markers):
        return False, "오류 또는 서비스 장애 문구가 보고서에 포함되어 있습니다."

    return True, ""
