# DSD Synthesis Boundary Counterexamples v0.1 Draft / DSD 합성론 경계 반례 v0.1 초안

Status: **planning Step 2 complete — pre-protocol boundary attack**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol status: **not yet executable**

## 1. Purpose / 목적

This artifact attacks the Step-1 Synthesis task interface before an executable protocol is frozen.

It tests whether Synthesis remains distinct from neighboring methods and whether the draft can resist hidden algebraic, structural, property, coverage, and process assumptions.

These are **pre-protocol planning attacks**.
They do not count as direct Synthesis validation evidence.

## 2. Source/interface lock / 기준 잠금

The attack uses the current project interfaces:

```text
methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md
methodology/DSD_INTERFACE_PROFILE.md
methods/METHOD_BOUNDARY_MATRIX.md
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
```

The following Step-1 guards are attacked rather than assumed true:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY

EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE

FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY

AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE

COMPONENT_PROPERTY
!= WHOLE_PROPERTY
```

## 3. Evaluation categories / 판정 범주

```text
PRESERVED_NO_REFINEMENT
PRESERVED_WITH_NONBREAKING_REFINEMENT
BOUNDARY_COLLAPSE
FUNDAMENTAL_INTERFACE_FAILURE
```

A non-breaking refinement may add an explicit field or guard that was already implicit in the method purpose.
It may not redefine Synthesis so broadly that Design, Transformation, Aggregation, Optimization, or another method is absorbed.

---

## SYN-BND-DRAFT-001 — Hidden Design by inventing missing architecture

### Attack

A task states only:

```text
GOAL: produce a redundant sensing system
CONSTRAINT: tolerate one sensor failure
```

No component set, connector architecture, or composition rule is supplied.

If Synthesis invents two sensors, a voter, wiring, and architecture in order to satisfy the goal, it is performing Design.

### Expected boundary behavior

Synthesis must not fabricate the missing parts or architecture.
The task is blocked for Synthesis until a Design or domain handoff supplies the required composition basis.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

The Step-1 `COMPONENT_SET_OR_FAMILY`, `COMPOSITION_RULE`, and `AUXILIARY_METHODS_OR_HANDOFFS` fields already separate the operations.

---

## SYN-BND-DRAFT-002 — Explicit Design -> Synthesis handoff

### Attack

Design supplies:

```text
parts = {A,B,C}
architecture = A connected to B through connector C
hard constraints already resolved upstream
```

Synthesis must test whether those supplied parts can actually form the declared whole under the supplied composition/interface rule.

### Boundary question

Does consuming a Design result collapse Design into Synthesis?

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

The Design verdict remains upstream.
Synthesis consumes the frozen parts/rule but produces a separate composability verdict.

---

## SYN-BND-DRAFT-003 — Transformation-only source-to-target mapping

### Attack

One object is mapped from representation `R_A` to representation `R_B`.
No multiple-part whole is formed.

```text
source object X in schema A
-> mapping F
-> X' in schema B
```

### Boundary question

Can this be called Synthesis merely because the transformed output is a larger record?

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

This is Transformation unless an actual parts-to-whole composition is separately supplied.

---

## SYN-BND-DRAFT-004 — Pre-transform components before synthesis

### Attack

Components `A` and `B` are individually admitted but use incompatible representations.
Each must first be transformed into a common target representation before the supplied composition rule applies.

### Expected behavior

```text
Transformation(A) -> A'
Transformation(B) -> B'
Synthesis(A',B') -> W
```

The transformation results are handoff inputs.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

Synthesis does not absorb the Transformation operation or its validation standard.

---

## SYN-BND-DRAFT-005 — Aggregation-only readout mistaken for a whole

### Attack

Two admitted analytic channel outputs are combined:

```text
y = T_1 + T_2
```

The scalar/vector readout is well defined, but no domain rule says that `y` is a structural whole composed of the two channels.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

Static Aggregation produces a readout.
The Step-1 guard `AGGREGATE_READOUT != SYNTHESIZED_WHOLE` survives.

---

## SYN-BND-DRAFT-006 — Aggregation used after genuine synthesis

### Attack

A supplied rule composes `A` and `B` into whole `W`.
A separate aggregate readout is then used to summarize load or output:

```text
A ⊙ B -> W
y = aggregate(W)
```

### Boundary question

Does the downstream aggregate become the Synthesis output itself?

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

Synthesis produces `W`; Aggregation produces `y`.
The latter may validate or summarize the former but does not replace its structural identity.

---

## SYN-BND-DRAFT-007 — Hidden Optimization among admissible compositions

### Attack

Three compositions satisfy every Synthesis hard condition:

```text
C1 admissible, cost 30
C2 admissible, cost 20
C3 admissible, cost 10
```

The task then asks for the cheapest one.

### Expected behavior

Synthesis returns the admissible family.
Optimization performs objective-based ranking/selection.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

`SYNTHESIS_SPACE` and `AUXILIARY_METHODS_OR_HANDOFFS` already prevent hidden Optimization.

---

## SYN-BND-DRAFT-008 — Component property automatically promoted to whole property

### Attack

Components `A` and `B` each have a defined property `p` under their own typed property profiles.
A composition `A ⊙ B -> W` is admissible.

The attack asserts:

```text
p(A) defined
p(B) defined
therefore p(W) automatically defined
```

### Expected behavior

The inference is invalid unless a whole-property lift, combination, inheritance, or redeclaration rule is supplied.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

`PROPERTY_LIFT_OR_REDECLARATION_RULE` already blocks the automatic promotion.

---

## SYN-BND-DRAFT-009 — Unjustified commutativity

### Attack

A binary rule permits:

```text
A ⊙ B -> W_AB
```

but interface direction makes:

```text
B ⊙ A
```

invalid.

The attack treats `A ⊙ B = B ⊙ A` without a supplied commutativity law.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

The Step-1 fields `COMPOSITION_ORDER_SENSITIVITY` and the nonconformance class `UNJUSTIFIED_COMMUTATIVITY_ASSUMPTION` already cover this case.

---

## SYN-BND-DRAFT-010 — Unjustified associativity / parenthesization collapse

### Attack

For components `A,B,C`, a supplied binary rule allows:

```text
(A ⊙ B) ⊙ C
```

but the intermediate result of `B ⊙ C` is incompatible with `A`, so:

```text
A ⊙ (B ⊙ C)
```

is not admissible.

The Step-1 draft has an `UNJUSTIFIED_ASSOCIATIVITY_ASSUMPTION` failure class, but it does not yet provide a positive task field for declaring grouping/parenthesization or the supplied algebraic law profile.

### Verdict

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

Required refinement: explicitly lock the supplied composition-law and grouping/parenthesization policy.

---

## SYN-BND-DRAFT-011 — Identity / idempotence / repetition collapse

### Attack

The task contains possible repeated or neutral-like components.

Examples:

```text
A ⊙ E
A ⊙ A
```

The attack silently assumes either:

```text
A ⊙ E = A
A ⊙ A = A
```

without a supplied identity or idempotence law.

`MULTIPLICITY_POLICY` controls whether repeated participation is allowed, but does not state what algebraic equivalence follows from repetition or a claimed neutral element.

### Verdict

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

The same composition-law profile required by SYN-BND-DRAFT-010 must include identity/idempotence only when explicitly supplied.

---

## SYN-BND-DRAFT-012 — Syntactic composition trees mistaken for materially distinct targets

### Attack

Suppose associativity is explicitly supplied for the relevant domain and target resolution:

```text
(A ⊙ B) ⊙ C
A ⊙ (B ⊙ C)
```

Two separately generated syntax trees may therefore denote the same synthesized target at the declared `TARGET_RESOLUTION`.

If candidate IDs alone are counted as distinct, a `UNIQUE_SYNTHESIZED_TARGET` claim may be falsely rejected as underdetermined.
The reverse problem also exists: two syntactically similar records may still be materially different if the domain rule preserves hidden interface structure.

### Verdict

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

Required refinement: lock a `COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE` before uniqueness/multiplicity conclusions.

---

## SYN-BND-DRAFT-013 — Partial synthesis silently upgraded to complete synthesis

### Attack

`A ⊙ B -> M` forms a valid submodule, but interface `p_open` remains unresolved and component `C` has not yet been connected.

The task correctly asks for `PARTIAL_SYNTHESIS`, but the candidate record contains no dedicated residual-interface field.

A downstream reader could therefore mistake `M` for a completed synthesized target.

### Verdict

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

Required refinement: record residual open interfaces, omitted parts, and downstream obligations explicitly for partial synthesis.

---

## SYN-BND-DRAFT-014 — Static composability mistaken for temporal assembly feasibility

### Attack

A final topology is statically composable under a supplied rule, but the actual assembly process may have order-dependent constraints or transient forbidden states.

Example:

```text
final structure A-B-C is valid
but attaching C before stabilizing A-B creates a forbidden intermediate state
```

`COMPOSITION_ORDER_SENSITIVITY` may describe operand/order semantics, but it is not sufficient to say whether a **time-resolved assembly sequence** is claimed.

### Verdict

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

Required refinement: separate static composition order from `ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE`; activate Dynamics only when process/transition feasibility is actually claimed.

---

## SYN-BND-DRAFT-015 — Exhaustive parts mistaken for exhaustive composition coverage

### Attack

The full component list is known:

```text
{A,B,C,D}
```

but possible topology, order, connector, grouping, or interface mappings are not exhaustively enumerated.

A sampled search finds no valid composition.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

The Step-1 distinction `EXHAUSTIVE_COMPONENT_LIST != EXHAUSTIVE_COMPOSITION_SPACE` already prevents `SYNTHESIS_INFEASIBLE` from being inferred.

---

## SYN-BND-DRAFT-016 — Formation Clause VII formal composition mistaken for domain assembly legitimacy

### Attack

Post-Stage-VI terms admit a finite formal composition under Formation Clause VII, but the domain-level parts have incompatible physical/logical interfaces.

The attack asserts that the existence of the Formation-side finite composition proves substantive assembly legitimacy.

### Verdict

```text
PRESERVED_NO_REFINEMENT
```

The Step-1 source discipline already separates formal Formation composition from domain Synthesis legitimacy and requires an explicit domain composition rule/bridge.

---

## 4. Aggregate result / 종합 결과

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

The 16 attacks do not force Synthesis to merge with Design, Transformation, Aggregation, or Optimization.
They do reveal four missing explicit interface obligations.

## 5. Required non-breaking refinements / 필요한 비파괴적 보강

### R1 — Composition-law and grouping profile

Add:

```text
COMPOSITION_LAW_PROFILE:
GROUPING_OR_PARENTHESIZATION_POLICY:
```

Only supplied laws may be recorded, including when relevant:

```text
commutative / noncommutative / unspecified
associative / nonassociative / unspecified
identity rule supplied / not supplied
idempotence rule supplied / not supplied
other domain composition law
```

Absence of a supplied law must not be converted into a default algebraic assumption.

### R2 — Composition equivalence / canonicalization

Add:

```text
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
```

Material distinctness and `UNIQUE_SYNTHESIZED_TARGET` are judged at `TARGET_RESOLUTION` under this prelocked rule, not by candidate IDs or syntax trees alone.

### R3 — Residual obligations for partial synthesis

Add:

```text
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS:
```

For `PARTIAL_SYNTHESIS`, record unresolved interfaces, omitted parts, unresolved prerequisites, and downstream completion obligations.

### R4 — Static composition versus assembly-process scope

Add:

```text
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
```

Suggested values:

```text
not_claimed
static_order_only
time_resolved_sequence_supplied
dynamic_process_model_supplied
```

A static composition verdict must not be promoted to temporal assembly feasibility.
When time-resolved sequence or transition behavior matters, Dynamics or an explicit domain process model must be activated.

## 6. Nonconformance additions / 비준수 후보 추가

Add to the future protocol pressure set:

```text
UNDECLARED_GROUPING_OR_PARENTHESIZATION_ASSUMPTION
UNDECLARED_COMPOSITION_EQUIVALENCE
PARTIAL_SYNTHESIS_RESIDUAL_OMISSION
STATIC_COMPOSABILITY_PROMOTED_TO_PROCESS_FEASIBILITY
```

The existing classes for unjustified associativity/commutativity remain.

## 7. Stable Step-2 boundary conclusion / 2단계 안정 결론

The Step-1 method identity survives the attack.
The required changes are interface-explicitness refinements rather than method redefinition.

Effective pre-protocol Synthesis interface after Step 2:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

The next stage is to freeze the first executable `Synthesis Protocol v0.1` from that effective interface.
