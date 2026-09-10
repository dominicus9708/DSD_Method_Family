# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.
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
INDEPENDENT_EVALUATOR_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

### `synthesis/` — DSD Synthesis / DSD 합성론

Planning opened `2026-09-10`; executable `PROTOCOL_v0.1.md` was established at commit `8787b24`.

Current Synthesis state after `SYN-AUD-001`:

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

Key Synthesis evidence:

```text
SYN-CH-001  28/28 PASS  positive
SYN-CH-002  36/36 PASS  INFEASIBLE != UNDERDETERMINED != BLOCKED
SYN-CH-003  46/46 PASS  method-boundary handoffs
SYN-CH-004  33/35 FAIL  CHALLENGE_DESIGN_DEFECT preserved
SYN-CH-005  37/37 PASS  competent B0 / NO_GAIN
SYN-CH-006  52/52 PASS  strongest-reasonable B1 / NO_GAIN
SYN-CH-007  48/48 PASS  deterministic_same_project retrace

SYN-APP-001
  RFC 3986 / URI generic syntax
  40/40 PASS

SYN-APP-002
  BIPM SI Brochure 9th ed. v4.01 (2026)
  physical metrology / SI unit composition
  46/46 PASS

SYN-APP-003
  USB Type-C Release 2.0 frozen mechanical subset
  physical connector assembly / mating interface
  44/44 PASS

SYN-AUD-001
  AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
  PRECOMMIT: ba966b5
  RESULT: bae4388
  28/28 audit-execution PASS
  METHOD_MATURITY_CLASSIFICATION: established
  PROMOTION_TO_ESTABLISHED: SUPPORTED
  M5: CONDITIONAL_PASS
  M9: PASS
  M10: UNRESOLVED_BUT_BOUNDED
  M11: PRESENT_NONFATAL
  M15: PASS
```

The established Synthesis label means method/protocol evidence maturity inside the current DSD method-family framework. It does not establish independent validation, independent replication, practical superiority, universal external generality, or permanent method survival/nonmerger.

Current Synthesis guards include:

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY != AUTOMATIC_COMPOSABILITY
EXHAUSTIVE_COMPONENT_LIST != EXHAUSTIVE_COMPOSITION_SPACE
FORMATION_CLAUSE_VII_COMPOSITION != DOMAIN_SYNTHESIS_LEGITIMACY
AGGREGATE_READOUT != SYNTHESIZED_WHOLE
COMPONENT_PROPERTY != WHOLE_PROPERTY
candidate ID / syntax tree != material synthesized-target distinctness
PARTIAL_SYNTHESIS != completed synthesized target
STATIC_COMPOSITION_ORDER != TEMPORAL_ASSEMBLY_SEQUENCE
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

The next Synthesis task is `SYN-IEP-001` independent-evaluator infrastructure. Packet preparation must remain infrastructure only until a genuinely separate evaluator submission is frozen and scored.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
