# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / validation in progress**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints, while preserving the current 22-method boundary discipline.

The method is not treated as mature merely because related DSD methods already have evidence. Shared-core evidence and neighboring-method results may be referenced, but direct Design validation must be accumulated separately.

## Current protocol / 현재 프로토콜

The first executable protocol is established:

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)

Its pre-protocol basis is preserved in:

- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)

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

Design does not assume a universal candidate generator. Domain-specific candidate or construction resources must be supplied explicitly enough to reproduce the space actually used.

## Current terminal-status ledger / 현재 종결 상태 장부

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

Method gain remains separate:

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Protocol conformance is a third independent ledger:

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

## Candidate-coverage guard / 후보 범위 보호 규칙

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` requires either exhaustive candidate coverage with all required candidates rejected or an explicit impossibility argument. Failure to find a candidate in a non-exhaustive search is not enough for a global infeasibility claim.

`DES-CH-002` directly exercises both sides of this rule:

```text
exhaustive + all rejected -> DESIGN_INFEASIBLE
non_exhaustive + none found -> DESIGN_UNDERDETERMINED
```

## Constraint-provenance guard / 제약 출처 보호 규칙

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

Design must not silently promote a soft preference into a hard constraint after candidate inspection merely to force a unique result. Any such change must be a new/upstream task revision with provenance.

## Output-level and target-resolution guard / 산출 수준·해상도 보호 규칙

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

Multiple admissible targets are an ordinary Design success when the declared output is `DESIGN_SPACE` or `ADMISSIBLE_TARGET`.

If `UNIQUE_TARGET` is requested and multiple materially distinct admissible targets survive without a non-optimization determinacy rule, the Design result is `DESIGN_UNDERDETERMINED`; choosing the best surviving alternative belongs to DSD Optimization.

`DES-CH-003` exposed an additional guardrail that was already implicit in Protocol v0.1 but had not yet been pressure-tested directly:

```text
material target distinctness must be judged at TARGET_RESOLUTION
```

Candidate IDs or downstream-only metadata do not by themselves establish multiple distinct Design targets.
This was preserved as a failed challenge rather than repaired post hoc.

## Method boundary / 방법 경계

- **Specification** locks or exposes requirements, permissions, prohibitions, unresolved conditions, and review scope when used as an upstream input.
- **Design** constructs an admissible target structure or admissible target family under goals and hard constraints.
- **Synthesis** combines already admitted parts or components under a composition rule.
- **Transformation** records preservation, loss, or non-correspondence between source and target structures or regimes.
- **Optimization** selects among already admissible alternatives by an explicit objective or preference criterion.
- **Audit** later retraces the Design execution against its locked scope, inputs, bridges, evidence, and verdict rules.

One workflow may use several methods, but their method verdicts and direct evidence remain separately identifiable.

## Boundary-counterexample result / 경계 반례 결과

```text
BOUNDARY_CASES_RUN: 8
BOUNDARY_PRESERVED_WITHOUT_REFINEMENT: 5
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 3
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
DIRECT_EVIDENCE_COUNT_INCREMENT: 0
```

Two non-breaking refinements were required:

1. `CONSTRAINT_SOURCE_OR_SPECIFICATION`
2. `AUXILIARY_METHODS_OR_HANDOFFS`

## Direct pilots / 직접 파일럿

### `DES-CH-001` — positive Design-space pilot

Precommitted before scoring.

```text
ADMISSIBLE_FAMILY: {T1,T2}
REJECTED: {T3,T4}
PRECOMMITTED_REQUIRED_CHECKS: 11
PASSED: 11
FAILED: 0
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
CHALLENGE_VERDICT: PASS
```

Directly tested:

```text
DEFINED_ZERO
!= APPLICABLE_BUT_UNDEFINED
!= CHANNEL_ABSENCE
```

No hidden Optimization was used; the method returned both admissible targets rather than selecting one as best.

### `DES-CH-002` — negative/failure terminal-status pilot

Precommitted before evaluation as one case ID with three locked subcases.

```text
Case I: exhaustive family + all candidates rejected
  -> DESIGN_INFEASIBLE

Case U: non_exhaustive sample + no admissible target found
  -> DESIGN_UNDERDETERMINED

Case B: required predecessor identity unavailable
  -> DESIGN_BLOCKED
```

Result:

```text
PRECOMMITTED_REQUIRED_CHECKS: 20
PASSED: 20
FAILED: 0
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in all three subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
CHALLENGE_VERDICT: PASS
```

Case B directly demonstrates that `DESIGN_BLOCKED + CONFORMANT` is a valid protocol outcome when the missing prerequisite is explicitly recorded and not fabricated.

### `DES-CH-003` — first executable Design/Optimization boundary attempt

Precommitted before evaluation.

The challenge froze three candidate records whose only difference was downstream-only `resource_cost`, while excluding that field from the Design target resolution.
The planned `UNIQUE_TARGET -> DESIGN_UNDERDETERMINED` result therefore lacked materially distinct Design targets at the declared resolution.

```text
PRECOMMITTED_REQUIRED_CHECKS: 21
PASSED: 20
FAILED: 1
CHALLENGE_VERDICT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
POST_HOC_REPAIR: none
```

The result is preserved as a failed direct challenge, not counted as a successful boundary validation.

### `DES-CH-004` — corrected Design/Optimization boundary pilot

A new precommit corrected only the future test design.
Candidate mode was explicitly included in `TARGET_RESOLUTION`:

```text
C1 -> MODE_A
C2 -> MODE_B
C3 -> MODE_C
```

All three targets remained Design-admissible, while downstream `resource_cost` could rank them only in Optimization.

Result:

```text
Case S: DESIGN_SPACE
  -> {C1,C2,C3}
  -> DESIGN_ADMISSIBLE

Case U: UNIQUE_TARGET
  -> three materially distinct admissible targets remain
  -> DESIGN_UNDERDETERMINED

PRECOMMITTED_REQUIRED_CHECKS: 23
PASSED: 23
FAILED: 0
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT in both subcases
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
CHALLENGE_VERDICT: PASS
```

The Design/Optimization boundary is therefore directly supported at pilot level without counting this as Optimization-method validation.

### `DES-CH-005` — first NO_GAIN pilot

The precommit froze the baseline, gain criteria, candidate family, expected outputs, and evidence-count rule before evaluation.

Baseline:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX
```

Frozen task:

```text
CANDIDATES: {N1,N2,N3}
H1 q_primary admitted
H2 q_reserve admitted
TARGET_RESOLUTION:
  exact admission state of q_primary, q_reserve, q_aux
```

Both B0 and DSD Design returned the same claim-relevant result:

```text
admissible family -> {N1,N2}
N3 -> rejected on H2
N1 != N2 at TARGET_RESOLUTION -> preserved
unsupported uniqueness/Optimization closure -> none
```

The four precommitted gain dimensions were not established:

```text
G1 distinction-preservation gain: not established
G2 rejection-traceability gain: not established
G3 unsupported-closure-avoidance gain: not established
G4 retraceability gain: not established
```

Result:

```text
PRECOMMITTED_REQUIRED_CHECKS: 25
PASSED: 25
FAILED: 0
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
CHALLENGE_VERDICT: PASS
```

This is the first direct confirmation that a correct, conformant Design run may still add no demonstrated method gain over a competent baseline on the declared task.
Extra DSD bookkeeping is not counted as gain by itself.

Evidence limit for all pilots: constructed same-session evidence only.

## DSD layer policy / DSD 층위 정책

The minimum-layer principle overrides a fixed serial package.

1. **Formation** — active for new structural targets, or explicitly locked as the inherited Stage-VI predecessor for downstream target design.
2. **General Property** — activated only when typed property declaration, applicability, contextual prerequisites, or partial property assignment matter to the target.
3. **Static Aggregation** — activated only when a candidate is evaluated through a declared analytic readout or aggregate.
4. **Dynamics** — activated only when trajectory, transition, lineage, propagation, or other time-dependent requirements matter.
5. **Optional specialization** — activated only through explicit supplied specialization/domain data.

No bridge is inferred from a property name, intuition, or shared vocabulary alone.

## Development sequence / 개발 순서

1. ✅ Lock the Design-specific task interface and minimum valid output at draft level.
2. ✅ Build boundary counterexamples against Specification, Synthesis, Transformation, and Optimization; incorporate non-breaking refinements.
3. ✅ Establish `PROTOCOL_v0.1.md`.
4. ✅ Run first positive constructed pilot: `DES-CH-001` PASS.
5. ✅ Run first negative/failure constructed pilot: `DES-CH-002` PASS.
6. ✅ Run executable boundary stage: `DES-CH-003` failed test design preserved; corrected `DES-CH-004` PASS.
7. ✅ Run first `NO_GAIN` pilot: `DES-CH-005` PASS.
8. **Next:** compare against a broader strongest reasonable baseline.
9. Run at least one external or independently generated application case.
10. Record reproducibility/retrace results.
11. Run a DSD Audit maturity review.

## Evidence rule / 증거 규칙

Direct Design evidence is stored under:

`evidence/method_specific/design/`

The minimum promotion architecture follows the repository-wide method-specific evidence rule:

- dedicated protocol;
- positive case;
- negative/failure case;
- boundary case;
- `NO_GAIN` case;
- reproducibility record;
- at least one external or independently generated application;
- strongest-reasonable-baseline comparison when applicable.

These are minimum evidence categories, not an automatic maturity grant.

Current direct evidence state:

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 5
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
NO_GAIN_VALIDATION_PASSES: 1
EXTERNAL_APPLICATIONS: 0
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

Historical runs are preserved under the protocol version used at execution time; later protocol revisions or corrected challenges do not rewrite earlier results.

`DES-CH-003 -> DES-CH-004` is the current explicit example of this rule.

## Next step / 다음 단계

Precommit and run a broader **strongest-reasonable-baseline comparison** under Protocol v0.1.

`DES-CH-005` used the strongest reasonable comparator for a deliberately simple synthetic finite task, but that narrow case does not by itself close the broader baseline evidence requirement.

The next baseline case should provide a competent non-DSD procedure a genuine chance to:

```text
match DSD
or outperform DSD
or lose a precommitted claim-relevant distinction
```

with baseline, gain criteria, task resolution, and scoring locked before evaluation.
