# CRA 법령 문언 심층 감사 — Batch 1 (CRA-001–CRA-010)

- 기준일: 2026-11-18 (KST)
- 검토 범위: 요구사항 추적표 CRA-001–CRA-010
- 1차 법령 기준: Regulation (EU) 2024/2847, EUR-Lex 공식 OJ HTML/ELI
- 공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- 보조 공식 PDF/원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 판정 원칙: 조항 locator가 존재한다는 사실과, 요구사항 설명 전체가 법적 문언을 정확히 반영한다는 판단을 분리한다. 제품 사실이 없는 적용성은 미확정으로 유지한다.

## 행별 검토 결과

| ID | 원문 대조 결과 | 수정/보완 사항 | 상태 |
|---|---|---|---|
| CRA-001 | Article 2(1)은 제품의 intended purpose 또는 reasonably foreseeable use에 직접/간접 논리적·물리적 데이터 연결이 포함되는 제품을 범위로 규정. Article 3(1)은 PDE 정의, 3(22)는 making available on the market 정의. | 조항 locator 자체는 유효. 다만 연결 판단을 Article 3(22)에 귀속시키면 안 된다. Article 3(8)–(10)의 logical/physical/indirect connection 정의와 Recital 9를 연결 근거로 추가 권고. Article 3(22)는 상업활동상 시장 공급 여부를 설명하는 별도 게이트로 분리. | 보완 필요 |
| CRA-002 | Article 3(1)은 소프트웨어/하드웨어 제품, remote data processing solutions 및 별도 시장 출시 구성요소를 PDE 정의에 포함. | 적절. 제품 경계에는 구성요소가 별도 공급되는지, 해당 소프트웨어/하드웨어가 PDE인지도 별도 판정해야 함. Recital 11–12의 제조자 책임 하 원격처리 및 제품 기능 필수성도 함께 명시 권고. | 1차 적정 |
| CRA-003 | Article 3(2)는 제조자 또는 제조자 책임하 개발된 원격 데이터 처리로, 그 부재가 PDE 기능 중 하나의 수행을 막는 경우로 한정. Recital 11–12는 제품 기능 수행에 필요한 원격처리만 제품 범위에 포함하며, 단순 웹사이트/제조자 책임 밖의 클라우드는 제외한다고 설명. | 현재 Article 13(2)는 일반 사이버보안 위험평가 조항으로 remote data processing 정의의 근거가 아님. 법적 locator에서 Article 13(2)를 삭제하고 Article 3(2), Recital 11–12를 중심으로 재구성. Guidance §8은 해석 보조로 유지. | locator 수정 필요 |
| CRA-004 | Article 13(2) 위험평가 수행, (3) 위험평가 최소 내용/갱신, (4) 기술문서 포함 및 비적용 요구사항의 명확한 정당화. Annex VII(3)은 위험평가 문서 항목. | 적절. 적용성 판단은 intended purpose, reasonably foreseeable use, 사용조건/운영환경, 보호자산 및 예상 사용기간에 근거해야 함. 비적용은 단순 공란이 아니라 기술문서상 명확한 정당화 필요. | 1차 적정 |
| CRA-005 | Annex I Part I(1)은 secure-by-design 요구, Part I(2)는 제품 특성에 따른 보안 요구를 규정. Article 13(3)은 Part I(2)의 적용 여부 및 구현 방식과 Part I(1) 적용 방식을 위험평가에 기록하도록 함. | locator 적절. 다만 모든 하위 요구가 모든 제품에 동일하게 기계적으로 적용된다고 표현하지 말고, 해당 제품의 특성/위험에 따른 적용성 판단 및 비적용 근거를 기술문서에 남기는 구조로 표현. | 1차 적정 |
| CRA-006 | Annex I Part II(1)은 취약점·구성요소 식별/문서화와 SBOM 작성, 통상 사용되는 기계판독 형식, 최소 최상위 의존성 포함을 요구. Article 13(7)은 관련 사이버보안 측면/인지 취약점/제3자 정보를 체계적으로 문서화. Annex VII(2)(b)는 취약점 처리 프로세스 기술문서에 SBOM을 포함. Annex VII(8)은 필요 시 합리적 당국 요청에 따른 추가 제출을 규정. | Article 13(5)는 제3자 구성요소 통합 시 due diligence 근거이지 SBOM의 직접 locator가 아님. 13(5)는 공급망 실사 문맥으로 분리하고, SBOM locator에는 Annex I Part II(1), Article 13(7), Annex VII(2)(b)를 명시. Annex VII(8)을 기본 SBOM 작성의 조건처럼 오독하지 않도록 기존 PR #42 설명 유지. | locator 보완 필요 |
| CRA-007 | Annex I Part II(2)는 위험에 비례해 취약점을 지체 없이 처리/수정하고 보안 업데이트를 제공하도록 함. 기술적으로 가능한 경우 신규 보안 업데이트는 기능 업데이트와 분리. Article 13(8)은 시장 출시 시점부터 지원기간 동안 제품 및 구성요소 취약점을 효과적으로 처리하도록 함. | 적절. '지원기간 동안'은 Article 13(8)의 명시 범위. 업데이트 분리는 '기술적으로 가능한 경우' 조건부. 개별 수정 SLA나 고정 일수는 이 조항만으로 창설되지 않으므로 별도 법령/표준/계약과 구분. | 1차 적정 |
| CRA-008 | Annex I Part II(3)은 제품 보안의 효과적이고 정기적인 테스트 및 검토를 요구. | 적절. Regulation은 이 항목에서 구체적인 월/분기/연간 주기를 직접 정하지 않음. 제품 위험·변경·취약점 추세를 반영해 제조자가 합리적 주기를 정하고 기록하도록 설계 권고. | 1차 적정 |
| CRA-009 | Annex I Part II(4)는 보안 업데이트가 제공된 후 수정된 취약점 정보의 공유/공개, 제품 식별정보, 영향, 심각도, 사용자 조치 정보를 요구. | 공개 시점 예외 중요: 정당한 사유로 공개의 사이버보안 위험이 이익보다 크다고 제조자가 판단하면, 사용자가 관련 패치를 적용할 기회를 얻을 때까지 공개를 늦출 수 있음. 이를 일반적/무기한 비공개 권한으로 표현하면 안 됨. | 예외 보완 필요 |
| CRA-010 | Annex I Part II(5)는 CVD 정책의 수립 및 집행. Article 13(8) 마지막 문단은 내부·외부 보고 취약점의 처리/수정을 위한 적절한 정책·절차(해당 CVD 정책 포함)를 요구. | 적절. Recital 76은 구조화된 보고·진단·수정 후 상세정보 공개 절차를 설명하고, 필요 시 CSIRT 경유 익명 보고를 언급하지만, 이를 Annex I Part II(5)의 모든 제조자에게 직접 부과된 별도 익명접수 의무로 과장하지 않는다. | 1차 적정 |

## 공통 해석 및 위험 통제

1. Article 2(1)의 연결성 테스트, Article 3(1)의 PDE 정의, Article 3(22)의 상업활동상 making available 테스트는 서로 다른 법적 요소다. 보고서와 매트릭스에서 하나로 합치지 않는다.
2. Article 3(2) 원격 데이터 처리의 핵심은 제조자 설계/책임과 기능 필수성이다. 단순히 인터넷/클라우드를 사용한다는 사실만으로 제조자 제품 경계에 자동 포함하지 않는다.
3. SBOM 기본 작성은 Annex I Part II(1)의 직접 의무다. Annex VII(8)의 당국 요청 제출 조항은 기본 작성 의무를 조건부로 바꾸지 않는다. Annex II(9)는 제조자가 사용자 공개를 결정한 경우의 접근 위치 안내다.
4. 'regular' testing은 법령상 정기 수행 요구이나 법정 고정 주기 숫자는 없다. 제품 위험과 변경 맥락에 따른 주기 근거를 기록한다.
5. 수정 취약점 공개는 기본적으로 보안 업데이트 제공 후이며, Annex I Part II(4)의 정당한 지연 예외를 함께 관리한다.
6. 본 Batch는 법령 문언 및 locator의 1차 심층 대조다. 법률의견서/법률가 검토가 아니며, 특정 서보 드라이브의 CRA 적용·분류·적합성 판정도 아니다.

## 근거 위치 (EUR-Lex)

- Article 2(1)–(8), Article 3(1)–(10),(22): EUR-Lex official text, lines/sections corresponding to Articles 2–3.
- Article 13(2)–(9), (17): EUR-Lex official text, Article 13.
- Annex I Part I(1)–(2), Part II(1)–(8): EUR-Lex official text, Annex I.
- Annex II(2),(9): EUR-Lex official text, Annex II.
- Annex VII(2)(b),(3),(8): EUR-Lex official text, Annex VII.
- Recitals 9, 11–12, 76–77: EUR-Lex official text, recitals.

## 다음 단계
- CRA-011–CRA-020: 제조자 연락창구, 사용자 정보, 지원기간·보존, DoC/CE, 분류 및 Article 32 절차를 행별 검토.
- 이후 CRA-021–CRA-035: 신고 의무, 적용시점/전환, 기계류 규정, 표준화, 경제운영자, 적용 제외/중복을 별도 검토.
- 최종 수정은 모든 행 검토가 끝난 뒤 추적표·통합 보고서·SEC 매트릭스·독립 감사 문서를 하나의 변경 묶음으로 정합화한다.
