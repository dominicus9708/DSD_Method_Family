# Audit v0.2 — Heterogeneous Cross-Domain Fixture Precommit

Status: **TEMPORARY / NON-CANONICAL / SYNTHETIC CROSS-DOMAIN CALIBRATION**  
Date: 2026-09-27 KST

## 0. Purpose

Test whether the surviving v0.2 additions remain meaningful outside mathematical proof-frontier work.

These are synthetic cases.
They are designed to exercise domain-independent structure, not to stand in for real engineering, laboratory, administrative, or data-analysis standards.

Expected outputs are frozen before scoring.

## 1. X1 — Software: shared latent state, different projections

System:

```text
Z = versioned cache state

UI view U = pi_UI(Z)
API view A = pi_API(Z)

pi_UI and pi_API expose different fields.
A stale timestamp can appear in U while a stale payload hash can appear in A.
One test instance shows the same boolean "stale=true" in both.
```

Question:
May U and A be merged as one defect/gate solely because they share Z and the same one-bit output?

Expected:

```text
RELATION: SIBLING_CONTRACTIONS or distinct projections
MERGE_AS_IDENTICAL: no
COMMON_PARENT: yes
CLAIM_RELEVANT_EQUIVALENCE: not established
```

Failure:
shared latent parent or same output is used as sufficient proof of identity.

## 2. X2 — Experimental specification: average criterion vs pointwise-uniform criterion

Declared acceptance claim:

```text
Average chamber temperature over the declared 10-minute interval <= 30 C.
```

Proposed route:

```text
Require every sensor reading at every sampled second <= 30 C.
```

Assume the pointwise-uniform requirement implies the average criterion, but the reverse implication is not established.

Expected:

```text
POINTWISE_UNIFORM:
  PROVEN_STRONGER_SUFFICIENT

NECESSARY_FOR_DECLARED_CLAIM:
  no evidence

DO_NOT_REWRITE_ACCEPTANCE_CLAIM:
  yes
```

Failure:
the stronger route is silently promoted into the declared acceptance standard.

## 3. X3 — Procedural workflow: AND/OR authorization structure

A release requires:

```text
Checksum verification C
AND
either:
  manual authorization M
  OR
  validated automated certificate V
```

M is currently unavailable but may reopen if an approver returns.
V is active.

Expected frontier families:

```text
F1 = {C, M}
F2 = {C, V}
COMMON_MANDATORY = {C}
M_STATE = FROZEN_OR_DORMANT_WITH_REOPEN_CONDITION
```

Failure:
M and V are counted as simultaneously mandatory,
or M is deleted because V is currently active.

## 4. X4 — Data analysis: signed balance vs absolute deviation

Declared question:

```text
Does the signed residual balance sum to zero?
```

Transformation:

```text
S = sum r_i
A = sum |r_i|
```

Expected:

```text
S -> A:
  information-losing with respect to sign/cancellation
  not a reversible representation

A may support a different/stronger deviation bound,
but it does not preserve the original signed-balance information.
```

Failure:
A is treated as merely a "higher-resolution form" of S.

## 5. X5 — Software project frontier: useful work that does not close the blocker

Active release blocker:

```text
G = schema migration compatibility bridge is missing.
```

New task:

```text
T = optimize rendering performance of an already passing UI path.
```

Expected:

```text
T_CLASS:
  SUPPORTING or NON_FRONTIER_EXPLORATION

T_DELETED:
  no

T_COUNTS_AS_DIRECT_RELEASE_BLOCKER_CLOSURE:
  no
```

Failure:
T is reported as direct closure progress or discarded as useless.

## 6. X6 — Incomparable coverage profiles

Two test strategies:

```text
Strategy P:
  exhaustive subsystem-state coverage
  only one software version

Strategy Q:
  all supported software versions
  sampled subsystem-state coverage
```

No theorem or empirical standard establishes P > Q or Q > P for the declared goal.

Expected:

```text
RELATION:
  INCOMPARABLE or RELATION_UNDETERMINED

SCALAR_COMPLETENESS_RANK:
  forbidden without an explicit weighting/ordering rule
```

Failure:
one strategy is pruned using an invented one-dimensional "resolution" score.

## 7. Scoring fields

```text
FIXTURE_ID
BASELINE_A_DETECTABILITY
CANDIDATE_B_DETECTABILITY
CLAIM_RELEVANT_ADDED_DISCRIMINATION
FALSE_PRUNING
UNSUPPORTED_MERGE
UNSUPPORTED_ESCALATION
MISSED_INFORMATION_LOSS
FRONTIER_MISCLASSIFICATION
EXTERNAL_STANDARD_REWRITE
NOTES
```

## 8. Precommitted interpretation rule

The candidate survives cross-domain calibration only when:

1. it adds a distinction that is not merely mathematical vocabulary;
2. it does not overwrite the domain's declared standard;
3. it does not delete alternative/supporting work merely because it is non-frontier;
4. it does not infer equivalence from shared causes or outputs;
5. it does not force incomparable descriptive profiles into a total order.

```text
RUN_STATUS: NOT_SCORED_YET
```
