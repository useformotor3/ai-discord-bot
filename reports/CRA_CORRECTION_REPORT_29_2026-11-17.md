# CRA 보고서 #29 정정 — 보안 로깅과 CVD 조항의 분리

- 원본: research_archive/2026-11-17_123050749049_db1988ac.md
- 원본 blob SHA: 499be639d1a37729d63b78a053bbc1f4b2ab4b08
- 원본 보존: 수정·삭제하지 않음

## 정정 사항
1. CVD는 Annex I Part II (5)/(6)이며 Part I이 아니다.
2. 보안 관련 내부 활동의 기록·모니터링은 Annex I Part I (2)(l)이다. relevant internal activity 중 data/services/functions에 대한 access 또는 modification을 포함하고 사용자 opt-out mechanism을 요구한다.
3. 데이터·명령·프로그램·구성의 무결성은 별도 조항 Annex I Part I (2)(f)다.
4. “모든 무단 접근·설정 변경 이벤트를 변조 불가능하게 저장”, “forensics 가능한 immutable local logs”, “원격 telemetry 유출 방지”는 CRA의 직접 문언이 아니다. 이벤트 분류, 보존기간, WORM 저장, SIEM 전송, OT 로컬 저장은 risk-based 설계 선택으로 문서화한다.
5. Annex I Part I (2)는 Article 13(2)의 제품 위험평가를 바탕으로 where applicable 적용된다.

## 수정 권고 문안
제품은 위험평가에 따라 Annex I Part I (2)(l)의 보안 관련 내부 활동을 기록·모니터링하고, data/services/functions 접근·변경 활동을 포함하며 사용자 opt-out mechanism을 제공한다. 로그 무결성, 보존기간, 이벤트 taxonomy, 원격 전송, SIEM 연계 및 OT 네트워크 분리는 위험평가를 근거로 설계하되 CRA 직접 인용과 구현 권고를 구분한다. CVD 정책은 Part II (5)/(6)로 별도 관리한다.

## 공식 근거
- Article 13(2)–(4)
- Annex I Part I (2)(f), (l); Part II (5)–(6)
- https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng
