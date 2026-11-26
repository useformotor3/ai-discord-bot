

> **PR #244 / post-merge main CI (2026-11-24):** PR #244 exact HEAD 285b4b705c2bc86b4e7a4602ee7825963770b869 passed Run #1517 / 45340773376 (25/25), then expected-head squash merged as 40a92f1b00bf3b0f4e4694895b6399918ee5561f. Main push Run #1518 / 45401343718 on exact merge SHA also passed 25/25. PR #244 changed 6 files (+70/-0), 6 ahead/0 behind, reviews/threads 0, branch PROJECT_LOG 376 valid / 0 invalid. iX700M manufacturer source metadata was rechecked; original manual/DoC/catalogue/CAD binaries remain unacquired. See report §81 / evidence register §38. CRA only; SIL 3 excluded.


> **PR #243 / final CI correction (2026-11-24):** Run #1514 / 45338702162 succeeded 25/25 on exact main SHA 3fbc1bcbf669324706c4ae2f882ff7269ae87f48. PR #243 exact HEAD 9ae09486a10dc374b83ad417fbd09742f0213dc1 passed Run #1515 / 45338890791 (25/25), then expected-head squash merged as 6548eec799c398b35007212e4831d058934fa83b. Post-merge main push Run #1516 / 45340565876 also succeeded 25/25 on exact merge SHA. Earlier in-progress snapshots are superseded. Official source recheck still did not acquire original iX700M manual/DoC/catalogue/CAD binaries; see report §80 / evidence register §37. CRA only; SIL 3 excluded.
> **PR #240 / post-merge main CI:** PR #240 merged at 36b38bfa5ced2894f3bfb06c226706ce0a9bf38b after Run #1507 exact-head success 25/25. Main push Run #1508 / 45329930118 on exact merge SHA also success 25/25. Main PROJECT_LOG 371 records / invalid 0. Official CRA PDF artifact 14890384807 includes all 3 PDFs; ZIP SHA-256 1cb11a4d35de7c922efd5ad2a8d49aada8929875682d20e520c5c9b50f4f19ba. See report §76 / evidence register §33.
>
> **Exact product source paths:** Solution Square manual listing is verified but detail/PDF unavailable; LS Mecapion manual detail wr_id=12652, Drive CE download, Converter CE detail and iX700M CAD detail wr_id=12455 were retried but timed out/502. CE/CAD originals remain unacquired. Manual index still has two Ver1.4 snapshots and one Ver1.3 snapshot. CRA only; SIL 3 excluded.

> **매뉴얼 revision snapshot 정밀 정정:** 기본 목록 및 Servo 필터는 Ver1.4, 명시적 sca= 목록만 Ver1.3을 표시합니다(모두 2026-05-26 게시). 실제 PDF bytes 미확보로 valid revision은 unresolved. See report §75.4 / evidence register §32.
> **최신 상태 정정 (2026-11-24):** PR #239 is merged. Exact PR HEAD e9a15eeaf69e56e610352941f5330604bf78639e, merge SHA 7d1fe1012bd2f8a8e1540918b43b58b4b41014f5; Run #1497 success 25/25 (pytest 189 passed), post-merge main push Run #1503 success 25/25 on exact merge SHA. Main PROJECT_LOG 369 records / invalid 0. The bounded retry recovered the C(2026)7861 Annex PDF; all three official PDFs were fetched in Run #1497. PR #239 and Run #1503: https://github.com/useformotor3/ai-discord-bot/actions/runs/45321136198.
>
> **제조사 자료 현황:** Solution Square iX700M manual index metadata/update 2026-09-16 verified, but SPA detail/PDF not acquired. LS Mecapion index conflict remains (Servo filter Ver1.4 vs unfiltered post no.41 Ver1.3, same 2026-05-26); original manual PDFs not acquired. Converter/Drive CE DoC and 2D CAD/3D STEP are metadata-only, original binaries not acquired. See report §75 / evidence register §32. Actual SKU, independent sale, EU/EEA supply, importer/economic operator, BOM/MCU/security remain Unknown; manufacturer inquiry draft_prepared_not_sent. CRA only; SIL 3 excluded.
>
> **PR #229 status correction:** main push Run #1452 / 45312941583 is verified success 25/25 for merge SHA 4263389aa79cbb7cc17ccda3a019c659ccddef85; prior pending/unverified wording is stale.

> **Source collector reliability:** M/606 Annex C(2026)7861 binary was fetched in Run #1481, but the next three runs (#1483–#1485) each timed out after 30s. A separate tested branch now adds bounded retry/backoff and an explicit partial-pack warning; workflow YAML changes are limited to refreshing the two modified-file source-blob integrity pins; no job steps, main.py behavior, secrets or API cadence changed. See report §74.9 / evidence register §31 and the open PR for exact status.

> **PR #237 / post-merge Run #1483:** PR #237 merged as `792eea6388382a1932f1b775e57776a7ccacf3a6`; Run #1482 and exact-merge main push Run #1483 succeeded 25/25. Important qualification: Run #1483 live PDF artifact fetched 2/3 PDFs; C(2026)7861 Annex timed out, but its 6-page original remains preserved from Run #1481 artifact 14886830715 (SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`). CI green is not equivalent to complete source pack. Details §74.8 / evidence register §30. CRA only; SIL 3 excluded.

> **최신 검증 (2026-11-24):** Main push Run #1481 / ID `45317449785`, exact main HEAD `c395fc5b5b2a393632bb2fbe65b10fd6572b936d`, final success 25/25. CRA official PDF artifact 14886830715 and provenance artifact 14885424833 uploaded. Solution Square manual detail/PDF, LS Mecapion Ver1.3/1.4 originals, Converter/Drive CE DoC originals and iX700M CAD/STEP originals remain unacquired; exact facts and Unknown boundaries are documented in report §74.7 and evidence register §29. Actual SKU/EU supply/importer/BOM/MCU/security remain Unknown. CRA only; SIL 3 excluded.

> **PR #235 최종 병합 및 CI:** Exact HEAD Run #1478 success, merge SHA `4e4aea75960de2e761e47ae3cdc33275ad5553f2`; post-merge main push Run #1479 success (25/25). main read-back identical; PROJECT_LOG 363 records / invalid 0. Report §74 / evidence register §28 include official iX700M architecture, catalog and training-material evidence, with all unacquired original manuals/DoC/CAD files and product-market unknowns preserved. [PR #235](https://github.com/useformotor3/ai-discord-bot/pull/235). CRA only; SIL 3 excluded.

> **PR #234 병합 및 CI 확인:** Exact HEAD Run #1473 success, merge SHA `bd46aa2a26a39a5389f3b314a94523bb495689b5`; post-merge main push Run #1474 success (25/25). main read-back identical, PROJECT_LOG 361 records / invalid 0. [PR #234](https://github.com/useformotor3/ai-discord-bot/pull/234). PR #235는 iX700M 공식 아키텍처 PDF/카탈로그 자료를 추가 기록하는 문서 PR이며 exact-head Run #1475 success 확인; 병합 전 검토 중.

> **2026-11-24 iX700M 공식 기술자료 추가:** LS ELECTRIC 호스팅 LS Mecapion 발표 PDF의 iX700M 전용 구간에서 Converter/Drive 모듈 분리, RS-485 내부 통신, EtherCAT In/Out, USB/Loader, I/O/encoder 구조를 확인했습니다. 2025 iX700M KR/EN 카탈로그 및 2025-10-27 교육자료 인덱스도 확인했지만 해당 원본 파일들은 미확보입니다. 보안 구현, 실제 SKU, EU 공급은 여전히 Unknown. [통합 보고서 §74](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md), [증거등록부 §28](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md). CRA only; SIL 3 제외.

> **2026-11-24 최신 확인:** PR #233 exact-head Run #1471 success, expected-head squash merge SHA `d160cb2eea13d3f18ac4bc8e98c40d4378881c1a`; post-merge main push Run #1472 success (25/25), main PROJECT_LOG 360 records / invalid 0. 제조사 iX700M 제품군 공식 인덱스는 EtherCAT 통신형, AC 380–480 V, 4.5–75 kW, 축당 16.1–168 A로 표시. Solution Square 상세 PDF, LS메카피온 매뉴얼 실제 revision, Converter/Drive CE DoC 원본, DWG/DXF/STEP 원본은 여전히 미확보. Ver1.3/Ver1.4 목록 충돌 및 실제 SKU·EU 공급·importer·BOM/MCU/security Unknown 유지. [통합 보고서 §73](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md), [증거등록부 §27](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md). CRA only; SIL 3 제외.

> **2026-11-24 최신 확인:** PR #232 Run #1462 success 및 merge SHA `d3b75a84d2b84ada59d2314780461e53b21e090b`. 공식 CRA PDF C(2026)5252, C/2026/6013, C(2026)7861 세 원본 모두 확보·hash 검증. iX700M 공식 manual list snapshot은 Ver1.3/Ver1.4로 충돌하며 PDF 내부 revision은 미확인. Converter/Drive DoC 및 CAD 원본, 실제 SKU/EU 공급·수입자·BOM/MCU/security는 계속 미확인. PR #229 main push Run #1452 success 확인. 상세는 통합 보고서 §72와 증거등록부 §26.

> **2026-11-24 PR #231 병합 및 공식 CRA PDF 증거:** Exact HEAD Run #1460 success, PDF artifact ID 14884517329에서 C(2026)5252 Annex 및 C/2026/6013 OJ Guidance PDF 원본과 SHA-256 확보. C(2026)7861 Annex는 timeout으로 미확보. PR #231 squash merge SHA `c7b59ae51891a2b878fc85b0910a89b50e4efe17`. 통합 보고서 §71 및 제품 증거등록부 §25 참조. Solution Square iX700M 상세 PDF, Ver1.3/Ver1.4 실제 revision, CE DoC/CAD 원본 및 제품별 SKU·EU 공급·BOM/MCU/security facts는 계속 Unknown. 제조사 질의서는 미발송.

> **2026-11-24 LS메카피온 질의 발송 안내:** [공식 연락 경로 및 커버메일 초안](reports/LS_MECAPION_IX700M_INQUIRY_DISPATCH_GUIDE_2026-11-24.md). 국내 영업·전국 기술지원·해외 채널을 공식 페이지 기준으로 구분했으며, 실제 발송/회신은 아직 미확인입니다.

> **상시 다음 단계 버튼 규칙 (2026-11-24):** 주요 CRA 진행 응답의 마지막에 **다음 단계 계속 진행** 버튼을 제공한다. 버튼은 단순 진행 요청이 아니라 최신 GitHub 상태 재확인, 과거 기록의 관련성 판정, 증거·테스트 검증, 실제 다음 작업, 실패/개선 기록, 버튼 재제공을 요청한다. 최신 연구 근거와 정식 payload는 [AI 지속 메모리·개선 및 버튼 운영 규약](docs/AI_CONTINUOUS_IMPROVEMENT_AND_NEXT_STEP_PROTOCOL.md)에 고정했다.

> **2026-11-24 LS메카피온 제조사 질의서 초안:** [iX700M 공식 기술·영업 질의서](reports/LS_MECAPION_IX700M_FORMAL_TECHNICAL_COMMERCIAL_INQUIRY_2026-11-24.md). Converter/Drive 독립 판매, EU 공급, 실제 SKU, Ver1.4 매뉴얼/CAD 원본, 회로도/BOM/MCU 전체 부품번호 및 보안 설정을 질문. 제조사 발송·회신은 아직 확인되지 않았으며 미확인 사항은 Unknown 유지.

> **PR #223 병합 완료:** `a1fe5b983e1cecb1235b56071534e05884d61786`. Run #1432 success, pytest 186. C(2026)5252 Annex와 C/2026/6013 OJ PDF의 실제 바이너리/SHA-256 및 PDF/provenance artifact를 확보했습니다. C(2026)7861은 Commission register timeout으로 manifest에 unavailable 기록. iX700M의 독립 판매·EU 개별 공급·실제 SKU는 계속 미확인입니다.

> **Run #1427 PDF 확보:** C(2026)5252 Annex(84p, SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`)와 C/2026/6013 OJ(61p, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`) 실제 PDF를 확보했습니다. C(2026)7861 Annex는 Commission register timeout으로 unavailable manifest에 기록했습니다. PDF artifact [14874639916](https://github.com/useformotor3/ai-discord-bot/actions/runs/45294643451/artifacts/14874639916), provenance [14875084483](https://github.com/useformotor3/ai-discord-bot/actions/runs/45294643451/artifacts/14875084483). Run #1427 success, pytest 186.

> **PDF 수집 안정성 보완:** Run #1419에서 ANFR fallback의 HTML 응답/timeout을 확인해 Commission-hosted transition-pathways.europa.eu PDF로 교체하고, source별 partial fetch 및 unavailable 사유 기록을 추가했습니다. 잘못된 PDF/identity mismatch/비허용 redirect는 계속 fail-closed입니다. PR #223 새 HEAD CI 검증 중입니다.

> **Run #1410:** Exact HEAD 1c49b9f4 CI workflow succeeded, including tests, CRA traceability, HTML locator validation and provenance manifest upload. C(2026)7861 PDF canary was explicitly SKIPPED because the Commission document-register anti-bot interstitial blocked the unauthenticated runner; no PDF bytes/hash claim is made. A source-comment/pin-only update followed, so the newest HEAD still needs final CI.

> **C(2026)7861 PDF 수집 한계:** Run #1404에서 Commission document-register API가 CI runner를 anti-bot interstitial로 리디렉션했습니다. 이 문서는 OJ PDF가 아니므로 대체 URL을 추정하지 않고 source-unavailable로 처리하도록 수정했습니다. 외부 mirror 자동 수용은 하지 않으며 PDF bytes/hash는 미확보 상태로 명시합니다. C/2026/6013은 공식 Publications Office OJ PDF로 전환했습니다.

> **CI 원문 수집 수정:** C/2026/6013 PDF의 EUR-Lex endpoint가 CI에서 interstitial로 리디렉션되어 실패한 것을 확인하고, 공식 Publications Office 직접 OJ PDF(61 pages)로 변경했습니다. exact host allowlist와 회귀 테스트를 추가했으며 새 HEAD CI 검증 전 PR #218은 미병합입니다.

> **2026-11-24 추가 조사:** iX700M 공식 제품군 사양, Ver1.4 매뉴얼 목록, 외형 CAD 2D/3D 게시, 해외 영업 창구 및 미해석 `iX700MCB-B-8K`를 확인했습니다. 매뉴얼/CAD 본문, 회로도/BOM/MCU는 미확보이며 독립 판매·EU 개별 공급은 Unknown입니다. PR #218 CI Run #1388은 Commission PDF newsroom interstitial redirect로 실패해 보완·재검증 중이며 미병합입니다. [상세 보고서 §14](reports/CRA_MECAPION_SERVO_DRIVE_SCOPE_CLASSIFICATION_2026-11-24.md), [증거 등록부 §18](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md), [통합 보고서 §56](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md).



> **2026-11-24 iX700M 제품경계 조사:** 제조사 자료로 Converter Unit/Drive Unit의 기능 분리, `iX700MCV...` / `iX700MD...` 별도 모델코드 및 유닛별 CE DoC 게시를 확인했습니다. 실제 독립 판매·EU 개별 공급 및 사용자 실제 SKU는 아직 Unknown입니다. [상세 보고서 §13](reports/CRA_MECAPION_SERVO_DRIVE_SCOPE_CLASSIFICATION_2026-11-24.md), [제품 증거 등록부 §17](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md), [통합 보고서 §55](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md). PR #217 merge SHA: `5ea2f500dc69bd7c946895aeb3141df8fd8d1f99`.

> **2026-11-24 CRA 제품 분류 분석:** [LS메카피온 서보 드라이브 CRA 적용 범위·제품 분류 보고서 v1.0](reports/CRA_MECAPION_SERVO_DRIVE_SCOPE_CLASSIFICATION_2026-11-24.md)을 추가했습니다. 통신형 제품의 Article 2 데이터 연결, 완제품 core functionality, EtherCAT/Fieldbus category 10, ST MCU category 14/4 및 구성품 실사를 구분합니다. 실제 SKU·HW/FW·BOM·MCU 주문코드·모듈 판매 경계는 Unknown으로 유지합니다. 작업 브랜치: research/cra-servo-drive-scope-classification-2026-11-24-v2; 기준 main: d1b33a4d8988f6f940070e03d5b4fa26570c384e.

> **PR #206 병합 — 2026-11-23:** Merge SHA `acd932fb70bb2e881fdd35b6b9e75f2c829ac59e`. 통합 보고서 v0.18 §49 및 제품 증거 등록부 §10에 LS ELECTRIC Solution Square와 LS메카피온 매뉴얼 인덱스 교차검증을 반영했습니다. Exact-head Run #1362 / ID `45137336327` success. iX700M 최신 목록 update 2026-09-16은 확인했으나 버전/파일명은 Unknown; PEGA2 영문 Ver1.3 및 한국어 Ver1.3 파일 메타데이터를 기록했으며 동일 개정 여부는 미검증. 복구 refs: `safety/pre-pr206-merge-2026-11-23`, `safety/post-merge-pr206-2026-11-23`.

> **제조사 매뉴얼 최신성 교차검증 — 2026-11-23:** [통합 보고서 v0.18 §49](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md) 및 [제품 증거 등록부 §10](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md)에 LS ELECTRIC Solution Square 자료를 추가했습니다. iX700M 목록 update 2026-09-16, PEGA2 영문 Ver1.3 문서 update 2026-09-23을 확인했으나 PDF 본문·hash는 미확보이며 버전 최신성을 과장하지 않습니다.

> **PR #204 병합 — 2026-11-23:** Merge SHA `8254b6f97a8c6a82cf33bfa25ab6d01bcf408ff0`. 통합 보고서 v0.17 §48에 Commission Guidance C/2026/6013(OJ C, 17.11.2026)을 반영하고, LS메카피온 제품 증거 등록부 §9를 추가했습니다. Exact-head Run #1358 / ID `45136682197` success: source integrity, compile, CRA traceability, full pytest, official PDF/HTML canary, provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped. 사전/사후 복구 refs: `safety/pre-pr204-merge-2026-11-23`, `safety/post-merge-pr204-2026-11-23`. 실제 SKU/HW/FW/ST MCU 주문코드 및 모듈 판매 경계는 계속 Unknown.

> **최신 CRA 공식 지침 — 2026-11-23:** [통합 보고서 v0.17 §48](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md) 및 [LS메카피온 제품 증거 등록부 §9](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md)에 Commission Guidance C/2026/6013 (OJ C, 17.11.2026)을 반영했습니다. 지침은 비구속적 Commission 해석 자료이며, 제품의 core functionality, 별도 판매 모듈 경계, ST MCU due diligence, 예상 사용기간 기반 support period, firmware substantial modification 판단을 구체화합니다. PR #204 문서 추가 커밋의 최신 head CI는 별도 재검증 대상입니다.

> **2026-11-23:** PR #203 병합 완료(merge SHA `584a7c092ea434d52f7794452ca85b0cbe981210`). Exact-head Run #1343 및 main push Run #1344 모두 성공. 복구 기준점: `safety/post-merge-pr203-2026-11-23`. LS메카피온 공식 제품군 목록과 iX700M 예시 모델코드를 증거 등록부에 추가하고, 통합 보고서 v0.16 §46을 작업 브랜치에 작성했습니다. 실제 대상 SKU와 ST MCU 전체 주문코드는 아직 Unknown.

> **2026-11-23:** PR #202 병합 완료(merge SHA `794d2d69c6a46e85d5cc64c7c0c337a7493ebcc4`). CRA 통합 보고서 v0.15 §45/§45.7 및 ETSI M/606 18개 최신 매트릭스(18 rows, 21 columns)가 main에 반영되었습니다. PR exact-head Run #1341 및 main push Run #1342 모두 성공. PDF evidence upload은 unchanged 조건으로 skipped. 복구 기준점: `safety/post-merge-pr202-2026-11-23`. CRA only; SIL 3 제외.

> **2026-11-23:** PR #201 병합 완료(merge SHA `0643c656b7801fcaf4453042e97623f2e57d73cd`); post-merge safety ref `safety/post-merge-pr201-2026-11-23`. PR #201 exact-head Run #1337 성공. Main push Run #1338은 마지막 확인 시점에 진행 중. ETSI M/606 18개 active work item 최신 상태를 2026-11-23 / Work Programme v2.3.3 기준으로 재점검했고, 통합 보고서 v0.15 §45 및 별도 Markdown/CSV 스냅샷을 작업 브랜치에 추가했습니다. EN 304 619 V1.0.3 및 EN 304 635 V1.0.9 변경 확인. CRA only; SIL 3 제외.

> **2026-11-23:** PR #200 병합 완료(merge SHA `53d91ee5beb16f703bbaddc3ec64dd238989d55a`). 보고서 v0.14 §44가 main에 반영되었습니다. Exact-head Run #1331 성공. Main push Run #1332 성공: source integrity, compile, CRA traceability, full pytest, 공식 PDF/HTML canary 및 provenance manifest upload 성공. PDF evidence upload은 unchanged 조건으로 skipped. 사후 복구 기준점: `safety/post-merge-pr200-2026-11-23`. CRA only; SIL 3 제외.

# CRA Servo Drive Compliance & Engineering Project

> **2026-11-23:** PR #198 병합 완료(merge SHA `447fd178fc0068c7616444485d75e639d9edc8f2`). 보고서 v0.13 §43 및 M/606 deadline crosswalk가 main에 반영되었습니다. Exact-head Run #1324 성공; duplicate Run #1325 cancelled. Main push Run #1326 성공: 전체 테스트·CRA traceability·공식 PDF/HTML 확인·PDF evidence 및 provenance 업로드 모두 성공. 사후 복구 기준점: `safety/post-merge-pr198-2026-11-23`.

> **최신 규제·보고서 갱신 — 2026-11-23:** [CRA 통합 보고서 v0.13](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)의 §43에 Commission Implementing Decision C(2026) 7861 final 원문을 반영했습니다. M/606 ESO 채택 기한은 항목 1·15: 2026-11-30, 항목 16~41: 2027-01-31, 항목 2~14: 2027-10-30입니다. Article 2의 ESO 수령 후 1개월 비수락 조건은 별도 추적하며, ESO 채택과 OJ 인용/CRA Article 27 적합성 추정을 혼동하지 않습니다. PR #197은 b69710cf1eb3c17c1e99fc2ecd57e86c23053fde로 병합되었습니다.


> **CRA 조사 갱신 — 2026-11-23:** [ST MCU 통합 제품 분류 및 ETSI M/606 AMD 1 후속 메모](reports/CRA_ST_MCU_INTEGRATION_AND_M606_FOLLOWUP_2026-11-23.md). ST MCU 사용만으로 서보 드라이브 완제품을 Annex III Class I category 14로 자동 분류하지 않으며, 제품 전체 core functionality와 정확한 MCU/제품 증거를 별도로 확인합니다. ETSI 공식 캘린더의 11월 23일 회의 일정은 확인했으나 회의 결과 및 ESO 수락은 미확인입니다.


> **보고서 독자 안내 — 2026-11-22:** [CRA 통합 보고서 v0.10](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)의 첫 부분에 읽는 순서, 서보 드라이브 작동 원리, CRA 판단 흐름, 핵심 용어 및 회사 내 활용 방법을 추가했습니다. 작성 기준은 [CRA 기업용 보고서 작성·설명 표준](REPORT_WRITING_STANDARD_CRA.md)을 따릅니다. 전문적인 법률·기술 세부사항은 생략하지 않고 비전문 독자도 따라갈 수 있도록 설명 계층을 추가합니다.

> **자동화 운영 점검 — 2026-11-20:** [실제 운영은 3시간 주기이며, 정각 지연을 줄이기 위해 UTC :17로 이동하고 no-op/모델 장애 결과를 별도 표시하도록 개선](reports/CRA_AUTOMATION_CADENCE_AND_OUTCOME_OBSERVABILITY_AUDIT_2026-11-20.md). 5분 주기 Gemini 실행은 설정하지 않음. 초기 PR #189 HEAD CI 182 passed / 0 failed. cron 변경 후 cadence 테스트의 구 설정값 고정 문제를 발견·수정했고 code HEAD Run #1271에서 182 passed / 0 failed; fallback fixture의 2개 실패를 수정했고 최신 HEAD Run #1285에서 183 passed / 0 failed; main 미병합.

> **최근 병합 — 2026-11-20:** PR #184 merged to main as `9dbe6e92c358d0361f9640651152e4d1e8b1ec6b`. Exact-head CI Run #1238 succeeded (174 passed / 0 failed). M/606 18-item matrix, latest EN304635/636 Class II draft checks, CENELEC 50770 WIID crosswalk and AI session self-review protocol are in main. See PROJECT_STATUS_CURRENT.md and PR #184.

## 최신 ETSI 조사 — 2026-11-20
- [M/606 active 18개 Work Item master matrix](reports/CRA_ETSI_M606_18_ACTIVE_WORK_ITEM_MASTER_MATRIX_2026-11-20.md)
- [18개 Work Item CSV](reports/CRA_ETSI_M606_18_ACTIVE_WORK_ITEM_MASTER_MATRIX_2026-11-20.csv)


> **최신 재개 상태 — 2026-11-20:** PR #182 merged to main (904b2ed0897331ced9dedfcbd25afd608f92f951). Exact-head Run #1177 success, 174 passed / 0 failed. Integrated report v0.9: full ETSI M/606 18-item matrix, two ETSI Work Item metadata discrepancies; latest EN304636 draft confirms legal Class II, EN304635 V1.0.1 public sample confirms Class II; both latest drafts align with law, OT 7-deliverable profile reconciliation, C(2026)7861 Article 2/deadlines, Annex III/IV and Article 32 route matrix. Product classification remains Unknown pending exact SKU/BOM/FW evidence.

## 최신 조사 산출물
- [통합 CRA 보고서 v0.11](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)
- [ETSI 8개 Work Item 및 OT 50770 재조사](reports/CRA_ETSI_M606_8_ITEM_AND_OT_50770_RECONCILIATION_2026-11-20.md)
- [Annex III/IV 및 Article 32 제품분류·경로 분석](reports/CRA_ANNEX_III_IV_ART32_SERVO_DRIVE_CLASSIFICATION_MATRIX_2026-11-20.md)


## 최신 법적 분류 산출물 — 2026-11-20
- [Annex III/IV 및 Article 32 서보 드라이브 분류·경로 분석](reports/CRA_ANNEX_III_IV_ART32_SERVO_DRIVE_CLASSIFICATION_MATRIX_2026-11-20.md)
- [제품 분류 및 Article 32 route matrix CSV](reports/CRA_ANNEX_III_IV_ART32_SERVO_DRIVE_CLASSIFICATION_MATRIX_2026-11-20.csv)


> **최신 재개 상태 — 2026-11-20:** ETSI M/606 미검토 8개 work item 개별 감사 및 CLC/TC 65X prEN 50770 split/status reconciliation 진행. prEN 50770-1은 -1-1 firewall / -1-2 IDS/IPS로 분할되어 7개 deliverable. C(2026)7861 Annex I deadline groups: 1/15=2026-11-30, 2–14=2027-10-30, 16–41=2027-01-31; Article 2 ESO receipt/acceptance condition remains unverified. CRA 전체 규제·표준화가 핵심이며 LS메카피온은 사례연구.

## 최신 조사 산출물 — 2026-11-20
- [ETSI 8개 Work Item 및 OT 50770 통합 재조사](reports/CRA_ETSI_M606_8_ITEM_AND_OT_50770_RECONCILIATION_2026-11-20.md)
- [ETSI 8개 상태 감사 CSV](reports/CRA_ETSI_M606_8_ITEM_STATUS_2026-11-20.csv)
- [OT 7개 deliverable 및 서보드라이브 경계 CSV](reports/CRA_M606_OT_IACS_7_VERTICAL_PROFILES_SERVO_DRIVE_BOUNDARY_2026-11-20.csv)


> **최신 재개 상태 — 2026-11-20:** PR #180 AI 자기검토·세션 연속성·토큰 효율 기준 병합 완료. Main merge SHA `3ded54116b3ecfa77645c50ada45575fbe656aea`; exact-head Run #1162 success (174 passed / 0 failed). CRA 전체 규제·표준화·제품 적용성 조사가 핵심이며 LS메카피온은 사례연구다. 다음 P0는 ETSI M/606 18개 개별 레코드, CEN/CENELEC OT prEN 50770 project records, C(2026)7861 Article 2 ESO acceptance evidence, 41-row deadline/OJ mapping이다.


> **최신 재개 상태 — 2026-11-20 CRA 중심 갱신:** main `8abf70a68add7f0e7a38283da3dd3d78c160829c`; PR #178 병합 완료; CRA 통합 보고서 v0.5 §§25–§28 main 반영. ENISA SRP 운영 제약, CEN EN 40000-1-1/-1-2 발행(단 CRA OJ citation 기대 없음), ETSI M/606 18개 active item, C(2026)7861 M/606 deadline amendment, COM(2026)780 표준화 법제 개편 제안 반영. LS메카피온은 사례연구이며 CRA 전체 규제·표준화·신고·적합성 트랙이 최우선.

산업용 서보 드라이브를 사례로 EU Cyber Resilience Act(CRA) 전체 규제·표준화·제품 적용성·설계·검증·문서화를 수행하는 프로젝트입니다. CRA 법령과 공통 이행체계가 중심이며 특정 제조사 조사는 사례연구로 관리합니다. 문서의 기본 언어는 한국어이며, 법령·표준·제조사 원문은 원어와 출처를 보존합니다.

## 공식 프로젝트 범위 — 2026-11-17 확정

- **현재 활성 프로젝트는 CRA 대응만**입니다. 조사, 법령 적용성 분석, 요구사항 추적, 설계 통제, 검증 증거 및 한국어 통합 보고서를 CRA 기준으로 진행합니다.
- SIL 3 기능안전 벤치마킹·하드웨어 설계 자료는 과거에 저장소에 반영된 별도 산출물로 보존합니다. CRA 작업의 후속 단계가 아니며, 사용자가 별도로 명시적으로 재개 요청하기 전에는 조사·수정·확장하지 않습니다.
- 과거 SIL 3 파일과 PR/커밋은 삭제하거나 이력을 재작성하지 않습니다. CRA 사이버보안 요구사항과 기능안전 요구사항을 동일시하지 않습니다.

> **기록 원칙:** 프로젝트의 공식 진행 상태와 재개 지점은 이 저장소에 기록합니다. 대화창의 기억에만 의존하지 않습니다.

### 현재 기준점 — PR #104 LS메카피온 제품군 예비 분석 보고서 병합 (2026-11-19)
- 최신 main: PR #104 merge SHA `c3d234240d342d82cf9402ef0b07b82531ddee03`.
- PR #104 exact-head Run #1004 / ID 44485297107: success, **174 passed / 0 failed**.
- CRA traceability 통과: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, M/606 41.
- Official CRA HTML source pack 10개 fetch 및 10-record JSON provenance manifest parse/round-trip 통과. Artifact #14509668548, SHA-256 `1d3ac8ea2e049780161766ef158fecfa3ab2a7d795b477424b339e5004772bf6`, expires 2026-11-26 08:10:28 UTC.
- PDF canary는 EUR-Lex C/2026/6013 endpoint empty body로 temporary outage / SKIPPED; PDF artifact 없음. PDF 검증 성공으로 기록하지 않음.
- Post-merge safety ref `safety/post-merge-pr104-2026-11-19`와 main identical. Exact-main push CI는 별도 확인 전.
- LS메카피온 13개 제품군 예비 분석 보고서 v0.1이 main에 추가됨. 모델별 CRA 판정과 법령 전수 수집은 미완료.

## 현재 상태 — 2026-11-19

- 최신 main: PR #102 merge `84101bcc8871e41f8a25de3edf892666b1650b8c`; PR #102 exact-head Run #1000 success, 174 passed / 0 failed. Official source provenance manifest artifact now JSON-round-trip verified.
- EVD-01~16 ↔ CRA ↔ SEC-001~036 추적표와 E-001~E-015 제품 증거 register가 main에 반영됨. Official source pack v4에는 2025/2392 기술 설명이 포함되며, 10-source provenance manifest가 GitHub Actions artifact로 보존됨.
- 실제 제품 자료는 모두 not_provided. accepted/비적용 판정은 provenance·SHA-256·locator·검토자·근거 검증을 통과해야 한다.
- 다음 단계는 정확한 모델 데이터시트와 사용설명서 확보 후 제품 variant별 CRA scope/core-functionality 및 증거 적용성 검토.

## 과거 상태 기록 — 2026-11-18

- 최신 main 기준: PR #88 merge 16cdec76def2e8920d8fc2ca3b6a43e497d41d83; exact-main Run #957 success, 162 passed / 0 xfailed.
- 현재 CRA 제품 분류 심화 감사 브랜치: cra/applicability-core-functionality-audit-2026-11-19 (PR/CI 전). 적용성 보고서와 EVD 매트릭스에 Annex III/IV core-functionality 및 제품 경계 게이트를 통합 중.
- 제품별 모델/SKU 및 실제 MCU 식별은 여전히 미확인. 개별 분류·MCU 선정 결론 금지.

## 이전 상태 기록 — 2026-11-18

- **활성 범위: CRA 대응만.** SIL 3 자료는 역사적 산출물로 보존하며 별도 명시적 재개 지시 전 비활성.
- 현재 구현 작업 브랜치: 없음 (PR #35 병합 완료; PR #36은 문서 전용 사후 동기화, 다음 구현은 최신 main에서 새 브랜치로 시작)
- 최신 운영 기준: GitHub `main` 브랜치 (정확한 HEAD는 세션 시작 시 저장소에서 실시간 조회; 과거 커밋 SHA를 현재 HEAD로 고정 표기하지 않음); 최신 CRA source 기준점: PR #29 merge commit `9c16724b8b72bd09d3492b19ff714602b235c66b`; PR #28 recovery checkpoint `942e1e6b5f2887001279a96c21f94138d283a689`; 관리 문서 PR #27 `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; source pipeline PR #26 `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`
- 최신 CRA source provenance 통합: [PR #26](https://github.com/useformotor3/ai-discord-bot/pull/26) 병합 완료; 공식 CELLAR 7개 법령 자료 + Commission 공식 페이지 2개 수집, claim-level validator 및 source manifest 반영
- 정오표 우선순위 보강: [PR #29](https://github.com/useformotor3/ai-discord-bot/pull/29) 병합 완료; Article 64(10)/67의 영어 corrigenda를 prompt excerpt에서 적용/확인하고 raw text hash와 corrected excerpt hash를 분리
- [CRA 공식 출처 수집·주장 추적 파이프라인 보고서](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md): Run #573, 138 passed / 1 xfailed, live 9-source canary 및 Article 13(8) quote 확인
- CRA-only 범위 통제 기준점: PR #18 merge `b7813ddd311bc51bfb0eb26458eace9ff82b621f`; 통합 보고서 PR #19 merge `5776ca609130033bfff17ca62c9fabc3b9570b3b`; 인터페이스 매트릭스 PR #20 merge `951fc5ee0122b847b5e8f77bd5e0706db65efb76`
- CRA 정정 보고서 #1–#38 및 인덱스: main 보존 확인
- [CRA 서보 드라이브 통합 규제·기술 준수 보고서 v0.9](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md): PR #21 병합 완료, 제품별 적용성 확인 전
- [CRA 요구사항 추적표 v0.2](reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv): PR #19 병합 완료, 35개 요구사항 행, 제품 증거 미확인 상태
- [서보 드라이브 인터페이스별 CRA 적용성 매트릭스](reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv): PR #20 병합 완료, 15개 인터페이스/기능 유형, 제품별 증거 확인 전 잠정
- [CRA 서보 드라이브 보안 통제·시험 매트릭스](reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv): 36개 통제 목표/위험/시험/증거 초안, 35개 요구사항 ID와 교차 연결, PR #22 병합 완료; 모델별 검증 전
- [CRA 서보 드라이브 참조 보안 아키텍처 v0.1](reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md): 논리 블록·신뢰 경계·데이터 흐름 참조 설계, PR #23 병합 완료; 제품별 회로 확인 전
- [브랜치 정합성 및 CRA 소스 검증 통합 감사](reports/BRANCH_RECONCILIATION_2026-11-17.md): divergent branches, source gate 선택 이식 계획, validator 결함 및 복구 원칙; PR #24 병합 완료
- CRA 정정 보고서 #1–#38: 개별 원문·원본 SHA 보존, 주요 정정/정확한 조항 locator를 통합 보고서 v0.2에 반영
- PR #21 merge commit: `e11d376bab43ccc99bdf70549ad47eec57a01760`; PR #22: `20e503c1da2fe2f053630263a8c4942680ec1515`; PR #23: `b90a0ac07865c18d846323d843fef38b1123077a`; PR #24: `153033aa535775a0df568ad83876bff487d33404`; PR #26: `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`
- PR #26 CI: [Run #573](https://github.com/useformotor3/ai-discord-bot/actions/runs/44039961078), 138 passed / 1 xfailed; 9개 official source live fetch 및 Article 13(8) locator/quote canary 통과. merge commit 자체의 별도 run은 아직 미확인.
- PR #27 [프로젝트 기록/행동강령 동기화](https://github.com/useformotor3/ai-discord-bot/pull/27) 병합 완료; [Run #575](https://github.com/useformotor3/ai-discord-bot/actions/runs/44040949610)에서 138 passed / 1 xfailed 및 live source canary 재통과.
- PR #27 rollback refs: `safety/pre-merge-main-pr27-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`; `safety/post-merge-main-pr27-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b` (readback SHA 확인)
- PR #28 [최종 복구 체크포인트 동기화](https://github.com/useformotor3/ai-discord-bot/pull/28) 병합 완료; [Run #577](https://github.com/useformotor3/ai-discord-bot/actions/runs/44041626911) 138 passed / 1 xfailed 및 live source canary 통과
- PR #28 rollback refs: `safety/pre-merge-main-pr28-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; `safety/post-merge-main-pr28-2026-11-17` → `942e1e6b5f2887001279a96c21f94138d283a689` (readback SHA 확인)
- PR #29 [정오표 우선순위 검증](https://github.com/useformotor3/ai-discord-bot/pull/29) 병합 완료; [Run #596](https://github.com/useformotor3/ai-discord-bot/actions/runs/44043479661) 141 passed / 1 xfailed, 9개 source 및 Article 64(10)/67/13(8) live canary 통과
- PR #29 rollback refs: `safety/pre-merge-main-pr29-2026-11-17` → `9ad730c42de6451ce6942298e9b17e3e82a3ef62`; `safety/post-merge-main-pr29-2026-11-17` → `9c16724b8b72bd09d3492b19ff714602b235c66b` (readback SHA 확인)
- 최신 법적/이행 자료 반영: Commission Guidance C(2026) 5252 (2026-07-27), M/606 개정 C(2026) 7861 (2026-11-10), Regulation (EU) 2025/327 개정 범위 검토
- 제품 모델/통신 프로토콜/시장 공급 구조가 미제공되어 CRA 적용성 및 Annex III/IV 분류는 잠정 판단으로 유지
- PR #19/#20은 문서·추적표 경로만 변경했으며 운영 코드, workflow, state/history 및 원본 archive는 수정하지 않음
- CI: PR #19 Run #500 및 main push Run #502 success; PR #22 [Run #525](https://github.com/useformotor3/ai-discord-bot/actions/runs/44029944407) success. PR #21 Run #517은 최종 2개 문서 수정 전 커밋에서 success; 최종 head/merge run은 미확정. PR #22 merge commit 자체의 별도 run은 조회되지 않았음.

자동화 신뢰성 개선(P0/P1-B1/P1-B2)의 과거 구현·CI 결과는 역사적 엔지니어링 기준선으로 보존한다. 해당 결과를 CRA 법령·제품 적합성 검증으로 해석하지 않는다.

## 프로젝트 관리 문서

| 문서 | 목적 |
|---|---|
| [현재 상황판](PROJECT_STATUS_CURRENT.md) | 현재 상태, 위험, 실제 검증 결과, 다음 재개 지점 |
| [마스터 계획](MASTER_PLAN.md) | 전체 단계, 우선순위, 완료 기준 |
| [AI 행동강령](AI_RULEBOOK.md) | 조사·근거·코드·테스트·기록 규칙 |
| [세션 로그](SESSION_LOG.md) | 날짜별 실제 작업, 변경 범위, 테스트 결과 |

## 주요 기술 자료

- [LS메카피온 서보드라이브 CRA 제품군 예비 분석 보고서 v0.1](reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md) — 제품군 13개, CRA 적용성·Annex III/IV 예비 검토, 보안 위협·시험·증거 계획

- [CRA 공식 출처 수집·주장 추적 파이프라인 보고서](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md)
- [CRA 통합 규제·기술 준수 보고서 v0.1](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)
- [CRA 요구사항 추적표 v0.1 (CSV)](reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv)
- [서보 드라이브 인터페이스별 CRA 적용성 매트릭스 (CSV)](reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv)
- [CRA 원문 정정 보고서 인덱스 (#1–#38)](reports/CRA_CORRECTION_INDEX_2026-11-17.md)
- [운영 실행 관찰 및 데이터 무결성 확인](reports/PRODUCTION_RUN_OBSERVATION_2026-11-17.md)
- [조사 품질 감사](reports/RESEARCH_QUALITY_AUDIT_2026-11-14.md)
- [CRA 보고서 #28·#29 정정 기록](reports/CRA_CORRECTIONS_REPORTS_28_29_2026-11-14.md)
- [자동화 코드 개선 설계 및 테스트 계획](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- [테스트 실행 환경 감사](reports/TEST_EXECUTION_ENVIRONMENT_AUDIT_2026-11-14.md)
- [테스트 가이드](tests/README.md)

## 진행 원칙

1. 공식 법령·표준 원문을 우선하고 조항, URL, 확인일, 원문 인용을 기록합니다.
2. 법적 의무, 표준 요구사항, 공식 해석, 엔지니어링 권고, 미확인 가설을 분리합니다.
3. 조사 초안 생성과 출처/내용 검증을 구분합니다.
4. 중복 보고서를 양산하기보다 기존 자료를 검증·정정·통합합니다.
5. 통상적인 CRA 범위 코드·테스트·문서·CI 변경은 반복 승인 질문 없이 작업 브랜치와 PR로 진행합니다. 변경 전 기준점·영향·테스트·복구 경로를 확보하고, CI와 readback이 확인된 경우 병합합니다. force-push/history rewrite, 삭제·secret 변경, 운영 workflow 실행, 외부 부작용이 있는 작업은 별도 안전 확인 대상으로 둡니다.
6. 테스트 원본과 blob SHA가 일치하지 않으면 결과를 예비 검증으로만 기록합니다.
7. 운영 workflow를 테스트 목적으로 실행하지 않습니다.
8. 의미 있는 작업이 끝날 때 README, 상황판, 마스터 계획, 행동강령, 세션 로그와 관련 보고서를 동기화하고 GitHub에서 재조회합니다.

## 초기 테스트 실행 증거 — 2026-11-14 (과거 기준선)

- [GitHub Actions latest Run #3 — 21 passed](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938)
- 실행 commit: `dddba44a41851e9d0319ce9a91535a9d26145d92`
- 다섯 개 핵심 파일의 Git blob SHA 일치 확인 후 compileall 및 pytest 실행.
- 테스트 전용 workflow: [.github/workflows/tests.yml](.github/workflows/tests.yml)

## 다음 작업

1. Commission Guidance C(2026) 5252 PDF 원문/Annex와 M/606 결정 C(2026) 7861 Annex를 별도 수집·파싱하고 페이지 locator 및 SHA-256을 기록한다. 현재 source pack은 관련 URL만 기록하며 PDF/결정 Annex 본문은 미수집이다.
2. Article 13(8) 외에 Annex I Part I/Part II 및 핵심 Article의 실시간 locator·quote 검증을 추가한다.
3. CRA 요구사항 35개, 인터페이스 15개, 보안 통제·시험 36개를 source claim ID, 설계 통제, 시험 케이스 및 증거 링크와 교차 연결한다.
4. 실제 모델·회로·펌웨어·프로토콜·EU 공급 구조 자료가 확보되면 제품별 적용성, Annex III/IV 분류 및 Article 32 경로를 검증한다. 자료가 없으면 일반 참조 설계/잠정 판단으로 유지한다.
5. main merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`의 post-merge CI 여부를 확인하고, 문서·상황판·세션 로그·기계 로그를 최신 main에 맞춰 동기화한다.

자세한 재개 지점과 검증 한계는 [PROJECT_STATUS.md](PROJECT_STATUS.md)를 기준으로 합니다.

## 프로젝트 작업 로그

- [기계 판독형 프로젝트 로그](PROJECT_LOG.jsonl): 작업 이벤트를 JSONL로 기록합니다. 각 줄은 독립 JSON 객체이며 이벤트 ID, 날짜, 상태, 변경 파일, 검증 결과, 근거 링크, 한계 및 승인 범위를 포함합니다.
- [한국어 세션 로그](SESSION_LOG.md): 작업 배경과 판단, 사용자 승인, 검증 해석을 사람이 읽기 쉽게 기록합니다.
- `state.json` 및 `history.json`은 기존 자동화 런타임 데이터로 유지하며 프로젝트 작업 로그로 대체하거나 임의 수정하지 않습니다.


## 과거 테스트 fixture 작업 기록 — 2026-11-14
- 작업 브랜치: `test/failure-path-fixtures-2026-11-14`
- 기준 브랜치/커밋: `docs/cra-audit-and-project-control-2026-11-14` @ `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 목적: Discord/Git 실패 응답을 주입할 수 있는 mock fixture 및 strict xfail 회귀 테스트 추가
- 최신 확인 CI: [Run #11 — success, 23 passed / 5 xfailed](https://github.com/useformotor3/ai-discord-bot/actions/runs/43569359083)
- 변경 파일: `.github/workflows/tests.yml`, `tests/README.md`, `tests/conftest.py`, `tests/test_mock_infrastructure.py`, `tests/test_external_failure_paths.py`
- 운영 `main.py`, 운영 workflow `run.yml`, `state.json`, `history.json`은 변경하지 않았다.
- 상세 현황은 작업 브랜치의 `PROJECT_STATUS.md` 및 `SESSION_LOG.md`를 확인한다.


## 최신 원격 상태 — 2026-11-14 확인
- CI 검증 대상 commit: `27d2c69287631b041672b9989fdeeb3066f5ebb9` (Run #13); 문서 정리 전 HEAD
- 기준 브랜치: `docs/cra-audit-and-project-control-2026-11-14` @ `c6dfc5cee2485922b2313030dd9a5843e347afe7`
- 기준 브랜치 대비: 23 ahead / 0 behind (Run #13 시점)
- `main` 대비: diverged, 134 ahead / 58 behind (Run #13 시점; 자동화 커밋으로 변동)
- 최신 확인 테스트 증거: [Run #13](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208), 30 passed / 5 xfailed. Run #13이 새 fixture 7개 case를 포함한 변경 소스 SHA와 compileall을 검증했다.
- 이 문서 앞부분의 과거 브랜치/Run #3 요약은 당시 기록이다. 현재 기준은 이 최신 상태 절과 `PROJECT_STATUS.md`를 따른다.

## 최신 상태 스냅샷 — 2026-11-14
- 문서 갱신 전 작업 브랜치 HEAD: `11c89c2bf513c0562aa0451caf38effae2041e26`
- 기준 docs commit `c6dfc5cee2485922b2313030dd9a5843e347afe7` 대비 24 ahead / 0 behind.
- `main` 대비 diverged 135 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- Run #13에서 검증된 테스트 commit은 `27d2c69287631b041672b9989fdeeb3066f5ebb9`이며, 그 이후 변경은 관리 문서와 로그다.
- `main.py` blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43`; 테스트 브랜치의 기준 commit 대비 변경 파일 목록에도 `main.py`는 없다.
- 문서 저장 후 ahead/behind는 다시 증가할 수 있으므로 다음 작업 시작 시 재조회한다.


## P1-B 정책 설계 최신화
- [P1-B 전송·저장·동기화 정책 명세](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)
- Discord 429/timeout/POST 중복 가능성, chunk 부분 성공, state/history transaction, Git 원격 동기화 확인 정책을 공식 기술 문서와 대조해 정리했다.
- 구현 승인이 아니다. 운영 코드 변경 전 별도 제안·승인이 필요하다.


## P1-B 테스트 정책 정합성 및 최신 CI
- 503 자동 재시도 xfail을 중복 방지 관점의 `delivery_unknown` 기대 동작으로 변경했다.
- Discord 401/403/404 영구 실패·재시도 금지 기대 테스트 3 case를 추가했다.
- [Run #15 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842), commit `b2e108768be08f06e85af154835424682337ebf5`: **30 passed / 8 xfailed**.

## 최신 상태 재조회 — 2026-11-14
- 직전 HEAD: `5b3cd6ca70dcff7a50f4ad4c20f834592c9e8ca9`.
- 기준 docs commit 대비 28 ahead / 0 behind.
- main 대비 diverged 139 ahead / 59 behind; main HEAD `8034668f45496ef532bfdfb865b29d4149cf2a94`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 마지막 테스트 코드 검증은 Run #15, commit `b2e108768be08f06e85af154835424682337ebf5`: 30 passed / 8 xfailed. 그 이후 변경은 문서/로그뿐이다.
- main.py SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지.


## 과거 승인 게이트 기록 — P1-B1 (이후 승인·구현 완료)
- P1-B는 단계별로 분리했다. 우선 제안은 **P1-B1 Discord 전송 결과 신뢰성**만이다.
- 변경 파일, 기대 동작, 테스트, 롤백 및 제외 범위는 [개선 설계 보고서](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md)의 §18을 참조한다.
- P1-B1은 main.py 운영 코드 변경이므로 별도 승인 전까지 구현하지 않는다.

## 최신 브랜치 상태 — 2026-11-14
- 조회 HEAD: `f5a83e3c8e04a43b6e38a593c7b01bd360583b3f`
- 기준 docs commit 대비 30 ahead / 0 behind.
- main 대비 diverged 141 ahead / 60 behind; main HEAD `1dff09ffa9722119f6fb0847a51b6c87c322d114`, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 마지막 테스트 검증 commit `b2e108768be08f06e85af154835424682337ebf5`, [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842): 30 passed / 8 xfailed. 이후 테스트 코드 변경은 없고 문서만 갱신했다.
- main.py blob SHA `470ac101d5cc4fdb2c5077d5468ef00327af3d43` 유지.


## P1-B1 Discord 전송 신뢰성 구현 — 2026-11-16
- 사용자 승인 범위 P1-B1을 작업 브랜치에서 구현했다.
- Discord webhook POST에 connect/read timeout (3.05, 10), wait=true, HTTP 응답 및 message ID 확인을 추가했다.
- 429 Retry-After, ConnectTimeout 제한 재시도, 400/401/403/404 영구 실패, 5xx/ReadTimeout/ConnectionError 전달 불명확 상태, chunk partial 처리를 구현했다.
- [GitHub Actions Run #18](https://github.com/useformotor3/ai-discord-bot/actions/runs/43808285335): 43 passed, 1 xfailed; source SHA 6개 및 compileall 통과.
- Run #17은 main.py SHA pin 불일치로 실패했고 Run #18에서 정정 후 통과했다. 실패 이력은 보존한다.
- 이 P1-B1 작업 시점에는 P1-B2/B3/B4와 운영 main 병합이 미실행이었다. P1-B2는 이후 별도 승인으로 구현·검증됐으며, P1-B3/B4는 여전히 보류다.


## 이전 원격 브랜치 비교 스냅샷 — 2026-11-16 (이후 갱신됨)
- 작업 브랜치 HEAD(비교 시점): bc0d05d45b63e9039a87abf6847c9daccc0124f3.
- 기준 docs commit c6dfc5cee2485922b2313030dd9a5843e347afe7 대비 36 ahead / 0 behind.
- 운영 main 대비 diverged: 147 ahead / 610 behind. main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- main.py SHA: 작업 브랜치 4b631c04e34b2b3bbade0aa9301e7d48578a1e03, main 86a7731aad5de8d75581fc953bcea2c44adf2f2b. 브랜치에는 P0/P1-A 및 P1-B1 변경이 있으나 main은 다른 시점의 코드다.
- 610 behind의 큰 차이가 있으므로 main으로 직접 PR/merge하지 않는다. 먼저 두 브랜치의 commit/file 차이, 자동 생성 보고서와 데이터 영향, 충돌을 별도 통합 감사해야 한다.
- merge/rebase/PR merge/운영 배포는 수행하지 않았다. 비교 수치는 조회 시점 기준이다.


## 최신 원격 비교 스냅샷 — 2026-11-16
- 비교 대상 작업 브랜치 HEAD: 934319884561ac772e7cc805a3ae58415742ab07.
- 기준 docs commit 대비 38 ahead / 0 behind.
- main 대비 diverged 149 ahead / 610 behind; main HEAD 8357da3abe3b87ca0e7a2fa50f862b693c0a226c, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- 문서 갱신 커밋 이후 ahead 수가 증가하므로 이 수치는 조회 시점 스냅샷이다.
- 610 behind로 직접 병합하지 않고 통합 감사 전까지 병합·리베이스를 보류한다.


## 2026-11-16 통합 감사 최신 결과
- 현재 작업 브랜치 HEAD: `a7f2cd285ad89df2d0c67f14acb036e8e42a73d9`; main HEAD: `a7f2cd285ad89df2d0c67f14acb036e8e42a73d9`; merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 작업 브랜치 기준 base 대비 41 ahead / 0 behind, main 대비 152 ahead / 657 behind.
- recursive Git tree 비교(양쪽 truncated=false): merge-base 1,600 entries, main 2,257 entries. main 고유 추가 657개는 전부 `research_archive/` 아래 자동 생성 보고서이며, 삭제 0개, 변경 경로는 `history.json`, `state.json`, `research_archive/` 3개.
- main history.json 2,249개 객체, merge-base 1,592개 객체. main state.json count=110/date=2026-11-16, merge-base count=29/date=2026-11-14.
- main.py는 merge-base와 동일 SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치는 `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`. 운영 run.yml은 merge-base와 동일 SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- 운영 state/history/archive, main.py, run.yml을 변경하지 않았다. merge/rebase/PR merge/운영 실행 없음.
- 상세 근거: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16.md`. 결론: 데이터 보존·코드 분리 통합안과 별도 승인이 있기 전까지 통합 보류.


## 2026-11-16 최신 main 자동 아카이브 반영 스냅샷
- 감사 도중 main 자동 실행 Auto-archive #111로 main HEAD가 `31e0f8137630630ee30ea55add039b571f2c6801`로 이동했다. 작업 브랜치 HEAD는 `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff`.
- 최신 비교: 작업 브랜치 base 대비 42 ahead / 0 behind, main 대비 153 ahead / 658 behind.
- 최신 recursive tree 비교(양쪽 truncated=false): base 1,600 entries, main 2,258 entries. 추가 658개(모두 research_archive), 삭제 0개, 변경 파일 history.json/state.json.
- 최신 main history.json 2,250개 객체, state.json count=111. main.py 및 운영 run.yml은 merge-base와 동일 SHA.
- 앞선 수치는 조회 시점 스냅샷이며 본 최신 수치로 대체한다. 상세 보고서와 PROJECT_LOG의 정정 이벤트 참조.


## 이전 통합 감사 스냅샷 — 2026-11-16 (KST, 이후 갱신됨)
- 작업 브랜치 HEAD `227e3298066af4bda83fb0713fc1d57c749ee8c6`; 운영 main HEAD `036334dd2665752c2e6ddb024001771cff4064c5`; merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- 작업 브랜치 기준 base 대비 44 ahead / 0 behind, main 대비 155 ahead / 660 behind.
- recursive tree 비교(양쪽 truncated=false): merge-base 1,600 entries, main 2,260 entries. archive 660개 추가, 삭제 0개, history/state 변경 2개.
- main history.json 2,252개 객체, state.json count=113. main.py SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`, 작업 브랜치 main.py SHA `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 자동 조사/아카이브 운영은 main에서 계속된 흔적이 있으나 P0/P1-A/P1-B1 신뢰성 개선은 작업 브랜치에만 존재한다. 운영 배포로 간주하지 않는다.
- 상세 감사: `reports/BRANCH_INTEGRATION_AUDIT_2026-11-16_REFRESH.md`.
- 통합 전략: `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`.


## 2026-11-16 재개 시점 원격 상태 재확인
- 작업 브랜치 HEAD: `7383385e7dd8b7abcdba5c72e70ce5cf78dfb2a7` (조회 기준).
- 운영 main HEAD: `c2936e9484a44d76dc60ff811e4b904c89cf742f` (Auto-archive: Research report #124).
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 기준 작업 브랜치 157 ahead / 671 behind, status diverged.
- 운영 main의 `state.json`: date `2026-11-16`, count `124`, blob SHA `e8b5d8a0797f985de437e62bdce4e399bb68de4a`.
- 운영 main의 `history.json`: top-level object 2,263개, blob SHA `c127452fadb3d9aff9074b8ac3ac2bbdd42943fc`.
- 운영 main의 `main.py` SHA `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치 SHA `4b631c04e34b2b3bbade0aa9301e7d48578a1e03`.
- 운영 `.github/workflows/run.yml` SHA `65a8cadc8eac593f551e390698e367b1d161ecf1`.
- recursive tree 전체 비교는 이번 조회에서 수행하지 못했으므로 archive 추가/삭제 수는 미확정이다. compare API의 파일 목록을 전체 경로 목록으로 간주하지 않는다.
- 운영 main, 운영 workflow, state/history/archive 변경 없음. merge/rebase/PR merge/운영 실행/Gemini·Discord 외부 호출 없음.
- P1-B2는 설계 완료·구현 별도 승인 대기. P1-B3/B4는 보류 상태 유지.


## 통합 전략 감사 — 2026-11-16
- merge-base 기준 main은 archive 678개만 추가하고 history/state를 갱신했으며 삭제는 0개다.
- 작업 브랜치는 main.py 수정 및 23개 경로 추가, 삭제 0개다. 따라서 3-way PR 통합 시 운영 archive/history/state 보존을 기대할 수 있다.
- P1-B2 recovery target allowlist 보강 후 CI Actions 43851438733에서 70 passed / 1 xfailed.
- PR 생성·merge·운영 배포는 별도 승인 전 수행하지 않는다.
- PR 비교 변경 경로: 24개(23개 추가 + main.py 수정). state/history/archive/run.yml 변경은 없어야 한다.
- 상세: [통합 전략 감사 보고서](reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md).


## 2026-11-16 — 최신 원격 branch/main 비교
- 작업 브랜치 HEAD(이 스냅샷 기준): `02fde2489323f9f553405e014fac20d75d13a7fa`.
- 운영 main HEAD: `267d97478b785e6bb268e224a70dbad6631cf43e` (Auto-archive #131).
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 221 ahead / 678 behind, diverged; PR compare 변경 파일 24개.
- main state count=131, history=2,270, archive=2,270, 참조 누락 0.
- 이 ahead 수치는 이 스냅샷 commit 기준이며, 로그/문서 추가 commit 이후 증가한다. main 자동 아카이브도 계속 변하므로 PR 직전 재조회한다.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지. PR/merge/운영 실행은 수행하지 않았다.



## 2026-11-16 — PR 사전 검사 결과 (원격 HEAD 고정)
- 운영 main HEAD: `267d97478b785e6bb268e224a70dbad6631cf43e` (Auto-archive #131).
- 작업 브랜치 HEAD(검사 기준): `be3e243a7cccaf8cf26b2ced453b733098debadd`.
- merge-base: `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 228 ahead / 678 behind.
- GitHub compare의 전체 변경 경로 24개: 신규 23개 + `main.py` 수정 1개, 삭제 0개.
- 변경 경로에 `state.json`, `history.json`, `research_archive/**`, 운영 `.github/workflows/run.yml` 없음.
- merge-base/main의 `main.py` blob SHA 모두 `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; main 쪽은 분기 이후 이 파일이 바뀌지 않았다. 작업 브랜치 main.py만 `fa8679b758916ba8a446bae41b9ec1b40328da09`로 변경됐다. 따라서 현재 확인 범위에서 main.py의 양쪽 동시 수정 충돌 요인은 없다.
- 테스트 workflow SHA `6a5bee0785eccc1f1b8074b80761b1b2a772d3c0`; `pull_request: branches: [main]`, `permissions: contents: read`, checkout `persist-credentials: false`.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지.
- Actions #43851438733은 성공(70 passed / 1 xfailed). 실행 HEAD는 `2b2645b23876378a6c384c8da819de84104ac49a`; 이후 변경은 문서/로그만이며 검증 대상 main.py, persistence.py, 테스트 파일, test workflow의 blob SHA가 동일함을 재확인했다.
- PR은 아직 생성하지 않았으므로 GitHub의 실제 `mergeable` 결과와 PR-triggered CI는 미확인. 현재는 merge-base/tree 및 파일 경로 사전 검사 결과이지 최종 충돌 판정이 아니다.
- PR 생성, merge/rebase/force-push, 운영 workflow/data 변경, 실제 Gemini/Discord 호출은 수행하지 않았다.



## 2026-11-16 — main 자동 아카이브 #132 이후 최신 재조회
- 운영 main HEAD `7296fcd9261a3171fc2cc8a5a51bde73dcf052cb` (Auto-archive #132); 작업 브랜치 감사 기준 HEAD `74b2c1281fe89a96b94ba13fbac74189350c4aa8`.
- merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; compare 229 ahead / 679 behind.
- 운영 state count=132, history=2,271, archive=2,271, history→archive 참조 누락 0.
- main recursive tree 2,276 blobs; tree 응답 truncated=false.
- PR 변경 경로 24개(23 added + main.py modified), 삭제 0. 보호 경로(state/history/archive/run.yml) 변경 없음.
- main.py merge-base/main blob SHA 동일 `86a7731aad5de8d75581fc953bcea2c44adf2f2b`; 작업 브랜치 blob SHA `fa8679b758916ba8a446bae41b9ec1b40328da09`. 분기 이후 main.py의 양측 동시 수정은 확인되지 않음.
- PR 미생성 상태이므로 GitHub mergeable 및 PR-triggered CI는 아직 미확인. 실제 통합 가능 여부는 PR 생성 후 재검증한다.
- 운영 run.yml SHA `65a8cadc8eac593f551e390698e367b1d161ecf1` 유지.


## 2026-11-16 — Draft PR #1 생성 및 PR CI 검증
- Draft PR: https://github.com/useformotor3/ai-discord-bot/pull/1
- 대상: `main` ← `feature/p1-b2-atomic-persistence-2026-11-16`; PR head `01e7cf50436f35d9eddb931ae4e1d177af805387`, PR 생성 시 base main `38abb075ebe0f7180abaebc4da52e2f18ea28915`.
- 생성 직전 compare: 230 ahead / 700 behind, merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`; 변경 24개(23 added + main.py modified), 삭제 0.
- 보호 경로 `state.json`, `history.json`, `research_archive/**`, 운영 `.github/workflows/run.yml`는 PR 변경 경로에서 제외됨.
- PR 생성 후 GitHub 재조회: open, draft=true, merged=false, mergeable=true.
- PR-triggered Actions Run #32 (`43869220252`) 성공: source integrity, compile, 전체 pytest 단계 완료. [Run #32](https://github.com/useformotor3/ai-discord-bot/actions/runs/43869220252).
- 이전 코드 검증 Run #43851438733은 70 passed / 1 xfailed였으며 PR-triggered run #32의 개별 테스트 수치는 job summary에서 확인되지 않아 별도 숫자로 단정하지 않는다.
- 현재 PR은 검토용 Draft이며 merge/rebase/운영 반영은 하지 않았다. main의 지속적인 자동 아카이브로 base가 움직일 수 있으므로 병합 직전 재비교가 필요하다.


## 2026-11-16 — 상시 진행 승인 및 복구 우선 운영 기준
- 사용자는 매 단계별 승인 질문 없이 목표 달성에 필요한 작업을 계속 진행하도록 상시 승인했다. 안전 통제·검증·복구 절차는 유지한다.
- AI_RULEBOOK.md §18에 변경 전 체크포인트, safety/ 백업 브랜치, merge commit, 운영 데이터 사전 백업/복원, 실패 시 revert/복구 절차를 명문화했다.
- 현재 main 백업 safety/pre-merge-main-2622e332 → 2622e332d6a3defd2079ccad3af36970001de5c1; feature 백업 safety/pre-merge-feature-eba3aeb → eba3aeb5710dcc6507623d56d586a619e9a4fc46.
- Draft PR #1: https://github.com/useformotor3/ai-discord-bot/pull/1. main은 2622e332d6a3defd2079ccad3af36970001de5c1까지 진행. 최신 compare는 231 ahead / 703 behind, merge-base f9a12a5778f5fa1d907201ab2931d20ca2656bb7.
- PR mergeable 값은 조회 시점에 변동했고 PR base SHA 응답도 main HEAD와 일치하지 않는 스냅샷을 반환했다. 최신 base 기준 통합 검증이 완료된 것으로 보지 않는다.
- 코드 백업 ref는 만들었지만 운영 데이터 snapshot/restore 절차는 아직 검증되지 않았다. 이를 완료하고 복원 리허설하기 전에는 신규 코드의 첫 운영 실행을 하지 않는다.

## 2026-11-16 — 운영 데이터 immutable baseline #158
- 기준 commit 4cf0e708b28a343898af00d01521044dfb9a1987 (Auto-archive #158).
- 동일 SHA 검사: state count=158, history=2,297, archive=2,297, 참조 누락 0, tree 2,305 entries.
- backup safety/pre-merge-main-4cf0e70가 같은 SHA를 가리킨다.
- U+200B가 앞에 붙은 별도 state 파일(date 2026-06-07,count 0)은 조사 전까지 보존한다.
- moving-ref 조회에서 보인 불일치 1건은 immutable SHA 재검사에서 재현되지 않았다.
- 상세 감사: reports/ROLLBACK_AND_DATA_BASELINE_AUDIT_2026-11-16.md.

## 2026-11-16 — 운영 rollback guard 구현 및 검증
- production workflow에 실행 전 고유 safety/data-pre-run checkpoint, 실행 직렬화, 실행 후 무결성 검증/조건부 데이터 복구를 추가했다.
- operational_guard.py 및 테스트 추가. local bare Git remote로 정상 전이/복구 commit/미push 거부/quota no-op을 검증.
- 최종 PR CI Run #43874801395: 86 passed, 1 xfailed, compileall 성공. https://github.com/useformotor3/ai-discord-bot/actions/runs/43874801395
- 최신 main #161 baseline: f5b5a112ec72b01f8b3f91f734b8d755dde416c6; state count 161, history 2,300, archive 2,300, missing refs 0.
- main backup safety/pre-merge-main-f5b5a11, feature backup safety/pre-merge-feature-8ad2364. 상세 reports/ROLLBACK_AND_DATA_BASELINE_AUDIT_2026-11-16.md


## 2026-11-16 — rollback guard final CI and main #162 baseline
- [Draft PR #1](https://github.com/useformotor3/ai-discord-bot/pull/1) includes production run.yml pre-run checkpoint and guarded restore.
- Latest feature head at code verification: abee2a88f7e0bbfad0ad483c6b50cea63e26b871; main #162: adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890.
- CI Run #43875746973 success: 87 passed, 1 xfailed, compileall and source SHA checks passed. https://github.com/useformotor3/ai-discord-bot/actions/runs/43875746973
- main #162 immutable baseline: state count 162, history 2,301, archive 2,301, missing refs 0.
- main backup safety/pre-merge-main-adf74ea readback SHA exact. Feature backup safety/pre-merge-feature-abee2a8 readback exact.
- Production workflow has not yet been executed; first execution remains external-effect operation. The workflow now snapshots before run and verifies/restores data after run.

## 2026-11-16 — PR #1 통합 완료
- PR #1 merged: https://github.com/useformotor3/ai-discord-bot/pull/1
- merge commit 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e (main #162 + feature d48ae1c9b655d7384aff497c9d17168a5d0b25c5).
- Post-merge safety branch safety/post-merge-main-6fd03ef, readback exact SHA.
- Push CI Run #43876347620 success: 87 passed, 1 xfailed, compileall success.
- Merge 직후 same-SHA data integrity: state count 162, history 2,301, archive 2,301, missing refs 0. state/history blob SHA는 pre-merge main #162와 동일.
- Merge 자체로 production workflow는 실행되지 않음(현재 trigger repository_dispatch/workflow_dispatch). 실제 Gemini/Discord 호출 없음.
- 다음: 첫 production run 전 snapshot branch 및 post-run guard 동작을 실제 workflow에서 관찰한다.


## 2026-11-17 — GitHub 자동화 점검 및 체크포인트 누적 개선
- 원격 Actions 최근 20건은 조회 당시 completed/success였으나, #2412는 현재 작업 중 main 커밋이 추가된 경합으로 실패했다.
- #2412: 로컬 보고서 #235 commit 생성, Discord 2/2 chunks 전송, Git push는 non-fast-forward(fetch first) 거부. operational_guard는 remote main 불일치로 자동 복구를 거부했다. 보고서 #235는 원격 history/archive/state에 반영되지 않았다.
- 실행별 safety/data-pre-run 브랜치 94개 확인. 성공 실행 이후에도 무제한 누적되는 구조를 결함으로 분류.
- main 변경 전 백업: safety/pre-checkpoint-prune-1abfcfb → 1abfcfb26a8b414dc75eb584082ed35cab0d6412.
- main commit b89f2bf58752045361fa088a6fc4311ba8798fcb에 성공 실행에서만 최근 30개 체크포인트를 남기고 현재 baseline ref를 보호하는 pruning step 및 스크립트를 추가했다.
- 첫 CI Run 43959203356: compileall 통과, pytest 96 passed / 1 failed / 1 xfailed. 실패는 보호된 오래된 ref 테스트의 기대값 오류이며 수정 후 재검증한다.
- 아직 실제 checkpoint pruning은 실행되지 않았다. CI 통과 후 다음 정상 운영 실행에서만 실행되도록 구성했다.
- 이후 main 변경은 활성 production run 종료 확인 후 수행한다. #2412 Discord 전송은 회수할 수 없으므로 후속 보고서 count 중복 가능성을 추적한다.


## 2026-11-17 운영 안정화 업데이트
- 체크포인트 보존 정책은 운영 run #2431에서 실제 정리 성공을 확인했다. 사전 실행 백업 브랜치는 30개 유지.
- 추가 개선: KST 기준 일일 카운트, Gemini 모델 404 즉시 fallback, Git push 실패 fail-closed.
- 상세 설계·근거·검증 한계: reports/OPS_TIMEZONE_MODEL_GIT_FAILURE_FIX_2026-11-17.md.

- KST/모델/Git 저장 실패 개선 CI: Run #59 성공(99 passed, 1 xfailed). Run #58은 테스트의 구형 모델명 기대값 2건으로 실패했으며 수정 후 #59에서 통과.


## 2026-11-17 운영 검증 업데이트
- KST 기준 state date=2026-11-17, count=4 확인.
- history 2,397개 파싱 및 당일 최신 archive 4개 원격 존재 확인.
- 운영 Git archive 저장은 확인했으나 상세 Job 로그가 없어 실제 Gemini model ID, operational_guard, checkpoint pruning, Discord 응답은 미확인.
- 상세: [운영 실행 관찰 및 데이터 무결성 확인](reports/PRODUCTION_RUN_OBSERVATION_2026-11-17.md).


## 2026-11-17 CRA 보고서 #4 정정 감사
- 원본은 보존하고 별도 정정 기록을 추가했다.
- 핵심 정정: CRA Annex I Part I (2)(m), IEC 62443-4-2 CR 4.2, NIST SP 800-88 Rev.2 적용.
- 상세: [CRA 보고서 #4 정정 및 기술 근거 감사](reports/CRA_CORRECTION_REPORT_4_2026-11-17.md).


## 2026-11-17 CRA 보고서 #3 정정 감사
- 원본은 보존하고 CRA Article 13(8)/(9), Annex I Part I (2)(c), Part II (2)/(4)/(8)을 공식 EUR-Lex 원문과 대조해 정정 기록을 추가했다.
- 주요 정정: Article 13(8)은 지원 기간, 보안 업데이트 분리 제공은 Annex I Part II (2), 무상 제공은 Part II (8), 장기 이용 가능성은 Article 13(9).
- 상세: [CRA 보고서 #3 정정 및 기술 근거 감사](reports/CRA_CORRECTION_REPORT_3_2026-11-17.md).


## 2026-11-17 CRA 보고서 #2 정정 감사
- 원본은 보존하고 Article 13–16, 69, 71 및 Annex I/II/VII를 공식 EUR-Lex 원문과 대조했다.
- Article 11은 General product safety이며 CVD 근거가 아니다. CVD는 Article 13(8)/(17), Annex I Part II (5)/(6), Annex II (2). 의무 신고는 Article 14.
- actively exploited vulnerability: 24h/72h/시정조치 가용 후 14일 final report. Severe incident: 24h/72h/incident notification 후 1개월 final report.
- Article 14는 2026-09-11부터 적용.
- 상세: [CRA 보고서 #2 정정 및 기술 근거 감사](reports/CRA_CORRECTION_REPORT_2_2026-11-17.md).


## 2026-11-17 CRA 보고서 #1 정정 감사
- 원본은 보존하고 Article 13(8), Annex I Part I (2)(c)/(f), Part II (5)–(8), Annex II/VII를 공식 EUR-Lex 원문과 대조했다.
- Article 11은 General product safety. 지원 기간은 Article 13(8), 무상 보안 업데이트는 Annex I Part II (8).
- CVD 정책/제보 연락처/안전한 배포는 Annex I Part II (5)–(7), Article 13(17), Annex II (2).
- 디지털 서명과 STO 연계 업데이트 설치는 특정 법정 구현 방식이 아니라 제품별 엔지니어링 검증 항목.
- 상세: [CRA 보고서 #1 정정 및 기술 근거 감사](reports/CRA_CORRECTION_REPORT_1_2026-11-17.md).
## 2026-11-17 최신 운영 안정화 및 조사 품질

- [운영 자동화 품질·실행 주기 감사](reports/PRODUCTION_AUTOMATION_QUALITY_AND_CADENCE_AUDIT_2026-11-17.md)
- CRA 원본 #33–#38 정정: [#33](reports/CRA_CORRECTION_REPORT_33_2026-11-17.md), [#34](reports/CRA_CORRECTION_REPORT_34_2026-11-17.md), [#35](reports/CRA_CORRECTION_REPORT_35_2026-11-17.md), [#36](reports/CRA_CORRECTION_REPORT_36_2026-11-17.md), [#37](reports/CRA_CORRECTION_REPORT_37_2026-11-17.md), [#38](reports/CRA_CORRECTION_REPORT_38_2026-11-17.md)
- PR #10 merge: EUR-Lex official-link gate 및 최근 30개 archive 기반 duplicate-topic suppression. CI #455: 101 passed, 1 xfailed.
- 외부 5분 dispatch를 hourly schedule로 바꾸는 cadence PR은 검증 후 병합 예정. 원본 state/history/archive는 보존한다.

- 운영 Run `44016487535` 실패 원인: Gemini Free Tier 20 requests/day 초과(429) + fallback 503. cadence PR에서 3시간 schedule, 모델당 최대 2회, quota/503/품질 거부 no-op 처리를 추가했다.
## 운영 안정화 최종 상태 — 2026-11-17

- PR #10: official EUR-Lex link validation + duplicate-topic gate; CI 101 passed, 1 xfailed.
- PR #11: repository_dispatch 제거, 3-hour cadence, quota-aware retries/no-op; CI 103 passed, 1 xfailed.
- PR #12: failure-path recovery guard, checkpoint rollback, guard-gated pruning, persist-before-Discord; CI 105 passed, 1 xfailed.
- Main merge head: `bef260a29481320de3eae9cafe4a6f907e38ead0`.
- Production data unchanged after quota failure: state count 38, history 2,431; original archives preserved.
- First three 3-hourly production runs remain the next live validation checkpoint.

## CRA correction archive — #1–#38
- [Master index](reports/CRA_CORRECTION_INDEX_2026-11-17.md)
- 원본 archive는 보존하고 법령 근거·조항·인용 오류는 별도 correction report로 관리한다.
- 이번 branch는 #5–#21 정정 문서 통합과 #22–#32 신규 정정을 포함한다. PR #14 CI/merge 대기.

## CRA source correction set — complete
- [CRA correction index #1–#38](reports/CRA_CORRECTION_INDEX_2026-11-17.md)
- All 38 correction reports are now present on main. Original auto-archive files remain unchanged.
- PR #14 merged: `6994e4828a03482713f7990c7f82036bacfe4772`; CI #474: 105 passed, 1 xfailed.

## 보존된 과거 산출물 — 기능안전 (현재 비활성 범위)

아래 파일은 2026-11-17 과거 작업의 기록 보존을 위해 main에 남아 있습니다. 현재 CRA 프로젝트의 활성 작업 범위에는 포함되지 않으며, 별도 재개 지시 전에는 후속 작업하지 않습니다.

- [SIL 3 벤치마킹 보고서](reports/SIL3_SERVO_DRIVE_BENCHMARK_REPORT_2026-11-17.md)
- [비교 매트릭스 CSV](reports/SIL3_SERVO_DRIVE_BENCHMARK_MATRIX_2026-11-17.csv)
- [하드웨어 블록 설계](design/SIL3_SERVO_DRIVE_HARDWARE_BLOCK_DESIGN_2026-11-17.md)
- [요구사항 추적성 매트릭스](reports/SIL3_SERVO_DRIVE_REQUIREMENTS_TRACEABILITY_2026-11-17.md)
- 역사적 반영 기록: PR #16, merge commit `34449753857c6ab004271f69aac19867a7aed1fa`, CI Run #488 (105 passed, 1 xfailed). 이는 당시 자동화 CI 결과이며 기능안전 인증이나 설계 적합성 승인을 뜻하지 않습니다.


## 최신 CRA 공식 문서 감사 — 2026-11-17

- [Commission Guidance C(2026) 5252 및 M/606 C(2026) 7861 Annex 감사](reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md): PDF text layer의 주요 조항·페이지 locator 및 Annex I 41개 표준 주제/기한 1차 확인.
- 원본 PDF 바이너리 다운로드 및 SHA-256은 아직 미확인이다. PDF 텍스트 내용 감사와 바이너리 무결성 검증을 구분한다.
- 현재 작업 브랜치: `cra/official-annex-audit-2026-11-17`; 운영 `main.py`, workflow, state/history/archive, 운영 Gemini/Discord 실행은 변경하지 않았다.


## PR #30 병합 및 검증

- [PR #30 CRA Guidance/M/606 Annex 감사](https://github.com/useformotor3/ai-discord-bot/pull/30) 병합 완료. Merge commit: `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`.
- [Actions Run #610](https://github.com/useformotor3/ai-discord-bot/actions/runs/44050954456): **141 passed, 1 xfailed**, compileall, exact source blob identity, 9개 official source live canary 및 Article 13(8) locator/quote 통과.
- 복구 기준점: `safety/pre-merge-main-pr30-2026-11-17` → `80245d9e132380a10581612c031f87869993b98d`; `safety/post-merge-main-pr30-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`. main과 post-merge ref는 compare 결과 identical.
- 원본 Guidance/M/606 PDF 바이너리 SHA-256과 M/606 item 18 날짜는 미확인으로 남긴다.


- PR #31 사후 상황판 동기화 병합: `24312166b892127e845721793b1abfee4d91f9c2`; [Run #618](https://github.com/useformotor3/ai-discord-bot/actions/runs/44051283237) success, 141 passed / 1 xfailed. Pre/post refs: `safety/pre-merge-main-pr31-2026-11-17` → `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`; `safety/post-merge-main-pr31-2026-11-17` → `24312166b892127e845721793b1abfee4d91f9c2`; post ref and main compare identical.


## CRA Guidance 추적 및 원문 PDF 검증 자동화 — 2026-11-17

- [Commission Guidance claim register](reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv): G-001~G-013 비구속적 설명과 문단/페이지·35개 요구사항·15개 인터페이스·36개 SEC 통제 연결.
- [공식 Guidance/M/606 Annex 감사](reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md): 41개 M/606 표준화 주제와 CRA 관련 해석.
- [PDF 원문 취득/해시 도구](cra_pdf_sources.py): Commission URL 우선, allowlist 검증된 Commission-hosted transition-pathways mirror fallback, PDF magic/header/marker 검증, raw-byte SHA-256 및 page count, CI artifact 저장.
- 현재 작업 브랜치: `cra/guidance-claim-mapping-2026-11-17`; PR/CI 검증 전. PDF binary hash 취득 결과는 CI artifact를 확인한 후에만 확정한다.


- [PDF source provenance manifest](reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json): Guidance mirror SHA-256, Commission M/606 Annex SHA-256, PDF page counts, extracted-text hashes, CI artifact digest and M/606 item 18 visual confirmation.
- M/606 item 18 deadline confirmed visually as `31/01/2027` on PDF printed page 3. Guidance binary is Commission-hosted transition-pathways mirror (Commission primary byte identity remains unverified).


- 최종 재검증 [Run #669](https://github.com/useformotor3/ai-discord-bot/actions/runs/44052967754): **148 passed / 1 xfailed**, compileall·source blob identity·PDF 2종 취득/해시·artifact upload·공식 HTML source 9건·Article 13(8) locator/quote 모두 통과.
- 최신 PDF artifact ID `14315096266`, ZIP SHA-256 `82e86c3347413bc6f210a7403939141679c34e5ad738822043af87fc5c2290c`; PDF별 raw hashes는 provenance manifest 참조.


- Final branch-head verification [Run #690](https://github.com/useformotor3/ai-discord-bot/actions/runs/44053390736): **148 passed / 1 xfailed**, compileall, source blob pins, PDF and HTML live canaries all pass. Latest artifact #14315106623 ZIP SHA-256 `da2f0e5fbfb5f5fa66360a2faa5af3d85821d3b7269885e34e1a3115f37cd3e2` reverified after download.


- Latest branch-head CI [Run #702](https://github.com/useformotor3/ai-discord-bot/actions/runs/44053693177): 148 passed / 1 xfailed; all source and PDF/HTML canaries passed. Artifact #14314174227 was downloaded and rehashed; ZIP digest `8fddbba46ccf9b0901b36d88ce27d79817ac620f9fabf37a8b6beefe5dfcaa82` matches GitHub metadata.


## PR #33 병합 — CRA Guidance 및 PDF 원문 검증

- [PR #33](https://github.com/useformotor3/ai-discord-bot/pull/33) squash merge 완료. Merge commit `50e4784de60430bb2b8c70ca06b41627d75379ae`.
- [Run #713](https://github.com/useformotor3/ai-discord-bot/actions/runs/44054006627): 148 passed / 1 xfailed; PDF 2종·HTML 공식 출처 9종 live canary 통과.
- Pre/post refs: `safety/pre-merge-main-pr33-2026-11-17` → `16b5d2e732e9f5f158d2b79aa9c0c62f0488fc92`; `safety/post-merge-main-pr33-2026-11-17` → `50e4784de60430bb2b8c70ca06b41627d75379ae`; post ref와 main compare identical.
- Guidance Commission-hosted transition-pathways mirror SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; M/606 Commission Annex SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`. Commission Guidance primary byte identity는 미확인.


## CRA 추적성 무결성 자동 검증

- `cra_traceability.py`는 G-001~G-013 claim register와 15 interface / 35 requirements / 36 SEC control matrix의 참조를 검사한다.
- M/606 Annex I 후보 항목 범위(1–41), Guidance 비구속적 분류, PDF raw/text SHA-256 provenance, item 18 시각 검증, README/통합 보고서 링크, PROJECT_LOG.jsonl 구문·event ID 중복을 검증한다.
- 로컬/CI 실행: `python cra_traceability.py`; 회귀 테스트 `tests/test_cra_traceability.py`.


## PR #35 병합 — CRA 추적성 무결성 자동화

- [PR #35](https://github.com/useformotor3/ai-discord-bot/pull/35) squash merge 완료. Merge commit `2a347a60f2632bbe87044484187765adab45aee2`.
- [Run #738](https://github.com/useformotor3/ai-discord-bot/actions/runs/44055249482): **151 passed / 1 xfailed**, traceability gate, PDF/HTML canaries 통과.
- Pre/post refs: `safety/pre-merge-main-pr35-2026-11-17` → `cad8452b64f274ceeaa203c1b0de6ecea5e2baac`; `safety/post-merge-main-pr35-2026-11-17` → `2a347a60f2632bbe87044484187765adab45aee2`; post ref와 main compare identical.


- [M/606 Annex I 41-item 서보 드라이브 관련성 매핑](reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv): horizontal/vertical/component 표준화 주제, ESO 일정, 조건부 제품 관련성 및 후보 CRA/SEC/interface cross-reference.


## PR #37 병합 — M/606 Annex I 41-item relevance map

- [PR #37](https://github.com/useformotor3/ai-discord-bot/pull/37) squash merge 완료. Merge commit `25e1c36cc61a3001b5045cb8a6e90473fe830459`.
- [Run #757](https://github.com/useformotor3/ai-discord-bot/actions/runs/44056704831): **154 passed / 1 xfailed**, 41-item mapping traceability, PDF/HTML canaries 통과.
- Pre/post refs: `safety/pre-merge-main-pr37-2026-11-17` → `360b93a1b9fbf554607e8f258edbaa303c1fcb6f`; `safety/post-merge-main-pr37-2026-11-17` → `25e1c36cc61a3001b5045cb8a6e90473fe830459`; post ref와 main compare identical.


- [CRA 제품 경계 및 증거 수집 기준서](reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md): 모델·의도된 목적·제품 경계·인터페이스·RDPS·BOM/SBOM·취약점/지원 정책을 제품 증거로 확정하기 위한 한국어 입력 템플릿.


## PR #39 병합 — CRA 제품 경계 및 증거 수집 기준서

- [PR #39](https://github.com/useformotor3/ai-discord-bot/pull/39) squash merge 완료: `aec679142bf8c12b1ce18b233956f9695d70ca21`.
- [Run #781](https://github.com/useformotor3/ai-discord-bot/actions/runs/44058504509): **154 passed / 1 xfailed**; traceability 41 M/606 rows, official PDF/HTML canaries 통과.
- Pre-merge ref `safety/pre-merge-main-pr39-2026-11-17` → `d212081d0f105fc2b293606d71f9b156f0c45c89`; post-merge ref `safety/post-merge-main-pr39-2026-11-17` → `aec679142bf8c12b1ce18b233956f9695d70ca21`; merge SHA와 main 비교 identical.

- [통합 CRA 보고서 독립 검토 기록](reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-17.md): 섹션 번호·법적 분류 용어·근거 출처 한계·제품별 미확정 사항을 2차 검토.


## PR #41 병합 — 통합 CRA 보고서 독립 검토

- [PR #41](https://github.com/useformotor3/ai-discord-bot/pull/41) squash merge: `acfa2f583157ac541c4c60d71090197322bc8efb`.
- [Run #806](https://github.com/useformotor3/ai-discord-bot/actions/runs/44060186518): **155 passed / 1 xfailed**; Guidance/M/606 PDF, HTML canaries 통과.
- Pre/post refs `safety/pre-merge-main-pr41-2026-11-17` / `safety/post-merge-main-pr41-2026-11-17`; post ref와 main 비교 identical.
## 최신 재개 상태 — 2026-11-18

- 최신 통합 상태 스냅샷: [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)
- 최신 세션 기록: [SESSION_LOG_2026-11-18.md](SESSION_LOG_2026-11-18.md)
- PR #42 병합: `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`; [PR #42](https://github.com/useformotor3/ai-discord-bot/pull/42)
- exact PR-head CI [Run #824](https://github.com/useformotor3/ai-discord-bot/actions/runs/44061121932): 155 passed / 1 xfailed. PDF/HTML source canaries 및 traceability gate 통과.
- 다음 작업: CRA-001–CRA-035 법령 문언·의무 주체·조건·예외·기한 행 단위 심층 감사. Guidance PDF Commission-primary byte identity는 미확인으로 유지.



## CRA 법령 심층 감사 진행
- Batch 1 (CRA-001–CRA-010) 상세 원문 대조: [감사 기록](reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md)
- 최신 프로젝트 상황 및 남은 범위: [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)


- Batch 2 (CRA-011–CRA-020) 법령 문언 감사: [상세 기록](reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md).


- Batch 3 (CRA-021–CRA-035) 법령 문언 감사: [상세 기록](reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md).


- 35개 요구사항과 인터페이스/통제/Guidance/M/606 간 교차 정합성 감사: [CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md](reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md).


- 제품별 증거 수집·판정 기준: [CRA 제품 경계 및 증거 수집 기준서](reports/CRA_PRODUCT_BOUNDARY_AND_EVIDENCE_INTAKE_2026-11-17.md) (2026-11-18 법령 감사 보완 포함 예정).


- 최신 main 기준(2026-11-18): PR #48 merge `dc03173cd78f6efb6f46717850a107c8165b1d1a`; 현재 재개/다음 단계는 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md) 참조.


## 최신 재개 기준 — 2026-11-18
- 현재 기준 main: PR #48 병합 후. 최신 프로젝트 상황은 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 기준으로 한다.
- PR #48 merge commit: `dc03173cd78f6efb6f46717850a107c8165b1d1a`; 이후 main 기록 커밋: `c7b939a0fdfa559f9d68a11873c107186da423c3`.
- PR #48 exact-head CI Run #834 success 및 pre/post safety refs는 상황판에 기록되어 있다.
- 2026-11-18 통합 보고서 독립 감사는 작업 브랜치 `cra/integrated-report-audit-2026-11-18`에서 진행 중이며, [독립 감사 기록](reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-18.md)과 제품별 판정 표현 보완을 포함한다.
- 제품별 제조사/모델 증거가 제공되기 전 CRA scope/classification/conformity는 Unknown으로 유지한다.


## 최신 main 기준점 — PR #50 병합 완료 (2026-11-18)
- PR #50 독립 CRA 통합 보고서 감사 및 요약 문구 보완 병합: `137d096123ccf5ee478292002d2c528b41981fc7`.
- Exact-head isolated CI Run #840 success (source integrity, compile, CRA traceability, complete pytest, official PDF/HTML canaries, evidence artifact upload).
- Pre-merge safety ref: `safety/pre-merge-cra-integrated-report-audit-2026-11-18`; post-merge safety ref: `safety/post-merge-pr50-2026-11-18`.
- 독립 감사 기록: [CRA 통합 보고서 독립 감사](reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-18.md).
- 제품별 scope/classification/conformity는 제조사·정확한 모델 증거 확보 전 Unknown. Commission Guidance PDF Commission-primary byte identity는 여전히 미확인.
- 최신 재개 기준과 미완료 항목은 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 따른다.

## 최신 Guidance 원문 기준 — OJ C/2026/6013 (2026-11-18)
- CRA Guidance는 2026-11-17 Official Journal에 C/2026/6013 (CELEX 52026XC06013)으로 게재되었다. 최신 공식 PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- OJ PDF raw SHA-256: `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2` (61 pages, fallback=False).
- C(2026) 5252 Commission-hosted transition-pathways mirror hash는 별도 historical provenance로 보존하며 OJ PDF와 byte identity를 주장하지 않는다.
- G-001–G-013 claim register는 OJ page locator로 이관되었다. 상세 crosswalk와 비교 한계는 `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §7 참조.

### PR #52 검증 결과 — 2026-11-18
- Run #854 (ID `44205498935`): success; 158 passed, 1 xfailed; OJ PDF primary fetch and all validation stages passed.
- Artifact #14382388555; SHA-256 digest `9e8dc7f1c1d90015b7738263155ca9d6b1170aaea75ea6bd17350aeff7d36af7`.
- Provenance/status metadata and session/project logs were updated after Run #854; a fresh exact-head CI is required before PR #52 merge.

- Latest pre-metadata exact-head validation: Run #857 (ID `44205723336`), 158 passed / 1 xfailed, all stages successful; artifact #14383167818.
- Provenance manifest updated to Run #857; final PR head requires one fresh CI before merge.

## PR #52 병합 완료 — 2026-11-18
- OJ C/2026/6013 guidance source integration and 13 claim locator migration merged as `d3956b7b364c507b8d59dcfc056763f2829ea867`.
- Exact-head Run #861 success: 158 passed, 1 xfailed; official EUR-Lex OJ PDF primary acquisition fallback=False.
- Pre-merge ref: `safety/pre-merge-cra-guidance-oj-6013-2026-11-18`; post-merge ref: `safety/post-merge-cra-guidance-oj-6013-2026-11-18`.
- Latest status and next steps: [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md). Claim/page crosswalk and provenance: `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §7.

## Guidance claim redline — 2026-11-18
- G-001–G-013 have been substantively checked against OJ C/2026/6013. G-003/G-008/G-013 wording was narrowed/refined; G-001/G-013 locators corrected; G-004 obligations clarified.
- PDF page images were visually checked for all cited locator ranges. Full findings: `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md` §8.
- All Guidance claims remain non-binding explanations; product-specific conclusions remain Unknown until model evidence exists.

## Guidance–matrix link verification — 2026-11-18
- Bidirectional check passed: 13 Guidance claims, 35 CRA requirements, 15 interfaces, 36 SEC controls; zero missing reverse links and zero dangling claim IDs.
- OJ C/2026/6013 ELI is now the primary Guidance URL in the three cross-matrices; historic Commission publication page retained as secondary.
- Full results and corrections: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.

- The isolated CI validator now enforces bidirectional foreign-key consistency between each Guidance claim and its linked CRA requirement, interface and SEC rows, including reverse links; regression tests reject missing and dangling references.

### PR #54 validator/claim redline CI
- Run #865 passed on head `1d5ae716cc6683365f4da6236d15bb9b32be1e52`: 161 passed, 1 xfailed; all source, traceability, pytest and live canary stages succeeded.
- Artifact #14383728315, digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`.
- Final exact-head CI required after status/log metadata update.

## PR #54 merge checkpoint — 2026-11-18
- Guidance claim redline and bidirectional matrix validator merged: `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Exact-head Run #868 passed: 161 passed, 1 xfailed; pre/post safety refs verified.
- Next research priority: M/606 C(2026) 7861 Annex source provenance and current ESO/OJ standard status.

## PR #56 merge checkpoint — 2026-11-18
- M/606 Annex 41-item locator correction and ESO/OJ status audit merged: `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- Exact-head Run #879 passed: 161 passed, 1 xfailed; all CI and live-source canaries passed.
- Post-merge safety ref `safety/post-merge-m606-annex-eso-2026-11-18` identical to main.


### 최신 ETSI M/606 작업계획 — 2026-11-18
- ETSI의 2026-11-17 M/606 Work Item Plan v2.3.3을 추가 확인했다. EN 304 636(방화벽/IDS/IPS), EN 304 625(네트워크 인터페이스)의 상태 및 목표 일정을 별도 기록했다.
- 목표 일정은 실제 채택/발행/OJ 게재와 구분한다. CRA Article 27 추정 적합성은 정확한 표준 참조의 OJ 공표 확인 전 주장하지 않는다.
- 상세: [ETSI M/606 최신 작업계획 및 OJ 상태 점검](reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md).
- 최신 프로젝트 재개 기준: [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md).


### PR #58 병합 완료 — ETSI M/606 최신 상태
- ETSI M/606 Work Programme v2.3.3 및 EN 304 636 / EN 304 625의 최신 상태·목표 일정, Commission OJ index 확인 결과를 기록했다.
- PR #58 merge: `88d5eacd71c4267f64f674f0e990a25ed6fafd3a`; exact-head Run #883 성공(161 passed, 1 xfailed).
- Post-merge safety ref `safety/post-merge-pr58-2026-11-18`와 main은 identical.
- 상세: [ETSI M/606 최신 상태 보고서](reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md). 다음 작업은 CEN/CENELEC EN 40000 및 OT prEN 50770 상태의 공식 원문 검증이다.


### CEN/CENELEC 공식 상태 업데이트 — 2026-11-18
- CEN 공식 레코드에서 EN 40000-1-1:2026은 Published (DAV 2026-11-18)로 확인됐다. 그러나 CRA OJ citation은 “No citation expected”이므로 Article 27 추정 적합성 근거가 아니다.
- FprEN 40000-1-3은 Under Approval, prEN 50770-1~6은 CENELEC 공식 레코드상 Committee stage다. 각 상태와 OJ 필드를 분리해 추적한다.
- 상세: [CEN/CENELEC EN 40000 및 OT prEN 50770 공식 상태 감사](reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md), [CSV 상태표](reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.csv).


### PR #60 병합 및 CI checkpoint
- CEN EN 40000-1-1:2026 CEN Published 상태와 “No citation expected”를 분리 기록했고, CENELEC prEN 50770-1~6 공식 Committee stage 기록을 추가했다.
- PR #60 merge: `1f39cb31d7f5e3466f1b22b798e9fc51971542da`; exact-head Run #887 성공(161 passed, 1 xfailed).
- Post-merge safety ref `safety/post-merge-pr60-2026-11-18`와 main은 identical.
- 상세 보고서: [EN 40000 / OT prEN 50770 상태 감사](reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md).



### CRA 요구사항–증거 추적 매트릭스 — 2026-11-18
- CRA 법적 요구사항을 서보 드라이브의 위험평가·설계통제·시험·기술문서 증거로 연결한 provisional matrix 16개 항목을 추가했다.
- 법적 근거, 공개된 표준 scope, 엔지니어링 제안, 제품별 미확인 상태를 구분한다. EN 40000-1-2/1-3의 미확인 최종 조항을 인용하거나 만들어내지 않는다.
- [상세 보고서](reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md) / [CSV 추적표](reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.csv).
- 제품별 증거 미제공 상태이므로 16개 항목 모두 Unknown / evidence pending이다.

### PR #62 검증 진행
- 초기 PR head의 Run #891 성공: **161 passed, 1 xfailed**.
- CRA 공식 PDF 3종 hash canary 및 9개 공식 HTML source canary 성공. 최종 CI metadata 갱신 후 재검증 대기.


### PR #62 병합 완료 — CRA 요구사항 증거 추적
- PR #62 merge commit: `612285ed720310cebd82340dc2e3b150e2c6f80a`.
- Exact-head Run #896 성공: **161 passed, 1 xfailed**; 공식 CRA PDF 3종과 9개 HTML 출처 canary 통과.
- Post-merge safety ref `safety/post-merge-pr62-2026-11-18`와 main identical 확인.
- EVD-01–EVD-16 [상세 매트릭스](reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md) / [CSV](reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.csv) main 반영 완료.


### CRA M/606 일정 정정 — C(2026) 7861 final
- Commission은 2026-11-10 M/606을 개정했다. 새 ESO adoption deadline은 item 1/15: 2026-11-30, items 2–14: 2027-10-30, vertical items 16–41: 2027-01-31.
- [개정 결정 추적 보고서](reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md). 날짜를 OJ citation/Article 27 presumption과 혼동하지 않는다.


### PR #64 초기 exact-head CI
- Run #900 success: **161 passed, 1 xfailed**; CRA cross-matrix traceability(13/15/35/36/41) 및 공식 CRA PDF/HTML canary 통과.
- Artifact #14390620457, SHA-256 `b7ced7629ab9e88bf44190d6d4f5fd50fc91f45bfc33a83ae09a02c1833e2f20`. CI 메타데이터 기록 후 최종 head 재검증 예정.


### PR #64 병합 완료 — M/606 일정 정정
- PR #64 merge commit `41229486baded6336aa43cd3b5de375476fe92f3`.
- Final exact-head Run #905: **161 passed, 1 xfailed**; CRA traceability 및 공식 PDF/HTML canary 통과.
- [M/606 개정 추적 보고서](reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md)가 main에 반영됨.
- Post-merge safety ref `safety/post-merge-pr64-2026-11-18`와 main identical.

### CRA 서보 드라이브 적용성·제품 분류 intake
- [P0 증거 intake 및 CRA 제품 분류 기준](reports/CRA_SERVO_DRIVE_APPLICABILITY_CLASSIFICATION_AND_P0_INTAKE_2026-11-18.md) 추가.
- Article 2 적용성과 Annex III/IV core functionality 분류를 분리하고, Commission Implementing Regulation (EU) 2025/2392 기술 설명을 기준으로 제품 경계 검토 절차를 정리.
- 제품 모델 자료 미제공 상태에서 개별 모델의 CRA 적용/제외 또는 Class I/II/Critical을 추정하지 않도록 명시.


### PR #65/#66 결과 및 분류 기준 보완
- PR #65 merge `d1f96fa6bba297e31ed47ae1b96f59421c55b774`; Run #908: 161 passed, 1 xfailed. Post-merge safety ref `safety/post-merge-pr65-2026-11-18` == main.
- PR #66 merge `9cb62579e4f45ebf57587cc19644c370cbe80ebb`; Run #910: 161 passed, 1 xfailed. Post-merge safety ref `safety/post-merge-pr66-2026-11-18` == main.
- EUR-Lex Implementing Regulation (EU) 2025/2392 원문에 따라 core functionality/통합 구성요소 구분, Annex I 기술 설명, Annex IV와 Article 8 인증 의무를 구분해 보고서를 보완.


### PR #67 병합 완료
- PR #67 merge `86af2db5fadf5098b22b39d2d6c07710ed0033ee`.
- Final exact-head Run #912 / ID `44223114411`: success; source integrity, compile, CRA traceability, full test suite, official CRA PDF/HTML canaries passed.
- Artifact #14391457563, digest `sha256:f172ed1762a693f626e8c5781638c557e9d5471d6750b5315a54cae9398d919c`.
- Post-merge safety ref `safety/post-merge-pr67-2026-11-18` == main.


### M/606 수락 상태 구분
- 원래 M/606은 CEN-CENELEC 공식 발표상 2025-04-03 CEN, CENELEC, ETSI 수락 확인.
- 개정 결정 C(2026)7861의 Article 2 절차(각 ESO 수령일 및 1개월 내 비수락 통지)는 별도 사실이며 아직 공개자료로 확인하지 못했다. 두 상태를 혼동하지 않는다.


### PR #69 병합 완료
- PR #69 merge `8089cb96fdeba390dafe6991b19abfa1bc5b3e25`; Run #916 success: source integrity, compile, CRA traceability, full tests and official PDF/HTML canaries passed.
- Artifact #14391159512, digest `sha256:a71b8d12c9c1bb627da1b8d771ed2fda04ea179a721a1c55add3d5e28e16a1da`.
- Original M/606 accepted 2025-04-03; C(2026)7861 amendment Article 2 separate condition still unconfirmed.
- Post-merge safety ref `safety/post-merge-pr69-2026-11-18` == main.


### PR #70 병합 완료 — 2026-11-18
- PR #70 merge `ca65475db4ca53d23ee55308c9c9616a054ea756`; Run #918 on exact PR head passed (161 passed, 1 xfailed).
- CRA traceability: 13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items; bidirectional links true.
- Artifact #14391727520, SHA-256 `f737a27f61f2b6cd153731941c9e615e4379912d03ccfc3696f0eea7b2ad0d09`.
- Pre/post safety refs recorded; post-merge safety ref identical to main.
- Run #919 / ID `44228633470` on the resulting main commit succeeded: 161 passed, 1 xfailed; CRA traceability, source integrity, compile and official PDF/HTML canaries passed. Artifact #14393668052, SHA-256 `3d6314562d9ac4f34d645ef3191be6e499ae2d25e829968e17658717bdf2ae22`.


### PR #71 병합 및 main 사후 검증 완료 — 2026-11-18
- PR #71 merge: `adcec0a0cb94a326e6b7d9b8c242c4ae3dab4152`; exact-head Run #921 success.
- Main exact commit Run #922 / ID `44230377812`: **success**, 161 passed / 1 xfailed; source integrity, compile, traceability, official PDF and 9-source live CRA canaries passed.
- Artifact #14393784949, SHA-256 `db75a58638b43fbe1798c70b7c4dad5951cb1b1f98bfa013fa771184e6cf2126`.
- Pre/post safety refs are preserved; `safety/post-merge-pr71-2026-11-18` == main. 다음 우선순위: 35개 CRA 요구사항 행 단위 법령 의미 감사 및 통합 보고서/매트릭스/독립 감사 정합화.


### PR #72 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `293a27a8ea2a8e03f58db50bbe27d2aaea194c8d`; exact-main Run #924 success, 161 passed / 1 xfailed.
- Artifact #14394119675, SHA-256 `43a5e60b947890886baeee6c355beae857928f3c47deb9d76489244199accb3a`.
- Post-merge safety ref equals main. CRA-001–035 semantics and cross-matrix mapping are audited; next technical work is reference architecture control-to-evidence refinement.


### 참조 보안 아키텍처 v0.2 설계 보강 — 2026-11-18
- [CRA 산업용 서보 드라이브 참조 보안 아키텍처](reports/CRA_SERVO_DRIVE_REFERENCE_SECURITY_ARCHITECTURE_2026-11-17.md): 실시간 데이터 경로와 관리/업데이트 경로, 단일/분리 MCU 선택 기준, secure boot/update 검증, 설계 수용 기준 및 EVD/SEC 추적을 구체화하는 중.
- 제품별 회로/부품/펌웨어/시험 증거가 없어 참조 설계이며 제품 구현 완료나 적합성 판정이 아님.


### PR #73 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `16ab607a919c6bfa4fee8dc90ab5af2ea2f53352`; exact-main Run #926 success, 161 passed / 1 xfailed.
- Artifact #14394634118, SHA-256 `cf7d6d6ef7020d5381a4a2f201f50bf3171251155459505420ffce16998ef027`.
- Post-merge safety ref equals main. 참조 보안 아키텍처 v0.2 설계 보강은 PR #74 작업 브랜치에서 검증 중.


### PR #74 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`; exact-main Run #928 success, 161 passed / 1 xfailed.
- Artifact #14395476337, SHA-256 `6aaf8fc76f87121e42f8190fec9568121fbd8a0005695ce8de87ff776f0d1d93`.
- Post-merge safety ref equals main. 참조 보안 아키텍처 v0.2는 병합됐고, MCU 후보 기술 벤치마킹 초안은 [여기](reports/CRA_SERVO_DRIVE_MCU_PLATFORM_BENCHMARK_2026-11-18.md)에 정리 중.


### PR #75 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `1d7325baa592b35585fde850cf5a155988ba4cde`; exact-main Run #930 success, 161 passed / 1 xfailed.
- Artifact #14395188271, SHA-256 `63017368ac7db313f298b23c24d288f9c6781c27cc26472baa6d408abb244695`.
- [MCU 후보 기술 벤치마킹](reports/CRA_SERVO_DRIVE_MCU_PLATFORM_BENCHMARK_2026-11-18.md) 병합. MCU-T01–T12 시험 매트릭스·결과 기록 양식은 후속 PR에서 보강 중.


### PR #76 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `48afedaf8114688a51a7e6ed695c514277bd6407`; exact-main Run #932 success, 161 passed / 1 xfailed.
- Artifact #14395691349, SHA-256 `ec315a8b305f9b572452d42846de38a3698d431256faff36162ddb733303385a`.
- MCU-T01–T12 시험 매트릭스와 결과 기록 양식 병합. 실제 ST MCU part number 및 제어 사양 확인 전 시험 결과/선정 결론은 보류.


### PR #77 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `caa32ed9ac6679b21b619155cdf28d1b75d81c33`; exact-main Run #934 success, 161 passed / 1 xfailed.
- Artifact #14395218493, SHA-256 `8c827f786583bb5d2f8d14224e990b194ae50bf7f1393b4b9009925d123773da`.
- Post-merge safety ref equals main. MCU benchmark and MCU-T01–T12 test protocol are merged; actual ST MCU identity and control requirements remain P0 inputs.


### PR #78 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `441b0198bcd695752d1adb053d8e077f91426a0a`; exact-main Run #936 success, 161 passed / 1 xfailed.
- Artifact #14396500899, SHA-256 `6ef8037213259261dd57bcc3b1229d50f58947092a953bbc12ffc106ee4c8a05`.
- Post-merge safety ref equals main. CRA legal/evidence matrix, reference architecture, ST/TI MCU benchmark and MCU-T01~T12 test protocol are synchronized.


### PR #79 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `2e377127a26d3d9c0232089cad583ff6f2d328ca`; exact-main Run #938 success, 161 passed / 1 xfailed.
- Artifact #14396566514, SHA-256 `d9f1c96ecab857a65c699b18489315fcf5edbe0892234dc5c42157dceb2dd156`.
- Post-merge safety ref equals main. 현재 CRA 문서·MCU 비교·시험 계획 checkpoint 기록이 동기화됨.


### PR #80 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `950cacef2ea4ed2bb4062f09ef0180a5621375a5`; exact-main Run #940 success, 161 passed / 1 xfailed.
- Artifact #14396950302, SHA-256 `dca34e12cfea64f9f6a5676a084910e465bf2f8bb415eee4173681683ea9a9cb`.
- Post-merge safety ref equals main. 문서 checkpoint 최신 상태. 제품별 MCU 실측을 시작하려면 실제 ST 부품번호와 제어 사양 필요.


### PR #81 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `11b7ccac639501b98e9a9f6c76dfac473d6e0535`; exact-main Run #942 success, 161 passed / 1 xfailed.
- Artifact #14397065458, SHA-256 `0d5a340c3ac3e0435704d5543f38ab35bd883ea7a5c30adfe1b3983db24882bf`.
- Post-merge safety ref equals main. 현재 문서 checkpoint는 PR #81까지 기록; 다음 단계는 제품별 MCU 식별과 실제 제어 사양 intake.


### PR #82 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `572de72c8bfab7a1e1e144527783c1508bb26cae`; exact-main Run #944 success, 161 passed / 1 xfailed.
- Artifact #14396972010, SHA-256 `f23e616d121c61d5825774f1098f213b40cff65e858a527807060d71b02734c4`.
- Post-merge safety ref equals main. CRA evidence, architecture, MCU candidate benchmark and test plan are synced; actual ST MCU identification remains outstanding.


### PR #83 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `0255e50f003792fa8f5d0d3a130e45dda3491c3d`; exact-main Run #946 success, 161 passed / 1 xfailed.
- Artifact #14396926567, SHA-256 `0da05816f553bfbe1f541df001f2f487bd66176e3b454eb04ee47cffd3330a33`.
- Post-merge safety ref equals main. 현재 CRA 산출물과 진행상황 checkpoint 최신화 완료.


### PR #84 병합 및 main 사후 검증 완료 — 2026-11-18
- Merge `774551f378f59c82ce34342f63fd595d4c743852`; exact-main Run #948 success, 161 passed / 1 xfailed.
- Artifact #14397286074, SHA-256 `1cd7be5fcd710e5fc193595602c974a701f1242f32ec5a549ea61a11c9eec388`.
- Post-merge safety ref equals main. 다음 제품별 MCU 단계는 실제 ST 부품번호 확인 후 진행.


### 최신 상태 — PR #85 / 2026-11-18
- Main `db05c57103fc9039347b61a29f473fe1af1c7082`; exact-main Run #950 success (161 passed / 1 xfailed).
- 제품별 증거 intake는 미완료. 실제 drive model/SKU와 ST MCU part marking/BOM, control requirements를 확보하기 전 CRA 분류 및 MCU selection 보류.
- MCU-T01~T12는 시험 계획만 존재하며 전부 Not Run. 자세한 현재 상태는 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 참조.


### 자동화 테스트 상태 — 2026-11-18
- PR #87 merge 이후 exact-main CI: **162 passed / 0 xfailed**.
- Git push 실패 시 실패 종료·오류 로그·성공 메시지 미출력을 테스트로 고정했다. 운영 main.py 및 운영 workflow는 변경하지 않았다.
- 최신 main 기준과 제품별 evidence gate는 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 참조.


## EVD–CRA–SEC 추적 체계

- [EVD–CRA–SEC 교차 추적표](reports/CRA_EVD_SEC_TRACEABILITY_CROSSWALK_2026-11-19.csv): 16개 EVD와 35개 CRA 요구사항·36개 SEC 통제 간 후보 링크. 제품별 적용성은 별도 판정.
- [요구사항–증거 매트릭스](reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md): EVD별 책임·생애주기·검증·내부 합격 게이트 및 추적 원칙.
- [제품 증거 register 템플릿](reports/CRA_PRODUCT_EVIDENCE_REGISTER_TEMPLATE_2026-11-19.csv): E-001~E-015 자료의 원본 provenance, EVD 연결, 검토 상태 및 승인 근거 입력 양식.


## LS메카피온 CRA 예비 평가
- [제품군 예비 분석 보고서](reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md): 13개 제품군 스크리닝 및 2026-11-19 Commission CRA guidance/M/606 개정 반영. v0.2도 제품군 예비 분석이며 모델별 적합성 판정은 아님.
- 공식 매뉴얼 첨부 메타데이터는 확인 중이나 원본 PDF 다운로드·해시·페이지 검토가 완료되지 않은 항목은 제품 증거로 승인하지 않는다.
- 최신 기준과 미완료 게이트는 [현재 상황판](PROJECT_STATUS_CURRENT.md) 및 [마스터 계획](MASTER_PLAN.md)을 참조.


## CRA 공식 이행자료 확장
- LS메카피온 CRA 보고서 v0.3에는 CRA 관련 위임규정 (EU) 2025/1535 및 2026/881, ENISA SBOM·보안 업데이트·Secure by Design·SME 평가·Single Reporting Platform 자료가 추가되었다.
- 이 자료들은 법령, 비구속적 지침, 기술 자문으로 법적 지위를 구분한다. 제품별 적합성 판정은 여전히 별도 증거가 필요하다.


## CRA와 Machinery Regulation 병행 검토
- LS메카피온 CRA 보고서 v0.4는 Regulation (EU) 2023/1230의 Annex III 1.1.9/1.2.1과 CRA의 병행 적용, 제품 경계, EMC/LVD/RED 등 관련 제품법령을 별도로 스크리닝한다.
- 제품별 공급 형태와 정확한 모델·무선 옵션·기계 내 역할이 확인되기 전에는 법령 적용 여부 및 책임 주체를 확정하지 않는다.


## CRA 표준화 추가 트랙
- LS메카피온 CRA 보고서 v0.5는 M/606 41개 표준과 Commission Notice C/2026/1695 Action 5(Annex III/IV 밖의 기계류 등 제품을 위한 추가 표준화 계획)를 구분한다.
- 연간 작업계획에 포함된 사실은 최종 조화표준 또는 CRA Article 27 적합성 추정이 아니다. 실제 OJ 인용 상태를 별도 확인한다.


## M/606 개정기한 원문 검증
- 보고서 v0.6은 Commission Implementing Decision C(2026) 7861 final Annex I의 41개 ESO 제출기한을 원문과 대조한다. 1·15번은 2026-11-30, 2–14번은 2027-10-30, 16–41번은 2027-01-31이다.
- 이 날짜는 제조자 CRA 준수기한이 아니며, 최종 조화표준의 OJ 인용·Article 27 적합성 추정과 구분한다.


## CRA 신고 운영 준비
- 보고서 v0.7은 ENISA SRP FAQ 2026-10-15와 SRP/User Manual v1.3을 반영해 실제 신고 절차·담당자·기한·UI 제약을 설명한다.
- SRP의 72시간 카운터 표시와 AEV 최종보고서 카운터에는 한계가 있으므로 법정 기한은 제조자 내부 기록의 인지시각과 패치 제공시각을 기준으로 별도 관리한다.


## LS메카피온 제품·도구·ESI 매핑
- 보고서 v0.8은 13개 제품군의 공개 인터페이스, DriveCM Ver1.03.2 지원 모델, EtherCAT ESI Ver0.98 적용 모델을 교차 비교한다.
- 공개 지원 목록에 없는 모델은 미지원으로 단정하지 않고 제조사 확인 필요/Unknown으로 유지한다. 도구·ESI·매뉴얼 원본의 해시·내용 검토는 다음 단계다.


## M/606 표준 개발 단계 및 OT/IACS 지원자료
- 보고서 v0.9는 STAN4CR/CEN-CENELEC/ETSI 공동 M/606 진행보고서 V2.0(2026-06-03)의 개발 단계 스냅샷과 EN IEC 62443-4-1/-4-2/-3-3 산업용 OT 지원 deliverables를 검토한다.
- 2026-06-03의 publication forecast는 과거 자료이며, 최신 M/606 제출기한은 C(2026) 7861 Annex I로 별도 관리한다. OT 지원 deliverables는 CRA 조화표준/OJ citation과 구분한다.


### 최신 CRA 진행상태 (2026-11-20)
PR #126 병합 완료(`9b61f1d9b177454c3530fa5339883e6434d01df3`), 정확한 PR head CI Run #1052 성공. EN 40000-1-1/-1-2 발행은 CEN-CENELEC 공식 공지로 확인했으나, OJ 인용 기대 여부에 대한 CEN 개별 카탈로그 필드 직접 검증은 미완료이며 2차 자료의 "No citation expected"는 잠정 정보로만 취급한다. M/606 41개 항목별 OJ 전수감사 및 모델별 CRA 판정은 계속 진행 중.


### EN 40000 OJ citation 확인 (2026-11-20)
CEN 공식 카탈로그에서 EN 40000-1-1:2026(JT013095) 및 EN 40000-1-2:2026(JT013089)의 citation 필드를 직접 확인했다. 두 항목 모두 “No citation expected for Directive 2024/2847”이며, CRA 제27조 적합성 추정 근거로 사용하지 않는다. 발행·가용일은 2026-11-18.


### M/606 Annex I 감사 (2026-11-20)
C(2026) 7861 final 대체 Annex I 기준 41개 항목의 번호·주제·ESO 채택기한을 41/41 대조했다. 1·15: 2026-11-30; 2–14: 2027-10-30; 16–41: 2027-01-31. ESO 작업기한은 제조사 준수기한이 아니다. 각 행의 실제 EN/ETSI 번호와 OJ 인용 상태는 별도 매핑이 필요하며, 41개 모두의 OJ 상태를 확인한 것은 아니다. 자세한 감사대장은 reports/CRA_M606_41_ITEM_PRIMARY_SOURCE_AUDIT_2026-11-20.csv 참조.


### 최신 CRA 진행 기준점 (2026-11-20)
- PR #128 병합 완료: `6733f37201117cb5744215d9deb337b0810acc49` (41개 M/606 Annex I 항목 1차 출처 감사대장 추가).
- PR exact-head Run #1060 성공. main push CI Run #1061 성공. PR #129 병합 및 main push CI Run #1063도 성공.
- 감사대장 `reports/CRA_M606_41_ITEM_PRIMARY_SOURCE_AUDIT_2026-11-20.csv` / `.md`; Annex I 항목번호·주제·ESO 채택기한 41/41 확인. 개별 표준 매핑 및 OJ 인용 전수감사와 동일한 작업은 아님.
- 상황판 `PROJECT_STATUS_CURRENT.md`, 마스터 계획 `MASTER_PLAN.md`, 세션 로그 `SESSION_LOG.md`, append-only 이력 `PROJECT_LOG.jsonl` 참조.


### 2026-11-20 M/606 Work Item 매핑 업데이트
CEN/CENELEC 공식 M/606 Work Programme V1(2025-04-02)에서 item 1 → JT013089, items 2–14 → JT013091, item 15 → JT013090 연결을 확인했다. CEN 공식 2026-02-23 webinar는 JT013090을 prEN 40000-1-3 Vulnerability Handling과 연결한다. CEN 2026-11-19 발표는 FprEN 40000-1-3 공개가 임박했다고 설명하지만 세부 카탈로그 단계/OJ 필드는 직접 확인되지 않았다. Article 2의 1개월은 ESO가 개정 결정을 수령한 날부터 계산하므로 10 November를 자동으로 종료일로 간주하지 않는다. 자세한 범위와 미확인 사항은 통합 보고서 §30 및 감사대장을 참조.


### PR #130 최신 검증 상태 (2026-11-20)
- PR #130 병합 완료: `bfcc2e61fc07b2148fca7a162349af40aa84bc47`.
- Exact-head Run #1064 및 main push Run #1065 모두 성공.
- 41-item Annex I audit CSV 41개 데이터행 유지, `PROJECT_LOG.jsonl` 221개 레코드 전부 JSON 파싱 통과.
- 다음 조사: M/606 OT/IACS 보조 Work Item과 서보드라이브 제품기능·제품경계의 관계를 별도 분석하되, 단순히 산업용 장비라는 이유로 Annex III 분류를 확대하지 않는다.


### 2026-11-20 — OT/IACS 수직 프로파일 6종 검토
CLC/TC 65X의 M/606 20b/21b/22b/25b/27b/36b를 prEN 50770-4/-2/-6/-3/-5/-1에 연결하고 개별 CENELEC 카탈로그 상태를 확인했다. 모두 Under Drafting / Committee stage이며 OJEU 필드는 Citation expected로 실제 인용은 아직 확인되지 않았다. 서보드라이브 기능경계 분석은 보고서 §31 및 `reports/CRA_M606_OT_IACS_6_VERTICAL_PROFILES_SERVO_DRIVE_BOUNDARY_2026-11-20.csv` 참조. 25b는 조건부 우선 검토 후보이며, 나머지 VPN/NMS/SIEM/router/switch/firewall/IDS/IPS 기능은 현재 제조사 증거에서 확인되지 않았다. 기능 미확인을 미지원으로 단정하지 않는다.


### PR #132 검증 및 병합 상태 (2026-11-20)
- PR #132 merge SHA `f3a8fc06b2a0c5fdaa98d98ad8bc0f21abee22df`; exact-head Run #1068 success, 174 passed / 0 failed.
- Source integrity, compileall, traceability, full pytest, official CRA PDF/HTML canaries, provenance manifest upload 통과.
- Pre/post safety refs: `safety/pre-pr132-merge-2026-11-20`, `safety/post-merge-pr132-2026-11-20`; post ref와 main 동일.
- Main push CI는 별도 확인 전까지 미확인으로 표시한다.


### PR #133 검증 및 병합 상태 (2026-11-20)
- Merge SHA `a889b03855e3c7683aa140220352510ab4c4c116`; exact-head Run #1070 success, 174 passed / 0 failed.
- PDF artifact #14596185499, provenance artifact #14595641444; official PDF/HTML canaries 및 provenance upload 성공.
- Pre/post safety refs: `safety/pre-pr133-merge-2026-11-20`, `safety/post-merge-pr133-2026-11-20`; post ref와 main 동일.


### PR #134 검증 및 병합 상태 (2026-11-20)
- Merge SHA `7162664b29554a01d2694cd027efb0191a6c3344`; exact-head Run #1072 success, 174 passed / 0 failed.
- PDF artifact #14594883481, provenance artifact #14594828906; official PDF/HTML canaries 및 provenance upload 성공.
- Pre/post safety refs: `safety/pre-pr134-merge-2026-11-20`, `safety/post-merge-pr134-2026-11-20`; post ref와 main 동일.


### 2026-11-20 — 제조사 1차 자료 인벤토리
공식 자료실에서 DriveCM 1.03.2 지원모델, EtherCAT ESI 0.98 적용모델, PEGA2/iX700M 매뉴얼 등록정보를 확인했다. 상세 내용은 통합 보고서 §32 및 `reports/LS_MECAPION_MANUFACTURER_PRIMARY_SOURCE_INVENTORY_2026-11-20.csv` 참조. 첨부 원본 bytes 및 SHA-256은 아직 미확보.


### PR #136 검증 및 병합 상태 (2026-11-20)
- Merge SHA `d7e921f5a6db04d20ce06778f6ea384dbd9c63fe`; exact-head Run #1076 success, 174 passed / 0 failed.
- PDF artifact #14595209202, provenance artifact #14595972121; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr136-merge-2026-11-20`, `safety/post-merge-pr136-2026-11-20`; post ref identical to main.


### 2026-11-20 — 모델별 통신 인터페이스 분류
공식 카탈로그에서 EtherCAT 통신형과 펄스형을 분리하고, iX7NH Modbus TCP 및 L7P Modbus RS-422 가이드, iX700M CE 모델코드 메타데이터를 확인했다. 상세는 통합 보고서 §33 및 `reports/LS_MECAPION_SERVO_MODEL_INTERFACE_EVIDENCE_2026-11-20.csv` 참조.


### PR #138 검증 및 병합 상태 (2026-11-20)
- Merge SHA `372860cfb1a149bc5d5a7bf993e11dbf68217478`; exact-head Run #1080 success, 174 passed / 0 failed.
- PDF artifact #14595309514, provenance artifact #14595489037; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr138-merge-2026-11-20`, `safety/post-merge-pr138-2026-11-20`; post ref identical to main.


### PR #139 검증 및 병합 상태 (2026-11-20)
- Merge SHA `7545a771ce16f362cf5b911cd8c850efc91c2e92`; exact-head Run #1082 success, 174 passed / 0 failed.
- PDF artifact #14596455559, provenance artifact #14596296397; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr139-merge-2026-11-20`, `safety/post-merge-pr139-2026-11-20`; post ref identical to main.


### PR #140 검증 및 병합 상태 (2026-11-20)
- Merge SHA `2edae2463e04b5d4280aa9d04c48f7805b554707`; exact-head Run #1084 success, 174 passed / 0 failed.
- PDF artifact #14595564027, provenance artifact #14595579119; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr140-merge-2026-11-20`, `safety/post-merge-pr140-2026-11-20`; post ref identical to main.


### PR #141 검증 및 병합 상태 (2026-11-20)
- Merge SHA `f798d9d16d74e399124c207c45ee6bdb6c1339a7`; exact-head Run #1086 success, 174 passed / 0 failed.
- PDF artifact #14596955128, provenance artifact #14595634151; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr141-merge-2026-11-20`, `safety/post-merge-pr141-2026-11-20`; post ref identical to main.


### PR #142 검증 및 병합 상태 (2026-11-20)
- Merge SHA `0c8144a59e0741eb9538af2e8493def6fe982f33`; exact-head Run #1088 success, 174 passed / 0 failed.
- PDF artifact #14595914125, provenance artifact #14597100049; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr142-merge-2026-11-20`, `safety/post-merge-pr142-2026-11-20`; post ref identical to main.


### PR #143 검증 및 병합 상태 (2026-11-20)
- Merge SHA `f1157fb1b5581f55b1f192c15b1822386ce3ed1e`; exact-head Run #1090 success, 174 passed / 0 failed.
- PDF artifact #14596188740, provenance artifact #14595554868; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr143-merge-2026-11-20`, `safety/post-merge-pr143-2026-11-20`; post ref identical to main.


### PR #144 검증 및 병합 상태 (2026-11-20)
- Merge SHA `c616169b4300521459cc3ae78d631fcd739103fb`; exact-head Run #1092 success, 174 passed / 0 failed.
- PDF artifact #14597230119, provenance artifact #14596691436; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr144-merge-2026-11-20`, `safety/post-merge-pr144-2026-11-20`; post ref identical to main.


### PR #145 검증 및 병합 상태 (2026-11-20)
- Merge SHA `482305a4d5334ef19105560d0b4a3bd012acc1d0`; exact-head Run #1094 success, 174 passed / 0 failed.
- PDF artifact #14596711210, provenance artifact #14596970810; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr145-merge-2026-11-20`, `safety/post-merge-pr145-2026-11-20`; post ref identical to main.


### PR #146 검증 및 병합 상태 (2026-11-20)
- Merge SHA `bd0938484b22b4d8c6d8ad94b440de2b479a0ea2`; exact-head Run #1096 success, 174 passed / 0 failed.
- PDF artifact #14597665057, provenance artifact #14597380473; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr146-merge-2026-11-20`, `safety/post-merge-pr146-2026-11-20`; post ref identical to main.


### PR #147 검증 및 병합 상태 (2026-11-20)
- Merge SHA `51d75213e3e035dfc7a7858570844533644aedc5`; exact-head Run #1098 success, 174 passed / 0 failed.
- PDF artifact #14597665320, provenance artifact #14596892018; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr147-merge-2026-11-20`, `safety/post-merge-pr147-2026-11-20`; post ref identical to main.


### PR #148 검증 및 병합 상태 (2026-11-20)
- Merge SHA `33d82ee31c151c4d2f19165f1c17882fc5dfe722`; exact-head Run #1100 success, 174 passed / 0 failed.
- PDF artifact #14597670650, provenance artifact #14597051830; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr148-merge-2026-11-20`, `safety/post-merge-pr148-2026-11-20`; post ref identical to main.


### PR #149 검증 및 병합 상태 (2026-11-20)
- Merge SHA `6e04cd691d637589af69437068befe623fd46312`; exact-head Run #1102 success, 174 passed / 0 failed.
- PDF artifact #14596792806, provenance artifact #14596862640; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr149-merge-2026-11-20`, `safety/post-merge-pr149-2026-11-20`; post ref identical to main.


### PR #150 검증 및 병합 상태 (2026-11-20)
- Merge SHA `89659bc8dc718e8f090644b3aeb2de7c1ec363d1`; exact-head Run #1104 success, 174 passed / 0 failed.
- PDF artifact #14596532979, provenance artifact #14597076911; official canaries and provenance upload passed.
- Pre/post safety refs: `safety/pre-pr150-merge-2026-11-20`, `safety/post-merge-pr150-2026-11-20`; post ref identical to main.


### PR #151 검증 및 병합 상태 (2026-11-20)
- Merge SHA `05d95d7760aacd1b608e85b583069507c0b4a369`; exact-head Run #1106 success, 174 passed / 0 failed.
- Provenance artifact #14597945822; official PDF/HTML canaries passed. PDF source artifact upload was skipped because content was unchanged.
- Pre/post safety refs: `safety/pre-pr151-merge-2026-11-20`, `safety/post-merge-pr151-2026-11-20`; post ref identical to main.


### PR #152 검증 및 병합 상태 (2026-11-20)
- Merge SHA `8f2fa6af11be627dc3926dc46a28eb70c1ec23a0`; exact-head Run #1108 success, 174 passed / 0 failed.
- Provenance artifact #14597237413; official PDF/HTML canaries passed. PDF source artifact upload was skipped because content was unchanged.
- Pre/post safety refs: `safety/pre-pr152-merge-2026-11-20`, `safety/post-merge-pr152-2026-11-20`; post ref identical to main.


### PR #153 검증 및 병합 상태 (2026-11-20)
- Merge SHA `61c432f7c310bb8bbbf2bd2c8143b5860926ee68`; exact-head Run #1110 success, 174 passed / 0 failed.
- Provenance artifact #14597622291; official PDF/HTML canaries passed. PDF source artifact upload was skipped because content was unchanged.
- Pre/post safety refs: `safety/pre-pr153-merge-2026-11-20`, `safety/post-merge-pr153-2026-11-20`; post ref identical to main.


### PR #154 검증 및 병합 상태 (2026-11-20)
- Merge SHA `481d340050df4fd93689b992a374df3da2cfaa47`; exact-head Run #1112 success, 174 passed / 0 failed.
- Provenance artifact #14597173328; official PDF/HTML canaries passed. PDF source artifact upload was skipped because content was unchanged.
- Pre/post safety refs: `safety/pre-pr154-merge-2026-11-20`, `safety/post-merge-pr154-2026-11-20`; post ref identical to main.


### PR #155 검증 및 병합 상태 (2026-11-20)
- Merge SHA `cd5976403f91c79beca845d8efd3f4e5f1930e23`; exact-head Run #1114 success, 174 passed / 0 failed.
- Provenance artifact #14597677644; official PDF/HTML canaries passed. PDF source artifact upload was skipped because content was unchanged.
- Pre/post safety refs: `safety/pre-pr155-merge-2026-11-20`, `safety/post-merge-pr155-2026-11-20`; post ref identical to main.


### 2026-11-20 — 제조사 펌웨어·업데이트 자료 목록 스크리닝
- 공식 소프트웨어/가이드북 목록에서 DFU Downloader 1.00.4, L7NH 특주 O/S, DriveCM 1.03.1/게인 튜닝 가이드, iX7NH 교육자료 5건을 추가 식별.
- 상세 첨부 원본·SHA-256·본문은 미확보. 목록 메타데이터만 확인했으며 secure update·서명·anti-rollback을 입증하지 않는다.
- 보고서 §34 및 제조사 원본 인벤토리 참조.


### PR #157 병합 및 CI 검증 — 2026-11-20
- Merge SHA `0ea0fba1fb37504f9d11b5c12d562c0d68f1d190`; exact-head Run #1118 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries and provenance upload passed; artifact #14602977168.
- Pre/post safety refs retained; post ref identical to main.


### 2026-11-20 — ESI·DriveCM 모델 적용범위 교차검증
- ESI Ver0.98 공식 적용목록 11개 모델과 DriveCM 1.03.2 지원 모델·PEGA2 EtherCAT/RS-485 변경내역 대조.
- ESI 목록에는 PEGA2/iX700M 미기재, DriveCM에는 PEGA2 지원 명시. 별도 ESI 여부는 미확인으로 두고 호환/비호환 단정하지 않음.
- 상세 내용은 통합 보고서 §35 및 제조사 원본 자료 인벤토리 참조.


### PR #159 병합 및 검증 — 2026-11-20
- Merge SHA `c43b35df267c30facbc8c8f62677e48189d24127`; exact-head Run #1122 success, 174 passed / 0 failed.
- CRA traceability and official source canaries passed; provenance manifest uploaded.
- Pre/post safety refs retained; post ref identical to main.

### PR #174 병합 및 검증 — 2026-11-20
- Merge SHA `090c78bfa0edc759641a8dd30f9156038fa86a82`; exact-head Run #1150 success, 174 passed / 0 failed.
- Official HTML canary 10 sources and key CRA legal locators passed; provenance artifact #14613952433, SHA-256 `84a6cab72e1403f205d03151a9259a8ac101244d95fafdd3e87b5c5fca05b718`.
- PDF evidence upload step skipped; this does not establish acquisition of original PDF bytes.
- Pre/post safety refs: `safety/pre-pr174-merge-2026-11-20`, `safety/post-merge-pr174-2026-11-20`; main compared identical to merge SHA.

### 2026-11-20 — 최신 iX7NH/DriveCM 자료실 인덱스 추가 감사
- 공식 인덱스에서 iX7NH 교육자료(2026-09-14), DriveCM V1.03.1 및 게인 튜닝 가이드(2026-09-08), PN8B+iX7NH CSV 동기제어와 EtherCAT 0x211F 외부 IO 가이드(2026-07-06) 확인.
- 상세 첨부 원문은 미확보. 목록 메타데이터만 기록; 보고서 §42 및 인벤토리 snapshot row 참조.
- 제품군 목록: iX7NH AC 100–120/200–240 V, 0.1–15 kW; 특정 SKU 적용성/CRA classification 근거로 확대하지 않음.

### PR #175 병합 및 CI 검증 — 2026-11-20
- Merge SHA `850e2c851630239140e9a39d5f0978204b2ee025`; exact-head Run #1152 success, 174 passed / 0 failed.
- Provenance artifact #14615596751, SHA-256 `25c5c192aa96544b5e41c8cac6eeda0d629f3c95af6755e090be6d34ae506a70`; pre/post safety refs retained.
- PDF evidence upload skipped; no claim of original PDF acquisition.


### PR #176 병합 및 검증 — 2026-11-20
- Merge SHA `8f19a8b9fcf8e4582a9470e5483ff08019d1711f`; exact-head Run #1154 success, 174 passed / 0 failed.
- Report v0.21 §42; manufacturer inventory 28 data rows.
- Provenance artifact #14614954168, SHA-256 `067e43ccfc1c5b438f719489dc44f3e2ead4e152a2294d2c9b5031ca6bc192dd`; official HTML canary 10 sources passed. PDF evidence upload skipped.
- Pre/post safety refs: `safety/pre-pr176-merge-2026-11-20`, `safety/post-merge-pr176-2026-11-20`; main compared identical to merge SHA.


## 2026-11-20 CRA 최신 이행자료
- [CRA 통합 규제·기술 준수 보고서 v0.3](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md) §25에 Commission/ENISA 최신 이행자료와 SRP 운영상 주의사항을 반영 중.
- [SRP 운영 준비 기준서](reports/CRA_SRP_OPERATIONAL_READINESS_2026-11-20.md) 및 [공식 출처 최신성 대장](reports/CRA_LIVE_SOURCE_FRESHNESS_REGISTER_2026-11-20.csv) 참조.
- ENISA SRP FAQ의 UI 카운터는 Article 14 법정기한과 다를 수 있으므로 최초 인지 UTC 기준으로 별도 계산한다.


## CRA 중심 최신 자료 — 2026-11-20
- [통합 규제·기술 준수 보고서 v0.5](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md) §25–§28.
- [SRP 운영 준비 기준서](reports/CRA_SRP_OPERATIONAL_READINESS_2026-11-20.md).
- [공식 출처 최신성 대장](reports/CRA_LIVE_SOURCE_FRESHNESS_REGISTER_2026-11-20.csv).
- [ETSI M/606 상태 감사](reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md), [CEN/CENELEC EN 40000 및 OT 상태 감사](reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md).
- Article 27 추정 적합성은 실제 OJ citation과 제품/표준 범위가 확인된 경우에만 주장한다. CEN 발행 또는 ETSI Work Programme의 Harmonised Standard 메타데이터만으로 추정 적합성을 주장하지 않는다.
 
> **CRA 보고서 갱신 — 2026-11-23:** 통합 보고서 v0.12에서 §5~§10의 제조사 의무, Article 14 신고 운영, 표준/OJ, 기계류 관계, 제품 증거, 실행 게이트 설명을 보강했습니다. M/606 AMD 1 회의는 ETSI 캘린더상 11월 23일 Online 일정으로 확인했으나 회의 결과/ESO 수락은 미확인입니다. [보고서 보기](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md)


> **2026-11-23 병합 기록:** CRA 보고서 v0.12 및 ST MCU/M/606 조사 메모가 PR #196으로 병합되었습니다. [PR #196](https://github.com/useformotor3/ai-discord-bot/pull/196)

> **PR #218 병합 완료:** final HEAD `e3ebe08b5dcf14563bba0a75dca171459ab992c5`, Run #1417 success, merge SHA `200ccca974ad3af09b1634fd9bf02c1baac5ca8c`. PDF canary was explicitly SKIPPED because the Commission newsroom interstitial was followed by a 30-second timeout on the configured Commission-hosted transition-pathways mirror; no PDF bytes/hash are claimed. HTML source locator and provenance manifest passed. iX700M separate commercial sales/EU supply and actual SKU remain Unknown.



> **2026-11-24 CRA 최신 상태:** PR #230 Run #1458 success 및 squash merge SHA `7b3eaa39d96e78081621f8c40cde97ad916722e5`. main read-back identical. LS ELECTRIC Solution Square에 iX700M 사용 설명서 update 2026-09-16 항목이 있으나 PDF 원본/개정판은 미확보. LS메카피온 Ver1.3/Ver1.4 표시 충돌 unresolved. [통합 보고서 §70](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md), [증거등록부 §24](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md). PR #229 merge SHA의 post-merge main push CI는 pending/unverified. CRA only; SIL 3 제외.

> PR #239 first CI Run #1486 stopped at source-blob verification because the expected hashes had not yet been refreshed after the code/test edits. The branch now updates only the two integrity pins; workflow job behavior and schedule remain unchanged. The next exact-head run is the required validation.> **Retry fix verified (PR #239):** Exact branch HEAD Run #1497 / ID `45320409623` success 25/25; pytest 189 passed. Retry recovered C(2026)7861 Annex, so official CRA PDF pack is again 3/3. PDF artifact 14887520943 SHA-256 `9f8c1c64a43c17fae1a093c454e4be212d5b55fd6914130c9a4e1921411a80b4`; M606 binary hash matches prior Run #1481. [PR #239](https://github.com/useformotor3/ai-discord-bot/pull/239) awaits final merge guards.

> **PR #241 merged:** exact HEAD 159f8c16ba50c41e1dd0f3aa0fffba7a3ee1a09d, Run #1509 success 25/25, 6 files, JSONL 372/0, no reviews/threads. Expected-head merge dd54132fb44ed752b1f7942f4485ee03399a2c2f; main read-back verified. Post-merge Run #1510 / 45333438936 was still running at the latest snapshot. See report §77 / evidence register §34.
> **Source acquisition boundary:** Solution Square iX700M manual listing re-confirmed (2026-09-16) but detail/PDF remains JS-shell blocked; LS Mecapion Ver1.3/Ver1.4 listing conflict remains unresolved at binary level; Drive CE attachment timeout, Converter CE metadata only, CAD detail timeout. No original manual/DoC/CAD binaries acquired. CRA only; SIL 3 excluded.

> **PR #242 CI final correction (2026-11-24):** Run #1510 / 45333438936 completed SUCCESS 25/25 on main SHA dd54132fb44ed752b1f7942f4485ee03399a2c2f. PR #242 Run #1511 / 45333628512 completed SUCCESS 25/25 on exact HEAD f9dd8484403f6f91daa94f14b74250965d67e4f6. Earlier in-progress notes above are superseded by these final results. New official listing evidence includes iX700M Converter UKCA DoC and UL/KC/catalogue index entries; none of the linked binaries was acquired. See report §78 and evidence register §35. CRA only; SIL 3 excluded.


> **PR #242 merged:** exact HEAD e92bb6a0830cbdeb7ed4c05e31faba201c2754a3, Run #1513 success 25/25, expected-head squash merge 3fbc1bcbf669324706c4ae2f882ff7269ae87f48; main read-back identical. Main push Run #1514 / 45338702162 was in progress at snapshot. See report §79 / evidence register §36.
> **Button omission corrective action:** the persistent protocol existed but the final-output gate was not executed. Protocol v1.1 now requires a final check for an actionable next-step button as the last response element. CRA only; SIL 3 excluded.


## 2026-11-24 — CRA main CI Run #1520 최종 확인

PR #245 merge SHA `2b9d924a92bbd497289b9e3afe0dd52df527472b`의 post-merge main push Run #1520 (ID `45401919091`)은 exact SHA 일치 및 최종 SUCCESS, 25/25 steps로 확인됐다. Source integrity, compile, CRA cross-matrix traceability, 전체 테스트, 공식 CRA PDF/source canary 및 evidence/provenance 업로드가 모두 성공했다. 이는 저장소 CI 검증 결과이며 iX700M 제품 CRA 적합성이나 제조사 보안 구현의 증명은 아니다. 제품 원본 자료 미확보 및 Unknown 항목은 상황판과 제품 증거등록부의 상태를 따른다. CRA only; SIL 3 excluded.


## CRA 최신 법령·지침 반영 — 2026-11-24

PR #247 문서 반영 후 main push Run #1523 (ID `45403594895`)이 exact SHA `30d5c5997d0c99a8eff804c589010695c8735ced`에서 SUCCESS 25/25로 완료됐다.

추가로 European Commission의 2026-11-17 CRA Guidance (C/2026/6013, OJ C)를 검토했다. Article 14의 보고 의무는 2026-09-11부터 이미 적용 중이며, CRA 전체 제품 요구사항 적용일 2027-12-11과 구분해야 한다. 최신 지침은 인지 시점 이후 24시간 early warning, 72시간 notification, actively exploited vulnerability에 대한 최종 보고는 수정/완화 조치가 제공된 뒤 14일, severe incident 최종 보고는 72시간 notification 후 1개월의 단계적 제출 구조를 설명한다. 이미 2026-09-11 이전에 취약점과 실제 악용 사실 모두를 인지한 경우의 비소급 처리도 설명한다.

공식 법령·지침: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 ; https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1

지원기간은 원칙적으로 최소 5년이며 제품의 예상 사용기간이 5년 미만이면 예상 사용기간에 대응한다. 지원기간 중 제공한 보안 업데이트는 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 이용 가능해야 한다. (Article 13(8)-(9))

Annex I Part II의 실무 요구사항은 machine-readable SBOM(최소 top-level dependencies), 취약점 신속 수정, 기능 업데이트와 보안 업데이트의 분리(기술적으로 가능한 경우), 정기 보안 테스트, 수정 취약점 공개, coordinated vulnerability disclosure policy, 보고 연락처, 안전한 업데이트 배포 및 지체 없는 무상 보안 업데이트(해당 tailor-made business agreement 예외 포함)다.

이 요구사항은 제조사 구현 증거가 없으므로 iX700M에 대해 현재 `Unknown`이다. CRA only; SIL 3 excluded.


> **PR #248 merged (2026-11-24):** Exact HEAD 8fceea39961ff1076066eaf0bfaf79383a769cbf passed Run #1525 / 45404057074 (job success; pytest 189 passed; CRA traceability and official-source canaries/provenance passed). Expected-head squash merge SHA dd09fc13cf9076c5cf895f4a8e8727f525847ee4. Main read-back confirms report §83 / evidence §40 and PROJECT_LOG 379 records / invalid 0. Post-merge main push CI is UNVERIFIED because the connected GitHub run-list tools do not expose push-triggered runs and combined commit statuses are empty; do not infer success. See report §84 / evidence §41 and manufacturer inquiry draft. CRA only; SIL 3 excluded.


> **Post-merge main CI final (2026-11-25):** PR #248 merge SHA `dd09fc13cf9076c5cf895f4a8e8727f525847ee4` → push Run #1526 / 45486715925 SUCCESS; PR #249 merge SHA `e0a0af3aa7d29acb9fa0e26bddf466af7f3398b5` → push Run #1528 / 45487328163 SUCCESS. Both exact-head runs returned 15/15 steps success, 189 pytest passed, CRA traceability PASS, 3 official CRA PDFs hashed, 10 official sources/provenance PASS. CI validates repository/test/source pipeline only, not iX700M product conformity. Product manual/DoC/catalogue/CAD binaries remain unacquired; only official listing metadata is available. Inquiry expanded to 55 questions. See integrated report §85 / evidence register §42. CRA only; SIL 3 excluded.


> **Additional iX700M CE index finding (2026-11-25):** The manufacturer's CE index separately lists iX700MCB and several Drive model groups (075B/050B/D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B), plus Converter iX700MCV. This is index metadata, not proof of each DoC's scope or binary. KC listings are separate Korean regulatory evidence, not EU DoC/CRA proof. Manufacturer inquiry expanded to 58 questions. See report §85.5 and evidence register §42. CRA only; SIL 3 excluded.


> **PR #250 and post-merge main CI (2026-11-25):** PR #250 exact-head Run #1535 / 45491181163 SUCCESS (15/15 returned steps, 189 pytest passed), squash merged as `ff42addc136836bbbb89bec48bb0c791f031db19`. Main push Run #1536 / 45491379142 SUCCESS on exact merge SHA (15/15 returned steps, 189 pytest passed). Both live canaries explicitly skipped CRA Guidance C/2026/5252 because its mirror returned temporary HTTP 503; two other PDFs were fetched/hash verified and 10-source provenance passed. Earlier Runs #1526/#1528 fetched all 3 PDFs. iX700M original binaries remain unacquired; inquiry now has 58 questions. See report §86 / evidence §43. CRA only; SIL 3 excluded.

 
> **PR #251 / main push CI (2026-11-25):** PR #251 exact-head Run #1537 / 45491681394 SUCCESS, 15/15 steps, 189 pytest passed, traceability 383 events; expected-head squash merge `4c386689ab42c48e01456b72055217a75a78b14a`. Main push Run #1538 / 45505264304 SUCCESS on exact merge SHA, 15/15 steps, 189 pytest passed, 10-source provenance PASS. Both runs freshly fetched 2/3 CRA PDFs; C/2026/5252 was skipped due timeout (#1537) / HTTP 429 (#1538). See report §87 / evidence §44. iX700M source pages remain metadata-only; no product binary acquired. Inquiry now 59 questions. CRA only; SIL 3 excluded.

 
> **Run #1540 final (2026-11-25):** main exact HEAD `cffd2118d2ce4127e50352650479553cb12c2bdf`, run 45505830283 completed/success, 15/15 steps, 189 pytest passed, CRA traceability 384 events and 10-source provenance PASS. PDF canary 2/3 (C/2026/5252 HTTP 503 skipped). See integrated report §88 and evidence register §45. iX700M original manual/DoC/catalogue/CAD binaries remain unacquired; official listing metadata only. Manufacturer inquiry now 60 questions, draft/not sent. CRA only; SIL 3 excluded.

 
> **PR #253 validation:** Initial Run #1541 exposed a blank JSONL line and was cancelled without merge. After normalization, exact-head Run #1542 / 45507153261 SUCCESS, 15/15 steps, 189 passed, traceability 385 events PASS; all 3 CRA PDFs fetched/hash-verified (C/2026/5252 via fallback). See report §88.6 / evidence §46. CRA source packs are not iX700M product binaries.

 
> **PR #253 / main Run #1547 (2026-11-25):** PR exact-head Run #1546 SUCCESS and expected-head squash merge `e89faa6f9d907edcaf09adbd8f72eb81091ed279`; main push Run #1547 / 45507593050 SUCCESS on exact merge SHA, 15/15 steps, 189 passed, traceability 386 events, 10-source provenance, CRA PDFs 3/3. C/2026/5252 fetched via fallback (not asserted byte-identical to primary mirror). See report §89 / evidence §47. iX700M original binaries still not acquired; manual Ver1.3/1.4 discrepancy unresolved, Q61 added. Inquiry 61 questions. CRA only; SIL 3 excluded.

 
> **PR #254 / main Run #1549 (2026-11-25):** PR Run #1548 and main push Run #1549 SUCCESS, 15/15 steps, 189 passed, traceability 387 events, 10-source provenance, CRA PDFs 3/3. C/2026/5252 uses fallback=true. Merge/main SHA `dc1704557e1c3e1071383701d7a4615546814054`. See report §90 / evidence §48. iX700M original manual/DoC/catalogue/CAD binaries remain unacquired; metadata only. Inquiry now 62 questions, including exact ST MCU/security/SBOM evidence. CRA only; SIL 3 excluded.

 
> **PR #255 / main Run #1551 (2026-11-25):** PR Run #1550 and main push Run #1551 SUCCESS, 15/15 steps, 189 passed, traceability 388 events, 10-source provenance, PDFs 3/3. Merge/main SHA `a8c51348615461f90560a3cce8443cce98c3b24f`. C/2026/5252 fallback=true. See report §91 / evidence §49. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions. CRA only; SIL 3 excluded.

 
> **PR #256 / main Run #1553 (2026-11-25):** PR Run #1552 and main push Run #1553 SUCCESS, 15/15 steps, 189 passed, traceability 389 events, 10-source provenance, PDFs 3/3. Merge/main SHA `0c732caa45e7fac532117e2a658463acc546ee72`. C/2026/5252 fallback=true. See report §92 / evidence §50. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #257 / main Run #1555 (2026-11-25):** PR Run #1554 and main push Run #1555 SUCCESS, 15/15 steps, 189 passed, traceability 390 events, 10-source provenance, PDFs 3/3. Merge/main SHA `6f26d7166bd8a1208733c82c8fda592e1cfc0f9a`. C/2026/5252 fallback=true. See report §93 / evidence §51. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #259 / main Run #1558 (2026-11-25):** PR Run #1557 and main push Run #1558 SUCCESS, 15/15 steps, 189 passed, traceability 391 events, 10-source provenance, PDFs 3/3. Merge/main SHA `cabf4bfbb9bd5c4881eb951590813af5aa034ef0`. C/2026/5252 fallback=true. See report §94 / evidence §52. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #260 / main Run #1560 (2026-11-25):** PR Run #1559 and main push Run #1560 SUCCESS, 15/15 steps, 189 passed, traceability 392 events, 10-source provenance, PDFs 3/3. Merge/main SHA `d18a3a651cf7cd5cecfd99564f4332b8a505f196`. C/2026/5252 fallback=true. See report §95 / evidence §53. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #261 / main Run #1562 (2026-11-25):** PR Run #1561 and main push Run #1562 SUCCESS, 15/15 steps, 189 passed, traceability 393 events, 10-source provenance, PDFs 3/3. Merge/main SHA `c7d4d360f4642d788859cf434ed9ddc5409d421d`. C/2026/5252 fallback=true. See report §96 / evidence §54. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #262 / main Run #1564 (2026-11-25):** PR Run #1563 and main push Run #1564 SUCCESS, 15/15 steps, 189 passed, traceability 394 events, 10-source provenance, PDFs 3/3. Merge/main SHA `a5f1f68351b19557c5444425ae46fb790ddaeec7`. C/2026/5252 fallback=true. See report §97 / evidence §55. iX700M original binaries remain unacquired; metadata only. Manufacturer inquiry 62 questions, draft not sent. CRA only; SIL 3 excluded.

 
> **PR #263 / main Run #1566 (2026-11-25):** PR Run #1565 completed success with 14/15 successful steps; optional source provenance canary timed out and upload was skipped. Main push Run #1566 SUCCESS, 15/15, 189 passed, traceability 395, 10-source provenance PASS/uploaded, PDFs 3/3. Merge/main SHA `8d2d78b4ccc0ad326813f8e5cb74470bc5738e14`. C/2026/5252 fallback=true. See report §98 / evidence §56. iX700M original binaries remain unacquired; metadata only. Inquiry 62 questions. CRA only; SIL 3 excluded.


> **운영 교정 v1.2 (2026-11-25):** "다음 단계 계속 진행" 버튼은 이미 행동규약 §1/§8.1에 기록돼 있었으나 assistant가 최종 응답에 실제 버튼을 누락했다. §8.2에 실제 DIL 버튼·`GenUI.issueNewTurn`·CRA 재개 payload·마지막 UI 요소 검사를 hard gate로 추가 중이다. 최신 main/PR/CI를 다시 확인하고, 모든 실질 CRA 응답 마지막에 작동 버튼을 제공한다. CRA only; SIL 3 제외.


 
> **PR #266 / main update (2026-11-25):** Exact HEAD `6529ec9a9234ffdaa5a763a60a7d3df72646eb98`, Run #1570 SUCCESS, 15/15 returned steps, 189 passed, traceability 397, JSONL 397 valid / 0 invalid / 0 internal blanks. Expected-head squash merge `a015dc95f6c59d331275d646306b2b2a2137f437`; main read-back confirmed. Main push CI remains UNVERIFIED (no combined status or push run returned). Protocol §8.2 v1.2 is merged. iX700M original manual/DoC/catalogue/CAD binaries remain unacquired; latest official listing search metadata is recorded in report §99 / evidence register §57. Inquiry 62 questions, draft not sent; actual SKU/EU supply/operators/DoC coverage/BOM-MCU-SBOM/security configuration/CRA classification remain Unknown. CRA only; SIL 3 excluded.


 
> **Manufacturer inquiry v2.0:** 실제 번호 목록 감사에서 기존 파일은 90개였고, 과거 62개 기록은 stale count였다. 중복 통합 후 Q01–Q62로 정규화했으며 ID 연속성/중복/누락 검증을 통과했다. Q61 매뉴얼 revision, Q62 SKU별 BOM/MCU/FW/SBOM/security/vulnerability evidence matrix. Draft only; not sent.


 
> **PR #267 merged (2026-11-25):** Exact HEAD `3047df34212f7e5887ac358cd0156a1a75345fb6`, Run #1581 / 45530155733 SUCCESS 15/15, pytest 189 passed, traceability 399, CRA PDFs 3/3 fetch/hash, 10-source provenance PASS/upload. Expected-head squash merge/current main `418e526485f1d7c8f43e0f16f471b42b5c2f5a6c`. Main push CI remains UNVERIFIED; do not infer from PR CI. Manufacturer inquiry v2.0 is exactly Q01–Q62 after audit corrected stale count (old file had 90 numbered items). iX700M original binaries remain unacquired; metadata only. CRA only; SIL 3 excluded.


 
> **다음 단계 버튼 운영규약 v1.3 (2026-11-25):** 실질 CRA 응답 마지막에 컨테이너 없는 단독 `다음 단계 계속 진행` 버튼을 제공한다. 버튼은 직접 `GenUI.issueNewTurn`를 호출하고 최신 GitHub 상태를 재조회하는 CRA-only/SIL3-excluded 재개 payload를 사용한다. 출력 전 button/action/payload/last-element 네 항목을 검사한다. 버튼은 사용자 클릭으로 새 턴을 여는 기능이며 백그라운드 자율 실행은 아니다.


> **2026-11-25 PR #266–#268 audit:** exact-head runs #1570/#1581/#1583 all SUCCESS, 15/15 returned steps, 189 pytest passed, traceability 397/399/400, CRA PDFs 3/3 hash and official source provenance 10/10 JSON round-trip/upload. Merged main = ea16c98118dceaecb5f37711152ccc83d189a799. Post-merge main push CI remains UNVERIFIED because Combined Status is empty and current run-list connector only exposes PR-triggered runs. iX700M official listing metadata is recorded in report §101 / evidence register §59; original binaries remain unacquired. CRA only; SIL 3 excluded.


> **PR #269 merged (2026-11-25):** behavior protocol v1.3 §8.3 is now on main. Exact-head Run #1585 / 45531936573 SUCCESS 15/15, 189 pytest passed, traceability 402, CRA PDFs 3/3 fetch/hash, 10-source provenance manifest round-trip/upload. Merge/current main: f0e351a8f1df6f24e103b12b73c71defe5b9757d. Main push CI remains UNVERIFIED; PR CI is not main push CI. The final next-step button is a standalone native DIL button calling GenUI.issueNewTurn. CRA only; SIL 3 excluded.


## 2026-11-25 — main push CI 성공 및 문서 상태 정정
- PR #270 exact-head Run #1587 SUCCESS, main push Run #1588 SUCCESS 확인. main push는 `head_sha=660eb6d20e62f772272c03971dcd773b03a703f5`, `event=push`, branch=main, 15/15 steps, 189 pytest passed, CRA traceability 403, official CRA PDF 3/3 hash, official sources 10-source provenance manifest round-trip/upload PASS.
- 기존 README/SESSION_LOG의 PR #270 누락 및 main push UNVERIFIED 문구는 과거 상태 기록으로 남기고, 이 최신 append가 현재 상태를 supersede한다.
- Actions API 조회 방법: `/actions/runs?head_sha={SHA}&event=push&per_page=100`.
- iX700M manual current list Ver1.4 vs alternate index Ver1.3 same date conflict remains; manual, DoC, catalogue, CAD binary unavailable. metadata_only.
- Inquiry v2.0 Q01–Q62 draft_prepared_not_sent. Unknowns unchanged. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #270 및 main push CI 최종 검증
- PR #270 exact-head Run #1587 / 45532177358 SUCCESS (15/15 steps, 189 pytest passed, CRA traceability 403, CRA PDF 3/3 fetch/hash, 10-source provenance manifest JSON round-trip/upload).
- main push Run #1588 / 45532289060 SUCCESS: exact main SHA `660eb6d20e62f772272c03971dcd773b03a703f5`, event=push, branch=main, completed/success, 15/15 steps, 189 pytest passed, traceability 403, PDF 3/3 hash, 10-source provenance round-trip/upload.
- 조회 방법: `GET /repos/useformotor3/ai-discord-bot/actions/runs?head_sha={SHA}&event=push&per_page=100`. 이 직접 목록 조회로 PR-only wrapper가 놓친 push run을 발견했다.
- iX700M 원본 매뉴얼/DoC/카탈로그/CAD binary는 미취득(metadata_only). Ver1.4 current listing vs Ver1.3 alternate indexed snapshot 충돌은 원본 PDF 확인 전 unresolved.
- Q01–Q62 draft_prepared_not_sent. Actual SKU, EU/EEA supply, economic operators, signed SKU DoC scope, BOM/MCU/SBOM/security configuration remain Unknown. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #271 및 main push CI 결과
- PR #271 exact-head Run #1589 SUCCESS; main push Run #1590 SUCCESS. Merge/main SHA `c9532486ad2aca0ba9538eeffb42d30f76d73ea0`.
- Both runs: 15/15 steps, 189 pytest passed, CRA traceability 404, CRA Commission PDFs 3/3 fetch/hash, official source 10-record provenance manifest JSON round-trip and artifact upload PASS.
- Main push run #1590 ID 45537026894. Actions API query: `actions/runs?head_sha={SHA}&event=push&per_page=100`.
- PR #271 main sync included report §103, evidence §61, protocol v1.4 §8.4 and project status; this follow-up adds merge/push run closeout to README/SESSION_LOG and append-only PROJECT_LOG.
- iX700M original binaries remain unacquired; metadata_only. Q01–Q62 draft not sent; Unknowns preserved. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #272 및 main Run #1592 검증
- PR #272 exact HEAD `c273e6511012ec6f7d29c87ab71c6da870c2cf46`, Run #1591 / 45537296095 SUCCESS, 15/15 steps, 189 pytest passed, traceability 405, CRA PDFs 3/3, official sources 10-source provenance PASS/upload.
- Expected-head squash merge/current main `eb5894767cebdc7f956e31252b2d1831ef554a85`. Diff 6 files(+70/-0), reviews 0, threads 0.
- Main branch Run #1592 / 45537422906 SUCCESS, 15/15 steps, 189 passed, traceability 405, PDFs 3/3, official sources 10, provenance round-trip/upload PASS. Artifact metadata confirms exact main SHA. Event field is not separately surfaced by job/artifact response.
- Four artifact ZIPs downloaded and SHA-256 rechecked; report §105 / evidence register §63.
- Manufacturer iX700M manual Ver1.4/Ver1.3 conflict persists; Converter CE/UKCA, KR/EN catalog and 2D CAD/3D STEP originals remain metadata_only. Q01–Q62 not sent; actual SKU/supply/operators/DoC/BOM/MCU/SBOM/security/classification remain Unknown. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #273 병합 및 post-merge CI 보류
- PR #273 exact-head Run #1593 / 45539484334 SUCCESS, 15/15 steps, 189 pytest passed, traceability 406, CRA PDFs 3/3, official sources 10, provenance round-trip/upload PASS.
- Expected-head squash merge/current main `ce36f290f34a6ce391b91cf3aa6742f48c93e44a`; diff 7 files(+98/-0), reviews/threads 0.
- PR #273 post-merge main push CI is UNVERIFIED: commit-run wrapper is PR-only, combined status empty, direct Actions run-list unavailable. Do not claim success/failure or invent run ID.
- Official LS Mecapion index recheck: manual default/Servo filter Ver1.4 vs empty `sca=` index Ver1.3 same date; Converter CE/UKCA DoC, KR/EN catalogue and 2D CAD/3D STEP metadata reconfirmed; Solution Square manual list update 2026-09-16. All originals remain metadata_only. Q01–Q62 not sent; all product facts Unknown. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #272~#274 및 post-merge main push CI exact-head 검증
- Actions runs 직접 조회: `GET /repos/useformotor3/ai-discord-bot/actions/runs?head_sha={SHA}&event=push&per_page=100`; 기존 connector wrapper는 PR event 중심이라 push run 조회에 이 경로 사용.
- PR #272/#273/#274 exact-head Runs #1591/#1593/#1595 및 main push Runs #1592/#1594/#1596 모두 15/15 steps, 189 pytest, CRA PDF 3/3, 10 official sources/provenance upload PASS. Main push 세 건은 exact SHA, branch=main, event=push, completed/success 직접 확인.
- Expected-head squash merges: #272 `eb5894767cebdc7f956e31252b2d1831ef554a85`; #273 `ce36f290f34a6ce391b91cf3aa6742f48c93e44a`; #274/current main `ea1c2b315a0828bceee5913c2620b4a62823856b`.
- PR diffs #272 6 files(+70/-0), #273 7(+98/-0), #274 7(+87/-0); reviews/threads 0.
- iX700M official manual views still conflict: default/Servo search views Ver1.4, direct empty-category page Ver1.3; original binary not obtained. Solution Square iX700M manual update 2026-09-16 confirmed in search index only. Converter DoCs/catalogue/CAD STEP remain metadata_only.
- Q01–Q62 not sent; product SKU/supply/operators/signed DoC/BOM/MCU/SBOM/security/classification Unknown. CRA only; SIL 3 excluded. See report §107 and evidence register §65.


## 2026-11-25 — PR #275 exact-head CI 완료 (병합 전)
- PR #275 HEAD `9231c47c88ff7fe9fc9ce1022eb3023e6af244ba`; Run #1597 / 45540553259 completed/success, 15/15 steps, 189 pytest passed.
- Traceability claims 13, interfaces 15, requirements 35, SEC 36, product evidence 15, M606 mapping 41, PROJECT_LOG events 408.
- Official CRA PDFs 3/3, official sources 10, Article 13(8) 및 Regulation 2025/2392 locators, 10-source provenance JSON manifest PASS.
- Artifacts PDF 14988832738 (SHA-256 f3a29c9b…7786861), provenance 14989265975 (SHA-256 61736ebe…76fabf).
- PR diff 7 files(+111/-0), reviews/threads 0. JSONL branch count 408, invalid 0. PR is not merged yet; any further documentation commit requires new exact-head CI before merge.
- Manufacturer binaries remain metadata_only; Q01–Q62 not sent; product facts Unknown. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #275 and main push closeout
- PR #275 final head `2918f4b62c76d211462428ea32bbbd93a1cbdb61`, Run #1601 SUCCESS; squash merge/current main `cd00a3b67eea7bf18f5143951f4616659157e15e`.
- Main push Run #1602 / 45541169420 verified from Actions runs collection with exact merge SHA, event=push, branch=main, completed/success. 15/15 steps, 189 pytest, traceability 409, CRA PDFs 3/3, official sources 10, provenance PASS.
- Artifact IDs/digests and detailed status in report §109, evidence register §67, SESSION_LOG and PROJECT_LOG event `2026-11-25-CRA-PR275-RUN1601-MAIN1602-EXACTHEAD-CLOSEOUT`.
- Q01–Q62 not sent; product-specific unknowns preserved. CRA only; SIL 3 excluded.


## 2026-11-25 — PR #276 / Run #1604 closeout
- PR #276 merged; current main 45ec85172d2b5022b0eced1740a2c269b539e55c.
- Main push Run #1604 / 45541495434 exact SHA + event=push + branch=main; completed/success, 15/15 steps, compileall PASS, 189 pytest passed.
- Traceability 410 log events at run time; official CRA PDFs 3/3 individually hashed; 10 official sources; Article 13(8) and Regulation 2025/2392 locator checks; provenance manifest JSON round-trip/upload PASS.
- Artifacts: PDF ZIP ID 14988843820, archive SHA-256 5b0f7e5cd59a4955b2a22a8b18d5dd448b4df167119fa72a531bdd4074b9879b; provenance ZIP ID 14988684163, archive SHA-256 c9d8a97e9db97452444ef64d4f8493cd953317d82dcd499541b124e02f6228ff. Individual PDF content hashes are recorded separately in report §110.
- Manufacturer originals remain metadata_only; manual Ver1.3/1.4 listing conflict unresolved; Q01–Q62 not sent; all product-specific facts remain Unknown. CRA only; SIL 3 excluded.


## PR #277 validation correction
- Initial PR exact-head Run #1605 failed at CRA traceability validation because a blank line was appended to PROJECT_LOG.jsonl; line 411 was not valid JSON. Compile succeeded; pytest and source checks were skipped.
- Preserve all 411 non-empty existing records, remove only blank line(s), append a structured failure event, then re-run strict JSONL validation and exact-head CI. Do not merge until the new run succeeds.


## 2026-11-25 — PR #277 and main push Run #1607 closeout
- PR #277 merged at e39c95cc993e39cd3950338f07e1ce9282cbc03e.
- PR Run #1606 / 45543168422 and main push Run #1607 / 45543315065 both completed/success, 15/15 steps, 189 pytest, traceability 412, CRA PDFs 3/3, official sources 10, provenance upload PASS.
- JSONL corrected after Run #1605 failure: 412 physical records, every line parses, 407 unique non-null event IDs; 5 legacy records without event_id retained.
- Artifact ZIP digests and individual PDF hashes are recorded separately in report §111 and evidence register §69.
- Manufacturer originals remain metadata_only; Q01–Q62 unsent; product-specific facts Unknown. CRA only; SIL 3 excluded.


> **2026-11-25 PR #278 / main push Run #1609 closeout:** PR #278 exact HEAD de30e11867d22801412b2daba39190791565b390 passed Run #1608 / 45543506669 (15/15, 189 pytest, traceability 413, CRA PDFs 3/3, official sources 10, provenance PASS), then expected-head squash merged as bb59d1b38e563d5b72db1e97522a4ae5b79c6d9b. Main push Run #1609 / 45543596033 was independently confirmed by exact head_sha + event=push: head_branch=main, completed/success, 15/15, 189 pytest, traceability 413, PDFs 3/3, sources 10, provenance PASS. Run #1609 artifacts: PDF ZIP 14990725944 / SHA-256 bbd048563aaa1cba86dbe40065a46cc1e583846137f38bb0380595b20dbbd8e9; provenance ZIP 14990043643 / SHA-256 55b15ffc7bd5aada82abe42ffb266aec04228da05b29e7a5e34b2fd804589593. See report §112 / evidence register §70. Individual PDF hashes remain distinct from archive hashes. Manufacturer originals remain metadata_only; manual Ver1.3/1.4 conflict unresolved; Q01–Q62 unsent; product-specific facts Unknown. CRA only; SIL 3 excluded.

> **2026-11-25 PR #279 / Run #1610 and main Run #1611:** PR exact HEAD 49aa465811739fb5eb0dd36877f5875556fc51f5 passed Run #1610 / 45548956440 (15/15, 189 pytest, traceability 414, PDFs 3/3, sources 10, provenance PASS); merged as 67244a3618ec21495613dedeaf707977effcc783. Main push Run #1611 / 45549049529 independently confirmed exact SHA + push + main, SUCCESS (15/15, 189 pytest, traceability 414, PDFs 3/3, sources 10, provenance PASS). See report §113 / evidence register §71. Manufacturer recheck confirms listing metadata only; no manufacturer original binary or per-file hash acquired. Ver1.3/1.4 conflict unresolved; Q01–Q62 unsent; product-specific Unknowns retained. CRA only; SIL 3 excluded.


> **2026-11-25 PR #280 / Run #1612 and main Run #1613:** PR exact HEAD 504ed25a538e0a61dbc500f3ba86ad60ed167414 passed Run #1612 / 45549584947 (15/15, 189 pytest, traceability 415, PDFs 3/3, sources 10, provenance PASS), then expected-head merged as e2b2f39a16b5b41b466d1ec3db7138c49874d70e. Main push Run #1613 / 45549672737 confirmed exact SHA + push + main, SUCCESS (15/15, 189 pytest, traceability 415, PDFs 3/3, sources 10, provenance PASS). See report §114 / evidence register §72. Manufacturer direct attachment attempts remain blocked (timeout/502/SPA); official support contact path is now recorded. No manufacturer binary obtained; Ver1.3/1.4 conflict unresolved; all manufacturer sources metadata_only; Q01–Q62 unsent; product-specific Unknowns retained. CRA only; SIL 3 excluded.


> **PR #281 / post-merge main Run #1615:** PR #281 exact HEAD 28b1568bd6cc37f724c9180e879a29141714fbdb passed Run #1614 / 45550104279 (15/15, 189 pytest, traceability 416, PDFs 3/3, sources 10, provenance PASS), then expected-head squash merged as 5805638439877d2b5dc18d64b7765a67c848a194. Main push Run #1615 / 45550213763 on exact merge SHA independently passed 15/15, 189 pytest, traceability 416, PDFs 3/3, sources 10, provenance PASS. See report §114.5 / evidence register §72.1. Manufacturer binaries remain unacquired; all metadata_only; Ver1.3/1.4 unresolved; Q01–Q62 unsent; product-specific Unknowns retained. CRA only; SIL 3 excluded.



> **PR #282 / Run #1616 and main Run #1617:** PR #282 exact HEAD 8eb522dad46a421f006ea5d0e75ee707f5b6cf8d passed 15/15 (189 pytest, traceability 417, PDFs 3/3, sources 10, provenance PASS). Expected-head merge/main SHA 127c9ec311e2939059dbff689c3b04f1208e2424; main push Run #1617 / 45550542045 on exact SHA + push/main passed 15/15. Manufacturer source entries rechecked but no original binary obtained; all metadata_only, Ver1.3/1.4 unresolved, Q01–Q62 unsent, product Unknowns retained. See report §114.6 / evidence register §72.2. CRA only; SIL 3 excluded.


> **PR #283 / Run #1618:** PR exact HEAD 616b2a42049930290a42cd495f6c7543b0ba8751 passed Run #1618 / 45551394041 (job 138993151093, 15/15, 189 pytest, traceability 418, CRA PDFs 3/3, 10 official sources, provenance PASS). Merge SHA is 0821dac7a336848c1609c4c663860be90eb17337. Post-merge main push Run #1619 / 45551493565 is now verified: exact SHA 0821dac7a336848c1609c4c663860be90eb17337 + event=push + branch=main, SUCCESS 15/15, 189 pytest, traceability 418, PDFs 3/3, sources 10, provenance PASS. See report §114.7.3. See report §114.7 / evidence register §72.3. Manufacturer originals remain metadata_only; Ver1.3/1.4 conflict unresolved; Q01–Q62 unsent. CRA only; SIL 3 excluded.


> **PR #284 / Run #1622 and main Run #1623:** PR exact HEAD 50e660161e269a75c85cea02d5a125f418e4aa4d passed Run #1622 / 45552789733 (15/15, 189 pytest, traceability 420, PDFs 3/3, sources 10, provenance PASS), then expected-head squash merged as 1c1e0f30b18877dd02b70078ca8863646c371e3b. Main push Run #1623 / 45552908709 on exact merge SHA + push/main passed 15/15 (189 pytest, traceability 420, PDFs 3/3, sources 10, provenance PASS). See report §114.7.6 / evidence register §72.4. Manufacturer binaries remain metadata_only; Ver1.3/1.4 unresolved; Q01–Q62 unsent. CRA only; SIL 3 excluded.


> **2026-11-25 Run #1625 / latest manufacturer recheck:** main HEAD `1b3d253211048411277c4ed04d8c6e0f60263602`; exact main push Run #1625 / 45553259298 SUCCESS (15/15, 189 pytest, traceability PASS, CRA PDFs 3/3, official sources 10). See report §114.7.7 / register §72.5. LS Mecapion originals remain metadata_only; manual Ver1.3/1.4 conflict unresolved; CE Drive Unit/Converter and UKCA Converter listings only; no Drive Unit UKCA item located in searched results; KR/EN catalogue and CAD/STEP binaries not obtained. Detail pages timed out/502; no guessed URLs. Q01–Q62 unsent. CRA only; SIL 3 excluded.


> **2026-11-25 iX700M source recheck:** Manual conflict now includes LS ELECTRIC Solution Square's separately indexed `iX700M 사용 설명서` (2026-09-16) in addition to LS Mecapion Ver1.3/1.4 listing snapshots. CE Drive Unit groups and 150B metadata, CE/UKCA Converter metadata, KR/EN catalogue, and CAD/STEP listing are documented in report §114.7.8 / evidence register §72.6. No manufacturer binaries obtained; metadata_only. Q01–Q62 unsent. CRA only; SIL 3 excluded.


> **2026-11-25 Solution Square / iX700M source recheck:** Official Solution Square lists iX700M 사용 설명서 updated 2026-09-16, but document ID, detail href and original attachment URL remain undisclosed by the JS-rendered listing. LS Mecapion Ver1.3/Ver1.4 conflict remains unresolved. CE Drive Unit groups and 150B metadata, CE/UKCA iX700MCV, KR/EN catalogue and CAD/STEP listings rechecked. No manufacturer binary acquired; all remain metadata_only, no file hashes/signatures/internal revisions verified. Q01–Q62 unsent; no manufacturer contact. See report §114.7.9 / evidence register §72.7. CRA only; SIL 3 excluded.

> **2026-11-25 iX700M CE/UKCA detail-ID recheck:** CE index rows 171–173 confirm grouped Drive Unit titles for 220B, 370B/300B, 750B/550B/450B, but individual detail IDs/hrefs remain undisclosed; 150B detail metadata only. UKCA search did not expose an iX700M Drive Unit item (not proof of non-existence). Direct official detail pages timed out; no new binary, all metadata_only, no guessed URLs. Q01–Q62 unsent; CRA only; SIL 3 excluded. See report §114.7.10 / evidence register §72.8.

> **2026-11-25 manual revision cross-reference:** Official PEGA2 Ver1.3 detail page's previous-post label points to iX700M DRIVE 400[V] Ver1.3, but target href/ID is not exposed. This confirms a navigation reference only; Ver1.3/Ver1.4 controlled revision remains unresolved. KR/EN catalogue filenames/sizes/date reconfirmed, no bytes. All metadata_only; CRA only; SIL 3 excluded. See report §114.7.11 / evidence §72.9.

> **2026-11-25 official locator update:** LS메카피온 iX700M Ver1.4 manual listing link resolves to wr_id=12652 (detail fetch 502; no binary). Solution Square 2026-09-16 iX700M manual title confirmed but ID/detail/attachment URL remain hidden by JS app shell. KC index rows 113/114 list 220B/370B but are not CE/UKCA replacements. Ver1.3, CE grouped Drive Units, UKCA Drive Unit, catalogs and CAD/STEP remain unresolved/metadata_only. No guessed URLs; Q01–Q62 unsent; CRA only. See report §114.7.12 / evidence §72.10.


> **2026-11-25 Ver1.3 index-row confirmation:** LS Mecapion's official empty-category manual listing snapshot shows row 41 as iX700M DRIVE 400[V] Ver1.3 (2026-05-26), while the full/Servo-filter listing shows Ver1.4. Ver1.3 detail href/wr_id is still not exposed; no inferred ID. Solution Square 2026-09-16 manual document ID/detail/attachment remains hidden by JS app shell. CE 220B/370B/300B/750B/550B/450B remain grouped index-only; UKCA Drive Unit unlocated; catalogue and CAD/STEP remain metadata_only. No manufacturer binaries; no file hash/signature/revision/SKU-scope validation. Q01–Q62 unsent. See report §114.7.13 / evidence §72.11. CRA only; SIL 3 excluded.


> **2026-11-26 source-locator correction:** Solution Square page 14/search page 70 index iX700M manual updated 2026-09-16, but JS shell hides document ID/detail/attachment. Current directly opened LS Mecapion general manual list row 41 is Ver1.4 and its actual anchor resolves to wr_id=12652 (detail 502); older cached empty-category row-41=Ver1.3 result is stale/conflicting snapshot evidence, not a current locator. Ver1.3 target ID remains unknown. CE groups 220B/370B/300B/750B/550B/450B, UKCA Drive Unit, catalogue and CAD/STEP remain metadata_only. No manufacturer binary; no manufacturer file hash/signature/revision/SKU validation. Q01–Q62 unsent. See §114.7.14 / §72.12. CRA only; SIL 3 excluded.


> **2026-11-26 official detail retry:** LS Mecapion official PEGA2 detail search result exposes previous-post text “iX700M DRIVE 400[V] 매뉴얼 Ver1.3”, but not the target href/wr_id; direct fetch times out. Empty-sca cached row 41=Ver1.3 conflicts with current general/Servo row 41=Ver1.4. Ver1.4 wr_id=12652 is confirmed but detail fetch returns 502. Solution Square iX700M manual title/date (2026-09-16) confirmed; JS shell hides document ID/detail/attachment. CE rows 171–173 group six SKUs; no individual detail IDs/attachments verified. UKCA Drive Unit not located; wr_id=12893 is Converter Unit. KR/EN catalogue and CAD/STEP remain metadata_only. No manufacturer binaries; no manufacturer SHA/signature/revision/SKU checks. Q01–Q62 unsent. See §114.7.15 / §72.13. CRA only; SIL 3 excluded.


> **2026-11-26 official locator retry (§114.7.16 / §72.14):** PEGA2 Ver1.3 previous-post title is indexed but actual target anchor href/wr_id remains unavailable; Ver1.3/Ver1.4 snapshots conflict. Ver1.4 wr_id=12652 confirmed, detail 502. Solution Square iX700M 2026-09-16 title/date confirmed, JS shell hides ID/detail/attachment. CE rows 171–173 remain grouped; individual IDs not recovered (row170 150B wr_id=12888 is separate; no inference). UKCA Drive Unit not located; wr_id=12893 is Converter Unit. KR/EN catalogue and CAD/STEP metadata only. No manufacturer binaries; all metadata_only; no hash/signature/revision/SKU validation. Q01–Q62 unsent. CRA only; SIL 3 excluded.



> **PR #294 / main push Run #1647 closeout (2026-11-26):** PR exact HEAD 774bfc45f2ca152d18b8236987cb616ab80f9a7f passed Run #1646 / 45718668986 (25/25, 189 pytest, traceability 431, CRA PDFs 3/3, 10 official sources, provenance PASS), then expected-head squash merged as f7fe9c1151afcb210dbb0c9d589e6d22b7aec603. Main push Run #1647 / 45718795105 independently confirmed exact SHA + event=push + branch=main + completed/success, 25/25, 189 pytest, traceability 431, PDFs 3/3, sources 10, provenance PASS. Artifact IDs/digests and details in report §114.7.17 / evidence §72.15. Manufacturer originals remain unacquired, metadata_only; Ver1.3/Ver1.4 conflict unresolved; Q01–Q62 unsent. CRA only; SIL 3 excluded.



> **2026-11-26 manufacturer evidence recheck (§114.7.18 / §72.16):** PEGA2 Ver1.3 detail wr_id12651 shows previous-post title iX700M Ver1.3 but target href/wr_id remains hidden; general/Servo row41=Ver1.4 conflicts with empty-category row41=Ver1.3, preserve conflict/no ID inference. Ver1.4 wr_id12652 detail 502. CE rows171–173 SKU group labels confirmed (220B; 370B/300B; 750B/550B/450B), individual detail IDs not recovered. UKCA wr_id12893 is Converter Unit only; Drive Unit UKCA not located (absence not proven). Solution Square iX700M manual 2026-09-16 SPA shell hides document ID/detail/attachment. KR/EN catalogues each indexed 10.7M; CAD/STEP item indexed 2026-04-21; binaries not acquired. Manufacturer binaries 0, metadata_only; no manufacturer SHA/signature/signer chain/revision/SKU verification. Q01~Q62 unsent. CRA only; SIL 3 excluded. Details §114.7.18 / §72.16.



> **PR #296 / main push Run #1651 closeout (2026-11-26):** PR exact HEAD 2eb266711577c64fc182014c649f435b7f7049b4 passed Run #1650 / 45728292172 (25/25, 189 pytest, traceability 433, CRA PDFs 3/3, 10 official sources, provenance PASS). Diff reviewed (6 documentation files, +75/-0), expected-head squash merged as 6f8dbbe907debd35292c29a2f994d2c0a2ae6b81. Main push Run #1651 / 45728389056 independently confirmed exact SHA + event=push + branch=main + completed/success, 25/25 and same checks PASS. Artifact ZIP IDs/digests in report §114.7.19 / evidence §72.17; these are not manufacturer document hashes. Manufacturer originals remain 0 / metadata_only; CRA only; SIL 3 excluded.



## CRA 제조사 원본 증거 상태 (2026-11-26)
- 최신 main: `792d4e4ba7d5e4652692d86274d8f85474bfeb0b`; 상세 조사 결과는 [통합 보고서 §114.7.20](reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md) 및 [제품 증거 등록부 §72.18](reports/CRA_LS_MECAPION_PRODUCT_EVIDENCE_REGISTER_2026-11-23.md).
- LS메카피온 매뉴얼 row41의 Ver1.3/Ver1.4 색인 충돌은 유지한다. `page=1` 검색 스니펫의 Ver1.3 표시는 실제 열린 HTML 본문과 일치하지 않아 검색 스니펫만으로 확정하지 않는다.
- 제조사 원본 바이너리 신규 취득 0, metadata_only. SHA-256·PDF 서명/서명자 체인·내부 revision·SKU 범위 검증 없음.
- Run #1653 exact main push success; 제조사 원본 취득 성공과는 별개다. CRA only; SIL 3 제외.


## CRA 진행 종결 업데이트 (2026-11-26)
- PR #298 merged; current main `4c948a4b0b829485064ea6f577c9db9b2ce664e6`. PR #298 exact-head Run #1655 and main push Run #1656 both passed; details in report §114.7.21 / evidence register §72.19.
- Solution Square search index independently shows the iX700M user manual and iX700M product result, but no document ID/detail/API/attachment locator; metadata_only.
- Manufacturer binaries remain 0. CI artifact ZIP digests are not manufacturer file hashes. CRA only; SIL 3 excluded.


## PR #299 / main CI 종결 (2026-11-26)
- PR #299 exact-head Run #1657 and main push Run #1658 passed; current main `9f77fcdb0498b4ab9dd88e8ac097458c8bd1d75b`.
- PROJECT_LOG.jsonl has 436 non-empty valid JSON records. Details in report §114.7.22 / evidence register §72.20.
- Manufacturer originals remain 0 / metadata_only; GitHub artifact ZIP hashes are not manufacturer source hashes. CRA only; SIL 3 excluded.


## CI 실패 및 복구 이력 (2026-11-26)
- Run #1654 failed because an empty separator line in PROJECT_LOG.jsonl was parsed as an invalid JSON record (line 435). The blank line was removed; 435 records then parsed cleanly and corrected exact-head Run #1655 passed.
- Preventive check: normalize JSONL separators and parse every non-empty record before opening a PR. Details: report §114.7.23 / evidence register §72.21.
