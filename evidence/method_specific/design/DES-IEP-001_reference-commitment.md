# DES-IEP-001 — Blinded Reference Commitment / 블라인드 참조키 커밋

Status: **REFERENCE COMMITMENT FROZEN BEFORE ANY INDEPENDENT SUBMISSION**  
Date: **2026-09-09**  
Packet class: `independent_evaluator_packet`  
Method: **DSD Design / DSD 설계론**

## 1. Frozen public artifacts

```text
REVIEWER_PACKET:
  evidence/method_specific/design/DES-IEP-001_reviewer-packet.md
  commit: 78b1fb45d0b2e40838517828d089942e7b55e7d8

SUBMISSION_TEMPLATE:
  evidence/method_specific/design/DES-IEP-001_submission-template.md
  commit: fe1eedca019b4283a21047d21fcac12dd672e328
```

These files are frozen before any eligible independent evaluator submission.
A later packet correction requires a new packet ID or explicit revision and cannot silently replace this commitment.

---

## 2. Reference-key commitment

Algorithm:

```text
SHA-256
```

Canonical commitment input:

```text
<32-hex-character secret nonce>
LF
<canonical DES-IEP-001 reference-key text>
```

Public commitment digest:

```text
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

The nonce and plaintext reference key are held outside the public reviewer packet and are not to be disclosed before the evaluator submission is frozen.

This commitment prevents post-submission answer rewriting only if the later reveal reproduces this digest exactly.

---

## 3. Reveal rule

The reference key may be revealed only after:

```text
1. an evaluator is declared eligible or provisionally eligible;
2. the evaluator completes DES-IEP-001;
3. the evaluator freezes the submission under an immutable or timestamped identifier;
4. that identifier is recorded before key reveal.
```

After those conditions:

```text
REVEAL nonce
REVEAL canonical reference key
RECOMPUTE SHA-256
REQUIRE digest match
THEN score the frozen evaluator submission
```

A hash mismatch invalidates the reference-key scoring event and requires an Audit record; it cannot be repaired by editing the key after reveal.

---

## 4. Precommitted agreement rule

Semantic score:

```text
TOTAL_SEMANTIC_CHECKS: 24
CRITICAL_CHECKS: 10
```

Classes:

```text
INDEPENDENT_AGREEMENT_FULL
  eligible evaluator
  24/24 semantic checks

INDEPENDENT_AGREEMENT_PARTIAL
  eligible evaluator
  >= 21/24 semantic checks
  10/10 critical checks

INDEPENDENT_DISAGREEMENT
  eligible evaluator
  < 21/24 semantic checks
  OR any critical check fails

CONTAMINATED_OR_INELIGIBLE
  independence eligibility fails
```

Critical checks are frozen as:

```text
C1 exact admissible family W
C2 exact admissible family N
C3 terminal status W
C4 terminal status N
C5 method-gain status W
C6 method-gain status N
C7 W-S1 scope answer
C8 W-S2 scope answer
C9 N-S1 scope answer
C10 N-S2 scope answer
```

Semantic equivalence is judged by meaning, not exact prose formatting.
Failure sets, candidate admissibility, family membership, ledger values, and yes/no scope positions must match the revealed canonical key.

---

## 5. Evidence effect before submission

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
DESIGN_DIRECT_PILOT_INCREMENT: 0
```

This record is infrastructure for a later independent-evaluator event.
It is not itself validation evidence.

---

## 6. Contamination guard

Because the project repository contains historical Design evidence, the preferred distribution mode is a standalone snapshot/export containing only:

```text
DES-IEP-001_reviewer-packet.md
DES-IEP-001_submission-template.md
required external-source material or links
```

The evaluator should not browse other Design evidence while scoring.
Any accidental exposure must be declared and assessed before an independence claim is made.
