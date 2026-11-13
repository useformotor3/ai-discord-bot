# Phase D Implementation — Exact Quote Validation and Human Review

- Date: 2026-11-13
- Status: IMPLEMENTED — CI verification pending
- Target branch: `cra-project-foundation`
- Design: [PHASE_D_EXACT_QUOTE_VALIDATION_DESIGN.md](PHASE_D_EXACT_QUOTE_VALIDATION_DESIGN.md)

## Implemented files

- `evidence_quote_validator.py`: deterministic Phase C bundle rebuild/compare; per-evidence exact excerpt check against Phase B normalized extraction segments; locator provenance classes; bounded context; claim-to-evidence reference checks; human-review packet; reviewer-record completeness validation.
- `tests/test_evidence_quote_validator.py`: positive, tamper, duplicate-location, repeated-occurrence, unsupported extraction, context-boundary, claim-reference and human-review tests.

## Machine behavior

- `EXACT_MATCH`: exact contiguous match to Phase B normalized extraction output, with a unique segment/occurrence.
- `MISMATCH`: source, raw/extraction hash, bundle, ID, excerpt, metadata or claim-reference mismatch.
- `AMBIGUOUS`: duplicate locator segments or repeated excerpt occurrence.
- `UNSUPPORTED_EXTRACTION`: optional PDF backend/OCR/format cannot be reproduced.
- `SOURCE_UNAVAILABLE`: original source bytes/extraction are unavailable.

Machine outcomes are integrity/provenance results only. Locator classes remain candidates. Legal status and product applicability remain `UNVERIFIED`; no automatic promotion exists.

## Human review

The packet carries the exact excerpt, source metadata/hashes, locator class, bounded context (maximum 500 characters per side), claim reference, and explicit untrusted-source warning. Reviewer identity, UTC timestamp, protocol version, rationale, counter-evidence and review decisions are blank for the human to complete.

A candidate acceptance record requires quote, locator, context/exception and claim-support PASS plus a completed countercheck. The validator checks completeness and timezone presence; it cannot authenticate reviewer identity, prove independence, or substitute for Pass B/C.

## Boundaries

- No network requests, file writes, source persistence, OCR, dependency/workflow changes or production imports.
- No changes to `main.py`, `.github/workflows/run.yml`, v2 prompt/contract, Phase C schema/IDs, Gemini settings, or `main`.
- No merge/rebase/sync.

## Verification

- New test count and full-suite result: pending exact-head GitHub Actions.
- Strict archive audit: pending exact-head GitHub Actions.
- Protected-file SHA recheck: pending final implementation review.
- Live source fetch and Gemini API compatibility: not tested; not in scope.
