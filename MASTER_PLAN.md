## 최신 재개 상태 — iX7NH Ver1.1 웹서버·Modbus TCP 1차 원문 감사 (2026-11-20)

- 현재 main 기준점: `2368b20ad90b40d473bd3cf86eac1310283ccb3f` (PR #168 상태 동기화 포함); 작업 브랜치 `research/ix7nh-v11-web-modbus-audit-2026-11-20`.
- 실질 조사: 공식 LS ELECTRIC iX7NH Ver1.1 PDF의 제12장 웹서버, 제13장 Modbus TCP, 제15장 업데이트 절차를 직접 검토하여 통합 보고서 v0.18 §39 추가.
- 확인 범위: 웹서버 ID/PW Object(0x2420/0x2421) 및 로그인·웹 업데이트, Modbus TCP Server(EtherCAT IN, 예시 TCP/502, 읽기/쓰기 기능 코드), USB OTG/FoE/DriveCM/Webserver 업데이트 경로.
- 제조사 원문: https://sol.ls-electric.com/uploads/document/16401412453260/_LSMecapion_%20iX7NH_KOR_Ver1.1_210830.pdf (추출 본문 검토; 원본 bytes/SHA-256 미확보).
- 구판 Ver1.1 증거로만 한정. 기본 인증정보 문자열은 공개 저장소에 재게시하지 않았으며, Ver1.7 현행성·취약점·TLS/서명/anti-rollback/복구는 Unknown.
- 제조사 인벤토리의 MANUAL-IX7NH-V1.1-UPDATE-SECURITY 행을 확장해 Modbus/Webserver 범위를 기록.
- 변경은 문서 전용. 운영 코드, workflow, secrets, state/history, SIL 3 보존 산출물은 수정하지 않음.
- 제품별 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run.
- 저장소 거버넌스: main `protected=false` 리스크 지속. PR exact-head CI 및 pre/post safety refs로 보완; 서버 보호 설정은 관리자 권한 작업 필요.

---

## 2026-11-20 — PR #167 사후 동기화 및 저장소 보호 점검
- PR #167 merge SHA `7f9c35c54f93505f541198f3ceef723540f4df72`; exact head `dace5c2b1c61e295e8aea6fef18d08fc4c09236d`; Run #1138 success, **174 passed / 0 failed**.
- Provenance artifact #14609352656 SHA-256 `1c9f5f187223cb6d9b8b4780eedc04cb1739bc9433d153ed38abb309e7517c63`; pre/post safety refs 생성 및 post == main 확인.
- PR #166 연구 결과: 보고서 v0.17 §38, 인벤토리 26행, JSONL 260건.
- **거버넌스 리스크:** GitHub main branch API reports `protected=false`; required checks are not server-enforced. Continue exact-head CI/manual merge/pre-post safety refs. Repository admin should configure a main ruleset requiring PR and the CI workflow. Current connected GitHub tools expose read-only ruleset/branch-protection endpoints, so no server-side setting was changed.
- 다음 P0: iX7NH Ver1.7/OS update guide/Modbus API originals; per-path auth/TLS/authorization/signature/anti-rollback/recovery evidence; PEGA2/iX700M ESI & SKU mapping.

---

## 2026-11-20 — PR #166 병합 및 iX7NH 통신면 분석 기준점
- PR #166 merge SHA `761b3ccffc142f11cbfe0d0dfb0e905b5d368ecb`; exact head `fa7120c73cbe6fe244319a8d1b1e7bc699b47259`; Run #1136 success, **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, EVD crosswalk 16, product evidence 15, bidirectional true, M/606 41, JSONL 259.
- Provenance artifact #14609257372 SHA-256 `e23c851495214060b6749de728888f6b7ea662fa1bf0ced9b42eb1179427d851`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- 보고서 v0.17 §38, 제조사 인벤토리 26행, JSONL 259건 main 반영.
- 다음 P0: iX7NH Ver1.7 매뉴얼 및 2025-12-24 표준 O/S 업데이트 영상 원본 확보; Modbus TCP API PDF/ZIP 내용 확인; USB OTG/FoE/EoE/Modbus TCP/웹서버별 인증·권한·TLS·서명·anti-rollback·복구 증거 확보. 현행 제품 보안상태는 Unknown 유지.

---

## 2026-11-20 — iX7NH 통신·원격설정 공격면 분석 P0
- 공식 iX7NH Series PDF (문서 하단 2021.05)를 텍스트 검토: USB OTG firmware update/parameter backup-restore/alarm-history export; EtherCAT FoE; EoE/UDP parameter configuration/copy; CoE/CiA402; Modbus TCP; built-in webserver/remote commissioning; STO1/STO2 + EDM.
- 이 기능들을 USB update, FoE, EoE, Modbus TCP, web, backup/restore, log/export 별 보안 검증질문으로 분해해 보고서 §38에 반영한다.
- STO 존재를 SIL/PL 등급 또는 CRA 사이버보안 통제로 해석하지 않는다. CE LVD/EMC 및 UL 인증 목록도 CRA conformity evidence가 아니다.
- 제조사 listing-only 자료: iX7NH standard O/S update video (2025-12-24), iX7NH training (2026-09-14), Modbus TCP API guide, CE LVD/EMC and UL certificate listings. 첨부 원본 미확보는 명시한다.
- P0: Ver1.7 manual, update video, Modbus API source package, per-path authentication/TLS/authorization/signature/anti-rollback/recovery evidence 확보.
- 제품 CRA scope/classification/Annex III-IV/RDPS Unknown; security tests Not Run.

## 2026-11-20 — PR #165 병합 기준점
- PR #165 exact head `cbdad281756ab906003e174ecaa9183270b1d41e`; Run #1134 success, **174 passed / 0 failed**.
- Traceability: claims 13, interfaces 15, requirements 35, SEC 36, crosswalk 16, product evidence 15, bidirectional true, M/606 41, JSONL 257.
- Provenance artifact #14608029442 SHA-256 `65dfbda197494eddcbad0abd6ef3d190ba8420f107c043c3ecb61423f29456d0`.
- Merge SHA `1b2a027162c45cb45b656bf4c01098c137a7183b`; pre/post safety refs created and post == main verified.

---

## 2026-11-20 — PR #164 사후 상태 동기화 검증
- PR #164 merge SHA `77e3050558869cab2624880bb1d5bfe8a9d5685c`; exact head `f0f7a51883bd66ad73f2252d8933067840c3d4c8`; Run #1132 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance upload 통과. Artifact #14609395254 SHA-256 `da47c2cf1d99bca2b067fb4836e9a7b3320d435e05cd7cf1e7859ab6ee566e0b`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- 보고서 v0.16 §36~§37, 제조사 인벤토리 20개 데이터 행. JSONL PR #164 이벤트를 append하여 257건으로 갱신.
- 다음 P0: iX7NH Ver1.7 매뉴얼 원본 확보 및 구판 대비 변경점 확인; FoE/Webserver 인증정보의 현행 여부, 기기별 고유성·변경 강제·TLS·권한·로그·펌웨어 서명·anti-rollback·복구 확인.

---

## 2026-11-20 — PR #163 사후 상태 동기화 검증
- PR #163 merge SHA `814cc6309e72461f0649b1b6d34109894cff4810`; exact head `3d1f28acb57078c59bcb3d634674f8ac279358fd`; Run #1130 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance upload 통과. Artifact #14609280243 SHA-256 `3bd36d529e45b20de019c783128a8f221bfd3debd895c65ddc640e11caf1f946`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- 현재 기준 보고서 v0.16 §37, 제조사 인벤토리 20개 데이터 행, JSONL 255건.
- 다음 P0: iX7NH Ver1.7 매뉴얼 원본 확보 및 구판 대비 변경점 확인; FoE/Webserver 초기 인증정보의 현행 여부, 기기별 고유성·변경 강제·TLS·권한·로그·펌웨어 서명·anti-rollback·복구 확인.

---

## 2026-11-20 — PR #162 병합 및 다음 P0
- PR #162 merge SHA `1d6110236984ee11387aaf2be99f239fa2f2ec1e`; exact head `903fd90709636b37f2b4ebd1abec893555955a8e`; Run #1128 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance upload 통과. Artifact #14609085450 SHA-256 `0407e5069a4f5d9698f6d9be994ffecbbc62c9dbae54b29b52cb96c39873cf4c`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- 보고서 v0.16 §37, 제조사 인벤토리 20개 행, JSONL 254건 main 반영.
- 다음 P0: iX7NH Ver1.7 원본 확보 및 Ver1.1 대비 변경점 검토; FoE/Webserver 초기 인증정보의 현행 여부·기기별 고유성·변경 강제·TLS·권한·로그·서명·anti-rollback·복구 확인. 제조사 증거 확보 전 취약점 판정 금지.

---

## 2026-11-20 — PR #161 병합 및 iX7NH 업데이트 보안 P0 조사
- PR #161 merge SHA `3e633d1b1b8312f5cb6665b44ee8a6fac43ee694`; exact head `66ed22f9ab16576b607fb70c898f71f82f860ea1`; Run #1126 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance upload 통과. Artifact #14608053214 SHA-256 `758aded424447f0d6fb74729a699ac9f856fa403d128a1db04883d9afb48ff42`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- P0: iX7NH 현행 Ver1.7 매뉴얼 본문 확보. 구판 Ver1.1에는 USB OTG/FoE/DriveCM/웹서버 4개 업데이트 경로, FoE password '00000000', 웹서버 ID/PASSWORD 기본값이 기재되어 있어 현행 펌웨어·SKU에서 유지되는지 제조사 확인.
- P0: FoE/Webserver 인증정보의 기기별 고유성/변경강제/전송 보호, HTTPS/TLS, 권한·로그·잠금·노출 경계, 펌웨어 서명/무결성/anti-rollback/복구 검증.
- Ver1.7 공식 첨부는 파일명·19.5MB·2026-06-05 첨부일 메타데이터만 확인. 다운로드는 '잘못된 접근'으로 실패. 구판 Ver1.1 내용을 현행 버전 사실로 일반화하지 않는다.

---

## 2026-11-20 — PR #160 병합 후 기준점 및 다음 작업
- PR #160 merge SHA `8bc9762efbd20ca9c7aaaddc3832745d4e6dc53e`; exact head `4f56e9b24354d25f03363127e8167a46049c5ded`; Run #1124 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance upload 통과. Provenance artifact #14606367087, SHA-256 `57dba2ea061de40faec834b3794e102e414fa2f0e13a8fd72a0af2ede1447a80`.
- Pre/post safety refs 보존, post ref == main 확인.
- 다음 P0: DriveCM Ver1.02.2 릴리스 노트의 downgrade 동작 단서를 보안 업데이트 검증 질문으로 편입; DFU/펌웨어 원본 확보와 ESI·SKU 매핑 확인 지속.

---

## 2026-11-20 — PR #159 병합 및 검증 완료
- PR #159 squash merge SHA `c43b35df267c30facbc8c8f62677e48189d24127`; exact-head Run #1122 success, **174 passed / 0 failed**.
- Source integrity, compileall, CRA traceability, official CRA PDF/10-source HTML canaries, provenance manifest upload 통과. PDF source upload은 unchanged로 skipped.
- Pre/post safety refs 생성 및 post ref == main 확인.
- Report v0.14 §35, manufacturer inventory 17 data rows, project log 250 valid JSON events main 반영.
- 다음 P0: PEGA2 EtherCAT/iX700M ESI 원본과 Vendor ID/Product Code/Revision 확보, DFU 보안 업데이트 메커니즘, L7N/L7S 지원정책 검증.

---

## 2026-11-20 — ESI·DriveCM·제품 SKU 교차검증
- 완료: ESI Ver0.98의 11개 적용 모델과 DriveCM Ver1.03.2의 지원 제품 및 PEGA2 EtherCAT/RS-485 신규 모델 변경내역을 제조사 상세 게시물에서 대조.
- 핵심 갭: ESI 공개 적용목록에는 PEGA2/iX700M 미기재, DriveCM 지원목록에는 PEGA2 포함, 제품 카탈로그에는 iX700M EtherCAT 명시. 별도 ESI 또는 controller package 존재 가능성을 열어두고 제조사 확인 전 호환/비호환 단정 금지.
- P0: PEGA2 EtherCAT·iX700M 전용 ESI 원본, Vendor ID/Product Code/Revision 및 firmware compatibility matrix 확보.
- P0: DFU update authentication/signature/integrity/rollback/recovery, L7N/L7S end-of-support 및 vulnerability handling 정책 확보.
- 첨부 원본 bytes·SHA-256 미확보; CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run 유지.

---

## 2026-11-20 — PR #157 병합 및 사후 검증
- PR #157 squash merge SHA `0ea0fba1fb37504f9d11b5c12d562c0d68f1d190`; exact-head Run #1118 success, 174 passed / 0 failed.
- Source integrity, compileall, CRA traceability, full pytest, official PDF/10-source HTML canaries, provenance upload 통과. PDF artifact 업로드는 동일 원본으로 skipped.
- Provenance artifact #14602977168; ZIP SHA-256 `aeb27bb37f157d6d3de8dcde48d4cfad56caae112ec4d5637a470eca325a4f17`.
- Pre/post safety refs 생성 및 post ref == main 확인.
- 다음 P0: 제조사 DFU/펌웨어/DriveCM 상세 첨부 원본 bytes 확보·SHA-256·서명·본문 검토 및 SKU별 업데이트/복구/지원기간 확인. 제품 CRA 판정 Unknown, 보안시험 Not Run 유지.

---



## 2026-11-20 — 제조사 펌웨어·업데이트 증거 수집 후속
- 완료: 공식 소프트웨어/가이드북 목록에서 DFU Downloader 1.00.4, L7NH 특주 O/S, DriveCM 1.03.1 가이드, DriveCM 게인 튜닝 가이드, iX7NH 교육자료의 제목·게시일을 확인하고 기존 LS메카피온 보고서 §34와 원본 자료 인벤토리에 listing-only로 추가.
- 미완료: 개별 상세 게시물 URL·첨부파일명·바이너리 bytes·SHA-256·전자서명·본문 검토.
- 우선순위 P0: DFU 업데이트 대상 SKU와 통신경로, 이미지 서명/검증, 업데이트 인증·권한, downgrade/anti-rollback, 전원차단 복구, 펌웨어 버전·지원기간 및 취약점 패치 릴리스 노트를 제조사 1차 자료로 확인.
- DriveCM 가이드에서 파라미터 쓰기권한·인증·진단로그·설정파일 처리 확인. 단, 설정 도구를 NMS/SIEM 또는 보안 통제로 확대 해석하지 않는다.
- 모든 제품별 CRA scope/classification/Annex III·IV/RDPS는 실제 SKU 및 제품 경계 증거 전까지 Unknown; security tests Not Run.
## 2026-11-20 — PR #155 병합 및 상태 동기화

- PR #155 merge SHA cd5976403f91c79beca845d8efd3f4e5f1930e23; pre/post safety refs retained; post ref identical to main.
- Exact PR head 19240925263c43c1f765463ad4e795f1767a2551; Run #1114 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; provenance artifact #14597677644. PDF source artifact upload skipped because unchanged.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #154 병합 및 상태 동기화

- PR #154 merge SHA 481d340050df4fd93689b992a374df3da2cfaa47; pre/post safety refs retained; post ref identical to main.
- Exact PR head 0e60f078ab7bb91ec599f97b117315013a03f70c; Run #1112 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; provenance artifact #14597173328. PDF source artifact upload skipped because unchanged.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #153 병합 및 상태 동기화

- PR #153 merge SHA 61c432f7c310bb8bbbf2bd2c8143b5860926ee68; pre/post safety refs retained; post ref identical to main.
- Exact PR head 84e73ec56fe375cfec52b584612d856475f5518d; Run #1110 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; provenance artifact #14597622291. PDF source artifact upload skipped because unchanged.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #152 병합 및 상태 동기화

- PR #152 merge SHA 8f2fa6af11be627dc3926dc46a28eb70c1ec23a0; pre/post safety refs retained; post ref identical to main.
- Exact PR head 95e8b887d41b7e33aa988ad83166184bb523c28c; Run #1108 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; provenance artifact #14597237413. PDF source artifact upload skipped because unchanged.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #151 병합 및 상태 동기화

- PR #151 merge SHA 05d95d7760aacd1b608e85b583069507c0b4a369; pre/post safety refs retained; post ref identical to main.
- Exact PR head 89aa425bc56fb7b3049ee10dc3effbb058b897d1; Run #1106 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; provenance artifact #14597945822. PDF source artifact upload skipped because source artifact content was unchanged from the prior run.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #150 병합 및 상태 동기화

- PR #150 merge SHA 89659bc8dc718e8f090644b3aeb2de7c1ec363d1; pre/post safety refs retained; post ref identical to main.
- Exact PR head 2c0dd8491a57d1cee9794fa6fb56e001f05bf193; Run #1104 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596532979 and #14597076911.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #149 병합 및 상태 동기화

- PR #149 merge SHA 6e04cd691d637589af69437068befe623fd46312; pre/post safety refs retained; post ref identical to main.
- Exact PR head 0e872bcf989951a446bc8263e015d786a0e51ed0; Run #1102 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596792806 and #14596862640.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #148 병합 및 상태 동기화

- PR #148 merge SHA 33d82ee31c151c4d2f19165f1c17882fc5dfe722; pre/post safety refs retained; post ref identical to main.
- Exact PR head 27a194485b7545a6c6e9c285b485822034e47815; Run #1100 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14597670650 and #14597051830.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #147 병합 및 상태 동기화

- PR #147 merge SHA 51d75213e3e035dfc7a7858570844533644aedc5; pre/post safety refs retained; post ref identical to main.
- Exact PR head 789963424610a4369930bc1f841f30160378d50b; Run #1098 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14597665320 and #14596892018.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #146 병합 및 상태 동기화

- PR #146 merge SHA bd0938484b22b4d8c6d8ad94b440de2b479a0ea2; pre/post safety refs retained; post ref identical to main.
- Exact PR head aed4a54883cdcacda59bad30f7b2a939b9b346b0; Run #1096 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14597665057 and #14597380473.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #145 병합 및 상태 동기화

- PR #145 merge SHA 482305a4d5334ef19105560d0b4a3bd012acc1d0; pre/post safety refs retained; post ref identical to main.
- Exact PR head dd536778451cb7629cf351480c41d9726b8e5365; Run #1094 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596711210 and #14596970810.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #144 병합 및 상태 동기화

- PR #144 merge SHA c616169b4300521459cc3ae78d631fcd739103fb; pre/post safety refs retained; post ref identical to main.
- Exact PR head 09ac041dbb3df72e8c3cf3dd01e53bbc80d9ff7f; Run #1092 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14597230119 and #14596691436.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #143 병합 및 상태 동기화

- PR #143 merge SHA f1157fb1b5581f55b1f192c15b1822386ce3ed1e; pre/post safety refs retained; post ref identical to main.
- Exact PR head d0aef1b098d5b1f52e83f24b5d0eb9a37e98b34d; Run #1090 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596188740 and #14595554868.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #142 병합 및 상태 동기화

- PR #142 merge SHA 0c8144a59e0741eb9538af2e8493def6fe982f33; pre/post safety refs retained; post ref identical to main.
- Exact PR head a7662c01f4c8f74790f4848a1d702ee22cb2d74a; Run #1088 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14595914125 and #14597100049.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #141 병합 및 상태 동기화

- PR #141 merge SHA f798d9d16d74e399124c207c45ee6bdb6c1339a7; pre/post safety refs retained; post ref identical to main.
- Exact PR head 468eba3d10c9d76279dfa2f64c445b11db25d288; Run #1086 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596955128 and #14595634151.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #140 병합 및 모델 인터페이스 상태 동기화

- PR #140 merge SHA 2edae2463e04b5d4280aa9d04c48f7805b554707; pre/post safety refs retained; post ref identical to main.
- Exact PR head 1f859f5431917e8202ffdcaf7141376c8712eb8e; Run #1084 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14595564027 and #14595579119.
- Main에 보고서 §31~§33, M/606 audit, vertical profile matrix, manufacturer source inventory, 14-row model-interface matrix 반영.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, inspect exact SKU ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #139 병합 및 모델 인터페이스 작업 상태 동기화

- PR #139 merge SHA 7545a771ce16f362cf5b911cd8c850efc91c2e92; pre/post safety refs retained; post ref identical to main.
- Exact PR head 28086497e73f123aef28e695a56e455ed9cc092a; Run #1082 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14596455559 and #14596296397.
- Main에 보고서 §31~§33, M/606 audit, vertical profile matrix, manufacturer source inventory, 14-row model-interface matrix 반영.
- Next P0: obtain original manufacturer PDF/XML/MSI/API ZIP/CE DoC bytes, compute SHA-256, review exact SKU ports/protocol/security controls; confirm iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — PR #138 병합 및 모델 인터페이스 증거 검증

- PR #138 merge SHA 372860cfb1a149bc5d5a7bf993e11dbf68217478; pre/post safety refs retained; post ref identical to main.
- Exact PR head 0ca7cfb745884ba8c7a1f3f383974286d0e88fd8; Run #1080 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success; artifacts #14595309514 and #14595489037.
- Report §33, 14-row model/interface matrix, source inventory, M/606 25b evidence updates merged.
- Next: acquire original manufacturer PDFs/XML/MSI/API ZIP, hash, inspect SKU-specific ports/protocols/security controls; verify iX7NH dual protocol and L7P RS-422 scope.
## 2026-11-20 — 모델별 통신 인터페이스 증거 분석

- PR #137 merge SHA 71db8880502bbd5be083e297e39acc338ea0d13a; exact-head Run #1078 success (174 passed / 0 failed); safety refs retained.
- 공식 드라이브 카탈로그에서 EtherCAT 통신형·펄스형 모델군을 분리; iX7NH Modbus TCP API guide, L7P Modbus RS-422 guide, iX700M CE model code evidence 확인.
- 모델별 인터페이스 evidence matrix 생성. ESI 0.98와 제품 카탈로그 명칭 불일치는 그대로 기록하고, 모델코드/ESI 호환성을 추정하지 않는다.
- 25b technical relevance is strong for EtherCAT/Modbus TCP interfaces; final standard scope and exact SKU applicability remain Unknown. L7P RS-422 scope requires interpretation.
- Next: exact SKU/HW/FW options, original manual/ESI/API bytes + SHA-256, port/protocol/security-function evidence, iX7NH dual-protocol configuration check.
## 2026-11-20 — PR #136 병합 및 제조사 자료 인벤토리 CI

- PR #136 squash merge SHA d7e921f5a6db04d20ce06778f6ea384dbd9c63fe; pre/post safety refs retained; post ref identical to main.
- Exact head 25215700a415b094c6c187278183b8ca15e4e4ca; Run #1076 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, source integrity, compile, traceability, pytest, provenance upload success; artifacts #14595209202 and #14595972121.
- §32 manufacturer source inventory is now in main. ESI 0.98 and PEGA2 EtherCAT variant strengthen 25b technical review, but legal applicability remains Unknown.
- Next: acquire original PDF/XML/MSI bytes, compute SHA-256, inspect model-specific communication and security functions, verify installer signature/dependencies.
## 2026-11-20 — 제조사 원본 자료 인벤토리 및 모델별 통신 경계

- PR #135 merge SHA 4299fd7301c22898cab8291dcb1a54d2a767d0cf; exact-head Run #1074 success (174 passed / 0 failed); pre/post safety refs retained.
- 제조사 공식 출처에서 DriveCM 1.03.2 지원모델, EtherCAT ESI 0.98/0.96 적용모델, PEGA2/iX700M 매뉴얼 등록정보를 확인하고 보고서 §32 및 source inventory CSV에 기록.
- ESI 0.98 model list + PEGA2 EtherCAT/RS-485 variant note로 25b technical candidate strengthened. This is not an automatic legal scope decision.
- PDF/XML/MSI bytes, SHA-256 and content-level manual/ESI review remain pending; keep all CRA classification and test statuses Unknown/Not Run.
- Next: exact model/SKU/HW/FW, download original files, hash and inspect interface/communication/security sections; inspect DriveCM installer signature and dependencies.
## 2026-11-20 — PR #134 사후 문서 동기화 및 exact-head CI

- PR #134 squash merge SHA 7162664b29554a01d2694cd027efb0191a6c3344; pre-merge safety safety/pre-pr134-merge-2026-11-20; post-merge safety safety/post-merge-pr134-2026-11-20 (main과 identical).
- Exact PR head 7a560c3d6db33f3d553f7fa9cd3596f9c7c6cd02; Actions Run #1072 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success. PDF artifact #14594883481, provenance artifact #14594828906; 7-day retention.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 모델별 원본 매뉴얼·데이터시트·DriveCM·ESI bytes/SHA-256, 정확한 SKU/HW/FW/EU 판매구성, 인터페이스 데이터흐름·보안기능 증거 확보.
## 2026-11-20 — PR #133 사후 문서 동기화 및 exact-head CI

- PR #133 squash merge SHA a889b03855e3c7683aa140220352510ab4c4c116; pre-merge safety safety/pre-pr133-merge-2026-11-20; post-merge safety safety/post-merge-pr133-2026-11-20 (main과 identical).
- Exact PR head 466b3d93db6119c3a73c8cef6bc2e55cf698294d; Actions Run #1070 success, 174 passed / 0 failed.
- Official CRA PDF/HTML canaries, compile, traceability, pytest, provenance upload success. PDF artifact #14596185499, provenance artifact #14595641444; 7-day retention.
- Main push CI는 독립 확인되지 않아 미확인으로 유지.
- 다음 P0: 제조사 원본 manual/datasheet/DriveCM/ESI bytes 확보 및 SHA-256, exact SKU/HW/FW, 통신 인터페이스·데이터 흐름·보안기능 증거 수집.
## 2026-11-20 — PR #132 병합 및 exact-head CI 검증 완료

- PR #132 squash merge SHA: f3a8fc06b2a0c5fdaa98d98ad8bc0f21abee22df; pre-merge safety: safety/pre-pr132-merge-2026-11-20; post-merge safety: safety/post-merge-pr132-2026-11-20 (main과 identical).
- Exact PR head 15df2eae8b3a5eea809496e46a412f67f0f3576e; Actions Run #1068 success, 174 passed / 0 failed.
- Source blob identity, compileall, CRA cross-matrix traceability, full pytest, official CRA PDF canary, 10-source HTML canary, manifest JSON round-trip 및 artifact upload 통과.
- Artifact #14595995557 (PDF sources, 3,070,503 bytes, SHA-256 2d3848ab2c7046b53154e3c304bee5dca5ad33bd23a00c4a5396b020922bb6ef) 및 #14595062566 (provenance, 2,567 bytes, SHA-256 657f92dd556ac2dc56ccb68278452a2e9f9422eeaec366098117c1ef52d47bc9), 7일 보존.
- PR #132에서 통합 보고서 §31, M/606 41-item 감사대장 6행, OT/IACS vertical-profile matrix 6행 및 관리 문서를 반영했다.
- main push CI는 별도 조회에서 확인되지 않았으므로 exact-head CI와 구분해 미확인으로 유지한다.
- 다음 P0: 모델별 제조사 원본 PDF/설치파일/ESI 확보와 SHA-256·페이지 검토, 제품 경계·통신 기능 증거 확보, 41개 실제 EN/ETSI/OJ 매핑 전수감사.
## 2026-11-20 — OT/IACS 수직 프로파일 6종 및 서보드라이브 경계 분석

- 기준 main HEAD: 36f170de199d2fc23e4e40969584e56c37dbebe7; 작업 브랜치 cra/ot-iacs-vertical-profile-boundary-2026-11-20; pre-work safety ref safety/pre-ot-iacs-vertical-audit-2026-11-20.
- CLC/TC 65X Work Programme과 개별 CENELEC 레코드에서 M/606 20b/21b/22b/25b/27b/36b가 prEN 50770-4/-2/-6/-3/-5/-1, project 81652/81650/81654/81651/81653/81649에 연결됨을 확인.
- 6개 프로젝트 모두 Under Drafting / Committee stage; CENELEC OJEU 필드는 Citation expected이나 actual OJ citation number/date는 없음. Article 27 presumption 없음.
- 서보드라이브 기능 경계는 보고서 §31 및 6-row CSV에 기록. 25b network interface는 조건부 우선 검토 후보. 나머지 VPN/NMS/SIEM/router-modem-switch/firewall-IDS-IPS는 현 증거로 기능 확인되지 않음.
- 제품 CRA scope/classification/Annex III·IV/RDPS Unknown, security tests Not Run 유지. 모델별 원본 매뉴얼·설치파일·ESI 확보 전 기능 부재를 확정하지 않는다.
- 다음: exact-head CI, PR review/diff, pre/post safety refs 및 main readback. 후속 우선순위는 모델별 매뉴얼 bytes/SHA-256/페이지 검토, 인터페이스별 기능·데이터흐름 증거 확보, 41개 실제 EN/ETSI 매핑·OJ 전수감사와 Article 2 ESO 통지 증거 확인.
## 2026-11-20 — PR #125 병합 후 OJ 감사 정밀화

- PR #125 merge SHA `0a5f5140e323303d6a960ca73edd8ec8c05f55f2`, exact-head CI Run #1050 success.
- EN 40000-1-1/-1-2 발행 확인과 CRA OJ citation 상태를 구분한다.
- 2차 CRA standards tracker는 CEN catalogue의 두 표준 OJ citation 기대 없음 정보를 보고하나, CEN catalogue 개별 레코드 직접 열람 전까지 잠정 2차 근거로만 관리한다.
- 다음 단계: CEN standards catalogue 개별 레코드 직접 확인, European Commission OJ harmonised standards dataset 및 EUR-Lex/OJ에서 CRA 표준 참조 확인, 이후 M/606 41개 행별 근거 업데이트.
- 상세 분석: 통합 보고서 §27.

## 2026-11-20 — M/606 표준 발행과 OJ 적합성 추정 분리

- CEN-CENELEC 2026-11-19 공식 발표에서 EN 40000-1-1/-1-2 발행을 확인했다.
- 표준 발행은 CRA 조화표준 OJ 인용과 다르다. Article 27 적합성 추정은 OJ에 실제 게재된 참조 및 그 범위에 한정한다.
- 이번 검색에서 EN 40000-1-1/-1-2의 CRA OJ 참조를 직접 확인하지 못했으나, 이를 OJ 미게재 확정으로 기록하지 않는다.
- 다음 우선순위: M/606 41개 항목 각각의 정확한 표준번호·ESO 상태·발행·OJ 참조·제한사항 전수감사 및 증거 register 구축. 일정표와 OJ 상태를 분리한다.
- 상세 분석: 통합 보고서 §27.

# CRA 서보 드라이브 마스터 계획서

## 2026-11-20 — iX700M 모델 코드 추적 단서

- 제조사 CE/LVD/EMC 게시물에 `iX700MD1-B-150B`가 명시되고 코드 정의는 D1=1축, B=480 Vac, 150=15 kW, encoder B=BiSS-C.
- 이는 SKU identification lead only. DoC PDF bytes are not acquired; do not claim CRA compliance or cybersecurity evidence from CE/LVD/EMC metadata.
- 보고서 §26 및 `sources/manufacturer/LS_MECAPION_MANUAL_INTAKE_2026-11-20.json` 기록 참조.


## 2026-11-20 — 제조사 매뉴얼 증거 수집 재시도

- iX7M/iX7NH 첨부파일 메타데이터는 확인했으나 실제 PDF 다운로드는 HTTP 502/timeout으로 실패. iX700M Ver1.4 목록도 확인했으나 첨부 상세 미확인.
- 다음은 제조사 기술지원으로 원본 PDF 요청 또는 정상 다운로드 경로 확보. PDF bytes + SHA-256 + 페이지 수 + 개정표지 확인 전 본문 내용을 인용하지 않는다.
- 증거 register: `sources/manufacturer/LS_MECAPION_MANUAL_INTAKE_2026-11-20.json`; 상세 분석은 보고서 §25.


## PR #119 병합 확인 — 2026-11-20

- Main merge SHA: `46feea8fab4924889be30f8ae5afb7a072673055`; post-merge safety ref: `safety/post-merge-pr119-2026-11-20`.
- Exact-head Run #1038 success; final OJ C/2026/6013 guidance analysis and durable PDF source manifest are in report §24 and sources/official/CRA_2026-11-19_SOURCE_MANIFEST.json.
- Next: collect LS Mecapion model-specific manuals, firmware, DriveCM/ESI original evidence; resolve product boundary, support period, update lifecycle, component due diligence and Article 14 process per §24.


## 최신 우선순위 — 2026-11-20: OJ CRA Guidance C/2026/6013

- 2026-11-17 EU 관보 C/2026/6013 최종본(61p)을 확보하고 §24에 LS메카피온 제품 적용 해설을 통합했다.
- 핵심 적용: 제품 경계/데이터 연결, core functionality, firmware substantial modification, support period, external dependencies/due diligence, family reuse, RDPS, Article 14 reporting.
- 모델별 증거가 없으므로 scope/classification/RDPS는 Unknown 유지. Article 14의 2026-09-11 적용 시점과 지원기간 종료 후에도 계속되는 보고 의무는 즉시 확인할 우선 항목이다.
- 다음 단계: 제조사 원본 매뉴얼/DriveCM/ESI 및 제품 SKU 증거를 확보해 §24의 각 Unknown을 모델별로 해소하고, 지원기간·업데이트·보고 절차 증거를 연결한다.


## PR #116 병합 확인 — 2026-11-20

- Main merge SHA: `6092ca1c61c696a716583e6bc0f7d5150cbee269`; post-merge safety ref: `safety/post-merge-pr116-2026-11-20`.
- PR #116 exact-head Run #1032 success: source integrity, compile, CRA traceability, pytest, live official CRA source manifest.
- PDF artifact는 생성/업로드되지 않았으므로 원문 PDF 확보 완료로 표시하지 않는다. Exact-main push CI는 독립 확인 전이다.
- 다음 우선순위는 EN 40000-1-1/-1-2의 OJ 상태와 -1-3/-1-4의 개발 상태, ETSI 18개별 최신 단계, M/606 41개 전체 OJ 인용, LS메카피온 원본 매뉴얼/DriveCM/ESI 확보다.


## 최신 진행 업데이트 — 2026-11-20

- M/606의 2026-11-10 개정 Annex I 납기를 C(2026) 7861 원문과 재확인했다.
- CEN-CENELEC 공식 발표(2026-11-19)에서 EN 40000-1-1 및 EN 40000-1-2 발행을 확인했다. EN 40000-1-2는 제품 위험관리·생애주기 절차의 우선 검토 자료다.
- ETSI M/606 활성 작업 18개(Work Programme v2.3.3, 2026-11-19) 중 서보드라이브와 연관성이 높은 EN 304 625(11-05), EN 304 626(11-06), EN 304 636(10-06)의 의견 분류 평가 단계를 최신 요약 목록 기준으로 업데이트했다. 11-11/11-09 상세 페이지의 이전 상태는 superseded로 처리했다.
- 계획된 Adoption/Publication/OJ 날짜를 실제 발행·OJ 인용으로 간주하지 않는다. Article 27 적합성 추정은 실제 OJ 게재 확인 후에만 기록한다.
- 다음 우선순위: EN 40000-1-1/-1-2 OJ 상태 및 EN 40000-1-3/-1-4 최신 개발 확인 → ETSI 18개 개별 상태/OJ 전수확인 → M/606 41개 OJ 인용표 완성 → LS메카피온 원본 매뉴얼·도구·ESI 파일의 해시/페이지 증거 확보.
- 세부 결과와 공식 링크: LS메카피온 통합 예비 보고서 §23. 이번 감사는 부분 최신화이며 41개 전수감사 완료가 아니다.


> **활성 범위 통제(2026-11-17): 본 계획은 CRA 대응만 다룬다.** SIL 3 기능안전 자료는 과거 산출물로 보존하지만 활성 단계·완료 기준·다음 작업에 포함하지 않는다. 별도 명시적 재개 지시가 있을 때만 독립 계획으로 다룬다.

## 목표

산업용 서보 드라이브 제조사가 EU CRA에 대응할 수 있도록 적용성 분석, 보안 요구사항 추적, 하드웨어·펌웨어·개발 프로세스 설계, 검증 증거, 한국어 보고서와 매뉴얼을 하나의 추적 가능한 체계로 만든다.

## 운영 원칙

- 운영 `main.py`와 workflow는 직접 수정하지 않고, CRA 목표에 필요한 변경만 작업 브랜치·mock/전체 테스트·CI·PR·rollback ref를 갖춰 통합한다. 사용자의 상시 진행 승인 범위에서는 반복 승인 질문을 하지 않는다. 운영 workflow 실행·비가역 외부 효과는 별도 안전 확인 대상으로 둔다.
- 조사 결과를 바로 최종 보고서로 승격하지 않는다.
- 모든 법령 주장은 공식 원문 조항·URL·원문 발췌·해석·제품 적용성을 함께 관리한다.
- 법적 의무, 표준의 요구사항, 엔지니어링 권고, 미확인 가설을 명확히 분리한다.
- 같은 주제를 반복 수집하는 것보다 기존 내용을 검증·정정·통합하는 일을 우선한다.
- 보고서 수를 늘리는 것보다 정확성, 추적성, 검증 가능성을 우선한다.
- 한국어를 기본 언어로 하고 영문 원문은 근거로 보존한다.
- 프로젝트의 공식 진행 기록은 GitHub 문서에 유지한다. 대화창은 의사소통 수단이지 단일 기록 저장소가 아니다.

## 관리 문서 구조

| 문서 | 책임 |
|---|---|
| `README.md` | 메인 페이지, 현황 요약, 주요 자료 링크 |
| `PROJECT_STATUS_CURRENT.md` | 현재 사실·상태·위험·다음 재개 지점 (최신 기준) |
| `PROJECT_STATUS.md` | 2026-11-17 이전의 역사적 스냅샷 보존; 현재 상태의 기준으로 사용하지 않음 |
| `MASTER_PLAN.md` | 목표·우선순위·단계·완료 기준 |
| `AI_RULEBOOK.md` | 조사·검증·코드·기록 행동강령 |
| `SESSION_LOG.md` | 작업별 변경·검증·미완료 기록 |
| `reports/` | 상세 감사·설계·정정·통합 보고서 |
| `tests/` | mock/unit test와 테스트 실행 지침 |

## 단계 및 완료 기준

### Phase 0 — 운영 현황과 보안 기준선
- 저장소 트리, 공개 범위, Actions, workflow, state/history, 최근 아카이브를 점검
- 비밀정보·개인정보·고객사 기밀이 공개 저장소에 들어가지 않도록 점검
- 특수문자 파일명과 중복 상태파일 조사
- 완료 기준: 현재 구조와 위험이 상황판에 기록되고 미확인 사항이 분리됨

### Phase 1 — 조사 품질 개선
- 최근 보고서 표본을 공식 EUR-Lex 원문과 대조
- 조항 번호, 적용 시점, 보고 시한, 용어, 원문 인용 검증
- 출처 URL·접근일·원문 발췌·해석·신뢰 상태 기록
- 완료 기준: 정정 전/후가 추적되고 근거가 재검증 가능함

### Phase 2 — 자동화 코드 신뢰성
- 모델 전부 실패 시 실패 종료 및 실패 상태 저장
- 응답이 비어 있거나 오류 문구인 경우 보고서 성공 처리 금지
- state/history 입력 검증 및 시간 처리
- HTTP timeout/status/retry/backoff 처리
- 조사 결과의 URL·법령 조항·인용 검증 메타데이터 보존
- 중복 주제 인덱싱 및 정정 이력
- 실행 성공, 조사 생성 성공, 근거 검증 성공을 별도 상태로 분리
- 통상적인 CRA 범위 변경은 사용자의 상시 진행 승인에 따라 작업 브랜치에서 수행하고, 영향분석·테스트·복구 경로·CI를 확인한 후 PR로 통합

### Phase 3 — 테스트 및 CI
- 모델 호출·Discord 전송·Git push를 mock 처리한 단위 테스트
- 모델 전부 실패, 빈 응답, Discord 오류, Git push 실패, quota 경계 테스트
- workflow에 lint/test 단계를 별도 구성
- 완료 기준: 저장소 전체 테스트 로그와 CI 링크가 남고 실패 경로가 실제 검증됨

### Phase 4 — CRA 요구사항 추적표
- CRA 조항 / Annex I 요구사항 / 적용성 / 설계 통제 / 검증 방법 / 증거 / 담당을 연결
- 제품 범위·용도·시장 출시 형태·구성요소·연결 기능을 확인해 적용성을 판단
- ST MCU를 기본 설계 비교 기준으로 삼고 TI MCU/솔루션은 비교 항목으로 유지
- 완료 기준: 각 요구사항에 상태와 객관적 근거가 연결됨

### Phase 5 — 하드웨어·펌웨어·운영 설계
- 보안 부팅, 펌웨어 무결성, 디버그 포트, 인증·권한, 통신 인터페이스, 업데이트/복구, 키 관리, 로그, SBOM 등 검토
- 활성 범위는 CRA 사이버보안 요구사항만 포함한다. 기능안전/SIL 설계·검증은 활성 범위에서 제외하며 별도 명시 지시 없이는 진행하지 않는다.
- 안전 관련 변경은 영향분석 및 전문 검토 없이 확정하지 않음

### Phase 6 — 통합 문서화
- 단일 통합 보고서 + 필요한 부속서(요구사항 추적표, 시험 증거, 설계 상세, 용어집)
- 문서마다 동일한 사실을 중복 기재하지 않고 기준 문서와 상호 링크
- 변경 이력과 검토 상태 유지
- 한국어 최종 보고서, 매뉴얼, 발표자료, 표/데이터 파일 생성

## 현재 진행 상태 — 2026-11-19

- PR #90에서 EVD-01~16 책임 역할·생애주기·검증 방법·내부 합격 게이트를 반영했다.
- PR #91에서 EVD→CRA→SEC 후보 교차표 및 fail-closed validator를 main에 통합했다. PR exact-head Run #971 및 exact-main Run #972 모두 success, 166 passed / 0 failed.
- PR #92에서 PR #91 사후 검증 기준을 README/상황판/로그에 동기화했다. exact-head Run #973 및 exact-main Run #974 모두 success, 166 passed / 0 failed; main `0e06f5672f2477f95f7b1088ee0299a7c336082e`.
- SEC-001~036 전체 연결, CRA/SEC 외래키, EVD-01~16 누락/중복 및 orphaned control을 자동 검사한다. 연결 자체는 제품 적용성·구현·시험 Pass를 의미하지 않는다.
- 다음 단계는 제품별 P0 자료 확보 후 각 후보 링크를 적용/비적용/조건부로 판정하고 제품 버전별 증거를 수집하는 것이다.
- 제품별 모델/SKU, BOM, 매뉴얼, 실제 MCU 부품번호 및 제어 사양은 미확인으로 유지한다.
- PR #93 status-sync exact-head Run #975 및 exact-main Run #976 모두 success, 166 passed / 0 failed.
- PR #94에서 E-001~E-015 제품 증거 register 및 provenance/state promotion gates를 main에 통합했다. Exact-head Run #977 및 exact-main Run #978 모두 success, 172 passed / 0 failed.
- PR #95 status-sync exact-head Run #979 및 exact-main Run #980 모두 success, 172 passed / 0 failed; safety post-ref와 main 동일성을 확인했다.
- PR #96 status-sync exact-head Run #981 및 exact-main Run #982 모두 success, 172 passed / 0 failed.

## 현재 진행 상태 — 2026-11-17

- Phase 1 표본 감사 및 #28/#29 정정본 작성: 수행
- Phase 2 P0 모델 응답 검증/실패 차단: 작업 브랜치 구현 및 격리 mock 테스트 9 passed 기록
- Phase 2 P1-A state/history 검증 및 datetime 호환: 작업 브랜치 구현, helper 독립 pytest 7 passed
- Phase 3 기본 원본 테스트 실행 기반: 확보. 테스트 전용 GitHub Actions Run #1~#3 success, 최신 Run #3에서 SHA 5개 일치, compileall 통과, pytest 21 passed
- Phase 2 P1-B1 Discord 전송 및 P1-B2 atomic persistence: 작업 브랜치 구현·CI 검증 완료; P1-B3 Git sync/P1-B4 구조 개선은 미구현
- Phase 4: CRA 요구사항 추적표 v0.2(35항목) 작성. 제품별 증거·설계 통제·시험 결과 연결은 진행 중.
- 서보 드라이브 인터페이스별 CRA 적용성 매트릭스 15항목 작성. 실제 모델 회로·프로토콜·의도된 사용 검증 전 잠정.
- CRA 보안 통제·시험 매트릭스 36항목 작성, 35개 요구사항 추적 ID와 연결. 각 구현 후보는 법정 단일 구현방식이 아닌 위험기반 선택지로 표시; 제품별 시험은 미실시.
- CRA 서보 드라이브 참조 보안 아키텍처 v0.1 PR #23 병합 및 main readback 완료: 논리 블록, trust boundary, data flow, HW/FW/network control candidates. 실제 부품/회로에 맞춘 설계는 제품 자료 확보 후 진행.
- Phase 6: CRA 통합 규제·기술 준수 보고서 v0.2 보강 및 PR #21 병합 완료. 2026-07 Commission Guidance 및 2026-11 M/606 개정 반영. 제품별 판정 전.
- Phase 2/3 CRA source provenance: PR #26 병합 완료. CELLAR official source 7건 + Commission page 2건, source SHA manifest, claim/paragraph/Annex locator validator, fail-closed source gate. Run #573: 138 passed / 1 xfailed; live 9-source canary와 Article 13(8) quote 확인.

## 2026-11-17 최신 재개 지점 — CRA source provenance 통합 완료

- canonical 운영 브랜치는 `main`이다. 최신 source provenance merge commit은 `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- PR #26에서 source/claim gate 선택 이식과 CELLAR official source retrieval을 완료했다. [검증 보고서](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md)를 상세 근거로 사용한다.
- PR #26 Actions Run #573: 138 passed / 1 xfailed; official source 9개 live fetch 및 Article 13(8) locator/quote canary 성공. PR head SHA는 `d1bda523c1b593bbd48bf4916dd7bbd741001894`; merge commit 자체의 별도 CI는 아직 확인되지 않았다.
- 운영 main의 history 15, retry 2, quota/429/503 no-op, duplicate-topic suppression, transactional persistence/rollback은 유지했다.
- Commission Guidance C(2026)5252 ANFR mirror 및 M/606 C(2026)7861 Commission Annex PDF를 실제 다운로드·파싱·raw SHA-256 검증했다. Commission-hosted Guidance primary byte identity만 미확인.
- 다음 우선순위는 PDF/decision Annex 수집, Article/Annex live locator 확대, 35 requirements/15 interfaces/36 SEC controls와 source claim 및 제품별 증거 연결이다.
- divergent branches 전체 병합 금지, force-push/history rewrite 금지. 과거 SIL 3 산출물은 역사 기록으로 보존하고 CRA 계획에 포함하지 않는다.

## 다음 실행 순서 — 2026-11-17 CRA 우선순위

1. **공식 부속문서 수집**: Commission Guidance C(2026) 5252 PDF 원문/Annex 및 M/606 결정 C(2026) 7861 Annex를 별도 수집·파싱하고 페이지 locator, source URL, retrieval time, SHA-256을 기록한다. 현재 source pack은 관련 URL만 기록하며 PDF/decision Annex 본문은 미수집이다.
2. **locator 검증 범위 확대**: Article 13(8) 외 Article 주요 paragraph, Annex I Part I/Part II point를 live source text에서 검증하는 canary와 regression test를 추가한다.
3. **요구사항·통제 추적 통합**: 35개 CRA 요구사항, 15개 인터페이스, 36개 SEC 통제/시험 항목에 source claim ID, 설계 통제, 검증 방법, 시험 결과, 증거 링크를 연결한다.
4. **제품 적용성·분류**: 실제 모델·회로·펌웨어·프로토콜·디지털 데이터 흐름·원격 처리·EU 공급 주체 자료가 확보되면 Annex III/IV core functionality 및 Article 32 경로를 검증한다. 미제공 사항은 잠정으로 유지한다.
5. **통합 보고서·매뉴얼**: 기존 v0.2 보고서와 38개 정정 보고서를 기준으로 신규 근거를 통합하고, 법적 의무·공식 해석·엔지니어링 권고·미확인 가설을 구분한다.
6. **CI/운영 관찰**: main merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`의 post-merge CI를 확인한다. 운영 Gemini/Discord 실행은 운영 모니터링 범위에서만 관찰하며 테스트 목적으로 실행하지 않는다.
7. **문서 정합성**: README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl을 같은 사건 ID/commit 기준으로 갱신하고 JSONL·CSV·문서 링크를 재검증한다.

기능 코드나 운영 workflow 변경은 CRA 산출물에 실제 필요성이 확인된 경우에만 별도 영향분석·테스트·롤백 계획을 수립한다. 과거 P1-B3/P1-B4 계획은 현재 CRA 보고서의 선행 조건으로 취급하지 않는다.

## 완료 정의

작업이 완료됐다고 말하려면 다음을 모두 만족해야 한다.
1. 공식 원문과 조항 번호 확인
2. 적용성 및 전제조건 명시
3. 독립된 근거 또는 교차 검증
4. 설계·시험·문서 증거 연결
5. 코드 변경 시 관련 mock/unit test와 CI 통과(실행 범위 명시)
6. 미해결 사항·제약·사람의 승인 필요 지점 명시
7. GitHub 저장 파일 재조회 및 변경 내역 확인



## 2026-11-14 추가 실행 게이트 — 테스트 신뢰성

### P0 선행 조건
- 저장소 원본 파일의 Git blob SHA가 실행환경의 테스트 대상과 일치해야 한다.
- SHA 불일치 사본의 테스트 결과는 예비 검증이며 전체 저장소 테스트 완료로 인정하지 않는다.
- 기존 운영 workflow는 테스트에 사용하지 않는다. 별도 테스트 workflow 추가/수정은 별도 사용자 승인 대상이다.

### 테스트 fixture 보완 완료 기준
- subprocess mock에서 명령별 returncode 및 `check=True` 예외를 재현한다.
- Git add/commit/push 각각의 실패 경로를 검증한다.
- Discord mock에서 timeout, 네트워크 예외, HTTP 429, 4xx, 5xx를 재현한다.
- 부분 chunk 전송 후 실패와 재실행 정책을 검증한다.
- 테스트가 확인하지 않은 실패 경로는 문서에 미검증으로 남긴다.

### 현재 우선순위 갱신
1. 원본 SHA 일치 실행환경 확보
2. fixture의 실패 시나리오 보강 및 원본 전체 pytest
3. P1-B 코드 변경 범위·테스트·롤백 제안 및 사용자 승인
4. 승인 후 전송/저장/동기화 안정성 개선
5. CRA 출처 검증 메타데이터 및 요구사항 추적 체계 구축


## 2026-11-14 15:31 KST — CI 증거 게이트 갱신

- 작업 브랜치 HEAD `8813eb53b186b25e72ac157d664d636be6d68fd8`의 Actions runs 조회 결과 0건.
- 이는 CI 성공이 아니라 해당 브랜치에 연결된 workflow 실행 기록을 확인하지 못했다는 뜻이다.
- 기존 운영 workflow를 실행해 테스트를 만들지 않는다. 별도 테스트 전용 workflow 신설/수정은 사용자 승인 전 금지한다.
- 다음 선행 작업은 원본 blob SHA 일치 실행환경 확보이며, 실행 불가 시 정확한 장애 원인과 대체 가능한 검증 수준을 문서화한다.

## 2026-11-14 — 테스트 전용 CI 구축 완료

- 별도 `.github/workflows/tests.yml`을 작업 브랜치에 추가했다. 기존 운영 workflow와 분리되어 있으며, 읽기 전용 권한과 mock 테스트만 사용한다.
- GitHub Actions Run #1: [21 passed, success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43567990149)
- 테스트 대상 commit: `d31c604c6067685e33f6888cbc488c0e45d80be7`
- 다섯 개 핵심 소스/테스트 파일의 Git blob SHA가 모두 기대값과 일치한 뒤 compileall 및 pytest를 수행했다.
- 이로써 Phase 3의 **기본 원본 테스트 실행 기반 확보**는 완료로 변경한다. 단, 실패 경로 fixture 보강 및 P1-B 검증까지 완료된 것은 아니다.
- 테스트 가이드의 SHA 고정 기준을 유지하고, 소스 변경 시 승인된 검토와 함께 기준값을 갱신한다.

### 우선순위 재정렬
1. Git/Discord 실패 시나리오의 fixture 보강 설계 및 별도 승인
2. P1-B 전송·저장·동기화 안정성 변경안과 롤백 설계 제시
3. 승인 후 코드 구현 및 CI 회귀 검증
4. CRA 출처 검증 메타데이터와 요구사항 추적 체계 구축


### 최신 HEAD 반복 검증 결과
- 문서 기록 반영 후 최신 작업 브랜치 HEAD `dddba44a41851e9d0319ce9a91535a9d26145d92`에서 테스트 전용 workflow가 다시 실행되었다.
- [Run #3 — success](https://github.com/useformotor3/ai-discord-bot/actions/runs/43568074938), SHA 5개 일치, compileall 통과, pytest **21 passed in 0.19s**.
- 기본 원본 테스트 실행 기반 확보 완료를 유지한다. 실패 경로 보강과 P1-B는 별도 작업/승인이다.
 
## 프로젝트 로그 운영 방식

- 모든 의미 있는 작업 단위는 `PROJECT_LOG.jsonl`(기계 판독)과 `SESSION_LOG.md`(한국어 상세 기록)에 함께 남긴다.
- JSONL은 자동 집계·검색·재개를 위한 최소 사건 데이터이며, 기술 설명과 근거 해석을 대신하지 않는다.
- 새 대화에서 작업을 재개할 때 `AI_RULEBOOK.md`, `README.md`, `PROJECT_STATUS.md`, `MASTER_PLAN.md`, 최근 `SESSION_LOG.md`, `PROJECT_LOG.jsonl`을 먼저 확인한다.
- 운영 자동화 런타임 데이터(`state.json`, `history.json`)와 프로젝트 변경 로그를 혼합하지 않는다.

## 다음 작업 — 실패 경로 검증 설계 완료 후

1. [실패 경로 fixture 설계](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md) §16를 기준으로 테스트 전용 변경 범위를 사용자에게 제안한다.
2. 테스트 fixture/test 추가 승인을 별도로 받은 뒤 작업 브랜치에서 mock만 확장한다. main.py 및 workflow는 변경하지 않는다.
3. 테스트만으로 기존 코드의 실패 동작을 확인하고, 기대 동작과 실제 동작의 차이를 기록한다.
4. 그 결과를 근거로 P1-B 최소 코드 변경안·데이터 일관성 정책·롤백 계획을 제시하고 별도 승인을 받는다.
5. 승인된 P1-B만 구현하고 SHA 고정 CI 게이트를 통과시킨다.


## 실패 경로 fixture 단계 완료 후 우선순위
1. 현재 strict xfail 5건을 근거로 P1-B의 실패 정책과 부분 성공 모델을 확정한다.
2. Discord HTTP 429/5xx/network retry 정책, 4xx 영구 실패, chunk 단위 부분 전송 정책을 명세한다.
3. Git add/commit/push 실패를 실행 성공과 분리하고, state/history atomic write 및 archive ordering의 데이터 일관성 기준을 확정한다.
4. 구현 제안서에 기존 동작/변경 동작, 파일 diff, 승인 범위, 테스트, 롤백 및 운영 영향 분석을 포함해 사용자 승인을 받는다.
5. P1-B 승인 전에는 `main.py`를 변경하지 않는다.


## 2026-11-14 — 실패 주입 fixture 2차 확장
- 기존 승인 범위(테스트 fixture/test만) 안에서 Discord transport exception, 401/403, Git add/commit/push 단계별 실패 주입을 추가한다.
- 각 테스트는 mock 경계의 주입/관찰 능력만 검증한다. 실제 운영 코드의 재시도·상태화·부분 성공 정책은 증명하지 않는다.
- 새 CI에서 원본 blob SHA 일치, compileall, 전체 pytest 결과를 확인한 후에만 이 테스트 묶음을 완료 처리한다.
- 다음 P1-B 단계는 정책 명세 및 구현 제안서 작성이다. 운영 코드 변경은 사용자 별도 승인 전 금지한다.


## 2026-11-14 — 실패 주입 fixture 2차 확장 검증 완료
- Discord transport exception 2 case, HTTP 401/403 2 case, Git add/commit/push 단계별 실패 3 case를 추가했다.
- [Run #13](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570175208), 검증 commit `27d2c69287631b041672b9989fdeeb3066f5ebb9`: 6개 SHA 일치, compileall 통과, **30 passed / 5 xfailed**.
- Run #12의 SHA pin 누락 실패를 기록하고 Run #13에서 정정 완료했다.
- 다음 우선순위는 P1-B 동작 정책 명세(Discord retry/영구 실패/부분 chunk, Git 단계 상태, archive·state/history atomic write 및 복구)다. 운영 코드 변경은 별도 승인 전 금지한다.


## 2026-11-14 — P1-B 설계 정책 정밀화
- [정책 명세 §17](reports/MAIN_PY_IMPROVEMENT_DESIGN_2026-11-14.md#17-p1-b-전송저장동기화-정책-명세--2026-11-14-구현-전-설계)를 P1-B 구현 전 기준으로 사용한다.
- Discord POST는 중복 가능성을 고려해 delivery unknown과 재시도 가능 상태를 구분한다. 429는 Retry-After/retry_after 준수, 400/401/403/404는 영구 실패로 중단한다.
- state/history의 다중 파일 일관성에는 transaction journal/recovery 검증이 필요하다.
- 다음 단계는 구현 전 변경 제안 및 승인이다. 운영 코드 변경은 별도 승인 전 금지한다.


## 2026-11-14 — Discord 실패 테스트 정책 정합화
- 503 응답의 무조건 재시도 기대를 제거하고 delivery_unknown으로 남기는 duplicate-safe 계약으로 수정했다.
- 401/403/404 영구 실패 및 자동 재시도 금지 xfail 3 case를 추가했다.
- [Run #15](https://github.com/useformotor3/ai-discord-bot/actions/runs/43570492842): 30 passed / 8 xfailed.
- 다음 단계는 P1-B 최소 구현안과 복구/중복 방지 설계를 승인 요청하는 것이다. 운영 코드 변경은 별도 승인 전 금지한다.


## 과거 승인 게이트 기록 — P1-B1 (이후 승인·구현 완료)
- P1-B 전체를 한 번에 구현하지 않고 B1 Discord 전송, B2 로컬 저장, B3 Git sync, B4 구조 개선으로 나눈다.
- 다음 승인 요청은 B1만으로 제한한다. 설계서 §18의 변경 파일·테스트·롤백·제외 범위를 따른다.
- 승인 전에는 main.py 및 운영 관련 코드를 수정하지 않는다.


## 2026-11-16 — P1-B1 Discord 전송 구현 및 CI 확인
- P1-B1을 구현하고 테스트 전용 Actions Run #18에서 43 passed / 1 xfailed를 확인했다.
- 1 xfailed는 P1-B3 Git sync 상태화 미구현 기대 동작이다.
- Run #17 SHA pin 오류는 기록 후 수정했다. Run #18에서 source SHA, compileall, 전체 pytest 통과를 확인했다.
- 당시 다음 우선순위는 P1-B2 설계였다. P1-B2는 이후 별도 승인으로 구현·검증 완료했다.


## 이전 통합 게이트 스냅샷 — 2026-11-16 (이후 merge-base 재감사로 갱신)
1. [완료] main/작업 브랜치 ref, merge-base, ahead/behind 재조회.
2. [완료] merge-base와 main의 recursive Git tree 비교(양쪽 API truncated=false).
3. [완료] 운영 state/history/archive 및 main.py/workflow 원문·SHA 교차확인.
4. [진행 전 보류] 데이터 보존을 전제로 한 코드/문서 통합 후보 분리와 migration 설계.
5. [승인 대기] main 반영, 데이터 변경, workflow 실행, P1-B2/B3/B4 구현.

통합은 단순 branch merge가 아니라 운영 데이터와 자동 생성 보고서 보존을 포함한 별도 change-control 작업으로 취급한다. 현재 main 대비 152 ahead / 657 behind이며 통합을 진행하지 않는다.


## 2026-11-16 최신 통합 감사 스냅샷
- main HEAD `31e0f8137630630ee30ea55add039b571f2c6801`, 작업 브랜치 HEAD `c43abc3315d8d7c8a3d5f4fc209465428a7e8aff`.
- 작업 브랜치 153 ahead / 658 behind main. main 고유 archive 658개, history 2,250개, state count 111.
- 데이터 보존 및 별도 통합 설계 전까지 merge/rebase/PR merge 금지.


## 다음 실행 단계 — P1-B2 구현/검증 완료
- [완료] P1-B2 원자적 저장 설계·구현: `reports/P1_B2_ATOMIC_PERSISTENCE_DESIGN_2026-11-16.md`.
- [완료] crash/failure injection tests 및 테스트 전용 CI Run #23: 63 passed / 1 xfailed.
- [완료] 정확한 source blob SHA, compileall, 전체 pytest 확인.
- [완료] P1-B2 diff/운영 위험 검토 및 merge-base 기반 통합 전략 보고서 작성.
- [다음] PR 사전 검사, PR CI 및 conflict check. PR 생성/merge/운영 rollout은 별도 승인 대상.
- [보류/별도 승인] P1-B3 Git sync status, P1-B4 import-time execution cleanup.
- 운영 main/data/workflow 변경과 merge/rebase/PR merge는 별도 승인 전 금지.


## 2026-11-16 운영 모니터링 설정
- ChatGPT 예약 작업 `매일 Git 브랜치 통합 상태 점검` 생성 완료. ID `6afacb7561d8819182728a42ffd4e867`, 매일 09:00 Asia/Seoul, 첫 실행 2026-11-17 09:00.
- refs/ahead-behind/recursive tree/state-history-archive 변경을 재조회한다. 안전할 때만 작업 브랜치의 상황판·로그 문서를 갱신한다.
- 운영 main/data/workflow 수정, merge/rebase/PR merge, 실제 Gemini/Discord 호출은 금지한다.
- 이 예약 작업은 ChatGPT의 모니터링이며 GitHub Actions 운영 workflow와 별개다.


## 최신 작업 브랜치 및 통합 기준 — 2026-11-16
- 작업 브랜치: `feature/p1-b2-atomic-persistence-2026-11-16`; 감사 스냅샷 HEAD `0fe9912b5dbba29eeb3ebd9e9f2c16a42544f925`.
- 운영 main HEAD `267d97478b785e6bb268e224a70dbad6631cf43e` (#131); merge-base `f9a12a5778f5fa1d907201ab2931d20ca2656bb7`.
- compare: 221 ahead / 678 behind. 이는 commit count이며 파일 삭제를 뜻하지 않는다.
- merge-base 기준 main은 archive 678개 추가·삭제 0·history/state 2개 수정; 작업 브랜치는 23개 경로 추가·삭제 0·main.py 1개 수정이다.
- 운영 데이터 보존을 위한 3-way PR 통합 후보가 양호하나, 실제 PR conflict check 및 별도 승인 전 merge 금지.


## 2026-11-16 — P1-B2 구현 완료
- 전용 브랜치 `feature/p1-b2-atomic-persistence-2026-11-16`에서 durable journal 기반 multi-file persistence를 구현했다.
- recovery는 state/history 읽기와 외부 서비스 호출보다 먼저 수행한다. commit 시 읽은 원본 snapshot SHA를 확인해 동시 변경을 fail-closed 한다.
- 장애 주입 및 통합 테스트 포함 Run #23에서 63 passed / 1 xfailed.
- POSIX flock/fsync 기반이므로 Ubuntu 등 POSIX 실행 환경을 전제로 한다. Windows lock backend는 미구현.
- P1-B3/B4, 운영 데이터, 운영 workflow, merge/rebase는 이번 승인 범위 밖이다.


## 2026-11-16 — 통합 전략 감사 완료
- merge-base 기준 전체 recursive tree 비교와 history→archive 참조 무결성 확인을 완료했다.
- main의 678개 archive는 merge-base 이후 추가된 자료이며 작업 브랜치가 삭제한 파일이 아니다. main history/state는 main에서만 변경됐고 작업 브랜치는 merge-base blob을 유지한다.
- 작업 브랜치의 코드·테스트·관리 문서 변경은 main의 운영 데이터 변경과 경로상 분리되어 3-way PR 통합 후보로 평가한다.
- P1-B2 recovery target allowlist 보강 후 Actions 43851438733: 70 passed / 1 xfailed.
- PR CI 트리거를 pull_request→main 및 main push로 준비했다.
- 실제 PR 생성, merge, rebase, 운영 workflow/data 변경은 수행하지 않았다. 통합 및 운영 배포는 별도 승인 후 진행한다.
- 상세: `reports/BRANCH_INTEGRATION_STRATEGY_2026-11-16.md`.


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


## 2026-11-16 — 복구 우선 통합/운영 단계 추가
1. 체크포인트 고정: main/feature 백업 브랜치 SHA를 원격 재조회해 검증한다.
2. 최신 base 통합 검증: main 자동 아카이브가 진행된 상태에서 PR base/head SHA, merge-base, 전체 diff 및 PR mergeability를 다시 확인한다. 최신 base에 대한 CI 결과가 없으면 merge하지 않는다.
3. 운영 데이터 복구체계: state/history/archive snapshot, checksum, file count, history 참조 무결성 검증 및 별도 복원 리허설을 구축한다.
4. 통합: 안전 게이트 통과 시 merge commit으로 통합하고, main HEAD와 PR merge SHA를 기록한다.
5. 첫 실행 검증: 운영 데이터 백업 후 단일 실행, state/history/archive 변화량 및 참조 무결성을 확인한다. 이상 시 재실행을 막고 코드 revert/데이터 복구를 수행한다.
6. 지속 운영: 매 세션 시작 시 이전 정상 commit/백업 ref/최근 CI를 확인하고, 변경 단위별 테스트 및 복구 가능성을 검증한다.

완료 기준은 단순히 Git commit이 존재하는 것이 아니라, 코드와 운영 데이터 각각에 대해 정상 기준점으로 되돌리는 절차가 실제로 검증된 상태다.

## 2026-11-16 — 운영 데이터 baseline 및 rollback
- main HEAD를 immutable SHA로 고정한 뒤 state/history/archive를 같은 SHA에서 검사한다.
- Git safety branch는 tracked 운영 데이터 기준 snapshot으로 유지한다.
- 첫 운영 실행 전 per-run snapshot branch 생성과 실패 시 restore commit 경로를 mock으로 구현·리허설한다.
- U+200B legacy state 파일은 참조/생성 경위를 확인할 때까지 보존한다.
- 코드 rollback과 데이터 rollback을 분리하고, 외부 Discord 전송은 회수 불가 경계로 유지한다.

## 2026-11-16 — 운영 rollback guard 계획
- 운영 workflow 실행 전 baseline branch를 생성하고 실행 후 append-only 및 참조 무결성을 검증한다.
- 복구는 remote main이 실행의 단일 child commit일 때만 data-only restore commit으로 수행하며 force-push하지 않는다.
- local bare Git remote integration tests 및 최신 base PR CI 성공 후 통합한다.
- 첫 실제 운영 실행 결과를 별도 관찰하고 외부 Discord 메시지는 회수 불가 경계로 관리한다.


## 2026-11-16 — latest rollback guard verification
- Run #43875746973: 87 passed, 1 xfailed; compileall and source blob identity checks passed.
- Tested normal one-report append, archive/history mismatch, deleted archive, invalid state count, date rollover, unsafe archive paths, local bare remote data restore, no-push fail-closed, quota no-op, missing state restore, symlink/empty archive detection.
- main #162 baseline state=162, history=2,301, archive=2,301, missing refs=0. safety/pre-merge-main-adf74ea exact SHA.
- First production execution is not yet performed; Gemini/Discord calls not made in CI.

## 2026-11-16 — 통합 단계 완료 및 다음 운영 단계
- Phase 2 신뢰성 개선 및 Phase 3 테스트 기반/운영 data guard를 main에 통합 완료.
- PR #1 merge commit 방식, post-merge CI 통과.
- 다음은 production workflow 첫 실행 관찰이다. 실행 전 snapshot branch 생성, 실행 후 operational_guard 결과, state/history/archive 무결성을 확인한다.
- 실제 운영 실행 결과를 법적 CRA 근거 검증과 혼동하지 않는다.


## 2026-11-17 — 자동화 운영 안정화 후속 작업
1. checkpoint pruning 테스트 기대값을 수정하고 main CI 성공을 확인한다.
2. 다음 production run은 정상 종료 및 guard 통과 여부를 확인한다. 실제 pruning이 30개 기준으로 작동했는지 원격 ref 수를 재조회한다.
3. #2412의 Discord 전송/미저장 보고서 #235를 중복 없이 처리할 방법을 검토한다. 보고서 본문이 원격에 없으므로 추측해 복원하지 않는다.
4. Gemini 모델 설정의 404 fallback 원인을 공식 모델 목록 및 SDK API 지원 기준으로 확인한다.
5. Git push 실패 시 운영 workflow가 성공처럼 끝나지 않도록 하고, main 변경과 운영 데이터 쓰기의 동시성 정책을 별도 설계·테스트한다.
6. main 변경 전 활성 production workflow가 없는지 확인한다. 작업 중 운영 workflow가 시작되면 main 변경을 중단한다.


## 2026-11-17 운영 신뢰성 후속 우선순위
1. KST 날짜 경계 및 기존 UTC naive health-check timestamp 호환성 테스트를 통과시킨다.
2. Gemini API 404/NOT_FOUND 즉시 fallback 및 공식 모델 ID 사용을 테스트한다.
3. Git push 실패가 workflow 실패로 전파되는지 mock으로 검증한다. 실제 Discord/Gemini는 호출하지 않는다.
4. CI 통과 후 다음 운영 실행에서 state date가 KST 기준인지, history/archive가 한 건씩 append되는지 확인한다.
5. Git push race가 발생하면 강제 push하지 않고 fail-closed한다. Discord delivery와 Git archive가 분리되므로 중복 방지/outbox 설계는 별도 과제로 둔다.


## 2026-11-17 — KST/model/Git fail-closed 구현 검증
- [완료] Asia/Seoul 기준 날짜·시간 및 legacy naive UTC health-check 호환.
- [완료] gemini-3.8-flash → gemini-3.5-flash-lite, 404/NOT_FOUND 즉시 fallback.
- [완료] Git 저장 실패 시 비정상 종료, 강제 push 금지.
- [완료] CI Run #59: 99 passed, 1 xfailed.
- [대기] 다음 운영 실행에서 KST 날짜·일일 count, 실제 Gemini 모델 ID 성공, Git push와 operational_guard의 정상 완료 확인.
- [대기] Discord 전송 이후 Git 저장 실패 시 재전송 중복 방지/outbox 설계.
## 2026-11-17 — 반복 자동화 및 조사 품질 개선

1. [완료] main의 최근 #33–#38을 EUR-Lex OJ 원문과 대조하고 원본 보존 정정 보고서 6건 추가.
2. [완료] PR #10을 main에 merge. EUR-Lex CRA 공식 링크 누락 거부, 최근 30개 원문 기반 중복 주제 차단, 프롬프트 최근 15개 이력 확대.
3. [완료] PR #10 CI Run #455: 101 passed, 1 xfailed.
4. [진행] 외부 5분 repository_dispatch를 제거하고 hourly schedule로 전환하는 PR 검증 및 병합.
5. [후속] 첫 3회 hourly production run의 checkpoint/guard/prune 및 archive 참조 무결성을 관찰.
6. [후속] 중복탐지 false positive/negative를 로그로 검토하고 임계값을 근거 기반 조정.
7. [핵심 산출물] CRA 통합 한국어 보고서 및 CRA 요구사항 추적표를 작성·검증한다. SIL 3 기능안전 자료는 과거 산출물로 보존하며 본 프로젝트의 후속 작업으로 진행하지 않는다.

## 2026-11-17 — Gemini 무료 할당량 장애 반영
1. [완료] Production Run `44016487535` 로그에서 Gemini 429 daily quota 20/day와 fallback 503 UNAVAILABLE를 확인.
2. [완료] 같은 모델의 429/503 반복 호출을 즉시 중단하고 대체 모델로 전환.
3. [완료] quota/일시 장애/품질 검증 실패 시 외부 전송·아카이브·상태 변경 없이 no-op 종료. 인증/설정 오류는 실패 유지.
4. [완료] Free Tier 일일 한도와 재시도 여유를 고려해 운영 schedule을 3시간마다(8회/일)로 조정; 모델당 최대 2회 시도 기준 최대 16회/일.
5. [진행] PR #11 isolated CI 재검증 및 병합, 이후 첫 3회 production run 관찰.
## 2026-11-17 — 운영 안정화 PR #10–#12 병합 완료

1. [완료] PR #10: EUR-Lex official-link gate + recent-30 archive duplicate-topic suppression. CI #455: 101 passed, 1 xfailed.
2. [완료] PR #11: 외부 5분 repository_dispatch 제거, 3시간 schedule, Gemini 429/503 즉시 fallback, quota/quality clean no-op. CI #467: 103 passed, 1 xfailed.
3. [완료] PR #12: 실패 후 guard always, dirty/unpublished data restore, guard 성공 후에만 checkpoint pruning, persist-before-Discord. CI #470: 105 passed, 1 xfailed.
4. [진행] 첫 3회 3-hourly production run을 관찰하고 actual quota/Discord/guard/prune 결과 확인.
5. [다음] CRA 한국어 통합 보고서와 requirements traceability matrix 작성. 법령 직접 의무와 제조사 권고 구현을 구분.
6. [다음] CRA 통합 한국어 보고서와 CRA cybersecurity 요구사항 추적표 작성·검증. 기능안전(SIL 3)은 별도 재개 지시 전 비활성.

## 2026-11-17 — CRA 자동 보관 #1–#38 원문 정정
1. [완료] CRA 정정 보고서 #1–#4 및 #33–#38 main의 기존 정정 확인.
2. [완료] #5–#21 정정 보고서를 이전 source-audit branch에서 main 통합 후보로 복사.
3. [완료] #22–#32 원본을 EUR-Lex final OJ와 대조해 11개 정정 보고서 작성.
4. [완료] #1–#38 인덱스 생성.
5. [진행] PR #14 CI 및 병합 후 정정 보고서/원본 archive SHA 무결성 확인.
6. [다음] 정정된 근거를 CRA 한국어 통합 보고서 및 requirements traceability matrix에 반영.

## 2026-11-17 — CRA correction coverage 완료
1. [완료] 자동 생성 CRA archive #1–#38 각각에 correction report #1–#38을 main에 통합.
2. [완료] master index `reports/CRA_CORRECTION_INDEX_2026-11-17.md` 작성.
3. [완료] 원본 archive SHA 보존, state/history SHA 동일성 검증.
4. [완료] PR #14 merge; CI #474 105 passed, 1 xfailed.
5. [진행] CRA 한국어 통합 보고서와 조항-제품요구-검증증거 traceability matrix 작성.
6. [다음] CRA 통합 보고서 및 CRA 요구사항 추적표를 완성하고 각 주장·조항·제품 적용성·통제·시험 증거를 교차 검증한다. SIL 3는 활성 범위에서 제외.
7. [운영] 첫 3회 3-hourly production run을 관찰하고 실제 quota/Discord/guard/prune 결과를 기록.

## 과거 산출물 기록 — SIL 3 기능안전 (비활성 범위)

아래 날짜별 기록은 과거 작업 이력 보존용이다. 활성 CRA 계획의 단계·우선순위·재개 지점으로 해석하지 않는다.

## 2026-11-17 — SIL 3 서보 드라이브 기술 산출물 v0.1
1. [완료] 제조사 4개 제품군(Mitsubishi J5, Yaskawa Sigma-7 ASM7, Rockwell Kinetix 5700, Siemens S210) 공식 자료 기반 벤치마킹.
2. [완료] 2026-11-17 현재 IEC 61800-5-2 AMD1:2026 및 IEC 62061 AMD2:2026 최신판 반영.
3. [완료] 1축 기준 하드웨어 reference block design 및 안전 기능별 구현 경로 작성.
4. [완료] FS/CYB 분리 traceability matrix 작성.
5. [진행] PR CI/병합 및 링크/수치/모델 조합 검증.
6. [다음] 정격 전압·출력·축 수·부하·엔코더·안전 기능 범위를 확정한 후 회로도/BOM/PFH 계산/시험 규격 상세화.

## 2026-11-17 — SIL 3 서보 드라이브 기술 산출물 main 반영
1. [완료] 4개 제조사 벤치마킹 보고서 v0.1.
2. [완료] 1축 하드웨어 reference block design v0.1.
3. [완료] FS/CYB 분리 요구사항 추적성 매트릭스.
4. [완료] Excel/Google Sheets에서 열 수 있는 CSV 비교표.
5. [완료] PR #16 merge `34449753857c6ab004271f69aac19867a7aed1fa`, CI #488 105 passed, 1 xfailed.
6. [진행] 정격/부하/피드백/안전 기능 범위 확정 후 schematic, component selection/BOM, thermal/EMC, FMEDA/PFH calculation.
7. [운영] 3시간 주기 첫 3회 production run 관찰.


## 2026-11-17 — CRA source provenance pipeline 완료

- PR #26 merge commit `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`.
- CELLAR official source 7건, Commission official page 2건을 allowlist 기반으로 수집하고, 전체 visible text/prompt excerpt SHA-256과 retrieval metadata를 manifest에 남긴다.
- Claim ID, 본문 statement, source ID, exact quote, Article paragraph/Annex Part-point locator 검증을 추가했다.
- Run #573: 138 passed / 1 xfailed, 9개 live source fetch, Article 13(8) locator/quote canary 성공.
- 상세: [CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md](reports/CRA_SOURCE_PROVENANCE_PIPELINE_2026-11-17.md).
- 제한: Guidance PDF/Annex와 M/606 decision Annex 미수집; 제품별 적용성/설계/시험 증거 미확정; merge commit 자체의 별도 CI는 미확인.


## 2026-11-17 — CRA source provenance 관리 문서 동기화 완료

- PR #27 merge commit: `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`.
- README, PROJECT_STATUS, MASTER_PLAN, AI_RULEBOOK, SESSION_LOG, PROJECT_LOG.jsonl 및 source provenance 상세 보고서를 PR #26 검증 결과에 맞춰 동기화했다.
- PR #27 Run #575: 138 passed / 1 xfailed, 9개 live official source 및 Article 13(8) locator/quote canary 재통과.
- PR #27 pre/post merge safety refs는 각각 `safety/pre-merge-main-pr27-2026-11-17` 및 `safety/post-merge-main-pr27-2026-11-17`; 두 ref의 SHA readback 검증 완료.
- merge commit 자체의 별도 Actions run은 확인되지 않았으므로 PR head CI 결과만 기록한다.


## 2026-11-17 — PR #28 main recovery checkpoint synchronization

- PR #28 merge commit: `942e1e6b5f2887001279a96c21f94138d283a689`.
- Run #577: 138 passed / 1 xfailed; 9 official sources and live Article 13(8) locator/quote canary passed on PR head.
- Pre/post merge safety refs: `safety/pre-merge-main-pr28-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; `safety/post-merge-main-pr28-2026-11-17` → `942e1e6b5f2887001279a96c21f94138d283a689`; both verified by readback.
- Merge commit-specific Actions run was not confirmed; only PR head CI is claimed.


## 2026-11-17 최신 재개 지점 — 공식 Guidance/M/606 Annex 1차 감사

- 현재 작업 브랜치 `cra/official-annex-audit-2026-11-17`는 `main` @ `80245d9e132380a10581612c031f87869993b98d`에서 생성했으며, 생성 직전 compare 결과 main과 동일(0 ahead/0 behind)이었다.
- [CRA 공식 Guidance 및 M/606 Annex 감사 보고서](reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md)를 추가했다. Commission Guidance C(2026) 5252의 주요 조항·페이지 locator와 C(2026) 7861 Annex I의 41개 표준 주제/ESO adoption deadline을 추출했다.
- Guidance는 비구속적 Commission 해석이다. 법령 정본과 구분하고, 제품별 판단은 실제 모델·회로·통신·공급 구조를 기준으로 한다.
- M/606 Annex의 ESO adoption deadline은 harmonised standard OJ citation 또는 CRA 제품 적용일과 동일하지 않다. 항목 18 날짜는 PDF text extraction에서 판독 불가로 미확인 처리한다.
- M/606 Commission Annex 및 Guidance ANFR mirror PDF raw SHA-256 검증 완료. Commission-hosted Guidance primary byte identity는 미확인으로 구분한다.

### 다음 작업 순서 업데이트
1. M/606 Annex 원본 PDF 이미지에서 항목 18 날짜와 병합 셀을 시각 확인하고, C(2026) 7861 본문 결정문 및 register 첨부 전체를 확인한다.
2. C(2026) 5252 PDF 원본 바이너리 취득 경로를 확보해 파일 크기, 페이지 수, SHA-256을 기록한다. ANFR mirror는 Commission 원본과 byte identity가 확인되기 전 보조 취득 경로로 표시한다.
3. Guidance §2.5 paras. 26–28을 15개 interface matrix에 반영하고, analog/discrete/STO와 encoded data exchange의 판정 규칙을 구체화한다.
4. Guidance §6 core functionality와 §8 RDPS 기준을 35 requirements/36 SEC controls 및 통합 보고서에 claim-level로 연결한다.
5. Annex I의 41개 표준 주제를 SEC control/설계/시험 후보에 매핑하되 ESO adoption deadline, harmonised status, presumption of conformity, CRA application date를 별도 필드로 관리한다.
6. Article/Annex live locator canary를 Annex I Part I/II 및 핵심 Article로 확대하고 mock regression + CI를 검증한다.


## 2026-11-17 — PR #30 병합 완료 및 다음 단계

- 공식 Guidance/M/606 Annex 감사 보고서 `reports/CRA_OFFICIAL_GUIDANCE_AND_M606_ANNEX_AUDIT_2026-11-17.md`가 PR #30으로 main에 병합됐다.
- Merge commit `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd`; [Run #610](https://github.com/useformotor3/ai-discord-bot/actions/runs/44050954456) success: 141 passed / 1 xfailed, compileall/source identity/live official source canary 통과.
- Pre/post safety refs `safety/pre-merge-main-pr30-2026-11-17` / `safety/post-merge-main-pr30-2026-11-17`를 생성했고, post-merge ref와 main이 동일함을 비교 확인했다.
- 다음 우선순위는 (1) M/606 item 18 원본 표 이미지 확인 및 C(2026)7861 문서등록부 전체 확인, (2) PDF 원본 bytes와 SHA-256 취득, (3) Guidance §2.5/§6/§8을 interface/requirements/SEC matrix에 claim-level 연결, (4) Annex I live locator canary 확대다.
- CI 성공은 PR head 기준이다. merge commit 자체의 별도 Actions run은 확인되기 전까지 미확인으로 표시한다.


- PR #30 병합 후 구현 작업 브랜치는 없는 상태로 정리한다. PR #31은 README/PROJECT_STATUS/SESSION_LOG 및 기록의 사후 동기화만 수행하며, 다음 기능·자료 구현은 PR #31 병합 후 최신 main에서 새 작업 브랜치로 시작한다.


## 2026-11-17 — Guidance claim mapping 및 PDF binary provenance

- G-001~G-013을 비구속적 Commission explanation으로 등록하고, 15 interface / 35 requirements / 36 SEC control matrix에 연결한다.
- `cra_pdf_sources.py`는 Commission PDF bytes를 fetch하고 redirect allowlist, PDF magic, document markers, page count, raw-byte SHA-256 및 text SHA-256을 검증한다. Commission Guidance primary fetch가 unavailable/non-PDF일 때만 ANFR mirror fallback을 허용하며 final URL과 fallback status를 기록한다.
- `tests/test_cra_pdf_sources.py`는 mirror fallback, redirect 차단, 임시 HTTP 오류, identity marker, artifact output을 mock으로 검증한다.
- 테스트 전용 workflow에서 pypdf 설치, source blob pins, live PDF canary, artifact upload를 실행한다. 일시적 네트워크 장애는 SKIPPED로 표시하고, redirect/identity/파싱 검증 실패는 CI fail-closed한다.
- 실제 PDF bytes, SHA-256, page count, M/606 item 18 날짜는 CI artifact를 readback하고 시각 검증한 후에만 확정한다.


## 2026-11-17 — PDF 원문 취득 검증 결과

- M/606 C(2026)7861 Annex Commission PDF: 151,267 bytes / 6 pages / SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276` verified.
- C(2026)5252 Guidance: ANFR mirror fallback bytes 1,190,726 / 84 pages / SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234` verified. Commission-hosted primary byte identity remains unverified.
- CI artifact #14313359693 downloaded; ZIP digest `150a687e4d4b13fdd20a432e99fc8ea9ec5bc847b8551dd3f157258dc41cd869` re-computed and matches GitHub metadata.
- M/606 item 18 deadline visually confirmed from original PDF page image: `31/01/2027`.
- Run #642's PDF source step and artifact upload passed; a separate existing HTML publication-page canary failed on an over-strict document-number marker. The marker is corrected to validate visible publication-page metadata separately from the PDF Annex identity; rerun required.


## Run #669 — source marker correction 검증 완료

- Commission guidance summary page와 PDF Annex 식별자 검증을 분리했다. Summary page는 실제 visible publication metadata만 확인하고, C(2026)5252 Annex의 document identity는 PDF binary canary가 확인한다.
- Run #669: 148 passed / 1 xfailed; compileall, blob pins, 2 PDF sources/raw hashes/artifact upload, 9 official HTML sources, consolidated corrigenda, Article 13(8) live locator/quote 모두 통과.
- PDF artifact #14315096266을 다운로드해 ZIP digest 및 PDF별 raw-byte hashes를 재계산하고 manifest와 일치시켰다.
- 남은 원문 취득 한계는 Guidance Commission-hosted original bytes와 ANFR mirror의 byte identity뿐이다.


- 최종 branch-head Run #690 성공(148 passed / 1 xfailed). PDF/HTML live canary, artifact download/readback 및 SHA-256 재검증을 포함한 최신 branch 상태 검증 완료. PR #33 병합 전 diff와 복구 체크포인트만 남음.


## CRA 추적성 무결성 자동화 — 2026-11-17

- `cra_traceability.py`를 CI gate로 추가해 Guidance claim register(13), interface matrix(15), CRA requirements(35), SEC controls(36)의 row count, unique ID, cross-reference integrity를 검증한다.
- M/606 Annex I item refs 1–41, non-binding Guidance category, source PDF raw/text hashes, artifact readback, item18 visual verification, README/report links 및 JSONL project log integrity를 검사한다.
- negative tests는 unknown Guidance claim ID 및 invalid M/606 item 42를 fail-closed로 확인한다.
- 이 검증은 법적 적합성을 판정하지 않는다. 문서·추적성 데이터의 내부 일관성만 검증한다.


## M/606 Annex I 41-item product relevance crosswalk — 2026-11-17

- 41개 표준화 항목을 모두 CSV로 정리하고 horizontal property (1–14), horizontal vulnerability handling (15), vertical product type (16–27, 31–36, 40), security component (28–30, 37–39, 41)로 구분한다.
- 각 항목에 ESO adoption deadline, printed page locator, servo-drive relevance class, candidate CRA requirements/SEC controls/interface IDs를 연결한다.
- Vertical product type은 intended purpose/product boundary/core functionality로 판단한다. component inclusion alone does not classify the complete servo drive.
- M/606 adoption deadlines are ESO deadlines, not manufacturer compliance dates; no harmonised status/presumption until OJ citation.
- Extend `cra_traceability.py` and CI to validate exactly 41 unique items, deadlines and all candidate foreign keys.


## 제품별 증거 수집 단계 — 2026-11-17

- 한국어 제품 경계 및 증거 수집 기준서를 추가했다.
- 제품별 모델·의도된 목적·제품 경계·인터페이스·원격 데이터 처리·보안 기능·BOM/SBOM·취약점/지원 정책 증거가 확보되기 전에는 CRA 제품 분류·Annex III/IV·RDPS 여부·적합성을 단정하지 않는다.
- 첫 입력 자료는 정확한 모델의 데이터시트와 사용설명서다. 그 후 architecture, network interface list, SBOM, security/vulnerability policy 순으로 증거를 확보한다.


## 통합 CRA 보고서 독립 검토 — 2026-11-17

- 보고서 번호 중복·제품 분류 용어 오류를 정정하고 독립 검토 기록을 추가한다.
- 법령 Article/Annex locator를 원문과 대조하고, Guidance claim PDF locator를 표본 검증한다.
- traceability gate에서 보고서 top-level section 번호 중복을 fail-closed로 검사한다.
- 제품별 모델 자료가 없으면 적용성·Annex III/IV·RDPS·적합성 결론은 Unknown/Conditional로 유지한다.


## CRA 요구사항 법령 locator 전수 대조 — 2026-11-17

- CRA-001~CRA-035의 Article/Annex paragraph locator를 공식 EUR-Lex 법령 원문과 행 단위로 대조한다.
- Article number만 맞는지 확인하지 않고 실제 법적 의무·적용 주체·조건·기한·예외가 매트릭스 설명과 일치하는지 확인한다.
- 발견된 오류는 requirement CSV, 통합 보고서, 관련 SEC control 및 audit log를 함께 수정한다.
- 근거가 불명확하면 '미확인'으로 유지하고 적합성 결론으로 확대하지 않는다.


## 최신 실행 순서 — 2026-11-18

1. CRA-001–CRA-035 각 행을 EUR-Lex 원문과 대조해 법적 의무 주체, 행위, 조건, 예외, 기한, 보존기간 및 제품 사실 전제를 확인한다.
2. 검토 결과를 요구사항 CSV, 한국어 통합 보고서, SEC 통제/시험 매트릭스 및 독립 감사 기록에 한 번에 반영한다.
3. 법령 의무, Commission Guidance 해석, M/606 표준화 요청/ESO 일정, 엔지니어링 권고를 분리한다.
4. Commission Guidance PDF primary byte identity 취득을 계속 시도하되 ANFR fallback은 fallback으로 표시한다.
5. 제품별 자료가 없으면 제품 분류·적합성·인증 경로는 Unknown/Conditional로 유지한다.

최신 재개 기준 및 PR #42 검증/복구 정보는 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)를 참조한다.


## 법령 심층 감사 진행 상태 — 2026-11-18
- CRA-001–CRA-010: EUR-Lex 원문 대조 1차 완료. locator 보완/정정 사항은 요구사항 CSV 및 통합 보고서/독립 감사에 반영 중.
- CRA-011–CRA-020: 다음 검토 묶음.
- CRA-021–CRA-035: 신고/전환, 기계류·표준화, 경제운영자, 적용 제외/중복 검토 대기.
- 상세 Batch 1: `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`.


## 법령 심층 감사 업데이트 — 2026-11-18
- CRA-001–CRA-020: EUR-Lex 원문 기준 1차 심층 대조 완료. 세부 보완은 Batch 1/2 감사 파일 및 추적표에 반영.
- 다음 묶음 CRA-021–CRA-035: 신고·자발신고, 적용일/전환, 기계류 규정 상호작용, 표준화/추정 적합성, 경제운영자, 적용 제외·중복.


## CRA 법령 심층 감사 — 35행 1차 대조 완료 (2026-11-18)
- CRA-001–CRA-035: EUR-Lex 공식 원문 및 관련 sectoral act 기준 1차 심층 문언 대조 완료.
- 후속 우선순위: 35행 전체 cross-matrix audit, 법령 locator/의무주체/조건/예외/기한의 중복·누락 확인, Guidance/M/606/engineering control 구분, 제품별 evidence intake 설계.
- 상세 Batch 1/2/3 감사 파일은 `reports/CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md`, `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md`, `reports/CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md` 참조.


## 다음 단계 업데이트 — 2026-11-18
- CRA-001–CRA-035 법령 문언 1차 대조 및 15/36/13/41 cross-matrix 정합성 감사 진행.
- 다음: 통합 보고서 독립 재검토(법령 locator·주장·표/그림·제품별 unknown 분리), 제품 evidence intake 필수 항목 확정, Guidance PDF primary byte identity 검증.


## 제품별 적용성 검증 단계 — 2026-11-18
- 35행 법령 문언 및 전체 cross-matrix 1차 검토 완료.
- 제품 증거 수집 기준서를 최신 법령 해석에 맞게 보완한다. 우선 P0: 정확한 모델 데이터시트/카탈로그 및 사용설명서; P1: 제품/통신 block diagram, 인터페이스 사양, SW/FW 구성표/SBOM, EU 공급망/출시 정보; P2: 보안 정책/지원기간 및 Machinery/기타 인증 자료.
- 증거가 없으면 Unknown 유지. 일반 인터페이스 예시를 실제 제품에 있다고 추정하지 않는다.


## 2026-11-18 재개 순서 갱신 — 통합 보고서 독립 감사
1. 통합 보고서의 제품 적용 가능성 및 Annex III/IV 표현을 제품별 판정과 분리하고, evidence gate 미충족 시 Unknown을 유지한다.
2. EUR-Lex OJ 원문 기준 Articles 7/8/13/14/15/69/71 및 Annex 핵심 항목을 표본 대조한 독립 감사 기록을 보존한다.
3. 보고서·요구사항 CSV·SEC/IF/Guidance/M/606 매트릭스 및 상황판 간 상태와 근거 링크를 동기화한다.
4. Commission Guidance C(2026) 5252 Commission-primary byte identity를 별도 검증하고, mirror fallback을 원본 검증으로 표현하지 않는다.
5. PR exact-head isolated CI와 readback, pre/post safety refs, main compare를 통과한 문서 변경만 병합한다.
6. P0 제조사/정확한 모델 데이터시트·카탈로그 및 사용설명서가 확보되면 모델별 evidence IDs를 CRA-001–035 및 IF/SEC 매트릭스에 연결한다.


## PR #50 병합 완료 및 다음 재개 순서 — 2026-11-18
- PR #50 `137d096123ccf5ee478292002d2c528b41981fc7` 병합 완료. Exact-head Run #840 success; pre/post safety refs 생성 및 변경 범위 비교 확인.
- 통합 보고서의 전형적 서보 드라이브 CRA 적용 가능성 및 Annex III/IV 표현은 제품별 결론이 아닌 사전 스크리닝 가설로 제한했다. 정확한 모델 증거 전 Unknown 유지.
- 다음 우선순위:
  1. Commission-hosted CRA Guidance PDF의 원본 bytes를 확보하고 공식 Commission source와 mirror fallback의 SHA-256을 직접 비교한다.
  2. Commission Implementing Decision C(2026) 7861 및 M/606 Annex의 원문/부속서 provenance, 발행·채택·인용 상태를 공식 출처에서 재확인한다.
  3. Guidance claim register 13개 및 M/606 41개 항목의 source locator/version/hash/claim mapping을 갱신하고 독립 재검증한다.
  4. 제조사/정확한 서보 드라이브 모델 P0 자료가 들어오면 CRA-001–035, 15 interfaces, 36 SEC controls를 model-specific evidence IDs로 연결한다.
- 제품 증거가 없는 동안 개별 scope/classification/conformity 및 구현/시험 상태를 임의로 확정하지 않는다.

## 2026-11-18 — Guidance 공식 관보 기준 전환
1. Commission Guidance의 현재 공식 인용은 OJ Communication C/2026/6013 (17.11.2026; CELEX 52026XC06013)으로 한다. C(2026) 5252는 27.07.2026 승인/게시 이력으로 보존한다.
2. EUR-Lex OJ PDF의 raw SHA-256, extracted-text SHA-256, page count 및 CI artifact provenance를 유지한다.
3. G-001–G-013의 page locator는 OJ 61-page PDF 기준으로 갱신했다. 다음에는 claim-by-claim substantive redline을 수행하고 문언 차이를 해결한다.
4. ANFR mirror는 historical copy로 보존하며 OJ PDF와 byte/text identity를 주장하지 않는다.
5. M/606 C(2026) 7861 및 Annex 최신 provenance, ESO adoption dates와 OJ harmonised-standard citation status를 별도 공식 출처에서 재검증한다.

## PR #52 병합 완료 및 다음 단계 — 2026-11-18
- OJ C/2026/6013 source acquisition, OJ page locator migration for 13 Guidance claims, provenance validator and CI updates merged in `d3956b7b364c507b8d59dcfc056763f2829ea867`.
- Exact-head Run #861 success: 158 passed, 1 xfailed; three PDF sources and official CRA HTML canary succeeded.
- Pre/post safety refs recorded in PROJECT_STATUS_CURRENT.
- Next: G-001–G-013 claim-by-claim substantive redline against OJ text; inspect claim-specific conditions, exceptions and footnotes, and verify relevant OJ page images. Then reconcile interface, requirement and SEC cross-links without converting non-binding Guidance into legal requirements.

## 2026-11-18 — Guidance substantive redline completed
- Completed claim-by-claim review of G-001–G-013 against OJ C/2026/6013 and visually checked the relevant PDF pages.
- Narrowed G-003 to the actual complex-system/interoperability text; distinguished external dependency risk from integrated-component due diligence in G-008; made identical spare-part conditions explicit for G-013; expanded G-004 continuing obligations.
- Next:
  1. Validate claim-to-CRA requirement IDs, IF interface IDs and SEC control IDs for semantic fit; do not treat non-binding guidance as a new requirement.
  2. Review M/606 C(2026) 7861 Annex source provenance and current ESO/OJ standard status.
  3. Continue evidence intake for exact servo-drive models; keep product-level determinations Unknown until evidence arrives.

## 2026-11-18 — Guidance claim redline 및 matrix link 검증 완료
- G-001–G-013 OJ C/2026/6013 substantive redline 및 page-image spot-check 완료.
- 13 claims ↔ 35 requirements ↔ 15 IF ↔ 36 SEC bidirectional link audit: 0 missing, 0 dangling. G-002 range notation을 명시적 ID로 확장하고 G-005↔IF-015 reverse link를 보완.
- 요구사항/IF/SEC matrix의 primary Guidance source URL을 EUR-Lex OJ ELI로 갱신.
- 다음 작업은 M/606 C(2026) 7861 Annex provenance, ESO adoption dates 및 OJ harmonised-standard citation 상태의 독립 원문 검증이다.

## 2026-11-18 — Cross-matrix validation gate hardened
- Added fail-closed bidirectional foreign-key validation between the 13 Guidance claims and the 35 CRA requirements, 15 IF interfaces and 36 SEC controls.
- Added regression tests for missing reverse links, dangling matrix claim IDs and unknown related IDs.
- Next independent source task: M/606 C(2026) 7861 Annex provenance, ESO adoption dates and current OJ harmonised-standard references.

## PR #54 merged — 2026-11-18
- OJ Guidance claim redline, matrix source updates, bidirectional cross-link validator and regression tests merged in `cd291c5161e7c3fdd9e494fe76749291a20b98de`.
- Exact-head Run #868 success (161 passed, 1 xfailed); post-merge safety ref identical to main.
- Next: M/606 C(2026) 7861 Annex provenance, ESO adoption date verification and current OJ harmonised-standard citations.

## PR #56 merged — 2026-11-18
- M/606 Annex I 41-item page locators corrected, including item 18 deadline cell on EN 2; ESO report and OJ citation status audited.
- Exact-head Run #879 success (161 passed, 1 xfailed); post-merge safety ref identical to main.
- Next: refresh ESO standards-stage evidence and Commission OJ harmonised-standard index; retain distinction between ESO adoption deadlines, publication forecasts and OJ citation.


## 2026-11-18 — ETSI M/606 최신 상태 점검
- ETSI Work Programme v2.3.3 (2026-11-17) 기준 M/606 활성 18개 work items를 확인하고, 서보 드라이브와 잠재적으로 직접 관련될 수 있는 EN 304 636(방화벽/IDS/IPS), EN 304 625(네트워크 인터페이스)를 상세 기록했다.
- ETSI의 adoption/publication/OJ publication 날짜는 계획 목표로만 취급한다. 실제 OJ 게재 확인 전 Article 27 추정 적합성 주장을 금지한다.
- 다음: CEN/CENELEC의 EN 40000 수평 표준 및 산업용 OT prEN 50770 작업의 최신 공식 상태를 별도 확인하고 41개 M/606 목록과 교차 대조한다.
- 상세: `reports/CRA_ETSI_M606_LIVE_STATUS_2026-11-18.md`.


## PR #58 병합 완료 — 2026-11-18
- ETSI M/606 Work Programme v2.3.3 상태 점검과 EN 304 636 / EN 304 625의 적용 경계 및 목표 일정이 `88d5eacd71c4267f64f674f0e990a25ed6fafd3a`로 병합되었다.
- Exact-head Run #883 성공: 161 passed, 1 xfailed; 공식 CRA PDF 3종 hash canary 및 공식 HTML 9개 source canary 성공.
- Pre/post safety refs 검증 완료; post-merge ref와 main identical.
- 다음: CEN/CENELEC EN 40000 수평 표준 및 산업용 OT prEN 50770 작업의 최신 상태를 공식 기록과 대조한다. 제3자 카탈로그는 보조 자료로만 취급한다.


## 2026-11-18 — CEN/CENELEC EN 40000 및 OT prEN 50770 상태 갱신
- CEN 공식 레코드상 EN 40000-1-1:2026 Published (DOR 2026-11-02, DAV 2026-11-18); OJ citation은 No citation expected. 따라서 “CRA 표준 미발행” 같은 포괄적 표현을 제거하고 ESO publication과 OJ citation을 별도 상태로 관리한다.
- FprEN 40000-1-3 Under Approval / Citation expected, prEN 40000-1-4 Work item. EN 40000-1-2는 ratification 2026-11-02 확인, 공식 상세 페이지 500 오류로 개별 원문 확인 미완료.
- CENELEC 공식 레코드 prEN 50770-1~6은 Committee stage / Citation expected; DOR/DAV 미기재.
- 상세 보고서 및 CSV 추적표: `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md`, `reports/CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.csv`.
- 다음: EN 40000-1-1/1-2 발행본 및 scope 확보, CENELEC OT 작업의 최신 stage 재조회, CRA OJ index 재확인.


## PR #60 병합 완료 — 2026-11-18
- CEN EN 40000-1-1 발행 상태와 CRA OJ citation 미예상 상태를 구분하고, CENELEC prEN 50770-1~6 공식 상태를 추가한 변경이 `1f39cb31d7f5e3466f1b22b798e9fc51971542da`로 병합되었다.
- Exact-head Run #887 성공: 161 passed, 1 xfailed. Pre/post safety refs 확인 완료.
- 다음: EN 40000-1-1/1-2 final text 확보·검증, CEN 1-2 개별 공식 레코드 재조회, CENELEC OT stage 및 OJ index 재확인.



## 2026-11-18 — CRA 요구사항–증거 추적 매트릭스
- 법적 요구사항에서 제품 통제·시험·최소 증거로 이어지는 EVD-01–EVD-16 provisional mapping을 생성한다.
- CRA 법적 의무 / 표준 공개 scope / 엔지니어링 제안 / 제품별 실제 증거 상태를 구분한다.
- EN 40000-1-2/1-3 최종 전문·조항을 확보하기 전에는 조항 번호 또는 normative shall 문장을 추정하지 않는다.
- 완료 기준: CSV 16행과 Markdown 표의 ID·내용 일치, 모든 행에 법적 locator/증거 패키지/상태 존재, 제품별 미확인 상태 유지, exact-head CI 성공, PR merge 후 safety ref와 main 동일.
- 후속 우선순위: 제품 P0 자료 확보 → EVD-01~07 제품 위험평가/아키텍처 → EVD-08~12 업데이트·취약점 프로세스 → EVD-13~16 기술문서·공급망 증거 → 표준 최종본 clause-by-clause redline.

## PR #62 1차 CI 및 최종 검증 게이트 — 2026-11-18
- PR #62 초기 head `360e83bba86a01bc83731ecd5ea5d0a6b975a8f6`, Run #891 success: 161 passed, 1 xfailed.
- Source blob identity, compile, CRA cross-matrix traceability, 3 Commission PDF fetch/hash, 9 official HTML source canary 성공.
- Artifact #14388303196, digest `sha256:47528b6e72af65dd95130a86a1442ac8f795a6eb3c34d93656369bf94734a2c2`.
- 검증 메타데이터를 문서에 반영한 뒤 변경된 최종 head에서 CI를 재실행하고 merge한다.


## PR #62 병합 완료 — 2026-11-18
- EVD-01–EVD-16 요구사항–증거 매트릭스 PR #62가 `612285ed720310cebd82340dc2e3b150e2c6f80a`로 squash merge됨.
- Final exact-head Run #896 success: 161 passed, 1 xfailed; source integrity, compile, CRA traceability, full pytest, official PDF/HTML canaries passed.
- Post-merge safety ref `safety/post-merge-pr62-2026-11-18` == main, 0 ahead / 0 behind.
- 다음 단계는 제품 P0 증거 intake 및 모델별 EVD 상태 갱신. 표준 전문이 확보되기 전 clause-level conformity mapping은 금지한다.


## 2026-11-18 — M/606 개정 결정 일정 반영
- C(2026) 7861 final(2026-11-10)이 C(2025)618 Annex I을 대체. 새 ESO adoption deadline: item 1 framework 및 item 15 vulnerability handling 2026-11-30; items 2–14 generic requirements 2027-10-30; items 16–41 vertical standards 2027-01-31.
- 공식 Commission 안내 페이지가 개정 사실을 확인. Article 2의 1개월 비수락 조건과 ESO 수령일은 미확인.
- OJ citation/Article 27 추정 적합성과 별도 단계임을 보고서/상황판에 명시한다.
- 상세: `reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md`.


## PR #64 초기 CI 검증 기록 — 2026-11-18
- Initial exact-head Run #900 / ID `44219718958` success: 161 passed, 1 xfailed.
- CRA traceability: 13 claims / 15 interfaces / 35 requirements / 36 SEC / 41 M/606 items; bidirectional links true.
- 9 official CRA PDF sources canary, artifact upload and official HTML canary passed.
- Artifact #14390620457, digest `sha256:b7ced7629ab9e88bf44190d6d4f5fd50fc91f45bfc33a83ae09a02c1833e2f20`.
- Record this result then rerun exact-head CI before merge.


## PR #64 병합 완료 및 다음 작업 — 2026-11-18
- C(2026)7861 일정 정정 PR #64가 `41229486baded6336aa43cd3b5de375476fe92f3`로 squash merge됨.
- 최종 exact-head Run #905 success: 161 passed, 1 xfailed; source integrity, compile, CRA cross-matrix traceability, official CRA PDF/HTML canaries 통과.
- Artifact #14388899741, digest `sha256:ecd0f1181457270eb5d3d9fd5e60c2271aafc730ac1250a025499aa614f5cb8b`.
- Post-merge safety ref `safety/post-merge-pr64-2026-11-18` == main.
- 후속 우선순위: (1) M/606 Article 2 ESO receipt/non-acceptance 사실 확인, (2) 제품 P0 자료 intake checklist, (3) CRA 적용성/제품 분류 decision matrix. 제품 데이터가 없으므로 모델별 결론/증거 상태는 Unknown 유지.

## 다음 실행 단계 — 제품 적용성 및 P0 evidence intake
- CRA Article 2 적용성(제품 경계·연결성·제외)과 Annex III/IV 제품 분류(core functionality)는 별도 판정으로 관리한다.
- Commission Implementing Regulation (EU) 2025/2392의 기술 설명을 Annex III/IV 판단 기준에 포함한다. 네트워크 포트·부가 기능만으로 분류하지 않는다.
- 서보 드라이브 P0 intake 보고서: `reports/CRA_SERVO_DRIVE_APPLICABILITY_CLASSIFICATION_AND_P0_INTAKE_2026-11-18.md`.
- 다음 완료 기준: 자료 intake 항목과 EVD-01~16 연결 검증, 법적 locator/제품 경계/분류 근거의 상호 추적, exact-head CI 성공.


## 2026-11-18 — 제품 분류 법령 원문 재대조
- EUR-Lex 2025/2392 recital (2)–(6), Annex I #10/#11/#12를 직접 대조하여 인터페이스/OS/라우터·스위치 경계를 더 정확히 명시한다.
- Annex IV critical category 해당과 Article 8(1)의 delegated-act 기반 인증 의무를 구분한다. 제품 범위·적용 가능한 delegated act 확인 전 인증 의무를 단정하지 않는다.
- CRA Article 6 및 Annex I 요구사항은 중요한/핵심 제품 분류와 무관하게 적용성 있는 제품에 대해 별도로 검토한다.
- PR #65/#66 병합·CI 및 사후 안전 refs는 상황판과 세션 로그에 기록.


## PR #67 완료 — CRA 분류 기준 보완 및 기록 정합성
- PR #67 merge `86af2db5fadf5098b22b39d2d6c07710ed0033ee`; exact-head Run #912 success, source integrity/compile/traceability/full tests/official PDF+HTML canaries 통과.
- Artifact #14391457563, digest `sha256:f172ed1762a693f626e8c5781638c557e9d5471d6750b5315a54cae9398d919c`.
- Post-merge safety ref `safety/post-merge-pr67-2026-11-18`와 main 동일.
- C(2026)7861 Article 2 ESO 수령일·비수락 통지는 공개 원문 확인이 남아 있어 미확인 상태 유지.


## M/606 Article 2 절차 확인 업데이트
- 원래 M/606(C(2025)618)은 CEN-CENELEC 공식 발표에 따라 2025-04-03 CEN/CENELEC/ETSI 수락 확인.
- C(2026)7861 개정 결정의 수령일 및 Article 2 비수락 통지 여부는 별도 확인사항. 원래 요청 수락 사실을 개정 요청 수락으로 간주하지 않는다.
- 세부: `reports/CRA_M606_AMENDMENT_C2026_7861_DEADLINES_2026-11-18.md` §5A.


## PR #69 완료 — M/606 acceptance status 분리
- PR #69 merge `8089cb96fdeba390dafe6991b19abfa1bc5b3e25`, Run #916 success.
- 원래 M/606의 2025-04-03 수락과 C(2026)7861 amendment Article 2 절차를 구분하여 관리한다.
- 개정 결정의 개별 수령일·비수락 통지는 미확인으로 유지.
- 사후 안전 ref `safety/post-merge-pr69-2026-11-18`와 main 동일.


## PR #70 병합 완료 — 2026-11-18
- Merge commit `ca65475db4ca53d23ee55308c9c9616a054ea756`; PR #70 documents PR #69 merge and M/606 acceptance-status distinction.
- PR head `b5fb2adc3eeba9d9839ff3d3519b128743cc6878`, Run #918 success: 161 passed, 1 xfailed; source integrity, compile, CRA traceability and official PDF/HTML canaries passed.
- Artifact #14391727520, digest `sha256:f737a27f61f2b6cd153731941c9e615e4379912d03ccfc3696f0eea7b2ad0d09`.
- Pre/post safety refs: `safety/pre-pr70-merge-checkpoint-2026-11-18`, `safety/post-merge-pr70-2026-11-18`; post-merge ref == main at merge.
- Post-merge exact-main Run #919 / ID `44228633470` on merge SHA `ca65475db4ca53d23ee55308c9c9616a054ea756` succeeded: 161 passed, 1 xfailed; source integrity, compile, CRA traceability and official CRA PDF/HTML source canaries passed. Artifact #14393668052, digest `sha256:3d6314562d9ac4f34d645ef3191be6e499ae2d25e829968e17658717bdf2ae22`.


## PR #71 병합 완료 및 재개 기준 — 2026-11-18
- PR #71 문서/로그 동기화가 exact-head Run #921 성공 후 squash merge되었다. Merge SHA: `adcec0a0cb94a326e6b7d9b8c242c4ae3dab4152`.
- Main exact commit Run #922 성공: 161 passed, 1 xfailed; source integrity, compile, CRA traceability, official PDF and 9-source live canaries passed.
- Pre/post safety refs are preserved; post-merge ref equals main. Artifact #14393784949, digest `sha256:db75a58638b43fbe1798c70b7c4dad5951cb1b1f98bfa013fa771184e6cf2126`.
- 다음 우선순위는 CRA-001–CRA-035 행 단위 법령 의미 감사 및 근거 provenance 검증을 완료하고, 통합 보고서·요구사항/SEC 매트릭스·독립 감사 간 불일치를 정정하는 것이다. 제품별 입력이 없으므로 적용성·분류는 Unknown으로 유지한다.


## PR #72 병합 완료 — 2026-11-18
- PR #72 merge `293a27a8ea2a8e03f58db50bbe27d2aaea194c8d`; exact-head Run #923 and exact-main Run #924 both success.
- Run #924: 161 passed / 1 xfailed; CRA traceability and live official source canaries passed. Artifact #14394119675, digest `sha256:43a5e60b947890886baeee6c355beae857928f3c47deb9d76489244199accb3a`.
- Pre/post safety refs preserved; post-merge ref == main. Continue with independent product-agnostic architecture verification and standards status updates; no model-specific claims without product evidence.


## 참조 아키텍처 v0.2 설계 보강 — 2026-11-18
- 실시간 cyclic data path, privileged management path, secure update/boot path 및 event logging path를 분리한다.
- 단일 MCU + MPU/RTOS isolation과 dual-MCU split은 위험·실시간성·BOM·복구·공급망을 기준으로 비교하며, 특정 구성을 선결하지 않는다.
- secure boot, signed update, key storage 등은 MCU 기능/부품 revision 검증 전 확정하지 않는다. 기술 선택은 CRA 결과 요구와 구체 구현 후보를 분리한다.
- 설계 수용 기준을 EVD-01~16 및 SEC-001~036에 연결하고, 모델별 회로·부품·시험 증거 확보 전에는 모든 제품별 상태를 Unknown/미검증으로 유지한다.


## PR #73 병합 완료 및 exact-main 검증 — 2026-11-18
- Merge `16ab607a919c6bfa4fee8dc90ab5af2ea2f53352`; exact-head Run #925 및 exact-main Run #926 success.
- Run #926: 161 passed / 1 xfailed; source integrity, compile, CRA traceability, 9 official sources and Article 13(8) canaries passed. Artifact #14394634118, digest `sha256:cf7d6d6ef7020d5381a4a2f201f50bf3171251155459505420ffce16998ef027`.
- Pre/post safety refs preserved; post-merge ref == main. Next architecture update is in `cra/servo-drive-security-architecture-v02-2026-11-18` and must pass exact-head CI before merge.


## PR #74 병합 완료 및 exact-main 검증 — 2026-11-18
- PR #74 merge `48dd8f7bc0617ec0c67eadf80a7e7cc364b862c0`; exact-head Run #927 및 exact-main Run #928 success.
- Run #928: 161 passed / 1 xfailed; source integrity, compile, CRA traceability, 9 official sources and Article 13(8) canaries passed. Artifact #14395476337, digest `sha256:6aaf8fc76f87121e42f8190fec9568121fbd8a0005695ce8de87ff776f0d1d93`.
- Pre/post safety refs preserved; post-merge ref == main.
- Next: source-backed ST-vs-TI MCU candidate benchmark. Actual ST part number and motor/control constraints remain P0 unknowns; do not declare G474RE/H753XI as the installed MCU.


## MCU 후보 벤치마킹 — ST 기준 / TI 비교 (2026-11-18)
- 예비 비교 문서 `reports/CRA_SERVO_DRIVE_MCU_PLATFORM_BENCHMARK_2026-11-18.md` 생성. ST 후보 STM32G474RE(모터제어 주변장치), STM32H753XI(고성능/crypto)와 TI MSPM0G3529-Q1(보안 기능 통합)을 비교한다.
- 실제 ST 부품번호 미확정. 제품 marking/BOM, FOC/current-loop timing, PWM/ADC/encoder, fieldbus, CPU/RAM budget 확보 전에는 동급성·승자·교체 가능성을 판단하지 않는다.
- 동일 조건 실측(WCET/jitter, ADC/PWM sync, comms+crypto load, update recovery) 후에만 가중치 평가를 수행한다.


## PR #75 병합 및 Run #930 완료 — 2026-11-18
- PR #75 merge `1d7325baa592b35585fde850cf5a155988ba4cde`; exact-head Run #929 및 exact-main Run #930 모두 success.
- Run #930: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14395188271, digest `sha256:63017368ac7db313f298b23c24d288f9c6781c27cc26472baa6d408abb244695`.
- Pre/post safety refs preserved; post-merge ref == main.
- MCU benchmark preliminary comparison is merged; next add MCU-T01–T12 measurement protocol and result-recording gates. Do not score/select before actual ST part number and control requirements are supplied.


## MCU-T01–T12 시험 매트릭스 — 2026-11-18
- 동일 조건으로 current/speed/position loop WCET, ADC/PWM sync, encoder/QEI, interrupt/DMA contention, fieldbus load, crypto load, secure boot/update, fault injection, memory/debug protection, power/reset, environment/endurance를 검증한다.
- 합격 기준은 제품의 실제 제어 주기/성능 요구에서 도출한다. 문서가 임의의 loop period/jitter limit을 만들지 않는다.
- 모든 미실시 시험은 Not Run, 미확인 입력은 Unknown으로 유지하고, 결과에는 part number/silicon revision/board/firmware/toolchain/source hash를 기록한다.


## PR #76 병합 및 Run #932 완료 — 2026-11-18
- PR #76 merge `48afedaf8114688a51a7e6ed695c514277bd6407`; exact-head Run #931 및 exact-main Run #932 모두 success.
- Run #932: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14395691349, digest `sha256:ec315a8b305f9b572452d42846de38a3698d431256faff36162ddb733303385a`.
- Pre/post safety refs preserved; post-merge ref == main.
- MCU-T01–T12 test protocol and result capture fields are merged. Next P0 input is the exact ST MCU order code/marking and product control requirements. Keep tests Not Run until hardware/product evidence exists.


## PR #77 병합 및 Run #934 완료 — 2026-11-18
- PR #77 merge `caa32ed9ac6679b21b619155cdf28d1b75d81c33`; exact-head Run #933 및 exact-main Run #934 success.
- Run #934: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14395218493, digest `sha256:8c827f786583bb5d2f8d14224e990b194ae50bf7f1393b4b9009925d123773da`.
- Pre/post safety refs preserved; post-merge ref == main.
- The next blocker is product-specific input: exact ST MCU part number/marking and drive control requirements. Existing MCU benchmark and MCU-T01–T12 plan are ready for product-specific completion; do not invent hardware values or report tests as executed.


## PR #78 병합 및 Run #936 완료 — 2026-11-18
- PR #78 merge `441b0198bcd695752d1adb053d8e077f91426a0a`; exact-head Run #935 및 exact-main Run #936 success.
- Run #936: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14396500899, digest `sha256:6ef8037213259261dd57bcc3b1229d50f58947092a953bbc12ffc106ee4c8a05`.
- Pre/post safety refs preserved; post-merge ref == main.
- Documentation checkpoint is current. The next blocker is exact installed ST MCU identification and drive control requirements; ask for chip top-marking/BOM before any product-specific benchmark or recommendation.


## PR #79 병합 및 Run #938 완료 — 2026-11-18
- PR #79 merge `2e377127a26d3d9c0232089cad583ff6f2d328ca`; exact-head Run #937 및 exact-main Run #938 success.
- Run #938: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14396566514, digest `sha256:d9f1c96ecab857a65c699b18489315fcf5edbe0892234dc5c42157dceb2dd156`.
- Pre/post safety refs preserved; post-merge ref == main. Current product-specific blocker: actual ST MCU order code/marking and drive control requirements.


## PR #80 병합 및 Run #940 완료 — 2026-11-18
- PR #80 merge `950cacef2ea4ed2bb4062f09ef0180a5621375a5`; exact-head Run #939 및 exact-main Run #940 success.
- Run #940: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14396950302, digest `sha256:dca34e12cfea64f9f6a5676a084910e465bf2f8bb415eee4173681683ea9a9cb`.
- Pre/post safety refs preserved; post-merge ref == main. Next action requires user-supplied exact ST MCU part number/marking and drive control requirements; avoid fabricated product-specific assumptions.


## PR #81 병합 및 Run #942 완료 — 2026-11-18
- PR #81 merge `11b7ccac639501b98e9a9f6c76dfac473d6e0535`; exact-head Run #941 및 exact-main Run #942 success.
- Run #942: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14397065458, digest `sha256:0d5a340c3ac3e0435704d5543f38ab35bd883ea7a5c30adfe1b3983db24882bf`.
- Pre/post safety refs preserved; post-merge ref == main. Next technical decision cannot be made until actual ST MCU part number/marking and drive control requirements are supplied.


## PR #82 병합 및 Run #944 완료 — 2026-11-18
- PR #82 merge `572de72c8bfab7a1e1e144527783c1508bb26cae`; exact-head Run #943 및 exact-main Run #944 success.
- Run #944: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14396972010, digest `sha256:f23e616d121c61d5825774f1098f213b40cff65e858a527807060d71b02734c4`.
- Pre/post safety refs preserved; post-merge ref == main. Product-specific MCU work is paused at the evidence gate: exact ST MCU order code/marking and control requirements must be identified before scoring or hardware tests.


## PR #83 병합 및 Run #946 완료 — 2026-11-18
- PR #83 merge `0255e50f003792fa8f5d0d3a130e45dda3491c3d`; exact-head Run #945 및 exact-main Run #946 success.
- Run #946: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14396926567, digest `sha256:0da05816f553bfbe1f541df001f2f487bd66176e3b454eb04ee47cffd3330a33`.
- Pre/post safety refs preserved; post-merge ref == main. Product-specific MCU benchmark still requires actual ST MCU part number/marking and drive control requirements.


## PR #84 병합 및 Run #948 완료 — 2026-11-18
- PR #84 merge `774551f378f59c82ce34342f63fd595d4c743852`; exact-head Run #947 및 exact-main Run #948 success.
- Run #948: 161 passed / 1 xfailed; source integrity, compile, CRA traceability 13/15/35/36/41, 9 official sources and Article 13(8) canaries passed. Artifact #14397286074, digest `sha256:1cd7be5fcd710e5fc193595602c974a701f1242f32ec5a549ea61a11c9eec388`.
- Pre/post safety refs preserved; post-merge ref == main. Product-specific MCU work requires actual ST part number/marking and drive control requirements.


## 현재 게이트 재확인 — 2026-11-18
- Main 최신 기준: PR #85 merge `db05c57103fc9039347b61a29f473fe1af1c7082`; exact-main Run #950 success (161 passed / 1 xfailed), 9 official CRA source canaries and Article 13(8) locator/quote passed.
- 공통 산출물은 존재하나 제품별 입력은 비어 있다. 정확한 드라이브 모델/SKU, 실제 ST MCU 주문코드·silicon revision, control-loop/PWM/ADC/encoder/fieldbus 요구를 확보하기 전 제품별 CRA 판정 및 MCU 점수화 금지.
- MCU-T01~T12는 시험 프로토콜만 준비됐고 전부 Not Run. 측정 전 pass/fail·승자·대체 결론 금지.
- M/606 개정 납기는 ESO delivery schedule이다. CRA 2027-12-11 일반 적용일 또는 OJ 인용/Article 27 presumption과 혼동하지 않는다. 개정 C(2026)7861 Article 2의 수령일·비수락 여부는 미확정.
- 다음 우선순위는 제품별 증거 intake → 적용성/core functionality 판정 → EVD/SEC 연결 → 실제 bench 시험이며, 반복적인 문서 checkpoint만으로 기술 작업이 완료된 것처럼 표시하지 않는다.


## 자동화 신뢰성 회귀시험 — Git push fail-fast (2026-11-18)
- PR #87에서 stale xfail을 실제 현재 동작을 검증하는 통과 테스트로 교체했다. git push 실패 시 subprocess check=True → 명시적 오류 로그 → SystemExit(1), 성공 동기화 메시지는 출력하지 않는다.
- 격리 테스트 workflow의 exact blob pin만 갱신했으며 production main.py / production run.yml은 미변경.
- Exact PR and exact-main CI: 162 passed / 0 xfailed. 향후 P1-B3 관련 변경은 이 실패 종료 계약을 회귀 기준으로 유지한다.


## 2026-11-19 우선순위 보완 — 제품 분류의 선행 게이트
- 제품별 EVD 추적 및 Article 32 경로 확정 전에 G1 제품 단위 → G2 intended purpose → G3 연결성/원격처리 → G4 Annex III/IV core functionality → G5 평가 경로 순으로 증거를 승인한다.
- Annex III/IV 분류는 제품 전체의 core functionality와 Regulation (EU) 2025/2392 기술 설명에 근거한다. 통합 구성요소의 존재만으로 완제품을 자동 분류하지 않으며, 구성요소 보안 위험은 완제품 위험평가에 계속 반영한다.
- Annex III/IV 비해당을 CRA 비적용으로 오인하지 않는다. Article 2 적용성과 Articles 7–8 분류는 별도 판정한다.
- 다음 기술 우선순위: (1) 분류 게이트 독립 검토 및 매트릭스 정합성 확인, (2) 제품별 P0 자료 수집, (3) EVD/SEC 추적, (4) 실제 MCU/드라이브 시험. 제품 식별 자료가 확보되기 전까지 제품별 점수·Pass·선정 결론을 만들지 않는다.

## 2026-11-19 — EVD 증거 합격 게이트 강화
- EVD-01~EVD-16 각각에 권고 책임 역할, 생애주기 단계, 검증 방법, 내부 합격 기준을 연결한다.
- 책임 역할은 조직 설계 제안이며 법적 책임 주체를 대체하지 않는다. 내부 합격 기준은 법령의 문언이나 정량 요구를 임의로 만들어내지 않고, 제품 위험평가·제조사 사양·법정 기한에 근거해 승인한다.
- 시험 결과는 제품 모델/HW/FW 버전, 환경, 절차, 예상/실제 결과, 로그, 시험자·검토자와 연결한다. 문서 존재만으로 구현/시험 Pass를 부여하지 않는다.
- PR #89 / Run #959가 최신 main 검증 기준이며, 다음 PR에서 현황판과 로그를 최신 기준으로 유지한다.


### Phase 4 추가 완료 기준 — EVD–CRA–SEC 추적
- EVD-01~16 각 행에 관련 CRA 요구사항 및 SEC 통제의 후보 링크를 유지한다.
- validator가 모든 EVD/SEC ID의 존재·중복·누락·외래키를 fail-closed로 검사한다.
- 교차 링크는 후보 추적일 뿐 제품별 적용성 또는 구현·시험 적합성의 증거가 아니다.


### Phase 4 추가 완료 기준 — 제품 증거 register
- E-001~E-015 제출 자료를 EVD-01~16과 연결하고 제품 variant별로 독립 관리한다.
- 원본 provenance(SHA-256, 발행자, 버전/일자, 수집일, 페이지/절 locator, 언어)를 기록한다.
- 증거 상태는 not_provided → received → source_verified → content_reviewed → cross_checked → accepted/rejected로 관리하며, not_applicable_with_rationale는 별도 근거 게이트를 적용한다.
- accepted/비적용 판정은 필수 메타데이터와 검토자·일자·근거가 없으면 validator가 fail-closed 한다.
- 템플릿은 자료 수집 양식일 뿐 제품별 적합성 판단을 의미하지 않는다.


### Phase 4 — 제품별 증거 register 완료 기준 (PR #94)
- E-001~E-015와 EVD-01~16 연결 템플릿을 main에 반영했다.
- variant별 provenance, SHA-256, locator, reviewer/date, cross-check, decision rationale를 기록한다.
- 상태 승격은 validator가 fail-closed로 검사한다. 현재 모든 항목은 not_provided이며 실제 제품 증거 수령 후에만 상태를 갱신한다.


## 2026-11-19 — PR #97 최신 기준점 동기화
- main 기준점: PR #97 merge `9ebab690b6cbbf0f3588bfeab16c622dca4d65e9`.
- PR #97 exact-head Run #983 및 exact-main Run #984 모두 success, 172 passed / 0 failed. Exact-main Run #984는 source integrity, compile, CRA traceability, full pytest, official CRA PDF canary, artifact upload, live EUR-Lex canary를 통과했다.
- PR #97 사후 안전 ref `safety/post-merge-pr97-2026-11-19`와 main의 동일성을 확인했다.
- 다음 실질 우선순위는 이미 구축된 E-001~E-015 증거 수집 체계에 실제 제품 자료를 투입하는 것이다. 제조사/정확한 모델·SKU, 데이터시트, 설치·사용 매뉴얼이 없으면 제품별 Article 2 및 Annex III/IV 판정은 보류한다.
- 문서 동기화만을 위한 반복 PR을 양산하지 않는다. 다음 문서 갱신은 법령/제품 증거/코드의 실질 변경과 함께 수행한다.


## 2026-11-19 — PR #99: 2025/2392 공식 출처 및 Annex locator 검증
- Official CRA source pack을 v4로 올리고 Commission Implementing Regulation (EU) 2025/2392를 공식 Publications Office/Cellar source catalog에 추가했다.
- 2025/2392 원문 33,865 visible chars를 수집하고 excerpt SHA-256 `9c9715a1c463dca7ccf499e5f901ac642426b70a2aba89eb479525fbb78a1702`를 기록했다.
- live canary가 core-functionality recital marker와 Annex I category 10 / Annex II category 1을 실제 원문에서 추출·검증한다.
- Annex category 번호 1.과 각주 (1) 혼동을 재현하고 명시적 Annex II category 1 locator와 회귀 테스트로 해결했다.
- PR #99 exact-head Run #993: 173 passed / 0 failed; source pack 10, PDF sources 3개 수집·해시 및 live canary 통과.
- 특정 서보 드라이브의 제품별 분류·적합성 판정은 제품 자료가 없으므로 계속 Unknown. 다음 단계는 실제 모델/SKU와 데이터시트·매뉴얼 수집이다.


## 2026-11-19 — PR #101/#102: 공식 source pack provenance artifact 영속화
- 10개 공식 CRA HTML source의 ID, URL/final URL, kind/version, visible-text 길이, full-text SHA-256, prompt-excerpt SHA-256, retrieval timestamp, related URL/corrigenda metadata를 JSON manifest로 생성한다.
- PR #101 exact-head Run #998에서 174 passed / 0 failed 및 artifact 업로드를 확인했다. 개행 escape를 재검토해 JSON parse 검증 공백을 발견했고, 초기 artifact는 authoritative evidence로 사용하지 않도록 기록했다.
- PR #102에서 실제 newline serialization 및 json.loads + object round-trip fail-closed 검증을 추가했다.
- PR #102 exact-head Run #1000: 174 passed / 0 failed. 10-record manifest artifact #14496534452, SHA-256 `7f2836072bdfa38b7857c47bdac4c6fdb2b71c38bd29b987889aad0646e78cc7`; PDF artifact #14497431708.
- 최신 main: `84101bcc8871e41f8a25de3edf892666b1650b8c`; post-merge safety ref `safety/post-merge-pr102-2026-11-19`와 main identical.
- 제품별 평가를 시작하려면 정확한 제조사/모델/SKU와 데이터시트·사용/설치 매뉴얼이 여전히 필요하다. 증거가 없으면 모델별 판정은 Unknown 유지.


## 2026-11-19 — LS메카피온 서보드라이브 제품군 예비 분석
- 사용자 지정 대상: LS메카피온 서보드라이브 제품군. 정확한 모델/SKU는 아직 미지정.
- 제조사 제품 목록 기준 13개 계열을 1차 인벤토리화했다: iX700M, iX7M, iX7NH, L7NHA, L7NHB, L7NHF, L7PA, L7PB, PHOX, L7C, L7SA, L7SB, GEM.
- 제조사 자료실의 iX700M/iX7M/iX7NH 등 매뉴얼 목록, DriveCM, ESI 파일, CAD, 가이드북 인덱스를 확인했다. 개별 PDF/설치파일 원본 다운로드·해시·페이지 분석은 다음 단계.
- 새 보고서: `reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md`. 초보자용 CRA 개요, 제품군별 스펙 요약, 데이터 연결, 제품 경계, Annex III/IV 예비 분류, Article 13/14 의무, 위협 시나리오, 참조 아키텍처, 시험·증거 계획 및 용어집을 포함.
- 법령 수집은 전수 완료가 아니다. HTML source pack 10개 및 PDF source pipeline 3개는 주요 CRA 법령·공식자료를 다루지만, 관련 제품법령, 최신 ENISA FAQ, M/606 41개 표준 상태, 최종 표준 전문 및 OJ 조화표준 인용 감사가 남아 있다.
- 모델별 EU 공급, exact SKU/HW/FW, 실제 인터페이스·프로토콜, SBOM, PSIRT, 지원기간, 시험 증거가 없으므로 제품별 판정 Unknown, 시험 Not Run 유지.
- 다음 P0: 제조사 카탈로그·모델 매뉴얼 원본 수집/해시 → 모델/variant 매핑 → Article 2 적용성 및 Annex III/IV 판정 → EVD/SEC/시험 연결.


## 2026-11-19 — PR #104 LS메카피온 제품군 예비 분석 병합
- PR #104 merge SHA / main: `c3d234240d342d82cf9402ef0b07b82531ddee03`; post-merge safety ref `safety/post-merge-pr104-2026-11-19`와 main identical.
- 신규 보고서 `reports/CRA_LS_MECAPION_SERVO_DRIVE_FAMILY_PRELIMINARY_ASSESSMENT_2026-11-19.md` v0.1, 542 lines. LS메카피온 공개 13개 제품 계열, CRA 입문 설명, Article 2 데이터 연결, 제품 경계, Annex III/IV 핵심 기능, Article 13/14, 위협 시나리오, 참조 아키텍처, 12개 시험 후보, E-001~E-015, 용어집 포함.
- Exact-head Run #1004 / ID 44485297107: success, **174 passed / 0 failed**. Source integrity, compile, CRA traceability, full pytest 통과.
- Live CRA HTML 10-source canary 통과. JSON provenance manifest 10 records parse + round-trip 통과. Artifact #14509668548 SHA-256 `1d3ac8ea2e049780161766ef158fecfa3ab2a7d795b477424b339e5004772bf6`.
- PDF canary는 EUR-Lex C/2026/6013 endpoint empty body로 temporary outage / SKIPPED; PDF artifact 없음. PDF canary 성공으로 주장하지 않는다.
- 법령 전수 수집·분석, 모델별 CRA 적용성/분류, 실제 보안 구현 및 시험은 미완료. 정확한 SKU/HW/FW와 EU 공급 증거 확보가 다음 단계.


## 2026-11-19 — CRA 공식 지침·M/606 개정 반영 및 제조사 매뉴얼 수집
- Commission guidance C(2026) 6013 및 Commission CRA standardisation page의 2026-11-10 M/606 개정 사실을 LS메카피온 예비 보고서 v0.2에 반영한다.
- M/606 41개 표준의 제출 일정은 CRA 법적 적용일이나 OJ 조화표준 인용과 별개로 관리한다. Article 27 presumption은 OJ 인용 상태·범위 확인 전 부여하지 않는다.
- LS메카피온 iX700M/iX7M/iX7NH 매뉴얼의 최신 공개 첨부 메타데이터를 확인했으나 공식 download endpoint가 접근 오류를 반환했다. PDF 본문/해시/페이지 분석은 미완료이며 증거 register 상태를 승격하지 않는다.
- 다음 P0: 공식 PDF 원본 확보 경로를 정상화하거나 제조사에 원본 제공을 요청하고, 수령한 파일을 SHA-256·페이지 수·개정·인터페이스·업데이트·보안 관련 locator와 함께 검토한다.
- 다음 법령 트랙: M/606 41개 개별 표준의 진행 상태 및 OJ 인용 여부, Commission guidance/FAQ, ENISA 자료, CRA와 연관 제품법령을 각각 1차 출처 기준으로 대조한다.


## 2026-11-19 — CRA 위임규정·ENISA 이행자료 조사 확장
- PR #106 merged: 2c24b16ede905009f2a2f07edb4072bb9c244316; exact-head Run #1008 success, 174 passed / 0 failed; 10-source live HTML canary and manifest round-trip passed; PDF canary skipped on empty EUR-Lex response.
- LS메카피온 보고서 v0.3에 Delegated Regulation (EU) 2025/1535(특정 L-category vehicle 제품의 CRA 제외 및 pedal-assisted L1e 예외), Delegated Regulation (EU) 2026/881(Article 14 신고 수신 후 CSIRT 전파 지연)을 반영했다.
- ENISA 2026 자료: SME Cyber Resilience Maturity Assessment Model, Secure by Design and Default Playbook, SBOM Technical Advisory, Secure Update Mechanisms Technical Advisory, Single Reporting Platform 안내를 제조사 절차에 연결했다.
- ENISA 자료는 비구속 참고자료로 구분하고 CRA 법적 요구·OJ harmonised-standard citation·Article 27 presumption과 혼동하지 않는다.
- 다음 단계: M/606 41개 개별 표준별 진행·최종안·OJ citation 상태, 제품별 적용 가능한 sectoral legislation, Commission FAQ 최신판, ENISA reporting/SRP 최신 매뉴얼을 근거·날짜·locator와 함께 감사한다.


## 2026-11-19 — CRA/Machinery Regulation 병행 적용 및 제품법령 스크리닝
- PR #107 merged: 0682d83f891a20438d6d37eb231c3b20ca72c67e; exact-head Run #1010 success, 174 passed / 0 failed; 10-source HTML canary + manifest round-trip success; PDF canary skipped on empty EUR-Lex body.
- Commission CRA FAQ (last updated 2026-09-04) states products simultaneously within CRA and Machinery Regulation (EU) 2023/1230 must consider both sets of requirements and both conformity assessment procedures. Compliance with one does not automatically satisfy the other.
- Machinery Regulation applies from 2027-01-20; Annex III 1.1.9 Protection against corruption and 1.2.1 Safety and reliability of control systems have direct relevance to machine safety/cybersecurity interactions.
- LS Mecapion report v0.4 separates drive component boundary from final machine / partly completed machinery boundary and adds a conditional screen for EMC, LVD, RED, RoHS, WEEE and Product Liability Directive.
- Do not infer that every drive is machinery, or that machinery rules automatically exclude CRA. Product variant, intended use, supply form, wireless option and economic-operator roles remain unknown.
- Next: model-by-model legal applicability table with exact product evidence; M/606 41-standard status/OJ citation audit; sector-law amendments and harmonised standards verification.


## 2026-11-19 — CRA 표준화 작업계획 확장
- PR #108 merged: 4a1b44501dec629ae2f42106d6b8d200f177765a; exact-head Run #1012 success, 174 passed / 0 failed; live 10-source HTML and manifest round-trip passed; PDF canary skipped on empty EUR-Lex response.
- Commission Notice C/2026/1695 (OJ C, 19.3.2026) Action 5는 M/606을 보완해 CRA Annex III/IV 밖 제품, 특히 machinery, rail, lifts, agricultural machinery, AI systems, solar inverters에 대한 추가 표준화 요청을 계획한다.
- 이는 연간 작업계획 및 향후 요청 방향이며, 이미 발행된 조화표준이나 Article 27 presumption을 뜻하지 않는다.
- 보고서 v0.5는 M/606 41개 표준과 C/2026/1695 Action 5를 별도 추적하도록 업데이트한다.
- 다음: 41개 M/606 개별 표준 현황, C(2026) 7861 상세 납기, Action 5 후속 요청 채택 여부, CRA 관련 OJ 인용 상태를 개별 레코드로 검증한다.


## 2026-11-19 — M/606 개정 Annex I 원문 검증
- PR #109 merged: 172caa7427dd7af412d555bf2a82660537c0e16f; exact-head Run #1014 success, 174 passed / 0 failed; 10-source HTML canary + manifest round-trip passed; PDF canary skipped on empty EUR-Lex response.
- Commission Implementing Decision C(2026) 7861 final Annex I 원문을 직접 검토했다. ESO adoption deadlines: item 1 and 15 = 30/11/2026; items 2–14 = 30/10/2027; items 16–41 = 31/01/2027.
- 기존 M/606 41행 CSV와 cra_traceability.py validator의 deadline 기대값이 개정 원문과 일치한다. 날짜 수정은 필요하지 않았다.
- 이 날짜는 ESO 표준 채택기한이지 제조자의 CRA compliance deadline이 아니다. OJ citation 전까지 Article 27 presumption을 주장하지 않는다.
- 보고서 v0.6에 41개 일정, 제품군 관련 항목 25/36/28–30/37–38 해석, 검증 범위를 반영한다.
- 다음: M/606 개별 41개 표준의 실제 진행 상태 및 OJ citation audit, C/2026/1695 Action 5의 후속 표준화 요청 발행 여부 확인.


## 2026-11-19 — CRA SRP v1.3 운영 준비 트랙
- PR #110 merged: 57c7734d59b5046598e67aefd5d74a2ea29d3e2b; exact-head Run #1016 success, 174 passed / 0 failed; 10-source live HTML canary and manifest round-trip passed; PDF canary skipped on empty EUR-Lex response.
- ENISA SRP FAQ (2026-10-15), SRP platform v1.3 (2026-11-04), AR User Manual v1.3 reviewed.
- Reporting readiness: AEV / severe incident definitions; 24h/72h/AEV 14d/SI 1 month deadlines; Primary AR=1, Secondary AR<=20; EU Login/MFA; no initial API; English UI; outage fallback; CDaC selection and integrated-component notification.
- Critical operational issue: SRP v1.3 FAQ says the current 72h counter may display overdue early because it adds 48h after Early Warning submission rather than calculating from original awareness time; AEV Final Report counter is not implemented. Internal legal deadline tracker is mandatory.
- Article 14 reporting applies from 2026-09-11 to all in-scope products, including products placed on the market before 2027-12-11, when the manufacturer becomes aware after reporting obligations apply. Integrated-component AEV reporting responsibilities are assessed at both finished-product and separately marketed component level.
- Next: incorporate SRP v1.3 manual into internal SOP / exercise; continue M/606 per-standard status and OJ citation audit; acquire manufacturer manual PDFs.


## 2026-11-19 — PR #111 신고 운영자료 반영 및 다음 우선순위
- PR #111 merged: 26e6cc348f0e4207fe04a4d789ace38b7434b8ea; exact-head Run #1018 success, 174 passed / 0 failed; 10-source HTML canary and manifest round-trip passed; PDF canary skipped on empty EUR-Lex response.
- LS메카피온 report v0.7 now contains CRA SRP FAQ 2026-10-15 and SRP/User Manual v1.3 operations, including deadline counters limitations.
- Next P0: obtain official LS Mecapion model manuals as original PDF bytes, compute SHA-256, review page-by-page, record exact revision and locators; source download endpoints currently fail from available retrieval route.
- Next P1: audit M/606 41 standards individually (draft/vote/adoption status), search OJ for actual CRA harmonised-standard citations, and track C/2026/1695 Action 5 follow-up.
- Exact-main push CI is not independently confirmed; do not mark as passed.


## 2026-11-19 — LS메카피온 제품군·DriveCM·ESI 매핑
- PR #112 merged: 4507bc5dc2a8c189073ab0728a2b271063c4bf5c; exact-head Run #1020 success, 174 passed / 0 failed; live 10-source HTML and manifest round-trip passed; PDF canary skipped.
- Manufacturer public product list reviewed for 13 drive families, voltage/power ranges and communication type.
- DriveCM Ver1.03.2 (2026-07-07 post; file date 2026-08-11) support list: L7P, L7NH, L7NHF, PEGA, PHOX, iX7NH, L7C, iX7M, PEGA2; L7S/L7N discontinued and use LIVE i.C.E. Do not assume near-identical model names are equivalent.
- EtherCAT ESI Ver0.98 (2025-07-15) public applicability list: L7NH, Pegasus, PHOX, L7NHF, L7N, GEM, SMT, L7MMT, iX7NH, iX7M, iX7MD.
- iX700M is absent from public ESI v0.98 list; current DriveCM post does not list iX700M, L7NHA/B, L7SA/B, GEM. Absence from these lists is a gap requiring manufacturer confirmation, not proof of unsupported status.
- Firmware update functionality is mentioned in DriveCM release history; actual signature/integrity/authentication/rollback/recovery controls remain unverified.
- Report v0.8 includes a family-level interface/tool/ESI/update matrix. Product-specific conformity remains Unknown and tests Not Run.
- Next P0: obtain official PDF manuals, DriveCM installer/release note and ESI XML bytes, hash and inspect; validate actual model/variant support with manufacturer.


## 2026-11-19 — ESO M/606 개발단계 및 OT/IACS 지원표준 조사
- PR #113 merged: 5273e6da25862a8ad1e92b2473a11a63b0d8015f; exact-head Run #1022 success, 174 passed / 0 failed; live 10-source HTML and manifest round-trip passed; PDF canary skipped.
- STAN4CR/CEN-CENELEC/ETSI joint M/606 progress report V2.0 dated 2026-06-03 reviewed (4 pages).
- Report contains per-item ESO status and historical publication forecasts for M/606 entries, plus complementary OT/IACS deliverables based on EN IEC 62443-4-1/-4-2/-3-3.
- Treat 2026-06-03 status/forecasts as historical snapshot, not current state; M/606 delivery dates follow C(2026) 7861 Annex I (2026-11-10).
- IEC 62443 supporting deliverables are not automatically M/606 Annex I harmonised standards or CRA Article 27 OJ citations.
- Report v0.9 maps relevant work to servo-drive product and industrial system boundaries.
- Next: update status after June snapshot using ESO live work programme / new progress reports, verify final publications and OJ citations; acquire manufacturer original PDF/ESI/installer bytes.


## 2026-11-19 — PR #114 M/606/OT 표준화 검토 반영 및 다음 우선순위
- PR #114 merged: 88a3c3b29ecf7af2884e6df288075a0ce48f73f2; exact-head Run #1024 success, 174 passed / 0 failed; 10-source HTML canary and manifest round-trip passed; PDF canary skipped.
- Report v0.9 includes 2026-06-03 ESO joint M/606 progress snapshot and complementary IEC 62443 OT/IACS deliverables.
- Next P0: obtain 2026-11-19 current status of each M/606 work item, final publications and OJ harmonised-standard citations. The June report is only historical stage evidence.
- Next P0: obtain official LS Mecapion manuals, DriveCM release notes/installer and ESI XML original bytes, hash and inspect. Current official download route remains blocked in the available runtime.
- Next P1: model-specific product boundary, EU supply chain, exact SKU/HW/FW revision, firmware update security controls, SBOM and product-level CRA applicability.
- Exact-main push CI remains unconfirmed; do not claim success.


## 2026-11-20 진행상태 갱신
- 완료: PR #126 문서 동기화 병합 및 정확한 head CI Run #1052 성공. main SHA `9b61f1d9b177454c3530fa5339883e6434d01df3`.
- 완료: EN 40000-1-1/-1-2 발행 공식 공지 확인, OJ 게시와 Article 27 presumption의 구분을 보고서에 명시.
- P1 계속: CEN 개별 카탈로그 citation 필드 직접 확인 및 OJ/EUR-Lex CRA 참조 대조. 2차 tracker의 "No citation expected" 주장은 잠정으로 유지.
- P1 계속: M/606 Annex I 41개 항목 전수감사. 각 항목에서 개발단계와 OJ citation을 분리하고 근거·날짜·상태를 기록.

- 완료(2026-11-20): CEN catalogue primary citation field direct verification for EN 40000-1-1 (JT013095) and EN 40000-1-2 (JT013089); both explicitly “No citation expected for Directive 2024/2847”. Keep Article 27 presumption unavailable from these two standards.
- P1 remains: M/606 Annex I 41-item standard-by-standard audit, including each item's actual candidate standards and OJ reference state.

- 완료: M/606 replacement Annex I 41개 항목의 항목번호·주제·ESO 채택기한 41/41 대조.
- P1: 41개 M/606 topic → 실제 CEN/CENELEC/ETSI work item 및 EN/ETSI reference 매핑. OJ citation/Article 27 상태는 개별 실제 표준 단위로 확인.
- P1: C(2026) 7861 Article 2에 따른 CEN/CENELEC/ETSI 수락/거부 통지 원본 확인(통지 후 1개월 조건).
- 기한 요약: items 1,15 2026-11-30; items 2–14 2027-10-30; items 16–41 2027-01-31. ESO adoption deadlines, not manufacturer CRA deadlines.


## 2026-11-20 실행상태 동기화 — PR #128
1. 완료: C(2026) 7861 replacement Annex I의 M/606 41개 항목 주제·ESO 채택기한 41/41 1차 출처 대조 및 감사대장 반영.
2. 완료: PR #128 exact-head Run #1060 성공 후 squash merge; main SHA `6733f37201117cb5744215d9deb337b0810acc49`; 사전·사후 복구 브랜치 생성.
3. 완료: main push CI Run #1061 success. PR #129의 상황판 동기화 후 main push CI Run #1063도 success.
4. 다음 P0: (a) CEN JT013090/prEN 40000-1-3의 공식 카탈로그 상태 및 OJ citation 필드 직접 확인, (b) C(2026) 7861 Article 2에 따른 ESO 1개월 비수락 통지 유무를 Commission/CEN/CENELEC/ETSI 1차 자료로 확인.
5. 범위 주의: 41개 항목의 Annex I 대조는 완료했으나 41개 개별 표준번호 매핑·OJ 인용상태 전수감사는 미완료. 제조사 제품별 CRA scope/classification/RDPS Unknown, 보안시험 Not Run.


## 2026-11-20 후속 1차 출처 조사 — Work Item 매핑 및 Article 2

1. 완료: CEN/CENELEC 공식 M/606 Work Programme에서 item 1 → JT013089, items 2–14 → JT013091, item 15 → JT013090 연결 확인.
2. 완료: CEN 공식 webinar에서 JT013090 ↔ prEN 40000-1-3 Vulnerability Handling 연결 확인. CEN 2026-11-19 발표에서 FprEN 40000-1-3 publication forthcoming 확인.
3. 미완료: JT013090 공식 개별 카탈로그의 현재 단계·공식 투표 일정·OJ citation 필드 직접 확인. Formal Vote 19 Nov 및 citation expected는 2차 자료에만 있어 검증된 사실로 승격 금지.
4. 미완료: C(2026) 7861 Article 2에 따른 ESO별 실제 수령일과 1개월 내 비수락 통지 원본. 발송일을 수령일로 간주하지 않는다.
5. 후속: ESO별 수령/통지 확인, JT013090 CEN record/OJ 필드, 41개 개별 EN/ETSI mapping/OJ audit.
6. 제품 CRA scope/classification/Annex III·IV/RDPS는 증거 전까지 Unknown, security tests Not Run.


## 2026-11-20 PR #130 사후 검증 및 다음 분석
- 완료: PR #130 exact-head Run #1064 success, squash merge SHA `bfcc2e61fc07b2148fca7a162349af40aa84bc47`, pre/post safety refs 생성, main read-back 확인.
- 완료: main push Run #1065 (`44658780153`) success; full tests, traceability, official source canaries, provenance manifest upload 통과.
- 다음 P0: M/606 Work Programme의 산업용 OT/IACS Work Items 20b/21b/22b/25b/27b/36b가 실제로 어떤 제품기능에 한정되는지와 LS메카피온 서보드라이브의 증거상 인터페이스/기능을 비교. 기능이 입증되지 않으면 적용대상이라고 추정하지 않는다.
- 제품별 CRA scope/classification/Annex III·IV/RDPS는 Unknown 유지; 보안시험 Not Run.
