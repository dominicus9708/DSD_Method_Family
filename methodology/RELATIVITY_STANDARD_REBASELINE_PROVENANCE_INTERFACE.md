# Standard Relativity Rebaseline Provenance Interface

Status: **REL Core 001R — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever a DSD analysis claims to reconstruct, compare, or organize a standard-relativity object.

The interface prevents a supplied relativistic structure from being counted retroactively as an independent DSD consequence.

## Provenance classes

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Only R0/R1 count as target-independent evidence.

## R0 baseline

```text
typed status / applicability
explicit bridge discipline
readout / reconstruction discipline
strict-equivalence firewall
state / relation / transition separation
```

## R1 baseline

```text
invertible representation change is not loss by itself
equal dimension/cardinality does not identify typed carriers
state data do not select an evolution law
fiber/factorization reconstruction criterion
passive re-description != active transition
```

## R2 supplied relativity package

At minimum, declare which of the following are being supplied:

```text
smooth spacetime manifold
spacetime dimension
Lorentzian signature
Lorentzian metric
time orientation
matter / stress-energy model
Einstein field equation
initial data / constraints
boundary or asymptotic conditions
weak-field or other approximation regime
```

Do not mark any of these as R0/R1 merely because DSD can store or type them.

## R3 theorem-consequence examples

Under the required R2 hypotheses:

```text
metric -> Levi-Civita connection
metric + orientation -> causal cone/future-past structure
metric + timelike curve -> proper time
metric + connection -> curvature
Lorentz action in Minkowski specialization -> interval/causal-class invariance
EFE + contracted Bianchi + metric compatibility -> local covariant conservation
constraint-satisfying Einstein initial data -> standard maximal globally hyperbolic development
weak-field specialization -> first-order proper-time relation
```

Always record theorem hypotheses. Do not export a conditional consequence outside its domain.

## R4 mandatory unresolved/external registry

Keep explicit when relevant:

```text
origin of 4D spacetime
origin of Lorentzian signature
origin/selection of Einstein dynamics
numerical constants G, c, Lambda
actual matter content / topology / boundary conditions / initial data
c_info vs relativistic c
GR equivalence vs DSD strict equivalence
QM-GR cross-dynamics
```

## Required firewalls

```text
coordinate representation != causal accessibility
coordinate-time order != causal lineage
chart coverage != global spacetime coverage
proper time != coordinate time
state operands != field equation satisfaction
metric value at a point != curvature
covariant conservation != Einstein equation
spacetime dimension != DSD channel/rank count
relativistic light cone != DSD c_info by vocabulary
GR diffeomorphism/isometry equivalence != DSD strict equivalence without proof
standard QM + standard relativity != unique cross-dynamics
```

## Reconstruction rule

For any claimed recovered quantity `q` from record/readout `f`, test whether

```text
f(x) = f(x')  =>  q(x) = q(x')
```

on the declared target domain.

A valid domain-restricted description can be sufficient for a local query while remaining insufficient for global reconstruction.

## Dynamic rule

Record separately:

```text
one-slice state
standard-domain relations / constraints
evolution or development law
domain of dependence
equivalence/gauge criterion
reconstruction target
```

One-slice data alone do not derive the evolution law.

## Claim template

Preferred:

> Given the supplied standard-relativity specialization X and theorem hypotheses Y, DSD provides a typed/reconstruction interface in which consequence Z is represented and audited without conflating representation, access, state, relation, transition, or reconstruction roles.

Do not write:

> DSD derives general relativity,

unless the Lorentzian/geometric/dynamical R2 package has itself been independently derived from R0/R1 under a proved chain.

## Current closure

REL Core 001R establishes:

```text
PHY-REL-001–007 provenance reclassified: YES
prior standard-relativity results invalidated: NO
DSD core contradiction found: NO
DSD core revision required: NO
Lorentzian metric independently derived: NO
Einstein field equation independently derived: NO
```

Next gate:

```text
REL Core 002 — Lorentzian Metric / Causal Geometry Admission and Reconstruction Gate
```
