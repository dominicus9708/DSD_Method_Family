# SPEC-CH-002 — Contradiction / Underspecification Challenge / 모순·미명세 구별 도전

Status: **SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
Precommit: [`SPEC-CH-002_precommit.md`](SPEC-CH-002_precommit.md)  
Precommit commit: `848a01b160ecfe4fcbdb8e69d6501e40555d782d`

## 1. Purpose / 목적

This challenge tests whether DSD Specification distinguishes two different failure classes:

```text
SPEC_CONTRADICTION
  simultaneously active requirements admit no satisfying state

SPEC_UNDERSPECIFIED
  a required decision cannot be made because the locked source/task leaves
  activation, selection, threshold, type, bridge, or violation semantics unresolved
```

The case set and scoring rule were committed before scoring. No post-reveal exception or diagnostic-family change was introduced.

## 2. Locked benchmark / 고정 벤치마크

Synthetic target: `ContextGateSpecToy-v2`  
Locked source inventory: `CG-SPEC-002-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: none
```

The locked source distinguishes NORMAL and EMERGENCY contexts, uses explicit value/status requirements, and defines profile-dependent candidate bridges when cross-carrier transfer is invoked.

## 3. Case scoring / 사례 판정

### WF-01 — Context-separated apparent conflict

```text
NORMAL    -> gate_state = OPEN
EMERGENCY -> gate_state = CLOSED
```

Observed: `usable`.

Reason: the requirements are not simultaneously active. Different states in disjoint contexts do not constitute contradiction.

Diagnostic match: exact.

### WF-02 — Compatible numeric intersection

```text
ACTIVE -> level >= 3
ACTIVE -> level <= 5
```

Observed: `usable` with admissible interval `[3,5]`.

Reason: the intersection is nonempty, so both simultaneously active constraints can be satisfied.

Diagnostic match: exact.

### CT-01 — Same-context categorical collision

```text
NORMAL -> gate_state = OPEN
NORMAL -> gate_state = CLOSED
```

The locked toy state space makes OPEN and CLOSED mutually exclusive.

Observed: `SPEC_CONTRADICTION / C1 MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS`.

Reason: both requirements are simultaneously active over the same target/context and no admissible state satisfies both.

Diagnostic match: exact.

### CT-02 — Empty numeric intersection

```text
ACTIVE -> level >= 5
ACTIVE -> level <= 3
```

Observed: `SPEC_CONTRADICTION / C2 EMPTY_VALUE_INTERSECTION`.

Reason: the admissible set is empty because no numeric level can satisfy both constraints.

Diagnostic match: exact.

### CT-03 — Required/prohibited status collision

```text
ACTIVE -> q(signal) must be defined_zero
ACTIVE -> q(signal) must not be defined_zero
```

Observed: `SPEC_CONTRADICTION / C3 REQUIRED_PROHIBITED_STATUS_COLLISION`.

Reason: the same active context both requires and prohibits the same DSD Property status.

Diagnostic match: exact.

### US-01 — Activation scope omitted

```text
gate_state = OPEN
ACTIVATION_CONDITION: omitted
```

Observed: `SPEC_UNDERSPECIFIED / U1 ACTIVATION_SCOPE_UNRESOLVED`.

Reason: the locked source distinguishes NORMAL and EMERGENCY, and the specification does not determine where the requirement applies. There is not yet a contradictory pair; the activation scope is missing.

Diagnostic match: exact.

### US-02 — Bridge selector omitted

```text
C_in -> C_out
candidate bridges: B_direct, B_scaled
profile/selector: omitted
downstream values differ by bridge
```

Observed: `SPEC_UNDERSPECIFIED / U2 BRIDGE_SELECTION_UNRESOLVED`.

Reason: multiple admissible mappings remain and the downstream result is bridge-sensitive. The specification cannot choose one without inventing selector information.

Diagnostic match: exact.

### US-03 — HIGH threshold undefined

```text
alarm if level is HIGH
numeric downstream checker required
HIGH threshold/decision rule absent
```

Observed: `SPEC_UNDERSPECIFIED / U3 VIOLATION_THRESHOLD_UNDEFINED`.

Reason: the checker cannot determine SATISFIED versus VIOLATED without an explicit threshold or categorical rule. The missing rule is not itself a logical contradiction.

Diagnostic match: exact.

## 4. Score / 점수

```text
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
CONTRADICTION_CASES_CORRECTLY_CLASSIFIED: 3/3
UNDERSPECIFICATION_CASES_CORRECTLY_CLASSIFIED: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CONTRADICTION_UNDERSPECIFICATION_CROSS_CLASS_ERRORS: 0
FALSE_POSITIVES_ON_INACTIVE_INTERFACES: 0
POST_REVEAL_RULE_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
```

| Case | Expected | Observed | Match |
|---|---|---|---|
| WF-01 | usable | usable | yes |
| WF-02 | usable | usable `[3,5]` | yes |
| CT-01 | contradiction / C1 | contradiction / C1 | yes |
| CT-02 | contradiction / C2 | contradiction / C2 | yes |
| CT-03 | contradiction / C3 | contradiction / C3 | yes |
| US-01 | underspecified / U1 | underspecified / U1 | yes |
| US-02 | underspecified / U2 | underspecified / U2 | yes |
| US-03 | underspecified / U3 | underspecified / U3 | yes |

## 5. Main finding / 핵심 결과

The protocol did not collapse all malformed requirements into one generic failure bucket.

```text
same-context impossible conjunction
-> contradiction

missing context / selector / threshold needed to decide
-> underspecification

apparent conflict separated by context
-> usable

compatible constraints with nonempty intersection
-> usable
```

This distinction matters operationally because the remedies differ:

```text
SPEC_CONTRADICTION
  -> revise, prioritize, or explicitly preserve conflicting source requirements

SPEC_UNDERSPECIFIED
  -> acquire or declare the missing condition, selector, threshold, type, or rule
```

The challenge therefore supports the method-specific claim that Specification Protocol v0.1 can represent and distinguish these two failure classes on the locked constructed benchmark.

## 6. Shared-core activation / 공통 코어 활성화

```text
SC-01 active: status distinction in CT-03
SC-02 active: locked source/interface semantics
SC-03 active: bridge-sensitive US-02
SC-04 active: inactive Static/Dynamics/axis interfaces remain non-required
SC-07 active: evidence classified as method_specific + constructed_benchmark
SC-08 active: precommit before case scoring; no post-reveal rescue

SC-05 inactive for core claim
SC-06 inactive for core claim
SC-09 inactive for core claim
SC-10 inactive for core claim
```

Shared-core use supports operating discipline only; this record is direct evidence for **Specification** because the scored outputs are Specification-specific contradiction/underspecification verdicts under its own protocol.

## 7. Evidence status / 증거 상태

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DIRECT_PILOT_RECORDS_COMPLETED: 2
  SPEC-CH-001
  SPEC-CH-002
MATURE_METHOD_STATUS: not_claimed
```

Two successful synthetic pilots are not sufficient for maturity. Optional-layer/bridge stress, `NO_GAIN`, independent retrace, and external or independently generated requirement cases remain outstanding.

## 8. Reproducibility / 재현성

```text
PROTOCOL_VERSION: Specification Protocol v0.1
PRECOMMIT_FILE: SPEC-CH-002_precommit.md
PRECOMMIT_COMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
SOURCE_INVENTORY: CG-SPEC-002-v1
CASE_COUNT: 8
SCORING_RULE: exact family match + class counts
MANUAL_JUDGMENT_POINTS:
  context overlap/disjointness
  categorical mutual exclusivity
  numeric intersection emptiness
  bridge sensitivity
  threshold sufficiency
POST_REVEAL_RULE_CHANGE: no
```

Another reviewer can retrace each case directly from the locked requirements and diagnostic rules without executable code.

## 9. Limits / 한계

- constructed synthetic benchmark;
- same-session evaluation, though scoring criteria were separately committed before scoring;
- not independent blind validation;
- no real-world requirements corpus;
- only contradiction versus underspecification is tested here;
- does not yet test complicated multi-source priority rules or inconsistent authority hierarchies.

## 10. Next step / 다음 단계

Proceed to **SPEC-CH-003 — Optional-Layer / Bridge Boundary Challenge**.

The existing SPEC-CH-001 and SPEC-CH-002 records remain append-only.
