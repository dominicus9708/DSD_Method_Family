# SYN-APP-001 Precommit / RFC 3986 Generic URI Composition

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`

## 1. Evidence identity

```text
CASE_ID: SYN-APP-001
CASE_CLASS: external_application
CASE_ORIGIN: externally_sourced_rule_with_constructed_candidate_fixture
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
BASELINE: none
```

This is the first Synthesis application whose composition grammar is supplied by an external public standard rather than invented by the project.

## 2. Frozen external authority

Primary authority:

```text
RFC 3986 / STD 66
Uniform Resource Identifier (URI): Generic Syntax
T. Berners-Lee, R. Fielding, L. Masinter
January 2005
RFC Editor official text:
https://www.rfc-editor.org/rfc/rfc3986.html
```

Frozen source sections:

```text
Abstract
Section 3     Syntax Components
Section 3.1   Scheme
Section 3.2   Authority
Section 3.3   Path
Section 3.4   Query
Section 3.5   Fragment
Appendix A    Collected ABNF for URI
```

Frozen source facts, paraphrased:

```text
S1 A generic URI is ordered as scheme, hierarchical part, optional query, optional fragment.
S2 The hierarchical part may be authority + path-abempty, path-absolute, path-rootless, or path-empty.
S3 With authority present, the path is empty or slash-led; without authority, the path cannot begin with //.
S4 A scheme starts with a letter and may then contain letters, digits, +, -, or .
S5 Query and fragment grammars permit zero-length content; their delimiters still distinguish present-empty from absence.
S6 Path segments use the RFC pchar grammar; a raw space is not an admitted pchar.
S7 Authority includes host; host may be a reg-name, and the reg-name grammar permits zero-length content at generic-syntax level.
S8 RFC 3986 generic syntax is a superset framework and does not itself establish every scheme-specific generative restriction.
```

No individual URI-scheme specification is activated in this case.

## 3. Frozen Synthesis task

```text
SYNTHESIS_TASK_ID: SYN-APP-TASK-001
TASK_SCOPE:
  compose declared generic-URI component records under the RFC 3986 generic syntax
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_DSD_LAYER_SCOPE:
  Formation-style admission/status bookkeeping only as method interface
DOMAIN_BRIDGE:
  RFC 3986 generic URI syntax
EXTERNAL_STANDARD:
  RFC 3986 / STD 66
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
  static_order_only
COMPOSITION_CANDIDATE_BASIS:
  {R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12}
COMPOSITION_COVERAGE:
  exhaustive relative only to the frozen twelve-candidate fixture
```

The task is **not** arbitrary URI parsing. It is a parts-to-whole Synthesis task: declared component identities and presence states are inputs, the external grammar supplies the composition legality, and an admissible output must preserve those declared component identities at the target resolution.

## 4. Frozen component-status vocabulary

```text
AUTHORITY_STATUS:
  ABSENT
  PRESENT_EMPTY
  PRESENT_NONEMPTY

QUERY_STATUS:
  ABSENT
  PRESENT_EMPTY
  PRESENT_NONEMPTY

FRAGMENT_STATUS:
  ABSENT
  PRESENT_EMPTY
  PRESENT_NONEMPTY
```

Presence and zero-length content are not collapsed.

## 5. Frozen target resolution

A material synthesized URI record includes:

```text
scheme string
authority presence status and authority string when present
path string
query presence status and query string when present
fragment presence status and fragment string when present
component order and delimiter placement
```

Therefore:

```text
ABSENT != PRESENT_EMPTY
raw character string accepted under a different component decomposition
  !=
valid synthesis of the declared component tuple
```

No normalization-equivalence relation is supplied. Distinct declared tuples remain distinct unless RFC generic parsing returns the exact same frozen tuple.

## 6. Frozen composition rule and hard conditions

External composition rule family:

```text
R_RFC3986_GENERIC_URI
```

Hard conditions:

```text
H1 SCHEME_ABNF
   scheme matches the RFC 3986 generic scheme syntax.

H2 HIER_PART_BRANCH_COMPATIBILITY
   if authority is PRESENT_EMPTY or PRESENT_NONEMPTY:
     use the authority branch with // and require an empty or slash-led path compatible with path-abempty.
   if authority is ABSENT:
     use a no-authority branch and do not admit a path beginning with //.

H3 COMPONENT_LEXICAL_ABNF
   authority, path, query, and fragment content each satisfy the relevant generic component grammar for the selected branch.

H4 DECLARED_COMPONENT_ROUNDTRIP
   after static composition under the declared component order/delimiters, generic RFC 3986 parsing must recover exactly the frozen tuple of component presence states and values.
   A character string that is generically parseable only by changing the declared component decomposition fails H4.
```

Evaluation staging:

```text
H1 and H2 are structural prerequisites and are both evaluated.
If H1 or H2 fails, H3-H4 are NOT_REACHED and do not enter FAILURE_SET.
If H1 and H2 pass, evaluate H3.
If H3 fails, H4 is NOT_REACHED.
If H1-H3 pass, evaluate H4.
```

## 7. Frozen candidates and expected results

```text
R1
  scheme: foo
  authority: PRESENT_NONEMPTY("example.com")
  path: "/a"
  query: PRESENT_NONEMPTY("x=1")
  fragment: PRESENT_NONEMPTY("frag")
  suffix order: query_then_fragment
  assembled target: foo://example.com/a?x=1#frag
  expected: admissible / NONE

R2
  scheme: foo
  authority: PRESENT_NONEMPTY("example.com")
  path: ""
  query: ABSENT
  fragment: ABSENT
  assembled target: foo://example.com
  expected: admissible / NONE

R3
  scheme: foo
  authority: ABSENT
  path: "/a"
  query: PRESENT_EMPTY("")
  fragment: ABSENT
  assembled target: foo:/a?
  expected: admissible / NONE

R4
  scheme: foo
  authority: ABSENT
  path: "a/b"
  query: ABSENT
  fragment: PRESENT_EMPTY("")
  assembled target: foo:a/b#
  expected: admissible / NONE

R5
  scheme: foo
  authority: PRESENT_NONEMPTY("example.com")
  path: "a/b"
  query: ABSENT
  fragment: ABSENT
  expected: rejected / {H2}
  H3-H4: NOT_REACHED

R6
  scheme: foo
  authority: ABSENT
  path: "//x"
  query: ABSENT
  fragment: ABSENT
  expected: rejected / {H2}
  H3-H4: NOT_REACHED

R7
  scheme: 1foo
  authority: ABSENT
  path: "/a"
  query: ABSENT
  fragment: ABSENT
  expected: rejected / {H1}
  H2: PASS
  H3-H4: NOT_REACHED

R8
  scheme: foo
  authority: ABSENT
  path: "/a"
  query: PRESENT_NONEMPTY("x=1")
  fragment: PRESENT_NONEMPTY("frag")
  suffix order: fragment_then_query
  raw assembled characters: foo:/a#frag?x=1
  expected: rejected / {H4}
  rationale frozen:
    the raw string can be parsed generically, but not as the declared tuple;
    the intended query is absorbed into fragment data under that order.

R9
  scheme: foo
  authority: ABSENT
  path: "/a b"
  query: ABSENT
  fragment: ABSENT
  expected: rejected / {H3}
  H4: NOT_REACHED

R10
  scheme: foo
  authority: ABSENT
  path: "/a"
  query: ABSENT
  fragment: PRESENT_NONEMPTY("frag")
  assembled target: foo:/a#frag
  expected: admissible / NONE

R11
  scheme: foo
  authority: ABSENT
  path: ""
  query: PRESENT_EMPTY("")
  fragment: PRESENT_EMPTY("")
  suffix order: query_then_fragment
  assembled target: foo:?#
  expected: admissible / NONE

R12
  scheme: foo
  authority: PRESENT_EMPTY("")
  path: "/a"
  query: ABSENT
  fragment: ABSENT
  assembled target: foo:///a
  expected: admissible / NONE at RFC 3986 generic-syntax level only
```

Expected admissible family:

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{R1,R2,R3,R4,R10,R11,R12}
```

Expected ledgers:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 8. Frozen external-scope guards

A PASS must preserve all of the following:

```text
RFC3986_GENERIC_SYNTAX_ADMISSIBLE
!= SCHEME_SPECIFIC_URI_VALIDITY

GENERIC_SYNTACTIC_COMPOSITION
!= RESOURCE_RESOLUTION_SUCCESS

GENERIC_SYNTACTIC_COMPOSITION
!= SECURITY_OR_TRUSTWORTHINESS

PRESENT_EMPTY
!= ABSENT
```

No claim is made about HTTP, HTTPS, FTP, URN, or any other particular scheme.
No normalization, dereference, reachability, security, ownership, or application-level semantic claim is scored.

## 9. Precommitted scoring

Total required checks: **40**.

```text
A. source / precommit integrity: 8
  A1 RFC 3986 official authority fixed
  A2 source sections fixed
  A3 generic-syntax-only scope fixed
  A4 twelve candidates fixed
  A5 coverage fixed as exhaustive only to fixture
  A6 H1-H4 and staging fixed
  A7 target resolution/presence states fixed
  A8 no baseline; method gain fixed to NOT_ASSESSED

B. exact candidate verdict/failure checks: 12
  B1-B12 exact R1-R12 verdict and FAILURE_SET behavior

C. structure/status discipline: 10
  C1 R3 query PRESENT_EMPTY preserved
  C2 R4 fragment PRESENT_EMPTY preserved
  C3 R11 query and fragment both PRESENT_EMPTY preserved
  C4 R12 authority PRESENT_EMPTY preserved
  C5 R5 not rescued by reparsing into a different authority/path tuple
  C6 R6 not rescued by converting declared no-authority path into authority syntax
  C7 R8 rejected because declared query/fragment tuple is not round-tripped
  C8 R9 raw-space path rejected lexically
  C9 no unsupplied normalization/equivalence used
  C10 no scheme-specific restriction invented

D. closure / protocol ledgers: 6
  D1 admissible family exactly {R1,R2,R3,R4,R10,R11,R12}
  D2 terminal = SYNTHESIS_ADMISSIBLE
  D3 conformance = CONFORMANT
  D4 method gain = NOT_ASSESSED
  D5 exhaustive claim limited to the twelve-candidate fixture
  D6 no neighboring-method or time-resolved process claim absorbed

E. external-scope discipline: 4
  E1 generic syntax not upgraded to scheme-specific validity
  E2 no resource-resolution claim
  E3 no security/trustworthiness claim
  E4 external-source verdict kept separate from DSD protocol conformance
```

Decision:

```text
40/40 -> EXTERNAL_APPLICATION_VERDICT: PASS
otherwise -> EXTERNAL_APPLICATION_VERDICT: FAIL
```

## 10. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
EXTERNAL_SYNTHESIS_DOMAINS: 0
REPRODUCIBILITY_CASES: 0
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

A 40/40 PASS may add exactly:

```text
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: +1
EXTERNAL_SYNTHESIS_DOMAIN_INCREMENT: +1
EXTERNAL_SYNTHESIS_APPLICATION_PASS_INCREMENT: +1
```

It does not automatically change the direct constructed-pilot count, method maturity, independent-validation status, or practical-gain status.
