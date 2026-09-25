# LIN-CH-004 — Competent Non-DSD Lineage Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-004`  
Method: **Lineage / DSD 계보론**  
Case class: `competent_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
LINEAGE_PROTOCOL_VERSION:
  v0.1

LINEAGE_PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e

LINEAGE_PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef
```

No Lineage protocol revision is allowed in response to the baseline result.

## 2. Baseline identity

```text
BASELINE_ID:
  B0_GENERIC_TYPED_SUCCESSION_EVALUATOR

BASELINE_CLASS:
  competent_non_DSD_constructed_identity_relation_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B0 is intentionally competent rather than weak.

It may use ordinary:

```text
stable object IDs
typed directed relations
time-indexed relation families
explicit same-registry identity rules
type-compatibility rules
required auxiliary-relation dependencies
set-coverage checks
relation composition
branch/merge graphs
scope/schema locks
evidence/provenance records
deterministic status/terminal rules
```

It does not invoke Formation, Property, Static Aggregation, Dynamics, or the DSD shared core as theory.

Vocabulary differences alone do not count as DSD gain.

## 3. B0 generic operation

B0 performs:

```text
B0-1 freeze task ID/version, requested identity level, times,
     direction, scope, query set, and completion rule

B0-2 retain predecessor/successor object IDs, types,
     registry/background records, and human-readable labels separately

B0-3 if a supplied stable-registry rule explicitly states that
     unchanged registry members preserve identity over an interval,
     instantiate only that rule inside its declared interval

B0-4 outside that interval, evaluate only supplied typed
     directed successor relations

B0-5 retain relation source and provenance separately

B0-6 evaluate type compatibility and any explicitly required
     auxiliary relation prerequisites

B0-7 test same-time relations against identity when family
     coherence is required

B0-8 test shorter-interval composition as a subset of a supplied
     direct long-interval relation when family coherence is required

B0-9 preserve direct long-interval records separately from
     composed intermediate relations

B0-10 for state-level identity, freeze the supplied nonempty
      identity-bearing member set before evaluation

B0-11 require predecessor-to-successor and successor-to-predecessor
      coverage for state-level succession

B0-12 allow one-to-many and many-to-one successor relations
      unless uniqueness/bijection/cardinality is separately required

B0-13 retain explicit negative, evaluable unsupported,
      ambiguity, conflict, prerequisite blockage, not-applicable,
      outside-scope, and unresolved-semantics outcomes separately

B0-14 summarize multiple required obligations as COMPLETE /
      PARTIAL / NOT_ESTABLISHED / BLOCKED / CONFLICT /
      OUTSIDE_SCOPE / UNRESOLVED

B0-15 retain neighboring trace, transform, compare, classify,
      aggregate, compression, reconstruction, and audit records
      only as typed sidecars unless a supplied rule authorizes
      their use in the successor decision

B0-16 emit a bounded identity-relation result and do not infer
      literal equality, truth/authenticity, causality, legal identity,
      unique succession, bijection, cardinality conservation,
      external validity, or audit success
```

## 4. Frozen output mapping

Relation-level mapping:

```text
B0_SUCCESSOR_PRESENT
  <-> LINEAGE_SUCCESSOR_ESTABLISHED

B0_EXPLICIT_NO_SUCCESSOR
  <-> LINEAGE_SUCCESSOR_EXPLICITLY_NEGATED

B0_SUCCESSOR_NOT_SUPPORTED
  <-> LINEAGE_SUCCESSOR_NOT_ESTABLISHED

B0_AMBIGUOUS_TARGET
  <-> LINEAGE_SUCCESSOR_AMBIGUOUS

B0_CONFLICT
  <-> LINEAGE_SUCCESSOR_CONFLICTING

B0_PREREQUISITE_BLOCKED
  <-> LINEAGE_SUCCESSOR_BLOCKED

B0_NOT_APPLICABLE
  <-> LINEAGE_SUCCESSOR_INAPPLICABLE

B0_OUTSIDE_SCOPE
  <-> LINEAGE_SUCCESSOR_OUT_OF_SCOPE

B0_UNRESOLVED_SEMANTICS
  <-> LINEAGE_SUCCESSOR_UNDERDETERMINED
```

Family-level mapping:

```text
B0_FAMILY_COHERENT
  <-> LINEAGE_FAMILY_COHERENT

B0_FAMILY_INCOHERENT
  <-> LINEAGE_FAMILY_INCOHERENT

B0_FAMILY_BLOCKED
  <-> LINEAGE_FAMILY_BLOCKED

B0_FAMILY_CONFLICT
  <-> LINEAGE_FAMILY_CONFLICTING

B0_FAMILY_OUTSIDE_SCOPE
  <-> LINEAGE_FAMILY_OUT_OF_SCOPE

B0_FAMILY_UNRESOLVED
  <-> LINEAGE_FAMILY_UNDERDETERMINED
```

Task-level mapping:

```text
B0_TASK_COMPLETE
  <-> LINEAGE_TASK_ESTABLISHED

B0_TASK_PARTIAL
  <-> LINEAGE_TASK_PARTIAL

B0_TASK_NOT_ESTABLISHED
  <-> LINEAGE_TASK_NOT_ESTABLISHED

B0_TASK_BLOCKED
  <-> LINEAGE_TASK_BLOCKED

B0_TASK_CONFLICT
  <-> LINEAGE_TASK_CONFLICTING

B0_TASK_OUTSIDE_SCOPE
  <-> LINEAGE_TASK_OUT_OF_SCOPE

B0_TASK_UNRESOLVED
  <-> LINEAGE_TASK_UNDERDETERMINED
```

## 5. Equal-information rule

For every fixture, Lineage and B0 receive the same claim-relevant:

```text
task ID/version
claim level
time set and direction
bounded scope
required query/obligation set

predecessor/successor IDs
object types
registry/background identity records
human-readable labels

stable-registry identity rule and its applicability interval
formation/registry-transition record

channel/component successor relations
relation type/direction
relation provenance

identity-bearing family ID/version/provenance/selection rule
identity-bearing member sets by time

component types
inherited relation tags
required auxiliary relation sets
auxiliary relation availability

self-time relation records
intermediate relations
direct long-interval relations

optional uniqueness/bijection/cardinality requirements

neighboring-method sidecars
secondary diagnostic/readout sidecars

explicit negation
completeness/evaluable-absence information
ambiguity records
conflict records
scope records
schema alternatives
precedence or explicit absence of precedence
```

Neither side receives hidden favorable information.

## 6. Frozen fixtures

### Q1 — positive interval identity with a transition and branching

Use the claim-relevant fixture of LIN-CH-001.

Frozen structure:

```text
t0 < t1 < t2

t0,t1:
  stable registry/background B0
  channels {cA,cB}

t2:
  registry/background B1
  channels {cA2,cB2,cC2}

stable-registry identity rule:
  applies only t0 -> t1

explicit transition successor relation t1 -> t2:
  cA -> cA2
  cB -> cB2
  cB -> cC2

direct long-interval relation t0 -> t2:
  same corresponding pairs
```

Identity-bearing component family:

```text
I(t0) = {a0,b0}
I(t1) = {a1,b1}
I(t2) = {a2,b2,c2}
```

Expected Lineage:

```text
family coherent
state succession established for:
  (t0,t1)
  (t1,t2)
  (t0,t2)

interval identity established
task terminal = LINEAGE_TASK_ESTABLISHED
```

Expected B0:

```text
family coherent
two-sided member coverage passes for all required pairs
branching preserved
interval identity complete
task terminal = B0_TASK_COMPLETE
```

Neither side may infer unique successor, bijection, or cardinality conservation.

### Q2 — explicit negative, evaluable absence, ambiguity

Use LIN-CH-002 N1-N3 semantics as three independent required relation queries in one bounded fixture.

Expected Lineage statuses:

```text
EXPLICITLY_NEGATED
NOT_ESTABLISHED
AMBIGUOUS
```

Expected B0 statuses:

```text
EXPLICIT_NO_SUCCESSOR
SUCCESSOR_NOT_SUPPORTED
AMBIGUOUS_TARGET
```

Both must preserve:

```text
explicit negation != evaluable absence
evaluable absence != prerequisite blockage
shared display label != shared identity
```

### Q3 — blocked + inapplicable

Use LIN-CH-002 N5-N6 semantics.

Frozen records:

```text
one multi-input component successor query
requires auxiliary lineage/relation for input sort b
required auxiliary relation unavailable

one separate requested relation
does not apply to the declared object types
```

Expected:

```text
Lineage:
  BLOCKED
  INAPPLICABLE
  -> task terminal BLOCKED

B0:
  PREREQUISITE_BLOCKED
  NOT_APPLICABLE
  -> task terminal B0_TASK_BLOCKED
```

### Q4 — conflict + underdetermined semantics

Use LIN-CH-002 N4 and N8 semantics as independent subfixtures.

Q4A:

```text
one applicable record supports cA -> cB
one applicable record explicitly rejects cA -> cB
same frozen semantics
no precedence
```

Expected:

```text
Lineage:
  CONFLICTING
  -> LINEAGE_TASK_CONFLICTING

B0:
  CONFLICT
  -> B0_TASK_CONFLICT
```

Q4B:

```text
object identities unambiguous
two admissible relation-schema interpretations
one yields successor
one yields no successor
no resolver
```

Expected:

```text
Lineage:
  UNDERDETERMINED
  -> LINEAGE_TASK_UNDERDETERMINED

B0:
  UNRESOLVED_SEMANTICS
  -> B0_TASK_UNRESOLVED
```

### Q5 — out of scope + partial task

Q5A uses LIN-CH-002 N7 semantics.

Expected:

```text
Lineage:
  OUT_OF_SCOPE
  -> LINEAGE_TASK_OUT_OF_SCOPE

B0:
  OUTSIDE_SCOPE
  -> B0_TASK_OUTSIDE_SCOPE
```

Q5B uses LIN-CH-002 N9 semantics.

Two independent required obligations:

```text
Q1 successor established
Q2 evaluably not established
```

Expected:

```text
Lineage:
  LINEAGE_TASK_PARTIAL

B0:
  B0_TASK_PARTIAL
```

Neither may use PARTIAL to rescue one failed state-succession proposition.

### Q6 — evaluably incoherent family

Use LIN-CH-002 N10 semantics.

```text
L_01 = {(a0,a1)}
L_12 = {(a1,a2)}
L_02 = empty
```

Expected:

```text
Lineage:
  LINEAGE_FAMILY_INCOHERENT
  LINEAGE_TASK_NOT_ESTABLISHED

B0:
  B0_FAMILY_INCOHERENT
  B0_TASK_NOT_ESTABLISHED
```

Neither side may relabel evaluable incoherence as prerequisite blockage.

## 7. Frozen gain axes

```text
G1 identity / label / type-lock advantage

G2 stable-registry versus transition successor-rule advantage

G3 family coherence / self-time / composition /
   direct-long-interval discipline advantage

G4 identity-bearing coverage / branch-merge /
   optional uniqueness-bijection-cardinality discipline advantage

G5 negative / ambiguous / conflict / blocked / scope /
   underdetermination / terminal semantic advantage

G6 neighboring-record / reduced-readout / reconstruction /
   overclaim-boundary advantage
```

Allowed axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall gain rule:

```text
if all claim-relevant outputs and all six frozen gain axes match:
  LINEAGE_METHOD_GAIN_STATUS = LINEAGE_METHOD_GAIN_NO_GAIN

if one or more frozen claim-relevant axes establish a DSD advantage:
  LINEAGE_METHOD_GAIN_STATUS = LINEAGE_METHOD_GAIN_ESTABLISHED

if one or more frozen claim-relevant axes establish a baseline advantage:
  record BASELINE_ADVANTAGE on those axes
  and do not relabel it as DSD gain

otherwise:
  LINEAGE_METHOD_GAIN_STATUS = LINEAGE_METHOD_GAIN_UNDERDETERMINED
```

No terminology difference counts as gain.

## 8. Frozen scoring — 64 checks

### A. Fairness and immutability — 10

```text
A1 Lineage protocol commit/blob fixed
A2 B0 operation fixed before execution
A3 relation/family/task output mappings fixed
A4 Q1-Q6 fixed before execution
A5 equal-information rule respected
A6 B0 receives every Lineage-visible claim-relevant input
A7 Lineage receives no hidden favorable input
A8 no post-hoc gain axis added
A9 no baseline rule changed after result inspection
A10 external application remains no
```

### B. Q1 positive interval identity — 16

```text
B1 Lineage uses stable-registry identity only t0->t1
B2 B0 uses same supplied identity rule only t0->t1
B3 Lineage requires explicit transition relation t1->t2
B4 B0 requires same explicit successor relation t1->t2
B5 Lineage preserves branching
B6 B0 preserves branching
B7 Lineage family coherence passes
B8 B0 family coherence passes
B9 Lineage direct long-interval record preserved separately
B10 B0 direct long-interval record preserved separately
B11 Lineage two-sided state coverage passes all required pairs
B12 B0 two-sided state coverage passes all required pairs
B13 Lineage interval identity established
B14 B0 interval identity complete
B15 Lineage terminal ESTABLISHED
B16 B0 terminal COMPLETE
```

### C. Q2 explicit negative / absence / ambiguity — 10

```text
C1 Lineage explicit negation retained
C2 B0 explicit negative retained
C3 Lineage evaluable absence = NOT_ESTABLISHED
C4 B0 evaluable absence = SUCCESSOR_NOT_SUPPORTED
C5 neither converts evaluable absence to BLOCKED
C6 Lineage duplicate-label target = AMBIGUOUS
C7 B0 duplicate-label target = AMBIGUOUS_TARGET
C8 neither chooses one target post hoc
C9 explicit negation remains distinct from unsupported
C10 claim-relevant mapping matches
```

### D. Q3 blocked / inapplicable — 8

```text
D1 Lineage missing required auxiliary relation = BLOCKED
D2 B0 same prerequisite absence = PREREQUISITE_BLOCKED
D3 neither relabels blockage as evaluable absence
D4 Lineage type-mismatched relation = INAPPLICABLE
D5 B0 same relation = NOT_APPLICABLE
D6 neither relabels inapplicability as explicit negative
D7 Lineage task terminal BLOCKED
D8 B0 task terminal BLOCKED
```

### E. Q4 conflict / underdetermination — 8

```text
E1 Lineage preserves both conflicting records
E2 B0 preserves both conflicting records
E3 Lineage relation CONFLICTING
E4 B0 relation CONFLICT
E5 Lineage unresolved schemas = UNDERDETERMINED
E6 B0 unresolved schemas = UNRESOLVED_SEMANTICS
E7 neither chooses a schema post hoc
E8 corresponding task terminals match claim-relevantly
```

### F. Q5 scope / partial — 6

```text
F1 Lineage outside-scope relation preserved as OUT_OF_SCOPE
F2 B0 same request preserved as OUTSIDE_SCOPE
F3 corresponding outside-scope terminals match
F4 Lineage multi-obligation task = PARTIAL
F5 B0 multi-obligation task = PARTIAL
F6 neither uses PARTIAL to rescue one failed state-succession proposition
```

### G. Q6 incoherent family — 4

```text
G1 Lineage composition failure = FAMILY_INCOHERENT
G2 B0 composition failure = FAMILY_INCOHERENT
G3 neither relabels evaluable incoherence as BLOCKED
G4 both task terminals = NOT_ESTABLISHED
```

### H. Gain conclusion — 2

```text
H1 six gain axes scored from frozen claim-relevant outputs only
H2 NO_GAIN preserved if all six axes are BASELINE_MATCH,
   without merger/deletion/absorption conclusion
```

```text
TOTAL_REQUIRED_CHECKS: 64
PASS_THRESHOLD: 64/64
PARTIAL_PASS_ALLOWED: no
```

Any mismatch remains visible.

## 9. Allowed counter changes on 64/64 PASS

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED:
  3 -> 4

SUCCESSFUL_DIRECT_LINEAGE_PILOTS:
  3 -> 4

BASELINE_LINEAGE_CASES:
  0 -> 1

NO_GAIN_LINEAGE_CASES:
  0 -> 1
  only if all six gain axes are BASELINE_MATCH
```

No counter change may imply external validation.

## 10. Interpretation lock

A fair `NO_GAIN` result means only:

```text
no claim-relevant DSD performance advantage over this
competent constructed baseline was established for these
frozen tasks under equal-information access
```

It does not mean:

```text
Lineage protocol failure
Lineage method deletion
Lineage merge into Tracking or Dynamics
permanent redundancy
permanent method irreducibility failure
absence of organizational/theoretical value
```

Required guards:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
```
