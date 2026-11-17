from pathlib import Path


def test_production_workflow_uses_hourly_schedule_not_external_five_minute_dispatch():
    workflow = (
        Path(__file__).resolve().parents[1] / ".github" / "workflows" / "run.yml"
    ).read_text(encoding="utf-8")

    assert "schedule:" in workflow
    assert '- cron: "0 * * * *"' in workflow
    assert "workflow_dispatch:" in workflow
    assert "repository_dispatch:" not in workflow
    assert "group: cra-production-run" in workflow
    assert "cancel-in-progress: false" in workflow
