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
1. 990개 추출 결과에서 URL 후보 0개 원인 분석 및 공식 출처 링크 복원
2. SBOM/지원기간/Article 14/제품 분류 관련 위험 플래그를 우선 표본 검증
3. 초기 5개 파일의 수동 감사 정정 내용을 전체 보고서의 근거·인용 규칙으로 반영
4. 서보 드라이브 제품 경계/인터페이스/의도된 용도를 정의해 CRA 적용성 검토
5. ST MCU 정확한 부품번호 확보 후 ST/TI 기능별 동급 비교
6. main.py와 Gemini 명령 구조는 분석 및 변경 제안만 수행하고 승인 대기
