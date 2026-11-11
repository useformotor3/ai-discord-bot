# 1차 저장소 및 자료 품질 감사

**감사일:** 2026-11-12  
**대상:** main 브랜치의 기존 CRA 조사 아카이브, history/state, main.py, 공식 CRA 원문  
**감사 범위:** 전체 985개 파일의 개별 주장 전수 검증이 아닌, 저장소 인벤토리와 대표 문서의 표본 대조  
**상태:** 초기 감사 / 추가 전수 검증 필요

## 1. 저장소 인벤토리

확인 시점의 main 브랜치 기준:
- `research_archive/`: Markdown 985개
- `history.json`: 항목 985개
- history의 각 `file` 경로가 archive 파일과 일치: 985/985
- 중복 file 경로: 0
- `state.json`: date=2026-11-11, count=279
- `main.py`: Gemini 조사, 최근 history snippet 5개를 프롬프트에 포함, Discord 전송, archive/history/state 저장, Git commit/push 로직
- `.github/workflows/run.yml`: workflow_dispatch 및 repository_dispatch 트리거 확인. cron 예약 실행 없음.

주의: `state.json`의 count는 날짜가 바뀌면 0으로 초기화되는 일일 카운터다. 누적 아카이브 수로 해석하면 안 된다. 과거의 count 275/279는 전체 보고서 수가 아니다.

## 2. 대표 문서에서 발견한 근거 오류

### Finding CRA-AUD-001 — 무료 보안 업데이트 조항 위치 오류
- 파일: `research_archive/2026-11-11_234543.md`
- 기존 주장: 무상 업데이트 및 안전한 배포 근거를 Annex I Part I, Section 2로 제시
- 공식 원문 대조:
  - Annex I Part I, point (2)(c)는 취약점을 보안 업데이트로 해결할 수 있어야 하고, 해당되는 경우 자동 보안 업데이트를 기본 활성화하는 등의 요구를 다룬다.
  - 보안 업데이트의 안전한 배포 메커니즘은 Annex I Part II, point (7)에 규정되어 있다.
  - 보안 업데이트의 지체 없는 제공 및 원칙적인 무상 제공은 Annex I Part II, point (8)에 규정되어 있다. 단, 맞춤형 제품에 관한 제조자와 기업 사용자 간 별도 합의 예외 문구가 있다.
- 판정: 조항/파트를 혼동한 부정확한 인용. 본문 수정 필요.
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 근거 위치: Annex I, Part I points (1)-(2), Part II points (1)-(8).

### Finding CRA-AUD-002 — 원문 인용으로 표시된 문구의 정확성 미확인
- 파일: `research_archive/2026-11-11_234543.md`
- 기존 주장: Annex I Part I, Section 2의 영문 문장을 따옴표로 인용
- 문제: 공식 원문에서 확인되는 실제 구조/문구와 일치하지 않는 복합 문장으로 보인다. 공식 법령의 직접 인용으로 사용할 수 없다.
- 판정: UNVERIFIED quote. 공식 원문과 문자 단위 대조 전까지 직접 인용으로 재사용 금지.
- 조치: 원문 인용은 공식 문서에서 정확히 복사하고 조항·항·점 위치를 병기한다. 해설·요약은 인용부호 없이 별도 표기한다.

### Finding CRA-AUD-003 — 취약점 신고 조항 번호 오류
- 파일: `research_archive/2026-11-11_232532.md`
- 기존 주장: 24시간 조기 경보 의무의 근거를 Article 11로 표시
- 공식 원문 대조: CRA Article 11은 General product safety이고, 제조자의 actively exploited vulnerability 및 severe incident 신고 의무는 Article 14에 규정되어 있다.
- 세부: Article 14(2)(a)는 actively exploited vulnerability 조기 경보를 인지 후 24시간 이내, 14(2)(b)는 취약점 신고를 72시간 이내 제출하도록 규정한다. severe incident에도 별도 24시간/72시간 및 최종 보고 일정이 있다.
- 판정: 24시간이라는 일부 내용은 맞지만 조항 번호와 의무 설명을 수정해야 한다.
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

### Finding CRA-AUD-004 — 서보 드라이브의 Important Class I/II 자동 분류 단정
- 파일: `research_archive/2026-11-11_232532.md`
- 기존 주장: 서보 드라이브가 Important Product Class I 또는 II에 포함된다고 일반화
- 문제: 제품 이름만으로 중요 제품 등급을 단정할 수 없다. CRA Article 7 및 Annex III의 제품 범주·핵심 기능과 Commission Implementing Regulation (EU) 2025/2392의 기술적 정의를 제품 전체의 핵심 기능에 대조해야 한다. 개별 MCU 부품의 범주 해당 가능성과 완제품 서보 드라이브의 분류는 구분해야 한다.
- 판정: 근거 부족한 일반화. 제품별 기능 분석 전에는 UNVERIFIED로 유지.
- 공식 원문:
  - CRA: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
  - Implementing Regulation (EU) 2025/2392: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R2392

### Finding CRA-AUD-005 — 지원기간과 업데이트 무상 제공 근거 혼동
- 파일: `research_archive/2026-11-08_082432.md`
- 기존 주장: Article 13(8)의 직접 인용문으로 무료 보안 업데이트 문장을 제시하고, 별도 배포 의무를 Annex I Part II point (5)로 표시
- 공식 원문 대조:
  - Article 13(8)은 지원 기간을 제품의 예상 사용기간·특성 등을 고려해 정하도록 하며, 원칙적으로 최소 5년(제품 예상 사용기간이 5년보다 짧으면 그 예상 사용기간)을 규정한다.
  - 업데이트의 안전한 배포는 Annex I Part II point (7), 무료 제공은 point (8), 기능 업데이트와 분리 제공(기술적으로 가능한 경우)은 point (2)에 해당한다.
  - Article 13(8)에 적힌 것으로 보이는 기존 따옴표 문장은 공식 조항의 실제 문장과 일치하지 않는다.
- 판정: 조항 위치 및 원문 인용 오류. 수정 필요.
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847

## 3. 적용 시점 기준선 (2026-11-12 확인)
CRA Article 71에 따르면 일반 적용일은 2027-12-11이다. 다만 Article 14의 신고 의무는 2026-09-11부터 적용되고, Chapter IV(Articles 35–51)는 2026-06-11부터 적용된다. 따라서 현 시점의 보고서에서는 'CRA 전체 적용 전'과 '이미 적용 중인 조항'을 구분해야 한다.
- 공식 원문: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847
- 확인 위치: Article 71(2)

## 4. 기존 자동 조사 코드의 품질 위험

파일: `main.py`
1. 생성 프롬프트는 공식 원문과 raw quote를 요구하지만, 생성 결과의 URL·문서 버전·조항 원문 일치 여부를 자동 검증하는 단계가 없다.
2. 모델 호출이 모두 실패해도 경고 문구를 결과로 넣고 `success = True`로 설정한다. 그 결과 실제 조사 실패 메시지가 정상 연구 보고서처럼 Discord로 전송되고 archive/history에 저장될 수 있다.
3. `MAX_DAILY_QUOTA = 1200`은 코드에 고정된 값이다. 실제 모델·계정·API 무료 티어 한도를 보장하는 수치로 확인되지 않았으므로 무료 사용량 보장이나 과금 방지 장치로 간주하면 안 된다.
4. Discord 전송에 timeout 및 HTTP 상태 코드 확인이 없다.
5. 프로젝트의 계획서·행동강령·검증 인덱스 전체를 AI 문맥으로 읽지 않고 최근 history snippet 5개만 사용한다. 따라서 세션 간 프로젝트 운영 맥락과 검증 상태를 충분히 반영하지 못한다.
6. 생성물의 출처 링크가 필수 필드인지 검사하지 않으며, 원문 인용을 공식 원문과 대조하지 않는다.

판정: 현재 자동화는 조사 초안 생성·저장에는 쓸 수 있으나, 검증된 근거 보고서를 자동 생성한다고 볼 수 없다. 검증 파이프라인과 실패 처리 개선이 필요하다.

## 5. 후속 조치
- [ ] 985개 자료 전체의 출처 URL/조항/인용문 추출
- [ ] 공식 원문과 인용문 자동/수동 대조
- [ ] 오류 유형별 집계 및 기존 보고서 정정 이력 작성
- [ ] Article 14 및 시행일 등 최신 법령 기준선 반영
- [ ] Article 7/Annex III/Implementing Regulation 2025/2392에 따른 제품 분류 판단표 작성
- [ ] main.py의 실패 처리, 출처 필드 강제, 검증 전 게시 차단 개선
- [ ] 기존 archive는 원본 보존, 정정본은 별도 파일 또는 명시적 정정 이력으로 관리

## 6. 감사 한계
이번 결과는 저장소 인벤토리와 대표 문서 표본에 대한 초기 감사다. 985개 파일 각각의 주장 전체를 전수 검증한 결과가 아니다. 이 문서에 기재한 오류 사례는 검증이 시작된 일부 표본이며, 다른 문서에 동일하거나 추가적인 오류가 있을 수 있다.
