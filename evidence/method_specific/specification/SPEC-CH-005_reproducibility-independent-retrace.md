# SPEC-CH-005 — Reproducibility / Independent Retrace Challenge / 재현성·독립 재추적 도전

Status: **SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
Precommit: [`SPEC-CH-005_precommit.md`](SPEC-CH-005_precommit.md)  
Precommit commit: `dda33b2028c9e5fb0f7b3bef938a8b834219f787`

## 1. Purpose / 목적

This challenge tests whether a frozen specification packet can be retraced reproducibly under the same locked protocol and whether the result is stable under a second processing order.

It explicitly does **not** equate procedural retraceability with a genuinely independent reviewer validation.

```text
procedural retrace reproducibility
!= independent evaluator validation
```

The same assistant/model family performed the retrace in the same project session, so the independent-evaluator claim remains unavailable.

## 2. Locked packet / 고정 패킷

Benchmark: `RetraceSpecToy-v5`  
Requirement packet: `RT-SPEC-005-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: inactive unless case-relevant
DYNAMICS_LAYER: inactive unless case-relevant
REALIZED_AXIS_SPECIALIZATION: inactive unless case-relevant
EXTERNAL_DOMAIN: none
```

The precommit froze eight cases, the retrace schema, two processing orders, allowed status/diagnostic families, and a SHA-256 commitment to the reference answer key.

## 3. Reference-key reveal / 참조키 공개

Plaintext reference key:

```text
R1|usable|NONE
R2|contradictory|C1_MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS
R3|underspecified|U1_ACTIVATION_SCOPE_UNRESOLVED
R4|overconstrained|O1_OPTIONAL_DYNAMICS_INJECTION
R5|no_gain|NG1_OPERATIONALLY_EQUIVALENT_BASELINE
R6|usable|G1_TRACEABILITY_GAIN
R7|usable|NONE
R8|underspecified|B1_REQUIRED_BRIDGE_OMITTED
```

Computed SHA-256:

```text
42dcc5398d60e26c1d7954cc794a7887fb4b03d28ca5c5aaea532564390cb945
```

Precommitted SHA-256:

```text
42dcc5398d60e26c1d7954cc794a7887fb4b03d28ca5c5aaea532564390cb945
```

Result: `REFERENCE_KEY_HASH_MATCH: yes`.

The hash commitment protects against changing the reference classification after retrace scoring, but it does not create evaluator independence.

## 4. Trace A / 재추적 A

Order:

```text
R1 R2 R3 R4 R5 R6 R7 R8
```

| Case | Activation | Bridge obligation | Optional-layer boundary | Source completeness | Final status | Diagnostic |
|---|---|---|---|---|---|---|
| R1 | resolved: ACTIVE | required + explicit B_sd | irrelevant layers inactive | sufficient | usable | NONE |
| R2 | resolved: ACTIVE | not relevant | inactive | sufficient but mutually inconsistent | contradictory | C1_MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS |
| R3 | unresolved | not relevant | inactive | activation information insufficient | underspecified | U1_ACTIVATION_SCOPE_UNRESOLVED |
| R4 | resolved/not task-critical | required bridge already explicit | Dynamics injected despite irrelevance | otherwise sufficient | overconstrained | O1_OPTIONAL_DYNAMICS_INJECTION |
| R5 | resolved | explicit | inactive | operationally complete baseline | no_gain | NG1_OPERATIONALLY_EQUIVALENT_BASELINE |
| R6 | resolved | as source-declared | inactive | facts sufficient; trace links scattered | usable | G1_TRACEABILITY_GAIN |
| R7 | resolved | none because no transfer claim | inactive | sufficient | usable | NONE |
| R8 | resolved | required but missing | inactive | mapping information insufficient | underspecified | B1_REQUIRED_BRIDGE_OMITTED |

`SOURCE_FACT_INVENTION: 0`.

## 5. Trace B / 재추적 B

Order:

```text
R6 R2 R8 R1 R7 R3 R5 R4
```

The same source packet and Protocol v0.1 were applied in the second order.

| Case | Activation | Bridge obligation | Optional-layer boundary | Source completeness | Final status | Diagnostic |
|---|---|---|---|---|---|---|
| R6 | resolved | as source-declared | inactive | facts sufficient; trace links scattered | usable | G1_TRACEABILITY_GAIN |
| R2 | resolved: ACTIVE | not relevant | inactive | sufficient but mutually inconsistent | contradictory | C1_MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS |
| R8 | resolved | required but missing | inactive | mapping information insufficient | underspecified | B1_REQUIRED_BRIDGE_OMITTED |
| R1 | resolved: ACTIVE | required + explicit B_sd | irrelevant layers inactive | sufficient | usable | NONE |
| R7 | resolved | none because no transfer claim | inactive | sufficient | usable | NONE |
| R3 | unresolved | not relevant | inactive | activation information insufficient | underspecified | U1_ACTIVATION_SCOPE_UNRESOLVED |
| R5 | resolved | explicit | inactive | operationally complete baseline | no_gain | NG1_OPERATIONALLY_EQUIVALENT_BASELINE |
| R4 | resolved/not task-critical | required bridge already explicit | Dynamics injected despite irrelevance | otherwise sufficient | overconstrained | O1_OPTIONAL_DYNAMICS_INJECTION |

`SOURCE_FACT_INVENTION: 0`.

## 6. Score / 점수

```text
SOURCE_PACKET_UNCHANGED: yes
PROTOCOL_VERSION_UNCHANGED: yes
REFERENCE_KEY_HASH_MATCH: yes

TRACE_A_FINAL_STATUS_MATCHES: 8/8
TRACE_B_FINAL_STATUS_MATCHES: 8/8
TRACE_A_B_FINAL_STATUS_AGREEMENT: 8/8
TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8
TRACE_A_B_ATOMIZATION_BOUNDARY_MATCHES: 32/32

SOURCE_FACT_INVENTION: 0
ORDER_SENSITIVITY_ERRORS: 0
POST_REVEAL_RULE_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no

NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
```

The 32/32 atomization-boundary count covers four precommitted operational dimensions across eight cases:

```text
activation resolution
bridge obligation
optional-layer relevance/injection
source completeness for the locked task
```

## 7. Main finding / 핵심 결과

On the frozen constructed packet, the protocol produced the same Specification-specific final classifications and diagnostics under two different processing orders.

```text
same packet
+ same protocol
+ different processing order
-> same eight final status families
-> same eight diagnostic families
-> same 32 operational boundary classifications
```

This supports **procedural retraceability** and order stability for the locked finite packet.

It does not prove that two independent humans, two independently initialized models, or an external requirements-engineering team would necessarily reproduce the same atomization or verdicts.

## 8. Independence audit / 독립성 감사

```text
SAME_SESSION: yes
SAME_ASSISTANT_MODEL_FAMILY: yes
REFERENCE_KEY_PRECOMMITTED_AS_HASH: yes
TWO_PROCESSING_ORDERS: yes
EXTERNAL_REVIEWER: no
INDEPENDENT_MODEL_INSTANCE: no
BLIND_EXTERNAL_SCORING: no
```

Therefore:

```text
PROCEDURAL_RETRACE_REPRODUCIBILITY: supported_on_locked_constructed_packet
ORDER_INVARIANCE: supported_on_locked_two_order_retrace
INDEPENDENT_EVALUATOR_VALIDATION: not_established
EXTERNAL_REAL_WORLD_VALIDATION: not_established
```

This limitation is part of the result, not a post-hoc qualification.

## 9. Relation to prior Specification pilots / 기존 명세론 pilot과의 관계

```text
SPEC-CH-001
  basic well-formed / malformed discrimination

SPEC-CH-002
  contradiction / underspecification distinction

SPEC-CH-003
  optional-layer overconstraint / required-bridge deficiency boundary

SPEC-CH-004
  NO_GAIN / operational gain / genuine underspecification boundary

SPEC-CH-005
  retrace reproducibility and order stability of a frozen mixed packet
```

SPEC-CH-005 reuses the previously established output families but tests a different property: whether the protocol's classification can be retraced consistently from a frozen record.

## 10. Shared-core activation / 공통 코어 활성화

```text
SC-01 active: status distinction in R1
SC-02 active: frozen source/protocol/version packet
SC-03 active: bridge obligations in R1/R8
SC-04 active: optional-layer restraint in R4/R7
SC-07 active: method-specific + constructed-benchmark evidence classification
SC-08 active: precommit/hash lock and no post-reveal rescue

SC-05 inactive for the core scored claim
SC-06 inactive for the core scored claim
SC-09 inactive for the core scored claim
SC-10 inactive for the core scored claim
```

No new shared-core rule is proposed. Reproducibility remains a method/evidence maturity requirement whose concrete form varies by method.

## 11. Evidence status / 증거 상태

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DIRECT_PILOT_RECORDS_COMPLETED: 5
  SPEC-CH-001
  SPEC-CH-002
  SPEC-CH-003
  SPEC-CH-004
  SPEC-CH-005
INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed
MATURE_METHOD_STATUS: not_claimed
```

The internal constructed sequence is complete, but maturity is intentionally not promoted because the project promotion rule still requires at least one **external or independently generated application case**, and preferably a competent external baseline comparison where applicable.

## 12. Reproducibility record / 재현성 기록

```text
PROTOCOL_VERSION: Specification Protocol v0.1
PRECOMMIT_FILE: SPEC-CH-005_precommit.md
PRECOMMIT_COMMIT: dda33b2028c9e5fb0f7b3bef938a8b834219f787
BENCHMARK: RetraceSpecToy-v5
REQUIREMENT_PACKET: RT-SPEC-005-v1
CASE_COUNT: 8
TRACE_A_ORDER: R1 R2 R3 R4 R5 R6 R7 R8
TRACE_B_ORDER: R6 R2 R8 R1 R7 R3 R5 R4
REFERENCE_KEY_SHA256: 42dcc5398d60e26c1d7954cc794a7887fb4b03d28ca5c5aaea532564390cb945
MANUAL_JUDGMENT_POINTS:
  context sufficiency
  mutual exclusivity
  bridge obligation and typing
  optional-layer relevance
  operational completeness of baseline
  whether traceability gain introduces any new fact
POST_REVEAL_RULE_CHANGE: no
```

## 13. Limits / 한계

- constructed synthetic packet;
- same-session same assistant/model-family retrace;
- no independent reviewer or separately initialized evaluator;
- finite simple requirement atoms;
- no inter-rater agreement statistic;
- no real-world requirements corpus;
- no measured engineering cost/time/error reduction;
- the result establishes procedural retraceability only within the locked packet and protocol.

## 14. Next step / 다음 단계

The initial internal Specification challenge sequence is complete.

Next, use an **external or independently generated requirement corpus** as a real application record before any maturity promotion. The existing `SPEC-CH-001` through `SPEC-CH-005` records remain append-only.
