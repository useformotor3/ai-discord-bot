# 최신 브랜치 통합 감사 스냅샷 — 2026-11-16

> 상세 분석 및 권장 절차는 `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`를 기준으로 한다.

## 기준 스냅샷
- 저장소: `useformotor3/ai-discord-bot`
- 운영 main HEAD: `3ebf6b977b0127291957ffb415dbdbc83b5b6d97` (Auto-archive #129)
- 작업 브랜치 HEAD: `0fe9912b5dbba29eeb3ebd9e9f2c16a42544f925`
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- compare: 204 ahead / 677 behind, diverged
- 확인일: 2026-11-16 (KST)
- base/main/feature recursive tree 모두 `truncated=false`.

## merge-base 기준 전체 tree 비교

| 항목 | merge-base | main | feature |
|---|---:|---:|---:|
| blob 파일 수 | 1,597 | 2,274 | 1,620 |
| research_archive | 1,592 | 2,269 | 1,592 |

- merge-base→main: 677개 추가(모두 archive), 삭제 0, `history.json` 및 `state.json` 수정.
- merge-base→feature: 22개 경로 추가(테스트·코드·문서), 삭제 0, `main.py` 수정.
- feature의 `state.json` 및 `history.json`은 merge-base와 같은 blob SHA다.
- main의 2,269 history 항목은 2,269 archive 파일을 참조하며 누락 참조는 0개.
- 677개 archive는 main이 분기 후 추가한 파일이며 feature가 삭제한 것이 아니다. 이 점을 직접 branch tree 비교와 혼동하지 않는다.

## 최신 운영 데이터
- main `state.json`: count=130, SHA `ede1a06952b0d2d67d5a67395d434dd886078d98`.
- main `history.json`: 2,269 entries, SHA `5c0142335e672197e3151404012ae9e0c7ef80c7`.
- main `research_archive/`: 2,269 files.
- main `.github/workflows/run.yml`: SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`, 미변경.

## 코드 검증 및 통합 판단
- P1-B2 recovery target allowlist를 `state.json`, `history.json`, `research_archive/*.md`로 제한.
- PR CI 및 main push 테스트 트리거 추가.
- Actions 43851438733: exact SHA, compileall, 70 passed / 1 xfailed.
- 3-way PR 통합 후보는 양호하나 실제 PR conflict check는 아직 수행하지 않았다.
- PR 생성·merge/rebase·운영 데이터/workflow 변경·실제 외부 서비스 호출 없음.
