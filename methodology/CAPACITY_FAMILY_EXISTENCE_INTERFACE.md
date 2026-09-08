# Capacity-Family Existence Interface

Status: **methodology / reusable reconstruction interface**  
Origin: QM Core 004J.  
Scope: any operational reconstruction program that needs systems of every finite capacity.

## 1. Capacity is an operational invariant

Use the declared operational capacity

\[
\operatorname{Cap}(S)
=
\sup\{n:\text{one admitted measurement perfectly distinguishes }n\text{ admitted states}\}.
\]

Do not identify this number with:

```text
DSD channel count
property arity
real vector-space dimension
Hilbert dimension
axis/rank count
number of readout coordinates
```

Any equality with one of those quantities requires a separate typed theorem.

## 2. Family-existence target

```text
CFE  Capacity-Family Existence
```

For every positive integer `N`, there exists an admitted dynamical system of operational capacity exactly `N`.

This is an existence statement about a whole system family. It is stronger than the existence of one high-capacity system and stronger than the existence of arbitrarily large capacities without a descent principle.

## 3. Two independent precursor directions

### 3.1 Upward / unbounded source

```text
IFPC  Iterated Finite Product Composition
```

A nontrivial seed `S` with `Cap(S)=q>=2` admits an independent `k`-fold composite for every finite `k`, and product preparations/measurements remain available.

Then

\[
\operatorname{Cap}(S^{\boxtimes k})\ge q^k.
\]

Thus realized capacities are unbounded.

Exact capacity multiplicativity is unnecessary for this conclusion.

### 3.2 Downward / predecessor closure

```text
IDDC  Intrinsic Descriptive Descent Closure
```

Every admitted finite-capacity system of capacity `m>=2` has an admitted restriction whose retained state/effect/dynamics data form a valid dynamical system of capacity exactly `m-1`.

This formulation is intentionally intrinsic. It does not presuppose a separately existing object already named `Q_{m-1}` and therefore avoids circularity when proving family existence.

## 4. Completion theorem

Let `R` be the set of realized positive-integer capacities.

If:

```text
1. R contains some q >= 2,
2. IFPC makes R unbounded,
3. IDDC makes R predecessor-closed,
```

then

\[
R=\mathbb N_{>0}.
\]

Proof: for any target `N`, choose realized `M>=N`; apply the predecessor rule repeatedly until `N` is reached.

## 5. Non-implication controls

```text
unbounded capacities alone      != all finite capacities
predecessor closure alone       != unbounded capacities
finite channel availability     != operational-capacity family existence
```

Examples:

```text
{1,2,4,8,...}  is unbounded but has holes.
{1,2,3,4}      is predecessor-closed but bounded.
```

## 6. Relation to recursive-restriction interfaces

A family-indexed statement of the form

```text
restricted N-system is equivalent to Q_(N-1)
```

already presupposes that `Q_(N-1)` exists.

When family existence itself is under audit, first use the intrinsic `IDDC` form. After family representatives have been constructed, a stronger recursive-equivalence interface may identify each intrinsic descendant with the selected lower-capacity representative.

## 7. Provenance discipline

When this interface is first isolated inside a target-theory reconstruction, keep target-specific precursor assumptions conservative:

```text
PRE_EXISTING_DSD / GENERAL_OPERATIONAL_DERIVATION
TARGET_SPECIALIZATION_SELECTOR
EXACT_COMPARATOR_LOCK
```

Do not retroactively label a target-discovered composition or descent assumption as generic merely because its wording is general.

## 8. Claim discipline

A valid claim is:

> Under explicit nontrivial-seed, iterated independent-composition, and intrinsic predecessor-descent assumptions, existence of a system of every finite operational capacity follows.

Do not claim:

> Generic DSD contains a system of every quantum dimension.

The latter additionally conflates operational capacity with Hilbert dimension and removes the provenance boundary.
