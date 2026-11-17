# CRA 보고서 #7 정정 및 기본 자격증명·접근통제 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_092344068727_b0f68c6b.md
- 원본 blob SHA: ff4395ebe2e4f2e5c0b843b8b0a92942f542f6f2
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Annex I Part I point (1)(e) | 존재하지 않는 locator | 실제 접근통제 근거는 Annex I Part I point (2)(d); Part I point (1)은 risk-based cybersecurity level의 일반 원칙 |
| CRA가 모든 기기에 동일한 기본 비밀번호를 명시적으로 금지 | 최종 OJ에 해당 문구 없음 | Official Journal에서 “default passwords” 문구가 검색되지 않는다. 적절한 access-control mechanism의 적합성은 제품 위험평가로 판단 |
| 기기별 랜덤 비밀번호를 반드시 부여 | 특정 구현을 법적 의무로 과장 | device-unique credentials는 강력한 구현 후보지만 CRA (2)(d)가 특정 credential issuance method를 지정하지 않는다 |
| 최초 접속 시 특수문자/길이 복잡성 규칙 강제 | CRA 직접 요구 아님 | 비밀번호 정책은 제품 위험, 사용자, 인증 방식 및 적용 표준에 따라 설계 |
| factory reset 후 초기 고유 비밀번호로 복원 | 특정 동작을 법적 의무로 과장 | Part I (2)(b)는 secure-by-default configuration 및 original-state reset 가능성을 요구하나, 고유 비밀번호 복원/강제 재설정 절차를 지정하지 않는다 |
| IEC 62443 CR 1.1/1.5를 CRA 조항처럼 사용 | 표준과 법령 혼합 | IEC 62443-4-2 요구는 별도 표준 traceability로 관리하고, 적용 판본·제품 범위·인증 목표를 확인 |

## 2. 정확한 CRA 근거

- Annex I Part I point (2)(d): 제품은 appropriate control mechanisms를 통해 unauthorised access를 방지해야 하며, authentication 및 identity/access management systems 등을 포함하고 possible unauthorised access를 보고한다.
- Annex I Part I point (2)(b): secure-by-default configuration으로 제공하고, original state로 reset할 수 있는 가능성을 포함한다.
- Article 13(2)–(3): 제품의 intended purpose, reasonably foreseeable use, operating environment 및 보호 자산을 고려해 cybersecurity risk assessment를 수행·문서화한다.
- Annex I Part I point (1): 제품이 위험에 기반한 적절한 cybersecurity level을 갖도록 설계·개발·생산해야 한다. (1)(e)라는 하위 locator는 존재하지 않는다.

## 3. 수정된 권고 문안

제조사는 Article 13(2)의 위험평가를 바탕으로 적절한 접근통제 메커니즘을 구현해야 하며, 인증 및 identity/access management systems 등을 활용할 수 있다(Annex I Part I point (2)(d)). 공통 기본 비밀번호 제거, device-unique credential, first-use credential setup, MFA, 비밀번호 정책 및 factory-reset credential recovery는 위험평가에 따른 구현 후보로 평가한다. 이를 CRA가 모든 제품에 동일한 구체 방식으로 직접 명령한다고 표현하지 않는다. Secure-by-default 및 original-state reset 요구는 Part I point (2)(b)와 연결하되, reset 후 인증정보 처리 방식은 제품 보안·안전 분석으로 결정한다.

## 4. 서보 드라이브 적용 시 권고

- 로컬 HMI, engineering tool, USB/service port, remote maintenance, industrial Ethernet interfaces별 사용자·권한·인증 요구를 식별.
- shared default credential의 위험을 평가하고, device-unique credential 또는 first-use enrollment 등 대안을 비교.
- password/MFA/credential recovery 정책이 현장 가용성, 유지보수 및 안전 관련 파라미터 접근에 미치는 영향 검증.
- factory reset이 인증정보·네트워크 설정·안전 파라미터를 어떻게 복원하는지 정의하고, 안전 파라미터의 검증된 상태를 훼손하지 않도록 설계.
- IEC 62443-4-2 CR 1.1/1.5 적용 여부는 별도 표준 판본 및 제품 인증 범위에서 확인.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
