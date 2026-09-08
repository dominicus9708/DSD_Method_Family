# DES-CH-005 — NO_GAIN Baseline Equivalence

Status: **PASS — first successful NO_GAIN constructed Design pilot under Protocol v0.1**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: `DES-CH-005_precommit.md`, commit `b030f90`

## 1. Evidence claim / 증거 주장

This challenge tests whether a fully correct and protocol-conformant DSD Design execution may still receive:

```text
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

when a strongest reasonable simple baseline reproduces every claim-relevant result required by the same frozen task at the same resolution.

The baseline, candidate family, expected outputs, and gain criteria were frozen before evaluation.

No post-hoc criterion change was made.

---

## 2. Frozen task recap / 동결 과업 요약

```text
DESIGN_TASK_ID: DES-TASK-005
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
CANDIDATE_COVERAGE: exhaustive
TARGET_DSD_LAYER_SCOPE: Formation only
TARGET_RESOLUTION:
  exact admission state of q_primary, q_reserve, q_aux
HARD_CONSTRAINTS:
  H1 q_primary is admitted
  H2 q_reserve is admitted
CANDIDATES:
  {N1,N2,N3}
```

Frozen candidates:

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

N1 and N2 are materially distinct at the declared target resolution because q_aux differs, even though q_aux is not a hard constraint.

---

## 3. Baseline B0 execution / 기준선 실행

Frozen baseline:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX
```

Execution table:

| Candidate | q_primary | q_reserve | q_aux | H1 | H2 | Baseline result | Rejection basis |
|---|---|---|---|---|---|---|---|
| N1 | ADMITTED | ADMITTED | ADMITTED | pass | pass | admissible | none |
| N2 | ADMITTED | ADMITTED | CHANNEL_ABSENCE | pass | pass | admissible | none |
| N3 | ADMITTED | CHANNEL_ABSENCE | ADMITTED | pass | fail | rejected | H2 |

Baseline result:

```text
BASELINE_ADMISSIBLE_FAMILY: {N1,N2}
BASELINE_REJECTED: {N3}
BASELINE_REJECTION_REASON_N3: H2
BASELINE_UNSUPPORTED_EXTRA_CLOSURE: none
BASELINE_OPTIMIZATION_OR_UNIQUENESS_CLAIM: none
```

The baseline preserved q_aux in the returned target records and therefore preserved N1 != N2 at the same target resolution.

Baseline execution: **correct under the frozen baseline procedure**.

---

## 4. DSD Design execution / DSD 설계 실행

### N1

```text
q_primary: ADMITTED
q_reserve: ADMITTED
q_aux: ADMITTED
H1: pass
H2: pass
ADMISSIBILITY_RESULT: admissible
```

### N2

```text
q_primary: ADMITTED
q_reserve: ADMITTED
q_aux: CHANNEL_ABSENCE
H1: pass
H2: pass
ADMISSIBILITY_RESULT: admissible
```

N2 does not violate H1 or H2 because q_aux is not constrained.
Its q_aux absence remains part of the target record rather than being erased.

### N3

```text
q_primary: ADMITTED
q_reserve: CHANNEL_ABSENCE
q_aux: ADMITTED
H1: pass
H2: fail
ADMISSIBILITY_RESULT: rejected
REJECTION_BASIS: H2
```

### DSD Design result

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {N1,N2}
REJECTED_CANDIDATES: {N3}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
TERMINAL_STATUS_BASIS:
  exhaustive frozen family evaluated; N1 and N2 satisfy H1-H2; N3 fails H2
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

No hidden Optimization, uniqueness claim, extra candidate, or target-resolution change occurred.

---

## 5. Claim-relevant comparison / 주장 관련 비교

Baseline and DSD Design agree on every claim-relevant output required by the frozen task:

```text
admissible family:
  B0  -> {N1,N2}
  DSD -> {N1,N2}

rejected candidate:
  B0  -> N3
  DSD -> N3

rejection basis:
  B0  -> H2
  DSD -> H2

N1/N2 distinctness at target resolution:
  B0  -> preserved
  DSD -> preserved

unsupported uniqueness/Optimization closure:
  B0  -> none
  DSD -> none
```

The DSD execution contains more explicit protocol and ledger structure, but the frozen challenge forbids counting additional bookkeeping alone as gain.

---

## 6. Gain-criterion execution / 이득 기준 실행

### G1 — distinction preservation

Frozen criterion:
DSD must preserve a claim-relevant distinction required by the task that B0 cannot preserve at the same target resolution.

Observed:

```text
B0 preserves q_aux and N1 != N2.
DSD preserves q_aux and N1 != N2.
```

Result:

```text
G1: NOT_ESTABLISHED
```

### G2 — rejection traceability

Frozen criterion:
DSD must provide a correct claim-relevant rejection basis that B0 cannot reproduce.

Observed:

```text
B0: N3 rejected on H2
DSD: N3 rejected on H2
```

Result:

```text
G2: NOT_ESTABLISHED
```

### G3 — unsupported closure avoidance

Frozen criterion:
B0 must make a stronger unsupported closure, uniqueness, or infeasibility claim that DSD correctly avoids.

Observed:

```text
B0 makes no unsupported closure.
DSD makes no unsupported closure.
```

Result:

```text
G3: NOT_ESTABLISHED
```

### G4 — retraceability

Frozen criterion:
A claim-relevant execution result required by this task must be retraceable under DSD but not under B0.

Observed:

```text
B0 frozen table + procedure retraces:
  N1 admissible
  N2 admissible
  N3 rejected on H2
  family {N1,N2}

DSD frozen record retraces the same claim-relevant result.
```

Result:

```text
G4: NOT_ESTABLISHED
```

Therefore:

```text
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

This is not a Design failure.

---

## 7. Three-ledger result / 3중 장부 결과

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT

DESIGN_METHOD_GAIN_STATUS:
  NO_GAIN
```

This pilot directly confirms that the three ledgers are operationally independent.

A method run can be correct and conformant while adding no demonstrated gain over a competent baseline for the declared task.

---

## 8. Precommitted scoring result / 사전 고정 점수 결과

```text
BASELINE_CHECKS:
  B0 evaluates exactly N1,N2,N3: PASS
  B0 keeps q_aux in target record: PASS
  B0 marks N1 admissible: PASS
  B0 marks N2 admissible: PASS
  B0 rejects N3 specifically on H2: PASS
  B0 returns exactly {N1,N2}: PASS
  B0 makes no Optimization or uniqueness claim: PASS

DSD_CHECKS:
  DSD evaluates exactly N1,N2,N3: PASS
  DSD preserves N1 != N2 at TARGET_RESOLUTION: PASS
  DSD marks N1 admissible: PASS
  DSD marks N2 admissible: PASS
  DSD rejects N3 specifically on H2: PASS
  DSD returns exactly {N1,N2}: PASS
  terminal status = DESIGN_ADMISSIBLE: PASS
  protocol conformance = CONFORMANT: PASS
  no hidden Optimization or uniqueness claim: PASS

GAIN_LEDGER_CHECKS:
  same claim-relevant admissible family: PASS
  same claim-relevant rejection reason for N3: PASS
  G1 not established: PASS
  G2 not established: PASS
  G3 not established: PASS
  G4 not established: PASS
  extra bookkeeping not counted as gain by itself: PASS
  DESIGN_METHOD_GAIN_STATUS = NO_GAIN: PASS
  NO_GAIN independent from DESIGN_ADMISSIBLE and CONFORMANT: PASS

PRECOMMITTED_REQUIRED_CHECKS: 25
PASSED: 25
FAILED: 0
CHALLENGE_VERDICT: PASS
```

---

## 9. Reproducibility / 재현성

```text
REPRODUCIBILITY_RECORD:
  protocol: methods/04_design/PROTOCOL_v0.1.md
  precommit: evidence/method_specific/design/DES-CH-005_precommit.md
  precommit_commit: b030f90
  candidate_order: N1,N2,N3
  candidate_coverage: exhaustive
  baseline: B0_EXPLICIT_CONSTRAINT_MATRIX
  baseline_candidate_order: N1,N2,N3
  baseline_hidden_information: none
  DSD_hidden_information: none
  stochastic_generation: none
  task_revision_after_lock: none
  gain_criterion_revision_after_lock: none
  baseline_revision_after_lock: none
```

The comparison is deterministically retraceable from the frozen record.

---

## 10. What this pilot directly supports / 직접 지지 범위

At pilot level, `DES-CH-005` directly supports that Protocol v0.1 can:

1. execute a correct admissible Design-space task;
2. compare against a precommitted baseline under the same inputs and resolution;
3. refuse to infer gain from extra notation or bookkeeping alone;
4. assign `NO_GAIN` without degrading the Design outcome or conformance verdict;
5. preserve the independence of Design result, protocol conformance, and method gain.

---

## 11. What this pilot does not support / 비지지 범위

This case does not establish:

```text
DSD Design superiority
broad baseline competitiveness
external-domain applicability
independent evaluator agreement
runtime/cost efficiency
large-space usefulness
complex design usefulness
method maturity
```

Although B0 is the strongest reasonable comparator for this intentionally simple synthetic task, this case does not by itself close the broader strongest-reasonable-baseline evidence requirement for method maturity.

---

## 12. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-005
CASE_CLASS: no_gain
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
BASELINE: B0_EXPLICIT_CONSTRAINT_MATRIX
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25
PASSED: 25
FAILED: 0
DIRECT_EVIDENCE_RESULT: PASS
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
NO_GAIN_VALIDATION_PASS_INCREMENT: +1
```

This is the first successful direct `NO_GAIN` Design pilot under Protocol v0.1.
