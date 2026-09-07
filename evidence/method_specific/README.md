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
- A maturity/status audit is an Audit meta-record and does not increase the audited method's direct-pilot count by itself.

## Method-specific evidence lanes / 개별 증거 경로

- [`specification/`](specification/) — **DSD Specification / DSD 명세론**
  - v0.1 and v0.2 historical evidence preserved;
  - Protocol v0.2.1 current for new runs after `SPEC-CH-007`;
  - current method status: `developing`;
  - `SPEC-CH-001~005`: v0.1 direct constructed pilots;
  - `SPEC-CH-006`: purpose/detail/viewpoint guardrail centerline challenge;
  - `SPEC-CH-007`: source-openness / downstream-determinacy axis challenge;
  - total direct constructed pilot count: `7`;
  - `SPEC-APP-001`: RFC 9112 §6.3 under v0.1, `SPEC_NO_GAIN`, baseline preferred;
  - `SPEC-APP-002`: Belmont Report Part C under v0.2, `MIXED_GAIN_WITH_GUARDRAIL_PRESSURE`;
  - `SPEC-APP-003`: OSHA Emergency Action Plan core corpus under v0.2.1, `SPEC_NO_GAIN` with `GUARDRAIL_PRESSURE`, baseline preferred;
  - external applications total: `3` across `3` external domains;
  - v0.2.1 external applications: `1`;
  - independent evaluator validation: `not established`;
  - first maturity audit predates `SPEC-APP-002`, `SPEC-CH-007`, and `SPEC-APP-003` and remains preserved;
  - current status remains `developing` until a new re-audit is explicitly performed.

### Current Specification-specific boundaries

Guardrail ledger:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Hard failure remains separate from guardrail pressure/recoverability/distortion.

v0.2.1 also separates:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

This prevents two opposite errors:

```text
intentional source openness -> falsely labeled accidental defect
missing required data -> falsely excused as discretion
```

`SPEC_UNDERSPECIFIED` remains relative to the declared downstream task. `SPEC-APP-003` additionally confirms on an external regulatory corpus that source-supported worksite implementation openness can be sufficient for a structural-review task without supplying the actual site-specific values.

Neither the guardrail profile nor the openness/determinacy axes are promoted to new shared-core IDs at this stage.

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

These eight categories are a minimum evidence architecture for promotion consideration, not an automatic promotion rule. Later method-specific blind spots may justify prospective protocol refinement without rewriting earlier evidence.

Same-session or same-project retrace does not substitute for a genuinely independent reviewer. With three external corpora now accumulated, the strongest remaining evidence gap for Specification is independent evaluation. If unavailable, the next internal step should be a maturity re-audit that explicitly discounts common-evaluator dependence rather than treating corpus count as independent replication.
