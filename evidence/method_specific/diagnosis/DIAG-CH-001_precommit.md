# DIAG-CH-001 — Positive Constructed Diagnosis Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-001`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `positive_constructed_diagnosis_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The protocol is immutable for this challenge.

No protocol rule may be edited in response to the result.

## 2. Challenge purpose

Test whether frozen Diagnosis Protocol v0.1 can execute one positive constructed challenge pack containing three prospectively frozen Diagnosis tasks that collectively exercise:

~~~text
coherent evidence sets

explicit deterministic bridges

multiple-compatible candidate result

unique-within-declared-class result

noninjective readout

required Property-status handoff

required support handoff

relation-valued transition constraint

typed scalar residual constraint

bounded cause-compatibility claim

candidate-class completeness limits

candidate-set outcome separated from task terminal

protocol conformance

maximum-supported-claim bounding
~~~

This challenge deliberately does not request:

~~~text
global unique diagnosis
unique past history
unrestricted causal proof
posterior ranking
optimal next measurement
external applicability
method gain
~~~

Challenge-level counters count this pack as one direct Diagnosis pilot.

## 3. Frozen challenge pack identity

~~~text
CHALLENGE_ID:
  DIAG-CH-001

CHALLENGE_VERSION:
  1

SUBTASKS:
  DIAG-CH-001-A
  DIAG-CH-001-B
  DIAG-CH-001-C

INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY

METHOD_GAIN_ASSESSMENT:
  not_requested

PROBABILISTIC_INTERFACE:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

Each subtask has one frozen primary claim level.

## 4. Subtask A — multiple compatible states under noninjective readout

### 4.1 Task lock

~~~text
DIAGNOSIS_TASK_ID:
  DIAG-CH-001-A

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

DIAGNOSIS_QUESTION:
  Which declared current hidden states remain compatible with
  readout zero, defined-zero status, support S1, and transition
  from predecessor p0?

CANDIDATE_CLASS_ID:
  H-A-v1

CANDIDATE_CLASS_VERSION_OR_DEFINITION:
  frozen below

CANDIDATE_CLASS_COMPLETENESS_STATUS:
  CANDIDATE_CLASS_DECLARED_BOUNDED

CANDIDATE_CLASS_COMPLETENESS_PROVENANCE:
  constructed fixture declaration

MAXIMUM_SUPPORTED_CLAIM:
  within H-A-v1 under the frozen evidence/bridge/transition semantics,
  a1 and a2 remain compatible while a3 is excluded;
  the result does not identify one unique current state
~~~

### 4.2 Candidate class

~~~text
a1:
  hidden_state = ALPHA
  main_readout = 0
  property_status = DEFINED_ZERO
  support = S1

a2:
  hidden_state = BETA
  main_readout = 0
  property_status = DEFINED_ZERO
  support = S1

a3:
  hidden_state = GAMMA
  main_readout = 0
  property_status = APPLICABLE_BUT_UNDEFINED
  support = S2
~~~

The main readout is intentionally noninjective:

~~~text
R(a1) = 0
R(a2) = 0
R(a3) = 0
~~~

Therefore main-readout equality alone cannot identify the hidden state.

### 4.3 Evidence set

~~~text
EVIDENCE_SET_ID:
  E-A-v1

EVIDENCE_SET_VERSION:
  1

EVIDENCE_SET_SCOPE:
  current-state Diagnosis on H-A-v1

EVIDENCE_SET_COHERENCE_STATUS_EXPECTED:
  EVIDENCE_SET_CONSISTENT
~~~

Evidence:

~~~text
eA1:
  type = main_readout
  observed = 0
  status = valid
  provenance = constructed_direct

eA2:
  type = Property-status handoff
  observed = DEFINED_ZERO
  status = valid
  provenance = constructed_typed_sidecar

eA3:
  type = support-retention handoff
  observed = S1
  status = valid
  provenance = constructed_typed_sidecar

eA4:
  type = transition constraint
  relation = p0 -> {a1,a2}
  status = valid
  provenance = constructed_relation
~~~

All four evidence records are jointly coherent under the frozen schema.

### 4.4 Bridge and required interfaces

~~~text
EVIDENCE_TO_CANDIDATE_BRIDGE_ID:
  BRIDGE-A-v1

BRIDGE_VERSION_OR_DEFINITION:
  candidate is compatible iff every frozen required evidence relation
  is compatible

BRIDGE_APPLICABILITY_SCOPE:
  H-A-v1 x E-A-v1

BRIDGE_RELATION_STATUS_EXPECTED:
  BRIDGE_RELATION_AVAILABLE

REQUIRED_DIAGNOSIS_INTERFACES:
  Property-status handoff
  support-retention handoff
  transition relation

REQUIRED_INTERFACE_STATUS_EXPECTED:
  AVAILABLE for all three
~~~

Frozen pair expectations:

~~~text
main readout eA1:
  a1 compatible
  a2 compatible
  a3 compatible

status eA2:
  a1 compatible
  a2 compatible
  a3 incompatible

support eA3:
  a1 compatible
  a2 compatible
  a3 incompatible

transition eA4:
  a1 compatible
  a2 compatible
  a3 incompatible
~~~

No pair is blocked, conflicting, out of scope, or underdetermined.

### 4.5 Expected candidate and set result

~~~text
a1:
  DIAGNOSIS_CANDIDATE_COMPATIBLE

a2:
  DIAGNOSIS_CANDIDATE_COMPATIBLE

a3:
  DIAGNOSIS_CANDIDATE_EXCLUDED

COMPATIBLE_CANDIDATE_SET:
  {a1,a2}

EXCLUDED_CANDIDATE_SET:
  {a3}

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Required preserved distinction:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
~~~

Cause claim:

~~~text
CAUSE_NOT_CLAIMED
~~~

## 5. Subtask B — unique within declared class under residual criterion

### 5.1 Task lock

~~~text
DIAGNOSIS_TASK_ID:
  DIAG-CH-001-B

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

DIAGNOSIS_QUESTION:
  Which declared current state is compatible with the frozen scalar
  residual target q*=10 under exact-zero residual?

CANDIDATE_CLASS_ID:
  H-B-v1

CANDIDATE_CLASS_COMPLETENESS_STATUS:
  CANDIDATE_CLASS_COMPLETENESS_NOT_CLAIMED

MAXIMUM_SUPPORTED_CLAIM:
  b2 is the unique compatible candidate within H-B-v1 under
  the frozen exact residual criterion; no global uniqueness is claimed
~~~

### 5.2 Candidate class and residual

~~~text
b1:
  q = 9

b2:
  q = 10

b3:
  q = 11

RESIDUAL_TARGET_ID:
  QSTAR-10-v1

RESIDUAL_CARRIER:
  real scalar

RESIDUAL_RULE:
  r(b) = abs(q(b)-10)

RESIDUAL_THRESHOLD_OR_EQUIVALENCE_RULE:
  compatible iff r(b)=0
~~~

Expected residuals:

~~~text
r(b1) = 1
r(b2) = 0
r(b3) = 1
~~~

### 5.3 Evidence and bridge

~~~text
EVIDENCE_SET_ID:
  E-B-v1

EVIDENCE_SET_COHERENCE_STATUS_EXPECTED:
  EVIDENCE_SET_CONSISTENT

EVIDENCE:
  target q*=10
  exact-zero residual required

BRIDGE_ID:
  BRIDGE-B-v1

BRIDGE_RELATION_STATUS_EXPECTED:
  BRIDGE_RELATION_AVAILABLE

INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
~~~

Expected pair/candidate result:

~~~text
b1:
  PAIR_INCOMPATIBLE
  DIAGNOSIS_CANDIDATE_EXCLUDED

b2:
  PAIR_COMPATIBLE
  DIAGNOSIS_CANDIDATE_COMPATIBLE

b3:
  PAIR_INCOMPATIBLE
  DIAGNOSIS_CANDIDATE_EXCLUDED
~~~

### 5.4 Expected set and task result

~~~text
COMPATIBLE_CANDIDATE_SET:
  {b2}

EXCLUDED_CANDIDATE_SET:
  {b1,b3}

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Required bounds:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_UNIQUE_DIAGNOSIS

RESIDUAL_ZERO
  !=
SOURCE_STATE_IDENTITY_BY_ITSELF
~~~

The unique result is established because the frozen candidate class plus frozen bridge/residual semantics leave one candidate, not because residual zero is treated as ontological identity.

## 6. Subtask C — bounded cause compatibility without causal proof

### 6.1 Task lock

~~~text
DIAGNOSIS_TASK_ID:
  DIAG-CH-001-C

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  CAUSE_COMPATIBILITY_ONLY

DIAGNOSIS_QUESTION:
  Which declared cause hypothesis remains compatible with
  the frozen marker evidence?

CANDIDATE_CLASS_ID:
  H-C-v1

CANDIDATE_CLASS_COMPLETENESS_STATUS:
  CANDIDATE_CLASS_DECLARED_BOUNDED

MAXIMUM_SUPPORTED_CLAIM:
  c1 is compatible and c2 is incompatible with the frozen marker
  evidence under BRIDGE-C-v1; no causal certainty or unrestricted
  cause identification is claimed
~~~

### 6.2 Cause candidates, evidence, and bridge

~~~text
c1:
  cause hypothesis CAUSE-A

c2:
  cause hypothesis CAUSE-B

EVIDENCE_SET_ID:
  E-C-v1

eC1:
  marker M = PRESENT

eC2:
  condition K = PRESENT

EVIDENCE_SET_COHERENCE_STATUS_EXPECTED:
  EVIDENCE_SET_CONSISTENT
~~~

Frozen compatibility bridge:

~~~text
BRIDGE-C-v1:

  c1 permits:
    M=PRESENT
    K=PRESENT

  c2 permits:
    M=ABSENT
    K=PRESENT
~~~

Expected:

~~~text
c1:
  compatible

c2:
  incompatible
~~~

No causal bridge establishing mechanism, intervention, or unrestricted real-world causality is supplied.

### 6.3 Expected cause/task result

~~~text
c1:
  DIAGNOSIS_CANDIDATE_COMPATIBLE

c2:
  DIAGNOSIS_CANDIDATE_EXCLUDED

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

CAUSE_CLAIM_STATUS:
  CAUSE_COMPATIBILITY_ONLY

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Required guard:

~~~text
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
~~~

## 7. Frozen optional-ledger expectations

Across the challenge pack:

~~~text
INFERENCE_MODE:
  INFERENCE_MODE_DETERMINISTIC_COMPATIBILITY

PROBABILISTIC_INTERFACE_LEDGER:
  NOT_REQUESTED

METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NOT_ASSESSED

ADDITIONAL_OBSERVATION_HANDOFF:
  A:
    unresolved distinction ALPHA vs BETA remains;
    possible measurement handoff may target a readout that separates a1/a2
  B:
    NOT_REQUESTED
  C:
    NOT_REQUESTED

OPTIMAL_MEASUREMENT_SELECTION:
  not performed

PAST_HISTORY_RECONSTRUCTION:
  not performed

GLOBAL_UNIQUENESS:
  not claimed

UNRESTRICTED_CAUSAL_CERTAINTY:
  not claimed
~~~

## 8. Frozen challenge-level expected result

~~~text
DIRECT_DIAGNOSIS_PILOT:
  positive

SUBTASK_A:
  DIAGNOSIS_TASK_ESTABLISHED
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

SUBTASK_B:
  DIAGNOSIS_TASK_ESTABLISHED
  DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

SUBTASK_C:
  DIAGNOSIS_TASK_ESTABLISHED
  CAUSE_COMPATIBILITY_ONLY

PROTOCOL_CONFORMANCE:
  conformant on all three subtasks

METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NOT_ASSESSED

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Frozen scoring — 80 checks

### A. Protocol / challenge immutability — 10

~~~text
A1 protocol commit/blob frozen
A2 G1-G18 identity frozen
A3 T1-T18 identity frozen
A4 challenge ID/version frozen
A5 all three subtask IDs frozen
A6 one primary claim per subtask frozen
A7 deterministic inference mode frozen
A8 method gain not requested
A9 no external application claim
A10 no post-hoc protocol/task repair
~~~

### B. Subtask A locks / evidence discipline — 12

~~~text
B1 H-A-v1 contains exactly a1,a2,a3
B2 all three main readouts equal zero
B3 a1 status DEFINED_ZERO
B4 a2 status DEFINED_ZERO
B5 a3 status APPLICABLE_BUT_UNDEFINED
B6 a1 support S1
B7 a2 support S1
B8 a3 support S2
B9 transition relation p0 -> {a1,a2}
B10 evidence set coherent
B11 required status/support/transition interfaces available
B12 bridge semantics frozen before execution
~~~

### C. Subtask A execution / multiplicity — 12

~~~text
C1 eA1 compatible with a1
C2 eA1 compatible with a2
C3 eA1 compatible with a3
C4 status sidecar compatible with a1
C5 status sidecar compatible with a2
C6 status sidecar incompatible with a3
C7 support sidecar compatible with a1
C8 support sidecar compatible with a2
C9 support sidecar incompatible with a3
C10 transition compatible with a1/a2 and incompatible with a3
C11 final compatible set exactly {a1,a2}
C12 MULTIPLE_COMPATIBLE not converted to task UNDERDETERMINED
~~~

### D. Subtask B residual / declared-class uniqueness — 12

~~~text
D1 H-B-v1 contains exactly b1,b2,b3
D2 q values frozen as 9,10,11
D3 scalar carrier frozen
D4 residual rule abs(q-10) frozen
D5 exact-zero threshold frozen
D6 r(b1)=1
D7 r(b2)=0
D8 r(b3)=1
D9 b1 excluded
D10 b2 compatible
D11 b3 excluded
D12 unique result remains declared-class bounded
~~~

### E. Subtask C cause-compatibility discipline — 12

~~~text
E1 H-C-v1 contains exactly c1,c2
E2 evidence M=PRESENT frozen
E3 evidence K=PRESENT frozen
E4 E-C-v1 coherent
E5 BRIDGE-C-v1 frozen
E6 c1 permits M=PRESENT
E7 c1 permits K=PRESENT
E8 c2 requires M=ABSENT
E9 c1 compatible
E10 c2 excluded
E11 cause status CAUSE_COMPATIBILITY_ONLY
E12 no causal-proof promotion
~~~

### F. Cross-cutting boundary / handoff discipline — 10

~~~text
F1 noninjective readout retained explicitly
F2 equal readout not promoted to hidden-state equality
F3 missing/undefined status not treated as zero
F4 support handoff not omitted
F5 transition compatibility not promoted to unique history
F6 residual zero not promoted to source identity
F7 no posterior/ranking inferred
F8 no optimal measurement selected
F9 additional-observation output remains handoff only
F10 no neighboring method substitutes for Diagnosis
~~~

### G. Final protocol results — 12

~~~text
G1 subtask A primary status DIAGNOSIS_ESTABLISHED
G2 subtask A terminal DIAGNOSIS_TASK_ESTABLISHED
G3 subtask A protocol conformant
G4 subtask B primary status DIAGNOSIS_ESTABLISHED
G5 subtask B terminal DIAGNOSIS_TASK_ESTABLISHED
G6 subtask B protocol conformant
G7 subtask C primary status DIAGNOSIS_ESTABLISHED
G8 subtask C terminal DIAGNOSIS_TASK_ESTABLISHED
G9 subtask C protocol conformant
G10 method gain NOT_ASSESSED
G11 protocol revision not required
G12 shared core reopen not required
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
~~~
