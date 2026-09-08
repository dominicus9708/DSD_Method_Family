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

Locked challenge:

```text
CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE
CANDIDATE_COVERAGE: exhaustive relative to the toy challenge
CANDIDATES: T1,T2,T3,T4
EXPECTED_ADMISSIBLE: T1,T2
EXPECTED_REJECTED: T3,T4
```

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

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol — **established at v0.1**;
2. positive constructed case — **DES-CH-001 PASS**;
3. negative/failure case;
4. boundary case;
5. `NO_GAIN` case;
6. reproducibility/retrace record;
7. at least one external or independently generated application case;
8. strongest-reasonable-baseline comparison when applicable.

A later maturity audit evaluates the accumulated corpus; the checklist itself does not confer maturity.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 1
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 0
BOUNDARY_CASES_UNDER_PROTOCOL: 0
NO_GAIN_CASES: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
BASELINE_BENEFIT: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

Run a **negative/failure constructed Design challenge** under a separately pre-frozen Protocol v0.1 task record.

The next case should test a genuine non-success terminal outcome without turning missing information or non-exhaustive search into an unsupported `DESIGN_INFEASIBLE` claim.