# SPEC-CH-003 — Optional-Layer / Bridge Boundary Challenge / 선택 층위·브리지 경계 도전

Status: **SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
Precommit: [`SPEC-CH-003_precommit.md`](SPEC-CH-003_precommit.md)  
Precommit commit: `d2cc07121043546be8e2450d8af288491b837e76`

## 1. Purpose / 목적

This challenge tests whether DSD Specification distinguishes two opposite specification failures:

```text
SPEC_OVERCONSTRAINED
  claim-irrelevant optional structure is made mandatory

SPEC_UNDERSPECIFIED
  claim-relevant cross-carrier mapping is missing, merely inferred, or wrongly typed
```

The case set, diagnostics, and scoring rule were committed before scoring. No post-reveal rule or exception was introduced.

## 2. Locked benchmark / 고정 벤치마크

Synthetic target: `BridgeBoundarySpecToy-v3`  
Locked requirement inventory: `BB-SPEC-003-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: inactive for the locked core requirements
DYNAMICS_LAYER: inactive for the locked core requirements
REALIZED_AXIS_SPECIALIZATION: inactive for the locked core requirements
EXTERNAL_DOMAIN: none
```

Locked carrier structure:

```text
C_src  source carrier
C_dst  target carrier
C_aux  unrelated auxiliary carrier

B_sd  : C_src -> C_dst
B_aux : C_aux -> C_dst
```

`B_sd` is the declared claim-relevant bridge. `B_aux` is a validly typed map for a different source carrier and therefore cannot satisfy a `C_src -> C_dst` transfer obligation.

## 3. Case scoring / 사례 판정

### WF-01 — Minimal valid cross-carrier specification

```text
source: C_src
target: C_dst
claim-relevant transfer: yes
bridge: explicit B_sd
Static: not used
Dynamics: not used
realized axis: not supplied
```

Expected: `usable`.

Observed: `usable`.

Reason: the only claim-relevant cross-carrier transfer is explicitly bridged, while irrelevant optional interfaces remain inactive.

Diagnostic match: exact.

### WF-02 — No cross-carrier transfer, therefore no bridge obligation

```text
q(s) remains on C_src
cross-carrier transfer: no
bridge: not supplied
Static/Dynamics/axis: inactive
```

Expected: `usable`.

Observed: `usable`.

Reason: bridge discipline is conditional on an actual cross-carrier correspondence claim. The protocol does not require an unused bridge merely because multiple carriers exist in the benchmark vocabulary.

Diagnostic match: exact.

This is the principal negative control against bridge over-requirement.

### OL-01 — Irrelevant Static Aggregation made mandatory

Perturbation:

```text
STATIC_AGGREGATION_LAYER: required
aggregate/readout requirement in BB-SPEC-003-v1: none
```

Expected: `SPEC_OVERCONSTRAINED / O1 OPTIONAL_STATIC_INJECTION`.

Observed: exact match.

Reason: the imposed layer is stronger than the locked requirement inventory and supplies no claim-relevant obligation.

### OL-02 — Irrelevant Dynamics made mandatory

Perturbation:

```text
DYNAMICS_LAYER: required
temporal identity/transition/lineage requirement: none
```

Expected: `SPEC_OVERCONSTRAINED / O2 OPTIONAL_DYNAMICS_INJECTION`.

Observed: exact match.

Reason: the benchmark has no evolution or lineage claim whose specification depends on Dynamics.

### OL-03 — Irrelevant realized-axis specialization made mandatory

Perturbation:

```text
REALIZED_AXIS_SPECIALIZATION: required
rank/normal/geometry data: mandatory
geometry requirement in locked inventory: none
```

Expected: `SPEC_OVERCONSTRAINED / O3 OPTIONAL_AXIS_INJECTION`.

Observed: exact match.

Reason: claim-irrelevant specialization has been converted into a hidden prerequisite.

### BR-01 — Required bridge omitted

Perturbation:

```text
claim transfer: C_src -> C_dst
bridge: omitted
```

Expected: `SPEC_UNDERSPECIFIED / B1 REQUIRED_BRIDGE_OMITTED`.

Observed: exact match.

Reason: the downstream target statement depends on a cross-carrier correspondence that the record does not define.

### BR-02 — Shared label used as bridge evidence

Perturbation:

```text
source field name: signal
target field name: signal
claim transfer: C_src -> C_dst
explicit/canonical bridge: none
justification: same label
```

Expected: `SPEC_UNDERSPECIFIED / B2 NAME_MATCH_AS_BRIDGE`.

Observed: exact match.

Reason: shared naming does not determine a map, selection rule, preserved structure, or loss boundary.

### BR-03 — Wrong-carrier bridge supplied

Perturbation:

```text
required transfer: C_src -> C_dst
supplied bridge: B_aux : C_aux -> C_dst
```

Expected: `SPEC_UNDERSPECIFIED / B3 WRONG_CARRIER_BRIDGE`.

Observed: exact match.

Reason: bridge existence alone is insufficient; source and target typing must match the claim-relevant correspondence.

## 4. Score / 점수

```text
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
OPTIONAL_LAYER_OVERCONSTRAINT_CASES_CORRECT: 3/3
REQUIRED_BRIDGE_FAILURE_CASES_CORRECT: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
OPTIONAL_LAYER_BRIDGE_CROSS_CLASS_ERRORS: 0
FALSE_BRIDGE_REQUIREMENT_WITHOUT_CROSS_CARRIER_TRANSFER: 0
FALSE_ACTIVATION_OF_STATIC_DYNAMICS_AXIS_ON_WF_CASES: 0
POST_REVEAL_RULE_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
```

| Case | Expected | Observed | Match |
|---|---|---|---|
| WF-01 | usable | usable | yes |
| WF-02 | usable | usable | yes |
| OL-01 | overconstrained / O1 | overconstrained / O1 | yes |
| OL-02 | overconstrained / O2 | overconstrained / O2 | yes |
| OL-03 | overconstrained / O3 | overconstrained / O3 | yes |
| BR-01 | underspecified / B1 | underspecified / B1 | yes |
| BR-02 | underspecified / B2 | underspecified / B2 | yes |
| BR-03 | underspecified / B3 | underspecified / B3 | yes |

## 5. Main finding / 핵심 결과

The protocol preserved the direction of the error:

```text
adding a dependency the claim does not need
-> SPEC_OVERCONSTRAINED

failing to supply a mapping the claim does need
-> SPEC_UNDERSPECIFIED
```

It also avoided the two symmetric false positives:

```text
optional interface absent but irrelevant
-> usable

bridge absent because no cross-carrier transfer is claimed
-> usable
```

Therefore the protocol did not reduce good specification practice to either "include every possible DSD layer" or "always require a bridge whenever more than one carrier is mentioned."

## 6. Relation to the shared core / 공통 코어와의 관계

```text
SC-03
  supplies the shared bridge discipline

SC-04
  supplies required-vs-optional dependency discipline

SPEC-CH-003
  directly tests whether Specification Protocol v0.1 turns those disciplines
  into Specification-specific output classes:
  SPEC_UNDERSPECIFIED versus SPEC_OVERCONSTRAINED
```

This distinction is why the record is method-specific direct evidence rather than a new shared-core candidate.

## 7. Shared-core activation / 공통 코어 활성화

```text
SC-02 active: source/interface lock
SC-03 active: explicit and typed bridge obligation
SC-04 active: optional-layer restraint
SC-07 active: evidence scope/case-origin classification
SC-08 active: precommit and no post-reveal rescue

SC-01 inactive for the core scored distinction
SC-05 inactive for the core scored distinction
SC-06 inactive for the core scored distinction
SC-09 inactive for the core scored distinction
SC-10 inactive for the core scored distinction
```

## 8. Evidence status / 증거 상태

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DIRECT_PILOT_RECORDS_COMPLETED: 3
  SPEC-CH-001
  SPEC-CH-002
  SPEC-CH-003
MATURE_METHOD_STATUS: not_claimed
```

Three successful constructed pilots still do not establish mature direct method validity.

## 9. Reproducibility / 재현성

```text
PROTOCOL_VERSION: Specification Protocol v0.1
PRECOMMIT_FILE: SPEC-CH-003_precommit.md
PRECOMMIT_COMMIT: d2cc07121043546be8e2450d8af288491b837e76
SOURCE_INVENTORY: BB-SPEC-003-v1
CASE_COUNT: 8
SCORING_RULE: exact family match + class counts + cross-class error count
MANUAL_JUDGMENT_POINTS:
  whether a claim actually crosses carriers
  whether an optional layer contributes to a locked requirement
  bridge source/target typing
  whether a bridge is explicit/canonical versus inferred from labels
POST_REVEAL_RULE_CHANGE: no
```

No executable code is required because all cases are finite declarative specification records whose verdicts can be retraced from the locked inventory and protocol.

## 10. Limits / 한계

- constructed synthetic benchmark;
- same-session evaluation with separately committed precommit;
- not independent blind validation;
- no real-world requirement corpus;
- bridge cases are finite and deliberately simple;
- does not test aggregate/reconstruction bridges, dynamic constitutive bridges, or external-domain bridges;
- does not yet establish comparative benefit over competent non-DSD requirements engineering.

## 11. Next step / 다음 단계

Proceed to **SPEC-CH-004 — NO_GAIN Specification Challenge**.

The existing SPEC-CH-001 through SPEC-CH-003 records remain append-only.
