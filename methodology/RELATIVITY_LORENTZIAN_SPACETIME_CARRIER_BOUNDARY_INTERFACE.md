# Relativity Lorentzian Spacetime Carrier Boundary Interface

Status: **ACTIVE — REL Extension 001 PASS_WITH_BOUNDARY**

## Purpose

Prevent a successful DSD representation or reconstruction of standard relativity from being reclassified as an independent derivation of the Lorentzian spacetime carrier.

Keep the following layers separate:

```text
generic DSD
general mathematical / differential-geometric structure
relativity selector / specialization
Lorentzian spacetime comparator
Einstein dynamics
```

## Existing DSD contribution

Generic DSD supplies typed status, applicability/prerequisites, explicit bridge discipline, reconstruction/equivalence distinctions, and separated Formation/Property/Static/Dynamics layers.

The current dynamics paper permits geometric and propagation specializations but does not make one localization carrier, metric, physical propagation constant, or constitutive law universal.

Therefore do not infer a Lorentzian spacetime metric from the existence of a DSD carrier or dynamic interface.

## Carrier/signature firewall

The same real carrier can support different nondegenerate signatures. In particular, \(\mathbb R^n\) for several dimensions supports both Euclidean and Lorentzian diagonal metrics.

Boundary rules:

```text
carrier != metric
carrier dimension != metric signature
Lorentzian admissibility != selection of 3+1 dimensions
metric existence != Einstein dynamics
```

## Causal firewall

Causal classification depends on the supplied Lorentzian metric. Future/past orientation additionally requires a time-orientation choice where applicable.

```text
carrier + tangent vector != causal class
Lorentzian metric alone != unique future direction
```

## Null-scale firewall

A bare carrier does not select the physical normalization of a relativistic invariant speed.

Do not infer:

```text
generic DSD -> numerical value of c
```

and do not identify

```text
c_info = relativistic c
```

without an explicit physical/constitutive bridge and an independent equivalence argument.

## Einstein-dynamics firewall

Lorentzian geometry alone does not impose the Einstein field equation.

```text
Lorentzian metric != Einstein equation
covariant conservation alone != Einstein equation
constitutive-bridge interface != Einstein equation by itself
```

## Provenance rule

Retain the REL Core provenance classes:

```text
R0 PRE_EXISTING_DSD
R1 GENERAL_MATHEMATICAL_STRUCTURAL
R2 RELATIVITY_SPECIALIZATION
R3 STANDARD_THEOREM_CONSEQUENCE
R4 REMAINS_EXTERNAL_NOT_DERIVED
```

The physical Lorentzian spacetime carrier, physical spacetime dimension/signature, relativistic normalization of \(c\), and Einstein dynamics remain R2/R4-side structure at the present stage.

## Allowed claim

```text
DSD conditionally reconstructs a broad ordinary classical standard-relativity slice
once the required Lorentzian and Einstein structures are explicitly supplied,
while preserving their provenance as target-specific inputs.
```

Do not claim:

```text
generic DSD independently derives physical Lorentzian spacetime or Einstein dynamics.
```

## Regression witness

```bash
python audits/science/2026-09-10_rel_extension_001_lorentzian_spacetime_carrier_independent_origin_boundary_gate.py --mode all
```

Expected status:

```text
TOTAL: 36/36 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

## Next interface

Proceed to **REL Extension 002 — Relativity Reconstruction Selectors / Causal–Projective–Metric Recovery Gate**.

That gate should test how much relativistic geometry can be recovered from explicitly declared causal/light-ray and free-fall/projective information, while preserving premise provenance and refusing to treat comparator assumptions as generic-DSD outputs.
