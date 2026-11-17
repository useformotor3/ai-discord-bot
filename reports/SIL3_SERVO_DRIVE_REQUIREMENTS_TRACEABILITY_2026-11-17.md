# SIL 3 서보 드라이브 요구사항 추적성 매트릭스
**기준일:** 2026-11-17  
**상태:** v0.1 — Reference architecture 기준, 제품 정격/위험평가 미확정

## 1. 사용 원칙

- 기능안전(FS)과 사이버보안(CYB)은 별도 요구사항 ID, 검증 증거 및 승인 경로를 유지한다.
- SIL 3/PL e 목표는 기계 위험평가와 안전 요구사항 명세서(SRS)에서 각 안전 기능별로 확정한다.
- 드라이브/모듈의 인증값을 완성된 기계 안전 기능의 인증값으로 대체하지 않는다.
- 각 제품의 safety sub-function, encoder, controller, firmware, license 및 communication 조건을 형번 단위로 고정한다.
- 표준 기준은 IEC 61800-5-2:2016+AMD1:2026, IEC 62061:2021+AMD1:2024+AMD2:2026, ISO 13849-1:2023, IEC 61508-1:2010 Ed.2(IEC 61508-1:2026 Ed.3 PRV는 FDIS 투표 2026-11-13 종료, 최종 발행 전)이다.

## 2. 기능안전 요구사항

| ID | 요구사항 | 설계/하드웨어 구현 | 검증 증거 | 상태 |
|---|---|---|---|---|
| FS-001 | E-stop, guard, light curtain 입력의 위험상태 감지 | dual-channel safety inputs, test-pulse/line-fault diagnostics, F-PLC | 단선/단락/교차단락/불일치 fault injection, reaction time | 설계 기준 정의 |
| FS-002 | STO에서 토크 생성 에너지 차단 | 독립 A/B gate-inhibit paths, certified safety module, gate-driver feedback | A/B 개별 차단, single fault, stuck-on, restart inhibit test | 설계 기준 정의 |
| FS-003 | SS1 controlled stop 후 STO | motion deceleration path + independent safety timer/monitor + STO | 감속 ramp, timeout, decel failure, stopping distance | 제품별 구현 확인 필요 |
| FS-004 | SS2/SOS standstill monitoring | safety-rated encoder/feedback, safe speed/position monitor | encoder mismatch, standstill window, position deviation | encoder/제품 미선정 |
| FS-005 | SLS/SDI/SLP/SLI motion limits | safety encoder/dual feedback, safety CPU/drive monitor | overspeed, wrong direction, limit crossing, feedback loss | 제품별 SIL/PL 확인 필요 |
| FS-006 | SBC/SBT 및 수직축 하중 유지 | dual-channel brake output, spring-applied brake, feedback/test | brake open/short/stuck/wear, engagement time, holding torque | 기계 부하 미확정 |
| FS-007 | Safety communication integrity | FSoE 또는 CIP Safety 또는 PROFIsafe, watchdog/CRC/sequence | timeout, CRC, stale data, reconnection, parameter mismatch | 프로토콜 미선정 |
| FS-008 | 전체 안전 기능 SIL 3 PFH | 센서+F-PLC+통신+드라이브+encoder+brake PFH chain | FMEDA, PFH calculation, certificate scope, independent review | 정격/구성 미확정 |
| FS-009 | Hardware fault tolerance 및 CCF | 독립 채널, 전원/clock/watchdog 감시, 배선 분리, diagnostics | HFT/architecture constraint, CCF assessment, fault injection | 상세 설계 필요 |
| FS-010 | Safety parameter integrity | CRC/signature, access control, safety signature, version lock | unauthorized change, corrupt parameter, rollback, restore test | 툴/프로세스 미선정 |
| FS-011 | Mission time 및 diagnostic interval | latest IEC 61800-5-2 AMD1:2026 + vendor manual | diagnostic test schedule, maintenance record, updated certificate | 제조사 최신 문서 확인 필요 |
| FS-012 | STO/SS1과 주전원 절연 구분 | separate isolator/LOTO and DC-link discharge | maintenance isolation procedure, residual voltage test | 설계 시 반영 |
| FS-013 | Brake/vertical axis hazard | fail-safe brake and mechanical risk assessment | loss-of-power, brake delay, gravity-load test | 수직축 여부 미확정 |
| FS-014 | EMC/thermal/mechanical immunity | PCB isolation, shielding, grounding, thermal design | IEC 61800-5-2 AMD1:2026 immunity test plan | 환경/정격 미확정 |

## 3. 사이버보안 요구사항 — 별도 추적

| ID | CRA 근거/목표 | 구현 후보 | 검증 증거 | 법적/설계 구분 |
|---|---|---|---|---|
| CYB-001 | Annex I Part I (2)(b): secure-by-default 및 초기 상태 reset | secure configuration, factory reset, role-based commissioning | default configuration audit, reset test | 법적 목표는 secure-by-default; 구체 credential 방법은 설계 선택 |
| CYB-002 | Annex I Part I (2)(d): unauthorized access 방지 | authentication, identity/access management, service access control | brute-force/unauthorized access test | 법적 목표와 특정 MFA/TPM 구현을 구분 |
| CYB-003 | Annex I Part I (2)(e): data/command/program/config integrity | signed firmware, secure boot, parameter CRC/signature | tampered image/parameter rejection | digital signature는 구현 선택 |
| CYB-004 | Annex I Part I (2)(l): relevant internal activity logging | security event log, access/change audit, opt-out where required | access/config change log test, storage integrity | CRA 문언에 맞는 이벤트 범위와 opt-out 반영 |
| CYB-005 | Annex I Part II (2)/(7)/(8): vulnerability remediation and secure/free security updates | signed update package, safe rollback/recovery, update channel | signature failure, rollback, interrupted update | update mechanism은 설계 선택, free security update는 별도 CRA 의무 |
| CYB-006 | Annex I Part II (5)/(6): CVD policy/contact | PSIRT intake, vulnerability contact address, CVD process | public policy/contact and triage records | security.txt/PGP/SLA/CVE는 특정 형식으로 직접 강제되지 않음 |
| CYB-007 | Article 14/15/16: mandatory/voluntary reporting | incident/vulnerability classification and reporting workflow | trigger/clock/recipient evidence | Article 14는 actively exploited vulnerability 및 severe incident 트리거에 한정 |
| CYB-008 | Article 13(8)/(9): support period/update availability | support policy, patch retention/release records | support-period and update availability audit | 5-year rule with shorter expected-use exception; 10-year update availability separate |
| CYB-009 | Article 13(18)/(19), Annex II: user information and support end date | installation/security instructions, support end-date notice | manual review, end-date purchase-time display | user instructions and retention separate from technical documentation |
| CYB-010 | Article 31/Annex VII, Article 13(13): technical documentation | threat model, architecture, SBOM, security design and test evidence | technical file and retention audit | technical documentation is not Annex VI; retain at least 10 years or support period, whichever longer |

## 4. 요구사항에서 시험까지의 추적성

| 검증 단계 | 산출물 | 승인 기준 |
|---|---|---|
| 위험평가 | Hazard analysis, PLr/SIL target, operating modes | 각 위험에 대한 안전 기능과 safe state 정의 |
| SRS | Safety function, trigger, safe state, reaction time, reset, bypass, diagnostics | 각 FS-ID와 제품 기능/외부 요소 연결 |
| 아키텍처 | Block diagram, schematics, safety partition, FMEA/FMEDA | single point/common cause 검토 및 architecture constraints 통과 |
| 정량 계산 | PFH chain, MTTFd/DCavg/HFT/SFF/CCF where applicable | 전체 안전 기능의 목표 SIL/PL 충족 |
| 구현 검증 | PCB, firmware, parameter, communication | 독립 검토 및 traceability complete |
| 시험 | fault injection, response time, EMC/thermal/mechanical, brake/load tests | 모든 SRS acceptance criteria 통과 |
| 유효성 확인 | Validation report, residual risk, manual | 독립 reviewer 승인 및 evidence archive |

## 5. 미결 항목

1. 모터/드라이브 정격 및 입력 전원 범위.
2. 안전 기능별 SIL/PLr, stop category, maximum stopping time/distance.
3. rotary/linear/direct-drive, 수직축/중력 부하 여부.
4. encoder/feedback type 및 dual-feedback 필요 여부.
5. F-PLC와 FSoE/CIP Safety/PROFIsafe 중 선택.
6. 정확한 제품 형번, firmware, safety module, license 및 TÜV certificate scope.
7. IEC 61800-5-2 AMD1:2026에 대한 각 제조사 인증 갱신 여부.
8. EMC/thermal/mechanical operating environment 및 mission time.
9. 외부 brake/contactor/isolator의 안전 기능 포함 여부.

## 6. 기준 출처

- IEC 61800-5-2:2016+AMD1:2026: https://webstore.iec.ch/en/publication/117563
- IEC 62061:2021+AMD1:2024+AMD2:2026: https://webstore.iec.ch/en/publication/112847
- ISO 13849-1:2023: https://www.iso.org/standard/73481.html
- IEC 61508-1:2010 / 2026 PRV(최종 발행 예정 2027-01-22): https://webstore.iec.ch/en/publication/117296
- CRA final OJ: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

**주의:** 이 매트릭스는 설계 추적성의 시작점이다. SIL 3 인증서, FMEDA, PFH 계산 및 최종 회로 검증을 대체하지 않는다.
