# Relativity Causal–Projective–Metric Recovery Interface

Status: **ACTIVE — REL Extension 002 PASS_WITH_BOUNDARY**

## Purpose

Define the selector/provenance discipline for reconstructing relativistic geometry from weaker observational or geometric inputs without silently supplying the full physical metric at the beginning.

Keep separate:

```text
light-ray data
free-fall path data
conformal structure
projective structure
Weyl-compatible structure
metric scale / pseudo-Riemannian representative
Einstein dynamics
```

## Selector ladder

Use the following as the working reconstruction ladder, not as generic DSD theorems:

```text
light propagation data
  -> conformal/light-cone information under declared assumptions

free-fall trajectory data
  -> projective information under declared connection assumptions

conformal + projective + compatibility
  -> Weyl-compatible structure under an applicable external theorem

Weyl structure + integrability/clock-scale conditions
  -> pseudo-Riemannian metric representative where justified
```

Every arrow must retain theorem hypotheses and provenance.

## Conformal firewall

Positive conformal rescaling preserves null cones and causal signs but changes metric scale.

```text
light cone != metric scale
causal class != calibrated proper time
conformal class != unique metric representative
```

## Projective firewall

For torsion-free affine representatives,

\[
\Gamma'^i{}_{jk}=\Gamma^i{}_{jk}+\delta^i_j\psi_k+\delta^i_k\psi_j
\]

preserves unparameterized geodesics.

```text
free-fall path family != unique affine connection
unparameterized geodesic != affine parameter
DSD lineage != projective geodesic by default
```

## Compatibility firewall

Conformal preservation of null geodesics does not by itself fix timelike projective structure.

The Matveev–Scholz theorem may be used as an external comparator in its stated n >= 3 indefinite-signature setting: light-cone compatible conformal and projective structures are Weyl compatible.

Do not erase its hypotheses or back-count them as DSD outputs.

## Modern-assumption caveat

The EPS reconstruction program is not treated as assumption-free. Modern analysis has emphasized restrictions on the connection class and conformal representation used in the standard derivation.

Therefore record separately:

```text
torsion-free affine assumption
reparameterization class
connection representation
regularity and dimensional assumptions
light-cone compatibility
```

A result obtained only after these assumptions remains conditional.

## Weyl-integrability firewall

A Weyl-compatible structure does not automatically supply a globally removable scale connection.

```text
Weyl compatibility != integrability
closed 1-form != globally exact 1-form in every topology
local Riemannian gauge != guaranteed global gauge
```

Chronometric or integrability conditions used to select metric scale must be given explicit provenance.

## DSD provenance

Use the established relativity classes:

```text
R0 PRE_EXISTING_DSD
R1 GENERAL_MATHEMATICAL_STRUCTURAL
R2 RELATIVITY_SPECIALIZATION / SELECTOR
R3 STANDARD_THEOREM_CONSEQUENCE
R4 REMAINS_EXTERNAL_NOT_DERIVED
```

Observed light rays, observed free-fall trajectories, conformal/projective equivalence rules, compatibility assumptions, clock calibration, and Einstein dynamics are not promoted to R0 solely because DSD can represent them.

## Regression witness

```bash
python audits/science/2026-09-10_rel_extension_002_causal_projective_metric_recovery_gate.py --mode all
```

Expected result:

```text
TOTAL: 43/43 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

## Allowed claim

```text
DSD can host a provenance-preserving conditional reconstruction audit in which
light-ray and free-fall selectors are compared with standard conformal/projective
spacetime reconstruction results.
```

Do not claim:

```text
observed paths alone uniquely force the complete physical metric without assumptions;
generic DSD independently derives the EPS selector premises;
kinematical reconstruction derives the Einstein field equation.
```

## Next interface

Proceed to **REL Extension 003 — Clock / Weyl Integrability / Metric-Scale Recovery Gate**.
