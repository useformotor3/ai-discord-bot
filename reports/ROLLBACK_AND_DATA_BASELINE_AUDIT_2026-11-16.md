# 운영 데이터 기준선 및 복구 체크포인트 감사 — 2026-11-16

## 1. 기준점
- 저장소: useformotor3/ai-discord-bot
- 운영 main commit: 4cf0e708b28a343898af00d01521044dfb9a1987 (Auto-archive: Research report #158)
- recursive tree: 2,305 entries, truncated=false
- 백업 브랜치 safety/pre-merge-main-4cf0e70 readback SHA가 운영 main SHA와 일치

## 2. 동일 immutable SHA에서 수행한 데이터 검사
- state.json: date=2026-11-16, count=158, blob SHA=0addc96770c027651c1cbd229d30e3a17b4fec4a
- history.json: 2,297 entries, blob SHA=dbfd792717ab6b4c6ddd10d33dcb2065afc73a19
- research_archive/: 2,297 files
- history의 file 참조 누락 0건
- 동일 SHA에서 tree/state/history를 조회했으며 tree 응답 truncated=false
- 이 snapshot 기준 데이터 무결성 검사는 통과

## 3. 특수 파일명
- 루트에 U+200B ZERO WIDTH SPACE가 앞에 붙은 별도 state.json이 존재한다.
- blob SHA=de8505bdcb7709a96a4fe89edf124f9ad1917ce8, size=41 bytes
- 내용: date=2026-06-07, count=0
- 현재 main.py가 읽는 일반 state.json과 별개다. 생성 경위/참조 여부를 확인하기 전 삭제하거나 합치지 않고 보존한다.

## 4. 운영 코드와 workflow
- main.py blob SHA=86a7731aad5de8d75581fc953bcea2c44adf2f2b
- .github/workflows/run.yml blob SHA=65a8cadc8eac593f551e390698e367b1d161ecf1
- workflow trigger는 repository_dispatch(run-bot) 및 workflow_dispatch, permissions는 contents:write, checkout credential은 기본 유지, python main.py를 실행한다.
- 현재 운영 main.py는 feature의 P0/P1 개선 전 버전이다. 모델 전체 실패를 성공처럼 취급하는 경로, Discord 응답/timeout 검증 부족, 직접 파일 쓰기 및 Git push 예외 처리 약점이 남아 있다.
- 이번 감사에서는 실제 Gemini/Discord 호출이나 운영 workflow 실행을 하지 않았다.

## 5. 이전 불일치 조회의 정정
- moving ref main을 여러 API 호출에서 각각 조회하면 자동 아카이브 commit 사이에 서로 다른 시점의 state/history/tree가 섞일 수 있다.
- 앞선 조회에서 history 2,296 vs archive 2,295 및 missing 1로 보였던 값은 immutable SHA가 고정되지 않은 moving-ref 조회 결과였다.
- 동일 immutable commit 4cf0e708... 기준 재검사 결과 history=2,297, archive=2,297, missing=0이었다.
- 이를 지속적인 데이터 손상으로 분류하지 않는다. 이후 데이터 감사는 HEAD SHA를 먼저 고정하고 모든 조회에 동일 SHA를 사용한다.

## 6. 롤백 준비 평가
- main #156: safety/pre-merge-main-2622e332 -> 2622e332d6a3defd2079ccad3af36970001de5c1
- main #158: safety/pre-merge-main-4cf0e70 -> 4cf0e708b28a343898af00d01521044dfb9a1987
- 최초 feature: safety/pre-merge-feature-eba3aeb -> eba3aeb5710dcc6507623d56d586a619e9a4fc46
- 최신 feature 당시: safety/pre-merge-feature-6050de5 -> 6050de540e712162e9b27c51d0bcc8831a21e0f3
- Git safety branch는 state/history/archive를 포함한 tracked snapshot을 보존한다.
- 다만 운영 실행 후 전체 snapshot을 무조건 덮어쓰면 이후 정상 조사 결과까지 삭제할 수 있다. 실패 실행 이후 변경 commit 범위를 식별하고 필요한 파일만 복구하는 별도 restore commit이 필요하다.
- Discord에 이미 전달된 메시지는 Git revert로 회수할 수 없다.
- per-run 자동 snapshot 및 자동 restore workflow는 아직 구현·리허설되지 않았다. 코드 기준점은 확보했지만 운영 실행까지 포함한 rollback 체계는 미완성이다.

## 7. 다음 단계
1. 최신 main backup ref 및 feature backup ref 유지
2. PR 최신 base 통합 검증과 해당 merge result CI 확인
3. per-run snapshot/restore workflow를 mock으로 구현하고 복원 리허설
4. 복원 리허설 통과 후 merge commit 통합
5. 첫 운영 실행 전 snapshot, 실행 후 state/history/archive 무결성 검사
6. 이상 시 재실행을 중단하고 코드 revert와 필요한 데이터 restore commit 수행

이 보고서는 기술 감사이며 CRA 법적 적합성 또는 안전 인증을 의미하지 않는다.

## 8. 신규 운영 workflow rollback guard 구현
- production run.yml에 실행 전 snapshot branch, concurrency, post-run guard를 추가했다.
- guard는 baseline commit과 run commit의 parent 관계 및 remote main HEAD를 확인한다.
- 변경 commit은 state.json, history.json, research_archive/**만 허용한다.
- history 1건 append, 기존 history 보존, archive 1개 추가, 기존 archive 보존, history file 참조, state count를 검사한다.
- 검증 실패 시 remote main이 해당 run의 단일 child commit일 때만 data-only restore commit을 push한다. concurrent advance 또는 미push면 자동 복구하지 않는다.
- local bare remote integration tests 및 CI Run #43874801395 (86 passed, 1 xfailed) 성공.
- 실제 운영 workflow는 아직 실행하지 않았다. Discord 외부 전송은 회수할 수 없다.


## 9. main #162 최종 pre-merge 데이터 기준선
- immutable main SHA adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890 기준 state count=162, history=2,301, archive=2,301, history 참조 누락 0, tree truncated=false.
- backup safety/pre-merge-main-adf74ea가 정확히 같은 SHA를 가리킨다.
- feature head abee2a88f7e0bbfad0ad483c6b50cea63e26b871에 대한 PR CI Run #43875746973 성공(87 passed, 1 xfailed).
- guard는 missing state, symlink data path, empty archive를 감지해 안전한 조건에서만 restore commit을 생성하도록 보강됐다.
- production workflow 실제 실행은 아직 하지 않았다.
