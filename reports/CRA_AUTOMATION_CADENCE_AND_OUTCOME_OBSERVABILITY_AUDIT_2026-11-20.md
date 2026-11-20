# CRA 자동화 주기·실행 품질 감사 및 관측성 개선 — 2026-11-20

## 1. 결론

- GitHub 운영 자동화는 **5분 주기가 아니다**. `.github/workflows/run.yml`의 실제 cron은 `0 */3 * * *`로 3시간마다 UTC 정각 실행을 요청한다.
- 최근 26개 schedule 실행은 모두 GitHub Actions job 기준 success였다. 이전 이력의 오래된 Run #8은 failure였으나 최근 26회와 구분한다.
- 그러나 최근 3회 실행 로그에서는 신규 보고서 생성/전달이 확인되지 않았다. 모델 장애·품질/할당량 보류·중복 주제 없음으로 정상 no-op 종료한 사례가 포함된다.
- 따라서 Actions의 초록색 success를 “CRA 신규 조사 완료”로 간주하면 안 된다.
- 이번 개선은 운영 실행 주기를 바꾸지 않고, 각 실행의 실제 결과를 GitHub Actions Summary에 구조화해 표시하도록 한다.

## 2. 실제 설정 및 최근 이력

### Workflow 설정

- 파일: `.github/workflows/run.yml`
- Cron: `0 */3 * * *` (UTC 기준 3시간 간격)
- Job timeout: 15분
- concurrency: `cra-production-run`, `cancel-in-progress: false`
- Gemini API 및 Discord webhook 사용
- 실행 전 safety checkpoint 생성, operational guard, checkpoint pruning 수행

### 최근 schedule 실행

| Run | 시작(UTC) | Job 결과 | 로그에서 확인한 실제 결과 |
|---:|---|---|---|
| #2522 | 2026-11-20 09:57 | success | Gemini 3.8 Flash 503 → 3.5 Flash Lite 전환 → 신규 주제 없음, 아카이브/Discord 변경 없음 |
| #2521 | 2026-11-20 07:10 | success | 조사 보류(모델/품질 관련) → 원격 main 동시 변경으로 no-op |
| #2520 | 2026-11-20 03:52 | success | 조사 보류(할당량/일시 장애 또는 품질 검증) → 운영 데이터 변경 없음 |

최근 26개 schedule event의 GitHub job conclusion은 모두 success다. 이는 workflow 단계와 guard가 정상 종료했다는 의미이지, 매 실행마다 신규 보고서가 생성됐다는 뜻은 아니다.

### 예약 작업과의 구분

- ChatGPT 자동화 중 매주 CRA·MCU 공식자료 점검은 enabled.
- 매일 Git 브랜치 통합 상태 점검과 매일 CRA 신규 보고서 감사 대기열 점검은 disabled.
- 5분 주기로 설정된 ChatGPT 자동화는 확인되지 않았다.
- GitHub Actions와 ChatGPT 예약 작업은 서로 다른 실행 체계다.

## 3. 5분마다 Gemini 조사 실행으로 바꾸지 않는 이유

5분마다 현재 production workflow 전체를 실행하면 하루 최대 288회 Gemini 호출 시도가 된다. 현재 job은 실행마다 공식 source fetch, Gemini 요청, Git checkpoint 및 필요 시 GitHub/Discord 쓰기를 수행한다. 일부 실행은 3분 이상 소요되고 timeout은 15분이다. 따라서 5분 cron은 queue 누적, 모델 rate/quota 소진, 중복 조사, Discord 과다전송 및 데이터 동시성 위험을 키운다.

현재 3시간 주기를 유지한다. 5분 확인이 필요하다면 Gemini/Discord/운영 데이터 쓰기가 전혀 없는 별도 read-only heartbeat로 분리해 설계해야 한다. 이번 변경에서는 heartbeat를 새로 배포하거나 production cadence를 변경하지 않는다.

## 4. 이번 관측성 개선

### 변경 파일

- `.github/workflows/run.yml`
  - `main.py` stdout/stderr를 runner 임시 로그에 tee하되 원래 프로세스 exit code를 보존.
  - main.py 실행 결과를 별도 summary step에서 분류.
  - operational guard/checkpoint 절차와 cron은 변경하지 않음.
- `scripts/automation_outcome_summary.py`
  - 로그에서 공식 출처 수, 모델 시도/폴백, 원격 아카이브, Discord 전송 상태를 보수적으로 추출.
  - GitHub Step Summary에 실행 결과 표시.
- `tests/test_automation_outcome_summary.py`
  - no new topic, deferred, duplicate, archived+delivered, archived+delivery deferred, nonzero exit, unclassified, missing log의 8개 사례 검증.

### 분류값

| 분류 | 의미 |
|---|---|
| `RESEARCH_ARCHIVED_AND_DELIVERED` | 원격 아카이브 및 Discord 전송 모두 명시적으로 확인 |
| `ARCHIVED_DELIVERY_DEFERRED` | 원격 아카이브는 확인, Discord는 보류/미확인 |
| `NO_NEW_TOPIC` | 신규 주제 없음, 저장/전송하지 않음 |
| `DUPLICATE_BLOCKED` | 중복 주제 차단 |
| `DEFERRED` | 모델 장애/할당량/품질 문제로 조사 보류 |
| `FAILED` | 프로세스 실패 또는 명시적 조사 실패 |
| `SUCCESS_UNCLASSIFIED` | exit 0이지만 로그로 실제 결과를 특정할 수 없음 |
| `NOT_RUN_OR_UNKNOWN` | 실행 또는 로그가 없어 결과를 판정할 수 없음 |

어떤 분류도 법적 적합성이나 제품 보안 검증의 PASS를 뜻하지 않는다.

## 5. 검증 및 제한

- CI는 작업 브랜치의 정확한 HEAD SHA에서 실행한다.
- 테스트는 실제 Gemini/Discord 호출 없이 fixture 로그만 사용한다.
- production run을 수동 dispatch하지 않는다.
- 이 변경은 실제 모델 503/429의 발생 자체를 제거하지 않는다. 다만 job success와 실제 조사 결과를 분리해 관측 가능하게 한다.
- dependency pinning, 모델 장애 backoff 정책, 독립 read-only heartbeat는 후속 개선 후보로 남긴다.
- PR/CI/merge 전에는 main 반영 완료라고 표현하지 않는다.

## 6. 다음 순서

1. PR exact-head CI 및 8개 분류 테스트 통과 확인.
2. diff에서 cron, secrets, main.py, Discord/Gemini 실행 빈도, operational guard가 의도치 않게 변경되지 않았는지 확인.
3. 병합 승인/기존 change-control에 따라 반영한 뒤, 다음 예약 실행에서 Summary가 실제 결과를 정확히 분류하는지 확인.
4. 별도 5분 read-only heartbeat의 효용과 무료 실행량을 평가한 후 필요할 때만 별도 PR로 제안.


### CI 검증 결과 — 2026-11-20
- PR #189 exact HEAD `434819fde00e1f72b7ff158cc4893e0fc1d2e367`, Actions Run #1247 / ID `44741088582`: success.
- 전체 pytest: **182 passed / 0 failed** (기존 174개 + 자동화 outcome 분류 테스트 8개).
- source blob identity, compileall, CRA cross-matrix traceability, official CRA PDF canary, live official CRA HTML canary, provenance manifest upload: success.
- PDF source artifact upload 단계는 unchanged/condition에 따라 skipped; workflow 실패가 아니다.
- 실제 production run/Discord/Gemini 호출은 하지 않았다. CI 결과는 테스트 브랜치의 classifier 검증이며 production 배포 검증이 아니다.
