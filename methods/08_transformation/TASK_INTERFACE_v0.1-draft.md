# DSD Transformation Task Interface v0.1 — historical draft

Status: **historical draft / preserved**  
Date: **2026-09-16**

## 1. Task identity

DSD Transformation receives a supplied source representation and a declared target representation together with an explicit transformation map or bridge policy. It returns transformed target records plus a trace of what was preserved, transformed under declared equivalence, merged, omitted, added, unresolved, or rendered non-reconstructible.

Transformation is not defined by target-output coincidence alone.

## 2. Inputs

Required inputs:

```text
SOURCE_OBJECT_OR_RECORD_SET
SOURCE_SCHEMA_OR_REPRESENTATION_ID_AND_VERSION
TARGET_SCHEMA_OR_REPRESENTATION_ID_AND_VERSION
TRANSFORMATION_MAP_OR_RULE_ID_AND_VERSION
DECLARED_DOMAIN_AND_CODOMAIN
TARGET_RESOLUTION
CLAIM_RELEVANT_SOURCE_CARRIERS
CARRIER_STATUS_AND_TYPE_RECORDS
MAPPING_OR_BRIDGE_PROVENANCE
```

Conditionally required inputs:

```text
EQUIVALENCE_RELATION_OR_TOLERANCE
LOSS_OR_MERGE_POLICY
TARGET_ADDITION_OR_DEFAULT_POLICY
RECONSTRUCTION_OR_INVERSE_CLAIM
TRANSFORMATION_CHAIN_OR_INTERMEDIATE_STAGES
TEMPORAL_OR_SCHEMA_VERSION_SCOPE
STOCHASTIC_OR_NONDETERMINISTIC_POLICY
NEIGHBORING_METHOD_HANDOFFS
```

## 3. Binding operation

Transformation must:

```text
1 lock source/target/map identities and versions;
2 lock the declared source domain and target codomain;
3 preserve source object identity separately from target representation identity;
4 evaluate map applicability before target-value generation;
5 transform only through declared rules or bridges;
6 preserve missing/undefined/zero/inapplicable/out-of-scope distinctions where claim-relevant;
7 record carrier correspondence and any merge/split/omission/addition;
8 record information loss and reconstruction limits;
9 evaluate reversibility only at the declared scope;
10 preserve intermediate-stage loss in composed transformation chains;
11 preserve provenance for target-added/default/enriched values;
12 preserve temporal/version scope where the map is version-sensitive;
13 keep neighboring-method handoffs typed rather than silently performing their operations;
14 emit a terminal transformation status and conformance record.
```

## 4. Carrier-preservation status family

```text
PRESERVED_EXACT
PRESERVED_UNDER_DECLARED_EQUIVALENCE
MERGED_IN_TARGET
SPLIT_IN_TARGET
OMITTED_BY_TRANSFORMATION
TARGET_ADDED_NOT_SOURCE_DERIVED
UNRESOLVED_PRESERVATION
INAPPLICABLE_AT_TARGET
OUT_OF_SCOPE_FOR_TRANSFORMATION
```

A target carrier may have more than one provenance role only when the roles are explicitly nonexclusive and recorded.

## 5. Transformation terminal status family

```text
TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRANSFORMATION_PARTIAL
TRANSFORMATION_BLOCKED
TRANSFORMATION_OUT_OF_SCOPE
TRANSFORMATION_UNDERDETERMINED
```

Terminal status is distinct from protocol conformance. A declared-loss or blocked result may still be conformant.

## 6. Reversibility status family

```text
REVERSIBLE_ON_DECLARED_DOMAIN
LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
RIGHT_INVERTIBLE_ON_DECLARED_CODOMAIN
NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
INVERSE_UNAVAILABLE
REVERSIBILITY_UNDETERMINED
NOT_ASSESSED
```

## 7. Outputs

```text
TARGET_OBJECT_OR_RECORD_SET
SOURCE_TO_TARGET_CARRIER_MAP
CARRIER_PRESERVATION_LEDGER
TRANSFORMATION_PROVENANCE_LEDGER
INFORMATION_LOSS_LEDGER
TARGET_ADDITION_LEDGER
INJECTIVITY_OR_COLLISION_RECORD
RECONSTRUCTION_OR_INVERSE_RECORD
TRANSFORMATION_CHAIN_RECORD
TERMINAL_TRANSFORMATION_STATUS
TRANSFORMATION_PROTOCOL_CONFORMANCE
TRANSFORMATION_METHOD_GAIN_STATUS
```

## 8. Core guards

```text
SAME_TARGET_OUTPUT != FAITHFUL_TRANSFORMATION
FORWARD_SUCCESS != REVERSE_SUCCESS
ROUND_TRIP_ON_SAMPLES != GLOBAL_INVERTIBILITY
LOSSLESS_RELATIVE_TO_DECLARED_CARRIERS != BIJECTIVE_ON_FULL_SOURCE_SPACE
EMBEDDING != STRICT_EQUIVALENCE
NORMALIZATION != IDENTITY
TARGET_DEFAULT != SOURCE_DERIVED_VALUE
MISSING != DEFINED_ZERO
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != OMITTED_BY_TRANSFORMATION
MERGED_CARRIERS != PRESERVED_CARRIERS
TARGET_ADDITION != SOURCE_PRESERVATION
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
PARTIAL_MAP != TOTAL_MAP
TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
```

## 9. Failure / no-gain criteria

Protocol nonconformance includes:

```text
hidden map substitution
unrecorded source or target schema version change
mapping outside declared domain without explicit extension
missing/undefined/zero collapse when claim-relevant
unrecorded many-to-one merge
unrecorded target-added value or default
reversibility claim without inverse/reconstruction support
sample round-trip generalized to full-domain invertibility
loss hidden by endpoint equality
neighboring-method output relabeled as transformation evidence without handoff provenance
```

`NO_GAIN` is allowed when a fair non-DSD transformation baseline receiving the same information produces the same claim-relevant output and preservation/loss trace.

```text
NO_GAIN != METHOD_FAILURE
CASE_FAIL != METHOD_DELETION_PROOF
```

## 10. Validation standard

A Transformation run is validated against the frozen task by checking:

```text
map applicability
source/target type and status preservation
carrier correspondence
merge/split/omission/addition provenance
information-loss claims
inverse/reconstruction claims
chain-stage trace
terminal status
conformance
scope-bounded claim strength
```

External-domain correctness is not part of this draft's internal-standardization stage.
