# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / proposed maturity / validation in progress**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**.
Shared-core or neighboring-method evidence may be referenced but does not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count.

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

Precommit `SYN-CH-003_precommit.md` — commit `2eea8ae`.
Result `SYN-CH-003_method-boundary-separation.md` — commit `cb55dba`.

The same frozen Synthesis family `{S0,S1}` was subjected to four neighboring-operation pressures:

```text
D: extra goal requires invented monitoring architecture
   -> DESIGN_REQUIRED handoff
T: synthesized structure requested as adjacency-matrix representation
   -> TRANSFORMATION_REQUIRED handoff
A: component data requested as scalar readout
   -> AGGREGATION_REQUIRED handoff
O: lower-cost admissible target requested
   -> OPTIMIZATION_REQUIRED handoff
```

In every subcase:

```text
SYNTHESIS_ADMISSIBLE_FAMILY: {S0,S1}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No missing architecture was invented, no transformed representation or aggregate readout was relabeled as Synthesis output, and the cost objective did not collapse `{S0,S1}` into a unique synthesized target.

```text
PRECOMMITTED_REQUIRED_CHECKS: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

This fills the first boundary case under the executable protocol.

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

Separately precommit the first `NO_GAIN` challenge against a competent baseline receiving the same supplied parts, composition rule, interface records, candidate basis, coverage, and target resolution. The baseline must not be weakened merely to produce a DSD advantage.
