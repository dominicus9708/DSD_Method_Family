# DSD Specification Method-Specific Evidence / DSD 명세론 개별 방법 직접 증거

Status: **evidence lane prepared / direct challenge corpus not yet accumulated**  
Date: 2026-09-06  
Method: **DSD Specification / DSD 명세론**  
Protocol: [`../../../methods/03_specification/PROTOCOL.md`](../../../methods/03_specification/PROTOCOL.md)

This folder is reserved for evidence that directly tests the **Specification** method under its own task, inputs, operation, outputs, failure/no-gain criteria, and validation standard.

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

## Initial direct-evidence sequence

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination
SPEC-CH-002  contradiction and underspecification challenge
SPEC-CH-003  optional-layer and bridge boundary challenge
SPEC-CH-004  NO_GAIN specification challenge
SPEC-CH-005  reproducibility / independent retrace challenge
```

After these internal challenges, add at least one external or independently generated application case before considering a maturity increase.

## Promotion restraint

Protocol preparation changes the method from `proposed` to `developing`, but does not establish mature direct evidence.

```text
CURRENT_DIRECT_METHOD_EVIDENCE: not_yet_established
CURRENT_METHOD_STATUS: developing
MATURE_METHOD_STATUS: not_claimed
```
