# SPEC-APP-006 — `ErrorTree` Read-Mutation Real-World Issue / Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case origin: organizational_or_technical_incident
External domain: Python library API behavior / error-structure semantics

## 1. Locked source before resolution reveal

Primary source available to the predicting evaluator:

- `python-jsonschema/jsonschema` issue #1328 body only.
- Issue title: `The return of __iter__() and __contains__() change after accessing of an index with no error`.
- Reproduction: an `ErrorTree` initially reports only index `0`; reading `tree[1]` then changes `list(tree)` to `[0, 1]` and `1 in tree` to `True` even though index `1` has no error.
- Reporter states this contradicts the documented `ErrorTree` behavior and is a bug.

Metadata visible before reveal:

```text
ISSUE_STATE: closed
ISSUE_LABEL: Bug
CLOSED_DATE: 2026-09-06
```

These metadata do not reveal the actual fix mechanism, tests, discussion, or maintainer resolution rationale.

## 2. Resolution information withheld until after prediction commit

Do not inspect before frozen prediction:

```text
issue comments
linked pull requests
patches / changed files
closing commit
maintainer resolution explanation
post-issue tests added by maintainers
```

A valid comparison requires a separate frozen prediction commit before any of the above are read.

## 3. Declared downstream task

From the issue body alone, construct a DSD Specification v1.0 acceptance record for a repair and predict the **behavioral acceptance/fix-test family**, not exact implementation details.

The result will be compared against the later maintainer discussion and actual resolution artifacts.

## 4. DSD interface lock

```text
FORMATION_LAYER: not used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

Rationale: the issue is about typed membership/iteration state and an operation that should not silently alter the externally reported error-key set. No aggregate or temporal lineage layer is required for the locked task.

## 5. Locked requirement-inventory candidates

The prediction must resolve the following source-derived questions without inventing implementation structure:

```text
Q1  What should `list(tree)` represent?
Q2  What should `key in tree` represent?
Q3  Should a read of a missing/error-free child change Q1 or Q2?
Q4  Must pre-existing actual-error keys remain observable after such a read?
Q5  Is internal storage strategy constrained by the issue body?
Q6  What minimum regression-test family follows from the reproduced behavior?
```

## 6. Scoring before reveal

After the prediction is frozen, score against the actual resolution artifacts on these axes:

```text
A1_BEHAVIORAL_REQUIREMENT_MATCH
A2_MEMBERSHIP_ITERATION_SEMANTICS_MATCH
A3_READ_NONMUTATION_OR_EQUIVALENT_OBSERVATIONAL_INVARIANT_MATCH
A4_PREEXISTING_ERROR_PRESERVATION_MATCH
A5_REGRESSION_TEST_FAMILY_MATCH
A6_IMPLEMENTATION_OVERPREDICTION_COUNT
A7_SOURCE_FACT_INVENTION_COUNT
A8_POST_REVEAL_PREDICTION_CHANGE
```

Possible verdicts:

```text
MATCH
PARTIAL_MATCH
NON_MATCH
UNRESOLVED_BY_RESOLUTION_ARTIFACTS
```

Do not convert a missing resolution detail into a match.

## 7. Hard-failure criteria

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
FABRICATED_RESOLUTION_DETAIL
POST_REVEAL_PREDICTION_REWRITE
IMPLEMENTATION_DETAIL_PRESENTED_AS_SOURCE_REQUIREMENT
CLAIMING_INDEPENDENT_EVALUATOR_VALIDATION
```

## 8. Guardrails

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive unless maintainer/source purpose becomes material
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: inactive unless a derivative design view is added
```

## 9. Baseline and claim restraint

Baseline is the issue report plus the maintainers' actual resolution artifacts.

The test does not ask whether DSD is superior to ordinary bug fixing. It asks whether DSD Specification v1.0 can derive a compact, source-faithful acceptance contract that aligns with a later real-world resolution without seeing that resolution first.

```text
EXTERNAL_REAL_WORLD_SOURCE: yes
RESOLUTION_WITHHELD_AT_PRECOMMIT: yes
PREDICTING_EVALUATOR_INDEPENDENCE: no
BLINDNESS_LEVEL: resolution-artifact-withheld, not evaluator-independent
```

## 10. Anti-post-hoc rule

Once the prediction file is committed:

```text
prediction wording is frozen
requirement atoms are frozen
scoring axes are frozen
implementation-specific surprises may be recorded only as unmatched/unpredicted facts
no criteria may be added merely because the resolution contains them
```
