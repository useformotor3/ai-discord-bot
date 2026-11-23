## 2026-11-23 — LS메카피온 제품군 증거 등록 및 PR #203 검증 동기화

- PR #203 병합 완료: merge SHA `584a7c092ea434d52f7794452ca85b0cbe981210`.
- PR exact-head Run #1343 / ID `45133630273`: success. Main push Run #1344 / ID `45133730871`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- 복구 기준점: `safety/post-merge-pr203-2026-11-23`.
- LS메카피온 공식 드라이브 페이지에서 iX700M, iX7M, iX7NH, L7NHA/B, L7NHF, L7PA/B, PHOX, L7C, L7SA/B, GEM 제품군을 확인. 제품군별 전압·용량·통신 유형이 달라 단일 SKU처럼 다루지 않음.
- iX700M 공개 모델코드 예시 `iX700MD1-B-150B`의 코드 구성은 제조사 인증서 페이지에서 확인. 실제 대상 모델이라고 단정하지 않음.
- 통합 보고서 작업 브랜치 v0.15 → v0.16, §46 추가. 상세 증거 등록부 `reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md` 작성.
- iX700M Ver1.4 매뉴얼 및 PEGA2 Ver1.3 매뉴얼의 제조사 목록 메타데이터는 확인했으나, iX700M Ver1.4 본문 PDF는 확보하지 못함. 미열람 내용을 검증된 사실처럼 쓰지 않음.
- 제품별 Annex III/IV 분류는 정확한 실제 SKU, HW/FW, ST MCU order code 미확보로 Unknown 유지.
- 범위: CRA only. SIL 3 제외. 운영 코드, workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — PR #202 병합 및 main 검증 완료

- PR #202 병합 완료: https://github.com/useformotor3/ai-discord-bot/pull/202
- squash merge SHA: `794d2d69c6a46e85d5cc64c7c0c337a7493ebcc4`
- 보고서 main read-back: v0.15, §45 및 §45.7 확인.
- 최신 매트릭스 Markdown/CSV main read-back 확인: 18개 데이터 행, CSV 21개 열, 모든 행의 열 수 일치.
- PR exact-head Run #1341 / ID `45133314471`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- main push Run #1342 / ID `45133462189`: success. 전체 테스트·CRA traceability·공식 PDF/HTML canary·provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- post-merge 복구 기준점: `safety/post-merge-pr202-2026-11-23`.
- PROJECT_LOG에는 이번 상태 갱신 이벤트를 추가한다. 제품별 분류는 LS메카피온 정확한 모델 및 ST MCU 주문 코드가 확보되기 전까지 Unknown.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — ETSI M/606 18개 Work Item live status 재점검

- 공식 ETSI active list 재조회: 2026-11-23 / Work Programme v2.3.3 / 18 active items.
- 통합 CRA 보고서 작업 브랜치에서 v0.14 → v0.15, §45 추가. 11월 20일 스냅샷과 구분해 11월 23일 최신 상태를 별도 기록.
- 새 매트릭스: `reports/CRA_ETSI_M606_18_ACTIVE_WORK_ITEM_MASTER_MATRIX_2026-11-23.md` 및 `.csv`. CSV는 18개 데이터 행, 20개 열, 모든 행 열 수 일치 확인.
- 중요 버전 변경: EN 304 619 V1.0.3, EN 304 635 V1.0.9. EN 304 635 상태는 EC assessment before WNV requested (2026-11-19), 다음 단계 2026-11-28로 표시.
- EN 304 617/618/620/621/622/623/625/626/627/631/632/633/634/636의 최신 active-list status 및 next-stage dates를 snapshot에 반영. EN 304 624는 11월 23일 최신 목록의 상세 행을 재확인하지 못해 이전 monitoring snapshot으로 구분.
- ETSI status milestone는 계획 단계다. 표준 채택·발행·OJ citation 또는 CRA Article 27 presumption으로 해석하지 않는다.
- 2026-11-23 GoSRSReq006-M/606 AMD 1 회의는 ETSI calendar의 일정 게시만 확인. 개최 결과·회의록·ESO 수령일/비수락 통지는 Unknown.
- PR #201 병합: merge SHA `0643c656b7801fcaf4453042e97623f2e57d73cd`. PR exact-head Run #1337 / ID `45123857980` success. Main push Run #1338 / ID `45132883785`는 마지막 확인 시점에 진행 중(공식 PDF canary 이후 단계 확인 필요).
- 복구 기준점: `safety/post-merge-pr201-2026-11-23`.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API cadence 변경 없음.

## 2026-11-23 — PR #200 병합 및 CRA Annex III MCU 분류 정밀화

- PR #200: https://github.com/useformotor3/ai-discord-bot/pull/200 — squash merge 완료.
- merge SHA: `53d91ee5beb16f703bbaddc3ec64dd238989d55a`; exact PR head: `bced199d83a1f6ee9a9948951851d2dafb2f5740`.
- 보고서 `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` main read-back: **v0.14**, §44 확인. Annex III Class I point 14 / Class II point 4와 M/606 item 29 / 38 번호 체계, Reg. (EU) 2025/2392 MCU technical descriptions, Article 7 core-functionality/component-integration 경계를 추가.
- PR exact-head Actions Run #1331 / ID `45114851876`: success. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, PDF evidence upload 및 provenance manifest upload 성공.
- post-merge safety ref: `safety/post-merge-pr200-2026-11-23` (merge SHA 기준).
- main push Actions Run #1332 / ID `45123598545`: **success**. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, provenance manifest upload 모두 성공. PDF evidence upload은 변경 없음 조건으로 skipped(실패 아님).
- 제품 판정 경계: ST MCU 정확한 order code·보안 구성 및 LS메카피온 정확한 SKU/HW/FW/BOM이 확보되지 않아 MCU/완제품 Annex III 분류는 Unknown. 부품 내장만으로 완제품 분류가 자동 승계되지 않지만 완제품 CRA 기본 의무는 유지.
- ETSI GoSRSReq006-M/606 AMD 1 examination meeting은 공식 ETSI calendar에서 2026-11-23 온라인 일정으로 재확인. 일정 게시만 확인되며 회의 결과·회의록·ESO 수령일/비수락 통지는 여전히 Unknown.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, API 호출 주기 변경 없음.

# 프로젝트 상황판 — 2026-11-23 (운영 자동화 기준 상세 기록: 2026-11-20)

- **PR #189 병합 완료:** `1683b5ec780c7396309d85b86cba100a021194e4` (squash). main read-back 동일.
- **현재 운영 schedule:** `17 */3 * * *` — UTC 매 3시간 17분. 기존 3시간 간격을 유지하고 정각(:00) 부하를 피하도록 이동. 5분 주기 아님.
- **관측성 개선:** `main.py` stdout/stderr runner 임시 로그 tee, 원래 exit code 보존, GitHub Actions Step Summary에 조사 결과·공식 source count·모델 폴백 사유·archive·Discord 상태를 분리 표시.
- **검증:** PR exact-head Run #1289 success, 183 passed / 0 failed. main push Run #1290 / ID `44742940672` success, **183 passed / 0 failed**. Source identity, compileall, CRA traceability, official PDF/HTML canaries, provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- **복구 기준:** pre-merge `safety/pre-merge-pr189-automation-observability-2026-11-20` 및 post-merge `safety/post-merge-pr189-automation-observability-2026-11-20` 모두 merge point main SHA와 동일.
- **기존 실행 품질:** 최근 26개 schedule job은 모두 success였지만 실제 시작 지연은 49~71분(평균 59분, 중앙값 58분). Run #2523은 공식 source 10개를 확보했으나 Gemini 3.8 Flash가 EUR-Lex 링크 누락으로 품질 탈락, 3.5 Flash Lite 전환 후 신규 주제 없음으로 종료. 보고서·archive·Discord 변경은 없었고 guard/pruning은 성공.
- **다음 운영 확인:** 새 cron 첫 예상 슬롯은 2026-11-20 15:17 UTC (한국시간 2026-11-21 00:17). 실제 GitHub schedule은 지연될 수 있으므로 다음 실행에서 새 Step Summary가 `NO_NEW_TOPIC`/폴백 사유를 정확히 표시하는지 확인한다. 아직 새 summary를 production에서 검증한 것은 아님.
- **5분 자동화:** GitHub Actions에 5분 production Gemini 실행을 설정하지 않았다. 하루 최대 288회 호출과 quota/중복/queue 위험 때문에 현 3시간 주기를 유지. 5분 모니터가 필요하면 Gemini/Discord/운영 데이터 쓰기 없는 read-only heartbeat로 별도 설계한다.
- **ChatGPT 예약 작업:** 주간 CRA·MCU 공식자료 점검 enabled; 일일 Git 브랜치 통합 점검과 CRA 보고서 대기열 점검 disabled. 5분 task는 확인되지 않았다.

---

## 최신 기준점 — ETSI M/606 18개 조사 및 최신 draft 재검증 (2026-11-20)

- 기준 main SHA: 8adf72f3bbda24165479f7aa4d4246d48e4acd99; PR #184, #185, #186 merged 2026-11-20. PR #185/#186 are post-merge documentation synchronization and self-review correction. 조사 브랜치: research/cra-etsi-18-active-matrix-class-audit-2026-11-20 (merged); pre-merge safety: safety/pre-merge-pr184-2026-11-20; post-merge safety refs: safety/post-merge-pr184-2026-11-20 (main as of PR184), safety/post-merge-pr185-2026-11-20, safety/post-merge-pr186-2026-11-20 (latest verified identical to main).
- Full 18-item M/606 master matrix added. EN 304 635 and EN 304 636 ETSI page metadata says Class I but Regulation 2025/2392 classifies both Class II. Latest EN304636 V1.0.0 PDF page 9 explicitly says Class II point 2; current Work Item page Class I label is stale metadata. EN304635 V1.0.1 public 15-page sample inspected: document p.15 Scope explicitly says Class II point 1. Latest public drafts for both EN304635/636 align with law; full 386-page EN304635 PDF not acquired.
- EN 304 627 industrial OT exclusion added; total OT exclusions tracked: EN 304 620/621/622/627.
- Next P0: obtain the complete 386-page EN304635 V1.0.1 PDF from the official ETSI download service if access permits; current 15-page sample already confirms Class II point 1. Then prepare an evidence-backed ETSI metadata clarification request, monitor official ETSI calendar event GoSRSReq006-M/606 AMD 1 - examination meeting on 2026-11-23; minutes/decision and ESO acceptance remain pending, CENELEC official WG3 mapping 81650–81654 is now cross-checked against the 2026-05-07 CENELEC presentation; direct individual catalogue stage/DOR/DAV readback remains pending, as does 81649 parent/child sync and actual OJ citations. Do not use Class I Article32 route for these categories.
- PR #184 final exact-head CI Run #1238 (commit 3dc3af115769ef2380a8895d41b0eced04b67fff): success; 174 passed / 0 failed; source integrity, compile, CRA traceability, live official CRA PDF/HTML canaries and provenance manifest upload succeeded. Squash merge commit: 9dbe6e92c358d0361f9640651152e4d1e8b1ec6b. Follow-up doc sync PR185 merged as ebc6fda0f2a89be0e5306a00fb12ac7b0d2802bf; no-op banner correction PR186 merged as 8adf72f3bbda24165479f7aa4d4246d48e4acd99.

---

## 최신 재개 상태 — ETSI M/606 18개 통합 매트릭스 및 법령 분류 오류 발견 (2026-11-20)

- ETSI Work Programme v2.3.3 M/606 active 18개 Work Item 상세 레코드를 통합 매트릭스로 정리. 17개는 Annex I vertical topics 17–27,31–36; EN 304 642는 telecom supporting work item으로 직접 41-topic mapping 미확인.
- EN 304 635(hypervisors) 및 EN 304 636(firewalls/IDS/IPS)의 ETSI scope text는 Class I로 표시하지만 Regulation 2025/2392는 각각 Class II category 1/2로 분류한다. 법령이 우선. 최신 공개 draft sample/full preview를 확인해 EN304635 V1.0.1 p.15 Class II point 1, EN304636 V1.0.0 p.9 Class II point 2를 확인했다. Work Item page metadata discrepancy로 범위를 좁힌다.
- EN 304 627 routers/modems/switches도 industrial OT 장비를 ETSI scope에서 제외한다. EN 304 620/621/622와 함께 OT exclusion 4개를 관리.
- 18개 모두 Harmonised Standard metadata Yes이나 OJ field blank; actual OJ citation/Article27 presumption 미확인.
- 다음 P0: EN304635 V1.0.1 전체 386쪽 원본 확보 가능성 확인; 두 최신 draft Class II 본문 근거로 ETSI metadata correction tracking; 2026-11-23 ETSI M/606 AMD1 meeting; ESO Article2 receipt/acceptance; CENELEC 81650–81654 direct records; OJ index crosswalk.
- 상세: reports/CRA_ETSI_M606_18_ACTIVE_WORK_ITEM_MASTER_MATRIX_2026-11-20.md 및 CSV.

---

## 최신 재개 상태 — PR #182 CRA 표준화·제품분류 분석 병합 완료 (2026-11-20)

- Main merge SHA: 904b2ed0897331ced9dedfcbd25afd608f92f951; PR #182 head ad57c7cc2595be0a42d1686fde5870fb2ab5cec8; post-merge safety ref safety/post-merge-pr182-cra-standardization-classification-2026-11-20.
- Exact-head Actions Run #1177 / ID 44713888650: success; 174 passed / 0 failed; source blob integrity, compile, CRA traceability and full pytest passed.
- Traceability readback: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, M/606 mapping 41, PROJECT_LOG 279 events (274 modern IDs + 5 legacy), bidirectional links true.
- Official CRA HTML source canary and provenance manifest upload passed. CRA Guidance PDF canary returned empty body and was explicitly skipped; no PDF verification claimed.
- Integrated report v0.9 includes ETSI 8-item audit, CLC/TC 65X OT 7-deliverable reconciliation, C(2026)7861 Article 2/Annex I deadlines, Annex III/IV core-functionality and Article 32 route analysis.
- ETSI EN 304 620/621/622 explicitly exclude industrial OT in scope. 8 reviewed records have blank OJ fields; no Article 27 presumption claimed.
- CENELEC official WG3 presentation confirms mapping 81649→prEN 50770-1; 81650→-2; 81651→-3; 81652→-4; 81653→-5; 81654→-6. DKE Oct-2026 national tracker shows seven deliverables (including -1-1/-1-2 split) at Drafting prEN. Central individual stage/DOR/DAV for 81650–81654 and 81649 child record synchronization remain unverified.
- C(2026)7861 Annex I deadlines: 1/15=2026-11-30; 2–14=2027-10-30; 16–41=2027-01-31. Article 2 receipt-based one-month non-acceptance condition remains Unknown pending ESO receipt/notice evidence.
- Annex III/IV and Article 32 matrix completed; product-level classification/route remains Unknown pending exact SKU, BOM, firmware and separately marketed interface/MCU evidence. Security tests Not Run.
- Main push-triggered CI after merge was not separately verified through the available GitHub connector; PR exact-head CI #1177 is verified.

---

## 최신 법률 분석 — Annex III/IV 및 Article 32 서보 드라이브 분류 기준 (2026-11-20)

- Article 2(1) data connection scope, Article 7(1) core functionality/component integration, Reg. (EU) 2025/2392 category technical descriptions, Article 32 conformity routes를 공식 EUR-Lex 원문으로 분석.
- Fieldbus/network-interface controller/adapter는 Annex III Class I category 10 기술 설명에 포함된다. 내장 포트만으로 완제품 드라이브를 자동 Class I로 분류하지 않지만, 별도 판매 interface module은 별도 제품 경계로 검토한다.
- Security-function MCU, RTOS, NMS/VPN/SIEM, router/switch, firewall/IDS/IPS, Annex IV security box/secure element는 각 기술 설명과 완제품 core function을 구분한다.
- Article 32: 일반제품 32(1), Class I 32(2), Class II 32(3), critical Annex IV 32(4)/Article 8(1) 조건부 경로를 matrix로 정리.
- 정확한 SKU/BOM/FW/별도 판매 interface board/MCU 증거 미확보로 제품별 Annex III/IV 및 Module route는 Unknown 유지.

---

## 추가 재개 메모 — CENELEC project 81649 직접 확인 (2026-11-20)

- CENELEC 중앙 record 81649 direct readback: prEN 50770-1 단일 부모 project, combined firewall + IDS/IPS scope, Committee stage, Citation expected, DOR/DAV 미기재. DKE Oct-2026의 -1-1/-1-2 분할과 central record가 다르므로 naming/record synchronization discrepancy 유지.
- CENELEC 81650–81654 direct readback는 이번 pass에서 실패. 81650/81651은 DKE Drafting prEN vs BSI PWI conflict, 81652–81654는 prior 2026-11-18 central snapshot 외 신규 direct confirmation 없음.

---

## 최신 재개 상태 — ETSI 8개 M/606 상세 감사 및 OT 표준화 상태 정정 (2026-11-20)

- 기준 main: PR #181 status-sync merge SHA 2239298939e6e5908a18cece796ab0da7250d219; 현재 조사 브랜치 research/cra-etsi-m606-8items-cen-ot-audit-2026-11-20.
- ETSI Work Programme v2.3.3에서 기존 미검토 8개 EN 304 617–624 상세 레코드를 개별 확인. scope/version/status/next milestone/Harmonised Standard metadata/OJ field 기록 완료.
- EN 304 620(VPN), EN 304 621(NMS), EN 304 622(SIEM)은 industrial OT domain 제외가 scope에 명시됨. 8개 모두 OJ field blank; Harmonised Standard=Yes는 후보 metadata이지 OJ citation이 아님.
- CLC/TC 65X prEN 50770-1은 -1-1 firewall / -1-2 IDS/IPS로 분할되어 7개 deliverable. DKE Oct-2026은 Drafting prEN, BSI는 -2/-3 PWI/target dates unknown, LVS는 In development로 표시. 중앙 CENELEC record 재확인 실패; stage conflict 유지.
- C(2026)7861 Annex I: 1/15=2026-11-30; 2–14=2027-10-30; 16–41=2027-01-31. Article 2 one-month non-acceptance condition은 ESO 실제 수령일 기준이며 receipt/acceptance evidence Unknown.
- ETSI GoSRSReq006-M/606 AMD 1 examination meeting 2026-11-23 예정; 11/20 현재 미래 일정.
- 신규 통합 감사 보고서와 2개 CSV 추가; 통합 보고서 v0.6, CEN 상태 감사, M/606 41-item item36 mapping 갱신.
- 다음 P0: 11/23 ETSI meeting minutes/decision; CEN/CENELEC central record로 DKE/BSI stage conflict 해소; ESO receipt/acceptance notice 확보; 18개 전체 consolidated matrix; 41개 OJ citation crosswalk; Annex III/IV 및 Article 32 route mapping.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.

---

## 최신 재개 상태 — PR #180 AI 자기검토·연속성 기준 병합 완료 (2026-11-20)

- PR #180 squash merge SHA: `3ded54116b3ecfa77645c50ada45575fbe656aea`; head `0b0f13b9b7844857c30e724e2f44691b76d92a66`; 변경 4 files / +140 lines.
- Exact-head Actions Run #1162 / ID `44711023208`: success. Source blob identity, compile, CRA traceability, full pytest **174 passed / 0 failed**, official CRA HTML source canary and provenance manifest upload passed.
- PDF canary returned an empty body for Commission Guidance CELEX `52026XC06013`; PDF acquisition/upload explicitly skipped. Do not infer PDF verification.
- New operational standard: `reports/AI_SESSION_CONTINUITY_SELF_REVIEW_AND_TOKEN_EFFICIENCY_2026-11-20.md`; AI_RULEBOOK §11, MASTER_PLAN, SESSION_LOG updated.
- Pre-merge safety ref `safety/pre-merge-pr180-ai-self-review-2026-11-20`; post-merge safety ref `safety/post-merge-pr180-ai-self-review-2026-11-20`. Post ref created at merge SHA; read-back verification pending this status-sync PR.
- Scope: documentation only; no runtime code/workflow/secrets/state/history or SIL 3 preservation files changed.
- CRA next P0 remains: finish individual ETSI M/606 records and scope, verify CEN/CENELEC OT prEN 50770 project states, confirm ESO Article 2 acceptance/receipt evidence for C(2026)7861, map all 41 items and OJ citations, then Annex III/IV + Article 32 mapping.
- Product-level scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.

---

## 최신 재개 상태 — PR #178 CRA 핵심 업데이트 병합 완료 (2026-11-20)

- PR #178 squash merge 완료. merge SHA `8abf70a68add7f0e7a38283da3dd3d78c160829c`; exact head `21b11774933e9b3a6c67922eddbb6bbb907439d4`.
- main read-back/compare: merge SHA와 identical. post-merge safety ref `safety/post-merge-pr178-2026-11-20`; pre-work safety ref `safety/pre-cra-core-implementation-refresh-2026-11-20`.
- Exact-head Actions Run #1158 / ID `44709421086`: success. Full pytest **174 passed / 0 failed**, source integrity, compile, CRA traceability, official source canary and provenance manifest upload passed.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional links true, M/606 mapping 41, PROJECT_LOG 274 events (269 modern IDs + 5 legacy).
- Provenance artifact #14616666445, 2,567 bytes, SHA-256 `77061f3b46331afb3ce9c1f8b60ce116754f4f4bb6c817ccdc8af1f4fa58ab54`. PDF evidence upload step skipped; original PDF acquisition must not be inferred.
- CRA 통합 보고서 v0.5 §§25–28, SRP 운영 기준서, 21-source freshness register, ETSI/CEN status addenda 반영.
- 핵심 다음 작업: ETSI M/606 미검토 8개 work item 상세 전수 확인, CEN/CENELEC prEN 50770-1~6 개별 최신상태 확인, C(2026)7861 Annex I 41개 기한/ESO 수락 통지 대조, CRA Annex III/IV 분류·Article 32 route 검토.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 현재 CRA 전체 프로젝트가 중심이며 LS메카피온 iX7NH는 하나의 사례연구다.

---

## 최신 재개 상태 — CRA 핵심 규제·표준화 최신정보 갱신 (2026-11-20)

- 활성 프로젝트는 CRA 전체 규제·표준화·제품 적용성·보안·신고 체계. LS메카피온 iX7NH는 사례연구일 뿐 핵심 CRA 조사 우선순위를 대체하지 않는다.
- 기준 main SHA `07d6d3b1d8f91637da7b6a9a023b2f4ec64e7efd`; 작업 브랜치 `research/cra-core-implementation-refresh-2026-11-20`; pre-safety ref `safety/pre-cra-core-implementation-refresh-2026-11-20`.
- 통합 보고서 v0.5 §25–§28 작업 브랜치 반영: ENISA SRP FAQ/Glossary/AR Manual 최신 운영 제약, CEN EN 40000-1-1/-1-2 Published but no CRA OJ citation, ETSI M/606 active 18 work items 및 관련 work item scope/status를 반영.
- 중요 정정: ETSI EN 304 625의 기존 2026-09-28 “7 VR” 상태는 outdated; 2026-11-20 상세 레코드는 Comments categorisation assessed (2026-11-05), 2026-11-19 EC second-assessment remark 확인.
- 신규 문서: `CRA_SRP_OPERATIONAL_READINESS_2026-11-20.md`, `CRA_LIVE_SOURCE_FRESHNESS_REGISTER_2026-11-20.csv`; ETSI/CEN 상태 보고서에 Nov20 addendum.
- 검증 한계: ENISA HTML parsed; raw hash 미확보. AR Manual metadata only. ETSI active 18 중 list 10 visible, selected records only. CEN prEN50770-1~6 Nov20 individual re-read not completed. OJ actual reference not found in these work-item records.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.

---

## 최신 재개 상태 — CRA 핵심 이행 최신정보 갱신 작업 (2026-11-20)

- 현재 활성 목표는 CRA 전체 규제·표준화·제품 적용성·보안·신고 체계다. LS메카피온 iX7NH는 제품 사례연구이며 CRA 조사 우선순위를 대체하지 않는다.
- 기준 main SHA: `07d6d3b1d8f91637da7b6a9a023b2f4ec64e7efd`; 작업 브랜치: `research/cra-core-implementation-refresh-2026-11-20`; 사전 복구 ref: `safety/pre-cra-core-implementation-refresh-2026-11-20`.
- CRA 통합 보고서 v0.3로 갱신 중. 신규 §25는 2026-11-20 기준 Commission/ENISA 최신 이행자료를 대조하고 SRP 실제 운영 제약을 정리한다.
- 신규 ENISA 공식 확인: SRP FAQ 2026-10-15, Glossary v1.6 2026-10-21, AR User Manual v1.3 2026-11-04. API 미제공, 영어 UI, Article 15 미구현, 72h UI counter와 법정 시한 불일치 가능성 등 반영.
- 신규 산출물: `reports/CRA_SRP_OPERATIONAL_READINESS_2026-11-20.md`, `reports/CRA_LIVE_SOURCE_FRESHNESS_REGISTER_2026-11-20.csv`.
- 검증 제한: ENISA FAQ/Glossary HTML parsed; raw bytes/hash 미확보. AR User Manual은 버전/날짜 메타데이터만 확인, PDF 본문 미검토. SRP status endpoint 열람 실패; live platform test 미실시.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, 보안시험 Not Run. 법적 정확성 100% 또는 제품 적합성 완료를 주장하지 않는다.

---

## 최신 재개 상태 — PR #173 병합 및 iX7NH Ver1.7/API 증거 갱신 완료 (2026-11-20)

- PR #173 squash 병합: main SHA `634c3178471ff20c99e97ba48fc4c5e187afb28d`; 연구 브랜치 exact head `2e536ed1cd893e433b0aab6b98185c40bff3ff8a`.
- Exact-head Actions Run #1148 / ID `44702831239`: success. Source blob integrity, compileall, CRA traceability 통과; full pytest **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional links true, M/606 41, PROJECT_LOG 266 events (261 modern IDs + 5 legacy).
- Official live source canary fetched 10 allowlisted official sources and verified CRA text/locators. One separate CRA PDF URL returned empty body and was explicitly skipped as temporary outage; overall workflow succeeded.
- Provenance artifact #14613259125, 2,567 bytes, SHA-256 `22b402eeb9c351c65210a80c47d7f0deb6cc2526383138b12c2c96d892ca73c1`.
- 통합 보고서 v0.20 §40–§41 main 반영. §40: LS메카피온 Ver1.7/API 공식 첨부 메타데이터 확인; 첨부 다운로드 TimeoutError로 원본 bytes·SHA-256·본문 미확보. §41: AutomationDirect 2026 Modbus TCP 가이드 14페이지 본문을 2차 자료로 검토.
- 2차 자료의 Node 98/99, Modbus timeout, 쓰기 제어면은 LS메카피온 최신 원문/정확 SKU·펌웨어로 확인 전까지 제조사 확정사양 아님.
- 사전 복구 ref `safety/pre-ix7nh-v17-api-audit-2026-11-20`; 사후 ref `safety/post-merge-pr173-2026-11-20`; post ref == main 확인.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run. 실기기/네트워크 시험 및 쓰기/운전 명령 미수행.
- main `protected=false` 상태 유지. 운영 코드/workflow/secrets/state/history/SIL 3 보존 산출물 미변경.

---

## 최신 재개 상태 — iX7NH Ver1.7/API 메타데이터 및 2026 Modbus TCP 보충 가이드 검토 (2026-11-20)

- 기준 main: `1d66302539d7d0cbb33780590251898ac76bb1ea`; 작업 브랜치 `research/ix7nh-v17-api-source-audit-2026-11-20`; 문서 전용.
- 통합 보고서 v0.20 §40–§41 반영. §40: LS메카피온 공식 Ver1.7 매뉴얼/API 첨부파일 메타데이터 확인. 공식 다운로드는 TimeoutError로 원본 bytes·SHA-256·본문 미확보.
- §41: AutomationDirect의 2026-05-05 iX7NH Modbus TCP Communication Guide(1st Ed Rev B) 14페이지 웹 파싱 본문 검토. 제조사 매뉴얼을 대체하지 않는 2차 자료로 분리 기록.
- 2차 가이드 주요 주장: Node 99=Modbus TCP+내장 웹서버, Node 98=Modbus TCP without webserver (firmware >=1.15), 내장 Modbus TCP timeout 없음(PLC 측 감시 권고), 제어 코일/Control Word/Target Position/Procedure Command의 RW 제어면. 실제 SKU·펌웨어 적용성과 모든 내용은 LS메카피온 공식 원문/기기에서 미검증.
- 제조사 인벤토리: Ver1.7 및 API 첨부는 metadata_only; AutomationDirect 보충 가이드는 web_parsed_text_reviewed, source_type=distributor_technical_guide_pdf로 별도 분리.
- 어떤 실기기·네트워크 시험도 하지 않았으며 쓰기/운전 명령을 실행하지 않음. 500 ms는 2차 가이드 예시일 뿐 안전 반응시간/안전기능으로 채택 금지.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 다음 P0: LS메카피온에 Node 98/99, timeout 동작, Modbus 쓰기 권한, Ver1.7 적용 펌웨어/SKU 및 공식 첨부 대체 다운로드를 서면 확인. 원본 확보 후 SHA-256 및 Ver1.1 대비 분석.
- 운영 코드/workflow/secrets/state/history/SIL 3 보존 산출물 미변경.

---

## 최신 재개 상태 — iX7NH Ver1.7·Modbus TCP API 공식 자료실 재감사 (2026-11-20)

- 기준 main: `1d66302539d7d0cbb33780590251898ac76bb1ea`; 문서 전용 작업 브랜치 `research/ix7nh-v17-api-source-audit-2026-11-20`.
- 통합 보고서 v0.19 §40 추가: LS메카피온 공식 Ver1.7 매뉴얼 게시물 및 Modbus TCP API 자료실 첨부 메타데이터 재검증.
- Ver1.7 첨부: `iX7NH_KOR_Ver1.7_260605.pdf`, 19.5 MB, 게시물 작성일 2021-05-14 / 첨부 표시일 2026-06-05.
- API 게시물 첨부: 테스트 가이드 PDF 1.3 MB, `iX7NH_TCP_API.zip` 69.8 MB, `x64.zip` 44.6 KB, `APIv1.02_20210505 1.pdf` 1.5 MB (첨부 표시일 2026-01-20).
- 공식 HTML 게시물/파일명/크기/날짜 확인 완료. 첨부 다운로드는 이번 세션에서 TimeoutError; 원본 bytes·SHA-256·본문/API 코드 미확보. 따라서 report/inventory status는 metadata_only, bytes_acquired=false, sha256=not_computed.
- Ver1.1 증거를 Ver1.7 현행 동작으로 전이하지 않음. 제품 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 다음 P0: 제조사 고객지원에 Ver1.7 및 API 원본의 대체 다운로드 URL 요청, 원본 취득 후 SHA-256/페이지·개정표 기록, Ver1.1 대비 페이지별 차이 분석.
- 운영 코드/workflow/secrets/state/history/SIL 3 보존 산출물 미변경.

---

## 최신 재개 상태 — PR #170 연구 병합 및 PR #171 상태 동기화 완료 (2026-11-20)

- 연구 변경 main 병합: PR #170 squash SHA `cad75135996c129bc576d83ce5b7ed968ca6a63b`; iX7NH Ver1.1 원문 감사 보고서 v0.18 §39 및 제조사 인벤토리 26행 반영.
- PR #170 exact head `8af0834e56c8ec8cd4c13d900a5fe77c0b788424`; Actions Run #1142 / ID `44701241693` success, **174 passed / 0 failed**.
- PR #171 상태 동기화 병합 SHA `a8db31bd2c7a1e0127ef226a432183633e66eb76`; exact head `19d296c154115d47ef3b30be25c8700b53fa745f`; Run #1144 / ID `44701518420` success, **174 passed / 0 failed**.
- PR #171 CI: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/HTML canaries, provenance upload 통과.
- PR #171 provenance artifact #14613405592, 2,567 bytes, SHA-256 `f14e2ad608899ec53d999aa0dda87178fbf87494bdee4de9a7fb9f7477b74d27`.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC 16, product evidence 15, bidirectional true, M/606 41, JSONL 263 events (258 modern IDs + 5 legacy records).
- PR #170 pre-main ref `safety/pre-main-pr170-merge-2026-11-20`; post ref `safety/post-merge-pr170-2026-11-20`; PR #171 post ref `safety/post-merge-pr171-2026-11-20`; 각 post ref와 해당 main merge 시점 동일성 확인.
- 최신 Ver1.7/현행 펌웨어 보안 상태 및 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- main `protected=false` 리스크 유지. 서버 측 branch protection/ruleset은 저장소 관리자 설정 필요.
- 운영 코드, workflow, secrets, state/history 및 기존 SIL 3 보존 산출물 미변경.

---

## 최신 재개 상태 — PR #170 병합 및 iX7NH Ver1.1 보안면 원문 감사 완료 (2026-11-20)

- 현재 main SHA: `cad75135996c129bc576d83ce5b7ed968ca6a63b`; PR #170 squash 병합 완료.
- PR #170 exact head `8af0834e56c8ec8cd4c13d900a5fe77c0b788424`; Actions Run #1142 / ID `44701241693` success, **174 passed / 0 failed**.
- CI: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 모두 통과.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD-SEC crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 262 events (257 modern IDs + 5 legacy records).
- Provenance artifact #14611894438, 2,567 bytes, SHA-256 `0563c2493e7d19acf7e0cddee34c91e4c4b0339cfc696e52f8d27c79de373ad6`.
- 보고서 v0.18 §39, 제조사 원본 인벤토리 26개 데이터 행 반영. iX7NH Ver1.1 구판 매뉴얼에서 웹서버 로그인·Object 0x2420/0x2421, Modbus TCP Server 및 TCP/502 예시·쓰기 기능 코드, USB OTG/FoE/DriveCM/Webserver 업데이트 경로를 확인.
- 사전 main 복구 ref `safety/pre-main-pr170-merge-2026-11-20`; 사후 ref `safety/post-merge-pr170-2026-11-20`; post ref와 main 동일성 확인.
- 구판 Ver1.1은 현행 Ver1.7 보안 설정의 증거가 아님. 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- main `protected=false` 상태는 유지. 서버 측 branch protection/ruleset은 저장소 관리자 설정 필요.
- 운영 코드, workflow, secrets, state/history, 기존 SIL 3 보존 산출물은 변경하지 않음.

---

## 최신 재개 상태 — iX7NH Ver1.1 웹서버·Modbus TCP 1차 원문 감사 (2026-11-20)

- 기준 main SHA: `2368b20ad90b40d473bd3cf86eac1310283ccb3f`; 최신 main에서 분기한 작업 브랜치 `research/ix7nh-v11-web-modbus-audit-v2-2026-11-20`.
- 실질 조사: 공식 LS ELECTRIC iX7NH Ver1.1 PDF의 제12장 웹서버, 제13장 Modbus TCP, 제15장 업데이트 절차를 직접 검토하여 통합 보고서 v0.18 §39 추가.
- 확인 범위: 웹서버 ID/PW Object(0x2420/0x2421) 및 로그인·웹 업데이트, Modbus TCP Server(EtherCAT IN, 예시 TCP/502, 읽기/쓰기 기능 코드), USB OTG/FoE/DriveCM/Webserver 업데이트 경로.
- 제조사 원문: https://sol.ls-electric.com/uploads/document/16401412453260/_LSMecapion_%20iX7NH_KOR_Ver1.1_210830.pdf (추출 본문 검토; 원본 bytes/SHA-256 미확보).
- 구판 Ver1.1 증거로만 한정. 기본 인증정보 문자열은 공개 저장소에 재게시하지 않았으며, Ver1.7 현행성·취약점·TLS/서명/anti-rollback/복구는 Unknown.
- 제조사 인벤토리의 MANUAL-IX7NH-V1.1-UPDATE-SECURITY 행을 확장해 Modbus/Webserver 범위를 기록.
- 변경은 문서 전용. 운영 코드, workflow, secrets, state/history, SIL 3 보존 산출물은 수정하지 않음.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 저장소 거버넌스: main `protected=false` 리스크 지속. PR exact-head CI 및 pre/post safety refs로 보완; 서버 보호 설정은 관리자 권한 작업 필요.

---

## 최신 재개 상태 — PR #167 사후 동기화 완료 (2026-11-20)

- 기준 main SHA(PR #167 병합 시점): `7f9c35c54f93505f541198f3ceef723540f4df72`; PR #167은 PR #166 결과를 상황판·계획·README·세션/JSONL에 동기화한 문서 전용 PR이다.
- PR #167 exact head `dace5c2b1c61e295e8aea6fef18d08fc4c09236d`; Actions Run #1138 / ID `44693025760` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, JSONL 260 events.
- Provenance artifact #14609352656, 2,567 bytes, SHA-256 `1c9f5f187223cb6d9b8b4780eedc04cb1739bc9433d153ed38abb309e7517c63`.
- 사전 복구 ref `safety/pre-pr167-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr167-2026-11-20`; 사후 ref와 PR #167 병합 시점 main identical 확인.
- 실질 조사 최신 기준: PR #166 보고서 v0.17 §38, 제조사 인벤토리 26개 데이터 행, JSONL 259건(이후 PR #166 merge 검증 이벤트를 포함한 status sync 후 260건).
- iX7NH 공식 시리즈 자료에서 USB OTG/FoE/EoE/Modbus TCP/웹서버/백업·복원/STO 기능 확인. 최신 Ver1.7 매뉴얼과 현행 보안 설정은 미확인.
- **저장소 보호 설정:** GitHub API에서 main `protected=false` 확인. 현재는 PR exact-head CI, 수동 병합 게이트, pre/post safety refs에 의존하며 서버 측 required checks/branch protection은 강제되지 않는다. 관리 권한으로 main ruleset/branch protection 설정 필요; 현재 연결 도구는 해당 설정 변경을 지원하지 않아 변경하지 않았다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.

---

## 최신 재개 상태 — PR #166 병합 및 iX7NH 통신면 분석 완료 (2026-11-20)

- 현재 main SHA: `761b3ccffc142f11cbfe0d0dfb0e905b5d368ecb`; PR #166 병합 완료.
- PR #166 exact head `fa7120c73cbe6fe244319a8d1b1e7bc699b47259`; Actions Run #1136 / ID `44692817817` success, **174 passed / 0 failed**.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, JSONL 259 events.
- Provenance artifact #14609257372, 2,567 bytes, SHA-256 `e23c851495214060b6749de728888f6b7ea662fa1bf0ced9b42eb1179427d851`.
- 사전 복구 ref `safety/pre-pr166-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr166-2026-11-20`; 사후 ref와 main identical 확인.
- 보고서 v0.17 §38, 제조사 자료 인벤토리 26개 데이터 행, JSONL 259건.
- 핵심 증거: 2021 공식 iX7NH Series 자료는 USB OTG 업데이트·백업/복원, FoE, EoE/UDP, CoE/CiA402, Modbus TCP, 내장 웹서버/원격 시운전, STO1/2·EDM 기능을 명시. 현행 Ver1.7 상세·현행 보안 설정을 입증하는 자료로는 사용하지 않는다.
- 후속 P0: Ver1.7 원본과 2025-12-24 표준 O/S 업데이트 가이드영상 확보, Modbus TCP API 원본 검토, 인터페이스별 인증·권한·TLS·서명·anti-rollback·복구 확인.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run. CE LVD/EMC 및 UL 자료는 CRA 적합성 증거가 아니다.

---

## 최신 재개 상태 — PR #165 병합 및 iX7NH 통신면 조사 착수 (2026-11-20)

- 현재 main SHA: `1b2a027162c45cb45b656bf4c01098c137a7183b`; PR #165 merge, open PR 없음.
- PR #165 exact head `cbdad281756ab906003e174ecaa9183270b1d41e`; Actions Run #1134 / ID `44691706437` success, **174 passed / 0 failed**.
- Run #1134 CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, JSONL events 257.
- Provenance artifact #14608029442, 2,568 bytes, SHA-256 `65dfbda197494eddcbad0abd6ef3d190ba8420f107c043c3ecb61423f29456d0`.
- PR #165 merge SHA `1b2a027162c45cb45b656bf4c01098c137a7183b`; pre safety `safety/pre-pr165-merge-2026-11-20`, post safety `safety/post-merge-pr165-2026-11-20`; post ref == main 확인.
- 보고서 v0.17 §38 초안: iX7NH USB OTG/FoE/EoE/Modbus TCP/웹서버/백업·알람이력/STO 기능을 2021 공식 시리즈 자료에서 확인하고 보안 공격면별 미검증 질문을 구조화. 최신 Ver1.7 본문과 현행 펌웨어 설정은 여전히 미확인.
- 제조사 자료 인벤토리 26개 데이터 행 예상(이번 PR에서 6개 추가); JSONL 259건 예상(PR165 merge 이벤트 + §38 조사 이벤트 추가).
- 현재 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run. CE LVD/EMC 및 UL 목록은 CRA 적합성 증거로 취급하지 않는다.
- 작업 브랜치: `research/ix7nh-communication-surface-2026-11-20`; PR #166 생성 전 문서/인벤토리 검증 중.

---

## 최신 main 기준점 — PR #164 사후 상태 동기화 완료 (2026-11-20)

- PR #164 merge SHA: `77e3050558869cab2624880bb1d5bfe8a9d5685c`; exact head `f0f7a51883bd66ad73f2252d8933067840c3d4c8`.
- Actions Run #1132 / ID `44691510530`: success. Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF 업로드는 unchanged로 skipped.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 256 events.
- Provenance artifact #14609395254, 2,567 bytes, SHA-256 `da47c2cf1d99bca2b067fb4836e9a7b3320d435e05cd7cf1e7859ab6ee566e0b` (7일 보존).
- 사전 복구 ref `safety/pre-pr164-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr164-2026-11-20`; 사후 ref와 main identical 확인.
- PR #164는 PR #163의 사후 병합 상태를 동기화한 문서 전용 PR이다.
- 보고서 v0.16 §36~§37, 제조사 인벤토리 20개 데이터 행 유지. JSONL에는 PR #164 검증 이벤트를 추가하여 257건으로 갱신한다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests는 Not Run 유지.

---

## 최신 main 기준점 — PR #163 사후 상태 동기화 완료 (2026-11-20)

- PR #163 merge SHA: `814cc6309e72461f0649b1b6d34109894cff4810`; exact head `3d1f28acb57078c59bcb3d634674f8ac279358fd`.
- Actions Run #1130 / ID `44691317078`: success. Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF 업로드는 unchanged로 skipped.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 255 events.
- Provenance artifact #14609280243, 2,567 bytes, SHA-256 `3bd36d529e45b20de019c783128a8f221bfd3debd895c65ddc640e11caf1f946` (7일 보존).
- 사전 복구 ref `safety/pre-pr163-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr163-2026-11-20`; 사후 ref와 main identical 확인.
- PR #163은 PR #162의 보고서 v0.16 §37, 제조사 인벤토리 20행, JSONL 254건 반영을 상황판·계획·README·로그에 동기화한 문서 전용 PR이다.
- iX7NH 구판 Ver1.1 매뉴얼의 네 업데이트 경로와 FoE/Webserver 초기 인증정보 단서는 현행 Ver1.7에서 유지되는지 확인되지 않았다. 구판 기본값을 현행 취약점으로 단정하지 않는다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests는 Not Run 유지.

---

## 최신 main 기준점 — PR #162 병합 및 iX7NH 업데이트 보안 조사 (2026-11-20)

- PR #162 squash merge SHA: `1d6110236984ee11387aaf2be99f239fa2f2ec1e`; exact head `903fd90709636b37f2b4ebd1abec893555955a8e`.
- Actions Run #1128 / ID `44691140978`: success. Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF 업로드는 unchanged로 skipped.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 254 events.
- Provenance artifact #14609085450, 2,567 bytes, SHA-256 `0407e5069a4f5d9698f6d9be994ffecbbc62c9dbae54b29b52cb96c39873cf4c` (7일 보존).
- 사전 복구 ref `safety/pre-pr162-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr162-2026-11-20`; 사후 ref와 main identical 확인.
- 보고서 v0.16 §37, 제조사 인벤토리 20개 데이터 행, JSONL 254개 이벤트 main 반영.
- iX7NH 구판 Ver1.1 매뉴얼은 USB OTG/FoE/DriveCM/Webserver 네 업데이트 경로와 FoE/Webserver 초기 인증정보 단서를 문서화한다. 최신 Ver1.7 첨부는 메타데이터만 확인되고 본문 다운로드는 실패했으므로, 구판 기본값을 현행 취약점으로 단정하지 않는다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests는 Not Run 유지.

---

## 최신 main 기준점 — PR #161 병합 및 downgrade 증거 반영 (2026-11-20)

- PR #161 squash merge SHA: `3e633d1b1b8312f5cb6665b44ee8a6fac43ee694`; exact head `66ed22f9ab16576b607fb70c898f71f82f860ea1`.
- Actions Run #1126 / ID `44690800297`: success. Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF 업로드는 unchanged로 skipped.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 41, project log 252 events.
- Provenance artifact #14608053214, 2,567 bytes, SHA-256 `758aded424447f0d6fb74729a699ac9f856fa403d128a1db04883d9afb48ff42` (7일 보존).
- 사전 복구 ref `safety/pre-pr161-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr161-2026-11-20`; 사후 ref와 main identical 확인.
- 보고서 v0.15 §36에서 DriveCM Ver1.02.2의 downgrade 관련 릴리스 노트를 기록. downgrade 동작 단서는 확인했으나 인증·서명·anti-rollback은 Unknown.
- 후속 조사에서 iX7NH 구판 Ver1.1 매뉴얼의 4개 펌웨어 업데이트 경로와 FoE/Webserver 인증정보 초기값 단서를 확인. 최신 Ver1.7 첨부는 다운로드 오류로 본문 확인 전이며, 구판 내용을 최신 버전에 일반화하지 않는다.
- PR #162 작업 브랜치에서 보고서 v0.16 §37, 제조사 인벤토리 20개 데이터 행, JSONL 254개 이벤트를 준비 중이다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests는 Not Run 유지.

---

## 최신 main 기준점 — PR #160 병합 및 PR #159 사후 상태 동기화 (2026-11-20)

- PR #160 squash merge SHA: `8bc9762efbd20ca9c7aaaddc3832745d4e6dc53e`; PR #160 exact head: `4f56e9b24354d25f03363127e8167a46049c5ded`.
- PR #160 Actions Run #1124 / ID `44685715888`: success. Source blob identity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload 성공. PDF 업로드는 unchanged로 skipped.
- Provenance artifact #14606367087, 2,566 bytes, SHA-256 `57dba2ea061de40faec834b3794e102e414fa2f0e13a8fd72a0af2ede1447a80` (7일 보존).
- 사전 복구 ref `safety/pre-pr160-merge-2026-11-20`; 사후 복구 ref `safety/post-merge-pr160-2026-11-20`; 사후 ref와 main은 identical (ahead 0 / behind 0).
- PR #160은 PR #159 병합 결과를 상황판·계획·README·세션/JSONL 로그에 동기화한 문서 전용 변경이다. 현재 main은 위 merge SHA.
- 보고서 v0.14 §35, 제조사 인벤토리 17개 데이터 행, JSONL 251개 유효 이벤트를 기준으로 후속 조사 진행.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests는 Not Run 유지.

---

## 최신 main 기준점 — PR #159 병합 및 CI 검증 (2026-11-20)

- PR #159 squash merge SHA: `c43b35df267c30facbc8c8f62677e48189d24127`; exact-head `cc91056b674e54d80dfdd59f412b140caec4e6ed`.
- Actions Run #1122 / ID `44685551882`: success. Source blob integrity, compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF/10-source HTML canaries, provenance manifest upload all passed. PDF upload skipped as unchanged.
- CRA traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional links true, M/606 mapping 41, project log 250 events.
- Pre-merge safety ref `safety/pre-pr159-merge-2026-11-20`; post-merge safety ref `safety/post-merge-pr159-2026-11-20`; post ref == main verified.
- Report v0.14 §35 and manufacturer inventory 17 data rows merged. ESI 0.98 published list 11 models; DriveCM 1.03.2 support list includes PEGA2 and notes EtherCAT/RS-485 variants. PEGA2/iX700M absent from ESI 0.98 public applicability list; separate ESI possibility remains open.
- ESI/MSI/PDF attachment bytes and SHA-256 remain unacquired. Product CRA scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- Next P0: obtain PEGA2 EtherCAT/iX700M ESI and exact Vendor ID/Product Code/Revision; verify DFU signature/authentication/rollback/recovery and L7N/L7S security support policy.

---

## 최신 main 기준점 — PR #158 병합 및 CI 검증 (2026-11-20)

- PR #158 squash merge SHA: `422e20d59f22bb66fade70e2b7df144e5b032384`; exact-head Run #1120 / ID `44678458799` success.
- 소스 무결성, compileall, CRA traceability, 전체 pytest, 공식 CRA PDF/HTML canary, provenance manifest 업로드 성공. PDF 업로드는 unchanged로 skipped.
- 사전 복구 ref `safety/pre-pr158-merge-2026-11-20`, 사후 복구 ref `safety/post-merge-pr158-2026-11-20`; 사후 ref와 main identical.
- 보고서 v0.13 및 PR #157 사후 상태동기화 반영. 다음 분석은 ESI·DriveCM·제품 SKU 적용범위 교차검증.

## 2026-11-20 추가 조사 — ESI·DriveCM·신형 모델 교차검증
- ESI Ver0.98 (2025-07-15) 상세 게시물의 적용 모델 11개 확인: L7NH, Pegasus, PHOX, L7NHF, L7N, GEM, SMT, L7MMT, iX7NH, iX7M, iX7MD.
- DriveCM Ver1.03.2 (2026-07-07) 지원제품 목록에 PEGA2 포함. Ver1.03.0 변경내역에 PEGA2 EtherCAT 및 RS-485 신규 모델 2종 명시; L7S/L7N 단종 제품은 LIVE i.C.E 사용 안내.
- PEGA2 매뉴얼 Ver1.3 첨부명/크기/날짜 확인. iX700M Ver1.4 매뉴얼 목록 항목과 제품 카탈로그상 EtherCAT 확인.
- ESI 0.98 적용목록에 PEGA2/iX700M이 없는 반면 DriveCM에 PEGA2가 포함되는 적용범위 차이를 발견. 별도 ESI 유무·SKU/컨트롤러 패키지 확인 필요. 부재를 단정하지 않는다.
- 첨부 원본 bytes·SHA-256은 미확보. 제품 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 다음 P0: PEGA2 EtherCAT 및 iX700M ESI 정확한 파일/버전/Vendor ID/Product Code/Revision 확보, DFU 업데이트 보안 메커니즘, L7N/L7S 지원 종료·취약점 처리 정책 확인.

---

## 최신 main 기준점 — PR #157 병합 및 사후 검증 (2026-11-20)

- main merge SHA: `0ea0fba1fb37504f9d11b5c12d562c0d68f1d190`; PR #157 exact head `5210f9f11f1898f3dc83173df7a1a352d889c696`.
- PR #157 Actions Run #1118 / ID `44678289573`: success. Compileall, CRA traceability, full pytest **174 passed / 0 failed**, official CRA PDF and 10-source HTML canaries, provenance manifest upload all passed. PDF source artifact upload skipped as unchanged.
- Provenance artifact #14602977168, 2,567 bytes, ZIP SHA-256 `aeb27bb37f157d6d3de8dcde48d4cfad56caae112ec4d5637a470eca325a4f17` (7-day retention).
- 복구 기준점: `safety/pre-pr157-merge-2026-11-20` → `af7fa899dd0e7c31871387befef62979ad032283`; `safety/post-merge-pr157-2026-11-20` → merge SHA. Post ref와 main 동일 확인.
- 보고서 §34, 제조사 자료 인벤토리 신규 5행, 상황판·계획·로그 반영. 인벤토리 총 16개 데이터 행, PROJECT_LOG.jsonl 248개 유효 JSON 레코드.
- 신규 제조사 항목은 목록 메타데이터만 확인. DFU/특주 OS/DriveCM/iX7NH 첨부 원본 bytes·SHA-256·본문 미확보. Signed firmware, Secure Boot, authenticated update, anti-rollback, support period 또는 CRA 적합성을 입증하지 않음.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown, security tests Not Run. Main push CI는 별도 조회 범위에서 독립 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 상세 게시물·첨부 원본 확보, SKU별 업데이트 경로/인증/서명/복구/롤백/지원기간 및 취약점 처리 증거 검증.

---



## 2026-11-20 추가 조사 — 제조사 펌웨어·도구 자료 목록 스크리닝
- PR #156 main 기준 SHA: `af7fa899dd0e7c31871387befef62979ad032283` (PR #156 exact-head Run #1116 success, 174 passed / 0 failed).
- 공식 소프트웨어 목록에서 DFU Downloader_Ver1.00.4 (2026-09-16), L7NH 특주 O/S (2026-08-31)를 확인. 공식 가이드북 목록에서 DriveCM V1.03.1 및 게인 튜닝 가이드(2026-09-08), iX7NH 교육자료(2026-09-14)를 확인.
- 위 자료는 목록 메타데이터만 확인. 개별 첨부 bytes·파일명·해시·본문은 미확보. secure boot, signed firmware, authenticated update, anti-rollback, vulnerability fix 또는 support period를 입증하지 않는다.
- 보고서 §34 및 제조사 원본 자료 인벤토리 신규 행 5개에 반영. 신규 행은 listing_metadata_only로 분류.
- 다음 P0: 상세 게시물/첨부 URL 확보, DFU·펌웨어·DriveCM 원본 bytes 다운로드, SHA-256 및 서명/게시자/버전/본문 검토, SKU별 업데이트 경로·권한·복구·롤백·지원기간 확인.
- 제품 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run 유지.
## 최신 main 기준점 — PR #155 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: cd5976403f91c79beca845d8efd3f4e5f1930e23 (PR #155 squash merge).
- PR #155 exact head 19240925263c43c1f765463ad4e795f1767a2551; Actions Run #1114 / ID 44665772110 success; 174 passed / 0 failed.
- Run #1114: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 성공. PDF source artifact 업로드는 이전 동일 파일과 중복되어 skipped.
- Provenance artifact #14597677644 (2,567 bytes; SHA-256 39c4c43327a6ecc2da82dd8adba0a2b99b4d7245e54ecfc410d56a017bacc9cd); 7일 보존.
- PR #155 pre-merge safety safety/pre-pr155-merge-2026-11-20; post-merge safety safety/post-merge-pr155-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #154 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 481d340050df4fd93689b992a374df3da2cfaa47 (PR #154 squash merge).
- PR #154 exact head 0e60f078ab7bb91ec599f97b117315013a03f70c; Actions Run #1112 / ID 44665540665 success; 174 passed / 0 failed.
- Run #1112: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 성공. PDF source artifact 업로드는 이전 동일 파일과 중복되어 skipped.
- Provenance artifact #14597173328 (2,567 bytes; SHA-256 2757b6776b78a089092c8af8997f7615fea68ea3c387b77564394ea64d18d6da); 7일 보존.
- PR #154 pre-merge safety safety/pre-pr154-merge-2026-11-20; post-merge safety safety/post-merge-pr154-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #153 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 61c432f7c310bb8bbbf2bd2c8143b5860926ee68 (PR #153 squash merge).
- PR #153 exact head 84e73ec56fe375cfec52b584612d856475f5518d; Actions Run #1110 / ID 44665312753 success; 174 passed / 0 failed.
- Run #1110: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 성공. PDF source artifact 업로드는 이전 동일 파일과 중복되어 skipped.
- Provenance artifact #14597622291 (2,567 bytes; SHA-256 c6446496947c8f1d615d19828b6e1a435b07f6774f26223234f444976261802b); 7일 보존.
- PR #153 pre-merge safety safety/pre-pr153-merge-2026-11-20; post-merge safety safety/post-merge-pr153-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #152 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 8f2fa6af11be627dc3926dc46a28eb70c1ec23a0 (PR #152 squash merge).
- PR #152 exact head 95e8b887d41b7e33aa988ad83166184bb523c28c; Actions Run #1108 / ID 44665093443 success; 174 passed / 0 failed.
- Run #1108: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 성공. PDF source artifact 업로드는 이전 동일 파일과 중복되어 skipped.
- Provenance artifact #14597237413 (2,567 bytes; SHA-256 5c4d4e47614375696d429775da93bcbe8a0e130a1548a786650008e106ed212f); 7일 보존.
- PR #152 pre-merge safety safety/pre-pr152-merge-2026-11-20; post-merge safety safety/post-merge-pr152-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #151 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 05d95d7760aacd1b608e85b583069507c0b4a369 (PR #151 squash merge).
- PR #151 exact head 89aa425bc56fb7b3049ee10dc3effbb058b897d1; Actions Run #1106 / ID 44664881039 success; 174 passed / 0 failed.
- Run #1106: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 성공. PDF source artifact 업로드는 이전 동일 파일과 중복되어 skipped.
- Provenance artifact #14597945822 (2,567 bytes; SHA-256 c50a3c3f3d459ea10de54a4a6682f0b55f35d3691da236610ac1743f7b84b37f); 7일 보존.
- PR #151 pre-merge safety safety/pre-pr151-merge-2026-11-20; post-merge safety safety/post-merge-pr151-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #150 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 89659bc8dc718e8f090644b3aeb2de7c1ec363d1 (PR #150 squash merge).
- PR #150 exact head 2c0dd8491a57d1cee9794fa6fb56e001f05bf193; Actions Run #1104 / ID 44664625871 success; 174 passed / 0 failed.
- Run #1104: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596532979 (3,070,503 bytes; SHA-256 629255735141dd80f36c04b8fe0be97aa8b447966d558445051ed58156f7332c); provenance #14597076911 (2,567 bytes; SHA-256 492975b4ac6d0c072e56b8c4d8a3b7a58a2ff7baec31af7fa73567cbe6fde92f); 7일 보존.
- PR #150 pre-merge safety safety/pre-pr150-merge-2026-11-20; post-merge safety safety/post-merge-pr150-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #149 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 6e04cd691d637589af69437068befe623fd46312 (PR #149 squash merge).
- PR #149 exact head 0e872bcf989951a446bc8263e015d786a0e51ed0; Actions Run #1102 / ID 44664418107 success; 174 passed / 0 failed.
- Run #1102: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596792806 (3,070,503 bytes; SHA-256 4f154be7978242c7ae1ae6e938fb3bc0190bb340fcf76aa2aa4560d31e50a958); provenance #14596862640 (2,567 bytes; SHA-256 17bf9c8c04619deccf312406b9cc9ef005b72b4e6f668d78bd719d7540078f11); 7일 보존.
- PR #149 pre-merge safety safety/pre-pr149-merge-2026-11-20; post-merge safety safety/post-merge-pr149-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #148 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 33d82ee31c151c4d2f19165f1c17882fc5dfe722 (PR #148 squash merge).
- PR #148 exact head 27a194485b7545a6c6e9c285b485822034e47815; Actions Run #1100 / ID 44664187925 success; 174 passed / 0 failed.
- Run #1100: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14597670650 (3,070,504 bytes; SHA-256 cf2196ee53be64f58f1d2bc570a1ec7879fdfd13cd9e978bd1094d5b9b065e1b); provenance #14597051830 (2,567 bytes; SHA-256 161343a0077a9057b01170a56e06f724b6a27842a28494d5ddfee64bdce64bf1); 7일 보존.
- PR #148 pre-merge safety safety/pre-pr148-merge-2026-11-20; post-merge safety safety/post-merge-pr148-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #147 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 51d75213e3e035dfc7a7858570844533644aedc5 (PR #147 squash merge).
- PR #147 exact head 789963424610a4369930bc1f841f30160378d50b; Actions Run #1098 / ID 44663993153 success; 174 passed / 0 failed.
- Run #1098: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14597665320 (3,070,502 bytes; SHA-256 20974038626f21d9a54f888c0b4ddaf47eb6c0f76b42c1a006ab4689d1b5a3cd); provenance #14596892018 (2,566 bytes; SHA-256 90c98687bcdc4eb8cdfb9692b1ed88fe6753d2d354be20ca364dfba554d387c4); 7일 보존.
- PR #147 pre-merge safety safety/pre-pr147-merge-2026-11-20; post-merge safety safety/post-merge-pr147-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #146 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: bd0938484b22b4d8c6d8ad94b440de2b479a0ea2 (PR #146 squash merge).
- PR #146 exact head aed4a54883cdcacda59bad30f7b2a939b9b346b0; Actions Run #1096 / ID 44663781793 success; 174 passed / 0 failed.
- Run #1096: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14597665057 (3,070,502 bytes; SHA-256 88940d8d171a9578b6475a52c1c967f737823dcef5b82c479556e82e856144bd); provenance #14597380473 (2,567 bytes; SHA-256 35d45fee83dbf0c907a5ec980bb7ebc407c3a71a6f23063eb75527229f7228d7); 7일 보존.
- PR #146 pre-merge safety safety/pre-pr146-merge-2026-11-20; post-merge safety safety/post-merge-pr146-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #145 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: 482305a4d5334ef19105560d0b4a3bd012acc1d0 (PR #145 squash merge).
- PR #145 exact head dd536778451cb7629cf351480c41d9726b8e5365; Actions Run #1094 / ID 44663593799 success; 174 passed / 0 failed.
- Run #1094: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596711210 (3,070,503 bytes; SHA-256 267ee572e7e36074114ffe259141268965cd79791f01f0b379d0ccc695a47741); provenance #14596970810 (2,567 bytes; SHA-256 556d6304875a80d6ffe6da0dfe46f09b2011abb7f59545667b510f61b1f16ed9); 7일 보존.
- PR #145 pre-merge safety safety/pre-pr145-merge-2026-11-20; post-merge safety safety/post-merge-pr145-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14-row model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #144 병합 및 프로젝트 상태 동기화 (2026-11-20)

- 최신 main SHA: c616169b4300521459cc3ae78d631fcd739103fb (PR #144 squash merge).
- PR #144 exact head 09ac041dbb3df72e8c3cf3dd01e53bbc80d9ff7f; Actions Run #1092 / ID 44663374900 success; 174 passed / 0 failed.
- Run #1092: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14597230119 (3,070,502 bytes; SHA-256 b8ff2c79732ee37e0bb625d84c66abf1026863bf229f85883ccc7b3d3036876b); provenance #14596691436 (2,567 bytes; SHA-256 3640500172144d9754c6dffbf5fe46af153ee6928376ede0ce947291172e4a34); 7일 보존.
- PR #144 pre-merge safety safety/pre-pr144-merge-2026-11-20; post-merge safety safety/post-merge-pr144-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #143 병합 및 모델 인터페이스 상태 동기화 (2026-11-20)

- 최신 main SHA: f1157fb1b5581f55b1f192c15b1822386ce3ed1e (PR #143 squash merge).
- PR #143 exact head d0aef1b098d5b1f52e83f24b5d0eb9a37e98b34d; Actions Run #1090 / ID 44663182762 success; 174 passed / 0 failed.
- Run #1090: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596188740 (3,070,503 bytes; SHA-256 2105504b4942f21db41a38eaca9b548e3a94a6696593238b3bf2cbf8e2b85c57); provenance #14595554868 (2,567 bytes; SHA-256 c3f7cf7311772cfa4687cef25c13790d3e302a916c2c847badf0589fa0457c63); 7일 보존.
- PR #143 pre-merge safety safety/pre-pr143-merge-2026-11-20; post-merge safety safety/post-merge-pr143-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14-row model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #142 병합 및 모델 인터페이스 상태 동기화 (2026-11-20)

- 최신 main SHA: 0c8144a59e0741eb9538af2e8493def6fe982f33 (PR #142 squash merge).
- PR #142 exact head a7662c01f4c8f74790f4848a1d702ee22cb2d74a; Actions Run #1088 / ID 44662991366 success; 174 passed / 0 failed.
- Run #1088: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14595914125 (3,070,503 bytes; SHA-256 91553fb5a43e6e30fdce54a04ccca0e2bf8198630d59417639a5a4a1e0b72197); provenance #14597100049 (2,567 bytes; SHA-256 ae842c563c3bd0ba36f4f0a2fb2052a8556146486c2ea7cf18bb13f2f9666b6c); 7일 보존.
- PR #142 pre-merge safety safety/pre-pr142-merge-2026-11-20; post-merge safety safety/post-merge-pr142-2026-11-20. Post ref와 main merge SHA identical.
- main 반영: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, manufacturer source inventory, 14행 model/interface matrix, 프로젝트 상황판·계획·세션 로그.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #141 병합 및 모델 인터페이스 작업 CI 동기화 (2026-11-20)

- 최신 main SHA: f798d9d16d74e399124c207c45ee6bdb6c1339a7 (PR #141 squash merge).
- PR #141 exact head 468eba3d10c9d76279dfa2f64c445b11db25d288; Actions Run #1086 / ID 44662805428 success; 174 passed / 0 failed.
- Run #1086: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596955128 (3,070,501 bytes; SHA-256 257c1f95b42c6b4122386e2bc34bb1a2de6789ead07ac85e77b25c250c4311a0); provenance #14595634151 (2,567 bytes; SHA-256 12ff89b7934e7fdf5d4cbc107d65e35acfe2bf755f65f29231922a5c872b0f78); 7일 보존.
- PR #141 pre-merge safety safety/pre-pr141-merge-2026-11-20; post-merge safety safety/post-merge-pr141-2026-11-20. Post ref와 main merge SHA identical.
- main 반영 산출물: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, manufacturer source inventory, 14행 model/interface matrix.
- 25b 기술 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 범위·SKU별 적용·iX7NH 듀얼 프로토콜·L7P RS-422 범위는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보/해시/본문 검토, exact SKU/옵션별 포트·프로토콜, 취약점·업데이트·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #140 병합 및 모델 인터페이스 상태 동기화 (2026-11-20)

- 최신 main SHA: 2edae2463e04b5d4280aa9d04c48f7805b554707 (PR #140 squash merge).
- PR #140 exact head 1f859f5431917e8202ffdcaf7141376c8712eb8e; Actions Run #1084 / ID 44662635778 success; 174 passed / 0 failed.
- Run #1084: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14595564027 (3,070,502 bytes; SHA-256 95dd3a2d6be26a27894175c4d73a94e26e883ff6a1253b2c99b8347cffbce4c6); provenance #14595579119 (2,567 bytes; SHA-256 c52b41c5124c4593847c4136956b4863c7c0befc20726646517ab5caa689d935); 7일 보존.
- PR #140 pre-merge safety safety/pre-pr140-merge-2026-11-20; post-merge safety safety/post-merge-pr140-2026-11-20. Post ref와 main merge SHA identical.
- main 산출물: 보고서 §31~§33 (v0.12), 41-item CRA audit, 6개 OT/IACS profile matrix, 11-row manufacturer source inventory, 14-row model/interface matrix.
- 제조사 카탈로그에서 EtherCAT 통신형/펄스형 구분; iX7NH Modbus TCP, L7P Modbus RS-422, iX700MD1-B-150B CE 모델코드 확인. 25b 기술 관련성은 강하지만 표준 최종 범위 및 SKU별 법적 적용은 Unknown.
- 원본 PDF/XML/MSI/API ZIP/CE DoC bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 파일 확보 및 해시/본문 검토, exact SKU/옵션별 포트·프로토콜, iX7NH dual-protocol, L7P RS-422 scope, 취약점/업데이트/지원기간 증거 수집.

---
## 최신 main 기준점 — PR #139 병합 및 모델 인터페이스 작업 CI 동기화 (2026-11-20)

- 최신 main SHA: 7545a771ce16f362cf5b911cd8c850efc91c2e92 (PR #139 squash merge).
- PR #139 exact head 28086497e73f123aef28e695a56e455ed9cc092a; Actions Run #1082 / ID 44662453390 success; 174 passed / 0 failed.
- Run #1082: source integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14596455559 (3,070,502 bytes; SHA-256 c58dc3d7a47b43d323a626db8f390754dc7b4a6db8ee49b880510a15fd5f3327); provenance #14596296397 (2,567 bytes; SHA-256 27132710326a210178372b9b0fb8ecc340b4b2c6e5b0f165eea705f574c4302c); 7일 보존.
- PR #139 pre-merge safety safety/pre-pr139-merge-2026-11-20; post-merge safety safety/post-merge-pr139-2026-11-20. Post ref와 main merge SHA identical.
- 최신 통합 보고서 §31~§33 (v0.12), 41-item CRA 감사대장, 6개 OT/IACS vertical profile matrix, 11-row manufacturer source inventory, 14-row model/interface matrix main 반영.
- M/606 25b 기술적 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 최종 표준 적용범위·정확한 SKU/포트/옵션·iX7NH 듀얼 프로토콜·L7P RS-422 포함 여부는 Unknown.
- 제조사 PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 별도 조회에서 독립 확인되지 않아 미확인으로 유지.
- 다음 P0: 모델별 원본 파일 확보 및 해시·본문 검토, iX7NH EtherCAT/Modbus TCP 동시지원 여부, ESI compatibility, L7P RS-422의 25b 범위, 제품별 보안기능·취약점 대응·지원기간 증거 수집.

---
## 최신 main 기준점 — PR #138 병합 및 모델별 통신 인터페이스 증거 (2026-11-20)

- 최신 main SHA: 372860cfb1a149bc5d5a7bf993e11dbf68217478 (PR #138 squash merge).
- PR #138 exact head 0ca7cfb745884ba8c7a1f3f383974286d0e88fd8; Actions Run #1080 / ID 44662266977 success; 174 passed / 0 failed.
- Run #1080: source integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14595309514 (3,070,503 bytes; SHA-256 bf73016cdd73cba8daab1c7108e5c469f4ac5bcfdd4648d43e9cc56d705f4f1e); provenance #14595489037 (2,567 bytes; SHA-256 8175503c2935119183cd810fd287028b288d36e837af79608de56c64883b27c9); 7일 보존.
- PR #138 pre-merge safety safety/pre-pr138-merge-2026-11-20; post-merge safety safety/post-merge-pr138-2026-11-20. Post ref와 main merge SHA identical.
- main 반영 산출물: 통합 보고서 §33 (v0.12), 14행 model/interface evidence matrix, manufacturer source inventory 보강, M/606 item25 및 25b matrix 갱신.
- 제조사 카탈로그는 EtherCAT 통신형과 펄스형을 구분. iX7NH Modbus TCP API, L7P Modbus RS-422 API, iX700MD1-B-150B CE DoC 모델코드 메타데이터 확인.
- 25b 기술적 관련성은 EtherCAT/Modbus TCP 모델에서 강함. 그러나 최종 표준 범위, exact SKU/port/option, iX7NH 동시 프로토콜, L7P RS-422 포함 여부는 Unknown.
- PDF/XML/MSI/API ZIP/CE DoC 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않아 미확인으로 유지.
- 다음: SKU별 원본 파일 확보, ESI/API/매뉴얼 본문 검토, iX7NH EtherCAT+Modbus TCP 동시지원 확인, 인터페이스 보안 통제·업데이트·취약점 대응 정책 증거 수집.

---
## 최신 main 기준점 — PR #137 병합 후 모델별 인터페이스 증거 분석 (2026-11-20)

- main SHA: 71db8880502bbd5be083e297e39acc338ea0d13a (PR #137 squash merge).
- PR #137 exact head f99d0cccc13a52744882a5869aab920aae0b036e; Actions Run #1078 / ID 44661804214 success; 174 passed / 0 failed.
- Run #1078: source integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance upload 모두 성공.
- PDF artifact #14595852559 (3,070,500 bytes; SHA-256 f8093f9b25dff09e971b2f312fef8617d620c9b690208729fb7dc2276cf270a5); provenance #14595338956 (2,566 bytes; SHA-256 361d32f0bf155851e352f977f31c242b1c3df47950466e2a5cf9ebc84813213c); 7일 보존.
- PR #137 pre-merge safety safety/pre-pr137-merge-2026-11-20; post-merge safety safety/post-merge-pr137-2026-11-20 (main과 identical).
- 새 작업 브랜치 cra/servo-model-interface-evidence-2026-11-20. 공식 드라이브 카탈로그에서 EtherCAT 통신형과 펄스형을 분리하고, iX7NH Modbus TCP 및 L7P Modbus RS-422 가이드, iX700M CE 모델코드 등록정보를 확인.
- 25b는 EtherCAT/Modbus TCP 통신 모델에 대해 기술적 후보가 명확해졌으나, 통합 인터페이스의 최종 표준 적용범위와 SKU/포트 옵션은 Unknown. L7P RS-422 포함 여부도 표준 정의 확인 필요.
- 제조사 첨부 PDF/XML/MSI/API ZIP 원본 bytes 미확보, SHA-256 미계산, content review metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 별도 확인되지 않아 미확인으로 유지.
- 다음: 정확한 SKU/HW/FW/옵션별 매뉴얼·ESI/API bytes 확보, 포트/프로토콜/보안 기능 매핑, iX7NH EtherCAT+Modbus TCP 동시지원 여부 및 ESI 호환성 확인.

---
## 최신 main 기준점 — PR #136 병합 및 제조사 자료 인벤토리 (2026-11-20)

- 최신 main SHA: d7e921f5a6db04d20ce06778f6ea384dbd9c63fe (PR #136 squash merge).
- PR #136 exact head 25215700a415b094c6c187278183b8ca15e4e4ca; Actions Run #1076 / ID 44661598986 success; 174 passed / 0 failed.
- Run #1076: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF/10-source HTML canaries, provenance manifest upload 모두 성공.
- PDF artifact #14595209202: 3,070,503 bytes; ZIP SHA-256 6356c21834522bcb9f90de5e903679d02b18ced0c49fe2287f7ae065a1b8e9ff; expires 2026-11-27 02:33:31 UTC.
- Provenance artifact #14595972121: 2,567 bytes; ZIP SHA-256 752e408af313d26b37d184b22180aea597b57058fc65e6a4d9398b9019c6638e; expires 2026-11-27 02:33:44 UTC.
- PR #136 pre-merge safety safety/pre-pr136-merge-2026-11-20; post-merge safety safety/post-merge-pr136-2026-11-20. Post ref와 main merge SHA identical.
- 보고서 §32 및 제조사 source inventory 반영: DriveCM 1.03.2, EtherCAT ESI 0.98/0.96, PEGA2/iX700M 매뉴얼 등록정보. ESI 0.98 11개 모델, PEGA2 EtherCAT/RS-485 변형 확인.
- 25b 기술적 후보 강화; 단, PDF/XML/MSI bytes 미확보·SHA-256 미계산·content review metadata-only. 법적 적용/제품분류 Unknown, security tests Not Run.
- main push CI는 독립 조회에서 확인되지 않음; PR exact-head CI와 구분하여 미확인 유지.
- 다음 P0: 모델별 원본 PDF/XML/MSI 다운로드 및 해시, 정확한 SKU/HW/FW/옵션 확인, ESI Vendor ID/Product Code/Revision/PDO/CoE 및 manual 통신표 분석, DriveCM 서명·의존성 검토.

---
## 최신 재개 기준점 — PR #135 병합 후 제조사 원본 자료 인벤토리 진행 (2026-11-20)

- main 기준 SHA: 4299fd7301c22898cab8291dcb1a54d2a767d0cf (PR #135 squash merge).
- PR #135 exact head 90f352bcf0219beb330839d97626937a776b7893; Actions Run #1074 / ID 44661159895 success; 174 passed / 0 failed.
- Run #1074: source integrity, compileall, CRA traceability, full pytest, official PDF/10-source HTML canaries, provenance artifact upload 성공.
- PDF artifact #14596121187 (3,070,503 bytes; SHA-256 df36911183a53d2147acef0cf5911a1fe72abe4e400a913594378ffcce3d5331); provenance #14595303097 (2,567 bytes; SHA-256 9bc61e239e2e4ab0dd8658145e8dd91e30c6da25796bcae371f07c9d97c865fa); 7일 보존.
- pre-merge safety safety/pre-pr135-merge-2026-11-20; post-merge safety safety/post-merge-pr135-2026-11-20 (main과 identical).
- 새 작업 브랜치 cra/manufacturer-source-inventory-2026-11-20; 제조사 공식 게시물에서 DriveCM 1.03.2, EtherCAT ESI 0.98/0.96, PEGA2/iX700M 매뉴얼 등록정보 확인.
- ESI 0.98은 11개 모델의 EtherCAT Drive XML 적용목록을 제시. DriveCM 1.03.2 변경이력은 PEGA2 EtherCAT 및 RS-485 두 모델 변형을 명시. 25b 기술적 검토 우선순위 강화; 법적 적용은 표준 전문/SKU 확인 전 Unknown.
- 제조사 첨부 원본 PDF/XML/MSI bytes 미확보, SHA-256 미계산, 본문 검토 metadata-only. Product scope/classification/Annex III·IV/RDPS Unknown; security tests Not Run.
- main push CI는 독립 확인되지 않아 미확인으로 유지.
- 다음: 제조사 첨부 bytes 확보, 정확한 SKU/HW/FW/옵션 확인, ESI XML과 매뉴얼 통신표/보안기능 분석, 설치파일 서명·의존성 검증.

---
## 최신 main 기준점 — PR #134 병합 및 PR #133 후속 CI 동기화 (2026-11-20)

- 최신 main SHA: 7162664b29554a01d2694cd027efb0191a6c3344 (PR #134 squash merge).
- PR #134 exact head 7a560c3d6db33f3d553f7fa9cd3596f9c7c6cd02; Actions Run #1072 / ID 44660976790 success; 174 passed / 0 failed.
- Run #1072: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF and 10-source HTML canaries, provenance manifest upload 모두 성공.
- PDF artifact #14594883481: 3,070,503 bytes; ZIP SHA-256 b78ae81c852f64e47167ccccf05420d5480a086cb6a1888e0992c40d5a66e2d7; expires 2026-11-27 02:28:13 UTC.
- Provenance artifact #14594828906: 2,567 bytes; ZIP SHA-256 73fca113ee234b576051b14454b8934c545742be616ecbef831cb020d15c849e; expires 2026-11-27 02:28:25 UTC.
- PR #134 pre-merge safety ref safety/pre-pr134-merge-2026-11-20; post-merge safety ref safety/post-merge-pr134-2026-11-20. Post ref와 main merge SHA identical.
- PR #132의 OT/IACS 수직 프로파일 분석 및 PR #133/#134 상황판 동기화가 main에 반영됨. 보고서 §31, M/606 41-item audit 6행, vertical profile matrix 6행 유지.
- main push CI는 별도 조회에서 독립 확인되지 않았으므로 PR exact-head CI 성공과 구분해 미확인으로 유지.
- 제품별 CRA scope/classification/Annex III·IV/RDPS = Unknown; security tests = Not Run. 제조사 원본 manual/DriveCM/ESI bytes와 SHA-256 미확보.
- 다음 P0: LS메카피온 정확한 SKU/HW/FW와 EU 판매구성 확정, 모델별 원본 매뉴얼·데이터시트·DriveCM·ESI/XML 확보 및 SHA-256/페이지 검토, 인터페이스별 데이터 흐름·보안기능 증거 수집. 이후 41개 실제 EN/ETSI 매핑·OJ 전수감사와 Article 2 ESO 통지 원본 확인.

---
## 최신 main 기준점 — PR #133 병합 및 PR #132 후속 CI 동기화 (2026-11-20)

- 최신 main SHA: a889b03855e3c7683aa140220352510ab4c4c116 (PR #133 squash merge).
- PR #133 exact head 466b3d93db6119c3a73c8cef6bc2e55cf698294d; Actions Run #1070 / ID 44660790965 success; 174 passed / 0 failed.
- Run #1070: source blob integrity, compileall, CRA traceability, full pytest, official CRA PDF and 10-source HTML canaries, provenance manifest upload 모두 성공.
- PDF artifact #14596185499: 3,070,503 bytes; ZIP SHA-256 5a84aeb59f8d960d80d611be7ee4b978d808e84b68255c489633fc94af84ca18; expires 2026-11-27 02:26:42 UTC.
- Provenance artifact #14595641444: 2,567 bytes; ZIP SHA-256 81bcba6e53025759610218c9d66334710919510c1b8d623c7e880af72d9501d5; expires 2026-11-27 02:26:53 UTC.
- PR #133 pre-merge safety ref safety/pre-pr133-merge-2026-11-20; post-merge safety ref safety/post-merge-pr133-2026-11-20. Post ref와 main merge SHA identical.
- PR #132 보고서 §31 / 6-row vertical-profile matrix / 41-item audit CSV updates는 main에 반영됨. Product scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- main push CI는 별도 조회에서 독립 확인되지 않았으므로 PR exact-head CI 성공과 구분해 미확인으로 유지.
- 다음: 모델별 제조사 원본 매뉴얼·데이터시트·DriveCM 설치파일·ESI/XML bytes 및 SHA-256 확보, 모델/SKU/HW/FW와 EU 공급경로 확인, 인터페이스 데이터 흐름·보안통제 증거 검토. 이후 41개 실제 EN/ETSI 매핑 및 OJ 전수감사와 Article 2 ESO 통지 원본 확인.

---
## 최신 main 기준점 — PR #132 병합 및 OT/IACS 수직 프로파일 감사 (2026-11-20)

- 최신 main merge SHA: f3a8fc06b2a0c5fdaa98d98ad8bc0f21abee22df (PR #132 squash merge).
- PR #132 exact head: 15df2eae8b3a5eea809496e46a412f67f0f3576e; GitHub Actions Run #1068 / ID 44660527456 success; 174 passed / 0 failed.
- Run #1068 단계: source blob integrity, compileall, CRA cross-matrix traceability, 전체 pytest, official CRA PDF read-only canary, 10-source official CRA HTML canary, JSON provenance manifest round-trip 및 artifact upload 모두 성공.
- PDF artifact #14595995557: 3,070,503 bytes; ZIP SHA-256 2d3848ab2c7046b53154e3c304bee5dca5ad33bd23a00c4a5396b020922bb6ef; 만료 2026-11-27 02:24:36 UTC.
- Provenance artifact #14595062566: 2,567 bytes; ZIP SHA-256 657f92dd556ac2dc56ccb68278452a2e9f9422eeaec366098117c1ef52d47bc9; 만료 2026-11-27 02:24:49 UTC.
- 사전 복구 ref safety/pre-pr132-merge-2026-11-20; 병합 후 복구 ref safety/post-merge-pr132-2026-11-20. Post-merge ref와 merge SHA compare 결과 identical.
- 반영 산출물: 통합 예비 보고서 §31 (v0.10), M/606 41-item 감사대장 행 20/21/22/25/27/36 보완, OT/IACS 6개 수직 프로파일 별도 6행 매트릭스, 상황판/계획/README/세션 로그/JSONL 동기화.
- M/606 여섯 프로젝트는 CENELEC Work Programme Under Drafting / 개별 Committee stage, OJEU Citation expected. 실제 OJ 인용은 미확인, Article 27 presumption 없음.
- 제품별 CRA scope/classification/Annex III·IV/RDPS = Unknown; security tests = Not Run. 제조사 매뉴얼/DriveCM/ESI 원본 bytes 및 SHA-256 미확보.
- main push CI는 현재 연결된 조회에서 독립 확인되지 않음. PR exact-head CI 성공과 main push CI를 혼동하지 않는다.
- 다음 우선순위: LS메카피온 모델별 원본 매뉴얼/데이터시트 bytes·SHA-256·페이지 검토, 정확한 SKU/HW/FW/EU 공급경로 확보, 인터페이스별 데이터 흐름 및 보안통제 확인, 41개 실제 EN/ETSI 매핑·OJ 전수감사, Article 2 ESO 통지 증거 확인.

---
# 최신 재개 기준점 — 2026-11-20 (OT/IACS 수직 프로파일 감사)

- GitHub 저장소: useformotor3/ai-discord-bot (Public); 기준 main HEAD 36f170de199d2fc23e4e40969584e56c37dbebe7 (PR #131 사후 문서 동기화).
- PR #130 merge SHA bfcc2e61fc07b2148fca7a162349af40aa84bc47; main push CI Run #1065 / ID 44658780153 success. Source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML canaries, provenance upload 모두 success.
- 사전 복구 ref: safety/pre-ot-iacs-vertical-audit-2026-11-20; 작업 브랜치: cra/ot-iacs-vertical-profile-boundary-2026-11-20 (base 36f170de199d2fc23e4e40969584e56c37dbebe7).
- 이번 1차 출처 확인: CLC/TC 65X 공식 Work Programme에서 M/606 20b/21b/22b/25b/27b/36b ↔ prEN 50770-4/-2/-6/-3/-5/-1 (project 81652/81650/81654/81651/81653/81649) 연결 및 각 개별 CENELEC 레코드 확인.
- 여섯 프로젝트 모두 Work Programme Under Drafting, 개별 레코드 Committee stage; OJEU 필드는 Citation expected이나 실제 OJ 인용번호·발행일은 없음. Article 27 presumption 없음.
- 서보드라이브 기능 경계: 25b 물리·가상 네트워크 인터페이스가 우선 기술 검토 후보. VPN/NMS/SIEM/router-modem-switch/firewall-IDS-IPS 기능은 현재 제조사 증거로 확인되지 않음. 기능 미확인은 미지원의 증명이 아니며, 모델별 매뉴얼 미확보 상태를 유지.
- 제품별 CRA scope/classification/Annex III·IV/RDPS = Unknown; 보안시험 = Not Run. 원본 매뉴얼/DriveCM/ESI bytes와 SHA-256 미확보.
- 산출물: 통합 예비 보고서 §31, 6행 OT/IACS vertical-profile matrix, 41-item 감사대장 행 20/21/22/25/27/36 보완. PR/CI 검증 전.
- 다음: 문서 readback·JSONL/CSV/추적성 검증, exact-head CI, PR review/diff 및 복구 ref 유지. main 직접 수정 금지.

---
## 최신 main 기준점 — PR #125 병합 및 M/606 감사 후속 (2026-11-20)

- 현재 main merge SHA: `0a5f5140e323303d6a960ca73edd8ec8c05f55f2` (PR #125 squash merge 확인).
- PR #125 exact-head SHA: `e940663da113dedcd8071f5781f1bcf78f449ccf`; CI Run #1050 성공. 전체 pytest, CRA cross-matrix, 공식 CRA PDF/source read-only canary, provenance manifest 업로드 단계 성공.
- 사전 복구 ref: `safety/pre-m606-oj-audit-2026-11-20`; 병합 후 복구 ref: `safety/post-merge-pr125-2026-11-20`.
- PR #125는 EN 40000-1-1/-1-2 발행 발표와 Article 27 OJ 게이트를 보고서 §27에 반영하고 상황판·계획서·로그를 동기화했다.
- 최신 추가 조사: CEN-CENELEC 발표는 두 EN의 발행 사실을 확인한다. CRA harmonised-standard tracker(2차 자료)는 CEN catalogue가 두 표준 모두 OJ citation을 기대하지 않는다고 표시한다고 보고한다. 다만 이번 세션에서는 CEN catalogue의 해당 개별 레코드를 직접 열람하지 못했으므로, 이를 **2차 자료에 의한 잠정 정보**로만 기록하고 OJ 상태의 최종 증거는 CEN catalogue 및 EUR-Lex/OJ 원문 직접 대조로 남긴다. Article 27 추정을 주장하지 않는다.
- M/606 41개 표준의 개별 개발상태·발행·OJ 인용·제한사항 전수감사는 미완료. OJ 검색 결과 없음은 미게재 확정이 아니다.
- 제조사 매뉴얼/DoC 원본 PDF bytes 미확보, SHA-256 미확인. 제품별 CRA scope/classification/RDPS Unknown, security tests Not Run. PR merge SHA에 대한 별도 main push CI는 독립 확인되지 않음.

## 최신 main 기준점 — PR #124 사후 동기화 및 M/606 OJ 감사 재개 (2026-11-20)

- 현재 main SHA: `3aebf09e6786fa9ee451b027ed83756f37bd89b3` (GitHub 최근 커밋 검색 및 PR #124 비교로 확인).
- PR #124: `docs(status): sync PR #123 merge and evidence intake`; main에 squash merge 반영, exact-head CI Run #1048 success. Post-merge safety ref: `safety/post-merge-pr124-2026-11-20`.
- 이번 작업 브랜치: `docs/m606-oj-citation-audit-2026-11-20`; 기준 SHA `3aebf09e6786fa9ee451b027ed83756f37bd89b3`; 사전 복구 ref `safety/pre-m606-oj-audit-2026-11-20`.
- CEN-CENELEC 2026-11-19 발표에서 EN 40000-1-1/-1-2 발행 확인. CRA Article 27 추정은 OJ 참조 게재 범위에 한정되며, 이번 검색에서 두 표준의 OJ 인용은 직접 확인되지 않아 추정 주장을 하지 않는다. 상세 보고서 §27.
- M/606 41개 표준의 개별 개발상태·발행·OJ 인용·제한사항 전수감사는 미완료. 초기 검색에서 결과가 없다는 사실을 OJ 미게재 확정으로 해석하지 않는다.
- 제조사 매뉴얼/DoC 원본 PDF bytes 미확보, SHA-256 미확인. 제품별 CRA scope/classification/RDPS Unknown, security tests Not Run. Exact-main push CI는 독립 확인되지 않음.

## 최신 main 기준점 — PR #123 iX700M 제품 식별 증거 병합 (2026-11-20)

- Main merge SHA: `2f09103fa5efe23374458ddf49de7c0fd4febddb`; post-merge safety ref: `safety/post-merge-pr123-2026-11-20`.
- PR #123 exact-head CI Run #1046 / ID `44644308627`: success (source identity, compile, CRA traceability, full pytest, official CRA PDF retrieval, provenance manifest upload).
- PR #123 adds report §26: manufacturer-listed iX700MD1-B-150B code definitions (D1=1-axis, B=480 Vac, 150=15 kW, encoder B=BiSS-C) and CE/LVD/EMC listing metadata. Attached DoC PDF bytes not acquired; this is not CRA conformity evidence.
- PR #122 remains the previous intake checkpoint: merge `8a18856a677ccbab4117c0ea35524116ac5ad70a`, exact-head CI Run #1044 success; report §25 and manufacturer intake register with iX7M/iX7NH metadata, original PDFs not acquired.
- Latest manufacturer intake register: `sources/manufacturer/LS_MECAPION_MANUAL_INTAKE_2026-11-20.json` (4 records; no unverified SHA-256 claims).
- Product scope/classification/RDPS remain Unknown; security tests Not Run. Exact-main push CI not independently confirmed.

## 추가 제품 식별 증거 — iX700M CE/LVD/EMC 게시물 (2026-11-20)

- 제조사 게시물에서 `iX700MD1-B-150B` 모델 코드 및 코드 체계(D1=1축, B=480 Vac, 150=15 kW, 인코더 B=BiSS-C)를 확인했다.
- CE_DoC-LVDEMC PDF 게시 메타데이터(238.9 KB, 2026-04-30)는 확인했으나 원본 PDF는 HTTP 502로 미확보. CE/LVD/EMC 게시물은 CRA 적합성이나 보안통제 증거로 취급하지 않는다.
- 상세 분석: 보고서 §26 및 manufacturer intake register. 제품별 CRA scope/classification/RDPS Unknown, security tests Not Run.

## 최신 재개 업데이트 — 제조사 매뉴얼 첨부 메타데이터 재확인 (2026-11-20)

- iX7M Ver1.3 및 iX7NH 200V Ver1.7 공식 게시물의 첨부파일명·표시 용량·첨부 표시시각을 확인했다. 파일은 각각 `iX7M_KOR_Ver1.3_260605.pdf`(12.4 MB), `iX7NH_KOR_Ver1.7_260605.pdf`(19.5 MB)로 표시된다.
- iX700M 400V DRIVE 매뉴얼 Ver1.4가 공식 Servo 매뉴얼 목록에 2026-05-26 게시물로 표시된다. 세부 첨부파일명/크기는 미확인.
- iX7M/iX7NH 직접 첨부 다운로드는 timeout/HTTP 502. PDF 원본 바이트, SHA-256, 페이지 수, 본문 검토는 미완료이며 METADATA_ONLY/METADATA_VERIFIED로만 기록한다.
- 보고서 §25 및 `sources/manufacturer/LS_MECAPION_MANUAL_INTAKE_2026-11-20.json` 참조. 제품별 scope/classification/RDPS Unknown, security tests Not Run.

# CRA 프로젝트 현재 상태 — 2026-11-20 KST

> 최신 상태 스냅샷. 역사 기록은 SESSION_LOG 및 PROJECT_LOG에 append-only로 보존한다.


## 인용 정정 — CRA 공식 지침 문서번호 (2026-11-20)

- 보고서 §15.1의 이전 표기 `C(2026) 6013`을 정정한다. 최종 공식 관보 인용은 `OJ C/2026/6013` (17.11.2026)이며, `C(2026) 5252 final`은 초안 지침 승인 문서다.
- 최종 해설 근거는 EUR-Lex OJ C/2026/6013 PDF와 committed source manifest를 사용한다. C(2026) 5252 ANFR fallback copy는 non-primary로만 기록한다.

## 최신 main 기준점 — PR #119 CRA 공식 관보 해설 분석 병합 (2026-11-20)

- PR #119 squash merge / main SHA: `46feea8fab4924889be30f8ae5afb7a072673055`; post-merge safety ref: `safety/post-merge-pr119-2026-11-20`.
- PR exact-head Run #1038 / ID `44639933454`: success. Source integrity, compile, CRA traceability, full pytest, official PDF source retrieval and provenance manifest upload passed.
- PDF source artifact #14584694804, 3,070,503 bytes, SHA-256 `a45396f7bc6d0d8abd29c1e0b3ee3655197e23f005fe5e3fbe6df16768a7f0c2`; official PDF byte hashes matched the durable manifest committed under `sources/official/`.
- OJ C/2026/6013 final guidance: 61 pages, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`. M/606 Annex: 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- C(2026)5252 draft fallback via ANFR is marked non-primary. Final interpretive source is EUR-Lex OJ C/2026/6013; the regulation prevails over non-binding guidance.
- Exact-main push CI remains not independently confirmed. Product-specific scope/classification/RDPS remain Unknown; security tests Not Run.

## 이전 main 기준점 — PR #118 ETSI 상태 정정 병합 (2026-11-20)

- PR #118 merge SHA / main: `ee30bdccbc719cce46999a9c9df4ee3fc0609144`; post-merge safety ref: `safety/post-merge-pr118-2026-11-20`.
- PR #118 exact-head Run #1036 / ID `44639411922`: success; source integrity, compile, CRA traceability, full pytest, official PDF source acquisition, HTML provenance manifest 단계 통과.
- PDF source artifact #14584269836, 3,070,504 bytes, SHA-256 `0c77f3ae2546927fd2ae37da024b1b398e0d58a0be08fde50581a984f685c94f`. EUR-Lex OJ C/2026/6013 final PDF (61 pages) SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`; C(2026)7861 Annex (6 pages) SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- Artifact includes one C(2026)5252 draft PDF fetched via ANFR fallback; that mirror is flagged as non-primary and not used for final legal interpretation.
- Exact-main push CI remains not independently confirmed. Product-specific scope/classification remain Unknown; security tests Not Run.
- CRA official guidance analysis is in integrated report §24. It is interpretive guidance, not a binding regulation.

## 최신 재개 업데이트 — 2026-11-20

- 작업 기준 main: `82e9bbf31124b840fa560f7a9e45b1fe84c53ce7` (세션 시작 시 실시간 조회).
- 이번 작업 브랜치: `cra/m606-live-etsi-status-audit-2026-11-20`; 사전 복구 기준: `safety/pre-m606-live-status-audit-2026-11-20`.
- M/606 개정 납기: C(2026) 7861 Annex I 원문 기준 항목 1·15 = 2026-11-30, 2–14 = 2027-10-30, 16–41 = 2027-01-31.
- ETSI Work Programme Version 2.3.3(2026-11-19)에서 M/606 활성 작업 18개를 확인. 이는 전체 41개를 의미하지 않는다.
- CEN-CENELEC 공식 발표(2026-11-19)에서 EN 40000-1-1(용어) 및 EN 40000-1-2(원칙·제품 위험관리·생애주기 활동) 발행을 확인. OJ 인용은 확인 전이므로 Article 27 적합성 추정은 주장하지 않는다.
- 11-19 ETSI 요약 목록 기준 EN 304 625 의견 분류 평가(11-05), EN 304 626 의견 분류 평가(11-06), EN 304 636 의견 분류 평가(10-06)를 반영했다. 이전 상세 페이지의 종료 상태와 다른 경우 최신 요약 목록을 우선하며, 예정 일정은 실적과 구분한다.
- CRA Article 27 적합성 추정은 실제 OJ 참조 게재 범위에 한정한다. ETSI 작업계획상 예정일이나 승인 절차 종료만으로 적합성 추정을 주장하지 않는다.
- 상세 addendum은 LS메카피온 통합 예비 보고서 §23에 기록한다.
- **미완료:** M/606 41개 전 항목의 CEN/CENELEC·ETSI 상태 및 OJ 실제 게재 전수감사 (EN 40000-1-1/-1-2 발행만 부분 확인), LS메카피온 원본 PDF/설치파일/ESI 원본 다운로드·SHA-256·페이지 검토, 정확한 SKU/HW/FW/EU 공급경로 증거, 제품별 분류 및 보안시험.
- 제품별 scope/classification/conformity = Unknown; security tests = Not Run. 이번 작업으로 이 상태를 승격하지 않는다.


## 이전 main 기준점 — PR #116 M/606·EN 40000 최신 상태 갱신 병합 (2026-11-20)

- PR #116 squash merge 완료: `6092ca1c61c696a716583e6bc0f7d5150cbee269`; 현재 main 기준점은 이 SHA다.
- Pre-work safety: `safety/pre-m606-live-status-audit-2026-11-20`; post-merge safety: `safety/post-merge-pr116-2026-11-20`. post-merge ref는 merge SHA에서 생성했다.
- PR exact-head Run #1032 / ID `44638812806`: success. Source blob integrity, compile, CRA traceability, full pytest, live official CRA HTML provenance manifest 단계 통과.
- Provenance artifact #14584442966, 2,566 bytes, SHA-256 `408714c0be46f9238250aaff678191a86ac0ff35112370132d679f59ba591836`, expires 2026-11-26 23:35:10 UTC.
- PDF artifact upload 단계는 skipped이며 PDF 파일 artifact가 생성되지 않았다. 이 run에서 PDF 원문 확보 성공으로 간주하지 않는다.
- PR #116은 보고서 §23 및 상황판/마스터 계획/README/로그만 변경. 운영 runtime/workflow/secrets/state/history/legacy SIL 3 자료는 변경하지 않았다.
- Exact-main push CI는 현재 연결된 조회에서 독립 확인되지 않았다. PR exact-head CI 성공과 구분해 기록한다.
- 제품별 CRA scope/classification/conformity = Unknown; security tests = Not Run. M/606 41개 전수 상태/OJ 감사와 LS메카피온 원본 파일 확보는 미완료.

## 이전 main 기준점 — PR #104 LS메카피온 제품군 예비 분석 보고서 병합 (2026-11-19)
- PR #104 merge SHA / main: `c3d234240d342d82cf9402ef0b07b82531ddee03`.
- PR #104 exact-head Run #1004 / ID 44485297107: success, **174 passed / 0 failed**.
- Source blob integrity, compile, CRA traceability (claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, M/606 41), full pytest 통과.
- Live official CRA HTML source pack 10개 fetch 성공. 10-record provenance manifest JSON parse + object round-trip 성공.
- Manifest artifact #14509668548, 2,566 bytes, SHA-256 `1d3ac8ea2e049780161766ef158fecfa3ab2a7d795b477424b339e5004772bf6`, expires 2026-11-26 08:10:28 UTC.
- PDF canary: EUR-Lex C/2026/6013 PDF endpoint empty body로 temporary source outage / SKIPPED. PDF artifact 없음. PDF canary를 성공으로 표시하지 않는다.
- Pre-merge safety `safety/pre-lsmecapion-family-assessment-2026-11-19`; post-merge safety `safety/post-merge-pr104-2026-11-19`와 main identical.
- Exact-main push CI는 독립 확인 전이므로 성공으로 기록하지 않는다.
- LS메카피온 제품군 예비 보고서 v0.1이 main에 추가됨. 정확한 모델/SKU, HW/FW revision, EU 공급 경로, 모델별 매뉴얼·SBOM·보안 설계·시험 증거는 미확인. 제품별 scope/classification/conformity Unknown, 시험 Not Run.


## LS메카피온 제품군 예비 분석 — 2026-11-19
- 사용자 지시에 따라 분석 대상을 LS메카피온 서보드라이브 제품군으로 설정했다. 정확한 SKU/model은 아직 미지정.
- 제조사 공개 제품 페이지에서 13개 계열(iX700M, iX7M, iX7NH, L7NHA, L7NHB, L7NHF, L7PA, L7PB, PHOX, L7C, L7SA, L7SB, GEM)을 확인했다.
- 제품군별 전압/용량/통신형·펄스형 정보는 공개 페이지 수준에서만 확인. 각 모델 PDF 매뉴얼·카탈로그의 원본 다운로드, SHA-256, 페이지별 검토는 아직 미완료.
- DriveCM 안내는 L7P/L7NH/L7NHF/PEGA/PHOX/iX7NH/L7C/iX7M 지원과 L7S/L7N 구형 도구 사용 구분을 보여준다. 이를 HW/FW 동일성이나 현재 지원기간의 증거로 확대하지 않는다.
- 보고서 `reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md` v0.1이 PR #104로 main에 병합됨: 초보자용 CRA 설명, 제품군 표, Article 2 데이터 연결, Annex III/IV 핵심 기능, 제조사 의무, Article 14, 위협 시나리오, 참조 아키텍처, 시험·증거 계획 포함.
- 잠정 결론: EtherCAT 계열은 데이터 연결이 포함될 가능성이 높다. 펄스/아날로그 계열도 디지털 서비스·설정 인터페이스 및 지령의 성격에 따라 판단한다. EtherCAT/RTOS/MCU 존재만으로 Annex III/IV 분류를 자동 확정하지 않는다.
- EU 시장 공급·모델별 intended purpose·HW/FW revision·프로토콜·제품 경계·RDPS·지원기간 자료가 없으므로 제품별 CRA scope/classification/conformity는 Unknown.
- 법령 전수 수집·분석은 미완료. 현재 HTML 10 source + PDF 3 source 파이프라인은 주요 CRA 법령·공식자료를 다루지만 관련 제품법령·표준 전문·OJ 조화표준 인용·최신 ENISA FAQ 전수 감사가 남아 있다.
- 보안 시험은 모두 Not Run. 이 보고서는 예비 분석이며 최종 적합성 평가가 아니다.

- PR #104 exact-head CI Run #1004: 174 passed / 0 failed. PDF canary는 EUR-Lex endpoint empty body로 SKIPPED이며 PDF artifact 없음. HTML 10-source manifest는 JSON round-trip 검증 및 artifact 업로드 성공.

## 현재 기술 게이트
- Annex III/IV classification is based on the product's core functionality as a whole under Implementing Regulation (EU) 2025/2392. Integrated components do not automatically classify the complete drive.
- CRA applicability under Article 2 and category classification under Articles 7–8 are separate decisions. Annex III/IV non-listing does not mean CRA exclusion.
- Product-specific model/SKU, manuals, network topology, remote-processing dependencies and actual MCU part number remain unknown. Individual product classification remains Unknown / Not assessed.
- Official source pack v4 includes Commission Implementing Regulation (EU) 2025/2392 with live Annex I category 10 / Annex II category 1 locator checks.
- The 10-source provenance manifest is now persisted as a GitHub Actions artifact and validated with JSON parse + round-trip equality.
- Next: LS메카피온 각 제품군별 P0 매뉴얼·카탈로그를 확보하고, 정확한 SKU/variant가 정해진 모델부터 E-001/E-002 증거를 검증한 뒤 EVD/SEC link를 적용/비적용/조건부로 판정. Product-specific classification, implementation and test evidence remain Unknown until source material and versioned test records are received.

## 추가 프로젝트 기록 — PR #86 및 PR #87
- PR #86 current-status/evidence-gate documentation sync merge `7ef3ecb44837826f53c2cad5a38787172ee430ab`; exact-head Run #951 and exact-main Run #952 success, 161 passed / 1 xfailed. Artifacts: #14401607639 (`sha256:41428d58615f76f6aee7010ff96ab91bc6d77ce84bb13e025220678d45a9b352`) and #14400948497 (`sha256:84c4a8855d7b254361438551e4489df75d477cc7431cc5c1a12a3a813d97ad42`).
- PR #87 removes the stale expected failure: production code already fails closed on git push error; the prior test expected a nonexistent namespace state instead of asserting SystemExit(1). New test asserts nonzero exit, checked git push, failure log, and absence of success message.
- Test suite improved from 161 passed / 1 xfailed to **162 passed / 0 xfailed**. No production runtime or production workflow change.

## 이전 main 기준점 — PR #85 및 사후 CI 완료 (2026-11-18)
- PR #85 PR #84 merge/Run #948 checkpoint squash merge: `db05c57103fc9039347b61a29f473fe1af1c7082`; PR head `68599373a5bcfe7bae0ea3240c3a0598b4e8d700`, Run #949 success.
- Pre-merge safety `safety/pre-pr85-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr85-2026-11-18`; post-merge safety == main.
- Exact-main Run #950 / ID `44235614741` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #949 artifact #14396114166, SHA-256 `a936ebf9dd3313dfe02294fddc4251edbbbbf392979afa9cbaf739741f7705a4`; Run #950 artifact #14397720052, SHA-256 `3db5dd4335c9e224aa46abc2e2cd4c3560801b7b5483678b89ec8b012b6d31fb`, expires 2026-11-25 04:12:03 UTC.
- PR #85 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 현재 기술 작업 상태 및 다음 게이트 — 2026-11-18
- CRA 통합 보고서 v0.2, 적용성/P0 intake, EVD-01~16 증거 매트릭스, 참조 보안 아키텍처 v0.2, ST/TI MCU 후보 비교 및 MCU-T01~T12 시험 프로토콜이 main에 존재한다.
- 법령/표준 측: M/606 C(2026)7861 일정 변경을 반영했으나 ESO의 개정 결정 수령일·Article 2 비수락 통지 여부와 각 표준 최종 전문/OJ 인용은 별도 확인 전까지 미확정. 표준 납기와 CRA 법적 적용일을 혼동하지 않는다.
- 제품별 판정: 제조사/정확한 드라이브 모델·SKU, BOM/회로도, 실제 ST MCU 마킹/주문코드, 펌웨어·프로토콜·원격처리 경계가 없으므로 적용성/Annex III·IV 분류 및 MCU 적합성은 Unknown/보류.
- 시험: MCU-T01~T12는 계획·기록 양식만 준비된 상태이며 전부 Not Run. 측정 결과·점수·승자·교체 권고를 만들지 않는다.
- 다음 우선순위: (1) 제품 라벨/BOM에서 ST MCU 정확한 part number와 silicon revision 확보, (2) 제어 주기·PWM/ADC·encoder·fieldbus·WCET/jitter 요구 수집, (3) 실제 제품 변형별 Article 2 및 Annex III/IV core-functionality 판정, (4) EVD/SEC 요구-통제-시험-증거를 제품별 연결, (5) 동일 조건 bench 실행.
- 독립 품질 감사 결과: 현재 문서는 공통 프레임워크/예비 설계로 올바르게 한계를 표시하고 있으며, 제품별 실증·적합성 완료로 오인하지 않도록 Unknown/Not Run 게이트를 유지해야 한다.

## 이전 main 기준점 — PR #84 및 사후 CI 완료 (2026-11-18)
- PR #84 PR #83 merge/Run #946 checkpoint squash merge: `774551f378f59c82ce34342f63fd595d4c743852`; PR head `ba5e6e6179d6259cb5088d110e352f316ddcb589`, Run #947 success.
- Pre-merge safety `safety/pre-pr84-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr84-2026-11-18`; post-merge safety == main.
- Exact-main Run #948 / ID `44235249125` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #947 artifact #14396088675, SHA-256 `9c164a7f550bc2f2c1f6292f971e9d4db250dcfa0bdb06ef0c6187da116b65ae`; Run #948 artifact #14397286074, SHA-256 `1cd7be5fcd710e5fc193595602c974a701f1242f32ec5a549ea61a11c9eec388`, expires 2026-11-25 04:08:57 UTC.
- PR #84 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #83 및 사후 CI 완료 (2026-11-18)
- PR #83 PR #82 merge/Run #944 checkpoint squash merge: `0255e50f003792fa8f5d0d3a130e45dda3491c3d`; PR head `7a6ecd85b786ad2fefc1422edaf9d904bcc2a758`, Run #945 success.
- Pre-merge safety `safety/pre-pr83-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr83-2026-11-18`; post-merge safety == main.
- Exact-main Run #946 / ID `44234852177` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #945 artifact #14395674978, SHA-256 `8fac91a19e3eedcdb99dea22c2bda49dc650f3cfe1a39582d172f2ff0f6af9fb`; Run #946 artifact #14396926567, SHA-256 `0da05816f553bfbe1f541df001f2f487bd66176e3b454eb04ee47cffd3330a33`, expires 2026-11-25 04:05:37 UTC.
- PR #83 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #82 및 사후 CI 완료 (2026-11-18)
- PR #82 PR #81 merge/Run #942 checkpoint squash merge: `572de72c8bfab7a1e1e144527783c1508bb26cae`; PR head `afce74763363aadf27b6c340f59b41da48198920`, Run #943 success.
- Pre-merge safety `safety/pre-pr82-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr82-2026-11-18`; post-merge safety == main.
- Exact-main Run #944 / ID `44234505453` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #943 artifact #14395849674, SHA-256 `b978bbe302f3d9e68aa8ef2a2a4643c69fdb485e80e9ec14514642645724f2bd`; Run #944 artifact #14396972010, SHA-256 `f23e616d121c61d5825774f1098f213b40cff65e858a527807060d71b02734c4`, expires 2026-11-25 04:02:31 UTC.
- PR #82 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #81 및 사후 CI 완료 (2026-11-18)
- PR #81 PR #80 merge/Run #940 checkpoint squash merge: `11b7ccac639501b98e9a9f6c76dfac473d6e0535`; PR head `e0d6f2015b65a1b6ca7dfc08947bc68d378e92a5`, Run #941 success; artifact #14396187702, SHA-256 `d01984ddcc528a9b70fbb55ca6904d3d86be0272dedd3018972202a4b16c8937`.
- Pre-merge safety `safety/pre-pr81-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr81-2026-11-18`; post-merge safety == main.
- Exact-main Run #942 / ID `44234103515` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #942 artifact #14397065458, SHA-256 `0d5a340c3ac3e0435704d5543f38ab35bd883ea7a5c30adfe1b3983db24882bf`, expires 2026-11-25 03:59:05 UTC.
- PR #81 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #80 및 사후 CI 완료 (2026-11-18)
- PR #80 PR #79 merge/Run #938 checkpoint squash merge: `950cacef2ea4ed2bb4062f09ef0180a5621375a5`; PR head `04461bd92328504687ba657f51adc0f3b490d108`, Run #939 success; artifact #14396676441, SHA-256 `fec64e8793a81a8297769bba11a2f55d775feb8c90bb34c5bcd338329c0f6680`.
- Pre-merge safety `safety/pre-pr80-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr80-2026-11-18`; post-merge safety == main.
- Exact-main Run #940 / ID `44233727424` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #940 artifact #14396950302, SHA-256 `dca34e12cfea64f9f6a5676a084910e465bf2f8bb415eee4173681683ea9a9cb`, expires 2026-11-25 03:55:48 UTC.
- PR #80 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #79 및 사후 CI 완료 (2026-11-18)
- PR #79 PR #78 merge/Run #936 checkpoint squash merge: `2e377127a26d3d9c0232089cad583ff6f2d328ca`; PR head `15b834717e94476a22f2b05719377eb356e9db29`, Run #937 success.
- Pre-merge safety `safety/pre-pr79-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr79-2026-11-18`; post-merge safety == main.
- Exact-main Run #938 / ID `44233403451` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #938 artifact #14396566514, SHA-256 `d9f1c96ecab857a65c699b18489315fcf5edbe0892234dc5c42157dceb2dd156`, expires 2026-11-25 03:52:43 UTC.
- PR #79 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #78 및 사후 CI 완료 (2026-11-18)
- PR #78 PR #77 merge/Run #934 checkpoint squash merge: `441b0198bcd695752d1adb053d8e077f91426a0a`; PR head `6610ee297b00c0717863daa4734141a519b78008`, Run #935 success.
- Pre-merge safety `safety/pre-pr78-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr78-2026-11-18`; post-merge safety == main.
- Exact-main Run #936 / ID `44233080095` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #936 artifact #14396500899, SHA-256 `6ef8037213259261dd57bcc3b1229d50f58947092a953bbc12ffc106ee4c8a05`, expires 2026-11-25 03:49:49 UTC.
- PR #78 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #77 및 사후 CI 완료 (2026-11-18)
- PR #77 PR #76 merge/Run #932 checkpoint squash merge: `caa32ed9ac6679b21b619155cdf28d1b75d81c33`; PR head `e3a8efcd33c601eccea1d1e1c1e054d07f946f9b`, Run #933 success.
- Pre-merge safety `safety/pre-pr77-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr77-2026-11-18`; post-merge safety == main.
- Exact-main Run #934 / ID `44232761348` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #933 artifact #14395517878, SHA-256 `b6218e7153590ed63f52b35dc6013e79bd38af098dafb3b0cc2149afe419138d`; Run #934 artifact #14395218493, SHA-256 `8c827f786583bb5d2f8d14224e990b194ae50bf7f1393b4b9009925d123773da`, expires 2026-11-25 03:47:01 UTC.
- PR #77 documentation/log-only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #76 및 사후 CI 완료 (2026-11-18)
- PR #76 MCU-T01~T12 시험 매트릭스·기록 양식 squash merge: `48afedaf8114688a51a7e6ed695c514277bd6407`; PR head `30340417bf8440292c1397c3d5afb77e017f5a20`, Run #931 success.
- Pre-merge safety `safety/pre-pr76-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr76-2026-11-18`; post-merge safety == main.
- Exact-main Run #932 / ID `44232432357` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #931 artifact #14395881347, SHA-256 `11d970dd8d64782fe5c62b12d5cea11cde231f28811c5470226ab6d126a31e4a`; Run #932 artifact #14395691349, SHA-256 `ec315a8b305f9b572452d42846de38a3698d431256faff36162ddb733303385a`, expires 2026-11-25 03:44:07 UTC.
- PR #76 documentation-only; production runtime/workflows/secrets/state/history/archive/legacy SIL 3 files untouched.

## 이전 main 기준점 — PR #75 및 사후 CI 완료 (2026-11-18)
- PR #75 MCU 예비 벤치마킹·상황판 업데이트 squash merge: `1d7325baa592b35585fde850cf5a155988ba4cde`; PR head `c809e834e6290dbe96f9c6e88d5615efb2765373`, Run #929 success.
- Pre-merge safety `safety/pre-pr75-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr75-2026-11-18`; post-merge safety == main.
- Exact-main Run #930 / ID `44231956995` on merge SHA: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #929 artifact #14396015379, SHA-256 `58e88c05c8501aba2d82c8345d0f1e5222843e15c9939c174e8beaad7a55f4da`; Run #930 artifact #14395188271, SHA-256 `63017368ac7db313f298b23c24d288f9c6781c27cc26472baa6d408abb244695`, expires 2026-11-25 03:39:52 UTC.
- PR #75 문서/로그 변경만 포함; runtime/workflow/secrets/state/history/archive/legacy SIL 3 자료 미변경.
- MCU-T01~T12 시험 케이스·재현성 기록 양식은 PR #76으로 병합 완료.
- P0 미확인: 실제 ST MCU 주문 코드/마킹·silicon revision, motor/control loop 사양, PWM/ADC/encoder 구성, fieldbus, BOM/firmware resource budget.
- 다음 게이트: 실제 ST MCU 부품번호(칩 마킹/BOM)와 제어 사양을 확보해 MCU-T01~T12를 제품별로 구체화하고 동일 조건 실측. 실행 전 점수/승자/교체 결론 금지.

## 이전 main 기준점 — PR #74 사후 검증 완료 (2026-11-18)
- `main` HEAD: `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`; exact-main Run #928 / ID `44231392940` success (161 passed, 1 xfailed).
- main 사후 안전 브랜치 `safety/post-merge-pr74-2026-11-18`가 main과 동일 SHA. PR #74 exact-head Run #927도 success.
- 현재 기술 산출물: 참조 보안 아키텍처 v0.2와 MCU 예비 벤치마킹 문서 `reports/CRA_SERVO_DRIVE_MCU_PLATFORM_BENCHMARK_2026-11-18.md`.
- PR #74 당시 main에는 참조 보안 아키텍처 v0.2가 병합됐고, 이후 PR #75에서 ST/TI MCU 예비 벤치마킹이 추가됐다.

## 이전 main checkpoint — PR #71 (2026-11-18)
- PR #71 `docs: record PR70 merge and exact-main verification` squash merge 완료: `adcec0a0cb94a326e6b7d9b8c242c4ae3dab4152`.
- PR #71 exact head `bb5cb36598c5a6daa7982781a6db2726d81f9530`, Run #921 / ID `44228810756`: success. Source integrity, compile, CRA cross-matrix traceability, full pytest, official CRA PDF/HTML canaries 통과. Artifact #14394585712, SHA-256 `cff5e21b032fd5f7de923e080de3b7b133b214da697a185efb2318ab04fbf0bc`.
- Pre-merge safety ref `safety/pre-pr71-merge-checkpoint-2026-11-18`; post-merge safety ref `safety/post-merge-pr71-2026-11-18`.
- Exact-main Run #922 / ID `44230377812`, head `adcec0a0cb94a326e6b7d9b8c242c4ae3dab4152`: **success**; 161 passed, 1 xfailed. Source blob integrity, compile, CRA traceability (13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items; bidirectional links true), official PDF source canary and 9-source live official CRA canary/corrigenda/Article 13(8) locator-quote verification all passed.
- Run #922 artifact #14393784949, SHA-256 `db75a58638b43fbe1798c70b7c4dad5951cb1b1f98bfa013fa771184e6cf2126`, expires 2026-11-25 03:26:21 UTC. Official PDF hashes: Guidance Annex mirror fallback=True `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; OJ C/2026/6013 fallback=False `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`; M/606 C(2026)7861 Annex fallback=False `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- Confirmed `main` == `safety/post-merge-pr71-2026-11-18` at the merge SHA. PR #71 touched only project-control documentation/log files; production runtime, production workflows, secrets, state/history/archive and legacy SIL 3 files were not modified.

## 이전 main checkpoint — PR #72 (2026-11-18)
- PR #72 문서/로그 checkpoint squash merge: `293a27a8ea2a8e03f58db50bbe27d2aaea194c8d`; PR head `0f85cc04eb64efe961e514a59a28386b5527708c`, Run #923 success.
- Pre-merge safety `safety/pre-pr72-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr72-2026-11-18`; post-merge safety == main at merge SHA.
- Exact-main Run #924 / ID `44230705429` on `293a27a8ea2a8e03f58db50bbe27d2aaea194c8d`: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability, 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Artifact #14394119675, SHA-256 `43a5e60b947890886baeee6c355beae857928f3c47deb9d76489244199accb3a`, expires 2026-11-25 03:29:17 UTC. PDF provenance hashes match Run #922; Guidance remains ANFR fallback=True, OJ Guidance and M/606 Annex fallback=False.
- PR #72 changed project-control documents only; runtime/workflow/secrets/state/history/archive/legacy SIL 3 materials untouched.

## 최신 설계 산출물 — 참조 보안 아키텍처 v0.2 (2026-11-18)
- `reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md`를 v0.2로 보강한 작업 브랜치 `cra/servo-drive-security-architecture-v02-2026-11-18`에서 PR #74 병합 완료; exact-head Run #927 및 exact-main Run #928 성공.
- 실시간 데이터 경로와 관리/업데이트 경로 분리, 단일 MCU vs 통신·제어 MCU 분리 선택 기준, 부팅/업데이트 검증 순서, 설계 수용 기준 및 EVD/SEC 추적을 추가.
- 제품별 부품/회로/펌웨어가 없으므로 참조 설계일 뿐 제품 구현·시험·적합성 판정은 미완료.

## 이전 main checkpoint — PR #73 (2026-11-18)
- PR #73 문서/로그 checkpoint squash merge: `16ab607a919c6bfa4fee8dc90ab5af2ea2f53352`; PR head `cd78b6694384d550ef68d7f1b7ec2972a02a663e`, Run #925 success.
- Pre-merge safety `safety/pre-pr73-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr73-2026-11-18`; post-merge safety == main.
- Exact-main Run #926 / ID `44230997446` on `16ab607a919c6bfa4fee8dc90ab5af2ea2f53352`: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Artifact #14394634118, SHA-256 `cf7d6d6ef7020d5381a4a2f201f50bf3171251155459505420ffce16998ef027`, expires 2026-11-25 03:31:37 UTC.
- PR #73 touched only project-control documents; no runtime/workflow/secrets/state/history/archive/legacy SIL 3 files changed.

## 이전 main checkpoint — PR #74 (2026-11-18)
- PR #74 참조 아키텍처 v0.2 문서 변경 squash merge: `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`; PR head `4ee2d73bf7bc5826c001011b17133d4a6a8071ec`, Run #927 success.
- Pre-merge safety `safety/pre-pr74-merge-checkpoint-2026-11-18`; post-merge safety `safety/post-merge-pr74-2026-11-18`; post-merge safety == main.
- Exact-main Run #928 / ID `44231392940` on `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`: **success**, 161 passed / 1 xfailed; source integrity, compile, CRA traceability (13/15/35/36/41), 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #927 artifact #14395142564, SHA-256 `64c359db2e764f2506345e3fee3c5e20bbacacdf3e3e67d095f02caa7126b528`; Run #928 artifact #14395476337, SHA-256 `6aaf8fc76f87121e42f8190fec9568121fbd8a0005695ce8de87ff776f0d1d93`, expires 2026-11-25 03:34:56 UTC.
- PR #74 changed only documentation/log files; production runtime/workflows/secrets/state/history/archive/legacy SIL 3 files untouched.

## 다음 하드웨어 조사 — MCU 후보 기술 벤치마킹 (2026-11-18)
- `reports/CRA_SERVO_DRIVE_MCU_PLATFORM_BENCHMARK_2026-11-18.md` 초안: ST 기준 후보 STM32G474RE/H753XI, TI 비교 후보 MSPM0G3529-Q1을 공식 제조사 자료로 대조.
- 실제 ST MCU 부품번호와 제어 사양이 미확정이므로 선정/대체 결론은 보류. CPU MHz/DMIPS는 동일 조건 벤치마크가 아님.

## 활성 범위
- 활성 프로젝트: EU Cyber Resilience Act(CRA) 조사·요구사항 추적·제품 적용성/기술 설계·보고서 검증.
- SIL 3 기능안전 자료는 과거 산출물로 보존하며 비활성이다. 별도 명시적 재개 지시 전까지 후속 작업하지 않는다.
- 보고서 기본 언어: 한국어.
- 제품별 적합성/Annex III·IV 분류는 제조사·정확한 모델·의도된 목적·제품 경계·인터페이스·공급 구조 증거 없이는 확정하지 않는다.

## 최신 기준점 및 PR #42 결과
- 기준 브랜치: `main`
- PR #42: [docs: clarify CRA legal locator and SBOM requirements](https://github.com/useformotor3/ai-discord-bot/pull/42) — merged.
- Merge commit: `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`
- PR head: `0ff686be74fb5c6309b46ed9c01473251d997579`
- CI: [Run #824](https://github.com/useformotor3/ai-discord-bot/actions/runs/44061121932) — success; 155 passed / 1 xfailed.
- 검증 단계: source blob integrity, compile, CRA cross-matrix traceability, full pytest, official PDF source fetch/hash/page canary, artifact upload, 9 official HTML sources 및 Article 13(8) live locator/quote canary.
- 변경 범위: 문서·감사·상황판/프로젝트 관리 자료. production runtime, production workflow, state/history/archive, Gemini/Discord side effects, SIL 3 자료는 변경하지 않았다.
- 리뷰 스레드/리뷰 제출은 없었으며 PR은 exact head CI 성공 후 squash merge했다.

## 복구 및 main 정합성
- Pre-merge safety ref: `safety/pre-merge-main-pr42-2026-11-18` → `acfa2f583157ac541c4c60d71090197322bc8efb`
- Post-merge safety ref: `safety/post-merge-main-pr42-2026-11-18` → `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`
- GitHub compare: `main` vs post-merge safety ref = identical, 0 ahead / 0 behind.
- 롤백이 필요하면 force-push 대신 검토된 revert commit을 우선한다. safety refs는 삭제하지 않는다.

## 현재 CRA 산출물 기준선
- 통합 한국어 보고서: `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` (v0.2 draft; 제품별 검증 전)
- 요구사항 추적표: `reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv` (CRA-001–CRA-035)
- 인터페이스 적용성 매트릭스: 15 rows
- SEC 통제/시험 매트릭스: 36 rows
- Commission Guidance claim register: 13 claims
- M/606 Annex I crosswalk: 41 items
- 독립 보고서 감사: `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md`
- 법령 locator 1차 인벤토리 검토는 35행 모두 조항 번호/구조의 명백한 불일치가 보이지 않았다는 수준이다. 모든 문장의 의무 주체·조건·예외·기한을 확정한 최종 법률 검토가 아니다.

## 확정된 SBOM 해석
1. Annex I Part II(1): 제조자의 기본 SBOM 작성 의무. 일반적으로 사용되는 기계 판독 가능 형식이며 최소 최상위 의존성을 포함한다.
2. Annex VII(2)(b): 취약점 처리 프로세스 설명에 SBOM을 기술문서 내용으로 포함한다.
3. Annex VII(8): 필요한 경우 시장감시당국의 합리적 요청에 따른 추가 제공 조항이다. 기본 작성 의무를 선택사항으로 만들지 않는다.
4. Annex II(9): 제조자가 SBOM을 사용자에게 제공하기로 결정한 경우 접근 위치 정보를 제공한다. 일반 사용자 공개 의무와 기본 작성/기술문서 의무를 혼동하지 않는다.

## 남은 원문 provenance 제한
- M/606 C(2026) 7861 Annex PDF: 151,267 bytes, 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`; primary Commission source canary fallback=False.
- Commission Guidance C(2026) 5252 Annex PDF: ANFR mirror fallback bytes 1,190,726, 84 pages, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; fallback=True. Commission-hosted primary bytes와의 동일성은 미확인이다.
- CI artifact #14318292097, Run #824에서 업로드 성공. artifact URL: https://github.com/useformotor3/ai-discord-bot/actions/runs/44061121932/artifacts/14318292097

## 다음 실행 순서
1. CRA-001–CRA-035를 법령 원문 기준으로 행 단위 심층 검토한다. 조항 locator뿐 아니라 의무 주체, 행위, 적용 조건, 예외, 기한, 보존기간, 제품 사실 전제 및 근거 문장을 별도 확인한다.
2. 발견 사항은 CSV·통합 보고서·SEC 통제/시험 매트릭스·독립 감사 기록을 한 변경 묶음으로 정합화한다. 법적 의무와 Guidance 해석, M/606 표준화 작업, 설계 권고를 분리한다.
3. Article 14 신고 시한/범위, Article 13 지원기간·업데이트 보존, Annex I Part II SBOM/취약점 처리, Article 32 평가 경로, Article 69 전환/중복 규칙을 우선 위험 영역으로 검토한다.
4. Guidance PDF Commission-primary byte identity 취득 경로를 계속 확인하되 mirror fallback을 원본이라고 표시하지 않는다.
5. 각 작업은 main 기준 feature/docs branch, pre-merge safety ref, exact-head CI, squash merge, post-merge safety ref 및 main compare를 유지한다.

## 해석상 금지
- CRA 적용 대상/등급/적합성/인증 경로를 특정 서보 드라이브 모델에 대해 증거 없이 단정하지 않는다.
- M/606 요청/ESO adoption deadline을 조화표준 OJ 공표나 제조사 CRA 적용일로 취급하지 않는다.
- CRA와 SIL 3 기능안전 인증을 동일시하지 않는다.
- CI 통과를 법적 적합성 또는 제품 시험 완료로 확대 해석하지 않는다.


## 최신 진행 추가 — CRA 법령 문언 Batch 1 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch1-2026-11-18` (PR 전 검증 중)
- 검토 범위: CRA-001–CRA-010, EUR-Lex Regulation (EU) 2024/2847 공식 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`.
- CSV locator 보완: CRA-001 연결 정의 Article 3(8)–(10)/Recital 9 추가; CRA-003의 부적절한 Article 13(2) 제거 및 Article 3(2)/Recital 11–12로 교체; CRA-006 SBOM/기록/기술문서 locator 분리.
- 해석 보완: CRA-008 정기 테스트에 법정 고정 주기 숫자는 없음; CRA-009 공개 지연 예외는 정당한 사유 및 사용자 패치 적용 기회와 연결.
- CRA-001–010 행별 심층 대조는 1차 완료. 제품별 적용성/적합성은 미확정이며 전체 35행 법률 검토 완료를 의미하지 않는다.
- 다음 대상: CRA-011–CRA-020.


## 최신 진행 추가 — CRA 법령 문언 Batch 2 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch2-2026-11-18` (PR 전 검증 중).
- 검토 범위: CRA-011–CRA-020, EUR-Lex 공식 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md`.
- CSV 보완: 연락창구 통신수단 조건, 업데이트 배포 통제와 법문 구분, 무상 제공 예외의 좁은 범위, support period 5년 예외 근거, 기술문서 작성/보관 분리, Annex V/VI DoC 구분, Article 32 Class I/II/Critical 경로 구분.
- CRA-001–020까지 1차 심층 대조 완료(제품별 증거·최종 법률 검토는 미완료). 다음 대상 CRA-021–035.


## 최신 진행 추가 — CRA 법령 문언 Batch 3 (2026-11-18)
- 작업 브랜치: `cra/legal-semantics-audit-batch3-2026-11-18` (PR 전 검증 중).
- 검토 범위: CRA-021–CRA-035, EUR-Lex 공식 CRA 및 관련 sectoral 원문 대조.
- 상세 결과: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md`.
- CSV locator/구조 보완: CRA-023 Article 14(8) 중심; CRA-026 CRA Article 2(5)/Machinery Regulation Article 9(9) 중심; CRA-028 Articles 18–22와 CRA-034 Article 23 분리; CRA-035 Article 2(8) 추가 및 Article 2(5) 조건부 제한 구분.
- CRA-001–035 전체 행의 1차 심층 문언 대조가 완료되었으나, 제품별 사실/증거 확인과 법률가 검토는 별도 미완료다.
- 다음 단계: 전체 35행 교차 검증 및 CSV·통합 보고서·SEC 매트릭스·근거 등록부의 누락/중복/표현 정합성 검토, 제품 적용성 증거 수집 설계.


## 최신 진행 추가 — 전체 교차 매트릭스 감사 (2026-11-18)
- 작업 브랜치: `cra/cross-matrix-consistency-audit-2026-11-18` (PR 전 검증 중).
- PR #46 병합: `42aca53bb735d79292be59120fb868474e728073`; exact-head CI 성공, pre/post safety refs, post-ref == main 검증 완료.
- CRA-001–CRA-035 1차 심층 문언 대조 완료. 추가로 15 interfaces, 36 SEC controls, 13 Guidance claims, 41 M/606 items 간 교차 참조를 검토.
- 교차 감사 기록: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.
- SEC-015/018/021/031/032/034/036의 locator/설명/연계 ID 정합화.
- 제품별 실제 구현/시험 증거가 없으므로 SEC controls 상태는 미작성/증거 미확인, interfaces는 제품별 미확인 유지.
- 다음 단계: 통합 보고서 전체 독립 재검토, 제품 증거 intake 기준 확정, Commission Guidance PDF primary byte identity 재확인.


## 최신 기준점 — 2026-11-18 (PR #47 반영)
- 최신 main: `fd9733b31e5dffa382a82a420de6a195a714e98f`.
- PR #47 cross-matrix audit merge: `fd9733b31e5dffa382a82a420de6a195a714e98f`; Run #832 exact-head CI success, post-merge safety ref와 main identical 확인.
- Pre-merge ref: `safety/pre-merge-main-pr47-2026-11-18`; post-merge ref: `safety/post-merge-main-pr47-2026-11-18`.
- 35 requirements / 15 interfaces / 36 SEC controls / 13 Guidance claims / 41 M/606 items 교차 정합성 감사 기록: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.
- 제품 증거 수집 기준서에 최신 Article 2/3, RDPS, Annex III/IV, Machinery Regulation, 신고 시한/전환 규칙 및 우선 제출 자료를 추가하는 작업 브랜치: `cra/product-evidence-intake-update-2026-11-18`.


## 최신 main 기준점 — PR #48 병합 후 (2026-11-18)
- 현재 main commit: `dc03173cd78f6efb6f46717850a107c8165b1d1a`.
- PR #48 제품 경계/증거 수집 기준서 보완 merge: `dc03173cd78f6efb6f46717850a107c8165b1d1a`.
- Exact-head CI Run #834 success: source integrity, compile, CRA cross-matrix traceability, full pytest, official PDF/HTML canaries, artifact upload passed.
- Pre-merge ref: `safety/pre-merge-main-pr48-2026-11-18`; post-merge ref: `safety/post-merge-main-pr48-2026-11-18`; post-ref == main identical.
- 제품 증거 기준서 업데이트: Section 13–15에 데이터 연결/RDPS/Annex III·IV/Machinery/신고·전환/자료 우선순위/모델별 판정 출력 기준 추가.
- 제품별 사실 증거는 아직 미제공. P0 자료는 정확한 모델 데이터시트/카탈로그와 사용설명서이며, 이를 받기 전 CRA 적용/등급/적합성은 Unknown 유지.
- 다음 작업: 통합 보고서 전체 독립 재검토 및 Commission Guidance PDF Commission-primary byte identity 재확인. 제품 P0 자료 확보 시 모델별 판정 착수.


## 최신 재개 추가 — 통합 보고서 독립 재검토 (2026-11-18)
- 작업 브랜치: `cra/integrated-report-audit-2026-11-18`; 기준 main: `c7b939a0fdfa559f9d68a11873c107186da423c3`.
- 독립 감사 기록: `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-18.md`.
- EUR-Lex Regulation (EU) 2024/2847 공식 OJ HTML에서 Articles 7, 8, 13(8)–(9), 14, 15, 69, 71 및 관련 Annex의 핵심 문언을 표본 대조했다.
- 통합 보고서 요약의 서보 드라이브 CRA 적용 가능성/기본 제품 분류 표현을 제품별 판정이 아닌 전형적 구성의 사전 스크리닝 가설로 한정하고, 모델별 결론은 증거 확보 전 Unknown으로 유지하도록 보완했다.
- 15 interfaces는 제품별 미확인, 36 SEC controls는 미작성/증거 미확인, 제품 scope/classification/conformity는 Unknown 유지.
- Commission Guidance PDF Commission-primary byte identity는 여전히 미확인. M/606 일정은 이번 회차 원문 bytes 신규 재취득 검증이 아니므로 기존 provenance 상태를 유지.
- 다음: 변경 파일 readback, exact-head isolated CI, PR 생성/검토, 안전 참조점 및 merge 후 main 정합성 확인. CI 성공 전 병합하지 않는다.


## 최신 main 기준점 — PR #50 통합 보고서 독립 감사 병합 완료 (2026-11-18)
- PR #50 squash merge commit: `137d096123ccf5ee478292002d2c528b41981fc7`.
- PR #50 exact-head: `49e98df9a7fef8f47cabe7b036b45cc150b88b91`; isolated CI Run #840 (ID `44200596113`) success.
- Run #840 통과 단계: source blob identity, compile, CRA cross-matrix traceability, complete pytest, official CRA PDF read-only canary 및 artifact upload, live official CRA source read-only canary.
- Pre-merge safety ref `safety/pre-merge-cra-integrated-report-audit-2026-11-18`는 main 당시 기준 commit `c7b939a0fdfa559f9d68a11873c107186da423c3`와 identical. PR #50 병합 후 main은 해당 안전 기준점보다 정확히 1 commit ahead이며, 변경 파일은 PR #50의 8개 문서 파일로만 확인.
- Post-merge safety ref: `safety/post-merge-pr50-2026-11-18`; 이 ref는 새 main 기준점 `137d096123ccf5ee478292002d2c528b41981fc7`에서 생성.
- 변경 내용: 2026-11-18 통합 CRA 보고서 독립 감사 기록 추가, 전형적 서보 드라이브의 적용 가능성/Annex III·IV 표현을 사전 스크리닝 가설로 한정, 개별 모델 결론은 제조사/모델 증거 전 Unknown 유지, README/MASTER_PLAN/SESSION_LOG/PROJECT_LOG 동기화.
- 운영 `main.py`, production workflow, secrets, state/history/archive, Gemini/Discord production execution 및 SIL 3 산출물은 변경하지 않았다.
- 미해결: Commission Guidance PDF의 Commission-primary byte identity, M/606 최신 결정 raw-byte provenance 재취득, 제품별 scope/classification/conformity 및 15 interfaces/36 SEC controls의 제품 증거.
- 다음 우선순위: Commission-hosted Guidance PDF primary byte identity 검증과 M/606 공식 결정 원문/Annex provenance 확인. 제품 P0 자료(정확한 모델 데이터시트/카탈로그 및 사용설명서) 확보 시 모델별 증거 연결.

## 최신 CRA Guidance 원문 기준 — OJ C/2026/6013 (2026-11-18)
- 기존 Commission 승인/게시 문서 참조 C(2026) 5252의 guidance는 2026-11-17 Official Journal에 Communication C/2026/6013 (CELEX 52026XC06013)으로 게재되었다.
- 현재 공식 인용/페이지 기준: EUR-Lex OJ PDF https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- OJ PDF: 2,709,282 bytes, 61 pages, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`; extracted text 255,974 chars, SHA-256 `384724af44e399cb997771e9e65ea4a5fe1dd264131d0754921bd691dd1f7720`.
- C(2026) 5252 ANFR mirror는 별도 역사적 사본으로 유지: 1,190,726 bytes, 84 pages, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`. Commission download document 131456는 2026-11-18 확인 시 HTTP 404.
- 두 PDF에서 numbered paragraph IDs 1–257 모두 발견; 정규화 토큰 multiset overlap은 mirror 99.50%, OJ 99.66%. 원본 bytes/추출 텍스트가 동일하다고 주장하지 않는다.
- Guidance claims 13개(G-001–G-013)의 source ID와 PDF page locator를 OJ C/2026/6013 기준으로 갱신했다. 세부 비교 및 페이지 crosswalk: `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §7.
- Run #844 (44204376214): exact head CI success, 156 passed / 1 xfailed; official OJ PDF primary fetch fallback=False 및 raw SHA 검증 성공. Artifact 14381529964, 7일 보존.

### 다음 작업
1. G-001–G-013 각 claim의 실제 문장·조건·예외를 OJ C/2026/6013 본문과 대조하는 substantive redline 수행.
2. OJ page locator를 표·그림·페이지 경계 포함 PDF 이미지로 표본 재검증.
3. Guidance claim IDs를 요구사항/인터페이스/SEC 매트릭스에 연결하되 법령상 의무와 비구속적 guidance 해석을 분리.
4. M/606 C(2026) 7861 Annex provenance 및 현재 표준화 상태를 최신 공식 원문과 별도 대조.

### PR #52 최종 검증 업데이트 — Run #854
- Exact-head at validation: `0ab0fc4d9b217a4994fd6e7a1b32607c854bb693`.
- Run #854 / ID `44205498935`: success; 158 passed, 1 xfailed; source blob identity, compile, CRA traceability, full pytest, three-PDF canary, official HTML canary all passed.
- OJ C/2026/6013 primary PDF: fallback=False, 2,709,282 bytes, 61 pages, SHA-256 unchanged `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`.
- Artifact #14382388555; digest `sha256:9e8dc7f1c1d90015b7738263155ca9d6b1170aaea75ea6bd17350aeff7d36af7`; expires 2026-11-25 00:09:59 UTC.
- Run #851 failure cause (validator's stale mirror-scope phrase check) corrected; validator now enforces both historical mirror-only scope and OJ primary-source/no-fallback gate. Run #854 passed.

### PR #52 exact-head CI 업데이트 — Run #857
- Tested head `152fe0bfe00c16ab32f7cc030efcde3258b73525`; Run #857 / ID `44205723336`: success.
- 158 passed, 1 xfailed; exact source blob identity, compile, CRA traceability, full pytest, three-PDF canary and live official HTML canary passed.
- OJ C/2026/6013 primary source hash unchanged; fallback=False.
- Artifact #14383167818; digest `sha256:a2f05428d57897a20a485cabaab17cbb976dcb91f6e5628ece0953ddfe22140d`; expires 2026-11-25 00:11:31 UTC.
- Provenance metadata now points to Run #857; final head after this metadata update still requires one fresh CI before merge.

## PR #52 병합 및 사후 안전 검증 — 2026-11-18
- PR #52 `feat: acquire official CRA guidance from OJ C/2026/6013` squash merge commit: `d3956b7b364c507b8d59dcfc056763f2829ea867`.
- Final exact-head Run #861 (ID `44205897044`) success; tested head `dee79027a49dfbb1fdd7cf1036bc0ae39e83b518`; 158 passed, 1 xfailed; source identity, compile, traceability, PDF/HTML live canaries passed.
- Final artifact #14384061014; digest `sha256:2b70d0f09f620c83a531f2ec9be9de6a1ec9a669ee861e16704804fe036eb3d3`; expires 2026-11-25 00:13:02 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-oj-6013-2026-11-18` matched main at `854d66fa6c145ca264dbd768c2c75fcf9f117153`. After merge, main is exactly one commit ahead of that ref and the diff is PR #52's 15 files.
- Post-merge safety ref `safety/post-merge-cra-guidance-oj-6013-2026-11-18` is identical to main at merge commit `d3956b7b364c507b8d59dcfc056763f2829ea867` (post-merge compare: identical).
- Current Guidance source is OJ C/2026/6013, EUR-Lex primary PDF, fallback=False; historical C(2026) 5252 ANFR mirror remains separate and is not claimed byte-identical.
- Next priority: substantive claim-by-claim redline for G-001–G-013 against OJ text, then update relevant interface/requirements/SEC evidence mappings. M/606 provenance review follows.

## CRA Guidance substantive redline complete — 2026-11-18
- OJ C/2026/6013 claim-by-claim review completed for G-001–G-013.
- 9 claims confirmed without substantive change; G-001 locator corrected; G-003/G-008/G-013 wording refined; G-004 expanded to make ongoing conformity/DoC/CE/vulnerability obligations explicit.
- Visual page-image checks completed for OJ pages 7–10, 24–25, 30, 32–35, 42–46, 53 and 61.
- CSV claim register and audit report §8 updated. All claims remain non-binding Commission explanations, not new legal requirements.
- Product-specific scope/classification/conformity remains Unknown; 15 interfaces remain product-unverified; 36 SEC controls remain unimplemented/unverified.
- Next: recheck cross-links from Guidance claims to CRA requirements, IF matrix and SEC matrix; then independently revalidate M/606 C(2026) 7861 and its Annex/ESO adoption and OJ citation status.

## Guidance–matrix 양방향 링크 검증 완료 — 2026-11-18
- 13 Guidance claims ↔ 35 requirements ↔ 15 interfaces ↔ 36 SEC controls를 프로그램으로 양방향 대조: 누락 링크 0, dangling claim ID 0.
- G-002의 IF-001–IF-013 범위 표기를 machine-readable 개별 ID 목록으로 확장.
- G-005 ↔ IF-015 reverse link 추가: remote diagnostics/management의 interface/dependency 변경이 substantial-modification 평가에 관련될 수 있음.
- 요구사항/IF/SEC matrix의 Commission Guidance source URL에 EUR-Lex OJ C/2026/6013 ELI를 primary로 추가하고 기존 Commission page URL은 보조/게시 이력으로 보존.
- 상세 결과: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md` 최신 섹션.
- 다음 최우선: M/606 C(2026) 7861 Annex 원문 provenance, ESO adoption dates, OJ harmonised-standard citation status 독립 검증.

### 교차 매트릭스 검증 자동화 강화 — 2026-11-18
- `cra_traceability.py`에 claim register ↔ requirements/interfaces/SEC 양방향 foreign-key 검증 추가.
- 존재하지 않는 related IDs, matrix의 dangling Guidance claim IDs, reverse link 누락을 CI에서 fail-closed 처리.
- 회귀 테스트 3개 추가: reverse link 누락, dangling matrix claim, unknown related interface ID.
- G-002의 IF range를 명시적 ID로 확장했고 G-005↔IF-015를 양방향 연결.
- 최신 변경은 exact-head CI 통과 후에만 병합한다.

### PR #54 exact-head CI result — Run #865
- Tested head `1d5ae716cc6683365f4da6236d15bb9b32be1e52`; Run #865 / ID `44207426703`: success.
- 161 passed, 1 xfailed; exact source blob identity, compile, CRA traceability (including bidirectional link checks), full pytest, three-PDF live canary, artifact upload and official HTML canary all passed.
- OJ C/2026/6013 primary PDF fallback=False, SHA-256 unchanged.
- Artifact #14383728315; digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`; expires 2026-11-25 00:23:53 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-claim-redline-2026-11-18` was identical to main at base `d92f14f6c275bf6b3fa0c8243ac696dca0358d50`.
- Status/project log metadata appended after Run #865; final head needs a fresh exact-head CI before merge.

## PR #54 병합 완료 및 사후 안전 확인 — 2026-11-18
- PR #54 squash merge: `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Exact-head Run #868 (ID `44207582798`) success; tested head `38fa6ef6b6cb08391a227aff7f7a795a98e3f2b4`; 161 passed, 1 xfailed; source integrity, compile, bidirectional traceability, complete pytest, PDF/HTML canaries all passed.
- Artifact #14383788351; digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`; expires 2026-11-25 00:25:03 UTC.
- Pre-merge safety ref `safety/pre-merge-cra-guidance-claim-redline-2026-11-18` matched main before merge; main is now exactly one PR #54 commit ahead.
- Post-merge safety ref `safety/post-merge-cra-guidance-claim-redline-2026-11-18` is identical to main at `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Guidance claim redline G-001–G-013 and bidirectional link validator are now in main.
- Next priority: M/606 C(2026) 7861 Annex provenance, ESO adoption dates and OJ harmonised-standard citation status.

## PR #56 M/606 Annex + ESO status checkpoint — 2026-11-18
- PR #56 merged to main: `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- Exact-head Run #879 (ID `44209828986`) on `3e455c63013b895bce977ac1734b0e939827418b`: success; 161 passed, 1 xfailed; source integrity, compile, bidirectional CRA traceability, full pytest, official PDF canary and live official-source canary passed.
- Evidence artifact #14384958566; digest `sha256:84f27e218042e278bbea0157b68f7251f17c2752bda227972c67c890959a8188`; expires 2026-11-25 00:41:24 UTC.
- Pre-merge safety ref `safety/pre-merge-m606-annex-eso-2026-11-18` matched main at base `adc22e3087009db51acff53ec29054f971fa508a`; post-merge safety ref `safety/post-merge-m606-annex-eso-2026-11-18` is identical to main at `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- M/606 item 18 deadline cell corrected to printed EN 2; row description continues EN 3. All 41 item locators are row-specific.
- June 2026 ESO report is image-based (3 text-layer chars) and intentionally excluded from text-layer CI; no weakened validation threshold.
- Next: independently verify standards-stage changes after the June ESO snapshot and refresh Commission OJ harmonised-standard index before any presumption-of-conformity statement.
 

## 최신 ETSI M/606 작업계획 확인 — 2026-11-18
- 최신 확인 자료: ETSI Work Item Plan, M/606 활성 work items, 2026-11-17 표시 / Work Programme v2.3.3 / 18 items. 상세 원문 대조: [ETSI M/606 live status audit](reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md).
- 서보 드라이브와 잠재적으로 직접 관련되는 EN 304 636(방화벽/IDS/IPS) 및 EN 304 625(물리·가상 네트워크 인터페이스)의 상태/목표 일정을 별도 기록했다. 두 항목의 ETSI OJ Publication 날짜는 목표 일정이지 실제 OJ 게재 증거가 아니다.
- EN 304 636: Comments categorisation assessed (2026-10-06); adoption 목표 2027-02-11, publication 목표 2027-02-19, OJ publication 목표 2027-05-15.
- EN 304 625: 7 VR – EC assessment before EV received (2026-09-28); adoption 목표 2027-03-08, publication 목표 2027-03-15, OJ publication 목표 2027-06-23.
- 제품 자체가 방화벽/IDS/IPS 또는 네트워크 인터페이스 제품인지 intended purpose/core functionality 기준으로 판정한다. 드라이브의 Ethernet/fieldbus 포트 또는 내장 필터링만으로 제품 카테고리를 확정하지 않는다.
- Commission harmonised standards index(2026-11-18 조회)는 OJ 참조 목록을 제공하며 CRA 전용 카테고리는 보이지 않았다. 결론은 “현재 조회 범위에서 CRA OJ 참조를 식별하지 못함”으로 제한한다. Article 27 추정 적합성은 정확한 OJ 참조·범위 확인 후에만 주장한다.
- ETSI 18개 활성 항목은 M/606 41개 전체가 아니다. CEN/CENELEC 작업과 분리 추적한다. 6월 STAN4CR 공동 보고서를 ETSI 개별 item의 최신 자료로 취급하지 않도록 갱신했다.
- 다음: CEN/CENELEC의 수평 표준(EN 40000 계열) 및 산업용 OT 작업(prEN 50770 계열) 최신 공식 진행 상태를 독립 확인하고, OJ index/EUR-Lex를 재조회한다.


## PR #57 관리 문서 병합 확인 — 2026-11-18
- PR #57 docs-only merge commit: `ff3c5b7875131ef92e3fe4a7974f4420ddfcc84c`.
- Post-merge safety ref `safety/post-merge-pr57-2026-11-18`는 merge commit에서 생성되었고 main과 identical(0 ahead/0 behind)로 확인되었다.
- PR #57은 관리 문서만 변경했으며 해당 커밋에 연결된 PR CI run은 확인되지 않았다. 따라서 CI 통과로 표현하지 않는다. 이번 ETSI 연구 변경은 별도 feature branch에서 exact-head CI를 실행한다.


## PR #58 ETSI M/606 상태 갱신 병합 완료 — 2026-11-18
- PR #58 squash merge commit: `88d5eacd71c4267f64f674f0e990a25ed6fafd3a`.
- Exact-head CI Run #883 / ID `44210773892`, tested head `da1b0dce8460b84ddae5d58bd744d382d4b07e7d`: success; **161 passed, 1 xfailed**. Source blob identity, compile, CRA traceability, full pytest, three official CRA PDF fetch/hash checks, evidence upload and nine-source official HTML canary passed.
- Evidence artifact #14385358813; digest `sha256:407da234ac5ad37821bd5d00b7e0872f8abddc28932b1db9f32a14b76aacf1d4`; expires 2026-11-25 00:48:28 UTC.
- Pre-merge safety ref `safety/pre-merge-etsi-m606-status-2026-11-18` matched main at base `ff3c5b7875131ef92e3fe4a7974f4420ddfcc84c`; post-merge ref `safety/post-merge-pr58-2026-11-18` is identical to main at merge commit.
- Latest ETSI Work Programme v2.3.3 (2026-11-17) status and bounded OJ index finding are in `reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md`.
- Next: independently validate CEN/CENELEC EN 40000 horizontal standards and industrial OT prEN 50770 work. Treat third-party catalog status as secondary until official CEN/CENELEC records or published EN texts are obtained.


## CEN/CENELEC 공식 EN 40000 및 OT prEN 50770 점검 — 2026-11-18
- 중요 정정: CEN 공식 프로젝트 레코드에서 **EN 40000-1-1:2026은 Published**로 확인됐다. DOR 2026-11-02, DAV 2026-11-18, DOA 2027-02-28, DOP/DOW 2027-05-31. 같은 레코드의 CRA OJ 필드는 **No citation expected**다. 따라서 “CRA 표준은 아직 발행되지 않았다”는 포괄적 표현을 쓰지 않는다. “CEN 발행은 완료됐으나 CRA OJ 인용은 예상되지 않는다”가 정확하다.
- EN 40000-1-2:2026은 DOR 2026-11-02 / publishing 상태 및 No citation expected가 tracker·2차 카탈로그에서 확인됐다. 공식 개별 CEN 레코드 링크는 HTTP 500으로 본문 readback에 실패했으므로 원문 직접 확인 미완료로 남긴다.
- FprEN 40000-1-3:2026은 CEN 공식 레코드 Under Approval / Citation expected. prEN 40000-1-4는 Work item/drafting.
- CENELEC 공식 레코드에서 prEN 50770-1~6은 모두 Committee stage, OJ citation expected. 각 scope는 OT firewall/IDS-IPS, network management, physical/virtual network interfaces, VPN, routers/modems/switches, SIEM. 아직 DOR/DAV가 없어 발행된 표준이 아니다.
- OJ citation expected는 실제 OJ 인용이 아니다. 2026-11-18 Commission harmonised standards index 확인 범위에서 CRA OJ citation은 식별되지 않았다. Article 27 추정 적합성은 실제 OJ citation과 scope를 확인하기 전 주장하지 않는다.
- 서보 드라이브는 제품 intended purpose/core functionality 기준으로 분류한다. Ethernet/fieldbus 포트 또는 내장 필터링만으로 network-interface/firewall 제품으로 분류하지 않는다. 제품 모델/BOM/데이터시트 미확보로 drive-level classification은 Unknown.
- 상세: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md`; 구조화 추적표: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.csv`.
- 다음: EN 40000-1-1 발행본 및 EN 40000-1-2 원문 확보/검증, 50770-1~6의 최신 committee status 재확인, OJ index 재조회.


## PR #60 CEN/CENELEC 상태 정정 병합 완료 — 2026-11-18
- PR #60 merge commit: `1f39cb31d7f5e3466f1b22b798e9fc51971542da`.
- Exact-head CI Run #887 / ID `44214446339`, tested head `1707d49cdc7d24d5f3de43606e4bc31451e9bf8f`: success; **161 passed, 1 xfailed**. Source blob identity, compile, CRA traceability, full pytest, three official Commission PDF fetch/hash checks, evidence upload and nine-source official HTML canary passed.
- Artifact #14386734709; digest `sha256:aa960c3ecc5e9e89a2f64fc038ccc92cb77a9b7180e58eb5788152752ccd949c`; expires 2026-11-25 01:16:15 UTC.
- Pre-merge safety ref `safety/pre-merge-cen-ot-status-2026-11-18` matched base main; post-merge `safety/post-merge-pr60-2026-11-18` is identical to main at merge commit.
- Corrected key fact: EN 40000-1-1:2026 is CEN Published (DAV 2026-11-18) but CEN says no CRA OJ citation expected. This does not create Article 27 presumption.
- Detailed report/CSV: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md/.csv`.
- Next: obtain/inspect EN 40000-1-1 and 1-2 final texts, retry CEN 1-2 official record, and refresh CENELEC OT project stages/OJ index.



## 최신 작업 — CRA 요구사항–증거 추적 매트릭스 (2026-11-18)
- 작업 브랜치: `cra/requirements-to-evidence-matrix-2026-11-18`; 기준 main: `e461c6246a90f3a6035ba2044da800ba349352f7`.
- 신규 산출물: `reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md` 및 동반 CSV.
- CRA 법적 근거와 제품별 통제·시험·최소 증거를 16개 EVD 항목으로 연결했다. 범위는 제품 경계, 위험평가, 자산/공격면, 보안 설계, 접근통제, 통신, 입력 무결성, 업데이트, SBOM, 취약점 처리, 공개, 지원기간, 기술문서, 신고, 공급망/변경관리다.
- EN 40000-1-2는 공개 scope만 사용하고 final text/clause 확인 전 normative clause mapping을 하지 않았다. EN 40000-1-3은 Under Approval scope만 참고한다. EN 40000-1-1 Published는 용어 정합성에만 활용한다.
- 제품별 모델/설계/시험 자료가 없으므로 16개 행은 모두 Unknown / evidence pending. 이 표는 적합성 판정 또는 법률 의견이 아니다.
- 다음: CSV/보고서 정합성 검증 및 기존 CRA traceability validator/CI 범위 확인 후 exact-head CI, PR, merge 안전절차 수행.

### PR #62 1차 exact-head CI 결과 — metadata 반영 후 재검증 필요
- PR #62 head `360e83bba86a01bc83731ecd5ea5d0a6b975a8f6`, Run #891 / ID `44217500114`: success.
- pytest **161 passed, 1 xfailed**; source blob integrity, compile, CRA cross-matrix traceability, official CRA PDF 3종 fetch/hash, 9-source live official HTML canary 모두 성공.
- Artifact #14388303196; digest `sha256:47528b6e72af65dd95130a86a1442ac8f795a6eb3c34d93656369bf94734a2c2`; expiry 2026-11-25 01:40:17 UTC.
- 이 CI 결과를 상황판/세션 로그/프로젝트 로그에 추가했으므로 해당 metadata 변경이 포함된 새 PR head에서 exact-head CI를 다시 실행한 뒤 병합한다.


## PR #62 병합 및 복구 검증 완료 — 2026-11-18
- PR #62: https://github.com/useformotor3/ai-discord-bot/pull/62 — squash merged.
- Merge commit / 현재 main 기준: `612285ed720310cebd82340dc2e3b150e2c6f80a`.
- 최종 exact-head `3947e25ba1717caea3e4099404da800ba349352f7`의 Run #896 / ID `44217724257`: success; **161 passed, 1 xfailed**.
- 검증: source blob identity, compile, CRA cross-matrix traceability(13 claims/15 interfaces/35 requirements/36 SEC/41 M/606 items), full pytest, Commission 공식 PDF 3종 fetch/hash, 9-source official HTML canary.
- Artifact #14389685192; digest `sha256:e11bcbf277f32b7386e72fb063fdfac2b19e896473e30c8e775522b7f6c55d85`; expiry 2026-11-25 01:41:53 UTC.
- Pre-merge safety ref: `safety/pre-cra-evidence-matrix-2026-11-18`; post-merge safety ref: `safety/post-merge-pr62-2026-11-18`. Post-merge ref와 main은 0 ahead / 0 behind, identical 확인.
- 신규 EVD-01–EVD-16 보고서/CSV 및 통합 보고서·README·상황판·마스터 계획·세션 로그·JSONL 기록이 main에 반영됨.
- 운영 코드/workflow, secrets, state/history/archive, Gemini/Discord 실행 및 SIL 3 자료는 변경하지 않았다.
- 다음: 제품 P0 자료(정확한 모델 데이터시트·사용설명서·통신/원격접속 구조) 확보 후 EVD-01부터 모델별 evidence mapping. 표준 최종 전문 취득 시 clause-by-clause 검증.


## 신규 규제 일정 변경 — Commission C(2026) 7861 final (2026-11-18)
- Commission CRA 표준화 공식 페이지는 2026-11-10 M/606 개정을 확인한다(페이지 최종 업데이트 2026-11-12).
- 새 Annex I ESO adoption deadline: item 1 framework/risk-based design (EN 40000-1-2 work) **2026-11-30**; item 15 vulnerability handling (EN 40000-1-3 work) **2026-11-30**; items 2–14 generic security requirements **2027-10-30**; items 16–41 vertical product standards **2027-01-31**.
- 날짜는 ESO adoption deadline이지 발행일/OJ citation/CRA 적용일이 아니다. OJ citation 전 Article 27 presumption을 주장하지 않는다.
- 결정 Article 2는 ESO가 수령 후 1개월 이내 개정 비수락을 통지하면 결정이 중단되는 조건을 둔다. ESO 수령일/비수락 여부는 미확인 후속 항목이다.
- 상세 보고서: `reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md`. CEN/OT 상태 보고서에도 일정 정정 추가.
- 기존 자료의 2026-10-30 수평/수직 deadline 설명은 개정 결정으로 superseded. 이전 역사 기록은 삭제하지 않고 정정 링크를 추가한다.


### PR #64 exact-head CI 검증
- PR #64 head `ff548d64b109e95c9f63fa0666ba419f9545e11f`, Run #900 / ID `44219718958`: success.
- pytest **161 passed, 1 xfailed**; source blob integrity, compile, CRA cross-matrix traceability, official CRA PDF source canary 9종, artifact upload, official HTML source canary 모두 통과.
- CRA traceability: 13 claims, 15 interfaces, 35 requirements, 36 SEC, 41 M/606 items; bidirectional links true.
- Artifact #14390620457; digest `sha256:b7ced7629ab9e88bf44190d6d4f5fd50fc91f45bfc33a83ae09a02c1833e2f20`; expires 2026-11-25 01:58:08 UTC.
- CI metadata를 이 문서에 기록했으므로 변경된 최종 head에서 exact-head CI를 재실행한 후 병합한다.


## PR #64 병합 및 사후 안전 검증 — 2026-11-18
- PR #64 `docs: update CRA M606 deadlines from C(2026) 7861` squash merge 완료: `41229486baded6336aa43cd3b5de375476fe92f3`.
- 최종 exact-head `ae896286ee63916679afa4c6cc44655f1c125a4f`, Run #905 / ID `44219914781`: success; **161 passed, 1 xfailed**.
- Source blob identity, compile, CRA cross-matrix traceability, 공식 CRA PDF/HTML read-only canary 통과. Traceability: 13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items, bidirectional links true.
- 공식 PDF canary에서 C(2026)7861 Annex 사본: 6 pages, SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276` 확인.
- Artifact #14388899741, SHA-256 `ecd0f1181457270eb5d3d9fd5e60c2271aafc730ac1250a025499aa614f5cb8b`, expires 2026-11-25 02:00:03 UTC.
- Pre-merge safety ref `safety/pre-m606-amendment-2026-11-18`; post-merge `safety/post-merge-pr64-2026-11-18`와 main identical (0 ahead / 0 behind).
- 다음: Article 2 비수락 조건의 ESO receipt/notice 확인은 계속 열어둔다. 제품 모델별 P0 evidence intake checklist 및 CRA applicability/classification decision matrix 작성.

## CRA 제품 적용성·분류 및 P0 intake 기준 초안
- `reports/CRA_SERVO_DRIVE_APPLICABILITY_CLASSIFICATION_AND_P0_INTAKE_2026-11-18.md` 추가.
- CRA Article 2 적용성, Article 3 제품/원격 데이터 처리 정의, Annex III/IV 및 Implementing Regulation (EU) 2025/2392 core functionality 기준을 분리해 정리.
- 포트/통신 기능만으로 Annex III Class I/II 또는 Annex IV 분류를 자동 결론내리지 않도록 경계 판단표를 포함.
- 모델별 증거 미제공이므로 CRA 적용성/분류/EVD-01~16은 Unknown 유지. 데이터시트·매뉴얼·블록도·통신/원격접속 구성도 등을 P0 intake로 정의.
- 다음: 문서·CSV·요구사항 추적성 CI 검증 및 PR merge. Article 2 M/606 ESO 비수락 조건은 별도 열린 조사 항목.


## PR #65/#66 병합 및 제품 분류 법령 재대조 — 2026-11-18
- PR #65 병합 커밋 `d1f96fa6bba297e31ed47ae1b96f59421c55b774`; exact-head Run #908 / ID `44221151662`: 161 passed, 1 xfailed; CRA traceability 13/15/35/36/41, bidirectional links true; JSONL event log 133 events. Artifact #14391145990, digest `sha256:f2a2f83b19d0488c874a032e83a41fcc4140dde1817d2a9c2fc171fdbd0b6c0f`, expires 2026-11-25 02:09:41 UTC. Post-merge safety `safety/post-merge-pr65-2026-11-18` identical to main.
- PR #66 병합 커밋 `9cb62579e4f45ebf57587cc19644c370cbe80ebb`; exact-head Run #910 / ID `44221522135`: 161 passed, 1 xfailed; source integrity, compile, CRA traceability 13 claims/15 interfaces/35 requirements/36 SEC/41 M606 items, bidirectional links true, PDF/HTML canaries passed. Artifact #14391145990, digest `sha256:f2a2f83b19d0488c874a032e83a41fcc4140dde1817d2a9c2fc171fdbd0b6c0f`, expires 2026-11-25 02:09:41 UTC. Post-merge safety `safety/post-merge-pr66-2026-11-18` identical to main.
- EUR-Lex 2025/2392 공식 OJ 본문 재대조: recital (2)–(6), Annex I의 #10 interface/#11 OS/#12 router-switch 기술 설명 및 Article 8(1) critical product 인증 절차를 보고서에 보완. Annex IV 카테고리 해당과 인증 의무 자동 발생을 구분.
- 다음: M/606 Article 2의 ESO 수령일/비수락 사실은 공개 확인 자료를 계속 찾되 미확인 상태 유지. P0 모델 자료가 오면 제품 경계·intended purpose·연결성·core functionality부터 검증.


## PR #67 병합 및 exact-head 검증 — 2026-11-18
- PR #67 `docs: record PR65 PR66 and CRA legal recheck` squash merge: `86af2db5fadf5098b22b39d2d6c07710ed0033ee`.
- Exact-head `58e2dc8608fc097dad87fa3ec614cb108d184fad`, CI Run #912 / ID `44223114411`: success. Source blob identity, compile, CRA cross-matrix traceability, 전체 pytest, 공식 CRA PDF/HTML read-only canaries 및 artifact upload 단계 모두 성공.
- Artifact #14391457563, digest `sha256:f172ed1762a693f626e8c5781638c557e9d5471d6750b5315a54cae9398d919c`, expires 2026-11-25 02:25:41 UTC.
- Post-merge safety ref `safety/post-merge-pr67-2026-11-18`와 main identical (0 ahead/0 behind).
- 다음: C(2026)7861 Article 2 ESO receipt/non-acceptance 공개 증거 확인 계속. 현 시점 receipt/notice 원문 확인 불가이므로 acceptance를 추정하지 않는다.


## M/606 수락 상태 추가 검증 — 2026-11-18
- CEN-CENELEC 공식 발표(2025-05-01)는 원래 M/606이 2025-04-03 CEN, CENELEC, ETSI에 의해 수락되었음을 명시. Commission Interoperable Europe 2026 rolling plan도 세 ESO가 요청을 수락했고 작업 중이라고 재확인.
- 단, 원래 요청 수락은 2026-11-10 개정 결정 C(2026)7861 Article 2의 개정 통지/수령 및 1개월 비수락 조건 충족을 증명하지 않는다. 개정 결정의 개별 수령일·비수락 통지는 미확인으로 유지.
- M/606 보고서에 원래 요청과 개정 결정의 수락 상태를 분리 기록. 공개 증거 없는 개정 수락을 추정하지 않는다.


## PR #69 병합 및 M/606 수락 상태 분리 검증 — 2026-11-18
- PR #69 merge `8089cb96fdeba390dafe6991b19abfa1bc5b3e25`.
- Exact-head `d60eb20100e682fe13ba0c5fac3f9724d9add842`, Run #916 / ID `44223566124`: success; source integrity, compile, CRA traceability, full test suite, official CRA PDF/HTML canaries passed.
- Artifact #14391159512, digest `sha256:a71b8d12c9c1bb627da1b8d771ed2fda04ea179a721a1c55add3d5e28e16a1da`, expires 2026-11-25 02:29:24 UTC.
- Post-merge safety ref `safety/post-merge-pr69-2026-11-18` == main (0 ahead/0 behind).
- Regulatory fact distinction: original M/606 accepted by CEN/CENELEC/ETSI on 2025-04-03 (official CEN-CENELEC announcement); C(2026)7861 amendment-specific Article 2 notification/receipt and non-acceptance status remain unconfirmed.


## PR #70 병합 및 사후 검증 — 2026-11-18
- PR #70 `docs: record PR69 merge and M606 status verification` squash merge: `ca65475db4ca53d23ee55308c9c9616a054ea756`.
- PR #70 exact head `b5fb2adc3eeba9d9839ff3d3519b128743cc6878`, Run #918 / ID `44223777837`: success; source blob identity, compile, CRA cross-matrix traceability, full pytest (**161 passed, 1 xfailed**), official CRA PDF/HTML canaries passed.
- Traceability: 13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items; bidirectional links true; JSONL 138 events (133 modern IDs, 5 legacy IDs).
- Artifact #14391727520, SHA-256 `f737a27f61f2b6cd153731941c9e615e4379912d03ccfc3696f0eea7b2ad0d09`, expires 2026-11-25 02:31:30 UTC.
- Pre-merge safety ref `safety/pre-pr70-merge-checkpoint-2026-11-18`; post-merge `safety/post-merge-pr70-2026-11-18` identical to main at merge SHA.
- PR #70 scope: documentation/log synchronization only; no runtime/workflow/secrets/state/history/archive or SIL 3 files changed.
- Post-merge exact-main CI Run #919 / ID `44228633470` on merge SHA `ca65475db4ca53d23ee55308c9c9616a054ea756`: **success**; 161 passed, 1 xfailed; source integrity, compile, CRA traceability, 9 official sources canary, corrigenda validation and Article 13(8) locator/quote canary passed. Artifact #14393668052, SHA-256 `3d6314562d9ac4f34d645ef3191be6e499ae2d25e829968e17658717bdf2ae22`, expires 2026-11-25 03:11:50 UTC.


## 2026-11-19 재개 — Annex III/IV core-functionality 감사 작업
- 재개 기준 main: PR #88 merge 16cdec76def2e8920d8fc2ca3b6a43e497d41d83; PR #88 사후 exact-main Run #957 success, 162 passed / 0 xfailed.
- 현재 작업 브랜치: cra/applicability-core-functionality-audit-2026-11-19 (PR 생성/CI 대기 전 단계). 기준 main은 변경하지 않았다.
- EUR-Lex 공식 Regulation (EU) 2024/2847 및 Commission Implementing Regulation (EU) 2025/2392의 recital (2)–(6), Annex I/II 기술 설명을 재대조했다.
- Annex III/IV 분류는 제품 전체의 core functionality로 판단하며, 통합 구성요소만으로 완제품 카테고리를 자동 확정하지 않는다. Annex III/IV 비해당과 CRA 비적용을 분리하고, 구성요소 보안은 완제품 위험평가에 계속 반영한다.
- 기존 제품 분류/intake 보고서와 EVD 매트릭스에 제품 단위별 판정 게이트 및 증거 조건을 통합했다. 특정 제조사·모델·SKU 입력이 없어 개별 제품 결론은 계속 Unknown / Not assessed.
- PR #88/Run #957는 직전 검증 기준점이며, 이번 변경은 아직 PR exact-head CI 및 main 병합 전이다. CI·병합·사후 검증 결과는 확인 후에만 추가한다.


## 진행 중 작업 — EVD–CRA–SEC 교차 추적 (2026-11-19)
- 작업 브랜치: `cra/evd-sec-crosswalk-2026-11-19`, 기준 main `732f5167ed1a272afc10bb66d4aceb68ccb96b79`.
- 신규 CSV: `reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv` — EVD-01~16을 CRA 요구사항 및 SEC 통제에 연결하는 후보 매핑. 각 행에 근거 설명과 제품별 적용성 한계를 기록.
- validator에 16개 EVD 전체, CRA/SEC 외래키, SEC-001~036 전체 연결, 중복/누락 및 근거/상태 필드 검증을 추가. Negative tests: unknown SEC reference, missing EVD row.
- PR/CI 전 상태. 제품별 적용성·구현·시험 Pass는 주장하지 않는다.


## PR #91 — EVD–CRA–SEC 추적 자동화 완료 (2026-11-19)
- 신규 `reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv`: EVD-01~16 ↔ CRA 요구사항 ↔ SEC-001~036 후보 연결. SEC-008/014/036 누락을 CI에서 발견해 보완했다.
- `cra_traceability.py`는 EVD 16행, CRA/SEC foreign keys, SEC 전체 커버리지, 중복/누락, rationale/applicability 필드를 fail-closed로 검사한다.
- Negative regression tests는 unknown SEC ID, missing EVD row, orphaned SEC control을 검증한다. Full suite: 166 passed / 0 failed.
- PR #91 exact-head Run #971 success; exact-main Run #972 success. 제품별 적용성/구현/시험 Pass는 여전히 Unknown.


## 제품별 증거 register — PR #94 병합 완료 (2026-11-19)
- reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv가 main에 반영됨. E-001~E-015를 EVD-01~16과 연결.
- validator는 15개 Evidence ID, EVD foreign keys, variant별 provenance, SHA-256, locator, reviewer/date, cross-check, accepted/rejected/not-applicable rationale gates를 검사.
- Negative regression tests: provenance 없는 accepted, unknown EVD, rationale 없는 not-applicable, invalid SHA-256, not_provided partial metadata.
- 모든 제품별 항목은 여전히 not_provided. 제품별 적합성·구현·시험 Pass는 주장하지 않는다.


## 2026-11-19 추가 진행 — Commission guidance / M/606 개정 / LS 매뉴얼 재확인
- 작업 기준 main: `d314a9c07ad336497948ae0d049d700d8e88b1e2`; safety ref `safety/pre-cra-guidance-m606-update-2026-11-19`, 작업 브랜치 `cra/commission-guidance-m606-update-2026-11-19`.
- Commission CRA guidance C(2026) 6013의 공식 랜딩 페이지를 검토했다. 적용 범위(RDPS/FOSS 포함), substantial modification, support period, reporting 및 risk assessment를 다루는 비구속적 실무 지침이며, 67개 사례를 포함한다.
- Commission CRA standardisation page(최종 업데이트 2026-11-12)는 M/606이 2026-11-10 개정되었고 일부 수평 표준 및 모든 수직 표준 제출 기한이 3개월 연장됐음을 명시한다. 표준 제출 일정과 CRA 적용일, OJ 조화표준 인용, Article 27 적합성 추정을 구분한다.
- LS메카피온 공식 매뉴얼 메타데이터 재확인: iX700M Ver1.4 첨부파일명 260915, iX7M Ver1.3 파일명 260605, iX7NH Ver1.7 파일명 260605. 첨부파일 다운로드 엔드포인트는 “잘못된 접근”을 반환했으므로 PDF 본문 확보·SHA-256·페이지 검토는 미완료.
- LS메카피온 보고서 v0.2에 최신 지침·M/606 개정 및 매뉴얼 수집 한계를 반영한다. 제품별 증거 상태는 승격하지 않는다.
- 현재 CRA 법령 전수 조사, 41개 표준/OJ 상태별 검증, ENISA 최신 자료, 제품별 매뉴얼 PDF 원본 검토는 미완료. 제품별 scope/classification/conformity Unknown, 시험 Not Run.


## 2026-11-19 — PR #106 병합 및 ENISA/위임규정 추가 감사
- PR #106 병합 SHA: 2c24b16ede905009f2a2f07edb4072bb9c244316; post-merge safety ref safety/post-merge-pr106-2026-11-19 생성.
- PR #106 exact-head Run #1008 / ID 44489742051: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML source 10개 수집·canary 통과, provenance manifest JSON parse + object round-trip 통과. Artifact #14511852597, SHA-256 a34bd69a01bfe18f4967c1982e7ade0e959d0e9ae6f7740cfc9e94b5c566304a, 2,565 bytes, expires 2026-11-26 08:42:02 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 PDF endpoint empty body로 SKIPPED. PDF artifact 없음. 정확한 main push CI는 별도 확인 전이므로 성공으로 기록하지 않는다.
- 보고서 v0.3 추가 조사: Delegated Regulation (EU) 2025/1535의 L-category 차량 범위 제외(페달 보조 L1e 예외), Delegated Regulation (EU) 2026/881의 CSIRT 신고 전파 지연 조건, ENISA SME maturity model, Secure by Design playbook, SBOM advisory, secure update advisory, CRA Single Reporting Platform을 설명한다.
- ENISA 실무자료는 비구속 참고자료이며 조화표준/OJ 인용이나 Article 27 presumption을 대체하지 않는다.
- 제품별 scope/classification/conformity Unknown, 보안 시험 Not Run. 법령·표준 전수 감사는 미완료.


## 2026-11-19 — PR #107 병합 및 Machinery Regulation 상호작용 분석
- PR #107 merge SHA: 0682d83f891a20438d6d37eb231c3b20ca72c67e; post-merge safety ref safety/post-merge-pr107-2026-11-19 생성.
- PR #107 exact-head Run #1010 / ID 44490148586: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON provenance manifest parse/round-trip 통과. Artifact #14511858034, SHA-256 dd4305ae872aec9cf208228f8924ed06a2cf2a2c3b9cabd7b063babbe3c2c69e, 2,566 bytes, expires 2026-11-26 08:45:00 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 endpoint empty body로 SKIPPED; PDF artifact 없음.
- Exact-main push CI는 독립 확인 전이므로 미확인. Post-merge safety ref는 main merge SHA에서 생성됨.
- Commission CRA FAQ(2026-09-04)와 Regulation (EU) 2023/1230을 확인했다. FAQ는 CRA와 Machinery Regulation이 함께 적용되는 제품은 두 규정의 요구사항 및 적합성 평가 절차를 각각 검토해야 하며, CRA 적합성이 MR 적합성을 자동 대체하지 않는다고 설명한다.
- Machinery Regulation Annex III 1.1.9/1.2.1의 corruption protection 및 control-system security 내용을 보고서 v0.4에 반영했다. 적용일 2027-01-20.
- 제품별 공급 경계·EU 공급·무선 variant·기계/부분완성기계 지위가 미확인이라 적용성/책임분담은 Unknown. 제품별 보안 시험 Not Run.


## 2026-11-19 — PR #108 병합 및 CRA 표준화 작업계획 확장
- PR #108 merge SHA: 4a1b44501dec629ae2f42106d6b8d200f177765a; post-merge safety ref safety/post-merge-pr108-2026-11-19 생성.
- PR #108 exact-head Run #1012 / ID 44490507909: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON manifest round-trip 통과. Artifact #14512183573, SHA-256 8e3b3883bc2b3b3f0c9c0d002efb2d794e1610883f186ccab16ebb0eb8f51c05, 2,567 bytes, expires 2026-11-26 08:47:23 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED. PDF artifact 없음.
- Exact-main push CI는 독립 확인 전이므로 미확인.
- Commission Notice C/2026/1695 (OJ C, 19.3.2026)의 CRA standardisation Action 5를 확인했다. M/606을 보완해 Annex III/IV 밖 제품, 특히 기계류·철도·승강기·농업기계·AI·태양광 인버터 분야에 대한 추가 표준화 요청을 계획한다.
- 연간 작업계획은 표준화 방향이지 최종 표준이나 OJ 조화표준 인용이 아니다. CRA Article 27 presumption은 실제 OJ citation 확인 전 주장하지 않는다.
- 보고서 v0.5에서 M/606 41개 표준과 C/2026/1695 Action 5를 별도 감사 트랙으로 구분한다.


## 2026-11-19 — PR #109 병합 및 M/606 개정 Annex 원문 대조
- PR #109 merge SHA: 172caa7427dd7af412d555bf2a82660537c0e16f; post-merge safety ref safety/post-merge-pr109-2026-11-19 생성.
- PR #109 exact-head Run #1014 / ID 44490815716: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON provenance manifest parse/round-trip 통과. Artifact #14511964662, SHA-256 16f516e1bb84f2267327318d70994b1e77f7eb1029c5a40685763e67cc882dfe, 2,566 bytes, expires 2026-11-26 08:49:33 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 endpoint empty body로 SKIPPED; PDF artifact 없음. Exact-main push CI는 독립 확인 전이므로 미확인.
- Commission Implementing Decision C(2026) 7861 final Annex I 원문을 문서 등록소에서 직접 열어 41개 ESO 제출기한을 확인했다: item 1·15 = 2026-11-30, items 2–14 = 2027-10-30, items 16–41 = 2027-01-31.
- 기존 M/606 41행 CSV와 validator의 날짜 기대값이 원문과 일치함을 대조했다. 날짜 불일치 수정은 불필요.
- 보고서 v0.6은 제출기한이 제조자 CRA 준수기한이 아님을 강조하고, EtherCAT 포트·MCU/FPGA 존재가 Annex III/IV 제품분류를 자동 결정하지 않는다는 주의사항을 강화한다.
- 개별 표준 진행 상태·OJ citation 전수 감사는 미완료. 제품별 CRA 판정 Unknown, 시험 Not Run.


## 2026-11-19 — PR #110 병합 및 M/606 Annex 원문 검증 완료
- PR #110 merge SHA: 57c7734d59b5046598e67aefd5d74a2ea29d3e2b; post-merge safety ref safety/post-merge-pr110-2026-11-19 생성.
- PR #110 exact-head Run #1016 / ID 44491245339: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON manifest round-trip 통과. Artifact #14512063867, SHA-256 b2630ffa5f6d6cd71026faf31422e2365a836c51c50225c6ccdd51f2b1f55b09, 2,566 bytes, expires 2026-11-26 08:52:34 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED; PDF artifact 없음. Exact-main push CI는 독립 확인 전.
- 보고서 v0.7에서 ENISA SRP FAQ 2026-10-15, 플랫폼 v1.3(2026-11-04), AR User Manual v1.3을 반영한다.
- 신고 기한(24h/72h/AEV 14d/SI 1 month), Primary AR 1명·Secondary AR 최대 20명, EU Login/MFA, 영어 UI, 초기 API 미제공, 장애 대응, SRP v1.3 카운터 한계를 설명한다.
- SRP 72h 카운터는 현재 Early Warning 제출 이후 48h를 더하는 표시 로직으로 실제 인지시각 기준 기한보다 일찍 overdue 표시될 수 있다. AEV Final Report 카운터도 미구현. 화면 알림이 법정 기한을 변경하지 않으므로 내부 tracker를 유지해야 한다.
- 과거 출시 제품의 Article 14 신고, 통합 부품 취약점의 완제품/부품 제조자 신고 책임도 보고서에 추가했다.


## 2026-11-19 — PR #111 병합 및 최신 CRA 신고 운영자료 반영
- PR #111 merge SHA: 26e6cc348f0e4207fe04a4d789ace38b7434b8ea; post-merge safety ref safety/post-merge-pr111-2026-11-19 생성.
- PR #111 exact-head Run #1018 / ID 44491554033: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON manifest parse/round-trip 통과. Artifact #14512443373, SHA-256 6354a013d1753e4b67dae2fb87071b330f6b591097b8946ce7ec95f050e29dea, 2,566 bytes, expires 2026-11-26 08:54:31 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED. Exact-main push CI는 독립 확인 전.
- LS메카피온 보고서 최신 v0.7: CRA 법령·Commission 지침·M/606·기계류 규정·ENISA 자료·SRP v1.3 신고 운영을 통합한 제품군 예비 분석.
- 미완료 P0: 모델별 제조사 PDF 원본 다운로드·해시·페이지 검토, M/606 41개 개별 표준의 실제 개발 상태 및 CRA OJ 인용 전수 감사, C/2026/1695 Action 5 후속 표준화 요청 추적.
- 제품별 CRA scope/classification/conformity는 Unknown, 보안시험 Not Run. 보고서는 최종 적합성 평가서가 아니다.


## 2026-11-19 — PR #112 병합 및 LS 제품/도구/ESI 매핑
- PR #112 merge SHA: 4507bc5dc2a8c189073ab0728a2b271063c4bf5c; post-merge safety ref safety/post-merge-pr112-2026-11-19 생성.
- PR #112 exact-head Run #1020 / ID 44491849633: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON manifest parse/round-trip 통과. Artifact #14513316478, SHA-256 a57834f4e1cf07fb42be120cb50090badb86acb3e4a8626503d2ed7747afd5c4, 2,566 bytes, expires 2026-11-26 08:56:37 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED. Exact-main push CI는 독립 확인 전.
- 제조사 공개 자료 대조: DriveCM Ver1.03.2(2026-07-07 게시, 2026-08-11 파일 날짜) 지원 목록 및 EtherCAT ESI Ver0.98(2025-07-15) 11개 적용 모델 확인.
- iX700M, L7NHA/B, L7SA/B, GEM의 DriveCM 지원은 공개 게시물에서 명시되지 않거나 명칭 대응이 불명확하다. 지원하지 않는다고 단정하지 않고 Unknown으로 둔다.
- ESI v0.98의 적용 목록에 iX700M은 명시되지 않는다. 별도 ESI 제공 여부와 실제 모델/SKU 매핑 확인 필요.
- report v0.8은 13개 제품군별 연결 경로와 도구·ESI·업데이트 증거 공백을 표로 정리한다.
- 제조사 PDF·설치 파일·ESI XML 원본을 다운로드·해시·검토한 것은 아님. 제품별 CRA scope/classification/conformity Unknown, 시험 Not Run.


## 2026-11-19 — PR #113 병합 및 ESO M/606 진행보고서 검토
- PR #113 merge SHA: 5273e6da25862a8ad1e92b2473a11a63b0d8015f; post-merge safety ref safety/post-merge-pr113-2026-11-19 생성.
- PR #113 exact-head Run #1022 / ID 44492219721: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON provenance manifest parse/round-trip 통과. Artifact #14513586428, SHA-256 bc438c098ff591da5690070adcc417d3f440adcf4a6635df87b00b05ed9b7d95, 2,566 bytes, expires 2026-11-26 08:59:19 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED. Exact-main push CI는 독립 확인 전.
- STAN4CR/CEN-CENELEC/ETSI 공동 M/606 진행보고서 V2.0(2026-06-03)을 4페이지 전체 검토했다. 개별 M/606 표준의 2026-06-03 단계와 publication forecast, 산업용 OT/IACS 지원 deliverables(EN IEC 62443-4-1/-4-2/-3-3)를 보고서 v0.9에 반영.
- 2026-06-03 forecast는 2026-11-10 C(2026) 7861 Annex I 개정 이전의 과거 예측이므로 현재 제출기한으로 사용하지 않는다. C(2026) 7861 Annex I를 제출기한 기준으로 유지한다.
- IEC 62443 지원 deliverables는 M/606 41개 Annex I 표준 및 CRA OJ 조화표준 인용과 구분한다.


## 2026-11-19 — PR #114 병합 및 M/606/OT 표준화 진행 스냅샷
- PR #114 merge SHA: 88a3c3b29ecf7af2884e6df288075a0ce48f73f2; post-merge safety ref safety/post-merge-pr114-2026-11-19 생성.
- PR #114 exact-head Run #1024 / ID 44492644455: success, 174 passed / 0 failed. CRA traceability 13/15/35/36/16/15/41 통과.
- Live official CRA HTML 10-source canary 및 JSON manifest parse/round-trip 통과. Artifact #14514585121, SHA-256 bd7e0fe6244c8d9ad0bd312ec3e4016836bfc1c738a0a685a8d5c3696bc6a198, 2,566 bytes, expires 2026-11-26 09:02:15 UTC.
- PDF canary는 EUR-Lex C(2026) 6013 empty body로 SKIPPED. Exact-main push CI는 독립 확인 전.
- 보고서 v0.9는 STAN4CR/CEN-CENELEC/ETSI 공동 M/606 진행보고서 V2.0(2026-06-03)의 개별 표준 개발 단계와 OT/IACS 지원 deliverables(EN IEC 62443-4-1/-4-2/-3-3)를 추가했다.
- 2026-06-03 개발단계·publication forecast는 역사적 스냅샷이다. 현재 ESO 제출기한은 C(2026) 7861 Annex I 기준이며, 실제 2026-11-19 표준 상태·최종 발행·OJ citation은 미확인이다.
- 제품별 CRA scope/classification/conformity Unknown, 보안시험 Not Run. 제조사 PDF/ESI/설치파일 원본 확보·해시·페이지 검토 미완료.


## 2026-11-20 추가 진행 기록 (PR #126)
- PR #126 병합 완료: `9b61f1d9b177454c3530fa5339883e6434d01df3`; 정확한 PR head `8bea10c55e2158a1c22c880c025a6ec9662cf857`, Actions Run #1052 성공.
- 병합 전/후 복구 브랜치: `safety/pre-pr126-merge-sync-2026-11-20`, `safety/post-merge-pr126-2026-11-20`.
- main read-back: 핵심 6개 문서 재조회 완료.
- EN 40000-1-1/-1-2의 발행은 CEN-CENELEC 2026-11-19 공식 공지로 확인. OJ 참조 게시가 CRA 제27조 적합성 추정의 별도 전제임은 EC 공식 페이지 및 CRA 법령으로 확인.
- CEN 개별 카탈로그의 "citation expected" 필드는 직접 열람하지 못함. "No citation expected"는 현재 2차 추적자료에 근거한 잠정 판단으로 유지.
- M/606 41개 전수 표준별 OJ 감사는 계속 미완료. 제품별 CRA scope/classification/RDPS는 Unknown, security tests는 Not Run.


## 2026-11-20 추가 1차 출처 검증 완료
- CEN-CENELEC 공식 카탈로그 개별 레코드를 직접 열람했다. EN 40000-1-1:2026(JT013095) 및 EN 40000-1-2:2026(JT013089) 모두 Published, DOR 2026-11-02, DAV 2026-11-18이며 OJEU citation 필드는 **“No citation expected for Directive 2024/2847”**로 확인됐다.
- 공식 레코드: https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:82349,2307986 및 https://standards.cencenelec.eu/ords/f?p=CEN:110::::::FSP_PROJECT,FSP_ORG_ID:81335,2307986
- 따라서 두 EN은 발행 사실과 별개로 CRA 제27조 적합성 추정의 근거로 취급하지 않는다. §28.2의 이전 “직접 확인 미완료” 상태는 이 검증으로 종료.


## 2026-11-20 M/606 41개 항목 감사
- C(2026) 7861 final replacement Annex I 기준 항목번호·주제·ESO 채택기한 41/41 대조 완료.
- 기한: 1·15 = 2026-11-30 (2건); 2–14 = 2027-10-30 (13건); 16–41 = 2027-01-31 (26건). ESO 표준 채택기한이며 제조사 CRA 준수기한이 아님.
- Annex I에 각 항목의 최종 EN/ETSI 번호 및 OJ 인용번호가 없으므로 실제 표준번호 매핑과 OJ 상태는 별도 작업. 41개 모두의 OJ 상태를 확인한 것은 아님.
- C(2026) 7861 Article 2의 1개월 내 ESO 비수락 통지 조건이 있으므로 수락/거부 통지 원본을 추가 확인해야 함.
- 감사대장: reports/CRA_M606_41_ITEM_PRIMARY_SOURCE_AUDIT_2026-11-20.csv 및 .md.


## 최신 main 기준점 — PR #128 병합 및 사후 검증 (2026-11-20)

- PR #128 `docs(cra): audit all 41 M606 Annex I items against C(2026) 7861` 병합 완료. PR exact-head `25ad1721045d489d8d0ce2b8689511c7b5776e9d`; Run #1060 (`44656220445`) 성공.
- main merge SHA: `6733f37201117cb5744215d9deb337b0810acc49`; main branch 재조회로 동일 SHA 확인.
- 복구 기준점: `safety/pre-pr128-merge-2026-11-20` (기준 main `ec9823cd9d1831a3a1047743d43496db76524ce1`), `safety/post-merge-pr128-2026-11-20` (병합 SHA).
- 41개 Annex I 항목의 주제·기한 감사대장 및 보고서/README/계획/로그 반영 완료. main의 `PROJECT_LOG.jsonl`은 218줄이며 전 줄 JSON 파싱 통과.
- 병합 후 main push CI Run #1061 (`44657049974`) 성공. 전체 단계 완료.
- 후속 우선순위: CEN JT013090/prEN 40000-1-3 1차 카탈로그 레코드 및 Article 2 ESO 비수락 통지 확인. 실제 개별 EN/ETSI 매핑·OJ 상태 41개 전수검증은 미완료.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, 보안시험 Not Run. 제조사 매뉴얼 원본 PDF bytes 및 SHA-256 미확보.


## 2026-11-20 추가 1차 출처 확인 — M/606 수평표준 Work Item 연결

- PR #129 병합: `da3cbc4b68ba92b8512f08740c02eefc415a616e`; main push CI Run #1063 (`44657325405`) 전체 성공. PR #129의 Run #1062도 성공.
- CEN/CENELEC 공식 M/606 Work Programme V1 (2025-04-02)에서 Annex I item 1 → JT013089 (Principles for cyber resilience), items 2–14 → JT013091 (Generic Security Requirements), item 15 → JT013090 (Vulnerability Handling) 연결을 확인.
- CEN-CENELEC 공식 2026-02-23 CRA webinar는 JT013090을 prEN 40000-1-3 Vulnerability handling과 연결한다. CEN 공식 2026-11-19 발표는 FprEN 40000-1-3이 곧 공개될 예정이라고만 밝힌다.
- 따라서 item 1, items 2–14, item 15의 ESO work-item 연결은 1차 자료로 확인되어 감사대장에 반영. 단, JT013090의 최신 공식 카탈로그 세부 레코드(현 단계, 날짜, OJ citation 필드)는 직접 확보하지 못했다. Formal Vote 19 Nov 개시 및 OJ citation expected는 현재 2차 자료에서만 확인되므로 공식 확정으로 승격하지 않는다.
- Article 2는 개정 결정을 ESO가 수령한 날부터 1개월 이내 비수락 통지를 할 경우 결정이 중단된다고 규정한다. 수령일은 발송일(10 Nov)과 동일하다고 가정할 수 없으며, ESO별 수령일/통지 원본을 찾지 못했다. 따라서 정확한 종료일 또는 비수락 통지 부재를 확정하지 않는다. 결정 전문의 Recital (2)는 2025년 원 요청의 수락만 확인하며 2026년 개정의 수락 증거가 아니다.
- 41개 item의 Annex I 주제·기한 41/41 검증은 유지. Work Item 매핑을 item 1, 2–14, 15까지 15개 행에 연결했으나, 개별 EN/ETSI 문서의 최신 상태·OJ 인용 전수감사는 미완료.
- CRA Article 27 적합성 추정은 해당 표준 참조가 OJEU에 게시된 경우에만 발생한다. EN 40000-1-2는 CEN 카탈로그의 “No citation expected” 기록에 따라 presumption 근거로 사용하지 않는다. JT013090은 OJ 필드 미확인으로 presumption 미확정.
- PR #129 main push CI Run #1063 전체 단계 성공. 복구 기준점: `safety/pre-pr129-merge-2026-11-20` 및 `safety/post-merge-pr129-2026-11-20`.


## PR #130 병합 후 검증 (2026-11-20)
- PR #130 exact-head `accf11726771374f632bb66783ce0fefaf400daa`, Run #1064 (`44658682554`) success.
- Squash merge SHA `bfcc2e61fc07b2148fca7a162349af40aa84bc47`; main read-back 일치.
- 사전/사후 복구 ref: `safety/pre-pr130-merge-2026-11-20`, `safety/post-merge-pr130-2026-11-20`.
- main push CI Run #1065 (`44658780153`) success. Compile, full pytest, CRA traceability, official CRA source canaries and provenance upload all passed.
- main `PROJECT_LOG.jsonl` 221 records, 221 valid JSON; 41-item audit CSV has 41 data rows.
- 다음 조사: CEN M/606 Work Programme의 OT/IACS 관련 work items 20b,21b,22b,25b,27b,36b와 서보드라이브 기능 경계 비교. 제품기능 증거 없이 해당 vertical scope에 포함된다고 결론 내리지 않는다.

## 최신 main 기준점 — PR #174 병합 및 사후 검증 (2026-11-20)
- PR #174 `docs(status): record PR173 merge, CI and evidence boundaries` 병합 완료. exact head `779474728cb39501991dff7846b52a5bbae83ec4`, squash merge SHA `090c78bfa0edc759641a8dd30f9156038fa86a82`.
- PR #174 exact-head Actions Run #1150 / ID `44703086698`: success. 전체 pytest 174 passed / 0 failed, compile, source integrity, CRA traceability, 공식 HTML source canary 및 provenance manifest 생성/업로드 성공.
- 공식 CRA PDF canary의 별도 증거 업로드 단계는 skipped. HTML canary에서 allowlisted official sources 10건을 읽고 주요 Article 13(8), 2025/2392 Annex I(10)/Annex II(1) locator 확인. PDF 파일 원본 확보로 간주하지 않음.
- Provenance artifact #14613952433, 2,567 bytes, SHA-256 `84a6cab72e1403f205d03151a9259a8ac101244d95fafdd3e87b5c5fca05b718`.
- main read-back/compare 결과 main == merge SHA. 복구 기준점 `safety/pre-pr174-merge-2026-11-20` 및 `safety/post-merge-pr174-2026-11-20`; post ref는 merge SHA 기준.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, 보안시험 Not Run. iX7NH Ver1.7/API 공식 첨부 원본 bytes/SHA-256 미확보; AutomationDirect 가이드는 2차 자료로만 사용.

## 2026-11-20 최신 가이드북 목록 추가 감사
- 공식 LS메카피온 가이드북 인덱스에서 iX7NH 교육자료(2026-09-14), DriveCM V1.03.1 가이드 및 게인 튜닝 가이드(2026-09-08), PN8B+L7NH(iX7NH) CSV 동기제어 및 EtherCAT 0x211F 외부 IO 가이드(2026-07-06) 확인.
- 목록 메타데이터만 확인; 상세 첨부 파일명/크기/본문/SHA-256 미확보. 보고서 §42 및 인벤토리 GUIDEBOOK-INDEX-SERVO-2026-09 행에 반영.
- 공식 제품 목록은 iX7NH를 AC 100–120/200–240 V, 0.1–15 kW EtherCAT 드라이브로 표기. 이는 제품군 범위 참고이며 특정 SKU/CRA 분류 근거가 아님.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, 보안시험 Not Run 유지.

## PR #175 병합 및 사후 검증 (2026-11-20)
- PR #175 exact head `65f0a5f136e0a37797710f485dcdc478b9cf45b0`, Run #1152 / ID `44707031513` success, 174 passed / 0 failed.
- Merge SHA `850e2c851630239140e9a39d5f0978204b2ee025`; main read-back/compare identical.
- Provenance artifact #14615596751, SHA-256 `25c5c192aa96544b5e41c8cac6eeda0d629f3c95af6755e090be6d34ae506a70`.
- Pre-merge ref `safety/pre-pr176-merge-2026-11-20`; post-merge ref `safety/post-merge-pr175-2026-11-20`.


## 최신 main 기준점 — PR #176 병합 및 사후 검증 (2026-11-20)
- PR #176 `docs(cra): audit latest iX7NH and DriveCM guidebook index` 병합 완료. exact head `788d5aea88d12a7bdb1087d264173ac0f487caf8`, squash merge SHA `8f19a8b9fcf8e4582a9470e5483ff08019d1711f`.
- Exact-head Actions Run #1154 / ID `44707491717` success; full pytest 174 passed / 0 failed, source integrity, compile, CRA traceability, official source canary 및 provenance manifest 업로드 성공.
- Provenance artifact #14614954168, 2,567 bytes, SHA-256 `067e43ccfc1c5b438f719489dc44f3e2ead4e152a2294d2c9b5031ca6bc192dd`. 공식 PDF evidence upload 단계는 skipped; 원본 PDF 취득으로 간주하지 않음.
- main read-back/compare는 merge SHA와 동일. 복구 기준점 `safety/pre-pr176-merge-2026-11-20`, `safety/post-merge-pr176-2026-11-20` 유지.
- 통합 보고서 v0.21 §42, 제조사 인벤토리 28행 반영. 2026-09-08~09-14 iX7NH/DriveCM 가이드북은 목록 메타데이터만 확인; 첨부 원문 미확보.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.


## 2026-11-21 최신 운영·ETSI 원문 상태 추가 검증

- Production Run #2526 / ID `44825006768`: job success이나 조사 결과는 **DEFERRED**. 공식 source 10개 확보 후 Gemini 3.8 Flash 503, Gemini 3.5 Flash Lite 응답은 EUR-Lex 공식 원문 링크 누락으로 품질 검증 거절. 신규 보고서·archive·Discord 변경 없음; operational guard no-op 및 checkpoint pruning 성공. Actions Summary step은 completed/success이나 job success를 조사 완료로 계산하지 않는다.
- Run #2526 시작: 2026-11-20 21:58:47 UTC (2026-11-21 06:58:47 KST). cron 예상 슬롯 21:17 UTC 대비 약 41분 47초 지연. :17 offset은 punctuality guarantee가 아님.
- ETSI live Work Programme query 및 Work Item Monitoring에서 EN 304 635 (DEN/CYBER-EUS-0016) 최신 version **V1.0.9** 확인. Current status: EC assessment before WNV requested (2026-11-19); next status: EC assessment before WNV received (2026-11-28). 2026-11-20 V1.0.9 draft upload remark: Draft Review after PE, Enquiry 및 EC HAS2 comments resolution을 포함한 CYBER-EUSR 승인본.
- 일부 cached individual Work Item detail snapshot은 여전히 V1.0.1 / 2026-09-17을 표시한다. Live query + Monitoring의 V1.0.9와 불일치하므로 stale cache discrepancy를 기록하고, V1.0.9 원문 PDF 확보 전 본문/페이지 수/SHA를 주장하지 않는다.
- ETSI free download area에는 V1.0.1 (2026-06), 2,700,830 bytes가 표시된다. 이는 V1.0.9 다운로드 가능성이나 원본 확보를 증명하지 않는다.
- 2026-11-23 GoSRSReq006-M/606 AMD 1 examination meeting은 예정 상태. 회의록/결정/ESO 통지 확인은 회의 후 수행.
- 상세 증거 및 후속 P0: `reports/CRA_ETSI_EN304635_V109_LIVE_STATUS_AND_RUN2526_AUDIT_2026-11-21.md`.
- 변경 범위: 문서·감사로그만. main.py, 운영 workflow, secrets, Gemini/Discord 호출 빈도 및 운영 데이터 미변경.


## 2026-11-21 — AI 자기검토 및 개선 선별 기준 정비
- AI_RULEBOOK의 자기검토·동적 표준화·ETSI·자동화 결과 관련 후행 섹션을 60~71번으로 재번호화해 기존 1~59번과의 중복을 해소.
- Section 69를 과거 EN 304 635 V1.0.1 sample evidence로 명확히 한정. 최신 Work Item V1.0.9와 무료 다운로드 V1.0.1을 구분하고, V1.0.9 원문/페이지 수/본문/hash 미확보를 명시.
- Section 71 및 세션 연속성 운영 문서 §8에 대화별 결과 검토, AI 행동 점검, 개선 선별 기준, 반영 수준(A~D), 효과 검증을 추가. 모든 대화를 무차별 저장하지 않고 반복 가능·근거 있는 개선만 영구 반영.
- PR #191 post-merge main CI #1294 / Run ID 44838660060: success. PR #191 merge SHA/main `c813b7d6b48890b87c099d5a3f7c322170c3baf3`.
- 이번 작업은 운영 행동 기준 정비이며 실제 장기 효과는 후속 세션/운영 실행에서 검증 예정.


## 2026-11-21 — 일일 재귀개선 모방 알고리즘
- PR #192 main post-merge CI Run 44839652639: success. Full pytest, CRA traceability, official source canaries, provenance upload까지 통과.
- 기준일 2026-11-21 KST. 다음 날짜 변경 시 세션 시작/재개에서 일일 검토 실행.
- 프로토콜: `AI_RECURSIVE_IMPROVEMENT_PROTOCOL.md`; AI_RULEBOOK §72; 세션 운영 문서 §9.
- 현재 상태: 문서화 및 CI 검증 완료, 장기 운영 효과는 미검증. 백그라운드 자동 감시/모델 가중치 재학습은 구현되지 않음.
- 다음 우선순위: CRA 공식 원문 최신성 검증을 지속하면서 다음 KST 날짜 경계에서 프로토콜 실행 및 효과 관찰.


## 2026-11-22 — 기업용 보고서의 비전문 독자 이해도 보강
- 기존 CRA 통합 보고서 v0.9는 법령·표준·기술 분석의 양은 충분히 축적되어 있었으나, 초심자용 읽는 순서·기초 원리·용어 해설이 전면에 정리되어 있지 않아 비전문 독자의 진입 장벽이 확인됨.
- 통합 보고서를 v0.10으로 갱신: 보고서 목적/독자, 권장 읽는 순서, 일반 서보 드라이브 동작 원리, CRA 적용 판단 단계, 핵심 용어집, 상태 표시, 회사 내 부서별 활용 방법을 서두에 추가.
- 별도 기준 문서 `REPORT_WRITING_STANDARD_CRA.md` 및 AI_RULEBOOK §73 추가. 전문 내용·법적 조건·예외·기술 세부사항을 생략하지 않고 설명 계층을 추가하는 원칙.
- 일반 서보 원리와 LS메카피온 특정 모델의 확인된 사실을 분리. 정확한 모델/SKU/HW/FW/BOM/매뉴얼 미확보 항목은 Unknown 유지.
- 현재 변경은 읽기 안내·설명 구조의 보강이며, 전체 본문 각 절의 상세 해설 확장과 실제 비전문 독자 검토는 계속할 과제.


## 2026-11-22 — 통합 보고서 §1~§4 단계별 해설 추가
- v0.11에서 §1 요약 10개 결론의 독자용 해설, §2 법령·가이드·표준·OJ 효력의 읽는 순서, §3 가상 인터페이스 사례와 증거 요구, §4 단계별 적용일·전환 규칙 설명을 추가.
- 원래 법률 조항·예외·제품별 Unknown 판정은 유지하고, 쉬운 설명과 정확한 전문 기준을 병렬 제공.
- 후속: §5~§10 제조사 의무·신고·표준·기계류·증거·실행 절을 같은 방식으로 순차 확장하고, 심층 부속서도 핵심 개념 안내 및 원문 추적을 보강.


## 2026-11-23 — ST MCU 및 M/606 AMD 1 추적

- 신규 메모: `reports/CRA_ST_MCU_INTEGRATION_AND_M606_FOLLOWUP_2026-11-23.md`.
- EUR-Lex 법령 대조: Implementing Regulation (EU) 2025/2392 Annex I Class I category 14는 보안 관련 기능을 가진 MCU의 기술 설명이며, CRA Article 7(1) 및 해당 규정 전문 (1)~(2)에 따라 중요/핵심 제품 카테고리는 제품 전체의 core functionality 기준으로 판단. ST MCU 통합만으로 드라이브 완제품의 category 14 분류를 자동 확정하지 않음.
- MCU의 실제 보안 기능은 완제품 위험평가·설계·시험 증거에서 별도 평가해야 한다. 정확한 ST order code, 기능 활성화 상태, 키/부트/디버그 정책 및 LS메카피온 SKU/HW/FW/BOM 미확보로 제품별 분류와 Article 32 경로는 Unknown.
- ETSI 공식 캘린더는 GoSRSReq006-M/606 AMD 1 examination meeting을 2026-11-23 Online으로 게시. 일정은 확인했으나 회의 결과·ESO receipt/acceptance는 확인되지 않음.
- 다음 P0: 회의 후 minutes/decision 및 ESO 공식 수령·수락/비수락 통지 확보. 제품 측은 ST 전체 part number와 LS메카피온 정확한 모델 자료를 증거 register에 연결.
 
## 2026-11-23 — CRA 통합 보고서 v0.12 및 M/606/CI 확인

- 통합 보고서 v0.12: §5~§10의 법률 조항을 개발 생애주기·부서 책임·Article 14 접수/triage·표준/OJ 상태 구분·기계류/CRA 위험 경계·제품 증거 추적·완료 게이트로 상세 해설. 기존 법적 조건과 제품별 Unknown을 유지.
- ETSI 공식 캘린더는 GoSRSReq006-M/606 AMD 1 examination meeting을 2026-11-23 Online으로 표시. 일정은 확인했으나 회의 실제 개최/결과·ESO 수락/비수락 원문은 확보하지 못해 Unknown 유지.
- PR #196 exact-head Run #1308 (45094691796): success. Source integrity, compile, CRA traceability, 전체 pytest, PDF/HTML source canary, PDF evidence 및 provenance 업로드 성공. 이전 Run #1307의 JSONL 빈 행 실패는 복구 이력으로 보존.
- ST MCU Category 14: 정확한 주문 코드와 완제품 구성/활성화 증거가 없으므로 부품·완제품 분류를 구분하고 Unknown 유지.
- 다음 P0: M/606 minutes/decision 및 ESO receipt/acceptance 확인, ST 전체 order code 및 LS메카피온 SKU/HW/FW/BOM 확보, §5~§10 실제 독자/전문가 검토.


## PR #196 병합 및 main read-back — 2026-11-23
- PR #196 squash merge 완료. Merge commit: e82683964413ca2c5922477e9755c62ae7b21064.
- PR exact-head 8877c5c3889c43248207e3f55d1bfdbb34a51fd2, Actions Run #1312 / ID 45095111260: success. Source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML canary, provenance manifest upload 성공. PDF evidence upload step은 skipped로 종료했으므로 PDF 원본 확보로 간주하지 않는다.
- main read-back: 보고서 v0.12, §39~§42, 신규 ST MCU/M/606 메모, 상태판 변경 확인. PROJECT_LOG.jsonl 310 records, invalid JSON 0, interior blank 0.
- 복구 refs: safety/pre-pr196-merge-2026-11-23 (pre-merge base), safety/post-merge-pr196-2026-11-23 (merge SHA).
- PR merge commit의 main push CI run은 확인 시점에 아직 조회되지 않음. PR exact-head CI 성공과 main push CI 실행/결과를 구분한다.



---

## 최신 CRA 상태 — M/606 개정 결정 및 PR #197 병합 (2026-11-23)

- PR #197 병합: squash merge SHA b69710cf1eb3c17c1e99fc2ecd57e86c23053fde. PR #196 병합 사후 상태·로그를 main에 반영.
- PR #197 exact-head CI: head 556d74a5133f092581d059e2ae37456793f7102f, Run ID 45095286445: success. Source identity, compile, CRA traceability, 전체 pytest, 공식 CRA PDF/HTML canary, provenance manifest 업로드 성공. PDF evidence upload 단계는 skipped이므로 PDF 원문 파일 확보로 기록하지 않는다.
- main read-back: PROJECT_LOG.jsonl 311 records, invalid JSON 0, interior blank lines 0. PR #197 post-merge safety ref: safety/post-merge-pr197-status-2026-11-23.
- main push CI 추가 검증 완료: PR #196 merge SHA e82683964413ca2c5922477e9755c62ae7b21064의 Run #1313 / ID 45095198162 success, PR #197 merge SHA b69710cf1eb3c17c1e99fc2ecd57e86c23053fde의 Run #1317 / ID 45104679354 success. 두 run 모두 source integrity, compile, CRA traceability, 전체 pytest, PDF/HTML canary, provenance manifest 업로드 성공; PDF evidence upload은 skipped. PR exact-head CI와 main push CI를 각각 기록한다.
- M/606 개정 원문: Commission Implementing Decision C(2026) 7861 final (2026-11-10) 및 Annex I 공식 문서 확보. 항목 1·15는 2026-11-30, 16~41은 2027-01-31, 2~14는 2027-10-30 ESO 채택 기한.
- 개정 제2조 조건: 각 ESO 수령일로부터 1개월 이내 비수락 통지 시 개정 결정이 적용 중단될 수 있다. 각 ESO 수령일과 비수락 여부는 아직 확인되지 않아 효력 관련 후속 검증을 유지한다.
- 법적 경계: 표준 ESO 채택 기한은 OJ 인용일이나 CRA Article 27 적합성 추정 발생일이 아니다. CRA Regulation 자체의 신고/전체 적용일도 이번 M/606 개정으로 바뀌지 않는다.
- ETSI 회의: 2026-11-23 M/606 AMD 1 examination meeting은 공식 캘린더 일정만 확인. 회의 결과·minutes·ESO 공식 통지는 Unknown.
- 제품별 한계: ST MCU 전체 주문 코드 및 보안 기능/활성화 증거, LS메카피온 정확한 SKU/HW/FW/BOM은 미확보. Category 14 또는 Annex III/IV 제품별 판정은 Unknown.
- 범위: CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets 및 API 실행 주기 변경 없음.
- 보고서: CRA 통합 보고서 v0.13, §43에 개정 원문·기한·Article 2 조건·서보 드라이브/ST MCU 영향 반영.


---

## 2026-11-23 — PR #198 병합 후 상태

- PR #198 squash merge SHA: 447fd178fc0068c7616444485d75e639d9edc8f2.
- PR #198 exact-head: d67423bde5c3cbc5dc6f9601e28a1cf494a46d4d, Run #1324 / ID 45105031988 success. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, provenance manifest upload success. PDF evidence upload step skipped.
- 동일 head의 Run #1325 / ID 45105052195는 cancelled. 취소 실행은 성공 건수에 포함하지 않으며, 앞선 #1324 success를 근거로 병합했다.
- main read-back: 보고서 v0.13 및 §43 존재, M/606 matrix Markdown/CSV 변경 반영, PROJECT_LOG.jsonl 314 records, invalid JSON 0, interior blank 0.
- Post-merge safety ref: safety/post-merge-pr198-2026-11-23.
- Main push CI Run #1326 / ID 45114580241 success. Source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries, PDF evidence upload 및 provenance manifest upload 모두 성공. PR exact-head Run #1324에서는 PDF evidence upload이 skipped였으나 main push에서는 실제 업로드 성공.



## 2026-11-23 17:00 KST — 일일 재개 점검 및 M/606 회의 후속 재조회

- 기준 main SHA: 584a7c092ea434d52f7794452ca85b0cbe981210 (PR #203 상태 동기화 기준).
- 열린 PR #204: research/cra-lsmecapion-product-evidence-2026-11-23, main 대비 27 commits ahead / 0 behind (2026-11-23 C/2026/6013 guidance 추가 문서 8개 반영 후), 변경 파일 7개. 현재 열린 PR로 유지하며 exact-head CI를 확인하기 전에는 병합하지 않는다.
- PR #204 보고서 v0.16 §46 및 LS메카피온 제품 증거 등록부를 검토. 제조사 13개 제품군과 예시 모델코드를 실제 사용자 대상 SKU와 구분하고, SKU/HW/FW/BOM 및 ST MCU full order code 미확보 상태를 Unknown으로 유지한다.
- 제조사 공식 카탈로그 상세 페이지를 추가 확인: iX700M 카탈로그 목록 제목은 2025년 7월을 표시하지만 상세 첨부파일 메타데이터는 2025-12-05 파일 날짜를 표시한다. 문서 개정일로 단정하지 않고 register §8에 메타데이터 차이와 PDF 본문 미확보 한계를 기록했다.
- ETSI 공식 캘린더는 GoSRSReq006-M/606 AMD 1 examination meeting을 2026-11-23 Online으로 계속 표시한다. 공개 회의록/결정/ESO receipt·acceptance·non-acceptance 원문은 이번 재조회에서 확보하지 못했다. 회의 개최 여부·결과·Article 2 수령일은 Unknown 유지; 보고서 §47 추가.
- 범위 CRA only. SIL 3 제외. 운영 코드, 운영 workflow, secrets, Gemini/Discord 호출 주기 변경 없음.
- 다음: PR #204 exact-head CI 및 최종 diff 확인, M/606 회의록·ESO 통지 추적, LS메카피온 실제 SKU/HW/FW/BOM 및 ST MCU 주문 코드 증거 확보.



## 2026-11-23 — Commission CRA Guidance C/2026/6013 반영

- EU 관보 OJ C, 17.11.2026에 게재된 Commission Guidance C/2026/6013 원문 61페이지를 확보·검토했다.
- 법적 지위: Commission 공식 해석 지침이나 비구속적 문서. Regulation (EU) 2024/2847 원문과 구분한다.
- 보고서 v0.17 §48 추가: core functionality와 별도 판매 모듈의 제품 경계, ST MCU 등 외부 부품 due diligence, risk appetite/비용만으로 잔여 위험 정당화 불가, 예상 사용기간 기반 지원기간, 보안 업데이트/실질적 변경 구분.
- 제품 증거 등록부 §9 추가: iX700M Converter/Drive Unit의 별도 판매 여부, 정확한 SKU, ST MCU 보안 기능 활성화, 제품 수명 및 지원기간, 펌웨어 변경 기록을 추가 증거 항목으로 등록. 모두 Unknown 유지.
- 공식 Commission CRA standardisation 페이지(2026-11-12 갱신)는 2026-11-10 M/606 개정 및 모든 vertical/일부 horizontal deliverable 기한 3개월 연장을 명시한다. C/2026/6013 guidance와 C(2026) 7861 implementing decision의 기능을 분리한다.
- PR #204 latest head dc9f6674f0a2e7cdeb3953776f3c573c7304272b exact-head Actions Run #1352 / ID 45135630033 success. Source identity, compile, CRA traceability, full pytest, PDF/HTML live canary 및 provenance manifest upload 성공. PDF evidence upload step은 unchanged 조건으로 skipped.
- 새 §48/§9 문서 변경은 별도 커밋으로 추가되므로 최신 head CI를 다시 수행해야 한다. 이전 Run #1352 성공을 새 커밋의 CI 성공으로 오인하지 않는다.
- 범위 CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.



## 2026-11-23 — PR #204 병합 및 최신 CRA 지침 반영 완료

- PR #204: https://github.com/useformotor3/ai-discord-bot/pull/204
- squash merge SHA: 8254b6f97a8c6a82cf33bfa25ab6d01bcf408ff0
- Exact-head CI Run #1358 / ID 45136682197: success.
  - Source identity, compile, CRA traceability, full pytest: success.
  - Official CRA PDF/HTML live canary: success.
  - Provenance manifest upload: success.
  - PDF evidence upload: skipped (unchanged); 신규 PDF 원문 확보로 간주하지 않음.
- main read-back: 통합 보고서 v0.17 §48, LS메카피온 제품 증거 등록부 §9 확인. PROJECT_LOG 324 records, invalid JSON 0.
- 복구 기준점: safety/pre-pr204-merge-2026-11-23 (merge 전 main SHA 584a7c092ea434d52f7794452ca85b0cbe981210), safety/post-merge-pr204-2026-11-23 (merge SHA 8254b6f97a8c6a82cf33bfa25ab6d01bcf408ff0).
- Main push CI: 현재 조회한 commit status에는 별도 status context가 없고, workflow 조회 도구는 PR-triggered runs만 반환하므로 main push run 여부/결과는 별도 확인 필요. PR exact-head CI success와 구분.
- 새 공식 근거: Commission Guidance C/2026/6013 (OJ C, 17.11.2026) 비구속적 해석 지침. Core functionality, 모듈 별도 판매 경계, ST MCU due diligence, 잔여 위험, support period, firmware update substantial modification 해석을 §48에 반영.
- 다음 P0: LS메카피온 실제 SKU/nameplate/HW/FW/BOM 및 Converter/Drive Unit 판매 경계 확보; ST MCU full order code와 보안 기능 활성화 증거 확보; M/606 ESO 수령·비수락 통지/회의 결과 추적.
- 범위 CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.



## 2026-11-23 — LS ELECTRIC Solution Square 매뉴얼 인덱스 교차검증

- LS ELECTRIC Solution Square 공식 Motion & Servo 문서 목록에서 iX700M 사용 설명서 update 2026-09-16, PEGA2 사용 설명서 update 2026-08-28 확인.
- PEGA2 User Manual 영문 상세 결과: update 2026-09-23, PEGA2_ENG_Ver1.3_260831.pdf, 6.0 MB, 적용 제품 PEGA2 series 및 14개 목차 메타데이터 확인.
- LS메카피온 PEGA2 상세 첨부파일은 PEGA2_KOR_Ver1.3_260826.pdf, DATE 2026-08-28. 언어별 파일 동일 개정 여부는 hash/본문 비교 전까지 Unknown.
- iX700M Solution Square update date는 기존 LS메카피온 Ver1.4 인덱스 게시일(2026-05-26)보다 늦지만 버전/파일명이 확인되지 않아 Ver1.5 또는 개정판으로 추정하지 않음.
- 보고서 v0.18 §49 및 제품 증거 등록부 §10 추가. PDF 원문·SHA-256·페이지별 본문은 아직 미확보/미검증.
- 다음 P0: Solution Square iX700M 정확한 파일 식별; iX700M/PEGA2 PDF 원문 확보 및 hash/버전/언어 비교; 통신·업데이트·접근통제 장의 조항별 추출.
- 범위 CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.



## 2026-11-23 — PR #206 제조사 매뉴얼 교차검증 병합 완료

- PR #206: https://github.com/useformotor3/ai-discord-bot/pull/206
- squash merge SHA: acd932fb70bb2e881fdd35b6b9e75f2c829ac59e
- Exact-head CI Run #1362 / ID 45137336327: success.
  - Source identity, compile, CRA traceability, full pytest: success.
  - Official CRA PDF/HTML live canary: success.
  - Provenance manifest upload: success.
  - PDF evidence upload: skipped (unchanged); 신규 PDF 원문 확보로 간주하지 않음.
- main read-back: 통합 보고서 v0.18 §49, 제품 증거 등록부 §10 확인. PROJECT_LOG 326 records, invalid JSON 0.
- 복구 refs: safety/pre-pr206-merge-2026-11-23 (merge 전 main SHA 369926f4e064bf675556135184dbabe22ec0888a), safety/post-merge-pr206-2026-11-23 (merge SHA acd932fb70bb2e881fdd35b6b9e75f2c829ac59e).
- iX700M Solution Square update 2026-09-16 확인, 버전/파일명 미확보. PEGA2 영문 Ver1.3 update 2026-09-23 및 한국어 Ver1.3 file date 2026-08-28 확인; 파일 동일성은 PDF hash/본문 비교 전 Unknown.
- 다음 P0: iX700M 최신 PDF 파일/버전 확보, iX700M·PEGA2 PDF 원문 및 hash 검증, 실제 SKU/HW/FW/ST MCU 주문코드 확보.
- 범위 CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.


## 2026-11-23 — M/606 및 EN 304 625 재확인 / main CI 확인

- 최신 main SHA 재확인: 5197ad352cdd79fdacf9c4e4cc20fedb8ae085c6. 이전 요약에서 언급된 PR #207 병합은 현재 GitHub branch API로 확인되지 않으며, main은 PR #206 merge 후의 이 SHA다. 확인되지 않은 PR #207은 진행 이력으로 사용하지 않는다.
- Main push Actions Run #1365 / ID 45137633064: success (main SHA와 일치). PR exact-head CI와 구분해 main push 검증 성공으로 기록.
- Commission CRA standardisation 공식 페이지: M/606은 2026-11-10 개정, 모든 vertical 및 일부 horizontal 표준 제출 기한 3개월 연장. 제출 기한과 OJ 인용/Article 27 presumption은 별개.
- ETSI 공식 캘린더: GoSRSReq006-M/606 AMD 1 examination meeting 일정 2026-11-23 Online. 공개 minutes/decision 및 ESO별 receipt/non-acceptance notice는 이번 확인에서 확보하지 못함; 결과·Article 2 효력 판단은 Unknown.
- ETSI EN 304 625 work item: 2026-11-19 이후 “Draft Review after PE”, candidate for harmonisation. 물리적·가상 네트워크 인터페이스 요구사항 표준 후보이나 iX700M 적용성은 제품 core functionality/최종 scope 미확정으로 Unknown. EtherCAT/RS-485 포트만으로 자동 분류하지 않는다.
- 통합 보고서 v0.19 §50, 제품 증거 등록부 §11 추가.
- CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.


## 2026-11-23 — PR #208 병합 및 CI 이중 검증 완료

- PR #208: https://github.com/useformotor3/ai-discord-bot/pull/208
- 변경 범위: 보고서 v0.19 §50, 제품 증거 등록부 §11, 상황판/계획/세션/JSONL. 운영 코드·workflow·secrets·API cadence 변경 없음.
- PR #208 squash merge SHA: a27130d7f4a36bdeb9a64717188583f9fa66278c.
- Exact-head PR CI Run #1366 / ID 45138293050: success. Source identity, compile, CRA traceability, full pytest, official PDF/HTML canaries, provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped.
- Main push CI Run #1367 / ID 45138412407: success. PR exact-head CI와 별도 확인.
- 복구 기준점: safety/pre-pr208-merge-2026-11-23 (기준 main SHA 5197ad352cdd79fdacf9c4e4cc20fedb8ae085c6), safety/post-merge-pr208-2026-11-23 (merge SHA a27130d7f4a36bdeb9a64717188583f9fa66278c).
- Main read-back: 보고서 v0.19 §50, 제품 증거 등록부 §11, PROJECT_LOG 328 records / invalid JSON 0.
- CRA only. SIL 3 제외. 운영 코드/workflow/secrets/API cadence 변경 없음.
