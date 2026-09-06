# SPEC-CH-002 Precommit — Contradiction / Underspecification Challenge

Status: **locked before case scoring**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
DSD interface profile date: **2026-09-05**

## 1. Purpose / 목적

Test whether DSD Specification can distinguish **contradiction** from **underspecification** rather than collapsing both into one generic failure state.

The locked distinction is:

```text
SPEC_CONTRADICTION
  = two or more requirements are simultaneously active over the same relevant target/context
    and no admissible state can satisfy them all.

SPEC_UNDERSPECIFIED
  = the locked source/task does not determine a type, context, selector, threshold,
    bridge, or violation condition needed for the declared downstream checker.
```

No scoring rule may be changed after the cases are evaluated. Any later revision must be recorded as a new protocol/challenge version.

## 2. Locked benchmark / 고정 벤치마크

Synthetic target: `ContextGateSpecToy-v2`  
Locked source inventory: `CG-SPEC-002-v1`

```text
SELECTED_DSD_LAYERS:
  FORMATION_LAYER: used
  PROPERTY_CORE: used
  STATIC_AGGREGATION_LAYER: not used
  DYNAMICS_LAYER: not used
  REALIZED_AXIS_SPECIALIZATION: not supplied

EXTERNAL_DOMAIN: none
EXTERNAL_STANDARD: not applicable
```

Base source requirements:

```text
R1 CONTEXTUAL STATE
  context NORMAL -> gate_state = OPEN

R2 CONTEXTUAL STATE
  context EMERGENCY -> gate_state = CLOSED

R3 VALUE WINDOW
  when a numeric level constraint is supplied, the admissible interval is the
  intersection of all simultaneously active lower/upper bounds.

R4 PROPERTY STATUS
  in ACTIVE context, q(signal) may be constrained by an explicit required status
  and/or explicit prohibited statuses.

R5 CROSS-CARRIER BRIDGE
  C_in -> C_out transfer uses:
    profile P1 -> B_direct
    profile P2 -> B_scaled
  If the downstream result differs between the bridges, the profile/selector must be known.

R6 THRESHOLD VERDICT
  if the downstream checker must decide whether level is HIGH, a threshold or
  categorical decision rule must be supplied by the locked source/task.
```

Completeness claims are relative only to `CG-SPEC-002-v1`.

## 3. Locked diagnostic families / 고정 진단군

```text
C1 MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS
   same active context requires mutually exclusive categorical states
   -> SPEC_CONTRADICTION

C2 EMPTY_VALUE_INTERSECTION
   simultaneously active numeric constraints have empty intersection
   -> SPEC_CONTRADICTION

C3 REQUIRED_PROHIBITED_STATUS_COLLISION
   same active context both requires and prohibits the same status
   -> SPEC_CONTRADICTION

U1 ACTIVATION_SCOPE_UNRESOLVED
   a context-sensitive requirement has no determinable activation scope
   -> SPEC_UNDERSPECIFIED

U2 BRIDGE_SELECTION_UNRESOLVED
   multiple admissible bridges yield different downstream results and no selector/profile is determined
   -> SPEC_UNDERSPECIFIED

U3 VIOLATION_THRESHOLD_UNDEFINED
   downstream verdict requires a threshold/decision rule absent from the locked source/task
   -> SPEC_UNDERSPECIFIED
```

## 4. Locked cases / 고정 사례

### WF-01 — Context-separated apparent conflict

```text
NORMAL    -> gate_state = OPEN
EMERGENCY -> gate_state = CLOSED
```

Expected: `usable`, no contradiction.

### WF-02 — Compatible numeric intersection

```text
ACTIVE -> level >= 3
ACTIVE -> level <= 5
```

Expected: `usable`, admissible interval `[3,5]`.

### CT-01 — Same-context categorical collision

```text
NORMAL -> gate_state = OPEN
NORMAL -> gate_state = CLOSED
OPEN and CLOSED are mutually exclusive in the locked toy state space.
```

Expected: `SPEC_CONTRADICTION / C1`.

### CT-02 — Empty numeric intersection

```text
ACTIVE -> level >= 5
ACTIVE -> level <= 3
```

Expected: `SPEC_CONTRADICTION / C2`.

### CT-03 — Required/prohibited status collision

```text
ACTIVE -> q(signal) must be defined_zero
ACTIVE -> q(signal) must not be defined_zero
```

Expected: `SPEC_CONTRADICTION / C3`.

### US-01 — Activation scope omitted

```text
gate_state = OPEN
ACTIVATION_CONDITION: omitted
```

The locked source distinguishes NORMAL from EMERGENCY.

Expected: `SPEC_UNDERSPECIFIED / U1`.

### US-02 — Bridge selector omitted

```text
source carrier: C_in
target carrier: C_out
candidate bridges: B_direct, B_scaled
profile/selector: omitted
downstream values differ by bridge
```

Expected: `SPEC_UNDERSPECIFIED / U2`.

### US-03 — HIGH threshold undefined

```text
alarm if level is HIGH
numeric downstream checker required
HIGH threshold/decision rule: absent from locked source/task
```

Expected: `SPEC_UNDERSPECIFIED / U3`.

## 5. Precommitted scoring / 사전 고정 점수

```text
WELL_FORMED_CONTROLS: 2
CONTRADICTION_CASES: 3
UNDERSPECIFICATION_CASES: 3

PASS_REQUIREMENT:
  well-formed controls accepted: 2/2
  contradiction cases classified as contradiction: 3/3
  underspecification cases classified as underspecified: 3/3
  exact diagnostic family matches: 8/8
  contradiction <-> underspecification cross-class errors: 0
  false requirement for inactive Static/Dynamics/axis interfaces: 0
```

## 6. Activated shared rules / 활성 공통 규율

Core-relevant for this challenge:

```text
SC-01 status/type distinction
SC-02 source/interface lock
SC-03 bridge explicitness
SC-04 optional-interface restraint
SC-07 evidence scope separation
SC-08 locked criteria / anti-post-hoc
```

SC-05, SC-06, SC-09, and SC-10 are not required for the core scoring claim.

## 7. Evidence limit / 증거 한계

This is a constructed same-session challenge. A PASS, if obtained, is pilot-level direct evidence for Specification Protocol v0.1 only. It is not independent blind validation, real-world validation, or mature method validation.
