# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / validation in progress**

This lane records evidence that directly tests **DSD Design / DSD 설계론**.
Evidence from DSD Analysis, Audit, Specification, Synthesis, Transformation, Optimization, or shared-core validation does not automatically count as direct Design validation.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — initial executable protocol.

Protocol creation is required infrastructure but does not itself count as direct Design evidence.

## Required evidence record fields

Every v0.1 evidence record should preserve at minimum:

```text
EVIDENCE_SCOPE_CLASS
METHOD_DIRECTLY_TESTED
METHOD_VERSION_OR_PROTOCOL
CASE_ID
CASE_CLASS
CASE_ORIGIN
DESIGN_TASK_ID
TASK_SCOPE
CLAIMED_OUTPUT_LEVEL
GOALS
HARD_CONSTRAINTS
CONSTRAINT_SOURCE_OR_SPECIFICATION
BASE_STRUCTURE_OR_PREDECESSOR
TARGET_DSD_LAYER_SCOPE
TARGET_RESOLUTION
CANDIDATE_OR_CONSTRUCTION_BASIS
CANDIDATE_GENERATION_RULE
CANDIDATE_COVERAGE
DSD_INTERFACE_PROFILE
DOMAIN_BRIDGE
EXTERNAL_STANDARD
AUXILIARY_METHODS_OR_HANDOFFS
CANDIDATE_STATUS_RECORD
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY
REJECTED_CANDIDATE_REASONS
UNRESOLVED_FIELDS
TERMINAL_DESIGN_STATUS
TERMINAL_STATUS_BASIS
DESIGN_PROTOCOL_CONFORMANCE
DESIGN_METHOD_GAIN_STATUS
BASELINE_IF_GAIN_ASSESSED
GAIN_CRITERION_IF_ASSESSED
RESULT
LIMITS
REPRODUCIBILITY_RECORD
```

## Case-ID convention

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Case classes include:

```text
positive
negative_or_failure
boundary
no_gain
baseline_comparison
reproducibility
external_application
other_declared
```

Planning-stage `DES-BND-DRAFT-*` counterexamples remain pre-protocol planning records and are not direct v0.1 evidence.

## Direct evidence registry

### `DES-CH-001` — positive status-sensitive Design space

Files:
- `DES-CH-001_precommit.md` — precommit `f82a333`.
- `DES-CH-001_positive-status-sensitive-design-space.md` — result `9cdf871`.

```text
ADMISSIBLE_FAMILY: {T1,T2}
PRECOMMITTED_REQUIRED_CHECKS: 11/11 PASS
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Directly preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and returned the full admissible family without hidden Optimization.

### `DES-CH-002` — negative terminal-status separation

Files:
- `DES-CH-002_precommit.md` — precommit `1c40630`.
- `DES-CH-002_negative-terminal-status-separation.md` — result `65b47c9`.

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED
PRECOMMITTED_REQUIRED_CHECKS: 20/20 PASS
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in all subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The case directly prevents non-exhaustive failure-to-find from becoming global infeasibility and confirms `DESIGN_BLOCKED + CONFORMANT` when a required predecessor is missing.

### `DES-CH-003` — first Design/Optimization boundary attempt

Files:
- `DES-CH-003_precommit.md` — precommit `0d1abcf`.
- `DES-CH-003_boundary-design-optimization.md` — result `d15aaec`.

```text
PRECOMMITTED_REQUIRED_CHECKS: 20/21
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

The candidate differences existed only in downstream-only `resource_cost`, outside the frozen Design target resolution. The failed challenge was preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary

Files:
- `DES-CH-004_precommit.md` — precommit `47d73f6`.
- `DES-CH-004_boundary-design-optimization-corrected.md` — result `0a89bde`.

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
PRECOMMITTED_REQUIRED_CHECKS: 23/23 PASS
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The correction placed `reserve_mode = MODE_A / MODE_B / MODE_C` inside `TARGET_RESOLUTION`; downstream `resource_cost` remained an Optimization-only objective.

### `DES-CH-005` — NO_GAIN baseline equivalence

Files:
- `DES-CH-005_precommit.md` — precommit `b030f90`.
- `DES-CH-005_no-gain-baseline-equivalence.md` — result `1533567`.

Baseline:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX
```

B0 and DSD both returned `{N1,N2}`, rejected N3 on H2, and preserved N1/N2 distinctness.

```text
G1-G4: NOT_ESTABLISHED
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25/25 PASS
```

This is the first successful direct `NO_GAIN` pilot and confirms that extra DSD bookkeeping is not gain by itself.

### `DES-CH-006` — broader strongest-reasonable-baseline comparison

Files:
- `DES-CH-006_precommit.md` — precommit `3a44350`.
- `DES-CH-006_broader-typed-baseline-comparison.md` — result `c3708c3`.

Baseline:

```text
B1_TYPED_ADMISSIBILITY_TABLE
```

Scope:

```text
Formation + General Property
15 candidates
seven typed baseline property-state classes
multi-constraint rejection sets
DESIGN_SPACE + UNIQUE_TARGET
```

```text
Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

candidate failure sets:
  B1 == DSD

G1-G5: NOT_ESTABLISHED
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

This fills the Design `baseline_comparison` category at constructed-evidence level. It is not a superiority result; the competent typed baseline matched DSD on every frozen measured dimension.

### `DES-APP-001` — WCAG 2.2 external-standard application

Files:
- `DES-APP-001_precommit.md` — source clauses, fixture assumptions, candidate family, and 36 checks frozen before evaluation; precommit `4847dbd`.
- `DES-APP-001_wcag22-submit-control-application.md` — executed result `32a7842`.

External authority:

```text
W3C Web Content Accessibility Guidelines (WCAG) 2.2
W3C Recommendation 12 December 2024
selected subset:
  SC 1.4.3 Contrast (Minimum)
  SC 2.5.3 Label in Name
  SC 2.5.8 Target Size (Minimum)
```

Frozen fixture candidate result:

```text
W1 -> admissible
W2 -> admissible
W3 -> admissible
W4 -> H1 target size
W5 -> H1 target size
W6 -> H2 label in name
W7 -> H2 with APPLICABLE_BUT_UNDEFINED accessible name
W8 -> H3 contrast
W9 -> H1,H2,H3
W10 -> H0 CHANNEL_ABSENCE

ADMISSIBLE_FAMILY: {W1,W2,W3}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
```

External-source discipline directly tested:

```text
no source rewrite
no promotion of the SC 2.5.3 best-practice note into a hard requirement
no post-hoc SC 2.5.8 exception invention
no undefined/inapplicable/absence collapse
no full-WCAG-conformance overclaim
```

This fills the Design `external_application` category at the single external-standard application level. The candidate family is still project-constructed, so it does not establish independent evaluator agreement or external candidate generation.

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol — **established at v0.1**;
2. positive constructed case — **DES-CH-001 PASS**;
3. negative/failure case — **DES-CH-002 PASS**;
4. boundary case — **DES-CH-004 PASS after DES-CH-003 failed test design was preserved**;
5. `NO_GAIN` case — **DES-CH-005 PASS**;
6. reproducibility/retrace record — **case-level records exist; dedicated retrace stage still open**;
7. external or independently generated application — **DES-APP-001 PASS at single external-standard application level**;
8. strongest-reasonable-baseline comparison — **DES-CH-006 PASS at constructed-evidence level; result NO_GAIN**.

These categories are evidence prerequisites for later maturity consideration, not an automatic maturity grant.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 6
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
EXTERNAL_APPLICATIONS: 1
EXTERNAL_APPLICATION_PASSES: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
DEDICATED_RETRACE_STAGE: not completed
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

Run a dedicated **reproducibility/retrace Design test** under Protocol v0.1.

The test should freeze an existing completed evidence record and require a clean re-execution path to reproduce candidate verdicts, terminal status, conformance, and any active external/bridge inputs without revising the original case.
