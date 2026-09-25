# DSD Lineage / DSD 계보론

Status: **Lineage Protocol v0.1 frozen / LIN-CH-001 64/64 PASS + LIN-CH-002 80/80 PASS / direct method-boundary challenge next**  
Legacy path ID: `09B`  
Higher field: **IV. Evidence & Lineage / 증거·계보**

## Internal-standardization files

- [`PLANNING.md`](PLANNING.md)
- [`WORKLOG.md`](WORKLOG.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- [`LIN-CH-001 precommit`](../../../evidence/method_specific/lineage/LIN-CH-001_precommit.md)
- [`LIN-CH-001 result`](../../../evidence/method_specific/lineage/LIN-CH-001_positive-constructed.md)
- [`LIN-CH-002 precommit`](../../../evidence/method_specific/lineage/LIN-CH-002_precommit.md)
- [`LIN-CH-002 result`](../../../evidence/method_specific/lineage/LIN-CH-002_negative-unresolved.md)

## Task

Determine and record predecessor/successor identity relations across dynamic or formation-level change when identity is not inherited automatically.

The method distinguishes channel-, component-, state-, and interval-level lineage claims.

It does not infer lineage from label continuity, temporal adjacency, Tracking continuity, numerical similarity, reduced aggregates, rank, entropy/stability diagnostics, Reconstruction candidates, or Transformation mappings alone.

## Primary DSD source

Current source anchor: **Structural Reorganization Dynamics**.

Source-derived core retained by this method:

```text
channel-lineage relation:
  Lambda_s_t subset C(s) x C(t)

coherent channel-lineage family:
  self-time relation = identity
  shorter-interval composition subset direct long-interval relation

canonical fixed-background channel lineage:
  identity relation on the fixed channel family inside one regular epoch

component-lineage relation:
  L_s_t subset Xcmp(s) x Xcmp(t)

coherent component lineage:
  self-time identity + composition inclusion
  + component-type preservation
  + inherited channel-lineage compatibility

state succession:
  supplied nonempty identity-bearing component families
  + predecessor-to-successor coverage
  + successor-to-predecessor coverage

branching / merging:
  allowed

unique successor / bijection / cardinality conservation:
  optional stronger application conditions

aggregate equality / aggregate inequality / rank / entropy diagnostic:
  not primary lineage criteria
```

## Method boundary

```text
Tracking:
  follows and records supported trace links.

Lineage:
  decides predecessor/successor identity across change.

Reconstruction:
  infers compatible missing/past structure or history.

Dynamics:
  supplies regular epochs, transition classes, and foundational lineage primitives.
  Lineage method execution evaluates a declared identity question;
  it does not derive a constitutive dynamic law.
```

Core guards:

```text
SUCCESSOR_RELATION != LITERAL_EQUALITY

SAME_LABEL != SAME_ENTITY
TEMPORAL_ADJACENCY != LINEAGE
TRACE_CONTINUITY != LINEAGE_IDENTITY

NUMERICAL_SIMILARITY != LINEAGE_IDENTITY
AGGREGATE_EQUALITY != LINEAGE_IDENTITY
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY
RANK_CHANGE != LINEAGE_COLLAPSE
SECONDARY_DIAGNOSTIC != PRIMARY_IDENTITY_CRITERION

FORMATION_TRANSITION != AUTOMATIC_SUCCESSION

BRANCHING != PROTOCOL_FAILURE
MERGING != PROTOCOL_FAILURE

TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
RECONSTRUCTED_LINEAGE_CANDIDATE != ESTABLISHED_LINEAGE
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
```

## Pre-protocol boundary attack

```text
TASK_INTERFACE_COMMIT:
  e233916530e8824427411d070ba0881160648618

BOUNDARY_ATTACK_COMMIT:
  3a8e860b7ea04eb321bb10c99922b224a58ff3dd

BOUNDARY_ATTACKS_RUN: 18

PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

The five required prospective refinements are limited to execution semantics:

```text
identity-bearing-family identity/version/provenance + selection rule
explicit lineage-family coherence status
NOT_ESTABLISHED vs BLOCKED exact boundary
required auxiliary-lineage absence rule
self-time/composition-coherence consequence and task-terminal precedence
```

No shared-core reopening is required.

## Current state

```text
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8

DEDICATED_LINEAGE_PROTOCOL: established v0.1
VALIDITY_GATES: G1-G16
BINDING_OPERATION: T1-T16

DIRECT_LINEAGE_PILOTS_ATTEMPTED: 2
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 2
POSITIVE_LINEAGE_CASES: 1
NEGATIVE_OR_UNRESOLVED_LINEAGE_CASES: 1
ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED: yes
BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

LINEAGE_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_LINEAGE_EVIDENCE_STATUS: validation_in_progress

SHARED_CORE_REOPEN_REQUIRED: no
```

## Boundary Amendment 001 and frozen protocol

```text
AMENDMENT_COMMIT:
  a448ac1ab49faddb97968ff5987d3c75ac77b6e0
AMENDMENT_BLOB:
  35568d0a27a8537347600efff87064b6b4ad177f

PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e
PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef

REFINEMENT_GROUPS_ADOPTED: 8/8
VALIDITY_GATES: G1-G16
BINDING_OPERATION: T1-T16
```

The amendment prospectively locks identity-bearing-family provenance, family-coherence status, NOT_ESTABLISHED versus BLOCKED semantics, required auxiliary-lineage handling, and task-terminal precedence.

Protocol v0.1 is now the frozen executable internal protocol for constructed validation.

## LIN-CH-001 — positive constructed challenge

```text
PRECOMMIT_COMMIT:
  0d797ac8321d2ed9b79e98d0890cc5bf721b25a4
PRECOMMIT_BLOB:
  f9f31a9c7cdb5692ba06e1d01750a02dc9984c3c

RESULT_COMMIT:
  0b455a95c46225182c4fa2627766334fd507480f
RESULT_BLOB:
  a53dedb60cee339d75d792ecccd72a5ff7e30d64

PRECOMMITTED_REQUIRED_CHECKS: 64
PASSED: 64
FAILED: 0

LINEAGE_TASK_TERMINAL_STATUS:
  LINEAGE_TASK_ESTABLISHED

LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT

LINEAGE_METHOD_GAIN_STATUS:
  LINEAGE_METHOD_GAIN_NOT_ASSESSED
```

The constructed fixture combined one fixed-background regular segment with one explicit formation-transition segment, preserved branching, satisfied channel/component coherence, passed bidirectional identity-bearing state coverage for all required ordered time pairs, and established interval Lineage identity without using Tracking continuity or reduced readouts as identity criteria.

## LIN-CH-002 — negative / unresolved-terminal challenge

```text
PRECOMMIT_COMMIT:
  169021711ea5069f1e63246efdd2ddfafbb3067a
PRECOMMIT_BLOB:
  d5537721f9dc55291f61569ad57eaa7e6b844a5b

RESULT_COMMIT:
  bce8356317ca8b1411eee7b518f1c993864b6fa6
RESULT_BLOB:
  3a40361b1c589e6a206bcbd4a6baa38054e6f075

PRECOMMITTED_REQUIRED_CHECKS: 80
PASSED: 80
FAILED: 0

ALL_NINE_LINEAGE_SUCCESSOR_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_LINEAGE_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
```

The challenge directly separated explicit negation, evaluable non-establishment, ambiguity, conflict, blockage, inapplicability, out-of-scope, underdetermination, partial completion, and evaluable family incoherence while preserving protocol conformance.

## Next

Prospectively precommit and execute the **direct neighboring-method boundary challenge** under fair shared-artifact access.

External validation remains deferred.
