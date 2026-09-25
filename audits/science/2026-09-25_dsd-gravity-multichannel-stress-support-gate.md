# BH-RB-028 — multi-channel causal transport / stress-support gate

Date: 2026-09-25

## Purpose

BH-RB-027 showed that the one-scale ultrarelativistic Boltzmann/RTA heat channel requires

\[
K_{F,\rm crit}\simeq1.806>1
\]

in the current fast trapped-shell control. Therefore simply increasing the heat conductivity is not a controlled near-equilibrium solution.

BH-RB-028 asks whether a second channel — anisotropic stress — can reduce the required radial heat-flux burden before abandoning hydrodynamics entirely.

The calculation is a frozen-shell algebraic control. It is **not** a global collapse solution and does not prove a persistent finite three-dimensional black-hole core.

## External GR comparators

Spherically symmetric dissipative anisotropic fluids are standard general-relativistic systems, and their dynamical equations contain distinct radial pressure, tangential pressure, heat flux, shear, and bulk-viscous sectors.

Relevant comparators:

- L. Herrera, A. Di Prisco, J. Martin, J. Ospino, N. O. Santos, O. Troconis, *Spherically symmetric dissipative anisotropic fluids: A general study*, Phys. Rev. D 69, 084026 (2004), arXiv:gr-qc/0403006.
- L. Herrera, N. O. Santos, *Dynamics of dissipative gravitational collapse*, Phys. Rev. D 70, 084004 (2004), arXiv:gr-qc/0410014.
- L. Herrera, A. Di Prisco, E. Fuenmayor, O. Troconis, *Dynamics of viscous dissipative gravitational collapse: A full causal approach*, Phys. Rev. D 79, 064025 (2009), arXiv:0804.3584.

These references justify separating heat, anisotropic stress, shear viscosity, and bulk viscosity. They do not supply the successor-core microphysics.

## Frozen-shell compactness equation

Continue the exact Misner-Sharp mass-balance structure already used in BH-RB-024:

\[
R D_T\mathcal C
=
V(\mathcal C+P_r)-Q\Gamma,
\]

where

\[
\Gamma^2=1+V^2-\mathcal C,
\qquad
V=-U>0,
\]

and

\[
E=8\pi\rho R^2,
\qquad
P_r=8\pi p_rR^2,
\qquad
P_t=8\pi p_tR^2,
\qquad
Q=8\pi qR^2.
\]

The radial heat-flux threshold is

\[
\boxed{
Q_{\rm crit}
=
\frac{V(\mathcal C+P_r)}{\Gamma}.
}
\]

The radial NEC necessary bound is

\[
\boxed{
Q_{\rm NEC}
=
\frac{E+P_r}{2}.
}
\]

Tangential pressure does not enter this mass-balance equation directly. Its role in this audit is to permit a change in \(P_r\) at fixed mean pressure.

## Fixed-mean-pressure anisotropy split

Let the EOS supply a mean pressure

\[
\bar P
=
\frac{P_r+2P_t}{3}.
\]

Define positive tangential anisotropy

\[
\Delta=P_t-P_r.
\]

Then

\[
\boxed{
P_r=\bar P-\frac{2}{3}\Delta,
\qquad
P_t=\bar P+\frac{1}{3}\Delta.
}
\]

Thus \(\Delta>0\) lowers the radial pressure while preserving the mean pressure.

For the BH-RB-024/025/027 fast shell,

\[
\mathcal C=1.2,
\qquad
V=0.8,
\qquad
E=3.6,
\]

and the previous EOS sample gives

\[
\bar P\simeq0.236714343.
\]

The isotropic thresholds are

\[
Q_{\rm crit}^{\rm iso}
\simeq1.732742693,
\]

\[
Q_{\rm NEC}^{\rm iso}
\simeq1.918357171.
\]

## Coupling to the BH-RB-027 heat channel

For the one-scale ultrarelativistic kinetic control,

\[
\frac{Q_{\rm heat,max}}{E+P_r}
=
h
=
\frac{\beta_TvK_{\max}}{3},
\]

with

\[
\beta_T=\frac34,
\qquad
v=1.
\]

To make the heat channel just close the compactness gate,

\[
h(E+P_r)
=
\frac{V}{\Gamma}(\mathcal C+P_r).
\]

For \(V/\Gamma>h\), the limiting radial pressure is

\[
\boxed{
P_r^\star
=
\frac{
hE-\frac{V}{\Gamma}\mathcal C
}{
\frac{V}{\Gamma}-h
}.
}
\]

Any

\[
P_r\le P_r^\star
\]

reduces the required heat-flux burden enough for the declared \(K_{\max}\).

## Witness A — \(K_{\max}=1\)

For

\[
K_{\max}=1,
\qquad
h=0.25,
\]

the required stress split is

\[
\boxed{
P_r^\star\simeq-0.572414727,
}
\]

\[
\boxed{
P_t\simeq0.641278878,
}
\]

\[
\boxed{
\Delta\simeq1.213693604.
}
\]

The required heat flux falls to

\[
\boxed{
Q_{\rm crit}\simeq0.756896318,
}
\]

while

\[
Q_{\rm NEC}\simeq1.513792637.
\]

Thus the same \(K_F\le1\) heat channel that failed in the isotropic control can close the **algebraic** compactness gate if the radial sector becomes sufficiently tensile and the tangential sector carries the compensating stress.

## Stronger near-equilibrium heat limits

For

\[
K_{\max}=0.3,
\]

the equality witness is

\[
P_r^\star\simeq-1.040855192,
\]

\[
P_t\simeq0.875499110,
\]

\[
\Delta\simeq1.916354302,
\]

\[
Q_{\rm crit}\simeq0.191935861.
\]

For

\[
K_{\max}=0.1,
\]

the equality witness is

\[
P_r^\star\simeq-1.149197549,
\]

\[
P_t\simeq0.929670289,
\]

\[
\Delta\simeq2.078867838,
\]

\[
Q_{\rm crit}\simeq0.061270061.
\]

Therefore algebraically even a small heat channel can be sufficient if a large enough positive tangential anisotropy lowers \(P_r\).

This does **not** show that such anisotropy can actually be generated causally.

## Energy-condition check of the witnesses

In the local orthonormal radial block,

\[
T_{\hat a\hat b}
=
\begin{pmatrix}
E & Q\\
Q & P_r
\end{pmatrix}.
\]

The type-I discriminant is

\[
D
=
(E+P_r)^2-4Q^2.
\]

All three witnesses have

\[
D>0.
\]

In the radial eigenframe,

\[
\rho_0
=
\frac{E-P_r+\sqrt D}{2},
\]

\[
p_{r0}
=
\frac{P_r-E+\sqrt D}{2}.
\]

The Python audit verifies for all three witnesses

\[
\rho_0>0,
\]

\[
\rho_0\ge|p_{r0}|,
\]

\[
\rho_0\ge|P_t|.
\]

Thus the witnesses are compatible with a type-I dominant-energy-condition check at this algebraic level.

This does not prove stability, causality of the shear constitutive law, or global regularity.

## Anisotropy magnitude

At fixed \(\bar P\), define only as a diagnostic

\[
\mathcal I_\pi
=
\frac{
\max(
|P_r-\bar P|,
|P_t-\bar P|
)
}{
E+\bar P
}.
\]

The three witnesses give approximately

\[
\mathcal I_\pi(K=1)\simeq0.211,
\]

\[
\mathcal I_\pi(K=0.3)\simeq0.333,
\]

\[
\mathcal I_\pi(K=0.1)\simeq0.361.
\]

These values are finite but not parametrically tiny. Therefore this audit does not label the required anisotropy as safely near-equilibrium. A causal shear-stress closure is required next.

## Bulk-viscosity sign control

In an ordinary near-equilibrium compression,

\[
\Theta_{\rm exp}<0,
\qquad
\Pi_{\rm bulk}
=
-\zeta\Theta_{\rm exp}>0
\quad
(\zeta\ge0).
\]

A positive isotropic bulk-pressure shift increases \(P_r\).

For the present shell,

\[
\frac{Q_{\rm crit}}{Q_{\rm NEC}}
=
\frac{
2(V/\Gamma)(\mathcal C+P_r)
}{
E+P_r
}.
\]

Since

\[
E>\mathcal C,
\]

this ratio increases with \(P_r\).

The control confirms that a positive compressive bulk pressure therefore **worsens**, rather than relieves, this particular compactness/heat-flux feasibility gate.

This does not mean bulk viscosity is dynamically irrelevant. It means it is not the missing channel for this specific mass-balance bottleneck.

## Diffusion firewall

Particle or charge diffusion is not added as another independent energy-flux number.

In relativistic dissipative hydrodynamics, the decomposition of energy flux and particle diffusion depends on the hydrodynamic frame and on which conserved currents exist.

Therefore

\[
\boxed{
q^\mu
+
j_{\rm diff}^\mu
}
\]

cannot be treated as two freely additive copies of the same transport channel without a declared Landau/Eckart or multi-component closure.

## Formation-transition firewall

A DSD formation transition is also not an additive force term.

Instead it may change

\[
\text{EOS},
\quad
P_r,
\quad
P_t,
\quad
\eta,
\quad
\zeta,
\quad
\kappa,
\quad
\tau_i,
\]

because the successor carrier and its constitutive law have changed.

Thus formation change belongs upstream in the provenance tree.

## Main result

BH-RB-027 excluded ordinary near-equilibrium single-scale heat conduction as a sufficient channel in the current isotropic fast-shell control.

BH-RB-028 finds a nontrivial alternative:

\[
\boxed{
\text{positive tangential anisotropy}
\rightarrow
P_r\downarrow
\rightarrow
Q_{\rm crit}\downarrow
}
\]

and explicit type-I DEC-compatible algebraic witnesses exist for

\[
K_F\le1,
\]

including \(K_F=0.3\) and \(0.1\).

Therefore the next bottleneck is no longer simply heat conductivity.

It is

\[
\boxed{
\text{Can one microscopic successor phase causally generate the required anisotropic stress?}
}
\]

## Scope firewalls

- Negative \(P_r\) is radial **tension**, not ordinary pressure support.
- Tangential anisotropy does not directly replace heat flux in the Misner-Sharp mass equation; it acts here through the changed \(P_r\).
- The frozen-shell witness does not establish a same-shell trapped bounce.
- The witness does not derive \(\eta\), \(\tau_\pi\), or a shear rate.
- No finite-radius floor or persistent three-dimensional core is derived.

## Python audit

Result:

\[
\boxed{41/41\ {\rm PASS}}
\]

Verdict:

PASS_WITH_BOUNDARY / POSITIVE_TANGENTIAL_ANISOTROPY_CAN_REDUCE_RADIAL_HEAT_FLUX_BURDEN_IN_FROZEN_SHELL_CONTROL / ALGEBRAIC_TYPE_I_DEC_COMPATIBLE_WITNESSES_EXIST_EVEN_FOR_KF_LE_1 / COMPRESSIVE_BULK_VISCOUS_PRESSURE_DOES_NOT_HELP_THIS_COMPACTNESS_GATE / DIFFUSION_AND_FORMATION_CHANGE_REQUIRE_SEPARATE_PROVENANCE / CAUSAL_SHEAR_STRESS_GENERATION_NOT_DERIVED / PERSISTENT_3D_BLACK_HOLE_CORE_NOT_DERIVED

## Next mainline target — BH-RB-029

The next gate should derive the anisotropic stress dynamically rather than inserting \(P_r\) and \(P_t\).

Use a causal shear-stress structure of the form

\[
\tau_\pi D_T\pi_{\langle\mu\nu\rangle}
+
\pi_{\mu\nu}
=
2\eta\sigma_{\mu\nu}
+
\text{second-order couplings},
\]

with the same microscopic collision operator supplying

\[
\eta,
\qquad
\tau_\pi,
\qquad
\text{EOS},
\qquad
\kappa,
\qquad
\tau_q.
\]

The primary question is whether the required

\[
\Delta=P_t-P_r
\]

can be reached before collapse changes the local state, while maintaining causal/stable transport and without entering a regime where hydrodynamics itself loses validity.

If not, the mainline should move to a direct kinetic stress-tensor evolution rather than tuning fluid anisotropy by hand.
