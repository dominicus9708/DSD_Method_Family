# DSD-AUDIT-20260908-MATH-026 — Collatz right-offset rolling bootstrap through 2e8

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE ONLY / ROLLING-OPERATOR ACCELERATED`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the exact MATH-025 rolling 11-step operator be used as the actual continuation engine to extend the finite MATH-024 right-offset exclusion from `10^8` to `2*10^8` without changing the logical scope of the result?

## DSD tuple

### D — Definition

The audited starts are

\[
N=b2^{61}+r,
\qquad1025\le b\le1363,
\qquad0\le r\le2\cdot10^8.
\]

The retained predicate is coefficient survival along the universal-spine candidate prefix.

The downstream claim concerns only internal adjacent-block candidates meeting at the same endpoint.

### R — Resolution

Every integer right offset in the finite domain is considered.

Stage 1 uses exact scalar shortcut evolution through depth 61.

Stage 2 retains the exact lifted endpoint and advances it in exact 11-step windows selected by `n mod 2048`.

The rolling continuation is audited through depth 1029.

### S — Selection

There is no sampling.

Stage-1 exhaustive result:

\[
\boxed{358,907}
\]

depth-61 surviving offsets.

First and last:

\[
703,\qquad199,999,983.
\]

For each survivor all 339 internal right-side address labels are continued.

### E — Exclusion

The MATH-025 local window gate is

\[
q\ge H_K(n\bmod2048).
\]

Failure of this gate means at least one coefficient threshold in that 11-step window fails.

Across the full finite MATH-026 state set, no state survives all rolling windows through depth 1029.

The deepest failing window begins at depth

\[
\boxed{501},
\]

so the longest finite states fail somewhere in depths `502..512`.

### T — Transition

For a surviving 11-step window, the exact propagated state is

\[
q'=q+s(u),
\qquad
n'=\frac{3^{s(u)}n+c(u)}{2^{11}},
\qquad u=n\bmod2048.
\]

The exact endpoint, not merely the residue, is propagated to the next window.

All finite arithmetic in this audit remains within an explicitly guarded unsigned-128-bit range.

### C — Consistency

MATH-021 requires any same-endpoint cross-boundary collision at depth `k` to use a right offset satisfying

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Hence the finite domain `r<=2*10^8` contains every possible right offset relevant through

\[
3(2\cdot10^8)+3=600,000,003.
\]

Every audited right-side candidate dies before even the earliest possible halo-entry depth `3*703+1=2110`.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

The exact consequence is

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le600,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

This is not a Collatz verification bound for all starts.

### O — Outcome

Established:

- finite right-offset domain doubled from `10^8` to `2*10^8`;
- 358,907 exact depth-61 survivors;
- MATH-025 rolling operator successfully used as the continuation engine;
- zero states survive the rolling continuation through depth 1029;
- internal adjacent-block same-endpoint coupling exclusion extended to depth `600,000,003`.

Still open:

- candidate mechanisms not requiring such endpoint coupling;
- offsets above `2*10^8`;
- avoiding exhaustive stage-1 right-offset scanning;
- first-cell emptiness;
- Collatz.

## AP-2 / transition audit

The rolling implementation never treats equal 11-bit residues as equal dynamical states. The residue selects a local transition rule; the propagated endpoint remains exact.

Thus the computation does not introduce a coarse finite-state aliasing assumption.

## Prohibited upgrades

Do not infer:

- finite `r<=2e8` ⇒ all offsets;
- no internal endpoint coupling ⇒ no first-cell candidate;
- rolling-window coefficient failure ⇒ ordinary Collatz start impossible;
- depth `600,000,003` ⇒ a general exhaustive Collatz verification limit;
- computational acceleration ⇒ stronger universal theorem.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_right_offset_rolling_bootstrap_200m_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-right-offset-rolling-bootstrap-200m.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-026`
