# CRA 프로젝트 — AI 연속성·실행 현황판

- 문서 ID: CRA-OPS-CONTINUITY-001
- 기준일: 2026-11-13
- 기준 작업 브랜치: `cra-project-foundation`
- 마지막 확인 작업 HEAD: **브랜치 tip을 새 세션 시작 시 실시간 조회** (이 문서에 고정 SHA를 두지 않음)
- 마지막 확인 main HEAD: `6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0` (Auto-archive: Research report #119)
- 상태: **상시 갱신 운영 기준 문서**
- 목적: 새 대화에서도 AI가 목표·현황·성과·실패·미완료·다음 행동을 추측 없이 복원하고, 과정 작업에 매몰되지 않고 실제 CRA 산출물을 계속 완성하도록 한다.

> 이 문서는 과거 기록의 요약본이자 현재 실행 기준이다. 과거 SESSION_LOG와 설계 문서의 충돌하는 문구는 이 문서의 최신 결정과 현재 Git 상태로 해석한다. 새 세션은 반드시 저장소에서 이 문서와 연결 문서를 다시 읽는다.

## 1. 프로젝트의 유일한 현재 목표와 범위

**목표:** CRA(Cyber Resilience Act)를 서보 드라이브 제품 개발·출시·지원에 적용하기 위한 공개 근거 기반 조사, 요구사항 해석, 제품 적용성 검토, 보안 HW/FW 참조 설계, 시험·증거 체계, 실제 보고서 작성.

- 현재 프로젝트는 **CRA 전용**이다.
- SIL 3 벤치마킹은 현재 범위가 아니다. 사용자가 새로 요청하지 않는 한 SIL 3 보고서나 기능안전 벤치마킹으로 범위를 확장하지 않는다.
- CRA와 기능안전은 필요할 때 경계·인터페이스 영향만 구분한다. CRA 결과를 SIL/PL 적합성 증거로 바꾸지 않는다.
- 제조사 MCU 조사 우선순위는 ST이며 TI는 비교·참고다. 정확한 ST MCU 주문 코드가 확인되기 전에는 ST 부품별 기능을 확정하지 않는다.
- 독자는 CRA를 처음 접하는 서보 드라이브 HW/FW/시스템 개발자, 품질·PSIRT·제품책임자다.
- 비용 0원 우선, 공개 저장소에는 공개 가능한 자료만 보관한다.
- 제품 SKU, intended purpose, EU 공급 형태, 제품 경계, 실제 인터페이스·업데이트 방식, 지원기간, ST MCU 주문 코드가 확보되기 전 제품별 CRA 적용성·분류·적합성은 UNVERIFIED다.

## 2. 작업을 시작할 때 반드시 복원할 현재 사실

| 구분 | 확인된 현재 상태 |
|---|---|
| 작업 브랜치 | `cra-project-foundation` |
| main 브랜치 | 읽기 전용. 병합·rebase·sync 금지 |
| main 최신 관찰 | HEAD `6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0`, report #119; state count 119; history 1,394 entries; archive tree count not rechecked |
| main 자료 상태 | history.json 1,394 entries; state.json count 119 (당일 카운터); archive tree count는 이번 조회에서 미확인 |
| 작업 브랜치 아카이브 | 최근 strict audit 기준 990개 / history 990개 정합 |
| main과 작업 브랜치 | diverged; ahead/behind 수치는 변경되므로 새 세션마다 동적 재조회. merge base `b425b6db591e34abe003522157cf97ecf2240d9f` |
| 최근 코드 검증 | Phase D hardening exact HEAD CI #43384495713 success: 140 tests, archive 990/990, consistent=true |
| 최근 문서 검증 | continuity/audit 갱신 후 CI #43384628893 success: 140 tests, archive 990/990, consistent=true |
| 보호 파일 | main.py, production run.yml, V2 prompt/contract, Phase C bundle/schema/V3 contract 변경 금지. 별도 승인 없이 수정하지 않음 |
| E3 | 실제 공식 URL fetcher 실행은 별도 승인 필요. 승인 전 실제 E3 실행 금지 |
| Gemini API | 이 프로젝트 진행 중 실제 API 호출·유료 기능 사용을 기본 실행하지 않음. 별도 승인/필요성 확인 |
| 제품 시험 | 실제 제품 DUT 시험은 NOT_RUN |

## 3. 실제로 완료된 주요 작업

### A. 아카이브·과거 조사 품질 감사
- 기존 작업 브랜치 archive/history 990/990 정합성 검사 체계와 GitHub Actions를 구축했다.
- main의 신규 자동 조사 보고서가 작업 브랜치에 누락된 문제를 발견해 감사 대기열 `docs/CRA_ARCHIVE_AUDIT_QUEUE.md`를 만들었다.
- main 보고서 #8–#12: 5건 모두 CONFLICT, 직접 인용 재사용 0/5.
- main 보고서 #13–#27: 15건 모두 CONFLICT, 직접 인용 재사용 0/15.
- main 보고서 #28–#32: 2026-11-13 현재 배치 감사에서 5건 모두 CONFLICT, 직접 인용 재사용 0/5. 상세는 `docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md`.
- 앞선 별도 34개 위험기반 표본은 VERIFIED 0 / PARTIALLY_VERIFIED 6 / REJECTED 28. 비무작위 표본이므로 전체 archive 오류율로 일반화하지 않는다.
- main의 원본 archive/history/state는 읽기 전용으로 보존한다. 교정은 작업 브랜치의 별도 감사·claim ledger에서 수행한다.

### B. 수집·추출·증거 파이프라인
- Phase A: 공식 출처 registry 기반 fetcher, HTTPS/host/redirect/MIME/status/timeout/size/hash 통제.
- Phase B: HTML/XML/PDF text extraction adapter 및 locator 후보 생성. 실제 PDF/OCR·실문서 fidelity는 별도 검증 필요.
- Phase C: Source Evidence Bundle, raw/text hash, source identity/revision, bounded excerpt, deterministic Evidence ID, schema/contract.
- C1+C2: strict decoding, extraction diagnostics, source bundle integrity.
- Phase D: quote reconstruction/locator validation, human review packet. 최신 hardening은 validation result와 bundle hash/Evidence ID set 연결, claim-level status, structured countercheck, future timestamp rejection.
- Phase E E1/E2: IP-pinned HTTPS transport와 offline adversarial tests. **E3 live official-source fetch는 아직 승인·실행되지 않았다.**
- Hash는 consistency/integrity check이며 publisher signature/authenticity proof가 아니다. Exact quote match는 법적 의미·제품 적용성·semantic support를 입증하지 않는다.

### C. 실제 CRA 문서 산출물
- 제1권 `docs/CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md`: 법령·제조사 의무·적용성 조사 초판.
- 제2권 `docs/SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md`: HW/FW 적용·인터페이스·업데이트·시험 계획 초판.
- `docs/CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md`: Article 14 신고 대응 절차 초판.
- `docs/SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md`: 보안 하드웨어 참조 아키텍처 초안.
- `docs/CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md`, `docs/CRA_INTEGRATED_TRACEABILITY_MATRIX.md`: 요구사항-위협-HW/FW-시험-증거 연결 초안.
- `docs/THREAT_MODEL_SERVO_DRIVE_CRA.md`, `docs/SECURITY_TEST_EVIDENCE_REGISTER.md`, Annex II 사용자 정보 체크리스트 등.
- 이들은 실제 파일 산출물이지만 **초판/초안/템플릿**이다. 제품별 적합성 보고서나 완료된 제품 시험 결과로 표현하지 않는다.

## 4. 발견한 반복 실패와 교훈

1. 자동 조사 아카이브가 쌓이는 속도에 비해 개별 주장 원문 검증이 뒤처졌다.
2. 과거 자동 보고서에 조항 번호 혼동, 합성·오기 인용, 현행 법령과 다른 초안 문구, 제품 분류 단정이 반복됐다.
3. “새 주제”를 강제하는 반복 자동 조사로 중복·법령 오해가 계속 생산될 수 있다. 보고서 개수나 자동화 실행 횟수를 진척으로 보지 않는다.
4. 수집 코드·검증 프레임워크를 오래 개선하면서 완성 보고서 내용 보강이 지연될 위험이 있다.
5. 같은 AI의 반복 검토는 독립 제3자 검증이 아니다. Pass A/B/C는 별도 반증 절차이지 외부 독립 감사로 과장하지 않는다.
6. 이전 문서의 계획/상태/일정은 최신 branch, commit, CI, 원문으로 다시 확인해야 한다. stale한 계획을 현재 사실로 복사하지 않는다.
7. **과정 산출물만 남기는 세션을 피한다.** 예외가 합리적인 코드·설계·안전 감사 작업이 아니라면, 매 작업에 보고서 장·비교표·검증 대장·설계 산출물 등 사용 가능한 결과물을 하나 이상 남긴다.

## 5. 앞으로의 작업 방식 — Output-first + evidence-first

매 작업은 아래 순서로 수행한다.

1. **복원:** 현재 branch HEAD, 최근 commit, 이 현황판, PROJECT_STATUS, MASTER_PLAN, MASTER_REPORT_INDEX, 최근 SESSION_LOG, 대상 파일을 읽는다.
2. **선택:** 최우선 P0/P1 문제 하나를 고르고, 왜 지금 하는지와 기대 산출물을 명시한다.
3. **근거:** 공식 원문·정확한 revision·조항/페이지/locator를 확인한다. 가능한 경우 별도 공식 출처 교차검증과 반증 검토를 한다. 미실시한 확인은 명시한다.
4. **작성:** 가능한 한 보고서 본문/표/설계/claim ledger를 실제 파일로 먼저 또는 코드와 함께 만든다.
5. **코드:** 결과물의 정확성·재현성·추적성을 높이는 데 필요한 경우 코드를 수정한다. 코드를 수정하지 않는 것을 목표로 삼지 않는다.
6. **검증:** diff와 저장 파일을 재열람하고 링크·ID·표·참조·상태를 확인한다. 코드 변경이면 focused tests, full tests, strict archive audit, exact-HEAD CI.
7. **기록:** 이 문서, PROJECT_STATUS, MASTER_PLAN, MASTER_REPORT_INDEX, SESSION_LOG를 실제 결과에 맞게 업데이트한다.
8. **보고:** 사용자에게 이번에 만든 파일/표/장, 검증 결과, 남은 미확인, 다음 작업을 짧고 명확히 제시한다.

### 매 작업 종료 시 답해야 하는 질문
- 이번에 실제로 만들어진 결과물은 무엇인가? 저장소 경로는?
- 무엇을 원문/독립 근거로 확인했는가?
- 무엇이 VERIFIED / PARTIALLY_VERIFIED / CONFLICT / UNVERIFIED / NOT_RUN인가?
- 이번 작업에서 잘한 점과 부족한 점은 무엇인가?
- 다음 행동은 무엇이며, 왜 그것이 최우선인가?
- 코드만 변경했다면 왜 보고서 결과물이 이번에는 예외였는가?

## 6. 현재 우선순위

### P0 — 현재 진행
1. **#8–#57 개별 주장·직접 인용 원자 분해:** 파일 중심 Claim ID를 세부 원자 Claim ID로 분해하고 공식 원문·정확한 조항/locator·정정·반증과 연결.
2. **상위 문서 전수 대조:** Claim Evidence Ledger와 제1권·제2권·PSIRT SOP·요구사항/통합 매트릭스·위협 모델·시험 증거 대장의 문장/요구 ID/상태/예외를 교차 대조.
3. #13–#57 영문 상세 감사 문서를 원본 보존 + 한국어 상세판 또는 한국어 본문으로 전환.
4. 다음 main-only 감사 #63–#67. 배치 시작 시 main HEAD/state/history를 재조회하고 원본 SHA를 고정한다.

### P1 — 이어서 진행
5. ST AN5156 등 제조사 공식 자료를 source register/claim ledger에 연결하되, 최신 revision 인덱스만 확인된 자료는 본문 확인 전 인용 금지.
6. 실제 ST MCU 주문 코드가 없으므로 일반 ST 기능 설명과 부품별 적용성 결론을 분리한다.
7. 제품 입력자료가 확보되면 Product Boundary & CRA Applicability Decision Record를 작성한다.
8. PSIRT 역할/연락처/T0 기록 필드 보완 및 tabletop 설계. 실행은 조직 승인 후.

### P2 — 보류/승인 필요
9. E3 real official source fetch: 별도 승인 전 실행 금지.
10. main.py, production workflow, Gemini V2 prompt/contract, production integration: 별도 change proposal 및 명시적 승인 전 수정 금지.
11. main 브랜치 merge/rebase/sync: 명시적 승인 전 금지.
12. 유료 서비스·유료 API·외부 배포: 사용자 승인 없이 실행 금지.

## 7. 완료 판정 원칙

- 문서 파일 생성만으로 내용 VERIFIED가 되지 않는다.
- 코드 테스트 PASS는 코드 동작의 지정 범위만 검증한다. 법령·제품 적용성 검증과 혼동하지 않는다.
- report archive 1,366개라는 수치는 파일 수이지, 검증 완료된 자료 수가 아니다.
- 현재 main archive 1,366개 중 개별 Pass A/B/C 완료 수를 전체 완료로 추정하지 않는다. 각 감사 배치와 대기열을 따로 집계한다.
- 제1권·제2권은 초판이며, 제품별 미확인 입력과 실제 시험이 남아 있다.
- 사용자 승인 없는 E3, production integration, main 변경, merge/rebase/sync를 하지 않는다.

## 8. 다음 세션 필수 읽기
1. 이 문서 `docs/AI_CONTINUITY_BOARD.md`
2. `START_HERE.md`
3. `docs/AI_RULEBOOK.md`
4. `docs/PROJECT_STATUS.md`
5. `docs/MASTER_PLAN.md`
6. `docs/MASTER_REPORT_INDEX.md`
7. `docs/CRA_ARCHIVE_AUDIT_QUEUE.md`
8. `docs/RESEARCH_DOUBLE_CHECK_STANDARD.md`
9. 최신 `SESSION_LOG/2026-11-13.md`
10. 다음 작업 대상 archive와 기존 감사 문서 원문

새 세션에서 이전 대화의 기억을 믿고 바로 구현하지 말 것. 현재 저장소를 재조회하고 이 문서의 HEAD/수치가 최신인지 먼저 확인할 것.


## 2026-11-13 진행 업데이트 — main reports #33–#37
- [#33–#37 수동 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md) 생성: 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/5.
- #33 CVD 채널/보안 권고문 요건을 특정 PGP 방식 의무로 과장; #34 CVD/Article 14 혼합 및 Article 11 오기; #35 unique password/port restrictions를 보편적 법정 의무로 과장; #36 Article 13(6)/지원기간/무상 업데이트 혼합; #37 Article 24 오기 및 Class I/II 자동 분류 오류.
- 누적 수동 감사: #8–#37, 총 30건. #8–#12 5, #13–#27 15, #28–#32 5, #33–#37 5. 30건 모두 CONFLICT, 직접 인용 재사용 0/30. 연속·비무작위 배치이며 전체 archive 오류율이 아님.
- 다음 감사 대상 #38. main tip은 새 세션/다음 배치 시작 시 재조회.


## CI verification after #28–#37 audit updates
- Audit/documentation HEAD `5fcd433436cc6261284d1bc8bbf648ae78af9b2e`: GitHub Actions [#43386808125](https://github.com/useformotor3/ai-discord-bot/actions/runs/43386808125) SUCCESS.
- Full unittest suite: 140 tests passed.
- Strict archive audit: 990 archive / 990 history / 990 unique valid paths; missing, orphan, duplicate and malformed entries all 0; consistent=true.
- This CI validates repository tests/archive consistency, not legal interpretation or product applicability.

## 2026-11-13 진행 업데이트 — main reports #38–#42

- main HEAD 재조회: `e9bc84bfb5ccc7c18a69298cbd8f88376691b18c` (Auto-archive report #93); main state `2026-11-13 / count 93`; history.json 1,368 entries. 이전 현황판의 main HEAD #91 및 archive/history 1,366 수치는 현재 기준으로 오래되었으므로 최신 수치로 대체해야 한다.
- reports #38–#42 원문과 history metadata를 다시 조회하고 blob SHA를 기록했다.
- 신규 [#38–#42 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_38_42_2026-11-13.md): 4 CONFLICT / 1 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- 주요 교정: Annex II point 8(d)는 안전한 폐기 및 사용자 데이터 제거 방법에 관한 지침 제공이며, 모든 제품에 복구 불가능한 NAND/EEPROM 소거 기능을 명시한 문구가 아니다. Annex II point 7/8은 사용자 정보·지침서 요구다. 무상 업데이트는 Annex I Part II(8), 지원기간은 Article 13(8), 제공된 업데이트 가용성은 Article 13(9). CVD/연락/공개/안전 배포는 Part II(4)–(7)로 구분한다.
- EUR-Lex Regulation (EU) 2024/2847 공식 HTML의 Article 13 및 Annex I/II 원문을 이번 배치에서 다시 열어 대조했다. 별도 제3자 법률검토, E3 controlled fetch, PDF 시각검토, 제품별 기술자료 확인은 하지 않았다.
- 누적 main-only 감사 #8–#42: 35건 중 34 CONFLICT / 1 PARTIALLY_VERIFIED / 0 VERIFIED. 연속·비무작위 표본이므로 전체 archive 오류율이 아니다.
- 다음 감사 시작점 #43. main은 계속 읽기 전용이며 branch merge/rebase/sync는 수행하지 않는다.



## 2026-11-13 — 최신 Git/CI 상태 재확인
- 작업 브랜치 HEAD: `3bec6968cf214a3748595a465b01cd308bf7dc25`; main HEAD: `e9bc84bfb5ccc7c18a69298cbd8f88376691b18c` (#93).
- main `research_archive` 실제 tree 파일 1,368개, `history.json` 1,368개, `state.json` count 93. Tree 응답 truncated=false로 확인.
- main 대비 작업 브랜치: diverged, ahead 657 / behind 384. Merge base `b425b6db591e34abe003522157cf97ecf2240d9f`. merge/rebase/sync 금지 유지.
- 최신 작업 commit `3bec6968cf214a3748595a465b01cd308bf7dc25`은 문서 8개만 변경했다. main.py, production workflow, prompts, contracts, schema, evidence bundle 등 보호 파일 변경 없음.
- 해당 exact HEAD의 Actions run은 조회되지 않았고 commit status는 pending / 0 statuses다. 따라서 이번 문서 변경에 대한 CI는 **미실행/미확인**이다. 마지막 확인된 이전 CI success(140 tests)는 과거 commit에 대한 결과이지 현재 HEAD의 CI 결과가 아니다.


- 참고: #38–#42 감사 본문 commit은 `3bec6968cf214a3748595a465b01cd308bf7dc25`; 그 후 연속성·대기열의 stale baseline을 보정한 문서 전용 commit이 추가되었다. 정확한 현재 HEAD는 매 세션 GitHub branch endpoint에서 확인한다.

## 2026-11-13 진행 업데이트 — main reports #43–#47

- 최신 main 재조회: HEAD `a3d5b567f216f5e001e643513ee7ce87443a806d` (report #98); state count 98; history.json 1,373 entries; recursive tree에서 research_archive 1,373개, truncated=false.
- 날짜+count+path로 2026-11-13 report #43–#47을 고정해 원문 5건과 blob SHA를 기록했다.
- 신규 [#43–#47 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md): 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- 핵심 발견: report #43의 “IACS/PLC/servo drives are Annex III Class II” 인용은 최종 CRA Annex III에 없다. Annex III Class II의 네 범주와 Implementing Regulation (EU) 2025/2392의 technical description을 대조했다. Article 7의 core functionality 기준 및 통합 구성요소만으로 분류가 자동 성립하지 않는다는 점도 반영했다. 적합성 평가는 Article 24가 아닌 Article 32.
- #44 접근통제의 실제 근거는 Annex I Part I point 2(d). RBAC/least privilege/unique credentials 등은 위험기반 구현 수단이지 CRA가 보편 구현방식으로 각각 명시한 문구가 아니다.
- #45–#47은 Article 13, Article 14, Annex I Part I 2(c), Part II(1)–(8)의 위치와 예외를 재정렬했다. Article 13(8) 최소 5년 지원기간의 5년 미만 예상 사용 예외, Article 13(9) 업데이트 가용성, Part II(8) 무상 제공 및 tailor-made/business-user 별도 합의 예외를 분리했다.
- 누적 main-only 감사 #8–#47: 40건, 36 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/40. 연속·비무작위 표본이므로 전체 archive 오류율 아님.
- 작업 branch 최신 기준(커밋 직전): `a1fd870632fdfdb0bf5ca04804515aaf0e37f868`; main 대비 diverged, ahead 659 / behind 389, merge base `b425b6db591e34abe003522157cf97ecf2240d9f`. main read-only, merge/rebase/sync 금지.
- 다음 감사 #48–#52. 보호 파일은 이번 배치에서 수정하지 않는다.

## 2026-11-13 실무 산출물 추가 — 제품 분류/접근통제 매트릭스 v0.1

- 신규 문서: [CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md).
- 목적: #43–#44 감사 결과를 실무용 분류 판단표와 접근통제 설계/시험 증거표로 전환.
- 핵심: 서보 드라이브가 Annex III Class II라고 자동 가정하지 않는다. Article 7 core functionality, Annex III, Implementing Regulation 2025/2392 technical descriptions를 적용한다. 접근통제는 Annex I Part I 2(d); RBAC/least privilege/unique credentials 등은 법문과 구분된 위험기반 설계 수단이다.
- SKU, intended purpose, 제품 경계 및 기술자료 미확보로 제품별 분류/적합성은 UNVERIFIED.



## 2026-11-13 사용자 의도·문서 통합 운영 결정 추가

### 사용자가 명확히 한 최종 목적
- 프로젝트 결과는 CRA 조사 기록 자체가 아니라, 검증·수정한 내용을 취합한 실제 보고서와 매뉴얼, 실무 설계·시험 자료다.
- 문서가 지나치게 쪼개지면 최신 기준과 관련 근거를 찾기 어렵다. 모든 내용을 한 파일로 합치지는 않되, 문서별 역할과 정본 위치를 분명히 하고 상위 문서에서 연결해야 한다.
- 전체 문서 구성, 역할, 링크를 모은 탐색 문서가 필요하다.
- 행동강령과 사용자의 의도는 대화에서만 기억하지 말고 저장소 운영 문서에 계속 반영해야 한다.

### 반영한 운영 구조
- 신규 [CRA 문서 구조·전체 목차·링크 안내](CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md)를 전체 문서 지도 정본으로 추가했다.
- START_HERE에서 문서 지도를 필수 읽기 항목으로 연결한다.
- AI_RULEBOOK에 문서 생성 억제, 정본 지정, 감사 결과의 보고서 반영, 문서 간 중복·불일치 방지 규칙을 추가한다.
- MASTER_REPORT_INDEX와 MASTER_REPORT에 상위 산출물/실무 문서의 역할과 링크를 연결한다.
- 상세 감사는 증거 보존용으로 유지하되, 검증된 결론은 제1권·제2권·MASTER_REPORT와 관련 매트릭스/SOP로 통합한다.
- 문서 지도를 만들었다는 사실은 과거 모든 감사 결과의 본문 통합이 완료되었다는 뜻이 아니다. 기존 제1권·제2권과 ledger 사이의 반영 여부를 별도 대조하고 누락을 채우는 작업이 남아 있다.

### 이후 강제 실행 규칙
1. 새 문서를 만들기 전에 기존 정본에 통합할 수 있는지 먼저 검토한다.
2. 독립 문서가 필요한 경우 목적·독자·상위 문서·정본 여부를 명시한다.
3. 매 감사 배치 종료 시 발견한 정정 사항을 claim ledger, MASTER_REPORT, 해당 권/매뉴얼/매트릭스에 반영하거나, 미반영 사유와 다음 반영 작업을 기록한다.
4. MASTER_REPORT_INDEX와 문서 지도는 문서 생성·이동·폐기 때 함께 갱신한다.
5. 매 세션마다 사용자의 최신 의도와 행동강령이 현행 문서에 반영되었는지 확인한다.


## 2026-11-13 추가 진행 — 감사 정정의 상위 보고서 통합 시작

- 문서 지도 생성 후 단순 링크 정리에서 멈추지 않고 제1권·제2권의 기존 내용을 다시 읽어 #43–#47 감사에서 확인된 분류·접근통제 오류와 중복 위험을 점검했다.
- 제1권 CRA compliance report에 다음을 반영했다.
  - Annex III Class I category 14(보안 관련 기능이 있는 MCU)와 Class II category 4(tamper-resistant MCU), 완제품 서보 드라이브 분류를 분리.
  - MCU 통합만으로 완제품이 자동 Class I/II가 되지 않음을 명시.
  - Article 32가 적합성 평가 조항이고 Article 24가 아니라는 점을 명시.
  - Annex I Part I point 2(d) 접근통제 법적 요구와 RBAC/MFA/least privilege 등 위험기반 구현 후보를 분리하고 매트릭스 링크 추가.
  - Article 14 운영 정본으로 PSIRT SOP 링크 연결.
- 제2권 구현 계획에 제품 분류 매트릭스, PSIRT SOP, HW 아키텍처, 통합 추적성 매트릭스의 정본 링크와 역할 구분을 추가했다.
- MASTER_REPORT의 MCU category 14 문구를 “MCU 자체의 기술 설명 및 별도 시장 제공 여부”와 “완제품 분류”가 서로 다른 판단임을 명확히 했다.
- 이번 내용 반영은 #43–#47 감사 정정의 관련 상위 문서 연결/명확화다. 과거 모든 archive 감사 항목을 제1권·제2권 전체에 전수 반영한 것은 아니다. 다음 P0에서 Claim Evidence Ledger와 정정 대장을 상위 보고서 전체와 대조한다.


## 2026-11-13 진행 업데이트 — main reports #48–#52 및 보고서 통합

- main 최신 HEAD를 재조회: aaded0f4d0b84a1891b5801a6048c4de92511822 (report #107); state count 107; history 1,382 entries. state count는 당일 카운터이며 누적 파일 수로 쓰지 않는다.
- #48–#52 원본 5개를 날짜+count+경로로 매핑하고 archive blob SHA를 기록했다.
- [#48–#52 수동 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md): 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- 핵심 정정: Article 14(8) machine-readable notification은 actively exploited vulnerability/severe incident 사용자 통지에 한정되고 “where appropriate” 조건이 있다. Annex I Part II(5)/(6)은 CVD/contact address, Part II(4)는 fixed vulnerability disclosure, Part II(7)은 secure update distribution, Part II(8)은 원칙적 무상 업데이트다. Article 13(6)은 제조사가 통합 구성요소 취약점을 구성요소 제조/유지 주체에 보고하는 방향이다.
- 누적 #8–#52: 45건, 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED; 비무작위 연속 표본.
- 이번 배치의 주요 결론은 Claim Evidence Ledger, 제1권, 제2권, PSIRT SOP 및 MASTER_REPORT에 연결·반영했다.
- 다음 감사 시작점 #53. main은 계속 read-only, 제품별 적용성은 UNVERIFIED, 실제 DUT 시험은 NOT_RUN.


## 2026-11-13 최신 Git 기준선 보정 — report #107 및 통합 작업 HEAD

- main HEAD: aaded0f4d0b84a1891b5801a6048c4de92511822 (Auto-archive report #107).
- main state.json: date 2026-11-13, count 107. 이는 당일 카운터이며 누적 자료 수가 아니다.
- main history.json: 1,382 entries. Recursive archive tree count는 이번 보정에서 조회하지 않았으므로 1,382개 archive 파일이라고 단정하지 않는다.
- cra-project-foundation history.json: 990 entries. state.json은 date 2026-11-12, count 3; 이 값은 일일 카운터다. 마지막 strict archive audit가 확인한 990/990 정합성 결과는 이전 검증 기준이며 이번 문서 전용 commit 후 새 strict audit를 실행한 것은 아니다.
- 이 기준선 조회 시 작업 HEAD는 ad7b2732b5a554842772be8cabb23ba29d270ae4였다. 이후 START_HERE 및 MASTER_REPORT 문서 정정 commit f42fa408858f8160fb5a379a052294c36cc0465d, 91372b411ccb037602c59e4a88791119b04a7a73가 추가되었으므로 현재 tip은 다음 세션 시작 시 동적으로 다시 조회한다. 기준선 시점 main 비교는 diverged, ahead 690 / behind 398, merge base b425b6db591e34abe003522157cf97ecf2240d9f.
- 최신 HEAD 문서 변경은 docs/SESSION_LOG에 한정된 마지막 commit이며, 전체 문서 변경은 그 직전 연속 docs-only commits에 기록되어 있다. main merge/rebase/sync는 수행하지 않았다.
- exact HEAD CI run/status는 별도 조회 결과가 없는 한 PASS로 기록하지 않는다.


## 2026-11-13 사용자 의도 업데이트 — 한국어 최종 산출물

- 사용자가 명시한 기본 언어는 한국어다. 최종 보고서·매뉴얼·SOP·설계·시험 자료의 설명과 결론을 한국어로 작성한다.
- 법령/표준의 공식 명칭, 조항 번호, 제조사 문서명, 부품번호, 정확한 원문 인용 및 고정 상태 코드는 영어 원문을 유지할 수 있다.
- 사용자는 검증·수정된 조사 결과를 실제 보고서와 매뉴얼에 통합하는 것을 중요하게 본다. 문서가 과도하게 분리되어 최종 내용을 찾기 어려워지지 않도록 기존 정본에 통합하고, 독립 목적이 있는 문서만 별도로 유지한다.
- 전체 문서 구성과 링크는 CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md, 발행 문서 목록은 MASTER_REPORT_INDEX.md가 담당한다.
- #8–#52 정정의 상위 문서 전수 대조는 미완료이며, 다음 P0 작업이다.


## 2026-11-13 — #13–#42 공통 정정 통합

- #13–#42 감사에서 반복 확인한 Article 11/13/14 혼동, Annex I Part I/II 혼합, Annex II/Annex VII 혼동, 지원기간·업데이트 가용성·무상 업데이트의 혼동, 제품 Class I/II 과장 및 설계 후보의 법적 의무화 오류를 법령 기준선 제2.3절에 통합했다.
- 제1권 제3장, 제2권, 요구사항 매트릭스와 문서 지도에 같은 기준의 상위 링크를 추가했다.
- 다음 P0는 감사 #8–#52와 Claim Evidence Ledger의 누락 레코드/중복 ID/상태 차이를 확인하고, #8–#12의 원본 감사 문서 및 주장별 연결 상태를 복원하는 것이다.


## 2026-11-13 — #13–#42 공통 정정 통합

- #13–#42 감사에서 반복 확인한 Article 11/13/14 혼동, Annex I Part I/II 혼합, Annex II/Annex VII 혼동, 지원기간·업데이트 가용성·무상 업데이트의 혼동, 제품 Class I/II 과장 및 설계 후보의 법적 의무화 오류를 법령 기준선 제2.3절에 통합했다.
- 제1권 제3장, 제2권, 요구사항 매트릭스와 문서 지도에 같은 기준의 상위 링크를 추가했다.
- 다음 P0는 감사 #8–#52와 Claim Evidence Ledger의 누락 레코드/중복 ID/상태 차이를 확인하고, #8–#12의 원본 감사 문서 및 주장별 연결 상태를 복원하는 것이다.


## 2026-11-13 — #8–#52 Ledger 원본 추적 연결 완료(파일 중심)

- #8–#52 총 45개 보고서의 2026-11-13 날짜, 원본 archive 경로, blob SHA, 파일 판정, 중심 정정 요약을 Claim Evidence Ledger에 날짜 포함 ID로 등록했다.
- #8–#12 상세 감사 파일을 다시 찾아 원본 SHA와 판정을 확인했다. 다섯 건 모두 CONFLICT, 직접 인용 재사용 0/5.
- #13–#52 40건은 CONFLICT 35 / PARTIALLY_VERIFIED 5 / VERIFIED 0. 전체 #8–#52는 CONFLICT 40 / PARTIALLY_VERIFIED 5 / VERIFIED 0.
- 이 연결은 파일별 중심 주장 추적이다. 보고서 내 모든 개별 주장과 인용 블록의 원자적 분해/정정 링크는 아직 미완료다.


## 2026-11-13 — main reports #53–#57 감사 및 정본 통합

- main 최신 관찰: HEAD `8ebc3cdc361a1b694e4ad18b5d85cc6dec5d1f35` (Auto-archive report #112), state.json count 112, history.json 1,387 entries. state count는 당일 카운터이며 archive 파일 수가 아니다.
- #53–#57 감사: 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/5.
- #8–#47 재검토 정정: #38은 Annex I Part I(2)(m) 데이터·설정 영구 제거 기능 결과 요구를 누락했던 점을 바로잡아 CONFLICT에서 PARTIALLY_VERIFIED로 변경. #8–#47 누계는 36 CONFLICT / 4 PARTIALLY_VERIFIED.
- #8–#52 누계: 45건, 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED.
- #8–#57 누계: 50건, 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/50. 비무작위 연속 표본.
- Claim Evidence Ledger에 #53–#57 날짜 포함 원본 경로·SHA·판정·중심 정정 claim ID 5개를 추가했다.
- 제1권·제2권·사용자 보안정보 체크리스트·요구사항 추적성 매트릭스·CRA 법령 기준선에 Part I 2(m), Annex II 8(d), Article 13(19), Article 14/69(3) 정정을 반영했다.
- 다음 감사 시작점 #58. main HEAD/state/history를 배치 시작 시 다시 조회한다.


## 2026-11-13 최종 기준선 — main #112 / audit #57 완료

- main 최신 관찰 HEAD: `8ebc3cdc361a1b694e4ad18b5d85cc6dec5d1f35` (report #112); state count 112; history 1,387 entries. archive tree count는 재조회하지 않았다.
- 작업 브랜치 history.json 990 entries, state.json 2026-11-12/count 3.
- main과 작업 브랜치: diverged, ahead 783 / behind 403, merge base `b425b6db591e34abe003522157cf97ecf2240d9f`. main은 read-only, merge/rebase/sync 금지.
- 직전 작업 tip `45be8357c676a1c15e672d4b381474943211230e`는 branch와 identical 확인. 이 commit의 workflow runs 0, combined statuses 0; CI 미실행/미확인.
- 보호 파일 7개 SHA 변경 없음.
- 최신 감사: #53–#57 완료, 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED.
- #38의 Annex I Part I(2)(m) 누락을 후속 검토에서 발견해 PARTIALLY_VERIFIED로 정정. 누적 #8–#57: 50건, 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/50.
- 다음 작업: #8–#57 원자 주장·인용 분해와 상위 문서 전수 대조. 이후 main-only #58–#62 감사.


## #8–#57 원본 Claim ID 확장 후 기준선 갱신

- Claim Evidence Ledger의 제31절 제목/범위를 #13–#57로 확장하고, #53–#57 다섯 건의 원본·SHA·파일 중심 claim ID를 확인했다.
- #8–#57 총 50개 보고서에 날짜 포함 파일 중심 Claim ID 50개를 연결했다. 개별 하위 주장·인용 블록의 원자 분해는 별도 미완료.
- Ledger 확장 commit: `e1b9ee24f1fe185a0fe8e9945a59836ba74246c7`. 이 commit은 docs/CLAIM_EVIDENCE_LEDGER.md만 변경했고 exact HEAD CI runs/status는 0/0으로 미실행·미확인.
- main #112와 비교: diverged, ahead 788 / behind 403, merge base `b425b6db591e34abe003522157cf97ecf2240d9f`.
- 이 continuity board 갱신이 다음 docs-only commit이므로 새 exact HEAD/CI는 갱신 직후 다시 확인한다.

## 2026-11-13 최신 연속성 갱신 — main #118 / audit #58–#62

- main HEAD \`75add8711d0254da7dea1766bb42f80fc04d36ee\` (Auto-archive #118); state count 118; history 1,393 entries. archive tree count는 별도 확인하지 않았다.
- 작업 브랜치 \`cra-project-foundation\`; main과 diverged, work ahead 791 / behind 409; merge base \`b425b6db591e34abe003522157cf97ecf2240d9f\`. main read-only, merge/rebase/sync 금지.
- #58–#62 감사: 5 PARTIALLY_VERIFIED / 0 CONFLICT / 0 VERIFIED; direct quote reuse 0/5.
- 누적 #8–#62: 55건, 40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/55. 비무작위 연속 표본.
- CVD Part II(5), contact address Part II(6), free updates Part II(8), Article14 active exploitation/severe incident two-track reporting, 24h/72h/14-day/1-month deadlines, logging Part I 2(l) 정정을 제1권/제2권/SOP/매트릭스에 반영.
- 원자 Claim ID 20개를 Ledger에 추가. 제품별 적용성 UNVERIFIED, 실제 DUT 시험 NOT_RUN.
- 다음 P0: #8–#57 원자 주장·인용 분해와 상위 문서 전수 대조. 그 후 main-only #63–#67.
- 이번 작업은 문서 전용이다. exact final documentation HEAD의 CI/Actions 결과는 별도 확인 전까지 미확인으로 유지한다.

## 사후 기준선 — main report #119 (2026-11-13)

- #58–#62 감사 시점 main 기준선은 report #118 / history 1,393 entries였다.
- 후속 자동 아카이브로 main이 report #119까지 진행: HEAD \`6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0\`, state count 119, history 1,394 entries.
- #119는 아직 감사하지 않았다. 다음 감사 시작점은 #63–#67이며, 배치 시작 시 main HEAD/state/history를 다시 조회한다.
- main/work branch는 diverged. ahead/behind는 변경되므로 매 세션 동적으로 확인하고 merge/rebase/sync하지 않는다.

## 2026-11-13 P0 진행 — #8–#12 원자 Claim ID 분해

- #8–#12 원본과 blob SHA를 main에서 다시 대조했고, 기존 파일 단위 판정 5 CONFLICT / direct quote reuse 0/5를 유지했다.
- Claim Evidence Ledger에 31개 원자 Claim ID를 추가했다. 일부 개별 법령 원칙은 VERIFIED이나 파일 전체 판정과 제품 적합성으로 확대하지 않는다.
- 핵심 법령 구조: secure-by-default Part I 2(b), access control 2(d), attack surface 2(j); Class II는 Annex III; Part II는 vulnerability handling.
- 다음 작업은 #13–#17 원자 주장 분해 후 #18–#57 순차 분해 및 정본 문서 교차 대조.
