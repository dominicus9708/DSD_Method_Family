# 04. DSD Design / DSD 설계론

Status: **Protocol v0.1 / maturity: developing / validation in progress**

Task: construct or filter a target structure or admissible target family from declared goals, hard constraints, and an explicit candidate/construction basis rather than only analyze an already formed target.

Primary DSD interface: Formation for new structural targets or a locked inherited Stage-VI formation background for downstream target design. General Property, Static Aggregation, Dynamics, and optional specialization are activated only when the declared task actually requires them.

Typical sequence:
`task lock -> constraint-source lock -> candidate/construction-basis lock -> candidate family -> status-sensitive admissibility -> explicit domain/bridge checks -> admissible target family -> output-level check -> terminal Design status -> conformance ledger -> gain ledger`.

## Core ledgers

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE
  DESIGN_INFEASIBLE
  DESIGN_UNDERDETERMINED
  DESIGN_BLOCKED

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Maturity classification is a separate Audit-level decision and is not inferred from these three ledgers.

## Method boundaries

- Specification may lock goals/constraints upstream.
- Design constructs or filters target/design space under those conditions.
- Synthesis combines admitted parts.
- Transformation records source-target preservation/loss.
- Optimization selects among already-admissible alternatives under an objective.
- Audit retraces a completed Design execution and may separately review maturity.
- Material target distinctness is judged at `TARGET_RESOLUTION`.
- Soft preferences are not silently promoted into hard constraints.
- External authority remains separate from the Design verdict; a subset application does not become a full-standard conformance claim.
- A correct Design result does not imply method gain; `NO_GAIN` is a valid comparison result.

Boundary: DSD Design structures design decisions but does not replace domain design knowledge and does not assume a universal candidate generator.

## Current protocol and evidence

- Executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Direct evidence lane: [`../../evidence/method_specific/design/`](../../evidence/method_specific/design/)
- `DES-CH-001` — positive constructed challenge, PASS.
- `DES-CH-002` — negative/failure status challenge, PASS.
- `DES-CH-003` — first boundary attempt, preserved failed challenge design; no protocol failure inferred.
- `DES-CH-004` — corrected Design/Optimization boundary, PASS.
- `DES-CH-005` — first NO_GAIN baseline-equivalence case, PASS.
- `DES-CH-006` — broader strongest-reasonable-baseline comparison, PASS with NO_GAIN.
- `DES-APP-001` — first external-standard application using W3C WCAG 2.2 subset, PASS.
- `DES-CH-007` — first dedicated deterministic retrace, PASS.
- `DES-AUD-001` — first Design maturity audit, completed; classification `developing`, established promotion withheld.

## Key accumulated results

`DES-CH-002`:

```text
exhaustive + all rejected -> DESIGN_INFEASIBLE
non_exhaustive + no admissible target -> DESIGN_UNDERDETERMINED
missing required predecessor -> DESIGN_BLOCKED
```

`DES-CH-004`:

```text
Design space -> {C1,C2,C3}
UNIQUE_TARGET request -> DESIGN_UNDERDETERMINED
objective-based choice remains Optimization
```

`DES-CH-005` and `DES-CH-006`:

```text
competent baseline comparison
-> DSD protocol result remains valid
-> measured superiority not established
-> DESIGN_METHOD_GAIN_STATUS: NO_GAIN
```

`DES-APP-001`:

```text
W3C WCAG 2.2 Recommendation 2024-12-12
SC 1.4.3 / 2.5.3 / 2.5.8 subset
ADMISSIBLE_FAMILY: {W1,W2,W3}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
36/36 PASS
```

The application preserved best-practice versus hard-criterion status, did not invent target-size exceptions, preserved undefined/inapplicable/absent distinctions, and did not overclaim full WCAG conformance.

`DES-CH-007` retraced `DES-APP-001` from immutable Git refs and matched candidate verdicts, rejection bases, admissible family, three Design ledgers, external source/version, and bridge.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This does not establish blinded or independent replication.

## First maturity audit — DES-AUD-001

Audit ID:

```text
DSD-AUDIT-20260908-DESIGN-001
```

The audit froze 14 maturity axes and 24 audit-discipline checks before scoring.

```text
M1  dedicated executable protocol                  PASS
M2  positive/negative terminal discrimination      PASS
M3  neighboring-method boundary discrimination     PASS
M4  NO_GAIN preservation                           PASS
M5  reproducibility/retraceability                 CONDITIONAL_PASS
M6  external application origin                    PASS
M7  strongest-reasonable-baseline comparison       PASS
M8  external source fidelity and bridge discipline PASS
M9  established-level evidence breadth             INSUFFICIENT
M10 independent/practical-performance evidence     UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect     PRESENT_NONFATAL
M12 maximum-supported-claim discipline             PASS
M13 candidate/construction-basis discipline        PASS
M14 historical failure / anti-post-hoc preservation PASS
```

Final decision:

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The audit does not count as an additional Design pilot.

## Current evidence state

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 7
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 1
EXTERNAL_DOMAINS: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Protocol v0.1: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md)
- Maturity audit: `../../evidence/method_specific/design/DES-AUD-001_maturity-review.md`

## Next development step

Address the primary maturity blocker.

Run a **second external Design application in a materially different domain**, preferably using an externally supplied real artifact, candidate family, or independently generated option set rather than a project-authored fixture.

After external breadth increases, prepare a genuinely independent evaluator packet. Do not revise Protocol v0.1 merely to improve maturity optics; revise only if a new case exposes a genuine protocol defect.
