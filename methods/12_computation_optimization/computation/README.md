# DSD Computation / DSD 계산론

Status: **proposed**
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
