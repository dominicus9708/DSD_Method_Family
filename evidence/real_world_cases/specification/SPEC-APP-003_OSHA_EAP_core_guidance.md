# SPEC-APP-003 — OSHA Emergency Action Plan External Application

Date: 2026-09-07
Method directly tested: **DSD Specification / DSD 명세론**
Protocol: **Specification Protocol v0.2.1**
Precommit: [`SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md`](SPEC-APP-003_OSHA_EAP_core_guidance_precommit.md)
Precommit commit: `ccda4cfe9e9b25b3a97029c6a19c2e8e07076eb0`
Case origin: `public_regulatory_standard_plus_official_guidance`
External domain: workplace emergency planning / occupational safety

## 1. Result in one line

Protocol v0.2.1 preserved all 18 locked source units, all 11 locked 1910.38 minimum/alarm/training/review obligations, and the distinction between legal requirements, OSHA guidance, and site-specific implementation openness without fabricating local workplace facts.

However, OSHA already supplies the regulation, cross-referenced eTool guidance, and strong checklist-style review material. For the locked structural-review task, DSD did not demonstrate enough additional operational value to displace that baseline.

```text
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
RESULT: SPECIFICATION_EXTERNAL_V0_2_1_NO_GAIN_WITH_GUARDRAIL_PRESSURE
```

## 2. Locked source set

Primary regulatory source:

- OSHA, **29 CFR 1910.38 — Emergency action plans**
- authoritative OSHA page with e-CFR link
- locked retrieval date: 2026-09-07

Official explanatory sources:

- OSHA Evacuation Plans and Procedures eTool — Emergency Action Plan / Minimum Requirements
- OSHA eTool — Reporting Emergencies
- OSHA eTool — Employee Alarm Systems
- OSHA Employee Alarm Systems / related checklist material

The source-status distinction was kept explicit:

```text
REGULATION_REQUIREMENT
!= OFFICIAL_EXPLANATORY_GUIDANCE
!= HELPFUL_OPTIONAL_RECOMMENDATION
!= SITE_SPECIFIC_IMPLEMENTATION_VALUE
```

## 3. Source-purpose and actor lock

The OSHA eTool explicitly states that the purpose of an EAP is to facilitate and organize employer and employee actions during workplace emergencies.

The derivative record therefore retained:

```text
SOURCE_PRIMARY_PURPOSE_PRESERVED: yes
SOURCE_TARGET_ACTORS_PRESERVED: yes
WORKSITE_SPECIFIC_FUNCTION_PRESERVED: yes
DSD_DERIVATIVE_VIEW_DECLARED: yes
DSD_ONTOLOGY_ATTRIBUTED_TO_OSHA: no
FULL_LEGAL_COMPLIANCE_CLAIMED: no
```

The DSD task remained a structural-review map, not a substitute for OSHA compliance determination or a site-specific emergency plan.

## 4. Locked source-unit coverage

All 18 precommitted source units remained represented.

| Unit | Preserved content |
|---|---|
| U01 | EAP applicability when another OSHA standard requires one |
| U02 | written/workplace/employee-review rule with <=10 oral communication exception |
| U03 | fire/other-emergency reporting procedure |
| U04 | evacuation procedure, type, and exit-route assignment |
| U05 | critical plant operations before evacuation |
| U06 | employee accountability after evacuation |
| U07 | rescue/medical duties |
| U08 | contact name/job title for plan/duty information |
| U09 | employee alarm system, distinctive signal per purpose, 1910.165 linkage |
| U10 | designate/train evacuation-assistance employees |
| U11 | review when plan developed / initial assignment |
| U12 | review when employee responsibilities change |
| U13 | review when plan changes |
| U14 | EAP purpose: facilitate/organize employer and employee emergency actions |
| U15 | worksite-specific planning tied to layout/features/systems |
| U16 | eTool helpful additions explicitly separated from OSHA-required minimums |
| U17 | emergency reporting / notification requirements and alarm behavior |
| U18 | required alarm properties separated from recommendation-level auxiliary/communication suggestions |

```text
SOURCE_UNIT_COVERAGE: 18/18
SILENTLY_DROPPED_SOURCE_UNITS: 0
```

## 5. Regulatory-minimum preservation

The precommit scored U03-U13 as the 11 locked minimum/alarm/training/review obligation families.

```text
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
NORMATIVE_FORCE_STRENGTHENINGS: 0
REGULATION_GUIDANCE_COLLAPSE: 0
```

Examples of force preservation:

```text
1910.38(c) "must include at a minimum"
  -> regulatory requirement

OSHA eTool "not specifically required by OSHA, you may find it helpful"
  -> optional/helpful guidance, not promoted to mandatory

"might include" / "you might want to consider"
  -> recommendation/example level, not rewritten as SHALL/MUST
```

This distinction was preserved even when required and optional material appeared on the same OSHA guidance page.

## 6. Site-specific openness and downstream determinacy

The source determines **what categories an EAP must address**, while many concrete values are intentionally worksite-specific.

Seven implementation families were scored as source-supported local openness:

```text
S1 reporting means / internal reporting arrangement
S2 evacuation conditions, type, and route assignments
S3 critical-operation shutdown or remain-before-evacuation procedures
S4 employee-accountability method
S5 rescue/medical duty allocation
S6 named/job-title contact implementation
S7 alarm device/signal implementation within applicable 1910.165 constraints
```

For each of these, the source defines required structure or constraints but does not provide the facts of a particular workplace.

```text
SITE_SPECIFIC_OPENNESS_FAMILIES_IDENTIFIED: 7
SOURCE_INTENTIONAL_OPENNESS_HANDLED_WITHOUT_FABRICATION: 7/7
INVENTED_SITE_SPECIFIC_FACTS: 0
```

Relative to the locked downstream task — structural review of whether a workplace plan addresses the required categories — that openness is not itself a defect in the OSHA source.

```text
SOURCE_OPENNESS_STATUS:
  mixed_by_atom
  source_determinate_on_required_categories
  source_intentional_openness_on_worksite_specific_implementation

DOWNSTREAM_DETERMINACY_STATUS:
  SUFFICIENT_AT_DECLARED_RESOLUTION

SPEC_UNDERSPECIFIED_DUE_SOLELY_TO_MISSING_REAL_WORKSITE_FACTS:
  no
```

A different task such as automatically generating exact routes, alarm devices, personnel assignments, or site-specific shutdown actions would be underdetermined from this source corpus alone. That stronger task was not silently imported into the locked run.

## 7. DSD derivative record

The 18 source units were represented by 24 derivative review atoms.

The extra atom count was not counted as a gain.

Representative atom families:

```text
A01 applicability trigger for 1910.38
A02 written-vs-oral plan condition
A03-A08 six minimum EAP content families
A09 alarm-system existence/maintenance
A10 distinctive-signal-per-purpose requirement
A11 explicit 1910.165 dependency
A12 trained evacuation-assistance role
A13-A15 three review/update triggers
A16 source-purpose preservation
A17 worksite-specific implementation boundary
A18 mandatory-vs-helpful source-force distinction
A19 immediate emergency-reporting function
A20 employee-notification/alarm perceptibility function
A21 optional auxiliary-power recommendation kept optional
A22 optional emergency-communications recommendation kept optional
A23 source-openness record for site-specific values
A24 downstream-determinacy record for the locked structural-review task
```

## 8. Hard-failure audit

```text
SOURCE_FACT_INVENTION: 0
SILENT_REQUIRED_SOURCE_OMISSION: 0
NORMATIVE_FORCE_STRENGTHENING: 0
REGULATION_GUIDANCE_COLLAPSE: 0
REQUIRED_ACTOR_OR_SCOPE_COLLAPSE: 0
FABRICATED_SITE_SPECIFIC_DETERMINACY: 0
SPEC_CONTRADICTION: 0
SPEC_WRONG_STANDARD: 0
CLAIM_RELEVANT_STATUS_COLLAPSE: 0

HARD_FAILURE_COUNT: 0
```

No exact route, alarm device, employee identity, assembly point, shutdown sequence, or worksite-specific hazard was invented.

## 9. Guardrail audit

### G1 — Source fidelity

**Inside.** All 18 units remained traceable and regulatory force was not strengthened.

### G2 — Purpose and priority fidelity

**Inside.** The derivative retained emergency planning / employee action as the source function and retained regulatory-minimum priority over merely helpful additions for the locked compliance-structure review.

### G3 — Detail proportionality

**Pressure.** The DSD derivative expands an already concise regulation plus OSHA checklist/guidance into 24 typed atoms and multiple source-status/openness ledgers.

That structure is useful for audit trail and method testing, but for routine EAP minimum-element review OSHA's own checklist and cross-referenced eTool are already more economical.

### G4 — Viewpoint separation

**Inside.** DSD-added source-openness/determinacy categories were declared as derivative method structure and were not attributed to OSHA's authorship or legal terminology.

```text
SEMANTIC_CONTENT_PRESERVED: yes_on_locked_inventory
SOURCE_PURPOSE_PRESERVED: yes
SOURCE_PRIORITY_SEMANTICS_PRESERVED: yes_for_regulatory_vs_optional_force
TARGET_USER_FUNCTION_PRESERVED: yes
DETAIL_INFLATION: present
REPRESENTATION_BURDEN: moderate
VIEWPOINT_CHANGE_DECLARED: yes
AUTHORIAL_INTENT_INFERRED_WITHOUT_BASIS: no
PURPOSE_DISTORTION: no
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
GUARDRAIL_REPAIR_IF_ANY: retain OSHA regulation/eTool/checklist as primary operational layer; use DSD only when a separate trace/audit ledger is needed
```

## 10. Gain audit against strongest baselines

### Baseline A — 29 CFR 1910.38 + OSHA eTool

This baseline already provides:

- explicit mandatory minimum elements;
- direct regulatory section references;
- worksite-specific implementation guidance;
- examples and actor roles;
- clear distinction between some mandatory and helpful additions.

The DSD derivative makes those distinctions formally typed but does not demonstrate a material improvement for the locked structural-review task.

### Baseline B — OSHA checklist material

The checklist baseline already provides strong downstream checkability for routine review.

Therefore merely converting the same obligations into DSD atoms is not counted as `DOWNSTREAM_CHECKABILITY_GAIN`.

### Gain-family verdicts

```text
DISTINCTION_GAIN: no_material_gain_over_combined_OSHA_baseline
TRACEABILITY_GAIN: no_material_gain_over_cross_referenced_OSHA_material
NORMATIVE_FORCE_SEPARATION_GAIN: limited_formalization_only
OPENNESS_DETERMINACY_SEPARATION_GAIN: conceptually_explicit_but_no_measured_task_gain
DOWNSTREAM_CHECKABILITY_GAIN: no_material_gain_over_OSHA_checklist
```

The openness/determinacy ledger remains useful methodologically, especially for preventing fabricated site details, but this run does not establish that it improves ordinary EAP review outcomes compared with OSHA's competent baseline.

## 11. Final scoring

```text
SOURCE_UNIT_COVERAGE: 18/18
REGULATORY_MINIMUM_ELEMENTS_PRESERVED: 11/11
REGULATION_GUIDANCE_FORCE_SEPARATION: pass
SITE_SPECIFIC_OPENNESS_HANDLING: 7/7_without_fabrication
DOWNSTREAM_DETERMINACY_FOR_LOCKED_TASK: SUFFICIENT_AT_DECLARED_RESOLUTION
INVENTED_SITE_SPECIFIC_FACTS: 0
SILENTLY_DROPPED_SOURCE_UNITS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
DSD_VIEWPOINT_OVERATTRIBUTIONS: 0
HARD_FAILURE_COUNT: 0

GAIN_RESULT: SPEC_NO_GAIN
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK

RESULT:
SPECIFICATION_EXTERNAL_V0_2_1_NO_GAIN_WITH_GUARDRAIL_PRESSURE
```

## 12. Interpretation

This result is intentionally non-favorable to a blanket DSD-advantage claim.

The OSHA corpus is different from both earlier external cases:

```text
SPEC-APP-001 RFC 9112:
  compact technical normative algorithm
  -> NO_GAIN / baseline preferred

SPEC-APP-002 Belmont Part C:
  ethically open-textured prose
  -> mixed traceability/checkability gain with guardrail pressure

SPEC-APP-003 OSHA EAP:
  regulation + official explanatory guidance + checklist
  -> NO_GAIN / baseline preferred, while v0.2.1 openness/determinacy separation remains source-faithful
```

The method therefore preserves both positive and negative comparative outcomes across distinct document types rather than forcing a single direction.

## 13. Limits

- no actual employer EAP was evaluated;
- no site-specific safety adequacy or legal compliance determination was made;
- no independent OSHA professional, safety engineer, attorney, or employer reviewer performed the scoring;
- no measured review-time, error-detection, comprehension, or inter-rater benefit;
- the corpus is U.S. federal OSHA material and does not represent all workplace-safety jurisdictions;
- some OSHA eTool material mixes explanation, examples, and incorporated regulatory citations; the run preserves those source-force distinctions only at the locked review resolution;
- current method status remains `developing`.

## 14. Next step

The external corpus count and domain breadth have increased, but another same-project application would have diminishing evidential value compared with a genuinely independent retrace.

The strongest next step is therefore:

```text
INDEPENDENT_RETRACE_TARGET:
  SPEC-APP-002 or SPEC-APP-003 locked source packet

PREFERRED:
  evaluator blinded to the project's expected verdict and given only the protocol + locked source inventory
```

If independent review is not feasible, the next internal step should be a new maturity re-audit that explicitly discounts same-project dependence rather than treating three external corpora as three independent evaluations.
