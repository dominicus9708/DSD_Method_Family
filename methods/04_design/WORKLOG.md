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
- The first technical development step is the Design-specific task interface and minimum valid output.

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

### Current direct-evidence status

```text
DEDICATED_PROTOCOL: not yet established
POSITIVE_CASE: not yet established
NEGATIVE_OR_FAILURE_CASE: not yet established
BOUNDARY_CASE: not yet established
NO_GAIN_CASE: not yet established
REPRODUCIBILITY_RECORD: not yet established
EXTERNAL_OR_INDEPENDENT_APPLICATION: not yet established
BASELINE_COMPARISON: not yet established
MATURITY_AUDIT: not yet performed
```

No maturity claim is made at this stage.

---

## 2026-09-08 — Step 1: task interface and minimum valid output

Status: **planning step 1 complete at draft level**

Created:

- `TASK_INTERFACE_v0.1-draft.md`

### Main results

1. A Design task must lock its goals, hard constraints, output level, target resolution, predecessor/base structure, target DSD layer scope, candidate/construction basis, candidate-generation rule, candidate coverage, domain bridge, and external standard where required.
2. DSD Design does not contain a universal candidate generator and does not fabricate missing domain design knowledge.
3. Candidate coverage is explicitly classified as `exhaustive / non_exhaustive / unknown`.
4. `DESIGN_INFEASIBLE` requires exhaustive candidate coverage or an explicit impossibility argument; non-exhaustive failure-to-find is not a global infeasibility result.
5. The earlier provisional `DESIGN_ACCEPTED` label is replaced with `DESIGN_ADMISSIBLE` to avoid conflating structural admissibility with downstream approval or optimization.
6. Terminal Design status is separated from method-gain status.

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE
  DESIGN_INFEASIBLE
  DESIGN_UNDERDETERMINED
  DESIGN_BLOCKED

DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

7. Multiple admissible candidates are an ordinary Design success when the task asks for a design space or an admissible target. Selecting the best alternative by an objective belongs to DSD Optimization.
8. Minimum valid output is defined for successful and non-success executions, including traceable target/rejection/status basis and reproducibility fields.

### Source-interface consistency notes

The task interface follows the current DSD interface profile:

- Formation status distinctions remain preserved.
- General Property remains a typed extension over a fixed Stage-VI formation background and cannot silently rewrite formation identity.
- Static Aggregation is optional and does not support reconstruction from aggregate equality without an additional condition.
- Dynamics is optional; formation-level identity changes require explicit lineage rather than ordinary value evolution.
- Optional geometric/specialization data are not universal Property coordinates.

### Evidence status after Step 1

This planning artifact is **not** counted as a direct Design pilot.

```text
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
CURRENT_PROTOCOL: not established
CURRENT_METHOD_STATUS: planning / proposed
```

### Next technical step

Build method-boundary counterexamples against:

```text
Specification
Synthesis
Transformation
Optimization
```

The purpose is to try to break the draft task-interface boundary before drafting `PROTOCOL_v0.1.md`.

---

## 2026-09-08 — Step 2: boundary counterexamples

Status: **planning step 2 complete with non-breaking refinements**

Created:

- `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`
- `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`

### Boundary attack set

Eight pre-protocol counterexamples were constructed across the nearest method boundaries:

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

### Result

```text
BOUNDARY_CASES_RUN: 8
BOUNDARY_PRESERVED_WITHOUT_REFINEMENT: 5
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 3
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
DIRECT_EVIDENCE_COUNT_INCREMENT: 0
```

No case forced Design to merge with Specification, Synthesis, Transformation, or Optimization.

### Non-breaking refinements

Two interface additions were required.

#### R1 — Constraint provenance guard

Add:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION:
```

Design may consume source-supplied hard constraints but may not silently promote a soft preference into a hard constraint after candidate inspection. Any such promotion must be a new/upstream task revision with provenance.

#### R2 — Auxiliary-method / handoff ledger

Add conditionally:

```text
AUXILIARY_METHODS_OR_HANDOFFS:
```

If Design depends on a substantive Synthesis composition verdict, Transformation preservation/loss verdict, downstream Optimization selection, or later Audit retrace, those neighboring methods remain separately identifiable. Design may consume their outputs but does not absorb their operations or evidence.

### Effective pre-protocol interface

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

### Evidence status after Step 2

These are planning-stage boundary attacks, not direct Design pilots.

```text
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
CURRENT_PROTOCOL: not established
CURRENT_METHOD_STATUS: planning / proposed
```

### Next technical step

Draft `PROTOCOL_v0.1.md` from the boundary-refined task interface.
