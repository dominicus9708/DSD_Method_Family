# SPEC-APP-004 — WCAG 2.2 Contrast (Minimum) v1.0 External Labeled-Example Regression

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0
Precommit commit: `d0c4538d923e3e8ff895ea02d5ceb5d5477dc3a0`

## Result in one line

DSD Specification v1.0 represented the four locked WCAG 2.2 SC 1.4.3 requirement branches and reproduced the eight selected official W3C ACT outcome families 8/8 without normative strengthening or applicability collapse. The new v1.0 conditional-field discipline also worked as intended: only claim-relevant dependency/applicability structure was activated. Because W3C already supplies the normative criterion and labeled ACT examples, the standalone comparative result is `SPEC_NO_GAIN` with mild detail-proportionality pressure.

```text
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
NORMAL_LARGE_THRESHOLD_SEPARATION: pass
INCIDENTAL_INACTIVE_BOUNDARY_PRESERVATION: pass
NORMATIVE_FORCE_STRENGTHENINGS: 0
SOURCE_FACT_INVENTIONS: 0
INACTIVE_CONDITIONAL_LEDGER_BOILERPLATE: 0
EXTERNAL_STANDARD_BOUNDARY_PRESERVED: yes
FULL_WCAG_CONFORMANCE_OVERCLAIM: 0
FINAL_SPEC_STATUS: no_gain
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
RESULT: SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
```

## 1. Source lock

Primary normative source:
- W3C Recommendation, WCAG 2.2, Success Criterion 1.4.3 Contrast (Minimum).
- Normal text/images of text: at least 4.5:1.
- Large-scale text/images of large-scale text: at least 3:1.
- Incidental text including inactive UI, pure decoration, text not visible to anyone, and text in a picture with significant other visual content: no SC 1.4.3 contrast requirement.
- Logotype/brand-name text: no SC 1.4.3 contrast requirement.

Auxiliary official labeled corpus:
- W3C/WAI ACT Rule `Text has minimum contrast`.

The ACT rule is a test-rule corpus, not a replacement for the WCAG normative Recommendation.

## 2. Locked DSD interface profile

```text
FORMATION_LAYER: not used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

No inactive DSD layer was introduced.

## 3. Requirement atoms

### W1 — normal text minimum

```text
REQUIREMENT_ID: W1
SOURCE_REFERENCE: WCAG 2.2 SC 1.4.3
TARGET_ENTITY_OR_CARRIER: visible text or image of text outside exceptions
REQUIREMENT_TYPE: value_or_range
REQUIRED_OR_OPTIONAL: required_when_active
ACTIVATION_CONDITION: visible qualifying non-large text/image of text; no exception applies
REQUIRED_STRUCTURE_OR_VALUE: contrast ratio >= 4.5:1
VIOLATION_CONDITION: qualifying text contrast < 4.5:1
UNRESOLVED_CONDITION: applicability or rendered contrast cannot be determined at locked resolution
VALIDATION_STANDARD: inherited from locked W3C standard
```

### W2 — large-text minimum

```text
REQUIREMENT_ID: W2
SOURCE_REFERENCE: WCAG 2.2 SC 1.4.3 + large-scale definition
TARGET_ENTITY_OR_CARRIER: large-scale text or image of large-scale text
REQUIREMENT_TYPE: value_or_range
REQUIRED_OR_OPTIONAL: required_when_active
ACTIVATION_CONDITION: large-scale text; no exception applies
DEPENDENCIES: large-scale classification (>=18pt or >=14pt bold, or defined equivalent)
REQUIRED_STRUCTURE_OR_VALUE: contrast ratio >= 3:1
VIOLATION_CONDITION: qualifying large-scale text contrast < 3:1
UNRESOLVED_CONDITION: size/weight or contrast cannot be determined at locked resolution
VALIDATION_STANDARD: inherited from locked W3C standard
```

### W3 — incidental/inactive exception

```text
REQUIREMENT_ID: W3
SOURCE_REFERENCE: WCAG 2.2 SC 1.4.3 Incidental
TARGET_ENTITY_OR_CARRIER: incidental text/image of text
REQUIREMENT_TYPE: applicability
REQUIRED_OR_OPTIONAL: exception_when_active
ACTIVATION_CONDITION: inactive UI, pure decoration, not visible to anyone, or part of a picture with significant other visual content
DEPENDENCIES: exception classification supported by source/target facts
REQUIRED_STRUCTURE_OR_VALUE: no SC 1.4.3 contrast requirement
VIOLATION_CONDITION: exception case is incorrectly forced through normal/large threshold solely as SC 1.4.3
UNRESOLVED_CONDITION: exception status cannot be established
VALIDATION_STANDARD: inherited from locked W3C standard
```

### W4 — logotype exception

```text
REQUIREMENT_ID: W4
SOURCE_REFERENCE: WCAG 2.2 SC 1.4.3 Logotypes
TARGET_ENTITY_OR_CARRIER: logo or brand-name text
REQUIREMENT_TYPE: applicability
REQUIRED_OR_OPTIONAL: exception_when_active
ACTIVATION_CONDITION: text is part of a logo or brand name
REQUIRED_STRUCTURE_OR_VALUE: no SC 1.4.3 contrast requirement
VIOLATION_CONDITION: logotype is assigned a SC 1.4.3 contrast failure solely from the general threshold
UNRESOLVED_CONDITION: logotype status cannot be established
VALIDATION_STANDARD: inherited from locked W3C standard
```

W4 is preserved because it belongs to the locked normative inventory even though none of the eight selected ACT examples was used as a logotype probe.

## 4. Eight official example classifications

| Example | Source facts at locked resolution | Active branch | DSD classification | Official family | Match |
|---|---|---|---|---|---|
| E1 ACT Passed 1 | normal text, #333 on #FFF, reported 12.6:1 | W1 | threshold satisfied | passed | yes |
| E2 ACT Passed 5 | 18pt black on #666, reported 3.6:1 | W2 | large-text threshold satisfied | passed | yes |
| E3 ACT Passed 6 | 14pt bold black on #666, reported 3.6:1 | W2 | large-text threshold satisfied | passed | yes |
| E4 ACT Failed 1 | normal text, #AAA on white, reported 2.3:1 | W1 | threshold violated | failed | yes |
| E5 ACT Failed 8 | informative font sample, #777 on #EEE, reported 3.85:1; not purely decorative | W1 | threshold violated | failed | yes |
| E6 ACT Failed 9 | active button text, #777 on #EEE, reported 3.85:1 | W1 | threshold violated | failed | yes |
| E7 ACT Inapplicable 1 | `display:none`, not visible | W3 | no SC 1.4.3 contrast requirement at this branch | inapplicable | yes |
| E8 ACT Inapplicable 6 | label associated with disabled widget | W3 / ACT applicability boundary | no ordinary active-text threshold failure | inapplicable | yes |

```text
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
FALSE_NORMAL_THRESHOLD_ON_LARGE_TEXT: 0
FALSE_FAILURE_ON_NOT_VISIBLE_TEXT: 0
FALSE_ACTIVE_TEXT_TREATMENT_OF_DISABLED_LABEL: 0
MISSED_NORMAL_TEXT_FAILURES: 0
```

## 5. Independent arithmetic spot check

As a non-authoritative implementation cross-check, standard sRGB relative-luminance calculations were repeated for representative color pairs. The rounded results agreed with the W3C-reported example ratios:

```text
#333 / #FFF  -> 12.6347:1  ~ reported 12.6:1
#000 / #666  ->  3.6574:1  ~ reported 3.6:1
#AAA / #FFF  ->  2.3231:1  ~ reported 2.3:1
#777 / #EEE  ->  3.8597:1  ~ reported 3.85:1
```

This arithmetic check does not replace W3C's normative definitions or the ACT outcome labels.

## 6. v1.0 conditional-field regression

The new standard protocol was intentionally tested for non-boilerplate behavior.

```text
PRECEDENCE_OR_PRIORITY: omitted
SOURCE_OPENNESS_STATUS: omitted
DOWNSTREAM_DETERMINACY_STATUS: omitted
ALLOWED_ALTERNATIVES: omitted; activation conditions were sufficient
PROHIBITED_STATES: omitted; violation conditions were sufficient
DEPENDENCIES: activated only on W2 and W3
ATOM_LOCAL_VALIDATION_STANDARD: inherited; no repeated local standard needed
```

Guardrails:

```text
G1 SOURCE_FIDELITY: active -> inside
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for locked narrow task
G3 DETAIL_PROPORTIONALITY: active -> pressure
G4 VIEWPOINT_SEPARATION: inactive; no derivative source-intent claim
```

```text
INACTIVE_CONDITIONAL_LEDGER_BOILERPLATE: 0
FALSE_MANDATORY_OPTIONAL_DSD_LAYER: 0
VALIDATION_STANDARD_REPETITION_REQUIRED: no
```

This is direct support for the v1.0 cleanup decision: conditional fields can remain absent without losing the distinctions needed by this task.

## 7. External-standard and claim boundary

The W3C Recommendation remains the normative accessibility standard for the locked criterion. DSD only re-expresses the criterion as a typed requirement carrier.

The ACT rule explicitly distinguishes rule outcome from complete success-criterion evaluation: a failed rule outcome can establish that the success criterion is not satisfied for that target, while all passed or inapplicable rule outcomes still require further testing for the success criterion as a whole.

Therefore this record does not infer:

```text
FULL_PAGE_WCAG_CONFORMANCE
FULL_SITE_WCAG_CONFORMANCE
LEGAL_ACCESSIBILITY_COMPLIANCE
ACCESSIBILITY_OF_UNTESTED_COMPONENTS
```

## 8. Baseline comparison and NO_GAIN

The official baseline already contains:

```text
normative threshold
large-text branch
exceptions
large-scale definition
labeled passed/failed/inapplicable examples
implementation-oriented ACT applicability rules
```

For the locked task of classifying these official examples, DSD adds traceable typed atom structure but does not improve the known outcome or demonstrate measured review benefit.

```text
STANDALONE_STRUCTURAL_GAIN: not demonstrated
MEASURED_PRACTICAL_GAIN: not measured
BASELINE_PREFERENCE: W3C normative text + ACT labels
FINAL_SPEC_STATUS: no_gain
```

This does not negate DSD method-family handoff utility established separately by `SPEC-LINK-001`.

## 9. Guardrail verdict

```text
G1 SOURCE_FIDELITY: INSIDE_GUARDRAILS
G3 DETAIL_PROPORTIONALITY: GUARDRAIL_PRESSURE
HARD_FAILURES: 0
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
```

The pressure is representational: a short labeled W3C example corpus does not need the DSD record for its own primary use. The v1.0 core/conditional split reduced the burden compared with forcing every available ledger, so the pressure did not reach recoverable exceed or purpose distortion.

## 10. Final standard result

```text
SPECIFICATION_RESULT_ID: SPEC-APP-004
SPECIFICATION_PROTOCOL_VERSION: v1.0
TARGET_SCOPE: WCAG 2.2 SC 1.4.3 + eight selected official ACT examples
DECLARED_DOWNSTREAM_TASK: typed threshold/applicability classification at selected-example resolution
LOCKED_REQUIREMENT_INVENTORY: W1-W4
REQUIREMENT_ATOMS: W1-W4
SELECTED_DSD_LAYERS: PROPERTY_CORE only
FINAL_SPEC_STATUS: no_gain
LIMITS: labeled/non-blind corpus; no full conformance or legal claim; no independent evaluator; no practical-time measurement
REPRODUCIBILITY_RECORD: source URLs + example IDs + protocol v1.0 + precommit commit

GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
HARD_FAILURES: none
```

## 11. Evidence interpretation

Supported:

```text
V1_0_EXTERNAL_LABELED_EXAMPLE_REPRESENTATION: pass
EXAMPLE_OUTCOME_FAMILY_MATCHES: 8/8
V1_0_CONDITIONAL_FIELD_RESTRAINT: pass_on_locked_case
EXTERNAL_STANDARD_BOUNDARY: preserved
```

Not supported:

```text
BLIND_PREDICTIVE_ACCURACY
INDEPENDENT_EVALUATOR_VALIDATION
FULL_WCAG_CONFORMANCE_TESTING
PRACTICAL_SUPERIORITY_OVER_W3C_TOOLS
UNIVERSAL_WEB_ACCESSIBILITY_VALIDATION
```

Because the W3C outcome labels were visible before DSD mapping, this case is stronger as a post-standardization interface/regression check than as new accuracy evidence.

## 12. Result

```text
RESULT:
SPECIFICATION_V1_0_EXTERNAL_LABELED_REGRESSION_NO_GAIN_WITH_LIMITATIONS
```
