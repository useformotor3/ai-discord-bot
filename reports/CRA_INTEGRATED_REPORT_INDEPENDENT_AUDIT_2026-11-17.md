# 통합 CRA 보고서 독립 검토 기록

- 기준일: 2026-11-17
- 대상: `reports/CRA_INTEGRATED_COMPLIANCE_REPORT_2026-11-17.md` 및 연결된 CRA 추적성 자료
- 검토 성격: 편집·법령 인용·근거 연결의 2차 검토
- 제품별 적합성 판정: 수행하지 않음 (제조사/정확한 모델/데이터시트/사용설명서/BOM/SBOM 미제공)

## 1. 검토 범위와 확인 자료

1. 통합 CRA 보고서 v0.2
2. Commission Guidance claim register G-001~G-013
3. CRA requirements traceability CRA-001~CRA-035
4. Security control/test matrix SEC-001~SEC-036
5. Interface applicability matrix IF-001~IF-015
6. M/606 Annex I 41-item relevance crosswalk
7. PDF source provenance manifest 및 CI Run #781/#789 source canary 결과
8. EUR-Lex CRA Regulation (EU) 2024/2847 원문/통합 정보 및 Regulation (EU) 2025/327 Article 104 개정 참조

## 2. 발견 사항 및 조치

| ID | 유형 | 발견 내용 | 조치/판정 | 상태 |
|---|---|---|---|---|
| AUD-001 | 문서 구조 | 본문 기존 §11–§13 뒤에 Guidance/M/606/제품 증거 섹션이 다시 §11–§13으로 추가되어 번호가 중복됨 | 추가된 세 섹션을 §14–§16으로 재번호 | 수정 완료 |
| AUD-002 | 법적 분류 용어 | 요약의 Annex III/IV 분류 표현이 '중요 제품'과 '중요·핵심 제품'을 혼용해 의미가 모호함 | Annex III Important products Class I/II와 Annex IV Critical products로 구분해 문구 수정 | 수정 완료 |
| AUD-003 | M/606 taxonomy | M/606 1–14는 horizontal property, 15는 horizontal vulnerability-handling으로 분류되나 보고서의 요약 표현은 두 하위 범주를 구분하지 않음 | 1–14와 15의 하위 범주를 명시하되 모두 horizontal topics임을 유지 | 수정 완료 |
| AUD-004 | 공식 원문 증거 | Commission Guidance PDF의 raw-byte SHA-256은 ANFR mirror에서 확인됐으나 Commission-hosted primary byte identity는 provenance상 미확인 | 보고서에 이 한계를 유지. mirror를 Commission 원본과 동일 출처라고 과장하지 않음 | 미해결/투명 공개 |
| AUD-005 | 제품별 적용성 | 특정 제조사/모델/제품 구성 증거가 없음 | PDE 적용성·Annex III/IV 분류·RDPS·적합성은 잠정/미확정 유지. 제품 증거 수집 기준서로 연결 | 증거 대기 |

## 3. 법령 교차 확인 포인트

- CRA Article 6: 제품 PDE의 필수 사이버보안 요구사항 준수 조건.
- Article 7 및 Annex III: 제품의 core functionality가 열거된 카테고리에 해당하는지로 Important product 분류. 카테고리 기능을 가진 제품이 다른 제품에 통합되었다는 사실만으로 통합 제품 전체가 자동 분류되지는 않는다는 Article 7(1)의 문언을 함께 적용.
- Article 8 및 Annex IV: Critical product 카테고리 검토.
- Article 13(8)–(9): 지원기간은 제품의 예상 사용기간 및 기타 법정 요소에 따라 정하고, 각 보안 업데이트의 제공 기간을 지원기간과 별도로 계산.
- Article 14 및 Article 71(2): Article 14 신고 의무의 적용일은 2026-09-11.
- Article 69(2)–(3): 2027-12-11 이전 출시 제품의 실질적 변경 규칙과 Article 14의 기존 제품 적용을 분리.
- Article 32: 제품 분류에 따라 적합성 평가 절차를 결정.
- Regulation (EU) 2025/327 Article 104: CRA Article 13(4), Article 31(3) 및 Article 32(5a) 관련 개정. 이 개정의 적용 예정일(2027-03-26)을 2026-11-17 현재 이미 적용 중인 의무로 표현하지 않도록 관리.

## 4. 검증 제한 및 남은 작업

- 이 검토는 법령·문서의 내부 일관성과 2차 검토이지 법률 자문, 인증기관 평가 또는 제품 적합성 선언이 아니다.
- M/606은 표준화 요청/납품 계획이다. 해당 문서의 ESO adoption deadline과 OJ에 인용된 harmonised standard 여부를 분리한다.
- Commission Guidance는 해석자료이며 Regulation 본문보다 우선하지 않는다.
- Guidance PDF는 현재 mirror byte identity를 검증했지만 Commission primary byte identity는 pending이다. primary URL이 정상적으로 검증되면 provenance를 갱신한다.
- 다음 검토에서는 각 CRA-001~CRA-035 요구사항의 Article/Annex locator를 법령 원문과 한 줄씩 대조하고, G-001~G-013의 PDF paragraph/page locator를 PDF 텍스트와 페이지 이미지에 표본 재대조한다.
- 제품별 자료가 제공되면 정확한 모델 데이터시트·사용설명서를 우선 증거로 제품 경계를 확정한 뒤 인터페이스, RDPS, BOM/SBOM 및 보안 통제를 연결한다.

## 5. 공식 원문 링크

- CRA Regulation (EU) 2024/2847: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- CRA official PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024R2847
- Regulation (EU) 2025/327: https://eur-lex.europa.eu/eli/reg/2025/327/oj/eng
- CRA Article 14 / application dates are also recorded in the project source provenance and CI canary outputs.
