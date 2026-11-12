# CRA 서보 드라이브 개발 프로젝트 — 상황판

> 기준 저장소: useformotor3/ai-discord-bot  
> 기준 작업 브랜치: cra-project-foundation  
> 기준 확인일: 2026-11-12  
> 프로젝트 목적: CRA를 처음 접하는 개발자도 서보 드라이브 개발에 적용할 수 있는 근거 기반 실무 지침과 통합 보고서를 구축한다.

## 현재 상태
- 프로젝트: CRA 전용. SIL 3 벤치마킹은 범위에서 제외.
- 저장소 공개 상태: Public 유지 결정. 공개 자료만 저장하며 비밀정보/비공개 설계자료 금지.
- 우선 MCU: STMicroelectronics (정확한 부품 번호 미확정). TI는 비교·참고.
- 독자: CRA를 모르는 서보 드라이브 개발자.
- 기본 문서: START_HERE 및 docs 운영 문서 존재. 각 문서는 지속적으로 개선 가능.
- 기존 자료: cra-project-foundation 브랜치 archive 984개, history 984개. file 경로 984개 전부 존재·유일. main 브랜치 archive는 989개로 5개 차이 확인.
- 브랜치 정합성: 5개 추가 archive의 main 유입 시점/의도 및 main history 연결은 미확인. [REPOSITORY_RECONCILIATION.md](REPOSITORY_RECONCILIATION.md)
- 내용 검증: 초기 표본 감사에서 조항 인용·직접 인용·제품 분류 오류 발견. 기존 archive 전수 검증 미완료.
- 자동화: main.py는 실패 메시지를 성공으로 처리할 위험, 출처 자동 검증 부재, 프로젝트 문서 문맥 미사용, timeout/HTTP 확인 부족. 운영 신뢰성 개선 필요.
- 자동 실행: 현재 run.yml에는 workflow_dispatch/repository_dispatch만 확인. cron 미구현.
- 보고서: 법령 기준선과 통합 보고서 골격 존재. 제품별 적용성 및 ST MCU 기능 분석은 미완료.

## 확정 운영 규칙
1. 모든 신규 세션/작업 시작 시 START_HERE.md와 AI_RULEBOOK, 상황판, 계획서, 지식 인덱스, 통합 보고서, 최근 세션 로그를 먼저 읽는다.
2. 현재 GitHub 원본과 대조하지 않은 과거 기록·대화 기억·AI 답변을 사실로 재사용하지 않는다.
3. 근거, 원문 위치, 확인일, 검증 상태가 없는 핵심 주장은 확정 보고서에 넣지 않는다.
4. 실패/오류/실패한 시도도 기록하고 재발 방지 조치를 만든다.
5. 문서뿐 아니라 폴더 구조·스키마·자동화 코드까지 개선 대상으로 삼는다.
6. 작업 후 변경 파일을 다시 읽고 검증한 뒤 SESSION_LOG와 상황판/계획을 갱신한다.
7. Public 저장소에는 공개 자료만 저장하고 유료 전환은 금지한다.

## 다음 우선 작업
- [ ] main과 cra-project-foundation의 공통 조상 및 커밋 그래프 비교
- [ ] main의 history.json/state.json 정합성 확인
- [ ] main에만 있는 archive 5개 조사 및 이관 필요성 판단
- [ ] 재현 가능한 archive/history 인벤토리 스크립트 추가
- [ ] main.py의 실패 처리·근거 필드·timeout·HTTP 오류·비밀정보 처리 개선 설계
- [ ] 기존 자료 984개 주제 분류 및 주장/출처 추출
- [ ] CRA 법령/공식기관 기준선 재검증
- [ ] 서보 드라이브 기능 기반 적용성 매핑
- [ ] ST MCU 정확한 파트넘버 확보 후 부품별 보안 기능 확인
- [ ] TI 비교 분석
- [ ] 개발 실무 통합 보고서 완성

## 상태 표기
VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED / CONFLICT / OUTDATED / NOT_APPLICABLE

## 주요 문서
- [시작점](../START_HERE.md)
- [AI 행동강령](AI_RULEBOOK.md)
- [마스터 계획](MASTER_PLAN.md)
- [지식 인덱스](KNOWLEDGE_INDEX.md)
- [통합 보고서](MASTER_REPORT.md)
- [초기 감사](INITIAL_AUDIT.md)
- [법령 기준선](CRA_LEGAL_BASELINE.md)
- [브랜치 정합성 감사](REPOSITORY_RECONCILIATION.md)

마지막 갱신: 2026-11-12
