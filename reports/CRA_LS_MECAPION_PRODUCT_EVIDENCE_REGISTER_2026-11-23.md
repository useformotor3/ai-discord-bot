# LS메카피온 서보 드라이브 제품군 — CRA 제품 증거 등록부

- 기준일: 2026-11-23 (KST)
- 범위: CRA only
- 목적: 제조사 공개자료에서 확인 가능한 제품군·모델코드·문서 버전을 등록하고, 특정 제품의 CRA 분류에 필요한 미확보 증거를 분리한다.
- 주의: 제조사 제품군 페이지는 제품군 수준의 공개 사양이다. 사용자 실제 대상 SKU를 확인한 것이 아니므로 어떤 행도 실제 프로젝트 대상 모델이라고 단정하지 않는다.

## 1. 제조사 제품군 목록

LS메카피온 공식 드라이브 제품 페이지에서 다음 제품군과 기본 전기/통신 범위를 확인했다.

| 제품군 | 공식 설명 | 입력 전압 | 용량 | 통신/유형 | CRA 조사상 주의 |
|---|---|---:|---:|---|---|
| iX700M | 다축 모듈러 EtherCAT 통신 | AC 380–480 V | 4.5–75 kW | 통신형 | 다축 모듈형, 전력변환/드라이브 유닛 및 네트워크 구조를 SKU별로 확인 |
| iX7M | 다축 EtherCAT 통신 | AC 200–240 V | 0.2–1 kW | 통신형 | 다축 구조와 모델별 포트·펌웨어 확인 |
| iX7NH | 개선형 EtherCAT 통신 | AC 100–120 / 200–240 V | 0.1–15 kW | 통신형 | 제품 개정·옵션별 차이 확인 |
| L7NHA | EtherCAT 통신 200 V | AC 220–230 V | 0.1–15 kW | 통신형 | 모델별 통신·업데이트 인터페이스 확인 |
| L7NHB | EtherCAT 통신 400 V | AC 380–480 V | 1–15 kW | 통신형 | 모델별 통신·업데이트 인터페이스 확인 |
| L7NHF | EtherCAT 통신 Full-Closed | AC 220–230 V | 0.4–7.5 kW | 통신형 | Full-Closed 피드백·외부 엔코더 경계 확인 |
| L7PA | 인덱스형 펄스 200 V | AC 220–230 V | 0.1–15 kW | 펄스형 | EtherCAT 기반 제품과 동일한 통신 위협 모델로 가정하지 않음 |
| L7PB | 인덱스형 펄스 400 V | AC 380–480 V | 1–15 kW | 펄스형 | 펄스·I/O·설정 포트 및 옵션 확인 |
| PHOX | 저전압 DC 드라이브 | DC 24–80 V | 공식 표에 용량 미기재 | 통신형 | 전원 범위만으로 MCU·네트워크 기능 추정 금지 |
| L7C | 경제형 펄스 200 V | AC 220–230 V | 0.1–1 kW | 펄스형 | 경제형 제품의 FW·서비스 포트 구성 확인 |
| L7SA | 펄스 200 V | AC 220–230 V | 0.1–15 kW | 펄스형 | 통신 기능이 있는 옵션과 기본형 구분 |
| L7SB | 펄스 400 V | AC 380–480 V | 1–15 kW | 펄스형 | 통신 기능이 있는 옵션과 기본형 구분 |
| GEM | 2축 제어기, 보드형 | AC 220–230 V | 0.1–1 kW | 통신형 | 보드형 제어기인지 완제품 드라이브인지 제품 경계 확인 |

출처: LS메카피온 공식 드라이브 제품 페이지(접속일 2026-11-23): https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive

## 2. 공식적으로 확인된 모델 코드 예시 — 대상 SKU로 오인 금지

LS메카피온 제품인증서 게시물은 iX700M Drive Unit의 예시 모델 `iX700MD1-B-150B`를 제시한다. 제조사 페이지에서 확인되는 코드 설명은 다음과 같다.

- iX700M: Servo Series
- D1: 1축 Drive Unit (D2는 2축, D3는 3축)
- B: 480 Vac 입력
- 150: 15 kW
- B: BiSS-C 엔코더 유형
- 후속 옵션 필드: 공란은 standard product, 문자/숫자 등 1~7자 custom option 가능

이 코드는 제조사 공개자료에 있는 실제 모델코드 예시일 뿐, 사용자의 실제 대상 모델이라는 증거는 없다. CRA 제품 평가 전에 nameplate, 주문서/BOM, HW revision, FW version으로 실제 SKU를 확정해야 한다.

출처: LS메카피온 공식 제품인증서 페이지, 2026-04-30 게시: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888

## 3. 제조사 문서 인덱스에서 확인된 문서 버전

LS메카피온 공식 매뉴얼 목록은 다음 문서 항목을 게시한다.

- iX700M DRIVE 400[V] 매뉴얼 Ver1.4 — 2026-05-26 게시
- PEGA2 매뉴얼 Ver1.3 — 2026-04-01 게시
- 별도 Servo 카탈로그 인덱스에는 iX700M Catalogue(2025년 7월), PEGA2 Series leaflet이 등재되어 있다. 다만 iX700M 상세 게시물의 첨부파일 메타데이터에는 PDF 파일명 iX700M 브로셔 최종KR_251205.pdf 및 iX700M 브로셔 최종EN_251205.pdf, 파일 날짜 2025-12-05가 표시된다. 목록 제목의 기준 월과 첨부파일의 파일 날짜를 서로 다른 메타데이터로 보존하며, PDF 본문/개정 이력은 실제 파일을 확보해 확인하기 전까지 검증 완료로 보지 않는다.

문서 인덱스 메타데이터와 문서 본문 검증을 구분한다. iX700M Ver1.4 PDF 원문 다운로드는 이번 조사에서 성공적으로 확보하지 못했다. 따라서 그 문서의 상세 통신·보안 기능을 읽은 것처럼 인용하지 않는다.

출처: LS메카피온 공식 매뉴얼 인덱스: https://www.lsmecapion.com/bbs/board.php?bo_table=manual
출처: LS메카피온 공식 카탈로그 인덱스: https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&sca=Servo

## 4. iX700M에 대한 공개 기술 설명의 한계

LS ELECTRIC 공식 세미나 자료의 iX700M 설명은 모듈형 Converter Unit/Drive Unit 구조, EtherCAT IN/OUT, 유닛 간 Cross Communication(RS-485), 2nd encoder 연결을 설명한다. 이 자료는 제품 구조의 공개 소개자료이며, 현재 실제 대상 SKU의 상세 설계 사양서나 보안 설계 증거가 아니다.

출처: LS ELECTRIC 공식 세미나 자료(공개 소개자료): https://sol.ls-electric.com/uploads/document/17120093352290/%5BLS%2BELECTRIC%2B%EC%98%A4%ED%94%88%EC%84%B8%EB%AF%B8%EB%82%98%5D%2B%EC%84%9C%EB%B3%B4%2B%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%2B%EC%8B%A0%EC%A0%9C%ED%92%88%2B%EC%86%8C%EA%B0%9C%2BiX7M_iX700M_LS%EB%A9%94%EC%B9%B4%ED%94%BC%EC%98%A8.pdf

## 5. CRA 적용성 분석에 필요한 제품별 증거

| 증거 | 필요한 세부 자료 | CRA 분석 목적 | 현재 상태 |
|---|---|---|---|
| 제품 식별 | 정확한 full model/order code, nameplate, 옵션 코드 | 제품 경계·intended purpose 확정 | Unknown |
| 하드웨어 | HW revision, 회로도, BOM, 통신 보드/모듈 구조 | 공격면·부품/완제품 경계 | Unknown |
| MCU | ST 전체 order code, silicon revision, reference manual | Annex III Class I category 14 / Class II category 4 검토 | Unknown |
| 펌웨어 | FW version, boot ROM/bootloader, update package, signature/rollback design | Annex I Part I 취약점·업데이트·무결성 요구 평가 | Unknown |
| 통신 | EtherCAT/RS-485/USB/serial/Ethernet/I/O별 모델 지원 여부, protocol stack, trust boundary | 원격·근거리 공격 경로와 인터페이스 요구사항 평가 | Unknown |
| 유지보수 | Drive CM 등 설정/진단 툴, PC 연결 방식, 인증·권한·로그 | 제조자·서비스·사용자 인터페이스 위험평가 | Unknown |
| 암호/키 | 인증, 암호, 키 생성·저장·주입·회전·폐기, secure boot | 보안 기능의 실제 존재·사용·보호대상 확인 | Unknown |
| 취약점 처리 | PSIRT, 신고 채널, 지원기간, 패치/공지 절차, SBOM | Article 13 vulnerability handling | Unknown |
| 공급망 | MCU/통신칩/오픈소스 구성요소, SBOM, 공급자 보안자료 | 제품 위험평가와 취약점 추적 | Unknown |

## 6. 법적 판단 경계

1. EtherCAT 또는 RS-485 포트가 존재한다는 사실만으로 제품이 Annex III Class I category 10(physical/virtual network interface), category 12(router/modem/switch), 또는 다른 중요한 제품 카테고리가 되는 것은 아니다. 제품 자체의 핵심 기능과 시장 공급 형태를 확인해야 한다.
2. 별도 판매되는 네트워크 인터페이스 모듈과 이를 포함하는 host servo drive는 제품 경계를 구분해 평가한다. EN 304 625의 Fieldbus/interface 기술 범위가 존재하더라도, host drive의 core functionality를 자동으로 대체하지 않는다.
3. 산업 OT용 VPN/NMS/SIEM 표준의 scope exclusion은 해당 표준의 적용범위에 관한 기술 설명이다. 이것만으로 서보 드라이브가 CRA 자체에서 면제된다는 뜻은 아니다.
4. CE 적합성 문서가 존재하더라도 그 사실만으로 CRA Annex I 요구사항 충족, Annex III 분류, CRA Article 27 presumption을 증명하지 않는다.
5. 정확한 SKU 및 구성 자료가 확보되기 전에는 최종 제품 분류를 Unknown으로 유지한다.

## 7. 현재 결론과 다음 조치

- LS메카피온은 여러 서보 드라이브 제품군을 공급하며 전압·용량·통신 방식이 제품군마다 다르다. 따라서 'LS메카피온 서보 드라이브'를 하나의 단일 구성으로 가정하면 안 된다.
- 공개자료에서 iX700M Drive Unit의 full model code 예시를 확인했으나, 사용자 실제 대상 모델인지 확인되지 않았다.
- ST MCU 사용 사실은 사용자 제공 정보이나, 전체 부품번호는 미확보 상태다.
- 다음 P0 증거는 대상 제품의 nameplate 또는 주문서상의 전체 모델코드, HW revision, FW version, ST MCU full order code, 통신 구성도다.
- 위 증거가 확보되면 제품별 Annex III/IV category, Article 32 conformity route, Annex I technical evidence matrix를 별도 판단한다.

## 8. 카탈로그 인덱스와 첨부파일 메타데이터의 날짜 차이

- Servo 카탈로그 목록의 iX700M 항목 제목은 “2025년 7월”을 표시한다.
- 해당 iX700M 상세 게시물은 첨부파일 iX700M 브로셔 최종KR_251205.pdf 및 iX700M 브로셔 최종EN_251205.pdf를 표시하고 파일 날짜를 2025-12-05로 제공한다.
- 이는 목록 제목과 첨부파일 메타데이터의 차이다. 파일명 날짜를 공식 문서 개정일로 단정하지 않으며, 첨부 PDF 원문을 확보해 표지·개정 이력·본문을 확인하기 전까지 문서 내용은 미검증으로 유지한다.
- 출처: LS메카피온 공식 Servo 카탈로그 인덱스 https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&sca=Servo ; iX700M 상세 게시물 https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110

## 9. 2026-11-17 Commission CRA Guidance — 제품별 추가 증거 요청

Commission Guidance C/2026/6013은 2026-11-17 OJ C에 게재된 61페이지 공식 해석 지침이다. 법령과 같은 구속력은 없지만 Commission의 CRA 적용 해석이므로 제품 증거 확보와 위험평가 설계에 반영한다.

| 추가 증거 | 확인 질문 | CRA 분석 영향 | 현재 상태 |
|---|---|---|---|
| 제품/모듈 판매 경계 | Converter Unit, Drive Unit, 통합 다축 시스템을 각각 독립 판매·공급하는가? | 독립 제공 모듈은 각 core functionality로 별도 판단, 통합 구성품은 통합 제품 수준 판단 | Unknown |
| 핵심 기능 정의 | 제품의 주된 intended purpose와 실제 기술 능력은 무엇인가? | Annex III/IV category 및 Article 32 경로 | Unknown |
| 추가 기능·표준 범위 | OJ 인용 표준이 핵심 기능 외 진단/통신/원격 업데이트 위험까지 다루는가? | 표준 적용 범위 밖 잔여 위험에 별도 조치 필요 | Unknown |
| ST MCU 공급자 실사 | 전체 주문 코드, silicon revision, 보안 문서, errata, 지원기간을 확보했는가? | 통합 부품이 완제품 보안 목표를 훼손하지 않는지 입증 | Unknown |
| 보안 기능 실제 설정 | Secure boot, debug lock, key storage, update verification이 제품에서 실제 활성화됐는가? | 칩의 기능 존재와 완제품의 구현·검증 구분 | Unknown |
| 제품 수명/지원기간 | 실제 산업 설비 예상 사용기간과 사용자 기대는 얼마인가? | Article 13(8) 지원기간은 최소 5년을 자동 기본값으로 하지 않고 예상 사용기간 기준 | Unknown |
| 펌웨어 변경 기록 | 업데이트가 보안 수정인지, 기능/목적/위험을 바꾸는 변경인지? | substantial modification 및 재평가 범위 | Unknown |
| 잔여 위험 승인 | 위험이 설계·기술조치로 충분히 처리됐는가? 내부 비용/위험 선호도를 이유로 미처리했는가? | 내부 risk appetite·비용만으로 잔여 위험 정당화 불가 | Unknown |

**실무 주의:** 서보드라이브의 장기 사용을 고려하면 지원기간은 5년으로 단순 고정하지 말고 설비 수명·서비스 계약·부품 지원기간을 근거로 결정해야 한다. 이는 제품 수명이 실제로 몇 년인지 확인하기 전의 확정 기간이 아니라 증거 확보 요구다.

**공식 근거:** Commission Guidance C/2026/6013, §§8, 108, 122~127, 141~151, 156~173, https://eur-lex.europa.eu/eli/C/2026/6013/oj

## 10. LS ELECTRIC Solution Square 최신 매뉴얼 인덱스 교차검증 (2026-11-23)

| 제품 | LS메카피온 인덱스 | Solution Square 인덱스 | 현재 해석 |
|---|---|---|---|
| iX700M | Ver1.4, 게시 2026-05-26 | 사용 설명서 update 2026-09-16, 검색 결과에서 버전/파일명 미확인 | 더 늦은 update date는 확인. Ver1.5 또는 Ver1.4 개정본으로 단정 금지 |
| PEGA2 | Ver1.3, 게시 2026-04-01; 첨부 PEGA2_KOR_Ver1.3_260826.pdf, DATE 2026-08-28 | PEGA2 User Manual, update 2026-09-23; PEGA2_ENG_Ver1.3_260831.pdf, English, 6.0 MB | Ver1.3 영문 파일 메타데이터 확인. 한국어 파일과 동일 개정 여부는 hash/본문 비교 필요 |

**Solution Square PEGA2 문서 목차 메타데이터:** Product Configuration; Wiring and Connection; EtherCAT Communication; CiA402 Drive Profile; Drive Application Functions; Safety Functions; Tuning; Procedure Function; Indexing Position operation; Object Dictionary; Maintenance and Inspection; Modbus-RTU Communication Protocol; Test Drive; Appendix.

**증거 한계**
- Solution Square 목록의 update date는 문서 목록/게시 정보다. iX700M의 정확한 파일명·버전·PDF 표지/개정 이력을 아직 확보하지 못했다.
- PEGA2 파일명과 update date를 확인했으나 PDF 본문 bytes·SHA-256·페이지별 내용은 아직 검증하지 않았다.
- Safety Functions 목차는 기능이 안전 관련 장으로 설명된다는 사실만 의미한다. CRA cybersecurity 또는 SIL 적합성의 증거가 아니다.
- 통신 프로토콜 목차는 인터페이스 조사 출발점이며 인증·암호화·업데이트 무결성 등 보안기능 구현의 증거로 간주하지 않는다.

**공식 출처**
- LS ELECTRIC Solution Square Motion & Servo: https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4
- LS ELECTRIC PEGA2 User Manual detail: https://sol.ls-electric.com/us/en/product/document/32720
- LS메카피온 PEGA2 Ver1.3 detail: https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651
- LS메카피온 manual index: https://lsmecapion.com/bbs/board.php?bo_table=manual


## 11. 2026-11-23 CRA 표준 후보 교차검증 — EN 304 625

| 표준 후보 | ETSI 공식 work item 상태 | 표준 목적/범위 | iX700M 적용 판단 |
|---|---|---|---|
| EN 304 625 (DEN/CYBER-EUS-0017) | 2026-11-19 이후 “Draft Review after PE”; candidate for harmonisation | 물리적·가상 네트워크 인터페이스에 대한 CRA Annex I Part 1 사이버보안 요구 및 평가기준 | Unknown — 제품 핵심 기능, 제품 경계, 최종 표준 scope 및 OJ 인용 여부 미확정 |

**적용성 판단 주의**
- EtherCAT/RS-485/USB/Ethernet 포트의 존재만으로 서보드라이브 전체가 네트워크 인터페이스 제품으로 분류되거나 이 표준이 자동 적용된다고 보지 않는다.
- 독립 판매되는 인터페이스 제품인지, 드라이브 내부 통신 인터페이스인지, host drive의 핵심 기능과 어떤 관계인지 확인한다.
- ETSI work item 상태는 표준 개발 상태이며, 발행·OJ citation·CRA Article 27 적합성 추정의 증거가 아니다.

**출처:** ETSI Work Programme EN 304 625 (DEN/CYBER-EUS-0017): https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=TRUE&WKI_ID=74860&butExpertSearch=Search&curItemNr=10&includeNonActiveTB=FALSE&includeSubProjectCode=FALSE&optDisplay=10&qCLUSTER_BOOLEAN=OR&qETSI_ALL=&qFREQUENCIES_BOOLEAN=OR&qINCLUDE_MOVED_ON=&qINCLUDE_SUB_TB=True&qKEYWORD_BOOLEAN=OR&qMandate_List=%27M%2F606%27&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qSTOPPING_OUTDATED=&qSTOP_FLG=N&titleType=all&totalNrItems=18

## 12. 2026-11-23 — M/606 개정 결정 C(2026) 7861의 iX700M 조사 영향

| 구분 | 개정 후 ESO 일정(교차확인) | iX700M 조사상 의미 |
|---|---:|---|
| Item 1: 위험기반 보안 설계·개발·생산 | 2026-11-30 | 수평 프로세스 표준 일정; 제품 분류 아님 |
| Item 15: 취약점 처리 | 2026-11-30 | 취약점 처리 프로세스 표준 일정; 제조사 의무 자체의 유예 아님 |
| Items 16–41: 제품별 vertical | 2027-01-31 | 해당 제품 범주 표준 후보 일정; iX700M이 어느 범주인지 별도 판정 |
| Items 2–14: 나머지 horizontal | 2027-10-30 (변경 없음) | 일반 제품 속성 요구 표준 일정 |

**법적 상태 주의**
- Commission Implementing Decision C(2026) 7861 (10.11.2026) Article 2는 CEN/CENELEC/ETSI 중 하나라도 결정 수령일부터 1개월 내 개정안을 수락하지 않는다고 통지하면 개정 결정이 적용 중단되고 2025-02-03 버전이 계속 적용된다고 규정한다.
- 결정일과 ESO별 실제 수령일은 동일하다고 확인되지 않았다. receipt date 및 non-acceptance notice가 확보되지 않아 기산일·만료일·최종 효력을 단정하지 않는다.
- 상세 날짜는 Commission 공식 개요와 독립 표준화 추적자료로 교차확인했으나, 확보된 결정문 PDF에는 Annex 세부 일정 표가 포함되어 있지 않다. 따라서 이 등록부에서는 날짜를 교차확인 값으로 분류하고 Annex 원본 확보 후 재검증한다.
- 이 deliverable 일정은 ESO의 표준화 일정이지 제조사 CRA 이행기한이나 OJ 인용일이 아니다. CRA Article 27 적합성 추정은 OJ 인용 범위에서만 판단한다.

**공식 1차 출처**
- Commission Implementing Decision C(2026) 7861 final: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_0/de00000001090398
- Commission CRA standardisation page: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation

**세부 날짜 교차확인(2차 출처)**
- https://shieldbook.ppftec.com/guides/cra-harmonised-standards
- https://craevidence.com/cra-compliance/harmonised-standards-status

**적용성:** iX700M에 대한 제품별 표준 선택, Annex III/IV 등급 및 conformity assessment route는 실제 SKU·core functionality·판매 경계·최종 표준 scope 증거가 확보되기 전까지 Unknown.
