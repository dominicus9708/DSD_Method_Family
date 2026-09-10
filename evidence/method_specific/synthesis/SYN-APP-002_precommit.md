# SYN-APP-002 Precommit / SI Unit Composition External Application

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`

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

This case is materially different from URI syntax. The external authority supplies rules for composing derived SI units from products of powers, special-name equivalences, and SI-prefix formation.

## 2. Frozen external authority

Primary authority:

```text
Bureau International des Poids et Mesures (BIPM)
The International System of Units (SI Brochure)
9th edition, version 4.01, updated 2026
DOI: 10.59161/AUEZ1291
Official BIPM publication page:
https://www.bipm.org/en/publications/si-brochure
Official current English PDF:
https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf/fcf090b2-04e6-88cc-1149-c3e029ad8232
```

Frozen source scope:

```text
Section 2.3.4 — Derived units
Table 4 — SI units with special names and symbols
Chapter 3 — Decimal multiples and sub-multiples of SI units
```

Frozen source facts, paraphrased:

```text
S1 Derived units are products of powers of base units.
S2 A derived unit is coherent when the numerical factor in that product is 1.
S3 Table 4 supplies special-name equivalences including:
   N  = kg m s^-2
   Pa = N m^-2 = kg m^-1 s^-2
   J  = N m = kg m^2 s^-2
   W  = J s^-1 = kg m^2 s^-3
   C  = A s
S4 SI prefixes supply powers of 10 and attach inseparably to a unit symbol.
S5 When a prefixed unit symbol is raised to a power, the prefix factor is raised with it.
S6 Units formed with SI prefixes are generally non-coherent because the prefix introduces a numerical factor other than 1.
S7 Compound prefix symbols are not permitted.
S8 Prefix symbols cannot stand alone.
S9 For historical reasons the kilogram is exceptional: decimal multiples/submultiples of mass are formed by attaching prefixes to gram/g, not by attaching another prefix to kg.
```

No non-SI unit conversion table, experimental realization procedure, uncertainty budget, or measurement-traceability claim is activated.

## 3. Frozen Synthesis task

```text
SYNTHESIS_TASK_ID: SYN-APP-TASK-002
TASK_SCOPE:
  compose declared SI unit factors and prefixes under the frozen BIPM rules,
  preserving numerical scale, exponent action, named-unit equivalence,
  prefix legality, and coherence status
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_DSD_LAYER_SCOPE:
  Formation-style component/status bookkeeping only as method interface
DOMAIN_BRIDGE:
  BIPM SI unit-composition and prefix rules
EXTERNAL_STANDARD:
  SI Brochure 9th ed. v4.01
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE:
  static_order_only
COMPOSITION_CANDIDATE_BASIS:
  {U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12}
COMPOSITION_COVERAGE:
  exhaustive relative only to the frozen twelve-candidate fixture
```

The task is not dimensional analysis in general and not a measurement task. It is a parts-to-whole unit-expression Synthesis task with externally supplied composition rules.

## 4. Frozen target resolution

A material output record preserves:

```text
input unit/prefix factors
powers applied to each factor
resulting base-unit exponent vector
resulting numerical scale factor relative to coherent SI expression
declared target unit/symbol when supplied
coherence status
prefix-formation legality
```

Therefore:

```text
SAME_DIMENSION
!= SAME_UNIT_SCALE

VALID_PREFIXED_SI_UNIT
!= COHERENT_SI_UNIT

PREFIX_ATTACHED_TO_UNIT
!= PREFIX_STANDING_ALONE

VALID_UNIT_EXPRESSION
!= CORRECT_DECLARED_SPECIAL-NAME_EQUIVALENCE
```

## 5. Frozen hard conditions

```text
H1 COMPONENT_OR_PREFIX_ADMISSION
   Every supplied base/special-name unit or prefix must be admitted by the frozen SI source.

H2 COMPOSITION_FORM_LEGALITY
   Product-of-powers composition and prefix attachment must obey the frozen SI rules.
   Compound prefixes, standalone prefixes, and an extra prefix attached directly to kg are rejected here.

H3 SCALE_AND_POWER_PROPAGATION
   Prefix numerical factors and exponents must be propagated exactly.
   Example: cm^3 carries (10^-2)^3 = 10^-6 relative to m^3.

H4 DECLARED_TARGET_EQUIVALENCE
   If a named or scaled target is declared, the synthesized expression must recover exactly its base-unit exponent vector and numerical scale.

H5 COHERENCE_STATUS_ACCURACY
   The recorded coherent/noncoherent status must match the frozen SI definition.
```

Staging:

```text
Evaluate H1 and H2 first.
If H1 or H2 fails -> H3-H5 NOT_REACHED.
If H1-H2 pass -> evaluate H3.
If H3 fails -> H4-H5 NOT_REACHED.
If H1-H3 pass -> evaluate H4 and H5.
```

## 6. Frozen candidates and expected results

```text
U1
  parts: kg · m · s^-2
  declared target: N
  expected scale: 1
  expected coherence: COHERENT
  expected: admissible / NONE

U2
  parts: N · m
  declared target: J
  expected scale: 1
  expected coherence: COHERENT
  expected: admissible / NONE

U3
  parts: J · s^-1
  declared target: W
  expected scale: 1
  expected coherence: COHERENT
  expected: admissible / NONE

U4
  parts: N · m^-2
  declared target: Pa
  expected scale: 1
  expected coherence: COHERENT
  expected: admissible / NONE

U5
  parts: A · s
  declared target: C
  expected scale: 1
  expected coherence: COHERENT
  expected: admissible / NONE

U6
  parts: kg · m · s^-1
  declared target: N
  expected: rejected / {H4}
  rationale: base-unit exponent vector does not match N

U7
  parts: cm^3
  declared scaled target: 10^-6 m^3
  expected coherence: NONCOHERENT
  expected: admissible / NONE

U8
  parts: cm^3
  declared scaled target: 10^-2 m^3
  expected: rejected / {H4}
  H3 must compute 10^-6 before H4 compares target

U9
  parts: k · N as inseparable prefixed unit kN
  declared scaled target: 10^3 N
  expected coherence: NONCOHERENT
  expected: admissible / NONE

U10
  parts: k · N as kN
  declared target: N at scale 1
  expected: rejected / {H4}
  rationale: same dimensions but numerical scale differs by 10^3

U11
  parts: m · µ · m interpreted as compound prefix mµm
  expected: rejected / {H2}
  H3-H5: NOT_REACHED

U12
  parts: µ · kg interpreted as µkg
  expected: rejected / {H2}
  H3-H5: NOT_REACHED
  rationale: SI mass-prefix formation attaches the prefix to gram/g rather than adding a prefix directly to kg
```

Expected admissible family:

```text
SYNTHESIS_ADMISSIBLE_FAMILY:
{U1,U2,U3,U4,U5,U7,U9}
```

Expected ledgers:

```text
TERMINAL_SYNTHESIS_STATUS: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE: CONFORMANT
SYNTHESIS_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 7. Frozen scope guards

```text
SI_UNIT_EXPRESSION_ADMISSIBLE
!= PHYSICAL_QUANTITY_MEASUREMENT_VALIDITY

SI_UNIT_COMPOSITION
!= EXPERIMENTAL_REALIZATION_OF_A_UNIT

DIMENSIONAL_MATCH
!= UNIT_SCALE_EQUIVALENCE

VALID_PREFIXED_UNIT
!= COHERENT_UNIT

SINGLE_EXTERNAL_APPLICATION_PASS_OR_FAIL
!= METHOD_SURVIVAL_MERGER_OR_DELETION_DECISION
```

No uncertainty, calibration, traceability chain, instrument performance, or physical-law validity claim is scored.

## 8. Precommitted scoring

Total required checks: **46**.

```text
A. source / precommit integrity: 8
  A1 BIPM authority and DOI fixed
  A2 version 4.01 / 2026 scope fixed
  A3 source sections fixed
  A4 candidate basis U1-U12 fixed
  A5 coverage fixed to twelve-candidate fixture
  A6 H1-H5 and staging fixed
  A7 target resolution fixed
  A8 no baseline; method gain fixed NOT_ASSESSED

B. exact candidate verdict/failure checks: 12
  B1-B12 exact U1-U12 verdict and failure-set behavior

C. unit-composition discipline: 12
  C1 U1 N equivalence exact
  C2 U2 J equivalence exact
  C3 U3 W equivalence exact
  C4 U4 Pa equivalence exact
  C5 U5 C equivalence exact
  C6 U6 dimensional/exponent mismatch retained
  C7 U7 cm^3 scale = 10^-6 m^3
  C8 U8 not mis-scaled as 10^-2 m^3
  C9 U9 kN scale = 10^3 N and NONCOHERENT
  C10 U10 same dimensions not mistaken for scale-1 N
  C11 U11 compound prefix rejected before downstream checks
  C12 U12 direct extra prefix on kg rejected under frozen mass-prefix rule

D. closure / protocol ledgers: 8
  D1 family exactly {U1,U2,U3,U4,U5,U7,U9}
  D2 terminal SYNTHESIS_ADMISSIBLE
  D3 conformance CONFORMANT
  D4 gain NOT_ASSESSED
  D5 exhaustive claim limited to frozen fixture
  D6 no measurement-method claim absorbed
  D7 no Optimization/Transformation/Aggregation claim absorbed
  D8 no temporal assembly/process claim

E. external-scope / independence discipline: 6
  E1 dimensional match not upgraded to scale equivalence
  E2 valid prefixed unit not upgraded to coherent unit
  E3 no experimental realization claim
  E4 no calibration/uncertainty/traceability claim
  E5 one external case does not decide method survival/merger/deletion
  E6 domain counted as materially different from URI syntax only if source/task remains physical-metrology unit composition
```

Decision:

```text
46/46 -> EXTERNAL_APPLICATION_VERDICT: PASS
otherwise -> EXTERNAL_APPLICATION_VERDICT: FAIL
```

## 9. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 1
EXTERNAL_SYNTHESIS_DOMAINS: 1
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

A 46/46 PASS may add exactly:

```text
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: +1
EXTERNAL_SYNTHESIS_DOMAIN_INCREMENT: +1
EXTERNAL_SYNTHESIS_APPLICATION_PASS_INCREMENT: +1
```

It does not increase constructed direct-pilot or reproducibility counts and does not establish independent validation, practical superiority, or maturity.
