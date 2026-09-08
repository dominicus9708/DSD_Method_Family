# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / no direct validation yet**

This lane records evidence that directly tests **DSD Design / DSD 설계론**.

Evidence from DSD Analysis, Audit, Specification, Synthesis, Transformation, Optimization, or shared-core validation does not automatically count as direct Design validation.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — initial executable protocol, validation pending.

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

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol — **established at v0.1**;
2. positive constructed case;
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
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
BASELINE_BENEFIT: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_pending
```

## Immediate next evidence task

Run the first **positive constructed Design challenge** under a pre-frozen Protocol v0.1 task record.
The case should contain at least one admissible target, preserve all claim-relevant DSD distinctions, avoid hidden Optimization, and leave `DESIGN_METHOD_GAIN_STATUS = NOT_ASSESSED` unless a baseline comparison is separately performed.
