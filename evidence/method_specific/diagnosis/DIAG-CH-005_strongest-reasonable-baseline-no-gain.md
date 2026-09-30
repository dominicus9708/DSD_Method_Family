# DIAG-CH-005 — Strongest-Reasonable Non-DSD Diagnosis Baseline Result

Status: **EXECUTED — 82/82 PASS / NO_GAIN**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-005`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Baseline: **B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE**

## 1. Frozen references

~~~text
DIAGNOSIS_PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

DIAGNOSIS_PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

PRECOMMIT_COMMIT:
  ce3c6d7e0bdab70453916875ef18b59720069114

PRECOMMIT_BLOB:
  7becc81d1ac3b9822fa6331fd8cfc6953e106c27
~~~

No Diagnosis Protocol rule, B1 capability, strong subcase, gain axis, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

DIAGNOSIS_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

BASELINE_WEAKENED_AFTER_PRECOMMIT:
  no

DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The materially stronger non-DSD B1 engine matched every claim-relevant Diagnosis result on the frozen strong workload.

The strongest-reasonable label is bounded to this constructed comparator class and workload.

## 3. Equal-information verification

Diagnosis and B1 received the same:

~~~text
task/version/claim identity
candidate-registry versions
candidate-class completeness records

evidence-registry versions
typed status/provenance/time/regime records
evidence-set coherence inputs

bridge-registry versions/scopes
pair relations

required-interface dependencies
status/support sidecars
readout/collision/injectivity records

resolution/threshold branches
residual and transition records

cause-model records
probabilistic priors/likelihoods/posterior semantics when supplied

terminal precedence
neighboring-method sidecars
maximum-supported claim
~~~

No hidden favorable input was supplied to Diagnosis.

No claim-relevant input was withheld from B1.

## 4. R1 — versioned registries and non-retroactivity

Frozen TASK-v1 used:

~~~text
CANDIDATES-v1:
  {h1,h2,h3}

EVIDENCE-v1:
  y=0
  status=DEFINED_ZERO
  support=S1

BRIDGE-v1:
  h1 -> y=0 / DEFINED_ZERO / S1
  h2 -> y=0 / DEFINED_ZERO / S1
  h3 -> y=0 / APPLICABLE_BUT_UNDEFINED / S2
~~~

Diagnosis:

~~~text
compatible:
  {h1,h2}

excluded:
  {h3}

task:
  DIAGNOSIS_TASK_ESTABLISHED

v2 retroactive substitution:
  prohibited
~~~

B1:

~~~text
compatible:
  {h1,h2}

excluded:
  {h3}

task:
  B1_TASK_COMPLETE

v2 retroactive substitution:
  prohibited
~~~

Both retained candidate/evidence/bridge registry provenance.

Result:

~~~text
MATCH
~~~

## 5. R2 — exact linear preimage and declared-class uniqueness

Frozen map:

~~~text
F(x,y,z):
  (x+z,y+z)
~~~

Exact kernel:

~~~text
ker(F):
  span{(-1,-1,1)}
~~~

Observed:

~~~text
(2,3)
~~~

Declared class:

~~~text
A:
  {(x,y,0): x,y in R}
~~~

Diagnosis and B1 both derive:

~~~text
DECLARED_CLASS_PREIMAGE:
  {(2,3,0)}

UNIQUE_WITHIN_DECLARED_CLASS:
  established

GLOBAL_INJECTIVITY:
  not established
~~~

Outside-class witness:

~~~text
(2,3,0)
and
(1,2,1)

both map to:
  (2,3)
~~~

Neither promotes the class-local uniqueness claim to global unique diagnosis.

Result:

~~~text
MATCH
~~~

## 6. R3 — required-interface dependency closure

Frozen candidates:

~~~text
s1:
  readout=0
  status=DEFINED_ZERO
  support=S1

s2:
  readout=0
  status=APPLICABLE_BUT_UNDEFINED
  support=S1
~~~

Main readout and support are non-discriminating.

The required Property-status sidecar is unavailable.

Diagnosis:

~~~text
required status interface:
  unavailable

task:
  DIAGNOSIS_TASK_BLOCKED
~~~

B1:

~~~text
required status dependency:
  unavailable

task:
  B1_TASK_BLOCKED
~~~

Neither coerces unavailable status to defined zero or ordinary incompatibility.

Result:

~~~text
MATCH
~~~

## 7. R4 — explicit probabilistic inference

Frozen:

~~~text
P(p1)=1/2
P(p2)=1/2

P(e|p1)=3/4
P(e|p2)=1/4
~~~

Both compute:

~~~text
P(e):
  1/2

P(p1|e):
  3/4

P(p2|e):
  1/4

posterior ranking:
  p1 > p2
~~~

Diagnosis:

~~~text
explicit probabilistic interface:
  valid

posterior:
  (3/4,1/4)

ranking:
  p1 > p2
~~~

B1:

~~~text
explicit Bayesian interface:
  valid

posterior:
  (3/4,1/4)

ranking:
  p1 > p2
~~~

Neither infers:

~~~text
p1 is the only compatible candidate
p1 is globally true
p1 is the proven cause
~~~

Result:

~~~text
MATCH
~~~

## 8. R5 — integrated conflict / threshold ambiguity / sidecar pressure

Q1 frozen conflicting evidence rules:

~~~text
same sensor/time/schema:
  S(t0)=0
  S(t0)=1

resolver:
  none
~~~

Both:

~~~text
Q1:
  conflict
~~~

Q2 frozen threshold alternatives:

~~~text
THRESHOLD-A:
  residual <= 0.2
  candidate passes

THRESHOLD-B:
  residual <= 0.1
  candidate fails

resolver:
  none
~~~

Both:

~~~text
Q2:
  unresolved / underdetermined
~~~

Q3 supplied neighboring sidecars:

~~~text
Measurement
Reconstruction
Classification
Comparison
Prediction
Simulation
Optimization
Audit
Tracking
Lineage
~~~

Both retain the substantive Diagnosis-compatible result only from the supplied Diagnosis relation.

No neighboring sidecar substitutes for Diagnosis.

Frozen precedence gives:

~~~text
run terminal:
  conflict
~~~

Both retain:

~~~text
Q2 unresolved state
Q3 substantive result
~~~

Both emit deterministic evaluation ledgers and rerun manifests.

Result:

~~~text
MATCH
~~~

## 9. Gain-axis execution

~~~text
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 EXACT_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN:
  BASELINE_MATCH

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN:
  BASELINE_MATCH

G4 EXPLICIT_PROBABILISTIC_INFERENCE_AND_SCOPE_GAIN:
  BASELINE_MATCH

G5 CONFLICT_UNDERDETERMINATION_AND_SIDECAR_BOUNDARY_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH
~~~

Overall:

~~~text
DIAGNOSIS_METHOD_GAIN_STATUS:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN
~~~

No claim-relevant DSD Diagnosis performance advantage was established over B1 on this frozen constructed strong workload under equal-information access.

## 10. Execution of the 82 frozen checks

### A — immutable fairness

~~~text
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
~~~

### B — R1 versioned registries

~~~text
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
~~~

### C — R2 exact preimage / declared class

~~~text
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
~~~

### D — R3 dependency closure

~~~text
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
~~~

### E — R4 probabilistic inference

~~~text
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
~~~

### F — R5 integrated pressure

~~~text
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
~~~

### G — comparative conclusion

~~~text
G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS
G8 PASS

G: 8/8
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
~~~

## 11. Counter update

~~~text
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

## 12. Interpretation lock

The result means:

~~~text
A materially strong non-DSD diagnostic inference engine matched
the claim-relevant Diagnosis Protocol v0.1 outputs on the frozen
constructed strong workload under equal-information access.
~~~

It does not mean:

~~~text
B1 is universally strongest possible
Diagnosis Protocol failure
Diagnosis method deletion
Diagnosis should merge into another method
Diagnosis should be absorbed
permanent redundancy
future DSD-specific gain is impossible
external validity
independent replication
~~~

Required guards:

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 13. Maximum-supported claim

Supported:

~~~text
Within the frozen DIAG-CH-005 constructed comparator class,
B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE matched Diagnosis Protocol
v0.1 on versioned registry semantics, exact linear preimage/kernel
analysis, declared-class uniqueness, required-interface dependency
closure, explicit probabilistic inference, conflict/threshold
ambiguity handling, neighboring-sidecar boundaries, bounded claims,
and deterministic replay metadata.

All seven frozen gain axes were BASELINE_MATCH.
~~~

Not established:

~~~text
universal baseline optimality
method redundancy
external applicability
independent validation
independent replication
method superiority
~~~

## 14. Next

Prospectively precommit and execute DIAG-CH-006 deterministic same-project retrace.

The retrace must reconstruct the frozen claim-relevant DIAG-CH-001~005 evidence from repository artifacts, compare independently reconstructed outputs against recorded outputs, preserve every mismatch, prohibit post-comparison correction, and keep:

~~~text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~
