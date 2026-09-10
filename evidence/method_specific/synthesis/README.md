# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **Protocol v0.1 established / two external domains PASS / deterministic retrace PASS / validation in progress**

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
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
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

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

## Pre-protocol boundary result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

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
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 40/40 PASS
```

This application uses an externally supplied generic composition grammar. It preserves `ABSENT != PRESENT_EMPTY` and rejects strings that are parseable only under a different declared component decomposition. Scope remains RFC-3986 generic syntax only.

### SYN-APP-002 — BIPM SI unit composition

```text
EXTERNAL_STANDARD: BIPM SI Brochure, 9th ed., version 4.01 (2026)
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
PRECOMMIT: 46479ae
RESULT: c504d53
ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
U6  -> {H4}
U8  -> {H4}
U10 -> {H4}
U11 -> {H2}; H3-H5 NOT_REACHED
U12 -> {H2}; H3-H5 NOT_REACHED
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 46/46 PASS
```

This materially different external domain activates products of powers, coherent special-name equivalences, prefix-factor propagation, coherence status, compound-prefix prohibition, and the kilogram/gram prefix exception. It preserves:

```text
SAME_DIMENSION != SAME_UNIT_SCALE
VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT
PREFIX_COMPONENT_ADMITTED != PREFIX_COMPOSITION_FORM_LEGAL
SI_UNIT_COMPOSITION != PHYSICAL_MEASUREMENT_VALIDITY
```

No uncertainty, calibration, traceability, realization, or physical-law claim is inferred.

## Reproducibility / retrace evidence

### SYN-CH-007 — deterministic same-project retrace of SYN-APP-001

```text
PRECOMMIT: 9bbcadf
RESULT: 7256456
RETRACE_TARGET: SYN-APP-001
REPRODUCIBILITY_LEVEL: deterministic_same_project
RECONSTRUCTED_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
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

Add a third materially different external domain, preferably one with nontrivial component compatibility or assembly constraints rather than primarily symbolic grammar. Only after broader external pressure should the first Synthesis maturity audit be considered.
