# SYN-APP-001 Result / RFC 3986 Generic URI Composition

Status: **EXECUTED — 40/40 PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `29ea45a1b9143dfda147b4987f005a4ff0313842`  
Precommit blob: `b383fbc09b79f68e4f3bc2f46ed0037bf51a85e9`

## 1. Evidence identity

```text
CASE_ID: SYN-APP-001
CASE_CLASS: external_application
CASE_ORIGIN: externally_sourced_rule_with_constructed_candidate_fixture
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
EXTERNAL_STANDARD: RFC 3986 / STD 66
BASELINE: none
```

This is the first Synthesis application in which the composition grammar itself comes from a stable external public standard rather than from a project-invented rule.

## 2. External-source lock and scope

Primary authority:

```text
RFC 3986 / STD 66
Uniform Resource Identifier (URI): Generic Syntax
RFC Editor official text:
https://www.rfc-editor.org/rfc/rfc3986.html
```

Applied source rules:

```text
- generic URI component order: scheme, hierarchical part, optional query, optional fragment
- authority branch uses // authority followed by path-abempty
- no-authority branches use path-absolute, path-rootless, or path-empty
- authority present -> path empty or slash-led
- authority absent -> path does not begin with //
- scheme begins with a letter and then uses the generic admitted scheme characters
- path component content follows pchar-based rules
- query and fragment may be present with zero-length content
- generic authority host may be represented by reg-name, whose generic grammar permits zero-length content
```

The result is deliberately limited to **RFC 3986 generic syntax**. RFC 3986 itself states that its generic grammar is broader than scheme-specific grammars; therefore no scheme-specific URI validity claim is inferred.

## 3. Frozen hard conditions

```text
H1 SCHEME_ABNF
H2 HIER_PART_BRANCH_COMPATIBILITY
H3 COMPONENT_LEXICAL_ABNF
H4 DECLARED_COMPONENT_ROUNDTRIP
```

Staging was executed exactly as precommitted:

```text
H1 and H2 both evaluated first.
If H1 or H2 fails -> H3-H4 NOT_REACHED.
If H1-H2 pass -> H3.
If H3 fails -> H4 NOT_REACHED.
If H1-H3 pass -> H4.
```

## 4. Candidate execution

### R1

```text
DECLARED:
  foo / authority PRESENT_NONEMPTY(example.com) / path /a
  query PRESENT_NONEMPTY(x=1)
  fragment PRESENT_NONEMPTY(frag)
ASSEMBLED:
  foo://example.com/a?x=1#frag
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R2

```text
DECLARED:
  foo / authority PRESENT_NONEMPTY(example.com) / path empty
  query ABSENT / fragment ABSENT
ASSEMBLED:
  foo://example.com
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

The authority branch permits an empty path at generic-syntax level.

### R3

```text
DECLARED:
  foo / authority ABSENT / path /a
  query PRESENT_EMPTY
  fragment ABSENT
ASSEMBLED:
  foo:/a?
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

`QUERY_PRESENT_EMPTY` remains distinct from `QUERY_ABSENT` because the query delimiter is present even though query content has zero length.

### R4

```text
DECLARED:
  foo / authority ABSENT / path a/b
  query ABSENT
  fragment PRESENT_EMPTY
ASSEMBLED:
  foo:a/b#
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

`FRAGMENT_PRESENT_EMPTY` remains distinct from absence.

### R5

```text
DECLARED:
  foo / authority PRESENT_NONEMPTY(example.com) / path a/b
H1 PASS
H2 FAIL
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H2}
```

With declared authority present, the frozen path must be compatible with the authority branch. The candidate was not rescued by allowing the raw characters to parse as a different authority/path decomposition.

### R6

```text
DECLARED:
  foo / authority ABSENT / path //x
H1 PASS
H2 FAIL
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H2}
```

The no-authority declaration was not silently replaced by an authority-bearing parse.

### R7

```text
DECLARED:
  scheme 1foo / authority ABSENT / path /a
H1 FAIL
H2 PASS
H3 NOT_REACHED
H4 NOT_REACHED
RESULT: rejected / {H1}
```

The generic scheme rule requires a leading alphabetic character.

### R8

```text
DECLARED:
  foo / authority ABSENT / path /a
  query PRESENT_NONEMPTY(x=1)
  fragment PRESENT_NONEMPTY(frag)
  declared suffix order: fragment_then_query
RAW CHARACTERS:
  foo:/a#frag?x=1
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
RESULT: rejected / {H4}
```

The raw characters themselves are generically parseable, but they parse as a different component tuple: the intended query is not recovered as the declared query component. Parseability under a different decomposition therefore does not establish successful Synthesis of the frozen tuple.

### R9

```text
DECLARED:
  foo / authority ABSENT / path /a b
H1 PASS
H2 PASS
H3 FAIL
H4 NOT_REACHED
RESULT: rejected / {H3}
```

The raw space is not admitted by the generic pchar-based path grammar.

### R10

```text
DECLARED:
  foo / authority ABSENT / path /a
  query ABSENT
  fragment PRESENT_NONEMPTY(frag)
ASSEMBLED:
  foo:/a#frag
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

### R11

```text
DECLARED:
  foo / authority ABSENT / path empty
  query PRESENT_EMPTY
  fragment PRESENT_EMPTY
ASSEMBLED:
  foo:?#
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
```

Both zero-length optional components are preserved as present rather than collapsed to absence.

### R12

```text
DECLARED:
  foo / authority PRESENT_EMPTY / path /a
  query ABSENT / fragment ABSENT
ASSEMBLED:
  foo:///a
H1 PASS
H2 PASS
H3 PASS
H4 PASS
RESULT: admissible / NONE
EXTERNAL_SCOPE: RFC3986_GENERIC_SYNTAX_ONLY
```

At generic-syntax level, the declared empty authority is structurally distinguishable from authority absence and is compatible with the generic authority/reg-name grammar. No claim is made that a particular registered scheme would accept the same form.

## 5. External admissible family

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{R1,R2,R3,R4,R10,R11,R12}
```

Rejected candidates:

```text
R5 -> {H2}
R6 -> {H2}
R7 -> {H1}
R8 -> {H4}
R9 -> {H3}
```

No rejected candidate was converted into an admissible candidate by changing the declared component boundaries after seeing the result.

## 6. Status and structural distinctions preserved

```text
QUERY_ABSENT != QUERY_PRESENT_EMPTY
FRAGMENT_ABSENT != FRAGMENT_PRESENT_EMPTY
AUTHORITY_ABSENT != AUTHORITY_PRESENT_EMPTY
GENERIC_PARSEABILITY_UNDER_DIFFERENT_DECOMPOSITION
  !=
SYNTHESIS_OF_DECLARED_COMPONENT_TUPLE
```

This application therefore tests a real external grammar against the same status-sensitive and structure-preserving discipline used in constructed Synthesis cases.

## 7. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS:
  SYNTHESIS_ADMISSIBLE

SYNTHESIS_PROTOCOL_CONFORMANCE:
  CONFORMANT

SYNTHESIS_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

No fair external baseline was precommitted, so external success does not become a `GAIN_ESTABLISHED` claim.

## 8. External-scope result

```text
RFC3986_GENERIC_SYNTAX_ADMISSIBLE
!= SCHEME_SPECIFIC_URI_VALIDITY

GENERIC_SYNTACTIC_COMPOSITION
!= RESOURCE_RESOLUTION_SUCCESS

GENERIC_SYNTACTIC_COMPOSITION
!= SECURITY_OR_TRUSTWORTHINESS
```

No claim is made about dereference success, endpoint existence, security, normalization equivalence, ownership, or validity under a particular URI scheme.

## 9. Precommitted scoring

```text
A. source / precommit integrity          8 / 8 PASS
B. exact candidate verdict/failure     12 / 12 PASS
C. structure/status discipline         10 / 10 PASS
D. closure / protocol ledgers           6 / 6 PASS
E. external-scope discipline            4 / 4 PASS

PRECOMMITTED_REQUIRED_CHECKS:          40
PASSED:                                 40
FAILED:                                  0
EXTERNAL_APPLICATION_VERDICT:          PASS
```

No scoring item, candidate, source rule, or scope guard was weakened after execution.

## 10. Evidence increment

```text
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: +1
EXTERNAL_SYNTHESIS_DOMAIN_INCREMENT: +1
EXTERNAL_SYNTHESIS_APPLICATION_PASS_INCREMENT: +1
```

Post-run state:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

The external application is kept separate from the direct constructed-pilot count.

## 11. Protocol pressure and interpretation

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

A PASS here means Protocol v0.1 can be applied without contradiction to this frozen external generic-syntax task. It does not by itself prove that Synthesis must remain an independent method, nor would a failure by itself justify deleting or absorbing the method. Method independence remains a separate boundary/maturity question.

## 12. Limits and next step

This is one external application in one domain, using an externally sourced composition grammar but a project-constructed candidate fixture.

It does not establish:

```text
broad external generality
scheme-specific URI validity
independent evaluator agreement
independent replication
practical superiority
method maturity
```

Next: create a dedicated deterministic same-project retrace/reproducibility case against the immutable `SYN-APP-001` source/precommit/result chain, then consider a second materially different external domain before maturity audit.
