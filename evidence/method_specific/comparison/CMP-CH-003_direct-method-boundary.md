# CMP-CH-003 Result / DSD 비교론 Direct Method-Boundary Challenge 결과

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `68d330bc43b78591be2ef2c197d6a177302789aa`  
Precommit blob: `22c36cdfabe2518f577ddc05957844108b4f0de8`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-003
CASE_CLASS: direct_method_boundary_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
```

The precommit was fetched at its immutable commit before execution. No task, neighboring-method request, handoff expectation, terminal state, or scoring item was changed.

## 2. B1 — Analysis boundary

Visible structural evaluation:

```text
f1(a0)=b0
f1(a1)=b1
f1 bijective: PASS
visible relation preservation: PASS
inverse preservation: PASS
readiness status preservation: PASS
COMPARISON_ELEMENT_COVERAGE: exhaustive at frozen visible target resolution
```

Therefore the supplied visible structures satisfy the frozen strict-equivalence criterion:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT
STRUCTURAL_EQUIVALENCE_RESULT: yes at visible target resolution
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
```

The auxiliary request asks for hidden internal decomposition of `a1` and `b1`. No such records exist.

```text
INTERNAL_DECOMPOSITION_INVENTED: no
ANALYSIS_OPERATION_PERFORMED_BY_COMPARISON: no
AUXILIARY_METHODS_OR_HANDOFFS: ANALYSIS_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The legitimate visible Comparison result remains resolved while the unsupported internal-decomposition request is handed off.

## 3. B2 — Classification boundary

Supplied map execution:

```text
f2(x0)=y0
f2(x1)=y1
f2(x2)=y2
f2 bijective: PASS
relation preservation: PASS
inverse preservation: PASS
COMPARISON_ELEMENT_COVERAGE: exhaustive at target resolution
```

Therefore:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
```

The separate taxonomy `{LINEAR_CHAIN, BRANCHED_GRAPH}` is supplied, but taxonomy assignment is a Classification operation rather than cross-subject correspondence evaluation.

```text
CLASSIFICATION_ASSIGNMENT_PERFORMED_BY_COMPARISON: no
HIDDEN_CLASSIFICATION_SUBSTITUTION: no
AUXILIARY_METHODS_OR_HANDOFFS: CLASSIFICATION_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The presence of a taxonomy does not erase the method boundary.

## 4. B3 — Transformation boundary

Frozen representations remain:

```text
A3: RA = Cartesian-like coordinates (1,0)
B3: RB = polar-like coordinates (r=1, theta=0)
```

The task requires component-wise comparison after normalization into one common representation, but no transformed representation or bridge is supplied.

```text
PRECOMPARISON_TRANSFORMATION_POLICY: external_transformation_handoff_required
SUPPLIED_TRANSFORMED_REPRESENTATION: none
ENCODING_OR_BRIDGE_RULE: none supplied
MAP_FAMILY_SOURCE: unavailable until common representation is supplied
```

Execution therefore stops before substantive comparison:

```text
UNSUPPLIED_NORMALIZATION_OR_CONVERSION_PERFORMED: no
SUBSTANTIVE_COMPARISON_PERFORMED: no
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_BLOCKED
AUXILIARY_METHODS_OR_HANDOFFS: TRANSFORMATION_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No Cartesian/polar conversion was invented and relabeled as a Comparison map.

## 5. B4 — Audit boundary

Direct field comparison gives:

```text
input:
  REPORT_A = 2
  REPORT_B = 2
  -> equal

process step:
  REPORT_A = multiply_by_3
  REPORT_B = add_4
  -> different

final result:
  REPORT_A = 6
  REPORT_B = 6
  -> equal
```

Thus:

```text
VISIBLE_COMPARISON_RESULT:
  input equal
  final result equal
  process step different
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
```

The equal result does not erase the process-trace distinction.

A separate audit standard states that `multiply_by_3` is the accepted process, but assigning procedural conformance is an Audit verdict.

```text
AUDIT_CONFORMANCE_VERDICT_PERFORMED_BY_COMPARISON: no
HIDDEN_AUDIT_VERDICT: no
AUXILIARY_METHODS_OR_HANDOFFS: AUDIT_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Comparison identifies the difference without deciding which prior process passes Audit.

## 6. B5 — Provenance/Lineage boundary

Supplied snapshot comparison:

```text
f5(p0)=q0
f5(p1)=q1
f5 bijective: PASS
snapshot relation preservation: PASS
inverse preservation: PASS
readiness-status preservation: PASS
COMPARISON_ELEMENT_COVERAGE: exhaustive at snapshot target resolution
```

Therefore:

```text
VISIBLE_COMPARISON_RESULT: STRICT_EQUIVALENT at snapshot target resolution
STRUCTURAL_EQUIVALENCE_RESULT: yes at snapshot target resolution
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
```

No historical successor or identity record is supplied.

```text
LINEAGE_IDENTITY_CLAIM_RESULT: not_established
PROVENANCE_OR_LINEAGE_INFERENCE_PERFORMED_BY_COMPARISON: no
AUXILIARY_METHODS_OR_HANDOFFS: PROVENANCE_LINEAGE_REQUIRED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Snapshot structural equivalence is preserved separately from historical identity.

## 7. Boundary summary

```text
BOUNDARY                COMPARISON RESULT                    HANDOFF
Analysis                STRICT_EQUIVALENT / RESOLVED        ANALYSIS_REQUIRED
Classification          STRICT_EQUIVALENT / RESOLVED        CLASSIFICATION_REQUIRED
Transformation          UNDETERMINED / BLOCKED               TRANSFORMATION_REQUIRED
Audit                   COMPARISON_PROFILE / RESOLVED        AUDIT_REQUIRED
Provenance/Lineage      STRICT_EQUIVALENT / RESOLVED        PROVENANCE_LINEAGE_REQUIRED
```

All five runs are `CONFORMANT`; all gain ledgers remain `NOT_ASSESSED`.

## 8. Preserved distinctions

```text
COMPARISON_EQUIVALENCE
!= INTERNAL_DECOMPOSITION

COMPARISON_RELATION
!= TAXONOMY_ASSIGNMENT

COMPARISON_MAP
!= UNSUPPLIED_TRANSFORMATION

TRACE_DIFFERENCE
!= AUDIT_CONFORMANCE_VERDICT

STRUCTURAL_EQUIVALENCE
!= LINEAGE_IDENTITY

LEGITIMATE_COMPARISON_RESULT + NEIGHBORING_HANDOFF
!= METHOD_BOUNDARY_FAILURE

MISSING_PREREQUISITE_TRANSFORMATION
-> COMPARISON_BLOCKED
```

## 9. Precommitted scoring

```text
A. immutable protocol / precommit discipline   8 / 8 PASS
B. B1 Analysis boundary                        8 / 8 PASS
C. B2 Classification boundary                  8 / 8 PASS
D. B3 Transformation boundary                  8 / 8 PASS
E. B4 Audit boundary                           8 / 8 PASS
F. B5 Provenance/Lineage boundary              8 / 8 PASS

PRECOMMITTED_REQUIRED_CHECKS:                 48
PASSED:                                        48
FAILED:                                         0
CHALLENGE_VERDICT:                           PASS
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 10. Evidence increment

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
BOUNDARY_COMPARISON_CASE_INCREMENT: +1
```

Post-run state:

```text
DIRECT_COMPARISON_PILOTS: 3
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 11. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No direct boundary collapse or Protocol-v0.1 contradiction was exposed by this challenge.

## 12. Limits and method-registry discipline

This challenge establishes only that the frozen boundary tasks were handled without neighboring-method absorption.

```text
BOUNDARY_PASS != PERMANENT_METHOD_INDEPENDENCE
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

No method survival, merger, absorption, deletion, or permanent-independence conclusion is drawn.

## 13. Next

Run a separately precommitted competent-baseline `NO_GAIN` challenge `CMP-CH-004`. The baseline should receive the same subject/map/coverage/bridge/status records and be allowed to preserve all claim-relevant distinctions. A fair `NO_GAIN` result must remain acceptable.
