# CRA 프로젝트 — 지속 메모리·검증 기반 개선 및 다음 단계 버튼 운영 규약

- 문서 ID: AI-OPS-CRA-001
- 버전: 1.0
- 기준일: 2026-11-24 (Asia/Seoul)
- 적용 범위: LS메카피온 iX700M 중심 CRA 조사·분석·증거·보고서·GitHub 작업
- 제외 범위: SIL 3, 무관한 제품/프로젝트 확장
- 목적: 대화 세션이 바뀌어도 프로젝트 상태와 교정된 작업 방식을 GitHub에서 이어가고, 모든 주요 응답에서 다음 작업 버튼을 일관되게 제공한다.

## 1. 운영상 약속: 다음 단계 버튼은 기본값

모든 주요 CRA 진행 응답의 마지막에는 사용자가 한 번 눌러 다음 작업을 요청할 수 있는 버튼을 제공한다.

- 표시 문구: **다음 단계 계속 진행**
- 버튼은 장식이 아니라 실제 새 대화 턴을 시작하는 동작이어야 한다.
- 버튼의 payload는 단순한 "진행해"가 아니다. 아래의 정식 프롬프트를 사용한다.
- 응답의 마지막에 버튼을 두고, 버튼이 가리키는 다음 작업은 현재 GitHub 상태에서 가장 우선순위가 높은 미완료 작업으로 정한다.
- 버튼을 제공하지 못한 경우 그 이유를 해당 응답에서 명시하고, 다음 응답에서 복구한다.
- 이 규칙은 GitHub의 이 문서와 PROJECT_STATUS_CURRENT.md, README.md, SESSION_LOG.md, PROJECT_LOG.jsonl에 기록한다.

## 2. 버튼이 제출할 정식 프롬프트

아래 본문을 다음 단계 버튼의 payload로 사용한다. 작업에 맞게 현재 PR/파일/Run 번호만 추가할 수 있으며, CRA 범위와 안전 규칙은 제거하지 않는다.

> CRA만 계속 진행해줘. 먼저 GitHub main의 최신 commit, PROJECT_STATUS_CURRENT.md, README.md, 관련 보고서·증거등록부·SESSION_LOG.md·PROJECT_LOG.jsonl 및 이 문서(docs/AI_CONTINUOUS_IMPROVEMENT_AND_NEXT_STEP_PROTOCOL.md)를 읽고 현재 상태를 재구성해. 과거 기록은 현재 작업과의 관련성·시간순서·현재 HEAD와의 호환성을 확인한 뒤에만 재사용하고, 오래되었거나 무관한 기록은 적용하지 마. 원본 로그·근거·실패 이력은 보존하고, 재사용할 규칙만 근거와 함께 간결하게 추출해. 다음 우선순위 CRA 작업 하나를 선택해 실제 수행하고, 공개 법령/공식 자료 및 제조사 증거를 교차검증해. 변경 전 기준 commit·작업 브랜치·대상 파일·복구 기준을 기록하고, 문서/코드 변경 후 해당 범위 테스트와 exact-HEAD CI를 검증해. 개선 후보는 가설·근거·적용 범위·예상 효과·검증 방법을 기록하고, 실패·회귀·부작용이 있으면 원인과 복구를 기록해. 검증되지 않은 사실이나 제조사 회신/자료 확보/병합 성공을 주장하지 마. 결과와 증거를 GitHub 상황판·보고서·증거등록부·작업 로그에 반영해. 운영 main.py/workflow/secrets/API cadence 변경은 CRA 목적과 직접 관련되고 안전한 변경 계획 및 회귀검증이 확보되지 않으면 하지 마. CRA only; SIL 3 제외. 응답 마지막에 이 버튼을 다시 제공해.

## 3. 연구 근거와 적용 원칙 (2026-11-24 확인)

### 3.1 MemDev-Bench — 관련성 평가와 원시 작업 궤적 보존

- Guorui Chen et al., *MemDev-Bench: Does Memory Help Code Agents? Benchmarking Memory Systems over Real Repository Histories*, arXiv:2610.27524, 2026-10-20.
- URL: https://arxiv.org/abs/2610.27524
- 벤치마크는 555개 작업과 4,869개 과거 작업을 사용해 이전 이력의 Strong Related / Weak Related / Unrelated 관련성을 구분했다.
- 핵심 관찰: 메모리는 파일 내 위치 특정·수정에 도움이 될 수 있지만, 관련 이력조차 현재 과제에 재평가 없이 적용하면 원래 풀 수 있던 과제에서 실패를 유발할 수 있다. 무관한 이력은 실패를 더 늘릴 수 있다.
- 원시 과거 trajectory를 직접 제공했을 때 압축 메모리보다 작업 단계가 줄어드는 경우가 있었다. 압축 과정에서 절차 정보가 누락될 수 있기 때문이다.
- 적용: 원본 GitHub 로그/CI 결과/PR diff는 삭제·덮어쓰기하지 않고 보존한다. 재사용 규칙은 현재 과제 관련성(강/약/무관), 날짜, 대상 branch/commit, 적용 전제와 함께 선택한다. 핵심 절차와 실패 원인은 지나치게 압축하지 않는다.

### 3.2 Continual AutoResearch — 상태 보존과 성과는 별개

- Jeremy Qin et al., *From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?*, arXiv:2611.05108, 2026-11-03.
- URL: https://arxiv.org/abs/2611.05108
- 동일한 task stream과 예산에서 persistent state가 5개 에이전트의 연구 효율을 개선했지만, 최종 성능 개선은 일관되지 않았다.
- 저자들은 경험을 보유하는 능력과 다음 과제에서 적절히 사용하는 능력이 별개라고 강조한다.
- 적용: GitHub에 기록했다는 사실을 성능 향상으로 간주하지 않는다. 실제로 재사용했는지, 결과가 좋아졌는지, 테스트/품질/작업 효율이 개선됐는지를 별도로 기록한다. 이전 프롬프트나 규칙을 무조건 재적용하지 않는다.

### 3.3 Self-Improvements in Modern Agentic Systems — 개선 대상 구분

- Zhe Ren et al., *Self-Improvements in Modern Agentic Systems: A Survey*, arXiv:2607.13104, 2026-07-14.
- URL: https://arxiv.org/abs/2607.13104
- 모델 가중치뿐 아니라 prompt, memory, tools, control logic을 포함하는 운영 scaffold를 개선 대상으로 보는 시스템 수준 프레임워크를 제시한다.
- 적용: 이 프로젝트는 모델 가중치를 업데이트하지 않는다. 개선 대상은 GitHub에 저장된 프롬프트, 프로젝트 메모리, 작업 규칙, 도구 사용 절차 및 검증 게이트로 제한한다. 이를 "모델 자체의 학습"이라고 표현하지 않는다.

### 3.4 Dual-Process Agent — 빠른 실행과 느린 검토 분리

- Liangyu Teng et al., *Towards Self-Evolving Agents: A Dual-Process Framework for Continual Context Refinement*, Electronics 2026, 15(6), 1232, 2026-03-16.
- DOI: https://doi.org/10.3390/electronics15061232
- 검색·기억을 활용한 빠른 실행(System 1)과 결과를 검토하고 선별된 메모리를 갱신하는 느린 검토(System 2)를 분리한다. 무분별한 메모리 누적보다 보수적인 curator gate가 중요하다고 설명한다.
- 적용: (A) 작업 시작 시 최신 상황판과 관련 근거를 신속히 회수하고, (B) 작업 종료 시 증거·오류·테스트·재사용 가치를 별도로 검토한 후에만 개선 규칙을 등록한다.

### 3.5 연구의 한계

- arXiv 논문은 peer review 여부가 별도로 확인되지 않는 한 preprint로 표시한다.
- 논문 결과는 해당 논문의 데이터·환경·모델에서 얻은 것이므로 이 CRA 저장소에서 동일한 성능 향상을 보장하지 않는다.
- 논문 초록/요약만 확인한 항목을 전문 검토했다고 주장하지 않는다. 상세 설계에 적용하기 전 원문과 실험 한계를 추가 확인한다.
- 연구 결과와 프로젝트 자체 관찰을 구분하고, 적용 근거·변경점·검증 결과를 각각 기록한다.

## 4. 세션별 반복 실행 루프

1. **상태 회수:** 최신 main HEAD, 미병합 PR, CI 상태, PROJECT_STATUS_CURRENT, 최근 session/project log를 읽는다.
2. **관련성 판단:** 과거 작업을 현재 이슈와 비교해 Strong / Weak / Unrelated로 분류한다. branch/commit이 달라진 과거 절차는 현재 환경에서 재검증한다.
3. **증거 확인:** CRA 법령·관보·집행위·표준화기관·제조사 원문을 우선한다. 출처 URL, 문서 식별자, 개정일, 접근일, hash/파일을 기록한다.
4. **가설과 계획:** 해결할 문제, 원인 가설, 변경 파일, 예상 결과, 위험, 복구 방법, 완료 판정 기준을 사전에 명시한다.
5. **실행:** 다음 우선순위의 실제 산출물을 만든다. 계획만 남기고 끝내지 않는다.
6. **검증:** 문서 링크/인용, 데이터 구조, 코드 compile/test, CRA traceability, exact-HEAD CI 및 artifact를 변경 범위에 맞게 확인한다.
7. **반성·선별:** 성공/실패, 원인, 재사용 가능성, 이번에만 해당하는 사실을 구분한다. 확인되지 않은 자기평가를 성과로 쓰지 않는다.
8. **기록:** 상황판, 보고서, 증거등록부, 세션 로그, append-only PROJECT_LOG를 동기화한다.
9. **다음 버튼:** 현재 미완료 작업 중 가장 높은 우선순위를 선택해 버튼 payload를 구성한다.

## 5. 개선 메모리의 등록·수정·폐기 게이트

개선 규칙은 아래 조건을 모두 만족할 때만 정식 규칙으로 등록한다.

- 실제 작업/테스트/공식 증거/사용자 명시 요구 중 하나 이상의 근거가 있다.
- CRA 범위와 현재 저장소 상태에 적용 가능하다.
- 기존 규칙과 충돌 여부를 확인했다.
- 구체적인 행동 지침과 실패 방지 목적이 있다.
- 검증 방법 또는 적용 후 관찰 지표가 있다.

규칙을 수정할 때는 이전 내용을 조용히 덮어쓰지 말고 변경 이유와 날짜를 기록한다. 실패한 후보도 삭제하지 말고 rejected/retired와 이유를 남긴다. 메모리 오염, 오래된 링크, 잘못된 전제, 무관한 이력의 과잉 재사용을 주기적으로 점검한다.

## 6. 최소 측정 지표

| 지표 | 기록 방법 | 주의점 |
|---|---|---|
| 반복 오류 | 동일 원인으로 재발한 횟수/기간 | 단순 오류 건수만으로 모델 개선을 주장하지 않음 |
| 검증 통과 | exact-HEAD CI 및 테스트 결과 | 실행 성공과 법률 해석 정확성은 별개 |
| 증거 완전성 | 주장별 1차 출처·문서판·SKU 연결 여부 | 미확보/Unknown을 숨기지 않음 |
| 작업 효율 | 유사 과제에서 재사용한 절차와 불필요한 재작업 | 작업량/난이도 차이를 함께 기록 |
| 회귀 | 변경 후 기존 통과 테스트/기능의 실패 여부 | 실패 시 원복/수정 경로 확보 |
| 메모리 품질 | 관련성 오판, 오래된 규칙 재사용, 충돌 사례 | 메모리 증가량을 성과로 보지 않음 |

## 7. 변경 안전·복구 규칙

- 작업은 main에서 직접 수행하지 않고 목적별 branch에서 수행한다.
- 변경 전 main SHA, branch, 변경 대상, 기존 상태를 기록한다.
- PR exact HEAD의 CI가 통과하고 diff/파일 목록/로그 무결성을 검토하기 전에는 병합하지 않는다.
- 문서 전용 변경은 문서 검증 및 저장소 전체 필수 CI를 확인한다.
- 운영 코드/workflow/secrets/API cadence 변경은 별도 위험 검토, 테스트, 사용자 승인/정책 및 rollback plan 없이 수행하지 않는다.
- 병합 후 main read-back과 main CI를 확인하고 post-merge 복구 기준을 기록한다.
- 실패하면 원인을 구분하고 마지막 정상 상태로 복구한다. 실패한 시도를 성공으로 기록하지 않는다.

## 8. 프로젝트 고정 경계

- 본 프로젝트의 주제는 CRA뿐이다.
- LS메카피온 iX700M은 현재 조사 대상이며, 제조사 답변 전 독립 판매·EU 개별 공급·실제 SKU·내부 회로/BOM/MCU/보안 설정을 Unknown으로 유지한다.
- 사용자의 별도 프로젝트 MCU가 ST라는 사실을 iX700M에 전용하지 않는다.
- 사용자가 이해하기 쉬운 한국어를 주 언어로 하고, 중학교 2학년도 따라올 수 있도록 용어 정의·원리·판정 근거를 충분히 설명하되 전문적 세부사항을 생략하지 않는다.
- CRA 외 주제(SIL 3 등)는 사용자가 새로 명시하지 않는 한 끌어오지 않는다.

## 8.1 최종 응답 버튼 누락 방지 게이트 (v1.1)

2026-11-24 운영 실패 분석: 기존 v1.0 규약과 README에 버튼 상시 제공이 명시되어 있었지만, 응답을 마무리할 때 출력 체크리스트를 강제하지 않아 버튼을 실제 답변에 렌더링하지 못했다. 원인은 규칙 부재가 아니라 규칙-출력 실행 사이의 통제 누락이다.

필수 마감 게이트:
1. 모든 실질적인 CRA 진행 응답의 마지막 UI 요소가 실제 동작하는 **다음 단계 계속 진행** 버튼인지 확인한다.
2. 버튼은 실제 새 대화 턴을 시작하는 동작과 정식 payload(§2)를 포함해야 한다. 단순 텍스트·링크·비활성 버튼은 통과로 보지 않는다.
3. 버튼 payload는 현재 main/PR/CI 상태와 이 규약을 다시 읽고, 현재 미완료 작업 중 최우선 CRA 작업을 수행하도록 한다.
4. 버튼 누락을 감지하면 응답을 완료하기 전에 수정한다. 스트리밍 중단 등으로 이전 응답에 버튼이 없었다면 다음 응답에서 원인을 기록하고 버튼을 복구한다.
5. 대화 사이에 모델이 자율적으로 계속 실행되는 것으로 표현하지 않는다. 버튼은 사용자의 한 번의 클릭으로 다음 턴을 시작하는 재개 장치이며, 재귀개선은 GitHub 기록·검증·선별된 규칙 갱신을 모방하는 절차다.

응답 직전 체크: CRA scope 확인 → 근거/실행상태 확인 → 성공·실패 과장 금지 → GitHub 기록 상태 확인 → 실제 버튼 컴포넌트 존재 및 payload 확인 → 버튼을 마지막에 배치.

## 9. 변경 이력

- 2026-11-24 v1.1: 실제 응답에서 버튼을 누락한 운영 실패의 원인을 규칙 부재가 아닌 최종 출력 게이트 미실행으로 분류하고, 응답 직전 강제 체크리스트·복구 절차를 추가.
- 2026-11-24 v1.0: 버튼 상시 제공과 정식 payload를 고정. MemDev-Bench, Continual AutoResearch, self-improvement survey, Dual-Process Agent 연구를 반영해 관련성 게이트·원시 trajectory 보존·보수적 memory curation·성과 검증 원칙을 수립.


## 8.2 실제 버튼 렌더링 검증 게이트 (v1.2)

2026-11-25 재발 분석: v1.1의 상시 버튼 규칙과 최종 출력 체크리스트가 main에 이미 존재했고, PR #253에도 Run #1540 및 JSONL 교정 결과가 기록되어 있었다. 그럼에도 assistant가 해당 문서를 다시 확인하지 않고, 사용자에게 "GitHub에 규칙으로 고정했는지 확인하지 않았다"고 부정확하게 답했으며, 이어진 실질 응답에서도 실제 버튼 컴포넌트를 누락했다. 이번 문제는 문서 부재가 아니라 **최신 규약 재확인 및 최종 응답 렌더링 게이트의 재실패**다.

v1.2 추가 통제:
1. CRA 진행을 마무리하는 모든 최종 응답에는 설명이나 진행 로그 뒤에 실제 동작하는 DIL `<button>`을 마지막 UI 요소로 렌더링한다. 버튼 설명, Markdown 링크, 버튼 모양 텍스트는 대체물이 아니다.
2. 버튼은 `GenUI.issueNewTurn(...)`를 직접 호출해야 하며, payload는 §2의 정식 CRA 재개 프롬프트를 바탕으로 현재 main HEAD, 미완료 PR/CI, 다음 최우선 작업을 다시 읽고 수행하도록 구성한다.
3. 최종 응답 직전 실제 출력 초안에서 다음 네 조건을 모두 확인한다: (a) `<button>` 존재, (b) `onClick`에 `GenUI.issueNewTurn` 존재, (c) payload에 CRA only/SIL 3 제외 및 GitHub 최신 상태 재확인 포함, (d) 버튼이 응답의 마지막 UI 요소.
4. 스트리밍 중단 또는 도구 호출 실패로 버튼이 빠졌다면 다음 응답에서 누락 사실을 인정하고, 현재 상태를 짧게 복구한 뒤 버튼을 다시 제공한다. 누락 원인을 GitHub SESSION_LOG/PROJECT_LOG에 남긴다.
5. 응답 생성 전에 최신 main의 이 규약과 상황판을 확인한다. 과거 대화 메모리만으로 규칙이 있다고 추정하거나, 이미 기록된 규칙을 새로 만들었다고 주장하지 않는다.
6. 버튼 payload는 "진행해" 한 단어로 끝내지 않는다. 현재 진행 중인 PR/Run의 exact HEAD·ID를 포함할 수 있으면 포함하고, 성공 시 diff/reviews/JSONL 검증·expected-head merge·main push CI를, 실패 시 로그 원인 분석·수정·재검증·성공 전 병합 금지를 지시한다. 이후 제품 증거 취득과 Unknown 관리까지 이어간다.

응답 직전 hard gate: **최신 GitHub 규약 재독 → 사실/상태 검증 → 문서 기록 여부 확인 → 실제 DIL 버튼 및 payload 검사 → 버튼을 마지막에 배치 → 응답 종료.** 버튼이 없으면 실질 진행 응답을 완료한 것으로 취급하지 않는다.



## 8.3 단독 버튼 렌더링/전달 게이트 (v1.3, 2026-11-25)

### 재발 분석
v1.2가 main에 존재하고 PROJECT_LOG에도 버튼 누락 재발 이력이 있었지만, 사용자가 다시 버튼을 찾지 못하거나 이용할 수 없다고 보고했다. 이전 응답은 버튼을 box 컨테이너 안에 배치했다. 이것이 플랫폼 렌더링 문제라고 단정할 수는 없으나, 버튼의 시각적 발견성과 클릭 접근성을 불필요하게 복잡하게 만든 선택이었다.

### v1.3 변경
1. 실질 CRA 응답의 마지막 UI 요소는 **컨테이너에 넣지 않은 단독 DIL `<button>`**으로 출력한다. 카드/박스/콜아웃/장식 레이아웃 안에 중첩하지 않는다.
2. 버튼 라벨은 짧고 일관되게 `다음 단계 계속 진행`으로 고정한다.
3. `onClick`은 `GenUI.issueNewTurn(...)`를 직접 호출한다. 단순 텍스트, 링크, 비활성 버튼은 인정하지 않는다.
4. payload는 CRA only / SIL 3 제외를 명시하고, 최신 main HEAD·행동규약·상황판·열린 PR/CI를 재조회한 뒤 exact-head 성공/실패 게이트, 제조사 원본 증거 취득, Unknown 유지, 보고서/로그 동기화를 수행하도록 지시한다.
5. 최종 출력 직전 네 항목을 강제 검사한다: 실제 button 태그, 직접 onClick action, 완전한 CRA 재개 payload, 응답 마지막 UI 요소.
6. 사용자가 버튼 누락/비가시/비작동을 보고하면 이를 사용자 탓으로 돌리지 않는다. 단독 버튼으로 즉시 복구하고 SESSION_LOG 및 PROJECT_LOG에 재발을 기록한다.

### 작동 범위의 정확한 설명
이 버튼은 사용자가 한 번 누르면 새 대화 턴을 시작하는 재개 장치다. 모델이 대화 사이에 스스로 계속 실행하거나 학습 가중치가 바뀌는 기능은 아니다. 재귀개선은 GitHub에 남긴 관찰·실패·검증·선별 규칙을 다음 턴에서 다시 읽고 적용하는 절차적 모방이다.

- 2026-11-25 v1.3: 단독 버튼 배치로 단순화하고, 사용자 관점의 실제 전달/발견 실패를 별도 운영사건으로 기록.


## 8.4 GitHub Actions main push 실행 직접 조회 (v1.4, 2026-11-25)

### 기존 조회의 한계 및 해결
기존 `fetch_commit_workflow_runs` wrapper는 pull_request 이벤트를 중심으로 반환하여, main 병합 후 push 실행을 누락할 수 있었다. Combined Status가 빈 배열인 경우에도 push workflow가 없다고 결론 내리면 안 된다.

정확한 main push 검증은 GitHub Actions runs collection을 직접 조회한다.

`GET /repos/{owner}/{repo}/actions/runs?head_sha={exact_commit_sha}&event=push&per_page=100`

반드시 응답의 `head_sha`, `head_branch=main`, `event=push`, `status=completed`, `conclusion=success`를 대조한 후 run jobs, 모든 step, logs 및 artifacts를 확인한다. PR exact-head run과 main push run을 별도 기록한다. 조회가 0건이거나 권한/도구 실패면 UNVERIFIED 유지. main push success를 확인하면 report, evidence register, status, README, SESSION_LOG, append-only PROJECT_LOG를 후속 PR에서 동기화한다.

### 2026-11-25 실증
main `660eb6d20e62f772272c03971dcd773b03a703f5`의 push Run #1588 / ID `45532289060`이 이 방식으로 발견되어 SUCCESS 및 15/15 steps로 검증되었다. 상세는 통합 보고서 §103과 PROJECT_LOG event에 기록한다.


### 2026-11-25 Run #1592 실증 추가
- PR #272 exact-head Run #1591 / 45537296095 SUCCESS, main branch Run #1592 / 45537422906 job SUCCESS; both 15/15 steps, 189 pytest passed, traceability 405, CRA PDFs 3/3, official source provenance 10건 round-trip/upload PASS.
- Main run artifact metadata confirms `head_branch=main` and exact merge SHA `eb5894767cebdc7f956e31252b2d1831ef554a85`. Job/artifact wrapper가 event 필드를 제공하지 않는 경우에는 그 한계를 기록하고 event property를 직접 조회했다고 주장하지 않는다.
- PR #272 merge 후 보고서 §105, 증거등록부 §63, 상황판, README, SESSION_LOG, append-only PROJECT_LOG 동기화는 후속 PR에서 수행한다.


### 2026-11-25 PR #273 post-merge 상태 기록
- PR #273 exact-head Run #1593 SUCCESS (15/15, 189 pytest, traceability 406, PDF 3/3, provenance 10-source upload) 후 expected-head squash merge SHA `ce36f290f34a6ce391b91cf3aa6742f48c93e44a`.
- Post-merge main push는 commit-run wrapper가 PR event만 반환하고 combined status가 empty여서 UNVERIFIED. Direct Actions run-list가 불가하면 성공/실패를 추정하지 않고, run ID도 만들지 않는다.
- 다음 동기화 PR에서 이 상태와 공식 제조사 인덱스 재확인 결과를 보고서·증거등록부·상황판·README·SESSION_LOG·PROJECT_LOG에 보존한다.
