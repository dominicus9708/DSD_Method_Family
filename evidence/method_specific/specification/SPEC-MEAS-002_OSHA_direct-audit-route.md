# SPEC-MEAS-002 — ROUTE_O Direct OSHA -> DSD Audit Result

Date: 2026-09-08
Precommit: `7de2ffba9e26bb1870519a95cf171c9614a65063`
Route: official OSHA regulation + official eTool/checklists -> DSD Audit directly
Status: FROZEN_DIRECT_BASELINE_RESULT

## 1. Source precedence used by the direct route

The route uses the authoritative regulation as the normative source and OSHA eTool/checklists as explanatory/review aids.

```text
29 CFR 1910.38 / 1910.165 regulatory text
> official OSHA eTool/checklist explanatory representation
```

A checklist prompt is not allowed to create a regulatory obligation absent support in the governing regulation.

## 2. Six locked probe findings

### P1 — reporting procedure present

1910.38(c)(1) requires procedures for reporting a fire or other emergency. The target probe states that the reporting procedure is present.

```text
FINDING: ADDRESSED
```

### P2 — accountability procedure absent

1910.38(c)(4) requires procedures to account for all employees after evacuation.

```text
FINDING: REQUIRED_OMISSION
```

### P3 — one undifferentiated alarm signal

1910.38(d) requires an employee alarm system with a distinctive signal for each purpose and invokes 1910.165.

```text
FINDING: REQUIREMENT_VIOLATION_OR_DEFICIENCY
```

### P4 — plan-change review trigger absent

1910.38(f)(3) requires review of the emergency action plan when the plan is changed.

```text
FINDING: REQUIRED_OMISSION
```

### P5 — optional auxiliary-power recommendation absent

OSHA's EAP reporting guidance says an employer "might want to consider" auxiliary power. The employee-alarm checklist also asks about auxiliary power while citing 1910.165(b)(2), but the regulatory text of 1910.165(b)(2) concerns perceptibility, while 1910.165(d)(3) requires maintaining/replacing power supplies as necessary for fully operational condition and providing backup means when systems are out of service.

Therefore absence of a separately named auxiliary-power supply is not, by itself, enough to declare a regulatory failure from this locked probe.

```text
FINDING: NO_AUTOMATIC_REGULATORY_FAILURE
SOURCE_PRESENTATION_NOTE: official checklist/guidance requires cross-check against regulatory text
```

### P6 — exact assembly point not supplied

1910.38 requires evacuation and accountability procedures, but the locked source/task leaves concrete worksite implementation values site-specific. OSHA's broader checklist discusses assembly areas, but an exact assembly-point value is not supplied by the general source corpus and must not be fabricated.

```text
FINDING: OPEN_SITE_SPECIFIC_VALUE / NO_FABRICATION
```

## 3. Primary-axis result

```text
AUDIT_FINDING_MATCHES: 6/6
FALSE_POSITIVE_ON_OPTIONAL_GUIDANCE: 0
FALSE_FAILURE_FROM_SITE_SPECIFIC_OPENNESS: 0
NORMATIVE_FORCE_PRESERVATION: pass
SOURCE_OR_NORM_REFERENCE_PRESERVATION: pass
FABRICATED_SITE_SPECIFIC_FACTS: 0
```

## 4. Burden proxy result

```text
INTERMEDIATE_SPECIFICATION_ARTIFACT_REQUIRED: no
REQUIREMENT_ATOM_OR_CHECK_ITEM_COUNT_USED_BY_ROUTE:
  six probe-relevant findings derived directly from official source corpus
SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED: yes
HIDDEN_RETRANSLATION_REQUIRED: no
ADDITIONAL_DSD_LAYER_OR_BRIDGE_REQUIRED: no
```

`SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED: yes` means only that the audit performs its own source-to-criterion extraction at this run because no prior DSD Specification carrier is being reused. It is not a measured time penalty.

## 5. Important baseline strength observation

The direct official route is stronger than a naive checklist-only route because a competent audit can cross-check source-force ambiguities against the regulation itself.

P5 demonstrates this directly: the eTool/checklist presentation of auxiliary power is not treated as an automatic statutory/regulatory violation merely because a checklist contains a yes/no item.

This prevents the comparison from artificially favoring DSD by giving the baseline a source-force error that the authoritative corpus itself allows an auditor to resolve.

## 6. Limits

- no human reviewer timing;
- no independent evaluator;
- no actual employer EAP;
- six fixed probes only;
- direct source extraction is performed by the same project evaluator;
- this route does not test reuse across multiple audits.
