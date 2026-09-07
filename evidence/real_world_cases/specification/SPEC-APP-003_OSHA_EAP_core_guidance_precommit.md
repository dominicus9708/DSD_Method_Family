# SPEC-APP-003 — OSHA Emergency Action Plan External Application Precommit

Date: 2026-09-07
Method directly tested: **DSD Specification / DSD 명세론**
Protocol: **Specification Protocol v0.2.1**
Case origin: `public_regulatory_standard_plus_official_guidance`
External domain: workplace emergency planning / occupational safety

## 1. Locked task

Apply DSD Specification Protocol v0.2.1 to the locked OSHA Emergency Action Plan corpus to test whether the method can preserve:

1. legally required minimum plan elements;
2. employer/employee actor roles;
3. legal requirement vs OSHA eTool helpful guidance;
4. site-specific implementation openness without fabricating local details;
5. downstream task determinacy relative to a declared structural-review task;
6. source purpose, priority, and audience function;
7. detail burden and viewpoint separation.

Declared downstream task:

```text
Determine whether a workplace EAP record structurally addresses the locked federal minimum elements and related alarm/training/review obligations, while keeping OSHA guidance and site-specific implementation details separate from the regulation itself.
```

This run does **not** attempt to:

- determine full legal compliance for any real employer;
- generate exact evacuation routes, alarm devices, staffing, or site-specific procedures;
- replace OSHA, legal counsel, fire code, or other competent safety authorities;
- infer facts about a workplace not present in the locked corpus.

## 2. Locked source set

### Source A — Regulatory baseline

OSHA, 29 CFR 1910.38 — Emergency action plans.
Authoritative host: Occupational Safety and Health Administration.
Locked retrieval date: 2026-09-07.

### Source B — Official OSHA explanatory guidance

OSHA eTool, Evacuation Plans and Procedures — Emergency Action Plan overview and Minimum Requirements.
Locked retrieval date: 2026-09-07.

### Source C — Official OSHA alarm/reporting guidance

OSHA eTool, Evacuation Plans and Procedures — Reporting Emergencies / Employee Alarm Systems.
Locked retrieval date: 2026-09-07.

### Source D — Strong structured comparison baseline

OSHA eTool Employee Alarm Systems Checklist / related OSHA checklist material.
Locked retrieval date: 2026-09-07.

Source-status rule:

```text
REGULATION_REQUIREMENT
!= OFFICIAL_GUIDANCE
!= HELPFUL_OPTIONAL_RECOMMENDATION
!= SITE_SPECIFIC_IMPLEMENTATION_VALUE
```

No guidance item may be promoted into a regulatory obligation unless the locked regulation or incorporated standard supports that force.

## 3. Locked source-purpose / actor frame

Pre-score purpose lock:

```text
SOURCE_PRIMARY_PURPOSE:
  facilitate and organize employer and employee actions during workplace emergencies

SOURCE_PURPOSE_EVIDENCE:
  explicitly stated by OSHA eTool overview

SOURCE_TARGET_ACTORS:
  employer
  employees covered by the plan
  designated/trained evacuation-assistance employees
  employees with critical-operation, rescue, or medical duties when applicable

SOURCE_PRIMARY_ACTION_OR_DECISION:
  prepare, maintain, communicate, train for, review, and execute an emergency action plan at the worksite

SOURCE_COMMUNICATION_OR_USE_FUNCTION:
  operational emergency planning and employee understanding, with regulatory minimum elements plus site-specific implementation
```

Priority lock:

```text
LEGAL_MINIMUM_OBLIGATIONS take precedence over merely helpful additions for regulatory-minimum review.
Emergency messages / alarm purposes retain any source-supported priority or distinct-signal relation.
No total priority ordering among all EAP elements is inferred unless source-supported.
```

## 4. Locked source-unit inventory

```text
U01  1910.38 applies when another OSHA standard requires an EAP.
U02  EAP must be written, kept in workplace, and available for employee review; <=10 employees may communicate orally.
U03  minimum plan element: procedures for reporting fire or other emergency.
U04  minimum plan element: evacuation procedures, including evacuation type and exit-route assignments.
U05  minimum plan element: procedures for employees remaining to operate critical plant operations before evacuation.
U06  minimum plan element: procedures to account for all employees after evacuation.
U07  minimum plan element: rescue and medical duties for employees performing them.
U08  minimum plan element: name or job title of employee contact for plan/duty information.
U09  employer must have and maintain an employee alarm system using distinctive signals for each purpose and meeting 1910.165.
U10  employer must designate and train employees to assist safe and orderly evacuation.
U11  employer must review the plan with each covered employee when the plan is developed or the employee is initially assigned.
U12  employer must review the plan when employee responsibilities change.
U13  employer must review the plan when the plan changes.
U14  OSHA eTool states the EAP purpose is to facilitate and organize employer/employee actions during emergencies.
U15  OSHA eTool says a comprehensive EAP should reflect worksite-specific evaluation, layout, structural features, and emergency systems.
U16  OSHA eTool minimum-requirements page labels certain additions as helpful although not specifically required by OSHA.
U17  OSHA alarm/reporting guidance requires immediate reporting and employee notification/alarm behavior at the relevant incorporated regulatory scope.
U18  OSHA guidance distinguishes required alarm properties from optional/helpful measures such as certain auxiliary or communication provisions where phrased as recommendations.
```

`SOURCE_UNIT_COVERAGE` will be scored against these 18 units only.

## 5. Source openness / downstream determinacy hypotheses

Precommitted interpretation rules:

```text
A requirement category can be SOURCE_DETERMINATE even when its exact site-specific implementation is not fixed.

Site-specific route, alarm implementation, role assignment, and procedure content may be SOURCE_INTENTIONAL_OPENNESS only where OSHA text/guidance supports worksite-specific selection or delegated implementation.

Missing local facts are not filled by DSD.

SOURCE_INTENTIONAL_OPENNESS
+ SUFFICIENT_AT_DECLARED_RESOLUTION
is acceptable for the locked structural-review task when the source fully determines what category must be addressed while leaving local implementation to the employer/worksite.
```

A stronger downstream task such as automatic generation of exact routes or exact alarm devices would be outside the locked task and must not be treated as supplied by this corpus.

## 6. Hard-failure criteria

```text
SOURCE_FACT_INVENTION
SILENT_REQUIRED_SOURCE_OMISSION
NORMATIVE_FORCE_STRENGTHENING
REGULATION_GUIDANCE_COLLAPSE
REQUIRED_ACTOR_OR_SCOPE_COLLAPSE
FABRICATED_SITE_SPECIFIC_DETERMINACY
SPEC_CONTRADICTION
REQUIRED_BRIDGE_OMISSION
SPEC_WRONG_STANDARD
CLAIM_RELEVANT_STATUS_COLLAPSE
```

Any fabricated local route, device, person, threshold, or worksite fact is a hard failure if represented as source-supported.

## 7. Guardrail criteria

Use the v0.2/v0.2.1 guardrails:

```text
G1 SOURCE_FIDELITY
G2 PURPOSE_AND_PRIORITY_FIDELITY
G3 DETAIL_PROPORTIONALITY
G4 VIEWPOINT_SEPARATION
```

Scored separately from hard failure:

```text
INSIDE_GUARDRAILS
GUARDRAIL_PRESSURE
GUARDRAIL_EXCEEDED_RECOVERABLE
PURPOSE_OR_VIEWPOINT_DISTORTED
UNDETERMINED
```

## 8. Openness / determinacy axes

When claim-relevant:

```text
SOURCE_OPENNESS_STATUS:
  SOURCE_DETERMINATE
  SOURCE_INTENTIONAL_OPENNESS
  OPENNESS_INTENT_UNDETERMINED
  NOT_APPLICABLE

DOWNSTREAM_DETERMINACY_STATUS:
  SUFFICIENT_AT_DECLARED_RESOLUTION
  UNDERDETERMINED_FOR_DECLARED_TASK
  NOT_APPLICABLE
```

`SPEC_UNDERSPECIFIED` remains task-relative and must not be weakened by calling every missing item “site discretion.”

## 9. Strongest reasonable baselines

```text
BASELINE_A:
  29 CFR 1910.38 + OSHA explanatory eTool pages

BASELINE_B:
  OSHA eTool/checklist structured review materials
```

Baseline B is deliberately strong. A DSD advantage may not be claimed merely because it converts prose into rows or checkboxes already available in OSHA material.

## 10. Precommitted gain criteria

A DSD gain is counted only if it adds operational value not already supplied by the strongest competent baseline for the locked task.

Candidate gain families:

```text
DISTINCTION_GAIN
TRACEABILITY_GAIN
NORMATIVE_FORCE_SEPARATION_GAIN
OPENNESS_DETERMINACY_SEPARATION_GAIN
DOWNSTREAM_CHECKABILITY_GAIN
```

Cosmetic relabeling, duplicate checklists, atom count, or mere DSD terminology do not count.

Possible final competitive outcomes:

```text
BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
SPEC_NO_GAIN
MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
DSD_OPERATIONAL_GAIN_DEMONSTRATED
```

No outcome is preselected.

## 11. Scoring fields

```text
SOURCE_UNIT_COVERAGE: /18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: /11  # U03-U13
REGULATION_GUIDANCE_FORCE_SEPARATION:
SITE_SPECIFIC_OPENNESS_HANDLING:
DOWNSTREAM_DETERMINACY_FOR_LOCKED_TASK:
INVENTED_SITE_SPECIFIC_FACTS:
SILENTLY_DROPPED_SOURCE_UNITS:
NORMATIVE_FORCE_STRENGTHENINGS:
DSD_VIEWPOINT_OVERATTRIBUTIONS:
HARD_FAILURE_COUNT:
GUARDRAIL_VERDICT:
GAIN_RESULT:
FINAL_SPEC_STATUS:
COMPETITIVE_RESULT:
```

## 12. Anti-post-hoc lock

```text
POST_REVEAL_CRITERION_CHANGE: prohibited
POST_REVEAL_EXCEPTION_ADDED: prohibited
POST_REVEAL_BASELINE_WEAKENING: prohibited
```

If a source-status or current-authority issue is discovered during verification, it must be recorded explicitly and cannot be repaired by silently replacing the baseline with an easier comparator.
