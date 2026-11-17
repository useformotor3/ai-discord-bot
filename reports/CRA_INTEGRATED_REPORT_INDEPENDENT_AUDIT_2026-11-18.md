# CRA 통합 보고서 독립 재검토 — 2026-11-18

## 1. 목적과 검토 경계

- 대상: `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` v0.2 및 현재 main의 제품 경계/증거 수집 기준서, 요구사항 추적표, 교차 매트릭스 감사.
- 검토 기준점: main `c7b939a0fdfa559f9d68a11873c107186da423c3` (PR #48 병합 후 상태 기록).
- 검토 방식: 통합 보고서의 핵심 법적 주장과 위험도가 높은 문구를 EUR-Lex 공식 OJ 텍스트와 대조하고, 추적표·독립 감사·제품 증거 intake의 표현 및 상태를 상호 비교.
- 제외: 제품별 적합성 평가, 법률 의견서, 제조사 자료 확인, 보안 구현/시험의 완료 판정.
- 결과 상태: 핵심 법률 locator/기한 표본은 공식 원문과 일치. 일부 결론 문구는 제품별 사실 부재를 더 강하게 드러내도록 편집 보완 권고. 본 검토는 35행 전체에 대한 변호사 수준의 법률 의견이 아니다.

## 2. 공식 원문 대조 결과

| 검토 항목 | 공식 원문 확인 | 보고서/추적표 평가 |
|---|---|---|
| PDE 범위 및 연결성 | CRA Article 2(1), Article 3(1), (8)–(10), Recital 9 | 연결성·시장 공급·제품 정의를 별도 게이트로 구분한 방향이 타당. 실제 모델별 인터페이스/사용 목적 확인 전 Unknown 유지 필요 |
| RDPS | Article 3(2), Recitals 11–12 | 제품 외부 처리, 제품 기능 수행에 필요, 제조자 또는 제조자 책임하 개발이라는 누적 요소를 intake에 반영. 단순 독립 SaaS/IaaS를 자동 포함하지 않는 표현 유지 |
| Annex III Important | Article 7(1)–(2) | 제품 카테고리의 core functionality 기준이며 구성품 통합만으로 호스트 제품 분류가 자동 전이되지 않는다는 보고서 설명과 일치 |
| Annex IV Critical | Article 8(1)–(2) | 카테고리 core functionality 및 인증 scheme/delegated act 조건을 함께 검토해야 함. 제품명/부품만으로 분류 금지 |
| 지원기간 | Article 13(8) | 최소 5년 원칙과 예상 사용기간이 5년 미만인 경우 예외, 제품 특성·사용자 기대 등 고려를 보고서가 반영 |
| 보안 업데이트 보존 | Article 13(9) | 각 보안 업데이트가 발행된 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 이용 가능해야 한다는 구분이 정확. 이를 제조사 지원기간 10년으로 오해하지 않도록 유지 |
| 의무 신고 | Article 14(1)–(8) | 적극 악용 취약점 및 제품 보안에 영향을 주는 심각한 사고를 구분하고 24h/72h/최종 보고 기산점을 분리한 내용이 원문과 일치 |
| 자발적 신고 | Article 15 | Article 14 의무 신고와 구별한 내용이 정확 |
| 기존 제품 전환 | Article 69(1)–(3), Article 71(2) | (1) 타 EU 법령 certificate/approval decision의 유효기간, (2) 기존 출시 제품의 substantial modification, (3) Article 14 예외 적용을 서로 분리한 내용이 정확 |
| SBOM | Annex I Part II(1), Annex VII(2)(b), Annex VII(8), Annex II(9) | 기본 SBOM 작성, 기술문서 포함, 시장감시당국의 합리적 요청, 제조자의 사용자 공개 결정 시 접근정보를 분리한 설명을 유지 |

## 3. 편집·해석상 조치 권고

### AUD-2026-001 — 제품 적용 가능성 문구의 조건부 표현 강화
- 위치: 통합 보고서 §1 요약 2번 및 §1 요약 4번, §3 적용성.
- 관찰: “일반적인 산업용 서보 드라이브는 ... CRA 적용 대상일 가능성이 높다”, “기본 제품 범주일 가능성이 높다”는 문구는 전형적인 디지털 인터페이스/모터제어 기능을 전제로 한 업계 가설이다.
- 위험: 제조사·모델·변형·사용 목적·실제 데이터 연결·시장 공급 구조가 없는 상태에서 독자가 개별 제품에 대한 판정으로 오해할 수 있다.
- 권고: “전형적 구성에 대한 사전 스크리닝 가설이며 제품별 결론이 아님”을 같은 문단에 명시하고, 판정값은 제품 증거가 확보될 때까지 Unknown으로 유지한다.
- 상태: 편집 권고; 법적 locator 오류로 판정하지 않음.

### AUD-2026-002 — 제품별 Unknown 상태의 문서 간 동기화
- 위치: 통합 보고서, `PROJECT_STATUS_CURRENT.md`, 제품 증거 intake, IF/SEC 매트릭스.
- 관찰: 제품별 데이터시트·사용설명서·아키텍처·인터페이스·SBOM이 제공되지 않은 점을 각 관리 문서가 명시한다.
- 조치: 이 상태를 변경하지 않는다. 15개 인터페이스는 제품별 미확인, 36개 SEC controls는 미작성/증거 미확인, 제품 CRA scope/classification/conformity는 Unknown으로 유지한다.
- 상태: 유지 확인.

### AUD-2026-003 — Commission Guidance PDF provenance 제한
- 위치: 통합 보고서 §2.2, Guidance claim register, source provenance manifest.
- 관찰: ANFR mirror의 PDF byte hash 검증은 Commission-hosted 원본 bytes의 동일성 증명이 아니다.
- 조치: primary Commission byte identity가 확인될 때까지 fallback 상태를 유지하고 “Commission 원본 SHA 검증 완료”라고 표현하지 않는다.
- 상태: 미해결; 재검증 필요.

### AUD-2026-004 — 표준화 일정과 법적 적용일 분리
- 위치: 통합 보고서 §7 및 M/606 crosswalk.
- 관찰: M/606의 ESO 납품/채택 일정은 제조자의 CRA 법적 적용일이나 OJ harmonised-standard citation과 동일하지 않다.
- 조치: 기존 구분 유지. 이번 독립 검토에서는 M/606 최신 결정의 원문/Annex bytes를 새로 재취득하지 않았으므로, 2026-11-30 / 2027-01-31 / 2027-10-30 일정은 기존 저장소 근거의 재사용이며 이번 회차 신규 독립 확인으로 표시하지 않는다.
- 상태: 기존 근거 유지; 다음 표준 현황 갱신 시 Commission 결정 원문 재확인.

## 4. 공식 원문 근거 및 확인 위치

- CRA Regulation (EU) 2024/2847, EUR-Lex OJ text: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- Article 7(1)–(2): Important product core functionality 및 통합만으로 자동 전이되지 않는 원칙.
- Article 8(1)–(2): Critical product category 및 delegated act/certification scheme 조건.
- Article 13(8)–(9): support period 기준과 각 security update의 이용 가능 기간.
- Article 14(1)–(8): 의무 신고 트리거, 시간표, CSIRT/ENISA 제출 및 영향 사용자 통지.
- Article 15: voluntary reporting.
- Article 69(1)–(3), Article 71(2): certificate transition, 기존 출시 제품, Article 14 적용일.
- Annex I Part II(1), Annex VII(2)(b)/(8), Annex II(9): SBOM 작성/기술문서/당국 요청/사용자 접근의 구분.

## 5. 검증 한계

- EUR-Lex 공식 HTML의 관련 조항을 직접 열람해 핵심 조항을 표본 대조했다. 전체 35행 CSV의 모든 문장·예외·제품별 적용 전제를 이번 회차에서 다시 전수 검증한 것은 아니다.
- Commission Guidance PDF의 Commission-primary byte identity는 여전히 미확인이다.
- M/606 C(2026) 7861 Annex의 raw bytes 및 최신 OJ harmonised-standard status는 이번 회차 재수집/검증하지 않았다.
- 제조사·정확한 모델·사용설명서·회로도·펌웨어/SBOM·시장 공급 증거가 없으므로 제품별 결론은 내리지 않았다.
- 본 기록은 내부 독립 검토 자료이며 법률 자문, 인증기관 판단 또는 적합성 선언이 아니다.

## 6. 다음 단계

1. AUD-2026-001의 조건부 문구를 통합 보고서 요약에 반영하고, 제품별 Unknown 게이트를 그대로 유지한다.
2. 통합 보고서·추적표·독립 감사·상황판·README·MASTER_PLAN·SESSION_LOG·PROJECT_LOG 간 버전/상태를 동기화한다.
3. Commission-hosted Guidance PDF primary byte identity와 M/606 결정 원문 provenance를 별도 수집 경로로 계속 검증한다.
4. P0 제품 증거(정확한 모델 데이터시트/카탈로그 및 사용설명서)가 확보되면 모델/variant별 evidence IDs로 CRA-001–035와 IF/SEC matrix를 연결한다.
