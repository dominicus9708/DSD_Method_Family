# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / maturity: developing / validation in progress**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints while preserving the 22-method boundary discipline.

Shared-core evidence and neighboring-method results may be referenced, but direct Design validation is accumulated separately.

## Protocol and interface

- Current executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Design assumes no universal candidate generator.
- Candidate coverage remains `exhaustive / non_exhaustive / unknown`.
- `DESIGN_INFEASIBLE` requires exhaustive coverage or an impossibility argument.
- Material distinctness is judged at `TARGET_RESOLUTION`.
- Soft preferences are not silently promoted into hard constraints.
- External authority and neighboring-method verdicts remain separately identifiable.

## Three independent Design ledgers

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

Maturity is evaluated separately by DSD Audit.

## Development sequence / 개발 순서

1. ✅ Design-specific task interface and minimum valid output.
2. ✅ Boundary counterexamples and non-breaking refinements.
3. ✅ `PROTOCOL_v0.1.md`.
4. ✅ Positive pilot `DES-CH-001` — 11/11 PASS.
5. ✅ Negative/failure pilot `DES-CH-002` — 20/20 PASS.
6. ✅ Boundary stage — failed `DES-CH-003` preserved; corrected `DES-CH-004` 23/23 PASS.
7. ✅ NO_GAIN pilot `DES-CH-005` — 25/25 PASS.
8. ✅ Broader strongest-reasonable-baseline comparison `DES-CH-006` — 54/54 PASS / NO_GAIN.
9. ✅ First external-standard application `DES-APP-001` — W3C WCAG 2.2 subset, 36/36 PASS.
10. ✅ Dedicated reproducibility/retrace `DES-CH-007` — 44/44 PASS at deterministic same-project level.
11. ✅ First DSD Audit maturity review `DES-AUD-001` — audit 24/24 PASS; maturity classified `developing`; established promotion withheld.
12. **Next:** second external Design application in a materially different domain, preferably with externally supplied candidate/construction basis.
13. Prepare a genuinely independent evaluator packet after external breadth increases.
14. Re-audit maturity only after materially new evidence is frozen.

## Evidence milestones / 증거 이정표

### Positive and non-success behavior

`DES-CH-001` preserved status distinctions and returned the complete admissible family.

`DES-CH-002` directly separated:

```text
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

including the valid `DESIGN_BLOCKED + CONFORMANT` combination.

### Boundary behavior

`DES-CH-003` exposed a challenge-design defect and was preserved at 20/21 rather than repaired post hoc.
`DES-CH-004` prospectively corrected the candidate-resolution problem and passed the Design/Optimization boundary test.

### Method-gain behavior

`DES-CH-005` and `DES-CH-006` both produced valid `NO_GAIN` results against competent baselines.
No extra DSD bookkeeping was counted as gain by itself.

### External application

`DES-APP-001` froze W3C WCAG 2.2 Recommendation 2024-12-12, limited to:

```text
SC 1.4.3 Contrast (Minimum)
SC 2.5.3 Label in Name
SC 2.5.8 Target Size (Minimum)
```

It returned `{W1,W2,W3}` and passed 36/36 checks while keeping source requirements separate from fixture assumptions, not promoting best-practice language into a hard criterion, not inventing an exception, and not overclaiming full WCAG conformance.

### Dedicated retrace

`DES-CH-007` froze immutable refs for the protocol, `DES-APP-001` precommit, and historical result.

The claim-relevant re-execution reconstructed exactly:

```text
H0-H3
W1-W10 candidate records
candidate verdicts and rejection sets
admissible family {W1,W2,W3}
external source/version
WCAG_APPLICATION_BRIDGE_001
DESIGN_ADMISSIBLE
CONFORMANT
NOT_ASSESSED
```

and matched the historical result.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This is not independent replication.

## First maturity audit / 첫 성숙도 감사

`DES-AUD-001` precommitted 14 maturity axes and 24 audit-discipline checks before scoring.

Audit ID:

```text
DSD-AUDIT-20260908-DESIGN-001
```

Result:

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

Final maturity decision:

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
AUDIT_EXECUTION_VERDICT: PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The audit is an Audit meta-record and does not increase the Design direct-pilot count.

## Evidence architecture status / 증거 구조 상태

```text
DEDICATED_PROTOCOL: established
POSITIVE_CASE: established
NEGATIVE_OR_FAILURE_CASE: established
BOUNDARY_CASE: established with one preserved failed predecessor test
NO_GAIN_CASE: established
STRONGEST_REASONABLE_BASELINE_COMPARISON: established at constructed level
EXTERNAL_OR_INDEPENDENT_APPLICATION: established at single external-standard application level
REPRODUCIBILITY_RETRACE: established at deterministic same-project level
INDEPENDENT_EVALUATOR_VALIDATION: not established
MATURITY_AUDIT: completed, developing classification
```

Current evidence counts:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_APPLICATIONS: 1
EXTERNAL_DOMAINS: 1
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

The minimum evidence categories are populated, but `DES-AUD-001` explicitly confirms that category completion is not an automatic maturity rule.

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time. Prospective corrections do not rewrite earlier evidence. Maturity re-audits must be new audit records rather than edits to `DES-AUD-001`.

## Next step / 다음 단계

Address the primary audit blocker: **external evidence breadth**.

The preferred next case is a second external Design application in a materially different domain. It should, where possible:

```text
use an externally supplied real artifact or option set
avoid a candidate family authored solely for the DSD challenge
preserve irregular/incomplete candidate coverage when the source supplies it
lock the external source and candidate/construction basis before Design scoring
keep domain authority separate from the DSD verdict
```

After this breadth increase, prepare a genuinely independent evaluator packet. Further same-project synthetic cases on already-covered axes have diminishing maturity value unless they expose a new failure mode.
