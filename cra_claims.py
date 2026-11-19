"""Strict claim-to-evidence validation for CRA draft reports.

This validates traceability to retrieved source text and exact locator scope. It does
not prove that a legal interpretation or product-specific conclusion is correct.
"""
import json
import re


ALLOWED_CATEGORIES = {
    "legal_requirement",
    "official_explanation",
    "interpretation",
    "engineering_recommendation",
}
CLAIM_BLOCK_PATTERN = re.compile(
    r"CLAIM_EVIDENCE_JSON\s*[:：]?\s*\x60\x60\x60json\s*(.*?)\x60\x60\x60",
    re.IGNORECASE | re.DOTALL,
)
CLAIM_REFERENCE_PATTERN = re.compile(r"\[(C-\d{3,})\]")
CLAIM_EVIDENCE_JSON_BLOCK_REMOVER = re.compile(
    r"CLAIM_EVIDENCE_JSON\s*[:：]?\s*\x60\x60\x60json\s*.*?\x60\x60\x60",
    re.IGNORECASE | re.DOTALL,
)


def _normalized(value):
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def _source_lines(source_text):
    return [
        re.sub(r"\s+", " ", line).strip()
        for line in str(source_text or "").splitlines()
        if line.strip()
    ]


def _is_article_heading(line, number):
    return bool(re.fullmatch(rf"Article\s+{re.escape(str(number))}", line, re.IGNORECASE))


def _is_annex_heading(line, roman):
    return bool(re.fullmatch(rf"Annex\s+{re.escape(str(roman))}", line, re.IGNORECASE))


def _is_part_heading(line, part):
    return bool(re.fullmatch(rf"Part\s+{re.escape(str(part))}", line, re.IGNORECASE))


def _next_section_boundary(lines, start, pattern):
    for index in range(start + 1, len(lines)):
        if pattern(lines[index]):
            return index
    return len(lines)


def _number_range(locator):
    match = re.search(r"\((\d+[a-z]?)\)\s*(?:[-–]\s*\((\d+[a-z]?)\))?", str(locator or ""), re.IGNORECASE)
    if not match:
        return []
    first = match.group(1).lower()
    last = (match.group(2) or first).lower()
    if first.isdigit() and last.isdigit():
        first_num, last_num = int(first), int(last)
        if last_num < first_num or last_num - first_num > 30:
            return []
        return [str(value) for value in range(first_num, last_num + 1)]
    return [first] if first == last else [first, last]


def _letter_range(locator):
    match = re.search(r"\(([a-z])\)\s*(?:[-–]\s*\(([a-z])\))?", str(locator or ""), re.IGNORECASE)
    if not match:
        return []
    first = ord(match.group(1).lower())
    last = ord((match.group(2) or match.group(1)).lower())
    if last < first or last - first > 25:
        return []
    return [chr(code) for code in range(first, last + 1)]


def _paragraph_scope(lines, section_start, section_end, number):
    marker = re.compile(rf"^\s*{re.escape(str(number))}\.\s*(.*)$")
    starts = [
        index for index in range(section_start, section_end)
        if marker.match(lines[index])
    ]
    if not starts:
        return None
    start = starts[-1]
    end = section_end
    for index in range(start + 1, section_end):
        if re.match(r"^\s*\d+[a-z]?\.\s*(?:.*)$", lines[index], re.IGNORECASE):
            end = index
            break
    return "\n".join(lines[start:end])


def _parenthesized_scope(lines, section_start, section_end, number):
    marker = re.compile(rf"^\s*\({re.escape(str(number))}\)\s*(.*)$", re.IGNORECASE)
    starts = [
        index for index in range(section_start, section_end)
        if marker.match(lines[index])
    ]
    if not starts:
        return None
    start = starts[-1]
    end = section_end
    for index in range(start + 1, section_end):
        if re.match(r"^\s*\(\d+\)\s*(?:.*)$", lines[index]):
            end = index
            break
    return "\n".join(lines[start:end])


def _letter_point_scope(lines, part_start, part_end, paragraph, point):
    paragraph_marker = re.compile(rf"^\s*\({paragraph}\)\s*(.*)$")
    paragraph_starts = [
        index for index in range(part_start, part_end)
        if paragraph_marker.match(lines[index])
    ]
    if not paragraph_starts:
        return None
    paragraph_start = paragraph_starts[-1]
    paragraph_end = part_end
    for index in range(paragraph_start + 1, part_end):
        if re.match(r"^\s*\(\d+\)\s*(?:.*)$", lines[index]):
            paragraph_end = index
            break

    point_marker = re.compile(rf"^\s*\({re.escape(point)}\)\s*(.*)$", re.IGNORECASE)
    point_starts = [
        index for index in range(paragraph_start + 1, paragraph_end)
        if point_marker.match(lines[index])
    ]
    if not point_starts:
        return None
    start = point_starts[-1]
    end = paragraph_end
    for index in range(start + 1, paragraph_end):
        if re.match(r"^\s*\([a-z]\)\s*(?:.*)$", lines[index], re.IGNORECASE):
            end = index
            break
    return "\n".join(lines[start:end])


def _article_scope(locator, lines):
    article = re.search(r"\bArticle\s+(\d+)\b", locator, re.IGNORECASE)
    if not article:
        return None
    number = article.group(1)
    headings = [
        index for index, line in enumerate(lines)
        if _is_article_heading(line, number)
    ]
    paragraph_numbers = _number_range(locator)
    for start in headings:
        end = _next_section_boundary(
            lines,
            start,
            lambda line: bool(re.fullmatch(r"Article\s+\d+", line, re.IGNORECASE))
            or bool(re.fullmatch(r"Annex\s+[IVX]+", line, re.IGNORECASE)),
        )
        if not paragraph_numbers:
            continue
        scopes = [
            _paragraph_scope(lines, start + 1, end, paragraph)
            for paragraph in paragraph_numbers
        ]
        scopes = [scope for scope in scopes if scope]
        if scopes:
            return "\n".join(scopes)
    return None


def _annex_scope(locator, lines):
    annex = re.search(r"\bAnnex\s+([IVX]+)\b", locator, re.IGNORECASE)
    if not annex:
        return None
    roman = annex.group(1).upper()
    headings = [
        index for index, line in enumerate(lines)
        if _is_annex_heading(line, roman)
    ]
    part_match = re.search(r"\bPart\s+(I{1,3}|IV|V)\b", locator, re.IGNORECASE)
    paragraph_numbers = _number_range(locator)
    letter_points = _letter_range(locator) if part_match and part_match.group(1).upper() == "I" else []
    category_match = re.search(r"\bcategory\s+#?(\d+)\b", locator, re.IGNORECASE)
    if category_match:
        category_number = category_match.group(1)
        for annex_start in headings:
            annex_end = _next_section_boundary(
                lines, annex_start,
                lambda line: bool(re.fullmatch(r"Annex\s+[IVX]+", line, re.IGNORECASE)),
            )
            scope = _paragraph_scope(lines, annex_start + 1, annex_end, category_number)
            if scope:
                return scope
        return None

    for annex_start in headings:
        annex_end = _next_section_boundary(
            lines, annex_start,
            lambda line: bool(re.fullmatch(r"Annex\s+[IVX]+", line, re.IGNORECASE)),
        )
        if not part_match:
            if not paragraph_numbers:
                continue
            scopes = [
                _parenthesized_scope(lines, annex_start + 1, annex_end, n)
                for n in paragraph_numbers
            ]
            scopes = [scope for scope in scopes if scope]
            if not scopes:
                scopes = [
                    _paragraph_scope(lines, annex_start + 1, annex_end, n)
                    for n in paragraph_numbers
                ]
                scopes = [scope for scope in scopes if scope]
            if scopes:
                return "\n".join(scopes)
            continue

        part = part_match.group(1).upper()
        part_starts = [
            index for index in range(annex_start + 1, annex_end)
            if _is_part_heading(lines[index], part)
        ]
        for part_start in part_starts:
            part_end = _next_section_boundary(
                lines, part_start,
                lambda line: bool(re.fullmatch(r"Part\s+(I{1,3}|IV|V)", line, re.IGNORECASE))
                or bool(re.fullmatch(r"Annex\s+[IVX]+", line, re.IGNORECASE)),
            )
            if part == "I" and paragraph_numbers and letter_points:
                scopes = [
                    _letter_point_scope(lines, part_start + 1, part_end, paragraph, point)
                    for paragraph in paragraph_numbers
                    for point in letter_points
                ]
                scopes = [scope for scope in scopes if scope]
                if scopes:
                    return "\n".join(scopes)
            elif paragraph_numbers:
                scopes = [
                    _parenthesized_scope(lines, part_start + 1, part_end, n)
                    for n in paragraph_numbers
                ]
                scopes = [scope for scope in scopes if scope]
                if not scopes:
                    scopes = [
                        _paragraph_scope(lines, part_start + 1, part_end, n)
                        for n in paragraph_numbers
                    ]
                    scopes = [scope for scope in scopes if scope]
                if scopes:
                    return "\n".join(scopes)
            else:
                continue
    return None


def extract_locator_scope(locator, source_text):
    """Return the exact Article paragraph or Annex Part/point text, else None."""
    if not isinstance(locator, str) or not locator.strip():
        return None
    lines = _source_lines(source_text)
    if re.search(r"\bArticle\s+\d+\b", locator, re.IGNORECASE):
        return _article_scope(locator, lines)
    if re.search(r"\bAnnex\s+[IVX]+\b", locator, re.IGNORECASE):
        return _annex_scope(locator, lines)
    return None


def _locator_is_present(locator, source_text):
    return extract_locator_scope(locator, source_text) is not None


def _quote_is_in_locator_scope(locator, quote, source_text):
    scope = extract_locator_scope(locator, source_text)
    return bool(scope) and _normalized(quote) in _normalized(scope)


def _legal_locator_lines(report):
    match = re.search(
        r"(?:규격 근거|상세 내용)\s*[:：]?\s*(.*?)(?=출처 자료|Source:|출처 원문|Raw Text Quote|$)",
        report,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return []
    return match.group(1).splitlines()


def validate_claim_evidence(report, source):
    """Validate claim IDs, exact source quotes, and paragraph/point-scoped locators."""
    if not isinstance(report, str):
        return False, "보고서가 문자열이 아닙니다."
    if not isinstance(source, dict) or not isinstance(source.get("sources"), list):
        return False, "공식 source pack 구조가 올바르지 않습니다."

    blocks = CLAIM_BLOCK_PATTERN.findall(report)
    if len(blocks) != 1:
        return False, "CLAIM_EVIDENCE_JSON 구조화 근거 블록은 정확히 1개여야 합니다."
    try:
        payload = json.loads(blocks[0])
    except (TypeError, ValueError):
        return False, "CLAIM_EVIDENCE_JSON이 유효한 JSON이 아닙니다."
    if not isinstance(payload, dict) or not isinstance(payload.get("claims"), list):
        return False, "근거 JSON에 claims 배열이 없습니다."
    claims = payload["claims"]
    if not claims:
        return False, "근거 JSON에 검증할 주장이 없습니다."

    source_by_id = {
        item.get("id"): item
        for item in source["sources"]
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    seen_ids = set()
    declared_ids = set()
    legal_count = 0
    body = CLAIM_EVIDENCE_JSON_BLOCK_REMOVER.sub("", report)
    normalized_body = _normalized(body)

    for index, claim in enumerate(claims, start=1):
        if not isinstance(claim, dict):
            return False, f"주장 {index}번 항목이 객체가 아닙니다."
        claim_id = claim.get("claim_id")
        category = claim.get("category")
        statement = claim.get("statement")
        if not isinstance(claim_id, str) or not re.fullmatch(r"C-\d{3,}", claim_id):
            return False, f"주장 {index}번의 claim_id 형식이 올바르지 않습니다."
        if claim_id in seen_ids:
            return False, f"중복 claim_id가 있습니다: {claim_id}"
        seen_ids.add(claim_id)
        declared_ids.add(claim_id)

        if not isinstance(category, str) or category not in ALLOWED_CATEGORIES:
            return False, f"{claim_id}: 허용되지 않은 주장 분류입니다."
        if not isinstance(statement, str) or len(statement.strip()) < 10:
            return False, f"{claim_id}: 주장 내용이 없거나 너무 짧습니다."
        if _normalized(statement) not in normalized_body:
            return False, f"{claim_id}: JSON statement가 본문에 그대로 연결되지 않습니다."

        if category in {"legal_requirement", "official_explanation"}:
            if category == "legal_requirement":
                legal_count += 1
            source_id = claim.get("source_id")
            locator = claim.get("locator")
            quote = claim.get("quote")
            if not isinstance(source_id, str) or source_id not in source_by_id:
                return False, f"{claim_id}: 등록되지 않은 공식 source_id입니다."
            if not isinstance(locator, str) or len(locator.strip()) < 3:
                return False, f"{claim_id}: 근거 locator/페이지 위치가 없습니다."
            source_text = source_by_id[source_id].get("text", "")
            if not isinstance(quote, str) or len(quote.strip()) < 50:
                return False, f"{claim_id}: 직접 인용문은 50자 이상이어야 합니다."
            if _normalized(quote) not in _normalized(source_text):
                return False, f"{claim_id}: 직접 인용문이 지정 source_id 원문과 일치하지 않습니다."
            if category == "legal_requirement":
                scope = extract_locator_scope(locator, source_text)
                if not scope:
                    return False, f"{claim_id}: 지정한 Article paragraph/Annex Part-point locator가 원문에서 확인되지 않습니다."
                if _normalized(quote) not in _normalized(scope):
                    return False, f"{claim_id}: 직접 인용문이 지정한 paragraph/point 범위 안에서 확인되지 않습니다."
        else:
            basis = claim.get("basis")
            if not isinstance(basis, str) or len(basis.strip()) < 10:
                return False, f"{claim_id}: 해석/엔지니어링 권고의 근거 설명이 없습니다."
            optional_source_id = claim.get("source_id")
            if optional_source_id is not None and (
                not isinstance(optional_source_id, str)
                or optional_source_id not in source_by_id
            ):
                return False, f"{claim_id}: 등록되지 않은 source_id입니다."

    if legal_count == 0:
        return False, "법적 주장으로 분류된 항목이 없습니다."

    for line in _legal_locator_lines(body):
        if re.search(r"\bArticle\s+\d+\b|\bAnnex\s+[IVX]+\b", line, re.IGNORECASE):
            if not CLAIM_REFERENCE_PATTERN.search(line):
                return False, "규격 근거의 Article/Annex 주장 줄에 claim ID가 없습니다."

    referenced_ids = set(CLAIM_REFERENCE_PATTERN.findall(body))
    if referenced_ids != declared_ids:
        unknown = sorted(referenced_ids - declared_ids)
        missing = sorted(declared_ids - referenced_ids)
        if unknown:
            return False, "근거 JSON에 선언되지 않은 claim_id가 본문에 있습니다: " + ", ".join(unknown)
        return False, "본문에서 참조되지 않은 claim_id가 있습니다: " + ", ".join(missing)

    return True, ""
