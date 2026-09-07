# DSD Specification — Maturity Evidence Status (2026-09-08)

Method: DSD Specification
Current internal protocol: v1.0
Internal protocol status: standardized
Method evidence status: developing

## Current evidence inventory

```text
DIRECT_CONSTRUCTED_PILOTS: 8
EXTERNAL_APPLICATIONS_COMPLETED: 7
EXTERNAL_DOMAINS_COMPLETED: 7
RESOLUTION_WITHHELD_REAL_WORLD_APPLICATIONS: 3
RESOLUTION_WITHHELD_NON_SOFTWARE_APPLICATIONS: 1
METHOD_FAMILY_LINKAGE_PILOTS: 1
BLOCKED_UNSCORED_EXTERNAL_BLIND_PRECOMMITS: 1
```

## Independent evaluator track

`SPEC-IND-001` is prepared but not completed.

```text
PACKET_COMMIT: 4a6abfaca4ef8bb9de788d844bd8ba0040fc2e15
ANSWER_HASH_COMMIT: 719c20816598cef0945f684dc14d11c917c1aa80
ANSWER_SHA256: 8655a3adc0e953c7de4e69d6732d3142a82717b7eebae938229ecb2f425d0bfe
INDEPENDENT_EVALUATOR_SUBMISSION: absent
INDEPENDENT_EVALUATOR_VALIDATION: not_established
```

The project evaluator must not self-complete this packet and call it independent evidence.

## Practical-benefit track

`SPEC-MEAS-001` is completed.

```text
CASE: pytest-dev/pytest#12112
BASELINE: strong conventional source-derived acceptance checklist
DSD_ROUTE: DSD Specification v1.0
BASELINE_SCORE: 5 MATCH + 1 PARTIAL
DSD_SCORE: 5 MATCH + 1 PARTIAL
BASELINE_UTF8_BYTES: 1921
DSD_UTF8_BYTES: 5697
DSD_TO_BASELINE_BYTE_RATIO: 2.966
COMPARATIVE_VERDICT: TIE_WITH_DSD_OVERHEAD
MEASURED_CASE_LEVEL_REPRESENTATION_RESULT: established
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not demonstrated
GENERAL_MEASURED_PRACTICAL_BENEFIT: not_established
```

The negative result is preserved. On the locked standalone bug-repair acceptance task, DSD did not improve material outcome coverage over the strong baseline and required materially more representation.

## Re-audit readiness

A new maturity re-audit is intentionally not run yet.

Current blockers remain:

```text
INDEPENDENT_EVALUATOR_VALIDATION: not_established
POSITIVE_MEASURED_PRACTICAL_BENEFIT: not demonstrated
```

The next maturity re-audit should occur after a genuine independent reviewer submission is frozen and compared, or after another precommitted practical benchmark provides materially new evidence. Running the audit now would mainly reconfirm the existing `developing` status without resolving the strongest remaining evidence dependency.

## Stable conclusion

```text
PROTOCOL_V1_0_STANDARDIZATION: retained
METHOD_EVIDENCE_STATUS: developing
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```
