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
  - Protocol v0.2 current for new runs after `SPEC-CH-006`;
  - current method status: `developing`;
  - `SPEC-CH-001~005`: v0.1 direct constructed pilots;
  - `SPEC-CH-006`: purpose/detail/viewpoint guardrail centerline challenge;
  - current total direct constructed pilot count: `6`;
  - `SPEC-APP-001`: RFC 9112 §6.3 under v0.1, `SPEC_NO_GAIN`, baseline preferred;
  - `SPEC-APP-002`: Belmont Report Part C under v0.2, `MIXED_GAIN_WITH_GUARDRAIL_PRESSURE`;
  - external applications total: `2`;
  - external domains total: `2`;
  - v0.2 external applications: `1`;
  - latest source-fidelity result: 22/22 locked Belmont source units preserved, hard failures 0;
  - latest guardrail result: `GUARDRAIL_PRESSURE`, primarily from representation/detail burden;
  - independent evaluator validation: `not established`;
  - first Specification maturity audit: completed before `SPEC-APP-002`;
  - promotion to `established` in that audit: `INSUFFICIENT_BASIS`;
  - current status remains `developing` until a new re-audit is performed;
  - next strongest evidence: independent retrace or intentional-open-texture boundary challenge.

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

`SPEC-APP-002` adds another method-specific pressure distinction that is not yet promoted into the protocol as a dedicated status:

```text
source-intentional normative openness
!= accidental specification underspecification
```

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

These eight categories are a minimum evidence architecture for promotion consideration, not an automatic promotion rule. If later use exposes a stable method-specific blind spot — such as purpose/viewpoint distortion or intentional open-texture handling in Specification — the protocol may be prospectively revised without rewriting earlier evidence.

Shared evidence alone does not satisfy method-specific promotion requirements. Procedural same-session retrace does not substitute for a genuinely independent reviewer, and external corpus origin does not substitute for independent evaluation.
