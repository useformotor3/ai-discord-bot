# CRA 프로젝트 문서 구조·전체 목차·링크 안내

- 문서 ID: CRA-DOC-MAP-001
- 기준일: 2026-11-13
- 적용 범위: CRA 서보 드라이브 프로젝트
- 상태: 운영 문서 구조 기준 v1.0
- 목적: 문서가 늘어나도 최신 기준, 검증된 결론, 최종 보고서, 세부 근거를 한 경로에서 찾고 중복·상충을 줄인다.

> 이 문서는 전체 문서의 길잡이다. 세부 내용을 복제하지 않고, 각 문서의 역할·권위·상태와 연결 링크를 안내한다. 내용의 최신성은 각 정본 문서와 Git 상태에서 확인한다.

## 1. 문서 운영의 기본 구조

문서는 목적에 따라 6개 층으로 관리한다.

| 층 | 역할 | 대표 문서 | 원칙 |
|---|---|---|---|
| 0. 진입·운영 | AI가 목표와 규칙을 복원하고 작업을 통제 | START_HERE, AI_CONTINUITY_BOARD, AI_RULEBOOK | 작업 시작 시 우선 확인 |
| 1. 통합 보고서 | 검증된 결론을 독자가 읽는 형태로 설명 | MASTER_REPORT, 제1권, 제2권 | 최종 산출물의 정본 |
| 2. 실무 매뉴얼·설계 | 실제 개발·운영·시험 절차와 설계 기준 | PSIRT SOP, HW 아키텍처, 매트릭스, 위협 모델 | 통합 보고서에서 링크 |
| 3. 요구사항·주장 추적 | 법령/기술 주장과 설계·시험·증거 연결 | KNOWLEDGE_INDEX, CLAIM_EVIDENCE_LEDGER, 통합 추적성 | 주장 단위 추적의 정본 |
| 4. 검증·감사 | 원문 대조, 반증, 오류·정정 이력 | CRA_LEGAL_BASELINE, 감사 보고서, correction ledger, double-check standard | 감사 기록 보존, 최종 결론은 상위 문서에 반영 |
| 5. 원자료·세션 기록 | 자동 조사 원본과 작업 이력 | research_archive, SESSION_LOG | 원자료는 근거 후보이지 검증된 사실이 아님 |

### 문서가 충돌할 때의 우선순위

1. 사용자의 가장 최근 명시적 지시(프로젝트 범위·승인 경계)
2. 현재 작업 브랜치의 최신 AI_RULEBOOK 및 AI_CONTINUITY_BOARD
3. 검증 상태와 근거가 명시된 최신 정본 법령/주장 대장 및 통합 보고서
4. 상세 실무 문서와 감사 배치 보고서
5. 과거 SESSION_LOG 및 자동 생성 archive

단, 법령·표준·제조사 기술 사실은 위 문서의 서술보다 해당 기관의 최신 공식 원문이 우선한다. 문서 우선순위는 원문보다 우위가 아니다.

## 2. 새 세션에서 읽을 순서

1. [START_HERE.md](../START_HERE.md) — 진입점과 읽기 순서
2. [AI 연속성·실행 현황판](AI_CONTINUITY_BOARD.md) — 사용자 의도, 현재 상태, 완료/미완료, 다음 행동
3. [AI 행동강령](AI_RULEBOOK.md) — 반드시 지킬 규칙과 승인 경계
4. [프로젝트 상황판](PROJECT_STATUS.md) — 확인된 상태 및 미해결 위험
5. [마스터 계획](MASTER_PLAN.md) — 우선순위와 완료 조건
6. [이 문서](CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md) — 전체 문서 지도
7. [마스터 보고서 인덱스](MASTER_REPORT_INDEX.md) — 산출물 카탈로그
8. [통합 마스터 보고서](MASTER_REPORT.md) — 현재 통합 본문
9. 최신 [세션 기록](../SESSION_LOG/) 및 이번 작업의 상세 근거 문서

필수 문서를 읽지 못하면 이전 대화 기억으로 빈 부분을 추정해 채우지 않는다.

## 3. 핵심 운영 문서 — 단일 책임

- [AI 연속성·실행 현황판](AI_CONTINUITY_BOARD.md): 사용자의 현재 의도, 범위, 진행 원칙, Git/CI 최신 확인값, 완료·실패·미완료와 다음 행동. 세션마다 갱신한다.
- [AI 행동강령](AI_RULEBOOK.md): 증거 기준, 더블체크, 문서 통합, 코드 승인, 비용·보안 등 변하지 않는 작업 규칙. 규칙 변경 시 갱신한다.
- [프로젝트 상황판](PROJECT_STATUS.md): 지금 실제로 확인된 상태와 위험. 오래된 수치·CI 결과는 최신 사실로 덮어쓰고 이력은 세션 로그에 남긴다.
- [마스터 계획](MASTER_PLAN.md): 우선순위, 의존관계, 완료 조건. 작업 순서가 바뀌면 갱신한다.
- [마스터 보고서 인덱스](MASTER_REPORT_INDEX.md): 발행 문서와 각 문서의 역할·상태·링크를 모은 카탈로그.
- [통합 마스터 보고서](MASTER_REPORT.md): 검증된 결론을 한 흐름으로 읽을 수 있게 통합하는 독자용 상위 문서.
- [지식 인덱스](KNOWLEDGE_INDEX.md): 공식 출처·주제·주장·검증 문서로 가는 인덱스.
- [검증 운영 프로토콜](VERIFICATION_PROTOCOL.md) 및 [더블체크 기준](RESEARCH_DOUBLE_CHECK_STANDARD.md): 원문 확인, 별도 재검증, 반증, 제품 적용성, 상태 승격 규칙.

## 4. 독자용 보고서·실무 매뉴얼

아래 문서는 서로 다른 독자 목적을 가진다. 모든 내용을 한 문서로 합치지 않는다. 대신 MASTER_REPORT와 MASTER_REPORT_INDEX에서 서로 연결한다.

### 4.1 상위 보고서

- [CRA 서보 드라이브 적합성 보고서 제1권](CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md): CRA 적용 범위, 법령 요구, 제조사 의무, 제품 적용성 판단의 상위 서술.
- [서보 드라이브 CRA 구현 계획 제2권](SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md): HW/FW 구현, 인터페이스, 업데이트, 시험·증거 계획.
- [통합 마스터 보고서](MASTER_REPORT.md): 제1·2권과 검증된 최신 결론을 연결하는 통합 본문 및 목차.

### 4.2 실무 매뉴얼·설계·절차

- [Article 14 PSIRT 신고 대응 SOP](CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md): 신고 대상, 타임라인, 역할·사건 기록 및 대응 절차. 조직별 연락처/담당자는 실제 확인 전 TBD.
- [서보 드라이브 CRA 보안 HW 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md): 참조 블록, 신뢰 경계, 인터페이스 및 설계 결정 후보. 제품 회로 확정본이 아니다.
- [제품 경계 템플릿](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md): SKU, 의도된 목적, EU 공급 형태, 연결성, 제품 경계와 core functionality 입력.
- [제품 분류·접근통제 매트릭스](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md): Article 7/Annex III 분류 판단, Article 32 경로, 접근통제의 법적 요구와 권장 구현 구분.
- [요구사항→서보 드라이브 추적성 매트릭스](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md): CRA 요구와 HW/FW·시험·증거 연결.
- [통합 요구사항–위협–설계–시험–증거 매트릭스](CRA_INTEGRATED_TRACEABILITY_MATRIX.md): end-to-end ID 추적.
- [서보 드라이브 위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md): 자산·공격자·신뢰 경계·위협 시나리오.
- [보안 시험·증거 대장](SECURITY_TEST_EVIDENCE_REGISTER.md): 시험 ID, 기대 결과, 증거 메타데이터와 실행 상태. 실제 미실행 시험은 NOT_RUN.

## 5. 근거·주장·정정의 정본

- [CRA 법령 기준선](CRA_LEGAL_BASELINE.md): 법령 구조와 기준 조항을 찾아가는 기준.
- [검증된 CRA 기준선](CRA_VERIFIED_BASELINE_2026-11-12.md): 원문 대조 범위와 시점이 표시된 기준선. 현행성 재확인 없이 영구 최신으로 간주하지 않는다.
- [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md): 개별 기술/법령 주장과 source ID, 버전, 위치, 적용 범위, 상태를 연결.
- [제조사 보안 자료 레지스터](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md): ST/TI 공식 문서와 revision·본문 검증 범위.
- [아카이브 주장 정정 대장](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md): 과거 자동 보고서의 주장별 오류·정정 추적.
- [아카이브 감사 대기열](CRA_ARCHIVE_AUDIT_QUEUE.md): 아직 검토할 원본과 배치 상태.

## 6. 감사 보고서와 원자료를 다루는 방법

- ARCHIVE_MANUAL_AUDIT_*.md 및 ARCHIVE_PASS_BC_*.md는 특정 배치의 원문·인용·반증 결과를 보존하는 감사 증거다. 매번 독자용 보고서로 읽게 하지 않는다.
- 감사에서 발견한 반복 법령 정정은 먼저 Claim Evidence Ledger/정정 대장에 연결하고, 검증된 결론은 제1권 또는 MASTER_REPORT의 해당 장과 실무 매트릭스에 반영한다.
- 자동 생성 research_archive/는 원본 보존 구역이다. 자동 보고서 문구나 인용을 검증 전 최종 보고서에 복사하지 않는다.
- 감사 원본의 SHA, 파일 경로, 행/페이지 위치를 남겨 추적성을 유지한다.
- 표본 감사 결과는 표본의 선택 방식과 범위를 함께 쓴다. 비무작위 연속 배치의 결과를 전체 archive 오류율로 일반화하지 않는다.

## 7. 문서 생성·수정·통합 규칙

1. 새 문서 생성 전 기존 정본 문서에 들어갈 내용인지 먼저 판단한다. 짧은 변경·정정은 기존 문서에 반영한다.
2. 새 문서가 필요한 경우 목적·독자·범위·정본 여부·상위 문서 링크를 명시한다.
3. 배치 감사·원문 캡처·긴 기술 부록처럼 독립 보존이 필요한 자료는 별도 파일로 둔다.
4. 독자용 설명·결론은 제1권/제2권/MASTER_REPORT에 통합한다. 매트릭스·SOP·시험 대장은 실무에서 직접 사용할 수 있으므로 독립 문서로 유지한다.
5. 동일한 사실을 여러 문서에 길게 복사하지 않는다. 요약과 링크만 두고 정본을 지정한다.
6. 검증된 결론을 변경하면 관련 문서, 매트릭스, 인덱스, 상황판을 함께 갱신한다. 불일치가 남으면 미동기화 상태를 기록한다.
7. 문서가 폐기되거나 superseded 되면 삭제하지 않고 상태·대체 문서·이유를 표시한다.
8. 새 문서가 만들어질 때마다 이 지도와 MASTER_REPORT_INDEX를 갱신한다.
9. 매 작업 종료 전 링크 대상 파일 존재, 제목/역할, 상태, 중복 ID와 상호 참조를 확인한다.

## 8. 최종 산출물 품질 상태

모든 보고서·매뉴얼·설계 자료는 아래 상태 중 하나를 명시한다.

- WORKING_DRAFT: 구조/초안 작성 중.
- EVIDENCE_REVIEW: 내용은 작성했으나 근거·반증 검증 진행 중.
- PARTIALLY_VERIFIED: 일부 주장·절만 검증되었고 미확인 범위가 남음.
- VERIFIED: 명시된 범위의 주장·근거·반증·적용성 검토가 완료됨. 법적 인증이나 제품 전체 적합성 승인과 동의어가 아니다.
- PRODUCT_INPUT_PENDING: 일반 지침은 작성됐으나 SKU/제품 경계/부품 정보가 없어 제품별 결론은 미확정.
- NOT_RUN: 시험·훈련·현장 절차를 실제 수행하지 않음.
- SUPERSEDED: 후속 정본으로 대체됨. 대체 링크를 남긴다.

현재 보고서·아키텍처·매트릭스 중 제품별 적용성은 제품 입력자료 미확보로 PRODUCT_INPUT_PENDING / UNVERIFIED, 실제 DUT 시험은 NOT_RUN으로 유지한다.

## 9. 작업 후 동기화 체크리스트

- [ ] 결과를 기존 정본 문서에 통합했는가?
- [ ] 감사·claim ledger와 최종 보고서의 상태/표현이 일치하는가?
- [ ] MASTER_REPORT와 MASTER_REPORT_INDEX 링크가 최신인가?
- [ ] 이 문서 지도와 START_HERE가 최신인가?
- [ ] PROJECT_STATUS와 MASTER_PLAN이 실제 Git/CI 상태를 반영하는가?
- [ ] AI_CONTINUITY_BOARD에 사용자 의도·결정·다음 행동을 기록했는가?
- [ ] SESSION_LOG에 성공·실패·미실행·제한을 기록했는가?
- [ ] 링크·ID·근거 위치를 다시 열어 확인했는가?

## 10. 범위와 주의

- 현재 프로젝트는 CRA 전용이다. 사용자가 새로 요청하지 않는 한 SIL 3 벤치마킹으로 확장하지 않는다.
- 제품 SKU, intended purpose, 제품 경계, 실제 인터페이스/업데이트 방식, ST MCU 주문 코드가 확보되기 전 제품별 적용성·분류·적합성은 UNVERIFIED다.
- 이 문서의 링크 목록은 저장소 문서 지도이며 법적·기술적 주장의 증거 자체가 아니다.


### 2026-11-13 audit navigation update

- [main reports #48–#52 audit](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md): 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- Claim-level corrections are indexed in [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md) and integrated into Volume 1, Volume 2, the Article 14 PSIRT SOP and MASTER_REPORT.


## 11. 문서 기본 언어 및 용어 관리 — 한국어 정본

- 이 프로젝트의 기본 언어는 한국어다. 최종 보고서, 매뉴얼, SOP, 설계 설명, 시험 절차, 표의 설명과 결론은 한국어로 작성한다.
- 법령·표준·공식 문서의 명칭, 조항 번호, 기술 식별자, 제조사 원문 인용은 원문 그대로 유지할 수 있다.
- 핵심 전문용어는 최초 등장 시 한국어(영문)로 병기하고, 이후 같은 문서와 관련 문서에서 한국어 표기를 통일한다.
- 법령 직접 인용, 번역, 요약, 해석, 설계 권고를 구분한다. 한국어 번역을 공식 법령의 원문 인용처럼 표시하지 않는다.
- 기존 영문 문서가 최종 산출물의 정본 역할을 한다면 한국어 본문으로 전환한다. 영어가 필요한 자료는 공식 원문 증거 또는 부록으로 유지하고, 독자용 한국어 설명을 제공한다.
- 파일명·코드·필드명·고정 상태 코드의 영어 표기는 링크와 도구 호환성을 위해 유지할 수 있다. 파일명이나 코드가 영어라는 이유로 본문까지 영어로 작성하지 않는다.
- 문서 언어 전환 시 요구사항 ID, 주장 ID, 조항 위치, 출처 URL, 버전, 검증 상태, 시험 상태를 변경하지 않는다.
