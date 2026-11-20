# CRA M/606 ETSI 실시간 작업계획 및 OJ 상태 점검 — 2026-11-18

## 범위와 판단 원칙

2026-11-18 확인 시점에 공개된 ETSI Work Programme의 M/606 작업계획(2026-11-17, Version 2.3.3)을 확인하고, 서보 드라이브의 수직 표준 후보와 직접 관련될 수 있는 항목을 우선 추출했다. 이 자료는 ETSI 작업관리 시스템의 일정/상태 스냅샷이며, 채택된 EN의 최종 원문, CEN/CENELEC의 별도 작업, Commission의 OJ 게재 결정과 동일하지 않다.

- Commission은 M/606에 41개 표준화 항목이 있다고 설명하고, 2026-11-10 개정으로 모든 수직 표준과 일부 수평 표준의 납품 기한을 3개월 연장했다고 명시한다.
- ETSI Work Programme은 M/606 아래 활성 work item 18개를 표시한다. 2026-11-17 Plan은 작업별 adoption, publication, OJ publication 날짜를 각각 열로 분리한다.
- ETSI의 미래 날짜는 계획/목표 일정으로 기록한다. 날짜가 지났더라도 별도 공식 채택/발행/OJ 확인 없이 achieved로 승격하지 않는다.
- Commission harmonised standards index는 OJ에 실제 게재된 참조 목록을 제공하며, 참조는 OJ에 게시되어야 한다. 2026-11-18 조회 페이지에는 CRA 전용 항목이 보이지 않았다. 따라서 현재 확인 범위에서 CRA OJ 참조를 식별하지 못했다는 제한적 결론만 유지한다.

## 서보 드라이브에 직접 확인할 ETSI work items

| ETSI 문서 | M/606 관련 제품 유형 | 2026-11-17 상태/일정(ETSI 계획) | 서보 드라이브 적용 경계 |
|---|---|---|---|
| EN 304 636, DEN/CYBER-EUS-0020 | Firewalls, IDS/IPS | 현재 상태: Comments categorisation assessed (2026-10-06). Adoption 목표 2027-02-11, Publication 목표 2027-02-19, OJ Publication 목표 2027-05-15 | 제품 그 자체의 의도된 목적/핵심 기능이 방화벽 또는 IDS/IPS일 때 수직 제품 표준 후보. 드라이브 내 단순 패킷 필터링, 진단 포트 보호, 보안 강화 기능만으로 드라이브 전체가 방화벽/IDS/IPS가 되지 않는다. |
| EN 304 625, DEN/CYBER-EUS-0017 | Physical and virtual network interfaces | 현재 상태: 7 VR – EC assessment before EV received (2026-09-28). Adoption 목표 2027-03-08, Publication 목표 2027-03-15, OJ Publication 목표 2027-06-23 | 판매되는 제품 자체가 네트워크 인터페이스 제품 카테고리에 해당하는지 의도된 목적/핵심 기능을 확인해야 한다. Ethernet/fieldbus 포트가 있다는 사실만으로 완제품 서보 드라이브를 네트워크 인터페이스 제품으로 분류하지 않는다. |

주의: 위 표의 'OJ Publication'은 ETSI Work Programme에 표시된 목표 일정이다. OJ 실제 게재 증거가 아니다. 또한 두 표준의 scope가 특정 드라이브에 적용되는지는 제품 설명서, intended purpose, architecture 및 해당 표준의 최종 범위 문언을 확보한 뒤 별도 판단한다.

## 최신성 및 출처의 교차검증

1. European Commission CRA standardisation page (마지막 업데이트 2026-11-12): M/606 41개 항목 및 2026-11-10 개정 사실.
   https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
2. ETSI Work Item Plan: All Active Work Items mandated under M/606; 페이지 표시 시각 2026-11-17, Work Programme Version 2.3.3, 18 items. 개별 표준의 상태/목표 일정 확인에 사용.
   https://portal.etsi.org/webapp/WorkProgram/WorkItemPlan.asp?SearchPage=TRUE&butExpertSearch=Search&includeNonActiveTB=FALSE&includeSubProjectCode=FALSE&optDisplay=10&qCLUSTER_BOOLEAN=OR&qETSI_ALL=&qFREQUENCIES_BOOLEAN=OR&qINCLUDE_MOVED_ON=&qINCLUDE_SUB_TB=True&qKEYWORD_BOOLEAN=OR&qMandate_List=%27M%2F606%27&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qSTOPPING_OUTDATED=&qSTOP_FLG=N
3. European Commission Harmonised Standards index: OJ 참조 목록의 공식 안내 및 CRA 전용 목록 항목 미확인.
   https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards_en
4. Commission CRA standardisation page가 STAN4CR를 ESO 활동 포털로 안내한다. 다만 2026-11-18 확인 시 새로 찾은 ETSI 실시간 작업계획은 2026-06 STAN4CR 공동 보고서보다 구체적이고 최신인 ETSI 개별 work item 데이터다. 이를 CEN/CENELEC 전체 41개 항목의 완전한 진행현황으로 일반화하지 않는다.

## 결론 및 후속 조치

- 2026-06 STAN4CR 공동 ESO 보고서만을 최신 진행자료로 보던 이전 기록은 보완한다. 이제 ETSI M/606 활성 work item에 대해서는 2026-11-17 Version 2.3.3 계획을 최신 관찰자료로 사용한다.
- CEN/CENELEC의 수평 표준 및 산업용 OT 표준(prEN 50770 계열 등)은 ETSI 작업계획과 별도 추적해야 한다. ETSI의 18개 활성 item을 M/606 41개 전체로 오인하지 않는다.
- OJ 참조가 실제 공표되기 전에는 CRA Article 27의 추정 적합성을 주장하지 않는다. Commission index와 EUR-Lex OJ를 매 업데이트 시 다시 확인한다.
- 제품별 BOM/모델 증거가 없는 현재, drive-level classification은 Unknown 유지한다. 네트워크 포트 존재만으로 item 25 또는 EN 304 625 적용을 확정하지 않는다.

---


## 2026-11-20 최신상태 추가 감사 및 기존 기록 정정

### 1. ETSI M/606 Work Programme 재조회
- 2026-11-20에 조회한 ETSI Work Programme Version 2.3.3은 M/606 활성 work item 18개를 표시한다. 목록 화면은 10개만 표시하므로 전체 18개 개별 상세 레코드의 전수검토를 완료했다고 주장하지 않는다.
- 기존 2026-11-18 표에서 EN 304 625의 2026-09-28 “7 VR – EC assessment before EV received”는 과거 상태다. 2026-11-20 개별 상세 레코드에는 현재 상태가 **Comments categorisation assessed (2026-11-05)**로 표시되며, 2026-11-19 비고에는 EC second assessment가 2026-09-28 및 2026-11-16 제출 코멘트 2개 묶음으로 수신됐다고 기록돼 있다.
- EN 304 636 firewall/IDS/IPS: Comments categorisation assessed (2026-10-06), 다음 milestone은 2026-12-22 final deliverable endorsed for registration 목표.
- EN 304 622 SIEM: Comments categorisation assessed (2026-11-06). Industrial OT domain은 scope에서 제외.
- EN 304 621 NMS: industrial OT domain 제외.
- EN 304 620 VPN: industrial OT domain 제외.
- EN 304 627 router/modem/switch: industrial OT domain 제외.
- EN 304 625 physical/virtual network interfaces는 Annex III Class I 제품 범주의 network-interface 제품을 위한 작업으로 기재돼 있다. EtherCAT/Ethernet/Modbus 포트만으로 드라이브 완제품을 이 범주로 자동 분류하지 않는다.
- 관련 work item의 OJ 필드는 실제 OJ reference를 제공하지 않는다. Work Programme의 “Harmonised Standard: Yes” 메타데이터는 실제 OJ citation 또는 Article 27 presumption을 입증하지 않는다.

### 2. CEN/CENELEC 수평 EN 2종 신규 발행 — 2026-11-19 발표
- EN 40000-1-1:2026 (JT013095) 및 EN 40000-1-2:2026 (JT013089)는 모두 Published, DOR 2026-11-02, DAV 2026-11-18.
- 두 개별 CEN 카탈로그 레코드는 “No citation expected for Directive 2024/2847”로 표시한다.
- 따라서 두 표준은 CEN 발행 표준이지만, 이 레코드에 근거한 CRA Article 27 추정 적합성은 성립한다고 주장하지 않는다.
- EN 40000-1-2는 제품 위험관리와 lifecycle activities를 포괄하는 수평 프레임워크다. EN 40000-1-1은 용어·정의 표준이다.

### 3. 공식 출처
- ETSI active M/606 work items (18): https://portal.etsi.org/webapp/WorkProgram/Frame_WorkItemList.asp?SearchPage=TRUE&butExpertSearch=Search&includeNonActiveTB=FALSE&includeSubProjectCode=FALSE&qCLUSTER_BOOLEAN=OR&qFREQUENCIES_BOOLEAN=OR&qINCLUDE_SUB_TB=True&qKEYWORD_BOOLEAN=OR&qMandate_List=%27M%2F606%27&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qSTOP_FLG=N&titleType=all
- EN 304 625 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74860
- EN 304 636 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74859
- EN 304 622 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74413
- EN 304 621 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74412
- EN 304 620 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74409
- EN 304 627 individual record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74416
- CEN EN 40000-1-1: https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:82349,2307986
- CEN EN 40000-1-2: https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:81335,2307986
- CEN-CENELEC announcement 2026-11-19: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/

### 4. 한계
- ETSI 목록은 18개 중 10개 표시이며, 18개 모든 상세 레코드 전수감사는 미완료.
- CEN/CENELEC prEN 50770-1~6 개별 레코드는 이번 addendum에서 전부 재조회하지 않았다. 기존 2026-11-18 snapshot과 별도 관리한다.
- 표준 본문 유료 원문은 취득/검토하지 않았고, 카탈로그/작업계획/공지 정보만 검토했다.
- Article 27 OJ index는 별도 재조회가 필요하다. 이 addendum의 OJ 상태는 확인한 ETSI/CEN 개별 레코드의 field 기준이다.

### 5. EN 304 620 상태도 최신 레코드로 정정
- 기존 2026-09-28 “7 VR – EC assessment before EV received”는 과거 상태다.
- 2026-11-20 조회한 ETSI 개별 레코드: EN 304 620 v1.0.0, Comments categorisation assessed (2026-11-06).
- 2026-11-19 remarks: EC second assessment received in two batches of comments, on 28 September 2026 and 22 October 2026.
- Scope description: VPN product with industrial OT domain VPNs excluded.
- Official Journal field는 비어 있다. Work Programme의 Harmonised Standard metadata만으로 CRA OJ citation/Article 27 presumption을 주장하지 않는다.
- Record: https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74409
