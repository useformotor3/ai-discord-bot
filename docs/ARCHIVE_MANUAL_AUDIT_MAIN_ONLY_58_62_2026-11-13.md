# main 아카이브 수동 감사 보고서 — 보고서 #58–#62

- 감사일: 2026-11-13
- 원본 브랜치: \`main\` (읽기 전용)
- 기록 브랜치: \`cra-project-foundation\`
- 감사 방법: Pass A 원본 주장·인용 추출 → Pass B EUR-Lex 현행 법령 원문 대조 → Pass C 조항 범위·예외·반증·제품 적용성 검토
- 감사 범위: 2026-11-13 일일 보고서 #58–#62 원본 5개
- 법령 기준: Regulation (EU) 2024/2847, EUR-Lex consolidated text 20.11.2024 (corrigenda C1–C3 반영). Article 13/14 및 Annex I Part I/II, Annex II를 직접 대조.
- 외부 법률전문가의 독립 검토는 수행하지 않았다. 제품 SKU·제품 경계·intended purpose·저장 구조·실제 MCU 정보가 없으므로 제품별 적용성은 UNVERIFIED다.

## 1. 감사 대상 원본 및 기준선

main의 \`history.json\`에서 날짜·일일 번호·경로를 대조하고, main에서 원본을 읽기 전용으로 가져와 blob SHA를 기록했다.

| 일일 보고서 | 원본 경로 | Blob SHA |
|---:|---|---|
| #58 | \`research_archive/2026-11-13_044541.md\` | \`a5d535859eee483d47abb4dbf809cb10fdd3b8ce\` |
| #59 | \`research_archive/2026-11-13_045038.md\` | \`798aadd8105d1b44a03823f0f058e2e5c5fdae04\` |
| #60 | \`research_archive/2026-11-13_045534.md\` | \`412a5cb249e0f198f7c024cf1a6736c9d2d932be\` |
| #61 | \`research_archive/2026-11-13_050052.md\` | \`6d3149dfd83b1862bc2388b6ee15d376d53a4e8e\` |
| #62 | \`research_archive/2026-11-13_050532.md\` | \`5a280db701cf970c32ef85d97010e0dd1dbd7fa0\` |

감사 시 main 기준선:
- main HEAD: \`75add8711d0254da7dea1766bb42f80fc04d36ee\` (Auto-archive report #118).
- \`state.json\`: 2026-11-13 / count 118 (당일 카운터).
- \`history.json\`: 1,393 entries.
- recursive archive tree의 파일 수는 이번 감사에서 별도 확인하지 않았다.
- 작업 브랜치 비교: diverged, 작업 브랜치 ahead 791 / behind 409, merge base \`b425b6db591e34abe003522157cf97ecf2240d9f\`. main은 계속 read-only이며 merge/rebase/sync 금지.

## 2. 적용한 법령 원문 기준

1. **제조사 의무 및 CVD**
   - Article 13(8): 제조사는 support period 동안 취약점을 효과적으로 처리해야 하며, 내부·외부에서 보고된 잠재 취약점을 처리·시정하기 위한 정책과 절차(Annex I Part II(5)의 CVD 정책 포함)를 갖춰야 한다.
   - Article 13(17): 사용자가 직접·신속하게 소통할 단일 연락 창구를 지정하고, 사용자가 쉽게 식별할 수 있도록 하며 Annex II 사용자 정보에 포함한다. 사용자가 선호하는 통신 수단을 선택할 수 있어야 하고 자동화 도구만으로 제한해서는 안 된다.
   - Annex I Part II(5): CVD 정책을 수립하고 집행한다.
   - Annex I Part II(6): 제품의 잠재 취약점 정보 공유를 촉진하는 조치와 취약점 신고 연락 주소를 제공한다.
   - Annex II(2): 취약점 신고·수신 연락 창구와 CVD 정책을 찾을 수 있는 위치를 사용자에게 제공한다.

2. **보안 업데이트**
   - Annex I Part II(2): 취약점을 지체 없이 처리·시정하고 보안 업데이트를 제공한다. 기술적으로 가능한 경우 보안 업데이트는 기능 업데이트와 분리한다.
   - Annex I Part II(8): 보안 업데이트는 지체 없이 배포하고, 원칙적으로 무상 제공한다. 단, 맞춤형 제품에 관하여 제조자와 사업 사용자 사이에 달리 합의한 경우는 예외다.
   - Article 13(9): 지원기간 중 사용자에게 제공한 각 보안 업데이트는 발행 후 최소 10년 또는 남은 support period 중 더 긴 기간 동안 계속 이용 가능해야 한다. 이는 support period 자체를 10년으로 정하는 규정과 다르다.

3. **Article 14 법정 신고**
   - Article 14(1)–(2): 제품에 포함된 **actively exploited vulnerability**를 인지하면 지정 CSIRT와 ENISA에 단일 신고 플랫폼을 통해 통지한다. 조기 경보는 인지 후 24시간 이내, 취약점 신고는 인지 후 72시간 이내, 최종 보고는 시정·완화 조치가 이용 가능해진 날부터 14일 이내다.
   - Article 14(3)–(4): 제품 보안에 영향을 미치는 **severe incident**도 별도 신고 트랙이다. 조기 경보 24시간, 사고 신고 72시간, 최종 보고는 사고 신고 제출 후 1개월 이내다.
   - Article 14(7): 지정 CSIRT의 전자 신고 엔드포인트를 통해 단일 신고 플랫폼으로 제출하며 ENISA에 동시에 접근 가능하게 한다.
   - Article 14(8): actively exploited vulnerability 또는 severe incident를 알게 된 경우 영향받은 사용자와, 적절한 경우 모든 사용자에게 통지한다. 완화·시정 조치 정보를 제공하며, 기계 판독 가능 형식은 적절한 경우의 조건부 요구다.
   - Article 16(3): 지정 CSIRT가 신고를 받은 후 필요한 정보를 해당 회원국 시장감시기관에 제공한다. 제조자가 Article 14 신고를 시장감시기관에 직접 제출하는 것과 구분한다.

4. **보안 이벤트 기록·모니터링**
   - Annex I Part I point 2(l): 보안 관련 정보를 제공하기 위해 데이터·서비스·기능에 대한 접근 또는 변경을 포함한 관련 내부 활동을 기록하고 모니터링하며, 사용자 opt-out 메커니즘을 제공한다.
   - Annex I Part I point 2(h)는 필수·기본 기능의 가용성과 DoS 공격에 대한 복원력·완화 조치다. 로깅 근거가 아니다.
   - CRA는 이 항목에서 tamper-proof 저장, 특정 로그 보존기간, circular buffer, Syslog over TLS를 일률적인 구현 방식으로 지정하지 않는다. 이러한 방식은 위험평가·제품 요구에 따른 설계 선택이다.

## 3. 개별 보고서 판정

### #58 — CVD 정책·연락처·무상 업데이트

**판정: PARTIALLY_VERIFIED**

- 맞는 핵심: CVD 정책, 취약점 신고 연락 주소, 무상 보안 업데이트는 CRA에 근거가 있다.
- 오류: Article 11을 제조사 의무 근거로 제시했다. 현행 CRA에서 제조사 의무는 Article 13이며 Article 11은 General product safety다.
- 오류: Part II(1), (2), (5)의 문장을 원문처럼 제시했으나 정확한 직접 인용이 아니다. Part II(1)은 SBOM을 포함한 취약점·구성요소 식별, (2)는 취약점 처리·시정, (5)는 CVD 정책이다.
- 과장: CVD 연락처를 제조사 웹사이트에 반드시 공개해야 한다는 문구는 Annex I Part II(6)의 contact address, Article 13(17)의 single point of contact, Annex II(2)의 사용자 정보 제공 요건을 혼합했다. 법령의 정확한 표현과 사용자에게 제공하는 위치를 분리해야 한다.
- 과장: 서보 드라이브를 Class II 또는 중요 제품으로 단정할 수 없다. Annex III 범주와 제품 전체의 core functionality에 대한 별도 분석이 필요하다.
- 정정: CVD 정책 Part II(5), 신고 연락 주소 Part II(6), 사용자 단일 연락 창구 Article 13(17), 사용자 정보 Annex II(2), 무상 업데이트 Part II(8)로 분리한다.

### #59 — CVD 및 무상 보안 패치

**판정: PARTIALLY_VERIFIED**

- 맞는 핵심: CVD 정책 및 보안 업데이트 제공·원칙적 무상 제공은 CRA에 근거가 있다.
- 오류: Article 11(7)을 취약점 시정·보안 업데이트 의무의 근거로 인용했으나 현행 CRA의 제조사 의무는 Article 13이며 Article 11은 General product safety다.
- 오류: Article 11(7) 인용문과 Annex I Section 2의 무상 업데이트 인용문은 현행 법령의 정확한 직접 인용이 아니다.
- 누락: Annex I Part II(8)의 무상 제공에는 맞춤형 제품에 관한 제조자와 사업 사용자 사이의 달리 합의한 경우 예외가 있다.
- 미확인: 서보 드라이브를 Class I로 분류할 근거가 제시되지 않았다. Annex III의 제품 범주와 core functionality를 확인하기 전까지 UNVERIFIED다.
- 정정: CVD Part II(5), 무상 업데이트 Part II(8), support period Article 13(8)을 각각 별도로 추적한다.

### #60 — CVD와 ENISA/CSIRT 신고

**판정: PARTIALLY_VERIFIED**

- 맞는 핵심: actively exploited vulnerability 및 제품 보안에 영향을 미치는 severe incident에 대한 Article 14 신고 트랙과 24시간·72시간 단계가 존재한다.
- 과장: 모든 발견 취약점이 자동으로 Article 14 신고 대상인 것은 아니다. 일반 취약점 처리·CVD 정책은 Annex I Part II 및 Article 13에 따르고, Article 14의 의무 신고 트리거는 actively exploited vulnerability와 severe incident다.
- 누락: actively exploited vulnerability 최종 보고는 시정·완화 조치가 이용 가능해진 날부터 14일 이내, severe incident 최종 보고는 사고 신고 후 1개월 이내다.
- 과장: Article 14(8) 사용자 통지는 모든 취약점 공지가 아니라 actively exploited vulnerability 또는 severe incident에 대한 통지다. 영향 사용자 및 적절한 경우 모든 사용자에게 통지한다.
- 오류: Part II(1)은 SBOM/구성요소 식별 항목이다. 업데이트 시정은 Part II(2), 자동 업데이트 등 제품 요구는 Part I 2(c)와 구분해야 한다.
- 정정: CVD, 일반 취약점 처리, Article 14 의무 신고, 사용자 통지를 별도 절차·판정 필드로 분리한다.

### #61 — 보안 이벤트 감사 로깅

**판정: PARTIALLY_VERIFIED**

- 맞는 핵심: CRA는 관련 내부 활동을 기록·모니터링해 보안 관련 정보를 제공하도록 요구한다.
- 조항 오류: 정확한 위치는 Annex I Part I point 2(l)이다. 보고서가 지목한 point 2(h)는 가용성 및 DoS 복원력 요구다.
- 인용 오류: 보고서의 Raw Text Quote는 실제 point 2(l) 문구가 아니며, 다른 요구를 혼합한 합성 인용이다.
- 과장: 변조 방지, 특정 보존기간, 순환 버퍼, Syslog over TLS는 CRA가 이 조항에서 직접 지정한 보편적 요구가 아니다.
- 정정: 법적 결과 요구는 관련 내부 활동의 기록·모니터링과 사용자 opt-out 메커니즘이다. 로그 무결성 보호·용량·전송 방식은 위험평가와 실시간 제어 성능을 반영해 설계 선택으로 기록한다.

### #62 — 취약점 보고 및 CVD

**판정: PARTIALLY_VERIFIED**

- 맞는 핵심: actively exploited vulnerability와 severe incident에 대한 Article 14 신고 및 24시간·72시간 기한이 존재한다.
- 범위 오류: 일반적으로 발견된 모든 취약점이 Article 14 의무 신고 대상인 것처럼 표현했다. 의무 신고 트리거와 일반 취약점 처리·CVD를 분리해야 한다.
- 수신자 오류: 제조자는 단일 신고 플랫폼을 통해 지정 CSIRT의 전자 엔드포인트로 신고하고 ENISA에 동시에 접근 가능하게 한다(Article 14(7)). 시장감시기관은 CSIRT가 Article 16(3)에 따라 필요한 정보를 제공한다. 제조자가 Article 14 신고를 시장감시기관에 직접 제출한다고 쓰지 않는다.
- 사용자 통지 범위 오류: Article 14(8)는 actively exploited vulnerability 또는 severe incident에 대해 영향 사용자와 적절한 경우 모든 사용자에게 통지하는 규정이다.
- 기한 누락: actively exploited vulnerability 최종 보고 14일, severe incident 최종 보고 1개월을 추가한다.
- 조항 오류: Article 11은 제조사 의무 조항이 아니다. Article 13(8)/(17), Article 14(1)–(8), Annex I Part II(5)/(6), Annex II(2)를 구분한다.
- 인용 오류: Article 14(1)의 실제 문구와 24시간 조기 경보 문구(14(2)(a))를 하나의 직접 인용처럼 결합하지 않는다.

## 4. 배치 결과

| 판정 | 건수 |
|---|---:|
| CONFLICT | 0 |
| PARTIALLY_VERIFIED | 5 (#58–#62) |
| VERIFIED | 0 |
| 직접 인용 재사용 승인 | 0 / 5 |
| 제품별 적용성 | 전부 UNVERIFIED |

- 누적 #8–#57: 50건, 40 CONFLICT / 10 PARTIALLY_VERIFIED / 0 VERIFIED.
- 누적 #8–#62: 55건, **40 CONFLICT / 15 PARTIALLY_VERIFIED / 0 VERIFIED**.
- 누적 직접 인용 재사용 승인: **0/55**.
- 표본은 연속·비무작위이며 전체 archive의 오류율로 일반화하지 않는다.
- 파일 단위 판정은 여러 개별 주장 중 핵심 일부가 근거와 일치한다는 의미다. 개별 인용문이 재사용 가능하다는 뜻은 아니다.

## 5. 보고서·설계 문서 반영 기준

| 주제 | 법령 기준 | 통합 기준 |
|---|---|---|
| CVD 정책 | Article 13(8), Annex I Part II(5) | 정책 수립·집행과 내부/외부 취약점 접수·처리·시정 절차 |
| 신고 연락처 | Annex I Part II(6), Article 13(17), Annex II(2) | contact address와 single point of contact, 사용자 정보 제공을 분리 |
| 무상 보안 업데이트 | Annex I Part II(8) | 원칙적 무상, 맞춤형 제품의 제조자-사업 사용자 합의 예외 |
| 취약점/사고 신고 | Article 14(1)–(7) | actively exploited vulnerability와 severe incident 두 트랙, 수신자·플랫폼·기한 구분 |
| 사용자 통지 | Article 14(8) | 영향 사용자, 적절한 경우 모든 사용자, machine-readable 형식의 조건부 적용 |
| 감사 로깅 | Annex I Part I 2(l) | 관련 내부 활동 기록·모니터링 및 opt-out. 2(h)는 가용성/DoS |
| 로그 설계 | 위험평가·제품 성능 | 무결성·보존·용량·전송 방식은 법령 문언과 구분한 설계 선택 |

## 6. 공식 1차 출처

1. EUR-Lex consolidated Regulation (EU) 2024/2847, CELEX 02024R2847-20241120:
   https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
   - Article 13(8), (17), Article 14(1)–(8), Article 16(3)
   - Annex I Part I point 2(h), 2(l)
   - Annex I Part II points (1), (2), (5), (6), (8)
   - Annex II point (2)
2. EUR-Lex Official Journal / consolidated PDF:
   https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R2847
3. EUR-Lex consolidated PDF with corrigenda:
   https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R2847-20241120

EUR-Lex HTML의 일부 화면은 로봇 확인을 반환했으므로, 이 배치에서 HTML 페이지를 시각적으로 검토했다고 주장하지 않는다. 공식 PDF의 텍스트 검색·원문 위치 대조를 수행했다. PDF 페이지 이미지를 별도로 시각 검토하지 않았으며, 외부 독립 법률 검토도 수행하지 않았다.

## 7. 한계와 다음 작업

- main 원본 archive/history/state는 읽기 전용으로 유지했다.
- main merge/rebase/sync를 수행하지 않았다.
- 이 감사는 법령 주장 감사이며 제품 적합성 평가나 DUT 시험이 아니다.
- 제품 SKU, intended purpose, 공급 형태, 실제 저장 데이터·설정, MCU 주문 코드, 통신/업데이트 구성은 미확정이다.
- 다음 P0는 #8–#57 개별 문서의 원자 주장·인용을 Claim ID와 공식 원문 locator에 연결하고 제1권·제2권·SOP·추적성 매트릭스와 전수 대조하는 것이다.
- 그 다음 main-only 감사 배치는 #63–#67이며, 배치 시작 시 main HEAD/state/history를 다시 조회한다.
