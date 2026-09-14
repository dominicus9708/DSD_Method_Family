# INT-CH-006 Precommit / DSD Interpretation Strongest-Reasonable-Baseline Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-15**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol commit at freeze: `40110a8a779f0ac6ff93ede6414544b8ec548fdf`  
Protocol blob at freeze: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`

## 1. Case identity

```text
CASE_ID: INT-CH-006
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: B1_STRONG_SOURCE_CONTEXT_INTERPRETATION_ENGINE
```

Purpose: pressure DSD Interpretation against a materially richer non-DSD baseline while giving both systems exactly the same claim-relevant source, witness/version, transformation, context, reconstruction-handoff, temporal-scope, bridge, candidate-reading, claim-strength, ambiguity, and provenance records.

A fair `NO_GAIN` is explicitly admissible. `NO_GAIN` is not method failure and does not establish merger, absorption, deletion, or permanent redundancy.

This challenge is entirely constructed and internal. No external corpus, legal record, historical document, scientific corpus, or Sunzi material is used.

## 2. Strong baseline capability freeze

Baseline identity:

```text
B1_STRONG_SOURCE_CONTEXT_INTERPRETATION_ENGINE
```

B1 receives exactly the same claim-relevant records as DSD and is explicitly competent to:

```text
1 preserve witness identity, version identity, and declared/nondeclared precedence;
2 preserve incompatible witness-supported readings without hidden harmonization;
3 apply only supplied translation/normalization mappings and retain mapping provenance;
4 preserve multiple licensed transformations when no precedence rule selects one;
5 consume reconstruction outputs only as typed handoffs and never relabel reconstructed content as observed source content;
6 preserve source/context temporal scope and prevent later-context back-projection;
7 separate direct source statement, source-supported inference, context-supported inference, and bridge-dependent interpretation;
8 preserve normative/conditional wording without upgrading it into factual occurrence, causal sufficiency, or prediction;
9 preserve source silence, ambiguity, blockage, and plurality where required;
10 retain enough source-to-reading, witness, transformation, reconstruction, temporal, bridge, and claim-strength records for deterministic retrace.
```

B1 need not use DSD terminology internally. For scoring its outputs are mapped one-to-one to the frozen Interpretation statuses.

B1 may not be weakened after this precommit.

## 3. Frozen task family

Five stronger constructed subcases are frozen:

```text
R1 witness/version conflict with no declared precedence
R2 competing supplied normalization mappings with provenance
R3 reconstruction-handoff provenance without observed-source promotion
R4 time-indexed context change under identical wording
R5 claim-strength interaction between obligation, occurrence, prediction, and causation
```

## 4. R1 — witness/version conflict without hidden harmonization

Witnesses:

```text
W1-A / version A: "The gate opens only when seal S is present."
W1-B / version B: "The gate may open when seal S is present."
```

Frozen records:

```text
SOURCE_ROLE(W1-A): PRIMARY_SOURCE
SOURCE_ROLE(W1-B): PRIMARY_SOURCE
WITNESS_PRECEDENCE: none supplied
HARMONIZATION_POLICY: prohibited unless explicit rule supplied
TARGET_SCOPE: cross-witness reading at supplied resolution
```

Candidate readings:

```text
R1A: S is necessary for opening
R1B: S is merely compatible with possible opening; necessity is not established
```

Frozen expected output for DSD and B1:

```text
W1-A supports R1A
W1-B supports R1B at its witness-local scope
CROSS_WITNESS_SINGLE_READING: not forced
HIDDEN_WITNESS_PRECEDENCE: prohibited
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
```

The task is resolved to a legitimate plurality because the method can determine the witness-conditioned alternatives even though it cannot collapse them into one global meaning.

Preserved distinctions:

```text
WITNESS_CONFLICT != METHOD_FAILURE
MULTIPLE_WITNESS_SUPPORTED_READINGS != INTERPRETATION_UNDERDETERMINED automatically
NO_PRECEDENCE_RULE != LICENSE_TO_HARMONIZE
```

## 5. R2 — competing supplied normalization mappings

Raw source token:

```text
S2-RAW: "mode=Q"
```

Supplied transformation records:

```text
T2-A: Q -> QUIESCENT
T2-B: Q -> QUEUED
TRANSFORMATION_ROLE: claim-relevant normalization/decoding alternatives
TRANSFORMATION_PRECEDENCE: none supplied
REVERSIBILITY_CLAIM: not required
```

Candidate readings:

```text
R2A: mode is QUIESCENT under T2-A
R2B: mode is QUEUED under T2-B
R2C: raw source itself directly states QUIESCENT
```

Frozen expected output for DSD and B1:

```text
R2A -> SUPPORTED under T2-A / BRIDGE_DEPENDENT_INTERPRETATION
R2B -> SUPPORTED under T2-B / BRIDGE_DEPENDENT_INTERPRETATION
R2C -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
TRANSFORMATION_PROVENANCE: preserved separately
HIDDEN_TRANSFORMATION_SELECTION: prohibited
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
```

Preserved distinctions:

```text
NORMALIZED_RENDERING != RAW_SOURCE_IDENTITY
MULTIPLE_LICENSED_MAPPINGS != LICENSE_TO_CHOOSE_ONE_SILENTLY
TARGET_RENDERING_EQUALITY != SOURCE_IDENTITY
```

## 6. R3 — reconstruction handoff provenance

Observed source:

```text
S3-OBSERVED: "The signal became [MISSING] before closure."
```

Explicit Reconstruction handoff:

```text
RH3:
  candidate A = stable
  candidate B = silent
  candidate status = equally admissible under reconstruction constraints
  provenance role = RECONSTRUCTION_HANDOFF
```

Candidate readings:

```text
R3A: "stable" is an admissible reconstructed completion
R3B: "silent" is an admissible reconstructed completion
R3C: observed source directly states "stable"
R3D: observed source directly states "silent"
```

Frozen expected output for DSD and B1:

```text
R3A -> SUPPORTED as reconstruction-handoff-dependent candidate
R3B -> SUPPORTED as reconstruction-handoff-dependent candidate
R3C -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R3D -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
OBSERVED_VS_RECONSTRUCTED_PROVENANCE: preserved
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
```

Preserved distinctions:

```text
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
ADMISSIBLE_RECONSTRUCTION != UNIQUE_RECOVERY
HANDOFF_SUPPORT != SOURCE_TEXT_PROMOTION
```

## 7. R4 — time-indexed context change under identical wording

Primary source records:

```text
S4-t0: "The blue flag is raised."
S4-t1: "The blue flag is raised."
```

Frozen contexts:

```text
C4-t0: within procedure version P0, blue flag means HAZARD
C4-t1: within later procedure version P1, blue flag means ALL_CLEAR
TEMPORAL_ORDER: t0 < t1
CONTEXT_BACK_PROJECTION: prohibited
```

Candidate readings:

```text
R4A: at t0 the blue flag means HAZARD
R4B: at t1 the blue flag means ALL_CLEAR
R4C: identical wording proves identical meaning across t0 and t1
```

Frozen expected output for DSD and B1:

```text
R4A -> SUPPORTED / CONTEXT_SUPPORTED_INFERENCE
R4B -> SUPPORTED / CONTEXT_SUPPORTED_INFERENCE
R4C -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
TEMPORAL_CONTEXT_SCOPE: preserved
LATER_CONTEXT_BACK_PROJECTED_TO_t0: no
EARLIER_CONTEXT_FORWARDED_TO_t1: no
TERMINAL -> INTERPRETATION_RESOLVED_MULTI at cross-time scope
```

Preserved distinctions:

```text
SAME_WORDING != SAME_MEANING_ACROSS_CONTEXT
TEMPORAL_ORDER != SEMANTIC_IDENTITY
LATER_CONTEXT != ORIGINAL_CONTEXT
```

## 8. R5 — claim-strength interaction

Primary source:

```text
S5: "The operator shall close valve V when pressure exceeds P."
```

Frozen bridge/context:

```text
B5: in this fixture, "shall" expresses an obligation rule, not a factual occurrence report
C5: no execution log is supplied
C5: no causal-mechanism proof is supplied
C5: no prediction model is supplied
```

Candidate readings:

```text
R5A: the source states an obligation to close V when pressure exceeds P
R5B: V in fact closed in every such event
R5C: pressure exceeding P is by itself causally sufficient to close V
R5D: V will certainly close in the next such event
```

Frozen expected output for DSD and B1:

```text
R5A -> SUPPORTED / DIRECT_SOURCE_STATEMENT
R5B -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R5C -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R5D -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
NORMATIVE_TO_FACTUAL_UPGRADE: prohibited
OBLIGATION_TO_PREDICTION_UPGRADE: prohibited
OBLIGATION_TO_CAUSAL_SUFFICIENCY_UPGRADE: prohibited
TERMINAL -> INTERPRETATION_RESOLVED_SINGLE
```

Preserved distinctions:

```text
OBLIGATION != OCCURRENCE
OBLIGATION != PREDICTION
CONDITIONAL_RULE != CAUSAL_SUFFICIENCY_PROOF
DIRECT_SOURCE_STATEMENT != EMPIRICAL_CONFIRMATION
```

## 9. Frozen gain criteria

```text
G1 WITNESS_VERSION_CONFLICT_GAIN
  established only if DSD preserves witness/version conflict or nonprecedence more correctly than B1.

G2 TRANSFORMATION_PROVENANCE_GAIN
  established only if DSD preserves competing normalization/translation choices and provenance more correctly than B1.

G3 RECONSTRUCTION_HANDOFF_GAIN
  established only if DSD preserves observed/reconstructed distinction or reconstruction nonuniqueness more correctly than B1.

G4 TEMPORAL_CONTEXT_SCOPE_GAIN
  established only if DSD preserves time-indexed context and prevents back-projection more correctly than B1.

G5 CLAIM_STRENGTH_INTERACTION_GAIN
  established only if DSD preserves obligation/occurrence/prediction/causation or claim-strength boundaries more correctly than B1.

G6 AMBIGUITY_AND_NO_HIDDEN_HARMONIZATION_GAIN
  established only if DSD retains justified plurality or conflict without hidden selection more correctly than B1.

G7 TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant derivation/provenance trace that B1 cannot reconstruct from the same inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> challenge FAIL.
If one or more G1-G7 are established against a correct B1 -> GAIN_ESTABLISHED.
If DSD and B1 are both correct and B1 matches all seven dimensions -> NO_GAIN.
Otherwise -> challenge FAIL or unresolved according to the frozen scoring record.
```

No implementation speed, elegance, terminology, pedagogical value, external practical advantage, or independent-evaluator result is scored.

## 10. Frozen expected task-level outputs

```text
R1 DSD/B1 -> witness-conditioned plurality / INTERPRETATION_RESOLVED_MULTI
R2 DSD/B1 -> two mapping-conditioned readings / INTERPRETATION_RESOLVED_MULTI
R3 DSD/B1 -> two reconstruction-conditioned candidates; no observed-source promotion / INTERPRETATION_RESOLVED_MULTI
R4 DSD/B1 -> t0 hazard + t1 all-clear; no semantic identity from wording / INTERPRETATION_RESOLVED_MULTI
R5 DSD/B1 -> obligation supported; factual/causal/predictive upgrades unsupported / INTERPRETATION_RESOLVED_SINGLE
```

All five DSD executions are expected to be `INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed correctly.

## 11. Frozen scoring

```text
A. immutable/fairness discipline        8
B. DSD execution                       18
C. B1 execution                        18
D. comparative gain                     9
E. scope/protocol pressure              7
TOTAL                                  60
```

Detailed check lock:

```text
A1 protocol commit/blob fixed
A2 five stronger subcases fixed
A3 B1 identity/capabilities fixed
A4 same claim-relevant inputs frozen
A5 gain criteria G1-G7 fixed
A6 scoring fixed
A7 B1 may not be weakened post-hoc
A8 no witness/transformation/reconstruction/context/bridge/policy revision after execution begins

B1-B5 exact terminal outputs R1-R5
B6 R1 witness-specific support preserved
B7 R1 no hidden precedence/harmonization
B8 R2 both supplied mappings preserved
B9 R2 raw source not equated with normalized renderings
B10 R3 reconstructed candidates not promoted to observed text
B11 R3 nonunique reconstruction retained
B12 R4 time-indexed context preserved
B13 R4 same wording not upgraded to semantic identity
B14 R5 obligation preserved as obligation
B15 R5 occurrence/prediction/causal upgrades rejected
B16 claim-strength ledger preserved across R2/R4/R5
B17 all neighboring handoff provenance retained
B18 all five DSD executions CONFORMANT

C1-C5 exact terminal outputs R1-R5
C6 R1 witness-specific support preserved
C7 R1 no hidden precedence/harmonization
C8 R2 both supplied mappings preserved
C9 R2 raw/normalized distinction preserved
C10 R3 observed/reconstructed distinction preserved
C11 R3 nonunique reconstruction retained
C12 R4 temporal contexts preserved without back-projection
C13 R4 same wording not treated as semantic identity
C14 R5 obligation/occurrence/prediction/causation separated
C15 claim-strength mappings retained
C16 ambiguity/plurality retained without hidden selection
C17 source-to-reading provenance sufficient for every subcase
C18 full result set deterministically retraceable from frozen B1 record

D1-D7 G1-G7 each NOT_ESTABLISHED if B1 matches
D8 final method gain = NO_GAIN when D1-D7 all hold
D9 NO_GAIN not interpreted as method failure/merger/absorption/deletion evidence

E1 protocol revision not required if no contradiction appears
E2 strongest-reasonable-baseline status may be established only at constructed-evidence level
E3 no external applicability claim
E4 no reproducibility claim
E5 no independent validation or practical-superiority claim
E6 no maturity-promotion claim
E7 no permanent survival/nonmerger/redundancy conclusion
```

Decision:

```text
60/60 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a challenge-design defect is discovered, this Case ID is preserved as failed and any correction must use a new Case ID.

## 12. Evidence-count lock

Before execution:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 4
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 1
NEGATIVE_OR_FAILURE_INTERPRETATION_CASES: 1
METHOD_BOUNDARY_INTERPRETATION_CASES: 1
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
BASELINE_INTERPRETATION_CASES: 1
NO_GAIN_INTERPRETATION_CASES: 1
STRONGEST_REASONABLE_BASELINE_INTERPRETATION: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
```

A 60/60 PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: +1
BASELINE_INTERPRETATION_CASES: +1
NO_GAIN_INTERPRETATION_CASES: +1
STRONGEST_REASONABLE_BASELINE_INTERPRETATION: established_at_constructed_evidence_level
```

It does not establish reproducibility, external applicability, independent validation, practical superiority, maturity, method survival, non-merger, or permanent independence.

## 13. Next if passed

Proceed to deterministic same-project retrace using frozen Interpretation artifacts. External validation remains deferred until internal standardization is complete.
