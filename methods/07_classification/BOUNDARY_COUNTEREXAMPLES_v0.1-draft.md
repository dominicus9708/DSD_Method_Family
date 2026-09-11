# DSD Classification Boundary Counterexamples v0.1-draft / DSD 분류론 경계 반례 초안

Status: **planning-stage boundary attack / not direct evidence**  
Date: **2026-09-12**  
Method: **DSD Classification / DSD 분류론**  
Source draft under attack: `TASK_INTERFACE_v0.1-draft.md`

## 1. Purpose / 목적

Pressure-test the Classification Task Interface before an executable protocol is frozen.

```text
PRE_PROTOCOL_BOUNDARY_ATTACK
!= DIRECT_CLASSIFICATION_PILOT
```

The attacks are allowed to preserve the draft, force non-breaking amendments, expose blocking defects, or show method-boundary collapse. They are not a survival/merger/deletion vote.

## 2. Summary / 요약

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 12
PRESERVED_WITH_NONBREAKING_REFINEMENT: 6
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_CLASSIFICATION_PILOT_INCREMENT: 0
```

Six non-breaking refinement groups were forced:

```text
R1 CLASS_RELATION_SEMANTICS
   MUTUAL_EXCLUSION_RULES

R2 CLASS_SCHEMA_ID_AND_VERSION
   SCHEMA_COVERAGE_CLAIM
   CLOSED_SCHEMA_CLOSURE_EVIDENCE

R3 EQUIVALENCE_CLOSURE_REQUIREMENT

R4 GENERATED_CLASS_PROVENANCE
   CLASS_GENERATION_FREEZE_OR_MUTATION_POLICY
   GENERATION_STOP_OR_CLOSURE_POLICY

R5 CRITERION_COMPOSITION_RULE
   DECISION_RULE

R6 FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY
   BOUNDARY_DECISION_SEMANTICS
```

The historical v0.1 draft is preserved unchanged. Refinements are recorded in `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`.

---

## 3. Boundary attacks / 경계 공격

### CLS-BND-DRAFT-001 — overlapping but nonexclusive classes

Fixture:

```text
Class A: feature x >= 1
Class B: feature y = true
Subject s: x = 2, y = true
OVERLAP_ALLOWED: yes
```

Attack: force a single class or report conflict merely because two criteria are satisfied.

Correct result:

```text
MEMBERSHIP_STATUS: CLASSIFIED_MULTI
ASSIGNMENTS: {A,B}
CRITERION_CONFLICT: no
```

Outcome: **preserved without refinement**.

The draft already separates multiple membership from conflict when overlap semantics permit it.

---

### CLS-BND-DRAFT-002 — mutually exclusive classes with simultaneous criterion satisfaction

Fixture:

```text
Class A and Class B are intended to be mutually exclusive.
The supplied record satisfies both membership predicates because the criteria overlap at a boundary.
MULTI_LABEL_POLICY: single_only
```

Attack: silently choose A, silently choose B, or infer that the subject itself is contradictory.

Correct result:

```text
ASSIGNMENT: not yet terminal
STATUS: CRITERION_CONFLICT or BOUNDARY_CASE according to declared semantics
```

Outcome: **preserved with non-breaking refinement R1**.

Gap exposed: mutual-exclusion semantics are currently nested under the conditional multi-label section, but exclusive-class relations matter even when multiple membership is not permitted. Class-to-class relation semantics must be lockable independently of multi-label permission.

---

### CLS-BND-DRAFT-003 — open-world registry with no current match

Fixture:

```text
CLASS_SCHEMA_STATUS: open
Registered classes: {A,B,C}
Subject matches none of A,B,C.
New admissible classes may exist.
```

Attack: output universal nonmembership or `UNCLASSIFIED_WITHIN_DECLARED_SCHEMA` as if the class universe were closed.

Correct result:

```text
CURRENT_REGISTERED_MATCH: none
UNIVERSAL_NONMEMBERSHIP: not established
STATUS: UNDERDETERMINED or open-world no-current-match record
```

Outcome: **preserved with non-breaking refinement R2**.

The draft states the principle, but an executable protocol needs explicit schema identity/version and an explicit coverage/closure claim to know when `UNCLASSIFIED_WITHIN_DECLARED_SCHEMA` is lawful.

---

### CLS-BND-DRAFT-004 — missing feature coerced to negative feature

Fixture:

```text
Criterion for A requires feature q = false.
Subject record contains no q observation.
```

Attack: treat missing q as `q=false` and assign A.

Correct result:

```text
q: missing
q=false: not established
A membership: unresolved
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-005 — undefined coerced to defined zero

Fixture:

```text
Criterion for A requires q = 0.
Subject q status = APPLICABLE_BUT_UNDEFINED.
```

Attack: coerce undefined to numeric zero.

Correct result:

```text
DEFINED_ZERO: not established
A membership: unresolved or blocked according to policy
```

Outcome: **preserved without refinement**.

This preserves the DSD Property distinction between defined zero and undefined status.

---

### CLS-BND-DRAFT-006 — aggregate collision used as structural class identity

Fixture:

```text
Subject s1 components: 1 + 3 = 4
Subject s2 components: 2 + 2 = 4
Declared aggregate readout: 4
Structural class criterion also depends on component decomposition.
```

Attack: classify s1 and s2 identically from aggregate equality alone.

Correct result:

```text
AGGREGATE_EQUAL: yes
STRUCTURAL_CLASS_IDENTITY: not established
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-007 — misleading class label substituted for criterion

Fixture:

```text
Class label: "stable"
Formal criterion: residual <= epsilon during declared window
Subject is colloquially described as stable but fails the formal criterion.
```

Attack: assign the class from the label's ordinary-language meaning.

Correct result:

```text
LABEL_MATCH: irrelevant to formal membership
FORMAL_MEMBERSHIP: not satisfied
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-008 — equivalence class inferred from incomplete relation checks

Fixture:

```text
Subjects {a,b,c}
a~b established
b~c established
a~c untested
The claimed relation has not yet been shown transitive on the required domain.
```

Attack: emit one equivalence class {a,b,c} merely from the chain of observed pairwise matches.

Correct result:

```text
EQUIVALENCE_CLASS: not established
PAIRWISE_RECORDS: preserved
```

Outcome: **preserved with non-breaking refinement R3**.

The draft already requires reflexivity/symmetry/transitivity checks and coverage, but a protocol needs a frozen closure requirement specifying what must be closed before an equivalence-class claim becomes terminal.

---

### CLS-BND-DRAFT-009 — ordinal-looking labels treated as a proven hierarchy

Fixture:

```text
Labels: Level 1, Level 2, Level 3
No order relation is supplied.
```

Attack: infer `Level 1 < Level 2 < Level 3` mathematically or semantically.

Correct result:

```text
ORDER_RELATION: not established
HIERARCHY: not established
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-010 — temporal class change falsely upgraded to identity change

Fixture:

```text
Same tracked subject s:
t0 -> Class A
t1 -> Class B
Valid lineage record preserves subject identity.
```

Attack: infer formation-level identity replacement merely from class change.

Correct result:

```text
CLASS_TRANSITION: A -> B
FORMATION_IDENTITY_CHANGE: not implied
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-011 — identical current class with different lineage

Fixture:

```text
s1 and s2 are independently formed.
At t1 both satisfy Class C.
No common predecessor or lineage is supplied.
```

Attack: infer common lineage or identity from common current class.

Correct result:

```text
CURRENT_CLASS_MATCH: yes
SHARED_LINEAGE_OR_IDENTITY: not established
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-012 — subject outside classification universe

Fixture:

```text
CLASSIFICATION_UNIVERSE: finite software modules in repository R
Subject: external policy document P
```

Attack: call P unclassified within the schema rather than outside the task universe.

Correct result:

```text
STATUS: OUT_OF_SCOPE
UNCLASSIFIED_WITHIN_SCHEMA: not applicable
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-013 — class-generation policy mutates the schema during the run

Fixture:

```text
Initial classes: {A,B}
Generation policy permits new classes from unmatched structural signatures.
Subject s creates candidate class C.
Later subject t is evaluated after C exists.
```

Attack: treat the initial and post-generation schema as one immutable classification frame, or create classes without provenance and stop conditions.

Correct result:

```text
INITIAL_SCHEMA_VERSION != POST_GENERATION_SCHEMA_VERSION
GENERATED_CLASS_C: provenance required
```

Outcome: **preserved with non-breaking refinement R4**.

The draft permits class-generation policies but does not yet freeze mutation/version semantics, generation provenance, or the rule that closes/stops generation.

---

### CLS-BND-DRAFT-014 — criterion precedence exists but criterion composition is unspecified

Fixture:

```text
Class A criteria:
C1 = x > 0
C2 = y = true
Both have valid provenance.
No statement says whether A requires C1 AND C2, C1 OR C2, threshold voting, veto, or weighted score.
```

Attack: choose a membership result from the criterion list alone.

Correct result:

```text
A membership: UNDERDETERMINED
Reason: criterion-composition semantics absent
```

Outcome: **preserved with non-breaking refinement R5**.

`CRITERION_PRECEDENCE_OR_DEPENDENCY` is insufficient by itself. A classifier must freeze the logical/decision composition that turns criterion evaluations into membership.

---

### CLS-BND-DRAFT-015 — multi-method input loses source-method provenance

Fixture:

```text
Analysis output supplies feature f.
Comparison output supplies relation r.
Classification consumes f and r.
During handoff, source method/status metadata are removed.
```

Attack: treat f and r as native Classification findings.

Correct result:

```text
CLASSIFICATION may consume f and r only with source/output-status provenance preserved.
```

Outcome: **preserved without refinement**.

The draft already requires feature source/provenance and explicit method handoff discipline.

---

### CLS-BND-DRAFT-016 — competent baseline reaches the same justified classes

Fixture:

```text
Frozen task and criteria are given to both methods.
Competent non-DSD baseline and DSD Classification produce the same assignments,
boundary cases, and missing-information treatment with no claim-relevant loss.
```

Attack: call the DSD method superior merely because it used DSD descriptors.

Correct result:

```text
METHOD_RESULT: valid if internally correct
GAIN_RESULT: CLASSIFICATION_NO_GAIN
SUPERIORITY: not established
```

Outcome: **preserved without refinement**.

---

### CLS-BND-DRAFT-017 — threshold boundary under measurement or extraction uncertainty

Fixture:

```text
Class A criterion: x >= 10.0
Observed/extracted x: 10.0 ± 0.2
No tolerance or uncertainty rule is supplied.
```

Attack: force a terminal A/non-A result from the central value alone.

Correct result:

```text
TERMINAL_MEMBERSHIP: not justified
STATUS: BOUNDARY_CASE or UNDERDETERMINED according to frozen semantics
```

Outcome: **preserved with non-breaking refinement R6**.

`BOUNDARY_CASE_POLICY` identifies that boundaries exist but does not specify how uncertainty/tolerance around a decision surface is to be handled.

---

### CLS-BND-DRAFT-018 — closed-schema nonmembership claimed without coverage evidence

Fixture:

```text
CLASS_SCHEMA_STATUS: closed
Declared classes: {A,B,C}
Subject matches none under tested criteria.
No evidence establishes that {A,B,C} exhaust the task universe at the target resolution.
```

Attack: emit `UNCLASSIFIED_WITHIN_DECLARED_SCHEMA` as a closed-world conclusion solely because the schema was labelled closed.

Correct result:

```text
SCHEMA_LABEL_CLOSED: insufficient by itself
CLOSED_WORLD_NONMEMBERSHIP: not established without closure/coverage evidence
```

Outcome: **preserved with non-breaking refinement R2**.

A schema's declared status and evidence for its coverage are separate records.

---

## 4. Refinement result / 보강 결과

### R1 — class-relation semantics outside multi-label conditionality

```text
CLASS_RELATION_SEMANTICS
MUTUAL_EXCLUSION_RULES
```

Purpose: represent disjointness, overlap, subsumption, or other declared class-to-class relations even when multi-label assignment is forbidden.

### R2 — schema identity, version, coverage, and closure evidence

```text
CLASS_SCHEMA_ID_AND_VERSION
SCHEMA_COVERAGE_CLAIM
CLOSED_SCHEMA_CLOSURE_EVIDENCE
```

Purpose: distinguish a named/declared closed schema from a justified closed-world classification claim, and prevent open-world no-match from becoming universal nonmembership.

### R3 — equivalence closure requirement

```text
EQUIVALENCE_CLOSURE_REQUIREMENT
```

Purpose: state exactly what relation checks and subject/domain coverage must be complete before an equivalence-class output is terminal.

### R4 — generated-class provenance and schema mutation policy

```text
GENERATED_CLASS_PROVENANCE
CLASS_GENERATION_FREEZE_OR_MUTATION_POLICY
GENERATION_STOP_OR_CLOSURE_POLICY
```

Purpose: make class creation a traceable state change in the classification frame rather than a silent mutation.

### R5 — criterion composition and membership decision rule

```text
CRITERION_COMPOSITION_RULE
DECISION_RULE
```

Purpose: distinguish criterion provenance/dependency from the actual logic that produces membership, such as conjunction, disjunction, veto, threshold, weighted rule, or externally fixed decision procedure.

### R6 — uncertainty/tolerance and boundary semantics

```text
FEATURE_UNCERTAINTY_OR_TOLERANCE_POLICY
BOUNDARY_DECISION_SEMANTICS
```

Purpose: prevent measurements or derived features straddling a decision boundary from being forced into a class by arbitrary central-value choice.

## 5. Boundary conclusion / 경계 결론

The Classification task concept survives all 18 pre-protocol attacks without fundamental rewrite or collapse into Analysis, Comparison, Specification, Diagnosis, Aggregation, or Lineage.

```text
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
NONBREAKING_REFINEMENT_GROUPS: 6
```

This does not establish permanent independence, general superiority, or maturity. It only supports moving from the historical draft plus Amendment 001 to the first executable Classification Protocol v0.1.

## 6. Next / 다음

Create and freeze `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`, then integrate the historical v0.1 draft plus the amendment into `PROTOCOL_v0.1.md`.