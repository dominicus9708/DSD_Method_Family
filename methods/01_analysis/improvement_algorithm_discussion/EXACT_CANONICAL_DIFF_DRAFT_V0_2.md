# Analysis — Exact Canonical Diff Draft v0.2

Status: **TEMPORARY / NON-CANONICAL / DO NOT APPLY YET**  
Date: 2026-09-27 KST  
Supersedes temporary draft: `EXACT_CANONICAL_DIFF_DRAFT_V0_1.md`

This revision incorporates the final boundary/duplication audit.

Target canonical file:
`methods/01_analysis/README.md`

Proposed canonical companion:
`methods/01_analysis/ANALYSIS_OPERATIONAL_CONTROLLER.md`

## 1. README minimal diff

### 1.1 Primary checks

Current anchor:

```text
Primary checks:
- candidate vs admitted/realized structure;
- undefined vs zero vs absence;
- applicability and prerequisite distinctions;
- direct/partial/encoded/non-correspondence when correspondence is part of the analysis;
- aggregate equality vs structural equality;
- first branching and boundary cases when applicable.
```

Proposed replacement:

```text
Primary checks:
- candidate vs admitted/realized structure;
- undefined vs zero vs absence;
- applicability and prerequisite distinctions;
- direct/partial/encoded/non-correspondence when correspondence is part of the analysis;
- aggregate equality vs structural equality;
- first branching and boundary cases when applicable;
- for multi-step targets, the relation between an already-declared claim and intermediate requirement strength, without assuming one universal scalar resolution order;
- when multiple routes are material, AND-prerequisites, OR-alternative sufficient routes, theorem gates, bridges, attack methods, and plural minimal dependency frontiers;
- when multiple representations are material, established equivalence versus projection, contraction, coarsening, one-way sufficiency, sibling contraction, or shared latent parenthood;
- claim-strength escalation and representation information loss as separate checks when both are material.
```

### 1.2 Controller pointer and boundary guard

Add after the current external-standard boundary sentence:

```text
For multi-step analyses, use [ANALYSIS_OPERATIONAL_CONTROLLER.md](ANALYSIS_OPERATIONAL_CONTROLLER.md) when the declared target contains material intermediate requirements, multiple sufficient routes, multiple representations, or claim-relevant reductions.

The controller analyzes an already-declared claim; it does not author domain requirements. Primary requirement specification remains DSD Specification or the competent external specification source. Dependency analysis does not decide run scheduling or resource allocation; executable omission/reuse belongs to DSD Computation, deliberate representation reduction to DSD Compression, and live lifecycle/resource orchestration to DSD Operation. When source-to-target mapping itself is the primary task, use DSD Transformation.
```

## 2. Proposed canonical companion file

Recommended canonical file:

`methods/01_analysis/ANALYSIS_OPERATIONAL_CONTROLLER.md`

### Proposed content

```text
# DSD Analysis Operational Controller

Status: established operational protocol for multi-step Analysis

Purpose:
Refine structural decomposition of one declared target when intermediate
requirements, alternative sufficient routes, multiple representations, or
claim-relevant reductions materially affect the result.

This controller receives an already-declared claim. It does not create or
replace domain requirements.

## 1. Declared-claim lock and requirement relation

Record:
DECLARED_CLAIM_LOCK
ACTIVE_REQUIREMENT_AXES
INTERMEDIATE_REQUIREMENT
RELATION_TO_DECLARED_CLAIM
IMPLICATION_OR_PRESERVATION_BASIS

Only activate axes material to the claim, for example:
scope, quantifier, locality, uniformity, moment, norm, sign, support,
aggregation, precision.

Allowed relations:
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED

Do not force heterogeneous axes into one total order without an explicit
implication or preservation rule.

## 2. Dependency/frontier representation

Use a typed AND/OR dependency representation when several routes are material.

Distinguish:
AND_PREREQUISITE
OR_SUFFICIENT_ROUTE
THEOREM_OR_DOMAIN_GATE
BRIDGE
SUPPORTING_LEMMA
ATTACK_METHOD
COMPUTATIONAL_CERTIFICATE

Preserve plural minimal dependency frontiers when more than one sufficient
route remains.

This is a structural representation, not a scheduler.
It does not decide which computation or project action must be run next.

## 3. Representation and information relation

Use claim-relevant relation labels:
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

Merge structural obligations only under established claim-relevant equivalence.

Equal outputs, a shared latent parent, or a one-way bound do not by themselves
establish equivalence.

Record separately:
CLAIM_STRENGTH_ESCALATION
REPRESENTATION_INFORMATION_LOSS

A route may simultaneously impose a stronger sufficient condition and discard
source information.

## 4. Descriptive branch state

When useful:
DIRECT_STRUCTURAL_OBLIGATION
SUPPORTING
OPTIONAL_STRONGER
DORMANT
FROZEN_UNDER_CURRENT_INPUTS
CLOSED
INVALIDATED_UNDER_SCOPE

For frozen branches record:
FROZEN_REASON
PRESERVED_RESULTS
REOPEN_CONDITION

FROZEN does not mean false or impossible.
These states do not allocate resources or execution priority.

## 5. Handoffs

If the primary operation becomes:
- authoring/organizing requirements -> DSD Specification
- source-to-target representation mapping -> DSD Transformation
- deciding what to evaluate/omit or implementing reuse/cache -> DSD Computation
- intentional representation reduction -> DSD Compression
- live lifecycle/resource/monitoring orchestration -> DSD Operation
- cross-target structural judgment -> DSD Comparison
- criterion-based class assignment -> DSD Classification
- source/context/interpretive-bridge reading -> DSD Interpretation

## 6. Gain recording

Optional multi-label record:
THEOREM_GAIN
STRUCTURAL_GAIN
COMPUTATIONAL_GAIN
REPRODUCIBILITY_GAIN
AUDIT_GAIN
NEGATIVE_NARROWING_GAIN
NO_DEMONSTRATED_GAIN

Gain labels do not alter the external-domain validity standard.

## 7. Safeguards

- no automatic branch deletion;
- no scalar total ordering without justification;
- no weaker condition called sufficient without an argument;
- no stronger sufficient condition called necessary without an argument;
- no representation merge from equal output/shared parent alone;
- no external-domain verdict generated from DSD structural classification alone;
- no historical record invalidated merely because it predates this controller.
```

## 3. Shared-core relation

Do not modify SC-01~SC-10.

Current relation:

```text
Claim requirement relation:
  adjacent to SC-04 but not identical

Representation/information relation:
  operational specialization of SC-03 + SC-05

Gain/external-standard guards:
  consistent with SC-08 + SC-10
```

No SC reopening until independent receiving-method evidence establishes a stable cross-method obligation not representable by current SCs.

## 4. Historical compatibility

```text
HISTORICAL_ANALYSIS_MIGRATION_REQUIRED: no
OLD_ANALYSIS_RESULTS_INVALIDATED: no
CONTROLLER_APPLICATION:
  prospective
  or explicit revision/reanalysis only
```

## 5. Apply state

```text
APPLIED_TO_MAIN: no
READY_FOR_FINAL_PATCH_REVIEW: yes
BOUNDARY_AUDIT_INCORPORATED: yes
```
