# DSD Synthesis Planning / DSD 합성론 기획

Status: **Protocol v0.1 established / Step 10 first external application complete / validation in progress**  
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

Earlier artifacts and failed challenges remain historical and are not rewritten after later evidence.

## Output / terminal / ledger structure

```text
OUTPUT_LEVELS:
  SYNTHESIS_SPACE
  SYNTHESIZED_TARGET
  UNIQUE_SYNTHESIZED_TARGET
  PARTIAL_SYNTHESIS

TERMINAL:
  SYNTHESIS_ADMISSIBLE
  SYNTHESIS_INFEASIBLE
  SYNTHESIS_UNDERDETERMINED
  SYNTHESIS_BLOCKED

THREE LEDGERS:
  TERMINAL_SYNTHESIS_STATUS
  SYNTHESIS_PROTOCOL_CONFORMANCE
  SYNTHESIS_METHOD_GAIN_STATUS
```

## Development sequence / 개발 순서

1. ✅ Synthesis-specific task interface.
2. ✅ 16 pre-protocol boundary attacks — 11 no refinement, 5 non-breaking refinement, 0 collapse.
3. ✅ Boundary Amendment 001.
4. ✅ Executable `Synthesis Protocol v0.1` — commit `8787b24`.
5. ✅ `SYN-CH-001` positive — **28/28 PASS**.
6. ✅ `SYN-CH-002` negative/failure — **36/36 PASS**.
7. ✅ `SYN-CH-003` direct method-boundary — **46/46 PASS**.
8. ✅ First `NO_GAIN` stage — `SYN-CH-004` **33/35 FAIL** challenge-design defect preserved; corrected `SYN-CH-005` **37/37 PASS / NO_GAIN**.
9. ✅ `SYN-CH-006` broader strongest-reasonable-baseline comparison — **52/52 PASS / NO_GAIN**, category established at constructed-evidence level.
10. ✅ `SYN-APP-001` first external application — RFC 3986 generic URI composition, **40/40 PASS**.
11. **Next:** deterministic same-project retrace/reproducibility of `SYN-APP-001`.
12. Second materially different external domain.
13. DSD Audit maturity review only after evidence architecture is materially populated.
14. Independent-evaluator infrastructure only when protocol/evidence stability justifies it.

## Step 9 — SYN-CH-006 broader strongest-reasonable-baseline

```text
PRECOMMIT: 4a6c1fe
RESULT: 8ad51b5
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
RAW DSD = B1 = {A1,A2,A3,A4}
CANONICAL DSD = B1 = {C0,C1}
GAIN: NO_GAIN
SCORE: 52/52 PASS
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

The competent baseline was not weakened and matched DSD on every frozen claim-relevant dimension.

## Step 10 — SYN-APP-001 first external application

External source:

```text
RFC 3986 / STD 66
Uniform Resource Identifier (URI): Generic Syntax
external domain: Internet identifier syntax / URI generic syntax
```

Precommit/result:

```text
PRECOMMIT: 29ea45a
RESULT: 6985246
```

Frozen task: compose declared generic-URI components under the external RFC grammar while preserving component identity and optional-component presence state.

```text
R1  admissible
R2  admissible
R3  admissible; query PRESENT_EMPTY preserved
R4  admissible; fragment PRESENT_EMPTY preserved
R5  rejected {H2}; authority/path branch mismatch
R6  rejected {H2}; no-authority path begins //
R7  rejected {H1}; invalid generic scheme start
R8  rejected {H4}; raw characters parse only under a different query/fragment decomposition
R9  rejected {H3}; raw-space path lexical failure
R10 admissible
R11 admissible; query + fragment PRESENT_EMPTY preserved
R12 admissible at RFC3986 generic-syntax level; authority PRESENT_EMPTY preserved
```

Closure and ledgers:

```text
SYNTHESIS_ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

Scope guards retained:

```text
RFC3986_GENERIC_SYNTAX_ADMISSIBLE != SCHEME_SPECIFIC_URI_VALIDITY
GENERIC_SYNTACTIC_COMPOSITION != RESOURCE_RESOLUTION_SUCCESS
GENERIC_SYNTACTIC_COMPOSITION != SECURITY_OR_TRUSTWORTHINESS
PRESENT_EMPTY != ABSENT
```

This application adds one external application and one external domain but does not alter the constructed-pilot count or maturity classification.

## Evidence state after Step 10 / 10단계 후 증거 상태

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
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## Recording rule / 기록 규칙

- Shared-core and neighboring-method evidence does not automatically become direct Synthesis validation.
- Historical planning and failed challenge designs are preserved; corrections are prospective under new Case IDs.
- A competent baseline is not weakened to manufacture a DSD advantage.
- `NO_GAIN` is a legitimate result and is separate from correctness/conformance.
- Success or failure of an individual challenge/application does not itself determine whether the method survives, merges, or is deleted.
- Grouping/equivalence is activated only when supplied by composition law and target-resolution rules.
- Component Property does not become whole Property without explicit lift/redeclaration.
- Relation loss and formation effect remain claim-relevant when the task includes them.
- No Formation Clause VII or Static Aggregation result is upgraded into domain composability without explicit legitimacy.
- No static composability result is upgraded into time-resolved assembly feasibility without explicit process scope/model.
- External-source generic validity is not upgraded into stronger domain-specific validity absent the required external specification.
- Protocol v0.1 is revised only prospectively if direct evidence exposes a genuine protocol defect.

## Immediate next task / 다음

Precommit and execute a deterministic same-project retrace of `SYN-APP-001` using only the immutable RFC-source lock, `SYN-APP-001` precommit, and result records. The retrace must reconstruct all twelve candidate verdicts, the admissible family, presence-state distinctions, scope guards, and three ledgers without changing the original case.
