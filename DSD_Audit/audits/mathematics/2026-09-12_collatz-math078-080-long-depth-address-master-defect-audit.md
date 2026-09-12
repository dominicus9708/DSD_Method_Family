# DSD Audit — Collatz MATH-078--080 long-depth envelope, address-credit separation, and master defect

Date: 2026-09-12

Status: `PASS / COMMON COORDINATE CONSOLIDATED / GLOBAL INEQUALITY STILL OPEN`

## 1. Scope

This audit covers:

- MATH-078: out-of-sample common-coordinate translation of depth-191 and depth-195 certificates;
- MATH-079: address contrast minus correction credit as endpoint separation;
- MATH-080: master affine comparison defect.

The objective is not to promote finite certificates into a Collatz proof. It is to determine whether the many historical descriptors are genuinely independent or are exact projections of a smaller future-relevant state.

## 2. Out-of-sample validation accepted

MATH-078 uses results developed independently before the current `(S,rho)` reduction.

The old fixed-`(k,q)` normalized root-credit envelope

\[
2^{k-q}\left(1-(2/3)^q\right)
\]

is exactly

\[
\boxed{2^{k-q}-\rho},
\qquad
\rho=2^k/3^q.
\]

With `S=1+Sigma-rho`, this is the elementary fixed-layer upper envelope for `S`.

The old forced-OO uniform safety inequality through depth 191,

\[
R_{max}<V_0(2^j-3^q),
\]

becomes exactly

\[
\boxed{S_{max}<V_0(\rho-1)}.
\]

The old depth-195 root-safe threshold and first-cell endpoint q-lock are likewise recovered from the same `S` envelope.

Because these data were not used to derive MATH-072/077, this counts as meaningful structural cross-validation rather than circular regression. `PASS`.

## 3. Address and correction must remain distinct until compatibility is imposed

MATH-079 defines, for same-depth states with `q_H=q_L+d`,

\[
A_d=r_L-3^dr_H
\]

and

\[
C_d=3^dS_H-S_L.
\]

The exact separation law is

\[
\boxed{
\rho_L(y_L-y_H)=A_d-C_d.
}
\]

This resolves a prior DSD ambiguity.

- `A_d` is an address/compatibility coordinate.
- `C_d` is a correction/Hensel-credit coordinate.
- endpoint merge is the equation `A_d=C_d`.

Therefore a Hensel carry state may compress `C_d` but cannot, by itself, certify same-integer endpoint compatibility. The dyadic address side is not redundant merely because correction credit is known.

`PASS`.

## 4. Historical collision halos reinterpreted correctly

Depth-72 and depth-75 internal-boundary certificates first used an analytic displacement envelope to prove that a collision, if any, had to lie inside a finite halo around each large dyadic block boundary. They then scanned exact address/endpoint states inside that halo.

MATH-078/079 show that this is exactly:

\[
\boxed{
\text{bound }|C_0|\text{ by an }S\text{ envelope}
\quad\to\quad
\text{search only addresses }A_0\text{ capable of matching it}.
}
\]

Thus the old method already had the correct analytic/address division of labor, though it was not expressed in the current common coordinates.

The depth-79--81 ordered-separation results are likewise sign statements for `A_0-C_0` after exact residue refinement. Their finite positive gaps must not be extrapolated to arbitrary depth.

## 5. Master affine comparison defect

MATH-080 defines

\[
\mathfrak D(X_1,X_2)
=\rho_2(a_1+S_1)-\rho_1(a_2+S_2)
\]

for affine states `X_i=(a_i,S_i,rho_i)`.

Since

\[
a_i+S_i=\rho_i y_i,
\]

one has identically

\[
\boxed{
\mathfrak D(X_1,X_2)
=\rho_1\rho_2(y_1-y_2).
}
\]

The identity is exact, antisymmetric, and zero exactly at endpoint equality.

This is accepted as the highest-level common **comparison coordinate** found so far.

It is not accepted as a proof invariant or Lyapunov function without an additional monotonicity/inequality theorem.

## 6. Self-descent and the first-cell terminal target are specializations

Compare a path state

\[
X=(N,S,\rho)
\]

with the identity reference

\[
X_0=(N,0,1).
\]

Then

\[
\boxed{
\mathfrak D(X,X_0)
=S-N(\rho-1)
=\rho[T^k(N)-N].
}
\]

Hence descent is `mathfrak D<0`.

With MATH-053

\[
S=S_{partial}-\mathcal P,
\]

the first-cell terminal defect is

\[
\boxed{
\mathfrak D_{term}
=S_{partial}-\mathcal P-N(\rho-1).
}
\]

MATH-060's penalty target is therefore exactly a sufficient route to force the master terminal defect negative.

This is a conceptual consolidation, not a new proof of the required penalty lower bound.

## 7. Revised minimal state hierarchy

The audit recommends separating the current proof state into the following roles.

### 7.1 Analytic affine state

\[
(k,q,S)
\]

with

\[
\rho=2^k/3^q
\]

derived.

Where phase dynamics are used, retain `Omega` or the equivalent exact phase descriptor required by the macro graph.

### 7.2 Exact source/address compatibility

Retain the exact dyadic source class, canonical residue, AP cylinder, or a proven equivalent residue quotient. Do not replace it by a real interval in `S`.

### 7.3 Dominance/correction-credit compression

Use bounded-carry/Hensel state only for the correction-credit question it actually answers.

### 7.4 Resolution budget

Retain

\[
R_{res}=\lceil\log_2M\rceil
\]

where multiplicity/resolution is needed for Bellman compensation and singleton handoff.

### 7.5 Target comparison

Use `mathfrak D` as a derived comparison/sign quantity, not as an independent stored coordinate when both compared affine states are already available.

## 8. Redundant descriptors now identified

Under the stated domain conditions, the following historical quantities are derived rather than independent:

- old correction numerator `R_corr = 3^q S`;
- old endpoint `y=(a+S)/rho`;
- old first-crossing `theta=S/[N(rho-1)]`;
- old crossing gap `H_gap=2[N(rho-1)-S]/rho`;
- fixed-layer normalized root-credit envelope `2^(k-q)-rho`;
- merge `G_d` after compatibility, as the common value `A_d=C_d`;
- first-cell `delta=rho-1`.

The following are **not** currently redundant:

- exact address/residue lineage;
- phase/macro legality information not recoverable from `(k,q,S)` alone;
- Hensel/dominance carry subset when dominance pruning is invoked;
- resolution multiplicity `R_res` when symbolic families remain unresolved.

## 9. Finite regressions

MATH-079:

- coefficient-surviving state pairs through depth 14: `372,731`;
- separation identity failures: `0`;
- merge-equivalence failures: `0`.

MATH-080:

- pair comparisons: `372,731`;
- start-reference comparisons: `1,608`;
- failures: `0`.

MATH-078 reproduces:

- root-safe envelope through depth `195`;
- first envelope failure `(196,124)`;
- forced-OO uniform safety through depth `191`;
- first simple envelope loss at depth `192`, `q=121`;
- first-cell q-lock envelope worst pair `(195,124)`.

## 10. Claim boundary

Accepted:

- common-coordinate reparameterization;
- exact separation/compatibility identity;
- master comparison defect;
- out-of-sample compatibility with depth-191/195 results;
- exact reinterpretation of old address-halo and ordered-separation calculations.

Open:

- global positivity/order of any separation margin;
- global first-crossing descent;
- a finite future-complete Bellman quotient;
- the `19/503` penalty lower bound;
- first-cell emptiness;
- later-cell coverage;
- the Collatz conjecture.

## 11. Next high-value target

The next calculation should not add another raw depth merely to extend a table. The strongest remaining target is to use the consolidated state to construct or falsify a small exact Bellman quotient.

A natural candidate state skeleton is

\[
\boxed{
(\Omega,\rho,S,R_{res},\text{exact compatibility residue},\text{optional carry class})
}
\]

with `S` possibly eliminated in favor of accumulated penalty where the boundary identity `S=S_partial-P` is exact.

The first test should use already closed `r=14..17` data as validation and hold out lower paid-count layers `2<=r<=13` as genuinely unseen data.
