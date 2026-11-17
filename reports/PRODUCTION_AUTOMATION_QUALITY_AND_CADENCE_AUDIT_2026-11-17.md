# 운영 자동화 품질·실행 주기 감사 및 개선 — 2026-11-17

## 1. 발견한 문제

운영 main의 최근 아카이브 #33–#38을 직접 확인했다. #33, #35, #37, #38은 취약점 처리/무상 보안 업데이트/지원기간 주제가 중복됐고, #36은 취약점·심각한 사고 신고 타임라인을 일부 혼합했다. #34는 사용자 정보·지침을 다루었으나 Annex II와 Annex VII, 제품 분류를 혼합했다.

기존 `run.yml`은 `repository_dispatch: run-bot`와 `workflow_dispatch`만 허용했고 내부 `schedule`은 없었다. 운영 main의 최근 자동 archive commit들이 약 5분 간격으로 반복 생성된 것은 외부 dispatch가 반복된 정황과 일치한다. workflow에 schedule이 없으므로 5분 주기의 발생원은 외부 dispatcher이며, 해당 외부 설정은 이 저장소에서 직접 변경할 수 없다.

또한 기존 `validate_research_report`는 최소 길이·섹션·오류 문구를 확인했지만 공식 EUR-Lex 링크와 주제 중복을 검증하지 않았다.

## 2. 실제 개선

### PR #10 — 이미 main에 병합
- PR: https://github.com/useformotor3/ai-discord-bot/pull/10
- merge commit: `2e583f5c7b24743fbb1bd7d375643e314cf3115d`
- CI Run #455: **101 passed, 1 xfailed**; exact blob SHA, compileall, 전체 pytest 통과.
- CRA 보고서 검증에서 EUR-Lex Regulation (EU) 2024/2847 공식 링크가 없으면 거부.
- 최근 30개 원문 archive의 주제어를 비교해 중복 주제면 Discord 전송, archive 생성, state/history 변경 및 Git 저장 전에 정상 no-op 처리.
- 최근 5개였던 프롬프트 이력 참고 범위를 최근 15개로 확대.
- 기존 state/history/archive는 byte-for-byte 보존.

### 별도 PR — 실행 cadence 개선 (현재 작업 브랜치)
- 브랜치: `fix/production-cadence-2026-11-17`
- 외부 5분 간격 repository_dispatch를 운영 workflow trigger에서 제거.
- 내부 GitHub Actions schedule을 매 3시간 UTC 정각(한국시간 매시간 정각)으로 전환하고 workflow_dispatch는 유지.
- 운영 동시성 `cra-production-run`, `cancel-in-progress: false` 및 실행별 immutable pre-run checkpoint/operational guard/pruning을 유지.
- 테스트 workflow가 run.yml 변경 PR에도 실행되도록 경로 필터를 보완하고 cadence 회귀 테스트를 추가.
- main.py 조사 프롬프트에 공식 OJ 링크, 실제 확인한 원문만 직접 인용, 신규 주제 없으면 억지 생성 금지 규칙을 추가.

외부 dispatcher의 설정 자체를 이 저장소에서 중단할 수는 없지만, workflow에서 해당 event를 더 이상 구독하지 않으므로 merge 후에는 5분 repository_dispatch가 운영 workflow를 실행하지 않는다. 내부 3-hourly schedule만 운영 실행을 시작한다.

## 3. 최근 보고서 #33–#38 법령 감사

각 원본은 수정·삭제하지 않고 별도 정정 보고서로 보존했다.

| 원본 | 정정 문서 | 주요 정정 |
|---|---|---|
| #33 | [정정 #33](CRA_CORRECTION_REPORT_33_2026-11-17.md) | Article 13(8)/(9), Annex I Part II (2)/(7)/(8), 지원기간 5년 예외, 업데이트 10년 보유 |
| #34 | [정정 #34](CRA_CORRECTION_REPORT_34_2026-11-17.md) | Article 13(18)/(19), Annex II 사용자 지침과 Annex VII 기술문서 구분 |
| #35 | [정정 #35](CRA_CORRECTION_REPORT_35_2026-11-17.md) | Article 10/11 오인용, Article 13 제조사 의무, Article 14 신고 트리거 분리 |
| #36 | [정정 #36](CRA_CORRECTION_REPORT_36_2026-11-17.md) | vulnerability와 severe incident의 서로 다른 final-report clock, 초안 인용 제거 |
| #37 | [정정 #37](CRA_CORRECTION_REPORT_37_2026-11-17.md) | Article 10/11 오인용, Annex I Part II 번호/문언, Annex III 분류 과장 |
| #38 | [정정 #38](CRA_CORRECTION_REPORT_38_2026-11-17.md) | 지원기간 예외, 무상 업데이트 예외, 10년 업데이트 이용 가능성, 제품 등급 과장 |

### 법령 원문 교차 확인

EUR-Lex 최종 Official Journal 원문을 확인했다.
- Article 13(8): support period, 최소 5년. 제품 예상 사용기간이 5년 미만이면 그 예상 사용기간에 맞춘다.
- Article 13(9): 지원기간 중 제공된 각 security update는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능해야 한다.
- Annex I Part II (2): 취약점을 지체 없이 처리·시정, 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리.
- Annex I Part II (7): 취약점의 적시 수정/완화를 위한 안전한 업데이트 배포 메커니즘.
- Annex I Part II (8): 보안 업데이트의 지체 없는 무상 배포. 맞춤형 제품과 business user의 달리 합의한 예외.
- Article 14(2)(c): actively exploited vulnerability final report는 corrective/mitigating measure available 후 14일 이내.
- Article 14(4)(c): severe incident final report는 incident notification 제출 후 1개월 이내.
- Annex III는 열거 카테고리다. 산업용 서보 드라이브 전체를 자동으로 Class I/II로 분류할 수 없다.

공식 출처: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

## 4. 운영 안전성

- 기존 원본 아카이브 #33–#38, state.json, history.json은 변경하지 않았다.
- PR #10 merge 전 최신 production run #44015895884는 success였고, archive #38 저장까지 확인했다.
- PR #10 CI는 테스트 전용이다. Gemini/Discord 실 API를 호출하지 않았다.
- cadence PR은 아직 main에 병합하지 않았다. PR CI 통과 및 main 최신화 후 병합하고, 첫 3-hourly run에서 checkpoint, guard, prune 및 state/history/archive 참조 무결성을 재확인한다.
- hourly schedule이 운영 run 빈도를 낮추는 조치이며, 향후 필요하면 운영 데이터 추세를 근거로 조정한다.

## 5. 한계 및 다음 단계

- 중복 주제 탐지는 주제어 기반 휴리스틱이며 법적 정확성을 증명하지 않는다. false positive/negative를 운영 로그로 검토해야 한다.
- EUR-Lex URL 존재 여부는 출처 링크 유무만 확인한다. 인용문이 실제 원문과 일치하는지 자동 증명하지 않는다. 별도 원문 대조 및 정정 감사가 계속 필요하다.
- cadence 변경 merge 후 첫 3회 hourly run을 관찰한다. 실패가 발생하면 run/job log와 단계별 원인을 확인하고, 반복 원인이면 수정 PR을 추가한다.
- 다음 핵심 산출물: CRA 통합 한국어 보고서, 요구사항 추적표, SIL 3 서보 드라이브 벤치마킹 보고서, 하드웨어 블록 설계. CRA와 기능안전의 추적성은 분리 유지한다.

## 6. Gemini Free Tier quota 장애 후속 — 2026-11-17

운영 Run `44016487535`의 job log에서 primary model의 Free Tier daily request limit 20 초과(429 RESOURCE_EXHAUSTED), fallback model의 503 UNAVAILABLE, EUR-Lex 링크 누락을 확인했다. 기존 5분 dispatch가 이 상황에서 재시도와 workflow 실패를 반복시켰다.

cadence PR은 내부 schedule을 3시간마다(8회/일)로 조정하고 모델별 최대 2회 시도로 제한한다. 이론상 모델별 16회/일로 20/day 제한보다 낮다. 429/503은 동일 모델 재시도 없이 fallback으로 이동하고, quota/일시 장애/품질 거부로 유효 보고서를 얻지 못하면 경고를 남기고 no-op 종료한다. 이 경우 Discord 전송·아카이브·state/history 변경은 없다. 인증/설정 등 복구가 필요한 미분류 오류는 실패 종료한다.

## 7. Failure-path recovery and persist-before-delivery — merged 2026-11-17

PR #12: https://github.com/useformotor3/ai-discord-bot/pull/12
- Merge commit: `bef260a29481320de3eae9cafe4a6f907e38ead0`
- CI Run #470: **105 passed, 1 xfailed**.
- The production workflow now runs the operational guard whenever the immutable pre-run checkpoint was successfully created, even if dependency installation or `main.py` fails.
- If uncommitted state/history/archive data is dirty, the guard restores tracked files from the checkpoint and removes only safe, untracked top-level archive Markdown files. It reports failure after restoring, so the checkpoint is retained for investigation.
- If a local operational-data commit was created but not pushed, and remote main is still exactly the baseline, the guard resets only the ephemeral local checkout to baseline. It does not push or force-push.
- If remote main advanced independently, the guard refuses automatic overwrite. If an invalid single-child commit was already pushed, the existing data-only rollback commit path remains.
- Old checkpoints are pruned only when the guard itself succeeds. Failed recovery keeps the checkpoint.
- Discord delivery now happens after archive/state/history commit and push. A Git push failure cannot produce a Discord message for an unpersisted report.

## 8. Final main status after PR #10–#12

- Main merge head: `bef260a29481320de3eae9cafe4a6f907e38ead0`.
- PR #10 CI #455: 101 passed, 1 xfailed.
- PR #11 CI #467: 103 passed, 1 xfailed.
- PR #12 CI #470: 105 passed, 1 xfailed.
- Production schedule: `0 */3 * * *` UTC (every three hours); manual workflow_dispatch retained; external repository_dispatch no longer subscribed.
- Model calls: max 2 attempts per model per scheduled run; 429/503 stops same-model retries and falls back; quota/service/quality rejection with no valid report is a clean no-op; authentication/configuration failures remain visible failures.
- Last verified production data snapshot after quota failure: state count 38, history 2,431 entries, state blob `da086ea3ffb7ef0c76d7fa03a58e13a24aa8fe34`, history blob `b9ea42fa437b2b3a5728db5d125d287fb746b46b`. No operational data changed in the quota-failed run.
- Actual live Gemini/Discord execution after these changes is not yet verified. Observe the first three scheduled production runs and record each workflow result, quota response, guard result, checkpoint pruning and state/history/archive hash comparison.

## 9. CRA archive #1–#38 correction coverage

The main documentation integration branch now contains correction reports #1–#38:
- #1–#4 were already on main.
- #5–#21 were copied from the previously source-audited integration branch without modifying originals.
- #22–#32 were newly checked against the final EUR-Lex Official Journal and corrected.
- #33–#38 were already corrected in the preceding main integration.

Master index: `CRA_CORRECTION_INDEX_2026-11-17.md`.

High-impact corrections include Article 10/11/24 misidentification, Article 31/Annex VII technical documentation vs Annex II user instructions, Article 13(8)/(9) support period vs update availability, Annex I Part I vs Part II, CVD vs mandatory/voluntary reporting, Article 14 separate clocks, Annex III classification overclaims, and implementation choices falsely presented as verbatim CRA obligations. Original archive files remain unchanged.

## 10. Final CRA correction integration

PR #14 merged as `6994e4828a03482713f7990c7f82036bacfe4772`; CI #474: **105 passed, 1 xfailed**. All 38 correction files are present on main and the master index is `reports/CRA_CORRECTION_INDEX_2026-11-17.md`. Original archive blobs for #22–#32 were re-fetched and match their pre-correction hashes. State/history blobs remain unchanged. Draft PRs #3 and #6 were closed as superseded after their source-gate and correction content had been integrated through PRs #10–#14.
