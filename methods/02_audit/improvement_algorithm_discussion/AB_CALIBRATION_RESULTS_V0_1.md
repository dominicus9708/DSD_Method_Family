# Audit v0.2 — Manual A/B Calibration Results

Status: **TEMPORARY / NON-CANONICAL / SAME-SESSION CALIBRATION**  
Date: 2026-09-27 KST

Expected outputs were frozen first in:
- `AB_FIXTURE_PLAN_V0_1.md`
- pre-result commit: `0dc75fa9f93622742bc1659df5595fedd94706a9`

This record does not rewrite the precommitted fixture expectations.

## 0. Scope and limitation

This is a manual structural comparison of:

```text
BASELINE_A =
  current canonical General Audit Framework
  + current Recording Standard
  + current Algorithmization Roadmap

CANDIDATE_B =
  BASELINE_A
  + GENERAL_AUDIT_EXTENSION_V0_2
```

The same analysis session designed the fixtures and scored them.
Therefore this is calibration, not independent validation.

## 1. F1 — Stronger-than-necessary route

Baseline A already locks scope/resolution and restricts verdicts to the maximum supported claim.
However, it does not explicitly require a proof that a stronger intermediate target is **necessary** for the parent claim.

```text
BASELINE_A:
  can preserve scope
  can prevent overclaim in final verdict
  necessity-vs-strong-sufficiency distinction = implicit / reviewer-dependent

CANDIDATE_B:
  explicit REQUIRED_MATCH / PROVEN_STRONGER_SUFFICIENT relation
  RES-001 available if stronger target is misreported as necessary
```

Result:
```text
ADDED_DISCRIMINATIVE_POWER: yes
FALSE_PRUNING_OBSERVED: no
EXTERNAL_VERDICT_CHANGE: no
```

## 2. F2 — AND/OR dependency frontier

Baseline A records alternatives, bridges, and transitions.
It can preserve A1/A2 as alternatives, but it does not define a typed AND/OR gate structure or minimal frontier families.

```text
BASELINE_A:
  alternatives can be retained
  gate counting / AND-OR semantics = not explicit

CANDIDATE_B:
  {A1,B1} and {A2,B1} preserved as two frontier families
  B1 identified as common mandatory gate
  A1 and A2 not double-counted as simultaneous mandatory gates
```

Result:
```text
ADDED_DISCRIMINATIVE_POWER: yes
FALSE_COMPRESSION_OBSERVED: no
FALSE_PRUNING_OBSERVED: no
EXTERNAL_VERDICT_CHANGE: no
```

## 3. F3 — Common latent object with sibling contractions

Baseline A is already strong here:
- same output does not prove unique cause/support/decomposition;
- aggregation/information-loss/injectivity/reconstruction are explicitly audited.

Therefore the unsafe conclusion “same scalar output -> same structure” is already rejectable under the canonical core.

Candidate B adds a more precise representation taxonomy:

```text
Z -> B1 = pi1(Z)
Z -> B2 = pi2(Z)

RELATION: SIBLING_CONTRACTIONS
MERGE_GATES: no
```

Result:
```text
NEW_CORE_PRINCIPLE_REQUIRED: no
IMPLEMENTATION_PRECISION_GAIN: yes
DUPLICATE_DETECTION_GAIN: possible
FALSE_MERGE_OBSERVED: no
EXTERNAL_VERDICT_CHANGE: no
```

Provisional interpretation:
AUD-Δ04 should probably be an **algorithmic specialization of existing aggregation/reconstruction safeguards**, not an independent new universal principle.

## 4. F4 — Stronger estimate plus information loss

Baseline A explicitly audits aggregation and information loss, so it can detect cancellation destruction if the reviewer checks it.

What is not explicit in the baseline is that a transform may simultaneously:

1. demand a stronger sufficient claim; and
2. retain less source information.

Candidate B records these on separate ledgers.

```text
CLAIM_STRENGTH: PROVEN_STRONGER_SUFFICIENT
INFORMATION_RETENTION: LOSSY
```

Result:
```text
ADDED_DISCRIMINATIVE_POWER: yes
CORE_INFORMATION_LOSS_PRINCIPLE_ALREADY_EXISTS: yes
ORTHOGONAL_LEDGER_GAIN: yes
EXTERNAL_VERDICT_CHANGE: no
```

## 5. F5 — Frontier admissibility

Baseline A can record alternatives and unresolved regions but has no explicit rule for whether a new piece of work counts as **canonical frontier progress**.

Candidate B classifies the sharper dormant-route calculation as:

```text
OPTIONAL_STRONGER_ROUTE
or
SUPPORTING
```

without deleting it.

Result:
```text
ADDED_OPERATIONAL_POWER: yes
FALSE_PRUNING_OBSERVED: no
RESOURCE_REPORTING_GAIN: yes
EXTERNAL_VERDICT_CHANGE: no
```

## 6. F6 — Incomparable resolution profiles

Baseline A fixes descriptive resolution but does not provide a multi-axis comparison rule.

Candidate B refuses to invent one scalar order:

```text
X vs Y = INCOMPARABLE
or RELATION_UNDETERMINED
```

unless an implication theorem is supplied.

Result:
```text
ADDED_DISCRIMINATIVE_POWER: yes
FALSE_ORDERING_AVOIDED: yes
FALSE_PRUNING_OBSERVED: no
EXTERNAL_VERDICT_CHANGE: no
```

## 7. Calibration summary

```text
F1 claim-to-resolution:
  SURVIVES_TEMP_CALIBRATION

F2 AND/OR dependency frontier:
  SURVIVES_TEMP_CALIBRATION

F3 common-object representation taxonomy:
  SURVIVES_AS_IMPLEMENTATION_SPECIALIZATION
  NOT_YET_JUSTIFIED_AS_NEW_CORE_PRINCIPLE

F4 escalation vs information-loss split:
  SURVIVES_TEMP_CALIBRATION
  information-loss principle itself already canonical

F5 frontier admissibility:
  SURVIVES_TEMP_CALIBRATION

F6 incomparable profile guard:
  SURVIVES_TEMP_CALIBRATION
```

## 8. Candidate status after this calibration

```text
AUD-Δ01  SURVIVES_TEMP_CALIBRATION
AUD-Δ02  SURVIVES_TEMP_CALIBRATION
AUD-Δ03  SURVIVES_TEMP_CALIBRATION
AUD-Δ04  RETAIN_AS_ALGORITHMIC_SPECIALIZATION
AUD-Δ05  ABSORB_AS_OPERATIONAL_SPECIALIZATION
AUD-Δ06  KEEP_AS_DOMAIN_REPRODUCIBILITY_SPECIALIZATION
AUD-Δ07  SURVIVES_TEMP_CALIBRATION
AUD-Δ08  ABSORB_INTO_EXISTING_CORE_SAFEGUARD
AUD-Δ09  ABSORB_INTO_SC-08
```

## 9. What has not been established

This calibration does not establish:
- lower real-world review cost;
- lower error rate on independent cases;
- transfer outside mathematics/research workflows;
- superior domain truth judgments;
- safe automatic pruning under arbitrary dependency graphs.

Those require heterogeneous held-out fixtures.

## 10. Next strengthening gate

Before canonical merge, test the surviving additions against at least:

```text
SOFTWARE:
  multiple bug reports / one latent state / different projections

EXPERIMENT OR SPECIFICATION:
  aggregate acceptance criterion vs unnecessarily uniform local criterion

ADMINISTRATIVE OR PROCEDURAL WORKFLOW:
  AND/OR prerequisites and alternative authorization routes

DATA ANALYSIS:
  signed or component-resolved information lost by aggregation
```

The goal of the next gate is to determine which additions are genuinely general and which are merely proof-frontier specializations.
