# 04. DSD Design / DSD 설계론

Status: **Protocol v0.1 / validation in progress**

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

## Method boundaries

- Specification may lock goals/constraints upstream.
- Design constructs or filters target/design space under those conditions.
- Synthesis combines admitted parts.
- Transformation records source-target preservation/loss.
- Optimization selects among already-admissible alternatives under an objective.
- Audit retraces a completed Design execution.
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

### Key accumulated results

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

`DES-CH-005`:

```text
B0_EXPLICIT_CONSTRAINT_MATRIX == DSD on frozen claim-relevant result
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
25/25 PASS
```

`DES-CH-006`:

```text
B1_TYPED_ADMISSIBILITY_TABLE
Formation + General Property
15 candidates
DESIGN_SPACE + UNIQUE_TARGET
G1-G5 all NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
54/54 PASS
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

`DES-CH-007` retraced `DES-APP-001` from immutable Git refs:

```text
Protocol v0.1 ref: b3d658c839dfe60b65efbc44abf874e257d4a0e2
DES-APP-001 precommit ref: 4847dbd1f5a38adb5d5c285b19ac41ebcfe86b96
historical result ref: 32a7842758be0cc179f996fdd8035d9683d31da9
```

Reconstructed candidate verdicts, rejection bases, `{W1,W2,W3}`, `DESIGN_ADMISSIBLE`, `CONFORMANT`, `NOT_ASSESSED`, external source/version, and bridge all matched the historical record.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
```

This establishes deterministic same-project retraceability only. It does not establish blinded or independent replication because the historical result was already known to the same project/evaluator.

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
NO_GAIN_VALIDATION_PASSES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_PASSES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 1
EXTERNAL_APPLICATION_PASSES: 1
INDEPENDENT_EVALUATOR_VALIDATION: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

All minimum evidence categories are now populated at least once, but this is not an automatic maturity grant.

## Development records

- Planning framework: [`PLANNING.md`](PLANNING.md)
- Protocol v0.1: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Task-interface draft: [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)
- Boundary counterexamples: [`BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md`](BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md)
- Boundary amendment 001: [`TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md`](TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md)
- Worklog: [`WORKLOG.md`](WORKLOG.md) — historical development log; current evidence README/Planning are the latest status sources.

## Next development step

Run a **DSD Audit maturity review** of the accumulated Design evidence.

The audit must explicitly discount common-evaluator/same-project dependence, preserve the `DES-CH-003` challenge-design failure, treat `NO_GAIN` evidence as valid non-superiority evidence rather than as method failure, and avoid automatic maturity promotion solely because the minimum evidence categories are now populated.
