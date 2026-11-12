import json
import unittest
from types import SimpleNamespace

from cra_report_contract import (
    CRA_REPORT_SCHEMA,
    ReportGenerationError,
    ReportValidationError,
    generate_validated_report,
    parse_and_validate_report,
    render_report,
)


def valid_payload():
    return {
        "schema_version": "cra-research-v2",
        "topic": "CRA 취약점 처리",
        "summary_ko": "원문 검증 전의 조사 초안이다.",
        "claims": [
            {
                "claim_id": "C-001",
                "claim_type": "LAW_REQUIREMENT",
                "claim_text_ko": "취약점 처리 요구사항 후보를 검토한다.",
                "legal_location_candidate": "Annex I Part II",
                "source_title_candidate": "Regulation (EU) 2024/2847",
                "publisher_candidate": "European Union",
                "source_url_candidate": "",
                "document_version_candidate": "",
                "source_excerpt": "",
                "excerpt_type": "NONE",
                "legal_location_status": "UNVERIFIED",
                "product_applicability": "UNVERIFIED",
                "limitations": "원문 및 제품 적용성 미확인",
            }
        ],
        "counterchecks": ["조항 위치를 EUR-Lex 원문으로 대조해야 한다."],
        "limitations": ["원문 수집 단계가 구현되지 않았다."],
        "overall_status": "UNVERIFIED",
    }


class FakeModels:
    def __init__(self, outcomes):
        self.outcomes = list(outcomes)
        self.calls = []

    def generate_content(self, **kwargs):
        self.calls.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return SimpleNamespace(text=outcome)


class ContractTests(unittest.TestCase):
    def config_factory(self, **kwargs):
        return kwargs

    def test_valid_json_and_markdown_render(self):
        payload = parse_and_validate_report(json.dumps(valid_payload(), ensure_ascii=False))
        rendered = render_report(payload)
        self.assertIn("Overall status:** UNVERIFIED", rendered)
        self.assertIn("직접 인용: 없음", rendered)

    def test_empty_response_rejected(self):
        with self.assertRaises(ReportValidationError):
            parse_and_validate_report("  ")

    def test_invalid_json_rejected(self):
        with self.assertRaises(ReportValidationError):
            parse_and_validate_report("{not-json")

    def test_missing_top_level_field_rejected(self):
        payload = valid_payload()
        del payload["counterchecks"]
        with self.assertRaises(ReportValidationError):
            parse_and_validate_report(json.dumps(payload))

    def test_model_cannot_promote_verified(self):
        payload = valid_payload()
        payload["overall_status"] = "VERIFIED"
        with self.assertRaises(ReportValidationError):
            parse_and_validate_report(json.dumps(payload))

    def test_direct_quote_without_source_bundle_rejected(self):
        payload = valid_payload()
        payload["claims"][0]["source_excerpt"] = "Invented legal quote"
        payload["claims"][0]["excerpt_type"] = "VERBATIM_FROM_INPUT"
        with self.assertRaises(ReportValidationError):
            parse_and_validate_report(json.dumps(payload))

    def test_model_fallback_after_invalid_json(self):
        first = json.dumps(valid_payload(), ensure_ascii=False)
        models = FakeModels(["not-json", first])
        payload, markdown, model = generate_validated_report(
            SimpleNamespace(models=models),
            ["model-a", "model-b"],
            "test prompt",
            self.config_factory,
            max_retries=1,
        )
        self.assertEqual(model, "model-b")
        self.assertEqual(payload["overall_status"], "UNVERIFIED")
        self.assertIn("CRA Research Report", markdown)
        self.assertEqual(len(models.calls), 2)
        self.assertEqual(models.calls[0]["config"]["response_mime_type"], "application/json")
        self.assertEqual(
            models.calls[0]["config"]["response_json_schema"],
            CRA_REPORT_SCHEMA,
        )

    def test_all_model_failures_raise_without_success_result(self):
        models = FakeModels([RuntimeError("secret-like provider detail"), RuntimeError("unavailable")])
        with self.assertRaises(ReportGenerationError) as caught:
            generate_validated_report(
                SimpleNamespace(models=models),
                ["model-a", "model-b"],
                "test prompt",
                self.config_factory,
                max_retries=1,
            )
        self.assertNotIn("secret-like", str(caught.exception))
        self.assertEqual(len(models.calls), 2)

    def test_empty_response_retries_then_fails_closed(self):
        models = FakeModels(["", "   "])
        with self.assertRaises(ReportGenerationError):
            generate_validated_report(
                SimpleNamespace(models=models),
                ["model-a", "model-b"],
                "test prompt",
                self.config_factory,
                max_retries=1,
            )
        self.assertEqual(len(models.calls), 2)


if __name__ == "__main__":
    unittest.main()
