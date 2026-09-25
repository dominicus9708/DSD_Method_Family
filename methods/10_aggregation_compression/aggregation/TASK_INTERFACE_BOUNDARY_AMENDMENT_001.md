# DSD Aggregation Task Interface Boundary Amendment 001

Status: **PROSPECTIVE AMENDMENT ESTABLISHED**
Date: **2026-09-25**
Method: **Aggregation / DSD 집계론**

Frozen historical basis:

```text
TASK_INTERFACE_COMMIT:
  58287d8b4d200c55860c5029281699de0750a5d4

TASK_INTERFACE_BLOB:
  0eb42ab35703b4ac684ddd0fa477289dd944a3f0

BOUNDARY_ATTACK_COMMIT:
  59eefe5347b8509c097ee69ec488fcfe808849e9

BOUNDARY_ATTACK_BLOB:
  5deb99c973c8c89b4aead5d588d88b525daa534c
```

The historical Task Interface and boundary-attack record are not rewritten.

## 1. Amendment result

```text
BOUNDARY_AMENDMENT_001:
  established

REFINEMENT_GROUPS_ADOPTED:
  5/5

METHOD_IDENTITY_CHANGED:
  no

TASK_INTERFACE_CORE_REOPENED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no

PROTOCOL_FREEZE_AUTHORIZED:
  yes
```

## 2. R1 — required support/status sidecar failure rule

If a frozen claim requires support-retaining or source-status data and that required interface is unavailable:

```text
AGGREGATION_TASK_TERMINAL:
  AGGREGATION_TASK_BLOCKED
```

Do not use `AGGREGATION_TASK_NOT_ESTABLISHED` merely because the required evidence is unavailable.

Use `NOT_ESTABLISHED` only when the frozen claim is in scope, all required interfaces are available, and the evaluable proposition fails.

Guard:

```text
REQUIRED_INTERFACE_UNAVAILABLE
  !=
EVALUABLE_FAILURE
```

## 3. R2 — injectivity-scope lock

Any injectivity claim must freeze:

```text
INJECTIVITY_SUPPORT:
  F

INJECTIVITY_OPERATOR:
  S_F

ADMISSIBLE_ASSIGNMENT_CLASS:
  A_F

INJECTIVITY_CLAIM_LEVEL:
  fixed_support_assignment
  support_recovery
  combined_reconstruction
```

Status semantics:

```text
A_F required but unavailable:
  INJECTIVITY_BLOCKED

multiple admissible A_F definitions,
different outcomes,
no resolver:
  AGGREGATION_UNDERDETERMINED

criterion evaluable and fails:
  INJECTIVITY_NOT_ESTABLISHED

criterion evaluable and passes:
  INJECTIVITY_ESTABLISHED_ON_DECLARED_CLASS
```

Guard:

```text
INJECTIVITY_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY
```

## 4. R3 — reconstruction-scope class

Every reconstruction-support claim must freeze one:

```text
RECONSTRUCTION_SCOPE_CLASS:
  fixed_support
  variable_support
  combined_coordinate
```

Semantics:

```text
fixed_support:
  source support F is frozen;
  only assignment reconstruction on that support is claimed

variable_support:
  support itself may vary and must be recoverable under
  an explicitly supplied larger reconstruction interface

combined_coordinate:
  channel and property coordinates may both participate,
  with cross-coordinate requirements explicitly declared
```

A fixed-support injectivity theorem may not be promoted to variable-support reconstruction.

Guard:

```text
FIXED_SUPPORT_INJECTIVITY
  !=
VARIABLE_SUPPORT_RECONSTRUCTION
```

## 5. R4 — cross-coordinate reconstruction condition

For `COMBINED_STATIC_DESCRIPTOR` reconstruction claims, freeze:

```text
CROSS_COORDINATE_RECONSTRUCTION_CONDITION:
  not_required
  supplied
  required_but_unavailable
  unresolved
```

Consequences:

```text
required_but_unavailable:
  AGGREGATION_TASK_BLOCKED

unresolved:
  AGGREGATION_TASK_UNDERDETERMINED

supplied:
  evaluate the supplied condition

not_required:
  do not invent one
```

Coordinatewise injectivity alone is insufficient for a cross-coordinate coupling claim unless the application declares that no such coupling must be recovered.

## 6. R5 — task-terminal precedence

Freeze:

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

Rules:

```text
OUT_OF_SCOPE:
  requested operation/claim lies outside frozen Aggregation scope

CONFLICTING:
  mutually incompatible applicable claim-relevant records
  exist under the same frozen semantics and no precedence resolves them

UNDERDETERMINED:
  multiple admissible claim-relevant interpretations/scopes/maps
  yield different outcomes and no resolver exists

BLOCKED:
  a required interface, support sidecar, admissible class,
  bridge, prerequisite, or reconstruction condition is unavailable

ESTABLISHED:
  all required obligations are established

PARTIAL:
  multiple independent required obligations exist,
  at least one is established and at least one evaluable obligation
  is not established, with no higher-priority terminal

NOT_ESTABLISHED:
  the in-scope required proposition is evaluable and fails
```

Lower-level statuses remain preserved under a higher-priority terminal.

## 7. Binding status refinements

The protocol must distinguish:

```text
SOURCE_STATUS:
  absent / undefined / defined_zero / defined_nonzero

AGGREGATION_DOMAIN_STATUS:
  admitted / not_admitted / blocked / underdetermined / out_of_scope

COLLISION_STATUS:
  not_tested
  witness_established
  no_collision_on_tested_class

INJECTIVITY_STATUS:
  not_tested
  established_on_declared_class
  not_established
  blocked
  underdetermined
  out_of_scope

RECONSTRUCTION_SCOPE_STATUS:
  fixed_support
  variable_support
  combined_coordinate
  not_claimed
```

These are not collapsed into one generic PASS/FAIL flag.

## 8. Protocol-freeze authorization

The five refinement groups are prospective and do not alter the source paper's mathematical statements.

They supply execution semantics required for a deterministic Method Family protocol.

Therefore:

```text
PROTOCOL_FREEZE_AUTHORIZED:
  yes
```
