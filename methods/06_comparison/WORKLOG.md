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

```text
PRECOMMIT: c852a688c3411c7d8568e2597262c4ec32a0355e
RESULT: ca2e91f6a73d36561e77f699c3b221ada0f97dfc
```

```text
N1 -> non-exhaustive map failure -> COMPARISON_UNDERDETERMINED
N2 -> partial Property/status coverage -> COMPARISON_UNDERDETERMINED
N3 -> missing required semantic bridge -> COMPARISON_BLOCKED
N4 -> forward success / inverse unverified -> COMPARISON_UNDERDETERMINED
N5 -> exhaustive all-map failure -> NONCORRESPONDENCE / COMPARISON_RESOLVED
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 2
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
PROTOCOL_REVISION_REQUIRED: no
```

---

## 2026-09-10 — Step 7: CMP-CH-003 direct method-boundary challenge

Status: **48/48 PASS**

```text
PRECOMMIT: 68d330bc43b78591be2ef2c197d6a177302789aa
RESULT: b4256d2a3c71d2a14ce9808668300ec3a879e646
```

```text
B1 Analysis -> visible STRICT_EQUIVALENT / RESOLVED + ANALYSIS_REQUIRED
B2 Classification -> visible STRICT_EQUIVALENT / RESOLVED + CLASSIFICATION_REQUIRED
B3 Transformation -> UNDETERMINED / BLOCKED + TRANSFORMATION_REQUIRED
B4 Audit -> resolved comparison profile + AUDIT_REQUIRED
B5 Provenance/Lineage -> snapshot STRICT_EQUIVALENT / RESOLVED; lineage not_established + PROVENANCE_LINEAGE_REQUIRED
```

Preserved method-boundary distinctions:

```text
COMPARISON_EQUIVALENCE != INTERNAL_DECOMPOSITION
COMPARISON_RELATION != TAXONOMY_ASSIGNMENT
COMPARISON_MAP != UNSUPPLIED_TRANSFORMATION
TRACE_DIFFERENCE != AUDIT_CONFORMANCE_VERDICT
STRUCTURAL_EQUIVALENCE != LINEAGE_IDENTITY
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 3
BOUNDARY_COMPARISON_CASES: 1
PROTOCOL_REVISION_REQUIRED: no
METHOD_SURVIVAL_OR_MERGER_DECISION_FROM_THIS_CASE: none
```

---

## 2026-09-11 — Step 8: CMP-CH-004 competent-baseline NO_GAIN challenge

Status: **50/50 PASS / NO_GAIN**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-004_precommit.md
commit 0d96d6ba83e25f2e14dba47c309cb74da7c71bad
blob 1c5917a6b854321605ce1d22e63201f5cadb3c7f
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-004_competent-baseline-no-gain.md
commit 4cacd55f73b2f4180ec8f11854d8dbe40974f536
```

Baseline:

```text
B0_TYPED_COMPARISON_LEDGER
```

B0 received the same claim-relevant subject, relation, Property/status, map, tested/untested, coverage, bridge, aggregate, equivalence, and terminal-rule records as DSD Comparison. It was explicitly allowed to preserve every scored distinction.

Execution:

```text
Q1 DSD = B0
  STRICT_EQUIVALENT / COMPARISON_RESOLVED

Q2 DSD = B0
  ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED

Q3 DSD = B0
  UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED

Q4 DSD = B0
  NONCORRESPONDENCE / COMPARISON_RESOLVED
  aggregate equal != structural equivalence

Q5 DSD = B0
  UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
```

Gain ledger:

```text
G1 RELATION_CLASS_SEPARATION_GAIN: NOT_ESTABLISHED
G2 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G3 COVERAGE_AND_CLOSURE_GAIN: NOT_ESTABLISHED
G4 BRIDGE_PROVENANCE_GAIN: NOT_ESTABLISHED
G5 AGGREGATE_COLLISION_GAIN: NOT_ESTABLISHED
G6 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

Precommitted score:

```text
A immutable/fairness                         8/8
B DSD task execution                       15/15
C B0 task execution                        15/15
D comparative gain                          8/8
E scope/protocol pressure                    4/4
TOTAL                                      50/50 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 4
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 1
BASELINE_COMPARISON_CASES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Interpretation:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
```

A competent non-DSD ledger equipped with the same frozen semantics matched DSD on all six comparison-gain dimensions. The result is preserved as an honest successful `NO_GAIN`.

### Next

Separately precommit `CMP-CH-005` strongest-reasonable-baseline comparison. Activate materially richer demands such as first-branch closure, forward/inverse directionality, partial-versus-global element coverage, representation/bridge provenance, and lineage-gated dynamic comparison. Give the baseline all claim-relevant information; another `NO_GAIN` remains acceptable.
