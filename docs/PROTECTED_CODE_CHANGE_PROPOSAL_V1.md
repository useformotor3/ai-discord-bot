# 운영 CRA 조사 자동화 코드 개선 제안서 — 승인 전 검토본

- 문서 ID: CRA-AUTO-CHANGE-001
- 버전: 1.0
- 기준일: 2026-11-13
- 상태: **변경 제안 / 구현 승인 대기**
- 보호 대상: `main.py`, `.github/workflows/run.yml`, Gemini 명령 템플릿·모델/폴백·운영 저장 흐름
- 현재 작업 브랜치에서 확인한 보호 파일 SHA:
  - `main.py`: `997952702fdd9d2472468b82e6efdd65b2bb4376`
  - `.github/workflows/run.yml`: `65a8cadc8eac593f551e390698e367b1d161ecf1`
  - `prompts/CRA_RESEARCH_PROMPT_V2.txt`: `14e9ce8618bc447a371dc28fc725cda3636470c5`

> 이 문서는 변경 전 검토안이다. 위 파일은 이 제안서 작성 과정에서 수정하지 않았다. 구현은 별도 명시 승인 후 작업 브랜치에서만 수행한다. main 병합·rebase·동기화는 별도 승인 없이는 하지 않는다.

## 1. 문제 정의

현재 운영 자동화의 주된 결과물은 Gemini가 생성한 자유형 CRA 조사 텍스트를 Discord와 `research_archive`에 저장하는 것이다. 저장 성공은 조사 품질이나 법령 정확성의 증거가 아니다. 과거 아카이브 감사에서 법령 조항·Annex 위치·직접 인용·제품 분류 오류가 반복 확인되었다.

프로젝트가 달성해야 할 것은 보고서 개수 증가가 아니라 **검증 가능한 보고서 파일과 제품 적용 산출물의 누적**이다.

## 2. 변경 목표

1. 조사 생성물과 검증 완료 근거를 분리한다.
2. 공식 원문을 확보하지 못하면 직접 인용을 생성하지 않는다.
3. 법령·제조사·표준 자료의 출처 메타데이터와 문서 버전을 구조화한다.
4. 각 주장에 source ID, 원문 위치, claim type, verification status, product applicability를 연결한다.
5. CRA 요구사항을 HW/FW 설계·시험·증거 ID에 매핑한다.
6. 검증 실패·모델 실패·빈 응답·저장 실패를 성공으로 기록하지 않는다.
7. 보고서는 단일 파일 크기 한계에 따라 여러 권/장으로 분리하되 master index와 stable IDs로 연결한다.
8. 완전 무료 운영 원칙을 유지하고 유료 API/서비스를 자동 호출하지 않는다.

## 3. 목표 파이프라인

1. **Scope Resolver**: 제품 SKU, intended purpose, EU 공급형태, 제품 경계 입력을 확인한다.
2. **Research Planner**: 요구사항 ID와 지식 인덱스를 기준으로 미해결 주제를 선정한다. 최근 5개 snippet만으로 중복 방지하지 않는다.
3. **Official Source Registry**: 허용된 공식 도메인, canonical URL, 문서번호, 버전, 날짜, hash, 취득시각을 기록한다.
4. **Controlled Fetch**: E1/E2 검증 transport를 재사용한다. 실제 외부 fetch는 E3 별도 승인 범위 안에서만 켠다.
5. **Extraction & Evidence**: 원문 텍스트/문단 위치를 추출하고 직접 인용과 요약을 구분한다.
6. **Claim Validator**: 조항/Annex/문서 버전/인용 문자열/주장 범위 검증. 불일치·모호성은 자동 탈락 또는 사람 검토.
7. **Applicability Mapper**: 법령상 의무와 제품 적용 여부를 분리한다. 제품 사실이 없으면 UNKNOWN/UNVERIFIED.
8. **Design Mapper**: HW/FW/통신/제조/서비스 설계 후보와 인터페이스·시험·증거 ID 연결.
9. **Report Builder**: Markdown 원본을 권/장으로 출력하고 master index를 갱신한다.
10. **Quality Gate**: 문서 링크, source ID, 요구사항 ID, 중복, 누락, 상태값, 인용 검증을 자동 검사.
11. **Publish**: draft/verified 영역을 분리해 저장한다. 검증 전 문서는 VERIFIED 폴더/상태로 이동 금지.

## 4. 보고서 데이터 계약 제안

각 claim은 최소한 다음 필드를 가져야 한다.

| 필드 | 의미 |
|---|---|
| claim_id | 안정적 고유 ID |
| claim_text | 한 개의 검증 가능한 주장 |
| claim_type | legal_requirement / manufacturer_fact / interpretation / design_proposal / test_result |
| source_id | 공식 출처 레지스터 ID |
| source_url | canonical URL |
| document_id/version/date | 문서 식별·개정 정보 |
| locator | Article/Annex/section/page/paragraph |
| quote_original | 원문 직접 인용. 검증 전에는 null |
| translation_or_summary | 번역/요약. 직접 인용과 분리 |
| verification_status | VERIFIED/PARTIAL/CONFLICT/UNVERIFIED |
| product_applicability | APPLICABLE/NOT_APPLICABLE/UNKNOWN |
| design_mapping | HW/FW/interface/control IDs |
| test_mapping | test IDs |
| evidence_refs | 증거 파일·hash·run ID |
| reviewer/date | 사람 검토 기록 |

## 5. 단계별 변경안

### Phase A — 안전한 보고서 계약·검증 게이트
- 현재 검증된 schema/validator를 재사용하고 필요한 필드·상태 전이를 검토한다.
- 모델 출력이 검증 계약을 통과하지 못하면 저장은 가능하더라도 DRAFT/REJECTED로 격리한다.
- 운영 상태/이력은 실행 실패를 성공 카운트로 기록하지 않도록 별도 검토한다.
- mock fixture로 성공/실패/부분 응답/중복/인용 오류/미확인 제품 사실을 테스트한다.

### Phase B — 공식 근거와 claim 연결
- 공식 source registry, source fetch result, extraction result, claim record를 연결한다.
- fetch 미실행 상태에서 AI가 출처를 읽었다고 주장하지 못하도록 한다.
- 원문 인용은 quote validator를 통과해야만 출력한다.
- E3 실시간 수집 기능은 E3 승인 전 비활성/미호출 상태로 둔다.

### Phase C — 제품 적용·설계·시험 매핑
- 요구사항 ID ↔ 제품 사실 ↔ 위험 ↔ HW/FW 통제 ↔ 인터페이스 ↔ 시험 ↔ 증거를 연결한다.
- 제품 SKU/MCU 미확정은 UNKNOWN 상태로 남긴다.
- 기능안전 요구와 CRA 요구는 서로 다른 분류·증거 체계로 유지한다.

### Phase D — 보고서 파일 빌드·배포
- Markdown 원본 권/장 분리, master index, 변경 이력 생성.
- 링크·참조·ID·문서 버전 검사.
- DOCX/PDF/PPTX/XLSX 변환은 사용자 기기에서 무료로 열 수 있는 포맷/워크플로를 확인한 뒤 구현한다.
- 파일 크기 제한 초과 시 장 단위 분할하고 누락 없이 인덱스에서 연결한다.

## 6. 현재 제안 우선순위

| 우선순위 | 변경 | 이유 |
|---|---|---|
| P0 | 원문 미확보 시 직접 인용 차단 | 법령 오인용 방지 |
| P0 | 실패/빈 응답/검증 실패의 성공 처리 금지 | 운영 상태 신뢰성 |
| P0 | 제품 적용성 UNKNOWN 강제 | 일반 설계안을 제품 적합성으로 오인하는 위험 차단 |
| P1 | Claim-Source-Requirement-Design-Test 연결 | 보고서가 실제 설계로 이어지도록 함 |
| P1 | 1,347개(현재 main 관측치) 아카이브 인덱스 및 주제/조항 분류 | 중복·누락을 데이터 기반으로 파악 |
| P1 | master report 권/장 자동 생성 | 실제 산출물 지속 생성 |
| P2 | DOCX/PDF/PPTX/XLSX 배포 | 검토·공유 편의 |
| P2 | 무료 한도·재시도·Discord 전송 신뢰성 | 운영 안정성 |

## 7. 영향 및 위험

- 변경 대상은 운영 자동화의 입력·검증·저장 동작에 영향을 줄 수 있다.
- 잘못된 상태 전이로 검증되지 않은 보고서가 VERIFIED로 표시될 위험이 있으므로 fail-closed 기본값을 사용한다.
- 아카이브 원본은 수정/삭제하지 않고 새 인덱스·검증 레코드를 추가한다.
- 기존 history/state의 의미를 바꾸지 않고 새 스키마를 별도 파일로 도입하거나 마이그레이션 검증을 거친다.
- 무료 티어 호출량은 실제 공급자 정책·계정 상태로 검증한다. 기존 `MAX_DAILY_QUOTA=1200`을 공급자 공식 한도로 표현하지 않는다.
- 외부 fetch는 E3 승인 전 수행하지 않는다.

## 8. 테스트·검증 계획

- Unit: claim schema, source metadata, quote match, status transition, report split/index.
- Negative: empty model response, timeout, malformed JSON, missing source, wrong article, quote mismatch, unknown SKU, duplicated claim, broken reference.
- Integration mock: planner → generated draft → validator → report builder → archive index.
- Regression: 기존 126개 테스트 및 archive strict audit.
- CI: 정확한 commit SHA, run URL, 모든 job/step, test count, strict archive counts를 확인한다.
- 운영 API/Discord/Gemini 실제 호출 테스트는 별도 승인 없이는 수행하지 않는다.

## 9. 롤백

- 작업 브랜치에서 변경 전 보호 파일 SHA와 비교한다.
- 실패 시 작업 브랜치의 변경 commit을 식별하고 revert commit으로 되돌린다. main에는 반영하지 않는다.
- 아카이브 원본·history 원본을 삭제/덮어쓰지 않는다.
- 검증기/리포트 빌더는 이전 버전으로 전환 가능한 버전 구분을 둔다.

## 10. 승인 요청

아래 범위별로 별도 승인이 필요하다.

- [ ] A단계: 신규 비운영 모듈/스키마/테스트만 구현
- [ ] B단계: E3 별도 승인 범위 내 공식 URL fetch/extraction 구현
- [ ] C단계: 제품 적용/설계/시험 매핑 기능 구현
- [ ] D단계: 문서 변환/배포 자동화 구현
- [ ] 보호 파일(`main.py`, 운영 workflow, Gemini prompt/명령 템플릿) 변경 — diff/영향/테스트 계획 확인 후 별도 승인
- [ ] main 병합/PR 병합 — 별도 승인

**현재 승인 상태:** 이 제안서 작성 및 보고서 초판 생성만 수행. 운영 코드·보호 파일·실제 외부 fetch·main 반영은 수행하지 않음.
