"""Phase C v3 CRA report contract; intentionally separate from the v2 runtime."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from evidence_bundle import validate_evidence_bundle

SCHEMA_VERSION = "cra-research-v3"
CLAIM_TYPES = {
    "LAW_REQUIREMENT", "RISK_BASED_DESIGN_OPTION", "PRODUCT_SPECIFIC_FACT",
    "INTERPRETATION", "ASSUMPTION",
}
REPORT_STATUSES = {"UNVERIFIED"}
CLAIM_FIELDS = (
    "claim_id", "claim_type", "claim_text_ko", "legal_location_candidate",
    "evidence_ids", "legal_location_status", "product_applicability", "limitations",
)
REPORT_FIELDS = (
    "schema_version", "topic", "summary_ko", "claims", "counterchecks",
    "limitations", "overall_status",
)


def _string_array():
    return {"type": "array", "items": {"type": "string"}}


CRA_REPORT_V3_SCHEMA: dict[str, Any] = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "schema_version": {"type": "string", "enum": [SCHEMA_VERSION]},
        "topic": {"type": "string"},
        "summary_ko": {"type": "string"},
        "claims": {
            "type": "array", "minItems": 1, "maxItems": 50,
            "items": {
                "type": "object",
                "properties": {
                    "claim_id": {"type": "string"},
                    "claim_type": {"type": "string", "enum": sorted(CLAIM_TYPES)},
                    "claim_text_ko": {"type": "string"},
                    "legal_location_candidate": {"type": "string"},
                    "evidence_ids": {
                        "type": "array", "maxItems": 10, "uniqueItems": True,
                        "items": {"type": "string"},
                    },
                    "legal_location_status": {"type": "string", "enum": ["UNVERIFIED"]},
                    "product_applicability": {"type": "string", "enum": ["UNVERIFIED"]},
                    "limitations": _string_array(),
                },
                "required": list(CLAIM_FIELDS),
                "additionalProperties": False,
            },
        },
        "counterchecks": _string_array(),
        "limitations": _string_array(),
        "overall_status": {"type": "string", "enum": sorted(REPORT_STATUSES)},
    },
    "required": list(REPORT_FIELDS),
    "additionalProperties": False,
}


class ReportV3ValidationError(ValueError):
    """The model output or evidence references violate the v3 contract."""


def validate_report_v3(payload: Any, evidence_bundle: Any) -> dict[str, Any]:
    try:
        bundle = validate_evidence_bundle(evidence_bundle)
    except Exception as exc:
        raise ReportV3ValidationError("evidence bundle failed validation") from exc
    if not isinstance(payload, dict) or set(payload) != set(REPORT_FIELDS):
        raise ReportV3ValidationError("top-level fields mismatch")
    if payload["schema_version"] != SCHEMA_VERSION:
        raise ReportV3ValidationError("unsupported schema_version")
    for field in ("topic", "summary_ko"):
        if not isinstance(payload[field], str) or not payload[field].strip():
            raise ReportV3ValidationError(f"{field} must be a non-empty string")
    if payload["overall_status"] != "UNVERIFIED":
        raise ReportV3ValidationError("overall_status must remain UNVERIFIED")
    for field in ("counterchecks", "limitations"):
        if not isinstance(payload[field], list) or not all(isinstance(v, str) for v in payload[field]):
            raise ReportV3ValidationError(f"{field} must be an array of strings")
    if not isinstance(payload["claims"], list) or not 1 <= len(payload["claims"]) <= 50:
        raise ReportV3ValidationError("claims must contain 1..50 entries")

    known_evidence = {item["evidence_id"] for item in bundle["evidence"]}
    seen_claim_ids: set[str] = set()
    for index, claim in enumerate(payload["claims"]):
        prefix = f"claims[{index}]"
        if not isinstance(claim, dict) or set(claim) != set(CLAIM_FIELDS):
            raise ReportV3ValidationError(f"{prefix} fields mismatch")
        for field in ("claim_id", "claim_type", "claim_text_ko", "legal_location_status",
                      "product_applicability"):
            if not isinstance(claim[field], str) or not claim[field].strip():
                raise ReportV3ValidationError(f"{prefix}.{field} must be non-empty")
        if claim["claim_id"] in seen_claim_ids:
            raise ReportV3ValidationError(f"{prefix}.claim_id duplicated")
        seen_claim_ids.add(claim["claim_id"])
        if claim["claim_type"] not in CLAIM_TYPES:
            raise ReportV3ValidationError(f"{prefix}.claim_type invalid")
        if claim["legal_location_status"] != "UNVERIFIED":
            raise ReportV3ValidationError(f"{prefix}.legal_location_status must remain UNVERIFIED")
        if claim["product_applicability"] != "UNVERIFIED":
            raise ReportV3ValidationError(f"{prefix}.product_applicability must remain UNVERIFIED")
        if not isinstance(claim["legal_location_candidate"], str):
            raise ReportV3ValidationError(f"{prefix}.legal_location_candidate must be a string")
        if not isinstance(claim["limitations"], list) or not all(
            isinstance(value, str) for value in claim["limitations"]
        ):
            raise ReportV3ValidationError(f"{prefix}.limitations must be an array of strings")
        references = claim["evidence_ids"]
        if not isinstance(references, list) or len(references) > 10:
            raise ReportV3ValidationError(f"{prefix}.evidence_ids invalid")
        if not all(isinstance(value, str) and value for value in references):
            raise ReportV3ValidationError(f"{prefix}.evidence_ids must contain non-empty strings")
        if len(references) != len(set(references)):
            raise ReportV3ValidationError(f"{prefix}.evidence_ids duplicated")
        unknown = sorted(set(references) - known_evidence)
        if unknown:
            raise ReportV3ValidationError(f"{prefix} references unknown evidence IDs")

    return payload


def parse_and_validate_report_v3(response_text: str | None, evidence_bundle: Any) -> dict[str, Any]:
    if not isinstance(response_text, str) or not response_text.strip():
        raise ReportV3ValidationError("model response is empty")
    try:
        payload = json.loads(response_text)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ReportV3ValidationError("model response is not valid JSON") from exc
    return validate_report_v3(payload, evidence_bundle)


def render_report_v3(payload: dict[str, Any], evidence_bundle: Any) -> str:
    validate_report_v3(payload, evidence_bundle)
    sources = {source["source_id"]: source for source in evidence_bundle["sources"]}
    evidence_map = {item["evidence_id"]: item for item in evidence_bundle["evidence"]}
    lines = [
        "# CRA Research Report",
        "",
        f"**Schema:** {SCHEMA_VERSION}",
        "**Overall status:** UNVERIFIED",
        "",
        "## 주제",
        payload["topic"],
        "",
        "## 요약",
        payload["summary_ko"],
        "",
        "## 주장별 분석",
    ]
    for claim in payload["claims"]:
        lines.extend(["", f"### {claim['claim_id']} — {claim['claim_type']}",
                      claim["claim_text_ko"],
                      f"- 조항 후보: {claim['legal_location_candidate'] or '미기재'}",
                      "- 법령 위치 상태: UNVERIFIED",
                      "- 제품 적용성: UNVERIFIED",
                      f"- 제한사항: {'; '.join(claim['limitations']) or '없음'}"])
        if not claim["evidence_ids"]:
            lines.append("- 증거 연결: NO_EVIDENCE")
            continue
        lines.append("- 증거 연결: BUNDLE_LINKED_UNVERIFIED")
        for evidence_id in claim["evidence_ids"]:
            item = evidence_map[evidence_id]
            source = sources[item["source_id"]]
            lines.extend([
                f"  - Evidence ID: {evidence_id}",
                f"    - 출처: {source['publisher']} — {source['title']}",
                f"    - 문서: {source['document_identifier']} / {source['revision']}",
                f"    - 위치 후보: {item['locator']}",
                f"    - URL: {source['final_url']}",
                f"    - 원문 발췌 후보: {item['excerpt']}",
                f"    - 발췌 SHA-256: {item['excerpt_sha256']}",
            ])
    lines.extend(["", "## 반증·교차 확인 항목"])
    lines.extend([f"- {item}" for item in payload["counterchecks"]] or ["- 없음"])
    lines.extend(["", "## 전체 제한사항"])
    lines.extend([f"- {item}" for item in payload["limitations"]] or ["- 없음"])
    lines.extend([
        "",
        "> 주의: Evidence ID 연결은 출처·발췌의 무결성 및 출처 추적성을 보조할 뿐,",
        "> 주장과 원문 사이의 의미적 적합성·법적 해석·제품 적용성을 검증하지 않는다.",
        "> 모든 주장은 UNVERIFIED이며 사람의 별도 검토가 필요하다.",
    ])
    return "\n".join(lines)


def load_schema_file() -> dict[str, Any]:
    """Load the checked-in JSON Schema for parity tests and tooling."""
    path = Path(__file__).resolve().parent / "schemas" / "cra_research_v3.schema.json"
    return json.loads(path.read_text(encoding="utf-8"))
