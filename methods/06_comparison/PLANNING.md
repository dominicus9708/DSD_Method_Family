# DSD Comparison Planning / DSD 비교론 기획

Status: **Protocol v0.1 established / CMP-AUD-001 maturity established / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Comparison as an independent method under **Field I: Structural Description & Understanding**. Comparison consumes two or more supplied subjects together with an explicit comparison scope, map/correspondence family, and preservation/equivalence criteria, then returns a justified correspondence/divergence profile without collapsing comparison into final-output equality.

## Protocol lineage / 프로토콜 계보

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Executable protocol commit:

```text
a1700d960e0b41dfe32bf85b6334448d9104100d
```

## Development sequence / 개발 순서

1. ✅ Comparison-specific task interface draft.
2. ✅ 16 pre-protocol boundary attacks.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Comparison Protocol v0.1` — commit `a1700d9`.
5. ✅ `CMP-CH-001` positive direct challenge — **40/40 PASS**.
6. ✅ `CMP-CH-002` negative/failure challenge — **48/48 PASS**.
7. ✅ `CMP-CH-003` direct method-boundary challenge — **48/48 PASS**.
8. ✅ `CMP-CH-004` competent-baseline `NO_GAIN` — **50/50 PASS / NO_GAIN**.
9. ✅ `CMP-CH-005` strongest-reasonable-baseline — **60/60 PASS / NO_GAIN**.
10. ✅ `CMP-APP-001` first external application — Unicode normalization, **42/42 PASS**.
11. ✅ `CMP-CH-006` deterministic same-project retrace — **48/48 PASS**.
12. ✅ `CMP-APP-002` second external domain — RFC 9110 HTTP ETag comparison semantics, **48/48 PASS**.
13. ✅ `CMP-APP-003` third external domain — JCGM VIM metrological compatibility, **52/52 PASS**.
14. ✅ `CMP-AUD-001` first maturity audit — **28/28 audit execution PASS / PROMOTE_ESTABLISHED**.
15. **Next:** `CMP-IEP-001` independent-evaluator infrastructure preparation.

## Constructed evidence summary

```text
CMP-CH-001  40/40 PASS
CMP-CH-002  48/48 PASS
CMP-CH-003  48/48 PASS
CMP-CH-004  50/50 PASS / NO_GAIN
CMP-CH-005  60/60 PASS / NO_GAIN
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

## External breadth summary

```text
CMP-APP-001
  Unicode Standard Annex #15
  Unicode normalization / text representation
  42/42 PASS

CMP-APP-002
  RFC 9110 HTTP ETag comparison
  protocol validator semantics
  48/48 PASS

CMP-APP-003
  JCGM 200:2012 VIM3 2.47
  physical metrology / measurement-result compatibility
  52/52 PASS
```

Materially different comparison mechanisms are represented:

```text
normalization-dependent equivalence
context-selected strong/weak direct validator comparison
quantitative uncertainty-dependent compatibility with correlation closure
```

## Reproducibility summary

```text
CMP-CH-006
  RETRACE TARGET: CMP-APP-001
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

Same-project retrace remains separate from independent replication.

## CMP-AUD-001 maturity audit

Evidence:

```text
PRECOMMIT: 69315746b3ed5367aa56e087b96b8ea878a59376
RESULT: afe4cc7d8a4efe2f7485768e0d9dc363010e34e2
AUDIT_EXECUTION_VERDICT: 28/28 PASS
```

Axis result:

```text
M1  dedicated executable protocol                          PASS
M2  positive/negative terminal discrimination              PASS
M3  neighboring-method boundary discrimination             PASS
M4  NO_GAIN preservation                                   PASS
M5  reproducibility/retraceability                          CONDITIONAL_PASS
M6  external application origin                            PASS
M7  strongest-reasonable-baseline comparison               PASS
M8  external source fidelity and criterion/bridge discipline PASS
M9  established-level evidence breadth                     PASS
M10 independent/practical-performance evidence             UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect             PASS
M12 maximum-supported-claim discipline                     PASS
M13 comparison coverage / criterion / equivalence closure  PASS
M14 historical / anti-post-hoc preservation                PASS
M15 method-survival / merger-separation discipline         PASS
```

Decision:

```text
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The audit changed no direct-pilot, external-application, or reproducibility counts.

Established maturity remains bounded away from:

```text
independent validation
independent replication
broad inter-rater agreement
measured practical superiority
universal external generality
permanent method-registry survival or irreducibility
```

## Current evidence state / 현재 증거 상태

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_COMPARISON_APPLICATIONS: 3
EXTERNAL_COMPARISON_DOMAINS: 3
EXTERNAL_COMPARISON_APPLICATION_PASSES: 3
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Recording rule / 기록 규칙

- Protocol establishment is infrastructure, not direct evidence.
- Constructed direct pilots, external applications, retrace evidence, and maturity-audit meta-records remain separate counters/classes.
- Same-project retrace is not independent replication.
- Comparison criteria are frozen per task; the same pair may legitimately receive different verdicts under different criteria.
- Aggregate equality does not become structural identity.
- One map does not close an untested map family.
- Map-family coverage and claim-relevant element coverage remain separate.
- Precomparison transformations require provenance and remain Transformation operations.
- First-branch claims require earlier-stage closure; later re-convergence does not erase an earlier justified branch.
- Similar dynamic trajectories do not establish lineage identity.
- Method gain requires a frozen competent baseline.
- `NO_GAIN` is legitimate and is not method failure or absorption proof.
- External standard terminology is not automatically relabelled `STRICT_EQUIVALENT`.
- Missing claim-relevant information remains underdetermined/blocked rather than being filled by assumption.
- Maturity promotion does not decide method survival, merger, absorption, or deletion.

## Next / 다음

Prepare `CMP-IEP-001` independent-evaluator infrastructure because the weakest remaining maturity axes are M5/M10. The packet must use immutable pre-submission locking and keep answer/reference material separated from the evaluator-facing task. Packet preparation alone is not independent validation.
