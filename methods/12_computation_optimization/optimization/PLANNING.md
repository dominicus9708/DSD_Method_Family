# DSD Optimization — Planning / Validation Roadmap

Status: **ACTIVE INTERNAL BUILD — OPT-CH-003 99/99 PASS / COMPETENT BASELINE NEXT**  
Date: **2026-10-05**

## 1. Canonical development sequence

~~~text
1. ✅ Computation -> Optimization active-front handoff
2. ✅ Optimization source / registry recovery
3. ✅ source-derived constraints separated from prospective method construction
4. ✅ planning / worklog lane
5. ✅ Optimization Task Interface v0.1 draft
6. ✅ serious pre-protocol boundary attack — 18 attacks / 12 preserved / 6 nonbreaking refinements / 0 collapse
7. ✅ Boundary Amendment 001 — 6/6 refinements adopted
8. ✅ executable Optimization Protocol v0.1 — G1-G18 / O1-O18
9. ✅ positive constructed challenge — OPT-CH-001 72/72 PASS
10. ✅ negative / blocked / conflicting / underdetermined / out-of-scope / partial terminal coverage — OPT-CH-002 80/80 PASS
11. ✅ direct neighboring-method boundary challenge — OPT-CH-003 99/99 PASS / 11 pairs / 0 collapse
12. ⏸ competent non-DSD baseline — OPT-CH-004 next
13. ⏸ strongest-reasonable non-DSD baseline
14. ⏸ deterministic same-project retrace
15. ⏸ frozen-axis internal-standardization audit
16. ⏸ external applications / independent validation later
~~~

Internal standardization is completed before external validation is opened.

## 2. Source and interface provenance

~~~text
SOURCE_REGISTRY_COMMIT:
  f48856ae9df1e189cc08681c1492398e06341def

SOURCE_REGISTRY_BLOB:
  34ff4cd5ad9acb5a8d9c83a87e226c58d6675ef0

TASK_INTERFACE_COMMIT:
  753206b90421bb317462e3cd214a280faf95e317

TASK_INTERFACE_BLOB:
  a3e3490a6a24d0793c608c85e6e0cb6a120f78f6
~~~

## 3. Method-construction lock

Optimization is constructed prospectively from recovered constraints.

The predecessor DSD papers and neighboring methods do not already contain an executable Optimization protocol.

~~~text
SOURCE_DERIVED_CONSTRAINT
  !=
OPTIMIZATION_THEOREM

COMPUTATION_HANDOFF
  !=
OPTIMIZATION_RESULT

SHARED_CORE_SUPPORT
  !=
DIRECT_OPTIMIZATION_VALIDATION
~~~

## 4. Boundary pressure to execute next

The frozen Task Interface declares 18 direct attack targets:

~~~text
A1  undefined objective value coerced to zero
A2  inadmissible candidate assigned favorable score
A3  hard constraint silently converted to penalty
A4  multiple objectives silently scalarized
A5  tied optimum mislabeled underdetermined
A6  Pareto set mislabeled unique optimum
A7  equal objective score used as structural identity
A8  incomplete candidate set used for global optimum claim
A9  overlapping uncertainty intervals used for strict order
A10 stale regime-A optimum reused after regime transition
A11 sufficient Computation plan mislabeled optimal
A12 Comparison ranking substituted for Optimization
A13 one-time optimum promoted to Control policy
A14 operation lifecycle cost omitted from a lifecycle objective
A15 aggregate / compressed objective collision ignored
A16 fair-baseline comparison with unequal candidate information
A17 sound optimization result with NO_GAIN
A18 terminal precedence / PARTIAL pressure
~~~

The attack may add pressure cases but may not rewrite the historical Task Interface after attack execution starts.

## 5. Expected evidence maturity path

~~~text
Task Interface
-> boundary attack
-> amendment
-> executable protocol
-> positive / negative / boundary / NO_GAIN
-> strongest-reasonable baseline
-> deterministic same-project retrace
-> frozen-axis internal-standardization audit
-> later external / independent validation
~~~

## 6. Current counters

~~~text
PRE_PROTOCOL_BOUNDARY_ATTACKS:
  18

BOUNDARY_AMENDMENT_001:
  established

DEDICATED_OPTIMIZATION_PROTOCOL:
  established v0.1


DIRECT_OPTIMIZATION_PILOTS_ATTEMPTED:
  2

SUCCESSFUL_DIRECT_OPTIMIZATION_PILOTS:
  2

POSITIVE_OPTIMIZATION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_OPTIMIZATION_CASES:
  1

ALL_SIX_OPTIMIZATION_PRIMARY_STATUSES_DIRECTLY_EXERCISED:
  yes

ALL_SEVEN_OPTIMIZATION_TASK_TERMINALS_DIRECTLY_EXERCISED:
  yes

METHOD_BOUNDARY_OPTIMIZATION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

EXACT_COLLAPSE_PAIRS:
  0

UNRESOLVED_BOUNDARY_PAIRS:
  0

PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  11

BASELINE_OPTIMIZATION_CASES:
  0

NO_GAIN_OPTIMIZATION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_OPTIMIZATION_APPLICATIONS:
  0

INDEPENDENT_OPTIMIZATION_VALIDATION:
  not established

OPTIMIZATION_INTERNAL_STANDARDIZATION_STATUS:
  developing
~~~

## 7. Next

OPT-CH-003 completed at 99/99 PASS.

The frozen fixture tested Optimization against Computation, Comparison, Design, Measurement, Aggregation, Compression, Simulation, Prediction, Control, Operation, and Audit. All 11 pairs were `PARTIAL_OVERLAP_NOT_COLLAPSE`; exact collapse 0 and unresolved boundary 0.

Next: prospectively precommit and execute **OPT-CH-004**, a fair competent non-DSD Optimization baseline with equal claim-relevant information and an explicit NO_GAIN-allowed scoring rule.
