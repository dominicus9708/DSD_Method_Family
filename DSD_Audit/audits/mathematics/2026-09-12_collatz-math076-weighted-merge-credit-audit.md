# DSD Audit — Collatz MATH-076 weighted merge-credit bridge

Date: 2026-09-12

Status: `PASS WITH FINITE-SCOPE BOUNDARY`

## Audited object

MATH-076 introduces, for two depth-`k` states with `q_H=q_L+d`,

\[
\Gamma_d=3^dS_H-S_L,
\qquad
A_d=r_L-3^dr_H,
\]

and the exact residual identity

\[
\boxed{\Gamma_d-A_d=\rho_L(y_H-y_L)}.
\]

At a common endpoint,

\[
\boxed{\Gamma_d=A_d}.
\]

## DSD channel separation

The audit keeps three roles distinct:

1. **correction/Hensel channel**: `Gamma_d`;
2. **dyadic address compatibility channel**: `A_d`;
3. **observable endpoint residual**: `rho_L Delta y`.

This resolves a prior risk of over-compressing the exact address into Hensel/carry data alone.

At fixed `q` (`d=0`), Hensel integrality constrains `Gamma_0=Delta S`, but actual endpoint equality additionally requires the exact address credit to satisfy

\[
A_0=\Gamma_0.
\]

Therefore the earlier rule "Hensel-only implication is invalid" is preserved, not weakened.

## Exact finite regression

The companion certificate regenerates the coefficient-surviving tree through depth 32 and reproduces exactly 6996 true first merges.

Observed sectors:

- `d=1`: 4549 positive, 0 zero, 0 negative;
- `d=2`: 2305 positive, 0 zero, 0 negative;
- `d=3`: 141 positive, 0 zero, 0 negative;
- `d=4`: 1 positive, 0 zero, 0 negative.

The sum is 6996, so no true-merge pair in the audited range is omitted by the generalized credit classification.

## Safe claims

- `Gamma_d-A_d=rho_L Delta y` is an exact algebraic identity.
- `Gamma_d=A_d` is an exact necessary and sufficient condition for equality of the two represented endpoints once the two states and `d` are fixed.
- Through depth 32, every true first merge has positive aligned credit.
- The old `d=1` contrast `G=r_L-3r_H` is exactly `3S_H-S_L` at a merge.
- Fixed-q Hensel translation and cross-q endpoint merge are different sections of the same aligned-correction formalism.

## Prohibited upgrades

- finite positivity through depth 32 => arbitrary-depth positivity;
- integer `Gamma_d` => actual merge without checking `A_d`;
- positive merge credit => first-cell closure;
- ordered separation at depths 79--81 => proof of weighted-credit positivity at all depths;
- MATH-076 => closure of `2<=r<=13` or Collatz.

## DSD interpretation

The important reduction is not that the address channel disappears. Instead, the two previously separate channels are coupled by one exact residual:

\[
\boxed{\text{correction credit}-\text{address credit}=\text{scaled endpoint separation}.}
\]

This is a useful common-coordinate bridge because any future quotient must preserve enough information to determine both credits, but it need not treat them as unrelated quantities.

## Verdict

`PASS WITH FINITE-SCOPE BOUNDARY`.

MATH-076 is suitable as a common-state identity and theorem-discovery target. The positivity pattern remains a finite exact observation and must be tested/proved separately at larger depth or by structural recursion.
