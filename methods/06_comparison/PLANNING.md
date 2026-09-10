# DSD Comparison Planning / DSD 비교론 기획

Status: **Protocol v0.1 established / CMP-CH-001 through CMP-CH-003 complete / validation in progress**  
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
PRECOMMIT: 16c4b15f93d66299a2a3890f436e1aff0076713c
RESULT: c601bd20d4d5fc6ba7dd5d4cb20b4a80f66ec880
SCORE: 40/40 PASS
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE / strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE under frozen strict family
ALL TERMINAL: COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

## Step 6 / CMP-CH-002 negative/failure challenge

```text
PRECOMMIT: c852a688c3411c7d8568e2597262c4ec32a0355e
RESULT: ca2e91f6a73d36561e77f699c3b221ada0f97dfc
SCORE: 48/48 PASS
N1 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N2 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N3 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
N4 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N5 -> NONCORRESPONDENCE / COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

Preserved distinctions:

```text
NONEXHAUSTIVE_MAP_FAILURE != RESOLVED_NONCORRESPONDENCE
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
MISSING_REQUIRED_BRIDGE != PROVEN_DIFFERENCE
FORWARD_SUCCESS != VERIFIED_INVERSE_PRESERVATION
COMPARISON_UNDERDETERMINED != COMPARISON_BLOCKED
EXHAUSTIVE_ALL_MAP_FAILURE != NONEXHAUSTIVE_FAILURE_TO_FIND
```

## Step 7 / CMP-CH-003 direct method-boundary challenge

Precommit and result:

```text
PRECOMMIT: 68d330bc43b78591be2ef2c197d6a177302789aa
RESULT: b4256d2a3c71d2a14ce9808668300ec3a879e646
SCORE: 48/48 PASS
```

Frozen neighboring boundaries and outcomes:

```text
B1 Analysis
   visible structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
   no hidden internal decomposition
   HANDOFF: ANALYSIS_REQUIRED

B2 Classification
   visible structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
   no taxonomy assignment
   HANDOFF: CLASSIFICATION_REQUIRED

B3 Transformation
   incompatible supplied representations, no transform/bridge supplied
   -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
   no unsupplied normalization
   HANDOFF: TRANSFORMATION_REQUIRED

B4 Audit
   input equal, final result equal, process trace different
   -> COMPARISON_PROFILE / COMPARISON_RESOLVED
   no conformance/pass-fail verdict
   HANDOFF: AUDIT_REQUIRED

B5 Provenance/Lineage
   snapshot structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
   lineage identity -> not_established
   HANDOFF: PROVENANCE_LINEAGE_REQUIRED
```

Boundary distinctions preserved:

```text
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
COMPARISON_MAP != UNSUPPLIED_TRANSFORMATION
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
LEGITIMATE_COMPARISON_RESULT + NEIGHBORING_HANDOFF != METHOD_BOUNDARY_FAILURE
```

All five subcases were `CONFORMANT`; gain remained `NOT_ASSESSED`. Protocol v0.1 revision and shared-core reopen were not required.

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Comparison Protocol v0.1` — commit `a1700d9`.
5. ✅ `CMP-CH-001` positive direct challenge — **40/40 PASS**.
6. ✅ `CMP-CH-002` negative/failure challenge — **48/48 PASS**.
7. ✅ `CMP-CH-003` direct method-boundary challenge — **48/48 PASS**.
8. **Next:** competent baseline `NO_GAIN` challenge.
9. Strongest-reasonable-baseline comparison.
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
DIRECT_COMPARISON_PILOTS: 3
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
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
- Case success/failure does not decide method survival, merger, absorption, or deletion.
- Later corrections are prospective under new artifact/version IDs rather than rewriting failed or superseded records.

## Next / 다음

Precommit `CMP-CH-004` competent-baseline challenge. The baseline must receive the same claim-relevant subjects, maps, map/element coverage, bridge/provenance, Property/status, equivalence and terminal-state information. Do not weaken the baseline; an honest `NO_GAIN` result is acceptable.
