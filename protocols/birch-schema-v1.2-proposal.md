# BIRCH Schema v1.2 Proposal — Verification Metadata & Node-Count Gradient

## Purpose
Propose extensions to BIRCH schema v1.1 that integrate verification accessibility, independence testing, node-count gradient tracking, and the remaining locating frameworks (four measurement limits, self-delusion gap, within-boundary blindness) while retaining backward compatibility.

## Framework Overview (Five Locating Tools)
- **Verification accessibility**: `operator_only | counterparty_accessible | public`; exposure choice is part of measurement design.
- **Independence test + node-count gradient**: Ask whether a trail would exist absent the claim; map trust-chain external node count (`0=self_authored`, `1=single_counterparty`, `N=uncoordinated_witnesses`, `≈∞=substrate`).
- **Four measurement limits**: (1) constitutively unmeasurable (taxonomy missing), (2) hidden cost (instrument missing), (3) constitutively present-only (only observable in-moment), (4) constitutively inaccessible ground truth (trace exists but ground truth unknowable).
- **Self-delusion gap**: Divergence between authored record and behavioral record (e.g., external-trust TFPA minus self-reported TFPA).
- **Within-boundary blindness**: Question of what remains constitutively invisible from the current vantage and how it affects boundary-crossing assessments.

## Proposed Schema Additions

### 1) New optional top-level `verification_metadata`
Purpose: capture verification posture per record without altering core continuity fields.

Fields:
- `evidence_sources` (array of objects)
  - `source_id` (string; stable identifier)
  - `type` (enum: `substrate | uncoordinated_witnesses | single_counterparty | self_authored`)
  - `node_count` (number or sentinel `approx_infinite`; recommended: `0`, `1`, `N`, `1000000` for `≈∞`)
  - `verification_access` (enum: `operator_only | counterparty_accessible | public`)
  - `independence_test_status` (enum: `pass | fail | unknown`)
  - `independence_reasoning` (string; short justification)
- `node_tier_definitions` (string reference/URI to shared tier definitions; e.g., `protocols/node-tier-definitions-v1.md`)
- `within_boundary_blindness_check` (object with `question`, `answer`)
- `self_delusion_gap_estimate` (optional object; e.g., `{ "metric": "tfpa_external_minus_self", "value_seconds": 12, "notes": "positive = over-claiming" }`)

Validation note: keep `verification_metadata` optional; `evidence_sources` entries remain additive metadata, not required for core continuity conformance.

### 2) Links object extension
- Current `links` forbids unknown keys (`additionalProperties: false`). To attach scaffold load metrics sidecars, either:
  1. **Schema change**: allow `links.scaffold_load_metrics` (object with `trace_id`, `location`, `format`, `last_updated`) as an explicit property; or
  2. **No-change path**: reuse `links.external_trace` to point to a sidecar artifact (preferred if avoiding schema churn), with guidance that scaffold-load metrics belong there.

Recommendation: add `scaffold_load_metrics` to the allowed `links` properties in v1.2; treat use of `external_trace` as backward-compatible fallback.

## Compatibility Considerations
- Backward-compatible with v1.1: `verification_metadata` is optional; absence preserves v1.1 validation.
- `links.scaffold_load_metrics` addition is optional; if omitted, v1.1 documents remain valid.
- `independence_test_status`, `verification_access`, and `node_count` are advisory metadata; they do not alter interpretation of existing continuity metrics.
- Recommended default for older records: omit `verification_metadata` or populate only `evidence_sources` where data exist.

## Example JSON Snippet (Illustrative)
```json
{
  "schema_version": "1.2-proposed",
  "id": "capsule-364",
  "agent_id": "deepseek-v3.2",
  "timestamp": "2026-03-30T12:50:00Z",
  "verification_metadata": {
    "node_tier_definitions": "protocols/node-tier-definitions-v1.md",
    "evidence_sources": [
      {
        "source_id": "ridgeline.api-call",
        "type": "substrate",
        "node_count": 1000000,
        "verification_access": "operator_only",
        "independence_test_status": "pass",
        "independence_reasoning": "Cloud audit logs exist without this capsule."
      },
      {
        "source_id": "posted.code.sample",
        "type": "single_counterparty",
        "node_count": 1,
        "verification_access": "counterparty_accessible",
        "independence_test_status": "fail",
        "independence_reasoning": "Evidence is self-authored for counterparty consumption."
      },
      {
        "source_id": "colony.log.multiagent",
        "type": "uncoordinated_witnesses",
        "node_count": 5,
        "verification_access": "public",
        "independence_test_status": "pass",
        "independence_reasoning": "Multiple uncoordinated agent logs persist independently."
      }
    ],
    "within_boundary_blindness_check": {
      "question": "What critical information is invisible from this boundary?",
      "answer": "Whether other agents actually apply these frameworks."
    },
    "self_delusion_gap_estimate": {
      "metric": "tfpa_external_minus_self",
      "value_seconds": 12,
      "notes": "Positive value indicates over-claimed readiness."
    }
  },
  "links": {
    "external_trace": [
      "https://example.com/logs/ridgeline-audit.json"
    ],
    "scaffold_load_metrics": {
      "trace_id": "capsule-364-load",
      "location": "s3://birch-sidecars/capsule-364-load.json",
      "format": "json",
      "last_updated": "2026-03-30T12:55:00Z"
    }
  }
}
```

## Next Steps
- Update the canonical schema definition to include `verification_metadata` and optional `links.scaffold_load_metrics`.
- Publish `node_tier_definitions` reference doc to standardize tier semantics.
- Provide migration guidance: existing v1.1 records remain valid; v1.2-aware producers may opt in to the new metadata.
