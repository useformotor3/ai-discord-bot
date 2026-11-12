# CRA 통합 요구사항–위협–HW/FW–시험–증거 추적성 매트릭스

**기준일:** 2026-11-12  
**브랜치:** `cra-project-foundation`  
**상태:** 일반 참조 모델 / 실제 제품 적용성·설계 구현·시험 결과 UNVERIFIED  
**목적:** 기존 법령 추적성 매트릭스, 위협 모델, 하드웨어 아키텍처, 시험·증거 대장을 하나의 end-to-end 추적 체계로 연결한다.

## 1. 읽는 법과 상태 경계

- CRA 조항은 법령상 결과/프로세스 요구를 식별한다. 표의 HW/FW 블록은 가능한 구현 후보이며 법령이 특정 회로·MCU·암호 알고리즘을 직접 요구한다는 뜻이 아니다.
- 위협 ID는 일반 서보 드라이브 참조 모델의 분석 시나리오다. 제품에 해당 인터페이스/기능이 없으면 제품 경계와 설계 증거를 근거로 NOT_APPLICABLE 판정한다.
- 시험 ID는 시험 설계 항목이다. 현재 실제 DUT 시험은 실행되지 않았으므로 모두 NOT_RUN이다.
- EV ID는 증거 산출 시 사용할 네이밍 패턴이다. 실제 evidence artifact가 존재한다는 뜻이 아니다.
- 제품 SKU, EU 공급 형태, 실제 인터페이스, ST MCU 전체 주문 코드/실리콘 리비전, 안전 아키텍처가 확인되기 전까지 제품 적용성·위험도·합격 기준은 UNVERIFIED다.

## 2. End-to-end 통합 추적표

| Trace ID | CRA 근거 / 의무 영역 | 요구 결과(요약) | 자산 / 위협 연결 | HW/FW 블록 및 통제 후보 | 시험 ID | 증거 ID 패턴 | 현재 상태 |
|---|---|---|---|---|---|---|---|
| TR-01 | Annex I Part I(1),(2)(a) | 위험 기반 보안 수준, 알려진 악용 가능 취약점 처리 | AST-01/08; TH-16/17 | HW-01 MCU, HW-03 통신 경계; 위협모델·SBOM·취약점 triage·release gate | TST-SUP-01..03, TST-OPS-01 | EV-SUP-001, EV-OPS-001 | 제품 적용 UNVERIFIED |
| TR-02 | Annex I Part I(2)(b) | secure-by-default 및 안전한 원래 상태 복구 | AST-05/06; TH-09/14 | HW-04 서비스/디버그, FW 기본 설정·최소 서비스·인증된 reset | TST-AUTH-03, TST-SVC-01..03 | EV-AUTH-003, EV-SVC-001 | UNVERIFIED |
| TR-03 | Annex I Part I(2)(c); Part II(2),(7) | 취약점 수정 업데이트 가능, 안전한 배포, 자동 업데이트 적용 시 관련 조건 | AST-01/10; TH-01..04 | HW-01 boot chain, HW-05 NVM, HW-08 reset/power; 서명/무결성·대상 ID·버전 정책·복구 | TST-UPD-01..06 | EV-UPD-001..006 | UNVERIFIED |
| TR-04 | Annex I Part I(2)(d); Part II(6) | 비인가 접근 방지/보고 및 신고 연락처 제공 | AST-05/06/07; TH-06/09/10/14 | HW-03 통신 경계, HW-04 service/debug; 역할·권한·인증·접근 이벤트 | TST-CMD-01..03, TST-SVC-01..03, TST-DBG-01..02, TST-AUTH-01..03 | EV-CMD-001, EV-SVC-001, EV-DBG-001, EV-AUTH-001 | UNVERIFIED |
| TR-05 | Annex I Part I(2)(e) | 저장·전송·처리 데이터 기밀성 | AST-02/05/06/09; TH-12/14/18 | HW-01 MCU 보안영역, HW-07 선택적 secure element, FW key lifecycle·통신 보호 | TST-KEY-01..03, TST-REM-02 | EV-KEY-001..003, EV-REM-002 | UNVERIFIED |
| TR-06 | Annex I Part I(2)(f) | 데이터·명령·프로그램·설정 무단 변경 방지 및 손상 보고 | AST-01/03/05; TH-01/02/06/07/11 | HW-01 boot chain, HW-05 NVM, HW-03 통신 경계; image/parameter integrity·range/state validation | TST-UPD-02..04, TST-CMD-02..04, TST-NVM-01..03 | EV-UPD-002, EV-CMD-004, EV-NVM-001 | UNVERIFIED |
| TR-07 | Annex I Part I(2)(g) | 목적에 필요한 최소 데이터 처리 | AST-08; TH-15/18 | FW telemetry/log minimization, data inventory, optional remote-service boundary | TST-LOG-01..02, TST-REM-01 | EV-LOG-001, EV-REM-001 | UNVERIFIED |
| TR-08 | Annex I Part I(2)(h),(i) | 필수 기능 및 연결된 다른 기기/네트워크 가용성·DoS 회복력 | AST-03/07; TH-05/08/18 | HW-02 PHY, HW-03 통신 경계, HW-08 power/reset; bounded queues, rate limiting, task isolation | TST-NET-01..03, TST-AVL-01..03, TST-REM-03 | EV-NET-001, EV-AVL-001..003 | UNVERIFIED |
| TR-09 | Annex I Part I(2)(j) | 외부 인터페이스 포함 공격 표면 제한 | AST-07; TH-05/09/10/18 | HW-02 PHY, HW-04 debug/service; interface inventory, unused port/service removal/restriction | TST-NET-03, TST-SVC-01, TST-DBG-01, TST-REM-01 | EV-IF-001, EV-DBG-001 | UNVERIFIED |
| TR-10 | Annex I Part I(2)(k) | 적절한 exploit mitigation | AST-01/03/05/06; TH-05/06/09/12/13 | HW-01 MCU, HW-03 comm boundary, HW-09 sensor interface; privilege separation, input validation, memory protection | TST-NET-02, TST-CMD-01..04, TST-SNS-01..03, TST-KEY-01 | EV-FUZZ-001, EV-CMD-001, EV-SNS-001 | UNVERIFIED |
| TR-11 | Annex I Part I(2)(l) | 내부 활동 기록·모니터링 및 보안 정보 제공 | AST-08; TH-09/14/15 | FW audit logging, event priority, bounded storage, optional log integrity | TST-LOG-01..02, TST-AUTH-02 | EV-LOG-001..002, EV-AUTH-002 | UNVERIFIED |
| TR-12 | Annex I Part I(2)(m) | 사용자 데이터/설정 영구 삭제 및 안전한 전송 | AST-02/05/06; TH-11/12/14 | HW-05 NVM, HW-07 optional SE; authenticated reset, key destruction, decommission workflow | TST-NVM-01..03, TST-KEY-03 | EV-NVM-003, EV-KEY-003 | UNVERIFIED |
| TR-13 | Annex I Part II(1) | 기계 판독 SBOM, 최소 top-level dependencies | AST-08/09; TH-16 | Build/release pipeline, dependency inventory, product-version mapping | TST-SUP-01, TST-SUP-03 | EV-SUP-001..003 | UNVERIFIED |
| TR-14 | Annex I Part II(2),(3) | 취약점 지체 없이 처리, 기술적으로 가능한 경우 보안 업데이트 분리, 효과적·정기적 시험/검토 | AST-01/08/10; TH-01..04/16/17 | PSIRT, patch branch, security regression, vulnerability triage | TST-SUP-02..03, TST-OPS-01..02, TST-UPD-01..06 | EV-PSIRT-001, EV-UPD-001 | UNVERIFIED |
| TR-15 | Annex I Part II(4),(5),(6) | 수정 취약점 정보 공개(정당한 지연 가능), CVD 정책, 연락처 | AST-08; TH-16/17 | PSIRT/CVD 운영, advisory workflow, public contact | TST-OPS-01, TST-OPS-04, TST-SUP-02 | EV-OPS-001..004 | UNVERIFIED |
| TR-16 | Annex I Part II(7),(8) | 안전한 업데이트 배포, 원칙적 무상 보안 업데이트(맞춤형 제품 예외 조건) | AST-01/10; TH-01..04/17 | Signed release, distribution channel, support/service policy | TST-UPD-01..06, TST-OPS-02 | EV-UPD-001..006, EV-SUP-002 | UNVERIFIED |
| TR-17 | Article 13(2)–(7) | 제품 위험평가, 구성요소 due diligence, 기술문서에 반영 | AST-01..10; TH-01..18 | Product boundary, threat model, supplier inventory, risk acceptance, technical file | TST-SUP-02..03, TST-REM-01, all applicable security tests | EV-RISK-001, EV-TD-001 | UNVERIFIED |
| TR-18 | Article 13(8)–(9) | 위험/예상 사용기간 기반 지원기간(법정 예외 포함), 보안 업데이트 보존 | AST-08/10; TH-17 | Product support policy, update archive, retention/restore process | TST-OPS-02 | EV-SUPPORT-001, EV-RETENTION-001 | UNVERIFIED |
| TR-19 | Article 14(1)–(4),(8) | actively exploited vulnerability와 severe incident를 구분해 신고·사용자 통지 | AST-08/10; TH-16/17 | PSIRT incident classification, ENISA SRP workflow, notification and timestamp controls | TST-OPS-03..04 | EV-INC-001..004 | UNVERIFIED |
| TR-20 | Article 7, Annex III, Implementing Regulation (EU) 2025/2392 | Important/critical product 분류는 Annex III category와 core functionality에 근거 | 제품 경계 전체; MCU 역할·제품 core functionality 확인 | Product boundary analysis, intended purpose, MCU functionality mapping; 분류를 MCU 탑재 사실만으로 추정 금지 | TST-REM-01 및 product classification review | EV-BOUNDARY-001, EV-CLASS-001 | UNVERIFIED |

## 3. 시험 대장과 통합 매트릭스의 연결 규칙

1. 모든 요구사항은 `TR-xx` 고유 ID를 가진다.
2. 위협 모델 ID는 `TH-xx`, 시험 ID는 `TST-...`, 증거 파일 ID는 `EV-...`로 관리한다.
3. 요구사항 한 개가 여러 위협/시험으로 분기될 수 있다. 하나의 시험도 여러 요구사항을 뒷받침할 수 있으나, 시험 보고서에는 실제 검증한 요구사항 ID를 명시한다.
4. `PASS`는 해당 시험의 승인된 합격 기준을 만족했다는 뜻만 가진다. CRA 적합성/제품 분류/인증 결론은 별도 법적·기술적 검토가 필요하다.
5. `NOT_APPLICABLE`은 인터페이스/기능 부재와 제품 경계 근거, 검토자 승인 기록이 있을 때만 허용한다.
6. 실제 증거는 원시 파일, SHA-256, DUT/FW/MCU 식별, 시험 환경, 재현 절차, 승인자까지 보존한다. 비밀키/실제 자격증명은 저장하지 않는다.

## 4. 제품 경계 및 부품 확인 게이트

제품 경계 템플릿 [SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md)의 BD-01..BD-15를 먼저 채운다. 특히 drive main unit, embedded firmware, 별도 fieldbus/network module, engineering PC tool, mobile app, cloud/remote diagnostics, motor/encoder/sensor, upper PLC/HMI/SCADA를 구분한다.

부품별 게이트:
- ST MCU 전체 주문 코드와 silicon revision, 해당 부품의 datasheet/RM/errata 확보
- secure boot/secure update/debug lifecycle/key storage/crypto/RNG/memory protection/flash topology의 실제 지원 확인
- boot/update/service/debug/fieldbus interface와 안전 아키텍처 경계 확인
- 각 선택 통제의 성능·비용·제조·RMA 영향 검토

현재 모두 UNVERIFIED다. ST AN5156은 제품군 개요 자료이며 정확한 부품 기능은 해당 부품의 공식 문서로 재확인해야 한다.

## 5. 우선 실행 백로그

| Priority | 작업 | 완료 조건 | 의존성 |
|---|---|---|---|
| P0-A | 제품 경계 BD-01..BD-15 확보 | SKU, 공급 형태, intended purpose, 실제 인터페이스/원격 기능, 구성품 경계에 증거 첨부 | 사용자/제품 자료 |
| P0-B | MCU part gate | 전체 주문 코드·실리콘 revision으로 기능별 공식 문서/errata 교차확인 | P0-A 또는 임시 후보 part |
| P0-C | boot/update/debug 설계 선택 | 신뢰 체인·복구·생산 lifecycle 설계 및 검토 근거 | P0-B |
| P0-D | 통신/명령 신뢰 경계 설계 | 외부 입력 파서·인증·권한·bounded resource 설계 | 실제 프로토콜/토폴로지 |
| P0-E | 위험·안전 성능 한계 승인 | 제어주기/지터/부하/복구시간 및 보안 실패 시 출력 상태 승인 | 제품 요구사항·기능안전 분석 |
| P1-A | 시험 실행 | 승인된 DUT/환경/합격 기준과 raw evidence/hash 확보 | P0-A..E |
| P1-B | PSIRT/지원/신고 운영 검증 | CVD, support period, update retention, Article 14 tabletop 증거 | 조직/제품 운영 정보 |

## 6. 근거 및 연결 문서

- [CRA 법령 검증 기준선](CRA_VERIFIED_BASELINE_2026-11-12.md)
- [기존 요구사항별 HW/FW 추적성 매트릭스](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md)
- [위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md)
- [하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md)
- [시험·증거 대장](SECURITY_TEST_EVIDENCE_REGISTER.md)
- [제품 경계 템플릿](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md)
- [검증 프로토콜](VERIFICATION_PROTOCOL.md)
- [주장·근거 대장](CLAIM_EVIDENCE_LEDGER.md)

