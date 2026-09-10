# DSD Synthesis Worklog / DSD 합성론 작업 기록

## 2026-09-10 — Planning preparation and Step 1

Status: **planning started / Step 1 complete**

Locked project paths:

```text
methods/05_synthesis/
evidence/method_specific/synthesis/
```

Defined DSD Synthesis as:

```text
supplied parts + supplied composition rule
-> admissible whole/composition space
```

Created `TASK_INTERFACE_v0.1-draft.md` with component identity/status, composition-rule provenance, candidate basis/coverage, interface/prerequisites, property-lift discipline, retention/loss, formation effect, output levels, ledgers, handoffs, and reproducibility fields.

---

## 2026-09-10 — Step 2: pre-protocol boundary counterexamples

```text
BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md   d089b04
TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md d1f51b2
```

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

The Step-1 draft remained historical and was not rewritten.

---

## 2026-09-10 — Step 4: Protocol v0.1 establishment

Created `methods/05_synthesis/PROTOCOL_v0.1.md` at commit `8787b24`. Executable sequence: `S1-S17`. Protocol creation itself added no direct pilot.

---

## 2026-09-10 — Step 5: SYN-CH-001 positive direct challenge

```text
PRECOMMIT: 4eeba2a
RESULT: 71e5d5c
ADMISSIBLE_FAMILY: {K1,K2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 28/28 PASS
```

---

## 2026-09-10 — Step 6: SYN-CH-002 negative/failure challenge

```text
PRECOMMIT: 09fc616
RESULT: 7dac87c
I -> SYNTHESIS_INFEASIBLE
U -> SYNTHESIS_UNDERDETERMINED
B -> SYNTHESIS_BLOCKED
SCORE: 36/36 PASS
PROTOCOL_REVISION_REQUIRED: no
```

---

## 2026-09-10 — Step 7: SYN-CH-003 direct method-boundary challenge

```text
PRECOMMIT: 2eea8ae
RESULT: cb55dba
BASE FAMILY: {S0,S1}
D -> DESIGN_REQUIRED
T -> TRANSFORMATION_REQUIRED
A -> AGGREGATION_REQUIRED
O -> OPTIMIZATION_REQUIRED
SCORE: 46/46 PASS
PROTOCOL_REVISION_REQUIRED: no
```

---

## 2026-09-10 — Step 8A: SYN-CH-004 first NO_GAIN baseline attempt

```text
PRECOMMIT: 1c77a0e
FIRST RESULT: 29730a5
POSTEXECUTION AUDIT: fe55899
STRICT SCORE: 33/35 FAIL
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

The failed challenge remains preserved and fills no successful NO_GAIN category.

---

## 2026-09-10 — Step 8B: SYN-CH-005 prospective corrected NO_GAIN challenge

```text
PRECOMMIT: 3c6f323
RESULT: f062d3f
DSD FAMILY: {R1,R2}
B0 FAMILY: {R1,R2}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NO_GAIN
SCORE: 37/37 PASS
```

---

## 2026-09-10 — Step 9: SYN-CH-006 broader strongest-reasonable-baseline comparison

```text
PRECOMMIT: 4a6c1fe
RESULT: 8ad51b5
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
RAW DSD FAMILY: {A1,A2,A3,A4}
RAW B1 FAMILY: {A1,A2,A3,A4}
CANONICAL DSD FAMILY: {C0,C1}
CANONICAL B1 FAMILY: {C0,C1}
GAIN: NO_GAIN
SCORE: 52/52 PASS
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

Interpretation: the richer typed composition task was handled correctly, but a strong non-DSD baseline supplied with the same semantics matched every measured dimension. No superiority claim was made.

---

## 2026-09-10 — Step 10: SYN-APP-001 first external application

Status: **40/40 PASS / first external Synthesis domain**

External authority:

```text
RFC 3986 / STD 66
Uniform Resource Identifier (URI): Generic Syntax
RFC Editor official source
external domain: Internet identifier syntax / URI generic syntax
```

Precommit:

```text
evidence/method_specific/synthesis/SYN-APP-001_precommit.md
commit: 29ea45a1b9143dfda147b4987f005a4ff0313842
blob: b383fbc09b79f68e4f3bc2f46ed0037bf51a85e9
```

Result:

```text
evidence/method_specific/synthesis/SYN-APP-001_RFC3986-generic-URI-composition.md
commit: 69852468a8493b4fddaa8a6ac61edf40335146d9
```

Frozen external composition rules included generic URI component order, authority/no-authority hierarchical branches, scheme syntax, path/query/fragment lexical grammar, and optional-component presence.

Execution:

```text
R1  admissible
R2  admissible
R3  admissible; QUERY_PRESENT_EMPTY preserved
R4  admissible; FRAGMENT_PRESENT_EMPTY preserved
R5  rejected {H2}
R6  rejected {H2}
R7  rejected {H1}
R8  rejected {H4}; raw string parses only under a different component tuple
R9  rejected {H3}
R10 admissible
R11 admissible; query + fragment PRESENT_EMPTY preserved
R12 admissible at RFC3986 generic-syntax level; AUTHORITY_PRESENT_EMPTY preserved

ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

Scope discipline:

```text
RFC3986_GENERIC_SYNTAX_ADMISSIBLE != SCHEME_SPECIFIC_URI_VALIDITY
GENERIC_SYNTACTIC_COMPOSITION != RESOURCE_RESOLUTION_SUCCESS
GENERIC_SYNTACTIC_COMPOSITION != SECURITY_OR_TRUSTWORTHINESS
PRESENT_EMPTY != ABSENT
```

Evidence effect:

```text
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
DIRECT_SYNTHESIS_PILOTS_COMPLETED: remains 6
```

Protocol pressure:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

A pass/fail result is evidence about the frozen application, not by itself a command to preserve, merge, absorb, or delete a method.

---

## 2026-09-10 — Step 11: SYN-CH-007 deterministic same-project retrace

Status: **48/48 PASS / first dedicated Synthesis retrace**

Precommit:

```text
evidence/method_specific/synthesis/SYN-CH-007_retrace-precommit.md
commit: 9bbcadf95e02f08334d7f45801b62429f9245987
blob: 0fb86f22b0a66c47ac4a4efe7baef3f8515e07cb
```

Result:

```text
evidence/method_specific/synthesis/SYN-CH-007_deterministic-retrace.md
commit: 72564564081b5aa58255d733fa0a78c4b9cf4fbd
```

Frozen retrace chain:

```text
Protocol commit 8787b242cb6648c47396151dbac3aadc19e3d184
SYN-APP-001 precommit commit 29ea45a1b9143dfda147b4987f005a4ff0313842
SYN-APP-001 precommit blob b383fbc09b79f68e4f3bc2f46ed0037bf51a85e9
SYN-APP-001 result commit 69852468a8493b4fddaa8a6ac61edf40335146d9
RFC 3986 / STD 66 official source
```

Semantic reconstruction exactly reproduced:

```text
R1-R4 admissible
R5 -> {H2}; H3-H4 NOT_REACHED
R6 -> {H2}; H3-H4 NOT_REACHED
R7 -> {H1}; H2 PASS; H3-H4 NOT_REACHED
R8 -> {H4}
R9 -> {H3}; H4 NOT_REACHED
R10-R12 admissible
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

Status/scope reconstruction also preserved:

```text
QUERY_ABSENT != QUERY_PRESENT_EMPTY
FRAGMENT_ABSENT != FRAGMENT_PRESENT_EMPTY
AUTHORITY_ABSENT != AUTHORITY_PRESENT_EMPTY
GENERIC_PARSEABILITY_UNDER_DIFFERENT_DECOMPOSITION != SYNTHESIS_OF_DECLARED_COMPONENT_TUPLE
RFC3986_GENERIC_SYNTAX_ADMISSIBLE != SCHEME_SPECIFIC_URI_VALIDITY
GENERIC_SYNTACTIC_COMPOSITION != RESOURCE_RESOLUTION_SUCCESS
GENERIC_SYNTACTIC_COMPOSITION != SECURITY_OR_TRUSTWORTHINESS
```

Scoring:

```text
PRECOMMITTED_REQUIRED_CHECKS: 48
PASSED: 48
FAILED: 0
RETRACE_VERDICT: PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_REPLICATION: not established
```

Evidence effect:

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
DIRECT_SYNTHESIS_PILOTS_COMPLETED: remains 6
EXTERNAL_SYNTHESIS_APPLICATIONS: remains 1
```

Protocol/method-independence discipline:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_RETRACE: none
```

A retrace outcome measures reproducibility of the frozen application. It does not itself decide method preservation, merger, absorption, or deletion.

### Next technical step

Add a second materially different external Synthesis domain before any maturity audit. Prefer an externally sourced physical, engineering, scientific, legal, or other non-URI composition/assembly rule so external breadth is not obtained from repeated URI-syntax variants.
