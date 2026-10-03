# DSD Computation / DSD 계산론

Status: **active internal-build front — Task Interface v0.1 established / boundary attack next**
Legacy path ID: `12A`
Higher field: **VII. Computation & Selection / 계산·선택**

Task: determine which structural branches, channels, dependencies, resolutions, and reusable common parts must actually be evaluated for a declared computational target.

Primary DSD sources: Formation/Property admissibility and applicability, first branching, explicit dependency structure, aggregation-loss criteria.

Candidate operations:
- eliminate impossible or inapplicable branches before expensive evaluation;
- identify common prefixes and reusable subcomputations;
- select only channels capable of affecting the declared output;
- choose calculation resolution from required distinguishability;
- preserve soundness conditions for every omitted computation.

Boundary: DSD structure can organize computation, but complexity improvement must be proved or measured separately.


## Active-front handoff — 2026-10-03

Reconstruction / DSD 복원론 completed its project-internal standardization lane at Protocol v0.1 with RECON-AUD-001.

Computation / DSD 계산론 becomes the next family-wide internal-build front.

This handoff does not transfer Reconstruction evidence into Computation validation.

~~~text
RECONSTRUCTION_INTERNAL_STANDARDIZATION != COMPUTATION_VALIDATION
RECONSTRUCTION_EVIDENCE != COMPUTATION_EVIDENCE_BY_DEFAULT
~~~

### Next canonical work

~~~text
1. recover Computation source / registry constraints
2. separate source-derived constraints from prospective Computation method construction
3. create Computation planning / worklog lane
4. draft Task Interface only after recovery
5. boundary-attack before protocol freeze
~~~

No dedicated Computation protocol is established yet.


## Source / registry recovery — 2026-10-03

~~~text
SOURCE_REGISTRY_COMMIT:
  af9951011d999aef3c29a2beba6093983c1546f6
SOURCE_REGISTRY_BLOB:
  6f5ad5731ee82fc9a6561a39ff6d66fc4bd82461

PLANNING_COMMIT:
  f6c6a3e57b132909125c2bc3b6ee59c3a1643a88
PLANNING_BLOB:
  c6e21a2562765aa181889bb0b1e577e18bbf2f3e

WORKLOG_COMMIT:
  0a0fd9bc1d4431f29c6a51d6d45ee77abff0ba5c
WORKLOG_BLOB:
  5da60993a0d77a06d961e763018a34446aa6ef8f

CURRENT_STATUS_COMMIT:
  aefe09288d88ea67b38e67e31e73bd1dcc3c315a
CURRENT_STATUS_BLOB:
  9d3ba44a110dd4420049a8082ca46815b8a5ed5a

SOURCE_REGISTRY_RECOVERY:
  complete

PLANNING_LANE:
  established

TASK_INTERFACE_DRAFT:
  v0.1 established

TASK_INTERFACE_COMMIT:
  e0376c35c9fd6c6ab2fc1a20a5bc0e329fc0fb71

TASK_INTERFACE_BLOB:
  0e307f2e6bb3b579a8bc161cb0a25bd76c28e69f

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

DEDICATED_COMPUTATION_PROTOCOL:
  not established

CURRENT_COMPUTATION_EVIDENCE_STATUS:
  source_and_interface_recovery
~~~

Recovered source-derived constraints are recorded as `CR-01~CR-16`.

The working method boundary remains:

~~~text
COMPUTATION:
  determine required evaluation / sound omission / scoped reuse

OPTIMIZATION:
  select among admissible alternatives
  under explicit objectives and constraints

COMPUTATION != OPTIMIZATION
~~~

The recovered source constraints do not themselves validate Computation as a method.

## Next canonical step

Execute a serious pre-protocol boundary attack against **Computation Task Interface v0.1**.

The historical Task Interface draft must not be rewritten once boundary attack begins; any required refinement must be recorded in a separate prospective amendment.
