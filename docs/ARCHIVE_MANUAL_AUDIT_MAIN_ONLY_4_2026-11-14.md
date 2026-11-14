# main-only CRA 아카이브 수동 감사 — 2026-11-14 report #4

- 감사 ID: CRA-AUDIT-MAIN-20261114-004
- 원본 main 파일: research_archive/2026-11-14_001549.md
- 원본 blob SHA: 44105223e8d841bbf2f5f273da950723a33dedbd
- 원본 main commit: 03b3ecaaa506c00146f5cb9d5855e6a66c3ef1c7
- 감사 기준 법령: Regulation (EU) 2024/2847, OJ L, 20.11.2024, EUR-Lex CELEX 32024R2847
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 비교 원본: 2026-11-14 report #2, research_archive/2026-11-14_000536.md, blob SHA 01fbc98108cc2b0d0c56878999f0e749e83eee43
- 파일 단위 판정: **CONFLICT**
- Raw Text Quote 재사용: **0/1** (원문 재사용 금지)
- 제품별 적용성: **UNVERIFIED**

## 1. 요약 판정

#4는 #2와 같은 secure-by-default/초기 인증/공격표면 주제를 반복한다. 새 법적 요구사항을 추가하지 않는다. Annex I Part I(2)(b), (d), (j)의 주제는 관련성이 있으나, 강제 비밀번호 변경·장치별 고유 비밀번호·모든 비필수 포트/서비스 일괄 비활성화를 CRA의 보편적 직접 명령으로 표현한 부분은 근거보다 강하다. Raw Text Quote는 (b)와 (c)를 제시하지만 접근통제 문언은 (d)에 위치하며, (c)는 보안 업데이트 관련 요구다.

## 2. 주장별 감사

| Claim ID | 원본 행 | 원자적 주장 | 공식 근거 | 판정 | 정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261114-004-001 | 10, 14 | 제품은 시장 출시 시 secure-by-default 구성이어야 한다. | Annex I Part I(2)(b) | PARTIALLY_VERIFIED | 요구의 핵심은 맞다. tailor-made product에 관해 제조자와 business user가 달리 합의한 예외와 original-state reset 가능성을 포함해야 한다. |
| CRA-ARCH-MAIN-20261114-004-002 | 15 | 고정/예측 가능한 기본 비밀번호는 엄격히 금지되고, 강제 최초 변경 또는 장치별 고유 비밀번호가 법정 필수다. | Annex I Part I(2)(b), (d) | CONFLICT | CRA는 secure-by-default와 적절한 접근통제 결과를 요구하지만, 모든 제품에 대해 특정 비밀번호 발급/강제 변경 방식을 일률 지정하지 않는다. 제품 위험평가에 따른 구현 선택으로 분리한다. |
| CRA-ARCH-MAIN-20261114-004-003 | 16 | 실시간 제어에 필수인 포트 외 모든 디버그/레거시/미사용 서비스는 기본적으로 비활성화되어야 한다. | Annex I Part I(2)(j), (d) | PARTIALLY_VERIFIED | 외부 인터페이스를 포함한 attack surface 제한 및 적절한 접근통제는 요구된다. 다만 특정 포트·서비스의 blanket disablement 목록은 법령에 지정되지 않는다. 제품 인터페이스 인벤토리와 위험평가로 정당화한다. |
| CRA-ARCH-MAIN-20261114-004-004 | 17 | 백업/복원 및 펌웨어 업데이트 인터페이스는 인증된 세션에서만 접근 가능해야 한다. | Annex I Part I(2)(d), (f); Annex I Part II(7) | PARTIALLY_VERIFIED | 적절한 접근통제·무결성·안전한 업데이트 배포 결과와 부합한다. 구체적인 session architecture는 설계 선택이며 제품별 구현·시험 증거가 필요하다. |
| CRA-ARCH-MAIN-20261114-004-005 | 11 | 제조사는 강력한 초기 인증 메커니즘을 기술문서에 입증해야 한다. | Article 13(7), Article 31, Annex VII | PARTIALLY_VERIFIED | 제조사는 관련 사이버보안 측면과 위험평가를 기술문서화해야 한다. 다만 법령이 '강력한 초기 인증 메커니즘 입증'이라는 특정 증거 항목을 그대로 지정한다고 표현하면 과장이다. |
| CRA-ARCH-MAIN-20261114-004-006 | 24–26 | Raw Text Quote의 (b)/(c)가 secure default와 unauthorized access 문언을 정확히 인용한다. | Annex I Part I(2)(b)–(d) | CONFLICT | (b)는 secure-by-default, (c)는 취약점의 보안 업데이트 처리, (d)는 비인가 접근 방지다. 인용한 (c) 문구는 실제 (d)의 내용을 잘못 배치했다. 직접 인용 재사용을 금지한다. |

## 3. 법령 원문 대조

- Annex I Part I(2)(b): secure-by-default configuration 및 original-state reset 가능성. tailor-made product에 대한 제조자-사업 사용자 간 별도 합의 예외가 있다.
- Annex I Part I(2)(c): 취약점을 security updates로 처리하는 요구이며, 해당되는 자동 업데이트의 기본 설정·opt-out·알림·일시 연기 조건을 포함한다.
- Annex I Part I(2)(d): 적절한 control mechanisms를 통한 unauthorized access 방지(인증, identity/access management 포함) 및 가능한 unauthorized access 보고.
- Annex I Part I(2)(j): 외부 인터페이스를 포함한 attack surface 제한.
- Article 13(7)/Article 31/Annex VII: 관련 사이버보안 측면 및 기술문서화의 근거다. 특정 비밀번호 방식이나 모든 포트 차단의 직접 법적 명령은 아니다.

## 4. #2와 중복성 분석

#2도 secure-by-default, 공격표면, 초기 인증을 다룬다. #4는 주제를 새로 확장하지 않고 유사 주장을 반복하며, 초기 인증/강제 비밀번호/포트 비활성화 표현을 다시 사용한다. 향후 통합 보고서에는 하나의 정본 절로 통합하고 #2/#4는 각각의 원본·SHA·오류 유형만 추적한다. 같은 법적 요구를 신규 Canonical Requirement로 중복 생성하지 않는다.

## 5. 정정 및 후속 조치

1. 제1권/제2권/제품 분류 매트릭스에서 secure-by-default, access control, attack-surface 요구와 구체 구현수단을 구분한다.
2. 기본 비밀번호, 강제 변경, 장치별 초기 인증정보, 포트/서비스 차단은 제품 위험평가·위협모델·사용자 환경에 근거한 설계 결정으로 기록한다.
3. 실제 SKU/계정 모델/포트 목록/디버그 정책/MCU가 확보되면 제품별 설계와 시험 기준을 확정한다.
4. 모든 시험은 현재 NOT_RUN이며, 본 감사는 DUT 시험 또는 CRA 적합성 PASS를 의미하지 않는다.

