# CRA 보고서 #37 정정 — 지원기간·업데이트 무상 제공 및 잘못된 조항 인용

- 원본: `research_archive/2026-11-17_131038065348_72e44c49.md`
- 원본 blob SHA: `737f20541a2b1df6cf39dced198eeaa330000b5d`
- 원본 보존: 변경하지 않음
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 핵심 정정

1. Article 10은 회원국의 사이버 복원력 역량 증진, Article 11은 General product safety다. 둘 다 원본 보고서가 인용한 manufacturer obligations 또는 CVD/취약점 처리의 직접 근거가 아니다.
2. 제조사 의무는 Article 13이다. Article 13(8)은 support period 동안 취약점이 효과적으로 처리되도록 하고, 예상 사용기간과 사용자 기대 등을 고려해 지원기간을 정하도록 한다. 기본 최소는 5년이며 예상 사용기간이 5년보다 짧으면 그 예상 기간을 적용한다.
3. Article 13(9)은 지원기간 중 사용자에게 제공된 보안 업데이트 각각이 발행 후 최소 10년 또는 지원기간 잔여기간 중 더 긴 기간 동안 이용 가능하도록 요구한다. 이를 '최소 5년 이상 권장' 또는 '10년 지원기간'으로 단순화하지 않는다.
4. Annex I Part II (2)는 취약점을 지체 없이 처리·시정하고 보안 업데이트를 제공하며, 기술적으로 가능한 경우 기능 업데이트와 분리하도록 한다. Part II (7)은 안전한 업데이트 배포, Part II (8)은 지체 없는 무상 배포를 규정한다. Part II (8)의 맞춤형 제품/business user 합의 예외를 함께 표시한다.
5. CVD 정책은 Article 13(8) 및 Annex I Part II (5), 제보 연락처는 Article 13(17)/Annex II (2), fixed-vulnerability 공개는 Annex I Part II (4)다.
6. 서보 드라이브를 Annex III Class II라고 단정할 근거는 없다. Annex III Class II의 실제 열거는 hypervisors/container runtime, firewalls/IDS/IPS, tamper-resistant microprocessors 및 microcontrollers다. 제품의 core functionality가 이 목록에 해당하는지 확인해야 한다.
7. 원본의 Annex I Part II (b)/(c)/(d) 인용은 번호·문구가 최종 OJ와 맞지 않는다. 최종 OJ Annex I Part II는 (1)~(8) numbered list다. 직접 인용은 OJ의 정확한 문언과 번호를 재확인한 뒤에만 사용한다.

## 수정 권고 문안

제조사는 Article 13(8)에 따라 제품의 예상 사용기간을 반영한 지원기간을 설정하고, 최소 5년 원칙 및 예상 사용기간이 더 짧은 경우의 예외를 적용한다. 지원기간 동안 Annex I Part II의 취약점 처리 프로세스를 유지하고, Part II (2), (7), (8)에 따라 취약점 시정, 안전한 업데이트 배포, 지체 없는 무상 보안 업데이트를 제공한다(맞춤형 제품/business user의 명시적 합의 예외 포함). Article 13(9)의 업데이트 장기 이용 가능성은 별도 보존 정책으로 구현한다.

## 공식 근거

- Article 10–11, Article 13(8)–(9)
- Annex I Part II (2), (4)–(8)
- Annex III
- 공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
