# CTRL-CH-006 — Deterministic Same-Project Control Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-10-06**

## Frozen derivation artifacts

~~~text
P0 Control Protocol v0.1
  commit: cda84e4298be81993a571f8f1277b3c7530c6057
  blob:   bb22a9b8ebca8d11fd29ae9eb072021e45130881

P1 CTRL-CH-001 precommit
  commit: e8a8098de206a50dc613f243e7c262595fe67cb4
  blob:   6266f83c410e598bacb6e57e2bb16725d65360f5

P2 CTRL-CH-002 precommit
  commit: b06e81a080cf204c9c6d84024f0fe395043f0de5
  blob:   eb88a123b83b88c9c990f036ad365b1ec4e82449

P3 CTRL-CH-003 precommit
  commit: e684473b906a4e1dd0e0bf56a096b4a4dbf47ff3
  blob:   552020b7ca07f7ff3eaa19818e910845621a6a48

P4 CTRL-CH-004 precommit
  commit: d90589a1527e082037a2777904c7e4f27cae14c8
  blob:   8191ae6b13756d5b8df3b3685b5376fe412190cc

P5 CTRL-CH-005 precommit
  commit: 86b9641ebfe495b982da7344cab9801a2ed6ff99
  blob:   c66208a17f2e91faad13e79a454350c9c2073fd4
~~~

Historical result artifacts may be used only after the retrace ledger is committed.

## Frozen comparison targets

~~~text
T1 CTRL-CH-001
  commit: 727157f99b32f18bff65668fbbed4b01d8dba2da
  blob:   6c116ac1df1bf874e76de2fc104f1ed29c6cf904

T2 CTRL-CH-002
  commit: 0dd8c01f7001ef50cfc439b57a63b62a0874372d
  blob:   23afb5e113641088ae9b53db6a046c48d5349441

T3 CTRL-CH-003
  commit: d0d5e841b7e4497139d3aa662622e91c4a31ac24
  blob:   35fdb5d5d6c8bd6d7bd0bcf92866d2053fc6a895

T4 CTRL-CH-004
  commit: 4d1a70b96e33463389fe37d7be475b6c7bcc748d
  blob:   f29de70fd288464841b6eb60683d9ba46bd6784e

T5 CTRL-CH-005
  commit: 2a53c45174b0c0dc86af87e63e3e5c35d832a07b
  blob:   aa816888783928539fa00a813fffa8f11e79747d
~~~

## Retrace targets

~~~text
CH001:
  one-step action 2
  feedback policy retained as feedback
  open-loop [1,1] retained as open-loop
  hard action 3 excluded
  typed hybrid transition and lineage retained
  readout target 7 without full-state identity
  P1 -> P2 update with P1 immutable

CH002:
  all six primary statuses
  all seven task terminals
  known prerequisite failure != blocked
  unavailable observation -> blocked
  unreachable target -> not established
  terminal precedence preserved

CH003:
  10 neighboring-method pairs
  exact collapse 0
  unresolved 0
  partial-overlap-not-collapse 10

CH004:
  B0 baseline
  six gain axes BASELINE_MATCH
  CONTROL_NO_GAIN

CH005:
  B1 strongest-reasonable constructed baseline
  seven gain axes BASELINE_MATCH
  CONTROL_NO_GAIN
~~~

## Sequence lock

~~~text
1 freeze this precommit
2 construct retrace ledger from P0-P5 only
3 commit ledger
4 compare frozen ledger with T1-T5
5 no post-comparison ledger correction
~~~

## Frozen scoring

~~~text
artifact / anti-post-hoc integrity:
  12
CH001 reconstruction:
  12
CH002 reconstruction:
  14
CH003 boundary reconstruction:
  10
CH004 baseline reconstruction:
  10
CH005 baseline reconstruction:
  10
final verdict:
  2

TOTAL_REQUIRED_CHECKS:
  70
PASS_THRESHOLD:
  70/70
PARTIAL_PASS_ALLOWED:
  no
~~~

On full pass:

~~~text
REPRODUCIBILITY_CASES:
  0 -> 1
SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once
CLAIM_RELEVANT_MISMATCHES:
  0
POST_COMPARISON_CORRECTIONS:
  0
~~~

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
~~~

Next on full pass: CTRL-AUD-001 frozen-axis internal-standardization audit.
