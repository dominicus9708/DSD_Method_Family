# DIAG-CH-002 — Negative / Unresolved-Terminal Diagnosis Challenge Result

Status: **EXECUTED — 80/80 PASS**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-002`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `negative_unresolved_terminal_coverage_constructed`

## 1. Frozen references

~~~text
PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

PRECOMMIT_COMMIT:
  119407929fe5e9d43fd9fc04ac21ec9a49147950

PRECOMMIT_BLOB:
  655c5feab5626453027d89faca66842cd5506fc5
~~~

No protocol rule, subcase identity, candidate class, evidence set, bridge semantics, interface status, terminal target, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0

ALL_SIX_DIAGNOSIS_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_DIAGNOSIS_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

This is constructed internal validation only.

A conformant negative, blocked, conflicting, underdetermined, out-of-scope, partial, or zero-compatible result is not a method failure.

## 3. N1 — evaluable uniqueness claim fails

Frozen:

~~~text
H={h1,h2}
y=0
h1 -> 0
h2 -> 0
~~~

Execution:

~~~text
h1:
  DIAGNOSIS_CANDIDATE_COMPATIBLE

h2:
  DIAGNOSIS_CANDIDATE_COMPATIBLE

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_MULTIPLE_COMPATIBLE
~~~

All required evidence/bridge information was available.

Therefore this is not blocked, conflicting, or underdetermined.

Result:

~~~text
PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
FAILED_UNIQUENESS_CLAIM != BLOCKED
~~~

## 4. N2 — unavailable required support sidecar

Frozen support distinction was required and claim-relevant.

Availability:

~~~text
required support sidecar:
  unavailable
~~~

No replacement interface was authorized.

Result:

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

No candidate was excluded merely because the required sidecar was unavailable.

Preserved:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != EVALUABLE_INCOMPATIBILITY
BLOCKED != NOT_ESTABLISHED
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
~~~

## 5. N3 — conflicting bridge rules

Frozen same-version applicable bridge rules:

~~~text
rule A:
  c,e -> PAIR_COMPATIBLE

rule B:
  c,e -> PAIR_INCOMPATIBLE

resolver:
  none
~~~

Execution:

~~~text
BRIDGE_RELATION_STATUS:
  BRIDGE_RELATION_CONFLICTING

PAIR_DISPOSITION:
  PAIR_CONFLICTING

DIAGNOSIS_CANDIDATE_DISPOSITION:
  DIAGNOSIS_CANDIDATE_CONFLICTING

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_CONFLICTING

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_CONFLICTING

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
PAIR_INCOMPATIBLE != PAIR_CONFLICTING
CONFLICTING != UNDERDETERMINED
~~~

## 6. N4 — underdetermined bridge semantics

Frozen admissible interpretations:

~~~text
A:
  u,e -> PAIR_COMPATIBLE

B:
  u,e -> PAIR_INCOMPATIBLE
~~~

The records were not mutually contradictory within one frozen interpretation.

No resolver was supplied.

Result:

~~~text
BRIDGE_RELATION_STATUS:
  BRIDGE_RELATION_UNDERDETERMINED

PAIR_DISPOSITION:
  PAIR_UNDERDETERMINED

DIAGNOSIS_CANDIDATE_DISPOSITION:
  DIAGNOSIS_CANDIDATE_UNDERDETERMINED

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_UNDERDETERMINED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_UNDERDETERMINED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
MULTIPLE_ADMISSIBLE_SEMANTICS != CONFLICTING_RECORDS
~~~

## 7. N5 — relation outside frozen bridge scope

Frozen:

~~~text
requested task regime:
  R2

bridge scope:
  R1 only

declared extension:
  none
~~~

Result:

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

No missing in-scope evidence was fabricated.

Preserved:

~~~text
OUT_OF_SCOPE != FALSE
OUT_OF_SCOPE != BLOCKED
~~~

## 8. N6 — valid PARTIAL task

Two independent in-scope obligations were frozen.

Q1:

~~~text
compatible set:
  {p1}

Q1 status:
  DIAGNOSIS_ESTABLISHED
~~~

Q2:

~~~text
compatible set:
  {q1,q2}

required claim:
  UNIQUE_WITHIN_DECLARED_CANDIDATE_CLASS

Q2 status:
  DIAGNOSIS_NOT_ESTABLISHED
~~~

No higher-priority out-of-scope, conflicting, underdetermined, or blocked state occurred.

Result:

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

Preserved:

~~~text
PARTIAL
  requires multiple independent required in-scope obligations

PARTIAL
  !=
rescue label for one failed atomic claim
~~~

## 9. N7 — conflicting evidence packet

Frozen evidence:

~~~text
same sensor:
  S

same time:
  t0

same exact single-valued schema:
  yes

e1:
  S(t0)=0

e2:
  S(t0)=1

resolver:
  none
~~~

Result:

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

Preserved:

~~~text
EVIDENCE_CONFLICT != CANDIDATE_EXCLUSION_BY_DEFAULT
NONE_COMPATIBLE_IN_DECLARED_CLASS != EVIDENCE_SET_CONFLICTING
~~~

## 10. N8 — coherent zero-compatible candidate class

Frozen:

~~~text
evidence:
  y=2

n1 predicts:
  y=0

n2 predicts:
  y=1
~~~

Evidence was coherent and the bridge was available.

Execution:

~~~text
n1:
  DIAGNOSIS_CANDIDATE_EXCLUDED

n2:
  DIAGNOSIS_CANDIDATE_EXCLUDED

COMPATIBLE_CANDIDATE_SET:
  {}

EXCLUDED_CANDIDATE_SET:
  {n1,n2}

DIAGNOSIS_SET_OUTCOME:
  DIAGNOSIS_SET_NONE_COMPATIBLE_IN_DECLARED_CLASS

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

The established result is exactly the bounded statement that no declared candidate is compatible.

It does not assert:

~~~text
NO_REAL_STATE_EXISTS
~~~

## 11. N9 — causal-identification claim evaluably fails

Frozen cause candidates:

~~~text
{k1,k2}
~~~

The supplied causal bridge was available and valid within the declared model but did not discriminate k1 from k2.

Execution:

~~~text
k1:
  compatible

k2:
  compatible

CAUSE_CLAIM_STATUS:
  CAUSE_IDENTIFICATION_NOT_ESTABLISHED

PRIMARY_DIAGNOSIS_STATUS:
  DIAGNOSIS_NOT_ESTABLISHED

TASK_TERMINAL_STATUS:
  DIAGNOSIS_TASK_NOT_ESTABLISHED

PROTOCOL_CONFORMANCE:
  DIAGNOSIS_PROTOCOL_CONFORMANT
~~~

Preserved:

~~~text
CAUSE_BRIDGE_AVAILABLE != CAUSE_IDENTIFICATION_ESTABLISHED
CAUSE_COMPATIBILITY != CAUSAL_CERTAINTY
~~~

## 12. N10 — terminal precedence

Frozen subordinate obligation states:

~~~text
Q1:
  DIAGNOSIS_OUT_OF_SCOPE

Q2:
  DIAGNOSIS_CONFLICTING

Q3:
  DIAGNOSIS_UNDERDETERMINED

Q4:
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

Execution:

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

The terminal summarized the run without erasing subordinate states.

## 13. Direct coverage achieved

Across DIAG-CH-001 and DIAG-CH-002:

Primary statuses:

~~~text
DIAGNOSIS_ESTABLISHED:
  directly exercised

DIAGNOSIS_NOT_ESTABLISHED:
  directly exercised

DIAGNOSIS_BLOCKED:
  directly exercised

DIAGNOSIS_CONFLICTING:
  directly exercised

DIAGNOSIS_OUT_OF_SCOPE:
  directly exercised

DIAGNOSIS_UNDERDETERMINED:
  directly exercised
~~~

Task terminals:

~~~text
DIAGNOSIS_TASK_ESTABLISHED:
  directly exercised

DIAGNOSIS_TASK_PARTIAL:
  directly exercised

DIAGNOSIS_TASK_NOT_ESTABLISHED:
  directly exercised

DIAGNOSIS_TASK_BLOCKED:
  directly exercised

DIAGNOSIS_TASK_CONFLICTING:
  directly exercised

DIAGNOSIS_TASK_OUT_OF_SCOPE:
  directly exercised

DIAGNOSIS_TASK_UNDERDETERMINED:
  directly exercised
~~~

Therefore:

~~~text
ALL_SIX_DIAGNOSIS_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_DIAGNOSIS_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes
~~~

## 14. Execution of the 80 frozen checks

### N1

~~~text
N1-1 PASS
N1-2 PASS
N1-3 PASS
N1-4 PASS
N1-5 PASS
N1-6 PASS
N1-7 PASS
N1-8 PASS
~~~

### N2

~~~text
N2-1 PASS
N2-2 PASS
N2-3 PASS
N2-4 PASS
N2-5 PASS
N2-6 PASS
N2-7 PASS
N2-8 PASS
~~~

### N3

~~~text
N3-1 PASS
N3-2 PASS
N3-3 PASS
N3-4 PASS
N3-5 PASS
N3-6 PASS
N3-7 PASS
N3-8 PASS
~~~

### N4

~~~text
N4-1 PASS
N4-2 PASS
N4-3 PASS
N4-4 PASS
N4-5 PASS
N4-6 PASS
N4-7 PASS
N4-8 PASS
~~~

### N5

~~~text
N5-1 PASS
N5-2 PASS
N5-3 PASS
N5-4 PASS
N5-5 PASS
N5-6 PASS
N5-7 PASS
N5-8 PASS
~~~

### N6

~~~text
N6-1 PASS
N6-2 PASS
N6-3 PASS
N6-4 PASS
N6-5 PASS
N6-6 PASS
N6-7 PASS
N6-8 PASS
~~~

### N7

~~~text
N7-1 PASS
N7-2 PASS
N7-3 PASS
N7-4 PASS
N7-5 PASS
N7-6 PASS
N7-7 PASS
N7-8 PASS
~~~

### N8

~~~text
N8-1 PASS
N8-2 PASS
N8-3 PASS
N8-4 PASS
N8-5 PASS
N8-6 PASS
N8-7 PASS
N8-8 PASS
~~~

### N9

~~~text
N9-1 PASS
N9-2 PASS
N9-3 PASS
N9-4 PASS
N9-5 PASS
N9-6 PASS
N9-7 PASS
N9-8 PASS
~~~

### N10

~~~text
N10-1 PASS
N10-2 PASS
N10-3 PASS
N10-4 PASS
N10-5 PASS
N10-6 PASS
N10-7 PASS
N10-8 PASS
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  80

PASSED:
  80

FAILED:
  0
~~~

## 15. Post-challenge state

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

## 16. Interpretation lock

~~~text
CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE

NOT_ESTABLISHED != BLOCKED

CONFLICTING != UNDERDETERMINED

OUT_OF_SCOPE != FALSE

PARTIAL != ATOMIC-FAILURE RESCUE

NONE_COMPATIBLE_IN_DECLARED_CLASS != NO_REAL_STATE_EXISTS

PROTOCOL_CONFORMANCE != TRUE_STATE_CERTAINTY

PASS != METHOD_SUPERIORITY
~~~

## 17. Next

Prospectively precommit and execute DIAG-CH-003 direct neighboring-method boundary challenge.
