# Relativity Lorentzian Causal Geometry Interface

Status: **REL Core 002 — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever a DSD analysis stores, reduces, reconstructs, or dynamically uses Lorentzian metric and causal-geometry data.

The interface prevents three common collapses:

```text
carrier != metric
metric causal cone != chosen time orientation
pointwise metric != sufficient differential-geometric germ
```

## Provenance lock

Retain REL Core 001R classes:

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Treat as R2 unless independently proved otherwise:

```text
smooth spacetime manifold
spacetime dimension
Lorentzian signature
Lorentzian metric
time-orientability assumptions
chosen time orientation
specified worldline/curve for proper-time queries
```

Do not promote them to R0/R1 merely because DSD can store them.

## Local causal typing

For signature `(-,+,...,+)` and nonzero tangent vector `v`:

```text
g(v,v) < 0   TIMELIKE
g(v,v) = 0   NULL
g(v,v) > 0   SPACELIKE
```

Required input:

```text
point p
tangent vector v_p
Lorentzian point metric g_p
```

A manifold/vector record without `g_p` is insufficient for causal classification.

## Time-orientation rule

Keep separate:

```text
TIME_ORIENTABLE
CHOSEN_TIME_ORIENTATION
FUTURE_DIRECTED
PAST_DIRECTED
```

A Lorentzian metric may define timelike cone components without selecting which component is called future.

Never infer a unique future direction from the metric alone.

## Proper-time rule

For a timelike curve, proper time is a curve functional.

Required information includes:

```text
curve identity / parametrization or equivalent tangent data
metric along the curve
timelike applicability
integration interval
```

Do not reconstruct proper time from endpoints alone unless an additional theorem/optimization condition selects the curve.

## Differential-resolution ladder

Use the following default query gate:

```text
QUERY: tangent causal class at p
  point metric g_p: sufficient

QUERY: future/past label
  point metric alone: insufficient
  chosen time orientation: additionally required

QUERY: Levi-Civita connection at p
  point metric alone: insufficient
  sufficient first-order metric germ: required

QUERY: curvature at p
  metric + first derivative at p: insufficient in general
  sufficient second-order metric germ / connection derivative: required
```

## Levi-Civita rule

For a supplied smooth nondegenerate pseudo-Riemannian metric `g`, the standard theorem gives the unique connection satisfying

```text
TORSION_FREE
METRIC_COMPATIBLE
```

This is an R3 theorem consequence of R2 metric supply.

It is not a generic DSD construction.

## Curvature rule

Do not infer zero curvature from vanishing Christoffel symbols at one coordinate point.

Normal/local inertial coordinates may give

```text
g(p) = eta
partial g(p) = 0
Gamma(p) = 0
```

while second-derivative data and curvature remain nonzero.

## Reconstruction audit template

For a claimed target `q`, declare the retained record `f` and test

```text
f(x) = f(x')  =>  q(x) = q(x')
```

on the declared target domain.

Typical failure witnesses:

```text
same manifold + vector, different metrics -> different causal class
same metric, opposite time orientations -> opposite future/past label
same endpoints, different timelike curves -> different proper time
same point metric, different first derivatives -> different connection
same point metric + first derivatives, different second derivatives -> different curvature
```

## DSD placement

```text
Formation:
  identity / admission of represented records

Property:
  typed metric, vector, orientation, connection,
  curvature, proper-time records

Static Aggregation:
  optional reduced geometric readouts
  + explicit reconstruction test

Dynamics:
  only after a worldline/transport/metric-evolution law is supplied

Relativity specialization:
  Lorentzian geometry and standard differential-geometric theorem package
```

## Mandatory firewalls

```text
smooth manifold != Lorentzian metric
Lorentzian metric != unique time orientation
causal class != causal accessibility
coordinate time != proper time
endpoints != worldline
point metric != Levi-Civita connection
connection coefficient at one point != curvature
vanishing Christoffels at one point != flat spacetime
geometric representation != physical metric selection
relativistic causal cone != DSD c_info cone by vocabulary
```

## Current closure

REL Core 002 establishes:

```text
metric-relative causal classification: CONFIRMED
metric-alone future orientation: REJECTED
endpoint-only proper-time reconstruction: REJECTED
full smooth metric -> Levi-Civita connection: STANDARD R3
point metric -> connection: INSUFFICIENT
metric + first derivative at point -> curvature: INSUFFICIENT
Lorentzian metric independently derived from generic DSD: NO
DSD core revision required: NO
```

Next gate:

```text
REL Core 003 — Geodesic / Parallel-Transport / Curvature-Response Gate
```
