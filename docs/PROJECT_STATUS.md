# CRA 서보 드라이브 개발 프로젝트 — 상황판

> 저장소: useformotor3/ai-discord-bot  
> 작업 브랜치: cra-project-foundation  
> 마지막 확인일: 2026-11-12

## 목적/범위
CRA를 모르는 개발자가 서보 드라이브 개발에 적용할 수 있는 공개 근거 기반 실무 지침과 통합 보고서 구축. CRA 전용이며 SIL 3 벤치마킹 제외. ST MCU 우선, TI 비교. Public 저장소에는 공개 자료만 저장.

## 실제 저장소 상태
- main과 작업 브랜치는 Git commit graph 기준 diverged 상태. archive 콘텐츠는 동기화했지만 commit graph를 병합한 것은 아니다.
- 작업 브랜치 마지막 확인 시 archive 990, history 990, 경로 중복/누락/orphan 0.
- main 마지막 확인 시 archive 990, history 990, 경로 중복/누락 0.
- main에서 확인된 6개 추가 자동 생성물을 원문 그대로 작업 브랜치에 보존.
- main state.json: date=2026-11-12, count=3 (일일 카운터).
- 6개 자동 생성 보고서 표본에서 CRA 조항/직접 인용/제품 분류 오류 발견. [ARCHIVE_TRIAGE_MAIN_ONLY_6.md](ARCHIVE_TRIAGE_MAIN_ONLY_6.md)
- 브랜치 및 파일 정합성: [REPOSITORY_RECONCILIATION.md](REPOSITORY_RECONCILIATION.md)

## 운영 규칙
- 신규 세션은 START_HERE, AI_RULEBOOK, 상황판, 계획, 지식 인덱스, 보고서, 최근 세션 로그를 먼저 읽는다.
- 과거 기억/AI 답변보다 최신 GitHub 상태와 공식 근거 우선.
- 이전 AI 산출물도 검증 전 사실로 취급하지 않는다.
- 성공·실패·오류·재발 방지 기록.
- 문서·폴더 구조·스키마·자동화 코드 모두 개선 가능.
- 미검증 주장을 확정 보고서로 승격하지 않는다.

## 자동화 위험
- main.py의 모든 모델 실패 후 경고 문구를 정상 성공으로 저장하는 위험.
- 출처 URL/원문 위치/문서 버전 자동 검증 부재.
- 프로젝트 운영 문서를 prompt에 로드하지 않고 최근 history snippet 5개만 사용.
- Discord timeout/HTTP status 확인 부재.
- MAX_DAILY_QUOTA=1200은 공식 무료 한도 근거가 없는 임의 상수.
- 기존 research workflow에는 cron 예약 실행 없음.

## 추가한 정합성 검사
- scripts/audit_archive.py: archive/history 경로, 중복, orphan, malformed history 검사. state.count는 일일 카운터로만 표시.
- tests/test_audit_archive.py: 정상/누락/고아/중복/잘못된 이력 항목 테스트 3개.
- .github/workflows/archive-audit.yml: 작업 브랜치 push 및 수동 실행 시 테스트와 strict audit 수행.
- 로컬 unittest: 3개 테스트 통과. GitHub Actions 최근 4회 실행의 audit job 및 단위 테스트/strict 검사 단계 모두 success 확인. [실행 이력](https://github.com/useformotor3/ai-discord-bot/actions/workflows/archive-audit.yml?query=branch%3Acra-project-foundation)

## CRA 근거 검증/전수 후보 추출
- [CRA_VERIFIED_BASELINE_2026-11-12.md](CRA_VERIFIED_BASELINE_2026-11-12.md): EUR-Lex Article 13/14/71, Annex I/II, Annex VII와 Commission reporting guidance를 원문 대조한 1차 기준선.
- ST AN5156 Rev 14 (June 2026), STM32Trust 및 TI MSPM0G3529-Q1 데이터시트(SLASFO2B, revised Oct 2025), TI SLAAE29A(Rev Dec 2025) 공식 자료를 확보. ST 부품번호가 없어 동급 비교는 미확정.
- scripts/extract_archive_claim_candidates.py schema 1.1 및 tests/workflow 최종 실행 성공. 990개에서 주장 후보 4,400개, Article 후보 1,224개 추출.
- 추출기에 출처 섹션, 주장 문단 행 번호, 인용 후보 행 번호, 위험 플래그별 문맥 스니펫(최대 3개)을 추가. 모든 항목은 UNVERIFIED.
- URL 후보 0개의 원인을 대표 원본 6개에서 확인: Source 영역은 법령 문서명/조항명 중심이고 canonical URL이 기록되지 않은 패턴. 표본은 원인 확인용이며 990개 전체의 URL 누락률을 대신하지 않는다.
- 상세: [ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md](ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md).
- 휴리스틱 플래그: SBOM 범위 과장 후보 305, 5년 고정 지원기간 표현 500, Article 14 신고 언급 201, Article 11 신고 오기 가능성 85, 제품 분류 단정 후보 190, Annex 구분 혼동 21, CRA 인증 의무 단정 16, 업데이트 분리 조건 누락 후보 4, Article 13(8) 지원기간 14. 오류 확정 수가 아니라 검토 우선순위 후보.
- 최초 구현의 URL 정규식 escaping 오류 및 테스트 fixture 길이 오류로 CI 실패를 경험. 로그에 근거해 수정 후 최종 extraction workflow와 archive integrity workflow success 확인.
- 전체 JSON은 reports/archive_claim_evidence_candidates.json에 GitHub Actions가 커밋함. Artifact run 43127072320도 success.

## 별도 인벤토리 파이프라인
- scripts/build_archive_inventory.py: 990개 archive에서 파일 SHA-256, 크기, 제목/헤딩, URL 후보, CRA 조항/Annex 후보, 주제 키워드 후보, history 메타데이터 추출.
- 모든 레코드는 UNVERIFIED_AI_ARCHIVE로 표시. 키워드 분류/URL 추출은 후보일 뿐 법령·링크·인용 정확성 검증이 아님.
- tests/test_build_archive_inventory.py: 메타데이터 추출/미분류/중복 이력 테스트.
- .github/workflows/archive-inventory.yml: 수동 실행 및 archive 변경 시 인벤토리 JSON을 30일 Artifact로 업로드. 최초 실행 상태 확인 중.

## 인벤토리 실행 결과
- 990개 파일, 990개 history 항목을 스캔.
- 주제 키워드 후보: SBOM/공급망 779, 취약점 처리 753, 보안 업데이트 723, 지원기간 406, 제품 분류 338, 사고 신고 259, 기술문서 253, 인증/암호 121, Secure Boot 97, 위협모델 97, 표준/시험 23, 미분류 10.
- 다중 라벨이며 단순 키워드 후보. 합계는 문서 수가 아니고 사실 검증 결과가 아님.
- 상세: [ARCHIVE_INVENTORY_2026-11-12.md](ARCHIVE_INVENTORY_2026-11-12.md)

## 메인 코드 변경 제안
- [CHANGE_PROPOSAL_MAIN_GEMINI.md](CHANGE_PROPOSAL_MAIN_GEMINI.md)에 main.py/Gemini prompt 개선안 작성.
- 사용자 승인 전 main.py, Gemini prompt, 운영 research workflow는 수정하지 않음.

## 수동 표본 감사
- 초기 5개 조사 파일 감사: 4 CONFLICT, 1 PARTIALLY_VERIFIED. [상세](ARCHIVE_MANUAL_SAMPLE_AUDIT_5_2026-11-12.md)
- 추가 9개 고위험 후보 감사: 7 CONFLICT, 2 PARTIALLY_VERIFIED. Article 10/11/14 혼동, 지원기간/무상 업데이트 조항 혼동, Class I 단정 및 Article 24/32 혼동 확인. [상세](ARCHIVE_MANUAL_AUDIT_9_2026-11-12.md)
- 당시 합계 14개 표본: 11 CONFLICT, 3 PARTIALLY_VERIFIED. 이후 추가 20개 감사 반영 누계는 34개: 25 CONFLICT, 9 PARTIALLY_VERIFIED. 무작위 표본이 아닌 위험 기반/시간순 표본이며 전체 990개 오류율을 의미하지 않는다.
- 출처 URL 누락 원인 표본 감사 및 전수 검증 큐: [ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md](ARCHIVE_SOURCE_GAP_AUDIT_2026-11-12.md)

## 제품 경계 및 적용성 템플릿
- [SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md](SERVO_DRIVE_PRODUCT_BOUNDARY_TEMPLATE.md) 생성. Article 2/3 scope, digital connection, remote data processing, product boundary, core functionality 및 Annex III/IV 분류 입력을 수집하도록 구성.
- 제품 SKU, EU 판매 형태, 실제 연결성, 원격 기능, ST MCU 주문 코드가 확인되지 않아 현재 적용성/등급은 UNVERIFIED.

## 다음 작업
- [x] URL 후보 0개 원인 대표 6개 표본에서 확인, 출처 메타데이터 개선/검증 큐 문서화
- [x] 위험 플래그에서 추가 9개 고위험 문서 수동 감사 (7 CONFLICT, 2 PARTIALLY_VERIFIED)
- [ ] 위험 플래그별 추가 표본검사 및 실제 오류/정상 주장 구분
- [ ] 원문 인용 후보와 내부 텍스트 원문 대조표 작성
- [ ] main.py 실패 처리·근거 스키마·검증 게이트 변경 제안서 작성 (사용자 승인 전 수정 금지)
- [ ] 기존 990개 자료 전체 주제 분류 및 주장/출처 인벤토리
- [ ] CRA 공식 근거 전수 검증
- [ ] 서보 드라이브 적용성 분석
- [ ] ST MCU 정확한 부품 번호 확보 후 기능 검증
- [ ] TI 비교 및 통합 보고서 작성
- [ ] 브랜치 PR/병합 전 diff 및 충돌 검토

## 최근 CI/기준 상태 (2026-11-12)
- 최신 CRA Archive Integrity run 43128434351: completed/success. 최신 run의 테스트 및 strict archive/history consistency 단계 success.
- Claim Evidence Extraction run 43127855869: completed/success. Artifact ID 13903243617 생성.
- archive 990개 유지. main.py SHA-1 blob은 기존 값 86a7731aad5de8d75581fc953bcea2c44adf2f2b로 변경 없음.
- main branch 병합/운영 workflow 변경 없음.

## 상태
VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED / CONFLICT / OUTDATED / NOT_APPLICABLE

마지막 갱신: 2026-11-12


## 추가 수동 감사 — 2026-11-12 (20개)
- [ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_20_2026-11-12.md): 2026-11-11~12 위험 주제 구간에서 20개 문서를 공식 EUR-Lex 원문과 대조.
- 결과: 14 CONFLICT / 6 PARTIALLY_VERIFIED.
- 초기 5개 + 추가 9개 + 이번 20개 = 누계 34개, 25 CONFLICT / 9 PARTIALLY_VERIFIED.
- 모두 비무작위 위험 표본으로 전체 990개 오류율을 나타내지 않는다.
- 반복 오류: Article 10/11/14 오기, Article 24/31/32 혼동, Article 13(8) 지원기간 예외 방향, Annex I Part I/II 및 Annex II/III 혼동, 허위 직접 인용, 존재하지 않는 산업 자동화/서보 드라이브 Annex III 분류.
- 원본 research_archive 990개는 수정하지 않았다. main.py/Gemini prompt/운영 run workflow 미수정.
- 기준 원문 EUR-Lex Regulation (EU) 2024/2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 (확인일 2026-11-12).

- 추가 감사 반영 후 CRA Archive Integrity workflow run [43130099298](https://github.com/useformotor3/ai-discord-bot/actions/runs/43130099298) completed/success. 단위 테스트와 strict archive/history consistency 단계 모두 통과.


## 제조사 MCU 보안 자료 기준선 / 주장 대장 (2026-11-12)
- [MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md](MANUFACTURER_SECURITY_SOURCE_REGISTER_2026-11-12.md): ST AN5156 Rev14 (June 2026), AN4992 Rev19 (July 2026), TI MSPM0G3529-Q1 SLASFO2B RevB (October 2025), TI SLAAE29A RevA 및 TI G-Series TRM revision index를 등록. 기능별 secure boot/update, debug/lifecycle, key storage, crypto/TRNG, memory isolation, manufacturing provisioning 비교.
- [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md): source ID, canonical URL, version, source location, claim type, status, correction, product scope 스키마 및 제조사 기술 주장 초기 12건(문서 수준 VERIFIED 11건, 최신판 확인 대기 PARTIALLY_VERIFIED 1건).
- TI MSPM0G3529-Q1은 구체적인 비교 예시 부품. 이 제품이 프로젝트 대상 또는 ST MCU의 동급 대체품이라는 뜻은 아님.
- TI의 MSPM0G3506 문서 인덱스에서 SLAAE29 RevB(2026-08-27), G-Series TRM RevF(2026-11-05) 목록을 확인. SLAAE29 RevB 본문 및 G3529-Q1 적용성은 아직 검증 전. 기존 RevA 기반 기술 설명은 이전 판본으로 한정.
- ST AN5156은 여러 STM32 시리즈를 다루므로 정확한 ST 주문 코드가 없으면 부품별 기능을 확정하지 않는다.
- TI 데이터시트의 PSA Level 1 “targeted”는 인증 취득 완료가 아니다. Automotive Q1/ASIL 관련 문구는 CRA 적합성 근거가 아니다.
- 원본 archive, main.py, Gemini prompt, 운영 research workflow 및 main branch는 수정하지 않음.
