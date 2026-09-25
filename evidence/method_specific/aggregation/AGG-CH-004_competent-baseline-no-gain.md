# AGG-CH-004 — Competent Non-DSD Aggregation Baseline Result

Status: **EXECUTED — 64/64 PASS / NO_GAIN**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-004`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Baseline: **B0_GENERIC_TYPED_AGGREGATION_EVALUATOR**

## 1. Frozen references

```text
AGGREGATION_PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

AGGREGATION_PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1

PRECOMMIT_COMMIT:
  e1152eae067817b0798b8e7618fad2362fd35b5f

PRECOMMIT_BLOB:
  f7b36207895160e1318c447b0e7528b518788e11
```

No protocol rule, baseline operation, output mapping, fixture, gain axis, or scoring rule was changed after precommit.

## 2. Final result

```text
TOTAL_REQUIRED_CHECKS:
  64

PASSED:
  64

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

AGGREGATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NO_GAIN

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

The competent generic evaluator reproduced the claim-relevant Aggregation outputs for the frozen tasks under equal-information access.

## 3. Equal-information verification

Aggregation and B0 received the same:

```text
task/version/claim identity
selected supports and source IDs
typed source statuses
provenance records
aggregation operators and output spaces
coordinate declarations
support/status sidecar policy
countable-extension rule
postprocessing map
collision/injectivity task data
reconstruction scope
required-interface availability
conflict/scope/alternative-class records
terminal precedence
maximum-supported claim
```

Result:

```text
FAIRNESS_CHECK:
  PASS
```

B0 was not asked to derive the DSD ontology from first principles.

It was asked to execute the same already-frozen task interface with the same claim-relevant information.

## 4. Q1 — positive combined finite aggregation

### Aggregation

```text
Comp(F):
  (1,4)

Agg(G):
  (3,2)

combined descriptor:
  ((1,4),(3,2))

separate equal-weight channel average:
  (1/3,4/3)

terminal:
  AGGREGATION_TASK_ESTABLISHED
```

Preserved:

```text
c0 defined zero != cX absent
i0 defined zero != u1 applicable-but-undefined
multi-input datum retains full typed input
formation coordinate != property coordinate
direct aggregate != postprocessing
```

### B0

Using the same supplied typed records and operators:

```text
channel readout:
  (1,4)

property readout:
  (3,2)

combined pair:
  ((1,4),(3,2))

separate declared postprocessing:
  (1/3,4/3)

terminal:
  B0_TASK_COMPLETE
```

B0 preserved the same explicit status and support distinctions.

Comparison:

```text
Q1_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q1.

## 5. Q2 — finite-domain and countable-admission failures

### Q2A — absent selected channel

Aggregation:

```text
absent channel:
  not zero-extended

domain:
  AGGREGATION_DOMAIN_NOT_ADMITTED

terminal:
  AGGREGATION_TASK_NOT_ESTABLISHED
```

B0:

```text
explicitly absent selected input:
  not coerced to zero

domain:
  rejected as evaluably not admitted

terminal:
  B0_TASK_NOT_ESTABLISHED
```

Claim-relevant match:

```text
yes
```

### Q2B — conditional but not absolute convergence

Frozen series:

```text
T_n = (-1)^(n+1)/n
```

Both evaluators recognize:

```text
ordinary convergence:
  conditional

absolute summability:
  fails
```

Aggregation:

```text
countable extension:
  not admitted

terminal:
  AGGREGATION_TASK_NOT_ESTABLISHED
```

B0:

```text
supplied countable admission rule:
  fails

terminal:
  B0_TASK_NOT_ESTABLISHED
```

Comparison:

```text
Q2_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q2.

## 6. Q3 — blocked / conflict / unresolved semantics

### Q3A — missing required inverse interfaces

Aggregation:

```text
required support sidecar:
  unavailable

required cross-coordinate condition:
  unavailable

terminal:
  AGGREGATION_TASK_BLOCKED
```

B0:

```text
required inverse-task interfaces:
  unavailable

terminal:
  B0_TASK_BLOCKED
```

Neither side converts unavailable required evidence into an evaluable negative result.

### Q3B — conflicting postprocessing definitions

Frozen:

```text
same map ID/version
two applicable incompatible definitions
no precedence
```

Aggregation:

```text
AGGREGATION_TASK_CONFLICTING
```

B0:

```text
B0_TASK_CONFLICT
```

Neither side chooses a preferred map post hoc.

### Q3C — unresolved injectivity class

Frozen:

```text
A_F^(1):
  injective

A_F^(2):
  non-injective

resolver:
  none
```

Aggregation:

```text
INJECTIVITY_UNDERDETERMINED
AGGREGATION_TASK_UNDERDETERMINED
```

B0:

```text
B0_INJECTIVITY_UNRESOLVED
B0_TASK_UNRESOLVED
```

Comparison:

```text
Q3_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q3.

## 7. Q4 — collision and declared-class injectivity

### Q4A — collision witness

Frozen:

```text
(1,-1) -> 0
(2,-2) -> 0
```

Aggregation:

```text
COLLISION_WITNESS_ESTABLISHED
INJECTIVITY_NOT_ESTABLISHED
AGGREGATION_TASK_NOT_ESTABLISHED
```

B0:

```text
B0_COLLISION_WITNESS
B0_NOT_INJECTIVE_ON_DECLARED_CLASS
B0_TASK_NOT_ESTABLISHED
```

Both preserve:

```text
same output != same assignment
```

### Q4B — injective declared finite class

Frozen:

```text
A_F:
  {(0,0),(1,0),(2,0)}

outputs:
  0,1,2
```

Aggregation:

```text
NO_COLLISION_ON_TESTED_CLASS
INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS
AGGREGATION_TASK_ESTABLISHED
GLOBAL_INJECTIVITY:
  not claimed
```

B0:

```text
B0_NO_COLLISION_ON_DECLARED_CLASS
B0_INJECTIVE_ON_DECLARED_CLASS
B0_TASK_COMPLETE
GLOBAL_INJECTIVITY:
  not claimed
```

Comparison:

```text
Q4_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q4.

## 8. Q5 — partial / outside-scope / precedence

### Q5A — partial multi-obligation task

Aggregation:

```text
one obligation:
  established

one obligation:
  evaluably not established

terminal:
  AGGREGATION_TASK_PARTIAL
```

B0:

```text
one obligation:
  complete

one obligation:
  not established

terminal:
  B0_TASK_PARTIAL
```

### Q5B — uncountable request

Aggregation:

```text
AGGREGATION_TASK_OUT_OF_SCOPE
```

B0:

```text
B0_TASK_OUTSIDE_SCOPE
```

Neither side converts scope exclusion into falsehood.

### Q5C — terminal precedence

Frozen lower states:

```text
conflict
unresolved semantics
blocked required interface
```

Both evaluators apply:

```text
CONFLICT
>
UNRESOLVED
>
BLOCKED
```

Aggregation:

```text
AGGREGATION_TASK_CONFLICTING
```

B0:

```text
B0_TASK_CONFLICT
```

Both retain lower-level unresolved and blocked records.

Comparison:

```text
Q5_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q5.

## 9. Q6 — bounded-claim / neighboring-sidecar discipline

Both evaluators receive the same:

```text
forward aggregate
support sidecar
collision result
declared-class injectivity result
Tracking sidecar
Lineage sidecar
Comparison sidecar
Classification sidecar
Audit sidecar
```

Neither infers without an explicit supplied rule:

```text
source identity
support identity
global injectivity
Lineage identity
classification membership
comparison equivalence
audit pass
external validity
```

Comparison:

```text
Q6_CLAIM_RELEVANT_MATCH:
  yes
```

No gain is established on Q6.

## 10. Frozen gain-axis result

The six precommitted axes were scored only from claim-relevant outputs.

```text
G1 typed-status and support-preservation advantage:
  BASELINE_MATCH

G2 finite/countable domain and convergence-discipline advantage:
  BASELINE_MATCH

G3 coordinate-separation and postprocessing-boundary advantage:
  BASELINE_MATCH

G4 collision / declared-class injectivity /
   reconstruction-scope advantage:
  BASELINE_MATCH

G5 negative / blocked / conflict / scope /
   underdetermination / partial terminal-semantic advantage:
  BASELINE_MATCH

G6 bounded-claim / neighboring-sidecar /
   overclaim-prevention advantage:
  BASELINE_MATCH
```

Therefore:

```text
AGGREGATION_METHOD_GAIN_STATUS:
  AGGREGATION_METHOD_GAIN_NO_GAIN
```

No DSD-specific performance advantage was established by this competent-baseline fixture.

## 11. Meaning of NO_GAIN

Here:

```text
NO_GAIN
  =
no claim-relevant performance advantage over
B0_GENERIC_TYPED_AGGREGATION_EVALUATOR was established
for the frozen constructed tasks under equal-information access
```

It does not mean:

```text
Aggregation protocol failure
Aggregation should be deleted
Aggregation should merge into Compression
Aggregation should merge into Reconstruction
Aggregation is identical to every aggregation framework
Aggregation has no theoretical or organizational role
future gain is impossible
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 12. Execution of the 64 frozen checks

### A. Fairness and immutability

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

### B. Q1 positive combined aggregation

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
B13 PASS
B14 PASS

B: 14/14
```

### C. Q2 finite/countable admission

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

C: 10/10
```

### D. Q3 blockage / conflict / unresolved

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

D: 10/10
```

### E. Q4 collision / injectivity

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

E: 10/10
```

### F. Q5 terminal and precedence semantics

```text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS

F: 6/6
```

### G. Q6 and gain conclusion

```text
G1 PASS
G2 PASS
G3 PASS
G4 PASS

G: 4/4
```

Final:

```text
TOTAL_REQUIRED_CHECKS:
  64

PASSED:
  64

FAILED:
  0
```

## 13. Counter update

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  4

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  4

POSITIVE_AGGREGATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_AGGREGATION_CASES:
  1

METHOD_BOUNDARY_AGGREGATION_CASES:
  1

BASELINE_AGGREGATION_CASES:
  1

NO_GAIN_AGGREGATION_CASES:
  1

STRONGEST_REASONABLE_BASELINE_AGGREGATION:
  not established

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

## 14. Maximum-supported claim

Supported:

```text
For the frozen AGG-CH-004 constructed tasks,
a competent non-DSD typed aggregation evaluator with equal
claim-relevant information reproduced all claim-relevant
Aggregation outputs and matched all six precommitted gain axes.

The result is NO_GAIN against this baseline.
```

Not established:

```text
strongest-reasonable baseline closure
method redundancy
method merger
external applicability
independent validation
independent replication
```

## 15. Next

Prospectively precommit the strongest-reasonable non-DSD Aggregation baseline.

It should be materially stronger than B0 by supporting, in one evaluator:

```text
versioned aggregation-rule registries
typed finite/countable operator families
automatic domain/admission validation
symbolic or exact collision detection where finite/exactly decidable
kernel/injectivity analysis on supplied algebraic classes
support-aware provenance
multiple coordinate families
explicit postprocessing pipelines
alternative-schema management
dependency-aware inverse-claim prerequisites
bounded-claim generation
deterministic execution ledgers
rerun manifests
```

A second NO_GAIN remains an acceptable result.
