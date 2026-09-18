# BH-RB-026 — explicit thermodynamic driver provenance gate

Date: 2026-09-19

## Purpose

BH-RB-025 showed that a finite-relaxation transport law adds both an amplitude gate and a response-time gate. BH-RB-026 moves one step upstream and asks whether the asymptotic transport driver itself can be written in explicit thermodynamic variables rather than inserted as a free constant.

This audit remains a synthetic relativistic transport control. It does not derive a physical black-hole successor-core microphysics.

## External relativistic transport comparator

Herrera & Santos (2004), *Dynamics of dissipative gravitational collapse*, couple Misner-Sharp collapse dynamics to Müller-Israel-Stewart causal heat transport. Their full transport equation contains

\[
\tau h^{\alpha\beta}V^\gamma q_{\beta;\gamma}+q^\alpha
=
-\kappa h^{\alpha\beta}(T_{,\beta}+Ta_\beta)
-\frac12\kappa T^2
\left(\frac{\tau V^\beta}{\kappa T^2}\right)_{;\beta}q^\alpha.
\]

The present audit uses only the minimal truncated radial control

\[
\tau D_T q+q
=
-\kappa\left(\partial_{\hat r}T+Ta_{\hat r}\right).
\]

Reference: https://arxiv.org/abs/gr-qc/0410014

The same source also gives linear causality/stability inequalities stronger than

\[
\tau>\frac{\kappa T}{\varepsilon+p}.
\]

Therefore

\[
\alpha
=
\frac{\kappa T}{\tau(\varepsilon+p)}
<1
\]

is used here only as a necessary synthetic gate, not as a sufficient full Israel-Stewart stability theorem.

## Dimensionless driver decomposition

Continue the BH-RB-024 normalization in geometrized units:

\[
\mathcal C=\frac{2m}{R},\qquad
E=8\pi\rho R^2,\qquad
P=8\pi p_rR^2,\qquad
Q=8\pi qR^2.
\]

Define

\[
\Theta=-R\left(\partial_{\hat r}\ln T+a_{\hat r}\right)
\]

and

\[
\Xi=8\pi R\kappa T.
\]

Then the asymptotic radial thermal driver becomes

\[
\boxed{Q_{\rm drive}=\Xi\Theta.}
\]

For

\[
\hat\tau=\frac{\tau}{R},
\]

the necessary linear gate becomes

\[
\boxed{\alpha=\frac{\Xi}{\hat\tau(E+P)}.}
\]

Hence, for fixed \(\alpha,\Theta\),

\[
Q_{\rm drive}=\alpha\hat\tau(E+P)\Theta.
\]

## Equilibrium firewall

In the static Tolman-like equilibrium limit, the temperature gradient and acceleration term cancel in the minimal heat law,

\[
\partial_{\hat r}\ln T+a_{\hat r}=0,
\]

so

\[
\Theta=0,\qquad Q_{\rm drive}=0.
\]

Therefore strong gravity by itself does not imply an outward heat flux. A non-equilibrium thermodynamic force is required.

This is used only as an equilibrium comparator. A dynamical anisotropic successor phase need not satisfy the simple scalar Tolman law.

## Coupled amplitude / relaxation / NEC window

BH-RB-024 requires

\[
Q_{\rm drive}>Q_{\rm crit}
\]

for the asymptotic flux to be capable of making compactness nonincreasing, while the radial NEC necessary bound gives

\[
Q_{\rm drive}\le Q_{\rm NEC}.
\]

With

\[
Q_{\rm drive}=\alpha\hat\tau(E+P)\Theta,
\]

a finite interval exists only if

\[
\boxed{
\frac{Q_{\rm crit}}{\alpha(E+P)\Theta}
<\hat\tau\le
\frac{Q_{\rm NEC}}{\alpha(E+P)\Theta}.
}
\]

Thus the relaxation time cannot simply be sent to zero while holding all thermodynamic transport data fixed. Once the conductivity/temperature scale and linear causal-stability provenance are tracked, response speed and achievable driver amplitude become coupled.

## Synthetic fast-branch witness

Use the same BH-RB-024/025 control:

\[
\mathcal C=1.2,\qquad V=0.8,
\]

with

\[
E=3.6,\qquad P\simeq0.236714343,
\]

\[
Q_{\rm crit}\simeq1.732742693,\qquad Q_{\rm NEC}\simeq1.918357171.
\]

Choose only as a synthetic witness

\[
\alpha=0.8,\qquad \Theta=1,\qquad \hat\tau=0.6.
\]

Then

\[
\Xi=\alpha\hat\tau(E+P)\simeq1.841622885,
\]

and

\[
\boxed{Q_{\rm drive}\simeq1.841622885.}
\]

Therefore

\[
Q_{\rm crit}<Q_{\rm drive}<Q_{\rm NEC}.
\]

The allowed interval is

\[
\boxed{0.564526877<\hat\tau\le0.625.}
\]

For the chosen point,

\[
\frac{t_{\rm cross}}{\tau}
=-\ln\left(1-\frac{Q_{\rm crit}}{Q_{\rm drive}}\right)
\simeq2.828154348,
\]

so

\[
\frac{t_{\rm cross}}{R}\simeq1.696892609.
\]

This is only an existence witness in parameter space.

## Slow-branch exclusion remains

For the BH-RB-024 slow control,

\[
V=0.5,
\]

\[
Q_{\rm crit}\simeq3.212590935>Q_{\rm NEC}\simeq1.918357171.
\]

Therefore no choice of thermodynamic driver that respects the same radial NEC necessary bound can close the amplitude gate in that branch.

## Chemical-potential provenance correction

The minimal heat-conduction law used here contains \(\nabla T+Ta\) and does not automatically contain a chemical-potential gradient.

A term involving \(\nabla\mu\) requires an explicit particle-diffusion law, frame choice, or a more general multi-component transport theory. It is therefore not inserted into \(Q_{\rm drive}\) at this stage.

## Interpretation

BH-RB-026 narrows the unknown upstream data from a free \(Q_{\rm drive}\) to

\[
\boxed{\kappa,\quad T,\quad\nabla T,\quad a^\mu,\quad\tau_q}
\]

plus the declared transport theory and frame.

The central new result is that transport amplitude and relaxation timescale are not independent free knobs once causal-stability provenance is tracked.

The result does not derive the black-hole core transport coefficients or a persistent finite 3D support.

## DSD audit role

DSD contributes the provenance questions: which formation carries temperature, conductivity and relaxation-time properties; under what prerequisites they are defined; whether coefficients survive a phase transition; whether a change in driver is a property, transport, or formation transition; and whether a heat-flux lineage is a real causal transport lineage or only a descriptor-level change.

DSD does not supply numerical \(\kappa,T,\tau_q\) values without a microscopic bridge.

## Python audit

Result: 23/23 PASS.

Verdict: PASS_WITH_BOUNDARY / THERMAL_FORCE_AND_CONDUCTIVITY_PROVENANCE_RESOLVE_QDRIVE_IN_MINIMAL_CAUSAL_CONTROL / TOLMAN_LIKE_EQUILIBRIUM_DOES_NOT_DRIVE_OUTWARD_HEAT_FLUX / FAST_SYNTHETIC_BRANCH_HAS_A_NARROW_ALPHA_TAU_THERMAL_FORCE_WINDOW_BETWEEN_QCRIT_AND_NEC / ARBITRARILY_SMALL_RELAXATION_TIME_IS_NOT_FREE_ONCE_CAUSAL_STABILITY_CONSTRAINTS_ARE_TRACKED / MICROPHYSICAL_KAPPA_TEMPERATURE_PROFILE_AND_FULL_TRANSPORT_LAW_NOT_DERIVED / PERSISTENT_3D_BLACK_HOLE_CORE_NOT_DERIVED

## Next mainline target — BH-RB-027

The next gate should stop treating \(\kappa,\tau_q,T(r),\partial_rT\) as independent synthetic inputs and ask whether a specified microscopic successor phase can produce them consistently.

A minimal target chain is

\[
\text{quantum/statistical carrier}
\rightarrow
\text{mean free path / scattering rate}
\rightarrow
\kappa,\tau_q
\rightarrow
Q_{\rm drive}
\rightarrow
Q(t)
\rightarrow
D_T\mathcal C.
\]

The key question is whether one microscopic closure can satisfy the EOS, causality, energy-condition, and transport-timescale gates simultaneously without fitting a desired core radius.
