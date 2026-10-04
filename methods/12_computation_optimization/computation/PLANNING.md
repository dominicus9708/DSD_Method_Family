# DSD Computation — Planning / Validation Roadmap

Status: **VALIDATION IN PROGRESS — COMP-CH-002 80/80 PASS / DIRECT METHOD-BOUNDARY CHALLENGE NEXT**  
Date: **2026-10-03**  
Method: **Computation / DSD 계산론**  
Legacy path ID: `12A`  
Higher field: **VII. Computation & Selection / 계산·선택**

## 1. Canonical basis

~~~text
SOURCE_REGISTRY_COMMIT:
  af9951011d999aef3c29a2beba6093983c1546f6

SOURCE_REGISTRY_BLOB:
  6f5ad5731ee82fc9a6561a39ff6d66fc4bd82461

SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

DEDICATED_COMPUTATION_PROTOCOL:
  established v0.1

PROTOCOL_COMMIT:
  03b1b7463af6d3a34dc3693a19933e83a3917b4d

PROTOCOL_BLOB:
  4c4fe0b0616371b7df6aff9ce6a1ff7636c49da4

VALIDITY_GATES:
  G1-G18

BINDING_OPERATION:
  T1-T18
~~~

The source registry separates predecessor/source constraints from prospective Computation method construction.

No source-derived constraint is to be silently upgraded into a Computation theorem.

## 2. Current working task

Not yet frozen:

~~~text
Given:
  a declared computational target,
  frozen source/model/interface versions,
  evaluation units / branches / channels,
  typed status and dependency records,
  explicit cross-layer bridges,
  resolution / distinguishability requirements,
  and any dynamic regime / locality assumptions,

determine:
  required evaluations,
  soundly omittable evaluations,
  reusable computations under a declared validity scope,
  blocked / unresolved dependencies,
  sufficient resolution for the declared target,
  and the soundness obligations attached to omission or reuse.
~~~

The target is a sound evaluation plan, not automatically a globally minimal-cost plan.

## 3. Canonical internal-build sequence

~~~text
1. ✅ Reconstruction -> Computation active-front handoff
2. ✅ Computation source / registry recovery
3. ✅ source-derived constraints separated from prospective method construction
4. ✅ Computation planning / worklog lane
5. ✅ Computation Task Interface v0.1 draft
6. ⏸ serious pre-protocol boundary attack
7. ⏸ Task Interface Boundary Amendment 001 if required
8. ⏸ executable Computation Protocol v0.1
9. ⏸ positive constructed challenge
10. ⏸ negative / blocked / conflicting / underdetermined / out-of-scope coverage
11. ⏸ direct neighboring-method boundary challenge
12. ⏸ competent non-DSD baseline
13. ⏸ strongest-reasonable non-DSD baseline
14. ⏸ deterministic same-project retrace
15. ⏸ frozen-axis internal-standardization audit
16. ⏸ external applications / independent validation later
~~~

A protocol may not be frozen before boundary attack and any required prospective amendment.

## 4. Initial boundary pressure

The Task Interface must be attacked against at least the following pressures:

~~~text
B01
  channel absent vs admitted zero-contribution channel

B02
  inapplicable property vs applicable-but-undefined vs defined zero

B03
  one failed branch vs whole branch-family elimination

B04
  same aggregate output vs distinct source support

B05
  same reduced readout vs different component-resolved state

B06
  common label / syntactic shape vs valid reusable subcomputation

B07
  reuse across version change or dynamic transition

B08
  static dependency graph vs dynamic causal / propagation dependency

B09
  finite-propagation specialization available vs unavailable

B10
  resolution reduction with and without target-preserving error bound

B11
  finite family vs countable family without convergence assumptions

B12
  required dependency unavailable vs dependency irrelevant

B13
  symbolic evaluation of intensional / infinite branch class

B14
  sound pruning with zero runtime gain

B15
  apparent speedup caused by changed target / information access

B16
  Computation result vs Optimization choice

B17
  Computation plan vs Simulation execution

B18
  computation soundness audit vs Audit-method substitution
~~~

This list is a planning target, not yet an executed boundary-attack artifact.

## 5. Neighboring-method boundary priorities

Highest-priority direct comparisons:

~~~text
Optimization
Aggregation
Compression
Analysis
Measurement
Simulation
Prediction
Transformation
Audit
Tracking
Lineage
~~~

The five-axis duplicate test remains:

~~~text
INPUTS
OPERATION
OUTPUTS
FAILURE_OR_NO_GAIN_CRITERIA
VALIDATION_STANDARD
~~~

No method merger or deletion claim is permitted from one boundary fixture.

## 6. Prospective challenge plan

After protocol freeze:

~~~text
COMP-CH-001
  positive constructed evaluation / pruning / reuse pack

COMP-CH-002
  negative / blocked / conflicting / underdetermined /
  out-of-scope / partial terminal coverage

COMP-CH-003
  direct neighboring-method boundary challenge

COMP-CH-004
  competent non-DSD dependency / execution-planning baseline

COMP-CH-005
  strongest-reasonable non-DSD computation-planning baseline

COMP-CH-006
  deterministic same-project retrace

COMP-AUD-001
  frozen-axis internal-standardization audit
~~~

Names are planning identifiers only until each precommit is created.

## 7. Expected failure / NO_GAIN discipline

~~~text
SOUND_PLAN_WITH_NO_SPEEDUP
  may be VALID_IN_DOMAIN and NO_GAIN

UNSOUND_PRUNING
  is a method failure for the declared target

MISSING_REQUIRED_INTERFACE
  must not be converted into branch irrelevance

OUT_OF_SCOPE_TARGET
  must not be converted into false / failed computation

NO_GAIN
  !=
METHOD_FAILURE

NO_GAIN
  !=
METHOD_DELETION_PROOF
~~~

Complexity, runtime, memory, energy, and evaluation-count gains require separate evidence.

## 8. Current evidence state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

PLANNING_LANE:
  established

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

PRESERVED_NO_REFINEMENT:
  11

PRESERVED_WITH_NONBREAKING_REFINEMENT:
  7

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_REQUIRED:
  7

REFINEMENT_GROUPS_ADOPTED:
  7/7

AMENDMENT_COMMIT:
  a5dacd3e80544d4a5058c1497cb2062124717c72

AMENDMENT_BLOB:
  1490548c203f70db5054007a27456e2073f1a7da

PROTOCOL_FREEZE_AUTHORIZED:
  yes

DEDICATED_COMPUTATION_PROTOCOL:
  not established

DIRECT_COMPUTATION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_COMPUTATION_PILOTS:
  2

METHOD_BOUNDARY_COMPUTATION_CASES:
  0

BASELINE_COMPUTATION_CASES:
  0

NO_GAIN_COMPUTATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPUTATION_APPLICATIONS:
  0

INDEPENDENT_COMPUTATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

COMPUTATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPUTATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Next

Prospectively precommit and execute COMP-CH-003, the direct neighboring-method boundary challenge.

COMP-CH-001 and COMP-CH-002 remain immutable evidence.
