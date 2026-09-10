# SYN-CH-007 Precommit — Deterministic Retrace of SYN-APP-001

Status: **PRECOMMITTED — retrace not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**

## 1. Retrace identity

```text
CASE_ID: SYN-CH-007
CASE_CLASS: reproducibility_retrace
RETRACE_TARGET: SYN-APP-001
REPRODUCIBILITY_LEVEL_TARGET: deterministic_same_project
INDEPENDENT_REPLICATION_CLAIM: no
BLINDED_REPRODUCTION_CLAIM: no
METHOD_GAIN_ASSESSMENT: NOT_ASSESSED
```

This case is a deterministic same-project retrace only. It does not claim evaluator independence, blindness, inter-rater agreement, or independent replication.

## 2. Frozen immutable chain

```text
PROTOCOL:
  methods/05_synthesis/PROTOCOL_v0.1.md
  commit 8787b242cb6648c47396151dbac3aadc19e3d184

TARGET PRECOMMIT:
  evidence/method_specific/synthesis/SYN-APP-001_precommit.md
  commit 29ea45a1b9143dfda147b4987f005a4ff0313842
  blob b383fbc09b79f68e4f3bc2f46ed0037bf51a85e9

TARGET RESULT:
  evidence/method_specific/synthesis/SYN-APP-001_RFC3986-generic-URI-composition.md
  commit 69852468a8493b4fddaa8a6ac61edf40335146d9

EXTERNAL AUTHORITY:
  RFC 3986 / STD 66
  Uniform Resource Identifier (URI): Generic Syntax
  RFC Editor official text
  https://www.rfc-editor.org/rfc/rfc3986.html
```

The retrace may read the immutable target result for final equality comparison, but the semantic reconstruction must be independently written from the frozen task/source rules rather than copying its prose as a substitute for execution.

## 3. Frozen retrace target

Reconstruct exactly the original twelve candidates `R1-R12` under the original four hard conditions:

```text
H1 SCHEME_ABNF
H2 HIER_PART_BRANCH_COMPATIBILITY
H3 COMPONENT_LEXICAL_ABNF
H4 DECLARED_COMPONENT_ROUNDTRIP
```

Original staging remains fixed:

```text
H1 and H2 both evaluated first.
If H1 or H2 fails -> H3-H4 NOT_REACHED.
If H1-H2 pass -> H3.
If H3 fails -> H4 NOT_REACHED.
If H1-H3 pass -> H4.
```

Original scope remains fixed to RFC 3986 generic syntax only.

## 4. Equality target

The retrace passes only if it reconstructs exactly:

```text
R1  admissible / NONE
R2  admissible / NONE
R3  admissible / NONE
R4  admissible / NONE
R5  rejected / {H2}; H3-H4 NOT_REACHED
R6  rejected / {H2}; H3-H4 NOT_REACHED
R7  rejected / {H1}; H2 PASS; H3-H4 NOT_REACHED
R8  rejected / {H4}
R9  rejected / {H3}; H4 NOT_REACHED
R10 admissible / NONE
R11 admissible / NONE
R12 admissible / NONE at RFC3986_GENERIC_SYNTAX_ONLY

ADMISSIBLE_FAMILY:
{R1,R2,R3,R4,R10,R11,R12}

TERMINAL_SYNTHESIS_STATUS:
SYNTHESIS_ADMISSIBLE

SYNTHESIS_PROTOCOL_CONFORMANCE:
CONFORMANT

SYNTHESIS_METHOD_GAIN_STATUS:
NOT_ASSESSED
```

It must also preserve:

```text
QUERY_ABSENT != QUERY_PRESENT_EMPTY
FRAGMENT_ABSENT != FRAGMENT_PRESENT_EMPTY
AUTHORITY_ABSENT != AUTHORITY_PRESENT_EMPTY
GENERIC_PARSEABILITY_UNDER_DIFFERENT_DECOMPOSITION
  != SYNTHESIS_OF_DECLARED_COMPONENT_TUPLE
RFC3986_GENERIC_SYNTAX_ADMISSIBLE
  != SCHEME_SPECIFIC_URI_VALIDITY
GENERIC_SYNTACTIC_COMPOSITION
  != RESOURCE_RESOLUTION_SUCCESS
GENERIC_SYNTACTIC_COMPOSITION
  != SECURITY_OR_TRUSTWORTHINESS
```

## 5. Precommitted scoring

Total required checks: **48**.

```text
A. immutable-chain/source identity: 8
  A1 Protocol commit exact
  A2 target precommit commit exact
  A3 target precommit blob exact
  A4 target result commit exact
  A5 RFC identity exact
  A6 frozen source sections/scope unchanged
  A7 candidate basis R1-R12 unchanged
  A8 H1-H4 and staging unchanged

B. candidate reconstruction: 18
  B1-B12 exact R1-R12 verdict/failure-set behavior
  B13 R5 H3-H4 NOT_REACHED
  B14 R6 H3-H4 NOT_REACHED
  B15 R7 H2 PASS and H3-H4 NOT_REACHED
  B16 R9 H4 NOT_REACHED
  B17 R8 declared tuple roundtrip failure retained
  B18 R12 generic-syntax-only qualifier retained

C. status/structure reconstruction: 10
  C1 R3 query PRESENT_EMPTY
  C2 R4 fragment PRESENT_EMPTY
  C3 R11 query PRESENT_EMPTY
  C4 R11 fragment PRESENT_EMPTY
  C5 R12 authority PRESENT_EMPTY
  C6 R5 not rescued by redecomposition
  C7 R6 not rescued by redecomposition
  C8 no normalization/equivalence invented
  C9 no scheme-specific restriction invented
  C10 no candidate/tuple rewritten post hoc

D. closure/ledger equality: 7
  D1 family exactly {R1,R2,R3,R4,R10,R11,R12}
  D2 terminal exact
  D3 conformance exact
  D4 gain exact
  D5 fixture-only exhaustive scope exact
  D6 no neighboring-method claim
  D7 no temporal-process claim

E. reproducibility/scope discipline: 5
  E1 reconstructed result semantically matches immutable target result
  E2 generic syntax not upgraded to scheme-specific validity
  E3 no dereference/resource-resolution claim
  E4 no security/trustworthiness claim
  E5 result labeled deterministic_same_project, not independent replication
```

Decision:

```text
48/48 -> RETRACE_VERDICT: PASS
otherwise -> RETRACE_VERDICT: FAIL
```

## 6. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 0
DEDICATED_RETRACE_PASSES: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

A 48/48 PASS may add exactly:

```text
REPRODUCIBILITY_CASE_INCREMENT: +1
DEDICATED_RETRACE_PASS_INCREMENT: +1
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

It does not increase constructed direct-pilot count or external-application count and does not establish independent validation, method superiority, or maturity.
