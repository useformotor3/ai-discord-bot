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
