# AI 재귀개선 모방 알고리즘 — 일일 검증·갱신 프로토콜

- 문서 버전: 1.0
- 기준일: 2026-11-21 (KST)
- 상태: **절차 정의·문서 반영 완료 / 장기 운영 효과 미검증**
- 적용 범위: CRA 조사·법령/표준 검증·보고서·GitHub 운영 및 AI 작업 품질
- 목적: 모델 가중치의 자기학습을 주장하지 않고, 검증된 경험을 규칙·체크리스트·테스트·상태판으로 외부화하여 다음 작업의 품질을 점진적으로 개선한다.

## 1. 핵심 원칙

1. **증거 우선**: 대화의 주장보다 GitHub 실제 파일, 원문 출처, CI, read-back, 운영 로그를 우선한다.
2. **날짜 경계에서 재검토**: 한국시간(Asia/Seoul) 날짜가 마지막 검토일보다 뒤로 바뀌면 일일 리뷰를 실행한다.
3. **선별적 학습 모방**: 반복 가능하고 유효성이 입증된 개선만 영구 규칙·검사·테스트로 반영한다.
4. **실패 보존**: 실패·보류·미확인은 성공으로 바꾸지 않는다. 이전 기준과 복구 지점을 보존한다.
5. **비용 통제**: 날짜 변경 자체가 불필요한 전체 조사·전체 파일 덤프·모델 호출을 유발하지 않도록 한다.
6. **사람 승인 경계**: 기존 권한으로 허용된 문서/테스트 개선은 진행하되, 비밀정보·권한·외부 전송·운영 호출 빈도·보호되지 않은 위험 변경은 별도 승인/검토 대상으로 둔다.

## 2. 일일 날짜 변경 감지

세션을 시작하거나 재개할 때 다음 값을 확인한다.

- `today_kst`: 현재 한국 날짜
- `last_reviewed_kst`: GitHub 상황판 또는 이 문서에 기록된 마지막 일일 검토 날짜
- `rulebook_version`: AI_RULEBOOK의 현재 규칙 버전/최종 갱신 커밋
- `last_verified_main_sha`: 마지막으로 read-back 및 CI까지 확인한 main SHA

판정:

- `today_kst == last_reviewed_kst`: 일일 전체 검토는 반복하지 않는다. 다만 현재 작업의 필수 시작 점검은 수행한다.
- `today_kst > last_reviewed_kst`: 날짜 경계 검토를 실행한다.
- `today_kst < last_reviewed_kst`: 시간대/시계/기록 오류 가능성을 표시하고 자동으로 날짜를 덮어쓰지 않는다.
- 날짜는 UTC가 아니라 **Asia/Seoul** 기준으로 비교한다. 실행 환경의 UTC 날짜만으로 일일 경계를 판단하지 않는다.

## 3. 일일 검토 파이프라인

### 단계 A — 기준 상태 동기화
1. GitHub main, 최근 PR, 미완료 CI, safety refs를 조회한다.
2. README 진입 링크, AI_RULEBOOK, PROJECT_STATUS_CURRENT, MASTER_PLAN, 최근 SESSION_LOG/PROJECT_LOG tail을 확인한다.
3. 마지막 검토 이후 변경된 파일과 commit/PR/CI 결과만 우선 확인한다.
4. 이전 대화의 요약이나 기억만으로 현재 상태를 추정하지 않는다.

### 단계 B — 결과·행동 감사
각 실질 작업을 다음 축으로 점검한다.
- 요청·범위 준수
- 공식 1차 출처와 최신성
- 사실/추론/미확인 구분
- 독립 교차검증 및 반대 근거
- 보고서/데이터의 완전성·정합성
- 도구 선택과 토큰/시간 효율
- 저장·read-back·테스트·CI·운영 결과의 구분
- AI의 오류·누락·과장·반복·잘못된 완료 주장

단순한 진행 지시 또는 새 결과가 없는 대화는 별도 상세 기록을 만들지 않는다.

### 단계 C — 개선 후보 평가
각 후보를 다음 기준으로 평가한다.
- 증거: 구체적인 로그·파일·테스트·출처가 있는가?
- 반복성: 다른 작업에서도 재발할 수 있는가?
- 영향: 정확성·최신성·안전성·추적성·재현성·효율을 실질적으로 개선하는가?
- 비중복성: 기존 규칙과 중복/충돌하지 않는가?
- 검증 가능성: 통과 여부 또는 효과를 확인할 방법이 있는가?
- 부작용: 불필요한 비용·복잡성·운영 위험을 만들지 않는가?

점수화가 근거 없는 정밀도를 만들 수 있으므로 임의 가중합 점수는 사용하지 않는다. 위 항목을 통과/보류/제외로 판정하고 이유를 남긴다.

### 단계 D — 개선 수준별 반영

| 수준 | 조건 | 반영 위치 |
|---|---|---|
| A | 일회성 사실/문장 오류 | 해당 보고서 또는 기록만 수정 |
| B | 재사용 가능한 절차 개선 | AI_RULEBOOK, 운영 프로토콜, 체크리스트 |
| C | 반복되는 기계적 오류 | 테스트, lint, validator, CI 검사 |
| D | 구조적·고위험 결함 | Issue/PR, safety ref, 복구 절차 |

규칙을 추가하기 전에 기존 규칙을 수정·통합하는 편이 나은지 먼저 확인한다.

### 단계 E — 변경·검증·배포
1. main SHA를 기준으로 safety ref와 작업 브랜치를 만든다.
2. 최소 diff로 변경하고 문서 간 링크/번호/상태를 동기화한다.
3. JSONL/CSV/코드 변경은 전체 파싱·구조 검사 및 관련 테스트를 수행한다.
4. PR exact-head CI를 확인한다. job success만으로 조사 산출물이나 운영 전송 성공을 주장하지 않는다.
5. 병합 후 main SHA, 파일 read-back, post-merge CI, safety ref를 확인한다.
6. 실패 시 원인을 기록하고 이전 정상 커밋/ref로 복구한다. 실패한 개선을 조용히 덮어쓰지 않는다.

## 4. 개선 효과의 증거 단계

각 변경은 아래 상태 중 하나로만 표시한다.

- `PROPOSED`: 개선 후보만 식별됨
- `DOCUMENTED`: 규칙/절차 문서에 반영됨
- `TESTED`: 테스트 또는 CI가 통과함
- `OPERATIONALLY_OBSERVED`: 후속 실제 작업/운영에서 기대 효과가 관찰됨
- `REGRESSED`: 부작용 또는 회귀가 확인됨
- `RETIRED`: 효과가 없거나 더 나은 기준으로 대체됨

문서화·CI 통과만으로 운영 효과를 입증했다고 표현하지 않는다. 가능한 경우 전후 사례를 비교하되, 측정하지 않은 효과 수치를 만들지 않는다.

## 5. 일일 버전·기록 정책

- 일일 검토가 실제로 수행된 날에만 마지막 검토일을 갱신한다.
- 변경이 없으면 `NO_CHANGE`로 간단히 기록하고 규칙 파일을 불필요하게 수정하지 않는다.
- 개선이 있으면 날짜·관찰 근거·원인·수정·검증·잔여 위험·복구 SHA를 기록한다.
- 하나의 통합 프로토콜을 기준 문서로 유지하고 AI_RULEBOOK에는 짧은 실행 규칙과 링크를 둔다.
- 매일 새 문서를 무조건 생성하지 않는다. 기존 프로토콜/상황판/세션 로그에 누적한다.
- 과거 판단을 삭제하지 않고 적용 시점과 상태를 남겨 추적 가능하게 한다.

## 6. 토큰·시간 효율 가드

- 날짜 경계에서는 우선 변경 목록, 최신 커밋, 최근 로그 tail, 실패한 CI만 확인한다.
- 대형 파일 전체 출력 대신 경로/라인 범위와 요약을 사용한다.
- 같은 출처·파일을 중복 조회하지 않는다.
- 외부 최신 정보가 필요한 CRA 주장만 공식 출처에서 재확인한다. 모든 문장을 매일 처음부터 조사하지 않는다.
- 필수 검증, 반대 근거, 법적 효력 구분을 토큰 절약 목적으로 생략하지 않는다.
- 운영 Gemini 호출·Discord 전송·cron 빈도는 이 일일 리뷰에서 변경하지 않는다.

## 7. 현재 기준선 및 미검증 사항

- 기준일: 2026-11-21 KST
- 기준 main SHA: `5ba75efdac9a755fd8adb0d114e2dcba2980bb91` (PR #192 merge)
- PR #192 main post-merge CI Run `44839652639`: success; source integrity, compile, CRA traceability, full pytest, official CRA PDF/HTML read-only canaries, provenance upload all passed.
- 이 CI는 이 문서의 장기 효과를 증명하지 않는다.
- 일일 날짜 변경 트리거는 현재 **세션 시작/재개 시 실행하는 운영 규칙**이다. 별도 자동 스케줄러/백그라운드 에이전트가 날짜 변경을 감지해 문서를 수정한다고 주장하지 않는다.
- 다음 검증: 다음 KST 날짜 경계에서 이 프로토콜에 따라 실제 리뷰를 수행하고, 중복 조회 감소·오류 재발 방지·상태 정확성을 관찰한다.

## 8. 실행 결과 템플릿

```yaml
review_date_kst: YYYY-MM-DD
previous_review_date_kst: YYYY-MM-DD
base_main_sha: <sha>
safety_ref: <ref>
work_branch: <branch>
observations:
  - evidence: <file/log/source/test>
    issue: <observed issue>
    recurrence: <one-off|recurring|structural>
    impact: <accuracy|safety|traceability|efficiency|other>
decisions:
  - level: <A|B|C|D>
    status: <PROPOSED|DOCUMENTED|TESTED|OPERATIONALLY_OBSERVED|REGRESSED|RETIRED>
    change: <minimal change>
validation:
  - <readback/test/CI>
residual_risks:
  - <unknown or none>
next_review:
  trigger: next Asia/Seoul date rollover
  priority: <one to three items>
```



## 9. 2026-11-23 KST 날짜 경계 검토 결과

- 이전 검토 기준일: 2026-11-21 KST. 이번 세션 재개일은 2026-11-23 KST이므로 날짜 경계 검토를 실행했다.
- 기준 main SHA: 584a7c092ea434d52f7794452ca85b0cbe981210.
- 관찰 1: 열린 PR #204는 main 대비 7 ahead / 0 behind이며 7개 문서를 변경한다. 정확한 PR head CI를 확인하기 전에는 병합하지 않는다.
- 관찰 2: 제조사 카탈로그 목록 제목의 날짜와 첨부파일 메타데이터 날짜가 다를 수 있다. 개선: 목록 제목·상세 페이지·첨부파일명/날짜·PDF 본문 개정 이력을 분리해 기록한다. 상태: DOCUMENTED; 후속 원본 확보/검증 필요.
- 관찰 3: ETSI 회의 캘린더는 2026-11-23 일정만 확인시킨다. 공개 회의록/결정/ESO 통지 원문은 확보되지 않았다. 개선: 일정, 개최, 결정, 수령, 수락, OJ citation을 별도 상태로 유지한다. 상태: DOCUMENTED.
- 규칙 변경 여부: 기존 증거 우선·Unknown 보존·정확한 head CI 게이트 규칙이 이미 이 문제를 다루므로 AI_RULEBOOK 신규 규칙은 추가하지 않았다(NO_CHANGE).
- 검증 경계: 이번 검토와 문서 read-back은 장기 운영 효과를 입증하지 않는다. PR #204의 exact-head CI 및 main 병합 후 효과는 별도 확인한다.
- 다음 검토: 다음 Asia/Seoul 날짜 변경 후 수행.
