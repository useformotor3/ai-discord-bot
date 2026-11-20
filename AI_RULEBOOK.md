# AI 행동강령 — CRA 서보 드라이브 프로젝트

## 1. 역할과 언어
- 프로젝트 목표는 CRA 대응을 위한 적용성 조사·기술 설계·검증·문서화다.
- 주 문서 언어는 한국어다. 법령·표준·제조사 원문은 원어 그대로 보존한다.
- 생소한 용어는 최초 등장 시 한국어 설명과 약어를 함께 쓴다.
- 이 문서는 대화창의 기억보다 우선하는 프로젝트 작업 기준이다. 충돌 시 사용자에게 알리고 승인된 최신 문서를 따른다.

## 1A. 활성 프로젝트 범위 통제 — 최우선
- 활성 프로젝트는 **CRA 대응만**이다. 조사·코드·설계·보고서·자동화 개선은 CRA 목표에 직접 기여하는지 먼저 확인한다.
- SIL 3/IEC 61508/기능안전 벤치마킹 및 하드웨어 설계는 과거 별도 산출물이다. CRA 작업의 후속 단계로 추론하거나 자동 재개하지 않는다.
- SIL 3 파일, PR #16, 커밋 및 당시 로그는 역사적 기록으로 보존한다. 사용자 명시 재개 지시 전에는 수정·확장·추가 조사하지 않는다.
- 과거 문서/로그에 남은 SIL 3 '다음 단계' 표현은 이 범위 통제보다 우선하지 않으며, 현재 작업 계획으로 인용하지 않는다.
- 범위 판단 우선순위는 최신 사용자 명시 지시 → 본 행동강령의 최신 범위 통제 → 상황판/마스터 계획 → 과거 세션 로그다. 서로 충돌하면 최신 지시를 적용하고 문서들을 함께 정정한다.
- 세션 시작 시 README, 본 행동강령, PROJECT_STATUS, MASTER_PLAN, 최근 SESSION_LOG, PROJECT_LOG를 읽고 활성 범위와 다음 작업을 확인한다. 읽기/검증을 못한 문서는 읽었다고 주장하지 않는다.
- 최신 스냅샷 파일이 `PROJECT_STATUS_CURRENT.md`로 관리되는 경우 기존 `PROJECT_STATUS.md`와 혼동하지 말고 두 파일의 역할/최신성 및 README 링크를 확인한다. 최신 재개 기준은 `PROJECT_STATUS_CURRENT.md`와 최근 main merge 기록을 우선한다.

## 2. 근거 규칙
- 법령 주장은 EUR-Lex 등 공식 원문을 우선한다.
- 각 주장에 규정 번호, 조항/Annex/point, 원문 링크, 확인 날짜를 남긴다.
- 원문 인용은 실제 출처에서 확인한 문장만 쓴다. AI가 재구성한 문장을 인용문으로 표시하지 않는다.
- 표준은 공식 발행기관의 공개 범위에서 확인하고, 유료 전문을 읽지 못했으면 읽은 것처럼 쓰지 않는다.
- 제조사 문서·블로그·2차 자료는 보조자료로 구분한다.
- 근거를 찾지 못하면 '미확인'으로 표시하고 의무라고 단정하지 않는다.
- 중요한 법적·기술적 결론은 가능한 경우 독립된 공식 자료 또는 별도 근거로 교차 확인한다.
- Commission Guidance처럼 내부 승인 문서번호와 Official Journal 게재번호가 다른 경우 둘을 구분해 기록한다. 현재 공식 인용은 OJ C/2026/6013 (CELEX 52026XC06013), C(2026) 5252는 2026-07-27 승인/게시 이력이다. OJ PDF를 최신 인용·page locator의 primary source로 사용하고, 과거 mirror/초안은 별도 source ID·hash로 보존한다. raw-byte 또는 extracted-text hash가 다르면 byte/text identity를 주장하지 않는다.
- CRA 법적 보고서를 작성/갱신하기 전에는 EUR-Lex OJ 원문과 현재 consolidated/amending acts, Commission CRA implementation/guidance/FAQ, 표준화 현황 및 OJ 조화표준 공표, ENISA 신고 플랫폼 자료의 최신 상태를 확인한다. 표준화기구 납품 일정과 법령 적용일을 혼동하지 않는다.
- 법령 개정의 적용일과 대상 제품 범위를 확인한다. 고위험 AI/EHR 등 특정 제품군에 한정된 개정은 일반 산업용 서보 드라이브에 자동 확장하지 않는다.

## 3. 분류 규칙
모든 결과를 다음 중 하나로 표시한다.
- 법적 의무(규정 원문으로 확인)
- 표준 요구사항(표준의 정확한 판·조항 확인)
- 공식 가이드/해석
- 엔지니어링 권고
- 가설/추가 확인 필요

## 4. CRA와 제품 적용성
- 서보 드라이브가 CRA 적용 대상이라고 무조건 단정하지 않는다.
- 제품의 디지털 요소, 시장 출시 주체, 의도된 용도, 별도 구성요소 판매 여부, 다른 EU 법령과의 관계, 예외를 확인한다.
- 산업용 제어 시스템이라는 이유만으로 CRA 분류 등급이나 제3자 적합성 평가 의무를 단정하지 않는다.
- 지원기간 5년은 일반적 최소 기준 문구와 제품의 예상 사용기간 예외를 함께 설명한다. 산업용 제품의 예상 사용기간이 5년보다 길다면 그 기간을 검토한다.

## 5. 검증과 문서화
- 보고서 자동 생성과 사실 검증을 별도 단계로 관리한다.
- 각 조사 항목에 주장, 근거, 원문, 해석, 적용성, 반대 근거/제약, 검증 상태를 기록한다.
- 중복 주제는 재작성하지 말고 기존 자료를 정정·보완한다.
- 수정 전 원본을 보존하고 정정 이력을 남긴다.
- 단일 통합 보고서와 필요한 부속서만 유지해 문서가 과도하게 쪼개지 않도록 한다.
- 한국어 본문, 공식 영문 원문, 근거 링크, 검토 기록을 상호 연결한다.
- 초안/구조 검증/출처 확인/전문가 검토/승인 상태를 구분하고, 미검증 초안을 최종 결론처럼 표현하지 않는다.

## 6. 코드·운영 변경
- 운영 `main.py`, workflow, secrets, 운영 데이터는 영향분석·백업/복구·테스트 없이 변경하지 않는다. CRA 범위 안의 통상적인 문서/코드 작업은 매번 사용자에게 반복 승인 요청하지 않고 작업 브랜치·PR·롤백 경로를 갖춰 진행한다.
- `main` 직접 수정은 기본 경로로 사용하지 않는다. 문서 정정 등 필요한 경우에도 변경 전 기준점, 최소 diff, 복구 방법, 사후 readback을 기록한다. 운영 workflow 실행·secret 변경·데이터 삭제 등 고위험 작업은 별도 안전 확인을 한다.
- 변경은 작업 브랜치에서 수행하고 mock 테스트부터 진행한다.
- 실패를 성공으로 기록하지 않는다. 생성 성공·전송 성공·저장 성공·근거 검증 성공을 분리한다.
- 외부 API 호출은 timeout, 재시도, 상태 코드, rate limit을 처리한다.
- secret은 코드·로그·보고서·이력에 출력하지 않는다.
- 변경 전후 diff, 테스트 결과, CI 링크, 롤백 방법을 기록한다.
- 테스트가 실제 실행되지 않았으면 '테스트 추가' 또는 '정적 검토'로만 표시하고 '통과'라고 쓰지 않는다.
- mock/helper 테스트 결과를 전체 저장소 테스트, 통합 테스트, CI 또는 운영 실행 결과로 확대 해석하지 않는다.

## 7. ST MCU 및 TI 비교
- 기본 설계 기준은 ST MCU 중심으로 작성한다.
- TI는 대체/비교 솔루션으로 동일한 기준(보안 기능, 안전 문서, 툴체인, 수명주기, 비용/가용성)을 적용해 비교한다.
- 특정 MCU 기능이 CRA 적합성을 자동 보장한다고 표현하지 않는다.
- 데이터시트·레퍼런스 매뉴얼·보안 매뉴얼·안전 매뉴얼 등 1차 자료를 근거로 한다.

## 8. 기능안전 경계
- CRA 사이버보안과 SIL 기능안전은 상호 영향이 있을 수 있지만 동일한 인증/요구사항이 아니다.
- 기능안전 관련 변경은 별도 안전 분석·검증·승인 없이는 적합성 결론을 내리지 않는다.

## 9. 프로젝트 기록 및 작업 연속성 — 필수
- 대화창의 문맥이나 모델 기억만을 프로젝트의 유일한 기록으로 사용하지 않는다.
- 의미 있는 작업 단위가 끝날 때마다 작업 브랜치의 GitHub 문서를 실제 갱신한다.
- 문서 역할을 분리해 중복·불일치를 줄인다.
  - `README.md`: 프로젝트 메인 페이지, 현재 상태 요약, 문서/산출물 진입점
  - `PROJECT_STATUS.md`: 현재 사실, 진행 상태, 위험, 다음 재개 지점이 있는 상황판
  - `MASTER_PLAN.md`: 목표, 우선순위, 단계별 완료 기준과 실행 순서
  - `AI_RULEBOOK.md`: 조사·검증·코드·문서화 행동강령
  - `SESSION_LOG.md`: 날짜별 수행 내용, 변경 파일, 검증 결과, 미완료 사항
  - `reports/`: 상세 감사·설계·정정·통합 기술 보고서
- 코드/조사 변경이 있으면 관련 보고서와 위 관리 문서 간 링크 및 상태를 함께 갱신한다.
- GitHub 파일을 수정한 뒤 동일 브랜치에서 다시 읽어 내용과 저장 여부를 확인한다. 저장 성공 응답만으로 검증 완료라고 하지 않는다.
- 작업 보고에는 반드시 실제 변경 파일, 커밋/저장 확인, 테스트 범위와 결과, 미실행 항목, 운영 영향, 다음 단계의 승인 필요 여부를 구분한다.
- 작업 브랜치와 운영 `main`의 차이를 확인하고, 자동 생성 데이터 손실 위험이 있으면 무리하게 merge/rebase하지 않는다.
- 작업을 시작할 때 이 문서와 README, 상황판, 마스터 계획, 최근 세션 로그를 기준으로 재개한다.
- 사용자에게 승인받지 않은 범위로 코드를 확장하지 않는다. 다만 문서·상황판의 사실 정합성 갱신은 기존 승인 범위 내에서 수행한다.

## 10. 객관적 우선순위
우선순위는 다음 기준으로 정한다.
1. 운영 데이터/비밀정보/안전 기능에 대한 손상 위험
2. 잘못된 법적·기술적 결론이 보고서로 확산될 위험
3. 재현성과 테스트 가능성, 장애 복구 가능성
4. 다른 작업을 막는 선행 조건
5. 사용자 최종 산출물에 대한 가치
6. 구현 비용과 유지보수 복잡도

빠르게 많은 파일이나 코드를 만드는 것보다, 선행 위험을 줄이고 검증 가능한 산출물을 누적하는 방식을 우선한다.


## 11. 테스트 원본성 및 부작용 검증 추가 규칙
- 테스트 실행 전 대상 브랜치, commit SHA, 각 핵심 소스 파일의 Git blob SHA를 기록한다.
- 로컬 테스트 사본은 GitHub에서 조회한 원본과 blob SHA가 일치할 때만 해당 브랜치 소스 테스트로 인정한다. 일치하지 않으면 예비 검증으로만 기록한다.
- mock은 성공 응답만 흉내 내서는 안 된다. HTTP timeout/429/4xx/5xx/네트워크 오류, Git 명령의 non-zero exit와 check=True 예외, 부분 전송 및 재시도 경로를 별도 검증한다.
- 테스트 fixture가 항상 성공을 반환하거나 실패 예외를 무시하면 그 경로는 검증되지 않은 것으로 명시한다.
- 운영 workflow를 테스트 목적으로 실행하지 않는다. CRA 범위 내 테스트 전용 workflow/CI 변경은 반복 승인 질문 없이 격리 브랜치와 PR에서 진행할 수 있다. 운영 workflow의 실제 실행, Gemini/Discord 외부 부작용, 유료 API 비용 발생은 테스트와 분리하고 별도 안전 확인 없이 실행하지 않는다.
- 정적 검토, helper 단위 테스트, 원본 전체 pytest, CI, 운영 실행을 서로 다른 검증 단계로 구분한다.
 
## 12. 이중 형식 프로젝트 로그
- 프로젝트 변경 이력은 `PROJECT_LOG.jsonl`과 `SESSION_LOG.md`에 함께 남긴다.
- JSONL은 한 줄에 하나의 완전한 JSON 객체를 기록한다. 최소 필드: `event_id`, `date`, `kind`, `status`, `summary_ko`, `branch`, `files`, `verification`, `limitations`, `approval`.
- 실행·검증 사건에는 가능한 경우 `commit`, `evidence`(CI/PR/공식 근거 링크)를 추가한다. 미실행 항목을 성공으로 기록하지 않는다.
- `SESSION_LOG.md`에는 배경, 판단 이유, 상세 절차, 검증 범위와 미해결 사항을 한국어로 기록한다.
- 두 로그는 같은 사건 ID 또는 명확한 상호 링크로 연결하고, 값이 충돌하면 원본 증거를 재조회해 정정한다.
- `state.json`·`history.json`은 기존 운영 자동화 데이터이며 프로젝트 작업 로그와 분리한다. 별도 승인 없이 변경하지 않는다.


## 13. 브랜치·커밋·변경 추적 규칙
- 운영 `main`은 직접 수정하지 않는다. 작업 목적별 짧고 명확한 feature/test/docs 브랜치를 만들고, 생성 시 기준 브랜치와 기준 commit SHA를 기록한다.
- 작업 시작 전에 기준 HEAD, 대상 파일 blob SHA, 현재 `main` 대비 ahead/behind 및 merge-base를 확인한다.
- 변경 단위마다 승인 범위, 파일별 변경 전·후, 변경 이유, 예상 영향, 테스트 계획, 복구 방법을 기록한다.
- 커밋은 논리적 작업 단위로 묶고 `test:`, `fix:`, `ci:`, `docs:` 등 의미가 분명한 메시지를 사용한다. 파일 단위 API로 작은 커밋이 불가피하면 그 이유를 세션 로그에 명시한다.
- CI는 실행 commit SHA와 핵심 소스 blob SHA를 대조한다. 단순히 최신 run이 성공했다는 이유로 다른 commit의 코드를 검증했다고 주장하지 않는다.
- 작업 완료 후 기준점 대비 파일 diff, branch HEAD, CI run, main 대비 diverged 상태를 다시 조회한다.
- 실패한 시도와 수정 내역도 감추지 않고 기록한다. 복구는 우선 revert commit으로 하며, force push·history rewrite는 금지한다.
- 사용자는 CRA 목표 달성에 필요한 통상적·가역적 코드/문서/CI 변경, PR 생성 및 검증 후 병합을 반복 승인 질문 없이 진행하도록 상시 승인했다. 단, 정확한 head SHA의 CI 성공, diff/readback, 충돌/보호 경로 확인 및 rollback ref를 확보한 경우에만 병합한다.
- 삭제·비밀정보/권한 변경·운영 workflow 실행·외부 유료/비가역 효과 등은 이 상시 승인에 포함된다고 추정하지 말고 별도 안전 확인을 한다.


## 14. HTTP POST·재시도·부분 성공 안전 원칙
- 외부 POST 요청은 timeout을 명시하고 HTTP 응답 성공 여부를 확인한다.
- 응답 유실 시 서버가 작업을 반영했는지 불명확할 수 있다. idempotency 보장 없이 timeout/5xx POST를 자동 재전송해 중복 작업을 만들지 않는다.
- Discord 429는 공식 Retry-After/retry_after를 준수하고, 400/401/403/404 등 영구 오류는 반복 요청하지 않는다.
- chunk 전송은 파트별 확인 상태를 유지하고 일부 성공을 전체 성공으로 표시하지 않는다.
- 파일별 atomic replace가 여러 파일을 하나의 transaction으로 만드는 것은 아니다. state/history 복구 journal 또는 동등한 일관성 설계를 검증한다.
- P1-B2는 2026-11-16 사용자 승인으로 작업 브랜치 구현 및 CI 검증을 완료했다. P1-B3/B4와 운영 반영은 별도 승인 전 금지한다.


## 15. P1-B1 Discord webhook 전송 구현 원칙
- webhook POST는 connect/read timeout과 wait=true를 사용한다.
- 2xx 응답이라도 message ID 확인 전에는 성공으로 기록하지 않는다.
- ConnectTimeout만 제한 재시도하고 ReadTimeout/일반 ConnectionError/5xx는 delivery_unknown으로 분류해 중복 전송을 피한다.
- 429는 Retry-After/retry_after를 따르며 재시도 횟수와 대기 예산을 제한한다.
- 400/401/403/404는 영구 실패로 분류하고 재시도하지 않는다.
- chunk별 성공 ID를 보존하고 일부 성공 후 실패는 partial로 표시한다.
- 전송 상태의 영속화는 P1-B2/B3에서 별도 설계·승인한다.
- P1-B1과 P1-B2는 각각 별도 사용자 승인을 받아 작업 브랜치 구현 및 테스트 전용 CI 검증을 완료했다. P1-B3/B4 및 운영 workflow 변경·운영 배포는 승인된 것으로 간주하지 않는다.


## Git 통합 감사 규칙 추가 — 2026-11-16
- GitHub compare API의 변경 파일 목록이 300개에서 잘릴 수 있으므로 대규모 분기에서는 이를 전체 목록으로 간주하지 않는다. recursive Git tree 조회와 blob SHA 비교로 전체 경로 차이를 교차검증한다.
- 운영 브랜치의 `state.json`, `history.json`, 자동 생성 archive는 코드 변경과 별도 보존 자산이다. 별도 데이터 migration 승인 없이 작업 브랜치의 파일로 덮어쓰지 않는다.
- ahead/behind, HEAD, merge-base는 조회 시점의 스냅샷이다. 병합 판단 직전에 다시 조회한다.
- CI 성공은 코드/테스트 범위의 검증 증거일 뿐 운영 데이터 보존, 법적 적합성 또는 기능안전 인증을 증명하지 않는다.


## P1-B2 저장 설계 승인 경계 — 2026-11-16
- archive/state/history의 atomicity는 파일별 os.replace만으로 다중 파일 transaction이 되지 않는다. durable journal, staged payload, old/new SHA 검증, idempotent recovery를 함께 설계한다.
- 손상된 journal/stage 또는 예상하지 못한 target SHA를 발견하면 자동 초기화·덮어쓰기하지 말고 fail-closed 한다.
- P1-B2는 로컬 저장 일관성만 다룬다. Discord exactly-once/outbox와 Git sync status를 보장하지 않는다.
- 이 문장은 P1-B2 설계 승인 이전의 경계 기록이다. 2026-11-16 사용자 승인 후 작업 브랜치 구현과 테스트 CI 검증을 완료했다. 운영 main/data/run.yml 변경과 PR merge/운영 배포는 여전히 별도 승인 대상.


## 16. P1-B2 durable persistence 구현 기준 — 2026-11-16
- `research_archive/`, `history.json`, `state.json`을 한 transaction ID로 묶고 PREPARED/APPLYING/COMMITTED journal을 사용한다.
- stage/backup/manifest/journal은 SHA 검증과 fsync를 수행한다. target 교체는 같은 디렉터리의 임시 파일과 os.replace를 사용하고 directory fsync를 수행한다.
- 시작 시 pending transaction recovery를 state/history 읽기 및 외부 API 호출보다 먼저 수행한다.
- commit 시 처음 읽은 raw bytes snapshot SHA와 현재 target SHA를 비교해 동시 변경을 덮어쓰지 않는다.
- journal/stage/backup 손상, 잘못된 경로, target SHA mismatch, lock 획득 실패는 fail-closed 한다. 자동 초기화·임의 복구·덮어쓰기를 금지한다.
- POSIX `fcntl.flock` 및 directory fsync 지원 환경을 전제로 한다. Windows 지원을 주장하지 않는다.
- lock은 recovery/commit 구간에 한정한다. 외부 API 호출 구간까지 잠그지 않으므로 Discord exactly-once 또는 중복 전송 방지는 제공하지 않는다.
- P1-B2 최신 보강 CI Actions 43851438733: source SHA 일치, compileall 통과, 70 passed / 1 xfailed. xfail은 P1-B3 범위다.


## 17. P1-B2 persistence target 제한 및 통합 기준 — 2026-11-16
- Recovery manifest가 지정할 수 있는 target은 `state.json`, `history.json`, `research_archive/*.md`로 제한한다.
- 저장소 내부 경로라는 이유만으로 README, 코드, workflow, `.git` 등 임의 파일을 persistence transaction target으로 허용하지 않는다.
- 이 allowlist는 신규 transaction 생성과 기존 journal recovery 양쪽에서 강제하고, 허용 범위 밖 target은 fail-closed 한다.
- merge-base 기준 tree diff로 운영 archive/state/history 보존 여부를 확인한다. 현재 tree 간 직접 차이를 삭제 기록으로 오인하지 않는다.
- PR은 pull_request 전용 mock CI로 검증한다. PR CI에 운영 secrets, Gemini/Discord 호출, 운영 workflow 실행을 포함하지 않는다.
- 코드 통합, 운영 workflow 변경, 실제 운영 실행/배포는 서로 다른 승인 경계로 유지한다.


## 18. 사용자 상시 진행 승인 및 복구 우선 운영 — 2026-11-16

### 18.1 진행 권한
- 사용자는 반복적인 단계별 승인 질문 없이 목표 달성에 필요한 조사, 설계, 구현, 테스트, 문서화, 브랜치/커밋/PR 관리 및 안전한 통합 작업을 계속 진행하도록 상시 승인했다.
- 기존 문서의 '매 단계 별도 승인' 문구는 이 상시 승인과 충돌하는 범위에서 이 조항으로 대체한다.
- 이 승인은 안전 통제를 생략하라는 뜻이 아니다. 위험이 큰 작업은 먼저 격리·백업·검증하고, 되돌릴 수 없는 외부 부작용은 자동 진행하지 않는다.

### 18.2 변경 전 체크포인트
- 모든 의미 있는 변경 전에 원격 main과 작업 브랜치의 HEAD SHA, merge-base, ahead/behind, 대상 파일 blob SHA를 기록한다.
- main에 통합하기 전 현재 main과 통합 대상 feature HEAD를 가리키는 별도 safety/ 백업 브랜치를 만든다. 백업 ref를 다시 읽어 SHA를 검증한다.
- 커밋은 논리적 변경 단위로 묶는다. 기존 커밋을 덮어쓰는 force-push/rebase는 기본 금지하며, 복구는 revert commit 또는 별도 복구 브랜치로 수행한다.
- 운영 데이터가 변경될 수 있는 실행 전에는 state.json, history.json, research_archive/의 스냅샷/체크섬/개수/참조 무결성을 확보한다. 백업을 실제 복원할 수 있는지 검증하지 못했다면 신규 코드의 운영 실행을 보류한다.

### 18.3 통합 및 실행 게이트
- PR 통합은 최신 base 기준 충돌 상태, PR 전체 diff, 보호 경로, 정확한 head SHA의 PR CI를 재확인한 후 수행한다.
- 기본 통합 방식은 merge commit이다. squash/rebase/force-push는 이력 추적과 복구를 약화시키므로 사용하지 않는다.
- 통합 후 main HEAD, merge commit, changed paths, workflow 결과를 재조회한다.
- 운영 실행 전 compile/test/정적 검사 외에 입력 데이터 사전검사와 데이터 백업을 수행한다. 실행 후 state count/date, history 증가량, archive 파일 수, history→archive 참조 무결성, 로그 및 외부 전송 상태를 점검한다.
- 문제가 발생하면 추가 실행/재시도를 중단하고 증거를 보존한다. 코드 문제는 직전 정상 merge commit으로 revert하고, 데이터 문제는 검증된 백업에서 별도 복구 commit으로 복원한다.
- Discord 등 외부 전송은 이미 전달된 메시지를 Git revert로 회수할 수 없다. 중복 전송 위험이 있으면 자동 재전송하지 않고 상태를 delivery-unknown으로 남긴다.

### 18.4 중단 조건과 보고
- 테스트 실패, 원본 SHA 불일치, 보호 경로의 예상 밖 변경, 백업/복원 검증 실패, 데이터 무결성 저하, secret 노출 징후가 있으면 해당 단계에서 중단하고 원인을 조사한다.
- 중단은 사용자에게 다시 승인받기 위한 절차가 아니라 데이터/서비스 손상을 막기 위한 안전 정지다. 복구 가능한 범위는 계속 자동으로 수행한다.
- 매 세션 종료 시 기준/현재 SHA, 커밋, 파일 diff, CI 링크, 백업 ref, 복구 방법, 실행 여부 및 남은 위험을 README·PROJECT_STATUS·SESSION_LOG·PROJECT_LOG에 기록한다.

### 18.5 현재 안전 체크포인트
- PR #26 pre-merge main checkpoint: `safety/pre-merge-main-pr26-2026-11-17` → `f4bb159e164b00e4586868f335519cea3c4802ae` (readback verified).
- PR #26 post-merge main checkpoint: `safety/post-merge-main-pr26-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854` (readback verified).
- PR #27 pre-merge main checkpoint: `safety/pre-merge-main-pr27-2026-11-17` → `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`; post-merge checkpoint: `safety/post-merge-main-pr27-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b` (both readback verified).
- PR #28 pre-merge main checkpoint: `safety/pre-merge-main-pr28-2026-11-17` → `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; post-merge checkpoint: `safety/post-merge-main-pr28-2026-11-17` → `942e1e6b5f2887001279a96c21f94138d283a689` (both readback verified).
- 과거 pre-integration refs는 역사적 checkpoint로 보존한다.
- PR #26은 코드/테스트/CI 통합이며 운영 Gemini/Discord 실행이나 state/history/archive 변경을 수행하지 않았다. 운영 데이터 snapshot/restore 검증은 별도 미완료이므로 새 코드를 실제 운영 실행하기 전에는 백업·복원 검증을 별도로 수행한다.

## 19. 운영 데이터 기준선 감사 결과 — 2026-11-16
- immutable main snapshot 4cf0e708b28a343898af00d01521044dfb9a1987 기준 state count=158, history=2,297, archive=2,297, 참조 누락 0.
- U+200B ZERO WIDTH SPACE가 앞에 붙은 별도 state.json(date=2026-06-07,count=0)은 원인 확인 전까지 보존한다.
- safety/pre-merge-main-4cf0e70가 위 immutable main commit을 정확히 가리키는 것을 확인했다.
- moving ref를 서로 다른 API 호출에서 조회하면 자동 아카이브 사이에 snapshot race가 생길 수 있다. 데이터 감사는 먼저 HEAD SHA를 고정한다.
- 이전 history/archive 1건 차이는 동일 immutable SHA 재검사에서 재현되지 않아 moving-ref race로 정정했다.
- per-run 자동 데이터 백업/복원 리허설은 아직 미완료다.

## 20. 운영 실행 checkpoint/복구 guard 구현 — 2026-11-16
- production run workflow는 실행 직전 현재 main HEAD를 고유 safety/data-pre-run-{run_id}-{attempt} 브랜치로 보존한다.
- production workflow concurrency group으로 중복 실행을 직렬화한다.
- main.py 실행 뒤 operational_guard.py가 baseline/current commit parent, remote main HEAD, changed paths, state/history/archive append-only, 새 보고서 1건, count 및 참조 무결성을 확인한다.
- 검증 실패 시 remote main이 해당 실행의 단일 child commit일 때만 state/history/archive를 baseline으로 복구하는 새 commit을 push한다. force-push는 사용하지 않는다.
- remote main이 baseline 또는 다른 commit이면 자동 복구하지 않고 fail-closed 한다. checkpoint는 보존한다.
- quota 등 clean no-op은 local/remote HEAD가 baseline과 같고 data path가 clean할 때만 허용한다.
- local bare Git remote integration tests로 정상 전이, 손상 후 restore commit, 미push 거부, quota no-op을 검증했다.
- CI Run 43873774430에서 fixture 오류 1건(80 passed, 1 failed, 1 xfailed)을 발견해 수정. 최종 Run 43874801395에서 86 passed, 1 xfailed 및 compileall 통과.
- 최종 Run은 base f5b5a112ec72b01f8b3f91f734b8d755dde416c6, head 8ad2364992cfd0e4f60108d4bfcdf36e99d9131e 기준 성공.
- 이는 데이터 구조 무결성 검사이며 CRA 법적 적합성 또는 외부 Discord 전달의 회수 가능성을 보장하지 않는다.


## 21. 최신 rollback guard 보강 및 통합 기준 — 2026-11-16
- _current_snapshot은 state/history/archive root의 symlink를 거부하고, 누락/읽기 오류를 GuardError로 바꿔 검증 실패 시 조건부 복구 경로로 보낸다.
- empty archive file도 무결성 오류로 처리한다.
- missing state file 통합 테스트를 추가해 baseline restore commit으로 복구되는 경로를 검증했다.
- 최신 PR CI Run 43875746973: 87 passed, 1 xfailed, compileall 성공; base main SHA adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890, head abee2a88f7e0bbfad0ad483c6b50cea63e26b871.
- main #162 backup safety/pre-merge-main-adf74ea -> adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890, readback exact.
- main #162 same-SHA baseline: state count=162, history=2,301, archive=2,301, missing refs=0.
 

## 22. PR #1 통합 후 운영 기준 — 2026-11-16
- PR #1은 merge commit으로 통합했다. merge commit 6fd03efaf8623cb3ec2ab938aa7161b41ffed82e, 부모는 main baseline adf74eaa6bfb102b661ea9e3e6d9ee84eaa4f890 및 feature head d48ae1c9b655d7384aff497c9d17168a5d0b25c5.
- merge 직전 main/feature 백업 ref 및 merge 직후 post-merge backup ref를 생성하고 readback SHA를 검증했다.
- merge 직후 push-triggered CI Run 43876347620 성공: 87 passed, 1 xfailed, compileall 성공.
- merge 직후 동일 SHA 데이터 검사: state count=162, history=2,301, archive=2,301, missing refs=0. state/history blob SHA는 pre-merge main #162와 동일.
- production run.yml의 pre-run snapshot 및 post-run guard가 main에 반영됐다. workflow는 repository_dispatch/workflow_dispatch만 트리거하므로 merge 자체가 Gemini/Discord 운영 실행을 유발하지 않았다.
- 실제 Gemini/Discord 운영 실행은 아직 하지 않았다. 첫 실행 전후 snapshot branch·데이터 무결성을 확인한다. Discord 메시지는 외부 전송 후 회수할 수 없다.


## 2026-11-17 — 운영 workflow와 main 변경의 상호 배제
- Production workflow가 queued/in_progress인 동안에는 main에 코드·workflow 커밋을 올리지 않는다.
- main 변경 전 최신 Actions run을 조회하고 production workflow의 active run이 0건임을 확인한다. 변경 후에는 push-triggered CI가 완료될 때까지 production workflow dispatch/외부 trigger와 충돌하지 않도록 한다.
- 실행 중 main이 이동하면 run의 Git push가 non-fast-forward가 될 수 있다. 운영 데이터 커밋을 강제 push하거나 무조건 자동 복구하지 않는다.
- checkpoint cleanup은 post-run guard가 성공한 경우에만 수행한다. 실패·복구 상황의 baseline ref는 정리하지 않는다.
- Discord 전송 후 Git 저장이 실패하면 외부 전송은 되돌릴 수 없다. 동일 count/내용을 재전송하기 전에 기존 Discord 전달 결과를 확인하고 중복 위험을 기록한다.


## 2026-11-17 운영 시간·외부 API·저장 실패 원칙
- 일일 CRA count 및 archive timestamp의 기준 시간대는 Asia/Seoul로 고정한다. 실행 runner의 OS 기본 시간대에 의존하지 않는다.
- legacy naive health-check timestamp는 이전 GitHub-hosted runner가 기록한 UTC로 해석한다. 신규 timestamp는 timezone-aware ISO 형식으로 기록한다.
- Gemini 모델 ID는 공식 Google AI for Developers 모델 카탈로그에서 확인한다. 404/NOT_FOUND는 동일 모델을 재시도하지 않고 다음 허용 모델로 전환한다. 429/5xx 등 일시 오류는 제한된 재시도 정책을 사용한다.
- Git add/commit/push 실패는 경고만 남기고 성공 종료하지 않는다. 강제 push, force update, 자동 rebase로 운영 main을 덮어쓰지 않는다.
- Discord 전송 후 Git 저장이 실패할 수 있다. 이 경우 Discord 전달을 취소할 수 없으므로 archive 누락과 중복 전송 위험을 명시적으로 추적한다.

- 2026-11-17 CI Run #59에서 KST/model/Git fail-closed 변경이 99 passed, 1 xfailed로 통과했다. 단, 실제 Gemini/Discord 운영 API 호출 결과와 KST 적용 후 첫 일일 경계는 별도 관찰 전까지 검증 완료로 주장하지 않는다.
## 42. 자동 생성 보고서의 출처·중복 품질 게이트
- CRA 법적 주장 보고서는 Regulation (EU) 2024/2847 공식 EUR-Lex OJ 링크를 포함해야 한다. 링크 존재는 원문 정확성 증명이 아니므로 중요한 인용·조항은 별도 원문 대조를 수행한다.
- 최근 archive 원문과 주제 유사도를 비교해 중복 주제를 전송/아카이브 전에 차단한다. 휴리스틱 판정은 정기적으로 false positive/negative를 검토한다.
- 주제 중복이거나 검증된 신규 주제가 없으면 새 보고서를 억지 생성하지 않는다.
- 법령 조항 번호, 제목, 원문 인용은 EUR-Lex final OJ를 기준으로 한다. 초안·2차 자료 문언을 final OJ 직접 인용으로 표시하지 않는다.

## 43. 운영 자동화 실행 주기 및 변경 안전
- 외부 event dispatcher가 과도한 빈도로 호출해도 운영 workflow가 그대로 실행되도록 두지 않는다. production cadence는 명시된 schedule로 관리하고 운영 주기 변경은 상황판·세션 로그에 기록한다.
- 운영 workflow 변경 전 현재 실행이 완료됐는지 확인하고, 변경 후 isolated CI와 workflow trigger 회귀 테스트를 통과시킨다.
- workflow의 동시성 `cancel-in-progress: false`, immutable pre-run checkpoint, operational guard, checkpoint pruning을 유지한다.
- 운영 실행 결과가 성공이라고 해서 보고서의 법적 정확성까지 검증된 것으로 표현하지 않는다.
## 44. 실패 경로 복구 및 외부 전송 순서
- 각 production run은 immutable pre-run data checkpoint를 먼저 생성한다.
- checkpoint 생성 성공 후 main.py의 성공/실패와 무관하게 operational guard를 실행한다.
- dirty uncommitted data는 baseline checkpoint에서 복원하고, unpublished local data commit은 remote main이 baseline 그대로일 때만 local reset한다.
- remote main이 독립적으로 전진했다면 force-push나 자동 덮어쓰기를 절대 수행하지 않는다.
- 이미 원격에 잘못 push된 단일 child commit은 기존 rollback commit 경로로 복원하고 검증한다.
- checkpoint pruning은 operational guard가 성공한 경우에만 수행한다. guard 실패 시 checkpoint를 보존한다.
- Discord 등 외부 알림은 GitHub archive/state/history commit+push 성공 후 전송한다. 외부 전송 실패가 원본 데이터 손실로 이어지지 않게 한다.

## 45. CRA 법령 인용·조항 식별 기준
- 최종 기준은 Regulation (EU) 2024/2847 Official Journal이다. 이전 초안/최종 타협안의 번호·문구를 final OJ 직접 인용으로 사용하지 않는다.
- Article 10은 cybersecurity skills, Article 11은 general product safety, Article 13은 manufacturer obligations, Article 14 mandatory reporting, Article 15 voluntary reporting, Article 16 single reporting platform이다.
- 기술문서는 Article 31/Annex VII, 사용자 지침은 Article 13(18)/Annex II, support-period end-date 표시 Article 13(19)로 추적한다.
- Article 13(8) support period와 Article 13(9) security update availability는 다른 기간이다.
- Annex I Part I는 제품 속성 요구, Part II는 vulnerability handling 요구다. CVD는 Part II (5)/(6), logging은 Part I (2)(l), data integrity는 Part I (2)(f).
- 제품 Annex III Class I/II 분류는 목록에 열거된 카테고리와 core functionality를 대조한다. 산업용/서보 드라이브라는 명칭만으로 등급을 추정하지 않는다.
- 법령 직접 의무와 구현 선택(PGP, security.txt, CVE/SLA, unique credentials, WORM/SIEM, digital signature 등)을 분리한다.

## 46. 기능안전 제품 벤치마킹과 표준 판본
- 제조사 제품군 이름만으로 SIL/PL 등급을 부여하지 않는다. 정확한 model, firmware, safety module, motor/encoder, safety controller, communication and license configuration을 명시한다.
- Drive/module PFH와 complete safety function PFH를 구분한다. 서로 다른 certification scope의 PFH를 직접 순위화하지 않는다.
- STO를 electrical isolation, controlled stop, mechanical holding brake와 동일시하지 않는다.
- 최신 IEC 61800-5-2 amendment와 제조사 인증서 판본을 대조한다. 구판 매뉴얼의 proof-test/diagnostic interval을 최신 규격 요구로 자동 전용하지 않는다.
- 전압/출력/부하/축 수/피드백/안전 기능이 미확정이면 parameterized reference architecture로 표시하고 최종 회로/BOM/PFH를 확정하지 않는다.
- 기능안전 FS traceability와 CRA cybersecurity CYB traceability는 별도 요구사항 ID와 증거 체계로 유지한다.

## 47. 제조사 안전 권고와 firmware revision
- SIL/PL 인증 주장을 검토할 때 제품 안전 권고(PSA/PCN), affected catalog numbers, installed firmware 및 safety-path configuration을 함께 조회한다.
- 출하 시 명판 firmware와 현장 설치 firmware가 다를 수 있으므로 실제 설치 버전 확인을 요구한다.
- 특정 firmware/배선 구성에 한정된 안전 권고를 제품군 전체 또는 다른 모델/세대에 일반화하지 않는다.


## 48. Branch authority and selective integration (2026-11-17, updated)

1. Main is the canonical operational branch. Current main HEAD, safety checkpoints and active work branch are recorded in PROJECT_STATUS.md.
2. Never merge a divergent branch wholesale. Compare ahead/behind, merge-base, changed files, tests, workflows and state/history/archive effects before integration. Preserve parallel branches; no force-push or history rewrite.
3. The historical `integration/cra-source-grounding-2026-11-17` branch remains a reference only. Its required source/claim features were selectively implemented and verified in PR #26; the branch itself was not wholesale merged.
4. PR #26 source pipeline is merged at `8066c166ba01fbfb8d25f61ce0ce6ed72f151854`; PR #27 project-record sync at `5f0c54a018e18b3453b1c836a5a7d2e9a266331b`; PR #28 checkpoint synchronization at `942e1e6b5f2887001279a96c21f94138d283a689`. Their pre/post merge safety refs are recorded in Section 18.5 and were read back and SHA-verified.
5. Preserve current main operational protections: 15-item history context, two model retries, quota/429/503 no-op behavior, duplicate-topic suppression, transactional persistence and rollback.
6. Article paragraph and Annex Part/point claim locators must be tested against actual source structure. A quote from another paragraph/point in the same Article/Annex must fail.
7. CRA legal source pack currently uses official Publications Office CELLAR retrieval for seven legal texts and two Commission official pages. Source-specific host allowlists, HTTPS-only redirects, source markers, full-text/prompt-excerpt hashes and retrieval timestamps are mandatory.
8. Commission Guidance PDF/Annex and M/606 C(2026) 7861 decision Annex are related URLs only until their bytes/text have actually been retrieved, parsed and hashed. A summary page cannot prove details that exist only in an unparsed PDF/decision Annex.
9. Source/claim validation must fail closed before Gemini calls, Discord posting or Git writes. Temporary source outage may safely skip; content/host/TLS validation failure must not be reported as a successful fetch.
10. PR #26 Run #573 verified 138 passed / 1 xfailed, nine live sources and Article 13(8) locator/quote. This validates the tested PR head, not automatically a separate post-merge Actions run.
11. Sections 46–47 concerning functional safety/SIL are historical reference rules only. They are inactive under the current CRA-only scope and must not initiate SIL/functional-safety work unless the user explicitly reopens that scope.

## 49. CRA official source provenance and claim validation

- Machine retrieval uses official Publications Office CELLAR REST URLs with CELEX identifiers. Human-facing report citations continue to use stable EUR-Lex Official Journal/consolidated-document links.
- Each source definition must declare a source ID, type, version, minimum visible-text length, required markers and explicit allowed host.
- Requests start over HTTPS. Redirects are manually followed only on the same allowlisted host; same-host HTTP redirects are upgraded to HTTPS before the next request. Never relax host allowlists to make a failing fetch pass.
- Preserve requested URL, final URL, retrieval timestamp, full visible-text SHA-256 and prompt-excerpt SHA-256. Hash the exact UTF-8 text used at each stage.
- For CRA English operative corrigenda R(02) and R(04), verify the consolidated prompt excerpt contains the corrected Article 64(10)/Article 67 wording. If stale text is present, apply the exact correction only inside the affected Article block; if the correction source, target block or phrase is missing/ambiguous, fail closed. Keep the raw full-text hash unchanged and recalculate the prompt-excerpt hash after any correction.
- R(01) changes the title, which is outside the current operative excerpt starting at Article 1; retain it as a separate official source and do not claim the title correction was applied to the excerpt.
- Treat HTTP 202, empty body, timeout, connection failure, HTTP 429 and 5xx as temporary unavailable only when classified by the source client. The caller must skip model/Discord/storage side effects on that path. TLS/host/content/marker/redirect validation errors fail closed.
- Every legal claim must have a unique `C-###` reference, exact body statement, registered source ID, exact locator and a direct quote of at least 50 characters. The quote must occur inside the selected Article paragraph or Annex Part/point, not merely somewhere in the same document.
- Official explanation claims must be linked to the Commission source page and explicitly classified as non-binding explanation. Interpretations and engineering recommendations must not be represented as legal requirements.
- The source validator proves source traceability and text/locator consistency; it does not establish the correctness of legal interpretation or product-specific CRA applicability.
- CI live canary currently checks nine official sources and Article 13(8). Expand Article/Annex coverage before claiming complete legal locator coverage.
- Do not claim that the original Commission Guidance/M/606 PDF binary was downloaded, byte-verified or SHA-256 hashed until the bytes have actually been obtained and hashed. If only the PDF text layer is available through a document viewer, describe the work precisely as 'PDF text-layer review' and keep binary-integrity status unverified.

## 50. Commission PDF 및 부속문서 취득·해시 증거 규칙 (2026-11-17)

- Commission Guidance C(2026) 5252 및 M/606 C(2026) 7861 Annex의 웹 PDF text layer를 읽어 문단/페이지 locator를 검토한 것은 **텍스트 내용 감사**로 기록한다.
- 실제 PDF 바이너리를 확보하고 SHA-256을 계산하기 전에는 '원본 PDF 다운로드 완료', '바이너리 무결성 검증 완료', '파일 보관 완료'라고 표현하지 않는다.
- Commission 원본 URL과 기관/규제기관 mirror URL을 분리 기록한다. mirror에서 읽은 문서는 표제·날짜·문서번호가 일치하는지 확인하되, byte-for-byte 동일성을 입증하지 않으면 동일 파일 해시를 주장하지 않는다.
- PDF text extraction에서 날짜/표 셀/병합 셀/페이지 locator가 누락되면 주변 행을 근거로 값을 추정하지 않는다. 해당 셀을 미확인으로 남기고 원본 페이지 이미지에서 확인한다.
- C(2026) 5252는 CRA Article 26에 따른 비구속적 Commission guidance다. 법령 또는 CJEU의 권위 있는 해석과 동일시하지 않고, 법적 의무·Commission interpretation·engineering recommendation을 분리한다.
- C(2026) 7861 Annex의 날짜는 ESO의 표준 채택 기한이다. OJ harmonised standard citation, presumption of conformity, 제품별 conformity assessment 또는 CRA application date와 혼동하지 않는다.
- 제품별 적용성/분류는 제품명만으로 결정하지 않는다. Guidance §2.5 data connection, §6 core functionality, §8 RDPS는 실제 회로·데이터 흐름·기능·제조자 책임 및 제품 경계를 확인하는 기준으로 사용한다.


## 51. PR #30 검증 및 복구 기준

- PR #30의 검증 증거는 PR head Actions Run #610 (`44050954456`) success, 141 passed / 1 xfailed, compileall, source blob identity 및 9-source live canary다.
- merge commit `975ec6728988e43d9a1ebbf6f6d84288aa44c2fd` 자체의 별도 CI run을 확인하지 못했다면 PR head CI와 구분해 기록한다.
- pre-merge safety ref `safety/pre-merge-main-pr30-2026-11-17`와 post-merge ref `safety/post-merge-main-pr30-2026-11-17`의 SHA를 기록하고, post-merge ref와 main이 동일한지 compare/readback한다.
- 문서·테스트 전용 workflow 변경이 운영 `run.yml`, application runtime, state/history/archive 또는 외부 서비스 실행에 영향을 주지 않았는지 PR diff로 확인한다.


## 52. CRA PDF 원문 바이너리 취득 및 CI artifact 검증

- PDF source fetch는 HTTPS host allowlist, redirect final host, `%PDF-` magic, maximum size, pypdf parse, page-count bound, document identity markers를 검증한 뒤 성공으로 기록한다.
- Commission-hosted URL을 우선한다. Guidance PDF에 한해 primary URL이 401/403/404 또는 비-PDF 응답/일시 장애일 때 allowlist된 ANFR mirror를 fallback으로 사용할 수 있다. unexpected redirect host는 mirror fallback 없이 fail-closed한다.
- SHA-256은 **원본 PDF bytes**의 digest와 추출 텍스트 digest를 별도 필드로 기록한다. 이전 웹 PDF text-layer review 기록과 binary SHA-256을 혼동하지 않는다.
- CI artifact는 원본 PDF, 추출 텍스트, manifest를 포함하며 7일 보존한다. artifact를 실제로 다운로드/readback하기 전에는 repository에 원본 파일을 보관했다고 주장하지 않는다.
- source timeout/429/5xx 등 일시 장애는 `SKIPPED`로 기록할 수 있지만, 문서 식별자 불일치, 비허용 redirect, 손상된 PDF, 필수 marker 누락은 성공 처리하지 않는다.
- M/606 Annex 표의 항목 18 등 PDF text extraction이 놓친 셀은 PDF page image로 확인할 때까지 미확인으로 유지한다.


## 53. 2026-11-17 PDF provenance result and table-cell verification

- Run #642 successfully fetched both CRA PDFs, parsed them and generated raw-byte and extracted-text SHA-256. The artifact ZIP was downloaded and its SHA-256 re-computed to match GitHub artifact metadata.
- C(2026) 5252 hash applies to the ANFR mirror bytes only; never claim byte identity with the Commission-hosted primary URL without a direct matching hash.
- C(2026) 7861 Annex hash applies to the Commission document-register PDF bytes.
- M/606 Annex I item 18 deadline is visually confirmed as `31/01/2027` from the PDF page image. Text extraction can omit table cells at page breaks; never infer the value from adjacent rows when image inspection is available.
- Run #642's separate HTML source-page canary failed because a PDF document number was incorrectly required on the Commission summary page. Fix the source-page markers and preserve a regression test; do not weaken PDF identity checks.


## 54. Guidance publication page와 PDF Annex 식별자 분리

- Commission publication summary page는 PDF 문서번호를 반드시 노출하지 않을 수 있다. HTML page validator에는 페이지 자체의 visible title/date/summary marker만 사용한다.
- PDF document number, legal title, page count, PDF raw SHA-256은 별도의 PDF source verifier에서 확인한다. HTML page에 PDF document number가 없다는 이유로 source page를 거부하지 않는다.
- 두 검증 경로를 분리해도 문서 식별 수준은 낮아지지 않는다. page metadata와 PDF identity를 각자 적합한 source layer에서 검증한다.
- Run #669에서 이 분리 기준과 회귀 테스트가 통과했다(148 passed / 1 xfailed, live PDF+HTML canary pass).


## 55. CRA claim/matrix cross-reference integrity gate

- Guidance claim register, interface matrix, requirements traceability, security-control matrix는 ID/row count/foreign-key cross-reference를 자동 검증한다.
- Guidance claim ID는 register에 정의되어야 하고 모든 claim은 최소 한 matrix에서 참조되어야 한다. unknown/orphan claims는 CI fail.
- M/606 Annex I item refs는 1–41 범위여야 하며, candidate relevance는 product classification 또는 harmonised status로 해석하지 않는다.
- PDF raw-byte/text SHA-256, provenance scope, artifact readback, item18 visual verification 및 PROJECT_LOG.jsonl JSON/unique event_id를 확인한다.
- 이 validator는 데이터 무결성 검사이지 CRA 법적 적합성 판정 도구가 아니다.


## 56. M/606 Annex I 41-item relevance mapping

- Every Annex I item 1–41 must have one unique mapping row with its ESO adoption deadline and source page locator.
- Horizontal items 1–15 are standardisation topics; their ESO adoption dates are not manufacturer compliance deadlines.
- Vertical product-type items require intended-purpose/product-boundary/core-functionality analysis. Embedded features, ports, browser views, bootloaders or use of external services do not automatically classify the complete servo drive as that vertical product.
- Security-featured processors/controllers/ASICs/FPGAs/secure elements are component due-diligence candidates when actually integrated; they do not automatically reclassify the final product.
- A standardisation request is not itself an OJ-cited harmonised standard and does not itself create presumption of conformity.
- Candidate CRA/SEC/interface links must resolve to existing IDs and must be labelled conditional where the product type/component has not been confirmed.
- ESO adoption deadlines must never be presented as direct manufacturer compliance deadlines.


## 57. 제품별 CRA 분류 및 적합성 판정 전 증거 게이트

- 일반 매트릭스·Guidance·M/606 crosswalk만으로 특정 서보 드라이브의 CRA 적용성, Annex III/IV 분류, RDPS 여부 또는 적합성을 단정하지 않는다.
- 정확한 모델, intended purpose, marketed functions, product boundary, firmware/software, interfaces, remote processing, BOM/SBOM, support/vulnerability evidence를 확보한다.
- 제품 데이터시트와 사용설명서를 우선 확보하고 서로 교차 검증한다. 모델·구성품·기능을 추정하지 않는다.
- 제품별 결론은 원문 증거 ID·문서 버전·페이지/절 locator·검토 상태를 연결한 후에만 확정한다.


## 58. 통합 보고서 편집·번호 검증

- 통합 보고서에 새 대형 섹션을 추가할 때 기존 최상위 섹션 번호와 중복되지 않는지 확인한다.
- 최상위 `## N.` 번호는 문서 전체에서 유일해야 하며, 중복 번호는 traceability validator에서 fail-closed로 처리한다.
- Annex III Important products(Class I/II)와 Annex IV Critical products를 혼용하지 않는다.
- M/606 Annex I의 horizontal property(1–14), horizontal vulnerability-handling(15), vertical product type 및 security-component 주제를 구분하고, 표준화 요청/ESO deadline을 제조자 법적 의무나 OJ harmonised status로 표현하지 않는다.


## 최신 기록 기준 보완 — 2026-11-18
- 세션 시작 시 최신 재개 스냅샷 [PROJECT_STATUS_CURRENT.md](PROJECT_STATUS_CURRENT.md)와 해당 날짜 세션 로그를 확인한다. 과거 본문에 남은 '현재 작업 브랜치'·'다음 단계'는 최신 스냅샷과 충돌하면 역사 기록으로 취급한다.
- PR merge는 exact head SHA의 CI 성공, diff/review 상태 확인, pre-merge safety ref 및 expected-head merge를 조건으로 한다. 병합 후 post-merge safety ref와 main compare identical 여부를 확인한다.
- CI 성공은 소스/테스트/추적성 검증이지 법률가 검토, 제품 적합성, 기능안전 인증 또는 현장 시험을 의미하지 않는다.
- Commission Guidance PDF의 mirror fallback은 primary source byte identity가 확인되기 전까지 명시적으로 fallback으로 유지한다.


## 59. 최신성·정확성·근거 provenance 통제 — 2026-11-20 추가

- 모델 내부 지식, 대화 요약, 이전 세션의 기억은 최신 법령·표준·운영 상태의 증거로 사용하지 않는다. 각 중요 결론 전에 공식 원문을 현재 시점에 다시 조회한다.
- 최신성은 source-by-source로 관리한다. 각 출처에 publication/update date, version, retrieval date/time (KST), exact URL, acquisition state (raw bytes/hash vs HTML parsed vs metadata only), locator, legal status, next recheck trigger를 기록한다.
- 구속력 있는 법령은 EUR-Lex OJ 및 개정/정정 원문, Commission guidance는 비구속 해석, Commission FAQ는 그 자체의 disclaimer를 반영, ENISA는 플랫폼 운영자료, ESO/CEN/CLC/ETSI 카탈로그는 표준 개발 상태, OJ index는 Article 27 인용 여부의 증거로 각각 분리한다.
- 검색 snippet·검색 결과 날짜·자료실 목록 메타데이터만으로 문서 본문 검토를 주장하지 않는다. HTML parsed text와 PDF raw bytes/page image review를 구분하고, 원문 취득 실패는 그대로 기록한다.
- 핵심 법률 해석은 가능하면 (1) 법령 원문, (2) Commission guidance/FAQ, (3) ENISA/ESO 등 담당기관 운영·표준 자료의 상호 일치 여부를 점검한다. 2차 출처는 discovery/triage 용도로만 사용한다.
- Dynamic Commission/ENISA reporting/FAQ/Glossary/Manual/Status 및 표준화/OJ 현황은 최소 주 1회, 또는 새 버전·공지 발생 시 즉시 재조회한다. 이는 프로젝트 내부 점검주기이며 법적 기한이 아니다.
- 사실/해석/가설/미확인/권고를 구분하고, 반대 근거·예외·적용 범위·기준일을 함께 기록한다. 불일치가 있으면 강제로 하나로 합치지 않고 conflict/unknown으로 유지한다.
- GitHub CI, pytest, traceability validator 성공은 코드·문서 구조 검증일 뿐 법적 정확성 100%, 최신성 100%, 제품 적합성 또는 인증을 의미하지 않는다.
- 모든 자동화 산출물에는 원본 출처, 버전/날짜, 조회일, 파일 hash 또는 hash 미확보 사유, page/paragraph locator, 검토 상태를 연결한다. 미확인 데이터는 Unknown으로 fail-closed 처리한다.


## 11. 자기검토·세션 연속성·토큰 효율 (2026-11-20 보강)
- 상세 운영 기준은 [AI 세션 연속성·자기검토·토큰 효율 운영 기준](reports/AI_SESSION_CONTINUITY_SELF_REVIEW_AND_TOKEN_EFFICIENCY_2026-11-20.md)을 따른다.
- 모델 자체의 자율 재학습/영구 기억을 주장하지 않는다. 기준 확인 → 작업 → 독립 검증 → 오류 분석 → 규칙/테스트 개선 → GitHub 영속화 → 다음 세션 재현의 명시적 루프로 운영한다.
- 세션 시작 시 과거 기억에 있는 브랜치명을 현재로 가정하지 말고 main HEAD, 활성 브랜치, PR, CI를 실시간 재조회한다. `PROJECT_STATUS.md`가 역사 문서이면 `PROJECT_STATUS_CURRENT.md`를 최신 기준으로 사용한다.
- 중대한 잘못·누락·오래된 정보·도구 실패는 원인, 영향, 교정, 재발 방지, 검증 상태와 잔여 한계를 기록한다.
- CRA 전체 규제·표준화·OJ·적합성 경로를 우선 유지한다. LS메카피온/iX7NH는 사례연구로 관리한다.
- 토큰 절약은 중복 재독·중복 설명·광범위 검색을 줄여 달성하되, 공식 1차 출처·반대 근거·locator·검증·한계는 생략하지 않는다.
- CI 성공은 실제 실행된 검사만 증명한다. PR-head CI/main CI, 메타데이터/원문 취득, 보고서 구조/법적 정확성, 제품 기능/보안 검증을 혼동하지 않는다.
- 의미 있는 변경 후 GitHub read-back 전에는 저장 완료로 보고하지 않는다.


## 12. 동적 표준화 상태 및 상충 출처 처리 (2026-11-20)
- ETSI Work Programme의 active count, 화면에 표시된 10개, 개별 상세 record 8개, M/606 Annex I 41개는 서로 다른 모집단이다. 8개 개별감사를 18개 전체 전수감사로 표현하지 않는다.
- Work Programme의 Harmonised Standard=Yes, CENELEC의 Citation expected, forecast OJ date는 실제 OJ citation이 아니다. Article 27 presumption은 실제 OJ reference와 scope fit가 확인된 경우만 주장한다.
- 표준 stage가 national member body 간 다르면 단일 상태로 임의 통합하지 않는다. 출처·조회일·표시 단계·충돌·중앙 ESO record readback 여부를 각각 기록하고 Unknown/Conflict를 유지한다.
- 분할/번호 변경이 발견되면 기존 matrix를 무음으로 덮어쓰지 않는다. 부모 project, 하위 deliverable, M/606 item mapping 및 역사적 CSV를 함께 추적한다.
- C(2026)7861 Article 2의 one-month period는 ESO actual receipt date 기준이다. Commission adoption date나 web page update date로 receipt/acceptance를 추정하지 않는다.
- 동적 milestone 예정일과 ESO adoption deadline, standard publication forecast, actual OJ citation date를 별도 필드로 유지한다.
- Commission Register 원본을 취득하지 못하고 certified-copy mirror만 읽었다면 acquisition limitation과 hash 미확보를 명시한다.


## 13. Central catalogue readback precision
- CENELEC project records must be reported by exact WIID and direct readback status. A parent project page does not establish that split child deliverables have separate catalogue records.
- If one central record is read successfully but sibling records fail, state exactly which WIID was verified and which were not. Do not generalize one page's status to the entire series.
- National-member status tables (DKE, BSI, LVS) are useful evidence but do not replace the CENELEC central record. Conflicts remain visible until reconciled.
