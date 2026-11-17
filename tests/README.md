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


## 추가 실패 주입 검증 — 2026-11-14
- transport 예외(RuntimeError 기반 connection reset/timeout) 주입 및 호출 캡처
- HTTP 401/403 응답 주입과 상태코드 관찰
- Git add/commit/push 각 단계의 non-zero return 및 check=True 예외, 실패 후 후속 명령 중단
- 이 테스트는 fixture 기능만 검증한다. 운영 코드의 retry, permanent-failure handling, sync status, atomic write를 검증하지 않는다.
- 최신 실행 결과는 이번 변경 commit의 GitHub Actions run을 확인한 뒤 기록한다.


## 2차 확장 CI 결과 — 2026-11-14
- Run #12: 실패. 변경된 `tests/test_mock_infrastructure.py`의 SHA pin 누락이 원인으로, source integrity 단계에서 중단되어 compileall/pytest는 실행되지 않았다.
- Run #13: [성공](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208), commit `27d2c69287631b041672b9989fdeeb3066f5ebb9`.
- 6개 핵심 파일 Git blob SHA 일치, compileall 통과, pytest **30 passed, 5 xfailed**.
- 새로 추가한 7개 fixture case는 Run #13에 포함된다.


## Discord 영구/불명확 전송 오류 기대 동작
- HTTP 401/403/404: permanent_failure, 자동 재시도 금지(strict xfail).
- HTTP 503: delivery_unknown, 중복 방지 수단이 없는 한 자동 재전송 금지(strict xfail).
- 429: Retry-After/retry_after 준수 제한 재시도(strict xfail).
- [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842): 30 passed, 8 xfailed. xfail은 아직 main.py에 구현되지 않은 P1-B 기대 동작을 나타낸다.


## P1-B1 Discord 전송 테스트
- timeout: connect/read (3.05, 10), wait=true, 응답 message ID 확인.
- ConnectTimeout: 최대 2회 재시도 후 failed.
- HTTP 429: Retry-After 헤더 또는 JSON retry_after, 최대 2회 재시도, 대기값 30초 초과 deferred.
- HTTP 400/401/403/404: permanent_failure, 재시도 금지.
- HTTP 5xx, ReadTimeout, 일반 ConnectionError: delivery_unknown, 자동 재전송 금지.
- 후속 chunk 실패: partial, 성공 chunk의 message ID 보존, archive/state/history 후속 저장 확인.
- CI Run #18: 43 passed, 1 xfailed. 유일한 xfail은 P1-B3 Git sync failure 상태화.


## P1-B2 원자적 로컬 저장 테스트
- `persistence.py`는 archive/history/state를 durable journal 기반 transaction으로 저장하고 PREPARED/APPLYING/COMMITTED 상태에서 재시작 roll-forward recovery를 수행한다.
- 검증: 각 target replace 직후 중단, PREPARED 이후 중단, stage/fsync 실패, journal/stage/backup 손상, target SHA 불일치, stale snapshot, archive 충돌, 중복 target, 경로 위반, main 시작 시 recovery 실패의 외부 호출 차단.
- P1-B2 allowlist 보강 CI Actions 43851438733: source SHA 일치, compileall 통과, 전체 suite 70 passed / 1 xfailed.
- xfailed 1건은 P1-B3 Git sync failure 상태화이며 P1-B2에서 변경하지 않는다.
- POSIX `fcntl.flock` 및 directory fsync를 사용하므로 테스트 runner는 Ubuntu 기반이다. Windows 호환성은 검증되지 않았다.
- 실제 Gemini/Discord/운영 Git push 및 운영 파일은 테스트하지 않으며 접근하지 않는다.

- persistence recovery target은 `state.json`, `history.json`, `research_archive/*.md`만 허용한다. README, 코드, workflow, .git 등 저장소 내 임의 경로를 지정하는 manifest는 fail-closed 한다.
- 테스트 전용 workflow는 pull_request→main 및 main push에도 실행되도록 구성했다. 외부 API/secrets 없이 mock 테스트만 수행한다.


## CRA 공식 원문 출처검증 gate
- cra_source.py는 EUR-Lex CRA consolidated HTML을 직접 가져온다. HTTPS/최종 host, 최소 본문 길이, known corrigenda date(5.12.2024 / 2.7.2025 / 17.10.2025)를 확인한다.
- main.py는 원문 수집 성공 후에만 Gemini를 호출한다. 보고서 공식 URL·source version·Article/Annex locator·50자 이상 direct quote를 source text와 대조한다.
- 원문 HTTP 오류, 비공식 redirect, corrigenda 누락, quote mismatch는 fail-closed한다.
- 테스트에는 source retrieval mock을 사용하며 실제 EUR-Lex/Gemini/Discord/Git은 호출하지 않는다.
- CI Run #111: 103 passed, 1 xfailed; exact source blob SHA, compileall, full pytest success. Evidence: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987722348.
- 이 검증은 최소 provenance gate이며 모든 법률 해석·제품 적용성·적합성 판단을 보증하지 않는다.


## EUR-Lex read-only live canary
- Workflow: .github/workflows/cra-source-canary.yml; script: scripts/cra_source_canary.py.
- The canary performs only a public HTTPS GET to the official EUR-Lex CRA consolidated text. It does not call Gemini, Discord, production workflow, or Git write APIs.
- Canary Run #11: success; 196,076 visible-text characters; all known corrigenda dates (5.12.2024, 2.7.2025, 17.10.2025) present.
- Evidence: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987730194.
- This verifies endpoint reachability and source-index preconditions, not legal interpretation or product conformity.


## 확장 CRA source pack 검증 — 2026-11-17
- 공식 EUR-Lex 원문: CRA 2024/2847 consolidated + Regulation 2025/327 + Delegated Regulations 2025/1535, 2026/881.
- Isolated CI Run #141: 103 passed, 1 xfailed. [로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211881).
- Read-only Canary Run #26: success; 네 문서 총 220,715자. [로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211861).
- Canary는 EUR-Lex 공개 GET만 수행한다. 실제 Gemini/Discord/운영 workflow 호출은 없다.


## Latest exact-head verification — 2026-11-17
- Isolated CI Run #154: 103 passed, 1 xfailed; exact blob SHA, compileall and complete pytest suite succeeded. https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859144
- EUR-Lex read-only canary Run #29: success. https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859223
