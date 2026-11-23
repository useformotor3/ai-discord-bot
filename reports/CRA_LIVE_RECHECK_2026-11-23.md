# CRA 최신 공개자료 재점검 — 2026-11-23

- 기준일: 2026-11-23 (KST)
- 작업 브랜치: `research/cra-2026-11-23-live-recheck`
- 기준 main: `324570b64affdfc03866df792eabfd67033db6b6`
- 범위: EU Cyber Resilience Act(CRA) only. SIL 3 분석은 포함하지 않는다.
- 목적: 2026-11-23 공개 원문 재조회 결과를 이전 스냅샷과 구분해 기록한다.

## 1. ETSI EN 304 625 최신 상태

공식 ETSI Work Item `DEN/CYBER-EUS-0017` 페이지는 2026-11-21 갱신된 Work Programme v2.3.3 화면에서 다음을 표시한다.

- ETSI 문서번호: EN 304 625
- 제목: Cybersecurity requirements for physical and virtual network interfaces
- 현재 상태: `Draft Review after PE (2026-11-19)`
- 최신 버전: 1.0.0
- 표지일: 2026-08-10
- CRA M/606 연계: Yes / candidate for harmonisation
- ETSI Remarks: EC second assessment가 2026-09-28 및 2026-11-16 두 차례 comment batch로 접수되었다고 기록.

해석 및 제한:
1. 위 상태는 초안 검토 단계다. 최종 EN 발행, 유럽조화표준으로서 OJ 공표, CRA Article 27 적합성 추정 발생을 의미하지 않는다.
2. 페이지의 Harmonised Standard 표시는 작업 항목의 목적/분류 메타데이터다. OJ 인용 여부와 동일하지 않다.
3. 서보 드라이브의 EtherCAT 포트가 있다는 사실만으로 EN 304 625의 적용 범위, Annex III 분류 또는 적합성 추정을 확정하지 않는다. 해당 표준의 최종 scope, 법령상 제품 분류, 인터페이스가 제품의 핵심 기능 및 별도 판매 단위와 맺는 관계를 함께 확인해야 한다.

공식 원문:
- https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=74860

## 2. M/606 AMD 1 회의 상태 — 개최 결과와 일정 게시 구분

ETSI 공식 Technical Body 달력에는 `GoSRSReq006-M/606 AMD 1 - examination meeting`이 2026-11-23 온라인 회의로 게시되어 있다. 동일 날짜의 CRA Network Interfaces(EN 304 625) 관련 CYBEREUSR 회의도 달력에 표시된다.

그러나 이번 재조회에서 공개적으로 확인 가능한 회의 결과, 회의록, 결정문 또는 ESO별 수령/비수락 통지는 확보하지 못했다.

따라서 상태를 다음과 같이 관리한다.
- 회의 일정 게시: Confirmed
- 실제 개최 여부 및 결과: Unknown
- CEN/CENELEC/ETSI의 C(2026)7861 수령일: Unknown
- C(2026)7861 Article 2의 1개월 내 비수락 통지 여부: Unknown
- C(2026)7861 최종 적용 상태: Unknown

결정일(2026-11-10)을 ESO 수령일로 간주하거나, 2026-12-10을 자동으로 법적 만료일이라고 계산하지 않는다.

공식 원문:
- https://portal.etsi.org/tb.aspx?TBID=287&subTB=287

## 3. M/606 일정과 제조사 의무 기한의 구분

European Commission의 CRA standardisation 페이지는 2026-11-10 표준화 요청 개정으로 모든 vertical 표준과 일부 horizontal 표준의 deliverable 일정을 3개월 연장했다고 설명한다. C(2026)7861 Annex I 일정표의 세부 날짜는 이전 조사에서 공식 결정의 Annex 원문 확보가 되지 않아 2차 추적 자료와 대조한 값으로 관리한다.

| M/606 항목 | deliverable 목표일 | 관리상 주의 |
|---|---:|---|
| Item 1, Item 15 | 2026-11-30 | horizontal deliverables |
| Items 16–41 | 2027-01-31 | 26개 vertical deliverables |
| Items 2–14 | 2027-10-30 | 기존 목표일 유지 |

이 날짜는 ESO가 표준화 deliverable을 제출하는 목표일이지, 제조사의 CRA 준수 기한이 아니다. 표준 초안의 존재나 제출만으로 CRA Article 27의 적합성 추정이 발생하지 않는다. 해당 표준의 참조가 OJ에 공표되었는지, 공표 범위/제한이 무엇인지 별도로 확인해야 한다.

공식 Commission 설명:
- https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation

법적 원문:
- Commission Implementing Decision C(2026) 7861 final, 2026-11-10
- https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_0/de00000001090398
- Article 2 수령일 및 비수락 통지 상태는 별도 증거가 확보될 때까지 Unknown.

## 4. LS메카피온 iX700M 매뉴얼 인덱스 재점검

2026-11-23 재조회에서 제조사 및 LS ELECTRIC 공개 인덱스의 다음 항목을 재확인했다.

| 출처 | 문서 항목 | 인덱스 날짜 | 확보 상태 |
|---|---|---:|---|
| LS메카피온 매뉴얼 | iX700M DRIVE 400[V] 매뉴얼 Ver1.4 | 2026-05-26 | 목록 메타데이터만 확인 |
| LS ELECTRIC Solution Square | iX700M 사용 설명서 | 2026-09-16 | 목록 메타데이터만 확인 |
| LS메카피온 매뉴얼 | PEGA2 매뉴얼 Ver1.3 | 2026-04-01 | 목록 메타데이터만 확인 |
| Solution Square | PEGA2 사용 설명서 | 2026-08-28 | 목록 메타데이터만 확인 |

중요 제한:
- Solution Square 목록의 2026-09-16 날짜는 문서 목록의 update 날짜로 확인했다. 파일명, 문서 revision, PDF 본문, SHA-256은 확보하지 못했다.
- LS메카피온 Ver1.4 PDF 바이너리도 이번 작업에서 확보하지 못했다.
- 날짜가 더 늦다는 이유만으로 Solution Square 문서를 Ver1.5 또는 Ver1.4 이후 개정판이라고 부르지 않는다.
- EtherCAT, Modbus-RTU, 펌웨어 업데이트, 진단, 파라미터 접근, 인증/접근통제, secure boot, 서명검증, 디버그 포트, 취약점 처리 관련 내용은 PDF 본문을 확보해 페이지 단위로 확인하기 전까지 판정하지 않는다.

공식 인덱스:
- https://www.lsmecapion.com/bbs/board.php?bo_table=manual
- https://ssq.ls-electric.com/kr/ko/product/category/4?pageNumber=14
- Solution Square 검색 결과: https://sol.ls-electric.com/kr/ko/newSearch?pageNumber=70

## 5. 자동화 상태의 최소 검증

GitHub Actions 조회 결과:
- 운영 CRA 자동 조사 workflow Run #2546 / ID `45155788066`
- 이벤트: schedule
- 실행 시작: 2026-11-23T10:24:21Z
- 대상 main SHA: `324570b64affdfc03866df792eabfd67033db6b6`
- 결론: success
- 단계: 자동 조사 스크립트, 결과 요약 단계, 데이터 검증/복원 guard, 오래된 checkpoint pruning 단계 모두 success로 표시.

해석 제한:
- Workflow job success는 자동화 스크립트가 오류 없이 종료되었다는 운영 신호다. 새롭고 유효한 CRA 자료가 수집되었다는 품질 보증과 동일하지 않다.
- 이번 조회에서 run artifact는 없었다. 상세 Step Summary 본문과 해당 run이 실제로 추가한 신규 증거의 품질까지 확인한 것으로 주장하지 않는다.
- 운영 schedule, workflow, secrets, API cadence는 변경하지 않았다.

Run:
- https://github.com/useformotor3/ai-discord-bot/actions/runs/45155788066

## 6. 다음 우선순위

1. ETSI GoSRSReq006 회의 결과/회의록 또는 공개 contribution/email archive를 재확인한다. 공개 자료가 없으면 ETSI 사무국/GoSR 연락처에 공식 확인이 필요한 항목으로 남긴다.
2. CEN, CENELEC, ETSI의 C(2026)7861 실제 수령일 및 Article 2 비수락 통지 여부를 공식 근거로 확인한다.
3. Solution Square의 iX700M 사용 설명서 실제 파일 식별자와 다운로드 원본을 확보하고, PDF SHA-256·문서번호·revision history·페이지 수를 기록한다.
4. iX700M Ver1.4와 Solution Square 파일을 확보한 뒤 문서 본문 및 바이너리 비교를 수행한다.
5. 제품별 CRA 판정은 실제 SKU, Converter/Drive Unit 판매 경계, HW/FW, BOM, ST MCU 전체 주문 코드와 보안 구성 자료가 확보될 때까지 Unknown으로 유지한다.

## 7. 검증 원칙

- 인덱스 메타데이터와 문서 본문을 구분한다.
- 회의 일정과 회의 결과를 구분한다.
- 표준화 목표일, 표준 발행일, OJ 인용일, 제조사 CRA 적용 의무일을 구분한다.
- 출처가 없는 제품 보안 기능은 존재/부재를 단정하지 않는다.
- 미확인 상태는 Unknown으로 표시하고, 이를 적합 또는 부적합으로 치환하지 않는다.
