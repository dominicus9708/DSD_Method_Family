# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / three external domains PASS / deterministic retrace PASS / validation in progress**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**. Shared-core or neighboring-method evidence may be referenced but does not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
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

Protocol establishment and the 16 pre-protocol attacks do not increase the direct-pilot count. Failed direct challenges remain historical attempts but do not fill successful evidence categories. External applications and retrace records are tracked separately from constructed direct pilots.

## Protocol and planning artifacts

- `methods/05_synthesis/PROTOCOL_v0.1.md` — first executable protocol, creation commit `8787b24`.
- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — 16 pre-protocol attacks.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — non-breaking refinements.
- `methods/05_synthesis/PLANNING.md` — development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronology.

## Direct Protocol-v0.1 evidence

```text
SYN-CH-001  positive                           28/28 PASS
SYN-CH-002  negative/failure distinction       36/36 PASS
SYN-CH-003  executable method-boundary         46/46 PASS
SYN-CH-004  first NO_GAIN attempt              33/35 FAIL
            FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
SYN-CH-005  corrected competent baseline       37/37 PASS / NO_GAIN
SYN-CH-006  strongest-reasonable baseline      52/52 PASS / NO_GAIN
SYN-CH-007  deterministic retrace               48/48 PASS
```

`SYN-CH-006` established `STRONGEST_REASONABLE_BASELINE_COMPARISON = established_at_constructed_evidence_level`; its competent baseline matched all frozen comparison dimensions. `SYN-CH-007` established only `deterministic_same_project` retraceability, not independent replication.

## External application evidence

### SYN-APP-001 — RFC 3986 generic URI composition

```text
EXTERNAL_STANDARD: RFC 3986 / STD 66
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
PRECOMMIT: 29ea45a
RESULT: 6985246
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 40/40 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

### SYN-APP-002 — BIPM SI unit composition

```text
EXTERNAL_STANDARD: BIPM SI Brochure, 9th ed., version 4.01 (2026)
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
PRECOMMIT: 46479ae
RESULT: c504d53
ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
SCORE: 46/46 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

Preserved distinctions include `SAME_DIMENSION != SAME_UNIT_SCALE`, `VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT`, and `SI_UNIT_COMPOSITION != PHYSICAL_MEASUREMENT_VALIDITY`.

### SYN-APP-003 — USB Type-C physical mating interface

```text
FROZEN_EXTERNAL_STANDARD:
  USB Type-C Cable and Connector Specification Release 2.0 (August 2019),
  mechanical mating/orientation subset
SUPPORTING_SOURCE: USB-IF Type-C overview
EXTERNAL_DOMAIN: physical connector assembly / USB Type-C mating interface
PRECOMMIT: 4159872
RESULT: 73faaa0
ADMISSIBLE_FAMILY: {M1,M2,M6,M7}
M3 -> {H2}; downstream NOT_REACHED
M4/M5 -> {H1}; downstream NOT_REACHED
M8/M9/M10 -> {H4}
M10 H5 PASS while H4 fails
SCORE: 44/44 PASS
SYNTHESIS_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
```

This first strongly physical interface case preserves:

```text
TYPE_C_COMPONENT_ADMITTED != DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT
REVERSIBLE_PLUG_ORIENTATION != ARBITRARY_ROTATIONAL_SYMMETRY
MECHANICAL_MATING != SOURCE_SINK_ROLE_ESTABLISHMENT
MECHANICAL_MATING != HOST_DEVICE_ROLE_ESTABLISHMENT
REVERSIBLE_CABLE_DIRECTION != POWER_ROLE_SYMMETRY
```

The frozen case is explicitly Release-2.0-mechanical-subset specific; it does not claim current Release-2.5 compliance, USB-IF certification, USB PD success, data-rate capability, durability, or complete electrical interoperability.

## Reproducibility / retrace evidence

### SYN-CH-007 — deterministic same-project retrace of SYN-APP-001

```text
PRECOMMIT: 9bbcadf
RESULT: 7256456
RETRACE_TARGET: SYN-APP-001
REPRODUCIBILITY_LEVEL: deterministic_same_project
RECONSTRUCTED_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 48/48 PASS
INDEPENDENT_REPLICATION: not established
```

## Protocol-v0.1 core guards

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY != AUTOMATIC_COMPOSABILITY
EXHAUSTIVE_COMPONENT_LIST != EXHAUSTIVE_COMPOSITION_SPACE
FORMATION_CLAUSE_VII_COMPOSITION != DOMAIN_SYNTHESIS_LEGITIMACY
AGGREGATE_READOUT != SYNTHESIZED_WHOLE
COMPONENT_PROPERTY != WHOLE_PROPERTY
candidate ID / syntax tree != material synthesized-target distinctness
PARTIAL_SYNTHESIS != completed synthesized target
STATIC_COMPOSITION_ORDER != TEMPORAL_ASSEMBLY_SEQUENCE
```

## Direct-evidence case convention

```text
SYN-CH-###   constructed Synthesis challenges and dedicated retrace cases
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific audit / maturity records
SYN-IEP-###  independent evaluator packet infrastructure
```

A challenge whose expected result matters must be separately precommitted before evaluation. Historical failed or superseded challenge designs are preserved rather than rewritten. Success or failure of a single case does not by itself determine whether a method must survive, merge, be absorbed, or be deleted; method independence is a separate boundary/maturity question.

## Minimum evidence architecture

A future promotion consideration should accumulate, at minimum: dedicated protocol; positive; negative/failure; boundary; `NO_GAIN`; reproducibility/retrace; external/independent application; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not an automatic maturity certificate.

## Immediate next direct-evidence task

Run the first Synthesis maturity audit against the now-populated evidence architecture. The audit must score protocol stability, boundary integrity, failure taxonomy, NO_GAIN honesty, external breadth, retraceability, and unresolved independence separately. It must not convert pass/fail counts into an automatic method-survival, merger, absorption, deletion, or promotion decision.
