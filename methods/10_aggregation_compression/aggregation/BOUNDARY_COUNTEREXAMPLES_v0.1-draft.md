# DSD Aggregation Boundary Counterexamples v0.1 Draft

Status: **EXECUTED — PRE-PROTOCOL BOUNDARY ATTACK COMPLETE**
Date: **2026-09-25**
Method: **Aggregation / DSD 집계론**
Task Interface basis:

```text
TASK_INTERFACE_COMMIT:
  58287d8b4d200c55860c5029281699de0750a5d4

TASK_INTERFACE_BLOB:
  0eb42ab35703b4ac684ddd0fa477289dd944a3f0
```

## 1. Purpose

Attack the historical Task Interface v0.1 draft before any executable Aggregation Protocol is frozen.

The attack asks whether the method boundary survives source-supported collision, support-loss, status, convergence, postprocessing, reconstruction, and neighboring-method cases without silent repair.

Allowed verdicts:

```text
PRESERVED_NO_REFINEMENT
PRESERVED_WITH_NONBREAKING_REFINEMENT
BOUNDARY_COLLAPSE
FUNDAMENTAL_INTERFACE_FAILURE
```

## 2. Summary result

```text
BOUNDARY_ATTACKS_RUN: 18

PRESERVED_NO_REFINEMENT: 13
PRESERVED_WITH_NONBREAKING_REFINEMENT: 5

BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0

BOUNDARY_AMENDMENT_REQUIRED: yes
PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The five required refinements concern execution semantics, not Aggregation method identity.

## 3. A1 — equal channel aggregate, different support-resolved data

Fixture:

```text
F1:
  two nonzero component terms that cancel

F2:
  one admitted zero term

Comp(F1) = Comp(F2) = 0

support-resolved data:
  different
```

Expected pressure:

```text
AGGREGATE_EQUALITY
  must not imply
SUPPORT_EQUALITY
```

Task Interface response:

```text
support sidecars are distinct from reduced aggregate
collision/injectivity claims are separate
```

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 4. A2 — equal property aggregate, different typed-property support

Fixture:

```text
G1:
  unary +2
  binary -2

G2:
  unary defined zero

Agg(G1) = Agg(G2) = 0

typed supports:
  different
```

The binary datum remains attached to its complete ordered typed input.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

Guard preserved:

```text
PROPERTY_AGGREGATE_EQUALITY
  !=
PROPERTY_SUPPORT_EQUALITY
```

## 5. A3 — admitted zero term versus absent channel

Fixture:

```text
c0 in C_L
T(c0) = 0

cX not in C_L
T(cX) undefined
```

A sum may fail to expose the difference.

The support/status ledger must retain it.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 6. A4 — undefined property versus defined zero

Fixture:

```text
p0:
  applicable and defined with value 0

p1:
  applicable but undefined
```

Only p0 belongs to the defined typed-property carrier.

Zero-padding p1 would collapse the source distinction.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 7. A5 — multi-input property allocation pressure

Fixture:

```text
property profile:
  (s1,s2)

datum:
  (x1,x2,z)

no selector/allocation rule supplied
```

Attack:

```text
assign datum to channel associated with x1
or
assign datum to channel associated with x2
```

Both are unsupported without additional application structure.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 8. A6 — direct finite sum versus normalized average

Fixture:

```text
T(c1) = 2
T(c2) = 4

direct Formation-compatible aggregate:
  6

normalized average with equal coefficients:
  3
```

Attack:

```text
treat 3 as the Clause-VII aggregate
```

Rejected.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 9. A7 — finite core versus absolutely summable countable extension

Fixture:

```text
finite F:
  core Clause-VII domain

countable F_infty:
  absolute sum of term norms finite
```

The countable case is an optional analytic extension, not a silent enlargement of the Formation core domain.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 10. A8 — conditionally convergent countable aggregation

Fixture:

```text
countable family
series converges only conditionally
enumeration can affect the value
```

The current source-defined countable extension requires absolute/unconditional convergence.

Attack:

```text
accept the conditionally convergent sum as current-core Aggregation
```

Rejected.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 11. A9 — formation/property coordinate conflation

Fixture:

```text
Comp(F) = 5
Agg(G)  = 5
```

Attack:

```text
because numerical values coincide,
identify the formation coordinate
with the property coordinate
```

Rejected.

The combined descriptor remains an ordered pair with distinct logical roles.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 12. A10 — postprocessing conflation

Fixture:

```text
core aggregate:
  y in W_L direct-sum output

later map:
  P(y) = scalar score
```

Attack:

```text
replace the core aggregation task by P(y)
and erase P provenance
```

Rejected.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 13. A11 — source reconstruction claim with missing required support sidecar

Fixture:

```text
aggregate value available
support-retaining channel/property records required by claim
support sidecar unavailable
```

The draft says support data must be retained when reconstruction matters, but does not yet freeze the exact task consequence of the missing required sidecar.

Required refinement:

```text
if a declared reconstruction/support-identification claim
requires a support sidecar and that required interface is unavailable:

  AGGREGATION_TASK_BLOCKED

not:

  AGGREGATION_TASK_NOT_ESTABLISHED
```

This mirrors the difference between unavailable required evidence and an evaluable negative result.

Verdict:

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

## 14. A12 — injectivity claim with no admissible assignment class

Fixture:

```text
fixed support F supplied
summation operator S_F supplied
admissible assignment class A_F not supplied
```

The exact kernel criterion is relative to the declared class.

Without A_F, a class-relative injectivity proposition is not fully evaluable.

Required refinement:

```text
INJECTIVITY_SCOPE must freeze:
  support F
  admissible assignment class A_F

if A_F is required but unavailable:
  INJECTIVITY_BLOCKED

if multiple admissible A_F definitions remain and
produce different outcomes with no resolver:
  AGGREGATION_UNDERDETERMINED
```

Verdict:

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

## 15. A13 — fixed-support injectivity misapplied to varying support

Fixture:

```text
S_F injective on A_F
but comparison asks whether equal aggregates
identify both support and assignments across
different possible support sets
```

Fixed-support injectivity alone does not establish support recovery across varying support.

Required refinement:

```text
RECONSTRUCTION_SCOPE_CLASS:
  fixed_support
  variable_support
  combined_coordinate

a fixed-support injectivity result may not be promoted
to variable-support reconstruction
```

Verdict:

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

## 16. A14 — combined descriptor reconstruction without cross-coordinate condition

Fixture:

```text
formation coordinate:
  individually injective on its declared class

property coordinate:
  individually injective on its declared class

combined reconstruction claim:
  also depends on a cross-coordinate association
  not supplied
```

Coordinatewise injectivity need not establish a cross-coordinate reconstruction claim if the application asks to recover their coupling.

Required refinement:

```text
CROSS_COORDINATE_RECONSTRUCTION_CONDITION:
  not_required
  supplied
  required_but_unavailable
  unresolved

required_but_unavailable:
  BLOCKED
```

Verdict:

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

## 17. A15 — static perturbation stability promoted to dynamical stability

Fixture:

```text
static map perturbation bound:
  established

physical/dynamical evolution law:
  not supplied
```

Attack:

```text
claim dynamical stability
```

Rejected.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 18. A16 — weighted structural descriptor equality promoted to source identity

Fixture:

```text
D_w(U) = D_w(V)
U != V
```

Attack:

```text
infer same underlying state/support from equal scalar readout
```

Rejected.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 19. A17 — Aggregation versus Compression / Reconstruction / Measurement

Shared data may overlap, but the atomic operations differ.

```text
Aggregation:
  combine selected admitted values into a declared readout

Compression:
  reduce representation while preserving distinctions required
  by a downstream purpose

Reconstruction:
  infer source/support/history compatible with reduced evidence

Measurement:
  acquire or estimate declared quantities/data
```

No pair becomes identical merely because one method's output can be another method's input.

Verdict:

```text
PRESERVED_NO_REFINEMENT
```

## 20. A18 — simultaneous conflict, blockage, and underdetermination

Fixture:

```text
task contains multiple required obligations

Q1:
  two applicable aggregation-map records conflict

Q2:
  required support sidecar unavailable

Q3:
  two admissible reconstruction scopes
  yield different injectivity outcomes
  no resolver
```

The draft deliberately left terminal precedence unfrozen.

A deterministic protocol needs one.

Required refinement:

```text
AGGREGATION_TASK_OUT_OF_SCOPE
>
AGGREGATION_TASK_CONFLICTING
>
AGGREGATION_TASK_UNDERDETERMINED
>
AGGREGATION_TASK_BLOCKED
>
AGGREGATION_TASK_ESTABLISHED /
AGGREGATION_TASK_PARTIAL /
AGGREGATION_TASK_NOT_ESTABLISHED
```

Lower-level statuses remain preserved even when a higher-priority task terminal is emitted.

Verdict:

```text
PRESERVED_WITH_NONBREAKING_REFINEMENT
```

## 21. Required prospective amendment groups

The 18 attacks expose five nonbreaking execution-semantic refinements.

### R1 — required support-sidecar failure rule

```text
required but unavailable support/status sidecar
  -> BLOCKED

evaluable aggregate/support claim that fails
  -> NOT_ESTABLISHED
```

### R2 — injectivity-scope lock

Freeze:

```text
support F
admissible assignment class A_F
operator S_F
claim level
```

and separate missing class from unresolved alternative classes.

### R3 — reconstruction-scope class

Freeze:

```text
fixed_support
variable_support
combined_coordinate
```

A fixed-support theorem cannot silently justify variable-support recovery.

### R4 — cross-coordinate reconstruction condition

Combined-descriptor reconstruction must state whether cross-coordinate coupling is:

```text
not required
supplied
required but unavailable
unresolved
```

### R5 — task-terminal precedence

Freeze:

```text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

## 22. Boundary conclusion

```text
AGGREGATION_METHOD_IDENTITY:
  preserved

TASK_INTERFACE_CORE:
  preserved

NONBREAKING_REFINEMENTS_REQUIRED:
  5

BOUNDARY_COLLAPSE_FOUND:
  0

FUNDAMENTAL_INTERFACE_FAILURE:
  0

PROTOCOL_FREEZE_AUTHORIZED_BEFORE_AMENDMENT:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 23. Next

Prospectively create **Aggregation Task Interface Boundary Amendment 001** containing R1-R5.

Do not rewrite the historical Task Interface or this attack record.
