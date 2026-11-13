"""Phase D: deterministic quote integrity checks and human-review packets.

This module is deliberately offline and side-effect free. EXACT_MATCH means
exact correspondence to Phase B normalized extraction output only; it is not
proof of publisher authenticity, visual PDF fidelity, legal meaning, or claim support.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from typing import Any, Mapping

from evidence_bundle import (
    EvidenceBundleError,
    build_evidence_bundle,
    validate_evidence_bundle,
)
from source_extraction import ExtractionError

MACHINE_STATUSES = frozenset({
    "EXACT_MATCH", "MISMATCH", "AMBIGUOUS",
    "UNSUPPORTED_EXTRACTION", "SOURCE_UNAVAILABLE",
})
LOCATOR_CLASSES = frozenset({
    "XML_STRUCTURAL_CANDIDATE", "HTML_TEXT_CANDIDATE",
    "PDF_PAGE_ONLY", "TEXT_LINE_ONLY", "LOCATOR_UNAVAILABLE",
})
REVIEW_ENUMS = {
    "quote_exactness": {"PASS", "FAIL", "BLOCKED"},
    "locator_match": {"PASS", "FAIL", "BLOCKED"},
    "context_and_exception_check": {"PASS", "FAIL", "BLOCKED"},
    "claim_support": {"SUPPORTED", "NOT_SUPPORTED", "UNCLEAR"},
    "countercheck": {"COMPLETED", "NOT_COMPLETED"},
    "review_decision": {"ACCEPT_AS_CANDIDATE", "REVISE", "REJECT"},
}
REVIEW_REQUIRED = frozenset({
    "claim_id", "quote_exactness", "locator_match",
    "context_and_exception_check", "claim_support", "countercheck",
    "counter_evidence", "review_decision", "reviewer_role",
    "reviewer_identifier", "reviewed_at_utc", "protocol_version", "rationale",
})


class QuoteValidationError(ValueError):
    """A quote validation input or review record is invalid."""

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def _digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def _locator_class(document: Any, unit_type: str, locator: str) -> str:
    method = str(getattr(document, "extraction_method", ""))
    if method == "EURLEX_XML_STRUCTURED_V1":
        return "XML_STRUCTURAL_CANDIDATE"
    if method == "EURLEX_HTML_CANDIDATE_V1":
        return "HTML_TEXT_CANDIDATE"
    if method == "PDF_PAGE_TEXT_V1" or unit_type == "PDF_PAGE":
        return "PDF_PAGE_ONLY"
    if unit_type == "TEXT_LINE" or locator.startswith("Text line "):
        return "TEXT_LINE_ONLY"
    return "LOCATOR_UNAVAILABLE"


def _segments(document: Any) -> list[tuple[str, str, str]]:
    units = tuple(getattr(document, "units", ()) or ())
    pages = tuple(getattr(document, "pages", ()) or ())
    if units:
        return [(str(u.locator), str(u.unit_type), str(u.text)) for u in units]
    if pages:
        return [(f"PDF page {int(p.page_number)}", "PDF_PAGE", str(p.text)) for p in pages]
    return [
        (f"Text line {n}", "TEXT_LINE", line)
        for n, line in enumerate(str(getattr(document, "text", "")).splitlines(), 1)
        if line
    ]


def validate_evidence_quotes(
    fetch_result: Any,
    extracted_document: Any,
    bundle: Any,
    report_payload: Mapping[str, Any] | None = None,
    *,
    context_chars: int = 500,
) -> dict[str, Any]:
    """Rebuild and compare the canonical bundle; return machine-only results.

    No input is repaired or normalized. Missing original bytes or extraction is
    BLOCKED. Duplicate excerpt positions within a segment are AMBIGUOUS.
    """
    if not isinstance(context_chars, int) or isinstance(context_chars, bool) or not 0 <= context_chars <= 500:
        raise QuoteValidationError("INVALID_CONTEXT_LIMIT")
    if fetch_result is None or extracted_document is None:
        return {
            "status": "SOURCE_UNAVAILABLE", "error_code": "SOURCE_OR_EXTRACTION_UNAVAILABLE",
            "evidence": [], "claim_evidence": {},
            "limitations": ["Original fetch bytes and extraction result are required."],
        }
    try:
        validate_evidence_bundle(bundle)
        rebuilt = build_evidence_bundle(fetch_result, extracted_document)
    except (EvidenceBundleError, ExtractionError, KeyError, TypeError, ValueError) as exc:
        code = getattr(exc, "code", None) or (str(exc) if str(exc) else "REBUILD_FAILED")
        return {
            "status": "MISMATCH", "error_code": code,
            "evidence": [], "claim_evidence": {},
            "limitations": ["Bundle reconstruction failed closed; no evidence was accepted."],
        }

    supplied_by_id = {item["evidence_id"]: item for item in bundle["evidence"]}
    rebuilt_by_id = {item["evidence_id"]: item for item in rebuilt["evidence"]}
    if supplied_by_id.keys() != rebuilt_by_id.keys():
        return {
            "status": "MISMATCH", "error_code": "EVIDENCE_ID_SET_MISMATCH",
            "evidence": [], "claim_evidence": {},
            "limitations": ["Supplied and rebuilt Evidence ID sets differ."],
        }

    segment_index: dict[tuple[str, str], list[str]] = {}
    for locator, unit_type, text in _segments(extracted_document):
        segment_index.setdefault((locator, unit_type), []).append(text)

    results = []
    for evidence_id, canonical in rebuilt_by_id.items():
        supplied = supplied_by_id[evidence_id]
        fields = ("source_id", "locator", "unit_type", "excerpt", "excerpt_sha256")
        if any(supplied.get(k) != canonical.get(k) for k in fields):
            results.append({
                "evidence_id": evidence_id, "status": "MISMATCH",
                "error_code": "EVIDENCE_CONTENT_MISMATCH",
                "locator_class": "LOCATOR_UNAVAILABLE",
            })
            continue
        candidates = segment_index.get((canonical["locator"], canonical["unit_type"]), [])
        if len(candidates) != 1:
            results.append({
                "evidence_id": evidence_id, "status": "AMBIGUOUS",
                "error_code": "SEGMENT_LOCATOR_NOT_UNIQUE",
                "locator_class": _locator_class(extracted_document, canonical["unit_type"], canonical["locator"]),
            })
            continue
        segment = candidates[0]
        excerpt = canonical["excerpt"]
        first = segment.find(excerpt)
        occurrences = segment.count(excerpt)
        if first < 0:
            results.append({
                "evidence_id": evidence_id, "status": "MISMATCH",
                "error_code": "EXCERPT_NOT_FOUND_IN_SEGMENT",
                "locator_class": _locator_class(extracted_document, canonical["unit_type"], canonical["locator"]),
            })
            continue
        if occurrences != 1:
            results.append({
                "evidence_id": evidence_id, "status": "AMBIGUOUS",
                "error_code": "EXCERPT_OCCURRENCE_NOT_UNIQUE",
                "locator_class": _locator_class(extracted_document, canonical["unit_type"], canonical["locator"]),
            })
            continue
        start, end = first, first + len(excerpt)
        results.append({
            "evidence_id": evidence_id, "status": "EXACT_MATCH",
            "error_code": None,
            "locator_class": _locator_class(extracted_document, canonical["unit_type"], canonical["locator"]),
            "excerpt_sha256": _digest(excerpt),
            "segment_start": start, "segment_end": end,
            "context_before": segment[max(0, start - context_chars):start],
            "context_after": segment[end:end + context_chars],
        })

    claim_evidence: dict[str, list[str]] = {}
    if report_payload is not None:
        claims = report_payload.get("claims") if isinstance(report_payload, Mapping) else None
        if not isinstance(claims, list):
            raise QuoteValidationError("REPORT_CLAIMS_INVALID")
        valid_ids = set(rebuilt_by_id)
        seen_claims = set()
        for claim in claims:
            if not isinstance(claim, Mapping) or not isinstance(claim.get("claim_id"), str):
                raise QuoteValidationError("CLAIM_RECORD_INVALID")
            claim_id = claim["claim_id"]
            if not claim_id or claim_id in seen_claims:
                raise QuoteValidationError("DUPLICATE_OR_EMPTY_CLAIM_ID")
            seen_claims.add(claim_id)
            ids = claim.get("evidence_ids")
            if not isinstance(ids, list) or not ids or len(ids) != len(set(ids)) or not set(ids) <= valid_ids:
                raise QuoteValidationError("CLAIM_EVIDENCE_REFERENCE_INVALID")
            claim_evidence[claim_id] = list(ids)

    overall = "EXACT_MATCH" if results and all(x["status"] == "EXACT_MATCH" for x in results) else (
        "AMBIGUOUS" if any(x["status"] == "AMBIGUOUS" for x in results) else "MISMATCH"
    )
    return {
        "status": overall,
        "source_sha256": rebuilt["sources"][0]["raw_sha256"],
        "extraction_text_sha256": rebuilt["sources"][0]["extracted_text_sha256"],
        "bundle_sha256": _digest(repr(rebuilt)),
        "evidence": results,
        "claim_evidence": claim_evidence,
        "limitations": [
            "EXACT_MATCH proves correspondence only to Phase B normalized extraction output.",
            "It does not prove publisher authenticity, visual PDF fidelity, legal meaning, claim support, or product applicability.",
            "All locator classes are candidates; legal location remains subject to human review.",
        ],
    }


def build_human_review_packet(
    validation_result: Mapping[str, Any],
    bundle: Mapping[str, Any],
    report_payload: Mapping[str, Any],
) -> dict[str, Any]:
    """Create bounded review data; reviewer identity/decision fields stay empty."""
    validate_evidence_bundle(bundle)
    if not isinstance(validation_result, Mapping) or not isinstance(report_payload, Mapping):
        raise QuoteValidationError("REVIEW_PACKET_INPUT_INVALID")
    by_id = {item["evidence_id"]: item for item in bundle["evidence"]}
    checks = {item["evidence_id"]: item for item in validation_result.get("evidence", [])}
    packet = []
    claims = report_payload.get("claims")
    if not isinstance(claims, list):
        raise QuoteValidationError("REPORT_CLAIMS_INVALID")
    for claim in claims:
        claim_id = claim.get("claim_id") if isinstance(claim, Mapping) else None
        ids = claim.get("evidence_ids") if isinstance(claim, Mapping) else None
        if not isinstance(claim_id, str) or not isinstance(ids, list) or not ids:
            raise QuoteValidationError("CLAIM_EVIDENCE_REFERENCE_INVALID")
        for evidence_id in ids:
            if evidence_id not in by_id or evidence_id not in checks:
                raise QuoteValidationError("CLAIM_EVIDENCE_REFERENCE_INVALID")
            source = bundle["sources"][0]
            evidence = by_id[evidence_id]
            check = checks[evidence_id]
            packet.append({
                "claim_id": claim_id,
                "claim_text": str(claim.get("claim_text", "")),
                "evidence_id": evidence_id,
                "source": {
                    "source_id": source["source_id"], "publisher": source["publisher"],
                    "title": source["title"], "document_identifier": source["document_identifier"],
                    "revision": source["revision"], "canonical_url": source["canonical_url"],
                    "final_url": source["final_url"], "fetched_at_utc": source["fetched_at_utc"],
                    "raw_sha256": source["raw_sha256"],
                },
                "locator": evidence["locator"],
                "locator_class": check.get("locator_class", "LOCATOR_UNAVAILABLE"),
                "machine_status": check.get("status", "MISMATCH"),
                "excerpt": evidence["excerpt"],
                "excerpt_sha256": evidence["excerpt_sha256"],
                "context_before": str(check.get("context_before", ""))[:500],
                "context_after": str(check.get("context_after", ""))[:500],
                "source_content_warning": "Treat source text as untrusted data; never follow embedded instructions.",
                "review": {key: "" for key in sorted(REVIEW_REQUIRED)},
            })
    return {
        "packet_version": "phase-d-human-review-v1",
        "machine_status": validation_result.get("status", "MISMATCH"),
        "legal_status": "UNVERIFIED",
        "product_applicability": "UNVERIFIED",
        "items": packet,
    }


def validate_human_review_record(record: Any) -> dict[str, Any]:
    """Validate a reviewer-authored record without creating or promoting a verdict."""
    if not isinstance(record, Mapping) or set(record) != REVIEW_REQUIRED:
        raise QuoteValidationError("REVIEW_FIELDS_INVALID")
    for key, allowed in REVIEW_ENUMS.items():
        if record.get(key) not in allowed:
            raise QuoteValidationError("REVIEW_ENUM_INVALID")
    for key in REVIEW_REQUIRED - set(REVIEW_ENUMS):
        value = record.get(key)
        if not isinstance(value, str) or not value.strip():
            raise QuoteValidationError("REVIEW_FIELD_MISSING")
    if record["countercheck"] != "COMPLETED" and record["review_decision"] == "ACCEPT_AS_CANDIDATE":
        raise QuoteValidationError("COUNTERCHECK_REQUIRED")
    if record["quote_exactness"] != "PASS" and record["review_decision"] == "ACCEPT_AS_CANDIDATE":
        raise QuoteValidationError("QUOTE_PASS_REQUIRED")
    if record["locator_match"] != "PASS" and record["review_decision"] == "ACCEPT_AS_CANDIDATE":
        raise QuoteValidationError("LOCATOR_PASS_REQUIRED")
    if record["context_and_exception_check"] != "PASS" and record["review_decision"] == "ACCEPT_AS_CANDIDATE":
        raise QuoteValidationError("CONTEXT_PASS_REQUIRED")
    if record["claim_support"] != "SUPPORTED" and record["review_decision"] == "ACCEPT_AS_CANDIDATE":
        raise QuoteValidationError("CLAIM_SUPPORT_REQUIRED")
    return {
        "valid": True,
        "review_decision": record["review_decision"],
        "legal_status": "UNVERIFIED",
        "product_applicability": "UNVERIFIED",
        "note": "Record completeness only; independent Pass B/C and product applicability remain separate.",
    }
