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
