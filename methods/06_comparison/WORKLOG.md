# DSD Comparison Worklog / DSD 비교론 작업 기록

## 2026-09-10 — Planning Step 1

Status: **planning started / Step 1 complete**

Method path:

```text
methods/06_comparison/
```

Direct-evidence path:

```text
evidence/method_specific/comparison/
```

Initial method form:

```text
supplied subjects
+ comparison scope/resolution
+ supplied map/correspondence family
+ preservation/equivalence criteria
-> correspondence/divergence profile
```

Created `TASK_INTERFACE_v0.1-draft.md` with subject identity/stage/status records, comparison domain, map-family source and coverage, feature/relation/property/status preservation, strict-equivalence criteria, encoding/bridge rules, first-branch search basis, aggregate-collision handling, dynamic-lineage guard, output levels, relation classes, terminal statuses, and three-ledger separation.

---

## 2026-09-10 — Planning Step 2: pre-protocol boundary attack

Created:

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
  commit 37e1ffd925a0f7d7eca88dd12d42a30a53892f57

TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
  commit 131541069f62c481da3098a61446f58d47e31ca7
```

Result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

The five refinement-bearing attacks required four groups:

```text
R1 MAP_PROPERTY_REQUIREMENT_PROFILE
   REVERSE_DIRECTION_OR_INVERSE_POLICY
R2 COMPARISON_ELEMENT_COVERAGE
   CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL
R3 PRECOMPARISON_TRANSFORMATION_POLICY
   REPRESENTATION_PROVENANCE
R4 LINEAGE_IDENTITY_CLAIM_POLICY
   LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

Step-1 draft was preserved unchanged.

---

## 2026-09-10 — Planning Step 4: Protocol v0.1 freeze

Status: **first executable Comparison protocol established**

Created:

```text
methods/06_comparison/PROTOCOL_v0.1.md
commit a1700d960e0b41dfe32bf85b6334448d9104100d
```

Lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Protocol v0.1 freezes a `C1-C20` executable sequence covering:

```text
subjects / claim / scope / target resolution
map-family source / direction / coverage
required map properties and reverse/inverse policy
claim-relevant structural-element coverage
output-level closure requirements
feature/relation/Property/status/equivalence rules
encoding/bridge and precomparison transformation provenance
first-branch search and earlier-stage closure
aggregate collision without structural upgrade
similarity vs lineage-identity separation
terminal / conformance / gain ledgers
limits / handoffs / reproducibility record
```

Key executable guards include:

```text
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
```

Evidence effect:

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
DIRECT_COMPARISON_PILOT_INCREMENT: 0
DIRECT_COMPARISON_PILOTS: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_pending
```

Protocol creation does not validate the method and does not decide method survival, merger, absorption, or deletion.

### Next

Separately precommit `CMP-CH-001` before execution. The first direct positive challenge should jointly test strict equivalence with sufficient closure, weaker direct correspondence, encoded correspondence, aggregate collision without structural inflation, explicit map-property/element-coverage records, and three-ledger separation.
