# CRA 보고서 #16 정정 및 원문 인용 감사

- 감사 대상 원본: research_archive/2026-11-17_112042372442_8faa5133.md
- 원본 blob SHA: e1eac72c39c6012f776e5ad231a11a1b9ebeed7d
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| “Products ... vulnerabilities can be addressed ... automatic security updates and notification ...” | 직접 인용 불일치 | Annex I Part I point (2)(c)의 실제 문언 중 default setting, appropriate timeframe, opt-out, notification 및 postpone 요소가 생략·재배열됐다. 따옴표를 제거하거나 정확한 연속 원문으로 교체해야 한다 |
| 무결성 문구가 “not authorised by the manufacturer”라고 인용 | 핵심 단어 오류 | 최종 OJ Part I point (2)(f)는 “not authorised by the user”라고 규정한다. manufacturer와 user는 법적 의미가 다르다 |
| “including cryptographic mechanisms”가 Part I point (2)(f)에 포함된다고 인용 | 원문에 없는 문구 | 해당 point (2)(f)는 integrity 보호 및 corruption 보고를 규정하지만 이 문구를 포함하지 않는다 |
| 디지털 서명/암호학적 서명 검증을 CRA가 강제 | 특정 구현을 법적 의무로 과장 | CRA는 무결성 보호 및 안전한 업데이트 배포를 요구하지만 모든 제품에 디지털 서명을 특정 구현으로 명시하지 않는다 |
| CVD와 업데이트 메커니즘을 한 의무로 혼합 | 조항 구분 필요 | CVD 정책은 Annex I Part II (5), 수정 취약점 공개는 (4), 제보 연락 주소는 (6), 안전한 업데이트 배포는 (7) |

## 2. 정확한 법적 근거

- Annex I Part I point (2)(c): 취약점이 보안 업데이트로 해결될 수 있어야 하며, 해당되는 경우 자동 업데이트의 기본 설정, 적절한 설치 시기, 명확한 opt-out, 업데이트 알림 및 일시 연기 선택을 규정한다.
- Annex I Part I point (2)(f): 저장·전송·처리 데이터, 명령, 프로그램 및 설정의 무단 조작/변경 방지와 corruption 보고.
- Annex I Part II (7): 취약점이 적시에 수정/완화되도록 제품 업데이트를 안전하게 배포하는 메커니즘.
- Annex I Part II (5): CVD 정책을 마련하고 시행.
- Annex I Part II (4): 보안 업데이트가 이용 가능해진 뒤 수정된 취약점 정보 공개 및 정당한 지연 예외.

## 3. 수정된 권고 문안

제조사는 제품별 위험평가에 따라 데이터·명령·프로그램·설정의 무단 변경을 방지하고 corruption을 보고해야 한다(Annex I Part I point (2)(f)). 또한 취약점을 적시에 해결할 수 있도록 안전한 업데이트 배포 메커니즘을 제공해야 한다(Annex I Part II (7)). 디지털 서명은 업데이트 진위성·무결성을 보장하기 위한 유력한 구현 후보지만, CRA 원문이 모든 제품에 특정 서명 알고리즘이나 서명 방식 자체를 직접 지정한다고 쓰지 않는다. CVD 정책·취약점 공개·안전한 업데이트 배포는 각각의 별도 조항에 연결한다.

## 4. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
