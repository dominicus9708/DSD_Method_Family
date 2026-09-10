# SYN-IEP-001 — Blinded Independent Evaluator Packet / 독립 평가자 블라인드 패킷

Status: **PREPARED — NOT YET EXECUTED**  
Date prepared: **2026-09-10**  
Method under evaluation: **DSD Synthesis / DSD 합성론**  
Protocol: **DSD Synthesis Protocol v0.1**  
Packet class: `independent_evaluator_packet`  
Evidence effect at preparation: **none**

## 1. Purpose / 목적

This packet is for a genuinely separate evaluator to apply DSD Synthesis Protocol v0.1 without access to the hidden reference key.

Packet preparation is infrastructure only.
Independent evidence begins only after an eligible evaluator completes the packet and freezes an immutable submission **before** reference-key reveal.

```text
PACKET_PREPARED
!= INDEPENDENT_SYNTHESIS_VALIDATION
```

The packet contains two held-out task fixtures derived from already public external authorities:

```text
Task S — BIPM SI unit-composition subset
Task P — USB Type-C physical mating/orientation subset
```

The packet candidate IDs `S1-S6` and `P1-P6` are evaluator-packet records, not the historical IDs from `SYN-APP-002` or `SYN-APP-003`.

---

## 2. Evaluator eligibility / 평가자 적격성

The evaluator must declare all of the following before scoring:

```text
E1  I did not receive the SYN-IEP-001 reference key or escrow nonce.
E2  I did not inspect Synthesis evidence files that reveal materially equivalent answers after accepting this packet.
E3  I used only this packet, the supplied external-source material/links, and the supplied Protocol-v0.1 rules unless a procedural clarification is logged.
E4  I did not receive answer-leading feedback after scoring began.
E5  I will freeze my submission before any reference-key reveal.
E6  I disclose prior DSD exposure and any accidental contamination.
```

If `E1`, `E4`, or `E5` is false, the submission is not eligible as independent evidence.
If `E2` or `E3` is false, the submission must be marked `CONTAMINATED_OR_NONBLIND` unless a later Audit establishes that the exposure was non-answer-bearing.

Eligible evaluator types may include:

- a human external reviewer;
- a separately initialized model/session with no access to the hidden key or project conversation history;
- an external team using a declared internal procedure.

The current project assistant/session is **not** eligible as the independent evaluator for this packet.

---

## 3. Required Synthesis rules supplied to evaluator / 제공 합성 규칙

Use the following Protocol-v0.1 rules for both tasks.

```text
R1  Individual component admission does not establish composability.
R2  Only the supplied external composition/interface rule may establish domain synthesis legitimacy.
R3  Candidate coverage is only the finite packet fixture declared for each task.
R4  SYNTHESIS_SPACE returns the complete admissible family within declared coverage.
R5  A failed prerequisite may make later whole-level checks NOT_REACHED rather than failed.
R6  Component/property/status distinctions must not be silently collapsed.
R7  Aggregate/readout equality does not substitute for a synthesized whole.
R8  Static composition does not establish temporal process feasibility unless explicitly supplied.
R9  TERMINAL_SYNTHESIS_STATUS is separate from SYNTHESIS_PROTOCOL_CONFORMANCE.
R10 SYNTHESIS_METHOD_GAIN_STATUS is NOT_ASSESSED when no baseline comparison is active.
R11 External-source compliance remains separate from the DSD Synthesis verdict.
R12 A subset verdict must not be expanded into full external-standard compliance.
```

Allowed terminal Synthesis statuses:

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

Protocol conformance:

```text
CONFORMANT
NONCONFORMANT
UNDETERMINED
```

Method gain:

```text
GAIN_ESTABLISHED
NO_GAIN
NOT_ASSESSED
```

---

# TASK S — BIPM SI unit composition

## 4. Task S source and scope lock / S 과업 출처·범위

External authority:

```text
Bureau International des Poids et Mesures (BIPM)
The International System of Units (SI Brochure)
9th edition, version 4.01 (2026)
DOI: 10.59161/AUEZ1291
```

Official source entry:

```text
https://www.bipm.org/en/publications/si-brochure
```

Only the following unit-composition rules are active:

```text
S-R1 derived units may be expressed as products of powers of SI base units;
S-R2 coherent derived-unit expressions have overall numerical factor 1;
S-R3 Pa = N m^-2 and N = kg m s^-2;
S-R4 a prefix attached to a unit symbol forms an inseparable unit symbol and a power applies to the whole prefixed unit;
S-R5 milli = 10^-3 and micro = 10^-6;
S-R6 compound prefixes are not permitted;
S-R7 mass multiples/submultiples are formed from gram/g rather than by adding another prefix to kilogram/kg;
S-R8 a valid prefixed SI unit is generally non-coherent because the prefix contributes a numerical factor other than 1.
```

Frozen hard conditions:

```text
H1 COMPONENT_OR_PREFIX_ADMISSION
H2 COMPOSITION_FORM_LEGALITY
H3 SCALE_AND_POWER_PROPAGATION
H4 DECLARED_TARGET_EQUIVALENCE
H5 COHERENCE_STATUS_ACCURACY
```

Staging:

```text
Evaluate H1-H2 first.
If H1 or H2 fails -> H3-H5 NOT_REACHED.
If H1-H2 pass -> evaluate H3.
If H3 fails -> H4-H5 NOT_REACHED.
If H1-H3 pass -> evaluate H4 and H5.
```

Claimed output level:

```text
SYNTHESIS_SPACE
```

Candidate coverage:

```text
exhaustive relative only to S1-S6
```

No baseline comparison is active.
No measurement, calibration, uncertainty, realization, or traceability claim is active.

## 5. Task S candidate records / S 후보

```text
S1
  expression: Pa · m^2
  declared target: N
  declared scale relative to N: 1
  declared coherence: COHERENT

S2
  expression: mJ
  declared target: 10^-3 J
  declared coherence: NONCOHERENT

S3
  expression: µm^2
  declared target: 10^-12 m^2
  declared coherence: NONCOHERENT

S4
  expression: kkPa
  interpretation: compound prefix kilo-kilo-pascal
  declared target: 10^6 Pa
  declared coherence: NONCOHERENT

S5
  expression: kPa
  declared target: Pa at scale 1
  declared coherence: NONCOHERENT

S6
  expression: mg
  declared target: 10^-3 kg
  declared coherence: NONCOHERENT
```

## 6. Task S required output / S 제출 항목

For each `S1-S6`, report:

```text
SYNTHESIS_CANDIDATE_RESULT:
  admissible / rejected / unresolved / blocked

FAILURE_SET:
  subset of {H1,H2,H3,H4,H5}, or NONE

COHERENCE_STATUS_RESULT:
  COHERENT / NONCOHERENT / NOT_REACHED / UNRESOLVED
```

Then report:

```text
ADMISSIBLE_FAMILY_S:
TERMINAL_SYNTHESIS_STATUS_S:
SYNTHESIS_PROTOCOL_CONFORMANCE_S:
SYNTHESIS_METHOD_GAIN_STATUS_S:
```

Scope questions:

```text
S-S1  Does a successful unit-composition verdict establish full physical measurement validity? yes/no + one sentence.
S-S2  Does being a valid prefixed SI unit imply that the unit is coherent? yes/no + one sentence.
```

---

# TASK P — USB Type-C physical mating

## 7. Task P source and scope lock / P 과업 출처·범위

Frozen external authority:

```text
USB Type-C Cable and Connector Specification Release 2.0 (August 2019)
mechanical mating / plug-orientation / attach-role subset only
```

Official USB-IF document library entry:

```text
https://www.usb.org/usb-type-cr-cable-and-connector-specification
```

Only the following rules are active:

```text
P-R1 direct Type-C connector mating is plug-to-receptacle;
P-R2 a Type-C plug admits two insertion orientations in a receptacle;
P-R3 reversible cable-end direction is not by itself a physical mating incompatibility;
P-R4 CC/electrical configuration participates in orientation and functional-role establishment;
P-R5 mechanical connector geometry alone does not establish Source/Sink or host/device roles.
```

Frozen hard conditions:

```text
H1 MATING_ROLE_COMPATIBILITY
H2 INSERTION_ORIENTATION_LEGALITY
H3 PHYSICAL_MATING_TARGET_ACCURACY
H4 FUNCTIONAL_ROLE_NONINFERENCE
H5 CABLE_DIRECTION_REVERSIBILITY
```

Staging:

```text
If H1 fails -> H2-H5 NOT_REACHED.
If H1 passes and H2 fails -> H3-H5 NOT_REACHED.
Otherwise evaluate only the downstream checks applicable to the declared candidate claim.
```

Claimed output level:

```text
SYNTHESIS_SPACE
```

Candidate coverage:

```text
exhaustive relative only to P1-P6
```

No baseline comparison is active.
No USB-IF certification, USB Power Delivery negotiation, data-rate, durability, insertion-force, or full electrical-interoperability claim is active.

## 8. Task P candidate records / P 후보

```text
P1
  direct Type-C plug -> Type-C receptacle
  insertion orientation: A
  no Source/Sink or host/device role inferred from geometry

P2
  direct Type-C plug -> Type-C receptacle
  insertion orientation: B
  no Source/Sink or host/device role inferred from geometry

P3
  direct Type-C plug -> Type-C plug
  insertion orientation: A

P4
  direct Type-C plug -> Type-C receptacle
  insertion orientation: 90-degree quarter-turn relative to the two admitted orientations

P5
  Type-C-to-Type-C cable between receptacles R1 and R2
  cable ends E1/E2 swapped relative to an arbitrary first assignment
  each end uses one of the two admitted plug orientations
  no functional role inferred from cable direction alone

P6
  direct Type-C plug -> Type-C receptacle
  insertion orientation: A
  additional claim: connector geometry alone establishes the Source/Sink relationship
```

## 9. Task P required output / P 제출 항목

For each `P1-P6`, report:

```text
SYNTHESIS_CANDIDATE_RESULT:
  admissible / rejected / unresolved / blocked

FAILURE_SET:
  subset of {H1,H2,H3,H4,H5}, or NONE
```

Then report:

```text
ADMISSIBLE_FAMILY_P:
TERMINAL_SYNTHESIS_STATUS_P:
SYNTHESIS_PROTOCOL_CONFORMANCE_P:
SYNTHESIS_METHOD_GAIN_STATUS_P:
```

Scope questions:

```text
P-S1  Does successful mechanical mating by itself establish Source/Sink roles? yes/no + one sentence.
P-S2  Does reversible Type-C plug orientation permit arbitrary rotational insertion? yes/no + one sentence.
```

---

## 10. Submission integrity / 제출 무결성

Use `SYN-IEP-001_submission-template.md` and freeze the completed submission before the hidden reference key is revealed.

Acceptable freeze methods include:

- immutable Git commit SHA;
- timestamped signed file;
- email to the project owner with the final attachment before key reveal;
- another immutable/time-ordered record documented in the later Audit.

After a valid freeze identifier is recorded, the project may reveal the escrow nonce and canonical reference key, recompute the public SHA-256 commitment, and score the frozen submission.

Do not edit the frozen evaluator submission after reveal.
Corrections after reveal must remain a separate post-reveal note.

---

## 11. Precommitted agreement classes / 사전 합의 판정 범주

Semantic scoring contains **24 checks**:

```text
12 candidate semantic checks
   each candidate check includes candidate result + exact reached failure set;
   Task-S candidate semantics also include the reached coherence-status result

6 task-level family / terminal / conformance / gain checks across the two tasks
  - exact admissible family S
  - exact admissible family P
  - terminal status S
  - terminal status P
  - protocol conformance S and P as one paired check
  - method-gain status S and P as one paired check

4 scope-boundary checks
2 source/task-identity checks
```

Critical subset:

```text
10 critical checks:
  exact admissible family S
  exact admissible family P
  terminal status S
  terminal status P
  method-gain status S
  method-gain status P
  S-S1
  S-S2
  P-S1
  P-S2
```

Agreement classes after reference-key reveal:

```text
INDEPENDENT_AGREEMENT_FULL
  eligibility gates satisfied
  24/24 semantic checks

INDEPENDENT_AGREEMENT_PARTIAL
  eligibility gates satisfied
  at least 21/24 semantic checks
  all 10 critical checks pass

INDEPENDENT_DISAGREEMENT
  eligibility gates satisfied
  fewer than 21/24 semantic checks
  OR any critical check fails

CONTAMINATED_OR_INELIGIBLE
  independence eligibility fails
```

A single eligible submission may establish only **single-evaluator independent agreement at the recorded level**.
It does not establish broad inter-rater agreement, population-level reproducibility, practical superiority, permanent method-registry survival, or universal method validity.

---

## 12. Evidence-count rule / 증거 계수 규칙

Preparation changes no Synthesis evidence count.

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_DIRECT_PILOT_INCREMENT_FROM_PACKET_PREPARATION: 0
METHOD_SURVIVAL_OR_MERGER_DECISION_FROM_PACKET_PREPARATION: none
```

Only an eligible frozen external submission scored after commitment verification can change the independent-evaluator evidence ledger.
