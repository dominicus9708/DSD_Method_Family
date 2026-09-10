# SYN-CH-007 Deterministic Retrace of SYN-APP-001

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Retrace level: **deterministic_same_project**  
Precommit commit: `9bbcadf95e02f08334d7f45801b62429f9245987`  
Precommit blob: `0fb86f22b0a66c47ac4a4efe7baef3f8515e07cb`

## 1. Immutable chain checked

```text
PROTOCOL COMMIT:
8787b242cb6648c47396151dbac3aadc19e3d184

SYN-APP-001 PRECOMMIT COMMIT:
29ea45a1b9143dfda147b4987f005a4ff0313842

SYN-APP-001 PRECOMMIT BLOB:
b383fbc09b79f68e4f3bc2f46ed0037bf51a85e9

SYN-APP-001 RESULT COMMIT:
69852468a8493b4fddaa8a6ac61edf40335146d9

EXTERNAL AUTHORITY:
RFC 3986 / STD 66
Uniform Resource Identifier (URI): Generic Syntax
RFC Editor official text
```

No source section, candidate, hard condition, staging rule, target-resolution rule, or scope qualifier was changed for this retrace.

## 2. Source-rule reconstruction

The frozen RFC source supports the retrace rule set:

```text
URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]

hier-part = "//" authority path-abempty
          / path-absolute
          / path-rootless
          / path-empty

scheme begins with ALPHA.
path-abempty is empty or slash-led.
query and fragment use zero-or-more grammars.
reg-name uses a zero-or-more grammar.
component recomposition distinguishes undefined from present-empty components.
generic URI grammar is broader than scheme-specific generative grammar.
```

These facts reproduce the original H1-H4 interpretation without adding a scheme-specific rule.

## 3. Candidate reconstruction

### R1

```text
foo://example.com/a?x=1#frag
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R2

```text
foo://example.com
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R3

```text
foo:/a?
QUERY_STATUS: PRESENT_EMPTY
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R4

```text
foo:a/b#
FRAGMENT_STATUS: PRESENT_EMPTY
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R5

```text
declared authority: PRESENT_NONEMPTY(example.com)
declared path: a/b
H1 PASS
H2 FAIL
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H2}
```

The declared tuple is not rescued by reparsing the characters under a different authority/path decomposition.

### R6

```text
declared authority: ABSENT
declared path: //x
H1 PASS
H2 FAIL
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H2}
```

The declared no-authority branch is not rewritten into an authority-bearing tuple.

### R7

```text
scheme: 1foo
H1 FAIL
H2 PASS
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H1}
```

### R8

```text
declared suffix order: fragment_then_query
raw characters: foo:/a#frag?x=1
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
RESULT: rejected / {H4}
```

The string is generically parseable, but it does not recover the declared query/fragment tuple. The intended query text becomes fragment data after `#`.

### R9

```text
declared path: /a b
H1 PASS
H2 PASS
H3 FAIL
H4 NOT_REACHED
RESULT: rejected / {H3}
```

The raw space is outside the frozen pchar-based path grammar.

### R10

```text
foo:/a#frag
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R11

```text
foo:?#
QUERY_STATUS: PRESENT_EMPTY
FRAGMENT_STATUS: PRESENT_EMPTY
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R12

```text
foo:///a
AUTHORITY_STATUS: PRESENT_EMPTY
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
QUALIFIER: RFC3986_GENERIC_SYNTAX_ONLY
```

The empty authority is preserved as present-empty rather than collapsed to absence. No particular URI scheme is claimed to accept it.

## 4. Reconstructed closure and ledgers

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{R1,R2,R3,R4,R10,R11,R12}

TERMINAL_SYNTHESIS_STATUS:
SYNTHESIS_ADMISSIBLE

SYNTHESIS_PROTOCOL_CONFORMANCE:
CONFORMANT

SYNTHESIS_METHOD_GAIN_STATUS:
NOT_ASSESSED
```

This semantically matches the immutable `SYN-APP-001` result.

## 5. Status and scope distinctions reproduced

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

No normalization-equivalence rule, dereference claim, resource-existence claim, security claim, or temporal process model was introduced.

## 6. Precommitted scoring

```text
A. immutable-chain/source identity       8 / 8 PASS
B. candidate reconstruction            18 / 18 PASS
C. status/structure reconstruction     10 / 10 PASS
D. closure/ledger equality              7 / 7 PASS
E. reproducibility/scope discipline     5 / 5 PASS

PRECOMMITTED_REQUIRED_CHECKS:          48
PASSED:                                 48
FAILED:                                  0
RETRACE_VERDICT:                       PASS
```

No scoring item was deleted, weakened, or reclassified after execution.

## 7. Reproducibility result

```text
REPRODUCIBILITY_CASE_INCREMENT: +1
DEDICATED_RETRACE_PASS_INCREMENT: +1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_REPLICATION: not established
BLINDED_REPRODUCTION: not established
```

This is a deterministic retrace of frozen rules and records by the same project environment. It is not independent evidence.

## 8. Post-run evidence state

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Constructed direct-pilot count and external-application count are unchanged.

## 9. Protocol and method-independence pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_RETRACE: none
```

A retrace PASS or FAIL is evidence about reproducibility of this frozen application. It is not, by itself, a reason to preserve, delete, merge, or absorb the Synthesis method. Method independence remains a separate boundary/maturity question.

## 10. Next evidence step

Add a second materially different external Synthesis domain before a maturity audit. Prefer a public standard whose composition legitimacy is physical, engineering, scientific, legal, or another non-URI domain so that external breadth is not obtained by repeating the same syntax family.
