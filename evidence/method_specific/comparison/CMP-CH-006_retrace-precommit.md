# CMP-CH-006 Precommit / DSD 비교론 CMP-APP-001 Deterministic Same-Project Retrace 사전동결

Status: **PRECOMMITTED — retrace not yet executed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**

## 1. Evidence identity

```text
CASE_ID: CMP-CH-006
CASE_CLASS: deterministic_same_project_retrace
RETRACE_TARGET: CMP-APP-001
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific_reproducibility
BASELINE: none
METHOD_GAIN: NOT_ASSESSED
```

Purpose: test whether the already frozen `CMP-APP-001` Unicode normalization application can be reconstructed deterministically from the frozen project record without reopening the task, changing the criterion, importing new source relations, or consulting the original result as a decision oracle during reconstruction.

## 2. Immutable chain lock

```text
PROTOCOL_PATH:
  methods/06_comparison/PROTOCOL_v0.1.md
PROTOCOL_COMMIT:
  a1700d960e0b41dfe32bf85b6334448d9104100d

TARGET_PRECOMMIT_PATH:
  evidence/method_specific/comparison/CMP-APP-001_precommit.md
TARGET_PRECOMMIT_COMMIT:
  e1a109b9e4515336b4ee22c4d8ff216d4fd21705
TARGET_PRECOMMIT_BLOB:
  640f2b5e7cf9b990a07a2e3db542b114d655122f

TARGET_RESULT_PATH:
  evidence/method_specific/comparison/CMP-APP-001_unicode-normalization-comparison.md
TARGET_RESULT_COMMIT:
  b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
```

The retrace execution must use the frozen Protocol and target precommit as the reconstruction basis. The target result is used only after reconstruction to score equality against the historical record.

No live revision of Unicode, later UAX #15 edition, alternate normalization library, new relation, or changed criterion may replace the frozen source lock.

## 3. Frozen source identity to reconstruct

```text
Unicode Standard Annex #15: Unicode Normalization Forms
Unicode version: 17.0.0
Revision: 57
Date: 2025-07-30
Publisher: Unicode Consortium
```

Frozen source-fact set to retain:

```text
S1 canonical equivalence is distinct from compatibility equivalence.
S2 NFC/NFD preserve canonical equivalence.
S3 NFKC/NFKD also fold compatibility-equivalent strings.
S4 normalized binary comparison can determine the corresponding frozen equivalence.
S5 Ç <-> C + COMBINING CEDILLA is canonical-equivalence example.
S6 reordered dot-above/dot-below combining sequence is canonical-equivalence example.
S7 가 <-> ᄀ + ᅡ is canonical-equivalence example.
S8 ① -> 1 is compatibility-equivalence example.
```

Scope exclusions to retain exactly:

```text
Unicode confusability
locale collation
grapheme-cluster identity
identifier security
rendering-engine behavior
language-semantic equality
```

## 4. Frozen criterion reconstruction

The retrace must reconstruct the same criterion assignment, not merely the same final label.

```text
U1 -> CANONICAL_EQUIVALENCE_VIA_NFC
U2 -> BINARY_IDENTITY
U3 -> CANONICAL_EQUIVALENCE_VIA_NFC
U4 -> COMPATIBILITY_EQUIVALENCE_VIA_NFKC
U5 -> CANONICAL_EQUIVALENCE_VIA_NFC
U6 -> CANONICAL_EQUIVALENCE_VIA_NFC
```

Required criterion guards:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
NFC_EQUIVALENCE_RESULT != NFKC_EQUIVALENCE_RESULT_IN_GENERAL
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

## 5. Frozen candidate reconstruction

### U1

```text
LEFT:  U+00C7 Ç
RIGHT: U+0043 C + U+0327 COMBINING CEDILLA
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
EXPECTED RETRACE:
  raw binary identity: no
  normalized canonical comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

### U2

```text
LEFT:  U+00C7 Ç
RIGHT: U+0043 C + U+0327 COMBINING CEDILLA
CRITERION: BINARY_IDENTITY
EXPECTED RETRACE:
  exact code-point sequence identity: no
  CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen binary criterion
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

### U3

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
EXPECTED RETRACE:
  compatibility relation retained
  canonical equivalence not established
  CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen canonical criterion
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

### U4

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: COMPATIBILITY_EQUIVALENCE_VIA_NFKC
EXPECTED RETRACE:
  normalized compatibility comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

### U5

```text
LEFT:  U+AC00 가
RIGHT: U+1100 ᄀ + U+1161 ᅡ
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
EXPECTED RETRACE:
  raw binary identity: no
  normalized canonical comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

### U6

```text
LEFT:  q + COMBINING DOT ABOVE + COMBINING DOT BELOW
RIGHT: q + COMBINING DOT BELOW + COMBINING DOT ABOVE
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
EXPECTED RETRACE:
  raw binary identity: no
  canonical ordering/normalization: equal normalized sequence
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
  CONFORMANCE: CONFORMANT
```

## 6. Frozen ledger reconstruction

The retrace must reproduce:

```text
TERMINAL_COMPARISON_STATUS:
  COMPARISON_RESOLVED for U1-U6

COMPARISON_PROTOCOL_CONFORMANCE:
  CONFORMANT for U1-U6

COMPARISON_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

It must not fabricate:

```text
FIRST_BRANCH_POINT
LINEAGE_IDENTITY
AGGREGATE_READOUT
INDEPENDENT_BASELINE
GAIN_ESTABLISHED
NO_GAIN
```

## 7. Retrace equality criterion

A retrace item matches the historical `CMP-APP-001` record only if all claim-relevant fields agree:

```text
candidate identity
code-point pair
criterion assignment
raw-vs-normalized distinction
correspondence class
terminal status
protocol conformance
criterion provenance
scope exclusions
method-gain ledger
```

A matching final relation label with changed criterion provenance counts as **FAIL**, not reproduction.

## 8. Precommitted scoring

Total required checks: **48**.

```text
A. immutable chain / source identity:        8
B. candidate reconstruction:               18
C. criterion / provenance reconstruction:  10
D. ledger / scope equality:                 7
E. reproducibility classification:          5
```

Detailed checks:

```text
A1 protocol commit exact
A2 target precommit commit exact
A3 target precommit blob exact
A4 target result commit exact
A5 Unicode version exact
A6 UAX revision/date exact
A7 candidate set U1-U6 exact
A8 no live/new source relation imported

B1-B6 exact U1-U6 correspondence class
B7-B12 exact U1-U6 terminal COMPARISON_RESOLVED
B13-B18 exact U1-U6 protocol conformance CONFORMANT

C1 U1 raw inequality retained
C2 U1 canonical equivalence retained
C3 U2 same pair / binary criterion retained
C4 U3 compatibility-only relation not upgraded to canonical
C5 U4 NFKC compatibility criterion retained
C6 U5 Hangul canonical equivalence retained
C7 U6 combining-order canonical equivalence retained
C8 criterion provenance retained for every case
C9 encoded normalization cases not relabelled direct/literal
C10 same-pair/different-criterion distinction retained

D1 method gain remains NOT_ASSESSED
D2 no first-branch claim fabricated
D3 no lineage claim fabricated
D4 no aggregate claim fabricated
D5 excluded Unicode relation families remain excluded
D6 constructed direct-pilot count unchanged
D7 external application/domain/pass counts unchanged by retrace

E1 retrace classified deterministic_same_project
E2 REPRODUCIBILITY_CASES increments by exactly one on PASS
E3 DEDICATED_RETRACE_PASSES increments by exactly one on PASS
E4 independent replication remains not established
E5 independent validation and maturity remain unchanged
```

Decision:

```text
48/48 -> RETRACE_VERDICT: PASS
otherwise -> RETRACE_VERDICT: FAIL
```

## 9. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 5
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 0
DEDICATED_RETRACE_PASSES: 0
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

A 48/48 PASS may change only:

```text
REPRODUCIBILITY_CASES: 0 -> 1
DEDICATED_RETRACE_PASSES: 0 -> 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

It does not increment constructed or external application counts and does not establish independent replication, independent validation, practical superiority, method maturity, or permanent method independence.

## 10. Registry discipline

```text
RETRACE_PASS != INDEPENDENT_REPLICATION
RETRACE_PASS != INDEPENDENT_VALIDATION
RETRACE_PASS != METHOD_SURVIVAL_PROOF
RETRACE_FAIL != METHOD_DELETION_PROOF
REPRODUCIBILITY != METHOD_GAIN
```
