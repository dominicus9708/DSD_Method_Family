# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / positive + negative/failure + boundary pilots PASS / validation in progress**

Task: compose supplied admitted components, properties, or partial structures into a larger construction under an explicit composition rule while preserving the conditions under which composition is legitimate.

Primary DSD sources: Formation Clause-VII-compatible composition interfaces, General Property typing, Static Aggregation only as a separate readout handoff, and Dynamics only when assembly/transition order is claim-relevant.

## Core method question

```text
Given supplied parts + an explicit composition rule + cross-part conditions,
which larger constructions are legitimately synthesizable,
and what structure/relations/statuses are retained or lost?
```

## Executable protocol and lineage

Current executable protocol:

- `PROTOCOL_v0.1.md`, creation commit `8787b24`.

Historical artifacts remain preserved:

- `TASK_INTERFACE_v0.1-draft.md`
- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`
- `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`
- `PLANNING.md`
- `WORKLOG.md`

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

## Output and terminal states

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
```

`SYNTHESIS_INFEASIBLE` requires exhaustive composition coverage or a sufficient impossibility argument. Non-exhaustive closure failure remains underdetermined. Missing claim-required input may yield `SYNTHESIS_BLOCKED + CONFORMANT`.

## Three-ledger separation

```text
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

### SYN-CH-001 — positive composition

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

### SYN-CH-002 — negative/failure distinction

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I -> SYNTHESIS_INFEASIBLE
U -> SYNTHESIS_UNDERDETERMINED
B -> SYNTHESIS_BLOCKED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
SCORE: 36/36 PASS
```

This preserves exhaustive rejection, insufficient closure coverage, and missing required input as distinct conditions.

### SYN-CH-003 — executable method-boundary challenge

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
BASE SYNTHESIS FAMILY: {S0,S1}
```

Four mixed-workflow pressures were separated without changing the Synthesis family:

```text
extra goal requiring new monitoring architecture -> DESIGN_REQUIRED
adjacency-matrix representation request          -> TRANSFORMATION_REQUIRED
scalar readout request                           -> AGGREGATION_REQUIRED
lower-cost selection objective                   -> OPTIMIZATION_REQUIRED
```

In every subcase:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No missing part/connector was fabricated, no representation conversion or scalar readout was relabeled as Synthesis, and the cost objective did not turn `{S0,S1}` into a unique synthesized target.

```text
SCORE: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 3
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The current constructed pilots do not establish external applicability, baseline superiority, reproducibility, independent validation, or maturity.

## Next development step

Separately precommit the first `NO_GAIN` case against a competent baseline that receives the same components, composition rule, interface records, candidate basis, coverage, and target resolution. Do not weaken the baseline to manufacture a DSD advantage.
