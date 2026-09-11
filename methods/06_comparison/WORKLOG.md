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

Precommit:

```text
evidence/method_specific/comparison/CMP-APP-001_precommit.md
commit e1a109b9e4515336b4ee22c4d8ff216d4fd21705
blob 640f2b5e7cf9b990a07a2e3db542b114d655122f
```

Result:

```text
evidence/method_specific/comparison/CMP-APP-001_unicode-normalization-comparison.md
commit b64cd882047b45c4caaaf27cbc414c0b9b44e2e6
```

External source:

```text
Unicode Standard Annex #15: Unicode Normalization Forms
Unicode 17.0.0
Revision 57
2025-07-30
```

Frozen criteria:

```text
BINARY_IDENTITY
CANONICAL_EQUIVALENCE_VIA_NFC
COMPATIBILITY_EQUIVALENCE_VIA_NFKC
```

Execution:

```text
U1 Ç vs C+cedilla / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED
U2 same pair / binary identity
  -> NONCORRESPONDENCE / RESOLVED
U3 ① vs 1 / NFC canonical
  -> NONCORRESPONDENCE / RESOLVED
U4 same pair / NFKC compatibility
  -> ENCODED_CORRESPONDENCE / RESOLVED
U5 가 vs ᄀ+ᅡ / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED
U6 combining-mark ordering / NFC canonical
  -> ENCODED_CORRESPONDENCE / RESOLVED
```

All six DSD runs were `CONFORMANT`; method gain remained `NOT_ASSESSED` because no fair independent baseline was supplied.

Key preservation:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

Precommitted score:

```text
A source/precommit integrity          8/8
B candidate verdicts/terminals      12/12
C criterion/provenance discipline   10/10
D closure/protocol ledgers           6/6
E external-scope discipline          6/6
TOTAL                               42/42 PASS
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
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Interpretation discipline remains:

```text
EXTERNAL_PASS != METHOD_SURVIVAL_PROOF
EXTERNAL_PASS != METHOD_GAIN_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

### Next

Run a separately precommitted deterministic same-project retrace of `CMP-APP-001` using the frozen protocol, source lock, precommit, and result record.
