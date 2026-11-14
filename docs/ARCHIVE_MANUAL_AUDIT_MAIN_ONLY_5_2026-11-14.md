# main-only CRA 아카이브 수동 감사 — 2026-11-14 report #5

- 감사 ID: CRA-AUDIT-MAIN-20261114-005
- 원본 main 파일: research_archive/2026-11-14_002038.md
- 원본 blob SHA: 447753b6ec40949251315d1274cdcf8ea3570218
- 원본 main commit: e3b94efcb955c4c39a6b63a3550987ca3e13068a
- 감사 기준 법령: Regulation (EU) 2024/2847, OJ L, 20.11.2024, EUR-Lex CELEX 32024R2847
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 비교 원본: 2026-11-14 reports #2 and #4, both secure-by-default/initial-auth topic
- 파일 단위 판정: **CONFLICT**
- Raw Text Quote 재사용: **0/2** (두 quote 모두 직접 인용으로 재사용 금지)
- 제품별 적용성: **UNVERIFIED**

## 1. 요약 판정

#5는 #2/#4와 동일한 secure-by-default, 초기 인증, 포트/진단 인터페이스 제한을 반복한다. 신규 Canonical Requirement를 만들지 않는다. Annex I Part I(2)(b), (d), (f), (j)의 관련 주제는 있으나, 강제 비밀번호 변경/고정 마스터 비밀번호 금지/모든 불필요 포트 일괄 비활성화를 CRA의 보편적 직접 명령으로 단정한 것은 과장이다.

법령 인용에는 두 가지 핵심 오류가 있다. 첫째, 제조자 의무를 Article 10으로 인용했으나 CRA의 제조자 의무는 Article 13이다. 둘째, Raw Text Quote의 "delivered with" 문구와 (2)(a) attack-surface 문구는 최종 Annex I Part I의 정확한 문언·위치가 아니다. (2)(a)는 알려진 악용 가능한 취약점 없이 시장에 제공하는 요구이고, secure-by-default는 (2)(b), attack-surface 제한은 (2)(j)에 있다.

## 2. 주장별 감사

| Claim ID | 원본 행 | 원자적 주장 | 공식 근거 | 판정 | 정정 |
|---|---:|---|---|---|---|
| CRA-ARCH-MAIN-20261114-005-001 | 요약/상세 | 제품은 factory default에서 secure-by-default 상태여야 한다. | Annex I Part I(2)(b) | PARTIALLY_VERIFIED | secure-by-default 및 original-state reset이 핵심이다. tailor-made product에 대한 제조자-사업 사용자 합의 예외를 포함한다. |
| CRA-ARCH-MAIN-20261114-005-002 | 요약/상세 | 불필요한 네트워크 포트·서비스·진단 인터페이스는 CRA에 따라 기본 차단해야 한다. | Annex I Part I(2)(j), (d) | PARTIALLY_VERIFIED | 외부 인터페이스를 포함한 attack surface 제한과 적절한 접근통제는 요구된다. 특정 포트/서비스의 blanket disablement는 제품별 위험기반 구현 선택이다. |
| CRA-ARCH-MAIN-20261114-005-003 | 상세 | 기본 계정이 있으면 최초 설치 시 강제 변경 또는 고정 마스터 비밀번호 차단이 의무다. | Annex I Part I(2)(b), (d) | CONFLICT | secure-by-default와 appropriate access control의 결과 요구를 특정 password lifecycle 방식의 보편 의무로 확장하지 않는다. |
| CRA-ARCH-MAIN-20261114-005-004 | 요약 | 제어 파라미터는 무단 접근/변경으로부터 보호되어야 한다. | Annex I Part I(2)(d), (f) | PARTIALLY_VERIFIED | 접근통제 및 사용자 승인 없는 조작/변경에 대한 무결성 보호와 부합한다. 실제 파라미터 접근 모델·안전 영향은 제품별 위험평가가 필요하다. |
| CRA-ARCH-MAIN-20261114-005-005 | 상세 | 제조자 의무는 Article 10이며 secure-by-default를 규정한다. | Article 13(1)–(4), Annex I Part I | CONFLICT | 제조자 의무는 Article 13이다. Article 13(1)은 Annex I Part I 준수를, Article 13(2)–(4)는 위험평가 및 기술문서화를 다룬다. |
| CRA-ARCH-MAIN-20261114-005-006 | Raw Text Quote | Annex I Part I(2)(a)가 secure-by-default/attack-surface 원문을 인용한다. | Annex I Part I(2)(a), (b), (j) | CONFLICT | (2)(a)=known exploitable vulnerabilities 없음, (2)(b)=secure-by-default, (2)(j)=attack surface 제한. 두 인용은 원문과 위치가 일치하지 않는다. |

## 3. 법령 원문 대조

- Article 13(1): 제조자는 제품이 Annex I Part I의 필수 사이버보안 요구사항에 맞게 설계·개발·생산되도록 해야 한다.
- Article 13(2)–(4): 제품의 사이버보안 위험평가, 그 결과를 수명주기 단계에 반영, 위험평가의 문서화 및 기술문서 포함을 규정한다.
- Annex I Part I(2)(a): 알려진 악용 가능한 취약점 없이 시장에 제공.
- Annex I Part I(2)(b): secure-by-default configuration, original-state reset 가능성, tailor-made product에 대한 제한적 합의 예외.
- Annex I Part I(2)(d): 적절한 control mechanisms를 통한 비인가 접근 방지 및 가능한 비인가 접근 보고.
- Annex I Part I(2)(f): 사용자 승인 없는 조작/변경으로부터 데이터·명령·프로그램·설정의 무결성 보호.
- Annex I Part I(2)(j): 외부 인터페이스를 포함한 attack surface 제한.

## 4. #2/#4와 중복성 분석

#2/#4/#5는 같은 secure-by-default/initial-auth/port-hardening 주제를 반복한다. 이 세 보고서에서 신규 Canonical Requirement를 만들지 않는다. 통합 정본에는 secure-by-default, access control, integrity, attack-surface를 하나의 절에서 분리 설명하고, 고정 비밀번호·최초 강제 변경·모든 포트 차단은 제품별 위험기반 설계 선택으로 기록한다. 세 원본의 blob SHA와 서로 다른 인용 오류는 각각 감사 이력으로 보존한다.

## 5. 정정 및 후속 조치

1. Article 10을 제조자 의무 조항으로 기재한 모든 문장을 Article 13과 대조해 수정한다.
2. Annex I Part I(2)(a)/(b)/(d)/(f)/(j)의 요구를 정확히 분리한다.
3. password/port/diagnostic-interface 정책은 제품 SKU, 서비스 목록, 사용자·현장 요구, 위험평가 및 검증시험이 확보되기 전까지 구현 후보로만 관리한다.
4. #2/#4/#5의 중복 서술은 한국어 정본의 단일 절로 통합한다.
5. 모든 DUT 시험은 현재 NOT_RUN이며 본 감사는 CRA 적합성 PASS를 의미하지 않는다.

