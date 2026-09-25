# AGG-CH-003 — Direct Neighboring-Method Boundary Challenge Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-26**  
Challenge ID: `AGG-CH-003`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Case class: `direct_neighboring_method_boundary`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen protocol identity

```text
PROTOCOL_COMMIT:
  85b4263ad47cd10acd2230add542f381bd5d6a05

PROTOCOL_BLOB:
  5ac926aa40594126b42dac99762ff33fe87450f1
```

The frozen protocol may not be changed in response to this boundary challenge.

## 2. Purpose

Test whether Aggregation collapses into neighboring Method Family methods when each comparison has fair access to the same claim-relevant artifact bundle.

The challenge tests eight neighboring methods:

```text
Compression
Reconstruction
Measurement
Comparison
Classification
Tracking
Lineage
Audit
```

This is a fixture-bounded method-boundary test.

It is not:

```text
a permanent irreducibility proof
a method-survival vote
a superiority claim
an external-validation result
```

## 3. Shared artifact bundle

Every pair receives fair access to the same relevant constructed records:

```text
admitted channel set and channel-term ledger

defined typed-property carrier and negative-status sidecar

finite channel support F

finite property support G

declared aggregation operator

formation aggregate Comp(F)

property aggregate Agg(G)

combined static descriptor Static(F,G)

support-retaining channel/property sidecars

collision witness:
  two distinct assignments -> same aggregate

declared-class injectivity result:
  one finite class injective

separate postprocessing map

Compression sidecar:
  retained-distinction set
  compression map
  destructive-collision profile

Reconstruction sidecar:
  admissible source/support candidates
  uniqueness condition

Measurement sidecar:
  observation/readout candidates
  declared resolution
  distinguishability profile

Comparison sidecar:
  source/target correspondence and divergence profile

Classification sidecar:
  class schema and criterion-traceable assignment

Tracking sidecar:
  typed provenance/version/handoff links

Lineage sidecar:
  predecessor/successor identity records

Audit sidecar:
  frozen criteria, evidence provenance, and conformance verdict
```

No method receives hidden claim-relevant evidence unavailable to the compared partner.

Fair access does not require identical task contracts.

## 4. Five-interface non-collapse test

For every pair compare:

```text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
```

Allowed pair result:

```text
EXACT_COLLAPSE
PARTIAL_OVERLAP_NOT_COLLAPSE
UNRESOLVED_BOUNDARY
```

`EXACT_COLLAPSE` requires no claim-relevant distinction across all five interfaces in this frozen fixture.

Shared maps, sidecars, data, or workflow handoffs are insufficient for collapse.

## 5. B1 — Aggregation vs Compression

Shared overlap:

```text
source values
readout maps
collision information
support/information-loss sidecars
downstream purpose
```

Frozen distinction:

```text
Aggregation operation:
  combine selected admitted values into a declared readout

Compression operation:
  intentionally reduce representation while preserving
  distinctions required by a declared downstream purpose
```

Outputs:

```text
Aggregation:
  aggregate value + aggregation ledger + optional support/collision sidecar

Compression:
  compressed representation + retained-distinction set
  + acceptable/destructive collision profile
  + reconstruction limits
```

Failure distinction:

```text
Aggregation can succeed even when information is lost,
provided no stronger reconstruction claim was frozen.

Compression fails relative to its task when the reduction destroys
a distinction declared necessary for the downstream purpose.
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

Guard:

```text
REDUCED_READOUT != PURPOSE_VALIDATED_COMPRESSION
```

## 6. B2 — Aggregation vs Reconstruction

Shared overlap:

```text
aggregate outputs
support sidecars
collision witnesses
injectivity conditions
```

Frozen distinction:

```text
Aggregation:
  forward construction of declared readout

Reconstruction:
  inverse inference of compatible prior/hidden/support structures
  from incomplete or reduced evidence
```

Outputs:

```text
Aggregation:
  aggregate/readout and information-loss ledger

Reconstruction:
  admissible reconstruction set
  uniqueness/nonuniqueness condition
  unrecoverable-information record
```

Required guard:

```text
AGGREGATE_OUTPUT != RECONSTRUCTED_SOURCE
COLLISION_TEST != RECONSTRUCTION
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 7. B3 — Aggregation vs Measurement

Shared overlap:

```text
readout candidates
resolution declarations
collision/information-loss data
defined-zero/undefined status
```

Frozen distinction:

```text
Aggregation:
  construct a readout from already-admitted data

Measurement:
  determine which supplied/proposed observations or readouts
  discriminate declared structural alternatives at a declared resolution
```

Outputs:

```text
Aggregation:
  aggregate/readout value

Measurement:
  distinguishability/candidate-status ledger
  plan sufficiency terminal
```

Required guard:

```text
READOUT_CONSTRUCTION != DISCRIMINATING_MEASUREMENT_PLAN
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 8. B4 — Aggregation vs Comparison

Shared overlap:

```text
same subjects
aggregate readouts
maps/correspondences
support and collision sidecars
```

Frozen distinction:

```text
Aggregation:
  compute declared readout on selected support

Comparison:
  judge correspondence/divergence/equivalence under frozen
  comparison scope and criteria
```

Outputs:

```text
Aggregation:
  aggregate value and support/injectivity ledger

Comparison:
  correspondence/divergence profile
  equivalence/branch result
```

Required guard:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 9. B5 — Aggregation vs Classification

Shared overlap:

```text
aggregate descriptors
typed status
source provenance
declared features
```

Frozen distinction:

```text
Aggregation:
  compute a declared summary/readout

Classification:
  assign class membership under explicit class criteria
```

Outputs:

```text
Aggregation:
  readout/aggregate

Classification:
  criterion-traceable class assignment or unresolved membership status
```

Required guard:

```text
SUMMARY_COINCIDENCE != STRUCTURAL_CLASS_IDENTITY
AGGREGATE_VALUE != CLASS_ASSIGNMENT
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 10. B6 — Aggregation vs Tracking

Shared overlap:

```text
support provenance
versioned readout records
transformation/aggregation handoffs
source identities
```

Frozen distinction:

```text
Aggregation:
  compute readout

Tracking:
  record where data/artifacts came from, went, and which
  evidence supports each trace link
```

Outputs:

```text
Aggregation:
  aggregate ledger

Tracking:
  trace graph/path/link-status ledger
```

Required guard:

```text
AGGREGATION_PROVENANCE_SIDECAR != TRACKING_TRACE
TRACE_OF_AGGREGATION != AGGREGATION_RESULT
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 11. B7 — Aggregation vs Lineage

Shared overlap:

```text
support identities
state/readout records
transition context
possibly equal or unequal aggregate values
```

Frozen distinction:

```text
Aggregation:
  construct reduced/static readout

Lineage:
  determine predecessor/successor identity across change
```

Outputs:

```text
Aggregation:
  aggregate/support/injectivity ledger

Lineage:
  successor-status/family-coherence/state-succession/
  interval-identity ledger
```

Required guard:

```text
AGGREGATE_EQUALITY != LINEAGE_IDENTITY
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 12. B8 — Aggregation vs Audit

Shared overlap:

```text
task/version locks
source provenance
aggregation ledger
collision/injectivity claims
maximum-supported claim
```

Frozen distinction:

```text
Aggregation:
  execute declared aggregation operation

Audit:
  retrace and evaluate performed work/evidence/procedure
  against frozen scope, rules, and verdict criteria
```

Outputs:

```text
Aggregation:
  readout plus aggregation-specific ledgers

Audit:
  conformance/evidence/procedure verdict
```

Required guard:

```text
AGGREGATION_RESULT != AUDIT_VERDICT
AGGREGATION_PROTOCOL_CONFORMANCE != GENERAL_AUDIT_PASS
```

Expected:

```text
PARTIAL_OVERLAP_NOT_COLLAPSE
```

## 13. Frozen scoring — 72 checks

Each pair receives nine checks:

```text
1 shared artifact access is fair
2 INPUTS overlap/difference recorded
3 OPERATION distinction recorded
4 OUTPUT distinction recorded
5 FAILURE/NO_GAIN distinction recorded
6 VALIDATION distinction recorded
7 required guard preserved
8 no hidden claim promotion
9 pair classification follows five-interface test
```

Eight pairs:

```text
8 x 9 = 72 checks
```

```text
TOTAL_REQUIRED_CHECKS:
  72

PASS_THRESHOLD:
  72/72

PARTIAL_PASS_ALLOWED:
  no
```

## 14. Frozen expected summary

```text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  8

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  8

BOUNDARY_STATUS:
  FIXTURE_BOUNDED_SEPARATION_ESTABLISHED
```

This expected result is precommitted from the frozen method definitions.

Execution must preserve any discovered contradiction rather than repairing the fixture.

## 15. Counter rule on full PASS

If all 72 checks pass:

```text
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  2 -> 3

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  2 -> 3

METHOD_BOUNDARY_AGGREGATION_CASES:
  0 -> 1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  0 -> 8

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  8

SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
```

Do not change baseline, NO_GAIN, reproducibility, external, or independent-validation counters.

## 16. Interpretation lock

```text
FIXTURE_BOUNDED_SEPARATION
  !=
PERMANENT_METHOD_IRREDUCIBILITY

PARTIAL_OVERLAP_NOT_COLLAPSE
  !=
METHOD_SUPERIORITY

NO_EXACT_COLLAPSE_IN_THIS_FIXTURE
  !=
PROOF_OF_PERMANENT_REGISTRY_SURVIVAL
```
