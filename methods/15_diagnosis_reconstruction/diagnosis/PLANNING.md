# DSD Diagnosis — Planning / Validation Roadmap

Status: **DIAG-CH-001 positive constructed 80/80 PASS / negative-terminal challenge next**  
Date: **2026-09-29**

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
6. ⏸ Executable Diagnosis Protocol v0.1.
7. ⏸ Positive constructed challenge.
8. ⏸ Negative / blocked / unresolved terminal coverage.
9. ⏸ Direct neighboring-method boundary challenge.
10. ⏸ Competent non-DSD baseline.
11. ⏸ Strongest-reasonable non-DSD baseline.
12. ⏸ Deterministic same-project retrace.
13. ⏸ Frozen-axis internal standardization audit.
14. ⏸ External applications / independent validation — separate later phase.

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
  1

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  1

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

## 8. Next

Prospectively precommit and execute DIAG-CH-002 negative / blocked / conflicting / underdetermined / out-of-scope / partial terminal coverage.
