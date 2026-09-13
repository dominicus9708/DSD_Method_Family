# BH-RB-016 — Repeated reorganization / radius-floor persistence gate

**Date:** 2026-09-14  
**Status:** `PASS_WITH_BOUNDARY / REPEATED_REORGANIZATION_CHANNEL_IDENTIFIED / ROTATIONAL_FLOOR_NOT_SELF_PERSISTING_UNDER_GENERIC_J_LOSS / POSITIVE_ASYMPTOTIC_RADIUS_REQUIRES_ADDITIONAL_CLOSURE`

## Scope

This audit continues BH-RB-014 and BH-RB-015.

It does **not** assume a finite black-hole-core radius.  
It asks a narrower question:

> If repeated rotational instability causes a successor core to reorganize, lose or redistribute angular momentum, and contract again, does that cycle itself force a positive asymptotic three-dimensional radius floor?

The answer in the present control is **no**.

That negative result is useful because it identifies the missing closure explicitly.

## Provenance boundary

The active DSD gravity rebaseline remains in force.

- DSD does not derive Einstein dynamics, a black-hole equation of state, a unique stress tensor, or a black-hole-core constitutive law.
- The moment-of-inertia relation used below is a finite-body Newtonian/weak-field control.
- Maclaurin/bar-mode thresholds are external standard-fluid comparators, not DSD constants.
- No result from the discarded pre-2026-09-11 structural-gravity radius branch is reused.

## Input from BH-RB-014/015

The finite-rotator control gave

\[
a_{\rm causal}
=
\frac{J_{\rm core}}{\kappa M_{\rm core}c},
\]

and with an aspect ratio

\[
q=\frac{R_{\rm pole}}{R_{\rm eq}}>0
\]

the volume-equivalent scale is

\[
R_V=a q^{1/3}.
\]

Combining them gives the conditional scale

\[
R_{\rm floor}
=
\frac{J_{\rm core}}{\kappa M_{\rm core}c}
q^{1/3}.
\]

This is not yet a black-hole-core radius law.  
It is only the lower scale supplied by the finite-rotator control if the branch has specified \(J_{\rm core},M_{\rm core},\kappa,q\).

## Reorganization recurrence

Let an instability/reorganization episode retain fractions

\[
J_{n+1}=s_J J_n,
\qquad
M_{n+1}=s_M M_n,
\]

with

\[
0\le s_J\le1,
\qquad
0<s_M\le1.
\]

For fixed \(\kappa\) and fixed positive shape control \(q\),

\[
R_{{\rm floor},n}
=
\frac{J_n}{\kappa M_n c}q^{1/3},
\]

so exactly

\[
\boxed{
\frac{R_{{\rm floor},n+1}}
     {R_{{\rm floor},n}}
=
\frac{s_J}{s_M}
}.
\]

Therefore three regimes exist:

\[
s_J<s_M
\quad\Rightarrow\quad
R_{{\rm floor},n}\to0,
\]

\[
s_J=s_M
\quad\Rightarrow\quad
R_{{\rm floor},n}=\text{constant},
\]

\[
s_J>s_M
\quad\Rightarrow\quad
R_{{\rm floor},n}\text{ grows}.
\]

Thus repeated reorganization plus angular-momentum shedding does **not** automatically protect a finite radius.

If angular momentum is removed fractionally faster than mass, the rotational lower scale itself moves inward.

## General one-cycle identity

If the shape and inertial factor also reorganize,

\[
\boxed{
\frac{R_{{\rm floor},n+1}}
     {R_{{\rm floor},n}}
=
\frac{s_J}{s_M}
\frac{\kappa_n}{\kappa_{n+1}}
\left(
\frac{q_{n+1}}{q_n}
\right)^{1/3}
}.
\]

Hence the actual persistence criterion is

\[
\boxed{
\inf_n
\left[
\frac{J_n}{\kappa_n M_n}
q_n^{1/3}
\right]
>0.
}
\]

A positive shape floor alone is insufficient if \(J_n/M_n\to0\).

Likewise, nonzero angular momentum alone is insufficient if \(q_n\to0\) or if \(\kappa_n\) changes without a bound.

## Numerical control

Use only the Sgr A* mass scale

\[
M_0=4.297\times10^6M_\odot
\]

and a synthetic spin control

\[
\chi_0=0.9.
\]

For the finite-body control

\[
\kappa=\frac25
\]

and the Maclaurin dynamical-instability shape comparator

\[
e_{\rm dyn}=0.9529,
\qquad
q_{\rm dyn}=\sqrt{1-e_{\rm dyn}^2}
\simeq0.303284668,
\]

the initial conditional scale is

\[
\frac{R_{{\rm floor},0}}{r_g}
=
\frac{\chi_0}{\kappa}q_{\rm dyn}^{1/3}
\simeq1.511701359.
\]

Now choose a deliberately simple reorganization control,

\[
s_J=0.80,
\qquad
s_M=0.99.
\]

Then

\[
\frac{s_J}{s_M}
\simeq0.808080808<1.
\]

The conditional floor becomes

\[
\frac{R_{{\rm floor},5}}{r_{g,0}}
\simeq0.520883,
\]

\[
\frac{R_{{\rm floor},10}}{r_{g,0}}
\simeq0.179479,
\]

\[
\frac{R_{{\rm floor},20}}{r_{g,0}}
\simeq0.021309.
\]

Therefore an indefinitely repeated cycle of this type drives the rotational floor toward zero even though every finite cycle still has positive radius.

## Optional bar-mode trigger scaling control

For the Newtonian finite-body scaling

\[
T=\frac{J^2}{2I},
\qquad
I=\kappa Ma^2,
\qquad
|W|=\alpha\frac{GM^2}{a},
\]

one gets

\[
\beta=\frac{T}{|W|}
=
\frac{J^2}
{2\kappa\alpha GM^3a}.
\]

At a supplied instability threshold \(\beta_{\rm crit}\),

\[
a_{\rm bar}
=
\frac{J^2}
{2\kappa\alpha\beta_{\rm crit}GM^3}.
\]

Hence across the same geometric retention cycle,

\[
\boxed{
\frac{a_{{\rm bar},n+1}}
     {a_{{\rm bar},n}}
=
\frac{s_J^2}{s_M^3}.
}
\]

For \(s_J=0.80,\ s_M=0.99\),

\[
\frac{s_J^2}{s_M^3}
\simeq0.659590497<1.
\]

So in this control the next rotational-instability trigger also moves inward after strong angular-momentum loss.

This reinforces the main result: instability can produce reorganization and angular-momentum transport without producing a self-sustaining positive radius floor.

## Standard-physics comparator

For incompressible Maclaurin spheroids the classical dynamical bar-mode threshold is near

\[
T/|W|\simeq0.2738,
\]

while fully relativistic differentially rotating stellar simulations can show dynamical bar instability around

\[
T/|W|\sim0.24-0.25.
\]

The physical consequences include nonaxisymmetric deformation, spiral structure in sufficiently unstable cases, angular-momentum redistribution, mass ejection, and gravitational-wave emission.

These facts justify the existence of a **reorganization channel** as an external comparator.  
They do not imply that a trapped black-hole successor core follows a Maclaurin or neutron-star instability sequence.

## Main result

The candidate picture

\[
\text{contraction}
\to
\text{rotational instability}
\to
\text{reorganization}
\to
J\text{ transport}
\to
\text{renewed contraction}
\]

is dynamically meaningful as a hypothesis.

However,

\[
\boxed{
\text{repeated reorganization}
\not\Rightarrow
R_{\min}>0.
}
\]

If instability repeatedly removes enough specific angular momentum,

\[
\frac{J_n}{M_n}\to0,
\]

then the rotational floor inherited from BH-RB-014 also tends to zero.

Thus rotation and instability can delay, reshape, and repeatedly reorganize contraction without by themselves resolving the finite-radius problem.

## What remains to close the radius

A genuine positive asymptotic core radius now requires at least one independently derived persistence mechanism, for example:

1. a constitutive stress/pressure law whose response stiffens before the support size reaches zero;
2. a lower bound on retained specific angular momentum \(J/M\);
3. a lower bound on the three-dimensional shape factor \(q\) together with bounded \(\kappa\);
4. an allowed energy/flux channel that changes the collapse dynamics without simply moving the rotational scale inward;
5. a standard-QM matter/energy scale that becomes dynamically relevant at sufficiently high density, if such a bridge can be supplied without postulating the desired radius.

The next audit should therefore stop trying to obtain the final radius from rotation alone and test the **constitutive/density closure** directly.

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
REPEATED\_REORGANIZATION\_CHANNEL\_IDENTIFIED /
ROTATIONAL\_FLOOR\_NOT\_SELF\_PERSISTING\_UNDER\_GENERIC\_J\_LOSS /
POSITIVE\_ASYMPTOTIC\_RADIUS\_REQUIRES\_ADDITIONAL\_CLOSURE}
}
\]

The accompanying script reports **14/14 PASS**.

## Reproducibility

```powershell
python audits/science/2026-09-14_dsd_gravity_repeated_reorganization_radius_floor_gate.py --mode all
```

## External comparators

- Paschalidis, V. & Stergioulas, N., *Rotating stars in relativity*, Living Reviews in Relativity 20, 7 (2017), DOI: 10.1007/s41114-017-0008-x.
- Basak, A., *Triaxial instabilities in rapidly rotating neutron stars*, MNRAS 477 (2018) 1383–1396, DOI: 10.1093/mnras/sty624.
