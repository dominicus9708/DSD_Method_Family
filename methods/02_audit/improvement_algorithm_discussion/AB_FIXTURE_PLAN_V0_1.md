# Audit v0.2 — A/B Fixture Plan

Status: **TEMPORARY / NON-CANONICAL / PRE-RUN**  
Date: 2026-09-27 KST

## 0. Purpose

Define minimal fixtures that can distinguish the canonical Audit baseline from the v0.2 extension.

The fixtures are designed to test **added discriminative power**, not to make the candidate look favorable.

Expected outputs are predeclared before any runner or manual scoring.

## 1. Baselines

```text
BASELINE_A:
  current canonical General Audit Framework
  current canonical Recording Standard
  current canonical Algorithmization Roadmap

CANDIDATE_B:
  BASELINE_A
  + GENERAL_AUDIT_EXTENSION_V0_2
```

External-domain truth is held fixed.
The candidate is not allowed to change the external standard.

## 2. Fixture F1 — Stronger-than-necessary route

Structure:

```text
Claim C requires global aggregate bound G.
Route R1 proves G directly.
Route R2 attempts pointwise uniform bound P.
Established bridge: P -> G.
No bridge: G -> P.
```

Precommitted expected audit:

```text
R1: REQUIRED_MATCH or direct sufficient route
R2: PROVEN_STRONGER_SUFFICIENT
P must not be recorded as a necessary gate.
```

Candidate-specific expected signal:
`RES-001` if P is treated as necessary.

Failure condition:
candidate prunes R2 entirely or claims P is false.

## 3. Fixture F2 — AND/OR dependency frontier

Structure:

```text
Final C requires A AND B.
A can be supplied by A1 OR A2.
B has one route B1.
A2 is currently frozen but reopenable.
```

Precommitted expected frontier representation:

```text
F1 = {A1, B1}
F2 = {A2, B1}
COMMON_MANDATORY = {B1}
```

Candidate-specific checks:
- do not count A1 and A2 as simultaneously mandatory;
- do not collapse F1/F2 into one route without proof;
- do not delete frozen A2.

Expected warning if flat OPEN counting is used:
`DEP-003`.

Failure condition:
false compression to `{A1,B1}` as uniquely necessary.

## 4. Fixture F3 — Common latent object, sibling contractions

Structure:

```text
Z = common latent object
B1 = pi1(Z)
B2 = pi2(Z)
pi1 and pi2 are non-injective and discard different coordinates.
B1 and B2 happen to have the same scalar output on one test instance.
```

Precommitted expected audit:

```text
RELATION: SIBLING_CONTRACTIONS
MERGE_GATES: no
SAME_OUTPUT_IMPLIES_SAME_STRUCTURE: no
```

Candidate-specific expected signals:
`REP-001` or `REP-002` if a merge is attempted.

Failure condition:
candidate deduplicates B1 and B2 merely because they share Z or one output value.

## 5. Fixture F4 — Stronger estimate plus information loss

Structure:

```text
Parent target allows signed cancellation.
A route replaces signed sum S with absolute mass A = sum |x_i|.
A yields a stronger sufficient upper estimate.
The absolute-value transform destroys cancellation information.
```

Precommitted expected audit:

```text
CLAIM_STRENGTH:
  stronger sufficient, if implication is established

INFORMATION_RETENTION:
  lossy
  claim relevance must be checked separately
```

Candidate-specific expected signals:
- ESC class for stronger requirement;
- INF-001 for cancellation loss if relevance is omitted.

Failure condition:
reporting the step as simply “higher resolution” with no information-loss record.

## 6. Fixture F5 — Frontier admissibility

Structure:

```text
Active gate G requires missing bridge M.
New task T computes a sharper constant inside an already sufficient dormant route D.
T does not establish M and does not invalidate G.
```

Precommitted expected class:

```text
T = OPTIONAL_STRONGER_ROUTE or SUPPORTING
T != FRONTIER_DIRECT
```

Candidate-specific expected signal:
`FRT-001` if T is reported as direct closure progress.

Failure condition:
deleting T rather than reclassifying it.

## 7. Fixture F6 — Incomparable resolution profiles

Structure:

```text
Route X:
  stronger locality
  weaker uniformity

Route Y:
  weaker locality
  stronger uniformity

No theorem establishes X -> Y or Y -> X.
```

Precommitted expected relation:

```text
INCOMPARABLE or RELATION_UNDETERMINED
```

Candidate-specific expected signal:
`RES-003` if a total ordering is forced.

Failure condition:
pruning one route using an invented scalar resolution rank.

## 8. Metrics

For each fixture record:

```text
BASELINE_A_WARNINGS
CANDIDATE_B_WARNINGS
CLAIM_RELEVANT_CORRECTIONS
FALSE_POSITIVES
FALSE_NEGATIVES
FALSE_PRUNING
DUPLICATE_GATE_COUNT
UNJUSTIFIED_ESCALATION_COUNT
MISSED_INFORMATION_LOSS
FRONTIER_CLASSIFICATION
EXTERNAL_VERDICT_CHANGE
REVIEW_STEPS
```

## 9. Acceptance rule

A candidate addition survives only if it produces claim-relevant discrimination that the baseline lacks **without** increasing false pruning or changing the external-domain verdict without external justification.

```text
SURVIVE_IF:
  added_claim_relevant_detection
  AND false_pruning_not_increased
  AND no_unsupported_external_verdict_change
```

A warning-count increase by itself is not evidence of improvement.

## 10. Runner status

```text
RUN_STATUS: NOT_RUN
REASON:
  fixture schema and expected outputs are now frozen in this document first.
NEXT:
  encode/run the same fixtures against BASELINE_A and CANDIDATE_B,
  then record discrepancies without rewriting the expected results.
```
