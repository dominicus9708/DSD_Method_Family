# DSD Measurement Task Interface v0.1 — historical draft

Status: **historical draft / preserved**  
Date: **2026-09-18**

## 1. Task identity

DSD Measurement receives a declared discrimination question, a finite or otherwise explicitly bounded alternative set, a target resolution, and supplied candidate observations/readouts with their applicability and measurement-to-claim mappings. It returns a trace of which measurements or measurement sets can distinguish the alternatives at that resolution, which cannot, and why.

The method asks what evidence/readout is discriminating under supplied structural and bridge information. It does not infer an unavailable readout map, fabricate an instrument, or turn a selected measurement into an observed result.

## 2. Inputs

Required inputs:

```text
MEASUREMENT_TASK_ID
DISCRIMINATION_QUESTION
ALTERNATIVE_OR_CANDIDATE_SET
DECLARED_DECISION_RESOLUTION
CLAIM_RELEVANT_STRUCTURAL_DIFFERENCE_SET
CANDIDATE_MEASUREMENT_OR_READOUT_SET
MEASUREMENT_IDENTITY_TYPE_DOMAIN_AND_UNIT
MEASUREMENT_APPLICABILITY_AND_STATUS_RECORD
MEASUREMENT_TO_ALTERNATIVE_OUTCOME_MAP_OR_BRIDGE
MAPPING_OR_BRIDGE_PROVENANCE
```

Conditionally required:

```text
TOLERANCE_OR_EQUIVALENCE_RELATION
UNCERTAINTY_OR_ERROR_MODEL
JOINT_MEASUREMENT_POLICY
AGGREGATE_OR_SUMMARY_READOUT_HANDOFF
RECONSTRUCTION_OR_INJECTIVITY_RECORD
TEMPORAL_WINDOW_AND_REGIME_SCOPE
DYNAMIC_DISTINGUISHABILITY_SUPPORT_HANDOFF
PREDICTION_OR_SIMULATION_HANDOFF
PROXY_MEASUREMENT_POLICY
NEIGHBORING_METHOD_HANDOFFS
```

If a required claim-relevant map, bridge, status, or tolerance is absent, the method must preserve the resulting limitation rather than invent it.

## 3. Binding operation

Measurement must:

```text
1 lock the discrimination question, alternatives, and declared resolution;
2 lock candidate measurement identity, type, domain, unit, and version where relevant;
3 identify which structural differences are claim-relevant to the declared question;
4 evaluate measurement applicability before using a candidate readout;
5 preserve undeclared/unavailable/inapplicable/prerequisite-unsatisfied/
  applicable-but-undefined/defined-zero/defined-nonzero distinctions when supplied;
6 apply only supplied measurement-to-alternative outcome maps or explicit bridges;
7 determine pairwise discrimination at the declared tolerance/resolution;
8 determine joint-measurement discrimination separately from single-measurement discrimination;
9 record readout collisions, aggregation loss, and noninjective mappings;
10 keep proxy evidence distinct from direct structural observation;
11 preserve temporal/regime scope and dynamic distinguishability availability;
12 preserve missing prediction/simulation information as a handoff limitation;
13 keep measurement-selection evidence distinct from an actually observed measurement result;
14 emit candidate-level statuses, plan-level terminal status, and conformance record.
```

## 4. Candidate measurement status family

```text
MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
MEASUREMENT_PARTIALLY_DISCRIMINATES
MEASUREMENT_NONDISCRIMINATING
MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
MEASUREMENT_INAPPLICABLE
MEASUREMENT_OUT_OF_SCOPE
MEASUREMENT_UNDERDETERMINED
```

A candidate may be applicable yet nondiscriminating. This is not protocol failure.

## 5. Plan-level terminal status family

```text
MEASUREMENT_PLAN_SUFFICIENT
MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
MEASUREMENT_PLAN_INSUFFICIENT
MEASUREMENT_PLAN_BLOCKED
MEASUREMENT_PLAN_OUT_OF_SCOPE
MEASUREMENT_PLAN_UNDERDETERMINED
```

A plan-level status is distinct from protocol conformance and distinct from the truth of any alternative.

## 6. Distinguishability record

For measurement candidate `m` and alternative `H_i`, let the supplied outcome-set record be `Y_m(H_i)`. This notation is an interface record, not a new DSD axiom.

At the declared tolerance/equivalence relation `~_m`:

```text
PAIRWISE_DISCRIMINATING(m, H_i, H_j)
  only when the supplied admissible outcome classes for H_i and H_j are disjoint at the declared resolution.

PAIRWISE_NONDISCRIMINATING
  when at least one admissible outcome class is shared.

PAIRWISE_UNDERDETERMINED
  when the supplied map/bridge/tolerance is insufficient to decide.
```

For a declared joint set `M={m1,...,mk}`, joint discrimination is evaluated on the supplied product/signature record. Joint sufficiency must not be inferred from any one member alone.

## 7. Outputs

```text
LOCKED_DISCRIMINATION_QUESTION_AND_RESOLUTION
ALTERNATIVE_DIFFERENCE_LEDGER
MEASUREMENT_CANDIDATE_REGISTER
MEASUREMENT_STATUS_LEDGER
PAIRWISE_DISTINGUISHABILITY_MATRIX
JOINT_MEASUREMENT_DISTINGUISHABILITY_RECORD
READOUT_COLLISION_AND_INFORMATION_LOSS_LEDGER
MEASUREMENT_TO_CLAIM_BRIDGE_LEDGER
PROXY_OR_DIRECTNESS_LEDGER
TEMPORAL_REGIME_AND_DYNAMIC_SUPPORT_LEDGER
MEASUREMENT_PLAN_TERMINAL_STATUS
MEASUREMENT_PROTOCOL_CONFORMANCE
MEASUREMENT_METHOD_GAIN_STATUS
```

## 8. Core guards

```text
MEASURABLE != DISCRIMINATING
DEFINED_ZERO != MISSING
UNDEFINED != ZERO
INAPPLICABLE != NEGATIVE_RESULT
EQUAL_READOUT != EQUAL_STRUCTURE
EQUAL_AGGREGATE != EQUAL_SUPPORT
NONINJECTIVE_READOUT != RECONSTRUCTIVE_MEASUREMENT
SINGLE_MEASUREMENT_INSUFFICIENCY != JOINT_MEASUREMENT_INSUFFICIENCY
JOINT_SUFFICIENCY != SINGLE_MEASUREMENT_SUFFICIENCY
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
MEASUREMENT_SELECTION != EXPERIMENTAL_EXECUTION
PROXY_MEASUREMENT != DIRECT_STRUCTURE_OBSERVATION
TEMPORAL_ORDER != CAUSAL_BRIDGE
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
FIRST_BRANCHING_LOCATION != AUTOMATIC_READOUT_AVAILABILITY
MISSING_PREDICTION_HANDOFF != NEGATIVE_PREDICTION
```

## 9. Failure / no-gain criteria

Protocol nonconformance includes:

```text
changing alternatives or resolution after seeing a preferred measurement;
using an inapplicable or undefined readout as if observed;
collapsing missing/undefined/zero when claim-relevant;
claiming discrimination from equal/noninjective aggregate readouts;
inventing a measurement-to-claim bridge;
silently importing a prediction, diagnosis, or causal model;
treating a not-yet-arrived dynamic distinction as negative evidence;
treating a proxy as direct observation without provenance;
declaring an observed result merely because a measurement was selected;
generalizing pairwise or partial discrimination to complete discrimination.
```

`NO_GAIN` is allowed when a fair non-DSD distinguishability evaluator receiving the same alternatives, measurement maps, status records, tolerance, provenance, and temporal information produces the same claim-relevant output.

```text
NO_GAIN != METHOD_FAILURE
CASE_FAIL != METHOD_DELETION_PROOF
```

## 10. Method boundaries

```text
Specification:
  states requirements/constraints; Measurement asks which supplied readouts discriminate them.

Design:
  proposes target structures or instruments; Measurement does not design hardware by default.

Aggregation:
  combines readouts; Measurement may consume an aggregate but must test whether it preserves discrimination.

Compression:
  reduces representation under error/reconstruction objectives; Measurement only records resulting discrimination consequences through handoff.

Comparison:
  compares supplied subjects; Measurement asks what observation/readout separates alternatives.

Diagnosis:
  infers explanatory state/cause from evidence; Measurement does not infer the cause merely from sufficiency of a readout.

Prediction/Simulation:
  may supply expected outcome sets; Measurement must not generate missing predictions silently.

Provenance:
  tracks origin; Measurement consumes provenance to bound bridge credibility but does not replace provenance tracing.

Audit:
  evaluates conformance; Measurement emits its own result but does not audit itself.
```

## 11. Validation standard

An internal Measurement run is checked against the frozen task by verifying:

```text
question / alternative / resolution lock
candidate measurement identity and applicability
status preservation
outcome-map and bridge provenance
pairwise discrimination
joint discrimination
collision / injectivity / reconstruction limits
tolerance / uncertainty scope
temporal / regime / dynamic-support scope
plan terminal status
conformance
bounded claim strength
```

External metrology, instrumentation validity, clinical validity, field calibration, and empirical truth are not established by this draft.
