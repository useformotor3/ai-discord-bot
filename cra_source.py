"""Official CRA source-pack retrieval and conservative provenance validation."""
from html.parser import HTMLParser
import re
from urllib.parse import urlparse


CRA_SOURCE_URL = "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120"
REQUIRED_CORRIGENDA_DATES = ("5.12.2024", "2.7.2025", "17.10.2025")
SOURCE_TIMEOUT = (3.05, 20)

CRA_SOURCE_CATALOG = (
    {
        "id": "CRA-2024-2847-consolidated",
        "url": CRA_SOURCE_URL,
        "version": (
            "Regulation (EU) 2024/2847 consolidated text 20.11.2024; "
            "English corrigenda 5.12.2024, 2.7.2025 and 17.10.2025"
        ),
        "min_chars": 10000,
        "required": ("Regulation (EU) 2024/2847",),
    },
    {
        "id": "CRA-2024-2847-corrigendum-2024-12-05",
        "url": "https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2024-12-05/oj/eng",
        "version": (
            "Official Journal corrigendum 2024/90780, 05.12.2024; "
            "corrects the CRA title by removing 'No' before 2019/1020"
        ),
        "min_chars": 200,
        "required": (
            "On page 1, in the title",
            "No 2019/1020",
            "(EU) 2019/1020",
        ),
    },
    {
        "id": "CRA-2024-2847-corrigendum-2025-07-02",
        "url": "https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2025-07-02/oj/eng",
        "version": (
            "Official Journal corrigendum 2025/90555, 02.07.2025; "
            "Article 64(10) changes the fine-derogation reference from paragraphs 3-9 to 2-9"
        ),
        "min_chars": 200,
        "required": (
            "Article 64(10)",
            "paragraphs 3 to 9",
            "paragraphs 2 to 9",
        ),
    },
    {
        "id": "CRA-2024-2847-corrigendum-2025-10-17",
        "url": "https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2025-10-17/oj/eng",
        "version": (
            "Official Journal corrigendum 2025/90828, 17.10.2025; "
            "Article 67 changes the referenced Regulation number from 69 to 72"
        ),
        "min_chars": 200,
        "required": (
            "Article 67",
            "69. Regulation",
            "72. Regulation",
        ),
    },
    {
        "id": "CRA-2025-327-EHDS-amendment",
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R0327",
        "version": (
            "Regulation (EU) 2025/327 Article 104 adds CRA Article 32(5a) "
            "for EHR systems; applies from 26.03.2027"
        ),
        "min_chars": 1000,
        "required": ("Article 104", "Article 32", "26 March 2027"),
        "extract": "article_104",
    },
    {
        "id": "CRA-2025-1535-product-scope-delegated-act",
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R1535",
        "version": (
            "Commission Delegated Regulation (EU) 2025/1535; in force 18.11.2025; "
            "limited exclusion for products within Regulation (EU) No 168/2013, "
            "except specified L1e pedal-assisted vehicles"
        ),
        "min_chars": 1000,
        "required": ("168/2013", "L1e", "Article 1"),
    },
    {
        "id": "CRA-2026-881-reporting-delay-delegated-act",
        "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R0881",
        "version": (
            "Commission Delegated Regulation (EU) 2026/881; in force 10.05.2026; "
            "conditions for delaying dissemination of notifications under CRA Article 16"
        ),
        "min_chars": 1000,
        "required": ("2026/881", "Article 16", "notifications"),
    },
)


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


def _extract_visible_text(html):
    parser = _VisibleText()
    parser.feed(html)
    return normalize_source_text(" ".join(parser.parts))


def _extract_relevant_excerpt(source_id, text):
    """Keep the CRA-amending EHDS Article 104 excerpt, not the unrelated full EHDS act."""
    if source_id != "CRA-2025-327-EHDS-amendment":
        return text
    match = re.search(r"Article\s+104\b.*?(?=Article\s+105\b|$)", text, flags=re.IGNORECASE)
    if not match:
        raise RuntimeError("Regulation (EU) 2025/327에서 CRA 개정 Article 104를 추출하지 못했습니다.")
    excerpt = match.group(0)[:12000]
    if "26 March 2027" not in text:
        raise RuntimeError("Regulation (EU) 2025/327의 적용 개시일 26 March 2027을 확인하지 못했습니다.")
    return "EHDS application date: 26 March 2027. Relevant CRA amendment: " + excerpt


def fetch_official_cra_source():
    """Fetch CRA base text plus official linked acts directly from EUR-Lex."""
    import requests

    source_items = []
    for definition in CRA_SOURCE_CATALOG:
        response = requests.get(
            definition["url"],
            headers={"User-Agent": "CRA-Research-Bot/1.0 (+https://eur-lex.europa.eu/)"},
            timeout=SOURCE_TIMEOUT,
        )
        response.raise_for_status()
        final_url = getattr(response, "url", definition["url"])
        parsed_url = urlparse(final_url)
        if parsed_url.scheme != "https" or parsed_url.hostname != "eur-lex.europa.eu":
            raise RuntimeError(
                f"EUR-Lex 이외의 도메인으로 리디렉션되어 원문 수집을 중단합니다: {definition['id']}"
            )

        full_text = _extract_visible_text(response.text)
        if len(full_text) < definition["min_chars"]:
            raise RuntimeError(f"EUR-Lex 원문이 너무 짧습니다: {definition['id']}")
        folded = full_text.casefold()
        missing = [marker for marker in definition["required"] if marker.casefold() not in folded]
        if missing:
            raise RuntimeError(
                f"EUR-Lex 후속 법령/원문 식별자를 확인하지 못했습니다: "
                f"{definition['id']} / {', '.join(missing)}"
            )

        if definition["id"] == "CRA-2024-2847-consolidated":
            missing_dates = [date for date in REQUIRED_CORRIGENDA_DATES if date not in full_text]
            if missing_dates:
                raise RuntimeError(
                    "EUR-Lex 통합본에서 알려진 CRA corrigenda 날짜를 모두 확인하지 못했습니다: "
                    + ", ".join(missing_dates)
                )

        relevant_text = _extract_relevant_excerpt(definition["id"], full_text)
        source_items.append({
            "id": definition["id"],
            "url": definition["url"],
            "version": definition["version"],
            "text": relevant_text,
            "visible_text_chars": len(full_text),
        })

    combined_text = "\n\n".join(
        f"[{item['id']}]\n{item['url']}\n{item['version']}\n{item['text']}"
        for item in source_items
    )
    version = " | ".join(item["version"] for item in source_items)
    return {
        "url": CRA_SOURCE_URL,
        "version": version,
        "sources": source_items,
        "text": combined_text,
    }


def append_source_manifest(report, source):
    """Append machine-collected source URLs and versions so the model cannot omit them."""
    lines = [
        "## 공식 출처 목록 (자동 수집)",
        f"Source pack version: {source['version']}",
    ]
    for item in source["sources"]:
        lines.append(f"- {item['id']}: {item['version']} — {item['url']}")
    return report.rstrip() + "\n\n" + "\n".join(lines)


def validate_research_report(report, source):
    """Check report structure, source manifest, clause locator, and one verbatim quote.

    This is a minimum provenance gate, not a full legal or semantic correctness review.
    """
    if not isinstance(report, str):
        return False, "응답이 문자열이 아닙니다."
    if not isinstance(source, dict) or not source.get("text") or not source.get("sources"):
        return False, "검증 가능한 공식 CRA source pack이 없습니다."

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

    if source["version"] not in text:
        return False, "출처 자료에 전체 official source pack version이 없습니다."
    for item in source["sources"]:
        if item["url"] not in text:
            return False, f"공식 출처 URL이 누락됐습니다: {item['id']}"
        if item["version"] not in text:
            return False, f"공식 출처 버전/적용일이 누락됐습니다: {item['id']}"

    if "관보" not in text or not any(
        marker in lowered for marker in ("문서화 도구", "documentation tool")
    ):
        return False, "EUR-Lex 통합본의 문서화 도구 지위와 관보 정본의 법적 효력 주의가 누락됐습니다."

    source_text = normalize_source_text(source["text"]).casefold()
    article_refs = re.findall(r"\bArticle\s+\d+\b", text, flags=re.IGNORECASE)
    annex_refs = re.findall(r"\bAnnex\s+[IVX]+\b", text, flags=re.IGNORECASE)
    if not article_refs and not annex_refs:
        return False, "확인 가능한 CRA Article 또는 Annex 번호가 없습니다."
    if article_refs and not any(ref.casefold() in source_text for ref in article_refs):
        return False, "보고서의 Article 번호가 수집한 official source pack에서 확인되지 않습니다."
    if annex_refs and not any(ref.casefold() in source_text for ref in annex_refs):
        return False, "보고서의 Annex 번호가 수집한 official source pack에서 확인되지 않습니다."

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
        return False, "보고서의 직접 인용문이 수집한 official source pack과 일치하지 않습니다."

    error_markers = (
        "시스템 긴급 경고", "모든 ai 모델", "temporarily unavailable",
        "quota exceeded", "rate limit exceeded", "internal server error",
        "resource_exhausted", "permission_denied", "service unavailable",
        "요청 처리에 실패", "응답 생성에 실패", "조사를 완료하지 못했습니다",
    )
    if any(marker.casefold() in lowered for marker in error_markers):
        return False, "오류 또는 서비스 장애 문구가 보고서에 포함되어 있습니다."

    return True, ""
