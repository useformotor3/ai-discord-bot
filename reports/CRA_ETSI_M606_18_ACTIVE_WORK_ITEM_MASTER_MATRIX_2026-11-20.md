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
- 공개된 이전 interim draft를 확인했다. EN 304 635 V0.0.8에는 Annex III/Class I/Class II label이 추출되지 않았고, EN 304 636 V0.0.9는 Introduction/Scope에서 Annex III Class II point 2를 명시한다. 최신 Work Item version인 1.0.1/1.0.0 draft bytes는 아직 미취득이므로 최신 draft 상태는 별도 미확인이다.

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

다음 milestone은 ETSI Work Programme forecast이며 ESO 법정 adoption deadline과 다르다. OJ field blank는 해당 record에서 조회 당시 reference가 표시되지 않았다는 의미다. EN 304 635/636은 이전 공개 draft를 확인했으나 최신 v1.0.1/v1.0.0 draft는 미취득 상태다.


## 추가 초안 대조 — EN 304 635/636 공개 interim draft

ETSI DocBox에서 최신 Work Item version보다 이전의 공개 interim draft를 확보해 class-label mismatch를 더 세분화했다.

- EN 304 636 V0.0.9 (2025-12-15): Introduction 및 Scope에서 CRA Annex III Class II point 2를 명시한다. 이는 Regulation 2025/2392 Annex III Class II category 2와 일치한다. 따라서 현재 Work Item page의 Class I scope label은 stale metadata일 가능성이 높다.
- EN 304 635 V0.0.8 (2025-11-10): 추출된 본문에서 “Class I”, “Class II”, “Annex III” 표기를 찾지 못했다. 이 문서는 법적 class를 잘못 명시한 것으로 확인되지 않았다.
- EN 304 635 current Work Item version 1.0.1 및 EN 304 636 current version 1.0.0의 actual draft bytes는 아직 취득하지 못했다. 최신 draft까지 동일하다고 확대 주장하지 않는다.

Sources:
- EN 304 635 V0.0.8: https://docbox.etsi.org/CYBER/EUSR/Open/EN-304-635_V0.0.8_2025-11-10_Virtualisation_Containers.pdf
- EN 304 636 V0.0.9: https://docbox.etsi.org/cyber/CYBER/Open/EN-304-636_V0.0.9_2025-12-15_Firewalls_Mature-draft.pdf


### 최신 EN 304 636 V1.0.0 직접 확인

ETSI DocBox directory listing shows EN_304-636_V1.0.0_2026-07-09_Firewalls_Enquiry-draft.pdf. The PDF was opened successfully. Page 9 (PDF zero-index page 8), Introduction, explicitly states that firewalls, intrusion detection systems and intrusion prevention systems are identified in Annex III, Class II, point 2 of Regulation (EU) 2024/2847. This confirms the latest public draft itself is legally aligned; the Work Item detail page's Class I label is stale/incorrect metadata.

EN 304 635 V1.0.1 file is listed in the same directory as EN_304-635_V1.0.1_2026-06-24_Virtualization_Container_Enquiry-draft.pdf, but fetching it timed out. The earlier V0.0.8 draft had no class label in extracted text. Latest V1.0.1 content remains unverified.

- ETSI DocBox directory: https://docbox.etsi.org/CYBER/EUSR/Open/
- EN 304 636 V1.0.0: https://docbox.etsi.org/CYBER/EUSR/Open/EN_304-636_V1.0.0_2026-07-09_Firewalls_Enquiry-draft.pdf
- EN 304 635 V1.0.1: https://docbox.etsi.org/CYBER/EUSR/Open/EN_304-635_V1.0.1_2026-06-24_Virtualization_Container_Enquiry-draft.pdf
