# 공식 자료 수집·추출 코드 우선 개선 감사 및 변경 제안

- 문서 ID: CRA-COLLECT-CODE-AUDIT-001
- 버전: 1.0
- 기준일: 2026-11-13
- 상태: **감사 완료 / 코드 변경 별도 승인 대기**
- 범위: 작업 브랜치의 `source_evidence.py`, `source_extraction.py`, 관련 테스트, source registry 및 archive extraction workflow
- 비범위: 실제 외부 URL 접속, Gemini API, `main.py`, 운영 workflow, v2 prompt, main branch

## 1. 결론

**수집 코드를 먼저 개선하는 것이 타당하다.** 현재 구현은 안전한 네트워크 전송의 기본 골격과 mock parser를 갖추었지만, 실제 공식 문서를 올바르게 수집하고 그 revision·구조·내용을 재현성 있게 보존한다는 검증은 아직 없다.

현재 상태를 "수집 파이프라인 완성" 또는 "공식 원문 검증 완료"라고 표시해서는 안 된다. 정확한 표현은 다음과 같다.

- source registry / guarded fetcher: 구현, mock tests 중심
- pinned HTTPS transport: 구현, local TLS fixture tests
- HTML/XML/PDF parser: 구현, synthetic fixture tests
- live official fetch: NOT RUN
- real EUR-Lex Formex/XML serialization fidelity: UNVERIFIED
- real ST/TI HTML/PDF extraction fidelity: UNVERIFIED
- extraction → source evidence bundle → claim validator → report builder 통합: NOT IMPLEMENTED
- production `main.py` / Gemini prompt / workflow integration: NOT IMPLEMENTED

## 2. 현재 코드의 확인된 구조

| 구성 | 현재 동작 | 한계 |
|---|---|---|
| `source_evidence.py` | 고정 source_id만 fetch, HTTPS/host/DNS/IP/redirect/MIME/size/hash 검사 | registry revision/date는 코드에 수기 고정. 응답의 실제 문서 표지와 자동 대조하지 않음 |
| `source_transport.py` | validated literal IP로 TCP 연결, TLS SNI/hostname identity 유지 | 실제 공용 네트워크 경로·DNS resolver·투명 프록시/egress 검증은 미실시 |
| `source_extraction.py` | HTML text, EUR-Lex XML/HTML locator candidates, PDF page text | 실제 원문 fixture가 아님. HTML decode replacement 허용, HTML parser는 generic text extraction. PDF backend는 optional |
| `tests/test_source_*.py` | mock response, inline HTML/XML, fake PDF reader, local TLS fixture | 실제 공식 문서에 대한 fidelity 검증이 아님 |
| `.github/workflows/claim-evidence-extraction.yml` | archive Markdown에서 claim/URL/조항 후보 추출, JSON을 작업 브랜치에 커밋 | 공식 URL을 fetch하지 않으며 법령·출처·인용을 검증하지 않음. heuristic candidate extraction |
| `main.py` / run workflow | 기존 Gemini 조사·아카이브 자동화 | 신규 official-source fetcher/extractor와 연결되지 않음 |

## 3. 우선 개선 항목과 심각도

### P0 — 공식 문서 식별·revision 검증

**문제**
- SourceDefinition의 title/document ID/revision/date는 registry 상수다.
- FetchMetadata의 `published_or_revision_date`가 실제 응답에서 추출된 값이 아니라 registry revision 문자열을 복사한다.
- 따라서 파일이 갱신되거나 publisher가 다른 revision을 제공해도 metadata가 registry와 일치하는 것처럼 보일 수 있다.

**제안**
- registry의 revision을 expected_revision으로 명시하고 observed_revision과 분리한다.
- HTML/PDF에서 document number, revision, publication date를 추출하는 source-specific identity adapter를 추가한다.
- expected/observed mismatch 또는 관측 불가 시 `IDENTITY_UNCONFIRMED` / `REVISION_MISMATCH`로 fail-closed.
- HTTP Last-Modified/ETag는 보조 메타데이터로만 기록하고 공식 개정일로 취급하지 않는다.
- canonical URL, final URL, redirect chain, content hash, fetch time, MIME, byte count를 evidence record에 남긴다.

### P0 — 원문 바이트와 추출 텍스트의 무결성·손실 감지

**문제**
- HTML bytes는 UTF-8 decode with replacement로 처리하므로 문자 손실이 있어도 추출이 계속될 수 있다.
- HTML parser의 text extraction은 레이아웃/표/각주/숨김 콘텐츠/동적 렌더링 차이를 완전히 표현하지 않는다.
- PDF text extraction은 스캔 페이지, 표, 다단, 각주, 글꼴 인코딩 문제를 자동으로 식별하지 못한다.

**제안**
- strict charset decode 우선, 실패 시 인코딩 추정/대체 경로를 명시하고 replacement 문자 수·비율 기록.
- replacement 문자 또는 비정상적으로 낮은 텍스트 추출률이 임계치를 넘으면 `EXTRACTION_DEGRADED`로 격리.
- PDF page별 텍스트 길이, 빈 페이지, 총 페이지 수, 메타데이터, 암호화 여부, 이미지 기반 페이지 후보를 기록.
- OCR은 별도 승인·별도 평가 전 구현하지 않는다.
- HTML/XML/PDF raw SHA-256과 normalized text SHA-256, extractor version을 묶은 immutable evidence manifest를 생성한다.

### P0 — source fetch와 extraction 결과의 단일 evidence bundle

**문제**
- FetchResult와 ExtractedDocument는 별개 API다. fetch metadata, raw hash, extracted text hash, locator, excerpt, claim을 이어주는 영속 schema/build step이 없다.
- 현재 fetch content는 memory only이며 보고서 재현을 위한 manifest/short excerpt 저장 규칙이 완성되지 않았다.

**제안**
- source_id, source version, fetched_at, raw_sha256, text_sha256, extractor_version, locator, excerpt hash, verification state를 묶는 source evidence bundle schema 추가.
- 원문 전체 및 전체 추출문은 public repository에 저장하지 않는다.
- 짧은 excerpt는 출처당 인용 상한과 저작권 검토를 통과한 경우에만 저장한다.
- claim은 실제 bundle 내 evidence ID를 참조해야 한다. 모델이 임의 source URL/title/revision을 작성하지 못하게 한다.

### P1 — source-specific adapter와 registry 관리

**문제**
- EUR-Lex XML, EUR-Lex HTML, ST/TI 문서 페이지, TI PDF가 서로 다른 구조인데 generic parser의 적용 가능 범위가 제한적이다.
- ST/TI source URL과 revision이 바뀌면 코드 registry를 수정해야 한다.

**제안**
- publisher별 adapter interface와 fixture contract를 정의한다.
- registry를 source_id, canonical URL, expected document ID/revision, accepted MIME, max bytes, adapter ID, review date로 구성한다.
- source registry 변경은 근거 URL·공식 revision·검토자 기록과 함께 code review한다.
- redirect final URL은 allowlist host 내라도 source identity check를 통과해야 수집 성공으로 인정한다.

### P1 — 실행 상태와 실패 격리

**문제**
- 현재 fetcher 자체는 실패를 예외로 내지만, 이를 archive/report pipeline에서 draft/blocked 상태로 격리하는 연결은 없다.
- archive claim extraction workflow는 후보 JSON을 자동 커밋하지만 legal verification과 분리 표시가 필수다.

**제안**
- 상태 전이: DISCOVERED → FETCHED → IDENTITY_CONFIRMED → EXTRACTED → EVIDENCE_BUNDLED → QUOTE_MATCHED → HUMAN_REVIEWED.
- 각 단계 실패는 FAILED/BLOCKED/REVIEW_REQUIRED로 남기고 다음 신뢰 단계로 승격하지 않는다.
- heuristic archive candidates는 계속 `UNVERIFIED_AI_ARCHIVE` 상태를 유지하고 VERIFIED 보고서 입력으로 직접 사용하지 않는다.
- workflow 산출물에 source commit, tool version, input archive count, output hash, error counts를 기록한다.

### P1 — PDF backend 재현성과 호환성

**문제**
- `pypdf`는 lazy optional import이며 현재 tests fake reader를 사용한다.
- 현재 TI PDF source max size 20 MiB, extractor default input max 25 MiB로 제한값이 일치하지 않는다.
- 실제 CI 환경에서 pypdf가 설치되어 있지 않으면 PDF 추출은 명시적으로 실패한다.

**제안**
- 무료·오픈소스 조건에서 pypdf의 정확한 버전 pin 여부를 검토하고, dependency 변경은 별도 diff로 제시한다.
- real public-domain/synthetic PDF fixture를 저장소에 넣어 페이지/표/텍스트 추출 regression을 테스트한다.
- source-specific max bytes와 extractor limits를 일치시키고, encrypted/corrupt/scanned-only PDF를 별도 상태로 분류한다.
- 실제 TI PDF의 표지·목차·선정 페이지를 사람이 시각 대조하기 전에는 extraction fidelity를 VERIFIED로 올리지 않는다.

## 4. 권장 구현 순서

| 단계 | 작업 | 산출물 | live network |
|---|---|---|---|
| C0 | 기존 코드/테스트 baseline 고정, registry·metadata 계약 정리 | baseline test + change spec | 금지 |
| C1 | strict decode, identity/revision observed fields, degraded extraction flags | 코드·unit tests | 금지 |
| C2 | source evidence bundle + manifest + deterministic report input | schema/builder/tests | 금지 |
| C3 | EUR-Lex/ST/TI source-specific adapters 및 fixture hardening | parser/tests | 금지 |
| C4 | E3 승인 후 공식 URL 2종만 controlled live fetch | live validation report | 별도 승인 후 허용 |
| C5 | 수집/추출 결과를 claim validator 및 report builder에 연결 | non-production integration tests | 금지 |
| C6 | production main/prompt/workflow 통합 | 별도 보호 파일 승인 필수 | 별도 승인 필수 |

**중요:** C1–C3는 offline code/test만으로 진행 가능하지만 parser/validation gate 및 evidence contract를 바꾸므로 변경 전 사용자 승인이 필요하다. C4는 기존 Phase E3 별도 승인이 필요하다. C6는 운영 코드 별도 승인 없이는 진행하지 않는다.

## 5. 파일별 예상 diff

| 파일 | 제안 변경 | 위험 |
|---|---|---|
| `source_evidence.py` | expected/observed revision 분리, HTTP headers metadata, content identity adapter hook | 잘못된 identity parser가 false match 가능 |
| `source_extraction.py` | strict decode/degradation metrics, PDF quality diagnostics, adapter interface | parser별 결과 차이 |
| 신규 `source_bundle.py` | fetch+extract manifest, bounded evidence references | schema migration/oversize |
| 신규 `schemas/source_evidence_bundle.schema.json` | versioned bundle contract | 계약 변경 호환성 |
| `tests/test_source_evidence.py` | stale revision, header, redirect identity, charset tests | regression |
| `tests/test_source_extraction.py` | replacement chars, malformed HTML, empty/scanned PDF, page diagnostics | parser behavior change |
| 신규 `tests/test_source_bundle.py` | deterministic manifest/hash/size/status tests | schema edge cases |
| `docs/...` | source registry review records and implementation report | documentation drift |

변경하지 않을 파일:
- `main.py`
- `.github/workflows/run.yml`
- `prompts/CRA_RESEARCH_PROMPT_V2.txt`
- production model/quota/fallback/command templates
- `main` branch and production archive/history/state

## 6. 검증 계획

- Existing baseline: Phase E final CI 126 tests OK; exact docs HEAD CI run #43367623076 success. New changes require a fresh CI run.
- Unit: strict decode, source identity/revision match/mismatch, header metadata, redirect chain, PDF quality metrics, evidence manifest hashes.
- Negative: wrong document ID, stale revision, changed raw hash, invalid charset, HTML challenge, login page, viewer shell, PDF empty/scanned/encrypted/corrupt, oversized response, missing extractor.
- Integration mock: fetch fixture → extract → evidence bundle → exact quote check → draft report.
- Regression: full unittest suite and strict archive audit; exact SHA and run logs.
- Live E3: only after explicit E3 approval; two-source limited sample, no bulk crawling, no original document commits, manual page/paragraph visual comparison.

## 7. Rollback

- Before change record exact branch HEAD and all target file blob SHAs.
- Each C1/C2/C3 stage uses separate commit.
- On regression revert only the stage commit in the work branch; do not force push.
- Keep old parser API available or provide explicit version switch until tests prove compatibility.
- Do not rewrite or delete archive source files, history, state, or existing reports.
- Re-run full tests and strict archive audit after rollback.
- No merge/rebase/sync to main.

## 8. 승인 요청

우선 권장: **C1 + C2만 작업 브랜치에서 구현**. 이유는 현재 가장 큰 위험인 잘못된 문서 revision 표시, 추출 손실 은폐, source와 claim의 연결 부재를 우선 제거할 수 있고 실제 외부 접속 없이 테스트 가능하기 때문이다.

- [ ] C1: strict extraction integrity + observed source identity/revision checks
- [ ] C2: evidence bundle manifest + deterministic hash/locator linkage
- [ ] C3: source-specific adapters / PDF backend changes
- [ ] C4: E3 live official-source fetch (separate approval)
- [ ] C5: claim validator/report builder non-production integration
- [ ] C6: production main/prompt/workflow integration (separate approval)

**현재 상태:** C1+C2 구현 결과는 `docs/C1_C2_SOURCE_EVIDENCE_IMPLEMENTATION_REPORT.md` 참조. C3 이후, E3 live fetch, C5/C6는 미실행이며 각각 별도 단계/승인 필요.
