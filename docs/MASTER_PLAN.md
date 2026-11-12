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
- [ ] main.py 제어흐름/예외/쿼터/출력 변경 제안서 작성 (승인 전 수정 금지)
- [ ] 모델 실패/빈 응답을 성공 처리하지 않도록 수정
- [ ] 근거 메타데이터 필수 스키마 적용
- [ ] 원문 인용/링크/의미 검증을 구분
- [ ] 미검증 생성물은 초안으로 격리
- [ ] Discord timeout/HTTP status/재시도/중복 방지
- [ ] 무료 한도 fail-closed 및 유료 호출 금지
- [ ] 실패 경로 테스트 fixture

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
