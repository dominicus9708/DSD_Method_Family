# BH-RB-017 — Constitutive density-scale / causal-EOS gate

**Date:** 2026-09-14  
**Status:** `PASS_WITH_BOUNDARY / CAUSAL_CONSTITUTIVE_SCALE_IDENTIFIED / DIMENSIONFUL_MICROPHYSICAL_SCALE_REQUIRED / STATIC_CAUSAL_FLUID_DOES_NOT_CLOSE_TRAPPED_CORE / FINITE_DYNAMIC_CORE_RADIUS_NOT_DERIVED`

## Scope

BH-RB-016 showed that repeated rotational instability and reorganization do not by themselves preserve a positive radius floor when specific angular momentum can decrease from cycle to cycle.

This audit therefore asks the next narrower question:

> Can a causal pressure/stress equation of state itself select a positive finite radius without inserting the desired radius by hand?

The answer is split in two parts.

1. A causal constitutive law can supply a **radius scale** if it contains an independent dimensionful density/energy scale.
2. Causality and stiffness alone do **not** choose that scale, and the standard static causal-fluid branch remains outside an event horizon.

Thus a trapped dynamic successor-core radius is still not derived.

## Provenance boundary

The active DSD gravity rebaseline remains in force.

- Generic DSD does not provide a black-hole-core EOS.
- The Einstein/TOV equations are external standard-GR input.
- The EOS parameters used below are external constitutive parameters, not DSD constants.
- The TOV calculation is a **static, spherical, regular-star comparator** only.
- It is not identified with the interior of an already trapped black hole.
- No discarded pre-2026-09-11 structural-gravity radius expression is reused.

## Causal barotropic gate

For a one-parameter perfect fluid, write

\[
p=p(\varepsilon).
\]

The local adiabatic sound-speed condition is

\[
c_s^2=c^2\frac{dp}{d\varepsilon}.
\]

The causal control therefore requires

\[
0\le \frac{dp}{d\varepsilon}\le1
\]

in units where the ratio is dimensionless.

This inequality constrains **stiffness**, but it does not by itself introduce a density or length scale.

## Scale-free EOS does not choose an absolute constitutive radius

The linear EOS

\[
p=w\varepsilon,
\qquad 0<w\le1
\]

contains only the dimensionless parameter \(w\).

It has no independent density offset such as \(\varepsilon_0\), no particle mass, no interaction length, and no other constitutive scale.

Therefore a scale-free EOS can constrain dimensionless structure such as compactness only after boundary/initial data are supplied; it does not by itself create a new absolute microscopic radius.

In geometric units a similarity rescaling can change \(M\) and \(R\) together while preserving

\[
\frac{M}{R}.
\]

Hence stiffness is not the same object as a dimensional radius selector.

## Affine causal EOS introduces a constitutive scale

Use the standard causal linear control

\[
p=s(\varepsilon-\varepsilon_0),
\qquad 0<s\le1,
\]

where

\[
\frac{dp}{d\varepsilon}=s.
\]

The maximal-stiffness causal limit is

\[
s=1.
\]

Unlike \(p=w\varepsilon\), this EOS contains the dimensionful energy density \(\varepsilon_0\).

Let

\[
\rho_0=\frac{\varepsilon_0}{c^2}.
\]

Then the natural GR length scale is

\[
\boxed{
L_0
=
\frac{c^2}{\sqrt{G\varepsilon_0}}
=
\frac{c}{\sqrt{G\rho_0}}
}.
\]

The corresponding mass scale is

\[
M_0
=
\frac{c^2}{G}L_0.
\]

Therefore, for a fixed dimensionless TOV solution,

\[
\boxed{
R\propto\varepsilon_0^{-1/2},
\qquad
M\propto\varepsilon_0^{-1/2}.
}
\]

This is the first key closure result:

\[
\boxed{
\text{a constitutive density scale can generate a radius scale.}
}
\]

But it also exposes the missing input:

\[
\boxed{
\text{causality does not choose }\varepsilon_0.
}
\]

## Static TOV comparator

In geometrized units the standard TOV system is

\[
\frac{dm}{dr}=4\pi r^2\varepsilon,
\]

\[
\frac{dp}{dr}
=-
\frac{(\varepsilon+p)(m+4\pi r^3p)}
{r(r-2m)}.
\]

For

\[
p=s(\varepsilon-\varepsilon_0)
\]

introduce

\[
\bar p=\frac{p}{\varepsilon_0},
\qquad
\bar\varepsilon=\frac{\varepsilon}{\varepsilon_0},
\]

and scale \(r,m\) by \(L_0\).

The dimensionless equations no longer contain \(\varepsilon_0\).

That directly proves the \(\varepsilon_0^{-1/2}\) mass/radius scaling.

## Numerical TOV control

The accompanying script integrates the dimensionless TOV equations with a fourth-order Runge-Kutta method and scans the central-pressure family.

For several stiffness values, the first mass maximum is approximately:

| \(s=dp/d\varepsilon\) | \(p_c/\varepsilon_0\) | \(\bar M\) | \(\bar R\) | \(GM/(Rc^2)\) | \(R/r_s\) |
|---:|---:|---:|---:|---:|---:|
| 1/3 | 1.274 | 0.051685 | 0.190866 | 0.270790 | 1.846 |
| 0.5 | 1.497 | 0.064391 | 0.210510 | 0.305881 | 1.635 |
| 0.7 | 1.719 | 0.074748 | 0.225750 | 0.331110 | 1.510 |
| 1.0 | 2.021 | 0.085128 | 0.240509 | 0.353949 | 1.413 |

For the maximally stiff causal control,

\[
\boxed{
\frac{GM}{Rc^2}\simeq0.354
}
\]

and therefore

\[
\boxed{
R\simeq1.41\,r_s>r_s.
}
\]

Thus even this maximally stiff **static regular perfect-fluid comparator** does not become a finite material configuration inside its own event horizon.

This is consistent with the earlier BH-RB-008 conclusion that standard static support is not the branch to use for a core at or inside a trapped region.

## Synthetic density-scale demonstration

Choose only as a scale demonstration

\[
\rho_0=2.7\times10^{17}\ \mathrm{kg\,m^{-3}}.
\]

For the \(s=1\) maximum-mass dimensionless solution the script gives approximately

\[
M_{\max}\simeq4.071\,M_\odot,
\qquad
R\simeq16.985\ \mathrm{km}.
\]

If only the constitutive density scale is multiplied by four,

\[
\rho_0\rightarrow4\rho_0,
\]

then

\[
M\rightarrow\frac12M,
\qquad
R\rightarrow\frac12R.
\]

The compactness is unchanged.

These numbers are **not black-hole-core predictions**.  
They only demonstrate that the dimensional radius comes from the supplied constitutive density scale.

## Standard-QM implication

Standard quantum mechanics can in principle provide dimensionful constitutive data through a specified microscopic carrier: particle masses, number density, statistics, interaction scales, chemical potentials, phase transitions, and similar quantities.

But the active successor-core branch intentionally does not preserve ordinary precursor constituent identity.

Therefore standard QM alone does not yet supply a unique \(\varepsilon_0\) for the re-formed core.

An explicit microscopic/thermodynamic bridge is still required:

\[
\boxed{
\text{specified quantum degrees of freedom}
\longrightarrow
\text{EOS / transport coefficients}
\longrightarrow
\varepsilon_0,K,\ldots
\longrightarrow
\text{macroscopic length scale}.
}
\]

Without that bridge, inserting \(\varepsilon_0\) would merely replace an arbitrary radius with an arbitrary density scale.

## Relation to the dynamic core hypothesis

The present audit does **not** invalidate the dynamic finite-support branch.

It shows instead that

\[
\boxed{
\text{pressure stiffening}
\not\Rightarrow
\text{a universal trapped-core radius}.
}
\]

The static TOV branch remains horizonless, while the active black-hole-core hypothesis is explicitly non-equilibrium and trapped.

Therefore the next required calculation must use a dynamic constitutive law together with flux/transport and the causal/trapped-state constraints already established in BH-RB-009 through BH-RB-016.

## Main result

BH-RB-017 closes a major ambiguity in the radius problem.

A dimensional core radius cannot be produced merely by saying that the matter becomes "very stiff" at high density.

One must specify what physical scale makes it stiff:

\[
\boxed{
R_{\min}
\text{ requires a constitutive/microphysical scale, not stiffness alone.}
}
\]

And for ordinary static causal perfect-fluid support,

\[
\boxed{
R_{\rm static}>r_s,
}
\]

so that branch cannot itself furnish the desired trapped successor core.

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
CAUSAL\_CONSTITUTIVE\_SCALE\_IDENTIFIED /
DIMENSIONFUL\_MICROPHYSICAL\_SCALE\_REQUIRED /
STATIC\_CAUSAL\_FLUID\_DOES\_NOT\_CLOSE\_TRAPPED\_CORE /
FINITE\_DYNAMIC\_CORE\_RADIUS\_NOT\_DERIVED}
}
\]

The accompanying script reports **14/14 PASS**.

## Reproducibility

```powershell
python audits/science/2026-09-14_dsd_gravity_constitutive_density_scale_gate.py --mode all
```

## External comparators

- Rhoades, C. E. Jr. & Ruffini, R., *Maximum Mass of a Neutron Star*, Physical Review Letters **32**, 324 (1974), DOI: 10.1103/PhysRevLett.32.324.
- Lattimer, J. M. & Prakash, M., *Neutron Star Structure and the Equation of State*, Astrophysical Journal **550**, 426 (2001), arXiv:astro-ph/0002232.
- Van Oeveren, E. D. & Friedman, J. L., *Upper limit set by causality on the tidal deformability of a neutron star*, Physical Review D **95**, 083014 (2017), arXiv:1701.03797.
