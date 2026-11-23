# ETSI M/606 active 18개 Work Item 통합 매트릭스 — 2026-11-20

- 기준: ETSI Work Programme v2.3.3, M/606 active list 18개.
- 17개는 M/606 Annex I vertical topics 17–27 및 31–36에 대응한다.
- EN 304 642는 telecom network functions용 추가 supporting work item이며, Annex I 41 topics와 1:1 매핑을 확인하지 못했다.
- 18개 모두 Harmonised Standard metadata는 Yes, Official Journal field는 blank. 실제 OJ citation 또는 Article 27 presumption은 확인되지 않았다.

## 주요 현황

| ETSI EN | M/606 item | 제목 | 최신 상태 / 버전 | 다음 milestone | 법적 class |
|---|---:|---|---|---|---|
| 617 | 17 | Browsers | 2026-11-06 / 1.0.0 | 2026-12-21 | I |
| 618 | 18 | Password managers | 2026-09-22 / 0.2.2 | 2026-11-23 | I |
| 619 | 19 | Anti-malware | 2026-10-14 / 1.0.2 | 2026-11-23 | I |
| 620 | 20 | VPN | 2026-11-06 / 1.0.0 | 2027-01-15 | I |
| 621 | 21 | NMS | 2026-11-06 / 1.0.5 | 2027-01-15 | I |
| 622 | 22 | SIEM | 2026-11-06 / 1.0.0 | 2027-01-15 | I |
| 623 | 23 | Boot managers | 2026-09-16 / 0.1.3 | 2026-12-05 | I |
| 624 | 24 | PKI | 2026-11-05 / 1.0.0 | 날짜 미표시; adoption forecast 2027-02-11 | I |
| 625 | 25 | Network interfaces | 2026-11-05 / 1.0.0 | 2027-01-15 | I |
| 626 | 26 | Operating systems | 2026-11-06 / 1.0.1 | 2027-01-21 | I |
| 627 | 27 | Routers/modems/switches | 2026-10-01 / 1.0.1 | 2026-11-25 | I |
| 631 | 31 | Smart-home virtual assistants | 2026-10-14 / 1.0.0 | 2026-12-04 | I |
| 632 | 32 | Smart-home security products | 2026-10-14 / 1.0.0 | 2026-12-04 | I |
| 633 | 33 | Internet-connected toys | 2026-10-14 / 1.0.0 | 2026-12-04 | I |
| 634 | 34 | Personal wearables | 2026-10-16 / 1.0.0 | 2026-12-05 | I |
| 635 | 35 | Hypervisors/container runtimes | 2026-09-17 / 1.0.1 | 2026-12-11 | **II** |
| 636 | 36 | Firewalls/IDS/IPS | 2026-10-06 / 1.0.0 | 2026-12-22 | **II** |
| 642 | 추가 supporting item | Telecom network functions | 2026-10-21 / 0.0.16 | Mature draft 2027-03-31 | 직접 Annex III 분류 없음 |

## 중대한 법령 분류 불일치

ETSI Work Item scope text는 EN 304 635와 EN 304 636을 Annex III Class I이라고 표기한다. 그러나 법적 원문인 Regulation (EU) 2024/2847 Annex III 및 Commission Implementing Regulation (EU) 2025/2392 Annex I은 각각 Class II category 1 (hypervisors/container runtimes) 및 Class II category 2 (firewalls/IDS/IPS)로 분류한다.

- EN 304 635: DEN/CYBER-EUS-0016, WKI 74858. ETSI page says Class I; legal class is Class II.
- EN 304 636: DEN/CYBER-EUS-0020, WKI 74859. ETSI page says Class I; legal class is Class II. M/606 item 36 includes industrial-use systems.
- 법령이 우선하며 해당 제품의 core functionality가 이 범주에 해당하면 Article 32(3) Class II route를 적용한다.
- 최신 draft 대조: EN 304 636 V1.0.0 (2026-07-09) PDF document p.9 Introduction은 Annex III Class II point 2를 명시한다. EN 304 635 V1.0.1 (2026-06) 공개 sample preview document p.15 Scope는 Annex III Class II point 1을 명시한다. 두 최신 공개 draft의 확인 가능한 본문은 법령과 일치한다. EN304635는 15-page sample only; full 386-page PDF 미확보.

## 산업용 OT 경계

- Industrial OT 제외: EN 304 620 VPN, EN 304 621 NMS, EN 304 622 SIEM, EN 304 627 routers/modems/switches.
- EN 304 625 network interfaces 기술 설명은 Fieldbus controllers/adapters를 포함한다. 별도 판매 interface module과 host servo drive의 core functionality를 분리한다.
- 18개 모두 Harmonised Standard metadata Yes이나 OJ field blank. 예상 OJ 일정이나 candidate metadata는 실제 OJ citation이 아니다.

## 근거

- ETSI M/606 progress report (18 items): https://portal.etsi.org/webapp/WorkProgram/TUBEReport.asp?SearchPage=TRUE&butExpertSearch=Search&curItemNr=1&includeNonActiveTB=FALSE&includeSubProjectCode=FALSE&optDisplay=10&qMandate_List=%27M/606%27&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qSTOP_FLG=N&totalNrItems=18
- EN 304 635: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74858
- EN 304 636: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74859
- EN 304 642: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74965
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng

## 한계

다음 milestone은 ETSI Work Programme forecast이며 ESO 법정 adoption deadline과 다르다. OJ field blank는 해당 record에서 조회 당시 reference가 표시되지 않았다는 의미다. EN 304 636 최신 V1.0.0은 확보·검토해 Class II point 2를 확인했다. EN 304 635 최신 V1.0.1은 DocBox에 등록되어 있으나 fetch timeout으로 본문은 미확인이다.


## 추가 초안 대조 — EN 304 635/636 공개 interim draft

ETSI DocBox에서 최신 Work Item version보다 이전의 공개 interim draft를 확보해 class-label mismatch를 더 세분화했다.

- EN 304 636 V1.0.0 (2026-07-09): 최신 public draft PDF page 9 Introduction에서 CRA Annex III Class II point 2를 명시한다. 이는 Regulation 2025/2392와 일치하며, 현재 Work Item page의 Class I scope label은 stale/incorrect metadata다. 이전 V0.0.9도 Class II로 일치한다.
- EN 304 635 V0.0.8 (2025-11-10): 추출된 본문에서 “Class I”, “Class II”, “Annex III” 표기를 찾지 못했다. 이 문서는 법적 class를 잘못 명시한 것으로 확인되지 않았다.
- EN 304 635 V1.0.1: 공개 preview 15쪽 Scope에서 Class II point 1 확인. 전체 원본 386쪽 미확보라는 열람 범위 제한은 유지한다.

Sources:
- EN 304 635 V0.0.8: https://docbox.etsi.org/CYBER/EUSR/Open/EN-304-635_V0.0.8_2025-11-10_Virtualisation_Containers.pdf
- EN 304 636 V0.0.9: https://docbox.etsi.org/cyber/CYBER/Open/EN-304-636_V0.0.9_2025-12-15_Firewalls_Mature-draft.pdf
- EN 304 636 V1.0.0 latest public draft: https://docbox.etsi.org/CYBER/EUSR/Open/EN_304-636_V1.0.0_2026-07-09_Firewalls_Enquiry-draft.pdf


### 최신 EN 304 636 V1.0.0 직접 확인

ETSI DocBox directory listing shows EN_304-636_V1.0.0_2026-07-09_Firewalls_Enquiry-draft.pdf. The PDF was opened successfully. Page 9 (PDF zero-index page 8), Introduction, explicitly states that firewalls, intrusion detection systems and intrusion prevention systems are identified in Annex III, Class II, point 2 of Regulation (EU) 2024/2847. This confirms the latest public draft itself is legally aligned; the Work Item detail page's Class I label is stale/incorrect metadata.

EN 304 635 V1.0.1 public sample preview (15 pages) explicitly states Annex III Class II point 1 in document p.15 Scope. Full 386-page original was not acquired; this is a sample-coverage limitation, not an unresolved class-label question. Source: https://standards.iteh.ai/catalog/standards/etsi/9277aaff-7da2-4e37-81c4-8dc2b472b2b4/etsi-en-304-635

- ETSI DocBox directory: https://docbox.etsi.org/CYBER/EUSR/Open/
- EN 304 636 V1.0.0: https://docbox.etsi.org/CYBER/EUSR/Open/EN_304-636_V1.0.0_2026-07-09_Firewalls_Enquiry-draft.pdf
- EN 304 635 V1.0.1: https://docbox.etsi.org/CYBER/EUSR/Open/EN_304-635_V1.0.1_2026-06-24_Virtualization_Container_Enquiry-draft.pdf


## 2026-11-21 live status correction — EN 304 635 V1.0.9

The previous table's EN 304 635 row (V1.0.1 / 2026-09-17) is a historical snapshot and must not be treated as the current live status.

- ETSI live Work Programme query + Work Item Monitoring: DEN/CYBER-EUS-0016 / EN 304 635 **V1.0.9**.
- Current status: EC assessment before WNV requested (2026-11-19).
- Next status: EC assessment before WNV received (2026-11-28).
- Remark: V1.0.9 uploaded 2026-11-20; Draft Review after PE; CYBER-EUSR-endorsed version resolving Enquiry and EC HAS2 comments.
- Conflicting cached detail page still showed V1.0.1 / 2026-09-17. Retain this as a source freshness/cache discrepancy.
- ETSI free download page lists V1.0.1 (2026-06), 2,700,830 bytes. Do not mistake this for V1.0.9.
- V1.0.9 original PDF bytes, page count, content and SHA-256: **not acquired / not verified**.
- Legal class remains **Class II, category 1** under Regulation (EU) 2024/2847 Annex III and Implementing Regulation (EU) 2025/2392 Annex I. ETSI Work Item scope wording does not override binding law.

Sources:
- Live Work Programme query: https://portal.etsi.org/webapp/WorkProgram/Frame_WorkItemList.asp?SearchPage=TRUE&butSimple=Search&includeNonActiveTB=FALSE&optDisplay=10&qINCLUDE_SUB_TB=True&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qTB_ID=824%3BCYBER
- Work Item Monitoring: https://portal.etsi.org/Portal_WI/Form1.asp?NbToDisplay=30&PersonId=0&SubTB=&SupCrit=CYBER+++++++++++++++++++++18878249&TabId=&TbId=0&WIcritID=18
- Free download area (V1.0.1 only): https://portal.etsi.org/webapp/ewp/copy_file.asp?wki_id=74858


## 2026-11-23 — M/606 amended deadlines crosswalk (C(2026) 7861 final)

The live ETSI status table above remains a 2026-11-20 snapshot of work-item status and technical milestones. The Commission's later Implementing Decision C(2026) 7861 final (2026-11-10) replaces Annex I to C(2025) 618 and changes the M/606 ESO adoption deadlines. These are distinct data fields: an ETSI work-item milestone such as final-deliverable endorsement is not itself the M/606 final adoption deadline.

| ETSI work item mapping | M/606 Annex I item | Amended ESO adoption deadline | Notes |
|---|---:|---:|---|
| 17 ETSI vertical work items (EN 304 617–627 and EN 304 631–636) | 17–27, 31–36 | 2027-01-31 | Vertical standards; each work item retains its own ETSI stage and forecast milestone |
| EN 304 642 | No direct Annex I mapping identified | Not assigned in this crosswalk | Supporting telecom work item; do not infer a vertical-item deadline without a direct mapping |
| Non-ETSI / remaining vertical items | 16, 28–30, 37–41 | 2027-01-31 | Check CEN/CENELEC/other ESO assignments separately |
| Horizontal item 1 | 1 | 2026-11-30 | Product design/development/production security requirements |
| Horizontal item 15 | 15 | 2026-11-30 | Vulnerability handling |
| Horizontal items 2–14 | 2–14 | 2027-10-30 | Unchanged by C(2026) 7861 |

**Article 2 condition:** If CEN, CENELEC or ETSI indicates non-acceptance of the amendments within one month after receiving the decision, C(2026) 7861 ceases to apply and the 2025-02-03 version of C(2025) 618 continues to apply. ESO receipt dates and any non-acceptance notice remain Unknown until supported by primary evidence.

**Legal boundary:** ESO adoption deadlines do not establish OJ citation or CRA Article 27 presumption of conformity. The CRA Regulation's own application dates are unchanged.

**Primary sources:**
- C(2026) 7861 final: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_0/de00000001090398
- Annex I: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401
