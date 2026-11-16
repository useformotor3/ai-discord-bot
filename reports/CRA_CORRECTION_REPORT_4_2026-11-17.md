# CRA 보고서 #4 정정 및 기술 근거 감사

- 감사 대상 원본: `research_archive/2026-11-17_082040817286_b5f20b1f.md`
- 원본 보고서 날짜: 2026-11-17 08:20:40 KST
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 검토 기준: 2026-11-17에 확인한 공식 CRA 원문, NIST 공식 간행물, IEC 공식 카탈로그 및 ISA 공개 표준 발췌본.

## 1. 판정 요약

| 원본 주장/인용 | 감사 결과 | 정정 |
|---|---|---|
| CRA Annex I Part I (2)(i)가 기밀 데이터 삭제를 규정 | **잘못된 조항 인용 및 원문 불일치** | 삭제 기능은 Annex I Part I (2)(m). (2)(i)는 제품/연결 장치가 다른 장치 또는 네트워크의 서비스 가용성에 미치는 부정적 영향을 최소화하는 항목 |
| CRA가 하드웨어·펌웨어 레벨의 특정 삭제 메커니즘을 의무화 | **법령 문언을 넘어선 단정** | (2)(m)는 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 삭제할 수 있는 가능성을 제공하도록 규정. 특정 기술(CE, 물리적 덮어쓰기, RoT)을 일률적으로 지정하지 않음 |
| IEC 62443-4-2 CR 4.1 = 정보 보호/키 파기 | **통제 번호·명칭 혼동** | CR 4.1은 Information confidentiality, CR 4.2는 Information persistence, CR 4.3은 Use of cryptography |
| NIST SP 800-88 Rev.1을 현행 기준으로 인용 | **폐지·대체된 판본** | Rev.1은 2025-09-26 철회됐고 Rev.2로 대체됨 |
| Flash에 multi-pass overwrite 권고 | **기술적으로 부적절한 일반화** | Rev.2는 SSD overprovisioning/wear leveling 때문에 host overwrite로 모든 이전 데이터를 지우기 어렵다고 설명하며, 과거식 다중 패스는 피해야 할 수 있다고 안내. 저장매체별 적합한 purge/sanitize 방법을 선택해야 함 |

## 2. CRA 법령 조항 대조

공식 EUR-Lex 원문 Regulation (EU) 2024/2847 Annex I Part I (2):

- (i): 제품 자체 또는 연결 장치가 다른 장치/네트워크가 제공하는 서비스 가용성에 미치는 부정적 영향을 최소화.
- (m): 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 삭제할 수 있는 가능성을 제공하고, 해당 데이터를 다른 제품/시스템으로 이전할 수 있는 경우 안전한 방식으로 이전되도록 보장.

따라서 원본 보고서의 Annex I (2)(i) 인용은 잘못됐다. 삭제 관련 주장은 (2)(m)에 연결해야 한다. Annex II point 8(d)는 제품의 안전한 폐기(secure decommissioning)와 사용자 데이터의 안전한 삭제 방법에 대한 설명서/정보를 요구하는 보완 근거다.

다만 법령은 삭제 결과·사용자 기능을 요구하는 것이지, 모든 제품에 특정 하드웨어 보안 모듈, 암호화 키 삭제, 다중 덮어쓰기 방식을 강제한다고 단정할 수 없다. 구현 방식은 저장매체 종류, 데이터 민감도, 위협모델, 제품 구조와 검증 가능성을 바탕으로 선택해야 한다.

## 3. IEC 62443-4-2 대조

IEC 공식 카탈로그는 IEC 62443-4-2:2019가 IACS 구성요소의 기술 보안 요구사항(CR)을 다루며 데이터 기밀성(Data Confidentiality)을 포함한 7개 foundational requirements와 연계된다고 설명한다.

공개된 ANSI/ISA-62443-4-2 발췌본의 FR 4 절은 다음과 같이 구분한다.

- CR 4.1 — Information confidentiality: 명시적 읽기 권한이 지원되는 저장 정보의 기밀성 보호 기능 및 전송 중 정보의 기밀성 보호 지원.
- CR 4.2 — Information persistence: active service에서 해제되거나 decommission될 구성요소에서 명시적 읽기 권한이 지원되는 정보를 지울 수 있는 기능.
- CR 4.2 RE(2) — Erase verification: 삭제가 수행됐음을 검증할 수 있는 기능. 발췌본의 보안 수준 표에서는 SL-C(DC, component) 3 및 4에 해당 enhancement가 표시된다.
- CR 4.3 — Use of cryptography: 암호기술 사용 요구. 보충 설명은 키 수립·관리, 키 파기·분배·백업 등을 다룬다.

따라서 원본 보고서는 삭제와 직접 관련된 CR 4.2를 놓치고 CR 4.1에 잘못 연결했다. 키 관리/암호기술 논의는 CR 4.3과 연계하되, CR 4.3 자체를 삭제 기능의 대체 조항으로 취급하지 않는다.

## 4. NIST SP 800-88 판본 및 Flash 삭제 방식

NIST는 SP 800-88 Rev.2를 2025-09-26 발행했고, Rev.1은 같은 날 철회·대체됐다. 따라서 2026-11-17 기준 참고 문헌은 Rev.2로 갱신해야 한다.

NIST Rev.2가 강조하는 사항:
- 매체 유형 및 데이터 민감도에 적합한 sanitization 방법을 선택.
- Cryptographic Erase는 암호화된 매체에서 유용한 방법 중 하나지만, 모든 제품에 자동으로 적용되는 만능 해법은 아니다. 암호화 적용 시점, 키 관리, 키 파기 신뢰성 등 전제조건을 검증해야 한다.
- SSD의 spare area/overprovisioning 및 wear leveling 때문에 일반 host interface로 접근 가능한 영역만 덮어써서는 과거 데이터 전체를 제거하지 못할 수 있다.
- 과거 HDD에서 쓰이던 multi-pass overwrite 패턴은 현대 SSD에 적합하지 않을 수 있으며, 수명만 저하시키고 기밀성 보장은 개선하지 못할 수 있다.
- 전용 sanitize 명령을 쓰는 경우 제조사 구현의 신뢰성과 보증 근거가 중요하다.

따라서 원본의 “Multi-pass Overwrite (Flash Sanitization)”는 권고안에서 제거한다. 실제 제품 설계는 NAND/EEPROM/NVRAM/배터리 백업 메모리/외장 저장매체별로 삭제 범위와 기술적 한계를 분석해야 한다.

## 5. 수정된 권고 문안

> CRA 대응 관점에서 제품은 사용자가 모든 데이터와 설정을 안전하고 쉽게 영구 삭제할 수 있는 기능을 제공해야 하며, 데이터 이전이 가능한 경우 안전한 이전 절차를 제공해야 한다(Annex I Part I (2)(m)). 안전한 제품 폐기 및 사용자 데이터 삭제 절차는 사용자 정보에 포함해야 한다(Annex II point 8(d)). 산업용 제어 구성요소의 폐기 시 정보 잔존 방지는 IEC 62443-4-2 CR 4.2(Information persistence)와 연계해 검토할 수 있다. 실제 sanitization 방식은 저장매체와 데이터 민감도에 따라 선택하고, 암호화 삭제(CE), 제조사 sanitize 명령, 물리적 파기 등 후보의 전제조건과 검증 방법을 평가한다. NIST 참고 기준은 현행 SP 800-88 Rev.2를 사용한다. 이 법령·표준의 문언만으로 모든 제품에 특정 하드웨어 구조나 단일 삭제 알고리즘이 의무라고 단정하지 않는다.

## 6. 제품 설계/시험 추적에 필요한 후속 항목

1. 데이터 자산 목록: 사용자 설정, 네트워크 자격 증명, 인증서/개인키, 로그, 펌웨어/설정 백업, 제조사 IP, 서비스 도구 저장 데이터.
2. 저장 위치 목록: 내부 Flash/NVM, 외부 EEPROM, removable media, battery-backed RAM, service/debug interface, cloud/engineering tool 복제본.
3. 삭제 시나리오: factory reset, ownership transfer, decommissioning, RMA/repair, component replacement.
4. 삭제 검증: 대상 데이터 범위, 비휘발성 저장영역 접근 경로, wear leveling/overprovisioning, 백업·복제본, 잔존 키·인증서, 삭제 완료 상태 및 감사 증거.
5. 제품별 구현 선택: CE/secure sanitize command/secure reset/물리적 파기 중 매체와 위험에 맞는 방식 선택. CE는 키 관리·암호화 적용 시점·키 파기 검증을 선행.
6. 기능안전 파라미터는 보안 삭제 기능과 별도 영향분석. 삭제 기능이 STO/SS1 등 안전 설정을 무단 변경하거나 안전 기능을 우회하지 않도록 권한·상태·복구 절차를 검토.

## 7. 출처 및 재검증 링크

1. EUR-Lex, Regulation (EU) 2024/2847, Annex I Part I (2)(i)/(m), Annex II point 8(d): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
2. NIST SP 800-88 Rev.2, final (2025-09-26): https://csrc.nist.gov/pubs/sp/800/88/r2/final
3. NIST, Rev.2 publication announcement (2025-09-26): https://www.nist.gov/news-events/news/2025/09/guidelines-media-sanitization-nist-publishes-sp-800-88r2
4. NIST SP 800-88 Rev.1 withdrawal notice / supersession details: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf
5. IEC official catalogue, IEC 62443-4-2:2019: https://webstore.iec.ch/en/publication/34421
6. ANSI/ISA-62443-4-2-2018 public excerpt, FR 4 / CR 4.1–4.3: https://s3.us-east-1.amazonaws.com/fonteva-customer-media/00D1I000002JB6nUAG/OvIGvqBd_S_62443_4_2_pdf

## 8. 제한 및 결론

- 이 문서는 원본 보고서 #4의 근거 오류와 기술적 과장을 바로잡는 감사/정정 기록이다. 원본 archive는 증거 보존을 위해 그대로 둔다.
- IEC 표준 전문은 저작권 보호 대상이다. 본 정정은 공개된 표준 설명 및 ISA 발췌본에서 확인 가능한 범위만 요약했다. 제품 적합성 결론 전에 정식 라이선스 표준 원문과 적용 범위를 확인해야 한다.
- 본 문서는 특정 servo drive 제품의 CRA 적합성 또는 인증을 선언하지 않는다.
