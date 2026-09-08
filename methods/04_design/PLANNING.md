# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / validation in progress**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Current protocol / 현재 프로토콜

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- pre-protocol basis: `TASK_INTERFACE_v0.1-draft.md`, `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`, `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`.

## Current task interface / 현재 과업 인터페이스

```text
GOALS
+ HARD_CONSTRAINTS
+ CONSTRAINT_SOURCE_OR_SPECIFICATION
+ BASE_STRUCTURE_OR_PREDECESSOR
+ TARGET_DSD_LAYER_SCOPE
+ TARGET_RESOLUTION
+ CANDIDATE_OR_CONSTRUCTION_BASIS
+ CANDIDATE_GENERATION_RULE
+ CANDIDATE_COVERAGE
+ selected DSD interface
+ explicit DOMAIN_BRIDGE when required
+ EXTERNAL_STANDARD when an external-domain claim is made
+ AUXILIARY_METHODS_OR_HANDOFFS when materially used
-> candidate design family
-> status-sensitive admissibility evaluation
-> admissible target family OR terminal non-success result
```

Design does not assume a universal candidate generator and does not fabricate missing domain design knowledge.

## Three independent ledgers / 3중 장부

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE
  DESIGN_INFEASIBLE
  DESIGN_UNDERDETERMINED
  DESIGN_BLOCKED

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

## Core guardrails / 핵심 보호 규칙

### Candidate coverage

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` requires exhaustive coverage with all relevant candidates rejected or an explicit impossibility argument. Non-exhaustive failure-to-find is not global infeasibility.

### Constraint provenance

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

Design does not silently promote soft preference to hard constraint after candidate inspection.

### Output level and target resolution

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

Material target distinctness is judged at `TARGET_RESOLUTION`; candidate IDs or downstream-only metadata are insufficient.

### Neighboring-method boundary

- Specification locks or exposes requirements and scope upstream when used.
- Design constructs/filters admissible target structures under goals and hard constraints.
- Synthesis combines admitted parts.
- Transformation records source-target preservation/loss.
- Optimization selects among already-admissible alternatives under an objective.
- Audit retraces a completed Design execution.

### External-source boundary

An external standard may supply hard requirements or applicability conditions through an explicit bridge, but DSD Design must keep:

```text
external authority
!= DSD method verdict

source requirement
!= task-local fixture assumption

best-practice note
!= hard criterion unless the source makes it normative

subset application
!= full-standard conformance claim
```

No source clause or exception is revised post hoc to rescue or reject a candidate.

## Evidence sequence / 증거 진행

### `DES-CH-001` — positive

```text
{T1,T2} -> DESIGN_ADMISSIBLE
11/11 PASS
```

Preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE`.

### `DES-CH-002` — negative/failure

```text
exhaustive no-solution -> DESIGN_INFEASIBLE
non_exhaustive failure-to-find -> DESIGN_UNDERDETERMINED
missing predecessor -> DESIGN_BLOCKED
20/20 PASS
```

### `DES-CH-003` — failed boundary test design

```text
20/21
FAIL_AS_PRECOMMITTED_CHALLENGE
CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

Preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
23/23 PASS
```

### `DES-CH-005` — NO_GAIN

```text
Baseline: B0_EXPLICIT_CONSTRAINT_MATRIX
DSD == B0 on frozen claim-relevant result
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
25/25 PASS
```

### `DES-CH-006` — broader strongest-reasonable baseline

```text
Baseline: B1_TYPED_ADMISSIBILITY_TABLE
Formation + General Property
15 candidates
DESIGN_SPACE + UNIQUE_TARGET
B1 == DSD on all frozen gain dimensions
G1-G5: NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
54/54 PASS
```

This establishes the `baseline_comparison` category at constructed-evidence level, not DSD superiority.

### `DES-APP-001` — first external-standard application

External source:

```text
W3C WCAG 2.2 Recommendation 2024-12-12
SC 1.4.3 Contrast (Minimum)
SC 2.5.3 Label in Name
SC 2.5.8 Target Size (Minimum)
```

Candidate fixture:

```text
W1-W10
Formation + General Property
DOMAIN_BRIDGE: WCAG_APPLICATION_BRIDGE_001
```

Result:

```text
ADMISSIBLE_FAMILY: {W1,W2,W3}
W4 -> H1 target size
W5 -> H1 target size
W6 -> H2 label in name
W7 -> H2 with APPLICABLE_BUT_UNDEFINED name
W8 -> H3 contrast
W9 -> H1,H2,H3
W10 -> H0 CHANNEL_ABSENCE

TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
36/36 PASS
```

The application did not promote the WCAG best-practice note about label position into a hard requirement, did not invent a target-size exception, and did not claim full WCAG conformance from the three-criterion subset.

## DSD layer policy / DSD 층위 정책

1. **Formation** — active for new structural targets, or explicitly locked as inherited Stage-VI predecessor for downstream design.
2. **General Property** — active only when typed property declaration, applicability, prerequisites, or partial assignment matter.
3. **Static Aggregation** — active only when a declared analytic readout/aggregate is needed.
4. **Dynamics** — active only when trajectory, transition, lineage, propagation, or other time dependence matters.
5. **Optional specialization** — active only through explicit supplied specialization/domain data.

No bridge is inferred from a name, intuition, or shared vocabulary alone.

## Development sequence / 개발 순서

1. ✅ Design-specific task interface and minimum valid output.
2. ✅ Boundary counterexamples and non-breaking refinements.
3. ✅ `PROTOCOL_v0.1.md`.
4. ✅ Positive pilot `DES-CH-001`.
5. ✅ Negative/failure pilot `DES-CH-002`.
6. ✅ Boundary stage: failed `DES-CH-003` preserved; corrected `DES-CH-004` PASS.
7. ✅ NO_GAIN pilot `DES-CH-005`.
8. ✅ Broader strongest-reasonable-baseline comparison `DES-CH-006` PASS / `NO_GAIN`.
9. ✅ First external-standard application `DES-APP-001` PASS.
10. **Next:** dedicated reproducibility/retrace test.
11. DSD Audit maturity review.

## Evidence architecture status / 증거 구조 상태

```text
DEDICATED_PROTOCOL: established
POSITIVE_CASE: established
NEGATIVE_OR_FAILURE_CASE: established
BOUNDARY_CASE: established with one preserved failed predecessor test
NO_GAIN_CASE: established
STRONGEST_REASONABLE_BASELINE_COMPARISON: established at constructed level
EXTERNAL_OR_INDEPENDENT_APPLICATION: established at single external-standard application level
REPRODUCIBILITY_RECORD: case-level records exist; dedicated retrace stage not completed
INDEPENDENT_EVALUATOR_VALIDATION: not established
MATURITY_AUDIT: not performed
```

Current evidence counts:

```text
DIRECT_CONSTRUCTED_PILOTS: 6
EXTERNAL_APPLICATIONS: 1
EXTERNAL_APPLICATION_PASSES: 1
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time. Corrected future tests do not rewrite earlier runs.

## Next step / 다음 단계

Precommit and run a dedicated **reproducibility/retrace Design test**.

The test should freeze an existing completed Design evidence record, reconstruct its declared inputs from the stored record only, and require a clean re-execution to reproduce candidate verdicts, terminal status, protocol conformance, source/bridge version, and method-gain status where applicable without editing the original case.
