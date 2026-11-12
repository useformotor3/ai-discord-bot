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
- [CLAIM_EVIDENCE_LEDGER.md](CLAIM_EVIDENCE_LEDGER.md): source ID, canonical URL, version, source location, claim type, status, correction, product scope 스키마 및 제조사 기술 주장 15건(문서/인덱스 수준 VERIFIED 13건, PARTIALLY_VERIFIED 1건, UNVERIFIED 1건).
- TI MSPM0G3529-Q1은 구체적인 비교 예시 부품. 이 제품이 프로젝트 대상 또는 ST MCU의 동급 대체품이라는 뜻은 아님.
- TI의 MSPM0G3506 문서 인덱스에서 SLAAE29 RevB(2026-08-27), G-Series TRM RevF(2026-11-05) 목록을 확인. SLAAE29 RevB 본문 및 G3529-Q1 적용성은 아직 검증 전. 기존 RevA 기반 기술 설명은 이전 판본으로 한정.
- ST AN5156은 여러 STM32 시리즈를 다루므로 정확한 ST 주문 코드가 없으면 부품별 기능을 확정하지 않는다.
- TI 데이터시트의 PSA Level 1 “targeted”는 인증 취득 완료가 아니다. Automotive Q1/ASIL 관련 문구는 CRA 적합성 근거가 아니다.
- 원본 archive, main.py, Gemini prompt, 운영 research workflow 및 main branch는 수정하지 않음.

- 제조사 source register/claim ledger 반영 후 CRA Archive Integrity run [43133646074](https://github.com/useformotor3/ai-discord-bot/actions/runs/43133646074) completed/success. Unit tests 및 strict archive/history consistency 모두 통과.


## 2026-11-12 추가 진행 — 보안 하드웨어 참조 설계 및 TI 문서 재점검
- [서보 드라이브 CRA 보안 하드웨어 아키텍처](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md) 생성: 12개 하드웨어 블록 후보, 6개 trust boundary, secure boot/update 흐름, 키/제조 프로비저닝, 10개 업데이트 시험, CRA 조항-설계-증거 매핑 포함.
- 문서는 제품별 설계 확정본이 아니다. ST MCU part number, 제품 SKU, 실제 인터페이스/업데이트/안전 경계가 없으므로 구현/적용성 상태는 UNVERIFIED.
- TI MSPM0G3529-Q1 제품 페이지에서 G-Series TRM 참조를 확인했고, TI MSPM0-DIAGNOSTIC-LIB 기술자료 인덱스에서 TRM Rev F (2026-11-05)를 확인. TRM 본문은 대용량으로 현재 도구에서 열람 실패하여 보안 장 세부 내용은 검증하지 않음.
- SLAAE29 Rev B는 공식 본문 재확보 실패. SLAAE29A Rev A만 본문 확인된 자료로 유지.
- 새 아키텍처 문서의 모든 CRA 설계 연결은 법령의 결과 요구를 개발 작업으로 번역한 권고이며, 특정 부품/알고리즘/회로를 CRA가 직접 요구한다고 표현하지 않음.


## 2026-11-12 추가 — 아카이브 34개 표본 정정 추적성
- [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md) 생성: 원본 파일 경로·SHA-1·행 위치·주장 요약·정정 근거 룰·판정 상태 연결.
- 집계 검증 중 감사 ID 중복을 발견: A-013과 B-006은 동일한 `2026-11-11_230055.md` / SHA-1. 따라서 35개 감사 ID 행이 34개 고유 파일을 가리킨다.
- 고유 파일 기준 판정은 25 CONFLICT / 9 PARTIALLY_VERIFIED로 기존 34건 집계와 일치한다. 추가 9개 보고서의 10개 ID 중 1개가 추가 20개 표본과 중복.
- 원본 아카이브 34개는 수정하지 않았다. 이 작업은 표본 정정 추적성 구축이며 990개 전체 전수 검증이 아니다.


## 2026-11-12 — 34개 표본 법령 인용문 단위 감사
- 상세 결과: [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md).
- 기존 감사 ID 35행을 원본 SHA-1 기준 34개 고유 파일로 대조했다. A-013/B-006은 동일 원본이므로 중복 집계하지 않는다.
- 각 원본의 법령 인용 후보를 EUR-Lex 공식 원문과 대조하고, 직접 인용/생략 인용/요약의 오표시/합성·창작 문구/조항 오기를 구분했다.
- 반복 오류: Article 10·11을 제조자 의무/신고로 오인, Article 14를 지원기간·무료 업데이트로 오인, Article 24를 기술문서/적합성 평가로 오인, Annex I Part I/II 혼동, 존재하지 않는 산업 자동화/서보 드라이브 Annex III 카테고리 생성.
- 지원기간 Article 13(8), 업데이트 무상 제공 Annex I Part II(8), 업데이트 분리 Part II(2), 신고 Article 14는 서로 다른 의무다. Annex I Part I(2)(g)는 데이터 최소화, (h)는 가용성 보호다.
- 감사 결과는 34개 위험 기반 표본에만 적용된다. 전체 990개 오류율로 일반화하지 않는다.
- 원본 research_archive, main.py, Gemini prompt, production run.yml은 수정하지 않았다. main merge 없음.


## 검증 품질 게이트 — 2026-11-12
- [검증 운영 프로토콜](VERIFICATION_PROTOCOL.md)을 프로젝트 공통 작업 기준으로 추가했다.
- VERIFIED 승격에는 공식 원문·정확한 버전/위치/문맥, 별도 재검증(Pass B), 반증 확인(Pass C), 제품 적용성 판단이 필요하다.
- 동일 AI의 반복 답변은 독립 검증으로 계산하지 않는다. 법령의 단일 권위 원문은 독립적인 문맥/조항 재확인으로 검증 절차를 남기며, 별도 출처가 원문을 반복하는 경우 독립 증거로 과장하지 않는다.
- 작업 순서는 P0 제품 범위/분류/핵심 의무/정확한 MCU → P1 설계·시험 → P2 보조 설명으로 고정했다.
- 이번 세션은 운영 프로토콜 문서화만 완료했다. 기존 34개 인용 감사 전체를 이 신규 Pass A/B/C 양식으로 재실행한 것은 아니다. 기존 인용 감사는 사람의 원문 대조 기록이며, 신규 프로토콜 기준으로는 재검증 보완이 남아 있다.


## Pass B/C 별도 재검증 — Batch 01
- 상세: [ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md).
- A-001–A-008 8개 원본의 인용 블록을 기존 감사 결론과 분리해 EUR-Lex 현행 법령 원문으로 재대조하고 예외/반대 근거를 확인했다.
- 8개 파일 중 인용 블록 전체가 VERIFIED인 파일은 0개. A-003의 SBOM 인용은 원문 일치, A-004의 secure-by-default/접근통제 인용은 대체로 일치, A-005의 CVD 취지는 일부 맞지만 신고 조항과 인용 번호가 잘못됐다. 나머지는 직접 인용 오기/합성 또는 위치 오류가 확인됐다.
- 중요 정정: Article 13(8)은 지원기간(최소 5년, 예상 사용기간이 더 짧으면 그 기간), 무상 업데이트는 Annex I Part II(8), 업데이트 분리는 Part II(2), 자동 업데이트 관련 제품 속성은 Part I(2)(c), 신고는 Article 14.
- Pass B/C는 동일 AI 세션 내 별도 원문 재확인 절차이며 제3자 독립 법률 검토가 아니다. VERIFIED 승격은 아직 없음.


## Pass B/C 별도 재검증 — Batch 02
- 상세: [ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md).
- A-009–A-015 및 B-001–B-002, 8개 파일의 Raw Text Quote를 EUR-Lex 현행 원문과 다시 대조했다.
- 8개 모두 직접 인용으로 재사용 불가 판정. 지원기간의 “whichever is shorter/longer” 혼동, Article 14 신고 대상 확대, Annex I Part I/II 구조 혼합이 반복됨.
- Batch 01과 Batch 02를 합쳐 Pass B/C 재검증 16/34개 고유 표본 진행. 이 수치는 문서 수이며 claim 수가 아니다. 동일 AI 세션의 별도 절차 검증이며 제3자 검토가 아니다.


## Pass B/C 별도 재검증 — Batch 03
- 상세: [ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md).
- B-003–B-010 8개 파일을 EUR-Lex 현행 원문으로 재검증했다. B-009의 secure-by-default 문구만 핵심 취지가 일치하나 위치/표현 수정 필요. 나머지는 직접 인용/조항/적용 범위에 오류가 확인됐다.
- B-010의 Class II 적합성 평가 근거는 Article 32(3)이며 Article 24가 아니다. Annex III Class II 카테고리 및 Article 7 core functionality 증거가 없어 서보 드라이브 Class II 단정은 미확정/근거 부족이다.
- Pass B/C 재검증 24/34개 고유 표본 진행. 10개 파일 남음. 동일 AI 세션의 별도 절차 검증이며 독립 제3자 검토는 아니다.


## Pass B/C 최종 재검증 완료 — 2026-11-12
- 상세 최종 요약: [ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md](ARCHIVE_PASS_BC_FINAL_SUMMARY_2026-11-12.md).
- 기존 감사 ID 35행에서 A-013/B-006 동일 원본을 제거한 34개 고유 파일 전체를 4개 배치로 재검증했다.
- 파일 단위 결과: VERIFIED 0, PARTIALLY_VERIFIED 6, REJECTED 28. 파일 내 일부 문구가 맞더라도 다른 인용/조항이 잘못된 경우 PARTIALLY_VERIFIED로 분류했다.
- 반복 오류: Article 13(8) 지원기간과 Part II(8) 무상 업데이트 혼동, Article 14 신고 대상 범위 과장, Annex I Part I/II 혼동, Article 31/32 및 Article 28/29/30 혼동, Annex III 산업 자동화/서보 드라이브 카테고리 창작.
- 범위는 34개 위험 기반 표본의 CRA 법령 인용이며 990개 전체 오류율이 아니다. 표준·제조사 인용 및 나머지 956개는 별도 검증 필요.
- 검증 절차는 동일 AI 세션의 별도 Pass B/C이며 제3자 독립 법률 검토가 아니다.


## 법령 요구사항 → HW/FW/시험 추적성 매트릭스
- [CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md](CRA_REQUIREMENTS_TO_SERVO_DRIVE_TRACEABILITY_MATRIX.md) 생성.
- Annex I Part I 제품 속성 13개 항목, Part II 취약점 처리 8개 항목, Article 13 제조자 의무, Article 14 신고를 HW/FW/운영 통제·시험·합격 기준·증거 파일 후보로 연결.
- 법령 요구와 구현 권고를 구분하고, 제품별 입력이 없는 모든 row는 UNVERIFIED 유지.
- 이 매트릭스는 일반 참조 설계 초안이며 제품별 적용성/CRA 적합성 결론이 아니다.


## 위협 모델 및 시험·증거 대장 (2026-11-12)
- [THREAT_MODEL_SERVO_DRIVE_CRA.md](THREAT_MODEL_SERVO_DRIVE_CRA.md): 자산 10종(AST-01..10), 공격자 6유형(ACT-01..06), 신뢰 경계 8개(TB-01..08), 위협 18개(TH-01..18) 등록.
- [SECURITY_TEST_EVIDENCE_REGISTER.md](SECURITY_TEST_EVIDENCE_REGISTER.md): 위협별 시험 케이스, NOT_RUN 기본 상태, 증거 ID/파일명/메타데이터 규칙, 제품별 수치형 합격 기준 입력표 작성.
- 설계 후보와 법령 의무를 분리했으며, 특정 알고리즘/secure element/dual-bank/네트워크 분리 회로를 법령 직접 요구로 표시하지 않음.
- 실제 DUT/SKU/MCU/인터페이스/안전 경계/승인된 합격 기준 미확보. 시험 실행 및 제품별 위험도는 미확정(UNVERIFIED).

## 2026-11-12 통합 추적성 및 공식 자료 변경 감시
- [CRA_INTEGRATED_TRACEABILITY_MATRIX.md](CRA_INTEGRATED_TRACEABILITY_MATRIX.md) 생성: TR-01..TR-20을 법령 요구 → 자산/위협 → HW/FW 통제 후보 → TST 시험 → EV 증거 ID로 연결.
- [CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md](CRA_COMMISSION_GUIDANCE_REVIEW_2026-11-12.md) 생성: European Commission C(2026) 5252, 2026-07-27 공식 게시 사실과 적용 영향 등록. Annex 본문 페이지/문단별 검증은 PENDING.
- TI SLAAE29 Rev B(2026-08-27)와 G-Series TRM Rev F(2026-11-05)는 공식 인덱스 메타데이터만 확인. 본문 세부 내용은 열람/검증하지 않았으므로 미확인 유지.
- ST AN5156 Rev14/June 2026 공식 페이지 메타데이터 재확인. 정확한 ST MCU 부품 기능은 여전히 미확인.
- 주간 CRA·MCU 보안 자료 점검 자동화 등록: 매주 월요일 09:00 Asia/Seoul, 첫 예정 실행 2026-11-16.
- 모든 신규 매트릭스 행은 제품 적용성 UNVERIFIED, 시험 NOT_RUN. `main.py`, Gemini prompt, production workflow, main branch는 변경하지 않음.

## 2026-11-12 — 통합 연결성·자동 생성물 감사 추가

- 통합 매트릭스 검사: TR-01..TR-20 20개, 중복 0.
- 위협 모델 검사: AST 10개, TH 18개, 중복 0.
- 시험 대장 검사: TST 45개, 중복 0. 매트릭스 내 모든 개별/범위 참조 45개가 대장에 존재. 실제 DUT 시험 결과는 전부 NOT_RUN.
- main 브랜치의 자동 생성 report #35(research_archive/2026-11-12_025041.md, blob f4bdaf84c19da80707b43f9db616712a7d17061d, commit f3eed0a20bfd9ee118561e8bcd0ae890d84ef6e2)를 EUR-Lex Annex I와 대조. 하드웨어 Secure Boot/TPM/SE/디지털 서명 의무 단정 및 Annex I Part I(2)(b)–(d) 직접 인용 번호/문구 오류 발견. 파일 판정 CONFLICT, 인용 블록 REJECTED.
- 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_35_2026-11-12.md). main 원본/이력/상태는 변경하지 않음.
- TI SLAAE29 Rev B 본문을 공식 HTML에서 직접 확인. Revision history와 CSC/KEYSTORE/AESADV/TRNG 설명을 확인했으나, 문서 지원 부품 목록에는 MSPM0G3529-Q1이 없음. 따라서 Rev B의 플랫폼 예제를 G3529-Q1 기능으로 전용하지 않음.
- Commission C(2026) 5252 Annex는 공식 endpoint에서 도구 Unicode decoding error로 다시 열지 못함. 본문 페이지별 검증 미완료.
- main.py SHA-1 86a7731aad5de8d75581fc953bcea2c44adf2f2b, production run.yml SHA-1 65a8cadc8eac593f551e390698e367b1d161ecf1 확인. 변경 없음.
- main 병합 없음. 이 감사/문서 변경은 cra-project-foundation 브랜치에만 저장.

## 2026-11-12 — main-only report #36 감사

- main report #36: research_archive/2026-11-12_025529.md, blob SHA 0d5b3f17b13f8935a90c23400173e401a76e1953, commit 5cd4a18dbf5dc4712d669b29b8846af799f5efc1.
- EUR-Lex 원문 대조 결과: Article 14(신고)와 Annex I Part II(8)(무상 보안 업데이트) 혼동, Annex I Part I(2)(b),(c),(g) 오기, Secure Boot/Measured Boot/TPM 보편 의무 단정, 정식 법령 제목의 개정 법령 번호 오류.
- 파일 판정 CONFLICT, Raw Text Quote REJECTED. 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_36_2026-11-12.md). main 원본 수정/병합 없음.

## 자동 조사 파이프라인 신뢰성 — #35/#36 증거 반영

- main-only report #35/#36에서 법령 조항 오기, 원문에 없는 Secure Boot 직접 인용, Article 14/무상 업데이트 혼동이 재현됨.
- [CHANGE_PROPOSAL_MAIN_GEMINI.md](CHANGE_PROPOSAL_MAIN_GEMINI.md)에 직접 인용 문자열 검증, Annex/Part/point 정합성, 법령 메타데이터 대조, 법령 의무와 설계 선택 분리, 회귀 테스트를 추가 제안했다.
- 제안 상태는 USER_APPROVAL_REQUIRED. main.py, Gemini prompt, 파서/검증 게이트, production workflow는 변경하지 않았다.

## 하드웨어 아키텍처 법령 매핑 정정 — 2026-11-12

- 재검사에서 CRA-HW-05의 confidentiality/integrity를 Part I(2)(f) 하나로 연결한 오류, CRA-HW-06의 availability/resilience를 Part I(2)(g)로 연결한 오류를 발견해 수정했다.
- 정확한 매핑: confidentiality (e), integrity (f), data minimisation (g), availability/DoS resilience (h), connected device/network impact (i).
- CRA-HW-11을 추가해 Part I(2)(g) 데이터 최소화 설계 검토를 별도 연결했다.
- TI SLAAE29 Rev B 직접 확인 결과와 MSPM0G3529-Q1 미포함 지원 부품 목록 주의사항도 아키텍처 문서에 반영했다. 제품별 기능 적용성은 UNVERIFIED.

## 하드웨어 설계 선택 매트릭스 추가

- [SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md](SERVO_DRIVE_CRA_SECURITY_HARDWARE_ARCHITECTURE.md)에 DEC-01..DEC-10 선택 매트릭스와 G-01..G-06 설계 동결 게이트를 추가했다.
- 단일/분리 MCU, boot trust anchor, Flash slot, debug/service, network boundary, key storage, power/reset, sensor, gate driver, manufacturing provisioning의 대안을 정리했다.
- 특정 부품/회로는 선택하지 않았다. 모든 DEC/Gate는 TBD/미충족이며 제품 SKU, 정확한 ST MCU, 실제 인터페이스, timing/safety 입력을 기다린다.

## main-only report #37–#39 감사 — 2026-11-12

- main 자동 생성 보고서 #37–#39 원문을 EUR-Lex와 대조했다. 3건 모두 CONFLICT, 합성/오위치 직접 인용은 REJECTED.
- 반복 오류: Article 11/13(2)/13(6)을 지원기간 또는 무상 업데이트 근거로 오용; Article 13(8) 지원기간과 Annex I Part II(8) 무상 업데이트 혼동; Annex I Part II를 (a)–(d)로 잘못 인용; Part I(2)(b)와 (c) 혼동.
- 정확한 법령 원문 위치: Article 13(2),(6),(8) lines 888–908; Annex I Part I(2)(b),(c) and Part II(1)–(8) lines 1747–1773.
- 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_37_39_2026-11-12.md). 원본 main archive/history/state 수정 없음.

## 하드웨어 인터페이스 설계 계약 — IF-01..IF-09

- 하드웨어 아키텍처에 IF-01..IF-09 인터페이스 설계 계약을 추가했다: 외부 통신, 통신→모션 명령, MCU→Gate Driver, 센서/엔코더, NVM, 선택적 Secure Element, debug/service, power/reset/clock, 제조 프로비저닝.
- 각 인터페이스에 신뢰 경계, 설계 계약, 전기/물리 검토 항목, 기존 시험 연결을 정의했다.
- 회로도 리뷰 체크리스트 10개 항목 추가. 모든 제품별 상태는 UNKNOWN/UNVERIFIED이며 전압·절연·ESD·타이밍 수치는 임의로 정하지 않았다.


## Main-only reports #40–#55 감사 — 2026-11-12

- main 자동 생성 보고서 #40–#55의 원문을 commit diff에서 확인하고 EUR-Lex Regulation (EU) 2024/2847과 대조했다.
- 파일 단위 판정: PARTIALLY_VERIFIED 2건 (#40 secure-by-default/attack-surface, #49 secure decommissioning/user-data removal), CONFLICT 14건. 직접 인용으로 재사용 가능한 완전 VERIFIED 파일은 0건.
- 반복 오류: Article 11/10/13(4)/13(6)/13(8)/14 혼동, Annex I Part I와 Part II 혼합, Part II(8) 무상 업데이트와 Article 13(8) 지원기간 혼동, Article 14 신고대상 범위 확대, 존재하지 않는 문장/번호의 인용, 특정 구현(RSA/ECDSA, dual-bank, hot-patch, zero downtime, STO/SIL core separation)을 법적 의무로 단정.
- 중요 정정: secure decommissioning은 Annex II point 8(d) 및 영구 데이터/설정 제거는 Annex I Part I(2)(m)에 근거가 있다. 다만 Annex VII가 아니라 Annex II이며 cryptographic erasure 자체가 일률적으로 명시된 것은 아니다.
- 정확한 매핑은 Article 13(8)=support period, Article 14=actively exploited vulnerability/severe incident reporting, Annex I Part II(7)=secure update distribution, Part II(8)=free security updates(맞춤형 제품에 대한 제조자-사업 사용자 별도 합의 예외), Annex II point 8(d)=secure decommissioning instructions.
- 상세: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_40_55_2026-11-12.md). 원본 main archive/history/state, main.py, Gemini prompt, production workflow는 수정하지 않았다.
- 공식 EUR-Lex source lines checked: Article 13 lines 888–905; Article 14 lines 939–964; Annex I lines 1743–1773; Annex II lines 1776–1794. Commission C(2026) 5252 official publication page confirms 27 July 2026 publication and non-binding nature.


## Commission guidance / TI TRM Rev F follow-up — 2026-11-12

- Commission C(2026) 5252 Annex structured text was inspected via a transcription page that identifies the official PDF filename and SHA-256 and states it was verified against the PDF; official Commission page confirms publication 2026-07-27 and non-binding status. Support-period guidance points 125–127: 5 years is not the default; use expected-use rationale, and industrial control systems often have longer expected use. Core-functionality points 139–145 reinforce that product category cannot be inferred from the presence of a component alone. Reporting points 209–210 reinforce Article 14's limited reporting scope and continuation after support ends. Commission PDF remains authoritative.
- TI official product page confirms MSPM0 G-Series TRM Rev F dated 2026-11-05. Full PDF is about 25 MB and could not be opened in this environment. Revision metadata VERIFIED; security chapter/register-level content NOT_VERIFIED. No Rev F feature/register claim added.
- Protected files independently compared on main and cra-project-foundation: main.py blob SHA 86a7731aad5de8d75581fc953bcea2c44adf2f2b; .github/workflows/run.yml blob SHA 65a8cadc8eac593f551e390698e367b1d161ecf1. Both match across branches.
- Latest audit commit status endpoint returned no statuses; do not claim CI passed.


## TI MSPM0 G-Series TRM Rev F 접근 재점검 — 2026-11-12

- TI MSPM0G3507 공식 제품 페이지의 Technical documentation 목록에서 MSPM0 G-Series 80-MHz TRM Rev F / 2026-11-05를 재확인했다. 같은 목록에 MSPM0G350x/G150x Errata Rev H (2026-08-14), Cybersecurity Enablers in MSPM0 MCUs Rev B (2026-08-27)도 표시된다.
- TI 페이지의 MSPM0G3507 기능 요약에는 MPU, flash ECC, SRAM parity option, AES, TRNG, CRC, SWD 및 security descriptors가 표시된다. 이는 MSPM0G3507 페이지의 정보일 뿐 다른 SKU, 특히 MSPM0G3529-Q1에 자동 전이하지 않는다.
- TRM HTML viewer는 25,348,105 bytes로 렌더링 제한을 초과하고 PDF 직접 열기도 실패했다. Rev F metadata VERIFIED, Rev F body/security chapter/register details NOT_VERIFIED.
- TI SLAAE29 Rev B supported-device scope의 G3529-Q1 적용성 미확정 경고 유지. G3529-Q1 기능을 주장하려면 해당 SKU의 데이터시트·TRM·errata를 별도로 확인한다.
- 상세 source register §9 및 claim ledger TI-TRM-REVF-001..TI-SLAAE29B-APPL-001 참조.


## Main-only reports #56–#59 감사 — 2026-11-12

- 정정: 이전 점검에서 #55를 최신으로 기록했으나, 후속 commit search에서 main의 #56–#59가 확인되었다. 현재 main HEAD는 report #59 commit ee5c75840ee4868c7d3f56f3895c8bc7b50cfe44.
- #56 CONFLICT: Article 14 신고 범위를 actively exploited vulnerability 및 severe incident로 구분하지 않고 확대, 자동보고/수신기관 경로를 과장, 취약점 final report 14일과 severe incident final report 1개월의 차이를 누락.
- #57 PARTIALLY_VERIFIED: CVD 정책 및 contact address 요구사항 자체는 실재하지만 정확한 근거는 Annex I Part II(5),(6), user-facing single point of contact는 Annex II point 2. 보고서의 Part I Section 2 인용 및 원문 인용은 부정확.
- #58 PARTIALLY_VERIFIED: Secure-by-default Annex I Part I(2)(b), access control (d), attack surface (j)는 실재. 다만 모든 보조 포트/debug를 무조건 비활성화하거나 최초 부팅 비밀번호 변경을 법문이 직접 강제한다고 단정할 수 없음.
- #59 CONFLICT: Article 13(2)는 위험평가; 지원기간은 Article 13(8); 무상 보안 업데이트는 Annex I Part II(8); secure-by-default는 Part I(2)(b). 서로 다른 요건과 인용을 혼합.
- 배치 판정: PARTIALLY_VERIFIED 2 / CONFLICT 2 / fully VERIFIED 0. 상세 감사 및 4개 atomic claim row 추가.
- 공식 EUR-Lex 확인: Article 14 lines 939–975; Annex I lines 1743–1773; Annex II lines 1776–1794.
- 원본 main archive/history/state, main.py, Gemini prompt, production workflow는 수정하지 않았다.


## Repository integrity check after #56–#59 audit

- main HEAD remains report #59: ee5c75840ee4868c7d3f56f3895c8bc7b50cfe44.
- Current compare: cra-project-foundation is 319 commits ahead and 62 behind main (diverged). No sync, merge or rebase performed.
- main.py blob SHA matches both branches: 86a7731aad5de8d75581fc953bcea2c44adf2f2b.
- .github/workflows/run.yml blob SHA matches both branches: 65a8cadc8eac593f551e390698e367b1d161ecf1.
- Latest work-branch commit: 26be6cbaa1285a7e6bf616d8a2af899b428f964b. Combined status returned an empty statuses array; CI result is unknown/not reported.


## Main-only reports #60–#78 audit — 2026-11-12

- 새 commit sequence 확인으로 main의 최신 자동 생성 보고서가 #78임을 확인했다. #60–#78 원본 diff 19건을 가져와 EUR-Lex Regulation (EU) 2024/2847 원문과 대조했다.
- 결과: 6 PARTIALLY_VERIFIED (#60, #61, #63, #73, #76, #77), 13 CONFLICT, 0 fully VERIFIED. 모든 Raw Text Quote 블록은 verbatim 재사용 불가로 판정.
- 반복 오류: Article 11/13(6)/(7)/(8)/14 혼동, Part I(2)(g) 데이터 최소화를 취약점 업데이트로 오인, Part II(1)/(2)/(7)/(8) 혼합, 지원기간 5년 예외 누락, secure-by-default/attack-surface의 설계 선택을 보편적 법적 명령으로 과장, 합성·비문언 인용.
- 핵심 정정: support period=Article 13(8), CVD=Annex I Part II(5), contact address=Part II(6), secure distribution=Part II(7), free updates=Part II(8), secure-by-default=Part I(2)(b), attack surface=Part I(2)(j), data minimisation=Part I(2)(g), access control=Part I(2)(d).
- 상세 감사: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_60_78_2026-11-12.md). 원본 main archive/history/state는 수정하지 않았다.
- EUR-Lex checked: Article 13 lines 888–908; Article 14 lines 939–975; Annex I lines 1743–1773; Annex II lines 1776–1794.
- No merge/rebase/sync. No main.py/Gemini prompt/production workflow/run.yml edits. CI status not yet rechecked; do not claim pass.


## Main-only report #79 audit — 2026-11-12

- #79 commit 61d596354e1e4a700915306cecb1bc29f0828698 was discovered after #60–#78 batch completion.
- Verdict: PARTIALLY_VERIFIED. Article 14 reporting and 24-hour early warning are relevant, but the report broadens the reportable category, mislabels the 72-hour notification as a final notification, and misattributes/non-verbatim quotes Article 14(2).
- Correct active-vulnerability sequence: early warning ≤24h; vulnerability notification ≤72h; final report ≤14 days after corrective/mitigating measure becomes available. Severe incident has a separate 24h/72h/one-month track.
- Detailed audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_79_2026-11-12.md). Original main archive remains unchanged.
- Latest main report now #79; compare main vs work branch is diverged 329 ahead / 82 behind. No sync/merge/rebase.
- main.py and production run.yml blob hashes remain 86a7731aad5de8d75581fc953bcea2c44adf2f2b and 65a8cadc8eac593f551e390698e367b1d161ecf1 on main. Latest work-branch status query returned empty statuses; CI remains unknown.


## TI MSPM0G3529-Q1 functional safety evidence — 2026-11-12

- Located TI SFFS983A Rev A *Functional Safety Manual for MSPM0Gx51x and MSPM0Gx52x*, dated October 30, 2026; supported-device header explicitly includes MSPM0G3529-Q1.
- §2 states SEooC, developed to relevant ISO 26262:2018 requirements, systematic integrity ASIL D and random-fault mechanisms up to ASIL B. This is component-level evidence, not SIL 3 certification or a complete servo-drive claim.
- §4.3 assumptions include integrator-selected diagnostics from FMEDA/safety manual, host-provisioned actuator-disable mechanism, host communication-loss supervision, FTTI >10 ms, MPFDTI <8 h, random ASIL B and systematic ASIL D assumptions.
- §4.3 explicitly classifies DEBUG, RTC, AES, TRNG, KEYSTORE, MATHACL and DFT as QM/non-safety-critical for this safety concept; do not count them as safety mechanisms. Unprotected SRAM bank is excluded from safety-critical contexts; TI recommends no flash programming during safety-critical tasks.
- §6 lists 74 diagnostic/safety mechanism entries, but implementation and diagnostic coverage remain application/system integrator responsibilities.
- Detailed review: [TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md](TI_MSPM0G3529_Q1_FUNCTIONAL_SAFETY_REVIEW_2026-11-12.md). Source register §10 and claim ledger TI-SAFETY-001..005.
- TRM Rev F remains metadata-only; full body/security register details remain NOT_VERIFIED. No SIL 3 equivalence inferred.


## Final repository integrity check — 2026-11-12 15:29 KST

- Latest main HEAD remains report #79: 61d596354e1e4a700915306cecb1bc29f0828698. No #80+ report appeared in the latest commit search.
- Compare status: cra-project-foundation is diverged, 347 commits ahead / 82 behind main. No sync, merge or rebase performed.
- Protected file hashes match across branches: main.py 86a7731aad5de8d75581fc953bcea2c44adf2f2b; .github/workflows/run.yml 65a8cadc8eac593f551e390698e367b1d161ecf1.
- Latest work branch HEAD: 9c23c6922570593bf6c47eca66f02e1d2ec9ea06. Combined status returned an empty statuses array; CI/test pass is not established.


## TI safety mechanism integration mapping — 2026-11-12

- Created [TI_SAFETY_MECHANISM_SERVO_DRIVE_INTEGRATION_MATRIX_2026-11-12.md](TI_SAFETY_MECHANISM_SERVO_DRIVE_INTEGRATION_MATRIX_2026-11-12.md).
- Maps TI SFFS983A mechanism families (ADC/comparator/CPU/memory/flash/DMA/GPIO/PWM/watchdog/clock/BOR/CAN-FD/common-cause) to servo-drive IF-01..IF-09 and candidate evidence.
- All entries are design/test proposals only and NOT_RUN. No diagnostic coverage or system safety metric is inferred. Exact FMEDA and product-specific verification remain open.


## Main-only report #80 audit — 2026-11-12

- New main report #80 discovered at commit 78e73cb118d8bd9ca4ab7ec1433afe02c5b3eb12 after #79.
- Verdict: PARTIALLY_VERIFIED. Secure-by-default, access-control and attack-surface themes are supported by Annex I Part I(2)(b),(d),(j), but the report's Section 1(a)–(d) quote is composite/misnumbered and universal debug/port/password/Secure Boot mandates are overstated.
- Detailed audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_80_2026-11-12.md). Claim row CRA-ARCH-080-001 added. Original main archive remains unchanged.
- Latest main report now #80; continue checking for new commits before concluding an audit batch.


## Main-only reports #81–#121 audit — 2026-11-12

- Source main HEAD: #121, commit d0ba9802e4b7fead4192263d8ebd08f44a7c547e. Reports #81–#121 are 41 consecutive archive commits; full added report text was inspected from commit diffs.
- File-level verdicts: 33 CONFLICT / 8 PARTIALLY_VERIFIED / 0 VERIFIED. All 41 Raw Text Quote blocks rejected for verbatim reuse. This is a consecutive risk batch, not a random sample or archive-wide error rate.
- Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_81_121_2026-11-12.md).
- Main recurring defects: Article 13(8) support period conflated with Annex I Part II(8) free updates; under-five-year expected-use exception reversed/omitted; Article 14 misattributed as general vulnerability reporting/free-update clause; fabricated Annex I subpoints and composite raw quotes; universal Secure Boot/signature/rollback/default-password/port-disable mandates overstated.
- Correct map: Article 13(8) support period; Article 13(9) update retention after issuance; Annex I Part I(2)(b),(c),(d),(j) secure default/updates/access/attack surface; Annex I Part II(1)–(8) vulnerability handling; Article 14 actively exploited vulnerability and severe incident reporting; Annex II(2) contact point; Annex II(8)(d) secure decommissioning information.
- No source archive/history/state, main.py, Gemini prompt, production workflow, run.yml or main branch modifications. No merge/rebase/sync. No tests run; no CI PASS claimed.
- Branch compare at audit start: diverged, work branch 364 ahead / 124 behind main. Do not use old branch counts after new commits; recheck after final documentation updates.


## Main-only report #122 audit — 2026-11-12
- New main report #122 discovered at commit 39d614a760aebc98ce16fb534ddd75ddbcc5c1e3; source file research_archive/2026-11-12_100532.md.
- Verdict: CONFLICT. Secure-by-default/access-control/attack-surface themes are relevant, but Annex I Part I/II numbering and the Raw Text Quote are wrong/composite. Forced first-use password change, unique credentials, universal port disabling and RBAC are not prescribed as universal implementations by the cited text.
- Correct map: Annex I Part I(2)(b)=secure-by-default/reset; (d)=access control; (j)=attack surface. CVD=Part II(5), user-facing contact information=Annex II(2).
- Detailed audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_122_2026-11-12.md).
- Original main archive/history/state unchanged. No protected code/prompt/workflow changes, no merge/rebase/sync. No tests/CI PASS claimed.
