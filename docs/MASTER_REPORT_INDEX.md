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

## 품질·검증 규칙
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

