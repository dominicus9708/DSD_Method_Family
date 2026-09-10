# SYN-IEP-001 — Blinded Reference Commitment / 블라인드 참조키 커밋

Status: **REFERENCE COMMITMENT FROZEN BEFORE ANY INDEPENDENT SUBMISSION**  
Date: **2026-09-10**  
Packet class: `independent_evaluator_packet`  
Method: **DSD Synthesis / DSD 합성론**

## 1. Frozen public artifacts

```text
REVIEWER_PACKET:
  evidence/method_specific/synthesis/SYN-IEP-001_reviewer-packet.md
  commit: 6be55803db46c1941904501ecfa5fb13ba4ec01f

SUBMISSION_TEMPLATE:
  evidence/method_specific/synthesis/SYN-IEP-001_submission-template.md
  commit: 079cdda0957314020001fbffac252a4765dac9a9
```

These public files were frozen before any eligible independent evaluator submission.
A later correction requires a new packet ID or explicit revision; it cannot silently replace this commitment.

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
<canonical SYN-IEP-001 reference-key text>
```

Public commitment digest:

```text
db5d1c505c3ab2d614357525489f3b2a0dd2fc595fff1e715c69f48ceeb7073f
```

The nonce and plaintext reference key are held outside the public evaluator packet and are not to be disclosed before an eligible evaluator submission is frozen.

This commitment prevents post-submission answer rewriting only if the later reveal reproduces the digest exactly.

---

## 3. Reveal rule

The hidden reference material may be revealed only after:

```text
1. an evaluator is declared eligible or provisionally eligible;
2. the evaluator completes SYN-IEP-001;
3. the evaluator freezes the submission under an immutable or time-ordered identifier;
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

A hash mismatch invalidates the scoring event and requires a separate Audit record. It cannot be repaired by editing the key after reveal.

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

Critical checks:

```text
C1 exact admissible family S
C2 exact admissible family P
C3 terminal status S
C4 terminal status P
C5 method-gain status S
C6 method-gain status P
C7 S-S1 scope answer
C8 S-S2 scope answer
C9 P-S1 scope answer
C10 P-S2 scope answer
```

Semantic equivalence is judged by meaning rather than prose formatting.
Candidate result/failure sets, Task-S reached coherence states, family membership, ledger values, source identity, and yes/no scope positions are checked against the revealed canonical key.

---

## 5. Evidence effect before submission

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
SYNTHESIS_DIRECT_PILOT_INCREMENT: 0
METHOD_SURVIVAL_OR_MERGER_DECISION: none
```

This record is infrastructure, not validation evidence.

---

## 6. Contamination guard

The project repository contains answer-bearing historical Synthesis evidence. Preferred distribution is a standalone clean snapshot containing only:

```text
SYN-IEP-001_reviewer-packet.md
SYN-IEP-001_submission-template.md
required external-source links or local source copies
manifest/readme
```

The hidden nonce and canonical reference key must never be included.
The evaluator should not browse the wider Synthesis evidence tree while scoring.
Any accidental exposure must be declared and assessed before an independence claim is made.
