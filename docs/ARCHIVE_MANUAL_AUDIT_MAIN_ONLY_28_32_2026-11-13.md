# Main-only CRA Archive Manual Audit — Reports #28–#32

- 감사일: 2026-11-13
- 원본 브랜치: `main` (읽기 전용)
- 기록 브랜치: `cra-project-foundation`
- 대상: main report #28–#32, `history.json`의 count/date와 archive path를 대조
- 프로토콜: Pass A 주장/인용 추출 → Pass B 기존 EUR-Lex 현행 법령 기준선 대조 → Pass C 조항 구조·예외·신고 범위·제품 적용성 반증
- 검증 한계: 본 배치는 앞선 #8–#27 감사에서 직접 확인한 EUR-Lex Regulation (EU) 2024/2847 기준선을 재사용했다. 이번 배치에서 Phase E3 fetcher 또는 새 live source fetch를 실행하지 않았다. 동일 AI 검토이며 독립 제3자 법률 검토가 아니다.
- 제품 적용성: 모든 보고서에서 UNVERIFIED. 제품 SKU, intended purpose, 제품 경계, 인터페이스/업데이트 구성, 실제 ST MCU 주문 코드 미확정.

## 1. 원본 추적성

| Report | Archive path (main) | Blob SHA-1 | Topic from body |
|---:|---|---|---|
| 28 | `research_archive/2026-11-13_021538.md` | `78de23c029c47dee16ebc82adf7123c2bf52fa4a` | Free security updates / CVD |
| 29 | `research_archive/2026-11-13_022039.md` | `e5248b9d23e94ea0ef5ad7ffb30f2dcd100e3434` | Free updates / vulnerability disclosure |
| 30 | `research_archive/2026-11-13_022538.md` | `15439fdad39d1759f522023fc3f1201c1fbf4e8f` | Manufacturer reporting / incident handling |
| 31 | `research_archive/2026-11-13_023045.md` | `bc85eca9a24980a199e00fc13752f158b11e059e` | VDP / reporting obligations |
| 32 | `research_archive/2026-11-13_023540.md` | `71146baf92e406e18209f9981d8a7afc47620be2` | Free updates / vulnerability handling |

## 2. 보고서별 판정

### #28 — CONFLICT

- 핵심 주장: 제품 예상 수명(“최소 5년 이상”) 동안 무상 업데이트, CVD 정책, ENISA 협력.
- 오류:
  - 지원기간을 “최소 5년 또는 예상 수명”처럼 단순화하고 5년 미만 예상 사용 예외를 충분히 반영하지 않았다.
  - 인용문에 “whichever is shorter”라는 표현을 넣었으나 현행 Article 13(8)의 지원기간 구조와 맞지 않는다. Article 13(8)은 예상 사용기간이 5년 미만이면 그 예상 사용기간에 대응한다.
  - 무상 보안 업데이트 근거는 Annex I Part II(8), CVD 정책은 Part II(5), 신고 연락/정보 공유는 Part II(6) 등으로 분리해야 한다. 보고서는 이를 “Annex I Section 2” 수준으로 합쳐 표현한다.
  - “ENISA와의 협력 체계”는 구체 법정 의무와 운영 권고를 분리해 써야 한다.
- 직접 인용: REJECTED — 원문 위치·버전 미제시, 문언에 법령 구조와 충돌하는 구절 포함.

### #29 — CONFLICT

- 핵심 주장: Article 10 및 Annex I를 근거로 무상 업데이트·고지·최소 5년 지원을 주장.
- 오류:
  - 제조사 일반 의무를 현행 CRA Article 13이 아닌 Article 10으로 잘못 연결.
  - Article 13(8) 지원기간, Article 13(9) 보안 업데이트 보존/가용 기간, Annex I Part II(8) 무상 업데이트 제공을 서로 구분하지 않는다.
  - “유상 서비스 계약 여부와 무관하게”라는 절대 표현은 Annex I Part II(8)의 맞춤형 제품과 사업 사용자 간 별도 합의 예외를 누락한다.
  - Raw Text Quote는 현행 법령의 정확한 문언/위치를 제시하지 않고 합성된 문장이다.
- 직접 인용: REJECTED — 조항 번호 오류 및 현행 원문과 일치하는 locator 없음.

### #30 — CONFLICT

- 핵심 주장: Article 11에 따른 신고 의무, 24h/72h ENISA 신고, 런타임 상시 모니터링.
- 오류:
  - CRA 제조자 신고 의무는 현행 Article 14이며 Article 11이 아니다.
  - Article 14 신고 대상은 제품에 포함된 actively exploited vulnerability와 제품 보안에 영향을 주는 severe incident 두 트랙이다. 모든 제품 취약점/보안 사고로 확대하지 않는다.
  - 취약점 트랙의 최종 보고는 시정/완화 조치가 가능해진 뒤 14일 이내, 심각한 사고 트랙은 72시간 신고 후 1개월 이내로 구분해야 한다. 보고서는 최종 보고 시한을 누락한다.
  - “ENISA에 제출”은 Article 14/16의 지정 CSIRT 및 Single Reporting Platform 경로와 구분해 표현해야 한다.
  - 실시간 런타임 탐지·로깅을 모든 서보 드라이브에 직접 요구하는 조항으로 단정할 수 없다. 위험평가에 따른 구현 후보로 분리한다.
- 직접 인용: REJECTED — Article 11/NIS2 문구 혼입 및 현행 Article 14와 불일치.

### #31 — CONFLICT

- 핵심 주장: Annex I Part II(2) VDP, Article 14 신고, 서보 드라이브는 Class I/II에 해당.
- 오류:
  - 현행 Annex I Part II(5)가 CVD 정책의 직접 매핑이며 Part II(6)는 신고 연락처/취약점 정보 공유에 해당한다. Part II(2)는 취약점의 처리·시정 및 기술적으로 가능한 경우 보안 업데이트 분리 관련 요구다.
  - Article 14는 모든 중요제품 Class I/II에만 적용된다고 제한하지 않는다. 제품에 포함된 적극 악용 취약점과 제품 보안에 영향을 미치는 심각한 사고의 신고 트랙을 적용 문언대로 판단해야 한다.
  - “산업용 서보 드라이브 등 포함” 또는 Class I/II 해당을 자동 단정할 근거가 없다. Annex III 범주와 core functionality, 관련 시행규정의 실제 기능 기준을 대조해야 한다.
  - “제3자가 악용 중인 취약점”이라는 표현은 제품에 포함된 취약점의 actively exploited 요건을 정확히 반영하도록 고쳐야 한다.
- 직접 인용: REJECTED — Part II point 오인용 및 제품 분류 단정.

### #32 — CONFLICT

- 핵심 주장: Annex I Part I point 2 vulnerability handling, Article 11, 최소 5년 지원 및 무상 패치.
- 오류:
  - 취약점 처리 프로세스는 Annex I Part II(1)–(8)이며 Part I(2)는 제품의 사이버보안 속성 관련 요구다.
  - 제조자 취약점 처리·무상 보안 업데이트 근거는 Annex I Part II(2)/(8) 등으로 분리해야 한다. Article 11은 이 보고서가 주장하는 무상 패치 근거가 아니다.
  - 지원기간 Article 13(8), 제공된 보안 업데이트의 가용성 Article 13(9), 무상 보안 업데이트 Annex I Part II(8)은 서로 다른 의무다.
  - 인용문은 조항 번호와 법령 문언이 불명확하며 “Annex I Part I, Point 2(2)”라는 위치 표기는 현행 구조와 맞지 않는다.
- 직접 인용: REJECTED — 조항·위치 오류 및 합성 인용.

## 3. 배치 결과

| 항목 | 결과 |
|---|---:|
| 감사 보고서 | 5 |
| CONFLICT | 5 |
| PARTIALLY_VERIFIED | 0 |
| VERIFIED | 0 |
| 현행 법령 직접 인용으로 재사용 가능한 Raw Text Quote | 0 / 5 |
| 제품별 적용성 | 전부 UNVERIFIED |

이 배치는 시간순 연속 5건이며 무작위 표본이 아니다. 전체 1,366개 archive의 오류율로 일반화하지 않는다.

## 4. 이후 보고서에 적용할 정정 규칙

1. Article 13(8) 지원기간과 Article 13(9) 보안 업데이트 가용 기간을 분리한다.
2. Annex I Part II(2) 취약점 시정, Part II(5) CVD 정책, Part II(6) 신고 연락/정보 공유, Part II(7) 안전한 배포, Part II(8) 적시·무상 보안 업데이트를 각각 구분한다.
3. Article 14는 적극 악용 취약점과 제품 보안에 영향을 주는 심각한 사고의 두 신고 트랙 및 서로 다른 최종 보고 기한을 유지한다.
4. 신고 경로는 Article 14/16의 지정 CSIRT·Single Reporting Platform 체계로 정확히 설명한다.
5. Secure monitoring, logging, real-time detection, signed update 등은 법령의 명시 문구와 위험기반 설계 권고를 구분한다.
6. 서보 드라이브의 Annex III Important Product Class I/II 분류를 제품명만으로 단정하지 않는다.
7. 원문 위치·버전·locator가 없는 Raw Text Quote는 직접 인용으로 재사용하지 않는다.

## 5. 사용한 기준 자료와 한계

- Regulation (EU) 2024/2847, EUR-Lex CELEX 32024R2847: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
- 기준선은 작업 브랜치의 `docs/CRA_LEGAL_BASELINE.md`, #8–#12 및 #13–#27 감사 문서에서 확인된 법령 매핑을 재사용했다.
- 이번 배치에서는 live fetch, PDF 시각 검토, 새로운 독립 공식 교차 출처 확인을 하지 않았다. 해당 작업은 후속 단계로 남긴다.
- 본 감사는 법률 자문, 독립 제3자 감사, 제품별 CRA 적합성 평가가 아니다.

## 원자 Claim ID 연결 — #28–#32

- #28–#32에 대해 [Claim Evidence Ledger](CLAIM_EVIDENCE_LEDGER.md)에 원자 Claim ID 33개를 등록했다.
- 파일 단위 결과는 5 CONFLICT / direct quote reuse 0/5로 유지한다.
- Article 13(8) support period, Article 13(9) update availability, Annex I Part II(5)/(6)/(8) CVD/contact/free updates, Article 14 two-track reporting, Annex VII(4) technical documentation을 각각 분리했다.
- “whichever is shorter” 지원기간 문구, Article 10/11 제조사 의무 오기, Part I/Part II 혼합, 모든 취약점의 ENISA 신고 주장은 재사용하지 않는다.
