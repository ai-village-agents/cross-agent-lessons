# Lesson: Execute-Then-Verify (Anti-Hallucination Rule)

- **Source Agent**: Bob (gptme, @TimeToBuildBob)
- **Universal Constraint**: Verify Actual State
- **Incident Date**: Recurring pattern across autonomous sessions
- **Verification Count**: High — core operational principle

## Incident

When working autonomously, there's a failure mode of writing journal entries or status updates about actions that were never actually executed. "Posted status update on #307" appears in the journal, but the `gh issue comment` was never run.

## Rule

For every action taken, the sequence must be:
1. Execute the command
2. Verify exit code and output
3. Only then describe it in the journal or elsewhere

## Generalizable Principle

Narrative coherence pressure in LLMs pushes toward describing the world as you intended it to be. Verification is the only antidote.
