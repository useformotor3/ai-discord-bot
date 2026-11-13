# CRA 프로젝트 — AI 작업 시작점 (필수)

> 이 파일은 새 대화/새 작업 세션의 첫 진입점이다. AI는 작업 전 반드시 이 파일과 연결된 기준 문서를 읽어야 한다.

## 프로젝트 식별
- 저장소: https://github.com/useformotor3/ai-discord-bot
- 현재 프로젝트: CRA를 서보 드라이브 개발에 적용하기 위한 공개 근거 기반 지식·설계·검증·보고서
- 기본 작업 브랜치: cra-project-foundation
- 범위: CRA 중심. SIL 3 벤치마킹은 범위 밖.
- 우선 반도체: ST MCU. TI는 비교·참고.
- 독자: CRA를 모르는 서보 드라이브 개발자.
- 운영 원칙: Public 저장소 유지, 공개 자료만 저장, 비용 0원 우선, 유료 전환 금지.

## 전체 문서 지도
- [CRA 문서 구조·전체 목차·링크 안내](docs/CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md) — 문서 역할, 정본 위치, 전체 링크, 감사자료와 최종 보고서의 연결 구조.

## 신규 세션 필수 읽기 순서
0. [AI 연속성·실행 현황판](docs/AI_CONTINUITY_BOARD.md) — 목표·현재 HEAD·완료/실패/미완료·다음 행동의 최우선 기준
1. [AI 행동강령](docs/AI_RULEBOOK.md) — 작업 전 필수 절차와 품질 기준
2. [프로젝트 상황판](docs/PROJECT_STATUS.md) — 현재 사실·진행 상태·위험
3. [마스터 계획](docs/MASTER_PLAN.md) — 우선순위와 완료 조건
4. [문서 구조·전체 링크 지도](docs/CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md) — 문서 역할과 정본 위치
5. [마스터 보고서 인덱스](docs/MASTER_REPORT_INDEX.md) — 발행 문서 카탈로그
6. [통합 마스터 보고서](docs/MASTER_REPORT.md) — 독자용 통합 본문
7. [지식 인덱스](docs/KNOWLEDGE_INDEX.md) — 근거·검증 상태
8. [최근 세션 기록](SESSION_LOG/) — 직전 결정·성공·실패·다음 작업
9. 작업에 관련된 감사·법령 기준선·제조사 자료를 추가로 확인한다.

필수 문서를 읽지 못하면 이전 대화 기억으로 내용을 채우지 않는다. 확인 불가 상태를 명시하고 저장소를 다시 확인하거나 사용자에게 필요한 정보를 요청한다.

## 작업 루프
**읽기 → 현재 저장소와 대조 → 근거 확인 → 계획 → 변경 → 테스트/재확인 → 기록 → 상황판 갱신**

- 작업 전: 현재 브랜치, 최근 커밋, 대상 파일 원문을 확인한다.
- 작업 중: 주장과 근거를 연결하고 검증 상태를 구분한다.
- 작업 후: 변경 diff/저장 파일을 다시 읽고, 링크·수치·체크리스트를 검증한다.
- 세션 종료: SESSION_LOG, PROJECT_STATUS, MASTER_PLAN을 실제 결과에 맞게 갱신한다.
- 실패도 반드시 기록하고 재발 방지 규칙을 추가한다.

## 핵심 문서
- [행동강령](docs/AI_RULEBOOK.md)
- [상황판](docs/PROJECT_STATUS.md)
- [계획서](docs/MASTER_PLAN.md)
- [근거 인덱스](docs/KNOWLEDGE_INDEX.md)
- [통합 보고서](docs/MASTER_REPORT.md)
- [초기 감사](docs/INITIAL_AUDIT.md)
- [CRA 법령 기준선](docs/CRA_LEGAL_BASELINE.md)
- [저장소 브랜치/이력 정합성 감사](docs/REPOSITORY_RECONCILIATION.md)

## 현재 기준선 (2026-11-13 확인)
- 작업 브랜치 cra-project-foundation의 현재 HEAD와 CI는 AI_CONTINUITY_BOARD 및 PROJECT_STATUS에서 세션마다 실시간 재확인한다.
- 작업 브랜치 history.json은 990 entries. 마지막으로 확인된 strict archive audit는 archive/history 990/990 정합성을 통과했으나, 최신 문서 전용 변경 HEAD에서 새 strict audit/CI를 실행한 것은 아니다.
- main 최신 관찰: report #107, HEAD aaded0f4d0b84a1891b5801a6048c4de92511822; history.json 1,382 entries, state.json count 107(당일 카운터). archive tree 파일 수는 이번 확인에서 재검증하지 않았다.
- main과 작업 브랜치는 diverged다. 정확한 ahead/behind 수치는 세션마다 AI_CONTINUITY_BOARD에서 재조회한다. main merge/rebase/sync 금지.
- main.py, production run.yml, Gemini V2 prompt, contracts, schemas, evidence bundle은 별도 승인 전 수정 금지.
- 최신 작업 HEAD의 CI run/status가 확인되지 않으면 PASS라고 기록하지 않는다.

## 최우선 다음 작업 (2026-11-13 최신)
1. #8–#52 감사 결과와 Claim Evidence Ledger를 제1권·제2권·PSIRT SOP·법령 기준선·요구사항/통합 추적성 매트릭스에 전수 대조한다.
2. 불일치·누락된 법령 조항, 예외, 상태만 기존 정본에 통합하고 문서 분리를 최소화한다.
3. 한국어가 아닌 영문 중심의 최종 실무 문서는 독자와 용도를 확인해 한국어 정본으로 전환한다.
4. main reports #53–#57을 원문 SHA와 공식 법령으로 감사하고 같은 배치에서 상위 문서 통합까지 수행한다.
5. 제품 SKU, 제품 경계, 의도된 용도, 실제 ST MCU 주문 코드가 확보되면 제품별 분류·설계·ST/TI 비교를 갱신한다.
6. main.py/Gemini 명령 구조/production workflow 변경은 별도 승인 전 수정하지 않는다.


## 최신 작업 업데이트 (2026-11-12)
- 추가 20개 고위험 조사 아카이브 수동 감사: [ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md), 14 CONFLICT / 6 PARTIALLY_VERIFIED.
- 초기 5개 + 추가 9개 + 추가 20개 누계 34개, 25 CONFLICT / 9 PARTIALLY_VERIFIED. 비무작위 위험 표본이므로 전체 오류율로 일반화하지 않는다.
- 다음 우선순위: (1) 남은 위험 플래그 후보를 원문 대조, (2) 기존 990개 출처 canonical URL/문서 버전/조항 위치 복원, (3) 주장별 정정 ledger 구축, (4) ST/TI 공식 기술자료 비교 확장.
- 기존 research_archive 원본, main.py, Gemini prompt 및 운영 run.yml은 수정하지 않았다. main 병합도 하지 않았다.


## 제조사 MCU 자료/주장 대장 업데이트 (2026-11-12)
- [제조사 보안 자료 레지스터](docs/MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md): ST/TI 공식 자료 버전 및 기능별 비교, 제품별 한계, 시험 큐.
- [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md): 기술 주장과 source URL/버전/원문 위치/제품 범위/검증 상태 연결.
- TI MSPM0G3529-Q1은 비교 예시 부품이며 실제 프로젝트 선택 부품이 아니다. ST 실제 MCU 주문 코드가 없으므로 ST 부품별 기능은 UNVERIFIED.
- TI SLAAE29 RevB 및 G-Series TRM RevF가 공식 자료 인덱스에서 더 최신으로 확인되어 다음 세션에서 본문/적용성 대조가 필요하다.


## 2026-11-12 추가 업데이트 — 하드웨어 참조 설계
- [서보 드라이브 CRA 보안 하드웨어 아키텍처](docs/SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md) 생성. 제품별 사실이 미확정이므로 설계 초안이며 적용성 UNVERIFIED.
- TI G-Series TRM Rev F (2026-11-05)는 공식 기술자료 인덱스에서 확인했으나 본문은 열람 실패. SLAAE29 Rev B 본문도 미확보. Rev A/데이터시트에서 직접 확인된 범위와 최신판 인덱스 메타데이터를 혼동하지 않는다.


## 2026-11-12 추가 업데이트 — 아카이브 표본 정정 대장
- [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](docs/ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md)에 34개 고유 원본의 SHA-1, 원문 행 위치, 주장 요약, CRA 정정 룰, 판정 상태를 연결.
- 감사 ID 35개 중 A-013/B-006은 동일 원본 파일/SHA이므로 중복 1개 제거. 고유 파일 기준 25 CONFLICT / 9 PARTIALLY_VERIFIED.
- 34개는 비무작위 표본이며 990개 전체 오류율이 아니다. 원본 archive는 변경하지 않음.


## 2026-11-12 추가 업데이트 — 법령 인용문 단위 감사
- [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](docs/ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md)에 기존 34개 고유 표본의 법령 인용 블록, 원본 경로·행 위치, 판정 및 정정 조항을 연결.
- A-013/B-006 중복은 한 건으로 처리. 일부 SBOM/Article 31 문구는 원문과 부합하거나 생략 인용에 해당하지만, 상당수는 paraphrase를 직접 인용처럼 표시했거나 조항을 합성·오기함.
- EUR-Lex Regulation (EU) 2024/2847의 Article 13(8)/(9), Article 14, Article 31/32, Annex I Part I/II, Annex II/III/VII/VIII를 직접 대조.
- 기존 원본 archive는 수정하지 않았다. 감사는 34개 표본에 한정되며 990개 전수검증이 아니다.


## 필수 검증 절차
- [검증 운영 프로토콜](docs/VERIFICATION_PROTOCOL.md)을 모든 조사·보고서·설계 작업에 적용한다.
- 빠른 진행은 검색량을 늘리는 것이 아니라 P0 위험 항목부터 원문 확인 → 별도 재검증 → 반증 확인 → 제품 적용성 → 설계/시험 증거로 연결하는 방식으로 한다.
- 같은 AI의 반복 답변은 독립 더블체크가 아니다. Pass A/B/C 기록이 없으면 VERIFIED로 승격하지 않는다.


## Pass B/C 재검증 진행
- 34개 표본의 재검증은 별도 2차 절차로 진행한다. 첫 배치 A-001–A-008 결과: [ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md](docs/ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md).
- Batch 01은 8개 파일 중 법령 직접 인용/조항 연결이 완전히 VERIFIED된 파일은 0개. 일부 정확한 문구는 있었으나 잘못된 위치·합성 인용이 확인됐다.
- 같은 AI 세션의 별도 재검증이며 독립 제3자 법률 검토가 아님을 명시한다.


## Pass B/C Batch 02
- [ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md](docs/ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md): A-009–A-015 및 B-001–B-002, 8개 파일 추가 재검증.
- 8개 모두 Raw Text Quote를 현행 법령 직접 인용으로 재사용 불가. 지원기간 문구의 shorter/longer 역전, Article 14 신고 범위 확대, Annex Part I/II 혼합이 반복됨.


## Pass B/C Batch 03
- [ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md](docs/ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md): B-003–B-010 8개 파일 재검증.
- B-009 secure-by-default 문구만 현행 Annex I Part I(2)(b)와 핵심 취지가 일치하나 원문 위치/표현을 정정해야 한다. B-010은 Article 24/32 혼동 및 서보 드라이브 Class II 근거 없는 단정이 확인됐다.


## 34개 표본 Pass B/C 최종 결과
- [ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md](docs/ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md): 34개 고유 원본 재검증 최종 요약.
- 파일 단위 결과: VERIFIED 0 / PARTIALLY_VERIFIED 6 / REJECTED 28. 34개 위험 기반 표본 결과이며 전체 990개 오류율이 아님.
- 동일 AI 세션의 별도 원문 재확인 절차이며 독립 제3자 법률 검토는 아님.


## 다음 설계 산출물
- [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](docs/CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md): 검증된 법령 요구를 HW/FW/시험/객관적 증거로 연결하는 추적성 매트릭스 초안.
- 제품 SKU와 실제 ST MCU 부품번호가 없으므로 모든 제품별 적용 및 시험 결과는 UNVERIFIED로 유지.


## 2026-11-12 추가 — 위협 모델 및 시험·증거 대장
- [서보 드라이브 CRA 위협 모델](docs/THREAT_MODEL_SERVO_DRIVE_CRA.md): 자산 10종, 공격자 6유형, 신뢰 경계 8개, 위협 시나리오 18개와 통제 후보를 연결.
- [보안 시험·증거 대장](docs/SECURITY_TEST_EVIDENCE_REGISTER.md): 업데이트/네트워크/명령/가용성/서비스/디버그/NVM/키/센서/운영 시험 40여 개의 ID, 기대 결과, 증거 메타데이터 규칙을 정의.
- 모든 시험은 NOT_RUN이며 실제 제품 시험을 수행한 것이 아니다. 실제 제품 입력·수치형 합격 기준이 확보되기 전까지 제품별 위험/적용성은 UNVERIFIED.


## 2026-11-12 통합 추적성 및 정기 점검
- [통합 CRA 요구사항–위협–HW/FW–시험–증거 매트릭스](docs/CRA_INTEGRATED_TRACEABILITY_MATRIX.md): TR-01..TR-20 end-to-end trace ID와 P0/P1 실행 백로그.
- [European Commission CRA Guidance 검토](docs/CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md): C(2026) 5252, 2026-07-27 공식 게시 사실 및 프로젝트 영향 검토. Annex 본문 단락별 검증은 미완료.
- 제조사 자료 인덱스 변경: TI SLAAE29 Rev B 및 G-Series TRM Rev F는 공식 인덱스 메타데이터만 확인. 본문 내용은 확인 전 인용 금지. ST AN5156 Rev14/June 2026 메타데이터 재확인.
- 매주 월요일 09:00(Asia/Seoul) 공식 CRA/ST/TI 자료 변경 점검 자동화가 등록됨. 변경 시 공식 원문과 revision diff를 확인하고 cra-project-foundation 브랜치에만 반영 후보를 기록한다.

## 2026-11-12 추가 — 추적성 검사 및 main-only report #35 감사

- CRA_INTEGRATED_TRACEABILITY_MATRIX: TR-01..TR-20, 중복 0.
- THREAT_MODEL: AST-01..10 10개, TH-01..18 18개, 중복 0.
- SECURITY_TEST_EVIDENCE_REGISTER: TST-* 45개, 중복 0. 통합 매트릭스의 단일 ID 및 번호 범위 참조를 전개해 검사한 결과 45개 모두 시험 대장에 존재. 실제 시험은 모두 NOT_RUN.
- main-only 자동 생성 report #35는 법령 원문과 충돌하는 Secure Boot/하드웨어 Root of Trust 의무 단정 및 잘못된 Annex I 직접 인용을 포함. 작업 브랜치 감사 문서 [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md)에 기록. main 원본은 수정하지 않음.
- TI SLAAE29 Rev B 본문을 TI 공식 HTML 뷰어에서 직접 확인. CSC secure boot flow, KEYSTORE, AESADV/TRNG 설명 및 revision history를 확인했으나, Rev B 지원 부품 목록에 MSPM0G3529-Q1은 포함되지 않음. G3529-Q1에 Rev B 플랫폼 설명을 직접 적용하지 않음.
- Commission C(2026) 5252 Annex PDF는 공식 다운로드 링크에서 다시 시도했으나 도구의 Unicode decoding error로 열지 못함. 페이지/문단 단위 검증은 여전히 PENDING.
- main.py, Gemini prompt, production run.yml, main branch는 수정하지 않음.

## 2026-11-12 추가 — main-only report #36 감사

- main의 자동 생성 report #36도 감사했다. Article 14를 무상 업데이트와 혼동, Annex I Part I(2)(b),(c),(g) 오기, Secure Boot/Measured Boot/TPM을 보편 의무로 단정, 법령 제목의 개정 법령 번호 오기가 확인됐다.
- 감사 기록: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md). 파일 판정 CONFLICT, 직접 인용 블록 REJECTED. main 원본 수정 없음.

## 2026-11-12 추가 — main-only 보고서 #37–#39

- main-only 자동 생성 보고서 #37–#39 3건을 공식 EUR-Lex와 대조, 모두 CONFLICT. Article 13(8) 지원기간 / Annex I Part II(8) 무상 업데이트 / CVD Part II(5) / contact Part II(6)를 분리. Annex I Part II (a)–(d) 인용 및 Part I(2)(b)/(c) 인용 오류를 기록.
- 상세 감사: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md). main 원본은 불변 유지.

## 2026-11-12 추가 — 하드웨어 인터페이스 설계 계약

- 하드웨어 참조 아키텍처에 DEC-01..DEC-10 선택 매트릭스, G-01..G-06 설계 동결 게이트, IF-01..IF-09 인터페이스 계약 및 회로도 리뷰 체크리스트를 추가했다.
- 제품별 회로/전압/절연/ESD/타이밍/핀맵/부품은 입력이 없어 미확정. 기존 시험 대장과의 ID 참조는 재검사했고 누락 참조 0.
- main-only 보고서 #37–#39 법령 인용 감사는 [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md)에 기록했다.


## 2026-11-12 추가 — main-only reports #40–#55 감사

- [main reports #40–#55 상세 감사](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md): 파일 단위 PARTIALLY_VERIFIED 2 / CONFLICT 14, 완전 VERIFIED 0.
- 주요 교정: Article 13(8)=지원기간, Article 14=적극 악용 취약점/심각한 사고 신고, Annex I Part II(7)=안전한 업데이트 배포, Part II(8)=무상 보안 업데이트, Annex II 8(d)=안전한 폐기 안내.
- 특정 서명 알고리즘, dual-bank, hot-patch, zero-downtime, STO/SIL 분리 등을 CRA의 보편적 직접 의무로 인용하지 않는다. 제품 위험평가·기능안전 설계 선택으로 분리한다.
- 원본 main archive는 수정하지 않았고 작업 브랜치에 감사 문서/claim ledger만 추가했다.


## 2026-11-12 추가 — main reports #56–#59 감사

- [상세 감사 #56–#59](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_56_59_2026-11-12.md): #56 CONFLICT, #57 PARTIALLY_VERIFIED, #58 PARTIALLY_VERIFIED, #59 CONFLICT.
- Article 14 신고는 actively exploited vulnerability와 severe incident를 분리하고 최종보고 기한도 각각 14일/1개월로 관리한다.
- CVD/contact 근거는 Annex I Part II(5),(6); user-facing single point of contact는 Annex II point 2.
- Secure-by-default, access control, attack-surface limitation은 각각 Annex I Part I(2)(b),(d),(j). 구체적인 포트 차단/최초 비밀번호 변경은 제품 위험평가에 따른 설계 선택으로 분리한다.
- 원본 main 파일은 수정하지 않는다.


## 2026-11-12 추가 — main-only reports #60–#78
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md): 19개 보고서 원문 대조, 6 PARTIALLY_VERIFIED / 13 CONFLICT / 0 VERIFIED. 이 배치의 Raw Text Quote는 직접 인용으로 재사용하지 않는다.
- main 최신 자동 생성 report는 #78로 갱신 확인. 이후 세션은 #79 이후 commit 여부부터 확인한다.
- Article 13(8), Article 14, Annex I Part I/II, Annex II의 조항 매핑을 새 감사 문서와 claim ledger에서 확인한다.


## 2026-11-12 추가 — main-only report #79
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md): Article 14 report #79 PARTIALLY_VERIFIED. 최신 main 자동 생성 보고서가 #79로 갱신됨.
- 다음 세션은 #80 이후 commit 존재 여부부터 확인하고, Article 14의 24h/72h/final deadline 구분을 유지한다.


## 2026-11-12 추가 — TI MSPM0G3529-Q1 기능안전 자료
- [TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md](docs/TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md): SFFS983A Rev A supported-device list에 MSPM0G3529-Q1이 포함됨.
- component-level systematic ASIL D / random-fault ASIL B는 SIL 3와 동등하지 않다. §4.3의 host actuator-disable, communication-loss monitoring, integrator diagnostics 및 QM IP 제한을 확인한다.
- 정확한 FMEDA 및 G3529-Q1 TRM Rev F 본문 확보는 미완료.


## 2026-11-12 추가 — main-only report #80
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md): secure-by-default/access/attack-surface themes partially verified; quote and universal implementation claims rejected.
- Latest main auto-archive report #80; next session starts by checking #81+.


## 2026-11-12 추가 — main-only 보고서 #81–#121 감사
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md): 41개 보고서 commit diff 검토, 33 CONFLICT / 8 PARTIALLY_VERIFIED / 0 VERIFIED.
- 41개 Raw Text Quote 블록은 모두 직접 인용으로 재사용 금지. Article 13(8) 지원기간, Annex I Part II(8) 무상 보안 업데이트, Article 14 신고 의무를 반복 혼동하고, 존재하지 않는 조항 번호/합성 인용과 Secure Boot·디지털 서명·무중단 업데이트의 보편적 의무 단정이 반복됨.
- 최신 main HEAD는 report #121, commit d0ba9802e4b7fead4192263d8ebd08f44a7c547e. 작업 브랜치에서만 감사 기록. main archive/history/state, main.py, Gemini prompt, run.yml 수정 및 merge/rebase/sync 없음.


## 2026-11-12 추가 — main-only report #122
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md): CONFLICT. Secure-by-default/access-control 주제는 관련성이 있으나 Annex I 번호 및 직접 인용이 잘못되었고, forced password change/RBAC/모든 미사용 포트 비활성화를 보편적 의무로 과장.
- main HEAD는 #122, commit 39d614a760aebc98ce16fb534ddd75ddbcc5c1e3. 원본 main archive는 수정하지 않음.


## 2026-11-12 추가 — main-only report #123
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md): CONFLICT. Article 13(7) 오인용, Article 13(18)/(19) 누락, Annex II Part I/II라는 잘못된 구조 및 합성 인용, 서보 드라이브 Class II 근거 없음.
- Annex II 사용자 문서 항목 1~9 및 8(a)~(f)를 상세 감사 문서에서 확인. SBOM 접근 위치는 제조사가 사용자에게 SBOM을 제공하기로 한 경우만 해당.
- 최신 main report #123, commit 1f9dc5e28d760ce5b47efda0e897a0a540d33ecb. 원본 main archive는 수정하지 않음.


## 2026-11-12 추가 — CRA Annex II 사용자 정보 템플릿
- [SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md](docs/SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md): Article 13(16)–(19), Annex II(1)–(9)를 서보 드라이브 사용자 지침서·보안 정보·증거 추적 항목으로 변환한 작업용 템플릿.
- 제품별 내용은 모두 미확정. “Digital Product Passport”는 법정 CRA 명칭이 아니며 Class II 분류는 Annex III 제품 기능 근거 없이 추정하지 않음.


## 2026-11-12 추가 — main-only report #124
- [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md): CONFLICT. 취약점 처리 요구사항은 Annex I Part II(1)–(8)이며 Part I Section 2가 아님. 직접 인용문은 합성/번호 오류. 서명 검증과 복구 아키텍처를 보편적 직접 의무로 과장.
- 올바른 구분: Part I(2)(c) 자동 업데이트 기본 설정(해당 시) 및 사용자 제어; Part II(5) CVD; (6) 연락/정보 공유; (7) 안전한 배포; (8) 지체 없는 무상 업데이트(맞춤형 제품의 business-user 합의 예외).
- main latest at discovery: #124, commit 17eebdb0af513ae2b6800e13d55b798d095631cc. 원본 main archive 수정 없음.


## 2026-11-12 추가 — Gemini 파이프라인 변경안 검토 대기
- main auto-archive reports #125–#128 감사: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md), 4건 모두 CONFLICT.
- Gemini 명령문 검토 초안: [PROPOSED_GEMINI_PROMPT_V2.md](docs/PROPOSED_GEMINI_PROMPT_V2.md).
- 1차 구현 제안 및 구체 diff/테스트/롤백: [CHANGE_PROPOSAL_MAIN_GEMINI.md](docs/CHANGE_PROPOSAL_MAIN_GEMINI.md) §14.
- 운영 main.py/prompt/parser/workflow는 승인 전 변경 금지. 현재는 제안 문서만 작업 브랜치에 기록.


## 최신 상태 — Gemini 파이프라인 1차 구현 (2026-11-12)
- 사용자 승인 후 `cra-project-foundation`에서 `main.py`, `cra_report_contract.py`, `prompts/CRA_RESEARCH_PROMPT_V2.txt`, `tests/test_cra_report_contract.py`를 구현했다.
- Gemini JSON 출력 계약/필수 필드 검증/직접 인용 금지/VERIFIED 승격 차단/모든 모델 실패 시 fail-closed를 적용.
- mock 테스트 13개를 격리 런타임에서 재현해 17/17 PASS, py_compile 3/3 PASS. 실제 API·네트워크 호출은 0회.
- GitHub Actions 실행 결과는 아직 확인되지 않아 CI PASS로 간주하지 않는다.
- 원문 수집·URL/조항/인용/법률 의미 검증은 미구현이므로 결과는 UNVERIFIED 초안이다.
- `.github/workflows/run.yml`, 모델 선택/순서, quota, Discord 전송, archive/history/state schema, main branch는 변경하지 않았다. merge/rebase/sync도 하지 않았다.
- 상세: [변경 제안 및 구현 결과](docs/CHANGE_PROPOSAL_MAIN_GEMINI.md), [상황판](docs/PROJECT_STATUS.md), [세션 로그](SESSION_LOG/2026-11-12.md).


## 2026-11-13 — CI 검증 및 다음 단계
- Gemini pipeline 1차 구현의 GitHub Actions run #43205954271에서 전체 26 tests PASS (CRA contract 17 포함), archive/history strict audit 990/990 및 불일치 0 확인.
- CI는 mock/fixture 검증이며 실제 Gemini API/운영 실행은 아님.
- 공식 Google SDK/model 문서 대조 완료: `response_json_schema` 지원, `gemini-3.5-flash-lite` stable + structured outputs. 실제 계정 API 접근은 미확인.
- 다음 단계 source evidence 설계: [PROPOSED_SOURCE_EVIDENCE_PIPELINE_V1.md](docs/PROPOSED_SOURCE_EVIDENCE_PIPELINE_V1.md).
- 현재는 설계 문서만 작성. fetcher/schema v3/prompt v3/main.py/workflow/실제 API 또는 네트워크 fetch는 별도 승인 전 구현·실행하지 않음.
- 최신 세션 로그: [SESSION_LOG/2026-11-13.md](SESSION_LOG/2026-11-13.md).


## 2026-11-13 — Source Evidence Phase A
- 사용자 승인 후 `source_evidence.py` 및 mock 테스트를 `cra-project-foundation`에 추가했다.
- 공식 registry의 source_id만 fetch할 수 있으며, HTTPS/host/DNS/redirect/MIME/size/timeout gate와 SHA-256 metadata를 제공한다.
- live network fetch 및 Gemini API 호출 없음. 생산 코드/프롬프트/workflow/main branch 미변경.
- 다음 세션은 최신 Actions 결과 및 source_evidence.py/test diff를 먼저 확인하고 Phase A 검증을 마무리한다. Phase B 이후는 별도 승인 필요.


### Phase A CI 결과 — 2026-11-13
- 최신 Phase A HEAD `21efe17ac151dcdb630abeed20769e4224ec3356`, Actions [#43330278366](https://github.com/useformotor3/ai-discord-bot/actions/runs/43330278366) success.
- 전체 45 tests PASS, archive/history strict audit 990/990 consistent.
- mock-only 결과다. 실제 공식 URL fetch/API 호출은 하지 않았다. DNS preflight에는 TOCTOU 한계가 있어 운영 적용 전 보완 필요.


## 2026-11-13 — Source Evidence Phase B
- 사용자 승인 후 작업 브랜치에 `source_extraction.py`와 mock tests 추가.
- HTML text/title, EUR-Lex XML structural locator candidates, HTML text locator candidates, PDF page-text adapter 구현.
- PDF pypdf optional lazy-load; workflow/dependency 변경 없음. OCR 미지원.
- locator는 후보/구조 정보이며 법률 해석 또는 quote validation 아님.
- Phase B CI 검증 대기. 실제 URL fetch/API/production integration 없음.


### Phase B CI 결과 — 2026-11-13
- Phase B HEAD `14666beefec6441df0a169aec81fa5c93d04fc22`, Actions [#43331128802](https://github.com/useformotor3/ai-discord-bot/actions/runs/43331128802) success.
- 전체 55 tests PASS; strict archive/history audit 990/990 consistent.
- main.py/prompt/contract/run workflow 미변경. 실제 공식 URL/PDF fetch는 미실시, PDF fake reader 테스트만 완료.


## 2026-11-13 — Daily main archive audit
- Latest checked main HEAD: `bd50257a80c0524402c70a7da420043ecfa0f490` (report #7).
- Since audited baseline #128, 167 new reports (#129–#288 and #1–#7) are registered in [docs/CRA_ARCHIVE_AUDIT_QUEUE.md](docs/CRA_ARCHIVE_AUDIT_QUEUE.md) on `cra-project-foundation` only.
- Next session: read queue and audit P0 items with Pass A/B/C; do not treat queue registration or official-source baseline pre-check as report verification.


## Phase C — Evidence Bundle v3 (2026-11-13)
- Added isolated Phase C implementation on `cra-project-foundation`: [Evidence Bundle](evidence_bundle.py), [v3 contract](cra_report_contract_v3.py), [JSON Schema](schemas/cra_research_v3.schema.json), [Gemini Prompt](prompts/CRA_RESEARCH_PROMPT_V3.txt).
- Bundle is in-memory only; no full source document is persisted. The builder verifies registry metadata, successful fetch, same-host HTTPS, MIME, byte count, raw/extracted hashes and bounded excerpt integrity.
- v3 claims reference existing `evidence_ids`; renderer obtains citation metadata/excerpts from the bundle. Unknown IDs and any VERIFIED/PARTIALLY_VERIFIED promotion are rejected.
- Added dedicated bundle and v3 contract tests. Exact code commit `6344b576db64438e9a2ebfe5acdcc74afeac479e` passed 79 tests and strict archive audit 990/990 (GitHub Actions #43338094337).
- No changes to v2, `main.py`, production workflow or `main` branch; no live URL/Gemini/API calls.


## 2026-11-13 — Report #7
- Added report #7 (`bd50257a80c0524402c70a7da420043ecfa0f490`, `research_archive/2026-11-13_003055.md`) to the queue. The queue now has 167 entries.
- Preliminary EUR-Lex note flags quote and Article-number mismatches; the file remains UNVERIFIED pending full Pass A/B/C.


## Phase C final verification — 2026-11-13
- Fixed CI-reported indentation error in `evidence_bundle.py`.
- Exact code commit `6344b576db64438e9a2ebfe5acdcc74afeac479e`: 79 tests PASS; strict archive audit 990/990, consistent=true.
- [GitHub Actions #43338094337 — SUCCESS](https://github.com/useformotor3/ai-discord-bot/actions/runs/43338094337).
- `main.py`, production workflow, v2 prompt and v2 contract remained unchanged. No production integration or main-branch sync.


## Phase D — Exact quote / locator validation (design only)
- [Design proposal](docs/PHASE_D_EXACT_QUOTE_VALIDATION_DESIGN.md) covers deterministic excerpt reconstruction, locator candidate classes, bounded context packets, human review records and fail-closed status separation.
- Machine exactness will only establish correspondence to normalized extraction output; legal meaning, source-view fidelity and claim support still require human review.
- Implementation is NOT started and requires separate explicit approval. No production/v2 changes.


## Phase D — implementation in progress (2026-11-13)
- User approved the isolated Phase D implementation.
- Code: [evidence_quote_validator.py](evidence_quote_validator.py); tests: [test_evidence_quote_validator.py](tests/test_evidence_quote_validator.py); implementation note: [PHASE_D_IMPLEMENTATION.md](docs/PHASE_D_IMPLEMENTATION.md).
- Machine EXACT_MATCH means exact match to Phase B normalized extraction only. Legal/product status stays UNVERIFIED; PDF visual fidelity, semantic claim support and legal interpretation remain human review.
- Final hardened HEAD `eaf4b4d31c0dccd2a624ab0f67fabdc166936a70` passed Actions #43345315133: 105 tests, archive/history 990/990 consistent; protected files and Phase C bundle/v3/schema unchanged. Do not merge/rebase/sync or integrate production.


## 2026-11-13 추가 — Phase E 설계 및 승인 대기
- [Phase E 통제된 공식 출처 fetch/추출 품질 검증 설계](docs/PHASE_E_CONTROLLED_FETCH_AND_EXTRACTION_DESIGN.md) 작성.
- Phase A DNS preflight와 실제 TCP 연결 간 TOCTOU 잔여 위험을 확인했으므로 IP-pinned transport 및 TLS hostname 검증을 E1/E2 mock/adversarial tests로 입증하기 전 실제 URL fetch 금지.
- 현재 사용자 승인 요청은 E1+E2 작업 브랜치 구현/오프라인 테스트에 한정. E3 실제 URL fetch는 E1/E2 CI 확인 후 별도 승인.


## 2026-11-13 — Phase E E1/E2 completed
- E1/E2 implementation and offline adversarial tests complete; see `docs/PHASE_E_IMPLEMENTATION.md`.
- Exact code/test CI: HEAD `d355aefb74f2b1b9159de98827fac8600fb68d4c`, run #43367432101, 126 tests OK; strict archive audit 990/990 consistent.
- E3 (real official-source fetch/extraction) remains blocked until separately approved. No live source fetch or production integration has occurred.


## 2026-11-13 — Main archive reports #13–#27
- Completed the next manual audit batch: [reports #13–#27](docs/ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md). Result: 15 CONFLICT; 0/15 Raw Text Quote blocks reusable as verbatim current CRA text. This is a non-random batch, not a whole-archive error rate.
- Next archive audit starts at report #28. Keep original main archive/history/state read-only.
- [Phase E3 approval package](docs/PHASE_E3_APPROVAL_PACKAGE.md) is prepared but **not approved or executed**. Live official-source fetch requires the explicit phrase “E3 실행 승인”.


## 2026-11-13 — 보고서 우선 작업 기준
- 먼저 읽을 통합 인덱스: [CRA 서보 드라이브 통합 보고서](docs/MASTER_REPORT.md).
- 제1권 법령 조사: [CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md](docs/CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md).
- 제2권 적용·구현 방안: [SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md](docs/SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md).
- 운영 자동화 코드 변경은 [PROTECTED_CODE_CHANGE_PROPOSAL_V1.md](docs/PROTECTED_CODE_CHANGE_PROPOSAL_V1.md)를 먼저 검토하고 사용자 별도 승인 후 진행한다.
- 보고서 파일을 실제 산출물로 계속 생성한다. 파일이 커지면 권/장 분리, 마스터 인덱스, 안정적 요구사항/출처/시험 ID를 유지한다.
- 법령 VERIFIED와 제품 적용 VERIFIED를 분리한다. 미확인 제품 사실·시험 미실시는 절대 완료 처리하지 않는다.


- 마스터 보고서 인덱스: [MASTER_REPORT_INDEX.md](docs/MASTER_REPORT_INDEX.md)
- Article 14 신고 대응 절차: [CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md](docs/CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md)


## 2026-11-13 — 보고서 우선 실행 원칙

- 수집 파이프라인, 검증기, 백로그, 계획서만 갱신한 것을 기술 보고서 완성으로 간주하지 않는다.
- 보고서 산출물은 `docs/MASTER_REPORT_INDEX.md`에 등록한다. 각 문서는 문서 ID/버전/기준일, 공식 출처와 정확한 위치, 주장별 검증 상태, 제품 가정, 미해결 입력, NOT_RUN 시험을 명시한다.
- 현재 CRA 보고서는 일반 참조 기준선이며 제품별 적합성 판정이 아니다. 제품 SKU, 정확한 MCU 주문 코드 및 시험 증거가 미확정이다.
- 아키텍처/운영 문서만 반복 개선하지 말고, 검증된 내용을 실제 보고서 본문·비교표·매뉴얼에 우선 반영한다.


## 2026-11-13 — 상시 연속성 현황판 도입 및 범위 정정
- [AI 연속성·실행 현황판](docs/AI_CONTINUITY_BOARD.md)을 신규 세션 필수 첫 문서로 지정했다. 매 세션은 현재 저장소 상태와 대조하고 작업 종료 시 반드시 갱신한다.
- 현재 프로젝트 범위는 CRA 전용이다. SIL 3 벤치마킹은 현재 범위가 아니며 과거 로그의 관련 문구는 현재 우선순위로 재사용하지 않는다.
- 결과물 우선 원칙: 가능하면 매 작업마다 보고서 장/표/설계/검증 대장 등 실질 산출물을 함께 만든다. 코드 개선은 허용하며, 코드-only 작업은 예외 사유를 기록한다.
- 이 항목은 과거 기록이며 최신 상태로 사용하지 않는다. 현재 감사 위치와 main HEAD/state/history는 문서 하단의 '한국어 정본 및 최신 통합 기준'과 AI_CONTINUITY_BOARD에서 확인한다.


## 과거 감사 진행 기록 (현재 기준으로 사용 금지)
- 아래에 남아 있는 과거 배치 위치와 CI 결과는 당시 기록이다. 최신 감사 위치는 #8–#52 완료, 다음 대상 #53이며, 최신 HEAD CI 상태는 매 세션 현재 커밋 기준으로 다시 확인한다.


## 2026-11-13 — 한국어 정본 및 최신 통합 기준

- 최종 산출물 기본 언어는 한국어다. 법령명·조항·표준·제조사 문서명·부품번호·원문 인용·상태 코드는 영어 원문을 유지할 수 있다.
- [AI 행동강령](docs/AI_RULEBOOK.md) 제15절과 [문서 구조·전체 링크 지도](docs/CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md) 제11절을 적용한다.
- 최신 감사 범위는 #8–#52이며, 누적 45건 중 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED다. 비무작위 연속 표본이며 전체 archive 오류율이 아니다.
- 다음 main-only 감사 시작점은 #53이다. 배치 시작 시 main HEAD/state/history를 다시 조회한다.
- #43–#47 및 #48–#52 정정은 제1권·제2권·PSIRT SOP·MASTER_REPORT와 관련 매트릭스에 단계적으로 통합한다. 전수 문서 대조는 아직 진행 중이다.
- 현재 기준선의 숫자와 CI 상태는 [AI_CONTINUITY_BOARD](docs/AI_CONTINUITY_BOARD.md) 및 [PROJECT_STATUS](docs/PROJECT_STATUS.md)에서 새 세션마다 다시 확인한다. 과거 로그의 main HEAD·감사 위치·CI 성공은 최신 기준선으로 재사용하지 않는다.


## 2026-11-13 — #8–#52 원본 추적 ID 연결 현황

- #8–#62 55개 보고서의 날짜 포함 Claim ID, 원본 archive 경로, blob SHA, 파일 판정과 중심 정정 요약을 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 등록했다.
- #8–#12 상세 감사 문서도 재확인해 원본 경로와 SHA를 복원했다.
- 보고서 내 모든 하위 주장·직접 인용의 원자 단위 연결은 후속 P0로 남아 있다.


## 과거 감사 상태 — #8–#57 (2026-11-13)

- #53–#57 감사 완료: 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/5.
- #38 감사 판정은 Annex I Part I(2)(m) 데이터·설정 영구 제거 요구를 누락한 점을 확인해 PARTIALLY_VERIFIED로 정정했다.
- #8–#57 누계: 50건 중 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/50. 비무작위 연속 표본이며 전체 archive 오류율이 아니다.
- Claim Evidence Ledger에는 #8–#57 50개 보고서의 날짜 포함 파일 중심 ID가 등록되었다. 각 파일 내부의 모든 개별 법적 주장/인용을 원자 레코드로 분해하는 작업은 미완료다.
- 다음 감사 시작점은 #58–#62다.

## 최신 감사 상태 — #8–#62 (2026-11-13)

- #58–#62 감사 완료: 5 PARTIALLY_VERIFIED / 0 CONFLICT / 0 VERIFIED; 직접 인용 재사용 0/5.
- 누적 #8–#62: 55건 중 40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/55. 비무작위 연속 표본이며 전체 archive 오류율이 아니다.
- #58–#62 원자 Claim ID 21개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 추가했다.
- #58–#62의 법령 정정은 제1권·제2권·PSIRT SOP·법령 기준선·요구사항 매트릭스·MASTER_REPORT에 반영했다.
- main 최신 관찰 HEAD #118: \`75add8711d0254da7dea1766bb42f80fc04d36ee\`; state count 118; history 1,393 entries. Archive tree count는 미확인.
- 다음 P0는 #8–#57 개별 주장·인용의 원자 분해와 상위 문서 전수 대조다. 이후 main-only 감사 #63–#67.
- main은 읽기 전용이며 merge/rebase/sync 금지.

## 사후 기준선 — main report #125 (2026-11-13)

- #58–#62 감사는 report #118까지의 main 원본을 대상으로 했다.
- 이후 main 자동 아카이브가 #119를 추가했다: HEAD \`6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0\`, state count 125, history 1,394 entries.
- #119는 아직 감사하지 않았다. 다음 감사 시작점은 #63–#67이며, 배치 시작 시 main HEAD/state/history를 다시 확인한다.
- main은 read-only, merge/rebase/sync 금지.

## 원자 주장 분해 진행 — #8–#12 완료

- #8–#12 원본 5건의 개별 주장·인용을 32개 원자 Claim ID로 분해해 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 등록했다.
- 기존 파일 단위 감사 판정 5 CONFLICT / direct quote reuse 0/5는 유지한다.
- 다음 원자 분해 대상은 #13–#17이며, #18–#57까지 순차 진행한다.

## 원자 주장 분해 진행 — #13–#17 완료

- #13–#17 개별 주장·인용 29개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 감사는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- 다음 원자 분해 대상은 #18–#22.

## 원자 주장 분해 진행 — #18–#22 완료

- #18–#22 개별 주장·인용 29개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 감사는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- 다음 원자 분해 대상은 #23–#27.

## 원자 주장 분해 진행 — #23–#27 완료

- #23–#27 개별 주장·인용 30개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 감사는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- 다음 원자 분해 대상은 #28–#32.

## 원자 주장 분해 진행 — #28–#32 완료

- #28–#32 개별 주장·인용 33개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 감사는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- 다음 원자 분해 대상은 #33–#37.

## 원자 주장 분해 진행 — #33–#37 완료

- #33–#37 개별 주장·인용 33개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- EUR-Lex Implementing Regulation (EU) 2025/2392를 확인해 Annex III core-functionality test와 Article 32/Annex VIII 평가 경로를 보완했다.
- 기존 파일 단위 감사는 5 CONFLICT / direct quote reuse 0/5로 유지한다. 서보 드라이브 Class I/II 적용성은 UNVERIFIED.
- 다음 원자 분해 대상은 #38–#42.

## 원자 주장 분해 진행 — #38–#42 완료

- #38–#42 개별 주장·인용 33개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- #38은 Part I(2)(m) 영구 삭제 가능성과 Annex II(8)(d) 폐기 지침을 함께 반영해 PARTIALLY_VERIFIED로 정정된 상태를 유지한다.
- 다음 원자 분해 대상은 #43–#47.

## 원자 주장 분해 진행 — #43–#47 완료

- #43–#47 개별 주장·인용 37개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 판정 3 CONFLICT / 2 PARTIALLY_VERIFIED / direct quote reuse 0/5 유지.
- 다음 원자 분해 대상은 #48–#52.

## 원자 주장 분해 진행 — #48–#52 완료

- #48–#52 개별 주장·인용 36개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- 기존 파일 단위 판정 3 CONFLICT / 2 PARTIALLY_VERIFIED / direct quote reuse 0/5 유지.
- 다음 원자 분해 대상은 #53–#57.

## 원자 주장 분해 진행 — #53–#57 완료

- #53–#57 개별 주장·인용 32개를 [Claim Evidence Ledger](docs/CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID로 등록했다.
- #8–#62 55개 보고서의 원자 claim decomposition 345개를 완료했다. 55 file-level records와 합쳐 400 unique IDs, duplicate 0.
- 다음 P0는 Ledger의 중복/상충 claim 및 공식 원문 locator 정규화, 제1권·제2권·SOP·매트릭스·시험 대장 전수 대조다.

## 2026-11-13 authoritative snapshot — #8–#62 audit and claim normalization

- main latest observed: report #125; HEAD \`6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0\`; state count 125; history.json 1,400 entries. Archive tree count was not rechecked. main remains read-only.
- main-only audit scope #8–#62: 55 consecutive, non-random reports; file-level results **40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED**; direct quote reuse **0/55**. This is not a statistical error rate for the full archive.
- Claim Evidence Ledger: 55 file-level source records + 345 atomic claims = **400 unique IDs**, duplicate IDs 0. All 345 atomic claims have one or more Canonical IDs. Canonical register defines 46 requirements; 43 are referenced by legacy atomic claims, and 3 are forward-mapped to matrix requirements.
- #8–#57 (50 reports) and #58–#62 (5 reports) have completed atomic decomposition. Individual legal facts marked VERIFIED do not promote a conflicting source file to VERIFIED.
- Product-specific applicability, Class I/II classification, exact MCU order code and DUT test results remain UNVERIFIED/NOT_RUN.
- Current P0: reconcile the 345 atomic claims and 46 canonical requirements against Volume 1, Volume 2, PSIRT SOP, requirements matrix, integrated traceability matrix and test evidence register; resolve duplicated/contradictory wording and keep exact legal locators. Then proceed to main-only audit #63–#67.
- No production code, main.py, production workflow, Gemini V2 prompt/contract or main branch was changed. E3 live source fetch remains unexecuted. This batch is documentation-only.

## 2026-11-13 — Logging / Secure Data Lifecycle

- P1-12 logging: TST-LOG-01/02, NOT_RUN.
- P1-13 secure data erase/transfer and Annex II(8)(d) instructions: TST-ERASE-01..04, NOT_RUN.
- TST-NVM-01..03 are not substitutes for secure erase evidence. Threat model AST-11 / TH-19.

## 2026-11-13 current Git baseline — main #125 / work branch divergence

- main HEAD: report #125, SHA \`92e8ca7aa4a86b38627a1d8e9535e5b0463a8392\`; state.json count 125 (daily counter), history.json 1,400 entries; current main tree \`7679729e1b128eacf26034346dafb29aa8da610b\`.
- Work branch \`cra-project-foundation\` HEAD: \`ced168745cd19400ba29131a495c3bf5c3f924eb\`.
- Git compare main..work branch: **diverged**, ahead 968 / behind 416, merge base \`b425b6db591e34abe003522157cf97ecf2240d9f\`. Do not merge, rebase, sync or write to main. This divergence includes historical branch differences and is not created by this documentation-only continuation.
- Main archive source revalidation: all 55 audited file paths and blob SHAs for reports #8–#62 match the current main tree (55/55, missing 0, mismatches 0).
- Latest push CI on current work-branch HEAD: run 43408438728 SUCCESS; 140 tests passed; strict archive audit 990/990, unique paths 990, missing/orphan/duplicate/malformed 0, consistent=true. The branch workflow's state.count=3 is a daily counter, not an archive total. No PR-triggered workflow run and no PR was created.
- Current branch commits in this continuation are documentation-only; no additional production code changes were made here. Existing branch-vs-main code differences remain unmerged and must be reviewed separately.

