# CRA 공식 Guidance 및 M/606 결정 Annex 감사 — 2026-11-17

- 감사 기준: 2026-11-17 (KST)
- 작업 브랜치: `cra/guidance-claim-mapping-2026-11-17`
- 기준 main: `16b5d2e732e9f5f158d2b79aa9c0c62f0488fc92`
- 범위: Commission Guidance C(2026) 5252 Annex 및 Commission Implementing Decision C(2026) 7861 Annex의 내용 확인, 서보 드라이브 CRA 적용성·설계·추적성 영향
- 상태: **M/606 Annex Commission PDF 원본 bytes/SHA-256 확인 완료; Guidance는 ANFR mirror bytes/SHA-256 확인 완료(Commission 원본과 byte identity 미확인); M/606 item 18 기한 시각 확인 완료**
- 해석 원칙: C(2026) 5252는 비구속적 Commission guidance이며 CRA 법령/법원 판결을 대체하지 않는다. C(2026) 7861 Annex의 ESO 표준 초안 채택 기한을 harmonised standard 발행일, CRA 적용일 또는 제품 인증 기한으로 오해하지 않는다.

## 1. 출처 및 취득 상태

### 1.1 Commission Guidance C(2026) 5252

- Commission publication page (27.07.2026): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
- Commission PDF download URL (Annex): https://ec.europa.eu/newsroom/dae/redirection/document/131456
- 확인 가능한 PDF mirror: https://www.anfr.fr/fileadmin/CRA/Commission_guidance_on_the_application_of_Regulation__EU__20242847__Cyber_Resilience_Act_.pdf
- 문서 표제: Brussels, 27.7.2026; C(2026) 5252 final; Annex, Commission guidance on the application of Regulation (EU) 2024/2847.
- PDF binary: 1,190,726 bytes; 84 pages; raw-byte SHA-256 `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234`; extracted text 250,162 chars; text SHA-256 `147f6649b5089cbc4d55c7af77abdcdbd04263b116960812c579fd25acda7425`.
- 취득 경로: Commission URL `https://ec.europa.eu/newsroom/dae/redirection/document/131456`를 우선 요청했으나 이 실행에서 PDF로 검증되지 않아 allowlist된 ANFR mirror를 fallback으로 사용했다. 최종 URL은 ANFR이며 mirror bytes의 hash를 확인했다. Commission-hosted 원본과 byte-for-byte 동일성은 아직 입증하지 않았다.
- 법적 지위: Guidance paragraph 8은 guidance가 경제운영자 등에게 구속력이 없고 CRA의 권위 있는 해석은 EU 사법재판소만 할 수 있음을 명시한다. 개별 제품의 case-by-case 평가를 대체하지 않는다.

### 1.2 Commission Implementing Decision C(2026) 7861 Annex (M/606)

- Commission document register record: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2026)7861&lang=en
- 직접 확인된 Annex PDF: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401
- 문서 표제: Brussels, 10.11.2026; C(2026) 7861 final; Annex to the Commission Implementing Decision amending Implementing Decision C(2025)618 on a standardisation request to CEN, Cenelec and ETSI for products with digital elements supporting Regulation (EU) 2024/2847.
- PDF binary: 151,267 bytes; 6 pages; raw-byte SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`; extracted text 8,058 chars; text SHA-256 `06409ee840550a4e602aa30b4f77a9eaf90a44735f820ce2b1239cccec6a54dd`.
- Commission document-register URL에서 PDF bytes를 직접 취득했고, PDF header, C(2026) 7861 document markers, page count, raw-byte/text SHA-256을 검증했다. 원본 파일은 7일 CI artifact로 보관되며 영구 저장소에 binary를 커밋했다고 주장하지 않는다.
- 중요 해석: 표의 날짜는 각 ESO가 표준을 채택(adoption)해야 하는 기한이다. 해당 날짜만으로 OJ 인용, harmonised status, presumption of conformity 발생 또는 CRA 제품 적합성 완료를 의미하지 않는다.



### 1.3 CI artifact 및 재현 가능한 provenance

- [기계 판독형 PDF provenance manifest](CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json)에 요청 URL, 최종 URL, fallback 여부, 파일 크기, 페이지 수, raw-byte SHA-256, extracted-text SHA-256을 기록했다.
- GitHub Actions Run #669 (`44052967754`) artifact ID `14315096266`에 PDF 2개, 추출 텍스트 2개, manifest를 업로드했다. ZIP SHA-256 `82e86c3347413bc6f210a7403939141679c34e5ad738822043af87fc5c2290c0`은 GitHub artifact metadata와 다운로드한 ZIP에서 재계산한 값이 일치하며, 내부 PDF raw hashes도 manifest와 재계산 값이 각각 일치한다.
- 최신 Artifact는 2026-11-24 09:14:39 UTC까지 보존된다. 원본 PDF의 영구 보관 위치는 artifact가 만료되기 전 별도로 결정해야 한다.

## 2. C(2026) 5252 Guidance에서 확인한 서보 드라이브 관련 핵심

| 주제 | Guidance locator | 확인 내용 | 서보 드라이브 프로젝트 반영 |
|---|---|---|---|
| 비구속력·해석 범위 | §1.2, para. 8, PDF p.5 | Guidance는 비구속적이며 권위 있는 법 해석은 CJEU에 속한다. 사례는 case-by-case 판단을 대체하지 않는다. | 보고서의 법적 의무와 Commission 해석을 별도 분류하고, guidance만으로 제품 적합성 확정 금지 |
| 하드웨어+소프트웨어 제품 경계 | §2.4, paras. 25–26 인접 | intended purpose 및 reasonably foreseeable use에 비추어 하드웨어의 의도된 기능 수행에 필요한 소프트웨어는 공급 채널/시점이 달라도 제품 범위에 포함될 수 있다. | 드라이브 본체, embedded firmware, 필수 설정·제어 툴, 제품 기능 수행에 필요한 소프트웨어를 공급·기능 구조로 확인 |
| 데이터 연결 | §2.5, paras. 26–28, PDF pp.11–12 | CRA 범위의 data connection은 단순히 전기 신호가 존재하는 것이 아니라, 정의된 scheme으로 의도적으로 인코딩된 디지털 정보가 송신되고 수신 측에서 데이터로 해독될 수 있어야 한다. 단순 on/off trigger 또는 power 신호는 그 자체로 데이터 연결이 아니다. | EtherCAT/PROFINET/EtherNet-IP/Modbus TCP/CANopen/USB/serial 등은 실제 프로토콜·데이터 교환 확인. Analog ±10 V/4–20 mA 및 단순 DI/DO/STO hardwire는 신호가 trigger인지 encoded data인지 회로·수신 동작으로 구분 |
| 복합 시스템 | §2.6, paras. 29–32, PDF pp.11–12 | 복합 시스템도 단일 제품으로 시장에 출시되면 제품 범위가 될 수 있다. 위험평가에서 기존 제약·상호운용성·안전·신뢰성 맥락을 고려하고, 필요 시 보상 통제를 문서화한다. | Drive + motor/encoder + safety controller + PLC/network + engineering software 조합이 단일 공급 제품인지, 별도 제품/부품인지 경계도 작성 |
| 기존 설계 제품 | §2.7, paras. 33–39, PDF pp.13–15 | CRA 적용 전 설계된 제품도 적용일 이후 시장 출시 시 위험평가와 기술문서가 필요하다. 이미 적절한 보안조치가 위험을 다루면 불필요한 redesign을 일률 요구하지 않지만, conformity assessment와 취약점 처리 등 의무는 남는다. | 기존 드라이브 플랫폼은 현재 설계/시험 근거를 위험평가와 연결. 재설계 여부는 risk-based로 결정하며 기존 설계라는 이유로 면제 주장 금지 |
| 수리·예비부품 | §4.1–4.2, Example 39, PDF pp.30–33 | 특정 시스템용으로 명확히 식별되어 공급되는 동일 대체 CPU/PLC spare part 사례는 Article 2(6) 예외 범위에 포함될 수 있다. 일반적 모든 교체품 면제라고 확대하지 않는다. | 드라이브 spare power module/CPU/encoder board 공급 형태, intended product, Article 2(6) 요건을 별도 확인 |
| 실질적 변경 | §4.3, paras. 104–107, PDF pp.34–37 | 변경 규모보다 신규/증가 사이버 위험이 기존 risk assessment에서 고려됐는지가 중요하다. 새 remote control, operating parameter change, fault restart 기능은 목적/위험 프로파일 변경 사례가 될 수 있다. | 펌웨어 기능 추가, 원격 제어, 파라미터 변경, 외부 API/통신 경로 추가는 위험평가 및 substantial modification 영향 분석 |
| 지원 기간 | §5, paras. 126–128, PDF pp.42–43 | Article 13(8)의 5년은 모든 제품에 적용되는 default가 아니다. 제품 특성·의도된 목적·합리적 사용자 기대·관련 EU 법령 등을 바탕으로 기대 사용 기간을 정하며, 5년보다 짧은 사용이 정당화되는 경우 예외가 가능하다. | 산업용 드라이브의 예상 사용기간·현장 수명·부품 공급·펌웨어 지원 및 사용 환경으로 support period 근거화 |
| Core functionality / 등급 | §6/§6.1, paras. 136–144, PDF pp.47–50 | Annex III/IV 분류는 제품의 실제 core functionality를 기준으로 한다. 부가 기능 또는 내부에 포함된 중요/핵심 제품 구성요소만으로 전체 제품 등급이 자동 결정되지 않는다. 기술적 기능을 객관적으로 평가한다. | 서보 드라이브라는 제품명만으로 Annex III/IV class를 부여하지 않는다. 실제 주기능, marketed product boundary, technical capabilities 확인 |
| 위험평가·외부 구성요소 | §7, paras. 163–176, PDF pp.58–61 | 제품 전체 위험평가와 third-party integrated components due diligence는 별개이면서 상호 보완적이다. 제품군 단일 평가 재사용은 architecture, security design, intended purpose, risk profile이 실질적으로 같을 때만 가능하다. 통신 인터페이스·software stack·update mechanism·remote connectivity 차이는 위험평가에 반영한다. | MCU/FPGA/secure element/fieldbus stack/bootloader/engineering tool/third-party library 공급사 증거와 제품 variant 차이를 추적 |
| RDPS | §8.1, paras. 178–190 및 flowchart, PDF pp.63–66 | RDPS 판단은 (1) 원격 처리인지, (2) 그 부재가 제품의 기능 중 하나를 불가능하게 하는지, (3) 소프트웨어가 제조자에 의해 또는 책임하에 개발되었는지의 누적 조건으로 평가한다. RDPS 범위는 해당 software element이며 underlying hardware infrastructure 전체가 자동 포함되는 것은 아니다. | Cloud fleet management/remote diagnostics/remote command/update service별 필수 기능성, 제조자 책임, data flow를 구분. 제3자 cloud는 자동 RDPS가 아니더라도 외부 의존성 위험평가 대상 |
| 산업용 로봇 예시 | §8.3.4, PDF p.73 (산업용 로봇 예시; 별도 paragraph number 없음) | 카메라 데이터를 제조자 설계 원격 서비스에서 처리해 로봇에 명령을 반환하고, 해당 처리가 없으면 기능 수행이 불가능한 예시를 RDPS로 본다. | 드라이브/모션 시스템의 원격 계산·제어가 실제 기능에 필수인지 평가할 때 참고하되 로봇 사례를 드라이브에 자동 전용하지 않는다. |
| Machinery Regulation과 사이버안전 | §9.3.2, paras. 255–257, PDF pp.81–82 | Machinery Regulation의 관련 cybersecurity risks에 대해 유효한 인증/승인 범위 안에서는 CRA 재평가·재입증이 면제될 수 있으나, 해당 인증이 다루지 않은 추가 위험은 제조자 책임으로 남는다. | Machinery Regulation 인증서를 CRA 전체 적합성 대체로 취급하지 않는다. 실제 인증 scope, covered risks, validity, 추가 위험을 대조 |

### 2.1 특히 중요한 데이터 연결 판단

Guidance paras. 26–28은 현재 인터페이스 적용성 매트릭스의 핵심 기준을 제공한다.

- 프로토콜이 정의한 정보 프레임/주소/명령/상태/파라미터를 교환하고 수신 측이 해독하면 data connection으로 볼 강한 근거가 있다.
- 단순 전압 레벨, 전원, relay contact, binary trigger만으로 데이터 연결을 자동 인정하지 않는다.
- DI/DO라도 펄스/비트열을 정의된 방식으로 인코딩하고 receiver가 이를 데이터로 해독하면 단순 trigger와 구별해야 한다.
- STO hardwired signal은 안전 기능 신호라는 명칭만으로 CRA scope 결론을 내리지 않는다. 신호가 정보로 인코딩·해독되는지, 제품의 다른 디지털 연결과 제품 경계를 함께 확인한다.

이는 Commission guidance의 비구속적 해석이며, 최종 적용성은 실제 회로도·통신 사양·제품 설명서·사용 목적을 바탕으로 결정한다.

## 3. C(2026) 7861 Annex I — 표준화 요청 목록 및 기한

Annex I는 ESO(CEN/Cenelec/ETSI)가 작성할 신규 유럽표준의 주제와 adoption deadline을 열거한다. 현재 PDF text extraction에서 41개 항목을 확인했다.

### 3.1 수평 표준

| 항목 | 표준 주제(요약) | ESO adoption deadline |
|---:|---|---|
| 1 | 위험 기반 설계·개발·생산 및 적절한 사이버보안 수준 | 30.11.2026 |
| 2 | 알려진 악용 가능 취약점이 없는 제품 출시 | 30.10.2027 |
| 3 | secure-by-default 구성 | 30.10.2027 |
| 4 | 보안 업데이트로 취약점 해결 | 30.10.2027 |
| 5 | 무단 접근 보호 및 무단 접근 가능성 보고 | 30.10.2027 |
| 6 | 저장·전송·처리 데이터 기밀성 | 30.10.2027 |
| 7 | 데이터·명령·프로그램·구성 무결성 및 변조 보고 | 30.10.2027 |
| 8 | 데이터 최소화 | 30.10.2027 |
| 9 | 필수·기본 기능 가용성 보호 | 30.10.2027 |
| 10 | 다른 기기/네트워크 서비스 가용성에 대한 부정적 영향 최소화 | 30.10.2027 |
| 11 | 공격 표면 제한 | 30.10.2027 |
| 12 | 사고 영향 완화를 위한 exploit mitigation | 30.10.2027 |
| 13 | opt-out mechanism을 포함한 관련 내부 활동 기록/모니터링 | 30.10.2027 |
| 14 | 데이터·설정의 안전하고 쉬운 제거/이전 | 30.10.2027 |
| 15 | 제품 취약점 처리 | 30.11.2026 |

### 3.2 제품 유형별 수직 표준

| 항목 | 표준 주제(요약) | ESO adoption deadline |
|---:|---|---|
| 16 | ID 관리/PAM, 인증 및 접근제어 리더(생체인식 포함) | 31.01.2027 |
| 17 | 독립형·내장형 브라우저 | 31.01.2027 |
| 18 | 비밀번호 관리자 | 31/01/2027 (PDF p.3, 인쇄 페이지 3의 우측 deadline 셀 시각 확인 완료; 설명은 다음 페이지로 이어짐) |
| 19 | 악성코드 검색·제거·격리 소프트웨어 | 31.01.2027 |
| 20 | VPN 기능 제품 | 31.01.2027 |
| 21 | 네트워크 관리 시스템 | 31.01.2027 |
| 22 | SIEM 시스템 | 31.01.2027 |
| 23 | Boot manager | 31.01.2027 |
| 24 | PKI 및 디지털 인증서 발급 소프트웨어 | 31.01.2027 |
| 25 | 물리·가상 네트워크 인터페이스 | 31.01.2027 |
| 26 | 운영체제 | 31.01.2027 |
| 27 | 인터넷 연결용 라우터·모뎀·스위치 | 31.01.2027 |
| 28 | 보안 기능을 가진 마이크로프로세서 | 31.01.2027 |
| 29 | 보안 기능을 가진 마이크로컨트롤러 | 31.01.2027 |
| 30 | 보안 기능을 가진 ASIC/FPGA | 31.01.2027 |
| 31 | Smart-home general-purpose virtual assistants | 31.01.2027 |
| 32 | 보안 기능을 가진 스마트홈 제품(스마트락·카메라·베이비 모니터·경보) | 31.01.2027 |
| 33 | 사회적 상호작용/위치 추적 기능이 있는 인터넷 연결 장난감 | 31.01.2027 |
| 34 | 특정 건강 모니터링/아동용 웨어러블 | 31.01.2027 |
| 35 | 가상화 OS 실행을 지원하는 hypervisor/container runtime | 31.01.2027 |
| 36 | 방화벽·IDS/IPS(산업용 포함) | 31.01.2027 |
| 37 | 변조 방지 마이크로프로세서 | 31.01.2027 |
| 38 | 변조 방지 마이크로컨트롤러 | 31.01.2027 |
| 39 | Hardware Devices with Security Boxes | 31.01.2027 |
| 40 | Smart-meter gateway 및 고급 보안 목적 장치 | 31.01.2027 |
| 41 | Smartcard 및 secure element 유사 장치 | 31.01.2027 |

**추출 품질 주의:** 항목 18의 날짜 셀은 PDF text extraction에서 행 분리로 누락됐으나, PDF p.3(인쇄 페이지 3) 원본 페이지 이미지의 우측 deadline 셀에서 `31/01/2027`을 시각적으로 확인했다. 행 설명은 페이지 경계에서 다음 페이지로 이어진다. 날짜는 이제 확인 상태다.

### 3.3 서보 드라이브에 대한 잠정적 관련성

직접적으로 검토 가치가 높은 항목은 다음과 같다.

- 수평: 1, 2–7, 9–13, 15 — risk-based design, known vulnerabilities, secure defaults, updates, access control, confidentiality/integrity, availability, attack surface, exploit mitigation, logging, vulnerability handling.
- 수직 구성요소/인터페이스: 25 (physical/virtual network interfaces), 28–30 (security-related MCU/ASIC/FPGA), 36 (industrial firewalls/IDS/IPS), 37–39 (tamper-resistant processors/MCUs/security-box devices), 41 (secure elements).
- 이 목록은 해당 부품/기능을 포함한다는 이유만으로 드라이브 전체가 해당 수직 제품 유형에 자동 분류된다는 뜻이 아니다.
- 표준이 실제로 채택·인용되기 전에는 해당 표준이 이미 harmonised standard이거나 presumption of conformity를 제공한다고 표현하지 않는다.
- 표준 초안 채택 기한과 CRA의 제품 의무 적용일(주요 의무 2027-12-11)은 별도 타임라인으로 관리한다.

## 4. 기존 CRA 산출물에 반영할 수정·추가 사항

1. **인터페이스 적용성 매트릭스:** Guidance §2.5 paras. 26–28을 각 디지털/아날로그/DI-DO/STO 행의 핵심 판단 근거로 명시한다. "전기 신호"와 "인코딩된 디지털 데이터"를 분리한다.
2. **제품 경계:** §2.4, §2.6을 이용해 drive + embedded software + 필수 engineering tool + 외부 controller/cloud service의 공급·기능 관계를 확인한다.
3. **제품 분류:** §6의 core functionality 원칙을 반영해 servo drive 명칭이나 내장 MCU/secure element만으로 Annex III/IV 분류를 부여하지 않는다.
4. **위험평가/통제 매트릭스:** §7을 이용해 third-party component due diligence, 제품군 공통 평가의 허용 조건, variant 차이(통신·update·remote connectivity)를 연결한다.
5. **RDPS:** §8.1의 누적 3요건과 §8.3.4 industrial robot example을 기준으로 remote diagnostics, remote parameterization, remote command, cloud analytics, update services를 기능별 평가한다.
6. **지원기간:** §5의 기대 사용기간 기준을 반영해 산업용 드라이브의 5년을 자동 default로 설정하지 않고 예상 사용기간 근거를 기록한다.
7. **표준 로드맵:** C(2026) 7861 Annex I 항목 1–15 및 25, 28–30, 36–41을 관련 SEC control과 교차 연결하되, adoption deadline과 harmonised status를 구분한다.

## 5. 확인되지 않은 사항과 후속 검증

- C(2026) 5252는 Run #669에서 Commission-hosted primary URL이 PDF로 확인되지 않아 allowlisted ANFR mirror fallback을 사용했다. Mirror binary hash는 확인됐지만 Commission-hosted 원본 URL과 byte identity는 미확인이다.
- C(2026) 7861 Annex I PDF는 Commission document-register 원본 bytes 및 SHA-256 확인 완료. C(2026) 7861 본문 decision 및 Annex I 외 첨부가 있는지 document register 전체 항목은 추가 확인한다.
- M/606 Annex I item 18 deadline `31/01/2027`은 PDF p.3(인쇄 페이지 EN 2) 원본 이미지로 시각 확인 완료. 행의 설명은 EN 3으로 이어지지만 오른쪽 기한 셀은 EN 2에 있다.
- C(2026) 5252의 서보 드라이브 직접 사례는 없다. Industrial robot 사례는 RDPS의 원리 예시로만 사용한다.
- 제품별 적용성/분류를 확정하려면 실제 모델, 회로도, MCU/FPGA, 통신 프로토콜, remote service architecture, firmware/update policy, EU supply chain facts가 필요하다.
- Guidance는 비구속적이다. CRA Regulation (EU) 2024/2847 및 Official Journal 정본과 충돌할 경우 법령 정본을 우선하고, 불확실한 해석은 법률 검토 대상으로 남긴다.

## 6. 출처

1. European Commission, C(2026) 5252 publication page (27.07.2026): https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
2. European Commission, C(2026) 5252 Annex download URL: https://ec.europa.eu/newsroom/dae/redirection/document/131456
3. French National Frequency Agency (ANFR) mirror of C(2026) 5252 Annex: https://www.anfr.fr/fileadmin/CRA/Commission_guidance_on_the_application_of_Regulation__EU__20242847__Cyber_Resilience_Act_.pdf
4. European Commission document register, C(2026) 7861: https://ec.europa.eu/transparency/documents-register/detail?ref=C(2026)7861&lang=en
5. European Commission, C(2026) 7861 Annex PDF: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401
6. CRA primary law: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng

---

*감사 상태: 최종 Run #702에서 148 passed / 1 xfailed, PDF 2개 취득·해시·artifact readback, 9개 공식 HTML source canary, Article 13(8) locator/quote 검증 통과. M/606 Commission PDF 및 Guidance ANFR mirror raw-byte SHA-256, item 18 시각 확인, G-001~G-013 claim register 및 matrix 연결 완료. Guidance Commission-hosted original byte identity와 실제 서보 드라이브 제품별 증거 연결은 미완료.*


## 7. 최신 공식 관보 원문 재기준화 — C/2026/6013 (2026-11-18)

### 7.1 출처 상태 변경

2026-11-18 재확인 결과, Commission의 2026-07-27 게시 페이지는 Guidance를 C(2026) 5252로 표시하지만, 공식 관보에는 같은 CRA Guidance가 **Communication C/2026/6013**로 2026-11-17 게재되었다. 공식 관보의 CELEX 식별자는 `52026XC06013`이다.

- Commission 2026-07-27 게시 페이지: https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation
- EUR-Lex Official Journal PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- EUR-Lex ELI: https://eur-lex.europa.eu/eli/C/2026/6013/oj/eng
- 기존 Commission PDF 다운로드 URL `https://ec.europa.eu/newsroom/dae/redirection/document/131456`는 2026-11-18 현재 HTTP 404를 반환했다.
- 따라서 C(2026) 5252는 2026-07-27 승인/게시 문서 참조로 역사 기록에 남기되, 현재 보고서의 공식 관보 인용과 page locator 기준은 C/2026/6013으로 전환한다.
- 기존 ANFR mirror는 삭제·재명명하지 않는다. 기존 bytes의 SHA는 mirror-only provenance로 유지한다.

### 7.2 EUR-Lex OJ PDF 원본 무결성

- Source ID: `CRA-GUIDANCE-OJ-2026-6013`
- 문서: Commission Communication C/2026/6013, OJ C, 17.11.2026.
- 취득 URL: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026XC06013
- 최종 URL: 동일, EUR-Lex 공식 호스트.
- fallback: false.
- PDF binary: 2,709,282 bytes; 61 pages.
- Raw-byte SHA-256: `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`.
- Extracted text: 255,974 chars.
- Extracted-text SHA-256: `384724af44e399cb997771e9e65ea4a5fe1dd264131d0754921bd691dd1f7720`.
- Identity markers: `C/2026/6013`, `Cyber Resilience Act`, `remote data processing`.
- CI: Run #844 (ID `44204376214`), exact head `0957ad4b3e85a8bb245c6b3adc62b7daec1a09de`, success; 156 passed, 1 xfailed; compile, traceability and three-PDF live canary passed.
- Artifact ID `14381529964`, digest `sha256:a55dba42db13ed7c350c39e62a158bf512686b6892857870056212e8b3a7a6ae`, retained until 2026-11-25 00:02:11 UTC.

### 7.3 C(2026) 5252 mirror와 OJ C/2026/6013 비교

| 비교 항목 | C(2026) 5252 ANFR mirror | C/2026/6013 EUR-Lex OJ |
|---|---:|---:|
| Raw bytes | 1,190,726 | 2,709,282 |
| Pages | 84 | 61 |
| Raw SHA-256 | `fe209c250e3d1f7599e42826d91963666951332927edcf511a2e79fe8d2f8234` | `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2` |
| Extracted chars | 250,162 | 255,974 |
| Extracted-text SHA-256 | `147f6649b5089cbc4d55c7af77abdcdbd04263b116960812c579fd25acda7425` | `384724af44e399cb997771e9e65ea4a5fe1dd264131d0754921bd691dd1f7720` |

- Numbered paragraph identifiers 1–257 were all found in both extracted documents.
- After whitespace normalization, case-folding, punctuation/footnote-marker normalization and word tokenization, the common token multiset was 36,467 tokens: 99.50% of mirror tokens and 99.66% of OJ tokens.
- This is strong evidence of substantial textual overlap, but **not** byte identity or exact extracted-text equality. Pagination, OJ headers/footers, footnote formatting and some extraction differences exist. Do not describe the two PDFs as byte-identical or word-for-word identical.
- The OJ document is the primary citation source. The mirror remains an independently hashed historical copy. Any substantive difference found in a claim-relevant paragraph must be resolved against the OJ wording.

### 7.4 Guidance claim register — OJ page locator migration

All 13 Guidance claims retain their claim IDs and cross-matrix links, but their source ID is now `CRA-GUIDANCE-OJ-2026-6013`. PDF page references are migrated to OJ pagination:

| Claim | Locator | OJ PDF pages |
|---|---|---:|
| G-001 | §2.4 paras. 25–26 | 7–8 |
| G-002 | §2.5 paras. 26–28 | 8 |
| G-003 | §2.6 paras. 29–32 | 8–9 |
| G-004 | §2.7 paras. 33–39 | 9–10 |
| G-005 | §4.3 paras. 104–107 | 24–25 |
| G-006 | §5 paras. 126–128 | 30 |
| G-007 | §6/§6.1 paras. 136–144 | 32–35 |
| G-008 | §7.1–§7.3 paras. 163–173 | 42–43 |
| G-009 | §7.4 paras. 174–177 | 44 |
| G-010 | §8.1 paras. 178–190 | 44–46 |
| G-011 | §8.3.4 industrial robot example | 53 |
| G-012 | §9.3.2 paras. 255–257 | 61 |
| G-013 | §4.1–§4.2 Example 39 | 24 |

Machine-readable details are in `reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json`; claim rows are in `reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv`.

### 7.5 Remaining verification

1. Perform a claim-by-claim substantive redline for G-001–G-013 against OJ C/2026/6013, prioritising scope/data connection, support period, core functionality, RDPS and reporting.
2. Reconfirm all page locators in the OJ pagination from the PDF page images where tables/figures or page breaks affect extraction.
3. Ensure integrated report, interface matrix, requirements matrix and SEC controls cite the OJ source ID and distinguish binding CRA law from non-binding Commission guidance.
4. Keep C(2026) 5252 mirror provenance and OJ C/2026/6013 provenance separate; never overwrite one hash with the other.

## 7.6 최종 PR head 재검증 — Run #854 (2026-11-18)

- PR #52 final code/document head at this checkpoint: `0ab0fc4d9b217a4994fd6e7a1b32607c854bb693`.
- GitHub Actions Run #854 (ID `44205498935`): **success**.
- Exact source blob identity: success; compileall: success; CRA cross-matrix traceability: success; full pytest: **158 passed, 1 xfailed**.
- Live PDF canary: three sources fetched and SHA-256 verified. C(2026) 5252 mirror used fallback=True; OJ C/2026/6013 retrieved directly from EUR-Lex with fallback=False; M/606 C(2026) 7861 retrieved directly from Commission register with fallback=False.
- OJ C/2026/6013 hash remained `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`; 61 pages.
- Artifact ID `14382388555`, digest `sha256:9e8dc7f1c1d90015b7738263155ca9d6b1170aaea75ea6bd17350aeff7d36af7`, expires 2026-11-25 00:09:59 UTC.
- The earlier Run #851 failure was a traceability-validator assumption requiring the explicit ANFR mirror-scope phrase in every claim row. The phrase is now retained as historical mirror-only provenance, while the validator also requires the OJ source and rejects OJ fallback. Run #854 passed this updated gate.

## 7.7 최종 PR head 확인 — Run #857 (2026-11-18)
- Tested head: `152fe0bfe00c16ab32f7cc030efcde3258b73525`; GitHub Actions Run #857 (ID `44205723336`) success.
- Source blob identity, compileall, CRA traceability, full pytest (158 passed, 1 xfailed), three-PDF acquisition, artifact upload and live official CRA HTML canary all passed.
- OJ C/2026/6013 remained EUR-Lex primary, fallback=False, 2,709,282 bytes, 61 pages, SHA-256 `40ca76caeb0108f5b97c8f373a95f590b453fe92bd45a483addf3326e48c1dc2`.
- Artifact #14383167818, digest `sha256:a2f05428d57897a20a485cabaab17cbb976dcb91f6e5628ece0953ddfe22140d`, expires 2026-11-25 00:11:31 UTC.
- Run #857 validates the PR head before this metadata append; a new exact-head CI is required after the provenance record update.


## 8. Claim-by-claim substantive redline against OJ C/2026/6013 — 2026-11-18

### 8.1 Method and outcome

- Reviewed all 13 rows G-001–G-013 in `reports/CRA_GUIDANCE_CLAIM_REGISTER_2026-11-17.csv` against the EUR-Lex OJ PDF text and the relevant rendered page images.
- Visual page-image checks: OJ pages 7–10, 24–25, 30, 32–35, 42–46, 53 and 61 (18 pages).
- All 13 claims remain interpretations of non-binding Commission Guidance, not independent legal requirements. Binding legal requirements remain those in Regulation (EU) 2024/2847 and other applicable legislation.
- Result: 9 claims confirmed without substantive change; G-001 locator corrected; G-003, G-008 and G-013 paraphrases refined; G-004 expanded to make continuing conformity/CE/vulnerability obligations explicit.
- No CRA requirement IDs, interface IDs or SEC control IDs were deleted or reclassified as completed. The source locator corrections do not establish product-specific applicability.

### 8.2 Detailed redline register

| Claim | OJ locator | Result | Substantive finding / action |
|---|---|---|---|
| G-001 | §2.4 para. 25, p.7 | Confirmed; locator corrected | Paragraph 25 says software belongs to the product where it is necessary for intended functions in light of intended purpose and reasonably foreseeable use, regardless of how/when delivered. The old locator incorrectly included para.26, which begins §2.5 Data connection. Corrected to para.25 only. |
| G-002 | §2.5 paras. 26–28, p.8 | Confirmed | Paras. 26–28 anchor scope to capacity to exchange digital information. Para.28 expressly distinguishes deliberately encoded/decoded information from signals used only to trigger or power a function. The paraphrase is supported. |
| G-003 | §2.6 paras. 29–32, pp.8–9 | Wording narrowed | These paragraphs address complex systems placed on the market as one product, legacy components, established architectures, interoperability constraints and the risk-based approach. They do not, within this locator, expressly support the previous broad phrase “interfaces and product-level mitigations”. Removed that overreach and tied the paraphrase to the actual text. |
| G-004 | §2.7 paras. 33–39, pp.9–10 | Expanded | Pre-application designs placed on the market after 11 December 2027 still require risk assessment and applicable conformity assessment, EU declaration of conformity and CE marking. Existing effective measures can be relied upon where they address the risks; no automatic redesign/new features. Vulnerability handling and other CRA obligations remain. |
| G-005 | §4.3 paras. 104–107, pp.24–25 | Confirmed | Substantial modification turns on new/increased cybersecurity risk not considered in the risk assessment. Para.107 expressly says the scale or complexity of the change is not decisive; even a limited feature may materially alter the risk profile. |
| G-006 | §5 paras. 126–128, p.30 | Confirmed | Five years is a safeguard, not a universal default; support period follows expected use time and Article 13(8) criteria. Substantially modified software versions may require a new declared support period. |
| G-007 | §6 and §6.1 paras. 136–144, pp.32–35 | Confirmed | Core functionality is the product’s main features/capabilities needed for intended purpose. Ancillary functionality does not automatically change classification; mere integration of an important/critical component does not itself make the host product important/critical. |
| G-008 | §7.1–§7.3 paras. 163–173, pp.42–43 | Wording refined | The OJ text distinguishes (i) external risks/dependencies, which must be assessed and mitigated through product-level measures where relevant, from (ii) integrated third-party components that form part of the product, for which risk-based due diligence is required. The paraphrase now states this distinction explicitly. |
| G-009 | §7.4 paras. 174–177, p.44 | Confirmed | Reuse across product families is conditional on shared architecture, security-relevant design, intended purpose and exposure to the same risks. Security-relevant differences in communication interfaces, software stacks, update mechanisms or remote connectivity must be reflected. |
| G-010 | §8.1 paras. 178–190, pp.44–46 | Confirmed | RDPS is software-based processing at a distance, designed/developed by or under manufacturer responsibility, whose absence prevents one product function. Paragraph 184 lists the three elements; paragraphs 188–190 clarify cumulative assessment and function scope. |
| G-011 | §8.3.4 Industrial robot, p.53 | Confirmed | The example explicitly treats manufacturer-developed cloud software that processes camera feeds and returns robot commands as RDPS where its absence prevents a robot function. Third-party IaaS infrastructure is documented and considered in risk assessment; due diligence when selecting the IaaS provider is also expected. |
| G-012 | §9.3.2 paras. 255–257, p.61 | Confirmed | Machinery Regulation certificates/approval decisions remain valid for the cybersecurity risks they cover, subject to their validity and the 11 June 2028 outer limit. Additional risks not covered by the certificate remain the manufacturer’s responsibility under the CRA. |
| G-013 | §4.2 Examples 37–39, p.24 | Wording refined; locator corrected | Example 37 shows a replacement chip with different cryptographic implementation/secure boot is not identical and is not exempt. Example 38 shows a different chipset can still be considered identical where cybersecurity-relevant characteristics are unchanged. Example 39 applies Article 2(6) to an identical replacement CPU or whole PLC supplied as a spare part through after-sales service for a clearly identified existing industrial automation system. The claim now states the identity and service-channel conditions rather than implying a generic replacement-part exemption. |

### 8.3 Page-image and locator verification

The rendered OJ page images were checked for the claim-bearing paragraphs/examples and their printed page numbers. This includes:
- p.7 para.25; p.8 paras.26–32; pp.9–10 paras.33–39;
- pp.24–25 Examples 37–39 and paras.104–107;
- p.30 paras.126–128;
- pp.32–35 paras.136–144 and the core-functionality figures;
- pp.42–43 paras.163–173;
- pp.44–46 paras.174–190;
- p.53 industrial robot example; and
- p.61 paras.255–257.

### 8.4 Residual boundaries

- Commission Guidance is non-binding. Where a paraphrase appears to extend beyond the Regulation, the Regulation text controls.
- The redline validates the 13 selected claims and locators; it is not a full legal opinion or exhaustive review of every sentence in the 61-page Guidance.
- This work does not determine whether a specific servo drive is in scope, which Annex category applies, or which conformity route is required. Manufacturer/model evidence remains necessary.
- The product-specific Unknown gates remain unchanged.


## 9. M/606 C(2026) 7861 — 최신 Annex, ESO 진행상황 및 OJ harmonised status 재검증 (2026-11-18)

### 9.1 공식 Commission Annex 원본

- 문서: Commission Implementing Decision C(2026) 7861 final, Annex, Brussels 10.11.2026; amends Implementing Decision C(2025) 618 (M/606).
- Official Commission document-register Annex API: https://ec.europa.eu/transparency/documents-register/api/files/C%282026%297861_1/de00000001090401
- PDF: 151,267 bytes; 6 pages; SHA-256 `262b09596cb5cbe7d72a2c7789fb2512ee00db7f69082e7def2c8181b0f63276`.
- Extracted text: 8,058 chars; SHA-256 `06409ee840550a4e602aa30b4f77a9eaf90a44735f820ce2b1239cccec6a54dd`.
- CI artifact Run #870 readback confirmed the same bytes/hash; direct Commission register source, fallback=False.
- All six PDF pages were visually inspected. The annex is headed “List of new European Standards to be drafted”; it is a standardisation request, not a published harmonised standard.

### 9.2 Correct ESO adoption deadlines — all 41 items

The Annex column is expressly “Deadline for the adoption by the ESOs”. The validated deadline groups are:
- Item 1: 30/11/2026.
- Items 2–14: 30/10/2027.
- Item 15: 30/11/2026.
- Items 16–41: 31/01/2027.

These are CEN/CENELEC/ETSI adoption deadlines, not manufacturer CRA compliance deadlines, CRA application dates or OJ publication dates.

#### Item 18 page-locator correction

A full visual recheck of the six-page Annex found that the item 18 row crosses a page break:
- PDF page 3 is printed page EN 2. The right-hand deadline cell `31/01/2027` is visible on EN 2.
- The description “requirements for password managers” continues onto printed page EN 3 (PDF page 4).
- The previous crosswalk/validator incorrectly attributed the deadline cell to EN 3 because the extracted text emitted the continuation after the page break.
- Correct locator: `EN 2–3 (item description continues on EN 3; deadline cell on EN 2, visually confirmed)`.
- `reports/CRA_PDF_SOURCE_PROVENANCE_2026-11-17.json` visual_verification now records zero-based PDF page index 2 and printed page number 2; the validator and negative test are corrected accordingly.

Other split rows were also rechecked:
- Item 8: description continues EN 1–2; deadline cell on EN 1.
- Item 31: description continues EN 3–4; deadline cell on EN 3.
- Item 40: description continues EN 4–5; deadline cell on EN 4.
The 41-row crosswalk page locators have been made row-specific to the printed pages.

### 9.3 Commission confirmation and current harmonised-standard status

- Commission CRA standardisation page (last updated 12.11.2026): https://digital-strategy.ec.europa.eu/en/policies/cra-standardisation
  - It states that M/606 contains 41 standards.
  - It confirms that on 10.11.2026 the request was amended to extend the deadline for all vertical standards and some horizontal standards by three months.
  - This is consistent with the amended Annex deadline groups above.
- Commission harmonised-standards index: https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards_en
  - The Commission explains that harmonised-standard references must be published in the OJ and that the index provides the latest OJ reference lists.
  - As checked on 18.11.2026, the index contains no CRA-specific entry (the Digital Single Market list includes AI and DPP, but not CRA). Exact EUR-Lex searches for `EN 40000-1-2`, `EN 40000-1-3` and `EN 304 617` did not surface a CRA OJ citation.
  - Conclusion is deliberately bounded: no CRA-specific harmonised-standard OJ reference was identified in the Commission index/EUR-Lex search as of this check. Do not claim a presumption of conformity from an M/606 request, draft prEN, ESO work item or publication forecast.
- This is a source-check conclusion, not a claim that the Commission can never publish a reference later. Recheck the index and OJ before any conformity assessment or market-placement decision.

### 9.4 Latest publicly linked ESO work-programme snapshot

- STAN4CR shared CEN/CENELEC/ETSI work programme, “Second Joint ESO semestrial report M/606”, Version V2.0, dated 03.06.2026, 4 pages: https://www.stan4cra.eu/_files/ugd/d3d362_20e5bfebe8bf47b1998caf05c5799333.pdf
- The Commission CRA standardisation page links to STAN4CR as the ESO activity portal. The report is an ESO progress snapshot, not a legal act or OJ citation.
- Selected June 2026 stage/forecast observations:
  - Item 1 (prEN 40000-1-2): ENQ closed 01.01.2026; preparation for FV in 08/2026; publication forecast 30.09.2026.
  - Items 2–14 (prEN 40000-1-4): Early Draft; publication forecast 30.10.2027.
  - Item 15 (prEN 40000-1-3): ENQ closed 05.03.2026; preparation for FV in 10/2026; publication forecast 30.11.2026.
  - Items 28–29: ENQ passed 10.04.2026; preparation for FV; publication forecast 30.11.2026.
  - Items 37–38: ENQ passed 10.04.2026; preparation for FV; publication forecast 15.11.2026.
  - Item 39: submitted to ENQ 21.05.2026; publication forecast 15.02.2027.
  - Item 40: mature draft; publication forecast 30.10.2026.
  - Item 41a/41b: ENQ passed 10.04.2026 / 09.04.2026; preparation for FV; publication forecast 15.11.2026 / 30.11.2026.
- Important distinction: the ESO report column is “Publication forecast”; the Commission Annex column is “Deadline for adoption by the ESOs”. These are different milestones. A publication forecast later than an adoption deadline is not, by itself, proof that the ESO missed the adoption deadline. The June snapshot also predates the 10 November amendment. Treat it as progress context only, not a current compliance status.
- The publicly linked V2.0 report is the latest ESO status document located in this check; no later public M/606 progress report was found on the STAN4CR site. It is image-based (the PDF text layer yields only 3 characters), so it is deliberately excluded from the text-layer PDF CI canary. Do not treat it as a machine-verified evidence artifact until its downloaded raw-byte hash, page count and visual/OCR review are separately recorded.

### 9.5 Servo-drive relevance boundaries

- Horizontal items 1–15 remain relevant to product-level risk management, vulnerability handling, secure configuration, access control, data protection, integrity, availability and updates as determined by actual product evidence.
- Item 25 (physical/virtual network interfaces) is conditional on the marketed product itself being a network-interface product; Ethernet/fieldbus ports alone do not automatically classify the complete drive.
- Items 28–30 and 37–39 may be component due-diligence topics where security-capable processors/MCUs/ASICs/FPGAs or tamper-resistant components/security boxes are integrated; component presence does not automatically classify the whole drive.
- Item 36 applies vertically only if the product itself is an industrial firewall/IDS/IPS, not merely because the drive has network filtering or hardening.
- Item 41 is conditional for smartcards/secure elements; an integrated secure element may be a supplier-evidence issue without making the whole drive a smartcard product.
- Existing conditional mappings remain unchanged unless exact product BOM, part numbers, datasheets and intended-purpose evidence justify a model-specific change.

### 9.6 Required follow-up

1. Retain the June ESO report as a separate supplementary source with its own raw-byte hash and extraction metadata.
2. Keep M/606 adoption dates, ESO publication forecasts and OJ harmonised-standard citations as three separate fields in the standardisation status tracker.
3. Recheck the Commission OJ index at each standards update; only add a presumption-of-conformity claim after the exact standard reference is published in the OJ and its scope matches the product.


### 9.7 CEN/CENELEC 발행 상태 업데이트 (2026-11-18)

이전 OJ 조회 결론(확인 범위에서 CRA OJ 인용 미식별)은 유지하되, 이를 “CRA 관련 EN이 하나도 발행되지 않았다”는 뜻으로 해석하지 않는다. CEN 공식 레코드에서 EN 40000-1-1:2026은 Published, DAV 2026-11-18로 확인됐으나 OJ citation 필드는 No citation expected다. EN 40000-1-2는 2026-11-02 ratification 및 No citation expected가 tracker/2차 자료에서 확인됐지만 공식 개별 레코드 readback은 HTTP 500으로 미완료다. FprEN 40000-1-3은 Under Approval / Citation expected. CENELEC prEN 50770-1~6은 모두 Committee stage / Citation expected이며 아직 발행된 표준이 아니다.

정확한 차이는 **ESO Published ≠ OJ-cited harmonised standard**다. Article 27(1) 추정 적합성은 정확한 참조가 OJ에 실제 공표되고 그 범위가 제품에 적용될 때에만 주장한다. 상세: [CEN/CENELEC 공식 상태 감사](CRA_CEN_CENELEC_EN40000_OT50770_STATUS_2026-11-18.md).
