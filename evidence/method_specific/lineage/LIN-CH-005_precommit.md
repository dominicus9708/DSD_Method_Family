# LIN-CH-005 — Strongest-Reasonable Non-DSD Lineage Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-005`  
Method: **Lineage / DSD 계보론**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

```text
LINEAGE_PROTOCOL_VERSION:
  v0.1

LINEAGE_PROTOCOL_COMMIT:
  f69f364985d604d2c883b14b2efa18535a6bbf6e

LINEAGE_PROTOCOL_BLOB:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef

PREVIOUS_COMPETENT_BASELINE:
  LIN-CH-004
  B0_GENERIC_TYPED_SUCCESSION_EVALUATOR
  64/64 PASS / NO_GAIN
```

No DSD protocol revision is allowed in response to this baseline result.

## 2. Strong baseline identity

```text
BASELINE_ID:
  B1_STRONG_TEMPORAL_IDENTITY_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_identity_engine

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B1 is materially stronger than B0.

B1 may use ordinary:

```text
versioned identity-rule registries
typed temporal multigraphs
relation algebra and composition checks
direct-versus-derived edge provenance
typed prerequisite dependency closure
identity-bearing set versioning
branch/merge policy profiles
optional uniqueness/bijection/cardinality constraints
schema-alternative management
terminal precedence
deterministic evaluation ledgers
bounded-claim generation
full rerun manifests
```

B1 may not be weakened after precommit.

## 3. Strong baseline operation

B1 performs:

```text
B1-1 freeze task, rule-registry version, times, scope,
     object identities, query set, and output level

B1-2 bind every successor rule to an explicit version
     and applicability interval; prohibit retroactive rule use

B1-3 maintain a typed temporal multigraph of predecessor/successor
     relations with source/provenance per edge

B1-4 distinguish supplied direct edges from relation-algebra
     compositions and path-derived consequences

B1-5 verify self-time identity and required composition inclusion
     for coherent-family claims

B1-6 evaluate typed relation compatibility and inherited tags

B1-7 compute prerequisite dependency closure for multi-input
     successor claims; unavailable required prerequisites block
     dependent claims rather than becoming negative results

B1-8 freeze versioned identity-bearing sets before evaluating
     state or interval identity

B1-9 run two-sided identity-bearing coverage for every required pair

B1-10 preserve branch/merge relations and evaluate optional
      uniqueness, bijection, or cardinality profiles separately

B1-11 retain explicit negative, unsupported, ambiguous, conflicting,
      blocked, inapplicable, outside-scope, and unresolved-schema
      states separately

B1-12 apply frozen terminal precedence without erasing lower-level states

B1-13 retain trace/transformation/comparison/classification/
      aggregation/compression/reconstruction/audit records as sidecars
      unless the task supplies an explicit identity-authorizing rule

B1-14 emit deterministic relation/family/state/interval ledgers

B1-15 emit a bounded claim generator that prohibits unsupported
      equality, causality, authenticity, legal identity, uniqueness,
      bijection, cardinality conservation, and external-validity claims

B1-16 emit a rerun manifest containing all claim-relevant
      version/scope/rule/provenance identifiers
```

## 4. Frozen strong subcases

### R1 — versioned identity-rule semantics and non-retroactivity

Times:

```text
t0 < t1 < t2
```

Rule registry:

```text
ID-RULE-v1:
  valid on t0 -> t1
  stable registry member preserves channel identity

ID-RULE-v2:
  valid from t1 -> t2
  registry transition means stable-registry identity rule is not applicable;
  explicit successor relation required
```

Supplied transition relation:

```text
cA -> cA2
```

No rule may be applied retroactively.

Expected both systems:

```text
t0 -> t1:
  identity successor established through v1 rule

t1 -> t2:
  successor established only through explicit supplied relation

v2 not retroactively applied to t0 -> t1
v1 not improperly extended through transition
```

### R2 — branch/merge with stronger optional policy profiles

Base relation:

```text
a -> {b,c}
{d,e} -> f
```

Frozen optional profiles:

```text
PROFILE-U:
  UNIQUE_SUCCESSOR_REQUIREMENT = required

PROFILE-B:
  BIJECTION_REQUIREMENT = required

PROFILE-C:
  CARDINALITY_CONSERVATION_REQUIREMENT = required
```

Expected:

```text
base relation:
  preserved

branching:
  allowed by base relation

merging:
  allowed by base relation

PROFILE-U:
  unsatisfied

PROFILE-B:
  unsatisfied

PROFILE-C:
  unsatisfied where frozen set cardinalities differ

base relation is not erased by optional-profile failure
```

### R3 — dependency-aware multi-input successor claim

Primary component claim:

```text
p0 -> p1
```

Required inputs:

```text
sort a lineage:
  supplied and established

sort b lineage:
  depends on decoder DB-v3

decoder DB-v3:
  unavailable
```

Expected both systems:

```text
sort a:
  established

sort b prerequisite closure:
  blocked

p0 -> p1:
  blocked

dependent state-level obligation:
  blocked

no explicit negative inferred
```

### R4 — direct-long-interval relation versus composed relation

Relations:

```text
L_01:
  (a0,a1)

L_12:
  (a1,a2)

composition:
  {(a0,a2)}

direct L_02:
  {(a0,a2),(a0,b2)}
```

Expected both systems:

```text
composition inclusion:
  pass

family:
  coherent

direct L_02:
  retained as direct supplied record

extra direct pair (a0,b2):
  retained

direct relation not replaced by composition equality
```

### R5 — integrated conflict / underdetermination / sidecar pressure

Frozen required obligations:

```text
Q1:
  conflicting successor records
  no precedence

Q2:
  two admissible relation schemas
  different outcomes
  no resolver

Q3:
  established successor relation
  plus Tracking continuity sidecar
  plus Transformation map
  plus high Comparison similarity
  plus same Classification class
  plus equal Aggregate readout
  plus Reconstruction candidate
  plus Audit pass on source-record conformance
```

Frozen terminal precedence:

```text
OUTSIDE_SCOPE
> CONFLICT
> UNRESOLVED
> BLOCKED
> COMPLETE/PARTIAL/NOT_ESTABLISHED
```

Expected both systems:

```text
Q1:
  conflict

Q2:
  unresolved / underdetermined

Q3:
  successor established from the supplied successor relation only;
  sidecars do not become identity criteria

run terminal:
  conflict

lower-level Q2 and Q3 states remain visible
```

## 5. Equal-information and fairness rule

Lineage and B1 receive exactly the same claim-relevant records.

```text
EQUAL_INFORMATION_REQUIRED:
  yes

HIDDEN_FAVORABLE_INPUT_ALLOWED:
  no

BASELINE_WEAKENING_ALLOWED:
  no

POST_HOC_RULE_CHANGE_ALLOWED:
  no
```

## 6. Frozen gain axes

```text
G1 VERSIONED_IDENTITY_RULE_GAIN

G2 TEMPORAL_MULTIGRAPH_AND_BRANCH_MERGE_GAIN

G3 RELATION_ALGEBRA_COHERENCE_GAIN

G4 PREREQUISITE_DEPENDENCY_CLOSURE_GAIN

G5 UNRESOLVED_CONFLICT_AND_SIDECAR_BOUNDARY_GAIN

G6 BOUNDED_MAXIMUM_CLAIM_GAIN

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN
```

Allowed per-axis result:

```text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
```

Overall rule:

```text
if Lineage is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  and do not relabel it as DSD gain

otherwise:
  UNRESOLVED
```

## 7. Frozen scoring — 72 checks

### A. Immutable fairness — 10

```text
A1 Lineage protocol identity frozen
A2 B1 identity and capabilities frozen
A3 R1-R5 frozen before execution
A4 output mappings frozen
A5 equal information supplied
A6 Lineage hidden favorable inputs = 0
A7 B1 claim-relevant withheld inputs = 0
A8 B1 not weakened after precommit
A9 gain axes/scoring frozen
A10 external application/evaluator not counted
```

### B. R1 versioned identity rules — 12

```text
B1 Lineage t0->t1 identity established under v1
B2 B1 same result under v1
B3 Lineage t1->t2 requires explicit relation
B4 B1 same transition rule
B5 Lineage explicit relation establishes successor
B6 B1 explicit relation establishes successor
B7 Lineage no v2 retroactive use
B8 B1 no v2 retroactive use
B9 Lineage no v1 extension through transition
B10 B1 no v1 extension through transition
B11 Lineage rule/version provenance retained
B12 B1 rule/version provenance retained
```

### C. R2 branch/merge and optional profiles — 14

```text
C1 Lineage branch retained
C2 B1 branch retained
C3 Lineage merge retained
C4 B1 merge retained
C5 Lineage base relation established independently
C6 B1 base relation established independently
C7 Lineage unique-successor profile unsatisfied
C8 B1 unique-successor profile unsatisfied
C9 Lineage bijection profile unsatisfied
C10 B1 bijection profile unsatisfied
C11 Lineage cardinality profile unsatisfied where applicable
C12 B1 same cardinality result
C13 neither erases base relation
C14 neither treats branch/merge as protocol failure
```

### D. R3 prerequisite dependency closure — 12

```text
D1 Lineage sort-a lineage established
D2 B1 sort-a relation established
D3 Lineage sort-b requires DB-v3
D4 B1 same dependency recorded
D5 Lineage DB-v3 unavailable
D6 B1 same unavailable prerequisite
D7 Lineage dependent relation BLOCKED
D8 B1 dependent relation BLOCKED
D9 Lineage dependent state obligation BLOCKED
D10 B1 dependent state obligation BLOCKED
D11 neither infers explicit negative
D12 both preserve prerequisite provenance
```

### E. R4 relation-algebra coherence — 12

```text
E1 Lineage composition computed correctly
E2 B1 composition computed correctly
E3 Lineage composition inclusion passes
E4 B1 composition inclusion passes
E5 Lineage family coherent
E6 B1 family coherent
E7 Lineage direct L_02 retained
E8 B1 direct L_02 retained
E9 Lineage extra direct pair retained
E10 B1 extra direct pair retained
E11 Lineage no equality assumption composition=direct
E12 B1 no equality assumption composition=direct
```

### F. R5 integrated unresolved/sidecar pressure — 14

```text
F1 Lineage Q1 conflict
F2 B1 Q1 conflict
F3 Lineage Q2 underdetermined
F4 B1 Q2 unresolved
F5 Lineage Q3 successor established from successor relation
F6 B1 Q3 same
F7 Lineage Tracking sidecar not promoted
F8 B1 trace sidecar not promoted
F9 Lineage transform/comparison/class/aggregate/reconstruction/audit sidecars not promoted
F10 B1 same non-substitution
F11 Lineage terminal conflict by frozen precedence
F12 B1 terminal conflict by frozen precedence
F13 lower-level Q2/Q3 states retained by Lineage
F14 lower-level Q2/Q3 states retained by B1
```

### G. Comparative conclusion — 8

```text
G1 all seven gain axes scored from claim-relevant results
G2 versioned-rule axis follows frozen result
G3 graph/branch axis follows frozen result
G4 relation-algebra axis follows frozen result
G5 prerequisite-closure axis follows frozen result
G6 sidecar/unresolved axis follows frozen result
G7 final gain status follows frozen rule
G8 strongest-reasonable status limited to constructed-evidence level
   and NO_GAIN does not imply merger/deletion/absorption
```

```text
TOTAL_REQUIRED_CHECKS: 72
PASS_THRESHOLD: 72/72
PARTIAL_PASS_ALLOWED: no
```

## 8. Counter lock on 72/72 PASS

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_LINEAGE_PILOTS:
  4 -> 5

BASELINE_LINEAGE_CASES:
  1 -> 2

NO_GAIN_LINEAGE_CASES:
  1 -> 2
  only if all seven gain axes are BASELINE_MATCH

STRONGEST_REASONABLE_BASELINE_LINEAGE:
  established_at_constructed_evidence_level
  only if the frozen strong workload completes without unresolved
  comparator weakness
```

## 9. Interpretation lock

```text
STRONGEST_REASONABLE_BASELINE_ESTABLISHED_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
PROOF_OF_METHOD_REDUNDANCY

NO_GAIN
  !=
METHOD_FAILURE

NO_GAIN
  !=
METHOD_DELETION_PROOF

NO_GAIN
  !=
METHOD_MERGER_PROOF

NO_GAIN
  !=
PERMANENT_REDUNDANCY
```
