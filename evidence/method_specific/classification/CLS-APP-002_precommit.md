# CLS-APP-002 Precommit / DSD 분류론 Additional External Application — NIST Security Impact Categorization

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-14**  
Method: **DSD Classification / DSD 분류론**  
Protocol: **Classification Protocol v0.1**  
Protocol commit: `c20be5f2507a766998ac346aeed2fcef8a045afc`

## 1. Evidence identity

```text
CASE_ID: CLS-APP-002
CASE_CLASS: additional_external_classification_application
CASE_ORIGIN: external_public_federal_standards
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_DOMAIN: information-security impact categorization
BASELINE: none
CLASSIFICATION_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Purpose: test Classification Protocol v0.1 against a materially different external classification structure from `CLS-APP-001`. This case uses externally fixed multi-axis security categories, a high-water-mark composition rule, and an externally documented state adjustment rather than a single numeric range rule.

This case does not test superiority. It tests whether DSD Classification can preserve external information-type security-category profiles, derive information-system profiles under the external high-water-mark rule, preserve a documented post-derivation adjustment as a distinct state, and separately classify overall system impact without collapsing vector profile, scalar impact class, source-object identity, or state history.

## 2. Frozen external sources

### S1 — NIST FIPS 199

```text
TITLE: Standards for Security Categorization of Federal Information and Information Systems
DOCUMENT: FIPS PUB 199
DATE: February 2004
SOURCE_URL: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf
CSRC_URL: https://csrc.nist.gov/pubs/fips/199/final
```

Frozen source facts used by this case:

```text
F1 information-type security category is a three-objective profile:
   confidentiality, integrity, availability;
F2 information-type objective values may be LOW, MODERATE, HIGH, or NOT APPLICABLE;
F3 NOT APPLICABLE is limited to confidentiality for an information type;
F4 an information-system security category also uses confidentiality, integrity, availability;
F5 information-system objective values are LOW, MODERATE, or HIGH; NOT APPLICABLE is not permitted at system level;
F6 the information-system category is initially formed by taking, objective by objective, the highest impact value among resident information types;
F7 Example 4 acquisition system uses contract information (MODERATE, MODERATE, LOW) and routine administrative information (LOW, LOW, LOW), yielding system category (MODERATE, MODERATE, LOW);
F8 Example 5 SCADA system uses sensor data (NA, HIGH, HIGH) and routine administrative information (LOW, LOW, LOW), yielding initial system category (LOW, HIGH, HIGH);
F9 Example 5 then documents a management adjustment raising SCADA confidentiality from LOW to MODERATE, giving final system category (MODERATE, HIGH, HIGH).
```

### S2 — NIST FIPS 200

```text
TITLE: Minimum Security Requirements for Federal Information and Information Systems
DOCUMENT: FIPS PUB 200
DATE: March 2006
SOURCE_URL: https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.200.pdf
```

Frozen overall-impact rules:

```text
LOW-IMPACT SYSTEM:
  confidentiality = LOW
  AND integrity = LOW
  AND availability = LOW

MODERATE-IMPACT SYSTEM:
  at least one objective = MODERATE
  AND no objective = HIGH

HIGH-IMPACT SYSTEM:
  at least one objective = HIGH
```

The system impact class is therefore a scalar classification derived from the three-objective system security-category profile; the scalar class is not identical to that profile.

No other external source may be introduced after execution begins to repair a failed frozen result.

## 3. Frozen Classification task

```text
CLASSIFICATION_TASK_ID: CLS-APP-002-NIST-SECURITY-IMPACT
TARGET_RESOLUTION:
  A. per-objective information-type impact profile
  B. per-objective information-system security-category profile
  C. overall information-system impact class
CLASSIFICATION_UNIVERSE:
  frozen FIPS 199 Example 4 and Example 5 records listed below
CLASS_SCHEMA_ID_AND_VERSION: FIPS199-FIPS200-SECURITY-CATEGORIZATION-v1
CLASS_SCHEMA_STATUS: externally_fixed
SCHEMA_COVERAGE_CLAIM: externally_fixed_scope_only
CLASS_RELATION_SEMANTICS: axis-qualified and externally ordered LOW < MODERATE < HIGH; NA allowed only at information-type confidentiality axis
MUTUAL_EXCLUSION_RULES: exactly one impact value per objective per frozen subject state
CRITERION_COMPOSITION_RULE:
  information type -> preserve external objective assignments;
  information system initial profile -> objective-wise high-water mark over resident information types with system low-water rule replacing NA where necessary;
  overall system impact -> FIPS 200 high-water-mark class rule
DECISION_RULE: apply only the externally fixed rules above and preserve documented adjustment state separately
FEATURE_BASIS: confidentiality/integrity/availability impact assignments plus resident-information-type membership and documented system adjustment
FEATURE_SOURCE_AND_PROVENANCE: FIPS 199 Example 4 and Example 5; FIPS 200 overall-impact definitions
TARGET_DSD_LAYER_SCOPE: method-level classification; no additional Formation/Property/Aggregation/Dynamics layer required
DOMAIN_BRIDGE: external FIPS impact values and subject/state records -> axis-qualified class assignments and overall system impact class
EXTERNAL_STANDARD: FIPS 199 + FIPS 200
```

Core separations:

```text
SECURITY_CATEGORY_VECTOR != OVERALL_SYSTEM_IMPACT_CLASS
SAME_OVERALL_IMPACT != SAME_SECURITY_CATEGORY_VECTOR
SAME_SECURITY_CATEGORY_VECTOR != SAME_OBJECT_IDENTITY
INFORMATION_TYPE_NA_ALLOWED != SYSTEM_NA_ALLOWED
OBJECTIVE_WISE_HIGH_WATER_MARK != LABEL_BASED_CLASSIFICATION
INITIAL_SYSTEM_CATEGORY != FINAL_ADJUSTED_SYSTEM_CATEGORY
DOCUMENTED_ADJUSTMENT != POST_HOC_REPAIR
SAME_PROFILE != SAME_SOURCE_OBJECT
```

## 4. Frozen external subject set

Seven externally supplied records are frozen.

### Information-type records

```text
I1 — acquisition contract information
  confidentiality: MODERATE
  integrity: MODERATE
  availability: LOW

I2 — acquisition routine administrative information
  confidentiality: LOW
  integrity: LOW
  availability: LOW

I3 — SCADA real-time sensor data
  confidentiality: NA
  integrity: HIGH
  availability: HIGH

I4 — SCADA routine administrative information
  confidentiality: LOW
  integrity: LOW
  availability: LOW
```

I2 and I4 intentionally have the same security-category profile but remain distinct source objects in distinct system contexts.

### Information-system state records

```text
S1 — acquisition system final category from Example 4
  resident records: I1 + I2
  expected system security-category profile:
    confidentiality: MODERATE
    integrity: MODERATE
    availability: LOW
  expected overall impact class: MODERATE-IMPACT SYSTEM

S2 — SCADA system initial high-water-mark category from Example 5
  resident records: I3 + I4
  expected initial system security-category profile:
    confidentiality: LOW
    integrity: HIGH
    availability: HIGH
  expected overall impact class: HIGH-IMPACT SYSTEM

S3 — SCADA system final adjusted category from Example 5
  predecessor state: S2
  externally documented adjustment:
    confidentiality LOW -> MODERATE
    integrity unchanged HIGH
    availability unchanged HIGH
  expected final system security-category profile:
    confidentiality: MODERATE
    integrity: HIGH
    availability: HIGH
  expected overall impact class: HIGH-IMPACT SYSTEM
```

## 5. Frozen operation

For information-type records I1-I4:

```text
1. preserve exact source-object identity and context;
2. preserve the three objective values exactly as externally assigned;
3. permit NA only where externally supplied and semantically allowed;
4. do not infer objective values from the subject name or prose label;
5. return the three-axis security-category profile and provenance.
```

For S1 and S2:

```text
1. preserve resident-information-type membership;
2. compute each objective independently from the external resident records;
3. use the highest externally ordered impact value per objective;
4. at system level, do not retain NA as a system objective value;
5. record the derived three-axis system security-category profile;
6. classify overall system impact by the FIPS 200 rule;
7. keep vector profile and scalar overall class as different outputs.
```

For S3:

```text
1. preserve S2 as the initial predecessor state;
2. apply only the adjustment explicitly documented by FIPS 199;
3. record the changed confidentiality coordinate and unchanged integrity/availability coordinates;
4. classify the final vector under FIPS 200;
5. do not rewrite S2 retroactively;
6. do not call the source-documented adjustment a post-hoc DSD repair.
```

Forbidden during execution:

```text
new security objective
new impact value
label-based inference
collapsing NA to LOW at information-type level
retaining NA at information-system level
single-scalar shortcut that discards the three-axis system profile
retroactive replacement of S2 by S3
object identity inferred from equal profile
new external source introduced after execution begins to repair a result
```

## 6. Frozen expected outputs

```text
I1 -> (MODERATE, MODERATE, LOW)
I2 -> (LOW, LOW, LOW)
I3 -> (NA, HIGH, HIGH)
I4 -> (LOW, LOW, LOW)

S1 acquisition system
  -> (MODERATE, MODERATE, LOW)
  -> MODERATE-IMPACT SYSTEM

S2 SCADA initial
  -> (LOW, HIGH, HIGH)
  -> HIGH-IMPACT SYSTEM

S3 SCADA final adjusted
  -> (MODERATE, HIGH, HIGH)
  -> HIGH-IMPACT SYSTEM
```

Additional expected distinctions:

```text
I2_PROFILE_EQUALS_I4_PROFILE: yes
I2_OBJECT_ID_EQUALS_I4_OBJECT_ID: no
I3_INFORMATION_TYPE_CONFIDENTIALITY_NA: yes
S2_SYSTEM_CONFIDENTIALITY_NA: no
S2_OVERALL_IMPACT_EQUALS_S3_OVERALL_IMPACT: yes
S2_VECTOR_EQUALS_S3_VECTOR: no
S2_RETAINED_AS_PREDECESSOR_STATE: yes
S3_DOCUMENTED_ADJUSTMENT_PROVENANCE: FIPS 199 Example 5
```

All seven source/state records are expected to be `CLASSIFICATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed faithfully.

## 7. Frozen scoring

Total required checks: **60**.

```text
A. source / precommit / immutability: 10
  A1 Classification Protocol commit fixed
  A2 FIPS 199 source fixed
  A3 FIPS 200 source fixed
  A4 Example 4 source records fixed
  A5 Example 5 source records fixed
  A6 seven-record subject/state set fixed
  A7 class/profile rules fixed
  A8 expected outputs fixed
  A9 scoring fixed
  A10 no post-hoc source/task/rule changes

B. information-type profile preservation: 12
  B1-B3 I1 exact C/I/A profile
  B4-B6 I2 exact C/I/A profile
  B7-B9 I3 exact C/I/A profile including NA
  B10 I4 exact LOW/LOW/LOW profile
  B11 I2 and I4 equal-profile / distinct-object separation
  B12 no label-based or name-based impact inference

C. information-system reconstruction and adjustment: 18
  C1-C3 S1 objective-wise high-water-mark reconstruction
  C4 S1 exact vector
  C5 S1 system-level NA prohibition respected
  C6-C8 S2 objective-wise high-water-mark reconstruction
  C9 S2 exact initial vector
  C10 S2 system-level NA prohibition respected
  C11 S2 retained as an explicit initial state
  C12 S3 adjustment provenance retained
  C13 confidentiality LOW -> MODERATE recorded
  C14 integrity HIGH unchanged
  C15 availability HIGH unchanged
  C16 S3 exact final vector
  C17 no retroactive replacement of S2
  C18 documented external adjustment not relabeled as DSD repair

D. overall-impact classification and cross-output distinctions: 12
  D1 S1 -> MODERATE-IMPACT SYSTEM
  D2 S2 -> HIGH-IMPACT SYSTEM
  D3 S3 -> HIGH-IMPACT SYSTEM
  D4 FIPS 200 low/moderate/high rule preserved
  D5 security-category vector kept separate from scalar impact class
  D6 same overall impact does not force equal vector
  D7 S2 and S3 same overall high impact retained
  D8 S2 and S3 unequal vectors retained
  D9 information-type NA allowed only in frozen context
  D10 system-level NA not emitted
  D11 all seven records CONFORMANT
  D12 source/provenance trace retained for every output

E. scope / evidence discipline: 8
  E1 method gain remains NOT_ASSESSED
  E2 external-origin evidence not relabeled independent validation
  E3 no independent replication claim
  E4 no practical-superiority claim
  E5 no maturity promotion from this case alone
  E6 no universal NIST/FISMA categorization claim beyond frozen examples/rules
  E7 no method survival/merger/absorption/deletion conclusion
  E8 no Protocol/shared-core revision unless a real contradiction appears
```

Decision:

```text
60/60 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

If a source-reading, task, or protocol mismatch is found, preserve this Case ID as failed and correct prospectively under a new Case ID. Do not rewrite the frozen interpretation after execution to obtain PASS.

## 8. Evidence-count lock

Before execution:

```text
DIRECT_CLASSIFICATION_PILOTS: 5
NO_GAIN_CLASSIFICATION_CASES: 2
BASELINE_CLASSIFICATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_CLASSIFICATION: established_at_constructed_evidence_level
EXTERNAL_CLASSIFICATION_APPLICATIONS: 1
EXTERNAL_CLASSIFICATION_DOMAINS: 1
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
