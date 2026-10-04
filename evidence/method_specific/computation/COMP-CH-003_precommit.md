# COMP-CH-003 — Direct Neighboring-Method Computation Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-04**  
Challenge ID: `COMP-CH-003`  
Method: **Computation / DSD 계산론**  
Protocol: **Computation Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

No protocol rule may be changed in response to this challenge.

## 2. Purpose

Test whether Computation collapses into neighboring Method Family methods when every pair receives fair access to the same claim-relevant constructed artifact bundle.

The eleven frozen neighboring methods are:

~~~text
Optimization
Aggregation
Compression
Analysis
Measurement
Simulation
Prediction
Transformation
Audit
Tracking
Lineage
~~~

This is a fixture-bounded method-boundary challenge.

It is not:

~~~text
a permanent irreducibility proof
a method-survival vote
a merger/deletion decision
a superiority claim
an external-validation result
~~~

## 3. Shared artifact bundle

Every compared pair receives fair access to the same relevant records:

~~~text
declared computational target T

frozen source/model/interface versions

evaluation units / branch registry

typed Formation / Property statuses

dependency graph and cross-layer bridge register

target-relevance ledger

semantic-obligation ledger

execution-action candidates

reuse-equivalence / cache / invalidation records

aggregation readout and collision sidecar

compression retained-distinction / loss sidecar

measurement resolution / distinguishability sidecar

analysis structural decomposition

transformation map / preservation-loss sidecar

dynamic transition / locality / propagation sidecar

simulation model / trajectory-capable state representation

prediction target / future-relevance sidecar

tracking provenance/version/handoff links

lineage predecessor-successor identity records

audit criteria / evidence provenance / conformance record

candidate sufficient computation plans

optional cost/resource descriptors
~~~

No pair receives hidden claim-relevant information unavailable to its compared partner.

Fair access does not require identical task contracts.

## 4. Five-interface non-collapse rule

For each pair compare:

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

`EXACT_COLLAPSE` requires no material claim-relevant distinction across all five interfaces in the frozen fixture.

Shared data, maps, ledgers, sidecars, or workflow order are insufficient for collapse.

## 5. B1 — Computation vs Optimization

Shared overlap:

~~~text
candidate plans
constraints
dependency/cost descriptors
resource estimates
target definition
~~~

Frozen distinction:

~~~text
Computation:
  determine target-relative semantic obligations,
  fresh/reuse/symbolic/omission actions,
  and a sound bounded computation plan

Optimization:
  choose among admissible alternatives
  under an explicit objective / loss / utility and constraints
~~~

Outputs:

~~~text
Computation:
  obligation/action ledgers
  required/omitted/reused/symbolic sets
  bounded computation plan

Optimization:
  selected alternative / ranking / optimum
  objective value or optimality record
~~~

Failure distinction:

~~~text
Computation:
  a set of multiple sufficient plans may be a complete valid result

Optimization:
  requires the frozen objective/constraint semantics
  to rank or select among admissible plans
~~~

Guard:

~~~text
SUFFICIENT_COMPUTATION_PLAN != OPTIMAL_PLAN
COMPUTATION != OPTIMIZATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. B2 — Computation vs Aggregation

Shared overlap:

~~~text
input values
channel/support information
component terms
declared readout maps
collision/injectivity sidecars
~~~

Frozen distinction:

~~~text
Computation:
  decide which evaluations are required, omitted,
  reused, or symbolically discharged for target T

Aggregation:
  execute a declared combination/readout over admitted data
~~~

Outputs:

~~~text
Computation:
  computation plan and soundness ledgers

Aggregation:
  aggregate/readout plus support/collision/injectivity records
~~~

Failure distinction:

~~~text
Aggregation:
  may validly produce a noninjective readout

Computation:
  may not use that equality to merge source-level branches
  unless target-relative equivalence justifies it
~~~

Guard:

~~~text
AGGREGATION_OUTPUT != COMPUTATION_PLAN
AGGREGATE_EQUALITY != CACHE_EQUIVALENCE
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. B3 — Computation vs Compression

Shared overlap:

~~~text
source representation
reduced representation
retained distinctions
collision/loss sidecars
downstream target
~~~

Frozen distinction:

~~~text
Computation:
  omit or reuse evaluation only under a sound target-relative justification

Compression:
  intentionally reduce representation while preserving
  distinctions required by a declared downstream purpose
~~~

Outputs:

~~~text
Computation:
  evaluation/action plan + soundness obligations

Compression:
  compressed representation + retention/loss/collision ledger
~~~

Failure distinction:

~~~text
Computation:
  unsound omission is a method failure for target T

Compression:
  may succeed despite evaluating fewer bits/fields because
  its criterion is purpose-relative representation preservation
~~~

Guard:

~~~text
COMPRESSION_REDUCTION != COMPUTATION_OMISSION
REPRESENTATION_LOSS != COMPUTATIONAL_IRRELEVANCE
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. B4 — Computation vs Analysis

Shared overlap:

~~~text
same target structure
dependencies
components
relations
status-separated representations
~~~

Frozen distinction:

~~~text
Analysis:
  decompose and structurally re-express one declared target

Computation:
  decide which decomposed units must actually be evaluated
  or may be omitted/reused for a declared computational target
~~~

Outputs:

~~~text
Analysis:
  structural decomposition / re-expression

Computation:
  target-relative execution plan and soundness ledger
~~~

Failure distinction:

~~~text
Analysis:
  may correctly expose all components without deciding execution necessity

Computation:
  fails if it prunes a target-relevant unit without justification
~~~

Guard:

~~~text
ANALYSIS_DECOMPOSITION != COMPUTATION_PLAN
STRUCTURAL_COMPONENT != REQUIRED_EVALUATION_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. B5 — Computation vs Measurement

Shared overlap:

~~~text
resolution
distinguishability
readout candidates
error/tolerance
alternative states
~~~

Frozen distinction:

~~~text
Measurement:
  determine whether supplied/proposed observations
  discriminate declared alternatives at declared resolution

Computation:
  determine whether a computational resolution/approximation
  is sufficient for the frozen target and how to evaluate it
~~~

Outputs:

~~~text
Measurement:
  observation/distinguishability plan or evidence status

Computation:
  resolution/error ledger + evaluation plan
~~~

Failure distinction:

~~~text
Measurement:
  can identify a sufficient observation plan without executing computation

Computation:
  can use an already supplied measurement/readout interface
  without being the measurement operation itself
~~~

Guard:

~~~text
MEASUREMENT_RESOLUTION != COMPUTATION_RESOLUTION_DECISION
MEASUREMENT_PLAN != COMPUTATION_PLAN
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. B6 — Computation vs Simulation

Shared overlap:

~~~text
state variables
transition/update functions
dependency graph
time/regime
locality/propagation constraints
~~~

Frozen distinction:

~~~text
Computation:
  decide which update/evaluation operations are required
  for the declared simulation target

Simulation:
  execute model-consistent state evolution
  through the supplied temporal/update semantics
~~~

Outputs:

~~~text
Computation:
  bounded evaluation/update plan

Simulation:
  generated trajectory / state sequence / readout sequence
~~~

Failure distinction:

~~~text
Computation:
  may produce a valid plan without generating any trajectory

Simulation:
  requires correct state evolution under the supplied model
~~~

Guard:

~~~text
COMPUTATION_PLAN != SIMULATION_EXECUTION
REQUIRED_UPDATE_SET != GENERATED_TRAJECTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. B7 — Computation vs Prediction

Shared overlap:

~~~text
model outputs
target variables
future-time labels
uncertainty / tolerance
computed quantities
~~~

Frozen distinction:

~~~text
Computation:
  evaluate or plan the mathematical/model quantities
  required by a declared target

Prediction:
  assert relevance to a future external target
  under model/domain/evidence conditions
~~~

Outputs:

~~~text
Computation:
  computed result or computation plan

Prediction:
  future-target claim with prediction-specific validity status
~~~

Failure distinction:

~~~text
a computation can be exactly correct for its model
while the future-target prediction is empirically wrong or unsupported
~~~

Guard:

~~~text
COMPUTATION_RESULT != PREDICTION_CLAIM_BY_DEFAULT
MODEL_CALCULATION_CORRECTNESS != FUTURE_VALIDITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. B8 — Computation vs Transformation

Shared overlap:

~~~text
functions/maps
input/output representations
versioned source/target schemas
preservation/loss records
~~~

Frozen distinction:

~~~text
Transformation:
  map a supplied source object into a target representation/regime

Computation:
  decide whether that map or submap must be evaluated,
  may be reused, or may be omitted for target T
~~~

Outputs:

~~~text
Transformation:
  transformed object + preservation/loss ledger

Computation:
  evaluation/action plan + target result/ledgers
~~~

Failure distinction:

~~~text
Transformation:
  may be correct even when every map component was executed

Computation:
  may soundly avoid executing some map components
  if they are proven irrelevant to the computational target
~~~

Guard:

~~~text
TRANSFORMATION_RESULT != REUSE_VALIDITY
TRANSFORMATION_STEP != REQUIRED_EVALUATION_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. B9 — Computation vs Audit

Shared overlap:

~~~text
frozen task/protocol
execution records
soundness obligations
provenance
maximum-supported claim
~~~

Frozen distinction:

~~~text
Computation:
  determine/execute the target-relative evaluation plan

Audit:
  retrace and evaluate performed work/evidence/procedure
  against frozen audit criteria
~~~

Outputs:

~~~text
Computation:
  substantive computation plan/result + conformance field

Audit:
  criterion-by-criterion audit findings/verdict
~~~

Failure distinction:

~~~text
Computation:
  a BLOCKED/CONFLICTING/UNDERDETERMINED terminal
  may be protocol-conformant

Audit:
  may pass precisely because the bounded terminal
  and evidence handling were correct
~~~

Guard:

~~~text
SOUNDNESS_AUDIT != COMPUTATION_PLAN
COMPUTATION_PROTOCOL_CONFORMANCE != GENERAL_AUDIT_PASS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 14. B10 — Computation vs Tracking

Shared overlap:

~~~text
versioned artifacts
cache/provenance records
source/model identities
handoff/dependency references
execution records
~~~

Frozen distinction:

~~~text
Tracking:
  establish supported trace links for origin/version/process/
  location/handoff/status/reference/evidence

Computation:
  determine target-relative evaluation obligations and actions
~~~

Outputs:

~~~text
Tracking:
  trace graph/path/link-status/evidence ledger

Computation:
  computation plan + obligation/action/soundness ledgers
~~~

Failure distinction:

~~~text
Tracking:
  a missing trace link remains a trace gap

Computation:
  missing required provenance may BLOCK reuse,
  but it does not infer a trace link
~~~

Guard:

~~~text
TRACKING_PROVENANCE != REUSE_VALIDITY
TRACKED_EXECUTION != COMPUTATION_NECESSITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 15. B11 — Computation vs Lineage

Shared overlap:

~~~text
state identity
version/regime changes
predecessor/successor records
transition context
reuse invalidation
~~~

Frozen distinction:

~~~text
Lineage:
  establish predecessor-successor identity/continuity across change

Computation:
  consume such identity/transition records to decide
  whether prior computation may remain reusable
~~~

Outputs:

~~~text
Lineage:
  successor/identity/coherence ledgers

Computation:
  reuse validity/action and bounded computation plan
~~~

Failure distinction:

~~~text
Lineage:
  may remain unresolved about successor identity

Computation:
  may then mark cross-transition reuse BLOCKED or UNDERDETERMINED
  without establishing lineage itself
~~~

Guard:

~~~text
LINEAGE_HANDOFF != COMPUTATION_EXECUTION
REUSE_INVALIDATION != LINEAGE_IDENTITY_PROOF
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 16. Source-layer handoff separation

Computation legitimately consumes constraints from:

~~~text
Formation
Property
Static Aggregation
Structural Reorganization Dynamics
~~~

but source-layer operationalization does not establish method identity.

Required guards:

~~~text
SOURCE_LAYER_HANDOFF != METHOD_IDENTITY
OPERATIONALIZATION != SOURCE_DEFINITION_REPLACEMENT
FORMATION_STAGE_ORDER != RUNTIME_SCHEDULE
FINITE_PROPAGATION_SPECIALIZATION != UNIVERSAL_COMPUTATION_RULE
~~~

Expected:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## 17. Frozen scoring — 99 checks

Each pair receives nine checks.

For every pair B1-B11:

~~~text
-1 shared artifact access fair
-2 INPUTS overlap/difference recorded without identity claim
-3 OPERATION distinction preserved
-4 OUTPUTS distinction preserved
-5 FAILURE/NO_GAIN distinction preserved
-6 VALIDATION_STANDARD distinction preserved
-7 semantic guard preserved
-8 pair result PARTIAL_OVERLAP_NOT_COLLAPSE
-9 no permanent irreducibility/superiority claim
~~~

Expected:

~~~text
B1 Computation vs Optimization: 9/9
B2 Computation vs Aggregation: 9/9
B3 Computation vs Compression: 9/9
B4 Computation vs Analysis: 9/9
B5 Computation vs Measurement: 9/9
B6 Computation vs Simulation: 9/9
B7 Computation vs Prediction: 9/9
B8 Computation vs Transformation: 9/9
B9 Computation vs Audit: 9/9
B10 Computation vs Tracking: 9/9
B11 Computation vs Lineage: 9/9

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

Counter update on full pass:

~~~text
DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  2 -> 3

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  2 -> 3

METHOD_BOUNDARY_COMPUTATION_CASES:
  0 -> 1
~~~

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.

## 19. Interpretation lock

~~~text
FIXTURE_BOUNDED_SEPARATION
  !=
PERMANENT_METHOD_IRREDUCIBILITY

PARTIAL_OVERLAP_NOT_COLLAPSE
  !=
METHOD_SUPERIORITY

NO_EXACT_COLLAPSE_IN_THIS_FIXTURE
  !=
PERMANENT_REGISTRY_SURVIVAL

SHARED_INPUT
  !=
SHARED_METHOD_IDENTITY

SHARED_OUTPUT_ARTIFACT
  !=
SHARED_OPERATION
~~~

## 20. Next

If the frozen bundle passes, proceed to COMP-CH-004, a fair competent non-DSD Computation baseline challenge.

The baseline must receive equal claim-relevant information and must permit `COMPUTATION_NO_GAIN` as a valid outcome.
