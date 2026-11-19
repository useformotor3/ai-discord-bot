# CRA 제품 경계 및 서보 드라이브 증거 수집 기준서

- 문서 상태: **작성용 템플릿 — 제품별 사실관계 미입력**
- 기준일: 2026-11-17
- 적용 목적: CRA(Regulation (EU) 2024/2847) 관점에서 서보 드라이브 제품 경계, 의도된 목적, 디지털 요소, 원격 데이터 처리, 구성품 및 보안 증거를 확정하기 위한 입력 기준
- 관련 기준 문서:
  - [통합 CRA 보고서](CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)
  - [요구사항 추적표](CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv)
  - [인터페이스 적용성 매트릭스](CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)
  - [보안 통제·시험 매트릭스](CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)
  - [Guidance claim register](CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv)
  - [M/606 Annex I 41-item 관련성 매핑](CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv)

> **중요:** 이 문서는 제품별 사실을 입력하기 위한 템플릿이며, 특정 서보 드라이브의 CRA 적용성·제품 분류·적합성을 판정한 문서가 아니다. 확인되지 않은 기능이나 공급자 정보를 추정해서 채우지 않는다.

---

## 1. 제품 식별 및 시장 공급 정보

| 입력 항목 | 제품별 입력 | 확인할 증거 |
|---|---|---|
| 제조자 법인명 | 미입력 | 법인/제품 공식 문서 |
| 제품 브랜드·제품군 | 미입력 | 공식 카탈로그 |
| 정확한 모델명·주문 코드 | 미입력 | 명판, 데이터시트 |
| 하드웨어 리비전 | 미입력 | BOM, 명판, 설계 릴리스 |
| 펌웨어/소프트웨어 버전 | 미입력 | 릴리스 노트, 버전 화면 |
| EU 시장 출시 예정/최초 공급일 | 미입력 | 공급·출시 계획 |
| EU 내 제조자/수입자/공인대리인 역할 | 미입력 | 계약·공급망 문서 |
| 제품의 intended purpose | 미입력 | 사용설명서, 카탈로그, 마케팅 자료 |
| 합리적으로 예견 가능한 오용 | 미입력 | 위험성 평가, 사용자 지침 |
| 제품 변형·옵션·지역별 차이 | 미입력 | 제품군 구성표 |

**판정 원칙:** 모델명이나 판매 페이지의 마케팅 표현만으로 제품 범위와 intended purpose를 확정하지 않는다. 사용설명서, 데이터시트, 설치 가이드, 실제 기능을 서로 대조한다.

## 2. 제품 경계(Product Boundary)

각 구성요소가 제품에 포함되는지, 별도 제품인지, 외부 서비스인지 구분한다.

| 구성요소 | 포함 여부 | 제조자/공급자 | 제품 경계 근거 | 버전/식별자 |
|---|---|---|---|---|
| 서보 드라이브 본체 | 미확인 | 미입력 | 미입력 | 미입력 |
| 제어 보드/전력 보드 | 미확인 | 미입력 | 미입력 | 미입력 |
| 부트로더/부팅 체인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 펌웨어/실시간 OS | 미확인 | 미입력 | 미입력 | 미입력 |
| 통신 스택/프로토콜 라이브러리 | 미확인 | 미입력 | 미입력 | 미입력 |
| PC 설정·시운전 도구 | 미확인 | 미입력 | 미입력 | 미입력 |
| 모바일 앱 | 미확인 | 미입력 | 미입력 | 미입력 |
| 게이트웨이/통신 모듈 | 미확인 | 미입력 | 미입력 | 미입력 |
| 클라우드·원격 모니터링 서비스 | 미확인 | 미입력 | 미입력 | 미입력 |
| 외부 업데이트/라이선스 서버 | 미확인 | 미입력 | 미입력 | 미입력 |
| 선택형 보안 모듈/secure element | 미확인 | 미입력 | 미입력 | 미입력 |

별도 제품·구성품·외부 서비스 여부를 구분하고, 제품에 통합된 기능이라는 이유만으로 별도 vertical product category로 자동 분류하지 않는다.

## 3. 네트워크 인터페이스 및 통신

각 인터페이스마다 물리 매체, 프로토콜, 방향, 노출 서비스, 인증 및 업데이트 경로를 기록한다.

| 인터페이스 | 탑재 여부 | 프로토콜/표준 | 물리·무선 매체 | Inbound/Outbound | 서비스/포트 | 인증·암호화 | 외부 연결 대상 |
|---|---|---|---|---|---|---|---|
| Ethernet | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| EtherCAT | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| PROFINET | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| Modbus TCP/RTU | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| CAN/CANopen | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| USB/Serial | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| Wi-Fi/Bluetooth/Cellular | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |
| 기타 | 미확인 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 | 미입력 |

필수 보충 증거:
- 네트워크 구성도 및 인터페이스 목록
- 프로토콜/서비스/포트 목록
- 원격 접속 경로 및 방화벽 정책
- 설정·시운전 도구와 드라이브 간 통신 구조
- 공장 네트워크 또는 외부 시스템과의 신뢰 경계

## 4. 데이터 처리 및 원격 데이터 처리(RDPS)

제품·앱·클라우드·서비스 도구별 데이터 흐름을 기록한다.

| 데이터 종류 | 생성/수집 위치 | 처리 위치 | 원격 전송 여부 | 목적 | 보존기간 | 삭제/내보내기 방법 |
|---|---|---|---|---|---|---|
| 모터/제어 파라미터 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 운전·진단 데이터 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 사용자/계정 정보 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 로그/이벤트 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 펌웨어/업데이트 정보 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |
| 기타 | 미확인 | 미확인 | 미확인 | 미입력 | 미입력 | 미입력 |

RDPS 여부는 다음을 모두 증거로 확인한 후 판단한다.

1. 소프트웨어 또는 솔루션이 제품 외부에서 데이터를 원격 처리하는가?
2. 그 원격 처리가 제품의 기능을 위해 필요한가?
3. 해당 솔루션의 개발·제공 책임이 제조자에게 있는가?
4. 원격 처리 솔루션이 없으면 제품의 기능이 수행되지 않는가?

단순 원격 모니터링, 원격 지원, 데이터 백업 또는 선택적 부가 서비스라는 이유만으로 RDPS라고 단정하지 않는다. 반대로 제조자가 제공하는 원격 처리 기능이 핵심 제품 기능에 필수라면 관련 계약·아키텍처·기능 의존성을 확인한다. Guidance claim G-010~G-012에 연결한다.

## 5. 보안 기능 및 제품 설정

| 항목 | 존재 여부 | 기본값/설정 | 제품 증거 | 검증 방법 |
|---|---|---|---|---|
| 사용자 계정/역할/권한 | 미확인 | 미입력 | 미입력 | 미입력 |
| 기본 비밀번호/초기 인증 | 미확인 | 미입력 | 미입력 | 미입력 |
| MFA/서비스 접근 통제 | 미확인 | 미입력 | 미입력 | 미입력 |
| Secure Boot/부트 체인 검증 | 미확인 | 미입력 | 미입력 | 미입력 |
| 서명된 펌웨어/보안 업데이트 | 미확인 | 미입력 | 미입력 | 미입력 |
| 암호화/키 관리 | 미확인 | 미입력 | 미입력 | 미입력 |
| 보안 로그/모니터링 | 미확인 | 미입력 | 미입력 | 미입력 |
| 방화벽/IDS/IPS | 미확인 | 미입력 | 미입력 | 미입력 |
| 취약 서비스 비활성화 | 미확인 | 미입력 | 미입력 | 미입력 |
| 데이터 초기화/삭제 | 미확인 | 미입력 | 미입력 | 미입력 |
| 복구/롤백/안전한 기본 상태 | 미확인 | 미입력 | 미입력 | 미입력 |

## 6. 하드웨어·소프트웨어 구성품 및 공급망

| 구성품 | 제조사/정확한 부품번호 | 보안 기능 | 펌웨어/버전 | 공급자 취약점 지원 | 증거 |
|---|---|---|---|---|---|
| CPU/MCU | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |
| ASIC/FPGA | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |
| Secure Element/TPM/보안 IC | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |
| OS/RTOS | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |
| 통신 스택 | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |
| 오픈소스/외부 라이브러리 | 미입력 | 미확인 | 미입력 | 미확인 | 미입력 |

필수 증거:
- SBOM(가능하면 기계 판독형)
- BOM 및 정확한 component part number
- 공급자 보안 공지·지원 기간·취약점 대응 정책
- 통합 버전 및 패치 이력
- 구성품의 실제 보안 기능을 뒷받침하는 데이터시트/인증/시험 자료

M/606 item 28–30, 37–39, 41은 실제 부품이 확인될 때 component due diligence 후보로 연결한다. 해당 부품이 들어 있다는 사실만으로 완제품 서보 드라이브를 해당 vertical product category로 분류하지 않는다.

## 7. 취약점 관리 및 지원 기간

| 항목 | 제품별 사실 | 필요한 증거 |
|---|---|---|
| 보안 연락처/취약점 신고 경로 | 미입력 | PSIRT/CVD 정책 |
| 취약점 접수·분류·우선순위 | 미입력 | 절차서/티켓 샘플 |
| CVE 및 외부 취약점 모니터링 | 미입력 | 모니터링 정책 |
| 보안 업데이트 주기·배포 방식 | 미입력 | 업데이트 정책/릴리스 |
| 업데이트 진위·무결성 검증 | 미입력 | 서명/검증 설계 |
| 지원 기간 시작·종료 기준 | 미입력 | 지원 정책/제품 문서 |
| 제품 단종·지원 종료 통지 | 미입력 | EOL 정책 |
| 공급망 취약점 대응 | 미입력 | 공급자 계약/프로세스 |

## 8. 안전 기능 및 규제 중첩 검토

CRA 사이버보안 요구와 기계·전기 안전 요구를 혼합하지 않는다. 제품에 실제로 포함된 안전 기능과 인증 범위를 별도로 기록한다.

- 안전 기능(예: STO, SS1 등): 미확인
- 적용 안전 표준 및 판본: 미입력
- 안전 인증서/시험 보고서: 미입력
- CRA와 Machinery Regulation의 적용 관계: 제품 구조·시장 공급 시점·기능을 근거로 별도 분석
- 안전 기능에 영향을 주는 사이버 공격 경로: 미입력

## 9. 제품별 증거 제출 목록

| Evidence ID | 자료 | 필수성 | 현재 상태 | 검토 기준 |
|---|---|---|---|---|
| E-001 | 제품 데이터시트/카탈로그 | 필수 | 미제공 | 정확한 모델·의도된 목적 |
| E-002 | 사용설명서/설치 가이드 | 필수 | 미제공 | 사용 조건·인터페이스·사용자 의무 |
| E-003 | 제품/소프트웨어 아키텍처 | 필수 | 미제공 | 제품 경계·구성품·신뢰 경계 |
| E-004 | 네트워크/인터페이스 목록 | 필수 | 미제공 | IF-001~IF-015 연결 |
| E-005 | 데이터 흐름/RDPS 설명 | 조건부 필수 | 미제공 | G-010~G-012 판단 |
| E-006 | BOM/SBOM | 필수 | 미제공 | CRA-006/CRA-024 |
| E-007 | 위협 모델/위험성 평가 | 필수 | 미제공 | CRA-004/SEC-001 |
| E-008 | 계정·권한·인증 설계 | 해당 시 필수 | 미제공 | SEC-005 |
| E-009 | Secure Boot/업데이트 설계 | 해당 시 필수 | 미제공 | SEC-004/SEC-007/SEC-021/SEC-022 |
| E-010 | 취약점 관리/CVD 정책 | 필수 | 미제공 | CRA-006~CRA-015/SEC-015~SEC-020 |
| E-011 | 지원 기간/EOL 정책 | 필수 | 미제공 | CRA-014/CRA-015 |
| E-012 | 보안 시험/침투 시험 보고서 | 해당 시 필수 | 미제공 | SEC test matrix |
| E-013 | 공급자 보안 자료 | 구성품별 필수 | 미제공 | CRA-024/M/606 component candidates |
| E-014 | 제품 릴리스·패치 이력 | 필수 | 미제공 | vulnerability handling/update evidence |
| E-015 | 외부 서비스/클라우드 계약·설계 | 해당 시 필수 | 미제공 | product boundary/RDPS |

## 10. 분류·판정 게이트

다음 질문은 근거가 확보될 때까지 미확인으로 유지한다.

- [ ] CRA상 제품 with digital elements 범위에 해당하는가?
- [ ] 제품 또는 구성요소가 CRA 적용 제외 범주에 해당하는가?
- [ ] 제조자·수입자·유통업자 등 경제운영자 역할은 무엇인가?
- [ ] 제품 자체의 intended purpose와 core functionality는 무엇인가?
- [ ] Annex III/IV 중요·중요 핵심 제품 범주에 실제로 해당하는가?
- [ ] 원격 데이터 처리 솔루션이 제품 기능에 필수인가?
- [ ] M/606 vertical product type은 제품 자체의 intended purpose에 해당하는가, 단지 내장 기능/부품인가?
- [ ] M/606 표준이 실제 OJ에 harmonised standard로 인용됐는가?
- [ ] Machinery Regulation 등 다른 EU 법령과 어떤 관계인가?

**판정 규칙:** 각 질문은 Yes / No / Conditional / Unknown 중 하나로 기록하고, 답변마다 제품 증거 ID와 법적 근거를 연결한다. 증거가 없으면 Unknown이며 No로 간주하지 않는다.

## 11. 증거 품질 및 승인 기준

모든 제품 증거는 아래 메타데이터를 함께 보관한다.

- 원본 파일명/문서 ID
- 제조자·공급자 및 출처 URL
- 문서 버전/발행일/수집일
- SHA-256(원본 파일 bytes)
- 해당 페이지·절·표·요구사항 ID
- 추출 내용과 원문 이미지 대조 여부
- 검토자·검토일·결론·미해결 사항

증거 상태는 not_provided, received, source_verified, content_reviewed, cross_checked, accepted, rejected, not_applicable_with_rationale 중 하나로 관리한다. accepted 또는 not_applicable_with_rationale에는 검토 근거를 반드시 남긴다.

---

## 12. 현재 미확인 사항 및 다음 입력

이 저장소에는 일반 CRA Guidance·M/606 근거와 서보 드라이브용 일반 통제 매트릭스가 구축되어 있다. 그러나 실제 제조사·모델·펌웨어·인터페이스·클라우드 기능·BOM/SBOM이 입력되지 않았으므로 제품별 적용성 및 최종 분류는 아직 판정하지 않았다.

가장 먼저 확보할 자료는 **정확한 제품 모델의 데이터시트와 사용설명서**다. 이 두 자료를 기준으로 제품 경계를 확정한 뒤, 네트워크/소프트웨어 구성과 SBOM, 취약점·지원 정책 순으로 증거를 연결한다.


## 13. 2026-11-18 법령 감사 반영 추가 확인사항

### 13.1 제품 범위/연결성 게이트
- CRA Article 2(1): intended purpose 또는 reasonably foreseeable use에 직접/간접 logical/physical data connection이 포함되는지 확인.
- Article 3(1): PDE 정의, Article 3(8)–(10): physical/logical/indirect connection 정의, Article 3(22): 상업활동상 making available on the market 정의는 서로 다른 게이트로 기록.
- Commission Guidance §2.5는 디지털 정보가 정의된 방식으로 인코딩되고 수신 측에서 데이터로 해독되는지를 설명하는 비구속적 해석 보조. 단순 전원·단순 switching trigger만으로 데이터 연결을 자동 판정하지 않는다.
- 제품 전체에 다른 디지털 인터페이스가 존재하면 단순 아날로그/하드와이어 신호가 있다는 이유로 제품 전체 CRA 범위를 부정하지 않는다.

### 13.2 원격 데이터 처리 솔루션(RDPS)
아래 세 요건을 누적 확인한다.
1. 제품 외부에서 원격 데이터 처리가 실제 수행되는가?
2. 해당 원격처리가 제품 기능 중 하나의 수행에 필요한가(없으면 그 기능 수행이 불가능한가)?
3. 관련 소프트웨어가 제조자에 의해 개발되었거나 제조자 책임하에 개발되었는가?

단순 독립 SaaS, 선택형 원격 모니터링 또는 외부 IaaS만으로 RDPS를 자동 판정하지 않는다. 서비스 계약, 기능 의존성, 장애 시 제품 기능 영향, 제조자 책임 및 데이터 흐름을 함께 제출한다. 법적 정의는 Article 3(2), Recitals 11–12이며 Article 13(2)는 일반 위험평가 조항이다.

### 13.3 Annex III/IV 분류 및 평가 경로
- Important/Critical 여부는 제품명·산업용이라는 수식어·내장 부품만으로 결정하지 않는다. Annex III/IV의 category core functionality가 제품 자체의 intended purpose/function에 해당하는지 확인한다.
- Important 제품이 다른 호스트 제품에 통합되었다는 사실만으로 호스트 제품에 분류가 자동 전이되지 않는다.
- Article 32(1) 일반 평가 경로, (2) Class I 조건부 제3자 평가, (3) Class II 경로, (4) Critical 제품 경로를 구분한다. Critical 제품은 Article 8(1) delegated act 및 적용 가능한 scheme 가용성, Article 32(4) 경로를 함께 확인한다.
- 제품별 core functionality를 입증할 기능 사양, block diagram, firmware feature list, sales/marketing claims, installation/use manual을 제출한다.

### 13.4 기계류 규정과 사이버보안 중복
- Machinery Regulation (EU) 2023/1230 Annex III §1.1.9(Protection against corruption), §1.2.1(Safety and reliability of control systems)와 CRA Annex I 요구를 위험별로 교차 매핑한다.
- Machinery Regulation Article 9(9)의 cybersecurity scheme 인증 기반 적합성 추정은 해당 인증이 두 Annex III 요구를 실제로 커버하는 범위에 한정된다.
- CRA Article 2(5)는 다른 EU 법령이 동일 사이버 위험을 다루는 경우의 조건부 제한/제외 가능성을 Commission delegated act로 구체화하는 구조다. Machinery Regulation 적용만으로 CRA 전체가 자동 면제되지 않는다.
- CRA Article 69(1)은 기존 타 EU 법령상 EU type-examination certificates/approval decisions의 유효성 전환 조항이며 일반적인 sectoral overlap 조항이 아니다.

### 13.5 적용일 및 기존 제품 분기
- Article 71(2): CRA 일반 적용일 2027-12-11; Article 14 신고 의무는 2026-09-11; Chapter IV(Articles 35–51)는 2026-06-11.
- Article 69(2): 2027-12-11 전에 시장 출시된 제품은 해당 날짜 이후 substantial modification이 있는 경우 CRA 요구사항 적용 여부를 판단.
- Article 69(3): Article 14 신고 의무는 CRA 범위 내에서 2027-12-11 이전 시장 출시 제품에도 적용.
- Regulation (EU) 2025/327 Article 104는 EHR systems에 대한 CRA 특칙이므로 일반 서보 드라이브에 확대 적용하지 않는다.

### 13.6 신고 시한 시나리오
| 트리거 | 초기 경보 | 후속 통지 | 최종 보고서 기산점 |
|---|---:|---:|---|
| actively exploited vulnerability | 인지 후 24시간 | 인지 후 72시간 vulnerability notification | corrective/mitigating measure available 후 14일 |
| severe incident affecting product security | 인지 후 24시간 | 인지 후 72시간 incident notification | incident notification 제출 후 1개월 |

신고는 single reporting platform을 통해 CSIRT designated as coordinator 및 ENISA에 동시에 제출한다. Article 14(7)의 EU main establishment 기준과 EU 주된 사업장이 없는 경우의 fallback 순서를 사고대응 절차에 반영한다. Article 14(8) 영향 사용자 통지는 감독기관 신고와 별도 의무다.

## 14. 제품별 증거 제출 우선순위 (최소 시작 세트)

스마트폰으로 자료를 전달할 때는 아래 순서로 파일/링크를 제공한다. 제품별 증거를 받기 전에는 모델별 판단을 확정하지 않는다.

| 우선순위 | 자료 | 이 자료로 확인할 핵심 | 필수 메타데이터 |
|---|---|---|---|
| P0 | 정확한 모델 데이터시트/카탈로그 | 모델/변형, intended purpose, core functionality, 옵션 | 제조자, 모델/주문코드, 발행일/버전, 원본 URL |
| P0 | 사용설명서/설치·시운전 매뉴얼 | 합리적으로 예견 가능한 사용, 인터페이스, 설치 환경, 서비스 접근 | 문서 버전, 해당 페이지, 시장/언어 |
| P1 | 제품/통신 block diagram 및 인터페이스 사양 | 물리·논리 연결, 프로토콜, 외부 데이터 흐름, trust boundary | HW revision, protocol/version, option card |
| P1 | 펌웨어/소프트웨어 구성표 및 SBOM | OS/RTOS, bootloader, libraries, dependencies, remote services | SW/FW version, SPDX/CycloneDX format, build/release ID |
| P1 | EU 공급망/상표/시장 출시 정보 | 제조자·수입자·유통자·authorized representative, launch date | 법인명/국가, contract/mandate, first placement date |
| P2 | 보안 기능·취약점 정책·지원기간 문서 | 인증, 업데이트, CVD, support period, EOL | 정책 버전, 담당 연락처, support end date |
| P2 | Machinery/기타 EU 인증서 및 위험성 평가 | sectoral overlap, certificate scope, safety-related cyber risks | 발행기관, certificate number, scope, validity, applicable version |

## 15. 제품 판정 출력 형식

각 모델/variant에 대해 다음 필드를 분리해 기록한다.
- CRA scope: Yes / No / Conditional / Unknown + evidence IDs
- PDE/data connection: Yes / No / Conditional / Unknown + interface evidence
- RDPS: Yes / No / Conditional / Unknown + three cumulative criteria
- Annex III Important / Annex IV Critical: category, core functionality match, counter-evidence
- Article 32 conformity assessment route: conditional route and reason; do not infer from class before classification
- Machinery/sectoral overlap: exact risk covered, certificate scope, delegated act status, residual CRA requirements
- Economic operator roles and Article 14 reporting route
- Open issues, missing evidence, reviewer and date

'No evidence'는 'No'가 아니며, 제품별 판단을 내릴 수 없는 경우 Unknown을 유지한다.


## 16. 제품별 증거 register — 2026-11-19

기존 E-001~E-015 제출 목록을 기계판독형 register로 관리한다: [제품 증거 register 템플릿](CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv).

- 각 E-ID는 관련 EVD-01~16에 연결된다. 제품 variant가 여러 개인 경우 variant별 행/복사본으로 분리하고, 모델 간 증거를 혼용하지 않는다.
- 원본 파일명, 출처 URL(해당 시), 발행자, 문서 버전·발행일, 수집일, SHA-256, 페이지/절 locator, 원문 언어, 검토자·검토일, 교차검증 참조 및 판정 근거를 기록한다.
- 상태는 not_provided, received, source_verified, content_reviewed, cross_checked, accepted, rejected, not_applicable_with_rationale 중 하나다.
- accepted는 파일·출처 provenance·SHA-256·locator·검토자/일자·교차검증 참조·결정 근거가 모두 있어야 한다. not_applicable_with_rationale는 제품 variant, 검토자/일자, 명시적 사유가 필요하다.
- 상태 이름만 바꾸거나 교차표 링크만 존재한다고 증거를 accepted/Pass로 승격하지 않는다. 현재 모든 E-ID는 제품 자료 미제공으로 not_provided다.
- 자동 검증: cra_traceability.py; 부정 테스트는 provenance 없는 accepted, 알 수 없는 EVD 링크, 근거 없는 비적용 판정을 거부한다.
