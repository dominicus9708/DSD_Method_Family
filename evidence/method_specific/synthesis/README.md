# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / proposed maturity / validation in progress**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**.
Shared-core or neighboring-method evidence may be referenced but does not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count.
A failed direct challenge remains a historical direct attempt but does not fill its successful evidence category.

## Protocol and planning artifacts

- `methods/05_synthesis/PROTOCOL_v0.1.md` — first executable protocol, creation commit `8787b24`.
- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — 16 pre-protocol attacks.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — non-breaking refinements.
- `methods/05_synthesis/PLANNING.md` — development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronology.

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

## Pre-protocol boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

## Direct Protocol-v0.1 evidence

### SYN-CH-001 — positive symbolic chain composition

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
K1 -> admissible
K2 -> admissible
K3 -> rejected {H3 readiness undefined}
K4-K6 -> rejected {H2 interface mismatch}
SYNTHESIS_ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 28/28 PASS
```

Directly preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED`, individual admission versus composability, no automatic whole-Property lift, and static-versus-temporal scope separation.

### SYN-CH-002 — negative/failure terminal-status distinction

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I: exhaustive all rejected -> SYNTHESIS_INFEASIBLE
U: non-exhaustive uniqueness closure -> SYNTHESIS_UNDERDETERMINED
B: required composition rule unavailable -> SYNTHESIS_BLOCKED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
```

Directly preserved `REJECTED_UNDER_EXHAUSTIVE_COVERAGE != INSUFFICIENT_COVERAGE_FOR_CLOSURE != MISSING_REQUIRED_INPUT` and `local admissibility != requested output-level closure`.

### SYN-CH-003 — executable method-boundary separation

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
SYNTHESIS_ADMISSIBLE_FAMILY: {S0,S1}
D -> DESIGN_REQUIRED
T -> TRANSFORMATION_REQUIRED
A -> AGGREGATION_REQUIRED
O -> OPTIMIZATION_REQUIRED
ALL TERMINAL: SYNTHESIS_ADMISSIBLE
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
```

This fills the first successful executable boundary case.

### SYN-CH-004 — first NO_GAIN baseline attempt, challenge-design defect preserved

```text
PRECOMMIT: 1c77a0e
FIRST RESULT: 29730a5
POSTEXECUTION AUDIT: fe55899
STRICT SCORE: 33/35
CHALLENGE_VERDICT: FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
```

The frozen rule required `H4 readiness(Y) is defined`, but candidate `Q5 = (M1 ⊙ SRC) ⊙ SNK` placed `SRC` in the middle position while `SRC` had no frozen readiness record. The precommit therefore incorrectly expected `{H2,H3}` instead of `{H2,H3,H4}`. The first result's attempted role-specific exception was not frozen and is invalid. This case does not fill the successful NO_GAIN or baseline-comparison category and does not imply Protocol-v0.1 failure.

### SYN-CH-005 — corrected prospective NO_GAIN baseline case

```text
PRECOMMIT: 3c6f323
RESULT: f062d3f
PREDECESSOR FAILURE PRESERVED: SYN-CH-004
R1 -> admissible / NONE
R2 -> admissible / NONE
R3 -> rejected / {H4}
R4 -> rejected / {H2}
R5 -> rejected / {H2,H3}
DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
DSD TERMINAL: SYNTHESIS_ADMISSIBLE
DSD CONFORMANCE: CONFORMANT
DSD METHOD GAIN: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 37/37 PASS
```

`B0_TYPED_CHAIN_CHECKER` received the same components, admission flags, interfaces, readiness status classes, rule, candidate basis, coverage, grouping, and target resolution. It preserved all five frozen gain dimensions, so:

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
G3 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
G4 TARGET_DISTINCTNESS_GAIN: NOT_ESTABLISHED
G5 RETRACEABILITY_GAIN: NOT_ESTABLISHED
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

This fills the first successful dedicated NO_GAIN case and first successful competent-baseline comparison at constructed-fixture level. It does not yet establish the broader strongest-reasonable-baseline category.

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

## Direct-evidence case convention

```text
SYN-CH-###   constructed Synthesis challenges
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific audit / maturity records
SYN-IEP-###  independent evaluator packet infrastructure
```

A challenge whose expected result matters must be separately precommitted before evaluation. Historical failed or superseded challenge designs are preserved rather than rewritten.

## Minimum evidence architecture

A future promotion consideration should accumulate, at minimum: dedicated protocol; positive; negative/failure; boundary; `NO_GAIN`; reproducibility/retrace; external/independent application; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not an automatic maturity certificate.

## Immediate next direct-evidence task

Run a separately precommitted broader strongest-reasonable-baseline comparison on a materially richer Synthesis task. The baseline must remain competent and receive the same composition-relevant information. The fixture should activate multiple Synthesis-specific dimensions at once, preferably composition equivalence/grouping plus property-lift, relation-retention, partial-residual, or formation-effect distinctions. A second `NO_GAIN` outcome must remain acceptable.
