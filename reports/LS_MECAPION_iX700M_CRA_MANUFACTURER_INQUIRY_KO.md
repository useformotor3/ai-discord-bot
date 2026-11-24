# LS메카피온 iX700M CRA 제조사 기술·공급망 질의서
- 문서 상태: **초안 / 발송 전 검토 필요**
- 작성 기준일: 2026-11-25 (Asia/Seoul)
- 조사 범위: LS메카피온 iX700M DRIVE / Converter 제품군의 EU Cyber Resilience Act(Regulation (EU) 2024/2847) 적용성 및 제품 개발·공급망 보안 요구사항
- 범위 제외: SIL 3 및 CRA와 무관한 인증·안전등급 평가
- 회신 요청 형식: 질문별 답변 + 근거 문서명/개정번호/발행일 + 적용 모델/SKU + 담당 부서

## 1. 질의 목적과 회신 시 주의사항
당사는 iX700M 제품의 CRA 적용성 및 제품 개발·공급망 보안 요구사항을 정확히 평가하기 위해 아래 정보를 요청합니다. 일반 시리즈 수준의 답변보다 실제 공급되는 개별 모델·옵션·하드웨어/펌웨어 개정에 연결된 답변을 요청합니다.

가능하면 원본 PDF 또는 기계 판독 가능한 파일을 제공해 주십시오. 문서가 비공개인 경우에는 NDA 가능 여부와 함께 규제 적합성 평가에 필요한 최소 정보 또는 redacted version 제공 가능 여부를 알려주십시오. 파일명·게시물 목록·파일 크기만으로는 원본 증거를 대체할 수 없으므로 원본 파일과 문서 식별정보를 함께 요청합니다.

## 2. 제품 식별 및 제품 경계
1. iX700M DRIVE와 Converter Unit의 현재 판매 모델명 전체 목록을 제공해 주십시오. 모델명에 포함된 D1/D2/D3, B(480 Vac), 정격 용량, encoder type, option code의 의미와 조합 규칙도 확인해 주십시오.
2. 아래 모델이 실제 공급 모델인지, 현재 공급 중인지 확인해 주십시오.
   - Drive Unit 예시: iX700MD1-B-150B
   - Converter Unit 계열: iX700MCV
   - 위 예시는 공식 게시물의 식별 예시이며 실제 평가 대상 SKU로 확정한 것은 아닙니다.
3. 각 모델별 HW revision, PCB revision, BOM revision, firmware/bootloader version, 제조일 또는 serial-number 범위를 구분해 주십시오.
4. Drive Unit, Converter Unit, 제어보드, 통신 모듈, encoder/I/O 모듈은 각각 별도 주문·판매·교체 가능한 제품입니까? 아니면 특정 구성으로만 공급되는 하나의 완제품/시스템입니까?
5. 제품이 기계·설비 OEM에 통합되어 공급되는 경우, 누가 제품을 자기 상표로 시장에 제공하며 누가 최종 제품의 제조자 책임을 부담합니까? OEM/ODM/private-label 공급 모델을 구분해 주십시오.
6. 제품의 의도된 목적, 정상 운전 구성, 합리적으로 예측 가능한 사용·오용, 사용 환경(공장망/인터넷 연결 여부)을 설명하는 최신 기술 자료를 제공해 주십시오.

## 3. EU/EEA 시장 공급 및 경제운영자
7. iX700M DRIVE 및 Converter 제품이 EU/EEA 국가에 실제 공급되었거나 공급 예정인지 확인해 주십시오. 해당한다면 국가, 최초 공급/시장 제공 시점, 모델/SKU, 공급 수량 범위, 판매 법인 및 유통 경로를 제공해 주십시오.
8. EU/EEA 공급이 없다면 현재 계획 여부와 공급을 결정하는 법인/부서를 알려주십시오. 단순히 CE 또는 UKCA 문서가 게시되어 있다는 사실만으로 실제 EU 공급을 의미하지는 않는다는 점을 전제로 답변해 주십시오.
9. 제조자, EU 내 수입자, 공인대리인(있는 경우), 유통업자 및 기타 경제운영자의 법인명·국가·역할·연락처를 알려주십시오.
10. EU/EEA 고객에게 직접 판매, 유통사를 통한 판매, 기계 제조사 통합 공급, 샘플·시험·서비스 부품 제공 중 어떤 공급 형태가 존재합니까? 무상 공급과 상업적 공급도 구분해 주십시오.
11. 제품이 다른 기계·설비에 통합되는 경우, 통합 전 iX700M 구성품 자체가 별도 시장에 제공되는지, 통합 후 전체 시스템의 제조자가 누구인지, 통합자가 펌웨어·보안 기능을 변경하는지 설명해 주십시오.

## 4. 통신·소프트웨어·제품 경계 증거
12. 각 SKU에 실제 장착된 외부/내부 인터페이스를 목록으로 제공해 주십시오. 예: EtherCAT, RS-485, USB, Loader/maintenance port, Ethernet, encoder, I/O, service/debug interface.
13. 각 인터페이스의 사용 목적, 물리적 접근 필요 여부, 프로토콜/버전, 인증·접근통제 방식, 기본 활성화 상태, 비활성화 가능 여부를 알려주십시오.
14. PC commissioning/configuration tool, firmware loader, bootloader, parameter editor, remote diagnostic tool이 제공됩니까? 제공된다면 제품명·버전·배포 방식·라이선스·지원 OS와 CRA상 제품 경계에 대한 제조사의 판단을 제공해 주십시오.
15. 원격 진단, 클라우드, telemetry, 원격 유지보수 또는 제조사 서버가 드라이브의 기능 수행에 필수입니까? 해당 시스템이 있다면 데이터 흐름도, 서버 운영 주체, 연결 방향 및 통신 보안 방식을 제공해 주십시오.
16. 제품·도구·원격 서비스의 기능과 인터페이스를 연결한 최신 시스템 아키텍처 및 데이터 흐름도를 요청합니다.

## 5. HW BOM, MCU 및 SBOM
17. 실제 SKU별 BOM 또는 보안 검토에 필요한 부품 목록을 제공해 주십시오. 최소한 MCU/MPU, memory, Ethernet/EtherCAT controller, 통신 IC, secure element/crypto IC, boot ROM, programmable logic, third-party module을 식별할 수 있어야 합니다.
18. MCU 제조사와 정확한 part number, silicon revision, security-related functionality, 보안 기능 사용 여부를 알려주십시오. ST MCU 사용 여부도 실제 iX700M 회로도/BOM에 근거해 확인해 주십시오. 다른 제품의 MCU 정보가 iX700M에 자동 적용되는 것으로 보지 않습니다.
19. 펌웨어/bootloader/RTOS/third-party library/OSS 및 제3자 소프트웨어 구성요소의 이름·버전·공급자·라이선스·취약점 식별자를 포함한 SBOM을 제공해 주십시오.
20. CRA Annex I Part II(1)의 최소 요구사항은 일반적으로 사용되는 기계 판독 가능한 형식으로 최소 top-level dependencies를 포함하는 SBOM입니다. 가능하다면 전체 직접·간접 의존성을 포함한 SPDX 또는 CycloneDX 파일을 모델/SKU 및 firmware version에 연결해 제공해 주십시오.
21. SBOM이 빌드 산출물에서 자동 생성되는지, 릴리스마다 갱신되는지, 취약점 데이터베이스와 대조되는지, 변경 이력을 추적하는지 설명해 주십시오.

## 6. 보안 설계·초기 설정·접근통제
22. Secure boot 또는 chain of trust가 구현되어 있습니까? 구현되어 있다면 boot ROM부터 bootloader/application firmware까지 검증 단계와 실패 시 동작을 설명해 주십시오.
23. Firmware image는 전자서명 또는 MAC 등으로 인증됩니까? 서명 알고리즘, 키 생성·보관·교체·폐기, 제조 단계 key injection, 제품별/공통 키 사용 여부를 알려주십시오. 비밀키 자체는 요청하지 않습니다.
24. Firmware update package의 무결성·진위 검증, downgrade 방지, rollback 허용 정책, 업데이트 실패 후 복구 절차를 설명해 주십시오.
25. Debug/JTAG/SWD/UART/Loader port는 양산품에서 어떻게 보호됩니까? 생산 모드와 field/service mode를 구분하고 debug lock, 인증, 물리적 봉인, 접근 로그 및 예외 승인 절차를 알려주십시오.
26. 기본 계정·암호, 서비스 패스워드, parameter write 권한, remote access 및 role-based access control의 초기 설정과 변경 정책을 설명해 주십시오.
27. 저장·전송 데이터, 제어 명령, 파라미터 및 firmware의 기밀성·무결성 보호 방식, 암호화 사용 여부, 보안 설정 초기화/공장 초기화 방법을 제공해 주십시오.
28. 제품의 secure-by-default 설정, 공격 표면 최소화, 필수 기능 가용성·복구, 보안 이벤트 기록 및 사용자 통지 기능에 대한 설계/시험 증거를 제공해 주십시오.

## 7. 취약점 처리 및 Article 14 보고 체계
29. 제조사의 PSIRT 또는 이에 준하는 취약점 대응 조직이 있습니까? 책임 부서, 24시간 연락 경로, 일반 사용자/연구자용 취약점 신고 주소, 보안 정책 및 CVD(Coordinated Vulnerability Disclosure) 정책을 제공해 주십시오.
30. 외부 신고 접수, 영향 SKU·firmware 식별, 심각도 평가, 재현, 조치 우선순위, 패치 개발, 검증, 고객 통지 및 공개까지의 절차와 목표 처리시간을 설명해 주십시오.
31. 제3자/OSS 구성요소 취약점 발견 시 해당 구성요소 제조자·유지관리자에게 통지하고 수정사항을 upstream 공유하는 절차가 있습니까?
32. 알려진 취약점, CVE, 보안 권고문, 패치 이력 및 제품 영향 분석 자료를 제공해 주십시오. 해당 사항이 없다고 답하는 경우에도 조사 범위와 기준일을 명시해 주십시오.
33. CRA Article 14에 따른 actively exploited vulnerability 및 severe incident 보고를 담당하는 법인·책임자·절차가 지정되어 있습니까? 2026-09-11부터 적용되는 24시간 early warning, 72시간 notification, final report 기한(악용 취약점은 시정/완화 조치 제공 후 14일, 중대 사고는 72시간 notification 후 1개월)을 운영 절차에 반영했는지 확인해 주십시오.
34. Article 14 보고 의무가 제품 지원기간 종료 후에도 계속 적용된다는 점을 고려해, 지원 종료 제품의 취약점/사고 보고 연락망과 고객 통지 방식을 어떻게 유지합니까?

## 8. 보안 업데이트 및 지원기간
35. Firmware/security update의 개발·서명·배포·설치·검증·실패 복구 절차를 설명해 주십시오. 업데이트 배포 채널, 고객 접근 방식, 무결성 검증 및 위조 패키지 거부 시험 증거를 요청합니다.
36. 보안 업데이트와 기능 업데이트를 기술적으로 분리해 배포할 수 있습니까? 불가능하다면 그 이유와 위험 완화 방안을 설명해 주십시오.
37. 보안 업데이트는 지체 없이 제공됩니까? 원칙적으로 무상 제공되는지, 맞춤형 제품에 대해 business user와 별도 합의가 있는 경우가 있는지 구분해 주십시오.
38. 모델/SKU별 지원기간 시작일·종료일(월/년), 지원기간 산정 근거, 예상 사용수명, 유사 산업용 제품의 지원기간 및 핵심 제3자 부품의 지원기간을 제공해 주십시오. 산업용 제어장치는 5년을 훨씬 넘게 사용될 수 있으므로, 5년을 자동 기본값으로 두지 말고 실제 예상 사용기간에 근거해 설명해 주십시오.
39. 지원기간 중 배포한 각 보안 업데이트를 발행 후 최소 10년 또는 남은 지원기간 중 더 긴 기간 동안 이용할 수 있도록 보존·배포합니까? 업데이트 archive, 접근권한 및 보존 정책을 요청합니다.
40. 구매 시점의 지원 종료일 표시, 지원 종료 알림, 지원 종료 후 취약점 접수·고객 안내 정책을 설명해 주십시오.

## 9. CRA 기술문서·EU DoC·매뉴얼·제품 자료
41. CRA Article 31 및 Annex VII에 따라 작성된 제품 기술문서가 있습니까? 있다면 제품 설명, HW/FW version, 아키텍처, BOM/SBOM, 취약점 처리 절차, CVD policy, 보안 업데이트 배포 설계, 위험평가, 지원기간 산정 및 시험 보고서를 제공하거나 검토 가능한 형태로 제공해 주십시오.
42. 실제 SKU별 signed EU Declaration of Conformity 원본을 요청합니다. 문서에 모델 식별, 제조자 법인/주소, 적용 EU 법령, 적용 표준, 평가기관(해당 시), 발행일, 서명자 성명·직위·서명 및 적용 범위가 명확히 표시되어야 합니다.
43. 공식 게시물에 표시된 Drive CE DoC iX700MD1-B-150B의 실제 PDF 원본, Converter CE DoC iX700MCV PDF 원본을 각각 제공해 주십시오. 각 선언서가 포괄하는 모델·옵션·HW revision·공급 조건을 명시해 주십시오.
44. Converter UKCA DoC는 별도 영국 규제 문서로 관리하고, EU DoC와 혼동되지 않도록 원본 및 적용 범위를 구분해 제공해 주십시오.
45. iX700M DRIVE 400[V] 매뉴얼 Ver1.4의 원본 PDF 및 발행/개정 이력을 제공해 주십시오. 공식 목록에서 Ver1.4와 Ver1.3이 서로 다르게 표시된 이유, 실제 배포 가능한 최신 revision, 대체·폐기된 revision 여부를 확인해 주십시오.
46. 최신 KR/EN 카탈로그 원본 PDF, iX700M 2D CAD(DWG/DXF 등) 및 3D CAD(STEP) 원본 파일과 각각의 개정번호·발행일을 제공해 주십시오.
47. 문서별 원본 파일명, 크기, SHA-256, 문서번호, revision, 발행일, 해당 SKU 및 공개/배포 상태를 함께 제공해 주십시오. 전자서명된 파일이면 서명 검증이 가능한 원본을 요청합니다.

## 10. 요청 자료 목록 및 우선순위
| 우선순위 | 자료 | 현재 확인 상태 | 제조사에 요청할 결과 |
|---|---|---|---|
| P0 | iX700M DRIVE 400[V] Ver1.4 manual | 목록 metadata만 확인, Ver1.3 충돌 | 원본 PDF + revision history |
| P0 | Drive SKU-specific EU DoC | iX700MD1-B-150B / 238.9K 첨부 metadata | signed original PDF + covered SKU list |
| P0 | Converter CE DoC | iX700MCV / 234.4K metadata | signed original PDF + scope |
| P0 | EU/EEA 공급·경제운영자 | Unknown | 국가·최초 공급일·공급 경로·법인 역할 |
| P1 | Converter UKCA DoC | iX700MCV / 224.1K metadata | original PDF, EU DoC와 별도 관리 |
| P1 | KR/EN catalogue | 각 10.7MB metadata | 원본 PDF + revision |
| P1 | 2D CAD / 3D STEP | 2026-04-21 listing metadata | 원본 DWG/DXF/STEP |
| P1 | SKU/HW/FW/BOM/SBOM | Unknown | version-bound machine-readable evidence |
| P1 | PSIRT/CVD/update/support | Unknown | policy, contact, test and lifecycle evidence |

## 11. 회신 표준 및 확인 요청
각 답변에 아래 정보를 기재해 주십시오.

| 필드 | 회신 내용 |
|---|---|
| 질문 번호 | 예: Q17 |
| 답변 | Yes / No / Not applicable / Unknown + 상세 설명 |
| 적용 제품 | 정확한 SKU / option / HW revision / FW version |
| 근거 문서 | 문서번호 / 파일명 / revision / 발행일 |
| 증거 파일 | 원본 첨부 또는 안전한 다운로드 위치 |
| 제한사항 | 비공개·NDA·미보유·미검증 여부 |
| 담당자 | 부서 / 직책 / 회신 책임자 |
| 회신일 | YYYY-MM-DD |

**중요:** 회신이 없거나 증거가 제공되지 않은 항목은 본 조사에서 Unknown으로 유지합니다. 제품 목록의 파일명·크기·게시일은 원본 문서 취득이나 내용·서명·적용 범위 검증과 동일하지 않습니다. 본 질의서는 초안이며 제조사에 발송하지 않았습니다.

## 공식 규제 근거
- Regulation (EU) 2024/2847 (Cyber Resilience Act): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- Commission Guidance C/2026/6013, OJ C, 17.11.2026: https://publications.europa.eu/resource/cellar/dcbc848b-e227-11f1-aefc-01aa75ed71a1.0006.01/DOC_1

CRA only; SIL 3 excluded.


## 12. 추가 확인 질문 — 공식 게시물의 모델 범위와 원본 진위 (2026-11-25)

아래 질문은 공식 게시물에서 확인된 시리즈/첨부 metadata를 실제 주문 모델과 연결하기 위한 추가 질문입니다. 게시물 제목이나 첨부파일 크기만으로 covered SKU, 서명, 적합성 또는 실제 공급을 확정하지 않습니다.

48. Drive EU CE DoC 게시물(wr_id=12888)은 제목상 iX700MD1-B-150B를 특정합니다. 해당 PDF의 covered model은 정확히 이 단일 SKU입니까? D2/D3, 다른 정격(예: 050B/075B/220B/300B/370B/450B/550B/750B), encoder code 및 custom option이 포함된다면 각 모델의 포함 근거와 제한을 DoC 원문 및 technical schedule로 제시해 주십시오.
49. Converter CE/UKCA DoC의 iX700MCV 480Vac 15/37/55/75kW는 실제 주문 가능한 각 모델코드와 어떻게 대응합니까? rating suffix, standard/option code, HW revision 및 인증서 적용범위를 표로 제시하고 CE와 UKCA의 제조자·법적 근거·평가범위를 별도로 확인해 주십시오.
50. 공식 iX700M 제품 소개의 AC 380–480V, 4.5–75kW, 축당 16.1–168A 및 EtherCAT 설명을 실제 Drive/Converter 조합별 SKU, axis count, firmware version, interface/option과 매핑한 공식 selection table을 제공해 주십시오. 이 시리즈 범위가 모든 개별 SKU에 동일하게 적용되는 것으로 보지 않습니다.
51. 매뉴얼 게시물 wr_id=12652의 Ver1.4와 동일 날짜의 별도 목록에 나타나는 Ver1.3 중 어느 것이 release authority가 있는 정식 배포본입니까? Ver1.3→Ver1.4 변경이력, 승인일, 적용 SKU/HW/FW, 폐기된 revision 여부, 원본 PDF 파일명·크기·SHA-256을 제시해 주십시오.
52. EU DoC/UKCA DoC 각각에 대해 원본 PDF의 전자서명 존재 여부, 서명 인증서 체인/검증 방법(전자서명이 없는 스캔본이면 원본 서명본 확인 방법), 서명자 권한, 발행일, 문서번호, 개정이력 및 현재 유효성 확인 책임부서를 알려주십시오. 비밀키나 민감한 내부 정보는 제공하지 않아도 됩니다.
53. CAD 게시물(wr_id=12455)의 2D 및 3D 원본 파일별 파일명, native format(DWG/DXF/STEP 등), revision, 작성 소프트웨어/version, 단위·축척, 적용 모델/외형 option, 포함/제외 부품(커넥터·방열판·브라켓 등)을 목록화해 주십시오. PDF preview나 이미지가 아닌 원본 binary를 요청합니다.
54. 카탈로그 KR/EN 파일 각각의 승인 revision, 언어별 내용 동등성, 발행일, SHA-256, 지원되는 모델·정격·옵션의 범위를 제공해 주십시오. 카탈로그의 marketing lineup과 현재 실제 판매/공급 가능한 SKU를 별도 표로 구분해 주십시오.
55. 위 모든 자료에 대해 제조사 공식 document owner, 승인 상태(Released/Obsolete/Draft), 공개·배포일, 교체 문서, 원본 보관 위치 및 고객이 최신본을 확인할 공식 경로를 제공해 주십시오.

**추가 증거 연결 원칙:** 각 답변은 질문번호 → exact SKU/order code → HW/FW revision → 문서번호/revision → 원본 파일 → SHA-256/서명 검증 결과 순으로 연결해야 합니다. 어느 한 연결고리가 누락되면 해당 제품·기능 판정은 Unknown으로 남깁니다.

## 13. 제조사 공식 자료 metadata 재확인 결과

| 게시물 | 공개 metadata | binary/내용 확인 |
|---|---|---|
| Manual wr_id=12652 | iX700M DRIVE 400[V] Ver1.4, 2026-05-26 | detail timeout; Ver1.3 index 충돌 지속 |
| Drive EU CE DoC wr_id=12888 | iX700MD1-B-150B, 238.9KB | original PDF/signature not obtained |
| Converter CE DoC wr_id=12886 | iX700MCV, 480Vac 15/37/55/75kW, 234.4KB | original PDF not obtained |
| Converter UKCA DoC wr_id=12893 | iX700MCV, 224.1KB | original PDF not obtained; UKCA distinct from EU DoC |
| Catalogue wr_id=12110 | KR/EN each 10.7MB | original PDFs not obtained |
| CAD wr_id=12455 | 2D CAD / 3D STEP listing, 2026-04-21 | detail timeout; native files not obtained |

이 자료는 게시물 metadata의 재확인 기록이며 원본 binary 취득 기록이 아닙니다. 제조사 회신 전까지 모든 product-specific facts remain Unknown.



56. CE 카테고리 인덱스에는 2026-04-30자로 iX700MCB 및 Drive Unit의 모델 그룹별 게시물(075B/050B/D2-B-045B, 150B, 220B, 370B/300B, 750B/550B/450B)이 각각 표시됩니다. 각 게시물에 연결된 원본 EU DoC PDF, 문서번호, covered model/SKU 전체 목록, 정격·encoder·option code, HW revision, DoC별 적용 표준/법령 및 서로 다른 게시물 간 scope 중복/공백을 제공해 주십시오. 특히 iX700MCB가 독립 판매되는지, Converter/Drive와 결합되는 내부 모듈인지 제품 경계를 설명해 주십시오.
57. KC 인덱스의 iX700MD1/MD2/MCV/MCB 모델 목록과 CE/UKCA DoC 목록을 별도 규제 근거로 관리하고 있습니까? 동일한 모델명이라도 각 문서의 관할·법적 근거·평가 범위·제조자 선언 책임을 구분한 compliance matrix를 요청합니다. KC 인증/게시 사실을 EU DoC 또는 CRA 적합성 증거로 간주하지 않는다는 점을 확인해 주십시오.
58. Drive Unit(D1/D2/D3), Converter Unit(CV), iX700MCB 및 통신/제어 모듈의 조립·판매·교체 관계를 설명해 주십시오. 각각 별도 주문·시장 제공되는지, 하나의 drive system으로만 공급되는지, 어느 구성요소에 펌웨어·네트워크 인터페이스·보안 기능이 위치하는지, 통합 OEM이 기능·펌웨어를 변경할 수 있는지 SKU별 block diagram으로 제시해 주십시오.


 
59. iX700M Drive Unit, Converter Unit 및 iX700MCB 각각에 대해 CRA상 제품 분류를 어떤 단위와 근거로 결정했습니까? Regulation (EU) 2024/2847 Article 7의 Annex III core-functionality test, Article 8 및 Annex IV를 기준으로 (a) default product인지, (b) Annex III Class I 또는 Class II의 정확한 항목번호인지, (c) Annex IV critical product인지 명시하고, 의도된 목적·핵심 기능·시장 제공 단위·기술 아키텍처를 연결한 분류 근거서를 제공해 주십시오. Annex III Class I item 14의 security-related microcontroller 또는 Class II item 4의 tamper-resistant microcontroller가 관련된다고 판단한다면, 해당 MCU가 독립 제품으로 시장에 제공되는지 또는 drive 내부 구성품인지, 보안 관련 기능이 실제 활성화되어 제품의 core functionality에 해당하는지 증거로 구분해 주십시오. 단순히 MCU가 내장되어 있거나 산업 자동화 설비에 사용된다는 이유만으로 드라이브 전체를 중요/중요등급/critical product로 분류하지 말고, published Annex III/IV의 정확한 범주와 core-functionality 연결을 설명해 주십시오. 그 분류에 따른 Article 32 conformity assessment procedure(Module A, B+C, H 또는 적용 가능한 European cybersecurity certification)와 notified body 개입 여부, 적용한 harmonised standards/common specifications/certification scheme 및 적용하지 않은 항목의 사유도 모델/SKU별로 제시해 주십시오.
