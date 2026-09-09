# DES-IEP-001 — Cleanroom Distribution Record / 클린룸 배포 기록

Status: **DISTRIBUTION MATERIAL PREPARED — NO EVALUATOR SUBMISSION YET**  
Date: **2026-09-09**  
Packet: `DES-IEP-001`  
Evidence effect: **none**

## 1. Purpose / 목적

Prepare a reviewer-facing handoff copy that can be sent to a genuinely separate evaluator without directing the evaluator into the broader DSD repository, where historical Design evidence may be answer-bearing.

This distribution step is infrastructure only.

```text
DISTRIBUTION_READY
!=
INDEPENDENT_EVALUATOR_VALIDATION
```

## 2. Canonical frozen public sources / 공개 정본

```text
REVIEWER_PACKET:
  DES-IEP-001_reviewer-packet.md
  commit 78b1fb45d0b2e40838517828d089942e7b55e7d8

SUBMISSION_TEMPLATE:
  DES-IEP-001_submission-template.md
  commit fe1eedca019b4283a21047d21fcac12dd672e328

REFERENCE_COMMITMENT:
  DES-IEP-001_reference-commitment.md
  commit 8fe4ff64b3fc964746d7e8c11bd03d712c40fedd
```

Public reference commitment:

```text
SHA-256
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

The canonical answer key and nonce remain outside the distribution package.

## 3. Clean handoff artifact / 클린 배포물

A standalone ZIP was generated from the frozen reviewer-facing material for direct handoff outside the repository.

```text
FILE_NAME:
  DES-IEP-001_clean_evaluator_handoff.zip

ZIP_SHA256:
  3389bcc675130e859f9b0c68c7f9ab18ee2c253d1e1467897c06c8463ad3c819
```

Contents:

```text
READ_ME_FIRST.md
DES-IEP-001_REVIEWER_PACKET.md
DES-IEP-001_SUBMISSION_TEMPLATE.md
EXTERNAL_SOURCES.md
MANIFEST_SHA256.txt
```

The ZIP intentionally excludes:

```text
reference answer key
escrow nonce
historical DES-APP-001 result
historical DES-APP-002 result
DES-AUD-001 scoring detail beyond what the reviewer packet itself requires
other DSD Design evidence files
```

The local ZIP is a convenience distribution copy; the GitHub commits above remain the canonical packet/template identities.

## 4. External source links included / 포함 외부 출처

```text
W3C WCAG 2.2 dated Recommendation:
https://www.w3.org/TR/2024/REC-WCAG22-20241212/

NIST SP 800-63B-4 official HTML:
https://pages.nist.gov/800-63-4/sp800-63b.html
```

The packet freezes only its declared subsets; the evaluator must not expand the task into full-standard conformance scoring.

## 5. Distribution guard / 배포 가드

Preferred handoff:

```text
send the standalone ZIP directly
-> do not send a repository browsing link as the primary task surface
-> evaluator reads READ_ME_FIRST.md
-> evaluator completes submission template
-> evaluator freezes final submission
-> only then may reference escrow be revealed
```

If the evaluator browses prior Design evidence or otherwise receives answer-bearing content, the exposure must be disclosed before any independence claim.

## 6. Current evidence state / 현재 증거 상태

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
CLEANROOM_DISTRIBUTION_BUNDLE: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
DESIGN_DIRECT_PILOT_INCREMENT: 0
```

## 7. Next operational gate / 다음 운영 게이트

The project cannot complete the next evidence step internally.
A genuinely separate evaluator must now:

1. receive only the clean packet/materials;
2. make the independence declarations;
3. complete the two held-out tasks;
4. freeze the submission under an immutable or timestamped identifier;
5. return that identifier before any key reveal.

Only after that event may the project reveal the escrow material, verify the commitment, and score the frozen submission under a new Audit/evidence record.
