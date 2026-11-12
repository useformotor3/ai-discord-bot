# CRA 아카이브 34개 표본 — Pass B/C 최종 재검증 요약

- 기준일: 2026-11-12
- 기준 브랜치: cra-project-foundation
- 대상: 기존 위험 기반 표본 35개 감사 ID 중 고유 원본 34개
- 중복: A-013/B-006은 동일 원본 research_archive/2026-11-11_230055.md이므로 한 번만 집계
- 1차 법령 출처: Regulation (EU) 2024/2847, EUR-Lex 현행 공식 원문
- 공식 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 목적: 기존 AI 조사 아카이브의 CRA 직접 인용·조항 연결 오류를 정정하고, 검증된 요구사항만 설계·시험 문서에 재사용하도록 한다.

## 1. 최종 집계

| Pass B/C 결과 | 고유 원본 수 | 의미 |
|---|---:|---|
| VERIFIED (모든 CRA 직접 인용과 조항 연결이 정확) | 0 | 파일 내 모든 직접 인용 블록이 문구·위치·조건까지 정확한 원본은 없음 |
| PARTIALLY_VERIFIED | 6 | 일부 인용/취지는 맞지만 같은 파일 내 다른 인용 또는 위치/조건에 정정 필요 |
| REJECTED | 28 | 직접 인용·조항 위치·법적 의무 표현을 현행 CRA 근거로 재사용할 수 없음 |
| 합계 | 34 | 고유 원본 수 |

**이 숫자는 34개 위험 기반 표본의 파일 단위 결과다.** 전체 990개 아카이브의 오류율이 아니며, 각 파일 안의 모든 문장/주장에 대한 제품별 적합성 판정도 아니다. 기존 수동 감사의 CONFLICT/PARTIALLY_VERIFIED 통계와는 평가 단위가 달라 합산하지 않는다.

### 1.1 배치별 집계

| 배치 | 표본 | VERIFIED | PARTIALLY_VERIFIED | REJECTED |
|---|---|---:|---:|---:|
| 01 | A-001–A-008 | 0 | 3 | 5 |
| 02 | A-009–A-015(중복 A-013 제외), B-001–B-002 | 0 | 0 | 8 |
| 03 | B-003–B-010 | 0 | 1 | 7 |
| 04 | B-011–B-020 | 0 | 2 | 8 |
| **합계** | **34개 고유 원본** | **0** | **6** | **28** |

## 2. 배치 보고서

1. [Batch 01 — A-001–A-008](ARCHIVE_PASS_BC_AUDIT_BATCH_01_2026-11-12.md)
2. [Batch 02 — A-009–A-015(중복 제외), B-001–B-002](ARCHIVE_PASS_BC_AUDIT_BATCH_02_2026-11-12.md)
3. [Batch 03 — B-003–B-010](ARCHIVE_PASS_BC_AUDIT_BATCH_03_2026-11-12.md)
4. [Batch 04 — B-011–B-020](ARCHIVE_PASS_BC_AUDIT_BATCH_04_2026-11-12.md)

기존 원본별 1차 인용 위치 목록은 [ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md](ARCHIVE_QUOTE_LEVEL_AUDIT_2026-11-12.md), 주장 요약/정정 연결은 [ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md](ARCHIVE_CLAIM_CORRECTION_LEDGER_2026-11-12.md)를 참조한다.

## 3. 반복된 중대 오류 패턴

1. **지원기간/무료 업데이트 혼동:** Article 13(8)은 지원기간 결정이다. 원칙 최소 5년이며 예상 사용기간이 5년보다 짧으면 그 기간이다. 무료 업데이트는 Annex I Part II(8).
2. **업데이트 분리/자동 업데이트 혼동:** 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리하는 것은 Part II(2). 자동 업데이트 조건은 Part I(2)(c). 둘은 같은 요구사항이 아니다.
3. **신고 범위 과장:** Article 14(1)–(2)는 actively exploited vulnerability, 14(3)–(4)는 severe incident다. 모든 취약점/사고를 같은 24h/72h 경로로 신고한다고 쓰면 안 된다.
4. **조항 번호 혼동:** Article 10은 enhancing skills, Article 11은 general product safety, Article 14는 manufacturer reporting obligations, Article 24는 open-source software stewards, Article 31은 technical documentation, Article 32는 conformity assessment.
5. **Annex 혼동:** Annex I Part I는 제품의 사이버보안 속성, Part II는 제조자의 vulnerability handling process. Annex II는 사용자 정보·지침, Annex VII는 기술문서 내용.
6. **제품 분류 허위 단정:** Annex III에 industrial automation/servo drive라는 독립 Class I/II 항목을 만들어서는 안 된다. Article 7의 core functionality 및 Implementing Regulation (EU) 2025/2392 기술 설명을 적용해야 한다.
7. **법령과 구현 예시 혼동:** Secure Boot, digital signature, PKI, TLS, eFuse/JTAG lock, dual-bank, anti-rollback, hot patch 등은 위험평가에 따른 설계 선택/권고일 수 있으나 CRA가 특정 구현을 직접 지정했다고 표현하지 않는다.

## 4. 재사용 가능한 현행 CRA 기준선

| 요구사항 | 정확한 위치 | 실무 번역 |
|---|---|---|
| 위험평가 | Article 13(2)–(4) | intended purpose, reasonably foreseeable use, operating environment, protected assets를 고려해 위험평가하고 기술문서에 포함 |
| 지원기간 | Article 13(8) | 제품 예상 사용기간/합리적 기대/제품 특성을 고려. 최소 5년, 단 예상 사용기간이 5년 미만이면 그 기간 |
| 업데이트 보존 | Article 13(9) | 지원기간 중 배포한 각 보안 업데이트를 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능하게 유지 |
| SBOM | Annex I Part II(1) | 일반적으로 사용되는 기계 판독 형식, 최소 top-level dependencies |
| 취약점 처리/분리 | Annex I Part II(2) | 취약점 지체 없이 수정. 기술적으로 가능한 경우 보안 업데이트를 기능 업데이트와 분리 |
| 정기 시험 | Annex I Part II(3) | 제품 보안에 대한 효과적이고 정기적인 테스트/검토 |
| CVD | Annex I Part II(5) | coordinated vulnerability disclosure policy 수립 및 시행 |
| 신고 연락처 | Annex I Part II(6), Annex II(2) | 취약점 신고 연락 창구 제공 및 사용자에게 정보 제공 |
| 안전한 업데이트 배포 | Annex I Part II(7) | 취약점을 적시에 수정/완화하도록 업데이트의 안전한 배포 메커니즘 제공 |
| 무상 보안 업데이트 | Annex I Part II(8) | 확인된 보안 문제 해결 업데이트를 지체 없이 배포하고, 맞춤형 제품에 대해 제조자-사업 사용자 간 별도 합의가 있는 경우 외에는 무상 |
| 제품 보안 속성 | Annex I Part I(2)(b),(c),(d),(f),(g),(h),(j) | secure-by-default, update, access control, integrity, data minimisation, availability, attack surface를 각각 별도 매핑 |
| 신고 | Article 14(1)–(4) | actively exploited vulnerability와 severe incident를 구분하고 각 기한 적용 |
| 기술문서 | Article 31, Annex VII | 시장 출시 전 작성, 적절한 경우 지원기간 동안 업데이트 |
| 적합성 평가 | Article 32, Annex VIII | 제품 분류/표준 적용 조건에 따라 경로 결정 |
| EU DoC | Article 28, Annex V | 적합성 입증에 따른 DoC |
| CE | Article 29–30 | 일반 원칙과 부착 규칙을 구분 |

## 5. 검증 방법과 한계

- Pass A: 기존 원본 파일의 직접 인용·인용형 문구와 출처 표시를 확인.
- Pass B: EUR-Lex 현행 법령을 다시 열어 원문 문구, 조항, 인접 문맥, 조건을 재대조.
- Pass C: 반대 근거, 예외, Article/Annex 번호, 적용 범위, draft/final version 차이를 확인.
- 이 절차는 동일 ChatGPT 세션이 별도 패스로 수행한 재확인이다. 독립 제3자 법률 검토, 외부 전문가 서명, 인증기관 검토는 아니다.
- 법령 텍스트의 권위 출처는 EUR-Lex 현행 법령이다. 다른 사이트가 같은 법령을 복제한 것을 독립적인 두 번째 근거로 과장하지 않는다.
- 이번 범위는 34개 기존 표본의 CRA 법령 인용 블록이다. 표준/제조사 문서의 인용은 별도 원문 검증이 필요하다.
- 이 결과는 법률 자문, 제품별 CRA 적용성/등급 결정, 인증 완료 판정을 대체하지 않는다.

## 6. 다음 작업 — 조사에서 엔지니어링으로 전환

1. 위 기준선을 요구사항 레지스터로 옮기고 각 요구사항에 HW/FW/시스템/제조/운영 조치, 시험 방법, 합격 기준, 증거 파일을 연결한다.
2. 서보 드라이브 제품 경계, EU 판매 형태, 연결성, 원격 처리, intended purpose를 확인해 scope/classification을 평가한다.
3. 정확한 ST MCU 주문 코드와 실리콘 리비전을 확인해 제조사 데이터시트/RM/Errata/보안 가이드로 구현 가능성을 검증한다.
4. Secure Boot, firmware update, key provisioning, debug lifecycle, vulnerability response, SBOM을 설계 블록과 시험 증거로 연결한다.
5. 기존 archive 원본은 변경하지 않는다. 검증된 정정본만 별도 문서로 유지한다.

