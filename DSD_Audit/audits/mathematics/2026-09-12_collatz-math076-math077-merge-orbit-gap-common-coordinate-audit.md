# DSD Audit — Collatz MATH-076/077 generalized merge credit and orbit-gap threshold

Date: 2026-09-12

Status: `PASS WITH CLAIM BOUNDARIES / STATE REDUCTION ACCEPTED / GLOBAL SIGN AND STOPPING CLAIMS OPEN`

## 1. Scope

This audit reviews two new reductions in `dominicus9708/Math-verification`:

- MATH-076: generalized same-depth cross-`q` endpoint merge credit;
- MATH-077: common orbit-gap threshold for first descent, first coefficient crossing, and the first-cell terminal condition.

The audit also checks consistency with the older integrated depth-32 DSD state, the first-descent interval formulation, MATH-051 fixed-layer Hensel credit, and MATH-072 common coordinates.

The Collatz conjecture remains `OPEN`. The first universal Farey cell remains `OPEN`. Paid-count layers `2<=r<=13` are outside this audit.

## 2. Accepted exact identities

For a parity word of depth `k` and odd count `q`, define

\[
S=C/3^q,
\qquad
\rho=2^k/3^q.
\]

The old canonical state identity is exactly

\[
\boxed{\rho y=r+S}.
\]

### 2.1 Merge credit

For two same-depth states with a common endpoint and

\[
q_H=q_L+d,
\]

MATH-076 derives

\[
\boxed{
G_d=r_L-3^dr_H=3^dS_H-S_L.
}
\]

With MATH-072's `S=1+Sigma-rho`, this is

\[
\boxed{
G_d=(3^d-1)+3^d\Sigma_H-\Sigma_L.
}
\]

The derivation preserves exact same-integer/address coordinates and uses no statistical assumption. `PASS`.

### 2.2 Orbit gap

MATH-077 rewrites the exact affine iterate as

\[
\boxed{
T^k(N)-N=\frac{S-N(\rho-1)}{\rho}.
}
\]

For `rho>1`, the real threshold

\[
\boxed{N_*=S/(\rho-1)}
\]

orders compatible starts by descent/non-descent at that prefix. `PASS`.

## 3. DSD state-reduction result

The following formerly separate quantities are derived coordinates rather than independent state variables once exact address lineage and `(S,rho)` are retained.

### 3.1 Historical first-crossing occupancy

\[
\theta
=\frac{R_{corr}}{N(2^k-3^q)}
=\frac{S}{N(\rho-1)}
=\frac{N_*}{N}.
\]

Therefore `theta` is an occupancy ratio of the common threshold. It need not be retained as an independent coordinate.

### 3.2 Historical first-crossing integer margin

The historical quantity called `H=2N-z` satisfies

\[
H_{gap}=\frac{2[N(\rho-1)-S]}{\rho}.
\]

It is a scaled terminal descent gap and is derived from `(N,S,rho)`.

### 3.3 First-descent interval upper bound

For a depth-`K` dyadic source cylinder

\[
N=r+2^K m,
\]

when a tested prefix has `rho>1`, non-descent at that prefix is exactly

\[
r+2^K m\le N_*.
\]

Hence the old affine upper bound on the unresolved lift parameter is simply

\[
\boxed{
m\le\left\lfloor\frac{N_*-r}{2^K}\right\rfloor
}
\]

when the right side is nonnegative. This is a lattice projection of the same threshold, not a separate dynamical mechanism.

### 3.4 First-cell terminal correction

MATH-054's

\[
\delta=2^{A_0}/3^{q_0}-1
\]

is exactly

\[
\delta=\rho-1.
\]

Thus its hypothetical bad-path necessity

\[
S\ge\delta N
\]

is precisely the non-descending side of the universal orbit-gap identity.

`STATE REDUCTION ACCEPTED`.

## 4. Important non-equivalences preserved

The reductions above must not collapse distinct logical layers.

### 4.1 Hensel credit versus endpoint merge

At fixed `(k,q)`, MATH-051 uses integer `Delta Sigma` to test Hensel translation/dominance possibilities. MATH-076 shows that cross-`q` common-endpoint credit is expressed in the same `S/Sigma` coordinate.

This does **not** imply that every Hensel comparison is an endpoint merge, nor that endpoint compatibility follows from a carry credit alone.

### 4.2 Threshold versus eventual descent

`N_*=S/(rho-1)` decides descent for one fixed prefix once `rho>1`. It does not prove that every positive integer reaches a suitable prefix, nor that every first coefficient crossing has `N>N_*` at arbitrary depth.

### 4.3 Finite positivity versus global ordering

MATH-076's depth-26 regression observes 388 true first merges, all with `G_d>0`. This is finite evidence only. The exact identity does not determine the sign by itself.

### 4.4 Finite first-crossing descent versus Proposition A

MATH-077 reproduces 190,067 first-crossing candidates through depth 26 with zero descent failures. This does not prove global equality of coefficient stopping time and actual descent time.

## 5. Regression audit

### MATH-076

Through depth 26:

- true first merges: `388`;
- `d=1`: `243`;
- `d=2`: `136`;
- `d=3`: `9`;
- merge-credit identity failures: `0`;
- Sigma-form failures: `0`;
- observed negative or zero `G_d`: `0`.

### MATH-077

Historical first-crossing candidate set through depth 26:

- candidates: `190,067`;
- historical per-depth counts reproduced exactly;
- `theta = S/[N(rho-1)]` failures: `0`;
- integer-margin bridge failures: `0`;
- finite strict-descent failures: `0`.

The algebraic identities are not dependent on these finite tests; the tests certify implementation translation.

## 6. Notation audit

Two historical symbol collisions must be avoided in future work.

1. `R_corr`: old correction numerator in `2^k y=3^q r+R_corr`.
2. `R_res`: recent resolution height `ceil(log2 M)`.

They are unrelated quantities and must not both be written simply as `R` in a common proof state.

Likewise:

1. `H_gap`: historical first-crossing integer descent margin.
2. `H_Bellman`: Bellman/potential function.

They must not share the bare symbol `H` in the integrated derivation.

Recommended current analytic/address state notation:

\[
(k,q,r,S;\,\Omega,R_{res};\,\mathcal A_{dom}),
\]

with `rho=2^k/3^q` derived and exact dyadic compatibility carried by `r` or its exact cylinder equivalent.

## 7. DSD conclusion

The new identities pass the latest DSD checks for:

- exact formation;
- same-integer lineage preservation;
- exact channel compatibility;
- no density-to-emptiness upgrade;
- no finite-to-global upgrade;
- no conflation of Hensel dominance with dyadic compatibility;
- removal only of algebraically redundant descriptors.

The strongest accepted structural conclusion is:

\[
\boxed{
\text{Hensel credit, cross-layer merge credit, first-descent interval bounds,}
\text{ first-crossing occupancy, and first-cell terminal necessity}
\text{ all admit one common }(S,\rho)\text{-centered description.}
}
\]

What remains open is not the coordinate translation but the global inequality/ordering needed to force every admissible same-integer path into descent.

## 8. Next audit target

The next high-value comparison is to take data that were not used to derive these identities and test the common coordinates out of sample:

1. Beatty-ballot coefficient language through depth 191;
2. root-safe/root-credit and endpoint-q-lock data through depth 195;
3. internal-boundary/collision data through depths 72--81;
4. closed paid-count layers `r=14..17`.

These should be used as validation data, not folded into the derivation before testing.
