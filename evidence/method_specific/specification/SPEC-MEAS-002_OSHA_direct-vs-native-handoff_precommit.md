# SPEC-MEAS-002 — OSHA Direct Baseline vs DSD Native Handoff Precommit

Date: 2026-09-08
Method under practical comparison: DSD Specification v1.0 as an upstream carrier into DSD Audit
Case source: OSHA 29 CFR 1910.38 + OSHA EAP / employee-alarm eTool and checklists
Existing DSD-side source record: `SPEC-APP-003_OSHA_EAP_core_guidance.md`
Existing DSD-side handoff evidence: `SPEC-LINK-001_specification-to-audit-handoff.md`
Status: PRECOMMITTED_BEFORE_DIRECT_BASELINE_RESULT

## 1. Question

Does inserting DSD Specification as a native criterion carrier between the OSHA source corpus and DSD Audit produce a measurable practical handoff advantage over letting DSD Audit consume the strong official OSHA source/checklist baseline directly?

This benchmark tests the user's project-level hypothesis that a native DSD method can have integration utility even where a competent external method already exists.

It does **not** assume that native handoff utility implies practical superiority.

## 2. Routes

```text
ROUTE_O — strong official baseline
OSHA regulation + official eTool/checklists
-> DSD Audit directly

ROUTE_D — DSD-native handoff
OSHA regulation + official eTool/checklists
-> DSD Specification typed criterion carrier
-> DSD Audit
```

The official OSHA route is not weakened or paraphrased into a strawman. It may use the full authoritative regulation, the eTool explanations, and the official checklist material.

## 3. Locked probes

Reuse the six already fixed probe families from `SPEC-LINK-001`:

```text
P1 reporting procedure present
P2 accountability procedure absent
P3 one undifferentiated alarm signal
P4 plan-change review trigger absent
P5 optional auxiliary-power recommendation absent
P6 exact assembly point not supplied
```

Expected domain-level families are already fixed by the source corpus and prior handoff pilot. No probe may be added or removed after the direct baseline result is created.

## 4. Primary comparison axes

For each route record:

```text
A1 AUDIT_FINDING_MATCHES / 6
A2 FALSE_POSITIVE_ON_OPTIONAL_GUIDANCE
A3 FALSE_FAILURE_FROM_SITE_SPECIFIC_OPENNESS
A4 NORMATIVE_FORCE_PRESERVATION
A5 SOURCE_OR_NORM_REFERENCE_PRESERVATION
A6 FABRICATED_SITE_SPECIFIC_FACTS
```

## 5. Burden proxies

Because no human-timing experiment is available, burden is measured only through explicit structural proxies.

```text
B1 INTERMEDIATE_SPECIFICATION_ARTIFACT_REQUIRED
B2 REQUIREMENT_ATOM_OR_CHECK_ITEM_COUNT_USED_BY_ROUTE
B3 SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED
B4 HIDDEN_RETRANSLATION_REQUIRED
B5 ADDITIONAL_DSD_LAYER_OR_BRIDGE_REQUIRED
```

Interpretation rules:

- `SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED = yes` means the receiving audit must derive the probe-relevant criterion semantics from the external source at audit time because no prior typed DSD criterion carrier exists.
- This is a structural handoff proxy, **not** measured cognitive time.
- Route D's prior Specification work counts as upstream cost and cannot be treated as free.
- Route O may be preferred on a single audit if it achieves the same findings without the extra upstream representation.
- Route D may have reusable-carrier value, but reuse is not credited as measured benefit unless multiple downstream uses are actually tested.

## 6. Verdict categories

```text
DSD_PRACTICAL_HANDOFF_GAIN
TIE_WITH_DSD_TRACEABILITY_ADVANTAGE
TIE_WITH_DSD_OVERHEAD
BASELINE_PREFERRED
DSD_PREFERRED
INDETERMINATE
```

Rules:

- `DSD_PRACTICAL_HANDOFF_GAIN` requires a measurable improvement on the locked accuracy/error axes or on an actually measured workload outcome; merely having more explicit fields is insufficient.
- `TIE_WITH_DSD_TRACEABILITY_ADVANTAGE` requires equal findings plus a clear structural carrier advantage, but no claim of time/error benefit.
- `TIE_WITH_DSD_OVERHEAD` applies when findings are equal and the DSD route adds upstream representation without a demonstrated downstream outcome advantage in this single-use benchmark.
- `BASELINE_PREFERRED` applies if the official direct route is materially better on the locked task.
- `DSD_PREFERRED` applies if DSD is materially better on the locked task.
- Unfavorable and tied results are valid.

## 7. Anti-post-hoc lock

```text
POST_RESULT_PROBE_CHANGE: prohibited
POST_RESULT_AXIS_CHANGE: prohibited
POST_RESULT_VERDICT_RULE_CHANGE: prohibited
CREDITING_UNMEASURED_TIME_SAVING: prohibited
CREDITING_HYPOTHETICAL_REUSE_AS_MEASURED_GAIN: prohibited
```

## 8. Independence limit

This is a same-project retrospective paired integration benchmark. The DSD handoff result already exists before this benchmark and is not blind.

Therefore:

```text
BLIND_COMPARISON: no
INDEPENDENT_EVALUATOR: no
EVIDENCE_USE: practical structural comparison only
```
