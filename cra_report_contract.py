"""Structured CRA research response contract and fail-closed Gemini adapter.

This module deliberately has no filesystem, network, Discord, or Google SDK side effects.
"""
from __future__ import annotations

import json
from typing import Any, Callable, Iterable


SCHEMA_VERSION = "cra-research-v2"
CLAIM_TYPES = {
    "LAW_REQUIREMENT",
    "RISK_BASED_DESIGN_OPTION",
    "PRODUCT_SPECIFIC_FACT",
    "INTERPRETATION",
    "ASSUMPTION",
}
REPORT_STATUSES = {"UNVERIFIED"}

CLAIM_FIELDS = (
    "claim_id",
    "claim_type",
    "claim_text_ko",
    "legal_location_candidate",
    "source_title_candidate",
    "publisher_candidate",
    "source_url_candidate",
    "document_version_candidate",
    "source_excerpt",
    "excerpt_type",
    "legal_location_status",
    "product_applicability",
    "limitations",
)
REPORT_FIELDS = (
    "schema_version",
    "topic",
    "summary_ko",
    "claims",
    "counterchecks",
    "limitations",
    "overall_status",
)

CRA_REPORT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "schema_version": {"type": "string", "enum": [SCHEMA_VERSION]},
        "topic": {"type": "string"},
        "summary_ko": {"type": "string"},
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim_id": {"type": "string"},
                    "claim_type": {"type": "string", "enum": sorted(CLAIM_TYPES)},
                    "claim_text_ko": {"type": "string"},
                    "legal_location_candidate": {"type": "string"},
                    "source_title_candidate": {"type": "string"},
                    "publisher_candidate": {"type": "string"},
                    "source_url_candidate": {"type": "string"},
                    "document_version_candidate": {"type": "string"},
                    "source_excerpt": {"type": "string"},
                    "excerpt_type": {"type": "string", "enum": ["NONE"]},
                    "legal_location_status": {"type": "string", "enum": ["UNVERIFIED"]},
                    "product_applicability": {
                        "type": "string",
                        "enum": ["UNVERIFIED", "NOT_APPLICABLE_PENDING_EVIDENCE"],
                    },
                    "limitations": {"type": "string"},
                },
                "required": list(CLAIM_FIELDS),
                "additionalProperties": False,
            },
        },
        "counterchecks": {"type": "array", "items": {"type": "string"}},
        "limitations": {"type": "array", "items": {"type": "string"}},
        "overall_status": {"type": "string", "enum": sorted(REPORT_STATUSES)},
    },
    "required": list(REPORT_FIELDS),
    "additionalProperties": False,
}


class ReportValidationError(ValueError):
    """The model output violates the controlled report contract."""


class ReportGenerationError(RuntimeError):
    """No model produced a valid report after the configured attempts."""


def _require_string(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ReportValidationError(f"{field} must be a non-empty string")


def validate_report(payload: Any) -> dict[str, Any]:
    """Validate structure and enforce the no-source/no-quote phase boundary."""
    if not isinstance(payload, dict):
        raise ReportValidationError("top-level JSON value must be an object")
    if set(payload) != set(REPORT_FIELDS):
        missing = sorted(set(REPORT_FIELDS) - set(payload))
        extra = sorted(set(payload) - set(REPORT_FIELDS))
        raise ReportValidationError(f"top-level fields mismatch; missing={missing}, extra={extra}")

    if payload["schema_version"] != SCHEMA_VERSION:
        raise ReportValidationError("unsupported schema_version")
    _require_string(payload["topic"], "topic")
    _require_string(payload["summary_ko"], "summary_ko")
    if not isinstance(payload["overall_status"], str) or payload["overall_status"] not in REPORT_STATUSES:
        raise ReportValidationError("overall_status cannot be VERIFIED or an unknown value")

    if not isinstance(payload["claims"], list) or not payload["claims"]:
        raise ReportValidationError("claims must be a non-empty array")
    if not isinstance(payload["counterchecks"], list) or not all(
        isinstance(item, str) for item in payload["counterchecks"]
    ):
        raise ReportValidationError("counterchecks must be an array of strings")
    if not isinstance(payload["limitations"], list) or not all(
        isinstance(item, str) for item in payload["limitations"]
    ):
        raise ReportValidationError("limitations must be an array of strings")

    seen_ids: set[str] = set()
    for index, claim in enumerate(payload["claims"]):
        prefix = f"claims[{index}]"
        if not isinstance(claim, dict) or set(claim) != set(CLAIM_FIELDS):
            raise ReportValidationError(f"{prefix} fields mismatch")
        optional_text_fields = {
            "legal_location_candidate",
            "source_title_candidate",
            "publisher_candidate",
            "source_url_candidate",
            "document_version_candidate",
            "source_excerpt",
        }
        for field in CLAIM_FIELDS:
            if field in optional_text_fields:
                if not isinstance(claim[field], str):
                    raise ReportValidationError(f"{prefix}.{field} must be a string")
            else:
                _require_string(claim[field], f"{prefix}.{field}")
        if claim["claim_id"] in seen_ids:
            raise ReportValidationError(f"{prefix}.claim_id is duplicated")
        seen_ids.add(claim["claim_id"])
        if claim["claim_type"] not in CLAIM_TYPES:
            raise ReportValidationError(f"{prefix}.claim_type is invalid")
        if claim["excerpt_type"] != "NONE" or claim["source_excerpt"] != "":
            raise ReportValidationError(
                f"{prefix} must not contain quotations before source retrieval is implemented"
            )
        if claim["legal_location_status"] != "UNVERIFIED":
            raise ReportValidationError(f"{prefix}.legal_location_status must remain UNVERIFIED")
        if claim["product_applicability"] not in {
            "UNVERIFIED",
            "NOT_APPLICABLE_PENDING_EVIDENCE",
        }:
            raise ReportValidationError(f"{prefix}.product_applicability is invalid")

    return payload


def parse_and_validate_report(response_text: str | None) -> dict[str, Any]:
    if not isinstance(response_text, str) or not response_text.strip():
        raise ReportValidationError("model response is empty")
    try:
        payload = json.loads(response_text)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ReportValidationError("model response is not valid JSON") from exc
    return validate_report(payload)


def render_report(payload: dict[str, Any]) -> str:
    """Render a validated JSON payload into the existing Markdown archive format."""
    validate_report(payload)
    lines = [
        "# CRA Research Report",
        "",
        f"**Schema:** {payload['schema_version']}",
        f"**Overall status:** {payload['overall_status']}",
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
        lines.extend(
            [
                "",
                f"### {claim['claim_id']} — {claim['claim_type']}",
                claim["claim_text_ko"],
                f"- 조항 후보: {claim['legal_location_candidate'] or '미기재'}",
                f"- 출처 후보: {claim['source_title_candidate'] or '미기재'}",
                f"- 발행기관 후보: {claim['publisher_candidate'] or '미기재'}",
                f"- URL 후보: {claim['source_url_candidate'] or '미기재'}",
                f"- 문서 버전 후보: {claim['document_version_candidate'] or '미기재'}",
                "- 직접 인용: 없음 (원문 수집 단계 미구현)",
                f"- 법령 위치 상태: {claim['legal_location_status']}",
                f"- 제품 적용성: {claim['product_applicability']}",
                f"- 제한사항: {claim['limitations']}",
            ]
        )
    lines.extend(["", "## 반증·교차 확인 항목"])
    lines.extend([f"- {item}" for item in payload["counterchecks"]] or ["- 없음"])
    lines.extend(["", "## 전체 제한사항"])
    lines.extend([f"- {item}" for item in payload["limitations"]] or ["- 없음"])
    lines.extend(
        [
            "",
            "> 주의: 이 결과는 원문 수집·조항·제품 적용성 검증 전의 AI 초안이다. "
            "UNVERIFIED 상태이며 법률 자문 또는 적합성 판정이 아니다.",
        ]
    )
    return "\n".join(lines)


def generate_validated_report(
    client: Any,
    models: Iterable[str],
    prompt: str,
    config_factory: Callable[..., Any],
    *,
    max_retries: int = 3,
    retry_delay: float = 5,
    sleeper: Callable[[float], None] = lambda _seconds: None,
    logger: Callable[[str], None] = print,
) -> tuple[dict[str, Any], str, str]:
    """Try model fallbacks; return payload, Markdown, and model name or fail closed."""
    errors: list[str] = []
    for model_name in models:
        for attempt in range(1, max_retries + 1):
            try:
                config = config_factory(
                    response_mime_type="application/json",
                    response_json_schema=CRA_REPORT_SCHEMA,
                )
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=config,
                )
                payload = parse_and_validate_report(getattr(response, "text", None))
                return payload, render_report(payload), model_name
            except Exception as exc:  # model/API/parse/validation errors all fail closed
                error_type = type(exc).__name__
                errors.append(f"{model_name} attempt {attempt}: {error_type}")
                logger(f"Model {model_name} attempt {attempt} failed ({error_type}).")
                if attempt < max_retries:
                    sleeper(retry_delay)
    summary = "; ".join(errors) if errors else "no model configured"
    raise ReportGenerationError(f"No valid CRA report generated: {summary}")
