# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **Protocol v0.1 established / positive and negative-failure direct challenges PASS / validation in progress**

This lane records evidence that directly tests **DSD Comparison / DSD 비교론**.

## Current development state

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
BOUNDARY_PRESERVED_NO_REFINEMENT: 11
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
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

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count.

## Protocol and planning artifacts

```text
methods/06_comparison/PROTOCOL_v0.1.md
  creation commit a1700d960e0b41dfe32bf85b6334448d9104100d
methods/06_comparison/TASK_INTERFACE_v0.1-draft.md
methods/06_comparison/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
methods/06_comparison/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
methods/06_comparison/PLANNING.md
methods/06_comparison/WORKLOG.md
```

## Direct Protocol-v0.1 evidence

### CMP-CH-001 — positive relation-separation challenge

```text
PRECOMMIT: 16c4b15
RESULT: c601bd2
SCORE: 40/40 PASS
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE / strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE under frozen strict family
ALL TERMINAL: COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

### CMP-CH-002 — negative/failure terminal distinction

```text
PRECOMMIT: c852a68
RESULT: ca2e91f
SCORE: 48/48 PASS

N1 non-exhaustive map failure
  -> UNDETERMINED_CORRESPONDENCE
  -> COMPARISON_UNDERDETERMINED

N2 partial Property/status coverage
  -> UNDETERMINED_CORRESPONDENCE
  -> COMPARISON_UNDERDETERMINED

N3 missing required semantic bridge
  -> UNDETERMINED_CORRESPONDENCE
  -> COMPARISON_BLOCKED

N4 forward map success, inverse-preservation evidence unverified in frozen run
  -> UNDETERMINED_CORRESPONDENCE
  -> COMPARISON_UNDERDETERMINED

N5 exhaustive all-map relation-preservation failure
  -> NONCORRESPONDENCE
  -> COMPARISON_RESOLVED

ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
PROTOCOL_REVISION_REQUIRED: no
```

The case preserves failure-to-close separately from proved noncorrespondence and keeps missing required bridge distinct from observed difference.

Evidence increment:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NEGATIVE_OR_FAILURE_COMPARISON_CASE_INCREMENT: +1
```

## Protocol-v0.1 core guards

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
NONEXHAUSTIVE_MAP_FAILURE != RESOLVED_NONCORRESPONDENCE
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
```

## Output / terminal / ledger structure

```text
OUTPUT_LEVELS:
  COMPARISON_PROFILE
  CORRESPONDENCE_CLASSIFICATION
  STRICT_EQUIVALENCE_DECISION
  FIRST_BRANCH_POINT
  PARTIAL_COMPARISON

TERMINAL:
  COMPARISON_RESOLVED
  COMPARISON_UNDERDETERMINED
  COMPARISON_BLOCKED

THREE LEDGERS:
  TERMINAL_COMPARISON_STATUS
  COMPARISON_PROTOCOL_CONFORMANCE
  COMPARISON_METHOD_GAIN_STATUS
```

## Evidence IDs

```text
CMP-CH-###   constructed Comparison challenges
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

Pre-protocol boundary planning uses `CMP-BND-DRAFT-###` and is not direct evidence.

## Inheritance and method-survival rule

Neighboring-method evidence may inform challenge design but does not automatically validate Comparison.

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
```

## Immediate next task

Precommit and execute `CMP-CH-003` direct method-boundary challenge. Require explicit handoffs for hidden Analysis, Classification, Transformation, Audit, and Provenance/Lineage operations while preserving legitimate Comparison outputs where the supplied comparison records are already sufficient.
