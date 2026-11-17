# 2026-11-17 통합 사전 감사 및 CRA 근거 검증 보강

- 감사 시각: 2026-11-17 KST
- 저장소: `useformotor3/ai-discord-bot`
- 기준 브랜치: `main`
- 작업 브랜치: `feature/cra-source-grounding-atomic-2026-11-17`
- PR: [#3](https://github.com/useformotor3/ai-discord-bot/pull/3), Draft/open/unmerged
- 감사 기준 main HEAD: `9ad23da7136e3af7167048be51a0bf7f7c96d850`
- 감사 기준 작업 HEAD: `3b1c2f3481e9b2e89288cbec80dfbff3d854c8b5`
- merge-base: `0dde26ebac80a789c7a9d9e26560abad54606d32`
- compare: 116 ahead / 9 behind, diverged

## 1. 통합 상태

최신 원격 compare에서 작업 브랜치는 main보다 116 commits ahead, 9 commits behind다. 이전 PR 설명의 8 commits behind 및 앞선 세션의 113 ahead 수치는 구버전 스냅샷이므로 현재 기준으로 사용하지 않는다.

main의 `main.py` blob은 `f28dbc540d56b313f0648d77c58734d27eb95d1a`이며 CRA source/claim validator import가 없다. 작업 브랜치의 `main.py` blob은 `1bdb99745c11fd731f2006f8b03d48e1d2aebdff`이며 `cra_source.py` 및 `cra_claims.py`를 import하고 보고서 acceptance 전에 검증한다.

main의 `.github/workflows/tests.yml` blob `a20555f248088b4fe49c204b1cf68661b71b237f`는 기존 P1-B2 소스 SHA를 검사한다. 작업 브랜치 workflow blob `abfacde1ebd5734428fbf1b6cee4fc49a9c99af6`는 CRA 모듈·테스트의 SHA까지 검사한다. 따라서 main의 CI 성공 기록은 CRA branch 통합 검증으로 간주할 수 없다.

통합 전에는 main의 9개 후속 커밋(운영 자동 archive 포함 가능성)과 작업 브랜치의 코드/문서 변경을 immutable SHA 기준으로 분리 검토해야 한다. merge/rebase/force-push 및 main 변경은 이 감사에서 수행하지 않았다.

## 2. 현재 격리 검증

- 이전 feature head `8e19f33fda5f963f5ef95b640bf134ee5bddb084`: Isolated CI Run #274 success, EUR-Lex read-only Canary Run #93 success.
- claim quote-to-locator 보강 후 workflow Run #279 (ID `44001952395`) 및 EUR-Lex read-only Canary Run #95 (ID `44001952398`)는 감사 시점 queued/pending이었다. 결과 확인 전 성공으로 간주하지 않는다.
- 실제 Gemini API 호출 0회. 실제 Discord 전송 및 production workflow 실행 없음.

## 3. 추가로 발견한 validator 결함과 수정

기존 `cra_claims.py`는 지정 source 전체에서 quote가 존재하는지만 확인했다. Article locator가 존재하고 quote가 다른 Article에 있어도 통과할 수 있는 교차 조항 false-positive가 가능했다.

보강:
- `_quote_is_in_locator_scope()`를 추가해 직접 인용문이 지정 Article 또는 Annex의 범위 안에 있는지 검사한다.
- 지정 Article/Annex 외부의 인용문을 거부하는 회귀 테스트를 추가했다.
- workflow exact blob pin을 새 validator 및 테스트 SHA로 갱신했다.

변경:
- validator commit: `0706df175d23cef3f40eeccebb96a08a728bafec`
- regression test commit: `fee65c436a0a112f6415d01aca35a9ba7c72a83c`
- workflow pin commit: `3b1c2f3481e9b2e89288cbec80dfbff3d854c8b5`
- validator blob: `8a3302179c9234f085d7b66b2e9bbf2d22d6f71d`
- test blob: `c7c45cb6d23eb3ddae5e25ccbfc88f15865f7247`

제한: 현재 보강은 Article/Annex 범위까지다. Article 내 특정 paragraph/point의 정확한 경계와 quote의 의미상 적합성까지 증명하지 않는다. 단순 텍스트 추출에서 다른 Article 참조가 heading처럼 인식되면 유효 인용을 보수적으로 거부할 수도 있으므로 false-negative 테스트도 추가해야 한다. 법률 해석 및 제품 적용성은 여전히 사람 검토 대상이다.

## 4. Official Journal / corrigenda 독립 대조

EUR-Lex consolidated page는 자체적으로 documentation tool이며 법적 효력이 없고, authentic versions는 Official Journal에 게시된 관련 act 및 corrigenda라고 명시한다.

공식 EUR-Lex 대조 결과:
1. 기본 법령: Regulation (EU) 2024/2847, OJ L 2024/2847, 20.11.2024.
2. Corrigendum 2024-12-05, CELEX `32024R2847R(01)`: 제목에서 “No 2019/1020” 표기 중 “No” 삭제 정정.
3. Corrigendum 2025-07-02, CELEX `32024R2847R(02)`: Article 64(10) 도입부의 “paragraphs 3 to 9”를 “paragraphs 2 to 9”로 정정.
4. Corrigendum 2025-10-17, CELEX `32024R2847R(04)`: Article 67의 Regulation 참조 번호 “69”를 “72”로 정정.

공식 링크:
- 기본 법령 OJ: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- 2024-12-05: https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2024-12-05/oj/eng
- 2025-07-02: https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2025-07-02/oj/eng
- 2025-10-17: https://eur-lex.europa.eu/eli/reg/2024/2847/corrigendum/2025-10-17/oj/eng

현재 source fetch gate는 consolidated text에 세 날짜가 존재하는지 확인하지만, 세 corrigenda의 개별 Official Journal 문서를 직접 fetch해 정정 대상 문구와 corrected wording까지 대조하지는 않는다. 따라서 “정오표 날짜 인덱스 확인”과 “정오표 내용 검증 완료”를 구분해야 한다. 다음 우선 작업은 세 corrigenda 원문을 source pack에 추가하고 각 문서의 식별자·대상 조항·for/read 문구를 테스트하는 것이다.

## 5. 다음 실행 순서

1. Run #279와 Canary #95 완료 여부 및 상세 로그 확인. 실패 시 원인 수정 후 재실행.
2. 세 공식 corrigenda 문서를 독립 source로 수집하고 corrected wording을 machine-check.
3. quote-to-locator 검증을 paragraph/point 범위까지 확장하되, false-positive와 false-negative fixture를 함께 검증.
4. main의 9개 후속 커밋 및 운영 state/history/archive 불변성을 immutable SHA 기준으로 대조.
5. 최신 main을 기준으로 별도 integration branch를 만들고 feature 변경을 단계적으로 이식한 뒤 exact SHA/compile/full pytest/CI 수행.
6. 통합 검증이 완료되기 전까지 PR #3 Draft 유지, main 병합 및 production workflow 실행 보류.
7. Gemini live canary는 project billing tier 및 Free Tier 데이터 사용 조건이 확인되지 않았으므로 계속 미실행.

## 6. 안전 경계

- main, 운영 `.github/workflows/run.yml`, state/history/archive 미변경.
- merge/rebase/force-push 및 production execution 없음.
- safety refs 및 기존 PR을 삭제하거나 이동하지 않았다.
- 이 문서는 통합 승인이나 법률 적합성 결론이 아니다.

## 7. 수정 후 재검증 — 2026-11-17

초기 Article/Annex scope helper 구현에서 정규식 escape를 이중 처리한 결함이 있었다. 그 결과 CI Run #279는 **25 failed, 92 passed, 1 xfailed**로 실패했다. 실패 원인은 회귀 테스트와 main 통합 fixture의 quote를 locator scope 안에서 찾지 못한 것이며, 이를 성공으로 숨기지 않고 job log에서 원인을 확인했다.

정규식 escape를 수정하고 workflow exact SHA pin을 갱신한 후:
- correction commit: `7882aaf890e933dff988a0891f1a98b6cb3abeee`
- exact pin update commit: `784c41a90bd77dd5776c1637f6abe646452e7175`
- Isolated CI Run #294 (ID `44002223181`): **117 passed, 1 xfailed**; exact source SHA, compileall, full pytest 모두 성공.
- EUR-Lex read-only Canary Run #101 (ID `44002223011`): success.
- 이전 실패 Run #279는 실패 이력으로 보존한다. 수정 후 성공이 과거 실패를 지우는 것은 아니다.

문서 및 로그 갱신 전 마지막 원격 compare 스냅샷은 main `83bc2430842413080e73bc5b98a8a82c45d03909`, feature 최신 검증 head `784c41a90bd77dd5776c1637f6abe646452e7175`, 125 ahead / 10 behind, diverged였다. main의 자동 archive가 계속 전진하므로 다음 통합 단계 직전에 다시 비교한다.

PROJECT_LOG.jsonl은 UTF-8 원문 전체를 보존해 빈 행을 제거하고 한 줄당 JSON 객체 형식으로 정리했다. 현재 로그 재검증은 다음 문서/코드 commit 이후 다시 수행한다.

## 8. 개별 Official Journal corrigenda 수집 구현 및 실시간 확인 — 2026-11-17

날짜 인덱스 확인에 그치던 기존 source gate를 보강해 CRA 기본 법령의 영어 Official Journal corrigenda 3건을 각각 독립 source로 추가했다.

- 2024-12-05 / OJ 2024/90780 / CELEX 32024R2847R(01): 제목의 “No 2019/1020”을 “2019/1020”으로 정정.
- 2025-07-02 / OJ 2025/90555 / CELEX 32024R2847R(02): Article 64(10)의 “paragraphs 3 to 9”를 “paragraphs 2 to 9”로 정정.
- 2025-10-17 / OJ 2025/90828 / CELEX 32024R2847R(04): Article 67의 참조 번호 “69”를 “72”로 정정.

각 공식 ELI URL을 직접 GET하고 HTTPS/EUR-Lex host, 최소 본문 길이, 대상 조항 및 for/read 양쪽 문구를 fail-closed로 확인한다. source manifest와 Gemini prompt에도 개별 문서 ID·URL·버전이 포함된다.

실제 EUR-Lex read-only Canary Run #115 (ID `44003013739`) success:
- 전체 source pack visible text 245,502자.
- CRA 통합본 196,076자.
- corrigenda: 7,583자 / 8,318자 / 8,179자.
- 기존 후속 법령 3건도 모두 수집.
- Gemini/Discord/production workflow 호출 없음.

추가 테스트 결과:
- source 확장 직후 CI #314: 8 failed, 109 passed, 1 xfailed. source manifest 증가로 Discord 분할 청크 수가 2→3으로 증가했는데 기존 테스트 기대값이 갱신되지 않은 문제.
- 다음 CI #319: 2 failed, 115 passed, 1 xfailed. 429 재시도 후 chunk 간 대기 횟수 기대값이 한 건 부족했다.
- 테스트 기대값을 실제 3청크 전송/대기 정책에 맞게 보강하고 workflow exact SHA를 갱신했다.
- 최종 CI #323: **117 passed, 1 xfailed**, exact source SHA / compileall / full pytest 성공.

이제 source gate는 날짜 인덱스뿐 아니라 개별 corrigenda의 정정 대상과 정정 문구까지 확인한다. 다만 문구 존재 검사는 법률 해석, 문맥상 적용 여부, 제품 적합성 판단을 대체하지 않는다.

## 9. Latest-main integration branch result — 2026-11-17

Main advanced through 13 auto-archive commits (#6–#18) after the original merge-base. A compare of main HEAD `92477fce1350cccb90a799f061b506461e9caff1` against the prior integration base `48521f877c5db114e9066180f5a2f721a26222c4` showed exactly three changed paths: `history.json`, `state.json`, and archive #18. The 13 commits were archive-only.

Integration sequence:
- PR #5 merged latest main into integration branch: `308bf4adc181ee6be5d866f3b4cd5ddf54ccf6cd`.
- PR #4 merged CRA feature into integration branch: `df854af3abc8c2aaf2e56381b0dcacfdbbd6c662`.
- PR #6 opened as a validation PR to main, run to completion, then returned to Draft. It remains unmerged.

Protected blob checks after integration:
- state.json: main and integration both `1358aae57047127462dfce7938af99843bebf8fc`.
- history.json: main and integration both `af79c5608a9789695e8f155ad0a91a260de7304e`.
- archive #18: main and integration both `f986f2f2db5f74ca8dd072deb2fe90e013b4a63c`.

Merged-tree verification:
- CI Run #366: **117 passed, 1 xfailed**, exact source SHA checks, compileall and full pytest passed.
- EUR-Lex read-only Canary #134: success; seven sources, 245,502 visible-text characters, including all three individual English corrigenda and their required wording markers.
- No production Gemini/Discord call and no main modification.

## 10. Main archive #19 sync and correction — 2026-11-17

Main advanced one archive-only commit after the #18 integration snapshot. The commit changed only `history.json`, `state.json`, and `research_archive/2026-11-17_113532369725_9840a64e.md`. PR #7 synchronized it into the integration branch (merge commit `01f4f797ac2689fcda425b02304685805272fd24`).

Main/integration protected blob comparison:
- state.json: `743ee4379421390c85203000cffe2fa0bc43a239`
- history.json: `fee7cbe25f5a4881af35124c8a984f8c8d1a9b6d`
- archive #19: `3d90ed95b47d6275e4d98d7c18cfbc5246ffa4e4`

Archive #19 correction report: `reports/CRA_CORRECTION_REPORT_19_2026-11-17.md`. The original archive remains unchanged. The corrected legal locators are Annex I Part I (2)(l) for logging/monitoring, (2)(c) for security updates, and (2)(h) for availability.

## 11. Main archive #13 correction — 2026-11-17

Original archive #13 blob: `7523b68c1537b6ed4d2de197eeb6e5bd4698ea2e`. Correction report: `reports/CRA_CORRECTION_REPORT_13_2026-11-17.md`.

Findings: Article 11 was incorrectly used as the manufacturer vulnerability-handling/CVD provision; Annex I Part II numbering and quotations were not the enacted OJ wording; anonymous intake and simultaneous publication were overstated; all servo drives were incorrectly treated as Important Class I/II. Correct mapping: Article 13 manufacturer duties and risk assessment; Annex I Part II (1)–(8) vulnerability handling; Article 14 mandatory reporting; Annex III classification only after product-category analysis. Original archive remains unchanged.
