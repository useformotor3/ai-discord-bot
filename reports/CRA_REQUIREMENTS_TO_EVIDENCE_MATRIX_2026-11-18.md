# CRA 요구사항–표준–서보 드라이브 증거 추적 매트릭스 (2026-11-18)

## 1. 목적과 판정 한계

이 문서는 CRA 법적 요구사항을 제조사의 제품 위험관리, 설계·개발, 검증, 취약점 처리 및 기술문서 증거로 연결하는 **실무 추적 제안**이다. 서보 드라이브 제품군의 공통 평가 프레임워크이며 특정 제조사·모델의 적합성 판정서가 아니다.

중요한 구분:
- **법적 근거**: Regulation (EU) 2024/2847의 조항/Annex. 실제 의무는 해당 법문 및 제품 적용조건에서 발생한다.
- **표준 연결**: EN 40000-1-2의 공개된 scope는 전 제품 디지털 요소에 대한 일반 원칙, 위험평가·처리 및 생애주기 활동이다. EN 40000-1-3은 취약점 처리 표준 초안으로 공식 CEN 레코드상 Under Approval이다. 이 보고서는 공개 scope와 CRA 법문만 연결하며 표준의 미확인 조항 번호나 문장을 만들어내지 않는다.
- **엔지니어링 제안**: 각 행의 통제/시험/증거 예시는 설계·검증 실무안이며 CRA 법문에 동일 문구로 열거된 요구라고 주장하지 않는다.
- **제품 판정**: 제품 모델, 사용설명서, BOM/SBOM, 펌웨어 구성, 통신 구조, 원격 데이터 처리 및 시장 공급 경계가 없으므로 모든 제품별 상태는 미확인이다.

## 2. 표준 원문 접근 상태

| 표준 | 2026-11-18 확인 상태 | 이 매트릭스에서의 사용 |
|---|---|---|
| EN 40000-1-1:2026 | CEN 공식 프로젝트 레코드 Published, DAV 2026-11-18. CRA OJ citation 필드 No citation expected | 용어 정합성에만 참고. 독립적인 기술 통제 근거로 사용하지 않음 |
| EN 40000-1-2:2026 | 2026-11-02 ratification 및 publishing 단계가 tracker/2차 카탈로그에서 확인됨. iTeh는 Not Published/6055로 표시. 개별 CEN 상세 레코드 readback은 HTTP 500으로 실패 | 공개 scope만 참고. 최종 발행본 전문·조항은 미확인 |
| FprEN 40000-1-3:2026 | CEN 공식 레코드 Under Approval / Citation expected | 취약점 처리 주제의 진행 중 표준화 작업으로만 참고. 승인·발행·OJ 인용으로 간주하지 않음 |
| prEN 40000-1-4 | Work item/drafting | 통제 요구사항의 확정 근거로 사용하지 않음 |

EN 40000-1-2의 공개 scope는 제품 생애주기 전반의 일반 사이버보안 원칙, 위험평가·처리 및 활동을 다루며 제품군별(vertical) 활동·요소는 제공하지 않는다고 명시한다. 따라서 이 표준을 서보 드라이브 전용 상세 설계 규격으로 취급하지 않는다.

## 3. 요구사항–증거 매핑

| ID | 법적 요구/주제 | 서보 드라이브 적용 시 확인할 통제·시험 | 최소 증거 패키지 | 표준 연결 및 상태 |
|---|---|---|---|---|
| EVD-01 | 제품 경계·의도된 목적·구성 (CRA Arts. 2, 3, 13; Annex VII) | 제품/옵션/펌웨어/통신 모듈/PC 도구/클라우드 구성요소의 경계와 공급 주체를 정의. 외부 시스템과 선택 옵션을 구분 | 모델·SKU 목록, intended-purpose 문서, 시스템 컨텍스트, 제품 구성도, 책임 경계표 | 1-2 일반 생애주기/위험관리 맥락. 제품 사실 입력 전 미확인 |
| EVD-02 | 위험평가 (Art. 13(2); Annex I Part I; Annex VII(3)) | 사용환경·오용 가능성·네트워크 연결·원격 접근·정비 경로·안전 영향 등 위험 시나리오 식별 및 평가 | 위험관리 계획, 평가 기준, 위험등록부, 승인/검토 기록, 잔여위험 | 1-2 공개 scope의 risk assessment/treatment와 직접 주제 연계. 규범 조항 상세 미확인 |
| EVD-03 | 자산·공격면·신뢰경계 (Arts. 13(2), 13(7); Annex VII(1),(3)) | 제어 CPU, 파라미터/레시피, 엔코더·필드버스, Ethernet, USB, 디버그 포트, 부트로더, 업데이트 경로, PC 툴 및 원격 서비스 식별 | 자산목록, 데이터흐름도, 네트워크/포트 목록, trust-boundary diagram | 1-2 생애주기 위험관리 제안. 표준 조항 주장 아님 |
| EVD-04 | 보안 설계·기본 구성 (Annex I Part I) | 불필요 서비스·계정 비활성화, 안전한 초기 설정, 최소 권한, 인터페이스 노출 최소화, 보안 설정 변경 통제 | 보안 아키텍처, 기본 설정표, hardening checklist, 설정 검증 결과 | 1-2 일반 원칙 범위. 세부 기술 요구는 법문 및 향후 1-4/수직 표준과 별도 대조 |
| EVD-05 | 인증·접근통제 (Annex I Part I; Annex VII(3),(6)) | 엔지니어링 툴·웹 UI·원격 유지보수·서비스 계정의 인증/권한/세션/계정 수명주기 검증 | 역할-권한표, 인증 설계, 계정 정책, 접근통제 시험, 감사로그 표본 | 일반 risk treatment 연결. 제품 구현 여부 미확인 |
| EVD-06 | 통신·프로토콜 보호 (Annex I Part I; Annex VII(3),(6)) | 지원 프로토콜, 암호화/인증 적용 범위, 평문 관리 인터페이스, 재전송·세션·프로토콜 파싱 경계 검증 | 프로토콜 인벤토리, 통신 흐름도, 보안 설정, 패킷/침투시험 결과 | 1-2 위험평가 프레임. Ethernet/fieldbus 포트만으로 네트워크 인터페이스 제품 분류 금지 |
| EVD-07 | 입력·명령·파라미터 무결성 (Annex I Part I) | 잘못된/경계값/비정상 명령, 파라미터 쓰기, 펌웨어 이미지, 레시피 파일 처리 시험 | 입력 검증 설계, fuzz/negative test 결과, 파라미터 권한 시험, 오류 처리 기록 | 엔지니어링 검증 제안. 법문에 특정 fuzz 기법이 직접 명시된 것은 아님 |
| EVD-08 | 보안 업데이트 설계·배포 (Annex I Part II(7); Art. 13(6)) | 업데이트 인증·무결성, 배포 채널, 설치 실패 복구, 버전 호환성, 롤백/anti-rollback 정책, 사용자 안내 검증 | 업데이트 아키텍처, 서명/검증 설계, 설치·복구 시험, 릴리스 승인 및 배포 로그 | 1-3 취약점 처리/보안 업데이트 주제와 연계. 공개 scope 기반이며 최종 규범 조항 미확인 |
| EVD-09 | SBOM 작성·유지 (Annex I Part II(1); Annex VII(2)(b)) | 직접·전이 의존성 및 최상위 의존성 식별, 제품 릴리스와 SBOM 버전 연결, 형식·완전성 검증 | 기계 판독 SBOM, 생성도구/버전, 빌드 산출물 연결, 검증 로그 | 1-3 공개 scope의 취약점 관리 기반 정보와 연계. CRA 법적 근거는 Annex I Part II(1) |
| EVD-10 | 취약점 접수·분류·우선순위 (Art. 13(6); Annex I Part II(2),(3)) | PSIRT/담당자, 접수 채널, 영향 모델·버전 확인, 심각도·악용 가능성·노출 평가, 처리 SLA 내부 기준 정의 | 취약점 처리 절차, 접수 티켓, triage 기록, 위험 결정 및 추적 이력 | 1-3의 vulnerability identification/documentation 주제. Under Approval 상태 |
| EVD-11 | 취약점 수정·검증·회귀시험 (Art. 13(6); Annex I Part II(2),(3),(7)) | 수정 코드 검토, 재현·수정 확인, 회귀/호환성/안전 관련 회귀시험, 배포 전 승인 | 취약점-수정-릴리스 trace, 코드 리뷰, 시험 결과, 릴리스 승인 기록 | 1-3 공개 scope의 remediation/testing 주제 |
| EVD-12 | 조정된 취약점 공개·보안 공지 (Annex I Part II(5),(6); Art. 13(6)) | 외부 연구자 연락·조정 공개, 사용자 영향 통지, 수정/완화 정보 및 공지 게시 흐름 운영 | 공개 정책, 연락 채널, 공개 타임라인, 보안 권고문, 통지 기록 | 1-3 공개 scope의 coordinated disclosure/advisories 주제 |
| EVD-13 | 지원기간·제품 수명주기 (Art. 13(8); Annex VII(4)) | 예상 사용기간, 산업용 설비 유지주기, 부품 공급·서비스 계획, 지원 종료/보안 업데이트 약속을 근거 기반으로 결정 | 지원기간 결정 메모, 시장/서비스 근거, EOL 정책, 제품별 지원 종료 공지 | 1-2 공개 scope의 lifecycle 활동. 법적 기간 산정은 CRA 법문 우선 |
| EVD-14 | 시험·검토·기술문서 (Arts. 13(7), 13(9), 31; Annex VII(3),(5),(6)) | 설계 통제와 취약점 처리 프로세스의 적합성 시험, 변경 시 재검토, 시험 범위/제외 근거 문서화 | 시험계획·보고서, 기술문서 인덱스, 위험-요구-시험-증거 traceability | 1-2 lifecycle/risk framework, 1-3 vulnerability process와 연계. 법적 문서 근거는 Annex VII |
| EVD-15 | 사고·취약점 신고 및 대응 (Arts. 14, 15) | 악용 중인 취약점/중대 사고 판정, 24h 조기 경보·후속 신고 기산점/조건, 책임자 및 당국 제출 절차 확인 | 신고 의사결정 트리, incident runbook, 타임스탬프 기록, 제출 사본 | 1-3 vulnerability handling 주제와 관련되나 신고 의무의 직접 근거는 CRA Art. 14/15 |
| EVD-16 | 공급망·구성요소·변경관리 (Arts. 13(5), 21–23; Annex VII) | 제3자 구성요소 취약점 확인, 공급자 통지·수정 경로, 펌웨어/하드웨어 변경 영향평가, 상표·실질적 변경자 책임 검토 | 공급자 보안 자료, 구성요소 목록, 변경 영향평가, 공급망 추적기록 | 1-2 lifecycle risk management 및 1-3 vulnerability handling 주제. 역할 책임은 법문 기준 |

## 4. 실행 우선순위 및 완료 게이트

1. **P0 제품 증거 확보**: 정확한 제조사/모델/SKU, 데이터시트, 사용설명서, 펌웨어·옵션 구성, 통신 포트/프로토콜, 원격 유지보수 구조, 제품 경계.
2. **P1 제품별 위험평가**: EVD-01~07의 제품 사실을 확정하고 위험등록부 및 아키텍처를 연결.
3. **P1 취약점·업데이트 운영**: EVD-08~12, EVD-15의 책임자·프로세스·시험·기록 확보.
4. **P2 기술문서 통합**: EVD-13~16을 Annex VII 및 DoC/평가 경로와 연결.
5. **표준 본문 대조**: EN 40000-1-1/1-2 발행본 및 EN 40000-1-3 최종 승인본 전문을 합법적으로 확보한 뒤 clause-by-clause redline을 수행한다. 현재는 공개 scope와 법령 근거만으로 만든 provisional mapping이다.

완료 판정은 단순 문서 존재가 아니라 요구사항-설계통제-시험-결과-제품 버전 간 양방향 추적이 가능하고, 미해결 위험/예외/미검증 항목이 승인 기록과 함께 남아 있을 때만 부여한다.

## 5. 법적 기준 및 공식 출처

- Regulation (EU) 2024/2847, EUR-Lex consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R2847-20241120
- Article 27(1): harmonised standard presumption applies only to references published in the Official Journal and only for requirements covered by the standard: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02024R2847-20241120
- CEN EN 40000-1-1 official project record: https://standards.cencenelec.eu/ords/f?cs=16635E5B87CB4221D8FFC1A74EC94EC6B&p=205:110:::::FSP_PROJECT,FSP_LANG_ID:82349,25
- CEN FprEN 40000-1-3 official project record: https://standards.cencenelec.eu/ords/f?cs=15781C8F1FFD5C2E76320E51B347858F5&p=205:110:::::FSP_PROJECT,FSP_LANG_ID:81343,25
- EN 40000-1-2 secondary status/scope corroboration (not final normative text): https://standards.iteh.ai/catalog/standards/cen/dd8e33f3-6d02-47d9-a878-7f97ad637d3d/en-40000-1-2-2026

## 6. 독립 검토 항목 및 미해결 한계

- 최종 EN 40000-1-1 및 EN 40000-1-2 전문을 직접 확보·검증하지 못했다. 이 문서에는 표준 조항 번호/shall 문장을 인용하지 않았다.
- EN 40000-1-2의 CEN 공식 상세 레코드가 HTTP 500으로 실패했고, 보조 카탈로그는 2026-11-18에도 Not Published/Publishing으로 표시한다. Published 여부는 추후 공식 원문/국가표준기관 발행본으로 재확인한다.
- EN 40000-1-3은 Under Approval이며, 공개 scope를 최종 표준 요구사항으로 오인하지 않는다.
- 제품별 증거가 없으므로 EVD 행의 제품 구현 상태는 전부 Unknown / evidence pending이다.
- 이 매핑은 법률 자문, 인증 결과, Article 27 presumption of conformity 또는 제품 시험 완료를 의미하지 않는다.
