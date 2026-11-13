# 서보 드라이브 CRA 적용·구현 방안 — 제2권

- 문서 ID: CRA-SD-IMP-001
- 버전: 1.0
- 기준일: 2026-11-13
- 상태: **일반 참조 구현 계획 / 제품별 설계 확정 아님**
- 상위 문서: [CRA 서보 드라이브 사이버보안 요구사항 조사 보고서](CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md)
- 추적성: [요구사항-HW/FW/시험/증거 매트릭스](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md)
- 아키텍처: [보안 하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md)
- 위협 모델: [위협 모델](THREAT_MODEL_SERVO_DRIVE_CRA.md)
- 시험 대장: [보안 시험·증거 대장](SECURITY_TEST_EVIDENCE_REGISTER.md)

> 본 계획은 설계 선택을 위한 기준안이다. 실제 회로도, PCB, 펌웨어, 부품값, 핀맵, 절연 등급, 타이밍, 안전기능을 확정하지 않는다. 제품 경계·SKU·MCU가 확인되기 전에는 모든 적용성은 UNVERIFIED다.

## 1. 실행 전략

**요구사항 → 제품 위험 → 설계 결정 → 인터페이스 계약 → 구현 → 시험 → 증거 → 승인** 순서를 강제한다. AI가 생성한 설계 제안은 자동으로 VERIFIED가 되지 않는다.

### 완료 게이트

- G0 제품 정의: SKU, intended purpose, EU 공급 형태, 제품 경계, 인터페이스, MCU 확정
- G1 법령 기준선: 조항/Annex/원문/예외/적용시기/책임주체 확인
- G2 위험평가: 자산·위협·영향·가능성·위험처리 승인
- G3 아키텍처: 신뢰 경계, HW/FW 인터페이스, 안전 경계, 키/업데이트 설계 승인
- G4 상세 설계: 실제 부품·회로도·펌웨어 상태기계·설정 기준선 승인
- G5 검증: 시험 환경·DUT 식별·합격 기준·원시 증거·독립 검토 완료
- G6 출시 문서: 기술문서, Annex II 사용자 정보, DoC, 지원기간, PSIRT/취약점 처리 프로세스 승인

앞 게이트의 미해결 사항은 다음 게이트의 VERIFIED 주장으로 승격하지 않는다.

## 2. P0 — 제품 경계 및 법적 적용성 확인

### 2.1 즉시 확보할 입력
1. 제조사 법인명, 브랜드, 주소, 제품명, SKU
2. EU 공급 방식과 제품의 독립 판매/기계 통합 여부
3. Intended purpose, essential functions, reasonably foreseeable misuse
4. Ethernet/fieldbus/USB/UART/Wi-Fi/Bluetooth/원격 서비스 유무
5. MCU 정확한 order code, silicon revision, HW revision
6. 펌웨어 업데이트 경로, bootloader, 복구 방법
7. 예상 사용기간, 지원기간 정책, 부품 단종/공급망 계획
8. 제품의 Annex III/Implementing Regulation 2025/2392 해당 가능성을 판단할 기능 자료

### 2.2 분류·적합성 평가
- 제품 경계 정의서를 먼저 작성한다.
- Annex III 범주와 핵심 기능을 대조한다.
- Important Product Class I/Class II 또는 critical product로 분류되는지 근거를 기록한다.
- 분류가 확정되기 전에는 conformity assessment route를 단정하지 않는다.
- 기능안전 분류와 CRA 제품 분류를 서로 대체하지 않는다.

**산출물:** Product Boundary & CRA Applicability Decision Record (PB-001). 현재 NOT_STARTED.

분류 판정의 근거표와 Article 32 절차별 조건은 [CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md)를 기준으로 작성한다. 제품에 통합된 MCU의 분류와 완제품 드라이브의 분류를 혼동하지 않는다.

## 3. P0 — Article 14 신고 대응 체계

2026-09-11부터 신고 의무가 적용 중이다. 제품이 시장에 나와 있거나 출시 준비 중이라면 제품 보안 사고 인지·분류·보고 절차를 우선 마련한다.

### 3.1 사건 분류 플로우
1. 취약점/사고 제보 또는 내부 탐지 접수
2. 제품·버전·구성요소·영향 범위 식별
3. 제품에 포함된 취약점인지, 적극 악용되는지 판단
4. 제품 보안에 영향을 미치는 심각한 사고인지 별도 판단
5. 법령상 신고 트리거 해당 여부와 인지 시각을 기록
6. 지정 CSIRT/CRA Single Reporting Platform 제출 준비
7. 조기 경고, 72시간 신고, 최종 보고 시각 추적
8. 완화·패치·사용자 통지·사후 검토

### 3.2 기한 관리

| 이벤트 | 기준 시각 | 기한 | 내부 운영 권고 |
|---|---|---|---|
| 적극 악용 취약점 인지 | T0 | T0+24h 조기 경고 | 즉시 PSIRT 책임자/법무/제품책임자 호출 |
| 적극 악용 취약점 인지 | T0 | T0+72h 신고 | 사실 미확정은 미확정으로 구분해 제출 준비 |
| 시정/완화 조치 제공 | Tfix | Tfix+14일 최종 보고 | 수정 버전·영향·완화 안내 첨부 |
| 심각한 제품 보안 사고 인지 | T0 | T0+24h 조기 경고 | 제품 영향과 사건 심각도 분리 평가 |
| 심각한 제품 보안 사고 인지 | T0 | T0+72h 신고 | 대응 타임라인 및 사용자 영향 기록 |
| 72h 신고 | T72 | T72+1개월 최종 보고 | 원인·완화·시정 조치·재발 방지 기록 |

법정 기한은 공식 CRA와 Commission 안내에 따라 관리한다. 이 표는 법률 자문을 대체하지 않으며 실제 사건 시 법무/규제 책임자 검토가 필요하다.

접수 필드, 사건 분류, 신고 판단 기록, 에스컬레이션 및 운영 역할은 [CRA Article 14 PSIRT 대응 SOP](CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md)를 실무 절차의 정본으로 사용한다. Article 14 신고 트리거와 Annex I Part II의 모든 취약점 처리 의무를 같은 것으로 취급하지 않는다.

**산출물:** PSIRT SOP, incident intake form, 24h/72h/14d/1month clock log, tabletop exercise report. 현재 NOT_STARTED.

## 4. P1 — 참조 HW/FW 아키텍처와 설계 후보

### 4.1 논리 블록
- 산업용 Ethernet/Fieldbus PHY 및 필요한 절연·보호 회로
- 통신 스택/게이트웨이 도메인
- 모션 제어 MCU 및 실시간 제어 경로
- Encoder/Resolver/Sensor front-end
- Gate driver/power stage와 별도 fault/inhibit 경계
- 내부 Flash/Data Flash 및 선택적 외부 NVM
- 선택적 Secure Element
- Power/Reset/Brownout/Clock Supervisor
- SWD/JTAG/ROM boot/생산 fixture 인터페이스
- 승인된 제조 프로비저닝 스테이션

각 블록은 제품에 실제 존재하는지 확인한다. 존재하지 않는 블록은 N/A로 처리하고 근거를 남긴다.

### 4.2 주요 인터페이스 계약

| IF ID | 경계 | 최소 설계 검토 | 검증 예 |
|---|---|---|---|
| IF-01 | 외부 PHY/Fieldbus → 통신 도메인 | 프레임 길이·상태·프로토콜 검증, rate limiting, 비정상 입력 격리 | malformed frame, fuzz, flood |
| IF-02 | 통신 도메인 → 모션 MCU | 인증·권한·명령 범위·상태 전이·bounded mailbox | replay, unauthorized command, queue saturation |
| IF-03 | MCU → Gate Driver/Power Stage | reset/fault 시 출력 억제 경로, watchdog/enable 독립성, 시스템 위험평가 | reset, brownout, watchdog, gate inhibit timing |
| IF-04 | Encoder/Sensor → MCU | 신호 plausibility, 단선/단락/범위 오류, 인터페이스 보호 | sensor fault injection |
| IF-05 | MCU ↔ NVM | 이미지/설정/로그/키 분리, 접근권한, 무결성 | corruption, rollback, unauthorized write |
| IF-06 | MCU ↔ Secure Element(선택) | 키 생성·주입·사용·폐기, 인증, bus threat | key export attempt, bus capture |
| IF-07 | SWD/JTAG/ROM Boot | 개발/생산/서비스 상태별 정책 | production debug access test |
| IF-08 | Power/Reset/Watchdog/Clock | 전압·클록 이상과 업데이트/부팅 상태 전이 | power interruption, clock fault |
| IF-09 | Factory Fixture → Device | 스테이션 인증, 장치 ID, 승인된 프로비저닝, 키 비밀 보호 | unauthorized station, duplicate identity |
| IF-10 | 원격/서비스 인터페이스(있는 경우) | 인증, 최소권한, 세션·감사, 기본 비활성/설정 근거 | unauthorized session, privilege escalation |

### 4.3 업데이트·부팅 신뢰 체인

참조 흐름:
1. 승인된 빌드 시스템에서 펌웨어 이미지 생성
2. 이미지에 제품 ID, HW 호환성, 버전, digest, 서명 메타데이터 부여
3. 승인된 키 관리 절차로 서명
4. 배포 전 패키지 무결성·서명 검증
5. 장치 부트로더가 서명·제품 대상·버전 정책 검증
6. 설치 중 전원 차단/통신 오류 시 복구 가능한 상태 유지
7. 부팅 후 이미지 상태·버전·결과 기록
8. 취약점 수정 공개·사용자 통지 및 보안 업데이트 저장소 유지

이중 뱅크, rollback 방지, secure boot, 서명 업데이트는 설계 후보다. 실제 MCU의 지원 기능·메모리 크기·실시간성·복구 동작을 확인한 뒤 선택한다. 'Secure Boot가 있다'는 부품 기능만으로 완제품 신뢰 체인이 성립하지 않는다.

## 5. P1 — 접근통제·데이터·인터페이스

법적 요구와 권장 구현 수단의 구분, 접근통제 설계 검토 및 시험 증거는 [CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md)를 참조한다. RBAC, least privilege, MFA, 고유 장치별 자격증명 등은 위험기반 구현 후보이며 CRA가 모든 제품에 동일한 기술을 직접 명령한다고 쓰지 않는다.

- 사용자/서비스/생산 역할을 구분하고 최소권한을 적용한다.
- 기본 비밀번호 강제, 계정 생성·변경·복구 방식은 위협모델과 사용자 환경을 반영해 설계한다. CRA가 모든 제품에 특정 로그인 방식을 명시한다고 주장하지 않는다.
- SWD/JTAG/ROM boot는 생산 상태에서의 정책을 정하고 설정값과 실제 접근 시험을 증거로 보존한다.
- Ethernet/Fieldbus 관리 기능, 웹 UI, FTP/SSH/Telnet 등은 실제 존재 여부를 인벤토리화하고 불필요 기능을 제거하거나 보호한다. 모든 포트를 무조건 닫는다는 법적 규칙으로 오해하지 않는다.
- 설정·모션 명령·펌웨어·키·사용자 데이터·로그의 기밀성/무결성/가용성 요구를 자산별로 구분한다.
- 로그는 사고 분석에 필요한 이벤트를 정의하고 데이터 최소화·보존·접근·opt-out 요건을 함께 검토한다.
- 사용자 데이터와 자격증명은 반품·수리·재판매·폐기 시 안전하게 제거할 수 있어야 한다.

## 6. P1 — 취약점·SBOM·지원기간·사용자 정보

### 6.1 취약점 처리 운영
- 제품 및 구성요소 버전 인벤토리 유지
- SBOM을 빌드/릴리스 버전과 연결
- CVE 및 공급업체 보안 권고 모니터링
- 영향도·악용 가능성·제품 노출·완화 가능성 triage
- 내부/외부 신고를 CVD 절차로 접수
- 구성요소 취약점을 식별하면 Article 13(6)에 따라 해당 구성요소 제조/유지 주체에 보고하고, 제품 측 시정·완화 조치를 병행. 공급자→제조사 자동 통지를 법령상 일반 의무로 전제하지 않음
- 패치 개발·검토·시험·배포·공개
- Article 14(8) 해당 사건은 영향 사용자 통지 여부·범위·시각을 판단하고, 구조화된 machine-readable 형식은 where appropriate 조건에 따라 선택
- 각 릴리스와 보안 공지의 원본/해시/승인 기록 보존

### 6.2 지원기간·업데이트 보존
- Article 13(8): 제품 예상 사용기간 등 고려; 일반 최소 5년, 예상 사용기간이 5년 미만이면 예상 사용기간에 대응.
- Article 13(9): 지원기간 중 사용자에게 제공한 각 보안 업데이트를 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 제공.
- Annex I Part II(8): 보안 업데이트를 지체 없이 제공하고 무상 제공(법령상 맞춤형 제품/사업 사용자 합의 예외 검토).
- 세 요구를 하나의 '5년/10년 지원' 문구로 합치지 않는다.

### 6.3 사용자 문서
Annex II의 1~9번을 제품 사용자 설명서/온라인 문서에 매핑한다. 기술문서(Annex VII)와 사용자 제공 정보(Annex II)를 분리 관리한다. SBOM 접근 위치는 제공하기로 결정한 경우에만 기재한다.

## 7. P2 — 검증·시험 계획

현재 기존 시험 대장에 45개 시험 후보가 있으나 실제 제품 시험은 수행되지 않았다. 우선 아래 범주별로 DUT 식별과 합격 기준을 확정한다.

| 시험군 | 대표 시험 | 합격 기준 확정 주체 | 상태 |
|---|---|---|---|
| Boot/Update | unsigned/tampered/wrong-product/rollback image | 제품 보안 설계·위험평가 | NOT_RUN |
| Access Control | unauthenticated/unauthorized/debug access | 보안 요구사항 승인자 | NOT_RUN |
| Protocol | malformed input/fuzz/replay/flood | 통신·시스템 설계 | NOT_RUN |
| Data Integrity | parameter corruption/NVM fault | 시스템·펌웨어 설계 | NOT_RUN |
| Availability | DoS/recovery/watchdog/reset | 시스템 위험평가·제어 설계 | NOT_RUN |
| Provisioning | unauthorized station/key misuse/duplicate ID | 제조·보안 책임자 | NOT_RUN |
| Vulnerability Process | intake/triage/patch/disclosure exercise | PSIRT 책임자 | NOT_RUN |
| User Information | Annex II completeness/usability | 제품·품질·규제 담당 | NOT_RUN |

실행 전 필수 메타데이터: DUT SKU, HW revision, MCU order code/silicon revision, FW hash, bootloader hash, 구성, 시험 환경, 도구 버전, 절차, 예상/관찰 결과, 원시 증거 hash, 판정자.

## 8. 위험 및 의존성

| 위험 ID | 위험 | 결과 | 완화 |
|---|---|---|---|
| R-01 | 제품 SKU/경계 미확정 | 잘못된 CRA 범위·등급 | G0에서 사실/증거 승인 |
| R-02 | 법령 조항을 AI가 잘못 인용 | 잘못된 설계 요구·문서 | 원문 위치·인용 검증기·독립 리뷰 |
| R-03 | MCU 기능을 다른 부품에 전이 | 구현 불가/보안 공백 | 정확한 order code 및 RM/Errata 대조 |
| R-04 | CRA와 기능안전 요구 혼합 | 잘못된 안전 주장 | 별도 추적성·안전 분석 |
| R-05 | 시험 전 합격 기준 임의 설정 | 시험 결과의 의미 상실 | 제품 위험/요구에서 수치 승인 |
| R-06 | 지원기간·패치 보존 혼동 | 규제 의무 누락 | Article 13(8)/(9), Annex I II(8) 분리 |
| R-07 | 운영 AI 보고서 무검증 축적 | 오정보가 근거처럼 재사용 | draft/verified 분리, 자동 승격 금지 |

## 9. 완료 조건 및 단계별 산출물

| 단계 | 산출물 | 완료 정의 |
|---|---|---|
| 0 | Product Boundary & Applicability Record | 제품 사실과 CRA 범위/분류 근거 승인 |
| 1 | Legal Requirement Baseline | 각 조항 원문·위치·해석·적용시기·예외 검증 |
| 2 | Product Cybersecurity Risk Assessment | 제품 사실 기반 자산·위협·위험처리 승인 |
| 3 | HW/FW Security Architecture | IF 계약·키·업데이트·접근통제·안전 경계 승인 |
| 4 | Detailed Design Package | BOM·회로도·펌웨어 설계·구성 기준선 |
| 5 | Verification & Evidence Package | DUT별 시험 실행, 결과, 원시 증거, 독립 검토 |
| 6 | Technical Documentation & User Information | Annex VII/II 및 DoC·지원기간·PSIRT 문서 승인 |
| 7 | Release Readiness Review | 미해결 위험 승인·릴리스 결정·추적성 폐쇄 |

## 10. 다음 실행 순서

1. 사용자/제품 자료에서 SKU·MCU·인터페이스·업데이트·지원기간 사실 확보.
2. 기존 추적성 매트릭스를 본 보고서의 법령 ID와 통합하고 중복/충돌 제거.
3. Article 14 tabletop 절차 및 PSIRT 연락 체계 초안 작성.
4. 실제 MCU 부품번호를 기준으로 ST/TI 기능 비교와 제조사 문서 원문 위치 검증.
5. IF-01~IF-10을 실제 회로도·펌웨어 아키텍처에 매핑.
6. TST/EV 시험 대장을 제품별로 갱신하고 승인된 시험부터 실행.
7. 기술문서/사용자 정보/최종 보고서의 버전 및 출처 추적성을 자동 검사.

---
문서의 '설계 후보'는 제품 설계 승인 전까지 제안 상태로 유지한다.


## 문서 간 연결 및 정본 참조

- 제품 경계·분류·접근통제의 법적 요구/구현 구분: [제품 분류·접근통제 매트릭스](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md).
- 신고 대응 역할·접수·기한·훈련: [Article 14 PSIRT SOP](CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md).
- 요구사항 ID에서 위협·HW/FW·시험·증거까지의 연결: [통합 추적성 매트릭스](CRA_INTEGRATED_TRACEABILITY_MATRIX.md).
- 설계 블록·신뢰 경계·인터페이스 계약: [보안 HW 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md).
- 전체 문서 지도: [CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md](CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md).

이 제2권은 실행 순서와 설계/시험 계획의 정본이다. 법령 해석의 세부 근거는 제1권 및 법령 기준선, 실제 운영 절차는 PSIRT SOP, 추적성 ID는 통합 매트릭스를 기준으로 한다.


### #48–#52 감사 정정 반영 — 공급망 취약점 및 사용자 통지

- Article 13(6)의 구성요소 취약점 신고 방향은 제품 제조사에서 해당 구성요소 제조사/유지관리 주체로 향한다. 공급자가 항상 상위 제조사에 자동 통지해야 한다는 일반 CRA 의무로 표현하지 않는다.
- Article 14(8)의 사용자 통지는 적극 악용 취약점 또는 제품 보안에 영향을 미치는 심각한 사고에 대한 통지다. 구조화된 기계 판독 가능 형식은 “where appropriate(적절한 경우)” 조건이며 모든 취약점 공지에 일률 적용하지 않는다.
- Annex I Part II(4) 수정 취약점 공개, (5) CVD 정책, (6) 취약점 신고 연락처, (7) 안전한 업데이트 배포, (8) 원칙적 무상 보안 업데이트를 서로 구분한다.
- 지원기간은 Article 13(8), 지원기간 중 제공된 각 보안 업데이트의 보존·가용성은 Article 13(9)로 관리한다.
- 상세 원문·SHA·반증: [#48–#52 감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md).


## #13–#42 감사 정정의 구현·매뉴얼 반영

- 법령 조항의 정본은 [CRA 공식 법령 기준선](CRA_VERIFIED_BASELINE_2026-11-12.md)을 따른다.
- Annex I Part I(2)(b)–(j)의 요구 결과와 위험기반 구현 선택을 구분한다. 특정 비밀번호 정책, 포트 비활성화, JTAG 잠금, TPM/SE, Secure Boot, 서명 방식, A/B bank, rollback, 무중단 업데이트를 보편적 법정 의무로 전제하지 않는다.
- Annex I Part II(1)–(8)의 취약점 처리 항목은 각각 분리해 추적한다. 사용자 설명서는 Article 13(18)/Annex II, 기술문서는 Article 31/Annex VII를 기준으로 한다.
- 안전한 폐기 안내(Annex II point 8(d))와 제품 내부의 데이터 삭제 기능 구현을 구분한다.
- Article 14 신고는 두 신고 트랙과 최종 보고 기한을 구분하고, CVD/일반 취약점 처리와 혼합하지 않는다.
