# Relativity Ricci / Weyl / Vacuum / Source-Attribution Interface

## Status

Validated in **REL Extension 007** with `PASS_WITH_BOUNDARY`.

## Core separation

Keep distinct:

```text
Riemann tensor
Ricci tensor
Ricci scalar
Weyl tensor
Ricci-flat condition
physical vacuum T_ab=0
cosmological constant Lambda
Einstein field equation
stress-energy tensor
microscopic matter model
DSD supplied structural data
```

## Audit rule 1 — Ricci-flat is not flat

In 4D, exact rank-nullity gives

\[
\operatorname{rank}(Riemann\to Ricci)=10,
\qquad
\dim\ker=10.
\]

A nonzero element of this kernel is a Weyl-curvature countermodel.

Never infer

\[
R_{ab}=0\Rightarrow R_{abcd}=0.
\]

Use Schwarzschild exterior as the standard physical comparator when desired, but retain it as external GR input.

## Audit rule 2 — Weyl-flat is not flat

For constant sectional curvature,

\[
R_{abcd}=K(g_{ac}g_{bd}-g_{ad}g_{bc}),
\]

while in four dimensions

\[
C_{abcd}=0,
\quad
R_{ab}=3K g_{ab},
\quad
R=12K.
\]

Thus conformal/Weyl flatness does not imply Riemann flatness when \(K\neq0\).

## Audit rule 3 — qualify vacuum by Lambda convention

With

\[
G_{ab}+\Lambda g_{ab}=\kappa T_{ab},
\]

physical vacuum \(T_{ab}=0\) implies in 4D

\[
R_{ab}=\Lambda g_{ab}.
\]

Only the \(\Lambda=0\) vacuum convention is Ricci-flat.

Never use `vacuum = Ricci-flat` without recording the cosmological-constant convention.

## Audit rule 4 — fixed-observer vacuum tidal data are still partial

The 4D Ricci-flat/Weyl sector has ten algebraic degrees of freedom. The fixed-observer tidal map has rank five on this sector.

Therefore one observer's tracefree electric/tidal Weyl block is not the full Weyl tensor.

## Audit rule 5 — source inversion requires a supplied field equation

The equation

\[
T_{ab}=\kappa^{-1}(G_{ab}+\Lambda g_{ab})
\]

is legitimate only after Einstein dynamics, \(\kappa\), and \(\Lambda\) are supplied.

Do not infer a material source from curvature decomposition alone and then use that inferred source as evidence that Einstein dynamics was independently derived.

## Audit rule 6 — stress-energy is not microscopic matter identity

Even after \(T_{ab}\) is fixed, a unique matter field/Lagrangian/microphysical constitution does not follow without additional modeling assumptions.

Keep geometric source attribution separate from microscopic source identification.

## Audit rule 7 — preserve DSD provenance

Do not identify without an explicit bridge:

```text
DSD localization metric -> physical spacetime metric
DSD property aggregation -> Ricci contraction
DSD structural residual -> Weyl curvature
DSD dynamic operator -> Einstein dynamics
DSD c_info -> relativistic c
```

A standard GR decomposition performed on supplied spacetime data remains a conditional external specialization.

## Regression command

```bash
python audits/science/2026-09-10_rel_extension_007_ricci_weyl_matter_source_vacuum_curvature_gate.py --mode all
```

Validated result:

```text
TOTAL: 147/147 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

## Next interface

REL Extension 008 should audit scalar-invariant incompleteness, frame dependence, and local curvature classification, with nonflat VSI/pp-wave spacetimes as a candidate minimal comparator after external verification.
