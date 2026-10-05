# SIM-CH-003 — Direct Neighboring-Method Simulation Boundary Challenge Result

Status: **EXECUTED — 108/108 PASS**  
Date: **2026-10-05**  
Challenge ID: `SIM-CH-003`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

PRECOMMIT_COMMIT:
  28438af12f0e80b441381b45b2cb836e587c4aa3

PRECOMMIT_BLOB:
  3f750323283a3525a4925d122f3ffee26211d654
~~~

No compared-method definition, shared artifact, expected pair result, scoring item, or pass threshold changed after precommit.

## 2. Aggregate result

~~~text
TOTAL_REQUIRED_CHECKS:
  108

PASSED:
  108

FAILED:
  0

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  12

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

All twelve pairs received fair access to the frozen claim-relevant artifact bundle.

## 3. Pair results

### B1 — Simulation vs Computation

~~~text
OPERATION:
  Computation determines required/omittable/reusable evaluation
  Simulation generates model-consistent temporal state evolution

OUTPUTS:
  Computation -> bounded evaluation plan + soundness ledgers
  Simulation -> trajectory / trajectory family / reachable-set records

FAILURE_OR_NO_GAIN:
  Computation may succeed without producing a trajectory
  Simulation must satisfy frozen evolution/transition semantics

VALIDATION:
  Computation -> target-relative evaluation soundness
  Simulation -> model/trajectory/transition/execution consistency

GUARD:
  COMPUTATION_PLAN != SIMULATION_EXECUTION
  REQUIRED_UPDATE_SET != GENERATED_TRAJECTORY

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B2 — Simulation vs Optimization

~~~text
OPERATION:
  Optimization selects among admissible alternatives
  Simulation evolves a supplied model/candidate

OUTPUTS:
  Optimization -> selected optimum/Pareto/tied set
  Simulation -> trajectory result

FAILURE_OR_NO_GAIN:
  Simulation can generate several candidate trajectories without choosing
  Optimization requires objective/constraint selection semantics

GUARD:
  SIMULATION_TRAJECTORY != OPTIMUM
  MODEL_EVOLUTION != SELECTION_RULE

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B3 — Simulation vs Measurement

~~~text
OPERATION:
  Measurement acquires/defines observations or distinguishability
  Simulation generates model states from supplied inputs/laws

OUTPUTS:
  Measurement -> observation / measurement evidence
  Simulation -> generated trajectory

FAILURE_OR_NO_GAIN:
  Measurement can be resolution-limited
  Simulation can consume measurement without performing it

GUARD:
  MEASUREMENT_RESULT != SIMULATED_STATE
  OBSERVED_VALUE != MODEL_GENERATED_VALUE_BY_DEFAULT

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B4 — Simulation vs Aggregation

~~~text
OPERATION:
  Aggregation constructs a declared readout
  Simulation evolves component-resolved state and may emit readout downstream

OUTPUTS:
  Aggregation -> aggregate/readout + collision/support ledger
  Simulation -> trajectory + optional readout history

FAILURE_OR_NO_GAIN:
  Aggregation may validly collapse distinct states
  Simulation may not infer equal states from equal readouts

GUARD:
  AGGREGATE_READOUT != COMPONENT_TRAJECTORY
  EQUAL_READOUT_HISTORY != EQUAL_STATE_HISTORY

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B5 — Simulation vs Compression

~~~text
OPERATION:
  Compression reduces representation under retained-distinction constraints
  Simulation generates temporal evolution

OUTPUTS:
  Compression -> reduced representation + loss/retention ledger
  Simulation -> trajectory / trajectory-family ledgers

FAILURE_OR_NO_GAIN:
  Compression may succeed despite intentional information loss
  Simulation full-state claims require required dynamic distinctions to survive

GUARD:
  COMPRESSED_TRAJECTORY_REPRESENTATION != SIMULATION_STATE_BY_DEFAULT
  REPRESENTATION_PRESERVATION != DYNAMIC_LAW_VALIDITY

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B6 — Simulation vs Transformation

~~~text
OPERATION:
  Transformation maps source to target representation/regime
  Simulation advances state through time/step evolution

OUTPUTS:
  Transformation -> transformed object + preservation/loss ledger
  Simulation -> time-indexed trajectory + epoch/transition ledger

FAILURE_OR_NO_GAIN:
  Transformation can be valid with no temporal semantics
  Simulation requires frozen temporal/update semantics

GUARD:
  TRANSFORMATION_RESULT != TIME_EVOLUTION
  REPRESENTATION_MAP != DYNAMIC_LAW_BY_DEFAULT

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B7 — Simulation vs Tracking

~~~text
OPERATION:
  Tracking establishes provenance/version/process/handoff trace links
  Simulation generates state evolution

OUTPUTS:
  Tracking -> trace graph/path/evidence ledger
  Simulation -> trajectory / transition / solver/readout ledgers

FAILURE_OR_NO_GAIN:
  Tracking trace gaps remain trace gaps
  Simulation may block on missing provenance but does not infer the trace

GUARD:
  TRACKING_TRACE != TRAJECTORY_DYNAMICS
  SIMULATION_LOG != TRACKING_PROOF_BY_DEFAULT

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B8 — Simulation vs Lineage

~~~text
OPERATION:
  Lineage establishes predecessor-successor identity
  Simulation consumes lineage when identity claims cross transitions

OUTPUTS:
  Lineage -> successor/coherence ledger
  Simulation -> hybrid trajectory + transition/lineage-consumption ledger

FAILURE_OR_NO_GAIN:
  unresolved lineage may remain unresolved
  Simulation may block/underdetermine identity-bearing trajectory claims

GUARD:
  LINEAGE_HANDOFF != SIMULATION_EXECUTION
  TRAJECTORY_CONTINUITY != LINEAGE_IDENTITY_PROOF

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B9 — Simulation vs Prediction

~~~text
OPERATION:
  Simulation generates model-consistent future-labeled states
  Prediction asserts relevance to a future external target

OUTPUTS:
  Simulation -> trajectory / model readout history
  Prediction -> future-target claim / forecast validity status

FAILURE_OR_NO_GAIN:
  Simulation may be internally correct for its model
  Prediction may still be empirically unsupported or false

GUARD:
  MODEL_CONSISTENT_FUTURE_STATE != FUTURE_WORLD_TRUTH
  SIMULATION_SUCCESS != PREDICTION_SUCCESS

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B10 — Simulation vs Control

~~~text
OPERATION:
  Control chooses state-dependent interventions
  Simulation executes a supplied policy without selecting it

OUTPUTS:
  Control -> intervention policy / action mapping
  Simulation -> trajectory under supplied policy

FAILURE_OR_NO_GAIN:
  Simulation may faithfully simulate a poor policy
  Control fails if intervention-selection requirements are not met

GUARD:
  SIMULATING_SUPPLIED_CONTROL_POLICY != CHOOSING_CONTROL_POLICY
  CONTROL_POLICY != SIMULATION_TRAJECTORY

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B11 — Simulation vs Operation

~~~text
OPERATION:
  Operation manages actual repeated lifecycle / monitoring / handoff
  Simulation generates a model trajectory of that lifecycle

OUTPUTS:
  Operation -> actual execution/lifecycle records
  Simulation -> model lifecycle trajectory/readout records

FAILURE_OR_NO_GAIN:
  Simulation can succeed while real operation later fails
  Operation depends on actual execution state handling

GUARD:
  SIMULATING_LIFECYCLE_MODEL != OPERATING_REAL_LIFECYCLE
  MODEL_RUN != LIVE_OPERATION

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

### B12 — Simulation vs Audit

~~~text
OPERATION:
  Simulation generates trajectory results
  Audit retraces/evaluates work and evidence against frozen criteria

OUTPUTS:
  Simulation -> trajectory/status/conformance result
  Audit -> criterion-level findings and verdict

FAILURE_OR_NO_GAIN:
  bounded Simulation negative/unresolved states may be protocol-conformant
  Audit may pass because those states were correctly preserved

GUARD:
  SIMULATION_PROTOCOL_CONFORMANCE != GENERAL_AUDIT_PASS
  AUDIT_VERDICT != SIMULATION_TRAJECTORY

RESULT:
  PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 4. Source / handoff separation

~~~text
SOURCE_LAYER_HANDOFF != METHOD_IDENTITY
DYNAMICS_LAYER != SIMULATION_METHOD_VALIDATION
STATIC_BRIDGE != DYNAMIC_EVOLUTION_OPERATOR
LINEAGE_HANDOFF != SIMULATION_EXECUTION
MEASUREMENT_HANDOFF != SIMULATION_RESULT
CONTROL_HANDOFF != CONTROL_SELECTION_BY_SIMULATION

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

The Dynamics paper remains the primary formal source interface, but that source role does not collapse the method-level Simulation protocol into the source layer itself.

## 5. Frozen-score execution

~~~text
B1  Simulation vs Computation: 9/9 PASS
B2  Simulation vs Optimization: 9/9 PASS
B3  Simulation vs Measurement: 9/9 PASS
B4  Simulation vs Aggregation: 9/9 PASS
B5  Simulation vs Compression: 9/9 PASS
B6  Simulation vs Transformation: 9/9 PASS
B7  Simulation vs Tracking: 9/9 PASS
B8  Simulation vs Lineage: 9/9 PASS
B9  Simulation vs Prediction: 9/9 PASS
B10 Simulation vs Control: 9/9 PASS
B11 Simulation vs Operation: 9/9 PASS
B12 Simulation vs Audit: 9/9 PASS

TOTAL_REQUIRED_CHECKS:
  108

PASSED:
  108

FAILED:
  0
~~~

## 6. Post-challenge state

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  3

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  3

POSITIVE_SIMULATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  1

METHOD_BOUNDARY_SIMULATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  12

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

BASELINE_SIMULATION_CASES:
  0

NO_GAIN_SIMULATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_SIMULATION_APPLICATIONS:
  0

INDEPENDENT_SIMULATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

SIMULATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_SIMULATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 7. Interpretation lock

~~~text
FIXTURE_BOUNDED_SEPARATION != PERMANENT_METHOD_IRREDUCIBILITY
PARTIAL_OVERLAP_NOT_COLLAPSE != METHOD_SUPERIORITY
NO_EXACT_COLLAPSE_IN_THIS_FIXTURE != PERMANENT_REGISTRY_SURVIVAL
SHARED_INPUT != SHARED_METHOD_IDENTITY
SHARED_OUTPUT_ARTIFACT != SHARED_OPERATION
NO_GAIN_OR_FAILURE != METHOD_DELETION_PROOF
~~~

No method is deleted, merged, absorbed, or declared permanently redundant on the basis of this challenge.

## 8. Maximum-supported claim

Within the frozen SIM-CH-003 shared-artifact fixture, Simulation remains five-interface distinguishable from Computation, Optimization, Measurement, Aggregation, Compression, Transformation, Tracking, Lineage, Prediction, Control, Operation, and Audit.

No permanent irreducibility, superiority, external applicability, independent validation, or independent replication is established.

## 9. Next

Prospectively precommit and execute `SIM-CH-004`, a fair competent non-DSD Simulation baseline challenge.

The baseline must receive equal claim-relevant information and must permit `SIMULATION_NO_GAIN` as a valid result.
