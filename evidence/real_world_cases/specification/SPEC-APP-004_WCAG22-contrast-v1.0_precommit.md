# SPEC-APP-004 — WCAG 2.2 Contrast (Minimum) v1.0 External Labeled-Example Regression Precommit

Date: 2026-09-08
Method: DSD Specification
Protocol: v1.0

## Purpose

Test the newly standardized DSD Specification Protocol v1.0 on a public, independently authored, externally labeled accessibility corpus.

This is primarily a **representation/conditional-activation regression**, not a blind prediction test.

The W3C ACT example outcome labels were visible before DSD mapping, so this case must not be counted as independent predictive validation.

## Locked sources

Primary normative source:
- W3C Recommendation, Web Content Accessibility Guidelines (WCAG) 2.2, Success Criterion 1.4.3 Contrast (Minimum), latest Recommendation text observed 2024-12-12.
- https://www.w3.org/TR/WCAG22/#contrast-minimum

Auxiliary official labeled test corpus:
- W3C/WAI ACT Rule: Text has minimum contrast.
- https://www.w3.org/WAI/standards-guidelines/act/rules/afw4f7/

## Locked downstream task

Represent the selected WCAG 1.4.3 requirement branches and classify eight official ACT examples at the resolution of text contrast requirement applicability/threshold status.

Do not claim full-page WCAG conformance.

## Locked DSD interfaces

```text
FORMATION_LAYER: not used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

Property Core is used only to preserve typed applicability/status distinctions. No DSD layer may replace the W3C normative standard.

## Locked requirement inventory

```text
W1 NORMAL_TEXT_MINIMUM
  visible text/images of text not covered by an exception require contrast >= 4.5:1

W2 LARGE_TEXT_MINIMUM
  large-scale text/images of large-scale text require contrast >= 3:1

W3 INCIDENTAL_EXCEPTION
  inactive UI, pure decoration, not-visible text, or text inside a picture with significant other visual content has no SC 1.4.3 contrast requirement

W4 LOGOTYPE_EXCEPTION
  logo/brand-name text has no SC 1.4.3 contrast requirement
```

For large-scale classification, use the WCAG definition: at least 18 point, or at least 14 point bold, or an equivalent size for CJK fonts.

## Locked selected official examples

```text
E1 ACT Passed Example 1  — #333 on #FFF, normal text, reported 12.6:1
E2 ACT Passed Example 5  — 18pt black on #666, reported 3.6:1
E3 ACT Passed Example 6  — 14pt bold black on #666, reported 3.6:1
E4 ACT Failed Example 1  — #AAA on white, reported 2.3:1
E5 ACT Failed Example 8  — informative Helvetica sample, #777 on #EEE, reported 3.85:1
E6 ACT Failed Example 9  — button text #777 on #EEE, reported 3.85:1
E7 ACT Inapplicable Example 1 — display:none text
E8 ACT Inapplicable Example 6 — label associated with disabled widget
```

## v1.0 conditional-field precommit

The test specifically checks that v1.0 does not force inactive ledgers.

Expected activation discipline:

```text
PRECEDENCE_OR_PRIORITY: inactive
SOURCE_OPENNESS_STATUS: inactive
DOWNSTREAM_DETERMINACY_STATUS: inactive
ALLOWED_ALTERNATIVES: active only when needed to express threshold branch/exception
PROHIBITED_STATES: optional
DEPENDENCIES: active only for large-text/applicability branch conditions
ATOM_LOCAL_VALIDATION_STANDARD: inherit W3C source unless local clarification needed

G1 SOURCE_FIDELITY: active
G2 PURPOSE_AND_PRIORITY_FIDELITY: inactive for this narrow classification task
G3 DETAIL_PROPORTIONALITY: active for baseline comparison
G4 VIEWPOINT_SEPARATION: inactive; no derivative interpretive viewpoint is claimed
```

## Scoring criteria

```text
S1 requirement branches W1-W4 preserved without normative strengthening
S2 all eight example outcome families represented without source-fact invention
S3 normal/large threshold distinction preserved
S4 inactive/not-visible exception not collapsed into ordinary threshold failure
S5 disabled-widget applicability boundary preserved
S6 inactive v1.0 conditional fields remain omitted rather than boilerplated
S7 external-standard authority remains W3C
S8 no full-WCAG or legal-compliance claim is inferred
S9 DSD result compared against the official labeled ACT baseline without forcing a gain claim
```

## Permitted final outcomes

```text
usable
usable_with_unresolved_items
no_gain
underspecified
contradictory
```

Likely comparative labels are not precommitted as success requirements. A `no_gain` result is acceptable.

## Evidence limitations locked before scoring

```text
SOURCE_OUTCOME_LABELS_VISIBLE_TO_EVALUATOR: yes
BLIND_PREDICTION_TEST: no
INDEPENDENT_EVALUATOR: no
MEASURED_ENGINEERING_BENEFIT: no
FULL_WCAG_CONFORMANCE_TEST: no
```
