# DSD Design Worklog / DSD 설계론 작업 기록

## 2026-09-08 — Planning preparation

Status: **planning started**

Prepared the Design development lane to follow the same record discipline used for other DSD methods.

### Locked project paths

```text
methods/04_design/
evidence/method_specific/design/
```

### Initial decisions

- Design remains an independent method under **Field III: Construction & Transformation**.
- Formation is the primary structural interface; General Property is activated only when typed property requirements materially enter the target.
- Static Aggregation and Dynamics remain optional and task-activated.
- Specification may provide locked goals/constraints upstream, but Specification and Design are not merged.
- Synthesis, Transformation, and Optimization remain neighboring but distinct methods.
- Shared evidence and evidence from other methods do not count as direct Design validation.

### Planned evidence sequence

```text
task interface
-> boundary counterexamples
-> Protocol v0.1
-> positive pilot
-> failure pilot
-> boundary pilot
-> NO_GAIN pilot
-> baseline comparison
-> external/independent application
-> reproducibility record
-> DSD Audit maturity review
```

---

## 2026-09-08 — Step 1: task interface and minimum valid output

Status: **planning step 1 complete at draft level**

Created:

- `TASK_INTERFACE_v0.1-draft.md`

Main results:

- explicit candidate/construction basis required;
- candidate coverage classified as `exhaustive / non_exhaustive / unknown`;
- non-exhaustive failure-to-find cannot support global infeasibility;
- `DESIGN_ACCEPTED` replaced by `DESIGN_ADMISSIBLE`;
- Design terminal status separated from method-gain status;
- multiple admissible candidates are ordinary success for design-space/admissible-target claims;
- Optimization begins when an objective ranks/selects among already admissible alternatives.

Evidence increment: **0 direct pilots**.

---

## 2026-09-08 — Step 2: boundary counterexamples

Status: **planning step 2 complete with non-breaking refinements**

Created:

- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`
- `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`

Boundary set:

```text
DES-BND-DRAFT-001  Specification-only requirement ledger
DES-BND-DRAFT-002  Specification-to-Design handoff
DES-BND-DRAFT-003  Synthesis-only fixed target
DES-BND-DRAFT-004  Design candidate generation invoking Synthesis
DES-BND-DRAFT-005  Transformation-only fixed source/target
DES-BND-DRAFT-006  Design target-schema construction invoking Transformation
DES-BND-DRAFT-007  hard threshold versus optimization objective
DES-BND-DRAFT-008  soft-preference promotion attack
```

Result:

```text
BOUNDARY_CASES_RUN: 8
BOUNDARY_PRESERVED_WITHOUT_REFINEMENT: 5
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 3
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
DIRECT_EVIDENCE_COUNT_INCREMENT: 0
```

Required non-breaking additions:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION
AUXILIARY_METHODS_OR_HANDOFFS
```

Evidence increment: **0 direct pilots**.

---

## 2026-09-08 — Step 3: Protocol v0.1 establishment

Status: **first executable Design protocol established; validation pending**

Created:

- `PROTOCOL_v0.1.md`

### Protocol-source lock

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
+ BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
-> PROTOCOL_v0.1.md
```

### Main protocol decisions

1. Protocol v0.1 fixes a pre-evaluation task/claim lock, constraint-source lock, candidate-basis/coverage lock, selected DSD interface lock, and validation rule.
2. `CLAIMED_OUTPUT_LEVEL` is fixed to `DESIGN_SPACE`, `ADMISSIBLE_TARGET`, `UNIQUE_TARGET`, or `PARTIAL_TARGET`.
3. `DESIGN_SPACE` is explicitly relative to declared candidate coverage; it does not silently claim a global exhaustive design universe.
4. Soft preferences cannot be promoted post hoc into hard constraints by Design.
5. Candidate/construction basis remains explicit; missing domain design knowledge may validly yield `DESIGN_BLOCKED`.
6. Formation, General Property, Static Aggregation, Dynamics, and optional specialization follow minimum-layer activation rather than mandatory serial use.
7. Synthesis, Transformation, Optimization, Specification, Audit, and other neighboring method verdicts remain separately recorded under `AUXILIARY_METHODS_OR_HANDOFFS` when used.
8. Candidate-level records distinguish admissible, rejected, unresolved, and blocked cases without collapsing claim-relevant DSD states.
9. The executable procedure is fixed as D1-D13.
10. Design outcome, protocol conformance, and method gain are three distinct ledgers.

### Terminal Design status

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

### Protocol conformance

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative protocol violations include post-hoc soft-to-hard promotion, undeclared candidate-basis changes, unsupported exhaustiveness/uniqueness, infeasibility overclaim, required-bridge omission, hidden Optimization, and neighboring-method verdict absorption.

### Method gain

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

`GAIN_ESTABLISHED` and `NO_GAIN` require an actual baseline comparison. Otherwise the protocol requires `NOT_ASSESSED`.

### Case-ID convention fixed

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Planning-stage `DES-BND-DRAFT-*` records remain planning artifacts and are not retroactively promoted to direct evidence.

### Evidence status after Protocol v0.1

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
BASELINE_BENEFIT: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_pending
```

Protocol establishment does not itself increase direct evidence.

### Related commits

```text
PROTOCOL_v0.1.md  b3d658c
README.md         d9a3eb2
PLANNING.md       0511c2c
```

### Next technical step

Pre-lock and execute the first **positive constructed Design challenge** under Protocol v0.1, using a case with at least one admissible target and no need for hidden Optimization.
