# DSD Comparison Planning / DSD 비교론 기획

Status: **Protocol v0.1 established / CMP-CH-001 through CMP-CH-004 complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Comparison as an independent method under **Field I: Structural Description & Understanding**. Comparison consumes two or more supplied subjects together with an explicit comparison scope, map/correspondence family, and preservation/equivalence criteria, then returns a justified correspondence/divergence profile without collapsing comparison into final-output equality.

## Current source/interface lock / 현재 기준 잠금

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
DSD_INTERFACE_PROFILE.md
METHOD_BOUNDARY_MATRIX.md
```

## Protocol lineage / 프로토콜 계보

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Executable protocol commit:

```text
a1700d960e0b41dfe32bf85b6334448d9104100d
```

## Step 1-4 summary

```text
Step 1 task interface draft: complete
Step 2 pre-protocol boundary attacks: 16
Step 3 Boundary Amendment 001: complete
Step 4 executable Protocol v0.1: complete
```

Boundary planning result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

## Step 5 / CMP-CH-001 positive direct challenge

```text
PRECOMMIT: 16c4b15
RESULT: c601bd2
SCORE: 40/40 PASS
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE / strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE under frozen strict family
```

## Step 6 / CMP-CH-002 negative/failure challenge

```text
PRECOMMIT: c852a68
RESULT: ca2e91f
SCORE: 48/48 PASS
N1 -> COMPARISON_UNDERDETERMINED
N2 -> COMPARISON_UNDERDETERMINED
N3 -> COMPARISON_BLOCKED
N4 -> COMPARISON_UNDERDETERMINED
N5 -> NONCORRESPONDENCE / COMPARISON_RESOLVED
```

Preserved distinctions include non-exhaustive failure versus resolved noncorrespondence, partial element coverage versus strict equivalence, missing bridge versus proven difference, and forward success versus verified inverse preservation.

## Step 7 / CMP-CH-003 direct method-boundary challenge

```text
PRECOMMIT: 68d330b
RESULT: b4256d2
SCORE: 48/48 PASS
```

```text
Analysis -> visible STRICT_EQUIVALENT + ANALYSIS_REQUIRED
Classification -> visible STRICT_EQUIVALENT + CLASSIFICATION_REQUIRED
Transformation -> COMPARISON_BLOCKED + TRANSFORMATION_REQUIRED
Audit -> resolved comparison profile + AUDIT_REQUIRED
Provenance/Lineage -> snapshot STRICT_EQUIVALENT, lineage not_established + PROVENANCE_LINEAGE_REQUIRED
```

All subcases remained `CONFORMANT`; gain was `NOT_ASSESSED`.

## Step 8 / CMP-CH-004 competent-baseline NO_GAIN

Precommit and result:

```text
PRECOMMIT: 0d96d6ba83e25f2e14dba47c309cb74da7c71bad
RESULT: 4cacd55f73b2f4180ec8f11854d8dbe40974f536
BASELINE: B0_TYPED_COMPARISON_LEDGER
SCORE: 50/50 PASS
```

Five frozen task classes:

```text
Q1 strict equivalence + typed status
Q2 encoded correspondence + supplied bridge provenance
Q3 non-exhaustive map failure + untested remainder
Q4 aggregate collision + structural noncorrespondence
Q5 missing claim-required bridge + blocked terminal
```

DSD and B0 matched on every frozen task-level result:

```text
Q1 -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
Q2 -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
Q3 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
Q4 -> NONCORRESPONDENCE / COMPARISON_RESOLVED
Q5 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
```

Gain ledger:

```text
G1 RELATION_CLASS_SEPARATION_GAIN: NOT_ESTABLISHED
G2 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G3 COVERAGE_AND_CLOSURE_GAIN: NOT_ESTABLISHED
G4 BRIDGE_PROVENANCE_GAIN: NOT_ESTABLISHED
G5 AGGREGATE_COLLISION_GAIN: NOT_ESTABLISHED
G6 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

The baseline received the same claim-relevant records and was explicitly allowed to preserve every scored distinction. This filled the first successful Comparison `NO_GAIN` and competent-baseline categories without manufacturing superiority.

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Comparison Protocol v0.1` — commit `a1700d9`.
5. ✅ `CMP-CH-001` positive direct challenge — **40/40 PASS**.
6. ✅ `CMP-CH-002` negative/failure challenge — **48/48 PASS**.
7. ✅ `CMP-CH-003` direct method-boundary challenge — **48/48 PASS**.
8. ✅ `CMP-CH-004` competent-baseline `NO_GAIN` challenge — **50/50 PASS / NO_GAIN**.
9. **Next:** strongest-reasonable-baseline comparison.
10. First external application.
11. Deterministic retrace/reproducibility record.
12. Additional materially different external domains.
13. Maturity audit after evidence architecture is materially populated.
14. Independent-evaluator infrastructure only after protocol/evidence stability justifies it.

## Current evidence state / 현재 증거 상태

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
DIRECT_COMPARISON_PILOTS: 4
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 1
BASELINE_COMPARISON_CASES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Protocol establishment is infrastructure, not direct evidence.
- Shared-core or neighboring-method evidence does not automatically become Comparison validation.
- Aggregate equality does not become structural identity.
- One map does not close an untested map family.
- Map-family coverage and claim-relevant element coverage remain separate.
- Precomparison transformations require provenance and remain Transformation operations.
- First-branch claims require earlier-stage closure.
- Similarity does not establish lineage identity.
- Legitimate Comparison output may coexist with a neighboring-method handoff.
- A missing neighboring operation that is a prerequisite for substantive comparison may produce `COMPARISON_BLOCKED` without protocol nonconformance.
- Method gain requires a frozen competent baseline.
- `NO_GAIN` is a legitimate comparative result and is not evidence of method absorption or redundancy by itself.
- Case success/failure does not decide method survival, merger, absorption, or deletion.
- Later corrections are prospective under new artifact/version IDs rather than rewriting failed or superseded records.

## Next / 다음

Precommit `CMP-CH-005` strongest-reasonable-baseline comparison. It must be materially richer than `CMP-CH-004`, activate first-branch closure, direction/inverse requirements, partial-versus-global element coverage, representation/bridge provenance, and possibly lineage-gated dynamic comparison, and give the strong baseline all claim-relevant information. Another honest `NO_GAIN` remains acceptable.
