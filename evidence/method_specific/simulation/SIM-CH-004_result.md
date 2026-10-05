# SIM-CH-004 — Competent Non-DSD Simulation Baseline Result

Status: **EXECUTED — 64/64 PASS / SIMULATION_NO_GAIN**  
Date: **2026-10-06**  
Challenge ID: `SIM-CH-004`  
Method: **Simulation / DSD 시뮬레이션론**  
Protocol: **Simulation Protocol v0.1**  
Baseline: **B0_GENERIC_TYPED_HYBRID_SIMULATOR**

## 1. Frozen references

~~~text
SIMULATION_PROTOCOL_COMMIT:
  ea271d04eb09d252299d9420d0fb1191564f5bc6

SIMULATION_PROTOCOL_BLOB:
  c3d6f80d99dabb5b84c7a60fd2df3f58bf9dba35

PRECOMMIT_COMMIT:
  7d85d57625f109ba2e1836c000d24b7b5a5fee16

PRECOMMIT_BLOB:
  066104319e65f5a5f420a494cf5857df9a6f7c47
~~~

No protocol rule, baseline capability, fixture, gain axis, scoring item, or pass threshold changed after precommit.

## 2. Fairness result

~~~text
BASELINE_ID:
  B0_GENERIC_TYPED_HYBRID_SIMULATOR

EQUAL_INFORMATION_ACCESS:
  yes

SIMULATION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0
~~~

B0 used ordinary typed hybrid-simulation machinery only.

## 3. Q1 — regular deterministic trajectory

Both evaluators received:

~~~text
x_0=1
x_(n+1)=x_n+2
n=0..3
~~~

Both generated:

~~~text
{1,3,5,7}
~~~

Both retained the same frozen horizon and established terminal.

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 4. Q2 — declared branching trajectory family

Both received:

~~~text
R(s0)={a,b}
R(a)={a2}
R(b)={b2}

TRAJECTORY_QUANTIFIER:
  ALL_DECLARED_BRANCHES_ON_SCOPE
~~~

Both generated:

~~~text
s0->a->a2
s0->b->b2
~~~

Both retained:

~~~text
BRANCH_COVERAGE:
  complete on declared scope

UNIQUENESS:
  not established

DECLARED_BRANCHING:
  not semantic underdetermination
~~~

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 5. Q3 — hybrid typed transition

Both retained:

~~~text
J1:
  Q_A/F_A
  regular evolution

transition:
  (A,1)->(B,10)

J2:
  Q_B/F_B
  regular evolution
~~~

Both preserved:

~~~text
support/formation-changing transition
post-transition initial-state admissibility
supplied lineage handoff
no lineage generation by Simulation
no cross-transition conservation claim
fixed-time static-slice validity
~~~

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 6. Q4 — readout collision without state collapse

Both generated distinct component trajectories:

~~~text
A_n=(1+n,2+n)
B_n=(2+n,1+n)
~~~

with the same readout history:

~~~text
O(A)=O(B)={3,5,7}
~~~

Both preserved:

~~~text
A_n != B_n

READOUT_EQUALITY:
  not state equality

READOUT_EQUALITY:
  not lineage identity
~~~

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 7. Q5 — numerical approximation and stochastic sample path

### Q5A numerical approximation

Both retained:

~~~text
dx/dt=x
x(0)=1
Euler h=0.1
x_num(0.1)=1.1

certified end-to-end error:
  <0.006

acceptance threshold:
  0.01
~~~

Both concluded:

~~~text
NUMERICAL_ACCEPTANCE:
  established on frozen horizon

EXACTNESS:
  not claimed
~~~

### Q5B stochastic sample path

Both retained:

~~~text
U={0.2,0.8,0.4}
X_0=0
X_(n+1)=1 if U_n<0.5 else 0
~~~

Both generated:

~~~text
{0,1,0,1}
~~~

Both preserved:

~~~text
STOCHASTIC_CLAIM_KIND:
  SAMPLE_PATH

DISTRIBUTIONAL_CLAIM:
  not made

EXACT_PROBABILITY_LAW:
  not inferred
~~~

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 8. Q6 — negative/status boundary bundle

Q6A:

~~~text
missing required evolution law
-> BLOCKED

zero dynamics invented:
  no
~~~

Q6B:

~~~text
incompatible applicable laws
no resolver
-> CONFLICTING

arbitrary law selection:
  no
~~~

Q6C:

~~~text
multiple admissible unresolved model semantics
no declared branching relation
no resolver
-> UNDERDETERMINED
~~~

Q6D:

~~~text
future external-world truth request
-> OUT_OF_SCOPE for Simulation
-> Prediction handoff retained
~~~

The four status classes remain distinct for both evaluators.

Claim-relevant result:

~~~text
BASELINE_MATCH
~~~

## 9. Gain-axis execution

~~~text
G1 trajectory-generation correctness:
  BASELINE_MATCH

G2 branch / hybrid-transition / lineage-handoff discipline:
  BASELINE_MATCH

G3 readout-information-loss / state-identity discipline:
  BASELINE_MATCH

G4 numerical / stochastic claim discipline:
  BASELINE_MATCH

G5 blocked / conflicting / underdetermined / out-of-scope discipline:
  BASELINE_MATCH

G6 claim-relevant Simulation outcome equivalence:
  BASELINE_MATCH
~~~

Overall:

~~~text
SIMULATION_METHOD_GAIN_STATUS:
  SIMULATION_NO_GAIN
~~~

This is a bounded constructed-baseline result.

## 10. Frozen-score execution

~~~text
A1-A10:
  10/10 PASS

B1-B8:
  8/8 PASS

C1-C10:
  10/10 PASS

D1-D10:
  10/10 PASS

E1-E12:
  12/12 PASS

F1-F10:
  10/10 PASS

G1-G4:
  4/4 PASS

TOTAL_REQUIRED_CHECKS:
  64

PASSED:
  64

FAILED:
  0
~~~

## 11. Post-challenge state

~~~text
DIRECT_SIMULATION_PILOTS_ATTEMPTED:
  4

SUCCESSFUL_DIRECT_SIMULATION_PILOTS:
  4

POSITIVE_SIMULATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_SIMULATION_CASES:
  1

METHOD_BOUNDARY_SIMULATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  12

BASELINE_SIMULATION_CASES:
  1

NO_GAIN_SIMULATION_CASES:
  1

REPRODUCIBILITY_CASES:
  0

EXTERNAL_SIMULATION_APPLICATIONS:
  0

INDEPENDENT_SIMULATION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

SIMULATION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_SIMULATION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 12. Interpretation lock

The result means only:

~~~text
No claim-relevant DSD Simulation advantage over
B0_GENERIC_TYPED_HYBRID_SIMULATOR was established
for the frozen constructed tasks under equal-information access.
~~~

It does not mean:

~~~text
Simulation Protocol failure
Simulation method deletion
Simulation merger into Computation
Simulation merger into the Dynamics source layer
Simulation merger into Prediction / Control / Operation
permanent redundancy
future DSD gain is impossible
~~~

Required guards:

~~~text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 13. Maximum-supported claim

Supported:

~~~text
At the competent constructed-baseline level and under equal
claim-relevant information, a generic typed hybrid simulator
reproduced the frozen Simulation outcomes for deterministic,
branching, hybrid-transition, lossy-readout, numerical,
stochastic-sample, and negative-status cases.

No DSD-specific Simulation gain was established on the six
frozen gain axes.
~~~

Not established:

~~~text
strongest-reasonable baseline equivalence
universal baseline equivalence
external applicability
independent validation
independent replication
method redundancy
method superiority
~~~

## 14. Next

Prospectively precommit and execute a strongest-reasonable non-DSD Simulation baseline challenge.
