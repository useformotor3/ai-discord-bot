# CRA 서보 드라이브 적용성·제품 분류 및 P0 증거 intake 기준 (2026-11-18)

## 목적과 현재 판정
본 문서는 제품별 적합성 판정이 아니라, 특정 모델의 CRA 적용성·제품군 분류에 필요한 사실을 수집하고 증거를 정리하는 기준이다. 모델명, 사용설명서, 통신구조 등 제품 자료가 아직 없으므로 현재 결과는 **Unknown / 판정 보류**다. 일반 서보 드라이브라는 제품명만으로 CRA 적용/제외 또는 Annex III/IV 분류를 확정하지 않는다.

## 1. 판정 순서
1. 시장에 제공되는 제품 단위를 고정한다: 드라이브 완제품, 별도 판매 옵션 카드/통신 모듈, 펌웨어/엔지니어링 소프트웨어, 원격 데이터 처리 서비스.
2. 제조사 문서의 intended purpose와 reasonably foreseeable use를 확인한다.
3. 제품의 목적 또는 합리적으로 예상 가능한 사용에 장치/네트워크와의 직접·간접 논리적/물리적 데이터 연결이 포함되는지 CRA Article 2(1)로 평가한다.
4. Article 2(2)–(7)의 제외 및 특례를 개별 확인한다. 다른 EU 법령이 적용된다는 사실만으로 자동 제외하지 말고 Article 2(5) 조건 및 적용 가능한 위임법령을 확인한다.
5. Annex III/IV와 Commission Implementing Regulation (EU) 2025/2392의 기술 설명을 제품 전체의 core functionality에 대조한다.
6. 분류 후 Article 32 적합성평가 경로를 판단한다. 자료가 부족하면 결론을 보류하고 필요한 사실을 명시한다.

## 2. 적용성 intake 매트릭스

| 질문 | 근거 | 필요한 증거 | 현재 상태 |
|---|---|---|---|
| 제품 범위 | CRA Art. 2(1), Art. 3(1)–(2) | 제품 경계, 별도 판매 여부, 하드웨어/소프트웨어/원격처리 구성 | Unknown |
| 연결성 | Art. 2(1) | 포트/프로토콜/네트워크 토폴로지, 제어·모니터링·서비스·업데이트 연결 | Unknown |
| 원격 데이터 처리 | Art. 3(2) | 제조사 책임으로 설계·개발된 원격처리 서비스인지, 부재 시 제품 기능이 막히는지 | Unknown |
| 제외·특례 | Art. 2(2)–(7) 및 관련 위임법령 | 의료/IVD/차량/항공/해양 등 적용 법령, 방산·기밀 목적, 동일 규격 교체부품 여부 | Unknown |
| 제조사/경제운영자 | Art. 3(12)–(17) | 상표·판매 주체, OEM/ODM/private label 관계, EU 수입자/대리인 | Unknown |
| 시장 시점 | Arts. 69–71, Art. 14 | EU 최초 시장 제공일, 기존 판매 여부, 실질적 변경, 사고/취약점 보고 준비 | Unknown |

연결 포트가 있다는 사실만으로 제품군 분류를 결정하지 않는다. 인터넷 연결이 없어도 intended purpose/reasonably foreseeable use에 장치 또는 네트워크와의 직접·간접 데이터 연결이 포함되면 Article 2(1) 검토가 필요하다.

## 3. Annex III/IV 분류 스크리닝

| CRA 제품군 | 핵심 기술 설명 | 드라이브에서 확인할 사실 | 안전한 1차 판단 |
|---|---|---|---|
| Annex III Class I #10 물리/가상 네트워크 인터페이스 | 장치를 네트워크에 직접/간접 연결하는 인터페이스 제품 | 별도 판매되는 NIC/Fieldbus adapter인지, 인터페이스 자체가 제품의 핵심 기능인지 | Ethernet/Fieldbus 포트 내장만으로 드라이브 전체를 자동 분류하지 않는다 |
| Annex III Class I #12 라우터/인터넷 모뎀/스위치 | 네트워크 간 경로 선택 또는 packet forwarding 및 관리 plane | routing protocol, 서로 다른 네트워크 간 경로 선택, managed switching이 핵심 기능인지 | IP 설정, packet filter, 진단 로그만으로 라우터/스위치라 단정하지 않는다 |
| Annex III Class I #6 네트워크 관리 시스템 | 네트워크 관리 제품 | 다수 장비/네트워크의 구성·감시·정책·운영을 관리하는 독립 제품인지 | 단일 드라이브 파라미터 설정/상태 모니터링은 자동 포함 근거가 아니다 |
| Annex III Class I #11 운영체제 | 하드웨어 추상화, 소프트웨어 실행·자원관리 | OS/RTOS가 별도 시장 제공되는 제품인지, 제품 전체의 핵심 기능인지 | RTOS를 사용한다는 사실만으로 완제품 드라이브가 OS 제품이 되지 않는다 |
| Annex III Class I #1 ID/PAM | 인증·권한·계정 수명주기 관리 시스템 | 제품 자체가 인증/권한/PAM 시스템인지 | 드라이브 로그인 기능만으로 자동 분류하지 않는다 |
| Annex III Class II #2 방화벽/IDS/IPS | 방화벽 또는 침입 탐지·방지 제품 | 보안 경계 제품으로 트래픽 정책 집행/침입 탐지가 주 기능인지 | 제한적 ACL/통신 필터링/로그만으로 자동 분류하지 않는다 |
| Annex IV | security box, smart-meter gateway/advanced security device, smartcard/secure element 등 | 변조방지 보안 외함, 특정 암호처리, 스마트미터 게이트웨이, secure element가 핵심 기능인지 | 산업용 드라이브라는 이유만으로 critical 제품이라 판단하지 않는다 |

### 해석 안전장치
- CRA Article 7(1), 8(1)은 Annex III/IV 제품군의 core functionality를 기준으로 한다.
- Regulation (EU) 2025/2392 recital (4)–(6)은 부수 기능/통합 구성요소와 제품 전체의 핵심 기능을 구분한다. listed 기능을 일부 수행할 수 있다는 사실만으로 제품 전체가 해당 카테고리가 되는 것은 아니다. 반대로 다른 기능이 추가되었다고 해서 실제 core functionality가 listed category인 사실이 사라지는 것도 아니다.
- 완제품, 별도 판매 구성품, 옵션 모듈, 소프트웨어 제품의 경계를 각각 기록한다.
- Annex III/IV 비해당과 CRA 비적용은 별개다. listed category가 아니어도 Article 2 적용 제품이면 CRA 기본 요구사항 검토가 필요하다.

## 4. P0 제출 자료 체크리스트

### A. 제품 식별·시장 경계
- [ ] 제조사 법인명, EU 제조사/수입자/공인대리인 역할
- [ ] 정확한 제품명·모델·형식·HW revision·펌웨어 버전
- [ ] 데이터시트, 카탈로그, 명판/주문 코드/옵션 코드
- [ ] 설치·사용·서비스 매뉴얼 및 제조사 intended purpose 문구
- [ ] 드라이브, 모터, 엔코더, 통신 옵션, 엔지니어링 툴, 게이트웨이, 클라우드 서비스 구성표
- [ ] 각 구성품의 별도 판매 여부, 상표, OEM/ODM/private label 관계
- [ ] EU 시장 최초 제공 예정일, 기존 판매 여부, 실질적 변경 이력

### B. 연결성·원격처리
- [ ] 물리/무선 포트 목록 및 하드웨어 블록도
- [ ] 실제 지원 프로토콜(Ethernet/IP, EtherCAT, PROFINET, Modbus, CAN/CANopen, USB, RS-232/485, Wi-Fi/Bluetooth 등)
- [ ] 인터페이스별 목적(제어, 모니터링, 파라미터, 업데이트, 진단, 서비스)
- [ ] 네트워크 토폴로지, 통신 방향, 서비스/포트, 인증·암호화 방식
- [ ] 인터넷/클라우드/원격 유지보수 유무와 데이터 흐름
- [ ] 제조사 책임 원격처리 서비스 및 서비스 중단 시 기능 영향
- [ ] 디버그/JTAG/UART/USB/서비스 포트 접근 경로
- [ ] 라우팅·스위칭·방화벽·IDS/IPS·네트워크 관리 기능의 실제 구현

### C. 기능·분류 경계
- [ ] 제품의 주 기능 및 핵심 기능에 대한 제조사 문서
- [ ] 기능 블록도, OS/RTOS·부트로더·소프트웨어 모듈 구조
- [ ] 보안 기능이 부수 기능인지, 별도 판매/사용되는 핵심 기능인지
- [ ] Annex III/IV 및 2025/2392 기술 설명과 대조한 근거
- [ ] 반대 해석, 경계 사례, 추가 확인 질문, 검토자 기록

### D. 보안 설계·공급망·시험
- [ ] 위협 모델, 자산/인터페이스 목록, 공격 표면, 위험평가 및 잔여 위험
- [ ] 인증·권한·계정·기본 암호·서비스 계정·권한 분리
- [ ] 보안 부팅, 펌웨어 서명/검증, secure update/rollback 보호
- [ ] 통신 보호, 키/인증서 생성·저장·교체·폐기
- [ ] 로그/감사 이벤트, 시간 동기, 저장·삭제 정책
- [ ] 취약점 접수·분류·조치·공개 프로세스, PSIRT 연락처
- [ ] 지원기간 근거, 보안 업데이트 정책, 단종/지원 종료 정책
- [ ] BOM/SBOM, 직접·전이 의존성, 공급자·버전·취약점 관리
- [ ] SAST/DAST/SCA, fuzzing, protocol robustness, penetration test 계획/결과
- [ ] 업데이트 무결성·실패 복구·롤백·전원 차단 시험
- [ ] 요구사항-설계통제-시험절차-결과-제품 버전 추적 링크
- [ ] Annex VII 기술문서, Annex II 사용자 정보, DoC 초안 및 적합성평가 근거

## 5. 제출 최소 패키지
1. 정확한 모델 데이터시트
2. 설치/사용설명서 및 서비스 매뉴얼
3. 하드웨어 블록도 또는 통신 인터페이스 설명
4. 네트워크/원격접속 구성도(없다면 제조사 확인서)
5. 펌웨어/소프트웨어 구성 및 업데이트 설명
6. BOM/SBOM 또는 공급망 구성요소 목록
7. 제조사·제품 판매 단위·EU 출시 예정일

자료 미제공은 Not provided, 검증 전 구두 진술은 Unverified statement로 기록한다. 원본 문서·버전·발행일·페이지/절을 확인하기 전에는 Verified로 바꾸지 않는다.

## 6. 증거 상태 코드
| 상태 | 의미 |
|---|---|
| Unknown | 판단할 자료 없음(기본값) |
| Not provided | 요청했으나 미제공; 요청일 기록 |
| Evidence received | 수령했으나 검토 전 |
| Verified | 원본·관련성·정합성 검증 및 독립 검토 완료 |
| Not applicable | 제품 경계상 비적용; 근거와 반대 해석 기록 필수 |
| Gap identified | 요구 대비 설계/증거 결손; 위험·조치·책임자·기한 기록 |
| Implemented, unverified | 구현 자료는 있으나 시험 미완료 |
| Tested, pass/fail | 특정 버전·환경·기준에서 시험 결과 확인 |

문서가 존재한다는 이유만으로 Pass 처리하지 않는다. 설계 구현, 시험 결과, 제품 버전, 요구사항 적용 범위가 연결되어야 한다.

## 7. 다음 단계
1. P0 패키지 수집 후 제품 경계와 intended purpose 확정.
2. Article 2 적용성·제외 검토 및 독립 검토.
3. Annex III/IV 및 2025/2392 core functionality 분류 근거 작성.
4. 분류 결과에 따른 Article 32 conformity assessment route 검토.
5. EVD-01~EVD-16에 모델별 증거·설계통제·시험 연결.
6. EN 40000 및 OT 표준 정식 전문 확보 후 clause-level redline.

## 8. 공식 법령·출처
- Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
- Commission CRA summary (설명자료; 법령 원문 우선): https://digital-strategy.ec.europa.eu/en/policies/cra-summary
- Commission CRA standardisation: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation

## 한계
이 문서는 제품군 intake/스크리닝 기준이지 개별 모델의 법률 의견서·적합성 선언이 아니다. 제품 자료가 없으므로 CRA 적용성 및 Annex III/IV 분류는 미판정이며 EVD-01~EVD-16 상태는 Unknown / evidence pending으로 유지한다.

## 10. 법령 원문 재대조 보완 — 2025/2392 기술 설명과 Annex IV 절차

2026-11-18 EUR-Lex 공식 OJ 본문을 다시 대조했다. Commission Implementing Regulation (EU) 2025/2392는 2025-12-01 OJ L에 게재되어 현재 시행 중이다. 특히 recital (2)–(6), Annex I, Annex II를 분류 판단의 직접 근거로 사용한다.

### 핵심 보완
- **Annex III/IV 분류는 제품 전체의 core functionality**로 결정한다. 통합 구성요소가 별도 Annex III/IV 제품군 기술 설명에 해당하더라도, 그 구성요소를 포함한 완제품 전체가 그 제품군의 core functionality를 갖는 것은 자동으로 아니다(recital (3), (5)).
- 반대로 다른 부수 기능이 함께 있더라도 제품 전체가 listed category의 core functionality를 가지면 분류에서 벗어나지 않는다(recital (4)).
- 물리/가상 네트워크 인터페이스(Class I #10)의 공식 기술 설명은 드라이버 API를 통해 장치를 네트워크에 직접 연결하는 인터페이스 제품을 대상으로 하며, 물리 제품은 통상 데이터링크/물리 계층의 어댑터와 펌웨어를 포함한다. 유선·무선 NIC, controller, adapter 및 독립 가상 NIC 등이 예시다(2025/2392 Annex I #10). 따라서 드라이브 내부의 네트워크 기능 블록과 별도 시장에 제공되는 인터페이스 제품을 제품 경계와 core functionality 기준으로 구분한다.
- 라우터는 서로 다른 네트워크 사이에서 routing protocol/algorithm으로 경로를 선택해 데이터 흐름을 제어하는 제품이다. 스위치는 packet forwarding과 management plane을 제공하는 제품이다(Annex I #12). 단순 IP 설정/필터/로그와는 기술적으로 구분한다.
- 운영체제 기술 설명은 하드웨어 추상화 및 소프트웨어 실행 통제를 제공하는 제품이며 RTOS도 예시로 포함한다(Annex I #11). 그러나 RTOS가 사용된다는 사실만으로 드라이브 완제품의 core functionality가 OS가 되는 것은 아니다.
- **Annex IV의 critical category 해당 여부와 인증 의무는 구분**한다. Article 8(1)은 Annex IV category 중 Commission delegated act로 특정된 제품에 대해, 적용 가능한 유럽 사이버보안 인증 scheme이 채택·가용한 경우 assurance level ‘substantial’ 이상의 인증을 요구할 수 있도록 한다. Annex IV라는 명칭만으로 모든 해당 제품에 동일 인증 의무가 자동 발생한다고 쓰지 않는다. Article 8(1) 및 Article 32(3) 등 구체 절차를 제품 범위와 시행 중인 delegated act에 대조한다.
- 중요/핵심 제품 여부와 무관하게 모든 CRA 적용 제품은 Article 6 및 Annex I의 본질적 사이버보안 요구사항을 검토해야 하며, Article 13(2)–(3)의 위험평가·비례성·시험/assurance 설명을 수행해야 한다(2025/2392 recital (6)).

### 공식 근거
- Regulation (EU) 2024/2847, Articles 2, 3, 6, 7, 8, 13, 32; Annexes III–IV: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Implementing Regulation (EU) 2025/2392, recital (2)–(6), Article 2, Annex I #1/#6/#10/#11/#12, Annex II: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng

이 보완에도 제품 모델·판매 단위·매뉴얼·통신 구조가 없는 현 상태의 개별 모델 분류는 **Unknown**으로 유지한다.
