# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **Protocol v0.1 established / strongest-reasonable baseline established at constructed-evidence level / two external domains PASS / deterministic same-project retrace PASS / validation in progress**

This lane records evidence that directly tests **DSD Comparison / DSD 비교론**.

## Current development state

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

Constructed direct-pilot counts, external-application counts, and reproducibility counts are separate.

## Protocol and constructed evidence

```text
PROTOCOL_v0.1 creation: a1700d9
CMP-CH-001: 40/40 PASS
CMP-CH-002: 48/48 PASS
CMP-CH-003: 48/48 PASS
CMP-CH-004: 50/50 PASS / NO_GAIN
CMP-CH-005: 60/60 PASS / NO_GAIN
```

`CMP-CH-005` established the strongest-reasonable-baseline category at constructed-evidence level. The strong baseline matched DSD on all frozen gain dimensions.

## CMP-APP-001 — Unicode normalization external application

```text
PRECOMMIT: e1a109b
RESULT: b64cd88
SOURCE: Unicode Standard Annex #15
UNICODE VERSION: 17.0.0
REVISION: 57
SCORE: 42/42 PASS
```

Frozen criteria and outputs:

```text
U1 Ç vs C+cedilla / NFC canonical -> ENCODED_CORRESPONDENCE / RESOLVED
U2 same pair / binary identity -> NONCORRESPONDENCE / RESOLVED
U3 ① vs 1 / NFC canonical -> NONCORRESPONDENCE / RESOLVED
U4 same pair / NFKC compatibility -> ENCODED_CORRESPONDENCE / RESOLVED
U5 가 vs ᄀ+ᅡ / NFC canonical -> ENCODED_CORRESPONDENCE / RESOLVED
U6 reordered combining marks / NFC canonical -> ENCODED_CORRESPONDENCE / RESOLVED
```

All six runs were `CONFORMANT`. `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED` because the external application did not include a separately justified independent baseline.

Preserved criterion discipline:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

The application makes no locale-collation, grapheme-cluster, confusability, identifier-security, visual-rendering, or language-semantic claim.

## CMP-CH-006 — deterministic same-project retrace

```text
RETRACE_TARGET: CMP-APP-001
PRECOMMIT: ffd374f
PRECOMMIT_BLOB: 80b6d0d
RESULT: 35d0a8d
SCORE: 48/48 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

The retrace reproduced exactly:

```text
U1 ENCODED / canonical via NFC / RESOLVED / CONFORMANT
U2 NONCORRESPONDENCE / binary identity / RESOLVED / CONFORMANT
U3 NONCORRESPONDENCE / canonical via NFC / RESOLVED / CONFORMANT
U4 ENCODED / compatibility via NFKC / RESOLVED / CONFORMANT
U5 ENCODED / canonical via NFC / RESOLVED / CONFORMANT
U6 ENCODED / canonical via NFC / RESOLVED / CONFORMANT
```

It also reproduced criterion provenance, scope exclusions, and `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED`. The historical result was used only after reconstruction for equality scoring.

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
```

## CMP-APP-002 — RFC 9110 HTTP ETag comparison semantics

```text
PRECOMMIT: f77ddb2
PRECOMMIT_BLOB: 7478867
RESULT: fbba59a
SOURCE: RFC 9110 — HTTP Semantics
SECTIONS: 8.8.3.2, 13.1.1, 13.1.2
SCORE: 48/48 PASS
```

Frozen criterion structure and outputs:

```text
H1 W/"1" vs W/"1" / strong -> NONCORRESPONDENCE / RESOLVED
H2 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H3 W/"1" vs "1" / strong -> NONCORRESPONDENCE / RESOLVED
H4 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H5 "1" vs "1" / strong -> DIRECT_CORRESPONDENCE / RESOLVED
H6 W/"1" vs W/"2" / weak -> NONCORRESPONDENCE / RESOLVED
H7 If-Match context -> strong -> NONCORRESPONDENCE / RESOLVED
H8 If-None-Match context -> weak -> DIRECT_CORRESPONDENCE / RESOLVED
```

All eight runs were `CONFORMANT`; `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED` because no separately justified independent baseline was included.

Preserved HTTP criterion discipline:

```text
STRONG_MATCH != WEAK_MATCH_IN_GENERAL
WEAK_MATCH != REPRESENTATION_IDENTITY
OPAQUE_TAG_EQUALITY_ALONE != STRONG_MATCH_WHEN_WEAK_MARKER_PRESENT
SAME_PAIR + DIFFERENT_HTTP_CRITERION -> possibly different verdict
IF_MATCH_CONTEXT -> STRONG_COMPARISON
IF_NONE_MATCH_CONTEXT -> WEAK_COMPARISON
RFC_COMPARISON_MATCH != WHOLE_REQUEST_PRECONDITION_RESULT
```

This application does not claim request status, cache freshness outside the selected comparison rule, ETag generation correctness, resource identity, representation-byte identity, range validity, or application-level semantic equality.

## Protocol-v0.1 core guards

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
RETRACE_PASS != INDEPENDENT_REPLICATION
HTTP_MATCH != REPRESENTATION_IDENTITY
```

## Evidence IDs

```text
CMP-CH-###   constructed Comparison challenges and dedicated retrace cases
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

## Inheritance and registry discipline

```text
BOUNDARY_PASS != PERMANENT_METHOD_INDEPENDENCE
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
EXTERNAL_PASS != METHOD_GAIN_PROOF
RETRACE_PASS != INDEPENDENT_REPLICATION
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
```

## Immediate next task

Add a third materially different external Comparison domain before maturity audit. Prefer a non-textual and non-HTTP-tag criterion structure so external breadth reaches three distinct domains without merely repeating the same comparison pattern.
