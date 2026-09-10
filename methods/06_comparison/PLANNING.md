# DSD Comparison Planning / DSD 비교론 기획

Status: **Protocol v0.1 established / CMP-CH-001 and CMP-CH-002 complete / validation in progress**  
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
```

```text
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE / strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE under frozen strict family
ALL TERMINAL: COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

## Step 6 / CMP-CH-002 negative/failure challenge

Precommit and result:

```text
PRECOMMIT: c852a688c3411c7d8568e2597262c4ec32a0355e
RESULT: ca2e91f6a73d36561e77f699c3b221ada0f97dfc
SCORE: 48/48 PASS
```

Frozen terminal distinctions:

```text
N1 non-exhaustive map family
   one evaluated map fails, another remains untested
   -> UNDETERMINED_CORRESPONDENCE
   -> COMPARISON_UNDERDETERMINED

N2 partial Property/status element coverage
   structural map closes but readiness(y1) withheld
   -> UNDETERMINED_CORRESPONDENCE
   -> COMPARISON_UNDERDETERMINED

N3 missing claim-required semantic bridge
   substantive comparison cannot start legitimately
   -> UNDETERMINED_CORRESPONDENCE
   -> COMPARISON_BLOCKED

N4 forward map succeeds but inverse-preservation evidence remains unverified in frozen run
   -> UNDETERMINED_CORRESPONDENCE
   -> COMPARISON_UNDERDETERMINED

N5 exhaustive two-bijection family, both relation-preservation failures
   -> NONCORRESPONDENCE
   -> COMPARISON_RESOLVED
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

All five subcases were `CONFORMANT`; gain was `NOT_ASSESSED` because no baseline was present. Protocol v0.1 revision was not required.

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Comparison Protocol v0.1` — commit `a1700d9`.
5. ✅ `CMP-CH-001` positive direct challenge — **40/40 PASS**.
6. ✅ `CMP-CH-002` negative/failure challenge — **48/48 PASS**.
7. **Next:** direct method-boundary challenge.
8. `NO_GAIN` comparison against a competent baseline.
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
DIRECT_COMPARISON_PILOTS: 2
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 0
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
- Method gain requires a frozen competent baseline.
- Case success/failure does not decide method survival, merger, absorption, or deletion.
- Later corrections are prospective under new artifact/version IDs rather than rewriting failed or superseded records.

## Next / 다음

Precommit `CMP-CH-003` direct method-boundary challenge. The fixture should preserve an executable Comparison core while presenting requests that would require hidden Analysis, Classification, Transformation, Audit, and Provenance/Lineage work. Comparison must emit explicit handoffs rather than absorb those operations.
