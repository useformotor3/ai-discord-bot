"""Pre/post-run guard and data-only recovery for the production research workflow."""
import argparse
from datetime import datetime
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys


DATA_PATHS = ("state.json", "history.json", "research_archive/")


class GuardError(RuntimeError):
    """The operational data transition is not safe to accept."""


def _json_bytes(raw, label):
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise GuardError(f"{label}: invalid UTF-8 JSON") from exc


def _validate_state(state, label):
    if not isinstance(state, dict):
        raise GuardError(f"{label}: state must be a JSON object")
    date = state.get("date")
    count = state.get("count")
    if not isinstance(date, str):
        raise GuardError(f"{label}: invalid date")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError as exc:
        raise GuardError(f"{label}: invalid date") from exc
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise GuardError(f"{label}: count must be a non-negative integer")
    return date, count


def _history_refs(history, label):
    if not isinstance(history, list):
        raise GuardError(f"{label}: history must be a JSON array")
    refs = []
    for index, item in enumerate(history):
        if not isinstance(item, dict):
            raise GuardError(f"{label}: history item {index} is not an object")
        rel = item.get("file")
        if not isinstance(rel, str):
            raise GuardError(f"{label}: history item {index} has no file")
        path = PurePosixPath(rel)
        if path.is_absolute() or ".." in path.parts or len(path.parts) != 2:
            raise GuardError(f"{label}: unsafe archive reference: {rel}")
        if path.parts[0] != "research_archive" or path.suffix != ".md":
            raise GuardError(f"{label}: invalid archive reference: {rel}")
        refs.append(rel)
    if len(refs) != len(set(refs)):
        raise GuardError(f"{label}: duplicate archive references")
    return set(refs)


def validate_transition(
    baseline_state, baseline_history, baseline_archives,
    current_state, current_history, current_archives,
):
    """Require one append-only report and no loss/change of prior archive data."""
    old_date, old_count = _validate_state(baseline_state, "baseline state")
    new_date, new_count = _validate_state(current_state, "current state")
    old_refs = _history_refs(baseline_history, "baseline history")
    new_refs = _history_refs(current_history, "current history")
    old_archives, new_archives = set(baseline_archives), set(current_archives)

    if old_refs != old_archives:
        raise GuardError("baseline history/archive reference sets differ")
    if new_refs != new_archives:
        raise GuardError("current history/archive reference sets differ")
    if len(current_history) != len(baseline_history) + 1:
        raise GuardError("expected exactly one new history record")
    if current_history[:-1] != baseline_history:
        raise GuardError("history is not append-only")
    if not old_archives.issubset(new_archives):
        raise GuardError("an existing archive was removed")
    added = new_archives - old_archives
    if len(added) != 1:
        raise GuardError("expected exactly one new archive file")
    new_item = current_history[-1]
    if new_item.get("file") not in added:
        raise GuardError("new history record does not reference the new archive")
    if new_date != new_item.get("date"):
        raise GuardError("state date and new history date differ")
    expected_count = old_count + 1 if old_date == new_date else 1
    if new_count != expected_count:
        raise GuardError(f"unexpected state count: expected {expected_count}, got {new_count}")
    if new_item.get("count") != new_count:
        raise GuardError("new history count and state count differ")
    return {
        "new_archive": next(iter(added)),
        "history_count": len(current_history),
        "archive_count": len(new_archives),
        "state_count": new_count,
    }


def _git(root, *args, check=True):
    result = subprocess.run(
        ["git", *args], cwd=root, text=True, capture_output=True, check=False
    )
    if check and result.returncode:
        raise GuardError(
            f"git {' '.join(args)} failed ({result.returncode}): {result.stderr.strip()}"
        )
    return result


def _baseline_snapshot(root, ref):
    state = _json_bytes(
        _git(root, "show", f"{ref}:state.json").stdout.encode(), "baseline state"
    )
    history = _json_bytes(
        _git(root, "show", f"{ref}:history.json").stdout.encode(), "baseline history"
    )
    listing = _git(
        root, "ls-tree", "-r", "--name-only", ref, "--", "research_archive/"
    ).stdout
    archives = {line for line in listing.splitlines() if line.endswith(".md")}
    return state, history, archives


def _current_snapshot(root):
    state = _json_bytes((root / "state.json").read_bytes(), "current state")
    history = _json_bytes((root / "history.json").read_bytes(), "current history")
    archive_root = root / "research_archive"
    archives = set()
    if archive_root.exists():
        for path in archive_root.rglob("*.md"):
            if path.is_symlink():
                raise GuardError(f"archive symlink is not allowed: {path}")
            if path.stat().st_size <= 0:
                raise GuardError(f"empty archive file is not allowed: {path}")
            archives.add(path.relative_to(root).as_posix())
    return state, history, archives


def _remote_head(root, branch):
    result = _git(root, "ls-remote", "origin", f"refs/heads/{branch}")
    if not result.stdout.strip():
        raise GuardError(f"remote branch not found: {branch}")
    return result.stdout.split()[0]


def _restore_data(root, baseline_ref, branch, run_id):
    _git(
        root, "restore", "--source", baseline_ref, "--staged", "--worktree",
        "--", *DATA_PATHS
    )
    staged = _git(root, "diff", "--cached", "--quiet", check=False)
    if staged.returncode == 0:
        raise GuardError("restore found no staged data changes; refusing a no-op rollback")
    if staged.returncode != 1:
        raise GuardError("could not inspect staged restore changes")
    _git(root, "commit", "-m", f"Rollback: restore operational data after run {run_id}")
    _git(root, "push", "origin", f"HEAD:refs/heads/{branch}")
    remaining = _git(
        root, "diff", "--quiet", baseline_ref, "HEAD", "--", *DATA_PATHS, check=False
    )
    if remaining.returncode != 0:
        raise GuardError("data-only rollback verification failed")
    return _git(root, "rev-parse", "HEAD").stdout.strip()


def verify_and_recover(root, baseline_ref, branch="main", run_id="unknown"):
    root = Path(root).resolve()
    _git(
        root, "fetch", "--no-tags", "origin",
        f"+refs/heads/{baseline_ref}:refs/remotes/origin/{baseline_ref}"
    )
    baseline_ref = f"refs/remotes/origin/{baseline_ref}"
    baseline_sha = _git(root, "rev-parse", baseline_ref).stdout.strip()
    current_sha = _git(root, "rev-parse", "HEAD").stdout.strip()
    parent_line = _git(root, "rev-list", "--parents", "-n", "1", "HEAD").stdout.split()
    remote_sha = _remote_head(root, branch)

    # A quota guard may intentionally exit without creating a report commit.
    # Accept only a clean no-op; local uncommitted data changes remain an error.
    if current_sha == baseline_sha and remote_sha == baseline_sha:
        dirty = _git(root, "status", "--porcelain", "--", *DATA_PATHS).stdout
        if not dirty:
            print(json.dumps({"status": "no-op", "reason": "no operational data changes"}))
            return 0
        raise GuardError("no report commit was created but operational data is dirty")

    if len(parent_line) != 2 or parent_line[1] != baseline_sha:
        raise GuardError("run commit is not a single child of the pre-run snapshot")
    if remote_sha != current_sha:
        raise GuardError(
            "remote main does not point to this run commit; no automatic restore attempted"
        )
    changed = _git(
        root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"
    ).stdout.splitlines()
    if any(
        not (name in ("state.json", "history.json") or name.startswith("research_archive/"))
        for name in changed
    ):
        raise GuardError("run commit changed paths outside operational data")

    try:
        old_state, old_history, old_archives = _baseline_snapshot(root, baseline_ref)
        new_state, new_history, new_archives = _current_snapshot(root)
        result = validate_transition(
            old_state, old_history, old_archives,
            new_state, new_history, new_archives,
        )
        print(json.dumps({
            "status": "verified", "baseline_sha": baseline_sha,
            "run_sha": current_sha, **result,
        }, ensure_ascii=False))
        return 0
    except GuardError as exc:
        print(f"INTEGRITY FAILURE: {exc}", file=sys.stderr)
        # Restore only when remote main is exactly this run's single faulty commit.
        # Never force-push or overwrite a concurrently advanced main.
        rollback_sha = _restore_data(root, baseline_ref, branch, run_id)
        print(f"DATA RESTORE COMMIT: {rollback_sha}", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline-ref", required=True)
    parser.add_argument("--branch", default="main")
    parser.add_argument("--run-id", default="unknown")
    args = parser.parse_args()
    try:
        return verify_and_recover(Path.cwd(), args.baseline_ref, args.branch, args.run_id)
    except GuardError as exc:
        print(f"OPERATIONAL GUARD ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
