# CRA 보고서 #8 정정 및 SBOM 기술문서·사용자 제공 근거 감사

- 감사 대상 원본: research_archive/2026-11-17_094748528255_b92e6d0d.md
- 원본 blob SHA: 38550036503c8d2dbb00e66a7625475e089b4cd7
- 원본 보존: 완료. 원본 archive는 수정·삭제하지 않는다.
- 기준: Regulation (EU) 2024/2847, Official Journal OJ L 2024/2847, 20.11.2024.

## 1. 판정 요약

| 원본 주장/인용 | 판정 | 정정 |
|---|---|---|
| SBOM을 기계 판독 형식으로 작성 | 방향은 맞음 | Annex I Part II (1)은 commonly used machine-readable format, 최소 top-level dependencies를 요구 |
| 모든 SBOM을 사용자에게 제공해야 함 | 오류 | Annex II point 9는 제조사가 SBOM을 사용자에게 제공하기로 결정한 경우 접근 위치를 안내하도록 함. 일반적인 의무 제공 조항이 아니다 |
| SBOM 근거가 Annex VI | 조항 오류 | Annex VI는 simplified EU declaration of conformity. SBOM은 Annex I Part II (1), Annex VII 2(b)/8, Annex II point 9와 연결 |
| 모든 open-source/commercial/transitive component의 상세 버전·관계를 SBOM에 반드시 전부 포함 | 범위 과장 | component 식별·문서화와 SBOM 최소 top-level dependency 범위를 구분. 법령의 최소 SBOM 범위는 top-level dependencies |
| 모든 servo drive가 Important Class I/II | 제품 분류 오류 | Annex III 목록의 실제 제품 기능/범주 정의에 따라 분류. servo drive라는 이름만으로 자동 분류 불가 |
| Raw Text Quote가 최종 OJ 직접 인용 | 비문언 인용 | 원본 문구의 open-source, version, support-period 등 결합 표현은 Annex I Part II (1)의 verbatim text가 아니다 |

## 2. 정확한 법적 근거

- Annex I Part II (1): 제품 내 vulnerabilities 및 components를 식별·문서화하고, commonly used machine-readable format의 SBOM을 작성한다. SBOM은 최소 top-level dependencies를 포함한다.
- Annex VII point 2(b): technical documentation에는 vulnerability handling process의 필요한 정보/사양이 포함되며, SBOM, CVD policy, contact address 제공 증거, secure update distribution 기술 솔루션을 포함한다.
- Annex VII point 8: 해당되는 경우, 시장감시기관이 essential cybersecurity requirements 준수 확인에 필요하다고 판단해 reasoned request를 한 경우 SBOM을 제공한다.
- Annex II point 9: 제조사가 SBOM을 사용자에게 제공하기로 결정한 경우, SBOM 접근 위치 정보를 제공한다. 사용자에게 SBOM을 반드시 제공하라는 일반 의무가 아니다.
- Annex VI: simplified EU declaration of conformity 양식이며 SBOM 요구 조항이 아니다.
- Annex III: Important products Class I/II의 분류 목록. 서보 드라이브가 특정 범주에 해당하는지 실제 제품 기능으로 판단해야 한다.

## 3. 수정된 권고 문안

제조사는 제품 내 취약점 및 구성요소를 식별·문서화하고, commonly used machine-readable format으로 최소 top-level dependencies를 포함하는 SBOM을 작성해야 한다(Annex I Part II (1)). SBOM과 취약점 처리 절차, CVD 정책, 연락 주소 및 secure update distribution 설명은 Annex VII technical documentation에 포함한다(Annex VII 2(b)). 시장감시기관의 reasoned request 등 Annex VII point 8의 조건에 해당하면 SBOM을 제공한다. 사용자에게 SBOM을 공개하는 경우에는 Annex II point 9에 따라 접근 위치를 안내한다. 이들 조항을 “모든 사용자에게 모든 component/version SBOM을 항상 제공”하는 의무로 확대하지 않는다.

## 4. 서보 드라이브 적용 시 권고

- 제품의 firmware, RTOS, bootloader, protocol stack 및 third-party libraries를 실제 구성 기준으로 식별.
- SBOM은 minimum top-level dependency coverage를 충족하고, 취약점 분석 효율을 위해 transitive dependencies까지 확장할 수 있다.
- SBOM과 firmware build/release, hardware revision, product variant를 내부 configuration management에서 연결.
- 기술문서 패키지에는 SBOM, vulnerability handling process, CVD policy, contact address evidence, secure update distribution design을 traceable하게 포함.
- 사용자 공개 여부는 정보보안·영업비밀·공급망 정책과 Annex II point 9를 고려해 별도 결정.

## 5. 공식 출처

- Official Journal: https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
- EUR-Lex consolidated text (documentation tool): https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng
