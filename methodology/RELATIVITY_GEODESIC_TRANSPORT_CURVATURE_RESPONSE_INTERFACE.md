# Relativity Geodesic / Transport / Curvature-Response Interface

Status: **REL Core 003 — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever DSD analysis handles worldlines, free-fall/geodesic claims, parallel transport, holonomy, or geodesic deviation inside a supplied standard Lorentzian geometry.

The interface prevents coordinate acceleration, generic DSD trajectory structure, and standard Levi-Civita geodesic dynamics from being silently identified.

## Required provenance

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Typical R2 supply for this interface:

```text
smooth Lorentzian metric
Levi-Civita connection
time orientation when needed
curve/worldline identity
initial point and tangent
parameterization convention
```

Typical R3 consequences:

```text
covariant acceleration
geodesic/autoparallel equation
parallel-transport equation
local geodesic existence/uniqueness
proper-time extremal characterization
curvature/holonomy response
geodesic-deviation equation
```

Do not count any R3 consequence as a generic DSD derivation of the R2 package.

## Core acceleration firewall

Never use

```text
d2x/dtau2 == 0
```

as the coordinate-independent geodesic criterion.

Use

\[
\nabla_u u=0,
\]

or in coordinates

\[
\frac{d^2x^\mu}{d\tau^2}
+
\Gamma^\mu{}_{\nu\rho}
\frac{dx^\nu}{d\tau}
\frac{dx^\rho}{d\tau}
=0.
\]

Required distinction:

```text
coordinate acceleration != covariant acceleration
```

Both counter-directions are possible:

```text
nonzero coordinate acceleration + zero covariant acceleration
zero coordinate acceleration + nonzero covariant acceleration
```

## Connection / curvature firewall

Keep distinct:

```text
connection coefficients
connection as geometric object
curvature tensor
```

A nonzero Christoffel symbol is not sufficient evidence of curvature.

```text
Gamma != 0  !=>  Riemann != 0
```

Likewise, a coordinate system can make connection coefficients vanish at a point without making curvature vanish there.

## Proper-time extremal gate

For a timelike curve,

\[
\tau[\gamma]
=
\int\sqrt{-g(u,u)}\,d\lambda.
\]

Before invoking the variational/geodesic relation, declare:

```text
metric
curve class
endpoint conditions
parameterization
variation class
local/global scope
```

Do not replace

```text
geodesic / stationary proper time
```

with

```text
unique global maximum in every spacetime.
```

## Parallel-transport gate

Parallel transport requires

```text
connection
path
initial tensor/vector
```

and satisfies

\[
\nabla_XV=0.
\]

Do not infer an endpoint comparison from endpoints alone.

Required test when path independence is claimed:

```text
compare transport along at least two admissible paths
or
prove the relevant flatness/holonomy condition.
```

## Holonomy / curvature-response gate

A closed-loop transport result is a loop- and connection-dependent object.

Keep distinct:

```text
one-point connection value
connection over loop neighborhood
loop identity/orientation
closed-loop holonomy
curvature over enclosed neighborhood
```

Do not promote a numerical holonomy from one supplied metric into a universal DSD invariant.

## Geodesic-deviation gate

For a geodesic family and deviation vector S, under a fixed Riemann-sign convention,

\[
\frac{D^2S^\mu}{D\tau^2}
=
R^\mu{}_{\nu\rho\sigma}u^\nu u^\rho S^\sigma.
\]

Declare the sign convention in any component calculation.

Required inputs:

```text
reference geodesic
neighboring geodesic family/congruence
deviation vector
curvature along reference geodesic
affine/proper-time parameter as applicable
```

Do not infer tidal/relative acceleration from one worldline's coordinate acceleration alone.

## DSD role mapping

```text
Formation:
  identity of spacetime model / path / worldline / endpoints

Property:
  metric / tangent / connection / curvature / acceleration /
  proper-time records with applicability status

Static Aggregation:
  optional summaries and readouts;
  no automatic recovery of full path/connection

Dynamics:
  trajectory / transition / lineage under a supplied dynamic law

Relativity specialization:
  Levi-Civita geodesic, parallel transport,
  holonomy and Jacobi/geodesic-deviation laws
```

## Mandatory non-identifications

```text
DSD trajectory != Levi-Civita geodesic
DSD lineage != causal/geodesic transport law
coordinate acceleration != covariant acceleration
Christoffel coefficient != curvature
same endpoints != same parallel transport
geodesic != universal global proper-time maximum
zero coordinate acceleration != zero tidal response
```

## Reconstruction checklist

For a claimed quantity, retain at least:

```text
GEODESIC TEST
  curve tangent + affine parameter + connection

PARALLEL TRANSPORT
  path + connection + initial transported object

HOLONOMY
  closed loop + connection over the loop neighborhood

GEODESIC DEVIATION
  geodesic family + deviation vector + curvature + parameterization
```

If any required datum is missing, report `NOT_SUFFICIENT_FOR_EXTENSION` rather than padding or guessing.

## Claim template

Preferred:

> Given a supplied Lorentzian metric and Levi-Civita connection, the standard geodesic/transport/curvature-response relation is represented in DSD with explicit curve, domain, applicability, and transition roles.

Do not write:

> DSD dynamics derives free fall or geodesic motion,

unless the metric, connection, and geodesic principle have themselves been independently derived from the generic DSD layer.

## Current closure

```text
coordinate-vs-covariant acceleration separated: YES
flat nonzero-Christoffel witness: YES
proper-time selected-variation witness: YES
curved path-dependent parallel-transport witness: YES
closed-loop holonomy witness: YES
FLRW geodesic-deviation witness: YES
DSD core revision required: NO
DSD-native geodesic principle derived: NO
```

Next gate:

```text
REL Core 004 — Einstein Field Equation / Constraint / Conservation / Initial-Value Gate
```
