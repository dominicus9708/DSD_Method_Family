# MF-REG-20261025-006 — Archived AGG-CH-001 D/E scoring row re-execution PRECOMMIT

**Date:** 2026-10-25 KST. **Author:** Kwon Dominicus.
**State at Git commit:** `PROSPECTIVELY_LOCKED_NOT_EXECUTED`. Prior `MF-REG-005` B1–B12/C1–C12 genuine row-specific replay 24/24 PASS remains separate.

## 1. Immutable historical evidence anchors

- Original `evidence/method_specific/aggregation/AGG-CH-001_precommit.md` Git commit `00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce`, blob `a59810b90b2b93a0e3b63ba7f23dc59178bef566`.
- Original `methods/10_aggregation_compression/aggregation/PROTOCOL_v0.1.md` Git commit `85b4263ad47cd10acd2230add542f381bd5d6a05`, blob `5ac926aa40594126b42dac99762ff33fe87450f1`.
- Original `evidence/method_specific/aggregation/AGG-CH-001_positive-constructed.md` blob `7e5d071936d52655886a8a91141785cf7ed580f9` (historical 64/64; **not new scoring credit**).
- Subsequent paper version overlay `FORMATION_20261022_COMPATIBILITY_OVERLAY.md` is prospective only. Source PDF SHA (and page count): Formation `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe` (34); Property `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c` (23); Static Aggregation `9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d` (23).
- Original Formation 2026-08-06 PDF is not present locally; `DIRECT_OLD_PDF_TO_NEW_PDF_REPLAY=BLOCKED_SOURCE_NOT_AVAILABLE`. No claim of old-paper/new-paper full semantic equivalence.

## 2. Precisely selected 18 ORIGINAL score rows (NOT new subtests)

**D1–D8 — combined descriptor:** D1 ordered descriptor `((1,4),(3,2))`; D2 correct Formation coordinate label; D3 correct Property coordinate label; D4 no numerical coordinate conflation, even if values happened to be equal; D5 preserve both source provenance families; D6 domain remains finite; D7 countable-core substitution absent; D8 combined claim established only when both declared finite-coordinate obligations are satisfied.

**E1–E10 — support/status retention:** E1 complete `H_channel(F)` including values and provenance on frozen F; E2 complete `H_property(G)` including values, input typing and provenance on frozen G; E3 retain `u1` applicable-but-undefined sidecar; E4 preserve c0 as admitted defined-zero; E5 preserve cX as absent; E6 preserve i0 as defined-zero; E7 preserve u1 as applicable-undefined, not zero; E8 no inference `AGGREGATE_EQUALITY -> SOURCE_IDENTITY`; E9 no inference `AGGREGATE_EQUALITY -> SUPPORT_EQUALITY/SOURCE_RECONSTRUCTION`; E10 all required support/status interfaces truly available.

Historical input: F={c1,c2,c0}; terms c1=(2,1), c2=(-1,3), c0=(0,0); cX is not admitted. G={i1,i2,i0}; values i1=(4,0) unary(x1), i2=(-1,2) binary(x1,x2), i0=(0,0) unary(x0). u1 applicable-but-undefined, typed(x3), kept outside G. Original positive constructed case declares **no injectivity, collision testing, or reconstruction claim**.

## 3. Strict acceptance protocol and edge cases

- Before running, separately commit frozen normalized JSON with exact typed supports, provenance, required sidecars, combined descriptor schema and expected individual D1..D8/E1..E10 labels (all PASS), carrying original artifact identities. Python independently recomputes and compares by row ID, never scoring the prior result text as new evidence.
- A row's positive verdict is a **condition of the frozen finite interface**, not validation of a full physical model, alternative property assignment, or all Formation 9-condition isomorphism obligations.
- A label or flag alone is not enough: D5 and E1–E3/E10 require concrete supplied supports, statuses, value ledgers and provenance, matched against the primary frozen input. E8/E9 require that the output schema does not contain forbidden identity/reconstruction promotions; supplement with a declared *additional counterexample* only when needed. The original positive case did not test injectivity.
- Stage-order and typed status retention cannot be proved just from sums; do not pretend an equality of aggregate values grants the sidecar by itself.
- Negative controls on temporary packet clones after the positive run: corrupt combined coordinate value (D1); swap coordinate roles (D2/D3); erase channel sidecar entry (E1/E10); suppress undefined property sidecar (E3/E7); change admitted defined-zero to absent (E4); falsely assert source-reconstruction from aggregate (E9). Source SHA tampering should reject independently. All mutations must be detected with specific failure row; retain original bytes.
- Counts must remain: 18 newly re-executed original rows in 006; prior 005 has 24 distinct original row predicates. **Combined B/C/D/E original score-row coverage, if successful, equals 42/64**, with **A(8)+F(8)+G(6)=22 NOT_EXECUTED**, rather than 64/64 or re-certified internal standardization.
- Do not alter original method statuses, original source profile or 22-method family. Method-gain, independent reviewer, external applications, and old PDF parity are all OPEN/unchanged.

## 4. Next output contract

Source-bound executable Python, immutable fixture, per-original-score-row JSON report, mutation test record, GitHub narrative report, Notion mirrored child page and root sync backlink, locally executed exact bytes matching uploaded GitHub blobs. Fail clearly rather than adjusting expected outputs after observing a failure.

**Next `MF-REG-20261025-007`:** A/F/G 22 remaining archived scoring rows, with immutable-source and optional-boundary/terminal-state controls; do not aggregate old historical results into fresh evidence.
