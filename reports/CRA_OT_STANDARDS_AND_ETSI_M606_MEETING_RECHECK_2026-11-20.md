# CRA OT 표준화 실시간 재확인 — 2026-11-20

## 목적과 범위

기존 CRA 조사에서 미확인으로 남은 CLC/TC 65X OT 프로파일 prEN 50770-2~6의 WIID 매핑·공개 상태를 독립 출처로 재확인하고, ETSI M/606 AMD 1 회의 일정을 공식 일정표에서 재검증했다. 이번 확인은 표준 전문 또는 중앙 CENELEC 프로젝트의 내부 stage history를 확보한 것이 아니다.

## 1. CENELEC OT WIID 매핑 — 독립 재확인

CENELEC/CLC-TC65X WG3의 2026-05-07 공식 발표자료는 다음 대응관계를 명시한다.

| WIID | OT deliverable | 범위 |
|---:|---|---|
| 81649 | prEN 50770-1 | Firewall 및 IDS/IPS (후속 -1-1/-1-2 분할 상태는 별도) |
| 81650 | prEN 50770-2 | Network management systems |
| 81651 | prEN 50770-3 | Physical/virtual network interfaces |
| 81652 | prEN 50770-4 | VPN-function products |
| 81653 | prEN 50770-5 | Internet routers/modems/switches |
| 81654 | prEN 50770-6 | SIEM systems |

공식 발표자료: https://www.cencenelec.eu/media/CEN-CENELEC/Events/Webinars/2026/2026-05-07_cra_unlocked_clc-tc65x-wg3-acs-technical-requirements.pdf

2026-11-20 재검색한 LVS(라트비아 표준화기관) CLC/TC 65X 공개 프로젝트 목록에서도 WIID 81650, 81651, 81652, 81653, 81654가 각각 위 prEN 50770-2~6 제목과 연결되어 있으며 상태는 모두 “In development”로 표시된다.

LVS 목록: https://www.lvs.lv/en/committees/projects/10907?Projects_page=12&Projects_sort=pr_number.desc

### 판정과 한계

- WIID ↔ part number ↔ 제목 매핑은 CENELEC 공식 발표자료와 국가표준기관 공개목록이 상호 뒷받침한다.
- LVS의 “In development”는 개발 중이라는 넓은 상태만 의미한다. CENELEC 중앙 카탈로그의 Drafting prEN/PWI/Committee stage, DOR, DAV, 예정 투표일을 대체하지 않는다.
- 이번 웹 재검색에서도 WIID 81650~81654의 중앙 CENELEC 개별 live record를 직접 열람하지 못했다. 따라서 중앙 stage/DOR/DAV 및 OJ citation은 여전히 Unknown.
- DKE national tracker의 Drafting prEN과 BSI의 81650/81651 PWI 표기 충돌은 해소되지 않았다. LVS의 “In development”만으로 어느 쪽 stage가 정확한지 판정하지 않는다.
- 81649는 중앙 record의 단일 parent prEN 50770-1과 DKE의 -1-1/-1-2 분할 기록 사이 synchronization 차이가 계속 남아 있다.
- OJ citation이 확인되지 않았으므로 CRA Article 27 적합성 추정(presumption of conformity)을 주장하지 않는다.

## 2. ETSI M/606 AMD 1 공식 일정 재확인

ETSI Portal의 공식 TB calendar 검색 결과는 “GoSRSReq006-M/606 AMD 1 - examination meeting”을 **2026-11-23, Online**으로 표시한다.

- 공식 ETSI calendar/TB portal: https://portal.etsi.org/tb.aspx?tbid=218
- 조회일: 2026-11-20
- 확인한 사실: 일정 항목명, 날짜(11월 23일), 온라인 개최 표시.
- 확인하지 못한 사실: 회의 안건 전문, 참석/개최 여부, 회의록, 결의, M/606 개정 수락 여부, CEN/CENELEC/ETSI의 C(2026)7861 수령일 또는 Article 2 비수락 통지.

따라서 이 일정은 미래 일정으로만 기록한다. 회의가 이미 개최되었다거나 개정안이 승인/수락되었다고 표현하지 않는다. 11월 23일 이후 공식 회의록/Work Programme/ESO 통지 원문을 재조회해야 한다.

## 3. 다음 확인 순서

1. 2026-11-23 이후 ETSI 회의 결과·회의록·M/606 AMD 1 결정 및 Work Programme 18개 항목 상태 재조회.
2. CEN/CENELEC/ETSI 각각 C(2026)7861 수령일과 acceptance/non-acceptance notice 원문 확보. 발송일을 수령일로 간주하지 않는다.
3. CENELEC 81650~81654 중앙 개별 record 및 81649 parent/child synchronization 직접 재확인.
4. M/606 41개 Annex I 주제 ↔ ESO work item ↔ 실제 EN/ETSI deliverable ↔ OJ citation crosswalk를 계속 갱신한다.
5. 실제 OJ reference가 확인될 때까지 Article 27 presumption은 미확정으로 유지한다.

## 4. 증거 수준

| 항목 | 상태 | 증거 수준 |
|---|---|---|
| WIID 81650~81654 ↔ prEN 50770-2~6 매핑 | 확인 | CENELEC 공식 발표자료 + LVS 공개 프로젝트 목록 |
| 81650~81654 최신 중앙 CENELEC stage/DOR/DAV | 미확인 | 중앙 live record 직접 열람 실패 |
| 국가별 stage 충돌(DKE vs BSI) | 미해결 | 국가표준기관별 공개자료 상이 |
| ETSI M/606 AMD 1 회의 일정 | 확인 | ETSI 공식 일정표에 2026-11-23 Online 표시 |
| 회의 결과/수락/ESO receipt | 미확인 | 회의 전이며 원문 미확보 |
| Article 27 OJ citation | 미확인 | 실제 OJ reference 증거 없음 |

