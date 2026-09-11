# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.
- `NO_GAIN` or baseline matching does not by itself prove redundancy or absorption.
- Same-project retrace does not establish independent replication.
- Established method/protocol evidence maturity does not permanently freeze the method registry.

## Method-specific evidence lanes / 개별 증거 경로

### `design/` — DSD Design / DSD 설계론

```text
PROTOCOL: v0.1 established
METHOD_MATURITY_CLASSIFICATION: established after DES-AUD-002
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

### `synthesis/` — DSD Synthesis / DSD 합성론

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

### `comparison/` — DSD Comparison / DSD 비교론

Executable `PROTOCOL_v0.1.md` was established at commit `a1700d960e0b41dfe32bf85b6334448d9104100d` after 16 pre-protocol boundary attacks.

Current Comparison state after `CMP-APP-002`:

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
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
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

Comparison evidence:

```text
CMP-CH-001  40/40 PASS
CMP-CH-002  48/48 PASS
CMP-CH-003  48/48 PASS
CMP-CH-004  50/50 PASS / NO_GAIN
CMP-CH-005  60/60 PASS / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level

CMP-APP-001
  PRECOMMIT: e1a109b
  RESULT: b64cd88
  SOURCE: Unicode Standard Annex #15, Unicode 17.0.0 Revision 57
  SCORE: 42/42 PASS
  U1 canonical Ç vs C+cedilla -> ENCODED
  U2 same pair binary criterion -> NONCORRESPONDENCE
  U3 ① vs 1 canonical criterion -> NONCORRESPONDENCE
  U4 same pair compatibility criterion -> ENCODED
  U5 Hangul syllable vs jamo -> ENCODED
  U6 combining-mark reorder -> ENCODED
  ALL TERMINAL: COMPARISON_RESOLVED
  ALL CONFORMANCE: CONFORMANT
  METHOD GAIN: NOT_ASSESSED

CMP-CH-006
  RETRACE TARGET: CMP-APP-001
  PRECOMMIT: ffd374f
  RESULT: 35d0a8d
  SCORE: 48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  all six candidate criteria/relation classes/terminals/conformance reproduced
  INDEPENDENT_REPLICATION: not established

CMP-APP-002
  PRECOMMIT: f77ddb2
  PRECOMMIT BLOB: 7478867
  RESULT: fbba59a
  SOURCE: RFC 9110 — HTTP Semantics §§8.8.3.2, 13.1.1, 13.1.2
  SCORE: 48/48 PASS
  H1 W/"1" vs W/"1" strong -> NONCORRESPONDENCE
  H2 same pair weak -> DIRECT_CORRESPONDENCE
  H3 W/"1" vs "1" strong -> NONCORRESPONDENCE
  H4 same pair weak -> DIRECT_CORRESPONDENCE
  H5 "1" vs "1" strong -> DIRECT_CORRESPONDENCE
  H6 W/"1" vs W/"2" weak -> NONCORRESPONDENCE
  H7 If-Match -> strong -> NONCORRESPONDENCE
  H8 If-None-Match -> weak -> DIRECT_CORRESPONDENCE
  ALL TERMINAL: COMPARISON_RESOLVED
  ALL CONFORMANCE: CONFORMANT
  METHOD GAIN: NOT_ASSESSED
```

Current Comparison guards include:

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
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
RETRACE_PASS != INDEPENDENT_REPLICATION
HTTP_MATCH != REPRESENTATION_IDENTITY
RFC_COMPARISON_MATCH != WHOLE_REQUEST_PRECONDITION_RESULT
```

The next Comparison event is a third materially different external application before maturity audit.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
