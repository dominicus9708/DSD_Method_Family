# SPEC-MEAS-001 — pytest #12112 Paired Practical-Benefit Benchmark Result

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit: `435ead45b8c1460b6c5eea18da0db71587beca15`
Frozen strong baseline: `9dcff7e1370886a59d49d6ce27045b5d59ce19b8`
Frozen DSD record: `8eb97d15a3d07d723c88bf9062e470fa25f148f6`
External issue: `pytest-dev/pytest#12112`
Later resolving PR: `pytest-dev/pytest#12169`
PR merge commit: `99890636bfd9bb156655050f22f1df47e74ac3f6`

## 1. Result in one line

The strong plain-language checklist and DSD Specification v1.0 record produced the same material acceptance coverage against the later pytest resolution: five full matches and one partial match each, with zero implementation overprediction and zero source-fact invention. The DSD record was about three times larger by stored UTF-8 size, so this locked standalone task is classified `TIE_WITH_DSD_OVERHEAD`, not a positive measured practical-benefit case.

```text
ROUTE_B_FULL_MATCH_AXES: 5/6
ROUTE_B_PARTIAL_MATCH_AXES: 1/6
ROUTE_B_NON_MATCH_AXES: 0/6

ROUTE_D_FULL_MATCH_AXES: 5/6
ROUTE_D_PARTIAL_MATCH_AXES: 1/6
ROUTE_D_NON_MATCH_AXES: 0/6

ROUTE_B_IMPLEMENTATION_OVERPREDICTION_COUNT: 0
ROUTE_D_IMPLEMENTATION_OVERPREDICTION_COUNT: 0
ROUTE_B_SOURCE_FACT_INVENTION_COUNT: 0
ROUTE_D_SOURCE_FACT_INVENTION_COUNT: 0
POST_REVEAL_REQUIREMENT_CHANGE: 0 for both routes

ROUTE_B_REPOSITORY_UTF8_BYTES: 1921
ROUTE_D_REPOSITORY_UTF8_BYTES: 5697
DSD_TO_BASELINE_BYTE_RATIO: 2.966

COMPARATIVE_VERDICT: TIE_WITH_DSD_OVERHEAD
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not demonstrated
```

## 2. Reveal sequence and an important source correction

Both representations were frozen from the original issue body before comments and PR #12169 were inspected.

The post-freeze discussion revealed an important complication. The original reporter concluded that the first supplied example was incomplete: after adding missing `__init__.py` files at the intended package levels the example ran successfully, and a separate erroneous `__init__.py` in the reporter's real project explained that initial failure. The reporter temporarily called the report a false alarm, and the maintainer initially closed it as working as intended.

Later, however, another user supplied a genuine related namespace-package failure in `jaraco.test`: pytest missed the `jaraco` namespace during discovery, imported `jaraco.test` as top-level `test`, and collided with the standard-library `test` package. Pinning pytest below 8.1 worked around that failure.

The issue then acquired a real pytest-side resolution. Maintainer PR #12169 was merged and explicitly states `Fix #12112`; it replaces hand-crafted namespace-package detection with `importlib`-based detection and adds regression coverage.

This mixed history means the benchmark must not pretend that the original exact reproducer was itself a clean bug case. The frozen representations are therefore scored against the final issue-resolution family while preserving a partial on A1.

## 3. External resolution facts

PR #12169 is merged.

Its declared purpose is to refine namespace-package detection by relying on `importlib` rather than the previous hand-crafted approach.

The implementation:

```text
- computes candidate module names from paths;
- asks importlib whether the candidate module is importable;
- checks that the resulting ModuleSpec corresponds to the intended module path;
- considers namespace packages while walking candidate roots when consider_namespace_packages is enabled.
```

The changelog states that namespace-package detection is improved when `consider_namespace_packages` is enabled, including more situations such as editable installs.

The test patch adds substantial namespace-package coverage, including a test whose docstring explicitly says `Regression test for #12112`, plus checks for module/path identity and broader namespace layouts.

Maintainer/user comments also report that #12169 makes the genuine `jaraco.test` and `jaraco.site` cases pass when `consider_namespace_packages` is enabled.

## 4. Locked-axis scoring

### A1 — reported-layout collection restoration

The original exact reproducer was later acknowledged by its reporter to be incomplete/misconfigured, so the premise that pytest itself had to repair that exact layout did not survive reveal unchanged.

At the same time, later independent examples exposed a genuine namespace-detection regression family, and PR #12169 restored correct behavior for those related cases.

Therefore neither frozen route receives a full match for the original exact-layout repair claim.

```text
ROUTE_B_A1: PARTIAL_MATCH
ROUTE_D_A1: PARTIAL_MATCH
```

### A2 — relative-import package identity

The later genuine failure was precisely an identity/scoping failure: `jaraco.test` was treated as top-level `test`. PR #12169 introduces module-spec/path matching and importlib-based namespace detection to retain the intended module identity.

```text
ROUTE_B_A2: MATCH
ROUTE_D_A2: MATCH
```

### A3 — importlib-mode compatibility

The issue family arose on the reported importlib collection path, and the merged resolution changes the import/path-resolution machinery rather than requiring the user to replace the task with another import mode. Existing namespace tests cover import modes including `importlib`.

```text
ROUTE_B_A3: MATCH
ROUTE_D_A3: MATCH
```

### A4 — `consider_namespace_packages` boundary

The merged changelog and maintainer comments preserve this option as a material activation boundary. The later genuine cases work with the option enabled; it is not silently discarded.

```text
ROUTE_B_A4: MATCH
ROUTE_D_A4: MATCH
```

### A5 — direct regression-test family

PR #12169 adds namespace-package detection tests, including an explicit `Regression test for #12112`, module/path identity checks, and broader multi-level namespace-package cases.

```text
ROUTE_B_A5: MATCH
ROUTE_D_A5: MATCH
```

### A6 — implementation freedom

Neither frozen route guessed the actual `importlib.util.find_spec`, `ModuleSpec.origin`, candidate-root walk, helper functions, or exact patch architecture.

```text
ROUTE_B_A6: MATCH
ROUTE_D_A6: MATCH
```

## 5. Error and overprediction comparison

```text
ROUTE_B_UNSUPPORTED_REQUIREMENT_COUNT: 0
ROUTE_D_UNSUPPORTED_REQUIREMENT_COUNT: 0

ROUTE_B_IMPLEMENTATION_OVERPREDICTION_COUNT: 0
ROUTE_D_IMPLEMENTATION_OVERPREDICTION_COUNT: 0

ROUTE_B_SOURCE_FACT_INVENTION_COUNT: 0
ROUTE_D_SOURCE_FACT_INVENTION_COUNT: 0

ROUTE_B_POST_REVEAL_REQUIREMENT_CHANGE: 0
ROUTE_D_POST_REVEAL_REQUIREMENT_CHANGE: 0
```

The A1 partial is not counted as source-fact invention. At freeze time both routes faithfully represented the original issue body's claim; later discussion corrected the source packet itself. The unfavorable partial is preserved rather than retroactively rewriting the frozen representations.

## 6. Representation-burden measurement

The committed GitHub objects provide exact stored UTF-8 sizes:

```text
ROUTE_B_STRONG_BASELINE: 1921 bytes
ROUTE_D_DSD_V1_0:       5697 bytes
RATIO_DSD/BASELINE:     2.966
```

Both representations contain six top-level acceptance requirements. DSD therefore did not reduce the requirement count in this case and required materially more representation to carry typed fields, violation/unresolved conditions, layer selection, and guardrails.

This byte-size comparison is a burden proxy only. It is **not** measured reviewer time, authoring time, cognitive load, or defect-prevention benefit.

## 7. Comparative verdict

The precommitted verdict rule yields:

```text
MATERIAL_OUTCOME_COVERAGE_DIFFERENCE: none demonstrated
ERROR_PROFILE_DIFFERENCE: none demonstrated
IMPLEMENTATION_FREEDOM_DIFFERENCE: none demonstrated
TRACEABILITY_STRUCTURE_DIFFERENCE: DSD explicit, but no measured task outcome gain
REPRESENTATION_BURDEN: materially higher for DSD

COMPARATIVE_VERDICT: TIE_WITH_DSD_OVERHEAD
```

This is a valid negative practical result.

For this narrow standalone bug-repair acceptance task, the strong conventional checklist is preferred on economy because it achieved the same externally checked acceptance coverage with substantially less representation.

The DSD record may still have method-family handoff or machine-traceability value, but this benchmark did not measure such a downstream use and therefore does not credit it here.

## 8. Guardrail result

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G2 PURPOSE_AND_PRIORITY_FIDELITY: INSIDE_GUARDRAILS
G3 DETAIL_PROPORTIONALITY: GUARDRAIL_PRESSURE
G4 VIEWPOINT_SEPARATION: INSIDE_GUARDRAILS
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

G3 pressure is supported by the approximately threefold stored representation size without a corresponding measured outcome advantage in the locked task.

This is not a hard failure.

## 9. Evidence interpretation

```text
MEASURED_CASE_LEVEL_REPRESENTATION_RESULT: established
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not demonstrated
GENERAL_MEASURED_PRACTICAL_BENEFIT: not established
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

The result strengthens the method's evidence discipline because a benchmark designed to look for practical gain was allowed to return an unfavorable tie-with-overhead result.

It does **not** justify changing Specification's evidence-maturity status upward by itself.

## 10. Final record

```text
BENCHMARK_ID: SPEC-MEAS-001
METHOD: DSD Specification
PROTOCOL: v1.0
CASE: pytest-dev/pytest#12112
RESOLUTION: merged PR #12169
BASELINE: strong source-derived plain-language acceptance checklist
DSD_ROUTE: DSD Specification v1.0 typed acceptance record

BASELINE_SCORE: 5 MATCH + 1 PARTIAL
DSD_SCORE:      5 MATCH + 1 PARTIAL

BASELINE_UTF8_BYTES: 1921
DSD_UTF8_BYTES: 5697
DSD_TO_BASELINE_BYTE_RATIO: 2.966

COMPARATIVE_VERDICT: TIE_WITH_DSD_OVERHEAD
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
POST_REVEAL_CRITERION_CHANGE: no
POST_REVEAL_REQUIREMENT_CHANGE: no

RESULT:
SPECIFICATION_V1_0_PAIRED_BENCHMARK_TIE_WITH_DSD_OVERHEAD
```
