# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **direct pilot evidence started / not mature**  
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

This is the first direct method-specific pilot for DSD Specification. It supports only the locked discrimination task under Protocol v0.1 and does not establish general real-world validity.

## Direct-evidence sequence

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination — completed, pilot pass with limitations
SPEC-CH-002  contradiction and underspecification challenge — next
SPEC-CH-003  optional-layer and bridge boundary challenge
SPEC-CH-004  NO_GAIN specification challenge
SPEC-CH-005  reproducibility / independent retrace challenge
```

After these internal challenges, add at least one external or independently generated application case before considering a maturity increase.

## Promotion restraint

Protocol preparation changed the method from `proposed` to `developing`. Completion of one synthetic pilot does not establish mature direct evidence.

```text
CURRENT_DIRECT_METHOD_EVIDENCE: pilot_started
CURRENT_METHOD_STATUS: developing
MATURE_METHOD_STATUS: not_claimed
NEXT_DIRECT_TEST: SPEC-CH-002
```