# CRA Servo Drive Compliance & Engineering Project

산업용 서보 드라이브의 EU Cyber Resilience Act(CRA) 대응을 위한 조사·설계·검증·문서화 프로젝트입니다. 문서의 기본 언어는 한국어이며, 법령·표준·제조사 원문은 원어와 출처를 보존합니다.

> **기록 원칙:** 프로젝트의 공식 진행 상태와 재개 지점은 이 저장소에 기록합니다. 대화창의 기억에만 의존하지 않습니다.

## 현재 상태

- 작업 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
- 운영 기준 브랜치: `main` — 별도 승인 없이 수정·병합하지 않습니다.
- 현재 작업: 조사 품질 감사, 자동화 코드 신뢰성 개선, 원본 테스트 실행 기반 확보
- P0 응답 검증/실패 차단: 작업 브랜치 구현 완료
- P1-A 상태·이력 안전성: 작업 브랜치 구현 완료
- helper 독립 pytest: 7 passed (전체 저장소 테스트 아님)
- 임시 재구성 사본 pytest: 21 passed (blob SHA 불일치로 예비 결과만 인정)
- **원본 동일성이 입증된 저장소 전체 pytest 및 GitHub Actions CI: 미실행 (작업 브랜치 Actions runs 0건 확인)**
- 실제 코드 리뷰에서 Discord/Git 실패 처리, 원자적 저장, 테스트 fixture의 실패 경로 검증 공백 확인
- main 대비 작업 브랜치: diverged. 문서 커밋으로 수치가 계속 변하므로 정확한 ahead/behind는 통합 직전에 실시간 재조회
- 2026-11-14 15:31 KST 스냅샷: 72 ahead / 50 behind; 당시 작업 브랜치 Actions runs 0건 (CI 성공 증거 없음)

Actions 성공은 자동화 실행 결과이지 CRA 법령 해석이나 출처의 사실 정확성을 보증하지 않습니다. 테스트 통과 숫자는 반드시 실행한 정확한 소스와 범위를 함께 표시합니다.

## 프로젝트 관리 문서

| 문서 | 목적 |
|---|---|
| [상황판](PROJECT_STATUS.md) | 현재 상태, 위험, 실제 검증 결과, 다음 재개 지점 |
| [마스터 계획](MASTER_PLAN.md) | 전체 단계, 우선순위, 완료 기준 |
| [AI 행동강령](AI_RULEBOOK.md) | 조사·근거·코드·테스트·기록 규칙 |
| [세션 로그](SESSION_LOG.md) | 날짜별 실제 작업, 변경 범위, 테스트 결과 |

## 주요 기술 자료

- [조사 품질 감사](reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md)
- [CRA 보고서 #28·#29 정정 기록](reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md)
- [자동화 코드 개선 설계 및 테스트 계획](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- [테스트 실행 환경 감사 및 예비 검증 한계](reports/TEST_EXECUTION_ENVIRONMENT_AUDIT_2026-11-14.md)
- [테스트 가이드](tests/README.md)

## 진행 원칙

1. 공식 법령·표준 원문을 우선하고 조항, URL, 확인일, 원문 인용을 기록합니다.
2. 법적 의무, 표준 요구사항, 공식 해석, 엔지니어링 권고, 미확인 가설을 분리합니다.
3. 조사 초안 생성과 출처/내용 검증을 구분합니다.
4. 중복 보고서를 양산하기보다 기존 자료를 검증·정정·통합합니다.
5. 코드 변경은 작업 브랜치에서 mock 테스트부터 수행하고, 운영 코드·workflow·데이터 변경은 별도 승인 없이 하지 않습니다.
6. 테스트 원본과 blob SHA가 일치하지 않으면 결과를 예비 검증으로만 기록합니다.
7. 운영 workflow를 테스트 목적으로 실행하지 않습니다.
8. 의미 있는 작업이 끝날 때 README, 상황판, 마스터 계획, 행동강령, 세션 로그와 관련 보고서를 동기화하고 GitHub에서 재조회합니다.

## 다음 작업

원본 소스의 blob SHA가 일치하는 격리 실행 경로를 확보하고 전체 pytest를 실행합니다. 이와 별개로 현재 테스트 fixture의 Git/Discord 실패 경로 검증 공백을 보완할 필요가 있습니다. P1-B 코드 변경과 workflow 변경은 별도 승인 전까지 수행하지 않습니다.

자세한 재개 지점과 검증 한계는 [PROJECT_STATUS.md](PROJECT_STATUS.md)를 기준으로 합니다.
