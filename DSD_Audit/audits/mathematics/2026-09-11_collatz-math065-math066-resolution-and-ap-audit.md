# DSD Audit — Collatz MATH-065 / MATH-066 resolution and arithmetic-progression split

Date: 2026-09-11

Status: `SAFE PARTIAL REDUCTION / CLAIM-LAYER SEPARATION LOCKED / COLLATZ OPEN`

## 1. Audit object

This audit covers the transition from MATH-064 through the repaired MATH-065 certificate and the MATH-066 `r=17` arithmetic-progression continuation.

Canonical mathematical repository:

- `dominicus9708/Math-verification`
- `collatz/notes/2026-09-11-math065-paid-count-18plus-closure.md`
- `collatz/notes/2026-09-11-math066-r17-ap-descent.md`

The domain norm remains ordinary mathematical proof validity.  DSD Audit is used only to expose state selection, lineage retention, resolution changes, and invalid claim upgrades.

## 2. Four claims that must remain distinct

The recent calculations require four logically different statements.

### A. Resolution collapse

A parity/dyadic cylinder may contain at most one ordinary source.

This means only

> the symbolic multiplicity has collapsed to one.

It does **not** imply the corresponding ordinary integer descends.

### B. Singleton closure

The unique ordinary source/target is explicitly continued and reaches the frozen verified floor `2^71`.

Only then may that singleton branch be called closed for the current minimal-counterexample calculation.

### C. Arithmetic-progression family closure

A finite target family

\[
P(a,b,m)=\{a+bk:0\le k<m\}
\]

is propagated exactly under the shortcut map by splitting `k` parity.  If every child family is eventually trimmed at or below `2^71`, the entire family is closed without materializing all members.

This is stronger than a count/density statement but still only a finite family certificate.

### D. Paid-count layer closure

An entire paid-count layer `r` is closed only if every negative-adjusted-cost completed cylinder in that layer is covered by B or C, or is excluded earlier by an exact safe lower-bound prune.

No subset count can be promoted to D.

## 3. MATH-064 correction

The original MATH-064 treatment correctly removed singleton-only cells from the multi-source symbolic graph, but incorrectly treated that as enough for complete layer closure.

The invalid implication was

\[
\boxed{
\text{singleton resolution}
\not\Rightarrow
\text{ordinary-integer closure}.
}
\]

MATH-065 repairs this by carrying singleton branches through exact ordinary continuation.

This correction is considered structurally important and should remain visible in all later summaries.

## 4. MATH-065 audit

MATH-065 retains, at each parity step,

\[
t\equiv\tau\pmod{2^h}
\]

for the original source lift and an affine endpoint family

\[
Y_h=A_h+3^{q_h}s.
\]

Thus same-integer lineage is preserved.

The future-cost prune uses only a lower bound on the remaining penalty.  Therefore pruning a branch because that lower bound already exceeds the `19/503` target is safe.

For `18<=r<=26`, every remaining negative-candidate ordinary target is explicitly continued to `<=2^71`.

For `27<=r<=64`, no completed negative-candidate cylinder remains after exact branch-and-bound.

For `r>=65`, MATH-062 supplies the independent analytic phase-sum closure.

Hence the current claim

\[
\boxed{r\ge18\text{ closed for the first-cell paid-cluster calculation}}
\]

is supported.

This does not close `r<=17`, one-paid branches, the first universal cell, later Farey cells, or Collatz.

## 5. MATH-066 exact AP state

At `r=17`, materializing all surviving cylinders would produce `38,457,239` ordinary target occurrences.

MATH-066 instead retains a completed target cylinder as

\[
P(a,b,m),\qquad b\text{ odd}.
\]

For

\[
k=\rho+2s,
\qquad \rho\in\{0,1\},
\]

one shortcut step gives exactly

\[
P\left(\frac{a+b\rho}{2},b,m'\right)
\]

on an even branch, or

\[
P\left(\frac{3(a+b\rho)+1}{2},3b,m'\right)
\]

on an odd branch.

Therefore the AP representation is closed under exact shortcut propagation.

No independence, randomness, density, or average-drift assumption is introduced.

## 6. MATH-066 supported claims

At `r=17`, the exact phase/address split is

\[
1090=256+596+238.
\]

The exact branch-and-bound leaves

\[
1,728,083
\]

negative-candidate cylinders with total target multiplicity

\[
38,457,239.
\]

The following subfamilies are closed:

1. all `1,013,728` multiplicity-one cylinders, by direct memoized ordinary descent;
2. all `4,086` cylinders with multiplicity at least `1024`, representing `17,143,582` target occurrences, by exact AP propagation.

Thus

\[
18,157,310
\]

target occurrences are covered by explicit closure certificates.

The unresolved part is

\[
710,269
\]

cylinders with multiplicity

\[
2\le m\le1023,
\]

representing

\[
20,299,929
\]

target occurrences.

Therefore

\[
\boxed{r=17\text{ remains OPEN}.}
\]

## 7. DSD information-loss audit

### Preserved information

- exact source dyadic lineage;
- exact endpoint affine lineage;
- exact phase cell;
- exact paid-count layer;
- exact finite multiplicity;
- exact ordinary targets when a singleton is materialized;
- exact AP membership when a family is propagated.

### Intentionally discarded information

Within an AP family, individual target identities are not separately stored while the family remains closed under the same affine/parity transformation.

This discard is safe because the set transformation is exact and invertible at the parameter-partition level.

### Forbidden discard

A singleton may not be discarded merely because symbolic multiplicity is one.

An AP family may not be discarded merely because its cardinality is small, large, sparse, or statistically favorable.

## 8. Claim-lock table

| Statement | Status |
|---|---|
| `r>=18` paid-count layers closed | SAFE in current first-cell calculation |
| `r=17` singleton track closed | SAFE |
| `r=17`, multiplicity `>=1024` AP track closed | SAFE |
| all `r=17` closed | OPEN / PROHIBITED UPGRADE |
| all multi-paid branches closed | OPEN |
| first universal Farey cell closed | OPEN |
| Collatz conjecture proved | OPEN |

## 9. Next audit target

The next mathematical optimization should operate only on the unresolved `r=17` range

\[
2\le m\le1023.
\]

The preferred DSD state should retain

\[
(\text{source congruence},\ \text{phase cell},\ a,b,m,\ \text{reduced-cost bound})
\]

and merge states only when all future-relevant coordinates are identical or when an exact dominance relation is proved.

Do not lower the multiplicity threshold blindly: MATH-066 already observed that some medium-sized AP families generate larger parity trees than some very large families.
