# TRN-CH-003 — Direct Transformation Method-Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-16**  
Case ID: `TRN-CH-003`  
Case class: `direct_method_boundary_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Audited method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Purpose

Test whether Transformation remains operationally distinguishable from seven neighboring methods when artifacts, maps, formulas, target records, or intermediate values overlap.

The challenge does **not** assume that overlap implies separation or collapse. Exact method collapse is permitted as an outcome if the frozen comparison axes become identical.

Neighboring methods:

```text
Design
Synthesis
Aggregation
Compression
Comparison
Interpretation
Computation
```

No external source, standard, benchmark, or evaluator is used.

## 2. Frozen exact-collapse criterion

For each pair, compare these five method axes:

```text
A1 REQUIRED_INPUT_CONTRACT
A2 PRIMARY_OPERATION
A3 PRIMARY_OUTPUT_CONTRACT
A4 FAILURE_OR_LIMIT_SEMANTICS
A5 VALIDATION_STANDARD
```

Boundary relation labels are frozen as:

```text
EXACT_COLLAPSE
PARTIAL_OVERLAP_NOT_COLLAPSE
HANDOFF_ONLY
INSUFFICIENT_FOR_BOUNDARY_JUDGMENT
```

`EXACT_COLLAPSE` requires all five claim-relevant axes to be operationally identical at the frozen task scope. Shared data, shared formulas, or equal endpoint values alone are insufficient.

Required guards:

```text
SHARED_ARTIFACT != SAME_METHOD
SHARED_FORMULA != SAME_METHOD
SHARED_TARGET_RECORD != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
SAME_NUMERIC_RESULT != SAME_OUTPUT_CONTRACT
TRANSFORMATION_LEDGER != NEIGHBORING_METHOD_OUTPUT_BY_DEFAULT
```

## 3. M1 — Transformation vs Design

Shared material:

```text
existing target schema: ARCHIVE_V2
existing source schema: SENSOR_V1
```

Transformation task:

```text
apply frozen MAP_SENSOR_ARCHIVE 1.0 to supplied SENSOR_V1 record
emit ARCHIVE_V2 record + carrier preservation/loss/provenance ledger
```

Design task:

```text
given goals and constraints, propose or choose a target archive structure
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

Reason to test: both may mention the same target schema, but Transformation consumes an already declared target and map whereas Design produces or selects a target structure from goals/constraints.

## 4. M2 — Transformation vs Synthesis

Shared material:

```text
two supplied component configuration records C1 and C2
```

Transformation task:

```text
map C1 and C2 separately from CONFIG_A schema into CONFIG_B schema
preserve per-carrier relation/loss/addition provenance
```

Synthesis task:

```text
compose C1 and C2 into one declared composite configuration under compatibility/composition rules
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 5. M3 — Transformation vs Aggregation

Shared source values:

```text
v = (2,3,5)
```

Transformation task T3:

```text
map vector positions to named target carriers {a=2,b=3,c=5}
carrier relation: one-to-one
```

Aggregation task A3:

```text
compute aggregate readout sum(v)=10
```

Additional overlap stress:

A transformation map **could** be declared as `{2,3,5} -> total=10`; if so, Transformation must classify the relation/loss semantics, while Aggregation's primary output remains the aggregate/readout under its aggregation rule.

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 6. M4 — Transformation vs Compression

Shared material:

```text
source representation R_LONG
reduced representation R_SHORT
```

Transformation task:

```text
apply a frozen source-to-target encoding map and report preservation/loss/reconstruction status
```

Compression task:

```text
produce or assess a reduced representation under an explicit size/rate/reconstruction/error objective
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

A lossy transformation is not automatically compression, and a compression output may be handed to Transformation without merging the methods.

## 7. M5 — Transformation vs Comparison

Shared material:

```text
record A in schema S_A
record B in schema S_B
map A_to_Bschema 1.0
```

Transformation task:

```text
map A into schema S_B and emit transformed A' plus preservation/loss ledger
```

Comparison task:

```text
compare supplied A' and B and emit correspondence/divergence profile
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 8. M6 — Transformation vs Interpretation

Shared material:

```text
source token X7
explicit frozen codebook bridge X7 -> ZONE_7
surrounding source context also available
```

Transformation task:

```text
apply the explicit codebook bridge to produce canonical token ZONE_7
record bridge identity and transformation provenance
```

Interpretation task:

```text
evaluate which reading(s) the source/context supports and at what claim strength
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

The explicit bridge may be an input to Interpretation, but applying a frozen bridge is not by itself the full source-grounded reading task.

## 9. M7 — Transformation vs Computation

Shared material:

```text
temperature_c = 25.00
formula: K = C + 273.15
```

Computation task:

```text
compute numeric result 298.15
```

Transformation task:

```text
map source carrier temperature_c in source schema to temperature_k in target schema
emit value 298.15 plus declared-equivalence, carrier relation, provenance, reconstruction, and reversibility records
```

Frozen expected relation:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

The same arithmetic may occur inside both methods, but arithmetic equality alone does not make the output contracts identical.

## 10. Frozen cross-boundary decision rules

For each pair:

```text
if all A1-A5 identical -> EXACT_COLLAPSE
if one or more claim-relevant axes differ while artifacts/operations partially overlap -> PARTIAL_OVERLAP_NOT_COLLAPSE
if neighboring method only consumes/produces typed handoff without shared primary operation -> HANDOFF_ONLY
if task information cannot determine axes -> INSUFFICIENT_FOR_BOUNDARY_JUDGMENT
```

No pair may be forced to `PARTIAL_OVERLAP_NOT_COLLAPSE` merely to preserve the registry.

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
BOUNDARY_DIFFERENCE != PERMANENT_IRREDUCIBILITY
```

## 11. Precommitted scoring — 60 checks

### A. Freeze / anti-bias discipline — 11 checks

1. Protocol v0.1 identity/blob remains unchanged.
2. Seven neighboring methods are fixed before execution.
3. Five exact-collapse axes A1-A5 are fixed before execution.
4. Four boundary relation labels are fixed before execution.
5. Shared-artifact overlap is not itself counted as method equality.
6. Shared formula overlap is not itself counted as method equality.
7. Equal endpoint values are not themselves counted as method equality.
8. No method is protected from an `EXACT_COLLAPSE` result by definition.
9. No registry-survival conclusion is permitted from a boundary PASS.
10. No external evidence is introduced.
11. No criterion is weakened or added after execution.

### B. Seven pairwise boundary evaluations — 42 checks

For each of M1-M7, six checks must pass:

```text
P1 required input contract compared explicitly
P2 primary operation compared explicitly
P3 primary output contract compared explicitly
P4 failure/limit semantics compared explicitly
P5 validation standard compared explicitly
P6 boundary relation emitted from A1-A5 rather than artifact coincidence
```

This yields:

```text
M1 Design:         6 checks
M2 Synthesis:      6 checks
M3 Aggregation:    6 checks
M4 Compression:    6 checks
M5 Comparison:     6 checks
M6 Interpretation: 6 checks
M7 Computation:    6 checks
TOTAL:            42 checks
```

### C. Cross-boundary and scope discipline — 7 checks

54. exact-collapse candidate count is reported explicitly.
55. any pair with overlap but axis difference is not mislabeled exact collapse.
56. handoff compatibility is not treated as collapse.
57. method gain remains NOT_ASSESSED.
58. method-boundary result does not increment baseline/NO_GAIN/reproducibility/external counters.
59. protocol/shared-core revision is required only if a frozen contradiction or missing core boundary rule is exposed.
60. conclusion remains limited to this constructed seven-pair fixture.

```text
PRECOMMITTED_REQUIRED_CHECKS: 60
```

## 12. Evidence-count lock

If the case passes, increment only:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED +1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS +1
METHOD_BOUNDARY_TRANSFORMATION_CASES +1
```

Do not increment baseline, NO_GAIN, reproducibility, external-application, or independent-validation counters.

A PASS does not establish permanent irreducibility, superiority, external applicability, or independent validation.