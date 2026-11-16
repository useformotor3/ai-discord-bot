# CRA Archive Queue Recovery Data — 2026-11-16

> Reconstructed from the append-only diffs of the corresponding work-branch queue commits. This is a temporary recovery artifact; entries are re-merged into the canonical queue after validation.

### 2026-11-15 #13 — P1 — 서보 드라이브 제조사는 제품 출시 시 잠재적 공격 표면을 최소화하기 위해 '기본적으로 안전한 상태(Secure by default)'로 설정해야 하며, 특히 인증되지 않은 원격 접
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:00:54 (원문 시간대 미표기)
- 원문: [commit 964d8e42385a763f97cb853330c7f43af19aba4c](https://github.com/useformotor3/ai-discord-bot/commit/964d8e42385a763f97cb853330c7f43af19aba4c) | [research_archive/2026-11-15_010054.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_010054.md) | commit UTC: 2026-11-15T01:01:10.000Z
- 원문 blob SHA: e02285bd75348bf3e463e1b063fc297aecd6233b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출시 시 잠재적 공격 표면을 최소화하기 위해 '기본적으로 안전한 상태(Secure by default)'로 설정해야 하며, 특히 인증되지 않은 원격 접속 및 디버그 포트가 차단된 상태로 공급해야 합니다. 또한, 사용 중 발생하는 보안 관련 이벤트와 로그를 사용자가 모니터링할 수 있도록 필수적인
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #14 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점과 보안 업데이트를 사용자가 쉽게 접근할 수 있는 방식으로 지체 없이 무상 제공해야 하며, 이를 위한 기계독실(Ma
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:05:32 (원문 시간대 미표기)
- 원문: [commit 4d5fc2dfe3ff67109af580cf0b756e5895b52a59](https://github.com/useformotor3/ai-discord-bot/commit/4d5fc2dfe3ff67109af580cf0b756e5895b52a59) | [research_archive/2026-11-15_010532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_010532.md) | commit UTC: 2026-11-15T01:05:48.000Z
- 원문 blob SHA: fea1aea37852bf75dcf4ff5ca28b90b6f8f6a0b3
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점과 보안 업데이트를 사용자가 쉽게 접근할 수 있는 방식으로 지체 없이 무상 제공해야 하며, 이를 위한 기계독실(Machine-readable) 형식의 취약점 정보 공표 체계를 갖추어야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #15 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치하고, 보안 업데이트(패치)를 지체 없이 제공할 법적 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:10:43 (원문 시간대 미표기)
- 원문: [commit bd2c1470840b6621ca51b2e547707fcca0b72715](https://github.com/useformotor3/ai-discord-bot/commit/bd2c1470840b6621ca51b2e547707fcca0b72715) | [research_archive/2026-11-15_011043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_011043.md) | commit UTC: 2026-11-15T01:10:59.000Z
- 원문 blob SHA: dcf707b0ac128670f9ce8ce9953e1e8c8ce90397
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치하고, 보안 업데이트(패치)를 지체 없이 제공할 법적 의무를 집니다. 이는 공장 자동화 현장에서 사용되는 OT/IoT 기기의 지속적인 보안 유지 상태를 강제하기 위한 핵심 요건입니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #16 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점과 보안 조치 정보를 유럽연합 사이버안보국(ENISA) 및 관할 시장 감시 당국에 정해진 법정 기한(조기 경보 24시간 이내) 내
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:15:39 (원문 시간대 미표기)
- 원문: [commit ebb14d621a6d45e17d65a70deb457c76466766e9](https://github.com/useformotor3/ai-discord-bot/commit/ebb14d621a6d45e17d65a70deb457c76466766e9) | [research_archive/2026-11-15_011539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_011539.md) | commit UTC: 2026-11-15T01:15:56.000Z
- 원문 blob SHA: b29986264efd0c1e36b63c3a18f5066afd3bc8fc
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점과 보안 조치 정보를 유럽연합 사이버안보국(ENISA) 및 관할 시장 감시 당국에 정해진 법정 기한(조기 경보 24시간 이내) 내에 자동으로 고지해야 합니다. 또한, 서보 드라이브의 예상 수명 동안 최소 5년 또는 규정된 지원 기간 동안 사용료 청구 없이 무상으로 보안 업
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #17 — P1 — 산업용 서보 드라이브는 공장 출하 시(Out-of-the-box) 인증 우회를 방지하기 위해 고유하고 변경 가능한 초기 비밀번호나 강력한 기본 인증 메커니즘을 갖추어야 하며, 공격
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:20:40 (원문 시간대 미표기)
- 원문: [commit 0ba31b23028c38176bb9b491e9eccc715a252c1f](https://github.com/useformotor3/ai-discord-bot/commit/0ba31b23028c38176bb9b491e9eccc715a252c1f) | [research_archive/2026-11-15_012040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_012040.md) | commit UTC: 2026-11-15T01:20:54.000Z
- 원문 blob SHA: d17006f2c020bad451f8ddb80b762fce6c4bd8f6
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출하 시(Out-of-the-box) 인증 우회를 방지하기 위해 고유하고 변경 가능한 초기 비밀번호나 강력한 기본 인증 메커니즘을 갖추어야 하며, 공격 표면을 최소화하기 위해 불필요한 서비스와 포트가 기본적으로 비활성화된 'Secure by default' 상태로 제공되어야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #18 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 지원 기간(최소 5년)을 명시해야 하며, 지원 종료 시점이 도래하기 최소 1년 전에 최종 사용자에게 명확한 사전 통지(En
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:25:32 (원문 시간대 미표기)
- 원문: [commit 36100f70ee727ac74eb25b3768d1cec16977993c](https://github.com/useformotor3/ai-discord-bot/commit/36100f70ee727ac74eb25b3768d1cec16977993c) | [research_archive/2026-11-15_012532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_012532.md) | commit UTC: 2026-11-15T01:25:48.000Z
- 원문 blob SHA: fba2cbde1e083a2b7bb7e3e24d279605395f3545
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 지원 기간(최소 5년)을 명시해야 하며, 지원 종료 시점이 도래하기 최소 1년 전에 최종 사용자에게 명확한 사전 통지(End-of-Life/Support Notification)를 제공하여 플랜트 운영의 보안 공백을 방지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #19 — P1 — 산업용 서보 드라이브는 제조 시점부터 외부 네트워크 인터페이스(예: 산업용 이더넷)가 활성화되어 공급될 때 발생할 수 있는 잠재적 공격 표면을 최소화하기 위해, 'Secure by
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:30:43 (원문 시간대 미표기)
- 원문: [commit b282918f786bafcb341ff505ae57371fff52cb28](https://github.com/useformotor3/ai-discord-bot/commit/b282918f786bafcb341ff505ae57371fff52cb28) | [research_archive/2026-11-15_013043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_013043.md) | commit UTC: 2026-11-15T01:30:59.000Z
- 원문 blob SHA: aaa8bdbfc6a3d33ef568454d13ae94087637b1c3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 제조 시점부터 외부 네트워크 인터페이스(예: 산업용 이더넷)가 활성화되어 공급될 때 발생할 수 있는 잠재적 공격 표면을 최소화하기 위해, 'Secure by Default(기본 보안 설정)' 원칙에 따라 사용자 인증 및 통신 인터페이스가 안전한 초기 상태로 설정되어야 하며, 이를 입증할 기술 문서와
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #20 — P0 — 서보 드라이브 제조사는 제품 출하 시 무단 접근을 막기 위해 모든 기본 네트워크 포트, 디폴트 계정, 진단 인터페이스가 안전하게 비활성화된 'Secure by Default' 상태
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:35:29 (원문 시간대 미표기)
- 원문: [commit 6b96533468bfa5b2c76ceb75c522ab6569afc9e0](https://github.com/useformotor3/ai-discord-bot/commit/6b96533468bfa5b2c76ceb75c522ab6569afc9e0) | [research_archive/2026-11-15_013529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_013529.md) | commit UTC: 2026-11-15T01:35:45.000Z
- 원문 blob SHA: b6337706328027ed607db8ac7597b24eb17860a1
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출하 시 무단 접근을 막기 위해 모든 기본 네트워크 포트, 디폴트 계정, 진단 인터페이스가 안전하게 비활성화된 'Secure by Default' 상태를 유지해야 합니다. 또한, CRA에 따라 발견된 취약점에 대해 최소 5년 또는 제품의 예상 수명 동안 보안 업데이트를 사용자에게 무상으로 제공
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #21 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 보안 업데이트는 새 기능 추가와 명확히 분리되어 사용자 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:40:41 (원문 시간대 미표기)
- 원문: [commit 9154a6060ca6d1f4c115b99a15e53505bb624493](https://github.com/useformotor3/ai-discord-bot/commit/9154a6060ca6d1f4c115b99a15e53505bb624493) | [research_archive/2026-11-15_014041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_014041.md) | commit UTC: 2026-11-15T01:40:57.000Z
- 원문 blob SHA: d7ac43b610c8160d58896daac6556c62327b9b81
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 보안 업데이트는 새 기능 추가와 명확히 분리되어 사용자 동의 없이 강제 배포되거나 시스템 가동을 중단시켜서는 안 됩니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #22 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용 없이(Free of charge) 제공해야 합니다. 취약점
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:45:42 (원문 시간대 미표기)
- 원문: [commit 24f010bbd09ac6a938814140d6b70af7ed6c4aeb](https://github.com/useformotor3/ai-discord-bot/commit/24f010bbd09ac6a938814140d6b70af7ed6c4aeb) | [research_archive/2026-11-15_014542.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_014542.md) | commit UTC: 2026-11-15T01:45:58.000Z
- 원문 blob SHA: 12b74cc2a66265b32782bf06186d8c9a4c5e33b9
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용 없이(Free of charge) 제공해야 합니다. 취약점 수정 패치는 제조사가 인지한 즉시, 무결성이 보장된 채널을 통해 지연 없이 배포되어야 하며, 이는 Annex I(부속서 I)의 필수 사이버 보
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #23 — P0 — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 취
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:50:42 (원문 시간대 미표기)
- 원문: [commit ba191e300ce3579e02218b0fa72f82fdad685e3c](https://github.com/useformotor3/ai-discord-bot/commit/ba191e300ce3579e02218b0fa72f82fdad685e3c) | [research_archive/2026-11-15_015042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_015042.md) | commit UTC: 2026-11-15T01:50:59.000Z
- 원문 blob SHA: 174158aeaa2ede5121f62c0b1b78eb832472b899
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 취약점 조율 및 공개 프로세스(VDP)를 법적으로 강제 적용받습니다. 이는 단순한 사후 조치가 아닌, 제품 기획 단계부터 설계되
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #24 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 최소 5년 또는 제품의 예상 사용 기간 동안 발견된 취약점에 대해 보안 업데이트를 무상으로 제공해야 합니다. 사용자(시스템 Integr
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 01:55:36 (원문 시간대 미표기)
- 원문: [commit fd6b2ea3b2d3848bca87fb8b1f36a6ee98cd208e](https://github.com/useformotor3/ai-discord-bot/commit/fd6b2ea3b2d3848bca87fb8b1f36a6ee98cd208e) | [research_archive/2026-11-15_015536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_015536.md) | commit UTC: 2026-11-15T01:55:55.000Z
- 원문 blob SHA: 8c454653a0e0a8c65b677334aac84ed9b0ea242b
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 최소 5년 또는 제품의 예상 사용 기간 동안 발견된 취약점에 대해 보안 업데이트를 무상으로 제공해야 합니다. 사용자(시스템 Integrator 및 공장 운영자)에게 취약점 처리 상태 및 패치 적용 방법에 대한 명확한 기술 정보를 사전에 고지하고 보장해야 합니다
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #25 — P1 — 산업용 서보 드라이브의 런타임 메모리 상에서 구동되는 모션 제어 파라미터 및 안전 기능(STO 등) 관련 펌웨어 영역에 대한 무단 변조를 방지하기 위해, 하드웨어 기반의 신뢰점(R
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:00:50 (원문 시간대 미표기)
- 원문: [commit 3381181b771e295a0487af638ba65be4129a4efd](https://github.com/useformotor3/ai-discord-bot/commit/3381181b771e295a0487af638ba65be4129a4efd) | [research_archive/2026-11-15_020050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_020050.md) | commit UTC: 2026-11-15T02:01:08.000Z
- 원문 blob SHA: 24da508f37072cde6c88423c83d55ef174621563
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브의 런타임 메모리 상에서 구동되는 모션 제어 파라미터 및 안전 기능(STO 등) 관련 펌웨어 영역에 대한 무단 변조를 방지하기 위해, 하드웨어 기반의 신뢰점(Root of Trust)과 연계된 실시간 런타임 무결성 검증 체계를 구축해야 합니다. CRA 부속서 I(Annex I)에 따라
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(e)–(f), Part II(2),(7): 기밀성·무결성 및 안전한 업데이트 배포 결과를 확인. Secure Boot/RoT/특정 알고리즘은 법령의 보편적 명시 구현수단이 아닌 설계 후보.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #26 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 이를 위해 구조화된 취약점 수신 및 처리 프로세스를 구축하고 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:05:32 (원문 시간대 미표기)
- 원문: [commit 7416bc5677a1e16920fe31d9a2cf16e5d077a075](https://github.com/useformotor3/ai-discord-bot/commit/7416bc5677a1e16920fe31d9a2cf16e5d077a075) | [research_archive/2026-11-15_020532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_020532.md) | commit UTC: 2026-11-15T02:05:47.000Z
- 원문 blob SHA: 4a769179790fad759db61e24e46aa9424490daf5
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 이를 위해 구조화된 취약점 수신 및 처리 프로세스를 구축하고 대외적으로 공표해야 합니다. 취약점 패치 및 보안 업데이트는 기능적 안전(Functional Safety, 예: IEC 615
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #27 — P0 — 산업용 서보 드라이브 제조사는 CRA 부속서 III(Class II 중요 제품)에 따라, 부팅 시부터 런타임까지 하드웨어 기반 신뢰점(Root of Trust)을 활용해 무단 소프
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:10:41 (원문 시간대 미표기)
- 원문: [commit dc740a13a93b5654a2e2e810d8cf7ebf0ef43e82](https://github.com/useformotor3/ai-discord-bot/commit/dc740a13a93b5654a2e2e810d8cf7ebf0ef43e82) | [research_archive/2026-11-15_021041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_021041.md) | commit UTC: 2026-11-15T02:10:58.000Z
- 원문 blob SHA: 2760393029da23aafdb610610d5b4882af9d2131
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA 부속서 III(Class II 중요 제품)에 따라, 부팅 시부터 런타임까지 하드웨어 기반 신뢰점(Root of Trust)을 활용해 무단 소프트웨어 수정을 원천 차단하고, 제조자 기본 설정(Secure by default) 상태에서 공격 표면을 최소화해야 합니다. 또
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 7 및 Annex III: Important Product Class I/II 여부는 제품 명칭만이 아니라 Annex III 범주와 core function으로 판정. 서보 드라이브라는 이유만으로 Class II/Notified Body를 단정하지 않음.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #28 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년 또는 법적 부합성 기간) 발견되는 모든 취약점에 대해 추가 비용 청구 없이(Free of charge
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:15:41 (원문 시간대 미표기)
- 원문: [commit 8ef02ddcd07784644a170bb903912ba3062e2730](https://github.com/useformotor3/ai-discord-bot/commit/8ef02ddcd07784644a170bb903912ba3062e2730) | [research_archive/2026-11-15_021541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_021541.md) | commit UTC: 2026-11-15T02:15:58.000Z
- 원문 blob SHA: 8ef79331f95c83d8f11d9fbc6f99fa501e0cd55a
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년 또는 법적 부합성 기간) 발견되는 모든 취약점에 대해 추가 비용 청구 없이(Free of charge) 보안 패치를 적시에 배포해야 합니다. 특히, 모션 컨트롤러와 서보 드라이브 간의 고속 실시간 통신 및 펌웨어 업데이트 과정
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #29 — P0 — 핵심 내용 1: EU CRA 제11조 및 Annex I에 따라, 산업용 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 보안 취약점을 자동으로 또는 사
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:20:40 (원문 시간대 미표기)
- 원문: [commit 2c0f11d8b41d6faa6cc96d630e2e5cac69635625](https://github.com/useformotor3/ai-discord-bot/commit/2c0f11d8b41d6faa6cc96d630e2e5cac69635625) | [research_archive/2026-11-15_022040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_022040.md) | commit UTC: 2026-11-15T02:20:57.000Z
- 원문 blob SHA: 1df355d52ee0253c19864a1e0c3f0ef9952a899c
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: EU CRA 제11조 및 Annex I에 따라, 산업용 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 보안 취약점을 자동으로 또는 사용자가 쉽게 접근할 수 있는 방식으로 무상(Free-of-charge)으로 패치해야 합니다. 핵심 내용 2: 특히 모션 컨트롤
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #30 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견되는 취약점을 무상으로(Free of charge) 적시에 패치해야 하며, 최소 5년 또는 제품의 예상 시장
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:25:27 (원문 시간대 미표기)
- 원문: [commit 14d8b51ad3c03f2291438c5229ba277bfd8c2b97](https://github.com/useformotor3/ai-discord-bot/commit/14d8b51ad3c03f2291438c5229ba277bfd8c2b97) | [research_archive/2026-11-15_022527.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_022527.md) | commit UTC: 2026-11-15T02:25:44.000Z
- 원문 blob SHA: 084ad05b6352a00dbfdec34e43fd598d068023e1
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견되는 취약점을 무상으로(Free of charge) 적시에 패치해야 하며, 최소 5년 또는 제품의 예상 시장 존속 기간 중 더 긴 기간 동안 보안 업데이트를 보장해야 합니다. 이를 위해 취약점 공개 수령을 위한 공지 프로세스, 자동화
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #31 — P0 — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 동안 발견되는 취약점에 대해 무상으로 보안 패치(Security Updates)를 제공하고, 취약점 공개 및 처
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:30:46 (원문 시간대 미표기)
- 원문: [commit 6273b1c2045998e8cf33a4f6c7285e0c81eed9ac](https://github.com/useformotor3/ai-discord-bot/commit/6273b1c2045998e8cf33a4f6c7285e0c81eed9ac) | [research_archive/2026-11-15_023046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_023046.md) | commit UTC: 2026-11-15T02:31:02.000Z
- 원문 blob SHA: f9f9b47c905c9991aa3ff664347bb1c55f2de2d0
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 동안 발견되는 취약점에 대해 무상으로 보안 패치(Security Updates)를 제공하고, 취약점 공개 및 처리 프로세스를 투명하게 이행해야 합니다. 이는 고중량·고출력 산업용 기기의 사이버 사고로 인한 물리적 재해 및 공장 가동 중단
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #32 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명 주기 동안(최소 5년 또는 법적 부합성 기간) 발견된 취약점을 무상으로 즉시 패치할 수 있는 취약점 관
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:35:35 (원문 시간대 미표기)
- 원문: [commit b26ebd648ebf97078e6b1bdfbdc04ecbc415493c](https://github.com/useformotor3/ai-discord-bot/commit/b26ebd648ebf97078e6b1bdfbdc04ecbc415493c) | [research_archive/2026-11-15_023535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_023535.md) | commit UTC: 2026-11-15T02:35:52.000Z
- 원문 blob SHA: 86cf13ec80518cb530054b3f7e980e759fb55108
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명 주기 동안(최소 5년 또는 법적 부합성 기간) 발견된 취약점을 무상으로 즉시 패치할 수 있는 취약점 관리 프로세스를 구축하고, 보안 업데이트 제공 사실을 사용자에게 투명하게 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #33 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견되는 취약점을 무상으로 즉시 패치할 수 있는 자동화된 공정과 보안 업데이트 배포 메커
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:40:39 (원문 시간대 미표기)
- 원문: [commit 3cb9cdcc0d36fcee4d8756725c63e909927ecd9a](https://github.com/useformotor3/ai-discord-bot/commit/3cb9cdcc0d36fcee4d8756725c63e909927ecd9a) | [research_archive/2026-11-15_024039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_024039.md) | commit UTC: 2026-11-15T02:40:55.000Z
- 원문 blob SHA: 82ca984ba04a9f7963bce29138d70704951be2b8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견되는 취약점을 무상으로 즉시 패치할 수 있는 자동화된 공정과 보안 업데이트 배포 메커니즘을 의무적으로 제공해야 합니다. 사용자가 보안 업데이트를 명확히 인지하고 안전하게 적용할 수 있도록 취약점 수명 주기 관리
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #34 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점과 인사이던트(Incident)를 정해진 법적 기한 내에 EU 관할 기관(CSIRCs network 및 EN
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:45:40 (원문 시간대 미표기)
- 원문: [commit 803952b8aee68dab2f734d8580d776a378f1e999](https://github.com/useformotor3/ai-discord-bot/commit/803952b8aee68dab2f734d8580d776a378f1e999) | [research_archive/2026-11-15_024540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_024540.md) | commit UTC: 2026-11-15T02:45:56.000Z
- 원문 blob SHA: 8eb772206cf865c85ed1f17c2cde63b89f4b7ec4
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점과 인사이던트(Incident)를 정해진 법적 기한 내에 EU 관할 기관(CSIRCs network 및 ENISA)에 자동으로 보고하고, 사용자에게 무상으로 보안 업데이트를 제공할 수 있는 체계를 갖추어야 합니다. 특히 산업용 실시간
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #35 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 대중과 당국에 투명하게 보고하기 위한 '조율된 취약점 disclosure 정책'을 수립해야 하며, 제품의 예상 수명 동
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:50:36 (원문 시간대 미표기)
- 원문: [commit d18f23eb6753e49802cea1487d16cac7e830cb4d](https://github.com/useformotor3/ai-discord-bot/commit/d18f23eb6753e49802cea1487d16cac7e830cb4d) | [research_archive/2026-11-15_025036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_025036.md) | commit UTC: 2026-11-15T02:50:53.000Z
- 원문 blob SHA: 5f71f8bfff6670ebfaef7ee65bec04e269200a53
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 대중과 당국에 투명하게 보고하기 위한 '조율된 취약점 disclosure 정책'을 수립해야 하며, 제품의 예상 수명 동안(최소 5년 또는 주요 사용 기간) 발견된 보안 취약점에 대한 무상 보안 업데이트(패치)를 제공해야 합니다. 이는 고출력 구
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #36 — P1 — 산업용 서보 드라이브는 실시간 제어 루프에서 사용되는 모터 튜닝 파라미터(PID 게인, 감속비, 전류/속도 제한 등)의 변조를 방지하기 위해 런타임 무결성 보호 및 안전 설정의 불
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 02:55:30 (원문 시간대 미표기)
- 원문: [commit ffcd54e3c9cf64e755b2dde15eba94b45c963b7f](https://github.com/useformotor3/ai-discord-bot/commit/ffcd54e3c9cf64e755b2dde15eba94b45c963b7f) | [research_archive/2026-11-15_025530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_025530.md) | commit UTC: 2026-11-15T02:55:46.000Z
- 원문 blob SHA: d4a2392921bc1f6f000bbd172e8f9a71d9f54941
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 실시간 제어 루프에서 사용되는 모터 튜닝 파라미터(PID 게인, 감속비, 전류/속도 제한 등)의 변조를 방지하기 위해 런타임 무결성 보호 및 안전 설정의 불법적 변경 차단 메커니즘을 갖추어야 합니다. 이는 규정에서 명시한 '사이버 보안 위험의 효과적인 완화' 및 '중요 디지털 제품
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(e)–(f), Part II(2),(7): 기밀성·무결성 및 안전한 업데이트 배포 결과를 확인. Secure Boot/RoT/특정 알고리즘은 법령의 보편적 명시 구현수단이 아닌 설계 후보.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #37 — P0 — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 주기 동안(최소 5년 또는 법적 요구 기간) 발견된 취약점을 무상으로 처리하고, 보안 업데이트를 적시에 배포할 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:01:01 (원문 시간대 미표기)
- 원문: [commit c7dc3eb9e7c33bf1a1b407da95b355cc8e914cb8](https://github.com/useformotor3/ai-discord-bot/commit/c7dc3eb9e7c33bf1a1b407da95b355cc8e914cb8) | [research_archive/2026-11-15_030101.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_030101.md) | commit UTC: 2026-11-15T03:01:19.000Z
- 원문 blob SHA: 0d8e756da8509f94d5c5576d96b32499d5679d24
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 주기 동안(최소 5년 또는 법적 요구 기간) 발견된 취약점을 무상으로 처리하고, 보안 업데이트를 적시에 배포할 수 있는 취약점 관리 프로세스를 구축해야 합니다. 또한, 자동화된 취약점 고지 및 패치 메커니즘을 기술 문서에 명시하고 이행해
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #38 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점을 지체 없이 수정(무상 보안 업데이트 제공)해야 하며, 특히 ENISA 및 국가별 CSIRT(Compute
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:05:37 (원문 시간대 미표기)
- 원문: [commit 8642fcc74ab5e6983231c311343094a57f378dec](https://github.com/useformotor3/ai-discord-bot/commit/8642fcc74ab5e6983231c311343094a57f378dec) | [research_archive/2026-11-15_030537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_030537.md) | commit UTC: 2026-11-15T03:05:53.000Z
- 원문 blob SHA: 712b8f917953734c6489797ac7be2f239252f904
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점을 지체 없이 수정(무상 보안 업데이트 제공)해야 하며, 특히 ENISA 및 국가별 CSIRT(Computer Security Incident Response Teams)와의 신속한 사고 및 취약점 통보 의무를 이행하기 위한 자동화된
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #39 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 발견된 취약점을 지체 없이 무료로 패치해야 하며, 제품의 예상 수명 동안(최소 5년) 보안 업데이트를 제공할 수 있는 취약점
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:10:40 (원문 시간대 미표기)
- 원문: [commit edb9aba3f3a65670546fd71b6a2b1772c00b7b0e](https://github.com/useformotor3/ai-discord-bot/commit/edb9aba3f3a65670546fd71b6a2b1772c00b7b0e) | [research_archive/2026-11-15_031040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_031040.md) | commit UTC: 2026-11-15T03:10:57.000Z
- 원문 blob SHA: 703abae44d4546f66a06cd4df09c4ca9e44f6bec
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 발견된 취약점을 지체 없이 무료로 패치해야 하며, 제품의 예상 수명 동안(최소 5년) 보안 업데이트를 제공할 수 있는 취약점 처리 프로세스를 구축·유지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #40 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 무상으로 적시에 패치해야 하며, 최소 5년 또는 제품의 예상 수명 동안 안전한 소프트웨어 업데이트를 제공할 수 있는 생
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:15:39 (원문 시간대 미표기)
- 원문: [commit 6141952b144a1d74465d30054b2a3e1b8ec8a94a](https://github.com/useformotor3/ai-discord-bot/commit/6141952b144a1d74465d30054b2a3e1b8ec8a94a) | [research_archive/2026-11-15_031539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_031539.md) | commit UTC: 2026-11-15T03:15:55.000Z
- 원문 blob SHA: 04f10240d16c1b3109df809d330f20048e915fdf
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 무상으로 적시에 패치해야 하며, 최소 5년 또는 제품의 예상 수명 동안 안전한 소프트웨어 업데이트를 제공할 수 있는 생명주기 관리 체계를 갖추어야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #41 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 최소 5년의 제품 예상 수명 동안 보안 취약점을 무상으로 패치해야 하며, 발견된 취약점은 규정된 기한 내에 관할 기관 및 사용자에게 투
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:20:42 (원문 시간대 미표기)
- 원문: [commit b09a0153b67f1dcc8da8ef4909107cdedf90477c](https://github.com/useformotor3/ai-discord-bot/commit/b09a0153b67f1dcc8da8ef4909107cdedf90477c) | [research_archive/2026-11-15_032042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_032042.md) | commit UTC: 2026-11-15T03:20:58.000Z
- 원문 blob SHA: 8c8d81e71ca58c05a0c5667875e3ba1c21951f3a
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 최소 5년의 제품 예상 수명 동안 보안 취약점을 무상으로 패치해야 하며, 발견된 취약점은 규정된 기한 내에 관할 기관 및 사용자에게 투명하게 공지하고 조치해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #42 — P0 — 산업용 서보 드라이브는 출하 시점부터 무단 접근을 방지하기 위해 보안이 설정된 상태(Secure by Default)로 제공되어야 하며, 초기 구동 시 고유한 기본 비밀번호 변경이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:25:33 (원문 시간대 미표기)
- 원문: [commit 54214f1c27861db3057e9701e1da0729aa2e3d40](https://github.com/useformotor3/ai-discord-bot/commit/54214f1c27861db3057e9701e1da0729aa2e3d40) | [research_archive/2026-11-15_032533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_032533.md) | commit UTC: 2026-11-15T03:25:50.000Z
- 원문 blob SHA: 915dd2e7ac4044caeb2ddc8e1cd0cd16bfb67c71
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출하 시점부터 무단 접근을 방지하기 위해 보안이 설정된 상태(Secure by Default)로 제공되어야 하며, 초기 구동 시 고유한 기본 비밀번호 변경이나 명시적인 보안 프로파일 활성화를 강제해야 합니다. 또한, 제조사는 제품의 예상 수명 주기 동안 보안 업데이트가 기본적으로
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #43 — P0 — 산업용 서보 드라이브 제조사는 CRA 부속서 I에 따라 발견된 취약점과 보안 공지를 사용자에게 지체 없이 무료로 제공해야 하며, 펌웨어 및 보안 업데이트가 배포될 때 무결성이 검증
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:30:50 (원문 시간대 미표기)
- 원문: [commit bf774c432c74c1af0bcb50177928c696d69bb428](https://github.com/useformotor3/ai-discord-bot/commit/bf774c432c74c1af0bcb50177928c696d69bb428) | [research_archive/2026-11-15_033050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_033050.md) | commit UTC: 2026-11-15T03:31:06.000Z
- 원문 blob SHA: cc5f8b14a6a8df8b8e0641177d3986927cbc2699
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA 부속서 I에 따라 발견된 취약점과 보안 공지를 사용자에게 지체 없이 무료로 제공해야 하며, 펌웨어 및 보안 업데이트가 배포될 때 무결성이 검증되고 안전하게 적용될 수 있는 자동화된 메커니즘을 지원해야 합니다. 이는 공장 자동화 환경에서 예기치 않은 가동 중단(Down
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #44 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 추가 비용(무상) 없이 적시에 패치하고 업데이트할 법적 의무를 집니다. 보안 업데이트 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:38:12 (원문 시간대 미표기)
- 원문: [commit 46e5d2ebabe1fe3c9c4c7318db36914966be19e1](https://github.com/useformotor3/ai-discord-bot/commit/46e5d2ebabe1fe3c9c4c7318db36914966be19e1) | [research_archive/2026-11-15_033812.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_033812.md) | commit UTC: 2026-11-15T03:38:28.000Z
- 원문 blob SHA: c142117b85891b346b6b6e25e5812795b3db5e07
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 추가 비용(무상) 없이 적시에 패치하고 업데이트할 법적 의무를 집니다. 보안 업데이트 가용성에 대해 최종 사용자에게 명확하고 이해하기 쉬운 방식으로 지연 없이 통지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #45 — P1 — 산업용 서보 드라이브는 초기 출고 시부터 무단 접근을 방지하는 안전한 기본 상태(Secure by default)로 설정되어야 하며, 사용자가 첫 설치 시 보안 파라미터를 강제로 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:40:37 (원문 시간대 미표기)
- 원문: [commit 4d5d2f4af108dfc4564fbd23a0de28a0b6a8eba8](https://github.com/useformotor3/ai-discord-bot/commit/4d5d2f4af108dfc4564fbd23a0de28a0b6a8eba8) | [research_archive/2026-11-15_034037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_034037.md) | commit UTC: 2026-11-15T03:40:54.000Z
- 원문 blob SHA: 0c53f9aa59709cf6b1d9f0c6be3f6fdeff6ef8c7
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시부터 무단 접근을 방지하는 안전한 기본 상태(Secure by default)로 설정되어야 하며, 사용자가 첫 설치 시 보안 파라미터를 강제로 변경하도록 유도하는 메커니즘을 갖추어야 합니다. 또한, 이러한 기본 보안 설정의 기술적 근거와 구성 내역은 평가 및 규정 준수
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #46 — P1 — 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 기능, 인터페이스, 서비스가 비활성화된 상태로 제공되어야 하며(Secure by Default), 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:45:39 (원문 시간대 미표기)
- 원문: [commit f399003eaf30f7d5992b19fb507b0b216f6862be](https://github.com/useformotor3/ai-discord-bot/commit/f399003eaf30f7d5992b19fb507b0b216f6862be) | [research_archive/2026-11-15_034539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_034539.md) | commit UTC: 2026-11-15T03:45:55.000Z
- 원문 blob SHA: 916c181d2facb3994674caba97650f11afc7b4a3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 기능, 인터페이스, 서비스가 비활성화된 상태로 제공되어야 하며(Secure by Default), 사용자가 보안 설정을 강제하거나 안전한 초기 인증 체계를 구축할 수 있도록 설계되어야 합니다. 이는 CRA Annex I에 명
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #47 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점에 대해 최소한 제품의 예상 수명 기간 동안(최소 5년) 보안 업데이트를 무상으로 제공해야 하며, 사용자가 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:50:34 (원문 시간대 미표기)
- 원문: [commit abd24d79c19150c2abb4d050c4525d2173dabc5b](https://github.com/useformotor3/ai-discord-bot/commit/abd24d79c19150c2abb4d050c4525d2173dabc5b) | [research_archive/2026-11-15_035034.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_035034.md) | commit UTC: 2026-11-15T03:50:50.000Z
- 원문 blob SHA: d3c759f8a85ee27377e06d6840fa931097a96cfb
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점에 대해 최소한 제품의 예상 수명 기간 동안(최소 5년) 보안 업데이트를 무상으로 제공해야 하며, 사용자가 이를 쉽게 인지하고 적용할 수 있도록 자동화된 업데이트 알림 및 배포 메커니즘을 구현해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #48 — P0 — 산업용 서보 드라이브 제조사는 제품에 악영향을 미치는 취약점이나 보안 사고를 인지한 즉시(규정된 시간 내에) ENISA 및 관련 관할 시장 감시 당국에 자동으로 신고할 수 있는 체
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 03:55:36 (원문 시간대 미표기)
- 원문: [commit 00de4c81a6b03412e1b4cc550a5d982e34500c54](https://github.com/useformotor3/ai-discord-bot/commit/00de4c81a6b03412e1b4cc550a5d982e34500c54) | [research_archive/2026-11-15_035536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_035536.md) | commit UTC: 2026-11-15T03:55:52.000Z
- 원문 blob SHA: 95959185b2aab739ffe921871cb848b9879290f7
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품에 악영향을 미치는 취약점이나 보안 사고를 인지한 즉시(규정된 시간 내에) ENISA 및 관련 관할 시장 감시 당국에 자동으로 신고할 수 있는 체계를 갖추어야 합니다. 또한, 인지된 취약점에 대해 무상으로 보안 업데이트(패치)를 배포하고, 이를 사용자에게 명확히 고지할
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #49 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 보안 비용 청구 없이 무상으로(Free of charge) 적시에 패치해야 하며, 제품의 예상 수명 또는 최소 5년 중
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:00:53 (원문 시간대 미표기)
- 원문: [commit f41a4c1bdf0c5ec0727e37c61c97e8abd879e4c1](https://github.com/useformotor3/ai-discord-bot/commit/f41a4c1bdf0c5ec0727e37c61c97e8abd879e4c1) | [research_archive/2026-11-15_040053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_040053.md) | commit UTC: 2026-11-15T04:01:11.000Z
- 원문 blob SHA: 35a4cfe0af5c07d399d241392c43b403353a088e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 보안 비용 청구 없이 무상으로(Free of charge) 적시에 패치해야 하며, 제품의 예상 수명 또는 최소 5년 중 긴 기간 동안 지원(Support period)을 보장해야 합니다. 자동화된 보안 업데이트 메커니즘을 제공하되, 사용자가 이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #50 — P0 — 서보 드라이브 제조사는 발견된 취약점에 대응하기 위해 보안 업데이트(패치)를 사용자가 안전하고 쉽게 적용할 수 있도록 무상으로 제공해야 하며, 중요 취약점 및 활성 악용 사례 발생
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:05:34 (원문 시간대 미표기)
- 원문: [commit cffd593a6e6a2e7b65e5484c05c3d904157ae416](https://github.com/useformotor3/ai-discord-bot/commit/cffd593a6e6a2e7b65e5484c05c3d904157ae416) | [research_archive/2026-11-15_040534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_040534.md) | commit UTC: 2026-11-15T04:05:51.000Z
- 원문 blob SHA: a0d9d05d5b9be16510136d95b7193c6a2c302b08
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 발견된 취약점에 대응하기 위해 보안 업데이트(패치)를 사용자가 안전하고 쉽게 적용할 수 있도록 무상으로 제공해야 하며, 중요 취약점 및 활성 악용 사례 발생 시 규제 기관(ENISA) 및 사용자에게 정해진 법정 기한 내에 의무적으로 통지해야 합니다. 자동화된 업데이트 메커니즘을 지
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #51 — P0 — 핵심 내용 1: 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패치
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:10:35 (원문 시간대 미표기)
- 원문: [commit 2145488bdcb556b95da0b5d3775c183f9398a99f](https://github.com/useformotor3/ai-discord-bot/commit/2145488bdcb556b95da0b5d3775c183f9398a99f) | [research_archive/2026-11-15_041035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_041035.md) | commit UTC: 2026-11-15T04:10:52.000Z
- 원문 blob SHA: 2bedfbf97a54baa0998a400ccdcd92c5b07aa570
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패치를 제공해야 합니다. 핵심 내용 2: 보안 업데이트는 사용자에게 안전하게 배포될 수 있도록 디지털 서명 등의 무결성 메커니즘을
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #52 — P1 — 산업용 서보 드라이브는 출고 시 보안이 취약한 기능이나 불필요한 인터페이스가 활성화되어 있지 않도록 가장 안전한 기본 설정(Secure by default) 상태로 제공되어야 하며
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:15:40 (원문 시간대 미표기)
- 원문: [commit 6306286b2ffed4b6f8603e1e1ba55457d24f3374](https://github.com/useformotor3/ai-discord-bot/commit/6306286b2ffed4b6f8603e1e1ba55457d24f3374) | [research_archive/2026-11-15_041540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_041540.md) | commit UTC: 2026-11-15T04:15:56.000Z
- 원문 blob SHA: e16fd6f444e1cf471a395000d3bbfb1bc34d2a47
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시 보안이 취약한 기능이나 불필요한 인터페이스가 활성화되어 있지 않도록 가장 안전한 기본 설정(Secure by default) 상태로 제공되어야 하며, 사용자가 명시적으로 변경하기 전까지 이 상태가 유지되어야 합니다. 또한, 제품과 함께 제공되는 모든 초기 설정 및 자격 증
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #53 — P0 — 산업용 서보 드라이브는 CRA Annex III(Class II)에 해당하는 중요 디지털 제품으로 분류되어, 제조사 자체 선언(Self-assessment)이 불가하며 공인 기관(
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:20:39 (원문 시간대 미표기)
- 원문: [commit 3b11fc1217a6afd8cab8a82a54530b53804d47ec](https://github.com/useformotor3/ai-discord-bot/commit/3b11fc1217a6afd8cab8a82a54530b53804d47ec) | [research_archive/2026-11-15_042039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_042039.md) | commit UTC: 2026-11-15T04:20:55.000Z
- 원문 blob SHA: ca3c42f126435f99148cb7306f040e28371d1d09
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 CRA Annex III(Class II)에 해당하는 중요 디지털 제품으로 분류되어, 제조사 자체 선언(Self-assessment)이 불가하며 공인 기관(Notified Body)의 개입이 필수적인 제3자 적합성 평가 절차를 거쳐야 합니다. 제조사는 설계 및 생산 단계 전반에 걸
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(17)–(19), Annex II(1)–(9): 사용자 정보·지침은 Article 13(18), 종료일 표시는 13(19), Annex II point 8(a)–(f); SBOM 사용자 접근은 point 9 조건부.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #54 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 또는 법적 의무 기간) 발견된 보안 취약점에 대한 패치를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 제조사
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:25:39 (원문 시간대 미표기)
- 원문: [commit 651d6fa27af847260e761b9707e51db4baf51e59](https://github.com/useformotor3/ai-discord-bot/commit/651d6fa27af847260e761b9707e51db4baf51e59) | [research_archive/2026-11-15_042539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_042539.md) | commit UTC: 2026-11-15T04:25:54.000Z
- 원문 blob SHA: e44260546076d98cee6616e583eb17ae94d284ea
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 또는 법적 의무 기간) 발견된 보안 취약점에 대한 패치를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 제조사는 제3자가 보안 취약점을 안전하게 신고할 수 있는 취약점 조정 공표(Coordinated Vulnerability Discl
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #55 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 대중과 당국에 투명하게 공개하고, 보안 업데이트를 무상으로 제공해야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:30:51 (원문 시간대 미표기)
- 원문: [commit 3150b794abfe83452b1fd1fd5d238b90ab3b9b70](https://github.com/useformotor3/ai-discord-bot/commit/3150b794abfe83452b1fd1fd5d238b90ab3b9b70) | [research_archive/2026-11-15_043051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_043051.md) | commit UTC: 2026-11-15T04:31:05.000Z
- 원문 blob SHA: 46c6ec0535e9c75e2b19c71bc6d91e1615209ceb
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 대중과 당국에 투명하게 공개하고, 보안 업데이트를 무상으로 제공해야 합니다. 또한, 제3자 연구자 등이 취약점을 안전하게 신고할 수 있는 명확한 창구와 정책을 수립·운영해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #56 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 사용자에게 자동으로 보안 업데이트 알림을 제공하고, 이를 추가 비용 없이 무상으로 배포해야 합
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:35:34 (원문 시간대 미표기)
- 원문: [commit 72e186b7667c50089b9b24fc949fb3720e130b48](https://github.com/useformotor3/ai-discord-bot/commit/72e186b7667c50089b9b24fc949fb3720e130b48) | [research_archive/2026-11-15_043534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_043534.md) | commit UTC: 2026-11-15T04:35:50.000Z
- 원문 blob SHA: 3a36c6759fc642ca3540c97ba5848d409f63c0b2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 사용자에게 자동으로 보안 업데이트 알림을 제공하고, 이를 추가 비용 없이 무상으로 배포해야 합니다. 제조 과정에서부터 기본 설정(Secure by default)된 상태로 출하되어야 하며, 악의적 취약점 악용을 방지하기
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #57 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 기본적으로 안전한 설정(Secure by Default) 상태여야 하며, 사용자가 초기 전원을
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:40:45 (원문 시간대 미표기)
- 원문: [commit 83582a5373d9d29927207700806b3ee2b2c1a9e6](https://github.com/useformotor3/ai-discord-bot/commit/83582a5373d9d29927207700806b3ee2b2c1a9e6) | [research_archive/2026-11-15_044045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_044045.md) | commit UTC: 2026-11-15T04:41:01.000Z
- 원문 blob SHA: 3a77af162020129896aa24a2baf83d8d8cc3eb80
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 기본적으로 안전한 설정(Secure by Default) 상태여야 하며, 사용자가 초기 전원을 켤 때 고유하거나 변경 가능한 강력한 기본 인증 정보를 강제하도록 설계되어야 합니다. 또한, 제조사는 제품의 예상 수명 주기
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #58 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근을 방지하기 위해 보안이 강화된 초기 상태(Secure by default)로 설정해야 하며, 특히 변경 가능한 기본 인증
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:45:38 (원문 시간대 미표기)
- 원문: [commit 694a7b520896970aeaea96e842c67a2d2b460744](https://github.com/useformotor3/ai-discord-bot/commit/694a7b520896970aeaea96e842c67a2d2b460744) | [research_archive/2026-11-15_044538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_044538.md) | commit UTC: 2026-11-15T04:45:54.000Z
- 원문 blob SHA: e4fb2e66e3c9b2a8a6b148dca4b49238ceb81405
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근을 방지하기 위해 보안이 강화된 초기 상태(Secure by default)로 설정해야 하며, 특히 변경 가능한 기본 인증 정보(Default passwords)나 불필요하게 활성화된 인터페이스 및 서비스가 없도록 보장해야 합니다. 이는 사용자가
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #59 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안 식별된 취약점에 대한 보안 업데이트를 추가 비용(무상) 없이 제공해야 합니다. 또한, 취약점 수정 및 보안
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:50:39 (원문 시간대 미표기)
- 원문: [commit 1bf14b8c290e83c2f469af6f16954ea693c33221](https://github.com/useformotor3/ai-discord-bot/commit/1bf14b8c290e83c2f469af6f16954ea693c33221) | [research_archive/2026-11-15_045039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_045039.md) | commit UTC: 2026-11-15T04:50:56.000Z
- 원문 blob SHA: 2b557cf172ad495be731327cd8dcc4f1099b124a
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안 식별된 취약점에 대한 보안 업데이트를 추가 비용(무상) 없이 제공해야 합니다. 또한, 취약점 수정 및 보안 업데이트가 배포될 때까지 임시 조치(Workaround)를 포함한 보안 권고를 지체 없이 공개해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #60 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 제공해야 합니다. 사용자가 보안 업데
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 04:55:35 (원문 시간대 미표기)
- 원문: [commit 36b9442126cd80689a00edf4d5e5ae9f07215cb3](https://github.com/useformotor3/ai-discord-bot/commit/36b9442126cd80689a00edf4d5e5ae9f07215cb3) | [research_archive/2026-11-15_045535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_045535.md) | commit UTC: 2026-11-15T04:55:50.000Z
- 원문 blob SHA: 96fe5191dee121ba545be8764edce4bc6a0b0f68
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 제공해야 합니다. 사용자가 보안 업데이트를 자동 또는 수동으로 안전하게 적용할 수 있는 메커니즘을 지원하고, 취약점 수정 정보와 함께 관련 보안 권고(Securi
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #61 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근을 방지하기 위해 안전한 기본 설정(Secure by Default)으로 구성되어야 하며, 특히 기본으로 설정된 고유 비밀
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:01:02 (원문 시간대 미표기)
- 원문: [commit 879d1be1552bee595edf030b6f63c03c4f94e367](https://github.com/useformotor3/ai-discord-bot/commit/879d1be1552bee595edf030b6f63c03c4f94e367) | [research_archive/2026-11-15_050102.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_050102.md) | commit UTC: 2026-11-15T05:01:19.000Z
- 원문 blob SHA: 6856c574d25801f58ed8581f6808bc314ae800fb
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근을 방지하기 위해 안전한 기본 설정(Secure by Default)으로 구성되어야 하며, 특히 기본으로 설정된 고유 비밀번호의 강제 변경 유도 또는 미리 설치된 기본 인증 정보의 무단 악용 방지 조치를 반드시 적용해야 합니다. 사용자가 제품을 최
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #62 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 수정하고 보안 업데이트를 제공해야 합니다. 업데이트 제공 시 디지털 서명 기반의
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:05:29 (원문 시간대 미표기)
- 원문: [commit ff3122f77066e868db605c76974a11fee901deba](https://github.com/useformotor3/ai-discord-bot/commit/ff3122f77066e868db605c76974a11fee901deba) | [research_archive/2026-11-15_050529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_050529.md) | commit UTC: 2026-11-15T05:05:45.000Z
- 원문 blob SHA: e7505c61b16e0b9d5e7c0c8d13360f7d13042d82
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 수정하고 보안 업데이트를 제공해야 합니다. 업데이트 제공 시 디지털 서명 기반의 안전한 메커니즘을 적용하여 배포 과정에서의 위변조를 원천 차단해야 합니다. --
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #63 — P1 — 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 네트워크 악용을 방지하기 위해 불필요한 서비스와 포트가 비활성화된 'Secure by default' 상태여야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:10:39 (원문 시간대 미표기)
- 원문: [commit 2ff5cd51161207c2baf5f8ce33765834cc70c792](https://github.com/useformotor3/ai-discord-bot/commit/2ff5cd51161207c2baf5f8ce33765834cc70c792) | [research_archive/2026-11-15_051039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_051039.md) | commit UTC: 2026-11-15T05:10:56.000Z
- 원문 blob SHA: b2a02a561e2faa5e47d632759d7b611ab517230d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 네트워크 악용을 방지하기 위해 불필요한 서비스와 포트가 비활성화된 'Secure by default' 상태여야 합니다. 관리자 계정의 초기 비밀번호는 고정값이 아닌 고유하게 생성되거나 최초 부팅 시 사용자의 강제 변경을 유도하는 메커니즘을
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #64 — P1 — 서보 드라이브 제조사는 제품 출하 시 무단 접근과 공격 면적(Attack Surface)을 최소화하기 위해 기본적으로 안전한 상태(Secure by Default)로 설정해야 하며
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:15:36 (원문 시간대 미표기)
- 원문: [commit c01d82b992477b0a771782dec76650792970e0f4](https://github.com/useformotor3/ai-discord-bot/commit/c01d82b992477b0a771782dec76650792970e0f4) | [research_archive/2026-11-15_051536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_051536.md) | commit UTC: 2026-11-15T05:15:53.000Z
- 원문 blob SHA: 8a93d3712534f7bf85d523ad9b24457e60fc79cd
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출하 시 무단 접근과 공격 면적(Attack Surface)을 최소화하기 위해 기본적으로 안전한 상태(Secure by Default)로 설정해야 하며, 불필요한 기능, 인터페이스, 서비스는 기본적으로 비활성화되어야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #65 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대한 보안 업데이트(패치)를 추가 비용 없이 사용자에게 제공해야 합니다. 취약점 및 그 처리 과정에 대한 투명성
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:20:46 (원문 시간대 미표기)
- 원문: [commit 8e2092e63df9e813eeb321220d176911134ecc6a](https://github.com/useformotor3/ai-discord-bot/commit/8e2092e63df9e813eeb321220d176911134ecc6a) | [research_archive/2026-11-15_052046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_052046.md) | commit UTC: 2026-11-15T05:21:06.000Z
- 원문 blob SHA: 51f376fb57d7a36e70d713be8c6a2dec56e59bd2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대한 보안 업데이트(패치)를 추가 비용 없이 사용자에게 제공해야 합니다. 취약점 및 그 처리 과정에 대한 투명성을 확보하기 위해 조정된 취약점 공개(Coordinated Vulnerability Disclosure) 정책을 수립하고 이행
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #66 — P1 — 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 사용자 인증 정보나 네트워크 인터페이스 등에서 가장 엄격한 보안 수준을 기본값
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:25:30 (원문 시간대 미표기)
- 원문: [commit 8106d91705434a2104bdf3f5cb35bd578066918b](https://github.com/useformotor3/ai-discord-bot/commit/8106d91705434a2104bdf3f5cb35bd578066918b) | [research_archive/2026-11-15_052530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_052530.md) | commit UTC: 2026-11-15T05:25:52.000Z
- 원문 blob SHA: 5178ae4e22d2ca6f8fc31495942b3e27596d29ce
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 사용자 인증 정보나 네트워크 인터페이스 등에서 가장 엄격한 보안 수준을 기본값(Secure by default)으로 설정하여 공급되어야 합니다. 핵심 내용 2: 제품의 수명주기 동안 보안 사고 발생 시
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #67 — P1 — 산업용 서보 드라이브는 초기 출고 시부터 무단 접근을 방지하는 안전한 기본 설정(Secure by Default) 상태여야 하며, 이를 위해 인증되지 않은 네트워크 및 로컬 인터페
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:30:38 (원문 시간대 미표기)
- 원문: [commit 0f958103a108ba2b68658afba739e51ce0cbaac4](https://github.com/useformotor3/ai-discord-bot/commit/0f958103a108ba2b68658afba739e51ce0cbaac4) | [research_archive/2026-11-15_053038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_053038.md) | commit UTC: 2026-11-15T05:30:54.000Z
- 원문 blob SHA: bdf7afc1d7a9379911c929145423d0fc74185e8a
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시부터 무단 접근을 방지하는 안전한 기본 설정(Secure by Default) 상태여야 하며, 이를 위해 인증되지 않은 네트워크 및 로컬 인터페이스를 차단하고 강력한 기본 사용자 인증 메커니즘을 강제해야 합니다. 또한, 사용자가 보안 설정을 변경할 수 있는 직관적인 수
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #68 — P0 — 제조사는 서보 드라이브의 예상 수명 주기(또는 최소 5년 중 긴 기간) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 패치 및 업데이트를 적시에
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:35:35 (원문 시간대 미표기)
- 원문: [commit 56aef65384883289a23e2b585d1d4bcfa221f75e](https://github.com/useformotor3/ai-discord-bot/commit/56aef65384883289a23e2b585d1d4bcfa221f75e) | [research_archive/2026-11-15_053535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_053535.md) | commit UTC: 2026-11-15T05:35:53.000Z
- 원문 blob SHA: 25fe712a2ea07ce9158e2ef8741f4d6935900bc9
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 서보 드라이브의 예상 수명 주기(또는 최소 5년 중 긴 기간) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 패치 및 업데이트를 적시에 배포해야 하며, 이를 위한 취약점 처리 공정(Vulnerability handling process)을 유지해야 합니다. 이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #69 — P0 — 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 보안 업데이트 및 패치를 사용자에게 안전하고 적시에 제공할 수 있는 기술적 체계를 갖추
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:40:44 (원문 시간대 미표기)
- 원문: [commit d932335c8e311beadc3c2a9d0f9c40c4bedcb882](https://github.com/useformotor3/ai-discord-bot/commit/d932335c8e311beadc3c2a9d0f9c40c4bedcb882) | [research_archive/2026-11-15_054044.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_054044.md) | commit UTC: 2026-11-15T05:40:59.000Z
- 원문 blob SHA: 54807812020bed2f0cae10a2130a4bc025eaea06
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 보안 업데이트 및 패치를 사용자에게 안전하고 적시에 제공할 수 있는 기술적 체계를 갖추어야 합니다. 이는 CRA Annex I(필수 사이버 보안 요구사항)에 근거하며, 제조사가 제품 판매 이후에도 전체 수명주기(
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #70 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(무상으로) 제공해야 합니다. 제조사는 취약점 처리 프로세
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:45:34 (원문 시간대 미표기)
- 원문: [commit 8e592f8607fd804ff717ac86e7efc5246971f351](https://github.com/useformotor3/ai-discord-bot/commit/8e592f8607fd804ff717ac86e7efc5246971f351) | [research_archive/2026-11-15_054534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_054534.md) | commit UTC: 2026-11-15T05:45:50.000Z
- 원문 blob SHA: bf0483259062144ca544a8052cbf97ecc9803a18
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(무상으로) 제공해야 합니다. 제조사는 취약점 처리 프로세스 및 보안 업데이트 가용성에 대한 정보를 명확하고 이해하기 쉬운 형태로 사용자에게 공개해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #71 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(수정 패치)를 제공해야 하며, 이를 위해 취약점 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:50:40 (원문 시간대 미표기)
- 원문: [commit 3e63c8fcb406e25131ad6130d2739cd33e08fae4](https://github.com/useformotor3/ai-discord-bot/commit/3e63c8fcb406e25131ad6130d2739cd33e08fae4) | [research_archive/2026-11-15_055040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_055040.md) | commit UTC: 2026-11-15T05:50:56.000Z
- 원문 blob SHA: 046a62ea6b85a3b158465ae1148f4aa4092b3b5f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(수정 패치)를 제공해야 하며, 이를 위해 취약점 공개 및 처리 정책을 수립하고 이행해야 합니다. 이는 산업 현장의 시스템 중단을 방지하고 지속적인 가용성을 보장하기 위한 필수
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #72 — P1 — 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 변경 가능한 기본 사용자 인증 정보나 사전 설정된 약한 비밀번호를 포함하지 않도록 안전한 기본 설정(Se
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 05:55:33 (원문 시간대 미표기)
- 원문: [commit ca62022f1d2342c80292dd74ba2d09f45aacd32b](https://github.com/useformotor3/ai-discord-bot/commit/ca62022f1d2342c80292dd74ba2d09f45aacd32b) | [research_archive/2026-11-15_055533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_055533.md) | commit UTC: 2026-11-15T05:55:51.000Z
- 원문 blob SHA: cf00bcf95da83f060ee0fbe96e1458a3e58aab37
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 변경 가능한 기본 사용자 인증 정보나 사전 설정된 약한 비밀번호를 포함하지 않도록 안전한 기본 설정(Secure by default) 상태로 제공되어야 합니다. 핵심 내용 2: 제품의 초기 구동 또는 첫 번째 사용 시점에 사용자가
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #73 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(Support Period) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:00:52 (원문 시간대 미표기)
- 원문: [commit f7e823499a1b1380cde7f8ff73f59168dd78d732](https://github.com/useformotor3/ai-discord-bot/commit/f7e823499a1b1380cde7f8ff73f59168dd78d732) | [research_archive/2026-11-15_060052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_060052.md) | commit UTC: 2026-11-15T06:01:08.000Z
- 원문 blob SHA: 93864b19a7d4a2cde1305c57d947e36d7fddad0e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(Support Period) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패치를 제공해야 합니다. 해당 보안 업데이트는 기능적 업데이트와 엄격히 분리되어야 하며, 공표 즉시 사용 가능하도록 안전한 메커
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #74 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Updates)를 지체 없이(Without un
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:05:36 (원문 시간대 미표기)
- 원문: [commit 248cbf94b8042e5b659af68feba50efceff89901](https://github.com/useformotor3/ai-discord-bot/commit/248cbf94b8042e5b659af68feba50efceff89901) | [research_archive/2026-11-15_060536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_060536.md) | commit UTC: 2026-11-15T06:05:51.000Z
- 원문 blob SHA: 57d49f8e8c04244a7e739cc23b4521ae70569fd2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Updates)를 지체 없이(Without undue delay) 제공해야 합니다. 사용자가 보안 패치를 쉽게 적용할 수 있도록 자동화되거나 사용자 친화적인 알림 및 배포
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #75 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년 또는 법적 지원 기간) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:10:38 (원문 시간대 미표기)
- 원문: [commit dea9aad65bedc3eb4c619c02f87e36d353fce36d](https://github.com/useformotor3/ai-discord-bot/commit/dea9aad65bedc3eb4c619c02f87e36d353fce36d) | [research_archive/2026-11-15_061038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_061038.md) | commit UTC: 2026-11-15T06:11:06.000Z
- 원문 blob SHA: 8260b2ec4db83e836e266b6b6a008976b7b215ab
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년 또는 법적 지원 기간) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 자동화 시스템의 가용성(Availability)과 안전성을 보장하기 위해, 보안 패치의 적용이 기존 실시간 제어 성능이나
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #76 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 안전하고 제한된 기본 설정(Secure by default) 상태여야 하며, 취약한 기본 비밀번호나 불필요하게 활성화된 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:15:39 (원문 시간대 미표기)
- 원문: [commit 46b4b90384bc3a64ff8ca7191bb99d1680a8980b](https://github.com/useformotor3/ai-discord-bot/commit/46b4b90384bc3a64ff8ca7191bb99d1680a8980b) | [research_archive/2026-11-15_061539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_061539.md) | commit UTC: 2026-11-15T06:16:15.000Z
- 원문 blob SHA: 4d70feb22d24478ff78c82981eab0f2c3b2ec979
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 안전하고 제한된 기본 설정(Secure by default) 상태여야 하며, 취약한 기본 비밀번호나 불필요하게 활성화된 네트워크 포트 및 서비스가 원천 차단되어야 합니다. 또한, 최초 인증 시 사용자가 고유한 비밀번호를 강제로 설정하도록 설계되어
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #77 — P0 — 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 초기 상태(Secure by default)로 설정되어야 하며, 사용자에게 안전하지 않은 기본 암호나 불필요하게 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:20:39 (원문 시간대 미표기)
- 원문: [commit b881a2be37b6731b83a888828bfee28c8d236306](https://github.com/useformotor3/ai-discord-bot/commit/b881a2be37b6731b83a888828bfee28c8d236306) | [research_archive/2026-11-15_062039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_062039.md) | commit UTC: 2026-11-15T06:21:00.000Z
- 원문 blob SHA: 380a3e3317457b6856c22349d66ddd7cba253061
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 초기 상태(Secure by default)로 설정되어야 하며, 사용자에게 안전하지 않은 기본 암호나 불필요하게 활성화된 포트/서비스가 없는 상태로 제공되어야 합니다. 또한, 제조사는 제품 수명주기 동안 식별된 취약점을 무상으로 신속하게
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #78 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 또는 법적 부합성이 요구되는 기간) 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Update
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:25:29 (원문 시간대 미표기)
- 원문: [commit cc825e6c7e9f31dd1ddfbb9a9230cfbb9435b3cc](https://github.com/useformotor3/ai-discord-bot/commit/cc825e6c7e9f31dd1ddfbb9a9230cfbb9435b3cc) | [research_archive/2026-11-15_062529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_062529.md) | commit UTC: 2026-11-15T06:25:45.000Z
- 원문 blob SHA: 82daad21cf222f3530cbf75e7678a6116f167ba3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 또는 법적 부합성이 요구되는 기간) 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Updates)를 지체 없이 제공해야 합니다. 또한, 사용자에게 취약점 처리 상태를 투명하게 고지하고 안전한 업데이트 메커니즘을 보장해야
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #79 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 또한, 취약점 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:30:50 (원문 시간대 미표기)
- 원문: [commit aa6704b33586f1a3c2dd5e88151e7761822d05df](https://github.com/useformotor3/ai-discord-bot/commit/aa6704b33586f1a3c2dd5e88151e7761822d05df) | [research_archive/2026-11-15_063050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_063050.md) | commit UTC: 2026-11-15T06:31:06.000Z
- 원문 blob SHA: 4b8ef7be7bfbda1bfba9afd8416ad2c81042038e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 또한, 취약점 정보의 책임 있는 공개(Coordinated Vulnerability Disclosure) 프로세스를 수립하고 관련 기술 문서
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #80 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 불필요한 기능, 포트, 서비스가 기본적으로 비활성화된 'Secure by Default' 상태여야 하며, 사
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:35:33 (원문 시간대 미표기)
- 원문: [commit f88391a096e7d10b0239ca11afe961abbac16796](https://github.com/useformotor3/ai-discord-bot/commit/f88391a096e7d10b0239ca11afe961abbac16796) | [research_archive/2026-11-15_063533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_063533.md) | commit UTC: 2026-11-15T06:35:52.000Z
- 원문 blob SHA: a65acaab5cc24b52db24a4a475313e991881581c
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 불필요한 기능, 포트, 서비스가 기본적으로 비활성화된 'Secure by Default' 상태여야 하며, 사용자가 제품을 안전하게 초기화 및 설정할 수 있는 메커니즘을 제공해야 합니다. 이는 CRA Annex I에 명시된 필수 보안
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #81 — P1 — 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하는 안전한 기본 설정(Secure by default) 상태로 제공되어야 합니다. 핵심
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:40:35 (원문 시간대 미표기)
- 원문: [commit 2f386761ab8cd2ab170d3fc9052469a00f8261fb](https://github.com/useformotor3/ai-discord-bot/commit/2f386761ab8cd2ab170d3fc9052469a00f8261fb) | [research_archive/2026-11-15_064035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_064035.md) | commit UTC: 2026-11-15T06:40:51.000Z
- 원문 blob SHA: fc782ed944c09d03d9500ed6b42f69ecbc9a6ab6
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하는 안전한 기본 설정(Secure by default) 상태로 제공되어야 합니다. 핵심 내용 2: 고정된 마스터 패스워드 사용을 금지하며, 초기 인증 정보는 고유하게 생성되거나 최초 설정 시 사용자가 강제로 변경
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #82 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견되는 취약점에 대해 사용자에게 추가 비용 청구 없이(Free-of-charge) 보안 업데이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:45:46 (원문 시간대 미표기)
- 원문: [commit 9d9d930ac0f74a3c97b04e816e2f194555b7b603](https://github.com/useformotor3/ai-discord-bot/commit/9d9d930ac0f74a3c97b04e816e2f194555b7b603) | [research_archive/2026-11-15_064546.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_064546.md) | commit UTC: 2026-11-15T06:46:03.000Z
- 원문 blob SHA: a19f477eadb2079aabf2c5f46d3e1bcd0521f190
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견되는 취약점에 대해 사용자에게 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패치를 안전한 방식으로 배포해야 합니다. 또한, 이를 위해 취약점 공개 정책과 자동화된 업데이트 메커니즘을 기술 문서에
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #83 — P1 — 서보 드라이브는 공장 출고 시(Out of the box) 제3자가 무단으로 악용할 수 있는 취약한 기본 설정이나 고정된 관리자 계정(Default credentials)을 포함해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:50:31 (원문 시간대 미표기)
- 원문: [commit 343d935bb5fb8f965cc91343392b11d5119158b3](https://github.com/useformotor3/ai-discord-bot/commit/343d935bb5fb8f965cc91343392b11d5119158b3) | [research_archive/2026-11-15_065031.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_065031.md) | commit UTC: 2026-11-15T06:50:47.000Z
- 원문 blob SHA: 82f3dc4a13af996883c28286e9e6f4b838bf203d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out of the box) 제3자가 무단으로 악용할 수 있는 취약한 기본 설정이나 고정된 관리자 계정(Default credentials)을 포함해서는 안 되며, 제품을 처음 사용할 때 사용자가 안전한 설정을 강제로 구성하거나 고유한 인증 정보를 설정하도록 설계되어야 합니
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #84 — P0 — EU CRA에 따라 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트를 제공해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 06:55:30 (원문 시간대 미표기)
- 원문: [commit 71669a2fc5aaa34ad99ba098c7e54bff7b781ce9](https://github.com/useformotor3/ai-discord-bot/commit/71669a2fc5aaa34ad99ba098c7e54bff7b781ce9) | [research_archive/2026-11-15_065530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_065530.md) | commit UTC: 2026-11-15T06:55:46.000Z
- 원문 blob SHA: 0b877ba36fe3c5164a4f903aeff3b1a0b7c20ccc
- 핵심 주장 주제(원문 요약 첫 부분): EU CRA에 따라 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트를 제공해야 하며, 이를 안전하게 배포할 수 있는 자동화된 업데이트 메커니즘을 구현해야 합니다. 이는 산업 현장의 중단 없는 운영과 레
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #85 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 즉시 해결할 수 있는 보안 업데이트를 무상으로(Free of charge) 제공하고, 이를 안
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:00:56 (원문 시간대 미표기)
- 원문: [commit 6e2c90b77654a434021972d034fb402f187f71a2](https://github.com/useformotor3/ai-discord-bot/commit/6e2c90b77654a434021972d034fb402f187f71a2) | [research_archive/2026-11-15_070056.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_070056.md) | commit UTC: 2026-11-15T07:01:12.000Z
- 원문 blob SHA: f663c3fc604a37304246c279960db27f1e559ce1
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 즉시 해결할 수 있는 보안 업데이트를 무상으로(Free of charge) 제공하고, 이를 안전하게 배포할 수 있는 자동화된 메커니즘을 갖추어야 합니다. 사용자가 보안 업데이트를 쉽게 적용할 수 있도록 공지 및 설치 프
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #86 — P1 — 서보 드라이브는 시장 출시 시점부터 무단 접근을 방지하기 위해 안전한 초기 상태(Secure by default)로 설정되어야 하며, 특히 기본 설정된 관리자 비밀번호의 강제 변경
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:05:38 (원문 시간대 미표기)
- 원문: [commit 875833c67c579fcb3e01dade339f9ccb1238e998](https://github.com/useformotor3/ai-discord-bot/commit/875833c67c579fcb3e01dade339f9ccb1238e998) | [research_archive/2026-11-15_070538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_070538.md) | commit UTC: 2026-11-15T07:05:56.000Z
- 원문 blob SHA: cb0f89a679e71f267298327c23cf999486029b58
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 시장 출시 시점부터 무단 접근을 방지하기 위해 안전한 초기 상태(Secure by default)로 설정되어야 하며, 특히 기본 설정된 관리자 비밀번호의 강제 변경 또는 고유 인증(Unique credentials) 메커니즘을 반드시 제공해야 합니다. 이는 사용자가 개입하기 전 제조사 단
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #87 — P1 — 서보 드라이브 제조사는 제품 출시 시 잠재적 공격 표면을 최소화하기 위해 기본적으로 안전한 상태(Secure by default)로 설정해야 하며, 불필요한 기능 및 기본 인증 정
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:10:36 (원문 시간대 미표기)
- 원문: [commit f9010d269663b046effd7ca4702f0668f089d579](https://github.com/useformotor3/ai-discord-bot/commit/f9010d269663b046effd7ca4702f0668f089d579) | [research_archive/2026-11-15_071036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_071036.md) | commit UTC: 2026-11-15T07:10:52.000Z
- 원문 blob SHA: 388620e8622d83171b89f168c18c15ae07fdf0ba
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출시 시 잠재적 공격 표면을 최소화하기 위해 기본적으로 안전한 상태(Secure by default)로 설정해야 하며, 불필요한 기능 및 기본 인증 정보는 비활성화하거나 강제 변경하도록 설계해야 합니다. 사용자가 명시적으로 변경하지 않는 한, 위험을 초래할 수 있는 기본 액세
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #88 — P1 — 핵심 1: 산업용 서보 드라이브는 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 가능한 강력한 고유 기본 비밀번호 또는 사전 설정된 인증 메커니즘을 갖춘 '
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:15:36 (원문 시간대 미표기)
- 원문: [commit 6ca7e71ee3ca203f1693288fe017540fce304662](https://github.com/useformotor3/ai-discord-bot/commit/6ca7e71ee3ca203f1693288fe017540fce304662) | [research_archive/2026-11-15_071536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_071536.md) | commit UTC: 2026-11-15T07:15:52.000Z
- 원문 blob SHA: bc928c6e36239ff05ce8a94228190daca93116d1
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 1: 산업용 서보 드라이브는 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 가능한 강력한 고유 기본 비밀번호 또는 사전 설정된 인증 메커니즘을 갖춘 'Secure by default' 상태로 제공되어야 합니다. 핵심 2: 제조사는 사용자가 제품을 최초로 설치 및 시운전할 때
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #89 — P0 — 제조사는 서보 드라이브의 예상 수명 주기 동안 발견되는 취약점에 대해, 사용자에게 지체 없이 알리고 보안 업데이트(패치)를 추가 비용 없이(무상으로) 제공해야 합니다. 이는 Ann
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:20:35 (원문 시간대 미표기)
- 원문: [commit ed8354ebfe5bef67fd947e133b1090ad1c36c393](https://github.com/useformotor3/ai-discord-bot/commit/ed8354ebfe5bef67fd947e133b1090ad1c36c393) | [research_archive/2026-11-15_072035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_072035.md) | commit UTC: 2026-11-15T07:20:51.000Z
- 원문 blob SHA: 44af3f17184b0c3f1d7aaca020dc659b663a37e5
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 서보 드라이브의 예상 수명 주기 동안 발견되는 취약점에 대해, 사용자에게 지체 없이 알리고 보안 업데이트(패치)를 추가 비용 없이(무상으로) 제공해야 합니다. 이는 Annex I(필수 요건) 및 관련 조항에 명시된 법적 의무로, 산업용 기기의 잠재적 보안 리스크가 공급망 전체로 전파되는 것을 차
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #90 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 추측 가능한 기본 패스워드가 없거나, 사용자가 최초 로그인 시 강제로 고유한 비밀번호를 설정하
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:25:27 (원문 시간대 미표기)
- 원문: [commit b906ac612db56150511e99295350b31792900ea5](https://github.com/useformotor3/ai-discord-bot/commit/b906ac612db56150511e99295350b31792900ea5) | [research_archive/2026-11-15_072527.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_072527.md) | commit UTC: 2026-11-15T07:25:43.000Z
- 원문 blob SHA: e43d37e499e7608fb60d225358ceacfff2f03d35
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 추측 가능한 기본 패스워드가 없거나, 사용자가 최초 로그인 시 강제로 고유한 비밀번호를 설정하도록 강제하는 '기본 보안 설정(Secure by default)' 상태를 유지해야 합니다. 또한, 불필요한 기능이나 기본 활
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #91 — P1 — 서보 드라이브 제조사는 제품 출고 시 무단 접근을 방지하기 위해 안전한 기본 설정(Secure by Default)을 적용해야 하며, 특히 고유하지 않은 기본 패스워드의 사전 설치
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:30:40 (원문 시간대 미표기)
- 원문: [commit 836adb6b66cca9c5b77a1ee981a8eadae953078d](https://github.com/useformotor3/ai-discord-bot/commit/836adb6b66cca9c5b77a1ee981a8eadae953078d) | [research_archive/2026-11-15_073040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_073040.md) | commit UTC: 2026-11-15T07:30:56.000Z
- 원문 blob SHA: e7518f4f3eeba754663a3a78cad5c766bdd19662
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 무단 접근을 방지하기 위해 안전한 기본 설정(Secure by Default)을 적용해야 하며, 특히 고유하지 않은 기본 패스워드의 사전 설치를 금지해야 합니다. 사용자가 최초로 기기를 조작할 때 비밀번호 변경 또는 고유한 초기 인증 정보(Authentication
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #92 — P0 — 제조사는 서보 드라이브의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 자동 업데이트 메커
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:35:33 (원문 시간대 미표기)
- 원문: [commit 2cdc7469154012690bb932cb4d5c88eca9a56b0d](https://github.com/useformotor3/ai-discord-bot/commit/2cdc7469154012690bb932cb4d5c88eca9a56b0d) | [research_archive/2026-11-15_073533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_073533.md) | commit UTC: 2026-11-15T07:35:49.000Z
- 원문 blob SHA: 6441a9d0aa97f0e5928a70ae2b55aacc3f29adb0
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 서보 드라이브의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 적시에 제공해야 합니다. 자동 업데이트 메커니즘을 지원하고, 사용자가 업데이트 적용 여부를 통제할 수 있는 기능을 보장해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #93 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 무료로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 자동화된 업데이트 고지 및 배포 메커
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:40:34 (원문 시간대 미표기)
- 원문: [commit 359c40b48eafa5a33759e59b773e934b620334b5](https://github.com/useformotor3/ai-discord-bot/commit/359c40b48eafa5a33759e59b773e934b620334b5) | [research_archive/2026-11-15_074034.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_074034.md) | commit UTC: 2026-11-15T07:40:50.000Z
- 원문 blob SHA: b4798271e6632b880e8269ee4337996d1642cd52
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대해 무료로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 자동화된 업데이트 고지 및 배포 메커니즘을 갖추어야 합니다. 또한 최종 사용자에게 제품의 지원 종료일(End-of-Support)을 명확히 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #94 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용 없이 무상으로 제공해야 하며, 지원 기간 동안 이를 안전하게 전달할 수 있는 메커니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:45:36 (원문 시간대 미표기)
- 원문: [commit 7a24f759b5be72f25d5a16305326e8d8c5de61e3](https://github.com/useformotor3/ai-discord-bot/commit/7a24f759b5be72f25d5a16305326e8d8c5de61e3) | [research_archive/2026-11-15_074536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_074536.md) | commit UTC: 2026-11-15T07:45:52.000Z
- 원문 blob SHA: 0db7931678bab009c59be8035ca731130126a750
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용 없이 무상으로 제공해야 하며, 지원 기간 동안 이를 안전하게 전달할 수 있는 메커니즘을 갖추어야 합니다. 업데이트 과정에서 악성코드 주입이나 무단 변조를 방지하기 위해 배포 채널의 무결성과 진위 여부를 기술적
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #95 — P1 — 산업용 서보 드라이브는 공장 출고 시점부터 무단 접근을 방지하기 위해 고유한 비밀번호 설정 강제, 불필요한 네트워크 서비스 및 포트 비활성화 등 안전한 기본 상태(Secure by
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:50:41 (원문 시간대 미표기)
- 원문: [commit 26bde23cae330864d2a4f1be14ff1ca30f736305](https://github.com/useformotor3/ai-discord-bot/commit/26bde23cae330864d2a4f1be14ff1ca30f736305) | [research_archive/2026-11-15_075041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_075041.md) | commit UTC: 2026-11-15T07:50:57.000Z
- 원문 blob SHA: 60bc7d1663d44f0e36d251f8b2d0f78162f8f1d9
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시점부터 무단 접근을 방지하기 위해 고유한 비밀번호 설정 강제, 불필요한 네트워크 서비스 및 포트 비활성화 등 안전한 기본 상태(Secure by default)로 구성되어야 합니다. 제조사는 사용자가 제품을 최초로 설치하고 가동할 때 보안 설정을 변경하거나 강화하도록
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #96 — P1 — 서보 드라이브를 포함한 디지털 요소를 갖춘 제품은 배송 시 무단 접근을 방지하기 위해 안전한 기본 상태(Secure by default)로 설정되어야 하며, 특히 초기 기본 비밀번
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 07:55:31 (원문 시간대 미표기)
- 원문: [commit 81aadc0832000278fd2d6bb4be8efd65e60aff2a](https://github.com/useformotor3/ai-discord-bot/commit/81aadc0832000278fd2d6bb4be8efd65e60aff2a) | [research_archive/2026-11-15_075531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_075531.md) | commit UTC: 2026-11-15T07:55:48.000Z
- 원문 blob SHA: 742d471eab23d13ccbe3b89f2bb3acbbe6dd8452
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브를 포함한 디지털 요소를 갖춘 제품은 배송 시 무단 접근을 방지하기 위해 안전한 기본 상태(Secure by default)로 설정되어야 하며, 특히 초기 기본 비밀번호는 고유하게 생성되거나 사용자가 최초 접속 시 반드시 변경하도록 강제해야 합니다. 제조사는 제품의 보안 기능을 사용자가 쉽게
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #97 — P1 — 서보 드라이브는 초기 출고 시점부터 무단 접근을 방지하는 가장 안전한 상태(Secure by default)로 설정되어야 하며, 제조사는 제품의 공격 표면을 최소화하기 위해 불필요
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:00:50 (원문 시간대 미표기)
- 원문: [commit 52e69761bcaec4d6d7405fe9f7a131a039a62e02](https://github.com/useformotor3/ai-discord-bot/commit/52e69761bcaec4d6d7405fe9f7a131a039a62e02) | [research_archive/2026-11-15_080050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_080050.md) | commit UTC: 2026-11-15T08:01:07.000Z
- 원문 blob SHA: 45d44ea3c507405f5822fff7a0159a84f2902be2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시점부터 무단 접근을 방지하는 가장 안전한 상태(Secure by default)로 설정되어야 하며, 제조사는 제품의 공격 표면을 최소화하기 위해 불필요한 기능과 인터페이스가 기본적으로 비활성화되도록 설계해야 합니다. 사용자가 보안 설정을 변경하지 않더라도, 시스템은 내재된 보
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #101 — P1 — 서보 드라이브 제조사는 제품 출하 시 무단 접근을 방지하기 위해 불필요한 기능과 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태를 제공해야 합니다
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:20:37 (원문 시간대 미표기)
- 원문: [commit 1e750b8454038ccb68f7358edc422d4cf38fc8db](https://github.com/useformotor3/ai-discord-bot/commit/1e750b8454038ccb68f7358edc422d4cf38fc8db) | [research_archive/2026-11-15_082037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_082037.md) | commit UTC: 2026-11-15T08:20:53.000Z
- 원문 blob SHA: a0cc092f6d3e6be88fc33f998b670ead96102677
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출하 시 무단 접근을 방지하기 위해 불필요한 기능과 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태를 제공해야 합니다. 사용자가 시스템을 최초 부팅하거나 설정할 때, 강력한 초기 인증 설정(예: 고유한 기본 비밀번호 강제 변경)을 의무화하는
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #102 — P1 — 산업용 서보 드라이브는 출고 시 기본적으로 안전한 상태(Secure by default)로 설정되어야 하며, 사용자가 이를 임의로 취약하게 변경하기 어렵거나 변경 시 보안 위험에 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:25:37 (원문 시간대 미표기)
- 원문: [commit a2c7bc8267ea612b9f693075d136c886cd3ad93f](https://github.com/useformotor3/ai-discord-bot/commit/a2c7bc8267ea612b9f693075d136c886cd3ad93f) | [research_archive/2026-11-15_082537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_082537.md) | commit UTC: 2026-11-15T08:25:53.000Z
- 원문 blob SHA: c871f04b04c285dd229de802d6f3919fa43af0f3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시 기본적으로 안전한 상태(Secure by default)로 설정되어야 하며, 사용자가 이를 임의로 취약하게 변경하기 어렵거나 변경 시 보안 위험에 대해 명확한 경고를 제공해야 합니다. 또한, 불필요한 공격 표면(Attack Surface)을 줄이기 위해 기본적으로 모든 외
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #103 — P1 — 핵심 내용 1: 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위해 기본적으로 안전한 상태(Secure by default)로 설정되어야 합니다. 핵심 내용 2: 특히
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:30:43 (원문 시간대 미표기)
- 원문: [commit eaa90c251a0da8e852565d3a14b4e6f6266d0e46](https://github.com/useformotor3/ai-discord-bot/commit/eaa90c251a0da8e852565d3a14b4e6f6266d0e46) | [research_archive/2026-11-15_083043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_083043.md) | commit UTC: 2026-11-15T08:31:00.000Z
- 원문 blob SHA: 569cd92ff6af35ed71d37b99f5acc65ed5a99ce2
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위해 기본적으로 안전한 상태(Secure by default)로 설정되어야 합니다. 핵심 내용 2: 특히 취약한 기본 비밀번호나 하드코딩된 인증 정보의 사용을 원천 차단하고, 초기 설정 과정에서 사용자가 고유한 인증 정보를 강제로
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #104 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대해 별도의 추가 비용 없이(무상으로) 보안 업데이트를 제공해야 하며, 사용자(운영자)가 이를 안전하고 원활하
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:35:29 (원문 시간대 미표기)
- 원문: [commit 0a7b95566164c86494ff004513718f2710fc47f4](https://github.com/useformotor3/ai-discord-bot/commit/0a7b95566164c86494ff004513718f2710fc47f4) | [research_archive/2026-11-15_083529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_083529.md) | commit UTC: 2026-11-15T08:35:46.000Z
- 원문 blob SHA: 2dfbd78a84b6a435347da6be923f4b3be6edd63f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대해 별도의 추가 비용 없이(무상으로) 보안 업데이트를 제공해야 하며, 사용자(운영자)가 이를 안전하고 원활하게 적용할 수 있는 메커니즘을 보장해야 합니다. 규정에 따라 보안 업데이트는 기본적으로 자동화된 방식으로 제공되거나, 사용자가
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #105 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box) 무단 접근 위험을 최소화하기 위해 강력한 기본 보안 설정(Secure by default)을 적용해야 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:40:35 (원문 시간대 미표기)
- 원문: [commit 3b8b9a246bba8423d17bf2ba49e423b5ac778f8d](https://github.com/useformotor3/ai-discord-bot/commit/3b8b9a246bba8423d17bf2ba49e423b5ac778f8d) | [research_archive/2026-11-15_084035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_084035.md) | commit UTC: 2026-11-15T08:40:52.000Z
- 원문 blob SHA: 0dd57fc61790823dc438d584f51eab0b76456200
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box) 무단 접근 위험을 최소화하기 위해 강력한 기본 보안 설정(Secure by default)을 적용해야 하며, 특히 초기 인증 정보, 불필요한 포트 및 서비스의 기본 비활성화를 보장해야 합니다. 또한, 사용자가 보안이 취약한 상태
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #106 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 동안 발견되는 취약점을 수정하기 위한 보안 업데이트를 추가 비용 없이(Free-of-charge) 제공해야 합니다. 또한, 발견된 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:45:37 (원문 시간대 미표기)
- 원문: [commit 843ad4b4b1d906f1e978ae8fd00819133c2bd6c8](https://github.com/useformotor3/ai-discord-bot/commit/843ad4b4b1d906f1e978ae8fd00819133c2bd6c8) | [research_archive/2026-11-15_084537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_084537.md) | commit UTC: 2026-11-15T08:45:53.000Z
- 원문 blob SHA: f98d4e153cb5c41bbe7e526b5174489c9cd6cb57
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 동안 발견되는 취약점을 수정하기 위한 보안 업데이트를 추가 비용 없이(Free-of-charge) 제공해야 합니다. 또한, 발견된 취약점은 불필요한 지연 없이 시기적절하게(Without undue delay) 패치되어야 하며, 이는 제조사의 명백한 법적 의
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #107 — P1 — 서보 드라이브 제조사는 제품 출고 시 잠재적 공격 표면을 최소화하기 위해 모든 기본(Default) 계정, 비밀번호, 통신 포트 및 서비스가 안전한 상태(Secure by defa
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:50:33 (원문 시간대 미표기)
- 원문: [commit 3ddf242c5080a5dbb40f97b0327ce04b8858f00a](https://github.com/useformotor3/ai-discord-bot/commit/3ddf242c5080a5dbb40f97b0327ce04b8858f00a) | [research_archive/2026-11-15_085033.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_085033.md) | commit UTC: 2026-11-15T08:50:50.000Z
- 원문 blob SHA: 199c0c53e59daf48002dcce15d91091b3041cc72
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 잠재적 공격 표면을 최소화하기 위해 모든 기본(Default) 계정, 비밀번호, 통신 포트 및 서비스가 안전한 상태(Secure by default)로 설정되도록 강제해야 합니다. 특히 초기 전원 인가 시 사용자가 기본 인증 정보를 반드시 변경하도록 유도하거나, 불필
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #108 — P1 — (핵심 내용 2줄) 서보 드라이브는 공장 출하 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 가능한 고유의 기본 비밀번호를 탑재하거나, 강력한 초기 인증 메커니즘
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:55:38 (원문 시간대 미표기)
- 원문: [commit 2d3246ea01f08059a9c9cfee9f82374ece8807a2](https://github.com/useformotor3/ai-discord-bot/commit/2d3246ea01f08059a9c9cfee9f82374ece8807a2) | [research_archive/2026-11-15_085538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_085538.md) | commit UTC: 2026-11-15T08:55:55.000Z
- 원문 blob SHA: 257d47b7684a8e6751a8b131e7b9f044997e6c9d
- 핵심 주장 주제(원문 요약 첫 부분): (핵심 내용 2줄) 서보 드라이브는 공장 출하 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 가능한 고유의 기본 비밀번호를 탑재하거나, 강력한 초기 인증 메커니즘을 강제하는 '기본 설정 보안(Secure by default)' 상태여야 합니다. 제조사는 제품이 사용자의 최소한의 개입으로
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #109 — P0 — 제조사는 서보 드라이브에 식별된 보안 취약점을 추가 비용 청구 없이(무상으로) 적시에 패치해야 하며, 사용자에게 안전한 업데이트 메커니즘과 배포 사실을 명확히 고지해야 합니다. 이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:00:50 (원문 시간대 미표기)
- 원문: [commit c75449d6826e5e0b2c5f1ac81cd0f4323c7f04ab](https://github.com/useformotor3/ai-discord-bot/commit/c75449d6826e5e0b2c5f1ac81cd0f4323c7f04ab) | [research_archive/2026-11-15_090050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_090050.md) | commit UTC: 2026-11-15T09:01:07.000Z
- 원문 blob SHA: fc90920872d84dfc5dbccb9cb1632282bacfa69e
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 서보 드라이브에 식별된 보안 취약점을 추가 비용 청구 없이(무상으로) 적시에 패치해야 하며, 사용자에게 안전한 업데이트 메커니즘과 배포 사실을 명확히 고지해야 합니다. 이는 산업 현장의 예기치 않은 가동 중단(Downtime)을 방지하고, 제품의 예상 수명 동안 지속적인 보안 무결성을 보장하기
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #110 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대응하기 위해 보안 업데이트(패치)를 추가 비용 없이 안전하게 배포해야 하며, 이를 지연 없이 사용자에게 제공
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:05:33 (원문 시간대 미표기)
- 원문: [commit 7dbb3b31aa55693efa2ac0c6da6248f4b05ead20](https://github.com/useformotor3/ai-discord-bot/commit/7dbb3b31aa55693efa2ac0c6da6248f4b05ead20) | [research_archive/2026-11-15_090533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_090533.md) | commit UTC: 2026-11-15T09:05:49.000Z
- 원문 blob SHA: ff90946b977d5a06ecfd0e513519476fef4a8ef5
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대응하기 위해 보안 업데이트(패치)를 추가 비용 없이 안전하게 배포해야 하며, 이를 지연 없이 사용자에게 제공할 기술적 수단을 강구해야 합니다. 또한, 업데이트 적용 과정에서 제품의 핵심 기능(모터 제어 등)이 중단되거나 손상되지 않도
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #111 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 불가능한 고유의 초기 비밀번호 또는 강력한 기본 인증 체계를 갖추어야 합니다. 제조사는 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:10:32 (원문 시간대 미표기)
- 원문: [commit 29637cec141dc8fc040884bc15b6410def208147](https://github.com/useformotor3/ai-discord-bot/commit/29637cec141dc8fc040884bc15b6410def208147) | [research_archive/2026-11-15_091032.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_091032.md) | commit UTC: 2026-11-15T09:10:48.000Z
- 원문 blob SHA: f5358bfe1195d9285c50b2101410529acbac49a2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 변경 불가능한 고유의 초기 비밀번호 또는 강력한 기본 인증 체계를 갖추어야 합니다. 제조사는 제품의 기본 설정 단계에서 공격 표면(Attack Surface)을 최소화하도록 보안이 강화된 상태로 작동(Secure by
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #112 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용료 청구 없이 무상으로 제공해야 하며, 이를 안전하게 배포할 수 있는 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:15:37 (원문 시간대 미표기)
- 원문: [commit d8c15f992ddcfcaa13b1fa0db37b0ec3dcfe426e](https://github.com/useformotor3/ai-discord-bot/commit/d8c15f992ddcfcaa13b1fa0db37b0ec3dcfe426e) | [research_archive/2026-11-15_091537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_091537.md) | commit UTC: 2026-11-15T09:15:53.000Z
- 원문 blob SHA: 988a3ff662602910d63a86c888df54d9b9057337
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용료 청구 없이 무상으로 제공해야 하며, 이를 안전하게 배포할 수 있는 메커니즘을 갖추어야 합니다. 또한, 취약점 정보는 ENISA 및 관련 당국에 법적 기한 내에 신고해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #113 — P1 — 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by Default)을 적용해야 합니다. 제조사는 사용자에게 제품 인계 시, 비밀번호, 통
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:20:36 (원문 시간대 미표기)
- 원문: [commit 2b7a9f908e3b85ff1121902080cc30d570699235](https://github.com/useformotor3/ai-discord-bot/commit/2b7a9f908e3b85ff1121902080cc30d570699235) | [research_archive/2026-11-15_092036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_092036.md) | commit UTC: 2026-11-15T09:20:54.000Z
- 원문 blob SHA: 2e119a30b14c68ad5c412b41a1f5b4e5e78d7f7f
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by Default)을 적용해야 합니다. 제조사는 사용자에게 제품 인계 시, 비밀번호, 통신 포트, 서비스 등의 초기 보안 상태가 최고 수준의 보호를 제공하도록 강제해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #114 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견되는 보안 취약점을 추가 비용 청구 없이(무상으로) 보안 업데이트 형태로 최종 사용자에게 제공해야 합니다.
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:25:31 (원문 시간대 미표기)
- 원문: [commit 58a96b8a8a8dfcd295c89a853291ede0cbc6a29b](https://github.com/useformotor3/ai-discord-bot/commit/58a96b8a8a8dfcd295c89a853291ede0cbc6a29b) | [research_archive/2026-11-15_092531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_092531.md) | commit UTC: 2026-11-15T09:25:47.000Z
- 원문 blob SHA: e79c420db9c8af95cd877a7372db489c5cc5031e
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견되는 보안 취약점을 추가 비용 청구 없이(무상으로) 보안 업데이트 형태로 최종 사용자에게 제공해야 합니다. 또한, 업데이트 가용성에 대해 명확하고 투명한 정보를 사전에 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #115 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견된 취약점에 대한 보안 업데이트(패치)를 추가 비용 없이 안전한 메커니즘을 통해 적시에 제공해야 합니다. 또한, 지
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:30:41 (원문 시간대 미표기)
- 원문: [commit 1c84fe525f8b43d651aafe26a0e3bbc8f7e2b227](https://github.com/useformotor3/ai-discord-bot/commit/1c84fe525f8b43d651aafe26a0e3bbc8f7e2b227) | [research_archive/2026-11-15_093041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_093041.md) | commit UTC: 2026-11-15T09:30:57.000Z
- 원문 blob SHA: f86a439036066fe8568b6796f46fda6488772ac4
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견된 취약점에 대한 보안 업데이트(패치)를 추가 비용 없이 안전한 메커니즘을 통해 적시에 제공해야 합니다. 또한, 지원 종료(EOL) 시점과 그 이후의 대응 방안을 사용자에게 명확히 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #116 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 이상) 발견된 보안 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 적시에 제공해야 하며, 취
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:35:29 (원문 시간대 미표기)
- 원문: [commit 82fba8b534d48f13a4e11c52b81318496a5e90e6](https://github.com/useformotor3/ai-discord-bot/commit/82fba8b534d48f13a4e11c52b81318496a5e90e6) | [research_archive/2026-11-15_093529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_093529.md) | commit UTC: 2026-11-15T09:35:47.000Z
- 원문 blob SHA: f0929cc02c7af6d4594448352170c16be26d3f58
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 이상) 발견된 보안 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 적시에 제공해야 하며, 취약점 발견 시 이를 제조사 및 관련 기관에 안전하게 신고할 수 있는 공개된 취약점 접수 메커니즘(Coordinated Vuln
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 corrective/mitigating measure 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지를 별도 확인.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #117 — P1 — 서보 드라이브는 제조 단계부터 불필요한 기능, 포트, 서비스 등이 기본적으로 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 공급되어야 합니다. 또한 사용자
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:40:36 (원문 시간대 미표기)
- 원문: [commit 0d98d8813052970bdd1b9cf43823997fafe79389](https://github.com/useformotor3/ai-discord-bot/commit/0d98d8813052970bdd1b9cf43823997fafe79389) | [research_archive/2026-11-15_094036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_094036.md) | commit UTC: 2026-11-15T09:40:52.000Z
- 원문 blob SHA: 78026343076d02db89268664a346c6e8debae6d9
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 제조 단계부터 불필요한 기능, 포트, 서비스 등이 기본적으로 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 공급되어야 합니다. 또한 사용자가 제품을 처음 안전하게 구동할 수 있도록 초기 인증 정보의 안전한 관리 체계를 제공해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #118 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 수정 패치 및 업데이트를 사용자에게 안전한 메커니즘을 통
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:45:36 (원문 시간대 미표기)
- 원문: [commit 86766bf8a4c6c8399fee705e01eb350df3fb415b](https://github.com/useformotor3/ai-discord-bot/commit/86766bf8a4c6c8399fee705e01eb350df3fb415b) | [research_archive/2026-11-15_094536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_094536.md) | commit UTC: 2026-11-15T09:46:04.000Z
- 원문 blob SHA: 6981fcc3329ae113bdc58e8f1eb101384bf7c7ed
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 수정 패치 및 업데이트를 사용자에게 안전한 메커니즘을 통해 지체 없이 제공할 기술적/운영적 체계를 갖추어야 합니다. 특히 중요 제품(Class I/II)의 경우 이를 입증하기 위한
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #119 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증되지 않은 원격 접속, 취약한 기본 비밀번호, 불필요하게 활성화된 통신 포트 및 서비스가 모두 차단된 'Secure 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:50:41 (원문 시간대 미표기)
- 원문: [commit f1315dc5b876b92028c2d46b050a37740f78f42c](https://github.com/useformotor3/ai-discord-bot/commit/f1315dc5b876b92028c2d46b050a37740f78f42c) | [research_archive/2026-11-15_095041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_095041.md) | commit UTC: 2026-11-15T09:51:15.000Z
- 원문 blob SHA: 5f181caa7ee4187dcdc9dca54eaa238cab9f055b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증되지 않은 원격 접속, 취약한 기본 비밀번호, 불필요하게 활성화된 통신 포트 및 서비스가 모두 차단된 'Secure by Default' 상태를 반드시 유지해야 하며, 사용자가 최초 전원을 켤 때 안전한 설정 변경을 강제할 수 있는 메커니즘을
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #120 — P3 — ⚠️ [시스템 긴급 경고] 모든 AI 모델(Latest 및 Lite)의 일시적 과부하로 이번 회차 조사가 지연되었습니다. 시스템은 정상 대기 중입니다.
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 09:55:33 (원문 시간대 미표기)
- 원문: [commit cd56916a8f842425d46ba25809a8170349615749](https://github.com/useformotor3/ai-discord-bot/commit/cd56916a8f842425d46ba25809a8170349615749) | [research_archive/2026-11-15_095533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_095533.md) | commit UTC: 2026-11-15T09:55:59.000Z
- 원문 blob SHA: 25a98c989c79f890b2bc77c742883ca0436ea4b8
- 핵심 주장 주제(원문 요약 첫 부분): ⚠️ [시스템 긴급 경고] 모든 AI 모델(Latest 및 Lite)의 일시적 과부하로 이번 회차 조사가 지연되었습니다. 시스템은 정상 대기 중입니다.
- 우선순위/검증 쟁점: P3 — 정확한 조항·문서 버전·주변 문맥을 원문에서 재확인해야 함. 이 항목은 주제 기반 사전 분류이며 개별 claim 검증 완료가 아님.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #121 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Updates)를 지체 없이 제공해야 합니다. 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:00:50 (원문 시간대 미표기)
- 원문: [commit b463182f3e3e265e3c73986a986021c24858d70d](https://github.com/useformotor3/ai-discord-bot/commit/b463182f3e3e265e3c73986a986021c24858d70d) | [research_archive/2026-11-15_100050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_100050.md) | commit UTC: 2026-11-15T10:01:15.000Z
- 원문 blob SHA: 4813cb3e9756642ade33a8b213242adaa7fd5148
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(Security Updates)를 지체 없이 제공해야 합니다. 사용자(공장 운영자)가 추가 비용 없이 안전하게 제품을 운영할 수 있도록 기본 취약점 수정 및 패치 메커니즘을 보장해야 합니다
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #122 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대해 사용자에게 추가 비용 부과 없이 보안 업데이트 및 패치를 안전한 방식으로 적시에 제공해야 합니다. 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:05:35 (원문 시간대 미표기)
- 원문: [commit 7eb1a6c05ff75eeb63e474040d698bd8a9a534c1](https://github.com/useformotor3/ai-discord-bot/commit/7eb1a6c05ff75eeb63e474040d698bd8a9a534c1) | [research_archive/2026-11-15_100535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_100535.md) | commit UTC: 2026-11-15T10:05:53.000Z
- 원문 blob SHA: 11a15414f000ed864bbae1067c7bec84c32047ac
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대해 사용자에게 추가 비용 부과 없이 보안 업데이트 및 패치를 안전한 방식으로 적시에 제공해야 합니다. 또한, 이를 위한 자동화된 업데이트 메커니즘과 무결성 검증 체계를 갖추어야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9)의 업데이트 가용성 유지와 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #123 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 우회를 방지하기 위해 고유하거나 변경 가능한 초기 비밀번호와 함께 안전한 기본 설정(Secure by def
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:10:36 (원문 시간대 미표기)
- 원문: [commit 8b754423eb65e297f4d2d9cd579968a61224dcdc](https://github.com/useformotor3/ai-discord-bot/commit/8b754423eb65e297f4d2d9cd579968a61224dcdc) | [research_archive/2026-11-15_101036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_101036.md) | commit UTC: 2026-11-15T10:10:54.000Z
- 원문 blob SHA: 5eac530700a2dc299c989fc6d634fb2f944e19a9
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 우회를 방지하기 위해 고유하거나 변경 가능한 초기 비밀번호와 함께 안전한 기본 설정(Secure by default) 상태로 제공되어야 합니다. 불필요한 서비스와 하드웨어가 기본적으로 비활성화되어 있어야 하며, 사용자가 제품을 안전하
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #124 — P1 — 산업용 서보 드라이브는 공장 출고 시부터 무단 액세스를 방지하는 안전한 기본 상태(Secure by Default)로 설정되어야 하며, 초기 인증 정보 변경을 강제하고 불필요한 공
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:15:34 (원문 시간대 미표기)
- 원문: [commit 21a771a71def02c021a15f35824505e97c98e7b7](https://github.com/useformotor3/ai-discord-bot/commit/21a771a71def02c021a15f35824505e97c98e7b7) | [research_archive/2026-11-15_101534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_101534.md) | commit UTC: 2026-11-15T10:15:50.000Z
- 원문 blob SHA: 54c3baaf6df9372271e1dcfde53f485248d57dc2
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시부터 무단 액세스를 방지하는 안전한 기본 상태(Secure by Default)로 설정되어야 하며, 초기 인증 정보 변경을 강제하고 불필요한 공격 표면(Attack Surface)을 원천 차단해야 합니다. 제조사는 제품이 시장에 출시되기 전 이러한 기본 보안 요구사항이
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #125 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 관리자 계정의 기본 비밀번호(Default credentials) 사용을 금지하고, 사용자가 최초 접속 시 반드시
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:20:37 (원문 시간대 미표기)
- 원문: [commit f8069982b63b11fbec2f5547e2c39282bf32f6e4](https://github.com/useformotor3/ai-discord-bot/commit/f8069982b63b11fbec2f5547e2c39282bf32f6e4) | [research_archive/2026-11-15_102037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_102037.md) | commit UTC: 2026-11-15T10:20:56.000Z
- 원문 blob SHA: c867eebb2ce62e92402281c9a9af9f8cb2c9675f
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 관리자 계정의 기본 비밀번호(Default credentials) 사용을 금지하고, 사용자가 최초 접속 시 반드시 고유한 비밀번호를 강제로 설정하도록 설계되어야 합니다. 또한, 공격에 악용될 수 있는 불필요한 네트워크 서비스와 포트는 기본
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #126 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box), 추가적인 보안 설정 변경 없이도 무단 접근 및 공격을 방어할 수 있도록 기본적으로 안전한 상태(Sec
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:25:29 (원문 시간대 미표기)
- 원문: [commit 47a3515b9494c36d612159253c3f483092674732](https://github.com/useformotor3/ai-discord-bot/commit/47a3515b9494c36d612159253c3f483092674732) | [research_archive/2026-11-15_102529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_102529.md) | commit UTC: 2026-11-15T10:25:46.000Z
- 원문 blob SHA: b2dc172101ae08696c855fda39ac29dd46aaa6ab
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box), 추가적인 보안 설정 변경 없이도 무단 접근 및 공격을 방어할 수 있도록 기본적으로 안전한 상태(Secure by Default)로 설정되어 제공해야 합니다. 특히 초기 인증정보(예: 기본 패스워드)가 하드코딩되거나 전역으로 동
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #127 — P1 — 서보 드라이브는 공장 초기화 시 보안이 취약한 기본값(예: 기본 비밀번호, 개방된 포트)이 설정되지 않아야 하며(Secure by default), 사용자가 강제로 안전한 설정으로
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:30:42 (원문 시간대 미표기)
- 원문: [commit 6c9e668deadb9cb286d68fc5b204ab1ebeb77197](https://github.com/useformotor3/ai-discord-bot/commit/6c9e668deadb9cb286d68fc5b204ab1ebeb77197) | [research_archive/2026-11-15_103042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_103042.md) | commit UTC: 2026-11-15T10:30:58.000Z
- 원문 blob SHA: 63f7197bfb16dec95016078eb3573313b262fed6
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 초기화 시 보안이 취약한 기본값(예: 기본 비밀번호, 개방된 포트)이 설정되지 않아야 하며(Secure by default), 사용자가 강제로 안전한 설정으로 변경하거나 복원할 수 있는 메커니즘을 제공해야 합니다. 또한, 승인되지 않은 개인이 제조사의 기본 설정을 임의로 변경하여 모
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #128 — P1 — 서보 드라이브는 초기 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 추측 가능한 기본 패스워드가 제거되어 있거나, 사용자가 최초 접속 시 강력하고 고유한 인증 정
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:35:33 (원문 시간대 미표기)
- 원문: [commit fddceb980b31d8d8b8f2d6bf5e168166b5228d4b](https://github.com/useformotor3/ai-discord-bot/commit/fddceb980b31d8d8b8f2d6bf5e168166b5228d4b) | [research_archive/2026-11-15_103533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_103533.md) | commit UTC: 2026-11-15T10:35:50.000Z
- 원문 blob SHA: 609e11188805ac2d430a9af6dea0419ac9195cf5
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시(Out-of-the-box) 무단 접근을 방지하기 위해 추측 가능한 기본 패스워드가 제거되어 있거나, 사용자가 최초 접속 시 강력하고 고유한 인증 정보를 강제로 설정하도록 하는 'Secure by Default(기본 설정 보안)' 및 취약한 인증 관리 체계를 갖추어야 합니다
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.
