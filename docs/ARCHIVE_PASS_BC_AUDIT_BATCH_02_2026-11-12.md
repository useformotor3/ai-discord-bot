# 34개 표본 Pass B/C 재검증 — Batch 02 (A-009–A-015, B-001–B-002)

- 기준일: 2026-11-12
- 대상: 8개 고유 원본. A-013/B-006 중복은 제외하고 A-014/A-015 포함.
- 법령 1차 출처: Regulation (EU) 2024/2847, EUR-Lex 현행 공식 원문
- URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 원문 재확인 구간: Article 13(8)–(9), Article 14(1)–(8), Annex I Part I(2), Part II(1)–(8)
- 재검증 방식: 원본의 Raw Text Quote를 다시 추출해 원문을 새로 열어 문구/위치/조건을 재대조하고, 관련 예외와 인접 항목을 확인했다.
- 한계: 동일 AI 세션의 별도 재검증 절차이며 제3자 독립 법률 검토가 아니다.

## 1. 원본별 Pass B/C 결과

| ID / 원본 | Pass B: 원문 재대조 | Pass C: 반증·예외 확인 | 판정 |
|---|---|---|---|
| A-009 — 2026-11-09_094606.md | 인용문 “at least 5 years or corresponds to expected lifetime … whichever is shorter”는 Article 13(8)의 문구가 아니다. 현행 조항은 지원기간을 제품 예상 사용기간/사용자 기대/제품 특성 등을 반영해 결정하고, 원칙적으로 최소 5년, 예상 사용기간이 5년 미만이면 그 예상 사용기간으로 한다. | “whichever is shorter”를 전체 기간 규칙으로 적용하면 원칙 최소 5년을 뒤집는다. Annex II point 7은 지원 종료일 등 사용자 정보 고지, Annex VII point 4는 지원기간 결정에 고려한 정보의 기술문서 포함을 규정한다. | **REJECTED (직접 인용)**. 본문 요약도 “최소 5년, 예상 사용기간이 5년보다 짧으면 그 기간”으로 정정. |
| A-010 — 2026-11-09_180532.md | Raw quote는 Article 14의 현행 원문과 일치하지 않는다. 현재 Article 14(1)은 모든 보안 영향 취약점이 아니라 actively exploited vulnerability를 신고 대상으로 규정한다. Article 14(2)는 24h early warning, 72h vulnerability notification, corrective/mitigating measure가 available된 후 14일 이내 final report다. | Severe incident는 Article 14(3)–(4)로 별도 처리: 24h early warning, 72h incident notification, (b) 통지 후 1개월 이내 final report. 모든 zero-day 또는 모든 취약점이 자동으로 Article 14 신고 대상이라는 주장은 과장. | **REJECTED (직접 인용/대상 범위)**. 두 유형과 각각의 타이머를 구분해 정정. |
| A-011 — 2026-11-10_110057.md | Annex II Part II는 해당 취약점 처리 요구의 위치가 아니다. SBOM은 Annex I Part II(1). 원본의 첫 quote는 취약점·오픈소스 요소 등을 모두 SBOM 필드처럼 묶어 현행 법령 문구와 일치하지 않는다. 두 번째 “expected lifetime or five years, whichever is longer”는 Article 13(8)의 규칙과 반대다. | Annex I Part II(1)은 최소 top-level dependencies. Annex VII 2(b)는 SBOM을 포함한 취약점 처리 프로세스 정보를 기술문서에 포함. Article 13(8)은 최소 5년, 5년보다 짧은 예상 사용기간이면 그 기간. | **REJECTED (직접 인용/기간 규칙)**. SBOM 범위와 지원기간을 별도 주장으로 분리. |
| A-012 — 2026-11-11_120102.md | Article 14(3)은 severe incident reporting이며 지원기간/무상 업데이트 문구가 아니다. Raw quote는 최종 법령과 일치하지 않는다. Annex I Part I(2)(g)는 데이터 최소화이며 업데이트 조항이 아니다. | 지원기간은 Article 13(8), 업데이트는 Part I(2)(c), Part II(2)/(8). Part I(2)(h)는 필수·기본 기능의 가용성 보호. | **REJECTED (직접 인용/조항 연결)**. 원본의 Article 14(3) 및 (g) 참조를 제거하고 각 의무를 정확한 위치로 이동. |
| A-014 — 2026-11-10_024038.md | Annex I Part I의 “Section 2 (1)”은 구조가 틀렸다. Part I point (2)(a)–(m)와 Part II points (1)–(8)는 서로 다른 체계다. Raw quote는 현행 Annex I 문구가 아니다. Article 13(8) quote 또한 “expected lifetime or five years, whichever is shorter” 형태로 법문과 다르다. | Part I(2)(c)는 보안 업데이트 및 해당되는 경우 자동 업데이트 설정·통지·opt-out·postpone을 규정. 무상 제공은 Part II(8), 지원기간은 Article 13(8). 서명·anti-rollback은 설계 수단이지 조항의 문자 그대로의 구현 명령이 아니다. | **REJECTED (직접 인용/구조/기간)**. 요구사항과 설계 권고를 분리해 다시 작성. |
| A-015 — 2026-11-10_192042.md | “manufacturers... shall ensure that ... security updates are made available free of charge...” 문구는 Annex I Part I의 직접 인용으로 확인되지 않는다. 두 번째 Recital quote도 인용한 Recital 39와 실제 문구를 일치시키지 못하며, “integrity of update data and mechanism”을 CRA가 특정한 직접 문구로 제시하면 안 된다. | 안전한 업데이트 배포는 Annex I Part II(7), 데이터/명령/프로그램 무결성은 Part I(2)(f), 무상 업데이트는 Part II(8). 법령은 특정 공개키 알고리즘/서명 포맷을 지정하지 않는다. | **REJECTED (직접 인용)**. 각각의 요구사항 위치를 분리하고 암호 서명은 위험 기반 설계 권고로만 제시. |
| B-001 — 2026-11-11_223547.md | Article 11(1)(e)는 현행 CRA의 지원기간/무료 패치 조항이 아니다. 현행 Article 11은 general product safety 관련 조항이며 제조자 지원기간은 Article 13(8). Annex I Part II(1)은 SBOM/구성요소·취약점 식별 문구로서 원본 인용과 다르다. | 지원기간은 최소 5년, 예상 사용기간이 더 짧으면 그 기간. 무상 제공은 Part II(8). Article 14는 적극 악용 취약점 및 중대한 사고 신고. | **REJECTED (직접 인용/조항 연결)**. 원본의 “수명 또는 5년 중 짧은 기간”은 규칙을 반대로 전달. |
| B-002 — 2026-11-11_224041.md | Article 10(6)은 현행 제조자 의무/지원기간 조항이 아니다. 현행 Article 10은 enhancing skills. Article 13(8)이 지원기간, Part II(8)이 무상 보안 업데이트. Annex I Part I Section 2(5),(6)이라는 위치도 잘못된 구조다. | Part II(5)는 CVD 정책, Part II(6)은 취약점 신고 연락처. Part I(2)(c)는 취약점 대응 업데이트 및 해당되는 자동 설치 조건. | **REJECTED (직접 인용/조항 연결)**. 법령의 조항·Annex 체계를 현행 최종본으로 교체. |

## 2. Batch 02 요약

- 대상 8개 파일 모두 Raw Text Quote를 법령 직접 인용으로 재사용할 수 없음.
- 지원기간 “whichever is shorter/longer”를 혼용하거나 반대로 표현한 사례가 반복됨.
- Article 14의 신고 대상을 모든 취약점으로 확장한 인용은 현행 Article 14(1)의 actively exploited vulnerability 요건과 일치하지 않음.
- Annex I Part I의 제품 속성 요건과 Part II의 제조자 취약점 처리 프로세스를 혼합한 사례가 반복됨.
- 파일 단위 오류 개수는 기존 34개 표본 CONFLICT/PARTIALLY_VERIFIED 통계와 합산하지 않는다. 이번 표는 직접 인용 블록 재검증 결과다.

## 3. 설계 문서 반영 규칙

1. Article 13(8) 지원기간: 원칙 최소 5년, 예상 사용기간이 5년 미만이면 그 예상 사용기간.
2. Article 13(9) 업데이트 가용성: 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간.
3. Annex I Part I(2)(c): 취약점 해결 보안 업데이트, 해당되는 자동 설치 기본값/opt-out/알림/일시 연기 조건.
4. Annex I Part II(2): 취약점 지체 없는 처리, 기술적으로 가능한 경우 기능 업데이트와 분리.
5. Annex I Part II(7): 안전한 업데이트 배포 메커니즘.
6. Annex I Part II(8): 지체 없는 무상 보안 업데이트, 맞춤형 제품에 대한 제조자-사업 사용자 별도 합의 예외.
7. Article 14(1)–(2): 적극 악용 취약점 신고. Article 14(3)–(4): 중대한 사고 신고.
8. 특정 서명 알고리즘, Secure Boot, anti-rollback, dual-bank는 법령 직접 인용이 아니라 위협모델에 근거한 설계 권고/선택으로 분류.

## 4. 근거

- EUR-Lex Regulation (EU) 2024/2847, Article 13(8)–(9), Article 14(1)–(8), Annex I Part I(2)(c),(f),(g),(h), Part II(1),(2),(5)–(8).
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 본 검토는 법령 원문 대조 기록이며 법률 자문/제3자 독립 검토/제품별 적합성 판정이 아니다.
