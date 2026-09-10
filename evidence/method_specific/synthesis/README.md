# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / method-protocol evidence maturity established by SYN-AUD-001 / validation in progress**

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
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

`SYN-AUD-001` is an Audit meta-record and does not increment direct-pilot, external-application, or reproducibility counts.

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

### SYN-APP-001 — RFC 3986 generic URI composition

```text
EXTERNAL_STANDARD: RFC 3986 / STD 66
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
PRECOMMIT: 29ea45a
RESULT: 6985246
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 40/40 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

### SYN-APP-002 — BIPM SI unit composition

```text
EXTERNAL_STANDARD: BIPM SI Brochure, 9th ed., version 4.01 (2026)
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
PRECOMMIT: 46479ae
RESULT: c504d53
ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
SCORE: 46/46 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

### SYN-APP-003 — USB Type-C physical mating interface

```text
FROZEN_EXTERNAL_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 (August 2019),
  mechanical mating/orientation subset
SUPPORTING_SOURCE: USB-IF Type-C overview
EXTERNAL_DOMAIN: physical connector assembly / USB Type-C mating interface
PRECOMMIT: 4159872
RESULT: 73faaa0
ADMISSIBLE_FAMILY: {M1,M2,M6,M7}
SCORE: 44/44 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
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

The weakest remaining evidence axis is independence. Prepare `SYN-IEP-001` as independent-evaluator infrastructure without counting packet preparation as validation. Only a genuinely separate immutable evaluator submission may change `INDEPENDENT_SYNTHESIS_VALIDATION` or `INDEPENDENT_REPLICATION` in a later audit.
