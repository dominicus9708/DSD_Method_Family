# DSD Measurement Boundary Counterexamples v0.1 — pre-protocol attack record

Status: **18 pre-protocol boundary attacks completed**  
Date: **2026-09-18**

Purpose: pressure the Measurement Task Interface before protocol freeze. These are constructed internal counterexamples, not external-domain validation.

## Results summary

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 9
PRESERVED_WITH_NONBREAKING_REFINEMENT: 9
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

## Attack ledger

### B1 — equal readout, different structure

Two alternatives have different component/support structure but the candidate readout gives the same scalar value.

Required:
```text
EQUAL_READOUT != EQUAL_STRUCTURE
MEASURABLE != DISCRIMINATING
```

Outcome: preserved; supports R5.

### B2 — defined zero versus missing

Alternative A produces a defined readout 0. Alternative B has no available datum.

Required: zero and missing remain distinct.

Outcome: **refinement R2**.

### B3 — applicable but undefined versus inapplicable

One candidate is applicable but its value is undefined; another candidate is not applicable to the supplied object.

Required: do not collapse both into “no measurement”.

Outcome: **refinement R2**.

### B4 — missing measurement-to-claim bridge

A sensor/readout value is well defined, but no supplied bridge connects it to the structural alternatives in the question.

Required: candidate is blocked/underdetermined for discrimination rather than interpreted by intuition.

Outcome: **refinement R3**.

### B5 — resolution mismatch

A readout distinguishes alternatives only below a finer scale than the declared measurement resolution.

Required: discrimination must be evaluated at the locked task resolution.

Outcome: **refinement R1**.

### B6 — downstream aggregate collision after first branching

Two alternatives first branch structurally, then later produce the same aggregate readout.

Required: first branching locates a structural distinction but does not guarantee every downstream readout preserves it.

Outcome: preserved; supports R5.

### B7 — one measurement separates only one pair

For alternatives {A,B,C}, candidate m separates A from B but cannot separate B from C.

Required: pairwise success must not be generalized to complete discrimination.

Outcome: **refinement R4**.

### B8 — two individually weak measurements jointly discriminate

m1 separates {A} from {B,C}; m2 separates {B} from {A,C}. Their joint signature distinguishes all three.

Required:
```text
SINGLE_MEASUREMENT_INSUFFICIENCY != JOINT_MEASUREMENT_INSUFFICIENCY
```

Outcome: **refinement R4**.

### B9 — redundant second measurement

m2 is a deterministic copy of m1 at the declared resolution.

Required: additional measurement count does not imply additional discrimination.

Outcome: preserved.

### B10 — aggregate readout loses support

An Aggregation handoff returns the same sum for two distinct support sets.

Required: equal aggregate cannot be treated as reconstructive measurement without injectivity/reconstruction support.

Outcome: preserved; supports R5.

### B11 — uncertainty/tolerance unspecified

Predicted/supplied outcome intervals overlap or separate depending on an unspecified tolerance rule.

Required: discrimination status is underdetermined rather than choosing a threshold post hoc.

Outcome: **refinement R6**.

### B12 — threshold changed after seeing outcome

A candidate only “discriminates” after the acceptance threshold is moved to fit the observed/readout value.

Required: threshold/tolerance semantics must be frozen prospectively.

Outcome: preserved; supports R6.

### B13 — dynamic difference has not reached the observer

A structural perturbation exists upstream but the supplied dynamic-support record says its distinguishability support has not yet reached the measurement location/time.

Required:
```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
```

Outcome: **refinement R7**.

### B14 — same readout label across regime change

A quantity label is unchanged at t0 and t1, but its active bridge or schema meaning changes.

Required: time/regime/version scope must be explicit.

Outcome: **refinement R7**.

### B15 — instrument design substituted for measurement analysis

The task asks which physical sensor architecture to build, but only discrimination requirements are supplied.

Required: Measurement may state required discrimination characteristics; actual device architecture belongs to Design/domain instrumentation handoff.

Outcome: preserved; supports R8.

### B16 — diagnosis substituted for measurement sufficiency

A readout can distinguish disease/state classes under a supplied bridge, and the run jumps to a causal diagnosis.

Required: discrimination sufficiency does not itself establish diagnosis or cause.

Outcome: preserved; supports R8.

### B17 — missing prediction handoff silently generated

The measurement question requires expected outcome sets for alternatives, but no Prediction/Simulation handoff is supplied.

Required: Measurement does not invent those expected outcomes.

Outcome: **refinement R8**.

### B18 — selected measurement treated as observed result

The method identifies candidate m as sufficient, then downstream text writes “m observed value v”.

Required:
```text
MEASUREMENT_SELECTION != EXPERIMENTAL_EXECUTION
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
```

Outcome: **refinement R8**.

## Refinement groups forced

```text
R1 discrimination question / alternative set / declared decision resolution
R2 measurement identity / typing / domain / unit / property-status preservation
R3 measurement-to-claim bridge / provenance / proxy-vs-direct record
R4 pairwise and joint distinguishability / outcome-partition ledger
R5 readout collision / aggregation loss / injectivity / reconstruction limits
R6 tolerance / uncertainty / decision-threshold semantics
R7 temporal / regime / dynamic distinguishability-support scope
R8 neighboring-method handoffs / measurement-selection-vs-observed-result separation
```

No attack requires collapsing Measurement into Design, Specification, Aggregation, Comparison, Diagnosis, Prediction, Simulation, Provenance, or Audit.

The historical Task Interface remains unchanged. R1-R8 are to be added prospectively through Boundary Amendment 001.
