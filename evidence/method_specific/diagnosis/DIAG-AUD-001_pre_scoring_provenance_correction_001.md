# DIAG-AUD-001 — Pre-Scoring Provenance Correction 001

Status: **RECORDED BEFORE AUDIT SCORING**  
Date: **2026-10-01**  
Audit ID: `DSD-AUDIT-20261001-DIAGNOSIS-001`  
Correction class: `pre_scoring_provenance_correction`

## 1. Scope

The immutable DIAG-AUD-001 precommit commit:

~~~text
7a61edc5eb3b5b40fb40e266dd484a67a0bba753
~~~

correctly froze the audit question, 15 audit axes, promotion rule, 28 scoring checks, counters, and historical-preservation rule.

One claim-relevant artifact-identity field in the frozen evidence-corpus listing was transcribed incorrectly before scoring:

~~~text
DIAG-CH-006 result blob

recorded in DIAG-AUD-001 precommit:
  3f2eb15ad52d0c5e9474b7f0e80a172f46288bc8

actual repository blob:
  21dd8a0de623f9e9838f244c2ac4efa073f14d5d
~~~

The result commit was recorded correctly:

~~~text
d0aaf3f7b13a9c44a2959e415cc2b8171931596f
~~~

## 2. Verification

Repository path:

~~~text
evidence/method_specific/diagnosis/
DIAG-CH-006_deterministic-same-project-retrace.md
~~~

Verified identity:

~~~text
RESULT_COMMIT:
  d0aaf3f7b13a9c44a2959e415cc2b8171931596f

RESULT_BLOB:
  21dd8a0de623f9e9838f244c2ac4efa073f14d5d

CHECKS:
  70/70 PASS
~~~

## 3. Non-substantive correction lock

This correction is made before any DIAG-AUD-001 scoring.

It changes no:

~~~text
audit axis
axis criterion
promotion rule
scoring item
pass threshold
Diagnosis protocol rule
Diagnosis challenge result
Diagnosis counter
maximum-supported claim
~~~

The original precommit is not rewritten.

For DIAG-AUD-001 scoring, the frozen evidence corpus shall use the actual DIAG-CH-006 result blob:

~~~text
21dd8a0de623f9e9838f244c2ac4efa073f14d5d
~~~

## 4. Audit treatment

The correction must remain visible in the audit result.

Because the provenance correction occurred before scoring and changes no audit criterion or method evidence:

~~~text
AUDIT_PRECOMMIT_CORE_REOPEN_REQUIRED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

The audit may score historical-preservation axis M13 as at most:

~~~text
PRESENT_NONFATAL
~~~

rather than silently treating the precommit provenance record as error-free.

This does not predetermine the final promotion decision.
