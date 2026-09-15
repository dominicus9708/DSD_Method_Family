# BH-RB-023 — trapped self-bound dynamic no-go gate

## Status

**PASS_WITH_BOUNDARY / SPHERICAL_POSITIVE_PRESSURE_SELF_BOUND_NO_FLUX_BRANCH_CLOSED / TRAPPED_COMPACTNESS_DEEPENS_DURING_COLLAPSE / FINITE_RADIUS_STALL_OR_BOUNCE_NOT_AVAILABLE_AFTER_STRICT_TRAPPING / EXTRA_TRANSPORT_OR_NONPERFECT_STRESS_REQUIRED / FINITE_CORE_RADIUS_NOT_DERIVED**

This audit continues BH-RB-021.  The globally causal self-bound EOS family remains admissible as an EOS envelope, but this audit asks the next dynamical question: can a spherically symmetric, comoving, no-flux, nonnegative-radial-pressure successor fluid use that EOS by itself to stop at a positive radius after it is already strictly trapped?

The answer for this restricted branch is **no**.

## Provenance firewall

The equations below are standard GR/Misner-Sharp relations used as **R4 external physical dynamics**, not DSD-native derivations.

The active DSD contribution remains the separation of formation/property/state/lineage, the explicit constitutive bridge requirement, and the refusal to identify a typed DSD property with a physical stress-energy component before that bridge is supplied.

This result does **not** prove that every black-hole interior reaches a literal zero-dimensional material object, and it does **not** exclude rotating, dissipative, anisotropic, negative-radial-pressure, phase-changing, or otherwise non-perfect-fluid successor branches.

## Spherical dynamical control

Use geometrized units \(G=c=1\), areal radius \(R\), Misner-Sharp mass \(m\), comoving areal-radius rate

\[
U=D_T R,
\]

and

\[
\Gamma^2=1+U^2-\frac{2m}{R}.
\]

Define compactness

\[
\mathcal C=\frac{2m}{R}.
\]

For the collapsing branch, \(U<0\).  A strictly trapped spherical shell satisfies

\[
\mathcal C>1.
\]

The Misner-Sharp constraint therefore gives

\[
U^2\ge \mathcal C-1.
\]

Hence if the shell remains separated from marginal trapping by

\[
\mathcal C\ge \mathcal C_0>1,
\]

then

\[
|U|\ge \sqrt{\mathcal C_0-1}>0.
\]

This \(U\) is an areal-radius derivative along the comoving shell, not a local special-relativistic 3-speed.

## Turning-point gate

At a genuine spherical turning point,

\[
U=0.
\]

Then

\[
\Gamma^2=1-\mathcal C\ge0,
\]

so necessarily

\[
\boxed{\mathcal C\le1.}
\]

Therefore

\[
\boxed{\mathcal C>1\ \Rightarrow\ U\neq0}
\]

within the same regular spherical Misner-Sharp branch.

Thus a strictly trapped shell cannot simply stop and reverse at the same event while retaining \(\mathcal C>1\).

## Perfect-fluid mass-work equation

For a spherical comoving fluid with no outward heat flux,

\[
D_Tm=-4\pi p_r U R^2.
\]

For collapse \(U<0\) and nonnegative radial pressure \(p_r\ge0\),

\[
D_Tm\ge0.
\]

This has a direct compactness consequence.  Differentiating

\[
\mathcal C=\frac{2m}{R}
\]

gives

\[
D_T\mathcal C
=
-8\pi p_rUR
-
\frac{\mathcal C U}{R}.
\]

Therefore for

\[
U<0,\qquad p_r\ge0,\qquad \mathcal C>0,
\]

one has

\[
\boxed{D_T\mathcal C>0.}
\]

This is stronger than the turning-point statement: the positive-pressure, no-flux collapse does not merely fail to untrap; its spherical compactness moves **deeper into the trapped regime**.

## Consequence for BH-RB-021 self-bound EOS

The physical self-bound EOS branch constructed in BH-RB-021 has a zero-pressure surface at \(\varepsilon_0>0\), and above that surface its causal CSS completion has

\[
p\ge0,
\qquad
0\le\frac{dp}{d\varepsilon}\le1.
\]

Therefore this EOS, when inserted as an isotropic/nonnegative-radial-pressure no-flux spherical fluid, falls directly into the monotonic compactness gate above.

Hence

\[
\boxed{
\text{globally causal self-bound EOS}
\not\Rightarrow
\text{finite trapped-core radius}.
}
\]

The EOS solves the constitutive-scale problem but not the post-trapping dynamical escape problem.

## No positive-radius asymptote under a persistent trapped gap

Suppose after some proper-time value the shell obeys

\[
\mathcal C\ge \mathcal C_0>1.
\]

Then

\[
U\le-\sqrt{\mathcal C_0-1}.
\]

For any lower target radius \(R_1<R_0\),

\[
\Delta\tau
\le
\frac{R_0-R_1}{\sqrt{\mathcal C_0-1}}.
\]

Thus a smooth trajectory cannot approach a positive asymptotic radius while remaining in a branch with compactness bounded away from unity.

A positive-radius asymptote would require at least

\[
U\to0,
\]

and therefore, from the Misner-Sharp relation, loss of the persistent strict trapped gap.  In particular one needs a route toward marginality \(\mathcal C\to1\), or a breakdown of the assumptions used here.

But the positive-pressure/no-flux perfect-fluid branch has

\[
D_T\mathcal C>0,
\]

so it cannot provide that route by itself once \(\mathcal C>1\).

## Explicit escape channels

For the more general spherical balance with outward energy flux \(q\),

\[
D_Tm
=
-4\pi R^2(p_rU+q\Gamma).
\]

Then

\[
D_T\mathcal C
=
-8\pi R(p_rU+q\Gamma)
-
\frac{\mathcal C U}{R}.
\]

For \(U<0\), the threshold for non-increasing compactness is

\[
q\Gamma
\ge
|U|
\left(
 p_r+
 \frac{\mathcal C}{8\pi R^2}
\right).
\]

Therefore a sufficiently large outward flux is one explicit route unavailable to the BH-RB-021 no-flux control.

If \(q=0\), the same algebra shows that compactness non-growth requires

\[
p_r
\le
-\frac{\mathcal C}{8\pi R^2},
\]

namely sufficiently negative radial pressure/tension.

These are **necessary algebraic channels within the same spherical balance law**, not claims that a realistic successor core actually realizes them.

Other open branches include non-spherical rotation, anisotropic transport, phase-change energy transport, magnetic/field stresses, and more general successor stress-energy closures.

## Synthetic control

For a dimensionless trapped shell with

\[
\mathcal C_0=1.05,
\]

the kinematic lower bound is

\[
|U|\ge\sqrt{0.05}\approx0.2236068.
\]

Therefore contraction from \(R=1\) to \(R=0.5\), while the strict trapped gap persists, obeys

\[
\Delta\tau\le
\frac{0.5}{\sqrt{0.05}}
\approx2.23607
\]

in the geometrized control units.

This is not a physical prediction for a specific black hole; it is a consistency control for the inequality.

## Result

The Python audit reports

\[
\boxed{15/15\ \mathrm{PASS}}.
\]

The correct conclusion is

\[
\boxed{
\text{positive-pressure self-binding}
+
\text{spherical no-flux GR collapse}
\not\Rightarrow
R_{\min}>0
\text{ after strict trapping}.
}
\]

More strongly, within this branch the trapped compactness increases during collapse, so a finite-radius stall, bounce, or positive-radius asymptote is not supplied by the EOS alone.

This does **not** eliminate the finite successor-core research branch.  It identifies what that branch must add beyond BH-RB-021: a mechanism that changes the compactness evolution, such as outward energy transport, sufficiently negative radial stress, or a non-spherical/non-perfect-fluid successor closure.

## Next gate

BH-RB-024 should therefore stop trying to obtain \(R_{\min}\) from positive-pressure EOS stiffness alone and audit the **minimal compactness-reversal mechanism**.

The primary comparison branches are:

1. outward energy/enthalpy flux sufficient to reduce \(m/R\),
2. negative radial pressure/tension compatible with the chosen quantum closure,
3. rotating/non-spherical transport where the spherical Misner-Sharp no-go no longer directly applies,
4. phase-transition/re-formation dynamics that changes the stress-energy carrier itself.

The goal is to determine whether any branch can generate

\[
D_T\mathcal C\le0
\]

without inserting \(R_{\min}\) by hand and without violating the declared causal/energy-condition boundary unintentionally.

## External standard-GR references

- Misner-Sharp spherical mass relation and areal velocity control: see modern summaries in Herrera et al., *Quasi-homologous evolution of self-gravitating systems with vanishing complexity factor*, Eur. Phys. J. C 80 (2020), especially the displayed Misner-Sharp mass and \(\Gamma^2=1+U^2-2m/R\) relation.
- A modern spherical-fluid presentation with heat flux gives \(D_Tm=-4\pi[(P_r)U+qE]R^2\): *Stability of evolving cluster of stars and exotic matter*, Eur. Phys. J. C (2024).

These equations are used only as external GR comparators/dynamics under the project provenance firewall.
