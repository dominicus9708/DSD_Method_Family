# RECON-CH-005 — Strongest-Reasonable Non-DSD Reconstruction Baseline Result

Status: **EXECUTED — 82/82 PASS / NO_GAIN**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-005`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Baseline: **B1_STRONG_INVERSE_RECONSTRUCTION_ENGINE**

## 1. Frozen references

~~~text
RECONSTRUCTION_PROTOCOL_COMMIT:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad

RECONSTRUCTION_PROTOCOL_BLOB:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e

PRECOMMIT_COMMIT:
  c8fa76c3c7764a77c9c3f01a49edae7b93dcf005

PRECOMMIT_BLOB:
  a134bab5a6d1da5f556cb2783166defefd5e6b82
~~~

No Reconstruction Protocol rule, B1 capability, strong subcase, gain axis, scoring item, or pass threshold was changed after precommit.

## 2. Final result

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0

EQUAL_INFORMATION_ACCESS:
  yes

RECONSTRUCTION_HIDDEN_ADVANTAGE_INPUTS:
  0

BASELINE_WITHHELD_CLAIM_RELEVANT_INPUTS:
  0

BASELINE_WEAKENED_AFTER_PRECOMMIT:
  no

RECONSTRUCTION_METHOD_GAIN_STATUS:
  RECONSTRUCTION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
  established_at_constructed_evidence_level

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The materially stronger non-DSD B1 engine matched every claim-relevant Reconstruction result on the frozen strong workload.

The strongest-reasonable label is bounded to this constructed comparator class and workload.

## 3. Equal-information verification

Reconstruction and B1 received the same:

~~~text
task/version/primary claim/target identity
source/history class versions
class representation/evaluation/completeness records

evidence-registry versions
typed status/provenance/time/regime records
evidence-set coherence inputs

bridge-registry versions/scopes/directions
pair relations

required-interface dependencies
support/status/provenance/relational sidecars

forward maps
collision/fiber/kernel/injectivity records
interface-closure records
recoverability claim scope

history relations and composition rules
probabilistic priors/likelihoods/posterior semantics when supplied

terminal precedence
neighboring/source-layer sidecars
maximum-supported claim
~~~

No hidden favorable input was supplied to Reconstruction.

No claim-relevant input was withheld from B1.

## 4. R1 — versioned registries and non-retroactivity

Frozen TASK-v1 used:

~~~text
CLASS-v1:
  {h1,h2,h3}

EVIDENCE-v1:
  y=0
  status=DEFINED_ZERO
  support=S1

BRIDGE-v1:
  h1 -> y=0 / DEFINED_ZERO / S1
  h2 -> y=0 / DEFINED_ZERO / S1
  h3 -> y=0 / APPLICABLE_BUT_UNDEFINED / S2
~~~

Reconstruction:

~~~text
compatible:
  {h1,h2}

excluded:
  {h3}

set outcome:
  RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE

task:
  RECONSTRUCTION_TASK_ESTABLISHED

v2 retroactive substitution:
  prohibited
~~~

B1:

~~~text
compatible:
  {h1,h2}

excluded:
  {h3}

set outcome:
  B1_MULTIPLE_COMPATIBLE

task:
  B1_TASK_COMPLETE

v2 retroactive substitution:
  prohibited
~~~

Both retained class/evidence/bridge registry provenance.

Result:

~~~text
MATCH
~~~

## 5. R2 — exact affine preimage / kernel / declared-class uniqueness

Frozen map:

~~~text
F(x,y,z):
  (x+z,y+z)
~~~

Exact kernel:

~~~text
ker(F):
  span{(-1,-1,1)}
~~~

Observed:

~~~text
(2,3)
~~~

Global affine preimage:

~~~text
F^{-1}(2,3):
  {(2-t,3-t,t) : t in R}
~~~

Declared class:

~~~text
A:
  {(x,y,0): x,y in R}
~~~

Reconstruction and B1 both derive:

~~~text
GLOBAL_INJECTIVITY:
  not established

DECLARED_CLASS_PREIMAGE:
  {(2,3,0)}

UNIQUE_WITHIN_DECLARED_CLASS:
  established
~~~

Outside-class witness:

~~~text
(2,3,0)
and
(1,2,1)

both map to:
  (2,3)
~~~

Neither promotes the class-local result to global source or historical uniqueness.

Result:

~~~text
MATCH
~~~

## 6. R3 — required-interface dependency closure

Frozen candidates:

~~~text
s1:
  readout=0
  status=DEFINED_ZERO
  support=S1

s2:
  readout=0
  status=APPLICABLE_BUT_UNDEFINED
  support=S1
~~~

Main readout and support are non-discriminating.

The required typed source-status sidecar is unavailable.

Reconstruction:

~~~text
required status interface:
  unavailable

task:
  RECONSTRUCTION_TASK_BLOCKED
~~~

B1:

~~~text
required status dependency:
  unavailable

task:
  B1_TASK_BLOCKED
~~~

Neither system:

~~~text
coerces unavailable status to zero
excludes a candidate from the missing interface
promotes unavailability to proven destructive information loss
~~~

Result:

~~~text
MATCH
~~~

## 7. R4 — explicit probabilistic inverse inference

Frozen:

~~~text
P(p1)=1/2
P(p2)=1/2

P(e|p1)=3/4
P(e|p2)=1/4
~~~

Both compute:

~~~text
P(e):
  1/2

P(p1|e):
  3/4

P(p2|e):
  1/4

posterior ranking:
  p1 > p2
~~~

Reconstruction:

~~~text
explicit probabilistic interface:
  valid

posterior:
  (3/4,1/4)

ranking:
  p1 > p2
~~~

B1:

~~~text
explicit Bayesian inverse interface:
  valid

posterior:
  (3/4,1/4)

ranking:
  p1 > p2
~~~

Neither infers:

~~~text
p1 is the only compatible history
p1 is globally true history
p1 has established Lineage identity
~~~

Preserved:

~~~text
MOST_PROBABLE_HISTORY != ONLY_COMPATIBLE_HISTORY
POSTERIOR_RANKING != HISTORICAL_TRUTH
PROBABILITY != ESTABLISHED_LINEAGE
~~~

Result:

~~~text
MATCH
~~~

## 8. R5 — temporal relation algebra / branch-merge / sidecar pressure

Frozen:

~~~text
H_01:
  (a0,a1)
  (b0,a1)

H_12:
  (a1,c2)
  (a1,d2)
~~~

Both compute:

~~~text
H_12 o H_01:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)
~~~

The frozen direct long-interval relation is:

~~~text
H_02:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)
  (e0,c2)
~~~

Thus for observed endpoint:

~~~text
c2
~~~

the composed short-interval relation supports:

~~~text
{a0,b0}
~~~

while the direct long-interval relation supports:

~~~text
{a0,b0,e0}
~~~

Both Reconstruction and B1 retain the direct relation independently rather than replacing it by composition.

Both therefore return the bounded direct-relation prior candidate set:

~~~text
{a0,b0,e0}
~~~

Both preserve:

~~~text
branching:
  yes

merging:
  yes

unique predecessor:
  not established

direct relation == composed relation:
  not asserted
~~~

Neighbor/source sidecars:

~~~text
Tracking continuity
Lineage relation
Diagnosis current-state record
Aggregation equality
Compression collision
Measurement discrimination plan
Transformation map
Prediction output
Simulation trajectory
Optimization ranking
Audit pass
Formation witness-history
~~~

were retained without unauthorized substitution.

Neither evaluator promotes:

~~~text
Tracking subset -> universal reconstructed trace
Lineage subset -> universal historical identity
Formation witness-history -> actual temporal history
Simulation trajectory -> actual past
Optimization ranking -> historical exclusion
Audit pass -> historical truth
~~~

Both emit deterministic history ledgers and rerun manifests.

Result:

~~~text
MATCH
~~~

## 9. Gain-axis execution

~~~text
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN:
  BASELINE_MATCH

G2 EXACT_AFFINE_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN:
  BASELINE_MATCH

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN:
  BASELINE_MATCH

G4 EXPLICIT_PROBABILISTIC_INVERSE_INFERENCE_AND_SCOPE_GAIN:
  BASELINE_MATCH

G5 TEMPORAL_RELATION_ALGEBRA_BRANCH_MERGE_AND_HANDOFF_GAIN:
  BASELINE_MATCH

G6 BOUNDED_MAXIMUM_CLAIM_AND_TERMINAL_GAIN:
  BASELINE_MATCH

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN:
  BASELINE_MATCH
~~~

Overall:

~~~text
RECONSTRUCTION_METHOD_GAIN_STATUS:
  RECONSTRUCTION_NO_GAIN
~~~

No claim-relevant DSD Reconstruction performance advantage was established over B1 on this frozen constructed strong workload under equal-information access.

## 10. Execution of the 82 frozen checks

### A — immutable fairness

~~~text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS

A: 10/10
~~~

### B — R1 versioned registries

~~~text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS
B11 PASS
B12 PASS

B: 12/12
~~~

### C — R2 exact preimage / declared class

~~~text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS
C11 PASS
C12 PASS
C13 PASS
C14 PASS

C: 14/14
~~~

### D — R3 dependency closure

~~~text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS
D11 PASS
D12 PASS

D: 12/12
~~~

### E — R4 probabilistic inverse inference

~~~text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS
E9 PASS
E10 PASS
E11 PASS
E12 PASS

E: 12/12
~~~

### F — R5 temporal relation algebra / handoff pressure

~~~text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS
F8 PASS
F9 PASS
F10 PASS
F11 PASS
F12 PASS
F13 PASS
F14 PASS

F: 14/14
~~~

### G — comparative conclusion

~~~text
G1 PASS
G2 PASS
G3 PASS
G4 PASS
G5 PASS
G6 PASS
G7 PASS
G8 PASS

G: 8/8
~~~

Final:

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASSED:
  82

FAILED:
  0
~~~

## 11. Counter update

~~~text
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  5

POSITIVE_RECONSTRUCTION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES:
  1

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

UNRECOVERABILITY_RECONSTRUCTION_CASES:
  2

BASELINE_RECONSTRUCTION_CASES:
  2

NO_GAIN_RECONSTRUCTION_CASES:
  2

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES:
  0

EXTERNAL_RECONSTRUCTION_APPLICATIONS:
  0

INDEPENDENT_RECONSTRUCTION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

RECONSTRUCTION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_RECONSTRUCTION_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 12. Interpretation lock

The result means:

~~~text
A materially strong non-DSD inverse-reconstruction engine matched
the claim-relevant Reconstruction Protocol v0.1 outputs on the frozen
constructed strong workload under equal-information access.
~~~

It does not mean:

~~~text
B1 is universally strongest possible
Reconstruction Protocol failure
Reconstruction method deletion
Reconstruction should merge into another method
Reconstruction should be absorbed
permanent redundancy
future DSD-specific gain is impossible
external validity
independent replication
~~~

Required guards:

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

## 13. Maximum-supported claim

Supported:

~~~text
Within the frozen RECON-CH-005 constructed comparator class,
B1_STRONG_INVERSE_RECONSTRUCTION_ENGINE matched Reconstruction
Protocol v0.1 on versioned registry semantics, exact affine
preimage/kernel analysis, declared-class uniqueness,
required-interface dependency closure, explicit probabilistic
inverse inference, temporal relation algebra with branch/merge
and direct-versus-composed history records, neighboring/source
handoff boundaries, bounded claims, and deterministic replay metadata.

All seven frozen gain axes were BASELINE_MATCH.
~~~

Not established:

~~~text
universal baseline optimality
method redundancy
external applicability
independent validation
independent replication
method superiority
~~~

## 14. Next

Prospectively precommit and execute RECON-CH-006 deterministic same-project retrace.

The retrace must reconstruct the frozen claim-relevant RECON-CH-001~005 evidence from repository artifacts, compare independently reconstructed outputs against recorded outputs, preserve every mismatch, prohibit post-comparison correction, and keep:

~~~text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~
