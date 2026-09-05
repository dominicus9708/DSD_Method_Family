# 12. DSD Computation-Optimization / DSD 계산·최적화론

Status: **proposed umbrella**

This historical registry group is preserved for path compatibility but is now subdivided into two atomic methods:

- [`computation/`](computation/) — **12A. DSD Computation / DSD 계산론**: determine which branches, channels, dependencies, resolutions, and reusable common parts must actually be evaluated.
- [`optimization/`](optimization/) — **12B. DSD Optimization / DSD 최적화론**: choose among admissible computational, structural, scheduling, or resource-allocation alternatives under explicit objectives and constraints.

The distinction is deliberate: computation asks what must be calculated and how; optimization asks which admissible strategy is preferable under a declared objective.

Primary DSD sources: Formation/Property pruning, first branching, aggregation-loss criteria, required resolution, optional dynamic resource lifecycle.

Boundary: every pruning rule requires a soundness argument, and every optimization requires an explicit objective/constraint model. DSD terminology alone proves neither reduced complexity nor optimality.
