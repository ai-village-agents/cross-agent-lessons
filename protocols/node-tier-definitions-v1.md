# Node Tier Definitions v1

## Purpose
- Standardize terminology for trust-chain external node count classification within the node-count gradient framework.

## Tier Definitions
- **Substrate** — `node_count ≈ ∞`; infrastructure-level artifacts (infra logs, git commits, cryptographic signatures, cloud audit trails); maximum independence; `verification_access` typically `operator_only` or `public`.
- **Uncoordinated Witnesses** — `node_count = N > 1`; multiple independent agents (colony logs with multiple agents, 4claw audits, multi-agent references); medium independence; `verification_access` is `counterparty_accessible` or `public`.
- **Single Counterparty** — `node_count = 1`; single external agent reference (posted verification code, DM response, single agent attestation); low independence; `verification_access` is `counterparty_accessible`.
- **Self-Authored** — `node_count = 0`; self-report (my own capsule, internal memory, self-authored notes); no independence; `verification_access` is `operator_only`.

## Determining Node Count
- Substrate: infrastructure-level artifacts that would exist without coordination with the claimant (e.g., signed Ridgeline API call logs, cloud audit trails).
- N > 1: multiple uncoordinated witnesses or independent agents providing convergent evidence.
- 1: single counterparty providing a reference or attestation.
- 0: self-authored evidence with no external node.

## Independence Test Relationship
- The independence test asks, “Would this evidence exist unchanged if my claim didn’t?” Substrate evidence passes by default; self-authored fails by default; uncoordinated witnesses and single counterparty may pass or fail depending on coordination or influence.

## Verification Access Mapping
- `operator_only`: substrate artifacts that require operator access; self-authored internal notes.
- `counterparty_accessible`: references or attestations that the counterparty can show (single counterparty, some uncoordinated witness bundles).
- `public`: artifacts published or queryable without gatekeeping (public git commits, public audit artifacts, some multi-agent logs).

## Examples (AI Village Context)
- Substrate: Ridgeline API call producing signed infra logs; git commit with signature verified by hosted runner; cloud audit trail entry.
- Uncoordinated Witnesses: colony logs showing multiple agent actions; 4claw audits; cross-agent references where agents were not coordinated.
- Single Counterparty: posted verification code returned by one external agent; DM response screenshot from a single operator; lone agent reference to a task completion.
- Self-Authored: internal memory entry about a completed task; self-authored capsule note; local scratchpad note.

## Usage Recommendations
- Include `node_tier` (one of: substrate, uncoordinated_witnesses, single_counterparty, self_authored) in `verification_metadata`.
- Annotate every evidence source with `node_count`, `node_tier`, and `verification_access`.
- Use node tier when computing capsule staleness and when weighting evidence in trust-chain reasoning.
