# CRA 공식 출처 수집·주장 추적 파이프라인 — 설계 및 검증 기록

- 기준일: 2026-11-17 (KST)
- 상태: **PR #26 source pipeline 및 PR #29 corrigenda precedence 보강 병합 완료**
- Main merge commit: PR #29 `9c16724b8b72bd09d3492b19ff714602b235c66b`; base source pipeline PR #26 `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`
- 구현 브랜치: `experiment/cellar-source-retrieval-2026-11-17`; 정오표 보강 `fix/cra-corrigenda-precedence-canary-2026-11-17`
- 검증 PR: [#26](https://github.com/useformotor3/ai-discord-bot/pull/26), [#29](https://github.com/useformotor3/ai-discord-bot/pull/29)
- 기본 통합 CI: [GitHub Actions Run #573](https://github.com/useformotor3/ai-discord-bot/actions/runs/44039961078)
- 정오표 적용/검증 CI: [Run #593](https://github.com/useformotor3/ai-discord-bot/actions/runs/44043229559), 최종 PR head [Run #596](https://github.com/useformotor3/ai-discord-bot/actions/runs/44043479661)

## 1. 목적과 경계

CRA 조사 자동화가 모델 생성 결과만을 근거로 보고서를 만들지 않도록, **공식 원문 수집 → 출처 무결성 기록 → 주장별 조항/문단/원문 인용 검증 → 외부 전송 전 안전 게이트**를 구성했다.

이 파이프라인은 주장과 수집된 원문 사이의 추적 가능성을 검사한다. 법률 해석의 정확성, 개별 서보 드라이브의 CRA 적용 여부, 제품 분류 또는 적합성 평가 결과를 자동으로 확정하는 법률 엔진은 아니다.

## 2. 공식 원문 수집 경로

EUR-Lex HTML endpoint를 GitHub Actions에서 직접 호출했을 때 HTTP 202 및 자동화 접근 확인 응답이 발생했다. 이를 정상 원문으로 취급하지 않고 수집 실패로 분류했다. 이후 Publications Office가 운영하는 공식 CELLAR REST API를 기계 수집 경로로 사용했다.

- CELLAR 소개 및 REST API: https://op.europa.eu/en/web/cellar/cellar-data/publications
- CELLAR 이용 설명: https://op.europa.eu/en/web/cellar/users
- EUR-Lex 문서 재사용/기계 판독 형식: https://eur-lex.europa.eu/content/help/content/help/data-reuse/reuse-contents-eurlex-details.html
- 보고서의 사람이 읽는 법령 인용에는 EUR-Lex 공식 문서 링크를 계속 사용한다. CELLAR URL은 기계 수집 및 provenance manifest의 retrieval URL이다.
- EUR-Lex consolidated text는 문서화 도구이며, 법적 효력의 기준은 Official Journal 정본이라는 제한을 보고서에 유지한다.

### 2.1 현재 등록된 9개 공식 출처

| ID | 자료 | 수집 범위 |
|---|---|---|
| CRA-2024-2847-consolidated | Regulation (EU) 2024/2847 consolidated text, 20.11.2024 | Article 1부터 operative Articles 및 Annex |
| CRA-2024-2847-corrigendum-2024-12-05 | OJ 2024/90780, CELEX 32024R2847R(01) | 제목 정정 |
| CRA-2024-2847-corrigendum-2025-07-02 | OJ 2025/90555, CELEX 32024R2847R(02) | Article 64(10) 정정 |
| CRA-2024-2847-corrigendum-2025-10-17 | OJ 2025/90828, CELEX 32024R2847R(04) | Article 67 참조 번호 정정 |
| CRA-2025-327-EHDS-amendment | Regulation (EU) 2025/327 | CRA 관련 Article 104 발췌 및 적용일 |
| CRA-2025-1535-product-scope-delegated-act | Commission Delegated Regulation (EU) 2025/1535 | CRA 적용범위 예외 관련 조문 |
| CRA-2026-881-reporting-delay-delegated-act | Commission Delegated Regulation (EU) 2026/881 | Article 16 신고 전파 지연 조건 |
| CRA-COMMISSION-GUIDANCE-2026-07-27 | Commission Guidance C(2026) 5252 게시 페이지 | 페이지에 표시된 공식 요약 |
| CRA-M606-STANDARDISATION-2026-11-12 | Commission CRA standardisation status page | M/606 연장 관련 페이지 요약 |

CELLAR 법령 자료 7건은 CELEX ID를 기준으로 수집한다. Commission 안내 페이지 2건은 각각 해당 Commission 공식 호스트만 허용한다.

### 2.2 수집하지 않은 관련 문서

- Commission Guidance C(2026) 5252의 PDF 다운로드 링크는 manifest에 관련 URL로 기록하지만 PDF 본문/Annex를 아직 다운로드·파싱하지 않았다.
- M/606 관련 C(2026) 7861 문서등록부 URL은 manifest에 기록하지만 결정문 Annex를 아직 다운로드·파싱하지 않았다.
- 따라서 두 PDF/결정문에만 있는 세부 요구사항·표준별 날짜·Annex 내용을 현재 source pack이 입증한다고 주장하지 않는다.

## 3. 네트워크·도메인 안전성

- 각 source definition에 허용된 공식 호스트를 명시한다.
- 요청은 HTTPS로 시작한다. redirect는 같은 source allowlist host로만 허용한다.
- CELLAR의 HTTP redirect는 동일 호스트임을 확인한 뒤 HTTPS로 승격해 재요청한다. 비허용 호스트 redirect는 거부한다.
- TLS 인증 오류, 비허용 redirect, 잘못된 source marker, 원문 길이 부족은 fail-closed 처리한다.
- timeout/connection failure, HTTP 429/5xx, HTTP 202, 빈 응답은 일시적 source unavailable로 처리하고 Gemini 호출·Discord 전송·저장 변경 없이 실행을 건너뛴다.
- source gate의 예상치 못한 오류도 외부 부작용 전에 실패 종료한다.

## 4. 출처 무결성 manifest

source별로 다음 값을 보존한다.

- source ID, 문서 유형, 판본/버전 설명
- 요청 URL 및 최종 응답 URL
- 원문 visible text 길이
- 전체 visible text의 SHA-256: `full_text_sha256` (수집된 원문 그대로)
- 모델 prompt에 전달한 excerpt의 SHA-256: `prompt_excerpt_sha256` (공식 정오표 적용/확인 후 재계산)
- UTC 수집 시각
- 관련 문서 URL 및 실제 미수집 상태 설명(해당 시)

전체 원문 해시와 prompt excerpt 해시를 분리해, 원문을 줄여 모델에 제공하더라도 원문과 제공 텍스트의 무결성을 구분할 수 있게 했다.

## 5. English corrigenda 우선순위 검증

CELLAR의 consolidated text는 원본 통합본과 정오표 자료를 별도 제공할 수 있으므로, 정오표 3건을 단순히 함께 prompt에 넣는 것만으로는 충분하지 않다. source pack은 Article 64(10)과 Article 67의 영어 정정 후 문구가 prompt excerpt에 반영되었는지 검증한다.

- 2025-07-02 R(02), Article 64(10): `paragraphs 3 to 9`가 남아 있으면 `paragraphs 2 to 9`로 교체한다. 이미 정정 후 문구라면 확인만 한다.
- 2025-10-17 R(04), Article 67: `69. Regulation (EU) 2024/2847`가 남아 있으면 `72. Regulation (EU) 2024/2847`로 교체한다. 이미 정정 후 문구라면 확인만 한다.
- 해당 정오표 source ID의 전/후 원문 문구를 함께 확인한다. correction source가 없거나 대상 Article/문구가 없거나 중복이면 fail-closed 처리한다.
- 원문 그대로의 `full_text_sha256`는 변경하지 않는다. 수정/검증된 prompt excerpt를 기준으로 `prompt_excerpt_sha256`를 다시 계산한다.
- 2024-12-05 R(01)은 영문 제목의 정정이다. operative excerpt는 Article 1부터 시작하므로 제목은 excerpt에 포함되지 않으며, R(01)은 별도 source로 보존한다.

## 6. 주장·근거 검증

보고서는 단일 `CLAIM_EVIDENCE_JSON` 블록을 포함한다. 각 claim에는 고유 ID, 분류, 본문과 동일한 statement, source ID, locator, 직접 인용을 기록한다.

- 허용 분류: `legal_requirement`, `official_explanation`, `interpretation`, `engineering_recommendation`
- 법적 주장 및 공식 설명은 등록된 source ID에 연결해야 한다.
- Article 64(10)/67은 정오표 전/후 문구를 확인하고 정정 후 문구를 사용해야 한다. source pack은 consolidated excerpt에 정정이 반영되었는지 검증하고, stale phrase가 있으면 안전하게 교체한다.
- 법적 직접 인용은 최소 50자이며 지정 source의 실제 텍스트에 존재해야 한다.
- Article 주장은 정확한 paragraph, Annex 주장은 Part/point 범위에서 인용문이 존재해야 한다.
- 같은 Article의 다른 paragraph에만 있는 문장을 가져와 현재 locator의 인용인 것처럼 쓰는 것은 거부한다.
- 본문 claim ID, JSON claim ID, JSON statement가 서로 일치해야 한다.
- legal requirement는 최소 1건 이상 포함해야 한다.
- claim validator는 원문 추적성 검증 도구이며, 법률적 의미의 최종 판단을 대체하지 않는다.

## 7. 실시간 검증 결과

[GitHub Actions Run #596](https://github.com/useformotor3/ai-discord-bot/actions/runs/44043479661), PR #29 final head `04368898a3b4ace935cd75bc801fd87c6a6b507d`:

- 전체 저장소 테스트: **141 passed, 1 xfailed**
- 실시간 official source canary: **9개 출처 수집 성공**
- Article 64(10)/Article 67 정오표 전/후 문구 및 consolidated prompt excerpt의 정정 후 상태 확인
- 실시간 Article 13(8) paragraph locator 및 원문 quote 일치 확인
- compileall 및 source blob identity 확인 통과

기본 PR #26 Run #573은 138 passed / 1 xfailed로 통과했다. PR #29 Run #593과 최종 head Run #596은 각각 141 passed / 1 xfailed로 통과했으며, Run #596에서 문서 변경을 포함한 최종 PR head를 재검증했다.

### 7.1 수집 원문 길이 및 prompt excerpt SHA-256

| Source ID | Visible text chars | Prompt excerpt SHA-256 |
|---|---:|---|
| CRA-2024-2847-consolidated | 196,071 | `730cafdf7f450ea9e0e06805946fbbd8c1cfcded201cf5548189f9ee2d9dfc10` |
| CRA-2024-2847-corrigendum-2024-12-05 | 1,183 | `3c571d13f24d66d38bb7f3caf9108dcbcbff7cdc4068c23a5afb68f54d2745ab` |
| CRA-2024-2847-corrigendum-2025-07-02 | 912 | `49ed1db4abc2db47965235c6d54fedfb562993c27ccbdd6018467f16326d680f` |
| CRA-2024-2847-corrigendum-2025-10-17 | 783 | `0d9f5bf6e6e00c399d6edda10fcdabfa9d955e8c65b72412b9e265a1c6f44733` |
| CRA-2025-327-EHDS-amendment | 394,101 | `f9ecf4f4bcda5676db068428b248f5cc82ac3068d2ce9b70229d90bb577d1ee3` |
| CRA-2025-1535-product-scope-delegated-act | 6,213 | `e4a6d9aba59124b39f31af63a4a5da989a92e187f59d6250a5a09c33a8817994` |
| CRA-2026-881-reporting-delay-delegated-act | 15,269 | `a386f82e575e424831500d244ee1a6e6ac32846cb306eec4c4905af11916d9ee` |
| CRA-COMMISSION-GUIDANCE-2026-07-27 | 3,302 | `d72a18e265f8708d5b353029d093fe33a6d0ac034e57b495981f7415c2ac7e02` |
| CRA-M606-STANDARDISATION-2026-11-12 | 3,282 | `7090598b5a0941d0c65f7f1e2c3bb5e6744d1a2d3bccfd5f8187e0f058267942` |

실시간 canary는 Article 13(8)에서 paragraph scope를 추출하고, 제조자가 지원 기간 중 제품 취약점을 효과적으로 처리해야 한다는 source quote가 해당 paragraph 안에 존재하는지 확인했다.

## 8. 변경 파일 및 병합

- `.github/workflows/tests.yml`
- `cra_source.py`
- `cra_claims.py`
- `main.py`
- `tests/conftest.py`
- `tests/test_main_characterization.py`
- `tests/test_cra_source.py`
- `tests/test_cra_claims.py`
- `tests/test_external_failure_paths.py`

PR #26은 merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`로 main에 통합했고, PR #29 정오표 우선순위 보강은 merge commit `9c16724b8b72bd09d3492b19ff714602b235c66b`로 추가 통합했다. PR #29는 Article 64(10)/67의 정오표 전/후 문구를 확인하고, stale 문구가 있을 때만 해당 Article block에서 교체한다. raw full-text hash는 유지하고 prompt excerpt hash를 재계산한다. 기존 운영 retry/quota/no-op, duplicate-topic suppression, transactional persistence/rollback 보호는 유지했다. 운영 Gemini/Discord 실행을 canary로 호출하지 않았다.
- PR #29 pre-merge ref: `safety/pre-merge-main-pr29-2026-11-17` → `9ad730c42de6451ce6942298e9b17e3e82a3ef62`; post-merge ref: `safety/post-merge-main-pr29-2026-11-17` → `9c16724b8b72bd09d3492b19ff714602b235c66b` (readback SHA 확인).

## 9. 남은 작업과 제한

1. Commission Guidance PDF 원문/Annex를 공식 URL에서 별도 수집하고 PDF text extraction, page locator, SHA-256을 추가한다.
2. C(2026) 7861 결정문과 M/606 Annex를 별도 수집·파싱해 페이지 요약과 구분한다.
3. Article 13(8) 외에 Annex I Part I/Part II 및 주요 조항의 실시간 locator/quote canary를 확대한다.
4. 35개 요구사항, 15개 인터페이스, 36개 보안 통제/시험 항목에 source claim ID와 제품별 증거 링크를 연결한다.
5. 실제 제품 모델·회로·펌웨어·프로토콜·시장 공급 구조가 제공되기 전에는 모델별 적용성/분류/적합성을 확정하지 않는다.
6. PR #26/#29의 PR head CI는 확인했으나 각 merge commit 자체의 별도 Actions run은 이 기록 작성 시점에 확인되지 않았다.

