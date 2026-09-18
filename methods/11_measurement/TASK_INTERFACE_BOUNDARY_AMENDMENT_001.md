# DSD Measurement Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**  
Date: **2026-09-19**

Historical input preserved:
- `TASK_INTERFACE_v0.1-draft.md`
- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

This amendment does not rewrite the historical Task Interface. It prospectively binds the refinements forced by the 18 pre-protocol boundary attacks.

## 1. Amendment purpose

The original interface correctly separated measurement selection from instrument design and experimental execution, but the boundary attacks showed that executable Measurement requires stronger locks around resolution, typed status, bridge provenance, joint discrimination, information loss, uncertainty, temporal availability, and neighboring-method handoffs.

The following eight refinement groups are therefore binding for Protocol v0.1.

## 2. R1 — discrimination question, alternatives, required distinctions, resolution

Every Measurement task must freeze before evaluation:

```text
DISCRIMINATION_QUESTION
ALTERNATIVE_SET_AND_IDENTITIES
REQUIRED_DISTINCTION_SET
DECLARED_DECISION_RESOLUTION
TASK_SCOPE
```

`REQUIRED_DISTINCTION_SET` is the set of alternative pairs or equivalence classes the task actually requires the measurement plan to separate.

A supplied first-branching record or structural-difference ledger may inform this set, but first branching is not itself a measurement readout and does not guarantee downstream discriminability.

```text
FIRST_BRANCHING_LOCATION != AUTOMATIC_READOUT_AVAILABILITY
STRUCTURAL_DIFFERENCE != GUARANTEED_MEASUREMENT_DIFFERENCE
```

The question, alternatives, required distinctions, or resolution may not be changed after candidate readout performance is inspected unless a new task version is opened.

## 3. R2 — measurement identity, typing, domain, unit, version, status

Each candidate measurement/readout must have a typed descriptor:

```text
MEASUREMENT_ID
MEASUREMENT_VERSION_IF_RELEVANT
READOUT_CARRIER_OR_TYPE
DECLARED_DOMAIN
UNIT_OR_REPRESENTATION
APPLICABILITY_SCOPE
STATUS_RECORD
```

When Property-layer statuses are supplied, the following remain distinct:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
```

The protocol may not silently convert any undefined/inapplicable state into numeric zero or a negative observation.

```text
DEFINED_ZERO != MISSING
UNDEFINED != ZERO
INAPPLICABLE != NEGATIVE_RESULT
PREREQUISITE_UNSATISFIED != NEGATIVE_RESULT
```

## 4. R3 — measurement-to-claim bridge, provenance, proxy/directness

Every candidate used for discrimination must have a supplied outcome/claim bridge or typed handoff identifying how alternative state constrains the readout.

The bridge ledger must record:

```text
BRIDGE_ID_AND_VERSION
BRIDGE_SOURCE_OR_HANDOFF
APPLICABILITY_SCOPE
DIRECT_OR_PROXY_ROLE
CLAIM_STRENGTH
MISSING_OR_CONFLICT_STATUS
```

No missing Prediction, Simulation, empirical-calibration, or domain-theory result may be generated inside Measurement.

```text
MISSING_PREDICTION_HANDOFF != NEGATIVE_PREDICTION
PROXY_MEASUREMENT != DIRECT_STRUCTURE_OBSERVATION
MEASUREMENT_TO_CLAIM_BRIDGE != SOURCE_FACT
```

If a required bridge is absent, the run records blockage or underdetermination according to the terminal rules rather than supplying an intuitive mapping.

## 5. R4 — pairwise and joint distinguishability ledger

For each candidate measurement `m` and alternative `H_i`, the task supplies an admissible outcome record `Y_m(H_i)` directly or through an explicit handoff.

After applying the frozen resolution/tolerance/decision relation, Measurement records pairwise status for every required pair:

```text
PAIRWISE_DISCRIMINATING
PAIRWISE_NONDISCRIMINATING
PAIRWISE_BLOCKED
PAIRWISE_UNDERDETERMINED
PAIRWISE_OUT_OF_SCOPE
```

For a declared measurement set `M={m1,...,mk}`, joint discrimination is evaluated on the supplied joint/product/signature semantics. It is not inferred from the member count.

```text
SINGLE_MEASUREMENT_INSUFFICIENCY != JOINT_MEASUREMENT_INSUFFICIENCY
JOINT_SUFFICIENCY != SINGLE_MEASUREMENT_SUFFICIENCY
MORE_MEASUREMENTS != MORE_DISCRIMINATING_INFORMATION
PAIRWISE_SUCCESS != COMPLETE_REQUIRED_COVERAGE
```

A plan is sufficient only relative to the frozen `REQUIRED_DISTINCTION_SET`.

## 6. R5 — readout collision, aggregation loss, injectivity, reconstruction

When a candidate readout is an aggregate, compressed output, transformed representation, or other reduced record, Measurement must retain any supplied information-loss and reconstruction sidecar.

At minimum the ledger distinguishes:

```text
READOUT_COLLISION_PRESENT_OR_ABSENT
INJECTIVITY_SCOPE
RECONSTRUCTION_SCOPE
SUPPORT_RETENTION_STATUS
AGGREGATION_OR_REDUCTION_HANDOFF
```

Guards:

```text
EQUAL_READOUT != EQUAL_STRUCTURE
EQUAL_AGGREGATE != EQUAL_SUPPORT
NONINJECTIVE_READOUT != RECONSTRUCTIVE_MEASUREMENT
GLOBAL_NONINJECTIVITY != FAILURE_TO_DISCRIMINATE_A_DECLARED_PAIR
DISCRIMINATING_READOUT != FULL_STRUCTURE_RECONSTRUCTION
```

Thus a globally noninjective readout may still distinguish a specific frozen alternative pair, while equal reduced readouts cannot be promoted to structural equality.

## 7. R6 — tolerance, uncertainty, threshold, decision semantics

Any claim of discrimination that depends on tolerance, uncertainty, confidence, threshold, equivalence class, or statistical decision semantics requires that rule to be frozen before scoring.

The protocol distinguishes:

```text
EXACT_DISJOINT_OUTCOME_CLASSES
TOLERANCE_DISJOINT_OUTCOME_CLASSES
DECISION_RULE_SUPPORTED_DISCRIMINATION
OVERLAPPING_OR_NONDISCRIMINATING
UNDERDETERMINED_DUE_TO_MISSING_DECISION_RULE
```

Measurement does not invent a statistical test, error budget, confidence level, calibration model, or domain-specific threshold.

```text
POST_HOC_THRESHOLD != PROSPECTIVE_DECISION_RULE
RAW_SEPARATION != CALIBRATED_DISCRIMINATION
UNSPECIFIED_TOLERANCE != LICENSE_TO_CHOOSE
```

## 8. R7 — temporal, regime, version, dynamic distinguishability support

When time, regime, propagation, or schema version is claim-relevant, the task must freeze:

```text
MEASUREMENT_TIME_OR_WINDOW
MEASUREMENT_LOCATION_IF_RELEVANT
ACTIVE_REGIME_OR_SCHEMA_VERSION
DYNAMIC_DISTINGUISHABILITY_SUPPORT_HANDOFF
TEMPORAL_BRIDGE_VERSION
```

A structural difference that exists upstream is not usable as a local discriminator before the supplied dynamic-support record makes that difference available at the measurement location/time.

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
SAME_READOUT_LABEL != SAME_SEMANTICS_ACROSS_REGIMES
TEMPORAL_ORDER != CAUSAL_BRIDGE
```

No universal propagation or causal law is introduced by this amendment.

## 9. R8 — neighboring-method handoffs and evidence/result separation

Measurement may consume explicit handoffs from:

```text
Analysis / Comparison
Specification
Design
Transformation
Aggregation / Compression
Prediction / Simulation
Diagnosis
Provenance / Lineage
Audit
domain-specific metrology or instrumentation
```

But consuming an artifact does not authorize Measurement to perform the neighboring method silently.

Required guards:

```text
MEASUREMENT_SELECTION != EXPERIMENTAL_EXECUTION
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
DISCRIMINATION_SUFFICIENCY != DIAGNOSIS
DISCRIMINATION_SUFFICIENCY != CAUSAL_PROOF
REQUIRED_SENSOR_CHARACTERISTIC != INSTRUMENT_DESIGN
PREDICTION_HANDOFF != MEASUREMENT_RESULT
SHARED_ARTIFACT != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
```

## 10. Prospective protocol obligations

Protocol v0.1 must therefore contain:

```text
question / alternative / required-distinction / resolution lock
typed candidate register
status preservation
bridge and provenance ledger
pairwise distinguishability matrix
joint-measurement rule
collision / information-loss / injectivity record
tolerance / uncertainty / decision-rule record
temporal / regime / dynamic-support record
neighboring-method handoff ledger
selection-vs-observation separation
candidate statuses
plan-level terminal statuses
conformance and method-gain records
```

## 11. Amendment result

```text
BOUNDARY_AMENDMENT_001: established
REFINEMENT_GROUPS_ADOPTED: 8/8
HISTORICAL_TASK_INTERFACE_REWRITTEN: no
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
PROTOCOL_FREEZE_AUTHORIZED: yes
EXTERNAL_APPLICATION: no
```

Next: freeze executable Measurement Protocol v0.1 from the historical Task Interface plus this amendment.
