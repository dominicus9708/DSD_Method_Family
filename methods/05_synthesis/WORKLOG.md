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
SYN-CH-007  48/48 PASS  deterministic_same_project retrace
```

`SYN-CH-004` remains historical and was not rewritten. `SYN-CH-006` established strongest-reasonable-baseline comparison only at constructed-evidence level. `SYN-CH-007` establishes same-project deterministic retraceability only.

---

## 2026-09-10 — External application 1: RFC 3986

```text
PRECOMMIT: 29ea45a
RESULT: 6985246
EXTERNAL_DOMAIN: Internet identifier syntax / URI generic syntax
SCORE: 40/40 PASS
```

---

## 2026-09-10 — External application 2: BIPM SI unit composition

```text
PRECOMMIT: 46479ae
RESULT: c504d53
EXTERNAL_DOMAIN: physical metrology / SI unit composition
SCORE: 46/46 PASS
```

Preserved `SAME_DIMENSION != SAME_UNIT_SCALE`, prefixed-unit coherence distinctions, and mass-prefix legality without absorbing measurement/calibration claims.

---

## 2026-09-10 — Step 13: SYN-APP-003 physical connector assembly

Status: **44/44 PASS / third external Synthesis domain**

External authority lock:

```text
USB Type-C Cable and Connector Specification Release 2.0 (August 2019)
Frozen subset:
  Section 2.3.2 plug orientation / cable twist detection
  Section 2.3.3 initial power/data relationship
  Section 3.2 connector mating interfaces
Supporting source:
  USB-IF Type-C overview
EXTERNAL_DOMAIN:
  physical connector assembly / USB Type-C mating interface
```

The test explicitly remains version-specific to the frozen Release-2.0 mechanical subset. Newer USB Type-C releases exist, but no current-release certification or compliance claim is made.

Precommit:

```text
evidence/method_specific/synthesis/SYN-APP-003_precommit.md
commit: 4159872ad761f1fe06a784e1771a9b5ac994bff8
blob: 0cfe2711c49e4a249751200dddaec357f2736ce9
```

Result:

```text
evidence/method_specific/synthesis/SYN-APP-003_USB-Type-C-physical-mating.md
commit: 73faaa03bf3309160fae4e7f690a277c12c40540
```

Execution:

```text
M1  plug->receptacle ORIENTATION_A        admissible
M2  plug->receptacle ORIENTATION_B        admissible
M3  invalid 90-degree insertion           rejected {H2}; H3-H5 NOT_REACHED
M4  plug->plug direct                     rejected {H1}; H2-H5 NOT_REACHED
M5  receptacle->receptacle direct         rejected {H1}; H2-H5 NOT_REACHED
M6  C-to-C cable E1/E2 assignment         admissible; H5 PASS
M7  C-to-C cable ends swapped             admissible; H5 PASS
M8  physical mate -> Source/Sink claim    rejected {H4}
M9  physical mate -> host/device claim    rejected {H4}
M10 cable direction -> power-role claim   rejected {H4}; H5 PASS

ADMISSIBLE_FAMILY: {M1,M2,M6,M7}
TERMINAL: SYNTHESIS_ADMISSIBLE
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
SCORE: 44/44 PASS
```

Key distinctions:

```text
TYPE_C_COMPONENT_ADMITTED != DIRECTLY_MATEABLE_WITH_ANY_TYPE_C_COMPONENT
REVERSIBLE_PLUG_ORIENTATION != ARBITRARY_ROTATIONAL_SYMMETRY
MECHANICAL_MATING != SOURCE_SINK_ROLE_ESTABLISHMENT
MECHANICAL_MATING != HOST_DEVICE_ROLE_ESTABLISHMENT
REVERSIBLE_CABLE_DIRECTION != POWER_ROLE_SYMMETRY
```

Evidence effect:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: remains 6
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
REPRODUCIBILITY_CASES: remains 1
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
```

Protocol pressure:

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_COLLAPSE_OR_SURVIVAL_DECISION_FROM_THIS_CASE: none
```

No USB-IF certification, USB Power Delivery, data-rate capability, signal-integrity, durability, insertion-force, or current Release-2.5 conformance claim was inferred.

### Next technical step

Run the first separately precommitted Synthesis maturity audit. The audit must evaluate evidence architecture and unresolved limitations independently from raw pass counts, and it must not turn a pass/fail record into an automatic method survival/merger/deletion decision.
