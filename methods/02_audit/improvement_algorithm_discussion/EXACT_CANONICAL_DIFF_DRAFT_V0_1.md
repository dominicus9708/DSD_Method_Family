# Audit — Exact Canonical Diff Draft v0.1

Status: **TEMPORARY / NON-CANONICAL / DO NOT APPLY YET**  
Date: 2026-09-27 KST

Target canonical files:
- `DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`
- `DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md`
- `DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md`

## 1. GENERAL_AUDIT_FRAMEWORK.md

### 1.1 Universal procedure — step 2

Current:

```text
2. Fix scope, time, descriptive resolution, exclusions, and external standard.
```

Proposed:

```text
2. Fix scope, time, descriptive resolution, exclusions, and external standard.
   When intermediate requirements differ materially in locality, uniformity, norm,
   moment, support, aggregation, precision, or another claim-relevant axis,
   record the active requirement profile and do not force incomparable axes into
   one total resolution order without an explicit implication or preservation rule.
```

### 1.2 Universal procedure — step 6

Current:

```text
6. Reconstruct available alternatives.
```

Proposed:

```text
6. Reconstruct available alternatives and, when several routes are material,
   distinguish AND-prerequisites, OR-alternative sufficient routes, theorem gates,
   bridges, attack methods, and supporting work.
```

### 1.3 Universal procedure — step 10

Current:

```text
10. Audit aggregation, information loss, injectivity, and reconstruction claims where used.
```

Proposed:

```text
10. Audit aggregation, information loss, injectivity, and reconstruction claims where used.
    When a route also strengthens the required claim, record claim-strength escalation
    separately from representation information loss. Equal outputs or a shared latent
    parent do not establish claim-relevant representation equivalence without an
    explicit preservation argument.
```

### 1.4 Universal procedure — insert conditional frontier check after step 12

Proposed new conditional step:

```text
When the audited object reports an active research, engineering, procedural, or
computational frontier, classify new work as direct gate closure, required bridge
or certificate, frontier-reducing equivalence, route invalidation, supporting work,
exploration, stronger-but-optional work, or duplicate work. Non-frontier status is
not a deletion instruction.
```

Keep numbering stable by presenting this as a conditional paragraph rather than renumbering all steps.

### 1.5 Core safeguards — add two bullets

```text
- A stronger sufficient condition must not be silently promoted into a necessary condition for the audited claim.
- A shared latent object, common source, or equal reduced output must not be promoted into structural equivalence without a claim-relevant preservation argument.
```

These clarify existing safeguards rather than create a new verdict class.

## 2. AUDIT_RECORDING_STANDARD.md

### 2.1 Add optional subsection after Scope lock

```text
### 4.1 Optional claim-requirement profile

Use when intermediate requirements materially differ.

CLAIM_REQUIREMENT_PROFILE:
  ACTIVE_AXES:
  PARENT_CLAIM:
  INTERMEDIATE_REQUIREMENT:
  RELATION:
  IMPLICATION_OR_PRESERVATION_BASIS:

Allowed relation vocabulary:
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED
```

### 2.2 Add optional subsection after Alternative ledger

```text
### 12.1 Optional dependency/frontier ledger

DEPENDENCY_FRONTIER:
  AND_PREREQUISITES:
  OR_SUFFICIENT_ROUTES:
  COMMON_MANDATORY_GATES:
  FRONTIER_FAMILIES:
  ATTACK_METHODS:
  SUPPORTING_WORK:
  FROZEN_BRANCHES:
  REOPEN_CONDITIONS:
```

### 2.3 Extend Aggregation and reconstruction ledger

Append:

```text
REPRESENTATION_RELATION:
CLAIM_STRENGTH_ESCALATION:
ESCALATION_BASIS:
CLAIM_RELEVANT_INFORMATION_LOSS:
MERGE_OR_DEDUPLICATION_BASIS:
```

Suggested optional representation vocabulary:

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

### 2.4 Revision compatibility note

Add:

```text
The optional fields above are prospective/additive.
Historical audit records are not invalidated solely because they predate these fields.
```

## 3. AUDIT_ALGORITHMIZATION_ROADMAP.md

### 3.1 Stable input schema

Add optional machine-readable fields:

```text
claim_requirement_profile
dependency_frontier
representation_relation
escalation_information_loss
branch_state_reopen
gain_set
```

Mark them optional/conditional, not required for every audit.

### 3.2 Phase 2 — structural rule engine

Append candidate rules:

```text
stronger sufficient -> necessary                [warn without implication basis]
incomparable resolution axes -> scalar order    [warn without ordering rule]
OR alternative -> mandatory AND prerequisite     [warn]
attack method -> theorem gate                    [warn]
shared parent -> representation equivalence      [warn without preservation proof]
one-way bound -> equivalence                     [warn]
claim-strength escalation -> unrecorded          [warn when material]
claim-relevant information loss -> unrecorded    [warn]
frozen branch -> false/impossible                [warn]
supporting/exploratory work -> direct closure     [warn]
```

### 3.3 Phase 4 pipeline

Proposed pipeline text:

```text
SOURCE LOCK
-> INTERFACE LOCK
-> SCOPE / CLAIM-REQUIREMENT LOCK          [conditional extension]
-> TYPE/STATUS VALIDATION
-> SELECTION/EXCLUSION CHECK
-> DEPENDENCY / FRONTIER CHECK             [conditional extension]
-> BRIDGE CHECK
-> REPRESENTATION-RELATION CHECK           [conditional extension]
-> TRANSITION/LINEAGE CHECK
-> ESCALATION / INFORMATION-LOSS CHECK     [conditional extension]
-> ALTERNATIVE/WITNESS CHECK
-> AGGREGATION/RECONSTRUCTION CHECK
-> CONTRADICTION CHECK
-> MAXIMUM-SUPPORTED-CLAIM CHECK
-> DOMAIN VERDICT + DSD AUDIT VERDICT
```

Executable invariant certificates remain under domain adapters/reproducibility and are not promoted to universal core.

## 4. Explicit non-changes

Do not change:
- default verdict vocabulary;
- eight-axis common frame;
- method count;
- SC-01..SC-10 registry;
- domain-verdict separation;
- finite computation safeguard;
- historical audit verdicts.

## 5. Apply state

```text
APPLIED_TO_MAIN: no
READY_FOR_CANONICAL_REVIEW: yes
HISTORICAL_MIGRATION_REQUIRED: no
SHARED_CORE_REOPENED: no
```
