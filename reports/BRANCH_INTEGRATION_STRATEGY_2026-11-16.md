# 운영 main 통합 전략 감사 보고서 — 2026-11-16

## 1. 목적 및 결론

P0/P1 신뢰성 개선이 포함된 작업 브랜치를 운영 `main`에 통합할 때, 운영 자동 생성 조사 자료를 보존하면서 코드·테스트·프로젝트 관리 문서를 안전하게 반영할 수 있는 방법을 평가했다.

**결론: merge-base 기준으로는 3-way PR 통합 후보가 양호하다.** 현재 작업 브랜치는 운영 데이터 파일을 삭제하거나 수정하지 않았고, 운영 main에서 분기 후 추가된 archive/history/state 변경과 작업 브랜치의 코드·문서 변경이 서로 분리되어 있다. 다만 P1-B2 코드 검토 보강과 PR CI 확인은 필요하며, 이번 감사에서는 PR 생성·merge·운영 실행을 하지 않았다.

## 2. 감사 기준 스냅샷

- 저장소: `useformotor3/ai-discord-bot`
- 운영 브랜치: `main`
- 작업 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`
- 운영 main HEAD: `3ebf6b977b0127291957ffb415dbdbc83b5b6d97` — Auto-archive: Research report #129
- 작업 브랜치 HEAD: `0fe9912b5dbba29eeb3ebd9e9f2c16a42544f925`
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- compare: 204 ahead / 677 behind, diverged
- 확인: GitHub API의 recursive Git tree 3개를 각각 조회했고 모두 `truncated=false`; blob 경로 및 SHA를 기준으로 비교했다.
- 이 수치는 스냅샷 기준이다. main 자동 아카이브와 후속 문서 커밋에 따라 변한다.

## 3. merge-base 기준 전체 tree 비교

| 항목 | merge-base | 운영 main | 작업 브랜치 |
|---|---:|---:|---:|
| blob 파일 수 | 1,597 | 2,274 | 1,620 |
| research_archive 파일 수 | 1,592 | 2,269 | 1,592 |

### 3.1 merge-base → main

- 추가: 677개
- 삭제: 0개
- 기존 경로 변경: `history.json`, `state.json` 2개
- 추가 677개는 전부 `research_archive/`의 자동 생성 보고서
- `history.json`은 1,592건에서 2,269건으로 증가
- `state.json`은 당일 count=130
- main의 archive 파일 2,269개와 history의 2,269개 file 참조가 모두 일치하며 누락 참조는 0개

### 3.2 merge-base → 작업 브랜치

- 추가: 23개 경로
- 삭제: 0개
- 수정: `main.py` 1개 경로
- `state.json` 및 `history.json`은 merge-base와 같은 blob SHA이며 작업 브랜치에서 수정하지 않았다.
- 작업 브랜치에 추가된 23개 경로는 테스트 전용 workflow, 프로젝트 관리 문서, 보고서, persistence 모듈 및 테스트 파일이다.

### 3.3 중요한 병합 의미

현재 두 branch tree만 직접 비교하면 main에만 존재하는 archive 677개가 보인다. 그러나 이것은 작업 브랜치가 삭제한 파일이 아니다. merge-base 이후 main이 추가한 파일이다. Git의 3-way 병합은 양쪽 변경을 merge-base와 비교하므로, **정상적인 merge commit은 main에서 추가된 677개 archive와 main에서 갱신된 history/state를 보존해야 한다.**

앞선 간이 비교에서 677개를 브랜치 삭제처럼 표현한 것은 부정확했다. 이번 보고서는 merge-base 기준의 실제 변경을 사용한다.

## 4. 운영 데이터 및 workflow 보호 확인

운영 main 스냅샷:
- `state.json`: SHA `b92c8c89cbd792796c9598382c5c662faeb5afcf`, date `2026-11-16`, count=130
- `history.json`: SHA `4e9d2d0f1c5e12064b5c4010c99bde2f0d34a367`, 2,269 entries
- `research_archive/`: 2,269 files, history의 참조 누락 0
- 운영 `.github/workflows/run.yml`: SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`

작업 브랜치는 위 운영 데이터 파일을 수정하지 않았고, 운영 `run.yml`도 변경하지 않았다. main.py만 작업 브랜치에서 개선되었다. merge 이후 운영 workflow가 개선된 main.py를 실행하면 실제 운영 동작이 바뀌므로, **코드가 main에 들어가는 행위와 운영 실행/배포 승인은 구분해야 한다.**

## 5. P1-B2 코드 리뷰 및 보강

### 발견 사항
기존 `persistence.py`의 `_safe_target()`은 저장소 root 바깥 경로는 거부했지만, root 안에 있는 임의 경로는 허용했다. 유효한 형식의 복구 manifest가 변조되면 `.github/workflows/run.yml`, `.git/config`, README 또는 코드 파일을 transaction target으로 지정할 수 있었다. 실제 정상 호출은 고정된 세 파일을 사용하지만, recovery 경계에서 target allowlist가 강제되지 않는 것은 fail-closed 설계의 빈틈이다.

### 보강
- 허용 target을 `state.json`, `history.json`, `research_archive/*.md`로 제한
- 저장소 문서·코드·workflow·`.git` 및 archive 하위 디렉터리 경로 거부
- 변조된 manifest가 `.github/workflows/run.yml`을 target으로 지정하는 recovery 실패 테스트 추가
- 테스트 전용 workflow의 SHA pin 갱신

보강 후 테스트 전용 CI:
- Run ID: `43851438733`
- 정확한 source blob SHA 일치
- compileall 통과
- pytest: **70 passed, 1 xfailed**
- 유일한 xfail은 P1-B3 Git sync 상태화로 이번 승인 범위 밖
- 결과: https://github.com/useformotor3/ai-discord-bot/actions/runs/43851438733

### 추가 PR CI 준비
테스트 전용 `.github/workflows/tests.yml`에 `pull_request` → `main` 트리거 및 merge 후 `main` push 트리거를 추가했다. 권한은 `contents: read`, checkout credential persist는 false이며 Gemini/Discord secrets나 운영 workflow를 사용하지 않는다. 이 workflow 변경은 작업 브랜치에만 있다.

## 6. 권장 통합 방식

**권장: 작업 브랜치 → main 대상 Pull Request → merge commit 방식.**

1. PR 생성 직전 main HEAD와 작업 브랜치 HEAD를 다시 조회한다. main 자동 아카이브가 계속되므로 이 보고서의 count를 영구 최신값으로 간주하지 않는다.
2. PR의 Files changed에서 변경 경로가 예상 범위인지 확인한다. 특히 `state.json`, `history.json`, `research_archive/`, 운영 `.github/workflows/run.yml`의 삭제/변경이 없어야 한다.
3. PR CI에서 source SHA, compileall, 전체 pytest가 실행되고 통과하는지 확인한다.
4. main의 자동 생성 archive/state/history가 PR diff에서 삭제 또는 덮어쓰기 대상으로 나타나지 않는지 다시 확인한다.
5. merge-base 및 PR conflict check를 확인한 뒤, 별도 승인 후 merge commit으로 통합한다.
6. 통합 후 main tree/data count, history-file 참조 무결성, 운영 workflow SHA를 재검증한다.

### 피해야 할 방식
- 현재 branch를 main 위로 무조건 rebase하거나 force-push하지 않는다.
- 작업 브랜치의 `state.json`/`history.json`을 main에 복사하지 않는다.
- archive를 복사/삭제하는 별도 migration을 하지 않는다. 현재 merge-base 분석상 migration은 필요하지 않다.
- `run.yml` 변경, 실제 Gemini/Discord 호출, 운영 실행, 운영 secrets 접근을 PR 테스트에 섞지 않는다.
- squash merge는 189개 커밋의 단계별 provenance를 압축하므로 우선 선택하지 않는다.

## 7. 통합 전 남은 운영 위험과 승인 경계

1. P1-B2는 POSIX `fcntl.flock` 및 directory fsync 기반이며 Ubuntu runner를 전제로 한다. Windows native 실행은 검증되지 않았다.
2. Discord POST와 로컬 transaction은 하나의 원자적 transaction이 아니다. 전송 성공 직후 로컬 저장 실패 시 중복/미기록 위험은 outbox/멱등성 설계(P1-B3 이후 별도 범위)로 해결해야 한다.
3. lock은 non-blocking이다. 중첩 실행은 기다리지 않고 실패한다. 운영 workflow의 concurrency 설정은 별도 운영 변경 승인이 필요하므로 이번에는 수정하지 않았다.
4. P1-B3 Git sync 상태화 및 P1-B4 import-time 구조 개선은 미구현이다.
5. CI 통과는 코드/테스트 검증이지 CRA 법적 정확성, 출처의 진위, 제품 적합성 또는 기능안전 인증 증거가 아니다.

## 8. 수행하지 않은 작업

- PR 생성, merge, rebase, force-push 없음
- 운영 main, 운영 state/history/archive, 운영 run.yml 수정 없음
- 운영 workflow 실행 없음
- 실제 Gemini API, Discord webhook 호출 없음
- 운영 Git push 없음

## 10. 최신 코드/테스트 blob SHA
- 작업 브랜치 `main.py`: `fa8679b758916ba8a446bae41b9ec1b40328da09`.
- `persistence.py`: `953e2a52b7e6d6e619a4f43766e52d6835df50c8`.
- P1-B2 tests: `f78d36164b5ac0d5d5eebe0c5eb5c1214c4e0671`.
- test workflow: `6a5bee0785eccc1f1b8074b80761b1b2a772d3c0`.
- production run.yml: `65a8cadc8eac593f551e390698e367b1d161ecf1`.

## 11. 감사 한계

Git tree 및 blob SHA 기반의 merge-base 변경 비교는 완료했다. 실제 Git merge-tree 실행 또는 PR 생성은 하지 않았으므로 충돌 없음은 merge-base 경로 변경 분석에 근거한 예상이며, GitHub PR의 최종 conflict check로 다시 확인해야 한다.
