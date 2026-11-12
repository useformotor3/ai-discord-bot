# 변경 제안서 — CRA 자동 조사 파이프라인 신뢰성 개선

**상태: USER_APPROVAL_REQUIRED — 제안만 작성, main.py/Gemini prompt 변경 없음**  
**대상:** `main.py`, Gemini prompt, 후속 근거 검증 단계  
**기준 코드:** cra-project-foundation의 현재 `main.py`  
**목표:** 0원 운영 원칙을 유지하면서, 근거가 확인되지 않은 AI 생성물이 성공 보고서처럼 게시·저장되는 것을 차단한다.

## 1. 현재 확인된 문제와 근거

현재 main.py를 직접 읽어 확인한 동작:

1. `recent_snippets = history_data[-5:]`로 최근 5개 snippet만 모델 문맥에 넣는다. 행동강령, 상황판, 계획, 지식 인덱스, 이전 오류 정정 이력은 모델 입력에 들어가지 않는다.
2. Gemini prompt는 법령·공식 가이드 조사를 요구하고 "Raw Text Quote"까지 생성하도록 하지만, API 호출에 Google Search grounding 또는 별도 원문 검색/수집 단계가 구성되어 있지 않다. 따라서 이 코드는 모델이 실제 원문을 조회했다고 보장할 수 없다.
3. 모델 결과의 URL, 발행기관, 법령 버전, 조항 위치, 인용문 원문 일치 여부를 검사하지 않는다.
4. 두 모델의 모든 호출이 실패해도 경고 문구를 `ai_message`에 넣고 `success = True`로 바꾼다. 이후 정상 결과와 같은 경로로 Discord 전송, Markdown 저장, state/history 증가가 진행될 수 있다.
5. `MAX_DAILY_QUOTA = 1200`은 코드 내부 임의값이다. 공급자 계정의 실제 RPM/TPM/RPD나 무료 한도를 반영한다고 확인되지 않았다.
6. 모델 목록에 alias `gemini-flash-latest`와 명시 모델 ID `gemini-3.5-flash-lite`가 섞여 있다. alias는 업데이트에 따라 실제 모델이 달라질 수 있으므로 재현 가능한 보고서에는 모델 ID와 실행 시각 기록이 필요하다.
7. Discord POST에 timeout 및 HTTP status 확인이 없다. Webhook 미설정 시 전송 함수가 조용히 종료된다.

## 2. 제안하는 목표 구조

원칙: Gemini는 법령 원문을 만들어내는 권위 있는 검색 엔진이 아니라, 검증 가능한 입력 자료를 정리·분석하는 보조자로 제한한다.

```text
[공식 출처 목록 / 허용 도메인]
          |
          v
[원문 수집 단계]  -- 실패 --> [UNVERIFIED / 중단]
          |
          v
[근거 묶음: URL, 발행기관, 문서번호/버전, 조항 위치, 원문]
          |
          v
[Gemini 분석/초안 생성]
          |
          v
[JSON Schema 및 필수 필드 검사]
          |
          v
[출처 URL / 인용 문자열 / 조항 식별자 검증]
          |
          +-- 실패 --> [검토 대기함, 게시/확정 저장 금지]
          |
          v
[검증 상태가 표시된 초안]
          |
          v
[Discord 알림 + archive/history 기록]
```

원문 수집 단계가 구현되기 전까지는 Gemini에게 "실제 원문을 조사했다"고 주장하게 하지 않고, 입력으로 제공된 근거에 대한 분석만 허용한다. URL 접속 성공은 출처 내용의 정확성 검증과 별개다.

## 3. 단계별 변경 제안

### P0 — 실패를 성공으로 위장하지 않기 (main.py)
- 모델 호출이 모두 실패하면 `success=False`를 유지한다.
- 실패 상태를 별도 로그로 남기고 non-zero exit code로 종료한다.
- 실패 시 archive/history/count를 정상 조사 건으로 증가시키지 않는다.
- Health-check와 연구 성공 상태를 분리한다.
- 오류 메시지는 비밀값을 마스킹하고 예외 종류/HTTP 상태/재시도 횟수만 기록한다.

### P1 — Gemini 입력/출력 계약 재설계 (prompt 및 파서)
- 역할 문구의 과장("최고 전문가") 제거.
- 모델에게 법령 원문을 추정하거나 직접 인용문을 창작하지 말라고 명시.
- 입력으로 제공된 근거 외의 주장에는 `UNVERIFIED` 표시.
- 출력은 자유 형식 4개 항목 대신 버전 관리되는 JSON schema로 생성.
- claim 단위 필드 예시:
  - `claim_id`, `claim_type`, `claim_text`
  - `source_id`, `source_url`, `publisher`, `document_id`, `document_version`
  - `legal_location`, `source_excerpt`, `excerpt_type`
  - `interpretation_ko`, `servo_drive_relevance`, `limitations`
  - `verification_status`, `verification_notes`
- 모델이 채운 `VERIFIED` 값은 신뢰하지 않는다. 검증기는 자체 판정만 부여한다.

### P2 — 근거 검증 게이트 (별도 모듈)
- URL의 HTTP 상태 및 최종 리디렉션 주소 확인.
- 허용 도메인/발행기관 정책 확인.
- 문서 식별자/버전/조항 위치 존재 여부 확인.
- 짧은 직접 인용은 수집된 원문과 문자열 대조.
- 법률 해석 및 제품 적용성은 자동 검증 완료로 처리하지 않고 사람 검토 대기.
- 검증 실패/출처 누락이면 게시하지 않고 검토 대기함에 보관.

### P3 — 무료 사용/비용 방어
- 1200이라는 임의 상수를 공급자 공식 한도로 표시하지 않는다.
- 현재 프로젝트의 모델별 무료 한도는 Google AI Studio의 해당 프로젝트 Rate Limits 화면에서 확인해야 한다.
- 설정되지 않은 모델 ID/일일 내부 호출 상한/무료 사용 허용 여부가 있으면 fail-closed.
- 유료 결제·유료 모델·유료 Search grounding을 자동 활성화하지 않는다.
- 사용자가 0원 운영을 유지하므로 무료 tier가 확인되지 않거나 초과 위험이 있으면 중단한다.
- Google의 Free tier 가격표는 특정 모델의 입력/출력이 무료로 표시되어도 프로젝트별 접근권한·한도까지 보장하지 않는다. 실제 프로젝트 화면을 확인한다.

## 4. 영향 범위 및 호환성

- 기존 `research_archive/*.md`, `history.json`, `state.json`은 삭제하거나 자동 변환하지 않는다.
- 새 스키마는 별도 폴더/파일로 도입하고 과거 자료는 legacy raw archive로 보존한다.
- Discord 메시지 형식은 검증 상태와 원문 링크를 포함하는 형태로 변경될 수 있다.
- 기존 workflow의 schedule/trigger/Secrets는 이 제안만으로 변경하지 않는다.
- 기존 자동 조사 실행은 사용자 승인 전 현재 동작 그대로 둔다.

## 5. 위험과 통제

| 위험 | 통제 |
|---|---|
| JSON 출력이 잘리거나 잘못된 형식 | schema validation, 재시도 제한, 실패 시 게시 금지 |
| 공식 원문 수집 실패 | 성공으로 간주하지 않고 UNVERIFIED 상태로 중단 |
| 링크는 살아 있으나 내용이 틀림 | URL 검사와 내용/조항/인용 검증을 분리 |
| Gemini가 VERIFIED라고 자기 판정 | 모델 상태를 무시하고 별도 검증기만 상태 부여 |
| 무료 quota 초과/유료 전환 | 프로젝트 실제 한도 확인, billing 자동 활성화 금지, fail-closed |
| 기존 데이터 호환성 손상 | 기존 파일 보존, 별도 신규 스키마, fixture 테스트 |
| Discord 실패 | timeout/status 확인, 전송과 저장 상태 분리 |

## 6. 테스트 및 승인 기준

승인 후 구현 시 최소 테스트:
1. 두 모델 모두 실패: archive/history/count 증가 0, non-zero 종료.
2. 빈 응답/잘못된 JSON: 게시 금지.
3. 출처 URL 누락/비공식 도메인/조항 불일치: VERIFIED 금지.
4. 원문 인용이 입력 원문과 다름: 검증 실패.
5. URL 404/timeout/redirect: 각각 올바른 상태 기록.
6. Discord 4xx/5xx/timeout: 성공으로 표시하지 않음.
7. 모델 quota 429/서비스 503: 제한된 재시도 후 중단, 유료 폴백 금지.
8. 기존 archive/history/state fixture: 읽기 호환 및 원본 보존 확인.
9. 모든 로그에서 API key/Webhook secret 마스킹 확인.

**성공 기준:** 실패를 성공으로 저장하는 경로 0건, 검증 없는 결과가 확정 게시되는 경로 0건, 무료 사용이 확인되지 않으면 API 호출 0건, 기존 기록 손실 0건.

## 7. 백업 및 롤백

- 구현 전 main.py, 관련 workflow, prompt, history/state의 현재 SHA를 기록한다.
- 변경은 cra-project-foundation에서 별도 커밋으로 수행하고 main에 병합하지 않는다.
- 각 단계는 작은 커밋과 독립 테스트로 분리한다.
- 실패 시 해당 커밋을 revert하고 이전 SHA로 복구한다.
- 기존 아카이브는 덮어쓰거나 재작성하지 않는다.

## 8. 사용자 승인 요청

아래 단계는 별도 승인 대상으로 둔다.
- P0: 실패 처리 수정
- P1: Gemini prompt/JSON 출력 계약 변경
- P2: 원문 수집·검증 모듈 추가 및 게시 게이트 연결
- P3: 무료 한도/모델 ID/비용 fail-closed 변경

승인 전에는 어떤 항목도 main.py, prompt, 실행 workflow에 반영하지 않는다.

## 9. 참고 근거 (2026-11-12 확인)
- Google Gemini API pricing / Free tier: https://ai.google.dev/gemini-api/docs/pricing
  - Free tier는 제한된 모델 접근을 제공하고, 입력·출력 토큰은 무료 모델에 대해 무료로 표시될 수 있다.
  - Google AI Studio 사용 데이터가 제품 개선에 사용될 수 있다고 안내한다.
  - Search grounding은 모델/티어별 무료 제공 여부가 다르므로 자동 사용 금지.
- Google AI Developers Forum 공식 응답(2026-10-22): https://discuss.ai.google.dev/t/subject-gemini-api-all-models-return-no-longer-available-to-new-users-404-despite-active-billing/178572/2
  - 신규 프로젝트용 모델로 gemini-3.8-flash 및 gemini-3.5-flash-lite를 안내. 실제 프로젝트 접근 가능 여부는 별도 확인 필요.
- 모델별 제한/사용량은 프로젝트별 AI Studio 화면에서 확인: https://aistudio.google.com/

## 10. 신규 실증 사례 — main-only 보고서 #35/#36 (2026-11-12)

### 관찰된 실패 증거

| Report | 원본 main commit / file | 확인된 문제 | 감사 기록 |
|---|---|---|---|
| #35 | f3eed0a20bfd9ee118561e8bcd0ae890d84ef6e2 / research_archive/2026-11-12_025041.md | Secure Boot/하드웨어 Root of Trust/TPM/디지털 서명을 CRA 보편 의무로 단정. Annex I Part I(2)(b)–(d) 문구와 번호를 잘못 조합한 Raw Text Quote | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md |
| #36 | 5cd4a18dbf5dc4712d669b29b8846af799f5efc1 / research_archive/2026-11-12_025529.md | Secure Boot/Measured Boot/TPM 보편 의무 단정. Annex I에 없는 Secure Boot 문장을 직접 인용처럼 삽입. Article 14를 무상 업데이트와 혼동. CRA 정식 제목의 개정 법령 번호 오류 | ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md |

두 원본은 main에만 존재하며 작업 브랜치에는 복사/수정하지 않았다. 원본 archive는 불변으로 유지하고 작업 브랜치의 감사 문서와 Claim Evidence Ledger에 정정 내용을 기록했다.

### 제안 보강 — P1/P2에 추가할 필수 게이트

1. **직접 인용 생성 금지 기본값:** 원문 수집 단계에서 확보한 정확한 source text가 입력으로 전달되지 않았다면 모델은 Raw Text Quote를 생성하지 않는다. 인용 대신 paraphrase와 UNVERIFIED를 사용한다.
2. **인용 문자열 일치:** quote는 수집된 원문과 공백/줄바꿈 정규화 후 문자열 대조한다. 일치하지 않으면 quote REJECTED, 게시 보류.
3. **법령 위치 정합성:** Annex/Part/point 및 Article 번호를 별도 공식 조항 인덱스와 대조한다. 문구가 다른 항목에 존재해도 번호가 틀리면 VERIFIED 금지.
4. **법령 식별 메타데이터:** CELEX/Regulation number, 정식 제목, 개정 대상 법령 목록, 문서 버전을 EUR-Lex 메타데이터와 대조한다.
5. **의무와 구현 선택 분리:** CRA의 결과 요구(예: integrity, access control, secure update distribution)와 구현 후보(예: Secure Boot, TPM, SE, digital signature)를 별도 claim_type/field로 저장한다. 구현 후보를 법령의 직접 의무 문장으로 승격하지 않는다.
6. **조항 역할 구분:** Article 13 support period, Article 14 reporting, Annex I Part II(8) free-of-charge security updates를 서로 다른 legal obligation ID로 고정 매핑한다.

### 추가 회귀 테스트

10. 원문에 없는 “secure boot” 직접 인용이 생성되면 검증 실패 및 게시 금지.
11. Annex I Part I(2)(b)/(c)/(g)와 실제 문구가 불일치하면 quote/claim을 REJECTED 처리.
12. Regulation (EU) 2024/2847 정식 제목 또는 amending act list가 EUR-Lex와 다르면 metadata validation 실패.
13. Article 14를 free-of-charge update obligation으로 매핑하면 실패.
14. 원문 수집 실패/본문 미제공 시 VERIFIED quote 0개, archive의 확정 연구 건수 증가 0.
15. Secure Boot/TPM/Measured Boot가 법령의 보편적 의무로 표현되면 risk-based design recommendation으로 강등하거나 게시 보류.

**상태:** 위 내용은 변경 제안에만 추가했다. main.py, Gemini prompt, parsing/validation gate, production workflow는 수정하지 않았으며 사용자 승인 대기 상태를 유지한다.


## 11. 신규 실증 사례 — main-only reports #81–#122 (2026-11-12)

### 관찰된 실패 증거

- Reports #81–#121의 41개 연속 commit diff를 확인하고 EUR-Lex Regulation (EU) 2024/2847 Article 13–14, Annex I Part I/II, Annex II와 대조했다.
- 파일 단위 판정: 33 CONFLICT / 8 PARTIALLY_VERIFIED / 0 VERIFIED. 41개 Raw Text Quote 블록 모두 직접 인용으로 재사용 불가.
- 후속 #122도 CONFLICT: secure-by-default/access-control 주제는 관련성이 있으나 Annex I 구조·인용이 잘못되고 forced password change, RBAC, 모든 미사용 포트 비활성화를 보편적 법적 의무로 과장했다.
- 상세 근거: ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md, ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md, claim ledger CRA-ARCH-081-001..CRA-ARCH-122-001.

### 반복 실패 유형

1. Article 13(8) support period와 Annex I Part II(8) free security updates를 반복 혼동.
2. 지원기간의 5년 원칙을 expected lifetime보다 무조건 짧은/긴 기간으로 오인하고, expected use가 5년 미만이면 그 예상 사용기간에 대응한다는 예외를 누락 또는 역전.
3. Article 14를 모든 취약점 신고, 무상 업데이트 또는 일반적인 취약점 처리 조항으로 오인. 실제 신고 대상은 actively exploited vulnerability 및 severe incident로 구분해야 한다.
4. 존재하지 않는 Annex I 세부 번호, Article 하위항목, 합성 Raw Text Quote를 생성.
5. Secure Boot, TPM/Root of Trust, 디지털 서명 알고리즘, dual-bank/rollback, zero-downtime update, 강제 최초 비밀번호 변경, RBAC, 모든 포트 비활성화 등을 법령이 일률적으로 명령하는 것처럼 표현.
6. Secure-by-default/access control/attack surface와 같은 정확한 상위 개념이 있더라도 잘못된 번호·합성 인용·구현 과장이 포함되면 파일 전체를 VERIFIED로 승격할 수 없음.

### P0/P1 변경 제안에 추가할 구체적 acceptance criteria

- Legal clause registry: 법령별 Article/Annex/Part/point의 공식 구조를 기계 판독 가능한 고정 레지스트리로 유지하고, 모델 출력의 legal_location이 존재하지 않거나 잘못된 경우 자동 거부.
- Source-bound quote only: 원문 수집기가 실제 본문을 가져오지 못했으면 source_excerpt와 direct_quote 필드는 비워 둔다. 모델은 인용문을 생성할 권한이 없다.
- Exact-match quote gate: 정규화된 인용 문자열이 확보된 원문에 존재하지 않으면 quote=REJECTED, claim status 최대 UNVERIFIED, archive 확정 저장/게시 금지.
- Obligation-vs-design taxonomy: LAW_REQUIREMENT, RISK_BASED_DESIGN_OPTION, PRODUCT_SPECIFIC_FACT, INTERPRETATION을 분리한다. Secure Boot/RBAC/TPM 등은 원문에 직접 명시되지 않는 한 LAW_REQUIREMENT로 허용하지 않는다.
- Cross-clause guard: Article 13(8), Article 13(9), Article 14, Annex I Part I(2), Annex I Part II(1)–(8), Annex II(2)/(8)(d)를 서로 다른 obligation ID로 매핑하고 상호 대체를 금지한다.
- Support-period exception test: 테스트 fixture에 expected use 3년, 5년, 10년 사례를 넣어 “3년 예상 제품은 3년 support period; 일반 제품은 최소 5년; 예상 사용이 10년이면 support period를 10년 수준으로 정당화”하는 방향을 검증한다. 구체 사례는 법률 자문이 아닌 문언 처리 회귀 테스트다.
- Article 14 dual-track test: actively exploited vulnerability와 severe incident를 분리하고, 24h/72h/14일-after-measure vs 24h/72h/1개월-after-incident-notification을 각각 검증한다.
- No class inference: 서보 드라이브 제품 분류는 실제 core functionality와 Annex III/Implementing Regulation 기준이 입력되기 전 자동 확정하지 않는다.
- Fail closed: 원문 미수집, legal-location mismatch, quote mismatch, 필수 메타데이터 누락 시 report success/archive count/history update/Discord publication을 차단한다.

### 현재 제안 상태와 사용자 승인 게이트

- 위 항목은 P0/P1 변경 제안의 추가 증거와 acceptance criteria일 뿐이다.
- main.py, Gemini prompt, parser/validator, model selection/fallback, context construction, production workflow 및 run.yml은 변경하지 않았다.
- 구현 전에는 이 추가 제안에 대해 별도 사용자 승인을 받고, 구체 diff·영향·회귀/비용 위험·테스트·롤백을 다시 제시한다.


## 12. 신규 실증 사례 — reports #123–#124 (2026-11-12)

### 관찰된 추가 실패 증거
- #123: 사용자 지침서 의무를 Article 13(7)에 잘못 연결(정확한 근거 Article 13(18)); Annex II에 존재하지 않는 Part I/Part II 구조를 생성; Annex II 8(a)–(f), 9의 조건을 왜곡; “Digital Product Passport”를 법정 용어처럼 사용; 서보 드라이브 Class II를 제품 증거 없이 단정.
- #124: 취약점 처리 요구사항을 Annex I Part I Section 2로 잘못 분류(정확한 구조 Annex I Part II(1)–(8)); 합성 Raw Text Quote; cryptographic signature 및 fail-safe recovery를 보편적 명시 의무로 과장.
- 상세 파일: ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md, ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md; ledger CRA-ARCH-123-001/124-001.

### 추가 P0/P1 acceptance criteria
- **Annex structure registry:** Article/Annex/Part/point/letter structure is canonicalized; non-existent labels such as “Annex II Part I/II” and “Annex I Part I Section 2” are rejected.
- **Obligation paragraph mapping:** Article 13(7) systematic cybersecurity documentation, 13(17) single contact, 13(18) user instructions, 13(19) support-end-date information are distinct IDs and cannot be substituted.
- **Annex II conditionality:** points 1–9 are represented exactly; point 8(a)–(f) separately typed; point 9 SBOM access location is conditional on manufacturer deciding to make SBOM available to users.
- **Article 13(18)/(19) document retention/display:** tests must separately validate instruction provision/retention and support-end-date display at purchase, including at least month/year and feasible end-of-support notification.
- **Part I vs Part II separation:** product cybersecurity properties (Part I) cannot be substituted for vulnerability-handling process obligations (Part II).
- **Security-update taxonomy:** Part I(2)(c) applicable automatic-update default and user controls are distinct from Part II(7) secure distribution and Part II(8) timely/free update availability.
- **Implementation mandate guard:** signature verification, secure boot, anti-rollback, dual-bank/recovery, fail-safe modes and RBAC are not classified as universal LAW_REQUIREMENT unless an exact legal source says so; they may be RISK_BASED_DESIGN_OPTION and need product-specific justification.
- **Product-class guard:** Important Product/Class I/Class II classification requires actual Annex III category and core-function evidence. Product name or industrial use alone is insufficient.
- **No statutory-label hallucination:** “Digital Product Passport” cannot be represented as CRA Annex II legal terminology; if used internally, it must be labelled manufacturer-created information package.

### Approval status
These are evidence-backed proposal additions only. No main.py, Gemini prompt, parser, validation gate, model selection/fallback, production workflow or run.yml was modified. Implementation remains USER_APPROVAL_REQUIRED.


## 13. 신규 실증 사례 — main-only reports #125–#128 (2026-11-12)

### 관찰된 실패 증거
- main HEAD가 #125 이후 #126, #127, #128까지 진행된 것을 commit history로 확인했다.
- #125: Article 13(18)/Annex II 사용자 지침을 Annex I Part II Section 2에 배치하고, Annex II Point 1에 존재하지 않는 하위항목을 직접 인용처럼 생성. Article 13(8)의 지원기간 예외를 단순화.
- #126: 신고 의무를 Article 11로 오기(정확한 법적 트랙은 Article 14), CVD/contact의 Annex I Part II 위치와 원문 인용 오류.
- #127: CVD를 Annex I Part I로 오배치, Article 13(6)을 지원기간 근거처럼 사용, expected lifetime/5-year 문구를 잘못 표현.
- #128: Annex I Part I에 존재하지 않는 (5)/(6) 하위항목을 생성하고 Secure Boot/RoT/서명/rollback/STO를 보편적 CRA 의무로 과장.
- 상세 감사: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md). 4개 모두 CONFLICT.

### 변경 제안에 미치는 영향
이 연속 사례는 프롬프트 문구만 추가하는 방식이 충분하지 않음을 보여준다. 오류는 (a) 법령 구조 생성, (b) 법적 근거 ID 혼동, (c) 원문 인용 합성, (d) 법적 의무와 설계 선택 혼합, (e) 제품 분류 추정으로 반복된다. 따라서 Gemini 명령문을 기준선/출력 계약으로 개선하고, 파서 및 실패 게이트를 최소 보완하는 범위로 제한한다.

## 14. 1차 구현 제안 — 범위 축소 및 구체 변경안

**목표:** 대규모 재설계 없이 Gemini 명령문을 핵심으로 개선하고, 운영상 가장 위험한 실패 경로만 차단한다.

### 14.1 변경 파일
1. `main.py` — 기존 inline prompt를 버전관리 prompt 파일에서 읽도록 변경하거나, prompt 파일을 명확한 단일 상수로 교체. JSON 응답 파싱/필수 필드 검사 및 모델 전체 실패 시 fail-closed 처리.
2. `prompts/CRA_RESEARCH_PROMPT_V2.txt` — 운영 Gemini 명령문. 현재는 제안서 `docs/PROPOSED_GEMINI_PROMPT_V2.md`에만 존재하며 운영 적용 전 복사/검토한다.
3. 테스트 파일 — 성공/실패/빈 응답/잘못된 JSON/필수 필드 누락/모델 폴백을 fixture로 검사한다.

`.github/workflows/run.yml`, Secrets, trigger, model list/ordering, quota policy, Discord format, archive/history/state schema, main branch는 1차 변경 범위에서 제외한다. 단, 기존 모델 ID가 structured output을 지원하지 않으면 구현 전 지원 모델 확인이 별도 선행 조건이다.

### 14.2 현재 → 제안 흐름

**현재**
```python
response = client.models.generate_content(
    model=model_name, contents=prompt
)
if response and response.text:
    ai_message = response.text
    success = True
...
if not success:
    ai_message = "시스템 긴급 경고..."
    success = True
# 이후 Discord/archive/state/history 정상 성공 경로로 진행
```

**제안**
```python
response = client.models.generate_content(
    model=model_name,
    contents=prompt,
    config=GenerateContentConfig(
        response_mime_type="application/json",
        response_json_schema=CRA_REPORT_SCHEMA,
    ),
)
payload = json.loads(response.text or "")
validate_required_fields(payload)
ai_message = render_report(payload)
success = True
...
if not success:
    log_failure_without_secrets()
    raise SystemExit(1)  # Discord/archive/state/history success path 진입 금지
```

위 코드는 변경 의도를 나타내는 diff 예시이며 실행 가능한 완성 코드가 아니다. 실제 구현에서는 현재 설치되는 `google-genai` SDK 버전과 선택된 모델의 schema 지원을 CI에서 확인한다. SDK 공식 문서는 `response_mime_type="application/json"` 및 `response_json_schema` 사용을 안내한다: https://googleapis.github.io/python-genai/ 및 https://ai.google.dev/gemini-api/docs/structured-output.

### 14.3 1차 Gemini 명령문 계약
- 검토용 프롬프트: [PROPOSED_GEMINI_PROMPT_V2.md](PROPOSED_GEMINI_PROMPT_V2.md).
- 법령 원문 본문이 입력되지 않으면 직접 인용을 생성하지 않고 excerpt를 빈 값으로 둔다.
- 출처/조항 후보는 후보로만 기록하고 `UNVERIFIED`를 유지한다.
- LAW_REQUIREMENT / RISK_BASED_DESIGN_OPTION / PRODUCT_SPECIFIC_FACT / INTERPRETATION / ASSUMPTION을 분리한다.
- Article 13(6)/(8)/(9)/(17)/(18)/(19), Article 14, Annex I Part I/II, Annex II를 구분한다.
- Annex II Point 1–9의 정확한 구조 및 Part I/II라는 허위 하위구조 생성 금지.
- 서보 드라이브만으로 Important Product Class I/II를 추정하지 않는다.
- 모델은 VERIFIED를 출력할 수 없다. 모델 전체 실패·빈 응답·JSON 오류·필수 필드 누락 시 성공 저장/게시를 금지한다.
- 기존 recent_snippets[-5:] 문맥 구조, 모델 선택/폴백, 실행 workflow, quota constant, Discord 전달은 1차에서 변경하지 않는다. 이 제한으로 중복 방지/출처 검증 문제가 완전히 해결되는 것은 아니다.

### 14.4 영향·제한·위험
- 장점: 변경 파일과 회귀 범위를 최소화, 허위 인용 기본 차단, 모델 실패가 정상 archive로 저장되는 P0 결함 차단, 출력 파싱 안정화.
- 제한: 원문 검색/수집이 없으므로 1차 산출물은 법령·출처 검증 완료 보고서가 아니라 근거 후보가 포함된 UNVERIFIED 초안이다. 정확한 조항 위치·URL·법률 해석을 자동 VERIFIED로 만들지 않는다.
- 위험: JSON schema 미지원 모델/SDK 버전, 응답 잘림, renderer 오류, 기존 보고서 포맷 변경, fail-closed로 인한 조사 공백. 테스트에서 모델 호출은 mock 처리하여 비용을 0으로 유지한다.
- 무료 정책: 유료 모델·유료 Search grounding·결제 활성화·유료 폴백은 추가하지 않는다. schema 지원 확인을 위해 실 API 호출이 필요해지면 사용자에게 별도 승인 요청하고, 우선 CI/mock 테스트만 수행한다.

### 14.5 테스트와 성공 기준
1. 두 모델 모두 예외: non-zero 종료, Discord/archive/history/state 변경 없음.
2. 빈 응답/공백 응답: 모델 폴백 이후에도 없으면 fail-closed.
3. 잘못된 JSON, top-level 필수 키 누락, claim 필드 누락/잘못된 enum: 게시/아카이브 금지.
4. 원문 미제공: direct quote 0개, 모델의 overall status는 UNVERIFIED/PARTIALLY_VERIFIED 범위.
5. 모델이 VERIFIED를 출력: schema/validator가 거부 또는 UNVERIFIED로 강등.
6. CRA 고정 회귀 fixture: Article 13(8) vs Part II(8), Article 14 vs Article 11, Annex I Part I vs Part II, Annex II 1–9, nonexistent Annex II Part I/II, Secure Boot/RoT/rollback universal mandate, Class II inference.
7. 성공 응답 fixture: Markdown renderer 결과가 기존 archive/Discord 흐름에 전달되고 기존 state/history schema가 유지됨.
8. 모든 실패 로그에서 API key/webhook secret 미노출.
9. mock 기반 테스트는 네트워크/API 호출 0회, 유료 비용 0원.

**성공 기준:** 모델 실패/빈 응답/invalid output이 성공 저장되는 경로 0개, 원문 미제공 direct quote 0개, 모델 자체 VERIFIED 승격 0개, 기존 archive/history/state 호환성 손상 0개. 테스트 PASS는 실제 CI 결과 확인 후에만 보고한다.

### 14.6 백업 및 롤백
- 적용 전 작업 브랜치 HEAD 및 변경 대상 파일 blob SHA 기록.
- prompt 파일, main.py, tests를 별도 커밋으로 나누어 변경.
- main branch와 운영 run.yml은 변경하지 않는다.
- 각 커밋 직후 diff 및 fixture tests 확인.
- 실패 시 해당 커밋을 revert하고 사전 SHA로 복구. archive/history/state 원본은 테스트에서 복사본만 사용.

### 14.7 승인 경계
현재 사용자의 "진행"은 이 1차 구현안을 구체화하고 제안 문서/프롬프트 초안을 작업 브랜치에 기록하는 범위로 적용했다. **실제 운영 프롬프트 파일 추가, main.py 수정, parser/validator 변경, 테스트 추가 및 실행은 본 문서의 최종 diff를 사용자가 명시적으로 승인한 뒤 수행한다.** 현재 운영 파일은 변경하지 않았다.
