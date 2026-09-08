# DES-CH-006 — Broader Typed Baseline Comparison

Status: **PASS — broader strongest-reasonable-baseline comparison completed under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **baseline_comparison**  
Precommit: `DES-CH-006_precommit.md`, commit `3a44350`

## 1. Evidence claim / 증거 주장

This case executes the broader baseline comparison frozen in `DES-CH-006_precommit.md`.

The comparator `B1_TYPED_ADMISSIBILITY_TABLE` was intentionally strong: it preserved the same structural/property distinctions, evaluated the same 15-candidate exhaustive universe, recorded full hard-constraint failure sets, and had an explicit no-unique-target outcome.

The comparison therefore gave the baseline a genuine opportunity to match DSD rather than being designed as a Boolean-only strawman.

No baseline weakening, candidate change, target-resolution change, or gain-criterion revision occurred after the precommit.

---

## 2. Frozen task recap / 동결 과업 요약

```text
DESIGN_TASK_ID: DES-TASK-006
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
CANDIDATE_COVERAGE: exhaustive
CANDIDATES: A1-A15

H1 q_primary is ADMITTED
H2 q_reserve is ADMITTED
H3 readiness(q_reserve) is DEFINED_ZERO or DEFINED_NONZERO
H4 authorization(q_primary) is DEFINED_NONZERO

TARGET_RESOLUTION:
  exact q_primary admission
  exact q_reserve admission
  exact readiness status/value class
  exact authorization status/value class
```

Subcases:

```text
Case S: DESIGN_SPACE
Case U: UNIQUE_TARGET
```

---

## 3. Baseline B1 execution / 기준선 실행

Baseline:

```text
B1_TYPED_ADMISSIBILITY_TABLE
```

B1 kept separate structural columns and typed property-state columns and applied H1-H4 independently.

| Candidate | q_primary | q_reserve | readiness | authorization | Failed constraints | B1 result |
|---|---|---|---|---|---|---|
| A1 | PRESENT | PRESENT | DEFINED_ZERO | DEFINED_NONZERO | none | admissible |
| A2 | PRESENT | PRESENT | DEFINED_NONZERO | DEFINED_NONZERO | none | admissible |
| A3 | PRESENT | ABSENT | NOT_APPLICABLE | DEFINED_NONZERO | H2,H3 | rejected |
| A4 | PRESENT | PRESENT | APPLICABLE_UNSET | DEFINED_NONZERO | H3 | rejected |
| A5 | PRESENT | PRESENT | PREREQUISITE_NOT_MET | DEFINED_NONZERO | H3 | rejected |
| A6 | PRESENT | PRESENT | NOT_APPLICABLE | DEFINED_NONZERO | H3 | rejected |
| A7 | PRESENT | PRESENT | DEFINED_ZERO | DEFINED_ZERO | H4 | rejected |
| A8 | PRESENT | PRESENT | DEFINED_NONZERO | APPLICABLE_UNSET | H4 | rejected |
| A9 | PRESENT | PRESENT | DEFINED_NONZERO | PREREQUISITE_NOT_MET | H4 | rejected |
| A10 | ABSENT | PRESENT | DEFINED_ZERO | NOT_APPLICABLE | H1,H4 | rejected |
| A11 | PRESENT | PRESENT | DEFINED_ZERO | NOT_APPLICABLE | H4 | rejected |
| A12 | PRESENT | PRESENT | DEFINED_ZERO | PROFILE_UNAVAILABLE | H4 | rejected |
| A13 | PRESENT | PRESENT | DEFINED_ZERO | PROPERTY_UNDECLARED | H4 | rejected |
| A14 | PRESENT | PRESENT | PROFILE_UNAVAILABLE | DEFINED_NONZERO | H3 | rejected |
| A15 | PRESENT | PRESENT | PROPERTY_UNDECLARED | DEFINED_NONZERO | H3 | rejected |

Case S baseline result:

```text
B1_ADMISSIBLE_FAMILY: {A1,A2}
B1_REJECTED: {A3-A15}
```

A1 and A2 remain materially distinct because their readiness states differ at the declared target resolution.

Case U baseline result:

```text
B1_UNIQUE_TARGET_RESULT:
  NOT_UNIQUE_AT_DECLARED_RESOLUTION

reason:
  A1 and A2 are both admissible and materially distinct
```

No preference between `DEFINED_ZERO` and `DEFINED_NONZERO` was introduced.
No Optimization or arbitrary tie-break was used.

Baseline execution: **correct under the frozen B1 procedure**.

---

## 4. DSD Design candidate execution / DSD 후보 실행

The DSD run preserved Formation admission separately from General-Property status.

| Candidate | Formation / Property status basis | Failed constraints | DSD admissibility |
|---|---|---|---|
| A1 | primary admitted; reserve admitted; readiness DEFINED_ZERO; authorization DEFINED_NONZERO | none | admissible |
| A2 | primary admitted; reserve admitted; readiness DEFINED_NONZERO; authorization DEFINED_NONZERO | none | admissible |
| A3 | reserve CHANNEL_ABSENCE; readiness INAPPLICABLE | H2,H3 | rejected |
| A4 | readiness APPLICABLE_BUT_UNDEFINED | H3 | rejected |
| A5 | readiness PREREQUISITE_UNSATISFIED | H3 | rejected |
| A6 | readiness INAPPLICABLE | H3 | rejected |
| A7 | authorization DEFINED_ZERO | H4 | rejected |
| A8 | authorization APPLICABLE_BUT_UNDEFINED | H4 | rejected |
| A9 | authorization PREREQUISITE_UNSATISFIED | H4 | rejected |
| A10 | primary CHANNEL_ABSENCE; authorization INAPPLICABLE | H1,H4 | rejected |
| A11 | authorization INAPPLICABLE | H4 | rejected |
| A12 | authorization PROFILE_UNAVAILABLE | H4 | rejected |
| A13 | authorization UNDECLARED | H4 | rejected |
| A14 | readiness PROFILE_UNAVAILABLE | H3 | rejected |
| A15 | readiness UNDECLARED | H3 | rejected |

No undefined, inapplicable, unavailable, undeclared, zero, or absent state was coerced into another status.

---

## 5. DSD Case S — DESIGN_SPACE

All and only A1 and A2 satisfy H1-H4.

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {A1,A2}
REJECTED_CANDIDATES: {A3-A15}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
TERMINAL_STATUS_BASIS:
  exhaustive frozen family evaluated; exactly A1 and A2 satisfy H1-H4
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

A1 and A2 are retained as separate Design targets because `readiness` differs inside `TARGET_RESOLUTION`.

No ranking or selection between them occurs.

Case S: **PASS**.

---

## 6. DSD Case U — UNIQUE_TARGET

The same hard constraints leave both A1 and A2 admissible.
They are materially distinct at the declared target resolution:

```text
A1 readiness = DEFINED_ZERO
A2 readiness = DEFINED_NONZERO
```

No non-Optimization determinacy rule chooses one.

Therefore:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {A1,A2}
UNRESOLVED_FIELDS:
  unique readiness-state selection between DEFINED_ZERO and DEFINED_NONZERO
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS:
  UNIQUE_TARGET requested while two materially distinct admissible targets remain
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

No arbitrary tie-break, hidden preference, or Optimization rule was used.

Case U: **PASS**.

---

## 7. Claim-relevant baseline comparison / 주장 관련 기준선 비교

B1 and DSD agree on the frozen claim-relevant structure:

```text
Case S admissible family:
  B1  -> {A1,A2}
  DSD -> {A1,A2}

Candidate failure sets:
  B1  -> exactly the frozen A3-A15 sets
  DSD -> exactly the frozen A3-A15 sets

A1/A2 material distinctness:
  B1  -> preserved
  DSD -> preserved

Case U closure:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED
```

The labels differ because B1 is not a DSD method, but the claim-relevant conclusion is the same: the frozen task does not justify one unique target.

---

## 8. Gain-criterion execution / 이득 기준 실행

### G1 — status distinction gain

B1 preserved the same claim-relevant status classes presented to it and did not Boolean-collapse them.
DSD also preserved them.

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
```

### G2 — rejection traceability gain

B1 and DSD reproduced the same full hard-constraint failure set for every rejected candidate.

```text
G2 REJECTION_TRACEABILITY_GAIN: NOT_ESTABLISHED
```

### G3 — structure/property separation gain

B1 used separate structural and property-state columns and did not conflate `ABSENT` with property-state failure.
DSD likewise preserved the Formation/Property distinction.

```text
G3 STRUCTURE_PROPERTY_SEPARATION_GAIN: NOT_ESTABLISHED
```

### G4 — output-level closure gain

B1 did not force a unique target and explicitly reported `NOT_UNIQUE_AT_DECLARED_RESOLUTION`.
DSD returned `DESIGN_UNDERDETERMINED`.
Neither made unsupported closure.

```text
G4 OUTPUT_LEVEL_CLOSURE_GAIN: NOT_ESTABLISHED
```

### G5 — retraceability gain

The frozen B1 table and rules retrace every candidate verdict, failure set, admissible family, and non-unique conclusion.
The DSD record is also retraceable.

```text
G5 RETRACEABILITY_GAIN: NOT_ESTABLISHED
```

The frozen gain rule therefore requires:

```text
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

This is a valid comparison result, not a Design failure.

---

## 9. Three-ledger DSD result / DSD 3중 장부

Case S:

```text
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

Case U:

```text
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

The gain ledger is shared across the comparison because the same B1 procedure matches the DSD claim-relevant results in both frozen output-level subcases.

---

## 10. Precommitted scoring result / 사전 고정 점수 결과

```text
BASELINE_B1_CHECKS: 23 / 23 PASS
DSD_CHECKS: 19 / 19 PASS
GAIN_COMPARISON_CHECKS: 12 / 12 PASS

PRECOMMITTED_REQUIRED_CHECKS: 54
PASSED: 54
FAILED: 0
CHALLENGE_VERDICT: PASS
```

No failed check was hidden or reclassified.

---

## 11. Baseline-comparison verdict / 기준선 비교 판정

```text
CASE_ID: DES-CH-006
CASE_CLASS: baseline_comparison
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
BASELINE: B1_TYPED_ADMISSIBILITY_TABLE
DIRECT_EVIDENCE_RESULT: PASS
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
BASELINE_COMPARISON_PASS_INCREMENT: +1
```

This case fills the Design `baseline_comparison` evidence category at the constructed-evidence level.

The result does **not** establish broad DSD superiority; it establishes the opposite for this frozen comparison: a competent typed non-DSD baseline matched DSD on every measured claim-relevant dimension.

---

## 12. Relation to DES-CH-005 / DES-CH-005와의 관계

`DES-CH-005` established that a simple explicit constraint matrix could match DSD on a deliberately small Formation-only fixture.

`DES-CH-006` raises the pressure substantially:

```text
Formation + General Property
15 candidates
7 typed property-status classes represented across the baseline vocabulary
multi-constraint failure sets
DESIGN_SPACE + UNIQUE_TARGET subcases
full rejection-set comparison
explicit structure/property separation
```

Despite the broader pressure, no measured DSD gain was established against the frozen competent comparator.

Therefore the baseline evidence is not interpreted as a superiority result.

---

## 13. Reproducibility / 재현성

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  precommit: evidence/method_specific/design/DES-CH-006_precommit.md
  precommit_commit: 3a44350
  candidate_order: A1-A15
  candidate_coverage: exhaustive
  baseline: B1_TYPED_ADMISSIBILITY_TABLE
  baseline_state_vocabulary: frozen in precommit
  target_resolution: frozen in precommit
  hard_constraints: H1-H4 frozen in precommit
  subcases: Case S DESIGN_SPACE / Case U UNIQUE_TARGET
  stochastic_generation: none
  hidden_information: none
  task_revision_after_lock: none
  candidate_revision_after_lock: none
  baseline_revision_after_lock: none
  gain_criterion_revision_after_lock: none
```

The comparison is deterministically retraceable from the frozen record.

---

## 14. Evidence limit / 증거 한계

This remains a constructed, same-session, same-project comparison.

It directly supports:

```text
broader typed baseline comparison completed
baseline_comparison evidence category filled at constructed level
NO_GAIN against B1 on the frozen gain dimensions
```

It does not establish:

```text
external-domain applicability
independent evaluator agreement
human usability advantage
runtime advantage
engineering performance
external baseline superiority or inferiority
method maturity
```

The next major evidence gap is an external or independently generated Design application.
