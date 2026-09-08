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
- Combined workflows are allowed, but method verdicts and direct evidence remain separate.

Boundary: DSD Design structures design decisions but does not replace engineering, architectural, artistic, organizational, or other domain design knowledge and does not assume a universal candidate generator.

## Current protocol and evidence

- Executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)
- `DES-CH-001` — positive constructed challenge, `PASS`.
- `DES-CH-002` — negative/failure terminal-status challenge, `PASS`.
- `DES-CH-003` — first Design/Optimization boundary attempt, `FAIL_AS_PRECOMMITTED_CHALLENGE` due to challenge-design defect; no protocol failure inferred.
- `DES-CH-004` — corrected Design/Optimization boundary challenge, `PASS`.

`DES-CH-001` returned exactly `{T1,T2}` as admissible while preserving `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and using no hidden Optimization.

`DES-CH-002` separately precommitted three non-success subcases and obtained:

```text
exhaustive + all candidates rejected
-> DESIGN_INFEASIBLE

non_exhaustive + no admissible target found
-> DESIGN_UNDERDETERMINED

required predecessor identity unavailable
-> DESIGN_BLOCKED
```

`DES-CH-003` revealed that its candidate differences existed only in `resource_cost`, which the same precommit had excluded from the Design target resolution. The planned underdetermination result was therefore not supported; the failed case was preserved without post-hoc repair.

`DES-CH-004` prospectively corrected the test by placing `reserve_mode = MODE_A / MODE_B / MODE_C` inside the target resolution. All three targets remained Design-admissible, while `resource_cost` remained only a downstream Optimization objective. The Design-space subcase returned all three; the `UNIQUE_TARGET` subcase correctly returned `DESIGN_UNDERDETERMINED` rather than selecting the cheapest target.

```text
DIRECT_CONSTRUCTED_PILOTS: 4
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 0
EXTERNAL_APPLICATIONS: 0
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

The current pilots are direct evidence for Protocol v0.1 execution only; they do not establish external applicability, baseline superiority, independent agreement, Optimization validity, or method maturity.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Protocol v0.1: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)

## Next development step

Precommit and run the first **`NO_GAIN` constructed Design challenge** under Protocol v0.1.

Lock a strongest reasonable baseline and gain criterion before evaluation. A correct Design result may still end with:

```text
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

when the baseline is equally sufficient on the declared comparison criterion.
