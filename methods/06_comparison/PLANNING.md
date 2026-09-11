# DSD Comparison Planning / DSD 비교론 기획

Status: **Protocol v0.1 established / Step 12 second external domain complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Comparison as an independent method under **Field I: Structural Description & Understanding**. Comparison consumes two or more supplied subjects together with an explicit comparison scope, map/correspondence family, and preservation/equivalence criteria, then returns a justified correspondence/divergence profile without collapsing comparison into final-output equality.

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

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Comparison Protocol v0.1` — commit `a1700d9`.
5. ✅ `CMP-CH-001` positive direct challenge — **40/40 PASS**.
6. ✅ `CMP-CH-002` negative/failure challenge — **48/48 PASS**.
7. ✅ `CMP-CH-003` direct method-boundary challenge — **48/48 PASS**.
8. ✅ `CMP-CH-004` competent-baseline `NO_GAIN` — **50/50 PASS / NO_GAIN**.
9. ✅ `CMP-CH-005` strongest-reasonable-baseline — **60/60 PASS / NO_GAIN**.
10. ✅ `CMP-APP-001` first external application — Unicode normalization, **42/42 PASS**.
11. ✅ `CMP-CH-006` deterministic same-project retrace of CMP-APP-001 — **48/48 PASS**.
12. ✅ `CMP-APP-002` second external domain — RFC 9110 HTTP ETag comparison semantics, **48/48 PASS**.
13. **Next:** third materially different external Comparison domain.
14. Maturity audit after external breadth reaches three materially different domains if no protocol-pressure defect appears.
15. Independent-evaluator infrastructure only after maturity audit supports it.

## Constructed evidence summary

```text
CMP-CH-001  40/40 PASS
CMP-CH-002  48/48 PASS
CMP-CH-003  48/48 PASS
CMP-CH-004  50/50 PASS / NO_GAIN
CMP-CH-005  60/60 PASS / NO_GAIN
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

## Step 10 / CMP-APP-001 external application

Source lock:

```text
Unicode Standard Annex #15: Unicode Normalization Forms
Unicode version: 17.0.0
Revision: 57
Date: 2025-07-30
```

Evidence:

```text
PRECOMMIT: e1a109b9e4515336b4ee22c4d8ff216d4fd21705
RESULT: b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
SCORE: 42/42 PASS
```

Frozen comparison criteria:

```text
BINARY_IDENTITY
CANONICAL_EQUIVALENCE_VIA_NFC
COMPATIBILITY_EQUIVALENCE_VIA_NFKC
```

Execution:

```text
U1 Ç vs C+cedilla / NFC canonical
  -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
U2 same pair / binary identity
  -> NONCORRESPONDENCE / COMPARISON_RESOLVED
U3 ① vs 1 / NFC canonical
  -> NONCORRESPONDENCE / COMPARISON_RESOLVED
U4 same pair / NFKC compatibility
  -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
U5 가 vs ᄀ+ᅡ / NFC canonical
  -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
U6 reordered combining marks / NFC canonical
  -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
```

Preserved distinctions:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

All six runs were `CONFORMANT`. No independent baseline was supplied, so `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED`.

## Step 11 / CMP-CH-006 deterministic same-project retrace

Immutable retrace chain:

```text
PROTOCOL: a1700d960e0b41dfe32bf85b6334448d9104100d
TARGET PRECOMMIT: e1a109b9e4515336b4ee22c4d8ff216d4fd21705
TARGET PRECOMMIT BLOB: 640f2b5e7cf9b990a07a2e3db542b114d655122f
TARGET RESULT: b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
RETRACE PRECOMMIT: ffd374fb0b8bfd284b9cbd343d3dcf07ba9cfbe1
RETRACE RESULT: 35d0a8d7a22c19593bae8f45843668f46d775a0a
SCORE: 48/48 PASS
```

The retrace reproduced all six candidate identities, code-point pairs, criterion assignments, relation classes, terminal states, conformance records, criterion provenance, and frozen scope exclusions.

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
```

The retrace did not increment constructed or external application counts and did not establish method gain or maturity.

## Step 12 / CMP-APP-002 external application

Source lock:

```text
RFC 9110 — HTTP Semantics
Date: June 2022
§8.8.3.2 Comparison
§13.1.1 If-Match
§13.1.2 If-None-Match
```

Evidence:

```text
PRECOMMIT: f77ddb2a384b15d6a1fe041c4be5c177c52b3623
PRECOMMIT BLOB: 7478867a0013cb94ae9a7e581a77548263cbe966
RESULT: fbba59a974482ff7469d7cec5b4ce63a85c2ae61
SCORE: 48/48 PASS
```

Frozen criterion structure:

```text
STRONG_COMPARISON:
  both tags not weak + identical opaque-tags

WEAK_COMPARISON:
  identical opaque-tags regardless of weak marking

If-Match -> STRONG_COMPARISON
If-None-Match -> WEAK_COMPARISON
```

Execution:

```text
H1 W/"1" vs W/"1" / strong -> NONCORRESPONDENCE / RESOLVED
H2 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H3 W/"1" vs "1" / strong -> NONCORRESPONDENCE / RESOLVED
H4 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H5 "1" vs "1" / strong -> DIRECT_CORRESPONDENCE / RESOLVED
H6 W/"1" vs W/"2" / weak -> NONCORRESPONDENCE / RESOLVED
H7 If-Match context -> strong -> NONCORRESPONDENCE / RESOLVED
H8 If-None-Match context -> weak -> DIRECT_CORRESPONDENCE / RESOLVED
ALL CONFORMANCE: CONFORMANT
METHOD GAIN: NOT_ASSESSED
```

Preserved distinctions:

```text
STRONG_MATCH != WEAK_MATCH_IN_GENERAL
WEAK_MATCH != REPRESENTATION_IDENTITY
OPAQUE_TAG_EQUALITY_ALONE != STRONG_MATCH_WHEN_WEAK_MARKER_PRESENT
SAME_PAIR + DIFFERENT_HTTP_CRITERION -> possibly different verdict
RFC_COMPARISON_MATCH != WHOLE_REQUEST_PRECONDITION_RESULT
```

This is materially different from Unicode normalization because the standard supplies two direct validator comparison functions and context-dependent criterion selection without a normalization transform or representation bridge.

## Current evidence state / 현재 증거 상태

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Protocol establishment is infrastructure, not direct evidence.
- Constructed direct pilots and external applications remain separate evidence counters.
- Same-project retrace is reproducibility evidence but is not independent replication.
- Shared-core or neighboring-method evidence does not automatically become Comparison validation.
- Comparison criteria are frozen per task; the same pair may legitimately receive different verdicts under different criteria.
- Aggregate equality does not become structural identity.
- One map does not close an untested map family.
- Map-family coverage and claim-relevant element coverage remain separate.
- Precomparison transformations require provenance and remain Transformation operations.
- First-branch claims require earlier-stage closure; later re-convergence does not erase an earlier justified branch.
- Similar dynamic trajectories do not establish lineage identity.
- Method gain requires a frozen competent baseline.
- `NO_GAIN` is legitimate and is not evidence of method absorption or redundancy by itself.
- External standard terminology such as HTTP "equivalent" is not automatically relabelled `STRICT_EQUIVALENT`; the frozen DSD output level controls the claim.
- Case success/failure or retrace success does not decide method survival, merger, absorption, or deletion.

## Next / 다음

Add a third external Comparison application from a materially different domain, preferably physical measurement tolerance, geometric/engineering standard compatibility, or another non-textual criterion system. If three-domain external breadth is obtained without new protocol pressure, proceed to the first Comparison maturity audit.
