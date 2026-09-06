# SPEC-CH-003 Precommit — Optional-Layer / Bridge Boundary Challenge / 선택 층위·브리지 경계 도전 사전고정

Status: **precommitted before scoring**  
Date: 2026-09-06  
Method: **DSD Specification / DSD 명세론**  
Protocol: **DSD Specification Protocol v0.1**  
Case origin: `constructed_benchmark`

## 1. Locked purpose / 고정 목적

Test whether DSD Specification can distinguish two opposite specification failures without collapsing them into one generic error:

```text
OPTIONAL-LAYER OVERCONSTRAINT
  a claim-irrelevant optional DSD layer or specialization is made mandatory
  -> SPEC_OVERCONSTRAINED

REQUIRED-BRIDGE FAILURE
  a claim-relevant cross-carrier correspondence is used without a valid explicit/canonical bridge
  -> SPEC_UNDERSPECIFIED
```

The challenge also includes negative controls showing that:

1. omitted optional layers are not failures when the locked claim does not depend on them;
2. a bridge is not required when no cross-carrier meaning transfer occurs;
3. a correctly typed explicit bridge is sufficient without activating unrelated Static, Dynamics, or realized-axis interfaces.

## 2. Locked benchmark / 고정 벤치마크

Synthetic target: `BridgeBoundarySpecToy-v3`  
Locked requirement inventory: `BB-SPEC-003-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used unless a case explicitly perturbs it
DYNAMICS_LAYER: not used unless a case explicitly perturbs it
REALIZED_AXIS_SPECIALIZATION: not supplied unless a case explicitly perturbs it
EXTERNAL_DOMAIN: none
EXTERNAL_STANDARD: not applicable
```

Locked carriers and relations:

```text
C_src  source carrier
C_dst  target carrier
C_aux  unrelated auxiliary carrier

B_sd : C_src -> C_dst
  explicit allowed bridge for claim-relevant source-to-target transfer

B_aux : C_aux -> C_dst
  validly typed bridge, but wrong source carrier for the claim
```

Locked requirement set:

```text
R1 source token s exists on C_src
R2 property q(s) is read on C_src
R3 if a requirement transfers q(s) into a target statement on C_dst,
   the transfer must use explicit bridge B_sd or an explicitly supplied canonical equivalent
R4 no aggregate/readout requirement exists
R5 no temporal identity/transition/lineage requirement exists
R6 no axis/rank/normal/geometry requirement exists
```

Completeness is claimed only relative to `BB-SPEC-003-v1`.

## 3. Precommitted diagnostic families / 사전고정 진단군

```text
O1 OPTIONAL_STATIC_INJECTION
  Static Aggregation is made mandatory although R4 contains no aggregate/readout claim
  -> SPEC_OVERCONSTRAINED

O2 OPTIONAL_DYNAMICS_INJECTION
  Dynamics is made mandatory although R5 contains no temporal claim
  -> SPEC_OVERCONSTRAINED

O3 OPTIONAL_AXIS_INJECTION
  realized-axis/rank/normal data are made mandatory although R6 contains no geometry claim
  -> SPEC_OVERCONSTRAINED

B1 REQUIRED_BRIDGE_OMITTED
  C_src -> C_dst meaning transfer is used but no explicit/canonical bridge is supplied
  -> SPEC_UNDERSPECIFIED

B2 NAME_MATCH_AS_BRIDGE
  transfer is justified only because source/target fields share the same label/name
  -> SPEC_UNDERSPECIFIED

B3 WRONG_CARRIER_BRIDGE
  a bridge exists but its source/target typing does not match the claim-relevant transfer
  -> SPEC_UNDERSPECIFIED
```

## 4. Locked cases / 고정 사례

```text
WF-01  minimal valid cross-carrier specification
  R1-R3 active
  explicit B_sd supplied
  Static/Dynamics/axis omitted as not used/not supplied
  EXPECTED: usable

WF-02  no cross-carrier transfer
  R1-R2 only; q(s) remains on C_src
  no bridge supplied
  Static/Dynamics/axis omitted
  EXPECTED: usable

OL-01  force Static Aggregation as mandatory
  EXPECTED: SPEC_OVERCONSTRAINED / O1

OL-02  force Dynamics as mandatory
  EXPECTED: SPEC_OVERCONSTRAINED / O2

OL-03  force realized-axis/rank data as mandatory
  EXPECTED: SPEC_OVERCONSTRAINED / O3

BR-01  use C_src -> C_dst transfer but omit bridge
  EXPECTED: SPEC_UNDERSPECIFIED / B1

BR-02  use C_src -> C_dst transfer and claim bridge by shared field name only
  EXPECTED: SPEC_UNDERSPECIFIED / B2

BR-03  use C_src -> C_dst transfer but supply B_aux : C_aux -> C_dst
  EXPECTED: SPEC_UNDERSPECIFIED / B3
```

## 5. Locked scoring rule / 고정 채점규칙

```text
WELL_FORMED_CONTROLS: 2
OPTIONAL_LAYER_OVERCONSTRAINT_CASES: 3
REQUIRED_BRIDGE_FAILURE_CASES: 3

PASS_REQUIREMENT:
  accept well-formed controls 2/2
  classify optional-layer cases 3/3 as SPEC_OVERCONSTRAINED with exact O-family
  classify bridge cases 3/3 as SPEC_UNDERSPECIFIED with exact B-family
  exact diagnostic family match 8/8
  optional-layer / bridge cross-class errors = 0
  false bridge requirement when no cross-carrier transfer = 0
  false activation of Static/Dynamics/axis on WF cases = 0
  no post-reveal rule or exception change
```

## 6. Shared-core activation lock / 공통 코어 활성화 고정

```text
SC-02 active: source/interface lock
SC-03 active: bridge discipline
SC-04 active: required-vs-optional dependency discipline
SC-07 active: method_specific + constructed_benchmark evidence classification
SC-08 active: precommit and no post-reveal rescue

SC-01 inactive for the core scored distinction
SC-05 inactive for the core scored distinction
SC-06 inactive for the core scored distinction
SC-09 inactive for the core scored distinction
SC-10 inactive for the core scored distinction
```

## 7. Locked interpretation rule / 해석 규칙

```text
unnecessary dependency added
-> overconstraint

necessary cross-carrier mapping missing or invalidly typed
-> underspecification

optional layer absent and irrelevant
-> not a failure

bridge absent because no cross-carrier transfer exists
-> not a failure
```

This precommit is append-only. Any later modification requires a new challenge/version and cannot retroactively change the scoring of SPEC-CH-003.
