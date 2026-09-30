# DIAG-CH-003 — Direct Neighboring-Method Diagnosis Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-003`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129
~~~

The frozen Diagnosis protocol may not be edited in response to this challenge.

## 2. Purpose

Test whether Diagnosis collapses into neighboring Method Family methods when every pair receives fair access to the same claim-relevant artifact bundle.

The challenge tests ten neighboring methods:

~~~text
Measurement
Reconstruction
Classification
Comparison
Prediction
Simulation
Optimization
Audit
Tracking
Lineage
~~~

This is a fixture-bounded method-boundary test.

It is not:

~~~text
a permanent irreducibility proof
a method-survival vote
a method-superiority claim
a merger/deletion decision
an external-validation result
~~~

## 3. Shared artifact bundle

Every compared pair receives the same claim-relevant constructed records:

~~~text
declared Diagnosis question
candidate class / candidate identities
candidate-class completeness status

evidence set
evidence statuses
provenance / time / regime
evidence-set coherence status

evidence-to-candidate bridge
bridge version / applicability scope
pair compatibility matrix

required-interface ledger
Property / Formation typed-status handoffs
support-retention sidecars
readout / collision / injectivity records

residual target / carrier / rule
transition relation / dynamic-support record

candidate-disposition ledger
compatible / excluded / blocked / conflicting / unresolved sets
candidate-set outcome
identifiability scope

cause-claim scope
maximum-supported claim
additional-observation handoff

protocol-conformance record
~~~

Neighbor-specific sidecars are also shared when relevant:

~~~text
Measurement:
  alternative set
  candidate readouts
  declared resolution
  discrimination profile

Reconstruction:
  prior / omitted / damaged structure candidates
  predecessor-history candidates
  reconstruction prerequisites
  uniqueness/nonuniqueness record

Classification:
  class schema
  criterion-traceable class assignments

Comparison:
  correspondence / divergence records

Prediction:
  supplied current state/model
  future-outcome relation

Simulation:
  supplied initial state/model
  trajectory execution record

Optimization:
  objective / constraints / feasible set
  selection rule

Audit:
  frozen audit scope
  evidence provenance
  criteria / conformance record

Tracking:
  provenance / version / handoff links

Lineage:
  predecessor-successor identity / continuity records
~~~

No neighboring method receives hidden claim-relevant information unavailable to Diagnosis.

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

Shared evidence, readouts, models, maps, candidates, ledgers, or workflow handoffs are insufficient for collapse.

## 5. B1 — Diagnosis vs Measurement

Shared overlap:

~~~text
alternatives/candidates
readouts
resolution
status/provenance
discrimination-related evidence
~~~

Frozen distinction:

~~~text
Diagnosis:
  infer which declared current-state / failure-mode / cause candidates
  remain compatible with frozen present evidence

Measurement:
  determine whether candidate observations/readouts can discriminate
  declared alternatives at a declared resolution
~~~

Failure distinction:

~~~text
Measurement:
  may establish a sufficient discrimination plan before any actual
  observed result selects a current candidate

Diagnosis:
  may remain BLOCKED without the required observed evidence even when
  the Measurement plan is sufficient
~~~

Guard:

~~~text
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
DISCRIMINATING_READOUT != DIAGNOSED_STATE
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. B2 — Diagnosis vs Reconstruction

Shared overlap:

~~~text
candidate structures
evidence
readout collisions
injectivity/nonuniqueness records
transition constraints
~~~

Frozen distinction:

~~~text
Diagnosis:
  primarily current hidden-state / current-condition /
  failure-mode / cause-hypothesis compatibility

Reconstruction:
  infer prior / omitted / damaged / compressed structures
  or histories compatible with evidence
~~~

Failure distinction:

~~~text
Diagnosis:
  may uniquely identify the current declared state

Reconstruction:
  may still preserve multiple compatible predecessor histories

or

Reconstruction:
  may recover a prior structure without establishing which
  present cause hypothesis is true
~~~

Guard:

~~~text
CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION
RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. B3 — Diagnosis vs Classification

Shared overlap:

~~~text
candidate labels
typed features/statuses
criteria
observed object/evidence
~~~

Frozen distinction:

~~~text
Diagnosis:
  evaluate evidence compatibility of hypotheses about hidden/current state

Classification:
  assign supplied objects to declared classes under frozen class semantics
~~~

Failure distinction:

~~~text
Classification:
  may assign an observed artifact to class K without explaining
  which hidden-state hypothesis generated it

Diagnosis:
  may preserve several compatible hidden states even if all map
  to the same visible class
~~~

Guard:

~~~text
CLASSIFICATION_RESULT != DIAGNOSIS_RESULT
CLASS_LABEL != HIDDEN_STATE_IDENTITY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. B4 — Diagnosis vs Comparison

Shared overlap:

~~~text
candidate/evidence objects
correspondence criteria
difference/residual information
resolution
~~~

Frozen distinction:

~~~text
Diagnosis:
  combine evidence-to-candidate relations to determine candidate disposition
  and candidate-set identifiability

Comparison:
  evaluate correspondence/divergence/equivalence between supplied targets
  under frozen comparison criteria
~~~

Failure distinction:

~~~text
Comparison:
  can report exact similarity/difference without deciding
  whether a candidate remains admissible under the full Diagnosis task

Diagnosis:
  can exclude a candidate only under the frozen claim-relevant
  bridge and evidence-combination semantics
~~~

Guard:

~~~text
COMPARISON_SIMILARITY != DIAGNOSIS_COMPATIBILITY
PAIRWISE_DIFFERENCE != CANDIDATE_EXCLUSION_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. B5 — Diagnosis vs Prediction

Shared overlap:

~~~text
state candidates
model/bridge
time/regime
dynamic constraints
outcome relations
~~~

Frozen distinction:

~~~text
Diagnosis:
  inverse-style inference from present evidence to compatible
  current-state/cause candidates

Prediction:
  forward inference from supplied state/model assumptions
  to future outcomes
~~~

Failure distinction:

~~~text
Prediction:
  may be valid conditional on each of several possible current states

Diagnosis:
  may remain multiple-compatible and therefore not select one
  current state merely because predictions can be generated
~~~

Guard:

~~~text
PREDICTION_OUTPUT != CURRENT_DIAGNOSIS
FORWARD_CONSEQUENCE != INVERSE_STATE_IDENTIFICATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. B6 — Diagnosis vs Simulation

Shared overlap:

~~~text
state representation
dynamic model
transition relation
time/regime
readout generation
~~~

Frozen distinction:

~~~text
Diagnosis:
  infer candidate compatibility from observed evidence

Simulation:
  execute supplied model evolution from supplied initial/state assumptions
  to generated trajectories/readouts
~~~

Failure distinction:

~~~text
Simulation:
  may correctly generate a trajectory from a hypothetical initial state

Diagnosis:
  cannot treat a simulated trajectory as an observed fact
  unless a valid evidence bridge supplies that role
~~~

Guard:

~~~text
SIMULATION_TRAJECTORY != OBSERVED_STATE
SIMULATED_MATCH != DIAGNOSIS_BY_DEFAULT
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. B7 — Diagnosis vs Optimization

Shared overlap:

~~~text
candidate set
constraints
scores or evidence-derived records
possible additional-observation actions
~~~

Frozen distinction:

~~~text
Diagnosis:
  determine compatible / excluded / blocked / unresolved candidates

Optimization:
  select among feasible alternatives according to an explicit
  objective / loss / utility / ordering rule
~~~

Failure distinction:

~~~text
Diagnosis:
  may legitimately return several compatible candidates without ranking them

Optimization:
  may select one action/candidate despite compatibility ties if
  an objective resolves them
~~~

Guard:

~~~text
CANDIDATE_COMPATIBILITY != OPTIMALITY
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
NEED_FOR_ADDITIONAL_OBSERVATION != OPTIMAL_MEASUREMENT_SELECTED
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. B8 — Diagnosis vs Audit

Shared overlap:

~~~text
frozen task/protocol
evidence provenance
status ledgers
conformance records
maximum-supported claim
~~~

Frozen distinction:

~~~text
Diagnosis:
  execute current-state/cause compatibility inference

Audit:
  retrace and evaluate performed work/evidence/procedure
  against a frozen audit scope and criteria
~~~

Failure distinction:

~~~text
a Diagnosis task may validly return NOT_ESTABLISHED, BLOCKED,
CONFLICTING, or UNDERDETERMINED and still be protocol-conformant

an Audit may pass because that terminal was produced correctly
rather than because the Diagnosis claim was established
~~~

Guard:

~~~text
AUDIT_PASS != DIAGNOSIS_RESULT
DIAGNOSIS_PROTOCOL_CONFORMANCE != TRUE_STATE_CERTAINTY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. B9 — Diagnosis vs Tracking

Shared overlap:

~~~text
evidence identity
provenance
version
time
handoff links
bridge-version records
~~~

Frozen distinction:

~~~text
Diagnosis:
  infer candidate compatibility under frozen evidence/bridge semantics

Tracking:
  record supported provenance/version/process/location/handoff relations
~~~

Failure distinction:

~~~text
Tracking:
  may perfectly trace evidence provenance while the evidence
  remains non-discriminating between Diagnosis candidates

Diagnosis:
  may establish compatibility using supplied provenance without
  itself being the provenance-tracking method
~~~

Guard:

~~~text
TRACKING_TRACE != DIAGNOSIS_RESULT
PROVENANCE_CHAIN != HIDDEN_STATE_IDENTIFICATION
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 14. B10 — Diagnosis vs Lineage

Shared overlap:

~~~text
state identities
transition/succession records
time
predecessor-successor constraints
~~~

Frozen distinction:

~~~text
Diagnosis:
  decide which current candidates remain compatible with evidence

Lineage:
  establish predecessor-successor identity/continuity across change
~~~

Failure distinction:

~~~text
Lineage:
  may establish that current object U descends from predecessor P
  without resolving which hidden failure mode currently applies

Diagnosis:
  may identify a current failure mode without proving a unique
  predecessor-successor identity chain
~~~

Guard:

~~~text
LINEAGE_IDENTITY != CURRENT_DIAGNOSIS
CURRENT_STATE_DIAGNOSIS != UNIQUE_LINEAGE_HISTORY
~~~

Expected:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 15. Source-handoff separation lock

Diagnosis may consume source/interface artifacts from:

~~~text
Formation
Property
Static Aggregation
Dynamics
Measurement
~~~

but source-layer or predecessor-method handoff does not by itself establish method identity.

Required guard:

~~~text
SOURCE_OR_METHOD_HANDOFF != METHOD_IDENTITY
~~~

Expected:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## 16. Frozen scoring — 90 checks

Each method pair receives nine checks.

For every pair B1-B10:

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

Expanded expected totals:

~~~text
B1 Diagnosis vs Measurement:
  9/9

B2 Diagnosis vs Reconstruction:
  9/9

B3 Diagnosis vs Classification:
  9/9

B4 Diagnosis vs Comparison:
  9/9

B5 Diagnosis vs Prediction:
  9/9

B6 Diagnosis vs Simulation:
  9/9

B7 Diagnosis vs Optimization:
  9/9

B8 Diagnosis vs Audit:
  9/9

B9 Diagnosis vs Tracking:
  9/9

B10 Diagnosis vs Lineage:
  9/9

TOTAL_REQUIRED_CHECKS:
  90

PASS_THRESHOLD:
  90/90

PARTIAL_PASS_ALLOWED:
  no
~~~

## 17. Expected aggregate boundary result

If all 90 checks pass:

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  10

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
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  3

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  3

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1
~~~

## 18. Next

If the frozen bundle passes, proceed to a fair competent non-DSD Diagnosis baseline challenge.
