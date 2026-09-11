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
DIRECT_COMPARISON_PILOTS: 5
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

Criterion provenance, raw-vs-normalized distinction, scope exclusions, and `COMPARISON_METHOD_GAIN_STATUS = NOT_ASSESSED` were reproduced.

```text
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
```

## 2026-09-11 — Step 12 CMP-APP-002 HTTP ETag comparison semantics

Status: **48/48 PASS**

```text
PRECOMMIT: f77ddb2a384b15d6a1fe041c4be5c177c52b3623
PRECOMMIT BLOB: 7478867a0013cb94ae9a7e581a77548263cbe966
RESULT: fbba59a974482ff7469d7cec5b4ce63a85c2ae61
SOURCE: RFC 9110 — HTTP Semantics
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

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5
REPRODUCIBILITY_CASES: 1
EXTERNAL_COMPARISON_APPLICATIONS: 2
EXTERNAL_COMPARISON_DOMAINS: 2
EXTERNAL_COMPARISON_APPLICATION_PASSES: 2
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 2026-09-11 — Step 13 CMP-APP-003 VIM metrological compatibility

Status: **52/52 PASS**

```text
PRECOMMIT: 446aae3861c485c62828bba5432bae73aa7a9a45
PRECOMMIT BLOB: 7aa6aa1b3aa2e75a233e2f39c2ca681448ddd2ae
RESULT: 6dad36fd3583c33159643ba888f3a802ac1b1ff3
SOURCE: JCGM 200:2012 VIM3 entry 2.47
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

Evidence effect:

```text
DIRECT_COMPARISON_PILOTS: 5
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
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

## 2026-09-11 — Step 14 CMP-AUD-001 first maturity audit

Precommit:

```text
evidence/method_specific/comparison/CMP-AUD-001_precommit.md
commit 69315746b3ed5367aa56e087b96b8ea878a59376
blob 1a1df45d6c8bb54e2e7ed9c63d7aaf03f139eab3
```

Result:

```text
evidence/method_specific/comparison/CMP-AUD-001_maturity-review.md
commit afe4cc7d8a4efe2f7485768e0d9dc363010e34e2
```

Frozen maturity-axis result:

```text
M1  PASS
M2  PASS
M3  PASS
M4  PASS
M5  CONDITIONAL_PASS
M6  PASS
M7  PASS
M8  PASS
M9  PASS
M10 UNRESOLVED_BUT_BOUNDED
M11 PASS
M12 PASS
M13 PASS
M14 PASS
M15 PASS
```

Promotion decision:

```text
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Precommitted audit discipline:

```text
PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0
AUDIT_EXECUTION_VERDICT: PASS
```

The audit itself adds no direct Comparison pilot, no external application, and no reproducibility case.

The strongest supported maturity statement remains bounded away from:

```text
independent validation
independent replication
broad inter-rater agreement
measured practical superiority
universal external generality
permanent method-registry survival or irreducibility
```

### Next

Prepare `CMP-IEP-001` independent-evaluator infrastructure because M5 and M10 are now the dominant unresolved axes. Packet preparation alone is infrastructure and must not be counted as independent validation.
