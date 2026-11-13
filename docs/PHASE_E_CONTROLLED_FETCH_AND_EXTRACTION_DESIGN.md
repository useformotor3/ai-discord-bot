# Phase E 설계 제안 — 통제된 공식 출처 수집 및 추출 품질 검증

- 기준일: 2026-11-13
- 상태: **DESIGN ONLY — 구현 승인 대기**
- 대상 브랜치: `cra-project-foundation`
- 기준 HEAD: `1b543af653435a25f89feea7f80abdf370ecda7f`
- 선행 단계: Phase A–D 구현 및 mock/fixture CI 검증 완료
- 운영 통합: 범위 밖
- 실 URL 접속: 본 설계 작성 중 수행하지 않음
- Gemini API 호출/과금 설정 변경: 수행하지 않음

## 1. 목적과 완료 기준

Phase E의 목적은 Phase A–D의 mock/fixture 검증을 넘어, 공식 출처의 실제 응답과 추출 결과가 재현 가능하고 검토 가능한지 확인할 준비를 하는 것이다. 단, 실제 URL fetch는 연결 목적지 검증이 구현·시험되고 별도 승인된 뒤에만 수행한다.

완료 조건:
1. DNS 사전검사와 실제 TCP 연결 목적지가 동일한 검증 IP로 고정된다.
2. TLS SNI 및 인증서 호스트 검증은 원래 allowlist hostname을 기준으로 유지된다.
3. 모든 A/AAAA 결과를 검사하며 비공인/특수 목적지 혼합 응답은 fail-closed 처리한다.
4. 리다이렉트·재시도·대체 IP 연결에도 동일한 정책을 적용한다.
5. 기존 source_id registry, MIME/status/byte/timeout/hash 제한과 Phase B parser 입력 경계가 유지된다.
6. 오프라인 adversarial 테스트가 통과하고 보호 파일 SHA가 불변임을 확인한다.
7. 별도 승인 후 최소 출처 세트에서 실제 fetch/extraction을 수행하고, 원문 보존·문서 버전·추출 품질 차이를 검토한다.
8. 모든 결과는 source hash, extractor version, fetch timestamp, source_id 및 정확한 검토 범위와 연결된다. 법령 의미/제품 적용성은 자동 VERIFIED로 승격하지 않는다.

## 2. 현재 구현의 확인된 상태와 위험

### 2.1 Phase A fetcher

현재 `source_evidence.py`는 고정 source registry 7개를 사용한다. 모델/호출자가 임의 URL을 제공하지 않고 source_id만 지정한다. HTTPS, 정확한 hostname, 443 포트, URL credentials/fragment 차단, 동일 호스트 리다이렉트 제한, 자동 리다이렉트 비활성화, timeout, MIME, HTTP 200, 응답 크기, SHA-256 및 메타데이터 기록이 구현되어 있다.

**잔여 핵심 위험 — DNS TOCTOU:**
- `_validate_https_target()`가 `socket.getaddrinfo()` 결과의 공인 IP 여부를 사전 검사한다.
- 이후 `requests.Session.get()`은 hostname을 이용해 연결하며, 검증 때와 다른 DNS 조회/응답을 사용할 수 있다.
- 따라서 검증된 IP에 실제 TCP 연결을 고정하는 보장이 없다. 사전검사만으로 DNS rebinding/TOCTOU가 제거되었다고 볼 수 없다.
- 현재 테스트는 resolver와 HTTP session을 mock으로 주입한다. 실제 socket 연결 IP, SNI 및 인증서 호스트 검증의 결합을 입증하지 않는다.

### 2.2 Phase B extraction

- HTML visible text/title, EUR-Lex XML 구조 후보, HTML 텍스트 locator 후보, PDF 페이지 텍스트 adapter가 구현되어 있다.
- XML DTD/entity 선언 거부, source_id 확인, 입력/텍스트/페이지 제한, raw/text SHA-256이 있다.
- PDF는 optional pypdf backend이며 현재 CI는 fake reader만 사용한다. OCR/스캔 PDF는 미지원이다.
- 실제 EUR-Lex serialization 및 실제 ST/TI HTML/PDF에 대한 추출 충실도는 미검증이다.
- locator는 구조/페이지 후보이며 법적 위치의 VERIFIED 판정이 아니다.

### 2.3 Phase C/D

- Phase C는 fetch/extraction provenance와 bounded excerpt/Evidence ID를 연결한다.
- Phase D는 동일 raw bytes와 extraction 결과에서 bundle을 재구성하고 exact excerpt/context 및 human-review packet을 검증한다.
- 이들 검사는 publisher authenticity, PDF 시각적 충실도, 의미적 주장 지지, 법령 해석 또는 제품 적용성을 자동 증명하지 않는다.

## 3. 제안하는 단계와 승인 게이트

### E0 — 설계/위협 분석 (현재 단계)

- 기존 fetcher, parser, bundle 및 quote validator 경계 확인.
- DNS TOCTOU, 리다이렉트, 다중 A/AAAA, TLS hostname 검증, proxy 환경, 응답 크기/압축, parser fidelity 위험을 명시.
- 코드 변경 및 live fetch 없음.

### E1 — 연결 IP 고정 transport 구현 (별도 명시 승인 필요)

권장 방향:
1. source_id registry에서 얻은 고정 URL/hostname만 transport에 전달한다.
2. 연결 직전 DNS A/AAAA 전체를 조회하고 모든 응답을 IP parser로 정규화한다.
3. loopback/private/link-local/multicast/reserved/unspecified 및 기타 비공인 주소가 하나라도 섞이면 요청 전체를 거부한다. IPv4-mapped IPv6 및 특수 IPv6 전환/번역 범위도 명시적으로 검사한다.
4. 검증된 IP 중 하나를 선택해 TCP 연결 목적지를 고정한다. 재시도는 해당 요청에서 검증된 IP 집합만 사용하거나 새 DNS 결과를 다시 검증한 뒤 수행한다.
5. HTTP Host 헤더, TLS SNI, 인증서 hostname 검증은 원래 공식 hostname을 유지한다. IP 주소를 인증서 검증 대상으로 바꾸거나 TLS 검증을 끄지 않는다.
6. 자동 proxy 환경변수 사용은 계속 비활성화한다. 별도 proxy를 사용할 경우 목적지 IP를 proxy 측에서 강제 검증하지 않는 한 허용하지 않는다.
7. 자동 redirect는 계속 비활성화한다. 각 redirect hop마다 URL scheme/host/port와 새 DNS 응답을 다시 검증하고, 등록된 동일 hostname만 허용한다.
8. connect/read timeout, 총 응답 byte cap, Content-Length 및 streaming cap, MIME/status 검사, response close, 오류 코드 sanitization을 유지한다.

구현 방식은 기존 requests/urllib3 버전과 호환되는 custom transport/adapter를 우선 검토하되, 내부 API 의존성이 과도하거나 TLS 검증을 정확히 보존하지 못하면 채택하지 않는다. 대안으로 검증된 egress proxy/network enforcement를 검토할 수 있으나, 비용·운영 의존성·실제 정책 강제 가능성을 확인하기 전에는 전제하지 않는다.

### E2 — 오프라인 adversarial transport 검증 (E1과 같은 승인 범위 또는 별도 승인)

필수 mock/integration cases:
- DNS 응답의 A/AAAA 중 하나라도 비공인 주소인 혼합 응답
- 사전 DNS 검사 후 연결 단계에서 다른 주소를 반환하려는 rebinding 시도
- 검증 IP로 TCP 연결이 이루어지는지 확인
- 원래 hostname이 HTTP Host/SNI/certificate verification에 유지되는지 확인
- 잘못된 인증서, hostname mismatch, 만료/신뢰되지 않는 인증서 거부
- redirect to other host, scheme downgrade, nonstandard port, redirect loop 거부
- same-host redirect hop마다 재검증
- retry/fallback이 검증되지 않은 주소를 사용하지 않는지 확인
- IPv4-mapped IPv6, IPv6 ULA/link-local/multicast, NAT64 well-known prefix 및 reserved address 거부
- DNS timeout/empty/invalid response, connect timeout, read timeout, truncated body, oversized body, invalid Content-Length, MIME mismatch, non-200, empty response
- response resource close와 sanitized error 확인
- 기존 Phase A–D 회귀 테스트 및 strict archive audit

TLS/연결 목적지 테스트는 fake session 호출 인자만 확인하는 테스트로 대체하지 않는다. 로컬 loopback TLS fixture를 사용하되, 해당 fixture 주소는 테스트 전용 경로에서만 허용하고 production allowlist/transport 정책을 우회하지 않도록 분리한다.

### E3 — 실제 공식 출처 fetch 및 추출 품질 검증 (별도 명시 승인 필요)

E1/E2 통과 후에도 별도 승인을 받은 경우에만 수행한다.
- 첫 배치는 법령 EUR-Lex XML/HTML 중 가능한 canonical 형태 1개와, 문서 구조가 다른 제조사 자료 1개를 우선한다.
- TI PDF는 pypdf 설치/사용 허용 및 실제 PDF 추출을 별도 확인한다. OCR은 현재 범위에 포함하지 않는다.
- ST/TI 자료는 registry revision과 실제 내려받은 문서 표지/문서번호/revision/date가 일치하는지 확인한다. URL 경로명만으로 revision 일치를 추정하지 않는다.
- 응답이 HTML challenge, login/consent, redirect landing page, viewer shell 또는 문서가 아닌 오류 페이지면 성공 문서로 취급하지 않고 BLOCKED/UNEXPECTED_DOCUMENT로 분류한다.
- 원문 bytes는 메모리에서만 처리한다. 공개 저장소에는 원문 전체, 전체 extracted text, 비공개 자료를 커밋하지 않는다. 저장 후보는 URL, publisher, document ID/revision, timestamp, MIME, byte count, SHA-256, extractor version, bounded excerpt 및 검토 결과로 제한한다.
- 법령 XML/HTML 결과는 같은 조항/항/점의 구조, 제목, 주변 문맥 및 본문 텍스트를 공식 EUR-Lex 페이지와 수동 대조한다.
- PDF 결과는 페이지별 텍스트 추출과 문서 표지/목차/선정 페이지의 시각적 원문을 비교한다. 텍스트 추출 성공만으로 표/각주/수식/다단 레이아웃 충실도를 확정하지 않는다.
- Pass A/B/C 및 사람 검토를 기록한다. URL fetch 성공은 claim VERIFIED를 의미하지 않는다.

## 4. 파일별 제안 diff와 범위

E1/E2 구현 승인 시 예상 변경 후보:
- 신규 `source_transport.py`: 연결 시점 DNS 검증 및 IP-pinned TLS transport.
- 수정 `source_evidence.py`: 기본 transport를 새 adapter에 연결하고 기존 source_id API/metadata/error contract 유지.
- 신규 `tests/test_source_transport.py`: DNS/IP/TLS/redirect/retry adversarial 테스트.
- 필요 시 수정 `tests/test_source_evidence.py`: 새 transport와 fetcher 통합 회귀.
- 신규 `docs/PHASE_E_IMPLEMENTATION.md`: 실제 변경, 테스트, CI SHA, 잔여 한계 기록.

E3 실제 fetch 승인을 받은 경우 추가 변경 후보:
- `docs/PHASE_E_LIVE_SOURCE_VALIDATION.md`: 실제 fetch별 source ID, timestamp, status, MIME, byte count, hash, revision 확인, 추출 품질/수동 대조 결과 기록.
- 필요한 경우 기존 registry metadata 수정은 diff/근거를 먼저 제시하고 별도 승인받는다.

**이번 설계 단계에서는 위 파일들을 생성/수정하지 않는다.** 운영 `main.py`, `.github/workflows/run.yml`, Gemini v2 prompt/contract, model/quota/fallback, production runtime, archive/history/state 및 `main` 브랜치는 변경 대상이 아니다.

## 5. 영향 및 위험 평가

- 긍정 효과: 검사 IP와 실제 연결 IP의 일치 보장, DNS rebinding/TOCTOU 노출 감소, TLS hostname 검증 유지, 실제 official document parser fidelity의 검증 가능성.
- 잔여 위험: OS/network routing, DNS resolver 신뢰, TLS CA store, HTTP library 내부 동작, IPv6 transition/NAT64, 서버 측 콘텐츠 변경, publisher authenticity, 악성/오류 문서, PDF 텍스트 추출 손실.
- 가용성 위험: 공식 CDN이 다수 IP/지역별 주소를 반환하거나 주소가 자주 바뀌면 fail-closed가 정상 문서 수집도 차단할 수 있다. 이 경우 allowlist를 느슨하게 하지 말고 원인과 공식 주소 변경 근거를 확인한다.
- 법적/기술 판단 위험: 추출된 문자열이 정확해도 조항 의미/예외/제품 적용성은 별도 검토가 필요하다.
- 비용: 설계 및 mock tests는 무료. live fetch는 기존 인터넷 접속만 사용하며 paid API/service/account upgrade는 금지. 예상치 못한 로그인/유료 다운로드/요금 안내가 나오면 즉시 중단한다.

## 6. 성공 기준 및 중단 조건

성공:
- 모든 E1/E2 adversarial tests와 전체 회귀 테스트 통과.
- exact tested HEAD의 GitHub Actions 성공 로그에 테스트 개수와 strict archive audit 결과가 명시됨.
- protected files SHA 불변 확인.
- E3 승인 후 source metadata/hash/revision이 일관되고, 수동 비교 결과/추출 손실이 문서화됨.

즉시 중단:
- 실제 연결 IP를 검증된 IP로 고정할 수 없음.
- TLS SNI/hostname verification을 보존할 수 없음.
- proxy/redirect/retry가 정책을 우회할 수 있음.
- 응답 제한을 강제할 수 없음.
- 문서 revision/identity를 확정할 수 없음.
- 유료 접근/서비스/계정 업그레이드가 필요함.
- protected file 또는 production behavior 변경이 필요해짐.

## 7. 백업 및 롤백

- 구현 전 현재 branch HEAD와 대상 파일 SHA를 기록한다.
- 새 transport를 독립 모듈로 구현하고 기존 fetcher 변경은 최소화한다.
- 기존 Phase A–D mock tests를 baseline으로 유지한다.
- 회귀 시 작업 브랜치의 해당 Phase E commit만 revert한다. force push, main merge/rebase/sync, archive 원본 변경은 하지 않는다.
- E3에서 수집한 원문 bytes는 영속 저장하지 않으므로 원문 재배포/삭제 작업은 발생하지 않는다.
- rollback 이후 기존 mock-only 상태로 되돌아갔음을 tests/CI로 확인한다.

## 8. 검토 결과 및 승인 요청

현재 판정:
- Phase A–D mock/fixture 구현: 완료 기록 및 CI 근거 존재.
- DNS TOCTOU: **OPEN — live fetch 차단 조건**.
- 실제 EUR-Lex/ST/TI fetch: NOT RUN.
- 실제 PDF backend/pypdf: CI에서 미검증.
- OCR: 미지원.
- 제품별 법령 적용성/MCU 부품 기능: 기존 UNVERIFIED 유지.

**요청하는 승인 범위는 E1 + E2의 작업 브랜치 전용 구현 및 오프라인 테스트뿐이다.**
실제 URL 접속(E3), Gemini API 호출, production integration, protected file 변경, 비용 발생, main merge/rebase/sync는 이 승인 요청에 포함되지 않는다. E1/E2 구현과 CI 검증 결과를 보고한 뒤 E3는 별도 승인받는다.
