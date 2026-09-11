# CMP-APP-002 Result / HTTP ETag Comparison Semantics 외부 적용

Status: **48/48 PASS**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Precommit commit: **f77ddb2a384b15d6a1fe041c4be5c177c52b3623**  
Precommit blob: **7478867a0013cb94ae9a7e581a77548263cbe966**

## 1. Frozen source confirmation

The execution used only the precommitted source lock:

```text
RFC 9110 — HTTP Semantics
RFC Editor / IETF Standards Track
June 2022
§8.8.3.2 Comparison
§13.1.1 If-Match
§13.1.2 If-None-Match
```

Confirmed source rules:

```text
STRONG_COMPARISON:
  match iff both entity tags are not weak
  AND opaque-tags match character-by-character.

WEAK_COMPARISON:
  match iff opaque-tags match character-by-character,
  regardless of weak marking.

If-Match:
  uses STRONG_COMPARISON.

If-None-Match:
  uses WEAK_COMPARISON.
```

No extra HTTP equivalence relation was imported.

## 2. Execution results

### H1 — weak/weak same opaque tag under strong comparison

```text
LEFT: W/"1"
RIGHT: W/"1"
CRITERION: STRONG_COMPARISON
WEAK_MARKER_CHECK: both weak -> strong criterion fails
OPAQUE_TAG_CHECK: equal
RFC_MATCH: no
DSD_CORRESPONDENCE_CLASS: NONCORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The equal opaque tag is insufficient for strong comparison because both tags carry the weak marker.

### H2 — same pair under weak comparison

```text
LEFT: W/"1"
RIGHT: W/"1"
CRITERION: WEAK_COMPARISON
OPAQUE_TAG_CHECK: equal
WEAK_MARKER_EFFECT: ignored by frozen weak criterion
RFC_MATCH: yes
DSD_CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

H1 and H2 preserve the same subjects while changing only the supplied comparison criterion.

### H3 — weak/strong same opaque tag under strong comparison

```text
LEFT: W/"1"
RIGHT: "1"
CRITERION: STRONG_COMPARISON
WEAK_MARKER_CHECK: left weak -> strong criterion fails
OPAQUE_TAG_CHECK: equal
RFC_MATCH: no
DSD_CORRESPONDENCE_CLASS: NONCORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

### H4 — same pair under weak comparison

```text
LEFT: W/"1"
RIGHT: "1"
CRITERION: WEAK_COMPARISON
OPAQUE_TAG_CHECK: equal
WEAK_MARKER_EFFECT: ignored by frozen weak criterion
RFC_MATCH: yes
DSD_CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

### H5 — two strong tags with same opaque tag under strong comparison

```text
LEFT: "1"
RIGHT: "1"
CRITERION: STRONG_COMPARISON
WEAK_MARKER_CHECK: neither weak
OPAQUE_TAG_CHECK: equal
RFC_MATCH: yes
DSD_CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The result is deliberately not upgraded to `STRICT_EQUIVALENT`; the frozen output asks only for correspondence under the external comparison function.

### H6 — different opaque tags under weak comparison

```text
LEFT: W/"1"
RIGHT: W/"2"
CRITERION: WEAK_COMPARISON
OPAQUE_TAG_CHECK: different
RFC_MATCH: no
DSD_CORRESPONDENCE_CLASS: NONCORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Weak comparison ignores weakness marking, not opaque-tag difference.

### H7 — If-Match context

```text
CONTEXT: If-Match
PRESENTED TAG: W/"1"
CURRENT TAG: "1"
CRITERION_PROVENANCE: RFC 9110 §13.1.1
SELECTED_CRITERION: STRONG_COMPARISON
RFC_COMPARISON_MATCH: no
DSD_CORRESPONDENCE_CLASS: NONCORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Only the entity-tag comparison is classified. No request outcome or status code is inferred.

### H8 — If-None-Match context

```text
CONTEXT: If-None-Match
PRESENTED TAG: W/"1"
CURRENT TAG: "1"
CRITERION_PROVENANCE: RFC 9110 §13.1.2
SELECTED_CRITERION: WEAK_COMPARISON
RFC_COMPARISON_MATCH: yes
DSD_CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Again, `RFC_COMPARISON_MATCH: yes` is not a claim that the If-None-Match precondition itself evaluates true; request-level precondition evaluation was outside the frozen output scope.

## 3. Criterion-sensitive comparison result

The external domain independently exhibits a criterion-sensitive comparison structure:

```text
W/"1" vs W/"1"
  STRONG_COMPARISON -> NONCORRESPONDENCE
  WEAK_COMPARISON   -> DIRECT_CORRESPONDENCE

W/"1" vs "1"
  STRONG_COMPARISON -> NONCORRESPONDENCE
  WEAK_COMPARISON   -> DIRECT_CORRESPONDENCE
```

Therefore this application preserves:

```text
SAME_SUBJECT_PAIR
+ DIFFERENT_SUPPLIED_COMPARISON_CRITERION
-> DIFFERENT_JUSTIFIED_COMPARISON_VERDICT
```

without treating the differing verdicts as protocol inconsistency.

## 4. Scope discipline

The execution did not infer any of the following:

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

Preserved guards:

```text
STRONG_MATCH != WEAK_MATCH_IN_GENERAL
WEAK_MATCH != REPRESENTATION_IDENTITY
OPAQUE_TAG_EQUALITY_ALONE != STRONG_MATCH_WHEN_WEAK_MARKER_PRESENT
SAME_PAIR + DIFFERENT_HTTP_CRITERION -> possibly different verdict
IF_MATCH_CONTEXT -> STRONG_COMPARISON
IF_NONE_MATCH_CONTEXT -> WEAK_COMPARISON
RFC_COMPARISON_MATCH != WHOLE_REQUEST_PRECONDITION_RESULT
```

## 5. Precommitted scoring

```text
A. source / immutable precommit integrity       8/8
B. candidate relation verdicts                 16/16
C. criterion and context provenance            10/10
D. scope / closure discipline                   8/8
E. evidence-count / interpretation discipline   6/6
TOTAL                                          48/48 PASS
FAILED                                          0
```

Detailed result:

```text
A1-A8 PASS
B1-B16 PASS
C1-C10 PASS
D1-D8 PASS
E1-E6 PASS
```

## 6. Evidence effect

```text
DIRECT_COMPARISON_PILOTS: 5
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

External domains now represented:

```text
1. Unicode normalization / text representation equivalence
2. HTTP validator and conditional-request comparison semantics
```

The second application is materially different from normalization: no string-normalization transform or representation bridge is executed; the external standard directly supplies two comparison functions over validator fields and prescribes which criterion applies in two request contexts.

## 7. Three-ledger result

```text
TERMINAL_COMPARISON_STATUS:
  COMPARISON_RESOLVED for H1-H8

COMPARISON_PROTOCOL_CONFORMANCE:
  CONFORMANT for H1-H8

COMPARISON_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

No baseline was supplied, so no method-gain claim is made.

## 8. Interpretation discipline

```text
EXTERNAL_PASS != METHOD_GAIN_PROOF
EXTERNAL_PASS != INDEPENDENT_VALIDATION
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_FAIL != METHOD_DELETION_PROOF
SAME_PAIR_DIFFERENT_CRITERION != PROTOCOL_INCONSISTENCY
HTTP_MATCH != REPRESENTATION_IDENTITY
```

## 9. Verdict

```text
APPLICATION_VERDICT: PASS
SCORE: 48/48
```

`CMP-APP-002` supports the current Comparison protocol's ability to preserve externally supplied criterion-dependent correspondence without collapsing weak/strong comparison, context provenance, or comparison match into broader identity claims.
