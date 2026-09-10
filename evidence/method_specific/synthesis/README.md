# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / method-protocol evidence maturity established / SYN-IEP-001 prepared / validation in progress**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**. Shared-core or neighboring-method evidence may be referenced but does not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
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
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

`SYN-AUD-001` is an Audit meta-record and `SYN-IEP-001` preparation is evaluator infrastructure. Neither increments direct-pilot, external-application, or reproducibility counts.

## Protocol and planning artifacts

- `methods/05_synthesis/PROTOCOL_v0.1.md` — first executable protocol, creation commit `8787b24`.
- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — 16 pre-protocol attacks.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — non-breaking refinements.
- `methods/05_synthesis/PLANNING.md` — development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronology.

## Direct Protocol-v0.1 evidence

```text
SYN-CH-001  positive                           28/28 PASS
SYN-CH-002  negative/failure distinction       36/36 PASS
SYN-CH-003  executable method-boundary         46/46 PASS
SYN-CH-004  first NO_GAIN attempt              33/35 FAIL
            FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
SYN-CH-005  corrected competent baseline       37/37 PASS / NO_GAIN
SYN-CH-006  strongest-reasonable baseline      52/52 PASS / NO_GAIN
SYN-CH-007  deterministic retrace               48/48 PASS
```

`SYN-CH-004` remains preserved as a failed challenge design. `SYN-CH-006` established the strongest-reasonable-baseline category at constructed-evidence level only. `SYN-CH-007` establishes deterministic same-project retraceability, not independent replication.

## External application evidence

```text
SYN-APP-001  RFC 3986 generic URI composition          40/40 PASS
SYN-APP-002  BIPM SI unit composition                  46/46 PASS
SYN-APP-003  USB Type-C physical mating interface      44/44 PASS
```

The three external domains are materially different at the frozen task resolution: URI grammar, SI unit algebra/scale composition, and physical connector mating/orientation.

## Reproducibility / retrace evidence

### SYN-CH-007 — deterministic same-project retrace of SYN-APP-001

```text
PRECOMMIT: 9bbcadf
RESULT: 7256456
RETRACE_TARGET: SYN-APP-001
REPRODUCIBILITY_LEVEL: deterministic_same_project
RECONSTRUCTED_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 48/48 PASS
INDEPENDENT_REPLICATION: not established
```

## Maturity audit

### SYN-AUD-001 — first Synthesis maturity review

```text
AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
PRECOMMIT: ba966b5
RESULT: bae4388
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Maturity-axis result:

```text
M1  PASS
M2  PASS
M3  PASS
M4  PASS
M5  CONDITIONAL_PASS
M6  PASS
M7  PASS
M8  PASS
M9  PASS
M10 UNRESOLVED_BUT_BOUNDED
M11 PRESENT_NONFATAL
M12 PASS
M13 PASS
M14 PASS
M15 PASS
```

The established label means **method/protocol evidence maturity within the current DSD method-family framework**. It does not establish independent validation, independent replication, practical superiority, universal external generality, or permanent method-registry survival/nonmerger.

## Independent evaluator infrastructure

### SYN-IEP-001 — prepared, not executed

```text
REVIEWER_PACKET:
  evidence/method_specific/synthesis/SYN-IEP-001_reviewer-packet.md
  commit: 6be55803

SUBMISSION_TEMPLATE:
  evidence/method_specific/synthesis/SYN-IEP-001_submission-template.md
  commit: 079cdda0

REFERENCE_COMMITMENT:
  evidence/method_specific/synthesis/SYN-IEP-001_reference-commitment.md
  commit: b785df0e
  SHA-256: db5d1c505c3ab2d614357525489f3b2a0dd2fc595fff1e715c69f48ceeb7073f

CLEAN_DISTRIBUTION_RECORD:
  evidence/method_specific/synthesis/SYN-IEP-001_distribution-record.md
  commit: af622b9d

PACKET_TASKS:
  Task S — BIPM SI unit-composition held-out fixture S1-S6
  Task P — USB Type-C physical-mating held-out fixture P1-P6

SEMANTIC_CHECKS: 24
CRITICAL_CHECKS: 10
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
```

The secret nonce and canonical reference key are held outside the public Synthesis tree. They may be revealed only after an eligible evaluator freezes a submission under an immutable or time-ordered identifier. The current project assistant/session is not eligible to self-score as independent evidence.

## Protocol-v0.1 core guards

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

## Method-independence / survival discipline

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
EXTERNAL_PASS != PERMANENT_INDEPENDENCE_PROOF
RETRACE_PASS != METHOD_IRREDUCIBILITY_PROOF
```

The current corpus supports operational separation from Design, Transformation, Aggregation, and Optimization under Protocol v0.1. Future registry reclassification remains a separate structural question.

## Direct-evidence case convention

```text
SYN-CH-###   constructed Synthesis challenges and dedicated retrace cases
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific audit / maturity records
SYN-IEP-###  independent evaluator packet infrastructure
```

## Immediate next evidence task

Do not create more same-project evidence merely to fill volume. The next high-value event is a **genuinely separate SYN-IEP-001 evaluator submission**. Freeze the evaluator's completed submission before revealing the hidden reference key; only then verify the SHA-256 commitment and score the predeclared 24 semantic checks. Until that event, independent validation and replication remain unestablished.
