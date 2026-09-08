# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **planning / no direct validation yet**

This lane records evidence that directly tests **DSD Design / DSD 설계론**.

Evidence from DSD Analysis, Audit, Specification, Synthesis, Transformation, Optimization, or shared-core validation does not automatically count as direct Design validation.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: method_specific
METHOD_DIRECTLY_TESTED: DSD Design
METHOD_VERSION_OR_PROTOCOL:
CASE_ID:
CASE_ORIGIN:
TASK:
GOAL:
CONSTRAINTS:
INPUTS:
DSD_LAYERS_USED:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
CANDIDATE_GENERATION_RULE:
ADMISSIBILITY_CHECK:
PROPERTY_AND_PREREQUISITE_CHECK:
CHANNEL_OR_BRIDGE_REQUIREMENTS:
OUTPUT_OR_TRAJECTORY_REQUIREMENTS:
SELECTION_RULE:
REJECTED_CANDIDATE_REASONS:
FAILURE_OR_NO_GAIN_CRITERIA:
BASELINE:
RESULT:
LIMITS:
REPRODUCIBILITY_RECORD:
```

## Planned case classes

```text
DES-CH-*   constructed challenges
DES-APP-*  external or independently generated applications
DES-AUD-*  Design-specific maturity/audit records
```

The prefixes are provisional until Protocol v0.1 fixes the case-ID convention.

## Minimum evidence architecture before promotion consideration

1. dedicated Design protocol;
2. positive constructed case;
3. negative/failure case;
4. boundary case;
5. `NO_GAIN` case;
6. reproducibility/retrace record;
7. at least one external or independently generated application case;
8. strongest-reasonable-baseline comparison when applicable.

A later maturity audit evaluates the accumulated corpus; the checklist itself does not confer maturity.

## Current status

```text
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
CURRENT_PROTOCOL: not established
CURRENT_METHOD_STATUS: planning / proposed
```

## Immediate next evidence task

Do not begin application pilots until the Design-specific task interface, minimum valid output, and boundary against Specification/Synthesis/Transformation/Optimization are explicitly fixed.
