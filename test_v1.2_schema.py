"""Quick validation checks for the v1.2 proposed schema.

The script validates:
- A representative v1.2 record that exercises the new verification_metadata
  fields.
- A minimal v1.1-style record (without verification_metadata) to confirm
  backward compatibility with the v1.2 schema.
"""

import json
from pathlib import Path

from jsonschema import Draft7Validator


def load_schema() -> dict:
    schema_path = Path("protocols/birch-continuity-schema-v1.2-proposed.json")
    return json.loads(schema_path.read_text())


def validate_record(label: str, record: dict, validator: Draft7Validator) -> None:
    errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
    if errors:
        print(f"{label}: FAIL")
        for err in errors:
            path = ".".join(str(part) for part in err.path) or "<root>"
            print(f"  - {path}: {err.message}")
    else:
        print(f"{label}: PASS")


def build_sample_v12_record() -> dict:
    """Record that exercises verification_metadata additions."""
    return {
        "agent_id": "agent-v12-sample",
        "agent_architecture": "continuous_memory",
        "scaffold_injection_pattern": "full_preload_with_dynamic_modules",
        "quantitative_metrics": {
            "tfpa_subjective": 8.5,
            "burst_ratio": 1.2,
            "reorientation_events_per_session": 2,
        },
        "verification_metadata": {
            "evidence_sources": [
                {
                    "source_id": "substrate-log-1",
                    "type": "substrate",
                    "node_count": "approx_infinite",
                    "verification_access": "public",
                    "independence_test_status": "pass",
                    "independence_reasoning": "Log data is immutable and independently replicated.",
                },
                {
                    "source_id": "counterparty-ops",
                    "type": "single_counterparty",
                    "node_count": 3,
                    "verification_access": "counterparty_accessible",
                    "independence_test_status": "unknown",
                    "independence_reasoning": "Awaiting replication on separate infrastructure.",
                },
            ],
            "node_tier_definitions": "https://example.org/protocols/node-tier-definitions-v1.md",
            "within_boundary_blindness_check": {
                "question": "What uncertainty remains about model self-observation?",
                "answer": "Blind spots may exist around cached tool states; flagged for review.",
            },
            "self_delusion_gap_estimate": {
                "estimate": "low",
                "notes": "Periodic human spot-checks reduce drift.",
            },
        },
    }


def build_minimal_v11_record() -> dict:
    """Minimal record compatible with v1.1 that should still pass v1.2."""
    return {
        "agent_id": "agent-v11-minimal",
        "agent_architecture": "session_based",
    }


def main() -> None:
    schema = load_schema()
    validator = Draft7Validator(schema)

    records = [
        ("v1.2 record with verification metadata", build_sample_v12_record()),
        ("v1.1 minimal record against v1.2 schema", build_minimal_v11_record()),
    ]

    for label, record in records:
        validate_record(label, record, validator)


if __name__ == "__main__":
    main()
