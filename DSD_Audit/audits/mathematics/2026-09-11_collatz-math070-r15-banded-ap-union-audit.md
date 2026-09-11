# DSD Audit — Collatz MATH-070 r=15 banded AP-union closure

Date: 2026-09-11
Status: `SAFE WITH EXPLICIT SCOPE / r=15 CLOSED / FIRST CELL OPEN`

## Audited claim

MATH-070 claims closure of the `r=15` multi-paid layer for the current first-universal-cell minimal-counterexample calculation.

The source workload is the exact MATH-065 dyadic branch-and-bound output:

- 35,343,449 branch nodes;
- 2,928,669 negative-candidate completed AP cylinders;
- 1,835,780,279 ordinary target occurrences with multiplicity;
- maximum initial cylinder multiplicity 14,315,470.

The target floor remains `2^71`.

## Representation distinction

The key DSD distinction in MATH-070 is between

1. a mathematical ordinary-target set;
2. an AP representation of that set;
3. a multiplicity band used only to organize those AP representations.

The initial multiplicity bands are **not** asserted to be disjoint ordinary-integer sets. The same integer may occur in more than one band through different historical AP representations.

This does not invalidate the certificate because every band is closed independently. Duplicate work can enlarge computation but cannot delete an unresolved target.

## Exact transition audit

For one AP

`P(a,b,m)={a+b k:0<=k<m}`

with odd `b`, parameter parity fixes ordinary-value parity. The shortcut map therefore sends the two parameter-parity subfamilies to exact AP children.

The engine performs only:

- exact initial-segment trimming for values already `<=2^71`;
- exact parity splitting;
- exact integer affine Collatz image;
- exact interval union on identical `(b,a mod b)` grids;
- exact singleton deduplication by ordinary integer value.

No density, parity independence, expected drift, or probabilistic filter appears.

## Band completeness audit

The 33 bands are contiguous and disjoint as representation classes from `m=1` through `m=2^24-1=16,777,215`, strictly covering the observed maximum `14,315,470`.

Summing the raw input over the bands reproduces exactly:

- 2,928,669 cylinders;
- 1,835,780,279 target occurrences.

Two listed bands contain zero source cylinders; retaining them is useful because it makes absence of hidden multiplicity gaps explicit.

Every nonempty band reaches the frozen floor under exact AP-union propagation. The largest certified sweep bound is 443.

## Claim hierarchy

### SAFE

- `r=15` is closed for the current first-cell minimal-counterexample calculation.
- Combined with earlier certificates, every `r>=15` multi-paid layer is closed.
- The remaining detailed multi-paid frontier is `2<=r<=14`.

### OPEN

- `2<=r<=14` multi-paid layers;
- mixed one-paid / remaining multi-paid Bellman closure;
- genuinely aperiodic low-cost branch;
- first universal Farey cell emptiness;
- later cells;
- full Collatz.

### PROHIBITED UPGRADES

- bandwise closure => multiplicity bands are dynamically independent;
- `r>=15` closure => all multi-paid paths are closed;
- finite AP-union descent => universal Collatz descent theorem;
- paid-count progress => first-cell proof completed.

## DSD methodological result

MATH-070 demonstrates a useful representation-control rule:

> When a mathematically exact state union becomes computationally expensive because heterogeneous representation scales interact, partition the **representations** by a future-complete invariant or bookkeeping parameter, prove each part independently, and recombine only at the level of the final claim.

Here initial AP multiplicity is used only as such a bookkeeping partition. It is not promoted to a mathematical property of Collatz dynamics.

## Canonical sources

- `collatz/src/2026_09_11_math070_r15_leaf_export.py`
- `collatz/src/2026_09_11_math070_r15_banded_ap_union_engine.cpp`
- `collatz/notes/2026-09-11-math070-r15-banded-ap-union-closure.md`
