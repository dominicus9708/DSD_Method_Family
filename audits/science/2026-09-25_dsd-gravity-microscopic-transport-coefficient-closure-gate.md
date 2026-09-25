# BH-RB-027 — microscopic transport-coefficient closure gate

Date: 2026-09-25

## Purpose

BH-RB-026 resolved the free asymptotic heat-flux driver into thermodynamic quantities but still left \(\kappa\) and \(\tau_q\) as independently supplied transport data.

BH-RB-027 moves one level upstream and asks whether one microscopic collision model can generate both quantities at once, while remaining compatible with the previously established trapped-shell flux gates.

This is a **synthetic kinetic-theory control**, not a derivation of the black-hole successor phase.

## External kinetic-theory comparators

Relativistic Boltzmann theory can derive both transport coefficients and relaxation times from the same collision operator rather than assigning them independently.

- K. Tsumura, Y. Kikuchi, T. Kunihiro, *Relativistic causal hydrodynamics derived from Boltzmann equation: A novel reduction theoretical approach*, Phys. Rev. D 92, 085048 (2015), DOI 10.1103/PhysRevD.92.085048.
- V. E. Ambruș, *Transport coefficients in ultrarelativistic kinetic theory*, Phys. Rev. C 97, 024914 (2018), DOI 10.1103/PhysRevC.97.024914. In the Anderson–Witting RTA control, the heat-flux relaxation time and shear relaxation time are equal to the kinetic relaxation time.
- G. S. Denicol et al., *Derivation of transient relativistic fluid dynamics from the Boltzmann equation*, Phys. Rev. D 85, 114047 (2012), DOI 10.1103/PhysRevD.85.114047.

These papers justify the **provenance strategy** that transport coefficients and relaxation times should come from one collision theory. They do not identify black-hole successor matter with a dilute gas.

## Minimal one-scale kinetic closure

Use \(c=k_B=G=1\).

For an isotropic kinetic control,

\[
\tau_{\rm coll}^{-1}\sim n\sigma_{\rm tr}v,
\qquad
\lambda_{\rm mfp}=v\tau_{\rm coll}.
\]

Use the standard kinetic estimate

\[
\kappa
\sim
\frac13 c_Vv^2\tau_{\rm coll},
\]

and write the heat-flux relaxation time as

\[
\tau_q=\chi\tau_{\rm coll}.
\]

For the Anderson–Witting RTA comparator,

\[
\chi=1.
\]

Define

\[
\beta_T
=
\frac{c_VT}{\varepsilon+p}.
\]

Then the BH-RB-026 stability parameter becomes

\[
\boxed{
\alpha_{\rm micro}
=
\frac{\kappa T}{\tau_q(\varepsilon+p)}
=
\frac{\beta_Tv^2}{3\chi}.
}
\]

The microscopic collision time cancels.

Therefore making collisions faster does **not** independently tune \(\alpha\): the same collision scale changes \(\kappa\) and \(\tau_q\) together.

## Force-scale Knudsen variable

BH-RB-026 used

\[
\Theta
=
-R\left(\partial_{\hat r}\ln T+a_{\hat r}\right).
\]

Define

\[
\boxed{
K_F
=
\frac{v\tau_{\rm coll}}{R}|\Theta|.
}
\]

If the temperature-gradient term dominates,

\[
K_F
=
\frac{\lambda_{\rm mfp}}{L_T},
\qquad
L_T
=
\left|\partial_{\hat r}\ln T\right|^{-1},
\]

so \(K_F\) is the ordinary thermal Knudsen number.

If the acceleration term dominates, \(K_F\) is only a **force-scale nonequilibrium proxy** and must not be overinterpreted as a literal mean-free-path / temperature-gradient-length ratio.

The normalized asymptotic heat driver is

\[
Q_{\rm drive}
=
8\pi R^2q_{\rm drive}.
\]

Using the kinetic closure,

\[
\boxed{
\frac{Q_{\rm drive}}{E+P}
=
\frac{\beta_Tv}{3}K_F.
}
\]

Thus the required force-scale nonequilibrium is

\[
\boxed{
K_{F,\rm crit}
=
\frac{3Q_{\rm crit}}
{(E+P)\beta_Tv}.
}
\]

The NEC amplitude ceiling corresponds to

\[
\boxed{
K_{F,\rm NEC}
=
\frac{3Q_{\rm NEC}}
{(E+P)\beta_Tv}.
}
\]

## Ultrarelativistic Boltzmann comparator

For a classical ultrarelativistic gas,

\[
\varepsilon=3nT,
\qquad
p=nT,
\qquad
c_V=3n,
\]

so

\[
\boxed{
\beta_T=\frac34.
}
\]

With \(v=1\) and \(\chi=1\),

\[
\boxed{
\alpha_{\rm micro}
=
\frac14.
}
\]

This is substantially below the free synthetic \(\alpha=0.8\) witness used in BH-RB-026.

## BH-RB-024/025 fast-shell control

Retain the same synthetic shell:

\[
\mathcal C=1.2,
\qquad
V=0.8,
\]

\[
E=3.6,
\qquad
P\simeq0.236714343,
\]

\[
Q_{\rm crit}
\simeq1.732742693,
\qquad
Q_{\rm NEC}
\simeq1.918357171.
\]

The ultrarelativistic one-scale kinetic control gives

\[
\boxed{
K_{F,\rm crit}
\simeq1.806486007,
}
\]

and

\[
\boxed{
K_{F,\rm NEC}=2.
}
\]

Therefore the formal amplitude + NEC window is

\[
1.806486007
<
K_F
\le2.
\]

But this entire interval satisfies

\[
K_F>1.
\]

Hence it lies outside the near-equilibrium kinetic/hydrodynamic regime in which the truncated conductivity closure is supposed to be reliable.

This is the central BH-RB-027 result:

\[
\boxed{
\text{the simple one-scale near-equilibrium kinetic heat channel
does not close the required flux gate in this synthetic trapped shell.}
}
\]

## Explicit small-K controls

For the same comparator,

\[
K_F=0.1
\quad\Rightarrow\quad
Q_{\rm drive}\simeq0.095918,
\]

\[
K_F=0.3
\quad\Rightarrow\quad
Q_{\rm drive}\simeq0.287754,
\]

\[
K_F=1
\quad\Rightarrow\quad
Q_{\rm drive}\simeq0.959179.
\]

All remain below

\[
Q_{\rm crit}\simeq1.732743.
\]

## Thermodynamic-efficiency gate

For a declared upper nonequilibrium scale \(K_{\max}\), the minimum thermodynamic ratio required to reach the flux gate is

\[
\boxed{
\beta_T^{\rm req}
=
\frac{3Q_{\rm crit}}
{(E+P)vK_{\max}}.
}
\]

For \(v=1\),

\[
K_{\max}=1
\quad\Rightarrow\quad
\beta_T^{\rm req}\simeq1.354865,
\]

\[
K_{\max}=0.3
\quad\Rightarrow\quad
\beta_T^{\rm req}\simeq4.516215,
\]

\[
K_{\max}=0.1
\quad\Rightarrow\quad
\beta_T^{\rm req}\simeq13.548645.
\]

The ultrarelativistic Boltzmann comparator has only

\[
\beta_T=0.75.
\]

This does **not** prove that all successor phases fail. It creates a new microscopic requirement:

\[
\boxed{
\frac{c_VT}{\varepsilon+p}
}
\]

must be large enough, or another transport channel / nonhydrodynamic regime must participate.

## Cross-section provenance

With dimensionless

\[
\hat n=nR^3,
\qquad
\hat\sigma=\sigma_{\rm tr}/R^2,
\]

the one-scale collision model gives

\[
\frac{\tau_{\rm coll}}{R}
=
\frac{1}{\hat n\hat\sigma v},
\]

\[
\frac{\lambda_{\rm mfp}}{R}
=
\frac{1}{\hat n\hat\sigma}.
\]

Therefore, in the gradient-dominated case,

\[
K_F
=
\frac{|\Theta|}{\hat n\hat\sigma}.
\]

This exposes a direct tradeoff: increasing mean free path increases \(\kappa\), but also increases \(K_F\) and worsens hydrodynamic control.

The required heat flux cannot be made arbitrarily large by simply weakening collisions while still claiming the same near-equilibrium fluid closure.

## Slow branch remains excluded

For the \(V=0.5\) comparator,

\[
Q_{\rm crit}\simeq3.212591
>
Q_{\rm NEC}\simeq1.918357.
\]

Correspondingly,

\[
K_{F,\rm crit}\simeq3.349315
>
K_{F,\rm NEC}=2.
\]

No microscopic refinement of this same radial heat channel can repair the NEC amplitude failure of that synthetic branch.

## Interpretation for the black-hole-core program

BH-RB-027 is a **negative narrowing result**, not a failure of the overall finite-3D-support program.

It shows that the sequence

\[
\text{ordinary near-equilibrium single-scale heat conduction}
\rightarrow
Q_{\rm drive}
\rightarrow
D_T\mathcal C<0
\]

is insufficient for the current fast trapped-shell control when represented by the ultrarelativistic Boltzmann/RTA comparator.

The remaining open routes include strong nonequilibrium kinetic evolution; anisotropic stress, viscosity, diffusion, and multi-component transport; formation change in which the effective transport carrier itself changes; and a successor phase with a substantially different \(\beta_T\), collision kernel, or nonlocal response.

None of these are yet derived.

## DSD audit role

DSD is useful here as a provenance firewall.

The same successor formation must specify, or explicitly bridge to:

- the carrier degrees of freedom,
- interaction / transport cross section,
- collision and relaxation times,
- heat capacity and enthalpy,
- conductivity,
- EOS,
- allowed transport channels,
- lineage across phase or formation changes.

It is no longer acceptable to choose an EOS from one microphysics and independently tune \(\kappa\) or \(\tau_q\) to rescue the collapse dynamics.

## Python audit

Result:

\[
\boxed{29/29\ {\rm PASS}}
\]

Verdict:

PASS_WITH_BOUNDARY / SAME_MICROSCOPIC_COLLISION_SCALE_CAN_CLOSE_KAPPA_AND_TAUQ_IN_KINETIC_CONTROL / RTA_ULTRARELATIVISTIC_CONTROL_GIVES_ALPHA_MICRO_1_OVER_4 / FAST_SHELL_QCRIT_REQUIRES_FORCE_KNUDSEN_GREATER_THAN_UNITY_FOR_BETA_3_OVER_4 / NEAR_EQUILIBRIUM_SINGLE_SCALE_HEAT_CONDUCTION_DOES_NOT_CLOSE_THE_REQUIRED_FLUX_GATE_IN_THIS_CONTROL / STRONG_NONEQUILIBRIUM_OR_OTHER_TRANSPORT_CHANNELS_REMAIN_OPEN / SUCCESSOR_MICROPHYSICS_AND_PERSISTENT_3D_CORE_NOT_DERIVED

## Next mainline target — BH-RB-028

The next audit should not merely increase the heat conductivity.

It should test whether the missing support can be supplied by **additional causal transport channels** while preserving one microscopic provenance:

\[
\text{heat flux}
+
\text{radial/tangential stress anisotropy}
+
\text{viscous transport}
+
\text{particle/diffusion flux}
+
\text{formation transition}.
\]

The first useful gate is to determine which term can reduce the required radial heat-flux burden without violating energy conditions or silently inserting an independent free coefficient.

If every near-equilibrium channel still requires \(K\gtrsim1\), the mainline should explicitly leave hydrodynamics and move to a kinetic/nonhydrodynamic successor-state evolution rather than continue tuning fluid coefficients.
