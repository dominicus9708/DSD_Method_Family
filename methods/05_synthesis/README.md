# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / method-protocol evidence maturity established / SYN-IEP-001 prepared / validation in progress**

Task: compose supplied admitted components, properties, or partial structures into a larger construction under an explicit composition rule while preserving the conditions under which composition is legitimate.

Primary DSD sources: Formation Clause-VII-compatible composition interfaces, General Property typing, Static Aggregation only as a separate readout handoff, and Dynamics only when assembly/transition order is claim-relevant.

## Core method question

```text
Given supplied parts + an explicit composition rule + cross-part conditions,
which larger constructions are legitimately synthesizable,
and what structure/relations/statuses are retained or lost?
```

## Executable protocol and lineage

Current executable protocol: `PROTOCOL_v0.1.md`, creation commit `8787b24`.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Historical planning artifacts and failed challenges remain preserved rather than rewritten.

## Core guards

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY != AUTOMATIC_COMPOSABILITY
EXHAUSTIVE_COMPONENT_LIST != EXHAUSTIVE_COMPOSITION_SPACE
FORMATION_CLAUSE_VII_COMPOSITION != DOMAIN_SYNTHESIS_LEGITIMACY
AGGREGATE_READOUT != SYNTHESIZED_WHOLE
COMPONENT_PROPERTY != WHOLE_PROPERTY
candidate ID / syntax tree != material synthesized-target distinctness
PARTIAL_SYNTHESIS != completed synthesized target
STATIC_COMPOSITION_ORDER != TEMPORAL_ASSEMBLY_SEQUENCE
```

## Method boundaries

```text
Design: goals + constraints -> target/parts/architecture basis
Synthesis: supplied parts + supplied composition rule -> whole/composition space
Transformation: source/whole -> target representation/regime
Aggregation: structure/data -> declared readout
Optimization: admissible alternatives -> objective-based selection
Dynamics/domain process model: time-resolved assembly when claimed
```

The current corpus supports this operational separation under Protocol v0.1. It does not make method-registry survival, nonmerger, or permanent irreducibility an automatic consequence of case success.

## Evidence architecture

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
CLEAN_DISTRIBUTION_RECORD: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

Key direct records:

```text
SYN-CH-001  28/28 PASS  positive
SYN-CH-002  36/36 PASS  terminal-state distinction
SYN-CH-003  46/46 PASS  Design/Transformation/Aggregation/Optimization boundary
SYN-CH-004  33/35 FAIL  CHALLENGE_DESIGN_DEFECT preserved
SYN-CH-005  37/37 PASS / NO_GAIN
SYN-CH-006  52/52 PASS / NO_GAIN strongest-reasonable baseline
SYN-CH-007  48/48 PASS  deterministic_same_project retrace
```

External records:

```text
SYN-APP-001  RFC 3986 generic URI syntax                  40/40 PASS
SYN-APP-002  BIPM SI unit composition                     46/46 PASS
SYN-APP-003  USB Type-C physical mating interface         44/44 PASS
```

## SYN-AUD-001 maturity result

```text
AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
PRECOMMIT: ba966b5
RESULT: bae4388
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Axis summary:

```text
M1 PASS
M2 PASS
M3 PASS
M4 PASS
M5 CONDITIONAL_PASS
M6 PASS
M7 PASS
M8 PASS
M9 PASS
M10 UNRESOLVED_BUT_BOUNDED
M11 PRESENT_NONFATAL
M12 PASS
M13 PASS
M14 PASS
M15 PASS
```

`established` means **method/protocol evidence maturity under the current DSD method-family framework**. It does not establish independent evaluator validation, independent replication, broad inter-rater agreement, measured practical superiority, universal external generality, or permanent survival/nonmerger of Synthesis in every future registry revision.

## SYN-IEP-001 independent-evaluator infrastructure

The independent-evaluator packet is now prepared but not executed.

```text
REVIEWER_PACKET: SYN-IEP-001_reviewer-packet.md
  commit 6be55803
SUBMISSION_TEMPLATE: SYN-IEP-001_submission-template.md
  commit 079cdda0
REFERENCE_COMMITMENT: SYN-IEP-001_reference-commitment.md
  commit b785df0e
  SHA-256 db5d1c505c3ab2d614357525489f3b2a0dd2fc595fff1e715c69f48ceeb7073f
CLEAN_DISTRIBUTION_RECORD: SYN-IEP-001_distribution-record.md
  commit af622b9d
SEMANTIC_CHECKS: 24
CRITICAL_CHECKS: 10
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
```

The packet uses two held-out evaluator fixtures: BIPM SI unit composition (`S1-S6`) and USB Type-C physical mating (`P1-P6`). The hidden nonce and canonical reference key are escrowed outside the public method tree. Packet preparation creates no direct or independent validation evidence.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

## Next development step

Internal evidence generation is no longer the highest-value step. Wait for or obtain a genuinely separate `SYN-IEP-001` evaluator submission. The evaluator must freeze the completed submission before any hidden reference-key reveal. Only after the freeze should the project reveal escrow, verify the SHA-256 commitment, and run the predeclared 24-check independent-evidence scoring. Until then, independence remains unestablished.
