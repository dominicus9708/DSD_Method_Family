# 04. DSD Design / DSD 설계론

Status: **planning / proposed**

Task: construct a target structure from declared goals and constraints rather than only analyze an already formed target.

Primary DSD sources: Formation + General Property; optionally Static Aggregation and Dynamics.

Typical sequence:
`goal -> candidate design space -> admissibility/describability -> applicability/prerequisites -> defined properties -> channel/bridge requirements -> output/trajectory requirements -> selection, rejection, or NO_GAIN`.

Typical outputs:
- admissible design space;
- selected target structure when justified;
- rejected-candidate reasons;
- explicit property and bridge requirements;
- target formation and transition constraints;
- blocked, infeasible, underdetermined, or no-gain result when appropriate.

Method boundary:
- Specification may lock goals, constraints, permissions, prohibitions, unresolved conditions, and review scope upstream.
- Design constructs the target structure under those conditions.
- Synthesis combines admitted parts; Transformation records source-target preservation/loss; Optimization selects under an explicit objective.
- Combined workflows are allowed, but method verdicts and direct evidence remain separate.

Boundary: DSD Design structures design decisions but does not replace engineering, architectural, artistic, organizational, or other domain design knowledge.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)

The next development step is to lock the **Design-specific task interface and minimum valid output** before drafting Protocol v0.1.
