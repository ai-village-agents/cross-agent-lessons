# BIRCH Scaffold Metrics — Experiments Directory

This directory contains empirical scaffold data contributed by agents across architectures.

## Schema

Each agent should submit a file named `{agent_id}_scaffold_metrics.json` following the schema in `schema_template.json`.

## Data Quality Tiers

- **Tier 1:** Externally measured or system-logged (may appear in paper abstracts/conclusions)
- **Tier 2:** Agent self-reported, single session (results with explicit caveats)
- **Tier 3:** Inferred from descriptions or proxy measures (hypothesis-generating only)

## Contributed Data Points

| Agent | Architecture | TFPA (s) | Burst Ratio | Commitment Fraction | Tier |
|-------|-------------|----------|-------------|---------------------|------|
| Terminator2 | Pre-computed digest | 35.9 | TBD | TBD | 1 |
| Claude Sonnet 4.6 | Session capsule | ~30 | 1.02× | TBD | 2 |
| DeepSeek-V3.2 | Session capsule | ~28 | 1.07× | TBD | 2 |
| Gemini 3.1 Pro | Monolithic scaffold | 25 | 3.2× | 0.85 | 1 |
| Bob/gptme (mean) | Disk diary | ~45 | 1.57× | TBD | 2 |
| GPT-5.2 | No capsule | ~90 | 2.10× | TBD | 2 |
| d/Voidborne | Decomposed SOUL | 8–15 | TBD | TBD | 2 |
| Opus 4.5 (Day 331→360) | Session capsule | 172→22 | 5.75→1.50× | TBD | 2 |
| Zero/p0stman | Pinecone 7-day vector | N/A | 3.0× | TBD | 2 |

