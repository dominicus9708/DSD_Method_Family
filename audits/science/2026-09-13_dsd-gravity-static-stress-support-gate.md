# DSD Gravity Static Stress Support Gate — BH-RB-008

Date: 2026-09-13

Status: **PASS_WITH_BOUNDARY / STATIC_STANDARD_SUPPORT_BRANCHES_EXCLUDED_FOR_R_LE_RS / DYNAMIC_BRANCH_REQUIRED**

## Purpose

Continue BH-RB-007 without reusing the discarded structural-gravity branch. The active working hypothesis is a finite three-dimensional successor core with

\[
\dim X_{\rm space}=3,\qquad R_{\rm core}>0,
\]

while the first comparator remains nonrotating and explicitly neutral:

\[
J=0,\qquad Q=0.
\]

This audit asks whether ordinary static stress support in standard GR can hold such a core in the target interval

\[
0<R_{\rm core}\le r_s,
\qquad
r_s=\frac{2GM}{c^2}.
\]

The answer is negative for the stated static isotropic branch and also for a broad static anisotropic branch satisfying the Andreasson hypotheses with nonnegative pressures and the dominant energy condition. This does **not** prove that a finite three-dimensional core is impossible; it closes only those static branches.

## Provenance boundary

The finite-support / formation-successor hypothesis is a DSD-side research branch. Einstein dynamics, the TOV equation, Buchdahl's theorem, and the Andreasson compactness theorem are external standard-GR inputs. Their use does not make them DSD-derived laws.

Current DSD dynamics also requires an explicit constitutive bridge before typed properties can be interpreted as dynamic coefficients or stress operators. Therefore no DSD property label is silently identified with pressure, stiffness, or a support law.

## 1. Static isotropic branch

For a static, spherically symmetric perfect fluid in GR, under the standard Buchdahl assumptions including isotropic pressure and nonincreasing density, the compactness obeys

\[
\frac{2GM}{Rc^2}\le\frac89.
\]

Therefore

\[
R\ge\frac98 r_s.
\]

The target black-hole-core interval is instead

\[
0<R_{\rm core}\le r_s.
\]

Hence the entire target interval lies below the Buchdahl static perfect-fluid domain.

### Constant-density pressure witness

For the interior Schwarzschild constant-density solution, define

\[
u=\frac{r_s}{R}.
\]

The central pressure is

\[
\frac{p_c}{\rho c^2}
=
\frac{1-\sqrt{1-u}}{3\sqrt{1-u}-1}.
\]

The denominator vanishes at

\[
3\sqrt{1-u}-1=0
\quad\Longrightarrow\quad
u=\frac89
\quad\Longrightarrow\quad
R=\frac98r_s.
\]

Thus this explicit solution witnesses the pressure blow-up at the same threshold.

For the fresh Sgr A* mass comparator

\[
M=4.297\times10^6M_\odot,
\]

we obtain

\[
r_s\approx1.2690499\times10^7\ {\rm km},
\]

and the Buchdahl minimum static radius is

\[
R_{\rm Buchdahl}\approx1.4276812\times10^7\ {\rm km}.
\]

The script evaluates the central-pressure ratio as the limit is approached from above:

| \(R/r_s\) | \(p_c/(\rho c^2)\) |
|---:|---:|
| 2.0 | 0.2612 |
| 1.5 | 0.5774 |
| 1.25 | 1.6180 |
| 1.13 | 37.6638 |
| 1.126 | 187.6661 |
| 1.1251 | 1875.1666 |

This witness is not itself the universal proof; Buchdahl's theorem supplies the broader static perfect-fluid bound.

## 2. Static anisotropic branch

Allow

\[
T^{\hat\mu}{}_{\hat\nu}
=
\operatorname{diag}(-\varepsilon,p_r,p_t,p_t),
\]

so that radial and tangential stresses need not agree.

For static spherically symmetric matter satisfying

\[
\rho\ge0,\qquad p_r\ge0,
\]

and

\[
p_r+2p_t\le\Omega\rho,
\]

Andreasson's sharp bound gives

\[
\frac{2GM}{Rc^2}
\le
\frac{(1+2\Omega)^2-1}{(1+2\Omega)^2}.
\]

If the pressures are nonnegative and the dominant energy condition is imposed, then

\[
p_r\le\rho,\qquad p_t\le\rho
\]

implies the admissible choice \(\Omega=3\). Therefore

\[
\frac{2GM}{Rc^2}\le\frac{48}{49},
\]

or equivalently

\[
R\ge\frac{49}{48}r_s
\approx1.0208333\,r_s.
\]

For the same Sgr A* scale,

\[
R_{\rm DEC,static}\gtrsim1.2954885\times10^7\ {\rm km}.
\]

Thus anisotropy relaxes the isotropic Buchdahl limit, but under these broad static DEC assumptions it still does not reach the horizon radius, let alone a static surface below it.

## 3. Result for the active finite-core branch

The present working target is

\[
0<R_{\rm core}\le r_s.
\]

Two static branches are now closed:

\[
\text{ordinary static isotropic perfect fluid}
\quad\Longrightarrow\quad
R\ge\frac98r_s>r_s,
\]

and

\[
\text{static anisotropic + nonnegative pressures + DEC}
\quad\Longrightarrow\quad
R\ge\frac{49}{48}r_s>r_s.
\]

Therefore a finite three-dimensional successor core inside the Schwarzschild radius cannot be modeled as either of those static support systems.

The surviving logical alternatives are:

1. a genuinely **dynamical** finite three-dimensional core/evolution;
2. relaxation of one or more static matter assumptions, with the relaxation stated explicitly;
3. an exotic effective stress regime, negative pressure, surface layer, or other nonstandard constitutive structure, again with explicit provenance;
4. failure of the finite-core working hypothesis itself.

The next branch must not select option 2 or 3 merely to force a desired radius. The least assumption-loading continuation is the dynamical branch.

## 4. Relation to describability collapse

This result concerns physical support, not observational reconstruction. Even if a dynamical finite core exists, the exterior map

\[
D_{\rm ext}(S_{\rm core})
\]

may remain non-injective, so the core radius and internal stress profile need not be externally reconstructible from \(M,J,Q,r_H\) alone. Conversely, inability to reconstruct the core does not establish that the core is zero-dimensional.

## External standard references

- E. Chavez Nambo and O. Sarbach, *Static spherical perfect fluid stars with finite radius in general relativity: a review*, arXiv:2010.02859. TOV formulation and Buchdahl compactness bound.
- H. Andreasson, *Sharp bounds on 2m/r of general spherically symmetric static objects*, arXiv:gr-qc/0702137. Sharp anisotropic compactness bound under \(p_r+2p_t\le\Omega\rho\).

## Audit verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY / STATIC\_STANDARD\_SUPPORT\_BRANCHES\_EXCLUDED\_FOR\_R\_LE\_RS / DYNAMIC\_BRANCH\_REQUIRED}
}
\]

The result does not prove nonexistence of a finite three-dimensional black-hole core. It proves that the target interval is not supported by the stated regular static GR matter branches. The next audit should therefore formulate a dynamical spherical finite-support problem without assuming the answer for the minimum radius.
