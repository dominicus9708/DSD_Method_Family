# DSD Comparison Boundary Counterexamples v0.1-draft / DSD 비교론 경계 반례 초안

Status: **planning-stage boundary attack / not direct evidence**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Source draft under attack: `TASK_INTERFACE_v0.1-draft.md`

## 1. Purpose / 목적

Pressure-test the Step-1 Comparison interface before any executable protocol is frozen.

These attacks ask whether the current draft can keep structural comparison separate from aggregate equality, arbitrary map choice, Transformation, Classification, Audit, and Lineage claims.

```text
PRE_PROTOCOL_BOUNDARY_ATTACK
!= DIRECT_COMPARISON_PILOT
```

A case PASS or FAIL here does not decide method survival, merger, absorption, or deletion.

## 2. Summary / 요약

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

Four non-breaking refinement groups were actually forced:

```text
R1 MAP_PROPERTY_REQUIREMENT_PROFILE
   REVERSE_DIRECTION_OR_INVERSE_POLICY

R2 COMPARISON_ELEMENT_COVERAGE
   CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL

R3 PRECOMPARISON_TRANSFORMATION_POLICY
   REPRESENTATION_PROVENANCE

R4 LINEAGE_IDENTITY_CLAIM_POLICY
   LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

The Step-1 draft is preserved unchanged. These refinements belong in a separate amendment and later executable protocol.

---

## 3. Boundary attacks / 경계 공격

### CMP-BND-DRAFT-001 — equal aggregate, different structure

Fixture:

```text
Subject A: support {a1,a2}, relation a1->a2
Subject B: support {b1,b2}, relation b2->b1
Aggregate readout of both: 2
```

Attack: infer strict structural equivalence from equal aggregate.

Correct result:

```text
AGGREGATE_READOUT_COMPARISON_RESULT: equal
RELATION_PRESERVATION_RESULT: failed under direct label-independent orientation rule
STRICT_EQUIVALENCE: not established
```

Outcome: **preserved without refinement**.

Reason: the draft already separates aggregate readout from structural equivalence and records aggregate collision independently.

---

### CMP-BND-DRAFT-002 — one failed map, another viable map

Fixture:

```text
Map family F = {f1,f2}
f1 tested -> fails relation preservation
f2 untested -> admissible map candidate remains
MAP_FAMILY_COVERAGE: non_exhaustive
```

Attack: convert `f1` failure into global noncorrespondence.

Correct result:

```text
GLOBAL_NONCORRESPONDENCE: not established
REQUESTED_CLOSURE: underdetermined
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-003 — injective embedding falsely upgraded to strict equivalence

Fixture:

```text
A has two nodes.
B has three nodes.
f: A -> B is injective and relation-preserving on A.
No surjectivity or inverse-equivalence condition is satisfied.
```

Attack: infer `STRICT_EQUIVALENT` from one successful embedding.

Correct result:

```text
EMBEDDING: established
STRICT_EQUIVALENCE: not established
```

Outcome: **preserved with non-breaking refinement R1**.

Gap exposed: the candidate record mentions injectivity/surjectivity, but the task interface does not yet explicitly lock which map properties are required for the claimed output. Add `MAP_PROPERTY_REQUIREMENT_PROFILE`. If bidirectional/inverse behavior matters, lock `REVERSE_DIRECTION_OR_INVERSE_POLICY` rather than infer it.

---

### CMP-BND-DRAFT-004 — common label, different semantic role

Fixture:

```text
A.feature label = "mass" meaning physical inertial mass
B.feature label = "mass" meaning database field name for stored file size
No semantic bridge is supplied.
```

Attack: match coordinates solely because the labels coincide.

Correct result:

```text
COMMON_LABEL: yes
COMMON_SEMANTIC_COORDINATE: not established
DIRECT_FEATURE_MATCH: blocked or unresolved for the requested semantic comparison
```

Outcome: **preserved without refinement**.

The existing comparison-domain and feature-matching rules already require more than label equality.

---

### CMP-BND-DRAFT-005 — partial element coverage falsely upgraded to global equivalence

Fixture:

```text
Target-resolution elements: {x,y,z,r_xy}
Compared: {x,y}
Preserved: {x,y}
Untested: {z,r_xy}
```

Attack: infer global/direct equivalence because every tested element matches.

Correct result:

```text
PARTIAL_CORRESPONDENCE: supported
GLOBAL_EQUIVALENCE: not established
```

Outcome: **preserved with non-breaking refinement R2**.

Gap exposed: map-family coverage is not the same as coverage of claim-relevant coordinates/relations/properties. Add `COMPARISON_ELEMENT_COVERAGE` and an output-level `CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL`.

```text
MAP_FAMILY_COVERAGE
!= COMPARISON_ELEMENT_COVERAGE
```

---

### CMP-BND-DRAFT-006 — encoded correspondence mislabeled as direct

Fixture:

```text
A encodes state as {0,1}
B encodes same declared states as {OFF,ON}
Supplied bridge e: 0<->OFF, 1<->ON
No direct literal-coordinate equality exists.
```

Attack: call the relation `DIRECT_CORRESPONDENCE` after applying the encoding bridge.

Correct result:

```text
ENCODING_OR_BRIDGE_USED: e
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-007 — first observed difference falsely labeled first branch

Fixture:

```text
Ordered claim-relevant stages: S1,S2,S3,S4
Traversal inspects S4 first and finds a difference.
S2 and S3 have not yet been closed.
```

Attack: report S4 as `FIRST_BRANCH_POINT` merely because it is the first difference encountered.

Correct result:

```text
S4_DIFFERENCE: supported
FIRST_BRANCH_AT_S4: not established
FIRST_BRANCH_RESULT: underdetermined
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-008 — non-exhaustive map family used for false closure

Fixture:

```text
Candidate map family declared non_exhaustive.
All two tested maps fail.
Unsearched maps remain possible by task definition.
```

Attack: infer `NONCORRESPONDENCE` globally.

Correct result:

```text
TESTED_MAPS_FAILED: yes
GLOBAL_NONCORRESPONDENCE: not established
TERMINAL: COMPARISON_UNDERDETERMINED for global closure request
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-009 — hidden Transformation used to manufacture comparability

Fixture:

```text
A supplied in representation RA.
B supplied in representation RB.
No bridge/transformation from RB to RA is supplied.
Evaluator silently normalizes B into RA and then compares.
```

Attack: treat the invented normalization as an internal Comparison operation.

Correct result:

```text
COMPARISON: cannot claim the transformed comparison without supplied transformation/bridge provenance
HANDOFF: Transformation required if such conversion is to be performed
```

Outcome: **preserved with non-breaking refinement R3**.

Gap exposed: `ENCODING_OR_BRIDGE_RULE` says what bridge exists but does not explicitly distinguish a pre-supplied transformed representation from a transformation invented during Comparison. Add:

```text
PRECOMPARISON_TRANSFORMATION_POLICY
REPRESENTATION_PROVENANCE
```

---

### CMP-BND-DRAFT-010 — Classification label substituted for relation comparison

Fixture:

```text
A.class = C
B.class = C
Class C is broad and admits structurally different members.
No structural correspondence has been evaluated.
```

Attack: infer direct correspondence or equivalence from shared class membership.

Correct result:

```text
SHARED_CLASS_LABEL: yes
STRUCTURAL_CORRESPONDENCE: not established
```

Outcome: **preserved without refinement**.

Classification may be an input annotation but cannot replace Comparison's map/preservation operation.

---

### CMP-BND-DRAFT-011 — hidden Audit turns comparison into verdict validation

Fixture:

```text
Record A = prior process output
Record B = expected/reference output
Task asks only to compare A and B.
Evaluator additionally declares the prior process conformant/nonconformant.
```

Attack: absorb Audit judgment into Comparison.

Correct result:

```text
Comparison may report agreement/divergence of A and B.
Process/verdict conformance remains an Audit handoff.
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-012 — dynamic similarity falsely upgraded to lineage identity

Fixture:

```text
Trajectory A(t) and B(t) are identical over the observed window.
They were independently initialized and no successor/identity chain is supplied.
```

Attack: infer shared lineage or object identity from dynamic similarity.

Correct result:

```text
DYNAMIC_SIMILARITY: supported within observed scope
SHARED_LINEAGE_OR_IDENTITY: not established
```

Outcome: **preserved with non-breaking refinement R4**.

Gap exposed: `DYNAMIC_LINEAGE_SCOPE` is too compact to state whether lineage claims are prohibited, externally supplied, or handed off. Add:

```text
LINEAGE_IDENTITY_CLAIM_POLICY
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

---

### CMP-BND-DRAFT-013 — aggregate collision with different support decomposition

Fixture:

```text
A terms: 1 + 1 + 2 = 4
B terms: 4 = 4
Aggregate readout equal.
Support/decomposition multiplicity differs.
```

Attack: reconstruct common support/decomposition from equal aggregate.

Correct result:

```text
AGGREGATE_EQUAL: yes
SUPPORT_OR_DECOMPOSITION_EQUAL: not established
STRUCTURAL_EQUIVALENCE: not established without injective reconstruction condition
```

Outcome: **preserved without refinement**.

---

### CMP-BND-DRAFT-014 — direction-sensitive map falsely treated as symmetric

Fixture:

```text
f: A -> B is an injective structure-preserving map.
No map B -> A satisfying the required criterion is supplied or established.
Task requests a symmetric equivalence claim.
```

Attack: infer the reverse direction from the forward success.

Correct result:

```text
FORWARD_CORRESPONDENCE: supported
REVERSE_CORRESPONDENCE: not established
SYMMETRIC_EQUIVALENCE: not established
```

Outcome: **preserved with non-breaking refinement R1**.

The draft has `COMPARISON_DIRECTIONALITY` and `MAP_DIRECTION`, but an explicit `REVERSE_DIRECTION_OR_INVERSE_POLICY` is needed to prevent a forward-map success from silently closing a bidirectional claim.

---

### CMP-BND-DRAFT-015 — Property status collapse across subjects

Fixture:

```text
A.q = DEFINED_ZERO
B.q = APPLICABLE_BUT_UNDEFINED
```

Attack: coerce both into numeric zero and report equality.

Correct result:

```text
STATUS_DISTINCTION_RESULT: different
PROPERTY_VALUE_EQUALITY: not established
```

Outcome: **preserved without refinement**.

The existing subject-status and status-distinction fields are sufficient if executed literally.

---

### CMP-BND-DRAFT-016 — missing bridge treated as proven structural difference

Fixture:

```text
A and B are expressed in non-common domains.
Claim requires cross-domain semantic correspondence.
No comparison bridge is supplied.
```

Attack: infer noncorrespondence from inability to compare.

Correct result:

```text
NONCORRESPONDENCE: not established
TERMINAL: COMPARISON_BLOCKED when the bridge is claim-required before substantive comparison
```

Outcome: **preserved without refinement**.

```text
MISSING_COMPARISON_BRIDGE
!= PROVEN_STRUCTURAL_DIFFERENCE
```

---

## 4. Refinement result / 보강 결과

### R1 — map-property and reverse-direction lock

Required by `CMP-BND-DRAFT-003` and `014`.

```text
MAP_PROPERTY_REQUIREMENT_PROFILE
REVERSE_DIRECTION_OR_INVERSE_POLICY
```

Purpose:

- state whether injectivity, surjectivity, bijectivity, inverse preservation, isometry, homomorphism, embedding, or another map property is actually required by the requested claim;
- distinguish one-way correspondence from bidirectional equivalence;
- prevent embedding success from becoming strict equivalence by implication.

### R2 — element coverage separate from map-family coverage

Required by `CMP-BND-DRAFT-005`.

```text
COMPARISON_ELEMENT_COVERAGE
CLOSURE_REQUIREMENT_BY_OUTPUT_LEVEL
```

Purpose:

- record how much of the target-resolution coordinate/relation/property/status set has actually been compared;
- prevent exhaustive map search over only a partial feature subset from masquerading as global equivalence.

### R3 — precomparison transformation provenance

Required by `CMP-BND-DRAFT-009`.

```text
PRECOMPARISON_TRANSFORMATION_POLICY
REPRESENTATION_PROVENANCE
```

Suggested policy values:

```text
none_required
supplied_transformed_representation
external_transformation_handoff_required
transformation_not_permitted_in_comparison
```

Comparison may consume a supplied transformed representation but does not invent a transformation and then call it a comparison map.

### R4 — lineage-claim gate

Required by `CMP-BND-DRAFT-012`.

```text
LINEAGE_IDENTITY_CLAIM_POLICY
LINEAGE_EVIDENCE_SOURCE_OR_HANDOFF
```

Suggested policy values:

```text
not_claimed
supplied_external_lineage_record
lineage_method_handoff_required
```

Similarity of static or dynamic records alone does not establish lineage identity.

---

## 5. Boundary conclusion / 경계 결론

The Step-1 Comparison concept survives all 16 planning attacks without a fundamental rewrite.

```text
EXACT_METHOD_COLLAPSE_FOUND: 0
FUNDAMENTAL_TASK_INTERFACE_FAILURE: 0
```

The attacks do not prove Comparison irreducible or permanently independent. They only show that the current task form can be made executable without collapsing the method into Aggregation, Transformation, Classification, Audit, or Lineage by adding the four non-breaking refinement groups above.

## 6. Next / 다음

Create `TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` and then integrate the historical Step-1 draft plus Amendment 001 into the first executable `Comparison Protocol v0.1`.
