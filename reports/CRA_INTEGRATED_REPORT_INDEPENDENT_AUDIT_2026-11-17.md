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


## 6. 공식 EUR-Lex 원문 표본 대조 — 2026-11-17

다음 locator는 EUR-Lex CRA 원문/공식 PDF와 대조했다.

| 조항 | 원문 제목/핵심 | 보고서 반영 상태 |
|---|---|---|
| Article 6 | PDE가 Annex I Part I 요구 및 제조자 프로세스 요구를 충족해야 하는 시장 공급 조건 | §1, §5에서 반영 |
| Article 7(1) | Annex III 제품 카테고리의 core functionality로 Important product 판정; 통합 사실만으로 통합 제품이 자동 분류되지 않음 | §3.4의 제품 경계 원칙과 일치 |
| Article 10 | Enhancing skills in a cyber resilient digital environment | §11.1의 기존 오인용 정정 설명과 일치 |
| Article 11 | General product safety — CRA가 다루지 않는 위험에 대해 GPSR 일부 조항이 적용되는 조건 | §11.1의 기존 오인용 정정 설명과 일치 |
| Article 14 / 71(2) | 신고 의무 2026-09-11 적용 | §1, §4, §6에서 반영 |
| Article 69(2)–(3) | 2027-12-11 이전 출시 제품의 substantial modification 규칙 및 Article 14의 별도 적용 | §4.1에서 분리 반영 |
| Article 32 | 일반/중요/핵심 제품에 따른 적합성 평가 경로 | §1, §5.4, §7에서 반영 |
| Regulation (EU) 2025/327 Article 104 | CRA Article 13(4), 31(3), 32(5a) 관련 개정의 적용 예정일 2027-03-26 | §2.3에서 미래 적용일로 구분 |

- EUR-Lex CRA: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- CRA 공식 PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024R2847
- EHDS Regulation (EU) 2025/327 공식 PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202500327
- 이 표본 검토는 전체 35개 requirement row의 전수 검토를 의미하지 않는다. 나머지 Article/Annex locator 및 Guidance PDF locator 대조는 계속한다.


## 7. Commission Guidance PDF paragraph/page locator 재대조

CI artifact Run #702의 원본 PDF를 다운로드해 SHA-256 manifest와 대조한 뒤, PDF 본문 추출 텍스트에서 각 claim의 paragraph number 및 인쇄 페이지 번호를 다시 확인했다. PDF physical page index와 문서에 인쇄된 page number를 혼동하지 않도록 인쇄 페이지 번호를 CSV에 기록했다.

| Claim | Paragraph/use case | 이전 CSV page | 재대조 결과 | 조치 |
|---|---|---|---|---|
| G-001 | §2.4 paras. 25–26 | pp.10–11 | pp.10–11 | 유지 |
| G-002 | §2.5 paras. 26–28 | pp.11–12 | p.11 | 수정 |
| G-003 | §2.6 paras. 29–32 | pp.11–12 | pp.11–12 | 유지 |
| G-004 | §2.7 paras. 33–39 | pp.13–15 | pp.13–15 | 유지 |
| G-005 | §4.3 paras. 104–107 | pp.34–37 | pp.34–35 | 수정 |
| G-006 | §5 paras. 126–128 | pp.42–43 | p.42 | 수정 |
| G-007 | §6/§6.1 paras. 136–144 | pp.47–50 | pp.47–50 | 유지 |
| G-008 | §7.1–§7.3 paras. 163–173 | pp.57–60 | pp.58–61 | 수정 |
| G-009 | §7.4 paras. 174–177 | pp.60–61 | p.61 | 수정 |
| G-010 | §8.1 paras. 178–190 | pp.63–67 | pp.63–65 | 수정 |
| G-011 | §8.3.4 Industrial robot use case | p.73 | p.73 | 유지 |
| G-012 | §9.3.2 paras. 255–257 | pp.81–82 | p.83 | 수정 |
| G-013 | §4.1–§4.2 Example 39 | pp.30–33 | p.33 | 수정 |

- 8개 claim의 page locator를 좁히거나 정정했다. paragraph locator 자체는 모두 PDF 추출 텍스트에서 확인됐다.
- G-008/G-009 및 G-012는 PDF physical page index가 아니라 인쇄된 페이지 번호로 변환했을 때 기존 값과 차이가 확인됐다.
- 이 변경은 해석 내용 자체를 새로 확장한 것이 아니라 기존 paraphrase가 가리키는 원문 위치를 정확히 하는 조치다.
- Commission-hosted primary PDF byte identity는 여전히 미확인이다. 이번 재대조는 검증된 ANFR mirror byte identity의 artifact에 한정된다.


## 8. SBOM 의무 — Annex I와 Annex VII의 구분

- EUR-Lex 원문 Annex I Part II(1)은 제조자에게 제품의 취약점·구성요소 식별/문서화와 함께 통상 사용되는 기계 판독 형식의 SBOM 작성(최소 최상위 의존성)을 요구한다.
- Annex VII(2)(b)는 SBOM을 취약점 처리 프로세스에 관한 기술문서 내용에 포함한다.
- Annex VII(8)은 해당되는 경우 시장감시당국의 합리적 요청 및 Annex I 적합성 확인에 필요한 경우 SBOM 추가 제출을 규정한다. 이 조항을 근거로 Annex I Part II(1)의 기본 SBOM 작성 의무를 선택사항으로 해석해서는 안 된다.
- 사용자에 대한 일반 공개 의무와 제조자의 SBOM 작성/기술문서 보유 의무는 별개다. Annex II(9)는 제조자가 SBOM을 사용자에게 제공하기로 결정한 경우 접근 위치 정보를 제공하도록 규정한다.
- 공식 근거: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32024R2847 (Annex I Part II(1), Annex II(9), Annex VII(2)(b), (8)).


## 9. CRA-001~CRA-035 법령 참조 1차 인벤토리 검토

- 요구사항 CSV의 35개 행에 기재된 CRA Article/Annex 참조를 1차로 훑어, 조항 번호와 법령 구조가 맞지 않는 명백한 locator 오류는 현재까지 발견하지 못했다.
- 특히 다음 묶음은 EUR-Lex 원문과 조항의 제목/핵심 문언을 대조했다.
  - CRA-001~CRA-006: 적용범위·PDE/RDPS 정의·위험평가·Annex I Part I 및 SBOM/구성요소 의무
  - CRA-007~CRA-018: Annex I Part II 취약점 처리, 지원기간, 업데이트 보존, 기술문서, 사용자 정보, 지원 종료일
  - CRA-019~CRA-020 및 CRA-027: EU DoC/CE, Annex III/IV 분류, Article 32 평가 절차, harmonised standards의 OJ 인용 여부
  - CRA-021~CRA-023 및 CRA-033: Article 14 의무 신고와 Article 15 자발적 신고의 시간표·범위 구분
  - CRA-025~CRA-026: Article 69 전환 규칙과 Machinery Regulation Annex III §§1.1.9/1.2.1의 제한된 위험 범위
  - CRA-028~CRA-034: 경제운영자 및 제조자 책임 전이, 양산 적합성 유지, 식별·DoC·시정조치 의무
  - CRA-035: Article 2(2)–(7) 적용 제외/중첩 검토 범위
- 이 결과는 35개 행의 모든 문장과 모든 적용 조건을 법률가 수준으로 확정했다는 의미가 아니다. 제품별 사실관계 및 세부 조건의 검토는 계속하며, 미확인 상태를 적합 판정으로 바꾸지 않는다.


## 10. 독립 감사 추가 — CRA 법령 문언 Batch 1 (2026-11-18)

- 검토 파일: [CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md](CRA_LEGAL_SEMANTICS_AUDIT_2026-11-18.md), 대상 CRA-001–CRA-010.
- 공식 원문: EUR-Lex Regulation (EU) 2024/2847, https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng.
- 주요 locator 정정: CRA-003에서 Article 13(2)를 원격 데이터 처리 근거에서 제외하고 Article 3(2)/Recital 11–12로 교체. CRA-006에서 SBOM 근거를 Annex I Part II(1), Article 13(7), Annex VII(2)(b)/(8)로 세분화하고 Article 13(5)는 제3자 구성요소 due diligence로 분리. CRA-001은 Article 3(8)–(10)/Recital 9를 보강.
- 해석 통제: Article 3(22) market-availability는 연결성 테스트와 별개. Annex VII(8) 당국 요청 제출은 SBOM 기본 작성 의무를 조건부로 만들지 않는다. Annex I Part II(3)의 regular testing은 법정 고정 주기를 특정하지 않는다. Part II(4)의 정당한 공개 지연 예외를 반영한다.
- 범위 제한: 10개 행의 1차 문언 대조이며 exhaustive legal opinion이나 제품별 적합성 판정이 아니다. 미검증 제품 사실은 미확정으로 유지.


## 11. 독립 감사 추가 — CRA 법령 문언 Batch 2 (2026-11-18)

- 검토 파일: [CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md](CRA_LEGAL_SEMANTICS_AUDIT_BATCH2_2026-11-18.md), 대상 CRA-011–CRA-020.
- 공식 근거: EUR-Lex Regulation (EU) 2024/2847, Articles 13(12)–(20), 28, 30–32, Annex I Part II(7)–(8), Annex II, Annex III–IV, Annex V–VII.
- 확인된 중요 조건: single point of contact는 자동화 도구만으로 제한 불가; 무상 보안 업데이트 예외는 tailor-made PDE + business user + 제조자 합의; 5년 미만 support period는 예상 사용기간이 5년 미만인 경우; 기술문서 작성/갱신과 보관은 별도; full/simplified DoC는 Annex V/VI 구분.
- 분류/평가: Annex III/IV core functionality 기준, 단순 통합만으로 host product에 Important 분류가 전이되지 않음. Article 32(2) Class I 조건부 평가와 (3) Class II, (4) Critical 절차를 분리했다.
- 범위 제한: 10개 행의 1차 심층 대조이며 법률가 의견서나 특정 제품의 분류·적합성 판정이 아니다.


## 12. 독립 감사 추가 — CRA 법령 문언 Batch 3 (2026-11-18)

- 검토 파일: [CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md](CRA_LEGAL_SEMANTICS_AUDIT_BATCH3_2026-11-18.md), 대상 CRA-021–CRA-035.
- 공식 CRA 근거: Articles 14–17, 18–23, 27, 69, 71, Article 2(2)–(8).
- 관련 sectoral 근거: Regulation (EU) 2023/1230 Article 9(9), Annex III §§1.1.9/1.2.1; Regulation (EU) 2025/327 Article 104/105.
- 주요 정정: CRA-023의 Annex II locator 제거(사건 후 사용자 통지 직접 근거는 Article 14(8)); CRA-026에서 CRA Article 69(1)을 일반 중복 근거로 사용하지 않도록 정정(기존 certificate/approval decision 전환 조항); CRA-028/034를 Articles 18–22 역할 책임과 Article 23 공급망 추적으로 분리; CRA-035에 Article 2(8) 추가 및 Article 2(5) delegated-act 조건부 제한을 명시.
- Article 14 신고기한의 기산점을 별도 구분: actively exploited vulnerability final report는 corrective/mitigating measure available 후 14일, severe incident final report는 incident notification 제출 후 1개월.
- Regulation 2025/327 Article 104 개정은 EHR systems 특칙으로 한정한다.
- 범위 제한: 15개 행의 1차 심층 대조이며 법률가 의견서나 특정 제품의 적용/적합성 판정이 아니다.
