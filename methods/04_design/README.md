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
- `DES-APP-002` — second external application using NIST SP 800-63B-4 AAL2 route-form grammar, PASS 38/38.

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

`DES-APP-002`:

```text
NIST SP 800-63B-4, July 2025
AAL2 permitted authenticator route forms
source-supplied positive grammar + four source-grounded controls

N1-N11 -> admissible
N12 password only -> rejected
N13 SF cryptographic only -> rejected
N14 biometric alone -> rejected
N15 password + biometric -> rejected because source-permitted two-SF grammar requires a listed physical authenticator

ADMISSIBLE_FAMILY:
{N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}

DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
38/38 PASS
```

The case preserves:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!= NIST_AAL2_PERMITTED_FORM
```

and keeps verifier-level phishing-resistant-option requirements separate from individual route-form filtering. It does not infer replay resistance, approved cryptography, protected channels, FIPS validation, or full deployed-system AAL2 conformance from form-level records.

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

`DES-APP-002` is later evidence and does not retroactively rewrite this audit. Any maturity reclassification requires a new revision audit.

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
EXTERNAL_APPLICATIONS: 2
EXTERNAL_DOMAINS: 2
EXTERNAL_APPLICATION_PASSES: 2
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
- Second external application: `../../evidence/method_specific/design/DES-APP-002_nist-aal2-route-form-application.md`

## Next development step

External breadth has increased from one to two domains, including a case whose positive construction grammar is directly supplied by NIST.

The next preferred step is a **genuinely independent evaluator packet** with expected results hidden before reviewer submission. A further non-software/physical external application remains useful for additional breadth and irregular real-artifact candidate pressure.

Do not revise Protocol v0.1 merely to improve maturity optics; revise only if a new case exposes a genuine protocol defect. Do not overwrite `DES-AUD-001`; any maturity change requires a new re-audit.
