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

## 신규 세션 필수 읽기 순서
1. [AI 행동강령](docs/AI_RULEBOOK.md) — 작업 전 필수 절차와 품질 기준
2. [프로젝트 상황판](docs/PROJECT_STATUS.md) — 현재 사실·진행 상태·위험
3. [마스터 계획](docs/MASTER_PLAN.md) — 우선순위와 완료 조건
4. [지식 인덱스](docs/KNOWLEDGE_INDEX.md) — 근거·검증 상태
5. [통합 보고서](docs/MASTER_REPORT.md) — 현재 보고서 구조와 작성 상태
6. [최근 세션 기록](SESSION_LOG/) — 직전 결정·성공·실패·다음 작업
7. 작업에 관련된 감사·법령 기준선·제조사 자료를 추가로 확인한다.

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

## 현재 기준선 (2026-11-12 확인)
- cra-project-foundation: archive 990개, history 990개, 경로 중복/누락/orphan 0.
- CRA Archive Integrity GitHub Actions: 최근 확인한 4회 실행 모두 success. 각 실행에서 단위 테스트와 strict archive/history 검사가 통과.
- main.py와 Gemini 프롬프트는 사용자 승인 전 수정 금지. 변경 필요 시 제안서를 먼저 제출하고 승인 대기.

## 최우선 다음 작업
1. 990개 자료의 위험 플래그별 표본을 원문과 대조해 실제 오류/정상 주장 구분
2. URL 후보 0개 원인을 대표 6개에서 확인했으므로 공식 canonical URL 복원
3. SBOM/지원기간/Article 14/제품 분류 관련 후보를 우선 검증
4. 초기 5개 파일 수동 감사 정정 규칙을 전체 보고서에 반영
4. 서보 드라이브 제품 경계/인터페이스/의도된 용도를 정의해 CRA 적용성 검토
5. ST MCU 정확한 부품번호 확보 후 ST/TI 기능별 동급 비교
6. main.py와 Gemini 명령 구조는 분석 및 변경 제안만 수행하고 승인 대기


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
