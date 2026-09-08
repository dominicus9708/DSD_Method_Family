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

- [`design/`](design/) — **DSD Design / DSD 설계론**
  - Protocol v0.1 established on `2026-09-08`;
  - current method evidence status: `validation_in_progress`;
  - direct constructed pilots: `6`;
  - positive cases: `1` (`DES-CH-001`, PASS);
  - negative/failure cases: `1` (`DES-CH-002`, PASS);
  - boundary cases under executable protocol: `2 attempted`;
  - successful boundary validations: `1` (`DES-CH-004`, PASS);
  - preserved boundary test-design failures: `1` (`DES-CH-003`, 20/21 with challenge-design defect; no protocol failure inferred);
  - `NO_GAIN` cases: `1` (`DES-CH-005`, PASS);
  - broader baseline-comparison cases: `1` (`DES-CH-006`, PASS with `NO_GAIN`);
  - external applications: `1` (`DES-APP-001`, PASS);
  - independent evaluator validation: `not established`;
  - `DES-CH-001` preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE`, returned `{T1,T2}`, and used no hidden Optimization;
  - `DES-CH-002` distinguished `DESIGN_INFEASIBLE`, `DESIGN_UNDERDETERMINED`, and `DESIGN_BLOCKED` with 20/20 checks passed;
  - `DES-CH-003` exposed a target-resolution test defect; the historical failed challenge was preserved without post-hoc repair;
  - `DES-CH-004` prospectively corrected the boundary test and passed 23/23 while keeping downstream Optimization separate;
  - `DES-CH-005` passed 25/25 with `DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN` against `B0_EXPLICIT_CONSTRAINT_MATRIX`;
  - `DES-CH-006` passed 54/54 against competent typed baseline `B1_TYPED_ADMISSIBILITY_TABLE`; B1 matched DSD on every frozen gain dimension, so `DESIGN_METHOD_GAIN_STATUS = NO_GAIN`;
  - strongest-reasonable-baseline comparison category is established at constructed-evidence level; this is not a superiority claim;
  - `DES-APP-001` used W3C WCAG 2.2 Recommendation 2024-12-12, limited to SC 1.4.3, 2.5.3, and 2.5.8, with a frozen W1-W10 candidate fixture; `{W1,W2,W3}` was the admissible family and all 36/36 checks passed;
  - `DES-APP-001` kept the external authority separate from the Design verdict, did not promote the SC 2.5.3 best-practice note into a hard requirement, did not invent a SC 2.5.8 exception, and did not overclaim full WCAG conformance;
  - external-application evidence category is now established at the single external-standard application level;
  - next required evidence: dedicated reproducibility/retrace test, followed by maturity audit; independent evaluator validation remains open.

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

Same-session or same-project retrace does not substitute for a genuinely independent reviewer. External corpus/application count also does not by itself establish independent replication.
