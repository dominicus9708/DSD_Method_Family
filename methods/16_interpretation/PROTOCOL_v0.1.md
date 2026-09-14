# DSD Interpretation Protocol v0.1

Status: **FROZEN EXECUTABLE INTERNAL PROTOCOL**  
Date: **2026-09-14**

Lineage:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Historical drafts and boundary records remain unchanged.

## 1. Method form

```text
supplied source set
+ source identity/version/witness and role records
+ declared interpretive question/resolution
+ declared context and perspective scope
+ explicit interpretive bridges
+ candidate-reading set or generation policy
-> source-grounded reading profile with alternatives, branch points, limits, and provenance
```

Interpretation does not convert source labels, translations, commentary, summaries, later reception, or preferred conclusions into source meaning by default.

## 2. Source-role vocabulary

```text
PRIMARY_SOURCE
TRANSLATION
COMMENTARY
LATER_RECEPTION
CONTEXT_RECORD
PROVENANCE_METADATA
RECONSTRUCTION_HANDOFF
SUMMARY_OR_AGGREGATE_HANDOFF
```

Roles do not themselves establish precedence or truth.

## 3. Reading support status

```text
SUPPORTED
PARTIALLY_SUPPORTED
NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
UNDERDETERMINED
BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
OUT_OF_SCOPE
```

## 4. Terminal interpretation status

```text
INTERPRETATION_RESOLVED_SINGLE
INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_UNDERDETERMINED
INTERPRETATION_BLOCKED
INTERPRETATION_OUT_OF_SCOPE
```

A valid run may terminate with plurality, underdetermination, blockage, or out-of-scope status without becoming protocol-nonconformant.

## 5. Reading relation

```text
compatible
mutually_exclusive
partially_overlapping
resolution_dependent
unspecified
```

## 6. Validity gates G1-G14

```text
G1  source identity/version/witness locked at claim-relevant resolution
G2  source roles explicit; precedence/authority relations separately declared when needed
G3  interpretive question, target resolution, temporal scope, and perspective/actor scope frozen
G4  translation/normalization/transformation policy explicit when claim-relevant
G5  context set and context provenance explicit; later reception not silently promoted to original context
G6  interpretive bridges explicit with provenance and applicability conditions
G7  candidate-reading set or reading-generation policy explicit
G8  source silence, missingness, damage, omission, undefined material, and source gaps preserved
G9  ambiguity, witness conflict, and alternative-reading policy explicit
G10 claim-strength rule distinguishes direct source statement, source-supported inference, context-supported inference, and bridge-dependent interpretation where material
G11 reconstruction, aggregation, dynamics, provenance, or lineage inputs used only through explicit handoffs
G12 requested authorial-intent, original-context, or historical-meaning claims have sufficient source/context obligations rather than being inferred from current reception alone
G13 neighboring-method outputs preserve their original status/provenance and are not relabelled as Interpretation verdicts
G14 requested output level and certainty do not exceed source/context/bridge closure actually available
```

Any failed claim-required gate prevents issuance of a stronger interpretation verdict than the evidence permits.

## 7. Binding operation I1-I14

```text
I1  lock task ID, interpretive question, requested output, target resolution, temporal and perspective scope
I2  lock source identities, versions/witnesses, spans, source roles, and any declared precedence
I3  separate primary source from translation, commentary, later reception, context, provenance, reconstruction, and summary handoffs
I4  execute only supplied translation/normalization mappings and record choice/loss/reversibility where material
I5  extract claim-relevant source features while preserving silence, ambiguity, missingness, damage, and undefined material
I6  lock claim-relevant context features and provenance separately from source features
I7  lock interpretive bridges, applicability conditions, and bridge provenance
I8  generate/read candidate readings only under the frozen reading-generation policy
I9  evaluate each reading against source support and context support separately
I10 preserve witness conflict, ambiguity, alternative readings, and supplied precedence without hidden harmonization
I11 identify the earliest supported interpretive branch point when requested and evidence-closed
I12 assign strongest justified reading-support status and terminal interpretation status without forced disambiguation
I13 preserve neighboring-method handoffs and claim-strength limits; do not infer provenance, reconstruction, classification, comparison, or audit verdicts silently
I14 record source-to-reading justification, alternatives, limits, conformance, gain status, and reproducibility metadata
```

## 8. Claim-strength ladder

When the task requires claim-strength tracking, use the strongest justified category only:

```text
DIRECT_SOURCE_STATEMENT
SOURCE_SUPPORTED_INFERENCE
CONTEXT_SUPPORTED_INFERENCE
BRIDGE_DEPENDENT_INTERPRETATION
UNDERDETERMINED_CLAIM
```

The ladder is not an epistemic truth ranking across all domains. It is a provenance/derivation ledger for this Interpretation run.

```text
CONTEXT_SUPPORTED_INFERENCE != DIRECT_SOURCE_STATEMENT
BRIDGE_DEPENDENT_INTERPRETATION != SOURCE_FACT
```

## 9. Translation/normalization discipline

If no claim-relevant transformation is required:

```text
TRANSLATION_OR_NORMALIZATION_POLICY: not_applicable
```

If a transformation is required, record the mapping and any material choice/loss. Unsupported reverse reconstruction is prohibited.

```text
TARGET_RENDERING_EQUALITY != SOURCE_IDENTITY
TRANSLATION_FLUENCY != SOURCE_DISAMBIGUATION_PROOF
```

## 10. Ambiguity and conflict discipline

```text
AMBIGUITY != CONTRADICTION
WITNESS_CONFLICT != METHOD_FAILURE
MULTIPLE_SUPPORTED_READINGS != UNDERDETERMINATION automatically
```

Use `INTERPRETATION_RESOLVED_MULTI` when the method can determine that multiple readings remain legitimately supported at the requested resolution.

Use `INTERPRETATION_UNDERDETERMINED` when the requested interpretive distinction cannot be resolved because support/closure is insufficient.

Use `INTERPRETATION_BLOCKED` when a claim-required source, bridge, or prerequisite is unavailable before meaningful evaluation.

## 11. Source silence and missing-source discipline

```text
SOURCE_SILENCE != NEGATIVE_CLAIM
MISSING_SOURCE != FALSE
DAMAGED_SOURCE != KNOWN_ABSENCE
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
```

No missing phrase, damaged witness, omitted condition, or absent bridge may be silently completed.

## 12. Original context and later reception

```text
LATER_RECEPTION != ORIGINAL_CONTEXT
CURRENT_READING != AUTHORIAL_INTENT
POPULAR_READING != SOURCE_ENTAILMENT
```

Later reception may itself be the interpretive target if explicitly requested; in that case it is not mislabelled as original context.

## 13. Optional DSD layers and handoffs

Formation/Property distinctions are used when claim-relevant source/context features require typed status, applicability, prerequisite, or formation distinctions.

Static Aggregation is activated only when a summary/readout is actually used and information-loss restrictions are relevant.

Dynamics is activated only when temporal sequence, state transition, or history materially affects the interpretation.

Provenance/Lineage, Reconstruction, Comparison, Classification, Analysis, and Audit remain separate methods; their outputs may be consumed through explicit handoffs.

```text
OPTIONAL_LAYER_AVAILABLE != OPTIONAL_LAYER_REQUIRED
HANDOFF_AVAILABLE != HANDOFF_VERDICT_RENAMED
```

## 14. Protocol conformance

```text
INTERPRETATION_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative `NONCONFORMANT` patterns include:

```text
translation treated as identical to primary source without mapping/provenance
commentary or later reception silently promoted to source statement
source silence converted to negation
missing source content silently reconstructed
hidden witness precedence or harmonization
unsupported authorial-intent claim
single reading forced despite frozen evidence supporting unresolved alternatives
summary/aggregate substituted for source structure after claim-relevant information loss
neighboring-method verdict renamed as Interpretation output
post-hoc source/context/bridge revision after precommit without preserving the original run
```

## 15. Method-gain ledger

```text
INTERPRETATION_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

A fair baseline must receive the same source records, source roles, version/witness identity, context, bridge, ambiguity/conflict policy, translation/normalization records, requested output, and claim-strength rules.

```text
CORRECT_AND_CONFORMANT != GAIN_ESTABLISHED
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
```

## 16. Method boundaries

```text
Analysis:
  source/target -> structural decomposition/re-expression

Comparison:
  supplied sources/readings -> correspondence/divergence

Classification:
  supplied object + schema/criteria -> class membership

Interpretation:
  source/context + bridge -> source-grounded reading

Provenance:
  artifact/record -> origin/custody/source chain

Lineage:
  record/state -> predecessor/successor identity chain

Reconstruction:
  incomplete observations -> candidate missing/latent structure

Audit:
  prior process/result -> conformance/defect retrace
```

Shared data carriers do not imply identical operations.

## 17. External-standard boundary

This internal protocol does not replace domain-specific interpretation standards.

For future external runs:

```text
DSD Interpretation conformance
!= philological correctness
!= legal interpretation correctness
!= historical consensus
!= scientific interpretation correctness
!= domain-expert agreement
```

External validation is intentionally deferred during the current internal-standardization phase.

## 18. Reproducibility record

Every executed case records:

```text
PROTOCOL_VERSION_OR_COMMIT
TASK_PRECOMMIT
SOURCE_SET_IDENTITY
SOURCE_VERSION_OR_WITNESS
CONTEXT_RECORDS
BRIDGE_RECORDS
READING_GENERATION_POLICY
EXPECTED_OR_SCORING_RECORD_IF_PRECOMMITTED
RESULT_ARTIFACT
POST_FREEZE_CHANGES
RETRACE_STATUS
```

Same-project deterministic retrace and independent replication remain separate.

## 19. Development status after freeze

```text
DEDICATED_INTERPRETATION_PROTOCOL: established v0.1
PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
BOUNDARY_AMENDMENT_001: established
DIRECT_INTERPRETATION_PILOTS: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: pre_validation
```

Protocol construction is infrastructure. The next step is a precommitted positive constructed challenge.