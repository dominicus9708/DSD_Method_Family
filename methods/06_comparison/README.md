# 06. DSD Comparison / DSD 비교론

Status: **Protocol v0.1 established / CMP-CH-001 through CMP-CH-003 PASS / validation in progress**

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

### CMP-CH-001 — positive relation-separation challenge

```text
PRECOMMIT: 16c4b15
RESULT: c601bd2
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE, strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE under frozen strict family
ALL TERMINAL: COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

### CMP-CH-002 — negative/failure terminal-state challenge

```text
PRECOMMIT: c852a68
RESULT: ca2e91f
N1 non-exhaustive map failure
   -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N2 partial Property/status coverage
   -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N3 missing claim-required bridge
   -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
N4 forward success but required inverse evidence unverified
   -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
N5 exhaustive all-map relation failure
   -> NONCORRESPONDENCE / COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
SCORE: 48/48 PASS
PROTOCOL_REVISION_REQUIRED: no
```

### CMP-CH-003 — direct method-boundary challenge

```text
PRECOMMIT: 68d330b
RESULT: b4256d2
B1 Analysis -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
   HANDOFF: ANALYSIS_REQUIRED
B2 Classification -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
   HANDOFF: CLASSIFICATION_REQUIRED
B3 Transformation -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
   HANDOFF: TRANSFORMATION_REQUIRED
B4 Audit -> COMPARISON_PROFILE / COMPARISON_RESOLVED
   HANDOFF: AUDIT_REQUIRED
B5 Provenance/Lineage -> STRICT_EQUIVALENT snapshot structure / COMPARISON_RESOLVED
   LINEAGE_IDENTITY: not_established
   HANDOFF: PROVENANCE_LINEAGE_REQUIRED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
SCORE: 48/48 PASS
PROTOCOL_REVISION_REQUIRED: no
```

`CMP-CH-003` preserved legitimate Comparison outputs while refusing hidden internal decomposition, taxonomy assignment, unsupplied representation conversion, Audit conformance verdicts, and lineage-identity inference.

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

```text
LEGITIMATE_COMPARISON_RESULT + NEIGHBORING_HANDOFF
!= METHOD_BOUNDARY_FAILURE
```

## Three ledgers

```text
TERMINAL_COMPARISON_STATUS
COMPARISON_PROTOCOL_CONFORMANCE
COMPARISON_METHOD_GAIN_STATUS
```

Method gain is assessed only against a separately frozen competent baseline.

## Current evidence state

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

Protocol establishment itself remains infrastructure and is not counted as a direct pilot.

## Next development step

Precommit and execute `CMP-CH-004` against a competent baseline. The baseline must receive the same claim-relevant subjects, maps, coverage, bridges, Property/status records, equivalence criteria, and terminal-state information and must not be weakened to manufacture a DSD advantage. A fair `NO_GAIN` result is acceptable.

Case success/failure does not decide method survival, merger, absorption, or deletion.
