# DSD Prediction — Boundary Amendment 001

Status: **ESTABLISHED — 8/8 REFINEMENTS ADOPTED / PROTOCOL FREEZE AUTHORIZED**  
Date: **2026-10-06**

Historical Task Interface:

~~~text
TASK_INTERFACE_COMMIT:
  b5e4004aeb1b90866e17ad0c26ffdba833b0effe
TASK_INTERFACE_BLOB:
  edcafd7e692933a5e02a5384e85cf78553670474
~~~

Boundary stress test:

~~~text
COMMIT:
  a1c90a4f6b5500e3dfb23b6dbb7a0b942e3c4121
BLOB:
  028eddff450b1bae49176b801cc2b205fab7c173
RESULT:
  18 tests / 10 preserved / 8 nonbreaking refinements / 0 collapse
~~~

The historical Task Interface is not rewritten.

## R1 — issue-time integrity

Freeze issue information cutoff and future-data leakage status.

~~~text
FUTURE_DATA_LEAKAGE_FOUND
  ->
original prospective claim cannot remain PREDICTION_ESTABLISHED
under the same Prediction version
~~~

## R2 — target-definedness binding

~~~text
known inapplicability/prerequisite failure -> NOT_ESTABLISHED
required status interface unavailable -> BLOCKED
conflicting applicable target records -> CONFLICTING
unresolved admissible target semantics with different outputs
  -> UNDERDETERMINED
~~~

Guards:

~~~text
UNDEFINED_TARGET != PREDICTED_ZERO
INAPPLICABLE_TARGET != ZERO_VALUE_TARGET
~~~

## R3 — uncertainty versus underdetermination

Freeze:

~~~text
UNCERTAINTY_KIND
UNCERTAINTY_SCOPE
SEMANTIC_RESOLUTION_STATUS
SEMANTIC_ALTERNATIVE_REGISTRY
~~~

Binding:

~~~text
declared uncertainty may remain inside a supported claim

unresolved admissible semantics that materially alter output
  ->
PREDICTION_UNDERDETERMINED
~~~

## R4 — update lineage

Every claim-relevant update records:

~~~text
parent Prediction version
new Prediction version
new information cutoff
trigger/provenance
new model/bridge version if any
supersession relation
~~~

Historical issue-time versions remain immutable.

## R5 — claim mode

Adopt:

~~~text
PROSPECTIVE_ISSUE
RETROSPECTIVE_RECONSTRUCTION
HINDCAST_OR_BACKTEST
POST_OUTCOME_EXPLANATION
~~~

Only `PROSPECTIVE_ISSUE` supports an original prospective Prediction claim.

## R6 — effective validity region

Define:

~~~text
EFFECTIVE_PREDICTION_VALIDITY_REGION
  =
intersection of all required claim-relevant
model / bridge / uncertainty / target applicability validity regions
~~~

Binding:

~~~text
evaluably outside effective region -> NOT_ESTABLISHED
required validity scope unavailable -> BLOCKED
~~~

## R7 — validation-standard lock

For a prospectively scored forecast, freeze before outcome availability:

~~~text
VALIDATION_STANDARD_ID
VALIDATION_STANDARD_VERSION
VALIDATION_METRIC_OR_RULE
VALIDATION_THRESHOLD_IF_ANY
VALIDATION_TARGET_MAPPING
~~~

A later alternative metric may be a new analysis but does not replace the original validation version.

## R8 — task terminal versus later validation

Task-terminal precedence:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

PARTIAL requires multiple independently required in-scope obligations, at least one ESTABLISHED and at least one evaluably NOT_ESTABLISHED, with no BLOCKED or higher-priority state.

Later validation remains separate:

~~~text
PREDICTION_VALIDATION_NOT_YET_DUE
PREDICTION_VALIDATION_PASSED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_FAILED_ON_DECLARED_STANDARD
PREDICTION_VALIDATION_BLOCKED
PREDICTION_VALIDATION_CONFLICTING
PREDICTION_VALIDATION_UNDERDETERMINED
PREDICTION_VALIDATION_OUT_OF_SCOPE
~~~

Guards:

~~~text
PREDICTION_VALIDATION_NOT_YET_DUE != PREDICTION_TASK_BLOCKED
PREDICTION_ESTABLISHED_AT_ISSUE != PREDICTION_VALIDATION_PASSED
PARTIAL != BLOCKED_WITH_SOME_SUCCESS
PARTIAL != ATOMIC_FAILURE_RELABELED
~~~

## Aggregate

~~~text
REFINEMENT_GROUPS_ADOPTED:
  8/8
METHOD_IDENTITY_CHANGED:
  no
HISTORICAL_TASK_INTERFACE_REWRITTEN:
  no
BOUNDARY_COLLAPSE:
  0
FUNDAMENTAL_INTERFACE_FAILURE:
  0
SHARED_CORE_REOPEN_REQUIRED:
  no
PROTOCOL_FREEZE_AUTHORIZED:
  yes
~~~

## Next

Freeze executable Prediction Protocol v0.1.
