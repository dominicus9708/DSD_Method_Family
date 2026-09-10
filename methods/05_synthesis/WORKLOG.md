# DSD Synthesis Worklog / DSD 합성론 작업 기록

## 2026-09-10 — Planning and protocol establishment

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
-> PROTOCOL_v0.1.md
```

Pre-protocol boundary attacks: `16`; preserved without refinement `11`; preserved with non-breaking refinement `5`; collapse `0`; fundamental interface failure `0`.

Executable Protocol v0.1 creation commit: `8787b24`.

---

## 2026-09-10 — Constructed direct evidence

```text
SYN-CH-001  28/28 PASS  positive
SYN-CH-002  36/36 PASS  INFEASIBLE / UNDERDETERMINED / BLOCKED distinction
SYN-CH-003  46/46 PASS  Design / Transformation / Aggregation / Optimization boundaries
SYN-CH-004  33/35 FAIL  CHALLENGE_DESIGN_DEFECT preserved
SYN-CH-005  37/37 PASS  competent baseline / NO_GAIN
SYN-CH-006  52/52 PASS  strongest-reasonable baseline / NO_GAIN
```

`SYN-CH-004` remains historical and was not rewritten after the fixture defect was found. `SYN-CH-006` established strongest-reasonable-baseline comparison only at constructed-evidence level.

---

## 2026-09-10 — Step 10: SYN-APP-001 first external application

```text
EXTERNAL_STANDARD: RFC 3986 / STD 66
PRECOMMIT: 29ea45a
RESULT: 6985246
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
ADMISSIBLE_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 40/40 PASS
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

External source supplied the composition grammar. Generic syntax was not upgraded to scheme-specific URI validity.

---

## 2026-09-10 — Step 11: SYN-CH-007 deterministic retrace

```text
PRECOMMIT: 9bbcadf
RESULT: 7256456
RETRACE_TARGET: SYN-APP-001
RECONSTRUCTED_FAMILY: {R1,R2,R3,R4,R10,R11,R12}
SCORE: 48/48 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_REPLICATION: not established
```

The immutable Protocol/RFC/precommit/result chain was retraced exactly. This fills a reproducibility category only at same-project deterministic level.

---

## 2026-09-10 — Step 12: SYN-APP-002 physical-metrology external application

Status: **46/46 PASS / second external Synthesis domain**

External authority:

```text
BIPM — The International System of Units (SI Brochure)
9th edition, version 4.01, updated 2026
DOI: 10.59161/AUEZ1291
EXTERNAL_DOMAIN: physical metrology / SI unit composition
```

Precommit:

```text
evidence/method_specific/synthesis/SYN-APP-002_precommit.md
commit: 46479ae87b71f92a117c3dc215eb71537c8dea29
blob: ac819ef86133ece054e54b24fec4f23f3d30c2dd
```

Result:

```text
evidence/method_specific/synthesis/SYN-APP-002_SI-unit-composition.md
commit: c504d53f65fabd7ed98098b2077ba4c4d1ac971d
```

Frozen source rules covered:

```text
derived units as products of powers of base units
coherent derived unit factor = 1
special-name equivalences N, Pa, J, W, C
prefix factors as inseparable parts of unit symbols
power propagation through a prefixed unit symbol
prefixed-unit noncoherence
compound-prefix prohibition
kilogram/gram mass-prefix exception
```

Execution:

```text
U1 kg m s^-2 -> N             admissible / COHERENT
U2 N m -> J                    admissible / COHERENT
U3 J s^-1 -> W                 admissible / COHERENT
U4 N m^-2 -> Pa                admissible / COHERENT
U5 A s -> C                    admissible / COHERENT
U6 kg m s^-1 -> N              rejected {H4}
U7 cm^3 -> 10^-6 m^3           admissible / NONCOHERENT
U8 cm^3 -> 10^-2 m^3           rejected {H4}
U9 kN -> 10^3 N                admissible / NONCOHERENT
U10 kN -> N                    rejected {H4}
U11 mµm compound prefix        rejected {H2}; H3-H5 NOT_REACHED
U12 µkg                        rejected {H2}; H3-H5 NOT_REACHED

ADMISSIBLE_FAMILY: {U1,U2,U3,U4,U5,U7,U9}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 46/46 PASS
```

Preserved distinctions:

```text
SAME_DIMENSION != SAME_UNIT_SCALE
VALID_PREFIXED_SI_UNIT != COHERENT_SI_UNIT
PREFIX_COMPONENT_ADMITTED != PREFIX_COMPOSITION_FORM_LEGAL
SI_UNIT_COMPOSITION != PHYSICAL_QUANTITY_MEASUREMENT_VALIDITY
```

Evidence effect:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: remains 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
REPRODUCIBILITY_CASES: remains 1
```

Protocol pressure:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

No uncertainty, calibration, traceability, experimental-realization, physical-law, or instrument claim was inferred. The application outcome does not decide method survival, merger, absorption, or deletion.

### Next technical step

Add a third materially different external domain with stronger component/interface or physical assembly constraints, then consider the first Synthesis maturity audit.
