# CRA 법령 문언 심층 감사 — Batch 2 (CRA-011–CRA-020)

- 기준일: 2026-11-18 (KST)
- 검토 범위: CRA-011–CRA-020
- 1차 법령 기준: Regulation (EU) 2024/2847 EUR-Lex 공식 OJ 원문
- 공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- 상태 구분: 법령 locator/문언 대조 결과이며, 제품별 적용성·적합성 및 실제 구현 증거는 별도다.

## 행별 검토 결과

| ID | 원문 대조 결과 | 수정/보완 사항 | 상태 |
|---|---|---|---|
| CRA-011 | Article 13(17)은 제조자가 단일 연락창구(single point of contact)를 지정해 사용자가 직접·신속히 소통하고 취약점을 신고할 수 있게 요구. 창구는 쉽게 식별 가능해야 하며 Annex II 사용자 정보에 포함. Annex II(2)는 취약점 신고·수신 창구 및 CVD 정책 접근정보를 요구. | locator 적절. 단일 창구는 자동화 도구만으로 제한할 수 없으며 사용자가 선호하는 통신 수단을 선택할 수 있어야 한다(Article 13(17) 마지막 문장). 이 추가 요구를 운영 설계/시험에 반영. | 보완 필요 |
| CRA-012 | Annex I Part II(7)은 취약점을 적시에 수정/완화하도록 업데이트를 안전하게 배포하는 메커니즘과, 보안 업데이트의 경우 해당되는 때 자동 배포를 요구. | locator 적절. 서명, 무결성 검증, 인증된 배포, rollback 방지/복구 등은 안전한 배포를 입증할 수 있는 설계 통제 예시이지 Part II(7)에 각 항목이 문자 그대로 열거된 독립 의무라고 쓰지 않는다. 자동 배포는 'where applicable' 조건을 유지. | 1차 적정 |
| CRA-013 | Annex I Part II(8)은 식별된 보안 문제를 해결하는 보안 업데이트를 지체 없이 배포하고, 원칙적으로 무상 제공하며, 사용자 조치가 포함된 advisory message를 동반하도록 요구. 예외는 제조자와 tailor-made PDE의 business user 사이에 달리 합의한 경우. | locator 적절. 예외는 일반 상용 제품 전체에 적용되는 유료화 예외가 아니라 'tailor-made product + business user + manufacturer와 별도 합의' 조건의 결합으로 한정. | 1차 적정 |
| CRA-014 | Article 13(8)은 지원기간을 예상 사용기간, 합리적 사용자 기대, 제품 성격/의도된 목적, 관련 EU 제품 수명 법령을 고려해 결정하도록 함. 유사 기능 제품 지원기간, 운영환경 가용성, 핵심 기능 제3자 구성요소 지원기간, ADCO/Commission guidance도 고려 가능하며 비례성 확보. 원칙상 최소 5년, 예상 사용기간이 5년 미만이면 그 예상 사용기간. 결정 근거는 Annex VII(4) 기술문서에 포함. | 현재 설명 적절하나 '5년 예외'는 제조자 임의 선택이 아님. 객관적으로 예상 사용기간이 5년 미만인 경우에 한정. support period는 단순 보증기간/상업지원 기간과 동일하다고 가정하지 않는다. | 보완 필요 |
| CRA-015 | Article 13(9)은 지원기간 동안 사용자에게 제공된 각 security update가 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 계속 이용 가능하도록 요구. | locator/기간 계산 적절. 기준 시점은 '제품 시장 출시일'이 아니라 각 보안 업데이트가 발행된 시점. 다운로드 가능성/접근성 보존 증거를 업데이트별로 관리. | 1차 적정 |
| CRA-016 | Article 31(1) 기술문서는 Annex VII 최소 항목 및 제조자가 적합성 확보에 사용한 관련 데이터/수단을 포함. Article 31(2)는 시장 출시 전 작성 및 적절한 경우 적어도 지원기간 동안 지속 갱신. Article 13(13)은 기술문서와 EU DoC를 시장 출시 후 최소 10년 또는 지원기간 중 더 긴 기간 동안 당국에 제공 가능하게 보관. | 현재 CSV는 보존기간을 포함해 대체로 적절. '작성/갱신 기간(Article 31)'과 '당국 제공을 위한 보관기간(Article 13(13))'을 구분하고, 제품 출시 전 기술문서 완성 및 지원기간 중 갱신을 별도 게이트로 표시. | 보완 필요 |
| CRA-017 | Article 13(18)은 Annex II 정보/지침을 종이 또는 전자 형태로 동봉하고, 사용자가 이해할 수 있는 언어로 명확·이해가능·읽기 쉽게 제공하도록 요구. 제조자는 시장 출시 후 최소 10년 또는 지원기간 중 더 긴 기간 동안 이용 가능하게 보관. 온라인 제공 시에도 사용자 친화적이고 온라인 접근 가능 상태를 같은 기간 유지. | locator 적절. '전자 제공'만으로 충분하다고 단정하지 말고 언어/가독성/접근성/보존 요구를 함께 점검. | 1차 적정 |
| CRA-018 | Article 13(19)은 지원기간 종료일을 구매 시점에 명확·이해 가능하고 쉽게 접근 가능한 방식으로 명시하며, 최소 월/연도 포함. 해당되는 경우 제품/포장/디지털 수단에 표시. 기술적으로 가능한 경우 지원기간 종료 알림 표시. | locator 적절. 종료일 표시의 기본 위치는 구매 시점의 쉽게 접근 가능한 정보이며, 제품/포장/디지털 표시는 'where applicable'. 종료 알림은 'where technically feasible' 조건부. | 1차 적정 |
| CRA-019 | Article 13(12)는 선택한 적합성 평가 절차로 적합성이 입증된 뒤 제조자가 Article 28 EU DoC를 작성하고 Article 30 CE 표시를 부착하도록 함. Article 28(2)는 Annex V 형식, 언어 및 적절한 갱신 요구. Article 30은 가시성/가독성/불멸성, 제품 특성상 불가한 경우 포장 및 동봉 DoC 등 표시 위치를 규정. | locator 적절. Annex V는 full EU DoC의 모델 구조이고 simplified DoC는 Annex VI(Article 13(20), Article 28(2))이므로 혼동 금지. CE 표시를 적합성 평가 이전 또는 단순 시험 통과만으로 부착했다고 표현하지 않는다. | 보완 필요 |
| CRA-020 | Article 7(1)은 Annex III 제품 범주의 core functionality를 가진 PDE를 Important product로 취급. 단순히 그런 제품이 다른 제품에 통합됐다는 이유만으로 통합된 호스트 제품까지 Article 32(2)/(3) 절차 대상이 되지는 않음. Article 8은 Annex IV core functionality 제품 중 delegated act 및 가용한 EU cybersecurity certification scheme 조건에 따라 인증 요구를 지정; 관련 delegated act가 없으면 Article 32(3) 경로가 적용됨. Article 32(1)은 일반 경로(A, B+C, H 또는 적용 가능한 scheme), 32(2)는 Class I의 특정 조건에서 B+C 또는 H, 32(3)은 Class II의 B+C/H 또는 적용 가능한 substantial scheme, 32(4)는 Critical 제품의 Article 8 인증 또는 Article 32(3) 경로. | 분류는 제품 이름/통합 여부가 아니라 Annex III/IV 범주의 core functionality로 판단. Article 32(2)의 제3자 평가 요건은 Class I 제품에 harmonised standards/common specifications/적용 가능한 certification scheme이 없거나 충분히 적용되지 않은 조건에서 발생. Article 32(3) Class II와 구분. Annex IV 제품에 인증이 항상 자동 의무라고 쓰지 말고 Article 8(1) delegated act/가용한 scheme 및 Article 32(4) fallback을 함께 명시. | 중요 보완 필요 |

## 공통 핵심 해석

1. Single point of contact는 단순히 이메일 주소 하나를 표시하는 수준이 아니다. 직접·신속한 연락, 쉬운 식별, 사용자 선호 통신 수단 선택, 자동화 도구만으로 제한하지 않는 조건을 확인한다.
2. 안전한 업데이트 배포 메커니즘의 구체적인 암호기술/절차는 위험기반 설계·검증으로 입증하되, 법문에 직접 열거되지 않은 기술 선택을 법정 문구와 혼동하지 않는다.
3. 보안 업데이트 무상 제공의 tailor-made 예외는 제조자와 business user 사이의 합의가 있는 경우로 제한한다.
4. Article 13(8)의 최소 5년은 기본값이며, 5년 미만 예상 사용기간 예외는 예상 사용기간 근거가 있어야 한다.
5. 기술문서의 작성·갱신 의무(Article 31)와 당국에 제공할 수 있도록 보관하는 기간(Article 13(13))은 별개의 관리 항목이다.
6. Full EU DoC(Annex V)와 simplified EU DoC(Annex VI)를 구분한다.
7. Important/Critical 제품 분류는 core functionality 및 Annex III/IV 목록을 근거로 하고, 제품 통합만으로 host product에 분류를 전이하지 않는다. Critical 제품의 인증은 Article 8(1)의 delegated act 및 가용한 scheme 요건과 Article 32(4) fallback을 함께 적용한다.

## 근거 위치 (EUR-Lex)

- Article 13(12)–(20): manufacturer DoC/CE, 보존, 식별, 연락창구, 사용자 정보, 지원 종료일.
- Article 28(1)–(2), Annex V–VI: EU DoC 형식과 simplified DoC.
- Article 30: CE 표시 위치/시점/가독성.
- Article 31(1)–(2), Annex VII: 기술문서 작성/갱신/내용.
- Article 7(1)–(4), Article 8(1)–(2), Article 32(1)–(4), Annex III–IV: 제품 분류 및 평가 절차.
- Annex I Part II(7)–(8), Annex II(2),(7)–(9): 업데이트 배포/무상 제공/사용자 정보.

## 다음 단계
- CRA-021–CRA-035: Article 14/15 신고·자발신고, Article 69/71 전환 및 적용일, 기계류 규정 상호작용, 표준화/추정적합성, 경제운영자 의무 및 Article 2 제외/중복을 행별 검토한다.
