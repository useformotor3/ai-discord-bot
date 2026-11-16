# 최신 브랜치 통합 감사 스냅샷 — 2026-11-16

## 기준
- 저장소: `useformotor3/ai-discord-bot`
- 작업 브랜치: `test/failure-path-fixtures-2026-11-14`
- 작업 브랜치 HEAD: `227e3298066af4bda83fb0713fc1d57c749ee8c6`
- 운영 main HEAD: `036334dd2665752c2e6ddb024001771cff4064c5`
- 공통 조상: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`
- 작업 브랜치 기준 문서 base: `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 확인일: 2026-11-16 (KST)

## 분기 수치
- 작업 브랜치 기준 base 대비: 44 ahead / 0 behind
- 작업 브랜치와 main 비교: 155 ahead / 660 behind
- 상태: diverged. merge/rebase/PR merge 금지.

## 전체 tree 비교
GitHub compare API의 변경 파일 목록은 최대 300개이므로 전체 변경 목록으로 사용하지 않았다. 양쪽 recursive Git tree를 조회하고 `truncated=false` 및 SHA를 확인했다.

| 항목 | merge-base | main |
|---|---:|---:|
| tree entries | 1,600 | 2,260 |
| main 고유 추가 | — | 660 |
| 삭제 | — | 0 |
| 변경 파일 | — | 2 |

- main 고유 추가 660개는 모두 `research_archive/`의 자동 생성 보고서다.
- 변경 파일은 `history.json`, `state.json`이다.
- tree SHA: merge-base `11470d4a1c6cf32203afd08c72da7c61c7bb03df`, main `044bd87d4207ddf13f184ce8bdd9cf31dda91fa9`.

## 운영 데이터
- main `state.json`: blob SHA `97192797b472e159a9e83845cb9984471df3cec4`; date `2026-11-16`, count `113`, last_health_check `2026-11-16T09:20:40.126333`.
- main `history.json`: blob SHA `e1e438305ac9d5930f523fcb90105bb50001c2ac`; 2,252개 객체 항목, 마지막 날짜 2026-11-16.
- 운영 데이터는 실제로 계속 갱신되고 있다. 작업 브랜치 파일로 덮어쓰지 않는다.

## 코드 및 workflow
- 작업 브랜치 `main.py`: `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 운영 main `main.py`: `86a7731aad5de8d75581fc953bcea2c44adf2f2b`.
- 운영 `.github/workflows/run.yml`은 공통 조상과 동일한 SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- P0/P1-A/P1-B1 개선 코드는 작업 브랜치에만 존재하며 운영 main에 배포되지 않았다.

## 결론
1. 자동 조사·아카이브 운영은 main에서 계속 실행 중인 흔적이 확인된다(최신 기록 #113, state count 113).
2. 신뢰성 개선(P0/P1-A/P1-B1)은 작업 브랜치에서 구현·검증됐지만 운영 main에는 아직 반영되지 않았다.
3. 운영 데이터 660개 archive 및 history/state 변경을 보존하는 통합 전략이 필요하다.
4. 코드·문서 통합과 운영 데이터 migration을 분리한다.
5. 운영 main, state/history/archive, workflow를 변경하지 않았고 merge/rebase/PR merge도 하지 않았다.

## 한계
이 감사는 Git ref/tree/blob과 데이터 구조를 확인했다. 보고서의 CRA 법적 정확성, 출처 진위, 기능안전 적합성은 평가하지 않았다. 테스트를 재실행하지 않았으며 새 PASS를 주장하지 않는다.
