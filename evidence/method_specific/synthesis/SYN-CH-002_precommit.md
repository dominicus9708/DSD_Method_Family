# SYN-CH-002 Precommit / DSD 합성론 Negative-Failure Challenge 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Protocol blob: `7367818f2d93125c84db7d559ac1409ed0e8d2e5`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-002
CASE_CLASS: negative_failure
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
SUBCASES: I, U, B
```

This file freezes all three subcases before execution. No later result may change the frozen coverage class, composition rule availability, expected terminal status, candidate verdict, failure set, or check count. If the fixture is defective, preserve the failure and use a new case ID.

## 2. Challenge purpose

Test whether Protocol v0.1 distinguishes three materially different non-success conditions instead of collapsing them into a generic failure:

```text
exhaustive all rejected
-> SYNTHESIS_INFEASIBLE

non-exhaustive coverage insufficient for requested uniqueness closure
-> SYNTHESIS_UNDERDETERMINED

claim-required composition rule unavailable before substantive evaluation
-> SYNTHESIS_BLOCKED
```

No baseline comparison is active in any subcase, so every method-gain ledger is expected to be `NOT_ASSESSED`.

---

# SUBCASE I — exhaustive all rejected

## 3. Frozen task I

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-I
TASK_SCOPE: finite symbolic two-component ordered-pair synthesis over frozen universe {I1,I2}
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component identities
  exact single interface mapping
COMPOSITION_CANDIDATE_BASIS: explicit family {I1,I2}
COMPOSITION_COVERAGE: exhaustive relative to SYN-TASK-002-I
```

Components:

```text
L
  role: left-capable component
  input_port: NONE
  output_port: alpha
  formation_status: ADMITTED

R
  role: right-capable component
  input_port: beta
  output_port: NONE
  formation_status: ADMITTED
```

Supplied composition rule:

```text
R_PAIR_MATCH
A ⊙ B is valid only when A.output_port and B.input_port both exist
and have exactly the same type.
```

Rule profile:

```text
COMPOSITION_ARITY: binary
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
MULTIPLICITY_POLICY: each candidate uses each listed occurrence exactly once
COMMUTATIVITY: supplied_false
ASSOCIATIVITY: not_applicable
IDENTITY_RULE: not_supplied
IDEMPOTENCE_RULE: not_supplied
GROUPING_OR_PARENTHESIZATION_POLICY: binary_only
```

Candidates:

```text
I1 = L ⊙ R
I2 = R ⊙ L
```

Hard conditions:

```text
H1 COMPONENT_ADMISSION
  every participating component is Formation-admitted

H2 INTERFACE_MATCH
  left output and right input both exist and have identical type
```

Expected candidate results:

```text
I1 -> rejected {H2}
  alpha != beta

I2 -> rejected {H2}
  R.output NONE and L.input NONE do not constitute an interface
```

Expected closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_I: {}
COMPOSITION_COVERAGE_I: exhaustive
TERMINAL_SYNTHESIS_STATUS_I: SYNTHESIS_INFEASIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_I: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_I: NOT_ASSESSED
```

`SYNTHESIS_INFEASIBLE` is restricted to this frozen exhaustive composition universe and is not a universal claim about all imaginable components or rules.

---

# SUBCASE U — non-exhaustive uniqueness closure

## 4. Frozen task U

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-U
TASK_SCOPE: symbolic ordered-pair synthesis over supplied component inventory {A,B,C}, but evaluated candidate subset {U1,U2}
CLAIMED_OUTPUT_LEVEL: UNIQUE_SYNTHESIZED_TARGET
TARGET_RESOLUTION:
  exact ordered component identities
  exact interface mapping
COMPOSITION_CANDIDATE_BASIS: explicit evaluated subset {U1,U2}
COMPOSITION_COVERAGE: non_exhaustive
```

Components:

```text
A
  input_port: NONE
  output_port: gamma
  formation_status: ADMITTED

B
  input_port: gamma
  output_port: NONE
  formation_status: ADMITTED

C
  input_port: gamma
  output_port: NONE
  formation_status: ADMITTED
```

Supplied rule: the same binary `R_PAIR_MATCH` rule.

Rule profile:

```text
COMPOSITION_ARITY: binary
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
COMMUTATIVITY: supplied_false
ASSOCIATIVITY: not_applicable
GROUPING_OR_PARENTHESIZATION_POLICY: binary_only
```

Evaluated candidates:

```text
U1 = A ⊙ B
U2 = B ⊙ A
```

The inventory also contains component `C`, but `A ⊙ C` is deliberately **outside the frozen evaluated candidate basis**. Its existence makes the non-exhaustive coverage materially relevant; Protocol v0.1 must not silently expand the candidate basis after outcome inspection.

Expected candidate results within frozen coverage:

```text
U1 -> admissible
  gamma -> gamma

U2 -> rejected {H2}
  B.output NONE and A.input NONE do not constitute an interface
```

Expected covered admissible family:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_U_WITHIN_COVERAGE: {U1}
```

Expected closure:

```text
UNIQUE_SYNTHESIZED_TARGET: not established
reason: COMPOSITION_COVERAGE is non_exhaustive and a materially distinct unexamined composition may remain
TERMINAL_SYNTHESIS_STATUS_U: SYNTHESIS_UNDERDETERMINED
SYNTHESIS_PROTOCOL_CONFORMANCE_U: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_U: NOT_ASSESSED
```

The challenge does not authorize evaluating or importing `A ⊙ C` as a third candidate. It is referenced only to make the frozen non-exhaustive coverage explicit.

---

# SUBCASE B — required rule unavailable

## 5. Frozen task B

```text
SYNTHESIS_TASK_ID: SYN-TASK-002-B
TASK_SCOPE: determine a synthesized target from supplied components P and Q
CLAIMED_OUTPUT_LEVEL: SYNTHESIZED_TARGET
TARGET_RESOLUTION: exact ordered component identities and interface relation
COMPONENT_SET_OR_FAMILY: {P,Q}
COMPOSITION_RULE: UNAVAILABLE
COMPOSITION_RULE_SOURCE: UNAVAILABLE
COMPOSITION_CANDIDATE_BASIS: not_evaluable_without_rule
COMPOSITION_COVERAGE: unknown
```

Components:

```text
P
  formation_status: ADMITTED
  declared_port_record: available

Q
  formation_status: ADMITTED
  declared_port_record: available
```

The challenge intentionally withholds the claim-required composition rule. Formation Clause VII, notation, coexistence, naming, or a neighboring method may not be substituted for the absent domain composition rule.

Expected result:

```text
SUBSTANTIVE_CANDIDATE_EVALUATION: not performed
SYNTHESIS_ADMISSIBLE_FAMILY_B: not constructed
TERMINAL_SYNTHESIS_STATUS_B: SYNTHESIS_BLOCKED
BLOCKING_BASIS: required composition rule unavailable
SYNTHESIS_PROTOCOL_CONFORMANCE_B: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS_B: NOT_ASSESSED
```

A blocked result is expected to be conformant because Protocol v0.1 requires exposing the missing claim-required input rather than fabricating it.

---

## 6. Shared frozen fields

```text
PROPERTY_LIFT_OR_REDECLARATION_RULE: not_used
SUPPORT_RETENTION_REQUIREMENT: preserve participating component identities when a candidate is admissible
RELATION_RETENTION_REQUIREMENT: preserve tested interface relation when a candidate is admissible
INFORMATION_LOSS_TOLERANCE: none at TARGET_RESOLUTION
NEW_FORMATION_MODEL_POLICY: remain_within_inherited_formation_background
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE: static_order_only
TARGET_DSD_LAYER_SCOPE: Formation only
STATIC_AGGREGATION_LAYER: not_used
DYNAMICS_LAYER: not_used
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: not_used
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED: not_used
```

Subcase B cannot complete rule-dependent relation/retention evaluation because the rule is unavailable; those checks must remain not-evaluated rather than being fabricated as pass or fail.

## 7. Precommitted scoring

Total required checks: **36**.

```text
A. common precommit integrity: 6
  A1 Protocol commit/blob fixed
  A2 three subcase identities fixed
  A3 claimed output level fixed in every subcase
  A4 coverage class fixed in every subcase
  A5 method-gain expectation fixed as NOT_ASSESSED
  A6 no post-hoc Protocol/rule/coverage revision

B. Subcase I: 9
  B1 I1 exact result = rejected
  B2 I1 exact failure set = {H2}
  B3 I2 exact result = rejected
  B4 I2 exact failure set = {H2}
  B5 covered admissible family exactly {}
  B6 coverage preserved as exhaustive
  B7 terminal status = SYNTHESIS_INFEASIBLE
  B8 protocol conformance = CONFORMANT
  B9 method gain = NOT_ASSESSED

C. Subcase U: 10
  C1 U1 exact result = admissible
  C2 U2 exact result = rejected
  C3 U2 exact failure set = {H2}
  C4 covered admissible family exactly {U1}
  C5 coverage preserved as non_exhaustive
  C6 A ⊙ C is not claimed evaluated
  C7 UNIQUE_SYNTHESIZED_TARGET is not established
  C8 terminal status = SYNTHESIS_UNDERDETERMINED
  C9 protocol conformance = CONFORMANT
  C10 method gain = NOT_ASSESSED

D. Subcase B: 6
  D1 unavailable composition rule recognized before substantive completion
  D2 no composition candidate is fabricated
  D3 no rule-dependent interface/retention verdict is fabricated
  D4 terminal status = SYNTHESIS_BLOCKED
  D5 protocol conformance = CONFORMANT
  D6 method gain = NOT_ASSESSED

E. cross-subcase status discipline: 5
  E1 I/U/B terminal statuses are pairwise distinct as precommitted
  E2 global infeasibility is not inferred from Subcase U non-exhaustive coverage
  E3 Subcase U is not relabeled SYNTHESIS_ADMISSIBLE merely because U1 is locally admissible
  E4 Subcase B missing-input condition is not treated as an ordinary rejected candidate
  E5 no method-maturity, external-validity, baseline-superiority, or independent-validation claim is inferred
```

Decision rule:

```text
36/36 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

No failed check may be removed after execution.

## 8. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS: 1
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
```

A completed execution record may add exactly one direct constructed pilot and one negative/failure case, regardless of the three subcases inside this one Case ID.

Even a PASS does not establish external applicability, baseline superiority, `NO_GAIN` behavior, executable method-boundary robustness, reproducibility, independent validation, or method maturity.
