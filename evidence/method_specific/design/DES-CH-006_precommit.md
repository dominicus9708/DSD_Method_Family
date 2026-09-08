# DES-CH-006 — Broader Typed Baseline Comparison Precommit

Status: **PRECOMMITTED BEFORE EVALUATION**  
Date: **2026-09-08**  
Evidence scope: `method_specific`  
Method directly tested: **DSD Design / DSD 설계론**  
Method protocol: **DSD Design Protocol v0.1**  
Case class: **baseline_comparison**

## 1. Purpose / 목적

Run a broader strongest-reasonable-baseline comparison than `DES-CH-005`.

The task combines Formation-level admission with General-Property status distinctions across a larger exhaustive candidate family.
A competent non-DSD typed decision table is given the same candidate data, the same target resolution, and an explicit status vocabulary capable of preserving the relevant distinctions.

The comparison is allowed to end in `GAIN_ESTABLISHED`, `NO_GAIN`, or a failed/undetermined comparison according to the frozen gain criteria.
Additional DSD terminology or bookkeeping alone is not gain.

---

## 2. Frozen Design task / 동결 설계 과업

```text
CASE_ID: DES-CH-006
DESIGN_TASK_ID: DES-TASK-006
PROTOCOL_VERSION: v0.1
CASE_CLASS: baseline_comparison
CASE_ORIGIN: constructed_same_session
TASK_SCOPE: mixed Formation + General-Property typed admissibility design space
CANDIDATE_COVERAGE: exhaustive relative to DES-TASK-006
TARGET_DSD_LAYER_SCOPE:
  Formation
  General Property
DOMAIN_BRIDGE: not_used
EXTERNAL_STANDARD: not_used
AUXILIARY_METHODS_OR_HANDOFFS: not_used
SOFT_PREFERENCES: not_used
```

Two output-level subcases use the same frozen candidate universe:

```text
Case S:
  CLAIMED_OUTPUT_LEVEL: DESIGN_SPACE

Case U:
  CLAIMED_OUTPUT_LEVEL: UNIQUE_TARGET
```

Goal for Case S:

```text
return the complete admissible family within the frozen exhaustive universe
```

Goal for Case U:

```text
determine whether one materially unique target follows from the same hard constraints
without Optimization or arbitrary tie-breaking
```

---

## 3. Frozen hard constraints / 동결 하드 제약

```text
H1 q_primary is ADMITTED
H2 q_reserve is ADMITTED
H3 readiness(q_reserve) is DEFINED_ZERO or DEFINED_NONZERO
H4 authorization(q_primary) is DEFINED_NONZERO
```

Interpretation lock:

```text
DEFINED_ZERO satisfies H3.
DEFINED_ZERO does not satisfy H4.

APPLICABLE_BUT_UNDEFINED
PREREQUISITE_UNSATISFIED
INAPPLICABLE
PROFILE_UNAVAILABLE
UNDECLARED

are not coerced into a defined value.
```

The constraint source is the synthetic fixture frozen in this precommit.

---

## 4. Frozen target resolution / 동결 목표 해상도

```text
TARGET_RESOLUTION:
  exact admission state of q_primary
  exact admission state of q_reserve
  exact General-Property status/value class of readiness(q_reserve)
  exact General-Property status/value class of authorization(q_primary)
```

Material target distinctness is judged at this resolution.
Therefore A1 and A2 are distinct because `readiness` is `DEFINED_ZERO` in A1 and `DEFINED_NONZERO` in A2.

---

## 5. Frozen candidate family / 동결 후보군

```text
A1:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = DEFINED_NONZERO

A2:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_NONZERO
  authorization = DEFINED_NONZERO

A3:
  q_primary = ADMITTED
  q_reserve = CHANNEL_ABSENCE
  readiness = INAPPLICABLE
  authorization = DEFINED_NONZERO

A4:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = APPLICABLE_BUT_UNDEFINED
  authorization = DEFINED_NONZERO

A5:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = PREREQUISITE_UNSATISFIED
  authorization = DEFINED_NONZERO

A6:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = INAPPLICABLE
  authorization = DEFINED_NONZERO

A7:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = DEFINED_ZERO

A8:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_NONZERO
  authorization = APPLICABLE_BUT_UNDEFINED

A9:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_NONZERO
  authorization = PREREQUISITE_UNSATISFIED

A10:
  q_primary = CHANNEL_ABSENCE
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = INAPPLICABLE

A11:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = INAPPLICABLE

A12:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = PROFILE_UNAVAILABLE

A13:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = DEFINED_ZERO
  authorization = UNDECLARED

A14:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = PROFILE_UNAVAILABLE
  authorization = DEFINED_NONZERO

A15:
  q_primary = ADMITTED
  q_reserve = ADMITTED
  readiness = UNDECLARED
  authorization = DEFINED_NONZERO
```

No candidate may be added, removed, edited, or reinterpreted after this precommit.

Expected hard-constraint failure sets are frozen as:

```text
A1  -> none
A2  -> none
A3  -> {H2,H3}
A4  -> {H3}
A5  -> {H3}
A6  -> {H3}
A7  -> {H4}
A8  -> {H4}
A9  -> {H4}
A10 -> {H1,H4}
A11 -> {H4}
A12 -> {H4}
A13 -> {H4}
A14 -> {H3}
A15 -> {H3}
```

---

## 6. Frozen strongest reasonable baseline / 동결 강한 기준선

Baseline ID:

```text
B1_TYPED_ADMISSIBILITY_TABLE
```

B1 is a competent non-DSD typed rule-table procedure.
It is intentionally not a Boolean-only strawman.

B1 receives the same four claim-relevant fields for every candidate and uses separate structural and property-status columns.

Baseline structural state vocabulary:

```text
PRESENT
ABSENT
```

Baseline property-state vocabulary:

```text
PROPERTY_UNDECLARED
PROFILE_UNAVAILABLE
NOT_APPLICABLE
PREREQUISITE_NOT_MET
APPLICABLE_UNSET
DEFINED_ZERO
DEFINED_NONZERO
```

Frozen correspondence used only to present the same task data to the baseline:

```text
DSD CHANNEL_ABSENCE              -> B1 ABSENT
DSD ADMITTED                     -> B1 PRESENT
DSD UNDECLARED                   -> B1 PROPERTY_UNDECLARED
DSD PROFILE_UNAVAILABLE          -> B1 PROFILE_UNAVAILABLE
DSD INAPPLICABLE                 -> B1 NOT_APPLICABLE
DSD PREREQUISITE_UNSATISFIED     -> B1 PREREQUISITE_NOT_MET
DSD APPLICABLE_BUT_UNDEFINED     -> B1 APPLICABLE_UNSET
DSD DEFINED_ZERO                 -> B1 DEFINED_ZERO
DSD DEFINED_NONZERO              -> B1 DEFINED_NONZERO
```

B1 procedure:

1. read exactly A1-A15;
2. preserve all four target-resolution fields without Boolean collapse;
3. evaluate H1-H4 independently for every candidate;
4. record the full failed-hard-constraint set, not merely a first failure;
5. return every candidate with an empty failure set for Case S;
6. for Case U, determine whether exactly one materially distinct admissible target remains at the same target resolution;
7. if more than one distinct admissible target remains, report `NOT_UNIQUE_AT_DECLARED_RESOLUTION`;
8. make no preference, Optimization, or arbitrary tie-break selection;
9. preserve enough table data to retrace every candidate verdict.

Why B1 is frozen as strongest reasonable for this constructed task:

```text
- it has identical candidate coverage;
- it has identical hard constraints;
- it has the same target resolution;
- it explicitly preserves the relevant typed non-success states;
- it keeps structural absence separate from property-state failure;
- it records full rejection sets;
- it has an explicit no-unique-target outcome;
- it has no hidden information unavailable to DSD.
```

B1 is therefore permitted to match or outperform DSD.
The challenge does not assume DSD gain.

---

## 7. Frozen expected baseline results / 동결 기준선 예상 결과

Case S:

```text
B1_ADMISSIBLE_FAMILY: {A1,A2}
B1_REJECTED: {A3-A15}
```

with the exact frozen failure sets from Section 5.

Case U:

```text
B1_UNIQUE_TARGET_RESULT:
  NOT_UNIQUE_AT_DECLARED_RESOLUTION

reason:
  A1 and A2 are both admissible and materially distinct because readiness differs
```

B1 must not use a value preference between `DEFINED_ZERO` and `DEFINED_NONZERO`.

---

## 8. Frozen expected DSD results / 동결 DSD 예상 결과

Case S:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {A1,A2}
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

Case U:

```text
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY: {A1,A2}
TERMINAL_DESIGN_STATUS: DESIGN_UNDERDETERMINED
TERMINAL_STATUS_BASIS:
  UNIQUE_TARGET requested while A1 and A2 remain materially distinct and admissible
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
```

Both subcases must preserve the exact status/value distinctions and full failure sets.

---

## 9. Frozen gain criteria / 동결 이득 기준

Gain is adjudicated only after both B1 and DSD are executed.

```text
G1 STATUS_DISTINCTION_GAIN
  established only if DSD preserves a claim-relevant status distinction
  that B1 loses or coerces at the same resolution.

G2 REJECTION_TRACEABILITY_GAIN
  established only if DSD provides a correct claim-relevant failure set
  that B1 cannot reproduce from the same frozen inputs.

G3 STRUCTURE_PROPERTY_SEPARATION_GAIN
  established only if B1 conflates structural absence with a property-state result
  in a way that changes or obscures a claim-relevant verdict while DSD does not.

G4 OUTPUT_LEVEL_CLOSURE_GAIN
  established only if B1 makes an unsupported unique-target or other stronger closure
  that DSD correctly avoids.

G5 RETRACEABILITY_GAIN
  established only if a claim-relevant result is reproducibly retraceable under DSD
  but not under the frozen B1 record.
```

Gain decision:

```text
if DSD result is incorrect or nonconformant:
  no DSD gain is established by this case

else if one or more of G1-G5 is established:
  DESIGN_METHOD_GAIN_STATUS = GAIN_ESTABLISHED

else if B1 and DSD are both correct and B1 matches every frozen gain dimension:
  DESIGN_METHOD_GAIN_STATUS = NO_GAIN

else:
  comparison is UNDETERMINED or FAIL according to the missing frozen condition
```

No efficiency, concision, readability, or domain usefulness claim is scored because none is measured here.

---

## 10. Precommitted required checks / 사전 고정 검사

### Baseline B1 checks

1. B1 evaluates exactly A1-A15.
2. B1 preserves separate structural and property-status columns.
3. B1 does not Boolean-collapse the seven property-status classes.
4. B1 marks A1 admissible.
5. B1 marks A2 admissible.
6. B1 records A3 failure set exactly {H2,H3}.
7. B1 records A4 failure set exactly {H3}.
8. B1 records A5 failure set exactly {H3}.
9. B1 records A6 failure set exactly {H3}.
10. B1 records A7 failure set exactly {H4}.
11. B1 records A8 failure set exactly {H4}.
12. B1 records A9 failure set exactly {H4}.
13. B1 records A10 failure set exactly {H1,H4}.
14. B1 records A11 failure set exactly {H4}.
15. B1 records A12 failure set exactly {H4}.
16. B1 records A13 failure set exactly {H4}.
17. B1 records A14 failure set exactly {H3}.
18. B1 records A15 failure set exactly {H3}.
19. B1 Case-S family is exactly {A1,A2}.
20. B1 preserves A1 != A2 at TARGET_RESOLUTION.
21. B1 Case-U result is NOT_UNIQUE_AT_DECLARED_RESOLUTION.
22. B1 uses no Optimization, preference, or arbitrary tie-break.
23. B1 result is retraceable from the frozen table.

### DSD checks

24. DSD evaluates exactly A1-A15.
25. DSD preserves Formation admission separately from Property status.
26. DSD preserves all claim-relevant Property status distinctions.
27. DSD marks A1 admissible.
28. DSD marks A2 admissible.
29. DSD records A3 failure set exactly {H2,H3}.
30. DSD records A4-A6 failure set exactly {H3} each.
31. DSD records A7-A9 failure set exactly {H4} each.
32. DSD records A10 failure set exactly {H1,H4}.
33. DSD records A11-A13 failure set exactly {H4} each.
34. DSD records A14-A15 failure set exactly {H3} each.
35. DSD Case-S family is exactly {A1,A2}.
36. DSD Case-S terminal status is DESIGN_ADMISSIBLE.
37. DSD Case-S conformance is CONFORMANT.
38. DSD preserves A1 != A2 at TARGET_RESOLUTION.
39. DSD Case-U terminal status is DESIGN_UNDERDETERMINED.
40. DSD Case-U conformance is CONFORMANT.
41. DSD uses no hidden Optimization or arbitrary tie-break.
42. DSD result is retraceable from the frozen record.

### Gain-comparison checks

43. B1 and DSD return the same Case-S admissible family.
44. B1 and DSD preserve the same A1/A2 material distinctness.
45. B1 and DSD reproduce the same candidate failure sets.
46. B1 non-unique result and DSD underdetermined result agree on the claim-relevant Case-U closure.
47. G1 is adjudicated from observed comparison, not assumed.
48. G2 is adjudicated from observed comparison, not assumed.
49. G3 is adjudicated from observed comparison, not assumed.
50. G4 is adjudicated from observed comparison, not assumed.
51. G5 is adjudicated from observed comparison, not assumed.
52. Extra DSD bookkeeping is not counted as gain by itself.
53. DESIGN_METHOD_GAIN_STATUS follows the frozen gain decision rule.
54. Design outcome, conformance, and gain remain separate ledgers.

```text
PRECOMMITTED_REQUIRED_CHECKS: 54
```

Any failed check remains failed in the executed record.
No post-hoc baseline weakening or gain-criterion rewriting is permitted.

---

## 11. Evidence-count rule / 증거 수 규칙

Once executed after this precommit, `DES-CH-006` counts as one direct constructed Design pilot regardless of outcome.

If the comparison is validly completed, it may fill the `baseline_comparison` evidence category for Design at the constructed-evidence level.
It does not establish independent evaluator agreement or external-domain applicability.

---

## 12. Frozen limitations / 동결 한계

This comparison remains:

```text
constructed
same-session
same-project
non-external
non-independent
```

It is broader than `DES-CH-005` because it activates Formation + General Property, uses 15 candidates, preserves multiple property failure states, records multi-constraint failure sets, and tests both DESIGN_SPACE and UNIQUE_TARGET closure.

It does not measure runtime, cognitive cost, usability, external design quality, engineering performance, or independent reviewer agreement.
