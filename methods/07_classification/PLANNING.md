# DSD Classification Planning / DSD 분류론 기획

Status: **Protocol v0.1 frozen / CLS-CH-001~005 PASS / CLS-CH-004~005 NO_GAIN / first external application next**  
Date opened: **2026-09-12**

## Purpose / 목적

Develop **DSD Classification / DSD 분류론** as an independent method under **Field I. Structural Description & Understanding**.

Classification receives one or more supplied subjects together with a declared classification scope, class schema or class-generation policy, class-relevant criteria, feature provenance, and any required DSD/domain bridge. It returns criterion-traceable class assignments, boundary or underdetermined cases, and class-relation structure without inferring mathematical or semantic properties from labels alone.

Classification may consume outputs from Analysis, Comparison, Interpretation, Specification, Diagnosis, Aggregation, Dynamics, Provenance/Lineage, and other methods only through explicit handoffs. Their verdicts are not silently converted into membership claims.

## Core methodological rules / 핵심 방법 규칙

```text
CLASS_LABEL != CLASS_CRITERION
SUMMARY_COINCIDENCE != STRUCTURAL_CLASS_IDENTITY
PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP
ORDERED_LABELS != PROVEN_PARTIAL_ORDER
CURRENT_CLASS_MATCH != TEMPORAL_LINEAGE_IDENTITY
MISSING_FEATURE != NEGATIVE_FEATURE
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != UNCLASSIFIED
BOUNDARY_CASE != CLASSIFICATION_FAILURE
MULTI_CLASS_MEMBERSHIP != CRITERION_CONFLICT
SCHEMA_STATUS_CLOSED != CLOSED_WORLD_COVERAGE_ESTABLISHED
CRITERION_LIST != MEMBERSHIP_LOGIC
PRE_GENERATION_SCHEMA != POST_GENERATION_SCHEMA
NO_CURRENT_MATCH_IN_OPEN_SCHEMA != UNIVERSAL_NONMEMBERSHIP
AGGREGATE_EQUALITY != STRUCTURAL_CLASS_IDENTITY
NO_GAIN != METHOD_ABSORPTION_PROOF
```

A classification claim is valid only relative to a declared task resolution, criterion set, class-schema semantics, schema identity/version, evidence/provenance basis, membership decision rule, and claim-relevant closure/bridge record.

## Development sequence / 개발 순서

1. ✅ Classification-specific Task Interface v0.1 draft.
2. ✅ Pre-protocol boundary attacks: 18 cases.
3. ✅ Boundary Amendment 001: 6 non-breaking refinement groups.
4. ✅ Executable Classification Protocol v0.1 frozen.
5. ✅ Positive direct challenge — `CLS-CH-001`, 36/36 PASS.
6. ✅ Negative/failure-terminal challenge — `CLS-CH-002`, 50/50 PASS.
7. ✅ Direct method-boundary challenge — `CLS-CH-003`, 48/48 PASS.
8. ✅ Competent-baseline challenge — `CLS-CH-004`, 50/50 PASS / `NO_GAIN`.
9. ✅ Strongest-reasonable-baseline comparison — `CLS-CH-005`, 60/60 PASS / `NO_GAIN`.
10. ⬜ First external application.
11. ⬜ Deterministic same-project retrace.
12. ⬜ Additional materially different external domains.
13. ⬜ Maturity audit under frozen axes.
14. ⬜ Independent-evaluator infrastructure only if the accumulated evidence warrants it.

## Boundary-attack result / 경계 공격 결과

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
NONBREAKING_REFINEMENT_GROUPS: 6
```

Amendment 001 added:

```text
R1 CLASS_RELATION_SEMANTICS + MUTUAL_EXCLUSION_RULES
R2 CLASS_SCHEMA_ID_AND_VERSION + SCHEMA_COVERAGE_CLAIM + CLOSED_SCHEMA_CLOSURE_EVIDENCE
R3 EQUIVALENCE_CLOSURE_REQUIREMENT
R4 GENERATED_CLASS_PROVENANCE + CLASS_GENERATION_FREEZE_OR_MUTATION_POLICY + GENERATION_STOP_OR_CLOSURE_POLICY
R5 CRITERION_COMPOSITION_RULE + DECISION_RULE
R6 FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY + BOUNDARY_DECISION_SEMANTICS
```

Historical task-interface and amendment records remain unchanged.

## Protocol v0.1 / 실행 프로토콜

`PROTOCOL_v0.1.md` prospectively integrates the Task Interface and Amendment 001 and freezes schema/version and coverage semantics, class relation/overlap/exclusion semantics, criterion applicability/provenance/composition/decision rules, feature status/provenance and uncertainty/boundary handling, generated-class provenance/schema mutation, special obligations for equivalence/hierarchy/aggregation/time dependence/multi-label output, membership-status vocabulary, validity gates G1-G14, operation sequence C1-C14, protocol-conformance ledger, method-gain ledger, and reproducibility record.

Membership statuses remain:

```text
CLASSIFIED_SINGLE
CLASSIFIED_MULTI
BOUNDARY_CASE
UNDERDETERMINED
UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OUT_OF_SCOPE
CRITERION_CONFLICT
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
OPEN_WORLD_NO_CURRENT_MATCH
```

## Direct constructed evidence / 직접 구성 증거

```text
CLS-CH-001  36/36 PASS
CLS-CH-002  50/50 PASS
CLS-CH-003  48/48 PASS
CLS-CH-004  50/50 PASS / NO_GAIN
CLS-CH-005  60/60 PASS / NO_GAIN
```

`CLS-CH-001` established one constructed typed-status classification case. `CLS-CH-002` preserved seven distinct non-positive result states. `CLS-CH-003` tested the Classification boundary against Analysis, Comparison, Specification, and Diagnosis and found four local `PARTIAL_OVERLAP_NOT_COLLAPSE` results with no exact-collapse candidate in the frozen tasks.

### CLS-CH-004 — competent baseline

```text
PRECOMMIT_COMMIT: 737761726107b67d2dc66da3559d69f11c1d91d6
PRECOMMIT_BLOB: 9e5f3cb2c32ac2be3fc7b9880cdb56231e2baac1
RESULT_COMMIT: 61f938e541153b441f913d32cd2dc95f596eb16d
BASELINE: B0_TYPED_RULE_CLASSIFIER
CLASSIFICATION_METHOD_GAIN_STATUS: NO_GAIN
SCORE: 50/50 PASS
PROTOCOL_REVISION_REQUIRED: no
```

The competent baseline matched DSD on typed status, legitimate multi-membership, open-world no-match, uncertainty-boundary handling, missing-bridge blockage, and retraceability when given the same semantics.

### CLS-CH-005 — strongest-reasonable baseline

Precommit and result:

```text
PRECOMMIT_COMMIT: cbe3ef209dd1434e2b2f7973753071ef6087d31e
PRECOMMIT_BLOB: 507f41efae1e0788ecc321f06239247269d10374
RESULT_COMMIT: 929810d333fefee81841348a492ca3963f80d7ce
BASELINE: B1_STRONG_TYPED_CLASSIFICATION_ENGINE
```

The stronger task family covered:

```text
R1 generated class + schema v1->v2 + no retroactive membership
R2 veto + k-of-n criterion composition
R3 aggregate collision + noninjectivity + reconstruction limit
R4 history-dependent temporal class + lineage separation
R5 equivalence-class closure + non-authoritative similarity rejection
```

DSD and B1 matched on every frozen task-level result. Gain evaluation:

```text
G1 SCHEMA_VERSION_AND_GENERATION_GAIN: NOT_ESTABLISHED
G2 CRITERION_COMPOSITION_GAIN: NOT_ESTABLISHED
G3 AGGREGATE_INFORMATION_LOSS_GAIN: NOT_ESTABLISHED
G4 TEMPORAL_HISTORY_AND_LINEAGE_SEPARATION_GAIN: NOT_ESTABLISHED
G5 EQUIVALENCE_CLOSURE_GAIN: NOT_ESTABLISHED
G6 STATUS_SCHEMA_AND_RELATION_TRACE_GAIN: NOT_ESTABLISHED
G7 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED

CLASSIFICATION_METHOD_GAIN_STATUS: NO_GAIN
SCORE: 60/60 PASS
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The constructed strongest-baseline result shows only that a strong equally informed non-DSD engine can match the frozen Classification outputs and discipline. It does not establish method redundancy, failure, absorption, merger, or deletion.

## Evidence discipline / 증거 규율

- Task-interface, boundary attack, amendment, and protocol construction are infrastructure, not direct method evidence.
- Constructed challenges, external applications, reproducibility evidence, and maturity audits remain separate evidence classes.
- PASS, FAIL, `NO_GAIN`, boundary, and underdetermined results remain evidence and do not vote on method survival.
- Shared-core support does not automatically validate Classification.
- External case origin does not imply independent evaluator validation.
- Same-project retrace does not imply independent replication.
- A baseline must receive the same claim-relevant task information as the DSD run.

## Current status / 현재 상태

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18 completed
BOUNDARY_AMENDMENT_001: established
DIRECT_CLASSIFICATION_PILOTS: 5
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 1
NO_GAIN_CLASSIFICATION_CASES: 2
BASELINE_CLASSIFICATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Next / 다음

Precommit and execute `CLS-APP-001`, the first external Classification application. It must use a stable public source that supplies an externally anchored class schema or criterion and a real source-backed subject record. The project must not invent both the classes and the evidence. Source/version provenance, external-domain correctness, and DSD protocol conformance must be recorded on separate ledgers.
