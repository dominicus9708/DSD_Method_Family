# Relativity Diffeomorphism / Gauge / Observable / Equivalence Interface

Status: **REL Core 005 — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever DSD analysis compares coordinate descriptions, active diffeomorphisms, isometries, gauge-related GR configurations, scalar/tensor readouts, relational observables, or global geometric equivalence.

The interface prevents five distinct relations from being collapsed:

```text
passive coordinate relabelling
active diffeomorphism pullback
isometry
GR gauge equivalence
DSD strict descriptive equivalence
```

## Provenance classes

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

## Mandatory representation firewall

For a passive coordinate change, compare the same geometric object in two charts.

Required data:

```text
underlying object
old chart
new chart
chart transition
component transformation rule
```

Do not infer physical information loss from changed coordinate components.

Preferred statement:

\[
\boxed{
\text{invertible representation change}
\neq
\text{physical information loss}.
}
\]

## Active diffeomorphism gate

For an active diffeomorphism \(\phi:M\to M\), the field configuration changes by pullback:

\[
\Psi\mapsto\phi^*\Psi.
\]

Keep distinct:

```text
same geometric object in a new chart
vs
pulled field configuration on the manifold
```

The mathematical formulas can look similar; the comparison target is different.

## Isometry gate

A diffeomorphism is an isometry only when

\[
\phi^*g=g.
\]

Therefore:

```text
diffeomorphism != isometry
```

unless this additional metric-preservation condition is verified.

## Scalar/tensor covariance gate

For a scalar built naturally from the metric,

\[
I[\phi^*g](p)=I[g](\phi(p)).
\]

Do not replace this by

\[
I[\phi^*g](p)=I[g](p)
\]

for arbitrary active \(\phi\).

For tensor components:

```text
component equality is chart-dependent
geometric tensor equality is not component equality
```

Retain chart/frame provenance for any component readout.

## GR gauge-equivalence gate

Before calling two diffeomorphism-related configurations physically gauge-equivalent, declare:

```text
full target-theory field tuple
admissible diffeomorphism class
simultaneous pullback rule
boundary/asymptotic conditions
whether the transformation is gauge-trivial or acts on physical boundary data
```

Do not use the unrestricted shortcut:

```text
every diffeomorphism = physically trivial gauge transformation
```

Boundary/asymptotic transformations may require a separate charge/symmetry analysis.

## Relational-observable gate

A coordinate-labelled local value is not automatically gauge-invariant.

If a relational observable is claimed, require an explicit rule such as:

```text
reference field(s)
clock/rod condition
dressing/reference-frame construction
domain where the reference is valid
proof/check of invariance under the declared gauge action
```

DSD may store and type these records; it does not supply the physical relational reference system by default.

## Local-vs-global geometry gate

Never infer global equivalence from only:

```text
same local dimension
same selected scalar curvature
same finite list of local scalar invariants
same local chart form
```

Global targets may require:

```text
topology
global causal structure
boundary/asymptotic structure
global metric/field map
global regularity
isometry/diffeomorphism witness
```

If these are absent, report:

```text
NOT_SUFFICIENT_FOR_EXTENSION
```

rather than global equivalence.

## DSD strict-equivalence firewall

Formation strict descriptive equivalence is a base-fixed formation isomorphism over the complete candidate-level formation descriptor.

It therefore retains requirements not present in the ordinary GR gauge predicate:

```text
candidate expressions/configurations
unsuccessful candidates
base fixing
full formation structure
presentation-sensitive preservation
```

GR diffeomorphism/gauge equivalence instead acts on target-theory spacetime fields.

Mandatory non-identification:

\[
\boxed{
\sim_{\mathrm{DSD,strict}}
\neq
\sim_{\mathrm{GR,gauge}}.
}
\]

A bridge between them is allowed only if an application defines it explicitly and proves compatibility on a declared restricted domain.

## DSD role mapping

```text
Formation:
  identity of model / representation / map / candidate-level structure
  strict descriptive equivalence

Property:
  typed metric / tensor / scalar / reference-field / gauge-status records

Static Aggregation:
  coordinate or invariant readouts
  reconstruction only under explicit support/injectivity conditions

Dynamics:
  time-indexed field/trajectory data under supplied constitutive rules

Relativity specialization:
  Lorentzian geometry
  diffeomorphism action
  GR gauge interpretation
  boundary/asymptotic convention
  relational-observable construction
```

## Mandatory non-identifications

```text
coordinate change != active diffeomorphism
active diffeomorphism != isometry
tensor component != geometric tensor
coordinate scalar value != automatically gauge-invariant observable
diffeomorphism covariance != unrestricted gauge triviality
local invariant agreement != global geometric equivalence
GR gauge equivalence != DSD strict descriptive equivalence
```

## Reconstruction checklist

```text
PASSIVE REPRESENTATION
  chart pair
  transition map
  transformed components
  invariant/geometric comparison target

ACTIVE PULLBACK
  diffeomorphism
  complete field tuple
  pullback action

ISOMETRY
  diffeomorphism
  metric
  proof/check phi^*g = g

GR GAUGE EQUIVALENCE
  complete fields
  admissible diffeomorphism
  gauge convention
  boundary/asymptotic conditions

RELATIONAL OBSERVABLE
  gauge action
  reference/dressing data
  applicability domain
  invariant readout

GLOBAL EQUIVALENCE
  global manifold
  topology
  global field structure
  global map

DSD STRICT EQUIVALENCE
  full formation descriptors
  base-fixing data
  strict formation-isomorphism witness
```

## Preferred claim form

Preferred:

> Given a supplied GR spacetime and declared diffeomorphism/gauge convention, DSD can keep representation, active pullback, isometry, gauge orbit, relational readout, and strict DSD equivalence as separately typed comparison roles.

Do not write:

> DSD strict descriptive equivalence is the same as diffeomorphism invariance.

Do not write:

> A coordinate-independent scalar is automatically a complete GR observable.

Do not write:

> Any diffeomorphism is physically trivial.

## Current closure

```text
passive-vs-active distinction: CLOSED
diffeomorphism-vs-isometry distinction: CLOSED
scalar covariance vs same-point invariance: CLOSED
component vs invariant distinction: CLOSED
local-vs-global equivalence firewall: CLOSED
GR gauge vs DSD strict-equivalence firewall: CLOSED

preferred relational observable from generic DSD: NOT DERIVED
complete global GR observable algebra: NOT DERIVED
boundary/asymptotic gauge classification: NOT UNIVERSALLY FIXED
DSD-native diffeomorphism principle: NOT DERIVED
```

Next gate:

```text
REL Core 006 — Linearized Gravity / Gauge Perturbation / Radiative-Degree Gate
```
