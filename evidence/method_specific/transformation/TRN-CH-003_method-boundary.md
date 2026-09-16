# TRN-CH-003 — Direct Transformation Method-Boundary Challenge Result

Status: **EXECUTED — 60/60 PASS**  
Date: **2026-09-16**  
Case ID: `TRN-CH-003`  
Case class: `direct_method_boundary_constructed_transformation`  
Case origin: `constructed_internal`  
Evidence scope class: `method_specific`  
Protocol: **Transformation Protocol v0.1**  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Precommit commit: `677a3c021dd32360c1aa999ad1f936d327b3624c`  
Precommit blob: `e80db5aea586ca6bdb2e13ceab842b1faa06ef09`

## 1. Execution discipline

Execution used only the seven frozen constructed pairings and the five precommitted exact-collapse axes:

```text
A1 REQUIRED_INPUT_CONTRACT
A2 PRIMARY_OPERATION
A3 PRIMARY_OUTPUT_CONTRACT
A4 FAILURE_OR_LIMIT_SEMANTICS
A5 VALIDATION_STANDARD
```

No external material was introduced. No neighboring method was protected from exact collapse by definition. Shared artifacts, formulas, values, or handoffs were treated as overlap evidence only.

## 2. M1 — Transformation vs Design

```text
A1 INPUT
Transformation: supplied source + already declared target schema + explicit map
Design: goals/constraints from which a target structure is proposed or selected
DIFFERENT

A2 OPERATION
Transformation: apply declared map/bridge to supplied source representation
Design: construct/select target structure satisfying goals/constraints
DIFFERENT

A3 OUTPUT
Transformation: target record + carrier preservation/loss/addition/reversibility ledger
Design: design specification / target architecture / constraint rationale
DIFFERENT

A4 FAILURE/LIMIT
Transformation: map inapplicability, missing bridge, loss, unresolved map/version
Design: infeasible or underdetermined design relative to goals/constraints
DIFFERENT

A5 VALIDATION
Transformation: map conformance + carrier/status/loss/reconstruction discipline
Design: design/constraint satisfaction and declared design-validation criteria
DIFFERENT
```

Both can reference `ARCHIVE_V2`, but the same target artifact does not erase the operation boundary.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 3. M2 — Transformation vs Synthesis

```text
A1 INPUT
Transformation: C1/C2 records + source/target schemas + explicit schema map
Synthesis: supplied parts/components + composition/compatibility rules
DIFFERENT

A2 OPERATION
Transformation: map each representation into CONFIG_B
Synthesis: combine supplied parts into a composite configuration
DIFFERENT

A3 OUTPUT
Transformation: mapped records + preservation/loss provenance
Synthesis: composed structure + composition/compatibility record
DIFFERENT

A4 FAILURE/LIMIT
Transformation: map/domain/bridge/loss limitations
Synthesis: incompatible parts, failed composition, unresolved closure/dependency
DIFFERENT

A5 VALIDATION
Transformation: mapping and preservation-ledger conformance
Synthesis: composition-rule and composite-structure conformance
DIFFERENT
```

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 4. M3 — Transformation vs Aggregation

Frozen shared values were `v=(2,3,5)`.

```text
A1 INPUT
Transformation: source representation + declared target representation + map
Aggregation: component states + aggregation/readout rule
DIFFERENT

A2 OPERATION
Transformation: map carriers to target carriers or, if declared, map to an aggregate target while recording merge/loss semantics
Aggregation: combine/reduce components into aggregate/readout
PARTIAL OVERLAP, NOT IDENTICAL CONTRACT

A3 OUTPUT
Transformation: target representation + carrier relation/loss/reconstruction ledger
Aggregation: aggregate/readout such as sum=10 + aggregation metadata
DIFFERENT

A4 FAILURE/LIMIT
Transformation: inapplicable map, hidden collision/loss, unsupported reconstruction
Aggregation: invalid/inapplicable aggregation rule or unsupported aggregate claim
DIFFERENT

A5 VALIDATION
Transformation: map/ledger/reconstruction conformance
Aggregation: aggregate-rule correctness and readout semantics
DIFFERENT
```

A sum can be encoded as a transformation target, but the Transformation task must still classify many-to-one loss while Aggregation's primary task is the aggregate/readout itself.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 5. M4 — Transformation vs Compression

```text
A1 INPUT
Transformation: source/target schemas + frozen map/bridge
Compression: source representation + size/rate/reconstruction/error objective
DIFFERENT

A2 OPERATION
Transformation: apply declared representation change
Compression: reduce/encode representation under compression objective
PARTIAL OVERLAP, NOT IDENTICAL CONTRACT

A3 OUTPUT
Transformation: target representation + preservation/loss/reversibility ledger
Compression: compressed representation + reconstruction/error/size metrics or guarantees
DIFFERENT

A4 FAILURE/LIMIT
Transformation: loss may be conformant if explicitly declared
Compression: failure may be inability to satisfy reconstruction/error/rate objective
DIFFERENT

A5 VALIDATION
Transformation: declared-map and preservation/loss conformance
Compression: compression objective, reconstruction, and error-budget conformance
DIFFERENT
```

Lossiness alone does not make a transformation a Compression task.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 6. M5 — Transformation vs Comparison

```text
A1 INPUT
Transformation: record A + S_A/S_B + map A_to_Bschema
Comparison: at least two supplied subjects/representations + correspondence policy
DIFFERENT

A2 OPERATION
Transformation: map A into S_B to produce A'
Comparison: compare A' with B across declared comparison axes
DIFFERENT

A3 OUTPUT
Transformation: A' + preservation/loss ledger
Comparison: correspondence/divergence/equivalence profile
DIFFERENT

A4 FAILURE/LIMIT
Transformation: map applicability/loss/reconstruction limits
Comparison: incomparability, unresolved correspondence, insufficient common resolution
DIFFERENT

A5 VALIDATION
Transformation: map and ledger conformance
Comparison: correspondence/equivalence/divergence decision traceability
DIFFERENT
```

The transformed record may be handed to Comparison, but that handoff does not collapse the methods.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 7. M6 — Transformation vs Interpretation

Frozen shared material included `X7`, explicit bridge `X7 -> ZONE_7`, and surrounding context.

```text
A1 INPUT
Transformation: source token + explicit frozen codebook bridge + declared target representation
Interpretation: source/context + relevant bridge(s) + candidate reading/support question
DIFFERENT

A2 OPERATION
Transformation: apply the explicit bridge to emit canonical token
Interpretation: evaluate which reading(s) are supported and at what claim strength
DIFFERENT

A3 OUTPUT
Transformation: ZONE_7 + bridge/provenance/preservation record
Interpretation: supported/unsupported/ambiguous/blocked reading status + evidential support
DIFFERENT

A4 FAILURE/LIMIT
Transformation: missing/inapplicable bridge or unresolved map identity
Interpretation: ambiguity, underdetermination, unsupported reading, blocked interpretation, scope limit
DIFFERENT

A5 VALIDATION
Transformation: bridge/map conformance and provenance
Interpretation: source-grounded support and claim-strength discipline
DIFFERENT
```

Applying an already frozen semantic codebook can be a Transformation operation; deciding what a source supports in context remains an Interpretation operation.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 8. M7 — Transformation vs Computation

The shared arithmetic was `25.00 C -> 298.15 K` under `K=C+273.15`.

```text
A1 INPUT
Transformation: formal value + source/target carrier identities + schemas + map + status/provenance obligations
Computation: formal input + formula/rule sufficient to calculate result
PARTIAL OVERLAP, NOT IDENTICAL CONTRACT

A2 OPERATION
Transformation: execute mapped representation change, which may internally compute 298.15
Computation: evaluate formula to obtain 298.15
PARTIAL OVERLAP, NOT IDENTICAL CONTRACT

A3 OUTPUT
Transformation: target carrier value + equivalence/relation/provenance/reconstruction/reversibility record
Computation: computed formal result 298.15 and computation trace as required
DIFFERENT

A4 FAILURE/LIMIT
Transformation: source/target/map applicability, status collapse, reconstruction/reversibility limits
Computation: undefined operation, invalid formal input, rule/evaluation failure
DIFFERENT

A5 VALIDATION
Transformation: map/typing/status/preservation/reconstruction conformance
Computation: formal rule application and result correctness
DIFFERENT
```

The same arithmetic is shared, but the required output and validation contracts are not identical.

```text
BOUNDARY_RELATION: PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 9. Boundary summary

```text
Design         -> PARTIAL_OVERLAP_NOT_COLLAPSE
Synthesis      -> PARTIAL_OVERLAP_NOT_COLLAPSE
Aggregation    -> PARTIAL_OVERLAP_NOT_COLLAPSE
Compression    -> PARTIAL_OVERLAP_NOT_COLLAPSE
Comparison     -> PARTIAL_OVERLAP_NOT_COLLAPSE
Interpretation -> PARTIAL_OVERLAP_NOT_COLLAPSE
Computation    -> PARTIAL_OVERLAP_NOT_COLLAPSE

EXACT_COLLAPSE_CANDIDATES_FOUND: 0/7
INSUFFICIENT_BOUNDARY_JUDGMENTS: 0/7
```

The result is fixture-bounded. It does not prove permanent irreducibility or forbid future merger/refactoring if later evidence changes the interfaces.

## 10. Preserved boundary guards

```text
SHARED_ARTIFACT != SAME_METHOD
SHARED_FORMULA != SAME_METHOD
SHARED_TARGET_RECORD != SAME_METHOD
HANDOFF_COMPATIBILITY != METHOD_COLLAPSE
SAME_NUMERIC_RESULT != SAME_OUTPUT_CONTRACT
TRANSFORMATION_LEDGER != NEIGHBORING_METHOD_OUTPUT_BY_DEFAULT
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
BOUNDARY_DIFFERENCE != PERMANENT_IRREDUCIBILITY
```

## 11. Precommitted scoring

```text
A. Freeze / anti-bias discipline:          11/11 PASS
B. Seven pairwise boundary evaluations:   42/42 PASS
C. Cross-boundary and scope discipline:     7/7 PASS

PRECOMMITTED_REQUIRED_CHECKS: 60
PASSED: 60
FAILED: 0
TOTAL: 60/60 PASS
```

No scoring rule was added, removed, or weakened after execution.

## 12. Protocol and scope result

```text
TRANSFORMATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
EXTERNAL_APPLICATION: no
INDEPENDENT_VALIDATION: not established
```

No frozen contradiction or missing core boundary rule was exposed by this fixture.

## 13. Evidence accounting

This case increments only the direct method-boundary lane:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 3
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 3
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
METHOD_BOUNDARY_TRANSFORMATION_CASES: 1
```

Unchanged:

```text
BASELINE_TRANSFORMATION_CASES: 0
NO_GAIN_TRANSFORMATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
```

## 14. Bounded conclusion

`TRN-CH-003` shows that, in the frozen constructed seven-pair fixture, Transformation shares artifacts or suboperations with Design, Synthesis, Aggregation, Compression, Comparison, Interpretation, and Computation without meeting the precommitted five-axis exact-collapse criterion for any pair.

This does not establish permanent method-registry survival, universal irreducibility, practical superiority, external applicability, or independent validation.

## 15. Next

Precommit and execute a fair competent-baseline Transformation challenge. The baseline must receive the same source/target/map/status/loss/reconstruction information and must be allowed to match DSD Transformation exactly; `NO_GAIN` remains an acceptable outcome. External validation remains deferred.