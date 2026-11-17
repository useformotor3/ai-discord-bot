import json

import pytest

from cra_claims import validate_claim_evidence


SOURCE_ID = "CRA-2024-2847-consolidated"
QUOTE = (
    "The manufacturer shall ensure that, for the support period, "
    "vulnerabilities of the product with digital elements are handled effectively."
)
SOURCE = {
    "sources": [{
        "id": SOURCE_ID,
        "text": "Article 13 (8) Obligations of manufacturers " + QUOTE,
    }]
}


def make_report(claim=None, *, body_ref="[C-001]", raw_json=None):
    claim = claim or {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "제조자는 지원 기간 동안 취약점을 효과적으로 처리해야 한다.",
        "source_id": SOURCE_ID,
        "locator": "Article 13(8)",
        "quote": QUOTE,
    }
    encoded = raw_json if raw_json is not None else json.dumps(
        {"claims": [claim]}, ensure_ascii=False
    )
    return (
        "## 법적 주장 및 근거\n"
        f"제조자는 지원 기간 동안 취약점을 처리해야 한다. {body_ref}\n\n"
        "CLAIM_EVIDENCE_JSON\n```json\n"
        f"{encoded}\n"
        "```\n"
    )


def test_accepts_legal_claim_with_matching_source_locator_and_quote():
    assert validate_claim_evidence(make_report(), SOURCE) == (True, "")


@pytest.mark.parametrize(
    ("field", "value", "expected"),
    [
        ("source_id", "UNKNOWN-SOURCE", "등록되지 않은 공식 source_id"),
        ("locator", "Article 13(9)", "locator"),
        ("quote", "This quotation is not present in the retrieved official source text and is longer than fifty characters.", "일치하지 않습니다"),
    ],
)
def test_rejects_unverifiable_legal_claim_fields(field, value, expected):
    claim = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "제조자는 지원 기간 동안 취약점을 효과적으로 처리해야 한다.",
        "source_id": SOURCE_ID,
        "locator": "Article 13",
        "quote": QUOTE,
    }
    claim[field] = value
    valid, reason = validate_claim_evidence(make_report(claim), SOURCE)
    assert not valid
    assert expected in reason


def test_rejects_quote_shorter_than_minimum():
    claim = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "제조자는 취약점을 처리해야 한다.",
        "source_id": SOURCE_ID,
        "locator": "Article 13",
        "quote": "Too short",
    }
    valid, reason = validate_claim_evidence(make_report(claim), SOURCE)
    assert not valid
    assert "50자 이상" in reason


def test_rejects_missing_or_invalid_json_block():
    valid, reason = validate_claim_evidence("보고서 본문 [C-001]", SOURCE)
    assert not valid
    assert "정확히 1개" in reason

    valid, reason = validate_claim_evidence(
        make_report(raw_json="{invalid json"), SOURCE
    )
    assert not valid
    assert "유효한 JSON" in reason


def test_rejects_claim_not_referenced_in_body_and_unknown_reference():
    valid, reason = validate_claim_evidence(make_report(body_ref=""), SOURCE)
    assert not valid
    assert "본문에서 참조되지 않은" in reason

    valid, reason = validate_claim_evidence(make_report(body_ref="[C-999]"), SOURCE)
    assert not valid
    assert "선언되지 않은" in reason


def test_nonlegal_recommendation_must_be_explicitly_classified_and_explained():
    legal_claim = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "제조자는 지원 기간 동안 취약점을 효과적으로 처리해야 한다.",
        "source_id": SOURCE_ID,
        "locator": "Article 13(8)",
        "quote": QUOTE,
    }
    recommendation = {
        "claim_id": "C-002",
        "category": "engineering_recommendation",
        "statement": "보안 업데이트의 서명 검증을 구현한다.",
        "basis": "제품 위협 모델과 업데이트 무결성 위험을 낮추기 위한 엔지니어링 권고이며 CRA가 특정 알고리즘을 지정한 것은 아니다.",
    }

    def report_for_claims():
        payload = json.dumps(
            {"claims": [legal_claim, recommendation]}, ensure_ascii=False
        )
        return (
            "본문 [C-001] [C-002]\nCLAIM_EVIDENCE_JSON\n```json\n"
            + payload
            + "\n```"
        )

    valid, reason = validate_claim_evidence(report_for_claims(), SOURCE)
    assert valid, reason

    recommendation["basis"] = "짧음"
    valid, reason = validate_claim_evidence(report_for_claims(), SOURCE)
    assert not valid
    assert "근거 설명" in reason


def test_rejects_duplicate_claim_ids():
    report = make_report()
    payload = {
        "claims": [
            {
                "claim_id": "C-001",
                "category": "legal_requirement",
                "statement": "첫 번째 법적 주장입니다.",
                "source_id": SOURCE_ID,
                "locator": "Article 13",
                "quote": QUOTE,
            },
            {
                "claim_id": "C-001",
                "category": "legal_requirement",
                "statement": "두 번째 법적 주장입니다.",
                "source_id": SOURCE_ID,
                "locator": "Article 13",
                "quote": QUOTE,
            },
        ]
    }
    # Build a deterministic block rather than depending on serialized key order.
    report = (
        "본문 [C-001]\nCLAIM_EVIDENCE_JSON\n```json\n"
        + json.dumps(payload, ensure_ascii=False)
        + "\n```"
    )
    valid, reason = validate_claim_evidence(report, SOURCE)
    assert not valid
    assert "중복 claim_id" in reason
