# MF-REG-20261025-007 — Original AGG-CH-001 A/F/G 22 scoring-row recheck PRECOMMIT

Date: 2026-10-26 KST (continuation of 2026-10-25 audit sequence); author Kwon Dominicus.
STATE AT PRECOMMIT: INPUT + CLAIM POLICY LOCKED / NO NEW 007 EXECUTION.

## Frozen scope

After `MF-REG-005` individually re-ran B1–B12/C1–C12 (24/24), and `MF-REG-006` individually re-ran D1–D8/E1–E10 (18/18), address remaining original A1–A8 / F1–F8 / G1–G6 **22 scored rows**. All 64 old row names originate in the original `AGG-CH-001_precommit.md`, not newly invented names. Do not quote historical `64/64` as new validation.

Historical fixed chain (confirmed via original Git and a separate commits path read before this precommit):
- Aggregation Protocol commit `85b4263ad47cd10acd2230add542f381bd5d6a05`, blob `5ac926aa40594126b42dac99762ff33fe87450f1`.
- Original positive precommit Git commit `00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce`, blob `a59810b90b2b93a0e3b63ba7f23dc59178bef566`, timestamp `2026-09-25T19:03:04Z`.
- Original positive result commit `21b54077a7fe48f690b7528b2ad0025d6b8a1325`, original precommit **direct parent** `00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce`, timestamp `2026-09-25T19:03:48Z`, result blob `7e5d071936d52655886a8a91141785cf7ed580f9`.
- Original paper hashes Formation new 2026-10-22 `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe` (34p); Property `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c` (23p); Static `9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d` (23p). Historical 2026-08-06 Formation PDF unavailable; preserve BLOCKED.
- Prior audits' 005/006 actual row output JSON Git blob values to use for traceability, not to reproduce positive row predicates here: `485d30075b52085df2f8a68e222446e79f49a845` and `773e9a3f3a4176dcb758985e34b543a2ab9d6af0`.
- Published compact `verify_mf_reg_006.py` Git blob `2ea1c2fe3a4d74b7c4c5b66c24955d1402a0ce0e` was NOT byte-identically locally executed in previous 006. A separate actual published-script parity test is an OPEN work item; do not call the extended local source identical.

## Frozen row criteria from original precommit

**A (8)**:
A1 protocol commit and blob must match **retrieved original commit**, not a copied string; A2 task ID/version=AGG-CH-001/v1; A3 claim COMBINED_STATIC_DESCRIPTOR; A4 frozen Formation background ID B-AGG-001 / Property model ID A-AGG-001; A5 F and G exactly as historically frozen; A6 aggregation operator AGG-SUM-v1 and W=R², U=R², W×U combined; A7 required support and negative-status sidecars; A8 chronology of original precommit before result, result's direct parent exactly precommit, plus no claim of repairing frozen inputs (positively evidenced only within auditable original commit diff). **If the historical result commit is not a direct child, A8 BLOCKED or FAIL, never inferred from text.**

**F (8)**:
F1 exact Fraction average of original channel terms = (1/3,4/3). F2 independently labelled EQUAL_WEIGHT_CHANNEL_AVERAGE-v1 postprocess. F3 Comp=(1,4) remains finite direct core and is not replaced by the normalized average. F4 countable extension NOT_REQUESTED; F5 collision COLLISION_NOT_TESTED; F6 injectivity INJECTIVITY_NOT_TESTED; F7 reconstruction RECONSTRUCTION_NOT_CLAIMED; F8 static stability and specialized readout both NOT_REQUESTED. These guards refer to the original case's **claimed analysis scope**; no inference that the underlying map is globally collision free. Supplemental finite counterexample in 006 is not an original collision-ledger promotion.

**G (6)**:
G1 output task terminal AGGREGATION_TASK_ESTABLISHED if the finite formation/property sums and combined/support interfaces meet declared local obligations; G2 protocol conformant if frozen domain/status/sum/sidecar and A/F safeguards meet declared requirements; G3 method gain status AGGREGATION_METHOD_GAIN_NOT_ASSESSED, do not promote to NO_GAIN or gain; G4 maximum claim limited to finite F/G aggregates, combined descriptor and separately declared average, excluding source reconstruction, global injectivity, external validity; G5 "protocol revision not required", G6 "shared core reopening not required": these are *broader governance conclusions* and **cannot receive PASS just because old result text says no**. Only PASS if an independent dated contemporaneous proof/operational-approval rule is supplied; otherwise mark `BLOCKED_EVIDENCE`. Do not convert missing evidence into method failure.

## Execution

1. Commit a frozen JSON fixture containing all 22 original row IDs and explicit expected outcomes separately: `A/F/G` substantive row semantics, fixed case input/support/status/source, current source-paper hashes, original Git ancestry, historic result provenance and independent evidence requirement.
2. Write and run actual Python against the **exact locked PDFs** using `Fraction`; apply 22 substantive predicates. Output every row with one of `PASS`, `FAIL`, `BLOCKED_EVIDENCE`, row reason and supporting calculated signal. No unconditional `all PASS` on G5/G6.
3. Provide negative mutations against A and F and G relevant rows, plus source SHA. Never mutate packet disk; re-read byte hash before/after.
4. Reconcile `MF-REG-005` B/C 24 and `MF-REG-006` D/E 18 as distinct earlier row verification. Cumulative resolved scored rows can reach only `42 + count(A/F/G PASS)`; `BLOCKED_EVIDENCE` rows are covered/inspected but **not passed**.
5. Conduct a separate exact published `006` source replay only when file identity matches Git blob; otherwise report `OPEN`.
6. Publish Python, input, JSON, Notion/GitHub reciprocal evidence; never alter original 64/64 archival result or 22-method historic standardization.

Output verdict policy: `PASS_WITH_BOUNDARY_AND_GOVERNANCE_EVIDENCE_OPEN` if every independently checkable local original row passes and some governance rows remain BLOCKED; `FAIL_WITH_EVIDENCE` on any substantive row failure. Unavailable old Formation paper remains `BLOCKED_SOURCE_NOT_AVAILABLE`.
