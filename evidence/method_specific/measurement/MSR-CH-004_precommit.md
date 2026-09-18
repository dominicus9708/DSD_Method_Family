# MSR-CH-004 Precommit — Competent Non-DSD Baseline Comparison

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-19**  
Case ID: `MSR-CH-004`  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
MEASUREMENT_PROTOCOL_COMMIT:
  70af7c3ddc618be34d0ff76fcc1ce63c895fc950

MEASUREMENT_PROTOCOL_BLOB:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331

MEASUREMENT_PROTOCOL_VERSION:
  v0.1
```

No DSD protocol revision is allowed in response to the baseline result.

## 2. Baseline identity

```text
BASELINE_ID:
  B0_GENERIC_DISTINGUISHABILITY_LEDGER

BASELINE_CLASS:
  competent_non_DSD_constructed_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

The baseline is intentionally competent rather than weak.

It receives the same claim-relevant task information as DSD Measurement and is allowed to use ordinary set comparison, explicit status flags, decision tables, and tuple signatures.

## 3. B0 operation

B0 performs the following generic procedure:

```text
B0-1 lock task alternatives, required pairs, scope, and supplied resolution rule
B0-2 retain supplied applicability/status flags without coercing them
B0-3 apply supplied decision rule to supplied outcome records
B0-4 compare required pairs for decision-class overlap/disjointness
B0-5 evaluate supplied joint tuple/signature policy when declared
B0-6 retain supplied collision/injectivity/reconstruction sidecars
B0-7 preserve explicit missing prerequisite/bridge as BLOCKED
B0-8 preserve explicit scope mismatch as OUT_OF_SCOPE
B0-9 preserve competing admissible mappings without precedence as UNDERDETERMINED
B0-10 classify plan coverage as sufficient / partial / insufficient / blocked /
      out-of-scope / underdetermined
B0-11 report only plan-selection adequacy; do not fabricate an observed result
```

B0 does not invoke Formation, Property, Static Aggregation, Dynamics, or any DSD shared-core rule as a theory.

It simply consumes the supplied records at face value.

## 4. Baseline output vocabulary

Candidate output vocabulary:

```text
B0_FULLY_DISCRIMINATING
B0_PARTIALLY_DISCRIMINATING
B0_NONDISCRIMINATING
B0_BLOCKED
B0_INAPPLICABLE
B0_OUT_OF_SCOPE
B0_UNDERDETERMINED
```

Plan output vocabulary:

```text
B0_PLAN_SUFFICIENT
B0_PLAN_PARTIAL
B0_PLAN_INSUFFICIENT
B0_PLAN_BLOCKED
B0_PLAN_OUT_OF_SCOPE
B0_PLAN_UNDERDETERMINED
```

Comparison mapping is frozen before execution:

```text
B0_FULLY_DISCRIMINATING
  <-> MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION

B0_PARTIALLY_DISCRIMINATING
  <-> MEASUREMENT_PARTIALLY_DISCRIMINATES

B0_NONDISCRIMINATING
  <-> MEASUREMENT_NONDISCRIMINATING

B0_BLOCKED
  <-> MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE

B0_INAPPLICABLE
  <-> MEASUREMENT_INAPPLICABLE

B0_OUT_OF_SCOPE
  <-> MEASUREMENT_OUT_OF_SCOPE

B0_UNDERDETERMINED
  <-> MEASUREMENT_UNDERDETERMINED
```

and:

```text
B0_PLAN_SUFFICIENT      <-> MEASUREMENT_PLAN_SUFFICIENT
B0_PLAN_PARTIAL         <-> MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
B0_PLAN_INSUFFICIENT    <-> MEASUREMENT_PLAN_INSUFFICIENT
B0_PLAN_BLOCKED         <-> MEASUREMENT_PLAN_BLOCKED
B0_PLAN_OUT_OF_SCOPE    <-> MEASUREMENT_PLAN_OUT_OF_SCOPE
B0_PLAN_UNDERDETERMINED <-> MEASUREMENT_PLAN_UNDERDETERMINED
```

Vocabulary differences alone do not count as DSD gain.

## 5. Equal-information rule

For every fixture, DSD Measurement and B0 receive the same:

```text
alternative identities
required distinction set
task scope
candidate identities
candidate domains/applicability/statuses
raw or symbolic outcome records
outcome-map or bridge records
bridge provenance/absence flags
decision rule / threshold
joint measurement policy
aggregate collision sidecar
injectivity/reconstruction sidecar
regime/scope records
observed-result availability flag
```

Neither side receives hidden favorable information.

## 6. Frozen fixtures

### Q1 — joint sufficiency + defined zero + aggregate collision

Use the claim-relevant fixture semantics of MSR-CH-001:

```text
ALTERNATIVES: H_A,H_B,H_C
REQUIRED PAIRS: AB, AC, BC

m_X:
  H_A -> 0.0 / defined zero / LOW
  H_B -> 0.8 / HIGH
  H_C -> 0.8 / HIGH

m_Y:
  H_A -> 0.2 / LOW
  H_B -> 0.2 / LOW
  H_C -> 0.9 / HIGH

joint:
  H_A -> (LOW,LOW)
  H_B -> (HIGH,LOW)
  H_C -> (HIGH,HIGH)

m_AGG:
  H_A support {+1,-1} -> aggregate 0
  H_B support {0}     -> aggregate 0
  H_C support {+1}    -> aggregate 1

aggregate map:
  noninjective on H_A/H_B
  full support reconstruction unavailable

observed experimental result:
  absent
```

Frozen expected comparison:

```text
DSD:
  m_X partial
  m_Y partial
  m_AGG partial
  joint plan sufficient
  defined zero preserved
  H_A/H_B aggregate collision preserved
  full support reconstruction not claimed
  observed result not fabricated

B0:
  m_X B0_PARTIALLY_DISCRIMINATING
  m_Y B0_PARTIALLY_DISCRIMINATING
  m_AGG B0_PARTIALLY_DISCRIMINATING
  joint plan B0_PLAN_SUFFICIENT
  numeric zero retained as supplied
  H_A/H_B collision sidecar retained
  reconstruction-unavailable sidecar retained
  observed result not fabricated
```

### Q2 — complete information but nondiscriminating

```text
ALTERNATIVES: D,E
REQUIRED PAIR: D-E

m_same:
  D -> SAME / defined
  E -> SAME / defined

all required assessment information:
  present
```

Expected:

```text
DSD candidate: MEASUREMENT_NONDISCRIMINATING
DSD plan: MEASUREMENT_PLAN_INSUFFICIENT

B0 candidate: B0_NONDISCRIMINATING
B0 plan: B0_PLAN_INSUFFICIENT
```

### Q3 — blocked + inapplicable

```text
ALTERNATIVES: F,G
REQUIRED PAIR: F-G

m_need_bridge:
  applicable
  source records supplied
  required claim bridge explicitly absent

m_inapp:
  declared domain K
  task object class L
```

Expected:

```text
DSD:
  m_need_bridge -> BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
  m_inapp -> INAPPLICABLE
  plan -> BLOCKED

B0:
  m_need_bridge -> B0_BLOCKED
  m_inapp -> B0_INAPPLICABLE
  plan -> B0_PLAN_BLOCKED
```

### Q4 — competing admissible bridges

```text
ALTERNATIVES: U,V
REQUIRED PAIR: U-V

B1:
  U -> LOW
  V -> HIGH

B2:
  U -> LOW
  V -> LOW

B1 and B2:
  both fully supplied
  both simultaneously admissible

precedence rule:
  absent
```

Expected:

```text
DSD:
  candidate -> UNDERDETERMINED
  plan -> UNDERDETERMINED

B0:
  candidate -> B0_UNDERDETERMINED
  plan -> B0_PLAN_UNDERDETERMINED
```

### Q5 — explicit scope mismatch

```text
ALTERNATIVES: P,Q
REQUIRED PAIR: P-Q
TASK SCOPE: R2

candidate m_R1:
  declared scope R1 only
  R1 map complete
  R2 extension not declared
```

Expected:

```text
DSD:
  candidate -> OUT_OF_SCOPE
  plan -> OUT_OF_SCOPE

B0:
  candidate -> B0_OUT_OF_SCOPE
  plan -> B0_PLAN_OUT_OF_SCOPE
```

## 7. Gain axes

The following gain axes are frozen before execution.

```text
G1 discrimination-classification advantage
G2 typed-status preservation advantage
G3 joint-plan sufficiency advantage
G4 information-loss / reconstruction-limit advantage
G5 negative-terminal semantic advantage
G6 selection-versus-observed-result discipline advantage
```

Allowed axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall method-gain rule:

```text
if all claim-relevant outputs match:
  MEASUREMENT_METHOD_GAIN_STATUS = NO_GAIN

if one or more precommitted claim-relevant axes show a DSD advantage:
  MEASUREMENT_METHOD_GAIN_STATUS = GAIN_ESTABLISHED

otherwise:
  MEASUREMENT_METHOD_GAIN_STATUS = NOT_ASSESSED
```

A difference in terminology or formatting is not a gain.

## 8. Frozen scoring — 60 checks

### A. Fairness and immutability — 10

```text
A1 DSD protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 output-vocabulary mapping fixed
A4 Q1-Q5 fixed before execution
A5 equal-information rule respected
A6 B0 not denied DSD-visible claim-relevant information
A7 DSD not given hidden favorable information
A8 observed-result absence identical
A9 no post-hoc gain axis added
A10 no external application counted
```

### B. Q1 positive/joint/loss case — 14

```text
B1 DSD m_X partial
B2 B0 m_X equivalent partial
B3 DSD m_Y partial
B4 B0 m_Y equivalent partial
B5 DSD joint sufficient
B6 B0 joint sufficient
B7 DSD defined-zero preserved
B8 B0 supplied zero preserved
B9 DSD aggregate collision preserved
B10 B0 aggregate collision preserved
B11 DSD reconstruction-unavailable preserved
B12 B0 reconstruction-unavailable preserved
B13 DSD no observed result fabricated
B14 B0 no observed result fabricated
```

### C. Q2 insufficiency — 8

```text
C1 DSD equal defined outcomes retained
C2 B0 equal defined outcomes retained
C3 DSD pair nondiscriminating
C4 B0 pair nondiscriminating
C5 DSD candidate nondiscriminating
C6 B0 candidate equivalent
C7 DSD plan insufficient
C8 B0 plan insufficient
```

### D. Q3 blockage/inapplicability — 10

```text
D1 DSD missing bridge remains explicit
D2 B0 missing bridge remains explicit
D3 DSD m_need_bridge blocked
D4 B0 m_need_bridge blocked
D5 DSD m_inapp inapplicable
D6 B0 m_inapp inapplicable
D7 neither converts missing bridge to negative result
D8 neither converts inapplicability to negative result
D9 DSD plan blocked
D10 B0 plan blocked
```

### E. Q4 underdetermination — 8

```text
E1 both supplied bridges preserved by DSD
E2 both supplied bridges preserved by B0
E3 DSD B1 path discriminating
E4 B0 B1 path discriminating
E5 DSD B2 path nondiscriminating
E6 B0 B2 path nondiscriminating
E7 DSD plan underdetermined
E8 B0 plan underdetermined
```

### F. Q5 out-of-scope — 6

```text
F1 DSD R1/R2 scope mismatch retained
F2 B0 R1/R2 scope mismatch retained
F3 DSD candidate out-of-scope
F4 B0 candidate out-of-scope
F5 DSD plan out-of-scope
F6 B0 plan out-of-scope
```

### G. Gain conclusion — 4

```text
G1 six gain axes scored from frozen evidence only
G2 terminology difference not counted as gain
G3 NO_GAIN preserved if all claim-relevant outputs match
G4 no method-merger/deletion conclusion inferred from NO_GAIN
```

```text
TOTAL_REQUIRED_CHECKS: 60
PASS_THRESHOLD: 60/60
PARTIAL_PASS_ALLOWED: no
```

Any mismatch must remain visible.

## 9. Allowed counter changes on 60/60 PASS

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 3 -> 4
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 3 -> 4
BASELINE_MEASUREMENT_CASES: 0 -> 1
```

If all six gain axes are `BASELINE_MATCH`:

```text
NO_GAIN_MEASUREMENT_CASES: 0 -> 1
MEASUREMENT_METHOD_GAIN_STATUS: NO_GAIN
```

Unchanged:

```text
POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 1
STRONGEST_REASONABLE_BASELINE_MEASUREMENT: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no unless contradiction found
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction found
```

`NO_GAIN` is not evidence for deleting, merging, or absorbing Measurement.
