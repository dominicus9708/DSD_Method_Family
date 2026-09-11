# DSD Classification Task Interface Boundary Amendment 001

Status: **pre-protocol amendment / infrastructure, not direct evidence**  
Date: **2026-09-12**  
Applies to: `TASK_INTERFACE_v0.1-draft.md`  
Forced by: `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`

## 1. Amendment rule / 개정 원칙

The historical Task Interface v0.1 draft is preserved unchanged.

This amendment adds only obligations forced by the pre-protocol boundary attacks. It does not retroactively count as a direct Classification pilot and does not promote method maturity.

```text
HISTORICAL_DRAFT: preserved
BREAKING_REWRITE: no
NONBREAKING_REFINEMENT_GROUPS: 6
DIRECT_EVIDENCE_INCREMENT: 0
```

## 2. Required additions to the general task record

Add the following fields before an executable classification run may issue a terminal membership claim:

```text
CLASS_SCHEMA_ID_AND_VERSION:
CLASS_RELATION_SEMANTICS:
MUTUAL_EXCLUSION_RULES:
SCHEMA_COVERAGE_CLAIM:
CLOSED_SCHEMA_CLOSURE_EVIDENCE:
CRITERION_COMPOSITION_RULE:
DECISION_RULE:
FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY:
BOUNDARY_DECISION_SEMANTICS:
```

### 2.1 Class relation semantics

`CLASS_RELATION_SEMANTICS` must state any claim-relevant relation among classes, including as applicable:

```text
disjoint
overlapping
subsumption_or_refinement
ordered_by_declared_relation
independent
externally_fixed_relation
unspecified
```

`MUTUAL_EXCLUSION_RULES` is no longer conditional on multi-label permission. Exclusive-class conflicts can exist even when the task permits only one final label.

### 2.2 Schema identity and coverage

`CLASS_SCHEMA_ID_AND_VERSION` locks the classification frame used for a run.

`SCHEMA_COVERAGE_CLAIM` must distinguish at least:

```text
open_world_no_exhaustiveness_claim
partial_coverage_claim
closed_world_claim
externally_fixed_scope_only
```

A `closed_world_claim` requires `CLOSED_SCHEMA_CLOSURE_EVIDENCE` sufficient for the target resolution. Merely labelling a schema `closed` does not establish exhaustive coverage.

```text
SCHEMA_STATUS_CLOSED
!= CLOSED_WORLD_COVERAGE_ESTABLISHED
```

## 3. Criterion-composition amendment

The original draft records criteria, precedence, and dependencies. Amendment 001 adds the missing operation that converts criterion evaluations into membership.

```text
CRITERION_COMPOSITION_RULE:
DECISION_RULE:
```

The composition rule may be, when explicitly supplied:

```text
conjunction
disjunction
k_of_n
veto_rule
weighted_threshold
ordered_rule_set
externally_fixed_decision_procedure
other_explicit_rule
```

The protocol must not infer a composition rule merely from criterion order, labels, or formatting.

```text
CRITERION_LIST
!= MEMBERSHIP_LOGIC
```

## 4. Generated-class amendment

Required only when `CLASS_SCHEMA_OR_GENERATION_POLICY` permits new classes during or as a result of the run:

```text
GENERATED_CLASS_PROVENANCE:
CLASS_GENERATION_FREEZE_OR_MUTATION_POLICY:
GENERATION_STOP_OR_CLOSURE_POLICY:
```

A generated class must record at minimum:

```text
GENERATED_CLASS_ID
PARENT_SCHEMA_ID_AND_VERSION
TRIGGERING_SUBJECT_OR_FEATURE_PATTERN
GENERATION_RULE_USED
GENERATION_TIME_OR_ORDER
NEW_SCHEMA_ID_AND_VERSION
```

If the run mutates the schema, later assignments must identify which schema version evaluated them.

```text
PRE_GENERATION_SCHEMA
!= POST_GENERATION_SCHEMA
```

## 5. Equivalence-class amendment

When equivalence classes are claimed, add:

```text
EQUIVALENCE_CLOSURE_REQUIREMENT:
```

This must specify the relation/domain coverage needed before an equivalence class is terminal. Pairwise successes do not substitute for the declared reflexive/symmetric/transitive closure obligation.

## 6. Boundary and uncertainty amendment

When class membership depends on measured, estimated, extracted, probabilistic, interval-valued, or otherwise uncertain features, add:

```text
FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY:
BOUNDARY_DECISION_SEMANTICS:
```

The policy must state how a feature interval or uncertainty region intersecting a class boundary is handled. Allowed terminal/nonterminal outcomes may include:

```text
CLASSIFIED_SINGLE
CLASSIFIED_MULTI
BOUNDARY_CASE
UNDERDETERMINED
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
```

A central estimate alone cannot be used to force membership when the frozen uncertainty/tolerance rule does not justify it.

## 7. Revised pre-protocol operation

The provisional operation is amended to:

```text
C1  lock task, target resolution, subjects, schema identity/version, schema status, and coverage claim
C2  lock class-relation semantics and any mutual-exclusion rules
C3  preserve subject identity and claim-relevant DSD statuses/types
C4  derive or read only declared class-relevant features through explicit mappings and provenance
C5  apply uncertainty/tolerance policy where claim-relevant
C6  evaluate criterion applicability and prerequisites
C7  evaluate each criterion without label-based inference
C8  combine criterion results only through the frozen composition/decision rule
C9  resolve permitted overlap, exclusion, precedence, dependency, or conflict through supplied rules
C10 issue terminal or nonterminal membership status
C11 record boundary, missing-information, open-world no-match, and out-of-scope cases separately
C12 validate equivalence/hierarchy/aggregate/dynamic special claims under their extra closure obligations
C13 if class generation is permitted, record schema mutation/provenance and re-identify the active schema version
C14 record provenance, limits, baseline comparison, and reproducibility information
```

These steps become binding only when incorporated into an executable protocol.

## 8. Additional validity gates for Protocol v0.1

The first executable protocol must fail, block, or remain underdetermined rather than issue a terminal class assignment when any required condition below is unmet:

```text
G1 schema identity/version is claim-relevant but not frozen
G2 class exclusivity/overlap semantics are required but absent
G3 closed-world nonmembership is claimed without closure evidence
G4 criteria exist but membership-composition logic is absent
G5 generated classes are used without generation provenance/schema-version transition
G6 equivalence-class closure is claimed without the frozen closure requirement
G7 an uncertainty region intersects a decision boundary and no boundary rule resolves it
```

## 9. Status after Amendment 001

```text
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved
BOUNDARY_ATTACKS: 18 completed
BOUNDARY_AMENDMENT_001: established
DEDICATED_CLASSIFICATION_PROTOCOL: not yet established
DIRECT_CLASSIFICATION_PILOTS: 0
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: pre_validation
```

## 10. Next / 다음

Integrate `TASK_INTERFACE_v0.1-draft.md` plus this amendment into an executable `PROTOCOL_v0.1.md`. The protocol must encode terminal/nonterminal states and validity gates without converting protocol construction into direct evidence.