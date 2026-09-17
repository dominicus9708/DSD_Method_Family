# INT-RT-001 Precommit / DSD Interpretation Deterministic Same-Project Retrace

Status: **PRECOMMITTED BEFORE RETRACE EXECUTION**  
Date: **2026-09-17**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**

## 1. Case identity

```text
CASE_ID: INT-RT-001
CASE_CLASS: deterministic_same_project_retrace
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific_reproducibility
EXTERNAL_APPLICATION: no
INDEPENDENT_REPLICATION: no
SELECTED_PRIOR_CASE: INT-CH-006
```

Purpose: reconstruct the frozen claim-relevant outputs of `INT-CH-006` from immutable Interpretation artifacts without changing protocol, task, source, witness/version, transformation, reconstruction handoff, temporal context, bridge, candidate-reading, baseline, gain, or scoring records.

This is a same-project deterministic retrace. It is not blinded, independent, or external replication.

## 2. Frozen artifact set

```text
PROTOCOL_PATH: methods/16_interpretation/PROTOCOL_v0.1.md
PROTOCOL_COMMIT_AT_SELECTED_CASE: 40110a8a779f0ac6ff93ede6414544b8ec548fdf
PROTOCOL_BLOB: dc3c3a46ba170b3b7565a59a7113c473fb02b463

SELECTED_PRECOMMIT_PATH: evidence/method_specific/interpretation/INT-CH-006_precommit.md
SELECTED_PRECOMMIT_COMMIT: fca5d6a9a8c4c3ca8a890ad1c028225868e3fa84
SELECTED_PRECOMMIT_BLOB: da1b2218acccd15063326382f92faa561f6b4edf

ARCHIVED_RESULT_PATH: evidence/method_specific/interpretation/INT-CH-006_strongest-reasonable-baseline.md
ARCHIVED_RESULT_COMMIT: cc7a12c9c3098813701841cab20dd7a630c2f5ff
ARCHIVED_RESULT_BLOB: 819af91ccf79f46cec18e82ca4b7a0196bd4dcb3
```

The protocol and selected precommit are the reconstruction inputs. The archived result is the comparison target after reconstruction.

No artifact may be edited in place for this retrace.

## 3. Frozen retrace procedure

```text
RT1 verify protocol identity and selected-case artifact identities
RT2 read the selected precommit task family and frozen policies
RT3 reconstruct DSD Interpretation outputs for R1-R5 using Protocol v0.1 only
RT4 reconstruct B1 outputs from the frozen B1 capability record and identical task inputs
RT5 reconstruct G1-G7 comparative-gain statuses and final gain status
RT6 reconstruct precommitted score and protocol-pressure statuses
RT7 compare the reconstructed claim-relevant result with the archived INT-CH-006 result
RT8 record any mismatch without repairing either historical artifact
```

No hidden source, external corpus, new bridge, new precedence rule, new transformation, new reconstruction candidate, or post-hoc exception may be introduced.

## 4. Frozen selected-case task summary

```text
R1 witness/version conflict with no declared precedence
R2 competing supplied normalization mappings with provenance
R3 reconstruction-handoff provenance without observed-source promotion
R4 time-indexed context change under identical wording
R5 obligation / occurrence / prediction / causation claim-strength interaction
```

## 5. Frozen expected retrace targets

The retrace is not allowed to modify these targets after execution begins.

```text
R1 DSD terminal -> INTERPRETATION_RESOLVED_MULTI
R2 DSD terminal -> INTERPRETATION_RESOLVED_MULTI
R3 DSD terminal -> INTERPRETATION_RESOLVED_MULTI
R4 DSD terminal -> INTERPRETATION_RESOLVED_MULTI
R5 DSD terminal -> INTERPRETATION_RESOLVED_SINGLE

R1-R5 DSD conformance -> CONFORMANT

B1 task-level terminal mappings -> same as DSD for all five subcases

G1 WITNESS_VERSION_CONFLICT_GAIN -> NOT_ESTABLISHED
G2 TRANSFORMATION_PROVENANCE_GAIN -> NOT_ESTABLISHED
G3 RECONSTRUCTION_HANDOFF_GAIN -> NOT_ESTABLISHED
G4 TEMPORAL_CONTEXT_SCOPE_GAIN -> NOT_ESTABLISHED
G5 CLAIM_STRENGTH_INTERACTION_GAIN -> NOT_ESTABLISHED
G6 AMBIGUITY_AND_NO_HIDDEN_HARMONIZATION_GAIN -> NOT_ESTABLISHED
G7 TRACEABILITY_GAIN -> NOT_ESTABLISHED

INTERPRETATION_METHOD_GAIN_STATUS -> NO_GAIN
STRONGEST_REASONABLE_BASELINE_INTERPRETATION -> established_at_constructed_evidence_level
PROTOCOL_REVISION_REQUIRED -> no
SHARED_CORE_REOPEN_REQUIRED -> no
```

The retrace must also preserve the following claim-relevant distinctions:

```text
WITNESS_CONFLICT != METHOD_FAILURE
NO_PRECEDENCE_RULE != LICENSE_TO_HARMONIZE
NORMALIZED_RENDERING != RAW_SOURCE_IDENTITY
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
ADMISSIBLE_RECONSTRUCTION != UNIQUE_RECOVERY
SAME_WORDING != SAME_MEANING_ACROSS_CONTEXT
OBLIGATION != OCCURRENCE
OBLIGATION != PREDICTION
CONDITIONAL_RULE != CAUSAL_SUFFICIENCY_PROOF
NO_GAIN != METHOD_FAILURE
```

## 6. Frozen mismatch classes

```text
M0 NO_MISMATCH
M1 ARTIFACT_IDENTITY_MISMATCH
M2 TASK_OR_INPUT_MISMATCH
M3 READING_SUPPORT_MISMATCH
M4 TERMINAL_STATUS_MISMATCH
M5 CLAIM_STRENGTH_OR_PROVENANCE_MISMATCH
M6 BASELINE_OUTPUT_MISMATCH
M7 GAIN_STATUS_MISMATCH
M8 SCORE_OR_PROTOCOL_PRESSURE_MISMATCH
M9 UNRETRACEABLE_FROM_FROZEN_RECORD
```

Any M1-M9 finding prevents a successful deterministic-retrace verdict.

Historical artifacts must not be repaired in place to remove a mismatch.

## 7. Frozen scoring

```text
A. artifact identity and procedure lock          8
B. DSD R1-R5 deterministic reconstruction      15
C. B1 and comparative-gain reconstruction      10
D. archived-result correspondence and scope     7
TOTAL                                           40
```

Detailed check lock:

```text
A1 protocol blob matches freeze
A2 selected precommit blob matches freeze
A3 archived result blob matches freeze
A4 no selected artifact edited
A5 retrace procedure RT1-RT8 followed
A6 no external material introduced
A7 no post-hoc bridge/precedence/transformation introduced
A8 mismatch classes frozen before execution

B1 R1 terminal exact match
B2 R1 witness/nonprecedence semantics exact match
B3 R2 terminal exact match
B4 R2 raw/normalized + mapping provenance exact match
B5 R3 terminal exact match
B6 R3 observed/reconstructed distinction exact match
B7 R4 terminal exact match
B8 R4 temporal-context scope exact match
B9 R5 terminal exact match
B10 R5 obligation/occurrence distinction exact match
B11 R5 obligation/prediction distinction exact match
B12 R5 conditional-rule/causal-sufficiency distinction exact match
B13 R1-R5 DSD conformance all CONFORMANT
B14 claim-strength statuses for R2/R4/R5 preserved
B15 neighboring-method handoff provenance preserved

C1-C5 B1 terminal mapping R1-R5 exact match
C6 G1-G7 all NOT_ESTABLISHED
C7 final method gain NO_GAIN
C8 strongest-reasonable-baseline status preserved
C9 protocol revision remains no
C10 shared-core reopen remains no

D1 archived result claim-relevant outputs match retrace
D2 archived score 60/60 reconstructed from selected precommit/result record
D3 mismatch class M0 only
D4 no external applicability claim
D5 no independent-replication claim
D6 no maturity-promotion claim
D7 successful retrace increments only REPRODUCIBILITY_CASES
```

Decision:

```text
40/40 + M0 -> RETRACE_VERDICT: PASS_DETERMINISTIC_SAME_PROJECT
otherwise -> RETRACE_VERDICT: FAIL_OR_UNRETRACEABLE
```

## 8. Evidence-count lock

Before retrace:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 6
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 5
BASELINE_INTERPRETATION_CASES: 2
NO_GAIN_INTERPRETATION_CASES: 2
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
```

A successful retrace changes exactly:

```text
REPRODUCIBILITY_CASES: 0 -> 1
```

It does not increment direct pilots, baseline cases, NO_GAIN cases, external applications, or independent validation.

## 9. Next if passed

Proceed to the frozen-axis internal maturity/standardization audit for Interpretation. External validation remains deferred.