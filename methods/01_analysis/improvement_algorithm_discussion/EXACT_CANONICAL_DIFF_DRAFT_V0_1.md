# Analysis — Exact Canonical Diff Draft v0.1

Status: **TEMPORARY / NON-CANONICAL / DO NOT APPLY YET**  
Date: 2026-09-27 KST

Target canonical file:
`methods/01_analysis/README.md`

Proposed new canonical companion:
`methods/01_analysis/ANALYSIS_OPERATIONAL_CONTROLLER.md`

## 1. README minimal diff

### Anchor

Current:

```text
Primary checks:
- candidate vs admitted/realized structure;
- undefined vs zero vs absence;
- applicability and prerequisite distinctions;
- direct/partial/encoded/non-correspondence when correspondence is part of the analysis;
- aggregate equality vs structural equality;
- first branching and boundary cases when applicable.
```

### Proposed replacement

```text
Primary checks:
- candidate vs admitted/realized structure;
- undefined vs zero vs absence;
- applicability and prerequisite distinctions;
- direct/partial/encoded/non-correspondence when correspondence is part of the analysis;
- aggregate equality vs structural equality;
- first branching and boundary cases when applicable;
- for multi-step targets, claim-relevant requirement strength without assuming one universal scalar resolution order;
- when multiple routes exist, AND-prerequisites, OR-alternative sufficient routes, theorem gates, bridges, attack methods, and plural active frontier families;
- when multiple representations are used, established equivalence versus projection, contraction, coarsening, one-way sufficiency, or shared latent parenthood;
- claim-strength escalation and information loss as separate checks when both are material.
```

### Add after the existing external-standard boundary sentence

```text
For multi-step analyses, use [ANALYSIS_OPERATIONAL_CONTROLLER.md](ANALYSIS_OPERATIONAL_CONTROLLER.md).
The controller is an optional operational protocol: it does not replace external-domain validity standards, does not delete non-frontier work, and does not transfer Computation, Compression, or Operation responsibilities into Analysis.
```

## 2. Companion file minimal canonical content

The canonical companion should be shorter than the temporary v0.2 research file.

Recommended canonical content:

```text
# DSD Analysis Operational Controller

Status: established operational protocol for multi-step Analysis

Use only when the declared target has material intermediate requirements,
multiple sufficient routes, multiple representations, or claim-relevant reductions.

1. Claim requirement profile
   - record only active axes;
   - compare strength only through explicit implication/preservation rules;
   - allowed relations:
     REQUIRED_MATCH
     PROVEN_STRONGER_SUFFICIENT
     CONDITIONAL_STRONGER_SUFFICIENT
     WEAKER_INSUFFICIENT
     INCOMPARABLE
     RELATION_UNDETERMINED

2. Dependency/frontier structure
   - distinguish AND prerequisites from OR sufficient routes;
   - distinguish theorem gates, bridges, attack methods, supporting lemmas;
   - preserve a family of minimal active frontiers when several routes remain;
   - non-frontier does not mean false or disposable.

3. Representation/information structure
   - distinguish:
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
   - merge only under established claim-relevant equivalence;
   - record claim-strength escalation separately from information loss;
   - equal outputs or shared latent parenthood do not establish structural identity.

4. Branch state
   - ACTIVE_FRONTIER
   - SUPPORTING
   - DORMANT_STRONG
   - FROZEN_UNDER_CURRENT_INPUTS
   - CLOSED
   - INVALIDATED_UNDER_SCOPE
   For frozen work, preserve reason and reopen condition.

5. Handoffs
   - cache/reuse execution -> DSD Computation
   - deliberate representation reduction -> DSD Compression
   - live lifecycle/resource orchestration -> DSD Operation
   - cross-target judgment -> DSD Comparison
   - criterion assignment -> DSD Classification
   - source/context reading -> DSD Interpretation

6. Safeguards
   - no automatic branch deletion;
   - no scalar total ordering without justification;
   - no weaker target called sufficient without an argument;
   - no stronger target called necessary without an argument;
   - no external-domain verdict generated from DSD structural classification alone.
```

## 3. Historical compatibility

No mandatory migration of earlier Analysis records.

The controller applies prospectively or when an older case is deliberately reopened.

## 4. Apply state

```text
APPLIED_TO_MAIN: no
READY_FOR_CANONICAL_REVIEW: yes
```
