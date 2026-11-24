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
