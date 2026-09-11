# DSD Audit — Collatz phase-address mechanical barrier

Date: 2026-09-11
Status: `EXACT SAME-INTEGER PHASE/ADDRESS BARRIER / CUMULATIVE VALUE CORRECTION / GLOBAL PROOF OPEN`

## Audited claim

Within the current first-cell ordinary-start window and before the first coefficient crossing, every `u=0` zero-penalty mechanical continuation has length at most 78.

The audit uses exact rational phase intervals, exact dyadic factor residues, and the same phase in the ordinary-start relation. No sampled phase or probabilistic frequency is used.

## Representation chain

The relevant DSD reduction is

\[
(q,d,\text{word},N)\to(q,u,\Omega,N)\to(\Omega,R,N\text{-window}),
\]

where

\[
u=m(q)-d,
\qquad
\Omega=2^{-\{q\log_2(3/2)\}}.
\]

At `u=0`, all future zero-penalty parity is determined by the single phase `Omega`. A length-L factor has one exact start residue `R mod 2^L`.

Because every boundary-anchor endpoint is `<2^73`, for `L>=73` the endpoint is the actual integer `R`, not merely its residue class. This is the crucial resolution change that makes the phase/address test pointwise.

## Exact exclusion

The phase range `(1/2,1)` is partitioned at the exact rational thresholds

\[
\tau_r=3^r/2^{r+m(r)+1}.
\]

For each interval the mechanical factor and its exact start residue are constant. Same-integer compatibility requires

\[
2^{71}<\Omega R<1364\,2^{61}+q_0/3.
\]

Exact interval intersection gives 2 compatible intervals at length 78 and none at length 79. The special phase `q=0`, `Omega=1` is also excluded at length 79.

Verdict:

\[
\boxed{\text{zero-penalty mechanical segment length}\le78.}
\]

## Cumulative-penalty consequence

If `P` is the number of positive-slack odd events in a length-K coefficient-valid prefix, paid-cluster decomposition gives

\[
K\le81P+78.
\]

Every such event costs `>1/12`, so

\[
\boxed{
\mathcal P_K>
\frac1{12}\left\lceil\frac{K-78}{81}\right\rceil.
}
\]

This is a structural cumulative lower bound, not an extrapolation from finite sampled depths.

## Audit correction to MATH-056 direction

MATH-056 optimized the penalty accumulated only during the first 72 steps while increasing the survival horizon K. That finite value function is valid, but its objective is frozen in time. Therefore a permanent positive additive law for that exact `V(K)` is not the natural asymptotic target.

The proof-facing value is instead

\[
W(K)=\min \mathcal P_K,
\]

where penalty is accumulated through K itself. MATH-057 provides the first nonzero linear lower bound for `W(K)`.

This is a methodological correction, not a retraction of the finite MATH-056 minima.

## DSD information-loss audit

Safe merges:

- replacing the full zero-penalty word by phase `Omega` at a `u=0` anchor;
- replacing an L-step factor by its exact dyadic start residue `R` after the endpoint `<2^73` bound is established;
- replacing individual paid histories by the cluster count bound only for a lower-bound theorem.

Unsafe upgrades:

- phase/address barrier => first-cell emptiness;
- linear positive penalty => sufficient terminal correction deficit without a quantitative comparison;
- `W(K)` lower bound => arbitrary later-strip coverage;
- finite first-cell theorem => Collatz proof.

## Next exact target

The scalar 78-step barrier discards transition compatibility between successive long zero-penalty segments. The next DSD-safe refinement is a weighted macro-transition graph whose vertices are boundary-anchor phase/address classes and whose edges are paid clusters. A minimum cycle/mean-cost bound on that graph could improve the current `1/(81*12)` penalty slope without returning to word enumeration.
