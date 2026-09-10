# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.

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

Current Synthesis state:

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
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
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
  external domain 1

SYN-APP-002
  BIPM SI Brochure 9th ed. v4.01 (2026)
  physical metrology / SI unit composition
  46/46 PASS
  external domain 2

SYN-APP-003
  USB Type-C Cable and Connector Specification Release 2.0 mechanical subset
  physical connector assembly / USB Type-C mating interface
  PRECOMMIT 4159872
  RESULT 73faaa0
  44/44 PASS
  admissible family {M1,M2,M6,M7}
  M3 -> H2
  M4/M5 -> H1
  M8/M9/M10 -> H4
  external domain 3
```

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
SAME_DIMENSION != SAME_UNIT_SCALE
VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT
SI_UNIT_COMPOSITION != PHYSICAL_MEASUREMENT_VALIDITY
TYPE_C_COMPONENT_ADMITTED != DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT
REVERSIBLE_PLUG_ORIENTATION != ARBITRARY_ROTATIONAL_SYMMETRY
MECHANICAL_MATING != SOURCE_SINK_ROLE_ESTABLISHMENT
REVERSIBLE_CABLE_DIRECTION != POWER_ROLE_SYMMETRY
```

The next Synthesis task is the first maturity audit. It must assess protocol stability, boundary integrity, failure taxonomy, `NO_GAIN` honesty, three-domain external breadth, and retraceability while preserving unresolved independent validation and replication as explicit limits.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, and external-application count does not establish practical superiority or method survival.
