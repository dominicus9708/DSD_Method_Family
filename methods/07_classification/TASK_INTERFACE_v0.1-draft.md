# DSD Classification Task Interface v0.1 Draft

Status: **draft / pre-protocol**  
Date: **2026-09-12**

## 1. Task identity

```text
METHOD: DSD Classification / DSD 분류론
TASK_INTERFACE_VERSION: v0.1-draft
CLASSIFICATION_TASK_ID:
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
TARGET_RESOLUTION:
```

The task interface defines what information must be frozen before an executable Classification protocol can issue a class-membership claim.

## 2. Required supplied inputs

```text
SUBJECT_SET:
SUBJECT_ID_POLICY:
CLASSIFICATION_UNIVERSE:
CLASS_SCHEMA_OR_GENERATION_POLICY:
CLASS_SCHEMA_STATUS: closed | open | partially_open | externally_fixed
CLASS_LABELS_IF_PREDECLARED:
CLASS_CRITERIA:
CRITERION_SOURCE:
CRITERION_PRECEDENCE_OR_DEPENDENCY:
FEATURE_BASIS:
FEATURE_SOURCE_AND_PROVENANCE:
FEATURE_EXTRACTION_OR_MAPPING_RULE:
TARGET_DSD_LAYER_SCOPE:
DSD_INTERFACE_PROFILE:
DOMAIN_BRIDGE_IF_ANY:
EXTERNAL_STANDARD_IF_ANY:
MISSING_INFORMATION_POLICY:
OUT_OF_SCOPE_POLICY:
BOUNDARY_CASE_POLICY:
MULTI_LABEL_POLICY:
CRITERION_CONFLICT_POLICY:
BASELINE_IF_GAIN_CLAIM:
PRECOMMIT_OR_FREEZE_REFERENCE:
```

The method must not manufacture a missing criterion, feature, class boundary, bridge, or domain standard merely to force a terminal assignment.

## 3. Conditional inputs

### 3.1 Equivalence-class claims

Required only when the output claims equivalence classes:

```text
EQUIVALENCE_RELATION_OR_CRITERION:
REFLEXIVITY_CHECK_SCOPE:
SYMMETRY_CHECK_SCOPE:
TRANSITIVITY_CHECK_SCOPE:
EQUIVALENCE_COVERAGE:
```

Pairwise similarity or one successful correspondence map is not sufficient to assert an equivalence class.

### 3.2 Hierarchy or partial-order claims

Required only when classes are arranged as a hierarchy or partial order:

```text
ORDER_RELATION:
REFLEXIVITY_CHECK_SCOPE:
ANTISYMMETRY_CHECK_SCOPE:
TRANSITIVITY_CHECK_SCOPE:
HIERARCHY_EDGE_PROVENANCE:
```

Ordered names, levels, severity words, or numeric labels do not establish a mathematical order relation.

### 3.3 Aggregate-based classification

Required only when aggregate/readout values enter the criterion:

```text
AGGREGATE_DEFINITION:
AGGREGATE_SUPPORT:
INFORMATION_LOSS_CHECK:
COLLISION_POLICY:
INJECTIVITY_OR_RECONSTRUCTION_CLAIM_IF_ANY:
```

Equal aggregates alone cannot establish equal structural class when distinct component states can collide under the readout.

### 3.4 Time-dependent classification

Required only when class membership depends on time or transition history:

```text
TIME_OR_ORDER_DOMAIN:
REGULAR_EPOCH_SCOPE:
CLASS_EVALUATION_TIME:
CLASS_TRANSITION_RULE:
LINEAGE_REQUIREMENT:
HISTORY_DEPENDENCE_POLICY:
```

A change in class assignment is not automatically a formation-level identity change, and similar class trajectories do not establish lineage identity.

### 3.5 Multi-label or overlapping classes

Required only when simultaneous membership is permitted:

```text
MULTI_MEMBERSHIP_SEMANTICS:
OVERLAP_ALLOWED:
MUTUAL_EXCLUSION_RULES:
PRIORITY_RULE_IF_ANY:
```

Multiple memberships are not treated as contradictory unless the declared class semantics make them mutually exclusive.

## 4. DSD activation rules

### Formation
Use when classification depends on formation stages, admitted channels, assignment state, absence, definedness, or composition structure.

### General Property
Use when classification depends on typed property applicability, prerequisites, partial assignment, defined zero/nonzero, or higher-order property records.

### Static Aggregation
Use only if a declared criterion explicitly uses an aggregate/readout. Record information loss and possible collisions.

### Dynamics
Use only if membership depends on time-indexed states, regular evolution, transitions, residuals, propagation, or lineage.

### Optional specialization
Use only when the class criterion explicitly requires the specialization. The specialization cannot be imported merely because another DSD method used it.

## 5. Classification operation

The pre-protocol operation is provisionally decomposed as:

```text
C1  lock task, resolution, subjects, class schema, and criterion sources
C2  preserve subject identity and claim-relevant DSD statuses/types
C3  derive or read only declared class-relevant features through explicit mappings
C4  evaluate criterion applicability and prerequisite satisfaction
C5  evaluate membership criterion-by-criterion without label-based inference
C6  resolve permitted overlap, precedence, dependency, or conflict using supplied rules
C7  issue terminal or nonterminal membership status
C8  record boundary, missing-information, and out-of-scope cases separately
C9  validate any equivalence/hierarchy/aggregate/dynamic special claim under its extra obligations
C10 record provenance, limits, baseline comparison, and reproducibility information
```

These step labels are provisional until boundary attacks determine whether they are sufficient.

## 6. Terminal and nonterminal membership statuses

The draft permits the following status family:

```text
CLASSIFIED_SINGLE
CLASSIFIED_MULTI
BOUNDARY_CASE
UNDERDETERMINED
UNCLASSIFIED_WITHIN_DECLARED_SCHEMA
OUT_OF_SCOPE
CRITERION_CONFLICT
BLOCKED_BY_MISSING_BRIDGE_OR_INFORMATION
```

`UNCLASSIFIED_WITHIN_DECLARED_SCHEMA` is meaningful only when the declared schema and coverage justify that statement. In an open class universe, absence of a current matching class does not become a universal nonmembership claim.

## 7. Required outputs

```text
CLASSIFICATION_RESULT_ID:
CLASSIFICATION_TASK_ID:
SUBJECT_ID:
APPLICABLE_CLASS_SCHEMA:
CLASS_ASSIGNMENT_OR_ASSIGNMENTS:
MEMBERSHIP_STATUS:
CRITERIA_SATISFIED:
CRITERIA_NOT_SATISFIED:
CRITERIA_UNRESOLVED:
FEATURES_USED_WITH_PROVENANCE:
BRIDGES_USED:
BOUNDARY_RECORD:
MISSING_INFORMATION_RECORD:
OUT_OF_SCOPE_RECORD:
CONFLICT_RECORD:
INFORMATION_LOSS_CHECK:
TEMPORAL_OR_LINEAGE_RECORD_IF_ANY:
JUSTIFICATION_TRACE:
BASELINE_RESULT_IF_ANY:
NO_GAIN_STATUS_IF_ANY:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## 8. Failure and no-gain conditions

The following are candidate failure conditions for later protocolization:

- a claim-relevant class criterion has no declared source or semantics;
- a class assignment requires an undeclared feature or hidden bridge;
- missing, undefined, inapplicable, absent, or zero states are collapsed contrary to the activated DSD interface;
- class membership is inferred from the class name or label rather than the criterion;
- the declared closed schema does not cover the claimed search space;
- a hierarchy/equivalence relation is asserted without satisfying its declared relation obligations;
- an aggregate collision is ignored in a structural-class claim;
- time-dependent membership is evaluated without a declared time/order scope;
- an open-world case is falsely converted into universal nonmembership;
- conflicting criteria are silently resolved without a supplied precedence/dependency rule;
- another method's output is silently treated as Classification's final verdict.

`NO_GAIN` is separate from method failure. If a competent baseline produces the same justified classifications under the same locked inputs and with no claim-relevant loss, the correct result may be `CLASSIFICATION_NO_GAIN` rather than forced superiority.

## 9. Method boundaries

```text
ANALYSIS_OUTPUT != CLASSIFICATION_ASSIGNMENT
COMPARISON_RELATION != CLASS_MEMBERSHIP_UNLESS_CRITERION_USES_IT
SPECIFICATION_REQUIREMENT != CLASSIFICATION_CRITERION_BY_DEFAULT
INTERPRETIVE_READING != CLASS_MEMBERSHIP_BY_DEFAULT
DIAGNOSIS_HYPOTHESIS != CLASS_ASSIGNMENT
AGGREGATE_VALUE != STRUCTURAL_CLASS
PREDICTION != CURRENT_CLASSIFICATION
```

A multi-method case may contain several of these outputs, but every handoff must preserve source method, output status, and any transformation/bridge used before Classification consumes it.

## 10. Pre-protocol questions for attack stage

The boundary-attack stage must test at least:

1. overlapping but nonexclusive classes;
2. mutually exclusive classes with conflicting evidence;
3. open-world class registries;
4. missing versus negative features;
5. undefined versus defined-zero features;
6. aggregate collisions;
7. misleading class labels;
8. equivalence claims from incomplete pairwise tests;
9. false hierarchy from ordinal-looking labels;
10. time-dependent class change without identity change;
11. identical current class with different lineage/history;
12. subject outside the classification universe;
13. class-generation policy that creates new classes during the run;
14. criterion precedence/dependency conflicts;
15. multi-method input provenance loss;
16. competent-baseline `NO_GAIN` conditions.

## 11. Current status

This draft is infrastructure only. It does not count as direct Classification evidence and does not establish that the proposed method is mature, superior, irreducible, or permanently independent.