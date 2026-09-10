# SYN-CH-001 Precommit / DSD 합성론 첫 Positive Challenge 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Protocol blob: `7367818f2d93125c84db7d559ac1409ed0e8d2e5`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-001
CASE_CLASS: positive
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
```

This file freezes the challenge before the result file is created.
No later correction may overwrite this precommit. If the fixture or scoring proves defective, preserve the failure and use a new case ID.

## 2. Frozen task

```text
SYNTHESIS_TASK_ID: SYN-TASK-001
TASK_SCOPE: finite symbolic three-component chain synthesis over candidate universe {K1,K2,K3,K4,K5,K6}
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component sequence
  exact adjacent interface mappings
  participating component identities
COMPOSITION_COVERAGE: exhaustive relative only to frozen candidate universe {K1,K2,K3,K4,K5,K6}
```

No claim is made about every possible composition of the component inventory outside the six frozen records.

## 3. Frozen component records

All five components are individually admitted on the Formation side.
Their `readiness` records are General-Property-side input statuses used only as a cross-component prerequisite.
They are **not** automatically lifted into a whole-object property.

```text
SRC
  role: source
  input_port: NONE
  output_port: alpha
  readiness: DEFINED_NONZERO
  formation_status: ADMITTED

AD0
  role: adapter_zero
  input_port: alpha
  output_port: beta
  readiness: DEFINED_ZERO
  formation_status: ADMITTED

AD1
  role: adapter_nonzero
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO
  formation_status: ADMITTED

ADU
  role: adapter_unknown
  input_port: alpha
  output_port: beta
  readiness: APPLICABLE_BUT_UNDEFINED
  formation_status: ADMITTED

SNK
  role: sink
  input_port: beta
  output_port: NONE
  readiness: DEFINED_NONZERO
  formation_status: ADMITTED
```

The challenge intentionally tests:

```text
DEFINED_ZERO
!= APPLICABLE_BUT_UNDEFINED
```

A defined zero readiness record satisfies the frozen `readiness is defined` prerequisite.

## 4. Frozen composition rule

Rule name:

```text
R_CHAIN_3
```

Rule source:

```text
constructed_same_session_fixture
```

Rule:

1. Each candidate is an ordered three-component chain `(X ⊙ Y) ⊙ Z`.
2. The first link is valid only when `X.output_port` and `Y.input_port` both exist and have exactly the same type.
3. The second link is valid only when `Y.output_port` and `Z.input_port` both exist and have exactly the same type.
4. Every participating component must have `readiness` applicable and defined. `DEFINED_ZERO` counts as defined.
5. No whole-object readiness Property is created by this challenge.
6. Successful candidates retain all participating component identities and both adjacency relations at the declared target resolution.
7. No information loss is permitted at the declared target resolution.

Frozen rule profile:

```text
COMPOSITION_ARITY: iterated_binary_to_fixed_three_component_chain
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
MULTIPLICITY_POLICY: each listed component occurrence used exactly as written in candidate record

COMPOSITION_LAW_PROFILE:
  COMMUTATIVITY: supplied_false
  ASSOCIATIVITY: unspecified
  IDENTITY_RULE: not_supplied
  IDEMPOTENCE_RULE: not_supplied
  OTHER_COMPOSITION_LAWS: none
  LAW_SOURCE: R_CHAIN_3 fixture

GROUPING_OR_PARENTHESIZATION_POLICY:
  fixed_left_associated_only
  evaluate (X ⊙ Y) ⊙ Z exactly as written
  do not regroup
```

## 5. Frozen candidate basis

```text
K1 = (SRC ⊙ AD0) ⊙ SNK
K2 = (SRC ⊙ AD1) ⊙ SNK
K3 = (SRC ⊙ ADU) ⊙ SNK
K4 = (AD0 ⊙ SRC) ⊙ SNK
K5 = (SRC ⊙ SNK) ⊙ AD0
K6 = (AD1 ⊙ SNK) ⊙ SRC
```

```text
COMPOSITION_CANDIDATE_BASIS: explicit frozen family {K1,K2,K3,K4,K5,K6}
COMPOSITION_COVERAGE: exhaustive relative to SYN-TASK-001 only
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
  two successful candidates are materially equal only if ordered component sequence and both adjacent interface mappings are identical at TARGET_RESOLUTION
```

Thus candidate IDs themselves do not establish distinctness, but under the frozen rule `K1` and `K2` are materially distinct because the middle component identity differs.

## 6. Frozen hard conditions

```text
H1 COMPONENT_ADMISSION
  every participating component is Formation-admitted

H2 ADJACENT_INTERFACE_MATCH
  each required adjacent output/input pair exists and has identical interface type

H3 READINESS_DEFINED
  every participating component readiness status is applicable and defined
  DEFINED_ZERO passes
  APPLICABLE_BUT_UNDEFINED fails

H4 SUPPORT_RETENTION
  successful synthesis retains all participating component identities

H5 RELATION_RETENTION
  successful synthesis retains both declared adjacency relations

H6 NO_TARGET_RESOLUTION_INFORMATION_LOSS
  no ordered-component or adjacent-interface information inside TARGET_RESOLUTION is lost
```

Full claim-relevant failure sets are required for rejected candidates, but conditions downstream of a failed composition prerequisite need not be fabricated as failures when they were not applicable to an unformed whole.

## 7. Other frozen task fields

```text
PROPERTY_LIFT_OR_REDECLARATION_RULE:
  none; do not create or infer a whole-object readiness Property

SUPPORT_RETENTION_REQUIREMENT:
  exact participating component identity retention for successful candidates

RELATION_RETENTION_REQUIREMENT:
  exact adjacent-link retention for successful candidates

INFORMATION_LOSS_TOLERANCE:
  none at TARGET_RESOLUTION

NEW_FORMATION_MODEL_POLICY:
  remain_within_inherited_formation_background
  result is a composition record; no new independent Stage-VI whole identity is claimed

RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
  not_applicable because CLAIMED_OUTPUT_LEVEL is SYNTHESIS_SPACE over complete three-component candidate records

ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
  static_order_only
  no time-resolved assembly feasibility claim

TARGET_DSD_LAYER_SCOPE:
  Formation + General Property
  Static Aggregation not_used
  Dynamics not_used

DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: not_used
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not_used
```

## 8. Precommitted expected candidate results

```text
K1
  EXPECTED_RESULT: admissible
  EXPECTED_FAILURE_SET: NONE
  reason: alpha->alpha and beta->beta; all readiness defined, including AD0 = DEFINED_ZERO

K2
  EXPECTED_RESULT: admissible
  EXPECTED_FAILURE_SET: NONE
  reason: alpha->alpha and beta->beta; all readiness defined

K3
  EXPECTED_RESULT: rejected
  EXPECTED_FAILURE_SET: {H3}
  reason: ADU readiness = APPLICABLE_BUT_UNDEFINED

K4
  EXPECTED_RESULT: rejected
  EXPECTED_FAILURE_SET: {H2}
  reason: AD0.output=beta cannot connect to SRC.input=NONE, and SRC.output=alpha cannot connect to SNK.input=beta

K5
  EXPECTED_RESULT: rejected
  EXPECTED_FAILURE_SET: {H2}
  reason: SRC.output=alpha cannot connect to SNK.input=beta; SNK has no output for AD0.input=alpha

K6
  EXPECTED_RESULT: rejected
  EXPECTED_FAILURE_SET: {H2}
  reason: AD1.output=beta connects to SNK.input=beta, but SNK has no output for SRC.input=NONE
```

Expected synthesis-admissible family:

```text
{K1,K2}
```

Expected material-distinctness result:

```text
K1 != K2 at TARGET_RESOLUTION
```

## 9. Precommitted three-ledger expectation

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

`NOT_ASSESSED` is mandatory because no baseline comparison is part of SYN-CH-001.

## 10. Precommitted checks

Total required checks: **28**.

```text
A. task/rule lock integrity: 8
  A1 protocol commit/blob fixed
  A2 claimed output level fixed
  A3 target resolution fixed
  A4 candidate universe/coverage fixed
  A5 order sensitivity and left grouping fixed
  A6 composition-law profile fixed
  A7 equivalence rule fixed
  A8 static process scope fixed

B. candidate verdicts: 6
  B1-B6 exact result for K1-K6

C. rejected-candidate failure sets: 4
  C1 K3 exact {H3}
  C2 K4 exact {H2}
  C3 K5 exact {H2}
  C4 K6 exact {H2}

D. successful-candidate status/retention guards: 4
  D1 K1 treats DEFINED_ZERO as defined
  D2 K1 support/relation/no-loss checks pass
  D3 K2 support/relation/no-loss checks pass
  D4 no whole readiness Property is auto-created

E. closure/material-distinctness: 3
  E1 admissible family exactly {K1,K2}
  E2 K1 and K2 materially distinct under frozen rule
  E3 no unexamined composition outside K1-K6 is claimed evaluated

F. three ledgers: 3
  F1 terminal status SYNTHESIS_ADMISSIBLE
  F2 protocol conformance CONFORMANT
  F3 method gain NOT_ASSESSED
```

Decision rule:

```text
28/28 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

No post-hoc check deletion, expected-output change, candidate replacement, rule change, or coverage expansion is allowed.

## 11. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
```

Only a completed result record may add the first direct constructed pilot.
A PASS does not establish external applicability, baseline superiority, reproducibility, independent validation, or Synthesis method maturity.
