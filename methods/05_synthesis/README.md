# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / strongest-reasonable-baseline PASS / two external domains PASS / deterministic retrace PASS / validation in progress**

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
SYN-CH-001  positive                           28/28 PASS
SYN-CH-002  negative/failure distinction       36/36 PASS
SYN-CH-003  executable method-boundary         46/46 PASS
SYN-CH-004  first NO_GAIN baseline attempt     33/35 FAIL
            FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
SYN-CH-005  corrected prospective baseline     37/37 PASS / NO_GAIN
SYN-CH-006  strongest-reasonable baseline      52/52 PASS / NO_GAIN
SYN-CH-007  deterministic same-project retrace 48/48 PASS
```

`SYN-CH-006` established the strongest-reasonable-baseline category only at constructed-evidence level. `SYN-CH-007` establishes deterministic same-project retraceability only.

## External application evidence

### SYN-APP-001 — RFC 3986 generic URI syntax

```text
PRECOMMIT: 29ea45a
RESULT: 6985246
EXTERNAL_DOMAIN: Internet identifier syntax
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 40/40 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

The RFC itself supplies the generic component grammar; `ABSENT != PRESENT_EMPTY` and declared-component roundtrip are preserved without upgrading generic syntax to scheme-specific validity.

### SYN-APP-002 — BIPM SI unit composition

```text
PRECOMMIT: 46479ae
RESULT: c504d53
EXTERNAL_STANDARD: SI Brochure 9th ed. v4.01 (2026)
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
U6/U8/U10 -> {H4}
U11/U12 -> {H2}; H3-H5 NOT_REACHED
SCORE: 46/46 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

The BIPM source supplies derived-unit products of powers, coherent special-name equivalences, prefix formation, exponent propagation, compound-prefix prohibition, and the kilogram/gram mass-prefix rule. The application preserves:

```text
SAME_DIMENSION != SAME_UNIT_SCALE
VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT
PREFIX_COMPONENT_ADMITTED != PREFIX_COMPOSITION_FORM_LEGAL
SI_UNIT_COMPOSITION != PHYSICAL_MEASUREMENT_VALIDITY
```

No calibration, uncertainty, traceability, experimental-realization, or physical-law claim is absorbed.

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
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The evidence does not establish broad external generality, independent reproducibility, practical superiority, or maturity.

## Next development step

Add a third materially different external Synthesis domain, preferably involving nontrivial physical/component compatibility or assembly constraints rather than mainly symbolic grammar. Then consider the first Synthesis maturity audit only after this broader pressure is recorded.
