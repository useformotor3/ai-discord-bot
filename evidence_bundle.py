"""Phase C: in-memory, provenance-bound evidence bundle builder.

The module never fetches URLs or writes files. It joins Phase A fetch results
with Phase B extraction results and exposes bounded, hash-addressed excerpts.
"""
from __future__ import annotations

from hashlib import sha256
import re
from typing import Any
from urllib.parse import urlsplit

from source_evidence import SOURCE_REGISTRY

BUNDLE_SCHEMA_VERSION = "cra-evidence-bundle-v1"
DEFAULT_MAX_EXCERPT_CHARS = 2000
DEFAULT_MAX_EVIDENCE_UNITS = 200
DEFAULT_MAX_TOTAL_EXCERPT_CHARS = 100_000


class EvidenceBundleError(ValueError):
    """A source/extraction pair cannot be represented as trusted provenance."""


def _digest(value: bytes) -> str:
    return sha256(value).hexdigest()


def _evidence_id(source_id: str, raw_hash: str, extractor_version: str,
                 locator: str, excerpt_hash: str, part: int) -> str:
    material = "\n".join((source_id, raw_hash, extractor_version, locator,
                         excerpt_hash, str(part))).encode("utf-8")
    return "EV-" + _digest(material)[:24]


def _split_exact(text: str, limit: int) -> list[str]:
    if not text:
        return []
    return [text[index:index + limit] for index in range(0, len(text), limit)]


def _source_segments(document: Any) -> list[tuple[str, str, str]]:
    segments: list[tuple[str, str, str]] = []
    units = tuple(getattr(document, "units", ()) or ())
    pages = tuple(getattr(document, "pages", ()) or ())
    if units:
        for unit in units:
            segments.append((str(unit.locator), str(unit.unit_type), str(unit.text)))
    elif pages:
        for page in pages:
            segments.append((f"PDF page {int(page.page_number)}", "PDF_PAGE",
                             str(page.text)))
    else:
        # HTML without structural locators is split into line-based candidates.
        for line_number, line in enumerate(str(getattr(document, "text", "")).splitlines(), 1):
            if line:
                segments.append((f"Text line {line_number}", "TEXT_LINE", line))
    return segments


def build_evidence_bundle(fetch_result: Any, extracted_document: Any, *,
                          max_excerpt_chars: int = DEFAULT_MAX_EXCERPT_CHARS,
                          max_evidence_units: int = DEFAULT_MAX_EVIDENCE_UNITS,
                          max_total_excerpt_chars: int = DEFAULT_MAX_TOTAL_EXCERPT_CHARS
                          ) -> dict[str, Any]:
    """Build a bounded bundle from matching Phase A and Phase B results.

    Raw bytes and full extracted document text are not copied into the bundle.
    Excerpts are exact contiguous substrings of extracted text/units.
    """
    if (min(max_excerpt_chars, max_evidence_units, max_total_excerpt_chars) <= 0
            or max_excerpt_chars > DEFAULT_MAX_EXCERPT_CHARS
            or max_evidence_units > DEFAULT_MAX_EVIDENCE_UNITS
            or max_total_excerpt_chars > DEFAULT_MAX_TOTAL_EXCERPT_CHARS):
        raise EvidenceBundleError("INVALID_BUNDLE_LIMIT")
    try:
        metadata = fetch_result.metadata.to_dict()
        raw = bytes(fetch_result.content)
        source_id = str(metadata["source_id"])
        source = SOURCE_REGISTRY[source_id]
        extracted_source_id = str(extracted_document.source_id)
        raw_hash = str(metadata["sha256"])
        extracted_raw_hash = str(extracted_document.raw_sha256)
        extractor_version = str(extracted_document.extractor_version)
        text = str(extracted_document.text)
        text_hash = str(extracted_document.text_sha256)
    except Exception as exc:
        raise EvidenceBundleError("INVALID_FETCH_OR_EXTRACTION_INPUT") from exc

    if extracted_source_id != source_id:
        raise EvidenceBundleError("SOURCE_ID_MISMATCH")
    if metadata.get("status") != "FETCHED" or metadata.get("http_status") != 200:
        raise EvidenceBundleError("SOURCE_NOT_SUCCESSFULLY_FETCHED")
    if metadata.get("canonical_url") != source.canonical_url:
        raise EvidenceBundleError("CANONICAL_URL_MISMATCH")
    if (metadata.get("publisher") != source.publisher
            or metadata.get("title") != source.title
            or metadata.get("document_identifier") != source.document_identifier
            or metadata.get("revision") != source.revision):
        raise EvidenceBundleError("SOURCE_REGISTRY_METADATA_MISMATCH")
    final_url = str(metadata.get("final_url", ""))
    if urlsplit(final_url).scheme != "https" or urlsplit(final_url).hostname != urlsplit(source.canonical_url).hostname:
        raise EvidenceBundleError("FINAL_URL_HOST_MISMATCH")
    if metadata.get("byte_count") != len(raw) or raw_hash != _digest(raw):
        raise EvidenceBundleError("FETCHED_BYTES_HASH_MISMATCH")
    if extracted_raw_hash != raw_hash:
        raise EvidenceBundleError("EXTRACTION_RAW_HASH_MISMATCH")
    if text_hash != _digest(text.encode("utf-8")):
        raise EvidenceBundleError("EXTRACTED_TEXT_HASH_MISMATCH")
    if not extractor_version or not text:
        raise EvidenceBundleError("EMPTY_EXTRACTION")

    source_record = {
        "source_id": source_id,
        "canonical_url": metadata["canonical_url"],
        "final_url": final_url,
        "publisher": metadata["publisher"],
        "title": metadata["title"],
        "document_identifier": metadata["document_identifier"],
        "revision": metadata["revision"],
        "published_or_revision_date": metadata["published_or_revision_date"],
        "fetched_at_utc": metadata["fetched_at_utc"],
        "http_status": metadata["http_status"],
        "mime_type": metadata["mime_type"],
        "byte_count": metadata["byte_count"],
        "raw_sha256": raw_hash,
        "extraction_method": extracted_document.extraction_method,
        "extractor_version": extractor_version,
        "extracted_text_sha256": text_hash,
        "locator_status": extracted_document.locator_status,
    }

    evidence: list[dict[str, str]] = []
    total_chars = 0
    for locator, unit_type, segment_text in _source_segments(extracted_document):
        if not segment_text:
            continue
        parts = _split_exact(segment_text, max_excerpt_chars)
        if not parts:
            continue
        for part_index, excerpt in enumerate(parts, 1):
            if len(evidence) >= max_evidence_units:
                raise EvidenceBundleError("EVIDENCE_UNIT_LIMIT_EXCEEDED")
            total_chars += len(excerpt)
            if total_chars > max_total_excerpt_chars:
                raise EvidenceBundleError("TOTAL_EXCERPT_LIMIT_EXCEEDED")
            total_excerpt_chars += len(excerpt)
        if total_excerpt_chars > DEFAULT_MAX_TOTAL_EXCERPT_CHARS:
            raise EvidenceBundleError("BUNDLE_TOTAL_EXCERPT_LIMIT_EXCEEDED")
        excerpt_hash = _digest(excerpt.encode("utf-8"))
            part_locator = locator if len(parts) == 1 else f"{locator} [segment {part_index}/{len(parts)}]"
            evidence.append({
                "evidence_id": _evidence_id(source_id, raw_hash, extractor_version,
                                            part_locator, excerpt_hash, part_index),
                "source_id": source_id,
                "locator": part_locator,
                "unit_type": unit_type,
                "excerpt": excerpt,
                "excerpt_sha256": excerpt_hash,
            })
    if not evidence:
        raise EvidenceBundleError("NO_EVIDENCE_SEGMENTS")

    bundle = {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "sources": [source_record],
        "evidence": evidence,
    }
    validate_evidence_bundle(bundle)
    return bundle


def validate_evidence_bundle(bundle: Any) -> dict[str, Any]:
    """Validate bundle structure, registry provenance, hashes and deterministic IDs."""
    if not isinstance(bundle, dict) or set(bundle) != {"schema_version", "sources", "evidence"}:
        raise EvidenceBundleError("BUNDLE_FIELDS_INVALID")
    if bundle["schema_version"] != BUNDLE_SCHEMA_VERSION:
        raise EvidenceBundleError("BUNDLE_SCHEMA_VERSION_INVALID")
    sources = bundle["sources"]
    evidence = bundle["evidence"]
    if not isinstance(sources, list) or not sources or not isinstance(evidence, list) or not evidence:
        raise EvidenceBundleError("BUNDLE_CONTENT_EMPTY")
    source_map: dict[str, dict[str, Any]] = {}
    source_fields = {
        "source_id", "canonical_url", "final_url", "publisher", "title",
        "document_identifier", "revision", "published_or_revision_date",
        "fetched_at_utc", "http_status", "mime_type", "byte_count",
        "raw_sha256", "extraction_method", "extractor_version",
        "extracted_text_sha256", "locator_status",
    }
    for source in sources:
        if not isinstance(source, dict) or set(source) != source_fields:
            raise EvidenceBundleError("BUNDLE_SOURCE_FIELDS_INVALID")
        source_id = source["source_id"]
        registered = SOURCE_REGISTRY.get(source_id)
        if registered is None or source_id in source_map:
            raise EvidenceBundleError("BUNDLE_SOURCE_ID_INVALID")
        if (source["canonical_url"] != registered.canonical_url
                or source["publisher"] != registered.publisher
                or source["title"] != registered.title
                or source["document_identifier"] != registered.document_identifier
                or source["revision"] != registered.revision):
            raise EvidenceBundleError("BUNDLE_SOURCE_REGISTRY_MISMATCH")
        if source["http_status"] != 200 or source["byte_count"] <= 0:
            raise EvidenceBundleError("BUNDLE_SOURCE_FETCH_METADATA_INVALID")
        for hash_field in ("raw_sha256", "extracted_text_sha256"):
            value = source[hash_field]
            if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
                raise EvidenceBundleError("BUNDLE_HASH_FORMAT_INVALID")
        source_map[source_id] = source

    if len(evidence) > DEFAULT_MAX_EVIDENCE_UNITS:
        raise EvidenceBundleError("BUNDLE_EVIDENCE_UNIT_LIMIT_EXCEEDED")
    seen: set[str] = set()
    total_excerpt_chars = 0
    for item in evidence:
        fields = {"evidence_id", "source_id", "locator", "unit_type", "excerpt", "excerpt_sha256"}
        if not isinstance(item, dict) or set(item) != fields:
            raise EvidenceBundleError("BUNDLE_EVIDENCE_FIELDS_INVALID")
        source_id = item["source_id"]
        source = source_map.get(source_id)
        if source is None:
            raise EvidenceBundleError("BUNDLE_EVIDENCE_SOURCE_UNKNOWN")
        excerpt = item["excerpt"]
        if not isinstance(excerpt, str) or not excerpt or len(excerpt) > DEFAULT_MAX_EXCERPT_CHARS:
            raise EvidenceBundleError("BUNDLE_EXCERPT_INVALID")
        excerpt_hash = _digest(excerpt.encode("utf-8"))
        if item["excerpt_sha256"] != excerpt_hash:
            raise EvidenceBundleError("BUNDLE_EXCERPT_HASH_MISMATCH")
        evidence_id = _evidence_id(source_id, source["raw_sha256"],
                                   source["extractor_version"], item["locator"],
                                   excerpt_hash, _segment_number(item["locator"]))
        if item["evidence_id"] != evidence_id:
            raise EvidenceBundleError("BUNDLE_EVIDENCE_ID_MISMATCH")
        if evidence_id in seen:
            raise EvidenceBundleError("BUNDLE_EVIDENCE_ID_DUPLICATED")
        seen.add(evidence_id)
    return bundle


def _segment_number(locator: str) -> int:
    match = re.search(r"\[segment (\d+)/\d+\]$", locator)
    return int(match.group(1)) if match else 1
