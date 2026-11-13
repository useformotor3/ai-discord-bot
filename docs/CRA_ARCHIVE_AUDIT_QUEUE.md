# CRA Main Archive Audit Queue

> 확인일: 2026-11-13  
> 대상 저장소: [useformotor3/ai-discord-bot](https://github.com/useformotor3/ai-discord-bot)  
> 감사 대상 브랜치: `main` (읽기 전용)  
> 기록 브랜치: `cra-project-foundation`  
> 기준점: 기존 감사 기록의 마지막 보고서 #128, commit `15ceea4b9477b8c0928352a5b4228c0508e88daa`  
> 이번 확인 main HEAD: `bd50257a80c0524402c70a7da420043ecfa0f490` (Auto-archive: Research report #7)

## 실행 결과 요약

- 기준점 #128 이후 main에서 **167개 보고서 commit 및 167개 신규 archive 파일** 확인.
- 신규 보고서: #129–#288 (2026-11-12 일일 카운트) 및 #1–#7 (2026-11-13 일일 카운트 리셋 후).
- compare 결과: `ahead 167 / behind 0`; 변경 파일 169개 = archive 167개 + `history.json` + `state.json`.
- `history.json`은 신규 기록을 추가했고, `state.json`은 날짜 `2026-11-13`, count `7`으로 갱신됨. 날짜 경계에서 일일 count가 288에서 1로 재시작한 것으로 보이며, 누적 history와 archive 경로로 개별 보고서를 매핑했다.
- 이번 실행에서 **23개 archive는 모델 과부하/조사 지연 경고 문구만 포함**한다. 실질 CRA 조사 주장으로 간주하지 않았고 P3로 분류했다.
- 우선순위 분포: P0 111 / P1 33 / P2 0 / P3 23.
- 기존 대기열 문서는 작업 브랜치에 없어 새로 생성했다. 모든 167개 항목은 중복 없이 등록했다.
- 이번 실행은 **대기열 등록과 법령 기준선 사전 확인**이다. 개별 보고서의 Pass A/B/C 감사는 수행하지 않았으므로 파일 판정은 전부 UNVERIFIED, 인용문/개별 주장은 NOT_YET_AUDITED로 유지한다.

## 우선순위 정의

- **P0**: 법령 적용범위·기한·예외·제품 분류·지원기간·무상 업데이트·SBOM·사용자 정보 등 잘못 인용하면 규제 판단에 직접 영향을 주는 주장.
- **P1**: Secure-by-default, 펌웨어/OTA 업데이트, 인증·무결성, 네트워크/디버그 인터페이스 등 위험기반 기술 설계 주장.
- **P2**: 위 두 범주 외 실질 주제. 개별 내용 확인 후 재분류.
- **P3**: 모델 호출 실패 경고 등 실질 조사 내용이 없는 파일. 조사 성공으로 취급할 수 있는지 운영 경로도 확인.

우선순위는 감사 순서를 정하는 triage 값이며 검증 판정이 아니다.

## 사전 확인한 공식 기준선 (개별 보고서 검증 완료를 뜻하지 않음)

### EUR-Lex — Regulation (EU) 2024/2847

공식 현행 법령 본문을 열어 조항과 주변 문맥을 확인했다: [EUR-Lex CELEX 32024R2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847), OJ L 2024/2847, 20 November 2024.

- **Article 13(8)**: 지원기간은 제품의 예상 사용기간을 반영해야 한다. 원칙적으로 최소 5년이지만, 제품이 5년 미만 사용될 것으로 예상되면 지원기간은 그 예상 사용기간에 대응한다. 따라서 “모든 제품은 무조건 5년”으로 단정하지 않는다.
- **Article 13(9)**: 지원기간 중 사용자에게 제공된 각 보안 업데이트는 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 이용 가능해야 한다. 이는 지원기간 자체와 별도다.
- **Article 14(1)–(5)**: 신고 대상은 제품에 포함된 actively exploited vulnerability와 제품 보안에 영향을 미치는 severe incident의 두 트랙이다. 취약점 트랙은 인지 후 24시간 조기경고, 72시간 취약점 신고, 시정/완화 조치 가능 후 14일 이내 최종보고. 심각한 사고 트랙은 24시간 조기경고, 72시간 사고 신고, 72시간 신고 후 1개월 이내 최종보고다. 모든 일반 취약점/버그를 Article 14 신고 대상으로 확대하지 않는다.
- **Article 14(7), Article 16**: 지정 CSIRT를 통한 단일 보고 플랫폼 경로이며 ENISA에 동시 접근 가능하도록 한다. 제조사 내부 시스템이 ENISA에 직접 자동 신고해야 한다는 문언으로 바꾸지 않는다.
- **Article 71(2)**: Article 14는 2026-09-11부터 적용되고, CRA의 주된 의무는 2027-12-11부터 적용된다.
- **Annex I Part I**: (1)은 위험기반 사이버보안 수준, (2)(a)–(m)은 제품 속성 요구다. (2)(b) secure-by-default, (2)(c) 해당하는 경우 기본 활성 자동 보안 업데이트와 opt-out/일시 연기, (2)(d) 적절한 접근통제, (2)(e)/(f) 기밀성·무결성, (2)(j) 외부 인터페이스를 포함한 공격표면 제한을 구분한다.
- **Annex I Part II(1)–(8)**: 제조사의 취약점 처리 프로세스다. SBOM은 (1)의 top-level dependencies, CVD 정책은 (5), 취약점 정보공유/contact는 (6), 안전한 업데이트 배포는 (7), 지체 없는 무상 보안 업데이트는 (8)에 있다. (8)은 tailor-made 제품에 대해 제조사와 business user가 달리 합의한 경우 예외가 있다.
- **Annex II point 1–9**: 사용자 정보·지침서 구조는 번호 1–9다. point 9의 SBOM 접근 위치는 제조사가 SBOM을 사용자에게 제공하기로 결정한 경우에만 조건부로 요구된다.
- **Article 7 및 Annex III**: Important Product 분류는 열거된 제품 범주와 core functionality에 따라 판단한다. 서보 드라이브라는 일반 명칭만으로 Class I/II를 지정하지 않는다.

### European Commission

- [Commission guidance publication page](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)에서 **C(2026) 5252**가 2026-07-27 게시된 사실, 지원기간·제품 범위·substantial modification·신고·위험평가를 다룬다는 점, 그리고 안내문 자체가 non-binding이라는 점을 확인했다.
- Commission guidance는 법령 원문을 대체하거나 법적 의무/적용일을 변경하지 않는다. 쟁점 해석 보조자료로 사용하고, 충돌 시 Regulation 본문과 구분한다.

### ENISA

- [ENISA Single Reporting Platform](https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp) 및 [ENISA SRP FAQ](https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions)를 확인했다.
- SRP는 2026-09-11부터 제조사의 Article 14 의무 신고에 사용되며 actively exploited vulnerabilities와 severe incidents를 대상으로 한다. ENISA FAQ는 2026-10-15 업데이트로 표시된다.
- ENISA SRP 페이지는 2026-11-04 버전 1.3 업그레이드 및 관련 안내문 갱신 중이라고 표시한다. 실제 신고 절차를 적용할 때는 최신 ENISA user guide/FAQ/glossary를 다시 확인해야 한다.

### 제조사 기술 주장 및 제품 적용성

- 이번 일괄 등록 단계에서 특정 제조사 MCU/서보 드라이브 기능을 VERIFIED 처리하지 않았다. 실제 서보 드라이브 SKU, ST MCU 주문 코드, 제품 핵심 기능·의도된 용도·실제 네트워크/원격 업데이트 구성은 미확정이다.
- Secure Boot, 서명 검증, anti-rollback, A/B bank, TPM/Root of Trust, JTAG/UART 차단, 강제 비밀번호 변경 등은 법령의 보편적 명시 구현수단이라고 단정하지 않는다. CRA 위험기반 요구와 구체 설계 선택을 분리하고, 제조사 공식 데이터시트/RM/errata 및 제품별 설계 증거를 별도 확인한다.

## 감사 프로토콜 및 판정 규칙

1. **Pass A — claim extraction**: 각 보고서의 주장, 법령 인용, Raw Text Quote, 제조사 기술 주장, 제품 적용성 가정을 분리해 추출한다.
2. **Pass B — authoritative source reopening**: EUR-Lex의 정확한 현행 조항/Annex/point, Commission 공식 guidance, ENISA 공식 자료, 제조사 공식 원문을 다시 열고 문서 버전·정확한 위치·주변 문맥을 확인한다.
3. **Pass C — countercheck**: 인접 조항, 예외, 적용일, 범위, 제품 분류 및 반대 근거를 확인한다.
4. URL 접속 성공이나 검색 snippet만으로 VERIFIED 처리하지 않는다. 같은 AI 세션의 반복 확인은 독립 제3자 법률 검토가 아니다.
5. 파일 단위 판정은 VERIFIED / PARTIALLY_VERIFIED / CONFLICT / UNVERIFIED 중 하나로 한다. Raw Text Quote와 개별 주장은 별도 판정한다. 제품별 적용성은 법령 문언 검증과 별도다.

## 신규 보고서 대기열


## 2026-11-12 reports #129–#288

### Report #129 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 10:40:43 (원문 Date; 시간대 미표기)
- 원문 commit: [5073799b393689b43aba4805f10b39e67d59c279](https://github.com/useformotor3/ai-discord-bot/commit/5073799b393689b43aba4805f10b39e67d59c279)
- 원문 파일: [research_archive/2026-11-12_104043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_104043.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 원격(OTA/네트워크 기반) 펌웨어 및 소프트웨어 업데이트 메커니즘의 무결성 및 인증(Secure Update Mechanism) — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라, 악성 변조나 무단 덮어쓰기를 원천 차단하기 위해 암호학적으로 안전하고 검증된 원격 소프트웨어 및 펌웨어 업데이트(Secure Update) 메커니즘을 반드시 구현해야 합니다. 특히 업데이트 실패 시
- 보고서 기재 조항(미검증): Annex I, Annex I), Part I(Cybersecurity requirements), Annex I (Cybersecurity requirements), Part I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #130 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 10:45:33 (원문 Date; 시간대 미표기)
- 원문 commit: [e695486e1e2b4fa12d9acbb0c07653981da4e54c](https://github.com/useformotor3/ai-discord-bot/commit/e695486e1e2b4fa12d9acbb0c07653981da4e54c)
- 원문 파일: [research_archive/2026-11-12_104533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_104533.md)
- 핵심 주장 주제: '디지털 제품 생명주기 전반에 걸친 취약점 무상 자동 공지 및 보안 업데이트(Coordinated Vulnerability Disclosure & Security Updates Handling)' — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(대개 10년 이상) 동안 발견된 취약점에 대해 무상으로 보안 업데이트(Patches/Updates)를 제공해야 하며, 이를 위한 안전한 배포 메커니즘과 취약점 처리 정책을 기술 
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I, Article 13 (Manufacturer obligations), Annex I (Cybersecurity requirements - P
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #131 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 10:50:41 (원문 Date; 시간대 미표기)
- 원문 commit: [cd81902c9fd6311ba3f43895c598bddf0e675dd0](https://github.com/useformotor3/ai-discord-bot/commit/cd81902c9fd6311ba3f43895c598bddf0e675dd0)
- 원문 파일: [research_archive/2026-11-12_105041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_105041.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 원격 진단 및 자동화된 보안 업데이트(Automated Security Updates & Remote Diagnostics) 메커니즘 — 산업용 서보 드라이브는 CRA Annex I에 따라 취약점 패치 및 펌웨어 업데이트를 안전하고 자동화된 방식으로 제공해야 하며, 특히 고속 실시간 제어 환경에서 업데이트 실패 시 물리적 위험을 방지하기 위한 트랜잭션 기반(A/B 파티션) 롤백 메커니즘과 
- 보고서 기재 조항(미검증): Annex I), Annex I, Annex I (Requirements with which produc, Part I (Cybersecurity requirements), Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #132 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 10:55:38 (원문 Date; 시간대 미표기)
- 원문 commit: [cb680879837a9e5c29619039fe3b1f6b02d932f2](https://github.com/useformotor3/ai-discord-bot/commit/cb680879837a9e5c29619039fe3b1f6b02d932f2)
- 원문 파일: [research_archive/2026-11-12_105538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_105538.md)
- 핵심 주장 주제: "디지털 요소가 포함된 제품의 지원 기간 동안의 취약점 무료 무상 패치 의무 및 보안 업데이트 수명주기 관리(Vulnerability Handling & Free Security Updates)" — 산업용 서보 드라이브 제조사는 CRA에 따라 최소 5년 또는 제품의 예상 사용 기간 중 더 긴 기간 동안 발견된 취약점에 대해 **추가 비용 청구 없이(Free of charge)** 보안 업데이트 및 패치를 제공해야 하며, 이를 위한 투
- 보고서 기재 조항(미검증): Annex I), Article 11 (Obligations of manufacturers), Annex I, Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #133 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:00:52 (원문 Date; 시간대 미표기)
- 원문 commit: [95900eb42d046763c7a25cd63a033e08a64119da](https://github.com/useformotor3/ai-discord-bot/commit/95900eb42d046763c7a25cd63a033e08a64119da)
- 원문 파일: [research_archive/2026-11-12_110052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_110052.md)
- 핵심 주장 주제: 산업용 서보 드라이브의 '소프트웨어 취약점 무상 공개 및 처리(Vulnerability Disclosure and Free-of-Charge Patching)와 연계된 공급망 생명주기 관리' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 추가 비용 없이(Free-of-charge) 적시에 제공해야 하며, 이를 위해 공급망 전반(서드파티 컴포넌트 포함)의 취약점 처리 프로세스를 기술 문서 및 사용자
- 보고서 기재 조항(미검증): Article 11, Annex I, Part II), Annex I(, Annex II
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #134 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:05:36 (원문 Date; 시간대 미표기)
- 원문 commit: [d681afb300443ec4f2a9acf19edded131c20ed4f](https://github.com/useformotor3/ai-discord-bot/commit/d681afb300443ec4f2a9acf19edded131c20ed4f)
- 원문 파일: [research_archive/2026-11-12_110536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_110536.md)
- 핵심 주장 주제: '취약점 무상 패치 및 보안 업데이트 전달 메커니즘(Vulnerability Correction & Secure Update Delivery)' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 최소 5년(또는 제품의 예상 수명 기간) 동안 추가 비용(무상)으로 보안 업데이트를 제공해야 하며, 이를 안전하게 전달할 수 있는 자동화된 무결성 검증 기반의 업데이트 배포 메커니즘을 강제 적용해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements) Part I, Annex I (Cybersecurity requirements), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #135 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:10:40 (원문 Date; 시간대 미표기)
- 원문 commit: [0457cc57fa3fe404553259e568f4d52f93e856ac](https://github.com/useformotor3/ai-discord-bot/commit/0457cc57fa3fe404553259e568f4d52f93e856ac)
- 원문 파일: [research_archive/2026-11-12_111040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_111040.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 '취약점 무상 패치 및 보안 업데이트 배포의 기술적·운영적 의무(Vulnerability handling and security updates)' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 최소 5년(또는 제품의 예상 수명 동안) 보안 업데이트를 무상으로 제공해야 하며, 이를 안전하게 전달할 수 있는 무결성이 보장된 자동 업데이트 메커니즘을 구현해야 합니다. 또한, 
- 보고서 기재 조항(미검증): Annex I, Part I, Article 14, Annex I), Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #136 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:15:46 (원문 Date; 시간대 미표기)
- 원문 commit: [306c44cf68859a9fee71213fc2cd597de5935954](https://github.com/useformotor3/ai-discord-bot/commit/306c44cf68859a9fee71213fc2cd597de5935954)
- 원문 파일: [research_archive/2026-11-12_111546.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_111546.md)
- 핵심 주장 주제: '디지털 요소가 포함된 제품의 지원 기간 종료 시점의 취약점 처리 및 안전한 폐기/전환 절차(End-of-Support 및 취약점 무상 패치 의무의 운영적 한계)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안(최소 5년) 보안 취약점 무료 패치를 제공해야 하며, 지원 종료(End of Support) 시점에는 잔여 리스크를 사용자에게 명확히 고지하고 안전한 가동 중단 또는 폐기를 유도하는 생명주기 관리 체계를
- 보고서 기재 조항(미검증): Annex I(, Article 13 (Manufacturer obligations), Annex I, Article 13(6), Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #137 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:20:39 (원문 Date; 시간대 미표기)
- 원문 commit: [08931f42ed1201f5e9bdab4f53691eed6c691347](https://github.com/useformotor3/ai-discord-bot/commit/08931f42ed1201f5e9bdab4f53691eed6c691347)
- 원문 파일: [research_archive/2026-11-12_112039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_112039.md)
- 핵심 주장 주제: '취약점 자동 무상 배포 및 취약점 정보 공개(Coordinated Vulnerability Disclosure 및 Free-of-charge Security Updates)' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 사용자에게 **추가 비용 없이(free of charge)** 적시에 제공해야 하며, 이를 위한 안전한 자동/수동 업데이트 메커니즘과 취약점 처리 프로세스를 기술 문서에 명시하
- 보고서 기재 조항(미검증): Article 13 (Obligations of manufacturers), Annex I (Section I, Annex I, Article 13 (7)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #138 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:25:39 (원문 Date; 시간대 미표기)
- 원문 commit: [bf3716d7b5e0025fad9b101a57ce6583c559e8ae](https://github.com/useformotor3/ai-discord-bot/commit/bf3716d7b5e0025fad9b101a57ce6583c559e8ae)
- 원문 파일: [research_archive/2026-11-12_112539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_112539.md)
- 핵심 주장 주제: "보안 취약점 처리 및 자동화된 무상 보안 업데이트(Vulnerability Handling & Free Security Updates)" — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 동안 발견되는 취약점을 무상으로 자동화된 방식(또는 사용자 통지 기반)으로 패치해야 하며, 이를 위한 취약점 처리 정책을 수립하고 공개해야 합니다. 특히 OT(운영 기술) 환경의 특수성을 고려하여 안전한 업데이트 배포 메커니즘을 강제
- 보고서 기재 조항(미검증): Annex I), Article 14, Annex I, Part I), Part II)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #139 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:30:51 (원문 Date; 시간대 미표기)
- 원문 commit: [0ad2c87ab5895c4e787ef290fb11e91fee6dfaa3](https://github.com/useformotor3/ai-discord-bot/commit/0ad2c87ab5895c4e787ef290fb11e91fee6dfaa3)
- 원문 파일: [research_archive/2026-11-12_113051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_113051.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 보안 업데이트 배포 생명주기 관리(Vulnerability Handling & Free-of-Charge Security Updates)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 모든 취약점을 무상으로 조치해야 하며, 자동화된 채널을 통해 보안 업데이트가 안전하고 무결하게 배포되도록 기술적 조치를 강제받습니다. 이는 단순한 패치 제공을 넘어 서보 드라
- 보고서 기재 조항(미검증): Annex I, Part I, Article 13), Part II, Article 14)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #140 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:35:32 (원문 Date; 시간대 미표기)
- 원문 commit: [cbf12a50acc7897027179fdf82bc895362617cec](https://github.com/useformotor3/ai-discord-bot/commit/cbf12a50acc7897027179fdf82bc895362617cec)
- 원문 파일: [research_archive/2026-11-12_113532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_113532.md)
- 핵심 주장 주제: '취약점 무상 처리 및 보안 업데이트 수명 주기 관리(Vulnerability Handling & Security Updates Lifecycle)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 또는 최소 10년 동안 발견된 취약점을 **무상으로 안전하게 패치(Vulnerability correction free of charge)**하여 배포해야 하며, 이를 위한 보안 업데이트 전달 메커니즘을 
- 보고서 기재 조항(미검증): Annex I (Essential Requirements), Part I (Cybersecurity requirements), Article 14 (Obligations of manufacturers), Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #141 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:40:38 (원문 Date; 시간대 미표기)
- 원문 commit: [0152039b8b173681aac8affcd9e3d9aa747faa85](https://github.com/useformotor3/ai-discord-bot/commit/0152039b8b173681aac8affcd9e3d9aa747faa85)
- 원문 파일: [research_archive/2026-11-12_114038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_114038.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 취약점 처리 프로세스(Vulnerability Handling & Free of Charge Security Updates)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 추가 비용 청구 없이(Free of charge) 무상으로 패치해야 하며, 이를 위한 체계적인 취약점 공개 및 처리 프로세스를 구축·유지해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part I, Article 14, Article 14 (Obligations of manufacturers), Annex I (Requirements with which produc
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #142 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:45:38 (원문 Date; 시간대 미표기)
- 원문 commit: [34600b91d68b0111dd8016c9d5fdc533ee54174a](https://github.com/useformotor3/ai-discord-bot/commit/34600b91d68b0111dd8016c9d5fdc533ee54174a)
- 원문 파일: [research_archive/2026-11-12_114538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_114538.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 취약점 핸들링 프로세스(Coordinated Vulnerability Disclosure)' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점과 관련 보안 업데이트를 제품의 예상 수명 동안(최소 5년 또는 주요 시장 주기에 맞춰) 사용자에게 **무상(Cost-free)으로 적시에 제공**해야 하며, 취약점 조율 공개(CVD) 프로세스를 운영할 법적 의무를 집니다.
- 보고서 기재 조항(미검증): Annex I(, Article 11 (Obligations of manufacturers), Annex I (Essential requirements), Part I (Requirements relating to the c, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #143 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:50:41 (원문 Date; 시간대 미표기)
- 원문 commit: [024fbd36b57b7d0495f2722e466cd3fb005caae0](https://github.com/useformotor3/ai-discord-bot/commit/024fbd36b57b7d0495f2722e466cd3fb005caae0)
- 원문 파일: [research_archive/2026-11-12_115041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_115041.md)
- 핵심 주장 주제: '지속적인 취약점 무상 처리 의무 및 보안 업데이트 수명 주기 관리(Vulnerability Handling & Coordinated Vulnerability Disclosure)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견되는 취약점을 무상으로 자동 패치해야 하며, 안전한 소프트웨어 업데이트 배포 메커니즘과 조정된 취약점 공개(CVD) 프로세스를 기술 문서에 입증해야 합니다.
- 보고서 기재 조항(미검증): Article 11, Annex I, Part I), Part I, Article 14)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #144 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 11:55:34 (원문 Date; 시간대 미표기)
- 원문 commit: [5e262ddf1e8a807d7bfd4849a017365f8316ae0d](https://github.com/useformotor3/ai-discord-bot/commit/5e262ddf1e8a807d7bfd4849a017365f8316ae0d)
- 원문 파일: [research_archive/2026-11-12_115534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_115534.md)
- 핵심 주장 주제: '취약점 무상 패치 및 지원 기간(Support Period)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 최소 5년 또는 제품의 예상 수명 기간 중 긴 기간 동안 발견된 취약점에 대해 **보안 업데이트를 무상(without charge)으로 제공**해야 하며, 단종(End-of-Life) 시점과 안전한 폐기 절차를 명확히 고지해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I (Requirements for products with, Article 13 (Obligations of manufacturers), Annex I, Article 13(7)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #145 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:00:58 (원문 Date; 시간대 미표기)
- 원문 commit: [b21cc907bebef837fd9da739b045181cd7aa539e](https://github.com/useformotor3/ai-discord-bot/commit/b21cc907bebef837fd9da739b045181cd7aa539e)
- 원문 파일: [research_archive/2026-11-12_120058.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_120058.md)
- 핵심 주장 주제: '디지털 제품에 대한 명확한 보안 업데이트 및 취약점 공개 수명주기(Vulnerability handling and coordinated disclosure during the expected product lifetime)' — 서보 드라이브 제조사는 CRA에 따라 최소 5년 또는 제품의 예상 사용 기간 동안 발견된 취약점에 대해 **무상으로 보안 업데이트를 제공**해야 하며, 제3자가 보고한 취약점을 안전하게 접수하고 패치할 수 있
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I, Part II, Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #146 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:05:32 (원문 Date; 시간대 미표기)
- 원문 commit: [57fe90ed0070f3525c4709bc612d691b6304252e](https://github.com/useformotor3/ai-discord-bot/commit/57fe90ed0070f3525c4709bc612d691b6304252e)
- 원문 파일: [research_archive/2026-11-12_120532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_120532.md)
- 핵심 주장 주제: 서보 드라이브 제조사가 준수해야 할 '자동화된 보안 업데이트 전달 메커니즘 및 무중단 적용(Secure Update Mechanism & Zero-Downtime Application)' — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 보안 업데이트가 가용 중단 없이 안전하게 전달되고 적용될 수 있는 메커니즘을 제공해야 합니다. 특히 실시간 모션 제어의 특성을 고려하여 업데이트 실패 시 자동 롤백(Rollback) 및 세
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I (Requirements for products with, Part I (Security requirements relating
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #147 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:10:36 (원문 Date; 시간대 미표기)
- 원문 commit: [c30f72653dd4d90a62bb414bf8d64bf2176a298c](https://github.com/useformotor3/ai-discord-bot/commit/c30f72653dd4d90a62bb414bf8d64bf2176a298c)
- 원문 파일: [research_archive/2026-11-12_121036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_121036.md)
- 핵심 주장 주제: '자동화된 취약점 감지 및 안전한 무선(OTA/Network) 업데이트 무결성 검증 메커니즘' — 서보 드라이브 제조사는 CRA에 따라 최종 사용자가 수동 개입하지 않고도 보안 업데이트를 안전하게 수신·적용할 수 있는 자동화된 메커니즘을 제공해야 하며, 업데이트 과정에서 펌웨어의 변조 방지와 롤백(Rollback) 방지 보호 기능을 강제해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I (Requirements for products with, Part I (Security requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #148 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:15:36 (원문 Date; 시간대 미표기)
- 원문 commit: [2102256407ad76322d2d512317f9028afd8a3802](https://github.com/useformotor3/ai-discord-bot/commit/2102256407ad76322d2d512317f9028afd8a3802)
- 원문 파일: [research_archive/2026-11-12_121536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_121536.md)
- 핵심 주장 주제: '디지털 제품에 대한 보안 업데이트의 안전한 전달 및 적용 메커니즘(Secure Update Mechanisms)' — 서보 드라이브 제조사는 CRA에 따라 펌웨어 및 보안 업데이트가 위조되거나 악성 코드에 감염되지 않도록 암호학적으로 검증된 안전한 경로를 통해 무결성이 보장된 상태로 배포 및 적용되도록 기술적 조치를 강구해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Essential Requirements), Part I (Cybersecurity requirements), Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #149 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:20:38 (원문 Date; 시간대 미표기)
- 원문 commit: [48c0b5b19a390aa03ff28c469967c1c284c92763](https://github.com/useformotor3/ai-discord-bot/commit/48c0b5b19a390aa03ff28c469967c1c284c92763)
- 원문 파일: [research_archive/2026-11-12_122038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_122038.md)
- 핵심 주장 주제: '취약점 자동 보고 의무(Reporting of actively exploited vulnerabilities and incidents - Article 14)' — 서보 드라이브 제조사는 제품과 관련하여 실제로 악용된 취약점(Actively exploited vulnerability)이나 보안 인사이더/사고 발생 시, 규정된 법적 기한(조기 경보 24시간 이내) 내에 ENISA 및 관할 CSIRT에 즉각 보고해야 합니다.
- 보고서 기재 조항(미검증): Article 14), Article 14 (Reporting obligations of manu, Article 69(1) for the purposes of the coo, Article 14
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #150 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:25:33 (원문 Date; 시간대 미표기)
- 원문 commit: [6632d1289ef3531c75947170cfe792d11309bac3](https://github.com/useformotor3/ai-discord-bot/commit/6632d1289ef3531c75947170cfe792d11309bac3)
- 원문 파일: [research_archive/2026-11-12_122533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_122533.md)
- 핵심 주장 주제: 서보 드라이브와 같은 IIoT/OT 제품의 '자동화된 보안 이벤트 로깅, 원격 측정(Telemetry) 및 사고 보고(Incident Reporting) 의무' — 서보 드라이브 제조사는 제품 내부에서 발생하는 보안 관련 이벤트와 비정상적인 제어 명령 시도를 실시간으로 로깅하고, 취약점 악용 징후를 탐지할 수 있는 자동화된 원격 측정 기능을 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I, Article 11)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #151 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:30:51 (원문 Date; 시간대 미표기)
- 원문 commit: [481463bd823e21ea05d3b020d701c88664c383c4](https://github.com/useformotor3/ai-discord-bot/commit/481463bd823e21ea05d3b020d701c88664c383c4)
- 원문 파일: [research_archive/2026-11-12_123051.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_123051.md)
- 핵심 주장 주제: '자동 보안 업데이트 및 사용자 고지 메커니즘 (Automatic Security Updates and Notification)' — CRA 규정에 따라, 서보 드라이브 제조사는 보안 취약점이 발견되었을 때 사용자에게 이를 알리고, 중요한 보안 업데이트를 **기본적으로 자동(Automatic)**으로 제공해야 하며, 사용자가 이를 명확히 제어할 수 있는 인터페이스를 보장해야 합니다. 단, 자동 업데이트가 시스템(서보 모터 제어 등)의 
- 보고서 기재 조항(미검증): Article 11, Annex I), Annex I(, Annex I (Requirements for products with, Part I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #152 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:35:35 (원문 Date; 시간대 미표기)
- 원문 commit: [f6ca140215f4eba27e1f69aa55e7e748f0639252](https://github.com/useformotor3/ai-discord-bot/commit/f6ca140215f4eba27e1f69aa55e7e748f0639252)
- 원문 파일: [research_archive/2026-11-12_123535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_123535.md)
- 핵심 주장 주제: '사이버 보안 사고 자동 통보 및 조기경보 의무(Incident Notification Obligations)' — 서보 드라이브 제조사는 제품의 보안에 영향을 미치는 취약점이나 활성 악성 사이버 공격을 인지한 즉시, 지정된 컴퓨터 보안 사고 대응팀(CSIRTs) 및 유럽사이버보안청(ENISA)에 법정 기한 내에 조기 경보 및 사고 통보를 수행해야 합니다. 특히 산업용 자동화 시스템의 중대한 가동 중단을 방지하기 위해 공급망 전반에 걸
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Article 17(1) of Directive (EU) 2022, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #153 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:40:40 (원문 Date; 시간대 미표기)
- 원문 commit: [a330055b304367a6c1cb617e5243ddd3cffefb40](https://github.com/useformotor3/ai-discord-bot/commit/a330055b304367a6c1cb617e5243ddd3cffefb40)
- 원문 파일: [research_archive/2026-11-12_124040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_124040.md)
- 핵심 주장 주제: '보안 취약점 처리 및 조정된 취약점 공개(Coordinated Vulnerability Disclosure, CVD) 프로세스' — 서보 드라이브 제조사는 CRA에 따라 발견된 보안 취약점의 효율적이고 안전한 처리를 위해 규정된 표준 절차를 수립해야 하며, ENISA(유럽사이버보안청) 및 국가별 조정 기관과 연계된 조정된 취약점 공개(CVD) 체계를 운영해야 합니다. 이는 산업 현장의 예기치 않은 모션 제어 중단을 방지하고 공급망 전
- 보고서 기재 조항(미검증): Annex I), Article 11 (General obligations of manufa, Annex I (Requirements for products with, Annex I, Part II - Vulnerability handling requi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #154 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:45:40 (원문 Date; 시간대 미표기)
- 원문 commit: [d52b255e8d961b7fbcba600867fd7de9cdc07f50](https://github.com/useformotor3/ai-discord-bot/commit/d52b255e8d961b7fbcba600867fd7de9cdc07f50)
- 원문 파일: [research_archive/2026-11-12_124540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_124540.md)
- 핵심 주장 주제: '취약점 조율된 공개(Coordinated Vulnerability Disclosure, CVD) 프로세스 수립 및 악용 방지 조치' — 산업용 서보 드라이브 제조사는 제품 내 발견된 취약점의 안전한 신고와 조율된 공개(CVD)를 보장하는 프로세스를 문서화하고, 보안 연구원 및 제3자와의 협력 체계를 갖추어야 합니다. 또한, 취약점 정보가 악용(Exploitation)되기 전 패치 배포가 가능하도록 엄격한 정보 관리 체계를 유지해야 합
- 보고서 기재 조항(미검증): Annex I (Requirements for products with, Article 11 (Obligations of manufacturers, Article 11a or specific sectorial rules., Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #155 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:50:42 (원문 Date; 시간대 미표기)
- 원문 commit: [edd7978457d4d5e5679dc8d3d1c5ed3309dc514c](https://github.com/useformotor3/ai-discord-bot/commit/edd7978457d4d5e5679dc8d3d1c5ed3309dc514c)
- 원문 파일: [research_archive/2026-11-12_125042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_125042.md)
- 핵심 주장 주제: 서보 드라이브 제조사가 준수해야 할 '안전한 기본 설정(Secure by Default) 중에서도 특히 원격 액세스 및 네트워크 인터페이스 제어의 기술적 요구사항과 예외적 상태 관리(Annex I, Part I, Point 2)' — 서보 드라이브는 기본 설정(Secure by default)에 따라 불필요한 네트워크 인터페이스와 원격 액세스 포트가 비활성화된 상태로 출하되어야 하며, 서비스 거부(DoS) 공격을 방지하고 공격 표면을 
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I), Part I), Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #156 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 12:55:31 (원문 Date; 시간대 미표기)
- 원문 commit: [435f80773b7bc1698b34e43fedd86c16c6cbaa22](https://github.com/useformotor3/ai-discord-bot/commit/435f80773b7bc1698b34e43fedd86c16c6cbaa22)
- 원문 파일: [research_archive/2026-11-12_125531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_125531.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 핵심 요건 중 아직 다뤄지지 않은 '자동화된 취약점 보고 및 공공 기관(ENISA/CSIRT) 통보 의무(Vulnerability Reporting Obligations)' — 산업용 서보 드라이브 제조사는 CRA에 따라 자사 제품에서 발견된 적극적으로 악용되는 취약점(Actively exploited vulnerability) 및 심각한 보안 사고(Severe incident)를 법적 기한(
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Article 61(1)... and ENISA, Article 11)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #157 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:00:53 (원문 Date; 시간대 미표기)
- 원문 commit: [d5eb7fe8950ea61a131e1527d99a585dba4617ac](https://github.com/useformotor3/ai-discord-bot/commit/d5eb7fe8950ea61a131e1527d99a585dba4617ac)
- 원문 파일: [research_archive/2026-11-12_130053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_130053.md)
- 핵심 주장 주제: 서보 드라이브와 같은 '중요 디지털 요소(Class II 중요 하드웨어 및 소프트웨어)'에 구체적으로 적용되는 심화 요건 — 서보 드라이브 제조사는 제품을 시장에 출시할 때 지원 종료(End of Support) 시점을 최소 5년 이상으로 명확히 고지해야 하며, 지원 기간 내에 발견된 취약점은 이용자에게 무료로(Without costs) 적시에 패치 형태로 제공할 법적 의무를 진다.
- 보고서 기재 조항(미검증): Annex I), Article 13 (Obligations of manufacturers), Annex I, Part I (Requirements related to the cy, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #158 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:05:36 (원문 Date; 시간대 미표기)
- 원문 commit: [dc7ab2081468d9363d502ff6695ca2c1004e75d2](https://github.com/useformotor3/ai-discord-bot/commit/dc7ab2081468d9363d502ff6695ca2c1004e75d2)
- 원문 파일: [research_archive/2026-11-12_130536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_130536.md)
- 핵심 주장 주제: '취약점 무상 패치 및 공표 의무(Handling of Vulnerabilities and Free Security Updates)' — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 패치 배포 전 제3자나 취약점 데이터베이스에 노출되지 않도록 책임 있는 공개(Coordinated Vulnerability Disclosure) 프로세스를 이행해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Article 14), Annex I(, Article 14(, Annex I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #159 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:10:38 (원문 Date; 시간대 미표기)
- 원문 commit: [272c7fb383fd3eaf5c631e26ef668b9ca7f17e03](https://github.com/useformotor3/ai-discord-bot/commit/272c7fb383fd3eaf5c631e26ef668b9ca7f17e03)
- 원문 파일: [research_archive/2026-11-12_131038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_131038.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive)의 펌웨어 무결성 검증 및 안전한 부팅(Secure Boot) 과정에서의 암호화 키 관리 의무 — 서보 드라이브와 같은 중요 디지털 요소(Important Digital Elements)는 부팅 시점부터 펌웨어의 무결성을 보장하기 위해 암호화된 서명 검증 메커니즘(Secure Boot)을 반드시 구현해야 합니다. 제조사는 하드웨어 기반 신뢰 루트(Root of Trust)를 활용하여 무단 펌웨어 변조
- 보고서 기재 조항(미검증): Annex I(, Annex II, Annex I, Annex II (Technical documentation), Article 31 shall contain all relevant dat
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #160 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:15:40 (원문 Date; 시간대 미표기)
- 원문 commit: [fd4b4ec18063e275917920775f168143ec32be3e](https://github.com/useformotor3/ai-discord-bot/commit/fd4b4ec18063e275917920775f168143ec32be3e)
- 원문 파일: [research_archive/2026-11-12_131540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_131540.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive) 등 중요 디지털 요소(Important Digital Elements)에 적용되는 '취약점 공개 정책(Vulnerability Disclosure Policy, VDP)' 및 '취약점 처리 프로세스(Handling of Vulnerabilities)'에 대한 세부 요건 — 서보 드라이브 제조사는 EU CRA에 따라 취약점의 탐지 및 보고, 무상 보안 업데이트 배포를 포함하는 구조화된 취약점 처리 프
- 보고서 기재 조항(미검증): Annex I (Security requirements), Annex III(Class II, Annex I, Article 11, Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #161 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:20:41 (원문 Date; 시간대 미표기)
- 원문 commit: [4d90114441e8a216283a6f442639a16a67a9d091](https://github.com/useformotor3/ai-discord-bot/commit/4d90114441e8a216283a6f442639a16a67a9d091)
- 원문 파일: [research_archive/2026-11-12_132041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_132041.md)
- 핵심 주장 주제: '취약점 공개 정책(Vulnerability Disclosure Policy) 및 조정된 취약점 공표(Coordinated Vulnerability Disclosure, CVD) 프로세스' — 서보 드라이브 제조사는 EU CRA에 따라 제품 사용자와 보안 연구자가 취약점을 안전하게 신고할 수 있는 명확한 **조정된 취약점 공표(CVD) 및 취약점 처리 프로세스**를 문서화하고 운영해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part II - Vulnerability Handling Requi, Article 11 - Reporting obligations of man, Article 11 (Reporting obligations of manu, Part II (Requirements pertaining to vu
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #162 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:25:36 (원문 Date; 시간대 미표기)
- 원문 commit: [4c108900991179cdf1d95ec6472ba5da9911c217](https://github.com/useformotor3/ai-discord-bot/commit/4c108900991179cdf1d95ec6472ba5da9911c217)
- 원문 파일: [research_archive/2026-11-12_132536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_132536.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive) 제조사가 준수해야 할 핵심 요건 중 아직 다루지 않은 '제품 취급(Handling of vulnerabilities)에 따른 무상 보안 업데이트 제공 및 공개 표준(Open standards) 준수 의무' — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대해 **추가 비용 청구 없이(Free of charge)** 보안 업데이트를 제공해야 하며, 안전한 업데이트 배포를 위한 **자동화된 메
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I(, Annex I (Requirements with regard to th, Part I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #163 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:30:43 (원문 Date; 시간대 미표기)
- 원문 commit: [b2423e6962b846f88303d6e4e29d0de7c4aaa52a](https://github.com/useformotor3/ai-discord-bot/commit/b2423e6962b846f88303d6e4e29d0de7c4aaa52a)
- 원문 파일: [research_archive/2026-11-12_133043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_133043.md)
- 핵심 주장 주제: 실시간 임베디드 펌웨어 환경(Real-time Embedded Firmware) — 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점에 대해 **사용자에게 추가 비용 청구 없이(무상으로) 보안 업데이트 및 패치를 제공**해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Part I (Requirements related to the cy, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #164 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:35:34 (원문 Date; 시간대 미표기)
- 원문 commit: [f1be1ec16746cbc0cda25fb7678c8af99f13b4c8](https://github.com/useformotor3/ai-discord-bot/commit/f1be1ec16746cbc0cda25fb7678c8af99f13b4c8)
- 원문 파일: [research_archive/2026-11-12_133534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_133534.md)
- 핵심 주장 주제: '취약점의 무상 및 시기적절한 보안 업데이트 제공 의무(Handling of Vulnerabilities and Free Security Updates)' — 서보 드라이브 제조사는 제품의 예상 수명 동안 발견되는 취약점에 대해 **추가 비용(무상) 없이 보안 업데이트(Security Updates)를 제공**해야 하며, 이를 체계적으로 관리할 수 있는 프로세스를 구축해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #165 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:40:43 (원문 Date; 시간대 미표기)
- 원문 commit: [1e18c4d567bb6f1cc5e194d56b238de54befe9e9](https://github.com/useformotor3/ai-discord-bot/commit/1e18c4d567bb6f1cc5e194d56b238de54befe9e9)
- 원문 파일: [research_archive/2026-11-12_134043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_134043.md)
- 핵심 주장 주제: ‘취약점 무상 패치 및 보안 업데이트 배포의 기술적 무결성(Vulnerability handling and security updates without undue delay)’ — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 지연 없이 무상으로 제공해야 하며, 실시간 모션 제어 환경의 가동 중단(Downtime)을 방지하기 위해 업데이트 배포 시 디지털 서명 등을 통한 무결성과 가역성(Rollback)을 
- 보고서 기재 조항(미검증): Annex I (Requirement 2 - Vulnerability, Article 13, Annex II (Technical Documentation), Annex I (Requirements relating to produ, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #166 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:45:39 (원문 Date; 시간대 미표기)
- 원문 commit: [b2e7514d4e55434d6c65e3484324a1a14e12cc9f](https://github.com/useformotor3/ai-discord-bot/commit/b2e7514d4e55434d6c65e3484324a1a14e12cc9f)
- 원문 파일: [research_archive/2026-11-12_134539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_134539.md)
- 핵심 주장 주제: "취약점의 무상 및 시차 없는 제공(Free of charge and without delay vulnerability correction), 보안 업데이트 배포의 기술적 무결성 검증, 그리고 서보 펌웨어/부트로더의 안전한 업데이트 메커니즘" — 서보 드라이브 제조사는 CRA에 따라 발견된 취약점에 대한 보안 업데이트를 **추가 비용 없이(free of charge) 지체 없이(without delay)** 제공해야 하며, 실시간 모터
- 보고서 기재 조항(미검증): Annex I, Part I, Part II, Annex I (Requirements for products with, Part I (Security requirements relating
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #167 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:50:43 (원문 Date; 시간대 미표기)
- 원문 commit: [c87a1cab7bd50c7fe20169af3ad8830feb3aa709](https://github.com/useformotor3/ai-discord-bot/commit/c87a1cab7bd50c7fe20169af3ad8830feb3aa709)
- 원문 파일: [research_archive/2026-11-12_135043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_135043.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive)의 실시간 통신 스택(예: EtherCAT, Profinet 등) 및 펌웨어 업데이트 시 무중단/안전성 보장(Secure Update & Rollback) — 서보 드라이브의 펌웨어 업데이트 시, 실시간 제어 루프의 안전성(Safe Torque Off 등)을 해치지 않도록 검증된 암호학적 서명이 포함된 안전한 업데이트 메커니즘을 구현해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part I - Security Requirements), Annex I (Requirements for products with, Part I (Cybersecurity requirements), Part I)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #168 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 13:55:31 (원문 Date; 시간대 미표기)
- 원문 commit: [43fcd55b1f52941087c16723dd32ba539a4ab858](https://github.com/useformotor3/ai-discord-bot/commit/43fcd55b1f52941087c16723dd32ba539a4ab858)
- 원문 파일: [research_archive/2026-11-12_135531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_135531.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 런타임 보안 및 무결성 검증(Secure Boot 및 Hardware Root of Trust) — 산업용 서보 드라이브는 부팅 시점부터 펌웨어의 암호학적 무결성을 검증하는 **Secure Boot(보안 부팅)**와 하드웨어 기반의 신뢰점(Root of Trust)을 강제하여, 악성 펌웨어 주입 및 물리적/원격 조작을 원천 차단해야 합니다. 이는 CRA Annex I의 필수 사이버 보안 요
- 보고서 기재 조항(미검증): Annex I, Part I (Security requirements - Genera, Annex I (Cybersecurity requirements), Part I (Requirements related to the pr, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #169 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:00:52 (원문 Date; 시간대 미표기)
- 원문 commit: [fd3604e713682e669b9e384e6f6931f89c075a23](https://github.com/useformotor3/ai-discord-bot/commit/fd3604e713682e669b9e384e6f6931f89c075a23)
- 원문 파일: [research_archive/2026-11-12_140052.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_140052.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #170 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:05:38 (원문 Date; 시간대 미표기)
- 원문 commit: [2ae39bb60721b042a01a5720d66c93db6f82882d](https://github.com/useformotor3/ai-discord-bot/commit/2ae39bb60721b042a01a5720d66c93db6f82882d)
- 원문 파일: [research_archive/2026-11-12_140538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_140538.md)
- 핵심 주장 주제: "하드웨어 및 펌웨어 수준의 안전한 기본 설정(Secure by default), 취약점 자동 통지 프로세스, 그리고 보안 업데이트의 무상 제공 의무" — 산업용 서보 드라이브는 초기 출고 시 악의적인 접근을 방지하는 **안전한 기본 설정(Secure by default)** 상태여야 하며, 취약점 발견 시 사용자 인터페이스를 통해 **자동으로 보안 업데이트(자동 패치/알림)를 제공**하고, 규정된 지원 기간 동안 이를 **무상으로 제
- 보고서 기재 조항(미검증): Annex I(, Article 11(, Annex I, Article 11, Article 11 (Obligations of manufacturers)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #171 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:10:41 (원문 Date; 시간대 미표기)
- 원문 commit: [691589d529182e807e707e812876826bd13220c1](https://github.com/useformotor3/ai-discord-bot/commit/691589d529182e807e707e812876826bd13220c1)
- 원문 파일: [research_archive/2026-11-12_141041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_141041.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive)의 펌웨어/소프트웨어 업데이트 무결성 보장 및 자동화된 보안 업데이트 전달 메커니즘(Secure Update Mechanism) — 산업용 서보 드라이브는 실시간 제어의 특성상 펌웨어 업데이트 시 시스템 중단이나 악성 코드 주입 위험이 큽니다. EU CRA는 제품의 생명주기 동안 보안 업데이트가 무결성을 유지하며 안전하게 배포되고 적용될 수 있는 기술적 메커니즘을 강제합니다.
- 보고서 기재 조항(미검증): Annex I(Essential Requirements), Part I(Requirements on cybersecurity o, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #172 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:15:40 (원문 Date; 시간대 미표기)
- 원문 commit: [5b41ec3cb9da2bbd6735595779158657a25114ee](https://github.com/useformotor3/ai-discord-bot/commit/5b41ec3cb9da2bbd6735595779158657a25114ee)
- 원문 파일: [research_archive/2026-11-12_141540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_141540.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive)의 펌웨어 무결성 검증 및 하드웨어 기반 루트 오브 트러스트(Root of Trust)를 포함한 '안전한 부팅(Secure Boot) 및 런타임 무결성' — 산업용 서보 드라이브는 CRA Annex I에 따라 악의적인 펌웨어 변조를 방지하고 부팅 시점부터 런타임까지 시스템 무결성을 보장하기 위해, 하드웨어 기반의 '안전한 부팅(Secure Boot)'과 암호학적 검증 메커니즘을 필수적으로 구현해야 합
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I (Requirements for products with, Part I (Security requirements relating
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #173 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:20:42 (원문 Date; 시간대 미표기)
- 원문 commit: [b2410d9082f239cb3ee9fd6aa518bfd74b0cf441](https://github.com/useformotor3/ai-discord-bot/commit/b2410d9082f239cb3ee9fd6aa518bfd74b0cf441)
- 원문 파일: [research_archive/2026-11-12_142042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_142042.md)
- 핵심 주장 주제: '취약점 자동 및 무상 패치 제공 의무와 안전한 기본 설정(Secure by Default)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 보안 취약점에 대한 **무상 보안 업데이트(Security Updates)를 지체 없이 제공**해야 하며, 출고 시 무단 접근을 방지하는 **안전한 기본 설정(Secure by Default)**을 강제해야 합니다. 특히 이는 실시간 모
- 보고서 기재 조항(미검증): Annex I, Part I, Article 14), Annex I (Requirements for products with, Part I (Requirements relating to the c
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #174 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:25:37 (원문 Date; 시간대 미표기)
- 원문 commit: [449f86b0571b7b20126d770b969c4760e339e17e](https://github.com/useformotor3/ai-discord-bot/commit/449f86b0571b7b20126d770b969c4760e339e17e)
- 원문 파일: [research_archive/2026-11-12_142537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_142537.md)
- 핵심 주장 주제: 서보 드라이브(Servo Drive)에 필수적인 '안전 관련 통신 프로토콜(예: EtherCAT FSoE 등)을 포함한 네트워크 인터페이스의 취약점 및 무단 액세스 방지(Secure by default 설정 및 취약점 공개 수신 체계)' — 산업용 서보 드라이브의 네트워크 인터페이스(실시간 제어 버스 및 엔지니어링 포트)는 'Secure by default' 원칙에 따라 기본적으로 무단 접근이 차단되어야 하며, 규정된 제어 경로 외의 
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements for products with, Part I (Cybersecurity requirements), Article 13 (Obligations of manufacturers), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #175 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:30:48 (원문 Date; 시간대 미표기)
- 원문 commit: [c52ebd75766815dca131c5463eee74ea09721305](https://github.com/useformotor3/ai-discord-bot/commit/c52ebd75766815dca131c5463eee74ea09721305)
- 원문 파일: [research_archive/2026-11-12_143048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_143048.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #176 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:35:38 (원문 Date; 시간대 미표기)
- 원문 commit: [74ad3b06bfb0e85a64753263495d5728c1800148](https://github.com/useformotor3/ai-discord-bot/commit/74ad3b06bfb0e85a64753263495d5728c1800148)
- 원문 파일: [research_archive/2026-11-12_143538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_143538.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 보안 업데이트 전달 메커니즘(Vulnerability Handling & Security Updates Delivery)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안 발견되는 취약점에 대해 **무상으로 보안 업데이트(패치)**를 제공해야 하며, 사용자가 이를 안전하게 자동 또는 수동으로 검증·적용할 수 있는 무결성 기반의 업데이트 메커니즘을 구현해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Essential Requirements) Part I, Part II, Article 11 (Obligations of manufacturers, Annex I (Security requirements
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #177 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:40:46 (원문 Date; 시간대 미표기)
- 원문 commit: [60e0ecfb9e88baad09d20227d3a2c7654ec307e2](https://github.com/useformotor3/ai-discord-bot/commit/60e0ecfb9e88baad09d20227d3a2c7654ec307e2)
- 원문 파일: [research_archive/2026-11-12_144046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_144046.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 보안 업데이트 전달 메커니즘(Vulnerability Handling & Security Updates)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 동안 발견되는 취약점에 대해 **추가 비용 청구 없이(Free of charge)** 보안 업데이트를 제공해야 하며, 이를 안전하게 전달하고 자동화할 수 있는 기술적 메커니즘을 구현해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements), Part I (Requirements related to the cy, Article 13 (Obligations of manufacturers), Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #178 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:45:42 (원문 Date; 시간대 미표기)
- 원문 commit: [ecc46264a9b9097700a6ecbf247b262526743f23](https://github.com/useformotor3/ai-discord-bot/commit/ecc46264a9b9097700a6ecbf247b262526743f23)
- 원문 파일: [research_archive/2026-11-12_144542.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_144542.md)
- 핵심 주장 주제: 서보 드라이브와 같은 중요 디지털 요소(Important Digital Products, Class II)가 현장에 배치되기 전 반드시 충족해야 하는 '공장 출하 시 보안 기본 설정(Secure by Default)' 및 '안전한 초기 인증(Initial Authentication) 메커니즘' — 서보 드라이브 제조사는 CRA Annex I에 따라, 제품 출하 시 무단 접근을 방지하기 위한 **강제적인 초기 보안 설정(Secure by
- 보고서 기재 조항(미검증): Annex I, Annex I(Cybersecurity requirements), Annex I (Cybersecurity requirements), Part I (Requirements for products with, Part I)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #179 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:50:38 (원문 Date; 시간대 미표기)
- 원문 commit: [cc467193d7cf60d0a93b2237c87e015983b99882](https://github.com/useformotor3/ai-discord-bot/commit/cc467193d7cf60d0a93b2237c87e015983b99882)
- 원문 파일: [research_archive/2026-11-12_145038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_145038.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #180 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 14:55:33 (원문 Date; 시간대 미표기)
- 원문 commit: [e5e75c58d2e6a1b546b015262aa71829355881b1](https://github.com/useformotor3/ai-discord-bot/commit/e5e75c58d2e6a1b546b015262aa71829355881b1)
- 원문 파일: [research_archive/2026-11-12_145533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_145533.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #181 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:00:59 (원문 Date; 시간대 미표기)
- 원문 commit: [66dfdbcc1ee33c6ec11aec5baea83a0857d31851](https://github.com/useformotor3/ai-discord-bot/commit/66dfdbcc1ee33c6ec11aec5baea83a0857d31851)
- 원문 파일: [research_archive/2026-11-12_150059.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_150059.md)
- 핵심 주장 주제: "취약점 무상 패치 및 보안 업데이트 배포의 기술적 보장(Vulnerability Handling & Free-of-charge Security Updates)" — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견되는 모든 취약점에 대한 보안 업데이트를 추가 비용 없이(Free-of-charge) 제공해야 하며, 이를 자동화된 메커니즘을 통해 안전하게 배포할 수 있는 기술적 수단을 강구해야 합
- 보고서 기재 조항(미검증): Annex I), Article 13 (Obligations of manufacturers), Annex I, Article 13, Part II
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #182 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:05:35 (원문 Date; 시간대 미표기)
- 원문 commit: [e72a3add6952251a99f94b21cbab54eb0a93c8ec](https://github.com/useformotor3/ai-discord-bot/commit/e72a3add6952251a99f94b21cbab54eb0a93c8ec)
- 원문 파일: [research_archive/2026-11-12_150535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_150535.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #183 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:10:41 (원문 Date; 시간대 미표기)
- 원문 commit: [732ee17ae696b0691f69408934cb76a45f767b5a](https://github.com/useformotor3/ai-discord-bot/commit/732ee17ae696b0691f69408934cb76a45f767b5a)
- 원문 파일: [research_archive/2026-11-12_151041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_151041.md)
- 핵심 주장 주제: '안전 관련 실시간 펌웨어 업데이트 시 취약점 무상 패치 의무 및 롤백 방지(Anti-rollback) 메커니즘' — 서보 드라이브 제조사는 CRA에 따라 제품의 지원 기간 동안 발견된 취약점에 대해 사용자에게 **무상으로 보안 업데이트(Security Updates)를 제공**해야 하며, 악성 펌웨어 다운그레이드를 방지하는 **안전한 부트 로더 및 롤백 방지 메커니즘(Anti-rollback protection)**을 구현하여 실시간
- 보고서 기재 조항(미검증): Annex I, Part I, Annex I (Requirements for products with, Part I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #184 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:15:36 (원문 Date; 시간대 미표기)
- 원문 commit: [ab2b04204ca53860f13b7f49bc450111cee2d8f5](https://github.com/useformotor3/ai-discord-bot/commit/ab2b04204ca53860f13b7f49bc450111cee2d8f5)
- 원문 파일: [research_archive/2026-11-12_151536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_151536.md)
- 핵심 주장 주제: '취약점 무상 패치 및 보안 업데이트 배포의 기술적·운영적 의무(Vulnerability Handling & Free-of-Charge Updates)' — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 모든 보안 취약점에 대해 **추가 비용 청구 없이(Free of charge)** 보안 업데이트 및 패치를 즉시 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex III(Class II, Annex I, Part I(Cybersecurity requirements), Article 11 (Obligations of manufacturers)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #185 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:20:45 (원문 Date; 시간대 미표기)
- 원문 commit: [8ae21f12f75e12be2c44db59ee35d1a025fdb12e](https://github.com/useformotor3/ai-discord-bot/commit/8ae21f12f75e12be2c44db59ee35d1a025fdb12e)
- 원문 파일: [research_archive/2026-11-12_152045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_152045.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #186 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:25:40 (원문 Date; 시간대 미표기)
- 원문 commit: [e8508dce5d2d88be41a7b359c0a815dee0a024f8](https://github.com/useformotor3/ai-discord-bot/commit/e8508dce5d2d88be41a7b359c0a815dee0a024f8)
- 원문 파일: [research_archive/2026-11-12_152540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_152540.md)
- 핵심 주장 주제: '취약점 무상 패치 의무 및 보안 업데이트 전달 메커니즘(Vulnerability Handling and Free-of-Charge Updates)' — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 이를 안전하게 배포하고 최종 사용자에게 자동 통지할 수 있는 무결한 업데이트 메커니즘을 기술 문서에 명시하고 구현해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Annex VII, Article 13 (Obligations of manufacturers), Annex I (Requirements relating to the c, Annex VII (Technical documentation)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #187 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:30:47 (원문 Date; 시간대 미표기)
- 원문 commit: [496c3bc6414fb2f0739ff5bfd87fdd42f3d7c638](https://github.com/useformotor3/ai-discord-bot/commit/496c3bc6414fb2f0739ff5bfd87fdd42f3d7c638)
- 원문 파일: [research_archive/2026-11-12_153047.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_153047.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #188 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:35:34 (원문 Date; 시간대 미표기)
- 원문 commit: [44bfcfc96e95a3736fbffe599bb10a50e0f2bd4e](https://github.com/useformotor3/ai-discord-bot/commit/44bfcfc96e95a3736fbffe599bb10a50e0f2bd4e)
- 원문 파일: [research_archive/2026-11-12_153534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_153534.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #189 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:40:46 (원문 Date; 시간대 미표기)
- 원문 commit: [93dafa5f80a2b84548be9d6fad1ad8a07d712fa8](https://github.com/useformotor3/ai-discord-bot/commit/93dafa5f80a2b84548be9d6fad1ad8a07d712fa8)
- 원문 파일: [research_archive/2026-11-12_154046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_154046.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #190 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:45:39 (원문 Date; 시간대 미표기)
- 원문 commit: [d2b0ea6f5dfbcf71e52bd48f2f48a1c5fd9d9bce](https://github.com/useformotor3/ai-discord-bot/commit/d2b0ea6f5dfbcf71e52bd48f2f48a1c5fd9d9bce)
- 원문 파일: [research_archive/2026-11-12_154539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_154539.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #191 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:50:42 (원문 Date; 시간대 미표기)
- 원문 commit: [e9a3166d954a2949930bd56fe83022aeb797ac87](https://github.com/useformotor3/ai-discord-bot/commit/e9a3166d954a2949930bd56fe83022aeb797ac87)
- 원문 파일: [research_archive/2026-11-12_155042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_155042.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #192 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 15:55:39 (원문 Date; 시간대 미표기)
- 원문 commit: [1b48064ca9fd83ee90f8937dc6fd04d4176e3917](https://github.com/useformotor3/ai-discord-bot/commit/1b48064ca9fd83ee90f8937dc6fd04d4176e3917)
- 원문 파일: [research_archive/2026-11-12_155539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_155539.md)
- 핵심 주장 주제: '소프트웨어 부품 명세서(SBOM, Software Bill of Materials) 작성 및 기계 판독 가능 형식 제공 의무' — EU CRA는 디지털 요소를 포함하는 모든 제품(서보 드라이브 포함)의 제조사에게 구성 요소를 식별할 수 있는 SBOM(소프트웨어 부품 명세서)을 기계 판독 가능한 형식으로 작성하고 유지할 것을 의무화합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I, Article 13 (Obligations of manufacturers), Part I, Annex IIa
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)의 top-level dependencies와 Annex II point 9의 사용자 접근정보 조건부 규칙, Article 31/Annex VII 기술문서 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #193 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:00:55 (원문 Date; 시간대 미표기)
- 원문 commit: [f6570c946021fc75ff454e29d715a202ce6671d9](https://github.com/useformotor3/ai-discord-bot/commit/f6570c946021fc75ff454e29d715a202ce6671d9)
- 원문 파일: [research_archive/2026-11-12_160055.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_160055.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #194 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:05:45 (원문 Date; 시간대 미표기)
- 원문 commit: [ea52f92fb236b748bbcd3b74cc69f1fd29c5db9a](https://github.com/useformotor3/ai-discord-bot/commit/ea52f92fb236b748bbcd3b74cc69f1fd29c5db9a)
- 원문 파일: [research_archive/2026-11-12_160545.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_160545.md)
- 핵심 주장 주제: '취약점 무상 처리 및 보안 업데이트(Vulnerability Handling and Security Updates)' — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대해 무상으로 보안 패치(Security Updates)를 제공하고, 취약점 공개 및 처리 프로세스를 투명하게 운영해야 합니다. 특히, 업데이트가 제품의 안전 관련(Safety-related) 기능에 미치는 영향을 최소화하면서 적시에 배포할 수 
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #195 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:10:45 (원문 Date; 시간대 미표기)
- 원문 commit: [e96430c8f4a958339475e3b37994e9a70e9f71c3](https://github.com/useformotor3/ai-discord-bot/commit/e96430c8f4a958339475e3b37994e9a70e9f71c3)
- 원문 파일: [research_archive/2026-11-12_161045.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_161045.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #196 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:15:50 (원문 Date; 시간대 미표기)
- 원문 commit: [7b80dbdcbff47d230be89edb9f9902f52b3b4970](https://github.com/useformotor3/ai-discord-bot/commit/7b80dbdcbff47d230be89edb9f9902f52b3b4970)
- 원문 파일: [research_archive/2026-11-12_161550.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_161550.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #197 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:20:50 (원문 Date; 시간대 미표기)
- 원문 commit: [8637dbd0f8b45a43552f2349a2eda3810a45ab93](https://github.com/useformotor3/ai-discord-bot/commit/8637dbd0f8b45a43552f2349a2eda3810a45ab93)
- 원문 파일: [research_archive/2026-11-12_162050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_162050.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #198 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:25:40 (원문 Date; 시간대 미표기)
- 원문 commit: [205d9f1f43037a39c94131448d98a5021ce125ef](https://github.com/useformotor3/ai-discord-bot/commit/205d9f1f43037a39c94131448d98a5021ce125ef)
- 원문 파일: [research_archive/2026-11-12_162540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_162540.md)
- 핵심 주장 주제: 'Secure by Default (기본 보안 설정)' 및 '초기 가용 상태에서의 위험 최소화' — 서보 드라이브 제조사는 제품 출시 시점에 악성 공격의 표적이 될 수 있는 불필요한 기능과 기본 포트를 원천 차단하고, 안전한 초기 상태(Secure by default)로 공장 출하해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements) Part I, ANNEX I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #199 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:30:46 (원문 Date; 시간대 미표기)
- 원문 commit: [67480049110be16eef20f717748681b820325876](https://github.com/useformotor3/ai-discord-bot/commit/67480049110be16eef20f717748681b820325876)
- 원문 파일: [research_archive/2026-11-12_163046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_163046.md)
- 핵심 주장 주제: '취약점 처리 및 조치 공개 (Vulnerability Handling and Public Disclosure)' — 산업용 서보 드라이브 제조사는 CRA에 따라 발견된 취약점을 효율적으로 처리하기 위한 정책을 수립하고, 패치 가용성 및 취약점 정보에 대한 보안 권고문(Security Advisory)을 대중과 관련 기관에 투명하게 공개해야 합니다. 특히 취약점 정보는 EU 기관(ENISA) 및 신뢰할 수 있는 플랫폼에 적시에 보고되어
- 보고서 기재 조항(미검증): Annex I, Article 11 (Obligations of manufacturers), Annex I (Requirements relating to the c, Part II, Part II - Vulnerability handling requi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #200 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:35:39 (원문 Date; 시간대 미표기)
- 원문 commit: [12701bda702a5bfddb5f752c8e28c94a2859243b](https://github.com/useformotor3/ai-discord-bot/commit/12701bda702a5bfddb5f752c8e28c94a2859243b)
- 원문 파일: [research_archive/2026-11-12_163539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_163539.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #201 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:40:40 (원문 Date; 시간대 미표기)
- 원문 commit: [9c212fbca8c0e7186645ead850bb681965510df8](https://github.com/useformotor3/ai-discord-bot/commit/9c212fbca8c0e7186645ead850bb681965510df8)
- 원문 파일: [research_archive/2026-11-12_164040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_164040.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #202 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:45:39 (원문 Date; 시간대 미표기)
- 원문 commit: [ba23457ea3aacebe383c95bd01b6db2633f0178f](https://github.com/useformotor3/ai-discord-bot/commit/ba23457ea3aacebe383c95bd01b6db2633f0178f)
- 원문 파일: [research_archive/2026-11-12_164539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_164539.md)
- 핵심 주장 주제: '취약점 수명주기 관리 및 사고 보고 의무(Vulnerability Handling and Incident Reporting)' — CRA에 따라 산업용 서보 드라이브 제조사는 제품 수명주기 동안 발견된 보안 취약점을 체계적으로 관리해야 하며, 특히 **활성(Actively exploited) 취약점 및 심각한 보안 사고(Incident)를 24시간(Early warning) 및 72시간(Notification) 이내에 관할 기관(CS
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Annex I (Requirements relating to the c, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #203 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:50:40 (원문 Date; 시간대 미표기)
- 원문 commit: [28a837196c5f825939c18b35379866b11ae1bcfc](https://github.com/useformotor3/ai-discord-bot/commit/28a837196c5f825939c18b35379866b11ae1bcfc)
- 원문 파일: [research_archive/2026-11-12_165040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_165040.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #204 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 16:55:37 (원문 Date; 시간대 미표기)
- 원문 commit: [4561aff741c1a624434d27f6e970c42bfbbce87c](https://github.com/useformotor3/ai-discord-bot/commit/4561aff741c1a624434d27f6e970c42bfbbce87c)
- 원문 파일: [research_archive/2026-11-12_165537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_165537.md)
- 핵심 주장 주제: '보안 업데이트 및 취약점 공개 정책(Coordinated Vulnerability Disclosure, CVD) 관리'
- 보고서 기재 조항(미검증): Annex I (Security Requirements), Article 11 (Obligations of manufacturers), Annex I, Article 11, Article 11 (Manufacturer obligations)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #205 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:01:01 (원문 Date; 시간대 미표기)
- 원문 commit: [3c4a638ce78c265a597ca273f0267abe5fdbaad8](https://github.com/useformotor3/ai-discord-bot/commit/3c4a638ce78c265a597ca273f0267abe5fdbaad8)
- 원문 파일: [research_archive/2026-11-12_170101.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_170101.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #206 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:05:33 (원문 Date; 시간대 미표기)
- 원문 commit: [79bb116d286420460a2d8b6fe405d480bdabbc30](https://github.com/useformotor3/ai-discord-bot/commit/79bb116d286420460a2d8b6fe405d480bdabbc30)
- 원문 파일: [research_archive/2026-11-12_170533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_170533.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #207 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:10:41 (원문 Date; 시간대 미표기)
- 원문 commit: [73b8d26d0384997cc28b30a3d7e1abab9e71be60](https://github.com/useformotor3/ai-discord-bot/commit/73b8d26d0384997cc28b30a3d7e1abab9e71be60)
- 원문 파일: [research_archive/2026-11-12_171041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_171041.md)
- 핵심 주장 주제: 안전 관련 하드웨어/소프트웨어 통합 및 원격 원격측정(Telemetry)·취약점 자동 차단 기능 — 산업용 서보 드라이브는 기계류(Machinery Regulation)와 결합되는 중요 디지털 요소이므로, CRA Annex I에 따라 **인증되지 않은 외부 접근을 방지하는 보안 인터페이스(Secure Interfaces) 설계**와 **보안에 영향을 미치는 악성 코드 유입을 막는 무결성 보호(Integrity Protection)** 
- 보고서 기재 조항(미검증): Annex I, Annex I (Essential Requirements), Part I (Requirements for cybersecurity, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #208 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:15:41 (원문 Date; 시간대 미표기)
- 원문 commit: [f3bc63bd9ca55465e8c7896b35ea2126e0912692](https://github.com/useformotor3/ai-discord-bot/commit/f3bc63bd9ca55465e8c7896b35ea2126e0912692)
- 원문 파일: [research_archive/2026-11-12_171541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_171541.md)
- 핵심 주장 주제: '소프트웨어 부품명세서(SBOM)의 머신 리더블(Machine-readable) 포맷 제공 의무 및 자동화된 취약점 연계 요건' — 산업용 서보 드라이브 제조사는 CRA Annex I에 따라 디지털 제품에 포함된 오픈소스 및 제3자 소프트웨어 구성 요소를 기계 판독 가능한(Machine-readable) 표준 형식의 SBOM으로 작성하여 제공해야 하며, 이를 자동화된 도구와 연계하여 실시간 취약점프레임워크에 대응할 수 있도록 생명주기를
- 보고서 기재 조항(미검증): Annex I, Annex I (Requirements for products with, Article 13 (Obligations of manufacturers), Article 13(2), Article 31 and ensure that the product wi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part II(1)의 top-level dependencies와 Annex II point 9의 사용자 접근정보 조건부 규칙, Article 31/Annex VII 기술문서 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #209 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:20:39 (원문 Date; 시간대 미표기)
- 원문 commit: [c42ddd07ec221e08761b86d018b3132cc59161a2](https://github.com/useformotor3/ai-discord-bot/commit/c42ddd07ec221e08761b86d018b3132cc59161a2)
- 원문 파일: [research_archive/2026-11-12_172039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_172039.md)
- 핵심 주장 주제: '중요 디지털 요소(Class II)에 대한 제3자 적합성 평가(Third-party Conformity Assessment) 및 사이버 보안 관리 시스템(CSMS)' — 산업용 서보 드라이브는 EU CRA 부속서 III(Class II)에 해당하는 중요 디지털 제품으로 분류될 수 있어, 내부 자체 평가(Module A)가 아닌 유럽 공인 기관(Notified Body)을 통한 제3자 적합성 평가가 강제됩니다.
- 보고서 기재 조항(미검증): Article 24 (Conformity assessment procedu, Annex III, Annex VII (Important products with digi, Article 24 (1), Annex VII (Module B)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #210 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:25:36 (원문 Date; 시간대 미표기)
- 원문 commit: [11c27722c1ffc90f1f575cc41c353cacc2a805da](https://github.com/useformotor3/ai-discord-bot/commit/11c27722c1ffc90f1f575cc41c353cacc2a805da)
- 원문 파일: [research_archive/2026-11-12_172536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_172536.md)
- 핵심 주장 주제: "디지털 요소가 포함된 제품의 지원 기간(Support Period) 및 취약점 처리 의무(Annex I, Part II - Vulnerability Handling Requirements)" — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 또는 최소 **5년** 중 더 긴 기간 동안 발견된 취약점에 대해 무상으로 보안 패치(Security Updates)를 배포해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part II - Vulnerability Handling Requi, Article 14, Annex I), Article 14 (Obligations of manufacturers)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #211 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:30:48 (원문 Date; 시간대 미표기)
- 원문 commit: [550d688ffaa9a27d6eee9ad7a1e06204cb787cf6](https://github.com/useformotor3/ai-discord-bot/commit/550d688ffaa9a27d6eee9ad7a1e06204cb787cf6)
- 원문 파일: [research_archive/2026-11-12_173048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_173048.md)
- 핵심 주장 주제: "중요 디지털 요소 제품(Class I/II)에 대한 제3자 적합성 평가 및 공인 기관(Notified Body)을 통한 강제 인증 절차"
- 보고서 기재 조항(미검증): Annex III), Annex III, Annex III shall follow, Article 24
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #212 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:35:37 (원문 Date; 시간대 미표기)
- 원문 commit: [52fb0e8866dc6771986bfa0abfcfce177c6655dc](https://github.com/useformotor3/ai-discord-bot/commit/52fb0e8866dc6771986bfa0abfcfce177c6655dc)
- 원문 파일: [research_archive/2026-11-12_173537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_173537.md)
- 핵심 주장 주제: "취약점 공개 정책 및 무상 보안 업데이트(Vulnerability Disclosure and Free Security Updates)" — 산업용 서보 드라이브 제조사는 EU CRA에 따라 취약점 무상 처리 체계를 수립하고, 발견된 취약점 및 보안 업데이트를 사용자에게 비용 청구 없이 적시에 배포해야 합니다. 이는 OT(운영 기술) 환경의 고질적인 패치 지연 문제를 해결하기 위한 법적 강제 사항입니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I, Article 11 (Obligations of manufacturers), Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #213 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:40:43 (원문 Date; 시간대 미표기)
- 원문 commit: [7893abe6678f7a6945dd505ff4d6fb51692dd8b0](https://github.com/useformotor3/ai-discord-bot/commit/7893abe6678f7a6945dd505ff4d6fb51692dd8b0)
- 원문 파일: [research_archive/2026-11-12_174043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_174043.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #214 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:45:36 (원문 Date; 시간대 미표기)
- 원문 commit: [4211f57a59a74d68b5373e9cf5aaf117267c78bf](https://github.com/useformotor3/ai-discord-bot/commit/4211f57a59a74d68b5373e9cf5aaf117267c78bf)
- 원문 파일: [research_archive/2026-11-12_174536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_174536.md)
- 핵심 주장 주제: "보안 업데이트의 자동화 및 무중단 배포(Secure Update Mechanism & Automated Delivery)" — **핵심 내용 1:** 산업용 서보 드라이브 제조사는 CRA에 따라 펌웨어 및 보안 업데이트를 안전하고 무결하게 전달할 수 있는 자동화된 메커니즘을 기술 문서에 명시하고 구현해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Part I (Requirements relating to produ, Annex I, Annex I - Requirements relating to prod
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #215 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:50:42 (원문 Date; 시간대 미표기)
- 원문 commit: [b66d1ab16d5706af1494373cf8ad77eda3954230](https://github.com/useformotor3/ai-discord-bot/commit/b66d1ab16d5706af1494373cf8ad77eda3954230)
- 원문 파일: [research_archive/2026-11-12_175042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_175042.md)
- 핵심 주장 주제: "취약점 공개 정책(Vulnerability Disclosure Policy) 및 조정된 취약점 공표(Coordinated Vulnerability Disclosure, CVD)" — 산업용 서보 드라이브 제조사는 보안 취약점의 접수, 평가, 조치 및 공개를 위한 명확한 **취약점 공개 정책(Vulnerability Disclosure Policy)**을 수립하고, EU 엔니사(ENISA) 및 관련 기관에 적시에 보고할 체계를 갖추어야
- 보고서 기재 조항(미검증): Annex I (Essential Requirements - Part, Article 11., Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #216 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 17:55:40 (원문 Date; 시간대 미표기)
- 원문 commit: [3a89a822a2db10e27f302dcff5d4dadc369bc4dc](https://github.com/useformotor3/ai-discord-bot/commit/3a89a822a2db10e27f302dcff5d4dadc369bc4dc)
- 원문 파일: [research_archive/2026-11-12_175540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_175540.md)
- 핵심 주장 주제: "디지털 요소가 포함된 제품의 지원 기간 종료(End of Support) 및 취약점 공개 투명성" — **주제:** 서보 드라이브의 예상 제품 수명(Expected Lifetime) 산정 및 지원 종료 시점의 명확한 고지 의무
- 보고서 기재 조항(미검증): Annex I (Requirements, Article 13 (Obligations of manufacturers), Article 13, Annex I - Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #217 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:00:55 (원문 Date; 시간대 미표기)
- 원문 commit: [a13ca523eb1fa8848c1881006260c1db25f6c276](https://github.com/useformotor3/ai-discord-bot/commit/a13ca523eb1fa8848c1881006260c1db25f6c276)
- 원문 파일: [research_archive/2026-11-12_180055.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_180055.md)
- 핵심 주장 주제: "취약점 공표 및 무상 보안 패치 제공 의무 (Vulnerability Disclosure and Free-of-Charge Security Updates)" — 서보 드라이브 제조사는 제품의 예상 수명(또는 최소 5년) 동안 발견된 취약점에 대해 무상으로 보안 패치(Security Updates)를 제공하고 대중에게 투명하게 공표해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Annex I (Requirements for products with, Article 10 (Obligations of manufacturers)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #218 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:05:34 (원문 Date; 시간대 미표기)
- 원문 commit: [e4ce3564639012c97babda8ae047e10579b944fc](https://github.com/useformotor3/ai-discord-bot/commit/e4ce3564639012c97babda8ae047e10579b944fc)
- 원문 파일: [research_archive/2026-11-12_180534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_180534.md)
- 핵심 주장 주제: 무결성 및 인증 (Secure Update Mechanism)
- 보고서 기재 조항(미검증): Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #219 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:10:42 (원문 Date; 시간대 미표기)
- 원문 commit: [8e06157ed94f55afbe126f96e8e07eb6bef12232](https://github.com/useformotor3/ai-discord-bot/commit/8e06157ed94f55afbe126f96e8e07eb6bef12232)
- 원문 파일: [research_archive/2026-11-12_181042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_181042.md)
- 핵심 주장 주제: '취약점 처리 공시(Vulnerability Disclosure) 및 투명한 보안 수명주기 관리 체계(Coordinated Vulnerability Disclosure)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 사용자 및 보안 연구원이 취약점을 안전하게 신고할 수 있는 창구를 상시 운영해야 하며, 발견된 취약점의 심각도에 따라 법정 기한 내에 조치 및 공시(Coordinated Vulnerability Disclosure
- 보고서 기재 조항(미검증): Annex I, Part II - Vulnerability Handling Requi, Article 14), Annex I (Requirements for products with, Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #220 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:15:47 (원문 Date; 시간대 미표기)
- 원문 commit: [a68e6410a254ebda79d508ead5e41eac14376880](https://github.com/useformotor3/ai-discord-bot/commit/a68e6410a254ebda79d508ead5e41eac14376880)
- 원문 파일: [research_archive/2026-11-12_181547.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_181547.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #221 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:20:39 (원문 Date; 시간대 미표기)
- 원문 commit: [6f1e9322e6bf716c215dd400c4efc27694e793b8](https://github.com/useformotor3/ai-discord-bot/commit/6f1e9322e6bf716c215dd400c4efc27694e793b8)
- 원문 파일: [research_archive/2026-11-12_182039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_182039.md)
- 핵심 주장 주제: '기본 설정(Secure by Default) 및 공격 표면 최소화(Minimization of Attack Surface)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품 출고 시 초기 설정으로 무단 접근을 방지하는 강력한 보안 기본값(Secure by default)을 적용해야 합니다. 특히, 현장 시운전 및 유지보수를 위해 사용되는 물리적·논리적 인터페이스(예: 디버그 포트, 미사용 네트워크 서비스)는 기본적으로 비활성화되
- 보고서 기재 조항(미검증): Annex I (Requirements for products with, Part I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #222 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:25:33 (원문 Date; 시간대 미표기)
- 원문 commit: [f8e51c13cb0d81b47e48e0de7f1456cfe1fb2e10](https://github.com/useformotor3/ai-discord-bot/commit/f8e51c13cb0d81b47e48e0de7f1456cfe1fb2e10)
- 원문 파일: [research_archive/2026-11-12_182533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_182533.md)
- 핵심 주장 주제: 'Secure by Default(기본 설정 보안) 및 초기 설정 무결성 보장' — 산업용 서보 드라이브는 공장 출고 시(Out-of-the-box) 모든 기본 계정의 패스워드가 비활성화되어 있거나 개별적으로 고유하게 설정되어야 하며, 공격 표면을 최소화하기 위해 불필요한 네트워크 인터페이스와 서비스가 기본적으로 차단(Secure by default)된 상태여야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements for products with, Part I (Security requirements relating, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #223 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:30:50 (원문 Date; 시간대 미표기)
- 원문 commit: [fb7af54d7c0e77c84ee7ca015cfff254220aff08](https://github.com/useformotor3/ai-discord-bot/commit/fb7af54d7c0e77c84ee7ca015cfff254220aff08)
- 원문 파일: [research_archive/2026-11-12_183050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_183050.md)
- 핵심 주장 주제: [Annex I, Part I, Paragraph 1 - General cybersecurity requirements]
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I, Annex I (Security requirements-Categori
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 원문 법령 조항·정확한 인용·주변 문맥·예외를 Pass A/B/C로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #224 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:35:34 (원문 Date; 시간대 미표기)
- 원문 commit: [9ab2233bdbc9231410b484fdaa7ec4464d119edd](https://github.com/useformotor3/ai-discord-bot/commit/9ab2233bdbc9231410b484fdaa7ec4464d119edd)
- 원문 파일: [research_archive/2026-11-12_183534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_183534.md)
- 핵심 주장 주제: 취약점 무상 패치 및 지원 기간 (Support Period & Free Updates):
- 보고서 기재 조항(미검증): Annex I(, Annex I (Essential requirements), Article 13 (Obligations of manufacturers), Annex I, Part I - Security requirements
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #225 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:40:38 (원문 Date; 시간대 미표기)
- 원문 commit: [5d002c65629fc7a40e3be909f85b9ad8fcac88c3](https://github.com/useformotor3/ai-discord-bot/commit/5d002c65629fc7a40e3be909f85b9ad8fcac88c3)
- 원문 파일: [research_archive/2026-11-12_184038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_184038.md)
- 핵심 주장 주제: '취약점 처리 프로세스 및 협조 의무(Vulnerability Handling and Reporting Obligations)' — 산업용 서보 드라이브 제조사는 CRA에 따라 자사 제품에서 발견된 취약점과 보안 사고(Incident)를 법적 기한 내에 관련 기관(ENISA 및 국가별 CSIRT)과 사용자에게 의무적으로 신고해야 하며, 외부 보안 연구원 등의 취약점 제보를 원활히 수용할 수 있는 취약점 조정 공개(Coordinated 
- 보고서 기재 조항(미검증): Annex I), Article 11 (Manufacturer, Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #226 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:45:37 (원문 Date; 시간대 미표기)
- 원문 commit: [0a825dd539d6dde281c1d25b5c2acf447c974fc5](https://github.com/useformotor3/ai-discord-bot/commit/0a825dd539d6dde281c1d25b5c2acf447c974fc5)
- 원문 파일: [research_archive/2026-11-12_184537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_184537.md)
- 핵심 주장 주제: '취약점 핸들링 및 조정된 취약점 공개(Coordinated Vulnerability Disclosure, CVD)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 보안 취약점 정보가 제3자에게 악용되기 전 안전하게 신고받고 처리할 수 있도록, 취약점 접수 채널을 공식 운영하고 제조사 간/고객 간 투명한 **조정된 취약점 공개(CVD) 프로세스**를 수립해야 합니다. 또한, 발견된 취약점은 공식 유럽사이버보안기관(ENIS
- 보고서 기재 조항(미검증): Annex I), Article 11 (Obligations of manufacturers), Article 14 (Reporting obligations of manu, Article 11, Article 17 of any vulnerability having an
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #227 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:50:40 (원문 Date; 시간대 미표기)
- 원문 commit: [56638de6c47aec95c95ef09c44f522fc62d151e4](https://github.com/useformotor3/ai-discord-bot/commit/56638de6c47aec95c95ef09c44f522fc62d151e4)
- 원문 파일: [research_archive/2026-11-12_185040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_185040.md)
- 핵심 주장 주제: "디지털 요소가 포함된 제품의 취약점 처리 공정 및 조정된 취약점 공개(Coordinated Vulnerability Disclosure, CVD) 프로세스 구축" — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품 생명주기 동안 발견되는 보안 취약점을 체계적으로 접수·분석·대응하기 위한 내부 취약점 처리 공정을 수립해야 하며, 외부 보안 연구원이나 사용자가 안전하게 취약점을 제보할 수 있도록 조정된 취약점 공개(CVD) 정책을
- 보고서 기재 조항(미검증): Annex I (Requirements relating to the c, Part II (Vulnerability handling requir, Article 11 (Obligations of manufacturers), Article 14 (Reporting obligations), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #228 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 18:55:41 (원문 Date; 시간대 미표기)
- 원문 commit: [fb80d7a4733960cf9cb85f0715a687cd00de6b2c](https://github.com/useformotor3/ai-discord-bot/commit/fb80d7a4733960cf9cb85f0715a687cd00de6b2c)
- 원문 파일: [research_archive/2026-11-12_185541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_185541.md)
- 핵심 주장 주제: '취약점 자동 보고 의무(Vulnerability Reporting Obligation to ENISA/CSIRTs)' — 산업용 서보 드라이브 제조사는 제품(디지털 요소를 가진 제품)에 영향을 미치는 활성 취약점(Actively exploited vulnerability)이나 심각한 보안 사건(Severe incident)을 인지한 즉시, 법적 기한 내에 유럽사이버보안청(ENISA) 및 관할 국가 CSIRT에 의무적으로 신고해야 합니
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #229 — P3
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:01:01 (원문 Date; 시간대 미표기)
- 원문 commit: [ff4fadbd7f3c0dd60d7aa36c95db7d442fbcd0a4](https://github.com/useformotor3/ai-discord-bot/commit/ff4fadbd7f3c0dd60d7aa36c95db7d442fbcd0a4)
- 원문 파일: [research_archive/2026-11-12_190101.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_190101.md)
- 핵심 주장 주제: 모델 호출 실패 경고(실질 CRA 주장 없음)
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: 실질 CRA 주장 없음; 모델 실패가 조사 성공으로 archive/history/state에 기록되는지 운영 경로 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #230 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:05:38 (원문 Date; 시간대 미표기)
- 원문 commit: [4fb7b45a6aa68f85c99256dfbe3784e3ae82325b](https://github.com/useformotor3/ai-discord-bot/commit/4fb7b45a6aa68f85c99256dfbe3784e3ae82325b)
- 원문 파일: [research_archive/2026-11-12_190538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_190538.md)
- 핵심 주장 주제: '취약점 핸들링 및 대중소기업/제품 수명주기 전반의 취약점 보고 의무(Vulnerability Handling & Reporting)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안 식별된 모든 보안 취약점을 체계적으로 처리해야 하며, 특히 **악용된 취약점(Actively exploited vulnerability) 및 심각한 인시던트(Severe incident)를 발견 즉시(지연 없이) 관련 기관(C
- 보고서 기재 조항(미검증): Article 11 (Obligations of manufacturers), Article 14 (Reporting obligations of manu, Article 14 - Reporting obligations, Article 17(1) of Directive (EU) 2022
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #231 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:10:36 (원문 Date; 시간대 미표기)
- 원문 commit: [3d822e3f788d86a0e15ee542741eb6cdf52175f7](https://github.com/useformotor3/ai-discord-bot/commit/3d822e3f788d86a0e15ee542741eb6cdf52175f7)
- 원문 파일: [research_archive/2026-11-12_191036.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_191036.md)
- 핵심 주장 주제: "취약점 핸들링 및 조치 보고 의무 (Vulnerability Handling and Reporting Obligations)" — 산업용 서보 드라이브 제조사는 제품에서 발견된 취약점과 활성 악성코드(Actively exploited vulnerabilities and incidents)를 규정된 기한 내에 ENISA 및 관할 국가 보안 기관에 의무적으로 신고하고, 이를 완화하기 위한 보안 조치(수정 패치 등)를 신속하게 이파(Dep
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Annex I (Requirements for products with, Article 11, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #232 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:15:44 (원문 Date; 시간대 미표기)
- 원문 commit: [6701ca9bfeac45b4850615448eb447e42580c290](https://github.com/useformotor3/ai-discord-bot/commit/6701ca9bfeac45b4850615448eb447e42580c290)
- 원문 파일: [research_archive/2026-11-12_191544.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_191544.md)
- 핵심 주장 주제: '취약점 보고 의무(Vulnerability Reporting Obligations)' — 산업용 서보 드라이브 제조사는 자사 제품에서 발견된 적극적으로 악용되는 취약점(Actively exploited vulnerability) 및 심각한 보안 사건(Severe incident)을 규정된 시한 내에 EU 회원국의 컴퓨터 보안 사고 대응팀(CSIRTs)과 유럽사이버안보청(ENISA)에 의무적으로 신고해야 합니다. 이는 공급망 전반의 신
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Article 17(1) of Directive (EU) 2022, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #233 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:20:43 (원문 Date; 시간대 미표기)
- 원문 commit: [8e50d720f09f554a8e0b1a59bbf53658dfcf730b](https://github.com/useformotor3/ai-discord-bot/commit/8e50d720f09f554a8e0b1a59bbf53658dfcf730b)
- 원문 파일: [research_archive/2026-11-12_192043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_192043.md)
- 핵심 주장 주제: "취약점 신고 의무 및 사고 대응 절차 (Reporting of Vulnerabilities and Incidents)" — 산업용 서보 드라이브 제조사는 제품과 관련된 적극적으로 explotación(악용)된 취약점 및 심각한 보안 인사이던트(Incident)가 발생했을 때, 법적으로 정해진 기한 내에 지정된 기관(CSIRT/ENISA) 및 사용자에게 의무적으로 신고해야 합니다. 이를 위해 탐지부터 보고, 후속 조치까지 아우르는 정형
- 보고서 기재 조항(미검증): Article 14 (Reporting obligations of manu, Article 17 of any vulnerability having an, Article 14
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #234 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:25:46 (원문 Date; 시간대 미표기)
- 원문 commit: [c28d00f3b88ee49d79883913f6dd5c75af910a39](https://github.com/useformotor3/ai-discord-bot/commit/c28d00f3b88ee49d79883913f6dd5c75af910a39)
- 원문 파일: [research_archive/2026-11-12_192546.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_192546.md)
- 핵심 주장 주제: '취약점 자동 통보 의무(Reporting of Actively Exploited Vulnerabilities and Incidents)' — 서보 드라이브 제조사는 제품 내에서 악용되는 취약점(Actively exploited vulnerability) 또는 중대한 보안 사고(Severe incident) 발생 시, 규정에 따라 지정된 기관(CSIRTs / ENISA)에 법적으로 정해진 시한 내에 의무적으로 통보해야 합니다.
- 보고서 기재 조항(미검증): Article 11 - Reporting obligations of man
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #235 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:30:58 (원문 Date; 시간대 미표기)
- 원문 commit: [58e95393b8c6b43dd08a402c1c87f31ba5d2e06b](https://github.com/useformotor3/ai-discord-bot/commit/58e95393b8c6b43dd08a402c1c87f31ba5d2e06b)
- 원문 파일: [research_archive/2026-11-12_193058.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_193058.md)
- 핵심 주장 주제: '취약점 자동 차단 및 접근 제어 메커니즘을 포함한 안전한 통신 인터페이스(Secure Interfaces and Protection against Denial of Service)' — 산업용 서보 드라이브는 외부 네트워크 및 상위 제어기(PLC 등)와 연결되는 통신 인터페이스에서 무단 접근을 방지하고, 서비스 거부(DoS) 공격 등 악의적 트래픽으로부터 실시간 제어 루프의 가용성을 보호할 수 있는 강력한 보안 메커니즘과 암호화된 통
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements relating to the c, Part I (Requirements for products with, Annex I, Part I)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #236 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:35:31 (원문 Date; 시간대 미표기)
- 원문 commit: [f56cc2389e8a0620732a2c7b61f2b4c407c74c25](https://github.com/useformotor3/ai-discord-bot/commit/f56cc2389e8a0620732a2c7b61f2b4c407c74c25)
- 원문 파일: [research_archive/2026-11-12_193531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_193531.md)
- 핵심 주장 주제: "취약점 신고 의무(Vulnerability Reporting Obligations - ENISA를 통한 활성 취약점 및 심각한 인시던트 보고)" — 산업용 서보 드라이브 제조사는 제품에 영향을 미치는 활성 취약점(Actively exploited vulnerability) 및 심각한 보안 인시던트 발생 시, 법적으로 정해진 기한 내에 지정된 컴퓨터 보안 사고 대응팀(CSIRTs) 및 유럽 네트워크정보보안청(ENISA)에 즉각적으로 신
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Article 17(1) of Directive (EU) 2022
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #237 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:40:43 (원문 Date; 시간대 미표기)
- 원문 commit: [87bba1fe21e6eef45c3213458ec598c781a683ae](https://github.com/useformotor3/ai-discord-bot/commit/87bba1fe21e6eef45c3213458ec598c781a683ae)
- 원문 파일: [research_archive/2026-11-12_194043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_194043.md)
- 핵심 주장 주제: '취약점 처리 공정 및 조정된 취약점 공개(Coordinated Vulnerability Disclosure, CVD)' — 산업용 서보 드라이브 제조사는 제품 생명주기 동안 발견되는 보안 취약점을 효율적으로 수집·분석하고 조치하기 위해 '조정된 취약점 공개(CVD)' 정책을 수립하고, ENISA(유럽사이버보안청) 및 국가 주관 기관에 취약점을 의무적으로 신고할 수 있는 프로세스를 구축해야 합니다.
- 보고서 기재 조항(미검증): 원문 조항 미추출
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #238 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:45:36 (원문 Date; 시간대 미표기)
- 원문 commit: [f7393876ffa7e92b207ce2a7172e0471553527ee](https://github.com/useformotor3/ai-discord-bot/commit/f7393876ffa7e92b207ce2a7172e0471553527ee)
- 원문 파일: [research_archive/2026-11-12_194536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_194536.md)
- 핵심 주장 주제: '취약점 핸들링 및 조정된 취약점 공개(Coordinated Vulnerability Disclosure, CVD) 프로세스 구축' — 산업용 서보 드라이브 제조사는 제품 생명주기 동안 발견되는 보안 취약점을 체계적으로 수집·분석하고 조치하기 위한 '조정된 취약점 공개(CVD)' 프로세스를 문서화하고 운영해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part II), Article 11, Article 11 - Vulnerability handling requi, Part II - Vulnerability handling requi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #239 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:50:34 (원문 Date; 시간대 미표기)
- 원문 commit: [d1cb6d40ffd8b77343c1a5f62f86e142b28d11fb](https://github.com/useformotor3/ai-discord-bot/commit/d1cb6d40ffd8b77343c1a5f62f86e142b28d11fb)
- 원문 파일: [research_archive/2026-11-12_195034.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_195034.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 펌웨어/소프트웨어 업데이트 생명주기 관리 및 부트 보안(Secure Boot & Update Mechanisms) — 산업용 서보 드라이브의 펌웨어 및 소프트웨어 업데이트는 무결성과 진위가 보장된 안전한 메커니즘을 통해 이루어져야 하며, 업데이트 실패 시 시스템 복구(Rollback/Recovery) 기능이 필수적으로 수반되어야 합니다. 이는 CRA Annex I의 필수 사이버 보안 요구사
- 보고서 기재 조항(미검증): Annex I, Annex I(Essential Requirements), Part I(Requirements on products with d, Annex I)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #240 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 19:55:31 (원문 Date; 시간대 미표기)
- 원문 commit: [8495aecfa5cd042e0de2f32ab2e6d9ae514e0846](https://github.com/useformotor3/ai-discord-bot/commit/8495aecfa5cd042e0de2f32ab2e6d9ae514e0846)
- 원문 파일: [research_archive/2026-11-12_195531.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_195531.md)
- 핵심 주장 주제: ‘취약점 처리 프로세스 및 조율된 취약점 공개(Coordinated Vulnerability Disclosure, CVD) 의무’ — 제조사는 제품 생명주기 동안 발견된 취약점과 보안 이슈를 안전하게 접수하고 처리하기 위한 **조율된 취약점 공개(CVD) 정책 및 프로세스**를 반드시 수립해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I Section 1(Security requirements, Article 11 (Reporting obligations of manu, Annex I, Part II (Requirements pertaining to vu
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #241 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:00:50 (원문 Date; 시간대 미표기)
- 원문 commit: [e2ba647ca49546bb56f49ea4965be38acf95e27d](https://github.com/useformotor3/ai-discord-bot/commit/e2ba647ca49546bb56f49ea4965be38acf95e27d)
- 원문 파일: [research_archive/2026-11-12_200050.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_200050.md)
- 핵심 주장 주제: "안전 관련 펌웨어/부트로더의 무결성 검증 및 암호학적 서명(Cryptographic Signing & Secure Boot)을 통한 공급망 악성 변조 방지" — 산업용 서보 드라이브의 펌웨어 및 부트 로더 업데이트 시 악성 코드 주입을 원천 차단하기 위해, 암호학적 서명(Cryptographic Signature) 검증과 하드웨어 기반 루트 오브 트러스트(Root of Trust)를 통한 안전한 부팅(Secure Boot) 메커니즘을
- 보고서 기재 조항(미검증): Annex I), Annex I, Annex I (Requirements for products with, Part I (Security requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #242 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:05:46 (원문 Date; 시간대 미표기)
- 원문 commit: [f01b01995d137e41400094498448d6d5cab5842b](https://github.com/useformotor3/ai-discord-bot/commit/f01b01995d137e41400094498448d6d5cab5842b)
- 원문 파일: [research_archive/2026-11-12_200546.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_200546.md)
- 핵심 주장 주제: '안전한 부팅(Secure Boot) 및 런타임 무결성(Runtime Integrity) 검증을 위한 암호 4장이 장착된 하드웨어 기반 신뢰 루트(Root of Trust) 구축 의무' — **주제:** 서보 드라이브 펌웨어 변조 방지 및 실시간 제어 환경을 위한 하드웨어 기반 '신뢰 루트(Root of Trust)' 및 안전한 부팅(Secure Boot) 강제화
- 보고서 기재 조항(미검증): Annex I(Essential Requirements), Part I(Requirements relating to the cy, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #243 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:10:39 (원문 Date; 시간대 미표기)
- 원문 commit: [6306c870f3e68a1be6c342352c4d2fe11fb7cfee](https://github.com/useformotor3/ai-discord-bot/commit/6306c870f3e68a1be6c342352c4d2fe11fb7cfee)
- 원문 파일: [research_archive/2026-11-12_201039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_201039.md)
- 핵심 주장 주제: '안전한 펌웨어 업데이트 및 암호화 서명을 통한 무결성 보장(Secure Update and Cryptographic Integrity)' — 산업용 서보 드라이브(Servo Drive)는 모터 제어라는 물리적 위험성을 내포하므로, 악성 펌웨어 주입을 원천 차단하기 위한 **강력한 암호화 기반의 부트 및 무손실 펌웨어 업데이트 메커니즘**을 반드시 구현해야 합니다. 이는 CRA Annex I의 필수 사이버 보안 요구사항을 충족하기 위한
- 보고서 기재 조항(미검증): Annex I, Annex I(Essential requirements), Annex I - Essential Cybersecurity Requi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #244 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:15:40 (원문 Date; 시간대 미표기)
- 원문 commit: [793fa1bda0d085a7b570466aceb465778991205f](https://github.com/useformotor3/ai-discord-bot/commit/793fa1bda0d085a7b570466aceb465778991205f)
- 원문 파일: [research_archive/2026-11-12_201540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_201540.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기(최소 5년) 동안 발견된 취약점에 대한 보안 업데이트를 **사용자에게 무상으로 제공**해야 하며, 이를 이행하기 위한 **취약점 수명주기 관리 프로세스와 상세 기술 문서(Technical Documentation)**를 규정된 양식에 맞춰 엄격히 유지·공
- 보고서 기재 조항(미검증): Annex I(, Annex VII, Annex I, Annex VII), Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #245 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:20:37 (원문 Date; 시간대 미표기)
- 원문 commit: [ba009e62076e3009c4906de4eebd3d774808eee9](https://github.com/useformotor3/ai-discord-bot/commit/ba009e62076e3009c4906de4eebd3d774808eee9)
- 원문 파일: [research_archive/2026-11-12_202037.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_202037.md)
- 핵심 주장 주제: '안전한 펌웨어 업데이트 메커니즘 및 암호화 서명(Secure Boot & Signed Firmware Updates)' — 산업용 서보 드라이브의 사이버 회복력 확보를 위해, 제조사는 무단 변조를 방지하는 암호화된 서명 기반의 펌웨어 업데이트 메커니즘을 강제하고, 업데이트 프로세스 전반에서 무결성과 기밀성을 기술적으로 보장해야 합니다.
- 보고서 기재 조항(미검증): Annex I(Essential Requirements) Part I, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #246 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:25:34 (원문 Date; 시간대 미표기)
- 원문 commit: [2093fce301d2ae24ac88e4b4ecf46a2bb9ac4d5b](https://github.com/useformotor3/ai-discord-bot/commit/2093fce301d2ae24ac88e4b4ecf46a2bb9ac4d5b)
- 원문 파일: [research_archive/2026-11-12_202534.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_202534.md)
- 핵심 주장 주제: "안전한 부트(Secure Boot) 및 펌웨어 업데이트 무결성 검증(Cryptographic Verification of Firmware Updates)" — 서보 드라이브의 펌웨어 변조를 방지하기 위해 암호학적 서명이 포함된 안전한 부트(Secure Boot) 및 안전한 펌웨어 업데이트 메커니즘을 구현해야 합니다. 이는 실시간 모션 제어 시스템의 물리적 오작동을 유발하는 사이버 공격을 원천 차단하기 위한 필수 요건입니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #247 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:30:55 (원문 Date; 시간대 미표기)
- 원문 commit: [22dde0dab1b714bc0265bd6250b099dbceb552bc](https://github.com/useformotor3/ai-discord-bot/commit/22dde0dab1b714bc0265bd6250b099dbceb552bc)
- 원문 파일: [research_archive/2026-11-12_203055.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_203055.md)
- 핵심 주장 주제: ‘취약점 무상 패치 제공 의무 및 수명 주기 동안의 보안 업데이트 관리(Vulnerability Handling and Free-of-Charge Security Updates)’ — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(Support Period) 동안 발견되는 모든 취약점에 대해 **추가 비용 없이(Free of charge)** 보안 업데이트 및 패치를 제공해야 하며, 실시간 모션 제어의 중단 없이 
- 보고서 기재 조항(미검증): Annex I(Essential requirements), Annex I, Part II, Article 11 (Manufacturer, Annex I (Cybersecurity requirements - P
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #248 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:35:29 (원문 Date; 시간대 미표기)
- 원문 commit: [a0a46dcf518a15198b7e1dfb6a352c267ee0b72a](https://github.com/useformotor3/ai-discord-bot/commit/a0a46dcf518a15198b7e1dfb6a352c267ee0b72a)
- 원문 파일: [research_archive/2026-11-12_203529.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_203529.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 실시간 모션 제어 환경에서 가장 핵심적인 '취약점 통지(Vulnerability Notification) 의무'와 공급망(Supply Chain) 전반에 걸친 '오픈소스/상용 컴포넌트 기반 취약점 식별 및 후속 조치 메커니즘' — **주제:** 서보 드라이브 제조사의 강제적 취약점 통지(Vulnerability Notification) 및 실시간 펌웨어 공급망 보안 관리 메커니즘
- 보고서 기재 조항(미검증): Article 11 (Reporting obligations of manu, Annex I, Part II (Vulnerability handling requir, Article 11, Annex I (Security requirements) - Part
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #249 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:40:42 (원문 Date; 시간대 미표기)
- 원문 commit: [ab834285e5cea762a93064377582ef96349cc1b0](https://github.com/useformotor3/ai-discord-bot/commit/ab834285e5cea762a93064377582ef96349cc1b0)
- 원문 파일: [research_archive/2026-11-12_204042.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_204042.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 펌웨어 업데이트 라이프사이클 및 취약점 무상 패치 의무(Vulnerability Handling and Free-of-Charge Security Updates) — **핵심 내용 1:** EU CRA 제11조 및 Annex I에 따라 서보 드라이브 제조사는 제품의 예상 사용 기간(최소 5년) 동안 발견된 취약점에 대해 보안 업데이트를 무상으로 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Annex I(Requirements for products with, Article 11 (Obligations of manufacturers), Part I (Requirements for products with, Article 11(2)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #250 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:45:39 (원문 Date; 시간대 미표기)
- 원문 commit: [f2f0e038f3b1254f3eb5d4e0e715fbde4a06898d](https://github.com/useformotor3/ai-discord-bot/commit/f2f0e038f3b1254f3eb5d4e0e715fbde4a06898d)
- 원문 파일: [research_archive/2026-11-12_204539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_204539.md)
- 핵심 주장 주제: 'CRA Annex I(Part I)에 따른 필수 보안 요건 중 서보 드라이브의 접근 제어, 하드웨어 루트 오브 트러스트(RoT), 그리고 민감한 제어 데이터 보호' — 산업용 서보 드라이브는 CRA Annex I에 따라 무단 물리적·논리적 접근을 방지하기 위한 하드웨어 기반의 신뢰점(Root of Trust)을 구축하고, 모션 제어 로직 및 안전 관련 설정값과 같은 민감한 자산을 강력한 암호화 메커니즘으로 보호해야 합니다.
- 보고서 기재 조항(미검증): Annex I(Part I), Annex I, Annex I), Part I, Annex I.1(g)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(e),(f)와 대조; 특정 알고리즘/TPM/Root of Trust/서명 구현은 제조사 공식 문서 및 SKU 확인 전 UNVERIFIED; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #251 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:50:40 (원문 Date; 시간대 미표기)
- 원문 commit: [8367a0507667afd7f15db0d23e13a5bc15e44336](https://github.com/useformotor3/ai-discord-bot/commit/8367a0507667afd7f15db0d23e13a5bc15e44336)
- 원문 파일: [research_archive/2026-11-12_205040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_205040.md)
- 핵심 주장 주제: "디지털 요소가 포함된 제품의 지원 기간 종료 시점의 취약점 처리 및 보안 공지(End of Support & Vulnerability Handling / Annex I, Part II)" — 산업용 서보 드라이브 제조사는 제품의 지원 종료(End of Support) 시점을 명확히 공지하고, 지원 기간 동안 발견된 취약점에 대해 무상 보안 업데이트를 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Part II), Annex I (Security Requirements) Part II, Article 13(2), Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #252 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 20:55:35 (원문 Date; 시간대 미표기)
- 원문 commit: [3bb26fee68700514294c419e94e98d61b709823f](https://github.com/useformotor3/ai-discord-bot/commit/3bb26fee68700514294c419e94e98d61b709823f)
- 원문 파일: [research_archive/2026-11-12_205535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_205535.md)
- 핵심 주장 주제: 산업용 서보 드라이브(Servo Drive)의 물리적·논리적 접근 제어 및 서비스 거부(DoS, Denial of Service) 방지 메커니즘 — 산업용 서보 드라이브는 모션 제어 환경에서 실시간 가용성 유지를 위해 무단 물리적·논리적 접근으로부터 보호되고, 통신 인터페이스를 통한 DoS(서비스 거부) 공격을 방어할 수 있는 설계적 조치를 반드시 갖추어야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #253 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:00:54 (원문 Date; 시간대 미표기)
- 원문 commit: [fa0cbafec29ee11e17591d32d70c921e3addd141](https://github.com/useformotor3/ai-discord-bot/commit/fa0cbafec29ee11e17591d32d70c921e3addd141)
- 원문 파일: [research_archive/2026-11-12_210054.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_210054.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 발견된 취약점 및 중대한 보안 사고를 지정된 단일 창구(CSIRTs Network / ENISA)에 **기계 판독 가능한 표준 형식(Machine-readable format)**으로 지연 없이 자동 보고할 수 있는 기술적 체계를 갖추어야 합니다.
- 보고서 기재 조항(미검증): Annex II... Manufacturers shall, Article 14 - Reporting obligations of man
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #254 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:05:37 (원문 Date; 시간대 미표기)
- 원문 commit: [dd96ddd0cf1dd129bbb553412f56ffdfaf30ef7c](https://github.com/useformotor3/ai-discord-bot/commit/dd96ddd0cf1dd129bbb553412f56ffdfaf30ef7c)
- 원문 파일: [research_archive/2026-11-12_210537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_210537.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 '취약점 처리 프로세스 및 무상 보안 패치 의무(Vulnerability Handling and Free Security Updates)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 기간(또는 최소 5년) 동안 발견된 취약점을 무상으로 조치해야 하며, 이를 위한 취약점 접수·공개 프로세스와 보안 업데이트 배포 체계를 기술 문서에 명시하고 엄격히 이행해야 합니다.
- 보고서 기재 조항(미검증): Article 11, Annex I), Annex I, Part II), Annex VII)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #255 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:10:40 (원문 Date; 시간대 미표기)
- 원문 commit: [c193880be48ccbc4ce7230c9d273c1331c9b18d3](https://github.com/useformotor3/ai-discord-bot/commit/c193880be48ccbc4ce7230c9d273c1331c9b18d3)
- 원문 파일: [research_archive/2026-11-12_211040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_211040.md)
- 핵심 주장 주제: "제품 생명주기 전반에 걸친 취약점 처리 의무 및 무상 보안 패치 제공 (Vulnerability Handling & Free Security Updates)" — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(또는 최소 5년) 동안 발견되는 모든 취약점을 무상으로 처리하고, 보안 업데이트를 자동으로 배포할 수 있는 체계를 갖추어야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements relating to the c, Annex II (Information and instructions
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #256 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:15:40 (원문 Date; 시간대 미표기)
- 원문 commit: [8fe5e30e65bbacf33d4f49eb298e5f1f4970eea3](https://github.com/useformotor3/ai-discord-bot/commit/8fe5e30e65bbacf33d4f49eb298e5f1f4970eea3)
- 원문 파일: [research_archive/2026-11-12_211540.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_211540.md)
- 핵심 주장 주제: "CRA Annex I에 따른 취약점 무상 패치 의무화 및 책임 공개 제도(Vulnerability Handling and Free-of-Charge Updates)" — 서보 드라이브 제조사는 제품의 예상 수명 기간(또는 최소 5년) 동안 발견되는 모든 취약점을 무상으로 조치하고 보안 업데이트(Security Updates)를 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Annex I(, Article 14(, Annex I (Cybersecurity requirements - P, Article 14 (Obligations of manufacturers)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #257 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:20:43 (원문 Date; 시간대 미표기)
- 원문 commit: [c6d28b823f9dbac57fc18c3923ac6d11b3121690](https://github.com/useformotor3/ai-discord-bot/commit/c6d28b823f9dbac57fc18c3923ac6d11b3121690)
- 원문 파일: [research_archive/2026-11-12_212043.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_212043.md)
- 핵심 주장 주제: "제품 생명주기 전반에 걸친 취약점 처리 의무 및 취약점 핸들링 프로세스(Vulnerability Handling)" — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 사용 기간(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 수리(패치 배포)해야 하며, 이를 위해 공식적인 취약점 처리 프로세스를 구축하고 사후 관리 체계를 문서화해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I (Essential Requirements), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #258 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:25:32 (원문 Date; 시간대 미표기)
- 원문 commit: [4ca3fa9aca3e0754310c8dd35c3f52cb17e7fd8e](https://github.com/useformotor3/ai-discord-bot/commit/4ca3fa9aca3e0754310c8dd35c3f52cb17e7fd8e)
- 원문 파일: [research_archive/2026-11-12_212532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_212532.md)
- 핵심 주장 주제: "SBOM(Software Bill of Materials, 소프트웨어 자재 명세서) 및 취약점 핸들링(Vulnerability Handling)" — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품에 포함된 모든 오픈소스 및 상용 구성 요소를 식별하는 기계 판독 가능한 SBOM을 작성·유지해야 하며, 발견된 취약점에 대해 지체 없이 무상 보안 패치를 배포할 수 있는 취약점 처리 프로세스를 구축해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Requirements for products with, Article 13 (Obligations of manufacturers), Article 13(6), Annex I, Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part II(1)의 top-level dependencies와 Annex II point 9의 사용자 접근정보 조건부 규칙, Article 31/Annex VII 기술문서 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #259 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:30:53 (원문 Date; 시간대 미표기)
- 원문 commit: [95e84a97584a30bfd3be5adcb6b1f32cff0b6cbd](https://github.com/useformotor3/ai-discord-bot/commit/95e84a97584a30bfd3be5adcb6b1f32cff0b6cbd)
- 원문 파일: [research_archive/2026-11-12_213053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_213053.md)
- 핵심 주장 주제: "제품 보안 취약점 처리 및 무상 패치 의무 (Vulnerability Handling and Free-of-Charge Security Updates)" — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 주기 동안 발견되는 모든 취약점을 적시에 무료로 패치(무상 보안 업데이트 제공)해야 하며, 이를 위한 취약점 처리 프로세스와 취약점 보고 체계를 의무적으로 구축해야 합니다.
- 보고서 기재 조항(미검증): Annex I, Article 14), Article 11), Article 11 (Reporting obligations of manu, Article 14 (Security requirements and vul
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #260 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:35:37 (원문 Date; 시간대 미표기)
- 원문 commit: [7073d78b07493e4562bfb189a33606949261d356](https://github.com/useformotor3/ai-discord-bot/commit/7073d78b07493e4562bfb189a33606949261d356)
- 원문 파일: [research_archive/2026-11-12_213537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_213537.md)
- 핵심 주장 주제: "제품 생명주기 전반에 걸친 취약점 무료 처리 의무 및 보안 업데이트 제공(Vulnerability handling and security updates)" — 서보 드라이브 제조사는 CRA에 따라 제품의 예상 사용 기간(또는 최소 5년) 동안 발견되는 보안 취약점을 무상으로 조치해야 하며, 취약점 수정 패치 및 업데이트를 안전한 메커니즘을 통해 지체 없이 배포해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Article 11 (Obligations of manufacturers), Annex I (Requirements with, Article 11, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #261 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:40:44 (원문 Date; 시간대 미표기)
- 원문 commit: [5dd12d2a5ab2af3b56e24292f50605e0a63df003](https://github.com/useformotor3/ai-discord-bot/commit/5dd12d2a5ab2af3b56e24292f50605e0a63df003)
- 원문 파일: [research_archive/2026-11-12_214044.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_214044.md)
- 핵심 주장 주제: "소프트웨어 자재 명세서(SBOM, Software Bill of Materials) 작성 및 관리 의무" — 산업용 서보 드라이브 제조사는 EU CRA 규정에 따라 제품에 포함된 모든 구성 요소와 오픈소스 소프트웨어를 식별할 수 있는 기계 판독 가능한 소프트웨어 자재 명세서(SBOM)를 작성하고 유지해야 합니다. 이는 공급망 투명성을 확보하고 취약점 발생 시 신속한 식별 및 대응을 위한 필수 법적 요건입니다.
- 보고서 기재 조항(미검증): Annex I (Security requirements - Part I, Article 13 (Obligations of manufacturers), Annex I, Article 31., Article 13(6)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part II(1)의 top-level dependencies와 Annex II point 9의 사용자 접근정보 조건부 규칙, Article 31/Annex VII 기술문서 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #262 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:45:50 (원문 Date; 시간대 미표기)
- 원문 commit: [e9153cb642b59082d70a5a8bd76ab7ee9dce59ac](https://github.com/useformotor3/ai-discord-bot/commit/e9153cb642b59082d70a5a8bd76ab7ee9dce59ac)
- 원문 파일: [research_archive/2026-11-12_214550.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_214550.md)
- 핵심 주장 주제: "취약점 처리 및 무상 보안 업데이트 의무(Vulnerability Handling and Free-of-Charge Security Updates)" — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 즉시 패치할 수 있는 프로세스를 구축해야 합니다. 또한, 취약점 정보는 지정된 기관(ENISA 및 관할 CSIRT)과 사용자에게 투명하게 공개하고 조치해야 합니다.
- 보고서 기재 조항(미검증): Article 11 (Manufacturer obligations - Vu, Annex I (Essential cybersecurity requir, Annex I, Article 11(2)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #263 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:50:38 (원문 Date; 시간대 미표기)
- 원문 commit: [c742d5f1e75893b8ba011f266d94f68907f913f5](https://github.com/useformotor3/ai-discord-bot/commit/c742d5f1e75893b8ba011f266d94f68907f913f5)
- 원문 파일: [research_archive/2026-11-12_215038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_215038.md)
- 핵심 주장 주제: "취약점 처리 및 무상 보안 업데이트 의무(Vulnerability Handling and Free Security Updates)" — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 관리하고, 보안 업데이트를 추가 비용 없이(무상으로) 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Article 11 (Obligations of manufacturers), Annex I (Requirements with regard to th, Annex I, Article 11(7)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #264 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 21:55:32 (원문 Date; 시간대 미표기)
- 원문 commit: [ab205d39e1022c92d451c46f6eb772d9989ac1d0](https://github.com/useformotor3/ai-discord-bot/commit/ab205d39e1022c92d451c46f6eb772d9989ac1d0)
- 원문 파일: [research_archive/2026-11-12_215532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_215532.md)
- 핵심 주장 주제: "취약점 처리 및 무상 보안 업데이트 의무(Vulnerability Handling and Free-of-Charge Security Updates)" — CRA에 따라 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 지체 없이 무료로 수정해야 하며, 이를 위해 구조화된 취약점 관리 프로세스 및 보안 업데이트 배포 메커니즘을 기술 문서에 구현하고 입증해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I, Article 10 (Obligations of manufacturers), Annex I (Requirements with which produc, Article 10
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #265 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:00:54 (원문 Date; 시간대 미표기)
- 원문 commit: [9a1746c798a5bf1790a3af5052739ded5cf6c82f](https://github.com/useformotor3/ai-discord-bot/commit/9a1746c798a5bf1790a3af5052739ded5cf6c82f)
- 원문 파일: [research_archive/2026-11-12_220054.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_220054.md)
- 핵심 주장 주제: 통신 보안, 파라미터 무결성, 펌웨어 라이프사이클, 인터페이스 접근 제어, 그리고 SBOM(Software Bill of Materials) — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 주기 동안 발견되는 취약점을 안전하게 신고받을 수 있는 취약점 공개 정책을 운영하고, 이에 대한 보안 업데이트를 사용자에게 무상으로 제공해야 합니다. 또한, 관련 취약점 정보는 지정된 취관(CSIRTs 등) 및 EU 수준의 중
- 보고서 기재 조항(미검증): Annex I, Part I - Security Requirements), Part II - Vulnerability Handling Requi, Article 11), Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part II(1)의 top-level dependencies와 Annex II point 9의 사용자 접근정보 조건부 규칙, Article 31/Annex VII 기술문서 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #266 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:05:39 (원문 Date; 시간대 미표기)
- 원문 commit: [d8f06c4db5f688a9acb58c4938e456c6daf19d6f](https://github.com/useformotor3/ai-discord-bot/commit/d8f06c4db5f688a9acb58c4938e456c6daf19d6f)
- 원문 파일: [research_archive/2026-11-12_220539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_220539.md)
- 핵심 주장 주제: "취약점 핸들링 및 무상 보안 업데이트 의무 (Vulnerability Handling and Free-of-Charge Security Updates)" — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 제조사의 비용 부담 없이 신속하게 처리(무상 패치 제공)할 수 있는 프로세스를 구축해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements) Part I, Annex I (Security requirements for prod, Article 11 (Reporting obligations of manu, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #267 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:10:40 (원문 Date; 시간대 미표기)
- 원문 commit: [f1e97549164913beed29610fbb1182194902c3f8](https://github.com/useformotor3/ai-discord-bot/commit/f1e97549164913beed29610fbb1182194902c3f8)
- 원문 파일: [research_archive/2026-11-12_221040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_221040.md)
- 핵심 주장 주제: '취약점 처리 및 무상 보안 업데이트(Vulnerability Handling and Free Security Updates)' — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 취약점을 무상으로 조치해야 하며, 이를 위해 구조화된 취약점 관리 및 보안 업데이트 배포 프로세스를 구축해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #268 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:15:37 (원문 Date; 시간대 미표기)
- 원문 commit: [8a181d15e2a415a6751052533f362e574f8722c4](https://github.com/useformotor3/ai-discord-bot/commit/8a181d15e2a415a6751052533f362e574f8722c4)
- 원문 파일: [research_archive/2026-11-12_221537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_221537.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 필수 CRA 핵심 주제인 '취약점 무료 공개 및 무상 패치 의무(Vulnerability Handling and Free-of-Charge Updates)' — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 조치해야 하며, 패치 및 보안 업데이트를 사용자에게 기본적으로 무료로 제공하고 이를 투명하게 관리해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements), Article 13 (Obligations of manufacturers), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #269 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:20:41 (원문 Date; 시간대 미표기)
- 원문 commit: [3d2cf63ce8fd5034f879530147d61e4fc60756ab](https://github.com/useformotor3/ai-discord-bot/commit/3d2cf63ce8fd5034f879530147d61e4fc60756ab)
- 원문 파일: [research_archive/2026-11-12_222041.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_222041.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 필수 CRA 핵심 주제 중 하나인 "취약점 처리 및 무상 보안 패치 의무(Vulnerability Handling and Free-of-Charge Security Updates)" — 산업용 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 취약점에 대해 적시에 무상으로 보안 패치(Updates)를 제공해야 하며, 이를 위한 취약점 취급 공정(Vulnerability Handlin
- 보고서 기재 조항(미검증): Annex I(, Annex I, Article 13 (Manufacturer obligations)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #270 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:25:37 (원문 Date; 시간대 미표기)
- 원문 commit: [10dec15d1430bcf054d97eec405f452abd488525](https://github.com/useformotor3/ai-discord-bot/commit/10dec15d1430bcf054d97eec405f452abd488525)
- 원문 파일: [research_archive/2026-11-12_222537.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_222537.md)
- 핵심 주장 주제: '취약점 수명주기 관리 및 무상 보안 패치 의무(Vulnerability Handling and Free-of-Charge Security Updates)' — 산업용 서보 드라이브 제조사는 제품의 예상 수명주기(또는 최소 5년) 동안 발견되는 취약점을 무상으로 처리하고, 보안 업데이트를 자동으로 또는 사용자가 쉽게 접근할 수 있는 방식으로 제공해야 합니다. 또한, 취약점 신고 절차(Vulnerability Disclosure Poli
- 보고서 기재 조항(미검증): Annex I), Annex I, Part I, Article 10
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #271 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:30:57 (원문 Date; 시간대 미표기)
- 원문 commit: [a20655505727986976be817a40c0c98a33e5a4f7](https://github.com/useformotor3/ai-discord-bot/commit/a20655505727986976be817a40c0c98a33e5a4f7)
- 원문 파일: [research_archive/2026-11-12_223057.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_223057.md)
- 핵심 주장 주제: "취약점 무상 공개 및 보안 업데이트 제공 의무 (Vulnerability Handling and Free-of-Charge Security Updates)" — 서보 드라이브 제조사는 제품의 예상 수명 주기(또는 최소 5년) 동안 발견된 보안 취약점을 무상으로 패치하고, 취약점 처리 정책을 공개해야 합니다.
- 보고서 기재 조항(미검증): Article 11, Annex I, Part II), Annex I (Requirements for products with, Part II (Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(8)의 예상 사용기간 및 5년 미만 예외, Article 13(9)의 업데이트 보관기간을 구분; Annex I Part II(8) 무상 업데이트와 혼동 여부; Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #272 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:35:36 (원문 Date; 시간대 미표기)
- 원문 commit: [8a7ad884161b626456df5cf4fe9732f7bfe904e1](https://github.com/useformotor3/ai-discord-bot/commit/8a7ad884161b626456df5cf4fe9732f7bfe904e1)
- 원문 파일: [research_archive/2026-11-12_223536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_223536.md)
- 핵심 주장 주제: "취약점 자동 보고 의무 및 조치 (Vulnerability Handling and Reporting Obligations)" — 서보 드라이브 제조사는 EU 시장 공급 이후 발견되는 모든 취약점과 보안 사고를 유럽망정보보호원(ENISA) 및 관할 국가기관에 법적 기한 내에 의무적으로 보고해야 합니다.
- 보고서 기재 조항(미검증): Article 11, Article 14, Article 11(1), Article 14(1)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #273 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:40:38 (원문 Date; 시간대 미표기)
- 원문 commit: [4a0545096c8535072885234b5aca095a659c6965](https://github.com/useformotor3/ai-discord-bot/commit/4a0545096c8535072885234b5aca095a659c6965)
- 원문 파일: [research_archive/2026-11-12_224038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_224038.md)
- 핵심 주장 주제: "기본 보안 설정(Secure by Default) 및 초기 취약점 감소 메커니즘" — 산업용 서보 드라이브는 출고 시(Out-of-the-box)부터 무단 접근을 방지하는 안전한 기본 설정(Secure by Default) 상태여야 하며, 사용자가 첫 부팅 시 고유한 비밀번호 설정 등을 강제하는 메커니즘을 갖추어 공급망 단계에서의 초기 사이버 리스크를 원천 차단해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements relating to the c, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #274 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:45:38 (원문 Date; 시간대 미표기)
- 원문 commit: [b279a1429a8930d39a5b4bdcf6ab68451215d1cc](https://github.com/useformotor3/ai-discord-bot/commit/b279a1429a8930d39a5b4bdcf6ab68451215d1cc)
- 원문 파일: [research_archive/2026-11-12_224538.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_224538.md)
- 핵심 주장 주제: "보안 업데이트 자동화 및 최종 사용자 통지 메커니즘 (Automatic Security Updates and User Notification)" — 서보 드라이브 제조사는 발견된 취약점에 대응하기 위해 보안 업데이트(Security Updates)가 기본적으로 자동 배포될 수 있는 기술적 수단을 제공해야 합니다. 또한, 업데이트 가용성 및 적용 결과에 대해 최종 사용자에게 명확하고 시의적절한 알림을 제공할 수 있는 메커니즘을 강구해야
- 보고서 기재 조항(미검증): Annex I), Annex I (Essential Requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #275 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:50:44 (원문 Date; 시간대 미표기)
- 원문 commit: [9c535c84987c83b8f951a425a8b595a06a9ce307](https://github.com/useformotor3/ai-discord-bot/commit/9c535c84987c83b8f951a425a8b595a06a9ce307)
- 원문 파일: [research_archive/2026-11-12_225044.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_225044.md)
- 핵심 주장 주제: "취약점 공개 정책(Vulnerability Disclosure Policy, VDP) 및 보안 공지(Security Advisories) 체계" — 서보 드라이브 제조사는 제품의 예상 수명 주기 동안 발견되는 보안 취약점의 안전한 접수, 검증 및 대외 공지를 위한 투명한 취약점 공개 정책(VDP)을 수립하고 운영해야 합니다.
- 보고서 기재 조항(미검증): Annex I - Requirements for products wit, Part II - Vulnerability handling requi
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #276 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 22:55:41 (원문 Date; 시간대 미표기)
- 원문 commit: [a33b43d07636f53efc6ef4f34d2513251c23fc63](https://github.com/useformotor3/ai-discord-bot/commit/a33b43d07636f53efc6ef4f34d2513251c23fc63)
- 원문 파일: [research_archive/2026-11-12_225541.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_225541.md)
- 핵심 주장 주제: "취약점 공개 정책(Vulnerability Disclosure Policy, VDP) 및 외부 보안 연구자/이해관계자 협업 프로세스 구축" — 서보 드라이브 제조사는 EU CRA 규정에 따라 제품 사용 중 발견되는 보안 취약점을 안전하게 접수하고 처리할 수 있도록 명확한 취약점 공개 정책(VDP)을 수립하고, 대중 및 보안 연구자가 접근 가능한 투명한 연락 창구를 유지해야 합니다. 또한, 발견된 취약점의 조치 상태를 적시에 신고하고 
- 보고서 기재 조항(미검증): Annex I, Article 11 (Obligations of manufacturers, Annex I (Requirements relating to the c, Part II. Vulnerability handling requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #277 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:00:48 (원문 Date; 시간대 미표기)
- 원문 commit: [c293176605421de23e1bfbaa599e5ffb4a461172](https://github.com/useformotor3/ai-discord-bot/commit/c293176605421de23e1bfbaa599e5ffb4a461172)
- 원문 파일: [research_archive/2026-11-12_230048.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_230048.md)
- 핵심 주장 주제: "제품 기본 설정 및 보안 기능 비활성화 방지 (Secure by Default 및 Out-of-the-Box 보안 상태)" — 서보 드라이브는 출고 시(Out-of-the-box) 별도의 복잡한 보안 설정 없이도 안전하게 작동하도록 **'Secure by Default'** 상태로 제공되어야 하며, 위험한 기본 인증 정보나 불필요하게 개방된 서비스 및 포트가 기본적으로 비활성화되어 있어야 합니다. 또한, 사용자가 보안 기능을 임의로 
- 보고서 기재 조항(미검증): Annex I(, Part I (Requirements for products with, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #278 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:05:36 (원문 Date; 시간대 미표기)
- 원문 commit: [333543abe0e76768a563f0a2e04e9f5c0da9e475](https://github.com/useformotor3/ai-discord-bot/commit/333543abe0e76768a563f0a2e04e9f5c0da9e475)
- 원문 파일: [research_archive/2026-11-12_230536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_230536.md)
- 핵심 주장 주제: '기본 설정(Secure by Default)에 따른 제품 출하 및 초기 사용자 인증 강화 의무' — 서보 드라이브는 공장 출하 시(Out-of-the-box) 무단 접근을 원천 차단하기 위해 **안전한 기본 설정(Secure by default)** 상태여야 하며, 특히 **고유하고 변경 가능한 초기 비밀번호**나 강력한 초기 인증 메커니즘을 강제해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements Table), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #279 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:10:38 (원문 Date; 시간대 미표기)
- 원문 commit: [e75f76bd907837bd0d37b537a0b8ee0ccdff0d95](https://github.com/useformotor3/ai-discord-bot/commit/e75f76bd907837bd0d37b537a0b8ee0ccdff0d95)
- 원문 파일: [research_archive/2026-11-12_231038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_231038.md)
- 핵심 주장 주제: '보안에 취약한 상태로 제품이 시장에 출시되지 않도록 하는 기본 설정(Secure by Default) 및 초기 상태의 무결성 보장' — 서보 드라이브는 시장 출시 시점에 외부 공격면(Attack Surface)을 최소화하기 위해 불필요한 포트, 서비스, 기본 계정이 비활성화된 'Secure by Default' 상태로 제공되어야 합니다. 또한, 사용자가 최초 전원을 인가할 때 안전한 초기 설정(Out-of-the-box securit
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements with regard to th, Article 10 (Obligations of manufacturers), Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #280 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:15:35 (원문 Date; 시간대 미표기)
- 원문 commit: [1ee8c4ef04708993d58640b8a62dc9327f6b8fd1](https://github.com/useformotor3/ai-discord-bot/commit/1ee8c4ef04708993d58640b8a62dc9327f6b8fd1)
- 원문 파일: [research_archive/2026-11-12_231535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_231535.md)
- 핵심 주장 주제: ‘서보 드라이브의 보안 사고 자동 보고 의무(Incident Reporting Obligations)’ — 서보 드라이브 제조사는 제품의 보안에 영향을 미치는 취약점이나 중대한 보안 사고(Incident) 발생 시, 법적으로 지정된 기한 내에 관할 국가 기관(CSIRT) 및 ENISA에 의무적으로 보고해야 합니다.
- 보고서 기재 조항(미검증): Article 11 - Reporting obligations of man, Article 11 (Reporting obligations of manu, Annex VII (Information on cybersecurity, Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #281 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:20:38 (원문 Date; 시간대 미표기)
- 원문 commit: [8f38f68064176a12e179bebffed8b3b0b0fbc663](https://github.com/useformotor3/ai-discord-bot/commit/8f38f68064176a12e179bebffed8b3b0b0fbc663)
- 원문 파일: [research_archive/2026-11-12_232038.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_232038.md)
- 핵심 주장 주제: ‘중요 디지털 제품(Important Class I)의 적합성 평가 절차 및 제3자 평가(Third-party Conformity Assessment) 의존성 요건’ — 산업용 서보 드라이브는 EU CRA Annex III(Class I 중요 디지털 제품)에 해당하므로, 제조사는 자체 선언(Self-assessment)만으로 CE 마크를 부착할 수 없으며, EU 공인 기관(Notified Body)을 통한 제3자 적합성 평가 또는 조화
- 보고서 기재 조항(미검증): Annex III(Class I, Article 24, Annex III), Annex III, Annex VI
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; Article 13(17)–(19)와 Annex II point 1–9 정확한 매핑·보존/지원 종료일; point 9 SBOM 접근정보는 제조사 제공 결정 시에만 조건부; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #282 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:25:33 (원문 Date; 시간대 미표기)
- 원문 commit: [757bd881d7a30f4cfc2f4756191f4cac18a1b5fc](https://github.com/useformotor3/ai-discord-bot/commit/757bd881d7a30f4cfc2f4756191f4cac18a1b5fc)
- 원문 파일: [research_archive/2026-11-12_232533.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_232533.md)
- 핵심 주장 주제: ‘취약점 무상 패치 의무화 및 보안 업데이트 배포 무결성 보장(Vulnerability Handling & Free-of-Charge Security Updates)’ — 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 생애주기 동안 발견된 취약점에 대해 **추가 비용(무상) 없이 보안 업데이트를 제공**해야 하며, 배포되는 업데이트의 무결성과 신뢰성을 기술적으로 보장해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Security Requirements), Article 14 (Manufacturer obligations)., Annex I, Annex I., Annex I (Requirements for products with
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #283 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:30:46 (원문 Date; 시간대 미표기)
- 원문 commit: [f09360788727039708cea22b91507ebd48a15d84](https://github.com/useformotor3/ai-discord-bot/commit/f09360788727039708cea22b91507ebd48a15d84)
- 원문 파일: [research_archive/2026-11-12_233046.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_233046.md)
- 핵심 주장 주제: ‘디폴트 보안 설정(Secure by Default) 및 초기 상태의 가공 방지(Out-of-the-box Security)’ — 서보 드라이브는 출고 시(Out-of-the-box) 권한 상승을 유발하는 기본 비밀번호나 취약한 공장 초기 설정값을 제거한 **Secure by Default** 상태로 제공되어야 합니다.
- 보고서 기재 조항(미검증): Annex I (Essential Requirements) Part I, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #284 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:35:32 (원문 Date; 시간대 미표기)
- 원문 commit: [0df81ca694913687f7abe7507f5ed96e96760721](https://github.com/useformotor3/ai-discord-bot/commit/0df81ca694913687f7abe7507f5ed96e96760721)
- 원문 파일: [research_archive/2026-11-12_233532.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_233532.md)
- 핵심 주장 주제: '취약점 공개 정책(Vulnerability Disclosure Policy) 및 조정된 취약점 공표(Coordinated Vulnerability Disclosure, CVD) 프로세스' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 동안 발견되는 보안 취약점을 안전하게 접수, 처리, 공개할 수 있는 '조정된 취약점 공표(CVD)' 프로세스를 운영하고 이를 기술 문서에 포함해야 합니다. 또한, 취약점 정보는 
- 보고서 기재 조항(미검증): Annex I (Requirements) - Part II (Vulne, Annex I, Article 11 (Reporting obligations of manu, Article 11 (Reporting obligations), Part II (Requirements pertaining to vu
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #285 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:40:40 (원문 Date; 시간대 미표기)
- 원문 commit: [757f0f00372b12bf1027db97bd6834c70cdd5a3a](https://github.com/useformotor3/ai-discord-bot/commit/757f0f00372b12bf1027db97bd6834c70cdd5a3a)
- 원문 파일: [research_archive/2026-11-12_234040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_234040.md)
- 핵심 주장 주제: '보안에 취약한 상태로 제품을 시장에 출시하는 것을 원천 방지하기 위한 기본 설정(Secure by Default) 및 초기 상태의 무결성 보장' — EU CRA Annex I에 따라 산업용 서보 드라이브는 초기 출고 시 무단 접근 및 악성 조작을 방지하기 위해 반드시 가장 안전한 상태(Secure by default)로 설정되어야 하며, 사용자가 제품을 수령한 직후 별도의 설정 변경 없이도 기본 인증 및 제한된 권한 체계가 강제 적용
- 보고서 기재 조항(미검증): Annex I, Annex I(Essential Requirements), Annex I (Essential cybersecurity requir
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #286 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:45:43 (원문 Date; 시간대 미표기)
- 원문 commit: [f3307a6cf9fe3cb2f66781981f56d7b2461dc346](https://github.com/useformotor3/ai-discord-bot/commit/f3307a6cf9fe3cb2f66781981f56d7b2461dc346)
- 원문 파일: [research_archive/2026-11-12_234543.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_234543.md)
- 핵심 주장 주제: '취약점 자동 통보 및 구조화된 취약점 정보 공유 체계(Vulnerability Reporting and Automated Machine-Readable Information Sharing)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 자사 제품에서 발견된 취약점과 관련 보안 조치 정보를 유럽연합 사이버안전국(ENISA) 및 관할 국가 당국에 정해진 법적 기한(조기 경보 24시간 이내) 내에 기계 판독 가능한 형식(Machi
- 보고서 기재 조항(미검증): Article 11
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #287 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:50:39 (원문 Date; 시간대 미표기)
- 원문 commit: [1e2cc71fcb047a5ea5310b2c2a873b51a0e66b9f](https://github.com/useformotor3/ai-discord-bot/commit/1e2cc71fcb047a5ea5310b2c2a873b51a0e66b9f)
- 원문 파일: [research_archive/2026-11-12_235039.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_235039.md)
- 핵심 주장 주제: '안전한 기본 설정(Secure by default) 및 초기 기기 상태 설정' — 산업용 서보 드라이브는 출고 시점부터 무단 접근을 방지하기 위해 변경 가능한 기본 인증 정보(Default Passwords)가 없거나, 최초 사용 시 강력한 고유 인증 설정을 강제하는 **'Secure by default(기본 안전)'** 상태로 제공되어야 합니다. 또한, 사용하지 않는 네트워크 서비스와 인터페이스는 기본적으로 비활성화되어야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Part I(, Annex I, Part I (Requirements for products with, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 실제 네트워크/원격진단 기능과 제품 경계를 확인하고 Article 13(2) 위험평가에 따라 적용성 판단; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #288 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-12 23:55:35 (원문 Date; 시간대 미표기)
- 원문 commit: [de05a7fc1e8767c2a41889d51c3d3e6be90af42b](https://github.com/useformotor3/ai-discord-bot/commit/de05a7fc1e8767c2a41889d51c3d3e6be90af42b)
- 원문 파일: [research_archive/2026-11-12_235535.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-12_235535.md)
- 핵심 주장 주제: '보안에 취약한 상태로 출고되지 않을 권리 및 시큐어 디폴트(Secure by Default) 설정 관리' — 서보 드라이브 제조사는 제품 출고 시 기본적으로 안전한 상태(Secure by default)를 유지하도록 설정해야 하며, 사용자가 별도로 변경하지 않는 한 무단 접근과 취약한 설정이 차단되도록 초기 보안 구성(Out-of-the-box security)을 강제해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements relating to the c, Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED


## 2026-11-13 reports #1–#7

### Report #1 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:00:53 (원문 Date; 시간대 미표기)
- 원문 commit: [0a644a43c8c3ef6099aa99d3fab942bbaad88803](https://github.com/useformotor3/ai-discord-bot/commit/0a644a43c8c3ef6099aa99d3fab942bbaad88803)
- 원문 파일: [research_archive/2026-11-13_000053.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_000053.md)
- 핵심 주장 주제: "보안 관련 정보 및 지침 제공 의무(Information and Instructions to the User)" 및 "사용자 계정/초기 설정 보안(Secure by Default - Default Credentials 철폐)" — 서보 드라이브 제조사는 제품 공급 시 안전한 초기 설정(Secure by default)을 강제하여 기본 관리자 계정의 무단 사용을 원천 차단하고, 최종 사용자가 보안 설정 및 잔여 수명 동안의 보안 업데이
- 보고서 기재 조항(미검증): Annex I(, Annex II(, Annex I, Annex II), Annex I (Requirements with which produc
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 13(17)–(19)와 Annex II point 1–9 정확한 매핑·보존/지원 종료일; point 9 SBOM 접근정보는 제조사 제공 결정 시에만 조건부; Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #2 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:05:36 (원문 Date; 시간대 미표기)
- 원문 commit: [5e79b4e44be05b641ecdda4bad809fdea26bf0ce](https://github.com/useformotor3/ai-discord-bot/commit/5e79b4e44be05b641ecdda4bad809fdea26bf0ce)
- 원문 파일: [research_archive/2026-11-13_000536.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_000536.md)
- 핵심 주장 주제: '취약점 공개 정책(Vulnerability Disclosure Policy) 및 보안 업데이트의 무료 제공(Free-of-charge Provision)' — 산업용 서보 드라이브 제조사는 CRA에 따라 제품의 예상 수명 기간 동안 발견된 보안 취약점을 안전하게 접수할 수 있는 취약점 공개 정책을 운영해야 하며, 식별된 취약점에 대한 보안 업데이트(패치)를 사용자에게 추가 비용 없이 무상으로 제공해야 합니다.
- 보고서 기재 조항(미검증): Annex I (Requirements for products with, Part I (Cybersecurity requirements), Annex I, Part I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(8)의 무상 보안 업데이트와 tailor-made 제품/business user 합의 예외; Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #3 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:10:44 (원문 Date; 시간대 미표기)
- 원문 commit: [2c5aa12cf8ecb97b2d176c79aab215836bdb816c](https://github.com/useformotor3/ai-discord-bot/commit/2c5aa12cf8ecb97b2d176c79aab215836bdb816c)
- 원문 파일: [research_archive/2026-11-13_001044.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_001044.md)
- 핵심 주장 주제: 제조사의 자가 평가 및 제3자 Conformity Assessment(적합성 평가) 절차와 관련 기술 문서(Technical Documentation) 편취 요건 — 산업용 서보 드라이브 제조사는 CRA Annex III에 명시된 중요급(Class II) 제품의 분류에 따라 공인된 제3자 기관(Notified Body)을 통한 적합성 평가 절차를 거치거나 조화 표준(Harmonised Standards) 기반의 엄격한 기술 문서를 작성
- 보고서 기재 조항(미검증): Annex III, Annex III(Class II), Article 24), Annex VII), Annex VIII)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Article 7/32 및 Annex III의 열거 범주·core functionality 기준; 서보 드라이브라는 이유만으로 Class I/II 단정 금지; Article 13(17)–(19)와 Annex II point 1–9 정확한 매핑·보존/지원 종료일; point 9 SBOM 접근정보는 제조사 제공 결정 시에만 조건부; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #4 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:15:45 (원문 Date; 시간대 미표기)
- 원문 commit: [782eeb3b37b58bdd2f432fbfbf33fd9ca7c26f98](https://github.com/useformotor3/ai-discord-bot/commit/782eeb3b37b58bdd2f432fbfbf33fd9ca7c26f98)
- 원문 파일: [research_archive/2026-11-13_001545.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_001545.md)
- 핵심 주장 주제: '기본 설정(Secure by Default) 상태로의 출고 및 초기화 보안 요건' — 산업용 서보 드라이브 제조사는 제품 출고 시 보안이 취약한 기본값(예: 기본 패스워드, 활성화된 불필요한 포트 등)을 제거하고, 안전한 기본 설정(Secure by default) 상태로 제공해야 하며, 사용자가 공장 초기화(Factory Reset)를 수행했을 때도 이러한 보안 상태가 안전하게 복원되도록 보장해야 합니다.
- 보고서 기재 조항(미검증): Annex I(, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #5 — P0
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:20:40 (원문 Date; 시간대 미표기)
- 원문 commit: [7dd94a4ebe6f7e7d98738897f18e8650b902f53b](https://github.com/useformotor3/ai-discord-bot/commit/7dd94a4ebe6f7e7d98738897f18e8650b902f53b)
- 원문 파일: [research_archive/2026-11-13_002040.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_002040.md)
- 핵심 주장 주제: '취약점 공개 정책(Vulnerability Disclosure Policy) 및 사용자 고지 의무(Reporting of Vulnerabilities)' — 산업용 서보 드라이브 제조사는 EU CRA에 따라 제품의 예상 수명 기간 동안 발견된 취약점과 보안 이슈를 체계적으로 수집·처리할 수 있는 취약점 공개 정책(VDP)을 수립하고, 사용자에게 적시에 보안 업데이트 및 패치 정보를 고지해야 합니다.
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements for products with, Part I (Cybersecurity requirements)
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part II(1)–(8)의 제조사 취약점 처리/CVD/업데이트 의무와 Article 14의 의무 신고 대상을 구분; Article 14(1)–(5): actively exploited vulnerability와 severe incident, 24h/72h 및 최종보고 14일/1개월 트랙; 모든 버그를 신고 대상으로 확대하지 않는지; Annex I Part I(2)(c),(f), Part II(2),(7),(8)의 업데이트·무결성·배포 위치; 서명/anti-rollback/A-B/fail-safe는 법령 문언과 설계 선택 분리; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED

### Report #6 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:25:39 (원문 Date; 시간대 미표기)
- 원문 commit: [173c4d29ee62c0e96cfadf93824d6807ef2d148a](https://github.com/useformotor3/ai-discord-bot/commit/173c4d29ee62c0e96cfadf93824d6807ef2d148a)
- 원문 파일: [research_archive/2026-11-13_002539.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_002539.md)
- 핵심 주장 주제: 산업용 서보 드라이브 제조사가 준수해야 할 "디폴트 보안 설정(Secure by Default) 및 초기 상태의 가용성/무결성 강제" — 산업용 서보 드라이브는 최초 출고 및 설치 시(Out-of-the-box), 사용자가 별도의 복잡한 보안 설정을 거치지 않아도 안전한 상태를 유지하도록 **'Secure by Default'** 원칙에 따라 가장 제한적인 권한과 비활성화된 불필요한 서비스/인터페이스를 기본값으로 제공해야 합니다. 또한
- 보고서 기재 조항(미검증): Annex I), Annex I (Requirements relating to cyber, Annex I
- 파일 단위 판정: **UNVERIFIED** (Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 우선 검증 쟁점: Annex I Part I(1),(2)(b),(d),(j)의 위험기반 요구와 tailor-made 예외; 강제 비밀번호 변경/모든 포트 차단은 보편적 직접 의무인지 별도 확인; Annex I Part I(2)(d),(j)의 접근통제·공격표면 제한; 특정 포트 일괄 차단을 법령의 직접 문언으로 과장하지 않는지; 제품 적용성 별도: 실제 서보 드라이브 SKU/핵심 기능/의도된 용도/인터페이스/업데이트 경로 및 ST MCU 주문 코드 미확정; 제조사 공식 데이터시트·RM·errata 확인 전 기술 기능 UNVERIFIED


### Report #7 — P1
- 상태: **NEW / NOT_YET_AUDITED**
- 확인일: 2026-11-13
- 생성 시각: 2026-11-13 00:30:55 (원문 Date; 시간대 미표기)
- 원문 commit: [bd50257a80c0524402c70a7da420043ecfa0f490](https://github.com/useformotor3/ai-discord-bot/commit/bd50257a80c0524402c70a7da420043ecfa0f490)
- 원문 파일: [research_archive/2026-11-13_003055.md](https://github.com/useformotor3/ai-discord-bot/blob/main/research_archive/2026-11-13_003055.md)
- 핵심 주장 주제: Secure by Default 및 초기 상태 위험 경감; 보고서는 최초 접속 강제 비밀번호 변경/기기별 고유 기본 비밀번호, 진단·디버그 포트 기본 비활성화, 공장 초기화 후 보안 패치 수준·암호키 유지가 CRA 준수에 필요하다고 주장한다.
- 보고서 기재 조항(미검증): Annex I Part I, Section 1, paragraph 2(b); Article 13 paragraph 2.
- 파일 단위 판정: **UNVERIFIED** (신규 대기; 전체 Pass A/B/C 미완료)
- Raw Text Quote 판정: **NOT_YET_AUDITED**
- 개별 주장 판정: **NOT_YET_AUDITED**
- 사전 원문 메모(최종 판정 아님): EUR-Lex 현행 Annex I Part I(2)(b)는 “made available on the market with a secure by default configuration”이라고 하며 tailor-made product/business user 합의 예외와 “original state” reset 문구를 포함한다. 보고서 quote의 “delivered”, “initial state” 표현 및 예외 생략은 verbatim quote와 불일치한다. Article 13(2)는 제조사 의무 quote가 아니라 cybersecurity risk assessment 조항이며, 인용된 제조사 설계·개발·생산 의무는 Article 13(1)에 있다. [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847) lines 888–892, 1750–1752 참조.
- 우선 검증 쟁점: Annex I Part I(2)(b)의 정확한 문언·tailor-made 예외·reset “original state”를 재확인; Article 13(1)/(2) 번호와 quote의 직접 인용 여부; forced first-boot password change/unique password, 모든 진단·디버그 포트 비활성화, factory reset 후 patch/key 보존은 법령의 보편적 구현 명령인지 위험기반 설계 선택인지 분리; 실제 제품 SKU·계정/포트·reset 동작·보안 업데이트 설계 및 제조사 근거 확인.

## 다음 감사 순서

1. P0 중 지원기간/무상 업데이트/Article 14 신고/Important Product 분류/Annex II/SBOM 주장을 우선 Pass A/B/C로 검증한다.
2. P1의 Secure-by-default/업데이트 무결성/디버그·네트워크 인터페이스 주장은 법령의 결과 요구와 특정 구현수단을 분리한다.
3. P3 warning-only 파일은 모델 호출 실패가 성공 보고서로 archive/history/state에 반영되는지 운영 실패 경로와 대조한다.
4. 다음 실행에서는 main HEAD 이후 새 commit만 추가하고 기존 queue의 commit SHA·파일 경로와 대조해 중복을 방지한다.

## 무결성 및 변경 경계

- 이번 기준 main HEAD: `bd50257a80c0524402c70a7da420043ecfa0f490`.
- 작업 브랜치 기록 대상: `cra-project-foundation`.
- main의 archive/history/state는 읽기만 했다. 원본 main 파일 수정·삭제 없음.
- `main.py`, Gemini prompt, 운영 자동화 코드, `.github/workflows/run.yml`, main 브랜치 수정 없음.
- main과 작업 브랜치 간 merge/rebase/sync 없음.
- 이번 문서 작업은 대기열/상황판/계획/세션 로그만 갱신한다. 실행하지 않은 테스트는 PASS로 기록하지 않는다.


## 2026-11-13 reports #8–#12 — Pass A/B/C batch audit completed

- Audit record: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_8_12_2026-11-13.md).
- Main-only source commits and archive blob SHAs were checked against the five report files. Original `main` archive files remain unchanged.
- #8 — P1 — CONFLICT; Raw Text Quote REJECTED. Secure-by-default theme is relevant, but draft quote/provision mapping and universal first-boot password/debug-disable claims are incorrect or overclaimed.
  - Commit: `2a295906507f0f2540a3c09cd760b5c77c4fb373`; file: `research_archive/2026-11-13_003535.md`; blob: `8141a7ff3d71cd2899e10a85c735b15351c72161`.
- #9 — P0 — CONFLICT; Raw Text Quote REJECTED. Free updates, support period, CVD, update distribution and Article 14 scope are materially conflated.
  - Commit: `fda58af984b8e5d0ad06d0f2e6bcdb19563e6914`; file: `research_archive/2026-11-13_004046.md`; blob: `c06112da2cd050b4eb0813828beb948975fb82d4`.
- #10 — P0 — CONFLICT; Raw Text Quote REJECTED. Secure-by-default is Annex I Part I(2)(b), not Part II/Class II; generic servo drive Class II and forced password details unsupported.
  - Commit: `5f45f1c28fd3b1542c4b574d495fadd009716e09`; file: `research_archive/2026-11-13_004542.md`; blob: `e9d5f5606a95567a9535de119edbbfa34739d02b`.
- #11 — P1 — CONFLICT; Raw Text Quote REJECTED. Malformed/composite quotation; broad secure-default/attack-surface themes do not create universal port/JTAG/first-use-password mandates.
  - Commit: `76589196b933c1da5ffbff47270dacf16dc4044a`; file: `research_archive/2026-11-13_005038.md`; blob: `3dab8049841c07992184993c5b18fc1dcab94836`.
- #12 — P0 — CONFLICT; Raw Text Quote REJECTED. CVD and contact obligations exist, but Article 11 is General product safety; manufacturer obligations are Article 13; Article 14 scope is limited to actively exploited vulnerabilities and severe incidents.
  - Commit: `59d1b14dcdb95badace59a13fe46a00e1e4177f9`; file: `research_archive/2026-11-13_005535.md`; blob: `acda92dbe87ffbc549a8d52d42961b4bf058b983`.

Batch result: 5/5 CONFLICT, 0 PARTIALLY_VERIFIED, 0 VERIFIED; 0/5 Raw Text Quote blocks reusable as verbatim current-law quotations. Product applicability remains UNVERIFIED. This is a non-random time-sequenced batch, not a representative archive error rate.

### Queue coverage gap
- The current main tip observed during this session is report #27 (`c7eb7296671541c1ad2268cdcee80885091f230c`). Reports #13–#27 were not part of the prior queue and remain to be registered before their audits. Do not treat this five-report batch as covering #13–#27 or the complete main archive.


## 2026-11-13 reports #13–#27 — Pass A/B/C batch audit completed

- Audit record: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_13_27_2026-11-13.md).
- Main report commits and archive blob SHA-1 values were checked read-only. No original main archive/history/state file was modified.
- Batch verdict: **15 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED**. All 15 Raw Text Quote blocks are **REJECTED** for direct quotation of current Regulation (EU) 2024/2847. Product applicability remains UNVERIFIED.
- Repeated defects: Article 11 used as manufacturer reporting/vulnerability handling; Article 14 scope expanded beyond actively exploited vulnerabilities/severe incidents; Annex I Part I product properties mixed with Part II vulnerability handling; free updates, CVD, support period and update availability conflated; Article 13(8) “whichever is shorter” misstatement; Annex II mistaken for technical documentation; secure-by-default subpoints misnumbered; forced password/MFA/JTAG/all-port-disablement claims presented as universal law; servo-drive Class I/II asserted without Annex III/core-functionality evidence.
- This is a sequential, non-random batch, not a representative archive error rate. The EUR-Lex current-law baseline was reused from the immediately preceding #8–#12 audit; this batch did not run the Phase E live fetcher.
- Per-report evidence (main commit, archive path and blob SHA-1):
  - #13 — CONFLICT; commit `5b46858ab88595ce9e5b7b33175b81c4e24e7905`; `research_archive/2026-11-13_010102.md`; blob `2e9fb641dcebcb411dca1e686de916bf09dbfcb9`; CVD/Article 14 신고 범위와 구판 NIS2 문구 혼합.
  - #14 — CONFLICT; commit `f4e8b82ad46f3fe5c5a6f55d0fcd33d44d0006d1`; `research_archive/2026-11-13_010538.md`; blob `dda0e0308d5fffb11659f6c395a9b0a3da26b1de`; Secure-by-default 구판 조항 번호 및 포트/비밀번호 보편 의무 과장.
  - #15 — CONFLICT; commit `54e67c1082d86fd8559d6c41107cdc9736ce8c76`; `research_archive/2026-11-13_011036.md`; blob `f150569deac61b8d74a424bb1c76518438816de0`; 무상 업데이트/CVD 주제는 관련되나 Annex I Part I·Article 11 오기 및 합성 인용.
  - #16 — CONFLICT; commit `c0f038825fcda6f2d546846870e0505080b96cb5`; `research_archive/2026-11-13_011537.md`; blob `2f67047e45084598819a1d7b4ccd4a463c2dc168`; 지원기간 5년 단정, Article 11/Part I 오기, quote 합성.
  - #17 — CONFLICT; commit `1e5fddc195a8f94483fdffbd3aa7b7ef4704c9e7`; `research_archive/2026-11-13_012038.md`; blob `a2a8c24d6e0933f5d6e3e6fcdb570037ed652e7e`; CVD·무상 업데이트를 Part I로 오배치, 여러 조항 합성 인용.
  - #18 — CONFLICT; commit `d5b4441be57c9a33cd256b30392f546cd6026b23`; `research_archive/2026-11-13_012535.md`; blob `a39605cfc909d39990ecc46bdd8caa5e8f97efd4`; Article 14 주제이나 Article 11로 오기, 모든 취약점/사고 신고로 범위 확대.
  - #19 — CONFLICT; commit `eb1d64f8b60127c0d68119ce06a8f0b9e63471da`; `research_archive/2026-11-13_013047.md`; blob `8211d1c2905452bf87e41722ca408119092644d1`; Article 11 오기, 지원기간 'whichever is shorter' 오류, Annex I Part II(1) 오인용.
  - #20 — CONFLICT; commit `6ec0d9eee85c141e1ab2e621d5a3989855c98c35`; `research_archive/2026-11-13_013528.md`; blob `d80151fca7d8302bd353715b3d8608412b99e065`; Secure-by-default와 integrity 하위항목 혼동, 강제 비밀번호 변경 과장.
  - #21 — CONFLICT; commit `8fafb874c5e1427d65def1b1672459d376e33567`; `research_archive/2026-11-13_014042.md`; blob `34c0a04a117ff8175bec68e93e26600b520cebb5`; Secure-by-default·지원기간·Annex II 기술문서 혼합 및 조항 오기.
  - #22 — CONFLICT; commit `3a0b1aec3c17d5ea61dcd674a71b12ba487b3b01`; `research_archive/2026-11-13_014539.md`; blob `a6695390839a167aa9a4b99473b2a70ba61dc838`; Class I/II 제품 단정, 비밀번호/MFA/포트 비활성화 보편 의무 과장.
  - #23 — CONFLICT; commit `0d5cc63bd9bbe47eb84887950c056d2d4df80f73`; `research_archive/2026-11-13_015044.md`; blob `d8315ca10d9d1d811978c73ab8ffbd77e296971d`; 초기 비밀번호 설정을 법정 강제 절차로 단정, quote의 문언·항목 오기.
  - #24 — CONFLICT; commit `4a13cfeb9cba3e378b68e52ee5e7c03990cca3ca`; `research_archive/2026-11-13_015535.md`; blob `c43117db6c681bd4b6865b955ac66a0fa012a1fd`; Secure-by-default와 업데이트 요구를 잘못된 문단·항목으로 합성 인용.
  - #25 — CONFLICT; commit `7d308b5a2b5c73385abde943412622bdc8f74317`; `research_archive/2026-11-13_020056.md`; blob `a482f9198569dfe173d63250eebee6d8f9a6f9e8`; 서보 드라이브 Class I/II 단정 및 Annex I draft 인용·하드웨어 구현 의무 과장.
  - #26 — CONFLICT; commit `d079e63339d20549361bba9d4c4de71fcb3346db`; `research_archive/2026-11-13_020541.md`; blob `132dd081b4bed0d431d8f68b8e00b3fc83b9035d`; 기본 설정·접근통제·무결성 조항 번호/문언 혼합, hardcoded credential/포트 보편 금지 과장.
  - #27 — CONFLICT; commit `c7eb7296671541c1ad2268cdcee80885091f230c`; `research_archive/2026-11-13_021039.md`; blob `3b6537c40590118c43d1fbc5f1922121d7f6d276`; 무상 업데이트/CVD 주제는 관련되나 Annex I Part I·Article 13(4) 오인용.


## 2026-11-13 — main reports #28–#32 Pass A/B/C audit

- Current main tip at queue refresh: `4452662e6cba0bb81c6efb4b309b30f4733d8f71`, Auto-archive report #91. Main history/archive inventory is 1,366/1,366 with 1,366 unique paths.
- Batch audit: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_28_32_2026-11-13.md).
- #28 CONFLICT; archive `research_archive/2026-11-13_021538.md`; blob `78de23c029c47dee16ebc82adf7123c2bf52fa4a`.
- #29 CONFLICT; archive `research_archive/2026-11-13_022039.md`; blob `e5248b9d23e94ea0ef5ad7ffb30f2dcd100e3434`.
- #30 CONFLICT; archive `research_archive/2026-11-13_022538.md`; blob `15439fdad39d1759f522023fc3f1201c1fbf4e8f`.
- #31 CONFLICT; archive `research_archive/2026-11-13_023045.md`; blob `bc85eca9a24980a199e00fc13752f158b11e059e`.
- #32 CONFLICT; archive `research_archive/2026-11-13_023540.md`; blob `71146baf92e406e18209f9981d8a7afc47620be2`.
- Batch: 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; raw direct quote reusable 0/5. Sequential non-random batch, not an archive-wide error rate.
- Method limitation: reused the existing EUR-Lex legal baseline and prior #8–#27 audit; no new E3 live fetch, PDF visual inspection or new independent official cross-source check in this batch.
- Next target: #33 onward; refresh/register all reports through current main #91 before choosing subsequent batches. Keep main read-only.


## 2026-11-13 — main reports #33–#37 audit

- Detailed report: [ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md](ARCHIVE_MANUAL_AUDIT_MAIN_ONLY_33_37_2026-11-13.md).
- #33 CONFLICT — `research_archive/2026-11-13_024039.md`, blob `c9c8f17bae8dd90890f9075927aa5fb6668c32b0`.
- #34 CONFLICT — `research_archive/2026-11-13_024544.md`, blob `97101ee32c543adc2b684c92eec4c831cbe2c479`.
- #35 CONFLICT — `research_archive/2026-11-13_025045.md`, blob `842b48aa5ba2382ce58cdddcb1f8b836c5336eb6`.
- #36 CONFLICT — `research_archive/2026-11-13_025531.md`, blob `06f32803648a15f7638add752a8b9a064d4ee3f9`.
- #37 CONFLICT — `research_archive/2026-11-13_030054.md`, blob `a8f77a2ecc3bc2301ab87a5f90d2ae6626489eab`.
- Batch 5 CONFLICT / 0 PARTIALLY_VERIFIED / 0 VERIFIED; direct quote reuse 0/5. Next target #38.
