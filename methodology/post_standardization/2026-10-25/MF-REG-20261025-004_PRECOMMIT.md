# MF-REG-20261025-004 — Archived method-case coverage and Comparison T2/T3 replay PRECOMMIT

Date: 2026-10-25 KST
Author: Kwon Dominicus
State when written: LOCKED_BEFORE_NEW_EXECUTION

## Carryover

MF-REG-003 replayed seven historically preserved subcases: Comparison T1/T4; Aggregation AGG-CH-001; Compression CPR-CH-001; Reconstruction RECON-CH-001 A/B/C. It did NOT re-execute every frozen scoring gate of those methods. Extend with original Comparison T2/T3, then audit remaining historical-gate coverage across Comparison, Aggregation, Compression, Reconstruction. No historical evidence is overwritten.

## Historical artifact identities and stable target

- `evidence/method_specific/comparison/CMP-CH-001_precommit.md`, Git commit `16c4b15f93d66299a2a3890f436e1aff0076713c`, blob `1c87d4261022a07175796bce16e794f9d0c77f31`.
- `evidence/method_specific/comparison/CMP-CH-001_positive-direct-comparison.md`, blob `3ec8f4dc7f3095ec5fa9f1522d064e74f70e35af`; historic method aggregate: 40/40 precommitted scoring checks PASS. Newly checking T2/T3 **does not** produce new 40/40 completion.
- Original `methods/06_comparison/PROTOCOL_v0.1.md` fixed; not edited here.
- Additional historically preserved AGG/CPR/RECON primary positive cases originally reported 64/64, 72/72, 80/80. The four totals must not be used as claims for this audit's *new executions*.
- The four pinned attached source PDFs are unchanged from MF-REG-003, Formation 2026-10-22 hash `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe`. Historical old Formation 2026-08-06 PDF is not present in attached container or retrieved file-library records. GitHub Formation repository's visible releases 1.0,1.1,1.1.1,1.1.2 have no binary release assets. `OLD_FORMATION_PDF` source itself stays `BLOCKED_SOURCE_NOT_AVAILABLE` absent a later verified exact SHA source.

## T2 original immutable case

A2 nodes x0,x1; directed x0->x1; readiness statuses DEFINED_ZERO,DEFINED_NONZERO.
B2 nodes y0,y1,y2; y0->y1 and y1->y2; readiness DEFINED_ZERO,DEFINED_NONZERO,DEFINED_ZERO.
Frozen f2(x0)=y0, f2(x1)=y1; one-way injective, preserves mapped edge/status, **not** surjective B2. Expected `DIRECT_CORRESPONDENCE`, `STRUCTURAL_EQUIVALENCE_RESULT=no`, `COMPARISON_RESOLVED`, `CONFORMANT`, `NOT_ASSESSED`.
Map-family singleton and mapped-subset element coverage are *scope-specific*, not a survey of all mathematical possible maps. Failure to cover y2 is legitimate for direct one-way claim but rules out strict equivalence.

## T3 original immutable case

A3 states numeric 0,1 and transition 0->1, readiness DEFINED_ZERO,DEFINED_NONZERO.
B3 states OFF,ON and transition OFF->ON, readiness DEFINED_ZERO,DEFINED_NONZERO.
Supplied encoding bridge e: 0->OFF, 1->ON, bijective, inverse preserved. No literal coordinate equality.
Expected `ENCODED_CORRESPONDENCE`, `equivalent_under_supplied_encoding_only`, `COMPARISON_RESOLVED`, `CONFORMANT`, `NOT_ASSESSED`.
No implicit type/value conversion; bridge has original provenance and remains a separate condition. Encoded equivalence is not automatically Formation strict isomorphism.

## Prohibited post hoc changes

- Freeze normalized actual subject fixtures and expected result keys BEFORE execution and maintain original precommit and reference-hash chain.
- Calculate map coverage, edges, inverse, statuses and exact output classifications independently from the normalized input.
- Source SHA lock and at least source scope anchors checked. No completion claim for original 40/64/72/80 full check suites.
- Controlled negative mutations: falsely make T2 surjective, falsely mark T2 strict equivalent, erase encoding bridge from T3, misclassify T3 direct correspondence, corrupt source SHA; frozen fixture unchanged. Any unexpected mutation acceptance -> FAIL.
- Coverage registry of original method check totals must separately name previously run original totals, newly rerun test counts, and still-unexecuted original scoring gates. Avoid math like `40+64+72+80 verified` in this new audit.
- If expected values or source artifact unavailable: mark specific blocked field, do not convert into pass.
- If old Formation PDF stays unavailable, direct source-paper old/new parallel replay remains BLOCKED. PDF absence is NOT evidence mathematical inconsistency.
- Save GitHub code+JSON+report and reciprocal Notion record, verify both.

Next proposed step: expand one-by-one to the remaining archived original scoring gates only if source- and scope-locked, then independent evaluation and real external domain tests separately.
