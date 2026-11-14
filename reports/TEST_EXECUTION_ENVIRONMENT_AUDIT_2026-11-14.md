# 격리 테스트 실행 환경 점검 기록 — 2026-11-14

## 목적
작업 브랜치 전체 pytest를 안전하게 실행할 수 있는지 확인한다. 운영 workflow와 외부 서비스는 실행하지 않는다.

## 저장소 접근 및 제약
- GitHub 저장소 `useformotor3/ai-discord-bot`는 public으로 확인했다.
- 작업 브랜치: `docs/cra-audit-and-project-control-2026-11-14`
- GitHub connector를 통해 다음 파일을 작업 브랜치에서 조회했다: `main.py`, `tests/conftest.py`, `tests/test_main_characterization.py`, `tests/test_mock_infrastructure.py`, `tests/test_p1_reliability.py`.
- 실행 컨테이너에서 `git clone`을 시도했으나 DNS 단계에서 `Could not resolve host: github.com`로 실패했다.
- 따라서 로컬 git checkout은 확보하지 못했다.

## 임시 격리 실행 결과
- 조회한 소스 내용을 바탕으로 별도 임시 디렉터리 `/tmp/cra_repo_test`에 테스트 실행용 사본을 구성했다.
- `compileall`: 종료 코드 0
- `pytest -q`: 21 passed (0.14s)
- Gemini SDK, Discord HTTP, Git subprocess, sleep은 mock 처리했다.
- 실제 Gemini API, Discord webhook, Git commit/push, GitHub Actions workflow 호출은 없었다.

## 중요 검증 한계 — 원본 동일성 불일치
- 임시 사본 5개 파일의 Git blob SHA-1을 계산해 GitHub에서 조회한 blob SHA와 비교했다.
- 5개 파일 모두 SHA가 일치하지 않았다.
- 따라서 임시 사본은 GitHub 원본과 byte-for-byte 동일하다고 입증되지 않았다.
- 테스트가 통과한 것은 이 임시 사본에 대한 결과다. 이를 작업 브랜치의 실제 저장소 전체 pytest 통과로 간주하지 않는다.
- 이 결과는 테스트 구성과 예상 동작을 확인하는 예비 검증으로만 취급한다.

## 결론
- 예비 격리 실행은 성공했으나 원본 동일성 검증이 실패했으므로 저장소 전체 테스트 완료 기준은 충족하지 못했다.
- 현재 전체 저장소 pytest 및 GitHub Actions CI 상태는 여전히 '미실행/미검증'이다.
- 원본 checkout 확보 또는 GitHub Actions에서 운영 workflow와 완전히 분리된 승인된 테스트 실행 경로가 필요하다.
- 운영 workflow, `main.py`, `state.json`, `history.json`, 운영 `main` 브랜치는 이 작업에서 변경하지 않았다.

## 다음 단계
1. GitHub에서 가져온 원본 파일을 변경 없이 로컬 테스트 환경에 전달할 수 있는 방법을 확보한다.
2. 각 파일의 Git blob SHA가 조회 시점의 SHA와 일치하는지 먼저 확인한다.
3. 일치한 원본에 대해 compileall 및 전체 pytest를 다시 실행한다.
4. 결과와 실행 로그를 상황판 및 세션 로그에 반영한다.

## 2026-11-14 추가 검증 — GitHub Actions 원본 checkout 성공

이전 임시 재구성 사본의 SHA 불일치 문제를 해소하기 위해 사용자의 별도 승인을 받아 테스트 전용 workflow를 작업 브랜치에 추가했다.

- Workflow: `.github/workflows/tests.yml`
- 실행: [GitHub Actions Run #1](https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149)
- 실행 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- checkout된 원본의 5개 핵심 파일 Git blob SHA: 모두 GitHub 조회값과 일치
- compileall: 종료 코드 0
- pytest: **21 passed in 0.16s**
- workflow/job 결론: success

이 결과는 임시로 재구성한 파일이 아니라 GitHub Actions가 실행 commit에서 직접 checkout한 원본에 대한 검증이다. 따라서 해당 commit의 기본 pytest suite는 통과한 것으로 인정한다.

### 보안 및 범위
- 테스트 전용 workflow는 작업 브랜치 push 및 수동 실행만 지원한다.
- `contents: read`, checkout credential persistence 비활성화.
- Gemini API/Discord webhook 비밀키와 운영 Git push 권한을 사용하지 않는다.
- 기존 운영 `run.yml`, 운영 `main.py`, `state.json`, `history.json`, 운영 `main` 브랜치는 변경하거나 실행하지 않았다.
- 테스트는 mock 기반이며 Discord timeout/status 및 Git push 실패 동작을 검증하지 않는다. 이 공백은 별도 P1-B 범위로 남긴다.

### 결론
원본 동일성 검증 실행 경로 및 기본 회귀 테스트 기반을 확보했다. 다만 테스트 커버리지의 실패 경로 공백까지 해소한 것은 아니므로 P1-B 구현 전 별도 설계·승인을 유지한다.
