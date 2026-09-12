# DSD Classification Planning / DSD 분류론 기획

Status: **Protocol v0.1 frozen / CLS-CH-001 and CLS-CH-002 PASS / method-boundary challenge next**  
Date opened: **2026-09-12**

## Purpose / 목적

Develop **DSD Classification / DSD 분류론** as an independent method under **Field I: Structural Description & Understanding**.

Classification receives one or more supplied subjects together with a declared classification scope, class schema or class-generation policy, class-relevant criteria, feature provenance, and any required DSD/domain bridge. It returns criterion-traceable class assignments, boundary or underdetermined cases, and class-relation structure without inferring mathematical or semantic properties from labels alone.

The method is distinct from:

- **DSD Analysis**: decomposes and structurally re-expresses one target;
- **DSD Comparison**: evaluates correspondence/divergence between supplied subjects under a comparison relation or map family;
- **DSD Interpretation**: forms source/context-dependent interpretive readings;
- **DSD Specification**: states requirements/status distinctions rather than assigning subjects to classes;
- **DSD Diagnosis**: infers candidate causes or latent states from observations.

Classification may consume outputs from these methods, but their verdicts are not silently converted into class membership.

## Core methodological rule / 핵심 방법 규칙

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
```

A classification claim is valid only relative to a declared task resolution, criterion set, class-schema semantics, schema identity/version, evidence/provenance basis, and membership decision rule.

## Development sequence / 개발 순서

1. ✅ Classification-specific Task Interface v0.1 draft.
2. ✅ Pre-protocol boundary attacks: 18 cases.
3. ✅ Boundary Amendment 001: 6 non-breaking refinement groups.
4. ✅ Executable Classification Protocol v0.1 frozen.
5. ✅ Positive direct challenge — `CLS-CH-001`, 36/36 PASS.
6. ✅ Negative/failure-terminal challenge — `CLS-CH-002`, 50/50 PASS.
7. ⬜ Direct method-boundary challenge against Analysis / Comparison / Specification / Diagnosis.
8. ⬜ Competent-baseline `NO_GAIN` challenge.
9. ⬜ Strongest-reasonable-baseline comparison.
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

Amendment 001 adds:

```text
R1 class-relation semantics and mutual-exclusion rules
R2 schema identity/version plus coverage/closure evidence
R3 equivalence closure requirement
R4 generated-class provenance and schema-mutation policy
R5 criterion-composition and decision rule
R6 uncertainty/tolerance and boundary-decision semantics
```

The historical task-interface draft remains unchanged. The amendment is additional infrastructure and does not count as direct Classification evidence.

## Protocol v0.1 result / 프로토콜 v0.1 결과

`PROTOCOL_v0.1.md` prospectively integrates the historical Task Interface v0.1 draft and Boundary Amendment 001.

The protocol freezes:

```text
schema identity/version and coverage semantics
class-to-class relation and mutual-exclusion semantics
criterion source, applicability, composition, and decision semantics
feature status/provenance and uncertainty/boundary handling
generated-class provenance and schema mutation
special obligations for equivalence, hierarchy/partial order, aggregation, time dependence, and multi-label results
membership-status vocabulary
validity gates G1-G14
binding operation sequence C1-C14
protocol conformance ledger
method-gain ledger
reproducibility record
protocol versioning rule
```

The membership-status vocabulary is:

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

Protocol v0.1 distinguishes subject/result status from protocol conformance. A boundary, blocked, conflict, open-world-no-match, or underdetermined outcome can be protocol-conformant when it correctly preserves the task limits.

## CLS-CH-001 result / 첫 Positive Direct Challenge

Precommit was frozen before execution:

```text
PRECOMMIT_COMMIT: 2c5944b2830201c8d9bdbbc3d945bb6bfb6f772d
PRECOMMIT_BLOB: 057df677e6337625b53f14c89b4d744a782c468e
RESULT_COMMIT: 8107d13f8b191199c202a324b8362e662ff6ab54
```

The constructed closed schema classified one applicable Property `q` by typed status:

```text
C-Z iff q_status == DEFINED_ZERO
C-N iff q_status == DEFINED_NONZERO
C-U iff q_status == APPLICABLE_BUT_UNDEFINED
```

Frozen subjects intentionally included:

```text
S1 DEFINED_ZERO, q=0, legacy_display=0
S2 APPLICABLE_BUT_UNDEFINED, no q value, legacy_display=0
S3 DEFINED_NONZERO, q=+7
S4 DEFINED_NONZERO, q=-3
```

Execution result:

```text
S1 -> C-Z / CLASSIFIED_SINGLE
S2 -> C-U / CLASSIFIED_SINGLE
S3 -> C-N / CLASSIFIED_SINGLE
S4 -> C-N / CLASSIFIED_SINGLE

VALIDITY_GATES: 14/14 PASS
SUBJECT_LEVEL_CHECKS: 16/16 PASS
GLOBAL_DISTINCTION_CHECKS: 6/6 PASS
TOTAL: 36/36 PASS
PROTOCOL_CONFORMANCE: CONFORMANT for all subject results
CLASSIFICATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED_BY_THIS_CASE: no
```

This directly preserves `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED` even when a non-authoritative display field collides, while also preserving that two different values may share a class at a coarser frozen target resolution. One constructed pass does not establish general superiority or external validity.

## CLS-CH-002 result / Negative-Failure Terminal Challenge

The seven-task challenge was frozen before execution:

```text
PRECOMMIT_COMMIT: eef7ea276186c382953c3b207ffa6c7dc237f603
PRECOMMIT_BLOB: a15719f5b7aebaf3b8df5c05f94f9b4f319ff464
RESULT_COMMIT: ba9ef338c95912ebec14d89f944ad54a640b7686
```

Execution preserved the following status matrix:

```text
N1 -> BOUNDARY_CASE
N2 -> UNDERDETERMINED
N3 -> CRITERION_CONFLICT
N4 -> BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
N5 -> OUT_OF_SCOPE
N6 -> OPEN_WORLD_NO_CURRENT_MATCH
N7 -> UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
```

Score:

```text
VALIDITY_GATES: 14/14 PASS
SEVEN_TASK_CHECKS: 28/28 PASS
CROSS_TASK_DISTINCTION_CHECKS: 8/8 PASS
TOTAL: 50/50 PASS
CLASSIFICATION_METHOD_GAIN_STATUS: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED_BY_THIS_CASE: no
```

The challenge directly established only the constructed-case distinction result. In particular:

```text
BOUNDARY_CASE != UNDERDETERMINED
UNDERDETERMINED != BLOCKED
CRITERION_CONFLICT != CLASSIFIED_MULTI
OUT_OF_SCOPE != CLOSED_WORLD_UNCLASSIFIED
OPEN_WORLD_NO_CURRENT_MATCH != CLOSED_WORLD_UNCLASSIFIED
OPEN_WORLD_NO_CURRENT_MATCH != UNIVERSAL_NONMEMBERSHIP
NONPOSITIVE_RESULT != PROTOCOL_NONCONFORMANCE
```

## Evidence discipline / 증거 규율

- Task-interface, boundary attack, amendment, and protocol construction are infrastructure, not direct method evidence.
- Constructed challenges, external applications, reproducibility evidence, and maturity audits remain separate evidence classes.
- A PASS, FAIL, `NO_GAIN`, boundary result, or underdetermined result does **not** decide method survival, merger, absorption, or deletion.
- Shared-core support does not directly validate Classification.
- External origin does not imply independent-evaluator validation.
- Same-project retrace does not imply independent replication.
- A classification baseline must receive the same frozen task, schema/version, criterion source, membership logic, and claim-relevant information as the DSD run.

## DSD layer use / DSD 층위 사용

Classification activates only the layers required by the task:

- **Formation** when channel/state admission, absence, undefinedness, or composition status is class-relevant;
- **General Property** when typed applicability, prerequisites, definedness, or property values are class-relevant;
- **Static Aggregation** only when aggregate descriptors are explicitly part of the criterion, with collision/information-loss checks;
- **Dynamics** when classification depends on time-indexed state, transition class, or lineage;
- **Optional specializations** only when explicitly required by the class criterion.

No unused DSD layer is activated merely to make the classification record more elaborate.

## Minimum Classification result / 최소 산출물

A Protocol-v0.1 run must record at least:

```text
CLASSIFICATION_TASK_ID
SUBJECT_ID
TASK_SCOPE
TARGET_RESOLUTION
CLASS_SCHEMA_ID_AND_VERSION_USED
SCHEMA_COVERAGE_AND_CLOSURE_RECORD
CLASS_ASSIGNMENT_OR_ASSIGNMENTS
MEMBERSHIP_STATUS
CRITERIA_SATISFIED
CRITERIA_NOT_SATISFIED
CRITERIA_UNRESOLVED
CRITERION_COMPOSITION_RESULT
DECISION_RULE_RESULT
FEATURES_USED_WITH_PROVENANCE
FEATURE_STATUS_RECORD
UNCERTAINTY_OR_BOUNDARY_RECORD
JUSTIFICATION_TRACE
LIMITS
PROTOCOL_CONFORMANCE
REPRODUCIBILITY_RECORD
```

If a hierarchy, equivalence class, partial order, generated class, temporal class transition, aggregate criterion, uncertainty-sensitive boundary, or multi-label result is claimed, its additional obligations must be recorded explicitly.

## Current status / 현재 상태

```text
DEDICATED_CLASSIFICATION_PROTOCOL: established v0.1
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18 completed
BOUNDARY_AMENDMENT_001: established
DIRECT_CLASSIFICATION_PILOTS: 2
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

## Next / 다음

Freeze `CLS-CH-003`, a direct method-boundary challenge, before execution. It should test whether Classification remains operationally distinct from Analysis, Comparison, Specification, and Diagnosis under frozen inputs and outputs, while allowing the evidence to reveal partial overlap or exact collapse if one actually occurs. Any such result must be recorded as a boundary finding, not used as an automatic survival, merger, absorption, or deletion decision.