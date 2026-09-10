# SYN-CH-005 Precommit / Corrected DSD 합성론 NO_GAIN Baseline Challenge 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Historical failed predecessor: `SYN-CH-004`, postexecution audit commit `fe55899cb08946d15e8d901d68f6097837b82b7d`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-005
CASE_CLASS: no_gain_baseline
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B0_TYPED_CHAIN_CHECKER
PREDECESSOR_CASE: SYN-CH-004 challenge-design defect preserved
```

This is a prospective replacement case, not a rewrite of SYN-CH-004.

## 2. Frozen task

```text
SYNTHESIS_TASK_ID: SYN-TASK-005
TASK_SCOPE: finite ordered three-component chain composition
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component identities
  exact adjacent interface mappings
  exact middle-component readiness status/value class
COMPOSITION_CANDIDATE_BASIS: {R1,R2,R3,R4,R5}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-005
TARGET_DSD_LAYER_SCOPE: Formation + General Property
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE: static_order_only
```

## 3. Frozen components

All components are Formation-admitted.

```text
SRC
  input_port: NONE
  output_port: alpha
  readiness: DEFINED_ZERO

M0
  input_port: alpha
  output_port: beta
  readiness: DEFINED_ZERO

M1
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO

MU
  input_port: alpha
  output_port: beta
  readiness: APPLICABLE_BUT_UNDEFINED

MX
  input_port: delta
  output_port: beta
  readiness: DEFINED_NONZERO

SNK
  input_port: beta
  output_port: NONE
  readiness: DEFINED_ZERO
```

The explicit readiness records on `SRC` and `SNK` prevent the predecessor ambiguity when either occupies the middle syntactic position in a malformed candidate.

## 4. Supplied rule

```text
R_CHAIN_READY
(X ⊙ Y) ⊙ Z is synthesis-admissible iff:
  H1 every participating component is Formation-admitted;
  H2 X.output exists and exactly matches Y.input;
  H3 Y.output exists and exactly matches Z.input;
  H4 readiness(Y) is DEFINED_ZERO or DEFINED_NONZERO.
```

Rule/profile:

```text
COMPOSITION_ARITY: ternary through fixed binary nesting
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
COMMUTATIVITY: supplied_false
ASSOCIATIVITY: unspecified
GROUPING_OR_PARENTHESIZATION_POLICY: fixed_left_associated_only
MULTIPLICITY_POLICY: one listed occurrence of each role per candidate
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
  material equality iff all TARGET_RESOLUTION fields match
PROPERTY_LIFT_OR_REDECLARATION_RULE: not_used
NEW_FORMATION_MODEL_POLICY: remain_within_inherited_formation_background
INFORMATION_LOSS_TOLERANCE: none at TARGET_RESOLUTION
```

## 5. Frozen candidates and expected results

```text
R1 = (SRC ⊙ M0) ⊙ SNK
  expected: admissible / NONE

R2 = (SRC ⊙ M1) ⊙ SNK
  expected: admissible / NONE

R3 = (SRC ⊙ MU) ⊙ SNK
  expected: rejected / {H4}

R4 = (SRC ⊙ MX) ⊙ SNK
  expected: rejected / {H2}

R5 = (M1 ⊙ SRC) ⊙ SNK
  expected: rejected / {H2,H3}
  because readiness(SRC)=DEFINED_ZERO satisfies H4
```

Expected DSD closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {R1,R2}
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

R1 and R2 are materially distinct at TARGET_RESOLUTION.

## 6. Competent baseline lock

```text
BASELINE: B0_TYPED_CHAIN_CHECKER
```

B0 receives exactly the same:

```text
component identities
Formation-admitted flags
input/output ports
all readiness status classes
R_CHAIN_READY
order/grouping lock
candidate basis {R1-R5}
coverage declaration
target resolution
```

B0 may preserve the exact raw vocabulary `DEFINED_ZERO`, `DEFINED_NONZERO`, and `APPLICABLE_BUT_UNDEFINED`.
It evaluates all H1-H4 checks independently, preserves full failure sets, returns the complete admissible family, preserves R1/R2 target distinctness, and performs no neighboring-method operation.

Expected B0 result:

```text
R1 -> admissible / NONE
R2 -> admissible / NONE
R3 -> rejected / {H4}
R4 -> rejected / {H2}
R5 -> rejected / {H2,H3}
BASELINE_ADMISSIBLE_FAMILY: {R1,R2}
```

## 7. Frozen gain criteria

```text
G1 STATUS_DISTINCTION_GAIN
G2 FAILURE_TRACEABILITY_GAIN
G3 COMPOSITION_CLOSURE_GAIN
G4 TARGET_DISTINCTNESS_GAIN
G5 RETRACEABILITY_GAIN
```

Each criterion is established only if DSD preserves a claim-relevant capability that B0 does not preserve on the same frozen inputs.
If both are correct and match on all five dimensions, final method gain is `NO_GAIN`.
Extra DSD bookkeeping, terminology, or formatting does not count as gain.

## 8. Precommitted scoring

Total required checks: **37**.

```text
A. lineage/precommit integrity: 8
  A1 Protocol commit fixed
  A2 SYN-CH-004 failure preserved rather than rewritten
  A3 corrected Case ID is new
  A4 all component readiness records fixed before execution
  A5 candidate basis/coverage fixed
  A6 baseline capabilities fixed
  A7 gain criteria fixed
  A8 no post-hoc weakening of B0/task

B. DSD checks: 10
  B1 R1 admissible
  B2 R2 admissible
  B3 R3 rejected {H4}
  B4 R4 rejected {H2}
  B5 R5 rejected {H2,H3}
  B6 family exactly {R1,R2}
  B7 R1/R2 materially distinct
  B8 terminal SYNTHESIS_ADMISSIBLE
  B9 conformance CONFORMANT
  B10 no neighboring operation absorbed

C. baseline checks: 9
  C1-C5 exact R1-R5 verdict/failure-set match
  C6 family exactly {R1,R2}
  C7 target distinctness preserved
  C8 full failure sets preserved
  C9 no neighboring operation

D. gain checks: 7
  D1-D5 G1-G5 NOT_ESTABLISHED if baseline matches
  D6 final gain = NO_GAIN
  D7 NO_GAIN != method failure

E. scope discipline: 3
  E1 no superiority claim
  E2 no external/reproducibility/independence/maturity claim
  E3 no whole-Property/temporal/global claim
```

Decision:

```text
37/37 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

## 9. Evidence-count lock

At precommit time, successful evidence categories remain:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 4 including failed SYN-CH-004 attempt
SUCCESSFUL_POSITIVE_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_CASES: 1
SUCCESSFUL_BOUNDARY_CASES: 1
SUCCESSFUL_NO_GAIN_CASES: 0
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 0
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGN: 1
```

A 37/37 PASS may add one successful NO_GAIN case and one successful baseline-comparison pass. It remains one additional direct constructed pilot.
