# CRA 프로젝트 현재 상태 — 2026-11-18 KST

> 이 문서는 2026-11-18 재개 시점의 최신 상태 스냅샷이다. 기존 날짜별 SESSION_LOG 및 PROJECT_LOG의 역사 기록을 대체하지 않는다. 충돌 시 본 문서의 최신 main 기준 사실과 원본 PR/Actions 증거를 우선한다.

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
