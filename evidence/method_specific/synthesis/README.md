# DSD Synthesis Direct Evidence / DSD 합성론 직접 증거

Status: **planning / proposed / Step 2 boundary attack complete / validation pending**

This lane records evidence that directly tests **DSD Synthesis / DSD 합성론**.

Shared-core evidence, Design evidence, Transformation evidence, Aggregation evidence, or other neighboring-method results may be referenced but do not automatically count as direct Synthesis validation.

## Current development state

```text
DEDICATED_SYNTHESIS_PROTOCOL: not established
DIRECT_SYNTHESIS_PILOTS: 0
POSITIVE_SYNTHESIS_CASES: 0
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 0
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 0
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_pending
```

## Planning artifacts

- `methods/05_synthesis/TASK_INTERFACE_v0.1-draft.md` — Step-1 historical task-interface draft.
- `methods/05_synthesis/BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` — Step-2 pre-protocol boundary attack, 16 cases.
- `methods/05_synthesis/TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md` — Step-2 non-breaking interface refinement.
- `methods/05_synthesis/PLANNING.md` — current development sequence.
- `methods/05_synthesis/WORKLOG.md` — chronological worklog.

Planning artifacts do not increase the direct-pilot count.

Effective pre-protocol interface:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

## Step-2 boundary planning result

```text
BOUNDARY_ATTACKS_RUN: 16
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
```

The attacks preserve the method boundary against Design, Transformation, Aggregation, and Optimization while pressure-testing property lifting, algebraic assumptions, target equivalence, partial-synthesis residuals, process scope, exhaustiveness, and Formation/domain-composition separation.

Required non-breaking refinement groups:

```text
COMPOSITION_LAW_PROFILE
GROUPING_OR_PARENTHESIZATION_POLICY
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE
RESIDUAL_OPEN_INTERFACES_OR_OBLIGATIONS
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE
```

These are not direct validation results because no executable Synthesis protocol existed when the attacks were run.

## Direct-evidence case convention

Initial convention:

```text
SYN-CH-###   constructed Synthesis challenges
SYN-APP-###  external or independently generated Synthesis applications
SYN-AUD-###  Synthesis-specific audit / maturity records
SYN-IEP-###  independent evaluator packet infrastructure
```

Case IDs become active after the first executable Synthesis protocol is frozen.
Pre-protocol planning attacks use the `SYN-BND-DRAFT-*` namespace and are not retroactively counted as protocol-level direct evidence.

## Minimum evidence architecture

A future promotion consideration should accumulate, at minimum:

1. a dedicated executable Synthesis protocol;
2. positive cases;
3. negative/failure cases;
4. method-boundary cases;
5. `NO_GAIN` cases;
6. method-appropriate reproducibility/retraceability records;
7. at least one external or independently generated application;
8. a strongest-reasonable-baseline comparison when applicable.

These are evidence categories, not an automatic maturity certificate.

## Current planning guards

```text
INDIVIDUAL_COMPONENT_ADMISSIBILITY
!= AUTOMATIC_COMPOSABILITY

EXHAUSTIVE_COMPONENT_LIST
!= EXHAUSTIVE_COMPOSITION_SPACE

FORMATION_CLAUSE_VII_COMPOSITION
!= DOMAIN_SYNTHESIS_LEGITIMACY

AGGREGATE_READOUT
!= SYNTHESIZED_WHOLE

COMPONENT_PROPERTY
!= WHOLE_PROPERTY

candidate ID / syntax tree
!= material synthesized-target distinctness

PARTIAL_SYNTHESIS
!= completed synthesized target

STATIC_COMPOSITION_ORDER
!= TEMPORAL_ASSEMBLY_SEQUENCE
```

The next direct-development task is **Protocol v0.1 establishment**, not yet a direct pilot.
No Synthesis result should be called direct validation until an executable protocol and separately frozen case record exist.
