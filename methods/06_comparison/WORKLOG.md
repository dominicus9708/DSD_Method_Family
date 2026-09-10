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

Created `TASK_INTERFACE_v0.1-draft.md` with the initial Comparison task interface.

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

```text
methods/06_comparison/PROTOCOL_v0.1.md
commit a1700d960e0b41dfe32bf85b6334448d9104100d
```

Protocol v0.1 freezes the `C1-C20` executable sequence. Protocol creation adds no direct Comparison pilot.

---

## 2026-09-10 — Step 5: CMP-CH-001 positive direct challenge

Status: **40/40 PASS**

```text
PRECOMMIT: 16c4b15f93d66299a2a3890f436e1aff0076713c
RESULT: c601bd20d4d5fc6ba7dd5d4cb20b4a80f66ec880
```

```text
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE / strict equivalence no
T3 -> ENCODED_CORRESPONDENCE
T4 -> aggregate equal + structural NONCORRESPONDENCE
ALL TERMINAL: COMPARISON_RESOLVED
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 1
POSITIVE_COMPARISON_CASES: 1
```

---

## 2026-09-10 — Step 6: CMP-CH-002 negative/failure terminal distinction

Status: **48/48 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-002_precommit.md
commit c852a688c3411c7d8568e2597262c4ec32a0355e
blob caec1bb29368cd291abd77ae7789ecfe50ac4a98
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-002_negative-failure-terminal-distinction.md
commit ca2e91f6a73d36561e77f699c3b221ada0f97dfc
```

Five frozen tasks:

```text
N1 -> non-exhaustive map failure -> COMPARISON_UNDERDETERMINED
N2 -> partial Property/status coverage -> COMPARISON_UNDERDETERMINED
N3 -> missing required bridge -> COMPARISON_BLOCKED
N4 -> forward success / inverse unverified -> COMPARISON_UNDERDETERMINED
N5 -> exhaustive all-map failure -> NONCORRESPONDENCE / COMPARISON_RESOLVED
```

Precommitted score: **48/48 PASS**.

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 2
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
```

---

## 2026-09-10 — Step 7: CMP-CH-003 direct method-boundary challenge

Status: **48/48 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-003_precommit.md
commit 68d330bc43b78591be2ef2c197d6a177302789aa
blob 22c36cdfabe2518f577ddc05957844108b4f0de8
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-003_direct-method-boundary.md
commit b4256d2a3c71d2a14ce9808668300ec3a879e646
```

Five neighboring boundaries were frozen and executed:

```text
B1 Analysis
  visible structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
  no hidden decomposition invented
  HANDOFF: ANALYSIS_REQUIRED

B2 Classification
  visible structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
  no taxonomy assignment
  HANDOFF: CLASSIFICATION_REQUIRED

B3 Transformation
  raw representations differ and no transform/bridge is supplied
  no hidden conversion
  -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
  HANDOFF: TRANSFORMATION_REQUIRED

B4 Audit
  input equal, final result equal, process step different
  -> COMPARISON_PROFILE / COMPARISON_RESOLVED
  no Audit pass/fail verdict
  HANDOFF: AUDIT_REQUIRED

B5 Provenance/Lineage
  snapshot structure -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
  lineage identity -> not_established
  HANDOFF: PROVENANCE_LINEAGE_REQUIRED
```

Preserved method-boundary distinctions:

```text
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
COMPARISON_MAP != UNSUPPLIED_TRANSFORMATION
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
LEGITIMATE_COMPARISON_RESULT + NEIGHBORING_HANDOFF != METHOD_BOUNDARY_FAILURE
```

Three-ledger result:

```text
ALL CONFORMANCE: CONFORMANT
ALL GAIN: NOT_ASSESSED
B1,B2,B4,B5 TERMINAL: COMPARISON_RESOLVED
B3 TERMINAL: COMPARISON_BLOCKED
```

Precommitted score:

```text
A immutable/precommit discipline     8/8
B Analysis boundary                  8/8
C Classification boundary            8/8
D Transformation boundary            8/8
E Audit boundary                     8/8
F Provenance/Lineage boundary        8/8
TOTAL                               48/48 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 3
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_SURVIVAL_OR_MERGER_DECISION_FROM_THIS_CASE: none
```

### Next

Separately precommit `CMP-CH-004` competent-baseline challenge. Give the baseline the same claim-relevant records and capabilities needed to preserve typed status, map/element coverage, bridge provenance, relation classes, terminal distinctions, and retraceability. Do not weaken it to force a DSD advantage; `NO_GAIN` is an acceptable outcome.
