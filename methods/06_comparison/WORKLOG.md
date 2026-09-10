# DSD Comparison Worklog / DSD 비교론 작업 기록

## 2026-09-10 — Planning Step 1

Status: **planning started / Step 1 complete**

Method path:

```text
methods/06_comparison/
```

Direct-evidence path:

```text
evidence/method_specific/comparison/
```

Initial method form:

```text
supplied subjects
+ comparison scope/resolution
+ supplied map/correspondence family
+ preservation/equivalence criteria
-> correspondence/divergence profile
```

Created `TASK_INTERFACE_v0.1-draft.md`.

---

## 2026-09-10 — Planning Step 2: pre-protocol boundary attack

Created:

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md
  commit 37e1ffd925a0f7d7eca88dd12d42a30a53892f57

TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
  commit 131541069f62c481da3098a61446f58d47e31ca7
```

Result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_COMPARISON_PILOT_INCREMENT: 0
```

Forced refinements:

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

---

## 2026-09-10 — Planning Step 4: Protocol v0.1 freeze

Status: **first executable Comparison protocol established**

```text
methods/06_comparison/PROTOCOL_v0.1.md
commit a1700d960e0b41dfe32bf85b6334448d9104100d
```

Protocol v0.1 freezes a `C1-C20` executable sequence. Protocol creation adds no direct Comparison pilot.

---

## 2026-09-10 — Step 5: CMP-CH-001 positive direct challenge

Status: **40/40 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-001_precommit.md
commit 16c4b15f93d66299a2a3890f436e1aff0076713c
blob 1c87d4261022a07175796bce16e794f9d0c77f31
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-001_positive-direct-comparison.md
commit c601bd20d4d5fc6ba7dd5d4cb20b4a80f66ec880
```

Four frozen task instances were executed:

```text
T1 -> STRICT_EQUIVALENT
     bijection + forward/inverse relation preservation + Property-status preservation

T2 -> DIRECT_CORRESPONDENCE
     injective direct map with preserved mapped relation/status
     y2 outside image
     strict equivalence = no

T3 -> ENCODED_CORRESPONDENCE
     supplied bridge e: 0<->OFF, 1<->ON
     bridge bijective and relation/status preserving
     not relabeled DIRECT_CORRESPONDENCE

T4 -> aggregate readout equal (4=4)
     support cardinalities 3 vs 1
     no bijection under frozen strict structural family
     structural equivalence = no
     NONCORRESPONDENCE under frozen strict family
```

Three-ledger result for all four:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Precommitted score:

```text
A immutable/precommit discipline  8/8
B T1 strict-equivalence           8/8
C T2 weaker-direct                8/8
D T3 encoded                      8/8
E T4 aggregate-collision          8/8
TOTAL                            40/40 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 1
POSITIVE_COMPARISON_CASES: 1
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_SURVIVAL_OR_MERGER_DECISION_FROM_THIS_CASE: none
```

The challenge preserved:

```text
STRICT_EQUIVALENT != DIRECT_CORRESPONDENCE
DIRECT_CORRESPONDENCE != ENCODED_CORRESPONDENCE
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
INJECTIVE_DIRECT_CORRESPONDENCE != BIJECTIVE_EQUIVALENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
```

### Next

Separately precommit `CMP-CH-002` negative/failure challenge. It should distinguish `COMPARISON_UNDERDETERMINED`, `COMPARISON_BLOCKED`, and resolved `NONCORRESPONDENCE`, including incomplete map-family/element/reverse evidence and missing claim-required bridge cases.
