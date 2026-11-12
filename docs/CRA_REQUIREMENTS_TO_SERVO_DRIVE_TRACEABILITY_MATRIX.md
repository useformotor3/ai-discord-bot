# CRA 요구사항 → 서보 드라이브 HW/FW/시험/증거 추적성 매트릭스 (초안)

- 기준일: 2026-11-12
- 상태: 일반 참조 설계 / 제품별 적용성 및 시험 기준 미확정
- 목적: 검증된 CRA 요구사항을 실제 개발 작업과 시험 증거로 연결한다. 이 문서는 법령 조항을 설계 통제로 번역한 초안이며 제품별 적합성 결론이 아니다.
- 상위 근거: [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md), [SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md), [SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md)
- 검증 운영 기준: [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md)

## 1. 사용 규칙

- **법적 요구** 열은 법령상 결과/프로세스 요건을 요약한다.
- **설계 후보** 열은 서보 드라이브에 적용할 수 있는 통제 후보이며, 법령이 특정 칩·알고리즘·회로를 직접 명령한다는 뜻이 아니다.
- **시험/합격 기준**은 개발 검증을 위한 제안이다. 제품 위험평가, 성능 요구, 기능안전 분석, MCU 데이터시트/RM/Errata를 반영해 승인해야 한다.
- **증거 파일**은 실제 산출물이 생성되기 전까지 placeholder다.
- 현재 제품 SKU, EU 판매 형태, 통신 옵션, MCU 주문 코드가 없으므로 모든 제품별 적용은 UNVERIFIED다.

## 2. 제품 속성 요구사항 — Annex I Part I

| ID | 법령 근거 | 법적 요구/조건 | 서보 드라이브 설계 후보 (비법정 구현 예) | 제안 시험 및 합격 기준 | 필요한 객관적 증거 | 상태 |
|---|---|---|---|---|---|---|
| P1-01 | Part I(1), (2)(a) | 위험 기반 적정 사이버보안 수준, 알려진 악용 가능 취약점 없이 시장 제공 | 위협모델, 취약점 스캔, 릴리스 차단 게이트, 구성요소 CVE 매핑 | 릴리스 시점 알려진 exploitable CVE 조사 완료; 미해결 항목은 승인된 위험처리/출시 보류 기준 적용 | Risk assessment, SBOM, VEX/취약점 평가, release checklist | UNVERIFIED |
| P1-02 | Part I(2)(b) | Secure-by-default 구성, 맞춤형 제품 관련 별도 합의 예외; original state 복구 가능성 | 기본 계정/서비스 최소화, 초기 보안 설정, 인증된 factory reset | 공장 초기화 후 보안 설정이 취약한 기본값으로 퇴행하지 않음; 기본 구성 검토 통과 | Default configuration baseline, reset test log, user manual | UNVERIFIED |
| P1-03 | Part I(2)(c) | 취약점은 보안 업데이트로 처리 가능해야 함. 해당되는 자동 업데이트는 기본 설정/opt-out/알림/일시 연기 조건 확인 | 서명 검증 업데이트 패키지, 사용자 알림, 업데이트 정책/연기 기능 | 유효 이미지 설치 성공; 변조/손상 이미지 거부; opt-out/연기/알림 동작 확인; 자동 업데이트 적용성 판단 기록 | Update architecture, signed test images, update logs, policy | UNVERIFIED |
| P1-04 | Part I(2)(d) | 적절한 통제 메커니즘으로 비인가 접근 방지 및 가능한 비인가 접근 보고 | 사용자/역할 권한, 서비스 권한 분리, 인증된 디버그/서비스 모드 | 미인증·권한 없는 요청이 보호 기능/파라미터를 변경하지 못함; 실패 이벤트 기록 | Access-control matrix, auth test report, audit log | UNVERIFIED |
| P1-05 | Part I(2)(e) | 저장/전송/처리되는 데이터의 기밀성 보호 | 필요한 데이터에 대한 at-rest/in-transit 보호, 키 수명주기 | 위협모델이 지정한 민감 데이터가 평문 노출되지 않음; 키/암호 설정 검토 통과 | Data-flow map, crypto configuration, key handling procedure | UNVERIFIED |
| P1-06 | Part I(2)(f) | 데이터·명령·프로그램·설정의 무단 조작/변경 방지 및 corruption 보고 | 펌웨어/설정 무결성 보호, 파라미터 범위검사, 업데이트 이미지 인증 | 저장·전송 데이터/명령 변조 시 검출/거부; corruption event 처리 확인 | Integrity design, fault-injection logs, boot/update test | UNVERIFIED |
| P1-07 | Part I(2)(g) | 의도된 목적에 필요한 적절·관련·최소 데이터만 처리 | 진단 로그 최소화, 불필요한 사용자/운영 데이터 수집 제거 | 데이터 인벤토리의 각 필드가 목적과 연결되고 불필요 필드가 없음 | Data inventory, privacy/security design review | UNVERIFIED |
| P1-08 | Part I(2)(h) | 필수·기본 기능 가용성 보호, 사고 후에도 DoS 회복력/완화 조치 | 통신 flood 격리, watchdog, bounded queue, safe recovery path | 정의된 부하/DoS 시나리오에서 제어 루프의 허용 성능/안전 경계를 벗어나지 않거나 위험평가된 안전 상태로 전이 | DoS/flood test, timing trace, recovery log, hazard analysis | UNVERIFIED |
| P1-09 | Part I(2)(i) | 연결된 다른 기기/네트워크의 가용성에 대한 부정적 영향 최소화 | 네트워크 rate limit, broadcast/multicast 제어, 프로토콜 오류 격리 | 비정상 트래픽 생성 시 연결망의 승인된 가용성 기준을 위반하지 않음 | Network load test, packet capture, integration report | UNVERIFIED |
| P1-10 | Part I(2)(j) | 외부 인터페이스를 포함한 공격 표면 제한 | 불필요한 포트/서비스 제거, 서비스 포트 접근 정책, debug lifecycle | 제품 포트/서비스 인벤토리와 실제 스캔 결과 일치; 불필요한 인터페이스 노출 없음 | Interface inventory, port scan, production configuration | UNVERIFIED |
| P1-11 | Part I(2)(k) | 적절한 exploit mitigation으로 사고 영향 감소 | privilege separation, memory protection, secure state machine, input validation | 정해진 공격/오류 주입에서 권한 상승/제어 명령 변조/비인가 실행이 발생하지 않음 | Threat model, fuzzing, penetration test, MPU config | UNVERIFIED |
| P1-12 | Part I(2)(l) | 사용자 opt-out 메커니즘을 포함해 관련 내부 활동을 기록·모니터링하고 보안 정보 제공 | 이벤트 로그, 접근/설정 변경 감사, 시간/용량 관리 | 권한 변경/서비스 접근/업데이트/무결성 실패가 로그에 남고 로그 포화 시 동작 정의 | Logging spec, sample logs, log integrity/retention test | UNVERIFIED |
| P1-13 | Part I(2)(m) | 사용자 데이터/설정 영구 삭제 가능; 다른 제품/시스템으로 전송 시 안전하게 수행 | 인증된 초기화, 키 폐기, 안전한 설정 삭제 | reset/decommission 후 지정 데이터 복구 불가 또는 허용된 보존 항목만 남음 | Secure erase test, decommission procedure, key zeroisation evidence | UNVERIFIED |

## 3. 제조자 취약점 처리 요구사항 — Annex I Part II

| ID | 법령 근거 | 법적 요구/조건 | 서보 드라이브 운영/설계 후보 | 제안 시험 및 합격 기준 | 필요한 객관적 증거 | 상태 |
|---|---|---|---|---|---|---|
| P2-01 | Part II(1) | 제품 구성요소/취약점 식별·문서화; 일반적 기계 판독 형식 SBOM, 최소 top-level dependencies | Firmware build pipeline에서 SPDX/CycloneDX 등 SBOM 생성, release별 보관 | 릴리스 이미지/소프트웨어 구성과 SBOM 간 일치; 최소 top-level dependencies 누락 없음 | SBOM, build manifest, dependency inventory | UNVERIFIED |
| P2-02 | Part II(2) | 제품 위험에 비례해 취약점 지체 없이 처리; 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리 | PSIRT workflow, severity triage, patch branch, security-only release | 샘플 취약점의 접수→분석→수정→검증→배포 추적; 기술적으로 분리 불가한 경우 근거 문서 | Vulnerability procedure, issue records, release notes, separation rationale | UNVERIFIED |
| P2-03 | Part II(3) | 효과적이고 정기적인 보안 테스트/검토 | 정적 분석, dependency scan, fuzzing, protocol/security regression, penetration testing | 정기 주기와 release gate 준수; critical/high finding disposition 기록 | Security test plan/report, CI logs, remediation evidence | UNVERIFIED |
| P2-04 | Part II(4) | 보안 업데이트 제공 후 수정 취약점 정보를 공개. 정당한 경우 패치 기회가 주어질 때까지 공개 지연 가능 | Security advisory/CVE handling, product/version impact statement | 패치 제공과 사용자 정보 공개 시점 및 지연 사유 추적 가능 | Advisory, disclosure decision record, release timestamp | UNVERIFIED |
| P2-05 | Part II(5) | Coordinated vulnerability disclosure 정책 수립·시행 | PSIRT/CVD policy, researcher coordination, response SLA | 외부 신고 시 접수·확인·분류·조율·종결 흐름 모의시험 | Published CVD policy, intake records, tabletop report | UNVERIFIED |
| P2-06 | Part II(6), Annex II(2) | 제품/제3자 구성요소 취약점 제보를 촉진하고 신고 연락처 제공 | 보안 신고 이메일/웹폼/제품 문서 내 단일 연락처 | 외부 사용자가 연락처를 찾고 신고할 수 있는지 사용성 확인 | Public contact point, user manual, intake test | UNVERIFIED |
| P2-07 | Part II(7) | 취약점을 적시에 수정/완화하도록 안전한 업데이트 배포 메커니즘 제공 | Authenticated update channel, package integrity/authenticity checks, staged rollout/recovery | 전송/저장 중 변조된 업데이트 거부; 배포 실패 복구; 대상 버전 식별 | Update distribution architecture, tamper test, rollout logs | UNVERIFIED |
| P2-08 | Part II(8) | 보안 문제 수정 업데이트 지체 없이 제공; 맞춤형 제품에 대한 제조자-사업 사용자 간 별도 합의 예외 외에는 무상 | 지원기간 내 보안 패치 정책과 비용/계약 분리 | 취약점 패치 제공 시 유료 라이선스/계약 장벽이 없는지 정책 감사 | Security update policy, contract/service terms review | UNVERIFIED |

## 4. 제조자 의무 및 신고 — Articles 13–14

| ID | 법령 근거 | 개발/운영 의무 | 시험·증거 |
|---|---|---|---|
| M-01 | Article 13(2)–(4) | intended purpose, reasonably foreseeable use, 운영 환경/보호 자산을 반영한 위험평가 및 기술문서 포함. 비적용 요구사항은 근거 기록 | Product risk assessment, applicability matrix, technical documentation |
| M-02 | Article 13(5)–(7) | 제3자/오픈소스 구성요소 due diligence, 구성요소 취약점 통보·수정, 관련 기록 | Supplier assessment, SBOM, vulnerability records, component notification evidence |
| M-03 | Article 13(8) | 제품 예상 사용기간/사용자 기대/제품 특성 등을 고려해 지원기간 결정. 최소 5년, 예상 사용기간이 5년 미만이면 그 기간 | Support-period rationale, product lifetime assumptions, user-facing end date |
| M-04 | Article 13(9) | 지원기간 중 제공된 각 보안 업데이트를 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 이용 가능하게 유지 | Update archive availability checks, retention policy, restore test |
| M-05 | Article 13(12), Article 31, Annex VII | 시장 출시 전 기술문서 작성 및 적합성 평가 수행/의뢰 | Technical file index, assessment record, DoC |
| R-01 | Article 14(1)–(2) | actively exploited vulnerability 신고: 24h early warning, 72h vulnerability notification, corrective/mitigating measure available 후 14일 내 final report | Reporting decision tree, incident tabletop, timestamped records |
| R-02 | Article 14(3)–(4) | severe incident 신고: 24h early warning, 72h incident notification, (b) 통지 후 1개월 이내 final report | Severe incident criteria, tabletop exercise, timestamped records |
| R-03 | Article 14(8) | 영향받는 사용자 및 적절한 경우 모든 사용자에게 취약점/사고 및 완화·시정 조치 정보 통지 | User notification procedure, contact coverage, message template |

## 5. 하드웨어 블록 연결

| Hardware block | 우선 연결 요구사항 | 설계 선택지 (확정 아님) | 부품별 확인 |
|---|---|---|---|
| Main MCU / boot chain | P1-02, P1-03, P1-06, P1-11 | ROM/root-of-trust, authenticated boot, image verification, version policy | Exact MCU order code, silicon revision, boot mode, memory protection |
| Internal/External Flash | P1-03, P1-06, P1-13, P2-01 | protected boot region, atomic update metadata, secure erase, SBOM/build mapping | Flash read/write protection, ECC, dual-bank/address swap availability |
| Debug/Service ports | P1-04, P1-10, P1-12 | lifecycle-dependent debug lock, authenticated service, production disable/restrict | RDP/debug auth, option bytes, recovery/return-to-service implications |
| Network PHY/fieldbus | P1-04, P1-08–P1-10, P1-11 | isolation, rate limiting, protocol parser boundary, authenticated management | Interface list, supported protocols, PHY/transceiver and isolation specs |
| Key storage / optional secure element | P1-05, P1-06, P2-07 | device identity, trust anchor, non-exportable key where justified | Exact part security features, key provisioning, anti-rollback support |
| Power/reset supervisor | P1-03, P1-08 | brownout-safe update state, reset sequencing, recovery path | reset behavior, power-fail recovery, boot-state retention |
| Manufacturing provisioning | P1-04, P1-06, P2-07 | authenticated provisioning station, unique device identity, key ceremony | SFI/secure provisioning availability for selected MCU |

## 6. 검증 게이트 및 미확인 입력

### 제품 정보가 없어서 아직 확정할 수 없는 항목
- 제품 SKU/모델, EU 공급 방식, intended purpose
- 제품/옵션 모듈/툴/클라우드 경계와 직접·간접 연결
- 정확한 ST MCU 주문 코드, silicon revision, Flash/보안 옵션
- fieldbus 종류, 서비스 포트, debug interface, update channel
- 기존 기능안전 경계 및 업데이트 시 안전상태 요구
- 제품 위험평가로 정해질 시험 부하/성능 한계/합격 기준

### VERIFIED 승격 조건
각 row는 다음이 모두 채워지기 전까지 UNVERIFIED로 유지한다.
1. 법령 원문·버전·정확한 위치
2. 별도 원문 재검증 및 반증 확인
3. 제품 적용성 또는 비적용 근거
4. 설계 결정/구현 문서
5. 시험 방법과 승인된 합격 기준
6. 객관적 시험 증거 및 결과

## 7. 다음 작업

1. 제품 경계 템플릿의 BD-01–BD-15 입력 확보.
2. 실제 ST MCU 주문 코드와 실리콘 리비전을 확보하고 제조사 문서의 부품별 지원 표 작성.
3. 위 매트릭스에서 P0 항목(secure default, access control, update, integrity, availability, support/vulnerability process)부터 회로·펌웨어 블록에 배정.
4. 제품 성능/위험평가 기반으로 시험 한계와 합격 기준을 승인.
5. 매트릭스 row ID를 Master Report의 각 장과 시험 증거 저장 경로에 연결.

