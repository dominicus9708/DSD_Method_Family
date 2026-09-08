# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / maturity: developing / validation in progress**

This lane records evidence that directly tests **DSD Design / DSD 설계론**. Evidence from other DSD methods or shared-core validation does not automatically count as direct Design validation.

A Design maturity audit is an **Audit meta-record** and does not increase the Design direct-pilot count.

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

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

The retrace reproduced candidate verdicts, rejection bases, `{W1,W2,W3}`, the three Design ledgers, external source/version, and `WCAG_APPLICATION_BRIDGE_001` from frozen artifacts.

It does **not** establish independent reproducibility: the same project/evaluator already knew the historical result and the run was non-blinded.

## Audit meta-record registry

### `DES-AUD-001` — first DSD Design maturity audit

Files:
- `DES-AUD-001_precommit.md` — maturity axes and 24 audit-discipline checks frozen before scoring; precommit `bf4c55c`.
- `DES-AUD-001_maturity-review.md` — completed audit; result `b2316d4`.

Audit ID:

```text
DSD-AUDIT-20260908-DESIGN-001
```

Maturity-axis result:

```text
M1  dedicated executable protocol                  PASS
M2  positive/negative terminal discrimination      PASS
M3  neighboring-method boundary discrimination     PASS
M4  NO_GAIN preservation                           PASS
M5  reproducibility/retraceability                 CONDITIONAL_PASS
M6  external application origin                    PASS
M7  strongest-reasonable-baseline comparison       PASS
M8  external source fidelity and bridge discipline PASS
M9  established-level evidence breadth             INSUFFICIENT
M10 independent/practical-performance evidence     UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect     PRESENT_NONFATAL
M12 maximum-supported-claim discipline             PASS
M13 candidate/construction-basis discipline        PASS
M14 historical failure / anti-post-hoc preservation PASS
```

Final audit decision:

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
DESIGN_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
```

The maturity audit explicitly preserves `DES-CH-003`, both `NO_GAIN` results, same-project retrace limitations, and the single-domain/project-constructed-fixture limit of `DES-APP-001`.

## Minimum evidence architecture

1. dedicated Design protocol — **established at v0.1**;
2. positive case — **DES-CH-001 PASS**;
3. negative/failure case — **DES-CH-002 PASS**;
4. boundary case — **DES-CH-004 PASS after DES-CH-003 failed test design was preserved**;
5. `NO_GAIN` case — **DES-CH-005 PASS**;
6. reproducibility/retrace record — **DES-CH-007 PASS at deterministic same-project level**;
7. external or independently generated application — **DES-APP-001 PASS at single external-standard application level**;
8. strongest-reasonable-baseline comparison — **DES-CH-006 PASS at constructed-evidence level; result NO_GAIN**.

The minimum category architecture is fully populated, but `DES-AUD-001` confirms that this does not confer established maturity.

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
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 1
EXTERNAL_DOMAINS: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

Address the primary maturity blocker rather than adding more same-project cases on already-covered axes.

The next preferred task is a **second external Design application in a materially different domain**, ideally with a candidate/construction basis supplied by an external artifact, source, or independently generated option set rather than authored solely for the DSD challenge.

After external breadth increases, prepare a genuinely independent evaluator packet. Practical benefit should be measured only when such a benefit is claimed.
