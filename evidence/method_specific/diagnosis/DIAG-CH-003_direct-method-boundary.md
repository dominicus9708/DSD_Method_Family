# DIAG-CH-003 — Direct Neighboring-Method Diagnosis Boundary Challenge Result

Status: **EXECUTED — 90/90 PASS**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-003`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

PRECOMMIT_COMMIT:
  8b21d04280c5c54e5897033acd8a42fbaffdd26c

PRECOMMIT_BLOB:
  299f1d74a60f0da07746abde6fa677f8c6c5d3f9
~~~

No compared-method boundary, shared artifact, pair expectation, semantic guard, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  90

PASSED:
  90

FAILED:
  0

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

All ten pairs received fair access to the same claim-relevant shared artifact bundle.

This result is fixture-bounded.

It does not establish permanent irreducibility, method superiority, permanent registry survival, or a merger/deletion decision.

## 3. Diagnosis vs Measurement

Five-interface assessment:

~~~text
INPUTS:
  partial overlap

shared:
  alternatives/candidates
  readouts
  resolution
  typed status/provenance
  discrimination-related evidence

OPERATION:
  distinct

Diagnosis:
  infer which current-state / failure-mode / cause candidates
  remain compatible with observed evidence

Measurement:
  evaluate whether candidate observations/readouts can discriminate
  declared alternatives at declared resolution

OUTPUTS:
  distinct

Diagnosis:
  candidate-disposition ledger
  compatible/excluded/blocked/unresolved sets
  identifiability outcome

Measurement:
  discrimination profile
  measurement-plan sufficiency / insufficiency record

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Diagnosis:
  can be BLOCKED without a required observed result

Measurement:
  can establish a sufficient plan before an observed result exists

VALIDATION_STANDARD:
  distinct

Diagnosis:
  candidate dispositions must follow frozen evidence/bridge semantics

Measurement:
  readout plan must discriminate required alternatives under
  frozen measurement semantics
~~~

Preserved:

~~~text
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
DISCRIMINATING_READOUT != DIAGNOSED_STATE
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 4. Diagnosis vs Reconstruction

Five-interface assessment:

~~~text
INPUTS:
  substantial overlap

shared:
  candidate structures
  evidence
  collision/injectivity records
  transition constraints

OPERATION:
  distinct

Diagnosis:
  current hidden-state / condition / failure-mode / cause compatibility

Reconstruction:
  prior / omitted / damaged / compressed structure or history inference

OUTPUTS:
  distinct

Diagnosis:
  current candidate set + identifiability record

Reconstruction:
  compatible prior/hidden structure set + reconstruction scope

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Diagnosis:
  can identify a current state while past histories remain multiple

Reconstruction:
  can recover a prior structure without establishing current cause

VALIDATION_STANDARD:
  distinct

Diagnosis:
  present-evidence compatibility under current-state claim scope

Reconstruction:
  inverse recovery bounded by evidence and reconstruction conditions
~~~

Preserved:

~~~text
CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION
RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 5. Diagnosis vs Classification

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  observed object/evidence
  candidate labels
  typed features/statuses
  criteria

OPERATION:
  distinct

Diagnosis:
  infer compatibility of hidden/current-state hypotheses

Classification:
  assign supplied objects to declared classes

OUTPUTS:
  distinct

Diagnosis:
  candidate compatibility sets and identifiability

Classification:
  class membership / assignment record

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Classification:
  may succeed while several hidden-state candidates remain compatible

Diagnosis:
  may preserve several candidates mapping to one visible class

VALIDATION_STANDARD:
  distinct

Diagnosis:
  bridge/evidence compatibility

Classification:
  criterion-traceable class assignment
~~~

Preserved:

~~~text
CLASSIFICATION_RESULT != DIAGNOSIS_RESULT
CLASS_LABEL != HIDDEN_STATE_IDENTITY
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 6. Diagnosis vs Comparison

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  candidate/evidence objects
  difference/residual information
  resolution
  comparison criteria

OPERATION:
  distinct

Diagnosis:
  combine evidence-to-candidate relations into candidate disposition
  and candidate-set identifiability

Comparison:
  evaluate correspondence/divergence/equivalence between supplied targets

OUTPUTS:
  distinct

Diagnosis:
  admissible/excluded candidate sets

Comparison:
  correspondence/divergence/equivalence profile

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Comparison:
  a difference can be validly reported without excluding either object

Diagnosis:
  exclusion requires the frozen Diagnosis bridge and combination rule

VALIDATION_STANDARD:
  distinct

Diagnosis:
  candidate result must be supported by all claim-relevant frozen interfaces

Comparison:
  relation must follow frozen comparison criterion
~~~

Preserved:

~~~text
COMPARISON_SIMILARITY != DIAGNOSIS_COMPATIBILITY
PAIRWISE_DIFFERENCE != CANDIDATE_EXCLUSION_BY_DEFAULT
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 7. Diagnosis vs Prediction

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  state candidates
  model/bridge
  time/regime
  dynamic constraints

OPERATION:
  opposite directional role in the fixture

Diagnosis:
  present evidence -> compatible current candidates

Prediction:
  supplied state/model -> future outcome set

OUTPUTS:
  distinct

Diagnosis:
  current candidate set

Prediction:
  future conditional outcome set

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Prediction:
  may be valid conditionally for several alternative current states

Diagnosis:
  may remain multiple-compatible and cannot choose one state
  merely because predictions are available

VALIDATION_STANDARD:
  distinct

Diagnosis:
  inverse compatibility with present evidence

Prediction:
  forward consequence under supplied assumptions
~~~

Preserved:

~~~text
PREDICTION_OUTPUT != CURRENT_DIAGNOSIS
FORWARD_CONSEQUENCE != INVERSE_STATE_IDENTIFICATION
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 8. Diagnosis vs Simulation

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  state representation
  dynamic model
  transition relation
  time/regime
  readout generation

OPERATION:
  distinct

Diagnosis:
  infer candidate compatibility from observed evidence

Simulation:
  execute model evolution from supplied initial/state assumptions

OUTPUTS:
  distinct

Diagnosis:
  evidence-conditioned candidate dispositions

Simulation:
  generated trajectory/readout records

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Simulation:
  may correctly generate a hypothetical trajectory

Diagnosis:
  may not treat that generated trajectory as observed evidence
  without an explicit valid handoff

VALIDATION_STANDARD:
  distinct

Diagnosis:
  observed-evidence compatibility and scope discipline

Simulation:
  correct execution of supplied model/state evolution
~~~

Preserved:

~~~text
SIMULATION_TRAJECTORY != OBSERVED_STATE
SIMULATED_MATCH != DIAGNOSIS_BY_DEFAULT
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 9. Diagnosis vs Optimization

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  candidate set
  constraints
  evidence-derived records
  possible actions/measurements

OPERATION:
  distinct

Diagnosis:
  filter candidates by compatibility

Optimization:
  select feasible alternatives by objective/loss/utility/order

OUTPUTS:
  distinct

Diagnosis:
  compatible/excluded/blocked/unresolved candidate sets

Optimization:
  selected optimum / ordered alternatives / objective value

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Diagnosis:
  multiple compatible candidates may be a valid final result

Optimization:
  may select one alternative if an objective breaks the tie

VALIDATION_STANDARD:
  distinct

Diagnosis:
  evidence-consistent candidate disposition

Optimization:
  objective/constraint-consistent selection
~~~

Preserved:

~~~text
CANDIDATE_COMPATIBILITY != OPTIMALITY
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
NEED_FOR_ADDITIONAL_OBSERVATION != OPTIMAL_MEASUREMENT_SELECTED
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 10. Diagnosis vs Audit

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  frozen protocol/task
  evidence provenance
  status ledgers
  maximum-supported claim

OPERATION:
  distinct

Diagnosis:
  perform candidate compatibility inference

Audit:
  retrace/evaluate performed work against frozen audit criteria

OUTPUTS:
  distinct

Diagnosis:
  substantive Diagnosis result + protocol conformance record

Audit:
  audit verdict / criterion-by-criterion trace

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Diagnosis:
  NOT_ESTABLISHED/BLOCKED/CONFLICTING/UNDERDETERMINED
  may be valid conformant outputs

Audit:
  may pass precisely because the negative Diagnosis terminal
  was produced correctly

VALIDATION_STANDARD:
  distinct

Diagnosis:
  frozen inference semantics followed

Audit:
  frozen audit scope/criteria satisfied
~~~

Preserved:

~~~text
AUDIT_PASS != DIAGNOSIS_RESULT
DIAGNOSIS_PROTOCOL_CONFORMANCE != TRUE_STATE_CERTAINTY
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 11. Diagnosis vs Tracking

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  evidence identity
  provenance
  version
  time
  handoff links
  bridge versions

OPERATION:
  distinct

Diagnosis:
  infer candidate compatibility under frozen evidence/bridge semantics

Tracking:
  record supported provenance/version/process/location/handoff relations

OUTPUTS:
  distinct

Diagnosis:
  candidate disposition and identifiability

Tracking:
  provenance/version/handoff trace

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Tracking:
  can succeed while evidence remains non-discriminating

Diagnosis:
  can use a valid trace without performing provenance tracking itself

VALIDATION_STANDARD:
  distinct

Diagnosis:
  compatibility result reproducible from evidence and bridge

Tracking:
  trace relations supported by recorded provenance/handoff evidence
~~~

Preserved:

~~~text
TRACKING_TRACE != DIAGNOSIS_RESULT
PROVENANCE_CHAIN != HIDDEN_STATE_IDENTIFICATION
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 12. Diagnosis vs Lineage

Five-interface assessment:

~~~text
INPUTS:
  overlap

shared:
  state identities
  transition/succession records
  time
  predecessor-successor constraints

OPERATION:
  distinct

Diagnosis:
  determine which current candidates remain compatible

Lineage:
  determine predecessor-successor identity/continuity across change

OUTPUTS:
  distinct

Diagnosis:
  current-state/failure/cause candidate set

Lineage:
  lineage identity / continuity / predecessor-successor record

FAILURE_OR_NO_GAIN_CRITERIA:
  distinct

Lineage:
  may establish continuity without resolving current hidden failure mode

Diagnosis:
  may identify a current failure mode without proving unique lineage history

VALIDATION_STANDARD:
  distinct

Diagnosis:
  current evidence compatibility

Lineage:
  supported continuity/identity relation across change
~~~

Preserved:

~~~text
LINEAGE_IDENTITY != CURRENT_DIAGNOSIS
CURRENT_STATE_DIAGNOSIS != UNIQUE_LINEAGE_HISTORY
~~~

Pair result:

~~~text
PARTIAL_OVERLAP_NOT_COLLAPSE
~~~

## 13. Source-handoff separation

Diagnosis consumed or may consume source/interface artifacts from:

~~~text
Formation
Property
Static Aggregation
Dynamics
Measurement
~~~

but no source-layer or predecessor-method handoff was counted as method identity.

Result:

~~~text
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

Preserved:

~~~text
SOURCE_OR_METHOD_HANDOFF != METHOD_IDENTITY
~~~

## 14. Execution of the 90 frozen checks

For each pair, all nine frozen checks passed.

~~~text
B1 Diagnosis vs Measurement:
  9/9 PASS

B2 Diagnosis vs Reconstruction:
  9/9 PASS

B3 Diagnosis vs Classification:
  9/9 PASS

B4 Diagnosis vs Comparison:
  9/9 PASS

B5 Diagnosis vs Prediction:
  9/9 PASS

B6 Diagnosis vs Simulation:
  9/9 PASS

B7 Diagnosis vs Optimization:
  9/9 PASS

B8 Diagnosis vs Audit:
  9/9 PASS

B9 Diagnosis vs Tracking:
  9/9 PASS

B10 Diagnosis vs Lineage:
  9/9 PASS
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  90

PASSED:
  90

FAILED:
  0
~~~

## 15. Aggregate boundary result

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

The result supports fixture-level separation only.

It does not establish permanent irreducibility.

## 16. Post-challenge state

~~~text
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  3

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  3

POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  10

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level

BASELINE_DIAGNOSIS_CASES:
  0

NO_GAIN_DIAGNOSIS_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_DIAGNOSIS_APPLICATIONS:
  0

INDEPENDENT_DIAGNOSIS_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

DIAGNOSIS_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 17. Interpretation lock

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

## 18. Next

Proceed to a fair competent non-DSD Diagnosis baseline challenge.
