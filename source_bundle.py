"""Deterministic, bounded evidence bundles joining fetch, extraction and locators.

Bundles contain hashes and short cited excerpts only; never persist full source bytes
or complete extracted manufacturer documents in this module.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import re
from typing import Iterable

from source_evidence import FetchResult, SOURCE_REGISTRY
from source_extraction import ExtractedDocument, LegalUnit

BUNDLE_SCHEMA_VERSION = "1.0.0"
DEFAULT_MAX_EXCERPT_CHARS = 500
DEFAULT_MAX_EVIDENCE_ITEMS = 100


class EvidenceBundleError(ValueError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class EvidenceExcerpt:
    evidence_id: str
    locator: str
    excerpt: str
    excerpt_sha256: str


@dataclass(frozen=True)
class SourceEvidenceBundle:
    schema_version: str
    source_id: str
    canonical_url: str
    final_url: str
    publisher: str
    title: str
    expected_document_identifier: str
    observed_document_identifier: str
    expected_revision: str
    observed_revision: str
    identity_status: str
    fetched_at_utc: str
    http_status: int
    mime_type: str
    byte_count: int
    raw_sha256: str
    extracted_text_sha256: str
    extraction_method: str
    extractor_version: str
    decode_charset: str
    replacement_char_count: int
    extraction_quality_status: str
    page_count: int
    empty_page_count: int
    locator_status: str
    evidence: tuple[EvidenceExcerpt, ...]

    def to_dict(self) -> dict[str, object]:
        result = asdict(self)
        result["evidence"] = [asdict(item) for item in self.evidence]
        return result


def _observed_identity(source_id: str, text: str, title: str) -> tuple[str, str]:
    definition = SOURCE_REGISTRY[source_id]
    combined = title + "\n" + text
    identifier = definition.document_identifier
    token = identifier.split(":", 1)[-1]
    observed_id = token if re.search(re.escape(token), combined, re.I) else ""
    # Revision extraction is deliberately conservative; no revision is inferred
    # from a URL, HTTP Last-Modified header, registry value or model-generated text.
    match = re.search(r"\bRev(?:ision)?\.?\s*((?:[A-Z]?\d+(?:\.\d+)?|[A-Z]))\b", combined, re.I)
    observed_revision = ""
    if match:
        observed_revision = "Rev " + match.group(1)
    return observed_id, observed_revision


def _revision_matches(expected: str, observed: str) -> bool:
    if not expected or not observed:
        return False
    expected_match = re.search(r"\bRev(?:ision)?\.?\s*((?:[A-Z]?\d+(?:\.\d+)?|[A-Z]))\b", expected, re.I)
    observed_match = re.search(r"\bRev(?:ision)?\.?\s*((?:[A-Z]?\d+(?:\.\d+)?|[A-Z]))\b", observed, re.I)
    return bool(expected_match and observed_match and expected_match.group(1).upper() == observed_match.group(1).upper())


def build_source_evidence_bundle(
    fetched: FetchResult,
    extracted: ExtractedDocument,
    *,
    max_excerpt_chars: int = DEFAULT_MAX_EXCERPT_CHARS,
    max_evidence_items: int = DEFAULT_MAX_EVIDENCE_ITEMS,
) -> SourceEvidenceBundle:
    metadata = fetched.metadata
    if metadata.source_id not in SOURCE_REGISTRY:
        raise EvidenceBundleError("UNKNOWN_SOURCE_ID")
    if extracted.source_id != metadata.source_id:
        raise EvidenceBundleError("SOURCE_ID_MISMATCH")
    if sha256(fetched.content).hexdigest() != metadata.sha256:
        raise EvidenceBundleError("FETCH_RAW_HASH_MISMATCH")
    if sha256(fetched.content).hexdigest() != extracted.raw_sha256:
        raise EvidenceBundleError("EXTRACTION_RAW_HASH_MISMATCH")
    if not extracted.text_sha256 or sha256(extracted.text.encode("utf-8")).hexdigest() != extracted.text_sha256:
        raise EvidenceBundleError("EXTRACTION_TEXT_HASH_MISMATCH")
    if max_excerpt_chars < 1 or max_evidence_items < 1:
        raise EvidenceBundleError("INVALID_EVIDENCE_LIMIT")

    observed_id, observed_revision = _observed_identity(metadata.source_id, extracted.text, extracted.title)
    expected_id = metadata.document_identifier.split(":", 1)[-1]
    id_match = bool(observed_id and observed_id.casefold() == expected_id.casefold())
    revision_match = _revision_matches(metadata.revision, observed_revision)
    if observed_id and not id_match:
        identity_status = "IDENTITY_MISMATCH"
    elif observed_revision and not revision_match:
        identity_status = "REVISION_MISMATCH"
    elif id_match and revision_match:
        identity_status = "IDENTITY_AND_REVISION_MATCHED"
    else:
        identity_status = "IDENTITY_UNCONFIRMED"

    evidence: list[EvidenceExcerpt] = []
    seen: set[tuple[str, str]] = set()
    for unit in extracted.units:
        excerpt = " ".join(unit.text.split())
        if not excerpt or len(excerpt) > max_excerpt_chars:
            continue
        key = (unit.locator, excerpt)
        if key in seen:
            continue
        seen.add(key)
        excerpt_hash = sha256(excerpt.encode("utf-8")).hexdigest()
        evidence_id = sha256(
            (metadata.source_id + "\n" + unit.locator + "\n" + excerpt_hash).encode("utf-8")
        ).hexdigest()[:24]
        evidence.append(EvidenceExcerpt(evidence_id, unit.locator, excerpt, excerpt_hash))
        if len(evidence) >= max_evidence_items:
            break

    return SourceEvidenceBundle(
        schema_version=BUNDLE_SCHEMA_VERSION,
        source_id=metadata.source_id,
        canonical_url=metadata.canonical_url,
        final_url=metadata.final_url,
        publisher=metadata.publisher,
        title=metadata.title,
        expected_document_identifier=metadata.document_identifier,
        observed_document_identifier=observed_id,
        expected_revision=metadata.revision,
        observed_revision=observed_revision,
        identity_status=identity_status,
        fetched_at_utc=metadata.fetched_at_utc,
        http_status=metadata.http_status,
        mime_type=metadata.mime_type,
        byte_count=metadata.byte_count,
        raw_sha256=metadata.sha256,
        extracted_text_sha256=extracted.text_sha256,
        extraction_method=extracted.extraction_method,
        extractor_version=extracted.extractor_version,
        decode_charset=extracted.decode_charset,
        replacement_char_count=extracted.replacement_char_count,
        extraction_quality_status=extracted.quality_status,
        page_count=extracted.page_count,
        empty_page_count=extracted.empty_page_count,
        locator_status=extracted.locator_status,
        evidence=tuple(evidence),
    )
