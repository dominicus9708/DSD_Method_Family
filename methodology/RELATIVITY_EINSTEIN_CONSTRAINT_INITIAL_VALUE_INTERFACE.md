# Relativity Einstein / Constraint / Initial-Value Interface

Status: **REL Core 004 — PASS_WITH_BOUNDARY**

## Purpose

Use this interface whenever a DSD analysis invokes the Einstein field equation, stress-energy conservation, ADM/3+1 constraints, Cauchy data, or maximal globally hyperbolic development.

The interface prevents geometric constructions, constraint projections, conservation identities, and full Einstein-matter dynamics from being silently identified.

## Required provenance

```text
R0  PRE_EXISTING_DSD
R1  GENERAL_MATHEMATICAL_STRUCTURAL
R2  RELATIVITY_SPECIALIZATION
R3  STANDARD_THEOREM_CONSEQUENCE
R4  REMAINS_EXTERNAL_NOT_DERIVED
```

Typical R2 supply:

```text
Lorentzian metric
Levi-Civita geometry
Einstein field equation
kappa and Lambda when used
stress-energy model
3+1 split / hypersurface data
matter closure equations
gauge/reduction assumptions
constraint-satisfying initial data
boundary/asymptotic conditions when required
```

Typical R3 consequences:

```text
Einstein tensor from the supplied metric
contracted Bianchi identity
covariant conservation from EFE+Bianchi
Hamiltonian/momentum constraints as projections of EFE
standard Cauchy-development theorems
maximal globally hyperbolic development under theorem hypotheses
```

Do not count R3 results as evidence that the R2 Einstein dynamics was independently derived by DSD.

## Core field-equation firewall

Keep distinct:

```text
metric exists
Einstein tensor is defined
stress-energy tensor is supplied
Einstein equation is satisfied
```

Required relation:

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa T_{\mu\nu}.
\]

Operand existence does not imply relation satisfaction.

## Conservation firewall

The standard implication is:

```text
EFE
+ contracted Bianchi identity
+ metric compatibility
+ constant couplings
-> covariant stress-energy conservation
```

Never reverse this automatically.

```text
nabla_mu T^{mu nu} = 0
!=>
Einstein equation
```

A divergence-free stress tensor can fail the Einstein equation.

## Constraint gate

For a standard 3+1 convention:

\[
R^{(3)}+K^2-K_{ij}K^{ij}=16\pi G\,\rho+2\Lambda,
\]

\[
D_j(K^{ij}-h^{ij}K)=8\pi G\,j^i.
\]

Before calling data admissible, declare:

```text
spatial manifold
h_ij
K_ij
matter projections
couplings
sign convention
constraint equations
```

Typed availability of `h` and `K` is not constraint satisfaction.

## Constraint / evolution firewall

Required separation:

```text
initial slice
constraint equations
evolution equations
gauge conditions
matter closure
```

Constraint satisfaction is necessary initial-data structure for the standard Cauchy problem but does not license arbitrary off-shell spacetime extensions.

Do not write:

```text
constraints satisfied
therefore any extension is an Einstein solution
```

## Matter-closure gate

A stress-energy symbol does not close the matter dynamics.

Retain separately:

```text
matter variables
T_mu_nu construction
matter field equations / transport laws
constitutive relations / equation of state
coupling to geometry
```

If closure is absent, report the Einstein-matter system as incomplete for the intended evolution claim.

## Initial-value theorem gate

Before invoking a Cauchy-development theorem, retain:

```text
constraint-satisfying initial data
specified Einstein-matter system
regularity hypotheses
gauge/hyperbolic reduction as required by the theorem
geometric equivalence criterion
```

Maximal globally hyperbolic development is a geometric theorem conclusion under these hypotheses.

Do not translate geometric uniqueness into fixed-coordinate component identity.

## DSD constitutive-bridge firewall

Structural Reorganization Dynamics supplies a general typed constitutive-bridge interface, not a canonical Einstein operator.

Therefore:

```text
DSD Bdyn can host a supplied GR realization
!=
DSD Bdyn independently derives Einstein dynamics
```

Likewise, a conservation law in DSD Dynamics remains an additional model condition unless separately supplied or derived.

## DSD role mapping

```text
Formation:
  identity of model/components/channels

Property:
  typed metric, curvature, stress-energy,
  initial-data and matter records

Static Aggregation:
  optional reduced summaries;
  no automatic recovery of field-equation satisfaction

Dynamics:
  time-indexed states, transition/lineage,
  constitutive bridge and evolution when explicitly supplied

Relativity specialization:
  Einstein equation
  ADM/3+1 constraints
  matter closure
  standard Cauchy-development theorem
```

## Mandatory non-identifications

```text
geometry != field equation
Einstein tensor != Einstein-equation satisfaction
conservation != Einstein equation
constraint satisfaction != full evolution
stress-energy tensor != matter closure
one-slice data != arbitrary spacetime extension
geometric uniqueness != coordinate identity
DSD constitutive bridge != Einstein equation
```

## Reconstruction checklist

```text
EFE SATISFACTION
  G_mu_nu + Lambda g_mu_nu
  kappa T_mu_nu
  same domain / convention / units

CONSTRAINT SATISFACTION
  h_ij
  K_ij
  spatial curvature/derivatives
  matter projections
  convention and couplings

CAUCHY DEVELOPMENT
  admissible initial data
  full Einstein-matter evolution law
  matter closure
  theorem regularity/gauge hypotheses

GLOBAL CLAIM
  topology / boundary / asymptotic data
  extension criterion
  geometric equivalence criterion
```

Missing prerequisites must be reported explicitly rather than padded.

## Claim template

Preferred:

> Given a supplied Einstein-matter specialization satisfying the stated constraints and theorem hypotheses, DSD provides a typed interface for separating initial data, constraint relations, constitutive/evolution laws, conservation consequences, and geometric development.

Do not write:

> DSD derives Einstein dynamics,

unless the Einstein field equation and its physical coupling have themselves been independently derived from the generic DSD layer.

## Current closure

```text
geometry-vs-EFE separated: YES
conservation-vs-EFE separated: YES
constraint gate explicit: YES
same-slice/different-extension witness: YES
matter closure separated: YES
MGHD provenance locked: YES
DSD Bdyn/EFE identification rejected: YES
DSD core revision required: NO
DSD-native Einstein equation derived: NO
```

Next gate:

```text
REL Core 005 — Diffeomorphism / Gauge / Observable / Equivalence Gate
```
