# Main-only 자동 생성 보고서 #36 법령 인용 감사

**검토일:** 2026-11-12  
**대상 브랜치:** main (작업 브랜치 cra-project-foundation에는 미포함)  
**원본 파일:** research_archive/2026-11-12_025529.md  
**원본 blob SHA:** 0d5b3f17b13f8935a90c23400173e401a76e1953  
**원본 commit:** [5cd4a18dbf5dc4712d669b29b8846af799f5efc1](https://github.com/useformotor3/ai-discord-bot/commit/5cd4a18dbf5dc4712d669b29b8846af799f5efc1)  
**공식 법령:** [Regulation (EU) 2024/2847 — EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847)  
**파일 판정:** CONFLICT — 법령 조항 오기, 합성 직접 인용, Article 14/무료 업데이트 혼동  
**원본 보존:** main 원본 파일, history.json, state.json은 수정하지 않음

## 1. 요약 판정

보고서 #36은 Secure Boot/Measured Boot, TPM 또는 MCU 내부 하드웨어 저장소, 디지털 서명 검증을 CRA가 일률적으로 요구하는 것처럼 서술한다. Annex I는 위험평가에 따른 보안 결과를 규정하지만, 모든 제품에 특정 하드웨어 Root of Trust, Measured Boot, Secure Boot 또는 특정 서명 체계를 의무 부품/구조로 지정하지 않는다. 이들은 제품 위험에 따라 선택할 수 있는 구현 통제 후보로 구분해야 한다.

또한 보고서는 무상 보안 업데이트를 Article 14와 연결한다. 이는 잘못된 조항이다. Article 14는 actively exploited vulnerability 및 severe incident의 신고 의무이며, 보안 업데이트의 무상 제공은 Annex I Part II(8)에 규정된다. 지원기간은 Article 13(8)과 연결된다.

보고서가 제시한 Annex I 직접 인용은 (b), (c), (g)의 실제 문구와 맞지 않으며, 원문에 없는 secure boot 표현을 직접 인용처럼 삽입했다. 문서 제목에 적힌 개정 법령 번호도 실제 CRA 제목과 불일치한다.

## 2. 주장별 원문 대조

| 원본 주장 | 공식 원문 대조 | 판정 |
|---|---|---|
| 하드웨어 RoT/TPM 또는 MCU 내부 secure storage를 반드시 활용해야 함 | Annex I는 접근통제·기밀성·무결성 등 결과를 요구하나 TPM/SE/내부 secure enclave를 일률적으로 특정하지 않음 | CONFLICT |
| Secure Boot 및 Measured Boot로 부트로더/OS/펌웨어의 디지털 서명을 순차 검증해야 함 | Annex I Part I에 Measured Boot 또는 전 단계 디지털 서명 검증의 보편 의무가 없음. Secure Boot도 직접 열거된 보편 요구가 아님 | CONFLICT |
| Article 14에 따라 취약점 보안 업데이트를 무상 제공해야 함 | Article 14는 적극 악용 취약점 및 중대 보안 사고 신고. 무상 보안 업데이트는 Annex I Part II(8), 지원기간은 Article 13(8) | CONFLICT |
| Secure Boot는 패치 출처/무결성 검증에 필수 | 위험 기반 설계에서 유용한 통제 후보일 수 있으나 CRA가 모든 제품에 이를 유일/필수 구현으로 지정하지 않음 | CONFLICT |
| 서보 드라이브는 실시간·물리적 위험 때문에 더 강한 통제가 필요할 수 있음 | 제품 위험평가에서 합리적으로 검토할 기술적 고려사항. 제품 사실·위험평가 없이 법적 결론으로 승격 불가 | PARTIALLY_VERIFIED |

## 3. 직접 인용 블록의 조항 오류

보고서는 Annex I Part I(2)(b), (c), (g)를 다음과 같이 인용한다: 데이터 무단 접근/변경 보호, secure boot로 비인가 코드 실행 방지, 보안 업데이트로 취약점 해결.

현행 EUR-Lex 원문은 다음과 다르다.

- Part I(2)(b): secure-by-default 구성 및 원래 상태로 재설정 가능성.
- Part I(2)(c): 취약점을 보안 업데이트로 해결할 수 있어야 함. 자동 업데이트가 적용되는 경우 기본 설정, 적절한 기간, opt-out 등 조건 포함.
- Part I(2)(e): 저장·전송·처리 데이터의 기밀성.
- Part I(2)(f): 데이터·명령·프로그램·설정의 무단 변경 방지 및 손상 보고.
- Part I(2)(g): 목적에 필요한 범위로 데이터 처리 최소화.
- Part I(2)(h): 필수·기본 기능의 가용성 보호 및 DoS 회복력.

Annex I Part I에는 보고서가 직접 인용한 “secure boot” 예시 문구가 없다. 원본 인용은 여러 항목을 합성하고 존재하지 않는 문장을 인용부호 안에 넣은 것으로 판정하며, 전체 인용 블록은 REJECTED다.

## 4. 올바른 CRA 조항 구분

- **Article 13(8):** 제조자의 지원기간 산정. 예상 사용기간, 사용자 기대, 제품 특성 등을 고려하며 최소 5년 원칙 및 예상 사용기간이 더 짧은 경우의 예외를 둔다.
- **Annex I Part II(8):** 확인된 보안 문제를 해결하는 보안 업데이트가 제공되는 경우 지체 없이 배포하고, 맞춤형 제품 관련 제조자와 사업 사용자 간 별도 합의 예외를 제외하면 무상 제공.
- **Article 14(1)–(4):** actively exploited vulnerability 및 severe incident의 신고와 유형별 24시간/72시간/최종 보고 시한.
- **Annex I Part II(7):** 취약점을 적시에 수정/완화하도록 보안 업데이트를 안전하게 배포하는 메커니즘.

따라서 Article 14를 무상 업데이트 조항으로 인용하면 안 된다.

## 5. 법령 제목 오류

원본 보고서는 CRA가 Regulation (EU) No 165/2014 및 Directive (2019/1939)를 개정한다고 적었다. EUR-Lex의 Regulation (EU) 2024/2847 정식 제목은 Regulations (EU) No 168/2013 및 (EU) 2019/1020, Directive (EU) 2020/1828의 개정을 명시한다. 원본의 법령 제목/개정 법령 목록도 잘못되었다.

## 6. 권장 정정 문안

> CRA는 제품 위험평가를 바탕으로 secure-by-default, 취약점 수정 업데이트 가능성, 비인가 접근 통제, 데이터 기밀성·무결성, 필수 기능 가용성 및 취약점 처리 프로세스 등의 결과를 요구한다. Secure Boot, Measured Boot, 펌웨어 서명 검증, TPM 또는 MCU 내부 보안 저장소는 해당 제품의 위험과 아키텍처에 따라 선택할 수 있는 구현 통제다. 무상 보안 업데이트는 Annex I Part II(8), 지원기간은 Article 13(8), 적극 악용 취약점 및 중대 보안 사고 신고는 Article 14로 구분해야 한다.

## 7. 출처 및 한계

- Regulation (EU) 2024/2847, EUR-Lex.
- 확인 위치: 정식 제목/개정 법령 정보, Article 13(8), Article 14(1)–(4), Annex I Part I(1)–(2)(a)–(m), Part II(2),(7),(8).
- EUR-Lex 원문을 직접 열어 문구/조항을 대조했다.
- 제품별 CRA 적용성, 제품 분류, 실제 Secure Boot 설계 적합성은 이 감사에서 판정하지 않는다.
- 본 감사는 main-only 자동 생성물에 대한 작업 브랜치의 감사 기록이다. main 원본과 main branch는 수정하지 않는다.
