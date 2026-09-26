# Analysis v0.2 — Canonical Challenge Regression Compatibility Check

Status: **TEMPORARY / NON-CANONICAL**  
Date: 2026-09-27 KST

## 0. Purpose

Check whether the proposed Analysis strengthening silently conflicts with the existing objectivity/consistency challenge corpus before running new A/B fixtures.

This is a compatibility review, not an independent validation.

## 1. ANL-CH-005 Layer Restraint

Existing rule:
- select only the minimum sufficient DSD interface layer set.

v0.2 distinction:
- `MINIMUM_SUFFICIENT_LAYER_SET` asks **which DSD layers are needed**.
- `REQUIRED_RESOLUTION_PROFILE` asks **what claim-relevant descriptive strength is needed inside the selected layers**.

Therefore these are not the same variable.

Regression guard:

```text
LAYER_SET_MINIMALITY != CLAIM_RESOLUTION_MINIMALITY
```

v0.2 must not infer that a minimal layer set automatically implies a minimal norm, moment, locality, uniformity, support, or aggregation requirement.

Compatibility result: **NO DIRECT CONFLICT FOUND**.

## 2. ANL-CH-007 Competing Explanation

Existing rule:
- compare against the strongest reasonable task-matched baseline;
- preserve baseline-preferred / tie / no analytical gain outcomes.

v0.2 guard:
- structural frontier compression or fewer branches must not itself count as external-domain superiority.
- multi-label gain must permit `STRUCTURAL_GAIN` together with `NO_DEMONSTRATED_GAIN` relative to the strongest external baseline when appropriate.

Compatibility result: **NO DIRECT CONFLICT FOUND**.

Required retention:

```text
DSD_INTERNAL_STRUCTURAL_GAIN
does not imply
EXTERNAL_BASELINE_OUTPERFORMED
```

## 3. ANL-CH-008 Procedural Unseen Transfer

Existing rule:
- pre-lock rules;
- record real holdout level;
- no post-reveal exception.

v0.2 adds:
- claim contract and required-resolution profile should also be locked before reveal when they materially affect scoring.
- dependency/representation rules added after reveal must be versioned as rule changes, not silently inserted.

Compatibility result: **SUPPORTIVE EXTENSION**.

New transfer fields proposed for A/B testing:

```text
CLAIM_CONTRACT_LOCK_STATUS
RESOLUTION_PROFILE_LOCK_STATUS
DEPENDENCY_RULESET_LOCK_STATUS
REPRESENTATION_RELATION_RULESET_LOCK_STATUS
```

## 4. ANL-CH-009 Reverse Prediction

Existing rule:
- commit directional predictions before reveal;
- preserve misses.

v0.2 adds:
- post-reveal strengthening of the required target can create a false miss;
- post-reveal weakening can create a false hit.

Therefore reverse-prediction records should distinguish:

```text
PREDICTION_LOCK
CLAIM_CONTRACT_LOCK
RESOLUTION_PROFILE_LOCK
```

Compatibility result: **SUPPORTIVE EXTENSION**.

Potential warning:
`RES-004 required resolution changed after reveal without revision record`.

## 5. Gap revealed by the current challenge corpus

The current challenge suite strongly tests:
- status discipline;
- layer restraint;
- specialization restraint;
- strongest-baseline comparison;
- transfer;
- prediction precommit.

It does **not yet directly stress-test** all v0.2 additions:

```text
GAP-1  AND/OR dependency frontier compression
GAP-2  sibling contractions sharing one latent object
GAP-3  stronger-estimate vs information-loss separation
GAP-4  frontier admissibility classification
GAP-5  false-pruning under incomparable resolution profiles
```

These gaps define the next temporary A/B fixture set.

## 6. Provisional regression verdict

```text
CANONICAL_CHALLENGE_CONFLICT: none_found_in_reviewed_cases
NEW_RULE_DUPLICATION:
  layer_minimality_vs_resolution_minimality = distinct
  strongest_baseline_vs_internal_gain = distinct
SUPPORTIVE_EXTENSIONS:
  precommit_claim_contract
  precommit_resolution_profile
UNTESTED_NEW_BEHAVIOR:
  dependency_hypergraph
  representation_common_object
  escalation_information_loss_split
  frontier_admissibility
  incomparable_profile_false_pruning
```

No canonical challenge record is modified by this compatibility check.
