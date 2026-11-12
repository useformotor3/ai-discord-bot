# 서보 드라이브 CRA 제품 경계·적용성 판단 템플릿

**상태:** 제품 정보 미확정 — 결론을 내리지 않는 입력/증거 수집 템플릿  
**목적:** CRA 적용 범위와 제품 분류를 제품명이나 MCU 제조사만으로 추정하지 않고, 제품 기능·시장 제공 형태·연결성·시스템 경계에 따라 판단한다.

## 1. 법적 판단의 출발점

Regulation (EU) 2024/2847:
- Article 2(1): EU 시장에 제공되는 제품 중 의도된 목적 또는 합리적으로 예견 가능한 사용에 직접/간접 논리적 또는 물리적 데이터 연결이 포함되는 제품에 적용.
- Article 3(1): 제품 with digital elements는 소프트웨어 또는 하드웨어 제품 및 해당 remote data processing solutions를 포함한다. 별도 시장에 제공되는 SW/HW 구성요소도 포함될 수 있다.
- Article 3(2): remote data processing은 제조자 또는 제조자 책임 하에 설계·개발된 원격 데이터 처리로서, 그것이 없으면 제품 기능 중 하나를 수행할 수 없는 경우다.
- Article 3(22): 시장에 제공됨은 상업 활동 과정에서 대가 유무와 관계없이 EU 시장에 공급하는 것을 포함.
- Article 7(1): Annex III 카테고리의 core functionality를 가진 제품이 Important product로 분류된다. 다른 제품에 그런 제품을 통합했다는 사실만으로 통합된 전체 제품이 자동으로 같은 평가 절차를 적용받는 것은 아니다.
- Implementing Regulation (EU) 2025/2392 recital (2)–(5): 제품의 핵심 기능을 기술적 설명과 비교한다. 기능을 일부 포함하는 것과 그 카테고리가 제품의 핵심 기능인 것은 다르다.

공식 원문:
- Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

## 2. 제품 경계 후보 — 확인 전 가정하지 말 것

| 후보 제품/구성요소 | 확인할 질문 | 필요한 객관적 증거 | 현재 상태 |
|---|---|---|---|
| 서보 드라이브 본체 | 자체 MCU/펌웨어가 있는 하드웨어 제품인가? EU에 독립 판매/공급되는가? | 제품 카탈로그, 주문 코드, EU 판매 계약/설명서, 블록도 | UNVERIFIED |
| 임베디드 제어 펌웨어 | 본체와 함께 공급되는가, 별도 판매/라이선스되는가? | FW 릴리스/라이선스/업데이트 문서 | UNVERIFIED |
| 필드버스/이더넷 옵션 모듈 | 별도 제품으로 판매되는가, 본체 내부 옵션인가? | SKU, 데이터시트, 장착/판매 구조 | UNVERIFIED |
| 엔지니어링 PC 툴 | 별도 제품으로 시장에 제공되는 SW인가? 드라이브 기능에 필수인가? | 설치 패키지, 라이선스, 기능 명세 | UNVERIFIED |
| 모바일 앱 | 제품 기능을 제공하는지, 단순 관리 편의 기능인지? | 앱 기능/통신 흐름/제품 설명 | UNVERIFIED |
| 제조사 클라우드/원격 서비스 | 서비스 부재 시 제품의 기능 중 하나가 수행 불가능한가? 제조자 책임으로 개발됐는가? | 아키텍처, API, 장애 시 기능 영향, 계약 | UNVERIFIED |
| 모터/엔코더/센서 | 독립 판매되는 디지털 제품인가, 드라이브의 구성품인가? | SKU, 데이터시트, 인터페이스 | UNVERIFIED |
| 공장/설비 상위 시스템 | 제품에 포함되어 판매되는지, 고객 설비인지? | 공급 범위, 시스템 구성도, 계약 경계 | UNVERIFIED |

## 3. 적용 범위 입력 시트

각 항목은 실제 제품 문서로 채우고, 모르면 UNKNOWN으로 둔다.

| 입력 ID | 확인할 내용 | 기록 |
|---|---|---|
| BD-01 | 제조사/브랜드 및 EU 시장 공급 주체 | UNKNOWN |
| BD-02 | 제품명, 모델명, 주문 코드, HW revision | UNKNOWN |
| BD-03 | EU 시장에 공급되는지, 첫 시장 제공 시점 | UNKNOWN |
| BD-04 | 판매/공급 방식: 단독 제품, OEM 내장, 시스템 일부, 주문제작 | UNKNOWN |
| BD-05 | 의도된 목적 및 합리적으로 예견 가능한 사용 | UNKNOWN |
| BD-06 | 유선/무선/광/필드버스 등 물리적 연결 인터페이스 | UNKNOWN |
| BD-07 | Ethernet/IP, EtherCAT, PROFINET, Modbus TCP 등 논리적/네트워크 연결 | UNKNOWN |
| BD-08 | 간접 연결: 상위 PLC, PC 툴, 게이트웨이, 원격 서비스 경유 | UNKNOWN |
| BD-09 | 제품의 주요 기능: 모션 제어, 파라미터 설정, 네트워크 관리, 인증/접근제어 등 | UNKNOWN |
| BD-10 | 원격 데이터 처리의 존재와 기능 필수성 | UNKNOWN |
| BD-11 | 별도 판매되는 SW/HW 구성요소 및 라이선스 | UNKNOWN |
| BD-12 | 펌웨어/설정/파라미터 업데이트 경로와 서명/인증 방식 | UNKNOWN |
| BD-13 | 제품이 포함하는 보안 기능(MCU, secure element, network security 등) | UNKNOWN |
| BD-14 | Annex III/IV 카테고리와 일치할 수 있는 핵심 기능 | UNKNOWN |
| BD-15 | 다른 EU 법령 적용 및 잠재적 중복/제외 검토 | UNKNOWN |

## 4. Important Class I/II 분류 절차

1. 완제품/별도 판매 구성요소 각각의 제품 경계를 정의한다.
2. 제품의 핵심 기능을 제조사 설명서, 마케팅 자료, 기술문서와 실제 동작으로 특정한다.
3. Annex III의 카테고리 이름만 검색하지 말고 Implementing Regulation (EU) 2025/2392의 세부 기술 설명을 대조한다.
4. 단순히 특정 기능을 포함하거나 다른 제품의 카테고리 제품을 내장했다는 이유만으로 전체 제품을 그 카테고리로 분류하지 않는다.
5. MCU 자체가 Annex III Class I category 14의 security-related microcontroller 기술 설명을 충족하는지 별도로 확인한다. 보안 기능의 존재뿐 아니라 해당 기능이 MCU 자체를 넘어 다른 제품/네트워크/서비스를 보호하는 목적을 갖는지 확인한다.
6. Class II category 4 tamper-resistant microcontroller는 단순한 암호 가속/secure boot 마케팅 문구만으로 단정하지 않는다. 기술 설명과 증거를 확인한다.
7. 판단이 불명확하면 CONFLICT/UNVERIFIED로 남기고 법률 검토를 요청한다.

## 5. 제품 경계 다이어그램 작성 지침

향후 실제 제품 자료가 확보되면 아래 구성요소와 데이터 흐름을 도식화한다.

- 전력 변환부와 제어 보드
- MCU/보안 MCU/secure element
- 부트 ROM, bootloader, application firmware
- Flash/NVM, key/certificate storage
- Ethernet/fieldbus/USB/serial/service port
- encoder/feedback/sensor interface
- PC engineering tool 및 update tool
- PLC/HMI/SCADA/industrial network
- cloud/remote diagnostics (해당 시)
- firmware, configuration, parameter, log, vulnerability data 흐름

각 연결마다 프로토콜, 인증, 암호화, 무결성, 권한, 물리적 접근, 업데이트 가능 여부 및 제품 경계를 기록한다.

## 6. 판단 결과 기록 템플릿

| 필드 | 기록 |
|---|---|
| Product boundary ID | TBD |
| Product / SKU | TBD |
| Intended purpose | TBD |
| Market availability in EU | TBD |
| Physical/logical connection | TBD |
| Remote data processing | TBD |
| Core functionality | TBD |
| Potential Annex III/IV category | TBD |
| Applicable technical description | TBD |
| Evidence links and revision | TBD |
| Conclusion | UNVERIFIED |
| Reviewer/date | TBD |
| Open questions | TBD |

## 7. 현재 결론

- 서보 드라이브는 네트워크 연결, 내장 펌웨어, 디지털 제어 기능을 가질 수 있으므로 CRA 제품 경계 검토 대상 후보로 다루는 것이 합리적이다. 실제 적용 여부는 Article 2 및 제품별 사실관계를 확인해야 한다.
- 서보 드라이브라는 명칭만으로 Important Class I/II라고 단정할 근거는 없다.
- ST MCU의 보안 기능과 완제품 서보 드라이브의 분류는 별개다.
- 현재 제품 SKU, 정확한 MCU 주문 코드, 네트워크/원격 기능, 시장 공급 형태가 확인되지 않았으므로 최종 적용성/분류 결론은 UNVERIFIED다.
