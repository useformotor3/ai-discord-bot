from pathlib import Path


def test_production_workflow_uses_three_hour_schedule_not_external_dispatch():
    workflow = (
        Path(__file__).resolve().parents[1] / ".github" / "workflows" / "run.yml"
    ).read_text(encoding="utf-8")

    assert "schedule:" in workflow
    assert '- cron: "17 */3 * * *"' in workflow
    assert "workflow_dispatch:" in workflow
    assert "repository_dispatch:" not in workflow
    assert "group: cra-production-run" in workflow
    assert "cancel-in-progress: false" in workflow
    assert "id: pre_run_checkpoint" in workflow
    assert "id: operational_guard" in workflow
    assert "steps.pre_run_checkpoint.outcome == 'success'" in workflow
    assert "steps.operational_guard.outcome == 'success'" in workflow
