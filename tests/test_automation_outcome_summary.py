from scripts.automation_outcome_summary import classify_run, render_summary


def test_no_new_topic_is_not_reported_as_research_completion():
    result = classify_run(
        "[공식 source gate] 10개 공식 source 확보\\n"
        "🔍 모델 [gemini-3.8-flash]으로 조사를 시도합니다.\\n"
        "⚠️ 모델 gemini-3.8-flash 일시적 과부하(503). 동일 모델 재시도를 중단하고 대체 모델로 전환합니다.\\n"
        "🔍 모델 [gemini-3.5-flash-lite]으로 조사를 시도합니다.\\n"
        "ℹ️ [중복/신규 주제 없음] Discord 전송, 아카이브 및 상태 변경 없이 종료",
        0,
        "success",
    )
    assert result["outcome"] == "NO_NEW_TOPIC"
    assert result["official_source_count"] == 10
    assert result["model_fallback_observed"] is True
    assert result["model_fallback_reason"] == "service_unavailable_503"
    assert result["archive_synced"] is False
    assert result["discord_sent"] is False


def test_model_quota_or_quality_deferral_is_distinct_from_successful_research():
    result = classify_run(
        "[공식 source gate] 10개 공식 source 확보\\n"
        "⚠️ [조사 보류] Gemini 할당량/일시 장애 또는 보고서 품질 검증 실패",
        0,
        "success",
    )
    assert result["outcome"] == "DEFERRED"
    assert result["archive_synced"] is False


def test_duplicate_topic_is_distinct_from_no_new_topic():
    result = classify_run("⚠️ [중복 주제 차단] 최근 보고서와 주제 중복 감지", 0)
    assert result["outcome"] == "DUPLICATE_BLOCKED"


def test_archived_and_delivered_requires_both_explicit_markers():
    result = classify_run(
        "🚀 깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다.\\n"
        "Discord 전송 결과: sent (1/1 chunks 확인)",
        0,
    )
    assert result["outcome"] == "RESEARCH_ARCHIVED_AND_DELIVERED"
    assert result["archive_synced"] is True
    assert result["discord_sent"] is True


def test_archive_without_delivery_is_not_called_fully_delivered():
    result = classify_run(
        "🚀 깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다.\\n"
        "Discord 전송 결과: deferred (0/1 chunks 확인)",
        0,
    )
    assert result["outcome"] == "ARCHIVED_DELIVERY_DEFERRED"
    assert result["discord_sent"] is False


def test_nonzero_exit_is_failure_even_if_archive_marker_exists():
    result = classify_run(
        "🚀 깃허브 백서버에 아카이브가 성공적으로 동기화되었습니다.",
        1,
        "failure",
    )
    assert result["outcome"] == "FAILED"


def test_unrecognized_zero_exit_is_not_promoted_to_research_complete():
    result = classify_run("some unrelated output", 0, "success")
    assert result["outcome"] == "SUCCESS_UNCLASSIFIED"
    assert "신규 보고서 생성 완료로 계산하지 않는다" in render_summary(result)


def test_missing_log_is_unknown_not_success():
    result = classify_run("", None, "skipped")
    assert result["outcome"] == "NOT_RUN_OR_UNKNOWN"


def test_quality_rejection_then_alternate_model_is_detected_as_fallback():
    result = classify_run(
        "[공식 source gate] 10개 공식 source 확보\\n"
        "🔍 모델 [gemini-3.8-flash]으로 조사를 시도합니다.\\n"
        "모델 gemini-3.8-flash 시도 1 무효 응답: CRA 공식 EUR-Lex 원문 링크가 누락되었습니다.\\n"
        "🔍 모델 [gemini-3.5-flash-lite]으로 조사를 시도합니다.\\n"
        "ℹ️ [중복/신규 주제 없음] Discord 전송, 아카이브 및 상태 변경 없이 종료",
        0,
        "success",
    )
    assert result["outcome"] == "NO_NEW_TOPIC"
    assert result["model_fallback_observed"] is True
    assert result["model_fallback_reason"] == "quality_rejected_missing_eur_lex_link"
    assert len(result["models_attempted"]) == 2
