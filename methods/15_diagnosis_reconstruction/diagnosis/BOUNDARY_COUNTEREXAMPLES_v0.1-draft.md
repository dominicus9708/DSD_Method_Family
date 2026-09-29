# DSD Diagnosis Boundary Counterexamples v0.1 — Pre-Protocol Attack Record

Status: **EXECUTED — PRE-PROTOCOL BOUNDARY ATTACK COMPLETE**  
Date: **2026-09-29**  
Method: **Diagnosis / DSD 진단론**

Purpose: pressure the historical Diagnosis Task Interface before any executable Diagnosis Protocol is frozen.

These are constructed internal counterexamples.

They are not external validation.

Task Interface under attack:

~~~text
TASK_INTERFACE_COMMIT:
  e2c636eb0751878423a35d6848f7ef5a8fe81cc3

TASK_INTERFACE_BLOB:
  8cc12899c9b3f7a5f78d0e1893c5aa3a3824d444
~~~

Source-registry basis:

~~~text
SOURCE_REGISTRY_COMMIT:
  63ccc25d5bc8ddadadabfe698852d846e5671f15

SOURCE_REGISTRY_BLOB:
  1152759be5b56462156c83ecd3c508c73f1755f7
~~~

## 1. Results summary

~~~text
BOUNDARY_ATTACKS_RUN:
  18

PRESERVED_NO_REFINEMENT:
  13

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  5

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_REQUIRED:
  yes

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The five refinements concern execution semantics and status discipline.

They do not change the Diagnosis method identity.

## 2. D1 — multiple compatible candidates under fully frozen semantics

Frozen declared candidate class:

~~~text
H = {h1,h2,h3}
~~~

Frozen evidence/bridge evaluation:

~~~text
h1:
  compatible with every required evidence item

h2:
  compatible with every required evidence item

h3:
  excluded by one valid incompatible evidence item
~~~

Primary claim level:

~~~text
CANDIDATE_COMPATIBILITY_SET
~~~

Required:

~~~text
compatible set:
  {h1,h2}

excluded set:
  {h3}

DIAGNOSIS_SET_MULTIPLE_COMPATIBLE

overall Diagnosis:
  may be ESTABLISHED
~~~

Attack:

~~~text
treat multiple compatible candidates as task underdetermination
or protocol failure
~~~

Rejected.

Required guard:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 3. D2 — one surviving declared candidate with incomplete candidate class

Frozen:

~~~text
declared candidates:
  {h1,h2,h3}

candidate-class completeness:
  CANDIDATE_CLASS_COMPLETENESS_NOT_CLAIMED

evidence:
  excludes h1 and h2
  retains h3
~~~

Required:

~~~text
DIAGNOSIS_SET_UNIQUE_WITHIN_DECLARED_CLASS

not:
  GLOBAL_UNIQUE_DIAGNOSIS
~~~

The draft already states that candidate-class completeness is not manufactured by Diagnosis.

Guard:

~~~text
SINGLE_REMAINING_DECLARED_CANDIDATE
  !=
GLOBAL_UNIQUE_DIAGNOSIS
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 4. D3 — zero compatible candidates in a declared class

Frozen:

~~~text
H = {h1,h2}

every required bridge/evidence relation:
  evaluable

h1:
  excluded

h2:
  excluded

evidence packet:
  internally coherent
~~~

Required:

~~~text
DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS
~~~

Not allowed:

~~~text
NO_REAL_STATE_EXISTS
THE_WORLD_IS_IMPOSSIBLE
~~~

Guard:

~~~text
NO_ADMISSIBLE_DECLARED_CANDIDATE
  !=
NO_REAL_STATE_EXISTS
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 5. D4 — mutually inconsistent evidence packet

Frozen evidence items:

~~~text
e1:
  same sensor / same time / same regime
  status = valid
  value = 0

e2:
  same sensor / same time / same regime
  status = valid
  value = 1

schema:
  exact single-valued readout
  no tolerance / multiplexing rule
  no precedence rule
~~~

Every candidate can be made to fail at least one item.

Attack:

~~~text
return NONE_COMPATIBLE_IN_DECLARED_CLASS
and silently treat the packet as coherent
~~~

This is insufficient.

The draft preserves evidence status/provenance but lacks an explicit frozen evidence-set coherence/conflict status and exact task consequence.

Required prospective record:

~~~text
EVIDENCE_SET_COHERENCE_STATUS:
  CONSISTENT
  CONFLICTING
  UNDERDETERMINED
  BLOCKED
  OUT_OF_SCOPE
~~~

For this fixture:

~~~text
EVIDENCE_SET_COHERENCE_STATUS:
  CONFLICTING

task-level consequence:
  DIAGNOSIS_CONFLICTING
  unless a frozen resolver/precedence rule applies
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R1 evidence-set coherence / conflict semantics
~~~

## 6. D5 — required evidence unavailable

Frozen task:

~~~text
candidate h requires evidence e_required
for the primary claim

e_required:
  required

availability:
  unavailable

no replacement evidence:
  authorized
~~~

Attack:

~~~text
treat missing e_required as negative evidence
and exclude h
~~~

Rejected.

Required:

~~~text
candidate disposition:
  DIAGNOSIS_CANDIDATE_BLOCKED

not:
  DIAGNOSIS_CANDIDATE_EXCLUDED
~~~

Guard:

~~~text
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 7. D6 — multiple admissible bridge semantics

Frozen:

~~~text
candidate:
  h

evidence:
  e

bridge interpretation A:
  PAIR_COMPATIBLE

bridge interpretation B:
  PAIR_INCOMPATIBLE

both interpretations:
  admissible under supplied records

resolver:
  none
~~~

Required:

~~~text
PAIR_UNDERDETERMINED

candidate/task:
  underdetermined if the distinction changes the requested claim
~~~

Attack:

~~~text
choose the favorable bridge after observing the result
~~~

Rejected.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 8. D7 — mutually incompatible same-version bridge rules

Frozen bridge registry:

~~~text
BRIDGE-v7 rule A:
  h + e -> PAIR_COMPATIBLE

BRIDGE-v7 rule B:
  h + e -> PAIR_INCOMPATIBLE

same applicability scope:
  yes

precedence/resolver:
  none
~~~

This is not merely two admissible semantic interpretations.

It is a claim-relevant rule conflict.

The draft explicitly left open whether a pair-level conflict status was needed.

Required refinement:

~~~text
BRIDGE_RELATION_STATUS:
  AVAILABLE
  UNAVAILABLE
  CONFLICTING
  UNDERDETERMINED
  OUT_OF_SCOPE

PAIR_CONFLICTING:
  available when mutually incompatible applicable bridge rules
  target the same candidate/evidence relation
~~~

Task consequence:

~~~text
claim-relevant unresolved bridge conflict
  -> DIAGNOSIS_CONFLICTING
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R2 bridge-rule conflict / pair-conflict semantics
~~~

## 9. D8 — noninjective forward map with equal readout

Frozen current-state candidates:

~~~text
h1 != h2
~~~

Forward readout:

~~~text
R(h1) = y
R(h2) = y
~~~

Observed:

~~~text
y
~~~

No sidecar or additional evidence distinguishes h1 from h2.

Required:

~~~text
h1:
  compatible

h2:
  compatible

DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
~~~

Forbidden:

~~~text
select h1
select h2
infer state equality
~~~

Guards:

~~~text
EQUAL_READOUT != EQUAL_HIDDEN_STATE
NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 10. D9 — injective on declared candidate class but not globally

Frozen forward map has collisions outside declared class H.

Within H:

~~~text
R|_H:
  injective
~~~

Observation selects exactly one h in H.

Candidate-class completeness:

~~~text
not claimed
~~~

Required:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS:
  established

GLOBAL_UNIQUE_DIAGNOSIS:
  not established
~~~

Guard:

~~~text
INJECTIVITY_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 11. D10 — required support/status sidecar unavailable

Frozen:

~~~text
main readout:
  y

candidate h1 and h2:
  collide at y

claim-relevant distinction:
  defined zero
  versus
  absent/undefined support

required support/status sidecar:
  declared required

availability:
  unavailable
~~~

The draft lists support/status handoffs but does not yet freeze the exact task consequence of a required sidecar being unavailable.

Required:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_STATUS:
  AVAILABLE
  UNAVAILABLE
  CONFLICTING
  UNDERDETERMINED
  OUT_OF_SCOPE
~~~

For this fixture:

~~~text
required interface:
  UNAVAILABLE

candidate distinction:
  cannot be evaluated

task/candidate result:
  BLOCKED

not:
  EXCLUDED
  NOT_ESTABLISHED from destructive evidence
  silent zero-padding
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R3 required-interface availability / BLOCKED semantics
~~~

## 12. D11 — zero residual for distinct states

Frozen target/reference:

~~~text
target observable:
  q = 0
~~~

Two distinct current states:

~~~text
h1 != h2
~~~

Both satisfy:

~~~text
R_q(h1) = 0
R_q(h2) = 0
~~~

Required:

~~~text
both candidates may remain compatible
~~~

Forbidden:

~~~text
RESIDUAL_ZERO -> SOURCE_STATE_IDENTITY
RESIDUAL_ZERO -> UNIQUE_DIAGNOSIS
~~~

The draft already requires residual target/carrier/rule and preserves residual-match limits.

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 13. D12 — branching transition relation

Frozen predecessor condition and transition relation admit:

~~~text
s0 -> h1
s0 -> h2
~~~

Present evidence is compatible with both h1 and h2.

No unique-successor rule is supplied.

Required:

~~~text
h1:
  compatible

h2:
  compatible

DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
~~~

Forbidden:

~~~text
transition relation
  -> unique current state
~~~

Guard:

~~~text
TRANSITION_COMPATIBILITY != UNIQUE_SUCCESSOR
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 14. D13 — unique current state but multiple compatible histories

Present evidence plus frozen transition constraints identify:

~~~text
current candidate:
  h_now
~~~

Two predecessor histories remain compatible:

~~~text
history A -> h_now
history B -> h_now
~~~

Primary task:

~~~text
CURRENT_STATE_OR_CONDITION_IDENTIFICATION
~~~

Required:

~~~text
current Diagnosis:
  may be established

unique past history:
  not established
~~~

Guard:

~~~text
CURRENT_STATE_DIAGNOSIS
  !=
PAST_HISTORY_RECONSTRUCTION
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 15. D14 — cause hypothesis compatible without causal bridge

Frozen cause hypotheses:

~~~text
c1
c2
~~~

Present observations are compatible with c1 and exclude c2.

No causal bridge is supplied.

Primary claim:

~~~text
CAUSE_COMPATIBILITY_ONLY
~~~

Required:

~~~text
c1:
  compatible

c2:
  excluded

cause identification:
  not claimed
~~~

Forbidden:

~~~text
c1 compatible
  -> c1 proven cause
~~~

Guard:

~~~text
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 16. D15 — posterior ranking requested without probabilistic interface

Request:

~~~text
"Which compatible candidate is most probable?"
~~~

Frozen task provides:

~~~text
candidate set
deterministic evidence-to-candidate compatibility rules

priors:
  absent

likelihood model:
  absent

posterior semantics:
  absent

decision loss:
  absent
~~~

The draft states:

~~~text
PROBABILITY != COMPATIBILITY
CANDIDATE_RANKING != CANDIDATE_ELIMINATION
~~~

but does not yet lock the exact scope consequence.

Required refinement for Diagnosis Protocol v0.1:

~~~text
INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY
  PROBABILISTIC_IF_EXPLICITLY_SUPPLIED

default v0.1 mode:
  DETERMINISTIC_COMPATIBILITY

posterior/ranking request without an explicit probabilistic interface:
  DIAGNOSIS_TASK_OUT_OF_SCOPE
  for the ranking claim

compatible-set Diagnosis:
  may remain independently established
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R4 deterministic/probabilistic inference-mode scope
~~~

## 17. D16 — unresolved candidates and request for the "best next measurement"

Frozen Diagnosis result:

~~~text
compatible candidates:
  {h1,h2}

unresolved distinction:
  feature f
~~~

Diagnosis can emit:

~~~text
required distinction:
  f

possible measurement handoff:
  observe a readout sensitive to f
~~~

Attack:

~~~text
Diagnosis must itself select the globally best measurement
under cost/risk/information objective
~~~

Rejected unless a separate Measurement/Optimization task is supplied.

Guards:

~~~text
NEED_FOR_ADDITIONAL_OBSERVATION
  !=
OPTIMAL_MEASUREMENT_SELECTED

DIAGNOSIS_DISCRIMINATOR_REQUIREMENT
  !=
MEASUREMENT_PLAN_EXECUTION
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 18. D17 — neighboring-method substitution pressure

A Measurement task reports:

~~~text
the planned readouts can distinguish h1 from h2
~~~

A Classification task assigns the observed artifact to class K.

A Reconstruction task supplies one plausible prior history.

An Audit task passes the evidence-recording procedure.

But no Diagnosis bridge has yet been executed for current-state candidates h1/h2.

Attack:

~~~text
Measurement sufficiency
or Classification output
or Reconstruction candidate
or Audit pass

substitutes for
the Diagnosis compatibility result
~~~

Rejected.

Required:

~~~text
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
CLASSIFICATION_RESULT != DIAGNOSIS_RESULT
RECONSTRUCTION_CANDIDATE != CURRENT_DIAGNOSIS
AUDIT_PASS != DIAGNOSIS_RESULT
~~~

Verdict:

~~~text
PRESERVED_NO_REFINEMENT
~~~

## 19. D18 — multi-obligation mixed result and terminal precedence

Frozen task contains independent required obligations:

~~~text
Q1:
  current-state compatibility set
  established

Q2:
  cause-identification claim
  causal bridge unavailable
  blocked

Q3:
  posterior-ranking request
  no probabilistic interface
  out of scope

Q4:
  same-version bridge rules conflict
  conflicting
~~~

The current Task Interface gives a draft terminal precedence but explicitly leaves it unfrozen.

Required refinement:

~~~text
task-terminal precedence:
  OUT_OF_SCOPE
  >
  CONFLICTING
  >
  UNDERDETERMINED
  >
  BLOCKED
  >
  ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

Also freeze:

~~~text
PARTIAL:
  only for multiple independently required in-scope obligations
  when no higher terminal applies

PARTIAL
  !=
rescue label for one failed atomic proposition
~~~

For this fixture:

~~~text
task terminal:
  DIAGNOSIS_TASK_OUT_OF_SCOPE

subordinate:
  conflict retained
  blocked retained
  established Q1 retained
~~~

Verdict:

~~~text
PRESERVED_WITH_NONBREAKING_REFINEMENT
~~~

Refinement group:

~~~text
R5 task-terminal precedence / PARTIAL semantics
~~~

## 20. Refinement groups

The boundary attack preserves the core Diagnosis identity but requires five prospective execution refinements.

~~~text
R1
  evidence-set coherence / conflict semantics

R2
  bridge-rule conflict / pair-conflict semantics

R3
  required-interface availability / BLOCKED semantics

R4
  deterministic versus explicitly supplied probabilistic
  inference-mode scope

R5
  task-terminal precedence / PARTIAL semantics
~~~

## 21. Forced prospective amendment

Diagnosis Boundary Amendment 001 must add or freeze at least:

~~~text
A. EVIDENCE_SET_COHERENCE_STATUS
   with explicit conflict / underdetermined / blocked consequences

B. BRIDGE_RELATION_STATUS
   and an explicit pair-level conflict state

C. REQUIRED_DIAGNOSIS_INTERFACE_STATUS
   with:
     unavailable required interface -> BLOCKED
     not candidate exclusion
     not evaluable NOT_ESTABLISHED

D. INFERENCE_MODE
   with deterministic compatibility as the default v0.1 scope
   and probabilistic/posterior ranking only when an explicit
   probabilistic interface is supplied

E. exact task-terminal precedence and PARTIAL semantics
~~~

The Amendment may refine execution status semantics.

It must not rewrite the historical Task Interface v0.1 draft.

## 22. Boundary result

No attack requires collapsing Diagnosis into:

~~~text
Measurement
Reconstruction
Prediction
Simulation
Classification
Comparison
Optimization
Audit
~~~

No attack requires changing the recovered source-derived core:

~~~text
typed status distinctions remain visible

equal aggregate/projection/readout
  does not imply equal hidden state

noninjective forward structure
  preserves multiple admissible candidates

residual evidence is target/carrier relative

relation-valued transitions may branch

Measurement discrimination does not itself execute Diagnosis

Diagnosis current-state inference
  does not automatically reconstruct unique history

cause compatibility
  does not itself establish causal proof
~~~

The historical Task Interface remains unchanged.

## 23. Current state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 historical draft preserved

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

BOUNDARY_AMENDMENT_001:
  not yet established

REFINEMENT_GROUPS_REQUIRED:
  5

DEDICATED_DIAGNOSIS_PROTOCOL:
  not established

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  0

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
  pre_protocol_boundary_attack_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable pre-protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 24. Next

Establish Diagnosis Task Interface Boundary Amendment 001 prospectively.

Protocol freeze is not authorized before that Amendment is established.
