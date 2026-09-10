# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 13 third external application complete / validation in progress**  
Date opened: **2026-09-10**

## Purpose / 목적

Develop DSD Synthesis as an independent method under **Field III: Construction & Transformation**. Synthesis consumes supplied admitted parts or typed component records plus an explicit composition rule and determines which larger constructions are legitimate while preserving component status, interface prerequisites, relations/support, information-loss conditions, and formation-model boundaries.

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
14. **Next:** first Synthesis maturity audit.
15. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 13 — SYN-APP-003 physical connector assembly

External source lock:

```text
FROZEN_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 (August 2019)
  mechanical mating / plug-orientation / role-establishment subset
SUPPORTING_SOURCE:
  USB-IF Type-C overview
EXTERNAL_DOMAIN:
  physical connector assembly / USB Type-C mating interface
```

The current USB-IF library has newer Type-C releases, but this case deliberately freezes Release 2.0 as a version-specific public mechanical source. It makes no current Release-2.5 compliance claim.

Precommit/result:

```text
PRECOMMIT: 4159872
RESULT: 73faaa0
```

Execution:

```text
M1 plug->receptacle orientation A       admissible
M2 plug->receptacle orientation B       admissible
M3 quarter-turn invalid orientation     rejected {H2}; downstream NOT_REACHED
M4 plug->plug direct                    rejected {H1}; downstream NOT_REACHED
M5 receptacle->receptacle direct        rejected {H1}; downstream NOT_REACHED
M6 C-to-C cable E1/E2 assignment        admissible; H5 PASS
M7 swapped cable-end assignment         admissible; H5 PASS
M8 mechanical mate -> Source/Sink claim rejected {H4}
M9 mechanical mate -> host/device claim rejected {H4}
M10 reversible cable direction -> power-role symmetry claim rejected {H4}; H5 PASS

ADMISSIBLE_FAMILY: {M1,M2,M6,M7}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 44/44 PASS
```

Preserved distinctions:

```text
TYPE_C_COMPONENT_ADMITTED != DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT
REVERSIBLE_PLUG_ORIENTATION != ARBITRARY_ROTATIONAL_SYMMETRY
MECHANICAL_MATING != SOURCE_SINK_ROLE_ESTABLISHMENT
MECHANICAL_MATING != HOST_DEVICE_ROLE_ESTABLISHMENT
REVERSIBLE_CABLE_DIRECTION != POWER_ROLE_SYMMETRY
```

Protocol pressure:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

## Evidence state after Step 13 / 13단계 후 증거 상태

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
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- Success or failure of any single challenge/application/retrace does not decide method survival, merger, absorption, or deletion.
- External validity is not upgraded beyond the source's declared version and scope.
- Same-project deterministic retrace is not independent replication.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Run a separately precommitted first Synthesis maturity audit `SYN-AUD-001`. It should evaluate evidence architecture rather than raw pass counts: protocol stability, distinct terminal-state handling, method-boundary integrity, honest failed-test preservation, NO_GAIN behavior under competent baselines, external-domain breadth, deterministic retrace, and unresolved independent validation. Method survival/merger/deletion must remain a separate conclusion, not an automatic consequence of audit score.
