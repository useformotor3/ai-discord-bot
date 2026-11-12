# main-only 자동 생성 보고서 #125–#128 감사 — 2026-11-12

**대상 기준:** main 보고서 #125–#128의 실제 커밋 diff  
**판정:** 4개 모두 CONFLICT  
**범위 제한:** 법령 원문과 명백한 조항/구조 오류를 중심으로 한 위험기반 감사. 990개 전체 오류율로 일반화하지 않는다. main 원본 archive/history/state는 수정하지 않았다.

## 요약

| 보고서 | 원본 commit | 핵심 오류 | 판정 |
|---|---|---|---|
| #125 | 11747ed41058a97ddccdccfdb95ac52bf63f3e46 | 사용자 지침을 Annex I Part II Section 2로 잘못 배치, Annex II Point 1에 존재하지 않는 하위항목을 직접 인용처럼 생성, 최소 5년을 고정값처럼 표현 | CONFLICT |
| #126 | 61e2b375a88b32d6385ba028f730517b3cdc1b0f | 신고 조항을 Article 11로 오기(Article 14), CVD/contact의 Annex I Part II 번호·인용 오류 | CONFLICT |
| #127 | 1fd180317b269e8cb69c69012008f089c4f99829 | CVD를 Annex I Part I에 배치, Article 13(6)을 지원기간·취약점 처리의 근거처럼 오인, 5년 문구 방향 오류 | CONFLICT |
| #128 | 15ceea4b9477b8c0928352a5b4228c0508e88daa | Annex I Part I에 존재하지 않는 (5)/(6) 업데이트 조항 생성, Secure Boot/RoT/rollback/STO를 보편적 CRA 의무로 과장, Class II를 근거 없이 언급 | CONFLICT |

## 개별 확인

### #125 — 사용자 정보 및 지침
- Annex I Part II Section 2라는 구조는 잘못된 위치다. 사용자 정보·지침 제공은 Article 13(18) 및 Annex II에 연결한다.
- Annex II는 Point 1–9 구조다. Point 1은 제조자 식별·연락처이며, secure-by-default settings/default password, minimum update period 등을 Point 1의 하위항목처럼 인용한 문구는 해당 원문 인용으로 사용할 수 없다.
- 지원기간은 Article 13(8)의 expected lifetime 등 요소와 최소 5년 원칙 및 expected use가 5년보다 짧은 경우의 예외를 함께 표현해야 한다. “최소 5년 또는 제품 예상 수명”이라는 단순 문구는 예외 방향을 오해하게 만든다.
- 정정 맵: Article 13(17) contact point, 13(18) user information/instructions, 13(19) support-period end-date information; Annex II(1)–(9), 특히 (7), (8)(a)–(f), 조건부 (9).

### #126 — CVD 및 신고
- 제조자 신고 의무는 Article 14이며 Article 11이 아니다.
- Article 14의 신고 대상은 모든 취약점이 아니라 actively exploited vulnerability 및 product security에 영향을 주는 severe incident의 별도 트랙이다.
- CVD는 Annex I Part II(5), vulnerability reporting/contact 및 information sharing은 Part II(6)에 연결한다. 보고서의 Part II 번호 및 직접 인용은 원문 구조와 재대조가 필요하며 현재 상태로 재사용하지 않는다.
- ENISA 단독 신고라고 단순화하지 말고 single reporting platform, designated CSIRT, ENISA 접근 구조를 정확히 구분해야 한다.

### #127 — EoL 및 CVD
- CVD는 Annex I Part I가 아니라 Annex I Part II(5)다.
- Article 13(6)은 지원기간의 5년 원칙을 정하는 조항이 아니다. 지원기간은 Article 13(8)에서 판단한다.
- “expected lifetime 또는 5년 중 더 짧은 기간”으로 일반화한 문장은 Article 13(8)의 expected use 예외와 최소 5년 원칙을 잘못 전달한다.
- “최소 수개월 전 EoL 통지”, “최종 패치 번들”, “Security.txt 필수”는 인용된 조항만으로 보편적 법정 의무라고 단정할 수 없다. 근거가 별도로 확인되지 않으면 운영/설계 권고로 분류한다.

### #128 — 업데이트 배포 및 복구
- Annex I Part I(2)(c)는 해당되는 경우 자동 업데이트 기본 설정, opt-out, 사용자 통지 및 일시 연기 관련 요구를 다룬다. Part I에 보고서가 인용한 (5)/(6) 하위항목은 존재하지 않는다.
- 안전한 업데이트 배포는 Annex I Part II(7), 보안 업데이트의 지체 없는 제공 및 원칙적 무상 제공은 Part II(8)다.
- Secure Boot, Root of Trust, cryptographic signature, dual-bank rollback, STO/safe state는 제품 위험·기능안전·설계 선택으로 검토할 수 있으나, 이 보고서의 인용만으로 모든 제품에 대한 보편적 CRA 직접 의무라고 결론낼 수 없다.
- Class II 분류는 Annex III와 Implementing Regulation (EU) 2025/2392의 core-functionality 기준에 따른 제품별 증거 없이 단정하지 않는다.

## 파이프라인 설계에 반영할 반복 패턴

1. Annex/Part/point/letter의 존재 여부를 법령 구조 레지스트리로 검증한다.
2. 모델이 직접 인용문을 새로 작성하지 못하게 한다. 수집된 원문 구간이 입력된 경우에만 그 구간에서 인용을 선택한다.
3. Article 13(6)/(8)/(18)/(19), Article 14, Annex I Part I/II, Annex II를 서로 대체할 수 없는 별도 obligation ID로 관리한다.
4. expected lifetime/support period의 예외 방향을 테스트 fixture로 고정한다.
5. 법정 의무와 risk-based design option, product-specific fact, interpretation을 별도 claim type으로 구분한다.
6. 제품 분류·Class I/II·기능안전 수준은 제품 사실/공식 기준 입력이 없으면 UNVERIFIED로 유지한다.
7. 보고서 생성 성공과 법적 검증 완료를 분리한다. 모델 출력 자체가 VERIFIED 상태를 지정할 수 없어야 한다.

## 근거 및 한계

- 원본은 GitHub main branch commit diff에서 직접 확인했다.
- 법령 기준선: Regulation (EU) 2024/2847, EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 제품 분류 기준 추가 자료: Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392
- 이 문서는 법률 자문이나 독립 제3자 법률검토가 아니다. 파일 단위 감사이며 개별 주장 전수검증을 의미하지 않는다.
