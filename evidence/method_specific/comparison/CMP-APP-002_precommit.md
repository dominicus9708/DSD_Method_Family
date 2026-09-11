# CMP-APP-002 Precommit / HTTP ETag Comparison Semantics 외부 적용 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**

## 1. Evidence identity

```text
CASE_ID: CMP-APP-002
CASE_CLASS: external_application
EXTERNAL_DOMAIN: HTTP validator / conditional-request semantics
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
BASELINE: none
METHOD_GAIN: NOT_ASSESSED
```

Purpose: test whether DSD Comparison preserves criterion-dependent correspondence in an external protocol domain where the same entity-tag pair can match under one standardized comparison function and fail under another.

## 2. Source lock

Primary source:

```text
RFC 9110 — HTTP Semantics
Publisher: RFC Editor / IETF Standards Track
Date: June 2022
Sections used:
  8.8.3.2 Comparison
  13.1.1 If-Match
  13.1.2 If-None-Match
Official URI:
  https://www.rfc-editor.org/rfc/rfc9110.html
```

Frozen source facts:

```text
S1 STRONG_COMPARISON:
   entity tags match only when both are not weak and opaque-tags match character-by-character.

S2 WEAK_COMPARISON:
   entity tags match when opaque-tags match character-by-character regardless of weak marking.

S3 RFC Table 3 records:
   W/"1" vs W/"1" -> strong no match / weak match
   W/"1" vs W/"2" -> strong no match / weak no match
   W/"1" vs "1"   -> strong no match / weak match
   "1"   vs "1"   -> strong match / weak match

S4 If-Match requires the strong comparison function.
S5 If-None-Match requires the weak comparison function.
```

No other HTTP equality, cache-validity, representation-identity, content-identity, resource-identity, or application-semantic relation is imported.

## 3. Comparison task lock

```text
TASK_SCOPE:
  compare supplied entity-tag pairs only under the frozen RFC comparison criterion

CLAIMED_OUTPUT_LEVEL:
  CORRESPONDENCE_CLASSIFICATION

TARGET_RESOLUTION:
  entity-tag weak marker + opaque-tag under selected RFC comparison function

COMPARISON_DIRECTIONALITY:
  symmetric for the selected comparison function

MAP_FAMILY_COVERAGE:
  exhaustive for each frozen pair/criterion instance

COMPARISON_ELEMENT_COVERAGE:
  weak-marker status: exhaustive where strong criterion requires it
  opaque-tag equality: exhaustive
  other HTTP representation/resource properties: not_applicable

MAP_PROPERTY_REQUIREMENT_PROFILE:
  custom_supplied_criterion

REVERSE_DIRECTION_OR_INVERSE_POLICY:
  not_required

PRECOMPARISON_TRANSFORMATION_POLICY:
  none_required

ENCODING_OR_BRIDGE_RULE:
  none

LINEAGE_IDENTITY_CLAIM_POLICY:
  not_claimed

AGGREGATE_READOUTS_IF_ANY:
  none
```

## 4. Relation-class policy

This application does not relabel RFC's word "equivalent" as DSD `STRICT_EQUIVALENT`.

For this frozen output level:

```text
RFC selected comparison says match
  -> DIRECT_CORRESPONDENCE

RFC selected comparison says no match
  -> NONCORRESPONDENCE
```

Reason: the task asks only whether the supplied entity-tag pair corresponds under the selected external comparison function. It does not claim complete structural or representation identity.

Required guards:

```text
STRONG_MATCH != WEAK_MATCH_IN_GENERAL
WEAK_MATCH != REPRESENTATION_IDENTITY
OPAQUE_TAG_EQUALITY_ALONE != STRONG_MATCH_WHEN_WEAK_MARKER_PRESENT
SAME_PAIR + DIFFERENT_HTTP_CRITERION -> possibly different verdict
IF_MATCH_CONTEXT -> STRONG_COMPARISON
IF_NONE_MATCH_CONTEXT -> WEAK_COMPARISON
```

## 5. Frozen candidates

### H1

```text
LEFT:  W/"1"
RIGHT: W/"1"
CRITERION: STRONG_COMPARISON
EXPECTED RFC MATCH: no
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H2

```text
LEFT:  W/"1"
RIGHT: W/"1"
CRITERION: WEAK_COMPARISON
EXPECTED RFC MATCH: yes
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H3

```text
LEFT:  W/"1"
RIGHT: "1"
CRITERION: STRONG_COMPARISON
EXPECTED RFC MATCH: no
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H4

```text
LEFT:  W/"1"
RIGHT: "1"
CRITERION: WEAK_COMPARISON
EXPECTED RFC MATCH: yes
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H5

```text
LEFT:  "1"
RIGHT: "1"
CRITERION: STRONG_COMPARISON
EXPECTED RFC MATCH: yes
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H6

```text
LEFT:  W/"1"
RIGHT: W/"2"
CRITERION: WEAK_COMPARISON
EXPECTED RFC MATCH: no
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H7

```text
CONTEXT: If-Match
PRESENTED TAG: W/"1"
CURRENT TAG:   "1"
CRITERION SOURCE: RFC 9110 §13.1.1 -> STRONG_COMPARISON
EXPECTED RFC MATCH: no
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### H8

```text
CONTEXT: If-None-Match
PRESENTED TAG: W/"1"
CURRENT TAG:   "1"
CRITERION SOURCE: RFC 9110 §13.1.2 -> WEAK_COMPARISON
EXPECTED RFC MATCH: yes
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

## 6. Scope exclusions

The application must not infer:

```text
same HTTP resource identity
same representation bytes
same selected-representation metadata
cache freshness outside the frozen precondition rule
request success/failure status code
range-request validity
ETag generation correctness
origin-server conformance beyond the selected comparison rule
cryptographic hash equality
application-level semantic equality
```

## 7. Three-ledger lock

For H1-H8:

```text
TERMINAL_COMPARISON_STATUS:
  COMPARISON_RESOLVED

COMPARISON_PROTOCOL_CONFORMANCE:
  CONFORMANT

COMPARISON_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

No baseline is supplied, so neither `GAIN_ESTABLISHED` nor `NO_GAIN` may be asserted.

## 8. Precommitted scoring

Total required checks: **48**.

```text
A. source / immutable precommit integrity:      8
B. candidate relation verdicts:                16
C. criterion and context provenance:           10
D. scope / closure discipline:                  8
E. evidence-count and interpretation discipline:6
```

Detailed checks:

```text
A1 Protocol remains v0.1 at frozen protocol commit.
A2 RFC number/title exact.
A3 RFC date exact.
A4 §8.8.3.2 source used for strong/weak comparison.
A5 §13.1.1 source used for If-Match criterion.
A6 §13.1.2 source used for If-None-Match criterion.
A7 H1-H8 identities unchanged after precommit.
A8 No post-hoc candidate or criterion replacement.

B1-B8 H1-H8 exact DSD correspondence class.
B9-B16 H1-H8 exact COMPARISON_RESOLVED terminal.

C1 H1 strong no-match retained.
C2 H2 same pair weak match retained.
C3 H3 weak-vs-strong strong no-match retained.
C4 H4 same pair weak match retained.
C5 H5 strong-vs-strong same opaque tag strong match retained.
C6 H6 different opaque tags weak no-match retained.
C7 H7 If-Match -> strong criterion retained.
C8 H8 If-None-Match -> weak criterion retained.
C9 Match cases are not upgraded to STRICT_EQUIVALENT.
C10 Same-pair/different-criterion distinction retained.

D1 Weak match is not representation identity.
D2 Strong no-match is not resource nonidentity.
D3 No hidden normalization/transformation introduced.
D4 No lineage claim introduced.
D5 No aggregate claim introduced.
D6 No ETag-generation validity claim introduced.
D7 No request-status outcome claim introduced.
D8 All frozen scope exclusions retained.

E1 External application count increments by exactly one on PASS.
E2 External domain count increments by exactly one on PASS.
E3 External application pass count increments by exactly one on PASS.
E4 Direct constructed-pilot count remains unchanged.
E5 Reproducibility counts remain unchanged.
E6 Independent validation/maturity remain unchanged.
```

Decision:

```text
48/48 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

## 9. Evidence-count lock before execution

```text
DIRECT_COMPARISON_PILOTS: 5
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

A PASS may change only:

```text
EXTERNAL_COMPARISON_APPLICATIONS: 1 -> 2
EXTERNAL_COMPARISON_DOMAINS: 1 -> 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1 -> 2
```

## 10. Registry discipline

```text
EXTERNAL_PASS != METHOD_GAIN_PROOF
EXTERNAL_PASS != INDEPENDENT_VALIDATION
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_FAIL != METHOD_DELETION_PROOF
SAME_PAIR_DIFFERENT_CRITERION != PROTOCOL_INCONSISTENCY
```
