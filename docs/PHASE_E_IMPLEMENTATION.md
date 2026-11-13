# Phase E Implementation — IP-pinned official-source transport and offline adversarial tests

- Date: 2026-11-13
- Status: **E1 + E2 IMPLEMENTED — CI VERIFIED**
- Branch: `cra-project-foundation`
- Baseline before implementation: `1b543af653435a25f89feea7f80abdf370ecda7f`
- Exact code/test verification HEAD: `d355aefb74f2b1b9159de98827fac8600fb68d4c`
- CI run: [CRA Archive Integrity #43367432101](https://github.com/useformotor3/ai-discord-bot/actions/runs/43367432101)
- Live official-source fetch: **NOT RUN**
- Production integration: **NOT IMPLEMENTED**

## 1. Scope completed

User approved E1 + E2 only:
- E1: implement a connection-time IP-pinned HTTPS transport for registered official sources.
- E2: offline adversarial tests for DNS/IP validation, TLS identity, redirects/retry boundaries and response handling.

The approval did not include E3 real official-source fetch, Gemini API calls, production integration, protected production files, or main-branch operations. None of those were performed.

## 2. Files changed

### New
- `source_transport.py`
- `tests/test_source_transport.py`

### Modified
- `source_evidence.py`
- `tests/test_source_evidence.py`: `b3a35fafd45a03277ec894589b9e2b137be8a95e`

No workflow or dependency file was changed. The transport uses only Python standard-library modules (`http.client`, `socket`, `ssl`, `ipaddress`); this avoids adding a package-install requirement to the existing archive-audit CI workflow.

## 3. Implemented transport controls

### 3.1 Resolve and validate all answers

- The fetcher resolves the current allowlisted hostname once per request hop.
- Every returned A/AAAA address is normalized and validated before any connection attempt.
- Any unsafe or invalid address in a mixed response causes fail-closed rejection of the entire DNS answer set.
- IPv4-mapped IPv6 is normalized to its IPv4 address and then checked.
- Loopback, private, link-local, multicast, reserved, unspecified, scoped IPv6, NAT64 well-known/local-use prefixes, 6to4 and Teredo addresses are rejected.
- Public IP candidates are de-duplicated and deterministically ordered.

### 3.2 Pin the actual TCP destination

- `PinnedHTTPSession` receives the already validated literal IP tuple.
- `_PinnedHTTPSConnection.connect()` calls `socket.create_connection((literal_ip, 443), ...)`, never with the URL hostname.
- There is no second hostname DNS resolution between preflight validation and TCP connect.
- Candidate failover is limited to the exact validated IP tuple and only occurs on TCP connection failure.
- TLS, HTTP protocol, response and certificate failures do not trigger a fallback to a different DNS answer.
- There is no implicit retry, proxy, environment proxy, or automatic redirect behavior.

### 3.3 Preserve TLS and HTTP hostname identity

- TCP destination: validated literal IP.
- TLS SNI: original allowlisted DNS hostname.
- Certificate hostname verification: original allowlisted DNS hostname.
- Certificate verification: required; hostname verification enabled; default OS trust store or an explicitly supplied CA bundle.
- `Host` is generated from the original hostname by `http.client`; the adapter filters user-supplied Host overrides to prevent duplicate/conflicting Host headers.
- `Accept-Encoding: identity` and `Connection: close` are used.
- TLS verification cannot be disabled through the adapter.

### 3.4 Redirect and response controls

- Automatic redirects are disabled at the transport.
- The existing fetcher handles redirects manually; every hop re-checks HTTPS, same-host policy, port, fragment and DNS/IP answers before connecting.
- Existing status 200, MIME allowlist, timeout, byte cap, SHA-256, source registry and response-close behavior remain.
- Non-identity Content-Encoding is rejected to avoid hidden compressed expansion/ambiguous byte accounting.
- Content-Length must be a non-negative decimal integer; empty, negative and malformed values are rejected.

## 4. Offline adversarial tests

New transport tests use a local TLS fixture. The fixture creates an ephemeral self-signed certificate with the expected DNS SAN using OpenSSL. During tests only, the socket connection function maps a supplied public-looking test IP to a loopback TLS server; the test records the exact IP passed to TCP connect. This is an offline harness and does not contact the public network.

Covered transport cases (14 tests):
1. IPv4-mapped IPv6 normalization and duplicate elimination.
2. Mixed public/private DNS answers fail closed.
3. Loopback, link-local, documentation/reserved, multicast and unsafe IPv6 ranges rejected.
4. NAT64, 6to4, Teredo and scoped IPv6 rejected.
5. Empty, malformed and non-string DNS answers rejected.
6. Actual local TLS handshake confirms literal pinned IPv4 destination, original hostname SNI, single original Host header and identity content encoding.
7. Public IPv6 literal is passed as TCP connect target while original hostname SNI is preserved (local route; not a real external IPv6 connection).
8. Certificate hostname mismatch is rejected.
9. Untrusted certificate chain is rejected.
10. Connection fallback uses only the supplied pinned IP list.
11. Connect timeout fails closed after the supplied pinned candidates.
12. Read timeout does not trigger fallback to another IP.
13. Caller-supplied private IP is rejected again at the transport boundary.
14. Disabled TLS verification and automatic redirects are rejected.

Additional fetcher tests verify:
- all DNS answers are passed as validated literal IPs;
- a mixed public/private answer set prevents any HTTP request;
- resolver invocation is not repeated by the transport contract;
- same-host redirect hops trigger DNS revalidation; HTTP downgrade redirects are rejected;
- compressed response bodies are rejected and closed;
- malformed/negative/empty Content-Length values and truncated bodies are rejected.
Existing regression tests continue to cover response status, MIME, byte limits, empty body, redirect host/limit, timeout arguments, metadata and SHA-256 behavior.

## 5. CI evidence

Exact code/test HEAD:
`d355aefb74f2b1b9159de98827fac8600fb68d4c`

GitHub Actions:
[Run #43367432101](https://github.com/useformotor3/ai-discord-bot/actions/runs/43367432101)

Verified job:
- `Run archive audit unit tests`: success
- `Ran 126 tests in 2.764s`
- `OK`
- `Verify archive and history consistency`: success
- `archive_count = 990`
- `history_entry_count = 990`
- `archive_missing_history = []`
- `history_orphans = []`
- `duplicate_history_paths = []`
- `malformed_history_entry_indexes = []`
- `consistent = true`

Earlier intermediate CI attempts failed while the transport briefly depended on packages not installed by the existing test workflow, and then while two new test expectations were incorrect. The implementation was changed to standard-library-only transport and the test expectations/content-length handling were corrected. The final exact code/test HEAD above passed all 126 tests and strict archive audit. Earlier failed runs are retained in GitHub Actions history and are not represented as successful.

## 6. Protected boundary and change review

The code/test delta from the Phase E baseline is limited to:
- `source_evidence.py`: `bf5258aa63692ad3fa1e07814b9d8f94899f3198`
- `source_transport.py` (new): `13160055d1785e6a788d78b9bc44bbb5eb0d20e8`
- `tests/test_source_evidence.py`: `b3a35fafd45a03277ec894589b9e2b137be8a95e`
- `tests/test_source_transport.py` (new): `a0cce1e3d1d9627f39bbcec7f3e2bfca263c619e`

The following hashes were re-read after implementation and remain unchanged:
- `main.py`: `997952702fdd9d2472468b82e6efdd65b2bb4376`
- `.github/workflows/run.yml`: `65a8cadc8eac593f551e390698e367b1d161ecf1`
- `prompts/CRA_RESEARCH_PROMPT_V2.txt`: `14e9ce8618bc447a371dc28fc725cda3636470c5`
- `cra_report_contract.py`: `e0c1f1db353f664ae8c817c2f335d3a6efef4076`
- `evidence_bundle.py`: `ad7227d9e89f74864f349d1b632d664752550fc1`
- `cra_report_contract_v3.py`: `911d616fec846fcbd361256ea08399c6fb50e93b`
- `schemas/cra_research_v3.schema.json`: `6afd04bafd4fe098972ce762e5354e2199ca237b`

The existing `.github/workflows/archive-audit.yml` was not changed. No main merge/rebase/sync, production workflow dispatch, main archive/history/state write, Gemini API call, or actual external source request was made.

## 7. Residual risks and limits

- The local TLS test proves the application passes the validated literal IP to the TCP connection function and uses the intended SNI/hostname checks; it does not prove real-world routing, NAT, transparent proxy or network egress behavior.
- The resolver and real DNS behavior were not exercised against the public Internet. Resolver integrity and DNS infrastructure remain trust assumptions.
- IPv6 transport was tested with an offline socket route that records the IPv6 literal; a real external IPv6 path was not tested.
- Conservative fail-closed treatment may reject legitimate CDN answers if any returned address is classified non-public or belongs to a blocked transition prefix. Do not weaken this policy without documented source/network evidence and separate review.
- TLS chain/hostname verification establishes a certificate chain trusted by the host trust store for the allowlisted hostname; it is not a publisher digital signature, pinned certificate, or guarantee of document authenticity.
- A legitimate HTTPS response can still be a login page, viewer shell, challenge, wrong revision, or unexpected document. Document identity/revision and extraction fidelity remain E3 checks.
- HTML/XML/PDF parser fidelity, PDF visual comparison, scanned-PDF OCR, legal interpretation, semantic claim support and product applicability remain unverified.
- This transport is still not connected to the production `main.py` workflow.

## 8. Rollback

- Revert only the Phase E code/test commits on `cra-project-foundation` if regression appears.
- Do not force-push, merge/rebase/sync with `main`, or alter the archive/history/state.
- Re-run the full archive-audit workflow and confirm the exact rollback HEAD and strict archive audit before considering rollback complete.

## 9. Next gate

E1 and E2 are complete. **E3 remains blocked pending separate explicit user approval.**

E3 would perform a small, controlled real-source fetch/extraction validation only after the user approves:
- one canonical EUR-Lex legal text response;
- one manufacturer HTML or PDF document;
- exact document identifier/revision checks;
- extraction output and source page/section comparison;
- in-memory raw bytes only, no public archive of complete source bytes or extracted documents.

No live fetch is authorized by the E1/E2 approval.
