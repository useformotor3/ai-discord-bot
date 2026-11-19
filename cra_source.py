"""Official CRA source-pack retrieval and conservative provenance validation."""
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import re
from urllib.parse import urljoin, urlparse


CRA_SOURCE_URL = "https://publications.europa.eu/resource/celex/02024R2847-20241120?language=eng"
REQUIRED_CORRIGENDA_DATES = ("5.12.2024", "2.7.2025", "17.10.2025")
SOURCE_TIMEOUT = (3.05, 20)


class SourceUnavailableError(RuntimeError):
    """Temporary network/service failure; caller should safely skip this run."""


class SourceValidationError(RuntimeError):
    """Unexpected host/content/version; caller must stop before model execution."""


CRA_SOURCE_CATALOG = (
    {
        "id": "CRA-2024-2847-consolidated",
        "url": CRA_SOURCE_URL,
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_legal_text",
        "version": (
            "Regulation (EU) 2024/2847 consolidated text 20.11.2024; "
            "English corrigenda 5.12.2024, 2.7.2025 and 17.10.2025"
        ),
        "min_chars": 10000,
        "required": ("Regulation (EU) 2024/2847",),
    },
    {
        "id": "CRA-2025-2392-important-critical-product-descriptions",
        "url": "https://publications.europa.eu/resource/celex/32025R2392?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_implementing_regulation",
        "version": (
            "Commission Implementing Regulation (EU) 2025/2392, OJ L 2025/2392, 01.12.2025; "
            "technical descriptions for Annex III important and Annex IV critical product categories"
        ),
        "min_chars": 5000,
        "required": (
            "Commission Implementing Regulation (EU) 2025/2392",
            "core functionality",
            "Physical and virtual network interfaces",
            "Hardware Devices with Security Boxes",
            "Smartcards or similar devices",
        ),
    },
    {
        "id": "CRA-2024-2847-corrigendum-2024-12-05",
        "url": "https://publications.europa.eu/resource/celex/32024R2847R%2801%29?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_corrigendum",
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
        "url": "https://publications.europa.eu/resource/celex/32024R2847R%2802%29?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_corrigendum",
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
        "url": "https://publications.europa.eu/resource/celex/32024R2847R%2804%29?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_corrigendum",
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
        "url": "https://publications.europa.eu/resource/celex/32025R0327?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_amending_regulation",
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
        "url": "https://publications.europa.eu/resource/celex/32025R1535?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_delegated_regulation",
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
        "url": "https://publications.europa.eu/resource/celex/32026R0881?language=eng",
        "allowed_hosts": ("publications.europa.eu",),
        "kind": "official_delegated_regulation",
        "version": (
            "Commission Delegated Regulation (EU) 2026/881; in force 10.05.2026; "
            "conditions for delaying dissemination of notifications under CRA Article 16"
        ),
        "min_chars": 1000,
        "required": ("2026/881", "Article 16", "notifications"),
    },
    {
        "id": "CRA-COMMISSION-GUIDANCE-2026-07-27",
        "url": "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation",
        "allowed_hosts": ("digital-strategy.ec.europa.eu",),
        "kind": "official_non_binding_guidance_publication_page",
        "related_urls": (
            "https://ec.europa.eu/newsroom/dae/redirection/document/131456",
        ),
        "related_allowed_hosts": ("ec.europa.eu",),
        "related_note": "Commission PDF Annex is fetched and hashed separately by cra_pdf_sources.py; this page-only source record does not contain the PDF binary.",
        "version": (
            "European Commission CRA guidance publication page, 27.07.2026, C(2026) 5252; "
            "page summary only, not the full guidance annex"
        ),
        "min_chars": 1000,
        "required": (
            "27 July 2026",
            "though non-binding",
            "remote data processing solutions",
        ),
    },
    {
        "id": "CRA-M606-STANDARDISATION-2026-11-12",
        "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation",
        "allowed_hosts": ("digital-strategy.ec.europa.eu",),
        "kind": "official_standardisation_status_page",
        "related_urls": (
            "https://ec.europa.eu/transparency/documents-register/detail?ref=C(2026)7861&lang=en",
        ),
        "related_allowed_hosts": ("ec.europa.eu",),
        "related_note": "The C(2026) 7861 Annex PDF is fetched and hashed separately by cra_pdf_sources.py; this status-page source record does not contain the Annex binary.",
        "version": (
            "European Commission CRA standardisation page, updated 12.11.2026; "
            "confirms 10.11.2026 M/606 three-month extension; page does not provide item-level revised dates"
        ),
        "min_chars": 1000,
        "required": (
            "M/606",
            "On 10 November 2026",
            "by 3 months",
            "41 standards",
        ),
    },
)


class _VisibleText(HTMLParser):
    """Extract visible text while preserving block boundaries for legal locators."""

    HIDDEN_TAGS = {"script", "style", "noscript", "svg", "nav", "header", "footer", "aside", "form"}
    BLOCK_TAGS = {
        "p", "div", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6",
        "li", "ol", "ul", "tr", "td", "th", "br", "table",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden_depth = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in self.HIDDEN_TAGS:
            self.hidden_depth += 1
            return
        if not self.hidden_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in self.HIDDEN_TAGS:
            if self.hidden_depth:
                self.hidden_depth -= 1
            return
        if not self.hidden_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden_depth:
            self.parts.append(data)


def normalize_source_text(value):
    """Normalize each visible block while retaining paragraph/point boundaries."""
    lines = []
    for raw_line in str(value or "").replace("\r", "\n").split("\n"):
        normalized = re.sub(r"\s+", " ", raw_line).strip()
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def _extract_visible_text(html):
    parser = _VisibleText()
    parser.feed(html)
    return normalize_source_text("".join(parser.parts))


def _missing_required_markers(text, markers):
    """Match required phrases across HTML paragraph/line boundaries."""
    normalized = re.sub(r"\s+", " ", str(text or "")).casefold()
    return [
        marker for marker in markers
        if re.sub(r"\s+", " ", marker).casefold() not in normalized
    ]


def _extract_relevant_excerpt(source_id, text):
    """Keep operative CRA text and the CRA-specific EHDS amendment excerpt."""
    if source_id == "CRA-2024-2847-consolidated":
        lines = text.splitlines()
        starts = [
            index for index, line in enumerate(lines)
            if re.fullmatch(r"Article\s+1", line, re.IGNORECASE)
        ]
        if not starts:
            raise SourceValidationError("EUR-Lex consolidated text에서 Article 1 시작 위치를 찾지 못했습니다.")
        # Exclude recitals/front matter; retain all operative Articles and Annexes with block boundaries.
        return "\n".join(lines[starts[-1]:])
    if source_id != "CRA-2025-327-EHDS-amendment":
        return text
    match = re.search(
        r"Article\s+104\b.*?(?=Article\s+105\b|$)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        raise SourceValidationError("Regulation (EU) 2025/327에서 CRA 개정 Article 104를 추출하지 못했습니다.")
    excerpt = match.group(0)[:12000]
    if "26 March 2027" not in text:
        raise SourceValidationError("Regulation (EU) 2025/327의 적용 개시일 26 March 2027을 확인하지 못했습니다.")
    return "EHDS application date: 26 March 2027.\nRelevant CRA amendment:\n" + excerpt


def _request_with_safe_redirects(requests_module, definition):
    """Follow only allowlisted HTTPS redirects; upgrade same-host HTTP redirects to HTTPS."""
    allowed_hosts = definition.get("allowed_hosts", ())
    current_url = definition["url"]
    for _ in range(6):
        current = urlparse(current_url)
        if current.scheme != "https" or current.hostname not in allowed_hosts:
            raise SourceValidationError(
                f"공식 source 요청 URL이 HTTPS allowlist를 벗어났습니다: {definition['id']} / {current_url}"
            )
        response = requests_module.get(
            current_url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
                ),
                "Accept": "application/xhtml+xml,text/html;q=0.9,application/xml;q=0.8,*/*;q=0.7",
                "Accept-Language": "eng",
                "Accept-Encoding": "gzip, deflate",
            },
            timeout=SOURCE_TIMEOUT,
            allow_redirects=False,
        )
        if response.status_code not in (301, 302, 303, 307, 308):
            return response, getattr(response, "url", current_url)
        location = response.headers.get("Location")
        if not location:
            raise SourceValidationError(
                f"공식 source 리디렉션 응답에 Location이 없습니다: {definition['id']}"
            )
        target = urljoin(current_url, location)
        parsed_target = urlparse(target)
        if parsed_target.hostname not in allowed_hosts or parsed_target.scheme not in ("http", "https"):
            raise SourceValidationError(
                f"허용되지 않은 공식 source 리디렉션입니다: {definition['id']} / {target}"
            )
        if parsed_target.scheme == "http":
            target = parsed_target._replace(scheme="https").geturl()
        current_url = target
    raise SourceValidationError(
        f"공식 source 리디렉션 횟수가 제한을 초과했습니다: {definition['id']}"
    )


def _article_section_text(source_text, article_number):
    """Extract one complete Article block from normalized official source text."""
    lines = str(source_text or "").splitlines()
    start = next(
        (
            index for index, line in enumerate(lines)
            if re.fullmatch(rf"\s*Article\s+{article_number}\s*", line, re.IGNORECASE)
        ),
        None,
    )
    if start is None:
        return ""
    end = next(
        (
            index for index in range(start + 1, len(lines))
            if re.fullmatch(r"\s*Article\s+\d+\s*", lines[index], re.IGNORECASE)
        ),
        len(lines),
    )
    return "\n".join(lines[start:end])


def _replace_article_phrase(text, article_number, old_pattern, new_phrase, new_pattern, label):
    lines = str(text or "").splitlines(keepends=True)
    start = next(
        (
            index for index, line in enumerate(lines)
            if re.fullmatch(rf"\s*Article\s+{article_number}\s*", line.strip(), re.IGNORECASE)
        ),
        None,
    )
    if start is None:
        raise SourceValidationError(f"정오표 적용 대상 Article {article_number}를 찾지 못했습니다: {label}")
    end = next(
        (
            index for index in range(start + 1, len(lines))
            if re.fullmatch(r"\s*Article\s+\d+\s*", lines[index].strip(), re.IGNORECASE)
        ),
        len(lines),
    )
    block = "".join(lines[start:end])
    old_matches = list(re.finditer(old_pattern, block, re.IGNORECASE))
    new_matches = list(re.finditer(new_pattern, block, re.IGNORECASE))
    if len(old_matches) == 1 and len(new_matches) == 0:
        block = re.sub(old_pattern, new_phrase, block, count=1, flags=re.IGNORECASE)
    elif len(old_matches) == 0 and len(new_matches) == 1:
        pass
    else:
        raise SourceValidationError(
            f"정오표 적용 대상 문구가 없거나 중복되어 안전하게 적용할 수 없습니다: {label} "
            f"(old={len(old_matches)}, corrected={len(new_matches)})"
        )
    return "".join(lines[:start]) + block + "".join(lines[end:])


def apply_consolidated_cra_corrigenda(source_items):
    """Apply operative English corrigenda to the model-facing consolidated excerpt."""
    if not isinstance(source_items, list):
        raise SourceValidationError("CRA source 목록이 올바르지 않습니다.")
    by_id = {
        item.get("id"): item
        for item in source_items
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    base = by_id.get("CRA-2024-2847-consolidated")
    july = by_id.get("CRA-2024-2847-corrigendum-2025-07-02")
    october = by_id.get("CRA-2024-2847-corrigendum-2025-10-17")
    if not all(isinstance(item, dict) for item in (base, july, october)):
        raise SourceValidationError("CRA consolidated text와 2025년 정오표 2건이 모두 필요합니다.")

    normalized = lambda value: re.sub(r"\s+", " ", str(value or "")).casefold()
    july_text = normalized(july.get("text"))
    october_text = normalized(october.get("text"))
    if "paragraphs 3 to 9" not in july_text or "paragraphs 2 to 9" not in july_text:
        raise SourceValidationError("2025-07-02 정오표의 Article 64(10) 전/후 문구를 확인하지 못했습니다.")
    if "69. regulation" not in october_text or "72. regulation" not in october_text:
        raise SourceValidationError("2025-10-17 정오표의 Article 67 전/후 문구를 확인하지 못했습니다.")

    corrected = base.get("text", "")
    corrected = _replace_article_phrase(
        corrected,
        64,
        r"paragraphs\s+3\s+to\s+9",
        "paragraphs 2 to 9",
        r"paragraphs\s+2\s+to\s+9",
        "2025-07-02 corrigendum / Article 64(10)",
    )
    corrected = _replace_article_phrase(
        corrected,
        67,
        r"69\.\s*Regulation\s+\(EU\)\s+2024/2847",
        "72. Regulation (EU) 2024/2847",
        r"72\.\s*Regulation\s+\(EU\)\s+2024/2847",
        "2025-10-17 corrigendum / Article 67",
    )
    base["text"] = corrected
    base["applied_corrigenda"] = [
        "CRA-2024-2847-corrigendum-2025-07-02",
        "CRA-2024-2847-corrigendum-2025-10-17",
    ]
    base["applied_correction_notes"] = [
        "Article 64(10): corrected reading verified as paragraphs 2 to 9 (stale text is patched if present)",
        "Article 67: corrected reference verified as 72. Regulation (EU) 2024/2847 (stale text is patched if present)",
    ]
    base["version"] = (
        str(base.get("version", ""))
        + "; English operative corrigenda R(02)/R(04) applied or verified in prompt excerpt"
    ).strip("; ")
    excerpt_hash = hashlib.sha256(corrected.encode("utf-8")).hexdigest()
    base["prompt_excerpt_sha256"] = excerpt_hash
    base["sha256"] = excerpt_hash
    validate_consolidated_cra_corrections(source_items)
    return base["applied_corrigenda"]


def validate_consolidated_cra_corrections(source_items):
    """Verify corrected Article 64(10)/67 text and their official corrigendum sources."""
    if not isinstance(source_items, list):
        raise SourceValidationError("CRA source 목록이 올바르지 않습니다.")
    by_id = {
        item.get("id"): item
        for item in source_items
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    base = by_id.get("CRA-2024-2847-consolidated")
    july = by_id.get("CRA-2024-2847-corrigendum-2025-07-02")
    october = by_id.get("CRA-2024-2847-corrigendum-2025-10-17")
    if not all(isinstance(item, dict) for item in (base, july, october)):
        raise SourceValidationError("CRA consolidated text와 2025년 정오표 2건이 모두 필요합니다.")

    normalized = lambda value: re.sub(r"\s+", " ", str(value or "")).casefold()
    article_64 = normalized(_article_section_text(base.get("text"), 64))
    article_67 = normalized(_article_section_text(base.get("text"), 67))
    if "paragraphs 2 to 9" not in article_64 or "paragraphs 3 to 9" in article_64:
        raise SourceValidationError(
            "CRA consolidated Article 64(10)이 2025-07-02 정오표의 정정 후 문구와 일치하지 않습니다."
        )
    if "72. regulation (eu) 2024/2847" not in article_67 or "69. regulation (eu) 2024/2847" in article_67:
        raise SourceValidationError(
            "CRA consolidated Article 67이 2025-10-17 정오표의 정정 후 문구와 일치하지 않습니다."
        )
    if "paragraphs 3 to 9" not in normalized(july.get("text")) or "paragraphs 2 to 9" not in normalized(july.get("text")):
        raise SourceValidationError("2025-07-02 정오표의 전/후 문구가 source pack에 없습니다.")
    if "69. regulation" not in normalized(october.get("text")) or "72. regulation" not in normalized(october.get("text")):
        raise SourceValidationError("2025-10-17 정오표의 전/후 문구가 source pack에 없습니다.")
    if not base.get("applied_corrigenda"):
        raise SourceValidationError("consolidated prompt excerpt에 적용된 정오표 기록이 없습니다.")
    return True


def fetch_official_cra_source():
    """Fetch allowlisted official legal texts and Commission publication/status pages."""
    import requests

    source_items = []
    retrieved_at = datetime.now(timezone.utc).isoformat()
    for definition in CRA_SOURCE_CATALOG:
        try:
            response, final_url = _request_with_safe_redirects(requests, definition)
        except requests.exceptions.SSLError as exc:
            raise SourceValidationError(
                f"공식 source TLS 인증 검증 실패: {definition['id']}"
            ) from exc
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
            raise SourceUnavailableError(
                f"공식 source 일시 접근 실패: {definition['id']} / {type(exc).__name__}"
            ) from exc
        except requests.exceptions.RequestException as exc:
            raise SourceValidationError(
                f"공식 source 요청 형식/리디렉션 오류: {definition['id']} / {type(exc).__name__}"
            ) from exc
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            status = getattr(getattr(exc, "response", None), "status_code", None)
            if status == 429 or (isinstance(status, int) and status >= 500):
                raise SourceUnavailableError(
                    f"공식 source 일시 HTTP 오류: {definition['id']} / {status}"
                ) from exc
            raise SourceValidationError(
                f"공식 source HTTP 오류: {definition['id']} / {status}"
            ) from exc
        if response.status_code == 202:
            raise SourceUnavailableError(
                f"공식 source가 HTTP 202 비동기 수락 응답을 반환했습니다: {definition['id']} "
                f"(Retry-After={response.headers.get('Retry-After', 'unknown')})"
            )
        response_text = response.text or ""
        if not response_text.strip():
            raise SourceUnavailableError(
                f"공식 source가 빈 응답을 반환했습니다: {definition['id']} "
                f"(HTTP {response.status_code}, Content-Length={response.headers.get('Content-Length', 'unknown')})"
            )
        parsed_url = urlparse(final_url)
        allowed_hosts = definition.get("allowed_hosts", ("eur-lex.europa.eu",))
        if parsed_url.scheme != "https" or parsed_url.hostname not in allowed_hosts:
            raise SourceValidationError(
                f"허용되지 않은 공식 도메인으로 리디렉션되어 원문 수집을 중단합니다: "
                f"{definition['id']} / {final_url}"
            )

        full_text = _extract_visible_text(response_text)
        if len(full_text) < definition["min_chars"]:
            raise SourceValidationError(
                f"공식 원문/페이지가 너무 짧습니다: {definition['id']} "
                f"(visible_text={len(full_text)}, html_chars={len(response_text)}, HTTP={response.status_code}, "
                f"Content-Type={response.headers.get('Content-Type', 'unknown')})"
            )
        missing = _missing_required_markers(full_text, definition["required"])
        if missing:
            raise SourceValidationError(
                f"공식 원문 식별자를 확인하지 못했습니다: "
                f"{definition['id']} / {', '.join(missing)}"
            )

        if definition["id"] == "CRA-2024-2847-consolidated":
            missing_dates = [date for date in REQUIRED_CORRIGENDA_DATES if date not in full_text]
            if missing_dates:
                raise SourceValidationError(
                    "EUR-Lex 통합본에서 알려진 CRA corrigenda 날짜를 모두 확인하지 못했습니다: "
                    + ", ".join(missing_dates)
                )

        related_urls = list(definition.get("related_urls", ()))
        related_hosts = definition.get("related_allowed_hosts", ())
        for related_url in related_urls:
            related = urlparse(related_url)
            if related.scheme != "https" or related.hostname not in related_hosts:
                raise SourceValidationError(
                    f"허용되지 않은 관련 공식 문서 URL입니다: {definition['id']} / {related_url}"
                )

        relevant_text = _extract_relevant_excerpt(definition["id"], full_text)
        source_items.append({
            "id": definition["id"],
            "url": definition["url"],
            "final_url": final_url,
            "kind": definition["kind"],
            "version": definition["version"],
            "related_urls": list(definition.get("related_urls", ())),
            "related_note": definition.get("related_note", ""),
            "text": relevant_text,
            "visible_text_chars": len(full_text),
            "full_text_sha256": hashlib.sha256(full_text.encode("utf-8")).hexdigest(),
            "prompt_excerpt_sha256": hashlib.sha256(relevant_text.encode("utf-8")).hexdigest(),
            "sha256": hashlib.sha256(relevant_text.encode("utf-8")).hexdigest(),
            "retrieved_at": retrieved_at,
        })

    apply_consolidated_cra_corrigenda(source_items)

    combined_text = "\n\n".join(
        f"[{item['id']}]\n{item['url']}\n{item['version']}\n"
        + (
            "Official corrigenda applied/verified in prompt excerpt: "
            + "; ".join(item.get("applied_corrigenda", [])) + "\n"
            if item.get("applied_corrigenda") else ""
        )
        + (
            "Related official documents (not fetched/parsed by this source pack): "
            + "; ".join(item.get("related_urls", []))
            + "\n" + item.get("related_note", "") + "\n"
            if item.get("related_urls") else ""
        )
        + item["text"]
        for item in source_items
    )
    version = f"CRA official source pack v3; sources={len(source_items)}; corrigenda_precedence=verified"
    return {
        "url": CRA_SOURCE_URL,
        "version": version,
        "retrieved_at": retrieved_at,
        "sources": source_items,
        "text": combined_text,
    }



def build_source_provenance_manifest(source):
    """Return a minimal, hash-verifiable JSON manifest for an official source pack."""
    if not isinstance(source, dict) or not isinstance(source.get("sources"), list) or not source["sources"]:
        raise SourceValidationError("공식 source pack manifest 입력 구조가 올바르지 않습니다.")
    pack_version = source.get("version")
    retrieved_at = source.get("retrieved_at")
    if not isinstance(pack_version, str) or not pack_version.strip():
        raise SourceValidationError("공식 source pack version이 없습니다.")
    if not isinstance(retrieved_at, str) or not retrieved_at.strip():
        raise SourceValidationError("공식 source pack retrieved_at이 없습니다.")

    records = []
    required_text_fields = (
        "id", "url", "final_url", "kind", "version", "full_text_sha256",
        "prompt_excerpt_sha256", "retrieved_at",
    )
    for index, item in enumerate(source["sources"], start=1):
        if not isinstance(item, dict):
            raise SourceValidationError(f"공식 source manifest 항목 {index} 구조가 올바르지 않습니다.")
        for field in required_text_fields:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                raise SourceValidationError(f"공식 source manifest 필드가 없습니다: {item.get('id', index)} / {field}")
        for field in ("full_text_sha256", "prompt_excerpt_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", item[field]):
                raise SourceValidationError(f"공식 source manifest SHA-256 형식 오류: {item['id']} / {field}")
        visible_chars = item.get("visible_text_chars")
        if not isinstance(visible_chars, int) or visible_chars <= 0:
            raise SourceValidationError(f"공식 source manifest visible_text_chars 오류: {item['id']}")
        if item["retrieved_at"] != retrieved_at:
            raise SourceValidationError(f"공식 source manifest retrieved_at 불일치: {item['id']}")
        record = {field: item[field] for field in required_text_fields}
        record["visible_text_chars"] = visible_chars
        record["related_urls"] = list(item.get("related_urls", []))
        record["related_note"] = item.get("related_note", "")
        record["applied_corrigenda"] = list(item.get("applied_corrigenda", []))
        records.append(record)

    return {
        "schema_version": "1.0",
        "source_pack_version": pack_version,
        "retrieved_at": retrieved_at,
        "source_count": len(records),
        "sources": records,
    }


def append_source_manifest(report, source):
    """Append machine-collected source metadata and content hashes after validation."""
    lines = [
        "## 공식 출처 목록 (자동 수집)",
        f"Source pack retrieved at: {source['retrieved_at']}",
        f"Source pack version: {source['version']}",
        (
            "주의: Commission guidance/standardisation 항목은 공식 설명·현황 페이지다. "
            "해당 페이지에 수록되지 않은 Annex/PDF의 세부 내용을 입증하는 원문으로 취급하지 않는다."
        ),
    ]
    for item in source["sources"]:
        lines.append(
            f"- {item['id']}: {item['version']} | Requested URL: {item['url']} | "
            f"Final URL: {item['final_url']} | Visible-text SHA-256: {item['full_text_sha256']} | "
            f"Prompt-excerpt SHA-256: {item['prompt_excerpt_sha256']} | "
            f"Retrieved: {item['retrieved_at']}"
        )
        if item.get("applied_corrigenda"):
            lines.append("  Official corrigenda applied/verified in prompt excerpt: " + "; ".join(item["applied_corrigenda"]))
            for note in item.get("applied_correction_notes", []):
                lines.append(f"  Applied correction: {note}")
        if item.get("related_note"):
            lines.append(f"  Related-document note: {item['related_note']}")
        for related_url in item.get("related_urls", []):
            lines.append(f"  Related official document URL (not fetched/parsed by this source pack): {related_url}")
    return report.rstrip() + "\n\n" + "\n".join(lines)


def validate_source_manifest(report, source):
    """Verify that the final report contains every machine-appended source record."""
    if not isinstance(report, str) or not isinstance(source, dict):
        return False, "source manifest 입력 구조가 올바르지 않습니다."
    if source.get("version") not in report or source.get("retrieved_at") not in report:
        return False, "자동 출처 manifest의 version/retrieved_at이 누락되었습니다."
    for item in source.get("sources", []):
        for field in ("id", "version", "url", "final_url", "full_text_sha256", "prompt_excerpt_sha256", "retrieved_at"):
            value = item.get(field)
            if not isinstance(value, str) or value not in report:
                return False, f"자동 출처 manifest 항목이 누락되었습니다: {item.get('id')} / {field}"
        if item.get("applied_corrigenda"):
            applied_line = "Official corrigenda applied/verified in prompt excerpt: " + "; ".join(item["applied_corrigenda"])
            if applied_line not in report:
                return False, f"적용 정오표 manifest가 누락되었습니다: {item.get('id')}"
            for note in item.get("applied_correction_notes", []):
                if note not in report:
                    return False, f"적용 정오표 설명이 누락되었습니다: {item.get('id')}"
        if item.get("related_note") and item["related_note"] not in report:
            return False, f"관련 문서 상태 설명이 누락되었습니다: {item.get('id')}"
        for related_url in item.get("related_urls", []):
            if related_url not in report:
                return False, f"관련 공식 문서 URL이 누락되었습니다: {item.get('id')}"
    return True, ""


def validate_research_report(report, source):
    """Check minimum report structure and a verbatim quote; not a legal opinion."""
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

    if "eur-lex.europa.eu" not in lowered or "2024/2847" not in lowered:
        return False, "CRA Official Journal 원문 링크/규정 번호가 누락됐습니다."
    if "관보" not in text or not any(
        marker in lowered for marker in ("문서화 도구", "documentation tool")
    ):
        return False, "EUR-Lex 통합본의 문서화 도구 지위와 관보 정본의 법적 효력 주의가 누락됐습니다."

    source_text = re.sub(r"\s+", " ", source["text"]).casefold()
    article_refs = re.findall(r"\bArticle\s+\d+\b", text, flags=re.IGNORECASE)
    annex_refs = re.findall(r"\bAnnex\s+[IVX]+\b", text, flags=re.IGNORECASE)
    if not article_refs and not annex_refs:
        return False, "확인 가능한 CRA Article 또는 Annex 번호가 없습니다."
    missing_articles = [
        ref for ref in set(article_refs) if ref.casefold() not in source_text
    ]
    missing_annexes = [
        ref for ref in set(annex_refs) if ref.casefold() not in source_text
    ]
    if missing_articles:
        return False, "보고서의 Article 번호가 수집한 official source pack에서 확인되지 않습니다: " + ", ".join(sorted(missing_articles))
    if missing_annexes:
        return False, "보고서의 Annex 번호가 수집한 official source pack에서 확인되지 않습니다: " + ", ".join(sorted(missing_annexes))

    quote_match = re.search(
        r"출처 원문(?: 텍스트)?\s*(?:\(raw text quote\))?\s*[:：]?\s*(?:\n|$)(.*?)(?=CLAIM_EVIDENCE_JSON|$)",
        text, flags=re.IGNORECASE | re.DOTALL,
    )
    if not quote_match:
        return False, "원문 인용 구역을 구분할 수 없습니다."
    quote_text = quote_match.group(1)
    quoted = re.findall(r"“([^”]{50,})”|\"([^\"]{50,})\"", quote_text)
    quote_candidates = [part for match in quoted for part in match if part]
    if not quote_candidates:
        return False, "50자 이상의 직접 인용문이 큰따옴표로 표시되지 않았습니다."
    if not any(
        re.sub(r"\s+", " ", candidate).strip().casefold() in source_text
        for candidate in quote_candidates
    ):
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
