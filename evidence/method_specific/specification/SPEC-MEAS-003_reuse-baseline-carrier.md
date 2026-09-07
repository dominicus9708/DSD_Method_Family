# SPEC-MEAS-003 — ROUTE_B Reusable Conventional Criterion Carrier

Date: 2026-09-08
Source basis: previously locked OSHA EAP requirement families used by `SPEC-APP-003` and `SPEC-LINK-001`
Status: FROZEN_BEFORE_REUSE_SCORING

This is a strong reusable non-DSD baseline. It is intended to remain available across all four downstream audit targets without re-reading the source corpus.

## B1 — Reporting procedure

Source reference: OSHA EAP reporting-procedure requirement family.
Normative character: required.
Decision rule: if the target plan contains a procedure for reporting fire or another emergency, mark addressed; if absent, record a required omission.

## B2 — Employee accountability

Source reference: OSHA EAP employee-accountability requirement family.
Normative character: required.
Decision rule: if the target plan contains a procedure to account for employees after evacuation, mark addressed; if absent, record a required omission.

## B3 — Distinctive alarm signal

Source reference: OSHA employee-alarm requirement family cross-referenced from the EAP material.
Normative character: required at the locked review resolution.
Decision rule: if the target uses a distinct alarm signal appropriate to the purpose being evaluated, mark addressed; if the target states only one undifferentiated signal where the locked requirement needs distinction, record a finding.

## B4 — Plan-change review trigger

Source reference: OSHA EAP review/update trigger for plan changes.
Normative character: required.
Decision rule: if the plan requires review with affected employees when the plan changes, mark addressed; if absent, record a required omission.

## B5 — Auxiliary-power recommendation

Source reference: auxiliary-power / backup-related OSHA guidance family as locked in `SPEC-LINK-001`.
Normative character for this benchmark probe: optional guidance; absence by itself is not a regulatory failure under this probe.
Decision rule: presence may be noted; absence is a non-failure for this locked probe.

## B6 — Exact assembly-point detail

Source reference: worksite-specific implementation openness preserved in `SPEC-APP-003` / `SPEC-LINK-001`.
Normative character: site-specific/open at this review resolution.
Decision rule: absence of an exact assembly-point value is not by itself a failure. Do not fabricate a site-specific value. Record as open/non-failure unless a different locked source requires the exact value.

## Reuse rule

```text
CARRIER_PERSISTENCE_ALLOWED: yes
SOURCE_REEXTRACTION_REQUIRED_AFTER_FREEZE: no
NUMBER_OF_LOCKED_CRITERIA: 6
```

The same carrier is reused for TARGET_A through TARGET_D.