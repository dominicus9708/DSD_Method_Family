# MSR-CH-005 Precommit — Strongest-Reasonable Non-DSD Baseline Comparison

Status: **PROSPECTIVELY FROZEN / NOT YET EXECUTED**  
Date: **2026-09-19**  
Case ID: `MSR-CH-005`  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen DSD comparator

```text
MEASUREMENT_PROTOCOL_COMMIT:
  70af7c3ddc618be34d0ff76fcc1ce63c895fc950

MEASUREMENT_PROTOCOL_BLOB:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331

MEASUREMENT_PROTOCOL_VERSION:
  v0.1
```

No Measurement protocol revision is allowed in response to this baseline.

## 2. Strong baseline identity

```text
BASELINE_ID:
  B1_STRONG_DISTINGUISHABILITY_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_evaluator

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
```

B1 is intentionally allowed to be materially stronger than the competent B0 baseline.

## 3. Frozen B1 capabilities

B1 may:

```text
1 preserve explicit typed states such as defined-zero, missing, undefined,
  inapplicable, prerequisite-missing, and out-of-scope;

2 preserve candidate identity, version, domain, unit/representation,
  proxy/directness, bridge identity, and provenance;

3 apply supplied exact/tolerance/statistical decision rules
  without inventing missing calibration or thresholds;

4 build pairwise distinguishability tables from supplied outcome sets/classes;

5 enumerate declared candidate subsets and evaluate supplied joint-signature rules
  to locate sufficient plans;

6 preserve redundant-candidate findings without counting candidate number as gain;

7 preserve aggregate/compression collision, injectivity, support-retention,
  and reconstruction-limit sidecars;

8 preserve time, location, regime, schema-version, and supplied
  distinguishability-support availability;

9 preserve multiple simultaneously admissible bridge versions without
  choosing a preferred one post hoc;

10 distinguish plan-selection adequacy from an actually observed result,
   diagnosis, causality, or truth of an alternative;

11 emit a bounded maximum-supported-claim record;

12 retain enough intermediate decision records for deterministic retrace.
```

B1 may use ordinary decision tables, partitions, set overlap tests, graph/ledger records, tuple signatures, and exhaustive finite subset enumeration.

B1 may not be weakened after precommit.

## 4. Equal-information rule

For each subcase, DSD Measurement and B1 receive exactly the same claim-relevant:

```text
task identity/version
alternative identities
required distinctions
candidate identities
candidate scope/domain/version
typed value/status records
raw/symbolic outcome maps
bridge identity/provenance
decision thresholds/rules
joint policy
collision/injectivity/reconstruction sidecars
time/location/regime/version records
dynamic-support handoffs
proxy/directness records
observed-result availability
```

Extra B1 computational competence is allowed; extra hidden factual input is not.

## 5. Stronger frozen subcases

Five subcases are frozen.

```text
R1 version-scoped decision semantics with identical raw value
R2 dynamic distinguishability support: not-yet-arrived versus later available
R3 finite plan search with partial, redundant, blocked, and inapplicable candidates
R4 proxy + aggregate collision + bounded reconstruction claim
R5 simultaneously admissible bridge versions causing underdetermination
```

## 6. R1 — version-scoped decision semantics

Alternatives:

```text
A,B
required pair: A-B
```

Candidate `m_v` has the same raw values under two schema versions:

```text
raw(A)=0.6
raw(B)=0.4

schema V1:
  HIGH iff x >= 0.5
  LOW  iff x < 0.5

schema V2:
  HIGH iff x >= 0.7
  LOW  iff x < 0.7
```

Two frozen tasks:

```text
R1-t0 uses V1
R1-t1 uses V2
```

Expected:

```text
R1-t0:
  A -> HIGH
  B -> LOW
  pair -> discriminating
  plan -> sufficient

R1-t1:
  A -> LOW
  B -> LOW
  pair -> nondiscriminating
  plan -> insufficient
```

Required guard:

```text
SAME_RAW_VALUES != SAME_DECISION_SEMANTICS_ACROSS_VERSIONS
LATER_RULE != RETROACTIVE_RULE_FOR_EARLIER_TASK
```

## 7. R2 — dynamic distinguishability support

Alternatives:

```text
C,D
required pair: C-D
candidate: m_dyn
measurement location: L
```

A supplied dynamic-support handoff states:

```text
t0:
  structural difference exists upstream
  distinguishability support at L: NOT_YET_AVAILABLE

t1:
  distinguishability support at L: AVAILABLE
```

Supplied local outcome maps once available:

```text
C -> RED
D -> BLUE
```

Expected:

```text
t0:
  local candidate cannot use the upstream difference as present evidence
  plan must not emit a negative-result claim from non-arrival
  terminal -> MEASUREMENT_PLAN_BLOCKED
  reason -> required dynamic-support availability absent at declared time

t1:
  pair -> discriminating
  terminal -> MEASUREMENT_PLAN_SUFFICIENT
```

Required guard:

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
UPSTREAM_DIFFERENCE != PRESENT_LOCAL_READOUT
```

For B1 vocabulary, t0 may be recorded as `B1_PLAN_BLOCKED_BY_AVAILABILITY` and t1 as `B1_PLAN_SUFFICIENT`.

## 8. R3 — finite plan search under mixed candidate quality

Alternatives:

```text
E,F,G
required pairs:
  E-F
  E-G
  F-G
```

Candidates:

```text
m1:
  E -> 0
  F -> 1
  G -> 1
  -> separates E from F/G only

m2:
  E -> 0
  F -> 0
  G -> 1
  -> separates G from E/F only

m3:
  exact duplicate of m1
  -> redundant

m4:
  applicable, but required bridge absent
  -> blocked

m5:
  declared domain object-class Z
  supplied task object-class Y
  -> inapplicable
```

Joint policy:

```text
ordered tuple over defined usable members
```

Expected DSD/B1 conclusions:

```text
{m1,m2}:
  sufficient for all three pairs

{m1,m3}:
  insufficient for F-G because redundancy adds no distinction

m4:
  blocked

m5:
  inapplicable

minimal sufficient cardinality among supplied usable plans:
  2

at least one minimal sufficient plan:
  {m1,m2}
```

Important limitation:

DSD Measurement Protocol v0.1 does not claim optimization as its binding task. For scoring, DSD only needs to correctly evaluate the predeclared plan `{m1,m2}`, candidate statuses, and redundancy sidecar. B1's finite plan search is extra baseline competence and may not be counted as a DSD defect.

Required guards:

```text
MORE_CANDIDATES != MORE_INFORMATION
REDUNDANT_CANDIDATE != NEW_DISCRIMINATION
BASELINE_EXTRA_SEARCH_CAPABILITY != DSD_PROTOCOL_FAILURE
```

## 9. R4 — proxy, aggregate collision, and bounded reconstruction

Alternatives:

```text
H,I,J
required pairs:
  H-I
  H-J
  I-J
```

Direct candidate `m_direct`:

```text
H -> P
I -> Q
J -> Q
DIRECT_OR_PROXY: direct
```

Proxy aggregate candidate `m_proxy`:

```text
H support {+2,-2} -> aggregate 0
I support {0}     -> aggregate 0
J support {+3}    -> aggregate 3

DIRECT_OR_PROXY:
  proxy via aggregate handoff

aggregate sidecar:
  H/I collision at 0
  map noninjective over H/I/J
  full support reconstruction unavailable
```

Frozen plan:

```text
{m_direct,m_proxy}
```

Expected:

```text
m_direct:
  H-I discriminate
  H-J discriminate
  I-J nondiscriminate
  -> partial

m_proxy:
  H-I nondiscriminate
  H-J discriminate
  I-J discriminate
  -> partial

joint:
  H -> (P,0)
  I -> (Q,0)
  J -> (Q,3)
  -> sufficient
```

Maximum supported claim must remain:

```text
the frozen joint plan discriminates H/I/J under supplied semantics

not:
  proxy is direct observation
  equal aggregate means equal support
  full support reconstructed
  true alternative identified
```

Required guards:

```text
PROXY != DIRECT
EQUAL_AGGREGATE != EQUAL_SUPPORT
DISCRIMINATING_PROXY != FULL_RECONSTRUCTION
PLAN_SUFFICIENT != TRUE_ALTERNATIVE_IDENTIFIED
```

## 10. R5 — competing bridge versions / underdetermination

Alternatives:

```text
K,L
required pair: K-L
candidate: m_bridge
```

Two bridge versions are both fully supplied and both admissible under the frozen task.

```text
BRIDGE V1:
  K -> OPEN
  L -> CLOSED
  -> discriminating

BRIDGE V2:
  K -> OPEN
  L -> OPEN
  -> nondiscriminating

PRECEDENCE:
  none
```

Expected:

```text
DSD candidate -> MEASUREMENT_UNDERDETERMINED
DSD plan -> MEASUREMENT_PLAN_UNDERDETERMINED

B1 candidate -> B1_UNDERDETERMINED
B1 plan -> B1_PLAN_UNDERDETERMINED
```

Required guard:

```text
MULTIPLE_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
NO_PRECEDENCE != LICENSE_TO_CHOOSE_POST_HOC
```

## 11. Frozen gain axes

```text
G1 VERSION_SCOPE_GAIN
  DSD advantage only if it handles R1 version semantics more correctly than B1.

G2 DYNAMIC_AVAILABILITY_GAIN
  DSD advantage only if it preserves R2 non-arrival / later availability more correctly than B1.

G3 PLAN_AND_REDUNDANCY_GAIN
  DSD advantage only if its claim-relevant plan/candidate judgments are more correct than B1.
  B1's extra finite search ability alone is not a B1 gain against DSD.

G4 PROXY_LOSS_RECONSTRUCTION_GAIN
  DSD advantage only if it preserves proxy/directness, aggregate collision,
  noninjectivity, and reconstruction scope more correctly than B1.

G5 AMBIGUITY_GAIN
  DSD advantage only if it preserves R5 competing bridge semantics more correctly than B1.

G6 BOUNDED_CLAIM_GAIN
  DSD advantage only if it avoids truth/diagnosis/reconstruction overclaims
  that B1 makes from the same inputs.

G7 TRACEABILITY_GAIN
  DSD advantage only if a claim-relevant decision cannot be retraced from B1's frozen record
  while it can from DSD's record.
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
if DSD is nonconformant or wrong -> FAIL

if DSD is correct and one or more G1-G7 show DSD advantage
while B1 remains a fair strongest-reasonable comparator
-> GAIN_ESTABLISHED

if DSD and B1 are both correct and all G1-G7 are BASELINE_MATCH
-> NO_GAIN

otherwise
-> FAIL or UNRESOLVED according to frozen scoring
```

Terminology, formatting, elegance, implementation speed, pedagogy, and external practical benefit are not gain axes.

## 12. Frozen scoring — 64 checks

### A. Immutable fairness — 8

```text
A1 DSD protocol commit/blob frozen
A2 B1 identity/capabilities frozen
A3 R1-R5 frozen before execution
A4 same claim-relevant information supplied
A5 G1-G7 frozen
A6 scoring frozen
A7 B1 not weakened after precommit
A8 no external application or evaluator counted
```

### B. DSD execution — 18

```text
B1 R1-t0 sufficient
B2 R1-t1 insufficient
B3 R1 version semantics not collapsed
B4 R2-t0 non-arrival not negative evidence
B5 R2-t0 blocked by unavailable dynamic support
B6 R2-t1 sufficient
B7 R3 m1 partial
B8 R3 m2 partial
B9 R3 m3 redundancy preserved
B10 R3 m4 blocked
B11 R3 m5 inapplicable
B12 R3 {m1,m2} sufficient
B13 R4 direct/proxy roles preserved
B14 R4 H/I aggregate collision retained
B15 R4 full support reconstruction not claimed
B16 R4 joint plan sufficient
B17 R5 underdetermined
B18 all DSD subcase outputs bounded and conformant
```

### C. B1 execution — 18

```text
C1 R1-t0 sufficient
C2 R1-t1 insufficient
C3 R1 version semantics retained
C4 R2-t0 non-arrival not negative evidence
C5 R2-t0 blocked by unavailable support
C6 R2-t1 sufficient
C7 R3 m1 partial
C8 R3 m2 partial
C9 R3 m3 redundancy retained
C10 R3 m4 blocked
C11 R3 m5 inapplicable
C12 R3 finds/evaluates {m1,m2} sufficient
C13 R4 direct/proxy roles retained
C14 R4 H/I collision retained
C15 R4 full support reconstruction not claimed
C16 R4 joint plan sufficient
C17 R5 underdetermined
C18 B1 decision record sufficient for deterministic retrace
```

### D. Comparative gain — 10

```text
D1 G1 scored
D2 G2 scored
D3 G3 scored
D4 G4 scored
D5 G5 scored
D6 G6 scored
D7 G7 scored
D8 final gain follows frozen rule
D9 B1 extra finite-search competence not misclassified as DSD protocol failure
D10 NO_GAIN not interpreted as merger/deletion/absorption evidence
```

### E. Scope / protocol pressure — 10

```text
E1 protocol revision required only if contradiction appears
E2 shared core reopened only if shared-core contradiction appears
E3 strongest-reasonable-baseline status limited to constructed-evidence level
E4 no external applicability claim
E5 no reproducibility claim
E6 no independent validation claim
E7 no practical superiority claim
E8 no permanent method survival claim
E9 no permanent redundancy claim
E10 next step remains deterministic same-project retrace if passed
```

```text
TOTAL_REQUIRED_CHECKS: 64
PASS_THRESHOLD: 64/64
PARTIAL_PASS_ALLOWED: no
```

## 13. Evidence-count lock

Before execution:

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 4
POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 1
BASELINE_MEASUREMENT_CASES: 1
NO_GAIN_MEASUREMENT_CASES: 1
STRONGEST_REASONABLE_BASELINE_MEASUREMENT: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
```

A `64/64 PASS` with final `NO_GAIN` may add exactly:

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 4 -> 5
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 4 -> 5
BASELINE_MEASUREMENT_CASES: 1 -> 2
NO_GAIN_MEASUREMENT_CASES: 1 -> 2

STRONGEST_REASONABLE_BASELINE_MEASUREMENT:
  established_at_constructed_evidence_level
```

It does not increment reproducibility or external validation counters.

## 14. Next if passed

Proceed to deterministic same-project retrace from immutable Measurement protocol, precommit, and result artifacts.

A successful retrace remains same-project artifact consistency evidence, not independent replication.
