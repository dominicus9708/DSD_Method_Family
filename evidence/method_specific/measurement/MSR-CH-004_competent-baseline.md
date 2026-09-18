# MSR-CH-004 — Competent Non-DSD Baseline Comparison Result

Status: **EXECUTED — 60/60 PASS / NO_GAIN**  
Date: **2026-09-19**  
Case ID: `MSR-CH-004`  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
MEASUREMENT_PROTOCOL_COMMIT:
  70af7c3ddc618be34d0ff76fcc1ce63c895fc950

MEASUREMENT_PROTOCOL_BLOB:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331

PRECOMMIT_COMMIT:
  5c3d2c3dbe941d324d8ff1a44990044e2c228a54

PRECOMMIT_BLOB:
  1a24d6d80a44a0b56b5cb4af684a75c599010ffc

BASELINE_ID:
  B0_GENERIC_DISTINGUISHABILITY_LEDGER
```

No protocol, baseline operation, fixture, output mapping, gain axis, or scoring rule was changed after precommit.

## 2. Equal-information check

Both DSD Measurement and B0 received the same claim-relevant records for every fixture:

```text
alternatives
required distinction set
task scope
candidate identities
candidate domains / applicability / statuses
outcome records
bridge records and explicit absence flags
decision rules
joint policy
collision sidecars
injectivity / reconstruction sidecars
regime / scope records
observed-result availability
```

No DSD-only hidden input was used.

No baseline-visible claim-relevant input was withheld.

```text
EQUAL_INFORMATION_ACCESS: yes
DSD_HIDDEN_ADVANTAGE_INPUTS: 0
BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS: 0
```

## 3. Q1 — joint sufficiency, defined zero, aggregate collision

### DSD Measurement

```text
m_X:
  H_A -> LOW
  H_B -> HIGH
  H_C -> HIGH
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m_Y:
  H_A -> LOW
  H_B -> LOW
  H_C -> HIGH
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m_AGG:
  H_A aggregate 0
  H_B aggregate 0
  H_C aggregate 1
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

joint {m_X,m_Y}:
  H_A -> (LOW,LOW)
  H_B -> (HIGH,LOW)
  H_C -> (HIGH,HIGH)
  -> MEASUREMENT_PLAN_SUFFICIENT
```

Preserved by DSD:

```text
H_A under m_X:
  DEFINED_ZERO

aggregate(H_A) = aggregate(H_B) = 0
support(H_A) != support(H_B)

aggregate map:
  noninjective on H_A/H_B

full support reconstruction:
  unavailable

observed experimental result:
  absent
```

### B0

B0 applied the same supplied LOW/HIGH rules and the same ordered joint tuple rule.

```text
m_X:
  H_A -> LOW
  H_B -> HIGH
  H_C -> HIGH
  -> B0_PARTIALLY_DISCRIMINATING

m_Y:
  H_A -> LOW
  H_B -> LOW
  H_C -> HIGH
  -> B0_PARTIALLY_DISCRIMINATING

m_AGG:
  H_A -> LOW
  H_B -> LOW
  H_C -> HIGH
  -> B0_PARTIALLY_DISCRIMINATING

joint {m_X,m_Y}:
  H_A -> (LOW,LOW)
  H_B -> (HIGH,LOW)
  H_C -> (HIGH,HIGH)
  -> B0_PLAN_SUFFICIENT
```

B0 retained the supplied numerical zero as a defined supplied value, retained the H_A/H_B collision sidecar, retained the noninjectivity/reconstruction-unavailable sidecar, and did not fabricate an observed result.

Comparison:

```text
Q1_CLAIM_RELEVANT_MATCH: yes
```

## 4. Q2 — complete information but nondiscriminating

Frozen values:

```text
m_same(D) = SAME
m_same(E) = SAME
both defined
all assessment information present
```

DSD:

```text
D-E -> PAIRWISE_NONDISCRIMINATING
candidate -> MEASUREMENT_NONDISCRIMINATING
plan -> MEASUREMENT_PLAN_INSUFFICIENT
```

B0:

```text
D-E -> nondiscriminating
candidate -> B0_NONDISCRIMINATING
plan -> B0_PLAN_INSUFFICIENT
```

Neither system converted equal defined readouts into missing data or blockage.

```text
Q2_CLAIM_RELEVANT_MATCH: yes
```

## 5. Q3 — blocked + inapplicable

Frozen state:

```text
m_need_bridge:
  applicable
  source records present
  required claim bridge explicitly absent

m_inapp:
  declared domain K
  task object class L
```

DSD:

```text
m_need_bridge
  -> MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE

m_inapp
  -> MEASUREMENT_INAPPLICABLE

plan
  -> MEASUREMENT_PLAN_BLOCKED
```

B0:

```text
m_need_bridge
  -> B0_BLOCKED

m_inapp
  -> B0_INAPPLICABLE

plan
  -> B0_PLAN_BLOCKED
```

Both preserved the explicit missing bridge and the explicit domain mismatch rather than turning either into a negative observation.

```text
Q3_CLAIM_RELEVANT_MATCH: yes
```

## 6. Q4 — competing admissible bridges

Frozen bridges:

```text
B1:
  U -> LOW
  V -> HIGH
  -> discriminating

B2:
  U -> LOW
  V -> LOW
  -> nondiscriminating

both fully supplied
both simultaneously admissible
no precedence rule
```

DSD:

```text
candidate -> MEASUREMENT_UNDERDETERMINED
plan -> MEASUREMENT_PLAN_UNDERDETERMINED
```

B0:

```text
candidate -> B0_UNDERDETERMINED
plan -> B0_PLAN_UNDERDETERMINED
```

Neither side selected B1 or B2 post hoc.

```text
Q4_CLAIM_RELEVANT_MATCH: yes
```

## 7. Q5 — explicit scope mismatch

Frozen state:

```text
task scope: R2
candidate scope: R1 only
R1 map complete
R2 extension absent
```

DSD:

```text
candidate -> MEASUREMENT_OUT_OF_SCOPE
plan -> MEASUREMENT_PLAN_OUT_OF_SCOPE
```

B0:

```text
candidate -> B0_OUT_OF_SCOPE
plan -> B0_PLAN_OUT_OF_SCOPE
```

Neither side fabricated an R2 outcome.

```text
Q5_CLAIM_RELEVANT_MATCH: yes
```

## 8. Gain-axis result

The six precommitted gain axes were scored only from the frozen fixtures.

```text
G1 discrimination-classification advantage:
  BASELINE_MATCH

G2 typed-status preservation advantage:
  BASELINE_MATCH

G3 joint-plan sufficiency advantage:
  BASELINE_MATCH

G4 information-loss / reconstruction-limit advantage:
  BASELINE_MATCH

G5 negative-terminal semantic advantage:
  BASELINE_MATCH

G6 selection-versus-observed-result discipline advantage:
  BASELINE_MATCH
```

Therefore:

```text
MEASUREMENT_METHOD_GAIN_STATUS:
  NO_GAIN
```

The baseline reproduced the claim-relevant outputs because it was supplied the same typed statuses, bridges, thresholds, joint policy, and sidecars and used a competent generic distinguishability ledger.

No special superiority claim is supported by this fixture.

## 9. What NO_GAIN means here

```text
NO_GAIN
  means:
    no measured advantage over B0 was established
    for these frozen constructed tasks under equal information access
```

It does not mean:

```text
Measurement protocol failed
Measurement should be deleted
Measurement is identical to every baseline
Measurement must merge into Comparison or another DSD method
Measurement has no organizational value
Measurement cannot show gain on a different precommitted task
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```

## 10. Frozen scoring

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

### B. Q1 positive/joint/loss case

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

### C. Q2 insufficiency

```text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS

C: 8/8
```

### D. Q3 blockage/inapplicability

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

### E. Q4 underdetermination

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS

E: 8/8
```

### F. Q5 out-of-scope

```text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS

F: 6/6
```

### G. Gain conclusion

```text
G1 PASS
G2 PASS
G3 PASS
G4 PASS

G: 4/4
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 60
PASSED: 60
FAILED: 0
TOTAL: 60/60 PASS
```

## 11. Conformance and protocol pressure

```text
MSR-CH-004_CONFORMANCE: CONFORMANT
MEASUREMENT_METHOD_GAIN_STATUS: NO_GAIN

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The result does not expose a contradiction in Protocol v0.1.

It instead shows that the current constructed tasks are also solvable by a competent generic distinguishability ledger when the same structured information is supplied.

## 12. Counter update authorized by precommit

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 3 -> 4
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 3 -> 4
BASELINE_MEASUREMENT_CASES: 0 -> 1
NO_GAIN_MEASUREMENT_CASES: 0 -> 1

POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 1

STRONGEST_REASONABLE_BASELINE_MEASUREMENT: not established
REPRODUCIBILITY_CASES: 0

EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established

MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 13. Maximum supported claim

MSR-CH-004 establishes only:

```text
Under Q1-Q5 and equal information access,
the competent B0 generic distinguishability ledger reproduced
the claim-relevant Measurement outputs.
No DSD-specific gain was established in this comparison.
```

It does not establish external adequacy, independent validation, general inferiority/superiority, or permanent redundancy.

## 14. Next

Proceed to a separately precommitted strongest-reasonable baseline challenge.

The stronger baseline should be allowed to integrate status-aware decision tables, joint-plan search, information-loss sidecars, scope/version control, ambiguity handling, and bounded claim reporting in one non-DSD evaluator.

Only after that comparison should same-project deterministic retrace be attempted.
