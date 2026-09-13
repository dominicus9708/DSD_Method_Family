# CLS-CH-005 Precommit / DSD 분류론 Strongest-Reasonable-Baseline Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-13**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Classification Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_TYPED_CLASSIFICATION_ENGINE
```

Purpose: test a materially richer Classification workload against a strong non-DSD classification engine that receives exactly the same claim-relevant records and is explicitly competent to preserve schema/version, criterion-composition, aggregate-information-loss, temporal, and equivalence-closure distinctions.

`NO_GAIN` is explicitly acceptable. This case does not define success as DSD superiority.

The previous competent baseline `B0_TYPED_RULE_CLASSIFIER` covered typed status, overlapping membership, open-world no-match, uncertainty boundary, and missing semantic bridge. `CLS-CH-005` is stronger because it adds schema mutation/versioning, nontrivial criterion composition, aggregate noninjectivity, history-dependent classification, and equivalence-class closure.

## 2. Frozen subcases

```text
R1 generated class with prospective schema-version transition and no retroactive membership
R2 composed criterion logic with veto plus k-of-n membership semantics
R3 aggregate collision with component-level classes and explicit information-loss control
R4 history-dependent temporal classification with current-state coincidence separated from history
R5 equivalence-class output with explicit relation closure and similarity non-authority
```

DSD uses the frozen ledgers:

```text
MEMBERSHIP_STATUS
CLASSIFICATION_PROTOCOL_CONFORMANCE
CLASSIFICATION_METHOD_GAIN_STATUS
```

B1 is evaluated for task correctness, distinction preservation, closure discipline, and deterministic retraceability, not for DSD-protocol conformance.

---

## 3. R1 — generated class and versioned schema semantics

Initial schema:

```text
TASK_ID: CLS005-R1
CLASS_SCHEMA_ID_AND_VERSION: CLS005-R1-SCHEMA-v1
CLASS_SCHEMA_STATUS: open
SCHEMA_COVERAGE_CLAIM: open_world_no_exhaustiveness_claim
TARGET_RESOLUTION: exact supplied categorical token
CLASS_RELATION_SEMANTICS: disjoint
```

Initial class:

```text
K-RED iff token == red
```

Subject:

```text
S-R1
  token_status: defined_nonzero categorical token
  token: blue
```

Generation policy:

```text
GENERATED_CLASS_POLICY_ID: CLS005-R1-GEN-v1
TRIGGER: admitted subject has a defined categorical token and no current registered class matches
GENERATION_RULE: create K-GEN[token] with criterion token == triggering token
SCHEMA_MUTATION: parent schema v1 -> new schema v2
GENERATED_CLASS_PROVENANCE: subject token + generation policy + generation order must be recorded
GENERATION_ORDER: G1
GENERATION_STOP_OR_CLOSURE_POLICY: stop after the single permitted generation in this task
RETROACTIVITY: prohibited
```

Frozen expected DSD and B1 sequence:

```text
PRE_GENERATION_SCHEMA: CLS005-R1-SCHEMA-v1
PRE_GENERATION_ASSIGNMENT: none
PRE_GENERATION_MEMBERSHIP_STATUS: OPEN_WORLD_NO_CURRENT_MATCH

GENERATED_CLASS: K-GEN-BLUE
NEW_SCHEMA_ID_AND_VERSION: CLS005-R1-SCHEMA-v2

POST_GENERATION_ASSIGNMENT: K-GEN-BLUE
POST_GENERATION_MEMBERSHIP_STATUS: CLASSIFIED_SINGLE

RETROACTIVE_MEMBERSHIP_IN_v1: no
PARENT_SCHEMA_HISTORY_REWRITTEN: no
```

This task distinguishes `PRE_GENERATION_SCHEMA != POST_GENERATION_SCHEMA` and tests whether a generated class is treated prospectively rather than as if it had always existed.

---

## 4. R2 — composed criterion logic

Schema:

```text
TASK_ID: CLS005-R2
CLASS_SCHEMA_ID_AND_VERSION: CLS005-R2-SCHEMA-v1
CLASS_SCHEMA_STATUS: externally_fixed
SCHEMA_COVERAGE_CLAIM: externally_fixed_scope_only
CLASS_RELATION_SEMANTICS: overlapping
OVERLAP_ALLOWED: yes
MUTUAL_EXCLUSION_RULES: none between K-ELIGIBLE and K-REVIEW
```

Class logic:

```text
K-ELIGIBLE:
  base = p AND q
  veto = v
  membership = base AND NOT veto

K-REVIEW:
  membership = k_of_n(2 of {p,q,r})
```

Subject:

```text
S-R2
  p: true
  q: true
  r: false
  v: true
```

Frozen expected DSD and B1 output:

```text
K-ELIGIBLE.base: satisfied
K-ELIGIBLE.veto: triggered
K-ELIGIBLE.membership: not_satisfied

K-REVIEW.k_of_n_count: 2/3
K-REVIEW.membership: satisfied

CLASS_ASSIGNMENT: K-REVIEW
MEMBERSHIP_STATUS: CLASSIFIED_SINGLE
K-ELIGIBLE_AND_K-REVIEW_MULTI_ASSIGNMENT: prohibited
CRITERION_LIST_AS_MEMBERSHIP_LOGIC: prohibited
```

This task pressures `CRITERION_LIST != MEMBERSHIP_LOGIC` and requires the frozen veto and `k_of_n` composition rules to be applied exactly.

---

## 5. R3 — aggregate collision and information loss

Schema:

```text
TASK_ID: CLS005-R3
CLASS_SCHEMA_ID_AND_VERSION: CLS005-R3-SCHEMA-v1
CLASS_SCHEMA_STATUS: closed
SCHEMA_COVERAGE_CLAIM: closed_world_claim relative to frozen fixture universe U-R3={A3,B3}
CLASS_RELATION_SEMANTICS: disjoint
TARGET_RESOLUTION: component-pattern class
```

Subjects:

```text
A3
  support: {a0,a1}
  component_values: {0,10}
  aggregate_sum: 10

B3
  support: {b0,b1}
  component_values: {5,5}
  aggregate_sum: 10
```

Classes:

```text
K-ZERO-SUPPORT iff exactly one supplied component is defined zero and the other is defined nonzero
K-EQUAL-SPLIT  iff both supplied components are defined nonzero and equal
```

Aggregate obligations:

```text
AGGREGATE_DEFINITION: sum of the two supplied component values
AGGREGATE_SUPPORT: exactly the two supplied components per subject
INFORMATION_LOSS_CHECK: required
COLLISION_POLICY: equal aggregate does not establish equal component pattern or equal class
INJECTIVITY_OR_RECONSTRUCTION_CLAIM: no; aggregate map is noninjective on U-R3 because A3 and B3 both map to 10
```

Frozen expected DSD and B1 output:

```text
A3 -> K-ZERO-SUPPORT / CLASSIFIED_SINGLE
B3 -> K-EQUAL-SPLIT  / CLASSIFIED_SINGLE
AGGREGATE_READOUT_EQUALITY: yes
STRUCTURAL_CLASS_EQUALITY_FROM_AGGREGATE: no
AGGREGATE_INJECTIVE_ON_U-R3: no
RECONSTRUCTION_FROM_AGGREGATE_ALONE: unavailable
```

This task directly pressures `AGGREGATE_EQUALITY != STRUCTURAL_CLASS_IDENTITY`.

---

## 6. R4 — history-dependent temporal classification

Time/order domain:

```text
TASK_ID: CLS005-R4
CLASS_SCHEMA_ID_AND_VERSION: CLS005-R4-SCHEMA-v1
CLASS_SCHEMA_STATUS: closed relative to frozen two-history fixture
SCHEMA_COVERAGE_CLAIM: closed_world_claim relative to U-R4={A4,B4}
TIME_OR_ORDER_DOMAIN: t0 < t1 < t2
REGULAR_EPOCH_SCOPE: t0..t2
CLASS_EVALUATION_TIME: t2
HISTORY_DEPENDENCE_POLICY: full frozen history required
```

Histories:

```text
A4:
  t0 NORMAL
  t1 ALARM
  t2 NORMAL
  LINEAGE_ID: LA

B4:
  t0 NORMAL
  t1 NORMAL
  t2 NORMAL
  LINEAGE_ID: LB

LA != LB
```

Classes:

```text
K-RECOVERED iff current(t2)==NORMAL AND at least one earlier frozen state == ALARM
K-STABLE    iff every frozen state t0,t1,t2 == NORMAL
```

Frozen expected DSD and B1 output:

```text
A4 -> K-RECOVERED / CLASSIFIED_SINGLE
B4 -> K-STABLE    / CLASSIFIED_SINGLE
CURRENT_STATE_AT_t2: equal (NORMAL)
CURRENT_STATE_EQUALITY_IMPLIES_TEMPORAL_CLASS_EQUALITY: no
CURRENT_STATE_EQUALITY_IMPLIES_LINEAGE_IDENTITY: no
LINEAGE_IDENTITY: no / DISTINCT_LINEAGES
```

This task separates current-state coincidence from history-dependent class and lineage identity.

---

## 7. R5 — equivalence-class output with closure

Task:

```text
TASK_ID: CLS005-R5
CLASS_SCHEMA_ID_AND_VERSION: CLS005-R5-SCHEMA-v1
CLAIMED_OUTPUT_LEVEL: EQUIVALENCE_CLASS_OUTPUT
EQUIVALENCE_CLOSURE_REQUIREMENT: exhaustive over frozen subject set
SUBJECT_SET: {E1,E2,E3,E4}
```

Typed keys:

```text
key(E1)=A
key(E2)=A
key(E3)=B
key(E4)=B
all key statuses: defined
```

Frozen equivalence relation:

```text
x ~ y iff key(x) == key(y)
```

Non-authoritative similarity side record:

```text
legacy_similarity(E1,E3)=0.99
SIMILARITY_IS_EQUIVALENCE_CRITERION: no
```

Required closure checks:

```text
REFLEXIVITY_CHECK_SCOPE: all 4 subjects
SYMMETRY_CHECK_SCOPE: all ordered distinct pairs
TRANSITIVITY_CHECK_SCOPE: all relevant triples over the 4-subject set
EQUIVALENCE_COVERAGE: exhaustive relative to frozen subject set and relation definition
```

Frozen expected DSD and B1 output:

```text
EQUIVALENCE_CLASSES:
  {E1,E2}
  {E3,E4}

REFLEXIVITY: PASS
SYMMETRY: PASS
TRANSITIVITY: PASS
LEGACY_SIMILARITY_OVERRIDES_RELATION: no
E1_EQUIVALENT_TO_E3: no
```

This task pressures `PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP` and requires explicit closure support for an equivalence-class claim.

---

## 8. Strong baseline freeze

Baseline identity:

```text
B1_STRONG_TYPED_CLASSIFICATION_ENGINE
```

B1 receives exactly the same:

```text
subject identities and all frozen evidence
feature values and typed feature/status records
class-schema identities and versions
schema status, coverage claims, and closure evidence
class relation, overlap, and exclusion semantics
criterion sources, prerequisites, composition rules, veto rules, k-of-n rules, and decision rules
generated-class trigger, generation rule, provenance, order, schema-mutation, and stop policy
aggregate definition, support, collision record, information-loss and injectivity/reconstruction obligations
time/order domain, history records, evaluation time, temporal-class rules, and lineage records
equivalence relation, closure scopes, exhaustive coverage requirement, and non-authoritative similarity record
terminal membership-status semantics
```

B1 is explicitly competent to:

```text
1. preserve prospective schema mutation and historical schema versions without retroactive class existence;
2. generate a class only through the supplied deterministic generation policy and record its provenance;
3. apply conjunction, negation/veto, and k-of-n criterion composition exactly as frozen;
4. distinguish equal aggregate readout from component structure, track noninjectivity, and refuse reconstruction from aggregate alone;
5. execute history-dependent classification using the full frozen time/order record and keep current-state coincidence separate from temporal class and lineage;
6. construct equivalence classes only from the supplied relation, verify reflexivity/symmetry/transitivity at the frozen scope, and ignore non-authoritative similarity;
7. preserve schema, criterion, feature, generation, aggregate, temporal, lineage, equivalence, and unresolved-state traces needed for deterministic retrace.
```

B1 must not be weakened after precommit.

---

## 9. Frozen gain criteria

```text
G1 SCHEMA_VERSION_AND_GENERATION_GAIN
G2 CRITERION_COMPOSITION_GAIN
G3 AGGREGATE_INFORMATION_LOSS_GAIN
G4 TEMPORAL_HISTORY_AND_LINEAGE_SEPARATION_GAIN
G5 EQUIVALENCE_CLOSURE_GAIN
G6 STATUS_SCHEMA_AND_RELATION_TRACE_GAIN
G7 TERMINAL_AND_RETRACEABILITY_GAIN
```

A criterion is `ESTABLISHED` only if DSD is correct and preserves a claim-relevant distinction that B1 loses despite receiving the same frozen information.

Decision rule:

```text
DSD incorrect or NONCONFORMANT -> FAIL
one or more G1-G7 established against correct B1 -> GAIN_ESTABLISHED
DSD and B1 both correct and B1 matches all seven dimensions -> NO_GAIN
fixture ambiguity/defect -> FAIL and correct prospectively under a new Case ID
```

No efficiency, terminology, elegance, pedagogical value, implementation effort, or external practical advantage is scored.

---

## 10. Expected task-level outputs

```text
R1 DSD = B1
  v1: no match / OPEN_WORLD_NO_CURRENT_MATCH
  generate K-GEN-BLUE -> schema v2
  v2: K-GEN-BLUE / CLASSIFIED_SINGLE
  no retroactive v1 membership

R2 DSD = B1
  K-ELIGIBLE blocked by veto
  K-REVIEW satisfied by 2-of-3
  K-REVIEW / CLASSIFIED_SINGLE

R3 DSD = B1
  A3 K-ZERO-SUPPORT / CLASSIFIED_SINGLE
  B3 K-EQUAL-SPLIT / CLASSIFIED_SINGLE
  equal aggregate != equal class; aggregate noninjective

R4 DSD = B1
  A4 K-RECOVERED / CLASSIFIED_SINGLE
  B4 K-STABLE / CLASSIFIED_SINGLE
  same current state != same temporal class or lineage

R5 DSD = B1
  equivalence classes {E1,E2}, {E3,E4}
  reflexive/symmetric/transitive closure PASS
  legacy similarity does not override relation
```

All DSD task results must be `CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed correctly.

---

## 11. Precommitted scoring

Total required checks: **60**.

```text
A. immutable/fairness discipline: 8
B. DSD execution: 18
C. B1 execution: 18
D. comparative gain: 9
E. scope/protocol pressure: 7
```

Detailed checks:

```text
A1 Protocol commit fixed
A2 R1-R5 frozen
A3 B1 identity and capabilities frozen
A4 same claim-relevant inputs frozen
A5 G1-G7 frozen
A6 scoring frozen
A7 baseline weakening prohibited
A8 no post-hoc task/schema/criterion/rule changes

B1-B5 exact R1-R5 main outputs
B6-B10 exact R1-R5 terminal/conformance results
B11 R1 v1 no-match, v2 generated membership, and no retroactivity preserved
B12 R2 veto and k-of-n composition applied exactly
B13 R3 aggregate collision, noninjectivity, and unavailable reconstruction preserved
B14 R3 A3/B3 remain different classes despite equal aggregate
B15 R4 current-state coincidence separated from temporal class
B16 R4 temporal class separated from lineage identity
B17 R5 equivalence closure plus similarity non-authority preserved
B18 all DSD task runs CONFORMANT

C1-C5 exact R1-R5 main outputs
C6-C10 exact R1-R5 terminal results
C11-C17 same seven claim-relevant discipline checks as B11-B17
C18 B1 full deterministic retrace record preserved

D1-D7 G1-G7 each NOT_ESTABLISHED if B1 matches
D8 final Classification method gain = NO_GAIN when D1-D7 all hold
D9 NO_GAIN not interpreted as method failure/merger/absorption/redundancy proof

E1 Protocol revision not required if no contradiction appears
E2 shared-core reopen not required if no contradiction appears
E3 strongest-reasonable-baseline claim limited to constructed-evidence level
E4 no external applicability claim
E5 no reproducibility/independent-validation claim
E6 no maturity promotion from this case alone
E7 no survival/merger/absorption/deletion/permanent-independence conclusion
```

Decision:

```text
60/60 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a fixture defect is discovered, preserve this Case ID as failed and correct prospectively under a new Case ID.

---

## 12. Evidence-count lock

Before execution:

```text
DIRECT_CLASSIFICATION_PILOTS: 4
POSITIVE_DIRECT_CHALLENGES: 1
NEGATIVE_FAILURE_CHALLENGES: 1
METHOD_BOUNDARY_CHALLENGES: 1
NO_GAIN_CLASSIFICATION_CASES: 1
BASELINE_CLASSIFICATION_CASES: 1
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: not established
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
```

A 60/60 PASS with `NO_GAIN` may add exactly:

```text
DIRECT_CLASSIFICATION_PILOT_INCREMENT: +1
NO_GAIN_CLASSIFICATION_CASE_INCREMENT: +1
BASELINE_CLASSIFICATION_CASE_INCREMENT: +1
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION:
  established_at_constructed_evidence_level
```

No external, reproducibility, independent-validation, maturity, survival, merger, absorption, deletion, redundancy, or permanent-independence claim follows automatically.
