# DSD Measurement Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-19**

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
  blob: 6df3816a3db14b7c45ccec8de0d967f5a4ab0d98

BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
  blob: 24256fec71287e0aa90e505f83f2579b93a0ccdc

TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
  commit: 7f09baa7e2bb2701b4f01471abbbd443d226a78a
  blob:   1ac7933fc19d95e9070432de99deb5a0fd1d382c
```

This protocol freezes the internal operational semantics of DSD Measurement. It does not establish external metrological validity, empirical truth, instrument calibration, clinical validity, causal correctness, or independent validation.

## 1. Method form

A Measurement task has the form

```text
(
  discrimination question,
  alternative identities,
  required distinction set,
  declared decision resolution,
  candidate measurement/readout records,
  applicability/status records,
  supplied outcome maps or bridges,
  tolerance/uncertainty/decision rules,
  information-loss/reconstruction sidecars,
  temporal/regime/dynamic-support records,
  neighboring-method handoffs
)
->
(
  candidate measurement statuses,
  pairwise distinguishability matrix,
  joint-measurement record,
  information-loss and provenance ledgers,
  plan-level terminal status,
  conformance,
  method-gain status
)
```

Measurement evaluates the discriminating adequacy of supplied or proposed readouts under frozen semantics. It does not create an observed result.

## 2. Source-layer discipline

Protocol v0.1 may consume the following DSD predecessor information when supplied:

```text
Formation:
  stage-aware structural difference / first-branching records.

Property:
  declaration, profile availability, applicability, prerequisite satisfaction,
  defined/undefined and zero/nonzero status.

Static Aggregation:
  aggregate/readout maps, support-retaining sidecars,
  collision/injectivity/reconstruction information.

Dynamics:
  temporal/regime scope and distinguishability-support availability.
```

The predecessor layers remain logically distinct.

```text
FIRST_BRANCHING != MEASUREMENT_RESULT
PROPERTY_STATUS != OBSERVED_VALUE
STATIC_AGGREGATE != FULL_STRUCTURE
DYNAMIC_SUPPORT_AVAILABILITY != CAUSAL_PROOF
```

## 3. Required task record

Every executable run freezes:

```text
MEASUREMENT_TASK_ID
TASK_VERSION
DISCRIMINATION_QUESTION
ALTERNATIVE_SET_AND_IDENTITIES
REQUIRED_DISTINCTION_SET
DECLARED_DECISION_RESOLUTION
TASK_SCOPE
CANDIDATE_MEASUREMENT_REGISTER
MEASUREMENT_STATUS_RECORDS
OUTCOME_MAP_OR_BRIDGE_RECORDS
BRIDGE_PROVENANCE
```

Conditionally required when claim-relevant:

```text
MEASUREMENT_VERSION
READOUT_UNIT_OR_REPRESENTATION
TOLERANCE_OR_EQUIVALENCE_RELATION
UNCERTAINTY_OR_ERROR_MODEL
DECISION_RULE
JOINT_MEASUREMENT_POLICY
AGGREGATE_OR_REDUCTION_HANDOFF
INJECTIVITY_OR_RECONSTRUCTION_RECORD
PROXY_OR_DIRECTNESS_RECORD
MEASUREMENT_TIME_OR_WINDOW
MEASUREMENT_LOCATION
ACTIVE_REGIME_OR_SCHEMA_VERSION
DYNAMIC_DISTINGUISHABILITY_SUPPORT_HANDOFF
PREDICTION_OR_SIMULATION_HANDOFF
OTHER_NEIGHBORING_METHOD_HANDOFF
```

Required claim-relevant data may be explicitly absent; absence is then part of the task state and may lead to a blocked or underdetermined result.

## 4. Candidate measurement descriptor

For each candidate `m`, record:

```text
MEASUREMENT_ID
MEASUREMENT_VERSION_IF_RELEVANT
READOUT_CARRIER_OR_TYPE
DECLARED_DOMAIN
UNIT_OR_REPRESENTATION
APPLICABILITY_SCOPE
STATUS
OUTCOME_RECORD_SOURCE
BRIDGE_ID_AND_VERSION
DIRECT_OR_PROXY_ROLE
TEMPORAL_OR_REGIME_SCOPE
```

When the task imports Property-layer status semantics, preserve:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
```

A status can be unavailable to Measurement without being a negative readout.

## 5. Outcome records and decision classes

For candidate measurement `m` and alternative `H_i`, let

```text
Y_m(H_i)
```

denote the supplied admissible outcome record.

`Y_m(H_i)` may be a value, set, interval, typed status family, distributional record, symbolic output, or other declared carrier supplied by an explicit bridge/handoff.

Protocol v0.1 does not infer a missing `Y_m(H_i)`.

When raw outcomes require tolerance, uncertainty, threshold, or statistical semantics, a supplied decision relation `D_m` maps admissible outcomes into declared decision classes.

If no such rule is required, identity on the declared outcome representation is used.

The protocol then evaluates overlap only after the frozen decision semantics are applied.

## 6. Pairwise distinguishability

For required pair `{H_i,H_j}` and candidate `m`:

```text
PAIRWISE_DISCRIMINATING
  when both sides are applicable/defined enough for the task and
  their admissible decision-class sets are disjoint.

PAIRWISE_NONDISCRIMINATING
  when both sides are evaluable and at least one admissible decision class overlaps.

PAIRWISE_BLOCKED
  when a required bridge, prerequisite, prediction, calibration record,
  or other required handoff is absent.

PAIRWISE_UNDERDETERMINED
  when claim-relevant competing mappings/rules/scopes remain admissible
  and yield different discrimination judgments with no frozen precedence.

PAIRWISE_OUT_OF_SCOPE
  when the requested pair/candidate relation lies outside the declared task or candidate domain.
```

A pairwise status is always scoped to the frozen resolution, decision rule, time/regime, and bridge version.

## 7. Joint-measurement distinguishability

For declared candidate set `M={m1,...,mk}`, joint discrimination is evaluated only when a joint policy is supplied or the task explicitly permits product-signature semantics.

The joint outcome record is:

```text
Y_M(H_i)
```

with provenance to the member records and any correlation/dependence assumptions.

The protocol does not assume independence of measurement errors or outcomes.

```text
MEMBER_COUNT != INFORMATION_GAIN
PAIRWISE_MEMBER_SUCCESS != JOINT_MODEL_VALIDITY
JOINT_SUFFICIENCY != SINGLE_MEASUREMENT_SUFFICIENCY
SINGLE_MEASUREMENT_INSUFFICIENCY != JOINT_MEASUREMENT_INSUFFICIENCY
```

## 8. Candidate measurement status family

After pairwise/joint evaluation, each candidate receives one of:

```text
MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
MEASUREMENT_PARTIALLY_DISCRIMINATES
MEASUREMENT_NONDISCRIMINATING
MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
MEASUREMENT_INAPPLICABLE
MEASUREMENT_OUT_OF_SCOPE
MEASUREMENT_UNDERDETERMINED
```

Interpretation:

```text
DISCRIMINATES
  candidate distinguishes every required pair assigned to its declared candidate scope.

PARTIALLY_DISCRIMINATES
  candidate distinguishes at least one but not all required in-scope pairs.

NONDISCRIMINATING
  all required information is present and the candidate distinguishes none
  of the required in-scope pairs at the frozen decision semantics.

BLOCKED
  assessment requires absent prerequisite/bridge/handoff data.

INAPPLICABLE
  candidate does not apply to the supplied object/alternative record under its declared domain.

OUT_OF_SCOPE
  candidate relation is outside the frozen Measurement task scope.

UNDERDETERMINED
  multiple admissible claim-relevant mappings/rules/scopes prevent a unique status.
```

## 9. Plan-level terminal status family

The overall Measurement plan emits exactly one:

```text
MEASUREMENT_PLAN_SUFFICIENT
MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
MEASUREMENT_PLAN_INSUFFICIENT
MEASUREMENT_PLAN_BLOCKED
MEASUREMENT_PLAN_OUT_OF_SCOPE
MEASUREMENT_PLAN_UNDERDETERMINED
```

Rules:

```text
MEASUREMENT_PLAN_SUFFICIENT
  every required distinction is discriminated by the declared admissible single/joint plan.

MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
  at least one but not all required distinctions are discriminated,
  and the remaining failure is not wholly due to missing required assessment data.

MEASUREMENT_PLAN_INSUFFICIENT
  all required assessment information is available,
  but the declared admissible measurement plan does not discriminate any
  or does not meet the task's frozen sufficiency rule.

MEASUREMENT_PLAN_BLOCKED
  no valid sufficiency determination can be completed because required
  bridge/prerequisite/handoff data are absent.

MEASUREMENT_PLAN_OUT_OF_SCOPE
  the requested operation is not a Measurement discrimination task
  or the entire supplied plan lies outside the declared scope.

MEASUREMENT_PLAN_UNDERDETERMINED
  multiple admissible claim-relevant mappings, decision rules, or regime scopes
  lead to incompatible plan judgments with no frozen precedence.
```

A non-sufficient terminal can still be protocol-conformant.

## 10. Information-loss, collision, and reconstruction ledger

For every reduced/aggregate/transformed readout used in a claim, record where supplied:

```text
READOUT_COLLISION_STATUS
INJECTIVITY_SCOPE
SUPPORT_RETENTION_STATUS
RECONSTRUCTION_SCOPE
AGGREGATION_OR_REDUCTION_HANDOFF
INFORMATION_LOSS_NOTE
```

Core guards:

```text
EQUAL_READOUT != EQUAL_STRUCTURE
EQUAL_AGGREGATE != EQUAL_SUPPORT
NONINJECTIVE_READOUT != RECONSTRUCTIVE_MEASUREMENT
GLOBAL_NONINJECTIVITY != FAILURE_TO_DISCRIMINATE_A_DECLARED_PAIR
DISCRIMINATING_READOUT != FULL_STRUCTURE_RECONSTRUCTION
SUPPORT_RECONSTRUCTION != VALUE_DISCRIMINATION
```

## 11. Tolerance, uncertainty, and threshold discipline

Any nontrivial decision rule must be frozen before execution.

Record:

```text
RULE_ID_AND_VERSION
RULE_TYPE
TOLERANCE_OR_THRESHOLD
UNCERTAINTY_OR_ERROR_MODEL_SOURCE
CALIBRATION_OR_STATISTICAL_HANDOFF
APPLICABILITY_SCOPE
```

The protocol does not create a statistical confidence level, significance threshold, sensor error model, calibration constant, or domain-specific acceptance criterion.

```text
POST_HOC_THRESHOLD != PROSPECTIVE_DECISION_RULE
RAW_SEPARATION != CALIBRATED_DISCRIMINATION
UNSPECIFIED_TOLERANCE != LICENSE_TO_CHOOSE
OVERLAPPING_RAW_VALUES != AUTOMATIC_STATISTICAL_NONDISTINGUISHABILITY
```

The final guard means a supplied statistical decision rule may still discriminate overlapping raw distributions; Measurement itself does not invent that rule.

## 12. Temporal, regime, and dynamic-support discipline

When claim-relevant, record:

```text
MEASUREMENT_TIME_OR_WINDOW
MEASUREMENT_LOCATION
ACTIVE_REGIME_OR_SCHEMA_VERSION
DYNAMIC_DISTINGUISHABILITY_SUPPORT_STATUS
TEMPORAL_BRIDGE_VERSION
```

If a supplied dynamic-support handoff says the distinguishing perturbation has not reached the target location/time, the corresponding candidate cannot use that difference as present local evidence.

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
SAME_READOUT_LABEL != SAME_SEMANTICS_ACROSS_REGIMES
TEMPORAL_ORDER != CAUSAL_BRIDGE
DYNAMIC_SUPPORT_AVAILABILITY != CAUSAL_SUFFICIENCY
```

## 13. Provenance, directness, and neighboring-method handoffs

Every claim-relevant input is labeled by role:

```text
DIRECT_SOURCE_OR_RECORD
PROPERTY_STATUS_HANDOFF
FORMATION_DIFFERENCE_HANDOFF
AGGREGATION_OR_COMPRESSION_HANDOFF
TRANSFORMATION_HANDOFF
PREDICTION_OR_SIMULATION_HANDOFF
PROVENANCE_OR_LINEAGE_HANDOFF
DOMAIN_METROLOGY_OR_CALIBRATION_HANDOFF
OTHER_TYPED_HANDOFF
```

Proxy/directness is recorded independently of outcome value.

Measurement may consume neighboring artifacts, but:

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

## 14. Validity gates

A conformant run must satisfy all applicable gates:

```text
G1  task ID/version, question, alternatives, required distinctions, resolution, and scope frozen
G2  candidate measurement identity/type/domain/unit/version frozen
G3  applicability and typed statuses preserved
G4  claim-relevant structural-difference inputs scoped and provenance-recorded
G5  outcome maps/bridges supplied explicitly; no invented prediction or calibration
G6  tolerance/uncertainty/decision semantics prospectively frozen when needed
G7  pairwise status evaluated for every required in-scope pair or explicitly blocked/out-of-scope
G8  joint-measurement semantics explicit; no hidden independence/correlation assumption
G9  collisions/information loss/injectivity/reconstruction limits preserved
G10 proxy/directness and bridge provenance preserved
G11 temporal/regime/dynamic-support scope preserved when claim-relevant
G12 neighboring-method handoffs remain typed and method boundaries preserved
G13 measurement selection is not relabeled as observed experimental result
G14 terminal status, conformance, gain status, and maximum claim scope emitted
```

An inapplicable gate is recorded as `NOT_APPLICABLE_WITH_REASON`, not silently omitted.

## 15. Binding operation

The executable operation is:

```text
M1  freeze task identity and discrimination target
M2  freeze alternatives and required distinction set
M3  freeze resolution and task scope
M4  register typed candidate measurements and status records
M5  register outcome maps/bridges and provenance
M6  freeze tolerance/uncertainty/decision semantics
M7  evaluate candidate applicability and data availability
M8  build pairwise distinguishability matrix
M9  evaluate declared joint measurement sets
M10 record collisions, information loss, injectivity, reconstruction scope
M11 evaluate proxy/directness and provenance limits
M12 evaluate temporal/regime/dynamic-support availability
M13 assign candidate statuses and overall plan terminal
M14 emit conformance, method-gain status, and bounded claim
```

No later operation may retroactively alter M1-M6 without opening a new task version.

## 16. Output contract

Every run emits:

```text
LOCKED_DISCRIMINATION_QUESTION_AND_RESOLUTION
ALTERNATIVE_AND_REQUIRED_DISTINCTION_LEDGER
MEASUREMENT_CANDIDATE_REGISTER
MEASUREMENT_STATUS_LEDGER
OUTCOME_MAP_AND_BRIDGE_LEDGER
PAIRWISE_DISTINGUISHABILITY_MATRIX
JOINT_MEASUREMENT_DISTINGUISHABILITY_RECORD
READOUT_COLLISION_AND_INFORMATION_LOSS_LEDGER
INJECTIVITY_AND_RECONSTRUCTION_RECORD
TOLERANCE_UNCERTAINTY_DECISION_RULE_RECORD
PROXY_OR_DIRECTNESS_LEDGER
TEMPORAL_REGIME_AND_DYNAMIC_SUPPORT_LEDGER
NEIGHBORING_METHOD_HANDOFF_LEDGER
MEASUREMENT_PLAN_TERMINAL_STATUS
MEASUREMENT_PROTOCOL_CONFORMANCE
MEASUREMENT_METHOD_GAIN_STATUS
MAXIMUM_SUPPORTED_CLAIM
```

## 17. Protocol conformance

Allowed conformance:

```text
CONFORMANT
NONCONFORMANT
UNRESOLVED_CONFORMANCE
```

Examples of nonconformance:

```text
changing alternatives/resolution after seeing candidate performance
using inapplicable/undefined status as an observed negative value
inventing outcome or prediction records
inventing a measurement-to-claim bridge
hiding aggregate collisions or reconstruction limits
selecting a tolerance/threshold post hoc
assuming measurement independence without a joint policy
using not-yet-arrived dynamic information as present evidence
promoting a proxy to direct observation without provenance
turning selected measurement into fabricated observed result
performing diagnosis/design/prediction silently inside Measurement
generalizing partial discrimination to complete required coverage
```

A conformant result may be blocked, underdetermined, out-of-scope, or insufficient.

## 18. Method-gain evaluation

Allowed:

```text
GAIN_ESTABLISHED
NO_GAIN
NOT_ASSESSED
```

A fair baseline must receive the same:

```text
question
alternatives
required distinction set
resolution
candidate identities/statuses
outcome maps/bridges
provenance
tolerance/uncertainty/decision rules
joint policy
collision/injectivity/reconstruction information
temporal/regime/dynamic-support information
neighboring-method handoffs
```

`GAIN_ESTABLISHED` requires a precommitted claim-relevant difference under equal access.

`NO_GAIN` is a valid comparative result.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 19. Reproducibility and evidence scope

Internal deterministic retrace may be performed only from immutable protocol/precommit artifacts with a separately frozen comparator.

A successful same-project retrace may establish:

```text
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once_or_more
```

but not:

```text
INDEPENDENT_REPLICATION
INDEPENDENT_VALIDATION
EXTERNAL_APPLICABILITY
PRACTICAL_SUPERIORITY
```

## 20. Shared-core obligations

Protocol v0.1 inherits the project shared-core guards, including:

```text
SC01 claim-relevant DSD status/type distinctions
SC02 source/interface/version lock
SC03 explicit claim-relevant mappings
SC04 sufficient dependencies without optional-interface overconstraint
SC05 information-loss/reconstruction limits
SC06 regular evolution vs transition vs lineage separation when relevant
SC07 evidence applicability vs case origin
SC08 failure/NO_GAIN/precommit integrity
SC09 evidence/audit status vs method-object status
SC10 external-domain standards separate from DSD internal success
```

No new shared-core clause is asserted by this protocol.

## 21. Maximum supported claim

A successful internal Measurement run may establish only that, under the frozen supplied maps, statuses, decision rules, provenance, and scope, a candidate measurement or measurement plan has the recorded discrimination status.

It does not by itself establish:

```text
empirical truth of an alternative
instrument validity
metrological traceability
clinical validity
causal correctness
diagnostic correctness
external-domain adequacy
independent validation
method superiority
permanent method-registry survival
```

## 22. Protocol freeze status

```text
DEDICATED_MEASUREMENT_PROTOCOL: established v0.1
BOUNDARY_AMENDMENT_001: established
VALIDITY_GATES: G1-G14
BINDING_OPERATION: M1-M14
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: protocol_frozen_pre_validation
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Next: prospectively precommit and execute the first positive constructed Measurement challenge. External validation remains deferred.
