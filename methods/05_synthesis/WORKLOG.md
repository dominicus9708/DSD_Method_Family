# DSD Synthesis Worklog / DSD 합성론 작업 기록

## 2026-09-10 — Planning preparation and Step 1

Status: **planning started / Step 1 complete**

Locked project paths:

```text
methods/05_synthesis/
evidence/method_specific/synthesis/
```

Defined DSD Synthesis as:

```text
supplied parts + supplied composition rule
-> admissible whole/composition space
```

Created `TASK_INTERFACE_v0.1-draft.md` with component identity/status, composition-rule provenance, candidate basis/coverage, interface/prerequisites, property-lift discipline, retention/loss, formation effect, output levels, ledgers, handoffs, and reproducibility fields.

---

## 2026-09-10 — Step 2: pre-protocol boundary counterexamples

Created:

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md  d089b04
TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md d1f51b2
```

Result:

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

Required refinements:

```text
R1 COMPOSITION_LAW_PROFILE + GROUPING_OR_PARENTHESIZATION_POLICY
R2 COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
R3 RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
R4 ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

The Step-1 draft remained historical and was not rewritten.

---

## 2026-09-10 — Step 4: Protocol v0.1 establishment

Created `methods/05_synthesis/PROTOCOL_v0.1.md` at commit `8787b24`.

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Executable sequence: `S1-S17`. Protocol creation itself added no direct pilot.

---

## 2026-09-10 — Step 5: SYN-CH-001 positive direct challenge

```text
PRECOMMIT: 4eeba2aaa7e684460a5c824a62301b6e8ed89b77
RESULT: 71e5d5cfe519e7afbe2584b667354632d77e9c44
```

Result:

```text
K1,K2 -> admissible
K3 -> rejected {H3}
K4-K6 -> rejected {H2}
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

Evidence effect:

```text
DIRECT_SYNTHESIS_PILOTS: 1
POSITIVE_SYNTHESIS_CASES: 1
```

---

## 2026-09-10 — Step 6: SYN-CH-002 negative/failure challenge

```text
PRECOMMIT: 09fc616835880e28aabcb4e9b47182d620a0da30
RESULT: 7dac87c90e9cab4e082bdb66ed09cd8b6a53ed78
```

Three frozen subcases:

```text
I: exhaustive all rejected
   -> SYNTHESIS_INFEASIBLE / CONFORMANT / NOT_ASSESSED
U: non-exhaustive uniqueness closure
   -> SYNTHESIS_UNDERDETERMINED / CONFORMANT / NOT_ASSESSED
B: required composition rule unavailable
   -> SYNTHESIS_BLOCKED / CONFORMANT / NOT_ASSESSED
```

```text
SCORE: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Evidence effect:

```text
DIRECT_SYNTHESIS_PILOTS: 2
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
```

---

## 2026-09-10 — Step 7: SYN-CH-003 direct method-boundary challenge

Status: **third direct Protocol-v0.1 pilot complete / 46/46 PASS**

### Precommit

```text
evidence/method_specific/synthesis/SYN-CH-003_precommit.md
commit: 2eea8aea66c080785d04c8d70830e77b545b5a2e
blob: 8c31bab8cbe3868621520e92e04a1c522ea40bee
```

### Shared fixture

```text
S0 = (SRC ⊙ M0) ⊙ SNK
S1 = (SRC ⊙ M1) ⊙ SNK
ADMISSIBLE_FAMILY: {S0,S1}
```

Both targets are admissible under the frozen `R_CHAIN_3` rule. The challenge then adds four operations that are intentionally outside the Synthesis operation itself.

### Boundary results

```text
D — monitoring output gamma required, but no new component/connector supplied
    Synthesis family remains {S0,S1}
    -> DESIGN_REQUIRED
    no architecture fabricated

T — adjacency-matrix representation requested for S0
    Synthesis family remains {S0,S1}
    -> TRANSFORMATION_REQUIRED
    no transformed representation produced as Synthesis output

A — scalar sum of component readout weights requested
    Synthesis family remains {S0,S1}
    -> AGGREGATION_REQUIRED
    no scalar readout substituted for the synthesized whole

O — lower-cost admissible target requested
    cost(M0)=1, cost(M1)=3
    Synthesis family remains {S0,S1}
    -> OPTIMIZATION_REQUIRED
    S0 is not selected by Synthesis
```

Every Synthesis subcase retained:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

### Result record

```text
evidence/method_specific/synthesis/SYN-CH-003_method-boundary-separation.md
commit: cb55dbaf0cefcfb25cc09a12c8a24b5df3e4dc53
```

Scoring:

```text
PRECOMMITTED_REQUIRED_CHECKS: 46
PASSED: 46
FAILED: 0
CHALLENGE_VERDICT: PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

### Direct evidence effect

```text
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
BOUNDARY_SYNTHESIS_CASE_INCREMENT: +1
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

### Interpretation

The run directly preserves:

```text
SYNTHESIS_SUCCESS != MIXED_WORKFLOW_COMPLETION
SYNTHESIS_ADMISSIBLE_FAMILY != OPTIMIZED_SELECTION
SYNTHESIZED_WHOLE != AGGREGATE_READOUT
SYNTHESIZED_STRUCTURE != TRANSFORMED_REPRESENTATION
SUPPLIED_PARTS != DESIGN_LICENSE_TO_INVENT_MISSING_PARTS
```

### Next technical step

Separately precommit the first `NO_GAIN` challenge against a competent baseline receiving the same parts, rule, interfaces, candidate basis, coverage, and target resolution. The baseline must be strong enough that a `NO_GAIN` result is allowed.
