# PA-P9B3-20260901-SECTION7-6-ITEMS-001 — detailed comparison-stage audit

**Executed:** 2026-10-23 KST. **Source author:** Kwon Dominicus.
**Locked PDF:** `DSD_Property_Axiom_System_EN(4).pdf`, 23 pp, print date 2026.09.01, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`. **Source pages:** 15–16.
**Prerecorded protocol:** [P9B3_SECTION7_PRECOMMIT.md](P9B3_SECTION7_PRECOMMIT.md), Git commit `be5aaaf4a4ef114743409dd38a0c1d2acd00de85`.

## Six source-numbered headings reviewed

| Original heading | Exact audited dependency / edge | Verdict |
| --- | --- | --- |
| **Definition 7.1, Stage-comparison sets** | `I_k(A,B)` is set of **all** auxiliary carrier bijection families compatible with first k property-stage coordinates. I1 tests availability+cardinal, I2 adds declaration equality, I3 reflects applicability/prerequisites, I4 assignment-domain/value matching, I5 derived C1 data. Shared inherited sorts are fixed identities. Source/target model pair have fixed Formation Stage VI and shared property signature. | **WELL_TYPED_COMPARISON_DEFINITION**, conditional on the typed-profile conventions from Def2.4–2.5. |
| **Proposition 7.2, Nestedness** | Each `I_(k+1)⊆I_k`; a bijection preserving all primitive stages up to 4 automatically respects derived `DomXi`, finite intersection of `Sat`, statuses and typed record triples. Thus `I4=I5` if C1 is deterministic and no independent Stage-5 coordinate is supplied. | **PROOF_SUPPORTED** from C1, no numerical assumption. |
| **Corollary 7.3, Strict comparison** | `A≅B iff I4(A,B)≠∅ iff I5(A,B)≠∅`. Strict S1–S4 includes equality of availability/declarations and biconditional primitive data preservation: exactly conditions embedded in I1–I4. The carrierwise “bijective embeddings” shorthand in Th6.8 must **not** replace full S1–S4 when using this corollary. | **SUPPORTED_WITH_S1–S4_SCOPE_GUARD**. |
| **Definition 7.4, First branching index** | For a strictly nonisomorphic pair, Cor7.3 gives `I4=∅`; nestedness ensures first zero among 1,2,3,4 exists. It is defined from **whole comparison-set nonemptiness**, not failure of one selected bijection. Stage-0 is not here an added property stage. | **WELL_DEFINED_FOR_STATED_NONISO_PAIR**. |
| **Theorem 7.5, Branching symmetry and invariance** | Inverse of a comparison bijection stays in the same `I_k(B,A)` because stagewise conditions preserve **and reflect** the appropriate visible coordinates; pre- and post-composition by full strict isomorphisms bijectively transports comparison families; `I4=I5` precludes Stage-5 independent first branch. | **PROOF_SUPPORTED**, conditional on coherent S1–S4 strict maps. |
| **Remark 7.6, One failed map does not prove branching** | Valid distinction between existence of any compatible bijection and the failure of one chosen candidate map. All actual relevant bijections must be ruled out before claiming `I_k=∅`. | **SCOPE_CORRECT**. |

## Independent proof considerations / no overclaim

- **Nestedness** follows from conjunction nesting; **I4=I5** follows uniquely from deterministic C1. This is a general *source mathematical argument*, not a numerical extrapolation from P9A.
- Stagewise *symmetry* uses constraints of **equality/reflection**, unlike one-way **forward** maps of §6.1. Do not conflate absence of forward embedding with absence of stagewise strict comparison. In particular, an A→B forward map is not generally a witness in `I_k`.
- First branch can occur as early as **property Stage 1** due to unavailable/available auxiliary-sort cardinal/availability differences; Stage 2,3,4 concrete witnesses occur in §8.
- Because strict isomorphisms explicitly require S1–S4, the source's Theorem 6.8 shorthand error does not by itself refute this §7 proof when read against Definition 6.7. However corrected definition 6.1/6.3 typed-availability guards should be propagated to all comparison prose.
- Separate finite audit [P9A 53-core result](P9A_FINITE_MORPHISM_EXHAUSTIVE_RESULT.md) / [actual CI run](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39897341069) verified `I4=I5`, nesting, symmetry and invariant comparison profiles for **2,809 limited one-sort/two-kind ordered pairs**. The original property software run #39733865420 supplies examples for b=2,3,4; neither suite is general source theorem proof.

```text
CASE: PA-P9B3-20260901-SECTION7-6-ITEMS-001
ORIGINAL_NUMBERED_SECTION7_ITEMS_AUDITED: 6/6
CUMULATIVE_NUMBERED_ITEMS_AUDITED_AT_SCOPE_LEVEL: 44/56
I4_EQUALS_I5: SOURCE_PROOF_SUPPORTED
STRICT_I4_NONEMPTY_EQUIVALENCE: SUPPORTED_UNDER_S1_S4
BRANCH_SYMMETRY_INVARIANCE: SOURCE_PROOF_SUPPORTED
SOURCE_EDITED: no
GENERAL_ZFC_MACHINE_VERIFICATION: not_claimed
FPA_FULL: OPEN
NEXT: PA-P9B4-20260901-SECTION8-8-ITEMS-001
```
