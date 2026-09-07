# DSD-AUDIT-20260907-MATH-004 — Collatz first-cell endpoint q-lock

Date: 2026-09-07
Domain: Mathematics / Collatz
Primary repository: `dominicus9708/Math-verification`

## Revision outcome

**Verdict: CONFIRMED across the full current first-universal-cell candidate language through the terminal first crossing.**

The original `k<=195` audit was correct but used an unnecessarily weak all-word correction envelope. A stronger candidate-language audit uses the universal-spine odd-position bound and proves

\[
S=R/3^q\le q/3<B_0
\]

through the whole first cell. Therefore endpoint q-lock remains valid for every candidate prefix through

\[
k=A_0=114,208,327,604.
\]

This revision preserves the older result as a valid weaker historical stage.

## Scope lock

Current start window:

\[
B_0=2^{71},
\qquad
B_0<N<\frac{1364}{1024}B_0.
\]

First universal cell:

\[
(A_0,q_0)
=(114,208,327,604,
72,057,431,991).
\]

The compared states must both lie in the universal minimal-counterexample prefix language through the depth being audited.

## Strengthened correction lemma

Let `p_r` be the zero-indexed position of the `r`-th odd step. Before that step the prefix has `r-1` odd entries and has not yet crossed the coefficient boundary, hence

\[
2^{p_r}\le3^{r-1}.
\]

Therefore

\[
S
=\sum_{r=1}^q\frac{2^{p_r}}{3^r}
\le\frac q3.
\]

Since `q<=q0` and `q0/3<B0`, every compared candidate state has `S<B0` throughout the first cell.

## Claim under audit

For two candidate-window universal-spine starts whose length-`k` prefixes reach the same endpoint,

\[
T^k(N_1)=T^k(N_2),
\qquad
1\le k\le A_0,
\]

show that

1. their odd counts are equal;
2. smaller start is equivalent to larger correction;
3. the endpoint fiber is an exact Hensel/address-translation fiber;
4. the ordinary-address diameter of one such candidate fiber is `<q/3`, hence `<2^35` at the first-cell terminal depth.

## Eight-axis audit

### D — Describability

PASS.

Ordinary start, prefix depth, odd positions, odd count, correction, normalized correction, endpoint, and address displacement are explicit.

### R — Resolution

PASS.

The proof remains at exact ordinary-integer and exact endpoint resolution. No density or averaged quotient replaces lineage.

### S — Selection

PASS WITH EXPLICIT LANGUAGE LOCK.

The strengthened `S<=q/3` bound applies only because both compared states satisfy the universal prefix spine. It must not be imported to arbitrary Hensel competitors outside that language.

### E — Exclusion

PASS.

If `q_1>q_2`, equal endpoints imply

\[
N_2+S_2=3^{q_1-q_2}(N_1+S_1)>3B_0,
\]

while the start cap and candidate-language correction theorem give

\[
N_2+S_2<C_*+B_0<3B_0.
\]

Contradiction. Hence equal endpoint forces equal `q` throughout the first cell.

### T — Transition / lineage

PASS.

The merge is an exact equality of two root-start trajectories at the same depth. No arbitrary later-block pullback or representative substitution is used.

### C — Consistency

PASS.

With equal `q`,

\[
R_1-R_2=3^q(N_2-N_1).
\]

Thus the endpoint fiber is precisely the same-`q` Hensel correction congruence equipped with its exact ordinary-start translation.

### N — Norm

PASS.

Minimal-positive-counterexample ordering is applied directly: a larger start that merges with a smaller positive start cannot be minimal.

### O — Outcome

CONFIRMED, WITH RANGE DISTINCTION.

- candidate-language endpoint q-lock: valid through the entire first cell;
- arbitrary-competitor full-Hensel maximality: still only automatically credit-safe through its separately proved root-safe range;
- the two mechanisms overlap through depth 195 but are not interchangeable outside their respective hypotheses.

## Address-locality consequence

For same-endpoint candidate states with common `q`,

\[
|N_1-N_2|=|S_1-S_2|<q/3.
\]

At the first-cell terminal depth,

\[
|N_1-N_2|<q_0/3<2^{35}.
\]

Each surviving top-address block has width `2^61`. Therefore endpoint fibers are block-local except within exact `<2^35` boundary halos, and no endpoint fiber can skip a block.

## Required prohibited upgrades

- Do not apply `S<=q/3` to arbitrary competitors that fail the universal prefix spine.
- Do not extend arbitrary-word full-Hensel maximality to the whole first cell from this result.
- Do not count endpoint quotient and Hensel translation as independent stochastic exclusions in their overlap range.
- Do not infer emptiness from the `<2^35` fiber diameter.
- This theorem does not close the first universal cell or Collatz.

## Evidence

Original weaker exact certificate:

`e4e921f9b19aeacc85d96c37731e0867c52fea98`

Full-first-cell scale certificate:

`522b7412e7b3bbf96e3c2ea8b45c642d9c46b305`

Canonical explanatory revision:

`83e221195a12fe774b0ed13ff7f1c251ad237261`

## Next audited transition

Separate the 340 top-address blocks into interiors and `<2^35` endpoint boundary halos. Any next quotient must preserve the exact ordinary address and may merge states across blocks only inside those audited halos.