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
- [x] Phase A HEAD `21efe17ac151dcdb630abeed20769e4224ec3356` Actions #43330278366: 45 tests PASS; strict archive audit 990/990 consistent.
- [ ] Phase A 구현 파일 재열람 및 diff/경계 검토.
- [ ] Phase B HTML/XML/PDF extraction 및 법령 locator 설계/승인.
- [ ] Phase C evidence bundle/schema v3/prompt v3 설계/승인.
- [ ] Phase D exact quote/source ID/locator validator 설계/승인.
- [ ] Phase E 실제 공식 URL read-only fetch는 별도 승인 전 수행 금지.
- 보호 경계: `main.py`, Gemini prompt, 운영 workflow, model order/quota, archive/history/state, `main` branch 변경 및 merge/rebase/sync 금지.

- [ ] 운영/live fetch 전 DNS TOCTOU 대응(IP-pinned transport 또는 egress enforcement) 설계 및 별도 검토.


## Source Evidence Pipeline — Phase B (2026-11-13)
- [x] 별도 parser module `source_extraction.py` 추가 (HTML text/title, EUR-Lex XML structure, HTML locator candidates, PDF page text adapter).
- [x] source_id registry binding, DTD/entity block, input/text/page limits, raw/text SHA-256 추가.
- [x] mock fixture tests `tests/test_source_extraction.py` 추가.
- [x] Phase B HEAD `14666beefec6441df0a169aec81fa5c93d04fc22` Actions #43331128802: 55 tests PASS; strict archive audit 990/990 consistent.
- [ ] live EUR-Lex XML/HTML fixture와 실제 ST/TI PDF의 parser fidelity 검증은 Phase E 별도 승인 후 진행.
- [ ] OCR/scanned PDF 지원 필요성 판단; 현재 미지원.
- [ ] Phase C evidence bundle/schema v3/prompt v3는 별도 승인 전 금지.

- [x] `main.py`, production prompt/contract, production run workflow 미변경 및 production import 부재 확인.


## 2026-11-13 — 신규 main archive 166개 대기열 등록
- [x] 기존 기준점 #128 / commit `15ceea4b9477b8c0928352a5b4228c0508e88daa` 이후 main commit history와 compare 결과 확인.
- [x] reports #129–#288 및 #1–#6 총 166개, archive 파일 166개, history/state 변경 2개를 확인하고 commit SHA/path/time/topic을 매핑.
- [x] [CRA_ARCHIVE_AUDIT_QUEUE.md](CRA_ARCHIVE_AUDIT_QUEUE.md) 신규 생성 및 166개 항목 중복 없는지 재조회 검증.
- [x] EUR-Lex 현행 본문, Commission C(2026) 5252 게시 페이지, ENISA SRP/FAQ의 법령 기준선·공식 운영정보 사전 확인.
- [ ] P0 항목부터 Pass A/B/C 개별 감사. 모든 신규 항목의 파일 판정은 현재 UNVERIFIED, Raw Text Quote/개별 주장 판정은 NOT_YET_AUDITED.
- [ ] P3 warning-only 23개에 대해 모델 호출 실패가 성공 archive로 처리되는지 운영 실패 경로 대조.
- [ ] 다음 실행에서 main HEAD 이후 신규 보고서만 대기열에 추가하고 SHA/path 기준으로 중복 제거.
- 보호 경계 유지: main.py, Gemini prompt, 운영 자동화 코드, .github/workflows/run.yml, main branch 변경 금지; merge/rebase/sync 금지.


## 2026-11-13 — Phase C implementation plan
- [x] Phase C design and implementation explicitly approved by user.
- [x] Add in-memory provenance-bound Evidence Bundle builder with strict source/raw/extraction hash checks and bounded excerpts.
- [x] Add isolated CRA report v3 validator/renderer, JSON Schema v3 and Gemini Prompt v3.
- [x] Add bundle/contract mock regression tests.
- [x] Confirm exact code commit `6344b576db64438e9a2ebfe5acdcc74afeac479e` GitHub Actions run #43338094337: 79 tests PASS; strict archive audit 990/990, consistent=true.
- [x] Re-read final Phase C diff and confirm `main.py`, production workflow, v2 prompt and v2 contract unchanged.
- [x] Record exact verified CI commit/run and update Phase C completion status.
- [ ] Phase D exact quote/context validator and human review design remains separate; not started.


### 2026-11-13 최종 무결성 및 감사 대기열 상태
- [x] 대기열 166개 재조회 및 중복/필수 필드 검사 완료. 우선순위 P0 111 / P1 32 / P2 0 / P3 23.
- [ ] 모든 항목은 아직 NEW / NOT_YET_AUDITED; 파일 판정 UNVERIFIED, Raw Text Quote/개별 주장 판정 NOT_YET_AUDITED. P0부터 Pass A/B/C 수행.
- [ ] P3 warning-only 23개가 모델 실패를 성공 archive로 처리하는지 운영 경로 감사.
- Final main HEAD #6: `173c4d29ee62c0e96cfadf93824d6807ef2d148a`; work HEAD `b3ff22437c8cac7124fa94e9bdda0bc52ae5563a`; work 510 ahead / 297 behind main. merge/rebase/sync 없음.
- Work branch에 별도 Phase C v3 관련 동시 커밋 10개가 관찰됨. 본 일일 감사는 해당 구현을 수정/검토/승인하지 않았으며 production 통합 전 별도 diff·승인·테스트 확인이 필요하다.


## 2026-11-13 — Report #7 added
- [x] Rechecked main HEAD `bd50257a80c0524402c70a7da420043ecfa0f490` and archive `research_archive/2026-11-13_003055.md`; history/state show daily count 7.
- [x] Added report #7 to the queue; verified 167 distinct items. Priority distribution P0 111 / P1 33 / P2 0 / P3 23.
- [ ] Complete Pass A/B/C for #7: Annex I Part I(2)(b) exact wording/exception/reset phrase; Article 13(1) vs 13(2); forced password change, debug-port disablement and factory-reset patch/key retention as risk-based design vs explicit mandate.


### Phase C final verification result — 2026-11-13
- Exact tested code commit: `6344b576db64438e9a2ebfe5acdcc74afeac479e`; GitHub Actions #43338094337 SUCCESS.
- 79/79 unit tests passed. Strict archive audit: archive/history 990/990; missing/orphan/duplicate/malformed = 0; consistent=true.
- Protected work-branch files unchanged: main.py `997952702fdd9d2472468b82e6efdd65b2bb4376`; run.yml `65a8cadc8eac593f551e390698e367b1d161ecf1`; v2 prompt `14e9ce8618bc447a371dc28fc725cda3636470c5`; v2 contract `e0c1f1db353f664ae8c817c2f335d3a6efef4076`.
- Phase C implementation and mock/fixture regression validation complete. No live source fetch, Gemini API invocation, production integration or protected branch sync.


## Phase D — exact quote / locator validation design (2026-11-13)
- [x] Read Phase B extraction structures, Phase C bundle/contract and verification protocol.
- [x] Prepare design-only proposal: deterministic bundle rebuild, locator provenance classes, bounded context packet, human review records and fail-closed statuses.
- [ ] User review/approval of Phase D implementation scope.
- [ ] Implementation not started. No changes to v2, `main.py`, production workflow, Phase C schema or runtime.


## Phase D — exact quote / locator validation implementation (2026-11-13)
- [x] User explicitly approved the isolated Phase D implementation scope.
- [x] Added `evidence_quote_validator.py`: canonical bundle rebuild, provenance/content comparison, locator candidate classification, repeated-position ambiguity handling, bounded context, claim-to-evidence reference checks.
- [x] Added human-review packet and mandatory reviewer-record fields; candidate acceptance requires explicit quote/locator/context/claim-support passes and completed countercheck.
- [x] Added adversarial tests for exact match, raw/extraction/bundle tampering, repeated excerpt/locator ambiguity, missing source/PDF backend, context bounds, claim references and human-review completeness.
- [x] First full test suite and strict archive audit: Actions #43345148925 SUCCESS, 103 tests PASS; archive/history 990/990, consistent=true.
- [x] Final hardened HEAD `eaf4b4d31c0dccd2a624ab0f67fabdc166936a70` Actions #43345315133 SUCCESS: 105 tests PASS; strict archive audit 990/990 consistent; protected files and Phase C schema/code SHAs unchanged.
- Boundaries unchanged: no `main.py`, production workflow, v2 prompt/contract, Phase C schema/IDs, live fetch, Gemini API, or main-branch changes; no merge/rebase/sync.


## Phase E — controlled official-source fetch and extraction quality (2026-11-13)
- [x] Phase E design proposal 작성: `docs/PHASE_E_CONTROLLED_FETCH_AND_EXTRACTION_DESIGN.md`.
- [x] Phase A fetcher의 DNS 사전검사와 실제 requests 연결 간 DNS TOCTOU 잔여 위험을 원문 코드로 확인.
- [x] Phase B real-document parser fidelity 미검증 및 PDF fake-reader-only/optional backend 상태 재확인.
- [ ] E1: source_id registry를 유지하면서 실제 TCP 연결을 검증된 A/AAAA IP로 고정하고 TLS SNI/hostname 검증을 원래 hostname으로 보존하는 transport 구현 — 사용자 별도 승인 대기.
- [ ] E2: DNS rebinding, IPv4/IPv6, TLS, redirect/retry, timeout/size/MIME/status adversarial tests 및 전체 CI — E1/E2 구현 승인 대기.
- [ ] E3: 실제 EUR-Lex/ST/TI fetch 및 HTML/XML/PDF 추출 품질 검증 — E1/E2 구현·CI 확인 후 별도 사용자 승인 필요.
- [x] Phase E 설계 단계에서는 코드, workflow, 운영 설정, live URL fetch, Gemini API 및 비용 설정을 변경하지 않음.
- 승인 요청 범위는 E1+E2 작업 브랜치 전용 구현/오프라인 테스트만. E3, production integration, protected files, main merge/rebase/sync는 포함하지 않음.


## 2026-11-13 — main-only reports #8–#12 audit
- [x] Reports #8–#12 original archive files, commit SHA and blob SHA 확인 후 현행 EUR-Lex Regulation (EU) 2024/2847 Article 11/13/14, Annex I Part I/II, Annex II 및 Annex III와 Pass A/B/C 대조.
- [x] 상세 감사: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md). 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; 5개 Raw Text Quote 모두 현행 법령 직접 인용으로 재사용 불가.
- [x] `CRA_ARCHIVE_AUDIT_QUEUE.md`에 #8–#12 판정·원본 SHA·commit·후속 교정 규칙 기록.
- [ ] main #13–#27 queue 등록 및 P0 우선 Pass A/B/C 감사. 현재 관찰된 main tip은 report #27, commit `c7eb7296671541c1ad2268cdcee80885091f230c`.
- 제품 적용성은 SKU/의도된 용도/연결성/실제 ST MCU 부품번호 미확정으로 계속 UNVERIFIED.


## Phase E status update — 2026-11-13 (E1/E2 complete)
- [x] User approved E1+E2 only; implemented `source_transport.py` standard-library IP-pinned HTTPS transport and connected it to `source_evidence.py`.
- [x] Validates every A/AAAA result; any non-public/invalid item fails closed. TCP uses only the validated literal IP set; TLS SNI/certificate hostname checks and Host header retain the allowlisted DNS hostname.
- [x] Redirects are manual and each hop is revalidated. Only TCP connect failures can fall back to another IP in the same validated answer set; TLS/read/protocol errors do not fallback.
- [x] Response handling hardened for Content-Encoding, malformed/negative/empty Content-Length and truncated body.
- [x] E2 offline tests cover IPv4/IPv6 literal routing, TLS hostname/trust, connect/read timeouts, pinned fallback, DNS answer validation, redirects, body/MIME/status/size and Phase A–D regressions.
- [x] Exact code/test HEAD `d355aefb74f2b1b9159de98827fac8600fb68d4c` CI run [#43367432101](https://github.com/useformotor3/ai-discord-bot/actions/runs/43367432101): 126 tests OK; strict archive 990/990, consistent=true.
- [x] Protected production files/workflows and main remain unchanged. No real URL fetch, Gemini API, production integration, or cost incurred.
- [ ] E3 real EUR-Lex + manufacturer source fetch/extraction fidelity: separate explicit user approval required.
- Details: `docs/PHASE_E_IMPLEMENTATION.md` and `docs/PHASE_E_CONTROLLED_FETCH_AND_EXTRACTION_DESIGN.md`.


## 2026-11-13 — Main archive reports #13–#27 audited
- Completed Pass A/B/C review of 15 main-only reports #13–#27; detailed findings and commit/blob traceability: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md).
- Result: 15 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; 0/15 Raw Text Quote blocks reusable as current-law verbatim quotes. Product applicability UNVERIFIED. Non-random sequential batch; not a whole-archive error rate.
- Add correction rules: distinguish Article 13(8) support period, Article 13(9) update availability, Annex I Part II(5) CVD, Part II(6) contact/information sharing, Part II(7) secure distribution, Part II(8) free updates and Article 14 reporting.
- Next audit target: reports #28 onward, prioritizing P0 claims. Original main branch remains read-only.
- Phase E3 approval package prepared: [PHASE_E3_APPROVAL_PACKAGE.md](PHASE_E3_APPROVAL_PACKAGE.md). It is design only; actual network fetch is still NOT AUTHORIZED.


## 2026-11-13 — 보고서 파일 우선 발행 및 운영 코드 개선 제안
- [x] 제1권 CRA 법령 조사 보고서 초판 생성: `docs/CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md`.
- [x] 제2권 서보 드라이브 적용·구현 방안 초판 생성: `docs/SERVO_DRIVE_CRA_IMPLEMENTATION_PLAN_V1.md`.
- [x] 기존 `docs/MASTER_REPORT.md`에 새 보고서 진입 링크 추가. 기존 본문은 삭제하지 않고 과거 초안으로 구분.
- [x] 운영 조사 자동화 보호 파일 개선 제안서 작성: `docs/PROTECTED_CODE_CHANGE_PROPOSAL_V1.md`. 코드 변경 전 승인 대기.
- [ ] 기존 추적성 매트릭스와 제1·2권 조항/요구사항 ID 통합 및 전수 링크 검사.
- [ ] 1,347개 main 아카이브의 inventory를 최신 main SHA 기준으로 재현하고 주제/조항/출처/중복/오류 후보 분류.
- [ ] Article 14 PSIRT tabletop 절차 및 제품 입력자료 확보.
- [ ] 실제 SKU/MCU/인터페이스/업데이트/지원기간 확보 후 제품별 적용성 확정.
- [ ] DOCX/PDF/PPTX/XLSX 무료 배포 파이프라인 설계·검증.

**진행 원칙:** 보고서 파일을 먼저 만들고 근거·설계·시험을 이어서 채운다. 파일이 커지면 권/장으로 분할하고 마스터 인덱스와 안정적 ID로 연결한다. 법령 근거 VERIFIED와 제품 적용 VERIFIED를 분리한다.

- [x] 마스터 보고서 인덱스 `docs/MASTER_REPORT_INDEX.md` 생성.
- [x] Article 14 신고 대응 절차서 `docs/CRA_ARTICLE14_PSIRT_RESPONSE_SOP_V1.md` 초판 생성.
- [ ] PSIRT 역할/연락처/제조사 단일 연락 창구 입력 및 tabletop 실행.


## 2026-11-13 — 수집 코드 우선순위 재조정
- [x] 현재 source fetcher/extractor 및 archive candidate workflow 코드 감사.
- [x] `docs/SOURCE_COLLECTION_CODE_AUDIT_AND_CHANGE_PROPOSAL_V1.md` 작성.
- [ ] **P0 선행:** C1 strict extraction integrity + observed document identity/revision.
- [ ] **P0 선행:** C2 source evidence bundle manifest + raw/text hash + locator linkage.
- [ ] C3 source-specific adapter/PDF backend hardening.
- [ ] C4 Phase E3 실제 공식 URL fetch — 별도 승인 필요.
- [ ] C5 non-production claim validator/report builder 통합.
- [ ] C6 main/prompt/production workflow integration — 별도 승인 필요.
- **현재 코드 변경·live fetch 없음.** C1+C2 구현은 상세 제안에 대한 사용자 승인 대기.


## C1+C2 수집 무결성 및 Evidence Bundle — 승인 후 구현
- [x] strict charset decoding; invalid/lossy bytes fail closed.
- [x] PDF page/empty-page/extraction quality diagnostics.
- [x] fetch raw hash ↔ extraction raw hash ↔ normalized text hash linkage.
- [x] source_id mismatch / hash mismatch blocks bundle.
- [x] expected vs observed document ID/revision separated; unconfirmed/mismatch states retained.
- [x] bounded excerpt/evidence IDs and versioned JSON schema.
- [ ] Final CI run and strict archive audit for exact final commit.
- [ ] Add real official-source fixtures and verify extraction fidelity only after separate E3 approval.
- [ ] C3 source-specific adapters/PDF backend hardening.
- [ ] C5 non-production report/claim integration after bundle contract review.
- [ ] C6 production integration remains separate protected-code approval.


## 조사 자료 더블체크 의무화
- [x] `docs/RESEARCH_DOUBLE_CHECK_STANDARD.md` 수립.
- 모든 향후 법령·제조사·제품·HW/FW 자료는 공식 원문, revision, 정확한 locator, 문맥·예외를 1차 확인한다.
- 독립적인 공식 근거를 통한 2차 교차검증을 수행한다.
- 2차 검증이 미완료면 VERIFIED 금지; PARTIALLY_VERIFIED / CONFLICT / UNVERIFIED로 유지한다.
- PDF 핵심 인용·표·도면은 페이지 이미지 시각 대조를 수행한다.
- Bundle의 IDENTITY_AND_REVISION_MATCHED는 문자열 일치일 뿐 VERIFIED가 아니다.


## Phase D hardening — 2026-11-13

1. Close validation-result/bundle mix-up risk with deterministic bundle fingerprint and complete Evidence ID inventory checks.
2. Carry claim-level machine evidence status into review packets; block candidate-support eligibility unless all linked evidence is EXACT_MATCH.
3. Require structured countercheck details and reject future UTC review timestamps.
4. Preserve the boundary that reviewer identity/independence are human-process controls, not machine-authenticated facts.
5. Require focused tests, full unittest suite, strict archive audit and exact-HEAD CI before marking complete.
6. After verification, return to the deliverable-first workstream: validate official source claims, expand the CRA servo-drive report with source-linked evidence, and publish the next report revision. Do not let pipeline hardening substitute for report production.


## 2026-11-13 — CRA 전용·결과물 우선 실행 기준

- 현재 범위는 CRA 서보 드라이브 조사·적용·설계·시험·증거·보고서이며 SIL 3 벤치마킹은 범위 밖이다.
- 신규 세션은 `docs/AI_CONTINUITY_BOARD.md`를 필수로 읽고, 현재 HEAD/main archive/CI를 다시 확인한다.
- 보고서 생산과 검증을 코드/파이프라인 개선과 동등한 최우선 결과로 취급한다. 가능한 작업마다 실제 보고서 본문, 비교표, 설계도, claim audit 또는 증거 대장을 남긴다.
- main archive report #8–#32 감사 완료: 총 25건 CONFLICT, direct quote reuse 0/25. 이 결과는 연속 비무작위 배치이며 전체 1,366개 archive 오류율이 아니다.
- main 현재 report #91, archive/history 1,366/1,366. 다음 audit target #33. 우선 #33–#91 대기열을 최신 main SHA 기준으로 등록하고 P0 claims부터 Pass A/B/C.
- 제1권 CRA 조사 보고서와 제2권 구현 계획은 초판이다. #28–#32 감사 결과 및 반복 정정 규칙을 통합해 다음 revision을 작성한다.
- E3 live source fetch, protected production code, Gemini V2 prompt/contract, main branch mutation/merge/rebase/sync는 별도 명시 승인 전 금지.


## 2026-11-13 — main reports #33–#37 감사 완료
- [x] #33–#37 Pass A/B/C 감사 및 blob SHA 기록.
- 결과 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; Raw Text Quote 재사용 0/5.
- 누적 #8–#37: 30 CONFLICT / direct quote reuse 0/30. 비무작위 연속 배치로 전체 오류율 추정에 사용하지 않는다.
- 다음 감사 시작점 #38. main tip 최신화 후 queue와 보고서 본문을 재확인한다.
- 적합성 평가 경로, 특히 Article 32 및 관련 Annex는 신규 공식 원문 재확인 전 제품별 판단/설계 확정 근거로 사용하지 않는다.


## 감사 문서 CI 확인
- #28–#37 감사 및 연속성 문서 HEAD `5fcd433436cc6261284d1bc8bbf648ae78af9b2e`: Actions #43386808125 SUCCESS, 140 tests, strict archive 990/990 consistent=true.
- 다음 감사는 #38부터 진행한다.

## 2026-11-13 — reports #38–#42 감사 완료 및 다음 실행

- #38–#42 Pass A/B/C 감사 완료. 결과 4 CONFLICT / 1 PARTIALLY_VERIFIED / 0 VERIFIED, 직접 인용 재사용 0/5.
- 이번 배치의 핵심 정정: Annex II point 8(d)는 secure decommissioning 및 user-data removal instructions 제공 의무다. 이는 모든 제품의 irrecoverable wipe 기능을 명시한 문구와 다르다. 사용자 정보는 Annex II point 7 및 8(a)–(f), 무료 보안 업데이트는 Annex I Part II(8), support period는 Article 13(8), update availability는 Article 13(9)로 분리한다.
- 다음 작업: #43–#47 감사 후 사용자 지침서 체크리스트/제1권 CRA 보고서의 EOL, support period, update, VDP 절을 정정한다. 아카이브 감사만 계속하지 말고 제1권/제2권에 교정 결과를 통합하는 deliverable-first 작업을 병행한다.
- main 최신 관찰: HEAD `e9bc84bfb5ccc7c18a69298cbd8f88376691b18c`, state count 93, history 1,368 entries. 작업 브랜치 상태는 커밋 직전 재확인한다.

## 2026-11-13 — reports #43–#47 감사 및 보고서 통합 우선순위

- #43–#47 감사 완료: 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- 제품 분류에서 가장 중대한 오류는 “산업용 서보 드라이브/IACS/PLC = Annex III Class II”라는 근거 없는 일반화다. Annex III Class II의 4개 범주와 Commission Implementing Regulation (EU) 2025/2392를 기준으로 core functionality를 평가한다.
- 마스터 보고서에 즉시 반영할 산출물:
  1. 제품 범주·제품 경계·core functionality 판정표(Article 7, Annex III, Implementing Regulation 2025/2392).
  2. 접근통제 매트릭스(Annex I Part I 2(d): 법적 요구와 RBAC/least privilege 등 설계 수단 구분).
  3. 취약점·지원기간 표(Article 13(8)/(9), Article 14, Annex I Part II(1)–(8)).
- 다음 #48–#52 감사는 위 세 문서 산출물과 병행하며, 단순 아카이브 판정 반복에 머물지 않는다.

## 2026-11-13 — 실무 산출물 v0.1 작성

- [CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md](CRA_PRODUCT_CLASSIFICATION_AND_ACCESS_CONTROL_MATRIX.md) 작성.
- 제품 분류 판단 게이트, Annex III category cross-check, Article 32 route, 접근통제 legal-vs-design matrix, 검증 증거 목록 및 미확인 입력을 한 문서로 구성했다.
- 다음 개정: 실제 SKU/매뉴얼/제품 경계 확보 후 classification record를 제품별로 완성하고, 접근통제 설계/시험 항목에 실제 HW/FW architecture evidence를 연결한다.



## 2026-11-13 추가 — 보고서·매뉴얼 통합 및 문서 구조 정리

### 목표
감사 보고서가 누적되는 데 그치지 않고 검증·정정 결과가 실제 CRA 보고서와 매뉴얼에 반영되도록 한다. 문서를 무조건 하나로 합치지 않되 과도한 분할과 중복을 줄인다.

### 실행 항목
- [x] 전체 문서 역할·정본·읽기 순서·링크를 정의한 CRA_DOCUMENT_ARCHITECTURE_AND_NAVIGATION.md 작성.
- [x] START_HERE에 문서 지도 및 상위 보고서 인덱스 연결.
- [x] AI_RULEBOOK에 문서 생성 억제, 정본 지정, 감사 결과의 본문 통합 의무 추가.
- [x] MASTER_REPORT_INDEX 및 MASTER_REPORT에 문서 구조·탐색 링크 추가.
- [ ] 제1권·제2권·MASTER_REPORT·Claim Evidence Ledger·정정 대장을 상호 대조해 감사에서 확인된 정정이 누락된 장/표를 찾는다.
- [ ] 반복 법령 정정(제품 분류, Article 13(8)/(9), Article 14, Annex I Part I/II, Annex II)을 단일 CRA 요구사항 기준표로 정리하고 제1권 본문에 반영한다.
- [ ] HW/FW 매뉴얼·PSIRT SOP·추적성 매트릭스에 동일 요구사항 ID와 근거 링크를 맞춘다.
- [ ] 문서별 중복 내용을 정리하고 superseded 상태 및 대체 링크를 표시한다.

### 완료 기준
- 사용자는 START_HERE에서 전체 문서 지도를 열 수 있다.
- MASTER_REPORT_INDEX에서 모든 현재 발행 산출물과 상태/역할을 찾을 수 있다.
- 반복 감사에서 검증된 핵심 결론을 최종 보고서에서 찾을 수 있고, 상세 원문 감사로 역추적할 수 있다.
- 동일 요구사항이 보고서·매뉴얼·매트릭스에서 서로 다른 조항·상태로 표시되지 않는다.
- 제품별 미확인 사항과 실제 미실행 시험은 계속 명시한다.


## 2026-11-13 추가 — main reports #48–#52 감사와 상위 문서 반영

- [x] main reports #48–#52 Pass A/B/C 감사: 3 CONFLICT / 2 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5.
- [x] 원본 archive path/blob SHA 및 공식 법령 조항·예외를 감사 문서에 기록.
- [x] Claim Evidence Ledger에 5개 원자 주장 정정 레코드 추가.
- [x] Article 14(8) 사용자 통지의 범위와 where appropriate machine-readable 조건을 제1권/PSIRT SOP에 반영.
- [x] Article 13(6) 구성요소 취약점 보고 방향과 Part II(4)–(8) 요구사항 구분을 제1권/제2권/MASTER_REPORT에 반영.
- [ ] 감사 #8–#52의 정정 사항 전체를 Claim Evidence Ledger와 제1권/제2권/매트릭스/매뉴얼 간에 전수 대조해 미반영 항목을 폐쇄한다.
- [ ] 다음 main-only audit batch #53–#57을 수행하고, 동일한 보고서 통합 절차를 반복한다.


## 2026-11-13 P0 — 한국어 정본 및 주장 대장 전수 동기화

- [x] 최종 산출물 기본 언어를 한국어로 확정하고 AI_RULEBOOK/문서 지도/START_HERE/MASTER_REPORT에 반영.
- [x] 제품 분류·접근통제 매트릭스 v0.2를 한국어 본문으로 전환.
- [x] #48–#52의 주장별 정정 레코드를 Claim Evidence Ledger에서 한국어로 정리.
- [ ] #8–#52의 기존 감사 결과를 Ledger와 제1권·제2권·PSIRT SOP·요구사항 매트릭스·위협/시험 대장에 전수 대조.
- [ ] 대조 결과 발견된 누락/상충만 기존 정본에 반영하고, 단순 요약용 신규 문서 생성을 피한다.
- [ ] 한국어 정본화가 필요한 영문 중심 실무 문서를 독자/용도 기준으로 선별해 번역·통합한다.
- [ ] 다음 main-only 감사 #53–#57 수행. 감사 결과는 같은 세션에서 상위 문서 반영 여부까지 확인한다.


## 2026-11-13 P0 — 감사 정정 정본 통합

- [x] #13–#42 반복 오류 패턴을 CRA 공식 법령 기준선 제2.3절에 통합.
- [x] 제1권에 Part I/Part II/Annex II/Article 14/64의 오해 방지 기준 추가.
- [x] 제2권에 법적 요구와 위험기반 설계 후보, 사용자 정보와 기술문서 구분 추가.
- [x] 요구사항 추적성 매트릭스에 #48–#52 조항 매핑 추가.
- [ ] #8–#52 원본 감사 결과와 Claim Evidence Ledger의 claim ID를 1:1 대조하고 누락/중복/판정 충돌을 폐쇄.
- [ ] #8–#12 원본 감사 문서 및 claim 연결을 확인. 찾지 못하면 미확인으로 기록.
- [ ] #13–#52 영문 감사 문서를 한국어 정본으로 전환하거나, 원본을 보존하면서 한국어 감사 요약을 본문 앞에 제공.
- [ ] 다음 #53–#57 감사는 위 정본 반영 확인 후 수행.


## 2026-11-13 P0 — #8–#52 파일 중심 Claim ID 연결

- [x] #8–#52 총 45개 원본 보고서의 날짜+경로+blob SHA+판정+중심 정정 요약을 Claim Evidence Ledger에 고유 ID로 등록.
- [x] #8–#12의 상세 감사 파일을 재발견하고 원본 경로/SHA/판정 확인.
- [ ] 각 보고서의 개별 법적 주장·Raw Text Quote 블록을 원자 주장 ID로 분해하고 정확한 조항·원문·정정·반증과 연결.
- [ ] 감사 결과와 제1권·제2권·SOP·추적성 매트릭스의 개별 요구사항 표현을 문장/조항 단위로 교차 대조.
- [ ] 영문 상세 감사 문서의 한국어 본문 전환 또는 한국어 상세 번역을 완료.


## 2026-11-13 P0 — #53–#57 통합 및 다음 감사

- [x] main reports #53–#57 Pass A/B/C 감사: 1 CONFLICT / 4 PARTIALLY_VERIFIED / 0 VERIFIED.
- [x] #53–#57 원본 경로/blob SHA 및 날짜 포함 Claim ID 5개를 Ledger에 등록.
- [x] Part I(2)(m) 데이터 제거 기능 결과, Annex II(8)(d) 사용자 지침, Article 13(19) 지원 종료일/종료 시점 알림을 법령 기준선과 보고서/매뉴얼에 반영.
- [x] Article 14 신고가 Class I/II 한정이 아니며 Article 69(3)상 기존 출시 제품에도 적용됨을 정정.
- [ ] #8–#57 개별 문서 내 모든 주장·인용을 원자 단위로 분해하고 Claim ID/공식 원문/정정/반증 연결.
- [ ] 영문 상세 감사 문서의 한국어 본문 전환 또는 상세 한국어판 작성.
- [ ] 다음 main-only 감사 #58–#62. 배치 시작 시 main HEAD/state/history 재조회.

## 2026-11-13 P0 — #58–#62 감사 완료 및 통합

- [x] main reports #58–#62 원본 5개를 main read-only에서 가져오고 날짜/일일 번호/경로/blob SHA 고정.
- [x] EUR-Lex Article 13/14, Article 16(3), Annex I Part I/II, Annex II Pass A/B/C 대조.
- [x] #58–#62 파일 단위 판정 5 PARTIALLY_VERIFIED / 0 CONFLICT / 0 VERIFIED; direct quote reuse 0/5.
- [x] 원자 Claim ID 20개를 Ledger에 추가하고 법령 위치/정정/상태 연결.
- [x] 제1권·제2권·PSIRT SOP·법령 기준선·요구사항 매트릭스·통합 매트릭스·MASTER_REPORT·인덱스에 정정 반영.
- [x] main #118 기준선 기록: state count 118, history 1,393; archive tree count 미확인.
- [ ] **다음 P0:** #8–#57 원본의 개별 주장·직접 인용을 원자 Claim ID/공식 원문 locator/정정/반증과 1:1 연결.
- [ ] #8–#57의 Claim Evidence Ledger와 제1권·제2권·PSIRT SOP·추적성 매트릭스·시험 대장 전수 대조.
- [ ] #13–#57 영문 상세 감사 문서를 한국어 본문으로 전환하거나, 원본 보존 + 한국어 상세판 작성.
- [ ] 위 전수 대조 후 main-only reports #63–#67 감사. 배치 시작 시 main HEAD/state/history를 다시 조회한다.
- main read-only, merge/rebase/sync 금지. E3 live fetch와 protected production integration은 별도 승인 전 금지.

## 사후 기준선 — main report #119 확인 (2026-11-13)

- #58–#62 감사는 main report #118 기준으로 수행했다.
- 이후 main에 report #119가 추가됨: HEAD \`6491a5db6ea35ea97a6d97e85bac43f9a3cf41c0\`, state count 119, history 1,394 entries.
- #119는 미감사 상태다. 다음 archive 감사는 #63–#67부터 수행하며, 배치 시작 시 main state/history/HEAD를 재조회한다.
- main read-only, merge/rebase/sync 금지.

## 2026-11-13 P0 — #8–#12 원자 주장 분해

- [x] main archive #8–#12 원본 경로/blob SHA 재대조.
- [x] 기존 감사 결과의 파일 단위 판정을 유지하면서 개별 주장·인용을 31개 원자 Claim ID로 분해.
- [x] secure-by-default Part I(2)(b), access control (d), attack surface (j), Class II Annex III 분리.
- [x] 강제 첫 접속 비밀번호 변경/모든 포트·JTAG 차단/least privilege를 보편적 법적 직접 의무로 쓰지 않도록 반증 연결.
- [ ] 다음 배치 #13–#17 원자 Claim ID 분해.
- [ ] 이어서 #18–#57 순차 분해 및 제1권·제2권·PSIRT SOP·추적성 매트릭스와 문장 단위 전수 대조.

## 2026-11-13 P0 — #13–#17 원자 주장 분해

- [x] #13–#17 main 원본 경로/blob SHA 재확인.
- [x] 개별 법령 주장·인용을 29개 원자 Claim ID로 분해해 Ledger에 연결.
- [x] Article 14 trigger/scope/timeline, Article 13 manufacturer duties, Annex I Part I/II, Annex III classification 혼동을 각각 분리.
- [x] 파일 단위 CONFLICT 5건과 개별 법령 사실 VERIFIED를 분리 기록.
- [ ] 다음 배치 #18–#22 원자 Claim ID 분해.
- [ ] #23–#57까지 순차 분해 후 제1권·제2권·PSIRT SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #18–#22 원자 주장 분해

- [x] #18–#22 main 원본 경로/blob SHA 재확인.
- [x] 개별 법령 주장·인용 29개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] Article 14 신고 trigger, support period, free updates/CVD, secure-default/access/integrity/attack-surface 조항을 분리.
- [x] file-level CONFLICT 5건과 개별 법령 사실 VERIFIED를 분리 기록.
- [ ] 다음 배치 #23–#27 원자 Claim ID 분해.
- [ ] #28–#57까지 순차 분해 후 제1권·제2권·PSIRT SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #23–#27 원자 주장 분해

- [x] #23–#27 main 원본 경로/blob SHA 재확인.
- [x] 개별 법령 주장·인용 30개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] secure-default/access/attack-surface와 특정 credential/port/MFA/JTAG 구현을 분리.
- [x] Annex III Class I/II 제품 분류를 제품 전체 core functionality 증거가 필요한 별도 판단으로 기록.
- [ ] 다음 배치 #28–#32 원자 Claim ID 분해.
- [ ] #33–#57까지 순차 분해 후 제1권·제2권·PSIRT SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #28–#32 원자 주장 분해

- [x] #28–#32 main 원본 경로/blob SHA 재확인.
- [x] 개별 법령 주장·인용 25개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] support period Article 13(8), update availability Article 13(9), CVD/contact/free update Annex I Part II, Article 14 two-track, Annex VII technical documentation을 분리.
- [x] file-level CONFLICT 5건과 개별 법령 사실 VERIFIED를 구분.
- [ ] 다음 배치 #33–#37 원자 Claim ID 분해.
- [ ] #38–#57까지 순차 분해 후 제1권·제2권·PSIRT SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #33–#37 원자 주장 분해

- [x] #33–#37 main 원본 경로/blob SHA 재확인.
- [x] 개별 주장·인용 31개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] Commission Implementing Regulation (EU) 2025/2392로 Annex III category technical descriptions/core functionality 추가 검증.
- [x] Article 32/Annex VIII conformity assessment, Article 28 DoC, Article 30 CE, Article 31/Annex VII technical documentation 정정.
- [ ] 다음 배치 #38–#42 원자 Claim ID 분해.
- [ ] #43–#57까지 순차 분해 후 제1권·제2권·SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #38–#42 원자 주장 분해

- [x] #38–#42 main 원본 경로/blob SHA 재확인.
- [x] 개별 주장·인용 33개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] #38 Annex I Part I(2)(m) 영구 삭제 기능 결과 요구와 Annex II(8)(d) 사용자 폐기 지침을 함께 반영.
- [x] Article 13(8)/(9), Annex II user instructions, Annex I Part II vulnerability handling을 분리.
- [ ] 다음 배치 #43–#47 원자 Claim ID 분해.
- [ ] #48–#57까지 순차 분해 후 제1권·제2권·SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #43–#47 원자 주장 분해

- [x] #43–#47 main 원본 경로/blob SHA 재확인.
- [x] 개별 주장·인용 37개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] Article 7/Annex III/Implementing Regulation 2025/2392, Article 32/Annex VIII, Article 64 penalty tiers, Article 13/Annex I vulnerability handling 정정.
- [x] #44 access-control result requirement와 RBAC/least-privilege implementation options 분리.
- [ ] 다음 배치 #48–#52 원자 Claim ID 분해.
- [ ] #53–#57까지 순차 분해 후 제1권·제2권·SOP·매트릭스 전수 대조.

## 2026-11-13 P0 — #48–#52 원자 주장 분해

- [x] #48–#52 main 원본 경로/blob SHA 재확인.
- [x] 개별 주장·인용 31개를 원자 Claim ID로 분해해 Ledger에 연결.
- [x] Article 14(8) machine-readable notice, Part II(4) disclosure, CVD/contact/free update, Article 13(5)–(7) supply-chain component obligations 정정.
- [x] file-level 3 CONFLICT / 2 PARTIALLY_VERIFIED와 개별 claim 상태 구분.
- [ ] 다음 배치 #53–#57 원자 Claim ID 분해.
- [ ] #8–#57 전체 원자 claim과 제1권·제2권·SOP·매트릭스 전수 대조.
