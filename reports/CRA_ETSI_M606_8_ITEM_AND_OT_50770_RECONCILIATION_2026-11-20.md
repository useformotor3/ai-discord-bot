# CRA ETSI M/606 8개 Work Item 및 CLC/TC 65X OT 프로파일 재조사

- 기준일: 2026-11-20
- 범위: 기존 미검토로 남아 있던 ETSI M/606 8개 work item 상세 레코드와 CLC/TC 65X OT profile series 분할·상태 정합성
- 상태: ETSI 개별 레코드 8건 확인 완료; CLC/TC 65X 상태는 national-member records 간 충돌로 central CENELEC live record 확인 필요
- 원칙: 표준화 진행상태와 Article 27 presumption of conformity를 분리한다. 실제 OJ citation이 확인되지 않으면 추정 적합성을 주장하지 않는다.

## 1. ETSI M/606 — 8개 Work Item 개별 감사

ETSI Work Programme v2.3.3의 M/606 조회 화면은 active work item 18개를 표시하고 기본 화면은 10개씩 나누어 보여준다. 본 감사는 기존 재개 계획에서 미검토로 남아 있던 8개 work item을 개별 상세 레코드로 열어 확인했다. 이는 ETSI M/606 18개 전체의 신규 전수 재감사를 의미하지 않는다.

| EN / Work Item | 현재 상태 / 버전 | 다음 상태 예정(요약 화면) | 제품 범위 및 경계 |
|---|---|---|---|
| EN 304 617 / EUS-006 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2026-12-21 final deliverable endorsement | Stand-alone browsers; Annex III Class I |
| EN 304 618 / EUS-007 | Comments categorisation assessed 2026-09-22 / 0.2.2 | 2026-11-23 | ICT common-use password managers |
| EN 304 619 / EUS-0018 | Comments categorisation assessed 2026-10-14 / 1.0.2 | 2026-11-23 | Anti-malware search/remove/quarantine software |
| EN 304 620 / EUS-005 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2027-01-15 | VPN products; industrial OT VPNs explicitly excluded |
| EN 304 621 / EUS-009 | Comments categorisation assessed 2026-11-06 / 1.0.5 | 2027-01-15 | NMS; industrial OT NMS explicitly excluded |
| EN 304 622 / EUS-0010 | Comments categorisation assessed 2026-11-06 / 1.0.0 | 2027-01-15 | SIEM; industrial OT SIEM explicitly excluded |
| EN 304 623 / EUS-008 | Comments categorisation assessed 2026-09-16 / 0.1.3 | 2026-12-05 | Boot managers |
| EN 304 624 / EUS-0015 | Work Item Plan 2026-11-16: Comments categorisation assessed 2026-11-05 / 1.0.0 | Next status date not shown | PKI and digital certificate issuance; cooperation with CEN/TC224 and ETSI TC ESI |

### 1.1 주요 해석

- EN 304 620(VPN), EN 304 621(NMS), EN 304 622(SIEM)의 개별 scope는 industrial OT domain에서 사용되는 해당 시스템을 제외한다. 산업용 서보 드라이브/OT 시스템을 일반 IT 제품 표준에 자동 포함시키면 안 된다.
- 브라우저·암호관리자·악성코드 탐지·boot manager·PKI는 제품의 핵심 기능과 intended purpose가 그 범주에 해당하는지 확인해야 한다. 웹 UI, 암호 저장, bootloader, TLS 인증서 사용이 존재한다고 완제품 드라이브를 해당 제품군으로 자동 분류하지 않는다.
- 8개 record 모두 Harmonised Standard metadata는 Yes이나 Official Journal field는 비어 있었다. 이 메타데이터는 조화표준 후보/의도이며 실제 OJ citation이 아니다.
- ETSI Work Item Plan의 adoption/publication/OJ publication 날짜는 예정 일정이다. OJ 예정일은 실제 OJ 게재가 아니다.
- EN 304 624는 2026-11-06 상세 페이지의 “Closing of approval procedure (2026-10-29)”와 Work Item Plan(2026-11-16)의 “Comments categorisation assessed (2026-11-05)”가 불일치한다. 최신 Work Item Plan 값을 잠정 기준으로 사용하고 stage history 추가 확인이 필요하다.

### 1.2 다음 ETSI 확인

- 2026-11-23 예정된 ETSI “GoSRSReq006-M/606 AMD 1 - examination meeting”의 실제 결과 및 amendment acceptance 여부를 회의 후 재확인한다.
- EN 304 618/619는 다음 상태 target이 2026-11-23이므로 이후 실제 상태를 재조회한다.
- 18개 전체의 consolidated master matrix는 기존 10개 기록과 이번 8개를 결합한 후 중복·상태 날짜·OJ 필드를 전부 재검증해야 한다.

### 1.3 ETSI 출처

- M/606 active list: https://portal.etsi.org/webapp/WorkProgram/Frame_WorkItemList.asp?includeNonActiveTB=FALSE&qINCLUDE_SUB_TB=True&qMandate_List=%27M/606%27&qSTOP_FLG=N
- EN 304 617: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74408
- EN 304 618: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74410
- EN 304 619: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74411
- EN 304 620: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74409
- EN 304 621: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74412
- EN 304 622: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74413
- EN 304 623: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=&WKI_ID=74414
- EN 304 624: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?SearchPage=TRUE&WKI_ID=74837
- ETSI Work Item Plan: https://portal.etsi.org/webapp/WORKPROGRAM/WorkItemPlan.asp?SearchPage=TRUE&butExpertSearch=Search&includeNonActiveTB=FALSE&optDisplay=ALL&qCLUSTER=19&qSTOP_FLG=N
- ETSI meeting calendar: https://portal.etsi.org/tb.aspx?tbid=218

## 2. CLC/TC 65X OT profile — prEN 50770 series 재조정

### 2.1 기존 6개 project에서 7개 deliverable로 변경

DKE의 2026년 10월 CRA 표준화 상태 PDF는 기존 prEN 50770-1이 다음 두 deliverable로 분할되었다고 명시한다.
- prEN 50770-1-1: OT firewalls
- prEN 50770-1-2: OT intrusion detection and prevention systems (IDS/IPS)

따라서 기존 “prEN 50770-1~6, 6개 표준”이라는 단순 표기는 7개 deliverable로 정정한다. 부모 프로젝트 81649와 분할된 두 세부 deliverable의 개별 CENELEC project ID 관계는 중앙 카탈로그에서 별도 확인한다.

| M/606 item | WIID | deliverable | OT scope |
|---|---:|---|---|
| 36b | 81649 | prEN 50770-1-1 | OT firewalls |
| 36b | 81649 (parent; child WIID 확인 필요) | prEN 50770-1-2 | OT IDS/IPS |
| 21b | 81650 | prEN 50770-2 | OT network management systems |
| 25b | 81651 | prEN 50770-3 | OT physical/virtual network interfaces |
| 20b | 81652 | prEN 50770-4 | OT VPN-function products |
| 27b | 81653 | prEN 50770-5 | OT routers/modems/switches |
| 22b | 81654 | prEN 50770-6 | OT SIEM systems |

### 2.2 National-member status records 간 충돌

**DKE (Germany), October 2026 status PDF**
- 7개 deliverable 모두 Start NWI 및 Drafting prEN 상태 marker가 있다.
- Voting prEN, Drafting EN, Voting EN, Adaption EN, HAS process, Citation hEN 단계는 표시되지 않는다.
- 이 자료는 national committee status snapshot이며 중앙 CENELEC project database의 실시간 readback과 동일시하지 않는다.

**BSI (UK) national project records**
- Project 9025-12804 / prEN 50770-2는 PWI로 표시되고 target dates가 알려지지 않았으며 EN IEC 62443-4-2 amendment work에 우선순위를 둔다고 설명한다.
- Project 9025-12805 / prEN 50770-3도 PWI/target dates unknown으로 표시한다.
- 이 기록은 DKE의 Drafting prEN marker와 충돌한다.

**LVS (Latvia) CLC/TC 65X project list**
- WIID 81649–81654 및 prEN 50770-1~6을 In development로 표시한다. 이는 개발 진행을 뒷받침하지만 정확한 stage를 결정하지 않는다.

**현재 판정**
- 7개 deliverable이 CLC/TC 65X OT profile work programme에서 추적되고 있음을 확인했다.
- DKE는 Drafting prEN, BSI는 -2/-3을 PWI/target dates unknown, LVS는 In development로 표시한다.
- CENELEC 중앙 프로젝트 81649는 직접 재열람했다. 공식 record는 여전히 단일 부모 참조 prEN 50770-1(방화벽 및 IDS/IPS 통합 scope), Committee stage, Citation expected, DOR/DAV 미기재로 표시하며 -1-1/-1-2 분할 child를 표시하지 않는다. 81650–81654 개별 중앙 record는 이번 pass에서 직접 readback에 실패했다. 따라서 -2/-3은 DKE/BSI status conflict를 유지하고 -4/-5/-6은 2026-11-18 이전 중앙 snapshot 외에는 신규 직접확인하지 않았다.
- DKE의 Citation hEN 열은 비어 있다. actual OJ reference는 이번 자료에서 확인되지 않았다. 기존 “Citation expected”는 실제 OJ citation이 아니다.

### 2.3 Servo-drive 경계

- -1-1/-1-2: 완제품 또는 별도 판매되는 OT firewall/IDS/IPS 제품 기능을 다룬다. 단순 통신 포트, 암호, 진단 로그, 접근제어만으로 드라이브를 해당 제품군으로 자동 분류하지 않는다.
- -2 NMS: DriveCM 파라미터 설정·commissioning 기능만으로 NMS라고 단정하지 않는다.
- -3 network interfaces: EtherCAT/Ethernet/Modbus 포트 존재와 완제품의 core functionality를 구분한다. 별도 공급 여부, 옵션/보드 경계, intended purpose, 제조사 분류 증거가 필요하다.
- -4 VPN, -5 router/modem/switch, -6 SIEM은 각 제품 기능의 실제 존재를 확인한다. 원격 유지보수, Ethernet 포트, 알람 이력만으로 분류하지 않는다.
- 개별 LS메카피온 SKU/FW/BOM evidence가 부족하므로 제품별 Annex III classification은 Unknown 유지한다.

### 2.4 출처

- DKE October 2026 status PDF: https://www.dke.de/resource/blob/2435170/215c8695b21563a904c94beeb62214e9/normungsprojekte-zum-cra-data.pdf
- BSI -2 PWI: https://standardsdevelopment.bsigroup.com/projects/9025-12804
- BSI -3 PWI: https://standardsdevelopment.bsigroup.com/projects/9025-12805
- LVS CLC/TC 65X list: https://www.lvs.lv/en/committees/projects/10907?Projects_page=12&Projects_sort=pr_number.desc
- CEN-CENELEC CLC/TC 65X WG3 webinar: https://www.cencenelec.eu/media/CEN-CENELEC/Events/Webinars/2026/2026-05-07_cra_unlocked_clc-tc65x-wg3-acs-technical-requirements.pdf

## 3. C(2026)7861 Annex I deadlines and Article 2 condition

Commission CRA standardisation page (last updated 2026-11-12) confirms that the request was amended on 2026-11-10 and delivery deadlines for all vertical standards and some horizontal standards were extended by three months.

| Annex I item | Scope | ESO adoption deadline |
|---|---|---|
| 1 | Risk-based secure design, development and production | 2026-11-30 |
| 2–14 | Horizontal security requirements | 2027-10-30 |
| 15 | Vulnerability handling | 2026-11-30 |
| 16–41 | Vertical product-specific standards | 2027-01-31 |

These are ESO adoption deadlines, not manufacturer CRA compliance dates, publication dates or OJ citation dates.

C(2026)7861 Article 2 states that if CEN, CENELEC or ETSI indicates that it does not accept the amendments within one month of receiving the decision, C(2026)7861 ceases to apply and Implementing Decision C(2025)618 in its 2025-02-03 version continues to apply.

- The one-month period runs from each ESO's actual receipt date, not automatically from 2026-11-10.
- Commission page confirmation that the request was amended does not prove that all three ESOs satisfied the Article 2 acceptance condition.
- Recital (2)'s statement that the ESOs accepted the original C(2025)618 request is not evidence that they accepted the 2026 amendments.
- This pass did not find public primary evidence of each ESO's receipt date or acceptance/non-acceptance notice. Status remains Unknown.
- ETSI calendar lists a 2026-11-23 “GoSRSReq006-M/606 AMD 1 - examination meeting”. As of 2026-11-20 this is a future meeting, not an acceptance result.

**Provenance limitation:** The Commission Register entry was located but its original PDF bytes were not acquired. Article 2 and Annex I were read from a third-party hosted copy bearing the Commission certified-copy stamp and cross-checked against the Commission official standardisation page. Do not claim original Register PDF bytes/hash were downloaded.

Sources:
- Commission CRA standardisation page: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
- Commission Register C(2026)7861: https://ec.europa.eu/transparency/documents-register/detail?lang=en&ref=C(2026)7861
- Certified-copy PDF mirror: https://www.ibf-solutions.com/fileadmin/dateidownloads/c-2026-7861-main-document-annex-cra-standards.pdf

## 4. Corrections and outstanding work

1. Replace the old six-profile prEN 50770 label with seven deliverables.
2. Resolve DKE Drafting prEN vs BSI PWI status for -2/-3 through central CENELEC records or committee confirmation.
3. Update M/606 item 36b mapping to both -1-1 and -1-2.
4. Confirm each ESO's receipt date and Article 2 acceptance/non-acceptance evidence.
5. Recheck actual OJ references; forecasts and “Harmonised Standard: Yes” metadata do not establish Article 27 presumption.
6. Recheck the ETSI 18-item list after the 2026-11-23 meeting and consolidate all 18.
7. Keep servo-drive product classification Unknown until exact SKU, intended purpose, core functionality, BOM and firmware evidence are obtained.
