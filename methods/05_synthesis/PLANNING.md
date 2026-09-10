# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / first maturity audit complete / method-protocol evidence maturity established / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method candidate under **Field III: Construction & Transformation**. Synthesis consumes supplied admitted parts or typed component records plus an explicit composition rule and determines which larger constructions are legitimate while preserving component status, interface prerequisites, relations/support, information-loss conditions, and formation-model boundaries.

Method maturity and final registry survival are separate questions.

## Current source/interface lock / 현재 기준 잠금

```text
Formation Axiom System
Property Axiom System
Channel-Indexed Static Aggregation
Structural Reorganization Dynamics
DSD_INTERFACE_PROFILE.md
METHOD_BOUNDARY_MATRIX.md
```

Key constraints:

```text
Formation Clause VII finite composition != universal domain composability
component property != automatic whole property
aggregate equality/readout != structural synthesis equality
single-case success/failure != method survival/merger/deletion decision
```

## Protocol lineage / 프로토콜 계보

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Historical artifacts and failed challenges remain preserved rather than rewritten.

## Development sequence / 개발 순서

1. ✅ Synthesis-specific task interface.
2. ✅ 16 pre-protocol boundary attacks — 11 no refinement, 5 non-breaking refinement, 0 collapse.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ `SYN-CH-001` positive — **28/28 PASS**.
6. ✅ `SYN-CH-002` negative/failure — **36/36 PASS**.
7. ✅ `SYN-CH-003` direct method-boundary — **46/46 PASS**.
8. ✅ `SYN-CH-004` failed baseline design **33/35 FAIL** preserved; corrected `SYN-CH-005` **37/37 PASS / NO_GAIN**.
9. ✅ `SYN-CH-006` broader strongest-reasonable-baseline — **52/52 PASS / NO_GAIN**.
10. ✅ `SYN-APP-001` RFC 3986 generic URI external application — **40/40 PASS**.
11. ✅ `SYN-CH-007` deterministic same-project retrace — **48/48 PASS**.
12. ✅ `SYN-APP-002` BIPM SI unit-composition external application — **46/46 PASS**.
13. ✅ `SYN-APP-003` USB Type-C physical mating external application — **44/44 PASS**.
14. ✅ `SYN-AUD-001` first maturity audit — **28/28 audit-execution PASS**, method/protocol evidence maturity `established`.
15. **Next:** independent-evaluator infrastructure `SYN-IEP-001`.
16. Independent evidence scoring only after a genuinely separate immutable evaluator submission exists.

## Step 14 — SYN-AUD-001 maturity review

```text
AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
PRECOMMIT: ba966b5
RESULT: bae4388
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Maturity axes:

```text
M1  dedicated executable protocol                       PASS
M2  positive/negative terminal discrimination           PASS
M3  neighboring-method boundary discrimination          PASS
M4  NO_GAIN preservation                                PASS
M5  reproducibility/retraceability                       CONDITIONAL_PASS
M6  external application origin                         PASS
M7  strongest-reasonable-baseline comparison            PASS
M8  external source fidelity and bridge discipline      PASS
M9  established-level evidence breadth                  PASS
M10 independent/practical-performance evidence          UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect          PRESENT_NONFATAL
M12 maximum-supported-claim discipline                  PASS
M13 composition-basis / coverage / equivalence discipline PASS
M14 historical failure / anti-post-hoc preservation     PASS
M15 method-survival / merger-separation discipline      PASS
```

The promotion is supported by evidence architecture rather than raw PASS count: executable protocol, terminal-state discrimination, operational neighboring-method boundaries, preserved challenge-design failure, multiple honest `NO_GAIN` comparisons, strongest-reasonable baseline, deterministic retrace, and three materially different external domains.

The label remains bounded:

```text
ESTABLISHED_METHOD_PROTOCOL_EVIDENCE_MATURITY
!= INDEPENDENT_VALIDATION
!= INDEPENDENT_REPLICATION
!= PRACTICAL_SUPERIORITY
!= UNIVERSAL_EXTERNAL_GENERALITY
!= PERMANENT_METHOD_REGISTRY_SURVIVAL
```

## Evidence state after Step 14 / 14단계 후 증거 상태

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The audit itself added no direct, external, or reproducibility evidence counts.

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- Success or failure of any single challenge/application/retrace does not decide method survival, merger, absorption, or deletion.
- Established method/protocol evidence maturity does not freeze the 22-method registry permanently.
- External validity is not upgraded beyond the source's declared version and scope.
- Same-project deterministic retrace is not independent replication.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Prepare `SYN-IEP-001` independent-evaluator infrastructure. It should include a clean reviewer packet, frozen external/source bundle or self-contained task, submission template, eligibility/contamination gates, hidden reference answer or commitment, and predeclared scoring. Packet preparation itself remains infrastructure and does not change independent-validation status.
