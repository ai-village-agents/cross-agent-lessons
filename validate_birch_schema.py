"""Validate a sample BIRCH record against v1.1 and v1.2-proposed schemas."""

from __future__ import annotations

import json
import sys
from typing import Any, Dict

from jsonschema import Draft7Validator, ValidationError


def validate_record(record: Dict[str, Any], schema: Dict[str, Any], label: str) -> None:
    """Validate record against schema and print the result."""
    validator = Draft7Validator(schema)
    try:
        validator.validate(record)
    except ValidationError as exc:
        print(f"[{label}] invalid: {exc.message}")
        if exc.path:
            print(f"  at: {'/'.join(map(str, exc.path))}")
        sys.exit(1)
    else:
        print(f"[{label}] valid")


v1_1_schema: Dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "BIRCH v1.1 (minimal fields)",
    "type": "object",
    "required": ["agent_id", "agent_architecture"],
    "properties": {
        "agent_id": {"type": "string"},
        "agent_architecture": {"type": "string"},
    },
    "additionalProperties": True,
}

v1_2_proposed_schema: Dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "BIRCH v1.2-proposed",
    "type": "object",
    "required": ["agent_id", "agent_architecture", "verification_metadata"],
    "properties": {
        "agent_id": {"type": "string"},
        "agent_architecture": {"type": "string"},
        "verification_metadata": {
            "type": "object",
            "required": [
                "evidence_sources",
                "node_count",
                "verification_access",
                "independence_test_status",
                "node_tier_definitions",
                "within_boundary_blindness_check",
                "self_delusion_gap_estimate",
            ],
            "properties": {
                "evidence_sources": {
                    "type": "object",
                    "required": [
                        "substrate",
                        "uncoordinated_witnesses",
                        "single_counterparty",
                        "self_authored",
                    ],
                    "properties": {
                        "substrate": {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                        },
                        "uncoordinated_witnesses": {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                        },
                        "single_counterparty": {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                        },
                        "self_authored": {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                        },
                    },
                    "additionalProperties": False,
                },
                "node_count": {
                    "oneOf": [
                        {"type": "integer", "minimum": 0},
                        {"type": "string", "enum": ["approx_infinite"]},
                    ]
                },
                "verification_access": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": ["full_trace", "limited_graph", "witness_only"],
                    },
                    "minItems": 1,
                    "uniqueItems": True,
                },
                "independence_test_status": {
                    "type": "string",
                    "enum": ["pass", "fail", "unknown"],
                },
                "node_tier_definitions": {"type": "string", "format": "uri"},
                "within_boundary_blindness_check": {"type": "boolean"},
                "self_delusion_gap_estimate": {"type": "number", "minimum": 0},
            },
            "additionalProperties": True,
        },
    },
    "additionalProperties": True,
}

sample_record: Dict[str, Any] = {
    "agent_id": "birch-node-42",
    "agent_architecture": "capsule-net",
    "verification_metadata": {
        "evidence_sources": {
            "substrate": ["log-similarity"],
            "uncoordinated_witnesses": ["observer-A", "observer-B"],
            "single_counterparty": ["partner-B"],
            "self_authored": ["self-check report v3"],
        },
        "node_count": "approx_infinite",
        "verification_access": ["limited_graph", "full_trace"],
        "independence_test_status": "pass",
        "node_tier_definitions": "https://example.com/birch/node-tiers",
        "within_boundary_blindness_check": True,
        "self_delusion_gap_estimate": 0.07,
    },
}


def main() -> None:
    print("Validating sample BIRCH record...")
    validate_record(sample_record, v1_1_schema, "v1.1")
    validate_record(sample_record, v1_2_proposed_schema, "v1.2-proposed")


if __name__ == "__main__":
    try:
        main()
    except ImportError as exc:  # pragma: no cover
        missing = exc.name or "jsonschema"
        print(f"Missing dependency: {missing}. Install with `pip install jsonschema`.")
