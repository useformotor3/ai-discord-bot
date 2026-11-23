# LS메카피온 서보 드라이브 CRA 적용 범위 및 제품 분류 조사

- 문서 버전: v1.0
- 조사 기준일: 2026-11-24 (KST)
- 적용 법령: Regulation (EU) 2024/2847 (Cyber Resilience Act)
- 공식 해석 자료: Commission Guidance C/2026/6013, OJ C 17.11.2026
- 기술 분류 시행규정: Commission Implementing Regulation (EU) 2025/2392
- 대상 사례: LS메카피온 산업용 서보 드라이브 제품군
- 범위: CRA only. SIL 3 기능안전 평가는 본 조사 범위에서 제외한다.

> **중요한 판정 원칙:** 이 문서는 제조사 제품군 공개자료를 이용한 예비 적용성·분류 분석이다. 실제 대상 SKU, nameplate, 하드웨어/펌웨어 revision, BOM, ST MCU 전체 주문코드 및 공급·판매 경계가 확인되지 않았으므로 특정 모델의 최종 법적 분류를 확정하지 않는다. 확인되지 않은 제품 구조를 가정하지 않는다.

## 1. 요약 및 현재 판단

### 1.1 핵심 결론

1. CRA 적용 여부는 제품이 디지털 데이터를 처리·저장·전송할 수 있는지와, 의도된 목적 또는 합리적으로 예상되는 사용에 기기/네트워크와의 직접·간접 데이터 연결이 포함되는지에 따라 판단한다. 전자회로가 있다는 사실만으로 충분하지 않다.
2. LS메카피온 공개 제품군 중 iX700M은 EtherCAT 기반 다축 모듈러 서보 드라이브로 소개되어 있으므로, 해당 제품군이 EU 시장에 공급되는 실제 구성이라면 CRA Article 2(1) 데이터 연결 요건을 충족할 가능성이 높다. 다만 실제 대상 SKU·구성 및 시장 공급 사실은 별도 확인이 필요하다.
3. 서보 드라이브의 핵심 기능이 전동기의 토크·속도·위치 제어라면, 그 기능 자체는 CRA Annex III/IV에 열거된 중요·핵심 제품 범주와 일치한다고 현재 확인되지 않는다. 따라서 **완제품은 기본(Default) 제품 범주일 가능성이 가장 높다**. 이는 실제 intended purpose와 기술문서를 확인하기 전의 잠정 분석이다.
4. EtherCAT/Fieldbus 인터페이스가 제품 내부의 통신 보조 기능인지, 별도 판매되는 네트워크 인터페이스 제품인지에 따라 판단이 달라진다. Annex III Class I category 10은 물리적·가상 네트워크 인터페이스를 명시하고 Fieldbus를 예시로 든다. 그러나 인터페이스가 포함되었다는 사실만으로 통합 서보 드라이브 전체가 category 10이 되지는 않는다.
5. ST MCU가 사용된다는 사실만으로 MCU가 Annex III Class I category 14에 해당하거나, 그 MCU를 내장한 서보 드라이브가 Class I이 되는 것은 아니다. MCU 전체 주문코드와 실제 보안 기능, 별도 시장 공급 여부를 확인해야 한다.
6. Class II category 4(변조 저항성 마이크로컨트롤러)는 단순히 secure boot 또는 암호 가속기가 있다는 것만으로 성립하지 않는다. 보안기능을 가진 MCU에 더해 변조 탐지·저항·대응과 AVA_VAN 2 또는 3 수준의 설계가 요구된다.
7. EN 40000-1-1 및 EN 40000-1-2는 2026-11-19 공개된 CRA 지원 유럽표준이다. 현재 확보한 공개 자료만으로 CRA Article 27의 적합성 추정이 발생한다고 보지 않는다. OJ에 조화표준 참조가 공표되었는지 별도 확인 전까지는 용어·위험관리·수명주기 설계 참고표준으로 취급한다.

### 1.2 판정표

| 대상 | 잠정 CRA 적용성 | 잠정 분류 | 신뢰도/조건 |
|---|---|---|---|
| iX700M 통합 드라이브 제품 | 데이터 연결이 있는 실제 공급 구성이라면 적용 가능성 높음 | Default 가능성 높음 | SKU·판매 단위·intended purpose 확인 전 잠정 |
| iX700M Converter Unit | 디지털 데이터 처리/연결 및 별도 공급 여부 확인 필요 | Unknown | 단독 기능·공급 단위 미확인 |
| iX700M Drive Unit | 디지털 데이터 처리/연결 및 별도 공급 여부 확인 필요 | Unknown | 단독 기능·공급 단위 미확인 |
| 독립 판매 EtherCAT/Fieldbus 인터페이스 | 별도 제품으로 시장 공급되고 기술 설명에 부합하면 적용 가능 | Annex III Class I category 10 가능성 | 제품 경계·API/driver·network interface 역할 확인 필요 |
| 서보 드라이브 내장 ST MCU | MCU 칩 자체의 기능·시장 공급 여부에 따라 별도 분석 | Class I category 14 또는 Class II category 4 가능성 | 전체 주문코드·보안기능·tamper/AVA 증거 미확보 |
| 통합 서보 드라이브에 MCU/통신 기능이 내장된 경우 | 완제품 자체는 별도 판단 | MCU 등급 자동 승계 안 됨 | CRA Article 7(1), Guidance §§141–145 |

## 2. 법령 체계와 법적 근거

### 2.1 CRA Regulation (EU) 2024/2847

- Article 2(1): 제품의 intended purpose 또는 reasonably foreseeable use에 기기/네트워크와의 직접·간접 논리적 또는 물리적 데이터 연결이 포함되면 적용 범위에 들어간다.
- Article 3(1): 제품 디지털 요소는 소프트웨어 또는 하드웨어 제품과 그 원격 데이터 처리 솔루션을 의미하며, 별도로 시장에 제공되는 하드웨어·소프트웨어 구성품도 포함한다.
- Article 3(5)~(8): 하드웨어, 구성품, 전자정보시스템, 논리적·물리적 연결의 정의를 함께 읽어야 한다.
- Article 6: 제품은 Annex I Part I의 제품 보안 요구사항과 Part II의 제조자 취약점 처리 프로세스 요구사항을 충족해야 한다.
- Article 7(1): Annex III 제품 범주의 핵심 기능(core functionality)을 가진 제품이 중요 제품이다. 중요 제품 기능을 가진 제품이 다른 제품에 통합되었다는 사실만으로 통합 제품에 동일한 적합성평가 절차가 자동 적용되지는 않는다.
- Article 8: Annex IV 핵심 기능을 가진 제품은 critical product 범주 검토 대상이다.
- Article 13(2), 13(5): 제조자는 제품 위험평가를 수행하고 통합 구성품에 대해 실사(due diligence)를 해야 한다.
- Article 31 및 Annex VII: 시장 출시 전에 기술문서를 작성하고 필요 시 지원기간 동안 갱신해야 한다.
- Article 32: 제품 분류에 따라 적합성평가 절차가 달라진다.

공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj

### 2.2 Commission Guidance의 날짜 및 법적 지위

2026-07-27 Commission이 발표한 실무 지침의 문서 식별자는 C(2026) 6013이다. Commission 페이지는 이 안내를 2026-07-27 공개 자료로 설명하고, 해당 Communication C(2026) 6013을 연결한다. 동일한 지침이 2026-11-17 OJ C에 C/2026/6013으로 게재되었으며, 서로 다른 두 개의 지침이 아니다. 관보판은 61페이지 공식 문서다.

C/2026/6013은 Commission의 공식 해석 지침이지만 Regulation과 같은 구속력 있는 법령은 아니다. 법령과 충돌하는 경우 Regulation 원문이 우선한다. 제품 적용성 및 분류 판단에는 이 지침의 구체적 해석을 참고하되, 지침 자체를 법령 조문처럼 인용하지 않는다.

공식 자료:
- 2026-07-27 발표: https://digital-strategy.ec.europa.eu/en/news/commission-publishes-new-guidance-support-businesses-implementation-cyber-resilience-act
- OJ C/2026/6013: https://eur-lex.europa.eu/eli/C/2026/6013/oj

### 2.3 Implementing Regulation (EU) 2025/2392

2025/2392는 CRA Annex III 및 Annex IV에 열거된 중요·핵심 제품의 기술적 설명을 정한다. 따라서 Annex III/IV 제품명만 검색하는 것으로 끝내면 안 되고, 각 category의 기술적 설명과 제품의 실제 핵심 기능을 비교해야 한다.

공식 원문: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng

## 3. 서보 드라이브의 CRA 적용 범위 분석

### 3.1 디지털 데이터 연결 판단

Commission Guidance §§26–28은 단순 전기 신호와 디지털 정보 교환을 구분한다. 데이터 연결이 되려면 송신 측이 정의된 방식으로 디지털 심볼을 정보로 생성하고 수신 측이 그 정보를 해석할 수 있어야 한다. 전원 공급이나 단순 ON/OFF 트리거만으로는 데이터 연결이 성립하지 않을 수 있다.

서보 드라이브 적용 예시는 다음과 같다.

| 인터페이스/기능 | CRA 적용성 검토 |
|---|---|
| EtherCAT cyclic process data, SDO, CoE 등 | 디지털 데이터 교환이므로 Article 2(1) 판단에 중요한 증거 |
| RS-485 Modbus 또는 제조사 전용 프로토콜 | 데이터 인코딩·해석이 확인되면 데이터 연결 후보 |
| USB 파라미터 다운로드/펌웨어 업데이트 | 디지털 데이터 연결 및 업데이트 공격면 검토 |
| Ethernet 기반 설정·진단 | 네트워크 데이터 연결 및 인증·무결성 검토 |
| 펄스/방향 입력 | 펄스가 단순 속도·위치 명령인지 디지털 정보 프로토콜인지 회로·규격 확인 필요 |
| 단순 전원선, 접점 ON/OFF | 그 사실만으로 디지털 데이터 연결이라 단정하지 않음 |
| 내부 MCU와 메모리/주변회로 | 디지털 제품 여부의 중요한 사실이나 외부 연결 요건과 함께 판단 |

### 3.2 공개된 LS메카피온 제품군 자료

기존 GitHub 제품 증거 등록부에서 제조사 공개자료를 통해 확인한 제품군은 iX700M, iX7M, iX7NH, L7NHA/B, L7NHF, L7PA/B, PHOX, L7C, L7SA/B 및 GEM이다. 제품군별 입력 전압, 용량, 통신 유형 및 제품 구조가 다르므로 단일 구성으로 묶지 않는다.

iX700M은 제조사 공개자료에서 다축 모듈러 EtherCAT 통신 제품군으로 설명되고, AC 380–480 V, 4.5–75 kW 범위가 제시되어 있다. 제조사 공개 세미나 자료는 Converter Unit/Drive Unit 구조, EtherCAT IN/OUT, 유닛 간 Cross Communication(RS-485), 2nd encoder 연결을 소개한다.

다만 이는 제품군 및 공개 소개자료 수준의 사실이다. 실제 프로젝트 대상 모델, 회로 구성, 포트 옵션, 내부 통신 구조 및 보안 구현을 입증하지 않는다.

공식 자료:
- LS메카피온 드라이브 제품군: https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive
- LS메카피온 제품 매뉴얼: https://www.lsmecapion.com/bbs/board.php?bo_table=manual
- iX700M 공개 소개자료: https://sol.ls-electric.com/uploads/document/17120093352290/%5BLS%2BELECTRIC%2B%EC%98%A4%ED%94%88%EC%84%B8%EB%AF%B8%EB%82%98%5D%2B%EC%84%9C%EB%B3%B4%2B%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%2B%EC%8B%A0%EC%A0%9C%ED%92%88%2B%EC%86%8C%EA%B0%9C%2BiX7M_iX700M_LS%EB%A9%94%EC%B9%B4%ED%94%BC%EC%98%A8.pdf

### 3.3 복잡한 시스템 및 시장 공급 단위

Commission Guidance §§29–31은 여러 하드웨어·소프트웨어 요소가 함께 하나의 기능을 수행하고 단일 제품으로 시장에 제공되는 복합 시스템도 CRA 제품이 될 수 있다고 설명한다. 기존 구성품이 오래되었거나 설계 변경이 어렵다는 사실 자체는 CRA 적용 제외 근거가 아니다.

따라서 iX700M을 분석할 때 다음 공급 형태를 구분해야 한다.

1. Converter Unit과 Drive Unit을 하나의 통합 시스템으로만 공급하는지.
2. Converter Unit을 별도 주문·판매·설치할 수 있는지.
3. Drive Unit을 별도 주문·판매·교체할 수 있는지.
4. 통신 인터페이스/제어 보드가 별도 SKU로 공급되는지.
5. DriveCM 등 설정·진단 소프트웨어가 별도 라이선스·다운로드·서비스로 제공되는지.
6. 통합 다축 제품이 단일 제품으로 판매되는지, 여러 독립 제품을 조합하는 방식인지.

Guidance §145에 따르면 독립 구매·라이선스·구독 등으로 별도 시장에 제공되는 모듈은 각자 별도의 제품 디지털 요소가 될 수 있으며 각 모듈의 핵심 기능을 기준으로 분류한다. 통합 제품의 구성품으로만 제공되고 별도 공급되지 않는 경우에는 통합 제품 수준에서 핵심 기능을 판단한다.

현재 Converter Unit/Drive Unit의 실제 계약·주문·판매 경계는 Unknown이다.

## 4. 완제품 분류: Annex III/IV와 core functionality

### 4.1 핵심 기능의 의미

Guidance §139는 핵심 기능을 제품이 의도된 목적을 달성하는 데 없으면 안 되는 주된 특징과 기술 능력으로 설명한다. 제품 설명서, 홍보·판매자료, 제조자 설명 및 기술문서 등을 함께 고려한다.

Guidance §§140–142는 중요·핵심 제품의 일부 기능을 포함하거나 해당 기능을 수행할 수 있다는 이유만으로 중요·핵심 제품이 되지 않는다고 설명한다. 통합 제품 전체의 핵심 기능을 기준으로 판단한다.

### 4.2 서보 드라이브 핵심 기능의 잠정 평가

서보 드라이브의 통상적 기능은 전동기에 공급되는 전력을 제어해 토크·속도·위치를 정밀하게 제어하는 것이다. 이 기능은 현재 CRA Annex III의 열거된 제품 범주와 직접 일치한다고 확인되지 않았다.

따라서 실제 iX700M 제품의 intended purpose가 전동기 제어·구동이고, 네트워크 인터페이스/진단/업데이트 기능이 이를 지원하는 부수 기능이라면 **완제품의 잠정 분류는 Default**가 가장 합리적이다.

단, 다음 사항이 확인되면 다시 판단한다.
- 제품의 실제 핵심 기능이 네트워크 인터페이스 자체인지.
- 별도 판매되는 네트워크 인터페이스 모듈이 있는지.
- 별도 판매되는 네트워크 관리/보안 소프트웨어가 포함되는지.
- 실제 제품이 Annex IV의 보안 장치·secure element 등의 핵심 기능을 수행하는지.

### 4.3 Annex III category 10: Physical and virtual network interfaces

2025/2392 Annex I category 10은 물리적 네트워크 인터페이스를 인터페이스 드라이버 API를 통해 장치를 네트워크에 직접 연결하고, 전송 매체용 하드웨어 어댑터와 펌웨어를 갖춘 제품으로 설명한다. Fieldbus도 예시에 포함된다.

따라서 EtherCAT 포트는 category 10 기술적 검토에서 무시할 수 없다. 그러나 다음을 구분해야 한다.

- **통합 드라이브:** 주된 기능이 모터 제어이고 EtherCAT이 제어 통신 수단이라면, 통신 기능이 존재한다는 이유만으로 완제품을 category 10으로 분류하지 않는다.
- **별도 판매 인터페이스 제품:** 별도 SKU로 시장에 공급되고 그 핵심 기능이 장치와 네트워크를 연결하는 네트워크 인터페이스라면 category 10 Class I 가능성을 검토한다.
- **내부 통신 회로/보드:** 통합 제품에만 포함되는 구성품이라면 제품 경계와 핵심 기능을 통합 제품 수준에서 판단한다.

EtherCAT/RS-485의 존재만으로 제품 분류를 확정하지 않는다. 최종 판단에 필요한 driver/API, PHY, MAC, Fieldbus stack, 별도 공급 여부 및 제품 intended purpose 증거가 없다.

### 4.4 Annex III category 6/12 및 기타 범주

- Category 6 Network management systems: 네트워크에 연결된 장비의 네트워크 운영·구성을 관리하는 제품이 핵심 기능이어야 한다. 모터를 제어하는 서보 드라이브와 구별한다.
- Category 12 Routers/modems/switches: 네트워크 간 라우팅, 인터넷 연결용 모뎀, 패킷 전달 및 관리 평면을 갖는 스위치가 핵심 기능이어야 한다. EtherCAT slave/controller라는 사실만으로 라우터·스위치가 되지 않는다.
- Category 11 Operating systems: RTOS를 사용한다는 사실만으로 서보 드라이브 완제품이 운영체제가 되지 않는다. 별도 OS 제품의 시장 공급 여부와 핵심 기능을 판단한다.
- Category 13/15: 보안 기능을 가진 MCU/MPU, ASIC/FPGA 자체의 별도 분류를 검토한다. 이 구성품의 기능을 host drive에 자동 승계하지 않는다.

### 4.5 Annex IV critical products

Annex IV에는 Hardware Devices with Security Boxes, 특정 Smart meter gateways 및 Smartcards/similar devices including secure elements가 열거되어 있다. 일반 서보 드라이브의 모터 제어 기능은 이들 범주의 핵심 기능과 일치한다고 확인되지 않았다.

다만 보안 모듈이나 secure element가 별도 제품으로 공급되는 경우 해당 구성품의 독립 분류는 따로 검토한다. Annex IV 제품이 통합되어 있다는 이유만으로 서보 드라이브 전체가 critical product가 되는 것은 아니다.

## 5. ST MCU 분류와 완제품 분류의 분리

### 5.1 Annex III Class I category 14

2025/2392 Annex I category 14는 다음 조건을 포함하는 마이크로컨트롤러 제품을 설명한다.

- 중앙처리 기능을 수행하는 집적회로.
- 프로그램 가능하도록 메모리를 통합하고 일반적으로 주변장치도 포함.
- 마이크로코드 및 저수준 펌웨어 포함.
- 암호화, 인증, 보안 키 저장, 난수 생성, Trusted Execution Environment 또는 기타 하드웨어 기반 보호기능과 같은 보안 관련 기능을 제공.
- 해당 기능이 MCU 자체를 넘어 다른 제품·네트워크·서비스를 보호하기 위한 목적을 가짐. 예: secure boot chain, virtualization, secure communication interfaces.

따라서 ST라는 제조사 이름만으로 category 14를 확정할 수 없다. 전체 주문코드, 데이터시트, reference manual, 보안 매뉴얼, 실제 구성과 사용 목적을 확인해야 한다.

### 5.2 Annex III Class II category 4

Category 4는 category 14의 보안 기능을 가진 마이크로컨트롤러 중에서 추가적으로 다음을 만족하도록 설계된 제품이다.

- 변조 증거(tamper evidence), 변조 저항(tamper resistance) 또는 변조 대응(tamper response).
- Common Criteria/Common Evaluation Methodology의 AVA_VAN 2 또는 AVA_VAN 3 수준 보호 설계.

Secure boot, debug lock, AES 가속기, RNG 또는 키 저장 기능이 존재한다는 사실만으로 category 4가 되지 않는다. 변조 저항 설계와 AVA_VAN 근거가 필요하다.

### 5.3 MCU가 내장된 서보 드라이브

CRA Article 7(1)과 Guidance §§141, 152는 중요 제품 기능을 가진 구성품이 통합 제품에 들어 있다는 사실만으로 통합 제품에 같은 분류가 자동 적용되지 않는다는 원칙을 설명한다.

따라서 가능한 경우를 나눈다.

| 경우 | 분류 처리 |
|---|---|
| ST MCU가 서보 드라이브 내부 부품으로만 통합 | MCU 기능을 완제품 분류에 자동 승계하지 않음 |
| MCU 자체가 별도 시장에 제공되는 제품 | MCU의 core functionality 및 2025/2392 기술 설명으로 독립 분류 |
| 별도 판매되는 보안 MCU/secure element | 해당 부품의 category 14/4 또는 Annex IV category 3 검토 |
| MCU가 암호기능을 갖지만 제품에서 사용하지 않음 | 기능 존재와 실제 구현·활성화·검증을 구분; 공급자 자료와 제품 설정 확인 |
| secure boot를 사용하지만 tamper/AVA 증거가 없음 | category 14 가능성만 검토; category 4로 단정 금지 |

### 5.4 서보 드라이브 제조자의 ST MCU 실사(due diligence)

Guidance §§167–173은 제품 자체의 위험평가와 외부 통합 구성품 실사를 구분한다. 제조자는 ST MCU가 완제품 보안 목표를 훼손하지 않도록 제품 요구사항을 정하고, MCU 공급자 문서 및 필요 시 시험으로 확인해야 한다.

필요 증거:
- ST 전체 order code, silicon revision, package 및 datasheet.
- Reference manual, security manual, errata, PCN 및 제품 수명/지원 정보.
- Secure boot, secure debug, key storage, cryptographic accelerator, RNG, TEE 등의 기능별 지원 여부.
- 실제 보드에서 기능이 활성화되었는지, lifecycle/option byte/fuse 설정 및 debug port 상태.
- 키 생성·주입·저장·회전·폐기 절차.
- firmware image signature, update authenticity/integrity, anti-rollback 여부.
- 공급자 보안 공지, 취약점 처리 및 지원 종료 정책.
- 필요한 경우 실제 보드/펌웨어 시험 결과.

기능이 칩 데이터시트에 기재되어 있다는 것과 완제품에서 안전하게 구현·활성화되어 있다는 것은 다른 증거다.

## 6. Article 32 적합성평가 경로의 잠정 영향

| 제품 분류 | CRA Article 32의 기본 경로 |
|---|---|
| Default 제품 | Module A 내부생산관리(자체 적합성평가) 가능 |
| Important Class I | 관련 OJ 인용 조화표준·공통규격·적격 EU 인증을 적용하지 못하거나 일부만 적용하면 Module B+C 또는 Module H 등 제3자 평가 필요 |
| Important Class II | Module B+C, Module H 또는 해당되는 경우 적격 EU 사이버보안 인증 등 제3자 평가 필요 |
| Critical product | Article 8에 따른 인증 경로 또는 Article 32(3) 경로 |

Default 분류는 CRA 의무 면제를 뜻하지 않는다. Annex I 제품 보안 요구사항, 제조자 취약점 처리, 위험평가, 기술문서 및 지원기간 의무는 여전히 적용된다.

Class I도 관련 조화표준의 적용범위가 제품 핵심 기능의 모든 관련 사이버 위험을 포괄하는지 확인해야 한다. 표준 범위 밖 추가 기능 위험은 별도 통제와 문서화가 필요하다.

## 7. EN 40000 표준 현황 및 서보 드라이브 활용

### 7.1 2026-11-19 공개된 표준

CEN/CENELEC는 2026-11-19 CRA 지원 유럽표준 두 종의 공개를 발표했다.

- EN 40000-1-1: Cybersecurity requirements for products with digital elements — Part 1-1: Vocabulary.
- EN 40000-1-2: Cybersecurity requirements for products with digital elements — Part 1-2: Principles, product risk management, and lifecycle activities.

CEN/CENELEC 발표는 EN 40000-1-1이 EN 40000 시리즈의 공통 용어를 정하고, EN 40000-1-2가 제품 위험관리 및 제품 수명주기 활동의 공통 기반을 제공한다고 설명한다.

공식 발표: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/
- EN 40000-1-1:2026 CEN catalogue: DAV 2026-11-18; OJEU citation expected: No.
- EN 40000-1-2:2026 CEN catalogue: DAV 2026-11-18; OJEU citation expected: No.
- Catalogue metadata: https://standards.cencenelec.eu/ (CEN/CLC/JTC 13 published standards; references EN 40000-1-1:2026 and EN 40000-1-2:2026).

### 7.2 실무 적용

| 표준 | 서보 드라이브 프로젝트에서 활용할 영역 |
|---|---|
| EN 40000-1-1 | 자산·위협·취약점·위험·보안 통제·지원기간 등 용어와 문서의 일관성 |
| EN 40000-1-2 | 제품 위험평가, 위험처리, 보안 원칙, 설계·개발·생산·유지보수·지원 종료·폐기 수명주기 활동 |

### 7.3 조화표준 및 적합성 추정에 관한 제한

CRA Article 27의 적합성 추정은 관련 조화표준의 참조가 OJ에 공표된 범위에서 판단한다. EN이라는 표준 번호가 붙었거나 CEN/CENELEC에서 발행되었다는 사실만으로 Article 27 적합성 추정이 발생하는 것은 아니다.

이번 조사에서 CEN/CENELEC 공식 카탈로그의 각 표준 메타데이터를 직접 확인했다. EN 40000-1-1:2026과 EN 40000-1-2:2026 모두 Legal 항목의 “Citation in OJEU”에 “No citation expected for Directive 2024/2847”라고 표시한다. 따라서 단순히 OJ 참조를 아직 찾지 못한 상태가 아니라, 현재 카탈로그상 CRA에 대한 OJ 인용을 기대하지 않는 표준이다. 이 두 표준을 CRA Article 27 조화표준 적합성 추정의 근거로 사용해서는 안 된다. 대신 공통 용어와 위험관리·제품 수명주기 활동의 설계·문서화 기준으로 활용한다.

또한 두 표준의 전문을 구매·확보해 조항별 요구사항을 대조하기 전에는 세부 조항 번호나 시험방법을 추정해 작성하지 않는다.

## 8. 다른 EU 법령과의 관계

서보 드라이브는 제품의 구성과 공급 형태에 따라 Machinery Regulation (EU) 2023/1230, EMC Directive, Low Voltage Directive 등 다른 제품 법령도 함께 검토할 수 있다. 다만 다른 법령이 적용된다는 이유만으로 CRA가 자동 제외되지는 않는다.

CRA Article 2(2)~(4)는 특정 의료기기, 자동차, 항공 인증 제품, 해양 장비 등 명시적 제외를 규정한다. Article 2(5)는 다른 EU 법령이 Annex I의 일부 또는 전부 위험을 다루는 경우 Commission이 위임법령으로 제한·제외를 구체화할 수 있도록 한다. 따라서 단순히 Machinery Regulation이 적용된다는 이유만으로 CRA 적용 제외라고 결론 내리지 않는다.

공식 CRA 범위 요약: https://digital-strategy.ec.europa.eu/en/policies/cra-summary

## 9. 미확인 사실과 증거 확보 요청

다음은 제품 구조를 추정하지 않기 위해 모두 Unknown으로 유지한다.

| 우선순위 | 필요한 자료 | 확인 목적 |
|---|---|---|
| P0 | 실제 대상 전체 모델코드/nameplate/주문서 | 제품 식별 및 intended purpose |
| P0 | 실제 대상이 iX700M인지 다른 제품군인지 | 제품군 오인 방지 |
| P0 | Converter Unit/Drive Unit 별도 주문·판매·공급 여부 | PDE 시장 공급 단위 확정 |
| P0 | 통합 다축 시스템 구성도 및 제품 공급 계약 | 단일 제품/복수 제품 경계 |
| P0 | HW revision, 회로도, BOM | MCU/통신 인터페이스 및 부품 경계 |
| P0 | ST MCU 전체 주문코드와 silicon revision | Category 14/4 독립 검토 |
| P0 | EtherCAT/RS-485/USB/Ethernet/I/O별 회로·프로토콜 | 데이터 연결과 공격면 분석 |
| P0 | bootloader, firmware update package, 서명/rollback 설계 | Annex I 업데이트·무결성 요구 |
| P1 | Secure boot/debug/key/RNG/crypto 기능 설정과 시험 | 칩 기능과 완제품 구현 분리 |
| P1 | DriveCM 등 설정·진단 도구의 설치/라이선스/배포 방식 | 별도 소프트웨어 제품 여부 |
| P1 | PSIRT/취약점 신고·패치·SBOM·지원기간 정책 | Article 13 Part II |
| P1 | 제품의 예상 사용기간 및 서비스/부품 지원 정책 | Article 13(8) 지원기간 |
| P1 | EU 시장 출시 주체와 제조자/수입자/브랜드 관계 | CRA 경제운영자 책임 |

### 9.1 제조사에 요청할 최소 자료

1. 제품 nameplate 사진 및 전체 order code.
2. 실제 공급되는 Converter Unit/Drive Unit의 구성도와 판매 단위 설명.
3. HW/FW revision, BOM 및 ST MCU 주문코드.
4. 통신 포트 목록과 프로토콜/서비스 도구 연결 방식.
5. Secure boot, firmware signature, debug lock, key management 설계 증거.
6. 취약점 신고 채널, 보안 업데이트 및 지원기간 정책.

## 10. 최종 판단을 확정하는 절차

1. 실제 제품 SKU를 고정한다.
2. 시장 공급 단위(완제품/모듈/소프트웨어/MCU 구성품)를 확정한다.
3. 각 제품 단위의 intended purpose와 core functionality를 제조자 문서 및 실제 기능으로 작성한다.
4. Article 2(1) 데이터 연결 여부를 인터페이스·프로토콜 증거로 판정한다.
5. Annex III/IV 및 2025/2392 기술 설명과 대조한다.
6. 구성품이 별도 판매되는 경우 독립 분류하고, 통합 제품에 기능을 자동 승계하지 않는다.
7. Article 32 적합성평가 경로를 결정한다.
8. Annex I 요구사항과 위험평가·시험·기술문서·취약점 처리 증거를 연결한다.
9. 불확실한 사실은 Unknown으로 유지하고 근거가 확보될 때만 판정을 갱신한다.

## 11. 검증 결과와 남은 한계

### 확인 완료
- CRA Regulation 2024/2847 Article 2, 3, 6, 7, 8, 13, 31, 32 및 Annex III/IV의 주요 판단 구조.
- Commission Guidance C/2026/6013의 2026-11-17 관보 게재 사실과 core functionality, 모듈 공급 경계, 구성품 due diligence 관련 설명.
- Implementing Regulation 2025/2392의 category 10, 14, Class II category 4의 기술적 설명.
- CEN/CENELEC의 EN 40000-1-1/-1-2 2026-11-19 공개 발표.
- GitHub main의 기존 LS메카피온 제품 증거 등록부와 보고서 상태.

### 아직 확정 불가
- 실제 대상 모델과 SKU.
- iX700M Converter Unit/Drive Unit의 독립 판매 여부.
- ST MCU의 전체 주문코드와 실제 보안 기능.
- 서보 드라이브 완제품의 최종 CRA 분류.
- 별도 네트워크 인터페이스 제품의 존재 및 분류.
- EN 40000 표준의 CRA Article 27 OJ 인용 상태.
- 개별 제품의 CRA 적합성 또는 CE 적합성.

### 최종 잠정 의견
실제 EU 시장에 공급되는 통신형 LS메카피온 서보 드라이브는 CRA 적용 가능성이 높다. 제품의 주된 목적이 모터 구동·제어라면 완제품은 Default category일 가능성이 가장 높으며, 별도 판매되는 Fieldbus 인터페이스나 ST MCU는 각자의 시장 공급 경계와 핵심 기능에 따라 독립 분류해야 한다. ST MCU의 보안 기능이나 네트워크 인터페이스를 완제품 분류에 자동 승계하지 않는다.

이 문서는 제품별 증거가 확보되기 전까지 최종 적합성 선언이나 법률의견을 대체하지 않는다.

## 12. 주요 공식 출처 목록

1. Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
2. Commission Guidance C/2026/6013: https://eur-lex.europa.eu/eli/C/2026/6013/oj
3. Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng
4. Commission CRA Guidance 2026-07-27 announcement: https://digital-strategy.ec.europa.eu/en/news/commission-publishes-new-guidance-support-businesses-implementation-cyber-resilience-act
5. CEN/CENELEC EN 40000-1-1/-1-2 announcement: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/
6. Commission CRA standardisation page: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
7. LS메카피온 drive products: https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive
8. LS메카피온 manuals: https://www.lsmecapion.com/bbs/board.php?bo_table=manual


## 13. 2026-11-24 제조사 공식자료 재조사 — Converter Unit / Drive Unit 제품 구조와 공급 경계

### 13.1 제조사 자료에서 직접 확인된 구조

LS ELECTRIC Solution Square에 게시된 LS메카피온의 iX700M 신제품 소개 자료는 iX700M을 *Modular Servo Drive*로 표시하고, Converter Unit과 Drive Unit을 별도 유닛으로 구분한다. 자료에는 Power/Converter 부분과 Drive의 Power 부분이 분리되어 필요한 용량의 Drive를 다중 연결할 수 있다고 설명되어 있다. 따라서 이 제품군이 단일 일체형 드라이브가 아니라 공통 DC Bus를 사용하는 모듈형 구성이라는 점은 제조사 공개자료로 확인된다.

기능 분담은 다음과 같다.

| 유닛 | 제조사 자료에 기재된 기능 | CRA 제품경계 검토 시 의미 |
|---|---|---|
| Converter (Power) Unit | AC 380–480 V 3상 입력을 정류·평활해 DC 535–675 V로 만들고 Bus-Bar를 통해 Drive Unit에 공급. 회생제동 구동회로 내장(저항은 외부 장착). DC24V 제어전원을 Bus-Bar로 Bypass 공급 | 전력 변환·공통 DC Link 공급 기능. 단독 판매 여부는 별도 확인 필요 |
| Drive Unit | Converter에서 Bus-Bar로 전원을 공급받아 모터 구동. Dynamic brake, DC24V 제어전원, 모터브레이크 출력, BiSS 1st encoder 및 2nd universal encoder 제공 | 실제 모터 토크/속도/위치 제어의 핵심 실행 유닛으로 보이나, 개별 SKU의 상세 기능은 매뉴얼 확인 필요 |
| 유닛 간 연결 | PE 연결 Bus-Bar, DC Link Bus-Bar, DC24V, Converter-Drive 간 RS-485 Cross Communication | 내부 유닛 연결 및 제어 데이터 교환의 제조사 설명. 이 RS-485가 외부 네트워크 제품으로 별도 공급된다는 근거는 아님 |
| 외부 통신 | Drive Unit 연결부 설명에 EtherCAT IN/OUT이 기재 | 디지털 데이터 연결 가능성을 뒷받침하나, 포트/프로토콜 상세와 실제 SKU는 매뉴얼·회로 자료로 확인 필요 |

제조사 자료는 15/37/55/75 kW Converter 및 5/7.5 kW Phase 3 Converter 용량군, Drive Unit의 축수(1/2/3축)와 용량군을 각각 표로 제시한다. 자료의 Phase 일정은 제품군 라인업 안내이지 현재 모든 SKU의 재고·판매 가능 상태를 입증하는 자료로 해석하지 않는다.

### 13.2 제조사 공식 모델코드 및 독립 문서 식별

LS메카피온 공식 제품인증서 게시판에는 Converter Unit과 Drive Unit이 각각 별도 항목으로 등록되어 있고, 각 항목에 대응하는 별도 CE DoC 첨부파일이 표시된다.

**Converter Unit 공개 모델코드 예시**
- CE 문서 페이지의 코드 체계: `iX700MCV` — Converter Unit = `CV`, Input Rating = `B (480 Vac)`, Rated Wattage = `150 (15 kW)`, `370 (37 kW)`, `550 (55 kW)`, `750 (75 kW)`; 옵션은 표준(blank) 또는 사용자 지정 코드.
- 별도 KC 게시 항목에는 `iX700MCV-B-150`, `iX700MCV-B-370`, `iX700MCV-B-550`, `iX700MCV-B-750`가 각각 표시된다.

**Drive Unit 공개 모델코드 예시**
- CE 문서 페이지의 코드 체계: `iX700MD1-B-150B`. 모델 설명에서 `D1`은 1축, `D2`는 2축, `D3`는 3축을 뜻하고, `B` 입력 정격은 480 Vac, `150`은 15 kW, Encoder `B`는 BiSS-C로 설명된다. 옵션 코드는 표준(blank) 또는 사용자 지정 코드다.
- CE 게시판에는 `iX700MD1-B-075B`, `iX700MD1-B-050B`, `iX700MD2-B-045B`, `iX700MD1-B-150B`, `iX700MD1-B-220B`, `iX700MD1-B-300B`, `iX700MD1-B-370B`, `iX700MD1-B-450B`, `iX700MD1-B-550B`, `iX700MD1-B-750B` 등 용량별 Drive Unit 항목이 나뉘어 있다. 목록의 모델명·첨부파일·정격을 사용자 실제 납품 SKU로 오인하지 않는다.

이 모델코드와 별도 DoC 게시 사실은 Converter Unit과 Drive Unit이 제조자 문서에서 서로 구별되는 제품 식별·정격 단위로 관리된다는 강한 증거다. 그러나 **별도 CE DoC 또는 모델코드가 존재한다는 사실만으로 독립적인 상업 판매·별도 주문·EU 시장 공급이 확정되지는 않는다.** 가격표, 주문서, 견적서, 계약, 포장·라벨, 판매조건 또는 제조사의 명시적 독립 판매 설명은 이번 공개 조사에서 확인하지 못했다.

### 13.3 공급 경계에 대한 현재 증거 판정

| 질문 | 판정 | 근거와 한계 |
|---|---|---|
| Converter와 Drive가 기능적으로 분리된 유닛인가? | **확인** | 제조사 자료가 유닛을 명시적으로 구분하고 전력 변환·모터 구동 기능을 각각 설명 |
| 각 유닛에 별도 모델코드 체계가 있는가? | **확인** | `iX700MCV...`와 `iX700MD...` 코드 체계 |
| 각 유닛에 별도 CE DoC 게시 항목이 있는가? | **확인** | 제조사 제품인증서 게시판에 Converter Unit과 Drive Unit 항목 및 각각의 첨부 DoC가 있음 |
| 유닛을 개별 교체·설치할 수 있는가? | **일부 정황만 확인** | 모듈형/Plug-and-Play 및 다중 연결 설명은 있으나, 실제 교체 절차·제한은 매뉴얼 본문 검증 필요 |
| Converter Unit을 독립 SKU로 별도 판매하는가? | **Unknown** | 모델코드·별도 DoC는 있으나 독립 판매·주문 증거 미확보 |
| Drive Unit을 독립 SKU로 별도 판매하는가? | **Unknown** | 모델코드·별도 DoC는 있으나 독립 판매·주문 증거 미확보 |
| 두 유닛이 EU 시장에서 각각 별도 PDE로 공급되는가? | **Unknown** | EU 판매 계약·주문·포장·EU 수입자 공급단위 자료 미확보 |
| 실제 사용자 대상 제품의 SKU는 무엇인가? | **Unknown** | 공개 모델 예시는 확인했으나 nameplate/주문서와 대조되지 않음 |

### 13.4 CRA 적용성에 미치는 영향

CRA Guidance C/2026/6013의 제품·모듈 공급 경계 원칙에 따라, Converter Unit 또는 Drive Unit이 실제로 독립적으로 시장에 제공되는 제품이라면 각 유닛을 별도의 PDE로 평가할 수 있다. 반대로 통합 시스템 내부 구성품으로만 제공된다면 통합 제품 전체의 intended purpose와 core functionality를 중심으로 평가해야 한다.

현재 공개자료만으로는 어느 공급 시나리오인지 확정할 수 없다. 따라서 다음을 병렬로 유지한다.

1. **통합 시스템 시나리오:** Converter + 하나 이상의 Drive Unit이 하나의 시스템 제품으로 공급되는 경우. 시스템 전체의 데이터 연결, 핵심 기능, 업데이트·취약점 처리 책임을 평가한다.
2. **별도 유닛 공급 시나리오:** Converter 및/또는 Drive Unit이 각각 별도 주문·판매·공급되는 경우. 각 유닛의 intended purpose, 자체 디지털 데이터 연결, 독립 core functionality를 각각 평가한다.
3. **혼합 시나리오:** Converter/Drive가 별도 주문되지만 특정 시스템 구성으로 함께 판매·설치되는 경우. 각 시장 공급 단위와 조합 시스템의 책임·기술문서 경계를 계약과 실제 판매 흐름으로 결정한다.

Converter Unit의 정류·DC bus 공급 기능만으로 CRA 적용 여부를 단정할 수 없다. 유닛 자체에 디지털 데이터 처리·저장·전송 및 직접/간접 데이터 연결 기능이 있는지, Drive Unit·외부 네트워크와의 연결이 해당 유닛의 의도된 사용에 포함되는지를 회로도·인터페이스·펌웨어·매뉴얼로 확인해야 한다. Drive Unit의 EtherCAT IN/OUT 및 내부 RS-485는 데이터 연결 분석의 주요 단서이나, 별도 제품 분류를 자동 확정하지 않는다.

### 13.5 최신 제조사 문서 상태와 미확보 자료

- LS메카피온 매뉴얼 목록: `iX700M DRIVE 400[V] 매뉴얼 Ver1.4`, 게시일 2026-05-26 확인. 이번 확인은 목록 메타데이터 수준이며 PDF 본문·페이지·해시를 취득해 검증한 것은 아니다.
- LS메카피온 카탈로그 목록: iX700M 국문/영문 카탈로그 항목 확인. 첨부파일명은 `iX700M 브로셔 최종KR_251205.pdf`, `iX700M 브로셔 최종EN_251205.pdf`로 표시되고 게시판에는 2025-11-17 항목, 파일 메타데이터에는 2025-12-05 시간이 표시된다. 파일 본문 및 SHA-256은 미확보.
- LS ELECTRIC Solution Square의 2024-04-01 내부 제작 표기가 있는 iX7M/iX700M 신제품 소개 PDF에서 구조·기능·용량표를 확인했다. 이 문서는 제조사 도메인에 게시된 자료지만, 2025/2026 개정 SKU 전체를 대표한다고 가정하지 않는다.
- CE DoC PDF 링크는 제조사 게시판에 존재함을 확인했으나 이번 웹 열람에서는 파일 본문을 성공적으로 내려받지 못했다. 따라서 DoC의 서명자·적용 법령·발행일·모델 범위·기술표준은 PDF 본문 확인 전까지 별도 검증 대상으로 남긴다. DoC 게시 사실을 CRA 적합성 증거로 사용하지 않는다.

### 13.6 다음 증거 확보 우선순위

**P0 — 제품 경계 확정**
1. 실제 사용 제품 nameplate 사진과 전체 모델코드(Converter/Drive 각각).
2. 견적서·발주서·납품서·송장 또는 제조사 대리점 주문 화면에서 각 유닛의 독립 주문 가능 여부.
3. EU 공급 계약에서 제품이 단일 시스템인지 개별 유닛인지, 제조자/수입자/유통자의 역할.
4. 실제 설치 구성도와 Converter-Drive 조합, Bus-Bar 및 통신 배선도.

**P1 — 기술 구조 검증**
1. iX700M DRIVE 400[V] Ver1.4 PDF 본문 및 해시 확보, 개정 이력 확인.
2. Converter/Drive 각 유닛의 회로도·BOM·HW revision·펌웨어 범위.
3. EtherCAT IN/OUT, RS-485 Cross Communication의 프로토콜·서비스·API 및 각 유닛에서의 종단점 확인.
4. 각 유닛의 MCU 전체 주문코드, 보안 기능, 업데이트·키 관리 및 취약점 대응 책임.

**현재 결론:** 제조사 자료는 Converter Unit과 Drive Unit의 기능적·모델코드·적합성 문서상 분리를 입증한다. 그러나 실제 독립 상업 판매와 EU 시장 공급 단위는 입증하지 않는다. 따라서 제품 구조의 분리는 Confirmed, 독립 판매/시장 공급은 Unknown으로 기록한다.
