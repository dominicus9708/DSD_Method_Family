# PRED-CH-006 — Deterministic Same-Project Prediction Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-10-06**

## Frozen derivation artifacts

~~~text
P0 Prediction Protocol v0.1
  commit: 1a03a96e270f0d975710f5d530a8b1dbf5105bb0
  blob:   54de0673e41fe46f88dd78a56c6150e8d97cfc3c

P1 PRED-CH-001 precommit
  commit: 70660aa399709faff8eab25a15fb9e918857f29c
  blob:   758988f687ffaa04a33936d8d6947df10df983d0

P2 PRED-CH-002 precommit
  commit: 0b4aa64207a3432cecf0d38dab21e87b26745c16
  blob:   b1cff116482a9d155c5b2a69ffa9da55ab65f5c5

P3 PRED-CH-003 precommit
  commit: 2d6a01eb379020ebcd227fcece00f52e99f48862
  blob:   693c21c851dbd0ea6bff1a3ae61a1df18c09f65e

P4 PRED-CH-004 precommit
  commit: ea475b3eb389761ff476e3a7f5696a2044d88654
  blob:   2cb8e963bbda7ca8e67822310ffebb9bf6cefca9

P5 PRED-CH-005 precommit
  commit: 742a1bc46bd240ad72c0c8d596cd663eda4ba906
  blob:   5fbff8ae542f32ea71c0b03755191c8e1df3a8c8
~~~

Historical result artifacts may be used only after the retrace ledger is committed.

## Frozen comparison targets

~~~text
T1 PRED-CH-001
  commit: 4a674e75312b16dcda1635364f2dcdaee454c641
  blob:   c4000ea9b3b6461a839720244236b7488a320211

T2 PRED-CH-002
  commit: c1a9b05924918ad77b131bc872f136115ef99108
  blob:   a75bd1507481d02b52fbb4cf09e632950270532d

T3 PRED-CH-003
  commit: f3bdcca9fa91619a443b92418658a5f0610f2503
  blob:   e62abcf3a4bfb60a16c8397967c36617b907666d

T4 PRED-CH-004
  commit: cefbd117fae8ab54042d188bd179d1d5c3a7109c
  blob:   59f54e5670dfb500874938cf47114fdf66f211b7

T5 PRED-CH-005
  commit: 5bbf237d177eb51d482db7fba14ff7cfd1898f71
  blob:   bfea17d3bf5029b842f00e4c8cdce55e90817247
~~~

## Retrace targets

~~~text
CH001:
  point 5
  interval [19,23]
  scenario warm=8 / cold=2 without probability invention
  probability 0.7 from explicit interface
  P1=10 then P2=12 with P1 retained
  readout target 7 without state-identity inference
  later validation pass for [4,6] with observation 5

CH002:
  all six primary statuses
  all seven task terminals
  future-data leakage not repaired
  horizon effective support through 6
  validation-not-yet-due separate from issue terminal

CH003:
  11 neighboring-method pairs
  exact collapse 0
  unresolved 0
  partial-overlap-not-collapse 11

CH004:
  B0 baseline
  six gain axes BASELINE_MATCH
  PREDICTION_NO_GAIN

CH005:
  B1 strongest-reasonable constructed baseline
  seven gain axes BASELINE_MATCH
  PREDICTION_NO_GAIN
  Brier score 0.09
~~~

## Sequence lock

~~~text
1 freeze this precommit
2 construct retrace ledger from P0-P5 only
3 commit ledger
4 compare against T1-T5
5 record every claim-relevant mismatch
6 do not alter ledger after comparison
~~~

## Frozen score

~~~text
artifact / anti-post-hoc integrity: 12
CH001 reconstruction: 12
CH002 reconstruction: 14
CH003 boundary reconstruction: 10
CH004 baseline reconstruction: 10
CH005 baseline reconstruction: 10
final verdict: 2

TOTAL_REQUIRED_CHECKS:
  70
PASS_THRESHOLD:
  70/70
~~~

On full pass:

~~~text
REPRODUCIBILITY_CASES:
  0 -> 1
SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once
CLAIM_RELEVANT_MISMATCHES:
  0 required
POST_COMPARISON_CORRECTIONS:
  0 required
~~~

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~

Next on full pass: PRED-AUD-001 frozen-axis internal-standardization audit.
