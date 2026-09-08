# DSD Design Task-Interface Boundary Amendment 001

Status: **effective non-breaking amendment to `TASK_INTERFACE_v0.1-draft.md`; still pre-protocol**

Date: **2026-09-08**

Source pressure test: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)

This amendment incorporates the two non-breaking refinements exposed by the first Design boundary attack. It does not create a new protocol version and does not count as direct Design validation.

## A1. Constraint provenance / 제약 출처

Add the following field to the well-formed task record and minimum valid execution ledger:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION:
```

Interpretation:

- hard constraints may come from the declared task owner, an upstream DSD Specification result, a domain standard, a theorem, a physical/technical limit, or another explicitly identified source;
- the Design record must retain enough provenance to distinguish a source-supplied hard constraint from a Design-internal convenience;
- Design itself must not silently promote a soft preference into a hard constraint after inspecting the candidate space;
- if a task owner, Specification process, or competent domain authority changes a preference into a hard requirement, that change is a new/upstream task revision and must be recorded before the revised Design selection is evaluated.

Therefore:

```text
SOFT_PREFERENCE
!= HARD_CONSTRAINT
```

and

```text
DESIGN-INTERNAL POST-HOC PROMOTION
= forbidden
```

Preference-based ranking among already admissible alternatives remains an Optimization operation unless the preference was legitimately converted into a hard constraint upstream before the Design verdict.

## A2. Auxiliary method and handoff ledger / 보조 방법·인계 장부

Add the following conditional field to the task/execution ledger:

```text
AUXILIARY_METHODS_OR_HANDOFFS:
```

Use it only when another method materially supplies a verdict used by Design.

Examples:

```text
DSD Specification -> locked requirement/status record -> DSD Design
DSD Synthesis -> composition-legitimacy record -> DSD Design admissibility
DSD Transformation -> preservation/loss record -> DSD Design admissibility
DSD Optimization <- admissible family from DSD Design
DSD Audit <- completed Design execution for retrace
```

Boundary rule:

```text
Design may consume a neighboring-method result.
Design does not absorb the neighboring method's operation, validation standard, failure state, or direct evidence.
```

### Candidate construction versus Synthesis

`D3 CANDIDATE CONSTRUCTION / ENUMERATION` may construct a symbolic or declared candidate description from the licensed candidate basis.

If a claim additionally requires that admitted parts are legitimately combined under a substantive parts-to-whole composition rule, that legitimacy claim is a **DSD Synthesis** result and must remain separately identifiable.

### Candidate evaluation versus Transformation

Design may declare a target-schema candidate.

If admissibility depends on whether a fixed source can be mapped to that candidate while preserving or losing declared distinctions, the preservation/loss claim is a **DSD Transformation** result and must remain separately identifiable.

### Admissible family versus Optimization

Design may filter candidates using declared hard constraints.

If several admissible alternatives are ranked or one is selected under an explicit objective, preference, utility, cost, or trade-off function, that ranking/selection is a **DSD Optimization** result.

## A3. Effective task record / 유효 과업 레코드

The effective pre-protocol Design task record is therefore the base `TASK_INTERFACE_v0.1-draft.md` record plus:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION:
AUXILIARY_METHODS_OR_HANDOFFS:
```

The first is required whenever claim-relevant hard constraints have an external/upstream source or could be confused with soft preferences. The second is conditional and should remain blank/not-used when no neighboring method materially contributes.

## A4. Effective minimum execution output / 유효 최소 실행 산출물

The minimum output ledger likewise adds:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION:
AUXILIARY_METHODS_OR_HANDOFFS:
```

This allows a later Audit to retrace both constraint provenance and cross-method verdict dependencies without treating the whole workflow as one merged method.

## A5. Amendment verdict / 개정 판정

```text
SOURCE_BOUNDARY_CASES: 8
NONBREAKING_REFINEMENTS: 2
METHOD_COLLAPSE_FOUND: 0
BASE_INTERFACE_REPLACED: no
EFFECTIVE_INTERFACE: TASK_INTERFACE_v0.1-draft + Amendment 001
PROTOCOL_STATUS: not yet established
DIRECT_EVIDENCE_INCREMENT: 0
NEXT_STEP: draft PROTOCOL_v0.1.md
```
