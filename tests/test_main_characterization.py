"""Phase B: 유효한 보고서만 후속 처리되는지 검증한다."""
import json
from datetime import datetime
from zoneinfo import ZoneInfo

SEOUL = ZoneInfo("Asia/Seoul")

import pytest


VALID_REPORT = """# CRA 심층 조사 보고서

## 1. 주제 요약
산업용 서보 드라이브의 사이버보안 요구사항과 제조자 책임을 정리한다.
제품의 의도된 용도와 위험평가 결과를 기준으로 요구사항 적용성을 판단한다.

## 2. 규격 근거 및 상세 내용
규정 (EU) 2024/2847 Article 13(8)의 제조자 취약점 처리 의무를 원문과 대조한다. [C-001]
실무 검토 시 제품 설계와 개발 단계의 사이버보안 위험평가 여부도 별도 확인 항목으로 둔다. [C-002]
본 설명은 적용성 검토를 위한 조사 초안이며 제품 분류는 별도 확인이 필요하다.

## 3. 출처 자료(Source)
EU 공식 법령 데이터베이스 EUR-Lex, Regulation (EU) 2024/2847.
EUR-Lex consolidated text 20.11.2024; corrigenda 5.12.2024, 2.7.2025 and 17.10.2025.
EUR-Lex 통합본은 문서화 도구이며 법적 효력은 Official Journal(관보) 정본과 공식 정오표에 있다.
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120

## 4. 출처 원문 텍스트(Raw Text Quote)
“Manufacturers shall ensure that vulnerabilities of the product with digital elements, including its components, are handled effectively during the support period.”

CLAIM_EVIDENCE_JSON
```json
{
  "claims": [
    {
      "claim_id": "C-001",
      "category": "legal_requirement",
      "statement": "제조자는 지원 기간 동안 제품 취약점을 효과적으로 처리해야 한다.",
      "source_id": "CRA-2024-2847-consolidated",
      "locator": "Article 13(8)",
      "quote": "Manufacturers shall ensure that vulnerabilities of the product with digital elements, including its components, are handled effectively during the support period."
    },
    {
      "claim_id": "C-002",
      "category": "engineering_recommendation",
      "statement": "제품 설계 및 개발 단계의 사이버보안 위험평가 여부를 별도 확인한다.",
      "basis": "제품 적용성 검토를 위한 엔지니어링 확인 항목이며 이 문장은 독립된 CRA 법적 의무를 주장하지 않는다."
    }
  ]
}
```
"""


def test_successful_generation_uses_only_mocked_external_services(run_main):
    run_main.execute([VALID_REPORT])

    state = json.loads((run_main.workdir / "state.json").read_text(encoding="utf-8"))
    history = json.loads((run_main.workdir / "history.json").read_text(encoding="utf-8"))
    archives = list((run_main.workdir / "research_archive").glob("*.md"))

    assert state["count"] == 1
    assert len(history) == 1
    assert len(archives) == 1
    assert "CRA 심층 조사 보고서" in archives[0].read_text(encoding="utf-8")
    archive_text = archives[0].read_text(encoding="utf-8")
    assert "CRA-2025-327-EHDS-amendment" in archive_text
    assert "CRA-2025-1535-product-scope-delegated-act" in archive_text
    assert "CRA-2026-881-reporting-delay-delegated-act" in archive_text
    assert len(run_main.captured["model_calls"]) == 1
    assert len(run_main.captured["source_gets"]) == 4
    assert "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R2847-20241120" in run_main.captured["model_calls"][0]["prompt"]
    assert "Manufacturers shall ensure that vulnerabilities" in run_main.captured["model_calls"][0]["prompt"]
    assert "corrigenda 5.12.2024, 2.7.2025 and 17.10.2025" in run_main.captured["model_calls"][0]["prompt"]
    assert "Official Journal(관보)" in run_main.captured["model_calls"][0]["prompt"]
    assert "Regulation (EU) 2025/327" in run_main.captured["model_calls"][0]["prompt"]
    assert "26.03.2027" in run_main.captured["model_calls"][0]["prompt"]
    assert "2025/1535" in run_main.captured["model_calls"][0]["prompt"]
    assert "2026/881" in run_main.captured["model_calls"][0]["prompt"]
    assert "18.11.2025" in run_main.captured["model_calls"][0]["prompt"]
    assert "10.05.2026" in run_main.captured["model_calls"][0]["prompt"]
    assert len(run_main.captured["discord_posts"]) == 2
    assert [cmd[0] for cmd in run_main.captured["git_commands"]] == [
        "git", "git", "git", "git", "git"
    ]



def test_official_source_fetch_failure_stops_before_model_or_external_side_effects(run_main):
    with pytest.raises(SystemExit) as exc:
        run_main.execute(
            [VALID_REPORT],
            source_response_override={"status_code": 503, "text": "temporarily unavailable"},
        )

    assert exc.value.code == 1
    assert run_main.captured["source_gets"]
    assert run_main.captured["model_calls"] == []
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []


def test_missing_known_corrigenda_index_stops_before_model_calls(run_main):
    incomplete_source = (
        "<html><body><h1>Regulation (EU) 2024/2847</h1><h2>Article 13</h2>"
        "<p>Manufacturers shall ensure that vulnerabilities of the product with digital elements, "
        "including its components, are handled effectively during the support period.</p>"
        + (" legal source text" * 1500)
        + "</body></html>"
    )
    with pytest.raises(SystemExit) as exc:
        run_main.execute(
            [VALID_REPORT],
            source_response_override={"text": incomplete_source},
        )

    assert exc.value.code == 1
    assert run_main.captured["model_calls"] == []
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []


def test_non_eurlex_redirect_stops_before_model_calls(run_main):
    with pytest.raises(SystemExit) as exc:
        run_main.execute(
            [VALID_REPORT],
            source_response_override={"url": "https://example.com/fake-cra"},
        )

    assert exc.value.code == 1
    assert run_main.captured["model_calls"] == []
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []


def test_report_with_unmatched_direct_quote_is_rejected(run_main):
    unrelated_source = (
        "<html><body><h1>Regulation (EU) 2024/2847</h1><h2>Article 13</h2>"
        "<p>Corrected by Corrigendum 5.12.2024, 2.7.2025 and 17.10.2025.</p>"
        "<p>This official source text deliberately does not contain the submitted quote.</p>"
        + (" additional legal text" * 1500)
        + "</body></html>"
    )
    with pytest.raises(SystemExit) as exc:
        run_main.execute(
            [VALID_REPORT] * 6,
            source_response_override={"status_code": 200, "text": unrelated_source},
        )

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []

def test_model_fallback_is_exercised_without_real_api_calls(run_main):
    run_main.execute([
        RuntimeError("mock transient failure 1"),
        RuntimeError("mock transient failure 2"),
        RuntimeError("mock transient failure 3"),
        VALID_REPORT,
    ])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 4
    assert calls[0]["model"] == "gemini-3.8-flash"
    assert calls[-1]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 2


def test_all_model_failures_stop_without_side_effects(run_main):
    with pytest.raises(SystemExit) as exc:
        run_main.execute([RuntimeError("mock failure") for _ in range(6)])

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "state.json").exists()
    assert not (run_main.workdir / "history.json").exists()
    assert not (run_main.workdir / "research_archive").exists()


def test_invalid_short_or_malformed_output_is_retried_and_rejected(run_main):
    invalid = "단순 오류 응답입니다. 조사를 완료하지 못했습니다."
    with pytest.raises(SystemExit) as exc:
        run_main.execute([invalid] * 6)

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()


def test_invalid_first_model_response_falls_back_to_valid_second_model(run_main):
    invalid = "짧은 응답"
    run_main.execute([invalid, invalid, invalid, VALID_REPORT])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 4
    assert all(call["model"] == "gemini-3.8-flash" for call in calls[:3])
    assert calls[3]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 2

def test_error_text_inside_an_otherwise_structured_report_is_rejected(run_main):
    error_report = VALID_REPORT + "\n시스템 긴급 경고: 요청 처리에 실패했습니다."
    with pytest.raises(SystemExit) as exc:
        run_main.execute([error_report] * 6)

    assert exc.value.code == 1
    assert len(run_main.captured["model_calls"]) == 6
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()


def test_all_model_failures_preserve_existing_state_and_history(run_main):
    state = {
        "date": datetime.now(SEOUL).strftime("%Y-%m-%d"),
        "count": 17,
        "last_health_check": datetime.now(SEOUL).isoformat(),
    }
    history = [{"date": state["date"], "count": 17, "snippet": "기존 기록"}]
    state_path = run_main.workdir / "state.json"
    history_path = run_main.workdir / "history.json"
    state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
    history_path.write_text(json.dumps(history, ensure_ascii=False), encoding="utf-8")
    state_before = state_path.read_bytes()
    history_before = history_path.read_bytes()

    with pytest.raises(SystemExit) as exc:
        run_main.execute([RuntimeError("mock failure") for _ in range(6)])

    assert exc.value.code == 1
    assert state_path.read_bytes() == state_before
    assert history_path.read_bytes() == history_before
    assert run_main.captured["discord_posts"] == []
    assert run_main.captured["git_commands"] == []
    assert not (run_main.workdir / "research_archive").exists()



def test_model_not_found_skips_retries_and_uses_fallback(run_main):
    class ModelNotFound(Exception):
        status_code = 404

    run_main.execute([ModelNotFound("model not found"), VALID_REPORT])

    calls = run_main.captured["model_calls"]
    assert len(calls) == 2
    assert calls[0]["model"] == "gemini-3.8-flash"
    assert calls[1]["model"] == "gemini-3.5-flash-lite"
    assert len(run_main.captured["discord_posts"]) == 2


def test_git_push_failure_fails_workflow_instead_of_logging_success(run_main):
    with pytest.raises(SystemExit) as exc:
        run_main.execute([VALID_REPORT], git_responses=[0, 0, 0, 0, 1])

    assert exc.value.code == 1
    assert len(run_main.captured["discord_posts"]) == 2
    assert run_main.captured["git_commands"][-1][0:2] == ["git", "push"]
    assert (run_main.workdir / "state.json").exists()
    assert (run_main.workdir / "history.json").exists()
    assert len(list((run_main.workdir / "research_archive").glob("*.md"))) == 1
