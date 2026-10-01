# RECON-CH-003 — Direct Neighboring-Method Reconstruction Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-003`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad

PROTOCOL_BLOB:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e
~~~

The frozen Reconstruction protocol may not be edited in response to this challenge.

## 2. Purpose

Test whether Reconstruction collapses into neighboring Method Family methods when every pair receives fair access to the same claim-relevant artifact bundle.

The challenge tests eleven neighboring methods:

~~~text
Diagnosis
Aggregation
Compression
Tracking
Lineage
Measurement
Transformation
Prediction
Simulation
Optimization
Audit
~~~

This is a fixture-bounded method-boundary test.

It is not:

~~~text
a permanent irreducibility proof
a method-superiority claim
a merger/deletion decision
a permanent registry-survival result
an external-validation result
~~~

## 3. Shared artifact bundle

Every compared pair receives the same claim-relevant constructed records:

~~~text
declared Reconstruction question
source/history candidate class
class representation/evaluation mode
candidate-class completeness status

available evidence
typed status / support / provenance
time / regime / resolution
evidence-set coherence status

forward / observation / aggregation / compression map
transition / history relation where relevant
bridge version / scope / direction
collision / fiber / kernel / injectivity records

support-retention sidecars
relational / cross-coordinate conditions
interface-closure record
candidate compatibility/exclusion ledger
compatible / excluded / blocked / unresolved sets
uniqueness scope
recoverability / unrecoverability record
maximum-supported claim
additional-evidence handoff
protocol-conformance record
~~~

Neighbor-specific sidecars are also shared when relevant.

No neighboring method receives hidden claim-relevant information unavailable to Reconstruction.

Fair access does not require identical task contracts.

## 4. Five-interface non-collapse test

For every pair compare:

~~~text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
~~~

Allowed pair result:

~~~text
EXACT_COLLAPSE
PARTIAL_OVERLAP_NOT_COLLAPSE
UNRESOLVED_BOUNDARY
~~~

`EXACT_COLLAPSE` requires no claim-relevant distinction across all five interfaces in the frozen fixture.

Shared evidence, maps, candidate sets, sidecars, ledgers, or handoffs are insufficient for collapse.

## 5. B1 — Reconstruction vs Diagnosis

Shared overlap:

~~~text
candidate structures
evidence
bridge semantics
collision/nonuniqueness records
typed status/provenance
~~~

Frozen distinction:

~~~text
Reconstruction:
  infer prior / omitted / damaged / compressed structures
  or histories compatible with evidence

Diagnosis:
  infer current hidden-state / condition / failure-mode /
  cause-hypothesis compatibility
~~~

Failure distinction:

~~~text
Diagnosis:
  may uniquely identify a current state while several predecessor histories remain

Reconstruction:
  may recover a bounded prior structure without establishing
  which present hidden-state or cause hypothesis applies
~~~

Guard:

~~~text
CURRENT_STATE_DIAGNOSIS != PAST_OR_OMITTED_RECONSTRUCTION
RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. B2 — Reconstruction vs Aggregation

Shared overlap:

~~~text
source values
support/status records
forward map
readout
collision / injectivity information
~~~

Frozen distinction:

~~~text
Aggregation:
  execute a declared forward combination/readout over admitted inputs

Reconstruction:
  invert evidence/readout constraints into a bounded compatible-source set
  and explicitly record uniqueness/nonuniqueness/recovery limits
~~~

Failure distinction:

~~~text
Aggregation:
  may be valid even when many source configurations share one aggregate

Reconstruction:
  must retain that multiplicity unless a frozen resolving condition excludes it
~~~

Guard:

~~~text
AGGREGATE_EQUALITY != SOURCE_IDENTITY
AGGREGATION_RESULT != RECONSTRUCTION_RESULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. B3 — Reconstruction vs Compression

Shared overlap:

~~~text
source objects
reduced representation
collision fibers
retained sidecars
losslessness/injectivity records
~~~

Frozen distinction:

~~~text
Compression:
  forward representation reduction under a frozen downstream-purpose
  and retained-distinction contract

Reconstruction:
  inverse determination of which source structures remain compatible
  and which distinctions are recoverable or unrecoverable
~~~

Failure distinction:

~~~text
Compression:
  may be intentionally lossy yet valid for its declared purpose

Reconstruction:
  cannot claim unique recovery through a destructive collision
  without a frozen resolving interface
~~~

Guard:

~~~text
COMPRESSION_SUCCESS != RECONSTRUCTION_SUCCESS
PURPOSE_SAFE_COLLISION != RECONSTRUCTION_SAFE_COLLISION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. B4 — Reconstruction vs Tracking

Shared overlap:

~~~text
evidence identity
provenance
version
time
handoff links
candidate trace relations
~~~

Frozen distinction:

~~~text
Tracking:
  establish supported provenance/version/process/location/handoff relations

Reconstruction:
  infer compatible missing/prior links or structures from available evidence
~~~

Failure distinction:

~~~text
Tracking:
  may have a missing trace link and must preserve that gap

Reconstruction:
  may emit several admissible inferred link candidates,
  but none becomes an established Tracking relation by inference alone
~~~

Guard:

~~~text
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACKING_GAP != LICENSE_TO_ASSERT_ONE_RECONSTRUCTION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. B5 — Reconstruction vs Lineage

Shared overlap:

~~~text
state identities
predecessor/successor candidates
transition relations
time/history constraints
continuity records
~~~

Frozen distinction:

~~~text
Lineage:
  establish predecessor-successor identity/continuity across change

Reconstruction:
  infer which prior/history candidates remain compatible
  without promoting candidate relations into established identity
~~~

Failure distinction:

~~~text
Reconstruction:
  may retain several predecessor histories

Lineage:
  may remain not established even when one reconstructed candidate
  is compatible unless lineage-specific identity evidence is supplied
~~~

Guard:

~~~text
RECONSTRUCTION_CANDIDATE != ESTABLISHED_LINEAGE
TRANSITION_COMPATIBILITY != SUCCESSOR_IDENTITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. B6 — Reconstruction vs Measurement

Shared overlap:

~~~text
alternative source candidates
candidate readouts
resolution
distinguishability information
possible additional evidence roles
~~~

Frozen distinction:

~~~text
Measurement:
  evaluate whether observations/readouts can discriminate
  declared alternatives at a declared resolution

Reconstruction:
  use actually supplied evidence/interfaces to determine
  the compatible source/history set
~~~

Failure distinction:

~~~text
Measurement:
  may establish a sufficient future observation plan

Reconstruction:
  remains BLOCKED or multiple-compatible until the required
  observation is actually supplied through a valid interface
~~~

Guard:

~~~text
MEASUREMENT_SUFFICIENCY != RECONSTRUCTION
DISCRIMINATOR_REQUIREMENT != MEASUREMENT_EXECUTION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. B7 — Reconstruction vs Transformation

Shared overlap:

~~~text
source/target structures
versioned mappings
preservation/loss records
relational sidecars
~~~

Frozen distinction:

~~~text
Transformation:
  map a supplied source structure into a target representation/regime

Reconstruction:
  infer an unknown prior/omitted source or history from retained evidence
~~~

Failure distinction:

~~~text
Transformation:
  may execute correctly from a known source even if the map is noninjective

Reconstruction:
  inverse uniqueness remains unavailable across a noninjective map
  without additional frozen evidence
~~~

Guard:

~~~text
TRANSFORMATION_MAPPING != INVERSE_SOURCE_IDENTIFICATION
FORWARD_MAPPING_CORRECTNESS != RECONSTRUCTION_UNIQUENESS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. B8 — Reconstruction vs Prediction

Shared overlap:

~~~text
states
models/bridges
time/regime
transition relations
uncertainty or multiplicity records
~~~

Frozen distinction:

~~~text
Prediction:
  forward consequence from supplied present state/model assumptions
  toward future outcomes

Reconstruction:
  inverse compatibility from evidence toward prior/omitted structures
  or histories
~~~

Failure distinction:

~~~text
Prediction:
  may produce valid future outcomes conditional on several possible states

Reconstruction:
  cannot use those forward outcomes to select one past source
  unless the frozen evidence bridge supports that exclusion
~~~

Guard:

~~~text
PREDICTION_OUTPUT != RECONSTRUCTED_PAST
FORWARD_CONSEQUENCE != INVERSE_HISTORY_IDENTIFICATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. B9 — Reconstruction vs Simulation

Shared overlap:

~~~text
state representations
transition/dynamic models
time/regime
generated readouts
history-shaped trajectories
~~~

Frozen distinction:

~~~text
Simulation:
  execute supplied model evolution from supplied initial/state assumptions

Reconstruction:
  infer compatible prior/history candidates from evidence
~~~

Failure distinction:

~~~text
Simulation:
  may generate a trajectory for each hypothetical initial state

Reconstruction:
  cannot treat one generated trajectory as the actual past
  without an evidence relation that excludes the alternatives
~~~

Guard:

~~~text
SIMULATED_HISTORY != RECONSTRUCTED_HISTORY_BY_DEFAULT
SIMULATION_MATCH != HISTORICAL_IDENTITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 14. B10 — Reconstruction vs Optimization

Shared overlap:

~~~text
candidate sets
constraints
evidence-derived records
additional-evidence options
~~~

Frozen distinction:

~~~text
Reconstruction:
  retain/exclude source/history candidates by evidence compatibility

Optimization:
  select among feasible alternatives using an explicit
  objective/loss/utility/order rule
~~~

Failure distinction:

~~~text
Reconstruction:
  may legitimately stop with several compatible candidates

Optimization:
  may rank/select among them if an objective is supplied,
  but that ranking does not eliminate candidates historically
~~~

Guard:

~~~text
RECONSTRUCTION_COMPATIBILITY != OPTIMALITY
CANDIDATE_RANKING != HISTORICAL_EXCLUSION
ADDITIONAL_EVIDENCE_HANDOFF != OPTIMAL_MEASUREMENT_SELECTED
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 15. B11 — Reconstruction vs Audit

Shared overlap:

~~~text
frozen task/protocol
evidence provenance
status ledgers
maximum-supported claim
conformance record
~~~

Frozen distinction:

~~~text
Reconstruction:
  perform source/history compatibility and recoverability inference

Audit:
  retrace and evaluate performed work/evidence/procedure
  against a frozen audit scope and criteria
~~~

Failure distinction:

~~~text
Reconstruction:
  may validly return NOT_ESTABLISHED, BLOCKED, CONFLICTING,
  UNDERDETERMINED, or OUT_OF_SCOPE

Audit:
  may pass precisely because that bounded terminal was produced correctly
~~~

Guard:

~~~text
AUDIT_PASS != RECONSTRUCTION_RESULT
RECONSTRUCTION_PROTOCOL_CONFORMANCE != HISTORICAL_TRUTH_CERTAINTY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 16. Source-layer handoff separation

Reconstruction legitimately consumes source/interface constraints from:

~~~text
Formation
Property
Static Aggregation
Structural Reorganization Dynamics
~~~

but source-layer handoff does not establish method identity.

Required guards:

~~~text
FORMATION_WITNESS_HISTORY != ACTUAL_TEMPORAL_HISTORY
SOURCE_LAYER_HANDOFF != METHOD_IDENTITY
OPERATIONALIZATION != SOURCE_DEFINITION_REPLACEMENT
~~~

Expected:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## 17. Frozen scoring — 99 checks

Each method pair receives nine checks.

For every pair B1-B11:

~~~text
-1 shared artifact access fair
-2 INPUTS overlap recorded without identity claim
-3 OPERATION distinction preserved
-4 OUTPUTS distinction preserved
-5 FAILURE/NO_GAIN distinction preserved
-6 VALIDATION_STANDARD distinction preserved
-7 semantic guard preserved
-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
-9 no permanent irreducibility/superiority claim
~~~

Expected totals:

~~~text
B1 Reconstruction vs Diagnosis: 9/9
B2 Reconstruction vs Aggregation: 9/9
B3 Reconstruction vs Compression: 9/9
B4 Reconstruction vs Tracking: 9/9
B5 Reconstruction vs Lineage: 9/9
B6 Reconstruction vs Measurement: 9/9
B7 Reconstruction vs Transformation: 9/9
B8 Reconstruction vs Prediction: 9/9
B9 Reconstruction vs Simulation: 9/9
B10 Reconstruction vs Optimization: 9/9
B11 Reconstruction vs Audit: 9/9

TOTAL_REQUIRED_CHECKS:
  99

PASS_THRESHOLD:
  99/99

PARTIAL_PASS_ALLOWED:
  no
~~~

## 18. Expected aggregate boundary result

If all 99 checks pass:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  11

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

Counter update:

~~~text
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  3

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  3

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
  1
~~~

## 19. Next

If the frozen bundle passes, proceed to a fair competent non-DSD Reconstruction baseline challenge.

The baseline must receive equal claim-relevant information and may produce NO_GAIN for Reconstruction.
