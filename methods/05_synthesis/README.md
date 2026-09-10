# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / first direct pilot PASS / validation in progress**

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

## Pre-protocol boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

The attacks required explicit composition-law/grouping, composition-equivalence/canonicalization, partial-residual, and process-scope guards without changing the method identity.

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

### Static Synthesis vs process/Dynamics

A final static composition may be admissible while a time-resolved assembly sequence remains untested.
Process feasibility requires an explicit process scope and, where relevant, Dynamics or a domain process model.

## First direct Protocol-v0.1 pilot — SYN-CH-001

The first positive challenge was separately precommitted before execution.

```text
PRECOMMIT:
  evidence/method_specific/synthesis/SYN-CH-001_precommit.md
  commit 4eeba2a

RESULT:
  evidence/method_specific/synthesis/SYN-CH-001_positive-chain-composition.md
  commit 71e5d5c
```

Frozen candidate result:

```text
K1 -> admissible
K2 -> admissible
K3 -> rejected {H3 readiness undefined}
K4 -> rejected {H2 interface mismatch}
K5 -> rejected {H2 interface mismatch}
K6 -> rejected {H2 interface mismatch}

SYNTHESIS_ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 28/28 PASS
```

The pilot directly shows that all components may be individually Formation-admitted while some compositions are still rejected, and that `DEFINED_ZERO` is not collapsed into `APPLICABLE_BUT_UNDEFINED`.
It also avoids automatic component-to-whole Property lift and makes no temporal process-feasibility claim.

## Protocol-v0.1 execution discipline

Protocol v0.1 locks, before outcome inspection:

```text
component identities/status sources
composition rule/source/arity/order/multiplicity
composition-law profile
grouping/parenthesization policy
candidate basis and composition coverage
target resolution
equivalence/canonicalization rule
interface and prerequisite rules
property-lift/redeclaration rule
retention/loss requirements
formation-model policy
assembly process scope
active DSD layers / domain bridges / external standard
```

Candidate IDs or syntax trees do not establish material uniqueness.
No algebraic law is inferred from notation alone.
A component property is not silently promoted to a whole property.
Static composability is not promoted to time-resolved process feasibility.

## Current evidence state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS: 1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

One positive constructed pilot does not establish external applicability, baseline superiority, reproducibility, independent validation, or maturity.

## Next development step

Separately precommit and execute a negative/failure challenge that distinguishes:

```text
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

The next challenge must preserve exhaustive-vs-non-exhaustive coverage and missing-input blocking rather than collapsing all non-success into a single failure state.
