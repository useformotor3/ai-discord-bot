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

### 2026-11-15 #129 — P1 — 서보 드라이브 제조사는 제품 출하 시 사용자가 별도의 복잡한 보안 설정을 하지 않아도 안전하게 동작하도록 '기본 보안 설정(Secure by default)' 상태를 제공해야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:40:36 (원문 시간대 미표기)
- 원문: [commit e3fe13db17afd6ddee3c3d7ac45e8c1d366fcdb8](https://github.com/useformotor3/ai-discord-bot/commit/e3fe13db17afd6ddee3c3d7ac45e8c1d366fcdb8) | [research_archive/2026-11-15_104036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_104036.md) | commit UTC: 2026-11-15T10:40:51.000Z
- 원문 blob SHA: 2b0b97829cfb7fb47ce5146783071fcf2a244304
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출하 시 사용자가 별도의 복잡한 보안 설정을 하지 않아도 안전하게 동작하도록 '기본 보안 설정(Secure by default)' 상태를 제공해야 합니다. 불필요한 기본 계정, 개방된 포트, 약한 인증 메커니즘을 원천 차단하고, 초기 상태에서 사용자가 보안 매개변수(비밀번호
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #130 — P0 — 서보 드라이브 제조사는 제품의 예상 사용 기간 동안(최소 5년 또는 법적 요구 기간) 발견된 취약점을 무상으로 패치할 수 있는 보안 업데이트를 제공해야 하며, 이를 명확한 지원 기
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:45:35 (원문 시간대 미표기)
- 원문: [commit a626f58ffad320dad574db0c9b7c61e15c35d901](https://github.com/useformotor3/ai-discord-bot/commit/a626f58ffad320dad574db0c9b7c61e15c35d901) | [research_archive/2026-11-15_104535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_104535.md) | commit UTC: 2026-11-15T10:45:50.000Z
- 원문 blob SHA: 12b710b7e441b0c115f87164e34b0f7ccb6ab568
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 사용 기간 동안(최소 5년 또는 법적 요구 기간) 발견된 취약점을 무상으로 패치할 수 있는 보안 업데이트를 제공해야 하며, 이를 명확한 지원 기간(Support Period)과 함께 사용자에게 고지해야 합니다. 이는 취약점 공개 이후 적시에 안전한 상태로 복원하기 위한
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #131 — P1 — 주제: 서보 드라이브의 출고 시 기본 설정 보안(Secure by Default) 및 초기 인증 강화 핵심 내용: 제조사는 서보 드라이브를 최초 부팅하거나 출고할 때, 변경 가능한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:50:35 (원문 시간대 미표기)
- 원문: [commit 4fbaa7803550bf7c37fb0677e38d05f0319b2d1b](https://github.com/useformotor3/ai-discord-bot/commit/4fbaa7803550bf7c37fb0677e38d05f0319b2d1b) | [research_archive/2026-11-15_105035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_105035.md) | commit UTC: 2026-11-15T10:50:49.000Z
- 원문 blob SHA: 356993f14b97b28b96cfd76d2f7426c9dd9a5c23
- 핵심 주장 주제(원문 요약 첫 부분): 주제: 서보 드라이브의 출고 시 기본 설정 보안(Secure by Default) 및 초기 인증 강화 핵심 내용: 제조사는 서보 드라이브를 최초 부팅하거나 출고할 때, 변경 가능한 기본 비밀번호 비활성화, 불필요한 네트워크 서비스 및 포트 폐쇄 등 무단 접근을 방지하는 안전한 기본 상태(Secure by
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #132 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치할 수 있는 보안 업데이트(패치)를 사용자에게 제공해야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 10:55:35 (원문 시간대 미표기)
- 원문: [commit 215cc40dbc63baaf74d1ffdb5eae890cd555759a](https://github.com/useformotor3/ai-discord-bot/commit/215cc40dbc63baaf74d1ffdb5eae890cd555759a) | [research_archive/2026-11-15_105535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_105535.md) | commit UTC: 2026-11-15T10:55:52.000Z
- 원문 blob SHA: a2e85537620728b71341b939f67bef747ca771b8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치할 수 있는 보안 업데이트(패치)를 사용자에게 제공해야 하며, 업데이트 가용성에 대한 명확한 사후 지원 정책을 수립해야 합니다. 이는 산업 현장의 레거시 기기가 보안 사각지대에 방
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #133 — P0 — 서보 드라이브 제조사는 제품의 예상 사용 기간(최소 5년) 동안 발견된 보안 취약점에 대해 추가 비용 청구 없이(free of charge) 보안 업데이트 및 패치를 적시에 제공해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:00:51 (원문 시간대 미표기)
- 원문: [commit 79591bf2f4cbde2f89d6a144fe6fa12d82582f63](https://github.com/useformotor3/ai-discord-bot/commit/79591bf2f4cbde2f89d6a144fe6fa12d82582f63) | [research_archive/2026-11-15_110051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_110051.md) | commit UTC: 2026-11-15T11:01:06.000Z
- 원문 blob SHA: f37eeb35a0389e632534d8ac2667451783d21c06
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 사용 기간(최소 5년) 동안 발견된 보안 취약점에 대해 추가 비용 청구 없이(free of charge) 보안 업데이트 및 패치를 적시에 제공해야 합니다. 또한, 이를 위해 사전에 정의된 지원 기간(Support Period) 정보를 사용자에게 명확히 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #134 — P1 — 서보 드라이브 제조사는 제품 출고 시 무단 액세스 방지를 위해 불필요한 기능과 인터페이스가 비활성화된 '기본 설정(Secure by Default)' 상태를 제공해야 합니다. 또한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:05:30 (원문 시간대 미표기)
- 원문: [commit c2064174c9ef49803093c9c297a59181a25a5ed2](https://github.com/useformotor3/ai-discord-bot/commit/c2064174c9ef49803093c9c297a59181a25a5ed2) | [research_archive/2026-11-15_110530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_110530.md) | commit UTC: 2026-11-15T11:05:47.000Z
- 원문 blob SHA: 986c9d5674ceac1f6903d05c84e45e1d5bf17499
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 무단 액세스 방지를 위해 불필요한 기능과 인터페이스가 비활성화된 '기본 설정(Secure by Default)' 상태를 제공해야 합니다. 또한, 사용자 인증 및 권한 관리를 통해 공격 표면을 원천적으로 최소화하도록 설계해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #135 — P0 — 제조사는 산업용 서보 드라이브의 예상 사용 기간(Support Period) 동안 발견된 취약점을 무상으로 수정해야 하며, 이를 위한 보안 업데이트(패치)를 지체 없이 제공할 법적
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:10:39 (원문 시간대 미표기)
- 원문: [commit 2e810a2b9ede0ba8f574aed75c7bed96fc08b043](https://github.com/useformotor3/ai-discord-bot/commit/2e810a2b9ede0ba8f574aed75c7bed96fc08b043) | [research_archive/2026-11-15_111039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_111039.md) | commit UTC: 2026-11-15T11:10:54.000Z
- 원문 blob SHA: 372f7850302bf4aa4ee759423001c1b98f982388
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 산업용 서보 드라이브의 예상 사용 기간(Support Period) 동안 발견된 취약점을 무상으로 수정해야 하며, 이를 위한 보안 업데이트(패치)를 지체 없이 제공할 법적 의무를 가집니다. 이는 제조물 책임 및 상업적 조건과 무관하게 강력한 사후 보안 무결성을 보장하기 위한 CRA 핵심 준수 사
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #136 — P1 — 서보 드라이브는 출하 시점부터 불필요한 서비스와 포트가 비활성화된 '기본 설정(Secure by Default)' 상태를 유지해야 합니다. 제조사는 제품의 공격면(Attack Su
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:15:38 (원문 시간대 미표기)
- 원문: [commit 7a065d083e45e95f7a864ce094155cc17660937d](https://github.com/useformotor3/ai-discord-bot/commit/7a065d083e45e95f7a864ce094155cc17660937d) | [research_archive/2026-11-15_111538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_111538.md) | commit UTC: 2026-11-15T11:15:53.000Z
- 원문 blob SHA: 316fe2c546aee8039db7d9b1bd1e20fe2693de59
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 출하 시점부터 불필요한 서비스와 포트가 비활성화된 '기본 설정(Secure by Default)' 상태를 유지해야 합니다. 제조사는 제품의 공격면(Attack Surface)을 최소화하기 위해 안전하지 않은 기능이 기본으로 작동하지 않도록 설계 및 구현해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #137 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견되는 보안 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 적시에 제공해야 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:20:36 (원문 시간대 미표기)
- 원문: [commit bdbe7d33694e4b97ee74d8307d1b41fb39ddc04c](https://github.com/useformotor3/ai-discord-bot/commit/bdbe7d33694e4b97ee74d8307d1b41fb39ddc04c) | [research_archive/2026-11-15_112036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_112036.md) | commit UTC: 2026-11-15T11:20:52.000Z
- 원문 blob SHA: c30cf50fd9883d07788706bc932ae2cf6006cb2d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견되는 보안 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 적시에 제공해야 합니다. 이는 공장 자동화 시스템의 단일 장애점(SPOF)이 될 수 있는 모터 제어기의 생명주기 전반에 걸친 지속적인 보안성
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #138 — P1 — 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by default) 상태여야 하며, 이를 검증하기 위한 공격 표면 최소화 조치가 강제됩니다. 제
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:25:34 (원문 시간대 미표기)
- 원문: [commit b90760234769c3d35dc81a1f89f40c26a1725e46](https://github.com/useformotor3/ai-discord-bot/commit/b90760234769c3d35dc81a1f89f40c26a1725e46) | [research_archive/2026-11-15_112534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_112534.md) | commit UTC: 2026-11-15T11:25:52.000Z
- 원문 blob SHA: 534142548b8dbbd742ed4a123e38715418cd6f0d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by default) 상태여야 하며, 이를 검증하기 위한 공격 표면 최소화 조치가 강제됩니다. 제품 작동 중 발생하는 사이버 보안 관련 이벤트 및 결함을 실시간으로 감지하고 기록할 수 있는 내부 로깅 및 모니터링 기능을 필
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #139 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대해 무료로 보안 업데이트(패치)를 제공해야 합니다. 해당 지원 기간 및 조건은 사용자가 제품
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:30:45 (원문 시간대 미표기)
- 원문: [commit 427b765db4d9c0ac20400c8022c3987d51c82e0d](https://github.com/useformotor3/ai-discord-bot/commit/427b765db4d9c0ac20400c8022c3987d51c82e0d) | [research_archive/2026-11-15_113045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_113045.md) | commit UTC: 2026-11-15T11:31:02.000Z
- 원문 blob SHA: 72acc99e00657503400b513812e3c02953dc2576
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대해 무료로 보안 업데이트(패치)를 제공해야 합니다. 해당 지원 기간 및 조건은 사용자가 제품을 구매할 때 명확하게 안내되어야 하며, 이는 CRA 부속서 I에 따른 필수 사이버 보안 요건입니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #140 — P1 — 서보 드라이브 제조사는 제품 출하 시(Out-of-the-box) 사용자 인증, 포트, 인터페이스 등 모든 보안 설정이 가장 안전한 상태(Secure by default)로 기본 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:35:25 (원문 시간대 미표기)
- 원문: [commit 7e6924bc3889fff5c60374d591da280cd90fa39f](https://github.com/useformotor3/ai-discord-bot/commit/7e6924bc3889fff5c60374d591da280cd90fa39f) | [research_archive/2026-11-15_113525.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_113525.md) | commit UTC: 2026-11-15T11:35:42.000Z
- 원문 blob SHA: 2fe1cd4030b069d093f95bdfeb7088d617e29d20
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출하 시(Out-of-the-box) 사용자 인증, 포트, 인터페이스 등 모든 보안 설정이 가장 안전한 상태(Secure by default)로 기본 구성되어야 합니다. 불필요한 서비스, 디버그 포트, 개방형 네트워크 인터페이스는 기본적으로 비활성화되어야 하며, 초기 사용자
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #141 — P0 — 산업용 서보 드라이브 제조사는 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 제공해야 하며, 이를 위한 패치 배포 생명주기
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:40:44 (원문 시간대 미표기)
- 원문: [commit 56e6570c5b72555169a3b5ff9d603f9cf3a12d42](https://github.com/useformotor3/ai-discord-bot/commit/56e6570c5b72555169a3b5ff9d603f9cf3a12d42) | [research_archive/2026-11-15_114044.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_114044.md) | commit UTC: 2026-11-15T11:40:59.000Z
- 원문 blob SHA: ac713c0a26573a02757cad510289bc15e1f17fc2
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 추가 비용(무상) 없이 제공해야 하며, 이를 위한 패치 배포 생명주기 관리 체계를 구축해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #142 — P1 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트, 서비스, 기본 계정이 비활성화된 Secure by Default(기본 설정 보안) 상태를 유지해야 합니다. 제조사는 사용
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:45:34 (원문 시간대 미표기)
- 원문: [commit f92b93a9c4b1a49d6244a90db282a00067ebfd37](https://github.com/useformotor3/ai-discord-bot/commit/f92b93a9c4b1a49d6244a90db282a00067ebfd37) | [research_archive/2026-11-15_114534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_114534.md) | commit UTC: 2026-11-15T11:45:49.000Z
- 원문 blob SHA: 813abba0afec87a3cb5b103e8473325b8f6a2d5e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트, 서비스, 기본 계정이 비활성화된 Secure by Default(기본 설정 보안) 상태를 유지해야 합니다. 제조사는 사용자가 보안 설정을 변경하지 않아도 제품이 안전한 상태로 동작하도록 초기 공격 표면(Attack Surface)을 원천적으로 최
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #143 — P0 — 산업용 서보 드라이브는 초기 출고 시부터 무단 액세스를 방지하는 안전한 기본 설정(Secure by Default) 상태여야 하며, 사용자가 명시적으로 변경하기 전까지는 취약할 수
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:50:39 (원문 시간대 미표기)
- 원문: [commit c4787337278fba4eb2a363d5b012f273ecc4ba9e](https://github.com/useformotor3/ai-discord-bot/commit/c4787337278fba4eb2a363d5b012f273ecc4ba9e) | [research_archive/2026-11-15_115039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_115039.md) | commit UTC: 2026-11-15T11:50:56.000Z
- 원문 blob SHA: a7a2c22a83fadd667000e53ce07859d8bedc6fdf
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시부터 무단 액세스를 방지하는 안전한 기본 설정(Secure by Default) 상태여야 하며, 사용자가 명시적으로 변경하기 전까지는 취약할 수 있는 기능이나 인터페이스가 비활성화되어 있어야 합니다. 또한, 제조사는 제품의 예상 수명 주기 동안 보안 업데이트가 무상으로
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #144 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공해야 합니다. 단종(End-of-Life) 시에도 안
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 11:55:29 (원문 시간대 미표기)
- 원문: [commit 6c67e7072dd0488ebee989e0119603538120d8a4](https://github.com/useformotor3/ai-discord-bot/commit/6c67e7072dd0488ebee989e0119603538120d8a4) | [research_archive/2026-11-15_115529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_115529.md) | commit UTC: 2026-11-15T11:55:45.000Z
- 원문 blob SHA: f9d0c3134448e5c0bb3bccc1b5fa424def1d8f26
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공해야 합니다. 단종(End-of-Life) 시에도 안전한 폐기 및 사후 관리를 위한 명확한 고지 프로세스가 수반되어야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #145 — P1 — 서보 드라이브는 출고 시점부터 모든 관리자 계정에 고유하고 변경 불가능한 강력한 초기 비밀번호를 설정하거나, 최초 접속 시 사용자의 강제 비밀번호 변경을 유도하는 'Secure b
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:00:51 (원문 시간대 미표기)
- 원문: [commit 2ac579d3e69cc6042b5db6094da739bc3033324f](https://github.com/useformotor3/ai-discord-bot/commit/2ac579d3e69cc6042b5db6094da739bc3033324f) | [research_archive/2026-11-15_120051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_120051.md) | commit UTC: 2026-11-15T12:01:08.000Z
- 원문 blob SHA: 779b6b5115c78869d1a878a4f8fb3545b2920883
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 출고 시점부터 모든 관리자 계정에 고유하고 변경 불가능한 강력한 초기 비밀번호를 설정하거나, 최초 접속 시 사용자의 강제 비밀번호 변경을 유도하는 'Secure by Default' 상태를 갖추어야 합니다. 불필요한 네트워크 서비스, 포트, 인터페이스는 기본적으로 비활성화되어 있어야 하며
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #146 — P1 — 서보 드라이브 제조사는 제품 출고 시 잠재적 공격 표면을 최소화하기 위해 'Secure by Default(기본 보안 설정)' 원칙을 적용해야 합니다. 특히, 추측하기 쉬운 하드코
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:05:29 (원문 시간대 미표기)
- 원문: [commit ab7ac101d1f31635baf4044f893840d45fdda97f](https://github.com/useformotor3/ai-discord-bot/commit/ab7ac101d1f31635baf4044f893840d45fdda97f) | [research_archive/2026-11-15_120529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_120529.md) | commit UTC: 2026-11-15T12:05:46.000Z
- 원문 blob SHA: 33732c263c858857de676cb737e8a0aba287b65b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 잠재적 공격 표면을 최소화하기 위해 'Secure by Default(기본 보안 설정)' 원칙을 적용해야 합니다. 특히, 추측하기 쉬운 하드코딩된 공장 초기 비밀번호(Hardcoded Default Credentials) 사용을 전면 금지하고, 사용자가 최초 설치 시
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #147 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 이상) 발견된 보안 취약점을 무상으로 조치하고 보안 업데이트(패치)를 제공해야 합니다. 이를 위해 규정된 지원 기간 동안 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:10:40 (원문 시간대 미표기)
- 원문: [commit 757b470d185930b00ff4f82c8bb843b03d2f222b](https://github.com/useformotor3/ai-discord-bot/commit/757b470d185930b00ff4f82c8bb843b03d2f222b) | [research_archive/2026-11-15_121040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_121040.md) | commit UTC: 2026-11-15T12:10:56.000Z
- 원문 blob SHA: 4954e60726341e29f82c47534e349a9f0bf0673b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 이상) 발견된 보안 취약점을 무상으로 조치하고 보안 업데이트(패치)를 제공해야 합니다. 이를 위해 규정된 지원 기간 동안 최신 상태를 유지할 수 있는 안전한 업데이트 배포 메커니즘과 가용성을 보장해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #148 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 추가 비용 없이(Cost-free) 제공해야 합니다. 사용 중단(End-of-L
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:15:44 (원문 시간대 미표기)
- 원문: [commit 48a8aef68b7c4a3c90c0dc7360ee37debcbd7e2e](https://github.com/useformotor3/ai-discord-bot/commit/48a8aef68b7c4a3c90c0dc7360ee37debcbd7e2e) | [research_archive/2026-11-15_121544.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_121544.md) | commit UTC: 2026-11-15T12:16:02.000Z
- 원문 blob SHA: bce849111d00d84478e2e13d40ce50faf6f0d640
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 추가 비용 없이(Cost-free) 제공해야 합니다. 사용 중단(End-of-Life) 시점 도래 시, 사용자에게 최소 1년 전에 사전 고지하고 안전한 폐기 및 전환 절차를 보장해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #149 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 기간(최소 5년) 동안 발견된 보안 취약점을 무상으로 수정해야 하며, 이를 위한 보안 업데이트(패치)를 지체 없이 제공하고 사용자에게 안전
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:20:37 (원문 시간대 미표기)
- 원문: [commit ef34d5b0ac708112bc9d7408db3c8ab1f35d9db5](https://github.com/useformotor3/ai-discord-bot/commit/ef34d5b0ac708112bc9d7408db3c8ab1f35d9db5) | [research_archive/2026-11-15_122037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_122037.md) | commit UTC: 2026-11-15T12:20:53.000Z
- 원문 blob SHA: cf96a4110757e5102944af99cd0e7b29e4e4222e
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 기간(최소 5년) 동안 발견된 보안 취약점을 무상으로 수정해야 하며, 이를 위한 보안 업데이트(패치)를 지체 없이 제공하고 사용자에게 안전하게 배포할 수 있는 메커니즘을 갖추어야 합니다. 자동화 시스템의 특성을 고려하여, 보안 업데이트 적용이 실시간 모션 제어 및
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #150 — P1 — 핵심 내용 1: 산업용 서보 드라이브는 공장 초기화(Out-of-the-box) 상태를 포함하여 배포 시점에 악성코드나 무단 접근의 위험을 최소화하도록 기본적으로 안전한 상태(Se
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:25:31 (원문 시간대 미표기)
- 원문: [commit 551a8e022382901c2807e8cace52a96f47d9f90d](https://github.com/useformotor3/ai-discord-bot/commit/551a8e022382901c2807e8cace52a96f47d9f90d) | [research_archive/2026-11-15_122531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_122531.md) | commit UTC: 2026-11-15T12:25:48.000Z
- 원문 blob SHA: f58e3813ed1d98bceebdc99da297432391d08fc4
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브는 공장 초기화(Out-of-the-box) 상태를 포함하여 배포 시점에 악성코드나 무단 접근의 위험을 최소화하도록 기본적으로 안전한 상태(Secure by default)로 설정되어야 합니다. 핵심 내용 2: 보안에 필수적이지 않은 외부 인터페이스, 포트, 서비스 및
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #151 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간(최소 5년) 동안 발견된 취약점을 무상으로 처리하고, 보안 업데이트를 사용자에게 지체 없이 안전하게 제공해야 합니다. 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:30:43 (원문 시간대 미표기)
- 원문: [commit bf311ed4d8408a66462098510ffec0b8cb15ce3f](https://github.com/useformotor3/ai-discord-bot/commit/bf311ed4d8408a66462098510ffec0b8cb15ce3f) | [research_archive/2026-11-15_123043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_123043.md) | commit UTC: 2026-11-15T12:30:59.000Z
- 원문 blob SHA: d38cc24d6c650b038436abc0cec4d533e95aca4a
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간(최소 5년) 동안 발견된 취약점을 무상으로 처리하고, 보안 업데이트를 사용자에게 지체 없이 안전하게 제공해야 합니다. 자동화 시스템의 가용성 저하를 방지하기 위해, 업데이트 과정은 시스템 중단을 최소화하고 사용자가 명시적으로 제어할 수 있는 메
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #152 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(Free of charge) 제공해야 하며, 이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:35:30 (원문 시간대 미표기)
- 원문: [commit 46a24922a94f7f60ca08d9fc1cbf354bbbcb2839](https://github.com/useformotor3/ai-discord-bot/commit/46a24922a94f7f60ca08d9fc1cbf354bbbcb2839) | [research_archive/2026-11-15_123530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_123530.md) | commit UTC: 2026-11-15T12:35:46.000Z
- 원문 blob SHA: 9398fe649e70412e053e99072790f7548b5e7da3
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(Free of charge) 제공해야 하며, 이를 위한 체계적인 취약점 공개 및 처리 프로세스를 보장해야 합니다. 이는 산업용 기기의 잠재적 보안 리스크가 공급망 전체로 전
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #153 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 또는 법적 요구 기간) 발견되는 취약점에 대한 보안 업데이트(패치)를 사용자에게 무상으로 제공해야 하며, 안전한 업데이트 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:40:41 (원문 시간대 미표기)
- 원문: [commit 6fc25f1698c3a20e055f0b54b77f417bd0a15207](https://github.com/useformotor3/ai-discord-bot/commit/6fc25f1698c3a20e055f0b54b77f417bd0a15207) | [research_archive/2026-11-15_124041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_124041.md) | commit UTC: 2026-11-15T12:40:59.000Z
- 원문 blob SHA: 59fbffaf5415b705a9583dabd224b0e0f13ff34d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년 또는 법적 요구 기간) 발견되는 취약점에 대한 보안 업데이트(패치)를 사용자에게 무상으로 제공해야 하며, 안전한 업데이트 적용 프로세스를 지원해야 합니다. 이는 CRA Annex I의 필수 보안 요건을 충족하기 위한 핵심 생명주기 관리 의무입니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #154 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대해 추가 비용 없이 보안 업데이트를 제공해야 하며, 사용자가 이를 안전하게 설치할 수 있는 매커니즘을 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:45:36 (원문 시간대 미표기)
- 원문: [commit fd6136556ef9da9afc9141244f4ccec6e4a8ff62](https://github.com/useformotor3/ai-discord-bot/commit/fd6136556ef9da9afc9141244f4ccec6e4a8ff62) | [research_archive/2026-11-15_124536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_124536.md) | commit UTC: 2026-11-15T12:45:53.000Z
- 원문 blob SHA: 54a908e4194b51e023b0559aa5b98a62797c9833
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대해 추가 비용 없이 보안 업데이트를 제공해야 하며, 사용자가 이를 안전하게 설치할 수 있는 매커니즘을 보장해야 합니다. 업데이트 가용성 및 적용 과정에 대한 명확한 정보(Support Period)를 기술 문서 및 사용자에게 투
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #155 — P1 — 서보 드라이브는 초기 출고 시(Out-of-the-box)부터 무단 접근을 방지하는 가장 안전한 상태로 설정되어야 하며(Secure by default), 공격 표면을 최소화하기 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:50:38 (원문 시간대 미표기)
- 원문: [commit fa36ad74af3c1569c0c3e09149e7785d4c1f461e](https://github.com/useformotor3/ai-discord-bot/commit/fa36ad74af3c1569c0c3e09149e7785d4c1f461e) | [research_archive/2026-11-15_125038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_125038.md) | commit UTC: 2026-11-15T12:50:55.000Z
- 원문 blob SHA: c2d013a2b4832d4af1b8227d65a51966c80d0a52
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시(Out-of-the-box)부터 무단 접근을 방지하는 가장 안전한 상태로 설정되어야 하며(Secure by default), 공격 표면을 최소화하기 위해 기본적으로 안전하지 않은 기능이나 불필요한 네트워크 서비스가 비활성화되어야 합니다. 제조사는 제품의 전체 수명주기 동안
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #156 — P1 — 서보 드라이브는 배송 및 초기 설치 시 악성코드 유입 및 무단 조작을 방지하기 위해 네트워크 서비스, 포트, 계정 등 불필요한 공격 표면이 원천 차단된 '기본 설정 보안(Secur
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 12:55:29 (원문 시간대 미표기)
- 원문: [commit ffa246dbf7793e22f3e55ac8155330d32fae9b97](https://github.com/useformotor3/ai-discord-bot/commit/ffa246dbf7793e22f3e55ac8155330d32fae9b97) | [research_archive/2026-11-15_125529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_125529.md) | commit UTC: 2026-11-15T12:55:45.000Z
- 원문 blob SHA: 9cdde08dfae32ac0ffca70ab82fcca41828ad64f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 배송 및 초기 설치 시 악성코드 유입 및 무단 조작을 방지하기 위해 네트워크 서비스, 포트, 계정 등 불필요한 공격 표면이 원천 차단된 '기본 설정 보안(Secure by Default)' 상태로 공급되어야 합니다. 제조사는 제품의 전 생애주기 동안 사용자가 안전한 상태를 손쉽게 유지하고
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #157 — P1 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 제공되어야 합니다. 사용자가
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:00:48 (원문 시간대 미표기)
- 원문: [commit 7b40b380920ee3db33102dc9adf45209ab731823](https://github.com/useformotor3/ai-discord-bot/commit/7b40b380920ee3db33102dc9adf45209ab731823) | [research_archive/2026-11-15_130048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_130048.md) | commit UTC: 2026-11-15T13:01:04.000Z
- 원문 blob SHA: b19d86e4a3ad0267d61546dcfb58be1164dc5d8f
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 제공되어야 합니다. 사용자가 첫 부팅 시 보안 매개변수(비밀번호, 암호화 키 등)를 강제로 변경하도록 유도하여 무단 접근 위험을 원천 차단해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #158 — P1 — 산업용 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 악의적인 조작이나 무단 접근을 방어할 수 있도록 기본 설정(Default) 상태에서 보안이 활성화되어 있어야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:05:39 (원문 시간대 미표기)
- 원문: [commit 356b5442b159d177a557ea67d928510ad9c76159](https://github.com/useformotor3/ai-discord-bot/commit/356b5442b159d177a557ea67d928510ad9c76159) | [research_archive/2026-11-15_130539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_130539.md) | commit UTC: 2026-11-15T13:05:59.000Z
- 원문 blob SHA: c2fda814b1cf16ac58d5829b3530504068d1c705
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 악의적인 조작이나 무단 접근을 방어할 수 있도록 기본 설정(Default) 상태에서 보안이 활성화되어 있어야 합니다. 제조사는 사용되지 않는 불필요한 기능, 인터페이스(예: 디버그 포트, 레거시 통신 프로토콜), 기본 계정 등을 비활
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #159 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(무상으로) 제공해야 합니다. 또한, 제품의 지원 종료 시점(E
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:10:38 (원문 시간대 미표기)
- 원문: [commit 1842b923ee9fc2d3690d8722d84d7727c8d99342](https://github.com/useformotor3/ai-discord-bot/commit/1842b923ee9fc2d3690d8722d84d7727c8d99342) | [research_archive/2026-11-15_131038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_131038.md) | commit UTC: 2026-11-15T13:10:53.000Z
- 원문 blob SHA: ec3f91725d1e0d49c3c23705cfb33bf975c370ba
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(무상으로) 제공해야 합니다. 또한, 제품의 지원 종료 시점(EOL)과 이에 따른 보안 지원 계획을 시장 출시 시점에 명확히 공개하여야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #160 — P1 — 서보 드라이브 제조사는 제품 출고 시 기본적으로 무단 접근을 방지하는 안전한 설정(Secure by default)을 적용해야 하며, 원치 않는 네트워크 접속이나 기능 활성화를 최
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:15:32 (원문 시간대 미표기)
- 원문: [commit aeda2561f508d12f21be747615f517cb51f0d0b0](https://github.com/useformotor3/ai-discord-bot/commit/aeda2561f508d12f21be747615f517cb51f0d0b0) | [research_archive/2026-11-15_131532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_131532.md) | commit UTC: 2026-11-15T13:15:48.000Z
- 원문 blob SHA: fd58dd286d21029d209d9734cb29c053bd021a0b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 기본적으로 무단 접근을 방지하는 안전한 설정(Secure by default)을 적용해야 하며, 원치 않는 네트워크 접속이나 기능 활성화를 최소화하여 공격 표면을 줄여야 합니다. 사용자가 보안 설정을 변경하지 않더라도, 최초 부팅 시점부터 높은 수준의 사이버 회복력(
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #161 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공해야 합니다. 해당 지원 기간 및 종료일에 대한 명확한 정보를 제품
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:20:39 (원문 시간대 미표기)
- 원문: [commit 48d7d8d9ee84cbb45a97716eb2ad8f47470f83d7](https://github.com/useformotor3/ai-discord-bot/commit/48d7d8d9ee84cbb45a97716eb2ad8f47470f83d7) | [research_archive/2026-11-15_132039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_132039.md) | commit UTC: 2026-11-15T13:20:56.000Z
- 원문 blob SHA: 41864b0743fc0e860151783fcf67f17fbe7e087d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공해야 합니다. 해당 지원 기간 및 종료일에 대한 명확한 정보를 제품과 기술 문서에 투명하게 공개하여 산업용 시스템 통합업체(System Integrator)가 생명주기 관리를 할 수 있도록 보
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #162 — P1 — 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 네트워크 서비스와 인터페이스가 비활성화된 'Secure by default' 상태여야 하며, 인증되지 않은
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:25:38 (원문 시간대 미표기)
- 원문: [commit c24eb67ef1f914bf96c57df36796ca2427db491e](https://github.com/useformotor3/ai-discord-bot/commit/c24eb67ef1f914bf96c57df36796ca2427db491e) | [research_archive/2026-11-15_132538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_132538.md) | commit UTC: 2026-11-15T13:25:54.000Z
- 원문 blob SHA: 4db32da7749f98a9e51d9ed0d25f51513fddd7ba
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 네트워크 서비스와 인터페이스가 비활성화된 'Secure by default' 상태여야 하며, 인증되지 않은 접근을 방지하는 안전한 초기 설정 메커니즘을 제공해야 합니다. 제조사는 사용자가 보안 설정을 변경할 수 있는 권한을 제공하되
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #163 — P0 — 서보 드라이브는 공장 자동화의 핵심 부품으로서 초기 출고 시 악용 가능한 기능이 차단된 기본 설정(Secure by Default) 상태여야 합니다. 또한, 보안 업데이트 과정에서
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:30:46 (원문 시간대 미표기)
- 원문: [commit 89a7524870ecd5ae904579a8dc6ddd9b626a3618](https://github.com/useformotor3/ai-discord-bot/commit/89a7524870ecd5ae904579a8dc6ddd9b626a3618) | [research_archive/2026-11-15_133046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_133046.md) | commit UTC: 2026-11-15T13:31:02.000Z
- 원문 blob SHA: a4c54792a8ad2bc852fff696edc97384e770660b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 자동화의 핵심 부품으로서 초기 출고 시 악용 가능한 기능이 차단된 기본 설정(Secure by Default) 상태여야 합니다. 또한, 보안 업데이트 과정에서 실시간 모션 제어의 안전성(Safety)과 실시간성(Real-time performance)이 저해되지 않도록 설계 및 배포
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #164 — P1 — 서보 드라이브 제조사는 제품 출고 시 무단 접근을 방지하기 위해 가장 안전한 상태로 초기 설정(Secure by default)되어야 하며, 불필요한 공장 출고 시 기본 계정(De
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:35:31 (원문 시간대 미표기)
- 원문: [commit 44e189af158733bde9c8779068452026943043a0](https://github.com/useformotor3/ai-discord-bot/commit/44e189af158733bde9c8779068452026943043a0) | [research_archive/2026-11-15_133531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_133531.md) | commit UTC: 2026-11-15T13:35:49.000Z
- 원문 blob SHA: fe2eafb93c53b85511175ff3538f8705a03f2db9
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 무단 접근을 방지하기 위해 가장 안전한 상태로 초기 설정(Secure by default)되어야 하며, 불필요한 공장 출고 시 기본 계정(Default accounts)이나 개방된 포트가 제거 또는 비활성화되어야 합니다. 또한, 프로세스 제어 및 파라미터 튜닝을 위한
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #165 — P1 — 서보 드라이브는 공장 출하 시(Out-of-the-box)부터 인증되지 않은 접근, 불필요한 포트 및 서비스가 차단된 'Secure by Default' 상태여야 합니다. 제조사는
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:40:38 (원문 시간대 미표기)
- 원문: [commit 6af54b49e0c1c1bd7baeabb378ffb7ec255f173e](https://github.com/useformotor3/ai-discord-bot/commit/6af54b49e0c1c1bd7baeabb378ffb7ec255f173e) | [research_archive/2026-11-15_134038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_134038.md) | commit UTC: 2026-11-15T13:40:54.000Z
- 원문 blob SHA: c35288754fbb90fe6ad44fbada31dea99d64f903
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출하 시(Out-of-the-box)부터 인증되지 않은 접근, 불필요한 포트 및 서비스가 차단된 'Secure by Default' 상태여야 합니다. 제조사는 사용자가 제품을 최초 설치·구성할 때 보안 설정(초기 비밀번호 변경, 통신 프로토콜 암호화 등)을 강제하거나 안전한 기본값으
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #166 — P1 — 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 사용자 개입 없이도 가장 안전한 상태로 설정(Secure by default)되어 있어야 합니다. 핵심 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:45:35 (원문 시간대 미표기)
- 원문: [commit 9deeb9dfd1b271a9aa818a62bf016fcecc39c42a](https://github.com/useformotor3/ai-discord-bot/commit/9deeb9dfd1b271a9aa818a62bf016fcecc39c42a) | [research_archive/2026-11-15_134535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_134535.md) | commit UTC: 2026-11-15T13:45:52.000Z
- 원문 blob SHA: ed46025948a791a25f8f3c9d06673b0cf0370541
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브는 공장 출고 시(Out-of-the-box) 사용자 개입 없이도 가장 안전한 상태로 설정(Secure by default)되어 있어야 합니다. 핵심 내용 2: 사용자가 무단으로 보안 기능을 해제하거나 임의로 등급을 낮추는 것을 기술적으로 방지하거나 경고해야 합니다. --
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #167 — P0 — CRA Annex I(필수 보안 요건)에 의거하여, 서보 드라이브 제조사는 발견된 취약점을 효과적으로 처리할 수 있는 취약점 공개 정책을 수립하고, 최소 5년 또는 제품의 예상 사
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:50:35 (원문 시간대 미표기)
- 원문: [commit 64a6191ee212dc7a974c1a8c4f80f9e94f3dd558](https://github.com/useformotor3/ai-discord-bot/commit/64a6191ee212dc7a974c1a8c4f80f9e94f3dd558) | [research_archive/2026-11-15_135035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_135035.md) | commit UTC: 2026-11-15T13:50:52.000Z
- 원문 blob SHA: ff77b4460891efda6902696a1b545856eec130f2
- 핵심 주장 주제(원문 요약 첫 부분): CRA Annex I(필수 보안 요건)에 의거하여, 서보 드라이브 제조사는 발견된 취약점을 효과적으로 처리할 수 있는 취약점 공개 정책을 수립하고, 최소 5년 또는 제품의 예상 사용 기간 동안 보안 업데이트를 무상으로 제공해야 합니다. 이를 통해 산업용 자동화 시스템 운용 중 제로데이 및 공표된 취약점이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #168 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 정보, 통신 포트, 서비스 등이 사용자 개입 없이 안전하게 설정된 '기본 안전(Secure by defaul
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 13:55:35 (원문 시간대 미표기)
- 원문: [commit e94cd10b2f7c37475b8b26c3614f143ef92110b1](https://github.com/useformotor3/ai-discord-bot/commit/e94cd10b2f7c37475b8b26c3614f143ef92110b1) | [research_archive/2026-11-15_135535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_135535.md) | commit UTC: 2026-11-15T13:55:51.000Z
- 원문 blob SHA: 5df73cb075fe97be1c3b9539835f1ce40ff3f508
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 정보, 통신 포트, 서비스 등이 사용자 개입 없이 안전하게 설정된 '기본 안전(Secure by default)' 상태를 유지해야 하며, 사용자가 이를 안전하게 변경할 수 있는 메커니즘을 제공해야 합니다. 이는 CRA Annex I에
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #169 — P0 — 핵심 내용 1: 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간 동안(최소 5년) 발견된 보안 취약점에 대한 패치와 업데이트를 이용자에게 무상(Free of charg
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:00:51 (원문 시간대 미표기)
- 원문: [commit 8ca1c537bcbf26ef0a57d668f5e7b29fac94cdf5](https://github.com/useformotor3/ai-discord-bot/commit/8ca1c537bcbf26ef0a57d668f5e7b29fac94cdf5) | [research_archive/2026-11-15_140051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_140051.md) | commit UTC: 2026-11-15T14:01:13.000Z
- 원문 blob SHA: a5e3f6bfb33fb3783a1bc5310396ddea96f90521
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간 동안(최소 5년) 발견된 보안 취약점에 대한 패치와 업데이트를 이용자에게 무상(Free of charge)으로 제공해야 합니다. 핵심 내용 2: 보안 업데이트는 기능 개선과 명확히 분리되어 제공되어야 하며, 업데이트 가용성에 대
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #170 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box), 사용자가 별도의 복잡한 보안 설정을 하지 않아도 무단 접근 및 공격 표면을 원천 차단할 수 있도록 가
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:05:31 (원문 시간대 미표기)
- 원문: [commit 06de52fdd4d6e217d3bd002c897466c0b14d1150](https://github.com/useformotor3/ai-discord-bot/commit/06de52fdd4d6e217d3bd002c897466c0b14d1150) | [research_archive/2026-11-15_140531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_140531.md) | commit UTC: 2026-11-15T14:05:48.000Z
- 원문 blob SHA: 2e638fae9d9c0522cb66af3113682fd435584964
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box), 사용자가 별도의 복잡한 보안 설정을 하지 않아도 무단 접근 및 공격 표면을 원천 차단할 수 있도록 가장 안전한 기본 설정(Secure by default) 상태로 공급해야 합니다. 또한, 불필요한 기본 계정, 개방형 포트, 디
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #171 — P0 — 서보 드라이브 제조사는 CRA 규정에 따라 제품의 예상 수명 주기 동안 발견된 취약점을 무상으로(free of charge) 보안 업데이트 형태로 즉시 수정 및 배포해야 합니다. 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:10:40 (원문 시간대 미표기)
- 원문: [commit 034f3402ed2db527d9fc28665d8c8ced04f2ce84](https://github.com/useformotor3/ai-discord-bot/commit/034f3402ed2db527d9fc28665d8c8ced04f2ce84) | [research_archive/2026-11-15_141040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_141040.md) | commit UTC: 2026-11-15T14:10:57.000Z
- 원문 blob SHA: 5e221233f0c357c9a97f902130be433fa968f7e7
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA 규정에 따라 제품의 예상 수명 주기 동안 발견된 취약점을 무상으로(free of charge) 보안 업데이트 형태로 즉시 수정 및 배포해야 합니다. 이는 제조사가 사용자에게 추가 비용을 청구하거나 유지보수 계약을 빌개로 보안 패치 제공을 거부할 수 없음을 명시하여, 산업용
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #172 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 보안 취약점을 무상으로 조치할 수 있는 보안 업데이트(패치)를 지체 없이 제공해야 하며, 이를 위한 취약점 처리 및 공개
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:15:43 (원문 시간대 미표기)
- 원문: [commit 87fefa488c326768a43a20095ea875eca5a88cac](https://github.com/useformotor3/ai-discord-bot/commit/87fefa488c326768a43a20095ea875eca5a88cac) | [research_archive/2026-11-15_141543.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_141543.md) | commit UTC: 2026-11-15T14:16:07.000Z
- 원문 blob SHA: dea5038e0541227320095971c989b0a880684e97
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견된 보안 취약점을 무상으로 조치할 수 있는 보안 업데이트(패치)를 지체 없이 제공해야 하며, 이를 위한 취약점 처리 및 공개 정책을 수립해야 합니다. 이는 사용자의 별도 비용 부담 없이 OT(운영 기술) 환경의 지속적인 무결성과 가용성을 보장하기 위
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #173 — P0 — 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 취약점에 대해 사용자에게 추가 비용 부과 없이 보안 업데이트(패치)를 무상으로 제공해야 하며, 이를 안전하게 배포하고 사용자가
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:20:35 (원문 시간대 미표기)
- 원문: [commit 50e6b5681d808a7ea57774840f0882a32d24ed6b](https://github.com/useformotor3/ai-discord-bot/commit/50e6b5681d808a7ea57774840f0882a32d24ed6b) | [research_archive/2026-11-15_142035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_142035.md) | commit UTC: 2026-11-15T14:20:52.000Z
- 원문 blob SHA: 479bf42289cb1269d6fcf7453c1e32d29819732a
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 취약점에 대해 사용자에게 추가 비용 부과 없이 보안 업데이트(패치)를 무상으로 제공해야 하며, 이를 안전하게 배포하고 사용자가 자동 또는 수동으로 적용할 수 있는 메커니즘을 갖추어야 합니다. 이는 CRA Annex I의 필수 사이버 보안 요구사항 중
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #174 — P1 — 서보 드라이브 초기 출고 시 변경 가능한 기본 비밀번호나 기설정된 범용 인증 정보를 배제하고, 설치 과정에서 사용자가 고유한 비밀번호를 강제로 설정하도록 하거나 제품 고유의 안전한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:25:30 (원문 시간대 미표기)
- 원문: [commit 657b2ed912beb7a9abb04a021b18d7aef80be3ee](https://github.com/useformotor3/ai-discord-bot/commit/657b2ed912beb7a9abb04a021b18d7aef80be3ee) | [research_archive/2026-11-15_142530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_142530.md) | commit UTC: 2026-11-15T14:25:47.000Z
- 원문 blob SHA: 647aad9a2d5bda400cac51fc1cc8fa4a1fd22dc7
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 초기 출고 시 변경 가능한 기본 비밀번호나 기설정된 범용 인증 정보를 배제하고, 설치 과정에서 사용자가 고유한 비밀번호를 강제로 설정하도록 하거나 제품 고유의 안전한 초기 상태를 보장해야 합니다. 제조업체는 제품이 무단 접근으로부터 보호되는 '기본 보안(Secure by default)'
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #175 — P1 — 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 포트, 서비스, 기본 계정이 비활성화되거나 변경된 상태여야 합니다. 제조사는 제품의 공격 표면을 최소화하고
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:30:51 (원문 시간대 미표기)
- 원문: [commit d5aedcd34e9df245ec4844c386ce0d99486fc683](https://github.com/useformotor3/ai-discord-bot/commit/d5aedcd34e9df245ec4844c386ce0d99486fc683) | [research_archive/2026-11-15_143051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_143051.md) | commit UTC: 2026-11-15T14:31:06.000Z
- 원문 blob SHA: 7fb1638e48c7449d5480616bd909699559760b93
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 불필요한 포트, 서비스, 기본 계정이 비활성화되거나 변경된 상태여야 합니다. 제조사는 제품의 공격 표면을 최소화하고, 사용자가 명시적으로 활성화하기 전까지는 안전한 기본값(Secure by default)을 유지하도록 설계해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #176 — P1 — 서보 드라이브 제조사는 제품을 시장에 출시할 때 안전한 기본 상태(Secure by default)로 설정해야 하며, 특히 변경 가능한 기본 인증 정보(비밀번호 등)나 예기치 않은
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:35:29 (원문 시간대 미표기)
- 원문: [commit be1fab434e1d867422fa2b5ead5a93c46e66d415](https://github.com/useformotor3/ai-discord-bot/commit/be1fab434e1d867422fa2b5ead5a93c46e66d415) | [research_archive/2026-11-15_143529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_143529.md) | commit UTC: 2026-11-15T14:35:46.000Z
- 원문 blob SHA: 7b22f27401b7f651dfda6d0f4c52baa9c98246cc
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품을 시장에 출시할 때 안전한 기본 상태(Secure by default)로 설정해야 하며, 특히 변경 가능한 기본 인증 정보(비밀번호 등)나 예기치 않은 네트워크 서비스가 기본 활성화되어 있는 상태로 출고하는 것을 엄격히 금지합니다. 사용자가 최초 전원을 켤 때 고유하고 강력한
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #177 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 안전하게 접수할 수 있는 공정(Vulnerability Handling)을 갖추어야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:40:36 (원문 시간대 미표기)
- 원문: [commit 2a25d7f4bf1b938896563adfd7177815d6858cc4](https://github.com/useformotor3/ai-discord-bot/commit/2a25d7f4bf1b938896563adfd7177815d6858cc4) | [research_archive/2026-11-15_144036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_144036.md) | commit UTC: 2026-11-15T14:40:53.000Z
- 원문 blob SHA: 88e1af738fc03780cd7533fd38c14f6ec2e8ea8b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 안전하게 접수할 수 있는 공정(Vulnerability Handling)을 갖추어야 합니다. 또한, 발견된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이(Free of charge) 적시에 제공해
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #178 — P1 — 서보 드라이브 제조사는 제품 출시 시점에 악의적인 조작을 방지하기 위해 기본적으로 안전한 설정(Secure by default)을 적용해야 하며, 보안에 영향을 미치는 불필요한 기
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:45:35 (원문 시간대 미표기)
- 원문: [commit d143977ef7c3db69d738575b9f4bdcce475c4973](https://github.com/useformotor3/ai-discord-bot/commit/d143977ef7c3db69d738575b9f4bdcce475c4973) | [research_archive/2026-11-15_144535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_144535.md) | commit UTC: 2026-11-15T14:46:06.000Z
- 원문 blob SHA: 7f5b7b68d5ba2dcde7e856cc761d51677a73698a
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출시 시점에 악의적인 조작을 방지하기 위해 기본적으로 안전한 설정(Secure by default)을 적용해야 하며, 보안에 영향을 미치는 불필요한 기능 및 서비스(Attack Surface)를 기본적으로 비활성화해야 합니다. 사용자가 보안 설정을 변경하거나 초기화할 때 위험
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #179 — P1 — 서보 드라이브는 공장 출고 시점부터 불필요한 기능, 인터페이스, 기본 계정 등이 비활성화되어 있어야 하며, 사용자가 명시적으로 활성화하기 전까지는 잠재적 공격면이 최소화된 'Sec
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:50:35 (원문 시간대 미표기)
- 원문: [commit c746ec867b609b694c933fec25497c9c40bf8827](https://github.com/useformotor3/ai-discord-bot/commit/c746ec867b609b694c933fec25497c9c40bf8827) | [research_archive/2026-11-15_145035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_145035.md) | commit UTC: 2026-11-15T14:50:52.000Z
- 원문 blob SHA: 43f1906d3b081c7fa99c0d1aba0118fcfaf96374
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시점부터 불필요한 기능, 인터페이스, 기본 계정 등이 비활성화되어 있어야 하며, 사용자가 명시적으로 활성화하기 전까지는 잠재적 공격면이 최소화된 'Secure by Default' 상태를 유지해야 합니다. 또한, 제조업체는 보안 관련 설정 변경 시 시스템 무결성이 저해되지 않도
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #180 — P0 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 외부 무단 접근을 방지하기 위해 안전한 기본 설정으로 구성되어야 하며, 모든 불필요한 네트워크 인터페이스와 기본 관리자 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 14:55:28 (원문 시간대 미표기)
- 원문: [commit 57a27881d77e87eec8df4fb59ccfb306a6e4bb69](https://github.com/useformotor3/ai-discord-bot/commit/57a27881d77e87eec8df4fb59ccfb306a6e4bb69) | [research_archive/2026-11-15_145528.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_145528.md) | commit UTC: 2026-11-15T14:55:51.000Z
- 원문 blob SHA: 5610fec6f4e6987f6353cc724b1715135fbe1e79
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 외부 무단 접근을 방지하기 위해 안전한 기본 설정으로 구성되어야 하며, 모든 불필요한 네트워크 인터페이스와 기본 관리자 계정은 비활성화 또는 사용자 지정 강제화 과정을 거쳐야 합니다. 제조사는 제품의 수명주기 동안 규정된 지원 기간(최소 5년)
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #181 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근 및 악용을 방지하기 위해 가장 안전한 상태로 설정된 기본값(Secure by default)을 제공해야 합니다. 사용자가
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:00:51 (원문 시간대 미표기)
- 원문: [commit e80efdca8920db91cadfcc1fe2bf903d67f61ea3](https://github.com/useformotor3/ai-discord-bot/commit/e80efdca8920db91cadfcc1fe2bf903d67f61ea3) | [research_archive/2026-11-15_150051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_150051.md) | commit UTC: 2026-11-15T15:01:08.000Z
- 원문 blob SHA: 9356dca7b5207fa991e0e065fa5ead3444366edf
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때 무단 접근 및 악용을 방지하기 위해 가장 안전한 상태로 설정된 기본값(Secure by default)을 제공해야 합니다. 사용자가 최초 부팅 시 고유한 비밀번호 변경 등을 강제하도록 설계되어야 하며, 불필요한 서비스나 인터페이스는 기본적으로 비활성화되어
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #182 — P1 — 서보 드라이브는 제조 단계부터 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 공급되어야 합니다. 사용자가 최초 설치 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:05:33 (원문 시간대 미표기)
- 원문: [commit 34cb502c75ffb87afdd69cc2d21f6dc3c97c6373](https://github.com/useformotor3/ai-discord-bot/commit/34cb502c75ffb87afdd69cc2d21f6dc3c97c6373) | [research_archive/2026-11-15_150533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_150533.md) | commit UTC: 2026-11-15T15:05:58.000Z
- 원문 blob SHA: 1716e2168aa4dbc5ef3db32662265d0877a327ba
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 제조 단계부터 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태로 공급되어야 합니다. 사용자가 최초 설치 시 보안 설정을 강제로 변경하도록 유도하여 산업용 네트워크의 초기 공격 표면을 원천 차단해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #183 — P1 — 서보 드라이브는 공장 출하 시(Out-of-the-box) 모든 불필요한 네트워크 서비스, 포트, 디버그 인터페이스가 비활성화된 'Secure by Default' 상태여야 합니다
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:10:45 (원문 시간대 미표기)
- 원문: [commit fdf99f24600e0f8a547b15a742ca69f35be3baf7](https://github.com/useformotor3/ai-discord-bot/commit/fdf99f24600e0f8a547b15a742ca69f35be3baf7) | [research_archive/2026-11-15_151045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_151045.md) | commit UTC: 2026-11-15T15:11:10.000Z
- 원문 blob SHA: 11a734aaec776b9163ce8f1832cb655930964c9b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출하 시(Out-of-the-box) 모든 불필요한 네트워크 서비스, 포트, 디버그 인터페이스가 비활성화된 'Secure by Default' 상태여야 합니다. 제조사는 사용자가 보안 위험을 인지하지 못한 상태에서 제품을 운용하지 않도록, 초기 인증 정보 변경 강제 및 공격 표면 최
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #184 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 권한 없는 접근을 차단하기 위해 기본적으로 안전한 상태(Secure by default)로 설정되어야 하며, 유추하기 쉬
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:15:37 (원문 시간대 미표기)
- 원문: [commit cd9d1831c2ea5fbd7026da03aad69e9b5dcfd0d3](https://github.com/useformotor3/ai-discord-bot/commit/cd9d1831c2ea5fbd7026da03aad69e9b5dcfd0d3) | [research_archive/2026-11-15_151537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_151537.md) | commit UTC: 2026-11-15T15:15:54.000Z
- 원문 blob SHA: 600d8227f26b7d74aa59488c8ea34fb143109022
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 권한 없는 접근을 차단하기 위해 기본적으로 안전한 상태(Secure by default)로 설정되어야 하며, 유추하기 쉬운 기본 비밀번호(Default passwords)나 불필요하게 활성화된 네트워크 서비스·인터페이스를 원천적으로 제거하거나 사
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #185 — P1 — 서보 드라이브는 초기 출고 시(Out-of-the-box) 인증되지 않은 접근, 불필요한 서비스 및 포트가 비활성화된 '기본 설정 안전(Secure by default)' 상태여야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:20:38 (원문 시간대 미표기)
- 원문: [commit 15493f6cf285af50a781597f31ebc5f53472a648](https://github.com/useformotor3/ai-discord-bot/commit/15493f6cf285af50a781597f31ebc5f53472a648) | [research_archive/2026-11-15_152038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_152038.md) | commit UTC: 2026-11-15T15:20:54.000Z
- 원문 blob SHA: 123287bef848d91af14f189388afc3231f1ef82e
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 초기 출고 시(Out-of-the-box) 인증되지 않은 접근, 불필요한 서비스 및 포트가 비활성화된 '기본 설정 안전(Secure by default)' 상태여야 하며, 공격 표면을 최소화하기 위해 사용자가 보안 구성을 강제할 수 있는 메커니즘을 제공해야 합니다. 또한 보안 관련 설정
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #186 — P1 — 서보 드라이브 제조사는 제품 출고 시(Out-of-the-box) 권한 상승, 불필요한 네트워크 서비스, 디버그 인터페이스 등이 비활성화되거나 안전하게 설정된 '기본 기본 설정(S
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:25:37 (원문 시간대 미표기)
- 원문: [commit cc00ebe4c94323f4e9a79ce6d5160230c56810b9](https://github.com/useformotor3/ai-discord-bot/commit/cc00ebe4c94323f4e9a79ce6d5160230c56810b9) | [research_archive/2026-11-15_152537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_152537.md) | commit UTC: 2026-11-15T15:26:00.000Z
- 원문 blob SHA: 9a8c7a7870050c922020d81844023a8bfd8c2332
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시(Out-of-the-box) 권한 상승, 불필요한 네트워크 서비스, 디버그 인터페이스 등이 비활성화되거나 안전하게 설정된 '기본 기본 설정(Secure by Default)' 상태를 강제해야 합니다. 사용자가 보안 설정을 변경하지 않더라도 잠재적 공격 표면을 최소화할
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #187 — P0 — 핵심 내용 1: 서보 드라이브 제조사는 제품의 예상 수명 동안 최소 5년(또는 제품의 예상 사용 기간) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:30:48 (원문 시간대 미표기)
- 원문: [commit 3af38323c0b402cf2486b4909710bba0bbba2841](https://github.com/useformotor3/ai-discord-bot/commit/3af38323c0b402cf2486b4909710bba0bbba2841) | [research_archive/2026-11-15_153048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_153048.md) | commit UTC: 2026-11-15T15:31:04.000Z
- 원문 blob SHA: ff66ca33ab5698c2ef635a26b822c60ff7e3acea
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브 제조사는 제품의 예상 수명 동안 최소 5년(또는 제품의 예상 사용 기간) 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 합니다. 핵심 내용 2: 보안 업데이트가 제공되는 동안 취약점 공개(Vulnerability Disclosure)와 함께 패치가
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #188 — P0 — 서보 드라이브와 같은 디지털 요소가 포함된 제품은 배송 시 악성 공격 면을 최소화하기 위해 가장 안전한 기본 설정(Secure by default) 상태로 제공되어야 하며, 사용자
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:35:31 (원문 시간대 미표기)
- 원문: [commit 9e66e86949d4c8263b36913a4315941a238bb05e](https://github.com/useformotor3/ai-discord-bot/commit/9e66e86949d4c8263b36913a4315941a238bb05e) | [research_archive/2026-11-15_153531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_153531.md) | commit UTC: 2026-11-15T15:35:47.000Z
- 원문 blob SHA: 52a13a4d2fd82f671474dd29ca0d11481de3cdd4
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브와 같은 디지털 요소가 포함된 제품은 배송 시 악성 공격 면을 최소화하기 위해 가장 안전한 기본 설정(Secure by default) 상태로 제공되어야 하며, 사용자가 변경하지 않는 한 추가 비용 없이 자동으로 보안 업데이트(Security updates)를 설치할 수 있는 메커니즘을 갖추
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #189 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대해 추가 비용(무상) 없이 시기적절한 보안 업데이트(패치)를 배포해야 합니다. 이는 사
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:40:38 (원문 시간대 미표기)
- 원문: [commit 5611e941d3814596ed2c14e741b6b5f76fc0ceaf](https://github.com/useformotor3/ai-discord-bot/commit/5611e941d3814596ed2c14e741b6b5f76fc0ceaf) | [research_archive/2026-11-15_154038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_154038.md) | commit UTC: 2026-11-15T15:40:56.000Z
- 원문 blob SHA: c8305f3987505ae13c1d38135f2d5ae6e610106d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점에 대해 추가 비용(무상) 없이 시기적절한 보안 업데이트(패치)를 배포해야 합니다. 이는 사용자(시스템integrator 및 최종 사용자)가 별도의 상용 라이선스나 서비스 계약 없이도 필수적인 보안 패치를 적용하여 산
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #190 — P1 — 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위한 안전한 기본 설정(Secure by default)과 보안 관리자 계정의 강제 변경 메커니즘을 갖추어야 합니다. 제
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:45:35 (원문 시간대 미표기)
- 원문: [commit c96746d9087079edd12b5203f7a623affdde89d0](https://github.com/useformotor3/ai-discord-bot/commit/c96746d9087079edd12b5203f7a623affdde89d0) | [research_archive/2026-11-15_154535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_154535.md) | commit UTC: 2026-11-15T15:45:51.000Z
- 원문 blob SHA: e567354a6b3d94067a09e19127968d746b94e0c2
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위한 안전한 기본 설정(Secure by default)과 보안 관리자 계정의 강제 변경 메커니즘을 갖추어야 합니다. 제조사는 사용자가 제품을 수령한 즉시 추가적인 보안 설정 없이도 최소한의 공격 표면만 노출되도록 초기 구성을 보장해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #191 — P1 — 서보 드라이브 제조사는 제품 출고 시 기본적으로 무단 접근을 방지하는 안전한 설정(Secure by Default)을 적용해야 하며, 특히 고유한 기본 비밀번호 설정 또는 첫 부팅
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:50:38 (원문 시간대 미표기)
- 원문: [commit 0bbd0f4b826b0ea843222ffa71a1061410f67058](https://github.com/useformotor3/ai-discord-bot/commit/0bbd0f4b826b0ea843222ffa71a1061410f67058) | [research_archive/2026-11-15_155038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_155038.md) | commit UTC: 2026-11-15T15:50:55.000Z
- 원문 blob SHA: e6b37673d75177d4e348ec8e1717d6a250110e47
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 기본적으로 무단 접근을 방지하는 안전한 설정(Secure by Default)을 적용해야 하며, 특히 고유한 기본 비밀번호 설정 또는 첫 부팅 시 강제적인 자격 증명(Credential) 변경 메커니즘을 제공해야 합니다. 공장 초기화 상태나 기본 설정 상태에서 취약한
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #192 — P1 — 서보 드라이브 제조사는 제품 출고 시 인증되지 않은 접근, 불필요한 서비스, 기본 패스워드 등 보안 취약점이 제거된 '기본 보안 설정(Secure by default)' 상태를 유
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 15:55:32 (원문 시간대 미표기)
- 원문: [commit 006c04125a8bc9e24a801e3e020e9d92da6e798c](https://github.com/useformotor3/ai-discord-bot/commit/006c04125a8bc9e24a801e3e020e9d92da6e798c) | [research_archive/2026-11-15_155532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_155532.md) | commit UTC: 2026-11-15T15:55:49.000Z
- 원문 blob SHA: 7b809660e0e41e277e133341ea723f2f8a0439e0
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 인증되지 않은 접근, 불필요한 서비스, 기본 패스워드 등 보안 취약점이 제거된 '기본 보안 설정(Secure by default)' 상태를 유지해야 하며, 사용자가 이를 안전하게 변경할 수 있는 초기 메커니즘을 제공해야 합니다. 이는 CRA Annex I의 필수 사이
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #193 — P1 — 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box) 인간이 개입하여 변경하기 전까지 가장 안전한 상태를 유지하도록 기본 설정(Secure by defaul
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:00:48 (원문 시간대 미표기)
- 원문: [commit 38b822206a0e3611993fec4c8b7bf37eda523e79](https://github.com/useformotor3/ai-discord-bot/commit/38b822206a0e3611993fec4c8b7bf37eda523e79) | [research_archive/2026-11-15_160048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_160048.md) | commit UTC: 2026-11-15T16:01:03.000Z
- 원문 blob SHA: 5c9f7de64449d8e1989cf9c0f4a0c9de97a6354b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품이 시장에 출시될 때(Out-of-the-box) 인간이 개입하여 변경하기 전까지 가장 안전한 상태를 유지하도록 기본 설정(Secure by default) 상태로 구성해야 합니다. 불필요한 공격 표면(Attack Surface)을 최소화하기 위해 기본적으로 모든 원격 접속 인
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #194 — P1 — 서보 드라이브 제조사는 제품을 시장에 출시할 때 안전하고 보안이 강화된 초기 상태(Secure by Default)로 설정해야 하며, 특히 인증되지 않은 무단 접근을 방지하기 위해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:05:34 (원문 시간대 미표기)
- 원문: [commit 5ad33337041c6042f2d4fae9cd63e962bcf58543](https://github.com/useformotor3/ai-discord-bot/commit/5ad33337041c6042f2d4fae9cd63e962bcf58543) | [research_archive/2026-11-15_160534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_160534.md) | commit UTC: 2026-11-15T16:05:59.000Z
- 원문 blob SHA: 303992ba142a650041ed8d29023b75ab15eceeff
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품을 시장에 출시할 때 안전하고 보안이 강화된 초기 상태(Secure by Default)로 설정해야 하며, 특히 인증되지 않은 무단 접근을 방지하기 위해 기본 계정의 패스워드 강제 변경 또는 비활성화 기능을 반드시 제공해야 합니다. 또한, 불필요한 기능과 기본 개방 포트를 사전
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #195 — P1 — 산업용 서보 드라이브는 공장 출고 시점부터 모든 불필요한 네트워크 포트, 서비스, 인터페이스가 기본적으로 비활성화(Off)되어 있어야 하며, 초기 관리자 계정의 무작위 패스워드 강
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:10:41 (원문 시간대 미표기)
- 원문: [commit deeebc5d64dbcb8ab1d32d471a8d2b69addac20b](https://github.com/useformotor3/ai-discord-bot/commit/deeebc5d64dbcb8ab1d32d471a8d2b69addac20b) | [research_archive/2026-11-15_161041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_161041.md) | commit UTC: 2026-11-15T16:10:57.000Z
- 원문 blob SHA: 9e9aa3d27655a87ec3cf5d7ca44854f6164e2693
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시점부터 모든 불필요한 네트워크 포트, 서비스, 인터페이스가 기본적으로 비활성화(Off)되어 있어야 하며, 초기 관리자 계정의 무작위 패스워드 강제 또는 사용자 설정 유도를 통해 공격 표면을 최소화해야 합니다. EU CRA 부속서 I(Annex I)에 의거하여, 제품의
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #196 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 시정하고 보안 업데이트를 제공해야 합니다. 또한, 이를 보
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:15:37 (원문 시간대 미표기)
- 원문: [commit 029f7afce80f21e65898f4d59106d5dfe434b0a4](https://github.com/useformotor3/ai-discord-bot/commit/029f7afce80f21e65898f4d59106d5dfe434b0a4) | [research_archive/2026-11-15_161537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_161537.md) | commit UTC: 2026-11-15T16:15:53.000Z
- 원문 blob SHA: 110f873d03605b3d9da6aadb98d56b9c629f2f45
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 시정하고 보안 업데이트를 제공해야 합니다. 또한, 이를 보장하기 위한 패치 배포 메커니즘을 사전에 구축해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #197 — P1 — 산업용 서보 드라이브는 제조 단계에서부터 무단 접근을 방지하기 위해 가장 제한적이고 안전한 상태로 설정(Secure by default)되어 출고되어야 합니다. 특히 사용자 인증을
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:20:39 (원문 시간대 미표기)
- 원문: [commit dc4d61638de797aae75b93a917569a7e26b88ec9](https://github.com/useformotor3/ai-discord-bot/commit/dc4d61638de797aae75b93a917569a7e26b88ec9) | [research_archive/2026-11-15_162039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_162039.md) | commit UTC: 2026-11-15T16:20:55.000Z
- 원문 blob SHA: 2fc1daf8ccb8a99badfdd0d05f92c8b930885d78
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 제조 단계에서부터 무단 접근을 방지하기 위해 가장 제한적이고 안전한 상태로 설정(Secure by default)되어 출고되어야 합니다. 특히 사용자 인증을 위한 초기 비밀번호나 사전 공유 키(Pre-shared keys)는 고정된 값이나 일괄적인 기본값 사용이 엄격히 금지됩니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #198 — P0 — 산업용 서보 드라이브는 초기 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by default)으로 구성되어야 하며, 불필요한 기능 및 기본 자격 증명이 제거되
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:25:35 (원문 시간대 미표기)
- 원문: [commit c8ad09f0d4287f95e72c35932b18e19a71c2d384](https://github.com/useformotor3/ai-discord-bot/commit/c8ad09f0d4287f95e72c35932b18e19a71c2d384) | [research_archive/2026-11-15_162535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_162535.md) | commit UTC: 2026-11-15T16:25:51.000Z
- 원문 blob SHA: d2eb533100da49fa594b4bc3492607e332f1db64
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시점부터 무단 접근을 방지하는 안전한 기본 설정(Secure by default)으로 구성되어야 하며, 불필요한 기능 및 기본 자격 증명이 제거되거나 제한되어야 합니다. 제조업체는 제품의 수명주기 동안 보안 업데이트 및 취약점 패치가 기본적으로 용이하고 안전하게 적용될
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #199 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 추가 비용 청구 없이 안전하고 신속하게 패치할 수 있는 메커니즘을 제공해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:30:45 (원문 시간대 미표기)
- 원문: [commit ee54b9dea3ac1c06cb01ed988c17a848675ba5db](https://github.com/useformotor3/ai-discord-bot/commit/ee54b9dea3ac1c06cb01ed988c17a848675ba5db) | [research_archive/2026-11-15_163045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_163045.md) | commit UTC: 2026-11-15T16:31:00.000Z
- 원문 blob SHA: 4f7e0f93b5d6df5e1b1fdb10a2a6be853c5b5f42
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 추가 비용 청구 없이 안전하고 신속하게 패치할 수 있는 메커니즘을 제공해야 합니다. 보안 업데이트(Security Updates)는 기능 개선 업데이트와 명확히 분리되어야 하며, 공표된 즉시 최종
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #200 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 관리자 계정의 기본 비밀번호 비활성화 또는 고유한 초기 인증 정보 강제 설정 등 '기본 보안 설정(Secure b
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:35:33 (원문 시간대 미표기)
- 원문: [commit cde4bb9c7d3033e82ab20324299b8ea52c0f4e23](https://github.com/useformotor3/ai-discord-bot/commit/cde4bb9c7d3033e82ab20324299b8ea52c0f4e23) | [research_archive/2026-11-15_163533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_163533.md) | commit UTC: 2026-11-15T16:35:49.000Z
- 원문 blob SHA: 2be5bb08b5b3e11af1ed39a53f0b94287aad91c8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 관리자 계정의 기본 비밀번호 비활성화 또는 고유한 초기 인증 정보 강제 설정 등 '기본 보안 설정(Secure by default)' 상태로 제공되어야 합니다. 또한, 사용자가 제품을 안전하게 구성할 수 있는 가이드와 함께 무단 접근을 방
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #201 — P1 — 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 보안 위험이 최소화된 '기본 설정에 따른 안전성(Secure by default)' 상태여야 하며, 사용되지
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:40:35 (원문 시간대 미표기)
- 원문: [commit 71d40fb64cb8f3b98c7ea45b6fe6c42489019be8](https://github.com/useformotor3/ai-discord-bot/commit/71d40fb64cb8f3b98c7ea45b6fe6c42489019be8) | [research_archive/2026-11-15_164035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_164035.md) | commit UTC: 2026-11-15T16:40:51.000Z
- 원문 blob SHA: 68bfdca762f3b2a0e42497beb7a8261594165114
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 모든 보안 위험이 최소화된 '기본 설정에 따른 안전성(Secure by default)' 상태여야 하며, 사용되지 않는 네트워크 인터페이스, 포트, 서비스 및 디폴트 계정은 기본적으로 비활성화되거나 변경을 강제해야 합니다. 이는 CRA A
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #202 — P0 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 정보 변경 강제, 불필요한 서비스 및 포트 비활성화 등 '기본 설정에 따른 안전성(Secure by defa
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:45:34 (원문 시간대 미표기)
- 원문: [commit ee19d8142a7ee8182c61944bb665ce4edc979d84](https://github.com/useformotor3/ai-discord-bot/commit/ee19d8142a7ee8182c61944bb665ce4edc979d84) | [research_archive/2026-11-15_164534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_164534.md) | commit UTC: 2026-11-15T16:45:50.000Z
- 원문 blob SHA: f18b8ebc95c45a7a0b910537795f9539ee5ec462
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 인증 정보 변경 강제, 불필요한 서비스 및 포트 비활성화 등 '기본 설정에 따른 안전성(Secure by default)'을 갖추어야 합니다. 제조사는 제품의 예상 수명 주기 동안 발견된 취약점에 대해 무상으로 보안 업데이트(Securit
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #203 — P1 — 서보 드라이브는 기본적으로 취약점이 악용될 수 있는 기능(예: 불필요한 포트, 서비스, 디버그 인터페이스)이 비활성화된 '안전한 기본 설정(Secure by Default)' 상태
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:50:40 (원문 시간대 미표기)
- 원문: [commit e981702a92f74d62bf0a069b13ad5b7effa60d77](https://github.com/useformotor3/ai-discord-bot/commit/e981702a92f74d62bf0a069b13ad5b7effa60d77) | [research_archive/2026-11-15_165040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_165040.md) | commit UTC: 2026-11-15T16:50:58.000Z
- 원문 blob SHA: 704c0e697fd5c55ba7249fd54719f6536e901ff9
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 기본적으로 취약점이 악용될 수 있는 기능(예: 불필요한 포트, 서비스, 디버그 인터페이스)이 비활성화된 '안전한 기본 설정(Secure by Default)' 상태로 공급되어야 하며, 제조사는 사용자 인증 및 권한 관리를 통해 무단 접근으로부터 제품을 보호해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #98 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점 정보를 사용자에게 투명하게 공개하고, 제품의 예상 수명 동안(최소 5년) 보안 업데이트를 추가 비용 없이(무상으로) 제공해야 합
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:05:36 (원문 시간대 미표기)
- 원문: [commit 9b8da3d1bdee87fb57e29caf7ce96c45d51145a7](https://github.com/useformotor3/ai-discord-bot/commit/9b8da3d1bdee87fb57e29caf7ce96c45d51145a7) | [research_archive/2026-11-15_080536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_080536.md) | commit UTC: 2026-11-15T08:05:53.000Z
- 원문 blob SHA: 994ce18e3edba55d0175e4478a232f9319ae0e28
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점 정보를 사용자에게 투명하게 공개하고, 제품의 예상 수명 동안(최소 5년) 보안 업데이트를 추가 비용 없이(무상으로) 제공해야 합니다. 이는 산업 현장의 레거시 기기가 방치되는 것을 막기 위한 핵심 법적 의무입니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #99 — P1 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 공격 표면을 최소화하기 위해 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Defa
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:10:37 (원문 시간대 미표기)
- 원문: [commit 09894017a5579d07bde8836fd28f9094ae6b65d6](https://github.com/useformotor3/ai-discord-bot/commit/09894017a5579d07bde8836fd28f9094ae6b65d6) | [research_archive/2026-11-15_081037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_081037.md) | commit UTC: 2026-11-15T08:10:53.000Z
- 원문 blob SHA: 815ea220f062d420a8f572487096f01961eab44e
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 공격 표면을 최소화하기 위해 불필요한 포트, 서비스, 기본 계정이 비활성화된 '기본 설정 보안(Secure by Default)' 상태여야 합니다. 특히, 최초 사용 시 관리자 계정의 무차별 대입(Brute-force) 공격을 방지하기 위해 고정
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #100 — P0 — 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 취약점에 대해 무상으로 보안 패치(Updates)를 제공해야 하며, 사용자가 이를 용이하게 적용할 수 있는 메커니즘을 보장해야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 08:15:41 (원문 시간대 미표기)
- 원문: [commit cc3aef91539aacc80e9f110344254682f01cef76](https://github.com/useformotor3/ai-discord-bot/commit/cc3aef91539aacc80e9f110344254682f01cef76) | [research_archive/2026-11-15_081541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_081541.md) | commit UTC: 2026-11-15T08:15:57.000Z
- 원문 blob SHA: b2123d646b808751770b22242f3c5c90524fe8a8
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 지원 기간 동안 발견된 취약점에 대해 무상으로 보안 패치(Updates)를 제공해야 하며, 사용자가 이를 용이하게 적용할 수 있는 메커니즘을 보장해야 합니다. 또한, 취약점 정보가 제조사에 안전하게 신고될 수 있도록 명확한 취약점 공개 정책(Coordinated Vulner
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #219 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명에 걸쳐 최소 5년 동안(또는 제품의 특성에 따른 적절한 기간) 보안 취약점 패치 및 업데이트를 무상으로 제공해야 합니
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:10:35 (원문 시간대 미표기)
- 원문: [commit 03bdab9cd5d7c2ecc88cb9bc8ff5d01cb2564b41](https://github.com/useformotor3/ai-discord-bot/commit/03bdab9cd5d7c2ecc88cb9bc8ff5d01cb2564b41) | [research_archive/2026-11-15_181035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_181035.md) | commit UTC: 2026-11-15T18:10:58.000Z
- 원문 blob SHA: dca5b6d22ff3ed62107e95bd6a0a2664046a17c2
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명에 걸쳐 최소 5년 동안(또는 제품의 특성에 따른 적절한 기간) 보안 취약점 패치 및 업데이트를 무상으로 제공해야 합니다. 이를 위해 구매 시점부터 최종 사용자에게 명확한 지원 기간과 업데이트 메커니즘을 투명하게 고지하고 기술 문서(Techni
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #220 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 시장 사용 기간(Expected Lifetime)을 정의하고, 최소 5년 또는 제품의 예상 수명 중 더 긴 기간 동안 보안 취약점
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:15:38 (원문 시간대 미표기)
- 원문: [commit 44678baf3956dcafc7527001428e1499086e3b7b](https://github.com/useformotor3/ai-discord-bot/commit/44678baf3956dcafc7527001428e1499086e3b7b) | [research_archive/2026-11-15_181538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_181538.md) | commit UTC: 2026-11-15T18:15:55.000Z
- 원문 blob SHA: 6272ac3b7f02d0c16803024b709acf332a929200
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 시장 사용 기간(Expected Lifetime)을 정의하고, 최소 5년 또는 제품의 예상 수명 중 더 긴 기간 동안 보안 취약점 패치 및 업데이트를 무상으로 제공해야 합니다. 또한, 이러한 지원 기간과 업데이트 절차를 사용자에게 명확히 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #221 — P0 — 산업용 서보 드라이브 제조사는 발견된 취약점을 대중과 당국에 투명하게 공개하기 위한 조정된 취약점 공개(Coordinated Vulnerability Disclosure) 정책을 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:20:39 (원문 시간대 미표기)
- 원문: [commit 5f7105653f3a55fe6907bd4a334a5475f8abf8bb](https://github.com/useformotor3/ai-discord-bot/commit/5f7105653f3a55fe6907bd4a334a5475f8abf8bb) | [research_archive/2026-11-15_182039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_182039.md) | commit UTC: 2026-11-15T18:20:56.000Z
- 원문 blob SHA: e05d9a5260a1055a21953ec4c4ea67ee15d376f4
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 발견된 취약점을 대중과 당국에 투명하게 공개하기 위한 조정된 취약점 공개(Coordinated Vulnerability Disclosure) 정책을 수립해야 하며, 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트(패치)를 사용자에게 제
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #222 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 제품의 예상 수명 주기 동안(최소 5년 또는 법적 지원 기간) 추가 비용 없이(Free of ch
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:25:29 (원문 시간대 미표기)
- 원문: [commit ab38111e0bcfdbf47c6f4418cadb1c8aea1a132e](https://github.com/useformotor3/ai-discord-bot/commit/ab38111e0bcfdbf47c6f4418cadb1c8aea1a132e) | [research_archive/2026-11-15_182529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_182529.md) | commit UTC: 2026-11-15T18:25:46.000Z
- 원문 blob SHA: 38d0d0b30bff009a5b76c9dcfb53e59ebccf2fbc
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 제품의 예상 수명 주기 동안(최소 5년 또는 법적 지원 기간) 추가 비용 없이(Free of charge) 최종 사용자에게 제공해야 합니다. 또한, 제3자 보안 연구원 등이 취약점을 안전하게 신고할 수 있는 조율된 취약점
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #223 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 기본 계정, 비밀번호, 불필요한 네트워크 서비스 및 포트가 비활성화되거나 안전하게 설정되어 있어야 합니다. 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:30:48 (원문 시간대 미표기)
- 원문: [commit fd69bc6877de578559549026eefb49379b4db5ea](https://github.com/useformotor3/ai-discord-bot/commit/fd69bc6877de578559549026eefb49379b4db5ea) | [research_archive/2026-11-15_183048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_183048.md) | commit UTC: 2026-11-15T18:31:04.000Z
- 원문 blob SHA: b041264933b02006b0e12c7ca1fded766fde05f1
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 기본 계정, 비밀번호, 불필요한 네트워크 서비스 및 포트가 비활성화되거나 안전하게 설정되어 있어야 합니다. 또한, 제조사는 제품을 시장에 출시하기 전에 알려진 취약점이 존재하지 않도록 보장해야 하는 엄격한 'Secure by Defa
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #224 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex I에 의거하여 제품의 예상 수명 주기 동안 발견된 보안 취약점에 대한 패치와 업데이트를 추가 비용 없이(free of charge)
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:35:32 (원문 시간대 미표기)
- 원문: [commit 239c0cd3d269d2066c55faaaeef791b3f8f21714](https://github.com/useformotor3/ai-discord-bot/commit/239c0cd3d269d2066c55faaaeef791b3f8f21714) | [research_archive/2026-11-15_183532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_183532.md) | commit UTC: 2026-11-15T18:35:48.000Z
- 원문 blob SHA: 38059c50e2ff0b3d8c369387b30f256e9c81c244
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex I에 의거하여 제품의 예상 수명 주기 동안 발견된 보안 취약점에 대한 패치와 업데이트를 추가 비용 없이(free of charge) 제공해야 하며, 최소 지원 기간(Support Period)을 명시하고 사용자에게 투명하게 고지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #225 — P0 — 핵심 내용 1: 제조사는 서보 드라이브의 예상 수명 주기(최소 5년) 또는 관련 법령에 명시된 지원 기간 동안 발견된 보안 취약점을 추가 비용(무상) 없이 시급하게 패치하여 배포해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:40:41 (원문 시간대 미표기)
- 원문: [commit ec1828ac373d9e177665c6644ab4faf840dfff82](https://github.com/useformotor3/ai-discord-bot/commit/ec1828ac373d9e177665c6644ab4faf840dfff82) | [research_archive/2026-11-15_184041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_184041.md) | commit UTC: 2026-11-15T18:40:58.000Z
- 원문 blob SHA: f0ff47c01c3e9c578b16e1d74c1ef0df6e3d2cd3
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 제조사는 서보 드라이브의 예상 수명 주기(최소 5년) 또는 관련 법령에 명시된 지원 기간 동안 발견된 보안 취약점을 추가 비용(무상) 없이 시급하게 패치하여 배포해야 합니다. 핵심 내용 2: 취약점 보안 업데이트는 기능적 업그레이드와 명확히 분리되어야 하며, 시장 출하 직후부터 엔드유저에
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #226 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 중 긴 기간 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 업데이트 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:45:43 (원문 시간대 미표기)
- 원문: [commit a4ea05db00d8b12889b7d5d1e4c090158ce7bae6](https://github.com/useformotor3/ai-discord-bot/commit/a4ea05db00d8b12889b7d5d1e4c090158ce7bae6) | [research_archive/2026-11-15_184543.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_184543.md) | commit UTC: 2026-11-15T18:46:00.000Z
- 원문 blob SHA: 63a60e998a5ec88d1224fb8092ddca2428471477
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 중 긴 기간 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 업데이트 가용성 및 배포 메커니즘을 보장해야 합니다. 이는 산업 현장의 시스템 가용성 유지와 공급망 보안 리스크를 원천 차단하기 위한
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #227 — P0 — 서보 드라이브 제조사는 CRA에 따라 예상되는 제품 수명 주기 동안 발견된 보안 취약점에 대한 보안 업데이트(패치)를 사용 비용 추가 청구 없이 무상으로 제공해야 하며, 이를 위한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:50:46 (원문 시간대 미표기)
- 원문: [commit 2b6ef527d6c61807a97550d5040ce444fa7fb2e0](https://github.com/useformotor3/ai-discord-bot/commit/2b6ef527d6c61807a97550d5040ce444fa7fb2e0) | [research_archive/2026-11-15_185046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_185046.md) | commit UTC: 2026-11-15T18:51:03.000Z
- 원문 blob SHA: df30245b2c6c3a4dc01e1eb7afc394a125c85567
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 예상되는 제품 수명 주기 동안 발견된 보안 취약점에 대한 보안 업데이트(패치)를 사용 비용 추가 청구 없이 무상으로 제공해야 하며, 이를 위한 기술 문서 및 사용자 안내 의무를 다해야 합니다. 또한, 제3자 신고를 통한 취약점 처리를 위해 명확한 조정된 취약점 공표(
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #228 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 사용자에게 자동으로(가능한 경우) 및 무상으로 제공해야 하며, 업데이트 가용성을 알리는 명확한 고지 메커
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:55:31 (원문 시간대 미표기)
- 원문: [commit 99d4b1932b66313534b892bd9d25f7241261ecf1](https://github.com/useformotor3/ai-discord-bot/commit/99d4b1932b66313534b892bd9d25f7241261ecf1) | [research_archive/2026-11-15_185531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_185531.md) | commit UTC: 2026-11-15T18:55:47.000Z
- 원문 blob SHA: 314de97c6e75aac67f188296debe0c811777f943
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 사용자에게 자동으로(가능한 경우) 및 무상으로 제공해야 하며, 업데이트 가용성을 알리는 명확한 고지 메커니즘을 제품 생명주기 동안 보장해야 합니다. 이는 제조사가 사후 보안 패치를 유료 서비스나 선택적 옵션으로 제공하는 관행을 법
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #229 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 시장 사용 기간(Expected Lifetime)을 정의하고, 최소 5년 또는 제품의 예상 수명 기간 중 더 긴 기간 동안 보안 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:00:53 (원문 시간대 미표기)
- 원문: [commit 8ba8038dc6743af2ade2ce24905df85fccc3fff2](https://github.com/useformotor3/ai-discord-bot/commit/8ba8038dc6743af2ade2ce24905df85fccc3fff2) | [research_archive/2026-11-15_190053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_190053.md) | commit UTC: 2026-11-15T19:01:10.000Z
- 원문 blob SHA: d73736e198891c66958224fe153b170dbe71988d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 시장 사용 기간(Expected Lifetime)을 정의하고, 최소 5년 또는 제품의 예상 수명 기간 중 더 긴 기간 동안 보안 취약점 무료 패치를 포함한 지원 의무를 사용자에게 명시적으로 제공해야 합니다. 지원 기간 종료 시점 도달 전이라도, 사용자에게
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #230 — P0 — 핵심 내용 1: CRA에 따라 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년)동안 발견된 취약점에 대해 사용자에게 추가 비용 청구 없이(free-of-charge)
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:05:32 (원문 시간대 미표기)
- 원문: [commit 023d9274c33530955101023f34c2231e8d9144e5](https://github.com/useformotor3/ai-discord-bot/commit/023d9274c33530955101023f34c2231e8d9144e5) | [research_archive/2026-11-15_190532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_190532.md) | commit UTC: 2026-11-15T19:05:48.000Z
- 원문 blob SHA: dc7cb5811fb814df03031f7bf8ba5e3145161f04
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: CRA에 따라 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년)동안 발견된 취약점에 대해 사용자에게 추가 비용 청구 없이(free-of-charge) 보안 업데이트 및 패치를 무상으로 제공해야 합니다. 핵심 내용 2: 이는 상용 라이선스나 유지보수 계약(SLA) 유무와 관계
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #231 — P1 — 서보 드라이브와 같은 실시간 고속 모션 제어 기기는 CRA 부속서 I(Annex I)에 따라 예기치 않은 동작이나 서비스 거부(DoS)를 방지하기 위해 런타임 무결성과 메모리 보호
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:10:35 (원문 시간대 미표기)
- 원문: [commit 46b0036c20c2292a003016a6e066560b6921d829](https://github.com/useformotor3/ai-discord-bot/commit/46b0036c20c2292a003016a6e066560b6921d829) | [research_archive/2026-11-15_191035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_191035.md) | commit UTC: 2026-11-15T19:10:53.000Z
- 원문 blob SHA: 2c46a9b2a926d338c160d99babf71864010716e2
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브와 같은 실시간 고속 모션 제어 기기는 CRA 부속서 I(Annex I)에 따라 예기치 않은 동작이나 서비스 거부(DoS)를 방지하기 위해 런타임 무결성과 메모리 보호 메커니즘을 강제해야 합니다. 본 주제는 제어 루프(Control Loop)의 타이밍 결정론(Determinism)을 훼손하지
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(e)–(f), Part II(2),(7): 기밀성·무결성 및 안전한 업데이트 배포 결과를 확인. Secure Boot/RoT/특정 알고리즘은 법령의 보편적 명시 구현수단이 아닌 설계 후보.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #232 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 생명주기(Expected Lifetime) 또는 최소 5년 중 긴 기간 동안 보안 취약점 패치를 무상으로 제공해야 하며, 지원 종
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:15:41 (원문 시간대 미표기)
- 원문: [commit 5efd5054b4b841cbb661ba45fb81f8e7e112a300](https://github.com/useformotor3/ai-discord-bot/commit/5efd5054b4b841cbb661ba45fb81f8e7e112a300) | [research_archive/2026-11-15_191541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_191541.md) | commit UTC: 2026-11-15T19:15:58.000Z
- 원문 blob SHA: ee25a521bf1b42a564e04507fd85a801b97353ae
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 생명주기(Expected Lifetime) 또는 최소 5년 중 긴 기간 동안 보안 취약점 패치를 무상으로 제공해야 하며, 지원 종료 시점 도래 시 최종 사용자가 인지할 수 있도록 명확하고 시의적절한 사전 통지 및 사후 지원 계획을 수립·공개해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #233 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 중 더 긴 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 하며, 이를 위한 배
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:20:36 (원문 시간대 미표기)
- 원문: [commit c2af1735294293969b340c736e08f36299d3fd57](https://github.com/useformotor3/ai-discord-bot/commit/c2af1735294293969b340c736e08f36299d3fd57) | [research_archive/2026-11-15_192036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_192036.md) | commit UTC: 2026-11-15T19:20:52.000Z
- 원문 blob SHA: bbdf88e2d768099aee49955df4a983dc72d7794d
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 5년 중 더 긴 기간 동안 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 하며, 이를 위한 배포 메커니즘과 수명 주기 종료(End-of-Life, EOL) 정책을 기술 문서에 명시해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #234 — P0 — 핵심 내용 1: 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(At least 5 years) 또는 최소 5년 중 더 긴 기간 동안 발견된 취약점에 대해 추가 비용 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:25:30 (원문 시간대 미표기)
- 원문: [commit 75b35094cc645f0ae1ec65c05b0c837c6fc42e93](https://github.com/useformotor3/ai-discord-bot/commit/75b35094cc645f0ae1ec65c05b0c837c6fc42e93) | [research_archive/2026-11-15_192530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_192530.md) | commit UTC: 2026-11-15T19:25:46.000Z
- 원문 blob SHA: d7f66d6f5a835b1e2bf079c2f16ffd0debe2d000
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(At least 5 years) 또는 최소 5년 중 더 긴 기간 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트 및 패치를 제공해야 합니다. 핵심 내용 2: 보안 업데이트는 기능적 업데
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #235 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안(최소 5년) 발견된 보안 취약점에 대한 무상 보안 업데이트 및 패치를 예외 없이 제공해야 합니다.
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:30:46 (원문 시간대 미표기)
- 원문: [commit 984e54498c0e70162eca5c2ef3ea3d2cd4b72d0d](https://github.com/useformotor3/ai-discord-bot/commit/984e54498c0e70162eca5c2ef3ea3d2cd4b72d0d) | [research_archive/2026-11-15_193046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_193046.md) | commit UTC: 2026-11-15T19:31:03.000Z
- 원문 blob SHA: ea0def52be026ed0b983dc30a95280ac4448623f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안(최소 5년) 발견된 보안 취약점에 대한 무상 보안 업데이트 및 패치를 예외 없이 제공해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #236 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 패치 배포 시 사용자가 쉽게 이해할 수 있는 보안
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:35:29 (원문 시간대 미표기)
- 원문: [commit bce34cf1421d55987a5c7846ec229e1cd147a5ec](https://github.com/useformotor3/ai-discord-bot/commit/bce34cf1421d55987a5c7846ec229e1cd147a5ec) | [research_archive/2026-11-15_193529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_193529.md) | commit UTC: 2026-11-15T19:35:52.000Z
- 원문 blob SHA: 06a4522658aec55d9f9c6cdb64c212c0e90d6fb6
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 패치 배포 시 사용자가 쉽게 이해할 수 있는 보안 권고문(Security Advisory)을 함께 제공해야 합니다. 제조사는 취약점 신고를 위한 명확한 단일 창구(Contac
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #237 — P0 — 핵심 내용: EU CRA 제11조 및 Annex I에 따라 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공하고,
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:40:38 (원문 시간대 미표기)
- 원문: [commit 1a1618de71887f5146169b46d4ba50a98ac1adaa](https://github.com/useformotor3/ai-discord-bot/commit/1a1618de71887f5146169b46d4ba50a98ac1adaa) | [research_archive/2026-11-15_194038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_194038.md) | commit UTC: 2026-11-15T19:40:55.000Z
- 원문 blob SHA: 56814b2aee857bcebb66a0e7da009b0bff7f7f69
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용: EU CRA 제11조 및 Annex I에 따라 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대한 보안 업데이트를 무상으로 제공하고, 수명 종료(End-of-Life) 시 이를 투명하게 공지해야 합니다. 기대 효과: 이는 단순한 초기 인증을 넘어 실질적인 운
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #238 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 즉시 패치해야 하며, 이를 위해 자동화된 보안 업데이트 배포 메커
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:45:35 (원문 시간대 미표기)
- 원문: [commit b877c82db2eadcb6dd93c88ecbeb183359fe0542](https://github.com/useformotor3/ai-discord-bot/commit/b877c82db2eadcb6dd93c88ecbeb183359fe0542) | [research_archive/2026-11-15_194535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_194535.md) | commit UTC: 2026-11-15T19:45:51.000Z
- 원문 blob SHA: 8987a2e2fe1b7fe5c82d53ede14604b889dcee2b
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 즉시 패치해야 하며, 이를 위해 자동화된 보안 업데이트 배포 메커니즘과 취약점 처리 정책을 기술 문서에 명시해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #239 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 부속서 VI에 따라 제품의 설계, 개발, 취약점 평가 과정 및 SBOM을 포함한 상세한 사이버 보안 기술 문서를 작성하고, 이를 시장 출
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:50:41 (원문 시간대 미표기)
- 원문: [commit d608d618eaa734e40ba944031b8574efd53844f8](https://github.com/useformotor3/ai-discord-bot/commit/d608d618eaa734e40ba944031b8574efd53844f8) | [research_archive/2026-11-15_195041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_195041.md) | commit UTC: 2026-11-15T19:50:58.000Z
- 원문 blob SHA: 5bdf2f6417b58daf38ec3ff919d5a4355720179e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 부속서 VI에 따라 제품의 설계, 개발, 취약점 평가 과정 및 SBOM을 포함한 상세한 사이버 보안 기술 문서를 작성하고, 이를 시장 출시 후 최소 10년간 보관해야 합니다. 해당 기술 문서는 서보 드라이브가 CRA의 본질적 요구사항(Annex I)을 충족함을
- 우선순위/검증 쟁점: P0 — EUR-Lex Annex I Part II(1): SBOM은 제조자 취약점 처리 요구이며 최소 top-level dependencies 포함. Annex VII(2)(b) 기술문서와 Annex II(9) 사용자 제공(제조자가 제공 결정 시)을 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #240 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 무료로 보안 업데이트를 제공해야 하며, 특히 산업 현장의 가용성(Availability)을 보장하기 위해 운전 중 무중단
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 19:55:34 (원문 시간대 미표기)
- 원문: [commit bd452130dad97e68cfd839f48afcd63236abf361](https://github.com/useformotor3/ai-discord-bot/commit/bd452130dad97e68cfd839f48afcd63236abf361) | [research_archive/2026-11-15_195534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_195534.md) | commit UTC: 2026-11-15T19:55:51.000Z
- 원문 blob SHA: 3c9dba4ef40e94fa27973201f15490a62b1869b5
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 무료로 보안 업데이트를 제공해야 하며, 특히 산업 현장의 가용성(Availability)을 보장하기 위해 운전 중 무중단으로 안전하게 패치를 적용하고 검증할 수 있는 메커니즘을 기술 문서에 구현해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #241 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 지원 기간(최소 5년)을 명시해야 하며, 해당 기간 동안 보안 업데이트 제공 여부와 지원 종료 시점(EOL)을 시장 출시 단계부터
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:00:50 (원문 시간대 미표기)
- 원문: [commit 79fc894caaf51f1099326b2d8576d6e066550e0a](https://github.com/useformotor3/ai-discord-bot/commit/79fc894caaf51f1099326b2d8576d6e066550e0a) | [research_archive/2026-11-15_200050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_200050.md) | commit UTC: 2026-11-15T20:01:06.000Z
- 원문 blob SHA: c4970994494e73f8d80249b15fdeb7a8eb6e8125
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 지원 기간(최소 5년)을 명시해야 하며, 해당 기간 동안 보안 업데이트 제공 여부와 지원 종료 시점(EOL)을 시장 출시 단계부터 최종 사용자와 수입상에게 투명하게 고지해야 합니다. 이는 산업 현장의 예기치 않은 레거시 장비 방치를 막고 공급망 전체의 보
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #242 — P1 — 서보 드라이브는 시장 출시(Placing on the market) 시점에 사용자 干渉(개입) 없이도 안전하게 작동하도록 기본 설정(Secure by default)되어야 하며, 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:05:28 (원문 시간대 미표기)
- 원문: [commit 388751f93cf281b2be4d3aa8b1a3ff8a866e77c6](https://github.com/useformotor3/ai-discord-bot/commit/388751f93cf281b2be4d3aa8b1a3ff8a866e77c6) | [research_archive/2026-11-15_200528.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_200528.md) | commit UTC: 2026-11-15T20:05:45.000Z
- 원문 blob SHA: de428d395e66cf53b91c669cc494c074f9d2f122
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 시장 출시(Placing on the market) 시점에 사용자 干渉(개입) 없이도 안전하게 작동하도록 기본 설정(Secure by default)되어야 하며, 이를 입증하기 위한 기술 문서(Technical Documentation)에 제3자 오픈소스 및 하드웨어 컴포넌트의 취약성 연
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #243 — P0 — 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점을 무상으로 즉시 패치할 수 있는 자동화된 배포 체계와 안전한 업데이트 생명
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:10:33 (원문 시간대 미표기)
- 원문: [commit a150ed796cbcdc4b2cb60c948f6a02023d517806](https://github.com/useformotor3/ai-discord-bot/commit/a150ed796cbcdc4b2cb60c948f6a02023d517806) | [research_archive/2026-11-15_201033.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_201033.md) | commit UTC: 2026-11-15T20:10:49.000Z
- 원문 blob SHA: 2fb9727c2ad572dbe1f2770b833b56775bec6cf0
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명 또는 최소 5년 동안 발견된 취약점을 무상으로 즉시 패치할 수 있는 자동화된 배포 체계와 안전한 업데이트 생명주기를 보장해야 합니다. 이는 단순히 취약점을 고치는 것을 넘어, 보안 업데이트 과정 자체가 새로운 공격 벡터가 되지 않도록
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #244 — P0 — 핵심 내용 1: 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명(또는 최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트를 안전하게 배포할 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:15:33 (원문 시간대 미표기)
- 원문: [commit a7c872408c3f23b2f01a1c657fe43c533aa54b5f](https://github.com/useformotor3/ai-discord-bot/commit/a7c872408c3f23b2f01a1c657fe43c533aa54b5f) | [research_archive/2026-11-15_201533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_201533.md) | commit UTC: 2026-11-15T20:15:50.000Z
- 원문 blob SHA: a8ed3ec2e3520649ffa5438dde9745b1bb094255
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 예상 수명(또는 최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트를 안전하게 배포할 수 있는 메커니즘을 제공해야 합니다. 핵심 내용 2: 기술 문서(Annex VII)에는 이러한 생명주기 동안의 업데이트 및 구
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #245 — P1 — 서보 드라이브의 핵심인 모션 컨트롤 펌웨어 및 실시간 제어 파라미터(게인 값 등)의 변조를 원천 차단하기 위해, 하드웨어 루트 오브 트러스트(RoT)를 활용한 암호학적 안전한 부팅
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:20:35 (원문 시간대 미표기)
- 원문: [commit bea34e4eaa3e4d8a9dedb13aa760c8ee09cc1933](https://github.com/useformotor3/ai-discord-bot/commit/bea34e4eaa3e4d8a9dedb13aa760c8ee09cc1933) | [research_archive/2026-11-15_202035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_202035.md) | commit UTC: 2026-11-15T20:20:52.000Z
- 원문 blob SHA: 5848cd9d163370a9ac178affefc33d1b8ea7c9ad
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브의 핵심인 모션 컨트롤 펌웨어 및 실시간 제어 파라미터(게인 값 등)의 변조를 원천 차단하기 위해, 하드웨어 루트 오브 트러스트(RoT)를 활용한 암호학적 안전한 부팅(Secure Boot) 및 런타임 무결성 검증 체계를 구축해야 합니다. CRA 부속서 I(Annex I)에 따라 제조사는 제
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(e)–(f), Part II(2),(7): 기밀성·무결성 및 안전한 업데이트 배포 결과를 확인. Secure Boot/RoT/특정 알고리즘은 법령의 보편적 명시 구현수단이 아닌 설계 후보.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #246 — P0 — 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 '예상 사용 수명(Expected Lifetime)'을 자체 산정하여 기술 문서에 명시해야 하며, 해당 기간 동안 발견된
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:25:36 (원문 시간대 미표기)
- 원문: [commit fd1e3b3917088c017f049b1db1846c527fed52bc](https://github.com/useformotor3/ai-discord-bot/commit/fd1e3b3917088c017f049b1db1846c527fed52bc) | [research_archive/2026-11-15_202536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_202536.md) | commit UTC: 2026-11-15T20:25:52.000Z
- 원문 blob SHA: b33866a5e5e67135a49aa63cce241b1ba9cade73
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA Annex I에 따라 제품의 '예상 사용 수명(Expected Lifetime)'을 자체 산정하여 기술 문서에 명시해야 하며, 해당 기간 동안 발견된 취약점에 대해 최소 5년 또는 산정된 수명 기간 중 더 긴 기간 동안 무상 보안 패치 및 지원을 제공해야 합니다. 이는 산업
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #247 — P0 — 서보 드라이브의 펌웨어 업그레이드나 제어 알고리즘 변경 등 '중대한 변경(Substantial Modification)' 발생 시, CRA 규정에 따른 적합성 평가(Conformi
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:30:42 (원문 시간대 미표기)
- 원문: [commit a2b6cd7f5a5dcc2364eaa9bf171b1226154752ea](https://github.com/useformotor3/ai-discord-bot/commit/a2b6cd7f5a5dcc2364eaa9bf171b1226154752ea) | [research_archive/2026-11-15_203042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_203042.md) | commit UTC: 2026-11-15T20:30:58.000Z
- 원문 blob SHA: 2af9f2130d43bf81c1eacf4ea035eea8aed1541f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브의 펌웨어 업그레이드나 제어 알고리즘 변경 등 '중대한 변경(Substantial Modification)' 발생 시, CRA 규정에 따른 적합성 평가(Conformity Assessment)를 재수행하고 기술 문서를 즉시 갱신해야 합니다. 제조사는 제품의 전체 생명주기 동안 이러한 변경 이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 7 및 Annex III: Important Product Class I/II 여부는 제품 명칭이 아니라 Annex III 범주와 core function으로 판정. 서보 드라이브라는 이유만으로 Class II/Notified Body를 단정하지 않음.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #248 — P0 — 서보 드라이브 제조사는 CRA에 따른 보안 업데이트 및 패치 적용 시, 공장 자동화 라인의 실시간 제어 무결성과 가용성(Availability)을 손상시키지 않도록 '무중단/안전한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:35:34 (원문 시간대 미표기)
- 원문: [commit f99b1dd08a8bca933033fcfefa9930c8dc477a34](https://github.com/useformotor3/ai-discord-bot/commit/f99b1dd08a8bca933033fcfefa9930c8dc477a34) | [research_archive/2026-11-15_203534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_203534.md) | commit UTC: 2026-11-15T20:35:51.000Z
- 원문 blob SHA: 2f383faba28ba2b0614e5a9ce3f7e65b592823d0
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따른 보안 업데이트 및 패치 적용 시, 공장 자동화 라인의 실시간 제어 무결성과 가용성(Availability)을 손상시키지 않도록 '무중단/안전한 롤백(Rollback) 및 이중화(A/B 파티션) 펌웨어 업데이트 아키텍처'를 강제해야 합니다. 패치 적용 실패나 오작동 시
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #249 — P0 — 서보 드라이브 제조사는 단순히 소프트웨어 목록을 나열하는 것을 넘어, 하드웨어 구성요소와 오픈소스/상용 라이브러리 간의 종속 관계가 정밀하게 매핑된 기계 판독 가능(machine-
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:40:40 (원문 시간대 미표기)
- 원문: [commit e3cd44179e88e609307de359b3603b60cb6a7197](https://github.com/useformotor3/ai-discord-bot/commit/e3cd44179e88e609307de359b3603b60cb6a7197) | [research_archive/2026-11-15_204040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_204040.md) | commit UTC: 2026-11-15T20:40:57.000Z
- 원문 blob SHA: 4ad6412969d8d3a2deaf1946931889993e770607
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 단순히 소프트웨어 목록을 나열하는 것을 넘어, 하드웨어 구성요소와 오픈소스/상용 라이브러리 간의 종속 관계가 정밀하게 매핑된 기계 판독 가능(machine-readable) 형태의 세부 SBOM을 제공해야 하며, 이를 통해 제품 생명주기 동안 발견되는 취약점이 서보 제어 루프나 실
- 우선순위/검증 쟁점: P0 — EUR-Lex Annex I Part II(1): SBOM은 제조자 취약점 처리 요구이며 최소 top-level dependencies 포함. Annex VII(2)(b) 기술문서와 Annex II(9) 사용자 제공(제조자가 제공 결정 시)을 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #250 — P0 — 서보 드라이브 제조사는 규정된 생명주기 동안 보안 취약점을 체계적으로 접수, 분석 및 무상 조치할 수 있는 '조정된 취약점 공표(CVD)' 프로세스를 구축하고, 고객 및 시장에 명
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:45:43 (원문 시간대 미표기)
- 원문: [commit 603817c982769c771a2ae318cbf651615823223b](https://github.com/useformotor3/ai-discord-bot/commit/603817c982769c771a2ae318cbf651615823223b) | [research_archive/2026-11-15_204543.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_204543.md) | commit UTC: 2026-11-15T20:46:00.000Z
- 원문 blob SHA: f9290c4b291fb85d7b3eb61a9cb2ecf8538e8608
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 규정된 생명주기 동안 보안 취약점을 체계적으로 접수, 분석 및 무상 조치할 수 있는 '조정된 취약점 공표(CVD)' 프로세스를 구축하고, 고객 및 시장에 명확한 취약점 보고 채널을 제공해야 합니다. EU CRA Annex I(필요한 사이버 보안 요구사항)에 따라, 발견된 취약점은
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #251 — P0 — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 최소 5년(또는 제품의 예상 사용 기간) 동안 사용자에게 추가 비용(무상) 없이 보안 업데이트를 제공해야 합니다. 업데이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:50:37 (원문 시간대 미표기)
- 원문: [commit 4e58b59007578c25d618c0c07ef1fd0db089a6ab](https://github.com/useformotor3/ai-discord-bot/commit/4e58b59007578c25d618c0c07ef1fd0db089a6ab) | [research_archive/2026-11-15_205037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_205037.md) | commit UTC: 2026-11-15T20:50:54.000Z
- 원문 blob SHA: 942905a2fba79274df209b9f4e6677bd5805c261
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 최소 5년(또는 제품의 예상 사용 기간) 동안 사용자에게 추가 비용(무상) 없이 보안 업데이트를 제공해야 합니다. 업데이트 메커니즘은 악성 개조를 방지하도록 설계되어야 하며, 업데이트 가용성이 규정된 기간 동안 지속적으로 보장되어야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #252 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트(패치)를 제공해야 하며, 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 20:55:30 (원문 시간대 미표기)
- 원문: [commit 53d4d726e4e034809fd2b247c72de1ba7083b2c3](https://github.com/useformotor3/ai-discord-bot/commit/53d4d726e4e034809fd2b247c72de1ba7083b2c3) | [research_archive/2026-11-15_205530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_205530.md) | commit UTC: 2026-11-15T20:55:47.000Z
- 원문 blob SHA: bb5924889c8a43a0b2fe2ecf2807bd8c677df041
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free-of-charge) 보안 업데이트(패치)를 제공해야 하며, 이를 안전하게 자동 또는 수동으로 배포할 수 있는 무결성 검증된 업데이트 메커니즘을 기술 문서에 명시하고 구현해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #253 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 패치를 제공해야 하며, 사용자가 이 업데이트를 안전하
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:00:52 (원문 시간대 미표기)
- 원문: [commit 09eaf49c3ff8851647e9d86eeffd74dd00d8b82b](https://github.com/useformotor3/ai-discord-bot/commit/09eaf49c3ff8851647e9d86eeffd74dd00d8b82b) | [research_archive/2026-11-15_210052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_210052.md) | commit UTC: 2026-11-15T21:01:08.000Z
- 원문 blob SHA: d9786c2a7067e62519d95a84d4d0505f65bc92c3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 패치를 제공해야 하며, 사용자가 이 업데이트를 안전하고 자동화된 방식으로 적용할 수 있는 무결성 검증된 메커니즘을 보장해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #254 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free of charge) 보안 업데이트 및
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:05:35 (원문 시간대 미표기)
- 원문: [commit a88f140b5b993c218ee41dd571b918dac673aaa5](https://github.com/useformotor3/ai-discord-bot/commit/a88f140b5b993c218ee41dd571b918dac673aaa5) | [research_archive/2026-11-15_210535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_210535.md) | commit UTC: 2026-11-15T21:05:51.000Z
- 원문 blob SHA: 6646fbd24396d41df8cb8053abf622b730fd52a8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점에 대해 추가 비용 청구 없이(Free of charge) 보안 업데이트 및 패치를 배포해야 합니다. 또한, 패치 가용성에 대한 명확하고 투명한 공지 프로세스를 수립하여 사용자가 적시에 업데이트를 적용
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #255 — P0 — 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점에 대한 보안 업데이트(Security Update)를 사용자가 안전하고 적시에 적용할 수 있도록 자동화된 메커니즘
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:10:36 (원문 시간대 미표기)
- 원문: [commit 938205dc83bb759d4200515c9080aab4f4a2077d](https://github.com/useformotor3/ai-discord-bot/commit/938205dc83bb759d4200515c9080aab4f4a2077d) | [research_archive/2026-11-15_211036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_211036.md) | commit UTC: 2026-11-15T21:10:52.000Z
- 원문 blob SHA: 6a858994b273ecd71fba8297127cf1589f125c52
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA Annex I에 따라 발견된 취약점에 대한 보안 업데이트(Security Update)를 사용자가 안전하고 적시에 적용할 수 있도록 자동화된 메커니즘과 명확한 통지 절차를 기술 문서 및 제품 설계에 구현해야 합니다. 특히 산업 현장의 가동 중단(Downtime) 위험을 최소
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #256 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견된 취약점에 대해 추가 비용 청구 없이 보안 패치(Free-of-charge security updates)
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:15:34 (원문 시간대 미표기)
- 원문: [commit 3fd2a9cbe195cc02d16b7c8462619b03b107066f](https://github.com/useformotor3/ai-discord-bot/commit/3fd2a9cbe195cc02d16b7c8462619b03b107066f) | [research_archive/2026-11-15_211534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_211534.md) | commit UTC: 2026-11-15T21:15:50.000Z
- 원문 blob SHA: 04c21a673e94a98bb973b0829ccabdc542a55ee8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견된 취약점에 대해 추가 비용 청구 없이 보안 패치(Free-of-charge security updates)를 제공해야 하며, 모션 제어 시스템의 가용성을 해치지 않는 안전한 업데이트 배포 메커니즘(Secure Update Deplo
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #257 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점을 무상으로 패치하고, 취약점 공개 및 처리 프로세스를 법적 기한 내에 이행
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:20:38 (원문 시간대 미표기)
- 원문: [commit 4100516e688469fb667644a9e5ff53d67474c69c](https://github.com/useformotor3/ai-discord-bot/commit/4100516e688469fb667644a9e5ff53d67474c69c) | [research_archive/2026-11-15_212038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_212038.md) | commit UTC: 2026-11-15T21:20:55.000Z
- 원문 blob SHA: de3689c0c856cec621b73710baceab7017186621
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점을 무상으로 패치하고, 취약점 공개 및 처리 프로세스를 법적 기한 내에 이행해야 합니다. 특히 모션 제어 시스템의 오작동이 인명 사고로 직결될 수 있으므로, 제조사는 취약점 발견 시 신속한 보안 업데이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #258 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 무상으로, 지체 없이 패치해야 하며, 제품의 예상 수명 주기(또는 최소 5년) 동안 보안 업데이트를 제공할 수 있는 취
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:25:33 (원문 시간대 미표기)
- 원문: [commit 336757edec34b667d8002142d16eacfd28172492](https://github.com/useformotor3/ai-discord-bot/commit/336757edec34b667d8002142d16eacfd28172492) | [research_archive/2026-11-15_212533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_212533.md) | commit UTC: 2026-11-15T21:25:49.000Z
- 원문 blob SHA: 54c4277f8f261f70953e9fda5350f80571ca387a
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 무상으로, 지체 없이 패치해야 하며, 제품의 예상 수명 주기(또는 최소 5년) 동안 보안 업데이트를 제공할 수 있는 취약점 처리 프로세스를 갖추어야 합니다. 특히 모션 제어 시스템의 가동 중단(Downtime)을 방지하기 위한 안전한 업데이트
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #259 — P0 — EU CRA 제11조 및 Annex I에 따라, 제조사는 서보 드라이브의 예상 사용 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 이를 위한 취약점 처
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:30:51 (원문 시간대 미표기)
- 원문: [commit f7031cd58a49a16c959142fb22e514e49c4fc62f](https://github.com/useformotor3/ai-discord-bot/commit/f7031cd58a49a16c959142fb22e514e49c4fc62f) | [research_archive/2026-11-15_213051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_213051.md) | commit UTC: 2026-11-15T21:31:10.000Z
- 원문 blob SHA: e037d93643c2343e4e9d4bcdaa2698ae773bcda3
- 핵심 주장 주제(원문 요약 첫 부분): EU CRA 제11조 및 Annex I에 따라, 제조사는 서보 드라이브의 예상 사용 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 이를 위한 취약점 처리 정책과 보안 업데이트를 보장해야 합니다. 사용자가 보안 업데이트(Security Updates)를 명시적으로 거부하지 않는
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #260 — P0 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트와 인터페이스가 잠긴 Secure by Default 상태여야 하며, CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:35:31 (원문 시간대 미표기)
- 원문: [commit 5af73f435904124acc33813be4ad3a5c4cdb9990](https://github.com/useformotor3/ai-discord-bot/commit/5af73f435904124acc33813be4ad3a5c4cdb9990) | [research_archive/2026-11-15_213531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_213531.md) | commit UTC: 2026-11-15T21:35:47.000Z
- 원문 blob SHA: c3e89a5c5130125e09b218190421358df22ec0f3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 포트와 인터페이스가 잠긴 Secure by Default 상태여야 하며, CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견되는 취약점에 대해 추가 비용 청구 없이 보안 패치 및 업데이트를 무상으로 제공해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #261 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 부속서 I에 따라 제품의 예상 수명주기(최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트를 제공해야 하며, 이를 자동화된 방
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:40:34 (원문 시간대 미표기)
- 원문: [commit 7c4b075a1f5b644ead1bb03a6350b82b501ee22b](https://github.com/useformotor3/ai-discord-bot/commit/7c4b075a1f5b644ead1bb03a6350b82b501ee22b) | [research_archive/2026-11-15_214034.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_214034.md) | commit UTC: 2026-11-15T21:40:49.000Z
- 원문 blob SHA: 9f1b623376d8526f9317eeff91f6f503a3c592f7
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 부속서 I에 따라 제품의 예상 수명주기(최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 업데이트를 제공해야 하며, 이를 자동화된 방식으로 최종 사용자에게 안전하게 배포할 수 있는 메커니즘을 갖추어야 합니다. 특히 모션 제어 중단 위험을 방지하기 위한 안전한
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #262 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 패치 및 업데이트를 제공해야 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:45:34 (원문 시간대 미표기)
- 원문: [commit 4d9031e2a2b87d3f6d3ceb207d1e162277d579c5](https://github.com/useformotor3/ai-discord-bot/commit/4d9031e2a2b87d3f6d3ceb207d1e162277d579c5) | [research_archive/2026-11-15_214534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_214534.md) | commit UTC: 2026-11-15T21:45:51.000Z
- 원문 blob SHA: 69b9330d7c03b2a48ccf3c805594805a37275975
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대해 추가 비용 청구 없이(무상으로) 보안 패치 및 업데이트를 제공해야 하며, 사용자가 이를 안전하고 마찰 없이 적용할 수 있는 자동화된 배포 메커니즘을 보장해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #263 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 모든 보안 취약점을 무상으로 조치(Patch)해야 하며, 업데이트 과정에서 모션 제어 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:50:38 (원문 시간대 미표기)
- 원문: [commit 33e5ee126d66892b03d37b2f9f7ea47f6cc5f683](https://github.com/useformotor3/ai-discord-bot/commit/33e5ee126d66892b03d37b2f9f7ea47f6cc5f683) | [research_archive/2026-11-15_215038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_215038.md) | commit UTC: 2026-11-15T21:50:54.000Z
- 원문 blob SHA: 9f7842fb1df032fba2069a185f284ac1e0b93a1e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 모든 보안 취약점을 무상으로 조치(Patch)해야 하며, 업데이트 과정에서 모션 제어 시스템의 실시간 가용성을 저해하지 않는 안전한 배포 메커니즘을 보장해야 합니다. 또한, 취약점 수정 조치는 지연 없이 대중에게
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #264 — P0 — 산업용 서보 드라이브 제조사는 EU CRA에 따라 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 체계적인 취약점 공개 정책을 운영하고 이행할 법적
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 21:55:30 (원문 시간대 미표기)
- 원문: [commit 666eaff1a735fe72f602b14a91c20264df652e7f](https://github.com/useformotor3/ai-discord-bot/commit/666eaff1a735fe72f602b14a91c20264df652e7f) | [research_archive/2026-11-15_215530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_215530.md) | commit UTC: 2026-11-15T21:55:46.000Z
- 원문 blob SHA: 8349526b1fb953d29807853a35125130cfe4bc79
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA에 따라 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 하며, 이를 위한 체계적인 취약점 공개 정책을 운영하고 이행할 법적 의무를 진다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #265 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 또는 법정 기준) 발견된 취약점에 대해 사용자에게 추가 비용(무상) 없이 보안 업데이트 및 패치를 적시에 제공
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:00:49 (원문 시간대 미표기)
- 원문: [commit 4ed4d071351a05d19da4e2fd59162756d858a5c7](https://github.com/useformotor3/ai-discord-bot/commit/4ed4d071351a05d19da4e2fd59162756d858a5c7) | [research_archive/2026-11-15_220049.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_220049.md) | commit UTC: 2026-11-15T22:01:05.000Z
- 원문 blob SHA: f899b478426b8e11c710a72203e1dce03bcab100
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안(최소 5년 또는 법정 기준) 발견된 취약점에 대해 사용자에게 추가 비용(무상) 없이 보안 업데이트 및 패치를 적시에 제공해야 합니다. 또한, 취약점 정보 처리를 위한 명확한 정책을 수립하고 외부에 공개해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #266 — P1 — 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 인증되지 않은 외부 접근이 원천 차단되도록 안전한 기본 설정(Secure by default) 상태여야 하며, 공
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:05:33 (원문 시간대 미표기)
- 원문: [commit 5a87345ca60e9f60ea0ade1692b4db193f5e4e3c](https://github.com/useformotor3/ai-discord-bot/commit/5a87345ca60e9f60ea0ade1692b4db193f5e4e3c) | [research_archive/2026-11-15_220533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_220533.md) | commit UTC: 2026-11-15T22:05:49.000Z
- 원문 blob SHA: 188d42285532919850ac73919509f55d26754881
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 인증되지 않은 외부 접근이 원천 차단되도록 안전한 기본 설정(Secure by default) 상태여야 하며, 공격 표면을 최소화하기 위해 기본적으로 불필요한 기능, 포트, 서비스가 비활성화되어야 합니다. 제조사는 제품의 전원 공급 및 네
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #267 — P1 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 네트워크 인터페이스와 서비스가 비활성화된 'Secure by Default' 상태여야 하며, 인증되지 않은 초기 설정의 임의 변
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:10:42 (원문 시간대 미표기)
- 원문: [commit 5f170cd6ade80bf83415887c5231ba9a2f0c0500](https://github.com/useformotor3/ai-discord-bot/commit/5f170cd6ade80bf83415887c5231ba9a2f0c0500) | [research_archive/2026-11-15_221042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_221042.md) | commit UTC: 2026-11-15T22:10:59.000Z
- 원문 blob SHA: 4686dac0bda0b56f210e36638ff23f30fadb79b0
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 네트워크 인터페이스와 서비스가 비활성화된 'Secure by Default' 상태여야 하며, 인증되지 않은 초기 설정의 임의 변경을 원천 차단하는 강력한 접근 통제 메커니즘을 갖추어야 합니다. 제조사는 사용자가 보안 설정을 명시적으로 활성화하기 전까지
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #268 — P1 — 산업용 서보 드라이브는 출고 시점부터 불필요한 네트워크 인터페이스, 포트, 서비스 및 기본 계정을 비활성화하여 공격 표면을 최소화해야 하며, 사용자가 첫 부팅 시 안전한 설정(Se
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:15:41 (원문 시간대 미표기)
- 원문: [commit 35efabf2a3fd52c581ffe480bde3dded64601bce](https://github.com/useformotor3/ai-discord-bot/commit/35efabf2a3fd52c581ffe480bde3dded64601bce) | [research_archive/2026-11-15_221541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_221541.md) | commit UTC: 2026-11-15T22:15:58.000Z
- 원문 blob SHA: ad6581adc350f67aa522afef20944906038e1106
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 불필요한 네트워크 인터페이스, 포트, 서비스 및 기본 계정을 비활성화하여 공격 표면을 최소화해야 하며, 사용자가 첫 부팅 시 안전한 설정(Secure by default)을 강제하도록 설계되어야 합니다. 또한, 공장 초기화 시에도 제조사의 기본 보안 상태가 안전하게
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #269 — P0 — 서보 드라이브는 공장 출고 시(Out-of-the-box) 권한 통제와 공격 표면을 최소화한 '기본 설정에 따른 안전(Secure by Default)' 상태여야 합니다. 제조사는
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:20:42 (원문 시간대 미표기)
- 원문: [commit cb6ecd9cbe3a099328843b667c6a162626f6675e](https://github.com/useformotor3/ai-discord-bot/commit/cb6ecd9cbe3a099328843b667c6a162626f6675e) | [research_archive/2026-11-15_222042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_222042.md) | commit UTC: 2026-11-15T22:20:58.000Z
- 원문 blob SHA: 8b542d879ffe7df0254da6ace825e540a878fe2c
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브는 공장 출고 시(Out-of-the-box) 권한 통제와 공격 표면을 최소화한 '기본 설정에 따른 안전(Secure by Default)' 상태여야 합니다. 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견되는 취약점에 대해 사용자에게 추가 비용 청구 없이 '무상 보안 업데이트'를 제
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #270 — P2 — 핵심 내용 1: 서보 드라이브 제조사는 발견된 취약점과 보안사고를 법정 기한 내에 유럽 컴퓨터 침해사고 대응팀(CSIRCs) 네트워크 및 ENISA에 자동으로 신고할 수 있는 체계
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:25:36 (원문 시간대 미표기)
- 원문: [commit bd555463c41a7e1da69b4a32e58be4dfd1251976](https://github.com/useformotor3/ai-discord-bot/commit/bd555463c41a7e1da69b4a32e58be4dfd1251976) | [research_archive/2026-11-15_222536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_222536.md) | commit UTC: 2026-11-15T22:25:52.000Z
- 원문 blob SHA: 86330be35b2bc4b980645dace1c4a04cf39b9a51
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 서보 드라이브 제조사는 발견된 취약점과 보안사고를 법정 기한 내에 유럽 컴퓨터 침해사고 대응팀(CSIRCs) 네트워크 및 ENISA에 자동으로 신고할 수 있는 체계를 갖추어야 합니다. 핵심 내용 2: 기계류 및 산업용 자동화 생태계 내에서 취약점 정보(CSAF 등 표준 포맷)를 최종 사용
- 우선순위/검증 쟁점: P2 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #271 — P1 — 산업용 서보 드라이브는 초기 출고 시점부터 공격 표면을 최소화하도록 '보안된 기본 설정(Secure by default)' 상태로 제공되어야 하며, 사용자가 네트워크 설정이나 권한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:30:46 (원문 시간대 미표기)
- 원문: [commit 898fc8b6802525a27c125238f3dee53055928b63](https://github.com/useformotor3/ai-discord-bot/commit/898fc8b6802525a27c125238f3dee53055928b63) | [research_archive/2026-11-15_223046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_223046.md) | commit UTC: 2026-11-15T22:31:01.000Z
- 원문 blob SHA: 3c8bc3ee4f7884e68fa35a622f697dbe1d55bd3e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시점부터 공격 표면을 최소화하도록 '보안된 기본 설정(Secure by default)' 상태로 제공되어야 하며, 사용자가 네트워크 설정이나 권한을 변경할 때 보안 위험을 초래하지 않는 안전한 인터페이스를 갖추어야 합니다. 특히 CRA 부속서 I에 따라, 제조사는 기본적
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #272 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 부속서 I에 따라, 제품 내 포함된 모든 오픈소스 및 상용 소프트웨어 구성 요소를 식별할 수 있는 기계 판독 가능한 소프트웨어 부품 명세
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:35:31 (원문 시간대 미표기)
- 원문: [commit abd08a0de69d33a989656d1f21f45485e388d986](https://github.com/useformotor3/ai-discord-bot/commit/abd08a0de69d33a989656d1f21f45485e388d986) | [research_archive/2026-11-15_223531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_223531.md) | commit UTC: 2026-11-15T22:35:47.000Z
- 원문 blob SHA: 1ce1484d4cd92c9514b3a182eb2138c914913010
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 부속서 I에 따라, 제품 내 포함된 모든 오픈소스 및 상용 소프트웨어 구성 요소를 식별할 수 있는 기계 판독 가능한 소프트웨어 부품 명세서(SBOM)를 작성하고, 제품 수명주기 동안 이를 최신 상태로 유지·제공해야 합니다. 이를 통해 공급망 투명성을 확보하고 예
- 우선순위/검증 쟁점: P0 — EUR-Lex Annex I Part II(1): SBOM은 제조자 취약점 처리 요구이며 최소 top-level dependencies 포함. Annex VII(2)(b) 기술문서와 Annex II(9) 사용자 제공(제조자가 제공 결정 시)을 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #273 — P2 — 서보 드라이브 제조사는 CRA 부속서 I(Annex I)에 따라 보안 취약점 정보와 관련 소프트웨어 업데이트를 사용자가 기계 판독 가능한 형식(Machine-readable for
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:40:38 (원문 시간대 미표기)
- 원문: [commit b7423a9ccae0c09611cb178168c55c0208fc6a18](https://github.com/useformotor3/ai-discord-bot/commit/b7423a9ccae0c09611cb178168c55c0208fc6a18) | [research_archive/2026-11-15_224038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_224038.md) | commit UTC: 2026-11-15T22:40:55.000Z
- 원문 blob SHA: 2f6caa9566a14ef1c6a855eb3ab54ac09d092e1e
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA 부속서 I(Annex I)에 따라 보안 취약점 정보와 관련 소프트웨어 업데이트를 사용자가 기계 판독 가능한 형식(Machine-readable format)으로 제공해야 하며, 이를 통해 공장 자동화 시스템의 대규모 자산 관리 및 자동화된 취약점 대응 체계를 구축해야 합니다
- 우선순위/검증 쟁점: P2 — 정확한 조항·문서 버전·주변 문맥 재확인 필요. 주제 기반 사전 분류이며 개별 claim 검증 완료가 아님.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #274 — P0 — 산업용 서보 드라이브 제조사는 제품의 예상 수명주기(또는 최소 5년) 동안 발견된 보안 취약점을 무료로 처리할 수 있는 보안 업데이트를 제공해야 하며, 취약점 신고 접수를 위한 명
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:45:45 (원문 시간대 미표기)
- 원문: [commit 4f341d42fb9fae794843352513b37be4c0322429](https://github.com/useformotor3/ai-discord-bot/commit/4f341d42fb9fae794843352513b37be4c0322429) | [research_archive/2026-11-15_224545.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_224545.md) | commit UTC: 2026-11-15T22:46:02.000Z
- 원문 blob SHA: c66c3eb7bffc64ec3135a4e3f7d1e19f617acd43
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 제품의 예상 수명주기(또는 최소 5년) 동안 발견된 보안 취약점을 무료로 처리할 수 있는 보안 업데이트를 제공해야 하며, 취약점 신고 접수를 위한 명확한 공개 정책(VDP)을 운영해야 합니다. 사용자 및 보안 연구자가 취약점을 안전하게 제보할 수 있는 채널을 구축하고, 제조
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #275 — P2 — 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 제품에서 발생하는 액티브 취약점 및 심각한 보안 인프런트(Incident)를 정해진 기한 내에 유럽 컴퓨터 침해사고 대응팀(
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:50:42 (원문 시간대 미표기)
- 원문: [commit 94cecfc6338d37188750441a4e7c45ef718d327c](https://github.com/useformotor3/ai-discord-bot/commit/94cecfc6338d37188750441a4e7c45ef718d327c) | [research_archive/2026-11-15_225042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_225042.md) | commit UTC: 2026-11-15T22:50:59.000Z
- 원문 blob SHA: 641e8c52406d64d374b9bc9f462edf43aa11e777
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 제품에서 발생하는 액티브 취약점 및 심각한 보안 인프런트(Incident)를 정해진 기한 내에 유럽 컴퓨터 침해사고 대응팀(CSIRTs) 네트워크 및 ENISA에 자동 통보할 수 있는 하드웨어/소프트웨어적 로깅 및 보고 체계를 강제 구축해야 합니다.
- 우선순위/검증 쟁점: P2 — 정확한 조항·문서 버전·주변 문맥 재확인 필요. 주제 기반 사전 분류이며 개별 claim 검증 완료가 아님.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #276 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년 또는 법적 정의 기간) 동안 발견된 보안 취약점을 추가 비용 부과 없이(무상으로) 시정해야 하며, 업
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 22:55:27 (원문 시간대 미표기)
- 원문: [commit 91e5a46a79a5d00ece82d24f3a1274f486f3d5e7](https://github.com/useformotor3/ai-discord-bot/commit/91e5a46a79a5d00ece82d24f3a1274f486f3d5e7) | [research_archive/2026-11-15_225527.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_225527.md) | commit UTC: 2026-11-15T22:55:44.000Z
- 원문 blob SHA: e77214377fd922ce9a47ffde19221f55dc8bb2b1
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년 또는 법적 정의 기간) 동안 발견된 보안 취약점을 추가 비용 부과 없이(무상으로) 시정해야 하며, 업데이트 과정에서 악성코드 주입이나 서비스 중단(가용성 침해)을 방지할 수 있는 안전하고 자동화된 배포 메커니즘을 기술 문서에
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #277 — P2 — 산업용 서보 드라이브 제조사는 CRA에 따라 자사 제품에서 발견된 취약점과 악용 사례를 규정된 기한 내에 유럽 네트워크정보보호청(ENISA) 및 관할 CSIRT(Computer S
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:00:52 (원문 시간대 미표기)
- 원문: [commit 086b45fe50bf84e97c96953f8f1d63a0e987e7a2](https://github.com/useformotor3/ai-discord-bot/commit/086b45fe50bf84e97c96953f8f1d63a0e987e7a2) | [research_archive/2026-11-15_230052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_230052.md) | commit UTC: 2026-11-15T23:01:08.000Z
- 원문 blob SHA: df4e2bb6feb474c042d81712d0865cbab7655552
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 자사 제품에서 발견된 취약점과 악용 사례를 규정된 기한 내에 유럽 네트워크정보보호청(ENISA) 및 관할 CSIRT(Computer Security Incident Response Team)에 의무적으로 신고해야 합니다. 제조업체는 취약점 수명주기 동안 신뢰할
- 우선순위/검증 쟁점: P2 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #278 — P0 — 산업용 서보 드라이브 제조사는 EU CRA 제11조 및 Annex I에 따라, 제품의 예상 수명 주기 동안 발견되는 취약점을 체계적으로 처리해야 하며, 알려진 취약점을 해결하기 위
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:05:30 (원문 시간대 미표기)
- 원문: [commit a4836d18f271f987c7efe35d00416f651a7bc42d](https://github.com/useformotor3/ai-discord-bot/commit/a4836d18f271f987c7efe35d00416f651a7bc42d) | [research_archive/2026-11-15_230530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_230530.md) | commit UTC: 2026-11-15T23:05:47.000Z
- 원문 blob SHA: 1c6e8b32c59e7ac5c8fe37e6e9b256d1940ac6b2
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 제11조 및 Annex I에 따라, 제품의 예상 수명 주기 동안 발견되는 취약점을 체계적으로 처리해야 하며, 알려진 취약점을 해결하기 위한 보안 업데이트를 추가 비용 없이(Free-of-charge) 적시에 제공하고 이를 사용자에게 투명하게 공지해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #279 — P1 — 산업용 서보 드라이브는 무단 접근을 방지하기 위해 안전한 액세스 제어 메커니즘을 탑재하고, 기본 설정(Secure by default)으로서 강력한 인증 및 최소 권한 원칙을 강제
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:10:40 (원문 시간대 미표기)
- 원문: [commit e609f9755cc997a840952e617fec39326ffeecf1](https://github.com/useformotor3/ai-discord-bot/commit/e609f9755cc997a840952e617fec39326ffeecf1) | [research_archive/2026-11-15_231040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_231040.md) | commit UTC: 2026-11-15T23:10:57.000Z
- 원문 blob SHA: 59cf7e40d49b6dc3ed45383aa70dbe86be4eeb52
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 무단 접근을 방지하기 위해 안전한 액세스 제어 메커니즘을 탑재하고, 기본 설정(Secure by default)으로서 강력한 인증 및 최소 권한 원칙을 강제해야 합니다. 이는 규정 Annex I(부속서 I) Part I의 필수 사이버 보안 요구사항에 직접 명시되어 있습니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #280 — P1 — 산업용 서보 드라이브는 기본 설정(Secure by default)에서 무단 접근을 방지하는 강력한 접근 제어 메커니즘을 갖추어야 하며, 펌웨어 및 구성 데이터의 보안 검증을 위해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:15:37 (원문 시간대 미표기)
- 원문: [commit 0d563394f13b3f2d330cd7616964ffd60f821959](https://github.com/useformotor3/ai-discord-bot/commit/0d563394f13b3f2d330cd7616964ffd60f821959) | [research_archive/2026-11-15_231537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_231537.md) | commit UTC: 2026-11-15T23:15:54.000Z
- 원문 blob SHA: 4d6246e87b5799daded34a86d85375acabac22b4
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 기본 설정(Secure by default)에서 무단 접근을 방지하는 강력한 접근 제어 메커니즘을 갖추어야 하며, 펌웨어 및 구성 데이터의 보안 검증을 위해 하드웨어 기반 루트 오브 트러스트(Root of Trust)를 필수적으로 구현해야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #281 — P1 — 산업용 서보 드라이브는 초기 출고 시 수정 가능한 기본 관리자 계정이나 비밀번호를 포함해서는 안 되며(Secure by default), 시스템이 처음 실행될 때 사용자가 고유한 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:20:35 (원문 시간대 미표기)
- 원문: [commit e19f279bc362086a5f7afe0cbba8a18f023bb0a1](https://github.com/useformotor3/ai-discord-bot/commit/e19f279bc362086a5f7afe0cbba8a18f023bb0a1) | [research_archive/2026-11-15_232035.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_232035.md) | commit UTC: 2026-11-15T23:20:51.000Z
- 원문 blob SHA: 2eb4a4e87004f6826b8fddd3b53d8a3a284bf879
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시 수정 가능한 기본 관리자 계정이나 비밀번호를 포함해서는 안 되며(Secure by default), 시스템이 처음 실행될 때 사용자가 고유한 보안 인증 정보를 강제로 설정하도록 설계되어야 합니다. 이는 CRA Annex I에 명시된 필수 사이버 보안 요건을 충족하기
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #282 — P1 — 산업용 서보 드라이브는 출고 시점(Out-of-the-box)부터 네트워크 악용을 방지하기 위해 공장 초기 비밀번호(Default Password) 사용을 금지하고, 사용자가 최초
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:25:32 (원문 시간대 미표기)
- 원문: [commit 74bc4721d08388842f8a423bfc553b91b9b386e7](https://github.com/useformotor3/ai-discord-bot/commit/74bc4721d08388842f8a423bfc553b91b9b386e7) | [research_archive/2026-11-15_232532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_232532.md) | commit UTC: 2026-11-15T23:25:52.000Z
- 원문 blob SHA: 4b5ef88ca203e1485a771acb112b7d11e57cbcdc
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점(Out-of-the-box)부터 네트워크 악용을 방지하기 위해 공장 초기 비밀번호(Default Password) 사용을 금지하고, 사용자가 최초 설치 시 강력한 고유 인증 정보를 강제로 설정하도록 하는 'Secure by Default' 의무를 준수해야 합니다. 또한,
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #283 — P1 — 서보 드라이브 제조사는 제품 출고 시 인증 정보 하드코딩을 금지하고, 사용자가 최초 부팅 시 고유한 비밀번호 설정이나 강력한 인증을 강제하도록 '안전한 기본 설정(Secure by
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:30:42 (원문 시간대 미표기)
- 원문: [commit 92cbe719996885fb5c18d0ca47d3668884adc163](https://github.com/useformotor3/ai-discord-bot/commit/92cbe719996885fb5c18d0ca47d3668884adc163) | [research_archive/2026-11-15_233042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_233042.md) | commit UTC: 2026-11-15T23:30:56.000Z
- 원문 blob SHA: 802ebc8db3c682b5d8785312fbd8198dae950939
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시 인증 정보 하드코딩을 금지하고, 사용자가 최초 부팅 시 고유한 비밀번호 설정이나 강력한 인증을 강제하도록 '안전한 기본 설정(Secure by Default)' 상태를 반드시 구현해야 합니다. 또한, 사용하지 않는 네트워크 인터페이스와 포트는 기본적으로 비활성화되어야
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #284 — P0 — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품 생명주기 동안 발견되는 보안 취약점을 체계적으로 접수·처리·공개할 수 있는 취약점 공개 정책(VDP)을 수립하고, 취약점 수
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:35:32 (원문 시간대 미표기)
- 원문: [commit 5c0941a4b448ff036ffe2ad4a4762395c1f349d8](https://github.com/useformotor3/ai-discord-bot/commit/5c0941a4b448ff036ffe2ad4a4762395c1f349d8) | [research_archive/2026-11-15_233532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_233532.md) | commit UTC: 2026-11-15T23:35:49.000Z
- 원문 blob SHA: ca24df6b685df0546bc0fc5fde608a9ca1545e12
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품 생명주기 동안 발견되는 보안 취약점을 체계적으로 접수·처리·공개할 수 있는 취약점 공개 정책(VDP)을 수립하고, 취약점 수정 정보 및 보안 업데이트를 무상으로 제공해야 합니다. 이는 사고 대응 투명성을 높이고 현장(Field)의 사이버 위협을 실시
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #285 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견된 취약점에 대한 보안 업데이트를 추가 비용(무상) 없이 제공해야 하며, 이를 위한 취약점 수명주기
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:40:38 (원문 시간대 미표기)
- 원문: [commit 229a1fa4978514df107e24f3fd5d0b95e069490f](https://github.com/useformotor3/ai-discord-bot/commit/229a1fa4978514df107e24f3fd5d0b95e069490f) | [research_archive/2026-11-15_234038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_234038.md) | commit UTC: 2026-11-15T23:40:55.000Z
- 원문 blob SHA: 2169beff1fd3829ba6d10780c4bed08cbd95cde4
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 또는 10년 동안 발견된 취약점에 대한 보안 업데이트를 추가 비용(무상) 없이 제공해야 하며, 이를 위한 취약점 수명주기 관리 체계를 기술 문서에 명시해야 합니다. 자동화 시스템의 특성상 패치 적용 중단에 따른 생산 라인 손실을 방지하기 위해,
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #286 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 보안 취약점을 추가 비용 청구 없이(Free of charge) 적시에 패치하고 보안 업데이트를 제공해야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:45:42 (원문 시간대 미표기)
- 원문: [commit 51350a4ac30a9a703c6893a9894fe7fa51e10625](https://github.com/useformotor3/ai-discord-bot/commit/51350a4ac30a9a703c6893a9894fe7fa51e10625) | [research_archive/2026-11-15_234542.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_234542.md) | commit UTC: 2026-11-15T23:45:59.000Z
- 원문 blob SHA: 730483aeb3c8942bdd39872f00cb34c07daeef6c
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 보안 취약점을 추가 비용 청구 없이(Free of charge) 적시에 패치하고 보안 업데이트를 제공해야 합니다. 이는 상업적 유지보수 계약과 무관하게 법적 의무로 강제되며, 다운타임(Downtime) 최소화를 고려한 안전한 업데
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #287 — P1 — 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위해 사용자 계정 및 비밀번호와 같은 초기 인증 정보를 고유하게 설정(Unique default credentials)해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:50:39 (원문 시간대 미표기)
- 원문: [commit aef6e019ca3caadc51229960428c67491f59be47](https://github.com/useformotor3/ai-discord-bot/commit/aef6e019ca3caadc51229960428c67491f59be47) | [research_archive/2026-11-15_235039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_235039.md) | commit UTC: 2026-11-15T23:50:57.000Z
- 원문 blob SHA: 78fd106029ca6c3fbb1e24030d8e85edebbb8450
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위해 사용자 계정 및 비밀번호와 같은 초기 인증 정보를 고유하게 설정(Unique default credentials)해야 하며, 공격 표면을 최소화하기 위해 필수적이지 않은 네트워크 서비스와 기능은 기본적으로 비활성화된 상태(Secure by
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #288 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 네트워크 인터페이스, 디버그 포트(JTAG/UART), 기본 계정이 잠겨 있거나 비활성화된 'Secure b
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 23:55:35 (원문 시간대 미표기)
- 원문: [commit f205da045ee004580146cc6ea9822fd2801667fa](https://github.com/useformotor3/ai-discord-bot/commit/f205da045ee004580146cc6ea9822fd2801667fa) | [research_archive/2026-11-15_235535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_235535.md) | commit UTC: 2026-11-15T23:55:51.000Z
- 원문 blob SHA: 6bcdd8acb79e51c76c1696708ba0b81b337b00cf
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 네트워크 인터페이스, 디버그 포트(JTAG/UART), 기본 계정이 잠겨 있거나 비활성화된 'Secure by default(기본 설정에 의한 보안)' 상태를 유지해야 하며, 사용자가 최초 구성 시 강제로 강력한 인증 설정을 거치도록
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #1 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간 동안 발견되는 취약점에 대한 보안 업데이트(Security updates)를 추가 비용 없이(Free of charge
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:00:52 (원문 시간대 미표기)
- 원문: [commit 5e3b8f404dd3e27a9e35511941ccf59de12c7960](https://github.com/useformotor3/ai-discord-bot/commit/5e3b8f404dd3e27a9e35511941ccf59de12c7960) | [research_archive/2026-11-16_000052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_000052.md) | commit UTC: 2026-11-16T00:01:10.000Z
- 원문 blob SHA: 5d1227baa4560d76e1a72356d14cbebdf510212f
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간 동안 발견되는 취약점에 대한 보안 업데이트(Security updates)를 추가 비용 없이(Free of charge) 제공해야 합니다. 또한, 취약점의 조정된 공개(Coordinated vulnerability disclosure)를 지원하
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #2 — P0 — 핵심 내용 1: 산업용 서보 드라이브 제조사는 제품에 영향을 미치는 중대한 취약점이나 활성 악용 사례를 인지한 즉시(늦어도 24시간 이내) ENISA에 조기 경보(Early War
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:05:37 (원문 시간대 미표기)
- 원문: [commit 3ff2f15706e5ccdaaa71592f6a54d089887d598f](https://github.com/useformotor3/ai-discord-bot/commit/3ff2f15706e5ccdaaa71592f6a54d089887d598f) | [research_archive/2026-11-16_000537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_000537.md) | commit UTC: 2026-11-16T00:05:54.000Z
- 원문 blob SHA: 4ea450318c42c400508da3d8a922e73986efbdcb
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브 제조사는 제품에 영향을 미치는 중대한 취약점이나 활성 악용 사례를 인지한 즉시(늦어도 24시간 이내) ENISA에 조기 경보(Early Warning)를 제출해야 합니다. 핵심 내용 2: 취약점 통지 후 법적 기한 내에 심각도 평가, 영향 분석, 그리고 사용자가 적용
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #3 — P1 — 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 사용자가 안전하게 제품을 설치, 운영, 유지보수할 수 있도록 보안 관련 필수 정보와 명확한 사용 지침을 디지털 또는 물리적 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:10:55 (원문 시간대 미표기)
- 원문: [commit 99f374ffee57abca87ac85605d0d9e22d3509bcf](https://github.com/useformotor3/ai-discord-bot/commit/99f374ffee57abca87ac85605d0d9e22d3509bcf) | [research_archive/2026-11-16_001055.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_001055.md) | commit UTC: 2026-11-16T00:11:12.000Z
- 원문 blob SHA: 564ad6d811f3826f42db6b7d2e8bfce5bd6d2bd9
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 사용자가 안전하게 제품을 설치, 운영, 유지보수할 수 있도록 보안 관련 필수 정보와 명확한 사용 지침을 디지털 또는 물리적 형태로 제공해야 합니다. 특히 초기 기본 보안 설정(Secure by default) 유지 및 취약점 통지 수신 방법을 포함해
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #204 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안 최소 5년 또는 규정된 기간 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 합니다. 제조사는 제품 출시 전 위험
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 16:55:28 (원문 시간대 미표기)
- 원문: [commit d9312eaafafd32d9c7c75c15122549ac26257b4d](https://github.com/useformotor3/ai-discord-bot/commit/d9312eaafafd32d9c7c75c15122549ac26257b4d) | [research_archive/2026-11-15_165528.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_165528.md) | commit UTC: 2026-11-15T16:55:43.000Z
- 원문 blob SHA: 817cbe72485320591182414453ac68d68273f26a
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안 최소 5년 또는 규정된 기간 동안 발견된 취약점에 대해 무상으로 보안 업데이트(패치)를 제공해야 합니다. 제조사는 제품 출시 전 위험 평가를 통해 산정된 지원 기간(Support Period)을 공개하고, 이를 기술 문서 및 사용자 설명서에 명시해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #205 — P1 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 인터페이스와 서비스가 비활성화된 '기본 설정에 따른 보안(Secure by Default)' 상태여야 합니다. 제조사는 제품의 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:00:53 (원문 시간대 미표기)
- 원문: [commit ab123c829072dd7c1f82d1a12626b01363a13b57](https://github.com/useformotor3/ai-discord-bot/commit/ab123c829072dd7c1f82d1a12626b01363a13b57) | [research_archive/2026-11-15_170053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_170053.md) | commit UTC: 2026-11-15T17:01:18.000Z
- 원문 blob SHA: a0861bde4b9dd10bb6a1853ab529dcbd19f9059d
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 인터페이스와 서비스가 비활성화된 '기본 설정에 따른 보안(Secure by Default)' 상태여야 합니다. 제조사는 제품의 공격 표면(Attack Surface)을 최소화하고, 초기 인증 시 고정된 기본 비밀번호 사용을 원천 차단하는 강력한 접근 통
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #206 — P1 — 서보 드라이브 제조사는 제품 출고 시(Out-of-the-box) 취약한 기본 인증 정보나 불필요한 서비스가 활성화되지 않도록 설정된 'Secure by Default' 상태를 강
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:05:31 (원문 시간대 미표기)
- 원문: [commit 1fe697b76d7ec7101ec14ee77b34858a4ca5b4b2](https://github.com/useformotor3/ai-discord-bot/commit/1fe697b76d7ec7101ec14ee77b34858a4ca5b4b2) | [research_archive/2026-11-15_170531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_170531.md) | commit UTC: 2026-11-15T17:05:52.000Z
- 원문 blob SHA: ec43a4846b32cfdb13a9c4805bec753d048078ce
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품 출고 시(Out-of-the-box) 취약한 기본 인증 정보나 불필요한 서비스가 활성화되지 않도록 설정된 'Secure by Default' 상태를 강제해야 합니다. 사용자가 보안 설정을 수동으로 강화하기 전이라도, 초기 제품 자체의 공격 표면(Attack Surface)을
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #207 — P1 — 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 네트워크 인터페이스와 서비스가 비활성화된 '기본 설정 보안(Secure by Default)' 상태여야 하며, 사용자가 최초 변
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:10:36 (원문 시간대 미표기)
- 원문: [commit 6d35179aa1d9b4a3af86fdc6d814356a935a0e34](https://github.com/useformotor3/ai-discord-bot/commit/6d35179aa1d9b4a3af86fdc6d814356a935a0e34) | [research_archive/2026-11-15_171036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_171036.md) | commit UTC: 2026-11-15T17:10:52.000Z
- 원문 blob SHA: e5c7433d710cd7940586899129c88421bb8149db
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 출고 시점부터 모든 불필요한 네트워크 인터페이스와 서비스가 비활성화된 '기본 설정 보안(Secure by Default)' 상태여야 하며, 사용자가 최초 변경 시 고유의 강력한 자격 증명을 강제하도록 설계되어야 합니다. 또한, 이러한 보안 구성 상태와 위험 평가 결과는 엄격한 기술
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #208 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 동안 발견되는 취약점을 무상으로 자동·수동 패치할 수 있는 보안 업데이트 메커니즘을 제공해야 하며, 이를 위한 취약점 공개 정책을 수립해야
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:15:37 (원문 시간대 미표기)
- 원문: [commit 75e3c6d6f0e01709ff30b056d555062d3cd321d8](https://github.com/useformotor3/ai-discord-bot/commit/75e3c6d6f0e01709ff30b056d555062d3cd321d8) | [research_archive/2026-11-15_171537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_171537.md) | commit UTC: 2026-11-15T17:15:55.000Z
- 원문 blob SHA: 3c9b1edf79bea5015e4448777c2e01165eaeb5c8
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 동안 발견되는 취약점을 무상으로 자동·수동 패치할 수 있는 보안 업데이트 메커니즘을 제공해야 하며, 이를 위한 취약점 공개 정책을 수립해야 합니다. 본 요건은 산업용 제어기기(IIoT/OT)의 은폐 관행을 근절하고, 사용자(PLC/HMI 제조사 및 최종 공장 운영
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #209 — P1 — 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 권한 상승, 무단 접근, 악의적인 설정 변경을 방지하기 위해 안전한 기본 설정(Secure by default) 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:20:40 (원문 시간대 미표기)
- 원문: [commit 7b81665e4956531fb95ce5ab748ce08bc33a4b11](https://github.com/useformotor3/ai-discord-bot/commit/7b81665e4956531fb95ce5ab748ce08bc33a4b11) | [research_archive/2026-11-15_172040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_172040.md) | commit UTC: 2026-11-15T17:20:56.000Z
- 원문 blob SHA: d0107da1dc274543fcb05c06205f93395470c63e
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 초기 출고 시(Out-of-the-box) 권한 상승, 무단 접근, 악의적인 설정 변경을 방지하기 위해 안전한 기본 설정(Secure by default) 상태를 유지해야 합니다. 특히, 제품과 함께 제공되거나 내장된 기본 인증 정보(Default Passwords/Credenti
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #210 — P0 — 제조사는 서보 드라이브의 예상 수명 주기 동안 발견되는 취약점에 대해 추가 비용 청구 없이(Free of charge) 보안 업데이트를 제공해야 하며, 이를 안전하게 배포하고 사용
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:25:33 (원문 시간대 미표기)
- 원문: [commit 335786f3f41bbe9842304551f2ba13330838c731](https://github.com/useformotor3/ai-discord-bot/commit/335786f3f41bbe9842304551f2ba13330838c731) | [research_archive/2026-11-15_172533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_172533.md) | commit UTC: 2026-11-15T17:25:50.000Z
- 원문 blob SHA: cf21185c5b01f206b9d702993525363b68199782
- 핵심 주장 주제(원문 요약 첫 부분): 제조사는 서보 드라이브의 예상 수명 주기 동안 발견되는 취약점에 대해 추가 비용 청구 없이(Free of charge) 보안 업데이트를 제공해야 하며, 이를 안전하게 배포하고 사용자가 검증할 수 있는 무결성 механиз(Mechanism)을 기본 탑재해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #211 — P1 — 핵심 내용 1: 산업용 서보 드라이브는 출고 시(Out-of-the-box) 모든 공격 표면(불필요한 네트워크 서비스, 디버그 포트 등)이 비활성화되거나 가장 안전한 상태로 설정된
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:30:46 (원문 시간대 미표기)
- 원문: [commit 51d3698a8037fc92c5913608d4c204c7bac6584c](https://github.com/useformotor3/ai-discord-bot/commit/51d3698a8037fc92c5913608d4c204c7bac6584c) | [research_archive/2026-11-15_173046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_173046.md) | commit UTC: 2026-11-15T17:31:02.000Z
- 원문 blob SHA: 37555ce4216724faee54205102a92420feba43e3
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브는 출고 시(Out-of-the-box) 모든 공격 표면(불필요한 네트워크 서비스, 디버그 포트 등)이 비활성화되거나 가장 안전한 상태로 설정된 'Secure by Default' 상태를 반드시 유지해야 합니다. 핵심 내용 2: 최초 인증을 위해 제조사가 부여한 기본
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #212 — P1 — 핵심 내용 1: 산업용 서보 드라이브는 출고 시점(Secure by default)부터 불필요한 네트워크 서비스, 포트, 디버그 인터페이스 등이 비활성화되어 있어야 하며, 사용자가
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:35:41 (원문 시간대 미표기)
- 원문: [commit 88d695b729f2495e82409299511d219698eabdc6](https://github.com/useformotor3/ai-discord-bot/commit/88d695b729f2495e82409299511d219698eabdc6) | [research_archive/2026-11-15_173541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_173541.md) | commit UTC: 2026-11-15T17:35:58.000Z
- 원문 blob SHA: dd026f2d98ca8c1360a173aeb9514b42c6adfdc4
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용 1: 산업용 서보 드라이브는 출고 시점(Secure by default)부터 불필요한 네트워크 서비스, 포트, 디버그 인터페이스 등이 비활성화되어 있어야 하며, 사용자가 명시적으로 활성화하지 않는 한 공격 표면이 최소화된 상태를 유지해야 합니다. 핵심 내용 2: 제조사는 제품의 초기 설정 과정
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #213 — P0 — 핵심 내용: 산업용 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 하며, 업데이트 가용성을 보장해야 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:40:37 (원문 시간대 미표기)
- 원문: [commit 8c4f3539c67957b3f939c22436125c7fa89fff09](https://github.com/useformotor3/ai-discord-bot/commit/8c4f3539c67957b3f939c22436125c7fa89fff09) | [research_archive/2026-11-15_174037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_174037.md) | commit UTC: 2026-11-15T17:40:54.000Z
- 원문 blob SHA: ad73f64e13f32546f1bd9e9532c1d3d1867059d2
- 핵심 주장 주제(원문 요약 첫 부분): 핵심 내용: 산업용 서보 드라이브 제조사는 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 하며, 업데이트 가용성을 보장해야 합니다. 핵심 내용: 배포된 보안 업데이트는 초기 펌웨어와 마찬가지로 암호화 서명 등을 통해 무결성이 검증되어야 하며, 업데이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #214 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 합니다. 이는 제조사가 소프트웨어
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:45:34 (원문 시간대 미표기)
- 원문: [commit 8cbbd648888a9d9ab18f063609c975aca1556a0d](https://github.com/useformotor3/ai-discord-bot/commit/8cbbd648888a9d9ab18f063609c975aca1556a0d) | [research_archive/2026-11-15_174534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_174534.md) | commit UTC: 2026-11-15T17:45:50.000Z
- 원문 blob SHA: ba918c085b51e85a753b466f7903210314669fc3
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 합니다. 이는 제조사가 소프트웨어 결함 수정을 유료 서비스(예: 유지보수 계약)와 연계하는 것을 원천 차단하고, 시장에 출시된 제품의 전 생애주기 동안의 실질
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #215 — P1 — 서보 드라이브 등 디지털 요소를 갖춘 제품은 출고 시 무단 액세스를 방지하기 위한 안전한 기본 설정(Secure by default)과 함께 제공되어야 하며, 시장 출시 시점에 알
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:50:36 (원문 시간대 미표기)
- 원문: [commit df607eed7c7ccf6db0a80c897198bd96bafd390c](https://github.com/useformotor3/ai-discord-bot/commit/df607eed7c7ccf6db0a80c897198bd96bafd390c) | [research_archive/2026-11-15_175036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_175036.md) | commit UTC: 2026-11-15T17:50:51.000Z
- 원문 blob SHA: e67e92b9ce86021200e5a25e0640190bfce7c1e8
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 등 디지털 요소를 갖춘 제품은 출고 시 무단 액세스를 방지하기 위한 안전한 기본 설정(Secure by default)과 함께 제공되어야 하며, 시장 출시 시점에 알려진 취약점이 없어야(Free of known vulnerabilities) 합니다. 이는 CRA Annex I에 명시된 필수
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #216 — P1 — 산업용 서보 드라이브는 공장 출고 시점부터 인증되지 않은 접근, 불필요한 포트 및 서비스가 원천 차단된 ‘기본 안전 설정(Secure by Default)’ 상태를 유지해야 하며,
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 17:55:35 (원문 시간대 미표기)
- 원문: [commit 2e6a998f0db43cbc198cd1689a951e8e985b4884](https://github.com/useformotor3/ai-discord-bot/commit/2e6a998f0db43cbc198cd1689a951e8e985b4884) | [research_archive/2026-11-15_175535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_175535.md) | commit UTC: 2026-11-15T17:55:49.000Z
- 원문 blob SHA: 40906394b6d57a119c4f38e1c89d7bf02c345ab0
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시점부터 인증되지 않은 접근, 불필요한 포트 및 서비스가 원천 차단된 ‘기본 안전 설정(Secure by Default)’ 상태를 유지해야 하며, 사용자가 명시적으로 활성화하기 전까지는 공격 표면을 최소화하도록 설계되어야 합니다.
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #217 — P0 — 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트를 제공하고, 이를 적시에 안전하게 배포할 수 있는 가용성을 보장해야 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:00:53 (원문 시간대 미표기)
- 원문: [commit 06a3346ad8dd56e49063d43069a7a61cc3157aa8](https://github.com/useformotor3/ai-discord-bot/commit/06a3346ad8dd56e49063d43069a7a61cc3157aa8) | [research_archive/2026-11-15_180053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_180053.md) | commit UTC: 2026-11-15T18:01:08.000Z
- 원문 blob SHA: 94c76cf1798d894dad0ff9d5cc3eb8942c809742
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점에 대한 무상 보안 업데이트를 제공하고, 이를 적시에 안전하게 배포할 수 있는 가용성을 보장해야 합니다. 사용자가 불필요한 비용이나 기술적 장벽 없이 중요한 패치를 적용할 수 있도록 지원함으로써, 산업용 시스템 전체의 사이
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-15 #218 — P0 — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점을 무상으로 조치하고 보안 업데이트를 제공해야 합니다. 사용자(공장 운영자)가 추가 비용 없이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 18:05:30 (원문 시간대 미표기)
- 원문: [commit d7df4f97330c18ce1f62c0ef547dada568aefd72](https://github.com/useformotor3/ai-discord-bot/commit/d7df4f97330c18ce1f62c0ef547dada568aefd72) | [research_archive/2026-11-15_180530.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-15_180530.md) | commit UTC: 2026-11-15T18:05:54.000Z
- 원문 blob SHA: 46a434b99a90019c17067ddb7f8881cb13b9cc35
- 핵심 주장 주제(원문 요약 첫 부분): 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년) 발견된 취약점을 무상으로 조치하고 보안 업데이트를 제공해야 합니다. 사용자(공장 운영자)가 추가 비용 없이 보안 패치 및 업데이트에 접근할 수 있도록 보장하는 체계를 기술 문서 및 상업적 계약에 명시해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #4 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 모든 보안 취약점을 예외 없이 무상(Cost-free)으로 패치해야 하며, 사용자 개입을 최소화하여 이를 적용할 수 있는 보안 
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:15:38 (원문 시간대 미표기)
- 원문: [commit 38b3456a7b576221144945922a5b71887d702899](https://github.com/useformotor3/ai-discord-bot/commit/38b3456a7b576221144945922a5b71887d702899) | [research_archive/2026-11-16_001538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_001538.md) | commit UTC: 2026-11-16T00:15:54.000Z
- 원문 blob SHA: f213e7b8210c993d769e256e65ad7f807efe9978
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 모든 보안 취약점을 예외 없이 무상(Cost-free)으로 패치해야 하며, 사용자 개입을 최소화하여 이를 적용할 수 있는 보안 업데이트 배포 메커니즘을 기본(Default)으로 제공해야 합니다. 이는 상업적 유지보수 계약과 무관하게 제품 수명주기 동안 
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(8)–(9), Annex I Part II(5)–(8): support period 원칙 최소 5년, expected use <5년이면 그 기간. 무료 보안 업데이트는 Part II(8) 원칙이며 tailor-made product/business user 합의 예외. Article 13(9) 업데이트 가용성과 구분.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #5 — P0 — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 무상으로 자동·수동 업데이트 형태로 즉시 패치해야 하며, 심각한 취약점이
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:20:38 (원문 시간대 미표기)
- 원문: [commit e580a2e75da2e57b8e3fd4b7982808883aa1b410](https://github.com/useformotor3/ai-discord-bot/commit/e580a2e75da2e57b8e3fd4b7982808883aa1b410) | [research_archive/2026-11-16_002038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_002038.md) | commit UTC: 2026-11-16T00:20:55.000Z
- 원문 blob SHA: 368277a32e41de1281abfaf4834e64f1a06af6bb
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 무상으로 자동·수동 업데이트 형태로 즉시 패치해야 하며, 심각한 취약점이나 사이버 침해 사고 발생 시 24시간 이내에 EU CSIRTs Network 및 ENISA에 의무적으로 조기 경보를 통지해야
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 14(1)–(8): actively exploited vulnerability와 severe incident 구분. AEV 24h/72h 및 조치 가용 후 14일 final report; severe incident 24h/72h 및 1개월 final report. SRP/CSIRT coordinator·ENISA 경로와 Article 14(8) 사용자 통지 별도.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #6 — P1 — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 기본 자격증명, 포트, 서비스가 가장 안전한 상태로 설정된 'Secure by default' 상태를 유지해
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:25:31 (원문 시간대 미표기)
- 원문: [commit e8b7431ca4df391ee53ca8735fe6c89cc6f145f1](https://github.com/useformotor3/ai-discord-bot/commit/e8b7431ca4df391ee53ca8735fe6c89cc6f145f1) | [research_archive/2026-11-16_002531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_002531.md) | commit UTC: 2026-11-16T00:25:48.000Z
- 원문 blob SHA: f16d74814357341c7b9c2475279f11f05cc887e0
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 기본 자격증명, 포트, 서비스가 가장 안전한 상태로 설정된 'Secure by default' 상태를 유지해야 합니다. 제조사는 사용자가 최초 설치 시 취약한 기본 패스워드를 강제로 변경하도록 유도하거나 비활성화된 상태의 불필요한 공
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 강제 비밀번호 변경, 모든 포트/JTAG/UART 차단은 보편적 명시 구현수단이 아니며 위험평가·제품 기능과 분리.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #7 — P0 — 산업용 서보 드라이브 제조사는 CRA Annex II에 따라 제품의 안전한 설치, 초기 구성, 안전한 기본 설정(Secure by default) 유지 및 취약점 통지 수신을 위한
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:30:50 (원문 시간대 미표기)
- 원문: [commit 34684a441277d6ca68a307562717f0eb2fc6614f](https://github.com/useformotor3/ai-discord-bot/commit/34684a441277d6ca68a307562717f0eb2fc6614f) | [research_archive/2026-11-16_003050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_003050.md) | commit UTC: 2026-11-16T00:31:06.000Z
- 원문 blob SHA: d4aceb12f1600706b022c6a6ef0c64be5f2f63a8
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브 제조사는 CRA Annex II에 따라 제품의 안전한 설치, 초기 구성, 안전한 기본 설정(Secure by default) 유지 및 취약점 통지 수신을 위한 명확한 보안 지침과 정보를 사용자에게 제공해야 합니다.
- 우선순위/검증 쟁점: P0 — EUR-Lex Article 13(17)–(19), Annex II(1)–(9): 사용자 정보·지침은 Article 13(18), 종료일 표시는 13(19), Annex II point 8(a)–(f); SBOM 사용자 접근은 point 9 조건부.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.

### 2026-11-16 #8 — P1 — 산업용 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 무단 접근을 원천 차단하기 위해 변경 가능한 기본 패스워드가 없거나, 사용자가 최초 설치 시 강력한 고유 인
- 상태: NEW / NOT_YET_AUDITED | 확인일: 2026-11-16 | 생성: 00:35:33 (원문 시간대 미표기)
- 원문: [commit 844ba4a80910dea52b5b49713b3b203c8d84ddb6](https://github.com/useformotor3/ai-discord-bot/commit/844ba4a80910dea52b5b49713b3b203c8d84ddb6) | [research_archive/2026-11-16_003533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-16_003533.md) | commit UTC: 2026-11-16T00:35:50.000Z
- 원문 blob SHA: 21a734ccadc3c7a78b84ac459118aa0a323f1951
- 핵심 주장 주제(원문 요약 첫 부분): 산업용 서보 드라이브는 공장 출고 시점(Out-of-the-box)부터 무단 접근을 원천 차단하기 위해 변경 가능한 기본 패스워드가 없거나, 사용자가 최초 설치 시 강력한 고유 인증 정보를 강제로 설정하도록 강제하는 'Secure by Default' 상태를 유지해야 합니다. 또한, 불필요한 기본 활성 
- 우선순위/검증 쟁점: P1 — EUR-Lex Annex I Part I(2)(b),(d),(j),(l): secure-by-default·접근통제·공격표면 제한·관련 내부활동 기록/모니터링(opt-out). 특정 비밀번호 변경·포트/JTAG/UART 차단은 보편적 명시 구현수단이 아님.
- 판정: 파일 UNVERIFIED; Raw Text Quote/개별 주장 NOT_YET_AUDITED; 제품 적용성 UNVERIFIED. 전체 Pass A/B/C 미완료.
