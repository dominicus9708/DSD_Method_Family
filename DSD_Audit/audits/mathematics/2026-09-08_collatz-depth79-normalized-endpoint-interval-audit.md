# DSD-AUDIT-20260908-MATH-019 — Collatz depth-79 normalized endpoint interval audit

## Verdict

`CONFIRMED / FINITE EXACT / INTERNAL-BOUNDARY COLLISION EXCLUSION THROUGH DEPTH 79`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited result

For the complete depth-79 internal-boundary halo

\[
D_{79}=2^{29}-1,
\]

all 339 internal boundaries were audited using the MATH-017 lift-bit generator and MATH-018 tail descriptor.

The final odd-count support gate is not sufficient: every boundary retains common final `Q` values on both sides.

However, after defining

\[
Z=2^{18}E-a3^Q
\]

for block label `a` and depth-79 endpoint `E`, every common `(boundary,Q)` cell satisfies strict normalized endpoint separation.

For adjacent labels `a` and `a+1`, endpoint equality with common `Q` is equivalent to

\[
Z_L-Z_R=3^Q.
\]

Across all 5,100 common cells the exact audit gives

\[
Z_L^{\max}<Z_R^{\min}+3^Q.
\]

Hence

\[
\max E_L<\min E_R
\]

for every same-`Q` cell, and there is no internal cross-boundary endpoint collision at depth 79.

## DSD tuple

### D — Describability

The endpoint comparison is decomposed into:

1. boundary label;
2. final odd-count `Q`;
3. normalized endpoint numerator `Z`.

This removes the large affine address term without discarding the exact tail residue dependence.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### R — Resolution

The complete displacement halo is used:

\[
D_{79}=2^{79-q_{\min}(79)}-1=2^{29}-1.
\]

The local range endpoints are handled exactly:

- left offsets: `1..D79`;
- right offsets: `0..D79-1`.

The right endpoint `D79` is excluded because every legal cross-boundary pair has left offset at least 1 and total displacement at most `D79`.

Outcome: `ESTABLISHED_WITHIN_SCOPE`.

### S — Selection

The MATH-018 `G18` descriptor applies every intermediate coefficient-survival condition through depth 79 before a state enters the endpoint interval comparison.

Generated local state counts:

\[
963,422\text{ left},
\qquad
964,227\text{ right}.
\]

Outcome: `CONFIRMED`.

### E — Exclusion

First gate: final `Q` support.

No boundary is excluded here.  The common-Q-count distribution is:

```text
14 common Q -> 43 boundaries
15 common Q -> 240 boundaries
16 common Q -> 54 boundaries
17 common Q -> 2 boundaries
```

Thus the `Q`-support route is classified as `SATURATED` for depth 79.

Second gate: normalized endpoint interval.

All 5,100 common `(boundary,Q)` cells are excluded from equality by strict interval order.

Outcome: `CONFIRMED`.

### T — Transition

For tail length `L=18`, block label `a`, lower state `(q,y)`, and final total odd-count `Q=q+s`, the exact shortcut affine formula gives

\[
2^{18}E=3^s(y+a3^q)+C_{18}.
\]

Therefore

\[
Z=2^{18}E-a3^Q=3^s y+C_{18}.
\]

For adjacent labels `a` and `a+1`, common-`Q` endpoint equality is equivalent to

\[
Z_L=Z_R+3^Q.
\]

No probabilistic or average transition is used.

Outcome: `CONFIRMED`.

### C — Consistency

The exact minimum numerator separation is

\[
219,414,528=837\cdot2^{18}.
\]

A direct ordinary-integer witness attaining the minimum same-Q endpoint gap is

\[
N_L=1241\cdot2^{61}-5,
\]

\[
N_R=1241\cdot2^{61}+703,
\]

with

\[
Q_L=Q_R=50
\]

and

\[
T^{79}(N_R)-T^{79}(N_L)=837.
\]

Outcome: `CONFIRMED`.

### N — Norm

Classification:

`FINITE EXACT`.

The strict order at depth 79 is not promoted to arbitrary-depth monotonicity.

### O — Outcome

Combined with MATH-017:

\[
\boxed{\text{no internal adjacent-block endpoint merger through depth }79.}
\]

The DSD cause classification is:

- odd-count support mismatch: not the cause;
- normalized endpoint one-sided separation: the active exclusion mechanism at depth 79.

The next structural target is to test whether this ordered separation persists at depths 80 and 81, where the same `m=29` local halo can be reused.  Repeated persistence should trigger an attempt at a recursive inequality rather than indefinite depth extension.

## Prohibited upgrades

Do not infer:

- finite depth-79 separation => arbitrary-depth separation;
- candidate-set endpoint order => global monotonicity of the Collatz map;
- internal-boundary exclusion => outer-window competitor exclusion;
- depth-79 exclusion => first-cell closure.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_depth79_normalized_endpoint_interval_certificate.cpp`

Commit:

`ef9eae15695e0fcb8f8a9c747485f2b3c3800d8a`

Explanatory note:

`collatz/notes/2026-09-08-depth79-normalized-endpoint-interval-separation.md`

Note commit:

`87a53b05e890f4e8b50395259dfba73434a8b41a`
