import copy
import hashlib
import unittest
from datetime import datetime, timezone

from evidence_bundle import (
    EvidenceBundleError,
    build_evidence_bundle,
    validate_evidence_bundle,
)
from source_evidence import FetchMetadata, FetchResult, SOURCE_REGISTRY
from source_extraction import extract_html_document


class EvidenceBundleTests(unittest.TestCase):
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
                http_status=200,
                mime_type="text/html",
                byte_count=len(self.raw),
                sha256=hashlib.sha256(self.raw).hexdigest(),
                extraction_method="NONE_PHASE_A_RAW_BYTES_ONLY",
                status="FETCHED",
            ),
            content=self.raw,
        )
        self.document = extract_html_document(self.source_id, self.raw)

    def test_builds_bundle_with_hashes_and_deterministic_ids(self):
        first = build_evidence_bundle(self.fetch, self.document)
        second = build_evidence_bundle(self.fetch, self.document)
        self.assertEqual(first, second)
        self.assertEqual(first["schema_version"], "cra-evidence-bundle-v1")
        self.assertEqual(first["sources"][0]["raw_sha256"], hashlib.sha256(self.raw).hexdigest())
        self.assertTrue(first["evidence"][0]["evidence_id"].startswith("EV-"))
        self.assertEqual(validate_evidence_bundle(first), first)

    def test_source_id_mismatch_rejected(self):
        other = extract_html_document("ST_AN4992_REV19", self.raw)
        with self.assertRaisesRegex(EvidenceBundleError, "SOURCE_ID_MISMATCH"):
            build_evidence_bundle(self.fetch, other)

    def test_fetch_bytes_tampering_rejected(self):
        tampered = FetchResult(self.fetch.metadata, self.raw + b"tamper")
        with self.assertRaisesRegex(EvidenceBundleError, "FETCHED_BYTES_HASH_MISMATCH"):
            build_evidence_bundle(tampered, self.document)

    def test_extraction_raw_hash_mismatch_rejected(self):
        altered = copy.copy(self.document)
        object.__setattr__(altered, "raw_sha256", "0" * 64)
        with self.assertRaisesRegex(EvidenceBundleError, "EXTRACTION_RAW_HASH_MISMATCH"):
            build_evidence_bundle(self.fetch, altered)

    def test_extracted_text_hash_mismatch_rejected(self):
        altered = copy.copy(self.document)
        object.__setattr__(altered, "text_sha256", "0" * 64)
        with self.assertRaisesRegex(EvidenceBundleError, "EXTRACTED_TEXT_HASH_MISMATCH"):
            build_evidence_bundle(self.fetch, altered)

    def test_unregistered_or_mismatched_registry_metadata_rejected(self):
        metadata = self.fetch.metadata
        altered_metadata = copy.copy(metadata)
        object.__setattr__(altered_metadata, "publisher", "Model invented publisher")
        altered = FetchResult(altered_metadata, self.raw)
        with self.assertRaisesRegex(EvidenceBundleError, "SOURCE_REGISTRY_METADATA_MISMATCH"):
            build_evidence_bundle(altered, self.document)

    def test_failed_fetch_metadata_rejected(self):
        metadata = copy.copy(self.fetch.metadata)
        object.__setattr__(metadata, "status", "FAILED")
        altered = FetchResult(metadata, self.raw)
        with self.assertRaisesRegex(EvidenceBundleError, "SOURCE_NOT_SUCCESSFULLY_FETCHED"):
            build_evidence_bundle(altered, self.document)

    def test_excerpt_mutation_rejected(self):
        bundle = build_evidence_bundle(self.fetch, self.document)
        bundle["evidence"][0]["excerpt"] += " changed"
        with self.assertRaisesRegex(EvidenceBundleError, "BUNDLE_EXCERPT_HASH_MISMATCH"):
            validate_evidence_bundle(bundle)

    def test_evidence_id_mutation_rejected(self):
        bundle = build_evidence_bundle(self.fetch, self.document)
        bundle["evidence"][0]["evidence_id"] = "EV-" + "0" * 24
        with self.assertRaisesRegex(EvidenceBundleError, "BUNDLE_EVIDENCE_ID_MISMATCH"):
            validate_evidence_bundle(bundle)

    def test_excerpt_and_unit_limits_fail_closed(self):
        with self.assertRaisesRegex(EvidenceBundleError, "EVIDENCE_UNIT_LIMIT_EXCEEDED"):
            build_evidence_bundle(self.fetch, self.document, max_evidence_units=1)
        with self.assertRaisesRegex(EvidenceBundleError, "TOTAL_EXCERPT_LIMIT_EXCEEDED"):
            build_evidence_bundle(self.fetch, self.document, max_total_excerpt_chars=1)


if __name__ == "__main__":
    unittest.main()
