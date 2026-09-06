# PHY-QM-002 — State-independent contextuality versus entanglement

Date: 2026-09-06

## Purpose

Separate two quantum structures that a DSD analysis could otherwise conflate:

1. **contextuality** — obstruction to one context-independent global value assignment compatible with all declared measurement contexts;
2. **entanglement** — non-factorization / non-separability of a state relative to a supplied subsystem tensor-product decomposition.

The analysis uses the same standard two-qubit Peres-Mermin operator specialization as PHY-QM-001.

## Exact state-independence

The six compatible context products in the Peres-Mermin square are operator identities

```text
R1 = +I
R2 = +I
R3 = +I
C1 = +I
C2 = +I
C3 = -I
```

For every normalized density operator rho,

```text
Tr(rho I) = 1,
Tr(rho (-I)) = -1.
```

Therefore the signed Peres-Mermin context score is

```text
S_QM(rho) = 6
```

for every rho in the two-qubit state space. No special entangled state is required for the operator contradiction.

## Explicit separable controls

### Product pure state

```text
rho_00 = |00><00| = |0><0| ⊗ |0><0|.
```

This is separable, but the six context-product identities still yield the same state-independent score 6.

### Maximally mixed state

```text
rho_mix = I_4 / 4.
```

This is separable and again yields the same six context-product values because the context products are ±I.

Hence, for this witness,

```text
CONTEXTUALITY_WITNESS_PRESENT
ENTANGLEMENT_REQUIRED = false
```

## DSD structural separation

A clean DSD specialization should use different diagnostics.

### Contextuality sector

```text
CONTEXT_FAMILY
LOCAL_ASSIGNMENTS
OVERLAP_IDENTIFICATION_RULE
GLOBAL_COMPLETION_SET
NONCONTEXTUAL_SCORE
```

The Peres-Mermin witness has nonempty local assignment sets but empty exact global noncontextual completion.

### Entanglement sector

Requires an externally supplied subsystem decomposition

```text
H = H_A ⊗ H_B
```

and a separate factorization/separability diagnostic.
For a pure state, product-factorization or Schmidt rank may be used; for mixed states, separability is a convex-decomposition question.

Neither diagnostic is inferred from the other merely because both involve multi-component quantum systems.

## Main verdicts

- `contextuality = entanglement`: **rejected**.
- `two-qubit observable acts on both subsystems -> state is entangled`: **rejected**.
- contextuality should be represented as context-overlap/global-completion structure: **confirmed for this specialization**.
- entanglement should be represented as state factorization/separability relative to an explicit tensor-product bridge: **confirmed as a distinct analysis sector**.
- DSD multi-input property support alone proves entanglement: **rejected**.

## DSD consequence

The Property core's ability to retain complete multi-input records is useful bookkeeping, but it does not turn a relational property into quantum entanglement by name. Likewise, contextual prerequisites do not become Kochen-Specker contextuality by name.

The two downstream bridges should remain independent:

```text
DSD typed records + quantum measurement-context bridge
    -> contextuality/gluing audit

DSD typed records + Hilbert tensor-product state bridge
    -> entanglement/factorization audit
```

## Audit status

```text
AUDIT_VERDICT: PASS_WITH_SEPARATION
NEW_PHYSICS_CLAIM: none
STRUCTURAL_RESULT: contextual gluing obstruction and subsystem factorization obstruction are inequivalent DSD analysis targets
```

## Next target

Bell/CHSH: distinguish

```text
contextuality
locality / parameter dependence
outcome assignment
state entanglement
causal support
```

under one finite witness and determine which DSD bridges are genuinely independent.
