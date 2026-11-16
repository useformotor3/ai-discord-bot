import subprocess

import pytest

from scripts.prune_checkpoints import (
    REF_PREFIX,
    prune_remote_checkpoints,
    select_refs_to_delete,
)


def _refs(count):
    return [f"{REF_PREFIX}{1000 + i}-1" for i in range(count)]


def test_keeps_newest_thirty_and_protected_current_ref():
    refs = _refs(94)
    deleted = select_refs_to_delete(refs, keep=30, protected=(refs[-1],))
    assert len(deleted) == 64
    assert refs[-1] not in deleted
    assert refs[-30:] == [ref for ref in refs if ref not in deleted]


def test_protected_older_checkpoint_is_retained_in_addition_to_newest():
    refs = _refs(40)
    deleted = select_refs_to_delete(refs, keep=30, protected=(refs[0],))
    assert len(deleted) == 9
    retained = [ref for ref in refs if ref not in deleted]
    assert retained == [refs[0], *refs[-30:]]


@pytest.mark.parametrize("keep", [0, -1, True, 1.5])
def test_rejects_invalid_retention_count(keep):
    with pytest.raises(ValueError, match="positive integer"):
        select_refs_to_delete(_refs(3), keep=keep)


def test_rejects_unexpected_ref_format():
    with pytest.raises(ValueError, match="unexpected checkpoint ref"):
        select_refs_to_delete(["refs/heads/safety/other-backup-123"])


def test_rejects_missing_protected_ref():
    with pytest.raises(ValueError, match="protected checkpoint ref not found"):
        select_refs_to_delete(_refs(3), protected=("refs/heads/safety/data-pre-run-9999-1",))


def test_remote_prune_deletes_only_old_refs_and_preserves_current(monkeypatch):
    refs = _refs(4)
    calls = []

    def fake_run(args, **kwargs):
        calls.append(args)
        if args[:3] == ["git", "ls-remote", "--heads"]:
            output = "".join(f"{'a' * 40} {ref}\n" for ref in refs)
            return subprocess.CompletedProcess(args, 0, stdout=output, stderr="")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)
    deleted = prune_remote_checkpoints(keep=2, protected=(refs[-1],))
    assert deleted == refs[:2]
    assert calls[0] == [
        "git", "ls-remote", "--heads", "origin", REF_PREFIX + "*"
    ]
    assert calls[1:] == [
        ["git", "push", "origin", "--delete", ref.removeprefix("refs/heads/")]
        for ref in refs[:2]
    ]


def test_remote_prune_fails_closed_if_listing_fails(monkeypatch):
    def fake_run(args, **kwargs):
        return subprocess.CompletedProcess(args, 128, stdout="", stderr="network down")

    monkeypatch.setattr(subprocess, "run", fake_run)
    with pytest.raises(RuntimeError, match="ls-remote failed"):
        prune_remote_checkpoints(protected=("refs/heads/safety/data-pre-run-1000-1",))
