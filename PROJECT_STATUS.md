# CRA 서보 드라이브 프로젝트 상황판

- 최종 갱신: 2026-11-14 (KST)
- 기준 저장소: `useformotor3/ai-discord-bot`
- 운영 기준 브랜치: `main` (운영 자동화 및 데이터 보존)
- 현재 작업 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
- 브랜치 관계(이번 확인): `main` 대비 45 commits ahead / 7 commits behind, diverged
- 프로젝트 상태: 조사 품질 감사 및 자동화 신뢰성 개선 진행 중
- 주 문서 언어: 한국어
- 안전 원칙: 법적 적합성·제품 분류·안전 관련 설계 판단은 근거와 인간 검토 없이 확정하지 않음

## 1. 한눈에 보는 현재 상태

| 영역 | 상태 | 확인된 사실 / 다음 조치 |
|---|---|---|
| 프로젝트 관리 체계 | 이번 갱신 반영 | 행동강령·상황판·마스터 계획·세션 로그·메인 페이지를 동기화 |
| CRA 조사 품질 감사 | 표본 감사 및 정정본 작성 | #27~#29 표본에서 인용·분류·시한 표현의 위험 식별 |
| P0 모델 실패 처리 | 작업 브랜치 구현 | 응답 구조 검증, 모든 모델 실패 시 비정상 종료 |
| P1-A 상태·이력 안전성 | 작업 브랜치 구현 | 손상 JSON/스키마 fail-closed, 날짜·시간 호환 |
| 전체 저장소 테스트 | 미완료 | 실제 checkout 기반 전체 pytest 실행 필요 |
| P1-B 전송·동기화 신뢰성 | 설계 단계 | Discord timeout/status/retry, Git sync 실패 상태화는 별도 승인 필요 |
| 통합 CRA 요구사항 추적 | 미착수/후속 | 공식 조항-제품 적용성-통제-시험 증거 연결 |
| SIL 기능안전 자료 | 별도 추적 필요 | CRA 사이버보안 결론과 혼합 금지 |

## 2. 최근 확인된 운영 기준선

| 항목 | 확인 결과 |
|---|---|
| 최근 확인된 Actions 실행 | #1608 |
| 실행 시각 | 2026-11-14 02:20 UTC |
| 실행 결과 | success |
| 최근 자동 보관 보고서(당시 확인) | #29 |
| 상태 카운터(당시 확인) | 2026-11-14 기준 29 |
| 이력 파일(당시 확인) | `history.json`, 1,592개 항목 |
| 조사 아카이브 | `research_archive/` |
| 자동화 코드 | `main.py` |
| 운영 워크플로 | `.github/workflows/run.yml` |

주의: 위 운영 기준선은 이전에 조회한 시점의 스냅샷이며 이번 작업에서 최신 Actions/아카이브를 다시 조회한 것은 아니다. Actions success는 코드 실행 결과이지 법령 해석이나 출처 정확성 검증 완료를 뜻하지 않는다.

## 3. 핵심 감사 발견사항

1. 원래 운영 코드에서 모델 호출이 모두 실패해도 경고 문구와 함께 성공으로 처리될 수 있는 결함을 식별했다. 작업 브랜치 P0 수정은 이 실패 경로를 차단한다.
2. 조사 결과에 공식 원문 URL·조항별 근거·인용 검증 상태가 구조화되어 있지 않은 문제가 남아 있다.
3. 보고서 #28·#29에서 CRA Article 13과 Article 14의 역할 및 보고 시한 설명에 정정이 필요해 정정본을 별도 작성했다.
4. 보고서 #27의 기본 비밀번호 금지·포트 비활성화 등은 CRA 원문에 직접 명시된 의무와 구현 권고를 분리해야 한다.
5. 저장소 루트에 U+200B가 포함된 별도 상태 파일이 있다는 과거 확인이 있다. 정체와 사용처를 확인하기 전 삭제 금지.
6. 현재 workflow에 독립 단위 테스트/법령 인용 검증 단계가 충분히 연결되어 있는지 추가 확인이 필요하다.

## 4. 작업 브랜치 구현 및 검증

### Phase A — 테스트 기반
- mock 경계: Gemini SDK, Discord HTTP, Git subprocess, sleep
- 기존 기록: 격리 mock suite 5 passed
- 운영 API/Discord/Git 실호출 및 운영 workflow 실행 없음

### Phase B — P0 응답 검증 및 실패 차단
- `validate_research_report()` 추가
- 최소 길이, 필수 섹션, 오류/쿼터/장애 문구 검사
- 동일 모델 재시도 후 다음 모델 폴백
- 모든 모델 실패 시 `SystemExit(1)`로 종료하고 전송·아카이브·상태 변경·Git 작업보다 먼저 차단
- 당시 격리 mock 테스트 9 passed
- 실제 외부 API/Discord/Git 및 GitHub Actions CI 실행 없음

### Phase P1-A — 상태·이력 안전성
- `load_state()`, `load_history()`, `parse_health_check()` 구현
- 손상 JSON/잘못된 구조/잘못된 필드/날짜 파싱 오류에서 원본을 조용히 초기화하지 않고 안전 종료
- aware/naive datetime 호환 처리
- 기존 `state.json` 구조 및 `history.json` 1,592개 배열 항목을 조회해 호환성 기준 확인
- 신규 helper 로직 독립 pytest: 7 passed
- 중요 한계: 위 7 passed는 helper 수준의 독립 검증이다. 저장소 전체 pytest, `main.py` 통합 실행, GitHub Actions CI 통과가 아니다.

## 5. 브랜치 보호 및 운영 영향

- 현재 작업 브랜치는 `main`보다 45 commits 앞서고 7 commits 뒤처진 diverged 상태다.
- 자동 생성 아카이브와 운영 변경을 보존하기 위해 merge/rebase는 보류한다.
- 운영 `main`, `.github/workflows/run.yml`, `state.json`, `history.json`은 이번 관리 문서 갱신에서 수정하지 않는다.
- 이번 단계에서 실제 Gemini/Discord/Git push 또는 운영 workflow를 실행하지 않는다.

## 6. 다음 우선순위 및 재개 지점

1. 작업 브랜치 전체 파일을 격리 checkout/테스트 환경에 확보할 수 있는 방법을 검토한다.
2. 실제 저장소 소스에 대해 compileall 및 전체 pytest를 실행하고 기존 Phase A/B/P1-A 회귀를 확인한다.
3. 실패가 있으면 승인된 P1-A 범위 내에서 원인·수정·재시험을 기록한다.
4. 전체 테스트 실행이 가능해진 뒤 P1-B(Discord timeout/status/retry 및 Git 동기화 실패 상태화)의 최소 변경안을 제시하고 별도 승인을 받는다.
5. 코드 안정성 이후 CRA 요구사항 추적표와 중복·정정 관리 인덱스를 구축한다.
6. 검증된 자료를 단일 통합 보고서와 필요한 부속서에 편입한다.

## 7. 문서 진입점

- 프로젝트 메인 페이지: [README.md](README.md)
- 행동강령: [AI_RULEBOOK.md](AI_RULEBOOK.md)
- 마스터 계획: [MASTER_PLAN.md](MASTER_PLAN.md)
- 작업 이력: [SESSION_LOG.md](SESSION_LOG.md)
- 조사 품질 감사: [reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md](reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md)
- CRA 보고서 #28·#29 정정: [reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md](reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md)
- 자동화 개선 설계: [reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- 테스트 가이드: [tests/README.md](tests/README.md)

