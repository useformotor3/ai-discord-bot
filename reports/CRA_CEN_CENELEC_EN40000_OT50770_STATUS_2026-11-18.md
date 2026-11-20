# CEN/CENELEC EN 40000 및 산업용 OT prEN 50770 공식 상태 감사 — 2026-11-18

## 1. 요약 및 중요 정정

2026-11-18 확인 결과, CEN 공식 프로젝트 레코드는 **EN 40000-1-1:2026을 Published**로 표시한다. 따라서 “CRA 표준이 아직 발행되지 않았다”는 포괄적 문장은 부정확하다. 정확한 구분은 다음과 같다.

- EN 40000-1-1:2026: CEN 발행 상태(Published), DAV 2026-11-18, DOR 2026-11-02. CEN 레코드는 CRA에 대해 “No citation expected”라고 명시한다.
- EN 40000-1-2:2026: CEN-CENELEC Work Item tracker와 독립 표준 카탈로그는 2026-11-02 ratification 완료 및 publication/publishing 단계로 표시한다. CRA OJ citation은 “No citation expected”로 기록된다. CEN-CENELEC 개별 레코드 링크는 이번 열람에서 서버 오류(500)로 본문을 읽지 못했으므로, 공식 원문 직접 readback은 미완료로 표시한다.
- FprEN 40000-1-3:2026: CEN 공식 프로젝트 레코드는 Under Approval, OJ citation expected. 아직 발행·OJ 인용 완료가 아니다.
- prEN 40000-1-4: CEN-CENELEC tracker에서 Work item / drafting 단계로 표시되며, OJ citation은 예상하지 않는 것으로 기록되어 있다.
- prEN 50770-1~6: CENELEC 공식 프로젝트 레코드에서 모두 Committee stage. 각각 OT 방화벽/IDS·IPS, 네트워크 관리, 네트워크 인터페이스, VPN, 라우터/모뎀/스위치, SIEM이다. 각 레코드는 CRA OJ citation expected라고 표시하지만, 아직 DOR/DAV가 없어 발행된 표준이 아니다.

**핵심 법적 해석:** CEN/CENELEC가 EN을 비준하거나 발행한 것과 Commission이 그 표준 참조를 CRA 조화표준으로 EU 관보(OJ)에 공표하는 것은 별도 절차다. EN 40000-1-1은 CEN에서 발행됐지만 “No citation expected”이므로 CRA Article 27(1) 추정 적합성을 주지 않는다. EN 40000-1-2 역시 OJ citation not expected로 표시된다. EN 40000-1-3 및 OT prEN 50770 계열은 OJ citation expected라는 작업 메타데이터일 뿐, 실제 OJ citation을 의미하지 않는다.

## 2. 공식 CEN/CENELEC 레코드

| 표준 | 공식 상태(2026-11-18 조회) | 날짜·OJ 필드 | 의미 |
|---|---|---|---|
| EN 40000-1-1:2026 | Published | DOR 2026-11-02; DAV 2026-11-18; DOA 2027-02-28; DOP/DOW 2027-05-31; OJ: No citation expected | 용어 표준. 발행 확인, CRA 추정 적합성은 제공하지 않음 |
| EN 40000-1-2:2026 | Ratification completed / publishing (2차 카탈로그 corroboration; CEN project record fetch failed) | DOR 2026-11-02; OJ: No citation expected (tracker 및 2차 카탈로그) | 전 제품의 사이버보안 원칙·위험관리·수명주기 프레임워크. OJ 인용 기대 없음 |
| FprEN 40000-1-3:2026 | Under Approval | DOR/DAV 미기재; OJ: Citation expected | 취약점 처리 프로세스. 아직 EN 발행/OJ citation 아님 |
| prEN 40000-1-4 | Work item / drafting | M/606 adoption deadline 30-10-2027; OJ: No citation expected (tracker) | 일반 보안 요구사항. 아직 초안 작업 |
| prEN 50770-1 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT 방화벽 및 IDS/IPS 보안 프로파일 |
| prEN 50770-2 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT 네트워크 관리 시스템 보안 프로파일 |
| prEN 50770-3 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT 물리·가상 네트워크 인터페이스 보안 프로파일 |
| prEN 50770-4 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT VPN 제품 보안 프로파일 |
| prEN 50770-5 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT 라우터·인터넷 연결 모뎀·스위치 보안 프로파일 |
| prEN 50770-6 | Committee stage | DOR/DAV 미기재; OJ: Citation expected | OT SIEM 시스템 보안 프로파일 |

CEN 공식 EN 40000-1-1 레코드에서 DAV는 승인된 공식 언어 버전이 중앙사무국에서 배포되는 날이고, DOP는 국가표준으로 동일 채택/발행을 완료해야 하는 최종일이다. 서로 혼동하지 않는다.

## 3. CENELEC OT 범위와 서보 드라이브 관련성

| CENELEC 프로젝트 | 공식 scope | 서보 드라이브 관련성 판단 |
|---|---|---|
| prEN 50770-1 | OT 환경용 방화벽 및 IDS/IPS | 드라이브 자체가 독립 판매되는 방화벽/IDS/IPS가 아닌 이상 직접 제품 분류로 적용하지 않는다. 내장 packet filtering이나 통신 보호는 자체 요구사항/통제 증거일 수 있지만 드라이브 전체를 방화벽으로 만들지 않는다. |
| prEN 50770-2 | OT 네트워크 관리 시스템 | 드라이브가 네트워크 관리 시스템 제품이 아닌 경우 직접 제품 표준이 아니다. 관리 기능/상위 시스템 연계는 인터페이스 위험 검토로 처리한다. |
| prEN 50770-3 | OT 물리·가상 네트워크 인터페이스 | 완제품 드라이브가 네트워크 인터페이스 제품으로 시장에 제공되는지 intended purpose와 core functionality로 판정한다. Ethernet/fieldbus 포트만으로 분류하지 않는다. |
| prEN 50770-4 | OT VPN 기능 제품 | 드라이브 자체가 VPN 제품 기능을 제공/판매하는지 확인. 단순 원격 유지보수 경로 존재만으로 자동 분류하지 않는다. |
| prEN 50770-5 | OT 라우터·인터넷 연결 모뎀·스위치 | 드라이브의 내장 이더넷 스위치/포트 존재만으로 제품 전체를 라우터·스위치로 분류하지 않는다. 독립 제품의 intended purpose 확인 필요. |
| prEN 50770-6 | OT SIEM 시스템 | 드라이브는 일반적으로 SIEM 제품이 아니므로 직접 분류하지 않는다. 로그 제공/연동은 시스템 통합 및 증거 연결 이슈다. |

제품 모델, 데이터시트, intended purpose, 네트워크 아키텍처, BOM이 없는 현 시점에서는 drive-level product classification은 **Unknown / evidence pending**으로 유지한다. 보안 기능이 포함된 구성품의 공급자 증거 요구와 완제품의 Annex III 제품 카테고리 분류는 구분한다.

## 4. 출처와 확인 한계

1. CEN 공식 EN 40000-1-1 프로젝트 레코드:
   https://standards.cencenelec.eu/ords/f?cs=16635E5B87CB4221D8FFC1A74EC94EC6B&p=205:110:::::FSP_PROJECT,FSP_LANG_ID:82349,25
2. CEN 공식 FprEN 40000-1-3 프로젝트 레코드:
   https://standards.cencenelec.eu/ords/f?cs=15781C8F1FFD5C2E76320E51B347858F5&p=205:110:::::FSP_PROJECT,FSP_LANG_ID:81343,25
3. CENELEC 공식 prEN 50770-1~6 프로젝트 레코드:
   - https://standards.cencenelec.eu/ords/f?cs=13322EAD4BB9270452A937D8259179562&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81649,25
   - https://standards.cencenelec.eu/ords/f?cs=104E404C05717FFC5BCCAD860A2799EC6&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81650,25
   - https://standards.cencenelec.eu/ords/f?cs=1837AABAB3786CCFE6D25A2AB9BB4C78D&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81651,25
   - https://standards.cencenelec.eu/ords/f?cs=17583FCAF37D99F9A7028E7956E422300&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81652,25
   - https://standards.cencenelec.eu/ords/f?cs=1942B619B9CF8CEF79834DF9A4E0D3234&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81653,25
   - https://standards.cencenelec.eu/ords/f?cs=1D9131DB1242FEC8D93BF297195E8A2A0&p=305:110:::::FSP_PROJECT,FSP_LANG_ID:81654,25
4. CEN-CENELEC Work Item Plan tracker (2차 요약; 행별 공식 레코드 링크 포함):
   https://www.edge-sdn.com/regulations/cyber-resilience-act/standards/
5. EN 40000-1-2 개별 CEN-CENELEC 링크는 이번 점검에서 HTTP 500 오류로 본문 readback에 실패했다. Ratification date 2026-11-02 및 “No citation expected” 상태는 tracker와 독립 카탈로그에서 교차 확인했으나, 공식 개별 페이지의 성공적인 readback이 완료될 때까지 원문 확인 미완료로 표시한다.
6. European Commission Harmonised Standards index:
   https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards_en
   2026-11-18 확인 범위에서 CRA 전용 OJ 인용을 찾지 못했다. 이 결론은 조회 범위에 한정하며 신규 OJ publication은 추후 재확인한다.

## 5. 보고서 및 검증 규칙 변경

- 문서 상태값을 Draft / Under Approval / Ratified / Published by ESO / Cited in OJ로 분리한다.
- 각 행에 DOR, DAV, DOA, DOP, M/606 ESO adoption deadline, ESO publication forecast, actual OJ citation reference/date를 독립 필드로 둔다.
- “CRA standards not yet published” 같은 포괄적 표현은 제거하고 “EN 40000-1-1 is published by CEN but no CRA OJ citation is expected; no CRA OJ-cited reference identified in the checked index”로 정정한다.
- EN 40000-1-1 vocabulary part는 용어 일관성용이며 단독 기술 통제/적합성 표준으로 취급하지 않는다.
- EN 40000-1-2 risk-management framework와 EN 40000-1-3 vulnerability handling의 요구사항은 제품 증거·프로세스와 연결해 후속 분석한다.
- OT prEN 50770는 IEC 62443 기반 OT 제품 프로파일로 추적하되, 드라이브가 해당 제품 카테고리에 해당하는지는 intended purpose와 core functionality를 기준으로 한다.
- OJ citation expected는 실제 OJ citation이 아니다. Article 27 presumption of conformity는 정확한 OJ 참조 및 해당 표준의 적용 범위가 확인될 때만 주장한다.


## 중요 일정 정정 — C(2026) 7861 final (2026-11-10)

2026-11-10 Commission Implementing Decision C(2026) 7861 final이 M/606 Annex I을 대체했다. Commission CRA 표준화 페이지(최종 업데이트 2026-11-12)가 개정 사실을 명시한다. 기존 표/문장에 남아 있는 2026-10-30 납기는 아래 새 일정으로 읽어야 한다.

| M/606 Annex item | 범위 | 새 ESO adoption deadline |
|---|---|---|
| 1 | 위험기반 설계·개발·생산(framework, EN 40000-1-2 work) | 2026-11-30 |
| 15 | 취약점 처리(EN 40000-1-3 work) | 2026-11-30 |
| 2–14 | 일반 보안 요구 | 2027-10-30 |
| 16–41 | 수직 제품별 표준 | 2027-01-31 |

이 날짜는 ESO adoption deadline이며 발행일, OJ citation 또는 Article 27 추정 적합성 발생일이 아니다. 결정 Article 2에 따라 ESO가 수령 후 1개월 이내 개정사항을 수락하지 않는다고 통지하면 결정이 적용을 중단하는 조건이 있으므로, ESO 수령일/비수락 통지는 별도 확인 대상으로 둔다.

상세 근거와 영향 분석: [CRA M/606 개정 결정 추적](CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md).

공식 Commission 페이지: https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
결정문 사본: https://www.ibf-solutions.com/fileadmin/dateidownloads/c-2026-7861-main-document-annex-cra-standards.pdf

---


## 2026-11-20 공식 CEN 카탈로그 재조회 — EN 40000-1-1/-1-2 직접 readback

2026-11-19 CEN-CENELEC 공식 공지 이후 개별 CEN 카탈로그 레코드를 다시 열었다. 2026-11-18 본문에 남아 있던 EN 40000-1-2 공식 레코드 readback 미완료 상태를 종료한다.

| 표준 | CEN Work Item | Status | DOR | DAV | DOA | DOP/DOW | Citation in OJEU |
|---|---|---|---|---|---|---|---|
| EN 40000-1-1:2026 | JT013095 | Published | 2026-11-02 | 2026-11-18 | 2027-02-28 | 2027-05-31 | No citation expected for Directive 2024/2847 |
| EN 40000-1-2:2026 | JT013089 | Published | 2026-11-02 | 2026-11-18 | 2027-02-28 | 2027-05-31 | No citation expected for Directive 2024/2847 |

- EN 40000-1-1은 EN 40000 series vocabulary.
- EN 40000-1-2는 generic cybersecurity principles, product risk management, lifecycle activities를 다룬다.
- 두 EN은 CEN에서 Published이나 해당 CRA 지침에 대한 OJ citation을 기대하지 않는다고 CEN 레코드가 명시한다. 따라서 Article 27 presumption of conformity 근거로 사용하지 않는다.
- DAV는 official-language definitive text의 중앙 배포 가능일이다. DOA/DOP/DOW는 national announcement/publication/withdrawal implementation dates다.
- 표준 본문 자체는 구매·취득·검토하지 않았으며, 이번 검증은 CEN catalog metadata 및 CEN-CENELEC announcement에 한정한다.

공식 레코드:
- https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:82349,2307986
- https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:81335,2307986
- https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/

**정정:** 이전 문서에서 EN 40000-1-2의 개별 CEN 페이지 직접 확인이 미완료라고 한 부분은 이 addendum으로 해소됐다. 두 EN의 OJ field는 No citation expected다.


## 2026-11-20 추가 상태 정합성 감사 — prEN 50770 split 및 national-member records conflict

DKE 2026년 10월 CRA 표준화 상태 PDF는 기존 prEN 50770-1이 firewall용 prEN 50770-1-1과 IDS/IPS용 prEN 50770-1-2로 분할되었음을 명시한다. 따라서 기존 6개 시리즈 항목은 7개 deliverable로 추적한다.

DKE 표는 7개 deliverable 모두 Start NWI 및 Drafting prEN marker를 표시하고, Voting prEN 이후 단계 및 Citation hEN marker는 표시하지 않는다. 그러나 BSI national project records는 prEN 50770-2 (9025-12804)와 prEN 50770-3 (9025-12805)를 PWI로 표시하고 target dates가 알려지지 않았다고 설명한다. LVS CLC/TC 65X list는 WIID 81649–81654를 In development로 표시한다. DKE Drafting prEN, BSI PWI, LVS In development는 stage granularity가 일치하지 않는다.

이번 재조회에서는 CEN-CENELEC 중앙 project record를 성공적으로 다시 열지 못했다. 따라서 -2/-3의 정확한 중앙 stage, forecast 및 OJ citation field는 Unknown/Conflict로 유지한다. DKE Citation hEN 열은 비어 있고 actual OJ reference는 확인되지 않았다. 과거 “Citation expected” 표현은 실제 OJ citation으로 오인하지 않는다.

새 매핑: 36b → 50770-1-1 + 50770-1-2; 21b → -2; 25b → -3; 20b → -4; 27b → -5; 22b → -6. 기존 6-row matrix는 역사적 snapshot이며 새 7-deliverable CSV를 현행 기준으로 사용한다.

- DKE October 2026 PDF: https://www.dke.de/resource/blob/2435170/215c8695b21563a904c94beeb62214e9/normungsprojekte-zum-cra-data.pdf
- BSI -2 PWI: https://standardsdevelopment.bsigroup.com/projects/9025-12804
- BSI -3 PWI: https://standardsdevelopment.bsigroup.com/projects/9025-12805
- LVS CLC/TC 65X list: https://www.lvs.lv/en/committees/projects/10907?Projects_page=12&Projects_sort=pr_number.desc
