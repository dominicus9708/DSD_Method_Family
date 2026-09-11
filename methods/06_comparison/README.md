# 06. DSD Comparison / DSD 비교론

Status: **Protocol v0.1 established / CMP-CH-001 through CMP-CH-005 complete / strongest-reasonable baseline established at constructed-evidence level / first external application PASS / validation in progress**

Task: compare two or more supplied structures without reducing comparison to final-output equality, and determine justified correspondence, preserved structure, divergence, strict-equivalence status, and earliest supported branching only within declared comparison/map/element coverage.

Primary DSD sources: strict equivalence, structure-preserving maps, stage comparison, first branching, Property-stage comparison, Channel-Indexed Static Aggregation as a separate readout source, and optional dynamic comparison with lineage claims gated separately.

## Core method form

```text
supplied subjects
+ declared comparison scope/resolution
+ supplied map/correspondence family
+ preservation/equivalence criteria
-> correspondence/divergence profile
```

## Executable protocol and lineage

Current executable protocol: `PROTOCOL_v0.1.md`, creation commit `a1700d960e0b41dfe32bf85b6334448d9104100d`.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Historical planning artifacts remain preserved and are not rewritten after protocol freeze.

## Core guards

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
COMMON_LABEL != COMMON_COORDINATE_OR_SEMANTIC_ROLE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
SIMILAR_OUTPUT != SHARED_LINEAGE_OR_IDENTITY
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
NONEXHAUSTIVE_MAP_FAILURE != RESOLVED_NONCORRESPONDENCE
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
NO_GAIN != METHOD_ABSORPTION_PROOF
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
```

## Output / relation / terminal structure

```text
OUTPUT_LEVELS:
  COMPARISON_PROFILE
  CORRESPONDENCE_CLASSIFICATION
  STRICT_EQUIVALENCE_DECISION
  FIRST_BRANCH_POINT
  PARTIAL_COMPARISON

RELATION_CLASSES:
  STRICT_EQUIVALENT
  DIRECT_CORRESPONDENCE
  PARTIAL_CORRESPONDENCE
  ENCODED_CORRESPONDENCE
  NONCORRESPONDENCE
  UNDETERMINED_CORRESPONDENCE

TERMINAL_COMPARISON_STATUS:
  COMPARISON_RESOLVED
  COMPARISON_UNDERDETERMINED
  COMPARISON_BLOCKED
```

A resolved comparison may resolve to equivalence, correspondence, or justified noncorrespondence. `UNDERDETERMINED` preserves incomplete closure; `BLOCKED` preserves missing claim-required records, representations, or bridges.

## Protocol-v0.1 forced locks

```text
MAP_PROPERTY_REQUIREMENT_PROFILE
REVERSE_DIRECTION_OR_INVERSE_POLICY
COMPARISON_ELEMENT_COVERAGE
CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL
PRECOMPARISON_TRANSFORMATION_POLICY
REPRESENTATION_PROVENANCE
LINEAGE_IDENTITY_CLAIM_POLICY
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

## Direct Protocol-v0.1 evidence

```text
CMP-CH-001  40/40 PASS  positive relation separation
CMP-CH-002  48/48 PASS  negative/failure terminal distinction
CMP-CH-003  48/48 PASS  direct method-boundary
CMP-CH-004  50/50 PASS / NO_GAIN  competent baseline
CMP-CH-005  60/60 PASS / NO_GAIN  strongest-reasonable baseline
```

`CMP-CH-005` established `STRONGEST_REASONABLE_BASELINE_COMPARISON = established_at_constructed_evidence_level`; the strong baseline matched DSD on first-branch closure, direction/inverse discipline, element coverage, bridge provenance, dynamic-vs-lineage separation, and retraceability.

## External application evidence

### CMP-APP-001 — Unicode normalization comparison

```text
SOURCE: Unicode Standard Annex #15
VERSION: Unicode 17.0.0
REVISION: 57
PRECOMMIT: e1a109b
RESULT: b64cd88
SCORE: 42/42 PASS

U1 Ç vs C+cedilla / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED
U2 same pair / binary identity
  -> NONCORRESPONDENCE / RESOLVED
U3 ① vs 1 / NFC canonical
  -> NONCORRESPONDENCE / RESOLVED
U4 same pair / NFKC compatibility
  -> ENCODED_CORRESPONDENCE / RESOLVED
U5 가 vs ᄀ+ᅡ / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED
U6 combining-mark reorder / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED

ALL CONFORMANCE: CONFORMANT
METHOD GAIN: NOT_ASSESSED
```

The external case preserves criterion provenance: binary identity, canonical equivalence, and compatibility equivalence are not collapsed. A relation class is not treated as intrinsic to a pair independently of the frozen comparison criterion.

## Method boundaries

```text
Analysis: internal decomposition/description
Comparison: cross-subject preservation/correspondence/divergence
Classification: taxonomy-based class assignment
Transformation: source -> target representation/regime
Audit: retrace/evaluate an existing process or verdict
Provenance/Lineage: historical/source/successor identity chain
Aggregation: admitted structure/data -> declared readout
```

Comparison may consume neighboring-method outputs but does not absorb their operations or verdicts.

## Three ledgers

```text
TERMINAL_COMPARISON_STATUS
COMPARISON_PROTOCOL_CONFORMANCE
COMPARISON_METHOD_GAIN_STATUS
```

## Current evidence state

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

External application count is separate from constructed direct-pilot count.

## Next development step

Run a deterministic same-project retrace of `CMP-APP-001` from the frozen protocol, precommit, external-source lock, and result. Reproduce all six criterion-specific correspondence classes, terminal states, and exclusions without reopening or rewriting the task.

Case success/failure and comparative gain do not decide method survival, merger, absorption, or deletion.
