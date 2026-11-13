# Main-only CRA Archive Manual Audit — Reports #33–#37

## 한국어 핵심 요약

- 대상: main 보고서 #33–#37, 총 5건.
- 판정: CONFLICT 5건 / PARTIALLY_VERIFIED 0건 / VERIFIED 0건.
- 직접 인용 재사용 승인: 0/5. 제품별 적용성은 모두 UNVERIFIED.
- 반복 오류: Article 13(8) 지원기간, Article 13(9) 업데이트 가용성, Annex I Part II(8) 무상 보안 업데이트를 서로 혼동; Article 14의 적극 악용 취약점/심각한 사고 신고 범위를 확대; Annex I Part I(2)(b)/(d)/(j) 보안 기본값·접근통제·공격표면 조항의 위치와 의미 오기; 서보 드라이브 Class I/II 자동 분류.
- 첫 접속 비밀번호 변경, 고유 자격증명, 모든 포트 비활성화, JTAG 일괄 잠금을 보편적 CRA 직접 의무로 단정하지 않는다. 위험평가 기반 설계 후보로 구분한다.
- 아래 영문 상세 기록은 원본 commit·archive SHA·보고서별 판정을 보존한다. 한국어 법령 정본은 [CRA 공식 법령 기준선](CRA_VERIFIED_BASELINE_2026-11-12.md), 독자용 설명은 [제1권](CRA_SERVO_DRIVE_COMPLIANCE_REPORT_V1.md)을 참조한다.


- 감사일: 2026-11-13
- 원본 브랜치: `main` (읽기 전용)
- 기록 브랜치: `cra-project-foundation`
- 대상: main report #33–#37, archive path/date/count 대조 및 원문 주장·인용 검토
- 프로토콜: Pass A 주장/인용 추출 → Pass B 기존 EUR-Lex 기준선 대조 → Pass C 조항 구조·예외·제품 적용성 반증
- 검증 한계: 앞선 #8–#32 감사에서 직접 확인한 EUR-Lex Regulation (EU) 2024/2847 법령 기준선을 재사용했다. 이번 배치에서 E3 live fetch, PDF 시각 대조, 별도 신규 공식 교차출처 확인은 하지 않았다. 동일 AI 검토이며 독립 제3자 법률 검토가 아니다.
- 제품 적용성: 전부 UNVERIFIED. 실제 제품 SKU, intended purpose, 제품 경계, 인터페이스/업데이트 방식 및 MCU 주문 코드 미확정.

## 1. 원본 추적성

| Report | Archive path | Blob SHA-1 | 주요 주제 |
|---:|---|---|---|
| 33 | `research_archive/2026-11-13_024039.md` | `c9c8f17bae8dd90890f9075927aa5fb6668c32b0` | CVD/VDP |
| 34 | `research_archive/2026-11-13_024544.md` | `97101ee32c543adc2b684c92eec4c831cbe2c479` | CVD/공급망/Article 14 |
| 35 | `research_archive/2026-11-13_025045.md` | `842b48aa5ba2382ce58cdddcb1f8b836c5336eb6` | Secure-by-default/초기 설정 |
| 36 | `research_archive/2026-11-13_025531.md` | `06f32803648a15f7638add752a8b9a064d4ee3f9` | 무상 업데이트/지원기간 |
| 37 | `research_archive/2026-11-13_030054.md` | `a8f77a2ecc3bc2301ab87a5f90d2ae6626489eab` | Important Product/적합성 평가 |

## 2. 보고서별 판정

### #33 — CONFLICT

- CVD 정책의 주제 자체는 CRA와 관련된다. 다만 법령 문언을 넘어 “PGP 등 암호화 채널을 반드시 공개”한다고 단정했다. 안전한 제보 처리와 연락 채널 요구를 특정 암호 방식의 법정 의무로 바꿔서는 안 된다.
- 보안 권고문 공개 의무의 정확한 조항·조건·시점이 특정되지 않았다. 취약점 처리 요구의 서로 다른 항목을 한 문단으로 합성했다.
- Annex I Part II(5)는 CVD 정책, Part II(6)은 취약점 정보 공유 및 연락처, Part II(4)는 보안 업데이트 제공 후 수정 취약점 정보 공개의 맥락으로 분리해야 한다.
- European Vulnerability Database/CSIRT 협력, 제로데이 대응, 물리적 오작동 시나리오는 규정 문언과 제품 위험 기반 권고를 구분해야 한다.
- Raw Text Quote: REJECTED — 정확한 locator/revision 부재 및 문언 검증 불충분.

### #34 — CONFLICT

- Annex I Part II 취약점 처리의 세부 구조를 “Section 2”로 뭉뚱그려 정확한 항목 번호를 잃었다.
- CVD 정책, 신고 연락처/정보 공유, 보안 업데이트 배포·무상 제공, Article 14 신고를 단일 프로세스로 혼합했다.
- Article 14를 Article 11로 잘못 연결했다. 현재 CRA 제조자 신고 의무의 근거는 Article 14이며, 모든 취약점의 신고가 아니라 actively exploited vulnerability 및 제품 보안에 영향을 주는 severe incident의 두 트랙이다.
- Raw Text Quote는 현행 법령의 정확한 구조·문언·위치가 확인되지 않는 합성 인용이다.
- Raw Text Quote: REJECTED.

### #35 — CONFLICT

- Secure-by-default는 Annex I Part I(2)(b)에 연결되는 주제지만, CRA가 모든 제품에 최초 부팅 시 고유 비밀번호 설정을 강제한다고 단정할 수 없다.
- 하드코딩된 자격증명, 불필요한 서비스·포트, 디버그 인터페이스의 위험을 줄이는 것은 위험기반 설계 후보다. 이를 일률적인 특정 구현 법정 의무로 표현하지 않는다.
- 인용문에 unique default password 또는 mandatory password change, 포트 제한 문구를 넣었으나 현행 CRA 원문 위치·문언과 맞지 않는다. Part I(2)(b) secure-by-default/reset 요구와 (d) 접근통제, (j) 공격표면 제한을 각각 정확히 매핑해야 한다.
- Raw Text Quote: REJECTED — draft/비현행 문언 및 합성된 조항 구조.

### #36 — CONFLICT

- 지원기간을 “예상 수명 또는 최소 5년”으로 서술하면서 Article 13(8)의 5년 미만 예상 사용기간 예외와 정확한 구조를 잘못 표현했다.
- Annex I Part I(2)(c)는 제품 속성·업데이트 관련 요구이며, 취약점 처리의 무상 업데이트는 Annex I Part II(8)에 매핑해야 한다.
- Article 13(6)을 무료 패치 의무로 인용했으나 이 조항을 무상 보안 업데이트의 직접 근거로 사용할 수 없다. Article 13(8) 지원기간, Article 13(9) 업데이트 가용성, Annex I Part II(8) 무상 보안 업데이트를 분리해야 한다.
- “상업적 계약이나 제한을 둘 수 없다”는 절대 표현은 맞춤형 제품과 사업 사용자 간 별도 합의 예외 등 법령 조건을 누락한다.
- Raw Text Quote: REJECTED — 조항·문언·locator 불일치.

### #37 — CONFLICT

- Important Product Class I/II 분류가 서보 드라이브에 자동 적용되는 것처럼 서술했다. 제품명·산업용 용도만으로 분류할 수 없고 CRA Article 7, Annex III의 범주 및 core functionality, 관련 시행규정의 실제 기능 기준을 대조해야 한다.
- 적합성 평가의 법적 절차를 Article 24로 표기했으나 현행 CRA 적합성 평가 절차의 핵심 근거는 Article 32다. 본문에 기재한 Annex VI/VII/VIII 모듈 조합도 현행 법령의 정확한 경로인지 확인되지 않았으므로 그대로 재사용하지 않는다.
- Class I/II 각각의 평가 경로는 제품의 정확한 분류, 관련 조화표준/공통규격 적용 여부, 현행 Article 32 및 해당 Annex 절차를 기준으로 다시 작성해야 한다. 이번 감사는 잘못된 모듈 번호를 대신 확정하지 않는다.
- DoC/CE/기술문서의 조항·Annex 연결도 Article 20, Article 31 및 관련 Annex 기준으로 별도 검증해야 한다.
- Raw Text Quote: REJECTED — 조항 번호 오류 및 제품 분류 미입증.

## 3. 배치 결과

| 항목 | 결과 |
|---|---:|
| 감사 보고서 | 5 |
| CONFLICT | 5 |
| PARTIALLY_VERIFIED | 0 |
| VERIFIED | 0 |
| 직접 인용 재사용 가능 | 0 / 5 |
| 제품별 적용성 | 전부 UNVERIFIED |

본 배치는 연속·비무작위 5건이다. 1,366개 전체 archive의 오류율로 일반화하지 않는다.

## 4. 통합 정정 규칙

1. CVD 정책 = Annex I Part II(5); 신고 연락처/정보 공유 = Part II(6); 보안 권고·취약점 정보 공개는 관련 세부 항목의 조건·시점을 확인해 분리한다.
2. Article 14 신고와 CVD/일반 취약점 접수를 동일시하지 않는다. Article 14는 적극 악용 취약점 및 제품 보안에 영향을 주는 심각한 사고의 법정 신고 트랙이다.
3. Secure-by-default Part I(2)(b), access control (d), attack surface (j)를 분리한다. 고유 비밀번호 강제·모든 포트 비활성화·JTAG 일괄 잠금은 보편적 CRA 명문 의무로 단정하지 않는다.
4. Article 13(8) support period, Article 13(9) update availability, Annex I Part II(8) free security updates는 별도 의무다.
5. Important Product Class I/II와 conformity assessment는 Article 7/Annex III 및 Article 32/해당 Annex를 실제 제품 기능에 대조한다.
6. 모든 Raw Text Quote는 exact current text, exact locator, document identity/revision이 확인되기 전 직접 인용으로 사용하지 않는다.

## 5. 기준 자료와 제한

- Regulation (EU) 2024/2847, EUR-Lex CELEX 32024R2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
- 기준선은 `docs/CRA_LEGAL_BASELINE.md`와 이전 #8–#32 감사 문서를 재사용했다.
- 이번 배치에서 E3 live fetch, PDF 시각 검토, 새 공식 교차 출처 검증을 하지 않았다. 적합성 평가 경로의 세부 Annex 매핑은 후속 공식 원문 재확인이 필요하다.
- 본 감사는 법률 자문, 독립 제3자 감사, 제품별 적합성 평가가 아니다.

## 2026-11-13 후속 공식 법령 확인 및 원자 Claim ID 연결 — #33–#37

- #33–#37에 대해 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID 33개를 등록했다.
- 파일 단위 결과는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- **추가 공식 확인:** Commission Implementing Regulation (EU) 2025/2392, adopted 28.11.2025, in force 21.12.2025. EUR-Lex: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng
- Article 7(1) 및 Implementing Regulation 2025/2392에 따라 중요한 제품 분류는 Annex III category의 **core functionality** 및 기술 설명으로 판단한다. 제품에 별도 네트워크 인터페이스 기능이 통합되어 있다는 사실만으로 host product가 자동으로 해당 category가 되지 않는다. 다만 standalone physical/virtual network interface product는 Class I category에 해당할 수 있다.
- Article 32(1)–(3), Annex VIII를 기준으로 conformity assessment를 정정: Class I은 조건에 따라 internal control Module A 또는 Module B+C/Module H, Class II는 Module B+C 또는 Module H. Module C는 internal production control, Module H는 full quality assurance.
- DoC Article 28, CE marking Article 30, technical documentation Article 31/Annex VII로 바로잡는다. 보고서의 Article 24/20/23 인용과 Module/Annex 매핑은 재사용 불가.
- 서보 드라이브 자체의 Class I/II 분류는 제품 전체 core functionality, 판매 형태, 내장 네트워크 인터페이스의 독립 제품 여부 등 증거가 없어 UNVERIFIED로 유지한다.
