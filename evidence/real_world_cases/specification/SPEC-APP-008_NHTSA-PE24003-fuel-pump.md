# SPEC-APP-008 — NHTSA PE24003 Low-Pressure Fuel-Pump Resolution-Withheld Result

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Case origin: public_regulatory_safety_investigation
External domain: automotive safety / defect investigation
Precommit: `290984342bfb42b909425c9a0e69f6c1798641c2`
Frozen prediction: `d11996c19c46c710a24df6259d0d2fb0c0c17a38`
External investigation: NHTSA ODI `PE24003`
Official closing action: recall `25V586`

## 1. Result in one line

The DSD Specification v1.0 acceptance contract was frozen from the NHTSA PE24003 Opening Resume before the Closing Resume and recall report were inspected. After reveal, five of six locked structural axes fully matched the official disposition; the remedy-to-hazard axis was only partially matched at the official closure-document stage because the recall established the defect/hazard bridge while the concrete remedy was still under development and explicitly reserved for later effectiveness evaluation.

```text
A1_SAFETY_CONSEQUENCE_CLOSURE: MATCH
A2_RECURRENCE_SENSITIVE_CLOSURE: MATCH
A3_AFFECTED_SCOPE_TRACEABILITY: MATCH
A4_DEFECT_OR_CAUSAL_DISPOSITION_TRACE: MATCH
A5_REMEDY_TO_HAZARD_MAPPING: PARTIAL_MATCH
A6_IMPLEMENTATION_FREEDOM_PRESERVED: MATCH

FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
UNRESOLVED_AXES: 0/6
NOT_APPLICABLE_AXES: 0/6
POST_REVEAL_PREDICTION_CHANGE: 0
SOURCE_FACT_INVENTION_COUNT: 0
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
HARD_FAILURES: 0
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
RESULT: SPECIFICATION_V1_0_AUTOMOTIVE_SAFETY_RESOLUTION_WITHHELD_MATCH_WITH_REMEDY_DETAIL_PARTIAL
```

## 2. Reveal sequence

Before the frozen prediction commit, only the NHTSA PE24003 Opening Resume was used as the external case source.

After the freeze, the following official artifacts were inspected:

1. NHTSA PE24003 Closing Resume, closed 2025-09-26;
2. NHTSA Part 573 Safety Recall Report `25V586`, submitted 2025-09-09;
3. NHTSA recall acknowledgement material for `25V586`;
4. NHTSA public recall-process material and later annual-report context concerning recalls lacking an available remedy.

No locked axis, failure criterion, or allowed unfavorable result was changed after reveal.

## 3. Official resolution facts

The Closing Resume states that ODI closed PE24003 with manufacturer action recall `25V586`.

The investigation expanded materially beyond the opening record. ODI reported that:

```text
- the investigated vehicles used fuel-delivery pumps supplied by Vitesco Technologies Germany GmbH;
- 2018–2019 Alfa Romeo Stelvio vehicles used the same suspect pump;
- an elevated failure rate was associated with the original pumps;
- the failure mode interrupts fuel flow, causing fuel starvation and unexpected loss of motive power, typically with little to no warning;
- combined investigation data identified 1,900 unique VIN experiencing failures;
- recall 25V586 covered 29,467 MY 2017–2019 Giulia vehicles and 24,382 MY 2018–2019 Stelvio vehicles.
```

The Part 573 report further described suspect fuel-delivery-module internal components as susceptible to heat, with loss of flow rate leading to loss of motive power. It stated that the manufacturer determined a safety defect existed.

At the official closure/reported-recall stage, however, the concrete remedy was still under development. ODI explicitly reserved the right to evaluate the remedy once available.

## 4. Locked-axis comparison

### A1 — safety consequence closure

Frozen requirement: later disposition must explicitly close or carry forward the investigated stall/loss-of-motive-power safety concern.

Actual official resolution directly ties the defect to fuel starvation, unexpected loss of motive power, and crash risk, then closes the PE because recall 25V586 addresses the alleged defect.

```text
A1_RESULT: MATCH
```

### A2 — recurrence-sensitive closure

Frozen requirement: because the opening record already contained repeat-failure allegations after repair, the later resolution could not silently treat a single prior inspect/replace event as sufficient closure. A changed/expanded corrective basis, supporting rationale, or explicit retained effectiveness uncertainty was required.

The Closing Resume itself preserves that many reports described recurrence after initial repair. The final defect basis is not merely a restatement of the 2018 DTC-triggered TSB: the later investigation identifies a suspect pump population, elevated failure rate, a fuel-flow interruption failure mode, and a new safety recall. The actual remedy was not yet finalized, and ODI explicitly retained authority to evaluate it later.

That satisfies the precommitted alternative of **retaining remedy-effectiveness uncertainty rather than fabricating closure**.

```text
A2_RESULT: MATCH
REMEDY_EFFECTIVENESS_AT_PE_CLOSURE: explicitly_not_yet_established
```

### A3 — affected-scope traceability

The opening estimate was about 22,000 MY 2017–2018 Giulia vehicles and explicitly allowed population expansion.

Later official material identifies a much broader recall population:

```text
2017–2019 Giulia: 29,467
2018–2019 Stelvio: 24,382
TOTAL: 53,849
```

The Part 573 report ties the suspect populations to production periods, suspect fuel-delivery modules, and plant production records.

```text
A3_RESULT: MATCH
SCOPE_EXPANSION_PRESERVED: yes
```

### A4 — defect / causal disposition traceability

The frozen record did not require a microscopic root cause; it required enough official causal/failure basis to explain the disposition.

The later official record provides:

```text
suspect fuel-delivery pump
-> elevated failure rate
-> interruption/loss of fuel flow
-> fuel starvation
-> unexpected loss of motive power
```

The Part 573 report adds heat susceptibility of internal fuel-delivery-module components and records the manufacturer's safety-defect determination.

```text
A4_RESULT: MATCH
FABRICATED_PRECISION_REQUIRED: no
```

### A5 — remedy-to-hazard mapping

The recall materials clearly map the recall **condition** to the hazard: fuel-pump failure/loss of fuel flow can produce loss of drive power and crash risk.

However, the official Part 573 report available at PE closure states:

```text
remedy is currently under development
```

and the Closing Resume explicitly reserves later remedy evaluation.

Therefore the recall-to-defect/hazard bridge is established, but a concrete remedy-component-to-failure-mode bridge is not yet present in those locked official resolution artifacts.

```text
A5_RESULT: PARTIAL_MATCH
RECALL_DEFECT_HAZARD_BRIDGE: yes
CONCRETE_REMEDY_ARCHITECTURE_AT_PE_CLOSURE: unresolved
REMEDY_EFFECTIVENESS_AT_PE_CLOSURE: unresolved
```

Later public secondary mirrors of NHTSA recall data report that dealers will replace the fuel delivery module, but no directly retrieved later official NHTSA remedy artifact is used here to upgrade this axis. The official closure-stage result remains partial.

### A6 — implementation freedom

The frozen prediction did not guess supplier, heat susceptibility, fuel-delivery-module design, component part numbers, manufacturing process, or exact remedy architecture.

Actual later materials introduced Vitesco Technologies, heat-related internal-component susceptibility, affected production periods, and component identifiers without conflicting with the frozen acceptance contract.

```text
A6_RESULT: MATCH
IMPLEMENTATION_OVERPREDICTION_COUNT: 0
```

## 5. Important unfavorable / incomplete result

This case is not converted into a 6/6 perfect correspondence.

The official PE closure occurred before a concrete remedy was available, so A5 stays `PARTIAL_MATCH` even though the authority concluded that a safety defect existed and a recall was required.

```text
FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
POST_REVEAL_EXCEPTION_ADDED: no
```

This preserves the distinction:

```text
DEFECT_AND_RECALL_DECISION_RESOLVED
!= REMEDY_IMPLEMENTATION_AND_EFFECTIVENESS_FULLY_RESOLVED
```

## 6. Source openness / downstream determinacy

The opening resume intentionally left scope, frequency, root cause, consequences, and possible scope expansion open.

The DSD record did not classify that preliminary openness as defective underspecification.

After reveal:

```text
SOURCE_OPENNESS_AT_OPENING: intentional_investigative_openness
DOWNSTREAM_DETERMINACY_AT_OPENING_FOR_FINAL_REMEDY: underdetermined
FINAL_DEFECT_DISPOSITION_BY_CLOSURE: determined
FINAL_REMEDY_DETAIL_BY_CLOSURE: still_open
```

This is a real-world non-software instance of the v1.0 distinction:

```text
SOURCE_OPENNESS_STATUS
!= DOWNSTREAM_DETERMINACY_STATUS
```

## 7. DSD Dynamics activation

The Dynamics layer was precommitted only because recurrence and event progression were claim-relevant:

```text
vehicle operation
-> pump failure condition
-> loss of fuel flow
-> stall/loss of motive power
-> possible permanent disablement
```

and:

```text
first failure
-> repair/replacement
-> later second-failure allegation
```

The later official record independently preserved recurrence and supplied a failure progression from pump condition to fuel starvation to unexpected loss of motive power.

```text
DYNAMICS_LAYER_JUSTIFIED_BY_TASK: yes
PHYSICAL_ROOT_CAUSE_INFERRED_BY_DSD: no
IRRELEVANT_OPTIONAL_LAYERS_ACTIVATED: 0
```

## 8. Guardrail evaluation

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G2 PURPOSE_AND_PRIORITY_FIDELITY: INSIDE_GUARDRAILS
G3 DETAIL_PROPORTIONALITY: INSIDE_GUARDRAILS
G4 VIEWPOINT_SEPARATION: INSIDE_GUARDRAILS
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS
```

The derivative DSD acceptance contract did not attribute DSD atoms or layer terminology to NHTSA.

## 9. Baseline / gain interpretation

The strongest baseline remains the NHTSA ODI defect-investigation and recall process.

DSD receives no credit for defect discovery, engineering testing, supplier identification, root-cause work, recall authority, or remedy engineering.

Case-level contribution demonstrated here:

```text
SAFETY_CONSEQUENCE_CARRIER: demonstrated
RECURRENCE_SENSITIVE_ACCEPTANCE: demonstrated
OPEN_SCOPE_TO_FINAL_SCOPE_TRACE: demonstrated
IMPLEMENTATION_FREEDOM_SEPARATION: demonstrated
UNRESOLVED_REMEDY_STATUS_PRESERVATION: demonstrated
MEASURED_ENGINEERING_BENEFIT: not measured
```

For the domain's own recall decision, the authoritative baseline remains preferred. DSD's value is as a portable method-family acceptance/interface record, not as a substitute automotive-safety authority.

## 10. External/evaluator boundary

```text
EXTERNAL_SOURCE_AUTHORSHIP: independent_of_DSD
NON_SOFTWARE_DOMAIN: yes
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
PREDICTING_EVALUATOR_INDEPENDENCE: no
FULL_BLINDNESS: no
MODEL_PRIOR_KNOWLEDGE_EXCLUSION: not_established
INDEPENDENT_REVIEWER_VALIDATION: not_established
```

This is the third completed resolution-artifact-withheld real-world comparison and the first such completed comparison in a non-software safety-regulatory domain.

## 11. Final record

```text
SPECIFICATION_RESULT_ID: SPEC-APP-008
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE: NHTSA PE24003 low-pressure fuel-pump safety investigation
DECLARED_DOWNSTREAM_TASK: freeze structural closure requirements from opening resume before later official resolution reveal
LOCKED_REQUIREMENT_INVENTORY: E1-E6
SELECTED_DSD_LAYERS: PROPERTY_CORE + DYNAMICS_LAYER
FINAL_SPEC_STATUS: usable_with_unresolved_items
HARD_FAILURES: none
GUARDRAIL_VERDICT: INSIDE_GUARDRAILS

FULL_MATCH_AXES: 5/6
PARTIAL_MATCH_AXES: 1/6
NON_MATCH_AXES: 0/6
POST_REVEAL_PREDICTION_CHANGE: 0
RESOLUTION_ARTIFACT_WITHHELD_UNTIL_AFTER_PREDICTION: yes
NON_SOFTWARE_DOMAIN: yes
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_PRACTICAL_BENEFIT: not_established

RESULT:
SPECIFICATION_V1_0_AUTOMOTIVE_SAFETY_RESOLUTION_WITHHELD_MATCH_WITH_REMEDY_DETAIL_PARTIAL
```
