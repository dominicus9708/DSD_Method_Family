# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / strongest-reasonable-baseline PASS / three external domains PASS / deterministic retrace PASS / validation in progress**

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

Success or failure of one case does not determine whether Synthesis must survive, merge, be absorbed, or be deleted. Method independence is evaluated separately by boundary structure, unique task/output/failure criteria, and maturity audit.

## Direct Protocol-v0.1 evidence

```text
SYN-CH-001  positive                           28/28 PASS
SYN-CH-002  negative/failure distinction       36/36 PASS
SYN-CH-003  executable method-boundary         46/46 PASS
SYN-CH-004  first NO_GAIN baseline attempt     33/35 FAIL
            FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
SYN-CH-005  corrected prospective baseline     37/37 PASS / NO_GAIN
SYN-CH-006  strongest-reasonable baseline      52/52 PASS / NO_GAIN
SYN-CH-007  deterministic same-project retrace 48/48 PASS
```

## External application evidence

```text
SYN-APP-001
  RFC 3986 / Internet identifier syntax
  40/40 PASS

SYN-APP-002
  BIPM SI Brochure 9th ed. v4.01 / physical metrology unit composition
  46/46 PASS

SYN-APP-003
  USB Type-C Cable and Connector Specification Release 2.0 mechanical subset
  physical connector assembly / mating interface
  PRECOMMIT 4159872
  RESULT 73faaa0
  ADMISSIBLE_FAMILY {M1,M2,M6,M7}
  M3 -> H2
  M4/M5 -> H1
  M8/M9/M10 -> H4
  44/44 PASS
```

`SYN-APP-003` is the first external case centered on physical plug/receptacle role compatibility, insertion orientation, and cable-end assignment rather than symbolic composition. It preserves:

```text
TYPE_C_COMPONENT_ADMITTED != DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT
REVERSIBLE_PLUG_ORIENTATION != ARBITRARY_ROTATIONAL_SYMMETRY
MECHANICAL_MATING != SOURCE_SINK_ROLE_ESTABLISHMENT
MECHANICAL_MATING != HOST_DEVICE_ROLE_ESTABLISHMENT
REVERSIBLE_CABLE_DIRECTION != POWER_ROLE_SYMMETRY
```

The case is version-specific to the frozen Release-2.0 mechanical subset and does not claim current Release-2.5 conformance, USB-IF certification, USB Power Delivery success, full electrical interoperability, durability, or data-rate capability.

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
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The evidence does not establish broad external generality, independent reproducibility, practical superiority, or maturity.

## Next development step

Run the first Synthesis maturity audit. The audit should inspect protocol stability, method-boundary integrity, negative/failure taxonomy, `NO_GAIN` honesty, three-domain external breadth, deterministic retraceability, and unresolved independence separately. It must not infer method preservation, merger, absorption, deletion, or promotion from raw PASS/FAIL counts alone.
