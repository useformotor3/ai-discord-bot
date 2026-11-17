# GitHub 브랜치 정합성 및 CRA 소스 검증 통합 감사

- 기준일: 2026-11-17
- 기준 브랜치: main
- main HEAD: addfa63d1a7d2d1c77ec61444aaadf2b1f327389
- 목적: 병렬 브랜치의 유용한 자료/코드를 보존하면서 현재 운영 기준에 안전하게 통합할 대상을 판별한다.
- 원칙: 브랜치 전체 병합, force-push, history rewrite, archive/state/history 삭제를 하지 않는다.

## 1. 결론

현재 운영·문서 기준 브랜치는 main이다. 다만 CRA 연구·자동화 작업이 여러 장기 브랜치로 갈라져 있고, 각 브랜치의 자체 안내 문서가 서로 다른 기본 브랜치를 선언한다. 따라서 main을 canonical로 유지하되, 유용한 고유 자료와 코드는 파일 단위로 감사 후 선택 이식한다.

어떤 분기에도 무조건 병합하지 않는다. 특히 100개 이상 커밋이 갈라진 브랜치는 main과 통합 기준점이 다르므로 전체 merge/cherry-pick을 하지 않는다.

## 2. 브랜치 비교 스냅샷

| 브랜치 | HEAD | main 대비 | 내용/판정 |
|---|---|---:|---|
| main | addfa63d1a7d2d1c77ec61444aaadf2b1f327389 | 기준 | 현재 운영 기준. PR #10–#14 및 #19–#23 병합 기록 |
| cra-project-foundation | da0e68b0edb0836f5604dd7a23bd11b20594ef10 | 1,159 ahead / 1,906 behind | START_HERE/AI_CONTINUITY_BOARD, MASTER_REPORT, 통합 traceability, archive audit queue 등 고유 자료. 자체 문서는 이 브랜치를 기본으로 선언하지만 main과 크게 분기. 전체 병합 금지; 자료 보존 후 별도 감사 |
| integration/cra-source-grounding-2026-11-17 | 1cfac86db1772a3d07ce89a903ae9983a60f68ee | 272 ahead / 201 behind | cra_source.py, cra_claims.py, source manifest, fail-closed gate, claim-evidence validator, 테스트/Canary. 선택 이식 후보 |
| feature/cra-source-grounding-atomic-2026-11-17 | 114dc1f1332bffc06409d67248a430ef024f6154 | 165 ahead / 218 behind | PR #3 관련 원본 feature branch. PR #3은 closed/unmerged; source gate 참고자료 보존 |
| feature/cra-source-grounding-2026-11-17 | 020ca0807cd140f403dc3ad252dfe24b4d75dc3d | 21 ahead / 218 behind | 더 이른 source/test branch. 참고용 |
| safety/post-merge-main-6fd03ef | 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e | 0 ahead / 346 behind | PR #1 당시 복구 기준점. 최신 main의 대체 브랜치가 아니며 rollback 참조로만 보존 |

### 2.1 통합 기준점 차이

- main ↔ integration branch merge-base: 6d47747a9d79a082d80d8680c25408c4bac847aa.
- merge-base 이후 main 고유 변경: 201 commits, 비교 결과 76개 파일 경로.
- merge-base 이후 integration 고유 변경: 272 commits, 비교 결과 40개 파일 경로.
- integration branch는 main의 최신 archive #22를 병합한 상태지만, 현재 main의 후속 운영/문서 변경 201 commits를 포함하지 않는다.
- cra-project-foundation의 START_HERE가 이 브랜치를 기본 작업 브랜치로 선언하는 반면, integration branch의 PROJECT_STATUS/AI_RULEBOOK은 main을 운영 기준으로 선언한다. 현재 main의 병합 이력과 PROJECT_STATUS를 기준으로 main을 canonical로 지정하고, foundation은 병렬 참조 브랜치로 유지한다.

## 3. 이미 병합된 main 개선과 미이식 코드

### 3.1 main에 보존된 운영 개선
- PR #10: EUR-Lex 공식 링크 게이트 및 중복 주제 억제 개선.
- PR #11: 수집 주기/재시도 정책 개선, 429/503 또는 quota 상태에서 반복 호출·오류 종료를 피하는 no-op 경로.
- PR #12: transactional persistence 및 보호된 rollback/checkpoint.
- PR #14: CRA 정정 보고서 및 archive 인덱싱 확장.
- PR #19–#23: CRA 통합 보고서 v0.1/v0.2, 35항목 traceability, 15개 인터페이스 매트릭스, 36개 보안 통제·시험 매트릭스, 참조 보안 아키텍처.

### 3.2 source-grounding branch의 선택 이식 후보
integration branch에는 다음 파일/기능이 있다.
- cra_source.py: EUR-Lex 및 관련 공식 법령 소스 수집, 출처 버전/URL manifest.
- cra_claims.py: 보고서 claim ID, source ID, locator, exact quote 검증.
- main.py: 모델 호출 전에 공식 source pack 수집, 생성 보고서의 claim evidence 검증, 출처 manifest 첨부; 검증 실패 시 fail-closed.
- tests/test_cra_claims.py, tests/test_cra_gemini_canary.py, tests/test_main_characterization.py 관련 테스트.
- scripts/cra_source_canary.py 및 수동 실행용 source canary workflow.
- 해당 branch 보고서가 기록한 CI는 117 passed / 1 xfailed이며, source canary Run #134 success. 이는 그 branch의 과거 결과이지 현재 main의 검증 결과는 아니다.

## 4. 통째로 복사하면 안 되는 main.py 차이

integration branch의 main.py는 source gate를 포함하지만, 현재 main의 운영 개선 일부를 되돌린다. 두 파일의 차이를 확인했다.

| 동작 | 현재 main | integration branch | 이식 원칙 |
|---|---|---|---|
| history context | 최근 15개 | 최근 5개 | main의 15개 유지 |
| model retry | 최대 2회 | 최대 3회 | main의 retry 정책 유지 |
| quota/429/503 | quota/429/503에서 안전한 no-op/종료 경로 | 일반 retry 후 실패 종료 | main의 quota 보호 유지 |
| duplicate topic | 주제 중복 감지/억제 | 해당 억제 제거 | main의 중복 억제 유지 |
| transactional persistence | PR #12의 원자적 저장/rollback guard | 별도 상태 구현 | main의 현재 persistence 유지 |
| source gate | 미통합 | 모델 호출 전 source fetch + claim validation | 해당 기능만 선택 이식 |

따라서 integration branch의 main.py 전체를 복사하거나 branch 전체를 merge하지 않는다. 최신 main에서 새 branch를 만들고 source gate 호출부만 수동 통합한다.

## 5. source validator의 발견된 결함/보강 요구

### 5.1 Article paragraph locator 표현 차이
- integration의 cra_claims.py는 Article locator의 paragraph를 (8) 형태로 찾는다.
- 실제 EUR-Lex consolidated HTML의 Article 13은 Article 13 제목 뒤에 1., 2., ... 8., 9. 형식으로 문단을 표시한다.
- 따라서 현재 validator는 유효한 Article 13(8) locator를 실제 원문에서 찾지 못할 수 있다. 테스트 fixture의 Article 13(8) 표기만으로는 이 결함을 잡지 못한다.
- 수정: 실제 EUR-Lex 텍스트 형태 Article 13 + paragraph 8.을 테스트하고, Article paragraph와 Annex point를 구분해 파싱한다.

### 5.2 quote scope가 article/annex 수준에 머무름
- 현재 validator는 quote가 지정 Article/Annex 안에 있는지 검사하지만, Article의 정확한 paragraph 또는 Annex의 정확한 Part/point까지 엄격하게 제한하지 못한다.
- 예: Annex I Part I (2)(f) locator에 같은 Part I의 (2)(b) quote가 들어가도 통과할 위험이 있다.
- 수정: Article 13(8), Annex I Part I (2)(f), Annex I Part II (5)를 각각 정확한 문단/point scope로 추출하고, 같은 Article/Annex 안의 다른 point quote는 실패하도록 테스트한다.

### 5.3 source pack의 범위
- integration source catalog는 7개 법령/정정 소스 중심이며 Commission Guidance C(2026) 5252와 M/606 개정 결정 C(2026) 7861의 공식 source entry가 없다.
- 보고서에서 이 두 자료를 인용하려면 공식 Commission page/source를 추가하고, 허용 host를 source별로 allowlist 해야 한다. PDF 본문 추출은 검증된 파서/fixture가 준비되기 전에는 자동화 성공으로 가정하지 않는다.
- 공식 Commission page의 요약 텍스트와 원문 PDF/Annex를 구분하고, page summary만으로 Annex의 세부 항목을 입증했다고 주장하지 않는다.

## 6. 안전한 통합 실행 순서

1. 최신 main에서 새 작업 브랜치 cra/source-provenance-integration-2026-11-17을 생성한다.
2. cra_source.py, cra_claims.py를 복사하되, URL host allowlist·source version·timeout·normalization을 검토한다.
3. claim validator를 실제 EUR-Lex 문단/Annex point 구조에 맞게 수정하고 위 5.1/5.2 회귀 테스트를 추가한다.
4. 현재 main.py의 history 15개, retry 2회, quota/429/503 no-op, duplicate-topic guard, persistence/rollback을 그대로 유지하면서 source fetch → prompt source pack → claim validation → source manifest 단계만 통합한다.
5. 기존 main 테스트를 교체하지 않는다. 새 source/claim 테스트를 별도 파일로 추가하고 기존 characterization/persistence tests를 함께 실행한다.
6. .github/workflows/tests.yml의 exact blob SHA pin과 테스트 대상 목록을 갱신한다. workflow secret 또는 live Gemini/Discord 호출 없이 mock 기반으로 검증한다.
7. PR/CI 성공 후에만 main에 병합한다. source canary는 읽기 전용 official GET이며, live Gemini canary는 quota/secret 영향 때문에 자동 실행하지 않는다.
8. cra-project-foundation의 249-item archive audit queue와 고유 문서는 별도 inventory 후 필요한 항목만 main에 이식한다.

## 7. 보존/복구 원칙

- 어떤 divergent branch도 삭제하거나 force-push하지 않는다.
- source branches, safety checkpoint, archive/history/state를 보존한다.
- 새 작업은 항상 최신 main에서 분기한다.
- 변경은 작은 PR로 나누고, branch/commit/changed files/tests/CI/rollback reference를 기록한다.
- source validator 실패는 모델 호출·Discord 발송·Git 저장 전에 차단한다.
- CI가 최종 head에 실행되지 않았다면 과거 run 성공을 최종 변경 전체의 성공으로 확대하지 않는다.

## 8. 공식 근거 확인 메모

- CRA consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120
- Article 13 paragraph numbering is rendered as numbered paragraphs (e.g. 8.) in the consolidated text; the validator must reflect the source's real structure.
- The branch comparison and source-gate code review were performed against the named branch refs on 2026-11-17.
