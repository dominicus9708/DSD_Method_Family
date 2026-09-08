# 04. DSD Design / DSD 설계론

Status: **planning / proposed**

Task: construct or filter a target structure or admissible target family from declared goals, hard constraints, and an explicit candidate/construction basis rather than only analyze an already formed target.

Primary DSD interface: Formation for new structural targets or a locked inherited Stage-VI formation background for downstream target design. General Property, Static Aggregation, Dynamics, and optional specialization are activated only when the declared task actually requires them.

Typical sequence:
`task lock -> candidate/construction-basis lock -> candidate family -> status-sensitive admissibility -> explicit domain/bridge checks -> admissible target family -> output-level check -> terminal Design status`.

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

Method gain is recorded separately:

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
- Combined workflows are allowed, but method verdicts and direct evidence remain separate.

Boundary: DSD Design structures design decisions but does not replace engineering, architectural, artistic, organizational, or other domain design knowledge and does not assume a universal candidate generator.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)

Effective pre-protocol interface:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

Planning Step 2 is complete. Eight boundary counterexamples preserved the Design boundary with **no method collapse** and required only two non-breaking refinements: constraint provenance and explicit auxiliary-method/handoff recording. The next development step is to draft `PROTOCOL_v0.1.md`.
