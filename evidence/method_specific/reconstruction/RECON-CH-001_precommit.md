# RECON-CH-001 — Positive Constructed Reconstruction Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-001`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Case class: `positive_constructed_reconstruction_challenge`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

~~~text
PROTOCOL_COMMIT:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad

PROTOCOL_BLOB:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The protocol is immutable for this challenge.

No protocol rule may be edited in response to the result.

## 2. Challenge purpose

Test whether frozen Reconstruction Protocol v0.1 can execute one positive constructed challenge pack containing three prospectively frozen Reconstruction tasks that collectively exercise:

~~~text
noninjective compressed-source reconstruction

multiple-compatible source result

declared-class unique prior-state reconstruction

relation-valued temporal bridge

typed marker sidecar

frozen-interface closure

explicit unrecoverability on a complete declared interface

candidate-set outcome separated from task terminal

class-bounded uniqueness

interface-bounded unrecoverability

protocol conformance

maximum-supported-claim bounding
~~~

This challenge deliberately does not request:

~~~text
global historical truth

global injectivity

absolute unrecoverability under all future evidence

probabilistic ranking

optimal next measurement

established Tracking link

established Lineage identity

external applicability

method gain
~~~

Challenge-level counters count this pack as one direct Reconstruction pilot.

## 3. Frozen challenge pack identity

~~~text
CHALLENGE_ID:
  RECON-CH-001

CHALLENGE_VERSION:
  1

SUBTASKS:
  RECON-CH-001-A
  RECON-CH-001-B
  RECON-CH-001-C

INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY

METHOD_GAIN_ASSESSMENT:
  not_requested

PROBABILISTIC_INTERFACE:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

Each subtask has exactly one frozen primary claim level.

## 4. Subtask A — noninjective compressed-source compatibility set

### 4.1 Task lock

~~~text
RECONSTRUCTION_TASK_ID:
  RECON-CH-001-A

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  RECONSTRUCTION_COMPATIBILITY_SET

RECONSTRUCTION_TARGET_KIND:
  COMPRESSED_SOURCE

RECONSTRUCTION_QUESTION:
  Which declared source vectors remain compatible with
  compressed readout y=3 under F(x1,x2)=x1+x2?

MAXIMUM_SUPPORTED_CLAIM:
  within H-A-v1 under F-A-v1 and E-A-v1,
  a1 and a2 remain compatible while a3 is excluded;
  no unique source is identified
~~~

### 4.2 Reconstruction class

~~~text
RECONSTRUCTION_CLASS_ID:
  H-A-v1

RECONSTRUCTION_CLASS_REPRESENTATION_MODE:
  EXPLICIT_ENUMERATION

CANDIDATE_EVALUATION_MODE:
  ELEMENTWISE

RECONSTRUCTION_CLASS_COMPLETENESS_STATUS:
  RECONSTRUCTION_CLASS_DECLARED_BOUNDED

a1:
  source = (1,2)

a2:
  source = (2,1)

a3:
  source = (0,0)
~~~

Frozen forward map:

~~~text
F-A-v1(x1,x2) = x1 + x2
~~~

Expected forward values:

~~~text
F(a1) = 3
F(a2) = 3
F(a3) = 0
~~~

### 4.3 Evidence and interface

~~~text
EVIDENCE_SET_ID:
  E-A-v1

EVIDENCE_SET_COHERENCE_STATUS_EXPECTED:
  EVIDENCE_SET_CONSISTENT

eA1:
  compressed_readout = 3
  provenance = constructed_direct
  status = valid

FORWARD_OR_OBSERVATION_BRIDGE_ID:
  F-A-v1

BRIDGE_RELATION_STATUS_EXPECTED:
  BRIDGE_RELATION_AVAILABLE

RECONSTRUCTION_INTERFACE_CLOSURE_STATUS:
  INTERFACE_EXPLICITLY_PARTIAL

REQUIRED_RECONSTRUCTION_INTERFACES:
  forward map F-A-v1
~~~

No support-retention or relation sidecar is supplied or required by the primary compatibility-set claim.

The interface is explicitly partial so this subtask does not make an unrecoverability claim.

### 4.4 Expected result

~~~text
a1:
  RECONSTRUCTION_CANDIDATE_COMPATIBLE

a2:
  RECONSTRUCTION_CANDIDATE_COMPATIBLE

a3:
  RECONSTRUCTION_CANDIDATE_EXCLUDED

COMPATIBLE_RECONSTRUCTION_SET:
  {a1,a2}

EXCLUDED_RECONSTRUCTION_SET:
  {a3}

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

RECONSTRUCTION_TASK_TERMINAL:
  RECONSTRUCTION_TASK_ESTABLISHED

RECONSTRUCTION_PROTOCOL_CONFORMANCE:
  RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

Required preserved distinctions:

~~~text
EQUAL_OUTPUT != EQUAL_SOURCE
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

## 5. Subtask B — unique prior state within declared class

### 5.1 Task lock

~~~text
RECONSTRUCTION_TASK_ID:
  RECON-CH-001-B

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  UNIQUE_WITHIN_DECLARED_RECONSTRUCTION_CLASS

RECONSTRUCTION_TARGET_KIND:
  PRIOR_STATE

RECONSTRUCTION_QUESTION:
  Which declared prior state is compatible with the frozen
  present-state marker and transition relation?

MAXIMUM_SUPPORTED_CLAIM:
  b2 is the unique compatible prior-state candidate within H-B-v1
  under the frozen marker and transition semantics;
  global historical uniqueness is not claimed
~~~

### 5.2 Candidate class

~~~text
RECONSTRUCTION_CLASS_ID:
  H-B-v1

RECONSTRUCTION_CLASS_REPRESENTATION_MODE:
  EXPLICIT_ENUMERATION

CANDIDATE_EVALUATION_MODE:
  ELEMENTWISE

RECONSTRUCTION_CLASS_COMPLETENESS_STATUS:
  RECONSTRUCTION_CLASS_COMPLETENESS_NOT_CLAIMED

b1:
  prior_state = P1
  marker = RED

b2:
  prior_state = P2
  marker = BLUE

b3:
  prior_state = P3
  marker = BLUE
~~~

Frozen current state:

~~~text
current_state:
  C
~~~

Frozen transition relation:

~~~text
T-B-v1:
  P1 !-> C
  P2 -> C
  P3 !-> C
~~~

Frozen marker evidence:

~~~text
observed_prior_marker_handoff:
  BLUE
~~~

### 5.3 Evidence / history relation

~~~text
EVIDENCE_SET_ID:
  E-B-v1

EVIDENCE_SET_COHERENCE_STATUS_EXPECTED:
  EVIDENCE_SET_CONSISTENT

HISTORY_RELATION_FAMILY_ID:
  T-B-v1

HISTORY_RELATION_COHERENCE_STATUS_EXPECTED:
  HISTORY_RELATION_CONSISTENT

BRANCHING_ALLOWED:
  yes

MERGING_ALLOWED:
  yes

UNIQUE_PREDECESSOR_REQUIREMENT:
  no independent axiom

UNIQUE_PATH_REQUIREMENT:
  no independent axiom
~~~

The result is derived from the frozen declared candidate class plus marker and transition compatibility.

No established Lineage identity is supplied.

### 5.4 Expected result

~~~text
b1:
  marker incompatible
  transition incompatible
  ->
  RECONSTRUCTION_CANDIDATE_EXCLUDED

b2:
  marker compatible
  transition compatible
  ->
  RECONSTRUCTION_CANDIDATE_COMPATIBLE

b3:
  marker compatible
  transition incompatible
  ->
  RECONSTRUCTION_CANDIDATE_EXCLUDED

COMPATIBLE_RECONSTRUCTION_SET:
  {b2}

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

RECONSTRUCTION_TASK_TERMINAL:
  RECONSTRUCTION_TASK_ESTABLISHED

RECONSTRUCTION_PROTOCOL_CONFORMANCE:
  RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

Required bounds:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS
  !=
GLOBAL_HISTORICAL_TRUTH

TRANSITION_COMPATIBILITY
  !=
ESTABLISHED_LINEAGE

CURRENT_STATE_DIAGNOSIS
  !=
PAST_STATE_RECONSTRUCTION
~~~

## 6. Subtask C — unrecoverable distinction on complete frozen interface

### 6.1 Task lock

~~~text
RECONSTRUCTION_TASK_ID:
  RECON-CH-001-C

TASK_VERSION:
  1

PRIMARY_CLAIM_LEVEL:
  UNRECOVERABLE_INFORMATION_ON_FROZEN_INTERFACE

RECONSTRUCTION_TARGET_KIND:
  COMPRESSED_SOURCE

RECONSTRUCTION_QUESTION:
  Can the ordered source identity of u1 versus u2
  be recovered from the complete frozen claim-relevant interface?

MAXIMUM_SUPPORTED_CLAIM:
  the distinction u1 versus u2 is unrecoverable on the
  frozen declared interface I-C-v1;
  no claim is made about future evidence outside I-C-v1
~~~

### 6.2 Candidate class and frozen interface

~~~text
RECONSTRUCTION_CLASS_ID:
  H-C-v1

RECONSTRUCTION_CLASS_REPRESENTATION_MODE:
  EXPLICIT_ENUMERATION

CANDIDATE_EVALUATION_MODE:
  ELEMENTWISE

RECONSTRUCTION_CLASS_COMPLETENESS_STATUS:
  RECONSTRUCTION_CLASS_DECLARED_BOUNDED

u1:
  source = (1,0)

u2:
  source = (0,1)

F-C-v1(x1,x2):
  x1 + x2
~~~

Frozen evidence:

~~~text
E-C-v1:
  readout = 1
~~~

Execution expectation:

~~~text
F(u1) = 1
F(u2) = 1
~~~

Frozen interface closure:

~~~text
RECONSTRUCTION_INTERFACE_CLOSURE_STATUS:
  INTERFACE_COMPLETE_FOR_DECLARED_CLAIM

FROZEN_INTERFACE_COMPONENT_REGISTER:
  F-C-v1
  E-C-v1

FROZEN_INTERFACE_SCOPE:
  distinguish ordered source identity u1 versus u2

FROZEN_INTERFACE_COMPLETENESS_PROVENANCE:
  constructed fixture declaration
~~~

There is no support, order, provenance, or relational sidecar in I-C-v1.

The interface is prospectively declared complete for this exact bounded distinction.

### 6.3 Expected result

~~~text
u1:
  RECONSTRUCTION_CANDIDATE_COMPATIBLE

u2:
  RECONSTRUCTION_CANDIDATE_COMPATIBLE

RECONSTRUCTION_SET_OUTCOME:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

RECOVERY_AND_UNRECOVERABILITY_STATUS:
  UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE

RECONSTRUCTION_PRIMARY_STATUS:
  RECONSTRUCTION_ESTABLISHED

RECONSTRUCTION_TASK_TERMINAL:
  RECONSTRUCTION_TASK_ESTABLISHED

RECONSTRUCTION_PROTOCOL_CONFORMANCE:
  RECONSTRUCTION_PROTOCOL_CONFORMANT
~~~

Required preserved distinctions:

~~~text
NO_REGISTERED_DISTINGUISHER
  !=
PROVED_UNRECOVERABILITY

but here:

complete-for-claim frozen interface
+
two distinct in-scope compatible sources
+
identical complete frozen evidence
+
no frozen distinguisher
->
interface-bounded unrecoverability established
~~~

Also preserve:

~~~text
UNRECOVERABLE_ON_FROZEN_INTERFACE
  !=
ABSOLUTELY_UNRECOVERABLE_BY_ANY_FUTURE_EVIDENCE
~~~

## 7. Frozen optional-ledger expectations

Across the challenge pack:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY

PROBABILISTIC_INTERFACE:
  NOT_REQUESTED

DEFINITIONAL_RECOMPLETION_ROLE:
  DEFINITIONAL_RECOMPLETION_NOT_USED

TRACKING_HANDOFF:
  NOT_REQUESTED

LINEAGE_HANDOFF:
  NOT_REQUESTED

METHOD_GAIN_STATUS:
  RECONSTRUCTION_GAIN_NOT_YET_TESTED

OPTIMAL_MEASUREMENT_SELECTION:
  not performed

GLOBAL_HISTORICAL_TRUTH:
  not claimed

ABSOLUTE_UNRECOVERABILITY:
  not claimed
~~~

## 8. Frozen challenge-level expected result

~~~text
DIRECT_RECONSTRUCTION_PILOT:
  positive

SUBTASK_A:
  RECONSTRUCTION_TASK_ESTABLISHED
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

SUBTASK_B:
  RECONSTRUCTION_TASK_ESTABLISHED
  RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS

SUBTASK_C:
  RECONSTRUCTION_TASK_ESTABLISHED
  UNRECOVERABLE_DISTINCTION_ESTABLISHED_ON_FROZEN_INTERFACE

PROTOCOL_CONFORMANCE:
  conformant on all three subtasks

METHOD_GAIN_STATUS:
  RECONSTRUCTION_GAIN_NOT_YET_TESTED

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
A6 exactly one primary claim per subtask
A7 deterministic inference mode frozen
A8 method gain not requested
A9 no external application claim
A10 no post-hoc protocol/task repair
~~~

### B. Subtask A locks / noninjective source discipline — 12

~~~text
B1 H-A-v1 contains exactly a1,a2,a3
B2 class representation mode explicit enumeration
B3 evaluation mode elementwise
B4 F-A-v1 frozen as x1+x2
B5 F(a1)=3
B6 F(a2)=3
B7 F(a3)=0
B8 evidence readout 3 frozen
B9 evidence set coherent
B10 bridge available
B11 interface explicitly partial
B12 no unrecoverability claim requested
~~~

### C. Subtask A execution / multiplicity — 10

~~~text
C1 a1 compatible
C2 a2 compatible
C3 a3 excluded
C4 compatible set exactly {a1,a2}
C5 excluded set exactly {a3}
C6 set outcome MULTIPLE_COMPATIBLE
C7 primary status ESTABLISHED
C8 terminal ESTABLISHED
C9 equal output not promoted to equal source
C10 no arbitrary preimage selected
~~~

### D. Subtask B prior-state / history discipline — 14

~~~text
D1 H-B-v1 contains exactly b1,b2,b3
D2 class completeness NOT_CLAIMED
D3 marker values frozen RED,BLUE,BLUE
D4 current state C frozen
D5 T-B-v1 frozen
D6 P1 !-> C
D7 P2 -> C
D8 P3 !-> C
D9 observed marker BLUE frozen
D10 b1 excluded
D11 b2 compatible
D12 b3 excluded
D13 set outcome UNIQUE_WITHIN_DECLARED_CLASS
D14 uniqueness remains declared-class bounded
~~~

### E. Subtask C frozen-interface unrecoverability — 14

~~~text
E1 H-C-v1 contains exactly u1,u2
E2 F-C-v1 frozen as x1+x2
E3 evidence readout 1 frozen
E4 F(u1)=1
E5 F(u2)=1
E6 both candidates compatible
E7 interface closure COMPLETE_FOR_DECLARED_CLAIM
E8 interface component register exactly F-C-v1 and E-C-v1
E9 requested distinction is u1 versus u2 ordered source identity
E10 no frozen distinguisher exists
E11 set outcome MULTIPLE_COMPATIBLE
E12 unrecoverability established on frozen interface
E13 absolute future unrecoverability not claimed
E14 no external sidecar invented
~~~

### F. Cross-cutting method-boundary discipline — 10

~~~text
F1 no probabilistic objects invented
F2 no candidate ranking performed
F3 no optimal measurement selected
F4 no Tracking link promoted
F5 no Lineage identity promoted
F6 no current-state Diagnosis substituted
F7 no definitional recompletion counted as Reconstruction evidence
F8 no global historical truth claimed
F9 candidate-set outcome remains separate from task terminal
F10 maximum-supported claim remains bounded on all subtasks
~~~

### G. Final protocol results — 10

~~~text
G1 subtask A protocol conformant
G2 subtask B protocol conformant
G3 subtask C protocol conformant
G4 subtask A terminal ESTABLISHED
G5 subtask B terminal ESTABLISHED
G6 subtask C terminal ESTABLISHED
G7 direct Reconstruction pilot counted as positive
G8 method gain remains NOT_YET_TESTED
G9 protocol revision not required
G10 shared core reopen not required
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
~~~
