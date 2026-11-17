# CRA 보고서 #11 정정 및 Secure-by-Default/Attack Surface 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_102531422970_665697b7.md
- 원본 blob SHA: b7555b23da08ff49e50d862aa3ec5485c104338c
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장 | 판정 | 정정 |
|---|---|---|
| Annex I Part I (2)(d)/(e) 원문 인용 | 정확 | 두 인용은 최종 OJ 문언과 일치 |
| 모든 비필수 포트·서비스를 기본 비활성화해야 함 | 구현 권고를 일률 의무로 확대 | (d)는 attack surface, including external interfaces를 제한하라고 요구하지만 모든 제품의 모든 비필수 포트를 예외 없이 disable하라고 문언화하지 않는다 |
| EtherCAT/PROFINET만 제어 필수, Modbus TCP 등은 모두 disable | 제품별 사실관계 과잉 일반화 | 실제 제어·안전·시운전·유지보수 아키텍처에 따라 attack surface와 operational need를 평가해야 한다 |
| 모든 추가 기능은 관리자 인증 후 opt-in만 가능 | 법령에 없는 특정 절차 | (e)는 secure-by-default configuration을 요구하지만 모든 추가 기능의 opt-in 절차나 관리자 인증 방식을 직접 지정하지 않는다 |
| least privilege/minimal functionality가 CRA 조항의 직접 문언 | 조항 혼합 | 이는 유용한 설계 원칙일 수 있으나 (d)/(e)의 직접 인용이 아니다. IEC 62443 참조 요구와 CRA 법령을 별도로 추적 |
| factory reset to original state | 정확 | (e)에 명시된 요구 |

## 2. 정확한 법적 근거

- Annex I Part I point (2)(d): 제품은 attack surfaces를 제한하도록 설계·개발·생산되어야 하며, external interfaces를 포함한다.
- Annex I Part I point (2)(e): 제품은 secure-by-default configuration으로 제공되어야 하며, original state로 reset할 수 있는 가능성을 포함한다.
- Article 13(2)–(3): 제품별 intended purpose, reasonably foreseeable use, operating environment, protected assets를 고려한 사이버보안 위험평가와 문서화.
- Annex I Part I point (2)(d)/(e)는 구체 포트 목록, 프로토콜별 금지, opt-in 인증 UI 또는 모든 비필수 서비스의 단일 비활성화 방법을 직접 지정하지 않는다.

## 3. 수정된 권고 문안

제조사는 제품의 외부 인터페이스를 포함한 공격 표면을 제한하고, secure-by-default configuration으로 제품을 제공하며, original state로 재설정할 수 있는 기능을 제공해야 한다(Annex I Part I point (2)(d)/(e)). 서보 드라이브의 HTTP/FTP/Telnet/Modbus TCP/debug/service interfaces는 제품 위험평가와 운영 목적에 따라 필요성, 기본 상태, 인증·권한, 접근 경로 및 복구 영향을 분석한다. 불필요한 서비스 비활성화, 관리자 opt-in, least privilege 및 최소 기능 프로파일은 적절한 구현 후보이나 모든 제품에 대한 법령의 구체적 단일 절차로 표현하지 않는다.

## 4. 서보 드라이브 적용 시 설계 항목

- 각 포트/서비스별 목적, 사용 주체, 기본 활성 여부, 인증, 권한, 노출 경로 및 유지보수 시나리오를 inventory화.
- EtherCAT/PROFINET/Modbus TCP 등은 제품의 실제 제어·진단·유지보수 구조와 threat model에 따라 평가.
- factory reset 시 사용자 설정, 네트워크 주소, 안전 파라미터, 인증정보 및 보안 설정의 복원/보존 정책을 명확히 정의.
- reset 기능이 안전 관련 파라미터나 안전 기능의 검증된 상태를 훼손하지 않는지 기능안전 검토.
- IEC 62443-4-2의 개별 요구는 별도 적용성/인증 범위 검토 후 CRA 조항과 구분해 traceability를 유지.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
