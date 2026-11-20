# CRA 서보 드라이브 통합 규제·기술 준수 보고서

- 문서 버전: v0.6 (ETSI 8개 Work Item 및 CLC/TC 65X OT profile 상태 정합성 / C(2026)7861 Article 2 보강) (CRA 핵심 규제·이행, CEN/ETSI 및 EU 표준화 법체계 최신정보 갱신 / 제품별 적용성 확인 전)
- 기준일: 2026-11-20
- 프로젝트 범위: EU Cyber Resilience Act(CRA) 대응만
- 기준 제품군: 산업용 서보 드라이브 및 필수 펌웨어·설정/진단 소프트웨어
- 법적 기준 원문: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024
- 상태: 법령·공식 가이드 기준의 공통 분석. 특정 제조사·모델의 적합성 판정 또는 인증 결과가 아님.

## 1. 요약 및 현재 결론

1. CRA는 EU 시장에 공급되는 제품 중 의도된 목적 또는 합리적으로 예견 가능한 사용에 장치/네트워크와의 직접·간접 논리적/물리적 데이터 연결이 포함된 제품 디지털 요소(PDE)에 적용된다(Article 2(1), Article 3(1), (22)).
2. 전형적인 산업용 서보 드라이브가 펌웨어를 내장하고 EtherCAT, PROFINET, EtherNet/IP, Modbus, CANopen, USB 설정·진단 등 디지털 데이터 통신을 의도된 목적 또는 합리적으로 예견 가능한 사용으로 수행한다면 CRA 적용 가능성이 높다는 사전 스크리닝 가설을 세울 수 있다. 이는 제품군 일반의 가설이며 개별 모델 판정이 아니다. 제조사·정확한 모델/variant, 실제 인터페이스·프로토콜·데이터 교환, intended purpose 및 EU 시장 공급 증거를 확인하기 전에는 해당 모델의 CRA 적용 여부를 Unknown으로 유지한다.
3. 전기 신호가 존재한다는 사실만으로 CRA의 데이터 연결이 성립하지는 않는다. Commission Guidance는 단순 전원/스위칭 신호와 송신자가 디지털 정보로 인코딩하고 수신자가 이를 해독하는 데이터 통신을 구분한다. 따라서 순수 아날로그 신호 또는 데이터로 인코딩되지 않은 단순 on/off 신호만 있는 구성은 적용 범위를 별도로 판단해야 한다.
4. 현재 CRA Annex III에는 중요 제품(Important products, Class I/II), Annex IV에는 중요 핵심 제품(Critical products) 카테고리가 열거되어 있으며 일반 서보 드라이브라는 제품 카테고리는 직접 열거되어 있지 않다. 통신 포트나 일반 MCU를 포함한다는 사실만으로 Annex III Class I/II 또는 Annex IV 제품으로 자동 분류하지 않는다. 제품 전체의 핵심 기능(core functionality)과 Annex III/IV 카테고리의 기능적 일치를 평가해야 한다. 통상적인 모터 제어가 핵심 기능인 서보 드라이브는 현재 확인된 일반 제품 카테고리와 구별될 수 있다는 잠정 가설만 둘 수 있다. 이는 Annex III/IV 비해당의 확정 결론이나 default classification이 아니다. 정확한 모델의 intended purpose, core functionality, 제품 경계와 Annex III/IV 각 카테고리의 기능적 일치를 제품 증거로 검토하기 전에는 분류를 Unknown으로 유지한다.
5. 일반 제품 범주라면 Article 32(1)이 허용하는 Module A, Module B+C, Module H 또는 가능한 경우 EU 사이버보안 인증 중 적절한 경로를 선택한다. Module A는 일반 제품에서 흔히 검토되는 내부 관리 경로지만 유일한 선택지는 아니다. Annex III/IV 핵심 기능 제품은 Article 32(2)–(4)의 추가 평가 절차를 적용하므로 분류를 먼저 확정해야 한다.
6. Article 14 신고 의무는 2026-09-11부터 이미 적용 중이다. CRA 적용일(2027-12-11) 전 시장에 출시된 제품도 신고 대상이 될 수 있으며, 지원기간이 끝난 제품에도 신고 의무는 계속된다. 기존 설치 제품을 보유한 제조사는 취약점·심각한 사고 접수, triage, 신고 책임자 및 24/72시간 대응 절차를 지금 운영해야 한다.
7. 지원기간은 일률적인 5년이 아니다. 제품의 예상 사용기간, 사용자 기대, 제품의 성격 및 관련 EU 법령을 반영해야 하며, 최소 5년이 원칙이나 실제 예상 사용기간이 5년보다 짧으면 그 기간에 맞춘다. 산업용 제어 제품은 장기간 사용되는 경우가 많으므로, 5년을 자동 기본값으로 두지 말고 근거를 문서화해야 한다.
8. Commission Guidance(2026-07-27)는 비구속적 해석 자료지만 데이터 연결, 하드웨어·소프트웨어 결합, 복합 시스템, 실질적 변경, 지원기간, 핵심 기능, 원격 데이터 처리 및 신고 의무를 구체화한다. CRA 법령 원문과 함께 제품별 판단의 핵심 참고자료로 사용한다.
9. 표준화 요청 M/606은 2026-11-10 결정 C(2026) 7861로 수정되었다. 일부 수평 표준의 기한은 2026-11-30, 모든 수직(제품별) 표준의 기한은 2027-01-31로 연장되었다. Annex I Part I의 나머지 수평 표준 기한은 2027-10-30이다. 이는 표준화기구의 납품 일정이지 CRA 법적 의무의 적용일을 변경하지 않는다.
10. 기계류 규정(Regulation (EU) 2023/1230)은 CRA의 일반 면제 근거가 아니다. 두 법령의 요구를 제품별로 함께 검토한다. 기계류 규정에 따른 유효한 인증서/승인 결정이 특정 사이버보안 위험을 이미 다루는 경우 Article 69(1)의 한시적 효력 인정이 가능하지만, 그 인증서가 다루지 않는 추가 CRA 위험은 별도 평가·완화해야 한다.

## 2. 법령·자료의 위계와 기준일

### 2.1 구속력 있는 법적 기준
- Regulation (EU) 2024/2847 본문 및 Annex I–VIII가 핵심 법적 기준이다.
- 법령과 공식 해석자료가 충돌하면 법령 문언을 우선한다.
- 공식 조화표준의 추정 적합성(presumption of conformity)은 해당 표준의 참조가 EU Official Journal에 공표된 범위에서만 인정된다(Article 27). 표준 초안, CEN/CENELEC/ETSI 내부 승인, M/606 납품 자체를 OJ 공표와 동일시하지 않는다.

### 2.2 공식 해석·이행자료
- European Commission, Commission Guidance (C(2026) 5252, 2026-07-27 승인/게시), Official Journal Communication C/2026/6013, 2026-11-17 게재, CELEX 52026XC06013. 비구속적이며 개별 제품에 대한 사례별 판단을 대체하지 않는다. 최신 인용 및 페이지 기준은 EUR-Lex OJ C/2026/6013 PDF를 우선한다.
- European Commission CRA implementation page, CRA implementation FAQs(마지막 갱신 2026-09-04), CRA standardisation page. 진행 일정과 정책 업데이트 확인에 사용한다.
- ENISA CRA SRP FAQ(마지막 갱신 2026-10-15). 플랫폼 등록·신고 단계·기존 제품 적용 및 사용 제한을 확인한다.
- ENISA CRA Single Reporting Platform FAQ. 신고 플랫폼 운영 절차 확인에 사용한다.
- Commission Implementing Decision C(2026) 7861 final, 2026-11-10. M/606 표준화 납품 기한 개정의 공식 근거다.

### 2.3 Regulation (EU) 2025/327 개정의 범위
Regulation (EU) 2025/327 Article 104는 CRA Article 13(4), Article 31(3)을 수정하고 Article 32(5a)를 추가한다. 해당 개정은 2027-03-26부터 적용된다. 개정의 핵심은 Article 12에 해당하는 고위험 AI 제품 및 EHDS상 EHR 시스템 등에 대한 위험평가·기술문서·적합성 평가 조정이다. 일반 서보 드라이브가 고위험 AI 시스템 또는 EHR 시스템에 해당하지 않는다면 이 개정의 특례가 직접 적용된다고 가정하지 않는다. 제품에 고위험 AI 기능이 포함되는 경우 별도 법률 분석을 수행한다.

## 3. CRA 적용성 — 산업용 서보 드라이브

### 3.1 판단 순서
| 판단 항목 | 확인 질문 | 잠정 해석 |
|---|---|---|
| EU 시장 공급 | 제조사 또는 경제운영자가 EU 시장에서 상업 활동으로 공급하는가? | 유상·무상 공급 모두 가능. 공급 구조와 경제운영자 역할 확인 |
| 제품 디지털 요소 | 하드웨어/소프트웨어 제품 또는 필수 원격 데이터 처리 솔루션인가? | 내장 펌웨어가 있는 서보 드라이브는 일반적으로 PDE 검토 대상 |
| 데이터 연결 | 의도된 목적/합리적으로 예견 가능한 사용에 장치·네트워크와의 직접/간접 논리적·물리적 데이터 연결이 포함되는가? | 필드버스/이더넷/디지털 설정·진단 프로토콜은 적용 가능성을 높임 |
| 통신의 실질 | 신호가 디지털 정보로 인코딩되어 수신 측에서 해독되는가? | 단순 전원·스위칭 신호만으로는 데이터 연결이 성립하지 않을 수 있음 |
| 제품 경계 | 드라이브, 펌웨어, 필수 PC 도구, 통신 게이트웨이, 클라우드가 하나의 제품 기능을 구성하는가? | 의도된 기능에 필요한 소프트웨어/원격 처리 포함 여부 검토 |
| 시장 출시 시점 | 개별 제품/모델이 언제 처음 EU 시장에 공급되었는가? | 2027-12-11 전후 구분 및 실질적 변경 이력 필요 |

### 3.2 통신 인터페이스별 초기 분류(검증 전)
- EtherCAT, PROFINET, EtherNet/IP, Modbus TCP, OPC UA, CANopen 등 프로토콜 기반 디지털 통신: 데이터 연결이 포함될 가능성이 높다.
- USB, Ethernet 서비스 포트, 시리얼 진단 인터페이스: 실제 사용 목적·통신 프로토콜·데이터 교환 여부 확인.
- 아날로그 지령(예: ±10 V) 및 단순 디지털 입력/출력: 단순 신호인지 디지털 정보 통신인지 Commission Guidance의 기준에 따라 구분.
- 내부 MCU/FPGA/메모리 존재만으로 제품 전체의 CRA 적용 또는 Annex III Class I/II 분류가 자동 결정되지는 않는다.
- [서보 드라이브 인터페이스별 CRA 적용성 증거 매트릭스](CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)는 EtherCAT/PROFINET/CANopen/Modbus/USB/serial/아날로그/24V DI/DO/엔코더/STO/무선/PC 도구/클라우드 등 15개 항목을 구분한다. 각 항목은 제품별 실제 회로·프로토콜·사용 목적 확인 전까지 잠정이다.

### 3.3 제품 경계와 원격 데이터 처리
- 하드웨어와 제조사가 제공하는 필수 펌웨어/소프트웨어가 의도된 기능을 수행하기 위해 함께 작동하면 단일 PDE로 평가할 수 있다. 소프트웨어의 전달 채널이 별도 다운로드라는 사실만으로 제품 경계에서 제외되지 않는다.
- PC commissioning/configuration/diagnostic tool이 독립 제품으로 공급되는지, 드라이브 기능에 필수로 결합되는지 구분한다.
- 클라우드 또는 제조사 서버의 처리가 제품 기능 수행에 필수이고 제조사가 개발했거나 책임지는 경우 Remote Data Processing Solution(RDPS)로 제품 경계에 포함될 수 있다. 제3자 IaaS/SaaS 의존성도 위험평가와 기술문서에 반영한다.
- 원격 서비스가 단지 브라우저로 접근되는 독립 서비스라는 이유만으로 자동 PDE가 되는 것은 아니다. 드라이브 기능에 필수인 원격 처리인지 판단한다.

### 3.4 중요/핵심 제품 분류
- CRA Article 7 및 Annex III는 중요 제품을 열거된 제품 카테고리의 핵심 기능을 가진 PDE로 정의한다.
- Annex III Class I에는 예를 들어 네트워크 관리 시스템, 운영체제, 라우터/스위치, 보안 기능을 가진 MCU/마이크로프로세서 등이 포함된다. Class II에는 하이퍼바이저/컨테이너 런타임, 방화벽·IDS/IPS, 변조 방지 MCU/마이크로프로세서가 포함된다.
- Annex IV의 핵심 제품 범주는 보안 박스 하드웨어, 특정 스마트미터 게이트웨이/고급 보안장치, 스마트카드/보안요소 등이다.
- 일반 서보 드라이브는 목록에 명시된 제품 카테고리가 아니다. 드라이브의 핵심 기능이 모터 제어라면 단순히 내부에 보안 기능 MCU, Ethernet 포트 또는 방화벽 기능을 일부 포함한다는 이유만으로 해당 카테고리로 분류하지 않는다.
- 별도 판매되는 보안 게이트웨이, 네트워크 관리 소프트웨어, 보안 기능 MCU 등은 각자의 제품 경계와 핵심 기능으로 별도 분류한다.

### 3.5 명시적 적용 제외 및 다른 EU 법령과의 관계
- Article 2(2): Regulation (EU) 2017/745(의료기기), Regulation (EU) 2017/746(체외진단 의료기기), Regulation (EU) 2019/2144(차량 형식승인 관련 제품)에 해당 EU 법령이 적용되는 PDE는 CRA 적용 제외 대상이다.
- Article 2(3): Regulation (EU) 2018/1139에 따라 인증된 PDE는 제외된다.
- Article 2(4): Directive 2014/90/EU(선박 장비) 적용 장비는 제외된다.
- Article 2(6): 동일한 사양으로 제조되어 동일 부품을 대체하는 예비부품은 제외된다. 단순히 '부품'이라는 이유만으로 제외되는 것은 아니다.
- Article 2(7): 국가안보·국방 목적만을 위해 개발/수정되거나 기밀정보 처리만을 위해 특별히 설계된 PDE는 제외된다.
- Article 2(5): 다른 EU 법령이 Annex I의 일부/전체 위험을 다루는 경우에도 자동 면제가 아니다. 동일하거나 더 높은 보호수준 등 법정 조건을 충족하고 Commission delegated act가 구체적인 제한/제외를 명시해야 한다.
- 따라서 일반 산업기계용 서보 드라이브는 Machinery Regulation이 존재한다는 이유만으로 CRA에서 자동 제외되지 않는다. 다만 드라이브가 의료·차량·항공·선박 제품에 통합되는 경우 제품 경계와 해당 sectoral law 적용 여부를 별도 검토한다.

## 4. 적용 일정과 전환 규칙

| 날짜 | 법적/행정적 사건 | 제조사 영향 |
|---|---|---|
| 2024-12-10 | CRA 발효 | 준비·설계 기준 확정 |
| 2026-06-11 | Chapter IV(Articles 35–51) 적용 | 적합성 평가기관 통보 체계 관련 |
| 2026-09-11 | Article 14 적용 | 적극 악용 취약점 및 제품 보안 영향 심각 사고 신고 의무 운영 |
| 2027-01-20 | Machinery Regulation (EU) 2023/1230 전면 적용 예정 | 기계류의 사이버보안 관련 안전 요구와 CRA 관계 검토 |
| 2027-03-26 | EHDS Regulation (EU) 2025/327의 관련 CRA 개정 적용 | 고위험 AI/EHR 등 해당 제품에 한정된 조정 검토 |
| 2027-12-11 | CRA 일반 적용 | 제품 요구사항·취약점 처리·기술문서·적합성 평가 등 본격 적용 |

### 4.1 기존 설치 제품 및 출시 전 제품
- Article 69(2)에 따라 2027-12-11 이전 시장에 출시된 PDE가 그 날짜 이후 실질적으로 변경되고 다시 시장에 공급되는 경우, 변경한 자가 제조자로 간주될 수 있다. 단순 유지보수·수리·위험을 줄이는 보안 업데이트가 언제나 실질적 변경인 것은 아니다. 변경이 초기 위험평가에서 예상되지 않았는지, intended purpose·위험의 성격·사이버보안 위험 수준에 영향을 주는지 사례별로 판단한다.
- Article 69(3) 및 Article 71(2)에 따라 Article 14 신고 의무는 2026-09-11부터 CRA 적용 대상인 모든 제품에 적용되며 2027-12-11 이전 출시 제품도 포함한다.
- Commission Guidance는 기존 출시 제품 또는 지원기간이 끝난 제품에 대해서도 Article 14 신고 의무가 지속되지만, 2027-12-11 이전 출시 제품 또는 지원기간 종료 제품에는 Annex I Part II의 취약점 처리 의무가 적용되지 않는다고 설명한다. 단, 별도 법률·계약·안전 의무는 별개로 검토한다.

## 5. 제조사 핵심 의무와 증거

### 5.1 제품 위험평가 및 설계
- Article 13(2)–(4): 제품의 intended purpose, reasonably foreseeable use, 환경·외부 의존성·구성요소를 반영한 사이버보안 위험평가를 수행하고 기술문서에 포함한다.
- Annex I Part I: 위험에 비례한 보안 수준, 알려진 악용 가능 취약점 없는 출시, secure-by-default, 보안 업데이트, 인증/접근통제, 기밀성·무결성·가용성, 공격 표면 축소, 완화, 보안 로깅 및 데이터·설정 삭제 기능 등을 제품별로 적용한다.
- 모든 세부 요구를 기계적으로 동일 적용하지 않는다. 위험평가 결과와 제품 기능·기술적 제약을 근거로 적용성 및 대체/보상 통제를 문서화한다.

### 5.2 구성요소·SBOM·취약점 처리
- Annex I Part II (1): 제품 내 구성요소와 취약점을 식별·문서화하고, 최소 최상위 의존성을 포함한 통상 사용되는 기계 판독 형식의 SBOM을 작성한다. 이는 제조자의 취약점 처리 의무이며, SBOM을 일반 사용자에게 무조건 공개해야 한다는 뜻은 아니다. Annex VII(2)(b)는 SBOM을 기술문서의 취약점 처리 프로세스 설명에 포함한다. Annex VII(8)의 시장감시당국 요청 조건은 별도의 추가 제출 규정이므로 Annex I Part II(1)의 기본 작성 의무를 선택사항으로 만들지 않는다.
- Article 13(5)–(6): 제3자 구성요소를 통합할 때 위험에 비례한 due diligence를 수행하고, 통합 구성요소에서 확인된 취약점을 구성요소 제조자/유지관리자에게 알리며 제품 차원에서 처리한다.
- Annex I Part II (2)–(8): 취약점 지체 없는 처리, 보안 테스트·리뷰, 수정 취약점 공개, coordinated vulnerability disclosure(CVD), 취약점 제보 경로, 안전한 업데이트 배포, 지체 없는 무상 보안 업데이트를 관리한다. 맞춤형 제품과 business user 사이의 별도 합의 예외는 정확히 구분한다.

### 5.3 지원기간·업데이트
- Article 13(8): 예상 사용기간을 반영한 지원기간을 설정한다. 최소 5년 원칙은 제품 예상 사용기간이 5년 미만인 경우 예외가 있으며, 산업용 제어 장비의 실제 수명·사용자 기대·부품/운영환경 지원기간을 고려한다.
- Article 13(9): 지원기간 중 사용자에게 제공한 각 보안 업데이트는 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능해야 한다.
- Article 13(19): 구매 시 지원 종료일(최소 월·연도)을 명확히 표시하고, 기술적으로 가능한 경우 지원 종료 알림을 제공한다.
- 보안 업데이트와 기능 업데이트는 기술적으로 가능한 경우 분리한다(Annex I Part II (2)). 보안 업데이트의 무상 제공은 Part II (8)의 문언 및 맞춤형 제품 예외를 확인한다.

### 5.4 사용자 정보·기술문서·적합성
- Annex II: 제조자 및 취약점 제보 연락처, 제품 식별, intended purpose, 보안 특성, 알려진 위험, 지원기간 종료일, 안전한 설치·운영·업데이트·폐기 지침을 사용자에게 제공한다.
- Article 31 및 Annex VII: 제품 설명, 소프트웨어 버전, 하드웨어/아키텍처, 설계·개발·생산·취약점 처리 프로세스(Annex VII(2)(b)의 SBOM·CVD·취약점 연락 주소·안전한 업데이트 배포 기술 포함), 위험평가, 지원기간 근거, 적용 표준/기술사양, 시험 보고서, EU DoC를 기술문서에 포함한다. Annex VII(8)은 해당되는 경우 시장감시당국의 합리적 요청 및 적합성 확인에 필요한 경우의 추가 SBOM 제출을 별도로 규정한다.
- Article 13(13): 기술문서와 EU DoC는 제품을 시장에 출시한 뒤 최소 10년 또는 지원기간 중 더 긴 기간 동안 시장감시당국이 열람할 수 있도록 보존한다. Article 13(18)도 Annex II 사용자 정보·지침의 보존 및 온라인 접근 기간에 같은 기준을 둔다.
- Article 28/30: 적합성 평가 후 EU Declaration of Conformity(DoC)를 작성하고 CE marking을 부착한다.
- Article 32(1): 일반 제품은 제조자가 Module A(내부 관리), Module B+C(EU type examination + production control), Module H(full quality assurance) 또는 가능한 경우 EU 사이버보안 인증 절차 중 하나로 적합성을 입증한다. Module A는 통상 단순한 선택지지만 유일한 경로라고 단정하지 않는다.
- Article 32(2): Annex III Class I 제품은 관련 조화표준/공통사양/실질적 보증 수준의 EU 인증을 전부 적용하지 않았거나 그러한 기준이 존재하지 않는 경우, 해당 요구사항에 대해 Module B+C 또는 Module H를 적용한다.
- Article 32(3): Annex III Class II 제품은 Module B+C, Module H 또는 가능한 경우 실질적 보증 수준 이상의 EU 사이버보안 인증을 사용한다.
- Article 32(4): Annex IV critical 제품은 Article 8(1)에 따른 EU 인증이 요구되는 경우 그 인증을 사용하고, 해당 조건이 충족되지 않으면 Article 32(3)의 절차를 적용한다.

### 5.5 추가 제조사 의무 및 시장감시 대응
- Article 13(14): series production 제품은 계속 적합성을 유지하는 절차를 갖추고, 개발/생산/설계/특성 및 적용 표준 변경을 적절히 반영한다.
- Article 13(15)–(16): 제품의 type/batch/serial 등 식별정보와 제조자 명칭·상표·우편주소·이메일/디지털 연락처를 제품, 포장 또는 동봉 문서에 표시하고 사용자 정보에도 반영한다.
- Article 13(20): 제품과 함께 EU DoC 사본 또는 간이 EU DoC를 제공한다. 간이 선언을 제공하면 전체 DoC의 정확한 인터넷 주소를 포함한다.
- Article 13(21): 시장 출시 시점부터 지원기간 동안 제품 또는 제조사 프로세스가 Annex I 요구에 부합하지 않는다고 알거나 믿을 이유가 있으면 즉시 시정조치를 취하고, 필요하면 제품을 철회/리콜한다.
- Article 13(22): 시장감시당국의 합리적 요청 시 적합성 입증에 필요한 문서·정보를 제공하고 위험 제거 조치에 협력한다.
- Article 13(23): 제조사가 운영을 중단해 CRA 의무를 이행할 수 없게 되는 경우, 운영 중단 전에 관련 시장감시당국과 가능한 범위의 사용자에게 알린다.

### 5.6 EU 경제운영자 역할 및 공급망 책임
- Article 18: authorised representative는 서면 위임 범위 내에서 DoC/기술문서 보관·당국 요청 대응 등 위임된 업무를 수행한다. 제조자 책임 전체를 자동 이전받는 것은 아니다.
- Article 19: EU importer는 시장 출시 전 제조자 적합성, CE/DoC, 사용자 정보, 식별/연락/지원 종료일 표시 등을 확인하고, 취약점 발견 시 제조자에게 알린다.
- Article 20: distributor는 CE 표시, 제조자/수입자의 필수 표시·문서 제공 여부를 확인하고, 부적합/중대한 위험을 인지하면 공급 보류·통지·시정 조치를 수행한다.
- Article 21–22: importer/distributor가 자기 이름/상표로 제품을 출시하거나 실질적 변경을 수행하는 경우, 또는 다른 자가 실질적 변경 후 시장에 공급하는 경우 제조자 의무가 적용될 수 있다.
- Article 23: 경제운영자는 공급받은 자와 공급한 자의 식별정보를 각 거래 후 10년간 제공할 수 있도록 보관한다.
- 한국 제조사는 EU 내 authorised representative, importer, distributor, 상표 표시 주체 및 실질적 변경자의 역할을 계약·라벨·공급 경로별로 구분해야 한다.

## 6. Article 14 신고 체계 — 이미 적용 중

### 6.1 적극 악용 취약점(Article 14(1)–(2))
- 제조자가 제품에 포함된 취약점의 적극 악용을 인지하면 CSIRT designated as coordinator와 ENISA에 신고한다.
- Early warning: 인지 후 부당한 지체 없이, 최대 24시간 이내.
- Vulnerability notification: 인지 후 부당한 지체 없이, 최대 72시간 이내.
- Final report: 시정/완화 조치가 제공된 후 최대 14일 이내.

### 6.2 제품 보안에 영향을 미치는 심각한 사고(Article 14(3)–(5))
- Early warning: 인지 후 최대 24시간 이내.
- Incident notification: 인지 후 최대 72시간 이내.
- Final report: 72시간 신고 후 1개월 이내.
- 심각성 판단은 민감/중요 데이터 또는 기능의 가용성·진정성·무결성·기밀성 보호에 대한 부정적 영향 가능성, 또는 악성 코드의 제품/사용자 시스템 내 유입·실행 가능성 등을 고려한다.

### 6.3 운영 통제
- 단일 신고 플랫폼은 ENISA가 설치·운영한다(Article 16). ENISA SRP FAQ는 2026-09-11부터 운영 중임을 확인한다.
- SRP 접속: https://portal.cra-srp.enisa.europa.eu. 2026-10-15 FAQ 기준 API 미제공 및 영어 UI 전용이다. 초기 운영상 기능 제한과 카운터 주의사항은 §25 및 [SRP 운영 준비 기준서](CRA_SRP_OPERATIONAL_READINESS_2026-11-20.md)를 따른다.
- 신고할 CSIRT는 Article 14(7)에 따라 제조자의 EU 내 주된 사업장 소재국을 기준으로 한다. 주된 사업장은 제품 사이버보안 관련 의사결정이 주로 이루어지는 곳이며, 이를 특정할 수 없으면 EU 내 직원 수가 가장 많은 사업장 소재국을 적용한다. EU 내 주된 사업장이 없는 제조자는 authorised representative, importer, distributor 및 제품 사용자가 가장 많은 회원국 순으로 법정 기준을 확인한다.
- Assigned Representative(AR)는 개인 EU Login 계정과 MFA를 사용한다. Primary AR 1명과 최대 20명의 Secondary AR 구조, AR 연계 검증 및 권한은 ENISA FAQ 최신판에서 재확인한다.
- Article 14 의무 AEV/SI 신고와 Article 15 자발적 신고를 분리한다. 2026-10-15 FAQ 기준 SRP의 Article 15 자발적 신고 기능은 아직 구현되지 않았다.
- SRP 장애 시 직접 CDaC 연락이 필요할 수 있으나, 복구 후 SRP 제출 의무는 남는다. 내부 절차는 최초 인지시각 UTC 기준으로 24h/72h/최종보고를 독립 계산하며 UI 카운터를 법정 시한으로 사용하지 않는다.
- Article 14는 지원기간 종료 후에도 적용될 수 있으므로 설치 제품의 자산/고객 식별 및 연락 체계를 유지한다.

### 6.4 자발적 신고와 의무 신고 구분
- Article 15는 Article 14의 의무 신고 대상이 아닌 취약점, 위협 또는 near miss 등에 대해 제조자/기타 자가 자발적으로 신고할 수 있는 체계를 둔다.
- 모든 취약점 발견을 Article 14에 따라 강제 신고한다고 표현하지 않는다. 적극 악용 취약점 및 제품 보안에 영향을 주는 severe incident는 Article 14 의무 신고, 그 외는 Article 15 자발적 신고 가능성으로 분리한다.
- 자발적 신고가 Article 14 의무 신고를 대체하거나 지연시키는 근거는 아니다.

## 7. 표준화 현황과 적합성 평가 전략

### 7.1 2026-11-10 M/606 개정
Commission Implementing Decision C(2026) 7861 final Annex는 M/606의 41개 표준 납품 일정을 다음과 같이 수정했다.

| M/606 항목 | 범위 | 개정 납품 기한 |
|---|---|---|
| 1 | 제품의 위험기반 보안 설계·개발·생산 수평 표준 | 2026-11-30 |
| 15 | 취약점 처리 수평 표준 | 2026-11-30 |
| 16–41 | Annex III/IV 제품 카테고리별 수직 표준 | 2027-01-31 |
| 2–14 | Annex I Part I 제품 속성 관련 나머지 수평 표준 | 2027-10-30 |

- 서보 드라이브 자체는 현재 Annex III/IV의 제품별 수직 표준 카테고리에 명시되어 있지 않다. 다만 모든 PDE에 적용되는 수평 요구사항은 계속 검토해야 한다.
- 납품 기한은 표준화기구가 표준을 완성·제출해야 하는 일정이다. CRA 의무 적용일 2027-12-11을 연기하지 않는다.
- 내부 표준 승인 또는 발행만으로 CRA 추정 적합성이 발생하지 않는다. Article 27에 따라 OJ에 조화표준 참조가 공표되었는지와 해당 표준이 포괄하는 요구사항을 확인한다.
- M/606 Annex는 2026-11-17 현재 확인한 공식 원문 기준이다. 향후 Commission standardisation page, CEN/CENELEC/ETSI 및 OJ 공표를 정기 재확인한다.

### 7.2 서보 드라이브 제조사 권고
- 기본 제품 범주에 해당하면 Annex I 요구사항 자체를 기준으로 내부 위험평가·설계·검증·기술문서를 준비한다. 표준이 늦어지는 것을 이유로 준비를 지연하지 않는다.
- Annex III Class I/II 가능성이 확인되면 실제 OJ 공표 표준 범위와 Article 32 평가 경로를 검토하고, 필요한 경우 Notified Body 접근을 일정·비용 위험으로 관리한다.
- 특정 표준 번호·초안 상태·표준의 적용 범위는 공식 원문과 OJ 공표를 확인하기 전까지 확정하지 않는다.

## 8. 기계류 규정과의 관계

- CRA Recital 49 및 Commission Guidance §9.3.2는 기계류 규정과의 사이버보안 요구가 겹칠 수 있음을 전제로 한다. Regulation (EU) 2023/1230의 Annex III Sections 1.1.9 및 1.2.1은 control system의 corruption 방지, 안전·신뢰성 등 사이버보안 관련 안전 요구를 포함한다.
- Machinery Regulation은 2027-01-20부터 전면 적용된다.
- 기계류 규정에 따라 발급된 유효한 EU type-examination certificate/approval decision이 해당 사이버보안 위험을 실제로 평가·포함했다면 CRA Article 69(1)에 따라 그 위험 범위에 한해 2028-06-11까지 효력이 인정될 수 있다(조기 만료 또는 다른 규정의 별도 조건은 제외).
- 이 효력은 포괄적 CRA 면제가 아니다. 기존 인증서가 다루지 않은 추가 CRA 위험은 Article 13 위험평가로 식별하고 완화해야 한다.
- 서보 드라이브 단품과 기계에 통합된 드라이브, 안전 관련 제어 시스템의 역할을 구분해 제품 경계 및 인증서 범위를 검토한다.

## 9. 제품별 최종 판정을 위해 필요한 증거

다음 정보가 확보되기 전에는 특정 서보 드라이브 모델의 CRA 적용 여부, Annex III/IV 분류, 지원기간 및 적합성 평가 경로를 확정하지 않는다.

1. 제품 모델/제품군, 제조자·상표, EU 시장 공급 주체 및 공급 방식.
2. 하드웨어 블록도, MCU/CPU/FPGA/메모리 구성, 펌웨어 및 부트로더 버전.
3. 통신 인터페이스와 프로토콜 목록, 실제 데이터 흐름, 설정·진단·원격 제어 기능.
4. 디지털 통신이 아닌 단순 전기 신호만 존재하는 인터페이스의 구분.
5. PC commissioning/configuration tool, mobile app, gateway, cloud/RDPS의 제공 주체와 기능 의존성.
6. 제품 intended purpose, reasonably foreseeable use, 설치 환경, 연결되는 PLC/산업 네트워크/상위 시스템.
7. 제품의 핵심 기능과 보안 기능의 경계, 별도 판매되는 구성요소의 유무.
8. EU 최초 출시/개별 제품 공급 시점, 현장 설치 제품의 펌웨어·하드웨어 변경 이력.
9. 예상 수명, 보증·유지보수 정책, 부품 공급 및 OS/SDK/third-party component 지원기간.
10. 기존 Machinery Regulation 또는 다른 EU 법령에 따른 시험·인증서와 해당 인증서가 다루는 구체적 사이버보안 위험.

## 10. 실행 권고 및 검증 순서

기술 통제/시험의 세부 초안은 [CRA 서보 드라이브 보안 통제·시험 매트릭스 (36항목)](CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)에 정리했다. 논리 블록과 신뢰 경계의 참조 설계는 [CRA 서보 드라이브 참조 보안 아키텍처 v0.1](CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md)에 별도로 정리했다. 매트릭스의 구현 후보는 위험기반 설계 선택지이며, CRA가 모든 제품에 동일한 특정 기술(예: MFA, RBAC, 디지털 서명, STO/SS1)을 직접 명령한다는 의미가 아니다.

1. 제품군/모델별 데이터 연결 및 제품 경계 매트릭스 작성.
2. Annex III/IV 핵심 기능 분류표와 Article 32 적합성 평가 경로 확정.
3. 위협 모델과 Article 13 위험평가를 작성하고 Annex I Part I 요구사항별 적용성·대체 통제 근거를 기록.
4. SBOM, 취약점 처리, CVD, 보안 업데이트 배포, 지원기간 및 Article 14 신고 절차를 운영 프로세스로 연결.
5. Annex VII 기술문서, Annex II 사용자 정보, EU DoC/CE 증거를 하나의 추적 체계로 연결.
6. 각 요구사항을 설계 산출물·시험 케이스·시험 결과·시정조치와 연결하고, 법령 직접 요구와 권고 구현을 분리.
7. 2026-11-30 및 2027-01-31 M/606 표준 일정, OJ 공표 여부, CRA FAQ/Guidance 개정, Machinery Regulation 적용을 정기 점검.

## 11. CRA 정정 보고서 #1–#38 통합 감사 결과

저장소의 개별 정정 보고서 #1–#38을 모두 조회하고, 각 보고서의 주요 오류 유형·수정 조항·기술 권고와 법적 의무의 구분을 통합했다. 세부 원문, 원본 archive 경로 및 원본 blob SHA는 [정정 보고서 인덱스](CRA_CORRECTION_INDEX_2026-11-17.md)와 개별 보고서에 보존한다.

### 11.1 반복적으로 발견된 법령 인용 오류
1. Article 10/11을 제조사 의무 근거로 사용한 오류: Article 10은 회원국 역량 증진, Article 11은 General product safety이며, 제조사 일반 의무는 Article 13이다.
2. Article 14를 취약점 처리/CVD 조항으로 혼동한 오류: Article 14는 제조자의 규제기관 신고, Article 15는 자발적 신고, Article 16은 단일 신고 플랫폼이다. CVD는 Article 13(8) 및 Annex I Part II (5), 제보 연락 주소는 Part II (6), 사용자 단일 연락 창구는 Article 13(17)/Annex II (2)다.
3. Annex I Part I과 Part II의 혼합: Part I은 제품 속성의 필수 사이버보안 요구, Part II는 제조자의 취약점 처리 프로세스다. 최종 OJ Part II는 번호 (1)–(8)이며, 초안/타협안의 구문을 직접 인용하지 않는다.
4. 기술문서는 Article 31/Annex VII, 사용자 정보·지침은 Article 13(18)/Annex II다. Annex VI는 간이 EU DoC이며 SBOM 또는 기술문서 부속서가 아니다.

### 11.2 Annex I Part I의 정확한 기술 요구 locator
- (1): 위험에 기반한 적절한 사이버보안 수준.
- (2)(a): 알려진 악용 가능한 취약점 없이 시장 출시.
- (2)(b): secure-by-default 및 원래 상태로 재설정 가능.
- (2)(c): 취약점 보안 업데이트, 해당되는 경우 자동 업데이트 기본 설정·적절한 설치 시기·opt-out·업데이트 알림·임시 연기.
- (2)(d): 적절한 통제 메커니즘, 인증/ID·접근관리 등을 통한 무단 접근 방지 및 가능한 무단 접근 보고.
- (2)(e): 저장·전송·처리 데이터 기밀성 보호.
- (2)(f): 데이터·명령·프로그램·설정 무결성 보호 및 corruption 보고. 원문은 “not authorised by the user”이며 manufacturer가 아니다.
- (2)(g): intended purpose에 필요한 범위로 데이터 최소화.
- (2)(h): 사고 이후를 포함한 essential/basic functions 가용성 및 DoS 완화.
- (2)(i): 제품/연결 장치가 다른 장치·네트워크의 서비스 가용성에 미치는 부정적 영향 최소화.
- (2)(j): 외부 인터페이스를 포함한 공격 표면 제한.
- (2)(k): exploitation mitigation을 통한 사고 영향 최소화.
- (2)(l): 관련 내부 활동의 기록·모니터링(데이터/서비스/기능 접근·변경 포함) 및 사용자 opt-out.
- (2)(m): 사용자가 데이터·설정을 안전하고 쉽게 영구 삭제할 수 있는 기능 및 안전한 이전.

### 11.3 취약점 처리·업데이트·지원기간 정정
- SBOM은 commonly used machine-readable format이며 최소 top-level dependencies를 포함한다. 모든 transitive dependency 포함이나 일반 사용자에 대한 무조건 공개를 CRA가 일률 요구하지 않는다.
- 지원기간은 Article 13(8)에 따라 예상 사용기간·사용자 기대·제품 성격 등을 반영하며 최소 5년 원칙, 예상 사용기간이 5년 미만이면 그 기간이다.
- Article 13(9)의 10년은 지원기간 중 제공된 각 보안 업데이트의 발행 후 이용 가능 기간이며, 제조사 지원기간을 10년으로 정한 규정이 아니다.
- 기능 업데이트와 보안 업데이트 분리는 Annex I Part II (2)의 “where technically feasible” 조건이 있고, 안전한 배포는 (7), 식별된 보안 이슈를 다루는 보안 업데이트의 무상 제공은 (8)이다. 맞춤형 제품/business user 합의 예외를 함께 표시한다.
- 수정 취약점 공개는 Part II (4)의 업데이트 제공 이후 공개가 원칙이며 정당한 보안 사유에 따른 지연 예외가 있다. 모든 취약점의 즉시 공개 의무로 확대하지 않는다.

### 11.4 신고·접근통제·설계 권고의 경계
- Article 14의 24h/72h/최종 보고 기한은 적극 악용 취약점과 제품 보안에 영향을 주는 severe incident에 각각 적용되며, 두 유형의 최종 보고 기한은 다르다. 모든 취약점에 24h/72h가 적용되는 것은 아니다.
- least privilege, RBAC, MFA, 장치별 고유 비밀번호, 디지털 서명, 특정 암호 알고리즘, immutable log, SIEM, hardware resource isolation, 자동 rollback, STO/SS1 전이, 특정 필드버스별 ACL은 CRA가 모든 서보 드라이브에 직접 지정한 구현이 아니다. 위험평가에 따라 선택할 수 있는 엔지니어링 통제/검증 후보로 분류한다.
- CRA는 모든 서보 드라이브에 DoS 시 STO/SS1을 강제하지 않는다. 안전 상태·제어 연속성·브레이크 동작은 제품 hazard analysis 및 별도 기능안전 요구로 결정한다.
- 일반 서보 드라이브가 Annex III Class I/II 또는 Annex IV에 자동 포함되지 않는다. 제품의 core functionality가 열거된 범주와 일치하는지 판단하며, 통합된 보안 MCU의 분류를 완제품에 자동 전이하지 않는다.
- NIST SP 800-88 Rev.1은 2025-09-26 철회되고 Rev.2로 대체되었다. 매체 삭제 설계 참고자료로 사용할 때 현행 판본을 확인하고, CRA 직접 법적 요구와 구분한다. Flash/SSD에 과거식 multi-pass overwrite를 무조건 적용하지 않는다.

## 12. 법적 한계

이 문서는 공개 법령 및 공식 자료에 기초한 일반 기술·규제 조사 초안이다. 특정 모델의 실제 회로·펌웨어·프로토콜·시장 공급 구조를 검토하지 않았으므로 법률 자문, 적합성 선언, 인증 또는 시장 출시 승인으로 사용할 수 없다. 최종 적용성 및 적합성 평가는 제조자 책임하에 제품별 증거와 최신 법령을 기준으로 수행해야 한다.

## 13. 주요 공식 출처

| 출처 | 용도 |
|---|---|
| Regulation (EU) 2024/2847, EUR-Lex / OJ | CRA 구속력 있는 법령·Annex 원문 |
| https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng | CRA 공식 ELI |
| Commission Guidance C(2026) 5252 (2026-07-27), OJ Communication C/2026/6013 (17.11.2026) | 적용 범위, 데이터 연결, 제품 경계, 핵심 기능, 지원기간, 신고, 기계류 규정 관계 해석; 현재 공식 인용 기준 |
| https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013 | Commission Guidance 공식 관보 PDF (OJ C/2026/6013); 61 pages; SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2` |
| https://www.anfr.fr/fileadmin/CRA/Commission_guidance_on_the_application_of_Regulation__EU__20242847__Cyber_Resilience_Act_.pdf | C(2026) 5252 historical mirror copy; mirror-only SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; not claimed byte-identical to OJ PDF |
| https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation | Commission CRA 이행 일정 |
| https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions | Commission CRA FAQ (마지막 갱신 2026-09-04) |
| https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | Commission 신고 의무·SRP 설명 (2026-09-11 갱신) |
| https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation | Commission 표준화 현황 및 M/606 |
| https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401 | C(2026) 7861 final Annex, M/606 개정 납품 기한 |
| https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng | EHDS Regulation 및 CRA 일부 개정 |
| https://csrc.nist.gov/pubs/sp/800/88/r2/final | NIST SP 800-88 Rev.2 (2025-09-26), media sanitization 기술 참고자료; CRA 법령은 아님 |
| https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions | ENISA Single Reporting Platform FAQ (2026-10-15 갱신) |

---
작성 기준일: 2026-11-17. 본문에서 '가능성 높음', '잠정'으로 표시된 결론은 제품별 증거 확보 후 확정한다.


## 14. Commission Guidance 및 M/606 표준화 근거 추적 — 2026-11-17 추가

- [Commission Guidance claim register](CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv)에 G-001~G-013의 비구속적 Commission 설명을 등록했다. 각 claim은 문서 locator, PDF page, 관련 CRA requirement/interface/SEC control ID와 연결한다.
- Guidance claim은 CRA 법령상 독립 의무가 아니다. 모든 CSV 열의 claim ID는 해석 근거의 추적 링크이며, 법적 요구사항을 새로 만들거나 적합성을 입증하지 않는다.
- [인터페이스 적용성 매트릭스](CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)에 Guidance claim ID 및 M/606 Annex I의 조건부 후보 항목 열을 추가했다. IF-001~IF-013은 §2.5 data-connection 판단과 연결하고, IF-014는 §2.4 제품 경계, IF-015는 §8 RDPS 조건과 연결한다.
- [요구사항 추적표](CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv)에 §2.4/§2.5/§2.6/§4/§5/§6/§7/§8/§9의 관련 claim ID를 연결했다. CRA-027은 M/606 Annex I 항목 1–41 표준화 주제를 참조하되, 이는 OJ harmonised status나 presumption of conformity를 뜻하지 않는다.
- [보안 통제·시험 매트릭스](CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv)에 Guidance claim ID와 M/606 Annex I 후보 항목을 연결했다. 항목 25, 28–30, 36–41은 구성요소/제품 유형의 실제 포함 및 intended purpose 확인을 전제로 하는 조건부 관련성이다.
- M/606 Annex I 표준화 주제는 표준 개발·채택 계획으로 관리한다. 드라이브에 관련 MCU/FPGA/네트워크 인터페이스/secure element가 들어간다는 이유만으로 드라이브 전체가 해당 수직 제품 유형에 자동 분류되지 않는다.
- Guidance PDF는 ANFR mirror raw-byte SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`를 검증했으나 Commission-hosted primary byte identity는 미확인이다. M/606 Commission Annex raw-byte SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276` 및 6페이지를 확인했다. M/606 item 18 deadline `31/01/2027`은 원본 PDF page image에서 시각 확인했다. 세부 값은 [PDF provenance manifest](CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json)를 참조한다.


- [Commission Guidance claim register](CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv)에 G-001~G-013의 비구속적 설명, 원문 문단/페이지 locator 및 관련 CRA requirement/interface/SEC control 연결을 기록했다.

## 15. M/606 Annex I 41개 항목의 서보 드라이브 관련성

- [M/606 Annex I 41-item relevance map](CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv)에 모든 항목의 paraphrased topic, ESO adoption deadline, PDF page locator, 관련 CRA requirement/SEC control/interface 후보 및 서보 드라이브 관련성 판단을 기록했다.
- 항목 1–14는 horizontal property 표준화 주제, 항목 15는 horizontal vulnerability-handling 주제로 분류했다. 두 범주 모두 수평 표준화 항목이며 ESO adoption deadline은 제조자의 CRA compliance deadline이 아니다.
- 항목 16–27 및 31–36은 vertical product-type 항목이다. servo drive의 내장 기능·포트·웹뷰·부트로더 사용만으로 제품 전체가 해당 vertical product type으로 자동 분류되지 않는다. intended purpose, product boundary 및 core functionality로 판단한다.
- 항목 28–30 및 37–39는 security-featured component 후보로 다뤘다. 실제 부품번호·기능·공급자 증거가 확인될 때 CRA-006/CRA-024 및 관련 SEC control의 component due diligence에 연결한다. 부품 포함만으로 완제품이 vertical category가 되지 않는다.
- 항목 25(network interfaces), 36(industrial firewall/IDS/IPS), 41(secure elements)은 실제 제품 기능·의도된 목적에 따른 조건부 후보로 표시했다.
- 항목 18 password-manager standard의 ESO adoption deadline `31/01/2027`은 PDF printed page EN 2의 우측 셀에서 시각 확인했다. 행의 설명은 EN 3으로 이어지지만 기한 셀은 EN 2에 있다. 이 표의 날짜는 ESO 표준 채택 일정이지 servo-drive 제조자의 직접 compliance deadline이 아니다.
- M/606은 표준화 요청이다. 이 결정만으로 해당 표준이 OJ에 인용된 harmonised standard가 되거나 presumption of conformity가 발생하지 않는다.



- 2026-11-18 기준 Commission의 공식 harmonised-standards index 및 EUR-Lex exact search에서 CRA-specific OJ citation은 확인되지 않았다. M/606 Annex와 ESO draft/work-programme는 harmonised-standard OJ reference가 아니므로, Article 27 presumption of conformity를 주장하지 않는다. 최신 확인 결과와 한계는 `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §9를 참조한다.

## 16. 제품별 사실관계 및 증거 수집 — 미완료

- [CRA 제품 경계 및 증거 수집 기준서](CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md)를 제품별 사실관계 입력 기준으로 추가했다.
- 현재 저장소의 Guidance·M/606 매핑은 일반 서보 드라이브 평가 프레임워크다. 정확한 제조사·모델·사용설명서·데이터시트·BOM/SBOM·네트워크 구성·원격 처리 구조가 확보되지 않았으므로 특정 제품의 CRA 적용성, Annex III/IV 분류, RDPS 여부 또는 최종 적합성을 확정하지 않는다.
- 제품별 증거가 제공되면 제품 경계부터 확정하고, 각 CRA requirement / interface / SEC control / M/606 candidate에 evidence ID와 원문 locator를 연결한다.


- [통합 CRA 보고서 독립 검토 기록](CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md): 보고서 구조, 분류 용어, 공식 근거의 한계 및 후속 2차 검토 항목.


## 17. 법령 문언 심층 대조 Batch 1 (CRA-001–CRA-010, 2026-11-18)

EUR-Lex 공식 Regulation (EU) 2024/2847 원문을 기준으로 CRA-001–CRA-010의 locator와 요구사항 설명을 재검토했다. 상세 행별 근거·한계는 [CRA 법령 문언 심층 감사 Batch 1](CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md)을 참조한다.

핵심 정합화 사항:
- CRA-001: Article 2(1)의 연결성 범위, Article 3(1)의 PDE 정의, Article 3(22)의 상업활동상 시장 공급 정의를 분리한다. 연결 유형 정의(Article 3(8)–(10))와 Recital 9를 추가 근거로 연결한다.
- CRA-003: Article 13(2)는 원격 데이터 처리 정의 조항이 아니므로 해당 locator에서 제외한다. Article 3(2), Recital 11–12를 중심으로 제조자 설계/책임 및 기능 필수성 기준을 적용한다.
- CRA-006: SBOM 직접 근거는 Annex I Part II(1), 기술문서 포함 근거는 Annex VII(2)(b), 체계적 기록은 Article 13(7)로 정리한다. Article 13(5)는 제3자 구성요소 due diligence 문맥으로 구분한다. Annex VII(8)의 합리적 당국 요청 제출을 기본 SBOM 작성 의무의 조건으로 오해하지 않는다.
- CRA-008: 효과적·정기적 테스트/검토는 요구되나 이 조항 자체에 법정 고정 주기 숫자는 없다.
- CRA-009: 수정 취약점 공개는 보안 업데이트 제공 후가 원칙이며, 공개 위험이 이익보다 크다는 정당한 사유가 있는 경우 사용자의 패치 적용 기회까지 공개를 늦출 수 있는 예외를 반영한다.

이 검토는 원문 locator/문언의 1차 심층 대조이며 법률가 의견서가 아니다. 제품별 적용성·적합성은 제품 사실 증거가 없으므로 미확정이다.


## 18. 법령 문언 심층 대조 Batch 2 (CRA-011–CRA-020, 2026-11-18)

EUR-Lex 공식 Regulation (EU) 2024/2847 원문 기준으로 CRA-011–CRA-020을 행별 대조했다. 상세 표는 [CRA 법령 문언 심층 감사 Batch 2](CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md)를 참조한다.

핵심 해석 보완:
- CRA-011: Article 13(17) 단일 연락창구는 직접·신속한 소통, 쉽게 식별 가능, 사용자 선호 통신수단 선택, 자동화 도구만으로 제한 금지를 포함한다.
- CRA-012: Annex I Part II(7)의 안전한 배포 메커니즘을 요구하되 서명/암호학적 무결성/전송 보호 등은 구현 증거 예시로 분리하고 법문에 직접 열거된 독립 요구로 과장하지 않는다.
- CRA-013: 무상 제공 예외는 tailor-made PDE의 business user와 제조자 간 별도 합의로 한정한다.
- CRA-014: 최소 5년 지원기간의 예외는 예상 사용기간이 5년 미만인 경우로 제한되며 객관적 근거와 Annex VII(4) 문서화를 요구한다.
- CRA-016/017: 기술문서의 작성·갱신(Article 31)과 당국 제공 가능 보관(Article 13(13)), 사용자 정보의 제공·보존(Article 13(18))을 구분한다.
- CRA-019: Full EU DoC(Annex V)와 simplified EU DoC(Annex VI)를 구분한다.
- CRA-020: Important/Critical 분류는 Annex III/IV core functionality에 기초하며, 단순 통합만으로 host product에 분류가 전이되지 않는다. Article 32(2) Class I의 조건부 third-party route와 Article 32(3) Class II, Article 32(4) Critical 경로를 분리한다.

제품별 적용성·분류·적합성은 제품 사실 증거가 없으므로 미확정이다.


## 19. 법령 문언 심층 대조 Batch 3 (CRA-021–CRA-035, 2026-11-18)

EUR-Lex 공식 CRA 원문 및 관련 Machinery Regulation/EHDS 원문 기준으로 CRA-021–CRA-035를 행별 대조했다. 상세 행별 근거는 [CRA 법령 문언 심층 감사 Batch 3](CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md)를 참조한다.

핵심 교정:
- CRA-023의 사건 후 사용자 통지는 Article 14(8)이 직접 근거이며 Annex II는 직접 locator에서 제외했다.
- CRA-026의 기계류 규정 상호작용은 CRA Article 2(5), Machinery Regulation Article 9(9), Annex III §§1.1.9/1.2.1을 중심으로 정리했다. CRA Article 69(1)은 일반적인 중복/면제 근거가 아니라 기존 타 EU 법령상 certificate/approval decision의 2028-06-11까지의 유효성 전환이다.
- CRA-028은 Articles 18–22의 경제운영자 역할 및 제조자 책임 전이, CRA-034는 Article 23의 양방향 공급망 추적으로 분리했다.
- CRA-035에 Article 2(8) 정보공개 예외를 추가하고, Article 2(5)는 자동 면제가 아니라 Commission delegated act에 의한 조건부 제한/제외로 명확히 했다.
- Regulation (EU) 2025/327 Article 104는 EHR system에 한정된 CRA 개정이며 일반 PDE/서보 드라이브에 확대 적용하지 않는다.

Article 14의 24h/72h/14일 및 24h/72h/1개월 기산점을 구분하고, 기존 출시 제품에 대한 Article 14의 예외 적용(Article 69(3))과 CRA 일반 적용일(Article 71(2))을 분리했다.


## 20. 전체 교차 매트릭스 정합성 감사 (2026-11-18)

CRA-001–CRA-035 법령 문언 감사 결과를 15개 인터페이스 적용성, 36개 보안 통제·시험, 13개 Commission Guidance claims, 41개 M/606 Annex I 항목과 교차 검토했다. 상세 불일치와 수정 내용은 [CRA 전체 교차 매트릭스 일관성 감사](CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md)를 참조한다.

주요 수정은 SEC-015(SBOM 근거), SEC-018(공개 지연 예외), SEC-021(법정 목표와 구현 후보 구분), SEC-031(RDPS locator), SEC-032(데이터 연결 locator), SEC-034(경제운영자 역할 및 Article 23 추적), SEC-036(전환 조항 범위)다.

현재 매트릭스의 상태값은 제품별 구현/시험 증거가 아직 없다는 뜻이므로 '미작성/증거 미확인' 및 '제품별 미확인'을 유지한다. 법령 문언 대조 완료를 제품 적합성 증거로 해석하지 않는다.


## 21. CEN/CENELEC EN 40000 및 OT 표준 상태 정정 (2026-11-18)

중요 정정: 이전에 작성된 “CRA 표준이 아직 발행되지 않았다”는 포괄적 문장은 더 이상 정확하지 않다. CEN 공식 프로젝트 레코드는 EN 40000-1-1:2026을 **Published**로 표시하며 DOR 2026-11-02, DAV 2026-11-18, DOA 2027-02-28, DOP/DOW 2027-05-31을 기록한다. 다만 해당 CEN 레코드의 CRA OJ citation 필드는 **No citation expected**이므로, 발행 완료가 CRA Article 27(1) 추정 적합성을 의미하지 않는다.

EN 40000-1-2:2026은 2026-11-02 ratification 및 publishing 상태가 tracker/2차 카탈로그에서 확인됐으나, 개별 CEN 공식 페이지의 본문 readback은 HTTP 500으로 실패했다. No citation expected도 tracker/2차 자료에서 확인했으며, 공식 개별 원문 확인 미완료로 기록한다. FprEN 40000-1-3:2026은 CEN 공식 레코드상 Under Approval / Citation expected이고, prEN 40000-1-4는 Work item 단계다.

CENELEC 공식 프로젝트 레코드는 prEN 50770-1~6 모두 Committee stage로 표시한다. 범위는 OT 방화벽/IDS·IPS, 네트워크 관리, 네트워크 인터페이스, VPN, 라우터·모뎀·스위치, SIEM이다. OJ citation expected는 향후 인용 예상 메타데이터일 뿐 실제 OJ 공표가 아니다. 현재 확인된 DOR/DAV는 없으므로 발행 완료로 간주하지 않는다.

서보 드라이브 적용성은 intended purpose/core functionality에 따라 판단한다. Ethernet/fieldbus 포트나 단순 필터링 기능만으로 완제품을 네트워크 인터페이스/방화벽 제품으로 분류하지 않는다. 모델/BOM/데이터시트 미확보 상태에서는 drive-level classification을 Unknown으로 유지한다.

상세 원문 감사: [CEN/CENELEC EN 40000 및 OT prEN 50770 공식 상태 감사](CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md), [구조화 상태 추적표](CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.csv).



## 요구사항–제품 증거 연결의 신규 작업 산출물 (2026-11-18)

CRA 요구사항과 서보 드라이브 설계·시험·기술문서 간의 provisional mapping을 별도 관리한다. EVD-01–EVD-16의 법적 locator, 통제·시험 제안, 최소 증거 패키지, 표준 scope 연결 및 제품별 상태는 [CRA 요구사항–증거 추적 매트릭스](CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md)와 [CSV](CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.csv)를 참조한다.

이 매트릭스는 CRA 법문을 대체하지 않으며, 표준 최종본의 확인되지 않은 조항을 인용하지 않는다. 제품별 증거가 없으므로 모든 EVD 상태는 Unknown / evidence pending이다.

## 최신 M/606 일정 변경 (2026-11-18 정정)

Commission은 2026-11-10 C(2026) 7861 final로 M/606 Annex I을 개정했다. 새 ESO adoption deadline은 item 1(framework) 및 item 15(vulnerability handling) 2026-11-30, items 2–14 일반 보안 요구 2027-10-30, items 16–41 수직 제품별 표준 2027-01-31이다. 이는 표준화기구의 채택 납기이며 발행일, OJ citation, CRA 적용일 또는 Article 27 추정 적합성 발생일이 아니다. Article 2의 1개월 비수락 조건 및 ESO 수령일 확인은 남은 조사 항목이다.

상세: [M/606 개정 결정 일정 추적](CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md). 공식 Commission 안내: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation


## EVD–CRA–SEC 교차 추적 부속서 — 2026-11-19

EVD-01~16과 CRA 요구사항·SEC-001~036 통제의 후보 연결은 [`CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv`](CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv)에 기록한다. 이는 제품별 적용성 판정이나 구현·시험 Pass가 아니며, 제품 모델·SKU·BOM·펌웨어·통신 경계 확인 후 각 링크의 적용성을 승인해야 한다. 세부 책임·검증·합격 게이트는 [`CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md`](CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md)를 기준으로 한다.


## 제품별 증거 register 부속서 — 2026-11-19

제품별 E-001~E-015 자료는 [CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv](CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv)에 기록하고 EVD-01~16에 연결한다. 이 register는 제출·검토·승인 provenance를 추적하는 양식이며 제품별 적합성 결론이 아니다. 모든 항목은 자료가 수령·검증되기 전까지 not_provided로 유지한다. accepted 및 not-applicable 판정은 hash, source/locator, reviewer/date, rationale 등 필수 메타데이터가 있어야 하며 validator가 이를 fail-closed로 검사한다.


## 25. CRA 핵심 이행 최신정보 재검증 — 2026-11-20 (LS 제품조사와 별도 트랙)

### 25.1 프로젝트 범위 재확인

CRA 프로젝트의 중심은 특정 서보드라이브 제조사 조사가 아니라 Regulation (EU) 2024/2847의 전 제품 공통 의무, Commission 해석, 표준화/OJ 상태, 제품 분류·적합성 평가, 취약점·사고 신고, 기술문서 및 증거체계다. LS메카피온 iX7NH는 이 공통 프레임워크를 적용해 보는 사례 연구이며, CRA 법령·표준화·공식 이행정보 조사와 우선순위를 대체하지 않는다.

### 25.2 2026-11-20 현재 공식 출처 최신성 대조

| 공식 출처 | 최신 확인된 버전/날짜 | 2026-11-20 확인 결과 | 법적·증거상 지위 |
|---|---|---|---|
| Regulation (EU) 2024/2847 | OJ L 2024/2847, 2024-11-20 | 기본 구속력 있는 법령. 개정법령과 적용일 별도 확인 | Binding law |
| Commission Guidance C(2026) 5252 / OJ C/2026/6013 | 2026-07-27 guidance; OJ 2026-11-17 | 61페이지 OJ PDF와 기존 claim register를 기준으로 해석. 비구속적 | Official non-binding guidance |
| Commission CRA implementation timeline | 페이지 last update 2026-07-27 | 2026-09-11 Article 14 신고 적용, 2027-12-11 전면 적용 일정 재확인 | Official implementation page |
| Commission CRA reporting obligations page | last update 2026-09-11 | 24h/72h/final report와 SRP 운영 경로 재확인 | Official operational explanation |
| Commission CRA FAQ | Version 1.4, 2026-09-04 | FAQ 자체가 Commission services 작성·비권위적·비구속적임을 명시. 법령/Guidance와 구분 | Official services FAQ, non-binding |
| ENISA CRA SRP FAQ | updated 2026-10-15 | 플랫폼 운영상 제약·절차·카운터 동작·미구현 기능 확인 | Official agency operational guidance |
| ENISA SRP Glossary | Version 1.6, last update 2026-10-21 | 신고 필드·단계별 필수/선택·AEV/SI 구분 확인 | Official agency operational guidance |
| ENISA SRP AR User Manual | Version 1.3, last update 2026-11-04 | AR 등록·신고 제출·수정·연결 관리 절차 문서 존재 확인 | Official agency user manual; page metadata checked |
| Commission Implementing Decision C(2026) 7861 | 2026-11-10 | M/606 Annex I의 41개 표준화 주제·ESO 기한 기준 유지 | Official standardisation request decision |

### 25.3 ENISA Single Reporting Platform의 실제 운영상 주의사항

ENISA의 2026-10-15 SRP FAQ, 2026-10-21 Glossary v1.6 및 2026-11-04 AR User Manual v1.3를 교차 확인했다. 법령의 신고기한과 플랫폼 UI 편의기능을 구분해야 한다.

1. **신고 대상과 기한:** 제조자는 적극 악용 취약점(AEV) 및 제품 보안에 영향을 미치는 심각한 사고(SI)를 인지하면 부당한 지체 없이, 최대 24시간 내 early warning, 최대 72시간 내 notification을 제출한다. AEV final report는 시정/완화 조치가 제공된 뒤 최대 14일, SI final report는 72시간 신고 뒤 1개월이다. 이는 제품 지원기간 종료나 2027-12-11 전면 적용 전 출시 여부만으로 배제되지 않는다(Article 69(3), 71(2); Commission FAQ 5.3; ENISA FAQ 7, 29).
2. **신고 플랫폼:** SRP는 2026-09-11부터 운영 중이다. 제조자는 해당 제조자의 EU 내 주된 사업장 등 Article 14(7) 기준에 맞는 CSIRT designated as coordinator(CDaC)를 선정한다. 하나의 사건에 대해 한 번 제출하고, 해당 CSIRT 및 ENISA에 전달되는 구조다.
3. **담당자·계정:** Assigned Representative(AR)는 개인 EU Login 계정과 MFA를 사용한다. 제조자별 Primary AR 1명과 최대 20명의 Secondary AR를 둘 수 있다. CSIRT의 AR-제조자 연계 검증은 신고와 병행되며, 미검증 상태에서도 최대 20건까지 제출 가능하다는 ENISA FAQ 설명이 있다. 이는 제조자 등록 준비를 늦춰도 된다는 뜻이 아니다.
4. **API 미제공:** ENISA FAQ 15 기준 SRP 초기 릴리스는 API를 제공하지 않는다. 제조자 내부 티켓·취약점 관리·제품 자산·고객 통지 워크플로는 자동화할 수 있지만, 규제 신고 제출은 SRP 웹 인터페이스를 전제로 운영 절차를 준비해야 한다. 향후 API 제공 여부는 재확인한다.
5. **영어 전용:** ENISA FAQ 24 기준 플랫폼 UI는 출시 시점에 영어만 제공된다. Factsheet 번역과 플랫폼 다국어화는 별도 상태다. 한국어 내부 프로세스만 준비해서는 실제 제출 운영이 불충분할 수 있다.
6. **Art. 15 자발적 신고 미구현:** ENISA FAQ 27 기준 현재 SRP는 Article 14의 의무 AEV/SI 신고를 지원하며 Article 15의 자발적 신고 기능은 아직 구현되지 않았다. 모든 취약점을 Article 14로 신고하는 것으로 혼동하지 말고, Art. 15 신고 경로가 실제 제공되는지 추후 재확인한다.
7. **SRP 장애 시:** ENISA FAQ 25는 플랫폼이 일시적으로 unavailable이면 복구 후 SRP에 제출하도록 안내한다. 즉시 연락이 필요하다고 판단하면 지정 CSIRT에 직접 연락할 수 있지만, SRP 복구 후 플랫폼 제출 의무는 남는다. 내부 장애 기록·인지 시각·시도 기록을 남긴다.
8. **UI 카운터를 법정기한으로 오인 금지:** ENISA FAQ 26에 따르면 현재 72시간 카운터는 24시간 Early Warning 제출 후 48시간을 표시하므로, 제조자가 처음 인지한 시각부터 72시간이 지나기 전에 UI가 overdue로 표시될 수 있다. AEV final report 카운터는 현재 구현되지 않았고, SI final report 카운터는 72시간 신고 제출 뒤 1개월로 표시된다. 카운터는 알림·참고용이며 Article 14 법정기한을 대체하지 않는다. 내부 시스템은 최초 인지 시각(UTC)을 기준으로 독립 계산한다.
9. **신고 필드:** Glossary v1.6은 AEV/SI 유형, 제품명·정확한 제품 버전/빌드/모델/FW, 제품 공급 회원국, 관련 구성요소, 인지 시각, 발생 시각, 영향·심각성, 조치, 공격경로 및 PEC 근거 등 필드를 신고 단계별로 구분한다. 초기에 확인되지 않은 사실을 추정해 채우지 않고, 각 단계에서 요구되는 필드와 추후 보완 필드를 구분한다.
10. **PEC 및 정보 공개:** 특히 예외적 상황(PEC)은 CRA Article 16(2)의 법정 조건에 맞는 경우에 한정한다. 단순한 영업비밀 또는 일반적 비공개 요청을 자동으로 PEC로 취급하지 않는다. 근거와 요청 사유를 구체적으로 작성한다.
11. **EUVD/CVE 후속:** ENISA FAQ 35는 Article 17(5)에 따라 제조자 동의를 전제로 공개적으로 알려진 신고 취약점을 EUVD에 추가할 수 있으며, CVE ID 지정 관련 연락이 올 수 있음을 설명한다. 취약점 공개·CVE/EUVD 커뮤니케이션을 incident response 계획에 포함한다.

### 25.4 제조자 내부 운영 준비 체크리스트

- [ ] 취약점/사고 최초 인지 시각을 UTC로 자동·수동 기록하고, 인지 주체·증거·제품 버전을 보존한다.
- [ ] AEV와 SI를 분리 분류하고, 24h/72h/최종보고 시한을 법령 기준으로 별도 계산한다. ENISA UI 카운터만 신뢰하지 않는다.
- [ ] EU 내 주된 사업장 및 Article 14(7) fallback 기준을 법무·사업·보안 책임자가 공동 확정하고 CDaC 목록을 재확인한다.
- [ ] Primary/Secondary AR, EU Login MFA, 제조자 등록정보, 제품 공급 회원국 및 제출권한을 사전 준비한다.
- [ ] API가 없고 UI가 영어 전용인 현행 SRP에 맞춰 영문 보고 템플릿, 승인·번역·제출 절차를 준비한다.
- [ ] SRP 장애 시 직접 CSIRT 연락과 복구 후 SRP 재제출을 포함한 비상 절차를 준비한다.
- [ ] 제품명, SKU, HW/FW/bootloader, 영향 버전, 구성요소/SBOM, 공격경로, 영향, 완화조치의 증거 저장소를 마련한다.
- [ ] Article 16(2) PEC 검토는 법적 조건별 근거와 승인 절차를 두고, 단순 기밀 표시는 PEC와 분리한다.
- [ ] Article 15 자발적 신고 기능, Glossary, User Manual, SRP Status를 신고 직전 다시 확인한다.

### 25.5 최신성·정확성 관리 원칙

- 법적 결론은 모델 내부 지식이나 과거 대화 요약이 아니라 현행 EUR-Lex/OJ 원문 및 공식 기관의 최신 자료에서만 도출한다.
- 공식 출처별로 source ID, 발행/개정일, 조회일(KST), 문서 버전, 원문 URL, 파일 bytes/hash 또는 HTML-parsed 상태, 확인한 locator, 법적 지위, 미확인 사항을 [CRA 공식 출처 최신성 대장](CRA_LIVE_SOURCE_FRESHNESS_REGISTER_2026-11-20.csv)에 기록한다.
- 동적 운영 자료(ENISA SRP FAQ/Glossary/Manual/Status, Commission implementation/reporting/FAQ)는 최소 주 1회 또는 새 공지·문서 버전 감지 시 재조회한다. 표준화·OJ 상태는 최소 주 1회 및 신규 OJ/CEN/CLC/ETSI 공지 시 재조회한다. 이는 프로젝트 내부 관리 주기이지 법적 의무가 아니다.
- 공식 원문을 읽지 못했으면 제목/검색 snippet/목록 메타데이터만으로 본문 확인을 주장하지 않는다. HTML parsed text는 raw PDF bytes/hash 확보와 구분한다.
- 2차 자료는 탐색·교차검토용이며, 법령·표준·제품 기능에 대한 최종 근거로 단독 사용하지 않는다.
- 자동화/pytest/CI 성공은 문서 구조·코드·추적성 검증일 뿐, 법적 해석의 100% 정확성이나 제품 적합성 인증을 의미하지 않는다.

### 25.6 출처 및 열람 한계

- Commission reporting page: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting (last update 2026-09-11; read 2026-11-20).
- Commission implementation page: https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation (last update 2026-07-27; read 2026-11-20).
- Commission CRA FAQ page: https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions (FAQ v1.4, 2026-09-04; Commission services FAQ disclaimer applies).
- ENISA SRP FAQ: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions (updated 2026-10-15).
- ENISA SRP Glossary: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/cra-srp-glossary2 (v1.6, 2026-10-21).
- ENISA AR User Manual page: https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/cra-srp-ar-user-manual (v1.3, 2026-11-04).
- ENISA SRP Status page is listed by ENISA but direct page retrieval failed during this audit; check live status at incident time.
- ENISA HTML pages were parsed and reviewed; binary PDF/HTML downloads, raw bytes and SHA-256 for SRP FAQ/Glossary/User Manual were not acquired in this session. No account registration, notification submission, or live platform workflow test was performed.

**판정:** 신고의 법적 기한과 SRP 운영 현실을 분리해 관리한다. 플랫폼의 현재 UI·기능·언어·카운터는 변경될 수 있으므로 실제 신고 시점에 ENISA 최신 문서를 재확인한다.

## 26. 2026-11-20 CEN/ETSI 표준화 최신상태 정정 — 발행과 OJ 인용의 엄격한 분리

### 26.1 CEN/CENELEC 수평표준 2종은 실제 Published로 갱신

CEN-CENELEC가 2026-11-19 공식 발표를 게시했고, 개별 CEN 카탈로그 레코드를 직접 다시 열람했다.

| 표준 | Work Item | 공식 상태 | DOR | DAV | DOA | DOP/DOW | CRA OJ citation 필드 |
|---|---|---|---|---|---|---|---|
| EN 40000-1-1:2026 Vocabulary | JT013095 | Published | 2026-11-02 | 2026-11-18 | 2027-02-28 | 2027-05-31 | No citation expected for Directive 2024/2847 |
| EN 40000-1-2:2026 Principles, product risk management and lifecycle activities | JT013089 | Published | 2026-11-02 | 2026-11-18 | 2027-02-28 | 2027-05-31 | No citation expected for Directive 2024/2847 |

- EN 40000-1-1은 EN 40000 시리즈의 용어·정의·약어를 제공한다.
- EN 40000-1-2는 PDE의 사이버보안 위험관리와 제품 수명주기(설계~지원 종료·폐기) 활동에 대한 일반 프레임워크다.
- 두 표준은 M/606에 따라 CEN/CENELEC에서 발행되었으나, 개별 공식 카탈로그의 OJ 필드는 CRA Directive 2024/2847에 대해 **“No citation expected”**다. 따라서 Article 27 추정 적합성의 근거로 제시하지 않는다.
- DOR/DAV/DOA/DOP/DOW는 서로 다른 날짜 개념이다. DAV 2026-11-18은 승인된 공식 언어판의 배포 가능일이고, DOP/DOW 2027-05-31은 국가표준 구현/충돌 표준 철회 최종기한이다. 이를 CRA 제조자 준수기한으로 오인하지 않는다.

공식 근거:
- CEN-CENELEC announcement (2026-11-19): https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/
- EN 40000-1-1 CEN record: https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:82349,2307986
- EN 40000-1-2 CEN record: https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:81335,2307986

### 26.2 ETSI M/606 활성 작업 및 서보 드라이브 관련 범위

ETSI Work Programme Version 2.3.3의 M/606 조회 결과는 활성 작업 18개를 표시한다. 이는 3개 ESO가 수행하는 M/606 Annex I 전체 41개 항목과 동일하지 않으며, ETSI 작업만의 일부다. 목록 화면은 18개 중 10개만 표시하므로, 18개 전부를 개별 검토 완료했다고 주장하지 않는다.

| ETSI EN / Work Item | 제품 유형 및 현재 확인 상태 | 산업용 OT/서보드라이브 경계 | 증거 상태 |
|---|---|---|---|
| EN 304 636 / DEN/CYBER-EUS-0020 | Firewalls, IDS/IPS; Comments categorisation assessed (2026-10-06); next milestone target 2026-12-22 | 제품 자체의 핵심 기능이 방화벽/IDS/IPS인 경우. 서보드라이브의 단순 패킷 필터·포트 보호만으로 분류하지 않음. 조회된 scope에는 OT exclusion 문구가 보이지 않음 | ETSI individual record metadata/scope read |
| EN 304 625 / DEN/CYBER-EUS-0017 | Physical/virtual network interfaces; Comments categorisation assessed (2026-11-05); 1.0.0; 2026-11-19 remark: EC second assessment received in batches dated 2026-09-28 and 2026-11-16 | CRA Annex III Class I의 network interfaces scope. Ethernet/EtherCAT/Modbus 포트 존재만으로 완제품 드라이브가 이 제품 유형이 되는 것은 아님. 최종 scope와 marketed product core functionality 확인 필요 | ETSI record read 2026-11-20; OJ field blank |
| EN 304 627 / DEN/CYBER-EUS-0013 | Routers, internet-connected modems, switches; Comments categorisation assessed (2026-10-01) | scope에 industrial OT domain 제외 명시. 단순 Ethernet switch/port 또는 EtherCAT 통신을 라우터/모뎀/스위치 제품 기능으로 확대하지 않음 | ETSI record scope reviewed; OJ field blank |
| EN 304 621 / DEN/CYBER-EUS-009 | Network Management Systems; Comments categorisation assessed (2026-11-06) | scope에 industrial OT domain 제외 명시. DriveCM 파라미터/commissioning 도구를 NMS로 자동 분류하지 않음 | ETSI record scope reviewed; OJ field blank |
| EN 304 620 / DEN/CYBER-EUS-005 | VPN products; Comments categorisation assessed (2026-11-06); 1.0.0; 2026-11-19 remark: EC second assessment received in batches dated 2026-09-28 and 2026-10-22 | scope에 industrial OT domain 제외 명시. 원격 유지보수 VPN을 제공하는 별도 제품/솔루션과 드라이브 자체를 구분 | ETSI record scope reviewed; ETSI record read 2026-11-20; OJ field blank |
| EN 304 622 / DEN/CYBER-EUS-0010 | SIEM systems; Comments categorisation assessed (2026-11-06) | scope에 industrial OT domain 제외 명시. 서보 알람/이력만으로 SIEM 제품이 되지 않음 | ETSI record read 2026-11-20; OJ field blank |

ETSI 개별 레코드의 Harmonised Standard: Yes 메타데이터는 향후 조화표준 후보/의도에 대한 Work Programme 필드다. 해당 필드만으로 OJ 실제 게재를 증명하지 않는다. 조회한 관련 work item의 Official Journal 필드는 비어 있거나 실제 참조번호가 확인되지 않았다. 따라서 Article 27 presumption은 이 자료만으로 주장하지 않는다.

특히 EN 304 620(VPN), EN 304 621(NMS), EN 304 622(SIEM), EN 304 627(router/modem/switch)은 각 ETSI scope description에 industrial OT domain 제외 문구가 확인된다. 이 점은 산업용 OT용 CENELEC prEN 50770 work items와 구분해야 한다. CENELEC prEN 50770-1~6의 별도 진행상태는 2026-11-18 감사 기준으로 유지하며, 이번 확인에서 모든 CENELEC 레코드를 다시 읽은 것은 아니다.

### 26.3 기존 상태표에 대한 정정

- EN 304 620의 2026-09-28 “7 VR – EC assessment before EV received” 역시 과거 상태다. 2026-11-20 조회한 개별 ETSI 레코드는 Comments categorisation assessed (2026-11-06), 2026-11-19 EC second-assessment remark(2026-09-28 및 2026-10-22 코멘트 묶음 수신)를 표시한다.

- `CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md`의 2026-11-18 시점 EN 40000-1-2 개별 CEN 레코드 미확인 문장은 이번 직접 readback으로 해소됐다. 현재 둘 다 Published이며 OJ citation 필드는 No citation expected다.
- `CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md`에서 EN 304 625의 2026-09-28 “7 VR – EC assessment before EV received” 상태를 현재 상태처럼 읽으면 안 된다. 2026-11-20 조회한 ETSI 상세 레코드는 Comments categorisation assessed (2026-11-05), 그리고 2026-11-19 EC second-assessment remark를 표시한다.
- 2026-11-10 C(2026) 7861 Annex I 41개 항목/ESO 기한 감사는 그대로 유지한다. ETSI 18개 active work item의 진행상태와 M/606 41개 전체 표준의 매핑·발행·OJ 상태는 별도 계층이다.

### 26.4 후속 조사

1. ETSI 활성 work item 18개 중 미검토 8개를 모두 개별 레코드로 읽고 제품유형·scope·OT exclusion·stage·planned milestone·OJ field를 추출한다.
2. CEN/CENELEC prEN 50770-1~6의 개별 카탈로그를 다시 읽고 2026-11-20 현재 stage/forecast/OT scope를 확인한다.
3. EN 40000-1-1/-1-2는 발행 텍스트의 구매/접근 가능성 및 표준 본문 검토 가능 범위를 확인하되, 현재 확인된 No citation expected 상태를 유지한다.
4. OJ harmonised standards index 및 EUR-Lex를 재조회하여 Article 27 인용이 실제 추가되었는지 확인한다.
5. 표준 본문을 유료로 구매/열람하지 못한 경우 제목·카탈로그·요약만으로 조항별 요구사항을 추정하지 않는다.

**현재 판정:** CEN EN 40000-1-1/-1-2 Published but no CRA OJ citation expected; ETSI related standards remain work programme items with no OJ citation established in this audit; industrial OT CENELEC work items tracked separately; servo-drive product classification remains Unknown.

## 27. EU 표준화 법체계 개편 제안 — COM(2026)780 (현행법 아님)

2026-10-06 European Commission은 Regulation (EU) No 1025/2012를 폐지·대체하려는 **Proposal for a Regulation on European standardisation, COM(2026)780**을 공개했다. 제안서와 영향평가 문서가 게시되어 있으나, 이 문서는 제안 단계 자료이며 채택·발효된 현행법으로 취급하지 않는다.

- 제안 식별: COM(2026)780; SWD(2026)785, SWD(2026)786, SWD(2026)787.
- 게시일: 2026-10-06.
- 공식 출처: https://single-market-economy.ec.europa.eu/publications/proposal-regulation-european-standardisation_en
- 현재 CRA 분석에서의 의미: ESO 요청·표준 채택·위원회 평가·OJ citation 등 유럽 표준화 거버넌스의 향후 구조에 영향을 줄 수 있으므로 입법 진행을 모니터링한다. 그러나 제안이 채택되기 전에는 Regulation 1025/2012 및 현행 CRA/M/606 절차를 대체하는 법적 근거로 사용하지 않는다.
- 후속 확인: Council/Parliament procedure, amendments, adopted text, entry-into-force/application dates, transition clauses 및 기존 M/606/C(2026)7861에 대한 경과조치를 확인한다.

## 28. M/606 기한 개정과 출처 충돌 처리 — C(2026)7861 final

### 28.1 공식 Commission 근거
- European Commission CRA standardisation page (last update 2026-11-12)는 2026-11-10에 M/606 standardisation request가 amendment 되었으며, 모든 vertical standards와 일부 horizontal standards의 ESO delivery deadlines가 3개월 연장되었다고 명시한다.
- Commission Register 문서 C(2026)7861 final 및 Annex는 Brussels, 2026-11-10 날짜로 확인된다. 이 문서는 Implementing Decision C(2025)618을 개정하는 Commission Implementing Decision이다.
- 공식 페이지: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
- 공식 register document: https://ec.europa.eu/transparency/documents-register/detail?lang=en&ref=C(2026)7861
- Annex search/document record: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401

### 28.2 상충하는 2차 자료 처리
2026-11-11 기준으로 “아직 amendment가 채택되지 않았다”고 기술한 일부 2차 표준화 추적자료가 검색된다. 그러나 현재 조회 가능한 Commission의 공식 standardisation page는 2026-11-12 업데이트에서 2026-11-10 amendment 완료를 명시하고, Commission Register에는 C(2026)7861 final 문서가 존재한다. 이 충돌에서는 날짜가 더 늦고 권한 있는 공식 Commission 자료를 우선한다. 2차 추적자료의 이전 상태를 현재 법적 상태로 복사하지 않는다.

### 28.3 기한의 적용 범위
- +3개월 연장은 Commission request에 따른 ESO 표준/표준화 deliverable 납품 일정의 변경이다.
- 이 날짜를 CRA 제조자의 Article 14 신고 의무, 2027-12-11 전면 적용일, 제품의 적합성 평가 기한과 혼동하지 않는다.
- 개별 41개 항목별 이전/수정 기한은 C(2026)7861 Annex I master mapping에서 관리한다. 이 보고서 §26의 ETSI work programme 일정은 ESO 내부 단계/예정일이므로 Annex I의 공식 기한이나 OJ citation을 대체하지 않는다.
- CEN/ETSI 표준이 발행·채택되더라도 CRA Article 27 추정 적합성은 해당 표준 참조가 OJ에 실제 게재되고 제품/요구사항 범위가 맞을 때만 주장한다.

**판정:** COM(2026)780은 proposal; C(2026)7861은 2026-11-10 공식 Commission amendment. 법적 지위와 적용 대상을 구분해 추적한다.


## 29. ETSI M/606 미검토 8개 Work Item 개별 감사 — 2026-11-20

기존 재개 계획에서 미검토로 남아 있던 EN 304 617–624 관련 8개 Work Item을 ETSI Work Programme v2.3.3의 개별 상세 레코드로 확인했다. 이는 ETSI M/606 active 18개 전체의 신규 전수 재감사를 의미하지 않는다.

| ETSI EN / Work Item | 최신 상태 / 버전 | 다음 상태 예정 | scope 및 경계 |
|---|---|---|---|
| EN 304 617 / EUS-006 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2026-12-21 | Stand-alone browsers; Annex III Class I |
| EN 304 618 / EUS-007 | Comments categorisation assessed 2026-09-22 / 0.2.2 | 2026-11-23 | ICT common-use password managers |
| EN 304 619 / EUS-0018 | Comments categorisation assessed 2026-10-14 / 1.0.2 | 2026-11-23 | Anti-malware search/remove/quarantine software |
| EN 304 620 / EUS-005 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2027-01-15 | VPN products; industrial OT VPNs excluded |
| EN 304 621 / EUS-009 | Comments categorisation assessed 2026-11-06 / 1.0.5 | 2027-01-15 | NMS; industrial OT NMS excluded |
| EN 304 622 / EUS-0010 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2027-01-15 | SIEM; industrial OT SIEM excluded |
| EN 304 623 / EUS-008 | Comments categorisation assessed 2026-09-16 / 0.1.3 | 2026-12-05 | Boot managers |
| EN 304 624 / EUS-0015 | Work Item Plan 2026-11-16: Comments categorisation assessed 2026-11-05 / 1.0.0 | Next status date not shown | PKI and digital certificate issuance; CEN/TC224 and ETSI TC ESI cooperation |

- EN 304 620/621/622의 industrial OT exclusion을 확인했다. 산업용 드라이브/OT 시스템을 일반 IT 제품 표준에 자동 포함하지 않는다.
- 8개 record 모두 Harmonised Standard metadata는 Yes이나 Official Journal field는 비어 있었다. Article 27 presumption은 확인되지 않았다.
- EN 304 624는 개별 상세 페이지의 2026-10-29 approval-closure와 Work Item Plan의 2026-11-05 comment categorisation 상태가 불일치한다. 최신 Work Item Plan 값을 잠정 기준으로 사용하고 이력 확인이 필요하다.
- 상세: reports/CRA_ETSI_M606_8_ITEM_AND_OT_50770_RECONCILIATION_2026-11-20.md 및 동명 CSV.

## 30. CLC/TC 65X OT profile 재조정 — prEN 50770-1 split 및 상태 충돌

DKE 2026-10 표준화 상태 PDF에서 기존 prEN 50770-1이 firewall용 prEN 50770-1-1과 IDS/IPS용 prEN 50770-1-2로 분할된 사실을 확인했다. 기존 6개 profile 표기는 7개 deliverable로 수정한다.

| M/606 item | WIID | deliverable | scope |
|---|---:|---|---|
| 36b | 81649 | prEN 50770-1-1 | OT firewalls |
| 36b | 81649 parent; child ID 확인 필요 | prEN 50770-1-2 | OT IDS/IPS |
| 21b | 81650 | prEN 50770-2 | OT NMS |
| 25b | 81651 | prEN 50770-3 | OT physical/virtual network interfaces |
| 20b | 81652 | prEN 50770-4 | OT VPN |
| 27b | 81653 | prEN 50770-5 | OT routers/modems/switches |
| 22b | 81654 | prEN 50770-6 | OT SIEM |

DKE 2026-10 national tracker는 7개 deliverable에 Start NWI 및 Drafting prEN marker를 표시한다. BSI national records는 prEN 50770-2/-3을 PWI 및 target dates unknown으로 표시하고, LVS CLC/TC 65X 목록은 WIID 81649–81654를 In development로 표시한다. CENELEC 중앙 81649 record는 직접 재열람되어 부모 prEN 50770-1(방화벽+IDS/IPS 통합 scope), Committee stage, Citation expected, DOR/DAV 미기재를 확인했으나 -1-1/-1-2 분할 child는 표시하지 않는다. 81650–81654는 이번 pass에서 direct readback하지 못했다. 따라서 -2/-3의 정확한 중앙 stage/date는 Conflict/Unknown으로 유지한다. DKE Citation hEN 열은 비어 있고 actual OJ reference는 확인되지 않았다. 과거 Citation expected 메타데이터는 OJ citation이 아니다.

드라이브의 통신 포트, 파라미터 설정, 원격 유지보수, 알람만으로 NMS/network-interface/VPN/router/SIEM/firewall 제품으로 자동 분류하지 않는다. 정확한 core functionality와 product boundary를 확인한다.

상세: reports/CRA_ETSI_M606_8_ITEM_AND_OT_50770_RECONCILIATION_2026-11-20.md 및 CRA_M606_OT_IACS_7_VERTICAL_PROFILES_SERVO_DRIVE_BOUNDARY_2026-11-20.csv.

## 31. C(2026)7861 Annex I 일정 및 Article 2 조건

Commission CRA standardisation page(최종 업데이트 2026-11-12)는 2026-11-10 M/606 개정 및 모든 vertical standards와 일부 horizontal standards의 3개월 연장을 확인한다. Annex I의 ESO adoption deadline은 1번·15번 2026-11-30, 2–14번 2027-10-30, 16–41번 2027-01-31이다. 이는 ESO 채택기한이지 제조자 CRA 준수기한 또는 실제 OJ publication 날짜가 아니다.

Article 2는 CEN, CENELEC 또는 ETSI가 결정 수령 후 1개월 이내 개정사항을 수락하지 않는다고 통지하면 C(2026)7861이 적용을 중단하고 2025-02-03 버전 C(2025)618이 계속 적용된다고 규정한다. 1개월은 각 ESO의 실제 수령일을 기준으로 하며, 결정일 2026-11-10으로 자동 계산하지 않는다. 이번 공개자료 확인에서는 ESO별 수령일 및 acceptance/non-acceptance notice 원문을 확보하지 못했다. Recital (2)의 기존 C(2025)618 수락 사실을 2026 amendment acceptance로 오인하지 않는다.

ETSI calendar에는 2026-11-23 “GoSRSReq006-M/606 AMD 1 - examination meeting”이 예정되어 있다. 2026-11-20 현재 미래 일정이므로 acceptance 결과가 아니다. 회의 후 minutes/decision/receipt evidence를 재확인한다.

**Provenance 한계:** Commission Register entry는 확인했으나 원본 PDF bytes는 취득하지 못했다. Article 2와 Annex I 문구는 Commission certified-copy stamp가 포함된 제3자 호스팅 PDF 사본에서 확인하고 Commission 공식 페이지와 대조했다. 원본 Register PDF bytes/hash를 취득했다고 주장하지 않는다.

공식 Commission 페이지: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
Commission Register: https://ec.europa.eu/transparency/documents-register/detail?lang=en&ref=C(2026)7861
Certified-copy PDF mirror: https://www.ibf-solutions.com/fileadmin/dateidownloads/c-2026-7861-main-document-annex-cra-standards.pdf


## 32. CENELEC 중앙 project 81649 직접 readback — 부모/하위 deliverable 불일치

2026-11-20 CENELEC 중앙 record 81649를 직접 재열람했다. record는 prEN 50770-1 단일 project, firewalls 및 IDS/IPS 통합 scope, Committee stage, Citation expected, DOR/DAV 미기재로 표시한다. 반면 DKE October 2026 national status table은 이를 prEN 50770-1-1 firewalls와 prEN 50770-1-2 IDS/IPS로 분리해 표시한다. 이는 표준 scope가 바뀌었다는 결론보다 project naming/record synchronization discrepancy로 관리한다.

중앙 81650–81654 record는 이번 pass에서 direct readback에 실패했다. -2/-3은 BSI PWI 및 DKE Drafting prEN 충돌을 유지하고, -4/-5/-6은 이전 2026-11-18 central snapshot과 DKE/LVS 자료를 분리해 기록한다. Citation expected는 actual OJ citation이 아니다.

CENELEC record 81649: https://standards.cencenelec.eu/ords/f?cs=13322EAD4BB9270452A937D8259179562&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81649,25
