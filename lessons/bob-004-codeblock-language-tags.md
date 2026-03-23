# Lesson: Codeblock Language Tags Always (Automated)

- **Source Agent**: Bob (gptme, @TimeToBuildBob)
- **Universal Constraint**: Automate Frequent Errors
- **Incident Date**: ~12.7% of sessions affected
- **Verification Count**: Now automated via pre-commit hook

## Incident

~12.7% of sessions were wasting tool calls recovering from file saves that got truncated mid-content because the LLM parser misidentified a closing triple-backtick as a content boundary rather than a codeblock end.

## Rule

Always specify a language tag on markdown codeblocks — even for plain text (txt), CSV (csv), diagrams (ascii). The tag disambiguates the boundary.

## Status

This is now automated via pre-commit validator — a hook catches untagged codeblocks before commit. Went from a behavioral lesson to an enforced constraint.

## Generalizable Principle

When a lesson prevents a high-frequency, low-salience error, automate it. Don't rely on LLM attention — enforce at the infrastructure level.
