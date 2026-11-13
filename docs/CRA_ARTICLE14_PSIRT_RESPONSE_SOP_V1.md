# CRA Article 14 취약점·심각한 사고 대응 절차서 (PSIRT SOP)

- 문서 ID: CRA-PSIRT-SOP-001
- 버전: 1.0
- 기준일: 2026-11-13
- 상태: **운영 절차 초안 / 조직 책임자·법무 검토 필요**
- 법적 기준: Regulation (EU) 2024/2847 Article 14, Article 13(17), Commission CRA reporting obligations
- 공식 출처: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- Commission 안내: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

> 이 절차는 CRA Article 14 대응을 위한 내부 운영 초안이다. 실제 법적 신고 판단·제출은 제조사 지정 책임자와 법무/규제 담당자가 확인해야 한다. 실제 제조사·제품·CSIRT 연락처가 미확정이므로 담당자와 연락처는 TBD로 남긴다.

## 1. 목적과 적용 범위

제품에 포함된 적극 악용 취약점 및 제품 보안에 영향을 미치는 심각한 사고를 접수·분류·신고·완화·최종 보고하는 절차를 정의한다. 모든 취약점이 자동으로 Article 14 신고 대상인 것은 아니므로 취약점 처리(Annex I Part II)와 Article 14 신고 트리거 판단을 분리한다.

2026-09-11부터 Article 14 신고 의무가 적용 중이다. 따라서 제품 출시 여부와 무관하게 PSIRT 접수·판단·에스컬레이션 절차를 준비하고 모의훈련해야 한다.

## 2. 역할 및 책임

| 역할 | 책임 | 현재 지정 |
|---|---|---|
| PSIRT Lead | 접수 사건의 조정, 인지 시각/기한 관리, 사건 기록 | TBD |
| Product Security Engineer | 제품·버전·구성요소 영향 분석, 재현·완화·패치 | TBD |
| Product Owner | 영향 제품·고객·출시/지원 상태 확인, 자원 결정 | TBD |
| Legal/Regulatory | Article 14 트리거 및 신고 문안·관할 절차 검토 | TBD |
| Communications/Customer Support | 영향 사용자 통지 및 고객 대응 | TBD |
| Executive Escalation | 심각 사건·기한 초과 위험의 의사결정 | TBD |
| Supplier Contact | 구성요소 공급자와 취약점 정보 공유 | TBD |

한 사람이 여러 역할을 맡을 수 있으나, 역할별 대체 담당자와 24시간 연락 수단을 사전에 지정해야 한다.

## 3. 접수 채널과 필수 기록

접수 채널(보안 이메일/웹 폼/전화/내부 사고 채널)은 제조사 단일 연락 창구와 연결한다. 공개 주소는 실제 제조사 결정 후 기입한다.

최초 접수 시 다음을 기록한다.

- case_id, 접수 일시 및 시간대, 접수 채널, 신고자 연락 수단(필요 최소)
- 제품명/SKU/버전/HW revision/FW hash/영향 구성요소
- 취약점 설명, 재현 단계, 공격 전제조건, PoC 존재 여부
- 공개/악용 징후, 관찰된 사고, 영향 범위, 탐지 시각
- 임시 완화, 패치 존재 여부, 고객 영향
- 원본 첨부파일 hash 및 접근 통제 위치
- 내부 인지 시각(T0)과 그 근거(이메일 수신/모니터링 경보/직원 보고 등)

신고자 개인정보·비밀키·실제 고객 자격증명은 공개 저장소에 기록하지 않는다.

## 4. 사건 분류

### 4.1 취약점 처리 트랙
모든 제품 취약점은 Annex I Part II에 따른 취약점 처리 프로세스에 들어간다. 영향 제품/구성요소 식별, 위험평가, 공급자 협업, 완화·수정, 업데이트, 공개 정책을 기록한다.

### 4.2 Article 14 신고 트랙
법령상 두 유형을 별도로 판단한다.

A. 제품에 포함된 actively exploited vulnerability인지 확인한다.
- 취약점이 제품 또는 제품에 통합된 구성요소에 존재하는가?
- 실제 적극 악용되고 있다는 신뢰할 수 있는 정보가 있는가?
- 제품/버전/구성요소 영향이 확인되었는가?
- 인지 시각과 판단 근거가 기록되었는가?

B. product security에 impact를 미치는 severe incident인지 확인한다.
- 사건이 제품의 보안에 영향을 주는가?
- 법령상 severe incident 기준에 해당하는 사실이 있는가?
- 제품/버전/영향·확산 범위 및 인지 시각이 확인되는가?

두 트랙의 결론은 각각 기록한다. 단순 취약점 제보, 악용 가능성, 일반 장애를 Article 14 신고 대상으로 자동 분류하지 않는다. 불확실한 경우 즉시 Legal/Regulatory와 PSIRT Lead에 에스컬레이션하고 기한을 보수적으로 추적한다.

## 5. 법정 기한 관리

| 신고 유형 | 이벤트 | 기한 | 타이머 |
|---|---|---|---|
| 적극 악용 취약점 | 제조사가 인지 | 조기 경고 24시간 이내 | T0 + 24h |
| 적극 악용 취약점 | 제조사가 인지 | 신고 72시간 이내 | T0 + 72h |
| 적극 악용 취약점 | 시정/완화 조치 제공 | 최종 보고 14일 이내 | Tfix + 14d |
| 심각한 제품 보안 사고 | 제조사가 인지 | 조기 경고 24시간 이내 | T0 + 24h |
| 심각한 제품 보안 사고 | 제조사가 인지 | 신고 72시간 이내 | T0 + 72h |
| 심각한 제품 보안 사고 | 72시간 신고 제출 | 최종 보고 1개월 이내 | T72 + 1 calendar month |

운영 규칙:
- T0는 법령상 제조사의 인지 시점을 기준으로 하고, 내부 접수 시각과 별도로 법무/규제 책임자가 확정한다.
- 시간대는 UTC와 원래 현지 시간대를 함께 기록한다.
- 기한은 담당자 부재와 주말을 이유로 늦추지 않도록 대체 담당자를 둔다.
- 법령·플랫폼 운영지침이 바뀌면 기한 계산을 재검토한다.
- 최종 제출 전 제출 경로·관할 CSIRT·필수 필드·보안정보 취급을 공식 최신 안내로 확인한다.

## 6. 대응 흐름

1. 접수 및 사건 ID 발급
2. 원본 증거 보존, 인지 시각 기록, 담당자 지정
3. 제품·버전·구성요소·공급망 영향 식별
4. actively exploited vulnerability 및 severe incident 별도 판단
5. 신고 트리거 검토와 법정 기한 타이머 시작
6. 제품 위험평가 갱신 및 임시 완화 결정
7. 공급자/통합자/관련 이해관계자와 필요한 정보 공유
8. 신고 대상이면 CRA Single Reporting Platform을 통한 지정 CSIRT 제출 절차 진행
9. 보안 업데이트/완화 배포, Article 14(8) 적용 사건의 사용자 영향·통지 판단
10. 최종 보고 제출 및 원인·시정·재발방지 기록
11. 사건 종료 검토, 교훈·위험평가·SBOM·테스트 케이스 갱신

## 7. 제출·정보 공유 기록

각 제출/통지 이벤트에 대해 다음을 남긴다.

- submission_id, 사건 ID, 신고 유형, 제출 시각, 시간대
- 제출 경로/관할 CSIRT, 제출자, 승인자
- 제출 자료의 버전/hash, 수정 이력, 수신 확인
- 공개 가능 정보와 제한 정보 구분
- ENISA/CSIRT 공유·후속 요청·시장감시기관 관련 기록(해당 시)
- 사용자 통지 여부, 통지 대상/시각/채널/내용
- Article 14(8) 사건이면 actively exploited vulnerability 또는 severe incident 해당 근거, 영향 사용자 범위, 통지 필요성, where appropriate machine-readable 형식 판단 및 사용자에게 제공한 완화·시정 조치
- Article 14(8)의 machine-readable 형식은 해당 사건의 사용자 통지에 대한 조건부 요구다. 모든 취약점/보안 권고를 자동 기계 판독 형식으로 배포해야 한다는 일반 의무로 확대하지 않는다.
- 미제출 판단 시 법적 근거·사실·승인자

CRA Single Reporting Platform을 통한 제출 구조를 기준으로 한다. 내부 자동화가 외부 기관에 직접 임의 전송하도록 만들지 말고, 제출 권한·승인·수신확인 기록을 통제한다.

## 8. 사건 기록 템플릿

| 필드 | 값 |
|---|---|
| Case ID | TBD |
| Product/SKU/Version | TBD |
| Affected component | TBD |
| Vulnerability/Incident summary | TBD |
| Awareness timestamp T0 (UTC + local) | TBD |
| Actively exploited? | YES / NO / UNKNOWN |
| Severe incident affecting product security? | YES / NO / UNKNOWN |
| Article 14 reportable? | YES / NO / LEGAL REVIEW |
| 24h deadline | T0 + 24h |
| 72h deadline | T0 + 72h |
| Corrective/mitigating measure available | TBD |
| Final report deadline | Tfix + 14d OR T72 + 1 month |
| Interim mitigation | TBD |
| Affected customers/products | TBD |
| CSIRT submission reference | TBD |
| User notification | TBD |
| Evidence hashes/locations | TBD |
| Reviewer/approver | TBD |

## 9. 모의훈련 시나리오

| Exercise ID | 시나리오 | 검증 포인트 | 상태 |
|---|---|---|---|
| PSIRT-EX-01 | 서보 드라이브 펌웨어의 actively exploited vulnerability 제보 | T0, 24h/72h/14d 타이머, 제품 영향 식별 | NOT_RUN |
| PSIRT-EX-02 | 제품 보안에 영향을 미치는 심각한 사고 | severe incident 판단, 24h/72h/1개월 기한 | NOT_RUN |
| PSIRT-EX-03 | 취약점은 확인됐으나 적극 악용 증거가 없음 | Annex I 취약점 처리와 Article 14 신고 트랙 분리 | NOT_RUN |
| PSIRT-EX-04 | 외부 MCU/라이브러리 구성요소 취약점 | 공급자 통지·SBOM 영향 매핑·패치 책임 | NOT_RUN |
| PSIRT-EX-05 | 주말/담당자 부재 중 신고 접수 | 대체 담당자·에스컬레이션·기한 보존 | NOT_RUN |

훈련 결과에는 실제 경과 시간, 누락된 정보, 의사결정 지연, 역할 공백, 개선 조치를 기록한다.

## 10. 운영 전 필수 확정 사항

- 제조사 법인 및 단일 연락 창구
- PSIRT Lead 및 24시간 대체 연락망
- Legal/Regulatory 승인자
- 제품/SKU/지원 대상 버전 인벤토리
- 공급자 보안 연락 채널
- CRA Single Reporting Platform 접근/제출 담당
- 고객 통지 승인 및 언어/지역별 템플릿
- 증거 보존·기밀정보 접근통제
- 모의훈련 주기 및 관리 검토

현재 조직·제품 입력이 없어 모든 역할/채널은 TBD, 모든 훈련은 NOT_RUN이다.

## 11. 공식 근거

- Regulation (EU) 2024/2847, Article 14 및 Article 13(17): https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- European Commission, CRA reporting obligations: https://digital-strategy.ec.europa.eu/en/policies/cra-reporting

본 절차는 규정 원문 및 유럽연합 집행위원회 안내를 기준으로 작성했다. 신고 플랫폼의 세부 화면/필수 입력항목·국가별 관할은 실제 제출 시 최신 공식 지침을 확인해야 한다.

용어 통일: 적극 악용 취약점, 제품 보안에 영향을 미치는 심각한 사고, 조기 경보, 신고, 최종 보고, 영향 사용자 통지를 구분한다. Article 14(8)의 기계 판독 가능 형식은 적절한 경우에 적용되는 조건부 요구다.


### #48–#52 감사 정정 반영 — 공급망 취약점 및 사용자 통지

- Article 13(6)의 구성요소 취약점 신고 방향은 제품 제조사에서 해당 구성요소 제조사/유지관리 주체로 향한다. 공급자가 항상 상위 제조사에 자동 통지해야 한다는 일반 CRA 의무로 표현하지 않는다.
- Article 14(8)의 사용자 통지는 적극 악용 취약점 또는 제품 보안에 영향을 미치는 심각한 사고에 대한 통지다. 구조화된 기계 판독 가능 형식은 “where appropriate(적절한 경우)” 조건이며 모든 취약점 공지에 일률 적용하지 않는다.
- Annex I Part II(4) 수정 취약점 공개, (5) CVD 정책, (6) 취약점 신고 연락처, (7) 안전한 업데이트 배포, (8) 원칙적 무상 보안 업데이트를 서로 구분한다.
- 지원기간은 Article 13(8), 지원기간 중 제공된 각 보안 업데이트의 보존·가용성은 Article 13(9)로 관리한다.
- 상세 원문·SHA·반증: [#48–#52 감사 보고서](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_48_52_2026-11-13.md).

## #58–#62 감사 정정 — 신고 트리거·수신자·기한

- 일반 취약점 접수·처리·CVD는 Article 13(8), Annex I Part II(5)/(6)에 따라 모두 관리한다. 그러나 모든 일반 취약점이 Article 14 의무 신고 대상은 아니다.
- Article 14 신고 트리거는 (1) actively exploited vulnerability, (2) 제품 보안에 영향을 미치는 severe incident 두 가지로 분리한다.
- actively exploited vulnerability: 24h early warning, 72h vulnerability notification, corrective/mitigating measure가 이용 가능해진 후 14일 이내 final report.
- severe incident: 24h early warning, 72h incident notification, incident notification 제출 후 1개월 이내 final report.
- 제조자는 Article 14(7)에 따라 지정 CSIRT의 전자 신고 엔드포인트/단일 신고 플랫폼을 이용하며 ENISA에 동시에 접근 가능하게 한다.
- 시장감시기관은 제조자의 Article 14 직접 신고 수신자로 적지 않는다. CSIRT가 Article 16(3)에 따라 필요한 정보를 시장감시기관에 제공한다.
- Article 14(8) 사용자 통지는 actively exploited vulnerability 또는 severe incident에 대한 통지이며, 영향 사용자와 적절한 경우 모든 사용자에게 제공한다. 기계 판독 가능 형식은 where appropriate 조건이다.
- CVD 신고 연락 주소(Part II(6)), 사용자 단일 연락 창구(Article 13(17)), Annex II(2) 사용자 정보는 각각 확인한다.

원문 대조: [main reports #58–#62 감사](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_58_62_2026-11-13.md).
