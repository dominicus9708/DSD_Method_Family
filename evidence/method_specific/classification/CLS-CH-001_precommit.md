# CLS-CH-001 Precommit / DSD 분류론 Positive Direct Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-12**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-CH-001
CASE_CLASS: positive_direct_classification_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Classification Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
METHOD_GAIN_ASSESSMENT: not_permitted_in_this_case
```

Purpose: test whether Protocol v0.1 can produce justified terminal class assignments while preserving claim-relevant Property-status distinctions that a summary-value or label-only classifier could collapse.

This case is not a baseline comparison. `CLASSIFICATION_METHOD_GAIN_STATUS` must remain `NOT_ASSESSED`.

## 2. Frozen task

```text
CLASSIFICATION_TASK_ID: CLS-TASK-001
TASK_SCOPE: classify supplied records by the status of one applicable Property q
CLAIMED_OUTPUT_LEVEL: MEMBERSHIP_ASSIGNMENT
TARGET_RESOLUTION: q-status class only; numeric magnitude/sign inside DEFINED_NONZERO is not a separate class dimension

SUBJECT_SET: {S1,S2,S3,S4}
SUBJECT_ID_POLICY: supplied IDs are immutable within this run

CLASSIFICATION_UNIVERSE U001:
  records for which q is applicable and q-status is exactly one of:
    DEFINED_ZERO
    DEFINED_NONZERO
    APPLICABLE_BUT_UNDEFINED

CLASS_SCHEMA_ID_AND_VERSION: CLS001-SCHEMA-v1
CLASS_SCHEMA_OR_GENERATION_POLICY: fixed supplied schema; no class generation
CLASS_SCHEMA_STATUS: closed
CLASS_LABELS_IF_PREDECLARED: {C-Z,C-N,C-U}
CLASS_RELATION_SEMANTICS: disjoint
MUTUAL_EXCLUSION_RULES: a subject may belong to exactly one of C-Z,C-N,C-U at this target resolution
SCHEMA_COVERAGE_CLAIM: closed_world_claim within U001 only
CLOSED_SCHEMA_CLOSURE_EVIDENCE:
  U001 admits exactly the three frozen q-status states above;
  C-Z, C-N, C-U map one-to-one onto those three statuses;
  no other q-status state is admitted into U001.
```

The closure evidence is fixture-local and definitional. It does not claim that these three states exhaust every possible DSD or external-domain state outside U001.

## 3. Frozen class criteria and decision semantics

```text
CRITERION CZ-1:
  TARGET_CLASS: C-Z
  REQUIRED_FEATURE: q_status
  EVALUATION_RULE: q_status == DEFINED_ZERO

CRITERION CN-1:
  TARGET_CLASS: C-N
  REQUIRED_FEATURE: q_status
  EVALUATION_RULE: q_status == DEFINED_NONZERO

CRITERION CU-1:
  TARGET_CLASS: C-U
  REQUIRED_FEATURE: q_status
  EVALUATION_RULE: q_status == APPLICABLE_BUT_UNDEFINED

CRITERION_SOURCE: frozen challenge fixture
CRITERION_PRECEDENCE_OR_DEPENDENCY: none
CRITERION_COMPOSITION_RULE: one status predicate per class; no cross-class score aggregation
DECISION_RULE:
  if exactly one class predicate is satisfied -> CLASSIFIED_SINGLE with that class;
  if more than one disjoint class predicate is satisfied -> CRITERION_CONFLICT;
  if none is satisfied for a record inside U001 -> UNCLASSIFIED_WITHIN_DECLARED_SCHEMA only after closure check.
```

No ordinary-language meaning may be inferred from class labels `C-Z`, `C-N`, or `C-U`.

## 4. Feature and DSD-interface freeze

```text
FEATURE_BASIS:
  q_status
  q_value_if_defined
  legacy_display_q as supplied distractor/readout only; not a membership criterion

FEATURE_SOURCE_AND_PROVENANCE: frozen subject records in this file
FEATURE_EXTRACTION_OR_MAPPING_RULE:
  read q_status literally;
  read q_value only when q_status is defined;
  do not convert APPLICABLE_BUT_UNDEFINED into numeric zero;
  do not promote legacy_display_q into q_status.

FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY: not_applicable; all fixture statuses are exact supplied records
BOUNDARY_DECISION_SEMANTICS: not_applicable; no numeric threshold defines class membership

TARGET_DSD_LAYER_SCOPE: General Property status/value interface only
DSD_INTERFACE_PROFILE:
  preserve APPLICABLE_BUT_UNDEFINED, DEFINED_ZERO, DEFINED_NONZERO as distinct claim-relevant states
DOMAIN_BRIDGE_IF_ANY: none
EXTERNAL_STANDARD_IF_ANY: none
AUXILIARY_METHODS_OR_HANDOFFS: none
```

The `legacy_display_q` field is intentionally non-authoritative. It exists only to test whether equal display values are mistakenly substituted for typed status.

## 5. Frozen policies

```text
MISSING_INFORMATION_POLICY:
  no missing q_status occurs in the frozen fixture;
  if one did occur, it could not be silently treated as any admitted status.

OUT_OF_SCOPE_POLICY:
  records whose q is not applicable or whose q_status is outside U001 are OUT_OF_SCOPE for this task.

BOUNDARY_CASE_POLICY: not_applicable to frozen fixture
MULTI_LABEL_POLICY: forbidden by disjoint schema
CRITERION_CONFLICT_POLICY: return CRITERION_CONFLICT; no hidden tie-break
BASELINE_IF_GAIN_CLAIM: none
PRECOMMIT_OR_FREEZE_REFERENCE: this file and its Git commit
```

## 6. Frozen subject records

### S1

```text
SUBJECT_ID: S1
q_status: DEFINED_ZERO
q_value: 0
legacy_display_q: 0
```

### S2

```text
SUBJECT_ID: S2
q_status: APPLICABLE_BUT_UNDEFINED
q_value: no numeric value supplied
legacy_display_q: 0
```

S1 and S2 intentionally share the same legacy display value while carrying different claim-relevant Property statuses.

### S3

```text
SUBJECT_ID: S3
q_status: DEFINED_NONZERO
q_value: +7
legacy_display_q: 7
```

### S4

```text
SUBJECT_ID: S4
q_status: DEFINED_NONZERO
q_value: -3
legacy_display_q: -3
```

S3 and S4 intentionally have different defined nonzero values but the same q-status class at the frozen target resolution.

## 7. Frozen expected membership outcomes

These expected outcomes are derived directly from the frozen schema and serve as the challenge oracle. They may not be altered after execution begins.

```text
S1 -> C-Z / CLASSIFIED_SINGLE
S2 -> C-U / CLASSIFIED_SINGLE
S3 -> C-N / CLASSIFIED_SINGLE
S4 -> C-N / CLASSIFIED_SINGLE
```

Additional required distinctions:

```text
S1 and S2:
  legacy_display_q equal
  classification must differ because DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED

S3 and S4:
  q_value differs
  classification may match because target resolution classifies q-status, not numeric sign/magnitude

COMMON_CLASS(S3,S4) != OBJECT_IDENTITY
COMMON_CLASS(S3,S4) != EQUAL_Q_VALUE
```

## 8. Frozen execution checks

The result file must score exactly 36 checks.

### A. Validity gates — 14 checks

One check each for G1 through G14 of Protocol v0.1. A gate that is structurally not applicable must be explicitly recorded as satisfied-by-explicit-nonuse rather than silently omitted.

### B. Subject-level classification — 16 checks

Four checks per subject:

```text
B1 correct class assignment
B2 correct membership status
B3 criterion/decision trace preserved
B4 subject-level protocol conformance = CONFORMANT
```

### C. Global distinction and scope checks — 6 checks

```text
C1 S1/S2 equal legacy display does not collapse their classes
C2 S2 APPLICABLE_BUT_UNDEFINED is not coerced to DEFINED_ZERO
C3 S3/S4 different numeric values may share C-N at the frozen target resolution
C4 common class is not upgraded to object identity, common cause, or equal value
C5 no label meaning, hidden criterion, bridge, transformation, lineage, diagnosis, or audit verdict is introduced
C6 method gain remains NOT_ASSESSED because no competent baseline is frozen
```

```text
TOTAL_FROZEN_CHECKS: 36
PASS_THRESHOLD: 36/36
PARTIAL_PASS_POLICY: none; any failed frozen check is recorded as challenge failure or protocol defect candidate according to the failed condition
```

## 9. Anti-post-hoc rule

After this precommit is committed, execution may not modify:

```text
subject records
classification universe
schema/version
class relations
criteria
composition/decision rule
feature-status semantics
expected outputs
check count
pass threshold
```

If execution exposes a protocol-level semantic defect, the result must preserve the failure. The protocol must not be rewritten first and then the same run relabelled as a pass.

## 10. Evidence interpretation limit

A 36/36 pass would establish only that Protocol v0.1 handled this constructed positive direct classification case as frozen.

It would **not** establish:

```text
general superiority
independent validation
independent replication
external-domain validity
permanent method irreducibility
method survival/merger/absorption/deletion
```
