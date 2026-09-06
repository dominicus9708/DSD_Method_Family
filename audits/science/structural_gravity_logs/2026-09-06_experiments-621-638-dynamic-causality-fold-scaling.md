# DSD Gravity Research Log — Experiments 621–638

Date: 2026-09-06

Current name: **Dimensional-Structural Describability Gravity (DSD Gravity)**. Historical folder name `structural_gravity_logs` is retained for repository continuity.

## Scope

This batch does not claim a universal gravity law, a derived value of `c_info`, a derived axis inertia, or a black-hole/horizon interpretation. It audits the reciprocal/common-action radial branch against the current DSD dynamical interface and extracts the dynamical consequences that survive without assigning missing constitutive normalizations.

---

## Experiment 621 — Dynamic-interface audit

The current Structural Reorganization Dynamics paper permits inertia-, stiffness-, restoration-, and coupling-like typed property data to influence dynamics only through an explicit constitutive dynamic bridge. Its second-order characteristic speeds are generalized eigenvalues of

\[
K(n)e=c^2Me.
\]

Verdict: the axis coefficients used below remain downstream constitutive coefficients. No property label is retroactively identified with physical mass, force, energy, or speed.

## Experiment 622 — Dimensionless axis inertia and damping

Use the conditional physical radial axis equation

\[
\mu_A a_{tt}+D_A a_t-\mathcal T_A L_{2,r}a+\mathcal R_Aa=F_A,
\]

where

\[
L_{2,r}a=a_{rr}+\frac2r a_r-\frac6{r^2}a.
\]

With

\[
s=\frac rR,\qquad \tau=\frac{c_*t}{R},
\]

define

\[
\nu_A=\frac{\mu_Ac_*^2}{\mathcal R_AR^2},
\qquad
\delta_A=\frac{D_Ac_*}{\mathcal R_AR},
\qquad
\ell_A^2=\frac{\mathcal T_A}{\mathcal R_AR^2}.
\]

Then

\[
\nu_Aa_{\tau\tau}+\delta_Aa_\tau-\ell_A^2L_2a+a=F_A/\mathcal R_A.
\]

Verdict: `nu_A` and `delta_A` are new dynamic data not fixed by the static branch.

## Experiment 623 — Axis characteristic speed

The principal high-frequency axis speed is

\[
c_A^2=\frac{\mathcal T_A}{\mu_A},
\]

hence

\[
\boxed{\frac{c_A}{c_*}=\frac{\ell_A}{\sqrt{\nu_A}}}.
\]

This matches the second-order generalized-eigenvalue structure of the DSD dynamics paper in the scalar isotropic axis-sector specialization.

## Experiment 624 — `c_info` compatibility for the axis sector

Requiring

\[
c_A\le c_{\mathrm{info}}
\]

gives

\[
\boxed{
\nu_A\ge \ell_A^2\left(\frac{c_*}{c_{\mathrm{info}}}\right)^2.
}
\]

If the extra specialization `c_*=c_info` is imposed, this reduces to

\[
\boxed{\nu_A\ge\ell_A^2}.
\]

Equality gives a shared sharp speed in this scalar axis sector; inequality leaves axis reorganization slower.

## Experiment 625 — Axis inertia is not statically identifiable

Changing `nu_A` or `delta_A` while holding the static coefficients `(beta_A, chi_A, ell_A)` fixed leaves the static Euler equations, equilibrium branches, saturation points, and static folds unchanged.

Verdict:

\[
\boxed{
\text{static DSD-gravity branch}\not\Rightarrow \mu_A\text{ or }D_A.
}
\]

The previous no-go separation between static support and axis inertia survives.

## Experiment 626 — Field characteristic cone under the determinant-one axis metric

For the radial uniaxial branch

\[
\mathcal A=a\left(P_r-\frac13I\right),
\qquad
h_A=e^{\beta_A\mathcal A},
\]

the inverse spatial coefficient has eigenvalues

\[
h_A^{rr}=e^{-2\beta_Aa/3},
\qquad
h_A^{tt}=e^{\beta_Aa/3}.
\]

For a local propagation direction making angle `theta` with the radial direction,

\[
\boxed{
\frac{c_U^2(\theta)}{c_*^2}
=e^{-2\beta_Aa/3}\cos^2\theta
+e^{\beta_Aa/3}\sin^2\theta.
}
\]

Thus, for `beta_A a >= 0`,

\[
c_{U,r}=c_*e^{-\beta_Aa/3},
\qquad
c_{U,\max}=c_*e^{\beta_Aa/6}.
\]

## Experiment 627 — Field-sector `c_info` headroom

To preserve the component-resolved propagation bound,

\[
c_{U,\max}\le c_{\mathrm{info}},
\]

one needs

\[
\boxed{
\frac{c_*}{c_{\mathrm{info}}}
\le e^{-\beta_Aa_{\max}/6}.
}
\]

For the continuum control fold

\[
(\beta_A,\chi_A,\ell_A)=(2,0.5,0.1),
\qquad
a_{\max}=a_b^{\rm fold}=0.62850146055,
\]

this gives

\[
\frac{c_{U,\max}}{c_*}=1.2330619754,
\qquad
\boxed{
\frac{c_*}{c_{\mathrm{info}}}\le0.8109892446.
}
\]

At full `a=1` saturation with `beta_A=2`, the uniform worst-case bound becomes

\[
\boxed{
\frac{c_*}{c_{\mathrm{info}}}\le e^{-1/3}=0.7165313106.
}
\]

Verdict: setting `c_*=c_info` is incompatible with this determinant-one anisotropic principal tensor once positive anisotropy is present. This is not a contradiction because the current research has kept `c_*` and `c_info` distinct.

## Experiment 628 — Combined field/axis causal control

If `c_*/c_info` is chosen to saturate the field bound at the control fold, then the axis condition becomes

\[
\nu_A\ge\ell_A^2(0.8109892446)^2.
\]

For `ell_A=0.1`,

\[
\boxed{\nu_A\ge0.00657703555.}
\]

This is a conditional lower bound on the dimensionless kinetic coefficient, not a derivation of `mu_A`.

## Experiment 629 — Conformal principal-factor alternative

A separate constitutive branch may replace the principal spatial tensor by

\[
\widetilde h_A^{ij}=\Omega_A(a)h_A^{ij}.
\]

The propagation bound requires

\[
\Omega_Ae^{\beta_Aa/3}
\le
\left(\frac{c_{\mathrm{info}}}{c_*}\right)^2.
\]

If `c_*=c_info`, the saturating choice

\[
\Omega_A=e^{-\beta_Aa/3}
\]

keeps the tangential characteristic speed at `c_*`.

However, this changes the radial static coefficient from `exp(-2 beta a/3)` to `exp(-beta a)` and therefore changes the previously calculated static thresholds.

Verdict: this is an alternate constitutive model, not a retroactive repair of the existing branch.

## Experiment 630 — Static exterior matching is not a dynamical boundary law

The static Robin condition

\[
U(1)+p(a_b)U_s(1)=1
\]

cannot simply be imposed at every time in a causal evolution: that would encode instantaneous exterior readjustment.

## Experiment 631 — Exact outgoing radial boundary under a Euclidean exterior

Assume the exterior is axis-free/Euclidean, source-free, and has no incoming radial disturbance. Put

\[
V=s(U-1).
\]

The exterior principal equation reduces to

\[
V_{\tau\tau}-V_{ss}=0.
\]

For an outgoing radial wave,

\[
V_\tau+V_s=0.
\]

Using flux continuity

\[
U_s^{\rm out}=p(a_b)U_s^{\rm in}
\]

at `s=1` yields

\[
\boxed{
U_\tau+U-1+p(a_b)U_s=0.
}
\]

Its static limit is exactly the previous Robin condition.

Verdict: the static continuum branch admits a causal outgoing-boundary extension under explicit exterior assumptions.

## Experiment 632 — Axis boundary audit

The continuum static branch uses

\[
a_s(1)=0.
\]

In a dynamical model this is naturally a no-gradient-flux/reflection boundary unless the axis carrier terminates at the source boundary. If axis reorganization is allowed to propagate into an exterior axis carrier, an exterior axis equation or radiation condition must be supplied instead.

Verdict: field causality can be closed by Experiment 631 under the stated exterior model, while axis-sector exterior support remains a model choice.

## Experiment 633 — Continuum fold curvature

For the previously verified continuum control point

\[
(\beta_A,\chi_A,\ell_A)=(2,0.5,0.1),
\]

\[
a_f=0.62850146055,
\qquad
\epsilon_f=0.529098307584,
\]

a symmetric continuum fit gives

\[
\boxed{
\epsilon_f-\epsilon
=Cq^2+O(q^3),
\qquad
q:=a_f-a_b,
\qquad
C\simeq0.230095.
}
\]

For comparison, the same fit gives approximately

\[
C(\ell_A=0.2)\simeq0.300064,
\qquad
C(\ell_A=0.3)\simeq0.358039
\]

at the corresponding `beta_A=2, chi_A=0.5` folds.

## Experiment 634 — Divergent static susceptibility

From

\[
q\sim\sqrt{\frac{\epsilon_f-\epsilon}{C}},
\]

one obtains

\[
\boxed{
\frac{da_b}{d\epsilon}
\sim
\frac{1}{2\sqrt C}
(\epsilon_f-\epsilon)^{-1/2}.
}
\]

For the control fold,

\[
\boxed{
\frac1{2\sqrt C}\simeq1.04236.
}
\]

Thus the static axis response becomes singular at the saddle-node even though `a_f<1` and no admissibility saturation has yet occurred.

## Experiment 635 — Generic saddle-node soft stiffness

A local one-mode potential consistent with the branch geometry is

\[
V(q;\Delta)
=A\left(-\Delta q+\frac{C}{3}q^3\right)+\cdots,
\qquad
\Delta:=\epsilon_f-\epsilon,
\]

with unknown positive projection normalization `A`.

On the stable branch

\[
q=+\sqrt{\Delta/C},
\]

and therefore

\[
\boxed{
k_{\rm soft}=V_{qq}\sim2A\sqrt{C\Delta}.}
\]

The soft static eigenvalue therefore scales as `Delta^(1/2)`, not linearly in `Delta`, for this nondegenerate fold.

## Experiment 636 — Conservative critical slowing

For a positive effective kinetic mass `m_eff`,

\[
m_{\rm eff}\ddot q+k_{\rm soft}q=0
\]

gives

\[
\boxed{
\omega_{\rm soft}\propto\Delta^{1/4},
\qquad
\tau_{\rm osc}\propto\Delta^{-1/4}.
}
\]

The coefficient cannot be fixed from the static branch because `m_eff` and the projection normalization remain constitutive data.

## Experiment 637 — Fixed-damping critical slowing

For nonzero fixed effective damping `d_eff`, sufficiently close to the fold the slow mode is asymptotically overdamped:

\[
d_{\rm eff}\dot q+k_{\rm soft}q\simeq0.
\]

Hence

\[
\boxed{
|r_{\rm slow}|\propto\Delta^{1/2},
\qquad
\tau_{\rm relax}\propto\Delta^{-1/2}.
}
\]

The damping ratio grows as `Delta^(-1/4)`, so any fixed nonzero damping eventually dominates arbitrarily close to the static fold.

## Experiment 638 — Current dynamical status

The following chain now survives conditionally:

\[
\text{continuum static fold}
\to
\text{divergent static susceptibility}
\to
\text{soft dynamical mode}
\to
\text{critical slowing},
\]

provided a positive kinetic bridge is supplied.

However:

- the absolute time scale is not statically determined;
- `c_*`, `c_info`, `mu_A`, and damping remain distinct constitutive inputs;
- the determinant-one anisotropic field tensor needs propagation headroom (or an alternate conformal principal factor) to respect a finite `c_info` bound;
- the static exterior Robin condition must be replaced by a causal dynamic boundary law;
- a full time-dependent fold crossing still requires the exterior/support and kinetic choices above;
- none of these results proves a horizon or black-hole endpoint.

## Next audit target

Construct the minimal causal time-dependent reciprocal radial model using

\[
U_\tau+U-1+p(a_b)U_s=0
\]

at the field boundary, choose an explicitly bounded axis kinetic sector satisfying the characteristic inequalities, then test slow parameter ramps through the continuum fold. Separate quasi-static tracking, critical delay, inertial overshoot, axis saturation, and post-fold departure.
