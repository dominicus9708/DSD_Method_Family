# DSD Gravity Static-Stress Constitutive Branch Gate — BH-RB-008

Date: 2026-09-13

Status: **PASS_WITH_BOUNDARY / STATIC_ISOTROPIC_CONTROL_CLOSED / ANISOTROPIC_AND_DYNAMIC_BRANCHES_OPEN**

## Purpose

Continue BH-RB-007 without importing the discarded structural-gravity branch.

The finite-3D successor-core hypothesis remains a working hypothesis:

\[
\dim X_{\rm space}=3,
\qquad
\dim\operatorname{Supp}_{\rm core}=3,
\qquad
R_{\rm core}>0.
\]

Compression of a finite three-dimensional support is not identified with a reduction of ambient spatial dimension or DSD realized-axis rank.

The present audit asks what can already be ruled out or retained before inventing a new black-hole-core constitutive law.

## Provenance

The gravitational field equations and hydrostatic equations used below are **external standard GR comparators**. They are not derived from generic DSD.

DSD contributes only the provenance firewall: property names do not determine coefficients or operators, formation-level transitions are distinct from value evolution, and static-branch failure does not imply a dimensional collapse.

## External static control

Take the nonrotating, uncharged comparison branch

\[
J=0,
\qquad
Q=0,
\qquad
r_s=\frac{2GM}{c^2},
\qquad
\lambda=\frac{R}{r_s}.
\]

For the constant-density interior-Schwarzschild perfect-fluid control, the central pressure is

\[
\frac{p_c}{\varepsilon}
=
\frac{1-\sqrt{1-C}}
{3\sqrt{1-C}-1},
\qquad
C=\frac{r_s}{R}=\frac1\lambda,
\]

where \(\varepsilon=\rho c^2\).

This control is useful because its pressure singularity reproduces the Buchdahl threshold

\[
C=\frac89
\quad\Longleftrightarrow\quad
R=\frac98 r_s.
\]

It is **not** accepted as a physical candidate EOS for the proposed re-formed core: strict constant density is incompressible and therefore not a causal material model.

Reference for the standard TOV/Buchdahl framework:
- E. Chavez Nambo and O. Sarbach, *Static spherical perfect fluid stars with finite radius in general relativity: a review*, arXiv:2010.02859.

## Numerical control — Sgr A* mass scale

Using the already adopted external mass benchmark \(M=4.297\times10^6M_\odot\),

\[
r_s\simeq1.2690499\times10^7\ {\rm km}.
\]

Selected constant-density control values are:

| \(\lambda=R/r_s\) | \(R\) [km] | \(\bar\rho\) [kg m\(^{-3}\)] | \(p_c/\varepsilon\) | control status |
|---:|---:|---:|---:|---|
| 2.0 | \(2.53810\times10^7\) | \(1.2476\times10^5\) | 0.2612 | finite control |
| 1.5 | \(1.90357\times10^7\) | \(2.9572\times10^5\) | 0.5774 | finite control |
| 4/3 | \(1.69207\times10^7\) | \(4.2106\times10^5\) | 1.0000 | central DEC boundary in this control |
| 1.25 | \(1.58631\times10^7\) | \(5.1101\times10^5\) | 1.6180 | central DEC violated |
| 1.20 | \(1.52286\times10^7\) | \(5.7759\times10^5\) | 2.6330 | central DEC violated |
| 1.1251 | \(1.42781\times10^7\) | \(7.0079\times10^5\) | \(1.875\times10^3\) | near Buchdahl divergence |
| 9/8 | \(1.42768\times10^7\) | \(7.0097\times10^5\) | divergent | regular isotropic control closes |
| 1.0 | \(1.26905\times10^7\) | \(9.9807\times10^5\) | N/A | static horizonless-star control not applicable |

For this particular constant-density isotropic control,

\[
p_c=\varepsilon
\]

occurs at

\[
\lambda=\frac43.
\]

Thus the central dominant-energy-condition check fails before the Buchdahl pressure divergence is reached. This is a statement about the control model, not a universal theorem for every anisotropic or dynamical core.

## Anisotropic static branch

A general spherically symmetric anisotropic stress tensor is written as

\[
T^{\hat\mu}{}_{\hat\nu}
=
\operatorname{diag}(-\varepsilon,p_r,p_t,p_t).
\]

The external-GR generalized hydrostatic equation contains

\[
\frac{dp_r}{dr}
=
-\frac{G(\rho+p_r/c^2)\left(m+4\pi r^3p_r/c^2\right)}
{r^2\left(1-2Gm/(rc^2)\right)}
+
\frac{2(p_t-p_r)}{r}.
\]

Therefore \(M\) and \(R\) alone do not determine the configuration. A constitutive law for

\[
\Delta(r)=p_t(r)-p_r(r)
\]

or equivalent additional matter structure is required.

The audit script explicitly verifies that two states with the same local \(\rho\) and \(p_r\), but different \(\Delta\), have different required radial pressure gradients.

This is why anisotropy cannot be used as a free parameter merely to force a desired radius.

A relevant standard-GR compactness result is H. Andreasson, *Sharp bounds on 2m/r of general spherically symmetric static objects*, arXiv:gr-qc/0702137. It shows that compactness bounds depend on explicit inequalities imposed on radial and tangential pressures. Hence anisotropy relaxes the isotropic assumptions but does not remove the need for physical constitutive restrictions.

## Horizon boundary

The ordinary static stellar TOV control contains the factor

\[
1-\frac{2Gm(r)}{rc^2}.
\]

The present audit therefore does **not** extend the ordinary static horizonless-star control through \(R\le r_s\).

This does not prove that a finite three-dimensional successor core is impossible. It means only that the next stage for

\[
0<R_{\rm core}\le r_s
\]

must use a horizon-penetrating and genuinely dynamical formulation, or another explicitly justified non-static formulation.

## DSD interpretation

The following implications are rejected:

\[
\text{static isotropic branch fails}
\not\Rightarrow
\text{finite 3D support fails},
\]

\[
\text{finite 3D support fails in one constitutive model}
\not\Rightarrow
\text{ambient space becomes 0D},
\]

and

\[
\text{external point-like describability}
\not\Rightarrow
\text{zero-dimensional ontology}.
\]

The new re-formed-core branch remains open only if its stress-energy and transition law are stated explicitly.

## Audit result

Script result: **12/12 PASS**.

Closed at this stage:
- ordinary constant-density isotropic static control as a candidate route toward the horizon;
- silent continuation of that control through the Buchdahl singularity;
- treating anisotropy as an unconstrained tuning parameter;
- inferring dimensional collapse from static-branch failure.

Still open:
- constitutively closed anisotropic finite-3D configurations outside the horizon;
- dynamical finite-3D successor-core evolution toward and through horizon formation;
- whether any causal, energy-condition-controlled re-formed stress-energy branch admits a nonzero minimum core radius.

## Next step — BH-RB-009

Construct a **minimal dynamical spherical successor-core interface** without choosing the final minimum radius in advance.

Use shell-resolved areal radius \(R(t,a)\), enclosed Misner-Sharp-type mass \(m(t,a)\), local energy density, radial/tangential stress, and explicit predecessor-successor balance data. The first goal is not to solve the endpoint, but to identify the smallest set of equations and constitutive inputs needed to evolve a finite three-dimensional support across the horizon without confusing coordinate singularity, trapped-surface formation, matter compression, and dimensional collapse.
