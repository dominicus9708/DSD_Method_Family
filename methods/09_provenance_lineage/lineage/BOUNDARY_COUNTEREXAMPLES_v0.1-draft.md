# DSD Lineage Boundary Counterexamples v0.1 — pre-protocol attack record

Status: **18 pre-protocol boundary attacks completed**  
Date: **2026-09-23**  
Method: **Lineage / DSD 계보론**

Purpose: pressure the Lineage Task Interface before any executable protocol is frozen.

These are constructed internal counterexamples.

They are not external validation.

Task Interface under attack:

```text
TASK_INTERFACE_COMMIT:
  e233916530e8824427411d070ba0881160648618
```

## 1. Results summary

```text
BOUNDARY_ATTACKS_RUN: 18

PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_REQUIRED: yes
PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT: no
```

The five refinements do not change the method's task identity.

They make unresolved-state semantics, family coherence, and identity-bearing-family provenance executable rather than merely descriptive.

## 2. Attack ledger

### B1 — same label across a formation transition

Pre-transition channel c0 and post-transition channel c1 both display label pressure, but their Stage-VI channel identities differ.

No lineage relation is supplied.

Required:

```text
SAME_LABEL != SAME_ENTITY
SAME_LABEL != SUCCESSOR_RELATION
```

Outcome: **preserved by current draft**.

No successor identity is created by label continuity.

---

### B2 — temporal adjacency without lineage data

State S(t1) immediately follows S(t0) in time.

No channel/component lineage relation or canonical fixed-background condition is supplied.

Required:

```text
TEMPORAL_ADJACENCY != LINEAGE
```

Outcome: **preserved by current draft**.

---

### B3 — numerically similar states without admissible lineage

Two states have nearly equal component values and the same reduced aggregate.

No admissible lineage connects their identity-bearing components.

Required:

```text
NUMERICAL_SIMILARITY != LINEAGE_IDENTITY
AGGREGATE_EQUALITY != LINEAGE_IDENTITY
```

Outcome: **preserved by current draft**.

This matches the source Dynamics rule that numerical similarity does not create lineage.

---

### B4 — unequal aggregate with explicit lineage

A state changes value assignments enough that its reduced aggregate changes substantially.

A coherent component-lineage relation connects all declared identity-bearing components in both directions.

Required:

```text
AGGREGATE_INEQUALITY != LINEAGE_NONIDENTITY
```

Outcome: **preserved by current draft**.

The primary identity question remains lineage-connected succession.

---

### B5 — canonical lineage inside one fixed-background regular epoch

The task supplies one regular epoch with fixed inherited Stage-VI formation background and fixed admitted channel family C_L.

No formation-level transition occurs.

Required:

```text
canonical channel lineage:
  identity relation on C_L
```

Outcome: **preserved by current draft**.

The canonical result is channel-level only and does not silently establish component/state identity beyond the supplied conditions.

---

### B6 — formation transition with no explicit relation: absence versus blockage

A formation-level transition changes the admitted operational-channel set.

The evaluator can inspect the complete supplied transition packet and confirms that no cross-transition lineage relation is declared for candidate pair (c_s,c_t).

The current draft distinguishes LINEAGE_SUCCESSOR_NOT_ESTABLISHED from LINEAGE_SUCCESSOR_BLOCKED, but it does not yet prospectively lock the exact rule separating:

```text
evaluated absence of a successor declaration
from
inability to evaluate because required lineage data are unavailable
```

Required:

```text
EVALUABLE_ABSENCE -> NOT_ESTABLISHED
UNAVAILABLE_REQUIRED_INTERFACE -> BLOCKED
```

Outcome: **nonbreaking refinement required — R7**.

---

### B7 — one predecessor branches to two successors

```text
c -> c1
c -> c2
```

The post-transition formation admits both successors and the relation satisfies typing/coherence.

No unique-successor requirement is declared.

Required:

```text
BRANCHING != PROTOCOL_FAILURE
LINEAGE_RELATION != UNIQUE_SUCCESSOR_BY_DEFAULT
```

Outcome: **preserved by current draft**.

This is consistent with the finite-lineage-branching construction in the source Dynamics layer.

---

### B8 — two predecessors merge into one successor

```text
c1 -> c
c2 -> c
```

The relation is admissible and no bijection/cardinality rule is declared.

Required:

```text
MERGING != PROTOCOL_FAILURE
LINEAGE_RELATION != BIJECTION_BY_DEFAULT
```

Outcome: **preserved by current draft**.

---

### B9 — base branching lineage valid but unique-successor condition fails

The same B7 relation is used, but the application separately declares:

```text
UNIQUE_SUCCESSOR_REQUIREMENT: required
```

Required result:

```text
base lineage relation:
  remains established

unique-successor constraint:
  unsatisfied
```

The stronger constraint failure must not erase the underlying supported relation.

Outcome: **preserved by current draft**.

---

### B10 — type-incompatible component-lineage candidate

A candidate relation pairs a predecessor of declared component type property_record with a successor of unrelated type location_container, without a supplied type-changing bridge.

Required:

```text
TYPE_INCOMPATIBLE_PAIR != ADMISSIBLE_COMPONENT_LINEAGE
```

Outcome: **preserved by current draft**.

---

### B11 — multi-input property succession with one auxiliary lineage missing

A downstream property component at t0 depends on typed inputs a,b.

At t1, a candidate successor is supplied.

Lineage for input sort a is supplied, but the claim explicitly requires lineage of auxiliary sort b, and that required relation source is unavailable.

The draft already says auxiliary lineage may be required, but the terminal effect is not yet fully locked.

Required:

```text
REQUIRED_AUXILIARY_LINEAGE_UNAVAILABLE
  -> component/state lineage evaluation BLOCKED

not:
  silently ignore auxiliary input
  or
  downgrade it to ordinary NOT_ESTABLISHED
```

Outcome: **nonbreaking refinement required — R5 / R7**.

---

### B12 — predecessor-side state coverage fails

Identity-bearing family:

```text
I(s) = {a,b}
I(t) = {a1}
```

Only a -> a1 is supplied.

Component b has no successor in I(t).

Required:

```text
STATE_SUCCESSION_COVERAGE:
  fail predecessor-to-successor coverage

LINEAGE_CONNECTED_STATE_SUCCESSION:
  not established
```

Outcome: **preserved by current draft**.

---

### B13 — successor-side state coverage fails

Identity-bearing family:

```text
I(s) = {a}
I(t) = {a1,b1}
```

Only a -> a1 is supplied.

Component b1 has no predecessor in I(s).

Required:

```text
STATE_SUCCESSION_COVERAGE:
  fail successor-to-predecessor coverage

LINEAGE_CONNECTED_STATE_SUCCESSION:
  not established
```

Outcome: **preserved by current draft**.

---

### B14 — direct long-interval lineage contains additional admissible information

For r<s<t:

```text
L_r_s = {(a,b)}
L_s_t = {(b,c)}

composition:
  {(a,c)}

direct L_r_t:
  {(a,c),(a,d)}
```

The extra direct pair (a,d) is independently supplied.

Required:

```text
L_s_t o L_r_s subset L_r_t

COMPOSED_INTERMEDIATE_RELATION
  !=
DIRECT_LONG_INTERVAL_RELATION_BY_DEFAULT
```

Outcome: **preserved by current draft**.

Equality is not imposed.

---

### B15 — incoherent family: composition inclusion fails

For r<s<t:

```text
L_r_s contains (a,b)
L_s_t contains (b,c)
L_r_t omits (a,c)
```

Thus the supplied family violates:

```text
L_s_t o L_r_s subset L_r_t
```

The current draft requires the check but lacks a frozen family-level coherence status and exact terminal consequence.

Required prospective record:

```text
LINEAGE_FAMILY_COHERENCE_STATUS:
  INCOHERENT

coherent-family claim:
  not established
```

Outcome: **nonbreaking refinement required — R4**.

---

### B16 — invalid self-time relation

At time t, the supplied relation L_t_t omits one identity pair and includes one cross-component pair between distinct identifiers.

This violates the exact self-time identity requirement.

The draft requires the check but does not yet define a family-level status for this failure.

Required:

```text
SELF_TIME_RELATION != IDENTITY
  -> LINEAGE_FAMILY_COHERENCE_STATUS: INCOHERENT
```

Outcome: **nonbreaking refinement required — R4**.

---

### B17 — identity-bearing family selected after observing the preferred outcome

Two plausible nonempty component families could be used for a state-identity question.

One yields state succession; the other does not.

The evaluator chooses the first only after inspecting the lineage result.

The draft prohibits changing the family after seeing the outcome, but does not yet require identity/version/provenance records for the identity-bearing family itself.

Required prospective lock:

```text
IDENTITY_BEARING_FAMILY_ID
IDENTITY_BEARING_FAMILY_VERSION
IDENTITY_BEARING_FAMILY_PROVENANCE
SELECTION_RULE_OR_JUSTIFICATION
```

Outcome: **nonbreaking refinement required — R1 / R5**.

---

### B18 — neighboring-method and diagnostic substitution

A complete Tracking chain connects two artifacts.

A Reconstruction method proposes a missing historical relation.

A secondary identity diagnostic remains below its threshold.

No admissible Lineage relation or canonical fixed-background condition establishes the requested successor identity.

Required:

```text
TRACKING_LINK != LINEAGE_SUCCESSOR_DECISION
RECONSTRUCTED_LINEAGE_CANDIDATE != ESTABLISHED_LINEAGE
SECONDARY_DIAGNOSTIC != PRIMARY_IDENTITY_CRITERION
```

Outcome: **preserved by current draft**.

No neighboring method substitutes for the Lineage decision.

## 3. Refinement groups

The attack record retains the current interface structure but requires the following eight prospective protocol groups.

```text
R1 task / claim-level / time-direction / scope /
   identity-bearing-family selection lock

R2 predecessor/successor identity / type / formation /
   status discipline

R3 fixed-background canonical lineage versus
   transition-lineage discipline

R4 lineage-family coherence:
   self-time identity / composition inclusion /
   direct-long-interval separation

R5 component lineage / multi-input auxiliary lineage /
   identity-bearing-family coverage discipline

R6 branching / merging / optional uniqueness /
   bijection / cardinality separation

R7 established / explicitly-negated / not-established /
   ambiguous / conflicting / blocked / inapplicable /
   out-of-scope / underdetermined semantics

R8 neighboring-method handoffs and
   secondary-diagnostic non-substitution
```

## 4. Forced amendments

Boundary Amendment 001 must prospectively add or lock at least:

```text
A. identity-bearing-family identity/version/provenance and
   selection-rule record

B. explicit lineage-family coherence status family

C. exact semantics:
   evaluable absence -> NOT_ESTABLISHED
   unavailable required interface -> BLOCKED

D. required auxiliary-lineage absence rule for
   multi-input component/state claims

E. self-time/coherence failure consequence

F. task-terminal precedence for conflicting /
   underdetermined / blocked / established-partial-not-established
```

## 5. Boundary result

No attack requires collapsing Lineage into:

```text
Tracking
Dynamics
Reconstruction
Transformation
Comparison
Aggregation
Compression
Classification
Audit
```

No attack requires changing the source-derived core:

```text
succession is relation-valued
coherence uses self-time identity and composition inclusion
state succession uses bidirectional coverage of identity-bearing components
branching and merging are allowed
lineage identity is primary over aggregate/similarity/diagnostic substitutes
```

The historical Task Interface remains unchanged.

The refinements must be adopted prospectively through **Lineage Boundary Amendment 001** before Protocol v0.1 is frozen.

## 6. Current state

```text
DEDICATED_LINEAGE_PROTOCOL: not established
TASK_INTERFACE_DRAFT: v0.1 historical draft preserved

PRE_PROTOCOL_BOUNDARY_ATTACKS: 18
PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_001: not yet established

DIRECT_LINEAGE_PILOTS_ATTEMPTED: 0
BASELINE_LINEAGE_CASES: 0
NO_GAIN_LINEAGE_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_LINEAGE_APPLICATIONS: 0
INDEPENDENT_LINEAGE_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

LINEAGE_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_LINEAGE_EVIDENCE_STATUS: pre_protocol_boundary_attack_complete

PROTOCOL_REVISION_REQUIRED: not applicable pre-protocol
SHARED_CORE_REOPEN_REQUIRED: no
```

Next: establish **Lineage Task Interface Boundary Amendment 001** prospectively, then freeze executable Protocol v0.1.
