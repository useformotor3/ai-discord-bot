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
