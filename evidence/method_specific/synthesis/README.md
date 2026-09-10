# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / first external application PASS / validation in progress**

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
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count. A failed direct challenge remains a historical direct attempt but does not fill its successful evidence category. External applications are tracked separately from constructed direct pilots.

## Protocol and planning artifacts

- `methods/05_synthesis/PROTOCOL_v0.1.md` — first executable protocol, creation commit `8787b24`.
- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — 16 pre-protocol attacks.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — non-breaking refinements.
- `methods/05_synthesis/PLANNING.md` — development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronology.

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
K1,K2 -> admissible
K3 -> rejected {H3}
K4-K6 -> rejected {H2}
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

### SYN-CH-002 — negative/failure terminal-status distinction

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I: exhaustive all rejected -> SYNTHESIS_INFEASIBLE
U: non-exhaustive uniqueness closure -> SYNTHESIS_UNDERDETERMINED
B: required composition rule unavailable -> SYNTHESIS_BLOCKED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
SCORE: 36/36 PASS
```

### SYN-CH-003 — executable method-boundary separation

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
BASE FAMILY: {S0,S1}
D -> DESIGN_REQUIRED
T -> TRANSFORMATION_REQUIRED
A -> AGGREGATION_REQUIRED
O -> OPTIMIZATION_REQUIRED
SCORE: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
```

### SYN-CH-004 — failed first NO_GAIN baseline attempt

```text
PRECOMMIT: 1c77a0e
FIRST RESULT: 29730a5
POSTEXECUTION AUDIT: fe55899
STRICT SCORE: 33/35 FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
```

The frozen H4 required `readiness(Y)` while `Q5` placed `SRC` in the middle position without a frozen readiness record. The attempted post-hoc exception was rejected. The case is preserved and does not fill a successful NO_GAIN or baseline-comparison category.

### SYN-CH-005 — corrected prospective NO_GAIN baseline case

```text
PRECOMMIT: 3c6f323
RESULT: f062d3f
DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 37/37 PASS
```

### SYN-CH-006 — broader strongest-reasonable-baseline comparison

```text
PRECOMMIT: 4a6c1fe
RESULT: 8ad51b5
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
RAW DSD FAMILY: {A1,A2,A3,A4}
RAW B1 FAMILY: {A1,A2,A3,A4}
CANONICAL DSD FAMILY: {C0,C1}
CANONICAL B1 FAMILY: {C0,C1}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 52/52 PASS
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

The richer fixture simultaneously activated explicit whole-Property lift, status distinctions, staged dependency, supplied associativity/grouping equivalence, relation retention, formation effect, and raw/canonical closure. The competent B1 baseline received the same claim-relevant information and matched all frozen dimensions.

## External application evidence

### SYN-APP-001 — RFC 3986 generic URI composition

```text
EXTERNAL_STANDARD: RFC 3986 / STD 66
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
PRECOMMIT: 29ea45a
RESULT: 6985246
CANDIDATES: R1-R12
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
R5 -> {H2}
R6 -> {H2}
R7 -> {H1}
R8 -> {H4}
R9 -> {H3}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

This application uses an externally supplied generic composition grammar rather than a project-invented domain rule. It preserves `ABSENT != PRESENT_EMPTY` for authority/query/fragment states and rejects candidates that are generically parseable only under a different component decomposition. The scope remains RFC-3986 generic syntax only; no scheme-specific validity, dereference, security, or normalization claim is inferred.

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

A challenge whose expected result matters must be separately precommitted before evaluation. Historical failed or superseded challenge designs are preserved rather than rewritten. Success or failure of a single case does not by itself determine whether a method must survive, merge, or be deleted; method independence is a separate boundary/maturity question.

## Minimum evidence architecture

A future promotion consideration should accumulate, at minimum: dedicated protocol; positive; negative/failure; boundary; `NO_GAIN`; reproducibility/retrace; external/independent application; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not an automatic maturity certificate.

## Immediate next direct-evidence task

Create a dedicated deterministic same-project retrace/reproducibility case against the immutable `SYN-APP-001` source/precommit/result chain. After that, add a second materially different external domain before any maturity audit.
