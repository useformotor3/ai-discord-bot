# CRA 보고서 #9 정정 및 SBOM 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_095530240241_c854bd06.md
- 원본 blob SHA: 98e58f3a89ad7c9b2c8e30cea04f11fabb7d725f
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장 | 판정 | 정정 |
|---|---|---|
| Annex I Part II (1) SBOM 인용 | 대체로 정확 | 최종 OJ는 제품 내 vulnerabilities/components를 식별·문서화하고, SBOM은 commonly used machine-readable format으로 최소 top-level dependencies를 포함하도록 규정 |
| 모든 transitive dependency를 SBOM에 반드시 포함 | 법적 최소범위 초과 | 최소 범위는 top-level dependencies. 더 깊은 dependency까지 포함하는 것은 공급망 위험관리상 권고/선택 |
| SPDX/CycloneDX 형식 의무 | 형식 과장 | 법령은 commonly used and machine-readable format을 요구하지만 두 포맷을 직접 지정하지 않는다 |
| RTOS/필드버스/암호 라이브러리 모두 SBOM에 포함해야 한다는 예시 | 제품별 적용성 필요 | 실제 제품에 포함된 component는 식별 대상이지만 특정 vendor, protocol 또는 library를 법령이 지정하지 않는다 |
| 취약점 공개 즉시 패치 및 고객 통지 | 시점/의무 과장 | Annex I Part II (2)는 vulnerabilities를 without delay 처리, (4)는 security update available 이후 fixed-vulnerability 정보를 공유·공개하며 정당한 지연 예외를 둔다 |
| 하드웨어 리비전별 SBOM 추적 | 법령의 직접 문언 아님 | product/build/configuration 관리에 유용한 엔지니어링 권고로 분류 |

## 2. 정확한 법적 근거

- Annex I Part II (1): 제조사는 제품에 포함된 vulnerabilities 및 components를 식별·문서화해야 하며, commonly used and machine-readable format의 SBOM을 작성한다. SBOM은 최소한 top-level dependencies를 포함한다.
- Annex I Part II (2): 제품 위험에 비례해 취약점을 지체 없이 해결·완화하고, 기술적으로 가능한 경우 새로운 security update를 functionality update와 분리한다.
- Annex I Part II (4): security update가 available된 뒤 fixed vulnerabilities에 대한 정보를 공유·공개한다. 정당한 경우 publication의 security risk가 security benefit보다 크면 사용자가 patch를 적용할 기회를 얻은 뒤 공개를 지연할 수 있다.
- Annex I Part II (6): third-party components의 잠재 취약점 공유를 촉진하고 제보 연락 주소를 제공한다.

## 3. 수정된 권고 문안

제조사는 제품에 포함된 vulnerabilities와 components를 식별·문서화하고, commonly used machine-readable format으로 최소 top-level dependencies를 포함하는 SBOM을 작성해야 한다(Annex I Part II (1)). SPDX/CycloneDX는 가능한 포맷 후보이며 법령이 특정 포맷을 직접 지정하지 않는다. 더 깊은 transitive dependency, firmware build, hardware revision 및 product variant와 SBOM을 연결하는 것은 취약점 영향 분석의 효율을 높이는 구현 권고다. 취약점 처리는 Part II (2)의 without delay 기준을 적용하고, fixed-vulnerability 공개는 Part II (4)의 시점과 예외를 따른다.

## 4. 서보 드라이브 적용 시 권고

- SBOM은 MCU firmware, RTOS, protocol stack, bootloader, cryptographic libraries, third-party binaries 등 실제 포함 component와 version을 식별.
- minimum top-level dependency coverage를 baseline으로 삼고, 제품 위험·공급망·업데이트 전략에 따라 transitive dependency까지 확장.
- SBOM과 firmware build ID, hardware revision, product variant, release date를 내부 configuration management에서 연결.
- 공개 취약점이 제품에 실제 포함되었는지, 빌드 옵션/기능 사용 여부/노출 인터페이스를 포함해 영향 분석.
- 취약점 공개와 patch timing은 Part II (4)의 예외 및 Part II (2)의 remediation 요구를 구분.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
