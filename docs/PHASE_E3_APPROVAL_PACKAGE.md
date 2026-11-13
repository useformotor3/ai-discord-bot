# Phase E3 — Controlled Live Source Validation Approval Package

- Date prepared: 2026-11-13
- Branch: `cra-project-foundation`
- Status: **DESIGN PACKAGE ONLY — NOT APPROVED / NOT EXECUTED**
- Prerequisites: E1 + E2 implemented and CI-verified; E3 remains a separate approval gate.
- This document does not authorize network requests by itself.

## 1. Decision requested

Approve or reject a one-time, tightly bounded live-source validation of exactly two registered source IDs:

1. `CRA_EURLEX_2024_2847` — EUR-Lex Regulation (EU) 2024/2847 current text.
2. `ST_AN5156_REV14` — STMicroelectronics AN5156, Rev 14 (June 2026), official HTML document page.

The run will validate actual HTTP responses, document identity/revision and extraction fidelity. It will not validate legal interpretation, product applicability, MCU feature applicability or CRA conformity.

## 2. Exact sources and limits

| Source ID | Publisher / document | Registered URL | Expected content | Maximum response |
|---|---|---|---|---:|
| CRA_EURLEX_2024_2847 | EU, Regulation (EU) 2024/2847, CELEX 32024R2847 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 | HTML/XHTML/XML as registered | 5 MiB |
| ST_AN5156_REV14 | STMicroelectronics, AN5156, Rev 14, June 2026 | https://www.st.com/content/st_com/en/technical-documents/an5156-introduction-to-security-for-stm32-mcus-stmicroelectronics.html | HTML/XHTML as registered | 5 MiB |

No other host, source ID, URL, redirect destination, document, login, API, account or paid service is in scope. The exact registry definitions and hashes are reviewed before execution. If either registered source has changed unexpectedly, stop and present a new diff/approval request rather than editing the registry in this run.

## 3. Execution sequence

1. Re-read exact branch HEAD and SHA-256/blob identities of `source_evidence.py`, `source_transport.py`, `source_extraction.py`, `evidence_bundle.py`, `evidence_quote_validator.py` and the relevant tests.
2. Confirm the E1/E2 transport still pins the validated literal TCP destination, retains original-host TLS SNI/certificate verification and Host identity, rejects unsafe DNS answers, disables proxy/automatic redirects and fails closed on stream/size/MIME/status errors.
3. Make one fetch attempt per source ID, sequentially, through `OfficialSourceFetcher.fetch(source_id)`. Do not add retries beyond the implementation's documented connect-candidate fallback. Do not manually browse to alternative URLs as a fallback.
4. Inspect metadata: source ID, canonical/final URL, publisher, document ID, expected revision, fetch timestamp, HTTP status, MIME, byte count, SHA-256 and error/status fields.
5. Reject challenge pages, login/consent screens, redirect landing pages, generic viewer shells, error pages, empty/truncated responses, unexpected MIME or any document whose identity/revision cannot be confirmed.
6. Parse only in memory:
   - EUR-Lex: use the existing HTML or XML extractor selected strictly by the returned MIME. For XML, compare structural unit candidates for Articles 13/14, Annex I Parts I/II and Annex II; for HTML, compare the visible text and bounded excerpts against the corresponding official rendered sections.
   - ST AN5156: use the existing HTML extractor. Confirm the visible page/document title, document number AN5156, Rev 14 and June 2026. If the response is only a document landing page or does not expose the actual technical text/revision, mark extraction fidelity BLOCKED/INSUFFICIENT and stop; do not discover/download an unregistered PDF in this approval.
7. Perform manual source-to-extraction checks on selected legal/technical passages, preserving headings, subpoint labels and adjacent context. Record extraction omissions, reordered text, duplicated text, malformed characters and locator limitations.
8. Generate only a bounded evidence record. Re-run deterministic Evidence Bundle and exact-quote checks on selected excerpts if the APIs accept the returned in-memory fetch/extraction objects without writing full text. Machine exact match is not legal verification.
9. Update only a new E3 result document and the session/status/plan records on `cra-project-foundation`. No source registry, parser, transport, schema or production file changes are pre-approved.

## 4. Data handling and privacy

- Raw response bytes and full extracted text remain in memory only.
- Do not commit or upload complete HTML/XML/PDF, complete extracted text, cookies, headers containing secrets, account data, personal data or server tokens.
- Persist only: source ID, publisher, document identifier/revision, canonical/final URL, fetch timestamp, status, MIME, byte count, SHA-256, extractor version, bounded excerpts (maximum 500 characters per side, subject to existing validator limits), locator candidates and human review notes.
- Do not use Gemini API, Discord, Google Drive, third-party extraction services, OCR services or paid APIs.
- No account login, consent acceptance, subscription, payment or plan upgrade. If a site requires one, stop.

## 5. Acceptance criteria

Each source must independently satisfy all applicable items:

- HTTP 200 and expected MIME; HTTPS hostname/port/redirect policy maintained.
- Actual TCP destination is one of the prevalidated public IPs; TLS certificate chain and hostname validation pass for the original registered hostname.
- Response is within the registered byte cap and has a complete, non-empty body.
- Publisher/document identity and exact revision/date match the registered target, not merely the URL slug or page title.
- Extractor version and raw/text hashes are recorded; extraction is deterministic when run twice against the same in-memory bytes.
- Selected passages match the official page/document text, including provision/section labels and surrounding context. Any material omission, reordering or ambiguous locator is documented and prevents a PASS for that passage.
- No complete source bytes or full extracted document text are persisted.
- Legal meaning, claim support and product applicability remain human-reviewed statuses; no automatic VERIFIED promotion.

Possible per-source outcomes: `PASS_METADATA_AND_EXTRACTION`, `PARTIAL_METADATA_ONLY`, `BLOCKED_UNEXPECTED_DOCUMENT`, `BLOCKED_SOURCE_UNAVAILABLE`, `FAIL_INTEGRITY_OR_TRANSPORT`. Overall E3 cannot be marked complete if either source is blocked or any critical integrity check fails.

## 6. Risks and stop conditions

Stop immediately if:
- DNS answer set contains any unsafe/invalid address or TCP cannot be pinned to the validated address.
- TLS chain/hostname validation fails.
- Redirect leaves the registered hostname, HTTPS is downgraded, or a nonstandard port is requested.
- Response MIME, status, size, Content-Length or stream completeness violates policy.
- Source content is a challenge, login, consent, viewer shell, error or unexpected document.
- AN5156 revision/date cannot be verified from the returned official content.
- The EUR-Lex text is not identifiable as CELEX 32024R2847/current OJ text.
- Any code, dependency, registry, parser, production, Gemini, account or paid-service change appears necessary.
- Any output would require storing full source bytes or full extracted text.

Do not weaken the transport policy or broaden the source registry to force success. A blocked result is a valid security outcome.

## 7. Rollback and change boundary

- E3 is read-only with respect to source and production code; no source bytes are persisted.
- If a documentation mistake is found, correct only the E3 result/documentation commit on the work branch.
- No force push, merge, rebase, sync or main-branch write.
- No changes to `main.py`, `.github/workflows/run.yml`, `.github/workflows/archive-audit.yml`, Gemini v2/v3 prompts/contracts, model/fallback/quota, archive/history/state or existing source registry.
- If implementation changes become necessary, stop and prepare a separate proposal with exact diff, impact, tests and rollback.

## 8. Approval record

**Current status: WAITING FOR EXPLICIT USER APPROVAL.**

To authorize only this bounded run, the user must explicitly say: **“E3 실행 승인”**. A general “진행” or approval of this design package is not treated as approval for live network access. If approved, execution remains limited to the two source IDs and conditions above.
