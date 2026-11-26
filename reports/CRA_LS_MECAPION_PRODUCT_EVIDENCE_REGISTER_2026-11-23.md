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

## 13. 2026-11-23 최신 공개자료 재점검

### 13.1 ETSI EN 304 625

공식 ETSI Work Item DEN/CYBER-EUS-0017은 2026-11-21 갱신 화면에서 EN 304 625 V1.0.0을 `Draft Review after PE (2026-11-19)`로 표시한다. CRA M/606 연계 및 candidate for harmonisation으로 분류되어 있으나, 이는 최종 발행 또는 OJ 인용을 뜻하지 않는다. EtherCAT 인터페이스 존재만으로 해당 표준 적용성이나 CRA class를 확정하지 않는다.

- 공식 Work Item: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74860
- 2026-11-23 현재 OJ 인용/Article 27 presumption: 이 조사에서 확인되지 않음.

### 13.2 M/606 AMD 1 / C(2026)7861

ETSI 달력에는 2026-11-23 GoSRSReq006-M/606 AMD 1 examination meeting 일정이 게시되어 있다. 회의 결과·회의록은 확보하지 못했다. ESO별 C(2026)7861 실제 수령일과 Article 2 비수락 통지 여부도 Unknown이다. 결정일을 수령일로 간주하거나 2026-12-10을 자동 만료일로 계산하지 않는다.

| 항목 | 상태 |
|---|---|
| 회의 일정 게시 | Confirmed |
| 회의 개최·결과·회의록 | Unknown |
| CEN/CENELEC/ETSI 수령일 | Unknown |
| Article 2 비수락 통지 | Unknown |
| 결정 최종 적용 상태 | Unknown |

- ETSI calendar: https://portal.etsi.org/tb.aspx?TBID=287&subTB=287
- C(2026)7861: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_0/de00000001090398

### 13.3 M/606 목표일

기존 교차확인값: Items 1 및 15는 2026-11-30, Items 16–41은 2027-01-31, Items 2–14는 2027-10-30. 공식 결정 PDF의 Annex 표 원본은 아직 확보되지 않았으므로, 이 세부 날짜는 교차확인값으로 표시한다. Commission 페이지는 일부 horizontal 및 모든 vertical deliverable의 3개월 연장을 설명한다: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation

이 목표일은 ESO 표준화 일정이며 제조사 CRA 적용기한이 아니다. OJ 공표 전 적합성 추정을 주장하지 않는다.

### 13.4 iX700M 매뉴얼 인덱스 재확인

- LS메카피온 iX700M DRIVE 400[V] Ver1.4: 2026-05-26 목록 게시.
- Solution Square iX700M 사용 설명서: 2026-09-16 목록 갱신.
- PEGA2 Ver1.3: LS메카피온 2026-04-01 / Solution Square 2026-08-28 목록 항목.

PDF 본문, 파일명/revision equivalence, SHA-256은 미확보다. 목록 날짜만으로 더 최신 revision을 추정하지 않는다. 보안기능의 유무도 PDF와 설계자료 확인 전에는 Unknown으로 유지한다.

공식 인덱스: https://www.lsmecapion.com/bbs/board.php?bo_table=manual

### 13.5 운영 자동화

CRA schedule Run #2546 (ID 45155788066)은 success. 조사·요약·검증 guard·checkpoint pruning 단계도 success였으나 artifact는 없었다. 이는 실행 성공이지 조사 결과의 법적 정확성 검증 완료를 의미하지 않는다. 운영 workflow/API cadence는 변경하지 않았다.

- Run: https://github.com/useformotor3/ai-discord-bot/actions/runs/45155788066

### 13.6 제품별 판정의 보류 사항

정확한 iX700M SKU/nameplate, Converter/Drive Unit 공급·판매 경계, HW/FW revision, BOM, ST MCU 전체 order code 및 보안 설정이 확보되기 전까지 제품별 CRA 분류·Annex III 등급·적합성 평가 경로는 Unknown이다.

## 14. C(2026)7861 Annex I — 공식 별첨 원문 확보 (2026-11-23)

### 14.1 1차 자료

별도 Annex PDF를 European Commission document register에서 직접 확보했다:
https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401

문서명: C(2026) 7861 final — ANNEX, 2026-11-10. Annex I 제목은 “List of new European Standards to be drafted”이며, 기한 열은 “Deadline for the adoption by the ESOs”로 표시한다.

### 14.2 공식 원문에서 확인한 날짜

| Item | ESO 채택 목표일 |
|---|---:|
| 1 | 2026-11-30 |
| 2–14 | 2027-10-30 |
| 15 | 2026-11-30 |
| 16–41 | 2027-01-31 |

주요 서보/MCU 관련 항목:
- Item 25: physical and virtual network interfaces.
- Item 28: microprocessors with security-related functionalities.
- Item 29: microcontrollers with security-related functionalities.
- Item 37: tamper-resistant microprocessors.
- Item 38: tamper-resistant microcontrollers.

이는 ESO 표준 채택 목표일이지 제조사 CRA 준수기한이 아니다. 표준 채택과 OJ 인용도 구분한다. CRA Article 27 적합성 추정은 OJ 공표된 표준 참조의 범위에 따라 판단한다.

### 14.3 앞선 증거 수준 표기의 정정·승격

보고서 §51~§52는 Annex 원문 미확보 당시 세부 날짜를 교차확인값으로 표시했다. 이번 공식 Annex 별첨 확보로 일정 근거를 1차 자료 직접 확인으로 상향한다. 이전 스냅샷은 과거 상태 기록으로 보존하되, 현재 일정 인용은 이 §14와 보고서 §53을 기준으로 한다.

ESO별 C(2026)7861 실제 수령일과 Article 2 비수락 통지는 여전히 Unknown. Annex 일정으로 결정의 최종 적용 상태를 추정하지 않는다.


## 15. 2026-11-24 — CRA 적용 범위 및 제품 분류 정밀 분석

### 15.1 조사 기준과 공식 근거
- Regulation (EU) 2024/2847 Article 2(1), Article 3(1), (5)~(8), Articles 6–8, 13, 31, 32 및 Annex III/IV.
- Commission Guidance C/2026/6013, OJ C 17.11.2026, 61 pages. 2026-07-27 Commission announcement와 구별하고 최신 관보 지침을 해석 기준으로 사용.
- Commission Implementing Regulation (EU) 2025/2392 Annex I category 10, 14, Class II category 4 및 Annex II critical products.
- CEN/CENELEC 2026-11-19 EN 40000-1-1 및 EN 40000-1-2 publication announcement.

### 15.2 제품별 잠정 판정
| 대상 | 현재 판정 | 보류 근거 |
|---|---|---|
| 통신형 서보 드라이브(예: iX700M 제품군) | 실제 EU 공급·데이터 연결 확인 시 CRA 적용 가능성 높음 | 실제 SKU, 판매 단위, intended purpose |
| 통합 서보 드라이브 완제품 | Default category 가능성 높음 | 모터 토크/속도/위치 제어가 실제 core functionality인지 기술문서 확인 |
| 독립 판매 EtherCAT/Fieldbus interface | Annex III Class I category 10 가능성 | 별도 PDE로 시장 공급되는지, driver/API/network-interface 기능이 핵심인지 |
| ST MCU | Class I category 14 가능성은 MCU별 검토 | 전체 주문코드, security functionality, separate placing on market |
| tamper-resistant MCU | Class II category 4 가능성 | tamper evidence/resistance/response 및 AVA_VAN 2/3 설계 근거 |
| 통합 제품 내 MCU | host 제품 등급 자동 승계 없음 | Article 7(1), Guidance §§141–145; component due diligence는 별도 |

### 15.3 주요 해석
- 단순 전자회로/전원/ON-OFF 신호와 디지털 정보 교환을 구별한다. Guidance §§26–28에 따라 송신 측의 정보 부호화와 수신 측의 정보 해석 여부를 확인한다.
- EtherCAT/Fieldbus는 2025/2392 category 10 기술 설명에 포함되는 인터페이스 유형이지만, 통합 드라이브 전체의 core functionality가 모터 제어라면 interface 존재만으로 완제품 Class I을 자동 부여하지 않는다.
- ST MCU의 secure boot, encryption, authentication, secure key storage, RNG, TEE 등 기능은 category 14 검토에 중요하나, 제조사·모델명만으로 판정하지 않는다.
- Category 4는 category 14에 더해 tamper evidence/resistance/response 및 AVA_VAN 2/3 설계가 요구된다. 단순 secure boot 또는 debug lock은 충분하지 않다.
- 제조자는 통합 MCU/통신칩의 due diligence를 수행하고, 제품 전체 위험평가와 구성품 실사를 구분한다(Guidance §§167–173).
- 별도 판매·구매·라이선스되는 모듈은 각자의 core functionality로 독립 분류할 수 있고, 통합 제품 전용 구성품은 통합 제품 수준에서 판단한다(Guidance §145).
- EN 40000-1-1/-1-2는 발행 확인. CRA Article 27 OJ 인용은 이번 조사에서 확인되지 않아 적합성 추정을 주장하지 않는다.

### 15.4 미확인 자료
실제 SKU/nameplate, Converter/Drive Unit 공급·판매 경계, HW/FW revision, BOM, ST MCU full order code, 보안 설정, interface driver/API, 제품 수명 및 지원정책은 모두 Unknown으로 유지한다. 보고서 v1.0을 참조하고 자료가 확보되면 갱신한다.

상세 보고서: reports/CRA_MECAPION_SERVO_DRIVE_SCOPE_CLASSIFICATION_2026-11-24.md


## 16. 2026-11-24 — C/2026/6013 및 EN 40000 OJ citation 메타데이터 정밀 정정

- 2026-07-27 Commission guidance announcement는 C(2026) 6013 Communication을 가리킨다. 2026-11-17 OJ C/2026/6013은 동일 지침의 관보 게재본이며 별개의 후속 지침이 아니다.
- CEN/CENELEC 공식 카탈로그에서 EN 40000-1-1:2026 및 EN 40000-1-2:2026 개별 metadata를 확인했다. 두 표준 모두 DAV 2026-11-18이며, Legal > Citation in OJEU는 “No citation expected for Directive 2024/2847”로 표시한다.
- 따라서 두 표준의 CRA Article 27 조화표준 적합성 추정은 기대하거나 주장하지 않는다. 두 표준은 공통 용어 및 위험관리/수명주기 설계 기준으로 활용한다.
- 공식 CEN/CENELEC news: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/
- Official CEN catalogue: https://standards.cencenelec.eu/ (CEN/CLC/JTC 13 published standards; EN 40000-1-1:2026 / EN 40000-1-2:2026).


## 17. 2026-11-24 — iX700M Converter Unit / Drive Unit 공식 제조사 증거 추가

### 공식 제조사 출처 및 확인 항목

| ID | 제조사 자료 | 확인된 사실 | 증거 한계 |
|---|---|---|---|
| MFG-IX7M-01 | LS ELECTRIC Solution Square, LS메카피온 「서보 드라이브 신제품 소개(iX7M, iX700M)」 PDF, iX700M section | Converter Unit/Drive Unit 외관·유닛 구분, Bus-Bar, DC Link, RS-485 Cross Communication, EtherCAT IN/OUT, 각 유닛 기능 및 용량표 | 문서 하단 제작일 표기는 2024-04-01; 이후 SKU 변경을 모두 반영한다고 보지 않음 |
| MFG-IX7M-02 | LS메카피온 공식 CE 제품인증서 페이지 — Converter Unit | `iX700MCV` 코드 체계, CV=Converter Unit, B=480 Vac, 150/370/550/750=15/37/55/75 kW; 별도 CE DoC 파일 게시 | PDF 본문 미확보; 별도 판매 증명은 아님 |
| MFG-IX7M-03 | LS메카피온 공식 CE 제품인증서 페이지 — Drive Unit `iX700MD1-B-150B` | D1/D2/D3=1/2/3축, B=480 Vac, 150=15 kW, Encoder B=BiSS-C, 옵션 코드; 별도 CE DoC 게시 | 대표 예시 SKU이지 사용자 실제 모델 아님; PDF 본문 미확보 |
| MFG-IX7M-04 | LS메카피온 공식 CE 목록 및 KC 목록 | 여러 용량별 Drive Unit 및 Converter Unit 코드가 개별 항목으로 게시됨 | 목록·문서 단위 식별이지 가격·계약·독립 판매의 직접 증거는 아님 |
| MFG-IX7M-05 | LS메카피온 공식 매뉴얼 목록 | iX700M DRIVE 400[V] 매뉴얼 Ver1.4, 2026-05-26 게시 | 목록 메타데이터만 확인; PDF 본문·hash 미확보 |
| MFG-IX7M-06 | LS메카피온 공식 카탈로그 게시판 | iX700M 국문/영문 카탈로그 항목; 파일명 KR/EN `251205` 표기 | 게시판 항목 2025-11-17, 파일 날짜 2025-12-05; 본문·hash 미확보 |

### 모델코드 예시(실제 대상 SKU 아님)

- Converter: `iX700MCV-B-150`, `iX700MCV-B-370`, `iX700MCV-B-550`, `iX700MCV-B-750`.
- Drive: `iX700MD1-B-150B` (CE page model code definition); official listing also shows D1/D2 and multiple power ratings, including 075B, 050B, 045B, 220B, 300B, 370B, 450B, 550B, 750B variants.

### 제품 구조에서 확인된 내용

- Converter Unit: AC 380–480 V 3상 입력을 DC 535–675 V로 정류·평활, Bus-Bar를 통해 Drive Unit 공급; 회생제동 회로 내장, DC24V 제어전원 Bypass.
- Drive Unit: DC Bus 전원으로 모터 구동, Dynamic brake, 모터브레이크 출력, BiSS 및 Universal 2nd encoder.
- 연결: PE Bus-Bar, DC Link Bus-Bar, DC24V, 내부 RS-485 Cross Communication; Drive Unit에는 EtherCAT IN/OUT 표기.
- 제조사 자료는 Power/Converter 부분과 Drive Power 부분을 분리하고 필요한 용량의 Drive를 다중 연결하는 modular architecture로 설명.

### 공급 경계 판정

- 기능적 유닛 분리: **Confirmed**.
- 별도 모델코드/용량 체계: **Confirmed**.
- 유닛별 별도 CE DoC 게시: **Confirmed (게시판/첨부파일 식별 수준)**.
- 실제 독립 주문·상업 판매: **Unknown**.
- EU 시장에서 개별 PDE로 각각 공급: **Unknown**.
- 사용자의 실제 대상 SKU: **Unknown**.

별도 DoC 및 SKU는 독립 제품으로 공급될 가능성을 높이는 자료이지만, 계약·주문·판매 증거를 대신하지 않는다. DoC PDF 본문도 확보 전이므로 발행 내용과 CRA 관련성을 추정하지 않는다.

### CRA 영향

- Converter+Drive를 하나의 통합 시스템으로 공급하면 시스템 제품의 intended purpose/core functionality를 중심으로 평가.
- Converter 및/또는 Drive를 독립 제품으로 공급하면 각 공급 단위의 PDE 정의, 데이터 연결, intended purpose, core functionality를 개별 평가.
- 혼합 공급이면 계약·주문·라벨·EU 수입자 문서와 실제 공급 흐름으로 시장 공급 단위를 판정.
- EtherCAT IN/OUT 및 RS-485는 데이터 연결 분석 근거이나 그 자체로 Annex III category 10 또는 host system classification을 자동 결정하지 않는다.
- CE/LVD/EMC 문서 게시 사실은 CRA 준수·CRA 적합성 추정의 증거가 아니다.

### 공식 링크
1. LS메카피온 드라이브 제품군: https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive
2. LS메카피온 CE Converter Unit page: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886
3. LS메카피온 CE Drive Unit page: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888
4. LS메카피온 매뉴얼 목록: https://www.lsmecapion.com/bbs/board.php?bo_table=manual
5. LS메카피온 카탈로그 목록: https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110
6. LS ELECTRIC Solution Square manufacturer PDF: https://ssq.ls-electric.com/uploads/document/17120093352290/%5BLS%2BELECTRIC%2B%EC%98%A4%ED%94%88%EC%84%B8%EB%AF%B8%EB%82%98%5D%2B%EC%84%9C%EB%B3%B4%2B%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%2B%EC%8B%A0%EC%A0%9C%ED%92%88%2B%EC%86%8C%EA%B0%9C%2BiX7M_iX700M_LS%EB%A9%94%EC%B9%B4%ED%94%BC%EC%98%A8.pdf


## 18. 2026-11-24 — 추가 제조사 증거와 CI 원인

| ID | 공식 자료 | 확인된 사실 | 한계 |
|---|---|---|---|
| MFG-IX7M-07 | iX700M 드라이브 제품군 페이지 | 다축 모듈러 EtherCAT, AC 380–480V, 4.5–75kW, 16.1–168A/축 | 제품군 사양, SKU별 사양 아님 |
| MFG-IX7M-08 | Servo 매뉴얼 목록, 게시물 12652 | iX700M DRIVE 400[V] Ver1.4, 2026-05-26 | PDF 본문/해시 미확보; 검색 캐시 Ver1.3은 최신 목록과 불일치 |
| MFG-IX7M-09 | Servo Drive 도면 목록, 게시물 12455 | 2D CAD/3D STEP 외형도, 2026-04-21 | 첨부 파일 미확보; 회로도/BOM/PCB 아님 |
| MFG-IX7M-10 | KC 및 CE 목록 | `iX700MCB-B-8K` / `iX700MCB` 항목 존재 | MCB/8K 코드 의미는 Unknown |
| MFG-IX7M-11 | 해외 대리점 페이지 | 해외 창구 LS ELECTRIC 자동화, `automation@ls-electric.com` | EU 판매/수입/개별 주문 증거 아님 |

- 별도 모델코드와 CE DoC 게시 사실은 문서상 제품 구분 증거이나 상업 판매 증거는 아니다.
- Converter/Drive 개별 견적·발주 및 EU 개별 PDE 공급: Unknown.
- 실제 사용자 SKU: Unknown.
- 내부 회로도, PCB, BOM, MCU order code 및 보안 설정: Unknown/not publicly acquired.
- 사용자가 프로젝트에서 ST MCU를 사용한다고 알린 사실을 iX700M BOM에 전용하지 않는다. iX700M의 ST MCU 탑재 여부는 Unknown.
- 외형 CAD 게시를 내부 설계 증거로 오인하지 않는다.

### CI failure / correction
- PR #218 Run #1388 attempt 1: source identity, compile, CRA traceability, 183 pytest passed.
- Failure: Commission newsroom PDF request redirected to `https://sorry.ec.europa.eu/`; strict host allowlist rejected the interstitial.
- Remediation: only this exact Commission interstitial becomes a fallback trigger; arbitrary non-allowlisted redirects remain fail-closed. Use only configured ANFR mirror and validate PDF magic, identity markers and extracted text. Added regression test and refreshed workflow blob pins.
- PR #218 remains unmerged pending exact-head full CI success.


## 18.1 CI 원문 수집 endpoint correction
- Run #1395: source identity, compile, CRA traceability 및 pytest 184개 성공; PDF canary 실패.
- 실패 지점은 C/2026/6013 EUR-Lex PDF URL의 CI redirect to sorry.ec.europa.eu. 이 source definition에는 fallback이 없어 fail-closed 처리.
- Official Publications Office direct PDF를 primary URL로 변경: https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1.
- Browser verification: official OJ PDF, 61 pages, title Commission guidance on the application of Regulation (EU) 2024/2847, C/2026/6013, 17.11.2026.
- Host allowlist is exact publications.europa.eu; test asserts URL and host. Existing PDF magic, required identity markers, extracted text and SHA-256 checks remain.
- New exact-head CI required; no merge based on Run #1395.


## 18.2 C(2026)7861 official register automated access restriction
- Run #1404: source identity, compile, CRA traceability and pytest 184 passed; PDF acquisition failed on C(2026)7861 Annex API redirect to sorry.ec.europa.eu.
- C/2026/6013 was already switched to the browser-verified official Publications Office direct OJ PDF.
- C(2026)7861 is a Commission document-register file, not an OJ publication; no substitute OJ URL is asserted.
- Exact Commission anti-bot interstitial now maps to PDFSourceUnavailableError. No external mirror is auto-accepted for C(2026)7861. Main reports SKIPPED with exit 0; PDF artifact upload may be skipped, while the independent HTML canary remains.
- This is not a content validation success: automated C(2026)7861 PDF bytes/hash remain unavailable. Official Commission register content is browser-verified; retain this provenance limitation.


## 18.3 Run #1410 검증 범위 및 PDF canary 한계
- Exact tested HEAD at Run #1410: 1c49b9f4b5ad8fa747ffa08051fa6116dd3eff85.
- Workflow conclusion success: source identity, compile, CRA traceability, pytest, official CRA HTML locator validation, provenance manifest upload passed.
- PDF source step printed SKIPPED because C(2026)7861 document-register API returned official anti-bot interstitial. PDF evidence upload was skipped. Do not record this as successful PDF acquisition or SHA-256 capture.
- C/2026/6013 primary PDF URL is the browser-verified official Publications Office OJ document. C(2026)7861 PDF bytes/hash remain not acquired automatically.
- After Run #1410, a comment-only source clarification and corresponding source-blob pin were committed; new exact HEAD requires a final CI run before merge.


## 18.4 PR #218 final CI and merge
- Final HEAD: e3ebe08b5dcf14563bba0a75dca171459ab992c5.
- Run #1417 / 45293726074: workflow success. Source identity, compile, CRA traceability, complete pytest, official CRA HTML locator validation and provenance manifest upload passed.
- PDF source canary: SKIPPED because C(2026)5252 primary Commission newsroom redirected to interstitial and the explicitly allowlisted ANFR mirror timed out after 30 seconds. PDF evidence upload skipped. Do not claim new Commission PDF bytes/hash were captured by this run.
- Final diff: 11 files, reviewed; no main.py, production workflow, secrets or API cadence change. Isolated test workflow source blob pins were updated.
- PR #218 squash merged; merge SHA 200ccca974ad3af09b1634fd9bf02c1baac5ca8c.
- Independent sale/EU supply, actual user SKU, manual/CAD attachment contents, internal schematic/BOM/MCU remain Unknown as detailed in §§17–18.


## 18.5 PDF source fallback 안정성 및 부분 provenance
- PR #223 Run #1419 failed after all 184 prior tests/traceability passed; PDF fallback URL for C(2026)5252 returned HTML instead of PDF (other run: 30-second read timeout).
- Removed unstable ANFR fallback. Configured Commission-hosted EU portal copy at transition-pathways.europa.eu for C(2026)5252 Annex; browser verified European Commission heading, 27.7.2026, C(2026)5252 final and CRA guidance text.
- fetch_all_pdf_sources now handles source-unavailable documents individually: verified PDFs are written with SHA-256; unavailable entries are retained in manifest with status/reason; remaining sources continue.
- Invalid PDF magic, missing required identity markers, malformed content and arbitrary non-allowlisted redirects still fail closed.
- Added regression test for partial acquisition and updated source/test blob pins. Exact PR #223 HEAD CI pending.


## 18.6 Run #1427 — verified partial PDF evidence
- Exact PR #223 HEAD: fc736e91e98ad384c3efa8112345dfa8c4156158; Run #1427 / 45294643451 success; pytest 186 passed.
- C(2026)5252 Annex: 84 pages / 1,190,726 bytes / SHA-256 fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234; Commission-hosted transition-pathways.europa.eu copy, fallback used.
- C/2026/6013 OJ: 61 pages / 2,709,282 bytes / SHA-256 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2; Publications Office direct, no fallback.
- C(2026)7861 Annex: Commission register read timeout after 30s; recorded as unavailable in manifest; does not prevent the other two PDFs from being stored.
- PDF artifact ID 14874639916; provenance manifest artifact ID 14875084483. Run #1427 also passed official HTML source locator validation (10 sources).
- Source acquisition now records per-source status; invalid PDF/identity/host checks remain hard failures.


## 18.7 PR #223 merge record
- PR #223 squash merged: a1fe5b983e1cecb1235b56071534e05884d61786.
- Exact HEAD 76e5bce626db999e434d41f50ac0b9413b9561d5, Run #1432 / 45295093222 success; 186 pytest passed; source identity/compile/CRA traceability/10 HTML locators/PDF canary/two artifact uploads all passed.
- C(2026)5252 and C/2026/6013 PDF hashes and artifact IDs in §18.6. C(2026)7861 remains unavailable due Commission register timeout, explicitly recorded in manifest.
- 11 files reviewed; only docs, CRA PDF source collector/tests and isolated test workflow blob pins changed. No production main.py, secrets or API cadence changes.


## 19. 2026-11-24 — 제조사 질의서 및 증거 확보 게이트

- MFG-IX7M-Q01: LS메카피온 공식 기술·영업 질의서 초안 — reports/LS_MECAPION_IX700M_FORMAL_TECHNICAL_COMMERCIAL_INQUIRY_2026-11-24.md.
- 요청 증거: 독립 판매/주문/교체 여부, EU 공급국·법인·수입자·거래 문서, 전체 SKU 및 옵션 정의, Ver1.4 매뉴얼 원본, 외형 CAD 원본, 회로도/BOM 또는 redacted BOM, MCU/통신/보안 IC 전체 주문코드와 revision, firmware/update/security controls, SBOM/PSIRT/support period, 유닛별 및 조합별 EU DoC.
- 질문별 답변 상태와 증거를 요구한다. 구두 답변은 참고자료로만 보관하고, 제품 분류를 변경하는 근거는 문서번호·개정일·적용 SKU·공급 단위가 확인되는 서면 자료로 한정한다.
- NDA/redacted version/부품군별 BOM/제조사 서명 확인서도 대체 증거로 허용한다. 개인키·암호키 원문·비밀번호·생산 계정 등 비밀값은 요청하지 않는다.
- 현재 상태: 질의서 작성 완료 / 제조사 발송 및 회신 미확인. 발송·회신 확인 전까지 Unknown 판정을 유지한다.


## 20. 2026-11-24 — LS메카피온 공식 질의 발송 경로

- CONTACT-DOM-01: 공식 국내 업무별 담당자 페이지 https://www.lsmecapion.com/customer/take.php. 지역별 국내 서보 영업 담당자 게시. 경기 담당자 공개 주소 scahn@lsmecapion.com / 070-7772-8422. 회사/프로젝트 소재지가 경기인지 확인한 후 사용하며 담당 업무와 접수 가능 여부는 발송 전 재확인.
- CONTACT-TECH-01: 공식 기술지원 페이지 https://www.lsmecapion.com/customer/take4.php. 전국 서보 기술문의 및 지원 1544-5948, 상담시간 08:30~17:30(점심 12:30~13:30 제외). 기술지원 이메일은 페이지에 확인되지 않아 임의 생성하지 않음.
- CONTACT-OVERSEAS-01: 공식 해외 담당 페이지 https://www.lsmecapion.com/customer/agency2.php. LS ELECTRIC 자동화 연락처 automation@ls-electric.com 게시. 해외 담당 창구로만 식별하며 실제 EU 수입자·판매 법인·경제운영자라고 추정하지 않음.
- 발송 경로 및 커버메일 안내: reports/LS_MECAPION_IX700M_INQUIRY_DISPATCH_GUIDE_2026-11-24.md.
- 질의서 발송/접수/회신은 미확인. 회사명·소재지·실제 담당부서 확인 전 발송 완료로 기록하지 않는다.


## 21. 2026-11-24 — iX700M CE·모델코드·매뉴얼/CAD 교차검증

| ID | 공식 출처 | 새로 확인한 사실 | 증거 한계 / 상태 |
|---|---|---|---|
| MFG-IX7M-12 | CE Converter 게시물 https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | iX700MCV, CV=Converter Unit, B=480Vac, 150/370/550/750=15/37/55/75kW; CE_DoC-LVDEMC iX700MCV.pdf 첨부명 표시 | PDF 본문/서명/hash 미열람. 별도 판매나 EU 공급 증거 아님 |
| MFG-IX7M-13 | CE Drive 게시물 https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | D1/D2/D3=1/2/3축, B=480Vac, 150=15kW, encoder B=BiSS-C, 옵션 suffix 정의; Drive별 CE 게시물 | 첨부 PDF 본문 미열람. 예시 SKU이며 실제 프로젝트 SKU 아님 |
| MFG-IX7M-14 | 공식 매뉴얼 목록 https://www.lsmecapion.com/bbs/board.php?bo_table=manual | 검색 색인은 Ver1.4(2026-05-26), 직접 연 목록 캐시는 Ver1.3(동일 게시일)로 상충 | 원본 PDF·revision history·hash 미확보. 최신 버전 Unknown/충돌 |
| MFG-IX7M-15 | 공식 Servo Drive 도면 목록 https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M 2D CAD/3D STEP 외형도 게시물, 2026-04-21 | 상세 첨부 원본·파일명·bytes·hash 미확보. 회로도/BOM 아님 |

- Confirmed: 제조사 문서/모델코드 차원에서 Converter Unit과 Drive Unit 구분.
- Unknown: 유닛별 독립 견적·발주·계약·판매, EU/EEA 개별 공급, 실제 프로젝트 SKU.
- Unknown: 매뉴얼 최신 revision 및 PDF 본문, CAD 원본 bytes/hash, 내부 회로도·PCB·BOM·MCU order code·보안 설정.
- 별도 CE DoC 게시 사실을 CRA conformity, 독립 판매, EU market placement로 해석하지 않는다.
- 질의서 발송/접수/회신 미확인. CRA only; SIL 3 제외.


## 22. 2026-11-24 — iX700M 매뉴얼 목록·CE DoC·CAD 원본 재검증

| ID | 공식 출처 | 확인 사실 | 증거 한계 / 판정 |
|---|---|---|---|
| MFG-IX7M-16 | 전체 매뉴얼 목록 https://www.lsmecapion.com/bbs/board.php?bo_table=manual | 직접 열린 페이지 본문에서 iX700M DRIVE 400[V] Ver1.3, 게시일 2026-05-26 | 검색엔진 저장 결과에는 Ver1.4가 남아 있음. 상세 게시물/첨부 다운로드 cache miss. PDF revision/hash Unknown |
| MFG-IX7M-17 | Servo 필터 목록 https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo | 직접 열린 페이지 본문에서도 Ver1.3, 게시일 2026-05-26 | 위 전체 목록과 동일 표시. 실제 첨부 PDF 본문 확인 아님 |
| MFG-IX7M-18 | Converter CE 게시물 https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | `[CE_DoC-LVDEMC] iX700MCV.pdf`, 234.4K 첨부명 및 게시일 2026-04-30 | 첨부 download URL cache miss; PDF 본문/서명/법령 범위 미검토 |
| MFG-IX7M-19 | Drive CE 게시물 https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | `[CE_DoC-LVDEMC] iX700MD1-B-150B.pdf`, 238.9K 첨부명 검색결과 확인 | 원본 PDF 미확보. 검색결과 외 상세 직접 열람 실패 |
| MFG-IX7M-20 | CAD 목록 https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M Series 2D CAD/3D STEP 외형도, 2026-04-21 게시 | 상세 `wr_id=12455` cache miss; 첨부 원본·파일명·크기·hash Unknown |
| MFG-IX7M-21 | 제품군 페이지 https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive | iX700M: AC 380–480 V, 4.5–75 kW, 다축 모듈러 EtherCAT 통신형 | 제품군 공개 사양. 실제 SKU/옵션/판매 계약 증거 아님 |

- 현재 공식 목록의 직접 페이지 표시는 Ver1.3. 검색 snippet의 Ver1.4는 cache/index 불일치로 격하하고, 실제 PDF 버전은 원본 확보 전 Unknown.
- CE DoC 첨부명/크기는 게시 메타데이터일 뿐 DoC 본문 검토나 CRA conformity 증거가 아니다.
- CAD 게시 사실은 확인했으나 원본 첨부 확보는 실패. 다른 모델(PHOX) 첨부 크기를 iX700M에 적용하지 않는다.
- 독립 판매, EU/EEA 개별 공급, 실제 대상 SKU, importer/economic operator, 내부 회로/BOM/MCU/보안 설정은 Unknown 유지.


## 23. 2026-11-24 — 매뉴얼 버전 충돌·CE DoC/CAD 첨부 재접근

| ID | 공식 출처 | 확인 사실 | 증거 한계 / 판정 |
|---|---|---|---|
| MFG-IX7M-22 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | 직접 열린 전체 목록 snapshot: iX700M DRIVE 400[V] Ver1.3, 2026-05-26 | 다른 공식 검색 snapshot은 Ver1.4 표시. revision conflict unresolved; 상세 `wr_id=12652` cache miss; PDF bytes/hash unknown |
| MFG-IX7M-23 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual 및 https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo | 공식 검색 snapshot에서 동일 게시일 Ver1.4 확인 | Ver1.3 snapshot도 존재. 검색 색인 오류/첨부 교체/실제 revision 중 무엇인지 제조사 확인 필요 |
| MFG-IX7M-24 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter CE 상세 페이지 및 첨부명 `[CE_DoC-LVDEMC] iX700MCV.pdf` (234.4K) 확인 | attachment URL cache miss; PDF body/signature/scope not inspected |
| MFG-IX7M-25 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | Drive DoC 검색 snapshot: `[CE_DoC-LVDEMC] iX700MD1-B-150B.pdf` (238.9K) | 상세 페이지 cache miss; PDF original/body unknown |
| MFG-IX7M-26 | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M 2D(CAD)/3D(STEP) 게시, 2026-04-21 | 상세 `wr_id=12455` cache miss; original DWG/DXF/STEP, filename, size, revision, hash unknown |

- 이전 “Ver1.4는 stale index” 단정은 철회. 현재 판정은 공식 페이지 snapshot 간 revision 표기 충돌이며 실제 PDF revision Unknown.
- 원본 첨부 접근 실패는 확보 실패로 기록. DoC/CAD 내용 검토 완료로 표현하지 않는다.
- 실제 프로젝트 SKU, 독립 판매, EU/EEA 개별 공급, importer/economic operator, BOM/MCU/security configuration은 Unknown.


### 공개 유통 경로 및 제품 세대 구분 보강

- `MFG-IX7M-27` — LS메카피온 해외 대리점 공식 페이지 https://www.lsmecapion.com/customer/agency2.php : 해외 담당 `LS ELECTRIC 자동화 / automation@ls-electric.com` 표시. EU/EEA 현지 유통사·수입자·경제운영자 또는 iX700M 거래 역할은 명시하지 않음.
- `MFG-IX7M-28` — LS메카피온 국내 대리점 페이지 https://www.lsmecapion.com/customer/agency.php : 경기 수원 등 국내 지역 대리점 목록 표시. 국내 대리점 등록은 EU 공급/수입자 증거가 아님.
- 검색된 LS ELECTRIC Solution Square의 `iX7M-A-...` DoC는 iX7M 모델을 대상으로 하므로 iX700M DoC로 전용하지 않음.
- EU/EEA 개별 공급, importer/economic operator, actual SKU 및 각 거래 역할은 계속 Unknown. 공개 페이지에서 EU 판매자/수입자 확인이 안 된다는 사실을 “없다”로 확대 해석하지 않는다.


## 24. 2026-11-24 — Solution Square iX700M 사용 설명서 메타데이터 및 재접근

| ID | 공식 출처 | 확인 사실 | 증거 한계 / 판정 |
|---|---|---|---|
| MFG-IX7M-29 | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 | LS ELECTRIC Solution Square Motion & Servo 목록에 `iX700M 사용 설명서`, update 2026-09-16 표시 | 상세는 JS 앱으로 실제 PDF 링크/파일명/document ID/revision/language/size/hash 접근 불가. Ver1.3/1.4 중 어느 것과 관계인지 Unknown |
| MFG-IX7M-30 | https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 | 공식 통합검색에서 `iX700M 사용 설명서` 문서 항목 확인 | 목록 메타데이터 외 상세 본문·첨부 미확보 |
| MFG-IX7M-31 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual 및 https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo | 직접 열린 페이지 본문 snapshot은 Ver1.3(2026-05-26) | 공식 검색 snapshot 일부는 Ver1.4(동일 게시일) 표시. 상세 `wr_id=12652` cache miss. actual PDF revision Unknown |
| MFG-IX7M-32 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter iX700MCV CE 게시물과 첨부명 `[CE_DoC-LVDEMC] iX700MCV.pdf` (234.4K) 확인 | 첨부 클릭 cache miss; PDF bytes/body/signature/scope/hash unknown |
| MFG-IX7M-33 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | Drive iX700MD1-B-150B DoC 검색 메타데이터 및 첨부명/238.9K 확인 | 상세 cache miss; PDF bytes/body/signature/scope/hash unknown |
| MFG-IX7M-34 | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M 2D(CAD)/3D(STEP) 게시, 2026-04-21 | 상세 `wr_id=12455` cache miss; DWG/DXF/STEP 원본과 revision/hash unknown |

- Solution Square update date는 PDF 발행일/revision number가 아니다. Ver1.5 등으로 추정하지 않는다.
- Ver1.3/Ver1.4 게시물 표시 충돌은 unresolved. 실제 PDF bytes와 제조사 문서관리 이력으로 해결해야 한다.
- Converter/Drive DoC 게시 사실과 별도 모델코드는 독립 상업 판매, EU 공급 또는 CRA conformity를 증명하지 않는다.


## 25. 2026-11-24 — Run #1460 공식 CRA PDF evidence artifact 검증

| ID | 공식 원본 | 확보/검증 결과 | SHA-256 |
|---|---|---|---|
| CRA-PDF-2026-5252 | Commission C(2026) 5252 final CRA Guidance Annex | PDF 84 pages, 1,190,726 bytes; artifact 14884517329 내부 원본 확인 | `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234` |
| CRA-PDF-2026-6013 | Commission C/2026/6013 CRA Guidance, OJ C 17.11.2026 | PDF 61 pages, 2,709,282 bytes; artifact 14884517329 내부 원본 확인 | `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2` |
| CRA-PDF-2026-7861 | Commission C(2026) 7861 M/606 Annex | unavailable; Commission document-register API 30초 read timeout. 바이너리 미확보 | Unknown |

- PDF evidence ZIP artifact SHA-256: `404f048a117e84dbeab4dcff863c4a5b0990e47bf0550a28bcb505fef339b134`.
- Provenance manifest artifact ID 14884017656, ZIP SHA-256 `4a2fe3024fe12f259dc1bce49ac0e32782a826fa01bbce4a16c19e604caaa1bf`; official source 10 records, manifest JSON round-trip passed.
- Run #1460 PDF canary step은 success이나, 세 PDF 중 2개만 실제 확보했다. C(2026)7861은 성공으로 승격하지 않고 unavailable로 유지한다.
- PR #231 exact HEAD `d1f0c2a32c455f2d2a27dda5eab8972cad87bcef`, Run #1460 / 45314263089 success. 8-file diff, JSONL 357 records / invalid 0, review threads 0. Expected-head squash merge SHA `c7b59ae51891a2b878fc85b0910a89b50e4efe17`.
- iX700M Solution Square 2026-09-16 항목의 상세 URL/PDF, LS메카피온 Ver1.3/Ver1.4 실제 revision, Converter/Drive DoC, DWG/DXF/STEP 원본은 미확보. 실제 SKU, 독립 판매, EU/EEA 공급, importer/economic operator, BOM/MCU/security 설정은 Unknown.
- 제조사 질의서는 `draft_prepared_not_sent`; 실제 발송·접수·회신 증거 없음.
- PR #229 merge SHA `4263389aa79cbb7cc17ccda3a019c659ccddef85`의 post-merge main push CI는 accessible run/status 없음. `pending_unverified` 유지.


## 26. 2026-11-24 — Run #1462 PDF 3종 확보 및 제품 증거 교차검증

### 공식 CRA PDF evidence artifact

Run #1462 / ID 45314843427, PDF artifact 14884218192. ZIP 3,070,568 bytes, SHA-256 `42775754732e4cc8b9a31a702beb7daf7c9722777210e55dfb87c8563176f6cf`.

| ID | 원본 | 페이지 / bytes | SHA-256 | 상태 |
|---|---|---:|---|---|
| CRA-GUIDANCE-2026-5252 | C(2026)5252 final Annex | 84 / 1,190,726 | `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234` | fetched |
| CRA-GUIDANCE-OJ-2026-6013 | C/2026/6013 OJ C 17.11.2026 | 61 / 2,709,282 | `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2` | fetched |
| CRA-M606-C2026-7861-ANNEX | C(2026)7861 final Annex, 10.11.2026 | 6 / 151,267 | `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276` | fetched |

각 PDF magic, 문서 식별문구, 페이지 수, SHA-256 확인. C(2026)7861은 Run #1460에서는 timeout/unavailable였으나 Run #1462에서 성공적으로 확보됨. Provenance artifact 14884277978 / 2,565 bytes / ZIP SHA-256 `098047a15d56c9908c9babc0a7afc8bb019900191621f08edb205a03df50b966`; manifest 10 sources, SHA-256 `7dff3ca57a325a1de522a344beffff48bdbbb785441e01014d3af33713c5902f`.

### PR #232

- Exact HEAD `94bbe5d2e43b428ccbb48436d8c826603bca01ac`, Run #1462 success, steps 1~12 and cleanup all success.
- Base `c7b59ae51891a2b878fc85b0910a89b50e4efe17`; 6 files; ahead 6 / behind 0; branch JSONL 358 / invalid 0; review threads 0 / reviews 0.
- Expected-head squash merge SHA `d3b75a84d2b84ada59d2314780461e53b21e090b`; main read-back identical, JSONL 358 / invalid 0.

### iX700M evidence status

- LS메카피온 공식 목록 snapshot 간 버전 충돌이 재현됨: `bo_table=manual` 및 `sca=Servo`는 Ver1.4, `sca=` 및 `page=1`은 같은 게시물 41번을 Ver1.3으로 표시(모두 2026-05-26). 어느 쪽이 실제 최신 PDF인지 미확정. 상세 `wr_id=12652` PDF 미확보; 내부 revision/hash/SKU applicability Unknown.
- Solution Square `iX700M 사용 설명서` 2026-09-16 항목은 재확인. JS detail route/PDF/문서 ID 미확보.
- Converter CE metadata: `iX700MCV`, 480Vac, 15/37/55/75kW rating codes, attachment metadata 234.4K. Drive CE metadata: example `iX700MD1-B-150B`, D1=1-axis, 480Vac, 15kW, BiSS-C encoder, attachment metadata 238.9K. Both original PDFs inaccessible (502/cache miss); DoC content and scope unverified. Separate CE listing is not proof of independent sale.
- CAD DWG/DXF/STEP bytes still missing. Actual target SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security config remain Unknown.
- Manufacturer inquiry remains `draft_prepared_not_sent`.
- PR #229 main push is now verified: Run #1452 / ID 45312941583, event push, exact merge SHA 4263389aa79cbb7cc17ccda3a019c659ccddef85, conclusion success, 25/25 steps passed.


## 27. 2026-11-24 — 공식 제조사 제품군·자료 인덱스 재검증 및 원본 접근 재시도

| ID | 공식 출처 | 새로 재확인한 내용 | 원본/한계 및 증거 상태 |
|---|---|---|---|
| MFG-IX7M-35 | https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive | iX700M 다축 모듈러 EtherCAT 통신형, AC 380–480 V, 4.5–75 kW, 축당 16.1–168 A | 제품군 공개 사양. 개별 SKU/구성/EU 공급 또는 CRA 분류 증거로 확대 불가 |
| MFG-IX7M-36 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual 및 `&sca=Servo`, `&sca=`, `&page=1` | 기본 목록·Servo filter는 Ver1.4, 빈 분류·page=1은 같은 게시물 41번/2026-05-26에 Ver1.3 표시 | 상세 `wr_id=12652` inaccessible/cache miss. 실제 PDF revision, 문서번호, 변경이력, hash Unknown; conflict unresolved |
| MFG-IX7M-37 | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 및 https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 | Solution Square 공식 목록/통합검색에 `iX700M 사용 설명서`, update 2026-09-16 | JS app shell만 접근. detail URL/document ID/PDF/file name/revision/hash Unknown |
| MFG-IX7M-38 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | Drive DoC 게시물 직접 열람. iX700MD1-B-150B 예시, 1-axis, 480Vac, 15kW, BiSS-C, attachment metadata 238.9K | attachment click/download timeout. PDF body/signature/scope/hash 미검증 |
| MFG-IX7M-39 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter DoC 공식 검색 index: iX700MCV, 480Vac, 15/37/55/75kW codes, attachment metadata 234.4K | detail/attachment timeout. PDF bytes/body/signature/scope/hash 미검증 |
| MFG-IX7M-40 | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M 2D(CAD)/3D(STEP) drawing list item 19, 2026-04-21 | detail `wr_id=12455` 502/cache miss. DWG/DXF/STEP original bytes/hash 미확보 |

- Official index metadata and source list evidence are distinct from acquiring/validating attached source bytes. Do not mark any manual, CE DoC or CAD original as acquired.
- Actual SKU, independent sale, EU/EEA supply, transaction-specific importer/economic operator, BOM/MCU/security configuration remain Unknown.
- Manufacturer inquiry remains `draft_prepared_not_sent`; no sending/receipt/reply proof.
- CRA only; SIL 3 excluded.


## 28. 2026-11-24 — iX700M 공식 아키텍처 PDF 및 제조사 카탈로그·교육자료 인덱스

| ID | 공식 출처 | 확인 사실 | 원본 확보/한계 |
|---|---|---|---|
| MFG-IX7M-41 | https://sol.ls-electric.com/uploads/document/17120093352290/%5BLS%2BELECTRIC%2B%EC%98%A4%ED%94%88%EC%84%B8%EB%AF%B8%EB%82%98%5D%2B%EC%84%9C%EB%B3%B4%2B%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%2B%EC%8B%A0%EC%A0%9C%ED%92%88%2B%EC%86%8C%EA%B0%9C%2BiX7M_iX700M_LS%EB%A9%94%EC%B9%B4%ED%94%BC%EC%98%A8.pdf | LS Mecapion PDF의 iX700M 전용 구간에서 Converter/Drive 모듈, DC Link, RS-485 cross communication, EtherCAT In/Out, USB, Loader, I/O, BiSS/Universal encoder 및 AC380–480V→DC535–675V 구조 확인 | PDF 텍스트는 브라우저에서 열람. 원본 바이너리 download/bytes/SHA-256 미확보. 푸터 내부 timestamp 2024-04-01; current manual 아님. iX7M 전용 표는 iX700M 근거에서 제외 |
| MFG-IX7M-42 | https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 | iX700M KR/EN catalog 게시물 및 첨부명 `iX700M 브로셔 최종KR_251205.pdf`, `iX700M 브로셔 최종EN_251205.pdf` 각 10.7M, attachment date 2025-12-05 표시 | 상세 페이지 502/cache miss. PDF bytes/body/revision/hash 미확보. 게시물 제목 (2025년 7월), 게시일 2025-11-17, 첨부일 2025-12-05 구분 |
| MFG-IX7M-43 | https://www.lsmecapion.com/bbs/board.php?bo_table=edu_data | iX700M 시스템서보 드라이브 교육자료 항목, 작성일 2025-10-27 | 상세 `wr_id=52` timeout. 첨부명·본문·hash Unknown |

- 아키텍처 PDF는 EtherCAT/USB/Loader 등 인터페이스 식별의 보조 근거이며, secure boot, signed update, encryption, authentication, vulnerability handling의 존재를 입증하지 않는다.
- PDF에 iX7M과 iX700M이 함께 수록되어 있으므로 iX700M 전용 구간만 사용하고 iX7M 사양을 전용하지 않는다.
- 목록 메타데이터를 원본 PDF 확보로 표현하지 않는다. Solution Square manual, actual Ver1.3/1.4 manuals, CE DoC, CAD 원본은 여전히 미확보.
- CRA only; SIL 3 제외.


## 29. 2026-11-24 — iX700M 매뉴얼·CE DoC·CAD 자료 재접근 및 Run #1481

| ID | 공식 자료/URL | 새로 확인된 정보 | 원본 취득 및 제한 |
|---|---|---|---|
| MFG-IX7M-44 | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 | Solution Square Motion & Servo 목록 및 통합 검색에 `iX700M 사용 설명서`, update 2026-09-16 표시 | JS app shell로 상세 URL/document ID/PDF 원본 확인 불가. LS Mecapion Ver1.3/1.4와 동일 문서인지 Unknown |
| MFG-IX7M-45 | https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo | Servo filter는 `iX700M DRIVE 400[V] 매뉴얼 Ver1.4`, 2026-05-26 표시 | 실제 detail `wr_id=12652` timeout. PDF bytes/hash/revision unknown |
| MFG-IX7M-46 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual&page=1 | Full index snapshot은 같은 게시물 no.41/date 2026-05-26을 Ver1.3으로 표시 | Ver1.3/Ver1.4 snapshot conflict unresolved. 실제 PDF revision 미확인 |
| MFG-IX7M-47 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter CE 게시물, iX700MCV, CV, B=480Vac, 150/370/550/750=15/37/55/75kW, 첨부명 `[CE_DoC-LVDEMC] iX700MCV.pdf` 234.4K, 2026-04-30 | 실제 DoC PDF 다운로드 timeout; 본문/서명/규격/지침/모델범위 미검증 |
| MFG-IX7M-48 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | Drive 게시물 iX700MD1-B-150B, D1=1축, B=480Vac, 150=15kW, B=BiSS-C 또는 custom, 첨부명 `[CE_DoC-LVDEMC] iX700MD1-B-150B.pdf` 238.9K, 2026-04-30 | 실제 DoC PDF 다운로드 timeout; DoC 본문 미검증 |
| MFG-IX7M-49 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE | CE 목록에 iX700MCB, MD1-B 용량별 항목, iX700MCV가 2026-04-30에 게시된 것으로 표시 | 목록 메타데이터만. 실제 판매/독립 공급/EU 시장 공급 또는 CRA 적합성 증거 아님 |
| MFG-IX7M-50 | https://lsmecapion.com/bbs/board.php?bo_table=drawing&page=1 ; https://lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | 게시물 117번, iX700M 2D(CAD)/3D(STEP), 2026-04-21 | 상세 timeout; 첨부명·확장자·bytes/hash 미확보. DWG/DXF 각각 존재 여부 Unknown |
| CRA-CI-1481 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45317449785 | exact main HEAD `c395fc5b5b2a393632bb2fbe65b10fd6572b936d`, Run #1481 / 45317449785 success 25/25 | PDF artifact 14886830715 ZIP 3,070,567B SHA-256 `de227aa54d5a76541738d10511b7f04de18fe6e6487ac0949c0a9a89be9c7175`; provenance artifact 14885424833 ZIP 2,565B SHA-256 `41be60344b6921ad9ccbead26ce870578e3bc2363b51dc24c78730e3fe1ee48c` |

- CE DoC listing/file names are not equivalent to inspected declarations; do not infer the standards/directives or CRA compliance until PDF body is acquired and reviewed.
- Solution Square update date is a listing metadata fact only; no proof that the manual equals LS Mecapion Ver1.3 or Ver1.4.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security configuration remain Unknown. Inquiry `draft_prepared_not_sent`.
- CRA only; SIL 3 excluded.


## 30. 2026-11-24 — PR #237 병합 및 Run #1483 partial source pack

| ID | 증거 | 결과 및 해석 |
|---|---|---|
| CRA-CI-1482 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45318431483 | PR #237 exact HEAD `0b173310aafc82d8db1c7bce032d93ee9fbd0db3`, Run #1482 success 25/25. 6 files, JSONL 365/0, review threads 0, reviews 0, base `c395fc5b5b2a393632bb2fbe65b10fd6572b936d`. Merge SHA `792eea6388382a1932f1b775e57776a7ccacf3a6`. |
| CRA-CI-1483 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45318639981 | Post-merge main push, exact merge SHA, success 25/25. Main read-back identical. |
| CRA-PDF-1483 | Artifact 14886766794 | ZIP 2,922,421B, SHA-256 `3f6c27de5224eb480951133a39ea5791b83753ae2038c1072158db94bbbb758c`. Includes C(2026)5252 (84p), C/2026/6013 (61p), text extracts and manifest. C(2026)7861 is explicitly `unavailable` due official Commission register API read timeout (30s); 2/3 PDF fetched. |
| CRA-PROV-1483 | Artifact 14885852834 | ZIP 2,565B, SHA-256 `16b7160436069a0ccecc2a1b04e923a5eb119aa11506b8fb7a6197030bc2be7c`. Separate official HTML source manifest, 10 sources. |
| CRA-M606-1481 | Run #1481 artifact 14886830715 | Previously acquired C(2026)7861 Annex 6-page original retained, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`. Run #1483 temporary timeout does not invalidate this earlier verified binary. |
| CRA-M606-REGISTRY | https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401 | Official browser extraction confirms C(2026)7861 final Annex, dated 10.11.2026, and 41 standards draft items/deadlines. Web extraction is not a substitute for the binary PDF artifact. |

- Important quality distinction: workflow conclusion `success` means test/canary process completed under its current policy; it does not mean every optional/live PDF source was retrieved. Run #1483 log truthfully states `fetched=2, unavailable=1`.
- `cra_pdf_sources.py` currently records transient `PDFSourceUnavailableError` as unavailable and returns exit 0. No code/workflow change made in this PR. Retry/backoff and explicit completeness indicator are candidates for a separate tested change.
- CRA only; SIL 3 excluded.


## 31. 2026-11-24 — M/606 PDF repeated timeout 및 bounded retry 개선

| 대상 | Run/근거 | 결과 |
|---|---|---|
| M606 PDF transient failure | Run #1483 ID 45318639981, Run #1484 ID 45319203387, Run #1485 ID 45319407719 | 3회 연속 artifact manifest에서 C(2026)7861 Annex unavailable, reason read timeout 30s. C(2026)5252 및 C/2026/6013은 3회 모두 fetched. |
| Prior successful binary | Run #1481 artifact 14886830715 | C(2026)7861 Annex 6 pages, 151,267B, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`. 원본은 유효하게 보존. |
| Code fix | `cra_pdf_sources.py` | transient network/HTTP errors only, max 3 attempts with 1s/2s backoff. Anti-bot interstitial and validation errors are not retried. |
| Partial-status clarity | `cra_pdf_sources.py` | unavailable source is preserved in manifest; exit 0 remains to avoid external service flakiness turning all CI red, but console now says `WARNING: partial CRA PDF source pack` rather than unconditional PASS. |
| Tests | `tests/test_cra_pdf_sources.py` | timeout-then-success, bounded exhaustion, and partial warning behavior covered. |

- Workflow YAML changes only refresh the exact source-blob integrity pins for `cra_pdf_sources.py` and `tests/test_cra_pdf_sources.py`; job steps, cadence, secrets and `main.py` behavior remain unchanged. Retry is bounded and does not accept untrusted mirrors or bypass PDF identity markers.
- CRA only; SIL 3 excluded.

- Run #1486 / 45319973724 failed at workflow step 4 only: stale expected blob for `cra_pdf_sources.py` (`bbbb4156...` vs actual `c24f4d1c...`). The test file pin also needed refresh (`79acd36f...` to `1664ebcf...`). Updated only these two integrity pins; workflow execution logic unchanged. No compile/test ran in failed attempt.

| CRA-PDF-1497 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45320409623 | PR #239 exact branch HEAD `00a00ef1ad8fa09efc68d9d2764d18c2b5b9040f`, Run #1497 success 25/25, pytest 189 passed. PDF artifact 14887520943, 3,070,568B, ZIP SHA-256 `9f8c1c64a43c17fae1a093c454e4be212d5b55fd6914130c9a4e1921411a80b4`; C(2026)5252 84p, C/2026/6013 61p, C(2026)7861 Annex 6p. M606 binary SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`, same as Run #1481. Provenance artifact 14887800169, 2,565B, ZIP SHA-256 `2247997aa180f94a61672674b4fc8144e18a0c91deb51fcb26d82880c1aef6bd`. |
- Retry improvement successfully recovered M606 Annex after three consecutive earlier timeouts; keep previous original and new identical hash as independent retrieval confirmations.


## 32. 2026-11-24 — PR #239 merge, official source recheck and retrieval boundary

| Evidence ID | 공식 자료 / 관찰 | 확인된 사실 | 미확보·한계 | 상태 |
|---|---|---|---|---|
| SQ-IX700M-MANUAL-2026 | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 | Motion & Servo 목록의 iX700M 사용 설명서, update 2026-09-16; 통합검색 문서명·분류 일치 | SPA 상세 URL/문서 ID/PDF bytes/revision/hash 없음 | metadata verified; original not acquired |
| LSM-MANUAL-V14 | https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual | Servo-filter and default lists both show iX700M DRIVE 400[V] 매뉴얼 Ver1.4, 2026-05-26 | detail fetch 502/timeout; PDF bytes/hash/revision scope 없음 | 2 index snapshots |
| LSM-MANUAL-V13 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | explicit empty-category list shows post no.41, same date 2026-05-26, Ver1.3 | conflicts with two Ver1.4 index snapshots; original binary unavailable | index only; conflict unresolved |
| LSM-CE-DRIVE | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | model example iX700MD1-B-150B; 480 Vac; 15 kW; attachment label and size 238.9K | attachment download timeout; DoC contents/signature/standards/model scope unverified | metadata only |
| LSM-CE-CONVERTER | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | iX700MCV; 480 Vac; 15/37/55/75 kW codes; attachment label and size 234.4K | detail/attachment timeout; DoC contents unverified | metadata only |
| LSM-CAD-IX700M | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M Series outline drawing 2D CAD / 3D STEP, 2026-04-21 | detail and binary DWG/DXF/STEP not acquired; no hash | index only |
| CI-PR239 | https://github.com/useformotor3/ai-discord-bot/pull/239 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45320409623 | merged; exact HEAD e9a15eeaf69e56e610352941f5330604bf78639e; base 1e218a61d09a280d8c4c2ec168c225c6456f215b; Run1497 branch CI 25/25, pytest 189 passed; merge 7d1fe1012bd2f8a8e1540918b43b58b4b41014f5 | none for recorded CI metadata | verified |
| CI-MAIN-1503 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45321136198 | push/main exact merge SHA; success 25/25; main read-back identical | none for recorded CI metadata | verified |

- Run #1481 / ID 45317449785 exact HEAD c395fc5b5b2a393632bb2fbe65b10fd6572b936d success 25/25 remains verified. The later retry implementation does not invalidate its earlier three-PDF artifact.
- Run #1497 recovered C(2026)7861 after three repeated timeouts; binary SHA-256 remains 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security configuration Unknown. Manufacturer inquiry draft_prepared_not_sent.
- CRA only; SIL 3 excluded.

- Revision snapshot correction: two official index URLs (default and Servo-filter) show Ver1.4; only the explicit sca= URL shows Ver1.3. This is an index/cache/query inconsistency, not proof that Ver1.4 binary was downloaded or is the valid deployed revision.


## 33. 2026-11-24 — PR #240 post-merge verification and exact manufacturer source paths

| Evidence ID | Source / exact URL | Confirmed | Acquisition outcome / limitation |
|---|---|---|---|
| CI-PR240 | https://github.com/useformotor3/ai-discord-bot/pull/240 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45329806653 | PR #240 exact HEAD 6f94454ffe41e313c8450918b43b58b4b41014f4, Run #1507 success 25/25, 6 files, reviews/threads 0, JSONL 371/0; merge 36b38bfa5ced2894f3bfb06c226706ce0a9bf38b | verified |
| CI-MAIN-1508 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45329930118 | exact main merge SHA, push success 25/25; PDF artifact 14890384807, ZIP SHA-256 1cb11a4d35de7c922efd5ad2a8d49aada8929875682d20e520c5c9b50f4f19ba; provenance 14891920424 SHA-256 b807be3bd107fc03c70a3fe7f4d59501f1fbcc87e91233286a68600440cc2fc5 | verified |
| SQ-IX700M-DETAIL | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 | item name and update 2026-09-16 | SPA JS shell; no verified document ID/detail URL/PDF |
| LSM-MANUAL-DETAIL | https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12652 | detail URL resolved from Ver1.4 listing link | 502/timeout; no original PDF/hash; version remains unresolved |
| LSM-CE-DRIVE-DOWNLOAD | https://www.lsmecapion.com/bbs/download.php?bo_table=certificate&no=0&page=4&wr_id=12888 | exact attachment link from opened Drive CE page | timeout/direct download failure; PDF not acquired |
| LSM-CE-CONVERTER | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | indexed detail metadata and attachment filename/size | detail/attachment fetch timeout; PDF not acquired |
| LSM-CAD-DETAIL | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | exact iX700M detail URL obtained via preceding post's previous-post link | timeout; DWG/DXF/STEP bytes/hash not acquired |
| LSM-CE-INDEX | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE | multiple iX700M Converter/Drive CE index entries | listing only; does not prove DoC coverage for every SKU |

- Keep Ver1.3/Ver1.4 actual revision Unknown; two list snapshots show Ver1.4, explicit sca= snapshot shows Ver1.3.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security configuration Unknown. Manufacturer inquiry draft_prepared_not_sent.
- CRA only; SIL 3 excluded.

## 34. 2026-11-24 — PR #241 merge and manufacturer-source recheck

| Evidence ID | Source / exact URL | Confirmed | Acquisition outcome / limitation |
|---|---|---|---|
| CI-PR241 | https://github.com/useformotor3/ai-discord-bot/pull/241 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45330332680 | exact HEAD 159f8c16ba50c41e1dd0f3aa0fffba7a3ee1a09d, Run #1509 success 25/25, 6 files +79/-0, reviews/threads 0, JSONL 372/0, merge dd54132fb44ed752b1f7942f4485ee03399a2c2f | verified |
| CI-MAIN-1510 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45333438936 | main push exact merge SHA dd54132fb44ed752b1f7942f4485ee03399a2c2f | in_progress at evidence snapshot; await final conclusion |
| SQ-IX700M-SEARCH | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 ; https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14 | official listing/search results show iX700M user manual, Motion & Servo, update 2026-09-16 | detail is JS shell; no document ID/PDF bytes/hash |
| LSM-MANUAL-INDEX | https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | default + Servo filter Ver1.4; explicit empty-category Ver1.3; same post/date 41 / 2026-05-26 | index conflict only; exact detail wr_id=12652 502/timeout; actual binary revision Unknown |
| LSM-DRIVE-DOC | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 ; https://www.lsmecapion.com/bbs/download.php?bo_table=certificate&no=0&page=4&wr_id=12888 | Drive example iX700MD1-B-150B and attachment metadata 238.9K | detail readable; attachment fetch timeout; PDF not acquired |
| LSM-CONVERTER-DOC | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter iX700MCV metadata, 480Vac and 15/37/55/75kW codes, attachment metadata 234.4K | search-index evidence only; detail/PDF not acquired |
| LSM-IX700M-CAD | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | drawing index item 19, 2D CAD/3D STEP; exact detail URL resolved through previous-post link from PHOX page | detail timeout; DWG/DXF/STEP filenames, bytes and hashes not acquired |

- Do not upgrade metadata to acquired binary evidence. Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown.
- Manufacturer inquiry remains draft_prepared_not_sent; no send/receipt/reply proof.
- CRA only; SIL 3 excluded.

## 35. 2026-11-24 — PR #242 최종 CI 및 공식 iX700M 인증·카탈로그 인덱스 확장

| Evidence ID | 공식 출처 | 목록에서 확인된 내용 | 실제 원본 상태 |
|---|---|---|---|
| CI-1510 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45333438936 | main exact SHA dd54132fb44ed752b1f7942f4485ee03399a2c2f, SUCCESS 25/25 | CI 검증 완료 |
| CI-1511 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45333628512 | PR #242 exact HEAD f9dd8484403f6f91daa94f14b74250965d67e4f6, SUCCESS 25/25 | CI 검증 완료; 문서 보정 후 새 HEAD CI 필요 |
| IX700M-CE-DRIVE | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | iX700MD1-B-150B; D1 1축, B 480Vac, 150 15kW, B BiSS-C/custom; CE DoC 238.9K | 상세 페이지 확인; PDF download timeout, 미확보 |
| IX700M-CE-CV | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | iX700MCV; 480Vac; 15/37/55/75kW; CE DoC 234.4K | 검색/게시물 메타데이터; PDF 미확보 |
| IX700M-UKCA-CV | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 | iX700MCV; 480Vac; 15/37/55/75kW; UKCA DoC 224.1K | 상세 페이지 확인; PDF download timeout, 미확보 |
| IX700M-UL | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=UL | iX700M Series UL Certificate of Compliance listing, 2026-04-13 | 상세/인증서 미확보; file number/scope Unknown |
| IX700M-KC | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate | iX700MD1-B-150B, iX700MD1-B-075B, iX700MCV-B-750/-550 listings | 개별 원본/범위 미확보 |
| IX700M-MANUAL | https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | Default/Servo/empty-sca query snapshots disagree between Ver1.3 and Ver1.4 | binary revision Unknown |
| IX700M-CATALOG | https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 | KR/EN iX700M brochure PDFs, each 10.7MB | detail/download timeout; not acquired |
| IX700M-CAD | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | 2D CAD / 3D STEP drawing listing dated 2026-04-21 | detail timeout; DWG/DXF/STEP binaries not acquired |
| IX700M-SQUARE | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 | iX700M 사용 설명서, update 2026-09-16 | SPA shell; PDF not acquired |

- Listing metadata is not a substitute for original file contents. CE/UKCA/UL/KC are not proof of CRA conformity or EU/EEA supply.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown. Manufacturer inquiry draft_prepared_not_sent.
- CRA only; SIL 3 excluded.


## 36. 2026-11-24 — PR #242 merge and response-control incident

| Evidence ID | Source | Confirmed | Status / limitation |
|---|---|---|---|
| CI-PR242 | https://github.com/useformotor3/ai-discord-bot/pull/242 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45335812764 | exact HEAD e92bb6a0830cbdeb7ed4c05e31faba201c2754a3; Run #1513 success 25/25; 6 files +141/-0; 12 ahead/0 behind; reviews/threads 0; JSONL 374/0 | expected-head squash merged as 3fbc1bcbf669324706c4ae2f882ff7269ae87f48; main read-back identical |
| CI-MAIN-1514 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45338702162 | push event targets exact merge SHA 3fbc1bcbf669324706c4ae2f882ff7269ae87f48 | in progress at snapshot; final result must be read back |
| OPS-NEXT-BUTTON-OMISSION | docs/AI_CONTINUOUS_IMPROVEMENT_AND_NEXT_STEP_PROTOCOL.md v1.1; SESSION_LOG 2026-11-24 entry | required button existed in v1.0 but was omitted from an assistant final response | execution failure: no mandatory final-output component check; v1.1 adds pre-finalization gate and recovery |

- No new iX700M original manual, CE/UKCA/UL/KC certificate, catalogue PDF, or CAD binary was acquired in this step. §35 remains the authoritative manufacturer-source index snapshot; listing metadata is not an acquired file.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown. Manufacturer inquiry draft_prepared_not_sent.
- CRA only; SIL 3 excluded.


## 37. 2026-11-24 — PR #243 merge chain and manufacturer source recheck

| Evidence ID | Source | Confirmed | Status / limitation |
|---|---|---|---|
| CI-MAIN-1514 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45338702162 | main SHA 3fbc1bcbf669324706c4ae2f882ff7269ae87f48; push SUCCESS 25/25 | Final state supersedes in-progress snapshot in §36 |
| CI-PR243 | https://github.com/useformotor3/ai-discord-bot/pull/243 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45338890791 | exact HEAD 9ae09486a10dc374b83ad417fbd09742f0213dc1; 7 files +75/-0; 7 ahead/0 behind; reviews/threads 0; JSONL 375/0; Run #1515 SUCCESS 25/25 | expected-head squash merge 6548eec799c398b35007212e4831d058934fa83b |
| CI-MAIN-1516 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45340565876 | main exact merge SHA 6548eec799c398b35007212e4831d058934fa83b; push SUCCESS 25/25 | post-merge verification complete |
| IX700M-MANUAL-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | Default/Servo list Ver1.4; explicit empty-sca list Ver1.3; same post 41/date 2026-05-26 | Detail wr_id=12652 timeout; PDF and binary revision Unknown |
| IX700M-CE-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | iX700MD1-B-150B; CE DoC PDF 238.9K listed | Attachment click timeout; no PDF bytes |
| IX700M-UKCA-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 | iX700MCV; 480Vac; 15/37/55/75kW; UKCA DoC 224.1K listed | Detail/download timeout; no PDF bytes |
| IX700M-CE-CV-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | iX700MCV CE listing metadata | PDF not acquired |
| IX700M-CATALOG-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 | KR/EN brochure PDFs 10.7MB each listed | Detail timeout; no PDF bytes |
| IX700M-CAD-RECHECK | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive | iX700M 2D CAD/3D STEP listing dated 2026-04-21 | Detail timeout; no DWG/DXF/STEP bytes |
| IX700M-SQUARE-RECHECK | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 | iX700M user manual listing update 2026-09-16 | SPA detail; no original PDF or hash |

- No original manual, CE/UKCA declaration, catalogue PDF, or CAD binary was acquired. Listing metadata must not be represented as acquired evidence.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown. Manufacturer inquiry draft_prepared_not_sent. CRA only; SIL 3 excluded.


## 38. 2026-11-24 — PR #244 merge chain and iX700M manufacturer source recheck

| Evidence ID | Source | Confirmed | Status / limitation |
|---|---|---|---|
| CI-PR244 | https://github.com/useformotor3/ai-discord-bot/pull/244 ; https://github.com/useformotor3/ai-discord-bot/actions/runs/45340773376 | exact HEAD 285b4b705c2bc86b4e7a4602ee7825963770b869; base 6548eec799c398b35007212e4831d058934fa83b; 6 files +70/-0; 6 ahead/0 behind; reviews/threads 0; branch JSONL 376/0; Run #1517 SUCCESS 25/25 | expected-head squash merge 40a92f1b00bf3b0f4e4694895b6399918ee5561f |
| CI-MAIN-1518 | https://github.com/useformotor3/ai-discord-bot/actions/runs/45401343718 | exact main merge SHA 40a92f1b00bf3b0f4e4694895b6399918ee5561f; push SUCCESS 25/25 | post-merge verification complete |
| IX700M-MANUAL-VER1.4 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo | Default and Servo filtered index: Ver1.4, 2026-05-26 | detail wr_id=12652 unavailable; PDF/hash Unknown |
| IX700M-MANUAL-INDEX-CONFLICT | https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= | Explicit empty sca index shows Ver1.3 for post 41, same date | Index snapshot conflict; no binary basis to select revision |
| IX700M-DRIVE-CE-DOC | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 | detail content readable; model iX700MD1-B-150B; 238.9K PDF attachment listed | exact download URL timeout; no PDF bytes/content/signature |
| IX700M-CONVERTER-CE | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | iX700MCV, 480Vac, 15/37/55/75kW; 234.4K PDF listed | metadata only, no PDF bytes |
| IX700M-CONVERTER-UKCA | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 | iX700MCV; 480Vac; 15/37/55/75kW; 224.1K PDF listed | direct page timeout; no PDF bytes |
| IX700M-CATALOGUE | https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 | KR/EN PDF each 10.7MB; attachment date 2025-12-05 | direct page timeout; no PDF bytes |
| IX700M-CAD | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | iX700M 2D CAD / 3D STEP listing dated 2026-04-21 | detail timeout; no DWG/DXF/STEP bytes |
| IX700M-SOLUTION-SQUARE | https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 | manual listing update 2026-09-16 | JavaScript app shell; no document bytes/hash |

- No original manual, DoC, catalogue or CAD binary was acquired. Metadata must not be labelled as acquired evidence.
- Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown. Manufacturer inquiry draft_prepared_not_sent. CRA only; SIL 3 excluded.


## §39. 2026-11-24 — PR #245 이후 main CI 및 제품 원본 자료 상태 재확인

### 저장소 CI
- PR #245 exact HEAD `2b23df758409743ba77e15d1b69bfce08abf941e`; Run #1519 / ID `45401753839`: success 25/25.
- Merge SHA / main HEAD `2b9d924a92bbd497289b9e3afe0dd52df527472b`.
- Main push Run #1520 / ID `45401919091`: event=push, exact SHA match, completed/success, 25/25. Source integrity, compile, CRA traceability, full tests, official CRA PDF/source canaries, evidence and provenance uploads all success.
- CI success is repository pipeline evidence only; not iX700M CRA conformity evidence.

### 제조사 제품 자료 — 메타데이터와 원본 분리
| 자료 | 현재 확인 | 원본 취득 상태 |
|---|---|---|
| iX700M Drive manual Ver1.4 | 공식 default/Servo filter index에 Ver1.4 표시, 다른 empty-sca snapshot은 Ver1.3 | 미취득; detail/download timeout; revision/hash Unknown |
| Drive EU DoC | iX700MD1-B-150B 게시물 및 238.9K 첨부 메타데이터 | PDF bytes/서명/적용범위 미검증, 미취득 |
| Converter CE DoC | iX700MCV, 480Vac 및 용량군, 234.4K 첨부 메타데이터 | PDF bytes/서명/적용범위 미취득 |
| Converter UKCA DoC | iX700MCV, 480Vac 및 용량군, 224.1K 첨부 메타데이터 | PDF bytes/서명/적용범위 미취득 |
| KR/EN catalogue | 각 10.7MB 첨부 목록 | 원본 PDF 미취득 |
| 2D CAD / 3D STEP | iX700M 목록 2026-04-21 | DWG/DXF/STEP 미취득; detail timeout |
| Solution Square manual | iX700M listing update 2026-09-16 | SPA shell; detail/PDF 미취득 |

### Unknowns — 유지
- Actual target SKU / HW revision / FW revision
- Independent sale versus integrated component supply
- EU/EEA market placement and supply chain
- Importer / economic operator identities and roles
- BOM, exact ST MCU part number, memory/communication ICs
- SBOM and OSS/third-party component inventory
- Secure boot, firmware signature, key storage, debug lock, cryptographic controls
- Vulnerability handling process, update policy and support period

Manufacturer inquiry: `draft_prepared_not_sent`; no sending, receipt or response evidence. CRA only; SIL 3 excluded.


## §40. 2026-11-24 — iX700M 공식 자료 재시도 및 최신 CRA 지침 상태

### 원본 취득 재시도
- Manual: 공식 목록의 Ver1.4/Ver1.3 충돌 재확인. 직접 detail 및 `download.php?bo_table=manual&no=0&page=1&wr_id=12652` 접근 실패/비접근. PDF bytes/hash 미확보.
- Drive EU DoC: `iX700MD1-B-150B` 게시물 및 첨부 metadata 확인. detail/attachment fetch timeout; signed PDF, 서명, 적용 EU 법령, 해당 SKU 적용 범위 미확보.
- Converter CE: `iX700MCV` 480Vac, 15/37/55/75kW 게시물 및 234.4K 첨부 metadata 확인. 원본 PDF 미확보.
- Converter UKCA: 동일 계열 게시물 및 224.1K 첨부 metadata 확인. 원본 PDF 미확보. UKCA는 EU DoC 대체 자료로 간주하지 않음.
- Catalogue: KR/EN 각 10.7MB 목록 metadata 확인. 원본 PDF 미확보.
- CAD: iX700M 2D CAD/3D STEP listing metadata만 확인. DWG/DXF/STEP 미확보.
- Search/index references: manual default `https://www.lsmecapion.com/bbs/board.php?bo_table=manual`; Servo filter `https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo`; empty-sca conflict `https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=`; Drive CE `https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888`; Converter CE `https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886`; Converter UKCA `https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893`; catalogue `https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110`.

### 법령·지침 추가 자료
- Regulation (EU) 2024/2847, official EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Guidance C/2026/6013, OJ C 17.11.2026: https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1
- Article 14 applies from 2026-09-11; CRA general application 2027-12-11. Article 14 vulnerability/incident report deadlines are 24h/72h/final 14d for exploited vulnerabilities and 24h/72h/final 1 month for severe incidents.
- Article 13(8)-(9): support period generally at least 5 years (unless expected use shorter); security updates remain available for at least 10 years or remainder of support period, whichever longer.

All product implementation claims remain Unknown pending original documents and manufacturer confirmation. CRA only; SIL 3 excluded.


## §41. 2026-11-25 — PR #248 병합, 제조사 원본 재접근 및 질의서 준비

### PR #248 저장소 검증
- Exact HEAD 8fceea39961ff1076066eaf0bfaf79383a769cbf; Run #1525 / 45404057074 job conclusion success. Job log: pytest 189 passed; CRA traceability PASS; official CRA source PDFs 3종 및 10개 allowlisted sources provenance PASS.
- PR diff 6 files(+93/-0), 7 ahead/0 behind, reviews 0, threads 0, PROJECT_LOG 379 records / invalid 0. Expected-head squash merge SHA dd09fc13cf9076c5cf895f4a8e8727f525847ee4. Main read-back blob contents for report §83/evidence §40/README/session/project log match the merged branch.
- Post-merge main push CI는 연결된 GitHub 도구에서 push-event workflow run 목록을 제공하지 않고 merge SHA combined statuses도 빈 배열이므로 최종 상태 UNVERIFIED. 성공으로 간주하지 않음.

### 제조사 공식 인덱스 재검색 — metadata only
| 자료 | 2026-11-25 재확인 metadata | 원본 binary 검증 |
|---|---|---|
| iX700M DRIVE 400[V] manual | 기본 목록 Ver1.4, Servo 필터 Ver1.4, empty-sca Ver1.3; 모두 2026-05-26 | 상세 페이지 timeout; PDF bytes/hash 및 유효 revision 미확인 |
| Drive EU DoC | iX700MD1-B-150B, CE_DoC-LVDEMC, 238.9K, 2026-04-30 게시 | signed PDF 미취득; 적용 SKU/서명/법령 미검증 |
| Converter CE DoC | iX700MCV, 480Vac, 15/37/55/75kW, 234.4K | PDF bytes 미취득 |
| Converter UKCA DoC | iX700MCV, 480Vac, 15/37/55/75kW, 224.1K | PDF bytes 미취득; EU DoC 대체 아님 |
| KR/EN catalogue | 각 10.7MB, iX700M catalogue 게시물 | PDF bytes 미취득 |
| 2D CAD / 3D STEP | iX700M Series 외형도 게시물, 2026-04-21 | DWG/DXF/STEP bytes 미취득 |
| Solution Square manual | iX700M 사용 설명서 listing update 2026-09-16 | detail은 JavaScript app shell; PDF 미취득 |

### 재접근 결과와 증거 경계
- Search index에서 공식 게시물의 모델명·첨부파일명·크기·게시일을 다시 확인했다. 제조사 사이트 상세 페이지는 timeout이 재현됐고 Solution Square는 JavaScript 실행이 필요하다는 응답을 반환했다.
- 현재 취득된 것은 게시물/index metadata뿐이다. 원본 PDF/DWG/DXF/STEP의 bytes, SHA-256, PDF 서명 및 문서 본문은 취득·검증되지 않았다.
- 관련 공식 목록: https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 ; https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive ; https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4

### 제조사 질의서
- 47문항의 한국어 질의서 초안: reports/LS_MECAPION_iX700M_CRA_MANUFACTURER_INQUIRY_KO.md
- 제품 경계, EU/EEA 공급 및 경제운영자, SKU/HW/FW/BOM/SBOM, MCU, secure boot/signature/key storage/debug, PSIRT/CVD/Article 14, 보안 업데이트, 지원기간, 기술문서, signed EU DoC, 매뉴얼 revision, catalogue 및 CAD 원본을 요청한다.
- 상태: draft_prepared_not_sent. 발송·수신·회신 증거 없음.

### 유지할 Unknown
실제 SKU, 독립 판매/통합 공급, EU/EEA 공급, 수입자·경제운영자, 정확한 MCU/BOM/SBOM, secure boot·서명·키 관리·debug lock, 취약점 처리, 보안 업데이트 방식 및 지원기간은 모두 Unknown.
CRA only; SIL 3 excluded.


## §42. 2026-11-25 — main push CI exact SHA 증거 및 iX700M 원본 취득 재시도

### Main push CI — GitHub Actions API 직접 조회
- PR #248 merge SHA dd09fc13cf9076c5cf895f4a8e8727f525847ee4 → Run #1526 / 45486715925, event push, head_sha exact match, completed/success. Job #138773948774: 15/15 returned steps success (step numbers 1-12,23-25), logs 459 lines, pytest 189 passed.
- PR #249 merge SHA e0a0af3aa7d29acb9fa0e26bddf466af7f3398b5 → Run #1528 / 45487328163, event push, head_sha exact match, completed/success. Job #138776089059: 15/15 returned steps success (step numbers 1-12,23-25), logs 459 lines, pytest 189 passed.
- Both runs: compile and source blob identity PASS; CRA cross-matrix traceability PASS; 3 official Commission CRA PDFs fetched and SHA-256 verified; 10 allowlisted official sources and Article 13(8)/2025/2392 source locators PASS; provenance manifest JSON roundtrip PASS; artifacts uploaded.
- Run #1526: PDF pack 3,070,565 bytes digest 9c7dfa9ddcca2c6d4573350f8487fe3f18897e075417dbd316987afe4a2c0f92; provenance 2,565 bytes digest a03785341ce79aa969f47ddcbcdfb56455079b3829d67f0f59e47d7ffc40ad1.
- Run #1528: PDF pack 3,070,567 bytes digest a917f455caea993d26a77e796fe47f35541647b55150b6400d89973e46897212; provenance 2,565 bytes digest a94615984a6380b86bea590a346a757a4a58eda03a3c1ce93cf2dbf339331ea1.
- These artifact bundles contain official CRA source documents/provenance, not LS Mecapion product manuals, declarations or CAD. Expiry 2026-12-01.
- Warnings only: Node.js 20 action deprecation and node url.parse deprecation. No failed steps. No workflow edit made.

### iX700M manufacturer source retry
- Manual index: Ver1.4 post wr_id=12652 / 2026-05-26; empty category list also shows Ver1.3. Detail page timed out. Original PDF not obtained.
- Drive EU DoC: post wr_id=12888, model iX700MD1-B-150B, 238.9KB metadata only.
- Converter CE DoC: post wr_id=12886, iX700MCV 480Vac 15/37/55/75kW, 234.4KB metadata only.
- Converter UKCA DoC: post wr_id=12893, same Converter family, 224.1KB metadata only; UKCA is not EU DoC.
- KR/EN catalogue: post wr_id=12110, each 10.7MB metadata only.
- CAD: post wr_id=12455, 2D CAD/3D STEP listing dated 2026-04-21; detail timeout, no archive downloaded.
- Public product page states multi-axis modular EtherCAT, AC 380–480V, 4.5–75kW, 16.1–168A/axis. Series information only, not proof of actual delivered SKU.
- No original product bytes, SHA-256, signature or content verification. Source links: https://lsmecapion.com/bbs/board.php?bo_table=manual ; https://lsmecapion.com/bbs/board.php?bo_table=manual&sca= ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 ; https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 ; https://www.lsmecapion.com/bbs/board.php?bo_table=pd_drive

### 질의서 변경
- 47 → 55 questions. Added covered SKU/options and model scope for Drive/Converter CE DoCs, exact Converter rating-to-order-code mapping, lineup and catalogue/manual/CAD mapping, manual revision authority, PDF signature/authenticity and CAD native-file metadata.
- State remains draft_prepared_not_sent.

### Unknown 유지
Actual SKU, EU/EEA supply, economic operators, independent sale/integration, BOM/exact MCU/SBOM, security settings, PSIRT/CVD, update policy and support period remain Unknown. CRA only; SIL 3 excluded.


### 추가 공식 인덱스 조사 — iX700M CE / KC 모델 그룹
- CE index(2026-04-30): #174 iX700MCB; #173 iX700MD1-B-750B/550B/450B; #172 370B/300B; #171 220B; #170 150B; #169 075B/050B/D2-B-045B; #168 Converter iX700MCV. Search-index metadata only; each original DoC binary/signature/scope not verified. Source: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE
- KC index(2026-03-09) separately lists iX700MD1-B-075B/150B/220B/370B, iX700MD2-B-045B, iX700MCV-B-150/370/550/750, iX700MCB-B-8K. KC is not EU DoC evidence and must not be conflated with CE or CRA. Source: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=2&sca=KC
- These lists expand model-specific questions only. They do not establish actual ordered SKU, EU/EEA supply, covered DoC scope or CRA conformity.


## §43. 2026-11-25 — PR #250 및 main push CI 증거

- PR #250 exact head `7d361e1f9973dcd1ec783d7ff3895e0ddf05fe6f`; Run #1535 / 45491181163 success; 15/15 returned steps success; pytest 189 passed; traceability PASS with 382 project log events; 10 official sources/provenance PASS. 2026-5252 source mirror HTTP 503 -> explicit temporary-outage SKIPPED; two other Commission PDFs fetched and hashed. Artifacts: PDF pack 1,906,816 bytes SHA-256 eaf0f8eca6ecc2796813c80430f03c8c658c140d42088aa832d4890415e057eb; provenance 2,565 bytes SHA-256 ed3e3e8468f6675a96fdb1a349dcb644a802154554975ba86e7f4500771a0794.
- Squash merge SHA `ff42addc136836bbbb89bec48bb0c791f031db19`.
- Main push Run #1536 / 45491379142 exact merge SHA success; 15/15 returned steps success; pytest 189 passed; traceability PASS 382; 10 official sources/provenance PASS. Same 2026-5252 HTTP 503 SKIPPED, other two PDFs fetched/hash verified. Artifacts: PDF pack 1,906,818 bytes SHA-256 71937d047f0bc84f8619c92ae2a34b5bfdd50a8b327cbf7b91dbd3afaf35dc29; provenance 2,565 bytes SHA-256 367419dec3c4c0351ab2eaea19578445a0ee21ce1c01d5455970dc6ceb34561b.
- Do not report 3/3 PDFs fetched for #1535/#1536. Earlier #1526/#1528 logs separately confirm 3/3. Temporary source outage is a skipped canary, not a failing test; workflow conclusion success. No actual errors. Node20/punycode/url.parse deprecation warnings.
- PR #250 diff 7 files(+179/-0), no reviews/threads, JSONL 382/0 invalid, expected-head squash merge.
- Product binary status unchanged: manual, signed EU/CE/UKCA DoCs, catalogue and CAD native files not downloaded; metadata only. Actual SKU/EU supply/operator/BOM/MCU/SBOM/security remain Unknown.

 
## §44. 2026-11-25 — PR #251 및 main push Run #1538

- PR #251 exact head `4e2dfd558bb69ab682f4d639a6c8387a1df6bad3`, base `ff42addc136836bbbb89bec48bb0c791f031db19`, 6 files(+54/-0), reviews 0, threads 0, JSONL 383/0 invalid. Run #1537 / 45491681394 success, 15/15 steps, 189 passed, traceability 383 events, 10-source provenance PASS. 2026-5252 timed out; 2/3 PDFs fetched. Merge SHA `4c386689ab42c48e01456b72055217a75a78b14a`.
- Main push Run #1538 / 45505264304 exact merge SHA success, 15/15 steps, 189 passed, traceability 383, 10-source provenance PASS. 2026-5252 HTTP 429 -> SKIPPED; OJ C/2026/6013 and M/606 C(2026)7861 Annex fetched and SHA-256 verified.
- #1537 PDF ZIP 1,906,868 bytes SHA-256 eadca2c5a44c934134c83947d8ec7f248ca41f67f22bffce57b242bd683b158a; provenance ZIP 2,565 bytes SHA-256 daf43bea110d65240c2f73ed659726cced876f9909644c74304a14f4bbce2b7f.
- #1538 PDF ZIP 1,906,816 bytes SHA-256 bab3279433d4178f275a9bf2c3860d28f3dd4f99238d156f31fde4ff5b043afe; provenance ZIP 2,565 bytes SHA-256 34edad760c791d48e390712847d3d0ec01f459515314bbf54918e2a24b8e4e17. Artifacts expire 2026-12-01; Commission source pack, not product binaries.
- No test failures; Node20/punycode/url.parse deprecation warnings. Do not overstate 3/3 PDF acquisition.
- iX700M manual/DoC/catalogue/CAD original binaries still not acquired. Official listing metadata only; detail pages inaccessible/502. Q59 added for product core-functionality classification and Annex III/IV/Article 32 evidence.
- Actual SKU, EU/EEA supply, economic operators, BOM/MCU/SBOM, security settings and classification remain Unknown. CRA only; SIL 3 excluded.

 
## §45. 2026-11-25 — Run #1540 final CI and iX700M source retrieval retry

- Run #1540 / 45505830283, main HEAD `cffd2118d2ce4127e50352650479553cb12c2bdf`: final completed/success; job 138840683889 completed/success; 15/15 steps; 189 passed; CRA traceability 384 events PASS; official provenance 10 sources PASS. Initial in_progress was transient upper-level status propagation after steps completed; final metadata verified success, no rerun.
- CRA PDFs: 2/3 fetched; C/2026/6013 2,709,282 bytes/61 pages SHA-256 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2; M/606 Annex fetched/hash verified; C/2026/5252 HTTP 503 skipped.
- PDF artifact 14972408962: 1,906,817 bytes, SHA-256 c7955d47a2c18f7f4eb9d93678a2a6a559c4e19abae35b98528389b0b1d60c0e. Provenance artifact 14973656717: 2,565 bytes, SHA-256 5468b1744806d109ba475574e5f209f568e83a3137f46f10b6ca9fb7c2c18d38. Expire 2026-12-01; not product binaries.
- iX700M manual/DoC/catalogue/CAD retries: official listing metadata only; manual and DoC/catalogue detail 502, CAD listing timeout. No original signed DoC/PDF/CAD binaries acquired.
- Q60 added requesting controlled official delivery, native format, original filename, size, SHA-256, revision/date, signature verification and SKU coverage. Inquiry 60 questions, draft/not sent.
- Unknowns retained: SKU, EU/EEA supply, economic operators, BOM/MCU/SBOM, security configuration, CRA classification, vulnerability process, update/support term. CRA only; SIL 3 excluded.

 
## §46. PR #253 JSONL 수정 및 Run #1542

- Run #1541 / 45507125350 (초기 PR head c0b3c56...)는 PROJECT_LOG.jsonl line 385 빈 줄로 CRA traceability 실패, cancelled; pytest skipped. 추가 leading newline가 원인.
- JSONL 정규화 후 exact head `e0788eb79d8b5c061b28111f96d9d6419eac950b`: 385 records, 0 invalid, 0 blank.
- Run #1542 / 45507153261 SUCCESS, 15/15 steps, 189 passed, traceability 385 events PASS, 10-source provenance PASS.
- CRA PDFs 3/3 fetched/hash verified. C/2026/5252 fallback=true (1,190,726 bytes, 84 pages, SHA-256 fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234); OJ C/2026/6013 (2,709,282 bytes, 61 pages, SHA-256 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2); M/606 Annex (151,267 bytes, 6 pages, SHA-256 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276).
- PDF artifact ID 14973509955: 3,070,565 bytes, SHA-256 ca03854e1a1fc393292d0676a9e73276fedb8f4e12f91f62ed08f5aba05ba8f7. Provenance artifact ID 14973037845: 2,565 bytes, SHA-256 ac0f673fc8844fcd62977fad35e0c0d1a00d2e2aab8ad78bdbe8f2728c74623c. Expiry 2026-12-01.
- C/2026/5252 fallback copy is not asserted byte-identical to original mirror. These artifacts are CRA source packs, not iX700M product binaries.

 
## §47. PR #253 merge 및 Run #1547 main CI

- PR #253 exact head f1322bccae3042d18d2b922deb3b394c76b48a53, base cffd2118d2ce4127e50352650479553cb12c2bdf, 7 files(+104/-0), reviews 0, threads 0. Run #1546 / 45507438974 SUCCESS, 15/15, 189 passed, traceability 386 events, 10-source provenance, PDF 3/3. Merge SHA e89faa6f9d907edcaf09adbd8f72eb81091ed279.
- Main push Run #1547 / 45507593050 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 386, 10-source provenance, PDF 3/3.
- C/2026/5252 fallback=true, 1,190,726 bytes, 84 pages, SHA-256 fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234. OJ C/2026/6013 SHA-256 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2. M/606 Annex SHA-256 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276.
- Run #1547 PDF artifact 14974835241, 3,070,565 bytes, SHA-256 10baf4713686d065422e9efa744ab7513767313ca23538d355520a3d18f2ce7e; provenance 14972713583, 2,565 bytes, SHA-256 040ebe67de2ba6a9b706f2666e01e74473bfdc1a75e2c613c9fc0df0bb8d92cf; expiry 2026-12-01.
- Manual index Ver1.4 vs Ver1.3 conflict remains; Q61 added. No original iX700M binary acquired. Unknowns retained.

 
## §48. PR #254 / main push Run #1549

- PR #254 exact head 5140882cdf89c3631c9fd9aaa0f0bf2fcedf38fb, 7 files(+56/-0), reviews/threads 0. Run #1548 SUCCESS 15/15, 189 passed, traceability 387 events, 10-source provenance, PDF 3/3. Merge SHA dc1704557e1c3e1071383701d7a4615546814054.
- Main push Run #1549 / 45508166302 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 387, 10-source provenance, PDF 3/3.
- PDF artifact 14974751014, 3,070,565 bytes, SHA-256 c8b1d01f6aba66886a675ac081c978f595ebc5f6c265f3768c40ad2c9be706c7. Provenance 14974510954, 2,566 bytes, SHA-256 0b358609a02446b0615a9a2f07fe591d88b8031ae1460052f2c76e4dd5ba290b. Expiry 2026-12-01.
- C/2026/5252 fallback=true; do not claim primary mirror byte identity. Product originals remain metadata only.
- Q62 added for ST MCU identity/security features, firmware/bootloader, SBOM and vulnerability monitoring. Inquiry 62 questions; draft not sent. Unknowns remain.

 
## §49. PR #255 / main push Run #1551

- PR #255 exact head 7ed4005622cd5c40f8cf0342c175d8bcdad8eca5, 7 files(+53/-0), reviews/threads 0. Run #1550 SUCCESS 15/15, 189 passed, traceability 388 events, provenance 10, PDF 3/3. Merge SHA a8c51348615461f90560a3cce8443cce98c3b24f.
- Main push Run #1551 / 45508666768 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 388, provenance 10, PDF 3/3.
- PDF artifact 14974826452, 3,070,563 bytes, SHA-256 e51c3492d882aeb2f53e30eb5b7fe155a50497bf176e986dd0a68a79d2de1491. Provenance 14974926433, 2,565 bytes, SHA-256 33e66afd51454c1d76a1a49deb0937b7a9c14fddbdf0fd9fdca550d20c069fd5. Expiry 2026-12-01.
- C/2026/5252 fallback=true; no primary mirror byte identity claim. Product binaries remain metadata only.
- Inquiry 62 questions, Q61 manual revision and Q62 ST MCU/security/SBOM/vulnerability evidence, draft not sent. Unknowns retained.

 
## §50. PR #256 / main push Run #1553

- PR #256 exact head ef3af6e9b4725422331737db6779429cb10504b3, 6 files(+46/-0), reviews/threads 0. Run #1552 SUCCESS 15/15, 189 passed, traceability 389 events, provenance 10, PDF 3/3. Merge SHA 0c732caa45e7fac532117e2a658463acc546ee72.
- Main push Run #1553 / 45509151327 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 389, provenance 10, PDF 3/3.
- PDF artifact 14973833111, 3,070,564 bytes, SHA-256 f0db5c8cffd867ff65d7ede817ba7ef9e373f07ea4a54a119fa02be114288714. Provenance 14974127712, 2,565 bytes, SHA-256 90c4ce87a3ba6c2b0075b9c8cfd588fec0152771ef17a9679f2e4731e461ca6a. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. No original iX700M binary acquired; metadata only. Inquiry 62 questions, draft not sent.

 
## §51. PR #257 / main push Run #1555

- PR #257 exact head c7938143b7e474e5e3f38d1675ac7136e408d162, 6 files(+44/-0), reviews/threads 0. Run #1554 SUCCESS 15/15, 189 passed, traceability 390 events, provenance 10, PDF 3/3. Merge SHA 6f26d7166bd8a1208733c82c8fda592e1cfc0f9a.
- Main push Run #1555 / 45509645611 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 390, provenance 10, PDF 3/3.
- PDF artifact 14973917921, 3,070,567 bytes, SHA-256 426c0c7dc9e24e980e7e4117eaa98bd58110a927f620164342b009686c696f22. Provenance 14975071982, 2,565 bytes, SHA-256 daf898155731bbf8b3c4f52ad0198cf174c42d67192259ddbfb5b2e946c5e535. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. No original iX700M product binary acquired; metadata only. Inquiry 62 questions, draft not sent.

 
## §52. PR #259 / main push Run #1558

- PR #259 exact head 764caffd921cfc9007b71843ce096b68c7a65325, 6 files(+44/-0), reviews/threads 0. Run #1557 SUCCESS 15/15, 189 passed, traceability 391 events, provenance 10, PDF 3/3. Merge SHA cabf4bfbb9bd5c4881eb951590813af5aa034ef0.
- Main push Run #1558 / 45510395033 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 391, provenance 10, PDF 3/3.
- PDF artifact 14974454558, 3,070,565 bytes, SHA-256 c58990a02462523067117f101ae053afc473c971d5896477bf568a7e3529ac21. Provenance 14973949377, 2,565 bytes, SHA-256 17778f980d7bc0fd1a3cfd6c028d830e19d7613962eb6898a0dc53ad7d622a23. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. Product binaries remain metadata only. Inquiry 62 questions, draft not sent. Unknowns retained.

 
## §53. PR #260 / main push Run #1560

- PR #260 exact head 432b04c7a7b247296f9799b20886c92474a93fab, 6 files(+43/-0), reviews/threads 0. Run #1559 SUCCESS 15/15, 189 passed, traceability 392 events, provenance 10, PDF 3/3. Merge SHA d18a3a651cf7cd5cecfd99564f4332b8a505f196.
- Main push Run #1560 / 45510915944 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 392, provenance 10, PDF 3/3.
- PDF artifact 14974783287, 3,070,565 bytes, SHA-256 62b97e10e83a9d1791d2f8930e69cd39425bd2322cc5df50db8f1cfd7b325634. Provenance 14974194343, 2,565 bytes, SHA-256 fd75f596c0f42eddb534c43ed5ea41ee3bd74a33cf69bf95148c3a5dee0680ce. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. Product binaries remain metadata only. Inquiry 62 questions, draft not sent. Unknowns retained.

 
## §54. PR #261 / main push Run #1562

- PR #261 exact head 9b64ca980a7818d9eab69724b818e53af95ccc42, 6 files(+44/-0), reviews/threads 0. Run #1561 SUCCESS 15/15, 189 passed, traceability 393 events, provenance 10, PDF 3/3. Merge SHA c7d4d360f4642d788859cf434ed9ddc5409d421d.
- Main push Run #1562 / 45511464761 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 393, provenance 10, PDF 3/3.
- PDF artifact 14976180926, 3,070,565 bytes, SHA-256 6eb56526131bc8ac54d315ff7700b5c9724279691a09cc606ff0b420b4e37e2c. Provenance 14976815077, 2,565 bytes, SHA-256 bfb63f7416eb323b81dbdb6fdc5f304f59e00ecfa3c9edece6c4f27bf6d0a022. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. Product binaries remain metadata only. Inquiry 62 questions, draft not sent. Unknowns retained.

 
## §55. PR #262 / main push Run #1564

- PR #262 exact head 2af04712217d0be2e207ca48865462c882378722, 6 files(+44/-0), reviews/threads 0. Run #1563 SUCCESS 15/15, 189 passed, traceability 394 events, provenance 10, PDF 3/3. Merge SHA a5f1f68351b19557c5444425ae46fb790ddaeec7.
- Main push Run #1564 / 45511961014 exact merge SHA SUCCESS, 15/15, 189 passed, traceability 394, provenance 10, PDF 3/3.
- PDF artifact 14974949830, 3,070,568 bytes, SHA-256 386c94782413af13217eff68e01390e07d411413f13aabaf58cee82a3f3aa6cc. Provenance 14975374608, 2,565 bytes, SHA-256 597b22e21c7da4d7e4454f15b22e6f3ed9748677c41b42c4ffb53a388a7d9057. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. Product binaries remain metadata only. Inquiry 62 questions, draft not sent. Unknowns retained.

 
## §56. PR #263 / main push Run #1566

- PR #263 exact head e4e2601252d56610bf3cf2043603291856ad68e3, 6 files(+44/-0), reviews/threads 0. Run #1565: conclusion success but 14/15 steps succeeded; optional provenance read-only canary timed out for CRA-COMMISSION-GUIDANCE-2026-07-27 and provenance upload step skipped. Other gates: 189 passed, traceability 395, PDFs 3/3.
- Merge SHA 8d2d78b4ccc0ad326813f8e5cb74470bc5738e14. Main push Run #1566 / 45512624809 exact merge SHA SUCCESS, 15/15 steps, 189 passed, traceability 395, 10-source provenance manifest PASS/uploaded, PDFs 3/3.
- PDF artifact 14976576885, 3,070,566 bytes, SHA-256 87d053774d70ba0794947802e98cede863d038cf24b5252541aadd21f1ef1672. Provenance 14976921254, 2,565 bytes, SHA-256 524a92d46f8c368430efafec8f5fd9e92a3ddd8a00895d8e1e46fa501b187c81. Expiry 2026-12-01.
- C/2026/5252 fallback=true; hash only identifies fallback bytes. Product binaries remain metadata only. Inquiry 62 questions, draft not sent. Unknowns retained.


 
## §57. 2026-11-25 — iX700M 공식 목록 재시도 및 PR #266 상태

| ID | 공식 출처 | 새로 확인한 metadata | Binary / 검증 상태 |
|---|---|---|---|
| MFG-IX7M-26 | https://www.lsmecapion.com/bbs/board.php?bo_table=manual | 검색 snapshot: iX700M DRIVE 400[V] Ver1.4, 2026-05-26 | 직접 페이지 502; PDF 미취득. Ver1.3/Ver1.4 충돌 미해결 |
| MFG-IX7M-27 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE | CE 목록 2026-04-30: iX700MCB, Drive 그룹 075B/050B/D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B | 목록 metadata only. SKU별 signed DoC 원본/서명/적용범위 미검증 |
| MFG-IX7M-28 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 | Converter iX700MCV CE DoC 첨부명, 234.4K, 2026-04-30 | PDF bytes 미취득; 서명·적용 법령·표준·SKU 범위 미검토 |
| MFG-IX7M-29 | https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 | Converter iX700MCV UKCA DoC 첨부명, 224.1K, 2026-04-30 | PDF bytes 미취득; 서명·UK 적용범위 미검토 |
| MFG-IX7M-30 | https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 | iX700M KR/EN catalogue, 각 10.7 MB attachment metadata, 2025-12-05 | 원본 binary 미취득; 카탈로그로 실제 SKU/EU supply 추정 금지 |
| MFG-IX7M-31 | https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive&wr_id=12455 | 기존 iX700M 2D CAD/3D STEP listing 단서 재확인 대상 | 상세/첨부 취득 실패; bytes/revision/hash Unknown |

**접근 판정:** 2026-11-25 직접 open 시 manual/CE/catalogue listing은 502 Bad Gateway. 검색 결과에 나타난 제목·파일명·첨부 크기·게시일만 metadata로 기록했다. 검색 snapshot은 원본 파일이 아니며 파일 본문, 서명, 해시, 적용 SKU를 검증하지 못한다.

### 질의서 62문항 개선 메모
- 문항 수는 62개 유지. Q61은 Ver1.3/Ver1.4 충돌의 원인, authoritative revision, revision history, 적용 SKU/HW/FW, 원본 PDF 및 SHA-256을 하나의 추적 가능한 답변으로 요구하도록 구체화한다.
- Q62는 실제 BOM 기준 MCU full part number, firmware build, SPDX/CycloneDX SBOM, secure boot/signing/debug lock/key lifecycle, PSIRT/CVD, vulnerability handling, update/rollback controls 및 support end date를 요구한다. secret key나 비밀번호 원문은 요청하지 않고 redacted/attested evidence를 허용한다.
- 질의서 state: draft_prepared_not_sent. 발송·접수·회신 확인 전 Unknown 해제 금지.

### Unknown 유지
Actual SKU, EU/EEA supply, economic operators, signed DoC coverage, BOM/exact MCU/SBOM, security configuration, CRA classification, vulnerability handling, security update/support period remain Unknown. No iX700M original manual/DoC/catalogue/CAD binary acquired. CRA only; SIL 3 excluded.

### PR #266 / main synchronization
- PR #266 exact head `6529ec9a9234ffdaa5a763a60a7d3df72646eb98`, Run #1570 / 45529191176 success; 189 pytest passed, traceability 397 records, JSONL 397/0 invalid/0 blank.
- Expected-head squash merge `a015dc95f6c59d331275d646306b2b2a2137f437`; main latest commit read-back matches.
- Main push CI UNVERIFIED: Combined Status and commit-associated workflow runs returned empty; do not infer success from PR Run #1570.


### §57.1 질의서 구조 감사 결과
- 질의서 원본의 실제 번호 목록은 90개였다. 과거 “62문항” 기록은 최신 파일과 일치하지 않는 stale count로 확인됐다.
- 질의서를 v2.0으로 통합·재번호화: Q01–Q62, 총 62개, unique ID 62, sequence gap 0. 중복 질문을 묶되 제품경계·EU 공급·SKU·DoC·설계·보안·취약점 범위는 유지했다.
- Q61 = 매뉴얼 Ver1.3/Ver1.4 authoritative revision 확인, Q62 = SKU별 BOM/MCU/FW/SBOM/security/vulnerability evidence matrix.
- 새 초안은 발송 전 상태(draft_prepared_not_sent)이며 제조사 답변은 없음.


 
## §58. 2026-11-25 — PR #267 / Run #1581 및 문서 정규화 병합

- PR #267 exact head `3047df34212f7e5887ac358cd0156a1a75345fb6`, base `a015dc95f6c59d331275d646306b2b2a2137f437`, 7 files(+269/-168), reviews 0, threads 0.
- Run #1581 / 45530155733 completed/success: 15/15 steps, 189 pytest passed, traceability 399 events, PDF 3/3 fetch/hash, 10 official source provenance manifest JSON round-trip/upload.
- Expected-head squash merge `418e526485f1d7c8f43e0f16f471b42b5c2f5a6c`; PR closed/merged; main latest commit read-back identical.
- Main push CI UNVERIFIED: Combined Status and push-run lookup empty; PR Run #1581 must not be represented as main push CI.
- Manufacturer inquiry v2.0 now has exactly 62 globally numbered questions Q01–Q62 after audit found the previous file actually had 90 numbered items. Q61 = manual revision discrepancy; Q62 = per-SKU BOM/MCU/FW/SBOM/security/vulnerability evidence matrix. Draft not sent.
- iX700M product documents remain metadata_only; no original manual/DoC/catalogue/CAD bytes or hash acquired. Unknowns retained.


## §59. 2026-11-25 — iX700M 공식 게시 metadata 추가 검증 및 binary 경계

| Evidence ID | Official listing locator | Listing metadata | Binary state |
|---|---|---|---|
| MFG-IX7M-31 | [Manual Servo list](https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo) | iX700M DRIVE 400[V] Ver1.4, 2026-05-26; detail ID 12652 | metadata_only; detail timeout; old cached snapshot also says Ver1.3 |
| MFG-IX7M-32 | [CE list](https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE) | iX700MCB and Drive Unit groups 075B/050B/D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B | metadata_only; signed PDFs not obtained |
| MFG-IX7M-33 | [Converter CE detail](https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886) | iX700MCV, CE_DoC-LVDEMC iX700MCV.pdf, 234.4K, 2026-04-30 | metadata_only |
| MFG-IX7M-34 | [Converter UKCA detail](https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893) | iX700MCV, UKCA_DoC_LVDEMC iX700MCV.pdf, 224.1K, 2026-04-30 | metadata_only |
| MFG-IX7M-35 | [KR/EN catalogue detail](https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110) | KR/EN brochures, each 10.7M | metadata_only |
| MFG-IX7M-36 | [Drawing list](https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&page=1) | iX700M Series 2D CAD/3D STEP drawing, 2026-04-21, detail ID 12455 | metadata_only; detail timeout |

주의: 파일명/게시일/크기는 metadata이지 binary 자체가 아니다. signed DoC의 진위·서명·적용 법령·SKU scope, manual revision, CAD geometry는 원본 취득 및 검사 전까지 확인되지 않았다.


## §60. 2026-11-25 — PR #269 / 행동규약 v1.3 병합
- PR #269 exact HEAD 0cdffd2ffed3f06b5fc3e910dd9ca18eb2b9a146, Run #1585 / 45531936573 SUCCESS 15/15, pytest 189 passed, traceability 402, PDF 3/3, official source provenance 10개 JSON round-trip/upload.
- Expected-head squash merge SHA / current main: f0e351a8f1df6f24e103b12b73c71defe5b9757d. 7 files(+107/-0), reviews 0, threads 0.
- 행동규약 v1.3 §8.3 main 반영: 단독 버튼을 마지막 UI 요소로 출력, 직접 GenUI.issueNewTurn 호출, CRA only/SIL3 제외 payload, 응답 직전 hard gate.
- Main push CI UNVERIFIED: Combined Status empty, available connector run lookup only returns PR events.
- iX700M product binaries remain unacquired; metadata_only. Actual SKU, EU/EEA supply, economic operators, signed SKU DoC, BOM/MCU/SBOM/security configuration remain Unknown.


## §61. 2026-11-25 — main push Run #1588 및 iX700M 원본 취득 재시도

| 확인 항목 | 결과 | 증거 |
|---|---|---|
| PR #270 exact head | SUCCESS, Run #1587 / 45532177358, 15/15 | `1d815fa2589ba8f55e52c53cf9778a2317b70859` |
| main push | SUCCESS, Run #1588 / 45532289060, 15/15 | main SHA `660eb6d20e62f772272c03971dcd773b03a703f5`, event=push |
| pytest | 189 passed in both | job logs |
| CRA traceability | PASS, 403 project log events | job logs |
| CRA Commission PDFs | 3/3 fetched+hashed | artifacts 14985756045 (PR), 14985077936 (push) |
| official sources provenance | 10 sources; JSON round-trip and upload PASS | artifacts 14984154078 (PR), 14985815057 (push) |

**Actions push lookup:** `GET /repos/useformotor3/ai-discord-bot/actions/runs?head_sha={SHA}&event=push&per_page=100`. This finds post-merge runs missed by the PR-only connector wrapper.

**iX700M original evidence:** manual current filtered list says Ver1.4; alternate indexed snapshot says Ver1.3 for the same date; PDF binary/detail page not obtained. Converter CE/UKCA PDFs, KR/EN catalogue, 2D CAD/3D STEP remain metadata_only. No manufacturer binary or content hash acquired. Inquiry v2.0 Q01–Q62 is draft_prepared_not_sent. Product identity, supply, operators, signed DoC scope, BOM/MCU/SBOM/security configuration remain Unknown.


## §62. 2026-11-25 — PR #271 및 main push Run #1590 증거

| 항목 | PR #271 | main push |
|---|---|---|
| Exact SHA | `47e36dadd2c61a891378a70b168a5cd5e0262c72` | `c9532486ad2aca0ba9538eeffb42d30f76d73ea0` |
| Run | #1589 / 45536881236 | #1590 / 45537026894 |
| Conclusion | SUCCESS | SUCCESS |
| Steps | 15/15 | 15/15 |
| pytest | 189 passed | 189 passed |
| Traceability events | 404 | 404 |
| CRA PDFs | 3/3 fetched+hashed | 3/3 fetched+hashed |
| Official sources | 10, manifest round-trip/upload | 10, manifest round-trip/upload |

PR #271 expected-head squash merge SHA `c9532486ad2aca0ba9538eeffb42d30f76d73ea0` and main read-back matched. Main push Run #1590 verifies post-merge workflow success.

iX700M manual/DoC/catalogue/CAD remain metadata_only; Ver1.4/Ver1.3 manual index discrepancy unresolved; no original binary or content hash. Inquiry Q01–Q62 draft_prepared_not_sent. Product SKU/supply/operators/DoC scope/BOM/MCU/SBOM/security configuration remain Unknown.


## §63. 2026-11-25 — PR #272 / Run #1591 및 main Run #1592 증거

| 확인 항목 | PR #272 exact-head | main branch post-merge |
|---|---|---|
| SHA | `c273e6511012ec6f7d29c87ab71c6da870c2cf46` | `eb5894767cebdc7f956e31252b2d1831ef554a85` |
| Run | #1591 / 45537296095 | #1592 / 45537422906 |
| Job | 138946910010 | 138947346705 |
| Job conclusion | SUCCESS | SUCCESS |
| Returned steps | 15/15 | 15/15 |
| pytest | 189 passed | 189 passed |
| Traceability events | 405 | 405 |
| CRA PDFs | 3/3 fetched+hashed | 3/3 fetched+hashed |
| Official sources | 10, manifest round-trip/upload | 10, manifest round-trip/upload |
| Article 13(8) locator/quote | PASS | PASS |
| Regulation 2025/2392 locators | Annex I(10), Annex II(1) PASS | Annex I(10), Annex II(1) PASS |

PR #272 diff: 6 files, +70/-0, 6 ahead / 0 behind, reviews 0, threads 0. Expected-head squash merge SHA and main read-back: `eb5894767cebdc7f956e31252b2d1831ef554a85`.

| Artifact | PR #272 Run #1591 | Main Run #1592 |
|---|---|---|
| CRA PDF ZIP | ID 14987053784; 3,070,566B; SHA-256 `3a5e66e5ddde36b6debbc5b29fd3b94c5e13ab90839485b6c8d5cdafd423f7af` | ID 14986973967; 3,070,568B; SHA-256 `ac77027d86715aaeb9695aaedd7f3bc88514e4f93705dfcae25ed0e49297a3a0` |
| Provenance ZIP | ID 14987088640; 2,565B; SHA-256 `d504115a03a541f57109f5da37c23b7af9d75635e670fe099625bf8e9f704d92` | ID 14987143761; 2,565B; SHA-256 `d670de307d2299a13d72d1c75bad0e301ed8743d3303471ce201a304646955aa` |

All four artifacts were downloaded and independently SHA-256 checked against the GitHub artifact digests. Main artifact metadata confirms head_branch=main and exact merge SHA. The job/artifact wrapper response does not expose the event property; avoid claiming that this particular response independently returned event=push.

Manufacturer originals remain metadata_only: manual Ver1.4/Ver1.3 index conflict unresolved; Converter CE/UKCA DoC, KR/EN catalogue, 2D CAD/3D STEP binaries and content hashes not acquired. Q01–Q62 draft_prepared_not_sent. All product identity/supply/operator/DoC scope/BOM/MCU/SBOM/security/classification fields remain Unknown.


## §64. 2026-11-25 — PR #273 merge 및 제조사 공식 인덱스 추가 확인

| 항목 | 확인 결과 |
|---|---|
| PR #273 exact HEAD | `c67927926da70cf8089bbf306dfe9261511bb9d0` |
| Exact-head Run | #1593 / 45539484334 SUCCESS, 15/15, 189 passed |
| Traceability | 406 events; cross-matrix PASS |
| CRA PDFs / official sources | 3/3 fetched+hashed; 10 sources, provenance round-trip/upload PASS |
| PR diff/reviews | 7 files, +98/-0, 7 ahead/0 behind, reviews 0, threads 0 |
| Expected-head squash merge | `ce36f290f34a6ce391b91cf3aa6742f48c93e44a` |
| Post-merge main push CI | **UNVERIFIED**; run-list unavailable, combined status empty; no inferred run ID |

**추가 제조사 공식 인덱스 자료 (2026-11-25 재확인)**

| Evidence | 공식 게시물/목록 | 메타데이터 | 원본 |
|---|---|---|---|
| MFG-IX7M-31 | [Manual default list](https://www.lsmecapion.com/bbs/board.php?bo_table=manual), [Servo filter](https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo) | Ver1.4, 2026-05-26 | detail wr_id=12652 timeout; metadata_only |
| MFG-IX7M-31A | [Manual empty-category index](https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=) | same post/date shown as Ver1.3 | index conflict; binary/revision Unknown |
| MFG-IX7M-33 | [Converter CE detail](https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886) | iX700MCV, CE_DoC-LVDEMC PDF, 234.4K, 2026-04-30 | metadata_only |
| MFG-IX7M-34 | [Converter UKCA detail](https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893) | iX700MCV, UKCA_DoC_LVDEMC PDF, 224.1K, 2026-04-30 | metadata_only |
| MFG-IX7M-35 | [KR/EN catalogue](https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110) | KR/EN PDFs, 10.7M each; 2025-12-05 attachment date | metadata_only |
| MFG-IX7M-36 | [Servo Drive drawing list](https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive) | 2D CAD/3D STEP, 2026-04-21, detail ID 12455 | metadata_only; detail timeout |
| MFG-IX7M-37 | [Solution Square Motion & Servo list](https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14) | iX700M user manual updated 2026-09-16 | JS shell only; no file/revision |

The manual listing discrepancy is confirmed by different official index views, not resolved by the index itself. No original manufacturer binary or content SHA-256 acquired. Inquiry Q01–Q62 remains draft_prepared_not_sent. All SKU, EU/EEA supply, operator, signed DoC scope, BOM/MCU/SBOM/security/classification facts remain Unknown.


## §65. 2026-11-25 — PR #272~#274 exact-head / main push CI 및 iX700M 재확인

### Actions CI 증거

| PR | PR HEAD run | PR HEAD SHA | Merge SHA | main push run | main push exact-head |
|---|---|---|---|---|---|
| #272 | #1591 / 45537296095 | `c273e651…` | `eb589476…` | #1592 / 45537422906 | SUCCESS |
| #273 | #1593 / 45539484334 | `c6792792…` | `ce36f290…` | #1594 / 45539588559 | SUCCESS |
| #274 | #1595 / 45539787326 | `b95b64ae…` | `ea1c2b31…` | #1596 / 45539874073 | SUCCESS |

각 6개 run 모두 15/15 step 성공, 189 pytest passed, CRA PDF 3/3 fetch/hash, official CRA source 10건, provenance round-trip/upload PASS. Traceability event counts 405/406/407. Main push run API 응답은 `event=push`, `head_branch=main`, exact `head_sha`, `completed/success`를 직접 반환했다.

PR diff: #272 6 files(+70/-0), #273 7 files(+98/-0), #274 7 files(+87/-0); reviews 0, threads 0. All expected-head squash merges confirmed. Detailed artifact IDs and digests are in PROJECT_LOG event `2026-11-25-CRA-PR272-274-POSTMERGE-PUSH-EXACTHEAD-VERIFIED-MANUAL-INDEX-DIVERGENCE`.

### Manufacturer source recheck

| 자료 | 최신 인덱스 관찰 | binary/hash |
|---|---|---|
| iX700M manual | default/Servo filter search views Ver1.4; direct official empty-category page row 41 Ver1.3; same post date 2026-05-26 | detail timeout; metadata_only |
| Solution Square manual | iX700M 사용 설명서, update 2026-09-16 | JS shell only; metadata_only |
| Converter CE | iX700MCV; CE_DoC-LVDEMC PDF 234.4K, 2026-04-30 | metadata_only |
| Converter UKCA | iX700MCV; UKCA_DoC_LVDEMC PDF 224.1K, 2026-04-30 | metadata_only |
| KR/EN catalog | each 10.7M; 2025-12-05 attachment timestamp | metadata_only |
| 2D CAD/3D STEP | official iX700M drawing listing, 2026-04-21 | detail timeout; metadata_only |

Official listing-view disagreement is not proof of which manual binary is current. Do not use Ver1.3 or Ver1.4 as the controlled product manual until the actual file and revision are acquired. Q01–Q62 remains draft_prepared_not_sent; product facts Unknown.


## §66. 2026-11-25 — PR #275 exact-head CI 증거

| 항목 | 검증 결과 |
|---|---|
| PR / HEAD | #275 / `9231c47c88ff7fe9fc9ce1022eb3023e6af244ba` |
| Actions | Run #1597 / 45540553259, completed/success, 15/15 |
| pytest | 189 passed |
| Traceability | claims 13; interfaces 15; requirements 35; SEC 36; product evidence 15; M606 41; project log events 408 |
| CRA official sources | PDF 3/3 fetched+hashed; official allowlist sources 10; Article 13(8) and Regulation 2025/2392 locators PASS |
| Provenance | 10-source manifest JSON round-trip and upload PASS |
| PDF artifact | ID 14988832738; 3,070,565 bytes; archive SHA-256 `f3a29c9b7ad2c8cbaea65fc9d0c5eb3d47ad348005b3bf6cbe3b98b037786861` |
| Provenance artifact | ID 14989265975; 2,565 bytes; archive SHA-256 `61736ebe2e84c8b8bba92820b4b2f69e132edfcc9d5304a434c45e392e76fabf` |
| Diff / reviews | 7 files, +111/-0; reviews 0; threads 0 |
| PROJECT_LOG | PR branch 408 JSONL records; invalid 0; test reports 408 |

Artifact archive digest equals job log uploaded ZIP digest; do not label it an individual PDF content hash. PR #275 is not merged at the time of this record. If this §66 entry is committed to the PR branch, re-run exact-head CI on the new HEAD before expected-head squash merge.

Manufacturer source statuses unchanged: iX700M manual Ver1.3/Ver1.4 index discrepancy unresolved; Solution Square manual 2026-09-16 item metadata-only; Converter CE/UKCA DoCs, KR/EN catalogue, CAD/STEP originals metadata_only. Q01–Q62 not sent. Product-specific facts remain Unknown.


## §67. 2026-11-25 — PR #275 merge / main push CI 증거

| 증거 | PR Run #1601 | main push Run #1602 |
|---|---|---|
| Run ID | 45540997785 | 45541169420 |
| Exact SHA | `2918f4b62c76d211462428ea32bbbd93a1cbdb61` | `cd00a3b67eea7bf18f5143951f4616659157e15e` |
| Event/branch | pull_request | push / main |
| Result | SUCCESS | SUCCESS |
| Steps / pytest | 15/15 / 189 | 15/15 / 189 |
| Traceability events | 409 | 409 |
| Official CRA PDFs / sources | 3/3 / 10 | 3/3 / 10 |

PR #275 expected-head squash merge SHA `cd00a3b67eea7bf18f5143951f4616659157e15e`.

- Run #1601 PDF artifact 14988823487, 3,070,565 bytes, SHA-256 `b9089acf0f81206b026c1f016e79588361e6c150bb49643cc9316e7bcad2bba0`; provenance artifact 14988593957, 2,565 bytes, SHA-256 `acea80b32d1ed91d9af8d78f54f0ed65fe508cb1882c83261ab1c1a06fb9f8da`.
- Run #1602 PDF artifact 14988324547, 3,070,566 bytes, SHA-256 `bd8018361bb18e5ef326ca9f3e57884bc9b00de97a76f70f4e5945b603ae149d`; provenance artifact 14989940245, 2,565 bytes, SHA-256 `27460361017e0da584e2fc1a021d121ac4e405b6b8133bd6007703a091482fcb`.
- Main PROJECT_LOG 409 valid JSONL records. Manufacturer source files remain metadata_only; Q01–Q62 not sent; product facts Unknown.


## §68. 2026-11-25 — Run #1604 main push CI 및 제조사 증거 재확인

| 항목 | 검증값 |
|---|---|
| Run | #1604 / 45541495434 |
| main exact SHA | 45ec85172d2b5022b0eced1740a2c269b539e55c |
| event / branch | push / main |
| 상태 | completed / success |
| Job / steps | 138960843560 / 15개 모두 success |
| pytest | 189 passed |
| Traceability | claims 13; interfaces 15; requirements 35; SEC 36; product evidence 15; M606 41; PROJECT_LOG events 410 |
| CRA sources | PDF 3/3 fetched+hashed; allowlist 10; Article 13(8) 및 Regulation 2025/2392 locators PASS |
| Provenance | 10-record JSON round-trip 및 upload PASS |

### Artifact archive SHA-256
- PDF ZIP artifact ID 14988843820, 3,070,565 bytes: 5b0f7e5cd59a4955b2a22a8b18d5dd448b4df167119fa72a531bdd4074b9879b.
- Provenance ZIP artifact ID 14988684163, 2,564 bytes: c9d8a97e9db97452444ef64d4f8493cd953317d82dcd499541b124e02f6228ff.

### 개별 PDF content SHA-256
- CRA-GUIDANCE-2026-5252: fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234.
- CRA-GUIDANCE-OJ-2026-6013: 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2.
- CRA-M606-C2026-7861-ANNEX: 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276.

Archive digest와 내부 개별 파일 content hash를 혼동하지 않는다. 위 hash들은 job log에서 확인한 값이며, 제조사 파일 hash가 아니다.

### 제조사 원본 취득 재시도
- 매뉴얼: 기본/Servo 목록 Ver1.4와 빈 category 목록 Ver1.3 충돌 지속. 둘 다 2026-05-26. 원본 PDF/detail page 미취득.
- Converter CE/UKCA: iX700MCV의 480 Vac 및 15/37/55/75 kW 코드군과 첨부 PDF metadata 재확인. 선언서 원본, 서명, 실제 SKU별 적용 범위 미검증.
- Solution Square: iX700M 사용 설명서 2026-09-16 목록 확인, 상세 JS shell only.
- 카탈로그: KR/EN 10.7M 첨부 이름 확인, 원본 binary 미취득.
- CAD/STEP: iX700M 2D CAD/3D STEP 목록 2026-04-21 확인, detail/binary 미취득.

모든 제조사 자료 상태는 metadata_only; 개별 content hash는 미확보. Q01–Q62 미발송. Actual SKU, EU/EEA 공급, 경제운영자, signed SKU DoC coverage, BOM/MCU/SBOM/security configuration 및 CRA classification Unknown 유지.


### §68.1 PR #277 최초 검증 실패와 JSONL 형식 교정
- Run #1605 / 45542964674, PR HEAD cf14a184135bd86be02efa4100a9a7a3894b71c3: failed.
- Job 138965657238: source blob identity 및 compile 성공 후 traceability 검사에서 PROJECT_LOG.jsonl line 411 invalid JSON. 빈 줄이 JSONL record로 해석된 것이 원인. pytest와 live-source/artifact 단계는 skipped.
- 기존 411개 비어 있지 않은 JSON record는 보존하고 빈 줄만 제거, 실패 event를 새 JSONL record로 추가한다. 재검증 전까지 PR #277은 병합 금지.


## §69. 2026-11-25 — PR #277 Run #1606 / main push Run #1607

| 검증 | PR exact-head Run #1606 | main push Run #1607 |
|---|---|---|
| Run ID | 45543168422 | 45543315065 |
| SHA | 56f09b43716dca8bda5391b0939a2c7891701ed9 | e39c95cc993e39cd3950338f07e1ce9282cbc03e |
| Event/branch | pull_request | push / main |
| Result | SUCCESS | SUCCESS |
| Steps / pytest | 15/15 / 189 | 15/15 / 189 |
| Traceability events | 412 | 412 |
| CRA PDFs / official sources | 3/3 / 10 | 3/3 / 10 |
| Provenance upload | PASS | PASS |

Run #1606 archive ZIPs:
- PDF ID 14990341815, 3,070,566 bytes, SHA-256 f5a548236ea06a8bf895c427a30f956af9d4f0e72d025c76e8b32db3d2946482.
- Provenance ID 14990650392, 2,564 bytes, SHA-256 b1fe3375ee1b483bbda8da88066eeb805b5c1e0c63b34fbab79f09613e298c6d.

Run #1607 archive ZIPs:
- PDF ID 14989938648, 3,070,566 bytes, SHA-256 fabb36f5bae932e24742d03672c772010cb0f94d8a4876448ade82eea42efd17.
- Provenance ID 14989474383, 2,565 bytes, SHA-256 d58229a18e47be2095f9d7e3671fa86d3595964f71b9a6013276bef35b15ccea.

Individual PDF content SHA-256: CRA-GUIDANCE-2026-5252 fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234; CRA-GUIDANCE-OJ-2026-6013 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2; CRA-M606-C2026-7861-ANNEX 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276. These are file hashes, not archive hashes.

Run #1605 failure was corrected: strict JSONL physical lines all parse; 412 records, 407 unique non-null event IDs and 5 retained legacy records without event_id. Manufacturer source files remain metadata_only; Q01–Q62 unsent; all product-specific Unknowns remain.


## §70. 2026-11-25 — PR #278 / Run #1608 및 main push Run #1609 증거

| 항목 | PR #278 exact-head | main push |
|---|---|---|
| Run ID | 45543506669 | 45543596033 |
| SHA | de30e11867d22801412b2daba39190791565b390 | bb59d1b38e563d5b72db1e97522a4ae5b79c6d9b |
| Event / branch | pull_request | push / main |
| Result | SUCCESS | SUCCESS |
| Job / steps | 138967457882 / 15/15 | 138967756419 / 15/15 |
| pytest | 189 passed | 189 passed |
| Traceability events | 413 | 413 |
| CRA PDFs / official sources | 3/3 / 10 | 3/3 / 10 |
| Provenance | PASS | PASS |

PR #278 merged=true, squash merge SHA equals main HEAD. Diff 7 files (+100/-0), 1 ahead/0 behind, reviews 0, inline comments 0.

### Artifact archive SHA-256
- Run #1608 PDF ZIP artifact 14989604437, 3,070,565 bytes: 1d2de3fbf53fb8528a61330d2969e75b7995db3b6eb8818abe6f8a2db6ab15eb.
- Run #1608 provenance ZIP artifact 14989674323, 2,565 bytes: bc8af92230d0f7667746633558c60e1522760cee0504c33cc302d50a7f7c860d.
- Run #1609 PDF ZIP artifact 14990725944, 3,070,567 bytes: bbd048563aaa1cba86dbe40065a46cc1e583846137f38bb0380595b20dbbd8e9.
- Run #1609 provenance ZIP artifact 14990043643, 2,565 bytes: 55b15ffc7bd5aada82abe42ffb266aec04228da05b29e7a5e34b2fd804589593.

### 개별 PDF content SHA-256
- CRA-GUIDANCE-2026-5252: fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234.
- CRA-GUIDANCE-OJ-2026-6013: 40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2.
- CRA-M606-C2026-7861-ANNEX: 262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276.

Run #1609 full job log: 459 lines; 15/15 steps success; compileall PASS; 189 pytest passed; traceability claims 13, interfaces 15, requirements 35, SEC 36, product evidence 15, M606 41, project log 413; 10 official sources and provenance upload PASS. ZIP digests are not individual PDF hashes.

### 제조사 원본 취득 게이트
- Manual Ver1.3/1.4 index conflict unresolved; original PDF unavailable.
- Converter CE/UKCA declarations: attachment metadata only; binary/signature/SKU scope not inspected.
- Solution Square iX700M manual: 2026-09-16 listing only; detail JS shell.
- KR/EN catalogues: 10.7M each in listing; binaries unavailable.
- CAD/STEP: official 2026-04-21 listing; binaries unavailable.
- All remain metadata_only; no individual manufacturer-file content hash.

Q01–Q62 unsent. Actual SKU, EU/EEA supply, economic operators, signed SKU DoC scope, BOM, exact MCU, SBOM, security configuration and CRA classification remain Unknown. CRA only; SIL 3 excluded.

## §71. 2026-11-25 — PR #279 / Run #1610 및 main push Run #1611

| 항목 | PR #279 exact-head | main push |
|---|---|---|
| SHA | 49aa465811739fb5eb0dd36877f5875556fc51f5 | 67244a3618ec21495613dedeaf707977effcc783 |
| Run ID | 45548956440 | 45549049529 |
| Job | 138985236009 | 138985534120 |
| Result | SUCCESS | SUCCESS |
| Steps / pytest | 15/15 / 189 passed | 15/15 / 189 passed |
| Traceability | 414 events | 414 events |
| CRA PDFs / sources | 3/3 / 10 | 3/3 / 10 |
| Provenance | PASS | PASS |

Archive hashes:
- Run #1610 PDF ZIP 14993082129: f9451891e7ec142502d39a86b412c7375f8cbd67e0103246e26cd4e51a4d32ac.
- Run #1610 provenance ZIP 14992572830: 593a3df9e6ef84ec22239c5c021f817d50992b783194377cd6e3e4476e6beb71.
- Run #1611 PDF ZIP 14992183761: 8f0c0a2d39b7df4bcc54fc4104749e70a1e28d40ae01344159118af9fd0ec358.
- Run #1611 provenance ZIP 14992473112: 2b38fca1efc50980ada42fa7c61e8f9cd3051aac9b65a4bebd21479ab63d2755.

### Manufacturer source recheck
- Manual list + Servo filter: Ver1.4, 2026-05-26; previously captured empty-category list: Ver1.3. Conflict unresolved; no PDF binary.
- CE Converter DoC: [CE_DoC-LVDEMC] iX700MCV.pdf, 234.4K, 2026-04-30 11:50:26; 480 Vac; listed ratings 15/37/55/75 kW.
- UKCA Converter DoC: [UKCA_DoC_LVDEMC] iX700MCV.pdf, 224.1K, 2026-04-30 12:04:05; same model/rating description.
- Solution Square: iX700M manual listing, update 2026-09-16; JS shell only.
- Catalog: KR and EN files each 10.7M; item attachment date 2025-12-05.
- CAD/STEP: listing dated 2026-04-21; 2D/3D binaries not retrieved.

All manufacturer sources remain metadata_only; no per-file content hash, signature validation, or revision inspection. Official detail fetches encountered 502/timeouts; Solution Square is JS-only; execution environment DNS could not resolve the manufacturer host. Q01–Q62 unsent. Actual SKU, EU/EEA supply, economic operators, SKU-specific signed DoC scope, BOM/MCU/SBOM/security configuration, CRA classification, vulnerability handling and support period remain Unknown. CRA only; SIL 3 excluded.

## §72. 2026-11-25 — PR #280 / Run #1612·1613 및 제조사 자료·기술지원 경로

| 항목 | PR #280 exact-head | main push |
|---|---|---|
| SHA | 504ed25a538e0a61dbc500f3ba86ad60ed167414 | e2b2f39a16b5b41b466d1ec3db7138c49874d70e |
| Run ID | 45549584947 | 45549672737 |
| Job | 138987281166 | 138987569743 |
| Result / steps | SUCCESS / 15/15 | SUCCESS / 15/15 |
| pytest | 189 passed | 189 passed |
| Traceability | 415 | 415 |
| CRA PDFs / sources | 3/3 / 10 | 3/3 / 10 |
| Provenance | PASS | PASS |

Archive SHA-256:
- Run #1612 PDF ZIP 14992078865: 37d1ed30a314c9afa52ddb5f9b78fbe8b1b8a04847a4a5164b78e5d48e05989f.
- Run #1612 provenance ZIP 14991919727: 298a4b0c94af9c31ffd7480158335a05a92ed4f92eadfee1dc0d370a6fe52cee.
- Run #1613 PDF ZIP 14992429240: 685dbace5088cba72eed25c632882dd18bf687ba875b6963eefe683d82057ffc.
- Run #1613 provenance ZIP 14992583792: 9ade5f0f156269d8cf6d0605230718f59eb88b43fc572d9bf29c641300b53d6b.

### Manufacturer acquisition state
- Manual official main/Servo lists: Ver1.4, 2026-05-26; detail click timed out. Earlier empty-category capture: Ver1.3. Conflict unresolved.
- Converter CE/UKCA: official filenames, sizes, timestamps and 480Vac/15/37/55/75kW family metadata confirmed; detail pages 502; no original PDF.
- Solution Square manual: listed 2026-09-16; SPA only, no direct binary URL.
- KR/EN catalogue: filenames and 10.7M each confirmed; detail 502.
- CAD/STEP: official listing 2026-04-21; detail 502.
- All six requested manufacturer evidence groups remain metadata_only. No individual content hashes, signature checks, or binary revision inspection.

### Official technical support
- LS Mecapion general customer center: 1544-5948, 08:30–17:30 (lunch 12:30–13:30 excluded).
- Servo technical-support page lists Seoul region khnam@lsmecapion.com / 070-4343-8207 and 경기 region 070-7772-8422.
- Drive A/S service listing: 053-580-9191.
- Official technical inquiry portal: https://lsmecapion.com/bbs/board.php?bo_table=inquiry&page=1&sca=%EA%B8%B0%EC%88%A0%EB%AC%B8%EC%9D%98&spt=-2831
- Contact path identified; no inquiry/email sent. Q01–Q62 remain draft_prepared_not_sent.

Actual SKU, EU/EEA supply, economic operators, signed SKU-specific DoC scope, BOM/MCU/SBOM/security configuration, CRA classification, vulnerability handling and support period remain Unknown. CRA only; SIL 3 excluded.

### §72.1 PR #281 문서 동기화 CI 후속 검증
- PR #281 exact HEAD 28b1568bd6cc37f724c9180e879a29141714fbdb; Run #1614 / 45550104279, job 138988973316, SUCCESS, 15/15, 189 pytest, traceability 416, PDFs 3/3, sources 10, provenance PASS.
- Merge SHA/main HEAD 5805638439877d2b5dc18d64b7765a67c848a194; main push Run #1615 / 45550213763, job 138989338467, exact SHA + push + main, SUCCESS, 15/15, 189 pytest, traceability 416, PDFs 3/3, sources 10, provenance PASS.
- Run #1614 PDF ZIP 14993188416: b9bd452aad02e17501f2df2b8b0eec5642e4f53d42005c4fb98ec2fd06c5be4d; provenance ZIP 14993430968: b045c9001f0140cc98069fda8ff8b08b915de1abf7ffe36ec58e0663e5a91d36.
- Run #1615 PDF ZIP 14993282289: 9ffdfbdc0a543537516a55bebffa1196b9567e6fdc2069323d84f3fd4f65fc8a; provenance ZIP 14992854400: 63fb6972b2089bf1c8a3c339b6a29501d583538190ed56755c0a353a2c6050dd.
- Archive hashes are not individual PDF hashes. No change to LS Mecapion evidence state. Metadata_only; manual Ver1.3/1.4 unresolved; Q01–Q62 unsent; all Unknowns retained. CRA only; SIL 3 excluded.

### §72.2 PR #282 / Run #1616 및 main push Run #1617, 제조사 자료 조사
- PR #282 exact HEAD 8eb522dad46a421f006ea5d0e75ee707f5b6cf8d; Run #1616 / 45550439993, job 138990088400, pull_request, SUCCESS, 15/15, 189 pytest, traceability 417, PDFs 3/3, official sources 10, provenance PASS.
- Merge/main SHA 127c9ec311e2939059dbff689c3b04f1208e2424; Run #1617 / 45550542045, job 138990414201, push/main exact SHA, SUCCESS, 15/15, 189 pytest, traceability 417, PDFs 3/3, sources 10, provenance PASS.
- Run #1616 PDF ZIP 14992959520: 2374cce45ba7f1e5d29450546fee2d2ea435c0847c5aa57e83a7111176d14d8b; provenance ZIP 14993720613: 66916a98c060444966da1304135572c03f8ec9f788c0ee1547076fce025debf9.
- Run #1617 PDF ZIP 14992829930: db929d6bcf77f075c91abb8fb945f6c06981a431e0343f8b5856788ccf4a6a67; provenance ZIP 14992794878: 504b7af212e3c71948fff36bfa5559819e7d2c09dfb6750975a472793bdd036e.
- These are archive hashes, not individual PDF hashes.
- Manufacturer metadata rechecked: manual list snapshots show Ver1.4 and Ver1.3 on different index/list snapshots (same displayed posting date 2026-05-26); unresolved. CE iX700MCV PDF metadata 234.4K; UKCA iX700MCV PDF 224.1K; KR/EN catalogue PDFs 10.7M each; CAD/STEP entry 2026-04-21 but actual filenames/sizes not exposed.
- Official detail pages return HTTP 502 on open; indexed sources do not expose attachment URLs; no original bytes acquired. Do not guess direct download paths. All manufacturer items remain metadata_only; no per-file SHA-256, signature, signer/certificate chain, or internal revision validation.
- Official support: 1544-5948 (08:30–17:30; lunch 12:30–13:30 excluded), Seoul Servo khnam@lsmecapion.com / 070-4343-8207, Gyeonggi scahn@lsmecapion.com / 070-7772-8422, official technical inquiry portal listed in report §114.6.3. No contact sent.
- Q01–Q62 draft_prepared_not_sent. Actual SKU, EU/EEA supply, economic operators, signed SKU-specific DoC, BOM/MCU/SBOM/security configuration, CRA classification, vulnerability handling, support period remain Unknown. CRA only; SIL 3 excluded.


### §72.3 PR #283 / Run #1618, Run #1619 검증 경계 및 제조사 원본 재시도 (2026-11-25)
- PR #283 closed/merged; base SHA 127c9ec311e2939059dbff689c3b04f1208e2424; exact PR HEAD 616b2a42049930290a42cd495f6c7543b0ba8751; merge commit SHA 0821dac7a336848c1609c4c663860be90eb17337. PR HEAD와 merge SHA를 구분한다.
- Run #1618 / 45551394041, exact PR head 616b2a42049930290a42cd495f6c7543b0ba8751, workflow Isolated Python Tests, job 138993151093, SUCCESS, 15/15 steps, 475 log lines, 189 pytest, traceability 418 events (413 modern IDs + 5 legacy), official CRA PDFs 3/3, official source canary 10/10, Article 13(8)/2025/2392 locator PASS, provenance 10-record round-trip PASS.
- Run #1618 PDF ZIP artifact 14992614962, 3,070,565 bytes, SHA-256 924219a47333054e5459f387df9ad11718d027ae3d7e8ca0224b15736bd5bc0d; provenance ZIP artifact 14993551840, 2,565 bytes, SHA-256 6848d995c1322e8b14f648ec1811d20ee26ee16ac1b7d3b758b2f754ca867810. ZIP digests are not individual PDF digests. Individual PDF SHA-256 values are in report §114.7.2.
- Run #1619 / 45551493565, event=push, branch=main, exact merge SHA 0821dac7a336848c1609c4c663860be90eb17337, job 138993472609, SUCCESS, 15/15, 459 log lines, 189 pytest, traceability 418, PDFs 3/3, sources 10, legal locators PASS, provenance PASS. PDF ZIP 14993487646 / 3,070,565 B / b65d54aa81ccf92eaff22a11bef4f2a5934d730b77f5e4d647e8e13b3b689e38; provenance ZIP 14994630545 / 2,565 B / f8e6b8d28350464ec0916553da120190f896b5da1bb3aa22a1c5e210ce553c5d. Log and artifact metadata digests match.
- Official LS Mecapion manual current board/Servo-filter view lists Ver1.4 (2026-05-26); separate captured official list snapshot shows Ver1.3 on the same displayed date. Conflict unresolved; no binary acquired. CE/UKCA converter entries, KR/EN catalogue and CAD/STEP listing rechecked; detail pages 502/timeout, no attachment bytes. All metadata_only; no manufacturer file hashes/signatures/internal revision inspection.
- No contact sent. Q01–Q62 draft_prepared_not_sent. Actual SKU, EU/EEA supply, economic operators, signed SKU-specific DoC, BOM/MCU/SBOM/security configuration, CRA classification, vulnerability handling and support period remain Unknown. CRA only; SIL 3 excluded.

- PR #284 exact HEAD cf6dec50e9ff952c33491b54aca6db8476151a97; Run #1620 / 45552496961, job 138996681495, pull_request SUCCESS, 15/15, 475 log lines, 189 pytest, traceability 419 (414 modern IDs + 5 legacy), CRA PDFs 3/3, official sources 10, locators PASS, provenance PASS. PDF ZIP 14993483515 / 3,070,564 B / a9acd2d18b9f3fc88d9b1dc04fb893d1472b3416f2440a35238c1cf4941e9456; provenance ZIP 14993882353 / 2,565 B / 7db26d3569b3582853fce0c833f6f776f68e7d74e0851e28b73d70a7d3c2810f. PR #284 exact-head pass; merge/main push still pending.


### §72.4 PR #284 Run #1622 / main Run #1623 closeout
- PR #284 exact HEAD 50e660161e269a75c85cea02d5a125f418e4aa4d; Run #1622 / 45552789733, job 138997652109, pull_request SUCCESS, 15/15, 475 logs, 189 pytest, traceability 420, CRA PDFs 3/3, official sources 10, legal locators PASS, provenance PASS.
- Run #1622 PDF ZIP 14994233122 / 3,070,566 B / SHA-256 003f4c31d72b7d1cfdc2fde0f15bda648ceede66b65d022ed483279d531cc2f2; provenance ZIP 14994597522 / 2,565 B / SHA-256 07b378870f8b1bddc42585bf674a39d8221636837c04f44aeda11dcb9dde49d6.
- Expected-head squash merge SHA / main HEAD: 1c1e0f30b18877dd02b70078ca8863646c371e3b.
- Main push Run #1623 / 45552908709, exact SHA + event=push + branch=main, job 138998000787, SUCCESS, 15/15, 459 logs, 189 pytest, traceability 420, PDFs 3/3, sources 10, legal locators/provenance PASS.
- Run #1623 PDF ZIP 14993579506 / 3,070,566 B / SHA-256 7a6015c038b6e8ce8f47d7cc41c6bee18d7b55bdf624dcb1c9c5a396069a324d; provenance ZIP 14993828989 / 2,564 B / SHA-256 4ffdbcfe5d99425f7a26cdd82cb6a6013e749d19e124e195cb6c1d376b881a43. ZIP hashes are not individual PDF hashes.
- Manufacturer binaries remain metadata_only; Ver1.3/1.4 conflict unresolved; no inquiry sent; Q01–Q62 unsent. CRA only; SIL 3 excluded.


## §72.5 2026-11-25 — 최신 main Run #1625 및 iX700M 공식 자료 재조사
- 기준 main `1b3d253211048411277c4ed04d8c6e0f60263602`; Run #1625 / 45553259298 exact SHA + event=push + branch=main SUCCESS. Job 138999166173, 15/15, 459 logs, 189 pytest, compileall PASS, traceability PASS, 3 CRA PDFs individually hashed, 10 official sources, Article 13(8)/2025/2392 locators and provenance PASS. PDF ZIP 14993674654 / 3,070,566 B / fcc6d0a55060d5f3eb76c6f2e5dabff6ab0c8a90dc0b4df9010d5f7e97a1a6b0; provenance ZIP 14993779653 / 2,565 B / c72506bd9a24e55e09394bf6473ecf0208c7dceda80ee594e4dda4333c8d9e64. Archive hashes only. https://github.com/useformotor3/ai-discord-bot/actions/runs/45553259298
- Manual official-list conflict: Servo-filter list Ver1.4 vs general/page=1 and empty-category snapshots Ver1.3, same 2026-05-26 item; detail `wr_id=12652` timeout/inaccessible. Internal revision unknown.
- CE index lists Drive groups 075B/050B + D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B, Converter iX700MCV and iX700MCB. CE detail metadata verified for iX700MD1-B-150B (238.9K) and iX700MCV (234.4K); no original PDFs/signatures acquired.
- UKCA: indexed iX700M Converter iX700MCV declaration (224.1K) found; no Drive Unit-specific item located in searched official results (not proof of non-existence). UKCA is not EU CE evidence.
- KR/EN catalogue: two listed PDFs, each 10.7M; detail timeout. CAD/STEP listing exists (2026-04-21); detail `wr_id=12455` timeout, no filenames/bytes. All originals metadata_only.
- Failure: detail pages repeatedly timeout/502/inaccessible; indexed results expose metadata but no usable direct attachment URL. No guessed download endpoint. No manufacturer file SHA-256, PDF signature, certificate chain, or embedded revision inspection possible. Q01–Q62 unsent; no contact. CRA only; SIL 3 excluded.
- Sources: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=UKCA ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&page=1 ; https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive


## §72.6 2026-11-25 — iX700M 공식 게시목록 교차검증 및 원본 재취득 시도
- **Manual:** LS Mecapion Servo-filter list Ver1.4 vs general list search snapshot Ver1.3 (same item/date 2026-05-26); additionally LS ELECTRIC Solution Square indexes `iX700M 사용 설명서` updated 2026-09-16. Solution Square SPA/JS page did not expose underlying file URL or revision. No binary; conflict remains unresolved, no revision selected.
- **CE Drive Unit:** official CE list 2026-04-30 includes 075B/050B + D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B groups. 150B detail metadata exposes PDF filename and 238.9K size; other group binary/details not inspected.
- **CE Converter:** iX700MCV detail metadata exposes `[CE_DoC-LVDEMC] iX700MCV.pdf`, 234.4K, B=480Vac and 150/370/550/750 ratings. iX700MCB is a separate CE index row; relationship/detail unknown.
- **UKCA:** iX700MCV Converter detail metadata exposes `[UKCA_DoC_LVDEMC] iX700MCV.pdf`, 224.1K, 2026-04-30, 480Vac and 150/370/550/750 ratings. No Drive Unit-specific iX700M UKCA item located in searched official results; absence is not proven.
- **KR/EN catalogue:** official post lists two PDFs, each 10.7M. **CAD/STEP:** official drawing list shows iX700M 2D CAD / 3D STEP, 2026-04-21. Detail pages did not yield bytes.
- **Acquisition result:** 0 manufacturer binary files acquired in this attempt. All remain `metadata_only`. No file SHA-256, PDF signature/signer/certificate chain, internal revision or SKU-scope verification possible. Official detail pages returned 502/timeout/inaccessible; Solution Square listing requires JS and no file URL surfaced; container DNS resolution to manufacturer host failed. No guessed attachment URL.
- Q01–Q62 unsent; no contact. CRA only; SIL 3 excluded.
- Source URLs: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&page=1 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 ; https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive


### §72.7 2026-11-25 — Solution Square 2026-09-16 문서 재추적 및 iX700M 원본 취득 재시도

- 기준: main HEAD a8eed059bef2446d6f99678fe8e8866e00a2c634; 선행 문서 §114.7.8 / §72.6 확인. 작업 브랜치 docs/cra-solution-square-20260916-recheck-20261125. 문서 전용 변경.
- Solution Square: 공식 Motion & Servo 목록 iX700M 사용 설명서, update 2026-09-16, 목록 순번 5, 검색 인덱스 조회수 172. 공식 통합 검색 결과에도 같은 제목이 문서/사용 설명서, #모션&Servo, 조회수 171로 노출. Sources: https://sol.ls-electric.com/kr/ko/product/category/4?pageNumber=4 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70
- Solution Square 식별/원본: document ID, detail href, attachment filename, byte size, direct download URL not exposed. Direct open returns JS app shell only. Actual source binary 0; relationship to LS Mecapion Ver1.3/1.4 unknown. No inferred Ver1.5.
- Manual conflict: LS Mecapion Servo filter Ver1.4 vs general/page=1 search snapshot Ver1.3, same posted date 2026-05-26; internal PDF revision and controlled copy unknown. No version selected.
- CE Drive Unit: official index groups 075B/050B + D2-B-045B; 150B; 220B; 370B/300B; 750B/550B/450B. 150B detail metadata [CE_DoC-LVDEMC] iX700MD1-B-150B.pdf, 238.9K, 2026-04-30, 480Vac, 15kW code. Other groups remain index-title/date only. CE index: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; 150B detail: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888
- CE Converter: iX700MCV [CE_DoC-LVDEMC] iX700MCV.pdf, 234.4K; 480Vac; rating codes 150/370/550/750. Separate iX700MCB index row; detailed document and MCB/MCV relationship unknown. https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886
- UKCA: iX700MCV Converter [UKCA_DoC_LVDEMC] iX700MCV.pdf, 224.1K, 2026-04-30; 480Vac; ratings 150/370/550/750. No Drive Unit-specific iX700M UKCA item located in searched official sources; not proof of non-existence. https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893
- KR/EN catalogue: official page lists KR and EN brochure PDFs, each 10.7M; no binary. https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110
- CAD/STEP: official drawing list item 19, iX700M 2D CAD / 3D STEP, 2026-04-21; actual filenames/size/bytes not exposed. https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive
- Acquisition/verification: newly acquired manufacturer binary count 0. All product source files remain metadata_only; no per-file SHA-256, PDF signature/signer/certificate chain, internal revision, content or SKU-scope inspection. Solution Square JS shell, official detail inaccessible/502, UKCA index timeout, and search-index no direct attachment href explain failure. No guessed download URL.
- Control: Q01–Q62 draft_prepared_not_sent; no manufacturer email/phone/portal inquiry. Actual SKU, EU/EEA supply, operators, signed SKU-specific EU DoC scope, BOM, exact MCU, SBOM, security config, CRA classification, vulnerability handling and support period remain Unknown. CRA only; SIL 3 excluded.

### §72.8 2026-11-25 — CE Drive Unit 개별 상세 식별자 및 UKCA Drive Unit 재검색

- 기준 main d8b3ec43024368d76175a20742e42a036bf88e9c; §72.7 / 보고서 §114.7.9 선행 확인. CE index rows 169–173, exact model strings 220B / 370B / 300B / 750B / 550B / 450B, UKCA index, CAD list 19를 재검색했다.
- CE index rows 171/172/173: 220B; 370B/300B; 750B/550B/450B (2026-04-30). 공식 검색 결과에서 이 그룹의 개별 wr_id/detail href/attachment metadata를 회수하지 못했다. Index: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE
- 150B 개별 상세: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888; filename [CE_DoC-LVDEMC] iX700MD1-B-150B.pdf, 238.9K. MCV CE/UKCA detail: https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE&wr_id=12886 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893.
- UKCA index https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=1&sca=UKCA&spt=-12859 에서 iX700M Drive Unit 개별 항목 미노출. 검색 범위 내 미발견이며 부존재 증명은 아니다.
- CAD list confirms item 19 / 2026-04-21, but no file identifier or attachment URL: https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive.
- Failure: official detail page requests timed out; index snippets omitted individual hrefs and IDs for grouped CE posts; Solution Square JavaScript shell did not expose document ID or attachment URL. No guessed URL, no new binary, no hash/signature/internal revision/SKU-scope verification. All manufacturer items metadata_only; Q01–Q62 unsent; no contact; product Unknowns unchanged. CRA only; SIL 3 excluded.

### §72.9 2026-11-25 — 매뉴얼 Ver1.3 navigation cross-reference 및 카탈로그 파일 메타데이터
- PEGA2 Ver1.3 official detail search result (wr_id=12651) shows previous-post label 'iX700M DRIVE 400[V] 매뉴얼 Ver1.3'; the target href/wr_id is not exposed. This corroborates the Ver1.3 list snapshot but does not establish the target detail URL or controlled revision. Source: https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651
- Servo filter continues to show iX700M Ver1.4; general/empty-category listing shows Ver1.3, same date 2026-05-26. No PDF bytes/internal revision/approval evidence; conflict unresolved.
- Catalog detail search result reconfirms KR/EN filenames, 10.7M each, DATE 2025-12-05 13:43:50; no binary. https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110
- No guessed Ver1.3 URL, no new manufacturer binary, no file hash/signature/revision/SKU-scope verification. All metadata_only; Q01–Q62 unsent; no manufacturer contact. CRA only; SIL 3 excluded.

### §72.10 2026-11-25 — Solution Square document ID / Ver1.4 wr_id / KC cross-reference

- 기준 main `8898a733ec8328acfa411041d527b0e1517ec678`; report §114.7.11 preflight passed.
- Solution Square: 2026-09-16 iX700M 사용 설명서 title visible on official list (https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=26) and official search result (https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70); direct page is JS shell only. document ID, detail URL, attachment URL and filename not exposed. metadata_only.
- LS메카피온 Ver1.4 manual: actual list anchor resolves to wr_id=12652; official detail URL https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12652 ; listing date 2026-05-26. Detail open returned 502; attachment/binary unavailable. ID confirmed, binary metadata_only.
- Ver1.3: PEGA2 detail wr_id=12651 exposes previous-post label for iX700M Ver1.3, but target href/wr_id not exposed. No inferred numeric ID. Ver1.3/1.4 controlled-revision conflict unresolved.
- Additional KC index cross-check: official KC listing https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=1&sca=KC lists iX700MD1-B-220B (row 113) and iX700MD1-B-370B (row 114), dated 2026-03-09. KC index rows are not CE/UKCA declarations and do not reveal CE detail IDs. No KC detail links/binaries verified for the other requested models.
- CE groups 220B, 370B/300B, 750B/550B/450B remain index-only; UKCA Drive Unit not found in searched index (not proof of non-existence). Confirmed UKCA wr_id=12893 is Converter Unit only.
- Catalog KR/EN filename and size metadata only; CAD/STEP index item 19 only. No original bytes or attachment URL acquired.
- No manufacturer binaries; no hash/signature/internal revision/SKU-scope checks. Q01–Q62 unsent; no manufacturer contact. CRA only; SIL 3 excluded.


### §72.11 2026-11-25 — Ver1.3 공식 목록 행 확인 및 자료 취득 재시도
- 공식 빈 카테고리 목록 `https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=`의 검색 스냅샷은 row 41 `iX700M DRIVE 400[V] 매뉴얼 Ver1.3`, 2026-05-26을 표시한다. PEGA2 Ver1.3 상세(wr_id=12651)의 이전글 표시와 일치한다. row 41의 target href/wr_id 및 첨부 URL은 노출되지 않아 Ver1.3 상세 ID는 Unknown.
- 전체 목록 및 Servo 필터는 Ver1.4를 표시한다. 실제 링크를 따라 확인한 상세 URL은 https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12652. 상세 요청은 timeout/502, 첨부 및 PDF bytes 미취득.
- 같은 게시일 2026-05-26에 목록 필터별 Ver1.3/Ver1.4 표기가 병존한다는 사실은 확인됐으나, controlled copy, 내부 개정번호, 배포/승인 이력 및 우선 적용본은 판정 불가. 어느 쪽도 authoritative 최신본으로 선언하지 않는다.
- Solution Square 2026-09-16 iX700M 사용 설명서는 공식 목록 pageNumber=15/26 및 통합검색 pageNumber=70에서 제목/업데이트일 재확인. JS app shell로 document ID, 상세 URL, attachment URL, filename/revision 미확정. metadata_only.
- CE Drive Unit 220B / 370B / 300B / 750B / 550B / 450B는 공식 인덱스 row 171–173의 그룹 제목만 확인. 개별 detail ID/href 및 첨부 미확정. UKCA Drive Unit은 검색 범위 내 미발견(부존재 증명 아님); 확인된 wr_id=12893은 Converter Unit iX700MCV.
- KR/EN 카탈로그 파일명·각 10.7M·2025-12-05 13:43:50 메타데이터, CAD/STEP item 19·2026-04-21만 확인. 원본 bytes/첨부 URL 미취득.
- 제조사 바이너리 신규 취득 0건. 모든 대상 자료 metadata_only. 개별 SHA-256, PDF 전자서명·서명자 체인, 내부 revision, SKU scope 검증 없음. Q01–Q62 draft_prepared_not_sent; 연락 없음. CRA only; SIL 3 제외.
- 실패 원인: Solution Square JS 앱 셸은 문서 ID/첨부 링크를 반환하지 않고, LS메카피온 세부 페이지는 502/timeout을 반복한다. 검색 스니펫은 그룹 게시물의 개별 링크를 숨긴다. URL 추정/조립 금지 원칙을 유지했다.


### §72.12 2026-11-26 — Solution Square / Ver1.3 row-cache conflict / official detail retry
- Solution Square official list pageNumber=14: iX700M 사용 설명서, updated 2026-09-16, view count 171. Official search pageNumber=70 also indexes title and #모션&Servo. Direct page opens JS shell only; document ID/detail href/attachment URL/file name/revision remain unknown. URLs: https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70. metadata_only.
- LS메카피온 current opened official general manual list shows row 41 = Ver1.4; actual link anchor 42 resolves to wr_id=12652. Detail returns 502. URL: https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12652. ID confirmed, binary metadata_only.
- Older cached empty-category search snapshot showed row 41 = Ver1.3, but the current directly opened general list shows row 41 = Ver1.4. PEGA2 Ver1.3 detail's previous-post label still names iX700M Ver1.3 but hides target href/wr_id. Reclassify old row-41 Ver1.3 claim as stale/cached snapshot evidence only; Ver1.3 detail ID unknown. Do not infer a numeric wr_id. Ver1.3/Ver1.4 controlled revision and approved-release status unresolved.
- CE official index rows 171/172/173 remain grouped: 220B; 370B/300B; 750B/550B/450B. Individual detail href/ID/attachments not recovered; list fetch timed out. KC rows for 220B/370B are not CE declarations.
- UKCA Drive Unit not located in searched official results (not proof of non-existence). wr_id=12893 is UKCA Converter Unit iX700MCV only.
- KR/EN catalog filenames and each 10.7M / 2025-12-05 13:43:50 metadata only; detail fetch timeout. CAD/STEP item 19 / 2026-04-21 metadata only; list fetch 502.
- New manufacturer binaries 0. All manufacturer items metadata_only; no SHA-256, PDF signature/signer chain, internal revision or SKU scope validation. Q01–Q62 draft_prepared_not_sent; no manufacturer contact. CRA only; SIL 3 excluded.
- Failure: Solution Square JS app shell does not expose document links; LS Mecapion detail/list fetches return 502/timeouts; cached index snippets have inconsistent row/title snapshots. No guessed or assembled URLs.


### §72.13 2026-11-26 — 공식 이전글·CE 그룹 및 제조사 원본 재추적
- Solution Square official list pageNumber=14 and search pageNumber=70 index iX700M 사용 설명서 updated 2026-09-16 / #모션&Servo. No document ID/detail href/attachment URL in search snapshot; direct open JS app shell. metadata_only.
- Ver1.3: official PEGA2 detail search result at https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651 exposes previous-post text “iX700M DRIVE 400[V] 매뉴얼 Ver1.3”. The target href/wr_id is not exposed; direct detail fetch timeout. Official empty-sca list snapshot row 41=Ver1.3, while current general list and Servo-filter snapshot row 41=Ver1.4. Title/existence evidence exists, actual ID/attachment/binary unresolved. Do not infer numeric wr_id.
- Ver1.4: current official general list row 41 and Servo listing entry 1; detail URL https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12652 (wr_id=12652) confirmed; detail fetch 502, attachment/binary absent. metadata_only.
- CE official index row 171=220B, row172=370B/300B, row173=750B/550B/450B, dated 2026-04-30. These are grouped index entries, not six individual pages; individual href/wr_id/attachment URLs remain unverified. Direct list fetch 502.
- UKCA Drive Unit not located (absence not proven); wr_id=12893 is UKCA Converter Unit iX700MCV only.
- KR/EN catalogue detail search metadata: KR and EN PDFs each 10.7M, DATE 2025-12-05 13:43:50; direct fetch 502, no bytes. CAD/STEP official Servo Drive list item 19 / 2026-04-21; detail/attachment/binary not recovered.
- Failures: Solution Square JS shell; LS Mecapion direct fetches 502/timeout; index snapshots disagree by date/filter and row numbers cannot identify a detail. Previous-post text lacks target href. No URL/ID guessing.
- New manufacturer binaries 0; manufacturer SHA-256, PDF signature/signer chain, internal revision, SKU scope not verified. Q01–Q62 draft_prepared_not_sent; no manufacturer contact. CRA only; SIL 3 excluded.


### §72.14 2026-11-26 — 공식 이전글 anchor/CE 개별 상세 및 원본 취득 재검증
- PEGA2 Ver1.3 공식 상세 검색 결과는 이전글 텍스트 `iX700M DRIVE 400[V] 매뉴얼 Ver1.3`을 표시하나 실제 anchor href/wr_id는 제공하지 않음; 직접 상세 fetch timeout/502. Ver1.3 locator unknown.
- Ver1.3/Ver1.4 index conflict retained: empty-sca search snapshot row41=Ver1.3; general list row41=Ver1.4; Servo-filter row18=Ver1.4. No row-number inference and no controlled revision conclusion.
- Ver1.4 actual list anchor resolves to wr_id=12652, URL https://lsmecapion.com/bbs/board.php?bo_table=manual&wr_id=12652; detail 502, no attachment/binary.
- Solution Square official page14/search page70: iX700M 사용 설명서, 2026-09-16, 171 views, #모션&Servo. JS shell; document ID/detail/attachment unavailable.
- CE rows 171/172/173 are grouped titles 220B; 370B/300B; 750B/550B/450B. Individual detail href/wr_id/attachment not found. Row170 150B wr_id=12888 is known separately; do not infer adjacent IDs.
- UKCA Drive Unit not located (not proof of absence); wr_id=12893 is Converter Unit iX700MCV only.
- KR/EN catalogue each 10.7M, DATE 2025-12-05 13:43:50; direct detail 502, bytes absent. CAD/STEP item19 date 2026-04-21; detail/attachment/binary absent.
- Failure causes: Solution Square SPA shell; LS Mecapion endpoints return 502/timeouts; search cache/filter snapshots inconsistent; PEGA2 previous-post text omits href. No guessed IDs/URLs.
- Manufacturer binaries acquired: 0. metadata_only; SHA-256, PDF signature/signer chain, internal revision, SKU scope not verified. Q01–Q62 draft_prepared_not_sent; no manufacturer contact. CRA only; SIL 3 excluded.



### §72.15 2026-11-26 — PR #294 exact-head merge / main push verification
- PR #294 exact HEAD `774bfc45f2ca152d18b8236987cb616ab80f9a7f`, Run #1646 / 45718668986 completed/success, 25/25; compile, traceability, pytest 189, CRA PDFs 3/3, 10 official sources, source provenance manifest round-trip/upload all PASS.
- Expected-head squash merge SHA `f7fe9c1151afcb210dbb0c9d589e6d22b7aec603`.
- Main push Run #1647 / 45718795105 exact SHA + event=push + branch=main + completed/success; 25/25, pytest 189, traceability 431, PDFs 3/3, official sources 10, provenance upload PASS.
- Run #1646 artifacts: PDF 15071491072 / SHA-256 db1ff28f7ef29678b1125143f57059b1500e0e2a08ed0a2f1675b045c5cc39ef; provenance 15070583873 / SHA-256 84bff376233110677ba498f8b320354c7a0ddcb38d927a4e6963bb593fd8063e.
- Run #1647 artifacts: PDF 15071680573 / SHA-256 bcf3c51abd37fea815f45b20bd656556ec8d09c3f06ab308967bf252c5b8c71e; provenance 15070574079 / SHA-256 e905328bb69917028525b62fa8a507defd9b74226abba802a4db44e7d9c7ec1b.
- Manufacturer binaries remain 0; metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU-scope validation. PR pipeline green is not manufacturer source acquisition. Q01–Q62 unsent; CRA only; SIL 3 excluded.



### §72.16 2026-11-26 — 공식 인덱스 재검증 및 증거 범위 구분
- PEGA2 Ver1.3 상세 `wr_id=12651` 검색 색인에 이전글 제목 `iX700M DRIVE 400[V] 매뉴얼 Ver1.3`가 표시됨. target anchor href/wr_id는 여전히 미노출. wr_id12651은 PEGA2 게시물 ID.
- 일반/Servo manual 목록 row41=Ver1.4, 빈 분류 snapshot row41=Ver1.3. 충돌 유지, row 번호에서 ID 추정 금지. Ver1.4 wr_id12652 detail 502, attachment/binary 없음.
- CE index rows 171/172/173의 SKU group 명칭을 확인: 220B; 370B/300B; 750B/550B/450B. 개별 상세 ID/href/첨부는 미확보. CE row170 wr_id12888=150B only; CE Converter wr_id12886=Converter, 개별 row ID 유추에 사용하지 않음.
- UKCA wr_id12893은 Converter Unit iX700MCV, attachment label `[UKCA_DoC_LVDEMC] iX700MCV.pdf` (index 224.1K). Drive Unit UKCA 자료는 미발견(부존재 증명 아님). UL index row17의 iX700M Series UL Certificate(2026-04-13)는 별도 인증 종류이며 UKCA 대체 아님.
- Solution Square iX700M 사용 설명서: 2026-09-16, 조회수 171 색인 확인. SPA direct page and search route show JS shell; document ID/detail/attachment unresolved.
- Catalogue wr_id12110: KR/EN filenames each 10.7M, index date 2025-12-05; binaries not fetched. CAD/STEP: drawing list row19/overall row117, 2026-04-21; detail ID/attachment/binaries not fetched.
- Manufacturer binaries newly acquired 0; metadata_only. No manufacturer SHA-256/PDF signature/signer chain/internal revision/SKU scope verification. Failure causes: 502/timeouts, JS shell, hidden previous-post href, grouped CE list, index snapshot mismatch. No guessed IDs/URLs. Q01~Q62 unsent. CRA only; SIL 3 excluded.
- Official URLs: https://lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651 ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; https://www.lsmecapion.com/bbs/board.php?bo_table=catalog&wr_id=12110 ; https://www.lsmecapion.com/bbs/board.php?bo_table=drawing&sca=Servo+Drive ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=3&wr_id=12893 ; https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70.



### §72.17 2026-11-26 — PR #296 exact-head and main push verification
- PR #296 exact HEAD `2eb266711577c64fc182014c649f435b7f7049b4`, Run #1650 / 45728292172, completed/success, 25/25; 189 pytest; traceability 433 events; CRA PDFs 3/3; official sources 10; provenance PASS.
- Diff reviewed: 6 docs, +75/-0; base d0fbdbd6b80688fd29bf420d5b709f6bd64dc493; 6 ahead / 0 behind.
- Expected-head squash merge SHA `6f8dbbe907debd35292c29a2f994d2c0a2ae6b81`.
- Main push Run #1651 / 45728389056: exact merge SHA + event=push + branch=main + completed/success, 25/25; pytest 189; traceability 433; CRA PDFs 3/3; official sources 10; provenance PASS.
- Run #1650 ZIP artifacts: PDF 15075168107 / SHA-256 df76ffe5f4bcfc2190b3271314ae39f029451ea54b7d321a41705bbe0a197776; provenance 15075472328 / SHA-256 4986511e2462ecc0476570c486bcba66f7d0a219a7e27324049a32f3d7fb773c.
- Run #1651 ZIP artifacts: PDF 15074329996 / SHA-256 36236eb3e3e4c897459ab34e94825a5c623a04ab5864c6b4dfe307700f403178; provenance 15075776058 / SHA-256 27eb727cd7589a1a6cd571a706786e98d8aa7840ad5ee8d46bb9f0123a5cd9a8.
- Digests above are GitHub artifact ZIP hashes, not manufacturer document hashes. Manufacturer binaries remain 0 / metadata_only; no manufacturer signature/signer chain/revision/SKU scope verification. CRA only; SIL 3 excluded.



### §72.18 2026-11-26 — 공식 색인 스니펫/열린 HTML 불일치 및 원본 취득 재검증

- 기준 main `792d4e4ba7d5e4652692d86274d8f85474bfeb0b`; §72.17 및 통합 보고서 §114.7.19 read-back 후 문서 전용 조사.
- **매뉴얼 색인:** 공식 검색결과 `manual?page=1` 스니펫은 row41=Ver1.3이라고 표시하지만, 해당 결과를 실제 open한 HTML 본문은 row39~30을 표시하고 row41은 포함하지 않는다. 기본 목록/Servo 필터 스니펫은 row41=Ver1.4, 빈 분류 스니펫은 Ver1.3. 이 불일치는 필터·페이지·캐시/색인 차이로 보존하며 어느 하나를 controlled revision으로 단정하지 않는다.
- **PEGA2 이전글:** PEGA2 Ver1.3 상세 검색결과는 iX700M Ver1.3 이전글 제목을 표시하지만 실제 target anchor href/wr_id 미노출. `wr_id=12651`은 PEGA2 페이지 ID. Ver1.3 ID 추정 금지.
- **Ver1.4:** `wr_id=12652`는 공식 목록 링크에서 확인. detail 502/timeout, attachment URL/bytes 없음.
- **CE:** row171=220B, row172=370B/300B, row173=750B/550B/450B. 개별 detail href/wr_id/attachment 미확정. row170 `wr_id=12888`은 150B만 해당.
- **UKCA:** Drive Unit 개별 DoC 미발견(부존재 증명 아님). `wr_id=12893`은 iX700MCV Converter Unit.
- **Solution Square:** iX700M 사용 설명서 2026-09-16 / 171 views 색인 확인. document ID/detail/API/attachment 미확정, 직접 open은 JS SPA shell. iX700M과 연결이 확인되지 않은 일반 document endpoint를 ID 추정에 사용하지 않는다.
- **KR/EN 카탈로그:** `wr_id=12110`, 파일 각 10.7M, 2025-12-05 13:43:50 메타데이터. bytes 미취득.
- **CAD/STEP:** 공식 Servo Drive 색인 iX700M 2D/3D 항목 2026-04-21. detail ID/attachment/ZIP bytes 미취득.
- **바이너리:** 제조사 원본 신규 취득 0. 모든 자료 metadata_only. 제조사 SHA-256/PDF signature/signer chain/internal revision/SKU scope 검증 없음.
- **실패 원인:** 502/timeout, search snippet와 opened HTML의 row 불일치, previous-post anchor target 미노출, CE 그룹형 목록, Solution Square JS shell.
- **Run #1653:** exact main SHA `792d4e4ba7d5e4652692d86274d8f85474bfeb0b`, event push, completed/success. API job step summary 15/15 success; job log에서 CRA 공식 원문/locator/provenance PASS. 기존 aggregate closeout의 25/25와 구분해 API 응답의 15개 step summary를 기록.
- Q01~Q62 미발송, 제조사 연락 없음. CRA only; SIL 3 제외.


### §72.19 2026-11-26 — Solution Square 검색 색인 교차확인 및 PR #298 CI 종결

- Solution Square 공식 통합검색 pageNumber=70: 전체 1,231건, 문서 28건, `iX700M 사용 설명서` 문서 결과(적용제품 제품명, #모션&Servo, 사용 설명서, 171 views) 및 제품 8건 중 `iX700M` 별도 결과를 확인. document ID/detail/API/attachment URL은 노출되지 않음.
- 공식 category pageNumber=8도 같은 제목/업데이트 2026-09-16을 표시하나 조회수 165; pageNumber=14는 171. 조회수 차이는 검색 시점/캐시 차이로 보고 문서 식별자·버전 증거로 사용하지 않는다. 직접 open은 JS SPA shell. metadata_only.
- PR #298 exact HEAD `82f1d778b48782e98340508081a394979eaf5a86`; diff 6 docs +75/-0; PROJECT_LOG.jsonl nonempty 435 records parse valid. Run #1655 / 45729969157 pull_request success, API step summary 15/15, pytest189, traceability435, CRA PDFs3/3, official sources10, legal locators/provenance PASS.
- Expected-head squash merge SHA/current main `4c948a4b0b829485064ea6f577c9db9b2ce664e6`. Main push Run #1656 / 45730146715 exact SHA/event=push/branch=main completed success; 15/15 API step summaries, pytest189, traceability435, CRA PDFs3/3, sources10, legal locators/provenance PASS.
- Run #1655 artifact ZIPs: PDF 15076785224 / SHA-256 `c126538f8e57946c6dabd37594d8ab679d95cb716129c7ce06f07da77b9678ba`; provenance 15076501353 / SHA-256 `e6f6c4d6e1ddf2781adddf530f7e3f386c540f0422e086f9576d83fa8a488fcb`.
- Run #1656 artifact ZIPs: provenance 15077015001 / SHA-256 `b89b8d65a97acedb32150afcc6a052461be2029d6788565168d6b29667a06064`; PDF 15075774949 / SHA-256 `b55ae7426dab02e131da081805bc51f1afec05700896e297d0b28f233abded5b`.
- Artifact digests are GitHub ZIP hashes, not manufacturer file hashes. Manufacturer originals 0 / metadata_only; manufacturer SHA/signature/signer chain/revision/SKU scope not verified. Q01~Q62 unsent; no manufacturer contact. CRA only; SIL 3 excluded.


### §72.20 2026-11-26 — PR #299 exact-head/main CI 종결 및 증거 상태 유지

- PR #299 exact HEAD `6c661ec285f800de90086cf470f83ab894742309`, 6 docs +55/-0, PROJECT_LOG.jsonl 436 records parse valid. Run #1657 / 45730411555 pull_request completed/success, API step summary 15/15, pytest189, traceability436, CRA PDFs3/3, official sources10, legal locators/provenance PASS.
- Expected-head squash merge SHA/current main `9f77fcdb0498b4ab9dd88e8ac097458c8bd1d75b`. Main push Run #1658 / 45730551230 exact SHA/event=push/branch=main completed/success; 15/15 API steps, pytest189, traceability436, PDFs3/3, sources10, legal locators/provenance PASS.
- Run #1657 artifacts: PDF ZIP 15077015432 / SHA-256 `a694ca8446af464febdd8998b184e4604fe3d3c0fe4d39bd7e83db7a64b4456a`; provenance ZIP 15075564111 / SHA-256 `af3c1d7ce5c0fa78f189fca0b2563269a8a1b89b2cc62d4f9fe18ec61ce5686a`.
- Run #1658 artifacts: PDF ZIP 15076701404 / SHA-256 `51a4a30aa7e42bedf5bcd471a0aa9e19eea4b81e1dc19efe565e9f193db0646f`; provenance ZIP 15076556925 / SHA-256 `9d3dc5c2a0fe3a2b3f323c830e96ac3f7f767bbadd6784d2f345c7ecc20aef12`.
- Artifact digests are GitHub ZIP hashes, not manufacturer file hashes. Manufacturer binaries 0 / metadata_only; SHA/signature/signer chain/internal revision/SKU scope unverified. CRA only; SIL 3 excluded.


### §72.21 2026-11-26 — Run #1654 JSONL 실패·복구 이력

- Run #1654 / 45729917159, PR head `ff84ae63b9053b6351de5b9c54ee1f096fd76219`, completed/failure.
- Failure output: `PROJECT_LOG.jsonl line 435: invalid JSON (Expecting value: line 1 column 1 (char 0))`, traceability validation exit 1. Cause was an empty separator line in JSONL, not a product-source or code test failure.
- Corrective action: removed empty lines, validated 435 non-empty records with invalid=0; corrected exact HEAD `82f1d778b48782e98340508081a394979eaf5a86`; Run #1655 / 45729969157 success, pytest189, traceability435, CRA PDFs3/3, official sources10, legal locators/provenance PASS.
- Prevent recurrence: normalize JSONL line separators and parse every non-empty line before PR creation; preserve failed run ID, exact failure text, corrective commit and rerun result. PR #298 final merged content has valid JSONL.


### §72.22 2026-11-26 — PR #300 exact-head/main CI 종결 및 CI 중복 실행 개선

- PR #300 final HEAD `35e42f29a18ba09086f149ffff911a3026092e2f`, 문서 6개 +75/-0, PROJECT_LOG.jsonl 438 records parse valid.
- Run #1667 / 45731053759 pull_request exact-head completed/success; API steps 15/15, pytest189, traceability438, CRA PDFs3/3, official sources10, Article13(8)/2025/2392 locators and provenance PASS.
- Expected-head squash merge SHA/current main `d510ca516adae596d4ba43fef7cb281fc185afc5`. Main push Run #1668 / 45731210292 exact SHA/event=push/branch=main completed/success; same checks PASS.
- Run #1667 artifacts: provenance ZIP 15076453510 / SHA-256 `89960ced3bb0434633423efbe65c5776bf1aaaf1c80fec539e9204b2a9ed0334`; PDF ZIP 15076309072 / SHA-256 `41c65b5207abb9cf0240d75c5aa8a4f569f574cfc387d3e6f7863156eeacf83f`.
- Run #1668 artifacts: provenance ZIP 15076841160 / SHA-256 `1b87f95bc366db21aff3b202b4d85818664f4641920215eda6a66094b992119c`; PDF ZIP 15076344123 / SHA-256 `334bcc8a484937809fd08542f7320d4636193188bc27b60c264fa74f775bc6de`.
- Artifact hashes are GitHub ZIP hashes, not manufacturer files. Manufacturer binaries 0 / metadata_only; SHA/signature/signer chain/revision/SKU unverified.
- Runs #1660–#1666 were cancelled because sequential multi-file writes created successive branch heads; this is superseded-run overhead, not a failed test. Future multi-file docs updates should use one Git tree/commit/ref update to trigger one final-head CI.
- CRA only; SIL 3 excluded.


### 72.23 2026-11-26 — PR #301 CI 원본 및 iX700M 제조사 locator 재검증

**PR #301 / CI**
- PR REST 원본: merged_at 2026-11-26T00:51:20Z; base `d510ca516adae596d4ba43fef7cb281fc185afc5`; exact head `55535995389441ccba2593ec9232c057ecb9a225`; merge commit `8ed9335322804f663f3546f9f80436144b0b14ab`.
- Run #1669 / 45731538549: pull_request, exact head 위 SHA, completed/success, job 1개, 요약 단계 15/15 success; pytest 189; traceability 439; CRA PDFs 3/3; official CRA sources 10; Article 13(8), 2025/2392 core functionality/Annex I(10)/Annex II(1), provenance PASS.
- Run #1669 ZIPs: PDF artifact 15076642899 / SHA-256 `e2ace762420310db0fea95cb8430c32ed85941cb6efc212878e4e96e12928914`; provenance artifact 15076772558 / SHA-256 `0a74e34ae5e753645445a324405ee33aa8b3e34311f1d55b036b1ab41d8bec9c`.
- Expected-head squash merge SHA `8ed9335322804f663f3546f9f80436144b0b14ab`. Run #1670 / 45731699115: push/main/exact merge SHA/completed/success; 15/15 step summaries, pytest 189, traceability 439, CRA PDFs 3/3, official sources 10, legal locators/provenance PASS.
- Run #1670 ZIPs: PDF 15076782644 / SHA-256 `bb2d0a31041980214c5256b4f2e6ccf2d2ede8239c6b3d5849ad84963eb7b3d9`; provenance 15076708008 / SHA-256 `4d374d72a5661871a294c93052e92e83e52fa3d15d6e9e9bd642c431e4a97e8a`. Digests identify GitHub artifact ZIPs, not manufacturer PDFs.

**Manufacturer locators**
- PEGA2 Ver1.3 `wr_id=12651` actual previous-post anchor text “iX700M DRIVE 400[V] 매뉴얼 Ver1.3” resolves to `bo_table=manual&wr_id=12652`. Target detail remains inaccessible; no attachment or binary acquired. Current official search-index variants show Ver1.3 vs Ver1.4 for the product entry. Direct detail/body proof that `12652` is a Ver1.4 record was not recovered; keep the version conflict unresolved and do not promote the index snippet to controlled-revision evidence.
- CE rows 171/172/173: SKU group labels and 2026-04-30 date confirmed; individual detail href/wr_id/attachments still unknown. `wr_id=12888` is CE 150B only.
- UKCA `wr_id=12893`: iX700MCV Converter Unit only; attachment label `[UKCA_DoC_LVDEMC] iX700MCV.pdf` (224.1K). iX700M Drive Unit UKCA not located; absence not proven.
- Solution Square category result: iX700M 사용 설명서, update 2026-09-16, 171 views; JS shell hides document ID/API/detail/attachment.
- KR/EN catalogue `wr_id=12110`: both named PDF attachments 10.7M, metadata date 2025-12-05 13:43:50; bytes not acquired.
- CAD/STEP index title/date 2026-04-21 confirmed; previous-post anchor target `wr_id=12455`; detail timed out, no ZIP acquired.
- Manufacturer binaries 0; metadata_only. No manufacturer-file SHA/signature/signer chain/revision/SKU verification. Q01–Q62 unsent; CRA only; SIL 3 excluded.


### 72.24 2026-11-26 — PR #302 exact-head/main push CI 종결
- PR #302 exact HEAD `0404622e767f657f674cafc8f715397b0d8c63ec`, 6 docs +63/-0, JSONL 440 valid. Run #1671 / 45749576500 pull_request completed/success, 15/15 steps, pytest189, traceability440, CRA PDFs3/3, official sources10, legal locators/provenance PASS.
- Expected-head merge/current main `8a06fa5b3790ebf14d743f9cdd5c8e6b66bc39c5`; Run #1672 / 45749657309 push/main exact SHA completed/success, 15/15 steps, same checks PASS.
- Artifact ZIP hashes: #1671 PDF `743a3a99452d44dc4133729bbcd5721e2b24a6dd8abd608ffa872b064c0b94dd`, provenance `b68d9797afd22ed07216c394407fdf05aed8a13e6d16f33cbc264f051ef79322`; #1672 PDF `b84bfec3e0f8903c9da1297e7e0aefe50d8433dbc49c84a6ddd21d2570cfd1d7`, provenance `95b892f0964b7441a3db9d46b6abfca96bdbbd5ad0a43070b283d1ae449d7e88`. These are GitHub ZIP hashes, not manufacturer binaries.
- Manufacturer originals 0 / metadata_only. CRA only; SIL 3 excluded.


### §72.25 2026-11-26 — PEGA2/iX700M anchor 충돌 및 CE #171~#173 상세 locator 재검증

- Baseline main: `8272efeda10f8432cf504d799e8698a9590d278c`.
- PEGA2 Ver1.3 official detail `manual&wr_id=12651`: previous-post label says “iX700M DRIVE 400[V] 매뉴얼 Ver1.3”; attachment metadata `PEGA2_KOR_Ver1.3_260826.pdf`, 6.6 MB, 2026-08-28.
- Official manual list row 41 labels iX700M as Ver1.4 (2026-05-26); clicking the row resolves to `manual&wr_id=12652`. The destination detail fetch timed out/Internal Error. Therefore the visible previous-post label and current index row disagree; whether stale label, cache, or actual version/revision mismatch remains UNRESOLVED. No PDF bytes acquired.
- CE index rows #171/#172/#173 identify respectively 220B; 370B+300B; 750B+550B+450B, dated 2026-04-30. Individual href/wr_id and attachment names/binaries were not exposed by the accessible index/search result. Do not infer from #170 `wr_id=12888` (150B, different SKU).
- UKCA `wr_id=12893` remains iX700MCV Converter Unit only, not Drive Unit evidence.
- Manufacturer binaries acquired this turn: 0. PEGA2/iX700M/CE items remain metadata_only; no manufacturer SHA-256, PDF signature, signer chain, internal revision, or SKU-scope validation.
- Official references: https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651 ; https://lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE .
- Q01~Q62 unsent; CRA only; SIL 3 excluded.


### §72.26 2026-11-26 — PR #304 exact-head/main push CI 종결
- PR #304 exact HEAD `7e10032519fd224419f8ba7e00ed9d9c0c559a6f`; Run #1675 / 45751710487 pull_request exact-head completed/success, 15/15 steps, compileall PASS, pytest189, traceability442, official CRA sources10, Article 13(8)/2025/2392 core-functionality/Annex I(10)/Annex II(1) locators and provenance PASS.
- Expected-head squash merge/current main `3d83dd2fb5ea5d49b12897d66b76d695b24f9b64`. Main push Run #1676 / 45751795978 exact SHA/event=push/branch=main completed/success, 15/15 steps, same validation PASS.
- Run #1675 artifact ZIPs: PDF 15086360629 / SHA-256 `991fccd6301a3e8b287093943f6b6738b9109ce0baa705e8d1b68b083b4a6d54`; provenance 15085942073 / SHA-256 `ff2381bf5801b6851816238f3b95150c1e6352f2990d17e8a4fc984beb001100`.
- Run #1676 artifact ZIPs: PDF 15086100969 / SHA-256 `48e323f91e5f11875f67a18f43308719e756866feb018c26a8bc714b63cd1068`; provenance 15085991303 / SHA-256 `4058633b3dae4b9e9baa85160fb6d7691e94fafa0fdabd737c3bf03b40498709`.
- Digests are CI artifact ZIP hashes, not manufacturer source files. Manufacturer binaries 0 / metadata_only; no manufacturer hash/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.27 2026-11-26 — Solution Square PEGA2 doc 32720 / iX700M / CE #171~#173 추가 교차검증

- Baseline main `73e48a0e786d7264bd750b8a85959d14d12baecd`.
- **PEGA2 Solution Square:** official document detail ID `32720`, title PEGA2 User Manual, update 2026-09-23. Search-index attachment metadata: `PEGA2_ENG_Ver1.3_260831.pdf`, English, 6.0 MB, applicable product PEGA2 series. Detail page itself is a JS shell; actual attachment href/storage path and bytes unavailable. Do not derive download path from doc ID.
- **PEGA2 KR counterpart:** LS Mecapion detail `manual&sca=Servo&wr_id=12651` shows `PEGA2_KOR_Ver1.3_260826.pdf`, 6.6 MB, metadata date 2026-08-28. Different language/filename/date/size; not treated as identical to Solution Square EN PDF.
- **iX700M version conflict:** PEGA2 detail wr_id=12651 previous-post label says iX700M Ver1.3. Basic official manual list row 41 and Servo-filter list show Ver1.4; empty-category snapshot shows Ver1.3. The row target previously followed from list anchor is wr_id=12652, but its detail/attachment is inaccessible. Version/revision remains UNRESOLVED; no iX700M binary acquired.
- **Solution Square iX700M:** category/search index confirms “iX700M 사용 설명서”, updated 2026-09-16, views 171. No detail ID/attachment filename exposed. JS SPA shell only. Do not reuse PEGA2 doc ID 32720.
- **CE:** #171=220B, #172=370B/300B, #173=750B/550B/450B, date 2026-04-30. Individual href/wr_id/attachments still unknown. #170 comparator `wr_id=12888` is iX700MD1-B-150B only, attachment `[CE_DoC-LVDEMC] iX700MD1-B-150B.pdf`, 238.9 KB, 2026-04-30 11:55:32; not used to infer adjacent IDs.
- Manufacturer binaries acquired this turn: 0. All PEGA2/iX700M/CE evidence remains metadata_only; SHA-256, PDF signature, signer chain, internal revision and SKU scope not verified.
- Sources: https://sol.ls-electric.com/us/en/product/document/32720 ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo&wr_id=12651 ; https://lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca= ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&page=4&wr_id=12888 .
- CRA only; SIL 3 excluded; Q01~Q62 not sent.


### §72.28 2026-11-26 — PR #306 exact-head/main push CI 종결
- PR #306 exact HEAD `0cd50a8acc78bb49de8a04bbb8600e209ec68958`; Run #1679 / 45752937289 pull_request exact-head completed/success, 15/15 steps, compileall PASS, pytest189, traceability444, official CRA sources10, Article 13(8)/2025/2392 core-functionality/Annex I(10)/Annex II(1) locators and provenance PASS.
- Expected-head squash merge/current main `770fc317d21a25dc99eb209d1a9644f2d1257ea8`. Main push Run #1680 / 45753033948 exact SHA/event=push/branch=main completed/success, 15/15 steps, same validation PASS.
- Run #1679 artifact ZIPs: PDF 15086810508 / SHA-256 `0498d87ed6f820353877fa59e431429ee355851a141339e93b1bb86ace06cd8c`; provenance 15085779588 / SHA-256 `ee367ac003a2c3c20cf3ca17b6effa2cd4cd0534cac034cb7b5346948e99c57b`.
- Run #1680 artifact ZIPs: PDF 15085918922 / SHA-256 `4ef3a706cc3083cf6455e206d88d03cde911042ab6d780d758fb1ca4f4cbe4d2`; provenance 15086795720 / SHA-256 `38e14b7f477a0eab1a5bafef7ce2457ca0d197335cf36d8b628ab1a8207bcf3c`.
- Digests are GitHub CI artifact ZIP hashes, not manufacturer source files. Manufacturer binaries 0 / metadata_only; no manufacturer hash/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.29 2026-11-26 — 공식 공개 색인 재검증: PEGA2 32720 / iX700M / CE #171~#173
- Solution Square PEGA2 doc 32720 공식 색인: `PEGA2_ENG_Ver1.3_260831.pdf`, EN, 6.0 MB, update 2026-09-23, PEGA2 series. Detail URL은 JS shell만 반환; 실제 attachment href/API object/download URL/bytes 없음.
- Solution Square iX700M manual 2026-09-16: 공식 category/search index title/date 확인. 개별 document ID/detail href/attachment UNKNOWN; PEGA2 ID 32720 전용 금지.
- LS메카피온 공식 manual index: iX700M DRIVE 400[V] Ver1.4 (2026-05-26), PEGA2 Ver1.3 (2026-04-01). wr_id=12652 상세/첨부는 이전 timeout/502 이후 반복 호출하지 않았으며 내부 revision은 UNRESOLVED.
- CE index #171=220B; #172=370B+300B; #173=750B+550B+450B, all 2026-04-30. 개별 detail href/wr_id/attachment name not exposed. #170 wr_id=12888 is 150B only; no adjacent-ID inference.
- New manufacturer binaries 0; metadata_only. No manufacturer SHA-256, PDF signature, signer chain, revision or SKU-scope verification.
- Sources: https://sol.ls-electric.com/us/en/product/document/32720 ; https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14 ; https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70 ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual ; https://www.lsmecapion.com/bbs/board.php?bo_table=manual&sca=Servo ; https://www.lsmecapion.com/bbs/board.php?bo_table=certificate&sca=CE .
- CRA only; SIL 3 excluded; Q01~Q62 not sent.


### §72.30 2026-11-26 — PR #308 exact-head/main push CI 종결
- PR #308 exact HEAD `6f7e7c39ae0e996de8256961a6f92bf7637d1642`; Run #1683 / 45761338380 pull_request completed/success, 15/15. Compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC crosswalk16/M606 mapping41/PROJECT_LOG events446; 3 Commission PDF sources and 10 official sources PASS; Article 13(8), 2025/2392 core-functionality, Annex I(10), Annex II(1) locators/provenance PASS.
- Run #1683 artifacts: PDF ZIP 15088989120 / SHA-256 `835474c34e153ea97f2458e154a9259ac3cb5d24e711d8b0c7321d3507bb7a2e`; provenance ZIP 15089233747 / SHA-256 `5e3325250e2cbe59eb7d9b59895902c5847785a54f288f063969b0a5496c7a2b`.
- Expected-head squash merge SHA/current main `ca405190093fca8796784d98abb4069d8a932a5c`. Run #1684 / 45761461078 main push exact SHA completed/success, 15/15, same test/traceability/source/legal checks PASS.
- Run #1684 artifacts: PDF ZIP 15088984387 / SHA-256 `451f82ffd4190993f047cca32d7b0ff4052ba07db75424e1c1bd045799b12ff8`; provenance ZIP 15089243856 / SHA-256 `1d7d333e507cf36f5c1f1c8654e4a467d6960321b26fd5f6857bddb4789cbe2a`.
- Digests are CI artifact ZIP hashes, not manufacturer-source PDF hashes. Manufacturer originals 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.31 2026-11-26 — PR #309 exact-head/main push CI 종결
- PR #309 exact HEAD `b09b5206b52cec5271ddffa3ff02fd6ab9f5f870`; Run #1685 / 45761654876 pull_request completed/success, 15/15. Compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC crosswalk16/M606 mapping41/PROJECT_LOG events447; Commission PDFs3/3 and official sources10 PASS; Article 13(8), 2025/2392 core-functionality, Annex I(10), Annex II(1) locators/provenance PASS.
- Run #1685 artifacts: PDF ZIP 15090207124 / SHA-256 `15b2751d0c160ede66d614e1832cef789ec67d0581d38e4fea1a6818d4055d48`; provenance ZIP 15089707959 / SHA-256 `059f9472dd0219a575745ab328da68143dde489717da87a43207708abfbd754e`.
- Expected-head squash merge SHA/current main `b04b7b0dd0e0d774af1c755fb5595316b2106a4c`. Run #1686 / 45761741257 main push exact SHA completed/success, 15/15, same checks PASS.
- Run #1686 artifacts: PDF ZIP 15090117382 / SHA-256 `e14a780fe2dc9e74f0db971cf98548262c1c1008976946915f5e18f118690eca`; provenance ZIP 15089812889 / SHA-256 `31036d381b3ff236a6c7fcd4220c811f068b74475b907842e8f6ffe12d442955`.
- Digests are CI artifact ZIP hashes, not manufacturer-source PDF hashes. Manufacturer originals 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.32 2026-11-26 — PR #310 exact-head/main push CI 종결
- PR #310 exact HEAD `119ee7207ea6ea8155ae80b0ae9eae1052690c5b`; Run #1687 / 45761944295 pull_request completed/success, 15/15. Compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC crosswalk16/M606 mapping41/PROJECT_LOG events448; Commission PDFs3/3 and official sources10 PASS; Article 13(8), 2025/2392 core-functionality, Annex I(10), Annex II(1) locators/provenance PASS.
- Run #1687 artifacts: PDF ZIP 15090401004 / SHA-256 `bdf68fb611e925996762a8fb46bf19b61b28b49e2d19f56946b1d92b8f936227`; provenance ZIP 15089898857 / SHA-256 `dccc11b5e272060cac5778424886b86f10b1075ee896760231dccce2ffc6ddbd`.
- Expected-head squash merge SHA/current main `7889937298c125cbbc402af29bb50f10591f361f`. Run #1688 / 45762058166 main push exact SHA completed/success, 15/15, same checks PASS.
- Run #1688 artifacts: PDF ZIP 15089799317 / SHA-256 `970def930b58444aa820e61b64e22190ad94bc4e16f6a89e327d7d6a357317d2`; provenance ZIP 15090199027 / SHA-256 `a4291bd943bbd4e390351806061f1f131c3acd687724aafdf9f71f5c1bd360c4`.
- Digests are CI artifact ZIP hashes, not manufacturer-source PDF hashes. Manufacturer originals 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.33 2026-11-26 — PR #311 exact-head/main push CI 종결
- PR #311 exact HEAD `8925fc79ba996030c9a0dd406eef5885342f1d23`; Run #1689 / 45762235936 pull_request completed/success, 15/15. Compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC crosswalk16/M606 mapping41/PROJECT_LOG events449; Commission PDFs3/3 and official sources10 PASS; Article 13(8), 2025/2392 core-functionality, Annex I(10), Annex II(1) locators/provenance PASS.
- Run #1689 artifacts: PDF ZIP 15090401004 / SHA-256 `bdf68fb611e925996762a8fb46bf19b61b28b49e2d19f56946b1d92b8f936227`; provenance ZIP 15089898857 / SHA-256 `dccc11b5e272060cac5778424886b86f10b1075ee896760231dccce2ffc6ddbd`.
- Expected-head squash merge SHA/current main `6ade255c74fecde2187df5898d544406e30ed94f`. Run #1690 / 45762318365 main push exact SHA completed/success, 15/15, same checks PASS.
- Run #1690 artifacts: PDF ZIP 15090700402 / SHA-256 `85b5026155d485f2f8cfe39dc56243b6ad5ec60d7debd2c15dce53d7503aaa7d`; provenance ZIP 15090710443 / SHA-256 `c53806d14334a3477e093fea68270189ec707763c9e569268e95438bdef8c41e`.
- Digests are CI artifact ZIP hashes, not manufacturer-source PDF hashes. Manufacturer originals 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.34 2026-11-26 — PR #312 exact-head/main push CI 종결
- PR #312 exact HEAD `b7a58ef619ac78abbd7f256957c3eba2ece5c4b5`; Run #1691 / 45762478066 pull_request completed/success, 15/15. Compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC crosswalk16/M606 mapping41/PROJECT_LOG events450; Commission PDFs3/3 and official sources10 PASS; Article 13(8), 2025/2392 core-functionality, Annex I(10), Annex II(1) locators/provenance PASS.
- Run #1691 artifacts: PDF ZIP 15090342253 / SHA-256 `7930ea83919010c257ed0c258aa4dead81e1a4515917d1d8f7929b311a1dbcd3`; provenance ZIP 15090975346 / SHA-256 `4a4ce22a691a8dd4d6de99576ec2896ec354dbac8d3506761cecf8eb9dfb9da6`.
- Expected-head squash merge SHA/current main `c92984b987083f6bc9133b5345867a804ea9d54f`. Run #1692 / 45762563955 main push exact SHA completed/success, 15/15, same checks PASS.
- Run #1692 artifacts: PDF ZIP 15089664214 / SHA-256 `03124c9991042c2536138f855d2b516317a472b875e64fd277307199726ca08f`; provenance ZIP 15089509400 / SHA-256 `8e2e161a1cd3ea0334877b2bab5e877f014818d468f5995fcf1b3c10b7870ba6`.
- Digests are CI artifact ZIP hashes, not manufacturer-source PDF hashes. Manufacturer originals 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded.


### §72.35 2026-11-26 — PR #313 closeout and new official index findings
- PR #313 exact head `18018194146eb996914578d9dd59d132effa281a`; Run #1693 / 45762752285 pull_request success 15/15; pytest189; traceability451 (modern446, legacy5); Commission PDFs3/3; official sources10; Article 13(8)/2025/2392 legal locators PASS.
- Run #1693 ZIPs: source ID 15091095590 / SHA-256 `6c24e3e42c69b3c5f9badcf538411b186e619203e7ec50b3234011291929bbc2`; provenance ID 15091095638 / SHA-256 `8580e462e08b6fe8e08539ed67c3602cea1386217a94321ad870df22d0eabc28`.
- Expected-head merge/current main `08138829040d8c262baf218385ae2d4968b8d1d1`; Run #1694 / 45762866934 main push exact SHA success 15/15; same checks PASS.
- Run #1694 ZIPs: source ID 15091165408 / SHA-256 `be5e2fba2b1814f4a12c67e4f3822c8fa130b7d0c1d81115bdf3a044f9ef9080`; provenance ID 15091045634 / SHA-256 `a05df3a653931da83b14797ea8640a1ab2b74678b7e5c9a463cc6f03ea8d7cf9`. Digests are CI ZIPs, not manufacturer PDF hashes.
- PR #313 body/title stale “PR #312” wording corrected in this record.
- Solution Square doc32720 detail is confirmed; indexed English PEGA2 Ver1.3 attachment name is visible but actual attachment URL not. Separate official PEGA2 Ver1.0 direct PDF URL: `https://ssq.ls-electric.com/uploads/document/17761472300650/PEGA2_KOR_Ver1.0_260413.pdf?type=attachment`. iX700M listing date 2026-09-16 confirmed; detail href/document ID unresolved.
- LS Mecapion CE #171/#172/#173 model titles are indexed (220B / 370B+300B / 750B+550B+450B); individual hrefs unresolved. PEGA2 Ver1.3 manual row is wr_id12651 with attachment `PEGA2_KOR_Ver1.3_260826.pdf`, not requested 12652. iX700M Ver1.4 manual index row confirmed but wr_id unresolved. CE #170 wr_id12888 is distinct.
- Manufacturer binaries 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation. CRA only; SIL 3 excluded; Q01~Q62 not sent.


### §72.36 2026-11-26 — PR #314 closeout / official source anchor recheck
- PR #314 merged from exact head `48d4d6621b4c36d42d04a76b4e466679e9bcbe87` to main `676289d6e854e9ff564ee8f345cbcb587f266b1b`; Run #1695 / 45782233267 pull_request exact-head success and Run #1696 / 45782409111 main push exact-SHA success, both 15/15 steps. Jobs: 139780236768 and 139780804594.
- Run #1695 CI ZIP digests: source `6a13b278e85a7cf5df207855790dced82f08accd73351a070105fb1bcce058b9`; provenance `ab2cfba50d2b975374914543fd8fef5733683776b536c899107b75da82e2c41f`. Run #1696 CI ZIP digests: source `c6562202f19a8b8d7e5feaf2b5acee77508d72060c3869a344e608b472d2c88f`; provenance `f4c9ae2fcd6b9df9d7823e8e48cce235146ad2f0bda16f2d4ca2881ec3387158`. These are ZIP hashes, not manufacturer document hashes.
- Rechecked official indexes: PEGA2 doc32720 detail and indexed English Ver1.3 filename confirmed, attachment href unresolved; iX700M 2026-09-16 list item confirmed, document ID/detail href unresolved; CE #171–#173 model strings/date reconfirmed, individual hrefs/attachments unresolved; wr_id12652 not retried and unresolved. wr_id12651 is PEGA2 Ver1.3 and must not be substituted.
- Solution Square pages are JS-rendered; page reader sees SPA shell only. Public web search did not disclose a documented API/JS resource endpoint yielding the requested identifiers. No guessed IDs, no constructed attachment URLs, no repeat of known failed wr_id12652 endpoint.
- Manufacturer binaries acquired: 0 / metadata_only. No manufacturer SHA-256, PDF signature, signer-chain, revision or SKU validation.


### §72.37 2026-11-26 — PR #315 exact-head / main push CI closeout
- PR #315 exact head `6d66a06a32a6ee8218bbb9b0eb5940f1e8bb7d2d`; Run #1697 / 45787893954 pull_request exact-head success 15/15; job139799254293; pytest189; traceability453 (modern448, legacy5); Commission PDFs3/3; official sources10; legal locators/provenance PASS.
- Expected-head merge SHA/current main `adeda5347682960e119f7df721c7c568c57b92a6`; main ref independently confirmed. Run #1698 / 45788121534 push/main exact SHA success 15/15; job139799990444; same tests and source checks PASS.
- Run #1697 ZIP digests: source `522a3c524b594fee69f82c9d02dacc621c8eeced18436b242f24fcba1ae5a6d3`; provenance `2e14ba168afb2eb89c201efb42b4ce6b0772ca1a50f3b526dd826c51fc2b555f`. Run #1698 ZIP digests: source `1d92f8a999414224feb91fd55059885d205a2c761b2752ddc17e279dc8db9e83`; provenance `10ba609f7df7391ff9500caaeae39a60ee7bef9842becbcdf0f5d00ced1ba1a3`. All are CI ZIP hashes, not manufacturer PDFs.
- Manufacturer originals remain 0 / metadata_only; no manufacturer SHA/signature/signer-chain/revision/SKU validation.


### §72.38 2026-11-26 — PR #316 exact-head / main push CI closeout
- PR #316 exact head `ccacb4716eb1665bcd2a695971f822dfaa7ce16e`; Run #1699 / 45788389243 pull_request exact-head success 15/15; job139800907274; pytest189; traceability454 (modern449, legacy5); Commission PDFs3/3; official sources10; legal locators/provenance PASS.
- Expected-head merge SHA/current main `26974977a527d546e0257a8bce3401db3e76c587`; main ref independently verified. Run #1700 / 45788548649 push/main exact SHA success 15/15; job139801437794; same validation PASS.
- Run #1699 ZIP digests: source `87bcdb1dd49e6e947c817a2ca45c87c18b3083d60cdd31d3a32677202b8fc804`; provenance `4726a352ab09652c9ca3b066c3741f79e16e11958a37e736a74143f090fe81f4`. Run #1700 ZIP digests: source `1844c5afd471795930bce7ba3655ae75a791315682de1987968059c424735294`; provenance `47076268b2b900c805f8ba4cb4248009456b084ad58c7c268345ca9dd27938b2`. These are ZIP hashes, not manufacturer PDF hashes.
- Manufacturer originals remain 0 / metadata_only; no manufacturer hash/signature/signer-chain/revision/SKU validation.


### 72.39 2026-11-26 — PR #317 / Run #1701~#1702 and manufacturer index evidence
- PR #317 merged; PR exact head `d130d1cb6056601aac680e4443844921c9b78d91`; merge/current main `eb0bccb746a94d3a24f5d13bfb6f561fd33b617a` exact match. Run #1701 / 45788826752 pull_request success 15/15 (job139802364956); Run #1702 / 45788943373 push/main exact SHA success 15/15 (job139802762357).
- Both logs: compileall PASS; pytest189; traceability claims13/interfaces15/requirements35/SEC36/EVD-SEC16/product evidence15/linked claims13/M60641/project_log_events455 (modern450, legacy5); Commission PDFs3/3; official sources10; Article 13(8) and Delegated Regulation 2025/2392 Annex I(10)/Annex II(1) locators PASS.
- Run #1701 artifact ZIPs: source ID15102151164, 3,070,566 bytes, SHA-256 `c7aa946a55353303280d40b6a9e9ec5c96f273bbee2864f99355a0c06a836ac9`; provenance ID15101966528, 2,565 bytes, SHA-256 `393f638535450c4c26c9820d0bda3b7a4f50830703f47c340de5168892425a4f`. Run #1702: source ID15101832131, 3,070,566 bytes, SHA-256 `48c8830ef8e6e83b778648deb23f265015bf36a42a627989b1f523df0942e02e`; provenance ID15101187896, 2,565 bytes, SHA-256 `acb45103e06e121935ed2617afec40468b1c9d3ce60a0419e19879ae21101871`. These digests describe GitHub artifact ZIPs only.
- Official Solution Square doc32720 search result: PEGA2 User Manual; updated 2026-09-23; indexed English file `PEGA2_ENG_Ver1.3_260831.pdf`, 6.0 MB; listed contents include EtherCAT, CiA402, Safety Functions, Modbus-RTU; applicable product PEGA2 series. Actual attachment href/API and binary unavailable; JS-only detail shell.
- Official Solution Square integrated search result: `iX700M 사용 설명서`, User Manual, Motion&Servo, 171 views. With the previously observed 2026-09-16 listing, this confirms title/category metadata only; document ID/detail href/attachment href remain UNKNOWN.
- LS메카피온 CE index: #171 iX700MD1-B-220B; #172 iX700MD1-B-370B, 300B; #173 iX700MD1-B-750B, 550B, 450B; date 2026-04-30. Individual detail/attachment hrefs remain UNKNOWN. Manual index row 41: iX700M DRIVE 400[V] Ver1.4, 2026-05-26; row 40: PEGA2 Ver1.3, 2026-04-01. wr_id=12651 is PEGA2 Ver1.3 and does not resolve requested wr_id=12652. No retry of failed wr_id=12652 endpoint.
- Manufacturer binaries=0; manufacturer SHA-256/PDF signature/signer chain/revision/SKU checks not performed. Metadata/index evidence must not be represented as a retrieved or authenticated manufacturer original. CRA only; SIL 3 excluded; Q01~Q62 not sent.
