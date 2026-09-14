# INT-CH-006 Result / DSD Interpretation Strongest-Reasonable-Baseline Challenge

Status: **EXECUTED — 60/60 PASS / NO_GAIN**  
Date: **2026-09-15**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol commit: `40110a8a779f0ac6ff93ede6414544b8ec548fdf`  
Protocol blob: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`  
Precommit commit: `fca5d6a9a8c4c3ca8a890ad1c028225868e3fa84`  
Precommit blob: `da1b2218acccd15063326382f92faa561f6b4edf`

## 1. Evidence identity

```text
CASE_ID: INT-CH-006
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_SOURCE_CONTEXT_INTERPRETATION_ENGINE
RESULT: PASS
INTERPRETATION_METHOD_GAIN_STATUS: NO_GAIN
EXTERNAL_APPLICATION: no
```

The immutable precommit was read before execution. No witness, version, transformation mapping, reconstruction handoff, temporal context, bridge, candidate-reading set, baseline capability, gain criterion, or scoring item was changed after execution began.

## 2. R1 — witness/version conflict without hidden harmonization

DSD execution:

```text
W1-A -> supports R1A: S necessary for opening
W1-B -> supports R1B at witness-local scope: S compatible with possible opening; necessity not established
WITNESS_PRECEDENCE -> none supplied
HIDDEN_HARMONIZATION -> no
CROSS_WITNESS_SINGLE_READING -> not forced
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_PROTOCOL_CONFORMANCE -> CONFORMANT
```

B1 execution from the same records:

```text
W1-A and W1-B preserved as distinct witnesses/versions
no precedence invented
no harmonized synthetic reading invented
witness-conditioned alternatives retained
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
WITNESS_CONFLICT != METHOD_FAILURE
NO_PRECEDENCE_RULE != LICENSE_TO_HARMONIZE
MULTIPLE_WITNESS_SUPPORTED_READINGS != UNDERDETERMINED automatically
```

No gain is established on R1.

## 3. R2 — competing supplied normalization mappings

DSD execution:

```text
T2-A: Q -> QUIESCENT
  R2A -> SUPPORTED
  CLAIM_STRENGTH -> BRIDGE_DEPENDENT_INTERPRETATION

T2-B: Q -> QUEUED
  R2B -> SUPPORTED
  CLAIM_STRENGTH -> BRIDGE_DEPENDENT_INTERPRETATION

R2C raw source directly states QUIESCENT
  -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET

TRANSFORMATION_PROVENANCE -> preserved for T2-A and T2-B
HIDDEN_TRANSFORMATION_SELECTION -> no
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_PROTOCOL_CONFORMANCE -> CONFORMANT
```

The claim-strength label is attached to the decoded reading, not to the raw token. The two supplied decoding mappings remain explicit transformation/bridge records rather than being collapsed into raw-source identity.

B1 execution:

```text
both supplied mappings retained
no preferred mapping invented
raw source kept distinct from both decoded renderings
mapping provenance retained
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
NORMALIZED_RENDERING != RAW_SOURCE_IDENTITY
MULTIPLE_LICENSED_MAPPINGS != LICENSE_TO_CHOOSE_ONE_SILENTLY
```

No gain is established on R2.

## 4. R3 — reconstruction-handoff provenance

DSD execution:

```text
RH3 candidate stable -> SUPPORTED as reconstruction-handoff-dependent candidate
RH3 candidate silent -> SUPPORTED as reconstruction-handoff-dependent candidate
observed source directly states stable -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
observed source directly states silent -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
OBSERVED_SOURCE_RECORD -> preserved separately
RECONSTRUCTION_HANDOFF -> preserved separately
UNIQUE_RECOVERY -> not claimed
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_PROTOCOL_CONFORMANCE -> CONFORMANT
```

No new claim-strength category was invented. The support ledger records the explicit `RECONSTRUCTION_HANDOFF` provenance and refuses `DIRECT_SOURCE_STATEMENT` status for either reconstructed token.

B1 execution:

```text
stable/silent candidates retained as reconstruction outputs
neither candidate promoted to observed text
nonuniqueness retained
candidate provenance sufficient to retrace support
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
ADMISSIBLE_RECONSTRUCTION != UNIQUE_RECOVERY
HANDOFF_SUPPORT != SOURCE_TEXT_PROMOTION
```

No gain is established on R3.

## 5. R4 — time-indexed context change under identical wording

DSD execution:

```text
R4A t0 blue flag -> HAZARD
  -> SUPPORTED / CONTEXT_SUPPORTED_INFERENCE
R4B t1 blue flag -> ALL_CLEAR
  -> SUPPORTED / CONTEXT_SUPPORTED_INFERENCE
R4C identical wording proves identical meaning across t0/t1
  -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
LATER_CONTEXT_BACK_PROJECTED_TO_t0 -> no
EARLIER_CONTEXT_FORWARDED_TO_t1 -> no
TEMPORAL_CONTEXT_SCOPE -> preserved
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
INTERPRETATION_PROTOCOL_CONFORMANCE -> CONFORMANT
```

B1 execution:

```text
t0/P0 and t1/P1 context records preserved separately
hazard/all-clear readings retained only in their time scopes
same wording not used as a semantic-identity rule
no context back-projection
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
SAME_WORDING != SAME_MEANING_ACROSS_CONTEXT
TEMPORAL_ORDER != SEMANTIC_IDENTITY
LATER_CONTEXT != ORIGINAL_CONTEXT
```

No gain is established on R4.

## 6. R5 — claim-strength interaction

DSD execution:

```text
R5A obligation to close V when pressure exceeds P
  -> SUPPORTED / DIRECT_SOURCE_STATEMENT
R5B V in fact closed in every such event
  -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R5C pressure exceeding P is causally sufficient by itself
  -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R5D V will certainly close next time
  -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
NORMATIVE_TO_FACTUAL_UPGRADE -> no
OBLIGATION_TO_PREDICTION_UPGRADE -> no
OBLIGATION_TO_CAUSAL_SUFFICIENCY_UPGRADE -> no
TERMINAL -> INTERPRETATION_RESOLVED_SINGLE
INTERPRETATION_PROTOCOL_CONFORMANCE -> CONFORMANT
```

B1 execution:

```text
obligation rule retained as normative source content
no execution-log claim invented
no causal mechanism inferred
no certainty prediction inferred
claim-strength trace retained
TERMINAL -> INTERPRETATION_RESOLVED_SINGLE
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
OBLIGATION != OCCURRENCE
OBLIGATION != PREDICTION
CONDITIONAL_RULE != CAUSAL_SUFFICIENCY_PROOF
DIRECT_SOURCE_STATEMENT != EMPIRICAL_CONFIRMATION
```

No gain is established on R5.

## 7. DSD versus B1 task-level comparison

```text
SUBCASE  DSD MAIN RESULT                              B1 MAIN RESULT
R1       witness-conditioned RESOLVED_MULTI            same
R2       mapping-conditioned RESOLVED_MULTI            same
R3       reconstruction-conditioned RESOLVED_MULTI     same
R4       time/context-conditioned RESOLVED_MULTI       same
R5       obligation-only RESOLVED_SINGLE               same
```

B1 preserved enough witness/version, transformation, reconstruction, temporal-context, bridge, claim-strength, ambiguity, and source-to-reading provenance records to deterministically reconstruct every frozen result.

## 8. Gain evaluation

```text
G1 WITNESS_VERSION_CONFLICT_GAIN: NOT_ESTABLISHED
G2 TRANSFORMATION_PROVENANCE_GAIN: NOT_ESTABLISHED
G3 RECONSTRUCTION_HANDOFF_GAIN: NOT_ESTABLISHED
G4 TEMPORAL_CONTEXT_SCOPE_GAIN: NOT_ESTABLISHED
G5 CLAIM_STRENGTH_INTERACTION_GAIN: NOT_ESTABLISHED
G6 AMBIGUITY_AND_NO_HIDDEN_HARMONIZATION_GAIN: NOT_ESTABLISHED
G7 TRACEABILITY_GAIN: NOT_ESTABLISHED
```

Therefore:

```text
INTERPRETATION_METHOD_GAIN_STATUS: NO_GAIN
STRONGEST_REASONABLE_BASELINE_INTERPRETATION:
  established_at_constructed_evidence_level
```

This is a successful strongest-reasonable-baseline comparison at constructed-evidence level. It is not a DSD superiority result.

## 9. Precommitted scoring

```text
A. IMMUTABLE_FAIRNESS_DISCIPLINE:      8/8 PASS
B. DSD_EXECUTION:                     18/18 PASS
C. B1_EXECUTION:                      18/18 PASS
D. COMPARATIVE_GAIN:                   9/9 PASS
E. SCOPE_PROTOCOL_PRESSURE:             7/7 PASS
TOTAL:                                 60/60 PASS
```

```text
CHALLENGE_VERDICT: PASS
INTERPRETATION_METHOD_GAIN_STATUS: NO_GAIN
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 10. Counter update

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 6
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 5
SUCCESSFUL_POSITIVE_INTERPRETATION_CASES: 1
NEGATIVE_OR_FAILURE_INTERPRETATION_CASES: 1
METHOD_BOUNDARY_INTERPRETATION_CASES: 1
PRESERVED_FAILED_CHALLENGE_DESIGNS: 1
BASELINE_INTERPRETATION_CASES: 2
NO_GAIN_INTERPRETATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_INTERPRETATION: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_INTERPRETATION_EVIDENCE_STATUS: validation_in_progress
```

## 11. Scope and registry discipline

This result establishes only strongest-reasonable-baseline coverage at the constructed-evidence level.

It does not establish:

```text
reproducibility
external applicability
independent validation
practical superiority
maturity promotion
permanent method independence
```

And:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

## 12. Next

Precommit and execute deterministic same-project retrace from frozen Interpretation artifacts. The retrace must reconstruct a prior result without changing the protocol, task, source, bridge, scope, or verdict records. It increments reproducibility only if deterministic reconstruction succeeds. External validation remains deferred until internal standardization is complete.
