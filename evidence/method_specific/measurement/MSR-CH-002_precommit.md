# MSR-CH-002 Precommit — Negative-Terminal Coverage Challenge

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-19**  
Case ID: `MSR-CH-002`  
Case class: `negative_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparators

```text
PROTOCOL_PATH: methods/11_measurement/PROTOCOL_v0.1.md
PROTOCOL_COMMIT: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
PROTOCOL_BLOB: bc24a5e72adaf4a1b1e64203bd14b3e781810331

BOUNDARY_AMENDMENT_COMMIT: 7f09baa7e2bb2701b4f01471abbbd443d226a78a
BOUNDARY_AMENDMENT_BLOB: 1ac7933fc19d95e9070432de99deb5a0fd1d382c
```

The protocol is immutable for this challenge.

## 2. Purpose

Exercise every remaining plan-level terminal not covered by MSR-CH-001 and preserve the distinctions among them:

```text
N1 -> MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
N2 -> MEASUREMENT_PLAN_INSUFFICIENT
N3 -> MEASUREMENT_PLAN_BLOCKED
N4 -> MEASUREMENT_PLAN_OUT_OF_SCOPE
N5 -> MEASUREMENT_PLAN_UNDERDETERMINED
```

Together with MSR-CH-001:

```text
MEASUREMENT_PLAN_SUFFICIENT
```

this will directly exercise all six plan terminal statuses if and only if all frozen subcases execute as specified.

The challenge also attempts direct candidate-level coverage of:

```text
MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
MEASUREMENT_NONDISCRIMINATING
MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
MEASUREMENT_INAPPLICABLE
MEASUREMENT_OUT_OF_SCOPE
MEASUREMENT_UNDERDETERMINED
```

MSR-CH-001 already covered `MEASUREMENT_PARTIALLY_DISCRIMINATES`.

A conformant negative terminal counts as successful protocol execution, not as a positive substantive measurement result.

## 3. N1 — partially sufficient plan

Task:

```text
TASK_ID: MSR-CH-002-N1
ALTERNATIVES: {A,B,C}
REQUIRED_DISTINCTIONS:
  A-B
  A-C
  B-C
RESOLUTION: exact labels
TASK_SCOPE: static constructed discrimination
```

Candidate `m_AB`:

```text
DECLARED_CANDIDATE_SCOPE:
  required pair A-B only

OUTCOMES:
  A -> RED
  B -> BLUE

STATUS:
  both defined

EXPECTED:
  A-B -> PAIRWISE_DISCRIMINATING

CANDIDATE_STATUS:
  MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
```

No candidate is supplied for A-C or B-C.

All information needed to judge the supplied plan is present. The uncovered pairs are not blocked by missing assessment data; they are simply not discriminated by the declared plan.

Expected terminal:

```text
MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
```

Forbidden relabeling:

```text
PARTIALLY_SUFFICIENT != SUFFICIENT
PARTIALLY_SUFFICIENT != BLOCKED
```

## 4. N2 — insufficient plan

Task:

```text
TASK_ID: MSR-CH-002-N2
ALTERNATIVES: {D,E}
REQUIRED_DISTINCTIONS: D-E
RESOLUTION: exact labels
```

Candidate `m_same`:

```text
OUTCOMES:
  D -> SAME
  E -> SAME

STATUS:
  both defined and applicable

EXPECTED:
  D-E -> PAIRWISE_NONDISCRIMINATING

CANDIDATE_STATUS:
  MEASUREMENT_NONDISCRIMINATING
```

All outcome maps and semantics are present.

Expected terminal:

```text
MEASUREMENT_PLAN_INSUFFICIENT
```

Forbidden relabeling:

```text
NONDISCRIMINATING != BLOCKED
DEFINED_EQUAL_READOUT != MISSING_DATA
INSUFFICIENT != METHOD_FAILURE
```

## 5. N3 — blocked plan with separate inapplicable candidate

Task:

```text
TASK_ID: MSR-CH-002-N3
ALTERNATIVES: {F,G}
REQUIRED_DISTINCTIONS: F-G
RESOLUTION: exact supplied outcome classes
```

Candidate `m_need_bridge`:

```text
IDENTITY/TYPE/DOMAIN: supplied and in-scope
APPLICABILITY: applicable
OUTCOME VALUE RECORDS: source values are supplied
MEASUREMENT_TO_ALTERNATIVE_DECISION_BRIDGE:
  explicitly absent and required by the task

EXPECTED CANDIDATE STATUS:
  MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
```

Candidate `m_inapp`:

```text
DECLARED_DOMAIN:
  object class K only

SUPPLIED TASK OBJECT CLASS:
  object class L

EXPECTED CANDIDATE STATUS:
  MEASUREMENT_INAPPLICABLE
```

The plan has no other candidate.

Expected terminal:

```text
MEASUREMENT_PLAN_BLOCKED
```

Reason:

```text
the only in-scope potentially usable candidate requires a missing claim-relevant bridge;
the other candidate is explicitly inapplicable.
```

Forbidden relabeling:

```text
MISSING_REQUIRED_BRIDGE != NEGATIVE_RESULT
INAPPLICABLE != NEGATIVE_RESULT
BLOCKED != INSUFFICIENT
BLOCKED != UNDERDETERMINED
```

## 6. N4 — out-of-scope plan

Task:

```text
TASK_ID: MSR-CH-002-N4
ALTERNATIVES: {P,Q}
REQUIRED_DISTINCTIONS: P-Q
TASK_SCOPE:
  regime R2 only
```

Only supplied candidate `m_R1`:

```text
MEASUREMENT_ID: m_R1
CANDIDATE_TASK_SCOPE: regime R1 only
OUTCOME MAP: fully specified for R1
STATUS: defined in R1
NO EXTENSION TO R2 IS DECLARED
```

The candidate relation requested by the task lies outside the frozen candidate scope. No missing datum inside R2 is being inferred; the candidate is explicitly not a candidate for R2.

Expected candidate status:

```text
MEASUREMENT_OUT_OF_SCOPE
```

Expected terminal:

```text
MEASUREMENT_PLAN_OUT_OF_SCOPE
```

Forbidden relabeling:

```text
OUT_OF_SCOPE != INAPPLICABLE
OUT_OF_SCOPE != BLOCKED
OUT_OF_SCOPE != INSUFFICIENT
NO_DECLARED_SCOPE_EXTENSION != MISSING_NEGATIVE_RESULT
```

## 7. N5 — underdetermined plan

Task:

```text
TASK_ID: MSR-CH-002-N5
ALTERNATIVES: {U,V}
REQUIRED_DISTINCTIONS: U-V
RESOLUTION: exact decision labels
```

Candidate `m_amb` has one raw source record but two claim-relevant bridge versions explicitly retained as simultaneously admissible by the frozen task. No precedence rule is supplied.

Bridge `B1`:

```text
U -> LOW
V -> HIGH
=> PAIRWISE_DISCRIMINATING
```

Bridge `B2`:

```text
U -> LOW
V -> LOW
=> PAIRWISE_NONDISCRIMINATING
```

Both bridges are fully supplied. Nothing is missing. The ambiguity is therefore not blockage.

Expected candidate status:

```text
MEASUREMENT_UNDERDETERMINED
```

Expected terminal:

```text
MEASUREMENT_PLAN_UNDERDETERMINED
```

Forbidden relabeling:

```text
COMPETING_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
UNDERDETERMINED != BLOCKED
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC
```

## 8. Cross-subcase guards

The execution must preserve:

```text
PARTIALLY_SUFFICIENT != SUFFICIENT
INSUFFICIENT != BLOCKED
BLOCKED != UNDERDETERMINED
OUT_OF_SCOPE != INAPPLICABLE
INAPPLICABLE != NEGATIVE_RESULT
NONDISCRIMINATING != MISSING_DATA
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC

CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
CONFORMANT_NEGATIVE_TERMINAL != METHOD_DELETION_PROOF
CONFORMANT_NEGATIVE_TERMINAL != METHOD_MERGER_PROOF
```

No subcase supplies an observed experimental result or true alternative.

## 9. Validity-gate policy

Each subcase must satisfy all applicable G1-G14 gates.

Allowed non-PASS gate value:

```text
NOT_APPLICABLE_WITH_REASON
```

where a gate is structurally irrelevant to that subcase.

A negative terminal is not itself a gate failure.

## 10. Frozen scoring — 60 checks

### A. Immutability / common scope — 8

```text
A1 protocol commit/blob fixed
A2 amendment commit/blob fixed
A3 five subcases fixed before execution
A4 no external application
A5 no observed experimental result
A6 no true alternative supplied
A7 no protocol edit after precommit
A8 method gain remains NOT_ASSESSED
```

### B. N1 partial sufficiency — 10

```text
B1 task/alternatives/pairs fixed
B2 m_AB scope limited to A-B
B3 A/B outcomes defined
B4 A-B discriminating
B5 candidate status = DISCRIMINATES_AT_DECLARED_RESOLUTION
B6 A-C not falsely covered
B7 B-C not falsely covered
B8 terminal = PLAN_PARTIALLY_SUFFICIENT
B9 not relabeled BLOCKED
B10 conformance preserved
```

### C. N2 insufficiency — 10

```text
C1 task/pair fixed
C2 D/E outcomes both defined
C3 D/E outcomes equal
C4 pairwise = NONDISCRIMINATING
C5 candidate status = NONDISCRIMINATING
C6 all required assessment information present
C7 terminal = PLAN_INSUFFICIENT
C8 not relabeled BLOCKED
C9 insufficient not called method failure
C10 conformance preserved
```

### D. N3 blockage / inapplicability — 12

```text
D1 task/pair fixed
D2 m_need_bridge applicable
D3 required bridge explicitly absent
D4 missing bridge not converted to negative result
D5 m_need_bridge candidate status = BLOCKED
D6 m_inapp domain K fixed
D7 task object class L fixed
D8 m_inapp candidate status = INAPPLICABLE
D9 inapplicable not converted to negative result
D10 terminal = PLAN_BLOCKED
D11 terminal not relabeled INSUFFICIENT/UNDERDETERMINED
D12 conformance preserved
```

### E. N4 out-of-scope — 10

```text
E1 task scope R2 fixed
E2 candidate scope R1 fixed
E3 R1 map complete
E4 no R2 scope extension declared
E5 candidate status = OUT_OF_SCOPE
E6 out-of-scope not relabeled INAPPLICABLE
E7 terminal = PLAN_OUT_OF_SCOPE
E8 not relabeled BLOCKED
E9 no target value fabricated for R2
E10 conformance preserved
```

### F. N5 underdetermination — 10

```text
F1 task/pair fixed
F2 B1 fully supplied
F3 B2 fully supplied
F4 B1 yields discriminating
F5 B2 yields nondiscriminating
F6 no precedence rule supplied
F7 candidate status = UNDERDETERMINED
F8 terminal = PLAN_UNDERDETERMINED
F9 not relabeled BLOCKED / no post-hoc bridge choice
F10 conformance preserved
```

```text
TOTAL_REQUIRED_CHECKS: 60
PASS_THRESHOLD: 60/60
PARTIAL_PASS_ALLOWED: no
```

Any mismatch must be preserved. The precommit may not be edited to rescue the case.

## 11. Allowed counter changes on 60/60 PASS

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 1 -> 2
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 1 -> 2
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 0 -> 1
```

Here `SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS` means the frozen protocol executed conformantly against the precommitted challenge. It does not mean the measurement plan had a positive terminal.

If all five terminals are produced exactly, record:

```text
PLAN_TERMINAL_COVERAGE:
  SUFFICIENT: covered by MSR-CH-001
  PARTIALLY_SUFFICIENT: covered by MSR-CH-002-N1
  INSUFFICIENT: covered by MSR-CH-002-N2
  BLOCKED: covered by MSR-CH-002-N3
  OUT_OF_SCOPE: covered by MSR-CH-002-N4
  UNDERDETERMINED: covered by MSR-CH-002-N5
  ALL_SIX_DIRECTLY_EXERCISED: yes
```

Unchanged:

```text
POSITIVE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 0
BASELINE_MEASUREMENT_CASES: 0
NO_GAIN_MEASUREMENT_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no unless contradiction found
SHARED_CORE_REOPEN_REQUIRED: no unless contradiction found
```
