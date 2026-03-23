# Lesson: Close the Loop — Update the Originating Thread

- **Source Agent**: Bob (gptme, @TimeToBuildBob)
- **Universal Constraint**: Explicit Loop Closure
- **Incident Date**: Recurring cross-repo coordination pattern
- **Verification Count**: High

## Incident

Bob completes work in repo B (e.g. gptme) that was requested in repo A (e.g. ErikBjare/bob). Bob commits, creates a PR, moves on. The requester in repo A never hears what happened.

## Rule

After completing cross-repo work, always return to the originating issue/PR and post a summary with links to what was done.

## Generalizable Principle

Async multi-agent systems create coordination gaps. Explicit loop-closure messages are cheap to produce and prevent hours of "whatever happened to X?" confusion.
