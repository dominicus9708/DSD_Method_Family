# PA-P14-20260901-NONEDIT-PROOF-OBLIGATION-MATRIX-001

**Executed:** 2026-10-24 KST. **Author:** Kwon Dominicus.
**Frozen manuscript:** `DSD_Property_Axiom_System_EN(4).pdf`, printed 2026.09.01, 23 pages, 157854 bytes; verified SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Prior prospective P14 test instructions:** [P14 precommit](P14_NONEDIT_PROOF_OBLIGATION_MATRIX_PRECOMMIT.md) (Git blob `7933f48ad03be21d6c6d91c5bb0d153e05657cbf`).
**Method:** independently re-read exact PDF source (in particular printed pp7–14,18–20; visually inspected rendered pp13–14); recompare against P9A–P13 proof and finite execution records, and check actual Github Actions statuses. This P14 is a *manual mathematical adversarial review and evidence classification*, not a new computer calculation, manuscript revision, Lean/Coq proof or external independent refereeing.

## A. Source-validity versus proof-status taxonomy

- **SOURCE-SUPPORTED:** premises in the printed manuscript suffice for the particular statement, subject to its actual quantifier scope.
- **CONDITIONAL-PROOF:** a mathematical deduction exists but uses an **added condition not literally in the original statement**. This is **not** SOURCE PASS.
- **SOURCE-CONDITION-MISSING:** a printed universal statement is ill typed or false under its ordinary reading; a legal counterinterpretation exists.
- **COUNTERMODEL-VALID:** a concrete typed witness refutes a logically stronger implication.
- **SCOPE-UNESTABLISHED:** a non-numbered or summarizing claim requires an interpretation bridge not proven in the printed source.
- **CI-REPRODUCED:** an executable *bounded* model suite ran; it never certifies an arbitrary-model theorem.
- **NOT-ESTABLISHED:** actual publication source edit, EN/KR parity, independent peer review or full formal-machine proof lacks evidence.

Never calculate a percent “of mathematics proven” from 56 source-heading count.

## B. Independent adversarial witness 1: declaration with unavailable profile

**Exact source:** Definition 2.5 p7–8 explicitly allows a declared kind without an available profile and requires no `Ap/Sat/Xi` coordinate. Definition 6.1 p13 states F3 “For every varpi in Pi_A” and invokes `phi_varpi:X_A,varpi→X_B,varpi`. Definition 6.3 p13 analogously quantifies over source input `x∈X_A,varpi`.

Fix shared signature containing auxiliary sort u, unary kind p with profile (u), and arbitrary Stage-VI inherited data.
- A supplies **no** auxiliary u carrier; `Pi_A={p}`; p is *declared* and profile unavailable. Both primitive soundness conditions are vacuous for p, and C1 completes this admitted core.
- The source-identity `A→A` must be a forward morphism by Proposition 6.2, but literal F3 requests the product `X_A,p` even though it is **undefined**.
- Therefore an all-object category with literal unguarded F3 does not have fully specified identity morphisms. F4/F5 inherit the same free/unrestricted p issue.

**Independent negative controls:**
- B with u *supplied as empty set* has `X_B,p=∅`, which is a **defined empty product**, not an unavailable product. The F3 condition for B's identity can be well typed and vacuous. This does **not** remove the A counterexample.
- Target-only declared kinds are permitted under F2; the guard should check **source declared AND source profile available** rather than forcing identical declarations in every forward map.
- Once **added guard G** explicitly restricts F3–F5 and Definition 6.3 reflection to source-declared/profile-available kinds, the general coordinatewise identity/composition proof in P11 is mathematically valid, including available-empty and repeated/mixed types. This is `CONDITIONAL-PROOF`, not an assertion that G is already in the PDF.

**Verdict P14-A:** `SOURCE-CONDITION-MISSING / SEVERITY=MATHEMATICAL-SCOPE / NOT_SOURCE-PASS`.

## C. Independent adversarial witness 2: carrier-bijective embedding need not be strict

**Exact source:** Definition 6.7 p14 demands S1 componentwise bijections, **S2 equal available auxiliary-sort sets**, **S3 equal property declaration sets**, S4 inverse embedding. Theorem 6.8 p14 instead summarizes strict isomorphisms as **“exactly the bijective property embeddings”** without defining that shorthand to include S2/S3.

**Counterexample to S3:** shared sort u supplied on both sides as singleton {x}; A declares no kinds, B additionally declares p with `Ap_B,p=∅`, no assigned values and (when present) every required `Sat_B,p,d=∅`. Both satisfy PI/PII/C1. Source-to-target u-identity is a forward property embedding, bijective on u. All source-property reflection demands are vacuous, but `Pi_A≠Pi_B`; strict S3 fails.

**Independent counterexample to S2:** A supplies no u, B supplies u as the **empty set**, and both declare no property kind. The empty family of component carrier maps from A is vacuously componentwise bijective and meets source-side embedding requirements; available-sort sets differ, so strict S2 fails. If one dislikes vacuous bijection, the first witness already supplies a nonempty bijective component and refutes the shorthand on S3.

Thus “embedding whose defined carrier components are bijections” is NOT equivalent to strict S1–S4 isomorphism. **The strict-isomorphism equivalence relation itself remains mathematically defensible with S1–S4 + G.** In P11, S4 can be derived from a *reflecting embedding* plus S1–S3 under G; stating S4 redundantly is not inconsistent.

**Verdict P14-B:** `SOURCE-CONDITION-MISSING / SEVERITY=MATHEMATICAL-CHARACTERIZATION / NOT_SOURCE-PASS`. Abstract and Theorem 11.1(7) inherit the shorthand issue.

## D. NEWLY SHARPENED P14 PROOF SCOPE: C1 versus axiom-independence counterpremodels

**Original text:** Clause C1 p9 starts “Given a primitive property core”, which Definition 2.6 requires to satisfy **both** PI and PII. Theorem 4.3 p11 says the two axioms are independent “Relative to the shared typed background and Definitional Closure Clause C1”. Its Countermodels 4.1 and 4.2 are correctly constructed as well-typed *premodels* intentionally violating a primitive axiom.

**Independent check on status single-valuedness:**
- CM4.1: `Ap=∅`, `DomXi={x}`, `Sat_d={x}`. By Definition 3.3's source formulas, x is **inapplicable** (`x∉Ap`) **and defined** (`x∈DomXi`).
- CM4.2: `Ap={x}`, `DepSat=∅`, `DomXi={x}`. x is **prerequisite-unsatisfied** and **defined**.
- For admitted full primitive cores, PI/PII prevent these overlaps and the status labels form the promised exclusive partition. On axiom-violating *premodels*, a single-valued C1 status cannot simply be carried over unchanged without allowing overlapping status predicates, a priority convention, or a narrowed relative-independence claim.

Accordingly, the previous phrase “C1 defining formulas can conservatively extend to typed premodels” is *not automatically sufficient* if “status” is a **single-valued exclusive label** rather than a collection of possibly overlapping predicates. Raw `DepSat`, domain and records remain definable on premodels, but exclusivity of statuses need not hold. An independence proof **relative to typing alone** remains valid; “relative to C1” needs an explicit metatheoretic interpretation of which defining equations, with which intended codomain, are being imposed on counterpremodels.

**Verdict P14-C:** `PROOF-SCOPE-UNESTABLISHED` specifically for **Theorem 4.3's “relative to C1” qualification**. This is a sharper logical gap than a purely stylistic note, but **not a third contradiction inside the class of full admitted property models**, nor a disproof of PI/PII independence over typed premodels. A full standalone closure-model formalization would be needed before a stronger FAIL is justified. Preserve previous countermodels rather than discard them.

## E. Twelve plus one theorem-11 summary evidence ledger

| Theorem 11.1 clause | Original PDF basis | Original-print status | Evidence level |
| --- | --- | --- | --- |
| (1) | Def2.1,2.3–2.5, pp6–8 | SOURCE-SUPPORTED | definition/typing |
| (2) | PI/PII, pp8–9 | SOURCE-SUPPORTED | primitive-soundness specification |
| (3) | CM4.1/4.2, Th4.3 p10–11 | PROOF-SCOPE-UNESTABLISHED *only re “relative to C1”* | typed premodel counterinterpretations remain valid |
| (4) | Def3.3, Prop4.5 pp9–11 | SOURCE-SUPPORTED with designated-zero guard | partition for full admitted cores |
| (5) | C1, Th3.7 pp9–10 | SOURCE-SUPPORTED relative to fixed primitive core | definitional inverse proof |
| (6) | Def6.1/6.3/6.5, Prop6.2/6.4, Th6.6 pp12–13 | SOURCE-CONDITION-MISSING | identity/category require G |
| (7) | Def6.7, Th6.8 p14 | SOURCE-CONDITION-MISSING in “exactly bijective embeddings” | S1–S4 equivalence itself conditional on G |
| (8) | Def5.4,6.10 Th6.11 pp12,14 | CONDITIONAL-PROOF / printed representation add-ons present | core S1–S4 relies on G |
| (9) | Def7.1–7.4, Th7.5 p15 | CONDITIONAL-PROOF | stagewise S1–S4 comparison and C1 |
| (10) | Th8.1, Th8.4 pp16–17 | SOURCE-SUPPORTED with finite compatible input scope | existence and C1 finite completion |
| (11) | Constructions8.5–8.7 p16–17 | SOURCE-SUPPORTED under finite witness signatures | selected cases, no general theorem by enumeration |
| (12) | Def9.1, Th9.2 p17–18 | SOURCE-SUPPORTED *existential* | collision witness (not blanket impossibility) |
| (13) | fixed inherited formation record, Remark3.5 and §10 | SOURCE-SUPPORTED as fixed interface | no claim of formation-coordinate evolution |

## F. Verified CI links and what they *do not* assert

As of this P14 run, checked the GitHub API statuses for four actual workflow runs in `dominicus9708/DSD_Method_Family`:
- [P9A #39897341069](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39897341069) — `completed/success`. **53** selected one-sort cores, map closure/stage checks.
- [P10 #39923494959](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39923494959) — `completed/success`. **108** bounded two-sort/mixed-profile cores.
- [P11 #39944973202](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39944973202) — `completed/success`. **10** independent empty/unavailable/multi-prerequisite source-specific cases.
- [P12 #39952098406](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/39952098406) — `completed/success`. **14** optional-representation/aggregate edge cases with JSON archive replay.
- All CI succeeded under Python 3.10 and 3.12, as logged in prior source-specific audits. **P14 did not run new code**, and no finite CI is evidence of an arbitrary-domain general theorem automatically.
- Original software companion in `dominicus9708/Property_Axiom_System` was separately exercised as run [#39733865420](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39733865420), 7 original tests under Python 3.10/3.12, with unchanged original generator, verifier and test blobs. No change to it in P14.

## G. Non-numbered source obligations and claim boundaries

1. **§9.2 p18 external Θ aggregate:** is separately supplied, and equality of arbitrary independent aggregates does **not** imply strict core isomorphism; strict core isomorphism likewise does not force equality of arbitrary external Θ outputs. P12 provides finite negative controls. Further bridge equivariance/injectivity is an extra assumption: `SCOPE-UNESTABLISHED` for unconditional hierarchy language, **not** a PI/PII contradiction.
2. **§10.1 p18 earlier realized-axis specialization:** additional geometric carrier sorts, prerequisite interpretation and axis totality rules are separately supplied. The paper describes a specialization possibility but contains no full formal interpretation theorem deriving every historical axis axiom from the general core. `INTERFACE-ONLY; TRANSFER NOT PROVED`.
3. **Def2.5 p7–8 unused coordinates:** “no coordinate required” is not equivalent to a formal assertion that unused metadata must always be forbidden; clarify canonical data identity only if mathematical comparison actually depends on it. `PRESENTATION/TYPE-CUSTODY-NOTE`.
4. **Abstract/Th11.1/Discussion:** cannot be recorded as an unqualified successful general theorem while their §6 claims contain the two printed problems. No other independently established primitive-axiom contradiction was found during P14.
5. **Definition 2.7 Stage P≤5:** stage numbers are ordering of information dependencies, not physical time. Later dynamics or aggregation do not follow from the two primitive soundness axioms.

## H. Independent closure/readiness gates

| Gate | Present status | Required evidence for closure |
| --- | --- | --- |
| Printed property core definitions, primitive soundness, C1 | SOURCE-REVIEWED / SUPPORTED IN SCOPE | preserve exact source and independent logical crosscheck |
| Printed §6 forward-map category over all admitted models | **BLOCKED — CONDITION MISSING** | explicit source-available profile guard with original-scope theorem re-evaluation |
| Printed Th6.8 “exactly bijective embeddings” | **BLOCKED — CHARACTERIZATION MISSING CONDITIONS** | formal S2/S3-inclusive equivalence statement and proof |
| “Relative to C1” independence in Th4.3 | **OPEN — PROOF SCOPE UNESTABLISHED** | specify definitional extension of C1 to typed premodels without assuming PI/PII or requiring impossible exclusive statuses; otherwise restrict relative scope |
| External aggregate comparison and old-axis transfer | SCOPE/INTERFACE ONLY | supply independent bridge/equivariance and optional axis interpretation theorem only if stronger claims are sought |
| 56/56 original heading audit | **DONE, manually typed/claim scoped** | NOT EQUAL to proof assistant verification |
| All general proof obligations independently formally verified | **NOT ESTABLISHED** | independent universal proof validation / formalization |
| Original EN/KR editable TeX + compiled PDF parity | **NOT VERIFIED** | verify original editable sources, one-section-at-a-time bilingual check, TeX compile/render and version-hash |
| Original PDF/Zenodo source revision | **NOT EXECUTED** | separate requested manuscript revision and public provenance, not this non-edit audit |
| External independent scholarly validation | **NOT ESTABLISHED** | actual third-party reviewing evidence rather than internal CI |
| P14 status | **COMPLETE, NON-EDIT** | archive reports and link Notion/GitHub |

No upgrade to publication-ready or globally complete proof is warranted from this P14 evidence.

```text
CASE: PA-P14-20260901-NONEDIT-PROOF-OBLIGATION-MATRIX-001
SOURCE_SHA256: 03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c
P13_REVERSE_DEPENDENCIES_RECHECKED: 13
§6_ISSUES: 2 CONFIRMED
§4_C1_INDEPENDENCE_QUALIFICATION: PROOF_SCOPE_UNESTABLISHED (newly sharpened)
CI_RECHECK_P9A_P10_P11_P12: ALL_COMPLETED_SUCCESS
P14_NEW_MACHINE_TESTS: NONE
P14_PAPER_OR_ORIGINAL_PYTHON_MODIFIED: NO
WHOLE_PROPERTY_FPA: OPEN
NEXT: PA-P15-20260901-C1_COUNTERMODEL_SEMANTICS-001 / NOT_STARTED
```
