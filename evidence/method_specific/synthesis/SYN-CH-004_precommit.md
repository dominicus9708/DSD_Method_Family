# SYN-CH-004 Precommit / DSD 합성론 NO_GAIN Baseline Challenge 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-004
CASE_CLASS: no_gain_baseline
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B0_TYPED_CHAIN_CHECKER
```

This file freezes the task, baseline, gain criteria, candidate basis, expected comparison dimensions, and scoring before execution. The baseline is intentionally competent and receives the same claim-relevant raw records as DSD Synthesis.

## 2. Purpose

Test whether DSD Synthesis can honestly return `NO_GAIN` when a non-DSD typed chain checker preserves the same information and reaches the same claim-relevant result.

The challenge must not weaken the baseline to manufacture a DSD advantage.

## 3. Frozen Synthesis task

```text
SYNTHESIS_TASK_ID: SYN-TASK-004
TASK_SCOPE: finite ordered three-component chain composition
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component identities
  exact adjacent interface mappings
  exact middle-component readiness status/value class
COMPOSITION_CANDIDATE_BASIS: {Q1,Q2,Q3,Q4,Q5}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-004
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: not_used
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE: static_order_only
```

## 4. Components

All components are Formation-admitted.

```text
SRC
  input_port: NONE
  output_port: alpha

M0
  input_port: alpha
  output_port: beta
  readiness: DEFINED_ZERO

M1
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO

MU
  input_port: alpha
  output_port: beta
  readiness: APPLICABLE_BUT_UNDEFINED

MX
  input_port: delta
  output_port: beta
  readiness: DEFINED_NONZERO

SNK
  input_port: beta
  output_port: NONE
```

## 5. Supplied composition rule and hard conditions

```text
R_CHAIN_READY
(X ⊙ Y) ⊙ Z is synthesis-admissible iff:
  H1 all participating components are Formation-admitted;
  H2 X.output exists and exactly matches Y.input;
  H3 Y.output exists and exactly matches Z.input;
  H4 readiness(Y) is defined, where DEFINED_ZERO and DEFINED_NONZERO both count as defined.
```

Rule profile:

```text
COMPOSITION_ARITY: ternary through fixed binary nesting
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
COMMUTATIVITY: supplied_false
ASSOCIATIVITY: unspecified
GROUPING_OR_PARENTHESIZATION_POLICY: fixed_left_associated_only
MULTIPLICITY_POLICY: one listed occurrence of each role per candidate
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
  candidates are materially equivalent only if all TARGET_RESOLUTION fields match exactly
PROPERTY_LIFT_OR_REDECLARATION_RULE: not_used
NEW_FORMATION_MODEL_POLICY: remain_within_inherited_formation_background
INFORMATION_LOSS_TOLERANCE: none at TARGET_RESOLUTION
```

## 6. Frozen candidates and expected DSD verdicts

```text
Q1 = (SRC ⊙ M0) ⊙ SNK
  expected: admissible
  failure set: NONE

Q2 = (SRC ⊙ M1) ⊙ SNK
  expected: admissible
  failure set: NONE

Q3 = (SRC ⊙ MU) ⊙ SNK
  expected: rejected
  failure set: {H4}

Q4 = (SRC ⊙ MX) ⊙ SNK
  expected: rejected
  failure set: {H2}

Q5 = (M1 ⊙ SRC) ⊙ SNK
  expected: rejected
  failure set: {H2,H3}
```

Expected DSD closure:

```text
SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {Q1,Q2}
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

`Q1` and `Q2` remain materially distinct because `TARGET_RESOLUTION` preserves middle-component identity and readiness class.

## 7. Frozen competent baseline

Baseline identity:

```text
B0_TYPED_CHAIN_CHECKER
```

B0 is a non-DSD finite typed composition checker. It receives exactly the same:

```text
component identities
Formation-admitted flags
input/output port records
readiness raw status classes
composition rule R_CHAIN_READY
grouping/order lock
candidate basis {Q1,Q2,Q3,Q4,Q5}
coverage declaration
target resolution
```

B0 is explicitly allowed to preserve the following readiness vocabulary:

```text
DEFINED_ZERO
DEFINED_NONZERO
APPLICABLE_BUT_UNDEFINED
```

B0 must:

```text
1. evaluate H1-H4 independently;
2. preserve all failed hard conditions rather than first-failure-only truncation;
3. return the complete admissible family within frozen coverage;
4. preserve Q1/Q2 material distinctness at TARGET_RESOLUTION;
5. retain candidate-to-failure-set traceability;
6. not perform Optimization, Transformation, Aggregation, or hidden Design;
7. report the same frozen-scope closure vocabulary in ordinary non-DSD terms.
```

Expected B0 results:

```text
Q1 -> admissible / NONE
Q2 -> admissible / NONE
Q3 -> rejected / {H4}
Q4 -> rejected / {H2}
Q5 -> rejected / {H2,H3}
BASELINE_ADMISSIBLE_FAMILY: {Q1,Q2}
BASELINE_CLOSURE: admissible synthesis family exists within frozen exhaustive candidate basis
```

## 8. Frozen gain criteria

```text
G1 STATUS_DISTINCTION_GAIN
  established only if DSD preserves a claim-relevant readiness distinction that B0 loses.

G2 FAILURE_TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant rejection basis that B0 cannot preserve.

G3 COMPOSITION_CLOSURE_GAIN
  established only if DSD reaches a more correct claim-level family/closure without changing the frozen task.

G4 TARGET_DISTINCTNESS_GAIN
  established only if DSD preserves a material target distinction at TARGET_RESOLUTION that B0 loses.

G5 RETRACEABILITY_GAIN
  established only if DSD provides a claim-relevant candidate/result trace that B0 cannot reproduce from the same frozen inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> method gain is not established and challenge fails.
If at least one G1-G5 is established -> GAIN_ESTABLISHED.
If DSD and B0 are both correct and B0 matches DSD on all G1-G5 dimensions -> NO_GAIN.
Otherwise -> NOT_ASSESSED / unresolved according to the frozen comparison record, and the challenge does not count as a NO_GAIN pass.
```

Efficiency, readability, terminology preference, implementation cost, and domain usefulness are not scored.
Extra DSD bookkeeping alone is not a gain criterion.

## 9. Precommitted scoring

Total required checks: **35**.

```text
A. precommit integrity: 6
  A1 Protocol commit fixed
  A2 baseline identity/capabilities fixed
  A3 candidate basis and coverage fixed
  A4 target resolution fixed
  A5 gain criteria G1-G5 fixed
  A6 no post-hoc weakening of B0 or task

B. DSD candidate/closure checks: 10
  B1 Q1 admissible
  B2 Q2 admissible
  B3 Q3 rejected {H4}
  B4 Q4 rejected {H2}
  B5 Q5 rejected {H2,H3}
  B6 DSD family exactly {Q1,Q2}
  B7 Q1/Q2 remain materially distinct
  B8 terminal = SYNTHESIS_ADMISSIBLE
  B9 conformance = CONFORMANT
  B10 no neighboring-method operation absorbed

C. baseline checks: 9
  C1-C5 Q1-Q5 exact verdict/failure-set match
  C6 baseline family exactly {Q1,Q2}
  C7 Q1/Q2 distinctness preserved
  C8 full failure traceability preserved
  C9 no hidden neighboring-method operation

D. gain checks: 7
  D1 G1 NOT_ESTABLISHED if B0 preserves readiness distinction
  D2 G2 NOT_ESTABLISHED if failure sets match
  D3 G3 NOT_ESTABLISHED if family/closure match
  D4 G4 NOT_ESTABLISHED if target distinctness matches
  D5 G5 NOT_ESTABLISHED if both are retraceable from frozen inputs
  D6 final method gain = NO_GAIN when D1-D5 all hold
  D7 NO_GAIN is not interpreted as method failure

E. scope discipline: 3
  E1 no baseline superiority claim
  E2 no external/reproducibility/independence/maturity claim
  E3 no whole-Property, temporal-process, or global-domain claim added
```

Decision:

```text
35/35 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

## 10. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS: 3
POSITIVE_SYNTHESIS_CASES: 1
NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
NO_GAIN_SYNTHESIS_CASES: 0
BASELINE_COMPARISON_CASES: 0
```

A completed PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
NO_GAIN_SYNTHESIS_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
```

It does not establish strongest-reasonable-baseline coverage, external applicability, reproducibility, independent validation, or method maturity.
