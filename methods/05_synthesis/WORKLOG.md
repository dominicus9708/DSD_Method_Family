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
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md   d089b04
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
Executable sequence: `S1-S17`. Protocol creation itself added no direct pilot.

---

## 2026-09-10 — Step 5: SYN-CH-001 positive direct challenge

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

Evidence effect: direct pilot 1, successful positive 1.

---

## 2026-09-10 — Step 6: SYN-CH-002 negative/failure challenge

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I -> SYNTHESIS_INFEASIBLE
U -> SYNTHESIS_UNDERDETERMINED
B -> SYNTHESIS_BLOCKED
SCORE: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
```

Evidence effect: direct pilot 2, successful negative/failure 1.

---

## 2026-09-10 — Step 7: SYN-CH-003 direct method-boundary challenge

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
BASE FAMILY: {S0,S1}
D -> DESIGN_REQUIRED
T -> TRANSFORMATION_REQUIRED
A -> AGGREGATION_REQUIRED
O -> OPTIMIZATION_REQUIRED
SCORE: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
```

Evidence effect: direct pilot 3, successful executable boundary 1.

---

## 2026-09-10 — Step 8A: SYN-CH-004 first NO_GAIN baseline attempt

Status: **challenge-design defect discovered after first execution record**

Precommit:

```text
evidence/method_specific/synthesis/SYN-CH-004_precommit.md
commit: 1c77a0e293551b0d9e9b0a0ba7c6bddc4d78ed8e
```

First result record:

```text
evidence/method_specific/synthesis/SYN-CH-004_no-gain-typed-chain-baseline.md
commit: 29730a54442a0c102148db97308ac859ff7fd4a5
```

Postexecution audit:

```text
evidence/method_specific/synthesis/SYN-CH-004_postexecution-audit.md
commit: fe55899cb08946d15e8d901d68f6097837b82b7d
```

Defect:

```text
Frozen H4: readiness(Y) is defined
Q5 = (M1 ⊙ SRC) ⊙ SNK
Y = SRC
SRC readiness record: absent in SYN-CH-004 precommit
Precommitted Q5 failure set: {H2,H3}
Strict failure set: {H2,H3,H4}
```

The first execution attempted an uncommitted role-specific H4 exception to preserve the expected answer. The postexecution audit rejected that move as invalid post-hoc reasoning.

Strict score:

```text
PRECOMMITTED_REQUIRED_CHECKS: 35
PASSED: 33
FAILED: 2
CHALLENGE_VERDICT: FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
PROTOCOL_REVISION_REQUIRED: no
```

Evidence handling:

```text
DIRECT_ATTEMPT: preserved
SUCCESSFUL_NO_GAIN_VALIDATION: no
SUCCESSFUL_BASELINE_COMPARISON: no
```

The predecessor is not rewritten into a pass.

---

## 2026-09-10 — Step 8B: SYN-CH-005 prospective corrected NO_GAIN challenge

Status: **corrected new Case ID / 37/37 PASS / NO_GAIN**

Precommit:

```text
evidence/method_specific/synthesis/SYN-CH-005_precommit.md
commit: 3c6f3239e817343223f44a308c3554deb11fad6e
```

Correction was frozen prospectively by giving `SRC` and `SNK` explicit readiness records before execution. No SYN-CH-004 record was edited to manufacture success.

Result:

```text
evidence/method_specific/synthesis/SYN-CH-005_no-gain-typed-chain-baseline.md
commit: f062d3f3f19a41c8bcb5d9b8b750cd48086fa215
```

Execution:

```text
R1 -> admissible / NONE
R2 -> admissible / NONE
R3 -> rejected / {H4}
R4 -> rejected / {H2}
R5 -> rejected / {H2,H3}

DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
```

Gain evaluation:

```text
G1 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
G2 FAILURE_TRACEABILITY_GAIN: NOT_ESTABLISHED
G3 COMPOSITION_CLOSURE_GAIN: NOT_ESTABLISHED
G4 TARGET_DISTINCTNESS_GAIN: NOT_ESTABLISHED
G5 RETRACEABILITY_GAIN: NOT_ESTABLISHED
SYNTHESIS_METHOD_GAIN_STATUS: NO_GAIN
```

Scoring:

```text
PRECOMMITTED_REQUIRED_CHECKS: 37
PASSED: 37
FAILED: 0
CHALLENGE_VERDICT: PASS
PROTOCOL_REVISION_REQUIRED: no
```

Evidence state after corrected Step 8:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

### Interpretation

The corrected case shows that DSD Synthesis can preserve an honest `NO_GAIN` result when a competent non-DSD typed checker receives the same raw information and matches every frozen comparison dimension. This is not evidence of DSD superiority.

### Next technical step

Build a separately precommitted broader strongest-reasonable-baseline comparison with a richer fixture that activates multiple Synthesis-specific dimensions simultaneously, preferably composition equivalence/grouping plus property-lift/redeclaration, relation retention, partial residual, or formation-effect distinctions. A second `NO_GAIN` result must remain acceptable.
