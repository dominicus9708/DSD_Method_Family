# DIAG-CH-002 — Negative / Unresolved-Terminal Diagnosis Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-002`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`  
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

No protocol rule may be changed in response to the result.

## 2. Purpose

Directly exercise the negative, blocked, conflicting, underdetermined, out-of-scope, and partial Diagnosis outcomes that DIAG-CH-001 intentionally did not claim.

A conformant negative or unresolved result counts as successful protocol execution.

~~~text
CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
~~~

Across DIAG-CH-001 and DIAG-CH-002, directly exercise all six primary Diagnosis statuses:

~~~text
DIAGNOSIS_ESTABLISHED
DIAGNOSIS_NOT_ESTABLISHED
DIAGNOSIS_BLOCKED
DIAGNOSIS_CONFLICTING
DIAGNOSIS_OUT_OF_SCOPE
DIAGNOSIS_UNDERDETERMINED
~~~

and all seven task terminals:

~~~text
DIAGNOSIS_TASK_ESTABLISHED
DIAGNOSIS_TASK_PARTIAL
DIAGNOSIS_TASK_NOT_ESTABLISHED
DIAGNOSIS_TASK_BLOCKED
DIAGNOSIS_TASK_CONFLICTING
DIAGNOSIS_TASK_OUT_OF_SCOPE
DIAGNOSIS_TASK_UNDERDETERMINED
~~~

DIAG-CH-001 already directly exercised `DIAGNOSIS_ESTABLISHED` and `DIAGNOSIS_TASK_ESTABLISHED`.

## 3. Frozen challenge bundle

~~~text
CHALLENGE_ID:
  DIAG-CH-002

CHALLENGE_VERSION:
  1

SUBCASES:
  N1 N2 N3 N4 N5 N6 N7 N8 N9 N10

DEFAULT_INFERENCE_MODE:
  DETERMINISTIC_COMPATIBILITY

METHOD_GAIN_ASSESSMENT:
  not_requested

POST_HOC_REPAIR:
  prohibited
~~~

## 4. N1 — evaluable uniqueness claim fails

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N1

PRIMARY_CLAIM_LEVEL:
  UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

CANDIDATE_CLASS:
  {h1,h2}

EVIDENCE:
  y=0

BRIDGE:
  h1 -> y=0
  h2 -> y=0

EVIDENCE_SET:
  coherent

BRIDGE_STATUS:
  available

REQUIRED_INTERFACES:
  available
~~~

Execution is fully evaluable and leaves:

~~~text
compatible:
  {h1,h2}

candidate-set outcome:
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
~~~

Expected:

~~~text
PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
MULTIPLE_COMPATIBLE
  !=
BLOCKED

FAILED_UNIQUENESS_CLAIM
  !=
TASK_UNDERDETERMINED
~~~

## 5. N2 — blocked by unavailable required support sidecar

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N2

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

CANDIDATE_CLASS:
  {s1,s2}

MAIN_READOUT:
  equal for s1 and s2

required support sidecar:
  unavailable

support distinction:
  claim-relevant

no substitute interface:
  authorized
~~~

Expected:

~~~text
REQUIRED_DIAGNOSIS_INTERFACE_STATUS:
  REQUIRED_DIAGNOSIS_INTERFACE_UNAVAILABLE

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_BLOCKED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_BLOCKED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE
  !=
EVALUABLE_INCOMPATIBILITY

BLOCKED
  !=
NOT_ESTABLISHED
~~~

## 6. N3 — conflicting bridge rules

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N3

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

candidate:
  c

evidence:
  e

same frozen bridge identity/version/scope:

rule A:
  c,e -> PAIR_COMPATIBLE

rule B:
  c,e -> PAIR_INCOMPATIBLE

resolver:
  none
~~~

Expected:

~~~text
BRIDGE_RELATION_STATUS:
  BRIDGE_RELATION_CONFLICTING

PAIR_DISPOSITION:
  PAIR_CONFLICTING

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_CONFLICTING

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_CONFLICTING

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
PAIR_INCOMPATIBLE != PAIR_CONFLICTING
CONFLICTING != UNDERDETERMINED
~~~

## 7. N4 — underdetermined bridge semantics

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N4

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

candidate:
  u

evidence:
  e

interpretation A:
  admissible
  u,e -> PAIR_COMPATIBLE

interpretation B:
  admissible
  u,e -> PAIR_INCOMPATIBLE

records mutually contradictory under one interpretation:
  no

resolver:
  none
~~~

Expected:

~~~text
BRIDGE_RELATION_STATUS:
  BRIDGE_RELATION_UNDERDETERMINED

PAIR_DISPOSITION:
  PAIR_UNDERDETERMINED

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_UNDERDETERMINED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_UNDERDETERMINED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
MULTIPLE_ADMISSIBLE_SEMANTICS
  !=
CONFLICTING_RECORDS
~~~

## 8. N5 — requested relation outside frozen bridge scope

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N5

PRIMARY_CLAIM_LEVEL:
  CURRENT_STATE_OR_CONDITION_IDENTIFICATION

CANDIDATE_CLASS:
  regime R2 states

BRIDGE_SCOPE:
  regime R1 only

extension from R1 to R2:
  not declared

requested Diagnosis relation:
  R2
~~~

Expected:

~~~text
BRIDGE_RELATION_STATUS:
  BRIDGE_RELATION_OUT_OF_SCOPE

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_OUT_OF_SCOPE

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_OUT_OF_SCOPE

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != BLOCKED
~~~

## 9. N6 — valid PARTIAL multi-obligation task

Frozen task contains two independently required in-scope Diagnosis obligations.

Primary claim:

~~~text
TASK_ID:
  DIAG-CH-002-N6

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET
~~~

Q1:

~~~text
candidate class:
  {p1,p2}

evidence / bridge:
  coherent and complete

result:
  compatible set {p1}

obligation result:
  DIAGNOSIS_ESTABLISHED
~~~

Q2:

~~~text
required subordinate uniqueness obligation:
  UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

candidate class:
  {q1,q2}

evidence / bridge:
  coherent and complete

result:
  compatible set {q1,q2}

obligation result:
  DIAGNOSIS_NOT_ESTABLISHED
~~~

No out-of-scope, conflicting, underdetermined, or blocked state exists.

Expected:

~~~text
PRIMARY_DIAGNOSIS_STATUS_FOR_Q1:
  DIAGNOSIS_ESTABLISHED

SUBORDINATE_Q2_STATUS:
  DIAGNOSIS_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_PARTIAL

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
PARTIAL
  requires multiple independently required in-scope obligations

PARTIAL
  !=
rescue label for one failed atomic claim
~~~

## 10. N7 — conflicting evidence packet is not zero-candidate Diagnosis

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N7

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

same sensor:
  S

same time:
  t0

same exact single-valued schema:
  yes

e1:
  S(t0)=0
  valid

e2:
  S(t0)=1
  valid

precedence/resolver:
  none
~~~

Candidates:

~~~text
z0 predicts 0
z1 predicts 1
~~~

Each candidate would fail one record if the evidence packet were incorrectly treated as coherent.

Expected:

~~~text
EVIDENCE_SET_COHERENCE_STATUS:
  EVIDENCE_SET_CONFLICTING

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_CONFLICTING

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_CONFLICTING

DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS:
  not asserted

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
EVIDENCE_CONFLICT
  !=
CANDIDATE_EXCLUSION_BY_DEFAULT
~~~

## 11. N8 — coherent zero-compatible candidate class

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N8

PRIMARY_CLAIM_LEVEL:
  CANDIDATE_COMPATIBILITY_SET

CANDIDATE_CLASS:
  {n1,n2}

EVIDENCE:
  y=2

BRIDGE:
  n1 predicts y=0
  n2 predicts y=1

EVIDENCE_SET:
  coherent

BRIDGE:
  available
~~~

Expected:

~~~text
n1:
  DIAGNOSIS_CANDIDATE_EXCLUDED

n2:
  DIAGNOSIS_CANDIDATE_EXCLUDED

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
NONE_COMPATIBLE_IN_DECLARED_CLASS
  !=
NO_REAL_STATE_EXISTS
~~~

## 12. N9 — evaluable causal-identification claim not established

Frozen task:

~~~text
TASK_ID:
  DIAG-CH-002-N9

PRIMARY_CLAIM_LEVEL:
  CAUSE_IDENTIFICATION_WITH_SUPPLIED_CAUSAL_BRIDGE

CAUSE_CANDIDATES:
  {k1,k2}

evidence:
  compatible with both k1 and k2

causal bridge:
  supplied
  valid in declared model
  non-discriminating between k1 and k2

required interfaces:
  all available
~~~

Expected:

~~~text
CAUSE_CLAIM_STATUS:
  CAUSE_IDENTIFICATION_NOT_ESTABLISHED

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Guard:

~~~text
CAUSE_BRIDGE_AVAILABLE
  !=
CAUSE_IDENTIFICATION_ESTABLISHED

CAUSE_COMPATIBILITY
  !=
CAUSAL_CERTAINTY
~~~

## 13. N10 — terminal precedence with subordinate-state retention

Frozen task contains four independent required obligations.

Q1:

~~~text
requested current-state relation lies outside frozen bridge scope

status:
  DIAGNOSIS_OUT_OF_SCOPE
~~~

Q2:

~~~text
same candidate/evidence pair receives mutually incompatible
same-version applicable bridge rules

status:
  DIAGNOSIS_CONFLICTING
~~~

Q3:

~~~text
two admissible bridge interpretations produce different outcomes
with no resolver

status:
  DIAGNOSIS_UNDERDETERMINED
~~~

Q4:

~~~text
required support sidecar unavailable

status:
  DIAGNOSIS_BLOCKED
~~~

Frozen precedence:

~~~text
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

Expected:

~~~text
TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_OUT_OF_SCOPE

LOWER_LEVEL_Q2_RETAINED:
  yes

LOWER_LEVEL_Q3_RETAINED:
  yes

LOWER_LEVEL_Q4_RETAINED:
  yes

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

No lower-level status may be erased merely because Q1 determines the terminal.

## 14. Protocol-conformance expectation

Every subcase is expected to remain:

~~~text
DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

including negative, blocked, conflicting, underdetermined, out-of-scope, partial, and bounded established outcomes.

No subcase assesses method gain.

~~~text
DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NOT_ASSESSED
~~~

## 15. Frozen scoring — 80 checks

Each subcase has eight checks.

### N1 — 8

~~~text
N1-1 unique claim frozen
N1-2 evidence set coherent
N1-3 bridge available
N1-4 both candidates compatible
N1-5 MULTIPLE_COMPATIBLE retained
N1-6 primary NOT_ESTABLISHED
N1-7 terminal NOT_ESTABLISHED
N1-8 protocol CONFORMANT
~~~

### N2 — 8

~~~text
N2-1 support distinction claim-relevant
N2-2 required support interface unavailable
N2-3 unavailable not converted to negative evidence
N2-4 unavailable not converted to incompatibility
N2-5 primary BLOCKED
N2-6 terminal BLOCKED
N2-7 BLOCKED != NOT_ESTABLISHED
N2-8 protocol CONFORMANT
~~~

### N3 — 8

~~~text
N3-1 same bridge identity/version/scope frozen
N3-2 rule A applicable
N3-3 rule B applicable
N3-4 outcomes mutually incompatible
N3-5 no resolver
N3-6 pair/bridge CONFLICTING
N3-7 terminal CONFLICTING
N3-8 protocol CONFORMANT
~~~

### N4 — 8

~~~text
N4-1 two admissible interpretations frozen
N4-2 interpretation A compatible
N4-3 interpretation B incompatible
N4-4 no one-interpretation contradiction fabricated
N4-5 no resolver
N4-6 bridge/pair UNDERDETERMINED
N4-7 terminal UNDERDETERMINED
N4-8 protocol CONFORMANT
~~~

### N5 — 8

~~~text
N5-1 requested regime R2 frozen
N5-2 bridge scope R1 frozen
N5-3 no R1->R2 extension declared
N5-4 relation outside scope
N5-5 primary OUT_OF_SCOPE
N5-6 terminal OUT_OF_SCOPE
N5-7 OUT_OF_SCOPE != BLOCKED
N5-8 protocol CONFORMANT
~~~

### N6 — 8

~~~text
N6-1 two independent required in-scope obligations
N6-2 Q1 fully evaluable
N6-3 Q1 established
N6-4 Q2 fully evaluable
N6-5 Q2 uniqueness not established
N6-6 no higher-priority terminal
N6-7 terminal PARTIAL
N6-8 protocol CONFORMANT
~~~

### N7 — 8

~~~text
N7-1 same sensor/time/schema frozen
N7-2 e1 valid zero
N7-3 e2 valid one
N7-4 no resolver
N7-5 evidence set CONFLICTING
N7-6 zero-compatible set not asserted
N7-7 terminal CONFLICTING
N7-8 protocol CONFORMANT
~~~

### N8 — 8

~~~text
N8-1 evidence y=2 frozen
N8-2 evidence coherent
N8-3 bridge available
N8-4 n1 excluded
N8-5 n2 excluded
N8-6 set NONE_COMPATIBLE_IN_DECLARED_CLASS
N8-7 task ESTABLISHED without ontological overclaim
N8-8 protocol CONFORMANT
~~~

### N9 — 8

~~~text
N9-1 causal-identification claim frozen
N9-2 causal bridge supplied
N9-3 all required interfaces available
N9-4 k1 compatible
N9-5 k2 compatible
N9-6 cause identification NOT_ESTABLISHED
N9-7 terminal NOT_ESTABLISHED
N9-8 protocol CONFORMANT
~~~

### N10 — 8

~~~text
N10-1 Q1 OUT_OF_SCOPE retained
N10-2 Q2 CONFLICTING retained
N10-3 Q3 UNDERDETERMINED retained
N10-4 Q4 BLOCKED retained
N10-5 precedence frozen
N10-6 terminal OUT_OF_SCOPE
N10-7 subordinate states preserved
N10-8 protocol CONFORMANT
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASS_THRESHOLD:
  80/80

PARTIAL_PASS_ALLOWED:
  no
~~~

## 16. Counter rule

If all 80 checks pass:

~~~text
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  2

POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

ALL_SIX_DIAGNOSIS_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_DIAGNOSIS_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  0

BASELINE_DIAGNOSIS_CASES:
  0

NO_GAIN_DIAGNOSIS_CASES:
  0

REPRODUCIBILITY_CASES:
  0

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 17. Next

If the frozen bundle passes, prospectively precommit the direct neighboring-method boundary challenge.
