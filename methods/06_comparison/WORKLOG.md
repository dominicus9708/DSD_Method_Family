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

### Next

Add materially different external Comparison domains before maturity audit.
