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
PRACTICAL_COMPARATIVE_BENCHMARKS_COMPLETED: 3
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

### SPEC-MEAS-001 — standalone acceptance benchmark

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
```

The negative result is preserved. On the locked standalone bug-repair acceptance task, DSD did not improve material outcome coverage over the strong baseline and required materially more representation.

### SPEC-MEAS-002 — direct external source vs native Specification->Audit handoff

```text
CASE: OSHA Emergency Action Plan
ROUTE_O: official OSHA corpus -> DSD Audit
ROUTE_D: official OSHA corpus -> DSD Specification -> DSD Audit
ROUTE_O_FINDINGS: 6/6
ROUTE_D_FINDINGS: 6/6
ROUTE_O_SOURCE_REEXTRACTION_AT_AUDIT: yes
ROUTE_D_SOURCE_REEXTRACTION_AT_AUDIT: no
ROUTE_D_UPSTREAM_SPECIFICATION_ATOMS: 24
CASE_LEVEL_HANDOFF_STRUCTURE_DIFFERENCE: established
CASE_LEVEL_ACCURACY_DIFFERENCE: none demonstrated
CASE_LEVEL_ERROR_DIFFERENCE: none demonstrated
PRIMARY_COMPARATIVE_VERDICT: INDETERMINATE
INDETERMINACY_CAUSE: PRECOMMITTED_VERDICT_CATEGORY_OVERLAP
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not established
```

`SPEC-MEAS-002` found a real structural carrier difference: the native DSD route avoids requirement-model rebuilding at the Specification->Audit receiving boundary, while the direct route re-extracts criterion semantics from the external source during Audit.

However, the DSD route also carries the upstream cost of the 24-atom Specification artifact. The precommit did not make `TIE_WITH_DSD_TRACEABILITY_ADVANTAGE` and `TIE_WITH_DSD_OVERHEAD` mutually exclusive, and both predicates became true. Anti-post-hoc discipline therefore requires the primary verdict to remain `INDETERMINATE` rather than adding a new precedence rule after the result.

This is a benchmark-design limitation, not a v1.0 protocol failure.

### SPEC-MEAS-003 — repeated-use carrier benchmark

```text
CASE: repeated reuse of six locked OSHA EAP criterion families across four target plans
NUMBER_OF_DOWNSTREAM_USES: 4
TOTAL_PROBES_PER_ROUTE: 24
ROUTE_B_PROBE_MATCHES: 24/24
ROUTE_D_PROBE_MATCHES: 24/24
ROUTE_B_SOURCE_REEXTRACTIONS_AFTER_CARRIER_FREEZE: 0
ROUTE_D_SOURCE_REEXTRACTIONS_AFTER_CARRIER_FREEZE: 0
ROUTE_B_CARRIER_REUSE_COUNT: 4
ROUTE_D_CARRIER_REUSE_COUNT: 4
ROUTE_B_UTF8_BYTES: 2653
ROUTE_D_UTF8_BYTES: 5146
DSD_TO_BASELINE_BYTE_RATIO: 1.940
STRUCTURAL_HANDOFF_AXIS: DSD_ADVANTAGE
REPRESENTATION_BURDEN_AXIS: BASELINE_ADVANTAGE
REUSE_AXIS: tie
OVERALL_SUMMARY: MIXED_RESULT
```

`SPEC-MEAS-003` directly weakens the simple reuse hypothesis. A competent conventional criterion carrier can also be frozen once and reused across repeated audits without re-reading the source. DSD retains a native receiving-method interface advantage, but that advantage does not become a reuse-count advantage on this benchmark.

The DSD carrier was about 1.94x the stored UTF-8 size of the strong conventional carrier while producing the same 24/24 outcome accuracy.

No human time, cognitive load, or productivity measurement was available.

### Current practical-benefit conclusion

```text
MEASURED_CASE_LEVEL_REPRESENTATION_RESULT: established_on_SPEC-MEAS-001_and_003
CASE_LEVEL_HANDOFF_STRUCTURE_DIFFERENCE: established_on_SPEC-MEAS-002_and_003
REPEATED_USE_COUNT_ADVANTAGE: not demonstrated_on_SPEC-MEAS-003
POSITIVE_MEASURED_PRACTICAL_BENEFIT: not demonstrated
GENERAL_MEASURED_PRACTICAL_BENEFIT: not_established
```

The practical evidence now supports a conditional interpretation:

```text
DSD_NATIVE_TYPED_HANDOFF: demonstrated_on_locked_cases
CONVENTIONAL_REUSABILITY: also demonstrated
DSD_AUTOMATIC_REUSE_SUPERIORITY: not supported
```

## Re-audit readiness

A new maturity re-audit is intentionally not run yet.

Current blockers remain:

```text
INDEPENDENT_EVALUATOR_VALIDATION: not_established
POSITIVE_MEASURED_PRACTICAL_BENEFIT: not demonstrated
```

Three practical comparative benchmarks now exist, including one prospectively governed by `PRACTICAL_BENCHMARK_RULE_v0.1`. Additional same-project benchmarks have diminishing value unless they add genuinely new measurements such as human time, independent reviewers, or another receiving-method boundary.

The next maturity re-audit should occur after a genuine independent reviewer submission is frozen and compared, or after materially stronger evidence resolves one of the blockers above. Running the audit now would mainly reconfirm the existing `developing` status.

## Stable conclusion

```text
PROTOCOL_V1_0_STANDARDIZATION: retained
METHOD_EVIDENCE_STATUS: developing
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```
