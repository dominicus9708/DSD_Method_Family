# 04. DSD Design / DSD 설계론

Status: **Protocol v0.1 executable / method validation pending**

Task: construct or filter a target structure or admissible target family from declared goals, hard constraints, and an explicit candidate/construction basis rather than only analyze an already formed target.

Primary DSD interface: Formation for new structural targets or a locked inherited Stage-VI formation background for downstream target design. General Property, Static Aggregation, Dynamics, and optional specialization are activated only when the declared task actually requires them.

Typical sequence:
`task/claim lock -> constraint-source lock -> candidate/construction-basis and coverage lock -> candidate family -> status-sensitive admissibility -> explicit domain/bridge/auxiliary checks -> admissible target family -> output-level check -> terminal Design status -> separate protocol-conformance and method-gain ledgers`.

Typical outputs:
- admissible design space within declared candidate coverage;
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

Protocol conformance is recorded separately:

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
- Combined workflows are allowed, but method verdicts and direct evidence remain separate.

Boundary: DSD Design structures design decisions but does not replace engineering, architectural, artistic, organizational, scientific, mathematical, legal, safety, or other domain design knowledge and does not assume a universal candidate generator.

## Current protocol

- [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md) — **initial executable protocol; validation pending**.

Protocol v0.1 fixes:

- task/claim and constraint-source locking;
- candidate/construction basis and coverage discipline;
- DSD layer activation rules;
- Design construction procedure D1-D13;
- terminal Design status ledger;
- separate protocol-conformance ledger;
- separate method-gain ledger;
- auxiliary-method handoff discipline;
- case-ID convention `DES-CH-*`, `DES-APP-*`, `DES-AUD-*`;
- minimum execution and reproducibility records.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)

Planning Steps 1-2 are complete and Protocol v0.1 is now executable. Protocol creation itself is not a direct Design pilot.

Current evidence state:

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_EVIDENCE_STATUS: validation_pending
```

The next development step is the first **positive constructed Design challenge** under a frozen Protocol v0.1 task record.
