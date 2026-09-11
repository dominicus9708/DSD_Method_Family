# CMP-CH-006 Result / DSD 비교론 CMP-APP-001 Deterministic Same-Project Retrace 결과

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Retrace target: **CMP-APP-001**

## 1. Immutable chain

```text
PROTOCOL_COMMIT:
  a1700d960e0b41dfe32bf85b6334448d9104100d

TARGET_PRECOMMIT_COMMIT:
  e1a109b9e4515336b4ee22c4d8ff216d4fd21705
TARGET_PRECOMMIT_BLOB:
  640f2b5e7cf9b990a07a2e3db542b114d655122f

TARGET_RESULT_COMMIT:
  b64cd882047b45c4caaaf27cbc414c0b9b44e2e6

RETRACE_PRECOMMIT_COMMIT:
  ffd374fb0b8bfd284b9cbd343d3dcf07ba9cfbe1
RETRACE_PRECOMMIT_BLOB:
  80b6d0df29da3eea2a8ca78184ba9787acb4899c
```

The retrace precommit was fetched by its immutable commit before execution. Reconstruction used the frozen Protocol and frozen `CMP-APP-001` precommit record. The historical target result was consulted only after reconstruction for equality scoring.

No current Unicode source, later normalization revision, alternate library output, or new semantic relation was imported.

## 2. Source identity reconstruction

Reconstructed exactly:

```text
Unicode Standard Annex #15: Unicode Normalization Forms
Unicode version: 17.0.0
Revision: 57
Date: 2025-07-30
Publisher: Unicode Consortium
```

Frozen exclusions were retained:

```text
Unicode confusability
locale collation
grapheme-cluster identity
identifier security
rendering-engine behavior
language-semantic equality
```

## 3. Criterion reconstruction

```text
U1 -> CANONICAL_EQUIVALENCE_VIA_NFC
U2 -> BINARY_IDENTITY
U3 -> CANONICAL_EQUIVALENCE_VIA_NFC
U4 -> COMPATIBILITY_EQUIVALENCE_VIA_NFKC
U5 -> CANONICAL_EQUIVALENCE_VIA_NFC
U6 -> CANONICAL_EQUIVALENCE_VIA_NFC
```

The retrace preserved criterion provenance rather than treating the final relation class as intrinsic to the subject pair.

## 4. Candidate reconstruction

### U1

```text
LEFT:  U+00C7 Ç
RIGHT: U+0043 C + U+0327 COMBINING CEDILLA
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
RAW_BINARY_IDENTITY: no
NORMALIZED_CANONICAL_COMPARISON: equal
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

### U2

```text
LEFT:  U+00C7 Ç
RIGHT: U+0043 C + U+0327 COMBINING CEDILLA
CRITERION: BINARY_IDENTITY
EXACT_CODE_POINT_SEQUENCE_IDENTITY: no
CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen binary criterion
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

### U3

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
SOURCE_RELATION: compatibility equivalence
CANONICAL_EQUIVALENCE: not established
CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen canonical criterion
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

### U4

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: COMPATIBILITY_EQUIVALENCE_VIA_NFKC
NORMALIZED_COMPATIBILITY_COMPARISON: equal
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

### U5

```text
LEFT:  U+AC00 가
RIGHT: U+1100 ᄀ + U+1161 ᅡ
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
RAW_BINARY_IDENTITY: no
NORMALIZED_CANONICAL_COMPARISON: equal
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

### U6

```text
LEFT:  q + COMBINING DOT ABOVE + COMBINING DOT BELOW
RIGHT: q + COMBINING DOT BELOW + COMBINING DOT ABOVE
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
RAW_BINARY_IDENTITY: no
CANONICAL_ORDERING/NORMALIZATION: equal normalized sequence
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

## 5. Cross-case equality against historical result

The reconstructed relation/criterion matrix is exactly:

```text
U1 ENCODED_CORRESPONDENCE     / canonical via NFC
U2 NONCORRESPONDENCE          / binary identity
U3 NONCORRESPONDENCE          / canonical via NFC
U4 ENCODED_CORRESPONDENCE     / compatibility via NFKC
U5 ENCODED_CORRESPONDENCE     / canonical via NFC
U6 ENCODED_CORRESPONDENCE     / canonical via NFC
```

Historical `CMP-APP-001` records the same matrix, the same terminal status for all six cases, and the same conformance ledger.

Preserved distinctions:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
NFC_EQUIVALENCE_RESULT != NFKC_EQUIVALENCE_RESULT_IN_GENERAL
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

## 6. Ledger equality

```text
TERMINAL_COMPARISON_STATUS:
  U1-U6 -> COMPARISON_RESOLVED

COMPARISON_PROTOCOL_CONFORMANCE:
  U1-U6 -> CONFORMANT

COMPARISON_METHOD_GAIN_STATUS:
  NOT_ASSESSED
```

Not fabricated:

```text
FIRST_BRANCH_POINT
LINEAGE_IDENTITY
AGGREGATE_READOUT
INDEPENDENT_BASELINE
GAIN_ESTABLISHED
NO_GAIN
```

## 7. Precommitted scoring

```text
A. immutable chain / source identity        8 / 8 PASS
B. candidate reconstruction               18 / 18 PASS
C. criterion / provenance reconstruction  10 / 10 PASS
D. ledger / scope equality                 7 / 7 PASS
E. reproducibility classification          5 / 5 PASS

PRECOMMITTED_REQUIRED_CHECKS:              48
PASSED:                                     48
FAILED:                                      0
RETRACE_VERDICT:                           PASS
```

No check was deleted, weakened, or reclassified after execution.

## 8. Reproducibility classification

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This is explicitly not:

```text
independent replication
blinded reproduction
independent evaluator validation
```

## 9. Evidence counters after retrace

Unchanged:

```text
DIRECT_COMPARISON_PILOTS: 5
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
```

Changed exactly as precommitted:

```text
REPRODUCIBILITY_CASES: 0 -> 1
DEDICATED_RETRACE_PASSES: 0 -> 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

Still not established:

```text
INDEPENDENT_REPLICATION
INDEPENDENT_COMPARISON_VALIDATION
MEASURED_PRACTICAL_SUPERIORITY
```

Maturity remains:

```text
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 10. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The retrace reproduced criterion-dependent correspondence without needing a protocol change.

## 11. Registry discipline

```text
RETRACE_PASS != INDEPENDENT_REPLICATION
RETRACE_PASS != INDEPENDENT_VALIDATION
RETRACE_PASS != METHOD_SURVIVAL_PROOF
RETRACE_FAIL != METHOD_DELETION_PROOF
REPRODUCIBILITY != METHOD_GAIN
```

## 12. Next

Proceed to materially different external Comparison domains. The next external application should not merely repeat Unicode/string-normalization semantics; it should test Comparison under a distinct external comparison structure before maturity audit.
