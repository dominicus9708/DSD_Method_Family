# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**.

Evidence does not transfer automatically between methods merely because the methods share a higher-level field or common DSD source layers.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED:
METHOD_VERSION_OR_PROTOCOL:
TASK:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
OPERATION:
OUTPUTS:
FAILURE_OR_NO_GAIN_CRITERIA:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## Current inheritance policy / 현재 상속 정책

- `challenges/ANL-CH-*` directly validate **DSD Analysis** challenge criteria only.
- `DSD_Audit/` and new audit records directly validate **DSD Audit** procedures and verdict discipline only.
- Shared-rule lessons may be cross-referenced under `../shared/`, but do not count as direct validation of another independent method.

## Method-specific evidence lanes / 개별 증거 경로

- [`specification/`](specification/) — **DSD Specification / DSD 명세론**
  - dedicated protocol v0.1 established;
  - current method status: `developing`;
  - `SPEC-CH-001` completed: well-formed/malformed discrimination pilot;
  - `SPEC-CH-002` completed: contradiction/underspecification pilot with precommit;
  - `SPEC-CH-003` completed: optional-layer/bridge boundary pilot with precommit;
  - `SPEC-CH-004` completed: NO_GAIN specification pilot with precommit;
  - `SPEC-CH-005` completed: reproducibility/retrace pilot with precommit + reference-key hash commitment;
  - current direct pilot count: `5`;
  - internal constructed challenge sequence: `completed`;
  - all five results are pilot PASS with limitations;
  - procedural retraceability and two-order stability: supported on the locked constructed packet;
  - independent evaluator validation: `not established`;
  - mature method status: not claimed;
  - next required evidence: `external_or_independently_generated_application_case`.

## Promotion expectation / 성숙도 승격 기준

A proposed or developing method should accumulate, at minimum:

1. a dedicated method protocol;
2. positive cases;
3. negative/failure cases;
4. boundary cases;
5. `NO_GAIN` cases;
6. reproducibility records;
7. at least one external or independently generated application case;
8. a strongest-reasonable-baseline comparison when applicable.

Shared evidence alone does not satisfy these method-specific requirements, and several constructed pilots alone are not enough for maturity promotion. Procedural same-session retrace does not substitute for a genuinely independent reviewer or external application corpus.