# Operational Randomization and Ordered Carrier Interface

Status: reusable DSD Method Family interface  
Origin: QM Core Reconstruction 004D  
Scope: physical specializations that use probabilistic preparation mixing

## Purpose

This interface prevents a physical DSD specialization from treating convex mixtures, affine readouts, or affine transformations as automatic consequences of generic Formation, Property, Static Aggregation, or Structural Reorganization Dynamics.

## 1. Operational Randomization Declaration — ORD

Declare:

```text
PREPARATION_CARRIER
RANDOMIZER_WEIGHT_DOMAIN
RANDOMIZED_PREPARATION_OPERATION
RANDOMIZER_RECORD_RETAINED_OR_DISCARDED
READOUT_FAMILY
OPERATIONAL_EQUIVALENCE_RELATION
```

## 2. Operational Randomization Equivalence — ORE

If the randomizer record is discarded before the declared readout, require

\[
p(e|R_\lambda(P,Q))
=
\lambda p(e|P)+(1-\lambda)p(e|Q)
\]

for every declared readout effect \(e\).

Then preparation classes modulo complete readout equivalence inherit a convex operation.

## 3. Affine readout consequence

For every declared effect \(e\),

\[
e(\lambda\omega+(1-\lambda)\sigma)
=
\lambda e(\omega)+(1-\lambda)e(\sigma).
\]

This applies to operational probability readouts. It does not state that every DSD property value is affine.

## 4. Mixture-Preserving Transformation — MPT

A declared transformation \(T\) is mixture-preserving when

\[
T(R_\lambda(P,Q))
\sim
R_\lambda(TP,TQ).
\]

Then its induced action on operational state classes is affine.

## 5. Finite evaluation carrier

For a finite separating readout family \(e_1,\ldots,e_m\), embed

\[
\omega\mapsto(1,e_1(\omega),\ldots,e_m(\omega)).
\]

The span defines a finite-dimensional real carrier, the nonnegative hull defines a positive cone, and the first coordinate defines a normalization functional.

This construction supplies an ordered operational carrier without presupposing Hilbert geometry.

## 6. Firewalls

```text
Static Aggregation linearity != preparation convexity
convexity != no-restriction
state tomography != effect-domain completeness
operational mixing != Formation Clause VII finite composition
mixture-affine transformation != arbitrary DSD dynamics
```

## 7. Status

ORD/ORE/MPT are reusable declaration/consistency interfaces.

They are not universal DSD axioms and do not imply complex quantum theory.
