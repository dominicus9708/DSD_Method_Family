# AGG-CH-005 — Strongest-Reasonable Non-DSD Aggregation Baseline Result

Status: **EXECUTED — 82/82 PASS / NO_GAIN**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-005`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Baseline: **B1_STRONG_AGGREGATION_ENGINE**

## 1. Frozen references

```text
AGGREGATION_PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

AGGREGATION_PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1

PRECOMMIT_COMMIT:
  da2bb2cb33d51f902e0a9a956846a13c0403a46a

PRECOMMIT_BLOB:
  d384d7f1c7a4fae71ad46ae12e7cbf504a8dc0d4
```

No task, fixture, baseline capability, gain axis, rule version, scoring item, or pass threshold was changed after the final precommit freeze.

## 2. Final result

```text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

BASELINE_WEAKENED_POST_HOC:
  no

AGGREGATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  established_at_constructed_evidence_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

B1 is materially stronger than AGG-CH-004's B0 and still reproduced the claim-relevant Aggregation outputs on the frozen workload.

## 3. R1 — versioned rule registry and postprocessing pipeline

Frozen task version:

```text
TASK_VERSION:
  1
```

Rule registry:

```text
AGG-RULE-v1:
  finite direct sum
  valid for task version 1

AGG-RULE-v2:
  weighted finite operator
  valid only for task version 2

POST-v1:
  equal-weight average
  downstream only
```

Frozen terms:

```text
T(c1)=(2,1)
T(c2)=(-1,3)
T(c0)=(0,0)
```

Aggregation and B1 both select:

```text
AGG-RULE-v1
```

and compute:

```text
(2,1)+(-1,3)+(0,0)
  =
(1,4)
```

Both reject retroactive substitution of AGG-RULE-v2.

Both separately execute:

```text
POST-v1:
  ((2,1)+(-1,3)+(0,0))/3
  =
  (1/3,4/3)
```

Neither replaces the primary aggregate with the postprocessed readout.

Both retain rule/version provenance.

Result:

```text
R1:
  BASELINE_MATCH
```

## 4. R2 — exact kernel and declared-class injectivity

Frozen operator:

```text
S(x,y,z):
  (x+z,y+z)
```

Kernel equations:

```text
x+z=0
y+z=0
```

Hence:

```text
x=-z
y=-z
```

and therefore:

```text
ker(S)
  =
{(-t,-t,t): t in R}
  =
span{(-1,-1,1)}
```

Both systems record:

```text
GLOBAL_INJECTIVITY:
  not established
```

because the kernel is nontrivial.

Frozen declared class:

```text
A:
  {(x,y,0): x,y in R}
```

Restricted map:

```text
S|_A(x,y,0):
  (x,y)
```

Therefore both establish:

```text
INJECTIVITY_ON_DECLARED_CLASS:
  yes
```

Explicit collision outside the restricted class:

```text
S(0,0,0):
  (0,0)

S(-1,-1,1):
  (0,0)

(0,0,0) != (-1,-1,1)
```

Both preserve:

```text
DECLARED_CLASS_INJECTIVITY
  !=
GLOBAL_INJECTIVITY
```

Result:

```text
R2:
  BASELINE_MATCH
```

## 5. R3 — admitted countable extension with exact sum

Frozen terms:

```text
T_n:
  (2^-n,2^-(n+1))
  for n >= 1
```

The supplied `l1` majorant is:

```text
||T_n||_1
  =
2^-n + 2^-(n+1)
  =
3 * 2^-(n+1)
```

and:

```text
sum_{n>=1} ||T_n||_1
  =
3/2
```

Thus the frozen absolute-summability admission rule passes.

Exact componentwise sums:

```text
sum_{n>=1} 2^-n
  =
1

sum_{n>=1} 2^-(n+1)
  =
1/2
```

Both systems compute:

```text
COUNTABLE_AGGREGATE:
  (1,1/2)

COUNTABLE_DOMAIN:
  admitted
```

Both retain:

```text
absolute-summability evidence
countable support identity
countable provenance
```

Neither relabels the result as the finite core.

Result:

```text
R3:
  BASELINE_MATCH
```

## 6. R4 — multi-coordinate inverse dependency closure

Available:

```text
Y1 channel aggregate:
  established

Y2 property aggregate:
  established

D1 channel support sidecar:
  available

D2 property support sidecar:
  available
```

Required but unavailable:

```text
D3 cross-coordinate coupling rule:
  requires XC-v3

XC-v3:
  unavailable
```

Both systems preserve the forward aggregates as established.

For the separately frozen combined-coordinate inverse claim, both compute the prerequisite closure and obtain:

```text
D3:
  blocked

combined-coordinate inverse claim:
  BLOCKED
```

Neither converts missing XC-v3 into an evaluable negative reconstruction result.

Neither promotes coordinatewise evidence into combined-coordinate reconstructibility.

Result:

```text
R4:
  BASELINE_MATCH
```

## 7. R5 — integrated alternative schema / conflict / sidecar / rerun pressure

### Q1 — conflicting version-identity record

Two equally applicable registry entries use the same frozen map identity:

```text
MAP-v7:
  direct sum

MAP-v7:
  normalized mean
```

No precedence resolver is supplied.

Both systems retain both records and emit:

```text
Q1:
  CONFLICT
```

Neither chooses one map post hoc.

### Q2 — unresolved admissible injectivity class

Two admissible class schemas produce different injectivity outcomes.

No resolver is supplied.

Both systems retain both and emit:

```text
Q2:
  UNDERDETERMINED / UNRESOLVED
```

### Q3 — established forward aggregate plus neighboring sidecars

Supplied sidecars:

```text
Tracking provenance
Lineage identity
high Comparison similarity
same Classification class
Reconstruction candidate
Audit conformance
```

Both systems preserve them as sidecars.

Neither promotes them into independent aggregation validity, source identity, or support identity criteria.

The forward aggregate remains established from the supplied aggregation rule itself.

Frozen precedence yields:

```text
run terminal:
  CONFLICT
```

Both retain lower-level Q2 and Q3 states.

Both emit deterministic ledgers and rerun identifiers/manifests.

Result:

```text
R5:
  BASELINE_MATCH
```

## 8. Frozen gain-axis result

All seven precommitted gain axes were scored only from frozen claim-relevant outputs.

```text
G1 VERSIONED_RULE_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 EXACT_OPERATOR_KERNEL_AND_DECLARED_CLASS_GAIN:
  BASELINE_MATCH

G3 COUNTABLE_ADMISSION_AND_EXACT_EXTENSION_GAIN:
  BASELINE_MATCH

G4 MULTICOORDINATE_DEPENDENCY_CLOSURE_GAIN:
  BASELINE_MATCH

G5 CONFLICT_UNDERDETERMINATION_AND_SIDECAR_BOUNDARY_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH
```

Therefore:

```text
AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  established_at_constructed_evidence_level
```

No claim-relevant DSD performance advantage over B1 was established on this workload.

No claim-relevant B1 advantage was established either.

## 9. Meaning of strongest-reasonable NO_GAIN

Supported:

```text
At the constructed-evidence level, a materially strong non-DSD
aggregation engine matched the claim-relevant Aggregation results
on the frozen R1-R5 workload under equal-information access.
```

Not supported:

```text
Aggregation is redundant
Aggregation should be deleted
Aggregation should merge into Compression
Aggregation should merge into Reconstruction
all future Aggregation tasks will produce NO_GAIN
B1 is universally strongest possible
external applicability is established
independent validation is established
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY

STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE
```

## 10. Execution of the 82 frozen checks

### A. Immutable fairness

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS

A: 10/10
```

### B. R1 versioned rule registry

```text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS
B11 PASS
B12 PASS

B: 12/12
```

### C. R2 exact kernel / declared class

```text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS
C11 PASS
C12 PASS
C13 PASS
C14 PASS

C: 14/14
```

### D. R3 countable admitted extension

```text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS
D11 PASS
D12 PASS

D: 12/12
```

### E. R4 inverse dependency closure

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS
E9 PASS
E10 PASS
E11 PASS
E12 PASS

E: 12/12
```

### F. R5 integrated pressure

```text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS
F8 PASS
F9 PASS
F10 PASS
F11 PASS
F12 PASS
F13 PASS
F14 PASS

F: 14/14
```

### G. Comparative conclusion

```text
G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS
G8 PASS

G: 8/8
```

Final:

```text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
```

## 11. Counter update

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  5

POSITIVE_AGGREGATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_AGGREGATION_CASES:
  1

METHOD_BOUNDARY_AGGREGATION_CASES:
  1

BASELINE_AGGREGATION_CASES:
  2

NO_GAIN_AGGREGATION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  0

EXTERNAL_AGGREGATION_APPLICATIONS:
  0

INDEPENDENT_AGGREGATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

AGGREGATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_AGGREGATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 12. Maximum-supported claim

Supported:

```text
For the frozen AGG-CH-005 constructed workload, the materially
strong B1_STRONG_AGGREGATION_ENGINE reproduced all claim-relevant
Aggregation outputs under equal-information access, including
versioned rule use, exact kernel/class-local injectivity analysis,
admitted countable extension, inverse dependency closure, conflict/
underdetermination handling, bounded claims, and deterministic rerun records.
```

Not established:

```text
universal strongest baseline
method redundancy
method merger
external applicability
independent validation
independent replication
```

## 13. Next

Prospectively precommit and execute deterministic same-project Aggregation retrace.

The retrace should reconstruct the strongest-baseline Aggregation-side outputs from frozen upstream artifacts before comparing against this result.

Required interpretation locks:

```text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```
