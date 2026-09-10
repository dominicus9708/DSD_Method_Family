# SYN-APP-002 Result / SI Unit Composition External Application

Status: **EXECUTED — 46/46 PASS**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`  
Precommit commit: `46479ae87b71f92a117c3dc215eb71537c8dea29`  
Precommit blob: `ac819ef86133ece054e54b24fec4f23f3d30c2dd`

## 1. Evidence identity

```text
CASE_ID: SYN-APP-002
CASE_CLASS: external_application
CASE_ORIGIN: externally_sourced_rule_with_constructed_candidate_fixture
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Synthesis
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EXTERNAL_DOMAIN: physical metrology / SI unit composition
EXTERNAL_STANDARD: BIPM SI Brochure, 9th edition, version 4.01 (2026)
BASELINE: none
```

This is the second external Synthesis application and the first non-URI external domain.

## 2. External-source confirmation

Frozen authority:

```text
Bureau International des Poids et Mesures (BIPM)
The International System of Units (SI Brochure)
9th edition, version 4.01, updated 2026
DOI: 10.59161/AUEZ1291
```

The official BIPM source confirms the frozen rules used here:

```text
- derived units are products of powers of base units;
- a numerical factor of one defines coherent derived units;
- Table 4 gives N = kg m s^-2, Pa = N/m^2, J = N m,
  W = J/s, and C = A s;
- prefix + unit-symbol forms an inseparable symbol and powers act on the whole;
- cm^3 therefore carries (10^-2)^3 = 10^-6 relative to m^3;
- compound prefixes are not permitted;
- prefixed SI units are non-coherent because the prefix introduces a factor other than one;
- mass multiples/submultiples are formed from gram/g rather than by adding a prefix to kg;
  the brochure explicitly gives mg rather than µkg for 10^-6 kg.
```

No source fact outside the frozen sections was required to rescue or reject a candidate.

## 3. Frozen hard-condition execution

```text
H1 COMPONENT_OR_PREFIX_ADMISSION
H2 COMPOSITION_FORM_LEGALITY
H3 SCALE_AND_POWER_PROPAGATION
H4 DECLARED_TARGET_EQUIVALENCE
H5 COHERENCE_STATUS_ACCURACY
```

Staging was preserved exactly:

```text
H1-H2 first.
H1 or H2 fail -> H3-H5 NOT_REACHED.
H1-H2 pass -> H3.
H3 fail -> H4-H5 NOT_REACHED.
H1-H3 pass -> H4 and H5.
```

## 4. Candidate execution

### U1 — newton

```text
parts: kg · m · s^-2
base exponent vector: kg^1 m^1 s^-2
scale: 1
declared target: N
H1 PASS
H2 PASS
H3 PASS
H4 PASS because N = kg m s^-2
H5 PASS -> COHERENT
RESULT: admissible / NONE
```

### U2 — joule

```text
parts: N · m
expand N: kg m s^-2
result: kg m^2 s^-2
scale: 1
declared target: J
H1 PASS
H2 PASS
H3 PASS
H4 PASS because J = N m
H5 PASS -> COHERENT
RESULT: admissible / NONE
```

### U3 — watt

```text
parts: J · s^-1
expand J: kg m^2 s^-2
result: kg m^2 s^-3
scale: 1
declared target: W
H1 PASS
H2 PASS
H3 PASS
H4 PASS because W = J/s
H5 PASS -> COHERENT
RESULT: admissible / NONE
```

### U4 — pascal

```text
parts: N · m^-2
expand N: kg m s^-2
result: kg m^-1 s^-2
scale: 1
declared target: Pa
H1 PASS
H2 PASS
H3 PASS
H4 PASS because Pa = N/m^2
H5 PASS -> COHERENT
RESULT: admissible / NONE
```

### U5 — coulomb

```text
parts: A · s
result: A s
scale: 1
declared target: C
H1 PASS
H2 PASS
H3 PASS
H4 PASS because C = A s
H5 PASS -> COHERENT
RESULT: admissible / NONE
```

### U6 — wrong exponent vector for newton

```text
parts: kg · m · s^-1
result: kg m s^-1
scale: 1
declared target: N = kg m s^-2
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
H5 PASS for the synthesized unprefixed product's coherence status
RESULT: rejected / {H4}
```

Dimensional/exponent mismatch was not repaired by the declared target name.

### U7 — cubic centimetre scale propagation

```text
parts: cm^3
cm = 10^-2 m
(cm)^3 = (10^-2 m)^3 = 10^-6 m^3
declared scaled target: 10^-6 m^3
H1 PASS
H2 PASS
H3 PASS
H4 PASS
H5 PASS -> NONCOHERENT
RESULT: admissible / NONE
```

The prefix factor was cubed together with the unit symbol.

### U8 — incorrect cubic-centimetre scale claim

```text
parts: cm^3
computed: 10^-6 m^3
declared scaled target: 10^-2 m^3
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
H5 PASS -> NONCOHERENT
RESULT: rejected / {H4}
```

The exponent was not applied only to `m` while leaving the `centi` factor unpowered.

### U9 — kilonewton

```text
parts: k · N as kN
k = 10^3
computed: 10^3 N
declared scaled target: 10^3 N
H1 PASS
H2 PASS
H3 PASS
H4 PASS
H5 PASS -> NONCOHERENT
RESULT: admissible / NONE
```

`kN` is a valid prefixed SI unit expression, but its prefix factor prevents it from being coherent.

### U10 — same dimension, wrong scale

```text
parts: kN
computed: 10^3 N
declared target: N at scale 1
H1 PASS
H2 PASS
H3 PASS
H4 FAIL
H5 PASS -> NONCOHERENT
RESULT: rejected / {H4}
```

Same base-unit exponents did not erase the factor `10^3`.

### U11 — compound prefix

```text
parts: m · µ · m interpreted as mµm
individual prefixes/units admitted
H1 PASS
H2 FAIL because compound prefixes are not permitted
H3-H5 NOT_REACHED
RESULT: rejected / {H2}
```

### U12 — extra prefix directly on kilogram

```text
parts: µ · kg interpreted as µkg
µ and kg individually admitted
H1 PASS
H2 FAIL under the frozen mass-prefix formation rule
H3-H5 NOT_REACHED
RESULT: rejected / {H2}
```

The external source requires the corresponding mass multiple/submultiple to be formed on gram/g; it gives `mg`, not `µkg`, for `10^-6 kg`.

## 5. Synthesis closure

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{U1,U2,U3,U4,U5,U7,U9}

REJECTED:
U6  -> {H4}
U8  -> {H4}
U10 -> {H4}
U11 -> {H2}; H3-H5 NOT_REACHED
U12 -> {H2}; H3-H5 NOT_REACHED
```

The family is exhaustive only relative to the frozen twelve-candidate fixture.

## 6. Structural/status distinctions preserved

```text
SAME_DIMENSION
!= SAME_UNIT_SCALE

VALID_PREFIXED_SI_UNIT
!= COHERENT_SI_UNIT

PREFIX_COMPONENT_ADMITTED
!= PREFIX_COMPOSITION_FORM_LEGAL

VALID_UNIT_FACTORS
!= CORRECT_DECLARED_SPECIAL-NAME_EQUIVALENCE
```

The case therefore exercises a non-software, physical-metrology composition system while keeping unit-expression legality separate from measurement validity.

## 7. Three-ledger result

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No competent baseline was precommitted, so the external PASS is not converted into a method-gain claim.

## 8. External-scope discipline

```text
SI_UNIT_EXPRESSION_ADMISSIBLE
!= PHYSICAL_QUANTITY_MEASUREMENT_VALIDITY

SI_UNIT_COMPOSITION
!= EXPERIMENTAL_REALIZATION_OF_A_UNIT

UNIT_SYMBOL_COMPOSITION
!= CALIBRATION_OR_TRACEABILITY
```

No uncertainty budget, calibration chain, measurement accuracy, realization procedure, physical-law validity, or instrument claim was inferred.

## 9. Precommitted scoring

```text
A. source / precommit integrity          8 / 8 PASS
B. candidate verdict/failure            12 / 12 PASS
C. unit-composition discipline          12 / 12 PASS
D. closure / protocol ledgers            8 / 8 PASS
E. external scope / independence         6 / 6 PASS

PRECOMMITTED_REQUIRED_CHECKS:           46
PASSED:                                  46
FAILED:                                   0
EXTERNAL_APPLICATION_VERDICT:          PASS
```

No candidate, hard condition, source rule, score, or baseline status was changed after execution.

## 10. Evidence increment

```text
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: +1
EXTERNAL_SYNTHESIS_DOMAIN_INCREMENT: +1
EXTERNAL_SYNTHESIS_APPLICATION_PASS_INCREMENT: +1
```

Post-run state:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 2
EXTERNAL_SYNTHESIS_DOMAINS: 2
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 2
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## 11. Protocol pressure and method-independence discipline

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

A PASS here is evidence about this external application only. A failure would likewise have required diagnosis of the failed claim/protocol/source bridge; neither success nor failure alone decides whether Synthesis survives, merges, is absorbed, or is deleted.

## 12. Limits and next step

The current external evidence spans two materially different domains:

```text
SYN-APP-001: Internet identifier syntax / RFC 3986
SYN-APP-002: physical metrology / SI unit composition
```

This does not establish broad cross-domain generality, independent replication, practical superiority, or mature-method status.

Next: add a third materially different external domain, preferably with nontrivial component compatibility/assembly constraints rather than primarily symbolic grammar, before the first Synthesis maturity audit.
