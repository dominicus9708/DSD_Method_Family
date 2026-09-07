# SPEC-MEAS-003 — Repeated-Use Carrier Benchmark Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Benchmark rule: `PRACTICAL_BENCHMARK_RULE_v0.1.md`
Status: PRECOMMITTED_BEFORE_ROUTE_CARRIER_CONSTRUCTION_AND_SCORING

## 1. Purpose

Test whether the structural handoff advantage previously observed in `SPEC-LINK-001` becomes a genuine repeated-use advantage when the same requirement set is applied to multiple downstream DSD Audit targets.

This benchmark explicitly allows a strong conventional baseline to create and retain its own reusable criterion sheet. It therefore does **not** assume that a non-DSD reviewer must re-read or re-extract OSHA source material on every run.

The benchmark is designed to falsify the simplistic claim:

```text
DSD_TYPED_CARRIER_EXISTS
=> DSD_AUTOMATICALLY_WINS_ON_REUSE
```

## 2. Locked source basis

Use only the already locked requirement families from:

- `SPEC-APP-003_OSHA_EAP_core_guidance.md`
- `SPEC-LINK-001_specification-to-audit-handoff.md`

No new OSHA requirement family may be added after the route carriers are created.

## 3. Routes

### ROUTE_B — strong reusable conventional carrier

Create one plain-language reusable criterion sheet containing the same six locked probe families used in `SPEC-LINK-001`.

The carrier may contain:

```text
criterion ID
source reference
mandatory / optional character
plain-language pass/fail/open rule
```

It may be retained and reused across all downstream targets.

It must not use DSD-specific field names or layer/status vocabulary.

### ROUTE_D — DSD Specification v1.0 reusable carrier

Create one DSD v1.0 criterion carrier for the same six probe families.

It may use the v1.0 typed fields and openness/validation structure only where claim-relevant.

It is retained and reused across all downstream targets.

## 4. Locked probe families

```text
P1 REPORTING_PROCEDURE
P2 EMPLOYEE_ACCOUNTABILITY
P3 DISTINCTIVE_ALARM_SIGNAL
P4 PLAN_CHANGE_REVIEW_TRIGGER
P5 OPTIONAL_AUXILIARY_POWER_GUIDANCE
P6 EXACT_ASSEMBLY_POINT_SITE_DETAIL
```

Locked normative semantics:

```text
P1 required
P2 required
P3 required
P4 required
P5 optional / no regulatory failure from absence by itself
P6 site-specific/open at this review resolution; absence of an exact value is not by itself a failure
```

## 5. Locked downstream target matrix

Four constructed EAP snapshots are used only as repeated downstream audit targets.

### TARGET_A — all required families addressed

```text
P1 present
P2 present
P3 distinctive signal present
P4 plan-change review present
P5 auxiliary-power recommendation absent
P6 exact assembly point not supplied
```

Expected findings:

```text
P1 addressed
P2 addressed
P3 addressed
P4 addressed
P5 non-failure
P6 non-failure/open
TOTAL_REQUIRED_FAILURES: 0
```

### TARGET_B — accountability and alarm failures

```text
P1 present
P2 absent
P3 one undifferentiated alarm signal
P4 plan-change review present
P5 auxiliary-power recommendation absent
P6 exact assembly point not supplied
```

Expected findings:

```text
P1 addressed
P2 omission
P3 finding
P4 addressed
P5 non-failure
P6 non-failure/open
TOTAL_REQUIRED_FAILURES: 2
```

### TARGET_C — review-trigger omission only

```text
P1 present
P2 present
P3 distinctive signal present
P4 plan-change review absent
P5 auxiliary-power recommendation absent
P6 exact assembly point not supplied
```

Expected findings:

```text
P1 addressed
P2 addressed
P3 addressed
P4 omission
P5 non-failure
P6 non-failure/open
TOTAL_REQUIRED_FAILURES: 1
```

### TARGET_D — reporting omission only

```text
P1 absent
P2 present
P3 distinctive signal present
P4 plan-change review present
P5 auxiliary-power recommendation present
P6 exact assembly point not supplied
```

Expected findings:

```text
P1 omission
P2 addressed
P3 addressed
P4 addressed
P5 non-failure
P6 non-failure/open
TOTAL_REQUIRED_FAILURES: 1
```

## 6. Locked reuse accounting

Each route gets one upfront carrier construction and then four downstream uses.

The strong baseline is allowed to persist its carrier after construction.

Record:

```text
NUMBER_OF_DOWNSTREAM_USES: 4
UPFRONT_CARRIER_CONSTRUCTIONS_PER_ROUTE: 1
REBUILD_OR_REEXTRACTION_COUNT_AFTER_FIRST_CARRIER_PER_ROUTE:
CARRIER_REUSE_COUNT_PER_ROUTE:
HANDOFF_RETRANSLATION_REQUIRED_PER_USE:
```

A baseline route must not be forced to rebuild criteria if its frozen conventional carrier is sufficient.

## 7. Required result vector

Per `PRACTICAL_BENCHMARK_RULE_v0.1.md`, report:

```text
OUTCOME_ACCURACY_AXIS:
ERROR_OR_FALSE_POSITIVE_AXIS:
SOURCE_FIDELITY_AXIS:
EXTERNAL_STANDARD_BOUNDARY_AXIS:
STRUCTURAL_HANDOFF_AXIS:
REPRESENTATION_BURDEN_AXIS:
MEASURED_WORKLOAD_OR_TIME_AXIS:
REUSE_AXIS:
INDEPENDENCE_AXIS:
```

## 8. Representation burden

Use exact GitHub UTF-8 byte size of the two frozen route-carrier files as a representation proxy.

This is not human-time or cognitive-load measurement.

Also record top-level criterion count for both routes.

## 9. Outcome scoring

There are `4 targets × 6 probes = 24` probe outcomes.

Record exact matches against the locked target matrix:

```text
ROUTE_B_PROBE_MATCHES: x/24
ROUTE_D_PROBE_MATCHES: x/24
FALSE_REQUIRED_FAILURES:
MISSED_REQUIRED_FAILURES:
FALSE_FAILURE_ON_OPTIONAL_P5:
FALSE_FAILURE_ON_OPEN_P6:
```

## 10. Reuse scoring

The reuse axis is determined independently of representation burden.

```text
DSD_REUSE_ADVANTAGE
```
may be claimed only if Route D demonstrates fewer actual rebuild/retranslation events across the four downstream uses than the strong persistent baseline.

If both frozen carriers can be reused without reconstruction, record:

```text
REUSE_AXIS: tie
```

even if DSD has stronger typed handoff structure.

## 11. Structural-handoff scoring

DSD may receive a structural-handoff advantage if its carrier natively exposes receiving-Audit fields such as source reference, normative force, activation, violation trigger, and openness without a separate mapping layer.

The baseline may still retain its own plain-language carrier.

Therefore:

```text
STRUCTURAL_HANDOFF_ADVANTAGE
!= REUSE_ADVANTAGE
!= MEASURED_TIME_ADVANTAGE
```

## 12. Scalar winner

```text
SCALAR_WINNER_REQUIRED: no
```

The final result is multidimensional.

Allowed overall summary labels:

```text
DSD_ADVANTAGE_ON_ONE_OR_MORE_AXES
BASELINE_ADVANTAGE_ON_ONE_OR_MORE_AXES
MIXED_RESULT
TIE
NO_GAIN
INDETERMINATE
```

Use `MIXED_RESULT` if different routes win different measured axes without a precommitted scalar priority.

## 13. Independence and limits

```text
INDEPENDENT_EVALUATOR: no
MEASURED_HUMAN_TIME: no
MEASURED_COGNITIVE_LOAD: no
MEASURED_ENGINEERING_PRODUCTIVITY: no
```

This benchmark tests repeated carrier reuse under one fixed requirement family. It is not external independent validation and does not establish general practical superiority.
