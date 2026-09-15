# DSD Transformation Protocol v0.1

Status: **EXECUTABLE / FROZEN**  
Date: **2026-09-16**

Protocol lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

## 1. Method form

```text
SUPPLIED SOURCE REPRESENTATION
+ EXPLICIT TRANSFORMATION MAP / BRIDGE
+ DECLARED TARGET REPRESENTATION
+ SOURCE/TARGET/MAP VERSION SCOPE
+ CLAIM-RELEVANT CARRIERS AND STATUS RECORDS
-> TARGET REPRESENTATION
+ CARRIER CORRESPONDENCE
+ PRESERVATION / MERGE / SPLIT / OMISSION / ADDITION LEDGER
+ INFORMATION-LOSS / RECONSTRUCTION RECORD
+ REVERSIBILITY RECORD
+ TERMINAL STATUS
```

Transformation does not infer faithfulness from endpoint coincidence.

## 2. Required task lock

Before execution freeze:

```text
TASK_ID
SOURCE_OBJECT_OR_RECORD_SET
SOURCE_SCHEMA_OR_REPRESENTATION_ID_AND_VERSION
TARGET_SCHEMA_OR_REPRESENTATION_ID_AND_VERSION
TRANSFORMATION_MAP_OR_RULE_ID_AND_VERSION
DECLARED_DOMAIN_AND_CODOMAIN
TARGET_RESOLUTION
CLAIM_RELEVANT_SOURCE_CARRIERS
SOURCE_CARRIER_STATUS_AND_TYPE_RECORDS
MAPPING_OR_BRIDGE_PROVENANCE
```

When applicable also freeze:

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

## 3. Carrier relation record

For each claim-relevant source carrier, record one or more explicit relations:

```text
ONE_TO_ONE
MANY_TO_ONE_MERGE
ONE_TO_MANY_SPLIT
OMITTED
NO_APPLICABLE_COUNTERPART
UNRESOLVED
```

Target-only carriers are separately recorded as:

```text
TARGET_ADDED
```

## 4. Carrier-preservation status

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

No preservation status may be inferred from equal rendered values alone.

## 5. Source-status preservation

Where claim-relevant, preserve distinctions inherited from DSD source layers, including:

```text
MISSING
ABSENT
INAPPLICABLE
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO
OUT_OF_SCOPE
```

A target encoding may collapse these only when the collapse is explicit in the loss ledger.

```text
MISSING != DEFINED_ZERO
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != OMITTED_BY_TRANSFORMATION
```

## 6. Target-addition provenance

Target values not source-derived must carry one of:

```text
DEFAULT_VALUE
EXTERNAL_ENRICHMENT
DESIGN_HANDOFF
SYNTHESIS_HANDOFF
MANUAL_SUPPLY
OTHER_EXPLICIT_ADDITION
```

```text
TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
TARGET_ADDITION != SOURCE_PRESERVATION
```

## 7. Information-loss and collision record

For claim-relevant many-to-one or omission behavior record:

```text
COLLISION_OR_MERGE_SCOPE
INJECTIVITY_STATUS
INFORMATION_LOSS_DESCRIPTION
RECONSTRUCTION_AVAILABILITY
RECONSTRUCTION_SCOPE
```

```text
SAME_TARGET_OUTPUT != SAME_SOURCE_STATE
SAME_TARGET_OUTPUT != FAITHFUL_TRANSFORMATION
```

unless a sufficient injectivity/reconstruction claim is explicitly established at the declared scope.

## 8. Reversibility status

```text
REVERSIBLE_ON_DECLARED_DOMAIN
LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
RIGHT_INVERTIBLE_ON_DECLARED_CODOMAIN
NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
INVERSE_UNAVAILABLE
REVERSIBILITY_UNDETERMINED
NOT_ASSESSED
```

```text
FORWARD_SUCCESS != REVERSE_SUCCESS
ROUND_TRIP_ON_SAMPLES != GLOBAL_INVERTIBILITY
LOSSLESS_RELATIVE_TO_DECLARED_CARRIERS != BIJECTIVE_ON_FULL_SOURCE_SPACE
```

## 9. Transformation-chain record

For composed transformations, preserve each intermediate stage:

```text
STAGE_ID_AND_VERSION
STAGE_SOURCE_SCHEMA
STAGE_TARGET_SCHEMA
STAGE_CARRIER_RELATIONS
STAGE_LOSS_OR_COLLISION
STAGE_TARGET_ADDITIONS
STAGE_REVERSIBILITY_STATUS
```

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
```

Information lost at an intermediate stage remains lost even if later stages add numerically similar or identical values from another source.

## 10. Stochastic/nondeterministic transformation

When transformation is not deterministic, freeze:

```text
RANDOM_OR_CHOICE_POLICY_ID_AND_VERSION
DISTRIBUTION_OR_SELECTION_RULE
ALLOWED_OUTPUT_SET_OR_SUPPORT
SEED_OR_REPLAY_RECORD if applicable
DETERMINISM_CLAIM
```

One realized output does not define the full transformation semantics.

## 11. Terminal transformation status

```text
TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRANSFORMATION_PARTIAL
TRANSFORMATION_BLOCKED
TRANSFORMATION_OUT_OF_SCOPE
TRANSFORMATION_UNDERDETERMINED
```

A lossy, partial, blocked, or underdetermined result may still be protocol-conformant.

## 12. Protocol conformance

```text
TRANSFORMATION_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative NONCONFORMANT behavior:

```text
hidden map substitution
unrecorded source/target/map version change
application outside declared domain without explicit extension
missing/undefined/zero collapse without loss record
unrecorded many-to-one merge
unrecorded split/duplication semantics
unrecorded target default or enrichment
reversibility claim without justified scope/inverse
sample round-trip generalized to global invertibility
intermediate loss hidden by chain endpoint equality
neighboring-method operation silently performed without typed handoff
```

## 13. Validity gates G1-G14

```text
G1  source identity/schema/version frozen
G2  target identity/schema/version frozen
G3  transformation map/rule identity/version frozen
G4  domain/codomain and applicability explicit
G5  claim-relevant carrier set explicit
G6  source statuses/types preserved at required resolution
G7  carrier relations explicit
G8  target additions/defaults/enrichment provenance explicit
G9  loss/collision/injectivity/reconstruction obligations explicit
G10 reversibility claim scope explicit
G11 chain/intermediate-stage semantics explicit when applicable
G12 stochastic/choice semantics explicit when applicable
G13 temporal/version scope explicit when applicable
G14 requested output claim does not exceed evidence, map, or reconstruction support
```

A task failing a required gate may be blocked, underdetermined, or nonconformant depending on whether the defect is in supplied task information or execution behavior.

## 14. Binding operation T1-T14

```text
T1  lock task/source/target/map identity and versions
T2  lock domain/codomain/applicability and target resolution
T3  preserve source object identity separately from target representation identity
T4  enumerate claim-relevant source carriers and statuses
T5  evaluate map applicability before target generation
T6  apply only declared transformation rules/bridges
T7  record one-to-one, merge, split, omission, or unresolved carrier relations
T8  record target-only values and provenance
T9  evaluate collisions/information loss/injectivity/reconstruction limits
T10 evaluate inverse/reversibility only at declared scope
T11 execute and record every intermediate chain stage when composed
T12 execute nondeterministic policy under its frozen semantics when applicable
T13 preserve temporal/schema-version scope and handoff provenance
T14 emit target record, ledgers, terminal status, conformance, gain/reproducibility metadata
```

## 15. Core guards

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

## 16. Neighboring-method boundaries

```text
Design         : goals/constraints -> target structure proposal
Synthesis      : supplied parts -> composed structure
Transformation : supplied source + explicit map/bridge -> target representation + preservation/loss ledger
Aggregation    : component states -> aggregate/readout
Compression    : source representation -> reduced representation under reconstruction/error objective
Comparison     : supplied subjects -> correspondence/divergence profile
Interpretation : source/context -> source-grounded reading
Computation    : formal inputs/rules -> computed result
```

Transformation may consume neighboring outputs only through explicit handoffs.

## 17. Method gain

```text
TRANSFORMATION_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

A fair baseline must receive the same frozen source records, maps/bridges, target schemas, carrier statuses, loss/reconstruction information, and required policies.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

## 18. Reproducibility

A same-project deterministic retrace may establish only artifact-level reproducibility for the frozen case.

```text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
```

## 19. External validation policy

No external Transformation application is opened during the internal-standardization lane.

Protocol v0.1 must first survive constructed positive, negative/loss/blockage, method-boundary, fair baseline, strongest-baseline, retrace, and frozen-axis internal audit stages.
