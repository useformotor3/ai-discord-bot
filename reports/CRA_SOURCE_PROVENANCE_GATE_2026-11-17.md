# CRA 공식 원문 출처검증 gate — 설계 및 구현 기록

- 작성일: 2026-11-17 (KST)
- 저장소: useformotor3/ai-discord-bot
- 작업 브랜치: feature/cra-source-grounding-atomic-2026-11-17
- Draft PR: https://github.com/useformotor3/ai-discord-bot/pull/3
- 기준 main SHA: 0dde26ebac80a789c7a9d9e26560abad54606d32
- 복구 브랜치: safety/pre-cra-source-grounding-2026-11-17

## 1. 문제와 원인

2026-11-17 생성 CRA 보고서 4건을 공식 EUR-Lex 원문과 대조한 결과, 조항 번호 혼동, 법적 의무와 엔지니어링 권고 혼동, 원문 인용 불일치가 확인됐다. 기존 main.py는 Gemini 일반 텍스트 생성 결과의 길이·필수 섹션·오류 문구만 검사했다. 공식 URL, 조항 locator, 직접 인용을 실제 원문과 대조하지 않았다.

## 2. 비용 및 출처 전략

Gemini 3 계열 Google Search Grounding은 현재 Gemini API 가격표상 Free tier에서 사용할 수 없는 기능이므로 무료 운영의 필수 의존성으로 삼지 않았다. 대신 EUR-Lex 공식 CRA HTML을 직접 조회한다.

- 공식 EUR-Lex consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120
- 공식 원문 페이지에는 다음 CRA corrigenda가 표시된다.
  - 2024-12-05
  - 2025-07-02
  - 2025-10-17
- 구현은 위 세 날짜가 모두 본문에 존재하는지 확인한다. 하나라도 빠지면 원문 버전의 완전성을 확인하지 못한 것으로 보고 fail-closed한다.
- 주의: EUR-Lex consolidated text는 documentation tool이다. 법적 효력은 Official Journal에 게시된 정본 및 공식 corrigenda에 있다. 통합본만으로 법적 결론을 확정하지 않는다.

## 3. 처리 흐름

1. cra_source.py가 고정된 EUR-Lex HTTPS URL에 GET 요청한다.
2. HTTP 오류, 20초 read timeout, 비 EUR-Lex redirect, 지나치게 짧은 본문은 실패 처리한다.
3. HTMLParser로 visible text를 추출하고 공백만 정규화한다. 원문 단어와 문장부호는 유지한다.
4. 본문에 알려진 corrigenda 날짜 3개가 모두 있는지 확인한다.
5. 원문 확보가 성공한 경우에만 main.py가 Gemini를 호출한다.
6. 프롬프트에 공식 URL·source version·원문 텍스트를 제공한다. 모델은 해당 원문 밖의 표준·가이드·관행을 CRA 법적 의무로 추가하지 않도록 제한한다.
7. 생성 결과는 필수 섹션, 공식 URL, source version, Article/Annex locator, 50자 이상 큰따옴표 직접 인용을 검사한다.
8. 직접 인용문은 수집한 원문 텍스트에 실제 포함되는지 대조한다.
9. 검증 실패가 재시도 한도를 넘으면 보고서 성공 처리·Discord 전송·Git 저장을 중단한다.

## 4. 구현 파일

| 파일 | 변경 |
|---|---|
| cra_source.py | 공식 원문 fetch, host/version/corrigenda 확인, 최소 provenance validator |
| main.py | 원문 fetch 후 Gemini 실행, source-aware validator, 초안 상태 표시 |
| tests/conftest.py | source HTTP mock 경계 추가 |
| tests/test_main_characterization.py | 정상·HTTP 503·비공식 redirect·corrigenda 누락·quote mismatch 테스트 |
| tests/test_mock_infrastructure.py | 외부 호출 capture 기대값 보강 |
| .github/workflows/tests.yml | source/test blob SHA 고정, PR CI |

## 5. 검증 결과

- CI Run #79: 97 passed, 5 failed, 1 xfailed. 실패 원인은 테스트 간 requests module cache로 source mock이 현재 테스트에 연결되지 않은 것이었다.
- HTTP import를 함수 호출 시점으로 이동해 mock 격리를 보완했다.
- CI Run #83: 102 passed, 1 xfailed.
- corrigenda version check 및 archive metadata 추가 후 CI Run #93: **103 passed, 1 xfailed**.
- Run #89: https://github.com/useformotor3/ai-discord-bot/actions/runs/43986520995
- blob SHA 검증, compileall, 전체 pytest가 성공했다. 최신 CI Run #111: 103 passed, 1 xfailed. Evidence: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987722348.
- 별도 read-only canary Run #5는 실제 EUR-Lex HTTPS endpoint를 호출해 196,076자 visible text와 corrigenda 3개 날짜를 확인했다. Evidence: https://github.com/useformotor3/ai-discord-bot/actions/runs/43987730194.
- canary는 EUR-Lex GET만 수행했으며 Gemini/Discord/production workflow/운영 Git write는 호출하지 않았다.

## 6. 검증 한계 및 위험

이 gate는 다음만 최소 확인한다.

- 공식 도메인 HTTPS URL로 응답을 받았는지
- 응답 본문에 알려진 정오표 인덱스 날짜가 포함되는지
- 보고서가 source URL/version을 기재하는지
- Article/Annex locator가 원문에서 확인되는지
- 50자 이상 직접 인용문 중 적어도 하나가 원문에 그대로 존재하는지

다음은 보증하지 않는다.

- 보고서의 모든 사실 주장과 모든 문장이 인용 근거로 뒷받침되는지
- 해당 조항 해석이 법적으로 정확한지
- 서보 드라이브 제품이 CRA 적용 범위·제품 등급·적합성 평가 절차에 해당하는지
- IEC 표준의 유료 전문 요구사항과 일치하는지
- 제품 안전·기능안전·실시간 제어 영향이 적절히 평가됐는지
- 공식 관보 정본과 통합본/정오표의 모든 차이를 자동 판별하는지

EUR-Lex 통합본은 documentation tool이며 법적 효력은 Official Journal(관보) 정본 및 공식 corrigenda에 있다. Validator는 이 주의사항이 보고서에 없으면 거부한다.\n\n따라서 모든 생성 보고서는 **“EUR-Lex 원문 인용 대조 통과 / 법률 해석·제품 적용성 미검증 초안”**으로 표시한다. 사람의 독립 검토 없이 최종 적합성 결론으로 사용하지 않는다.

## 7. 안전 및 롤백

- 운영 main, .github/workflows/run.yml, state/history/archive를 변경하지 않았다.
- 기준 main SHA: 0dde26ebac80a789c7a9d9e26560abad54606d32.
- 복구 브랜치 safety/pre-cra-source-grounding-2026-11-17는 해당 기준 SHA를 보존한다.
- 코드 및 테스트 변경은 Draft PR #3에만 존재한다.
- 운영 Gemini/Discord 실행, production workflow dispatch, main 병합은 하지 않았다.
- 변경 취소가 필요하면 PR을 닫고 작업 브랜치를 폐기하면 된다. main에는 되돌릴 변경이 없다.

## 8. 다음 단계

1. [완료] 운영과 분리된 canary 환경에서 EUR-Lex HTML endpoint의 실제 HTTP 상태·최종 URL·본문 길이·정오표 날짜를 확인했다.
2. 보고서의 각 법적 주장마다 개별 Article/Annex/point와 근거 인용을 연결하는 claim-to-evidence 구조로 확장한다.
3. 원문 hash/version 변화 및 새 corrigenda 감지 테스트를 추가한다.
4. 검증 불확실 또는 인용 대조 실패 보고서를 게시하지 않고 검토 큐로 보내는 방식을 설계한다.
5. 그 후에만 production workflow 적용 여부를 판단한다.


## 9. 공식 후속 법령 source pack 확장 — 2026-11-17

초기 구현은 CRA 통합본 한 건만 가져왔기 때문에, 통합본 밖에서 CRA의 범위·적용시기·신고 절차에 영향을 줄 수 있는 후속 법령을 놓칠 수 있었다. 이를 보완하기 위해 EUR-Lex 공식 HTML에서 아래 3건을 별도 원문으로 수집하도록 확장했다.

| 공식 법령 | source pack에서 확인하는 관련성 | 적용상 주의 |
|---|---|---|
| Regulation (EU) 2025/327, Article 104 | EHR 시스템 관련 EHDS 규정과 CRA Article 32(5a)의 연결 | 2027-03-26 적용 예정인 후속 변경으로 기록하고, 일반 산업용 서보 드라이브 의무로 확대하지 않는다. |
| Commission Delegated Regulation (EU) 2025/1535 | Regulation (EU) No 168/2013 적용 제품의 제한적 CRA 범위 제외 | 특정 L-category 제품 범위와 L1e 예외를 구분한다. 산업용 서보 드라이브에 자동 적용하지 않는다. |
| Commission Delegated Regulation (EU) 2026/881 | CRA Article 16에 따른 통지 전파 지연 조건 | Article 14의 기본 취약점·중대 사고 신고 시한과 혼동하지 않는다. |

공식 원문:
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R0327
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R1535
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R0881

이 세 법령의 수집 성공은 서보 드라이브에 적용된다는 법률 결론이 아니다. 실제 제품 분류·의도된 용도·관련 EU 법령 범위를 별도 검토해야 한다.

## 10. 확장 source pack 검증 결과

- Isolated CI Run #154: **103 passed, 1 xfailed**. 정확한 source blob SHA 검증, compileall, 전체 pytest 성공. [실행 로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859144).
- EUR-Lex read-only canary Run #29: **success**. 네 공식 법령 HTML에서 source pack에 전달된 추출 텍스트 220,715자 확인(2025/327은 관련 Article 104 발췌). 각 원문 HTML의 전체 visible text는 CRA 통합본 196,076자, Regulation 2025/327 394,354자, Delegated Regulation 2025/1535 6,246자, Delegated Regulation 2026/881 15,284자. [실행 로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43995859223).
- 기존 CRA 통합본의 정오표 인덱스 3개 날짜(2024-12-05, 2025-07-02, 2025-10-17)도 다시 확인했다.
- 검증은 공개 EUR-Lex GET과 mock 기반 CI다. Gemini/Discord/운영 workflow 호출은 하지 않았다.

## 11. 현재 상태 및 다음 검증

- 코드 변경은 Draft PR #3에만 존재한다: https://github.com/useformotor3/ai-discord-bot/pull/3.
- PR head: d564e91faf616d95c0ab91c269fcfc3315413c50. 기준 main: 0dde26ebac80a789c7a9d9e26560abad54606d32.
- 2026-11-17 현재 main은 자동 아카이브 #10으로 별도 전진했다. 이 PR은 해당 변경을 덮어쓰지 않았으며 main에 병합하지 않았다.
- 아직 미완료: 모든 보고서 문장/주장을 개별 조항·문단·인용에 연결하는 claim-to-evidence 검증, 관보 정본과 통합본/정오표 차이의 체계적 대조, 실제 운영 Gemini 모델 응답 호환성 canary.
- 따라서 이 변경은 자동 보고서의 출처 추적성을 개선하는 최소 gate이며, 법률 해석·제품 적용성·CRA 적합성 검증을 대체하지 않는다.


## 2026-11-17 — 주장별 근거 연결 및 fail-closed 검증 추가

### 구현 범위
- `cra_claims.py`에 구조화된 claim-to-evidence validator를 추가했다.
- 보고서 마지막에 단일 `CLAIM_EVIDENCE_JSON` JSON 블록을 요구한다.
- 주장 분류는 `legal_requirement`, `official_explanation`, `interpretation`, `engineering_recommendation`으로 분리한다.
- 법적 의무/공식 설명은 source pack에 등록된 정확한 source_id, Article/Annex locator, 해당 원문에서 복사한 50자 이상 직접 인용을 요구한다.
- 본문에는 각 claim_id(`[C-001]`)를 표시해야 하며, 중복 ID, 본문 미참조 ID, JSON 미선언 ID, 미등록 source_id, 원문과 다른 인용, 확인되지 않는 locator는 fail-closed 한다.
- 해석 및 엔지니어링 권고는 법적 의무와 분리하고 별도의 basis 설명을 요구한다.
- `main.py`는 기존 최소 provenance validator 전에 새 claim evidence validator를 실행한다. 두 검증 중 하나라도 실패하면 보고서 승인/전송/저장 단계로 진행하지 않는다.
- `.github/workflows/tests.yml`은 신규 모듈·테스트의 정확한 blob SHA를 고정하고 pull_request 경로에도 CRA source/claim 파일을 포함한다.

### 검증 범위와 제한
- 신규 테스트는 정상 legal claim, source_id 누락/오류, Article locator 오류, quote mismatch/길이 부족, JSON 누락·문법 오류, 본문 claim_id 연결, 중복 ID, 엔지니어링 권고 분류/근거를 다룬다.
- 이 gate는 **선언된 주장**의 추적성을 검증한다. 본문 자연어 전체를 완전하게 파싱해 누락된 모든 법률 주장을 자동 발견하는 NLP 검증은 아니다. 따라서 모델 프롬프트에서 모든 법적 문장에 claim_id를 붙이도록 요구하고, 최종 사람 검토를 유지한다.
- locator 검사는 해당 source_id 원문에서 명시된 Article/Annex/Part 및 paragraph/point 토큰 존재를 확인하는 보수적 기계 검사다. locator가 법률상 주장과 정확히 같은 의미인지, 문맥상 예외/단서가 적용되는지는 검증하지 않는다.
- 인용의 원문 일치도 법률 해석의 정확성, 제품 분류, 제품 적용성, CRA 적합성을 증명하지 않는다.
- 실제 Gemini/Discord 및 운영 workflow는 호출하지 않는다. 실제 모델이 새 JSON 계약을 일관되게 출력하는지는 별도 격리 canary가 필요하다.
- 작업 전 복구 기준: `safety/pre-claim-evidence-2026-11-17-d8870e3` (기준 SHA `d8870e32e16ba5ebd3a7670d12816324de3b485a`).


### 최종 격리 검증 결과 — 2026-11-17
- 최종 feature head: `b11f0dcb9bc8f41a0e82ac8062c75c1ca2d08143`.
- Isolated CI Run #194: **112 passed, 1 xfailed**. 정확한 source blob SHA, compileall, 전체 pytest 모두 성공.
  https://github.com/useformotor3/ai-discord-bot/actions/runs/43998058880
- EUR-Lex read-only canary Run #53: **success**, 동일 feature head 기준.
  https://github.com/useformotor3/ai-discord-bot/actions/runs/43998058856
- CI는 mock 격리 테스트이며 실제 Gemini/Discord 호출은 포함하지 않는다. Canary는 EUR-Lex read-only GET만 수행한다.
- 다음 미완료 게이트: 실제 Gemini 출력의 JSON 계약 호환성을 비운영 canary로 확인, Official Journal 정본/정오표와 통합본 대조, claim 본문 누락에 대한 사람 검토, 제품 적용성 평가.


### 문서 동기화 head 최종 CI
- 문서 및 테스트 가이드 동기화 head `7c9360ad6c4e833e0037e3fbc0756d736a15efd2`에서 CI Run #206: **112 passed, 1 xfailed**.
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43998309434


## 2026-11-17 — Gemini JSON compatibility canary 및 비용/데이터 경계

### 공식 정책 확인
- Google Gemini API 가격표는 `gemini-3.8-flash` Standard Free Tier의 입력/출력 토큰을 무료로 표시한다. 다만 Free Tier의 콘텐츠는 Google 제품 개선에 사용될 수 있다고 명시한다.
- 같은 가격표에서 Gemini 3.8 Flash의 Google Search Grounding은 Free Tier에서 제공되지 않는다. 따라서 이 프로젝트는 유료 grounding을 호출하지 않고 EUR-Lex 공식 HTML 직접 수집을 유지한다.
- Free Tier rate limit은 모델/프로젝트별로 달라지고 AI Studio에서 현재 quota를 확인해야 한다. 계정/프로젝트의 실제 billing tier는 이 저장소에서 확인할 수 없다.
- Google API reference는 REST `generateContent`에 `x-goog-api-key` 헤더 사용을 명시한다. Google은 2026년 6월 이후 신규 개발에 Interactions API를 권장하고 `generateContent`를 legacy로 분류하므로, 현재 운영 코드를 바꾸기 전에 별도 migration 평가가 필요하다.

공식 자료:
- Pricing: https://ai.google.dev/gemini-api/docs/pricing/
- Rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- API reference/authentication: https://ai.google.dev/api
- GenerateContent: https://ai.google.dev/api/generate-content

### 구현
- `scripts/cra_gemini_canary.py`: `gemini-3.8-flash`에 단 한 번의 제한된 REST 요청을 보내고 JSON claim shape 및 synthetic quote 일치를 확인한다.
- 입력은 코드에 고정된 공개 합성 문장뿐이다. CRA 법령 원문, 보고서, 저장소 파일, Discord 정보, 운영 상태는 전송하지 않는다.
- Google Search grounding/tools는 요청에 포함하지 않는다. API key는 URL이 아닌 `x-goog-api-key` header로 전달하며 로그에 출력하지 않는다.
- `.github/workflows/cra-gemini-canary.yml`은 `workflow_dispatch` 전용이며 `confirm_free_tier` boolean 기본값은 false다. 확인을 명시하지 않으면 API 호출 job은 실행되지 않는다.
- workflow dispatch 시에도 GitHub Secret `GEMINI_API_KEY`가 필요하다. 사용자가 실제 프로젝트가 Free Tier인지, 유료 결제가 활성화되어 있지 않은지 확인한 경우에만 수동 실행한다.
- `tests/test_cra_gemini_canary.py`는 mock opener를 사용해 성공/오류 경로를 검증하며 실제 Gemini API를 호출하지 않는다.

### 안전 경계 / 상태
- canary workflow는 자동 push/PR 트리거가 없고 아직 dispatch하지 않았다. 실제 Gemini API 호출은 0회.
- Google 가격표상 무료 토큰은 확인되지만, 특정 사용자의 프로젝트 tier/billing 상태는 알 수 없으므로 무조건 무료라고 단정하지 않는다.
- Free Tier 데이터는 제품 개선에 사용될 수 있으므로 실제 CRA 조사 자료나 개인정보/기밀을 canary에 넣지 않는다.
- REST generateContent compatibility test는 현행 main.py 호출과의 호환성을 확인하는 임시 단계다. Interactions API migration은 별도 검토 과제로 남긴다.


### Live Gemini canary의 배포 제약
- `.github/workflows/cra-gemini-canary.yml`은 현재 feature/Draft PR 브랜치에만 존재한다.
- GitHub `workflow_dispatch` 실행은 workflow 파일이 default branch에 존재해야 하므로, 이 PR이 main에 반영되기 전에는 live canary를 실행할 수 없다.
- 이 제약은 의도된 안전 경계다. main에 workflow를 별도로 배포하거나 PR을 병합하지 않았고, 실제 Gemini API 요청은 수행하지 않았다.
- 다음 단계는 최신 main과 PR 통합 검토, billing tier 확인, Free Tier 데이터 사용 조건 검토다.


### Gemini canary 격리 CI 결과
- 구현 및 문서 동기화 head `e2f3dbbc9e6cfb5bbd414cf410b5e23e506ed135`의 Isolated CI Run #247: **116 passed, 1 xfailed**.
- 신규 Gemini canary의 mock request/response 검증, exact source blob pins, compileall, 전체 pytest 성공.
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43998889661
- 이 CI는 실제 Gemini API를 호출하지 않았다. Live canary workflow는 default branch 반영 전까지 dispatch 불가하며, 실제 project billing tier 확인 전에는 실행하지 않는다.


### Gemini canary 최종 검증 head
- 최종 canary 코드 및 문서 head `173181265a157bb0086358ea0479c93941149dc6`에서 Isolated CI Run #257: **116 passed, 1 xfailed**.
- EUR-Lex read-only Canary Run #85: success.
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43999017790
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43999023906
- 실제 Gemini API는 호출하지 않았다.


### Gemini canary 최신 문서/로그 head 검증
- head `d335612023398184c54b6b86e9c56e7668779a7c`에서 CI Run #266 **116 passed, 1 xfailed**.
- https://github.com/useformotor3/ai-discord-bot/actions/runs/43999131134
- source SHA pin / compileall / 전체 pytest 성공. 실제 Gemini API 호출은 하지 않았다.
