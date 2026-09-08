# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / validation in progress**

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

## Three independent ledgers

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
11. **Next:** DSD Audit maturity review.

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
The latter used Formation + General Property, 15 candidates, typed status distinctions, full failure sets, and DESIGN_SPACE + UNIQUE_TARGET.
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

`DES-CH-007` froze immutable refs for:

```text
Protocol v0.1:
  b3d658c839dfe60b65efbc44abf874e257d4a0e2
DES-APP-001 precommit:
  4847dbd1f5a38adb5d5c285b19ac41ebcfe86b96
DES-APP-001 historical result:
  32a7842758be0cc179f996fdd8035d9683d31da9
```

The clean claim-relevant re-execution from frozen Protocol + source precommit reconstructed exactly:

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
```

The evidence claim is deliberately limited: this is a same-project, same-evaluator-family, non-blinded deterministic retrace. It does not establish independent replication.

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
MATURITY_AUDIT: not performed
```

Current evidence counts:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_APPLICATIONS: 1
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

The minimum evidence categories are now populated, but category completion is not an automatic maturity rule.

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time. Prospective corrections do not rewrite earlier evidence.

## Next step / 다음 단계

Run a **DSD Audit maturity review** over the accumulated Design corpus.

The audit must:

```text
preserve DES-CH-003 as a real challenge-design failure
separate protocol correctness from method gain
count DES-CH-005 and DES-CH-006 NO_GAIN without converting them into superiority evidence
recognize DES-APP-001 as one external-standard application, not broad external validation
recognize DES-CH-007 as deterministic retrace, not independent replication
discount common-evaluator/same-project dependence
keep independent evaluator validation explicitly open
avoid automatic promotion merely because minimum evidence categories are populated
```
