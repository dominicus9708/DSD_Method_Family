# DSD Prediction — Planning / Validation Roadmap

Status: **ACTIVE INTERNAL BUILD — PROTOCOL v0.1 FROZEN / PRED-CH-001 NEXT**  
Date: **2026-10-06**

## 1. Canonical development sequence

~~~text
1. ✅ Simulation -> Prediction active-front handoff
2. ✅ Prediction source / registry recovery
3. ✅ source-derived constraints separated from prospective method construction
4. ✅ planning / worklog lane
5. ✅ Prediction Task Interface v0.1 draft
6. ✅ serious pre-protocol boundary attack — 18 tests / 10 preserved / 8 refinements / 0 collapse
7. ✅ Boundary Amendment 001 — 8/8 refinements adopted
8. ✅ executable Prediction Protocol v0.1 — G1-G18 / P1-P18
9. ✅ positive constructed challenge — PRED-CH-001 84/84 PASS
10. ⏸ negative / blocked / conflicting / underdetermined /
       out-of-scope / partial terminal coverage — PRED-CH-002 next
11. ⏸ direct neighboring-method boundary challenge
12. ⏸ competent non-DSD baseline
13. ⏸ strongest-reasonable non-DSD baseline
14. ⏸ deterministic same-project retrace
15. ⏸ frozen-axis internal-standardization audit
16. ⏸ external applications / independent validation later
~~~

Internal standardization is completed before external validation is opened.

## 2. Source and interface provenance

~~~text
SOURCE_REGISTRY_COMMIT:
  7c7bc16cf93e756a12688dc5261aecfce5e83533

SOURCE_REGISTRY_BLOB:
  8a93199fdb4abb8c4a4ffbfa0a7ea0f1c3ac34cf

TASK_INTERFACE_COMMIT:
  b5e4004aeb1b90866e17ad0c26ffdba833b0effe

TASK_INTERFACE_BLOB:
  edcafd7e692933a5e02a5384e85cf78553670474
~~~

## 3. Method-construction lock

Prediction is constructed prospectively from recovered source constraints.

The predecessor DSD papers and Simulation supply structural/model interfaces, but they do not already contain this complete method-level Prediction protocol.

~~~text
SOURCE_DERIVED_CONSTRAINT
  !=
PREDICTION_METHOD_PROTOCOL

SIMULATION_TRAJECTORY
  !=
PREDICTION_VALIDATION

SHARED_CORE_SUPPORT
  !=
DIRECT_PREDICTION_VALIDATION
~~~

## 4. Boundary pressure to execute next

The frozen Task Interface declares 18 direct attack targets:

~~~text
A1  post-outcome/future data leaks into issue-time prediction
A2  missing target bridge silently treated as zero prediction
A3  undefined/inapplicable target silently treated as zero
A4  trajectory branch count silently converted to probability mass
A5  scenario set silently converted to probability distribution
A6  uncertainty conflated with semantic underdetermination
A7  Simulation trajectory promoted to future-world truth
A8  newer model version retroactively rewrites old forecast
A9  new observation update retroactively rewrites old forecast
A10 retrospective fit mislabeled as prospective prediction
A11 equal reduced readouts promoted to equal future structural state
A12 target horizon exceeds model/bridge validity region
A13 validation metric/threshold changed after target outcome is known
A14 target observation unavailable treated as hit or miss
A15 Prediction substituted for Control intervention choice
A16 Prediction substituted for Operation live execution
A17 fair competent baseline yields NO_GAIN
A18 terminal precedence / PARTIAL / NOT_YET_DUE validation pressure
~~~

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

DEDICATED_PREDICTION_PROTOCOL:
  established v0.1

DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  1

SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  1

POSITIVE_PREDICTION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_PREDICTION_CASES:
  0

METHOD_BOUNDARY_PREDICTION_CASES:
  0

BASELINE_PREDICTION_CASES:
  0

NO_GAIN_PREDICTION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_PREDICTION_APPLICATIONS:
  0

INDEPENDENT_PREDICTION_VALIDATION:
  not established

PREDICTION_INTERNAL_STANDARDIZATION_STATUS:
  developing
~~~

## 7. Next

PRED-CH-001 completed at 84/84 PASS.

Next: prospectively precommit and execute **PRED-CH-002** terminal / negative coverage.
