# SYN-CH-006 Precommit / DSD 합성론 Broader Strongest-Reasonable-Baseline 사전동결

Status: **PRECOMMITTED — evaluation not yet executed at commit time**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**  
Protocol: **v0.1**  
Protocol commit: `8787b242cb6648c47396151dbac3aadc19e3d184`

## 1. Evidence identity

```text
CASE_ID: SYN-CH-006
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_session
METHOD_VERSION_OR_PROTOCOL: Synthesis Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_TYPED_COMPOSITION_GRAPH_CHECKER
```

This file freezes a materially richer comparison than `SYN-CH-005`. The baseline is intentionally strong and receives the same claim-relevant component, property, grouping, equivalence, relation-retention, and formation-effect information as DSD Synthesis. A second `NO_GAIN` result is explicitly allowed.

## 2. Frozen task

```text
SYNTHESIS_TASK_ID: SYN-TASK-006
TASK_SCOPE: finite three-component composition with grouping equivalence, explicit whole-property lift, relation retention, and formation-effect checks
CLAIMED_OUTPUT_LEVEL: SYNTHESIS_SPACE
TARGET_RESOLUTION:
  exact ordered component identities
  exact adjacent interface mapping types
  exact lifted whole-readiness status/value class
  exact retained adjacency-relation set
  exact formation effect
  grouping syntax excluded when canonicalized by the supplied associativity/equivalence rule
COMPOSITION_CANDIDATE_BASIS: {A1,A2,A3,A4,A5,A6,A7,A8}
COMPOSITION_COVERAGE: exhaustive relative only to SYN-TASK-006
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: not_used
ASSEMBLY_SEQUENCE_OR_PROCESS_SCOPE: static_order_only
```

## 3. Frozen component records

All listed components are individually Formation-admitted.

```text
SRC
  input_port: NONE
  output_port: alpha
  formation_trigger: same_background

M0
  input_port: alpha
  output_port: beta
  readiness: DEFINED_ZERO
  formation_trigger: same_background

M1
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO
  formation_trigger: same_background

MU
  input_port: alpha
  output_port: beta
  readiness: APPLICABLE_BUT_UNDEFINED
  formation_trigger: same_background

MX
  input_port: delta
  output_port: beta
  readiness: DEFINED_NONZERO
  formation_trigger: same_background

ML
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO
  formation_trigger: same_background

MN
  input_port: alpha
  output_port: beta
  readiness: DEFINED_NONZERO
  formation_trigger: new_formation_required

SNK
  input_port: beta
  output_port: NONE
  formation_trigger: same_background
```

## 4. Supplied composition rule family

Rule family:

```text
R_SEGMENT_CHAIN
```

For ordered components `X,Y,Z`, a full synthesized chain is admissible iff the following hard conditions hold under the candidate's supplied composition mode.

```text
H1 COMPONENT_ADMISSION
   every participating component is Formation-admitted.

H2 INTERFACE_COMPATIBILITY
   X.output exactly matches Y.input
   AND Y.output exactly matches Z.input.

H3 WHOLE_READINESS_DEFINED
   apply L_READY exactly:
     readiness(Y)=DEFINED_ZERO
       -> whole.readiness=DEFINED_ZERO
     readiness(Y)=DEFINED_NONZERO
       -> whole.readiness=DEFINED_NONZERO
     readiness(Y)=APPLICABLE_BUT_UNDEFINED
       -> whole.readiness=APPLICABLE_BUT_UNDEFINED
   The hard condition passes only for DEFINED_ZERO or DEFINED_NONZERO.

H4 RELATION_RETENTION
   both adjacency relations r(X,Y) and r(Y,Z) must be retained in the synthesized whole at TARGET_RESOLUTION.

H5 INHERITED_FORMATION_BACKGROUND
   apply F_FORM exactly:
     if every participating component formation_trigger=same_background
       -> FORMATION_EFFECT=same_background
     if any participating component formation_trigger=new_formation_required
       -> FORMATION_EFFECT=new_formation_required
   The hard condition passes only for same_background in SYN-TASK-006.
```

Evaluation staging is frozen:

```text
H1 and H2 are structural prerequisites.
If H1 or H2 fails, downstream whole-level H3-H5 are recorded as NOT_REACHED and are not added to FAILURE_SET.
If H1 and H2 pass, H3-H5 are all evaluated and every failed hard condition is retained.
```

## 5. Grouping, law, equivalence, and composition modes

```text
COMPOSITION_ARITY: ternary through binary composition of chain segments
COMPOSITION_ORDER_SENSITIVITY: order_sensitive
MULTIPLICITY_POLICY: one occurrence of each listed role per candidate

COMPOSITION_LAW_PROFILE:
  COMMUTATIVITY: supplied_false
  ASSOCIATIVITY: supplied_true for R_SEGMENT_CHAIN under RETAIN_ALL mode when ordered component sequence and retained relation set are unchanged
  IDENTITY_RULE: not_supplied
  IDEMPOTENCE_RULE: not_supplied
  LAW_SOURCE: frozen task rule R_SEGMENT_CHAIN

GROUPING_OR_PARENTHESIZATION_POLICY:
  left-associated and right-associated syntax both permitted where listed

COMPOSITION_MODES:
  RETAIN_ALL
    preserve both adjacency relation records
  DROP_FIRST_RELATION
    preserve interfaces for structural joining but omit r(X,Y) from the resulting whole relation record
```

Canonicalization rule:

```text
COMPOSITION_EQUIVALENCE_OR_CANONICALIZATION_RULE:
  Two candidates belong to the same material synthesized-target class iff all TARGET_RESOLUTION fields match.
  Under supplied associativity, left/right grouping syntax alone does not distinguish material targets.
  Relation loss, whole-readiness class, component identity, interface mapping, or formation effect remains material.
```

Property discipline:

```text
PROPERTY_LIFT_OR_REDECLARATION_RULE: L_READY exactly as frozen in H3
```

Relation discipline:

```text
RELATION_RETENTION_REQUIREMENT: retain r(X,Y) and r(Y,Z)
```

Formation discipline:

```text
NEW_FORMATION_MODEL_POLICY: remain_within_inherited_formation_background
```

Information-loss discipline:

```text
INFORMATION_LOSS_TOLERANCE: no loss of TARGET_RESOLUTION fields
```

## 6. Frozen candidates and expected DSD results

```text
A1 = ((SRC ⊙ M0) ⊙ SNK), mode RETAIN_ALL
  expected: admissible / NONE
  whole.readiness: DEFINED_ZERO
  relations: {r(SRC,M0), r(M0,SNK)}
  formation: same_background
  canonical class: C0

A2 = (SRC ⊙ (M0 ⊙ SNK)), mode RETAIN_ALL
  expected: admissible / NONE
  whole.readiness: DEFINED_ZERO
  relations: {r(SRC,M0), r(M0,SNK)}
  formation: same_background
  canonical class: C0

A3 = ((SRC ⊙ M1) ⊙ SNK), mode RETAIN_ALL
  expected: admissible / NONE
  whole.readiness: DEFINED_NONZERO
  relations: {r(SRC,M1), r(M1,SNK)}
  formation: same_background
  canonical class: C1

A4 = (SRC ⊙ (M1 ⊙ SNK)), mode RETAIN_ALL
  expected: admissible / NONE
  whole.readiness: DEFINED_NONZERO
  relations: {r(SRC,M1), r(M1,SNK)}
  formation: same_background
  canonical class: C1

A5 = ((SRC ⊙ MU) ⊙ SNK), mode RETAIN_ALL
  expected: rejected / {H3}
  whole.readiness: APPLICABLE_BUT_UNDEFINED

A6 = ((SRC ⊙ MX) ⊙ SNK), mode RETAIN_ALL
  expected: rejected / {H2}
  downstream H3-H5: NOT_REACHED

A7 = ((SRC ⊙ ML) ⊙ SNK), mode DROP_FIRST_RELATION
  expected: rejected / {H4}
  whole.readiness: DEFINED_NONZERO
  retained relations: {r(ML,SNK)}
  formation: same_background

A8 = ((SRC ⊙ MN) ⊙ SNK), mode RETAIN_ALL
  expected: rejected / {H5}
  whole.readiness: DEFINED_NONZERO
  relations retained
  formation: new_formation_required
```

Expected DSD closure:

```text
RAW_ADMISSIBLE_CANDIDATES_DSD: {A1,A2,A3,A4}
CANONICAL_SYNTHESIS_ADMISSIBLE_FAMILY_DSD: {C0,C1}
C0 = {A1,A2}
C1 = {A3,A4}
TERMINAL_SYNTHESIS_STATUS_DSD: SYNTHESIS_ADMISSIBLE
SYNTHESIS_PROTOCOL_CONFORMANCE_DSD: CONFORMANT
```

`C0 != C1` at TARGET_RESOLUTION because middle-component identity and lifted whole-readiness class differ.

## 7. Frozen strongest-reasonable competent baseline

Baseline identity:

```text
B1_TYPED_COMPOSITION_GRAPH_CHECKER
```

B1 receives exactly the same:

```text
component identities and Formation-admitted flags
input/output interface records
component readiness status classes
formation_trigger records
R_SEGMENT_CHAIN
L_READY
F_FORM
composition mode per candidate
associativity and noncommutativity declarations
grouping syntax
candidate basis {A1-A8}
coverage declaration
TARGET_RESOLUTION
canonicalization rule
relation-retention requirement
formation-background requirement
staged failure-evaluation rule
```

B1 is explicitly competent to:

```text
1. preserve DEFINED_ZERO, DEFINED_NONZERO, APPLICABLE_BUT_UNDEFINED;
2. apply the explicit whole-property lift L_READY without collapsing status classes;
3. evaluate structural prerequisite H1-H2 before downstream H3-H5;
4. preserve every reached failed hard condition;
5. track exact retained adjacency-relation sets;
6. track same_background versus new_formation_required;
7. canonicalize left/right grouping under the supplied associativity rule only;
8. preserve material distinctions required by TARGET_RESOLUTION;
9. return both raw admissible candidates and canonical admissible classes;
10. remain fully retraceable from frozen records;
11. perform no Design, Transformation, Aggregation, Optimization, or dynamic-process inference.
```

Expected B1 result:

```text
A1 -> admissible / NONE / C0
A2 -> admissible / NONE / C0
A3 -> admissible / NONE / C1
A4 -> admissible / NONE / C1
A5 -> rejected / {H3}
A6 -> rejected / {H2}; H3-H5 NOT_REACHED
A7 -> rejected / {H4}
A8 -> rejected / {H5}

RAW_ADMISSIBLE_CANDIDATES_B1: {A1,A2,A3,A4}
CANONICAL_ADMISSIBLE_FAMILY_B1: {C0,C1}
```

## 8. Frozen gain criteria

```text
G1 STATUS_AND_PROPERTY_LIFT_GAIN
  established only if DSD preserves a claim-relevant component/whole Property status distinction that B1 loses.

G2 FAILURE_TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant reached failure or staging distinction that B1 loses.

G3 GROUPING_EQUIVALENCE_GAIN
  established only if DSD handles supplied associativity/canonicalization more correctly than B1 on the frozen task.

G4 RELATION_RETENTION_GAIN
  established only if DSD preserves a claim-relevant adjacency relation/loss distinction that B1 loses.

G5 FORMATION_EFFECT_GAIN
  established only if DSD preserves same-background versus new-formation-required separation that B1 loses.

G6 COMPOSITION_CLOSURE_GAIN
  established only if DSD returns a more correct raw/canonical admissible family without changing frozen inputs.

G7 RETRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant provenance/trace needed to reconstruct the verdict that B1 cannot reconstruct from the same frozen records.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> strongest-reasonable-baseline challenge fails.
If one or more G1-G7 are established -> GAIN_ESTABLISHED.
If DSD and B1 are both correct and B1 matches all frozen claim-relevant dimensions -> NO_GAIN.
Otherwise -> unresolved / challenge fail according to the frozen scoring record.
```

No efficiency, elegance, terminology, implementation cost, or practical-domain benefit is scored.
Extra DSD bookkeeping alone does not establish gain.

## 9. Precommitted scoring

Total required checks: **52**.

```text
A. precommit / source integrity: 8
  A1 Protocol commit fixed
  A2 B1 identity and capabilities fixed
  A3 candidates and coverage fixed
  A4 target resolution fixed
  A5 composition law/grouping/equivalence fixed
  A6 L_READY and F_FORM fixed
  A7 gain criteria G1-G7 fixed
  A8 no post-hoc weakening of baseline/task

B. DSD candidate checks: 16
  B1-B8 exact A1-A8 candidate verdict/failure-set results
  B9 A1/A2 canonicalize to C0
  B10 A3/A4 canonicalize to C1
  B11 C0 != C1 at target resolution
  B12 raw family exactly {A1,A2,A3,A4}
  B13 canonical family exactly {C0,C1}
  B14 terminal SYNTHESIS_ADMISSIBLE
  B15 conformance CONFORMANT
  B16 no neighboring-method or temporal-process claim absorbed

C. B1 baseline checks: 16
  C1-C8 exact A1-A8 verdict/failure-set results
  C9 A1/A2 canonicalize to C0
  C10 A3/A4 canonicalize to C1
  C11 C0 != C1 preserved
  C12 raw family exactly {A1,A2,A3,A4}
  C13 canonical family exactly {C0,C1}
  C14 property-lift/relation/formation records preserved
  C15 staged NOT_REACHED discipline preserved for A6
  C16 no neighboring-method or temporal-process operation

D. gain/comparison checks: 9
  D1-D7 G1-G7 each NOT_ESTABLISHED if B1 matches
  D8 final method gain = NO_GAIN when D1-D7 all hold
  D9 NO_GAIN is not interpreted as method failure

E. scope / category checks: 3
  E1 no DSD superiority or practical-efficiency claim
  E2 no external/reproducibility/independence/maturity claim
  E3 strongest-reasonable-baseline category, if passed, is limited to constructed-evidence level
```

Decision:

```text
52/52 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

## 10. Evidence-count lock

Before execution:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 5
SUCCESSFUL_POSITIVE_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_CASES: 1
SUCCESSFUL_BOUNDARY_CASES: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_CASES: 1
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
EXTERNAL_SYNTHESIS_APPLICATIONS: 0
```

A 52/52 PASS may add exactly:

```text
DIRECT_CONSTRUCTED_PILOT_INCREMENT: +1
SUCCESSFUL_BASELINE_COMPARISON_PASS_INCREMENT: +1
SUCCESSFUL_NO_GAIN_CASE_INCREMENT: +1 only if final gain is NO_GAIN
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

It does not establish external applicability, reproducibility, independent validation, practical superiority, or Synthesis method maturity.
