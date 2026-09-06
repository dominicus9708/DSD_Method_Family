# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **three direct pilot records completed / not mature**  
Date: 2026-09-06  
Method: **DSD Specification / DSD 명세론**  
Protocol: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)

This folder records evidence that directly tests the **Specification** method under its own task, inputs, operation, outputs, failure/no-gain criteria, and validation standard.

Shared-core pilots SC-01 through SC-10 may be reused as operating disciplines, but they do not count as direct Specification validation.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Specification
METHOD_VERSION_OR_PROTOCOL: Specification Protocol v0.1
CHALLENGE_ID:
TASK:
LOCKED_REQUIREMENT_INVENTORY:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
PRECOMMITTED_CRITERIA:
PERTURBATIONS_OR_CASES:
EXPECTED_SPEC_STATUS:
OBSERVED_SPEC_STATUS:
CONTRADICTIONS_FOUND:
UNDERSPECIFIED_ITEMS:
OVERCONSTRAINTS_FOUND:
NO_GAIN_STATUS:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## Direct evidence registry / 직접 증거 레지스트리

### SPEC-CH-001 — Well-Formed / Malformed Specification Discrimination

Record: [`SPEC-CH-001_well-formed-malformed-discrimination.md`](SPEC-CH-001_well-formed-malformed-discrimination.md)

```text
DATE: 2026-09-06
CASE_ORIGIN: constructed_benchmark
WELL_FORMED_CASES_ACCEPTED: 2/2
MALFORMED_CASES_DETECTED: 6/6
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
FALSE_POSITIVES_ON_INACTIVE_INTERFACES: 0
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
METHOD_MATURITY: not mature
```

This was the first direct method-specific pilot for DSD Specification. It supports only the locked discrimination task under Protocol v0.1 and does not establish general real-world validity.

### SPEC-CH-002 — Contradiction / Underspecification Challenge

Precommit: [`SPEC-CH-002_precommit.md`](SPEC-CH-002_precommit.md)  
Result: [`SPEC-CH-002_contradiction-underspecification.md`](SPEC-CH-002_contradiction-underspecification.md)

```text
DATE: 2026-09-06
CASE_ORIGIN: constructed_benchmark
PRECOMMIT_COMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
CONTRADICTION_CASES_CORRECTLY_CLASSIFIED: 3/3
UNDERSPECIFICATION_CASES_CORRECTLY_CLASSIFIED: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CONTRADICTION_UNDERSPECIFICATION_CROSS_CLASS_ERRORS: 0
FALSE_POSITIVES_ON_INACTIVE_INTERFACES: 0
POST_REVEAL_RULE_CHANGE: no
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
METHOD_MATURITY: not mature
```

This second pilot directly tests Specification's own distinction between impossible simultaneous requirements and missing decision information. It remains synthetic same-session evidence and is not independent blind validation.

### SPEC-CH-003 — Optional-Layer / Bridge Boundary Challenge

Precommit: [`SPEC-CH-003_precommit.md`](SPEC-CH-003_precommit.md)  
Result: [`SPEC-CH-003_optional-layer-bridge-boundary.md`](SPEC-CH-003_optional-layer-bridge-boundary.md)

```text
DATE: 2026-09-06
CASE_ORIGIN: constructed_benchmark
PRECOMMIT_COMMIT: d2cc07121043546be8e2450d8af288491b837e76
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
OPTIONAL_LAYER_OVERCONSTRAINT_CASES_CORRECT: 3/3
REQUIRED_BRIDGE_FAILURE_CASES_CORRECT: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
OPTIONAL_LAYER_BRIDGE_CROSS_CLASS_ERRORS: 0
FALSE_BRIDGE_REQUIREMENT_WITHOUT_CROSS_CARRIER_TRANSFER: 0
FALSE_ACTIVATION_OF_STATIC_DYNAMICS_AXIS_ON_WF_CASES: 0
POST_REVEAL_RULE_CHANGE: no
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
METHOD_MATURITY: not mature
```

This third pilot directly tests whether Specification distinguishes an unnecessary optional dependency (`SPEC_OVERCONSTRAINED`) from a missing or invalid claim-relevant mapping (`SPEC_UNDERSPECIFIED`). It does not create a new shared-core rule; it is a method-specific application of SC-03 and SC-04 under Specification's own output classes.

## Direct-evidence sequence

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination — completed, pilot pass with limitations
SPEC-CH-002  contradiction and underspecification challenge — completed, pilot pass with limitations
SPEC-CH-003  optional-layer and bridge boundary challenge — completed, pilot pass with limitations
SPEC-CH-004  NO_GAIN specification challenge — next
SPEC-CH-005  reproducibility / independent retrace challenge
```

After these internal challenges, add at least one external or independently generated application case before considering a maturity increase.

## Promotion restraint

Protocol preparation changed the method from `proposed` to `developing`. Completion of three synthetic pilots does not establish mature direct evidence.

```text
CURRENT_DIRECT_METHOD_EVIDENCE: three_pilots_completed
CURRENT_METHOD_STATUS: developing
MATURE_METHOD_STATUS: not_claimed
NEXT_DIRECT_TEST: SPEC-CH-004
```