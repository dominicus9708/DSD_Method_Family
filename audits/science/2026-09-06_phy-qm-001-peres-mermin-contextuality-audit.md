# PHY-QM-001 — Peres-Mermin contextuality under the DSD describability interface

Date: 2026-09-06

## Interface lock

```text
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
FORMATION_LAYER: fixed background only
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: used only for information-loss analogy
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: standard two-qubit quantum observables / Peres-Mermin square
EXTERNAL_STANDARD: standard Kochen-Specker contextuality / compatible-observable product constraints
```

## Purpose

Audit whether the current DSD Property Axiom System merely renames quantum contextuality, whether it can faithfully represent the relevant context dependence, and which additional constraints are required before a Kochen-Specker contradiction can be obtained.

This record does **not** claim to derive quantum mechanics from DSD.
The Hilbert-space operators, spectra, compatibility relations, and operator-product identities are supplied by the external quantum specialization.

## Standard finite witness

Use the two-qubit Peres-Mermin square

```text
X⊗I    I⊗X    X⊗X
I⊗Y    Y⊗I    Y⊗Y
X⊗Y    Y⊗X    Z⊗Z
```

Each row and column is pairwise commuting.
The operator products are

```text
rows:    +I, +I, +I
columns: +I, +I, -I
```

Thus every context is locally compatible and admits ±1 outcome assignments satisfying its own product rule.

## DSD representation audit

### 1. Context should be a typed input, not merely a fixed prerequisite label

The current Property Axiom System allows finite typed input profiles and explicit contextual coordinates.
For this application, a clean specialization is

```text
Outcome(state, observable, context) -> {+1,-1}
```

with applicability restricted to `observable ∈ context` and to compatible measurement contexts.

Using only one fixed prerequisite set attached to the observable kind would be too weak or incorrectly typed for an observable that participates in multiple alternative contexts.
Therefore the measurement context should appear in the complete typed input (or an equivalent explicit application-level context carrier).

### 2. Local context-wise describability is nonempty

For one commuting triple with target product ±1, exactly four ±1 assignments satisfy the product constraint.
For six independently treated contexts there are

```text
4^6 = 4096
```

context-local assignment tuples before overlap consistency is imposed.

Hence the Kochen-Specker obstruction is **not** a failure of local assignment existence.

### 3. Noncontextuality is an additional cross-context gluing condition

If an observable O occurs in contexts C and C', noncontextuality requires

```text
v(O,C) = v(O,C').
```

This equality is not supplied by the generic DSD Property core merely because both records use the same observable label.
It is an application-specific cross-context identification rule.

### 4. Exhaustive global assignment result

Enumerating all

```text
2^9 = 512
```

context-independent ±1 assignments to the nine observables gives

```text
exact assignments satisfying all six product constraints: 0
maximum constraints simultaneously satisfied: 5 / 6
satisfaction-count distribution:
  1 satisfied: 96 assignments
  3 satisfied: 320 assignments
  5 satisfied: 96 assignments
```

The parity reason is exact: multiplying the three row constraints gives the product of all nine assigned values, while multiplying the three column constraints gives the same product with the opposite sign.

Therefore

```text
LOCAL_CONTEXT_ASSIGNMENT_SET != empty
GLOBAL_NONCONTEXTUAL_COMPLETION_SET = empty
```

is the correct structural statement.

## Contextuality score audit

Define the six signed context products so that the quantum operator identities correspond to +1 in every term.
For any context-independent assignment the sum obeys

```text
S_NC <= 4,
```

whereas the operator identities give

```text
S_QM = 6.
```

The difference is the standard Peres-Mermin contextuality gap, not a new DSD constant.
DSD can record it as a domain-specific compatibility/gluing failure diagnostic.

## Main verdicts

### Confirmed

1. The DSD Property core can represent context-indexed quantum outcome records without identifying context with observer identity.
2. `defined zero`, `undefined`, `inapplicable`, and `prerequisite-unsatisfied` remain separate from contextual incompatibility.
3. Local describability and global noncontextual completion are distinct mathematical questions.
4. A global noncontextual value assignment fails for the Peres-Mermin witness even though every compatible context is locally assignable.
5. DSD's generic contextual prerequisite machinery is **not itself** the Kochen-Specker theorem.

### Required external quantum bridges

- Hilbert-space representation
- Pauli observables and spectra
- compatible/jointly measurable context relation
- operator functional/product constraints
- noncontextual overlap-identification assumption when testing a noncontextual model

Without these bridges, the DSD core does not produce the quantum contradiction.

## Important correction to a tempting DSD reading

Do not state

```text
quantum contextuality = DSD prerequisite-unsatisfied state.
```

The Peres-Mermin witness instead shows an obstruction to **global gluing of locally valid context-indexed records under a noncontextual overlap constraint**.
Every individual context may be perfectly applicable and defined.

## Consequence for the current Property Axiom System

No core-paper modification is required merely to host context-indexed records.
However, a full structural treatment of contextuality would benefit from an optional downstream extension carrying

```text
CONTEXT_FAMILY
CONTEXT_OVERLAPS
LOCAL_ASSIGNMENT_SECTIONS
OVERLAP_COMPATIBILITY_RULE
GLOBAL_COMPLETION_TEST
```

or an equivalent gluing/sheaf-like specialization.
This is consistent with the Property paper's own scope boundary, which places sheaf-like locality outside the current finite core unless explicitly added.

## DSD Analysis/Audit status

```text
ANALYTICAL_GAIN:
  moderate — clean separation of local assignment, context typing, overlap gluing,
  and global completion, but no replacement of standard contextuality theory

AUDIT_VERDICT:
  PASS_WITH_BOUNDARY

NOVEL_PHYSICS_CLAIM:
  none

NEW_DSD_STRUCTURAL_RESULT:
  context-indexed local describability does not imply global noncontextual completable describability
```

## Reproducibility

Script:

```text
audits/science/2026-09-06_peres_mermin_dsd_contextuality.py
```

Run from repository root:

```bash
python audits/science/2026-09-06_peres_mermin_dsd_contextuality.py
```

Expected key output:

```text
row products: +1,+1,+1
column products: +1,+1,-1
exact_noncontextual_global_assignments=0
max_context_constraints_satisfied=5/6
noncontextual_score_max=4
quantum_operator_context_score=6
independent_context_local_products_before_overlap_gluing=4096
```

## Next audit target

1. Separate contextuality from entanglement using a state-independent Peres-Mermin witness.
2. Compare the DSD overlap/gluing formulation with the standard sheaf-theoretic contextuality formulation without importing that formalism into the Property core prematurely.
3. Then test Bell/CHSH, where locality and contextuality constraints enter differently.
