# Phase C — Evidence Bundle / JSON Schema v3 / Gemini Prompt v3

- Date: 2026-11-13
- Status: implementation and CI verification complete on cra-project-foundation.
- Approval: user explicitly approved the bounded Phase C proposal on 2026-11-13.
- Production integration: NOT IMPLEMENTED.

## Scope implemented

1. `evidence_bundle.py`
   - Joins Phase A `FetchResult` and Phase B `ExtractedDocument` in memory.
   - Requires registered `source_id`, successful HTTP 200 fetch metadata, exact canonical registry metadata, same-host HTTPS final URL, allowed MIME, matching byte count and raw SHA-256.
   - Requires extraction raw SHA-256 to match fetched bytes and extracted text SHA-256 to match extracted text.
   - Emits deterministic `EV-` IDs derived from source ID, raw hash, extractor version, locator, excerpt hash and segment index.
   - Excerpts are exact contiguous slices, limited to 2,000 characters each, 200 evidence entries and 100,000 total excerpt characters.
   - Does not write files, persist document bytes, fetch URLs, or store full extracted document text in the bundle.
   - `validate_evidence_bundle` rechecks bundle schema, registered source metadata, HTTPS final host, MIME, excerpt hashes, limits and deterministic IDs.

2. `cra_report_contract_v3.py`
   - Separate v3 contract; does not replace or import into v2 runtime.
   - Requires claim-level `evidence_ids`, candidate legal locator, `UNVERIFIED` legal location and product applicability.
   - Rejects missing/unknown/duplicate Evidence IDs, duplicate claim IDs, additional fields, invalid JSON and any status promotion.
   - Renderer derives `BUNDLE_LINKED_UNVERIFIED` or `NO_EVIDENCE` from actual references and resolves source/excerpt metadata from the bundle. The model cannot author source URLs or quote fields.

3. `schemas/cra_research_v3.schema.json`
   - Draft 2020-12 schema; Python schema parity is covered by a test.

4. `prompts/CRA_RESEARCH_PROMPT_V3.txt`
   - Requires the model to select only existing Evidence IDs, not create URLs, source metadata or quotations.
   - Treats source text as untrusted data and forbids following embedded instructions.
   - Keeps all claim/legal/product statuses `UNVERIFIED`.

5. Tests:
   - `tests/test_evidence_bundle.py`
   - `tests/test_cra_report_contract_v3.py`

## Safety and provenance boundaries

- Evidence ID linkage proves only that a claim references an item in the supplied bundle. It does NOT prove semantic relevance, legal interpretation, quote context, product applicability or independent corroboration.
- Hashes provide integrity consistency checks, not a digital signature or cryptographic proof of publisher authenticity.
- Source text and excerpts remain untrusted input. Prompt-injection-like text inside a source must not be followed.
- Evidence bundles are runtime data only. No full manufacturer PDF/HTML is committed to the public repository.
- No actual URL fetch, Gemini API call, billing change, paid service, OCR, PDF backend installation, `main.py` change, v2 prompt/contract change or production workflow change occurred.
- Phase D must separately implement exact quotation/context validation and human review. No automatic `VERIFIED` promotion is permitted.

## Expected regression checks

- Existing 55-test suite remains unchanged.
- New unit tests cover fetch/extraction hash mismatch, source registry mismatch, URL/MIME tampering, excerpt/hash/ID tampering, size limits, schema parity, unknown/duplicate Evidence IDs, invalid JSON, status promotion, and rendering.
- Verified: code commit `6344b576db64438e9a2ebfe5acdcc74afeac479e`, GitHub Actions #43338094337 SUCCESS; 79 tests passed and strict archive audit 990/990, consistent=true.


## Final verification record
- Corrected the initial CI import failure (IndentationError in segment loop) before acceptance.
- Exact tested code SHA: `6344b576db64438e9a2ebfe5acdcc74afeac479e`.
- Actions run #43338094337: SUCCESS; 79 tests passed; strict archive audit 990/990 and consistent=true.
- Protected production/v2 files unchanged. Phase C remains isolated and is not wired into production.
