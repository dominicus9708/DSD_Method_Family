# 05. DSD Synthesis / DSD 합성론

Status: **planning / proposed / Step 1 task interface complete**

Task: compose supplied admitted components, properties, or partial structures into a larger construction under an explicit composition rule while preserving the conditions under which composition is legitimate.

Primary DSD sources: Formation Clause-VII-compatible composition interfaces, General Property typing, Static Aggregation when analytic outputs are combined, and Dynamics only when assembly/transition order is claim-relevant.

## Core method question

```text
Given supplied parts + an explicit composition rule + cross-part conditions,
which larger constructions are legitimately synthesizable,
and what structure/relations/statuses are retained or lost?
```

## Step-1 planning locks

The first Synthesis-specific task interface is now drafted at:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)

Planning and chronology:

- [`PLANNING.md`](PLANNING.md)
- [`WORKLOG.md`](WORKLOG.md)

Direct-evidence lane:

- [`../../evidence/method_specific/synthesis/`](../../evidence/method_specific/synthesis/)

Current guards:

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
```

## Initial output levels

```text
SYNTHESIS_SPACE
SYNTHESIZED_TARGET
UNIQUE_SYNTHESIZED_TARGET
PARTIAL_SYNTHESIS
```

## Initial terminal statuses

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

`SYNTHESIS_INFEASIBLE` requires exhaustive composition coverage or an explicit impossibility argument.
A non-exhaustive failure to find a valid composition is not global infeasibility.

## Three-ledger separation

```text
TERMINAL_SYNTHESIS_STATUS

SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

SYNTHESIS_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Maturity is a later DSD Audit decision and is not inferred from these ledgers.

## Main method boundaries

### Synthesis vs Design

Design constructs or filters a target/design space from goals and constraints.
Synthesis consumes supplied parts and a supplied composition rule to build a larger whole/composition space.
If the task invents missing parts, connectors, or architecture to meet a goal, that operation belongs to Design or a Design handoff.

### Synthesis vs Transformation

Synthesis is parts-to-whole composition.
Transformation is a source-to-target mapping across representations, schemas, models, or regimes.

### Synthesis vs Aggregation

Aggregation constructs a declared readout.
A finite sum or analytic output is not automatically a substantive synthesized whole.

### Synthesis vs Optimization

Synthesis forms the legitimate composition family.
Optimization chooses among already legitimate alternatives under an objective.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: not established
DIRECT_SYNTHESIS_PILOTS: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

Planning artifacts do not count as direct Synthesis validation.

## Next development step

Pressure-test the Step-1 interface with pre-protocol boundary counterexamples against:

```text
Design
Transformation
Aggregation
Optimization
implicit component-to-whole property lifting
```

Apply only non-breaking refinements that those counterexamples actually require, then freeze the first executable `Synthesis Protocol v0.1`.
