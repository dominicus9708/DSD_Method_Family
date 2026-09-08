# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / validation in progress**

This lane records evidence that directly tests **DSD Design / DSD 설계론**. Evidence from other DSD methods or shared-core validation does not automatically count as direct Design validation.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — initial executable protocol.

## Case-ID convention

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Case classes include `positive`, `negative_or_failure`, `boundary`, `no_gain`, `baseline_comparison`, `reproducibility`, `external_application`, and other explicitly declared classes.

## Direct evidence registry

### `DES-CH-001` — positive status-sensitive Design space

```text
ADMISSIBLE_FAMILY: {T1,T2}
PRECOMMITTED_REQUIRED_CHECKS: 11/11 PASS
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and returned the full admissible family without hidden Optimization.

### `DES-CH-002` — negative terminal-status separation

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED
PRECOMMITTED_REQUIRED_CHECKS: 20/20 PASS
```

Directly prevents non-exhaustive failure-to-find from becoming global infeasibility and confirms `DESIGN_BLOCKED + CONFORMANT` when a required predecessor is missing.

### `DES-CH-003` — first Design/Optimization boundary attempt

```text
PRECOMMITTED_REQUIRED_CHECKS: 20/21
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

Candidate differences existed only outside the frozen Design target resolution. The failed challenge was preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
PRECOMMITTED_REQUIRED_CHECKS: 23/23 PASS
```

The correction placed `reserve_mode = MODE_A / MODE_B / MODE_C` inside `TARGET_RESOLUTION`; downstream `resource_cost` remained Optimization-only.

### `DES-CH-005` — NO_GAIN baseline equivalence

Baseline: `B0_EXPLICIT_CONSTRAINT_MATRIX`.

```text
B0 == DSD on frozen claim-relevant result
G1-G4: NOT_ESTABLISHED
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25/25 PASS
```

Confirms that extra DSD bookkeeping is not method gain by itself.

### `DES-CH-006` — broader strongest-reasonable-baseline comparison

Baseline: `B1_TYPED_ADMISSIBILITY_TABLE`.

```text
Formation + General Property
15 candidates
multi-constraint failure sets
DESIGN_SPACE + UNIQUE_TARGET

Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

G1-G5: NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

Fills the `baseline_comparison` category at constructed-evidence level. It is not a superiority result; the competent typed baseline matched DSD on all frozen measured dimensions.

### `DES-APP-001` — WCAG 2.2 external-standard application

Files:
- `DES-APP-001_precommit.md` — precommit `4847dbd`.
- `DES-APP-001_wcag22-submit-control-application.md` — result `32a7842`.

External authority: W3C `WCAG 2.2`, Recommendation 2024-12-12, limited to SC 1.4.3, 2.5.3, and 2.5.8.

```text
W1,W2,W3 -> admissible
W4 -> H1
W5 -> H1
W6 -> H2
W7 -> H2 with APPLICABLE_BUT_UNDEFINED name
W8 -> H3
W9 -> H1,H2,H3
W10 -> H0 CHANNEL_ABSENCE

ADMISSIBLE_FAMILY: {W1,W2,W3}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
```

Kept source requirement separate from fixture assumptions, did not promote a best-practice note into a hard requirement, did not invent a post-hoc exception, and did not overclaim full WCAG conformance.

### `DES-CH-007` — deterministic retrace of DES-APP-001

Files:
- `DES-CH-007_precommit.md` — immutable artifact manifest and 44 checks frozen before retrace scoring; precommit `d6d9103`.
- `DES-CH-007_retrace-des-app-001.md` — executed retrace; result `d666a41`.

Frozen retrace anchors:

```text
Protocol v0.1:
  b3d658c839dfe60b65efbc44abf874e257d4a0e2
DES-APP-001 precommit:
  4847dbd1f5a38adb5d5c285b19ac41ebcfe86b96
DES-APP-001 historical result:
  32a7842758be0cc179f996fdd8035d9683d31da9
```

Re-execution from frozen Protocol + source precommit reconstructed exactly:

```text
candidate order W1-W10
H0-H3
external source/version
bridge WCAG_APPLICATION_BRIDGE_001
candidate verdicts and rejection sets
admissible family {W1,W2,W3}
DESIGN_ADMISSIBLE
CONFORMANT
NOT_ASSESSED
```

Retrace ledger:

```text
RETRACE_ARTIFACT_INTEGRITY:      PASS
RETRACE_TASK_FIELD_MATCH:        PASS
RETRACE_EXTERNAL_SOURCE_MATCH:   PASS
RETRACE_BRIDGE_MATCH:            PASS
RETRACE_CANDIDATE_RECORD_MATCH:  PASS
RETRACE_CANDIDATE_VERDICT_MATCH: PASS
RETRACE_REJECTION_BASIS_MATCH:   PASS
RETRACE_ADMISSIBLE_FAMILY_MATCH: PASS
RETRACE_TERMINAL_STATUS_MATCH:   PASS
RETRACE_CONFORMANCE_MATCH:       PASS
RETRACE_GAIN_LEDGER_MATCH:       PASS
RETRACE_RESULT:                  PASS

PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
```

This fills the dedicated Design `reproducibility/retrace` category at the deterministic same-project level.
It does **not** establish independent reproducibility: the same project/evaluator already knew the historical result, the run was non-blinded, and the historical result had been fetched to freeze its immutable identity before the retrace precommit.

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol — **established at v0.1**;
2. positive case — **DES-CH-001 PASS**;
3. negative/failure case — **DES-CH-002 PASS**;
4. boundary case — **DES-CH-004 PASS after DES-CH-003 failed test design was preserved**;
5. `NO_GAIN` case — **DES-CH-005 PASS**;
6. reproducibility/retrace record — **DES-CH-007 PASS at deterministic same-project level**;
7. external or independently generated application — **DES-APP-001 PASS at single external-standard application level**;
8. strongest-reasonable-baseline comparison — **DES-CH-006 PASS at constructed-evidence level; result NO_GAIN**.

The minimum category architecture is now populated, but this does not confer maturity. Independent evaluator validation remains absent and must be discounted in the later maturity audit.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 7
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
NO_GAIN_VALIDATION_PASSES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_PASSES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 1
EXTERNAL_APPLICATION_PASSES: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

Run a **DSD Audit maturity review** of the accumulated Design corpus.

The audit must explicitly discount same-project/common-evaluator dependence, preserve the historical DES-CH-003 challenge-design failure, treat NO_GAIN results as valid non-superiority evidence rather than failures, and avoid automatic maturity promotion merely because all minimum evidence categories are populated.
