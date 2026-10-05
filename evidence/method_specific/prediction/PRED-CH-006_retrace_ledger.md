# PRED-CH-006 Retrace Ledger

Status: **FROZEN BEFORE FORMAL COMPARISON**  
Date: **2026-10-06**

~~~text
PRECOMMIT_COMMIT:
  e8660a8a3a28180c31bae4ba45cf5a5686540196
PRECOMMIT_BLOB:
  8760589fa391f657717df807e6e3735d5d2545d1

DERIVATION_SOURCES:
  P0 protocol
  P1-P5 challenge precommits

FORMAL_COMPARISON_TARGETS_USED_DURING_LEDGER_CONSTRUCTION:
  none

POST_COMPARISON_LEDGER_CORRECTION_ALLOWED:
  no
~~~

## Reconstructed CH001

~~~text
point target:
  5

interval target:
  [19,23]

scenario conditional:
  warm -> 8
  cold -> 2
  no probability inference

probability:
  0.7 from explicit interface

update:
  P1=10
  P2=12
  P1 retained

readout:
  target 7
  no future-state identity inference

later validation:
  historical [4,6]
  observation 5
  pass on frozen standard
~~~

## Reconstructed CH002

~~~text
all six primary statuses:
  yes

all seven task terminals:
  yes

future-data leakage:
  original prospective claim not established
  no retroactive repair

effective validity:
  requested 10
  effective through 6
  evaluable NOT_ESTABLISHED

validation not yet due:
  issue terminal remains ESTABLISHED
~~~

## Reconstructed CH003

~~~text
METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11
EXACT_COLLAPSE_PAIRS:
  0
UNRESOLVED_BOUNDARY_PAIRS:
  0
PARTIAL_OVERLAP_NOT_COLLAPSE_PAIRS:
  11
SOURCE_HANDOFF_SEPARATION:
  established_at_fixture_level
~~~

## Reconstructed CH004

~~~text
BASELINE_ID:
  B0_GENERIC_VERSIONED_FORECASTER
EQUAL_INFORMATION_ACCESS:
  yes
G1-G6:
  BASELINE_MATCH
PREDICTION_METHOD_GAIN_STATUS:
  PREDICTION_NO_GAIN
~~~

## Reconstructed CH005

~~~text
BASELINE_ID:
  B1_STRONG_VERSIONED_FORECAST_ENGINE
EQUAL_INFORMATION_ACCESS:
  yes

model-version lock:
  retained

interval mapping:
  [5,11]

scenario probabilities:
  0.5 / 0.3 / 0.2

update lineage:
  retained

prospective/hindcast distinction:
  retained

Brier:
  0.09

G1-G7:
  BASELINE_MATCH

PREDICTION_METHOD_GAIN_STATUS:
  PREDICTION_NO_GAIN

STRONGEST_REASONABLE_BASELINE_PREDICTION:
  established_at_constructed_evidence_level
~~~

## Protocol-level reconstruction

~~~text
PROTOCOL_REVISION_REQUIRED:
  no
SHARED_CORE_REOPEN_REQUIRED:
  no
CURRENT_PREDICTION_EVIDENCE_STATUS:
  validation_in_progress
~~~

## Counter discipline

~~~text
DIRECT_PREDICTION_PILOTS_ATTEMPTED:
  retain 5
SUCCESSFUL_DIRECT_PREDICTION_PILOTS:
  retain 5
POSITIVE_PREDICTION_CASES:
  retain 1
NEGATIVE_OR_UNRESOLVED_PREDICTION_CASES:
  retain 1
METHOD_BOUNDARY_PREDICTION_CASES:
  retain 1
BASELINE_PREDICTION_CASES:
  retain 2
NO_GAIN_PREDICTION_CASES:
  retain 2
~~~

Only formal comparison may establish one reproducibility case and same-project deterministic retrace.

~~~text
FORMAL_COMPARISON_PERFORMED:
  no
CLAIM_RELEVANT_MISMATCH_COUNT:
  not yet scored
POST_COMPARISON_CORRECTIONS:
  prohibited
~~~
