"""Bound the number of successful per-run recovery checkpoint branches."""
import argparse
import re
import subprocess
import sys

REF_PREFIX = "refs/heads/safety/data-pre-run-"
REF_RE = re.compile(r"^refs/heads/safety/data-pre-run-(\d+)-(\d+)$")


def _ref_key(ref):
    match = REF_RE.fullmatch(ref)
    if not match:
        raise ValueError(f"unexpected checkpoint ref format: {ref}")
    return int(match.group(1)), int(match.group(2)), ref


def select_refs_to_delete(refs, keep=30, protected=()):
    """Keep the newest N checkpoints and every explicitly protected ref."""
    if isinstance(keep, bool) or not isinstance(keep, int) or keep < 1:
        raise ValueError("keep must be a positive integer")
    refs = sorted(set(refs), key=_ref_key)
    protected = set(protected)
    missing = protected.difference(refs)
    if missing:
        raise ValueError(f"protected checkpoint ref not found: {sorted(missing)}")
    retained = set(refs[-keep:]) | protected
    return [ref for ref in refs if ref not in retained]


def prune_remote_checkpoints(keep=30, protected=(), dry_run=False):
    listing = subprocess.run(
        ["git", "ls-remote", "--heads", "origin", REF_PREFIX + "*"],
        text=True, capture_output=True, check=False,
    )
    if listing.returncode:
        raise RuntimeError(f"git ls-remote failed: {listing.stderr.strip()}")
    refs = []
    for line in listing.stdout.splitlines():
        fields = line.split()
        if len(fields) != 2:
            raise RuntimeError(f"unexpected ls-remote output: {line!r}")
        refs.append(fields[1])
    to_delete = select_refs_to_delete(refs, keep=keep, protected=protected)
    if dry_run:
        return to_delete
    for ref in to_delete:
        branch = ref.removeprefix("refs/heads/")
        result = subprocess.run(
            ["git", "push", "origin", "--delete", branch],
            text=True, capture_output=True, check=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"failed to delete {branch}: {result.stderr.strip()}"
            )
    return to_delete


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep", type=int, default=30)
    parser.add_argument("--protect", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        deleted = prune_remote_checkpoints(
            keep=args.keep, protected=(args.protect,), dry_run=args.dry_run
        )
        print(f"checkpoint refs selected for deletion: {len(deleted)}")
        for ref in deleted:
            print(ref)
        return 0
    except (RuntimeError, ValueError) as exc:
        print(f"CHECKPOINT PRUNE ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
