# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / positive + terminal-failure pilots PASS / validation in progress**

Task: compose supplied admitted components, properties, or partial structures into a larger construction under an explicit composition rule while preserving the conditions under which composition is legitimate.

Primary DSD sources: Formation Clause-VII-compatible composition interfaces, General Property typing, Static Aggregation when analytic outputs are combined, and Dynamics only when assembly/transition order is claim-relevant.

## Core method question

```text
Given supplied parts + an explicit composition rule + cross-part conditions,
which larger constructions are legitimately synthesizable,
and what structure/relations/statuses are retained or lost?
```

## Executable protocol and lineage

Current executable protocol:

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md), creation commit `8787b24`.

Historical planning artifacts remain preserved:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Planning and chronology:

- [`PLANNING.md`](PLANNING.md)
- [`WORKLOG.md`](WORKLOG.md)

Direct-evidence lane:

- [`../../evidence/method_specific/synthesis/`](../../evidence/method_specific/synthesis/)

## Core guards

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

## Protocol-v0.1 output levels

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

## Terminal statuses

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

`SYNTHESIS_INFEASIBLE` requires exhaustive composition coverage or an explicit impossibility argument sufficient for the frozen scope.
A non-exhaustive failure-to-find is not global infeasibility.
A missing claim-required composition rule or bridge may produce `SYNTHESIS_BLOCKED + CONFORMANT` when the missing input is correctly exposed rather than fabricated.

## Three-ledger separation

```text
TERMINAL_SYNTHESIS_STATUS
SYNTHESIS_PROTOCOL_CONFORMANCE
SYNTHESIS_METHOD_GAIN_STATUS
```

Maturity remains a later DSD Audit decision.

## Method boundaries

```text
Design: goals + constraints -> target/design space
Synthesis: supplied parts + supplied composition rule -> whole/composition space
Transformation: source -> target representation/regime
Aggregation: structure/data -> declared readout
Optimization: admissible alternatives -> objective-based selection
Dynamics/domain process model: time-resolved assembly when claimed
```

## Direct Protocol-v0.1 evidence

### SYN-CH-001 — positive composition

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

This case preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED` and `individual admission != composability`.

### SYN-CH-002 — terminal failure distinction

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c

I: exhaustive {I1,I2}, all rejected {H2}
   -> SYNTHESIS_INFEASIBLE / CONFORMANT / NOT_ASSESSED

U: non-exhaustive {U1,U2}, U1 admissible, uniqueness requested
   -> SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED

B: required composition rule unavailable
   -> SYNTHESIS_BLOCKED / CONFORMANT / NOT_ASSESSED

SCORE: 36/36 PASS
```

This case shows that local admissibility does not establish the requested output-level closure, and that missing required input is not the same as an ordinary candidate rejection.
No Protocol-v0.1 revision was required.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 2
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The current pilots establish only limited constructed-fixture behavior. They do not establish external applicability, baseline superiority, reproducibility, independent validation, or maturity.

## Next development step

Separately precommit and execute a direct method-boundary challenge under Protocol v0.1.
The challenge should force explicit handoffs for hidden Design, Transformation, Aggregation, and Optimization operations rather than allowing Synthesis to absorb those operations or their verdicts.
