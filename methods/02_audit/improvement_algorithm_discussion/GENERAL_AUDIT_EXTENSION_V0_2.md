# DSD Audit General Strengthening Extension v0.2

Status: **TEMPORARY / NON-CANONICAL / A/B-TEST CANDIDATE**  
Date: 2026-09-27 KST  
Parent discussion: `README.md`

## 0. Purpose

This document turns the strongest hard-problem-derived Audit deltas into explicit machine-assistable checks while preserving the canonical General Audit Framework.

The extension generates warnings, dependency summaries, and traceable classifications.
It does not decide domain truth.

## 1. New audit input fields under test

```text
CLAIM_CONTRACT
REQUIRED_RESOLUTION_PROFILE
DEPENDENCY_HYPERGRAPH
REPRESENTATION_RELATION_LEDGER
ESCALATION_LEDGER
INFORMATION_LOSS_LEDGER
FRONTIER_FAMILIES
BRANCH_STATE_LEDGER
GAIN_SET
```

These are temporary extension fields.
They are not yet part of the canonical minimum audit record.

## 2. Required-resolution audit

Audit the claim and each intermediate obligation separately.

Required outputs:

```text
RESOLUTION_RELATION:
  REQUIRED_MATCH
  PROVEN_STRONGER_SUFFICIENT
  CONDITIONAL_STRONGER_SUFFICIENT
  WEAKER_INSUFFICIENT
  INCOMPARABLE
  RELATION_UNDETERMINED

IMPLICATION_BASIS:
PARENT_CLAIM_REQUIRES_THIS_LEVEL:
```

### Warning codes

```text
RES-001  stronger target treated as necessary without implication basis
RES-002  weaker target treated as sufficient without bridge
RES-003  incomparable profiles forced into a total strength ordering
RES-004  required resolution changed after result reveal without revision record
```

## 3. Dependency/gate audit

Audit a typed AND/OR hypergraph rather than only a flat OPEN list.

Checks:

- attack method counted as theorem gate
- equivalent nodes double-counted
- alternative sufficient routes collapsed into one mandatory route
- one route's stronger descendant counted as an independent global gate
- dependency direction reversed
- frozen branch silently reactivated without reopen condition

### Warning codes

```text
DEP-001  attack method counted as unresolved theorem gate
DEP-002  established-equivalent obligations double-counted
DEP-003  OR-alternative silently promoted to mandatory AND-prerequisite
DEP-004  stronger descendant double-counted beside its parent gate
DEP-005  dependency direction unsupported
DEP-006  reactivation lacks declared reopen condition
```

Audit output should preserve a **family of minimal frontier sets** when more than one admissible route exists.
Do not force one scalar frontier rank when the route structure is genuinely plural.

## 4. Representation/common-object audit

For each proposed merge or deduplication, require an explicit relation:

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

### Warning codes

```text
REP-001  same output used as evidence of same structure
REP-002  shared latent parent used to erase distinct contractions
REP-003  one-way bound treated as equivalence
REP-004  representation merge lacks map or preservation argument
REP-005  dual/isometric relation asserted outside its declared assumptions
```

Only established claim-relevant equivalence permits gate deduplication.

## 5. Escalation audit and information-loss audit are separate

### 5.1 Claim-strength escalation

```text
ESC-001  average -> supremum without parent necessity or sufficiency justification
ESC-002  global -> pointwise without parent necessity or sufficiency justification
ESC-003  lower moment -> higher moment without bridge
ESC-004  weighted target -> uniform envelope without bridge
ESC-005  convenience strengthening silently reclassified as required
```

### 5.2 Information loss / coarsening

```text
INF-001  signed cancellation removed without relevance check
INF-002  component/support information aggregated before it is no longer needed
INF-003  non-injective reduction followed by unsupported reconstruction
INF-004  information-loss status omitted for a material transform
```

A step may trigger both ESC and INF warnings.
That is intentional.

## 6. Frontier admissibility audit

Classify every proposed new branch or calculation:

```text
FRONTIER_DIRECT
FRONTIER_BRIDGE
FRONTIER_REDUCTION
FRONTIER_INVALIDATION
FRONTIER_REQUIRED_CERTIFICATE
SUPPORTING
EXPLORATORY
OPTIONAL_STRONGER_ROUTE
DUPLICATE_ROUTE
```

### Warning codes

```text
FRT-001  non-frontier exploration reported as direct closure progress
FRT-002  duplicate route opened without a distinct unresolved obligation
FRT-003  frozen route resumed without new input matching reopen condition
FRT-004  supporting lemma counted as closure of the parent gate
```

Non-frontier status is not a reason to delete the work.
It is a reporting and resource-allocation distinction.

## 7. Branch-state audit

Temporary operational states:

```text
ACTIVE_FRONTIER
SUPPORTING
DORMANT_STRONG
FROZEN_UNDER_CURRENT_INPUTS
CLOSED
INVALIDATED_UNDER_SCOPE
```

For any transition to or from `FROZEN_UNDER_CURRENT_INPUTS`, require:

```text
STATE_TRANSITION_REASON:
MISSING_INPUT_OR_IDENTITY:
PRESERVED_RESULTS:
REOPEN_CONDITION:
```

### Warning codes

```text
STA-001  frozen treated as false/impossible
STA-002  invalidated route retains active-frontier status
STA-003  closed route reopened without scope/version change
STA-004  branch-state change lacks lineage/revision record
```

This is provisionally an operational specialization of existing revision/alternative/lineage rules, not a new universal verdict layer.

## 8. Computation/theorem boundary

The canonical safeguard already forbids finite computation from becoming a general proof without a separate argument.

The extension only makes that rule more executable:

```text
CMP-001  finite certificate reported as general theorem
CMP-002  computational acceleration reported as theorem gain
CMP-003  empirical pattern reported as structural identity
CMP-004  structural narrowing reported as closure
```

No new core principle is claimed here.

## 9. Executable invariant certificate

When the audited object is computational, optionally require a deterministic certificate for claims that are mechanically checkable.

Candidate checks:

```text
LINEAGE_IDENTITY
ACCOUNTING_CONSERVATION
EXACT_MAPPING_PRESERVATION
SUPPORT_OR_CARDINALITY_CONSISTENCY
CANONICAL_ANCHOR_TOTALS
NO_DOUBLE_APPLICATION
STATE_TRANSITION_LEGALITY
```

This remains a reproducibility/math/software adapter specialization unless cross-domain tests show that it belongs in the universal audit core.

## 10. Multi-label gain audit

Allowed gain labels:

```text
THEOREM_GAIN
STRUCTURAL_GAIN
COMPUTATIONAL_GAIN
REPRODUCIBILITY_GAIN
AUDIT_GAIN
NEGATIVE_NARROWING_GAIN
NO_DEMONSTRATED_GAIN
```

Warnings:

```text
GAIN-001  computational gain promoted to theorem gain
GAIN-002  branch reduction promoted to proof closure
GAIN-003  audit error detection promoted to domain truth
```

## 11. v0.2 extension pipeline

The current canonical pipeline is preserved.
The candidate checks are inserted as follows:

```text
SOURCE LOCK
-> INTERFACE LOCK
-> SCOPE + CLAIM CONTRACT LOCK                  [candidate]
-> TYPE / STATUS VALIDATION
-> REQUIRED-RESOLUTION CHECK                    [candidate]
-> SELECTION / EXCLUSION
-> DEPENDENCY HYPERGRAPH + GATE CHECK           [candidate]
-> BRIDGE
-> REPRESENTATION / COMMON-OBJECT CHECK         [candidate]
-> TRANSITION / LINEAGE
-> ESCALATION + INFORMATION-LOSS CHECK          [candidate]
-> ALTERNATIVE / WITNESS
-> FRONTIER ADMISSIBILITY + BRANCH STATE        [candidate]
-> AGGREGATION / RECONSTRUCTION
-> CONTRADICTION
-> EXECUTABLE INVARIANT CHECK                   [optional specialization]
-> MAXIMUM-SUPPORTED-CLAIM
-> DOMAIN VERDICT + DSD STRUCTURAL VERDICT
-> MULTI-LABEL GAIN RECORD                      [candidate recording]
```

## 12. Provisional disposition of Audit delta candidates

```text
AUD-Δ01 Claim-to-Resolution Sufficiency
  -> PROMOTE_TO_AB_TEST
  -> use multi-axis profile, not scalar resolution

AUD-Δ02 Dependency-Rank / Gate
  -> PROMOTE_TO_AB_TEST
  -> use AND/OR hypergraph and frontier families

AUD-Δ03 Escalation
  -> PROMOTE_TO_AB_TEST
  -> separate claim-strength escalation from information loss

AUD-Δ04 Representation Duplication / Common Object
  -> PROMOTE_TO_AB_TEST
  -> gate merge only under established claim-relevant equivalence

AUD-Δ05 Freeze and Reopen
  -> ABSORB_AS_OPERATIONAL_SPECIALIZATION
  -> likely under alternatives + lineage + revision

AUD-Δ06 Executable Invariant Certificate
  -> KEEP_AS_DOMAIN/REPRODUCIBILITY_SPECIALIZATION

AUD-Δ07 Frontier Admissibility
  -> PROMOTE_TO_AB_TEST

AUD-Δ08 Computation/Theorem Boundary
  -> ABSORB_INTO_EXISTING_CORE_SAFEGUARD
  -> add warning implementation only

AUD-Δ09 Negative Result Retention
  -> ABSORB_INTO_SC-08 / existing failure-preservation rules
```

All dispositions remain temporary until A/B validation and user approval.

## 13. A/B validation protocol

Use the frozen canonical Audit as baseline and this extension as candidate.

The test must use the same source set and the same external-domain standard.

Measure:

```text
MISSED_OVERCLAIM
FALSE_PRUNING
DUPLICATE_GATE_COUNT
UNNECESSARY_STRONG_TARGET_COUNT
UNJUSTIFIED_ESCALATION_COUNT
CLAIM_RELEVANT_INFORMATION_LOSS_MISSED
FINITE_TO_GENERAL_OVERCLAIM
FRONTIER_BRANCH_COUNT
FRONTIER_FAMILY_COUNT
REVIEW_STEPS
TRACEABLE_WARNING_COUNT
EXTERNAL_VERDICT_CHANGED_WITHOUT_EXTERNAL_JUSTIFICATION
```

Acceptance constraints:

1. `FALSE_PRUNING` must not increase.
2. The candidate must not reduce plural alternative routes to one route without proof.
3. The candidate must not change an external-domain verdict without an external-domain argument.
4. Any reduction in frontier size must be traceable to equivalence, sufficiency, invalidation, or dependency structure.
5. Warning count alone is not a success metric; warnings must correspond to claim-relevant corrections.
