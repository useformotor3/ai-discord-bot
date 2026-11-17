import json

import pytest

from cra_claims import validate_claim_evidence


SOURCE_ID = "CRA-2024-2847-consolidated"
QUOTE = (
    "Manufacturers shall ensure, when placing a product with digital elements on the market, "
    "and for the support period, that vulnerabilities of that product, including its components, "
    "are handled effectively and in accordance with the essential cybersecurity requirements "
    "set out in Part II of Annex I."
)
SOURCE_TEXT = "\n".join([
    "Article 13",
    "Obligations of manufacturers",
    "8.",
    QUOTE,
    "9.",
    "Manufacturers shall ensure that each security update remains available after it has been issued.",
    "Article 14",
    "Reporting obligations of manufacturers",
    "1.",
    "A manufacturer shall notify any actively exploited vulnerability.",
    "ANNEX I",
    "ESSENTIAL CYBERSECURITY REQUIREMENTS",
    "Part I",
    "(1)",
    "Products with digital elements shall be designed and developed securely.",
    "(2)",
    "The product with digital elements shall protect the availability, authenticity, integrity and confidentiality of data.",
    "(a)",
    "The product shall protect stored data.",
    "(b)",
    "The product shall prevent unauthorized access to user data.",
    "(f)",
    "The product shall protect the integrity of commands and configuration data.",
    "(g)",
    "The product shall log security-relevant events.",
    "Part II",
    "(5)",
    "Manufacturers shall have appropriate policies and procedures, including coordinated vulnerability disclosure policies.",
    "(6)",
    "Manufacturers shall facilitate the sharing of information about potential vulnerabilities.",
])
SOURCE = {
    "sources": [{
        "id": SOURCE_ID,
        "text": SOURCE_TEXT,
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
        "## 규격 근거 및 상세 내용\n"
        f"{claim['statement']} {body_ref}\n\n"
        "## 출처 자료\nEUR-Lex\n"
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
        ("locator", "Article 13(99)", "locator"),
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
            "## 규격 근거 및 상세 내용\n"
            + legal_claim["statement"] + " [C-001]\n"
            + recommendation["statement"] + " [C-002]\n"
            + "## 출처 자료\nEUR-Lex\nCLAIM_EVIDENCE_JSON\n```json\n"
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



def test_rejects_quote_from_a_different_article_even_when_locator_exists():
    unrelated_quote = (
        "The manufacturer shall provide a detailed report to the authority "
        "within the required period after the incident has been identified."
    )
    source = {
        "sources": [{
            "id": SOURCE_ID,
            "text": (
                "Article 13 (8) Obligations of manufacturers. "
                "This section contains a different requirement. "
                "Article 14 Reporting obligations. "
                + unrelated_quote
            ),
        }]
    }
    claim = {
        "claim_id": "C-001",
        "category": "legal_requirement",
        "statement": "제조자는 지원 기간 동안 취약점을 처리해야 한다.",
        "source_id": SOURCE_ID,
        "locator": "Article 13(8)",
        "quote": unrelated_quote,
    }
    valid, reason = validate_claim_evidence(make_report(claim), source)
    assert not valid
    assert "paragraph/point 범위" in reason
