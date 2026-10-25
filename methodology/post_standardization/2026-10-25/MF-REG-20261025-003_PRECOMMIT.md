# MF-REG-20261025-003 — Historical archived-case rebase audit PRECOMMIT

Author: Kwon Dominicus
Date: 2026-10-25 KST
Status at commit: PLAN_LOCKED / NO NEW CASE REPLAY EXECUTED

## Scope and explicit gap

Evaluate source-preserving **historical stored fixtures** from four methods against the supplied 2026-10-22 Formation edition. Unlike MF-REG-002, cases must come from actual historically published precommit and result documents. Preserve original status and outputs; compute a prospective 2026-10-22 compatibility replay, with no historical edits.

**Old full Formation 2026-08-06 PDF is not currently mounted.** The original method precommits also do not independently establish that every method claim depended on an identical version of every foundational source. Accordingly:
- direct side-by-side OLD_PDF -> NEW_PDF whole-method rerun: `BLOCKED_SOURCE_NOT_AVAILABLE`
- historic frozen inputs vs archived outputs: independently recompute using declared finite maps, and additionally check the affected 2026-10-22 source guard where applicable
- outcome without unexpected finite result drift: `ARCHIVED_FIXTURE_REPLAY_MATCH`, NOT `FULL_HISTORICAL_PROOF_REVALIDATED`.

## Four exact original source precommit Git locks (verified from GitHub commit refs)

| method | historical precommit | historic commit | blob |
| --- | --- | --- | --- |
| Comparison | `evidence/method_specific/comparison/CMP-CH-001_precommit.md` | `16c4b15f93d66299a2a3890f436e1aff0076713c` | `1c87d4261022a07175796bce16e794f9d0c77f31` |
| Aggregation | `evidence/method_specific/aggregation/AGG-CH-001_precommit.md` | `00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce` | `a59810b90b2b93a0e3b63ba7f23dc59178bef566` |
| Compression | `evidence/method_specific/compression/CPR-CH-001_precommit.md` | `8d19e2672854926afef33b9aea16df213dfe6a4f` | `49788325989be77aa1d5ac69eba5a18a5ae6ec25` |
| Reconstruction | `evidence/method_specific/reconstruction/RECON-CH-001_precommit.md` | `f56cce9a1228384b5607b89ce9092606053696bf` | `88058d72c76ff953e75dc18f179c64f040f8e51d` |

Original comparison protocol v0.1 and each method's original protocol v0.1 remain historical; this audit DOES NOT fully execute the dozens of method-specific scoring gates.

## Planned bounded archived cases and known historic results

- `CMP-CH-001-T1`: node triples {a0,a1,a2}/{b0,b1,b2} with paths, mapped zero/nonzero/zero status and f(ai)=bi; original strict equivalent / COMPARISON_RESOLVED.
- `CMP-CH-001-T4`: supplied aggregates A4 terms [1,1,2], B4 terms [4] each readout 4; supports sizes 3 vs 1, no bijective strict equivalence, NONCORRESPONDENCE / COMPARISON_RESOLVED.
- `AGG-CH-001`: admitted c1=(2,1), c2=(-1,3), c0=(0,0); cX absent; F={c1,c2,c0}; typed property i1=(4,0), i2=(-1,2), i0=(0,0), u1 applicable but undefined; G={i1,i2,i0}; expected finite Comp(F)=(1,4), Agg(G)=(3,2), descriptor=((1,4),(3,2)), separate channel average=(1/3,4/3), statuses preserved, no invented reconstruction.
- `CPR-CH-001`: (A,a1,NONZERO),(A,a2,NONZERO),(B,b1,ZERO),(B,b2,ZERO); C(group,detail,status)=(group,status), old/new field count 12 -> 8, same-group same-status collision safe relative to purpose, cross-group/status pairs preserved; COMPRESSION_TASK_ESTABLISHED.
- `RECON-CH-001-A`: bounded H-A {a1=(1,2),a2=(2,1),a3=(0,0)}, F(x1,x2)=x1+x2, y=3 -> compatible {a1,a2}, a3 excluded.
- `RECON-CH-001-B`: b1(P1,RED) no edge to C, b2(P2,BLUE) edge to C, b3(P3,BLUE) no edge; marker BLUE -> only b2 within declared class, not global historical truth.
- `RECON-CH-001-C`: u1=(1,0),u2=(0,1), sum readout 1 with declared complete-for-claim interface; class-local nonreconstructibility and multiple compatible sources.

Total: seven historical subcases across four methods. Source identity, expected case fields and source-manuscript guard are to be frozen in a separate JSON packet BEFORE executing Python. Preserve original labels exactly; distinguish report projections from full protocol checks.

## Audit acceptance gates

G1 source input four uploaded paper PDFs SHA/page lock (Formation `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe`, 34 pp; Property `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`,23pp; Static `9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d`,23pp; Dynamics `9994af76a1a0694e7c020ee2959d920966a4417940b0470e32068c43fa692176`,38pp).

G2 original four historical precommit commit-ref blob SHA locked and non-modified.

G3 historical result claims extracted as limited task-specific expected outcomes. G4 independent finite calculation from frozen input, not transcribed answer.

G5 new Formation §§5.12/5.13 conditional zero channel, §5.14 finite readout collision, §6.22/6.26 support-cardinality obstruction, and §8 strict isomorphism/fixed J distinction verified as current-source context. F1 4.7 and D2 7.3 not activated by these seven specific cases, NOT universal pass.

G6 for each tested archive case, retain old `OLD_INPUT / ARCHIVED_OLD_OUTPUT / NEW_FORMATION_SOURCE / NEW_REPLAY_OUTPUT / MIGRATION_DELTA`, and original terminal vs bounded replay compatibility.

G7 compare output key sets and values, count failures, preserve null/NO_GAIN/blocked correctly. Do not promote locally recomputed equality to global Formation proof, internal-standard 22 method revalidation or independent evaluator.

G8 create one or more adversarial mutations after positive run, and verify tester rejects falsified expectation. Original frozen packet never edited.

G9 publish source-lock, executable, result JSON, report, and Notion mirror; verify file hashes and reciprocal references.

**Fail-fast:** if original result or input field lacks reconstructible record, mark `BLOCKED_INCOMPLETE_HISTORIC_ARTIFACT`, not PASS. No historic rescore or scope expansion after seeing results.

## Planned next

Execute 7-case archived-identity check then deeper full method-protocol gate reproduction only for cases with enough original data. Independently recover old Formation PDF before stronger article-version difference claims.
