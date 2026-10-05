# DSD Control — Planning / Validation Roadmap

Status: **ACTIVE INTERNAL BUILD — CTRL-CH-005 82/82 PASS / CTRL-CH-006 NEXT**  
Date: **2026-10-06**

## Canonical sequence

~~~text
1. ✅ Prediction -> Control active-front handoff
2. ✅ Control source / registry recovery
3. ✅ Control Task Interface v0.1 draft
4. ✅ pre-protocol boundary review — 18 tests / 8 refinements / 0 collapse
5. ✅ Boundary Amendment 001 — 8/8 adopted
6. ✅ executable Control Protocol v0.1 — G1-G18 / C1-C18
7. ✅ positive constructed challenge — CTRL-CH-001 84/84 PASS
8. ✅ status / terminal coverage — CTRL-CH-002 100/100 PASS
9. ✅ direct neighboring-method boundary challenge — CTRL-CH-003 90/90 PASS / 10 pairs / exact collapse 0
10. ✅ competent non-DSD baseline — CTRL-CH-004 64/64 PASS / NO_GAIN
11. ✅ strongest-reasonable non-DSD baseline — CTRL-CH-005 82/82 PASS / NO_GAIN
12. ⏸ deterministic same-project retrace — CTRL-CH-006 next
13. ⏸ frozen-axis internal-standardization audit
14. ⏸ external / independent validation later
~~~

## Current counters

~~~text
PRE_PROTOCOL_BOUNDARY_TESTS:
  18
BOUNDARY_AMENDMENT_001:
  established
DEDICATED_CONTROL_PROTOCOL:
  established v0.1

DIRECT_CONTROL_PILOTS_ATTEMPTED:
  5
SUCCESSFUL_DIRECT_CONTROL_PILOTS:
  5
POSITIVE_CONTROL_CASES:
  1
NEGATIVE_OR_UNRESOLVED_CONTROL_CASES:
  1
METHOD_BOUNDARY_CONTROL_CASES:
  1
BASELINE_CONTROL_CASES:
  2
NO_GAIN_CONTROL_CASES:
  2
REPRODUCIBILITY_CASES:
  0

EXTERNAL_CONTROL_APPLICATIONS:
  0
INDEPENDENT_CONTROL_VALIDATION:
  not established
INDEPENDENT_REPLICATION:
  not established
CONTROL_INTERNAL_STANDARDIZATION_STATUS:
  developing
~~~

## Evidence path

~~~text
Task Interface
-> boundary review
-> amendment
-> executable protocol
-> positive / negative / boundary / NO_GAIN
-> strongest-reasonable baseline
-> deterministic retrace
-> frozen-axis audit
-> later external validation
~~~

## Next

CTRL-CH-005 completed at 82/82 PASS with `CONTROL_NO_GAIN` and a constructed-evidence strongest-reasonable baseline.

Next: prospectively precommit and execute **CTRL-CH-006**, the deterministic same-project Control retrace.
