# DSD Gravity Finite 3D Re-formed Core Assumption Gate — BH-RB-007

Date: 2026-09-13

Status: **PASS_WITH_BOUNDARY / FINITE_3D_SUCCESSOR_CORE_BRANCH_OPEN / CONSTITUTIVE_CLOSURE_REQUIRED**

## Purpose

Open the next black-hole branch without reusing the discarded structural-gravity equations.

The target is not a point singularity radius. The working question is whether a finite, positive-radius, three-dimensional mass-energy support can remain after stellar constituents cease to preserve their prior particle-level identity.

The branch therefore distinguishes:

1. lower-dimensional effective motion or representation;
2. realized-axis rank change;
3. compression of a three-dimensional matter support;
4. an actual reduction of ambient spatial dimensionality.

No automatic identification among these four is permitted.

## Working specialization

For the first spherical branch, adopt:

\[
\dim X_{\rm space}=3,
\qquad
\dim \operatorname{Supp}_{\rm core}=3,
\qquad
R_{\rm core}>0.
\]

These are working specialization assumptions, not generic DSD theorems.

The predecessor stellar state may lose constituent identity and cross a formation-level transition into a new macroscopic successor core:

\[
S_\star \longrightarrow S_{\rm diss} \longrightarrow S_{\rm core}.
\]

The successor is not assumed to be made from intact neutrons, nuclei, atoms, or any other specific inherited particle species. It is therefore called a **constituent-agnostic re-formed core**.

The phrase `pure mass` is not used as a literal material ontology. Physical closure must be expressed through stress-energy or another explicit external physical representation.

## DSD provenance

The active DSD dynamics permits formation-level transitions when the inherited Stage-VI formation background or admitted channel set changes. Such transitions are not treated as value evolution of one fixed channel; predecessor and successor structures require lineage data.

Component-lineage relations do not require literal equality of pre- and post-transition objects, and branching or merging is not excluded. Therefore many predecessor constituents may, in principle, be related to a new successor structure without claiming that their old formation identity is preserved.

DSD also does not canonically map a property label to a pressure, stress, stiffness, inertia, or evolution operator. Any such physical role requires an explicit constitutive bridge. Conservation laws likewise remain additional model conditions.

## First external comparator specialization

The initial branch uses explicit physical/global statuses

\[
J=0,
\qquad
Q=0,
\]

not undefined values silently replaced by zero. The external comparator is therefore the spherical, neutral, nonrotating branch.

The global mass input is denoted by \(M\), and the external Schwarzschild radius only sets a comparison scale:

\[
r_s=\frac{2GM}{c^2}.
\]

Define a dimensionless candidate core-radius fraction

\[
\lambda:=\frac{R_{\rm core}}{r_s},
\qquad
0<\lambda\le1.
\]

Then

\[
R_{\rm core}=\lambda r_s,
\]

and the mean mass density of a finite three-dimensional support is

\[
\bar\rho(M,\lambda)
=\frac{3M}{4\pi R_{\rm core}^3}
=\frac{3c^6}{32\pi G^3M^2\lambda^3}.
\]

This is only a kinematic scale relation. It is not an equilibrium solution or an equation of state.

The associated compactness ratio is

\[
\mathcal C=\frac{r_s}{R_{\rm core}}=\lambda^{-1}.
\]

## Sgr A* scale control

Using the independently reintroduced benchmark mass

\[
M=4.297\times10^6M_\odot,
\]

the external Schwarzschild scale is

\[
r_s\approx1.2690499\times10^7\;\mathrm{km}.
\]

For representative positive-radius fractions:

| \(\lambda\) | \(R_{\rm core}\) (km) | \(\bar\rho\) (kg m\(^{-3}\)) |
|---:|---:|---:|
| 1 | \(1.26905\times10^7\) | \(9.98067\times10^5\) |
| 0.5 | \(6.34525\times10^6\) | \(7.98454\times10^6\) |
| 0.1 | \(1.26905\times10^6\) | \(9.98067\times10^8\) |
| 0.01 | \(1.26905\times10^5\) | \(9.98067\times10^{11}\) |

The \(\lambda^{-3}\) density scaling follows only from fixed mass plus finite 3D volume.

## Stress-energy requirement

The first general spherical effective form is left open as

\[
T^{\hat\mu}{}_{\hat\nu}
=
\operatorname{diag}
\left(
-\varepsilon(r),
 p_r(r),
 p_t(r),
 p_t(r)
\right).
\]

No equation of state or stress law is yet imposed.

This gate therefore does **not** claim that a stable or static core exists at any \(0<R_{\rm core}\le r_s\). Before such a claim, one must supply either:

- a constitutive relation for \(\varepsilon,p_r,p_t\); or
- a fully dynamical evolution law for the successor core.

## Audit result

The executable audit checks eight items:

1. ambient spatial dimension is kept at 3 by explicit specialization;
2. the candidate support remains finite and three-dimensional;
3. inherited constituent identity is not required;
4. stress-energy closure is required;
5. \(J=0\) and \(Q=0\) are explicit defined-zero statuses;
6. mean density scales as \(R^{-3}\);
7. no equilibrium claim is made before constitutive closure;
8. the scan domain excludes \(R_{\rm core}=0\).

Result: **8/8 PASS**.

## Boundary

This result does not establish a black-hole interior equation of state, does not prove a finite core exists, and does not derive a minimum radius.

It only opens a logically consistent calculation branch in which the stellar predecessor may reorganize into a new finite 3D successor core without identifying constituent loss, compression, or external point-like describability with an actual dimensional collapse.

## Next step — BH-RB-008

Close the physical constitutive search space before solving for a radius.

The next audit should compare at least:

1. isotropic stress \(p_r=p_t\);
2. anisotropic stress \(p_r\ne p_t\);
3. static versus explicitly dynamical support;
4. energy-condition and causality constraints;
5. whether any constituent-agnostic closure can be stated without inserting the desired minimum radius by hand.
