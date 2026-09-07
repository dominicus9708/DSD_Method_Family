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
METHOD_FAMILY_LINKAGE_PILOTS: 2
BLOCKED_UNSCORED_EXTERNAL_BLIND_PRECOMMITS: 1
PRACTICAL_COMPARATIVE_BENCHMARKS_COMPLETED: 3
INDEPENDENT_EVALUATOR_PACKETS_PREPARED: 2
INDEPENDENT_EVALUATOR_PACKETS_READY_FOR_CONFIRMATORY_SCORING: 1
```

## Independent evaluator track

### SPEC-IND-001 — historical prepared packet

`SPEC-IND-001` is prepared but not completed.

```text
PACKET_COMMIT: 4a6abfaca4ef8bb9de788d844bd8ba0040fc2e15
ANSWER_HASH_COMMIT: 719c20816598cef0945f684dc14d11c917c1aa80
ANSWER_SHA256: 8655a3adc0e953c7de4e69d6732d3142a82717b7eebae938229ecb2f425d0bfe
INDEPENDENT_EVALUATOR_SUBMISSION: absent
INDEPENDENT_EVALUATOR_VALIDATION: not_established
```

The project evaluator must not self-complete this packet and call it independent evidence.

`DSD-AUDIT-20260908-METHODOLOGY-005` reviewed the packet as a **post-hoc internal readiness review** rather than as confirmatory evidence.

```text
INDEPENDENCE_REQUIREMENT_DISCIPLINE: PASS
ANSWER_COMMITMENT_DISCIPLINE: PASS
PRIMARY_CLASS_EXCLUSIVITY: FAIL
PREDECLARED_CLASS_PRECEDENCE: ABSENT
DECISIVE_INDEPENDENT_SCORING_READINESS: NOT_READY
SPEC_IND_001_HISTORY_PRESERVED: yes
```

The packet's independence gates and hidden-answer hash commitment are sound. The weakness is the exact-one `PRIMARY_CLASS` scoring rule: Protocol v1.0 allows different diagnostic families to be simultaneously relevant, while `SPEC-IND-001` does not prospectively define a global precedence rule that would make the listed primary classes mutually exclusive.

Because the expected primary-class sequence has already been committed, adding such a precedence rule now would be a post-hoc scoring change. `SPEC-IND-001` is therefore preserved unchanged as a historical prepared packet, but its eventual exact-primary-class score should not be treated as decisive maturity evidence.

### SPEC-IND-002 — axis-separated successor packet

`SPEC-IND-002` has now been prospectively prepared as the successor independent-evaluator packet.

```text
PACKET_PRECOMMIT_AUDIT_COMMIT: c78f430a0883e44ed3119a8817aa30f2762ebd17
INITIAL_PACKET_COMMIT: dd343dcf25a678f71bf8ff3f02935aaa1a096054
PRE_REVIEW_VOCABULARY_CLEANUP_COMMIT: 43be7d28e78c4b42d8e6d51f3ee696bdbb0e2db1
ANSWER_HASH_COMMIT: 83ddb2866df3ce742f713c6031ea653edc9170fc
ANSWER_SHA256: 962c65d8ad27ca7e0af6aba201ceeb1a9fdbac80e525651942756a911dc455ff
READINESS_AUDIT_COMMIT: 9afe0b763d23566db4451c483b7743cce38c03c0
INDEPENDENT_EVALUATOR_SUBMISSION: absent
INDEPENDENT_EVALUATOR_VALIDATION: not_established
```

The packet replaces the global forced `PRIMARY_CLASS` with exactly one scored target axis per case. Secondary diagnostics may still coexist, but they cannot change the target-axis score.

```text
SCORING_FORM: axis-separated
TARGET_AXIS_PER_CASE: exactly_one
GLOBAL_PRIMARY_CLASS: absent
SECONDARY_DIAGNOSTIC_SCORE_OVERRIDE: prohibited
EXPECTED_SEQUENCE_HASH_COMMITTED_BEFORE_REVIEW: yes
```

The readiness audit `DSD-AUDIT-20260908-METHODOLOGY-006` passed all 14 precommitted gates after one disclosed pre-review cleanup: the initial packet had included a non-protocol `NONE` sentinel in the hard-failure vocabulary, which was removed before any reviewer submission. The expected hash did not change.

```text
CRITICAL_GATES_PASSED: 14/14
CRITICAL_RELEASE_BLOCKERS_FAILED: 0
READINESS_VERDICT: READY_FOR_INDEPENDENT_SUBMISSION
SPEC_IND_002_STATUS: AWAITING_INDEPENDENT_EVALUATOR
```

The next meaningful independent-evidence event is therefore **not another same-project self-retrace**. It is a genuinely separate reviewer submission frozen before answer comparison.

```text
RECOMMENDED_NEXT_INDEPENDENT_PACKET: SPEC-IND-002
NEXT_BLOCKER_RESOLUTION_EVENT: genuine independent evaluator submission
PROTOCOL_V1_0_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## Method-family linkage breadth

### SPEC-LINK-001 — Specification -> Audit

```text
RECEIVING_METHOD: DSD Audit
AUDIT_FINDING_MATCHES: 6/6
REQUIREMENT_IDENTITY_PRESERVATION: pass
NORMATIVE_FORCE_PRESERVATION: pass
OPENNESS_PRESERVATION: pass
HIDDEN_RETRANSLATION_REQUIRED: no
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
```

This demonstrates one receiving boundary where the upstream Specification carrier becomes actively evaluative because the receiving method is Audit.

### SPEC-LINK-002 — Specification -> Analysis

`SPEC-LINK-002` prospectively locked a constructed sensor-status carrier and then tested whether established DSD Analysis could consume it without becoming Audit.

```text
PRECOMMIT_COMMIT: 3f199bc0305b53ec2d26d7b73848c2493568f701
RESULT_COMMIT: 0b08a9b8db24d4bfeb3d0780194c538e5424b17c
PRECOMMITTED_PROBES_PASSED: 8/8
UPSTREAM_REQUIREMENT_IDS_PRESERVED: 6/6
CARRIER_IDENTITIES_PRESERVED: 6/6
ZERO_UNDEFINED_COLLAPSE: 0
ABSENCE_UNDEFINED_COLLAPSE: 0
FABRICATED_THRESHOLD_VALUE: no
A_TO_C_BRIDGE_INFERRED_FROM_NUMERIC_SIMILARITY: no
AUDIT_OR_COMPLIANCE_VERDICT_EMITTED: no
EXTERNAL_STANDARD_E_REPLACED_BY_DSD: no
LINKAGE_VERDICT: FULL_LINKAGE_PASS
```

The case supports the narrow boundary rule:

```text
TYPED_REQUIREMENT_CARRIER_TRANSFER
!= REQUIREMENT_EVALUATION
```

Specification atoms may serve as stable structural reference carriers for Analysis while normative force remains unjudged. This differs from `SPEC-LINK-001`, where Audit legitimately activates criterion evaluation.

```text
METHOD_FAMILY_LINKAGE_PILOTS: 2
DEMONSTRATED_RECEIVING_METHODS:
  Audit
  Analysis
ALL_METHOD_HANDOFF_INTEROPERABILITY: not_established
```

This increases receiving-method breadth but does not establish practical superiority, independent evaluator validation, or universal interoperability.

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

The independent-evaluator blocker now has a release-ready packet, but it remains unresolved until a genuinely separate reviewer completes `SPEC-IND-002` and freezes the result before answer comparison.

The second receiving-method linkage adds genuinely new cross-method breadth, so repeated same-boundary linkage pilots now have diminishing value. Additional internal work should target a materially new measurement axis or wait for the independent reviewer event rather than accumulating similar handoff successes.

The next maturity re-audit should occur after a genuine independent reviewer submission is frozen and compared, or after materially stronger practical evidence resolves one of the blockers above. Running the audit now would mainly reconfirm the existing `developing` status.

## Stable conclusion

```text
PROTOCOL_V1_0_STANDARDIZATION: retained
METHOD_EVIDENCE_STATUS: developing
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```
