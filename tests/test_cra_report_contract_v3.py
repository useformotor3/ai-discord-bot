import copy
import json
import unittest
from pathlib import Path

from cra_report_contract_v3 import (
    CRA_REPORT_V3_SCHEMA,
    ReportV3ValidationError,
    load_schema_file,
    parse_and_validate_report_v3,
    render_report_v3,
    validate_report_v3,
)
from evidence_bundle import build_evidence_bundle
from source_evidence import FetchMetadata, FetchResult, SOURCE_REGISTRY
from source_extraction import extract_html_document
from datetime import datetime, timezone


def fixture_bundle():
    source_id = "ST_AN5156_REV14"
    source = SOURCE_REGISTRY[source_id]
    raw = b"<html><body><p>Debug controls and secure update.</p></body></html>"
    metadata = FetchMetadata(
        source_id=source_id,
        canonical_url=source.canonical_url,
        final_url=source.canonical_url,
        publisher=source.publisher,
        title=source.title,
        document_identifier=source.document_identifier,
        revision=source.revision,
        published_or_revision_date=source.revision,
        fetched_at_utc=datetime(2026, 11, 13, tzinfo=timezone.utc).isoformat(),
        http_status=200,
        mime_type="text/html",
        byte_count=len(raw),
        sha256=__import__("hashlib").sha256(raw).hexdigest(),
        extraction_method="NONE_PHASE_A_RAW_BYTES_ONLY",
        status="FETCHED",
    )
    return build_evidence_bundle(
        FetchResult(metadata, raw), extract_html_document(source_id, raw)
    )


def valid_payload(bundle):
    return {
        "schema_version": "cra-research-v3",
        "topic": "CRA 보안 기능 검토",
        "summary_ko": "Bundle과 연결된 검토 초안.",
        "claims": [{
            "claim_id": "C-001",
            "claim_type": "RISK_BASED_DESIGN_OPTION",
            "claim_text_ko": "디버그 수명주기 통제를 검토한다.",
            "legal_location_candidate": "",
            "evidence_ids": [bundle["evidence"][0]["evidence_id"]],
            "legal_location_status": "UNVERIFIED",
            "product_applicability": "UNVERIFIED",
            "limitations": ["제품별 적용성은 미확인"],
        }],
        "counterchecks": ["해당 MCU 주문 코드의 기능 범위를 확인해야 한다."],
        "limitations": ["의미 검증은 아직 수행하지 않았다."],
        "overall_status": "UNVERIFIED",
    }


class ContractV3Tests(unittest.TestCase):
    def setUp(self):
        self.bundle = fixture_bundle()
        self.payload = valid_payload(self.bundle)

    def test_schema_file_matches_python_schema(self):
        self.assertEqual(load_schema_file(), CRA_REPORT_V3_SCHEMA)

    def test_valid_payload_and_render_linked_evidence(self):
        parsed = parse_and_validate_report_v3(
            json.dumps(self.payload, ensure_ascii=False), self.bundle
        )
        rendered = render_report_v3(parsed, self.bundle)
        self.assertIn("BUNDLE_LINKED_UNVERIFIED", rendered)
        self.assertIn(self.bundle["evidence"][0]["evidence_id"], rendered)
        self.assertIn(self.bundle["sources"][0]["final_url"], rendered)
        self.assertIn("의미적 적합성", rendered)

    def test_empty_evidence_means_no_evidence(self):
        self.payload["claims"][0]["evidence_ids"] = []
        rendered = render_report_v3(self.payload, self.bundle)
        self.assertIn("NO_EVIDENCE", rendered)

    def test_unknown_evidence_id_rejected(self):
        self.payload["claims"][0]["evidence_ids"] = ["EV-NOT-IN-BUNDLE"]
        with self.assertRaisesRegex(ReportV3ValidationError, "unknown evidence"):
            validate_report_v3(self.payload, self.bundle)

    def test_duplicate_evidence_ids_rejected(self):
        evidence_id = self.bundle["evidence"][0]["evidence_id"]
        self.payload["claims"][0]["evidence_ids"] = [evidence_id, evidence_id]
        with self.assertRaisesRegex(ReportV3ValidationError, "duplicated"):
            validate_report_v3(self.payload, self.bundle)

    def test_verified_status_promotion_rejected(self):
        self.payload["overall_status"] = "VERIFIED"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)

    def test_partial_status_promotion_rejected(self):
        self.payload["overall_status"] = "PARTIALLY_VERIFIED"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)

    def test_claim_location_and_product_status_cannot_be_promoted(self):
        self.payload["claims"][0]["legal_location_status"] = "VERIFIED"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)
        self.payload = valid_payload(self.bundle)
        self.payload["claims"][0]["product_applicability"] = "APPLICABLE"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)

    def test_unrecognized_fields_rejected(self):
        self.payload["claims"][0]["invented_quote"] = "not allowed"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)

    def test_duplicate_claim_ids_rejected(self):
        self.payload["claims"].append(copy.deepcopy(self.payload["claims"][0]))
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, self.bundle)

    def test_invalid_json_and_empty_response_rejected(self):
        with self.assertRaises(ReportV3ValidationError):
            parse_and_validate_report_v3("{bad", self.bundle)
        with self.assertRaises(ReportV3ValidationError):
            parse_and_validate_report_v3(" ", self.bundle)

    def test_invalid_bundle_rejected_before_report(self):
        broken = copy.deepcopy(self.bundle)
        broken["evidence"][0]["excerpt"] += " forged"
        with self.assertRaises(ReportV3ValidationError):
            validate_report_v3(self.payload, broken)

    def test_prompt_contract_has_no_quote_generation_or_status_promotion(self):
        prompt = (Path(__file__).resolve().parents[1] / "prompts" /
                  "CRA_RESEARCH_PROMPT_V3.txt").read_text(encoding="utf-8")
        self.assertIn('schema_version은 "cra-research-v3"', prompt)
        self.assertIn("overall_status는 반드시 UNVERIFIED", prompt)
        self.assertIn("직접 인용도 생성하지 않는다", prompt)
        self.assertIn("evidence_ids", prompt)


if __name__ == "__main__":
    unittest.main()
