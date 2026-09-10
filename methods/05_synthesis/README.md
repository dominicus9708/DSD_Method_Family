# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / strongest-reasonable-baseline PASS / first external application PASS / deterministic retrace PASS / validation in progress**

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

Success or failure of one case does not determine whether Synthesis must survive, merge, or be deleted. Method independence is evaluated separately by boundary structure, unique task/output/failure criteria, and later maturity audit.

## Direct Protocol-v0.1 evidence

```text
SYN-CH-001
  positive
  28/28 PASS
  PRECOMMIT 4eeba2a
  RESULT 71e5d5c

SYN-CH-002
  negative/failure distinction
  36/36 PASS
  PRECOMMIT 09fc616
  RESULT 7dac87c

SYN-CH-003
  executable method-boundary
  46/46 PASS
  PRECOMMIT 2eea8ae
  RESULT cb55dba

SYN-CH-004
  first NO_GAIN baseline attempt
  33/35 FAIL
  FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
  PRECOMMIT 1c77a0e
  FIRST RESULT 29730a5
  POSTEXECUTION AUDIT fe55899

SYN-CH-005
  corrected prospective NO_GAIN case
  37/37 PASS
  PRECOMMIT 3c6f323
  RESULT f062d3f
  DSD family = B0 family = {R1,R2}
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NO_GAIN

SYN-CH-006
  broader strongest-reasonable-baseline comparison
  52/52 PASS
  PRECOMMIT 4a6c1fe
  RESULT 8ad51b5
  RAW DSD = B1 = {A1,A2,A3,A4}
  CANONICAL DSD = B1 = {C0,C1}
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level

SYN-CH-007
  deterministic same-project retrace of SYN-APP-001
  48/48 PASS
  PRECOMMIT 9bbcadf
  RESULT 7256456
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

## External application evidence

```text
SYN-APP-001
  external source: RFC 3986 / STD 66 generic URI syntax
  external domain: Internet identifier syntax
  precommit 29ea45a
  result 6985246
  candidates R1-R12
  admissible family {R1,R2,R3,R4,R10,R11,R12}
  40/40 PASS
  SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

`SYN-APP-001` is the first case in which domain composition legitimacy is not invented by the project. The external grammar supplies generic URI component order, authority/path branch conditions, scheme/path/query/fragment syntax, and enough structure to distinguish absent from present-empty optional components. The result remains generic-syntax-only and is not upgraded to scheme-specific validity, dereference success, normalization equivalence, or security.

`SYN-CH-007` then retraced the immutable Protocol/RFC/precommit/result chain and reconstructed all twelve candidate verdicts, failure staging, status distinctions, closure, scope guards, and three ledgers exactly. This establishes only deterministic same-project retraceability, not independence.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
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
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The evidence does not establish broad external generality, independent reproducibility, practical superiority, or maturity.

## Next development step

Add a second materially different external Synthesis domain before considering a maturity audit. Prefer a stable physical, engineering, scientific, legal, or other non-URI source that supplies its own composition/assembly legitimacy. Keep application outcome separate from any method survival, merger, or deletion decision.
