# DSD-AUDIT-20260908-MATH-025 — Collatz rolling 11-step tail operator

Date: 2026-09-08

Verdict:

`CONFIRMED / EXACT LOCAL OPERATOR / COMPUTATIONAL ACCELERATION`

Global status:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## Audited question

Can the MATH-011 fixed `61+11` complete descriptor be generalized to an exact operator that advances **any** current endpoint by one 11-step shortcut window, without scalar step-by-step iteration?

## DSD tuple

### D — Definition

At current shortcut depth `K`, let the exact state used by this operator be

\[
(K,q,n),
\]

where `q` is the accumulated odd-step count and `n` is the exact current ordinary shortcut endpoint.

Set

\[
u=n\bmod2^{11}.
\]

For this residue let `s_j(u)` be the odd count in the first `j` of the next 11 shortcut steps and let

\[
s(u)=s_{11}(u).
\]

For the coefficient threshold sequence `Q(k)`, define

\[
H_K(u)=\max_{1\le j\le11}\bigl(Q(K+j)-s_j(u)\bigr).
\]

### R — Resolution

The operator retains exactly the information needed by one 11-step window:

- exact base depth `K`;
- exact accumulated odd count `q`;
- exact endpoint `n` for the affine transition;
- endpoint residue `u=n mod 2048` for selecting the 11-step parity descriptor.

No quotient of the exact endpoint is used as the next full state.

### S — Selection

The certificate exhausts all

\[
u=0,\dots,2047
\]

and all audited base depths

\[
K=0,\dots,1024.
\]

For every `(K,u)`, threshold cases around `H_K(u)` are compared with direct 11-step coefficient checks.

Total exact survival comparisons:

\[
\boxed{6,297,600}.
\]

For each residue, six different lifts `n=u+2^{11}t`, including a very large integer lift, are directly iterated for 11 shortcut steps and compared with the affine transition.

### E — Exclusion / representation gate

The 11-step survival predicate is exactly

\[
\boxed{q\ge H_K(u)}.
\]

If it fails, at least one coefficient threshold inside the next 11 steps fails.

If it passes, all 11 thresholds pass.

This exclusion is local to the audited coefficient-survival mechanism. It does not exclude an ordinary Collatz integer from the conjecture.

### T — Transition

Define `c(u)` by

\[
2^{11}T^{11}(u)=3^{s(u)}u+c(u).
\]

All integers congruent to `u mod 2^{11}` share the same next 11 parity bits, so the exact transition is

\[
\boxed{
T^{11}(n)=\frac{3^{s(u)}n+c(u)}{2^{11}}
}
\]

with

\[
\boxed{q'=q+s(u)}.
\]

Thus 11 scalar shortcut steps are replaced exactly by:

1. one residue lookup;
2. one threshold lookup;
3. one affine endpoint update.

### C — Consistency

This is the rolling generalization of the MATH-011 descriptor.

MATH-011 used one fixed base depth `K=61`. MATH-025 permits the same construction at arbitrary `K` while preserving exact ordinary-endpoint lineage.

The frozen published-floor threshold

\[
(3+2^{-71})^q>2^k
\]

was checked against the integer threshold used by the implementation throughout the audited range.

### N — Norm

Evidence status:

`ESTABLISHED_WITHIN_SCOPE`.

The operator is complete for **one 11-step coefficient-survival window** once the exact state `(K,q,n)` is supplied.

It is not a complete descriptor of the entire Collatz/Hensel state.

### O — Outcome

Established:

- exact rolling 11-step coefficient gate;
- exact rolling 11-step affine transition;
- exhaustive residue/depth regression in the stated finite validation range;
- reusable computational acceleration for later finite bootstrap scans.

Not established:

- arbitrary state merging by `(K,q,u)` alone;
- a universal Collatz theorem;
- a universal lifespan bound;
- first-cell emptiness.

## AP-2 audit

No finite-state aliasing is introduced into the propagated state because `u` is used only to **select** the local descriptor. The next state carries the exact affine endpoint `n'`, not merely its 11-bit residue.

Therefore the dangerous transition

\[
\text{same residue}\Rightarrow\text{same full future state}
\]

is never assumed.

## Prohibited upgrades

Do not infer:

- one-window completeness ⇒ arbitrary-depth quotient completeness;
- same `(K,q,u)` ⇒ same full Collatz state;
- local computational acceleration ⇒ stronger Collatz theorem;
- coefficient-gate failure ⇒ ordinary Collatz candidate impossible.

## Reproducibility

Math-verification certificate:

`collatz/src/2026_09_08_rolling_11step_tail_operator_certificate.cpp`

Math-verification note:

`collatz/notes/2026-09-08-rolling-11step-tail-operator.md`

Audit ID:

`DSD-AUDIT-20260908-MATH-025`
