# Phase D Design Proposal — Exact Quote / Locator Validation and Human Review

- Date: 2026-11-13
- Status: DESIGN BASELINE — implementation approved and recorded in [PHASE_D_IMPLEMENTATION.md](PHASE_D_IMPLEMENTATION.md). The proposal remains the scope reference.
- Depends on: Phase A source registry/fetcher, Phase B extraction adapters, Phase C Evidence Bundle v1 / CRA report v3.
- Target branch: `cra-project-foundation`.
- Production integration: explicitly out of scope.

## 1. Objective

Phase C binds model claims to existing Evidence IDs and preserves source/excerpt provenance. It does not prove that an excerpt is an exact source-derived segment, that a locator is legally correct, or that the excerpt supports the claim.

Phase D should add a deterministic validation layer and a human-review packet while preserving the rule that all legal/product claim statuses remain `UNVERIFIED` until the separate verification protocol is completed.

## 2. Current inputs and limitations

### Existing data available
- Phase A `FetchResult`: source ID, canonical/final URL, publisher/document metadata, HTTP status, MIME, byte count, fetched timestamp, raw SHA-256 and raw bytes.
- Phase B `ExtractedDocument`: source ID, extraction method/version, raw/text SHA-256, full normalized extracted text, structural candidate units, PDF page text and locator status.
- Phase C Evidence Bundle: source metadata plus bounded excerpts, excerpt SHA-256, deterministic Evidence IDs and candidate locators.
- Phase C report v3: atomic claim candidates with claim type, candidate legal location, Evidence IDs, UNVERIFIED legal-location/product-applicability fields and limitations.

### Known limitations
- Evidence Bundle v1 does not store character offsets or the full source document text.
- XML Article/Annex/paragraph/point hierarchy is structural extraction output, not an independent legal-location determination.
- HTML locators are text-derived candidates only.
- PDF locators are page-only; current tests use a fake reader. The optional pypdf backend is not installed in CI and OCR/scanned PDF support is absent.
- Evidence ID linkage and hashes do not prove semantic relevance, legal interpretation, publisher authenticity or product applicability.

## 3. Proposed architecture (no code changes yet)

### D-1 — Deterministic source/excerpt revalidation

Proposed module: `evidence_quote_validator.py` (new; pure Python, no network and no file writes).

Inputs:
1. Phase A `FetchResult` with raw bytes;
2. Phase B `ExtractedDocument`;
3. Phase C Evidence Bundle;
4. Phase C v3 report payload.

Validation sequence:
1. Revalidate the Evidence Bundle using the Phase C validator.
2. Check that fetch result, extracted document and bundle all have the same registered source ID.
3. Check HTTP 200, canonical registry identity, allowed MIME, same-host HTTPS final URL, byte count and raw SHA-256.
4. Check extractor version/method, raw SHA-256 and full normalized text SHA-256.
5. Rebuild the canonical Evidence Bundle from the same fetch/extraction pair using the canonical Phase C limits.
6. Compare each Evidence ID, source ID, locator, unit type, excerpt text and excerpt hash byte-for-byte/string-for-string with the supplied bundle.
7. Reject or mark BLOCKED any mismatch; do not repair or silently normalize mismatching evidence.

This reconstruction approach avoids storing the full source document in the bundle or public repository. It proves that the excerpt is an exact contiguous segment of the Phase B normalized extraction output, not that PDF visual text/OCR or publisher-authored page layout is independently verified.

### D-2 — Locator provenance classification

Every evidence item receives a machine-derived locator class:
- `XML_STRUCTURAL_CANDIDATE`: Phase B XML hierarchy candidate.
- `HTML_TEXT_CANDIDATE`: text-derived HTML locator candidate.
- `PDF_PAGE_ONLY`: page number only.
- `TEXT_LINE_ONLY`: fallback line number only.
- `LOCATOR_UNAVAILABLE`: no stable locator.

Machine validation may confirm that the locator is reproducibly derived from the selected extraction output. It must not label a legal provision VERIFIED merely because the string says “Article 13” or “Annex I”.

For CRA legal claims, the human reviewer must compare the locator against the current official EUR-Lex text, including parent/child structure, adjacent paragraphs, definitions, exceptions and amendment/consolidation date. Manufacturer claims require exact part number, document identifier/revision and relevant section/page.

### D-3 — Context packet generation

For each evidence item, create a review packet containing:
- Evidence ID and claim IDs referencing it;
- registered publisher/document/revision, canonical and final URL, fetched time and source hashes;
- extraction method/version and locator class/status;
- exact excerpt and excerpt hash;
- bounded preceding/following context where reproducibly available (target cap: 500 characters on each side);
- explicit warning that source content is untrusted data;
- machine checks and human-review fields.

Do not put full source documents or unrestricted extracted text into GitHub. Context is transient or limited to the review artifact; any persistent artifact should contain only bounded context and metadata.

### D-4 — Claim-to-evidence and legal review

Automated checks may identify missing evidence, mismatched source IDs, non-reproducible excerpts and invalid locators. They must not decide legal meaning or whether an excerpt semantically supports a claim.

Human review records, per claim:
- `QUOTE_EXACTNESS`: PASS / FAIL / BLOCKED;
- `LOCATOR_MATCH`: PASS / FAIL / BLOCKED;
- `CONTEXT_AND_EXCEPTION_CHECK`: PASS / FAIL / BLOCKED;
- `CLAIM_SUPPORT`: SUPPORTED / NOT_SUPPORTED / UNCLEAR;
- `COUNTERCHECK`: COMPLETED / NOT_COMPLETED, with counter-evidence and notes;
- `REVIEW_DECISION`: ACCEPT_AS_CANDIDATE / REVISE / REJECT;
- reviewer role/identifier, UTC timestamp, review protocol version and rationale.

A single reviewer completing a checklist is not automatically an independent second reviewer. Pass A/B/C independence requirements remain governed by `docs/VERIFICATION_PROTOCOL.md`.

## 4. Status model and fail-closed behavior

Machine status is separate from legal/product verification status.

| Machine result | Meaning | Allowed report effect |
|---|---|---|
| `EXACT_MATCH` | Excerpt reproducibly matches normalized extraction output | Evidence integrity check only |
| `MISMATCH` | Hash, ID, excerpt, source or locator mismatch | Reject bundle/report for that evidence |
| `AMBIGUOUS` | Multiple plausible source positions or unstable locator | Human review required; no exactness pass |
| `UNSUPPORTED_EXTRACTION` | Backend/format cannot reproduce the extraction | BLOCKED; no inferred pass |
| `SOURCE_UNAVAILABLE` | Original fetch bytes are unavailable | BLOCKED; do not rely only on stale bundle |
| `HUMAN_REVIEW_PENDING` | Machine checks passed but semantic/legal review incomplete | Claim remains UNVERIFIED |

No Phase D machine result may promote `UNVERIFIED` to `PARTIALLY_VERIFIED` or `VERIFIED`. Those are evidence-review outcomes governed by the verification protocol and separate human decision. Product applicability remains independently UNVERIFIED until product boundary and exact SKU evidence exist.

## 5. Proposed outputs

1. `QuoteValidationResult`: machine-only structured result with source hash, extractor version, bundle hash, per-Evidence-ID checks and stable error codes.
2. `HumanReviewPacket`: bounded Markdown/JSON review artifact with excerpts/context and empty reviewer fields.
3. `ClaimReviewRecord`: separate reviewer-entered record; machine code must not fabricate reviewer identity, time or decision.
4. Renderer: display machine status and human review status separately; never collapse them into one VERIFIED badge.

## 6. Regression and adversarial test plan

Required tests before any implementation can be accepted:
- Exact deterministic rebuild accepts a valid bundle.
- Mutated excerpt, excerpt hash, Evidence ID, locator, unit type, source ID or source metadata fails closed.
- Raw byte mutation, stale revision, MIME mismatch, HTTP error and final-host mismatch fail closed.
- Extracted text/hash mismatch and extractor-version mismatch fail closed.
- Same excerpt appearing more than once is AMBIGUOUS unless the deterministic segment/offset mapping uniquely resolves it.
- Segment boundaries, multi-part excerpts, empty lines, Unicode normalization and whitespace normalization are tested explicitly.
- XML nested Article/Annex/paragraph/point locators are classified as candidates only.
- HTML candidate locators and PDF page-only locators cannot be auto-promoted to legal location VERIFIED.
- Missing pypdf, encrypted/unsupported PDF, scanned PDF and OCR absence return BLOCKED/UNSUPPORTED, not PASS.
- Prompt-injection text inside extracted source remains inert data and is never executed or followed.
- Unknown/duplicate claim references and missing Evidence IDs are rejected.
- Machine exactness PASS does not promote legal or product status.
- Human review record requires all mandatory fields; missing countercheck/rationale cannot produce ACCEPT_AS_CANDIDATE.
- Deterministic output, stable error codes, no network/file writes, no full-source persistence.
- Full existing suite plus new tests and strict archive audit must pass on the exact final tested commit.

## 7. Risks and controls

| Risk | Control |
|---|---|
| Extraction output is not identical to visual PDF/original layout | Label result as normalized-extraction exactness only; PDF page locator only; manual source-view check |
| Repeated text creates ambiguous position | Rebuild with deterministic segment mapping; mark AMBIGUOUS if unique position cannot be proven |
| Legal locator parser mistakes hierarchy | Machine locator remains candidate; reviewer checks current official text and parent/child context |
| Prompt injection in source | Treat all excerpts/context as untrusted data; never execute or follow source instructions |
| Hash mistaken for publisher authenticity | State clearly that SHA-256 is integrity metadata, not digital signature |
| Human reviewer rubber-stamps AI output | Require independent Pass B/C evidence and explicit rationale/countercheck |
| Large context leaks source content | Bounded context only; no full source persistence in repo |
| Existing v3 bundle lacks offsets | Initial design uses deterministic canonical rebuild; any schema/offset change must be separately proposed and approved |

## 8. Scope, protected files and approval gates

This document is a design proposal only. No Phase D code has been implemented.

Explicitly excluded unless separately proposed and approved:
- changes to `main.py`, production workflow, v2 contract or v2 prompt;
- wiring v3 or Phase D into production;
- changing Gemini model order, API calls, billing, quotas or network schedule;
- live source fetching, OCR or adding dependencies;
- modifying Phase C bundle schema/IDs;
- automatic VERIFIED/PARTIALLY_VERIFIED promotion;
- main-branch changes, merge, rebase or synchronization.

Before Phase D implementation, present the exact file list/diff, status and schema changes (if any), test cases, threat analysis, rollout isolation and rollback plan, then obtain explicit user approval.
