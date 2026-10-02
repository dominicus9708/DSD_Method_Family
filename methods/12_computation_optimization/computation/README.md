# DSD Computation / DSD 계산론

Status: **active internal-build front — source/registry recovery and planning next**
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
