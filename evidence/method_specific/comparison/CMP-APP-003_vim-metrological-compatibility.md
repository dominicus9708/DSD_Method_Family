# CMP-APP-003 Result / VIM Metrological Compatibility External Application

Status: **52/52 PASS**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**

## 1. Immutable chain

```text
PROTOCOL_CREATION_COMMIT:
  a1700d960e0b41dfe32bf85b6334448d9104100d

CMP-APP-003 PRECOMMIT:
  446aae3861c485c62828bba5432bae73aa7a9a45

CMP-APP-003 PRECOMMIT BLOB:
  7aa6aa1b3aa2e75a233e2f39c2ca681448ddd2ae
```

The precommit was re-read from its immutable commit before execution. No candidate identity, multiplier, correlation status, expected relation class, terminal status, or scoring rule was changed.

## 2. External source identity

```text
JCGM 200:2012
International Vocabulary of Metrology – Basic and general concepts and associated terms (VIM), 3rd edition
Entry 2.47: metrological compatibility of measurement results
DOI: 10.59161/JCGM200-2012
```

Frozen source rule used:

```text
metrological compatibility:
  absolute difference of measured values
  < chosen multiple × standard uncertainty of that difference

completely uncorrelated measurements:
  u_delta = sqrt(u1^2 + u2^2)

correlation:
  affects the standard uncertainty of the difference
```

The strict inequality and correlation dependence were retained exactly as precommitted.

## 3. Candidate execution

### M1 — compatible, uncorrelated, k=2

```text
x1 = 10.000
u1 = 0.003
x2 = 10.006
u2 = 0.004
u_delta = 0.005
difference = 0.006
threshold = 0.010
0.006 < 0.010 -> yes

SOURCE RESULT: METROLOGICALLY_COMPATIBLE
DSD CLASS: DIRECT_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

### M2 — same pair, k=1

```text
x1 = 10.000
u1 = 0.003
x2 = 10.006
u2 = 0.004
u_delta = 0.005
difference = 0.006
threshold = 0.005
0.006 < 0.005 -> no

SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
DSD CLASS: NONCORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

The same measurement-result pair changes verdict only because the chosen multiplier is part of the frozen criterion.

### M3 — exact threshold boundary

Exact decimal arithmetic:

```text
x1 = 10.000
u1 = 0.003
x2 = 10.010
u2 = 0.004
u_delta = sqrt(0.003^2 + 0.004^2) = 0.005 exactly
difference = 0.010 exactly
threshold = 2 × 0.005 = 0.010 exactly
0.010 < 0.010 -> no

SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
DSD CLASS: NONCORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

No floating-point approximation was allowed to convert equality at the boundary into a false pass.

### M4 — just inside threshold

```text
x1 = 10.000
u1 = 0.003
x2 = 10.009
u2 = 0.004
u_delta = 0.005
difference = 0.009
threshold = 0.010
0.009 < 0.010 -> yes

SOURCE RESULT: METROLOGICALLY_COMPATIBLE
DSD CLASS: DIRECT_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

### M5 — same central-value separation, small uncertainties

```text
x1 = 50.000
u1 = 0.001
x2 = 50.006
u2 = 0.001
u_delta = sqrt(0.000002) ~= 0.001414213562
threshold ~= 0.002828427125
difference = 0.006
0.006 < 0.002828427125 -> no

SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
DSD CLASS: NONCORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

### M6 — same central-value separation, larger uncertainties

```text
x1 = 50.000
u1 = 0.003
x2 = 50.006
u2 = 0.003
u_delta = sqrt(0.000018) ~= 0.004242640687
threshold ~= 0.008485281374
difference = 0.006
0.006 < 0.008485281374 -> yes

SOURCE RESULT: METROLOGICALLY_COMPATIBLE
DSD CLASS: DIRECT_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

M5/M6 preserve that the central-value separation alone does not determine compatibility.

### M7 — zero central-value difference

```text
x1 = 100.000
u1 = 0.0005
x2 = 100.000
u2 = 0.0010
u_delta ~= 0.001118033989
threshold ~= 0.001118033989
difference = 0
0 < threshold -> yes

SOURCE RESULT: METROLOGICALLY_COMPATIBLE
DSD CLASS: DIRECT_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

### M8 — correlation information unavailable

```text
x1 = 20.000
u1 = 0.003
x2 = 20.004
u2 = 0.003
k = 1
CORRELATION_STATUS = UNKNOWN_AND_CLAIM_RELEVANT
```

The frozen source states that correlation affects the standard uncertainty of the difference. The supplied record contains neither a correlation/covariance value nor authorization to assume complete lack of correlation.

Therefore:

```text
u_delta: not closed from supplied information
SOURCE RESULT: NOT_CLOSED_FROM_SUPPLIED_INFORMATION
DSD CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL: COMPARISON_UNDERDETERMINED
CONFORMANCE: CONFORMANT
GAIN: NOT_ASSESSED
```

No uncorrelated formula was silently substituted.

## 4. Preserved distinctions

```text
METROLOGICAL_COMPATIBILITY
!= STRICT_STRUCTURAL_EQUIVALENCE

METROLOGICAL_NONCOMPATIBILITY
!= PROOF_OF_DIFFERENT_PHYSICAL_OBJECT

CENTRAL_VALUE_DIFFERENCE_ALONE
!= COMPATIBILITY_VERDICT

SAME_PAIR + DIFFERENT_CHOSEN_MULTIPLE
-> possibly different verdict

THRESHOLD_EQUALITY
!= STRICT_SMALLER_THAN

UNKNOWN_CORRELATION
!= ASSUME_UNCORRELATED

COMPARISON_UNDERDETERMINED
!= APPLICATION_FAILURE
```

The application therefore extends external breadth beyond text normalization and protocol validator semantics into physical measurement-result comparison with uncertainty and criterion-closure dependence.

## 5. Scope discipline

No claim was made about:

```text
same physical object identity
same true quantity value
calibration correctness
measurement-system validity
instrument conformance
metrological traceability-chain validity
cause of incompatibility
which measurement is wrong
whether the measurand changed
practical acceptance for a specific industry
```

No hidden Transformation, Classification, Audit, or Lineage operation was introduced.

## 6. Three ledgers

M1-M7:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

M8:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

A correct underdetermined result is treated as protocol-conformant rather than forced into correspondence or noncorrespondence.

## 7. Precommitted scoring

```text
A. source / immutable precommit integrity:       8 / 8
B. candidate relation + terminal verdicts:      16 / 16
C. numerical / criterion discipline:            12 / 12
D. scope / closure discipline:                  10 / 10
E. evidence-count / interpretation discipline:   6 / 6

TOTAL: 52 / 52 PASS
FAILED: 0
APPLICATION_VERDICT: PASS
```

## 8. Evidence effect

```text
DIRECT_COMPARISON_PILOTS: 5  # unchanged
REPRODUCIBILITY_CASES: 1  # unchanged
DEDICATED_RETRACE_PASSES: 1  # unchanged

EXTERNAL_COMPARISON_APPLICATIONS: 3
EXTERNAL_COMPARISON_DOMAINS: 3
EXTERNAL_COMPARISON_APPLICATION_PASSES: 3

INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The three external domains are now:

```text
1. Unicode normalization / text-representation equivalence
2. HTTP ETag / protocol validator comparison semantics
3. VIM metrological compatibility / physical measurement-result comparison
```

## 9. Interpretation discipline

```text
EXTERNAL_PASS != METHOD_GAIN_PROOF
EXTERNAL_PASS != INDEPENDENT_VALIDATION
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_FAIL != METHOD_DELETION_PROOF
COMPATIBILITY != STRICT_EQUIVALENCE
UNDERDETERMINED != FAILURE
THREE_EXTERNAL_DOMAINS != AUTOMATIC_MATURITY_PROMOTION
```

## 10. Next

With three materially different external domains now populated without protocol revision pressure, the next Comparison step is a separately precommitted maturity audit. The audit must evaluate evidence breadth, protocol stability, baseline discipline, reproducibility classification, external-source fidelity, method-boundary preservation, and unresolved independent-validation limits without increasing direct evidence counts.
