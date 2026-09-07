# DSD-AUDIT-20260908-MATH-031 — Collatz 22-step cyclic-window address prefilter

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT FINITE PREFILTER / COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the 339 internal right-side address labels of every MATH-028 depth-61 right-offset survivor be filtered through the next 22 coefficient-survival steps by an exact complete descriptor and cyclic-window transform before exact endpoint continuation is instantiated?

## DSD tuple

### D — Definition

For a depth-61 exact endpoint `n` with current odd-count `q`, define the 22-step residue

\[
u=n\bmod2^{22}.
\]

The local descriptor stores:

- `H22(u)` — minimum current `q` required for all next 22 coefficient gates;
- `s22(u)` — added odd-count;
- `c22(u)` — exact affine correction.

### R — Resolution

The descriptor is exhaustively constructed on all

\[
2^{22}=4,194,304
\]

residues.

For every residue, the certificate checks exact equality with the composition of two previously audited 11-step blocks in three quantities:

1. survival threshold;
2. total added odd-count;
3. affine correction.

The full exact ordinary endpoint is retained for any state that survives and must be propagated beyond the local window.

### S — Selection

At depth 61, for fixed lower state `(q,y)`, internal right-side address endpoints are

\[
n_b=y+b3^q,
\qquad1025\le b\le1363.
\]

Since `3^q` is invertible modulo `2^22`, with

\[
z=(3^q)^{-1}y\pmod{2^{22}},
\]

these 339 address residues become one contiguous cyclic window in transformed coordinates.

The local survival indicator is therefore aggregated by an exact range query rather than 339 separate threshold evaluations.

### E — Exclusion

On the exact MATH-028 `RMAX=10^9` depth-61 survivor set:

\[
1,796,718\cdot339
=609,087,402
\]

raw internal address states exist before the 22-step local gate.

Exactly

\[
\boxed{189,767,400}
\]

survive all coefficient gates through depth 83.

Therefore states failing the local 22-step predicate are safely excluded from deeper continuation in this finite computation.

### T — Transition

For every surviving local state,

\[
q'=q+s_{22}(u),
\]

and

\[
T^{22}(n)=\frac{3^{s_{22}(u)}n+c_{22}(u)}{2^{22}}.
\]

Thus the residue selects an exact transition while the exact endpoint remains the propagated state.

### C — Consistency

The raw-to-surviving address-state ratio is

\[
\frac{609,087,402}{189,767,400}
\approx3.20965.
\]

This is a finite address-instantiation reduction, not a mathematical density statement.

The effect is strongest at low `q61`, consistent with MATH-006/011. For example, `q61=39` leaves average only about `14.93` of the 339 internal labels surviving to depth 83, while high-q leaves approach all 339 labels.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / COMPUTATIONAL ACCELERATION / FINITE ONLY`.

No new universal endpoint-coupling theorem follows solely from the 22-step prefilter.

### O — Outcome

Established:

- exact 22-step complete local descriptor on all `2^22` residues;
- exact composition with two audited 11-step operators;
- exact cyclic-window address aggregation;
- finite address states reduced from `609,087,402` to `189,767,400` before deeper continuation.

Still open:

- deeper continuation of the surviving depth-83 address states;
- best block length for larger finite domains;
- right offsets above `10^9`;
- first-cell emptiness;
- Collatz.

## AP-2 / representation check

The residue `u mod 2^22` is used only for a local exact predicate and affine transition. It is not treated as a complete global Collatz state.

Therefore no coarse residue alias is promoted to a universal state equivalence.

## Prohibited upgrades

Do not infer:

- `3.20965x` finite reduction ⇒ universal density reduction;
- failure by depth 83 ⇒ arbitrary Collatz convergence;
- local descriptor completeness ⇒ arbitrary-depth completeness;
- address prefilter ⇒ first-cell emptiness;
- computational acceleration ⇒ proof completion.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_tail22_cyclic_window_prefilter_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-tail22-cyclic-window-prefilter.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-031`
