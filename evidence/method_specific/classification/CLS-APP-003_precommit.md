# CLS-APP-003 Precommit / DSD 분류론 Additional External Application — UNESCO World Heritage Property Types

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-14**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-APP-003
CASE_CLASS: additional_external_classification_application
CASE_ORIGIN: external_public_intergovernmental_standard_and_registry
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_DOMAIN: cultural-natural heritage property-type classification
BASELINE: none
CLASSIFICATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Purpose: test Classification Protocol v0.1 in a third materially different external domain after HTTP response classes and NIST security-impact categorization.

This case uses a finite symbolic criterion set rather than a numeric interval or high-water-mark vector. The externally fixed decision is based on whether an inscribed World Heritage property satisfies cultural criteria `(i)-(vi)`, natural criteria `(vii)-(x)`, or at least one criterion from each family.

The case specifically pressures label leakage and coarse property-type collapse. A property that is physically a mountain must not be called a natural World Heritage property merely from its name or physical appearance when its frozen inscription criteria are cultural only.

## 2. Frozen external sources

All sources are official UNESCO World Heritage Centre records.

### U1 — World Heritage criteria-family rule

```text
SOURCE: UNESCO World Heritage Centre — Understanding World Heritage / Criteria for inscription
URL: https://whc.unesco.org/en/renewable-energy/understanding-wh/
```

Frozen source facts:

```text
U1-F1 World Heritage properties are inscribed under at least one of ten criteria.
U1-F2 criteria (i)-(vi) refer to cultural values.
U1-F3 criteria (vii)-(x) apply to natural values.
U1-F4 mixed World Heritage properties must meet at least one cultural and one natural criterion.
```

### U2 — Taj Mahal

```text
URL: https://whc.unesco.org/en/list/252
PROPERTY_ID: 252
CRITERIA: (i)
```

### U3 — Fujisan, sacred place and source of artistic inspiration

```text
URL: https://whc.unesco.org/en/list/1418
PROPERTY_ID: 1418
CRITERIA: (iii)(vi)
```

### U4 — Great Barrier Reef

```text
URL: https://whc.unesco.org/en/list/154
PROPERTY_ID: 154
CRITERIA: (vii)(viii)(ix)(x)
```

### U5 — Historic Sanctuary of Machu Picchu

```text
URL: https://whc.unesco.org/en/list/274
PROPERTY_ID: 274
CRITERIA: (i)(iii)(vii)(ix)
```

No external source may be added after execution begins to repair a failed frozen result.

## 3. Frozen Classification task

```text
CLASSIFICATION_TASK_ID: CLS-APP-003-UNESCO-WH-PROPERTY-TYPE
TARGET_RESOLUTION: World Heritage property type derived from frozen inscription-criterion family membership
CLASSIFICATION_UNIVERSE: the four frozen inscribed properties U2-U5
CLASS_SCHEMA_ID_AND_VERSION: UNESCO-WH-CRITERIA-FAMILY-v1
CLASS_SCHEMA_STATUS: externally_fixed
SCHEMA_COVERAGE_CLAIM: externally_fixed_scope_only
CLASS_RELATION_SEMANTICS: three mutually exclusive target property-type classes at this resolution
MUTUAL_EXCLUSION_RULES: one and only one of CULTURAL / NATURAL / MIXED for each frozen criteria set under the decision rule
CRITERION_COMPOSITION_RULE: set-family membership over inscription criteria
DECISION_RULE:
  if criteria_set intersects {(i)..(vi)} and does not intersect {(vii)..(x)} -> CULTURAL_WORLD_HERITAGE_PROPERTY;
  if criteria_set intersects {(vii)..(x)} and does not intersect {(i)..(vi)} -> NATURAL_WORLD_HERITAGE_PROPERTY;
  if criteria_set intersects both families -> MIXED_WORLD_HERITAGE_PROPERTY
FEATURE_BASIS: exact externally listed inscription-criterion set per property
FEATURE_SOURCE_AND_PROVENANCE: UNESCO U1-U5 frozen records
TARGET_DSD_LAYER_SCOPE: method-level classification only
DOMAIN_BRIDGE: UNESCO symbolic criterion identifiers -> criterion-family membership -> property-type class
EXTERNAL_STANDARD: UNESCO World Heritage criteria framework and property registry records
```

This task classifies **already inscribed frozen properties by property type**. It does not decide whether a new property should be inscribed or whether Outstanding Universal Value, integrity, authenticity, protection, or management requirements are satisfied.

Core separations:

```text
PROPERTY_TYPE_CLASSIFICATION != INSCRIPTION_ELIGIBILITY_DECISION
CRITERIA_FAMILY_MEMBERSHIP != FULL_OUTSTANDING_UNIVERSAL_VALUE_ASSESSMENT
PROPERTY_NAME_OR_PHYSICAL_APPEARANCE != PROPERTY_TYPE_CRITERION
CULTURAL_CRITERIA_COUNT != CULTURAL_VALUE_MAGNITUDE
NATURAL_CRITERIA_COUNT != NATURAL_VALUE_MAGNITUDE
MIXED_PROPERTY != UNSTRUCTURED_LABEL_COMBINATION
SAME_PROPERTY_TYPE != SAME_CRITERIA_SET
SAME_CRITERIA_SET != SAME_PROPERTY_IDENTITY
```

## 4. Frozen external subject set

```text
W1 Taj Mahal
  UNESCO property id: 252
  criteria_set: {(i)}
  expected criteria-family membership: cultural only
  expected property type: CULTURAL_WORLD_HERITAGE_PROPERTY

W2 Fujisan, sacred place and source of artistic inspiration
  UNESCO property id: 1418
  criteria_set: {(iii),(vi)}
  expected criteria-family membership: cultural only
  expected property type: CULTURAL_WORLD_HERITAGE_PROPERTY

W3 Great Barrier Reef
  UNESCO property id: 154
  criteria_set: {(vii),(viii),(ix),(x)}
  expected criteria-family membership: natural only
  expected property type: NATURAL_WORLD_HERITAGE_PROPERTY

W4 Historic Sanctuary of Machu Picchu
  UNESCO property id: 274
  criteria_set: {(i),(iii),(vii),(ix)}
  expected criteria-family membership: cultural + natural
  expected property type: MIXED_WORLD_HERITAGE_PROPERTY
```

W2 is an explicit label/appearance stressor. The subject is a stratovolcano/mountain, but the frozen UNESCO inscription criteria are `(iii)(vi)`, both in the cultural family. The run must therefore classify W2 as cultural at this target resolution rather than infer natural status from the object name or physical form.

## 5. Frozen operation

For each W1-W4:

```text
1. preserve UNESCO property identity and exact criteria set;
2. map each criterion identifier only to the frozen U1 criterion family;
3. evaluate whether the criteria set intersects cultural, natural, or both families;
4. apply the frozen mutually exclusive property-type decision rule;
5. emit one property-type class plus criterion-family trace and source provenance;
6. do not infer property type from name, geography, physical appearance, country, narrative description, or criterion count;
7. do not reinterpret a mixed criteria set as two independent property identities;
8. do not infer inscription eligibility beyond the frozen already-inscribed subject record.
```

Forbidden during execution:

```text
new criterion family
new property-type class
name-based classification
physical-appearance-based classification
criterion-count weighting
using narrative prose to override frozen criteria identifiers
using current tourism/management/state-of-conservation status as a property-type criterion
claiming that this task reproduces full UNESCO inscription evaluation
new external source introduced after execution begins to repair a mismatch
```

## 6. Frozen expected outputs

```text
W1 Taj Mahal
  criteria family: cultural only
  -> CULTURAL_WORLD_HERITAGE_PROPERTY
  -> CLASSIFIED_SINGLE

W2 Fujisan
  criteria family: cultural only
  -> CULTURAL_WORLD_HERITAGE_PROPERTY
  -> CLASSIFIED_SINGLE

W3 Great Barrier Reef
  criteria family: natural only
  -> NATURAL_WORLD_HERITAGE_PROPERTY
  -> CLASSIFIED_SINGLE

W4 Historic Sanctuary of Machu Picchu
  criteria family: cultural + natural
  -> MIXED_WORLD_HERITAGE_PROPERTY
  -> CLASSIFIED_SINGLE
```

Additional frozen distinctions:

```text
W1_TYPE_EQUALS_W2_TYPE: yes
W1_CRITERIA_SET_EQUALS_W2_CRITERIA_SET: no
W1_PROPERTY_ID_EQUALS_W2_PROPERTY_ID: no
W2_NATURAL_SOUNDING_OR_PHYSICAL_FORM_OVERRIDES_CRITERIA: no
W3_HAS_CULTURAL_CRITERION: no
W4_HAS_CULTURAL_CRITERION: yes
W4_HAS_NATURAL_CRITERION: yes
W4_MIXED_DUE_TO_BOTH_FAMILIES: yes
```

All four records are expected to be `CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed faithfully.

## 7. Frozen scoring

Total required checks: **60**.

```text
A. source / precommit / immutability: 10
  A1 Classification Protocol commit fixed
  A2 U1 criteria-family rule fixed
  A3 W1 UNESCO property record fixed
  A4 W2 UNESCO property record fixed
  A5 W3 UNESCO property record fixed
  A6 W4 UNESCO property record fixed
  A7 four-subject set fixed
  A8 decision rule and expected outputs fixed
  A9 scoring fixed
  A10 no post-hoc source/task/rule changes

B. criteria-set preservation: 16
  B1-B4 W1 exact identity / criteria / family / provenance
  B5-B8 W2 exact identity / criteria / family / provenance
  B9-B12 W3 exact identity / criteria / family / provenance
  B13-B16 W4 exact identity / criteria / family / provenance

C. property-type classification: 16
  C1-C4 W1 cultural-only derivation / cultural class / single membership / conformance
  C5-C8 W2 cultural-only derivation / cultural class / single membership / conformance
  C9-C12 W3 natural-only derivation / natural class / single membership / conformance
  C13-C16 W4 both-family derivation / mixed class / single membership / conformance

D. cross-case distinctions and anti-leakage: 10
  D1 W1 and W2 same type retained
  D2 W1 and W2 unequal criteria sets retained
  D3 W1 and W2 distinct identities retained
  D4 Fujisan physical form/name does not override criteria-family classification
  D5 W3 contains no frozen cultural criterion
  D6 W4 contains at least one cultural criterion
  D7 W4 contains at least one natural criterion
  D8 mixed classification justified by both families rather than label concatenation
  D9 property-type class kept separate from full inscription eligibility
  D10 criterion count not interpreted as value magnitude

E. scope / evidence discipline: 8
  E1 method gain remains NOT_ASSESSED
  E2 external-origin evidence not relabeled independent validation
  E3 no independent replication claim
  E4 no practical-superiority claim
  E5 no maturity promotion from this case alone
  E6 no universal UNESCO classification claim beyond frozen rule and subjects
  E7 no method survival/merger/absorption/deletion conclusion
  E8 no Protocol/shared-core revision unless a real contradiction appears
```

Decision:

```text
60/60 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

If a source, task, or protocol mismatch is found, preserve this Case ID as failed and correct prospectively under a new Case ID. Do not rewrite the frozen task after execution to obtain PASS.

## 8. Evidence-count lock

Before execution:

```text
DIRECT_CLASSIFICATION_PILOTS: 5
NO_GAIN_CLASSIFICATION_CASES: 2
BASELINE_CLASSIFICATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
EXTERNAL_CLASSIFICATION_APPLICATIONS: 2
EXTERNAL_CLASSIFICATION_DOMAINS: 2
REPRODUCIBILITY_CASES: 1
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: validation_in_progress
```

A 60/60 PASS may add exactly:

```text
EXTERNAL_CLASSIFICATION_APPLICATION_INCREMENT: +1
EXTERNAL_CLASSIFICATION_DOMAIN_INCREMENT: +1
```

It does not by itself increment direct constructed pilots, reproducibility, independent validation, independent replication, comparative gain, or maturity.
