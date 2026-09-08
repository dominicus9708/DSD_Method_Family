# 04. DSD Design / DSD 설계론

Status: **Protocol v0.1 / validation in progress**

Task: construct or filter a target structure or admissible target family from declared goals, hard constraints, and an explicit candidate/construction basis rather than only analyze an already formed target.

Primary DSD interface: Formation for new structural targets or a locked inherited Stage-VI formation background for downstream target design. General Property, Static Aggregation, Dynamics, and optional specialization are activated only when the declared task actually requires them.

Typical sequence:
`task lock -> constraint-source lock -> candidate/construction-basis lock -> candidate family -> status-sensitive admissibility -> explicit domain/bridge checks -> admissible target family -> output-level check -> terminal Design status -> conformance ledger -> gain ledger`.

Typical outputs:
- admissible design space;
- one or more admissible target structures when justified;
- rejected-candidate reasons;
- explicit property and bridge requirements when used;
- target formation and transition constraints when used;
- `DESIGN_INFEASIBLE`, `DESIGN_UNDERDETERMINED`, or `DESIGN_BLOCKED` with an explicit status basis when no admissible output at the claimed level can be established.

Current terminal Design statuses:

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

Protocol conformance is separate:

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Method gain is also separate:

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Method boundary:
- Specification may lock goals, constraints, permissions, prohibitions, unresolved conditions, and review scope upstream.
- Design constructs or filters the target structure/design space under those conditions.
- Synthesis combines admitted parts; Transformation records source-target preservation/loss; Optimization selects among already-admissible alternatives under an explicit objective.
- Multiple admissible targets are not a Design failure when the declared output is a design space or an admissible target. Choosing the best one by preference/objective belongs to Optimization.
- Soft preferences are not silently promoted to hard constraints by Design; any such revision must come from an explicit upstream/task-authority change with provenance.
- When Design consumes a substantive neighboring-method verdict, that handoff is recorded and the neighboring method remains separately identifiable.
- Material distinctness for `UNIQUE_TARGET` and `DESIGN_UNDERDETERMINED` is judged at the declared `TARGET_RESOLUTION`; candidate IDs or downstream-only metadata are insufficient by themselves.
- A correct Design result does not imply method gain. `NO_GAIN` is valid when a precommitted competent baseline reproduces the claim-relevant result under the declared gain criterion.
- External authority remains separate from the Design verdict. A domain standard may supply constraints, but Design may not rewrite the standard, silently add exceptions, or expand a subset application into a full-standard conformance claim.
- Combined workflows are allowed, but method verdicts and direct evidence remain separate.

Boundary: DSD Design structures design decisions but does not replace engineering, architectural, artistic, organizational, accessibility, or other domain design knowledge and does not assume a universal candidate generator.

## Current protocol and evidence

- Executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)
- `DES-CH-001` — positive constructed challenge, `PASS`.
- `DES-CH-002` — negative/failure terminal-status challenge, `PASS`.
- `DES-CH-003` — first Design/Optimization boundary attempt, `FAIL_AS_PRECOMMITTED_CHALLENGE` due to challenge-design defect; no protocol failure inferred.
- `DES-CH-004` — corrected Design/Optimization boundary challenge, `PASS`.
- `DES-CH-005` — first `NO_GAIN` baseline-equivalence challenge, `PASS`.
- `DES-CH-006` — broader strongest-reasonable-baseline comparison, `PASS` with `NO_GAIN`.
- `DES-APP-001` — first external-standard application using W3C WCAG 2.2 subset, `PASS`.

`DES-CH-001` returned `{T1,T2}` while preserving `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and used no hidden Optimization.

`DES-CH-002` obtained:

```text
exhaustive + all candidates rejected -> DESIGN_INFEASIBLE
non_exhaustive + no admissible target found -> DESIGN_UNDERDETERMINED
required predecessor identity unavailable -> DESIGN_BLOCKED
```

`DES-CH-003` exposed a challenge-design defect because its candidate differences existed only outside the Design target resolution; the failed result was preserved. `DES-CH-004` prospectively corrected the test by placing `reserve_mode` inside the target resolution and then passed the Design/Optimization boundary check.

`DES-CH-005` established the first direct `NO_GAIN` case against `B0_EXPLICIT_CONSTRAINT_MATRIX`.

`DES-CH-006` raised the baseline pressure to Formation + General Property, 15 candidates, typed failure states, full multi-constraint rejection sets, and both `DESIGN_SPACE` and `UNIQUE_TARGET`. The competent `B1_TYPED_ADMISSIBILITY_TABLE` matched DSD on all frozen measured dimensions:

```text
Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

G1-G5: all NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

`DES-APP-001` then used a real external normative source:

```text
W3C WCAG 2.2 Recommendation 2024-12-12
selected criteria:
  SC 1.4.3 Contrast (Minimum)
  SC 2.5.3 Label in Name
  SC 2.5.8 Target Size (Minimum)
```

The frozen fixture preserved source requirements separately from task assumptions. The Design run returned:

```text
ADMISSIBLE_FAMILY: {W1,W2,W3}
W4 -> target-size failure
W5 -> target-size failure
W6 -> label-in-name failure
W7 -> label-in-name failure with APPLICABLE_BUT_UNDEFINED name
W8 -> contrast failure
W9 -> target-size + label-in-name + contrast failure
W10 -> task-local CHANNEL_ABSENCE failure

TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
```

The case did not promote the WCAG best-practice note about label position into a hard requirement, did not invent a target-size exception after inspection, and did not claim full WCAG conformance from the three-criterion subset.

## Current evidence state

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 6
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
NO_GAIN_VALIDATION_PASSES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_PASSES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
EXTERNAL_APPLICATIONS: 1
EXTERNAL_APPLICATION_PASSES: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
DEDICATED_RETRACE_STAGE: not completed
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

The evidence establishes Protocol v0.1 execution across constructed, baseline-comparison, and one external-standard application. It does not establish independent agreement or method maturity.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Protocol v0.1: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)

## Next development step

Run a dedicated **reproducibility/retrace Design test** under Protocol v0.1.

The next case should freeze one completed Design evidence record and require a clean re-execution to reproduce candidate-level verdicts, terminal status, protocol conformance, and active source/bridge inputs without modifying the historical case.
