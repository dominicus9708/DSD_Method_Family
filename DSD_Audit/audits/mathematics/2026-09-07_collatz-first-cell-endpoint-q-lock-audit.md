# DSD-AUDIT-20260907-MATH-004 — Collatz first-cell endpoint q-lock

Date: 2026-09-07
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Outcome

**Verdict: CONFIRMED within the current first-universal-cell candidate window through depth 195.**

The audit confirms an endpoint q-lock and an address-faithful equivalence with the already-established root full-Hensel maximality mechanism. It does **not** count endpoint quotienting as an independent second exclusion mechanism.

## Scope lock

Current start window:

\[
2^{71}<N<\frac{1364}{1024}2^{71}.
\]

Prefix scope:

\[
k\le195.
\]

Coefficient-surviving normalized correction:

\[
S=R/3^q.
\]

The companion exact certificate verifies

\[
S<2^{71}
\]

for all coefficient-surviving prefixes in the locked depth range.

## Claim under audit

For two candidate-window starts whose length-`k` prefixes reach the same endpoint,

\[
T^k(N_1)=T^k(N_2),
\]

show that

1. their odd counts are equal;
2. smaller start is equivalent to larger correction;
3. the endpoint fiber coincides with a translated full-Hensel correction class;
4. only the smallest start / maximum-correction representative needs to be retained for a minimal-counterexample search.

## Eight-axis audit

### D — Describability

PASS.

Objects are explicit: ordinary start `N`, prefix depth `k`, odd count `q`, correction `R`, normalized correction `S`, and exact endpoint.

### R — Resolution

PASS.

The proof keeps ordinary integer starts and exact endpoints. It does not replace them by density, residue frequency, or an averaged state.

### S — Selection

PASS WITH SCOPE.

The start interval and depth are inherited from independently certified first-cell reductions. The theorem is not asserted outside them.

### E — Exclusion

PASS.

If `q_1>q_2`, equal endpoints imply

\[
N_2+S_2=3^{q_1-q_2}(N_1+S_1)>3B_0,
\]

while

\[
N_2+S_2<C_*+B_0<3B_0.
\]

Thus unequal odd counts are excluded exactly.

### T — Transition / lineage

PASS.

The merge is an exact equality of the two ordinary trajectories at depth `k`. No arbitrary later-block pullback is used.

### C — Consistency

PASS.

With `q_1=q_2=q`, endpoint equality gives

\[
R_1-R_2=3^q(N_2-N_1),
\]

which is exactly the full-Hensel correction congruence plus ordinary-start displacement.

### N — Norm

PASS.

The standard minimal-positive-counterexample norm is used. A larger start that merges with a smaller positive start cannot be minimal.

### O — Outcome

CONFIRMED WITH NON-INDEPENDENCE NOTE.

The quotient is legal and address-faithful, but in the q-locked range it is the same underlying root-minimality mechanism as full-Hensel maximality. Treating both as independent filters is prohibited double counting.

## Required prohibited upgrades

- `endpoint quotient` and `root-Hensel maximality` must not be multiplied as independent exclusion rates.
- q-lock must not be extended past the proved correction-envelope range without a new inequality.
- same endpoint at one depth must not be conflated with equality of earlier histories.
- this theorem does not close the first universal cell or Collatz.

## Evidence

Primary exact certificate commit:

`e4e921f9b19aeacc85d96c37731e0867c52fea98`

Primary explanatory note commit:

`f63e98711689d839ab9d36aa0a58e9c999382d31`

## Next audited transition

Investigate unequal-q endpoint collisions beyond the all-q locked depth. The safe question is whether the correction envelope forces the higher-q member to have the smaller ordinary start, allowing exact endpoint dominance without transferring arbitrary later-block Hensel maximality.