# LS메카피온 iX700M 기술·영업 공식 질의서 (CRA 제품경계 및 설계증거 확인)

- 문서 상태: 제조사 발송 전 검토용 초안
- 개정: v2.0 (2026-11-25)
- 대상: LS메카피온 iX700M Series, 400 V modular servo drive
- 목적: EU Cyber Resilience Act (Regulation (EU) 2024/2847) 적용성·제품경계·기술문서 확인
- 질문 ID: Q01–Q62 (총 62개, 중복 통합 후 재번호화)
- 회신 요청: 질문별 답변, 해당 원본 문서/증거 첨부, 미제공 사유 및 담당부서 표시

## 1. 문의 목적 및 비밀유지

당사는 산업용 서보 드라이브의 EU 시장 공급 및 Cyber Resilience Act(CRA) 대응을 위한 제품 적용성·기술자료 검토를 수행하고 있습니다. 공개된 iX700M 제품군 자료를 바탕으로 아래 사항을 확인하고자 합니다.

Converter Unit과 Drive Unit의 독립 주문·판매 가능 여부, EU/EEA 공급범위, 실제 판매 SKU, 원본 매뉴얼·DoC·카탈로그·CAD, 유닛별 회로도/BOM과 주요 반도체 전체 부품번호, 펌웨어 업데이트 및 보안 설정, 취약점 대응·지원기간을 확인하고자 합니다.

회로도, BOM, 보안 설계자료 등 비공개 자료는 NDA 체결 후 제공 가능한 범위와 열람 조건을 안내해 주십시오. 자료 제공이 어려운 경우 고객사/제3자 비밀정보를 제거한 redacted version, 부품군 수준의 BOM, 보안기능 체크리스트, 또는 제조사 서명 확인서로 대체할 수 있는지도 알려 주십시오.

**요청하지 않는 정보:** 개인키, 인증서 개인키, 암호키 원문, 비밀번호, 생산용 계정, 취약점 악용에 직접 이용될 수 있는 비공개 접근정보는 보내지 마십시오. 보안 설정의 존재·상태·정책·검증 결과만 요청합니다.

## 2. 회신 및 증거 작성 방법

질문마다 다음 중 하나의 상태를 표시해 주십시오.

- 확인됨 (Confirmed)
- 해당 없음 (Not applicable)
- 개발 중 (In development)
- 확인 필요 (Needs confirmation)
- 공개 불가 / NDA 가능 (Restricted / NDA possible)
- 보유하지 않음 (Not held)

각 답변에는 가능한 범위에서 문서 ID, 개정번호, 발행일, 적용 SKU/HW/FW, 담당부서 및 첨부파일 ID를 연결해 주십시오. “확인됨” 답변은 원본 문서 또는 제조사 서명 확인서로 뒷받침해 주십시오. 구두 답변은 참고 기록으로 보관하되 제품 경계·공급범위·CRA 분류를 바꾸는 증거로 단독 사용하지 않습니다.

## 3. 질문 목록 (Q01–Q62)

### A. 회신 주체 및 제품·상업적 경계

1. **Q01 [P0]** 회신 회사의 정확한 법인명, 사업장 주소, 회신 부서, 담당자 성명·직책 및 회신 권한은 무엇입니까?
2. **Q02 [P0]** 회신자는 제품 설계·품질·인증·영업·해외사업·제품보안 중 어느 업무를 대표하며, 질문별 답변 담당부서를 지정할 수 있습니까?
3. **Q03 [P0]** 답변 기준 제품의 정확한 제품명, HW revision, FW revision, 생산/판매 기간 및 적용 유닛은 무엇입니까?
4. **Q04 [P0]** Converter Unit은 Drive Unit과 별도로 견적·발주·계약·납품·송장 처리할 수 있습니까? Drive Unit의 독립 판매 가능 여부도 별도로 답변해 주십시오.
5. **Q05 [P0]** 두 유닛의 독립 판매가 가능하다면 실제 판매 가능한 전체 표준 SKU와 전체 주문코드(suffix/option 포함)를 제공해 주십시오. 불가능하다면 반드시 함께 공급해야 하는 기술적·상업적 이유를 설명해 주십시오.
6. **Q06 [P1]** 한 개 Converter에 복수 Drive Unit을 조합하는 구성, 복수 Converter 구성, 예비품·교체품 판매가 가능한지 각각 답변해 주십시오.
7. **Q07 [P1]** Converter, Drive, Bus-Bar, DC Link, 제어/통신 보드 및 외부 옵션 모듈의 독립 주문 가능 여부와 각 유닛의 별도 포장·명판·일련번호·보증·수리·펌웨어 관리 단위를 표로 제공해 주십시오.
8. **Q08 [P1]** Converter 또는 Drive만 교체·추가 구매할 수 있습니까? 교체 시 호환성 제한, 파라미터 이관, 시스템 재평가 또는 재인증 조건이 있습니까? 민감정보를 삭제한 견적서/발주서의 개별 line-item 예시를 제공할 수 있습니까?

### B. EU/EEA 공급·시장 출시 및 경제운영자

9. **Q09 [P0]** iX700M Series가 EU/EEA 회원국에 실제 판매·수출·납품된 적이 있습니까? 예/아니오/확인 중으로 답변하고 증거를 제시해 주십시오.
10. **Q10 [P0]** 현재 EU/EEA에 판매 가능한 상태입니까? 판매 중단·출시 예정·프로젝트 한정 공급을 구분해 주십시오.
11. **Q11 [P0]** 실제 공급 국가, 최초/최근 공급 시점, 현재 공급 가능한 국가 및 공급을 담당한 법인을 알려 주십시오.
12. **Q12 [P0]** EU 고객에게 Converter만, Drive만 또는 양 유닛 조합으로 공급한 사례가 있습니까? 각 공급 단위와 SKU를 구분해 주십시오.
13. **Q13 [P0]** 실제 EU 수입자(importer), 유통업체(distributor), 현지 대리점, 제조자 및 CRA 경제운영자(economic operator)의 법인명과 역할을 공개 가능한 범위에서 알려 주십시오.
14. **Q14 [P0]** EU 공급 SKU, 명판/제품 라벨 및 포장 표기를 확인할 수 있는 사진이나 redacted 계약서·견적서·송장·납품서·선적서류를 제공할 수 있습니까?
15. **Q15 [P1]** EU 공급이 아직 없다면 향후 공급 계획·목표 시점·판매 주체·예상 공급 단위는 무엇이며, CRA 관점에서 제조자·수입자·유통업체·EU 연락창구를 어느 법인이 담당합니까?

### C. 실제 SKU 및 제품 구성 식별

16. **Q16 [P0]** CRA 평가에 사용해야 할 iX700M 현행 표준 SKU 전체 목록과 주문 가능한 옵션 조합을 제공해 주십시오.
17. **Q17 [P0]** iX700MCV-B-150/370/550/750, iX700MD1-B-150B 등 Drive 코드, iX700MCB 및 iX700MCB-B-8K의 각 자리와 suffix 의미를 공식 정의해 주십시오.
18. **Q18 [P0]** MCB 및 8K의 의미, 기능, 구성품 및 판매/공급 단위를 정의해 주십시오. 공식 정의가 없다면 해당 표기가 적용되는 제품을 설명해 주십시오.
19. **Q19 [P0]** SKU별 정격 입력·출력, 전압, 정격용량·전류, 축수, 엔코더, 통신 옵션 및 지원 모터를 포함한 모델 매트릭스를 제공해 주십시오.
20. **Q20 [P0]** Converter/Drive 조합 가능표, Bus-Bar/DC Link 구성, 조합 제한 및 호환 HW/FW 매트릭스를 제공해 주십시오.
21. **Q21 [P0]** 본 프로젝트의 실제 대상 SKU를 특정하기 위해 필요한 명판 사진, 주문서 항목, serial number 조회 절차를 안내하고, 표준품·주문형(customized) 코드 및 부품 대체(AVL/second source) 식별 방법을 설명해 주십시오.

### D. 매뉴얼·카탈로그·외형 CAD 원본

22. **Q22 [P0]** 현재 공식 배포 중인 iX700M 매뉴얼의 원본 PDF, 정확한 문서번호, revision, 발행일, 언어 및 문서관리 ID를 제공해 주십시오.
23. **Q23 [P0]** 매뉴얼별 적용 SKU, HW/FW revision, 유닛(Converter/Drive), 변경 이력, 변경 요약 및 구판 대체 여부를 알려 주십시오.
24. **Q24 [P1]** KR/EN iX700M 카탈로그의 원본 PDF, 문서번호·revision·발행일·적용 SKU 및 두 언어판의 차이를 제공해 주십시오.
25. **Q25 [P0]** iX700M 2D CAD의 원본 DWG/DXF 파일을 제공하고, 파일별 revision·적용 SKU·CAD 버전·단위(mm/inch)를 알려 주십시오.
26. **Q26 [P0]** iX700M 3D CAD의 원본 STEP 파일을 제공하고, 파일별 revision·적용 SKU·단위·좌표/기준면 정보를 알려 주십시오.
27. **Q27 [P1]** Converter 단독, Drive 단독, Bus-Bar 및 조합 설치 상태의 외형도를 구분하고, 커넥터·단자·통풍·접지·장착 치수의 포함 여부를 알려 주십시오.
28. **Q28 [P1]** 각 매뉴얼·카탈로그·CAD 원본의 파일명·형식·크기·발행/개정일·적용 SKU·SHA-256 또는 제조사 문서관리 식별자를 제공해 주십시오. 외형도와 별도로 회로도·배선도·블록도·핀맵의 제공 가능 범위 및 NDA 조건도 알려 주십시오.

### E. 회로도·PCB·BOM 및 주요 반도체

29. **Q29 [P1]** Converter와 Drive 각각의 최신 회로도(schematic), 기능 블록도, PCB revision 및 BOM을 제공할 수 있습니까?
30. **Q30 [P0]** 전체 BOM 제공이 어렵다면 주요 보안·통신·제어 부품에 한정한 redacted BOM 또는 제조사 서명 부품목록을 제공해 주십시오.
31. **Q31 [P0]** MCU/MPU/DSP, Ethernet/EtherCAT controller, PHY, FPGA/CPLD, Flash/RAM/EEPROM, 보안 IC/secure element 및 USB/시리얼 통신 IC의 제조사·전체 부품번호·적용 유닛을 알려 주십시오.
32. **Q32 [P0]** 각 반도체의 full ordering code(패키지·온도등급·메모리·보안 옵션 suffix 포함), silicon stepping/revision 및 적용 SKU/HW revision을 알려 주십시오.
33. **Q33 [P0]** 각 유닛에서 사용하는 MCU/MPU/DSP의 실제 제조사와 전체 주문코드를 확인해 주십시오. STMicroelectronics 제품이면 ST의 full part number·silicon revision·package를, ST 제품이 아니면 실제 제조사와 전체 주문코드를 알려 주십시오.
34. **Q34 [P1]** 부품 대체(AVL/second source)가 있다면 대체 전후의 전체 부품번호, 적용 생산 lot/기간, 기능·보안 차이 및 영향받는 SKU를 알려 주십시오.
35. **Q35 [P1]** 펌웨어가 실행되는 각 프로세서, 부트 ROM, bootloader, 외부 Flash 및 FPGA bitstream의 소유·관리 주체와 버전 식별 방법을 제공해 주십시오. NDA로 자료 제공이 제한되면 제조사 서명 확인서를 제시해 주십시오.

### F. 펌웨어·부트·업데이트 구조

36. **Q36 [P1]** 각 유닛별 firmware, bootloader, FPGA/CPLD image 및 통신 stack의 구성요소·버전·build ID를 알려 주십시오.
37. **Q37 [P1]** USB, EtherCAT, Ethernet, RS-485 또는 전용 툴 등 펌웨어 업데이트 인터페이스와 업데이트 대상 유닛을 알려 주십시오.
38. **Q38 [P0]** 업데이트 파일의 진위성·무결성을 digital signature, MAC, hash 또는 secure boot chain 중 어떤 방식으로 검증합니까? 적용 알고리즘·검증 단계·적용 SKU를 알려 주십시오.
39. **Q39 [P1]** 서명 검증을 사용한다면 알고리즘/키 길이/인증서 체계, 키 관리 책임자, 키 교체·폐기 절차를 알려 주십시오. 비밀키 원문은 요청하지 않습니다.
40. **Q40 [P0]** 서명되지 않은 이미지, 변조 이미지, 구버전 이미지, 잘못된 이미지 또는 업데이트 중 전원 차단을 장치가 어떻게 처리하는지 알려 주십시오.
41. **Q41 [P0]** anti-rollback/version downgrade 방지 기능의 존재 여부, 적용 유닛, 기본 활성화 상태, 예외 및 서비스 해제 절차를 알려 주십시오.
42. **Q42 [P1]** 업데이트 실패 시 복구·복원 방식, 안전한 기본 상태, 현장 복구 도구, 업데이트 권한(사용자/서비스/제조사) 및 Converter-Drive 간 버전 호환표를 제공해 주십시오.

### G. 보안 구성 및 보안 기능

43. **Q43 [P0]** Secure boot 또는 firmware authenticity verification의 적용 유닛·SKU·FW 버전 및 생산 기본 활성화 여부는 무엇입니까?
44. **Q44 [P0]** Debug/JTAG/SWD/UART/bootloader/service port의 생산 단계 잠금 상태와 현장 서비스 시 재활성화 통제를 알려 주십시오.
45. **Q45 [P1]** 디버그 잠금 해제에 필요한 인증·물리적 접근·제조사 도구와 잠금 해제 이력 기록 여부를 알려 주십시오.
46. **Q46 [P0]** 장치 식별·사용자 인증·역할 기반 권한(RBAC)·기본 계정/초기 비밀번호 정책 및 최초 설치 시 변경 강제 여부를 알려 주십시오.
47. **Q47 [P0]** EtherCAT, RS-485, USB, Ethernet 등 각 인터페이스의 프로토콜·서비스·포트·인증·암호화 지원 여부와 불필요한 서비스 비활성화 방법을 알려 주십시오.
48. **Q48 [P1]** 읽기/쓰기 권한 분리, 설정 변경 보호, 원격/로컬 관리 기능의 접근 통제 및 감사 로그 기능을 알려 주십시오.
49. **Q49 [P1]** MCU/SoC의 암호화·인증·RNG·TEE·hardware root of trust·secure element 기능 중 실제 제품에서 사용하는 항목과 적용 SKU를 알려 주십시오.
50. **Q50 [P0]** 암호키·인증서의 생성·주입·저장·교체·폐기 및 생산라인 접근통제 정책을 알려 주십시오. 실제 키·비밀번호 원문은 제공하지 마십시오.
51. **Q51 [P1]** tamper evidence/detection/resistance/response 기능의 존재 여부, 적용 유닛 및 검증 자료를 알려 주십시오.
52. **Q52 [P1]** 보안 이벤트·인증 실패·설정 변경·펌웨어 업데이트·오류 로그의 기록 항목·보존기간·외부 반출 방법과 공장 초기화 시 계정·인증서·키·네트워크 설정 처리 방법을 알려 주십시오.

### H. 취약점 대응·SBOM·지원기간·CRA 운영

53. **Q53 [P0]** 제품 보안 취약점 접수용 공식 연락처 또는 PSIRT가 있습니까? 공개 신고 절차, CVD 정책 및 보안 권고문 페이지를 알려 주십시오.
54. **Q54 [P0]** 취약점 접수, triage, 영향 SKU 확인, 심각도 평가, 수정 개발, 배포, 고객 통지 및 종료 절차와 담당 조직을 설명해 주십시오.
55. **Q55 [P0]** CVE/제3자 취약점 데이터베이스를 모니터링합니까? MCU, EtherCAT stack, RTOS, bootloader 및 third-party library의 취약점 추적 책임과 기록 방식을 알려 주십시오.
56. **Q56 [P0]** SBOM을 SPDX 또는 CycloneDX의 machine-readable 형식으로 제공할 수 있습니까? 형식·버전·구성품 식별 수준·갱신 주기·파일 hash를 알려 주십시오.
57. **Q57 [P1]** 취약점이 확인되면 보안 업데이트·완화책·보안 공지를 고객에게 어떤 경로로 제공하며, 기능 업데이트와 보안 업데이트를 구분합니까?
58. **Q58 [P0]** 제품 예상 사용기간, 판매 종료(EOL), 지원 종료(EOS), 보안 업데이트 제공 종료일 및 SKU별 지원정책·계약 예외를 알려 주십시오.
59. **Q59 [P0]** CRA Article 14의 actively exploited vulnerability/severe incident 신고를 위한 24시간·72시간·최종 보고 절차, 내부 인지시점 기록, 담당 조직 및 고객/제조자 간 정보 전달 체계를 준비했습니까? 보안 개발수명주기·위험평가·보안시험 요약을 NDA 후 제공할 수 있습니까?

### I. CE/UKCA DoC 및 통합 증거

60. **Q60 [P0]** Converter Unit, 각 Drive Unit 및 조합 시스템별 CE DoC와 해당하는 UKCA DoC 원본을 제공해 주십시오. 각 선언서의 정확한 모델/SKU·옵션·제조자 법인·적용 법령/표준·발행일·서명권자·시험 구성·제외 조건을 연결하고, DoC 적용 범위가 단독 유닛인지 조합 시스템인지 명시해 주십시오. EMC/LVD 시험성적서와 기존 CE 자료가 CRA 기술문서·위험평가와 별도 관리되는지도 알려 주십시오.

### J. 미해결 핵심 확인사항

61. **Q61 [P0] — 매뉴얼 Ver1.3/Ver1.4 충돌:** 공식 배포용 iX700M DRIVE 400[V] 매뉴얼의 원본 PDF, 문서번호, authoritative revision, 발행일, 전체 revision history 및 변경 요약을 제공해 주십시오. Ver1.3과 Ver1.4가 실제 별도 개정인지, 게시판 첨부 교체인지, 검색 색인 snapshot 차이인지, 어느 버전이 현재 판매·서비스 기준인지 서면으로 확인해 주십시오. 적용 Drive SKU/HW/FW, 언어판, 구판 대체 여부, 원본 파일명·형식·크기·SHA-256 또는 제조사 문서관리 ID도 함께 제시해 주십시오. LS ELECTRIC Solution Square에 표시된 2026-09-16 update 항목과 동일 문서인지도 확인해 주십시오.

62. **Q62 [P0] — 실제 SKU별 MCU·BOM·SBOM·보안 증거 통합표:** 실제 공급/평가 대상 SKU마다 Converter/Drive 구성, BOM 기준 MCU 제조사와 full orderable part number·silicon revision, firmware/bootloader build ID, machine-readable SBOM(SPDX/CycloneDX 및 버전/hash), secure boot·firmware signing·debug/JTAG/SWD lock·인증/권한·키 lifecycle·update/anti-rollback 설정, 취약점 접수/PSIRT/CVD·지원기간을 한 개의 추적 가능한 표로 연결해 주십시오. 전체 BOM이 NDA로 제한되면 redacted BOM 또는 제조사 서명 확인서로 대체하고, 실제 비밀키·비밀번호는 제외해 주십시오. 답변이 SKU별로 다르면 각 SKU를 분리해 주십시오.

## 4. 요청 자료 목록 및 제출 형식

| ID | 자료 | 우선순위 | 권장 형식 |
|---|---|---|---|
| A01 | Converter/Drive 독립 판매 및 EU 공급 답변 | P0 | 서면 답변 + redacted quotation/order evidence |
| A02 | 실제 표준 SKU/옵션 전체 목록 및 코드 정의 | P0 | XLSX/CSV/PDF |
| A03 | EU 공급 국가·수입자·판매 법인·공급 단위 | P0 | 서면 답변 + redacted shipping/sales evidence |
| A04 | 현재 공식 매뉴얼 원본 및 revision history | P0 | 원본 PDF + revision table |
| A05 | iX700M 외형 2D/3D CAD 원본 | P0 | DWG/DXF + STEP |
| A06 | 유닛별 회로도·블록도·BOM 또는 redacted BOM | P1 | PDF + XLSX/CSV |
| A07 | MCU/MPU/DSP/통신/보안 IC 전체 부품번호와 revision | P0 | XLSX/CSV + datasheet |
| A08 | firmware/bootloader/FPGA 버전 및 update architecture | P1 | PDF/표 |
| A09 | secure boot/debug lock/authentication/crypto/tamper 설정표 | P1 | 체크리스트 + 검증 요약 |
| A10 | SBOM, vulnerability handling, support period, PSIRT | P0 | SPDX/CycloneDX + 정책문서 |
| A11 | 유닛별/조합별 CE·UKCA DoC 및 시험자료 | P0 | 원본 PDF |
| A12 | 자료 미제공 항목과 대체 확인서/NDA 조건 | P0 | 서면 답변 |

원본 파일명은 유지하고 문서번호·revision·발행일·적용 SKU를 표시해 주십시오. 가능하면 각 파일의 SHA-256 또는 제조사 문서관리 식별자를 함께 제공해 주십시오.

## 5. 회신 및 후속 협의 요청

- 질문별 답변 담당부서(설계/기술/품질·인증/영업/해외사업/제품보안)를 지정해 주십시오.
- 비공개 자료에 NDA가 필요하면 귀사의 NDA 양식과 절차를 안내해 주십시오.
- 우선 P0 항목과 A01~A05, A07, A10, A11에 대한 1차 답변 및 제공 가능 자료 목록을 회신해 주십시오.
- 회신이 어려운 질문은 미회신으로 남기지 말고 담당부서·미제공 사유·대체 증거 가능 여부를 표시해 주십시오.
- 질문별로 답변 상태, 근거 문서, 적용 SKU, 담당자 및 예상 회신일을 기입해 주십시오.

## 6. 발송 경로 및 현재 상태

- 공식 국내 서보 영업, 기술지원 및 해외 문의 경로는 별도 문서 `reports/LS_MECAPION_IX700M_INQUIRY_DISPATCH_GUIDE_2026-11-24.md`에 기록한다.
- 회사명·발신 담당자·회사 소재지·실제 수신 담당부서 확인 후 발송한다.
- 현재 상태: `draft_prepared_not_sent`. 발송·접수번호·제조사 회신은 확인되지 않았다.
- 제조사 원본 binary를 확보하기 전까지 매뉴얼·DoC·카탈로그·CAD의 파일 본문/서명/hash 검증 완료라고 주장하지 않는다.
- Actual SKU, EU/EEA supply, economic operators, signed DoC coverage, BOM/exact MCU/SBOM, security configuration, CRA classification, vulnerability handling 및 security update/support period는 Unknown으로 유지한다.

CRA only; SIL 3 excluded.
