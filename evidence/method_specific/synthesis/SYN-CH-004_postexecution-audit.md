# SYN-CH-004 Postexecution Audit / 사후 실행 감사

Status: **CHALLENGE-DESIGN DEFECT FOUND — PASS VERDICT INVALIDATED**  
Date: **2026-09-10**  
Audited precommit: `1c77a0e293551b0d9e9b0a0ba7c6bddc4d78ed8e`  
Audited first result commit: `29730a54442a0c102148db97308ac859ff7fd4a5`

## 1. Defect

The frozen rule states:

```text
H4 readiness(Y) is defined
```

For frozen candidate:

```text
Q5 = (M1 ⊙ SRC) ⊙ SNK
```

the middle operand is `Y = SRC`.
The frozen component record for `SRC` contains no `readiness` assignment/status.
Therefore the precommitted expected failure set:

```text
Q5 -> {H2,H3}
```

is incomplete under the rule as written.
A strict full-failure-set execution must also flag H4 as unresolved/not-defined for the middle component. Under the intended binary definedness test, the correct claim-relevant result is:

```text
Q5 -> rejected {H2,H3,H4}
```

The first result commit attempted to preserve the precommitted expectation by introducing an uncommitted "role-specific" exception for H4. That exception does not exist in the frozen rule and is therefore invalid post-hoc reasoning.

## 2. Consequence

The Synthesis and competent baseline can still agree on the corrected Q5 failure set, so the underlying comparison may still suggest no measured gain. However the **precommitted challenge itself fails** because two exact expected checks were wrong:

```text
B5 Q5 DSD exact failure set = {H2,H3}      FAIL
C5 Q5 baseline exact failure set = {H2,H3} FAIL
```

All other precommitted checks remain satisfiable without changing the fixture.

Revised strict score:

```text
A. precommit integrity                 6 / 6 PASS
B. DSD candidate/closure               9 / 10 PASS
C. competent baseline                  8 / 9 PASS
D. gain checks                         7 / 7 PASS
E. scope discipline                    3 / 3 PASS

PRECOMMITTED_REQUIRED_CHECKS:         35
PASSED:                                33
FAILED:                                 2
CHALLENGE_VERDICT:                   FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
```

## 3. Evidence handling

```text
SYN-CH-004_DIRECT_ATTEMPT: preserved
SYN-CH-004_SUCCESSFUL_NO_GAIN_VALIDATION: no
SYN-CH-004_SUCCESSFUL_BASELINE_COMPARISON: no
PROTOCOL_FAILURE_INFERRED: no
PROTOCOL_REVISION_REQUIRED: no
```

The defect is in the test fixture, not in Synthesis Protocol v0.1.

The first result commit `29730a5` remains in Git history and must not be cited as a successful NO_GAIN validation without this audit.

## 4. Prospective correction rule

Do not repair `SYN-CH-004` by changing Q5 after seeing the result.
Use a new Case ID with a new precommit.

The corrected prospective case should either:

```text
1. give SRC an explicit readiness status and retain Q5 expected {H2,H3};
   or
2. preserve SRC without readiness and precommit Q5 as {H2,H3,H4}.
```

A new case may count as a successful NO_GAIN/baseline comparison only after its own immutable precommit and execution.
