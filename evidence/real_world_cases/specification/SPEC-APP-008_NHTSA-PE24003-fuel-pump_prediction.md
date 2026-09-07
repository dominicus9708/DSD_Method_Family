# SPEC-APP-008 — NHTSA PE24003 Frozen DSD Resolution-Acceptance Prediction

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit commit: `290984342bfb42b909425c9a0e69f6c1798641c2`
Status: FROZEN_BEFORE_LATER_RESOLUTION_ARTIFACT_REVEAL

## 1. Locked downstream task

From the PE24003 opening resume only, declare what a later official resolution would need to make explicit for the original safety-investigation problem to be structurally closed at the published resolution level.

This is **not** a prediction that NHTSA must order a recall.

Allowed disposition families remain open:

```text
D1  safety defect identified -> recall/remedy or equivalent official corrective action
D2  investigation expanded/upgraded -> unresolved items explicitly carried forward
D3  no safety defect / no further action -> official rationale closes the opening concern at the agency's standard
D4  mixed disposition -> some population/cause/remedy resolved while other scope remains open
```

No disposition family is scored as preferable merely because DSD can represent it.

## 2. Frozen requirement atoms

### E1 — safety consequence closure

```text
SOURCE_REFERENCE:
  PE24003 opening resume problem description + reported loss/stall/permanent-disablement allegations

TARGET_ENTITY_OR_CARRIER:
  official resolution of the investigated condition

REQUIREMENT_TYPE:
  safety-consequence closure

ACTIVATION_CONDITION:
  always active

REQUIRED_STRUCTURE_OR_VALUE:
  later resolution must explicitly connect its disposition to the investigated stall/loss-of-motive-power risk, or give an official basis for concluding that this risk does not require further defect action

VIOLATION_CONDITION:
  final disposition addresses only an incidental diagnostic code or administrative closure while leaving the original loss-of-motive-power safety concern unexplained

UNRESOLVED_CONDITION:
  investigation remains open or is upgraded and the safety consequence is intentionally carried forward
```

### E2 — recurrence-sensitive closure

```text
SOURCE_REFERENCE:
  complaints reporting failure, repair, then second fuel-pump failure; opening resume also notes the 2018 inspect/replace TSB

TARGET_ENTITY_OR_CARRIER:
  later remedy or closure rationale

REQUIREMENT_TYPE:
  recurrence-sensitive acceptance

ACTIVATION_CONDITION:
  active if later disposition relies on a corrective action for the same investigated failure family

REQUIRED_STRUCTURE_OR_VALUE:
  the later resolution must not silently treat one successful repair/replacement event as sufficient evidence of closure when the opening record already contains repeat-failure allegations; it must either use a changed/expanded corrective basis, provide evidence/rationale supporting the final remedy, or explicitly retain effectiveness uncertainty

ALLOWED_ALTERNATIVES:
  changed component or design; changed manufacturing/supplier control; broader replacement policy; additional inspection logic; substantiated finding that prior repeat allegations do not undermine the final remedy; other authority-supported corrective basis

VIOLATION_CONDITION:
  merely restating the same prior inspect/replace approach as sufficient without addressing the opening record's recurrence concern
```

### E3 — affected-scope traceability

```text
SOURCE_REFERENCE:
  opening population approximately 22,000; ODI expressly left population expansion open

TARGET_ENTITY_OR_CARRIER:
  official final subject/affected population

REQUIREMENT_TYPE:
  scope traceability

ACTIVATION_CONDITION:
  active whenever a final population boundary is published or corrective action applies to a defined population

REQUIRED_STRUCTURE_OR_VALUE:
  later resolution must identify the population to which its determination/remedy applies and permit comparison with the opening scope; expansion, contraction, model-year change, engine/variant split, or no-change are all allowed if externally supported

VIOLATION_CONDITION:
  a changed population boundary appears without enough official description to determine what the disposition actually covers
```

### E4 — defect/root-cause disposition traceability

```text
SOURCE_REFERENCE:
  ODI opened PE24003 to assess scope, frequency, root cause(s), and consequences

TARGET_ENTITY_OR_CARRIER:
  later defect determination / investigation closure rationale

REQUIREMENT_TYPE:
  unresolved-to-resolved traceability

ACTIVATION_CONDITION:
  always active

REQUIRED_STRUCTURE_OR_VALUE:
  the later official record must state enough about the defect condition, causal/failure basis, or alternative closure rationale to explain why the chosen disposition follows; exact microscopic root cause is not mandatory if the authority can justify corrective action or closure without it

PROHIBITED_STATES:
  fabricated precision; DSD-imposed root cause; treating 'root cause unknown' as automatic failure if the external authority can still legitimately resolve the safety defect

UNRESOLVED_CONDITION:
  issue is upgraded/carried forward and root-cause or defect determination remains explicitly open
```

### E5 — remedy-to-hazard mapping

```text
SOURCE_REFERENCE:
  low-pressure fuel-pump failure -> stall/loss of motive power, often above 25 MPH, often permanent disablement

TARGET_ENTITY_OR_CARRIER:
  later official remedy, if any

REQUIREMENT_TYPE:
  corrective-action bridge

ACTIVATION_CONDITION:
  active only if later resolution includes a recall/remedy or equivalent corrective action

REQUIRED_STRUCTURE_OR_VALUE:
  official materials must make a traceable bridge from the corrective action to the investigated fuel-pump failure condition and resulting loss-of-motive-power hazard

VIOLATION_CONDITION:
  corrective action is published but its relation to the investigated failure/hazard cannot be established from official materials
```

### E6 — implementation freedom

```text
SOURCE_REFERENCE:
  opening resume does not determine a final engineering mechanism or remedy architecture

TARGET_ENTITY_OR_CARRIER:
  DSD prediction itself

REQUIREMENT_TYPE:
  anti-overprediction constraint

ACTIVATION_CONDITION:
  always active

REQUIRED_STRUCTURE_OR_VALUE:
  prediction does not require a particular supplier, pump design, manufacturing defect, software calibration, service procedure, or component architecture

VIOLATION_CONDITION:
  after reveal, the prediction is rewritten to claim prior knowledge of the actual technical fix
```

## 3. Frozen event/recurrence carrier

Dynamics is limited to the following claim-relevant sequence:

```text
R1 vehicle operates
-> R2 low-pressure fuel-pump failure condition manifests
-> R3 stall/loss of motive power
-> R4 vehicle may become permanently disabled

and, for recurrence allegations:

R2 first failure
-> R5 repair/replacement
-> R6 later second failure allegation
```

The DSD record does not infer the physical cause of R2.

## 4. Frozen comparison axes

```text
A1_SAFETY_CONSEQUENCE_CLOSURE           <- E1
A2_RECURRENCE_SENSITIVE_CLOSURE         <- E2, conditional on corrective-action relevance
A3_AFFECTED_SCOPE_TRACEABILITY          <- E3
A4_DEFECT_OR_CAUSAL_DISPOSITION_TRACE   <- E4
A5_REMEDY_TO_HAZARD_MAPPING             <- E5, conditional on remedy/recall disposition
A6_IMPLEMENTATION_FREEDOM_PRESERVED     <- E6
```

Axis result vocabulary:

```text
MATCH
PARTIAL_MATCH
NON_MATCH
UNRESOLVED
NOT_APPLICABLE
```

## 5. Frozen success and unfavorable-result rules

A favorable comparison does not require all axes to be full matches because conditional axes may be inactive and official public records may legitimately leave some engineering details unavailable.

Preserve the following without repair-by-reinterpretation:

```text
PARTIAL_MATCH
NON_MATCH
UNRESOLVED
NOT_APPLICABLE
SPEC_NO_GAIN
BASELINE_PREFERRED_FOR_LOCKED_TASK
```

A later official recall is not by itself evidence that DSD predicted the remedy.
A later no-recall closure is not by itself evidence that DSD failed.
The comparison concerns the **structure of closure**, not whether DSD guessed the agency outcome.

## 6. Guardrail expectations

```text
G1 SOURCE_FIDELITY:
  opening facts retained without importing later facts into the frozen record

G2 PURPOSE_AND_PRIORITY_FIDELITY:
  preliminary safety-investigation purpose retained; DSD derivative acceptance use explicitly separated

G3 DETAIL_PROPORTIONALITY:
  six axes only; no speculative engineering decomposition

G4 VIEWPOINT_SEPARATION:
  DSD requirement atoms are derivative and not attributed to NHTSA authors
```

## 7. Frozen claim limits

```text
PREDICTED_RECALL: no
PREDICTED_ROOT_CAUSE: no
PREDICTED_RECALL_POPULATION: no
PREDICTED_COMPONENT_DESIGN_CHANGE: no
PREDICTED_SUPPLIER: no
PREDICTED_CAMPAIGN_NUMBER: no
PREDICTED_ENGINEERING_EFFECTIVENESS_METRIC: no
```

The next stage may reveal later NHTSA/manufacturer official artifacts and score only A1–A6 under this frozen record.
