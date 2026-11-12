# CRA 서보 드라이브 개발 — 마스터 계획서

살아 있는 계획서. 상태는 GitHub 증거로 갱신한다. 문서·폴더 구조·스키마·코드 모두 개선 가능하며 변경 이유와 영향은 세션 로그에 기록한다.

## 목표
CRA 입문부터 서보 드라이브 설계·구현·시험·취약점 관리까지 연결하는 실무 보고서와 추적성 매트릭스 구축. ST MCU 우선, TI 비교.

## P0 — GitHub 운영/연속성
- [x] START_HERE.md 생성
- [x] AI_RULEBOOK에 매 세션 필수 읽기/검증 절차 반영
- [x] 성공·실패·오류·재발 방지 규칙 반영
- [x] 브랜치별 파일/이력 정합성 확인
- [x] main 전용 6개 자료 표본 감사
- [ ] 문서 상충 자동 점검과 운영 절차 테스트

## P1 — 브랜치/자료 정합성
- [x] main/작업 브랜치 archive 및 history 정합성 확인(990/990)
- [x] main에서 확인한 6개 추가 파일을 작업 브랜치에 콘텐츠 단위로 보존
- [x] archive/history 검사 스크립트 추가
- [x] 검사 스크립트 단위 테스트 3개 로컬 통과
- [x] 작업 브랜치 push/수동 실행용 GitHub Actions 검사 워크플로 추가
- [x] GitHub Actions 실제 실행 결과 확인: 최근 4회 audit workflow success
- [ ] inventory 결과에 기준 브랜치/commit SHA/확인시각 저장
- [ ] PR/병합 전 commit graph와 diff 검토

## P2 — 자동화 신뢰성
- [x] main.py 및 Gemini 프롬프트의 변경 위험 분석 (수정 없음)
- [x] main.py 제어흐름/예외/출력 변경 제안서 작성 및 사용자 승인 확보 (쿼터 정책 변경은 제외)
- [x] 모델 실패/빈 응답/invalid JSON/필수 필드 오류를 성공 처리하지 않도록 수정 (작업 브랜치)
- [x] 근거 메타데이터 후보 필드를 포함한 JSON schema/필수 필드 검증 적용 (원문 검증 전 후보 상태)
- [ ] 원문 인용/링크/의미 검증을 구분
- [x] 미검증 생성물을 UNVERIFIED 초안으로 렌더링하고 법령/제품 적용성 VERIFIED 승격 차단
- [ ] Discord timeout/HTTP status/재시도/중복 방지
- [ ] 무료 한도 fail-closed 및 유료 호출 금지
- [x] mock 실패 경로 테스트 fixture 13개 추가 (격리 런타임 17/17 PASS; CI 결과 별도 확인 대기)

## P3 — CRA 근거 검증
- [ ] Regulation (EU) 2024/2847 및 개정 이력 재확인
- [ ] EU Commission/ENISA/표준기관 공식 자료 최신성 확인
- [ ] 적용 범위·예외·분류·일정·의무를 조항 단위로 연결
- [x] 기존 990개 자료의 기초 인벤토리/키워드 후보 생성 (법적 검증 아님)
- [x] 기존 990개 자료에서 주장·Article/Annex/URL/인용 후보 전수 추출 (4,400 claim blocks; 1,224 Article strings)
- [x] 출처 URL 후보 0개 원인을 대표 원본 6개에서 확인하고 출처 누락 감사 문서 작성
- [ ] 기존 990개 자료의 법령/표준/제조사 공식 출처 URL 복원 및 원문 연결
- [x] 초기 5개 파일 수동 표본 감사: 4 CONFLICT, 1 PARTIALLY_VERIFIED
- [x] 추출기 schema 1.1: 주장/인용/위험 후보 행 번호와 문맥 스니펫 추가, CI success
- [x] 위험 주제 표본검사로 실제 오류/정상 주장 분리 (추가 20개: 14 CONFLICT / 6 PARTIALLY_VERIFIED)
- [x] 34개 고유 표본의 원본 SHA-1·행 위치·주장 요약·정정 근거·판정 상태를 별도 정정 대장으로 연결 (25 CONFLICT, 9 PARTIALLY_VERIFIED; 비무작위 표본)
- [x] 34개 표본의 법령 인용 블록을 EUR-Lex 원문과 대조하고 quote claim별 판정 기록
- [ ] 990개 전체 위험 후보의 원본 근거 연결 및 추가 표본 검증

## P4 — 제품/반도체 적용
- [x] 제품 경계/의도된 용도/인터페이스/원격 기능/업데이트 경로 확인 템플릿 작성
- [ ] 실제 제품 사실 입력 및 제품별 CRA 적용성 판단
- [ ] CRA 적용성 및 분류 판단표 작성 (Article 7 + Implementing Regulation 2025/2392 core-functionality 기준 반영)
- [ ] 위협 모델 및 HW/FW/통신/운영 요구사항 분해
- [x] ST AN5156 Rev 14 (June 2026) 및 STM32Trust 공식 기준선 확보
- [x] TI MSPM0G3529-Q1 데이터시트 및 SLAAE29A 보안 기능 문서 확보 (참고 기준 예시, 동급 비교 아님)
- [ ] ST MCU 정확한 부품 번호와 문서 리비전 확인
- [x] 제조사 보안 자료 source register 및 기능별 ST/TI 비교표 작성 (ST AN5156 Rev14, TI MSPM0G3529-Q1 SLASFO2B RevB)
- [x] 제조사 기술 주장 ledger 초기화 및 원문 위치 연결
- [ ] TI SLAAE29 RevB (2026-08) 본문 및 최신 G-Series TRM RevF 상세 대조
- [ ] Secure Boot, 디버그 잠금, 키 저장, 암호, 난수, 업데이트 기능의 실제 구현/시험 검증
- [ ] TI 동급 제품 비교

## P5 — 통합 보고서
- [ ] CRA 입문/용어집/적용 범위
- [ ] 요구사항-설계-구현-시험-증거 매핑
- [ ] 서보 드라이브 보안 아키텍처
- [ ] ST 구현 가이드 및 TI 비교
- [ ] SBOM/취약점 대응/지원기간/신고 의무
- [ ] 시험계획·추적성 매트릭스·증거 목록
- [ ] 출처/원문 부록 및 미해결 쟁점

## P6 — 배포/유지관리
- [ ] Markdown 보고서 검토
- [ ] DOCX/PDF 출력 자동화
- [ ] 무료 운영 한도 검증
- [ ] 세션 로그/상황판/계획 갱신 자동화
- [ ] 공식 자료 변경 감시(무료·승인 범위 내)

## 완료 기준
핵심 요구사항에 ID, 공식 조항, 원문 위치, 해석/한계, 적용성 근거, 개발 조치, 시험 방법/기준, 증거, 검증 상태, 확인일이 있어야 한다. 미확인 항목은 완료 처리하지 않는다.

## 변경 이력
- 2026-11-12: 기본 계획 및 세션 연속성 규칙 수립.
- 2026-11-12: main/작업 브랜치 archive 동기화 및 표본 감사.
- 2026-11-12: archive/history 무결성 검사 스크립트, 테스트, GitHub Actions 워크플로 추가.


## 2026-11-12 추가 진행 — 고위험 아카이브 20개 감사
- [x] 2026-11-11~2026-11-12 생성물 중 지원기간/업데이트/분류/적합성 평가/SBOM/신고 관련 20개를 공식 EUR-Lex 원문과 대조.
- 결과: 14 CONFLICT, 6 PARTIALLY_VERIFIED. 무작위 표본이 아니므로 전체 오류율 추정 불가.
- 상세: [ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md).
- 원본 archive는 수정하지 않음. main.py/Gemini prompt/운영 workflow 미수정.


## 2026-11-12 제조사 보안 자료 및 주장 대장
- [x] ST/TI 공식 자료 레지스터 및 기능별 비교: [MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md).
- [x] 출처·문서 버전·원문 위치·주장 유형·상태를 연결하는 [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md) 생성. 제조사 주장 15건 등록(VERIFIED 13 / PARTIALLY_VERIFIED 1 / UNVERIFIED 1).
- [ ] TI SLAAE29 최신 revision 공식 본문 확보 및 Rev A와 차이 검토. 현재 Rev A SLAAE29A 분석만 본문 확인된 상태.
- [x] TI G-Series TRM Rev F(2026-11-05) 공식 인덱스 메타데이터 및 문헌번호 SLAU846 확인. PDF/HTML 본문 열람 실패로 보안 장 내용 검증은 미완료.
- [ ] 실제 ST MCU part number 확보 전 ST 기능 비교는 제품군 수준으로만 유지.


## 2026-11-12 추가 진행 — 하드웨어 설계 참조 초안
- [x] 서보 드라이브 CRA 보안 하드웨어 참조 아키텍처 초안 작성 (제품별 설계 확정 아님)
- [x] 외부 네트워크/서비스/업데이트/디버그/제조 프로비저닝 trust boundary 정의
- [x] Secure Boot/update negative test 및 power-cut/recovery test 후보 10개 작성
- [x] CRA 요구사항-설계 작업-객관적 증거 매핑 초안 작성
- [ ] 실제 ST MCU 주문 코드 확보 후 part-specific 기능/제약/errata 검증
- [ ] TI G-Series TRM Rev F 본문 보안 장 열람 및 MSPM0G3529-Q1 적용성 확인
- [ ] TI SLAAE29 최신 revision 원문 확보 및 Rev A와 diff 검토
- [ ] 제품 회로도/통신 인터페이스/업데이트 경로/서비스 포트 사실 반영


## 2026-11-12 추가 진행 — 법령 인용문 단위 감사
- [x] 기존 34개 고유 표본의 법령 인용 블록을 EUR-Lex 원문과 대조하고 원본 행 위치·정정 조항을 기록: [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md).
- [ ] 인용 정정 규칙을 반영한 별도 정정본/통합 보고서 개정. 원본 archive는 불변으로 유지.
- [ ] 나머지 956개 파일 및 4,400 claim blocks의 위험 기반 추가 검증.
- [ ] 표준·제조사 문서에서 인용한 문구는 각 해당 1차 원문을 별도로 확보해 검증.


## 검증 품질·효율 게이트
- [x] 근거 등급, claim 상태, 별도 재검증, 반증 확인, 제품 적용성, 설계/시험 연결 기준을 [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md)에 문서화.
- [ ] 기존 34개 인용 표본을 Pass A/B/C 이력 기준으로 보완 검증. 기존 감사 결과를 자동으로 VERIFIED로 간주하지 않는다.
- [ ] 법령 요구사항을 HW/FW/시험/증거 추적성 매트릭스로 전환.
- [ ] 제품 경계 필수 입력과 ST MCU 정확한 주문 코드를 확보해 제품별 적용성 검증.
- [ ] P0 위험 후보부터 나머지 archive를 단계별 검증하고, 각 배치에서 표본 범위·해시·반증 결과를 기록.


## Pass B/C 재검증 진행 현황
- [x] EUR-Lex 현행 원문을 다시 열어 재검증 기준 구간(Article 13, 14, Annex I Part I/II) 확인.
- [x] A-001–A-008 Pass B/C 배치 01 작성: [ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md).
- [ ] A-009–A-020 Pass B/C 배치 02 수행.
- [ ] B-001–B-020 Pass B/C 배치 03/04 수행.
- [ ] 각 배치 완료 후 원본별 인용 상태와 통합 보고서 문구를 동기화.


## Pass B/C 재검증 진행 현황
- [x] Batch 01 A-001–A-008 (8개 파일): [상세](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)
- [x] Batch 02 A-009–A-015 및 B-001–B-002 (8개 파일): [상세](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md)
- [ ] B-003–B-010 Pass B/C 배치 03 수행.
- [ ] B-011–B-020 Pass B/C 배치 04 수행.
- [ ] 각 배치 완료 후 인용 상태와 통합 보고서 문구 동기화.


## Pass B/C 재검증 진행 현황
- [x] Batch 01 A-001–A-008 (8개): [상세](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)
- [x] Batch 02 A-009–A-015 및 B-001–B-002 (8개): [상세](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md)
- [x] Batch 03 B-003–B-010 (8개): [상세](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md)
- [ ] Batch 04 B-011–B-020 (10개) Pass B/C 수행.
- [ ] 전체 34개 재검증 완료 후 최종 상태 집계와 정정본 동기화.


## Pass B/C 최종 재검증 — 34/34 완료
- [x] Batch 01 A-001–A-008
- [x] Batch 02 A-009–A-015(중복 A-013 제외), B-001–B-002
- [x] Batch 03 B-003–B-010
- [x] Batch 04 B-011–B-020
- [x] 최종 집계: VERIFIED 0 / PARTIALLY_VERIFIED 6 / REJECTED 28. [최종 요약](ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md)
- [x] HW/FW/시험/증거 추적성 매트릭스 작성: CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md.
- [ ] 나머지 956개 archive는 P0 위험 후보부터 단계별 검증. 34개 표본 결과를 전수 오류율로 일반화하지 않음.


## 설계/시험 추적성 매트릭스
- [x] 법령 요구사항을 HW/FW/시험/증거 구조로 변환한 초안 작성: [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md).
- [ ] 제품 경계 BD-01–BD-15 입력 확보 후 적용성 업데이트.
- [ ] 실제 ST MCU 주문 코드/실리콘 리비전 확인 후 부품별 기능과 시험 가능성 확정.
- [ ] 제품 위험평가/기능안전 검토를 반영해 각 시험의 수치형 합격 기준 승인.


## 위협 모델 및 시험·증거 구조
- [x] 일반 서보 드라이브 자산/공격자/신뢰 경계/위협 시나리오 초안 작성: [THREAT_MODEL_SERVO_DRIVE_CRA.md](THREAT_MODEL_SERVO_DRIVE_CRA.md).
- [x] 위협별 시험 ID, 기대 결과, 증거 파일/메타데이터, 시험 상태 규칙 작성: [SECURITY_TEST_EVIDENCE_REGISTER.md](SECURITY_TEST_EVIDENCE_REGISTER.md).
- [ ] 제품 SKU/실제 인터페이스/설치 토폴로지 입력으로 위협 모델 맞춤화 및 위험도 산정.
- [ ] 실제 ST MCU 주문 코드/실리콘 리비전으로 boot/debug/crypto/NVM 통제 가능성 확인.
- [ ] 제어주기/지터/부하/복구시간 등 수치형 합격 기준을 제품 요구사항·위험평가·기능안전 분석으로 승인.
- [ ] 승인된 시험환경에서 TST 케이스 실행, raw evidence hash 기록 및 별도 검토.


## 2026-11-12 통합 추적성 / 공식 가이드 검토
- [x] 통합 end-to-end 추적성 표 작성: [CRA_INTEGRATED_TRACEABILITY_MATRIX.md](CRA_INTEGRATED_TRACEABILITY_MATRIX.md), TR-01..TR-20.
- [x] CRA Commission guidance 공식 게시 메타데이터 기록: [CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md](CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md).
- [x] TI SLAAE29 Rev B / G-Series TRM Rev F 및 ST AN5156 Rev14의 공식 인덱스 메타데이터 재확인(본문 내용 검증과 구분).
- [ ] Commission C(2026) 5252 Annex PDF 원문을 확보해 페이지/문단별 Pass B/C 검증.
- [ ] TI SLAAE29 Rev B PDF/HTML 원문 확보 및 Rev A와 revision diff 검토.
- [ ] TI G-Series TRM Rev F(SLAU846) 본문 보안 관련 장 열람·부품별 적용성 확인.
- [ ] 제품 경계 BD-01..BD-15를 실제 제품 사실로 채움.
- [ ] ST MCU 전체 주문 코드/실리콘 revision 확보 후 part-specific security capability matrix 작성.
- [ ] 승인된 제품 위험/안전 요구로 수치형 합격 기준 확정 및 실제 DUT 시험 실행.

## 정기 공식 자료 점검
- 주간 자동화 등록: 매주 월요일 09:00 Asia/Seoul. 범위는 EUR-Lex/European Commission/ENISA 및 ST/TI 공식 보안 문서.
- 자동화는 자료 변경을 조사·요약하고 작업 브랜치 반영 후보를 제시한다. main.py/Gemini prompt/production workflow/main branch 변경 권한을 부여하지 않는다.

## 추가 검증 진행 — 2026-11-12

- [x] 통합 매트릭스 TR-01..20 / 위협 TH-01..18 / 자산 AST-01..10 / 시험 TST 45개 ID 중복·참조 정합성 검사. 모든 매트릭스 시험 참조가 시험 대장에 존재.
- [x] main-only 자동 생성 report #35의 CRA 법령 인용 감사 및 정정 기록. 원본 main 파일은 수정하지 않음.
- [x] TI SLAAE29 Rev B 공식 HTML 본문 및 revision history 확인.
- [ ] TI SLAAE29 Rev B의 지원 부품 목록과 MSPM0G3529-Q1 데이터시트/적용 TRM 사이의 part-specific 보안 기능 교차확인.
- [ ] TI G-Series TRM Rev F 보안 장/레지스터 상세 본문 확보. 현재 대용량 HTML 본문은 열람 실패.
- [ ] Commission C(2026) 5252 Annex PDF 페이지/문단별 검증. 공식 download endpoint는 Unicode decoding error.
- [ ] main branch의 신규 자동 생성 archive/history 차이 및 CRA 법령 오류를 계속 감사하되 main은 사용자 승인 없이 수정/병합하지 않음.

## main-only 자동 생성 보고서 후속 감사

- [x] main-only report #35 법령 인용 감사.
- [x] main-only report #36 법령 인용 감사: Article 14/Part II(8) 혼동, Annex I 항목 오기, Secure Boot/TPM 보편 의무 단정, 정식 법령 제목 오류 확인.
- [ ] 이후 main 자동 생성 자료는 새 commit을 확인한 뒤 위험 기반 감사 큐에 추가. main 변경/수정/병합은 별도 승인 전 금지.

## 자동 조사 파이프라인 개선 제안 업데이트

- [x] main-only report #35/#36에서 관찰된 허위/합성 인용과 조항 혼동을 변경 제안서의 실증 근거로 등록.
- [x] quote exact-match, legal location cross-check, legal metadata check, Article 13/14/Annex I Part II(8) 분리, Secure Boot/TPM 설계 권고와 법적 의무 구분을 회귀 테스트 요구사항에 추가.
- [ ] P0/P1/P2 변경은 사용자 승인 후에만 구현. 현재 main.py/Gemini prompt/production workflow 변경 없음.

## 하드웨어 아키텍처 조항 매핑 정정

- [x] CRA-HW-05 confidentiality/integrity의 조항 분리·정정: Part I(2)(e)/(f).
- [x] CRA-HW-06 availability/resilience 정정: Part I(2)(h),(i).
- [x] 데이터 최소화 Part I(2)(g)를 CRA-HW-11로 별도 추가.
- [x] TI SLAAE29B 문서 내용과 MSPM0G3529-Q1 part applicability 경고를 하드웨어 아키텍처에 반영.
- [ ] 수정된 아키텍처/요구사항 매트릭스 전체 조항을 EUR-Lex와 한 번 더 비교하고, 제품별 적용성은 실제 SKU/MCU 입력 후 확정.

## 하드웨어 블록 설계 선택 단계

- [x] 일반 참조 아키텍처에 DEC-01..DEC-10 설계 선택 매트릭스 추가.
- [x] G-01..G-06 설계 동결 입력 게이트 정의.
- [ ] 제품 SKU/BD-01..15 및 실제 ST MCU 전체 주문 코드 확보 후 DEC 선택과 part-specific capability matrix 완료.
- [ ] timing/jitter, communications, power/reset, gate-driver/safety boundary를 승인된 수치/회로 증거로 검증.

## main-only 보고서 #37–#39 감사

- [x] main-only 자동 생성 보고서 #37–#39를 EUR-Lex Article 13 및 Annex I 원문과 대조.
- [x] Article 13(8) 지원기간과 Annex I Part II(8) 무상 보안 업데이트 분리, Article 13(6) component vulnerability 처리와 혼동 방지.
- [x] Annex I Part II 번호(1)–(8)와 Part I(2)(b)/(c) 오인용을 감사 문서 및 claim ledger에 기록.
- [ ] main 자동 생성물 신규 commit 감시 및 위험기반 감사 계속. 브랜치 동기화/병합은 승인 없이 하지 않는다.

## 하드웨어 인터페이스 설계 계약

- [x] IF-01..IF-09의 신호 경계·설계 계약·검토 항목·시험 연결 작성.
- [x] 회로도 리뷰 체크리스트 10개 항목 추가.
- [ ] 실제 회로도, 커넥터/핀맵, PHY·센서·gate driver 부품번호, power tree, clock/reset, isolation/EMC 요구를 확보해 설계 검토.
- [ ] 승인된 motion control timing/jitter budget 및 fault response 기준으로 시험 수행.


## Main-only reports #40–#55 audit
- [x] main-only CRA reports #40–#55 source text reviewed from GitHub commits and compared with EUR-Lex Regulation (EU) 2024/2847.
- [x] Detailed audit report and 16 atomic claim rows added to the work branch.
- [x] Distinguish Article 13(8) support period, Article 14 reporting, Annex I Part II(7) secure distribution, Part II(8) free updates, Annex II 8(d) decommissioning.
- [ ] Continue with later main-branch reports after checking commit sequence and source content.
- [ ] Commission C(2026) 5252 Annex full paragraph-level review; official index/publication metadata is verified, full PDF extraction remains incomplete in this environment.
- [ ] TI G-Series TRM Rev F security chapter: official revision metadata verified (Nov 5 2026), but full body not yet verified; do not make feature/registration claims from revision metadata alone.


## TI TRM Rev F 재점검
- [x] TI 공식 MSPM0G3507 제품 페이지에서 TRM Rev F / 2026-11-05 게시 메타데이터 확인.
- [x] 동일 페이지에 공개된 MSPM0G3507 feature summary를 해당 제품 페이지 주장으로만 기록하고 G3529-Q1과 분리.
- [ ] Rev F PDF/HTML 전체 본문 확보 후 security/debug/boot/flash/NVM/register 내용을 실제 페이지·표 번호와 함께 검증.
- [ ] 최종 TI benchmark order code가 정해지면 datasheet, TRM family applicability, errata, SLAAE29B supported-device list를 삼중 대조.


## Main-only reports #56–#59 audit
- [x] main #56–#59 source text and commit diffs checked; main HEAD currently report #59.
- [x] EUR-Lex Article 14 reporting tracks, Annex I Part I security properties, Part II CVD/contact/free update clauses, Annex II contact details compared.
- [x] Four atomic claim rows and detailed audit report added.
- [ ] Continue auditing future main reports only after confirming new commits; no auto-sync/merge.
- [ ] Improve automated research quality gate proposal (exact quote, article/annex/part/point validation, obligation vs design-option classification) only after explicit approval.


## Main-only reports #60–#78 audit
- [x] main #60–#78 commit diffs fetched and compared with EUR-Lex Regulation (EU) 2024/2847.
- [x] Detailed audit report and 19 atomic claim rows added to the work branch.
- [x] Distinguish Article 13(8) support period, Article 14 reporting, Annex I Part II(5) CVD, Part II(6) vulnerability contact, Part II(7) secure distribution, Part II(8) free updates, Part I(2)(b)/(d)/(g)/(j) secure-by-default/access/data minimisation/attack surface.
- [ ] Continue auditing only after checking commits newer than #78; preserve main archive and require separate approval for any sync/merge.
- [ ] Add quote-level exact-match checks to the pending main.py/Gemini change proposal; do not implement without explicit user approval.


## Main-only report #79 follow-up
- [x] Report #79 commit diff fetched and compared with EUR-Lex Article 14.
- [x] File-level PARTIALLY_VERIFIED verdict and atomic claim CRA-ARCH-079-001 added.
- [ ] Continue with report #80+ after checking latest main commits; do not merge/sync without approval.


## TI MSPM0G3529-Q1 functional safety evidence
- [x] TI SFFS983A Rev A opened; exact MSPM0G3529-Q1 supported-device inclusion verified.
- [x] Component-level ASIL D systematic / ASIL B random-fault statements and integration assumptions recorded.
- [x] QM/non-safety-critical status of DEBUG/AES/TRNG/KEYSTORE etc. recorded to prevent misuse in safety-critical path.
- [ ] Retrieve exact G3529-Q1 FMEDA/safety analysis report and confirm failure rates, diagnostic coverage, hardware metrics and restrictions.
- [ ] Map TI manual's host/actuator-disable assumptions and safety mechanisms to IF-01..IF-09 and test/evidence register as a comparison example, not target-product selection.
- [ ] Acquire/read full G-Series TRM Rev F and exact G3529-Q1 register applicability; do not infer from index metadata.
- [ ] Do not convert ASIL D/ASIL B into IEC 61508 SIL 3 equivalence or certification claim.


## TI safety mechanism to servo-drive mapping
- [x] Created a separate SFFS983A-to-servo-drive integration matrix, mapping diagnostic mechanism families to IF-01..IF-09 and candidate validation evidence.
- [ ] Confirm exact G3529-Q1 applicability of every referenced IP/diagnostic in the full TRM/datasheet/errata.
- [ ] Retrieve FMEDA and establish system-level diagnostic coverage/metrics.
- [ ] Convert selected candidates into approved safety test procedures only after target safety requirements and DUT are defined; all current candidates remain NOT_RUN.


## Main-only report #80 follow-up
- [x] Report #80 commit diff fetched and compared with EUR-Lex Annex I Part I.
- [x] File-level PARTIALLY_VERIFIED verdict and atomic claim CRA-ARCH-080-001 added.
- [ ] Continue with report #81+ after checking latest main commits; no automatic branch sync or merge.


## 2026-11-12 추가 진행 — main-only reports #81–#121 감사
- [x] main #81–#121의 41개 archive commit diff에서 보고서 원문을 확인하고 EUR-Lex Regulation (EU) 2024/2847 Article 13–14, Annex I Part I/II, Annex II와 대조.
- [x] 감사 문서 [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md) 생성.
- [x] 파일 판정 33 CONFLICT / 8 PARTIALLY_VERIFIED / 0 VERIFIED. 41개 직접 인용 블록 모두 verbatim 재사용 금지.
- [ ] 41개 보고서에서 반복된 법령 정정사항을 원본과 구분한 별도 errata/정정본에 통합.
- [ ] #122 이후 신규 main archive 보고서는 commit 기준으로 대기열/감사 수행.
- [ ] P0: Article 13(8) 지원기간 shorter-than-five-years exception, Annex I Part II(8) 무상 업데이트 예외, Article 14 두 신고 트랙을 통합 보고서와 claim ledger에 재검증.
- [ ] #81–#121 이후 추가된 main 보고서가 있는지 다음 세션에서 HEAD 재확인. main 동기화/병합은 승인 없이 금지.


## 2026-11-12 추가 진행 — main-only report #122
- [x] main report #122 commit diff 확인 및 EUR-Lex Annex I Part I(2)(b),(d),(j), Part II(5), Annex II(2)와 대조.
- [x] [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md) 작성. 판정 CONFLICT.
- [ ] #123 이후 신규 보고서 commit 여부를 계속 확인하고 위험기반 감사.
- [ ] #81–#122 정정사항을 원본과 분리한 별도 errata로 통합.


## 2026-11-12 추가 진행 — main-only report #123
- [x] main #123 commit diff 검토 및 EUR-Lex Article 13(7),(17)–(19), Annex II(1)–(9)와 대조.
- [x] [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_123_2026-11-12.md) 작성. 판정 CONFLICT.
- [x] 올바른 사용자 문서 항목을 Annex II(1)–(9), 특히 (7), (8)(a)–(f), (9)로 정리.
- [ ] #123 감사 기준으로 서보 드라이브 CRA 사용자 보안정보/지침서 체크리스트를 원본과 별도 문서로 작성.
- [ ] 제품 핵심 기능·의도된 용도 확인 전 Important Product Class II 자동 단정 금지.
- [ ] 다음 세션에서 main HEAD를 재확인하고 #124 이후 보고서 감사.


## CRA 사용자 보안정보·지침서 산출물
- [x] #123 법령 매핑에 따라 [SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md](SERVO_DRIVE_CRA_USER_SECURITY_INFORMATION_CHECKLIST.md) 템플릿 작성.
- [ ] 실제 제품 SKU/경계/기능/인터페이스/저장 데이터/업데이트 방식/지원기간 입력값 확보.
- [ ] Annex II 각 항목의 증거 파일·버전·담당자·승인자·문서 위치를 채우고 상태를 검증.
- [ ] Annex III 기준에 따라 제품 분류를 별도 검토; servo drive라는 이유만으로 Class II 지정 금지.


## 2026-11-12 추가 진행 — main-only report #124
- [x] main #124 commit diff 검토 및 EUR-Lex Annex I Part I(2)(c), Part II(1)–(8), Article 13(17), Annex II(2)와 대조.
- [x] [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_124_2026-11-12.md) 작성. 판정 CONFLICT.
- [ ] #124에서 반복된 legal requirement vs risk-based design 구분을 Gemini 변경 제안서 acceptance criteria에 반영.
- [ ] 서보 드라이브 업데이트 경로·boot architecture·flash layout·recovery/safe-state 요구사항 확보 후 구현 후보를 제품별로 평가.
- [ ] 다음 세션에서 main HEAD 확인 후 #125 이후 보고서 감사.


## 2026-11-12 추가 — 파이프라인 변경안 구체화 (#125–#128 반영)

- [x] main reports #125–#128 commit diff 검토 및 반복 오류 유형을 정리: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_125_128_2026-11-12.md). 4개 모두 CONFLICT.
- [x] Gemini 명령문 v2 검토 초안 작성: [PROPOSED_GEMINI_PROMPT_V2.md](PROPOSED_GEMINI_PROMPT_V2.md). 운영 prompt에는 미적용.
- [x] [CHANGE_PROPOSAL_MAIN_GEMINI.md](CHANGE_PROPOSAL_MAIN_GEMINI.md)에 #125–#128 증거, 구체 변경 범위, diff 예시, 테스트/롤백/승인 경계 추가.
- [ ] 사용자 최종 승인 후에만 운영 prompt 파일, main.py JSON parsing/schema validation, fail-closed path 및 mock fixture tests 구현.
- [ ] 구현 후 mock 기반 회귀 테스트 및 GitHub Actions 결과를 직접 확인. 실제 API/유료 호출은 별도 승인 없이 수행하지 않는다.
- [ ] main branch, main.py 운영본, .github/workflows/run.yml, archive/history/state는 별도 승인 전 변경/동기화하지 않는다.



## 2026-11-12 승인된 CRA 조사 파이프라인 1차 구현
- [x] 운영 prompt를 `prompts/CRA_RESEARCH_PROMPT_V2.txt`로 분리하고 원문 미제공 시 직접 인용을 금지.
- [x] `cra_report_contract.py`에 structured JSON schema, strict validator, UNVERIFIED Markdown renderer, 제한된 모델 폴백/fail-closed 예외 구현.
- [x] `main.py`를 validator와 연결. 전체 모델 실패/빈 응답/invalid JSON/필수 필드 오류 시 non-zero 종료로 Discord/archive/state/history 성공 경로 차단.
- [x] mock 회귀 테스트 13개 추가 및 격리 런타임에서 17/17 PASS, py_compile 3/3 통과.
- [ ] GitHub Actions 실제 실행 결과 확인 및 google-genai SDK/모델 structured-output 호환성 검증(실 API 호출 승인 전까지 미실시).
- [ ] 원문 수집/URL·인용·조항·법률 해석 자동 검증 모듈은 별도 설계 및 승인 후 진행.
- [ ] quota 정책, 모델 선택/순서, Discord HTTP 오류 처리, recent_snippets 문맥 개선은 이번 범위에서 제외.
- [ ] main branch 반영/merge/rebase/sync는 별도 승인 전 금지.

## 2026-11-13 — 1차 구현 CI 실증 및 Source Evidence Pipeline 설계
- [x] 최신 작업 브랜치 GitHub Actions run #43205954271에서 전체 26 tests PASS (CRA contract 17 포함).
- [x] archive/history strict audit PASS: 990/990, missing/orphan/duplicate 0.
- [x] Google 공식 SDK의 JSON Schema structured output 문서 및 현재 모델 카탈로그 확인. 실제 API 호출/모델 접근 검증은 하지 않음.
- [x] 다음 단계의 source evidence pipeline 설계 문서 작성: `docs/PROPOSED_SOURCE_EVIDENCE_PIPELINE_V1.md`.
- [ ] source registry/fetcher/metadata/hash 구현 — 별도 승인 필요.
- [ ] EUR-Lex clause locator 및 ST/TI official document extraction adapter — 별도 승인 필요.
- [ ] schema v3, evidence bundle, exact quote/locator validator — 별도 승인 필요.
- [ ] SDK-only smoke test/workflow/dependency changes — diff 제시 및 별도 승인 필요.
- [ ] 실제 Gemini API/실제 외부 fetch는 별도 승인 전 금지.


## Source Evidence Pipeline — Phase A (2026-11-13)
- [x] 사용자 승인 후 작업 브랜치에 고정 공식 source registry 및 source_id-only fetcher 추가 (`source_evidence.py`).
- [x] HTTPS/host/DNS public-IP/redirect/timeout/MIME/status/response-size 제한 및 SHA-256 provenance metadata 구현.
- [x] mock-only 테스트 추가 (`tests/test_source_evidence.py`). CI 검증은 별도 결과로 확정한다.
- [ ] 최신 branch HEAD의 GitHub Actions 전체 unittest + strict archive audit 결과 확인.
- [ ] Phase A 구현 파일 재열람 및 diff/경계 검토.
- [ ] Phase B HTML/XML/PDF extraction 및 법령 locator 설계/승인.
- [ ] Phase C evidence bundle/schema v3/prompt v3 설계/승인.
- [ ] Phase D exact quote/source ID/locator validator 설계/승인.
- [ ] Phase E 실제 공식 URL read-only fetch는 별도 승인 전 수행 금지.
- 보호 경계: `main.py`, Gemini prompt, 운영 workflow, model order/quota, archive/history/state, `main` branch 변경 및 merge/rebase/sync 금지.
