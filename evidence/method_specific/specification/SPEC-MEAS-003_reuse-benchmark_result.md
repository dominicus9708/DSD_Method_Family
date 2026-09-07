# SPEC-MEAS-003 — Repeated-Use Carrier Benchmark Result

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Benchmark rule: `PRACTICAL_BENCHMARK_RULE_v0.1.md`
Precommit commit: `14d6a8d827de9b890ff40cf3bf740ce26a63a218`
Frozen conventional carrier commit: `9c328e88c9922229164e8b30848d1c067f8e8ba9`
Frozen DSD carrier commit: `bd67e02a1d2e482125792b8a659b5cf7e2a65c89`
Status: COMPLETED

## 1. Result in one line

Across four repeated downstream EAP audit targets, both the strong reusable conventional carrier and the DSD Specification v1.0 carrier produced all 24 locked probe outcomes correctly and both were reusable without source re-extraction after their initial construction. DSD retained a native structural-handoff advantage, while the conventional carrier used substantially less representation. The repeated-use axis itself was a tie.

```text
OVERALL_SUMMARY: MIXED_RESULT

OUTCOME_ACCURACY_AXIS: tie
ERROR_OR_FALSE_POSITIVE_AXIS: tie
SOURCE_FIDELITY_AXIS: tie
EXTERNAL_STANDARD_BOUNDARY_AXIS: tie
STRUCTURAL_HANDOFF_AXIS: DSD_ADVANTAGE
REPRESENTATION_BURDEN_AXIS: BASELINE_ADVANTAGE
MEASURED_WORKLOAD_OR_TIME_AXIS: not_measured
REUSE_AXIS: tie
INDEPENDENCE_AXIS: same_project_not_independent
```

## 2. Frozen carriers

### Route B — strong reusable conventional carrier

```text
FILE: SPEC-MEAS-003_reuse-baseline-carrier.md
GITHUB_UTF8_BYTES: 2653
TOP_LEVEL_CRITERIA: 6
PERSISTENT_REUSE_ALLOWED: yes
```

### Route D — DSD v1.0 reusable carrier

```text
FILE: SPEC-MEAS-003_reuse-dsd-carrier.md
GITHUB_UTF8_BYTES: 5146
TOP_LEVEL_CRITERIA: 6
PERSISTENT_REUSE_ALLOWED: yes
```

Representation ratio:

```text
DSD_TO_BASELINE_BYTE_RATIO: 1.940
```

The byte ratio is only a representation proxy. It is not a measurement of human review time, cognitive load, engineering effort, or error probability.

## 3. Downstream-use matrix

Four target snapshots were precommitted.

### TARGET_A

```text
P1 addressed
P2 addressed
P3 addressed
P4 addressed
P5 non-failure
P6 non-failure/open
```

Both routes: `6/6` exact.

### TARGET_B

```text
P1 addressed
P2 omission
P3 finding
P4 addressed
P5 non-failure
P6 non-failure/open
```

Both routes: `6/6` exact.

### TARGET_C

```text
P1 addressed
P2 addressed
P3 addressed
P4 omission
P5 non-failure
P6 non-failure/open
```

Both routes: `6/6` exact.

### TARGET_D

```text
P1 omission
P2 addressed
P3 addressed
P4 addressed
P5 non-failure
P6 non-failure/open
```

Both routes: `6/6` exact.

## 4. Accuracy and error result

```text
ROUTE_B_PROBE_MATCHES: 24/24
ROUTE_D_PROBE_MATCHES: 24/24

ROUTE_B_FALSE_REQUIRED_FAILURES: 0
ROUTE_D_FALSE_REQUIRED_FAILURES: 0

ROUTE_B_MISSED_REQUIRED_FAILURES: 0
ROUTE_D_MISSED_REQUIRED_FAILURES: 0

ROUTE_B_FALSE_FAILURE_ON_OPTIONAL_P5: 0
ROUTE_D_FALSE_FAILURE_ON_OPTIONAL_P5: 0

ROUTE_B_FALSE_FAILURE_ON_OPEN_P6: 0
ROUTE_D_FALSE_FAILURE_ON_OPEN_P6: 0

OUTCOME_ACCURACY_AXIS: tie
ERROR_OR_FALSE_POSITIVE_AXIS: tie
```

No positive DSD accuracy claim is supported by this run.

## 5. Reuse accounting

The benchmark intentionally allowed the conventional baseline to persist its carrier.

```text
NUMBER_OF_DOWNSTREAM_USES: 4

ROUTE_B_UPFRONT_CARRIER_CONSTRUCTIONS: 1
ROUTE_D_UPFRONT_CARRIER_CONSTRUCTIONS: 1

ROUTE_B_SOURCE_REEXTRACTIONS_AFTER_CARRIER_FREEZE: 0
ROUTE_D_SOURCE_REEXTRACTIONS_AFTER_CARRIER_FREEZE: 0

ROUTE_B_CARRIER_REUSE_COUNT: 4
ROUTE_D_CARRIER_REUSE_COUNT: 4

REUSE_AXIS: tie
```

This directly falsifies the simplistic claim that a DSD typed carrier automatically produces a repeated-use advantage merely because it can be reused.

A well-constructed conventional carrier can also be reused.

## 6. Structural handoff

The two reusable artifacts differ in receiving-method interface structure.

Route B carries:

```text
criterion ID
source reference
normative character
plain-language decision rule
```

Route D natively exposes fields already aligned with DSD Audit consumption:

```text
SOURCE_REFERENCE
REQUIRED_OR_OPTIONAL
ACTIVATION_CONDITION
VIOLATION_CONDITION
SOURCE_OPENNESS_STATUS when active
DOWNSTREAM_DETERMINACY_STATUS when active
```

Accordingly:

```text
ROUTE_B_INITIAL_DSD_AUDIT_MAPPING_LAYER_REQUIRED: yes
ROUTE_D_INITIAL_DSD_AUDIT_MAPPING_LAYER_REQUIRED: no

ROUTE_B_REPEATED_SOURCE_REEXTRACTION_AFTER_MAPPING: no
ROUTE_D_REPEATED_SOURCE_REEXTRACTION_AFTER_MAPPING: no

STRUCTURAL_HANDOFF_AXIS: DSD_ADVANTAGE
```

This is a structural interface result only.

It is not converted into measured time or productivity gain.

## 7. Representation burden

```text
ROUTE_B_UTF8_BYTES: 2653
ROUTE_D_UTF8_BYTES: 5146
DSD_TO_BASELINE_BYTE_RATIO: 1.940
TOP_LEVEL_CRITERIA: 6 vs 6

REPRESENTATION_BURDEN_AXIS: BASELINE_ADVANTAGE
```

The DSD record uses more text to carry typed activation, violation, unresolved, and openness semantics.

On this six-criterion benchmark, that extra structure did not improve downstream classification accuracy or the number of reusable executions.

## 8. Source and external-standard boundaries

Both carriers preserve the locked normative split:

```text
P1-P4 required
P5 optional / absence not regulatory failure under locked probe
P6 site-specific/open / exact value not fabricated
```

Neither carrier replaces OSHA as external authority.

```text
ROUTE_B_SOURCE_FACT_INVENTION: 0
ROUTE_D_SOURCE_FACT_INVENTION: 0
ROUTE_B_EXTERNAL_STANDARD_REPLACEMENT: 0
ROUTE_D_EXTERNAL_STANDARD_REPLACEMENT: 0

SOURCE_FIDELITY_AXIS: tie
EXTERNAL_STANDARD_BOUNDARY_AXIS: tie
```

## 9. Measured workload / time

No human timing instrumentation was available.

```text
MEASURED_AUTHORING_TIME: not_measured
MEASURED_REVIEW_TIME: not_measured
MEASURED_COGNITIVE_LOAD: not_measured
MEASURED_ENGINEERING_PRODUCTIVITY: not_measured

MEASURED_WORKLOAD_OR_TIME_AXIS: not_measured
```

No break-even point in minutes or labor can be claimed.

## 10. Independence

```text
INDEPENDENT_EVALUATOR: no
SAME_PROJECT_EVALUATOR: yes
INDEPENDENCE_AXIS: same_project_not_independent
```

This is a constructed repeated-use benchmark grounded in an external OSHA requirement corpus. It is not independent evaluator evidence.

## 11. Multidimensional verdict

Under `PRACTICAL_BENCHMARK_RULE_v0.1.md`, no scalar winner is required.

```text
OUTCOME_ACCURACY_AXIS:              tie
ERROR_OR_FALSE_POSITIVE_AXIS:       tie
SOURCE_FIDELITY_AXIS:               tie
EXTERNAL_STANDARD_BOUNDARY_AXIS:    tie
STRUCTURAL_HANDOFF_AXIS:            DSD_ADVANTAGE
REPRESENTATION_BURDEN_AXIS:         BASELINE_ADVANTAGE
MEASURED_WORKLOAD_OR_TIME_AXIS:      not_measured
REUSE_AXIS:                         tie
INDEPENDENCE_AXIS:                  same_project_not_independent

OVERALL_SUMMARY: MIXED_RESULT
```

This is more informative than forcing either `DSD_PREFERRED` or `BASELINE_PREFERRED`.

## 12. Interpretation

The benchmark changes the interpretation of the earlier reuse hypothesis.

Supported:

```text
DSD_SPECIFICATION_CAN_PROVIDE_NATIVE_AUDIT_INTERFACE: yes
DSD_CARRIER_CAN_BE_REUSED_ACROSS_MULTIPLE_AUDITS: yes
CONVENTIONAL_STRONG_CARRIER_CAN_ALSO_BE_REUSED: yes
DSD_REUSE_COUNT_ADVANTAGE: no
DSD_NATIVE_HANDOFF_ADVANTAGE: yes
BASELINE_REPRESENTATION_ECONOMY_ADVANTAGE: yes
```

Not supported:

```text
REPEATED_USE_ALONE_MAKES_DSD_PREFERRED
MEASURED_TIME_SAVING
MEASURED_TOTAL_WORK_REDUCTION
MEASURED_ERROR_REDUCTION
GENERAL_BREAK_EVEN_POINT
```

The likely practical value of DSD Specification therefore remains conditional: typed native handoff is a real structural property, but it does not automatically dominate a competent reusable conventional criterion artifact.

## 13. Guardrail result

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G2 PURPOSE_AND_PRIORITY_FIDELITY: INSIDE_GUARDRAILS
G3 DETAIL_PROPORTIONALITY: GUARDRAIL_PRESSURE
G4 VIEWPOINT_SEPARATION: INSIDE_GUARDRAILS
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

G3 pressure follows from approximately 1.94x representation size without accuracy or reuse-count gain on the locked task.

## 14. Final record

```text
BENCHMARK_ID: SPEC-MEAS-003
NUMBER_OF_DOWNSTREAM_USES: 4
TOTAL_PROBES_PER_ROUTE: 24
ROUTE_B_PROBE_MATCHES: 24/24
ROUTE_D_PROBE_MATCHES: 24/24
ROUTE_B_REEXTRACTIONS_AFTER_FREEZE: 0
ROUTE_D_REEXTRACTIONS_AFTER_FREEZE: 0
ROUTE_B_REUSE_COUNT: 4
ROUTE_D_REUSE_COUNT: 4
ROUTE_B_BYTES: 2653
ROUTE_D_BYTES: 5146
DSD_TO_BASELINE_BYTE_RATIO: 1.940
STRUCTURAL_HANDOFF_AXIS: DSD_ADVANTAGE
REPRESENTATION_BURDEN_AXIS: BASELINE_ADVANTAGE
REUSE_AXIS: tie
OVERALL_SUMMARY: MIXED_RESULT

RESULT:
SPECIFICATION_V1_0_REPEATED_USE_MIXED_RESULT_NATIVE_HANDOFF_WITHOUT_REUSE_COUNT_ADVANTAGE
```
