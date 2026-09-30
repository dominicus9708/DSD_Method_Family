# DSD Diagnosis — Planning / Validation Roadmap

Status: **Diagnosis Protocol v0.1 internally standardized / DIAG-AUD-001 28/28 PASS / external validation deferred**  
Date: **2026-10-01**

## 1. Goal

Develop Diagnosis / DSD 진단론 as an independent DSD method for determining which declared current hidden states, failure modes, cause hypotheses, or structural conditions remain compatible with present evidence.

Diagnosis is not allowed to silently become:

~~~text
Measurement
Reconstruction
Prediction
Simulation
Classification
Comparison
Audit
Optimization
causal proof
~~~

## 2. Recovered source basis

Canonical recovery artifact:

~~~text
SOURCE_REGISTRY:
  SOURCE_REGISTRY_v0.1.md

SOURCE_REGISTRY_COMMIT:
  63ccc25d5bc8ddadadabfe698852d846e5671f15

SOURCE_REGISTRY_BLOB:
  1152759be5b56462156c83ecd3c508c73f1755f7
~~~

Recovered predecessor classes:

~~~text
Formation:
  typed assignment/channel status
  strict-vs-composite equivalence
  staged comparison / first branching

Property:
  declaration/profile/applicability/prerequisite/definedness
  defined zero vs defined nonzero/value
  complete typed-input retention

Static Aggregation:
  support-retaining data
  aggregate collision / injectivity
  reconstruction limits
  cross-coordinate information loss

Dynamics:
  typed residuals
  relation-valued transitions
  descriptive projections
  latent distinctions
  reduced readouts

Measurement:
  discrimination/evidence handoffs
  resolution / decision-rule / temporal scope
  information-loss and dynamic-support records

Registry boundary:
  Diagnosis current hidden-state/current-condition inference
  vs Reconstruction prior/omitted/history inference
~~~

## 3. Canonical internal-build sequence

1. ✅ Registry recovery.
2. ✅ Source recovery and source-derived constraint extraction.
3. ✅ Task Interface v0.1 draft.
4. ✅ Pre-protocol boundary counterexamples — 18 attacks / 13 preserved / 5 nonbreaking refinements.
5. ✅ Boundary Amendment 001 — 5/5 refinements adopted / Protocol freeze authorized.
6. ✅ Executable Diagnosis Protocol v0.1.
7. ✅ Positive constructed challenge.
8. ✅ Negative / blocked / unresolved terminal coverage.
9. ✅ Direct neighboring-method boundary challenge.
10. ✅ Competent non-DSD baseline.
11. ✅ Strongest-reasonable non-DSD baseline.
12. ✅ Deterministic same-project retrace — 70/70 PASS / 0 claim-relevant mismatches.
13. ✅ Frozen-axis internal standardization audit — 28/28 PASS / PROMOTE_INTERNAL_STANDARD.
14. ⏸ External applications / independent validation — separate later phase; deferred by sequence.

## 4. Working five-interface identity — not yet frozen

~~~text
INPUTS:
  declared diagnosis question
  declared candidate class
  present observation/evidence records
  typed status/applicability/provenance
  explicit evidence-to-candidate bridge or forward model
  claim-relevant resolution / time / regime
  optional support / residual / transition / measurement handoffs
  optional causal bridge for causal claims

OPERATION:
  evaluate every declared candidate against frozen evidence and bridge semantics;
  preserve missing, conflicting, inapplicable, and unresolved states;
  compute admissible/excluded/evaluation-blocked candidates;
  record identifiability within the declared class;
  bound any causal or uniqueness claim

OUTPUTS:
  candidate register
  evidence-to-candidate compatibility ledger
  admissible candidate set
  excluded candidate set
  blocked / unresolved candidate records
  identifiability record
  remaining-discriminator / additional-observation handoff
  causal-claim scope
  maximum-supported claim

FAILURE_OR_NO_GAIN:
  required bridge absent
  status/provenance collapsed
  post-hoc candidate or rule change
  unsupported uniqueness
  unsupported causal promotion
  hidden reconstruction/prediction/optimization
  no claim-relevant advantage over fair baseline

VALIDATION_STANDARD:
  every candidate disposition reproducible from frozen evidence;
  multiplicity preserved when warranted;
  unavailable evidence not treated as negative evidence;
  no fabricated observation, causal proof, or history;
  maximum claim remains candidate-class and evidence scoped
~~~

## 5. High-priority boundary questions

~~~text
Q1
  multiple admissible candidates
  vs underdetermined task semantics

Q2
  zero compatible declared candidates
  vs evidence conflict / model mismatch

Q3
  one surviving declared candidate
  vs globally unique diagnosis

Q4
  current hidden-state diagnosis
  vs past-history reconstruction

Q5
  compatibility with a cause hypothesis
  vs causal proof

Q6
  measurement plan sufficiency
  vs diagnosis result

Q7
  residual match
  vs state identity

Q8
  noninjective forward/readout map
  vs arbitrary preimage selection

Q9
  additional-observation request
  vs Measurement / Optimization task execution

Q10
  candidate ranking / posterior probability
  vs compatibility filtering
~~~

## 6. Prospective non-substitution guards

These remain candidates until boundary attack:

~~~text
OBSERVATION_COMPATIBLE != TRUE_STATE_ESTABLISHED
SINGLE_REMAINING_DECLARED_CANDIDATE != GLOBAL_UNIQUE_DIAGNOSIS
NO_ADMISSIBLE_DECLARED_CANDIDATE != NO_REAL_STATE_EXISTS
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
RESIDUAL_MATCH != CAUSE_ESTABLISHED
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
EQUAL_READOUT != EQUAL_HIDDEN_STATE
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
PROBABILITY != COMPATIBILITY
~~~

## 7. Current evidence counters

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

DEDICATED_DIAGNOSIS_PROTOCOL:
  established v0.1

PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18

TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  13

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  5

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  5

POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

BASELINE_DIAGNOSIS_CASES:
  2

NO_GAIN_DIAGNOSIS_CASES:
  2

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

CLAIM_RELEVANT_MISMATCHES:
  0

POST_COMPARISON_CORRECTIONS:
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

## Task Interface v0.1

~~~text
TASK_INTERFACE_COMMIT:
  e2c636eb0751878423a35d6848f7ef5a8fe81cc3

TASK_INTERFACE_BLOB:
  8cc12899c9b3f7a5f78d0e1893c5aa3a3824d444

TASK_INTERFACE_STATUS:
  historical draft once boundary attack begins
~~~

The draft separates:

~~~text
candidate compatibility
candidate-set identifiability
task status
task terminal
cause-claim scope
information-loss / noninjectivity
current-state Diagnosis
past-history Reconstruction
~~~

## Boundary attack result

~~~text
BOUNDARY_ATTACK_COMMIT:
  f930b29b1422f4306fa38e8063edd9a8a3ed8118

BOUNDARY_ATTACK_BLOB:
  50de1b4ccb64264cf100a573f3831b8e2d1c7057

BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
BOUNDARY_AMENDMENT_REQUIRED: yes
PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT: no
SHARED_CORE_REOPEN_REQUIRED: no
~~~

Required refinement groups:

~~~text
R1 evidence-set coherence / conflict semantics
R2 bridge-rule conflict / pair-conflict semantics
R3 required-interface availability / BLOCKED semantics
R4 deterministic vs explicit probabilistic inference mode
R5 task-terminal precedence / PARTIAL semantics
~~~

## Boundary Amendment 001

~~~text
AMENDMENT_COMMIT:
  eb51b70765a69277aeabe4152260431c970b95e5

AMENDMENT_BLOB:
  c5b9fde42828d67f77a7e92d3a588cb6a7aeca2d

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  5/5

PROTOCOL_FREEZE_AUTHORIZED:
  yes

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## Diagnosis Protocol v0.1

~~~text
PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

DEDICATED_DIAGNOSIS_PROTOCOL:
  established v0.1

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

## DIAG-CH-001

~~~text
PRECOMMIT_COMMIT: 2d832246197b9ed474962c10732fa2196ed065a5
PRECOMMIT_BLOB: 53874c7c53115373b358b467eeb79682bade5034
RESULT_COMMIT: 6a182dce0976a25b6317e9c9af85b8317781d88b
RESULT_BLOB: 591e9aaeba8176b7a535c979851064294aef0c56
CHECKS: 80/80 PASS
~~~

~~~text
A: MULTIPLE_COMPATIBLE / TASK_ESTABLISHED
B: UNIQUE_WITHIN_DECLARED_CLASS / TASK_ESTABLISHED
C: CAUSE_COMPATIBILITY_ONLY / TASK_ESTABLISHED
~~~

## DIAG-CH-002

~~~text
PRECOMMIT_COMMIT: 119407929fe5e9d43fd9fc04ac21ec9a49147950
PRECOMMIT_BLOB: 655c5feab5626453027d89faca66842cd5506fc5
RESULT_COMMIT: edc89cc16df5290c78a7dd033ad67e34c59dc695
RESULT_BLOB: 024ed7f48b06ff20e7eca8e2dbc1136f878cc6d3
CHECKS: 80/80 PASS
ALL_SIX_DIAGNOSIS_PRIMARY_STATUSES_DIRECTLY_EXERCISED: yes
ALL_SEVEN_DIAGNOSIS_TASK_TERMINALS_DIRECTLY_EXERCISED: yes
~~~

## DIAG-CH-003

~~~text
PRECOMMIT_COMMIT: 8b21d04280c5c54e5897033acd8a42fbaffdd26c
PRECOMMIT_BLOB: 299f1d74a60f0da07746abde6fa677f8c6c5d3f9
RESULT_COMMIT: 67b1d448540387426c13fe0d58e8bdc8f1f83cdc
RESULT_BLOB: 1ba8520cbb376867094d413d5bed66258d8c258e
CHECKS: 90/90 PASS
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED: 10
EXACT_COLLAPSE_PAIRS: 0
UNRESOLVED_BOUNDARY_PAIRS: 0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS: 10
BOUNDARY_STATUS: FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
SOURCE_HANDOFF_SEPARATION: established_at_fixture_level
~~~

## DIAG-CH-004

~~~text
PRECOMMIT_COMMIT: cf85b4299cfdedb85fffdc3ef4c588681c71f268
PRECOMMIT_BLOB: af35f3074b96a1764c71f7c4bf9ed8e5e1a638bb
RESULT_COMMIT: 8978b543144742dc5d1a7e4bffb2a0a24692eeaf
RESULT_BLOB: 2f3e5f966e8fc6102a633dffee7df9af8c5635a8
CHECKS: 64/64 PASS
GAIN_AXES: 6/6 BASELINE_MATCH
DIAGNOSIS_METHOD_GAIN_STATUS: DIAGNOSIS_METHOD_GAIN_NO_GAIN
~~~

## DIAG-CH-005

~~~text
BASELINE_ID: B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE
PRECOMMIT_COMMIT: ce3c6d7e0bdab70453916875ef18b59720069114
PRECOMMIT_BLOB: 7becc81d1ac3b9822fa6331fd8cfc6953e106c27
RESULT_COMMIT: 6dbcd396baf61bf6c05b7ac051a49342c3c03634
RESULT_BLOB: 85c01c39ce6daef445442218b153896f42a8e8a6
CHECKS: 82/82 PASS
GAIN_AXES: 7/7 BASELINE_MATCH
DIAGNOSIS_METHOD_GAIN_STATUS: DIAGNOSIS_METHOD_GAIN_NO_GAIN
STRONGEST_REASONABLE_BASELINE_DIAGNOSIS: established_at_constructed_evidence_level
~~~

## DIAG-CH-006

~~~text
PRECOMMIT_COMMIT: 9e9ba8d6b7e832d1456778559f5431a2c650f556
PRECOMMIT_BLOB: 3d2337667e058442cf744a6af4a93bb2a6a17484
RECONSTRUCTION_LEDGER_COMMIT: dc8a2bef09d2ccef590bd2dca145e4a707f31ea5
RECONSTRUCTION_LEDGER_BLOB: 5c88893c4a5d643571c19df7033ff4e5498eb21c
RESULT_COMMIT: d0aaf3f7b13a9c44a2959e415cc2b8171931596f
CHECKS: 70/70 PASS
REPRODUCIBILITY_CASES: 1
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once
CLAIM_RELEVANT_MISMATCHES: 0
POST_COMPARISON_CORRECTIONS: 0
~~~ 

The retrace reconstructed DIAG-CH-001~005 from the frozen protocol and precommit artifacts, committed the reconstruction ledger before formal comparison, and found zero claim-relevant mismatch. It remains same-project, non-blind retraceability evidence rather than independent replication.


## DIAG-AUD-001 — frozen-axis internal standardization audit

~~~text
AUDIT_PRECOMMIT_COMMIT:
  7a61edc5eb3b5b40fb40e266dd484a67a0bba753

AUDIT_PRECOMMIT_BLOB:
  3cc2b55b0cc50850ffaf6fed58cf52b3b64608b8

PRE_SCORING_PROVENANCE_CORRECTION_COMMIT:
  9ef1b2216b4cd0a195710e34bd276fb493f2a1f1

PRE_SCORING_PROVENANCE_CORRECTION_BLOB:
  1697443467605dd3e2140c9838d79d1baac6f919

AUDIT_RESULT_COMMIT:
  8895b421dc8ef1075f5717a7ab69781c0aa59a22

AUDIT_RESULT_BLOB:
  982594b44047d5a97c1e69dd9fce3b42f329f9d7

AUDIT_CHECKS:
  28/28 PASS

FINAL_INTERNAL_STANDARDIZATION_DECISION:
  PROMOTE_INTERNAL_STANDARD

DIAGNOSIS_INTERNAL_STANDARDIZATION_STATUS:
  established

M7:
  CONDITIONAL_PASS

M13:
  PRESENT_NONFATAL

M14:
  DEFERRED_BY_SEQUENCE
~~~

The audit precommit contained one incorrect transcription of the DIAG-CH-006 result blob. The original precommit was not rewritten. A separate provenance-correction artifact was committed before scoring, and the audit retained this as `M13: PRESENT_NONFATAL`.

`PRESENT_NONFATAL` is not a hidden pass: the correction remains visible and was permitted by the prospectively frozen promotion rule.

The promotion is limited to project-internal protocol standardization. Diagnosis external application and independent validation remain separate.

## 8. Next

Diagnosis internal standardization is closed.

Family-wide internal build proceeds to **Reconstruction / DSD 복원론** source/registry recovery and planning. Diagnosis external validation remains deferred and separate.
