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

```text
PRECOMMIT: 0d96d6ba83e25f2e14dba47c309cb74da7c71bad
RESULT: 4cacd55f73b2f4180ec8f11854d8dbe40974f536
BASELINE: B0_TYPED_COMPARISON_LEDGER
```

```text
Q1 DSD = B0 -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
Q2 DSD = B0 -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
Q3 DSD = B0 -> UNDETERMINED / COMPARISON_UNDERDETERMINED
Q4 DSD = B0 -> NONCORRESPONDENCE / COMPARISON_RESOLVED
Q5 DSD = B0 -> UNDETERMINED / COMPARISON_BLOCKED
G1-G6: NOT_ESTABLISHED
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 4
NO_GAIN_COMPARISON_CASES: 1
BASELINE_COMPARISON_CASES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
```

---

## 2026-09-11 — Step 9: CMP-CH-005 strongest-reasonable-baseline comparison

Status: **60/60 PASS / NO_GAIN**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-005_precommit.md
commit ad542304a184303c7898ef8506afe167735683c5
blob cbefe2e0948a5b14343b8202fd2461192ce603df
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-005_strongest-reasonable-baseline.md
commit 61675b35e55a7ce288dc18a3afc773eeb135b180
```

Baseline:

```text
B1_STRONG_TYPED_COMPARISON_ENGINE
```

Activated simultaneously:

```text
earliest justified first branch + prior-stage closure
later re-convergence without branch erasure
forward direct correspondence vs bijective strict equivalence
surjectivity/inverse requirements
partial-vs-global comparison-element coverage
uncovered-element preservation
supplied representation bridge + provenance
encoded correspondence without direct relabeling
sampled dynamic trajectory equivalence
lineage identity gated by supplied lineage evidence
```

Execution:

```text
R1 DSD = B1
  PARTIAL_CORRESPONDENCE
  FIRST_BRANCH_POINT: S2
  earlier {S0,S1} closed
  COMPARISON_RESOLVED

R2 DSD = B1
  DIRECT_CORRESPONDENCE
  strict equivalence no
  target remainder {b2}
  COMPARISON_RESOLVED

R3 DSD = B1
  PARTIAL_CORRESPONDENCE
  uncovered element {mode(u1)<->mode(v1)}
  strict equivalence not_established
  COMPARISON_RESOLVED

R4 DSD = B1
  ENCODED_CORRESPONDENCE
  bridge provenance preserved
  COMPARISON_RESOLVED

R5 DSD = B1
  sampled-trajectory STRICT_EQUIVALENT
  lineage relation DISTINCT_LINEAGES
  lineage identity no
  COMPARISON_RESOLVED
```

Gain ledger:

```text
G1 FIRST_BRANCH_CLOSURE_GAIN: NOT_ESTABLISHED
G2 DIRECTIONAL_MAP_AND_INVERSE_GAIN: NOT_ESTABLISHED
G3 ELEMENT_COVERAGE_DISCIPLINE_GAIN: NOT_ESTABLISHED
G4 BRIDGE_AND_REPRESENTATION_PROVENANCE_GAIN: NOT_ESTABLISHED
G5 DYNAMIC_VS_LINEAGE_SEPARATION_GAIN: NOT_ESTABLISHED
G6 STATUS_AND_RELATION_TRACE_GAIN: NOT_ESTABLISHED
G7 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

Precommitted score:

```text
A immutable/fairness discipline       8/8
B DSD execution                      18/18
C B1 execution                       18/18
D comparative gain                    9/9
E scope/protocol pressure             7/7
TOTAL                                60/60 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_COMPARISON_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Interpretation discipline:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
```

### Next

Precommit and execute the first external Comparison application `CMP-APP-001` from a stable public source that supplies the compared records and a defensible comparison criterion. External source truth, Comparison conformance, and method gain remain separate ledgers.
