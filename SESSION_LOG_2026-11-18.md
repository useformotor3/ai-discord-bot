# 세션 로그 — 2026-11-18

## CRA 재개 및 PR #42 통합

- 최신 프로젝트 상태를 기준으로 CRA 작업을 재개했다. SIL 3는 과거 자료로 보존하며 활성 범위에서 제외한다.
- PR #42 `docs: clarify CRA legal locator and SBOM requirements`의 exact head `0ff686be74fb5c6309b46ed9c01473251d997579`에 연결된 GitHub Actions Run #824 (ID `44061121932`) 성공을 확인했다.
- 전체 테스트: 155 passed / 1 xfailed. Source integrity, compile, CRA cross-matrix traceability, live official source canary, Commission PDF source canary 및 artifact upload가 통과했다.
- Guidance PDF는 ANFR mirror fallback=True로 취득했다. Commission primary PDF bytes와의 동일성은 확인되지 않았음을 유지했다.
- PR 리뷰 스레드 및 제출 리뷰가 없는 것을 확인한 뒤 exact head SHA guard로 squash merge했다.
- Merge commit: `bc5f4a6adda081a58e0cbc2ba02a3bad8bcf3946`.
- Pre-merge ref `safety/pre-merge-main-pr42-2026-11-18` 및 post-merge ref `safety/post-merge-main-pr42-2026-11-18` 생성. post-merge ref와 main compare는 identical (0 ahead/0 behind).
- PR #42는 CRA-001–CRA-035 법령 locator의 1차 인벤토리 검토 및 SBOM 의무 체계(Annex I Part II(1), Annex VII(2)(b)/(8), Annex II(9))를 명확히 했다.
- 새 현재 상태 스냅샷 `PROJECT_STATUS_CURRENT.md`를 추가해 최신 main/PR/CI/복구 ref/미완료 사항을 한곳에 기록한다.
- 다음 작업은 35개 요구사항의 법령 문언·의무 주체·조건·예외·기한을 행 단위로 심층 검토하고 관련 보고서/매트릭스를 함께 정합화하는 것이다.


## CRA 법령 문언 심층 감사 Batch 1
- EUR-Lex 공식 Regulation (EU) 2024/2847 원문을 기준으로 CRA-001–CRA-010을 행별 대조했다.
- 신규 상세 감사: `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`.
- 추적표 locator 수정: CRA-001(Article 3(8)–(10), Recital 9 보강), CRA-003(Article 13(2) 제거, Article 3(2)/Recital 11–12로 정정), CRA-006(Annex I Part II(1), Article 13(7), Annex VII(2)(b)/(8) 분리 및 Article 13(5) due diligence 구분).
- CRA-008의 regular testing은 고정 법정 주기 숫자 미규정, CRA-009의 공개 지연 예외를 감사 문서와 통합 보고서에 기록했다.
- 추적표·통합 보고서·독립 감사·상황판/세션 로그를 같은 작업 브랜치에서 정합화했다. exact-head CI 통과 전 병합하지 않는다.
- 다음 대상은 CRA-011–CRA-020.


## CRA 법령 문언 심층 감사 Batch 2
- EUR-Lex 공식 Regulation (EU) 2024/2847 원문으로 CRA-011–CRA-020을 행별 대조했다.
- 신규 상세 감사: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md`.
- 요구사항 CSV에 연락창구의 비자동화 연락 수단 선택, 보안 업데이트의 무상 제공 예외, support period의 5년 미만 조건, 기술문서 작성/갱신과 보관 분리, Annex V/VI DoC, Article 32 평가경로 차이를 반영했다.
- CRA-020의 중요 해석: Annex III/IV core functionality 기준, 통합만으로 host product 분류 전이 금지, Class I/II/Critical 평가경로 분리.
- 통합 보고서·독립 감사·상황판을 같은 브랜치에서 동기화한다. exact-head CI 성공 전 병합 금지.
- 다음 대상: CRA-021–CRA-035.


## CRA 법령 문언 심층 감사 Batch 3
- EUR-Lex CRA 및 관련 Machinery Regulation/EHDS 공식 원문을 기준으로 CRA-021–CRA-035를 행별 대조했다.
- 신규 상세 감사: `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md`.
- CRA-023 사건 후 사용자 통지의 직접 근거를 Article 14(8)로 정정하고 Annex II를 제거했다.
- CRA-026에서 CRA Article 69(1)을 일반 sectoral overlap 근거로 사용하지 않도록 정정. CRA Article 2(5), Machinery Regulation Article 9(9), Annex III §§1.1.9/1.2.1을 중심으로 상호작용을 기록했다.
- CRA-028/034의 중복 범위를 경제운영자 역할(Articles 18–22)과 공급망 추적(Article 23)으로 분리했다.
- CRA-035에 Article 2(8)을 추가하고 Article 2(5)의 delegated-act 조건부 제한/제외를 명시했다.
- 35개 요구사항의 1차 심층 문언 대조를 마쳤다. 제품별 사실 검증/적합성 결정 및 법률가 검토는 완료를 주장하지 않는다.
- 다음 단계는 전체 35행 cross-matrix audit 및 누락/중복/표현 정합성 검증이다. exact-head CI 성공 전 병합하지 않는다.


## 전체 교차 매트릭스 정합성 감사
- CRA 35개 요구사항과 15 interfaces / 36 SEC controls / 13 Guidance claims / 41 M/606 items의 교차 참조를 검토했다.
- 신규 감사 기록: `reports/CRA_CROSS_MATRIX_CONSISTENCY_AUDIT_2026-11-18.md`.
- SEC-015 SBOM locator, SEC-018 공개 지연 예외, SEC-021 구현 후보 설명, SEC-031 RDPS 근거, SEC-032 데이터 연결 근거, SEC-034 경제운영자/추적성 링크, SEC-036 전환 조항 범위를 정정했다.
- 제품별 구현/시험 증거는 없으므로 기존 evidence status를 완료로 올리지 않았다.
- PR #46 merge commit `42aca53bb735d79292be59120fb868474e728073`, post-merge safety ref와 main 동일성 확인.
- 현재 브랜치에서 교차 감사와 통합 보고서/독립 감사/상황판을 동기화하고 exact-head CI 후 병합한다.


## PR #47 병합 및 제품 증거 수집 기준 보완
- PR #47 `docs: reconcile CRA requirements and evidence cross-matrices` exact-head CI Run #832 성공 후 squash merge.
- Merge commit `fd9733b31e5dffa382a82a420de6a195a714e98f`; pre/post safety refs 생성, post ref == main 비교 identical.
- 35 requirements, 15 interfaces, 36 SEC controls, 13 Guidance claims, 41 M/606 items 교차 감사 및 SEC-015/018/021/031/032/034/036 정합화 완료.
- 제품 증거 수집 기준서에 제품 범위/데이터 연결, RDPS 누적 기준, Annex III/IV core functionality, Machinery Regulation 관계, 신고 시한, 전환일 및 제출 우선순위를 보완하는 중.


## PR #48 병합 — 제품 증거 수집 기준서 업데이트
- PR #48 exact-head CI Run #834 성공 후 squash merge.
- Merge commit `dc03173cd78f6efb6f46717850a107c8165b1d1a`; pre/post safety refs 생성 및 post ref == main identical 확인.
- 제품 경계/증거 수집 기준서 Section 13–15에 데이터 연결·RDPS·Annex III/IV·Machinery Regulation·신고 시한·전환일 및 우선 증거 제출 목록 추가.
- 제품별 사실은 아직 입력되지 않았으므로 적용/등급/적합성은 Unknown 유지. P0 자료는 정확한 모델 데이터시트/카탈로그와 사용설명서.
- 다음: 통합 보고서 독립 재검토, Commission Guidance PDF primary byte identity 재확인, 제품 자료가 도착하면 evidence IDs와 35-row requirements를 모델별 연결.


## 통합 CRA 보고서 독립 재검토 — 2026-11-18
- 저장소의 행동강령, 현재 상황판, 마스터 계획, 최근 세션 로그 및 프로젝트 로그를 확인하고 main 기준에서 재개했다.
- EUR-Lex 공식 OJ HTML에서 CRA Articles 7, 8, 13(8)–(9), 14, 15, 69, 71 및 관련 Annex 문언을 열람해 통합 보고서의 핵심 법적 설명을 표본 대조했다.
- 새 독립 감사 기록: `reports/CRA_INTEGRATED_REPORT_INDEPENDENT_AUDIT_2026-11-18.md`.
- 감사 중 확인한 제품별 적용 가능성/기본 분류 문구의 과도한 확정 인상을 줄이기 위해 통합 보고서 요약을 수정했다. 전형적 디지털 서보 드라이브에 대한 사전 스크리닝 가설과 개별 모델의 법적 판정을 분리했다.
- 제품 증거가 없는 상태는 그대로 유지: 제품별 scope/classification/conformity Unknown, interfaces 미확인, SEC controls 미작성/증거 미확인.
- Guidance PDF Commission-primary byte identity 및 M/606 결정의 raw-byte 재취득은 이번 회차 완료로 주장하지 않는다.
- 변경 브랜치: `cra/integrated-report-audit-2026-11-18`; 기준 main commit: `c7b939a0fdfa559f9d68a11873c107186da423c3`.
- 운영 main.py, production workflow, secrets, state/history/archive, Gemini/Discord 운영 실행은 변경하지 않았다.
- 다음: 관리 문서/프로젝트 로그 동기화, 동일 브랜치 readback, exact-head CI, PR 및 safety-ref/main 비교.


## PR #50 병합 및 사후 검증 — 2026-11-18
- PR #50 `docs: independently audit and qualify CRA report conclusions` exact head `49e98df9a7fef8f47cabe7b036b45cc150b88b91`에 대해 Run #840 (ID `44200596113`) 성공 확인.
- 성공 단계: exact source blob identity, compile, CRA cross-matrix traceability, complete pytest, official CRA PDF read-only canary/artifact upload, live official CRA source read-only canary.
- Pre-merge safety ref `safety/pre-merge-cra-integrated-report-audit-2026-11-18`는 PR 전 main `c7b939a0fdfa559f9d68a11873c107186da423c3`와 identical.
- PR #50 squash merge 성공: `137d096123ccf5ee478292002d2c528b41981fc7`.
- Merge 후 compare: post-merge safety ref는 main 기준점에서 생성되며, main은 pre-merge safety ref 대비 정확히 1 commit ahead. 변경된 8개 파일은 PR #50 범위와 일치.
- 사후 safety ref: `safety/post-merge-pr50-2026-11-18`.
- 다음 동기화 PR에서 PROJECT_STATUS_CURRENT/README/MASTER_PLAN/SESSION_LOG/PROJECT_LOG에 PR #50 결과와 정확한 main 기준점을 기록한다.
- 운영 코드/production workflow/secrets/state/history/archive/Gemini·Discord 실행은 변경하지 않았다.

## CRA Guidance 공식 관보 원문 확보 — 2026-11-18
- Commission Guidance가 2026-11-17 OJ에 C/2026/6013 (CELEX 52026XC06013)으로 게재된 사실을 확인했다.
- 기존 Commission PDF download document 131456는 2026-11-18 현재 HTTP 404. 기존 C(2026)5252 ANFR mirror는 별도 historical copy로 보존.
- EUR-Lex OJ PDF를 CI Run #844에서 primary source로 직접 취득: 2,709,282 bytes, 61 pages, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`, fallback=False.
- OJ extracted text 255,974 chars, SHA-256 `384724af44e399cb997771e9e65ea4a5fe1dd264131d0754921bd691dd1f7720`.
- C(2026)5252 mirror와 OJ PDF 모두 numbered paragraph IDs 1–257 확인. 정규화 token multiset overlap 99.50% / 99.66%; exact byte/text identity는 주장하지 않는다.
- G-001–G-013 claim register의 source ID 및 page locator를 OJ pagination으로 이관했다. 상세 비교 및 limitations는 Guidance/M606 audit report §7과 provenance JSON을 참조.
- Run #844 (44204376214), exact head `0957ad4b3e85a8bb245c6b3adc62b7daec1a09de`: 156 passed, 1 xfailed; compile, source blob pins, CRA traceability, three PDF sources, official HTML canary success. Artifact ID 14381529964, digest sha256:a55dba42db13ed7c350c39e62a158bf512686b6892857870056212e8b3a7a6ae.
- 다음: claim-by-claim substantive redline, OJ page/image locator spot-check, matrix cross-link review, M/606 latest source provenance review.

## PR #52 validator 보정 및 최종 exact-head CI — 2026-11-18
- Run #851에서 CRA traceability validator가 G-001–G-013 evidence status에 기존 문자열 `ANFR mirror raw-byte SHA-256 verified`를 요구해 실패했다. 이는 새로운 OJ source를 추가한 뒤에도 historical mirror provenance phrase를 유지해야 하는 기존 검증 계약을 반영하지 못한 문서 변경 문제였다.
- CSV에 historical mirror-only hash scope 문구를 보존하고, `cra_traceability.py`가 기존 mirror source와 신규 OJ source를 각각 검증하도록 개선했다. OJ source 누락 및 OJ fallback 사용을 거부하는 회귀 테스트 2개 추가.
- Workflow source blob pin 갱신 후 PR #52 exact-head Run #854 success: 158 passed, 1 xfailed; source identity, compile, CRA traceability, full pytest, PDF/HTML canaries 모두 성공.
- Run #854 tested head: `0ab0fc4d9b217a4994fd6e7a1b32607c854bb693`.
- Artifact #14382388555, digest `sha256:9e8dc7f1c1d90015b7738263155ca9d6b1170aaea75ea6bd17350aeff7d36af7`, expiry 2026-11-25 00:09:59 UTC.
- 다음: Run #854 검증 후 provenance/status metadata 업데이트를 포함한 최종 PR head를 다시 CI로 검증한 다음 병합한다.

## PR #52 Run #857 성공 및 provenance readback — 2026-11-18
- Exact head `152fe0bfe00c16ab32f7cc030efcde3258b73525`의 Run #857 / ID `44205723336` success 확인.
- 158 passed, 1 xfailed; source blob identity, compile, CRA traceability, complete pytest, three-PDF canary, artifact upload, official HTML canary 모두 성공.
- OJ PDF raw hash/bytes/pages는 Run #844/#854와 동일; EUR-Lex primary fallback=False.
- Artifact #14383167818, digest `sha256:a2f05428d57897a20a485cabaab17cbb976dcb91f6e5628ece0953ddfe22140d`.
- Provenance JSON의 latest_verification을 Run #857로 갱신했다. 이 metadata 변경 후 새 exact-head CI를 수행한 뒤 PR #52 병합한다.

## PR #52 병합 및 사후 기준점 — 2026-11-18
- PR #52 merged squash: `d3956b7b364c507b8d59dcfc056763f2829ea867`.
- Exact head Run #861 / ID `44205897044`: success; 158 passed, 1 xfailed; source blob integrity, compile, CRA traceability, full pytest, three-PDF acquisition, artifact upload, official HTML canary passed.
- Tested head: `dee79027a49dfbb1fdd7cf1036bc0ae39e83b518`; artifact #14384061014, digest `sha256:2b70d0f09f620c83a531f2ec9be9de6a1ec9a669ee861e16704804fe036eb3d3`.
- Pre-merge safety ref matched main `854d66fa6c145ca264dbd768c2c75fcf9f117153`; main after merge was one commit ahead with exactly PR #52's 15 files. Post-merge ref created at merged main.
- Next: substantive redline of all 13 Guidance claims against OJ C/2026/6013; then matrix link and page-image recheck.

## OJ C/2026/6013 Guidance claim substantive redline — 2026-11-18
- Reviewed G-001–G-013 against official OJ PDF text and rendered page images.
- Visually checked pages 7–10, 24–25, 30, 32–35, 42–46, 53 and 61.
- Confirmed 9 claims; corrected G-001 locator to §2.4 para.25/p.7; refined G-003 (remove unsupported “interfaces/product-level mitigations” from §2.6 locator), G-008 (separate external risks from integrated-component due diligence), and G-013 (identical spare-part conditions/examples 37–39); expanded G-004 to note continuing conformity/DoC/CE/vulnerability obligations.
- Claim register and audit report §8 updated. Guidance remains non-binding; legal duties are derived from the Regulation, not the Guidance paraphrase.
- No product-specific classification or conformity conclusions changed. Unknown gates preserved.
- Next: semantic review of G-001–G-013 links to CRA-001–035, 15 IF interfaces and 36 SEC controls; then M/606 source/provenance review.

## Guidance–matrix 양방향 링크 감사 — 2026-11-18
- 13 claims, 35 requirements, 15 interfaces, 36 SEC controls의 claim-to-matrix references를 프로그램으로 대조.
- 첫 검사에서 G-002의 IF-001–IF-013 범위 shorthand와 G-005→IF-015의 reverse link 누락을 발견.
- G-002는 explicit IDs로 확장, IF-015는 G-005를 포함하도록 보완.
- 재검사 결과 누락 링크 0, dangling Guidance claim IDs 0.
- Requirements/IF/SEC matrices의 Commission Guidance URL을 EUR-Lex OJ C/2026/6013 ELI primary link + 기존 Commission page secondary link로 정합화.
- 교차 매트릭스 감사 보고서 최신 섹션 갱신.
- 다음: M/606 C(2026) 7861 Annex raw provenance, ESO adoption dates 및 OJ harmonised-standard citation status 독립 검증.

## CRA Guidance cross-matrix validator 강화 — 2026-11-18
- Manual bidirectional audit found G-002 IF range shorthand and G-005/IF-015 reverse-link inconsistency; both corrected.
- Extended `cra_traceability.py` to verify every claim-register related requirement/interface/SEC ID exists and has a reverse Guidance claim ID, and every matrix Guidance claim ID links back to the corresponding claim row.
- Added three regression tests for missing reverse link, dangling matrix claim ID and unknown related interface ID.
- Workflow exact blob pins updated for validator and tests. New PR exact-head CI required.

## PR #54 Guidance redline/validator CI — 2026-11-18
- Exact head `1d5ae716cc6683365f4da6236d15bb9b32be1e52`, Run #865 / ID `44207426703`: success.
- 161 passed, 1 xfailed; source blob identity, compile, CRA traceability with bidirectional links, full pytest, three-PDF live canary, artifact upload and official HTML canary passed.
- Artifact #14383728315, digest `sha256:03b260173f643a68841f54c9f9ac1b3d99c9064762a677ed310160618170f8bb`.
- Pre-merge safety ref identical to main at base `d92f14f6c275bf6b3fa0c8243ac696dca0358d50`.
- Metadata updated after Run #865; rerun exact-head CI before merge.

## PR #54 병합 및 복구 기준점 — 2026-11-18
- PR #54 merged squash: `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Run #868 / ID `44207582798` exact-head success: 161 passed, 1 xfailed; source blob identity, compile, bidirectional CRA traceability, full pytest, PDF/HTML canaries passed.
- Pre-merge safety ref matched main at base `d92f14f6c275bf6b3fa0c8243ac696dca0358d50`; post-merge ref `safety/post-merge-cra-guidance-claim-redline-2026-11-18` identical to main.
- Next: M/606 C(2026) 7861 Annex raw source provenance, ESO adoption dates and OJ harmonised-standard status.

## PR #56 merge and recovery checkpoint — 2026-11-18
- PR #56 squash merge: `9e42dbd790816b4669793f5bbb9edc4b4686e195`.
- Run #879 / ID `44209828986` exact-head success: 161 passed, 1 xfailed; source blob integrity, compile, CRA traceability, full pytest, official PDF and live official-source canaries passed.
- Pre-merge safety ref matched main at `adc22e3087009db51acff53ec29054f971fa508a`; post-merge safety ref `safety/post-merge-m606-annex-eso-2026-11-18` identical to main.
- June ESO PDF is scanned/image-based and excluded from text-layer CI; visual findings remain supplementary and not CI-hashed evidence.
- Next: current ESO stage evidence and OJ index refresh.


## ETSI M/606 최신 Work Programme 점검
- ETSI 공식 Work Item Plan의 2026-11-17 / Version 2.3.3 스냅샷을 확인했다. M/606 활성 work items는 18개로 표시된다.
- EN 304 636 방화벽/IDS/IPS와 EN 304 625 물리·가상 네트워크 인터페이스의 상태 및 adoption/publication/OJ 목표 일정을 상세 보고서에 기록했다.
- Commission harmonised standards index를 재조회했다. OJ 참조는 실제 게재되어야 하며, 현재 페이지에서 CRA 전용 항목을 식별하지 못했다. 검색 범위를 넘는 절대적 부재 주장이나 추정 적합성 주장은 하지 않는다.
- ETSI 계획의 OJ publication date는 미래 목표 일정이지 실제 OJ 인용이 아니다. 네트워크 포트가 있는 서보 드라이브가 자동으로 네트워크 인터페이스 제품이 되지 않으며, 내장 필터링만으로 방화벽 제품이 되지 않는다.
- 상세 기록: `reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md`.
- 후속: CEN/CENELEC EN 40000 및 산업용 OT prEN 50770 작업의 최신 공식 상태를 확인한다.


## PR #57 관리 문서 merge readback
- PR #57 merge commit `ff3c5b7875131ef92e3fe4a7974f4420ddfcc84c` 및 `safety/post-merge-pr57-2026-11-18`를 확인했다. safety ref와 main은 identical.
- PR #57은 docs-only이며 해당 merge commit에 연결된 CI run은 확인되지 않았다. 성공 CI라고 기록하지 않는다.


## PR #58 병합 및 CI 확인
- PR #58 `docs: refresh ETSI M606 work item and OJ status` squash merge: `88d5eacd71c4267f64f674f0e990a25ed6fafd3a`.
- Exact-head Run #883 / ID `44210773892` success; tested head `da1b0dce8460b84ddae5d58bd744d382d4b07e7d`; 161 passed, 1 xfailed.
- Source blob identity, compile, CRA cross-matrix, full pytest, three official CRA PDF source hashes, evidence artifact upload, nine-source official HTML canary 모두 통과.
- Artifact #14385358813, digest `sha256:407da234ac5ad37821bd5d00b7e0872f8abddc28932b1db9f32a14b76aacf1d4`, expires 2026-11-25 00:48:28 UTC.
- Pre-merge safety ref `safety/pre-merge-etsi-m606-status-2026-11-18` matched main at base; post-merge ref `safety/post-merge-pr58-2026-11-18` identical to main.
- Next: CEN/CENELEC EN 40000 and industrial OT prEN 50770 status review; distinguish official catalogue evidence from secondary aggregators.


## CEN/CENELEC 공식 EN 40000 / OT prEN 50770 점검 및 정정
- CEN 공식 EN 40000-1-1:2026 레코드를 직접 확인: Status Published, DOR 2026-11-02, DAV 2026-11-18, OJ field “No citation expected”. 발행 완료와 CRA Article 27 추정 적합성을 분리하도록 기존 포괄 표현을 정정했다.
- EN 40000-1-2:2026은 2026-11-02 ratification 및 No citation expected가 tracker/2차 카탈로그에서 확인됐지만, 공식 개별 레코드 fetch는 HTTP 500으로 실패해 직접 readback 미완료.
- CEN FprEN 40000-1-3:2026 공식 레코드: Under Approval / Citation expected.
- CENELEC 공식 레코드 prEN 50770-1~6: 모두 Committee stage, Citation expected. 각 제품 scope와 서보 드라이브 직접 적용 경계를 상세 보고서에 기록.
- CRA OJ citation은 조회한 Commission index에서 미식별. “Citation expected”는 actual OJ citation이 아니다.
- 산출물: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md`, CSV 추적표, 통합 보고서 및 상태판 갱신.
- 다음: EN 40000-1-1/1-2 발행본 확보·검증, CENELEC OT 표준 stage 재조회 및 OJ 재검증.


## PR #60 병합 및 검증
- PR #60 squash merge: `1f39cb31d7f5e3466f1b22b798e9fc51971542da`.
- Exact-head Run #887 / ID `44214446339` success; tested head `1707d49cdc7d24d5f3de43606e4bc31451e9bf8f`; **161 passed, 1 xfailed**.
- Official PDF 3종 fetch/hash, nine-source HTML canary, source blob integrity, compile 및 CRA traceability 통과.
- Artifact #14386734709; digest `sha256:aa960c3ecc5e9e89a2f64fc038ccc92cb77a9b7180e58eb5788152752ccd949c`.
- Pre-merge ref `safety/pre-merge-cen-ot-status-2026-11-18`와 base main 동일; post-merge ref `safety/post-merge-pr60-2026-11-18`와 main 동일.



## CRA 요구사항–증거 추적 매트릭스 작성
- main 기준점: `e461c6246a90f3a6035ba2044da800ba349352f7`.
- 안전 기준 ref: `safety/pre-cra-evidence-matrix-2026-11-18`.
- 작업 브랜치: `cra/requirements-to-evidence-matrix-2026-11-18`.
- EN 40000-1-2 공개 scope는 일반 사이버보안 원칙, 제품 위험평가·처리, 생애주기 활동이다. iTeh 카탈로그는 2026-11-18 기준 Not Published / stage 6055 Publishing으로 표시한다. CEN 공식 개별 상세 페이지는 HTTP 500으로 성공적 readback 미완료.
- EN 40000-1-3은 CEN 공식 레코드 Under Approval. 공개 scope의 SBOM, 취약점 식별/문서화, 수정, 테스트, 조정 공개, 보안 업데이트·권고문 주제만 참고했다.
- EVD-01–EVD-16 16개 행의 법적 locator, 드라이브 통제·시험 제안, 최소 증거 패키지, 표준 연결, 우선순위 및 Unknown 상태를 Markdown/CSV로 작성.
- 법적 요구와 제안된 구현 예시를 분리하고, 최종 표준 조항을 추정하지 않았다. 제품별 증거 미제공으로 구현 상태를 모두 Unknown / evidence pending으로 유지.
- 상세: `reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.md`, `reports/CRA_REQUIREMENTS_TO_EVIDENCE_MATRIX_2026-11-18.csv`.
- 후속: Markdown/CSV ID 및 행 수 검증, 관리 문서 readback, exact-head isolated CI, PR merge 및 safety ref 정합성 확인.

## PR #62 1차 exact-head CI
- PR #62 초기 head: `360e83bba86a01bc83731ecd5ea5d0a6b975a8f6`.
- Run #891 / ID `44217500114`: success; **161 passed, 1 xfailed**.
- Steps: source blob integrity, compile, CRA cross-matrix traceability, full pytest, 3 Commission official PDF fetch/hash, artifact upload, 9-source official HTML canary 모두 성공.
- Artifact #14388303196; SHA-256 digest `47528b6e72af65dd95130a86a1442ac8f795a6eb3c34d93656369bf94734a2c2`; expiry 2026-11-25 01:40:17 UTC.
- 이 CI 결과 metadata를 관리 문서에 추가했으므로 최종 변경 head에서 CI를 재실행한다. 아직 merge하지 않았다.


## PR #62 병합 및 사후 복구 검증
- PR #62 squash merge commit: `612285ed720310cebd82340dc2e3b150e2c6f80a`.
- Final exact-head `3947e25ba1717caea3e4099404da800ba349352f7`, Run #896 / ID `44217724257`: success; **161 passed, 1 xfailed**.
- Source blob identity, compile, CRA traceability, 3 official Commission PDF fetch/hash, 9-source official HTML canary 통과.
- Artifact #14389685192; digest `sha256:e11bcbf277f32b7386e72fb063fdfac2b19e896473e30c8e775522b7f6c55d85`; expiry 2026-11-25 01:41:53 UTC.
- Pre-merge safety ref `safety/pre-cra-evidence-matrix-2026-11-18`; post-merge ref `safety/post-merge-pr62-2026-11-18`; post-ref와 main identical 확인.
- 제품별 EVD 상태는 모두 Unknown / evidence pending 유지. 다음 작업은 제품 P0 자료 intake 및 표준 최종본 clause redline.


## M/606 개정 결정 조사 및 기존 일정 정정
- 새 공식 자료 확인: European Commission CRA standardisation 페이지는 2026-11-10 M/606 개정을 명시(페이지 최종 업데이트 2026-11-12).
- C(2026) 7861 final 본문: 2026-11-10, Article 1은 Annex I 대체; Article 2는 ESO 수령 후 1개월 이내 비수락 통지 시 개정 결정 중단 조건.
- 새 Annex I adoption deadline: item 1/15 = 2026-11-30; items 2–14 = 2027-10-30; vertical items 16–41 = 2027-01-31.
- 기존 2026-10-30 납기 서술은 최신 상태로 superseded. 기존 이력은 유지하되 정정 링크/현재 일정 추가.
- 결정문 공개 PDF 사본은 비공식 도메인에서 확보했으며 Commission 공식 CRA 표준화 페이지에서 개정 사실을 교차 확인했다. ESO receipt/non-acceptance 상태는 미확인.
- 보고서: `reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md`; CEN/OT 상태 보고서도 개정 일정 주석 추가.


## PR #64 initial exact-head CI
- PR #64 initial head `ff548d64b109e95c9f63fa0666ba419f9545e11f`, Run #900 / ID `44219718958`: success.
- pytest: **161 passed, 1 xfailed**. Source blob identity, compile, CRA cross-matrix traceability, 9 official CRA PDF source read-only canaries, artifact upload, 9-source official HTML canary passed.
- Traceability summary: 13 claims, 15 interfaces, 35 requirements, 36 SEC, 41 M/606 items; bidirectional_links=true.
- Artifact #14390620457; SHA-256 `b7ced7629ab9e88bf44190d6d4f5fd50fc91f45bfc33a83ae09a02c1833e2f20`; expires 2026-11-25 01:58:08 UTC.
- CI metadata recorded in status/docs; rerun exact-head CI after this update before merge.


## PR #64 병합 및 사후 검증
- PR #64 squash merge: `41229486baded6336aa43cd3b5de375476fe92f3`.
- 최종 exact-head `ae896286ee63916679afa4c6cc44655f1c125a4f`, Run #905 / ID `44219914781`: success, 161 passed, 1 xfailed.
- CRA traceability 13/15/35/36/41 및 bidirectional links true; 공식 CRA PDF/HTML canary 모두 통과.
- Artifact #14388899741, SHA-256 `ecd0f1181457270eb5d3d9fd5e60c2271aafc730ac1250a025499aa614f5cb8b`.
- Pre-merge `safety/pre-m606-amendment-2026-11-18`; post-merge `safety/post-merge-pr64-2026-11-18`, main과 identical.
- 다음 단계는 Article 2 절차 확인, 제품 P0 intake checklist 및 제품 분류 매트릭스.

## CRA 제품 적용성·분류 intake 초안 작성
- 서보 드라이브 제품 경계, intended purpose, reasonably foreseeable use, Article 2 연결성/제외, Annex III/IV core functionality를 구분하는 intake 보고서 작성.
- Commission Implementing Regulation (EU) 2025/2392 기술 설명을 포함하고, 네트워크 포트/부가 기능만으로 제품군을 단정하지 않는 분류 안전장치를 추가.
- 데이터시트, 매뉴얼, 블록도, 통신/원격접속, 펌웨어/업데이트, SBOM, 시험·기술문서 등을 P0 제출 패키지로 정리.
- 모델 자료가 없으므로 개별 모델 결론과 EVD 상태는 Unknown 유지.


## PR #65/#66 및 제품 분류 원문 재검토
- PR #65 merge `d1f96fa6bba297e31ed47ae1b96f59421c55b774`, Run #908: 161 passed, 1 xfailed; post-merge safety ref와 main identical.
- PR #66 merge `9cb62579e4f45ebf57587cc19644c370cbe80ebb`, Run #910: 161 passed, 1 xfailed; traceability/source canaries 통과; post-merge safety ref와 main identical.
- 2025/2392 EUR-Lex OJ 원문 recital (2)–(6), Annex I 기술 설명과 Article 8(1)을 재대조해 제품 분류 보고서의 통합 구성요소·core functionality·Annex IV 인증 관련 한계를 보완.
- 제품별 증거가 아직 없으므로 적용성/분류/EVD-01~16 Unknown 유지.


## PR #67 병합 및 사후 검증
- PR #67 merge commit `86af2db5fadf5098b22b39d2d6c07710ed0033ee`.
- Exact-head `58e2dc8608fc097dad87fa3ec614cb108d184fad`, Run #912 / ID `44223114411`: success; source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries 통과.
- Artifact #14391457563, SHA-256 `f172ed1762a693f626e8c5781638c557e9d5471d6750b5315a54cae9398d919c`.
- Post-merge safety `safety/post-merge-pr67-2026-11-18` == main.
- Article 2 ESO receipt/non-acceptance notice는 미확인 상태로 유지하고 추가 공식 확인을 진행.


## M/606 수락 절차 추가 검증
- CEN-CENELEC 공식 발표에 따라 원래 M/606은 2025-04-03 CEN/CENELEC/ETSI가 수락했다.
- 2026-11-10 개정 결정 C(2026)7861 Article 2의 통지/수령일 및 1개월 비수락 여부는 별도이며 확인되지 않았다. 원래 요청 수락을 개정 결정 수락으로 확대 해석하지 않도록 보고서와 상황판에 반영.


## PR #69 병합 및 사후 검증
- Merge commit `8089cb96fdeba390dafe6991b19abfa1bc5b3e25`.
- Exact-head Run #916 / ID `44223566124`: success; source integrity, compile, traceability, full pytest, official PDF/HTML canaries passed.
- Artifact #14391159512, SHA-256 `a71b8d12c9c1bb627da1b8d771ed2fda04ea179a721a1c55add3d5e28e16a1da`.
- Post-merge safety `safety/post-merge-pr69-2026-11-18` == main.
- Original M/606 accepted 2025-04-03; amendment Article 2 notification/receipt/non-acceptance status remains unconfirmed.


## PR #70 병합 및 사후 CI 진행 — 2026-11-18
- PR #70 squash merge: `ca65475db4ca53d23ee55308c9c9616a054ea756`.
- PR exact-head `b5fb2adc3eeba9d9839ff3d3519b128743cc6878`, Run #918 / ID `44223777837`: success, 161 passed, 1 xfailed; source integrity, compile, traceability, official CRA PDF/HTML canaries passed.
- Artifact #14391727520, digest `f737a27f61f2b6cd153731941c9e615e4379912d03ccfc3696f0eea7b2ad0d09`.
- Pre-merge safety `safety/pre-pr70-merge-checkpoint-2026-11-18`; post-merge `safety/post-merge-pr70-2026-11-18` == main.
- Post-merge exact-main Run #919 / ID `44228633470` on merge SHA `ca65475db4ca53d23ee55308c9c9616a054ea756`: success, 161 passed, 1 xfailed; source integrity, compile, CRA traceability, official PDF/HTML canaries passed. Artifact #14393668052, SHA-256 `3d6314562d9ac4f34d645ef3191be6e499ae2d25e829968e17658717bdf2ae22`.


## PR #71 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #71 exact head `bb5cb36598c5a6daa7982781a6db2726d81f9530`, Run #921 / ID `44228810756`: success; source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML canaries 통과.
- Artifact #14394585712, SHA-256 `cff5e21b032fd5f7de923e080de3b7b133b214da697a185efb2318ab04fbf0bc`.
- PR #71 squash merge: `adcec0a0cb94a326e6b7d9b8c242c4ae3dab4152`; pre-merge ref `safety/pre-pr71-merge-checkpoint-2026-11-18`, post-merge ref `safety/post-merge-pr71-2026-11-18`.
- Exact-main Run #922 / ID `44230377812` on merge SHA: **success**, 161 passed / 1 xfailed. Source integrity, compile, 13/15/35/36/41 CRA traceability, official PDF source canary, 9 official HTML sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Artifact #14393784949, SHA-256 `db75a58638b43fbe1798c70b7c4dad5951cb1b1f98bfa013fa771184e6cf2126`.
- Guidance Annex PDF remains mirror fallback=True; Commission OJ C/2026/6013 and M/606 Annex PDFs were fetched fallback=False. Do not describe the Guidance mirror bytes as Commission-primary identity.
- Post-merge safety ref and main are identical. PR #71 was documentation/log-only; production runtime/workflows/secrets/state/history/archive/legacy SIL 3 materials untouched.
- Next: complete row-level legal semantics/provenance audit of CRA-001–CRA-035, then synchronize the integrated report, traceability matrix, SEC matrix and independent audit. Keep model-specific applicability Unknown until product evidence arrives.


## PR #72 병합 및 사후 exact-main 검증 완료 — 2026-11-18
- PR #72 exact head `0f85cc04eb64efe961e514a59a28386b5527708c`, Run #923 success.
- Merge `293a27a8ea2a8e03f58db50bbe27d2aaea194c8d`; pre/post safety refs `safety/pre-pr72-merge-checkpoint-2026-11-18`, `safety/post-merge-pr72-2026-11-18`.
- Main exact Run #924 / ID `44230705429`: success, 161 passed / 1 xfailed; source integrity, compile, traceability, official PDF and 9-source live CRA canaries passed.
- Artifact #14394119675, digest `sha256:43a5e60b947890886baeee6c355beae857928f3c47deb9d76489244199accb3a`.
- Main and post-merge safety ref are identical. Continue by tightening product-agnostic servo-drive security architecture and its evidence links; product-specific implementation remains Unknown pending manufacturer/model evidence.


## CRA 서보 드라이브 참조 보안 아키텍처 v0.2 설계 검토 — 2026-11-18
- 기존 v0.1 도식에서 통신 입력·실시간 제어 경로와 인증/관리/업데이트 경로가 같은 흐름으로 보일 수 있는 점을 발견해 논리 경계를 분리했다.
- v0.2에 cyclic data ingress, privileged command/parameter gate, management service, secure update staging/boot verification, event monitoring을 구분했다.
- 단일 MCU + MPU/RTOS isolation vs communication/control dual-MCU 분리 선택 기준을 비교했다. 특정 아키텍처·부품을 CRA 의무로 단정하지 않는다.
- 설계 후보와 수용 기준을 EVD-01~16 및 SEC-001~036에 연결하고, malformed frame, unauthorized write, image tampering, downgrade, power-loss, interrupt/resource exhaustion, key lifecycle, log integrity 등 검증 시나리오를 명시했다.
- 제품별 회로/부품/펌웨어/프로토콜 증거 및 시험 결과가 없으므로 문서 상태는 reference design only / implementation unverified.


## PR #73 병합 및 사후 exact-main 검증 완료 — 2026-11-18
- PR #73 exact head `cd78b6694384d550ef68d7f1b7ec2972a02a663e`, Run #925 success.
- Merge `16ab607a919c6bfa4fee8dc90ab5af2ea2f53352`; pre/post safety refs `safety/pre-pr73-merge-checkpoint-2026-11-18`, `safety/post-merge-pr73-2026-11-18`.
- Main exact Run #926 / ID `44230997446`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Artifact #14394634118, SHA-256 `cf7d6d6ef7020d5381a4a2f201f50bf3171251155459505420ffce16998ef027`.
- Main and post-merge safety ref are identical. Reference architecture v0.2 work was then started on a separate CRA branch; product-specific implementation remains unverified.


## PR #74 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #74 exact head `4ee2d73bf7bc5826c001011b17133d4a6a8071ec`, Run #927 success; merge `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`.
- Pre/post safety refs `safety/pre-pr74-merge-checkpoint-2026-11-18`, `safety/post-merge-pr74-2026-11-18`; main and post-merge ref identical.
- Main exact Run #928 / ID `44231392940`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) locator/quote canaries passed.
- Run #927 artifact #14395142564 digest `sha256:64c359db2e764f2506345e3fee3c5e20bbacacdf3e3e67d095f02caa7126b528`; Run #928 artifact #14395476337 digest `sha256:6aaf8fc76f87121e42f8190fec9568121fbd8a0005695ce8de87ff776f0d1d93`.
- 참조 보안 아키텍처 v0.2에서 실시간 데이터/관리 경로 분리, single/dual MCU 선택 기준, update/boot 검증 및 EVD/SEC 추적을 추가했다.
- 후속 MCU 벤치마킹에서는 실제 ST 부품번호가 없음을 명시하고 ST G474RE/H753XI와 TI MSPM0G3529-Q1을 공식 자료 기준 예비 비교한다. 성능 실측·최종 선정은 보류.


## PR #75 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #75 exact head `c809e834e6290dbe96f9c6e88d5615efb2765373`, Run #929 success; merge `1d7325baa592b35585fde850cf5a155988ba4cde`.
- Pre/post safety refs `safety/pre-pr75-merge-checkpoint-2026-11-18`, `safety/post-merge-pr75-2026-11-18`; main and post-merge ref identical.
- Main exact Run #930 / ID `44231956995`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) canaries passed.
- Run #929 artifact #14396015379 digest `sha256:58e88c05c8501aba2d82c8345d0f1e5222843e15c9939c174e8beaad7a55f4da`; Run #930 artifact #14395188271 digest `sha256:63017368ac7db313f298b23c24d288f9c6781c27cc26472baa6d408abb244695`.
- ST baseline candidates STM32G474RE/H753XI and TI MSPM0G3529-Q1 were compared using official manufacturer sources; actual installed ST part number remains unknown and no replacement/selection is made.
- Next: add MCU-T01–T12 same-condition measurement plan and evidence capture sheet; tests are not executed until actual board/product constraints are available.


## PR #76 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #76 exact head `30340417bf8440292c1397c3d5afb77e017f5a20`, Run #931 success; merge `48afedaf8114688a51a7e6ed695c514277bd6407`.
- Pre/post safety refs `safety/pre-pr76-merge-checkpoint-2026-11-18`, `safety/post-merge-pr76-2026-11-18`; main and post-merge ref identical.
- Main exact Run #932 / ID `44232432357`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) canaries passed.
- Run #931 artifact #14395881347 digest `sha256:11d970dd8d64782fe5c62b12d5cea11cde231f28811c5470226ab6d126a31e4a`; Run #932 artifact #14395691349 digest `sha256:ec315a8b305f9b572452d42846de38a3698d431256faff36162ddb733303385a`.
- MCU-T01~T12 test cases and result recording fields merged; all are planning items and Not Run. Next required input: actual ST MCU marking/order code and product control requirements.


## PR #77 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #77 exact head `e3a8efcd33c601eccea1d1e1c1e054d07f946f9b`, Run #933 success; merge `caa32ed9ac6679b21b619155cdf28d1b75d81c33`.
- Pre/post safety refs `safety/pre-pr77-merge-checkpoint-2026-11-18`, `safety/post-merge-pr77-2026-11-18`; main and post-merge ref identical.
- Main exact Run #934 / ID `44232761348`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) canaries passed.
- Run #933 artifact #14395517878 digest `sha256:b6218e7153590ed63f52b35dc6013e79bd38af098dafb3b0cc2149afe419138d`; Run #934 artifact #14395218493 digest `sha256:8c827f786583bb5d2f8d14224e990b194ae50bf7f1393b4b9009925d123773da`.
- PR #77 only records prior checkpoint. MCU-T01–T12 test protocol is merged, but all hardware test cases remain Not Run. Next P0: actual ST MCU part number and product control requirements.


## PR #78 병합 및 exact-main 사후 검증 완료 — 2026-11-18
- PR #78 exact head `6610ee297b00c0717863daa4734141a519b78008`, Run #935 success; merge `441b0198bcd695752d1adb053d8e077f91426a0a`.
- Pre/post safety refs `safety/pre-pr78-merge-checkpoint-2026-11-18`, `safety/post-merge-pr78-2026-11-18`; main and post-merge ref identical.
- Main exact Run #936 / ID `44233080095`: success, 161 passed / 1 xfailed; source integrity, compile, 13/15/35/36/41 traceability, 9 official sources, corrigenda and Article 13(8) canaries passed.
- Run #936 artifact #14396500899 digest `sha256:6ef8037213259261dd57bcc3b1229d50f58947092a953bbc12ffc106ee4c8a05`.
- PR #78 only records prior checkpoint. The next product-specific work requires actual ST MCU marking/order code and drive control specifications; until then MCU candidates remain preliminary and all MCU-T01~T12 tests remain Not Run.
