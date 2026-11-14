# CRA 서보 드라이브 프로젝트 상황판

- 최종 갱신: 2026-11-14 (KST)
- 기준 저장소: `useformotor3/ai-discord-bot`
- 기준 브랜치: `main` (운영 코드 보존)
- 작업 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
- 프로젝트 상태: 자동 조사 운영 중 / 조사 품질 감사 및 문서 체계 보강 중
- 프로젝트 범위: EU Cyber Resilience Act(CRA)와 산업용 서보 드라이브 제조사의 적용성·기술·문서 대응
- 주 문서 언어: 한국어
- 안전 원칙: 법적 적합성·제품 분류·안전 관련 설계 판단은 근거와 인간 검토 없이 확정하지 않음

## 최근 확인된 운영 상태

| 항목 | 확인 결과 |
|---|---|
| 최근 Actions 실행 | #1608 |
| 실행 시각 | 2026-11-14 02:20 UTC |
| 실행 결과 | success |
| 최근 자동 보관 보고서 | #29 |
| 상태 카운터 | 2026-11-14 기준 29 |
| 이력 파일 | history.json, 1,592개 항목 |
| 조사 아카이브 | research_archive/ |
| 자동화 코드 | main.py |
| 워크플로 | .github/workflows/run.yml |

주의: Actions success는 파이썬 작업이 오류 없이 종료했다는 뜻이며, 법령 해석이나 출처 정확성이 검증됐다는 뜻이 아니다.

## 핵심 감사 발견사항

1. main.py는 모든 Gemini 모델 호출이 실패해도 경고 문구를 넣고 success=True로 설정한다. 실패를 성공처럼 기록할 수 있는 결함이다.
2. 조사 프롬프트는 공식 원문 인용을 요구하지만, 결과 아카이브에는 원문 URL·조항별 근거 링크·인용 검증 상태가 구조화되어 있지 않다.
3. 최근 보고서 #28과 #29에서 CRA Article 13(제조자 의무)과 Article 14(제조자 보고 의무)의 역할이 혼동되었다.
4. 보고서 #28의 지원기간 근거는 Article 13(8) 및 Annex I Part I point 2(g)로 정정해야 한다. Article 14는 해당 지원기간 조항이 아니다.
5. 보고서 #29는 적극 악용 취약점 보고의 24시간/72시간/최종보고 시한을 설명하면서 조항 구분과 조건을 충분히 정확히 쓰지 않았다.
6. 보고서 #27의 기본 비밀번호 금지·포트 비활성화 등은 CRA 원문 그대로의 명시적 문구가 아니라 구현 권고/해석으로 구분해야 한다.
7. 저장소 루트에 눈에 보이지 않는 문자(U+200B)가 포함된 별도 `state.json` 파일이 존재한다. 정체와 사용처를 확인하기 전에는 삭제하지 않는다.
8. 현재 확인한 workflow는 조사 실행 중심이며 별도 단위 테스트/법령 인용 검증 단계는 확인되지 않았다.

## 현재 작업 우선순위

- [x] 최신 main / Actions / 최근 보고서 확인
- [x] 최근 CRA 보고서 #27~#29 표본 감사
- [x] 공식 EUR-Lex 원문으로 핵심 조항 대조
- [x] 운영 코드의 실패 처리 결함 식별
- [x] 보고서 #28·#29 정정본 작성 및 원본 보존
- [x] 자동화 실패 상태·근거 URL·조항 검증을 위한 코드 변경안 제출
- [ ] 사용자 승인 후 작업 브랜치에서 main.py 변경
- [ ] Phase A 테스트 기반 구축 승인 및 mock/unit 테스트 실행
- [ ] 검증된 자료를 누적 통합 보고서로 편입

## 다음 재개 지점

먼저 `reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md`와 `reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md`를 읽는다. 다음은 `reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md`의 Phase A 테스트 기반 구축이다. 사용자 승인 전까지 main.py와 운영 workflow는 수정하지 않는다.
## Phase A 진행 결과 — 2026-11-14

- 사용자 승인: Phase A 테스트 기반 구축 승인 완료
- 추가 파일: `tests/conftest.py`, `tests/test_main_characterization.py`, `tests/test_mock_infrastructure.py`, `tests/README.md`
- mock 경계: Gemini SDK, Discord HTTP 요청, Git subprocess, sleep
- 테스트 실행 결과(격리된 로컬 검증): `python -m compileall -q tests` 통과, `pytest -q tests/test_mock_infrastructure.py` 2 passed
- 브랜치에서 조회한 `main.py` 원문을 격리 작업공간에 반영해 전체 테스트를 실행했다: `python -m compileall -q tests` 통과, `pytest -q` 5 passed. 이는 mock 격리 실행이며 운영 환경/CI 실행은 아니다.
- 외부 서비스 실호출: 없음
- 운영 파일 변경: 없음 (`main.py`, workflow, `state.json`, `history.json` 미변경)

## 브랜치 동시성 주의

- 작업 브랜치는 최신 `main`과 diverged 상태이며, 확인 시점 기준 main보다 4 commits behind였다.
- main에는 자동화 아카이브가 계속 추가되고 있다(확인된 최신 보고서 #31).
- 운영 아카이브를 덮어쓰지 않도록 이번 단계에서 merge/rebase하지 않았다. 후속 통합 전 최신 main 변경을 별도 비교한다.

## Phase B P0 수정 결과 — 2026-11-14

- 사용자 승인: Phase B P0 수정 진행 승인
- `main.py`에 `validate_research_report()` 추가
- 최소 250자, 4개 필수 섹션(주제 요약 / 규격 근거·상세 내용 / 출처 자료·Source / 출처 원문·Raw Text Quote) 검사
- 빈 응답, 짧은 응답, 필수 섹션 누락, 알려진 오류/쿼터/서비스 장애 문구가 포함된 응답은 거부
- 유효하지 않은 응답은 모델별 재시도 후 다음 모델로 폴백
- 모든 모델 실패 시 `SystemExit(1)`로 종료하며 Discord 전송, 아카이브 생성, state/history 변경, Git 명령을 실행하지 않음
- 기존 state/history 파일 보존 여부를 테스트로 확인
- 격리 mock 테스트: compileall 통과, pytest 9 passed
- 실제 Gemini/Discord/Git 외부 호출 및 운영 workflow 실행: 없음
- GitHub Actions CI는 실행하지 않음

## 변경 범위
- 수정: `main.py`, `tests/test_main_characterization.py`, `tests/README.md`
- 미수정: `.github/workflows/run.yml`, `state.json`, `history.json`
- P1 항목(상태파일 손상 처리, datetime 오류, Discord timeout/status 검증, Git push 실패 상태화)은 이번 Phase B 범위에서 제외하고 후속 개선 대상으로 유지한다.



## Phase P1-A — 상태·이력 안전성 개선 진행 (2026-11-14)

- 사용자 승인 범위: 작업 브랜치에서 상태파일·이력파일·날짜 처리와 mock 테스트만 개선
- `main.py`: `load_state()`, `load_history()`, `parse_health_check()` 추가
- 손상된 JSON, 잘못된 최상위 자료형, 필수 상태 필드 오류, 음수/비정수 count, 잘못된 날짜는 조용히 초기화하지 않고 안전 종료하도록 변경
- `history.json`은 배열인지, 각 항목이 객체인지 확인하고 기존 항목 필드는 강제하지 않아 구형 이력 호환성을 유지
- timezone-aware datetime은 로컬 naive 시각으로 정규화해 기존 NOW 비교에서 aware/naive 혼합 오류를 방지
- 새 테스트 파일 `tests/test_p1_reliability.py` 추가
- `.github/workflows/run.yml`, `state.json`, `history.json`, 운영 `main` 브랜치는 변경하지 않음
- 실제 외부 API/Discord/Git push 및 GitHub Actions 운영 실행은 하지 않음
- 테스트 실행/최종 저장 검증은 별도 기록으로 완료 여부를 구분한다.


### P1-A 검증 현황 보충
- 저장소에서 기존 `state.json`을 재조회해 객체/date 문자열/count 정수/last_health_check 문자열 구조 확인
- 기존 `history.json` 1,592개 항목을 JSON 파싱해 최상위 배열 및 모든 항목 객체임을 확인
- 신규 helper 및 P1 테스트 모듈의 Python 문법 파싱(ast.parse) 통과
- 이 환경에서는 GitHub 저장소 checkout 기반 pytest 실행을 수행하지 못했으므로, P1-A pytest 통과로 보고하지 않는다.
- 현재 브랜치 비교: main 대비 41 commits ahead / 6 commits behind. main 자동화가 계속 진행 중이므로 merge/rebase 보류
