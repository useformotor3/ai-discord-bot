# CRA 보고서 #5 정정 및 물리/논리 인터페이스 공격 표면 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_085437245683_43a9bcbe.md
- 원본 blob SHA: e6dfcf688a3859b9468dbe7a4ef28c2d7d3c94ad
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| Annex I Part I point 3(f) | 존재하지 않는 final OJ locator | attack surface 제한은 Annex I Part I point (2)(j) |
| Recital 46의 physical/logical ports quote | final OJ 원문과 일치하지 않음 | final Recital 9는 물리적 하드웨어 인터페이스 및 논리적 연결 예시를 설명하지만, 원본의 “ports limited to what is necessary” / “unnecessary logical interfaces disabled by default” 문구는 확인되지 않는다 |
| JTAG/SWD/UART를 양산 전에 영구 disable/eFuse blow | 특정 구현을 법적 의무로 확대 | attack surface 제한은 요구되나 영구 디버그 차단, eFuse/OTP, 특정 root-of-trust 방식은 법령이 지정하지 않는다 |
| 모든 비필수 네트워크 포트를 완전히 disable | 과도한 단정 | 필요성·위험평가에 따라 외부 인터페이스 attack surface를 제한한다. 인증, 접근 제한, service-mode, physical controls 등 다양한 방법 가능 |
| IEC 62443-4-2 CR 2.8/2.9/2.10 | 별도 표준 요구 | 적용 판본/제품 범위/적합성 평가를 별도 확인하며 CRA 조문과 혼합하지 않는다 |

## 2. 정확한 법적 근거

- Annex I Part I point (2)(j): 제품은 attack surfaces, including external interfaces를 제한하도록 설계·개발·생산되어야 한다.
- Annex I Part I point (2)(b): secure-by-default configuration 및 original-state reset 가능성.
- Annex I Part I point (2)(d): appropriate control mechanisms를 통한 unauthorised access 방지, authentication/identity/access management 예시.
- Recital 9: 제품은 물리적 hardware interfaces 및 network sockets/pipes/files/APIs 등 논리적 인터페이스를 통해 연결될 수 있으므로 간접 연결을 포함한 제품 보안을 고려해야 한다. 이는 개별 디버그 포트를 영구 비활성화하라는 직접 명령이 아니다.

## 3. 수정된 권고 문안

제조사는 제품의 물리적·논리적 외부 인터페이스를 포함한 attack surface를 위험평가에 따라 제한해야 한다(Annex I Part I point (2)(j), Article 13(2)). JTAG/SWD/UART, service/debug ports, network services 및 maintenance interfaces는 제품 lifecycle, 제조·시험·현장 유지보수 시나리오, 접근통제, 인증, 물리적 보호 및 복구 가능성을 고려해 보호한다. 영구 disable, eFuse/OTP, challenge-response service access, default-off network services는 가능한 설계 선택이지 CRA가 모든 제품에 지정한 단일 방식이 아니다.

## 4. 서보 드라이브 적용 시 설계 항목

- 개발·양산·현장 서비스 모드별 debug/service interface inventory 작성.
- 생산 종료 시 debug port 상태, 인증, 물리적 접근, tamper evidence 및 service authorization 검증.
- 영구 차단이 필요한 인터페이스와 안전한 인증 기반 유지보수 접근이 필요한 인터페이스를 구분.
- eFuse/OTP 설정은 복구 불가능성, RMA, 현장 장애 분석, secure boot, firmware recovery와 함께 검토.
- 물리 포트 차단이 안전 관련 진단/정비를 방해하지 않는지 기능안전 및 유지보수 절차 검토.
- IEC 62443-4-2 CR 2.8/2.9/2.10은 별도 요구 매핑표에 기록.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
