# SPEC-MEAS-003 — ROUTE_D DSD Specification v1.0 Reusable Criterion Carrier

Date: 2026-09-08
Protocol: DSD Specification v1.0
Source basis: previously locked OSHA EAP requirement families used by `SPEC-APP-003` and `SPEC-LINK-001`
Status: FROZEN_BEFORE_REUSE_SCORING

## Core lock

```text
SPECIFICATION_ID: SPEC-MEAS-003-ROUTE-D
TARGET_SCOPE: six locked OSHA EAP audit criterion families
REQUIREMENT_SOURCE_SET: existing SPEC-APP-003 locked OSHA corpus
SELECTED_DSD_LAYERS: PROPERTY_CORE
DECLARED_DOWNSTREAM_TASK: repeated DSD Audit criterion reuse across four target plan snapshots
```

No Formation, Static Aggregation, or Dynamics layer is activated for this benchmark.

## D1 — Reporting procedure

```text
REQUIREMENT_ID: D1
SOURCE_REFERENCE: OSHA EAP reporting-procedure requirement family
TARGET_ENTITY_OR_CARRIER: target plan reporting procedure
REQUIREMENT_TYPE: mandatory content requirement
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: EAP minimum-content review is active
REQUIRED_STRUCTURE_OR_VALUE: procedure for reporting fire or another emergency is present
VIOLATION_CONDITION: required reporting procedure is absent
UNRESOLVED_CONDITION: target evidence is insufficient to determine whether a reporting procedure exists
```

## D2 — Employee accountability

```text
REQUIREMENT_ID: D2
SOURCE_REFERENCE: OSHA EAP employee-accountability requirement family
TARGET_ENTITY_OR_CARRIER: target plan accountability procedure
REQUIREMENT_TYPE: mandatory content requirement
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: EAP minimum-content review is active
REQUIRED_STRUCTURE_OR_VALUE: procedure to account for employees after evacuation is present
VIOLATION_CONDITION: required accountability procedure is absent
UNRESOLVED_CONDITION: target evidence is insufficient to determine whether such a procedure exists
```

## D3 — Distinctive alarm signal

```text
REQUIREMENT_ID: D3
SOURCE_REFERENCE: OSHA employee-alarm requirement family cross-referenced from EAP material
TARGET_ENTITY_OR_CARRIER: target alarm signaling arrangement
REQUIREMENT_TYPE: mandatory alarm distinction requirement at locked review resolution
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: alarm signaling is part of the reviewed EAP condition
REQUIRED_STRUCTURE_OR_VALUE: alarm signal distinction satisfies the locked purpose-specific requirement
VIOLATION_CONDITION: only one undifferentiated signal is supplied where the locked criterion requires distinction
UNRESOLVED_CONDITION: target evidence does not establish the alarm-signaling distinction
DEPENDENCIES: applicable employee-alarm requirement family
```

## D4 — Plan-change review trigger

```text
REQUIREMENT_ID: D4
SOURCE_REFERENCE: OSHA EAP plan-change review/update trigger
TARGET_ENTITY_OR_CARRIER: target plan employee-review rule
REQUIREMENT_TYPE: mandatory review-trigger requirement
REQUIRED_OR_OPTIONAL: required
ACTIVATION_CONDITION: the emergency action plan changes
REQUIRED_STRUCTURE_OR_VALUE: affected employees are covered by the required review when the plan changes
VIOLATION_CONDITION: no plan-change review trigger is present
UNRESOLVED_CONDITION: target evidence is insufficient to determine whether the trigger exists
```

## D5 — Auxiliary-power recommendation

```text
REQUIREMENT_ID: D5
SOURCE_REFERENCE: auxiliary-power / backup-related OSHA guidance family as locked in SPEC-LINK-001
TARGET_ENTITY_OR_CARRIER: target auxiliary-power feature
REQUIREMENT_TYPE: optional guidance at this probe resolution
REQUIRED_OR_OPTIONAL: optional
ACTIVATION_CONDITION: optional guidance is being noted
REQUIRED_STRUCTURE_OR_VALUE: presence may be recorded if supplied
VIOLATION_CONDITION: none from absence by itself under this locked probe
UNRESOLVED_CONDITION: none required for an absent optional feature
```

## D6 — Exact assembly-point site detail

```text
REQUIREMENT_ID: D6
SOURCE_REFERENCE: worksite-specific implementation openness preserved in SPEC-APP-003 / SPEC-LINK-001
TARGET_ENTITY_OR_CARRIER: exact assembly-point implementation value
REQUIREMENT_TYPE: site-specific implementation detail
REQUIRED_OR_OPTIONAL: conditional / source-open at this review resolution
ACTIVATION_CONDITION: a downstream task specifically requires an exact site value
SOURCE_OPENNESS_STATUS: SOURCE_INTENTIONAL_OPENNESS
DOWNSTREAM_DETERMINACY_STATUS: SUFFICIENT_AT_DECLARED_RESOLUTION
REQUIRED_STRUCTURE_OR_VALUE: preserve the site-specific boundary; do not fabricate an exact value
VIOLATION_CONDITION: an exact assembly-point value is fabricated or its absence alone is treated as a failure without additional authority
UNRESOLVED_CONDITION: exact value remains open if a stronger downstream task later requires it
```

## Handoff availability

The receiving DSD Audit can directly consume:

```text
SOURCE_REFERENCE
REQUIRED_OR_OPTIONAL
ACTIVATION_CONDITION
VIOLATION_CONDITION
SOURCE_OPENNESS_STATUS when active
DOWNSTREAM_DETERMINACY_STATUS when active
```

## Reuse rule

```text
CARRIER_PERSISTENCE_ALLOWED: yes
SOURCE_REEXTRACTION_REQUIRED_AFTER_FREEZE: no
NUMBER_OF_LOCKED_CRITERIA: 6
```

The same carrier is reused for TARGET_A through TARGET_D.