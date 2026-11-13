# C1+C2 구현 결과 및 검증 기록

- 기준일: 2026-11-13
- 구현 범위: 승인된 C1 + C2만
- 브랜치: \`cra-project-foundation\`
- 상태: **구현 완료 후보 / 전체 CI 및 최종 코드 검토 대기**
- 외부 공식 URL fetch: NOT RUN
- production integration: NOT IMPLEMENTED

## 변경 사항

### C1 — 엄격한 추출 무결성 및 품질 진단
- \`source_extraction.py\` 버전 1.1.0.
- HTML/XML 텍스트 디코딩에서 무조건적인 replacement fallback 제거.
- UTF-8 기본, 명시적 BOM/문서 charset 선언만 엄격하게 디코딩. 실패하면 \`CHARSET_DECODE_FAILED\`.
- replacement 문자 수를 결과 metadata에 기록하며 현재 strict 경로에서는 0만 허용.
- PDF page_count, empty_page_count, quality_status를 추가.
- 빈 페이지가 일부 있으면 PARTIAL_TEXT, 모든 페이지가 비어 있으면 REVIEW_REQUIRED, 텍스트가 있더라도 TEXT_EXTRACTED_NOT_VISUALLY_VERIFIED로 시각 검증 미완료를 명시.

### C2 — Evidence Bundle
- \`source_bundle.py\` 추가.
- fetch raw hash, extraction raw hash, normalized text hash가 일치하지 않으면 bundle 생성 차단.
- source_id 불일치 차단.
- expected/observed document identifier 및 revision을 분리.
- 원문에서 식별정보·Revision을 찾지 못하면 IDENTITY_UNCONFIRMED.
- 관측 revision이 다르면 REVISION_MISMATCH.
- 식별정보와 revision 둘 다 일치하면 IDENTITY_AND_REVISION_MATCHED. 이는 문서 식별정보의 문자열 대조 결과일 뿐, 발행기관 진위나 문서 전체의 시각적 충실도 인증은 아님.
- 조항/구조 locator 후보에 한해 excerpt 최대 500자, 최대 100건을 저장. 전체 원문 및 전체 추출 텍스트는 bundle에 포함하지 않음.
- \`schemas/source_evidence_bundle.schema.json\` 계약 추가.
- deterministic evidence_id 및 excerpt SHA-256.

## 테스트

추가한 테스트:
- invalid UTF-8 byte sequence 거부
- 선언된 Windows-1252 strict decode
- PDF 빈 페이지 진단
- source bundle raw/text hash linkage
- source_id mismatch 차단
- 문서 식별정보 및 revision mismatch/unconfirmed
- excerpt hash/길이 상한

## 중요한 제한

- CI가 아직 최종 SHA에서 성공하기 전까지 통과를 주장하지 않는다.
- 실제 EUR-Lex/ST/TI 자료를 가져오지 않았으므로 실제 publisher revision parser의 recall/precision은 미검증.
- generic HTML parser는 표·각주·동적 렌더링·숨김 콘텐츠를 완전하게 보존한다고 보장하지 않는다.
- PDF text extraction은 시각적 페이지 검증을 대체하지 않는다.
- identity string match는 서명·발행자 인증이 아니다.
- bundle은 현재 non-production library이며 report builder/claim validator와 아직 연결되지 않았다.

## 다음 검증

1. 전체 unittest suite + strict archive audit CI.
2. JSON schema parsing/validation test 추가 여부 검토.
3. EUR-Lex/ST/TI real-document fixture는 E3 별도 승인 후에만 확보.
4. C3 adapter/PDF backend는 C1+C2 검증 종료 후 별도 계획.
5. C5 report integration은 bundle contract가 안정된 뒤 non-production path로 제안.

