# SPEC-CH-008 — `dependentRequired` Label-Withheld Cross-Validator Challenge Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Evidence class: method-specific constructed challenge
External normative basis: JSON Schema Draft 2020-12 Validation §6.5.4 `dependentRequired`
Independent implementation used only after prediction freeze: Python `jsonschema` Draft202012Validator

## 1. Purpose

Test whether DSD Specification v1.0 can represent and apply conditional property dependencies without false activation, false bidirectionality, or irrelevant-ledger expansion, and compare the frozen DSD predictions against an implementation result that is not consulted until after prediction commit.

This is not an independent evaluator test because the same assistant constructs and interprets the cases. It is a **label-withheld implementation cross-check**.

## 2. Locked normative atoms

```text
DR1  If trigger property p is present in an object instance and dependentRequired[p]=[q1,...,qn], every qi must be present.
DR2  If trigger property p is absent, its dependency list is inactive.
DR3  Multiple present trigger properties activate independently; every active dependency list must be satisfied.
DR4  Dependency direction is not automatically symmetric.
DR5  An empty dependency list adds no required property.
DR6  A dependency may name a property not otherwise declared by `properties`; presence, not declaration, is the assertion tested here.
DR7  `dependentRequired` does not invalidate non-object instances solely by this keyword.
DR8  Property presence is evaluated at the object level to which the keyword applies; nested same-named properties do not activate a root dependency.
```

## 3. Locked DSD interface

```text
FORMATION_LAYER: not used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
OPTIONAL_SPECIALIZATION: none
```

Expected active conditional field:

```text
DEPENDENCIES
```

Expected inactive unless genuinely needed:

```text
PRECEDENCE_OR_PRIORITY
SOURCE_OPENNESS_STATUS
DOWNSTREAM_DETERMINACY_STATUS
ALLOWED_ALTERNATIVES
PROHIBITED_STATES
```

Validation standard is inherited from JSON Schema Draft 2020-12; atom-level repetition is not required.

## 4. Locked cases

Every case schema contains `$schema: https://json-schema.org/draft/2020-12/schema` and the shown `dependentRequired` object. No other assertion keyword is present unless explicitly stated.

```text
C01 schema {a:[b]}                    data {a:1,b:2}
C02 schema {a:[b]}                    data {a:1}
C03 schema {a:[b]}                    data {b:2}
C04 schema {a:[]}                     data {a:1}
C05 schema {a:[b], c:[d]}             data {a:1,b:2,c:3,d:4}
C06 schema {a:[b], c:[d]}             data {a:1,b:2,c:3}
C07 schema {a:[b]}                    data {b:2}
C08 schema {a:[b]}                    data {a:1}
C09 schema {a:[a]}                    data {a:1}
C10 schema {a:[b,c]}                  data {a:1,b:2,c:3}
C11 schema {a:[b,c]}                  data {a:1,b:2}
C12 schema {a:[b]}                    data {x:{a:1}}
C13 schema {a:[b]}                    data ["a"]
C14 schema {a:[b]}                    data "a"
C15 schema {a:[b]}                    data 7
C16 schema {a:[b]}                    data null
```

C03/C07 and C02/C08 are deliberate repeated boundary controls. They may not be removed as duplicates after reveal; agreement across repeated controls is itself checked.

## 5. Prediction classes

Before the cross-validator is invoked, every case must be frozen as exactly one of:

```text
VALID
INVALID
UNRESOLVED
```

No post-reveal prediction change is permitted.

## 6. Primary score and diagnostics

```text
CROSS_VALIDATOR_MATCHES / 16

FALSE_DEPENDENCY_ACTIVATION_ON_ABSENT_TRIGGER
MISSED_ACTIVE_DEPENDENCY
FALSE_BIDIRECTIONAL_INFERENCE
EMPTY_DEPENDENCY_LIST_ERROR
SELF_DEPENDENCY_ERROR
MULTI_TRIGGER_COMBINATION_ERROR
ROOT_NESTED_SCOPE_ERROR
FALSE_FAILURE_ON_NON_OBJECT
POST_REVEAL_PREDICTION_CHANGE
```

Repeated controls must agree with each other before reveal.

## 7. Guardrails

```text
G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for this narrow assertion task
G3 DETAIL_PROPORTIONALITY: active
G4 VIEWPOINT_SEPARATION: inactive unless a derivative claim is introduced
```

## 8. Anti-post-hoc and limits

No score threshold automatically promotes method maturity. All mismatch or `UNRESOLVED` results are preserved.

The cross-validator may reveal an implementation difference or a DSD reasoning error, but it does not replace the normative JSON Schema specification.

Not established by this challenge:

```text
independent evaluator agreement
full JSON Schema conformance
external real-world application evidence
engineering productivity gain
superiority over JSON Schema tooling
```
