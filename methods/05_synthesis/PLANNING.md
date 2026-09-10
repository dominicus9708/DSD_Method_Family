# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 12 second external application complete / validation in progress**  
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
13. **Next:** third materially different external domain with nontrivial component/assembly compatibility.
14. First DSD Audit maturity review after that external pressure.
15. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 10 — SYN-APP-001

```text
EXTERNAL_STANDARD: RFC 3986 / STD 66
PRECOMMIT: 29ea45a
RESULT: 6985246
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

Scope guards:

```text
RFC3986_GENERIC_SYNTAX_ADMISSIBLE != SCHEME_SPECIFIC_URI_VALIDITY
GENERIC_SYNTACTIC_COMPOSITION != RESOURCE_RESOLUTION_SUCCESS
PRESENT_EMPTY != ABSENT
```

## Step 11 — SYN-CH-007 retrace

```text
PRECOMMIT: 9bbcadf
RESULT: 7256456
RETRACE_TARGET: SYN-APP-001
REPRODUCIBILITY_LEVEL: deterministic_same_project
RECONSTRUCTED_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 48/48 PASS
INDEPENDENT_REPLICATION: not established
```

## Step 12 — SYN-APP-002 physical-metrology external application

External source:

```text
BIPM SI Brochure
9th edition, version 4.01, updated 2026
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
```

Precommit/result:

```text
PRECOMMIT: 46479ae
RESULT: c504d53
```

The frozen task uses externally supplied rules for products of powers, coherent derived units, special-name equivalences, SI-prefix factors, power propagation, compound-prefix prohibition, and the kilogram/gram prefix convention.

Execution:

```text
U1 kg m s^-2 -> N             admissible / COHERENT
U2 N m -> J                    admissible / COHERENT
U3 J s^-1 -> W                 admissible / COHERENT
U4 N m^-2 -> Pa                admissible / COHERENT
U5 A s -> C                    admissible / COHERENT
U6 kg m s^-1 -> N              rejected {H4}
U7 cm^3 -> 10^-6 m^3           admissible / NONCOHERENT
U8 cm^3 -> 10^-2 m^3           rejected {H4}
U9 kN -> 10^3 N                admissible / NONCOHERENT
U10 kN -> N at scale 1         rejected {H4}
U11 mµm compound prefix        rejected {H2}; H3-H5 NOT_REACHED
U12 µkg direct prefix on kg    rejected {H2}; H3-H5 NOT_REACHED

ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 46/46 PASS
```

Preserved distinctions:

```text
SAME_DIMENSION != SAME_UNIT_SCALE
VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT
PREFIX_COMPONENT_ADMITTED != PREFIX_COMPOSITION_FORM_LEGAL
SI_UNIT_COMPOSITION != PHYSICAL_MEASUREMENT_VALIDITY
```

Protocol pressure:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

## Evidence state after Step 12 / 12단계 후 증거 상태

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
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
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
- External validity is not upgraded beyond the source's declared scope.
- Same-project deterministic retrace is not independent replication.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Precommit a third external Synthesis application in a domain with genuine component/interface or assembly constraints, preferably physical engineering or another non-symbolic setting. The goal is broader pressure, not a forced PASS or forced method-survival conclusion.
