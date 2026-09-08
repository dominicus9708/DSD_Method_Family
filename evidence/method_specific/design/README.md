# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / validation in progress**

This lane records evidence that directly tests **DSD Design / DSD 설계론**.

Evidence from DSD Analysis, Audit, Specification, Synthesis, Transformation, Optimization, or shared-core validation does not automatically count as direct Design validation.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — initial executable protocol.

Protocol creation is required infrastructure but does not itself count as a direct Design pilot.

## Required evidence record fields

Every v0.1 evidence record should preserve at minimum:

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Design
METHOD_VERSION_OR_PROTOCOL: v0.1
CASE_ID:
CASE_CLASS:
CASE_ORIGIN:
DESIGN_TASK_ID:
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
GOALS:
HARD_CONSTRAINTS:
CONSTRAINT_SOURCE_OR_SPECIFICATION:
BASE_STRUCTURE_OR_PREDECESSOR:
TARGET_DSD_LAYER_SCOPE:
TARGET_RESOLUTION:
CANDIDATE_OR_CONSTRUCTION_BASIS:
CANDIDATE_GENERATION_RULE:
CANDIDATE_COVERAGE:
DSD_INTERFACE_PROFILE:
VALIDATION_OR_ACCEPTANCE_RULE:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
AUXILIARY_METHODS_OR_HANDOFFS:
CANDIDATES_ACTUALLY_EVALUATED_OR_SYMBOLIC_FAMILY:
CANDIDATE_STATUS_RECORD:
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY:
REJECTED_CANDIDATE_REASONS:
UNRESOLVED_FIELDS:
TERMINAL_DESIGN_STATUS:
TERMINAL_STATUS_BASIS:
DESIGN_PROTOCOL_CONFORMANCE:
DESIGN_METHOD_GAIN_STATUS:
BASELINE_IF_GAIN_ASSESSED:
GAIN_CRITERION_IF_ASSESSED:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

Inactive conditional fields should be omitted or marked consistently rather than filled with invented content.

## Case-ID convention fixed by Protocol v0.1

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Every case additionally records one or more explicitly tested `CASE_CLASS` values:

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

### `DES-CH-001` — positive status-sensitive admissible Design space

Files:

- `DES-CH-001_precommit.md` — task/candidate/pass criteria frozen before scoring; precommit commit `f82a333`.
- `DES-CH-001_positive-status-sensitive-design-space.md` — executed result; result commit `9cdf871`.

Result:

```text
PRECOMMITTED_REQUIRED_CHECKS: 11
PASSED: 11
FAILED: 0
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
```

Directly tested distinctions:

```text
DEFINED_ZERO
!= APPLICABLE_BUT_UNDEFINED
!= CHANNEL_ABSENCE
```

The admissible family `{T1,T2}` was returned without selecting one as best, so no hidden Optimization was invoked.

Evidence limit: constructed same-session positive pilot only; no external, baseline, or independent-evaluator claim.

### `DES-CH-002` — negative terminal-status separation

Files:

- `DES-CH-002_precommit.md` — three non-success subcases frozen before evaluation; precommit commit `1c40630`.
- `DES-CH-002_negative-terminal-status-separation.md` — executed result; result commit `65b47c9`.

Frozen pressure points:

```text
Case I: exhaustive candidate universe + all candidates rejected
Case U: non_exhaustive evaluated sample + no admissible target found
Case B: claim-required predecessor identity unavailable
```

Result:

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED

PRECOMMITTED_REQUIRED_CHECKS: 20
PASSED: 20
FAILED: 0
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in all three subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
```

The case directly tests that non-exhaustive failure-to-find is not promoted to global infeasibility and that a missing claim-required predecessor is exposed as blocking rather than fabricated or treated as a rejection.

Evidence limit: constructed same-session negative/failure pilot only; one case ID with three locked subcases, therefore direct-pilot increment is +1, not +3.

### `DES-CH-003` — first Design/Optimization boundary attempt

Files:

- `DES-CH-003_precommit.md` — precommit commit `0d1abcf`.
- `DES-CH-003_boundary-design-optimization.md` — executed result; result commit `d15aaec`.

Result:

```text
PRECOMMITTED_REQUIRED_CHECKS: 21
PASSED: 20
FAILED: 1
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

The failed requirement was the expected `DESIGN_UNDERDETERMINED` result for `UNIQUE_TARGET`.
The only differences among `O1-O3` were `resource_cost` values, but the same precommit excluded `resource_cost` from the declared Design target resolution and treated it only as downstream Optimization metadata.
Therefore `O1-O3` were not materially distinct Design targets at the frozen resolution.

The case was not repaired post hoc and remains direct evidence of the precommit/test-resolution blind spot.
It counts as an executed direct pilot but not as a successful boundary validation.

### `DES-CH-004` — corrected Design/Optimization boundary

Files:

- `DES-CH-004_precommit.md` — corrected candidate distinction frozen before evaluation; precommit commit `47d73f6`.
- `DES-CH-004_boundary-design-optimization-corrected.md` — executed result; result commit `0a89bde`.

Prospective correction:

```text
reserve_mode(q_reserve) = MODE_A / MODE_B / MODE_C
```

is explicitly part of `TARGET_RESOLUTION`, so `C1`, `C2`, and `C3` are materially distinct Design targets while all remain admissible under the same hard constraints.

A separate downstream objective:

```text
minimize resource_cost
```

can rank them, but is not used inside Design.

Result:

```text
Case S: DESIGN_SPACE
  -> {C1,C2,C3}
  -> DESIGN_ADMISSIBLE

Case U: UNIQUE_TARGET
  -> three materially distinct admissible targets remain
  -> DESIGN_UNDERDETERMINED

PRECOMMITTED_REQUIRED_CHECKS: 23
PASSED: 23
FAILED: 0
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in both subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_EVIDENCE_RESULT: PASS
```

This is the first successful executable-protocol Design boundary validation.
It validates the Design-side separation only; DSD Optimization itself is not validated by this case.

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol — **established at v0.1**;
2. positive constructed case — **DES-CH-001 PASS**;
3. negative/failure case — **DES-CH-002 PASS**;
4. boundary case — **DES-CH-004 PASS after DES-CH-003 test-design failure was preserved**;
5. `NO_GAIN` case;
6. reproducibility/retrace record;
7. at least one external or independently generated application case;
8. strongest-reasonable-baseline comparison when applicable.

A later maturity audit evaluates the accumulated corpus; the checklist itself does not confer maturity.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 4
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
BASELINE_BENEFIT: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

Run a separately precommitted **`NO_GAIN` Design challenge** under Protocol v0.1 with a strongest reasonable baseline locked before comparison.

The challenge should allow the DSD Design result to be correct while demonstrating that the DSD procedure adds no material gain over the baseline on the declared gain criterion.
