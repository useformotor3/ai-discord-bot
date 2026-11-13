import copy
import hashlib
import unittest
from datetime import datetime, timezone

from evidence_bundle import build_evidence_bundle
from source_evidence import FetchMetadata, FetchResult, SOURCE_REGISTRY
from source_extraction import LegalUnit, extract_html_document
from evidence_quote_validator import (
    QuoteValidationError,
    build_human_review_packet,
    validate_evidence_quotes,
    validate_human_review_record,
    REVIEW_REQUIRED,
)


class QuoteValidatorTests(unittest.TestCase):
    def setUp(self):
        self.source_id = "ST_AN5156_REV14"
        self.source = SOURCE_REGISTRY[self.source_id]
        self.raw = (
            b"<html><head><title>Security note</title></head>"
            b"<body><h1>Introduction</h1><p>Debug lifecycle controls.</p>"
            b"<p>Secure firmware update overview.</p></body></html>"
        )
        self.fetch = FetchResult(
            metadata=FetchMetadata(
                source_id=self.source_id,
                canonical_url=self.source.canonical_url,
                final_url=self.source.canonical_url,
                publisher=self.source.publisher,
                title=self.source.title,
                document_identifier=self.source.document_identifier,
                revision=self.source.revision,
                published_or_revision_date=self.source.revision,
                fetched_at_utc=datetime(2026, 11, 13, tzinfo=timezone.utc).isoformat(),
                http_status=200, mime_type="text/html", byte_count=len(self.raw),
                sha256=hashlib.sha256(self.raw).hexdigest(),
                extraction_method="NONE_PHASE_A_RAW_BYTES_ONLY", status="FETCHED",
            ), content=self.raw,
        )
        self.document = extract_html_document(self.source_id, self.raw)
        self.bundle = build_evidence_bundle(self.fetch, self.document)
        self.report = {"claims": [{
            "claim_id": "C-001", "claim_text": "Debug lifecycle controls are discussed.",
            "evidence_ids": [self.bundle["evidence"][0]["evidence_id"]],
        }]}

    def test_exact_match_rebuilds_bundle_and_context(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, self.report)
        self.assertEqual(result["status"], "EXACT_MATCH")
        self.assertEqual(result["evidence"][0]["status"], "EXACT_MATCH")
        self.assertEqual(result["evidence"][0]["locator_class"], "TEXT_LINE_ONLY")
        self.assertEqual(result["claim_evidence"]["C-001"], self.report["claims"][0]["evidence_ids"])
        self.assertIn("EXACT_MATCH proves correspondence only", result["limitations"][0])

    def test_context_is_bounded_to_500_each_side(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, context_chars=500)
        item = result["evidence"][0]
        self.assertLessEqual(len(item["context_before"]), 500)
        self.assertLessEqual(len(item["context_after"]), 500)

    def test_context_limit_over_500_rejected(self):
        with self.assertRaisesRegex(QuoteValidationError, "INVALID_CONTEXT_LIMIT"):
            validate_evidence_quotes(self.fetch, self.document, self.bundle, context_chars=501)

    def test_missing_source_is_blocked(self):
        result = validate_evidence_quotes(None, self.document, self.bundle)
        self.assertEqual(result["status"], "SOURCE_UNAVAILABLE")

    def test_missing_pdf_backend_is_unsupported_not_pass(self):
        result = validate_evidence_quotes(
            self.fetch, None, self.bundle, extraction_error="PDF_BACKEND_UNAVAILABLE"
        )
        self.assertEqual(result["status"], "UNSUPPORTED_EXTRACTION")

    def test_mutated_excerpt_fails_closed(self):
        altered = copy.deepcopy(self.bundle)
        altered["evidence"][0]["excerpt"] += " altered"
        result = validate_evidence_quotes(self.fetch, self.document, altered)
        self.assertEqual(result["status"], "MISMATCH")

    def test_mutated_excerpt_hash_fails_closed(self):
        altered = copy.deepcopy(self.bundle)
        altered["evidence"][0]["excerpt_sha256"] = "0" * 64
        result = validate_evidence_quotes(self.fetch, self.document, altered)
        self.assertEqual(result["status"], "MISMATCH")

    def test_mutated_evidence_id_fails_closed(self):
        altered = copy.deepcopy(self.bundle)
        altered["evidence"][0]["evidence_id"] = "EV-" + "0" * 24
        result = validate_evidence_quotes(self.fetch, self.document, altered)
        self.assertEqual(result["status"], "MISMATCH")

    def test_mutated_source_metadata_fails_closed(self):
        altered = copy.deepcopy(self.bundle)
        altered["sources"][0]["revision"] = "invented"
        result = validate_evidence_quotes(self.fetch, self.document, altered)
        self.assertEqual(result["status"], "MISMATCH")

    def test_mutated_raw_bytes_fails_closed(self):
        altered_fetch = FetchResult(self.fetch.metadata, self.raw + b"tamper")
        result = validate_evidence_quotes(altered_fetch, self.document, self.bundle)
        self.assertEqual(result["status"], "MISMATCH")

    def test_mutated_extraction_hash_fails_closed(self):
        altered = copy.copy(self.document)
        object.__setattr__(altered, "text_sha256", "f" * 64)
        result = validate_evidence_quotes(self.fetch, altered, self.bundle)
        self.assertEqual(result["status"], "MISMATCH")

    def test_duplicate_excerpt_occurrence_is_ambiguous(self):
        altered = copy.copy(self.document)
        original = self.document.units
        # The bundle's line fallback uses document.text, so create a structural unit
        # with a repeated phrase and a unique stable locator.
        unit = LegalUnit("Article 1", "ARTICLE", "1", "repeat " * 600)
        object.__setattr__(altered, "units", (unit,))
        bundle = build_evidence_bundle(self.fetch, altered)
        result = validate_evidence_quotes(self.fetch, altered, bundle)
        self.assertEqual(result["status"], "AMBIGUOUS")
        self.assertEqual(result["evidence"][0]["error_code"], "EXCERPT_OCCURRENCE_NOT_UNIQUE")

    def test_duplicate_locator_segments_are_ambiguous(self):
        altered = copy.copy(self.document)
        unit_a = LegalUnit("Article 1", "ARTICLE", "1", "one")
        unit_b = LegalUnit("Article 1", "ARTICLE", "1", "two")
        object.__setattr__(altered, "units", (unit_a, unit_b))
        bundle = build_evidence_bundle(self.fetch, altered)
        result = validate_evidence_quotes(self.fetch, altered, bundle)
        self.assertEqual(result["status"], "AMBIGUOUS")
        self.assertEqual(result["evidence"][0]["error_code"], "SEGMENT_LOCATOR_NOT_UNIQUE")

    def test_claim_unknown_evidence_rejected(self):
        report = {"claims": [{"claim_id": "C1", "evidence_ids": ["EV-unknown"]}]}
        with self.assertRaisesRegex(QuoteValidationError, "CLAIM_EVIDENCE_REFERENCE_INVALID"):
            validate_evidence_quotes(self.fetch, self.document, self.bundle, report)

    def test_duplicate_claim_ids_rejected(self):
        report = {"claims": [
            {"claim_id": "C1", "evidence_ids": [self.bundle["evidence"][0]["evidence_id"]]},
            {"claim_id": "C1", "evidence_ids": [self.bundle["evidence"][0]["evidence_id"]]},
        ]}
        with self.assertRaisesRegex(QuoteValidationError, "DUPLICATE_OR_EMPTY_CLAIM_ID"):
            validate_evidence_quotes(self.fetch, self.document, self.bundle, report)

    def test_review_packet_keeps_status_unverified(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, self.report)
        packet = build_human_review_packet(result, self.bundle, self.report)
        self.assertEqual(packet["legal_status"], "UNVERIFIED")
        self.assertEqual(packet["product_applicability"], "UNVERIFIED")
        self.assertEqual(packet["items"][0]["review"]["reviewer_identifier"], "")
        self.assertIn("untrusted data", packet["items"][0]["source_content_warning"])

    def test_review_packet_rejects_unknown_evidence(self):
        report = {"claims": [{"claim_id": "C1", "evidence_ids": ["EV-unknown"]}]}
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle)
        with self.assertRaisesRegex(QuoteValidationError, "CLAIM_EVIDENCE_REFERENCE_INVALID"):
            build_human_review_packet(result, self.bundle, report)

    def _valid_review(self):
        record = {key: "reviewed" for key in REVIEW_REQUIRED}
        record.update({
            "claim_id": "C1", "quote_exactness": "PASS", "locator_match": "PASS",
            "context_and_exception_check": "PASS", "claim_support": "SUPPORTED",
            "countercheck": "COMPLETED", "review_decision": "ACCEPT_AS_CANDIDATE",
            "countercheck_target": "The exact claim wording and its legal scope are checked.",
            "counter_evidence_examined": "Adjacent paragraphs, exceptions and referenced definitions were examined.",
            "countercheck_conclusion": "No contrary provision was found in the examined source context."
            "reviewer_role": "Independent technical/legal reviewer",
            "reviewer_identifier": "reviewer-1",
            "reviewed_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "protocol_version": "VERIFICATION_PROTOCOL_V1",
            "rationale": "Exact excerpt and locator checked against official source.",
        })
        return record

    def test_complete_human_record_valid_but_does_not_promote(self):
        result = validate_human_review_record(self._valid_review())
        self.assertTrue(result["valid"])
        self.assertEqual(result["legal_status"], "UNVERIFIED")
        self.assertEqual(result["product_applicability"], "UNVERIFIED")

    def test_missing_human_field_rejected(self):
        record = self._valid_review()
        del record["countercheck_target"]
        with self.assertRaisesRegex(QuoteValidationError, "REVIEW_FIELDS_INVALID"):
            validate_human_review_record(record)

    def test_incomplete_countercheck_cannot_accept(self):
        record = self._valid_review()
        record["countercheck"] = "NOT_COMPLETED"
        with self.assertRaisesRegex(QuoteValidationError, "COUNTERCHECK_REQUIRED"):
            validate_human_review_record(record)

    def test_failed_quote_cannot_accept(self):
        record = self._valid_review()
        record["quote_exactness"] = "FAIL"
        with self.assertRaisesRegex(QuoteValidationError, "QUOTE_PASS_REQUIRED"):
            validate_human_review_record(record)

    def test_missing_rationale_rejected(self):
        record = self._valid_review()
        record["rationale"] = " "
        with self.assertRaisesRegex(QuoteValidationError, "REVIEW_FIELD_MISSING"):
            validate_human_review_record(record)

    def test_review_timestamp_requires_timezone(self):
        record = self._valid_review()
        record["reviewed_at_utc"] = "2026-11-13T00:00:00"
        with self.assertRaisesRegex(QuoteValidationError, "REVIEW_TIMESTAMP_INVALID"):
            validate_human_review_record(record)

    def test_review_timestamp_must_be_utc_not_local_offset(self):
        record = self._valid_review()
        record["reviewed_at_utc"] = "2026-11-13T09:00:00+09:00"
        with self.assertRaisesRegex(QuoteValidationError, "REVIEW_TIMESTAMP_INVALID"):
            validate_human_review_record(record)

    def test_review_packet_rejects_duplicate_claim_ids(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle)
        duplicate = {"claims": self.report["claims"] * 2}
        with self.assertRaisesRegex(QuoteValidationError, "CLAIM_EVIDENCE_REFERENCE_INVALID"):
            build_human_review_packet(result, self.bundle, duplicate)

    def test_review_packet_rejects_validation_result_from_other_bundle(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, self.report)
        result["bundle_sha256"] = "0" * 64
        with self.assertRaisesRegex(QuoteValidationError, "VALIDATION_BUNDLE_HASH_MISMATCH"):
            build_human_review_packet(result, self.bundle, self.report)

    def test_review_packet_rejects_incomplete_evidence_inventory(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, self.report)
        result["evidence"] = []
        with self.assertRaisesRegex(QuoteValidationError, "VALIDATION_EVIDENCE_ID_SET_MISMATCH"):
            build_human_review_packet(result, self.bundle, self.report)

    def test_claim_level_status_blocks_non_exact_evidence(self):
        result = validate_evidence_quotes(self.fetch, self.document, self.bundle, self.report)
        result["evidence"][0]["status"] = "MISMATCH"
        result["status"] = "MISMATCH"
        packet = build_human_review_packet(result, self.bundle, self.report)
        self.assertEqual(packet["claim_evidence_status"]["C-001"]["status"], "BLOCKED")
        self.assertFalse(packet["items"][0]["claim_support_eligible"])

    def test_generic_countercheck_text_rejected(self):
        record = self._valid_review()
        record["counter_evidence_examined"] = "reviewed"
        with self.assertRaisesRegex(QuoteValidationError, "COUNTERCHECK_DETAIL_INSUFFICIENT"):
            validate_human_review_record(record)

    def test_future_review_timestamp_rejected(self):
        record = self._valid_review()
        record["reviewed_at_utc"] = (
            datetime.now(timezone.utc).replace(microsecond=0)
            + __import__("datetime").timedelta(hours=1)
        ).isoformat().replace("+00:00", "Z")
        with self.assertRaisesRegex(QuoteValidationError, "REVIEW_TIMESTAMP_INVALID"):
            validate_human_review_record(record)

    def test_chunked_excerpt_locator_rebuilds(self):
        altered = copy.copy(self.document)
        unit = LegalUnit("Article 2", "ARTICLE", "2", "A" * 2000 + "B" * 2000 + "C" * 500)
        object.__setattr__(altered, "units", (unit,))
        bundle = build_evidence_bundle(self.fetch, altered)
        result = validate_evidence_quotes(self.fetch, altered, bundle)
        self.assertEqual(result["status"], "EXACT_MATCH")
        self.assertEqual(len(result["evidence"]), 3)


if __name__ == "__main__":
    unittest.main()
