# CLS-APP-001 Precommit / DSD 분류론 First External Application 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-13**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-APP-001
CASE_CLASS: first_external_classification_application
CASE_ORIGIN: external_public_standard_and_registry
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_DOMAIN: HTTP semantics / HTTP status-code classification
BASELINE: none
CLASSIFICATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Purpose: test Classification Protocol v0.1 against an externally fixed classification rule and externally supplied status-code records rather than a project-constructed class schema and subject set.

This case does **not** test superiority. It tests whether DSD Classification can preserve and execute an external standard's class criteria, coverage semantics, registry provenance, and subject records without importing label-based or registry-status-based meaning into class membership.

## 2. Frozen external sources

### S1 — RFC 9110

```text
TITLE: HTTP Semantics
DOCUMENT: RFC 9110
DATE: June 2022
SECTION: 15 Status Codes
SOURCE_URL: https://www.rfc-editor.org/rfc/rfc9110.html#section-15
```

Frozen source facts used by this case:

```text
F1 status code is a three-digit integer code;
F2 valid HTTP status codes are within 100..599 inclusive;
F3 the first digit defines the response class;
F4 the last two digits have no categorization role;
F5 the five first-digit classes are 1xx, 2xx, 3xx, 4xx, 5xx;
F6 an unrecognized status code still has a class indicated by the first digit;
F7 RFC 9110 explicitly uses 471 as an example of an unrecognized 4xx status code and says it can be treated as the 400 class for class-level handling.
```

### S2 — IANA HTTP Status Code Registry

```text
TITLE: Hypertext Transfer Protocol (HTTP) Status Code Registry
SOURCE_URL: https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml
SOURCE_RETRIEVAL_DATE: 2026-09-13
REGISTRY_LAST_UPDATED_AS_OBSERVED: 2025-09-15
REFERENCE: RFC 9110 Section 16.2.1
```

Frozen registry rows used by this case:

```text
103 -> Early Hints
204 -> No Content
304 -> Not Modified
418 -> (Unused)
511 -> Network Authentication Required
452-499 -> Unassigned
```

The `452-499 -> Unassigned` range is used only to preserve the registry-assignment status of `471`. It is not used to deny `471` a first-digit response class.

No other external source may be introduced after execution begins to repair a failed frozen result.

## 3. Frozen Classification task

```text
CLASSIFICATION_TASK_ID: CLS-APP-001-HTTP-STATUS-CLASS
TARGET_RESOLUTION: RFC 9110 response-status class by first digit
CLASSIFICATION_UNIVERSE: HTTP status-code values interpreted at RFC 9110 class level
CLASS_SCHEMA_ID_AND_VERSION: RFC9110-HTTP-STATUS-CLASS-SCHEMA-v1
CLASS_SCHEMA_STATUS: externally_fixed
SCHEMA_COVERAGE_CLAIM: closed_world_claim at response-class resolution for 100..599
CLASS_RELATION_SEMANTICS: disjoint
MUTUAL_EXCLUSION_RULES: one status-code value has exactly one first-digit class in 100..599
CRITERION_COMPOSITION_RULE: single numeric range predicate
DECISION_RULE: assign the unique class whose first-digit range contains the supplied status code
FEATURE_BASIS: numeric status_code
FEATURE_SOURCE_AND_PROVENANCE: RFC 9110 and frozen IANA registry rows
DESCRIPTION_FIELD_ROLE: non-authoritative side record
REGISTRY_ASSIGNMENT_STATUS_ROLE: non-authoritative for response-class membership
TARGET_DSD_LAYER_SCOPE: method-level classification only; no Formation/Property/Aggregation/Dynamics layer required
DOMAIN_BRIDGE: supplied HTTP integer status-code feature -> RFC 9110 numeric class predicate
EXTERNAL_STANDARD: RFC 9110 Section 15
```

External class schema:

```text
HTTP-1XX-INFORMATIONAL iff 100 <= code <= 199
HTTP-2XX-SUCCESSFUL    iff 200 <= code <= 299
HTTP-3XX-REDIRECTION   iff 300 <= code <= 399
HTTP-4XX-CLIENT-ERROR  iff 400 <= code <= 499
HTTP-5XX-SERVER-ERROR  iff 500 <= code <= 599
```

Closure claim is limited to response-class resolution. This case does not claim that every integer in 100..599 is currently assigned a distinct registered IANA status-code meaning.

Core separation:

```text
STATUS_DESCRIPTION != CLASS_CRITERION
REGISTRY_ASSIGNED != RESPONSE_CLASS_MEMBER
REGISTRY_UNASSIGNED != CLASSLESS
LAST_TWO_DIGITS != CLASS_CRITERION
UNRECOGNIZED_STATUS != NO_RESPONSE_CLASS
```

## 4. Frozen external subject set

Six externally sourced subject records are frozen.

```text
E1
  status_code: 103
  external_description: Early Hints
  registry_status: assigned
  expected_class: HTTP-1XX-INFORMATIONAL
  expected_membership_status: CLASSIFIED_SINGLE

E2
  status_code: 204
  external_description: No Content
  registry_status: assigned
  expected_class: HTTP-2XX-SUCCESSFUL
  expected_membership_status: CLASSIFIED_SINGLE

E3
  status_code: 304
  external_description: Not Modified
  registry_status: assigned
  expected_class: HTTP-3XX-REDIRECTION
  expected_membership_status: CLASSIFIED_SINGLE

E4
  status_code: 418
  external_description: (Unused)
  registry_status: assigned registry row with unused description
  expected_class: HTTP-4XX-CLIENT-ERROR
  expected_membership_status: CLASSIFIED_SINGLE

E5
  status_code: 511
  external_description: Network Authentication Required
  registry_status: assigned
  expected_class: HTTP-5XX-SERVER-ERROR
  expected_membership_status: CLASSIFIED_SINGLE

E6
  status_code: 471
  external_description: unrecognized example in RFC 9110
  registry_status: unassigned under frozen IANA 452-499 range
  expected_class: HTTP-4XX-CLIENT-ERROR
  expected_membership_status: CLASSIFIED_SINGLE
```

E3, E4, E5, and E6 intentionally pressure label/registry leakage:

```text
"Not Modified" does not move 304 outside 3xx;
"(Unused)" does not make 418 classless;
"Network Authentication Required" does not move 511 into 4xx;
unassigned/unrecognized 471 still has 4xx class-level handling by first digit.
```

## 5. Frozen operation

For each subject:

```text
1. preserve exact externally supplied integer status_code and source provenance;
2. preserve external description and registry-assignment status as side records;
3. check code against the five frozen RFC numeric class predicates;
4. assign exactly one class if exactly one predicate is satisfied;
5. do not use description wording as criterion;
6. do not use IANA assignment/unassignment as response-class criterion;
7. record the criterion trace and source record;
8. return Classification Protocol conformance separately from membership status.
```

No semantic inference from English descriptions is allowed.
No new class may be generated.
No range boundary may be changed after execution begins.

## 6. Expected task-level outputs

```text
E1 103 -> HTTP-1XX-INFORMATIONAL / CLASSIFIED_SINGLE
E2 204 -> HTTP-2XX-SUCCESSFUL    / CLASSIFIED_SINGLE
E3 304 -> HTTP-3XX-REDIRECTION   / CLASSIFIED_SINGLE
E4 418 -> HTTP-4XX-CLIENT-ERROR  / CLASSIFIED_SINGLE
E5 511 -> HTTP-5XX-SERVER-ERROR  / CLASSIFIED_SINGLE
E6 471 -> HTTP-4XX-CLIENT-ERROR  / CLASSIFIED_SINGLE
```

Additional expected records:

```text
E3 DESCRIPTION_OVERRIDE: no
E4 UNUSED_DESCRIPTION_CAUSES_CLASSLESS: no
E5 DESCRIPTION_WORDING_OVERRIDES_FIRST_DIGIT: no
E6 REGISTRY_UNASSIGNED: yes
E6 RESPONSE_CLASS_MEMBER: yes, 4xx
E6 UNIVERSAL_REGISTERED_STATUS_CLAIM: no
```

All six DSD results are expected to be `CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed correctly.

## 7. Frozen scoring

Total required checks: **50**.

```text
A. source / precommit / immutability: 10
  A1 Classification Protocol commit fixed
  A2 RFC 9110 source fixed
  A3 IANA registry source fixed
  A4 source retrieval/version metadata fixed
  A5 six-subject set fixed
  A6 five-class criteria fixed
  A7 471 unrecognized/unassigned handling fixed
  A8 expected outputs fixed
  A9 scoring fixed
  A10 no post-hoc task/source/criterion changes

B. DSD Classification execution: 18
  B1-B6 exact membership status for E1-E6
  B7-B12 exact class assignment for E1-E6
  B13 E3 description does not override 3xx criterion
  B14 E4 unused description does not cause classless/out-of-scope result
  B15 E5 authentication wording does not override 5xx criterion
  B16 E6 unassigned registry status remains separate from 4xx response class
  B17 all six DSD executions CONFORMANT
  B18 no hidden bridge, label criterion, or generated class introduced

C. external-source correctness and provenance: 14
  C1 RFC 9110 range/class rule preserved
  C2 1xx class semantics preserved
  C3 2xx class semantics preserved
  C4 3xx class semantics preserved
  C5 4xx class semantics preserved
  C6 5xx class semantics preserved
  C7 IANA 103 row preserved
  C8 IANA 204 row preserved
  C9 IANA 304 row preserved
  C10 IANA 418 row preserved
  C11 IANA 511 row preserved
  C12 IANA 452-499 unassigned range preserved for 471 registry status
  C13 RFC 9110 471 example preserved at class level
  C14 source identity and retrieval metadata retained in result

D. scope / evidence discipline: 8
  D1 method gain remains NOT_ASSESSED
  D2 external-origin evidence not relabeled independent validation
  D3 no independent replication claim
  D4 no practical-superiority claim
  D5 no maturity promotion from this case alone
  D6 no universal HTTP semantic reconstruction claim
  D7 no method survival/merger/absorption/deletion conclusion
  D8 no Protocol/shared-core revision unless a real contradiction appears
```

Decision:

```text
50/50 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

If a fixture/source-reading defect is found, preserve this Case ID as failed and correct prospectively under a new Case ID. Do not rewrite the frozen source interpretation after execution to obtain PASS.

## 8. Evidence-count lock

Before execution:

```text
DIRECT_CLASSIFICATION_PILOTS: 5
NO_GAIN_CLASSIFICATION_CASES: 2
BASELINE_CLASSIFICATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
EXTERNAL_CLASSIFICATION_DOMAINS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

A 50/50 PASS may add exactly:

```text
EXTERNAL_CLASSIFICATION_APPLICATION_INCREMENT: +1
EXTERNAL_CLASSIFICATION_DOMAIN_INCREMENT: +1
```

It does not by itself increment same-project reproducibility, independent validation, independent replication, baseline gain, or maturity.
