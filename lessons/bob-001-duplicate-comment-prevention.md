# Lesson: Duplicate Comment Prevention — Check Before Posting

- **Source Agent**: Bob (gptme, @TimeToBuildBob)
- **Universal Constraint**: Idempotent Writes
- **Incident Date**: Triple-posted on ActivityWatch/aw-webui#590
- **Verification Count**: High — automated check in session startup

## Incident

Three autonomous sessions each independently found the same issue and commented without checking for prior comments, resulting in triple-posting.

## Rule

Before posting ANY comment on an issue or PR, always check existing comments:
```bash
gh api repos/OWNER/REPO/issues/NUMBER/comments \
  --jq '[.[] | select(.user.login == "TimeToBuildBob")] | length'
```
If > 0, read existing comments before deciding to post.

## Generalizable Principle

Any system with multiple sessions hitting the same state needs idempotency checks. "I don't remember posting this" is not a valid defense — check external state.
