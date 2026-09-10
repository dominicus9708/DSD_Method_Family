# SYN-IEP-001 — Clean Distribution Record / 독립 평가자 배포 기록

Status: **PREPARED — NO ELIGIBLE SUBMISSION YET**  
Date: **2026-09-10**  
Method: **DSD Synthesis / DSD 합성론**

## 1. Frozen public handoff artifacts

The clean evaluator handoff is defined by the following immutable public commits:

```text
REVIEWER_PACKET
  evidence/method_specific/synthesis/SYN-IEP-001_reviewer-packet.md
  commit: 6be55803db46c1941904501ecfa5fb13ba4ec01f

SUBMISSION_TEMPLATE
  evidence/method_specific/synthesis/SYN-IEP-001_submission-template.md
  commit: 079cdda0957314020001fbffac252a4765dac9a9

SYNTHESIS_PROTOCOL
  methods/05_synthesis/PROTOCOL_v0.1.md
  commit: 8787b242cb6648c47396151dbac3aadc19e3d184

PUBLIC_REFERENCE_COMMITMENT
  evidence/method_specific/synthesis/SYN-IEP-001_reference-commitment.md
  commit: b785df0e30c7e534693b9bc7f3a2011fb1617778
```

The evaluator needs the reviewer packet, submission template, protocol, and the external-source links contained in the reviewer packet. The public reference-commitment file may be supplied as proof that the hidden answer key was frozen in advance; it contains no plaintext answer key or nonce.

## 2. Explicit exclusions

Do not include or expose before submission freeze:

```text
secret nonce
plaintext canonical reference key
private escrow page
SYN-APP-002 answer-bearing result
SYN-APP-003 answer-bearing result
SYN-AUD-001 scoring result beyond general method status
other historical Synthesis candidate answers
project conversation history containing packet answers
```

The public repository contains answer-bearing historical material. Therefore sending a link to the repository root is **not** the preferred clean distribution mode.

## 3. Preferred evaluator instructions

```text
1. Receive only the frozen reviewer packet, submission template, and Protocol-v0.1 file or their exact commit-specific links.
2. Use only the external source links named inside the packet.
3. Do not browse the wider synthesis evidence tree after accepting the packet.
4. Complete the submission template independently.
5. Freeze the completed submission before any reference-key reveal.
6. Return the immutable/time-ordered freeze identifier.
7. Only then permit escrow reveal and scoring.
```

## 4. Current distribution/evidence ledger

```text
CLEAN_DISTRIBUTION_RECORD: prepared
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
PRIVATE_ESCROW: prepared_outside_public_method_tree
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
DIRECT_SYNTHESIS_PILOT_INCREMENT: 0
EXTERNAL_SYNTHESIS_APPLICATION_INCREMENT: 0
METHOD_SURVIVAL_OR_MERGER_DECISION: none
```

## 5. Archive note

A standalone ZIP or copied folder may be produced from the exact frozen commits for convenience, but such packaging is transport infrastructure only. The immutable commit identities above are the authoritative public content lock. A packaging artifact must never include the hidden nonce or canonical reference key.
