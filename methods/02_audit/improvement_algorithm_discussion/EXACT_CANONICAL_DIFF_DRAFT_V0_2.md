# Audit — Exact Canonical Diff Draft v0.2

Status: **TEMPORARY / NON-CANONICAL / DO NOT APPLY YET**  
Date: 2026-09-27 KST  
Supersedes temporary draft: `EXACT_CANONICAL_DIFF_DRAFT_V0_1.md`

This revision incorporates:
- final method-boundary audit;
- canonical-path audit;
- template synchronization gap;
- stale Analysis-scope wording found in the dedicated Audit module.

Canonical targets:
- `DSD_Audit/README.md`
- `DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`
- `DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md`
- `DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md`
- `DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md`

Do not mirror these changes into the older root-level audit methodology copies.

## 1. DSD_Audit/README.md — scope synchronization

Current historical wording:

```text
DSD Analysis / DSD 분석론: decomposes, compares, and reinterprets structures.
```

Proposed replacement:

```text
DSD Analysis / DSD 분석론: decomposes and structurally re-expresses one declared target.
Cross-target structural comparison belongs to DSD Comparison, explicit criterion-based class assignment to DSD Classification, and source/context/interpretive-bridge reading to DSD Interpretation.
```

This is a method-boundary synchronization correction.

## 2. GENERAL_AUDIT_FRAMEWORK.md

### 2.1 Position section — Analysis wording

Current:

```text
- Analysis decomposes and compares structures.
```

Proposed:

```text
- Analysis decomposes and structurally re-expresses one declared target.
```

### 2.2 Universal procedure — step 2

Current:

```text
2. Fix scope, time, descriptive resolution, exclusions, and external standard.
```

Proposed:

```text
2. Fix scope, time, descriptive resolution, exclusions, and external standard.
   When intermediate requirements differ materially in locality, uniformity, norm,
   moment, support, aggregation, precision, or another claim-relevant axis,
   record their relation to the already-declared claim and do not force
   incomparable axes into one total resolution order without an explicit
   implication or preservation rule.
```

This does not authorize Audit to create the requirement.
The requirement remains supplied by the source, Specification, or competent external standard.

### 2.3 Universal procedure — step 6

Current:

```text
6. Reconstruct available alternatives.
```

Proposed:

```text
6. Reconstruct available alternatives and, when several routes are material,
   distinguish AND-prerequisites, OR-alternative sufficient routes, theorem/domain
   gates, bridges, attack methods, and supporting work.
```

### 2.4 Universal procedure — step 10

Current:

```text
10. Audit aggregation, information loss, injectivity, and reconstruction claims where used.
```

Proposed:

```text
10. Audit aggregation, information loss, injectivity, and reconstruction claims where used.
    When a route also strengthens an intermediate requirement, record claim-strength
    escalation separately from representation information loss. Equal outputs, a
    shared latent parent, or a one-way bound do not establish claim-relevant
    representation equivalence without an explicit preservation argument.
```

### 2.5 Conditional frontier paragraph after step 12

Add:

```text
When the audited object itself declares an active research, engineering,
procedural, or computational frontier, audit whether reported progress directly
discharges a declared gate, supplies a required bridge/certificate, establishes
a frontier-reducing equivalence, invalidates a route under the locked scope, or
is instead supporting, exploratory, or stronger-but-optional work.

This check audits the accuracy of the progress claim. DSD Audit does not choose
the project's resource allocation or execution priority unless a separate
Operation, Computation, Optimization, or external governance rule is supplied.
Non-frontier status is not a deletion instruction.
```

### 2.6 Core safeguards — add

```text
- A stronger sufficient condition must not be silently promoted into a necessary condition for the audited claim.
- A shared latent object, common source, or equal reduced output must not be promoted into structural equivalence without a claim-relevant preservation argument.
```

## 3. AUDIT_RECORDING_STANDARD.md

### 3.1 Optional claim-requirement subsection after Scope lock

Add:

```text
### 4.1 Optional claim-requirement relation

Use when intermediate requirements materially differ.

DECLARED_CLAIM:
ACTIVE_REQUIREMENT_AXES:
INTERMEDIATE_REQUIREMENT:
RELATION_TO_DECLARED_CLAIM:
IMPLICATION_OR_PRESERVATION_BASIS:

Allowed relation vocabulary:
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED
```

### 3.2 Optional dependency/frontier subsection after Alternative ledger

Add:

```text
### 12.1 Optional dependency/frontier ledger

Use only when several material routes exist or the audited object itself makes a frontier/progress claim.

AND_PREREQUISITES:
OR_SUFFICIENT_ROUTES:
COMMON_MANDATORY_GATES:
MINIMAL_FRONTIER_FAMILIES:
ATTACK_METHODS:
SUPPORTING_WORK:
FROZEN_BRANCHES:
REOPEN_CONDITIONS:
```

### 3.3 Extend Aggregation and reconstruction ledger

Append optional fields:

```text
REPRESENTATION_RELATION:
REPRESENTATION_PRESERVATION_BASIS:
CLAIM_STRENGTH_ESCALATION:
ESCALATION_BASIS:
CLAIM_RELEVANT_INFORMATION_LOSS:
MERGE_OR_DEDUPLICATION_BASIS:
```

Suggested relation vocabulary:

```text
IDENTICAL
BIJECTIVE_EXACT
ISOMETRIC_OR_PARSEVAL_EQUIVALENT
FIXED_WEIGHT_EQUIVALENT
PROJECTION
CONTRACTION
COARSENING
ONE_WAY_BOUND
SIBLING_CONTRACTIONS
INDEPENDENT
UNKNOWN
```

If source-to-target mapping is itself the primary task, Transformation remains the primary method; Audit only checks the performed mapping/claim.

### 3.4 Revision compatibility sentence

Add near the revision section:

```text
The optional fields introduced by later Audit methodology revisions are prospective/additive.
Historical audit records are not invalidated solely because they predate those fields.
```

## 4. AUDIT_ALGORITHMIZATION_ROADMAP.md

### 4.1 Stable input schema

Add optional conditional groups:

```text
claim_requirement_relation
dependency_frontier
representation_relation
escalation_information_loss
branch_state_reopen
gain_set
```

They are not required for every audit.

### 4.2 Phase 2 structural rule engine

Add candidate warning families:

```text
stronger sufficient -> necessary                 [warn without implication basis]
weaker requirement -> sufficient                  [warn without bridge/argument]
incomparable axes -> scalar total order           [warn without ordering rule]
OR alternative -> mandatory AND prerequisite      [warn]
attack method -> theorem/domain gate               [warn]
established-equivalent obligations -> double count [warn]
shared parent -> representation equivalence        [warn without preservation proof]
one-way bound -> equivalence                       [warn]
material claim-strength escalation -> unrecorded   [warn]
claim-relevant information loss -> unrecorded      [warn]
frozen branch -> false/impossible                  [warn]
supporting/exploratory work -> direct closure      [warn]
```

Warnings remain traceable structural messages, not truth verdicts.

### 4.3 Phase 4 pipeline

Proposed extension:

```text
SOURCE LOCK
-> INTERFACE LOCK
-> SCOPE / CLAIM-REQUIREMENT RELATION        [conditional]
-> TYPE/STATUS VALIDATION
-> SELECTION/EXCLUSION CHECK
-> DEPENDENCY / FRONTIER CHECK               [conditional]
-> BRIDGE CHECK
-> REPRESENTATION-RELATION CHECK             [conditional]
-> TRANSITION/LINEAGE CHECK
-> ESCALATION / INFORMATION-LOSS CHECK       [conditional]
-> ALTERNATIVE/WITNESS CHECK
-> AGGREGATION/RECONSTRUCTION CHECK
-> CONTRADICTION CHECK
-> MAXIMUM-SUPPORTED-CLAIM CHECK
-> DOMAIN VERDICT + DSD AUDIT VERDICT
```

Executable invariant certificates remain domain/reproducibility specializations.

## 5. AUDIT_CASE_TEMPLATE.md

Add only optional blocks so ordinary audits do not gain boilerplate.

### 5.1 After Scope

```text
## 3A. Optional claim-requirement relation / 선택: 주장-요구조건 관계

Use only when intermediate requirement strength is material.

DECLARED_CLAIM:
ACTIVE_REQUIREMENT_AXES:
INTERMEDIATE_REQUIREMENT:
RELATION_TO_DECLARED_CLAIM:
IMPLICATION_OR_PRESERVATION_BASIS:
```

### 5.2 After Alternative describabilities

```text
## 11A. Optional dependency/frontier ledger / 선택: 의존성·전선 장부

Use only when several material routes exist or a frontier/progress claim is audited.

AND_PREREQUISITES:
OR_SUFFICIENT_ROUTES:
COMMON_MANDATORY_GATES:
MINIMAL_FRONTIER_FAMILIES:
ATTACK_METHODS:
SUPPORTING_WORK:
FROZEN_BRANCHES:
REOPEN_CONDITIONS:
```

### 5.3 Extend Aggregation and reconstruction block

Append:

```text
REPRESENTATION_RELATION:
REPRESENTATION_PRESERVATION_BASIS:
CLAIM_STRENGTH_ESCALATION:
ESCALATION_BASIS:
CLAIM_RELEVANT_INFORMATION_LOSS:
MERGE_OR_DEDUPLICATION_BASIS:
```

All added template fields are optional and conditional.

## 6. Method-boundary guards

```text
Specification:
  supplies/organizes requirements;
  Audit checks whether work respects them.

Transformation:
  performs source-to-target mapping;
  Audit checks mapping claims when audited.

Computation:
  decides actual evaluation/omission/reuse;
  Audit checks soundness/reporting.

Compression:
  performs deliberate reduction against a purpose;
  Audit checks loss/reconstruction claims.

Operation:
  manages live priority/resources/lifecycle;
  Audit checks declared progress or process claims.
```

## 7. Shared-core decision

Do not modify or reopen SC-01~SC-10 now.

```text
Module A:
  adjacent to SC-04; keep Audit/Analysis-specific pending receiving-method evidence

Module B:
  method-specific operational structure with Computation/Operation handoff

Module C:
  SC-03 + SC-05 algorithmic specialization

Module D:
  SC-08 + SC-10 compatible recording/handoff layer
```

## 8. Explicit non-changes

Do not change:
- default verdict vocabulary;
- eight-axis frame;
- method count;
- SC-01~SC-10;
- external-domain verdict separation;
- finite computation safeguard;
- historical verdicts;
- older root-level audit methodology files.

## 9. Apply state

```text
APPLIED_TO_MAIN: no
READY_FOR_FINAL_PATCH_REVIEW: yes
BOUNDARY_AUDIT_INCORPORATED: yes
CANONICAL_PATH_LOCKED_TO_DSD_AUDIT: yes
TEMPLATE_SYNC_INCLUDED: yes
HISTORICAL_MIGRATION_REQUIRED: no
SHARED_CORE_REOPENED: no
```
