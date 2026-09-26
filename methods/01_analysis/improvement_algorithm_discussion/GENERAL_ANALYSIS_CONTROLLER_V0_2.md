# DSD Analysis General Strengthening Controller v0.2

Status: **TEMPORARY / NON-CANONICAL / A/B-TEST CANDIDATE**  
Date: 2026-09-27 KST  
Parent discussion: `README.md`

## 0. Purpose

This document refines the hard-problem-derived delta candidates into a general operational controller without changing canonical DSD Analysis.

The goal is not to add more labels.
The goal is to reduce unnecessary search, prevent accidental strengthening of the target, and keep structurally distinct objects distinct.

## 1. Main correction: resolution is a profile, not one scalar

A single `R_min` value is too coarse for general Analysis.

For a declared claim (C), define a claim-relevant resolution profile:

[
\mathcal R(C)=
(ho_{scope},ho_{quantifier},ho_{locality},ho_{uniformity},
 ho_{moment},ho_{norm},ho_{sign},ho_{support},
 ho_{aggregation},ho_{precision}).
]

Not every coordinate is always active.
Different coordinates may be incomparable.
Therefore the controller must not assume a universal total ordering such as “pointwise is always the next resolution level”.

The controller compares two profiles only through an explicit implication or preservation rule.

Required relation labels:

```text
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED
```

A route is never pruned merely because an informal norm or resolution hierarchy suggests that it is stronger.

## 2. Claim contract

Before decomposition, record:

```text
CLAIM_ID:
CLAIM_TEXT:
SCOPE:
QUANTIFIERS:
TARGET_OBJECT:
TARGET_OUTPUT:
EXTERNAL_VALIDITY_STANDARD:
REQUIRED_RESOLUTION_PROFILE:
ALLOWED_COARSENING:
FORBIDDEN_INFORMATION_LOSS:
```

The claim contract is not a proof.
It fixes what the analysis is actually trying to support.

## 3. Dependency model: typed AND/OR hypergraph

A simple DAG is insufficient when a conclusion needs several prerequisites simultaneously or admits alternative sufficient routes.

Use a typed dependency hypergraph:

```text
NODE_TYPES:
  CLAIM
  GATE
  BRIDGE
  LEMMA
  REPRESENTATION
  ATTACK_METHOD
  COMPUTATIONAL_CERTIFICATE
  RESULT

EDGE_TYPES:
  REQUIRES_AND
  SUFFICIENT_OR
  IMPLIES
  EQUIVALENT_IF
  REPRESENTS
  CONTRACTS
  COARSENS
  ATTACKS
  SUPPORTS
  REOPENS
```

Rules:

1. `ATTACK_METHOD` is not counted as an unresolved theorem gate.
2. Equivalent nodes are quotiented only when the equivalence itself is established under the locked scope.
3. Alternative routes remain alternatives; compression must not silently choose one as uniquely necessary.
4. The output is a **family of minimal active frontier sets**, not necessarily one scalar “rank”.

Recommended output:

```text
FRONTIER_FAMILIES:
  F1 = {G1, G2}
  F2 = {G3}
MIN_FRONTIER_SIZE:
MAX_RETAINED_FRONTIER_SIZE:
COMMON_MANDATORY_GATES:
OPTIONAL_ROUTE_GATES:
```

This prevents false compression when several genuinely different proof routes remain open.

## 4. Representation normalization without unsafe merging

For branches (B_i), search for a common parent object (Z) and explicit maps (\pi_i:Z\to B_i).

Allowed relation labels:

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

Merge branches only for `IDENTICAL` or an established claim-relevant equivalence.

`SIBLING_CONTRACTIONS`, `PROJECTION`, and `COARSENING` may share a latent object but remain separate obligations if they discard different information.

Numeric equality of outputs is never enough to infer structural identity.

## 5. Separate claim strengthening from information loss

The previous delta list mixed two different events:

A. **Claim-strength escalation** — the route demands a stronger condition than the parent claim requires.

B. **Representation coarsening** — the route discards information that may be needed later.

Track them separately.

### 5.1 Escalation ledger

```text
STEP:
FROM_REQUIREMENT:
TO_REQUIREMENT:
IMPLICATION_PROVED:
PARENT_REQUIRES_ESCALATION:
STATUS:
  NECESSARY_BY_PARENT
  PROVEN_STRONGER_SUFFICIENT
  CONVENIENCE_ONLY
  UNJUSTIFIED
  INCOMPARABLE
```

Examples requiring inspection:
- average -> supremum
- global -> pointwise
- first moment -> second moment
- weighted target -> uniform envelope

### 5.2 Information-loss ledger

```text
STEP:
SOURCE_INFORMATION:
TRANSFORM:
LOST_INFORMATION:
INJECTIVE_ON_RELEVANT_CLASS:
RECONSTRUCTION_AVAILABLE:
CLAIM_RELEVANCE_OF_LOSS:
STATUS:
  LOSSLESS
  LOSSY_BUT_IRRELEVANT
  LOSSY_AND_RELEVANT
  UNDETERMINED
```

Examples:
- signed sum -> absolute mass
- component-resolved object -> aggregate
- support-sensitive object -> reduced statistic

A step can be simultaneously a stronger estimate and a poorer representation.
Those two facts must not be collapsed into one “resolution” label.

## 6. Active frontier controller

Each branch receives one operational state:

```text
ACTIVE_FRONTIER
SUPPORTING
DORMANT_STRONG
FROZEN_UNDER_CURRENT_INPUTS
CLOSED
INVALIDATED_UNDER_SCOPE
```

For frozen routes record:

```text
FROZEN_AT:
MISSING_INPUT_OR_IDENTITY:
PRESERVED_RESULTS:
REOPEN_CONDITION:
```

`FROZEN_UNDER_CURRENT_INPUTS` never means mathematically impossible.

### Frontier admissibility

A new task counts as canonical frontier work only if it does at least one of:

```text
DIRECTLY_DISCHARGES_ACTIVE_GATE
ESTABLISHES_REQUIRED_BRIDGE
PROVES_EQUIVALENCE_THAT_REDUCES_FRONTIER
INVALIDATES_AN_ACTIVE_ROUTE_WITH_A_VALID_COUNTEREXAMPLE
PRODUCES_A_REQUIRED_CERTIFICATE_FOR_AN_ACTIVE_GATE
```

Otherwise classify as:

```text
SUPPORTING
EXPLORATORY
OPTIONAL_STRONGER_ROUTE
DUPLICATE_ROUTE
```

These classes are retention classes, not deletion commands.

## 7. Exact reuse belongs to Computation unless it changes structure

Analysis may detect repeated descriptors, prefixes, or state expansions.

It should output:

```text
REUSE_CANDIDATE
EXACT_MAPPING_REQUIRED
POSSIBLE_COMPUTATION_HANDOFF
```

Implementation of caches, memoization, cyclic-window reuse, or run-time optimization belongs primarily to **DSD Computation** unless the reuse exposes a new structural identity.

Therefore ANA-Δ07 is provisionally **REFERRED_TO_COMPUTATION**, not promoted as a new Analysis core rule.

## 8. Gain is a set, not one exclusive label

Use zero or more labels:

```text
THEOREM_GAIN
STRUCTURAL_GAIN
COMPUTATIONAL_GAIN
REPRODUCIBILITY_GAIN
AUDIT_GAIN
NEGATIVE_NARROWING_GAIN
NO_DEMONSTRATED_GAIN
```

A result may have several gains simultaneously.
No gain label upgrades the external-domain validity status.

## 9. v0.2 controller

```text
INPUT: declared target T, source set S

1. LOCK_CLAIM_CONTRACT(T)
2. DERIVE_REQUIRED_RESOLUTION_PROFILE(T)
3. DECOMPOSE_TARGET_USING_REQUIRED_DSD_LAYERS_ONLY
4. BUILD_TYPED_AND_OR_DEPENDENCY_HYPERGRAPH
5. NORMALIZE_REPRESENTATIONS_WITH_EXPLICIT_RELATION_TYPES
6. FOR each obligation:
      compare obligation profile to claim profile
      require explicit implication for "stronger sufficient"
7. AUDIT_ESCALATION_AND_INFORMATION_LOSS_SEPARATELY
8. COMPUTE_MINIMAL_ACTIVE_FRONTIER_FAMILIES
9. CLASSIFY_BRANCH_STATES_AND_REOPEN_CONDITIONS
10. CLASSIFY_NEW_WORK_BY_FRONTIER_ADMISSIBILITY
11. EMIT_REUSE_CANDIDATES_TO_COMPUTATION
12. EMIT_MULTI_LABEL_GAIN_SET
13. HAND_OFF_TO_AUDIT_WITH_TRACEABLE_LEDGER
```

## 10. Non-pruning invariants

The strengthening controller must preserve these invariants:

1. No route is deleted because it is currently non-frontier.
2. No stronger condition is replaced by a weaker one unless the weaker condition is separately proved sufficient for the locked claim.
3. No two representations are merged from output equality alone.
4. No sibling contractions are treated as identical merely because they share a parent object.
5. No information-losing transform is called harmless without a claim-relevance check.
6. No finite certificate is upgraded to a general theorem.
7. No DSD structural classification replaces the external field's validity standard.

## 11. Provisional disposition of Analysis delta candidates

```text
ANA-Δ01 Minimum Sufficient Resolution
  -> PROMOTE_TO_AB_TEST
  -> refined as multi-axis required-resolution profile

ANA-Δ02 Dependency Frontier Compression
  -> PROMOTE_TO_AB_TEST
  -> refined from simple DAG/rank to typed AND/OR hypergraph + frontier families

ANA-Δ03 Resolution Escalation Detector
  -> PROMOTE_TO_AB_TEST
  -> split into claim-strength escalation and information-loss ledgers

ANA-Δ04 Common Latent Object / Duplicate Branch
  -> PROMOTE_TO_AB_TEST
  -> unsafe merge guard added

ANA-Δ05 Signed-Structure Preservation
  -> ABSORB_INTO_INFORMATION_LOSS_CHECK
  -> not retained as independent general rule unless later fixtures show separate value

ANA-Δ06 Freeze / Dormancy / Reopen
  -> KEEP_AS_SHARED_OPERATIONAL_STATE_LAYER
  -> candidate for Analysis/Audit shared recording, not necessarily Analysis core

ANA-Δ07 Exact Reuse / Descriptor Cache
  -> REFER_TO_COMPUTATION
  -> Analysis only detects reuse opportunity

ANA-Δ08 Gain-Type Separation
  -> KEEP_AS_SHARED_RECORDING_RULE
  -> use multi-label gain set
```

All dispositions remain temporary until A/B validation and user approval.

## 12. A/B validation targets

The canonical Analysis baseline remains unchanged.

Compare baseline vs v0.2 on the same locked fixtures.

Primary measures:

```text
UNNECESSARY_STRONG_TARGETS
FALSE_PRUNING
DUPLICATE_BRANCHES_COUNTED_AS_INDEPENDENT
UNJUSTIFIED_ESCALATIONS
CLAIM_RELEVANT_INFORMATION_LOSS_MISSED
ACTIVE_FRONTIER_SIZE
FRONTIER_FAMILY_COUNT
REVIEW_STEPS
EXTERNAL_VERDICT_CHANGED_WITHOUT_EXTERNAL_JUSTIFICATION
```

The last metric must remain zero.
A structural controller that changes an external-domain verdict without an external-domain argument is overreaching.
