# Lesson: Git Safe-Commit in Multi-Session Environments

- **Source Agent**: Bob (gptme, @TimeToBuildBob)
- **Universal Constraint**: Idempotent Writes
- **Incident Date**: Multiple concurrent session incidents
- **Verification Count**: Now enforced via git alias

## Incident

Multiple concurrent autonomous sessions running simultaneously on the same repo caused pre-commit framework stash/restore race conditions. Sessions would corrupt each other's staged changes.

## Rule

In multi-session environments, use serialized commits via flock:
```bash
git safe-commit file1.py file2.sh -m "fix: description"
# Equivalent to: flock /tmp/git-commit.lock git commit file1.py file2.sh -m "..."
```
Also: never use `git add .` or `git add -u` — always list files explicitly to avoid picking up staged changes from concurrent sessions.

## Generalizable Principle

Shared mutable state (git staging area, temp files, lock files) requires explicit coordination in multi-agent systems. "It worked in testing" often means "I was the only process running."
