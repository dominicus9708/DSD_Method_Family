# CMP-APP-003 Precommit / VIM Metrological Compatibility 외부 적용 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**

## 1. Evidence identity

```text
CASE_ID: CMP-APP-003
CASE_CLASS: external_application
EXTERNAL_DOMAIN: physical metrology / measurement-result compatibility
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
BASELINE: none
METHOD_GAIN: NOT_ASSESSED
```

Purpose: test whether DSD Comparison preserves an uncertainty-dependent external comparison criterion, including strict threshold behavior, criterion-parameter dependence, and an underdetermined case when correlation information needed for the uncertainty of a difference is unavailable.

## 2. Source lock

Primary source:

```text
JCGM 200:2012
International Vocabulary of Metrology – Basic and general concepts and associated terms (VIM), 3rd edition
Entry 2.47: metrological compatibility of measurement results
Publisher context: Joint Committee for Guides in Metrology / BIPM
DOI: 10.59161/JCGM200-2012
Official interactive entry:
  https://jcgm.bipm.org/vim/en/2.47.html
Official publication landing page:
  https://www.bipm.org/en/doi/10.59161/jcgm200-2012
```

Frozen source facts:

```text
S1 A set of measurement results for a specified measurand is metrologically compatible when
   the absolute difference of any pair of measured quantity values is smaller than some chosen
   multiple of the standard measurement uncertainty of that difference.

S2 For completely uncorrelated measurements, the standard measurement uncertainty of the
   difference is the root-mean-square sum of their standard measurement uncertainties.

S3 Correlation between measurements affects the standard measurement uncertainty of their
   difference; therefore individual standard uncertainties alone need not determine the
   compatibility result when correlation is claim-relevant but unavailable.

S4 The compatibility definition uses a strict "smaller than" relation; equality with the chosen
   threshold does not satisfy the frozen compatibility criterion.
```

No calibration validity, instrument conformance, common-cause diagnosis, traceability-chain validity, true-value claim, or physical identity claim is imported.

## 3. Frozen comparison rule

For candidates marked `UNCORRELATED`, define:

```text
u_delta = sqrt(u1^2 + u2^2)
threshold = k * u_delta
absolute_difference = abs(x1 - x2)

if absolute_difference < threshold:
  METROLOGICALLY_COMPATIBLE
else:
  NOT_METROLOGICALLY_COMPATIBLE
```

`k` is frozen per candidate as the chosen multiple permitted by the VIM definition. It is not inferred after execution.

For a candidate whose correlation status is frozen as `UNKNOWN_AND_CLAIM_RELEVANT`, no uncorrelated formula may be silently substituted.

## 4. Comparison task lock

```text
TASK_SCOPE:
  compare supplied measurement-result pairs only under the frozen VIM compatibility criterion

CLAIMED_OUTPUT_LEVEL:
  CORRESPONDENCE_CLASSIFICATION

TARGET_RESOLUTION:
  measured value + standard uncertainty + chosen multiplier + correlation-status sufficiency

COMPARISON_DIRECTIONALITY:
  symmetric

MAP_FAMILY_COVERAGE:
  exhaustive for each frozen pair/criterion instance

COMPARISON_ELEMENT_COVERAGE:
  measured values: exhaustive
  standard uncertainties: exhaustive
  chosen multiplier k: exhaustive
  correlation status: exhaustive or explicitly unresolved as frozen per candidate
  calibration/instrument/traceability properties: not_applicable

MAP_PROPERTY_REQUIREMENT_PROFILE:
  custom_supplied_criterion

REVERSE_DIRECTION_OR_INVERSE_POLICY:
  not_required

PRECOMPARISON_TRANSFORMATION_POLICY:
  none_required

ENCODING_OR_BRIDGE_RULE:
  none

LINEAGE_IDENTITY_CLAIM_POLICY:
  not_claimed

AGGREGATE_READOUTS_IF_ANY:
  none
```

## 5. Relation-class policy

This application does not equate metrological compatibility with DSD `STRICT_EQUIVALENT` or physical identity.

```text
VIM criterion satisfied
  -> DIRECT_CORRESPONDENCE

VIM criterion not satisfied with sufficient frozen information
  -> NONCORRESPONDENCE

VIM criterion cannot be closed because correlation information required for u_delta is unavailable
  -> UNDETERMINED_CORRESPONDENCE
```

Terminal policy:

```text
sufficient information + criterion evaluated
  -> COMPARISON_RESOLVED

substantive comparison possible but compatibility closure depends on missing correlation information
  -> COMPARISON_UNDERDETERMINED
```

Required guards:

```text
METROLOGICAL_COMPATIBILITY != STRICT_STRUCTURAL_EQUIVALENCE
METROLOGICAL_NONCOMPATIBILITY != PROOF_OF_DIFFERENT_PHYSICAL_OBJECT
CENTRAL_VALUE_DIFFERENCE_ALONE != COMPATIBILITY_VERDICT
SAME_PAIR + DIFFERENT_CHOSEN_MULTIPLE -> possibly different verdict
THRESHOLD_EQUALITY != STRICT_SMALLER_THAN
UNKNOWN_CORRELATION != ASSUME_UNCORRELATED
```

## 6. Frozen candidates

All numeric quantities below are expressed in the same arbitrary length unit and refer, for the task, to measurement results supplied as concerning the same specified measurand. No real-world instrument performance is claimed.

### M1 — compatible, uncorrelated, k=2

```text
x1 = 10.000
u1 = 0.003
x2 = 10.006
u2 = 0.004
CORRELATION_STATUS = UNCORRELATED
k = 2
u_delta = 0.005
difference = 0.006
threshold = 0.010
EXPECTED SOURCE RESULT: METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M2 — same pair, stricter chosen multiple k=1

```text
x1 = 10.000
u1 = 0.003
x2 = 10.006
u2 = 0.004
CORRELATION_STATUS = UNCORRELATED
k = 1
u_delta = 0.005
difference = 0.006
threshold = 0.005
EXPECTED SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M3 — exact threshold boundary

```text
x1 = 10.000
u1 = 0.003
x2 = 10.010
u2 = 0.004
CORRELATION_STATUS = UNCORRELATED
k = 2
u_delta = 0.005
difference = 0.010
threshold = 0.010
EXPECTED SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M4 — just inside threshold

```text
x1 = 10.000
u1 = 0.003
x2 = 10.009
u2 = 0.004
CORRELATION_STATUS = UNCORRELATED
k = 2
u_delta = 0.005
difference = 0.009
threshold = 0.010
EXPECTED SOURCE RESULT: METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M5 — same central-value separation, small uncertainties

```text
x1 = 50.000
u1 = 0.001
x2 = 50.006
u2 = 0.001
CORRELATION_STATUS = UNCORRELATED
k = 2
u_delta = sqrt(0.000002) ~= 0.00141421356
difference = 0.006
threshold ~= 0.00282842712
EXPECTED SOURCE RESULT: NOT_METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: NONCORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M6 — same central-value separation, larger uncertainties

```text
x1 = 50.000
u1 = 0.003
x2 = 50.006
u2 = 0.003
CORRELATION_STATUS = UNCORRELATED
k = 2
u_delta = sqrt(0.000018) ~= 0.00424264069
difference = 0.006
threshold ~= 0.00848528137
EXPECTED SOURCE RESULT: METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M7 — zero central-value difference

```text
x1 = 100.000
u1 = 0.0005
x2 = 100.000
u2 = 0.0010
CORRELATION_STATUS = UNCORRELATED
k = 1
u_delta ~= 0.00111803399
difference = 0
threshold ~= 0.00111803399
EXPECTED SOURCE RESULT: METROLOGICALLY_COMPATIBLE
EXPECTED DSD CLASS: DIRECT_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_RESOLVED
EXPECTED CONFORMANCE: CONFORMANT
```

### M8 — correlation information unavailable

```text
x1 = 20.000
u1 = 0.003
x2 = 20.004
u2 = 0.003
CORRELATION_STATUS = UNKNOWN_AND_CLAIM_RELEVANT
k = 1

The VIM notes that correlation changes the standard uncertainty of the difference.
The task does not supply covariance/correlation or a source-authorized uncorrelated assumption.

EXPECTED SOURCE RESULT: NOT_CLOSED_FROM_SUPPLIED_INFORMATION
EXPECTED DSD CLASS: UNDETERMINED_CORRESPONDENCE
EXPECTED TERMINAL: COMPARISON_UNDERDETERMINED
EXPECTED CONFORMANCE: CONFORMANT
```

## 7. Scope exclusions

The application must not infer:

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

## 8. Three-ledger lock

For M1-M7:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

For M8:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No baseline is supplied, so neither `GAIN_ESTABLISHED` nor `NO_GAIN` may be asserted.

## 9. Precommitted scoring

Total required checks: **52**.

```text
A. source / immutable precommit integrity:       8
B. candidate relation + terminal verdicts:      16
C. numerical / criterion discipline:            12
D. scope / closure discipline:                  10
E. evidence-count / interpretation discipline:   6
```

Detailed checks:

```text
A1 Protocol remains v0.1 at frozen protocol commit.
A2 JCGM publication identity remains JCGM 200:2012.
A3 VIM entry remains 2.47.
A4 strict "smaller than" criterion retained.
A5 uncorrelated RMS uncertainty rule retained.
A6 correlation-dependence note retained.
A7 M1-M8 identities unchanged after precommit.
A8 no post-hoc candidate, multiplier, or correlation-status replacement.

B1-B8 exact DSD relation class for M1-M8.
B9-B15 M1-M7 exact COMPARISON_RESOLVED terminal.
B16 M8 exact COMPARISON_UNDERDETERMINED terminal.

C1 M1 difference 0.006 < threshold 0.010.
C2 M2 same pair differs only by frozen k and is not compatible.
C3 M3 equality at 0.010 is not treated as smaller-than.
C4 M4 0.009 < 0.010 retained.
C5 M5 small-uncertainty threshold approximately 0.00282842712 retained.
C6 M5 is not compatible.
C7 M6 larger-uncertainty threshold approximately 0.00848528137 retained.
C8 M6 is compatible.
C9 M7 zero difference is compatible under positive threshold.
C10 central-value difference alone is not used as the verdict rule.
C11 M8 does not silently assume uncorrelated measurements.
C12 compatibility outcomes are not upgraded to STRICT_EQUIVALENT.

D1 metrological compatibility is not physical-object identity.
D2 metrological noncompatibility is not a causal diagnosis.
D3 no calibration-validity claim introduced.
D4 no traceability-chain claim introduced.
D5 no instrument-conformance claim introduced.
D6 no hidden transformation introduced.
D7 no lineage claim introduced.
D8 M8 preserves unresolved correlation rather than fabricating a number.
D9 all frozen scope exclusions retained.
D10 source truth, Comparison conformance, and method gain remain separate ledgers.

E1 external application count increments by exactly one on PASS.
E2 external domain count increments by exactly one on PASS.
E3 external application pass count increments by exactly one on PASS.
E4 direct constructed-pilot count remains unchanged.
E5 reproducibility counts remain unchanged.
E6 independent validation and maturity remain unchanged until a separate maturity audit.
```

Decision:

```text
52/52 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

## 10. Evidence-count lock before execution

```text
DIRECT_COMPARISON_PILOTS: 5
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

A PASS may change only:

```text
EXTERNAL_COMPARISON_APPLICATIONS: 2 -> 3
EXTERNAL_COMPARISON_DOMAINS: 2 -> 3
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2 -> 3
```

## 11. Registry discipline

```text
EXTERNAL_PASS != METHOD_GAIN_PROOF
EXTERNAL_PASS != INDEPENDENT_VALIDATION
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_FAIL != METHOD_DELETION_PROOF
COMPATIBILITY != STRICT_EQUIVALENCE
UNDERDETERMINED != FAILURE
```
