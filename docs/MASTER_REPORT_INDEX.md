# CRA 서보 드라이브 통합 보고서 — 마스터 인덱스

- 문서 ID: CRA-SD-MASTER-INDEX
- 버전: 1.0
- 기준일: 2026-11-13
- 작업 브랜치: cra-project-foundation
- 제품별 상태: UNVERIFIED — 제품 식별정보/제품 경계 미확정

## 발행 문서

| 권 | 파일 | 핵심 내용 | 상태 |
|---|---|---|---|
| 1 | [CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md](CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md) | CRA 법령 조사·적용성·Article 13/14·Annex I/II·우선순위 | 초판 발행 |
| 2 | [SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md](SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md) | 서보 드라이브 HW/FW 적용·인터페이스·업데이트·시험·게이트 | 초판 발행 |
| 3 | [CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md](CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md) | 취약점/사고 접수·분류·24h/72h/최종보고 대응 절차 | 초판 발행 |
| 4 | [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md) | 요구사항-HW/FW-시험-증거 연결 | 기존 초안 |
| 5 | [SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md) | 보안 하드웨어 참조 아키텍처 | 기존 초안 |
| 6 | [THREAT_MODEL_SERVO_DRIVE_CRA.md](THREAT_MODEL_SERVO_DRIVE_CRA.md) | 자산·공격자·신뢰 경계·위협 | 기존 일반 참조 모델 |
| 7 | [SECURITY_TEST_EVIDENCE_REGISTER.md](SECURITY_TEST_EVIDENCE_REGISTER.md) | 보안 시험 및 증거 대장 | 시험 미실시 |
| 8 | [SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md](SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md) | Annex II 사용자 정보·설명서 | 템플릿 |
| 9 | [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md) | 법령 조항·의무·예외의 한국어 기준선 | 정본 기준선 |
| 10 | [CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md) | 제품 분류 판단과 접근통제 요구/설계/증거 | v0.2 한국어판 |

## 품질·검증 규칙

**기본 언어:** 이 인덱스가 연결하는 최종 보고서·매뉴얼·SOP·설계·시험 자료는 한국어를 기본으로 한다. 공식 법령명·문서명·조항·부품번호·원문 인용·상태 코드는 영어 원문을 유지할 수 있다.
- 법령 원문에서 확인된 법적 요구와 제품 적용 판정을 분리한다.
- 공식 원문, 문서번호/버전, 조항·페이지·문단 위치가 없는 직접 인용은 금지한다.
- 번역/요약/해석은 직접 인용문과 분리한다.
- 제품 사실이 없으면 UNKNOWN/UNVERIFIED.
- 제안 시험은 NOT_RUN. 실제 시험 결과와 AI 제안은 구분한다.
- 기능안전(SIL/PL)과 CRA 사이버보안 적합성은 별도 평가한다.
- 각 문서는 문서 ID/버전/기준일/상태/범위/한계/출처를 유지한다.

## 분량 및 파일 관리
- 한 파일이 편집·열람·렌더링 한계를 넘으면 장/별책으로 나눈다.
- 각 장은 고유 문서 ID와 요구사항/출처 ID를 유지한다.
- 이 인덱스는 최신 발행본만 가리키며, 이전 버전은 삭제하지 않고 이력으로 보존한다.
- DOCX/PDF/PPTX/XLSX 변환은 Markdown 원본 검증 후 수행하고 원본 버전/해시를 기록한다.

## 수집 코드 개선 감사 및 제안
- [SOURCE_COLLECTION_CODE_AUDIT_AND_CHANGE_PROPOSAL_V1.md](SOURCE_COLLECTION_CODE_AUDIT_AND_CHANGE_PROPOSAL_V1.md) — 공식 원문 수집·추출 코드의 P0/P1 결함, 단계별 수정·테스트·롤백 제안. C1+C2 승인 대기.

## 운영 코드 개선 제안
- [PROTECTED_CODE_CHANGE_PROPOSAL_V1.md](PROTECTED_CODE_CHANGE_PROPOSAL_V1.md) — 보호 파일 변경 전 승인 검토본. 구현 승인 전.

## 수집 파이프라인 검증 기반
- [SOURCE_COLLECTION_CODE_AUDIT_AND_CHANGE_PROPOSAL_V1.md](SOURCE_COLLECTION_CODE_AUDIT_AND_CHANGE_PROPOSAL_V1.md) — 수집·추출 코드 감사 및 전체 개선 로드맵.
- [C1_C2_SOURCE_EVIDENCE_IMPLEMENTATION_REPORT.md](C1_C2_SOURCE_EVIDENCE_IMPLEMENTATION_REPORT.md) — 승인된 C1+C2 구현, 테스트 및 잔여 제한.

- [RESEARCH_DOUBLE_CHECK_STANDARD.md](RESEARCH_DOUBLE_CHECK_STANDARD.md) — 모든 CRA 조사 자료의 필수 원문·독립 교차검증 규칙.


## 2026-11-13 — 감사 산출물 및 운영 연속성

- [AI 연속성·실행 현황판](AI_CONTINUITY_BOARD.md): 신규 세션에서 프로젝트 목표, Git/CI 기준선, 실제 완료·실패·미완료, 작업 교훈, 다음 행동을 복원하는 필수 문서.
- [main reports #28–#32 수동 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md): 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5. main 원본은 read-only.


## main archive 수동 감사 추가
- [#33–#37 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md): 5 CONFLICT / direct quote reuse 0/5.

## 2026-11-13 — main reports #38–#42 감사 추가

- [#38–#42 상세 감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_38_42_2026-11-13.md): 4 CONFLICT / 1 PARTIALLY_VERIFIED / 0 VERIFIED, Raw Text Quote 직접 인용 재사용 0/5.
- 주요 정정: Annex II point 8(d) 폐기 지침과 실제 secure erase 기능 구분; Article 13(8)/(9)와 Annex I Part II(8) 구분; Annex II point 7/8 사용자 정보; Annex I Part II(4)–(8) 취약점 처리 항목 구분.

## 2026-11-13 — main reports #43–#47 감사 추가

- [#43–#47 상세 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md): 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; Raw Text Quote 재사용 0/5.
- 핵심 정정: 서보 드라이브가 자동으로 Annex III Class II라는 근거 없음; 분류는 Article 7 core functionality 및 Implementing Regulation (EU) 2025/2392에 따라 검토. 적합성 평가는 Article 32. 접근통제는 Annex I Part I 2(d). 지원기간 Article 13(8), 업데이트 가용성 13(9), 무상 업데이트 Annex I Part II(8).

## 실무 요구사항 매트릭스

- [CRA 제품 분류 및 접근통제 매트릭스 v0.1](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md): Article 7/Annex III/Implementing Regulation 2025/2392 기반 제품 분류 결정 게이트, Article 32 적합성 평가 경로, Annex I Part I 2(d) 접근통제의 법적 요구와 권장 구현·시험 증거를 분리.



## 문서 구조·전체 링크 안내

- [CRA 문서 구조·전체 목차·링크 안내](CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md): 문서 계층, 정본 우선순위, 세션 읽기 순서, 보고서·매뉴얼·설계·감사자료의 역할과 전체 링크를 모은 탐색 문서.
- [AI 연속성·실행 현황판](AI_CONTINUITY_BOARD.md): 사용자 의도와 작업 우선순위·진행 상태의 운영 정본.
- [AI 행동강령](AI_RULEBOOK.md): 검증 및 문서 통합 규칙.
- 문서 운영 원칙: 감사 보고서는 증거·이력 보존, Claim Evidence Ledger/정정 대장은 주장별 교정 추적, MASTER_REPORT 및 제1·2권은 독자용 결론 통합, SOP/아키텍처/매트릭스/시험 대장은 실제 사용 목적에 따라 분리 유지.


## 상위 보고서 통합 업데이트 — 2026-11-13

- 제1권 [CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md](CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md): #43–#47 정정에 맞춰 MCU category 14와 완제품 분류의 차이, Article 32 평가 경로, 접근통제 법적 요구와 권장 구현의 차이를 명확히 하고 분류 매트릭스/PSIRT SOP 링크를 추가.
- 제2권 [SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md](SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md): 분류 매트릭스, PSIRT SOP, 접근통제 매트릭스, HW 아키텍처, 통합 추적성의 역할별 연결을 추가.
- [MASTER_REPORT.md](MASTER_REPORT.md): MCU category 14 관련 문장을 기술 설명 및 MCU 자체의 시장 제공 여부를 포함하도록 명확화.
- 제품별 SKU/MCU/제품 경계가 미확정이므로 제품별 분류·적합성은 계속 UNVERIFIED. 문서 수정은 제품 적합성 승인이나 DUT 시험을 의미하지 않는다.


## main reports #48–#52 감사 및 법령 정정 통합

- [#48–#52 상세 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md): 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 주장별 correction record 5개를 추가했다.
- 제1권/제2권/PSIRT SOP 및 MASTER_REPORT에 Article 14(8) machine-readable user notification의 제한 조건, CVD/contact address의 정확한 Annex I Part II 위치, Article 13(6) component vulnerability reporting 방향, support/update 의무의 조항 구분을 반영했다.
- 누적 #8–#52: 45건, 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED. 비무작위 연속 표본.


## 문서 언어 및 통합 원칙 — 2026-11-13

- 최종 독자용 문서의 기본 언어는 한국어다. 제목·요약·설명·표·절차·판단 근거·결론을 한국어로 유지한다.
- 법령/표준의 공식 명칭, 조항 번호, 제조사 문서명, 부품번호, 코드, 정확한 원문 인용 및 고정 상태 코드는 영어 원문을 유지할 수 있다.
- 영어로 작성된 기존 실무 문서는 별도 영어판이 필요한 경우가 아니면 한국어 정본으로 전환한다.
- 감사 파일은 원본 SHA·반증·검증 이력을 보존한다. 검증된 정정 결론은 주장 대장과 이 인덱스가 연결하는 제1권·제2권·SOP·매트릭스에 반영한다.
- 최신 통합 상태: [#48–#52 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md) 및 [주장·근거 정정 대장](CLAIM_EVIDENCE_LEDGER.md) 참조. 제품별 적용성은 미검증, 실제 DUT 시험은 미실시.


## 최신 통합 진행 위치 — 2026-11-13

- 최신 감사 범위: main reports #8–#52. #8–#52 누적 45건 중 39 CONFLICT / 6 PARTIALLY_VERIFIED / 0 VERIFIED. 비무작위 연속 표본이며 전체 아카이브 오류율이 아니다.
- 상세 감사 정본: [#43–#47](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_43_47_2026-11-13.md), [#48–#52](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md).
- 주장별 정정 정본: [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md).
- 법령 조항 통합 정본: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md).
- 최종 독자용 설명: 제1권, 제2권, MASTER_REPORT. 운영 절차: PSIRT SOP. 분류·접근통제 상세: 한국어 매트릭스 v0.2.
- #8–#52 전체 정정의 제1권·제2권·SOP·추적성 매트릭스 간 전수 대조는 진행 중이며 완료로 표시하지 않는다.


## #13–#52 반복 감사 정정의 상위 통합

- 법령 조항/예외 통합 정본: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md) 제2.3절.
- 제1권 제3장에 Part I/Part II/Annex II/Article 14/64의 반복 오해 방지 기준을 추가했다.
- 제2권에 설계 후보와 직접 법적 의무의 구분, 사용자 매뉴얼/기술문서/폐기 안내의 구분을 추가했다.
- 주장 대장과 배치 감사 문서는 원본 SHA·개별 판정·반증을 보존하며, 독자용 보고서는 정정된 결론을 설명한다.
- #8–#52 전체 문서 간 전수 대조는 아직 진행 중이다.


## #13–#52 반복 감사 정정의 상위 통합

- 법령 조항/예외 통합 정본: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md) 제2.3절.
- 제1권 제3장에 Part I/Part II/Annex II/Article 14/64의 반복 오해 방지 기준을 추가했다.
- 제2권에 설계 후보와 직접 법적 의무의 구분, 사용자 매뉴얼/기술문서/폐기 안내의 구분을 추가했다.
- 주장 대장과 배치 감사 문서는 원본 SHA·개별 판정·반증을 보존하며, 독자용 보고서는 정정된 결론을 설명한다.
- #8–#52 전체 문서 간 전수 대조는 아직 진행 중이다.


## #8–#52 원본·Claim ID 추적성 업데이트

- [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md) 제30–31절에 2026-11-13 main reports #8–#52 총 45건의 날짜 포함 파일 중심 ID, archive path, blob SHA, 판정 및 중심 정정 요약을 연결했다.
- #8–#12 상세 감사 문서를 재확인하고 누락되었던 원본 식별 정보를 보완했다.
- 이전 상태 기록이며 superseded. #8–#62 55개 보고서의 원자 주장 345개 분해 및 Canonical ID 매핑을 완료했다.


## #53–#57 감사 및 정본 통합 — 2026-11-13

- [main 보고서 #53–#57 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_53_57_2026-11-13.md): 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/5.
- #38 판정은 Annex I Part I(2)(m) 누락을 확인해 PARTIALLY_VERIFIED로 정정했다.
- 누적 #8–#57: 50건, 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/50.
- 정정은 CRA 법령 기준선, 제1권·제2권, 사용자 정보 체크리스트, 요구사항 추적성 매트릭스에 반영했다.
- 다음 main-only 감사 대상은 #58–#62다.

## #58–#62 감사 및 정본 연결 — 2026-11-13

- [main 보고서 #58–#62 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md): 5 PARTIALLY_VERIFIED / 0 CONFLICT / 0 VERIFIED; 직접 인용 재사용 0/5.
- 주장별 원자 레코드: [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)의 #58–#62 섹션.
- 법령 정본: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md)의 CVD·신고·로깅 보완.
- 독자용 보고서: 제1권에 CVD/Article 14/로그 법령 요구를 통합, 제2권에 PSIRT/로그 설계 선택을 통합.
- 운영 절차: Article 14 PSIRT SOP의 trigger/recipient/deadline을 보완.
- 누적 #8–#62: 55건, 40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED; 직접 인용 재사용 0/55. 비무작위 연속 표본.
- #8–#57 개별 주장·인용의 원자 분해 및 상위 문서 전수 대조는 계속 진행 중이다.

## 원자 주장 추적성 진행 — #8–#12

- #8–#12 원자 Claim ID 32개를 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 등록했다.
- 기존 파일 단위 판정은 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- 다음 원자 분해 대상은 #13–#17이며, #18–#57까지 순차 진행 후 상위 보고서·SOP·매트릭스와 전수 대조한다.

## #33–#37 원자 주장·제품 분류 법령 보완

- #33–#37 원자 Claim ID 33개: [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md).
- #37의 Article 7/32/28/30/31 및 Annex VIII 정정과 Commission Implementing Regulation (EU) 2025/2392의 core-functionality test를 [CRA_VERIFIED_BASELINE](CRA_VERIFIED_BASELINE_2026-11-12.md) 및 제1권/제2권에 반영.
- 실제 servo drive Class I/II 적용성은 UNVERIFIED. 별도 네트워크 인터페이스 제품과 host drive를 구분하고 제품 자료 확보 후 판단.

## 2026-11-13 authoritative evidence index

- main-only reports #8–#62: 55 files, 40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED, direct quote reuse 0/55; consecutive non-random sample only.
- Claim Evidence Ledger: 55 file-level records + 345 atomic claims = 400 unique IDs, zero collisions; 45 canonical requirements, all atomic claims mapped.
- Canonical requirement mapping is integrated into [requirements-to-servo-drive matrix](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md) and [integrated traceability matrix](CRA_INTEGRATED_TRACEABILITY_MATRIX.md).
- Next P0: reconcile Volume 1/2, PSIRT SOP, traceability matrices and test evidence register against the 345 atomic claims; then audit main reports #63–#67.