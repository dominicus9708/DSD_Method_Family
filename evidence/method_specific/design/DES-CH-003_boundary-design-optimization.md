# DES-CH-003 — Design / Optimization Boundary

Status: **FAIL AS PRECOMMITTED CHALLENGE — test-design defect exposed; no Design Protocol failure inferred**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Precommit: `DES-CH-003_precommit.md`, commit `0d1abcf`

## 1. Evidence claim / 증거 주장

This case was intended to test whether Design stops at admissibility while a downstream Optimization objective remains separate.

The precommit froze three candidates `O1-O3` whose only listed difference was:

```text
resource_cost(O1) = 30
resource_cost(O2) = 20
resource_cost(O3) = 10
```

However, the precommit also froze the Design target resolution as:

```text
TARGET_RESOLUTION:
  channel admission + readiness definedness
```

and explicitly placed `resource_cost` outside Design admissibility as downstream Optimization metadata.

That combination creates a challenge-design defect: `O1`, `O2`, and `O3` are not materially distinct **at the declared Design target resolution**.

The defect was discovered only after precommit and is therefore recorded rather than repaired in place.

---

## 2. Case S execution — DESIGN_SPACE

All three frozen candidate records satisfy the Design hard constraints:

```text
H1 q_primary admitted: pass for O1,O2,O3
H2 q_reserve admitted: pass for O1,O2,O3
H3 readiness(q_reserve) applicable and defined: pass for O1,O2,O3
```

The `resource_cost` values are not Design hard constraints and are not used to reject or rank candidates.

Therefore the candidate records can be preserved as the covered admissible records:

```text
ADMISSIBLE_CANDIDATE_RECORDS: {O1,O2,O3}
HIDDEN_OPTIMIZATION: no
RESOURCE_COST_PROMOTED_TO_HARD_CONSTRAINT: no
HANDOFF_TO_OPTIMIZATION: recorded, not executed
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Case S therefore preserves the intended Design/Optimization separation.

But the three records represent the same Design target state at the frozen target resolution because their only difference is outside that resolution.

---

## 3. Case U execution — UNIQUE_TARGET

The precommitted expectation was:

```text
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
```

That expectation is not justified by the frozen task record.

At the declared Design target resolution, all three candidate records have the same resolved Design state:

```text
q_primary: admitted
q_reserve: admitted
readiness(q_reserve): applicable and defined
```

The only listed difference is `resource_cost`, which the precommit itself excluded from Design target resolution and Design admissibility.

Therefore `O1-O3` cannot be used as three materially distinct Design targets to demonstrate underdetermination.

The correct protocol-respecting conclusion is:

```text
UNIQUE_TARGET_AT_DECLARED_DESIGN_RESOLUTION:
  not defeated by O1-O3, because O1-O3 are equivalent at that resolution

HIDDEN_OPTIMIZATION: no
UNSUPPORTED_UNIQUENESS_CLAIM: no objective-based uniqueness claim made
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The precommitted Case-U terminal-status requirement therefore fails as a **challenge-construction error**, not because Protocol v0.1 crossed into Optimization.

No post-hoc candidate distinction is added.
No target-resolution field is changed.
No new property is inserted into O1-O3.

---

## 4. Precommitted scoring result / 사전 고정 점수 결과

```text
CASE_S_REQUIRED_CHECKS:
  O1 Design-admissible: PASS
  O2 Design-admissible: PASS
  O3 Design-admissible: PASS
  returned Design family exactly {O1,O2,O3}: PASS as candidate records
  single best target selected by Design: PASS (none selected)
  resource_cost promoted to hard constraint: PASS (no)
  handoff to Optimization recorded: PASS
  Optimization executed inside Design case: PASS (no)
  terminal status = DESIGN_ADMISSIBLE: PASS
  protocol conformance = CONFORMANT: PASS

CASE_U_REQUIRED_CHECKS:
  O1 Design-admissible: PASS
  O2 Design-admissible: PASS
  O3 Design-admissible: PASS
  UNIQUE_TARGET=O3 claimed by Design: PASS (no)
  hidden objective tie-breaker used: PASS (no)
  terminal status = DESIGN_UNDERDETERMINED: FAIL
    reason: O1-O3 are not materially distinct at the frozen Design target resolution
  protocol conformance = CONFORMANT: PASS

CROSS_CASE_REQUIRED_CHECKS:
  Design admissibility and Optimization ranking remain distinct: PASS
  neighboring-method verdict absorption: PASS (none)
  method gain = NOT_ASSESSED in both cases: PASS
  no inactive DSD layer introduced: PASS

PRECOMMITTED_REQUIRED_CHECKS: 21
PASSED: 20
FAILED: 1
CHALLENGE_VERDICT: FAIL_AS_PRECOMMITTED_CHALLENGE
```

---

## 5. Failure classification / 실패 분류

```text
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
METHOD_BOUNDARY_COLLAPSE_FOUND: no
POST_HOC_REPAIR_PERFORMED: no
```

Specific defect:

```text
The challenge attempted to prove that multiple materially distinct Design targets survive,
but candidate differences existed only in downstream Optimization metadata that the
same precommit excluded from Design target resolution.
```

The failure is informative: Design uniqueness and underdetermination must be judged relative to the declared target resolution, not merely by candidate IDs or downstream objective metadata.

---

## 6. Prospective correction rule / 전향적 수정 규칙

A replacement boundary challenge must be a new case ID and must freeze, before evaluation:

1. at least two candidates that are materially distinct **inside** `TARGET_RESOLUTION`;
2. all such candidates as Design-admissible under the same hard constraints;
3. a separate downstream objective capable of ranking them;
4. the prohibition against using that objective as a Design hard constraint or uniqueness proof.

The historical `DES-CH-003` record is preserved unchanged.

---

## 7. Evidence verdict / 증거 판정

```text
CASE_ID: DES-CH-003
CASE_CLASS: boundary
CASE_ORIGIN: constructed_same_session
PROTOCOL: v0.1
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT for the boundary discipline actually exercised
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
BOUNDARY_VALIDATION_PASS_INCREMENT: +0
```

This failed challenge is retained as evidence of precommit discipline and of a target-resolution blind spot in the test design.
It does not count as a successful Design boundary validation.
