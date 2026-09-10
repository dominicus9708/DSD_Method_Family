# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / proposed maturity / validation in progress**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**.

Shared-core evidence, Design evidence, Transformation evidence, Aggregation evidence, or other neighboring-method results may be referenced but do not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 2
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Protocol establishment does not increase the direct-pilot count.
`SYN-CH-001` and `SYN-CH-002` are the first two direct Protocol-v0.1 constructed pilots.

## Protocol and planning artifacts

- `methods/05_synthesis/PROTOCOL_v0.1.md` — first executable protocol, creation commit `8787b24`.
- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — Step-2 pre-protocol boundary attack, 16 cases.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — Step-2 non-breaking interface refinement.
- `methods/05_synthesis/PLANNING.md` — current development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronological worklog.

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

The pre-protocol artifacts remain preserved and are not retroactively counted as Protocol-v0.1 direct validation.

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

### `SYN-CH-001` — positive symbolic chain composition

Precommit `SYN-CH-001_precommit.md` — commit `4eeba2a`.
Result `SYN-CH-001_positive-chain-composition.md` — commit `71e5d5c`.

```text
K1 -> admissible
K2 -> admissible
K3 -> rejected {H3}
K4 -> rejected {H2}
K5 -> rejected {H2}
K6 -> rejected {H2}

SYNTHESIS_ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 28/28 PASS
```

The case preserves `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED`, rejects interface-incompatible arrangements despite individual component admission, avoids automatic whole-Property lift, and makes no temporal process-feasibility claim.

### `SYN-CH-002` — negative/failure terminal-status distinction

Precommit `SYN-CH-002_precommit.md` — commit `09fc616`.
Result `SYN-CH-002_terminal-failure-distinction.md` — commit `7dac87c`.

Three frozen subcases produced:

```text
I: exhaustive all rejected
   -> SYNTHESIS_INFEASIBLE / CONFORMANT / NOT_ASSESSED

U: locally admissible U1 + non-exhaustive coverage
   + UNIQUE_SYNTHESIZED_TARGET requested
   -> SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED

B: required composition rule unavailable
   -> SYNTHESIS_BLOCKED / CONFORMANT / NOT_ASSESSED

PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
CHALLENGE_VERDICT: PASS
```

The case directly preserves:

```text
REJECTED_UNDER_EXHAUSTIVE_COVERAGE
!= INSUFFICIENT_COVERAGE_FOR_CLOSURE
!= MISSING_REQUIRED_INPUT

local admissibility
!= requested output-level closure
```

No Protocol-v0.1 revision was required by the case.

## Protocol-v0.1 core guards

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY

EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE

FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY

AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE

COMPONENT_PROPERTY
!= WHOLE_PROPERTY

candidate ID / syntax tree
!= material synthesized-target distinctness

PARTIAL_SYNTHESIS
!= completed synthesized target

STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

## Direct-evidence case convention

```text
SYN-CH-###   constructed Synthesis challenges
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific audit / maturity records
SYN-IEP-###  independent evaluator packet infrastructure
```

A challenge whose expected result or score matters must be separately precommitted before evaluation.
Pre-protocol planning attacks retain the `SYN-BND-DRAFT-*` namespace and remain planning evidence only.

## Minimum evidence architecture

A future promotion consideration should accumulate, at minimum:

1. a dedicated executable Synthesis protocol;
2. positive cases;
3. negative/failure cases;
4. method-boundary cases;
5. `NO_GAIN` cases;
6. method-appropriate reproducibility/retraceability records;
7. at least one external or independently generated application;
8. a strongest-reasonable-baseline comparison when applicable.

These are evidence categories, not an automatic maturity certificate.

## Immediate next direct-evidence task

Separately precommit a direct method-boundary challenge under Protocol v0.1.
It should pressure at least hidden Design, Transformation, Aggregation, and Optimization handoffs and verify that Synthesis neither fabricates missing architecture nor absorbs neighboring-method verdicts.
