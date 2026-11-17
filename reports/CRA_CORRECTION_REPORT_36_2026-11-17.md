# CRA 보고서 #36 정정 — Article 14 단계별 신고 시한

- 원본: `research_archive/2026-11-17_130541904347_82e74d12.md`
- 원본 blob SHA: `584ee8b56d2c872a6352fe20ca8fbc7152f62ac6`
- 원본 보존: 변경하지 않음
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 핵심 정정

1. **Actively exploited vulnerability** — Article 14(1)–(2): 24시간 이내 early warning, 72시간 이내 vulnerability notification, corrective/mitigating measure가 available된 뒤 14일 이내 final report.
2. **Severe incident** — Article 14(3)–(5): 24시간 이내 early warning, 72시간 이내 incident notification, incident notification 제출 후 1개월 이내 final report. '인지 후 1개월'로 표현하지 않는다.
3. **24h early warning 내용**: 최종 OJ Article 14(2)(a)는 제품이 제공된 회원국을 가능한 경우 표시하도록 한다. 원본 보고서에 포함된 '악의적 행위자에 의한 악용 여부 및 국경 간 위협 여부' 문구는 이전 초안 계열의 문언과 혼동된 것으로, 최종 OJ의 해당 point 직접 인용으로 사용할 수 없다. Severe incident early warning의 Article 14(4)(a)는 위법/악의적 행위 의심 여부 등을 포함한다.
4. **신고 플랫폼**: Article 14(7)는 Article 16 single reporting platform을 통해 제조사의 주된 EU establishment 소재 회원국의 coordinating CSIRT endpoint로 제출하고 ENISA에 동시에 접근 가능하도록 한다. 단순히 각국 CSIRT와 ENISA에 별도 이메일을 보내는 방식으로 축약하지 않는다.
5. **사용자 통지**: Article 14(8)는 actively exploited vulnerability 또는 product security에 영향을 주는 severe incident를 인지한 뒤 영향받는 사용자, 적절한 경우 모든 사용자에게 위험 완화/시정 조치를 알리도록 한다.
6. **PSIRT**: PSIRT 조직은 합리적인 운영 권고이나 CRA가 'PSIRT'라는 특정 조직명을 모든 제조사에 직접 의무화한 것은 아니다. 의무 요구사항과 권고 조직 모델을 분리한다.

## 수정 권고 문안

제조사는 actively exploited vulnerability와 severe incident를 별도 신고 시계로 관리한다. 전자는 인지 후 24h/72h 및 corrective/mitigating measure available 후 14일, 후자는 인지 후 24h/72h 및 incident notification 제출 후 1개월을 적용한다. 신고 경로는 Article 16 플랫폼과 Article 14(7)의 coordinating CSIRT endpoint/ENISA 접근 조건에 맞춘다. Article 14(8) 사용자 통지와 제조사 내부 PSIRT 운영 모델은 규제기관 신고 시한과 별도로 관리한다.

## 공식 근거

- Article 14(1)–(8), Article 16
- 공식 원문: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
