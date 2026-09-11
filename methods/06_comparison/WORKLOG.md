# DSD Comparison Worklog / DSD 비교론 작업 기록

## 2026-09-10 — Planning Step 1
Created the Comparison task-interface and evidence paths.

## 2026-09-10 — Planning Step 2
Ran 16 pre-protocol boundary attacks. Eleven required no refinement and five required non-breaking refinement. No boundary collapse or fundamental interface failure was found.

## 2026-09-10 — Planning Step 4
Established `PROTOCOL_v0.1.md` at commit `a1700d960e0b41dfe32bf85b6334448d9104100d`. Protocol creation added no direct pilot.

## 2026-09-10 — Step 5 CMP-CH-001
```text
40/40 PASS
positive relation-separation challenge
```

## 2026-09-10 — Step 6 CMP-CH-002
```text
48/48 PASS
negative/failure terminal distinction
```

## 2026-09-10 — Step 7 CMP-CH-003
```text
48/48 PASS
direct method-boundary challenge
```

## 2026-09-11 — Step 8 CMP-CH-004
```text
50/50 PASS / NO_GAIN
competent baseline B0_TYPED_COMPARISON_LEDGER
```

## 2026-09-11 — Step 9 CMP-CH-005
```text
60/60 PASS / NO_GAIN
strongest-reasonable baseline B1_STRONG_TYPED_COMPARISON_ENGINE
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

## 2026-09-11 — Step 10 CMP-APP-001 Unicode normalization external application

Status: **42/42 PASS**

```text
PRECOMMIT: e1a109b9e4515336b4ee22c4d8ff216d4fd21705
PRECOMMIT BLOB: 640f2b5e7cf9b990a07a2e3db542b114d655122f
RESULT: b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
SOURCE: Unicode Standard Annex #15, Unicode 17.0.0 Revision 57
```

```text
U1 Ç vs C+cedilla / NFC canonical -> ENCODED / RESOLVED
U2 same pair / binary identity -> NONCORRESPONDENCE / RESOLVED
U3 ① vs 1 / NFC canonical -> NONCORRESPONDENCE / RESOLVED
U4 same pair / NFKC compatibility -> ENCODED / RESOLVED
U5 가 vs ᄀ+ᅡ / NFC canonical -> ENCODED / RESOLVED
U6 combining-mark ordering / NFC canonical -> ENCODED / RESOLVED
ALL CONFORMANCE: CONFORMANT
METHOD GAIN: NOT_ASSESSED
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5  # unchanged
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

Interpretation discipline remains:

```text
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_PASS != METHOD_GAIN_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

## 2026-09-11 — Step 11 CMP-CH-006 deterministic same-project retrace

Status: **48/48 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-CH-006_retrace-precommit.md
commit ffd374fb0b8bfd284b9cbd343d3dcf07ba9cfbe1
blob 80b6d0df29da3eea2a8ca78184ba9787acb4899c
```

Result:

```text
evidence/method_specific/comparison/CMP-CH-006_deterministic-retrace.md
commit 35d0a8d7a22c19593bae8f45843668f46d775a0a
```

Immutable target chain:

```text
PROTOCOL: a1700d960e0b41dfe32bf85b6334448d9104100d
CMP-APP-001 PRECOMMIT: e1a109b9e4515336b4ee22c4d8ff216d4fd21705
CMP-APP-001 PRECOMMIT BLOB: 640f2b5e7cf9b990a07a2e3db542b114d655122f
CMP-APP-001 RESULT: b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
```

Reconstructed exactly:

```text
U1 ENCODED_CORRESPONDENCE / canonical via NFC / RESOLVED / CONFORMANT
U2 NONCORRESPONDENCE / binary identity / RESOLVED / CONFORMANT
U3 NONCORRESPONDENCE / canonical via NFC / RESOLVED / CONFORMANT
U4 ENCODED_CORRESPONDENCE / compatibility via NFKC / RESOLVED / CONFORMANT
U5 ENCODED_CORRESPONDENCE / canonical via NFC / RESOLVED / CONFORMANT
U6 ENCODED_CORRESPONDENCE / canonical via NFC / RESOLVED / CONFORMANT
```

Criterion provenance, raw-vs-normalized distinction, scope exclusions, and `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED` were reproduced. No first-branch, lineage, aggregate, or independent-baseline claim was added.

Precommitted score:

```text
A immutable chain / source identity        8/8
B candidate reconstruction               18/18
C criterion / provenance reconstruction  10/10
D ledger / scope equality                 7/7
E reproducibility classification          5/5
TOTAL                                    48/48 PASS
```

Evidence effect:

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
DIRECT_COMPARISON_PILOTS: 5  # unchanged
EXTERNAL_COMPARISON_APPLICATIONS: 1  # unchanged
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Interpretation discipline:

```text
RETRACE_PASS != INDEPENDENT_REPLICATION
RETRACE_PASS != INDEPENDENT_VALIDATION
RETRACE_PASS != METHOD_SURVIVAL_PROOF
RETRACE_FAIL != METHOD_DELETION_PROOF
REPRODUCIBILITY != METHOD_GAIN
```

## 2026-09-11 — Step 12 CMP-APP-002 HTTP ETag comparison semantics

Status: **48/48 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-APP-002_precommit.md
commit f77ddb2a384b15d6a1fe041c4be5c177c52b3623
blob 7478867a0013cb94ae9a7e581a77548263cbe966
```

Result:

```text
evidence/method_specific/comparison/CMP-APP-002_http-etag-comparison.md
commit fbba59a974482ff7469d7cec5b4ce63a85c2ae61
```

External source:

```text
RFC 9110 — HTTP Semantics
June 2022
§8.8.3.2 strong/weak entity-tag comparison
§13.1.1 If-Match -> strong comparison
§13.1.2 If-None-Match -> weak comparison
```

Execution:

```text
H1 W/"1" vs W/"1" / strong -> NONCORRESPONDENCE / RESOLVED
H2 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H3 W/"1" vs "1" / strong -> NONCORRESPONDENCE / RESOLVED
H4 same pair / weak -> DIRECT_CORRESPONDENCE / RESOLVED
H5 "1" vs "1" / strong -> DIRECT_CORRESPONDENCE / RESOLVED
H6 W/"1" vs W/"2" / weak -> NONCORRESPONDENCE / RESOLVED
H7 If-Match context -> strong -> NONCORRESPONDENCE / RESOLVED
H8 If-None-Match context -> weak -> DIRECT_CORRESPONDENCE / RESOLVED
ALL CONFORMANCE: CONFORMANT
METHOD GAIN: NOT_ASSESSED
```

Preserved criterion/context discipline:

```text
STRONG_MATCH != WEAK_MATCH_IN_GENERAL
WEAK_MATCH != REPRESENTATION_IDENTITY
OPAQUE_TAG_EQUALITY_ALONE != STRONG_MATCH_WHEN_WEAK_MARKER_PRESENT
SAME_PAIR + DIFFERENT_HTTP_CRITERION -> possibly different verdict
RFC_COMPARISON_MATCH != WHOLE_REQUEST_PRECONDITION_RESULT
```

Precommitted score:

```text
A source / immutable precommit integrity       8/8
B candidate relation verdicts                 16/16
C criterion and context provenance            10/10
D scope / closure discipline                   8/8
E evidence-count / interpretation discipline   6/6
TOTAL                                          48/48 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5  # unchanged
REPRODUCIBILITY_CASES: 1     # unchanged
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

This application is materially different from the Unicode case because no normalization transform or representation bridge is performed. The source itself supplies criterion-dependent validator comparison semantics.

## 2026-09-11 — Step 13 CMP-APP-003 VIM metrological compatibility

Status: **52/52 PASS**

Precommit:

```text
evidence/method_specific/comparison/CMP-APP-003_precommit.md
commit 446aae3861c485c62828bba5432bae73aa7a9a45
blob 7aa6aa1b3aa2e75a233e2f39c2ca681448ddd2ae
```

Result:

```text
evidence/method_specific/comparison/CMP-APP-003_vim-metrological-compatibility.md
commit 6dad36fd3583c33159643ba888f3a802ac1b1ff3
```

External source:

```text
JCGM 200:2012
International Vocabulary of Metrology (VIM), 3rd edition
Entry 2.47 — metrological compatibility of measurement results
DOI 10.59161/JCGM200-2012
```

Execution:

```text
M1 compatible / k=2 -> DIRECT_CORRESPONDENCE / RESOLVED
M2 same pair / k=1 -> NONCORRESPONDENCE / RESOLVED
M3 exact threshold equality -> NONCORRESPONDENCE / RESOLVED
M4 just inside threshold -> DIRECT_CORRESPONDENCE / RESOLVED
M5 same central-value separation / small uncertainties -> NONCORRESPONDENCE / RESOLVED
M6 same central-value separation / larger uncertainties -> DIRECT_CORRESPONDENCE / RESOLVED
M7 zero central-value separation -> DIRECT_CORRESPONDENCE / RESOLVED
M8 unknown claim-relevant correlation -> UNDETERMINED_CORRESPONDENCE / UNDERDETERMINED
ALL CONFORMANCE: CONFORMANT
METHOD GAIN: NOT_ASSESSED
```

Preserved criterion/closure discipline:

```text
METROLOGICAL_COMPATIBILITY != STRICT_STRUCTURAL_EQUIVALENCE
METROLOGICAL_NONCOMPATIBILITY != PROOF_OF_DIFFERENT_PHYSICAL_OBJECT
CENTRAL_VALUE_DIFFERENCE_ALONE != COMPATIBILITY_VERDICT
SAME_PAIR + DIFFERENT_CHOSEN_MULTIPLE -> possibly different verdict
THRESHOLD_EQUALITY != STRICT_SMALLER_THAN
UNKNOWN_CORRELATION != ASSUME_UNCORRELATED
UNDERDETERMINED != FAILURE
```

Precommitted score:

```text
A source / immutable precommit integrity       8/8
B candidate relation + terminal verdicts      16/16
C numerical / criterion discipline            12/12
D scope / closure discipline                  10/10
E evidence-count / interpretation discipline   6/6
TOTAL                                          52/52 PASS
```

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5  # unchanged
REPRODUCIBILITY_CASES: 1     # unchanged
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

This application is materially different from both earlier external cases because the relation depends on quantitative uncertainty and correlation sufficiency. The correctly underdetermined M8 case is not counted as a run failure.

### Next

Run a separately precommitted first Comparison maturity audit. The audit itself must not add direct-pilot, external-application, or reproducibility counts.
