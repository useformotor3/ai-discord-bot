# 자동화 테스트 가이드

## 목적
- 운영 `main.py`의 핵심 흐름을 격리된 mock 환경에서 검증한다.
- Gemini SDK, Discord HTTP, Git subprocess, sleep을 mock 처리한다.
- 상태파일과 아카이브는 pytest 임시 디렉터리에서만 생성한다.
- 실제 Gemini API, Discord Webhook, Git commit/push는 호출하지 않는다.

## 실행

```bash
python -m pip install pytest
python -m compileall -q main.py tests
python -m pytest -q
```

## 검증 범위
- 정상 보고서 생성 및 Gemini 모델 폴백
- 전체 모델 실패, 짧은 응답, 필수 섹션 누락, 오류 문구 차단
- 실패 시 기존 state/history 보존 및 외부 후속 작업 차단
- `state.json`의 JSON 파싱·필수 필드·자료형·날짜 형식 검증
- `history.json`의 JSON 파싱·최상위 배열·항목 객체 구조 검증
- 손상된 파일의 원본 보존 및 안전 종료
- naive/ timezone-aware `last_health_check` 처리
- mock 경계가 외부 호출을 실제로 가로채는지 검증

## 테스트 결과 해석
- pytest 통과는 mock 환경에서 코드 경로가 기대대로 동작한다는 뜻이다.
- 실제 Gemini·Discord 연동, GitHub Actions 운영 실행, CRA 법령 해석의 정확성을 보증하지 않는다.
- Discord timeout/HTTP status, Git push 실패 상태화, 아카이브 원자적 저장은 P1-B 후속 범위다.

## GitHub Actions 자동 검증

작업 브랜치 `docs/cra-audit-and-project-control-2026-11-14`에서 테스트 코드, `main.py` 또는 `.github/workflows/tests.yml`가 변경되면 테스트 전용 workflow가 실행되도록 구성했다.

- workflow: [Isolated Python Tests](../.github/workflows/tests.yml)
- 실행 순서: 원본 Git blob SHA 확인 → pytest 설치 → `compileall` → `pytest -q`
- 권한: `contents: read`만 사용
- Gemini API 키, Discord webhook, Git push 권한을 사용하지 않는다.
- 운영 workflow `run.yml`은 호출하지 않는다.
- 현재 workflow의 SHA 기준값은 2026-11-14에 확인한 다섯 개 원본 파일의 blob SHA다. 이 파일들을 의도적으로 변경할 때는 변경 검토와 함께 기준값도 갱신해야 한다.
- GitHub Actions 결과는 해당 실행의 commit SHA, 각 단계 로그, 테스트 결과와 함께 판단한다.
## 실제 GitHub Actions 실행 결과 — 2026-11-14

- Run #1: [Isolated Python Tests — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149)
- 실행 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- 원본 Git blob SHA 5개: 전부 일치
- compileall: 통과
- pytest: **21 passed in 0.16s**
- 기존 운영 workflow와 외부 Gemini/Discord/Git push는 호출하지 않았다.


## Discord/Git 실패 경로 테스트 — 2026-11-14

- `tests/conftest.py`는 Discord 응답 큐(HTTP status, headers, 예외), timeout 전달값, Git 명령별 return code/예외, `check=True`의 `CalledProcessError`, sleep 호출을 mock으로 기록한다.
- `tests/test_mock_infrastructure.py`는 429/Retry-After 응답과 Git push 실패를 fixture 단위에서 주입하고 격리되는지 확인한다.
- `tests/test_external_failure_paths.py`는 현재 `main.py`에서 아직 구현되지 않은 P1-B 기대 동작을 `xfail(strict=True)`로 표시한다. 이는 결함을 통과로 위장하지 않고 CI에 예상 미구현 항목을 명시한다. 향후 코드가 기대 동작을 충족하면 XPASS(strict)로 CI가 실패하므로 해당 xfail 표식을 제거하고 정상 통과 테스트로 전환해야 한다.
- 이번 범위는 fixture/test/테스트 전용 workflow뿐이다. 운영 `main.py`, 운영 workflow, state/history 데이터는 수정하지 않는다.
- 외부 Gemini, 실제 Discord webhook, 실제 Git push는 호출하지 않는다.
