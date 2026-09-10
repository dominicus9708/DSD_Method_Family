# 05. DSD Synthesis / DSD 합성론

Status: **Protocol v0.1 established / proposed maturity / validation pending**

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

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)

Historical Step-1 draft and Step-2 pressure artifacts remain preserved:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)

Protocol v0.1 prospectively integrates the effective pre-protocol interface:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

The planning artifacts are not rewritten and do not count as direct Synthesis validation.

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

Sixteen boundary attacks were run before the executable protocol was frozen.

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
DIRECT_SYNTHESIS_PILOTS: 0
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

Protocol establishment does not establish correctness, superiority, external applicability, or maturity.

## Next development step

Create a separate precommit for the first direct positive Protocol-v0.1 challenge:

```text
SYN-CH-001
CASE_CLASS: positive
```

The case should include at least one admissible composition and one explicit interface/prerequisite rejection, with frozen composition law, target resolution, equivalence rule, candidate coverage, and three separate Synthesis ledgers.
