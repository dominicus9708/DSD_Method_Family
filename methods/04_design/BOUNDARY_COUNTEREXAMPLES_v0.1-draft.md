# DSD Design Boundary Counterexamples v0.1-draft / DSD 설계론 경계 반례 v0.1 초안

Status: **pre-protocol boundary attack; not direct Design evidence**

Date: **2026-09-08**

## 1. Purpose / 목적

This document attacks the current `TASK_INTERFACE_v0.1-draft.md` against the nearest method boundaries before `PROTOCOL_v0.1.md` is written.

The target boundaries are:

```text
Specification <-> Design
Design <-> Synthesis
Design <-> Transformation
Design <-> Optimization
```

These cases are planning-stage counterexamples. They test whether the proposed Design interface can keep neighboring operations separately identifiable. They do **not** increase the direct Design pilot count.

## 2. Reference lock / 기준 잠금

```text
DESIGN_INTERFACE: methods/04_design/TASK_INTERFACE_v0.1-draft.md
SPECIFICATION: methods/03_specification/README.md
SYNTHESIS: methods/05_synthesis/README.md
TRANSFORMATION: methods/08_transformation/README.md
OPTIMIZATION: methods/12_computation_optimization/optimization/README.md
METHOD_BOUNDARY_MATRIX: methods/METHOD_BOUNDARY_MATRIX.md
DSD_INTERFACE_PROFILE: methodology/DSD_INTERFACE_PROFILE.md
```

The current registry distinguishes methods by materially different inputs, operations, outputs, failure/NO_GAIN criteria, or validation standards. Shared layers or shared operators do not merge methods.

## 3. Counterexample family / 반례군

### DES-BND-DRAFT-001 — Specification-only requirement ledger

**Setup**

A source document declares requirements `R1...Rn`, including required, prohibited, conditionally applicable, and unresolved items. The requested task is only to preserve these requirements, their statuses, prerequisites, and unresolved boundaries. No candidate structure, construction grammar, or target architecture is supplied.

**Tempting misclassification**

Treat the requirement ledger itself as a Design output because it constrains a future target.

**Expected classification**

```text
PRIMARY_METHOD: DSD Specification
DESIGN_EXECUTION: not applicable to the declared task
```

If a separate Design task is nevertheless declared without a candidate/construction basis, that Design task is `DESIGN_BLOCKED`; the Specification result itself does not become Design.

**Boundary reason**

Specification states what must be preserved or resolved. Design begins only when a declared target/design-space construction task and candidate/construction basis exist.

**Verdict**: `BOUNDARY_PRESERVED`

---

### DES-BND-DRAFT-002 — Specification-to-Design handoff

**Setup**

Specification supplies a locked requirement set `R`. A separate Design task supplies candidate structures `T1, T2, T3` or a reproducible construction grammar. Design filters them against `R` and returns the admissible family.

**Tempting misclassification**

Merge Specification and Design because the Design constraints came from Specification.

**Expected classification**

```text
UPSTREAM_METHOD: DSD Specification
RECEIVING_METHOD: DSD Design
HANDOFF_OBJECT: locked requirement/status record
DESIGN_OUTPUT: admissible target family or terminal Design status
```

Design may consume Specification output but may not silently rewrite the source requirement, purpose, priority, intentional openness, or unresolved status.

**Verdict**: `BOUNDARY_PRESERVED`

---

### DES-BND-DRAFT-003 — Synthesis-only fixed target

**Setup**

Components `A, B, C` are already admitted. The target whole and the parts-to-whole rule are fixed in advance. The task is to combine the parts under the supplied composition rule and check whether the composition is legitimate.

**Tempting misclassification**

Call the operation Design merely because a larger structure is produced.

**Expected classification**

```text
PRIMARY_METHOD: DSD Synthesis
DESIGN_SELECTION_OR_TARGET_CONSTRUCTION: none
```

**Boundary reason**

The target structure is not being chosen or constructed from competing goal-constrained alternatives; the method-specific operation is the legitimacy of the parts-to-whole composition.

**Verdict**: `BOUNDARY_PRESERVED`

---

### DES-BND-DRAFT-004 — Design candidate generation that invokes Synthesis

**Setup**

A Design task receives goals, hard constraints, allowed parts, and constructors. Several candidate topologies can be generated. To claim that a particular candidate is actually a legitimate composition of admitted components, a parts-to-whole composition rule must be checked.

**Tempting misclassification**

Let Design step `D3 CANDIDATE CONSTRUCTION` absorb all composition-validity claims and therefore swallow Synthesis.

**Expected classification**

```text
DESIGN_ROLE: define/generate the candidate family and filter target structures
SYNTHESIS_ROLE: establish the legitimacy of any claimed parts-to-whole composition
HANDOFF: synthesis result -> candidate admissibility input for Design
```

A symbolic candidate description can be generated inside Design, but if the result relies on a substantive composition claim, the Synthesis verdict remains separately identifiable.

**Interface pressure found**

The Design execution ledger needs an explicit conditional field for auxiliary method handoffs so that candidate generation does not hide Synthesis.

**Verdict**: `BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT`

---

### DES-BND-DRAFT-005 — Transformation-only fixed source and target

**Setup**

Source schema `S` and target schema `T` are both fixed. The task is to define a mapping `S -> T` and record which statuses, fields, relations, or information are preserved, merged, omitted, or newly supplied.

**Tempting misclassification**

Call the target mapping Design because a target representation is involved.

**Expected classification**

```text
PRIMARY_METHOD: DSD Transformation
DESIGN_TARGET_CONSTRUCTION: none
```

**Boundary reason**

The target is already fixed. The method-specific question is source-target preservation/loss under a map, not construction of the target design space.

**Verdict**: `BOUNDARY_PRESERVED`

---

### DES-BND-DRAFT-006 — Design of a target schema that invokes Transformation

**Setup**

A source structure `S` is fixed, but the target representation is not. Candidate targets `T1, T2, ...` are generated under hard preservation constraints. For each candidate, a source-target mapping is required to determine whether the preservation constraints are actually met.

**Tempting misclassification**

Let Design itself make unsupported claims about preservation/loss and thereby absorb Transformation.

**Expected classification**

```text
DESIGN_ROLE: construct/filter candidate target schemas
TRANSFORMATION_ROLE: establish preservation/loss for S -> Ti
HANDOFF: transformation record -> Design admissibility check
```

If candidates are later ranked by minimum information loss rather than filtered by a hard loss threshold, that ranking step belongs to Optimization.

**Interface pressure found**

The same auxiliary-method/handoff ledger needed for Synthesis is also needed here.

**Verdict**: `BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT`

---

### DES-BND-DRAFT-007 — Hard threshold versus optimization objective

**Setup**

Three structurally admissible candidates have costs:

```text
A: 80
B: 90
C: 120
```

Two task variants are declared.

**Variant X**

```text
HARD_CONSTRAINT: cost <= 100
```

Design returns `{A, B}` as the admissible family.

**Variant Y**

```text
OBJECTIVE: minimize cost
```

Optimization chooses `A` from an already justified admissible family.

**Tempting misclassification**

Treat both filtering and ranking as the same Design operation.

**Expected classification**

```text
THRESHOLD_FILTERING: Design
BEST-UNDER-OBJECTIVE SELECTION: Optimization
```

Design may return one admissible target if only one survives hard constraints, but it does not claim that target is optimal unless an Optimization step is separately invoked.

**Verdict**: `BOUNDARY_PRESERVED`

---

### DES-BND-DRAFT-008 — Soft-preference promotion attack

**Setup**

The task declares:

```text
HARD_CONSTRAINTS: all candidates must satisfy safety condition S
SOFT_PREFERENCE: prefer fewer channels
```

Two candidates satisfy the hard constraints:

```text
T1: 2 channels
T2: 3 channels
```

A Design execution silently rewrites the soft preference into:

```text
NEW_HARD_CONSTRAINT: channel_count <= 2
```

and then claims `T1` is the uniquely determined Design target.

**Why this attacks the interface**

The current draft says a preference may be promoted into a hard design constraint by the task definition, but without provenance this could be misread as permission for Design itself to make the promotion after seeing the candidate space.

**Expected classification**

```text
SILENT_DESIGN-INTERNAL_PROMOTION: forbidden
DESIGN_RESULT_BEFORE_AUTHORIZED_TASK_REVISION: admissible family {T1, T2}
PREFERENCE-BASED_SELECTION: Optimization if used as an objective
AUTHORIZED_HARD-CONSTRAINT_REVISION: allowed only as a new/upstream task revision with provenance
```

**Required refinement**

Add explicit constraint provenance and state that Design itself cannot convert a soft preference into a hard constraint merely to force determinacy.

**Verdict**: `BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT`

## 4. Boundary attack result / 경계 공격 결과

```text
BOUNDARY_CASES_RUN: 8
BOUNDARY_PRESERVED_WITHOUT_REFINEMENT: 5
BOUNDARY_PRESERVED_WITH_NONBREAKING_REFINEMENT: 3
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
DIRECT_EVIDENCE_COUNT_INCREMENT: 0
```

The three refinement-pressure cases reduce to two non-breaking interface additions.

### R1 — Constraint provenance and anti-promotion guard

Add:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION:
```

Rule:

```text
Design may consume hard constraints supplied by the declared task, Specification, or domain authority.
Design itself must not silently promote a soft preference into a hard constraint after candidate inspection.
Any such change is a new/upstream task revision and must retain provenance.
```

### R2 — Auxiliary-method / handoff ledger

Add:

```text
AUXILIARY_METHODS_OR_HANDOFFS:
```

Rule:

```text
If Design candidate construction or admissibility depends on a substantive Synthesis, Transformation, Optimization, Audit, or other method verdict, that method remains separately recorded.
Design may consume the verdict; it does not absorb the neighboring method.
```

## 5. Updated boundary rule / 갱신 경계 규칙

After R1-R2, the Design interface can be read as:

```text
Specification may supply constraints.
Design constructs/filters the target design space.
Synthesis validates substantive parts-to-whole composition when invoked.
Transformation validates substantive source-target preservation/loss when invoked.
Optimization ranks or selects among admissible alternatives under an objective.
Audit later retraces the execution.
```

The same workflow may contain several of these methods, but every method-specific result must remain separately identifiable and auditable.

## 6. Stage-2 verdict / 2단계 판정

```text
SPECIFICATION_BOUNDARY: pass
SYNTHESIS_BOUNDARY: pass_with_nonbreaking_refinement
TRANSFORMATION_BOUNDARY: pass_with_nonbreaking_refinement
OPTIMIZATION_BOUNDARY: pass_with_nonbreaking_refinement
CONSTRAINT_PROVENANCE_GUARD: required
AUXILIARY_METHOD_HANDOFF_GUARD: required
METHOD_COLLAPSE: not found
TASK_INTERFACE_REWRITE_REQUIRED: no
TASK_INTERFACE_NONBREAKING_AMENDMENT_REQUIRED: yes
NEXT_STEP: draft Design Protocol v0.1 from the boundary-refined interface
```

This planning-stage result supports moving to the first protocol draft after the two refinements are incorporated into the task-interface document.
