# DSD-AUDIT-20260908-MATH-028 — Collatz combined lifting + rolling bootstrap through 1e9

Date: 2026-09-08

Verdict:

`CONFIRMED / FINITE ONLY / COMBINED EXACT ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the exact MATH-027 bounded prefix generator and the exact MATH-025 rolling continuation be composed without loss of ordinary-integer lineage, and can that composition extend the finite internal endpoint-coupling exclusion to the right-offset domain `0<=r<=10^9`?

## DSD tuple

### D — Definition

The finite starts are

\[
N=b2^{61}+r,
\qquad1025\le b\le1363,
\qquad0\le r\le10^9.
\]

The candidate predicate is prefixwise coefficient survival in the current universal-spine route.

The conclusion concerns only internal adjacent-block candidates meeting at the same endpoint.

### R — Resolution

Three exact resolution stages are preserved:

1. binary-prefix state `(r,T^k(r),q_k)` through depth 61;
2. exact address-lifted endpoint at depth 61;
3. exact endpoint plus residue-selected 11-step transition thereafter.

No stage replaces the exact endpoint with a residue-only propagated state.

### S — Selection

MATH-027 bounded residue lifting exhausts all coefficient-surviving right offsets in the stated finite domain.

Result:

\[
\boxed{1,796,718}
\]

depth-61 survivors.

First and last:

\[
703,\qquad999,999,207.
\]

The generator performs `187,063,991` exact lift-branch attempts and reaches a peak of `11,894,128` live states at depth 30.

### E — Exclusion

For every depth-61 survivor, all 339 internal right-side labels are continued by the exact MATH-025 rolling gate.

No state survives every 11-step window through depth 1029.

The deepest failing-window base is

\[
\boxed{545},
\]

with first witness

\[
\boxed{r=378,620,799,\qquad b=1183}.
\]

Hence that longest audited state still fails coefficient survival inside depths `546..556`.

### T — Transition

The combined transition chain is

\[
T^k(x+e2^k)=T^k(x)+e3^{q_k}
\]

for bounded binary lifting,

then

\[
T^{61}(b2^{61}+r)=T^{61}(r)+b3^{q_{61}},
\]

then, window by window,

\[
q'=q+s(u),
\qquad
n'=\frac{3^{s(u)}n+c(u)}{2^{11}}.
\]

Every transition preserves the exact ordinary endpoint required by the next stage.

### C — Consistency

The final certificate constructs the threshold sequence with arbitrary-precision integers and verifies the frozen theorem-facing coefficient floor throughout the used depth range.

An exploratory fixed-width threshold computation was detected as unsafe and discarded before this audit. It contributes no evidence to the verdict.

MATH-021 supplies the independent collision-halo necessity

\[
r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
\]

Thus the finite domain `r<=10^9` contains every right offset relevant through depth

\[
3\cdot10^9+3.
\]

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE / FINITE ONLY`.

Exact finite consequence:

\[
\boxed{
\text{no internal adjacent-block same-endpoint candidate coupling for }
61\le k\le3,000,000,003
}
\]

within the audited universal-spine/coefficient-survival scope.

### O — Outcome

Established:

- exact composition of MATH-027 and MATH-025;
- finite right-offset domain extended to `10^9`;
- 1,796,718 exact depth-61 survivors;
- zero states survive rolling continuation through depth 1029;
- internal adjacent-block same-endpoint coupling exclusion extended to depth `3,000,000,003`.

Still open:

- right offsets above `10^9`;
- full first-cell halo;
- candidate mechanisms not involving such endpoint coupling;
- first-cell emptiness;
- Collatz.

## AP-2 and implementation audit

No state is merged because of equal truncated phase. Residues select local rules only; exact endpoints are propagated.

Threshold arithmetic in the final certificate is arbitrary precision. Fixed-width overflow in an exploratory threshold generator was identified and rejected, demonstrating the implementation audit gate rather than being hidden as evidence.

## Prohibited upgrades

Do not infer:

- finite `r<=10^9` ⇒ all collision-halo offsets;
- depth `3,000,000,003` ⇒ ordinary Collatz verification to that depth;
- same-endpoint coupling exclusion ⇒ candidate emptiness;
- finite maximum failure depth ⇒ universal lifespan bound;
- combined acceleration ⇒ complete proof.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_combined_lifting_rolling_bootstrap_1b_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-combined-lifting-rolling-bootstrap-1b.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-028`
