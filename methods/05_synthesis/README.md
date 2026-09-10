# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / positive + negative/failure + boundary + NO_GAIN evidence present / validation in progress**

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
Historical planning artifacts remain preserved: `TASK_INTERFACE_v0.1-draft.md`, `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`, `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`, `PLANNING.md`, and `WORKLOG.md`.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

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

## Output / terminal / ledger structure

```text
OUTPUT_LEVELS:
  SYNTHESIS_SPACE
  SYNTHESIZED_TARGET
  UNIQUE_SYNTHESIZED_TARGET
  PARTIAL_SYNTHESIS

TERMINAL_SYNTHESIS_STATUS:
  SYNTHESIS_ADMISSIBLE
  SYNTHESIS_INFEASIBLE
  SYNTHESIS_UNDERDETERMINED
  SYNTHESIS_BLOCKED

THREE LEDGERS:
  TERMINAL_SYNTHESIS_STATUS
  SYNTHESIS_PROTOCOL_CONFORMANCE
  SYNTHESIS_METHOD_GAIN_STATUS
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

## Direct Protocol-v0.1 evidence

```text
SYN-CH-001
  positive
  PRECOMMIT 4eeba2a
  RESULT 71e5d5c
  28/28 PASS

SYN-CH-002
  negative/failure terminal distinction
  PRECOMMIT 09fc616
  RESULT 7dac87c
  36/36 PASS
  INFEASIBLE != UNDERDETERMINED != BLOCKED

SYN-CH-003
  executable method-boundary
  PRECOMMIT 2eea8ae
  RESULT cb55dba
  46/46 PASS
  Design / Transformation / Aggregation / Optimization handoffs preserved

SYN-CH-004
  first NO_GAIN baseline attempt
  PRECOMMIT 1c77a0e
  FIRST RESULT 29730a5
  POSTEXECUTION AUDIT fe55899
  33/35 FAIL
  FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
  Protocol failure not inferred

SYN-CH-005
  corrected prospective NO_GAIN baseline challenge
  PRECOMMIT 3c6f323
  RESULT f062d3f
  37/37 PASS
  DSD family = B0 family = {R1,R2}
  TERMINAL: SYNTHESIS_ADMISSIBLE
  CONFORMANCE: CONFORMANT
  GAIN: NO_GAIN
```

The `SYN-CH-004` predecessor is intentionally preserved. Its Q5 fixture omitted the middle component's readiness record while expecting no H4 failure. `SYN-CH-005` repaired this prospectively under a new Case ID by freezing explicit readiness records before execution.

The successful `SYN-CH-005` comparison established no measured DSD gain over `B0_TYPED_CHAIN_CHECKER` on the frozen dimensions:

```text
G1 status distinction       NOT_ESTABLISHED
G2 failure traceability     NOT_ESTABLISHED
G3 composition closure      NOT_ESTABLISHED
G4 target distinctness      NOT_ESTABLISHED
G5 retraceability           NOT_ESTABLISHED
```

`NO_GAIN` is a valid evidence result and is not treated as method failure.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The evidence so far is constructed and does not establish external applicability, cross-domain generality, strongest-reasonable-baseline coverage, reproducibility, independent validation, practical superiority, or maturity.

## Next development step

Separately precommit and execute a broader strongest-reasonable-baseline comparison. Use a richer Synthesis task that activates multiple method-specific dimensions at once, preferably composition equivalence/grouping together with property-lift, relation-retention, partial-residual, or formation-effect distinctions. The baseline must receive the same information and a further `NO_GAIN` outcome must remain acceptable.
