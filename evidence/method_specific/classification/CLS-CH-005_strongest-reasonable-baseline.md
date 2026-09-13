# CLS-CH-005 Result / DSD 분류론 Strongest-Reasonable-Baseline 결과

Status: **EXECUTED — 60/60 PASS / NO_GAIN**  
Date: **2026-09-13**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`  
Precommit commit: `cbe3ef209dd1434e2b2f7973753071ef6087d31e`  
Precommit blob: `507f41efae1e0788ecc321f06239247269d10374`

## 1. Evidence identity

```text
CASE_ID: CLS-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Classification Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_TYPED_CLASSIFICATION_ENGINE
RESULT: PASS
CLASSIFICATION_METHOD_GAIN_STATUS: NO_GAIN
```

The immutable precommit was fetched from the precommit commit before execution. No task, fixture, schema version, generation rule, criterion-composition rule, aggregate rule, temporal rule, equivalence relation, baseline capability, gain criterion, or scoring item was changed after execution began.

---

## 2. R1 — generated class and versioned schema semantics

Initial v1 execution:

```text
schema: CLS005-R1-SCHEMA-v1
registered class: K-RED iff token == red
subject token: blue
K-RED: not satisfied
schema status: open
coverage: open_world_no_exhaustiveness_claim

PRE_GENERATION_ASSIGNMENT: none
PRE_GENERATION_MEMBERSHIP_STATUS: OPEN_WORLD_NO_CURRENT_MATCH
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

The frozen generation trigger is therefore satisfied. Generation ledger:

```text
GENERATED_CLASS_POLICY_ID: CLS005-R1-GEN-v1
TRIGGERING_SUBJECT: S-R1
TRIGGERING_TOKEN: blue
GENERATED_CLASS_ID: K-GEN-BLUE
GENERATED_CLASS_CRITERION: token == blue
PARENT_SCHEMA_ID_AND_VERSION: CLS005-R1-SCHEMA-v1
GENERATION_ORDER: G1
NEW_SCHEMA_ID_AND_VERSION: CLS005-R1-SCHEMA-v2
RETROACTIVITY: prohibited
```

Post-generation v2 execution:

```text
K-GEN-BLUE: satisfied
POST_GENERATION_ASSIGNMENT: K-GEN-BLUE
POST_GENERATION_MEMBERSHIP_STATUS: CLASSIFIED_SINGLE
RETROACTIVE_MEMBERSHIP_IN_v1: no
PARENT_SCHEMA_HISTORY_REWRITTEN: no
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution from the same records produced the same v1 no-match, the same deterministic generated class and v2 transition, and the same prospective-only membership.

Preserved distinction:

```text
PRE_GENERATION_SCHEMA != POST_GENERATION_SCHEMA
POST_GENERATION_MEMBERSHIP != RETROACTIVE_v1_MEMBERSHIP
```

No gain is established on R1.

---

## 3. R2 — composed criterion logic

Frozen subject:

```text
p=true
q=true
r=false
v=true
```

DSD execution:

```text
K-ELIGIBLE.base = p AND q = true
K-ELIGIBLE.veto = v = true
K-ELIGIBLE.membership = true AND NOT true = false

K-REVIEW.k_of_n(2 of {p,q,r})
  true_count = 2
  threshold = 2
  membership = true

CLASS_ASSIGNMENT: K-REVIEW
MEMBERSHIP_STATUS: CLASSIFIED_SINGLE
K-ELIGIBLE_AND_K-REVIEW_MULTI_ASSIGNMENT: no
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 applied the same conjunction, veto, and `k_of_n` rules and returned the same assignment and membership status.

Preserved distinction:

```text
CRITERION_LIST != MEMBERSHIP_LOGIC
BASE_CRITERION_SATISFACTION != FINAL_MEMBERSHIP_WHEN_VETO_APPLIES
```

No gain is established on R2.

---

## 4. R3 — aggregate collision and information loss

Frozen component records:

```text
A3 components: {0,10}
B3 components: {5,5}
aggregate_sum(A3)=10
aggregate_sum(B3)=10
```

DSD component-level classification:

```text
A3:
  exactly one component DEFINED_ZERO: yes
  other component DEFINED_NONZERO: yes
  K-ZERO-SUPPORT: satisfied
  K-EQUAL-SPLIT: not satisfied
  -> K-ZERO-SUPPORT / CLASSIFIED_SINGLE

B3:
  both components DEFINED_NONZERO: yes
  component values equal: yes
  K-ZERO-SUPPORT: not satisfied
  K-EQUAL-SPLIT: satisfied
  -> K-EQUAL-SPLIT / CLASSIFIED_SINGLE
```

Aggregate ledger:

```text
AGGREGATE_READOUT_EQUALITY: yes
A3 aggregate: 10
B3 aggregate: 10
A3 component pattern != B3 component pattern
AGGREGATE_INJECTIVE_ON_U-R3: no
RECONSTRUCTION_FROM_AGGREGATE_ALONE: unavailable
STRUCTURAL_CLASS_EQUALITY_FROM_AGGREGATE: no
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

The two-point collision itself is a witness of noninjectivity on the frozen fixture universe.

B1 retained the same component records, detected the same aggregate collision, refused aggregate-only reconstruction, and returned the same different classes.

Preserved distinction:

```text
AGGREGATE_EQUALITY != STRUCTURAL_CLASS_IDENTITY
SAME_READOUT != SAME_COMPONENT_PATTERN
```

No gain is established on R3.

---

## 5. R4 — history-dependent temporal classification

Frozen histories:

```text
A4: NORMAL -> ALARM -> NORMAL
B4: NORMAL -> NORMAL -> NORMAL
current(t2): NORMAL for both
LINEAGE_ID(A4)=LA
LINEAGE_ID(B4)=LB
LA != LB
```

DSD execution:

```text
A4:
  current NORMAL: yes
  earlier ALARM exists: yes
  K-RECOVERED: satisfied
  K-STABLE: not satisfied
  -> K-RECOVERED / CLASSIFIED_SINGLE

B4:
  current NORMAL: yes
  earlier ALARM exists: no
  all t0,t1,t2 NORMAL: yes
  K-RECOVERED: not satisfied
  K-STABLE: satisfied
  -> K-STABLE / CLASSIFIED_SINGLE
```

Temporal and lineage ledger:

```text
CURRENT_STATE_AT_t2: equal
TEMPORAL_CLASS_EQUALITY: no
CURRENT_STATE_EQUALITY_IMPLIES_TEMPORAL_CLASS_EQUALITY: no
CURRENT_STATE_EQUALITY_IMPLIES_LINEAGE_IDENTITY: no
LINEAGE_IDENTITY: no
LINEAGE_RELATION: DISTINCT_LINEAGES
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 used the same frozen histories and lineage records and returned the same two temporal classes without upgrading current-state equality into class or lineage identity.

Preserved distinction:

```text
CURRENT_CLASS_MATCH != TEMPORAL_LINEAGE_IDENTITY
CURRENT_STATE_COINCIDENCE != HISTORY_DEPENDENT_CLASS_EQUALITY
```

No gain is established on R4.

---

## 6. R5 — equivalence-class output with closure

Frozen relation:

```text
x ~ y iff key(x) == key(y)

key(E1)=A
key(E2)=A
key(E3)=B
key(E4)=B
```

DSD relation checks:

```text
REFLEXIVITY:
  E1~E1 yes
  E2~E2 yes
  E3~E3 yes
  E4~E4 yes
  -> PASS

SYMMETRY:
  equality of typed key is symmetric for every frozen ordered pair
  -> PASS

TRANSITIVITY:
  equality of typed key is transitive for every relevant frozen triple
  -> PASS

EQUIVALENCE_COVERAGE: exhaustive relative to {E1,E2,E3,E4}
```

Equivalence-class output:

```text
{E1,E2}
{E3,E4}
```

Non-authoritative similarity pressure:

```text
legacy_similarity(E1,E3)=0.99
SIMILARITY_IS_EQUIVALENCE_CRITERION: no
E1_EQUIVALENT_TO_E3: no
LEGACY_SIMILARITY_OVERRIDES_RELATION: no
CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 constructed the same two equivalence classes from the supplied relation, verified the same closure requirements, and did not use the legacy similarity record as a hidden criterion.

Preserved distinction:

```text
PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP
HIGH_SIMILARITY_SCORE != SUPPLIED_EQUIVALENCE_RELATION
```

No gain is established on R5.

---

## 7. DSD versus B1 task-level comparison

```text
SUBCASE  DSD MAIN RESULT                                      B1 MAIN RESULT
R1       v1 OPEN_WORLD_NO_CURRENT_MATCH                       same
         generate K-GEN-BLUE -> v2 CLASSIFIED_SINGLE          same
         no retroactive v1 membership                         same

R2       K-REVIEW / CLASSIFIED_SINGLE                         same
         K-ELIGIBLE vetoed                                    same

R3       A3 K-ZERO-SUPPORT / CLASSIFIED_SINGLE                same
         B3 K-EQUAL-SPLIT / CLASSIFIED_SINGLE                 same
         aggregate collision/noninjectivity preserved         same

R4       A4 K-RECOVERED / CLASSIFIED_SINGLE                   same
         B4 K-STABLE / CLASSIFIED_SINGLE                      same
         current-state and lineage distinctions preserved     same

R5       {E1,E2}, {E3,E4} equivalence classes                 same
         reflexive/symmetric/transitive closure PASS          same
```

B1 preserved enough schema, criterion, generation, aggregate, temporal, lineage, equivalence, and decision records to deterministically reconstruct every frozen result.

---

## 8. Gain evaluation

```text
G1 SCHEMA_VERSION_AND_GENERATION_GAIN: NOT_ESTABLISHED
  B1 preserved v1/v2 schema identity, deterministic generation provenance, and no-retroactivity.

G2 CRITERION_COMPOSITION_GAIN: NOT_ESTABLISHED
  B1 applied the same conjunction, veto, and k-of-n membership semantics.

G3 AGGREGATE_INFORMATION_LOSS_GAIN: NOT_ESTABLISHED
  B1 detected the same aggregate collision/noninjectivity and refused aggregate-only reconstruction.

G4 TEMPORAL_HISTORY_AND_LINEAGE_SEPARATION_GAIN: NOT_ESTABLISHED
  B1 used full history and kept current-state equality separate from temporal class and lineage.

G5 EQUIVALENCE_CLOSURE_GAIN: NOT_ESTABLISHED
  B1 used the supplied relation, checked reflexivity/symmetry/transitivity, and ignored non-authoritative similarity.

G6 STATUS_SCHEMA_AND_RELATION_TRACE_GAIN: NOT_ESTABLISHED
  B1 preserved the same typed status, schema-version, class-relation, and provenance records.

G7 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
  B1 preserved enough frozen records to reconstruct all five decisions and the R1 schema transition.
```

Therefore:

```text
CLASSIFICATION_METHOD_GAIN_STATUS: NO_GAIN
```

This is a successful strongest-reasonable-baseline comparison at constructed-evidence level. It is not a DSD superiority result.

---

## 9. Precommitted scoring

```text
A. immutable/fairness discipline       8 / 8 PASS
B. DSD execution                      18 / 18 PASS
C. B1 execution                       18 / 18 PASS
D. comparative gain                    9 / 9 PASS
E. scope/protocol pressure             7 / 7 PASS

PRECOMMITTED_REQUIRED_CHECKS:         60
PASSED:                                60
FAILED:                                 0
CHALLENGE_VERDICT:                   PASS
```

No scoring item was removed, weakened, or reinterpreted after execution.

---

## 10. Evidence increment

```text
DIRECT_CLASSIFICATION_PILOT_INCREMENT: +1
NO_GAIN_CLASSIFICATION_CASE_INCREMENT: +1
BASELINE_CLASSIFICATION_CASE_INCREMENT: +1
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION:
  established_at_constructed_evidence_level
```

Post-run state:

```text
DIRECT_CLASSIFICATION_PILOTS: 5
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 1
NO_GAIN_CLASSIFICATION_CASES: 2
BASELINE_CLASSIFICATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

---

## 11. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No Protocol-v0.1 contradiction or fixture defect appeared in the frozen tasks.

The strong baseline matching DSD is not a protocol defect: the protocol disciplines classification semantics and evidence handling but does not guarantee superiority over every equally informed competent classification engine.

---

## 12. Scope limits and registry discipline

This result establishes only the strongest-reasonable-baseline category at **constructed-evidence level**.

It does not establish:

```text
external applicability
reproducibility
independent validation
practical superiority
method maturity
permanent method independence
```

And:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

No method survival, merger, absorption, deletion, redundancy, or permanent-independence conclusion is drawn.

---

## 13. Next

Run the first external Classification application `CLS-APP-001` using a stable public source that supplies a real class schema or externally anchored class criterion. The external application must not invent both the domain categories and the evidence inside the project fixture. It should preserve source/version provenance and keep external-domain validity separate from DSD-internal protocol conformance.
