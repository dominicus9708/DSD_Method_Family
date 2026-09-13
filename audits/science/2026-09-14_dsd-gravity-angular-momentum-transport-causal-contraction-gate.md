# BH-RB-014 — Angular-Momentum Transport / Causal Contraction Gate

**Date:** 2026-09-14  
**Project:** DSD gravity restart branch  
**Status:** `PASS_WITH_BOUNDARY / ANGULAR_MOMENTUM_CAUSAL_SCALE_IDENTIFIED / CONTRACTION_REQUIRES_J_TRANSPORT_OR_STRONG_FIELD_REORGANIZATION / POLAR_CLOSURE_STILL_REQUIRED / FINITE_3D_CORE_RADIUS_NOT_DERIVED`

## 1. Purpose

BH-RB-012 identified rotation as a genuine scale and directional channel, while BH-RB-013 showed that direct centrifugal support vanishes on the rotation axis and that spatial/flow anisotropy does not by itself require anisotropic material stress.

BH-RB-014 asks a narrower question:

> If a finite rotating successor core carries a nonzero fraction of the black hole's total angular momentum, can it contract indefinitely while retaining that angular momentum?

This audit does **not** attempt a full axisymmetric black-hole interior solution. It uses a minimal finite-body angular-momentum control to identify a necessary transport/causality gate before a more complete GR dynamical closure is attempted.

## 2. Provenance and firewall

External standard-relativity comparator:

\[
r_g=\frac{GM}{c^2},
\qquad
\chi=\frac{Jc}{GM^2},
\qquad
r_+=r_g\left(1+\sqrt{1-\chi^2}\right).
\]

Minimal finite-rotator control:

\[
J_{\rm core}=f_J J,
\qquad
M_{\rm core}=f_M M,
\]

\[
I=\kappa M_{\rm core}a^2,
\qquad
v_{\rm eq}=\Omega a,
\qquad
J_{\rm core}=I\Omega.
\]

For a homogeneous oblate spheroid about its symmetry axis,

\[
\kappa=\frac25.
\]

The relation \(I=\kappa M a^2\) and \(v_{\rm eq}=\Omega a\) is a Newtonian/weak-field control only.

In full GR, rotating matter is described relative to the spacetime geometry and frame dragging. There is no unique general-relativistic extension of the Newtonian moment of inertia; \(I=J/\Omega\) is a common equilibrium definition. Therefore the following scale is **not** an exact black-hole-interior law.

Reference:

- V. Paschalidis and N. Stergioulas, *Rotating Stars in Relativity*, Living Rev. Relativ. **20**, 7 (2017), DOI: 10.1007/s41114-017-0008-x.
- E. Gourgoulhon, *An introduction to the theory of rotating relativistic stars*, arXiv:1003.5015.

## 3. Causal equatorial contraction scale

From

\[
J_{\rm core}
=
\kappa M_{\rm core}a^2\Omega
=
\kappa M_{\rm core}a\,v_{\rm eq},
\]

the dimensionless rotational-speed control is

\[
\beta_{\rm rot}
\equiv
\frac{v_{\rm eq}}{c}
=
\frac{J_{\rm core}}
{\kappa M_{\rm core}ca}.
\]

Using

\[
J=\chi\frac{GM^2}{c}
=
\chi M r_gc,
\]

one obtains

\[
\beta_{\rm rot}
=
\frac{f_J}{f_M}
\frac{\chi r_g}{\kappa a}.
\]

Therefore \(\beta_{\rm rot}<1\) requires

\[
\boxed{
a>
a_{\rm causal}
\equiv
\frac{f_J}{\kappa f_M}\chi r_g
}.
\]

This is the first conditional finite equatorial scale in the restart branch that follows directly from a nonzero angular-momentum carrier plus the finite-rotator control.

It is **not** yet a physical black-hole core radius.

## 4. Kerr-horizon scale comparison

Requiring this toy causal equatorial scale to fit below the Kerr outer-horizon coordinate scale gives

\[
a_{\rm causal}\le r_+.
\]

With

\[
\eta\equiv\frac{f_J}{f_M},
\]

this becomes

\[
\boxed{
\eta
\le
\eta_{\max}
=
\frac{\kappa}{\chi}
\left(1+\sqrt{1-\chi^2}\right)
}.
\]

For \(\kappa=2/5\):

| \(\chi\) | \(r_+/r_g\) | \(\eta_{\max}\) | \(a_{\rm causal}(f_J=f_M=1)/r_g\) |
|---:|---:|---:|---:|
| 0.30 | 1.953939 | 2.605252 | 0.750000 |
| 0.50 | 1.866025 | 1.492820 | 1.250000 |
| 0.70 | 1.714143 | 0.979510 | 1.750000 |
| 0.90 | 1.435890 | 0.638173 | 2.250000 |
| 0.99 | 1.141067 | 0.461037 | 2.475000 |
| 1.00 | 1.000000 | 0.400000 | 2.500000 |

For an all-mass/all-angular-momentum toy core, \(\eta=1\).

The equality condition

\[
\frac{\chi}{\kappa}
=
1+\sqrt{1-\chi^2}
\]

gives

\[
\boxed{
\chi_{\rm crit}
=
\frac{2\kappa}{1+\kappa^2}
}.
\]

For \(\kappa=2/5\),

\[
\boxed{
\chi_{\rm crit}
=
\frac{20}{29}
\approx0.689655.
}
\]

Thus, within this control, an all-\(M\), all-\(J\) homogeneous rigid core cannot both remain subluminal and fit below the Kerr outer-horizon coordinate scale once \(\chi>20/29\).

This does **not** prove such a core is impossible in GR. It means that at least one control assumption must fail: the core may carry only part of \(J\), the core mass assignment may differ, \(\kappa\) may change, rotation may be differential, frame dragging may strongly modify the local velocity relation, or angular momentum may reside partly in geometry/fields rather than in a rigid material carrier.

## 5. Sgr A* scale control

Using

\[
M=4.297\times10^6M_\odot,
\qquad
\chi=0.9,
\]

gives

\[
r_g
\approx
6.3452497\times10^6\ {\rm km},
\]

\[
r_+
\approx
9.1110799\times10^6\ {\rm km}.
\]

For \(f_J=f_M=1\),

\[
a_{\rm causal}
=
2.25r_g
\approx
1.4276812\times10^7\ {\rm km},
\]

which exceeds the Kerr \(r_+\) coordinate scale.

For \(f_J=0.5,\ f_M=1\),

\[
a_{\rm causal}
=
1.125r_g
\approx
7.1384059\times10^6\ {\rm km},
\]

which lies below that comparator.

The maximum toy ratio at \(\chi=0.9\) is

\[
\boxed{
\left(\frac{f_J}{f_M}\right)_{\max}
\approx0.638173.
}
\]

## 6. Dynamic angular-momentum transport gate

The same control yields

\[
\beta_{\rm rot}
=
\frac{J_{\rm core}}
{\kappa M_{\rm core}ca}.
\]

Taking a logarithmic derivative with respect to a common evolution parameter gives

\[
\boxed{
\frac{\dot\beta_{\rm rot}}{\beta_{\rm rot}}
=
\frac{\dot J_{\rm core}}{J_{\rm core}}
-
\frac{\dot\kappa}{\kappa}
-
\frac{\dot M_{\rm core}}{M_{\rm core}}
-
\frac{\dot a}{a}
}.
\]

If \(M_{\rm core}\) and \(\kappa\) are fixed, then

\[
\frac{\dot\beta_{\rm rot}}{\beta_{\rm rot}}
=
\frac{\dot J_{\rm core}}{J_{\rm core}}
-
\frac{\dot a}{a}.
\]

For contraction,

\[
\dot a<0.
\]

If \(J_{\rm core}\) is conserved,

\[
\dot J_{\rm core}=0,
\]

then

\[
\dot\beta_{\rm rot}>0,
\qquad
\beta_{\rm rot}\propto a^{-1}.
\]

Therefore the minimal control cannot support indefinite contraction to \(a=0\) while keeping both nonzero fixed core angular momentum and subluminal equatorial motion.

To keep \(\beta_{\rm rot}\) constant with fixed \(M_{\rm core},\kappa\),

\[
\boxed{
\frac{\dot J_{\rm core}}{J_{\rm core}}
=
\frac{\dot a}{a}
}.
\]

To make \(\beta_{\rm rot}\) decrease,

\[
\boxed{
\frac{\dot J_{\rm core}}{J_{\rm core}}
<
\frac{\dot a}{a}
}.
\]

Thus continued contraction requires angular-momentum transport, redistribution, radiation, changing inertia structure, or a strong-field reorganization of the simple finite-rotator relation.

## 7. Equatorial floor is not yet a 3D core radius

Let the oblate support have equatorial semiaxis \(a\), polar semiaxis \(c\), and

\[
q=\frac ca.
\]

Its volume-equivalent radius is

\[
R_V
=
(a^2c)^{1/3}
=
a q^{1/3}.
\]

Even if

\[
a\ge a_{\rm causal}>0,
\]

one may still have

\[
q\to0,
\qquad
c\to0,
\qquad
R_V\to0.
\]

Therefore

\[
\boxed{
\text{finite equatorial scale}
\neq
\text{finite 3D core radius}.
}
\]

However, if a later polar-support closure independently proves

\[
q\ge q_{\min}>0,
\]

then the present angular-momentum scale immediately implies the conditional 3D lower bound

\[
\boxed{
R_{V,\min}
\ge
\frac{f_J}{\kappa f_M}
\chi r_g
q_{\min}^{1/3}.
}
\]

This is the main radius-reconstruction bridge opened by BH-RB-014.

## 8. Interpretation for the dynamic successor-core hypothesis

The current branch can now be narrowed to two possibilities.

1. **Angular momentum remains substantially in the successor core.**  
   Then contraction increases the required local rotational speed unless \(J_{\rm core}\) is redistributed. A nonzero equatorial causal scale appears.

2. **Angular momentum is continuously exported or stored elsewhere.**  
   Then the equatorial scale can shrink, and \(J\) alone cannot set \(R_{\min}\).

In either case, rotation by itself does not close the polar radius.

Therefore the hypothesized continuously compressing/re-forming core must be modeled together with angular-momentum transport rather than as a rigid body with fixed \(J_{\rm core}\).

## 9. Audit result

The Python audit performs 13 algebraic/logical checks.

Result:

\[
\boxed{13/13\ \mathrm{PASS}}
\]

Final verdict:

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
ANGULAR\_MOMENTUM\_CAUSAL\_SCALE\_IDENTIFIED /
CONTRACTION\_REQUIRES\_J\_TRANSPORT\_OR\_STRONG\_FIELD\_REORGANIZATION /
POLAR\_CLOSURE\_STILL\_REQUIRED /
FINITE\_3D\_CORE\_RADIUS\_NOT\_DERIVED}
}
\]

## 10. Next audit

**BH-RB-015 — dynamic polar-support / aspect-ratio-floor gate**

Target question:

\[
\boxed{
\text{Can the dynamical stress/pressure closure produce }
q_{\min}=\inf_\tau\frac{R_{\rm pole}(\tau)}{R_{\rm eq}(\tau)}>0
\text{ without inserting }q_{\min}\text{ by hand?}
}
\]

If yes, BH-RB-014 and BH-RB-015 combine to produce the first conditional positive three-dimensional radius bound:

\[
R_{V,\min}
\ge
a_{\rm causal}q_{\min}^{1/3}.
\]
