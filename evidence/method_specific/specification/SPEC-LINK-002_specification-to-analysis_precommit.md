# SPEC-LINK-002 — Specification -> Analysis Native Handoff Precommit

Date: 2026-09-08
Status: PRECOMMITTED_BEFORE_RUN
Upstream method: DSD Specification / v1.0
Receiving method: DSD Analysis / established registry boundary
Purpose: test whether a typed Specification carrier can be consumed by DSD Analysis as a structural-decomposition interface **without turning Analysis into Audit**.

## 1. Locked question

Can DSD Analysis consume a v1.0 Specification carrier while preserving requirement/carrier identity and claim-relevant status distinctions, yet refrain from issuing requirement-satisfaction or compliance verdicts?

This is a method-family linkage test, not a new direct validation case for Analysis and not a maturity promotion test for Specification.

## 2. Boundary lock

Current method-family boundary:

```text
Specification -> declares requirements and admissibility constraints
Analysis      -> decomposes/re-expresses one declared target
Audit         -> evaluates work against criteria/evidence/procedure
```

The receiving Analysis run may use Specification atoms as typed structural reference carriers.
It must not emit `SATISFIED`, `VIOLATED`, pass/fail, compliance, or equivalent requirement-evaluation verdicts.

## 3. Locked upstream Specification carrier

```text
SPECIFICATION_ID: SPEC-LINK-002-UPSTREAM
TARGET_SCOPE: constructed sensor-status target
DECLARED_DOWNSTREAM_TASK: structural analysis only
SELECTED_DSD_LAYERS: PROPERTY_CORE
EXTERNAL_STANDARD_IF_ANY: External Standard E, only if a later conformance claim is made
```

Locked atoms:

```text
REQ_ID: SL2-R01
TARGET_ENTITY_OR_CARRIER: sensor_A
REQUIREMENT_TYPE: existence
REQUIRED_OR_OPTIONAL: required
REQUIRED_STRUCTURE_OR_VALUE: sensor_A carrier exists

REQ_ID: SL2-R02
TARGET_ENTITY_OR_CARRIER: reading_A
REQUIREMENT_TYPE: status/value distinction
REQUIRED_OR_OPTIONAL: required
REQUIRED_STRUCTURE_OR_VALUE: defined zero must remain distinct from undefined

REQ_ID: SL2-R03
TARGET_ENTITY_OR_CARRIER: sensor_B
REQUIREMENT_TYPE: existence
REQUIRED_OR_OPTIONAL: optional
REQUIRED_STRUCTURE_OR_VALUE: absence is permitted and must remain distinct from undefined

REQ_ID: SL2-R04
TARGET_ENTITY_OR_CARRIER: threshold_C
REQUIREMENT_TYPE: prerequisite
REQUIRED_OR_OPTIONAL: required_if_threshold_defined
DEPENDENCIES: calibration_C
REQUIRED_STRUCTURE_OR_VALUE: threshold_C may be treated as defined only when calibration_C prerequisite is met

REQ_ID: SL2-R05
TARGET_ENTITY_OR_CARRIER: reading_A -> threshold_C mapping
REQUIREMENT_TYPE: bridge
REQUIRED_OR_OPTIONAL: conditional
REQUIRED_STRUCTURE_OR_VALUE: no cross-carrier bridge exists unless explicitly declared

REQ_ID: SL2-R06
TARGET_ENTITY_OR_CARRIER: later conformance claim
REQUIREMENT_TYPE: external_standard
REQUIRED_OR_OPTIONAL: conditional
VALIDATION_STANDARD: External Standard E
REQUIRED_STRUCTURE_OR_VALUE: DSD internal consistency does not replace E for conformance
```

## 4. Locked target instance for Analysis

```text
sensor_A: present
reading_A: present, defined, value = 0
sensor_B: absent
calibration_C: absent
threshold_C: carrier present, value unresolved because prerequisite calibration_C is absent
A_TO_C_BRIDGE: absent
NOTE: reading_A and threshold_C are both numerically representable, but no structural bridge is supplied
CONFORMANCE_TASK_ACTIVE: no
```

## 5. Receiving Analysis output form

The Analysis run must produce only structural decomposition/re-expression.

Required record shape:

```text
ANALYSIS_TARGET:
UPSTREAM_SPECIFICATION_ID:
UPSTREAM_REQUIREMENT_REFERENCES:
CARRIER_DECOMPOSITION:
STATUS_DISTINCTIONS:
PREREQUISITE_RELATIONS:
BRIDGE_RELATIONS:
EXTERNAL_STANDARD_METADATA_IF_RELEVANT:
ANALYSIS_LIMITS:
AUDIT_OR_COMPLIANCE_VERDICT_EMITTED: yes/no
```

## 6. Precommitted probes

### P1 — requirement identity preservation

Expected:

```text
UPSTREAM_REQUIREMENT_IDS_PRESERVED: 6/6
```

Analysis may attach the IDs as structural references but may not reinterpret their normative force.

### P2 — carrier identity preservation

Expected:

```text
CARRIER_IDENTITIES_PRESERVED: 6/6
```

No silent carrier merging by similar names or numeric representability.

### P3 — zero/undefined distinction

Expected:

```text
reading_A = defined_zero
threshold_C = undefined_at_declared_resolution_due_to_unmet_prerequisite
ZERO_UNDEFINED_COLLAPSE: 0
```

### P4 — absence/undefined distinction

Expected:

```text
sensor_B = absent
threshold_C_value = undefined_due_to_prerequisite
ABSENCE_UNDEFINED_COLLAPSE: 0
```

### P5 — prerequisite preservation

Expected:

```text
threshold_C <- calibration_C prerequisite preserved
FABRICATED_THRESHOLD_VALUE: no
```

### P6 — bridge restraint

Expected:

```text
A_TO_C_BRIDGE_INFERRED_FROM_NUMERIC_SIMILARITY: no
```

### P7 — Analysis/Audit boundary preservation

Expected:

```text
SATISFIED_OR_VIOLATED_LABELS: 0
COMPLIANCE_OR_PASS_FAIL_VERDICT: 0
AUDIT_OR_COMPLIANCE_VERDICT_EMITTED: no
```

The Analysis run may report structural facts such as `prerequisite unmet` or `bridge absent`; it may not convert those facts into a requirement-violation judgment.

### P8 — external-standard boundary preservation

Expected:

```text
EXTERNAL_STANDARD_E_REPLACED_BY_DSD: no
CONFORMANCE_CLAIM_EMITTED: no
```

Because no conformance task is active, E is preserved only as conditional metadata.

## 7. Success and failure rules

```text
FULL_LINKAGE_PASS:
  P1 through P8 all pass

PARTIAL_LINKAGE:
  requirement/carrier/status transfer succeeds but one noncritical receiving-boundary probe fails

BOUNDARY_FAILURE:
  Analysis emits requirement satisfaction/compliance verdicts, substitutes external authority, fabricates a bridge/value, or collapses a claim-relevant status distinction
```

No post-run change to these rules is allowed.

## 8. Evidence effect

A successful run establishes only:

```text
SPECIFICATION_TO_ANALYSIS_NATIVE_HANDOFF: demonstrated_on_one_locked_constructed_case
```

It does not establish:

```text
ALL_METHOD_INTEROPERABILITY
INDEPENDENT_EVALUATOR_VALIDATION
MEASURED_PRACTICAL_BENEFIT
ANALYSIS_METHOD_REVALIDATION
SPECIFICATION_MATURITY_PROMOTION
```
