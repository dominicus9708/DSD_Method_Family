# DSD Design Task Interface v0.1-draft / DSD 설계론 과업 인터페이스 v0.1 초안

Status: **draft task-interface lock; not yet a protocol**

Date: **2026-09-08**

This document completes the first planning step for DSD Design: define what must be supplied before a Design task is well-formed, what Design itself does, and what minimum output is required for a valid execution record.

It does **not** yet count as `PROTOCOL_v0.1.md`, and it does not create direct Design-validation evidence by itself.

## 1. Core distinction / 핵심 구분

DSD Design does not invent domain design knowledge from nothing.
It structures a declared design problem and constructs or filters target structures only relative to supplied goals, constraints, candidate/construction resources, DSD predecessor layers, and explicit domain bridges.

The minimal conceptual form is:

```text
DECLARED DESIGN TASK
+ candidate/construction basis
+ selected DSD interface
+ explicit domain bridge / external standard when required
-> candidate design family
-> status-sensitive admissibility evaluation
-> admissible target family OR terminal non-success result
```

The output may be one target, several admissible targets, a partial target at declared resolution, or a justified non-success status.
Design does not require uniqueness unless the declared task itself requests a unique target.

## 2. Well-formed Design task / 적형 설계 과업

A Design task is well-formed only when the following fields are fixed sufficiently for the claimed output level.

```text
DESIGN_TASK_ID:
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
GOALS:
HARD_CONSTRAINTS:
SOFT_PREFERENCES:
BASE_STRUCTURE_OR_PREDECESSOR:
TARGET_DSD_LAYER_SCOPE:
TARGET_RESOLUTION:
CANDIDATE_OR_CONSTRUCTION_BASIS:
CANDIDATE_GENERATION_RULE:
CANDIDATE_COVERAGE:
DSD_INTERFACE_PROFILE:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
VALIDATION_OR_ACCEPTANCE_RULE:
```

### 2.1 `CLAIMED_OUTPUT_LEVEL`

Recommended values:

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

- `DESIGN_SPACE`: return the admissible family; uniqueness is not claimed.
- `ADMISSIBLE_TARGET`: return at least one admissible target without claiming it is uniquely best.
- `UNIQUE_TARGET`: claim that the declared task determines one target at the stated resolution.
- `PARTIAL_TARGET`: construct only the declared subset of target coordinates/relations; unresolved coordinates outside that scope are not defects.

### 2.2 Hard constraints and soft preferences

`HARD_CONSTRAINTS` determine admissibility.

`SOFT_PREFERENCES` may be recorded for downstream use, but Design alone does not rank admissible alternatives by preference. If a preference or objective is used to choose among multiple already-admissible alternatives, that selection step belongs to **DSD Optimization** unless the preference has first been promoted into an explicit hard design constraint by the task definition.

### 2.3 Candidate/construction basis

DSD Design does not assume a canonical universal candidate generator.
At least one of the following must be supplied:

- an explicit candidate family;
- a construction grammar;
- allowed parts plus constructors;
- a parameterized target schema;
- a theorem or domain rule that determines a candidate family;
- another explicit mechanism sufficient to reproduce the candidate space used by the task.

If the domain itself supplies no candidate/construction basis, DSD does not fabricate one silently.

### 2.4 Candidate coverage

Record:

```text
CANDIDATE_COVERAGE: exhaustive / non_exhaustive / unknown
```

`DESIGN_INFEASIBLE` may be asserted only when one of the following is established:

1. the declared candidate/construction space is exhaustive for the task and every candidate fails a required condition; or
2. a valid impossibility argument establishes that no target can satisfy the declared hard constraints.

Failure to find a candidate in a non-exhaustive search is **not** by itself infeasibility.

## 3. DSD layer activation / DSD 층위 활성화

The method-family minimum-layer rule remains active.
Do not activate a downstream layer only because DSD contains it.

### 3.1 Formation

For a new structural target, Formation is the primary candidate-admission and channel-formation interface.

For a target built over an already fixed Stage-VI predecessor, the inherited formation background may be locked rather than redesigned.

The execution must preserve distinctions such as:

```text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
```

### 3.2 General Property

Activate the Property layer only when the design task requires typed properties, applicability, contextual prerequisites, or partial property assignments.

A property-design extension is evaluated over a fixed Stage-VI formation background and does not silently alter formation assignments, roles, operational-channel identity, or formation traces.

Preserve as applicable:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
```

### 3.3 Static Aggregation

Activate Static Aggregation only when a candidate must be evaluated through a declared analytic readout or aggregate.

Aggregate equality alone cannot establish equality of support, decomposition, source structure, or design identity. Any reconstruction claim requires the corresponding injectivity or reconstruction condition.

### 3.4 Dynamics

Activate Dynamics only when the target includes trajectories, time-dependent requirements, regular epochs, transitions, propagation, or other dynamic conditions.

A formation-level identity change is not represented as ordinary value evolution of one unchanged inherited channel. If predecessor-successor identity is claimed across such a change, the required lineage relation must be supplied.

### 3.5 Optional specialization

Geometry or other specialization data are activated only when explicitly supplied by the task or domain bridge. They are not inferred from property names or from the existence of a general Property model.

## 4. Design operation / 설계 연산

A Design execution performs the following method-specific operations.

```text
D1  TASK LOCK
D2  CANDIDATE-BASIS LOCK
D3  CANDIDATE CONSTRUCTION / ENUMERATION
D4  DSD STATUS-SENSITIVE ADMISSIBILITY CHECK
D5  DOMAIN-BRIDGE / EXTERNAL-CONSTRAINT CHECK
D6  ADMISSIBLE-FAMILY CONSTRUCTION
D7  OUTPUT-LEVEL CHECK
D8  TERMINAL STATUS AND TRACE RECORD
```

### D1 — Task lock
Fix goals, hard constraints, output claim, target resolution, selected DSD layers, and validation rule.

### D2 — Candidate-basis lock
Fix the explicit candidate/construction basis and whether it is exhaustive.

### D3 — Candidate construction / enumeration
Construct or enumerate only candidates licensed by the declared basis. Candidate generation may be deterministic, branching, relational, finite, symbolic, or externally supplied.

### D4 — DSD status-sensitive admissibility check
For every candidate used by the result, retain the DSD distinctions that materially affect admissibility rather than collapsing unavailable, inapplicable, undefined, absent, and zero states.

### D5 — Domain-bridge / external-constraint check
Where the claim leaves the DSD-internal domain, apply only an explicitly supplied bridge and keep external validation distinct from DSD-internal structural success.

### D6 — Admissible-family construction
Let `C_D` be the declared candidate family actually covered by the execution. Construct the admissible subfamily `A_D` consisting of candidates for which every task-required check is established at the claimed resolution.

This is a status-sensitive filter, not a simple zero-padded Boolean test.

### D7 — Output-level check
Match the result to the declared output level.

- For `DESIGN_SPACE`, multiple admissible targets are an ordinary success.
- For `ADMISSIBLE_TARGET`, at least one traceable admissible target is sufficient; Design does not claim optimality.
- For `UNIQUE_TARGET`, uniqueness must follow from the declared exhaustive space or an explicit determinacy argument. If several materially distinct admissible targets remain and no non-optimization rule removes them, the uniqueness claim is underdetermined.
- For `PARTIAL_TARGET`, only the declared partial coordinates/relations must be resolved.

### D8 — Terminal status and trace record
Return the terminal Design status together with its basis, candidate coverage, rejected-candidate reasons when relevant, unresolved fields, and reproducibility record.

## 5. Terminal Design-status ledger / 종결 설계 상태 장부

The earlier provisional `DESIGN_ACCEPTED` label is replaced by `DESIGN_ADMISSIBLE` to avoid implying external approval or optimization.

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

### `DESIGN_ADMISSIBLE`

At least one target satisfies every required condition for the declared output level and resolution.

This may return one or many admissible targets. It does not by itself claim that the target is optimal, externally approved, empirically validated, or uniquely determined.

### `DESIGN_INFEASIBLE`

No target can satisfy the required conditions **and** the no-target claim is supported by exhaustive candidate coverage or an explicit impossibility argument.

### `DESIGN_UNDERDETERMINED`

The available task definition permits valid candidates but does not support the stronger output claim being requested.

Typical examples:

- a `UNIQUE_TARGET` is requested but several materially distinct admissible targets remain;
- required target coordinates are not constrained enough for the claimed resolution;
- a non-exhaustive candidate search cannot support a global no-solution claim.

### `DESIGN_BLOCKED`

A required prerequisite for performing or validating the declared Design task is missing.

Examples include:

- no reproducible candidate/construction basis;
- missing required predecessor-layer data;
- missing required domain bridge;
- missing external standard for a claim that explicitly depends on it;
- a required typed profile or prerequisite decision cannot be supplied at all.

## 6. Gain ledger is separate / 이득 판정 장부 분리

`NO_GAIN` is not a target-structure status.
It is a method-evaluation result and is therefore recorded separately from the Design terminal status.

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

For example, a case may be structurally `DESIGN_ADMISSIBLE` while also being `NO_GAIN` relative to a strongest reasonable baseline because the same result was obtained more simply without DSD structure.

This separation prevents method utility from being confused with object/design status.

## 7. Minimum valid execution output / 최소 유효 실행 산출물

A Design execution is record-valid only if it produces the following minimum ledger, even when no target is successfully constructed.

```text
DESIGN_TASK_ID:
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
GOALS:
HARD_CONSTRAINTS:
BASE_STRUCTURE_OR_PREDECESSOR:
TARGET_DSD_LAYER_SCOPE:
TARGET_RESOLUTION:
CANDIDATE_OR_CONSTRUCTION_BASIS:
CANDIDATE_COVERAGE:
DSD_INTERFACE_PROFILE:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
CANDIDATES_ACTUALLY_EVALUATED_OR_SYMBOLIC_FAMILY:
CANDIDATE_STATUS_RECORD:
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY:
REJECTED_CANDIDATE_REASONS:
UNRESOLVED_FIELDS:
TERMINAL_DESIGN_STATUS:
TERMINAL_STATUS_BASIS:
DESIGN_METHOD_GAIN_STATUS:
LIMITS:
REPRODUCIBILITY_RECORD:
```

### 7.1 Minimum output for `DESIGN_ADMISSIBLE`

Must include:

- at least one reproducibly identified admissible target or an explicit admissible family;
- trace from every claim-relevant target coordinate/relation to the constraint or supplied rule that licenses it;
- unresolved fields outside the declared resolution, if any;
- no implicit claim of optimality or external validation.

### 7.2 Minimum output for `DESIGN_INFEASIBLE`

Must include:

- the exhaustive-space justification or impossibility argument;
- the violated condition classes;
- enough rejected-candidate or symbolic proof structure to retrace the no-target claim.

### 7.3 Minimum output for `DESIGN_UNDERDETERMINED`

Must include:

- the stronger output claim that could not be supported;
- at least one explicit unresolved discriminator, unconstrained coordinate, or surviving alternative family;
- a statement of what additional input would be required to resolve it without silently invoking Optimization.

### 7.4 Minimum output for `DESIGN_BLOCKED`

Must include:

- the specific missing prerequisite, bridge, source datum, or candidate basis;
- the exact downstream checks that cannot be performed because it is missing.

## 8. Method boundary consequences / 방법 경계 귀결

### Specification -> Design
Specification may provide requirements and unresolved conditions as upstream data. Design does not retroactively change what the source specification said.

### Design != Optimization
If multiple admissible targets remain, Design may return the family. Choosing the "best" one under an objective is Optimization.

### Design != Synthesis
A Design task may declare how a target should be structured. The actual parts-to-whole composition operation is Synthesis when admitted parts are combined under a composition rule.

### Design != Transformation
A Design target may later be represented in another schema or regime. Preservation/loss under that source-target map is Transformation.

### Design != Audit
A Design execution creates a target/design-space result. Audit retraces whether that execution respected its scope, inputs, bridge rules, evidence, and verdict discipline.

## 9. First-step verdict / 1단계 판정

```text
TASK_INTERFACE_DEFINED: yes, draft
MINIMUM_VALID_OUTPUT_DEFINED: yes, draft
TERMINAL_STATUS_LEDGER_DEFINED: yes, draft
NO_GAIN_SEPARATED_FROM_DESIGN_STATUS: yes
CANDIDATE_COMPLETENESS_GUARD: yes
OPTIMIZATION_BOUNDARY_GUARD: yes
PROTOCOL_STATUS: not yet established
DIRECT_EVIDENCE_CREATED_BY_THIS_DOCUMENT: no
```

The next development step is to build boundary counterexamples against Specification, Synthesis, Transformation, and Optimization before drafting Protocol v0.1.
