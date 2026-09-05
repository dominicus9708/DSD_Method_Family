# DSD Gravity — Experiments 607–620

Date: 2026-09-06

Status: conditional reciprocal/common-action spherical specialization. Historical folder name `structural_gravity_logs` is retained for continuity after the repository rename to `DSD_Method_Family`.

## 607 — Continuum regularization of the radial axis tensor

For `ell_A>0`, write

\[
a(s)=s^2g(s),\qquad U_s=s\,r(s),\qquad g_s=s\,k(s).
\]

This removes the explicit `6a/s^2` coordinate singularity from the radial tensor equation.

Verdict: **pass**.

## 608 — Center compatibility

Regularity gives

\[
r(0)=-\frac{\epsilon U(0)}{2},
\]

and

\[
k(0)=\frac{g(0)-2\beta_A\chi_A r(0)^2}{7\ell_A^2}.
\]

These conditions provide a regular shooting start for the continuum two-field problem.

Verdict: **pass**.

## 609 — Boundary-amplitude parameterization

For prescribed boundary axis amplitude `a_b`, the endpoint conditions are

\[
U(1)+p(a_b)U_s(1)=1,
\]

\[
g(1)=a_b,
\]

\[
k(1)=-2a_b,
\]

where `p(a)=exp(-2 beta_A a/3)`. The last condition is the natural radial axis boundary condition `a_s(1)=0`.

This lets the stationary branch be represented as `epsilon(a_b)` and identifies a fold without pseudo-arclength in the continuum control problem.

Verdict: **pass**.

## 610 — Continuum fold control at beta=2, chi=0.5, ell=0.1

Direct continuum shooting gives

\[
a_b^{\rm fold}=0.6285014730,
\]

\[
\epsilon_{\rm fold}=0.5290983076.
\]

The unconstrained branch reaches the admissibility boundary `a_b=1` at

\[
\epsilon_{a=1}=0.5067850836.
\]

Thus this control remains fold-first.

Verdict: **pass**.

## 611 — Center-start sensitivity

Changing the shooting start radius through

`1e-4, 3e-5, 1e-5, 3e-6`

left the fold evaluation at fixed `a_b=0.628501473` unchanged to the displayed digits:

\[
\epsilon\simeq0.529098307583.
\]

The `a_b=1` contact likewise remained

\[
\epsilon\simeq0.506785083694.
\]

Verdict: **pass; no visible start-radius artifact at this precision**.

## 612 — Continuum vs finite-grid extrapolation

Earlier finite-grid extrapolation gave approximately

\[
\epsilon_{\rm fold}^{FD}\approx0.52909879,
\qquad
\epsilon_{a=1}^{FD}\approx0.50678555.
\]

The continuum differences are about

\[
4.82\times10^{-7},\qquad4.66\times10^{-7},
\]

respectively, or roughly `9e-7` relative.

Verdict: **the earlier finite-grid extrapolation is independently validated for this control point**.

## 613 — Continuum ell=0.2 control

At `(beta,chi,ell)=(2,0.5,0.2)`:

\[
a_b^{\rm fold}=0.5817591162,
\]

\[
\epsilon_{\rm fold}=0.5767733499,
\]

\[
\epsilon_{a=1}=0.5408079706.
\]

Verdict: **pass**.

## 614 — Continuum ell=0.3 control

At `(beta,chi,ell)=(2,0.5,0.3)`:

\[
a_b^{\rm fold}=0.5489473664,
\]

\[
\epsilon_{\rm fold}=0.6334858113,
\]

\[
\epsilon_{a=1}=0.5851685352.
\]

Verdict: **pass**.

## 615 — Spatial stiffness trend survives in the continuum

For fixed `(beta,chi)=(2,0.5)`, increasing `ell_A` from `0.1` to `0.2` to `0.3` raises both the unconstrained fold epsilon and the `a_b=1` contact epsilon while lowering the axis amplitude at the fold.

Therefore the earlier statement

\[
\ell_A\uparrow\ \Rightarrow\ \text{axis-feedback softening is suppressed}
\]

survives replacement of the radial finite-difference calculation by a continuum BVP.

Verdict: **conditional confirmation strengthened**.

## 616 — Continuum fold-first/saturation-first boundary at chi=0.5, ell=0.1

Define the regime boundary by

\[
\left.\frac{d\epsilon}{da_b}\right|_{a_b=1}=0.
\]

Continuum shooting gives

\[
\beta_{FS}^*(\chi_A=0.5,\ell_A=0.1)\approx1.06331.
\]

Verdict: **pass**.

## 617 — Boundary-derivative step control

Using centered boundary-amplitude steps

`h=0.015, 0.010, 0.008, 0.006, 0.005`

gives approximately

`1.0634115, 1.0633453, 1.0633262, 1.0633114, 1.0633055`.

Thus the continuum boundary is stable near

\[
\boxed{\beta_{FS}^*\simeq1.06330}
\]

for this parameter slice.

Verdict: **pass**.

## 618 — Susceptibility dependence of the continuum regime boundary

At `ell_A=0.1`:

| chi_A | continuum beta_FS* |
|---:|---:|
| 0.25 | 0.8936168 |
| 0.50 | 1.0633255 |
| 1.00 | 1.2122420 |

Thus on this tested slice

\[
\chi_A\uparrow\ \Rightarrow\ \beta_{FS}^*\uparrow.
\]

This remains a slice result, not a universal monotonicity theorem.

## 619 — Spatial-stiffness dependence of the continuum regime boundary

At `chi_A=0.5`:

| ell_A | continuum beta_FS* |
|---:|---:|
| 0.10 | 1.06333 |
| 0.20 | 0.93490 |
| 0.30 | 0.83867 |

Thus on this tested slice

\[
\ell_A\uparrow\ \Rightarrow\ \beta_{FS}^*\downarrow.
\]

The trend agrees with the earlier finite-grid map.

## 620 — Audit correction on the ell=0 codimension-two estimate

The exact local constitutive fold/saturation boundary remains

\[
\beta_A=\frac32
\]

for the reciprocal `ell_A=0` eliminated law.

However, attempts to sharpen the susceptibility at which the global fold merges into that local endpoint become numerically ill-conditioned because `d epsilon/d a_b` itself degenerates as `(beta_A,a_b) -> (3/2,1)`.

Therefore the previously stated `chi_A ~ 0.30–0.31` is retained only as a **provisional numerical bracket**, not promoted to a theorem or precise critical constant. The finite-ell continuum BVP results above do not depend on assigning a precise value to this ell=0 codimension-two point.

Verdict: **correction / claim-strength reduction**.

## Current impact on the DSD-gravity logic chain

Survives:

\[
\text{reciprocal common action}
\to
\text{continuum axis-field BVP}
\to
\text{admissibility saturation and global fold as distinct events}
\to
\text{finite-ell regime boundary }\beta_{FS}^*(\chi_A,\ell_A).
\]

Not established:

- a universal value of `beta_A`, `chi_A`, or `ell_A`;
- a black-hole or horizon interpretation of any fold;
- a precise ell=0 codimension-two susceptibility;
- derivation of `mu_0` from DSD alone.

Next audit target: use the continuum BVP as the static background for the time-dependent axis-inertia/damping problem, while first checking the kinetic operator and causal-speed normalization independently of the static fold location.
