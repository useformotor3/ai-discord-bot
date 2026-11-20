# CRA ETSI EN 304 635 최신 상태 및 자동조사 Run #2526 사후 검증 — 2026-11-21

## 1. 조사 범위와 기준

- 확인 기준시각: 2026-11-21 (KST)
- 저장소 main 기준 SHA: `5be75068b7413e39bd1b2509d65e715d96907ae5`
- 변경 범위: 문서·감사로그만. `main.py`, 운영 workflow, secrets, Gemini/Discord 호출 설정 및 운영 데이터는 변경하지 않음.
- 공식 자료 우선순위: ETSI Work Programme live listing / individual Work Item record / ETSI download page / EUR-Lex binding law.

## 2. EN 304 635 최신 상태 — 기존 기록 정정

### 2.1 최신 버전 및 상태

ETSI Work Programme의 2026-11-21 조회 결과에서 DEN/CYBER-EUS-0016 (EN 304 635)의 최신 버전은 **V1.0.9**로 표시된다.

- Current status: **EC assessment before WNV requested (2026-11-19)**
- Next status: **EC assessment before WNV received (2026-11-28)**
- Remarks: 2026-11-20 새 draft V1.0.9 업로드. 상태는 **Draft Review after PE**이며, 설명은 Enquiry 및 EC HAS2 comments 해결을 포함한 CYBER-EUSR 승인 버전이라는 것.
- Work Item: DEN/CYBER-EUS-0016; ETSI WKI_ID=74858.
- ETSI Work Programme search result와 Work Item Monitoring은 V1.0.9 / 2026-11-19 상태를 일치하게 표시한다.

주의: 기존에 열람한 일부 개별 상세 페이지 캐시는 V1.0.1 / 2026-09-17 상태를 계속 표시했다. 따라서 개별 상세 페이지의 stale snapshot을 최신 상태로 간주하지 않는다. 이번 감사는 live Work Programme query result와 Work Item Monitoring의 교차 확인을 우선 근거로 삼는다. 원본 상세 페이지의 캐시/갱신 불일치 자체도 추적 이슈로 남긴다.

### 2.2 공개 다운로드 파일의 버전 한계

ETSI 공식 Download area는 무료 개별 다운로드 publication으로 **EN 304 635 V1.0.1 (2026-06), 2,700,830 bytes**를 표시한다. 이 항목은 공식 다운로드 경로의 존재를 확인하지만, V1.0.9 최신 draft와 동일한 버전이 아니다.

- V1.0.1 public preview/sample은 이전 감사에서 15쪽 Scope를 확인했으며 Annex III Class II point 1 문구가 확인되었다.
- V1.0.1 download-area listing은 V1.0.9 full draft 확보 증거가 아니다.
- 이번 조사에서는 다운로드 페이지에서 실제 PDF bytes를 가져오거나 SHA-256을 계산하지 않았다.
- 따라서 V1.0.9 본문 전체의 문구, 페이지 수, 변경 이력 및 SHA-256은 **미확인**으로 유지한다.

### 2.3 법적 제품 등급 분류

ETSI Work Item scope text의 Class I 표현과 달리, 법적 분류는 CRA Annex III 및 Commission Implementing Regulation (EU) 2025/2392 Annex I에 따라 **Class II, category 1 (hypervisors and container runtime systems)**이다. ETSI 작업항목 설명문 또는 metadata는 법령의 등급 분류를 변경하지 않는다.

- 법적 근거: Regulation (EU) 2024/2847 Annex III, Class II point 1.
- 기술 설명 보완: Commission Implementing Regulation (EU) 2025/2392 Annex I.
- 이 판단은 hypervisor/container runtime이라는 제품 범주에 대한 법적 분류다. 특정 servo drive 또는 내장 구성요소가 이 범주에 속한다고 자동 추정하지 않는다.

## 3. M/606 회의 일정

ETSI 공식 Technical Body calendar는 **GoSRSReq006-M/606 AMD 1 - examination meeting**을 2026-11-23 온라인 일정으로 표시한다. 2026-11-21 기준 회의 전 상태다.

회의 후 다음을 별도 증거로 확인한다.
1. 회의록 또는 결정문 공개 여부
2. M/606 AMD 1 검토 결과 및 후속 조치
3. ESO 수락·비수락 통지 원본과 실제 수령일
4. 관련 EN Work Item status/version/next milestone의 후속 변경

회의 예정 사실을 회의 개최·결정 완료로 서술하지 않는다.

## 4. 운영 자동조사 Run #2526 사후 검증

- Workflow: Servo Drive CRA Automated Research
- Run: #2526 / ID `44825006768`
- Head: main `5be75068b7413e39bd1b2509d65e715d96907ae5`
- Schedule event: 2026-11-20 21:58:47 UTC 시작 (2026-11-21 06:58:47 KST)
- 예상 cron slot: 21:17 UTC. 관찰된 시작 지연 약 41분 47초.
- Job conclusion: success. 총 실행은 약 41초.
- 공식 source gate: 10개.
- Gemini 3.8 Flash: HTTP 503 과부하로 대체 모델 전환.
- Gemini 3.5 Flash Lite: CRA 공식 EUR-Lex 원문 링크 누락으로 품질 검증 거절.
- main.py 로그: 조사 보류. 전송·아카이브·카운트 변경 없이 종료.
- Operational guard: no-op (운영 데이터 변경 없음); checkpoint pruning 성공.
- Research report/archive/Discord: 신규 보고서 생성 없음, archive 변경 없음, Discord 전송 없음.

분류 기준: 실행 로그의 조사 보류 문구는 classifier의 `DEFERRED` 경로에 해당한다. Summary step은 completed/success로 실행되었다. GitHub Jobs API는 Step Summary의 렌더링 본문 자체를 별도 필드로 반환하지 않으므로, 본 감사는 실제 원시 실행 로그와 classifier 규칙으로 결과를 판정한다. workflow job success를 조사 완료로 계산하지 않는다.

## 5. 결론 및 우선순위

### P0
1. ETSI EN 304 635 V1.0.9 full draft를 공식 경로에서 확보 가능한지 확인한다. 확보 시 원본 bytes, SHA-256, page count, version/date metadata를 기록한다.
2. V1.0.1 공개본과 V1.0.9를 대조해 Enquiry 및 EC HAS2 comment resolution으로 바뀐 요구사항·적합성 평가·범위를 변경표로 작성한다.
3. 2026-11-23 M/606 AMD 1 examination meeting 이후 공식 minutes/decision/status update를 확인한다.
4. EN 304 635/636 Work Item scope의 Class I 표기와 법령상 Class II의 discrepancy를 ETSI metadata correction 대상으로 유지한다.

### P1
1. 18개 M/606 active Work Item matrix를 2026-11-19/20 live status 기준으로 재검증한다. V1.0.9처럼 이전 snapshot이 바뀐 경우 변경일과 source snapshot을 보존한다.
2. 41개 Annex I topic별 실제 EN/ETSI mapping 및 OJ citation field를 제품별/표준별로 계속 대조한다.
3. ESO별 C(2026) 7861 Article 2 수령일과 1개월 내 비수락 통지 여부를 원문으로 확인한다.

## 6. 1차 출처

- ETSI Work Programme live result (DEN/CYBER-EUS-0016, V1.0.9, 2026-11-19 status): https://portal.etsi.org/webapp/WorkProgram/Frame_WorkItemList.asp?SearchPage=TRUE&butSimple=Search&includeNonActiveTB=FALSE&optDisplay=10&qINCLUDE_SUB_TB=True&qREPORT_TYPE=SUMMARY&qSORT=HIGHVERSION&qTB_ID=824%3BCYBER
- ETSI Work Item Monitoring: https://portal.etsi.org/Portal_WI/Form1.asp?NbToDisplay=30&PersonId=0&SubTB=&SupCrit=CYBER+++++++++++++++++++++18878249&TabId=&TbId=0&WIcritID=18
- ETSI official free download area, V1.0.1 listing: https://portal.etsi.org/webapp/ewp/copy_file.asp?wki_id=74858
- ETSI M/606 AMD 1 meeting calendar: https://portal.etsi.org/tb.aspx?TBID=442&subTB=442
- CRA consolidated legal text: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847
- Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/eli/reg_impl/2025/2392/oj/eng
- GitHub production run #2526: https://github.com/useformotor3/ai-discord-bot/actions/runs/44825006768

## 7. 검증 한계

- ETSI Work Programme query result and monitoring show V1.0.9; a cached individual detail page still showed V1.0.1. The disagreement is explicitly retained, not silently reconciled.
- V1.0.9 full PDF was not acquired; no page count/content/hash claims are made.
- V1.0.1 download-area listing is not proof of V1.0.9 availability.
- Meeting is scheduled for 2026-11-23; minutes/decision are not yet verified.
- Run #2526 was operationally successful but research was deferred; no new report/archive/Discord delivery occurred.
