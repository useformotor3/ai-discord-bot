# 브랜치 통합 감사 보고서 — 2026-11-16

## 1. 감사 목적과 범위

작업 브랜치 `test/failure-path-fixtures-2026-11-14`와 운영 `main`의 분기 상태 및 운영 데이터·코드 차이를 읽기 전용으로 조사했다. 이 보고서는 Git ref/commit/tree, Git blob SHA, 파일 원문을 교차 확인한 결과다.

- 감사 시각: 2026-11-16 (KST)
- 저장소: `useformotor3/ai-discord-bot`
- 작업 브랜치 HEAD: `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff`
- 운영 main HEAD: `31e0f8137630630ee30ea55add039b571f2c6801`
- 공통 조상(merge-base): `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- 작업 브랜치 기준 문서 base: `c6dfc5cee2485922b2313030dd9a5843e347afe7`

## 2. 분기 상태

| 비교 | 결과 |
|---|---:|
| 작업 브랜치 vs 기준 문서 base | 42 ahead / 0 behind |
| 작업 브랜치 vs main | 153 ahead / 658 behind |
| merge-base 이후 main 고유 커밋 | 657 |
| merge-base 이후 작업 브랜치 고유 커밋 | 152 |

이전 문서의 610 behind 수치는 오래된 스냅샷이다. 현재 기준으로 657 behind로 갱신해야 한다. 브랜치는 diverged 상태이며 직접 병합·리베이스·PR 병합은 안전하지 않다.

## 3. 전체 Git tree 비교 — 파일 목록 한도 우회 교차검증

GitHub compare 응답의 변경 파일 목록은 300개에서 잘렸으므로 이를 전체 목록으로 간주하지 않았다. 대신 main과 merge-base의 Git tree를 각각 recursive 조회해 SHA를 비교했다.

- merge-base tree: `11470d4a1c6cf32203afd08c72da7c61c7bb03df` (1,600 entries)
- main tree: `9bc69a07783b10e7df5294b30376f7bc3ab6e264` (2,258 entries)
- 양쪽 모두 API 응답의 `truncated=false`
- 추가: 658개
- 삭제: 0개
- 변경: 3개 경로

추가 658개는 모두 `research_archive/` 아래 새 자동 생성 보고서다. 변경 파일은 `history.json`, `state.json` 2개다.

1. `history.json` — 자동화 실행 이력 변경
2. `state.json` — 운영 상태 변경
3. `research_archive/` — 디렉터리 tree SHA 변경(657개 파일 추가에 따른 상위 tree 변경)

따라서 운영 main의 차이는 단순히 657개 커밋의 수치 문제가 아니다. 자동 생성된 보고서와 운영 상태·이력 데이터가 대량으로 추가/갱신된 상태다.

## 4. 중요 파일 원문 및 SHA 교차확인

### 4.1 운영 코드

- main `main.py`: `86a7731aad5de8d75581fc953bcea2c44adf2f2b`
- merge-base `main.py`: 동일 SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`
- 작업 브랜치 `main.py`: `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`

main의 운영 코드는 merge-base 이후 변경되지 않았다. P0/P1-A/P1-B1이 반영된 작업 브랜치 코드와 main의 코드는 서로 다르다. 이 상태에서 main에 작업 브랜치 코드를 덮어쓰거나 전체 브랜치를 병합하면 안 된다.

### 4.2 운영 workflow

- `.github/workflows/run.yml` main SHA: `65a8cadc8eac593f551e390698e367b1d161ecf1`
- merge-base SHA: 동일

운영 workflow는 merge-base 이후 변경되지 않았다. 원문상 `repository_dispatch`, `workflow_dispatch`, `contents: write`, Gemini/Discord secrets 사용, `python main.py` 실행이 확인된다. 운영 workflow는 감사 과정에서 수정하거나 실행하지 않았다.

### 4.3 운영 상태 파일

- main `state.json` SHA: `f4690efdd0e96d771e4ab826f1149a933ee282f5`
- merge-base `state.json` SHA: `172963125a28bcdc51f3bfc4504866505d7626c2`
- main 내용: date=`2026-11-16`, count=`111`, last_health_check=`2026-11-15T21:20:38.480365`
- merge-base 내용: date=`2026-11-14`, count=`29`, last_health_check=`2026-11-13T21:05:41.862977`

운영 상태 파일이 실제로 변경되어 있다. 작업 브랜치로 가져오거나 덮어쓰면 안 된다.

### 4.4 실행 이력

- merge-base `history.json`: 1,592개 객체 항목, 마지막 날짜 2026-11-14
- main `history.json`: 2,250개 객체 항목, 마지막 날짜 2026-11-16
- main 파일 blob SHA: `d4e283fc30b67ef11a6a4ce43614d30de047ea67`

두 파일 모두 JSON 배열이며 조사한 항목은 모두 객체였다. 운영 이력은 657개 항목 증가했다. 원본 이력은 보존 대상이며 통합 시 자동 병합/덮어쓰기를 금지한다.

## 5. 통합 위험 평가

| 위험 | 등급 | 근거 / 통제 |
|---|---|---|
| 운영 상태 데이터 유실 | 매우 높음 | `state.json`이 main에서 갱신됨. main 원본 보존 |
| 실행 이력 유실·중복 | 매우 높음 | `history.json` 1,592 → 2,250 항목 |
| 자동 생성 보고서 누락 | 높음 | main에 고유 archive 657개 |
| 코드 회귀 | 높음 | main.py SHA가 작업 브랜치와 다름 |
| 운영 자동화 영향 | 높음 | main workflow는 write 권한과 외부 secrets를 사용 |
| 변경 파일 목록 누락 | 중간 | compare 응답은 300개 한도; recursive tree로 전체 경로 수 교차확인 |

## 6. 결론 및 통합 원칙

**현재 상태에서는 merge/rebase/PR merge를 진행하지 않는다.** 이 결론은 분기 수치뿐 아니라 운영 데이터와 자동 생성 산출물의 실제 차이에 근거한다.

통합 전 필수 절차:

1. main의 `state.json`, `history.json`, `research_archive/`를 원본 보존 대상으로 고정한다.
2. 작업 브랜치의 코드·테스트·관리 문서를 별도 통합 후보로 분류한다.
3. 운영 데이터는 코드 통합과 분리해 백업·중복 판정·무결성 검증 절차를 설계한다.
4. `main.py`와 workflow는 별도 diff/review/CI를 거친 뒤 승인된 변경만 반영한다.
5. 데이터 migration, 운영 workflow 실행, secrets 접근, 실제 Discord/Gemini 호출은 각각 별도 승인 없이는 하지 않는다.
6. P1-B2/B3/B4 구현은 각각 별도 승인 전까지 보류한다.

## 7. 감사 한계

- Git tree 비교는 경로와 blob/tree SHA의 차이를 검증한다. CRA 법령 해석, 출처 진위, 연구 보고서의 사실 정확성은 검증하지 않는다.
- 운영 `main.py`와 workflow 원문을 확인했지만 운영 workflow를 실행하지 않았다.
- 이 감사에서는 운영 파일을 수정하지 않았고, branch merge/rebase/PR merge도 수행하지 않았다.
- P1-B1의 기존 CI 결과(43 passed / 1 xfailed)는 해당 검증 commit의 결과이며 이번 tree 감사에서 재실행한 결과가 아니다.


## 감사 중 main 자동 실행에 따른 스냅샷 갱신
- 최초 tree 비교 직후 main에서 Auto-archive #111 커밋이 추가되어 main HEAD가 `c6262ddb96d608216e16b0860d2d02b6aedde940`에서 `31e0f8137630630ee30ea55add039b571f2c6801`로 이동했다.
- 최신 ref 재조회 및 recursive tree 재비교 결과를 본문 수치에 반영했다. 최신 main은 658개 archive 추가, history 2,250개, state count 111이다.
- 최초 로그 이벤트의 main_head 필드 오기(작업 브랜치 SHA 기록)는 실제 최초 main SHA로 정정 이벤트를 추가했다.


## 문서 커밋 이후 브랜치 포인터 해석
- 위 153 ahead / 658 behind는 감사 스냅샷 작업 브랜치 HEAD `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff` 기준이다.
- 감사 결과를 기록·정정하는 후속 문서 커밋은 작업 브랜치만 전진시키며 운영 main에는 영향을 주지 않는다. 따라서 이후 ahead 수는 문서 커밋 수만큼 증가한다. 이 문서의 운영 main 기준 tree/데이터 수치는 main HEAD `31e0f8137630630ee30ea55add039b571f2c6801` 스냅샷이다.


## 8. 2026-11-17 09:09 KST — 최신 읽기 전용 스냅샷
조회 시각: 2026-11-17T09:09:39+09:00

### 8.1 Ref 및 commit 관계
- 운영 main HEAD: `0dde26ebac80a789c7a9d9e26560abad54606d32`
- 작업 브랜치 HEAD: `7ae3b251861b9a3de9981bd7202e346d05ca9430`
- merge-base: `7ae3b251861b9a3de9981bd7202e346d05ca9430`
- compare API: `status=behind`, ahead=0, behind=919. 작업 브랜치는 main의 조상이며 branch-only commit은 없다.
- compare API의 파일 목록은 변경 파일 전체 판정에 사용하지 않았다. 양쪽 recursive Git tree를 직접 비교했다.

### 8.2 Recursive tree
| 항목 | main | 작업 브랜치 |
|---|---:|---:|
| Tree SHA | `d606a8f03ba1db6cfb292e4087ae696234ea7ce0` | `5d40aa70d81faf7602c077e1ba440c7a166fa1c2` |
| Blob 수 | 2,438 | 1,617 |
| research_archive 파일 | 2,398 | 1,592 |
| truncated | false | false |

전체 blob path 비교: main-only 821, branch-only 0, 동일 경로 blob 변경 16.

### 8.3 운영 데이터 비교
| 항목 | main | 작업 브랜치 | 차이 |
|---|---:|---:|---:|
| state.json date | 2026-11-17 | 2026-11-14 | 변경 |
| state.json count 필드 | 5 | 29 | 변경 |
| history.json 항목 | 2,398 | 1,592 | main +806 |
| research_archive 파일 | 2,398 | 1,592 | main +806 |

- 데이터 관련 path 차이는 총 808개: main-only archive 806개, branch-only archive 0개, archive blob 변경 0개, state.json/history.json 변경 2개.
- history.json은 양쪽 모두 배열이며 branch의 1,592개 항목이 main 배열의 정확한 prefix다. main이 뒤에 806개를 추가했다.
- state count는 history/archive 누적 건수가 아니라 state 파일 내부 별도 카운터다.
- state SHA: main `c94cc82a55ad64555fe1c946a4acc163c98da2d5`, branch `172963125a28bcdc51f3bfc4504866505d7626c2`.
- history SHA: main `dbf719321a8fc27f7d910df5767734a1e2120964`, branch `4dc2d720418944be1dea42841933199247417864`.

### 8.4 주요 코드 및 workflow
- main.py: main `f28dbc540d56b313f0648d77c58734d27eb95d1a`, branch `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- .github/workflows/run.yml: main `743c2300d9d5fd51f86b3bee3effaeb7ec456f71`, branch `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- 두 파일 모두 blob SHA가 달라 내용이 다르다. 이번 작업은 해당 파일을 열거나 수정/실행하지 않았으며, SHA 차이만 기록한다.

### 8.5 결론 및 실행 범위
- 작업 브랜치는 main보다 919 commits 뒤처져 있고 고유 커밋이 없다. 이 브랜치를 main에 병합할 이유가 없으며, 통합 후보로 취급하지 않는다.
- main의 자동 생성 데이터 806건 증가가 확인됐다. 운영 데이터는 main 원본을 보존해야 한다.
- README, PROJECT_STATUS, MASTER_PLAN, SESSION_LOG, PROJECT_LOG 및 본 감사 보고서만 작업 브랜치에 기록한다.
- main, main.py, 운영 run.yml, state.json, history.json, research_archive 원본은 수정하지 않았다. merge/rebase/PR merge, workflow 실행, Gemini/Discord 외부 호출은 하지 않았다.
- 테스트는 실행하지 않았다. 따라서 테스트 PASS 판정은 없다.

## 2026-11-19 09:34 KST — 매일 통합 상태 점검 (읽기 전용 비교)

- 조회 기준 시각: 2026-11-19T09:34:27+09:00
- 운영 main HEAD: `732f5167ed1a272afc10bb66d4aceb68ccb96b79`
- 작업 브랜치 HEAD (문서 갱신 전): `ca3f6ee8c917da8e2485cf75cd9c90ee7fb03a85`
- merge-base: `7ae3b251861b9a3de9981bd7202e346d05ca9430`
- GitHub compare API: status=`diverged`, **ahead=1 / behind=1,357**. 작업 브랜치에는 main에 없는 고유 커밋 1개가 있다.
- compare API wrapper의 파일 통계는 6개만 반환했으므로 전체 파일 경로 판정에 사용하지 않았다. 양쪽 recursive Git tree 전체를 조회하고 `truncated=false`를 확인한 뒤 path/blob SHA를 비교했다.
- recursive tree: main tree `d1281ea188b7313ee4923c2e9df5ab88a1014561`, 2,548 blobs; branch tree `9bed5aa6d39e210ac564fcaea9d744d086d5ce21`, 1,617 blobs.
- 전체 blob 경로 차이: main-only 931, branch-only 0, 동일 경로 blob 변경 19. main-only 중 archive 839, 비-archive 92.
- 변경 경로 19개: `.github/workflows/run.yml`, `.github/workflows/tests.yml`, `AI_RULEBOOK.md`, `MASTER_PLAN.md`, `PROJECT_LOG.jsonl`, `PROJECT_STATUS.md`, `README.md`, `SESSION_LOG.md`, `history.json`, `main.py`, `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16.md`, `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`, `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`, `state.json`, `tests/README.md`, `tests/conftest.py`, `tests/test_external_failure_paths.py`, `tests/test_main_characterization.py`, `tests/test_p1_reliability.py`.
- 데이터 경로: main archive 2,431 / branch archive 1,592; main-only archive 839, branch-only 0, modified archive 0. 즉 archive 원본은 추가분 외에 동일 경로 내용 변경이 없다.
- `history.json`: main 2,431개 / branch 1,592개. branch 배열 1,592개 항목은 main 배열의 정확한 prefix이며 main에 839개가 추가됐다. main SHA `b9ea42fa437b2b3a5728db5d125d287fb746b46b`, branch SHA `4dc2d720418944be1dea42841933199247417864`.
- `state.json`: main date/count=`2026-11-17 / 38`, branch date/count=`2026-11-14 / 29`. main SHA `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, branch SHA `172963125a28bcdc51f3bfc4504866505d7626c2`. count는 상태 파일 내부 실행 카운터이며 history/archive 누적 개수와 별개다.
- 주요 코드/워크플로 SHA도 다르다: `main.py`와 `.github/workflows/run.yml`은 양쪽 blob SHA가 각각 다르다. 이번 감사에서는 파일 내용을 변경하거나 실행하지 않았다.
- 작업 브랜치의 README, PROJECT_STATUS, MASTER_PLAN, SESSION_LOG, PROJECT_LOG, 본 감사 보고서를 읽었다. 기존 PROJECT_LOG.jsonl 26행 모두 유효 JSON이었다.
- 판단: 작업 브랜치는 main보다 1,357 commits 뒤처져 있고 main에 없는 커밋은 1개다. 운영 데이터 839건 누적 차이와 코드/workflow/test 변경이 공존하므로 이 브랜치를 main에 직접 통합하지 않는다. 고유 1개 커밋의 내용은 별도 검토 대상이다.
- 이번 실행은 문서 기록만 작업 브랜치에 추가한다. main, main.py, 운영 run.yml, state/history/archive 원본은 수정하지 않는다. merge/rebase/PR merge, 운영 workflow 실행, Gemini/Discord 외부 호출은 하지 않는다.
- 테스트는 실행하지 않았으므로 PASS 판정은 없다.
