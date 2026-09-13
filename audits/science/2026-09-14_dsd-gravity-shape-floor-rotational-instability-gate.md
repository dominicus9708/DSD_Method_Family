# BH-RB-015 — Shape-floor / rotational-instability gate

## Status

**PASS_WITH_BOUNDARY / POSITIVE_SHAPE_FLOOR_EXISTS_ON_STABLE_MACLAURIN_CONTROL / INSTABILITY_PREEMPTS_AXISYMMETRIC_Q_TO_ZERO / UNIVERSAL_GR_Q_MIN_NOT_DERIVED / POST_INSTABILITY_DYNAMIC_BRANCH_REQUIRED**

This audit continues BH-RB-014. BH-RB-014 produced a conditional equatorial causal scale from retained angular momentum but left the polar/equatorial aspect ratio

\[
q=\frac{c}{a}
\]

open. BH-RB-015 asks whether a positive `q` floor can emerge from a concrete fluid branch without inserting `q_min` by hand.

## External control only

The control model is the classical homogeneous, incompressible, uniformly rotating Maclaurin spheroid. It is Newtonian, horizonless, and is **not** a black-hole interior model.

For an oblate spheroid,

\[
e^2=1-\frac{c^2}{a^2},
\qquad
q=\frac ca=\sqrt{1-e^2}.
\]

Braviner & Ogilvie (MNRAS 441, 2321, 2014) summarize the classical Maclaurin sequence: the sequence is secularly unstable for approximately

\[
e\gtrsim0.8127,
\]

and dynamically unstable for approximately

\[
e\gtrsim0.9529.
\]

The corresponding positive aspect ratios are

\[
q_{\rm sec}=\sqrt{1-0.8127^2}\approx0.582682,
\]

\[
q_{\rm dyn}=\sqrt{1-0.9529^2}\approx0.303285.
\]

Thus the stable axisymmetric Maclaurin branch loses stability while `c/a` is still positive. The axisymmetric stable branch therefore does **not** continuously reach `q=0`.

## What this does and does not prove

The result is branch-conditional:

\[
\boxed{
q\ge q_{\rm dyn}>0
}
\]

only if one insists on remaining inside the dynamically stable Maclaurin control branch, and

\[
\boxed{
q\ge q_{\rm sec}>0
}
\]

if one also requires secular stability.

This does **not** prove a universal relativistic `q_min`. Once the instability is crossed, the object can leave axisymmetry, form a bar/spiral structure, redistribute angular momentum, emit gravitational waves, and possibly eject matter. In full relativity the dynamical bar-mode threshold shifts; standard reviews quote values around `T/|W| ~ 0.24–0.25` in some relativistic differentially rotating models instead of the Newtonian Maclaurin value near `0.27`. Differential rotation can also trigger lower-`T/|W|` instabilities. Therefore the numeric Maclaurin `q` floors are not universal.

## Combination with BH-RB-014

BH-RB-014 supplied the minimal finite-rotator control

\[
a_{\rm causal}
=
\frac{f_J}{\kappa f_M}\chi r_g,
\qquad
r_g=\frac{GM}{c^2},
\]

with `kappa=2/5` for the uniform-spheroid control.

For

\[
R_V=(a^2c)^{1/3}=a q^{1/3},
\]

an independently supplied positive `q` floor gives

\[
\boxed{
R_{V,\min}
\ge
\frac{f_J}{\kappa f_M}\chi r_g q_{\min}^{1/3}
}.
\]

Using the Maclaurin stability cutoffs only as controls,

\[
q_{\rm sec}^{1/3}\approx0.835239,
\qquad
q_{\rm dyn}^{1/3}\approx0.671867.
\]

For the synthetic control `chi=0.9`, `f_J=f_M=1`, `kappa=2/5`,

\[
\frac{R_{V,\min}^{\rm sec}}{r_g}
\approx1.879287,
\]

\[
\frac{R_{V,\min}^{\rm dyn}}{r_g}
\approx1.511701.
\]

Using the same Sgr A* mass scale employed in the prior restart audits gives approximately

\[
R_{V,\min}^{\rm sec}\approx1.19245\times10^7\ \mathrm{km},
\]

\[
R_{V,\min}^{\rm dyn}\approx9.59212\times10^6\ \mathrm{km}.
\]

These are **not black-hole-core radius predictions**. They are conditional control scales showing that once a specific stable-fluid branch supplies a positive shape floor, the BH-RB-014 equatorial causal floor converts into a positive 3D volume-equivalent scale.

## Structural interpretation

The useful result is not the Maclaurin number itself but the intervention mechanism:

\[
\boxed{
\text{continued flattening}
\rightarrow
\text{nonaxisymmetric instability}
\rightarrow
\text{reorganization / angular-momentum transport}
}
\]

before the stable axisymmetric branch reaches `q=0`.

This is compatible with the current working idea of a highly dynamical successor core: a contracting rotating structure may be forced to reorganize rather than remain a single axisymmetric equilibrium sequence all the way toward zero polar thickness.

However,

\[
\boxed{
\text{instability-driven reorganization}
\neq
\text{proof of a persistent finite black-hole core}
}
\]

and the post-instability relativistic evolution still has to be solved.

## Next gate

**BH-RB-016 — post-instability reorganization / angular-momentum-loss gate** should test whether nonaxisymmetric instability, gravitational-wave angular-momentum loss, and mass/energy redistribution can drive the system toward a bounded nonzero finite-support cycle or whether standard GR collapse still reaches an incomplete/singular endpoint.

The key quantities are

\[
\dot J_{\rm core},
\qquad
\dot M_{\rm core},
\qquad
R_{\rm eq}(\tau),
\qquad
R_{\rm pole}(\tau),
\qquad
\beta=T/|W|,
\]

with explicit provenance separation between standard GR/hydrodynamics and any DSD-level descriptor.

## References

- Braviner, H. J. & Ogilvie, G. I., *Tidal interactions of a Maclaurin spheroid – I. Properties of free oscillation modes*, MNRAS 441, 2321–2340 (2014), https://academic.oup.com/mnras/article/441/3/2321/1122401
- Paschalidis, V. & Stergioulas, N., *Rotating Stars in Relativity*, Living Reviews in Relativity 20, 7 (2017), https://link.springer.com/article/10.1007/s41114-017-0008-x
