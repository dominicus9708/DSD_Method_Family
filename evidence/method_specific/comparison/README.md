# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **Protocol v0.1 established / strongest-reasonable baseline established at constructed-evidence level / first external application PASS / validation in progress**

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
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

Constructed direct-pilot counts and external-application counts are separate.

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

All six runs were `CONFORMANT`. `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED` because the external application did not include a separately justified independent baseline.

Preserved criterion discipline:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

The application makes no locale-collation, grapheme-cluster, confusability, identifier-security, visual-rendering, or language-semantic claim.

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
```

## Evidence IDs

```text
CMP-CH-###   constructed Comparison challenges
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
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
```

## Immediate next task

Precommit and run a deterministic same-project retrace of `CMP-APP-001`. Reproduce all six criterion-specific relation classes, terminal states, criterion provenance, and scope exclusions from the frozen protocol/source/precommit/result chain without reopening the task.
