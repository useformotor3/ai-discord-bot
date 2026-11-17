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

- Isolated CI Run #141: **103 passed, 1 xfailed**. 정확한 source blob SHA 검증, compileall, 전체 pytest 성공. [실행 로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211881).
- EUR-Lex read-only canary Run #26: **success**. 네 공식 법령 HTML에서 총 220,715자 visible text 확인. CRA 통합본 196,076자, Regulation 2025/327 394,354자, Delegated Regulation 2025/1535 6,246자, Delegated Regulation 2026/881 15,284자. [실행 로그](https://github.com/useformotor3/ai-discord-bot/actions/runs/43989211861).
- 기존 CRA 통합본의 정오표 인덱스 3개 날짜(2024-12-05, 2025-07-02, 2025-10-17)도 다시 확인했다.
- 검증은 공개 EUR-Lex GET과 mock 기반 CI다. Gemini/Discord/운영 workflow 호출은 하지 않았다.

## 11. 현재 상태 및 다음 검증

- 코드 변경은 Draft PR #3에만 존재한다: https://github.com/useformotor3/ai-discord-bot/pull/3.
- PR head: b094a5d5c36bd66c2e7b21179f263f6b6d8a82ce. 기준 main: 0dde26ebac80a789c7a9d9e26560abad54606d32.
- 2026-11-17 현재 main은 자동 아카이브 #10으로 별도 전진했다. 이 PR은 해당 변경을 덮어쓰지 않았으며 main에 병합하지 않았다.
- 아직 미완료: 모든 보고서 문장/주장을 개별 조항·문단·인용에 연결하는 claim-to-evidence 검증, 관보 정본과 통합본/정오표 차이의 체계적 대조, 실제 운영 Gemini 모델 응답 호환성 canary.
- 따라서 이 변경은 자동 보고서의 출처 추적성을 개선하는 최소 gate이며, 법률 해석·제품 적용성·CRA 적합성 검증을 대체하지 않는다.
