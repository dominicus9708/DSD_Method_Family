# DES-CH-005 — NO_GAIN Baseline Comparison Precommit

Status: **PRECOMMITTED BEFORE EVALUATION**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **no_gain**

## 1. Purpose / 목적

Test whether DSD Design can return a correct Design result while still receiving `DESIGN_METHOD_GAIN_STATUS = NO_GAIN` when a strongest reasonable simple baseline reaches the same claim-relevant result at the same declared resolution.

This challenge is deliberately constructed so that no claim-relevant undefinedness, prerequisite ambiguity, cross-layer bridge, neighboring-method handoff, dynamic transition, or aggregation-reconstruction issue is present.

The test is not allowed to treat additional DSD bookkeeping by itself as method gain.

---

## 2. Frozen Design task / 동결 설계 과업

```text
CASE_ID: DES-CH-005
DESIGN_TASK_ID: DES-TASK-005
PROTOCOL_VERSION: v0.1
CASE_CLASS: no_gain
CASE_ORIGIN: constructed_same_session
TASK_SCOPE: finite symbolic channel-admission design space
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
GOALS:
  return every admissible target in the frozen exhaustive candidate universe
HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
CONSTRAINT_SOURCE_OR_SPECIFICATION:
  synthetic_test_fixture DES-CH-005 precommit
BASE_STRUCTURE_OR_PREDECESSOR:
  none; new symbolic target records
TARGET_DSD_LAYER_SCOPE:
  Formation only
TARGET_RESOLUTION:
  exact admission state of q_primary, q_reserve, q_aux
CANDIDATE_OR_CONSTRUCTION_BASIS:
  explicit frozen family {N1,N2,N3}
CANDIDATE_GENERATION_RULE:
  none; candidates are enumerated explicitly
CANDIDATE_COVERAGE:
  exhaustive relative to DES-TASK-005
DSD_INTERFACE_PROFILE:
  current Formation interface as referenced by Protocol v0.1
VALIDATION_OR_ACCEPTANCE_RULE:
  candidate is Design-admissible iff H1 and H2 both pass
DOMAIN_BRIDGE:
  not_used
EXTERNAL_STANDARD:
  not_used
AUXILIARY_METHODS_OR_HANDOFFS:
  not_used
SOFT_PREFERENCES:
  not_used
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
  not_used
```

---

## 3. Frozen candidates / 동결 후보

```text
N1:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  q_aux = ADMITTED

N2:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  q_aux = CHANNEL_ABSENCE

N3:
  q_primary = ADMITTED
  q_reserve = CHANNEL_ABSENCE
  q_aux = ADMITTED
```

`q_aux` is inside `TARGET_RESOLUTION` but is not constrained by H1-H2.
Therefore N1 and N2 are materially distinct Design targets while both can remain admissible.

No candidate may be added, removed, or edited after this precommit.

---

## 4. Frozen strongest reasonable baseline / 동결 기준선

Baseline ID:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX
```

Baseline procedure:

1. read the same frozen candidate family N1-N3;
2. inspect q_primary and q_reserve admission states;
3. mark H1/H2 pass or fail for each candidate;
4. retain every candidate passing both constraints;
5. record the first explicit failed hard constraint as rejection reason for rejected candidates;
6. preserve q_aux in the returned target records because it is part of the declared target resolution;
7. make no ranking, uniqueness, or Optimization claim.

Baseline output schema:

```text
CANDIDATE_ID
q_primary admission
q_reserve admission
q_aux admission
H1 verdict
H2 verdict
BASELINE_ADMISSIBILITY
BASELINE_REJECTION_REASON
```

This baseline is considered the strongest reasonable comparator for this deliberately simple finite task because it has the same candidate coverage, the same hard constraints, the same target resolution, and enough explicit record structure to reproduce the Design-space verdict without DSD-specific machinery.

The baseline is not allowed to receive hidden information unavailable to DSD, and DSD is not allowed to receive extra candidate information unavailable to the baseline.

---

## 5. Frozen gain criteria / 동결 이득 기준

Method gain is adjudicated only after both B0 and DSD Design are executed from the frozen record.

```text
G1 DISTINCTION_PRESERVATION_GAIN
  established only if DSD preserves a claim-relevant distinction required by the task
  that B0 cannot preserve at the same target resolution.

G2 REJECTION_TRACEABILITY_GAIN
  established only if DSD provides a correct claim-relevant rejection basis
  that B0 cannot reproduce from the same frozen inputs.

G3 UNSUPPORTED_CLOSURE_AVOIDANCE_GAIN
  established only if B0 makes a stronger unsupported closure/uniqueness/infeasibility claim
  that DSD correctly avoids.

G4 RETRACEABILITY_GAIN
  established only if a claim-relevant execution result required by this task
  is reproducibly retraceable under DSD but not under the frozen B0 record.
```

Gain decision rule:

```text
if DSD execution is nonconformant or incorrect:
  challenge does not establish NO_GAIN or GAIN_ESTABLISHED

else if one or more of G1-G4 is established:
  DESIGN_METHOD_GAIN_STATUS = GAIN_ESTABLISHED

else if B0 and DSD are both correct at the frozen claim/resolution
     and B0 reproduces every claim-relevant distinction, rejection basis,
     closure restraint, and retrace result required by this task:
  DESIGN_METHOD_GAIN_STATUS = NO_GAIN

otherwise:
  DESIGN_METHOD_GAIN_STATUS = NOT_ASSESSED or challenge failure,
  according to the missing comparison condition
```

Additional DSD labels, headings, ledger fields, or verbosity do **not** count as gain unless they satisfy G1-G4 on this task.

---

## 6. Frozen expected baseline result / 동결 예상 기준선 결과

```text
N1: H1 pass, H2 pass -> admissible
N2: H1 pass, H2 pass -> admissible
N3: H1 pass, H2 fail -> rejected on H2

BASELINE_ADMISSIBLE_FAMILY: {N1,N2}
BASELINE_REJECTED: {N3}
BASELINE_UNSUPPORTED_EXTRA_CLOSURE: none
```

---

## 7. Frozen expected DSD result / 동결 예상 DSD 결과

```text
N1 -> admissible
N2 -> admissible
N3 -> rejected on H2

ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {N1,N2}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

Expected gain result if the frozen comparison executes exactly as specified:

```text
G1: not established
G2: not established
G3: not established
G4: not established
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

This expectation is frozen before evaluation and must not be repaired in place if the executed comparison disagrees.

---

## 8. Precommitted required checks / 사전 고정 검사

### Baseline checks

1. B0 evaluates exactly N1,N2,N3.
2. B0 keeps q_aux in the target record.
3. B0 marks N1 admissible.
4. B0 marks N2 admissible.
5. B0 rejects N3 specifically on H2.
6. B0 returns exactly {N1,N2}.
7. B0 makes no Optimization or uniqueness claim.

### DSD checks

8. DSD evaluates exactly N1,N2,N3.
9. DSD preserves N1 != N2 at TARGET_RESOLUTION because q_aux differs.
10. DSD marks N1 admissible.
11. DSD marks N2 admissible.
12. DSD rejects N3 specifically on H2.
13. DSD returns exactly {N1,N2}.
14. DSD terminal status is DESIGN_ADMISSIBLE.
15. DSD protocol conformance is CONFORMANT.
16. DSD makes no hidden Optimization or uniqueness claim.

### Gain-ledger checks

17. B0 and DSD have the same claim-relevant admissible family.
18. B0 and DSD have the same claim-relevant rejection reason for N3.
19. G1 is not established.
20. G2 is not established.
21. G3 is not established.
22. G4 is not established.
23. Additional DSD bookkeeping is not counted as gain by itself.
24. DESIGN_METHOD_GAIN_STATUS = NO_GAIN.
25. NO_GAIN is recorded independently from DESIGN_ADMISSIBLE and CONFORMANT.

```text
PRECOMMITTED_REQUIRED_CHECKS: 25
```

Any failed required check is preserved in the executed result.

---

## 9. Evidence-count rule / 증거 수 규칙

If executed after this precommit, `DES-CH-005` counts as one direct constructed Design pilot regardless of result.

A successful result may satisfy the Design `NO_GAIN` evidence category.
It does **not** by itself close the broader strongest-reasonable-baseline evidence requirement for method maturity because this comparator is intentionally a simple same-session synthetic baseline.

---

## 10. Frozen limitations / 동결 한계

This challenge does not test:

```text
external-domain applicability
independent evaluator agreement
complex domain-native design practice
runtime or cost efficiency
large candidate spaces
heuristic generation
cross-layer bridge value
neighboring-method handoff value
dynamic design
method maturity
```

The purpose is narrower: verify that Protocol v0.1 permits an entirely correct Design execution to end with `NO_GAIN` when a competent simple baseline already does the claim-relevant work equally well.
