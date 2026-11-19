# CRA 프로젝트 현재 상태 — 2026-11-19 KST

> 최신 상태 스냅샷. 역사 기록은 SESSION_LOG 및 PROJECT_LOG에 append-only로 보존한다.

## 최신 main 기준점 — PR #104 LS메카피온 제품군 예비 분석 보고서 병합 (2026-11-19)
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
