import hashlib
import unittest
from datetime import datetime, timezone

from source_bundle import EvidenceBundleError, build_source_evidence_bundle
from source_evidence import FetchMetadata, FetchResult, SOURCE_REGISTRY
from source_extraction import extract_eurlex_html


class SourceBundleTests(unittest.TestCase):
    def make_pair(self, html):
        source = SOURCE_REGISTRY["ST_AN5156_REV14"]
        raw = html.encode("utf-8")
        metadata = FetchMetadata(
            source_id=source.source_id,
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
            sha256=hashlib.sha256(raw).hexdigest(),
            extraction_method="NONE_PHASE_A_RAW_BYTES_ONLY",
            status="FETCHED",
        )
        fetched = FetchResult(metadata, raw)
        extracted = extract_eurlex_html(source.source_id, raw)
        return fetched, extracted

    def test_bundle_links_hashes_identity_revision_and_excerpt(self):
        fetched, extracted = self.make_pair(
            "<html><head><title>AN5156 Rev 14</title></head><body>"
            "<h1>AN5156</h1><p>Rev 14 (June 2026)</p>"
            "<h2>Article 13</h2><p>Security lifecycle requirements.</p></body></html>"
        )
        bundle = build_source_evidence_bundle(fetched, extracted)
        self.assertEqual(bundle.identity_status, "IDENTITY_AND_REVISION_MATCHED")
        self.assertEqual(bundle.raw_sha256, fetched.metadata.sha256)
        self.assertEqual(bundle.extracted_text_sha256, extracted.text_sha256)
        self.assertTrue(bundle.evidence)
        item = bundle.evidence[0]
        self.assertEqual(item.excerpt_sha256, hashlib.sha256(item.excerpt.encode()).hexdigest())
        self.assertLessEqual(len(item.excerpt), 500)

    def test_missing_identity_is_not_promoted_to_verified(self):
        fetched, extracted = self.make_pair("<html><body><p>Generic content.</p></body></html>")
        bundle = build_source_evidence_bundle(fetched, extracted)
        self.assertEqual(bundle.identity_status, "IDENTITY_UNCONFIRMED")

    def test_revision_mismatch_is_explicit(self):
        fetched, extracted = self.make_pair(
            "<html><head><title>AN5156 Rev 13</title></head><body>AN5156 Rev 13</body></html>"
        )
        bundle = build_source_evidence_bundle(fetched, extracted)
        self.assertEqual(bundle.identity_status, "REVISION_MISMATCH")

    def test_raw_hash_mismatch_blocks_bundle(self):
        fetched, extracted = self.make_pair("<html><body>AN5156 Rev 14<h2>Article 13</h2><p>Article text.</p></body></html>")
        object.__setattr__(fetched.metadata, "sha256", "0" * 64)
        with self.assertRaisesRegex(EvidenceBundleError, "FETCH_RAW_HASH_MISMATCH"):
            build_source_evidence_bundle(fetched, extracted)

    def test_source_mismatch_blocks_bundle(self):
        fetched, extracted = self.make_pair("<html><body>AN5156 Rev 14</body></html>")
        object.__setattr__(extracted, "source_id", "ST_AN4992_REV19")
        with self.assertRaisesRegex(EvidenceBundleError, "SOURCE_ID_MISMATCH"):
            build_source_evidence_bundle(fetched, extracted)

    def test_excerpt_limits_are_enforced(self):
        fetched, extracted = self.make_pair("<html><body>AN5156 Rev 14</body></html>")
        with self.assertRaisesRegex(EvidenceBundleError, "INVALID_EVIDENCE_LIMIT"):
            build_source_evidence_bundle(fetched, extracted, max_excerpt_chars=0)


if __name__ == "__main__":
    unittest.main()
