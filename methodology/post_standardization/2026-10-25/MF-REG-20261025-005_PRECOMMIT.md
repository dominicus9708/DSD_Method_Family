# MF-REG-20261025-005 — Archived AGG-CH-001 original B/C scoring-row regression PRECOMMIT

Date: 2026-10-25 KST. Author: Kwon Dominicus.
At commit: **NOT_EXECUTED / scoring rules fixed prospectively**.

## Original evidence and immutable baseline

Original AGG-CH-001 method-specific precommit: `evidence/method_specific/aggregation/AGG-CH-001_precommit.md`, commit `00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce`, SHA blob `a59810b90b2b93a0e3b63ba7f23dc59178bef566`. Original protocol: `methods/10_aggregation_compression/aggregation/PROTOCOL_v0.1.md`, commit `85b4263ad47cd10acd2230add542f381bd5d6a05`, blob `5ac926aa40594126b42dac99762ff33fe87450f1`. Both exact blobs independently retrieved from historical commits and verified before this precommit. Original historic result: `evidence/method_specific/aggregation/AGG-CH-001_positive-constructed.md`, blob `7e5d071936d52655886a8a91141785cf7ed580f9`, historical 64/64 PASS. Do not substitute this historical count for new work.

Source-paper input lock: Formation (2026-10-22) 34pp SHA256 `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe`; Property (2026-09-01) 23pp SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`; Static Aggregation (2026-09-02) 23pp SHA256 `9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d`. Dynamics is optional/NOT_REQUESTED in the original frozen task and therefore need not be activated for the B/C rows. Historical 2026-08-06 Formation old PDF NOT available: `DIRECT_OLD_PDF_TO_NEW_PDF_REPLAY=BLOCKED_SOURCE_NOT_AVAILABLE`.

## Only 24 original scoring rows activated by this numbered audit

Block B — Formation-side execution, original score `B1..B12`:

- B1 c1 admitted; B2 c2 admitted; B3 c0 admitted; B4 cX absent.
- B5 admitted c0 defined zero preserved; B6 cX not zero extended.
- B7 exact T(c1)=(2,1), B8 exact T(c2)=(-1,3), B9 exact T(c0)=(0,0).
- B10 finite sum Comp(F)=(1,4).
- B11 direct aggregate is unnormalized; B12 formation aggregate established for frozen admitted finite F.

Block C — Property-side execution, original score `C1..C12`:

- C1 i1 selected and defined; C2 i2 selected and defined; C3 i0 defined zero and selected.
- C4 u1 applicable-but-undefined retained as negative-status sidecar; C5 u1 not in selected defined carrier; C6 u1 not zero padded.
- C7 i2 ordered typed input (x1,x2) preserved; C8 no canonical single-channel owner of i2 inferred absent selector.
- C9 exact Theta(i1)=(4,0); C10 Theta(i2)=(-1,2); C11 Theta(i0)=(0,0).
- C12 finite property sum Agg(G)=(3,2), aggregation established on frozen selected defined G.

## Prospective procedure and constraints

1. Commit separate immutable normalized input/expected-label fixture file **before** any run. Each row B1..B12 and C1..C12 is an independent labelled predicate in output. Source ID/term/status and support selections are frozen; evaluator must calculate from fixture inputs and checks, not copy the old report's PASS labels.
2. Verify exact PDF SHA256/pages for three activated source papers, and minimal relevant source text anchors. Historical Git precommit/protocol commit blobs are immutable baseline; if missing or tampered, abort/block.
3. Actively compute both finite sums, test all membership and status states and non-padded undefined/absent channels. Preserve provenance and multi-input source schema.
4. Truthful scope: B and C **24 original-row criteria can be retested**, not the 64-score total. Remaining A(8),D(8),E(10),F(8),G(6) = **40 original scoring rows not rerun in 005**. The fixture replay in prior 003 overlaps underlying values; new contribution now is **direct row-wise labelled verification**, not a new independent application.
5. Re-run adversarial mutations after the positive pass: flip c0 admission, falsely insert absent cX, corrupt c1 term, reclassify u1 as defined zero, change i2 input order, corrupt Property paper digest. Mutation must make at least one appropriate original-row check fail; never edit original packet.
6. Preserve unrequested collision/injectivity/reconstruction sidecars as `NOT_REQUESTED/NOT_TESTED`. No claim of universal injectivity, proof of all Formation clauses, 22-method validation, independent evaluator evidence, method-gain assessment or original old-vs-new source-paper execution. No revision or merge/delete of methods from success/failure.
7. Publish actual checker Python, frozen fixture and output with explicit execution hashes; update Notion/GitHub reciprocally after success, otherwise report failure without changing frozen expected values.

**Next:** remaining A,D,E,F,G block replays under a separately frozen numbered audit; do not infer their status from 005.
