# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**.

Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

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
- A maturity/status audit of a method is an Audit meta-record; it does not increase that method's direct-pilot count by itself.

## Method-specific evidence lanes / 개별 증거 경로

- [`specification/`](specification/) — **DSD Specification / DSD 명세론**
  - v0.1 historical protocol retained;
  - prospective Protocol v0.2 established for new runs after `SPEC-CH-006`;
  - current method status: `developing`;
  - `SPEC-CH-001~005`: v0.1 direct constructed pilots;
  - `SPEC-CH-006`: purpose/detail/viewpoint guardrail centerline challenge;
  - current total direct constructed pilot count: `6`;
  - first external/independently generated corpus application `SPEC-APP-001`: completed under v0.1;
  - external application result: `SPEC_NO_GAIN`, `BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK`;
  - external source-fidelity result: pass on the locked RFC 9112 §6.3 corpus;
  - v0.2 external applications: `0`;
  - independent evaluator validation: `not established`;
  - first Specification maturity audit: completed;
  - promotion to `established`: `INSUFFICIENT_BASIS`;
  - current `developing` status: confirmed;
  - next direct application: `SPEC-APP-002` on a less-structured external corpus under v0.2.

### Specification guardrail distinction

The current v0.2 method-specific guardrails are:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

They are centerline controls, not automatic discard conditions.

```text
HARD_FAILURE
!= GUARDRAIL_PRESSURE
!= GUARDRAIL_EXCEEDED_RECOVERABLE
!= PURPOSE_OR_VIEWPOINT_DISTORTED
```

The guardrail profile is **not** promoted to a new shared-core rule at this stage.

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

These eight categories are a minimum evidence architecture for promotion consideration, not an automatic promotion rule. If later use exposes a stable method-specific blind spot — such as purpose/viewpoint distortion in Specification — the protocol may be prospectively revised without rewriting earlier evidence.

Shared evidence alone does not satisfy method-specific promotion requirements. Procedural same-session retrace does not substitute for a genuinely independent reviewer, and external corpus origin does not substitute for independent evaluation.
