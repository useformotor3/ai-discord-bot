# CRA 프로젝트 — AI 연속성·실행 현황판

- 문서 ID: CRA-OPS-CONTINUITY-001
- 기준일: 2026-11-13
- 기준 작업 브랜치: `cra-project-foundation`
- 마지막 확인 작업 HEAD: `81d58716071fdb7debe5f780707d3b0d7870a902`
- 마지막 확인 main HEAD: `4452662e6cba0bb81c6efb4b309b30f4733d8f71` (Auto-archive: Research report #91)
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
| main 최신 관찰 | HEAD `4452662e6cba0bb81c6efb4b309b30f4733d8f71`, report #91 |
| main 아카이브 | 1,366개 파일 / history 1,366개 / 고유 경로 1,366개 (2026-11-13 조회) |
| 작업 브랜치 아카이브 | 최근 strict audit 기준 990개 / history 990개 정합 |
| main과 작업 브랜치 | diverged, 작업 브랜치 ahead 653 / behind 382. 수치 재확인 전에는 고정 사실로 재사용 금지 |
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

### P0 — 진행 중
1. **main archive 보고서 #33 이후 최신까지 감사 대기열 복원 및 우선순위화.** 현재 main tip은 #91이며, 기존 queue가 #27에서 멈춰 있어 #28–#91 범위의 추적성을 최신화해야 한다.
2. 연속 보고서 #28–#32의 원문/인용 오류를 별도 감사 보고서로 기록하고 queue/claim ledger에 연결.
3. 법령 오류가 반복된 영역(Article 13(8)/(9), Article 14, Annex I Part II(2)/(5)–(8), Annex II, Annex III 분류)을 통합 정정표로 제1권 보고서에 반영.
4. 기존 제1권/제2권/아키텍처/추적성 매트릭스 사이의 requirement ID와 근거 링크 정합성 확인.

### P1 — 이어서 진행
5. main archive의 최신 조사물 중 반복이 적은 실질 주장만 추출해 claim-level audit. “새 주제” 프롬프트 문구를 그대로 신뢰하지 말고 실제 본문 중복을 판단.
6. ST AN5156 Rev14 등 공식 제조사 자료를 source register와 claim ledger에 연결. 최신 revision 인덱스만 확인된 자료는 본문을 확인할 때까지 인용 금지.
7. 실제 ST MCU 부품번호가 없으므로 일반 ST 기능 설명과 부품별 적용성 결론을 분리.
8. 제품 입력자료가 확보되면 Product Boundary & CRA Applicability Decision Record 작성.
9. PSIRT SOP에 역할/연락처/T0 기록 필드를 보완하고 tabletop 시나리오를 작성하되, 실행은 실제 조직 승인 후.

### P2 — 보류/승인 필요
10. E3 real official source fetch: 별도 승인 전 실행 금지.
11. main.py, production workflow, Gemini V2 prompt/contract, production integration: 별도 change proposal 및 명시적 승인 전 수정 금지.
12. main 브랜치 merge/rebase/sync: 명시적 승인 전 금지.
13. 유료 서비스·유료 API·외부 배포: 사용자 승인 없이 실행 금지.

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
