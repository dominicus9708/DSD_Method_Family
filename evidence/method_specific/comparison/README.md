# DSD Comparison Direct Evidence / DSD 비교론 직접 증거

Status: **Protocol v0.1 established / method-protocol evidence maturity established after CMP-AUD-001 / validation in progress**

This lane records direct Comparison evidence and Comparison-specific audit meta-records. Maturity audits do not themselves increment direct-pilot, external-application, or reproducibility counts.

## Current development state

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PROTOCOL_CREATION_COMMIT: a1700d960e0b41dfe32bf85b6334448d9104100d
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_COMPARISON_APPLICATIONS: 3
EXTERNAL_COMPARISON_DOMAINS: 3
EXTERNAL_COMPARISON_APPLICATION_PASSES: 3
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Protocol and constructed evidence

```text
PROTOCOL_v0.1 creation: a1700d9
CMP-CH-001: 40/40 PASS
CMP-CH-002: 48/48 PASS
CMP-CH-003: 48/48 PASS
CMP-CH-004: 50/50 PASS / NO_GAIN
CMP-CH-005: 60/60 PASS / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level
```

The constructed corpus directly preserves positive relation classes, `RESOLVED`/`UNDERDETERMINED`/`BLOCKED` terminal distinction, neighboring-method handoffs, aggregate-vs-structure separation, map-family/element coverage separation, direction/inverse requirements, first-branch closure, bridge provenance, and honest `NO_GAIN` results.

## Reproducibility evidence

```text
CMP-CH-006
  RETRACE TARGET: CMP-APP-001
  PRECOMMIT: ffd374f
  RESULT: 35d0a8d
  SCORE: 48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

## External application evidence

```text
CMP-APP-001
  PRECOMMIT: e1a109b
  RESULT: b64cd88
  SOURCE: Unicode Standard Annex #15, Unicode 17.0.0 Revision 57
  DOMAIN: text representation / normalization
  SCORE: 42/42 PASS
  METHOD GAIN: NOT_ASSESSED

CMP-APP-002
  PRECOMMIT: f77ddb2
  RESULT: fbba59a
  SOURCE: RFC 9110 §§8.8.3.2, 13.1.1, 13.1.2
  DOMAIN: HTTP validator comparison semantics
  SCORE: 48/48 PASS
  METHOD GAIN: NOT_ASSESSED

CMP-APP-003
  PRECOMMIT: 446aae3
  RESULT: 6dad36f
  SOURCE: JCGM 200:2012 VIM3 entry 2.47
  DOMAIN: physical metrology / measurement-result compatibility
  SCORE: 52/52 PASS
  METHOD GAIN: NOT_ASSESSED
```

The three external domains are materially distinct at the current evidence level: normalization-dependent equivalence, context-selected strong/weak validator comparison, and quantitative uncertainty/correlation-dependent metrological compatibility.

## CMP-AUD-001 maturity audit

```text
PRECOMMIT:
  69315746b3ed5367aa56e087b96b8ea878a59376
RESULT:
  afe4cc7d8a4efe2f7485768e0d9dc363010e34e2
PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0
AUDIT_EXECUTION_VERDICT: PASS
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

Axis summary:

```text
M1 PASS
M2 PASS
M3 PASS
M4 PASS
M5 CONDITIONAL_PASS
M6 PASS
M7 PASS
M8 PASS
M9 PASS
M10 UNRESOLVED_BUT_BOUNDED
M11 PASS
M12 PASS
M13 PASS
M14 PASS
M15 PASS
```

`CMP-AUD-001` is an Audit meta-record. It adds no Comparison direct pilot and does not change external-application or reproducibility counts.

Maximum supported claim:

```text
ESTABLISHED_METHOD_PROTOCOL_EVIDENCE_MATURITY
!= INDEPENDENT_COMPARISON_VALIDATION
!= INDEPENDENT_REPLICATION
!= PRACTICAL_SUPERIORITY
!= UNIVERSAL_EXTERNAL_GENERALITY
!= PERMANENT_METHOD_REGISTRY_SURVIVAL
```

## Protocol-v0.1 core guards

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
EMBEDDING != STRICT_EQUIVALENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
UNSUPPLIED_NORMALIZATION_OR_CONVERSION != COMPARISON_MAP
DYNAMIC_TRAJECTORY_SIMILARITY != SHARED_LINEAGE_OR_IDENTITY
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
RETRACE_PASS != INDEPENDENT_REPLICATION
HTTP_MATCH != REPRESENTATION_IDENTITY
METROLOGICAL_COMPATIBILITY != STRICT_STRUCTURAL_EQUIVALENCE
UNKNOWN_CORRELATION != ASSUME_UNCORRELATED
```

## Evidence IDs

```text
CMP-CH-###   constructed Comparison challenges and dedicated retrace cases
CMP-APP-###  external or independently generated Comparison applications
CMP-AUD-###  Comparison-specific audit/maturity records
CMP-IEP-###  independent-evaluator infrastructure
```

## Inheritance and registry discipline

```text
BOUNDARY_PASS != PERMANENT_METHOD_INDEPENDENCE
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
EXTERNAL_PASS != METHOD_GAIN_PROOF
RETRACE_PASS != INDEPENDENT_REPLICATION
PROTOCOL_ESTABLISHED != METHOD_VALIDATED
MATURITY_ESTABLISHED != INDEPENDENT_VALIDATION
```

## Immediate next task

Prepare `CMP-IEP-001` independent-evaluator infrastructure. The evaluator-facing packet and hidden/reference material must remain separated, and infrastructure preparation must not be counted as independent validation before a genuinely separate frozen submission exists.
