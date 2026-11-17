# CRA 전체 교차 매트릭스 일관성 감사 — 2026-11-18

## 목적과 범위
CRA-001–CRA-035 법령 문언 심층 감사(Batch 1–3) 결과가 제품 인터페이스 적용성 표, 보안 통제·시험 매트릭스, Commission Guidance claim register, M/606 Annex I 매핑과 일치하는지 확인했다.

검토 파일:
- `reports/CRA_REQUIREMENTS_TRACEABILITY_2026-11-17.csv` — 35 requirements
- `reports/CRA_SERVO_DRIVE_INTERFACE_APPLICABILITY_2026-11-17.csv` — 15 interfaces
- `reports/CRA_SERVO_DRIVE_SECURITY_CONTROL_TEST_MATRIX_2026-11-17.csv` — 36 controls
- `reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv` — 13 non-binding claims
- `reports/CRA_M606_ANNEX_I_SERVO_DRIVE_RELEVANCE_2026-11-17.csv` — 41 standardisation topics

## 교차 참조 불일치 및 반영

| 대상 | 발견 사항 | 정합화 조치 |
|---|---|---|
| SEC-015 ↔ CRA-006/024 | SBOM control locator가 Annex I Part II(1), Article 13(5)만 표시하여 Article 13(7), Annex VII(2)(b)/(8) 누락. 13(5)는 due diligence 문맥. | SBOM locator에 Article 13(7), Annex VII(2)(b)/(8) 추가. Article 13(5)는 구성요소 due diligence와 별도 검증하도록 설명 수정. |
| SEC-018 ↔ CRA-009 | 수정 취약점 공개 지연 예외가 시험 설명에 충분히 드러나지 않음. | 보안 업데이트 제공 후 공개 원칙 및 공개 위험이 이익보다 크다는 정당한 사유가 있는 경우 사용자 패치 적용 기회까지 지연하는 예외를 시험 항목에 추가. |
| SEC-021 ↔ CRA-012 | 서명/무결성/전송보호를 법령이 직접 열거한 단일 구현 요구처럼 읽을 수 있음. | 안전한 배포 메커니즘은 법적 목표로, 서명/무결성/전송보호는 위험기반 구현 후보/증거로 분리. |
| SEC-031 ↔ CRA-003 | Article 13(2)를 remote data processing solution 정의 근거로 잘못 연결. | Article 13(2) 제거, Article 3(2) 및 Recital 11–12로 정정. |
| SEC-032 ↔ CRA-001 | 데이터 연결 판단 locator가 Article 3(8)–(10)/Recital 9를 반영하지 못함. | Article 2(1), Article 3(1),(8)–(10), Recital 9 및 Guidance §2.5로 정합화. |
| SEC-034 ↔ CRA-028/032/034 | 경제운영자 역할, 제조자 책임 전이, Article 23 공급망 추적이 한 control에 연결되어 법적 근거가 불명확. | cross-cutting SEC-034의 통합 범위는 유지하되 Article 18–23을 명시하고, CRA-028(Articles 18–22), CRA-034(Article 23)로 requirement-level trace를 분리. |
| SEC-036 ↔ CRA-025 | Article 69(1) certificates transition을 substantial modification/기존 제품 일반 판단에 함께 묶음. | Article 69(2)–(3), Article 71(2)만 남김. Article 69(1)은 기존 타 법령 certificate/approval decision 유효성 이슈가 있을 때 별도 확인. |

## 기존 매트릭스에서 유지한 올바른 구분

### 인터페이스 적용성 (15 rows)
- IF-001–IF-008, IF-013: 실제 프로토콜/디지털 명령·상태·설정 교환이 의도된 사용에 포함되는지 제품별 증거로 확인.
- IF-009/010/012: 단순 아날로그 값 또는 on/off/hardwired trigger만으로 데이터 연결을 단정하지 않음.
- IF-011: 엔코더 펄스/직렬 디지털 프로토콜과 제품 경계를 별도 확인.
- IF-014: commissioning PC tool은 intended function에 필수인지, 제품과 함께 제공/책임지는지 Guidance 기준으로 판단.
- IF-015: Article 3(2) 제조자 책임 및 기능 필수성 요건을 누적 적용. 단순 독립 SaaS는 자동 포함하지 않음.
- 모든 15개 인터페이스는 일반 예시이며 특정 모델에서 실재/활성 여부가 확인되지 않았으므로 상태를 '제품별 미확인'으로 유지.

### Commission Guidance claim register (13 claims)
- Guidance claims는 비구속적 해석 보조로 유지하고, 법적 의무 locator와 혼합하지 않는다.
- G-002 데이터 연결, G-005 substantial modification, G-006 support period, G-007 core functionality, G-010/011 RDPS, G-012 machinery certificate scope, G-013 spare part interpretation의 claim-to-requirement links를 확인했다.
- Commission Guidance PDF는 ANFR mirror fallback hash를 검증했으나 Commission-hosted primary bytes 동일성은 아직 미확인. claim register는 이 한계를 그대로 유지한다.

### M/606 Annex I (41 items)
- 1–14는 horizontal product properties, 15는 horizontal vulnerability-handling topic으로 분리한다.
- 16–41은 vertical product-type/interface topics로 취급하고, 제품의 core functionality 또는 실제 product boundary가 확인되기 전에는 조건부 후보로만 유지한다.
- M/606 ESO adoption deadline은 표준화 기구의 작업/채택 일정이며 제조자 CRA compliance deadline이 아니다.
- M/606 Annex/Commission standardisation request만으로 harmonised standard의 OJ reference가 공표되거나 CRA Article 27 presumption of conformity가 발생하지 않는다.

## 남은 데이터/증거 한계
1. 36개 SEC controls는 설계·검증 후보와 evidence checklist이며 실제 구현/시험 완료 증거가 아니다. 현재 상태 '미작성/증거 미확인' 유지.
2. 15개 interfaces는 전형적 인터페이스 예시이며 제품별 실재/활성/제품 경계 증거가 없다. '제품별 미확인' 유지.
3. 41개 M/606 항목은 표준화 주제와 conditional relevance mapping이며 제품 분류/적합성 판단이 아니다.
4. 13개 Guidance claims는 Commission 해석 요약이지 binding law가 아니다.
5. 제품 제조사·모델·회로도·펌웨어/소프트웨어 구성·사용설명서·시장 공급/상표·remote-service 계약이 확보되기 전 제품별 CRA scope/classification/conformity를 확정하지 않는다.

## 다음 단계
- 전체 보고서 본문과 35-row CSV의 용어/조항/날짜/예외/조건이 15/36/13/41 매트릭스와 일치하는지 독립 재검토.
- 제품 evidence intake 문서에 manufacturer/model/variants, intended purpose, connection/protocol, RDPS, software components/SBOM, market placement/supply chain, support period, Annex III/IV core function, sectoral certificates를 증거 단위로 요청.
- Commission-hosted Guidance PDF primary byte identity를 재확인하고 fallback 상태 유지.
