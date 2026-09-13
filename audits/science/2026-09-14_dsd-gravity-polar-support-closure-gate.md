# BH-RB-013 — Polar-support closure gate

Date: 2026-09-14

## Status

**PASS_WITH_BOUNDARY / DIRECT_POLAR_ROTATION_SUPPORT_ZERO / ISOTROPIC_PRESSURE_CAN_CLOSE_POLAR_BALANCE_IN_STATIONARY_CONTROL / TRAPPED_DYNAMIC_CORE_STILL_UNCLOSED**

## Scope

This audit follows BH-RB-012 and asks what actually supplies support on the rotation axis of a rotating finite-support successor-core candidate.

It corrects one over-strong inference from the previous step:

> spatial/flow anisotropy produced by rotation does **not** by itself imply anisotropic material stress.

The audit therefore separates three statements:

1. direct centrifugal support vanishes on the rotation axis;
2. a stationary rotating perfect fluid can nevertheless close the polar balance by a pressure/enthalpy gradient;
3. this stationary-star result does **not** establish a stationary trapped black-hole core.

## 1. Relativistic stationary-axisymmetric perfect-fluid comparator

For a circular stationary rotating perfect fluid,

\[
T^{\alpha\beta}=(\varepsilon+p)u^\alpha u^\beta+p g^{\alpha\beta},
\]

and the fluid 3-speed relative to a local ZAMO can be written

\[
v=(\Omega-\omega)e^{\psi-\nu}.
\]

The Euler equation in the meridional subspace can be written as

\[
\frac{\nabla p}{\varepsilon+p}
=
-\nabla\nu
+
\frac{1}{1-v^2}
\left(
 v\nabla v
-
\frac{v^2\nabla\Omega}{\Omega-\omega}
\right).
\]

For a regular symmetry axis, the azimuthal orbit shrinks there and the physical circular speed tends to zero. Hence on the axis the direct rotation-dependent terms vanish with \(v\to0\). The polar force balance is therefore supplied by the pressure/enthalpy gradient against the gravitational metric potential, not by a local centrifugal term.

This is a structural comparator only. It is a hydrostationary rotating-star equation and is not asserted to hold as a stationary matter configuration through a trapped region or event horizon.

## 2. Newtonian Maclaurin control

To test whether axisymmetric oblateness itself forces anisotropic stress, use the classical homogeneous Maclaurin spheroid as an analytic control.

Let the equatorial semi-axis be \(a\), polar semi-axis be \(c\), and

\[
e^2=1-\frac{c^2}{a^2}.
\]

The interior gravitational-potential coefficients are

\[
A_1=A_2=
\frac{\sqrt{1-e^2}}{e^3}\sin^{-1}e
-
\frac{1-e^2}{e^2},
\]

\[
A_3=
\frac{2}{e^2}
-
\frac{2\sqrt{1-e^2}}{e^3}\sin^{-1}e,
\]

with

\[
2A_1+A_3=2.
\]

Maclaurin equilibrium gives

\[
\frac{\Omega^2}{\pi G\rho}
=
\frac{2\sqrt{1-e^2}}{e^3}(3-2e^2)\sin^{-1}e
-
\frac{6(1-e^2)}{e^2}.
\]

Equivalently,

\[
\frac{\Omega^2}{\pi G\rho}
=
2\left[A_1-(1-e^2)A_3\right].
\]

Along the rotation axis there is no centrifugal term. Integrating the polar hydrostatic balance from the pole to the center gives the dimensionless central-pressure load

\[
\frac{p_c}{\pi G\rho^2a^2}
=
A_3(1-e^2).
\]

Along the equator the centrifugal contribution reduces the required pressure load to

\[
\frac{p_c}{\pi G\rho^2a^2}
=
A_1-rac12\frac{\Omega^2}{\pi G\rho}.
\]

Using the Maclaurin relation,

\[
A_3(1-e^2)
=
A_1-rac12\frac{\Omega^2}{\pi G\rho}.
\]

Thus a single isotropic pressure field closes both the equatorial and polar balances even though the equilibrium figure is oblate and the flow is rotationally anisotropic.

Therefore

\[
\boxed{
\text{spatial/flow anisotropy}
\neq
\text{material-stress anisotropy}
}
\]

and

\[
\boxed{
\text{zero direct polar centrifugal support}
\not\Rightarrow
p_r\neq p_\theta\neq p_\phi
}
\]

by itself.

## 3. Numerical control values

For selected eccentricities:

| \(e\) | \(c/a\) | \(\Omega^2/(\pi G\rho)\) | \(p_c/(\pi G\rho^2a^2)\) |
|---:|---:|---:|---:|
| 0.00000 | 1.000000 | 0.000000000 | 0.666666667 |
| 0.30000 | 0.953939 | 0.048615784 | 0.629701999 |
| 0.60000 | 0.800000 | 0.201352060 | 0.504883632 |
| 0.80000 | 0.600000 | 0.363158848 | 0.342594660 |
| 0.81267 | 0.582724 | 0.374229666 | 0.328775673 |
| 0.90000 | 0.435890 | 0.440528882 | 0.214709792 |
| 0.92996 | 0.367661 | 0.449331412 | 0.165002473 |

The classical Maclaurin sequence becomes secularly unstable near \(e\simeq0.8127\), so the higher-e rows are only algebraic continuation controls, not preferred stable equilibria.

At the secular-instability threshold control,

\[
e=0.81267,
\qquad
\frac ca\approx0.582724,
\]

while the polar central-pressure coefficient remains positive:

\[
\frac{p_c}{\pi G\rho^2a^2}
\approx0.328776.
\]

Therefore rapid rotation can strongly flatten the object and reduce the required polar load, but it does not replace the polar pressure support by centrifugal support.

## 4. Consequence for the DSD black-hole core branch

BH-RB-012 correctly identified a **direct polar rotation-support deficit**, but BH-RB-013 narrows its meaning.

The correct conclusion is

\[
\boxed{
\text{rotation supplies no direct polar centrifugal support,}
\quad
\text{but isotropic pressure may supply polar support in a stationary nontrapped control.}
}
\]

Hence the next calculation should **not** assume anisotropic stress from the outset.

The constitutive hierarchy should be tested in this order:

\[
\text{axisymmetric perfect-fluid dynamics}
\rightarrow
\text{differential rotation / shear}
\rightarrow
\text{anisotropic stress only if required}
\rightarrow
\text{flux / magnetic or other field stress if required}.
\]

This preserves the project rule against fitting a desired finite radius by adding unnecessary constitutive freedom.

## 5. Remaining firewall

The Maclaurin model is Newtonian and horizonless. The relativistic comparator is stationary and designed for rotating-star equilibria. Neither establishes

\[
R_{\rm core}>0
\]

inside a trapped black-hole region.

The active black-hole problem therefore remains

\[
\boxed{
\text{Can an axisymmetric, rotating, dynamically evolving finite-support matter configuration}
\atop
\text{remain regular with }R_{\rm core}(\tau)\ge R_{\min}>0\text{ in a trapped region?}
}
\]

That question requires the next gate to abandon hydrostationarity and evolve the axisymmetric stress-energy and angular-momentum transport explicitly.

## 6. Next step

**BH-RB-014 — axisymmetric dynamic finite-support / angular-momentum-transport gate**

Minimum unknowns should include a time-dependent matter support, differential rotation, shear, energy density, pressure, angular-momentum transport, and a geometry carrier sufficient to distinguish equatorial and polar support scales.

No finite-core radius is to be inserted as a target value. Any positive \(R_{\min}\) must emerge from the chosen standard-GR constitutive closure and evolution.

## Sources

- V. Paschalidis and N. Stergioulas, *Rotating Stars in Relativity*, Living Reviews in Relativity 20, 7 (2017), DOI: 10.1007/s41114-017-0008-x.
- H. J. Braviner and G. I. Ogilvie, *Tidal interactions of a Maclaurin spheroid — I. Properties of free oscillation modes*, MNRAS 441 (2014) 2321–2341.
- FLASH User's Guide, Maclaurin gravity test, analytic interior potential coefficients; formulation traces to the classical theory of ellipsoidal figures.
