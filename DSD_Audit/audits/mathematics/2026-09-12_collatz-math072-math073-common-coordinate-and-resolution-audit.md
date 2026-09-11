# DSD Audit — Collatz MATH-072/MATH-073 common coordinate and resolution potential

Date: 2026-09-12

Status: `SAFE ALGEBRAIC BRIDGE / SAFE PARTIAL BELLMAN POTENTIAL / GLOBAL CLOSURE OPEN`

## 1. Audit scope

MATH-072 identifies an exact coordinate bridge between the depth-41 fixed-d Hensel description and the later paid-count/phase description.

MATH-073 adds an exact dyadic source-resolution potential.

Neither result closes the first universal Farey cell or the Collatz conjecture.

## 2. Common analytic coordinate

Definitions:

\[
S=\frac{C}{3^q},
\qquad
\rho=\frac{2^k}{3^q},
\qquad
\Omega_q=\frac{2^{q+m(q)}}{3^q},
\qquad
u=m(q)-d.
\]

MATH-051 gives

\[
S=1+\Sigma_d-\rho.
\]

Since `k=q+d=q+m(q)-u`,

\[
\rho=2^{-u}\Omega_q.
\]

Therefore

\[
\boxed{
S=1+\Sigma_d-2^{-u}\Omega_q.
}
\]

This is an identity, not a fitted relation.

## 3. Penalty interpretation

The paid penalty atom

\[
p=\frac13(1-2^{-u})\Omega
\]

satisfies

\[
\boxed{p=(\Omega-\rho)/3}.
\]

An odd shortcut extension gives

\[
\Delta S=\rho/3.
\]

Hence

\[
\boxed{p=\Omega/3-\Delta S}.
\]

DSD interpretation: the paid penalty is the exact deficit between a phase-boundary reference increment and the actual normalized-correction increment.

## 4. Redundancy audit

The ratio

\[
x=\rho/\Omega
\]

satisfies

\[
x=2^{-u}.
\]

Thus `u` and `rho/Omega` are not independent state coordinates.

Similarly, at fixed `(k,d)` the value `rho` is fixed, so

\[
\Delta S=\Delta\Sigma.
\]

Therefore the depth-41 bounded-carry collision test is testing integer translation differences in the same normalized correction `S` used in the paid-count description.

## 5. Exact address coordinate

Let `M` be the number of ordinary source anchors in one exact dyadic source cylinder.

One additional parity bit refines the source residue modulo `2^h` to one residue modulo `2^{h+1}`.
The two child counts form a floor/ceiling split, hence

\[
M'\le\lceil M/2\rceil.
\]

Define

\[
R(M)=\lceil\log_2M\rceil.
\]

For every non-singleton child,

\[
\boxed{R'\le R-1}.
\]

This is an exact resolution monotone.

## 6. Bellman audit

For

\[
\lambda=19/503
\]

define

\[
H_R=-\lambda R.
\]

On a resolution-active unit transition with penalty increment `p>=0`,

\[
p-\lambda+H_R'-H_R
=p-\lambda+\lambda(R-R')
\ge p\ge0.
\]

Thus every exact multi-source resolution step is Bellman-safe under this partial potential.

This does not establish safety after source resolution reaches singleton.

## 7. 73 versus 89 audit

The existing source-resolution result gives the conservative first-cell bound

\[
R\le73.
\]

MATH-060 independently allows an additive overhead of 89 step units.

Therefore the resolution-potential range fits inside the existing allowance:

\[
73<89,
\qquad
89-73=16.
\]

Important claim boundary:

- `89` was not derived from `73`;
- MATH-073 only compares two independently established budgets;
- sufficiency of the remaining 16 units is OPEN.

## 8. Representation distinction

The following quantities must not be merged conceptually:

1. source-anchor count `M` in one dyadic same-integer cylinder;
2. target AP multiplicity after affine propagation;
3. AP-union multiplicity after merging same-grid intervals;
4. number of unique singleton ordinary integers.

MATH-073's `R` is defined from item 1 only.

Using item 2 or 3 as a substitute without ancestry tracking would be an invalid DSD coordinate substitution.

## 9. Current state skeleton

The present common-state candidate is

\[
\boxed{
(S,\rho,\Omega,R,\mathcal A)
}
\]

where `A` is the exact dyadic address class or an exact quotient retaining equivalent future information.

Known exact laws:

- even: `S'=S`, `rho'=2rho`, `Sigma'=Sigma+rho`;
- odd: `S'=S+rho/3`, `rho'=(2/3)rho`, `Sigma'=Sigma`;
- `rho=2^{-u}Omega`;
- `p=(Omega-rho)/3`;
- while multi-source: `R'<=R-1`.

The remaining unknown is the smallest exact quotient of `A` sufficient to certify post-resolution behavior without ordinary-integer enumeration.

## 10. SAFE conclusions

SAFE:

\[
S=1+\Sigma-\rho,
\]

\[
\rho=2^{-u}\Omega,
\]

\[
p=(\Omega-\rho)/3,
\]

\[
R'\le R-1\quad(M\ge2),
\]

and the partial Bellman inequality on resolution-active edges.

## 11. OPEN conclusions

OPEN:

- a complete Bellman potential for every legal long-path transition;
- symbolic closure of singleton/post-resolution states;
- sufficiency of the residual 16-step overhead;
- a bounded exact address quotient at arbitrary depth;
- `2<=r<=13` paid-count layers if treated layerwise;
- first universal Farey cell emptiness;
- the Collatz conjecture.

## 12. Next audit target

Use the MATH-051 bounded-carry state to compress the exact address coordinate after or near singleton resolution.

The concrete question is whether the Hensel translation/carry state can replace explicit ordinary-integer identity while preserving all information needed for future descent.

If successful, combine its potential with

\[
H_R=-\lambda R
\]

and the analytic deficit

\[
(\Omega-\rho)/3
\]

to form a complete Bellman state.
