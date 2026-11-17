"""Strict claim-to-evidence validation for CRA draft reports.

The validator proves only traceability to the retrieved source text. It does not
prove that a legal interpretation or product-scope conclusion is correct.
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
    r"CLAIM_EVIDENCE_JSON\s*\x60\x60\x60json\s*(.*?)\x60\x60\x60",
    re.IGNORECASE | re.DOTALL,
)
CLAIM_REFERENCE_PATTERN = re.compile(r"\[(C-\d{3,})\]")


def _normalized(value):
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def _locator_is_present(locator, source_text):
    """Require locator components to exist in the selected source text."""
    locator = str(locator or "").strip()
    if not locator:
        return False
    source = _normalized(source_text)
    normalized = _normalized(locator)
    if normalized in source:
        return True

    # EUR-Lex HTML may separate an article heading, paragraph and point with
    # whitespace or markup. Verify each explicit locator component in order.
    article = re.search(r"\bArticle\s+(\d+)\b", locator, re.IGNORECASE)
    annex = re.search(r"\bAnnex\s+([IVX]+)\b", locator, re.IGNORECASE)
    part = re.search(r"\bPart\s+(I{1,3}|IV|V)\b", locator, re.IGNORECASE)
    components = []
    if article:
        components.append(re.escape("Article " + article.group(1)))
    if annex:
        components.append(re.escape("Annex " + annex.group(1)))
    if part:
        components.append(re.escape("Part " + part.group(1)))
    if not components:
        return False
    if not all(re.search(component, source, re.IGNORECASE) for component in components):
        return False
    paragraph = re.search(r"\((\d+)\)", locator)
    point = re.search(r"\(([a-z])\)", locator, re.IGNORECASE)
    if paragraph and not re.search(r"\(" + re.escape(paragraph.group(1)) + r"\)", source):
        return False
    if point and not re.search(r"\(" + re.escape(point.group(1)) + r"\)", source, re.IGNORECASE):
        return False
    return True



def _quote_is_in_locator_scope(locator, quote, source_text):
    """Require the verbatim quote to occur inside the selected Article/Annex section."""
    normalized_source = _normalized(source_text)
    normalized_quote = _normalized(quote)
    if not normalized_quote:
        return False

    locator_text = str(locator or "")
    article = re.search(r"\\bArticle\\s+(\\d+)\\b", locator_text, re.IGNORECASE)
    annex = re.search(r"\\bAnnex\\s+([IVX]+)\\b", locator_text, re.IGNORECASE)
    if article:
        heading_pattern = re.compile(r"\\bArticle\\s+(\\d+)\\b", re.IGNORECASE)
        target_kind, target_value = "article", article.group(1)
    elif annex:
        heading_pattern = re.compile(r"\\bAnnex\\s+([IVX]+)\\b", re.IGNORECASE)
        target_kind, target_value = "annex", annex.group(1)
    else:
        return False

    matches = list(heading_pattern.finditer(normalized_source))
    for match in matches:
        if match.group(1).casefold() != target_value.casefold():
            continue
        end = len(normalized_source)
        if target_kind == "article":
            boundary = re.search(
                r"\\b(?:Article\\s+\\d+|Annex\\s+[IVX]+)\\b",
                normalized_source[match.end():],
                re.IGNORECASE,
            )
        else:
            boundary = re.search(
                r"\\bAnnex\\s+[IVX]+\\b",
                normalized_source[match.end():],
                re.IGNORECASE,
            )
        if boundary:
            end = match.end() + boundary.start()
        section = normalized_source[match.start():end]
        if normalized_quote in section:
            return True
    return False

def validate_claim_evidence(report, source):
    """Validate every declared claim and its in-body reference; fail closed."""
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

        if category in {"legal_requirement", "official_explanation"}:
            legal_count += 1
            source_id = claim.get("source_id")
            locator = claim.get("locator")
            quote = claim.get("quote")
            if not isinstance(source_id, str) or source_id not in source_by_id:
                return False, f"{claim_id}: 등록되지 않은 공식 source_id입니다."
            source_text = source_by_id[source_id].get("text", "")
            if not _locator_is_present(locator, source_text):
                return False, f"{claim_id}: 지정한 Article/Annex locator가 해당 원문에서 확인되지 않습니다."
            if not isinstance(quote, str) or len(quote.strip()) < 50:
                return False, f"{claim_id}: 직접 인용문은 50자 이상이어야 합니다."
            if _normalized(quote) not in _normalized(source_text):
                return False, f"{claim_id}: 직접 인용문이 지정 source_id 원문과 일치하지 않습니다."
            if not _quote_is_in_locator_scope(locator, quote, source_text):
                return False, f"{claim_id}: 직접 인용문이 지정한 Article/Annex 범위 안에서 확인되지 않습니다."
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

    body = CLAIM_EVIDENCE_JSON_BLOCK_REMOVER.sub("", report)
    referenced_ids = set(CLAIM_REFERENCE_PATTERN.findall(body))
    if referenced_ids != declared_ids:
        missing = sorted(declared_ids - referenced_ids)
        unknown = sorted(referenced_ids - declared_ids)
        if unknown:
            return False, "근거 JSON에 선언되지 않은 claim_id가 본문에 있습니다: " + ", ".join(unknown)
        return False, "본문에서 참조되지 않은 claim_id가 있습니다: " + ", ".join(missing)

    return True, ""


CLAIM_EVIDENCE_JSON_BLOCK_REMOVER = re.compile(
    r"CLAIM_EVIDENCE_JSON\s*\x60\x60\x60json\s*.*?\x60\x60\x60",
    re.IGNORECASE | re.DOTALL,
)
