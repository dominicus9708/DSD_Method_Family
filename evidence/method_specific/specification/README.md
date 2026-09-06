# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **five direct pilot records completed / internal constructed sequence complete / not mature**  
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
WELL_FORMED_CASES_ACCEPTED: 2/2
MALFORMED_CASES_DETECTED: 6/6
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-002 — Contradiction / Underspecification Challenge

Precommit: [`SPEC-CH-002_precommit.md`](SPEC-CH-002_precommit.md)  
Result: [`SPEC-CH-002_contradiction-underspecification.md`](SPEC-CH-002_contradiction-underspecification.md)

```text
PRECOMMIT_COMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
CONTRADICTION_CASES_CORRECTLY_CLASSIFIED: 3/3
UNDERSPECIFICATION_CASES_CORRECTLY_CLASSIFIED: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CROSS_CLASS_ERRORS: 0
RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-003 — Optional-Layer / Bridge Boundary Challenge

Precommit: [`SPEC-CH-003_precommit.md`](SPEC-CH-003_precommit.md)  
Result: [`SPEC-CH-003_optional-layer-bridge-boundary.md`](SPEC-CH-003_optional-layer-bridge-boundary.md)

```text
PRECOMMIT_COMMIT: d2cc07121043546be8e2450d8af288491b837e76
WELL_FORMED_CONTROLS_ACCEPTED: 2/2
OPTIONAL_LAYER_OVERCONSTRAINT_CASES_CORRECT: 3/3
REQUIRED_BRIDGE_FAILURE_CASES_CORRECT: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CROSS_CLASS_ERRORS: 0
RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-004 — NO_GAIN Specification Challenge

Precommit: [`SPEC-CH-004_precommit.md`](SPEC-CH-004_precommit.md)  
Result: [`SPEC-CH-004_no-gain-specification.md`](SPEC-CH-004_no-gain-specification.md)

```text
PRECOMMIT_COMMIT: 4d55d00af7fa376d370415a48b82de6883ba6fc8
NO_GAIN_CASES_CORRECTLY_PRESERVED: 3/3
OPERATIONAL_GAIN_CASES_CORRECTLY_DISTINGUISHED: 3/3
UNDERSPECIFIED_CASES_CORRECTLY_DISTINGUISHED: 2/2
EXACT_EXPECTED_FINAL_STATUS_FAMILY: 8/8
FALSE_NO_GAIN_ON_INCOMPLETE_SOURCE: 0
FALSE_GAIN_FROM_COSMETIC_RELABELING_OR_REORDERING: 0
INVENTED_SOURCE_FACTS: 0
RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-005 — Reproducibility / Independent Retrace Challenge

Precommit: [`SPEC-CH-005_precommit.md`](SPEC-CH-005_precommit.md)  
Result: [`SPEC-CH-005_reproducibility-independent-retrace.md`](SPEC-CH-005_reproducibility-independent-retrace.md)

```text
PRECOMMIT_COMMIT: dda33b2028c9e5fb0f7b3bef938a8b834219f787
REFERENCE_KEY_HASH_MATCH: yes
TRACE_A_FINAL_STATUS_MATCHES: 8/8
TRACE_B_FINAL_STATUS_MATCHES: 8/8
TRACE_A_B_FINAL_STATUS_AGREEMENT: 8/8
TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8
TRACE_A_B_ATOMIZATION_BOUNDARY_MATCHES: 32/32
SOURCE_FACT_INVENTION: 0
ORDER_SENSITIVITY_ERRORS: 0
RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

This fifth pilot supports procedural retraceability and order stability on a frozen constructed packet. It does **not** count as an independent external review because both retraces were performed in the same project session by the same assistant/model family.

## Direct-evidence sequence

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination — completed
SPEC-CH-002  contradiction and underspecification challenge — completed
SPEC-CH-003  optional-layer and bridge boundary challenge — completed
SPEC-CH-004  NO_GAIN specification challenge — completed
SPEC-CH-005  reproducibility / independent retrace challenge — completed with independence limitation
```

The initial internal constructed challenge sequence is now complete.

## Promotion restraint / 승격 절제

```text
CURRENT_DIRECT_METHOD_EVIDENCE: five_pilots_completed
INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed
CURRENT_METHOD_STATUS: developing
MATURE_METHOD_STATUS: not_claimed
NEXT_REQUIRED_EVIDENCE: external_or_independently_generated_application_case
```

Completion of five constructed pilots does not establish mature direct validity. Before maturity promotion, add at least one external or independently generated requirement corpus, preserve the applicable external baseline/standard, and preferably obtain genuinely independent retrace or review evidence.
