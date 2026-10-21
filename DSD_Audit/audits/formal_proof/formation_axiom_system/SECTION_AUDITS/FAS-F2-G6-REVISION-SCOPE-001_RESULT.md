# FAS-F2-G6-REVISION-SCOPE-001 — Four outstanding manuscript scope and revision issues

**2026-10-21 KST · original author Kwon Dominicus · Formal Proof Audit (FPA) v0.1.**

## 0. Immutable evidence, prospective boundary, scope

- Primary source: `DSD_Formation_Axiom_System_EN(5).pdf`, 33 pages. Original PDF SHA256: `8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a` (matched from actual supplied PDF).
- Original printed p11 Theorem 4.7, p14 Proposition 5.13, pp25–26 Section 7.3, pp28–29 Section 8 Discussion. The source pages 26 and 29 were directly rendered and examined; `pdftotext -layout` independently checked.
- [Prospective audit obligations](FAS-F2-G6-REVISION-SCOPE-001_PRECOMMIT.md), frozen **before result** at commit `282085333d31ff0096f7f89c90c209f83778a7dd`.
- Earlier separate FPA evidence, not overwritten:
  1. [Theorem 4.7](../THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md);
  2. [Section 7.3 D2](FAS-F2-SEC7.3-D2-001_RESULT.md);
  3. [Section 8 Discussion](FAS-F2-SEC8-DISC-001_RESULT.md);
  4. [Section 5 / Proposition 5.13](FAS-F2-G3-SEC5-001_RESULT.md).
- Independent amendment documents for author review: [English source-section patch proposal](FAS-F2-G6-REVISION-SCOPE-001_PATCH_DRAFT_EN.md), current commit `f2072a4c0d557e8f7799e13bf46d847abb6bb180`, and [1:1 Korean verification draft](FAS-F2-G6-REVISION-SCOPE-001_PATCH_DRAFT_KO.md), commit `b814072262f75e6938e90112ac4ec788af2ad28c`. **Proposals only, NOT changes to source PDF, LaTeX, Zenodo or published theorem statements.**

## 1. Verdict matrix — four independent open author-source issues

| Case | Original wording/scope issue | Verified mathematical position | Editing class and necessity | Original manuscript status |
| --- | --- | --- | --- | --- |
| Theorem 4.7 (§4.2) | The phrase "other primitive axioms" can mean the **intact parent axiom** which includes the residual clause deliberately falsified in the witness. | Six residual constraints are independent relative to typed background and the **other five residual constraints**, as tested in prior 6/6 counterinterpretations. The intact parent axiom cannot remain true when one of its own conjuncts is false. | **CLARIFICATION / necessary to disambiguate the independence premise and final proof sentence**. | Not revised. |
| §7.3 D2 grid witness | Exposed blocked boundary annotation is not exhaustively encoded/inherited in the printed construction, and "horizontal" for edge (0,0)–(1,0) depends on coordinate convention. | A common typed 57-item grid material carrier (9 vertices, 12 edge-items, 36 slot-items), restricted 9-item h*/p* material (2 vertices, 1 edge, 6 exposed slots), common inherited blocked annotations, and differing primitive BC policies gives a legal completion with **b(L+,L-)=3**. Geometry alone does not derive BC. | **SPECIFICATION COMPLETION / recommended for a reproducible "fully specified" witness; coordinate terminology clarification**. | Not revised. |
| §8 Discussion, p29 | "Composite-level coincidence ... is therefore strictly weaker" may assert a universal strict-equivalence ⇒ fixed-J coincidence implication. | Source Proposition 6.22 proves coincidence **does not imply** strict equivalence. Reverse implication fails for arbitrarily fixed J even when descriptors are strictly equivalent; empty admitted-channel models also fail Definition 6.21's nonempty-family requirement. | **LOGICAL_STRENGTH_CORRECTION / required**, replace implication-hierarchy sentence with condition-aware comparison. | Not revised. |
| Proposition 5.13 | "It therefore loses channel membership" may be read as **inevitable in every model** after zero extension. | A collision occurs if an absent candidate and an admitted zero-term channel both exist. In models with only nonzero admitted terms, membership is recoverable from output. | **CONDITIONAL_SCOPE / clarify quantifiers and meaning of channel-faithful**, without weakening the intended "absent ≠ zero" distinction. | Not revised. |

**Prior case conclusions retained without conflation:** Mathematical independence in T4.7 is not refuted; D2 earliest branching index remains 3 in a consistent completion; Proposition 6.22 is still a valid existential counterexample to coincidence implying strict equivalence; Proposition 5.13's conditional collision is still valid.

## 2. Source-level derivations and amended-claim proof

### G6-02 — Theorem 4.7 in its residualized background

The original source lists residual constraints R1–R6 after Proposition 4.6's typing-induced dependencies.
For any i, the intended witness has R_j true for all j≠i and R_i false.
If R_i is a conjunct of a parent primitive Axiom A_k, then A_k is also false in that witness.
Therefore an English claim that "**the other primitive axioms** remain true" must explicitly exclude the undecomposed parent axiom or, better, be replaced by "**the other five residual constraints** remain true".
This is an equivalence of the *axiom presentation* in a fixed typed background, not a new independent primitive axiom.
The prior six typed witness checks are sufficient to support the proposed reformulation relative to their frozen condition sets.
No new finite countermodel code was executed in G6 itself.

### G6-03 — Section 7.3 D2 consistent specification

Let X_D2={0,1,2}×{0,1,2} and S*={(0,0),(1,0)}.
There are nine sites; the undirected grid has 3·2 horizontal and 3·2 vertical nearest-neighbor edges =12; one potential directional slot per site and four cardinal directions gives 36 slots; 57 typed items overall.
The two chosen adjacent sites have eight incident cardinal directions in total, two consumed by their common internal edge, leaving **six exposed boundary slots**.
The selected h*/p* material has exactly 2+1+6=9 items.

A specific additional **consistent completion not literally enumerated in source** is:
- assign external boundary-record annotation blocked to exactly the six S*-exposed slots, transmissive to the other 30 potential slots;
- retain this one map by induced material restriction from H* into h* and p*, preserving the required anchor maps and typed material-incidence records;
- take identical annotations and material structures in both regimes; let primitive BC_{L+}(p*)=true (blocked permitted), BC_{L-}(p*)=false (transmissive-only policy);
- leave both models' first two stage inputs the same.

Then the source's described expr/config gates give K_des(L+)={p*}, K_des(L-)=empty and the first incompatible comparison stage is 3, not a speculative physically derived grid law.
In (row,column) convention, the joining edge changes first coordinate and is conventionally vertical; to eliminate ambiguity, label it "joining nearest-neighbor edge" rather than "horizontal".
This is a **reproducibility and annotation-completeness** repair to an example; it does not create a new counterexample to the source's b=3 statement.

### G6-04 — What a fixed comparator J actually implies

Define S as strict formation equivalence of full descriptors over the same base and C_J as existence of nonempty finite admitted-channel families with composite equality under **independently prescribed** J (original Definition 6.21).

1. C_J⇒S is false: original Proposition 6.22 constructs strictly nonequivalent models L,M and J=id with nonempty equal-composite witness families.
2. S⇒C_J for every prescribed J is false: take a legal one-channel full model L=M with T(c)=1, W=R, strict identity descriptor isomorphism, but prescribe J=-id_R for the separate composite-coincidence test. Its only nonempty family {c} yields J(1)=-1 vs 1. C_J fails.
3. Independently, any full model with admitted channel set empty is strictly equivalent to itself but cannot supply the nonempty family required by Definition 6.21 even at J=id.
4. Positive qualified direction: when strict isomorphism Phi exists and its channel set is nonempty, **using the J_Phi component of that same witnessing strict isomorphism**, E9 and channel bijectivity give termwise transport and hence coincidence of the matching nonempty finite family F and PhiHat[F].

Thus **there is no unconditional logical implication ordering between S and C_J with freely fixed J**, although checking a selected output equality forgets more primitive structure than a strict formation isomorphism.
The manuscript's §8 "strictly weaker" phrase is the only incorrect logical-strength formulation in this local comparison; it should be corrected without changing original Proposition 6.22 or Definition 6.21.

### G6-05 — Exact Proposition 5.13 condition as output-only decodability

Let U_L be the candidate channel universe with admitted subset C_L and supplied component map T_L:C_L→W_L.
For a zero extension barT:U_L→W_L set barT(c)=T(c) on C_L and barT(u)=0 outside C_L.
Call membership **output-decodable** if there exists d:W_L→{0,1} such that d(barT(u))=1 exactly for admitted u∈C_L (this is an **audit definition**, not a term in the original paper).

The exact elementary criterion is:

```text
NOT output-decodable
iff (U_L \ C_L != empty) AND (there exists c in C_L with T_L(c)=0_W).
```

If the two sets of witnesses exist, an absent u and admitted zero c produce equal outputs with unequal membership, so no decoder d exists.
Conversely, if there is no absent candidate, the constant-one decoder works.
If absent candidates exist but all admitted T(c) are nonzero, the decoder d(v)=1 if v≠0 and 0 otherwise works.
This identifies exactly the information-loss condition for **membership from value only**.
The source first clause ("identifies absence with any admitted ... zero") is correct when those witnesses coexist; the follow-up “It therefore loses channel membership” needs a conditional/quantifier specification to prevent universal over-reading.
Do **not** confuse T(c)=0 with global q(a)=0; they are independent inputs.

## 3. Manuscript dependency impact and what remains valid

- **Primitive Axioms I–III, V:** no amendment is proposed or justified by these four findings.
- **Closure IV, VI, VII; original operational channel 5-tuple:** unchanged.
- **Original T4.5, T4.7 intended residual proof, T6.16 branching, P6.22 coincidence nonimplication:** retained under their explicit hypotheses.
- **Discussion §8:** the corrected comparison phrase should accompany the already validated one-way Proposition 6.22, and should not imply an arbitrary-J structural isomorphism.
- **Conclusion §9:** its residual "in the sense established by countermodels" and distinct-output/strict-equivalence claims do not themselves reproduce the unqualified fixed-J implication; check cross-references at actual future edit, but this G6 does not prescribe mandatory global rewriting of §9.
- **§7.3 title "fully specified":** the specified completion is required to make the witness truly reproducible without extra interpretation; the proposed six blocked and 30 transmissive boundary annotations should be incorporated by author when preparing a manuscript revision.

## 4. Evidence/provenance and absence of invented execution

G6 uses **logical implication checks and the previously executed, archived source-specific finite scripts and JSON**; it did NOT run a new Python verifier and did not generate a fresh full-model exhaustive certificate.
The precise proofs above are based on the actual supplied PDF and the earlier frozen result cases.

Linked prior verifier artifacts:
- [T4.7 original finite countermodels](../THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md);
- [D2 source-typed finite model](FAS-F2-SEC7.3-D2-001_RESULT.md);
- [§8 fixed-J finite comparison](FAS-F2-SEC8-DISC-001_RESULT.md);
- [§5 zero-extension full typed models](FAS-F2-G3-SEC5-001_RESULT.md).

The numerical 57/9/6 D2 carrier counts and the two finite scalar counterexamples are elementary direct deductions; this case does not claim to have run previously unexecuted code.

## 5. Detailed proposed text and author-governance decision

- [G6 English per-section manuscript patch proposal](FAS-F2-G6-REVISION-SCOPE-001_PATCH_DRAFT_EN.md), **status NOT APPLIED**, latest commit `f2072a4c0d557e8f7799e13bf46d847abb6bb180`.
- [G6 1:1 Korean verification draft](FAS-F2-G6-REVISION-SCOPE-001_PATCH_DRAFT_KO.md), **status NOT APPLIED**, commit `b814072262f75e6938e90112ac4ec788af2ad28c`.
- Per original source section, proposals preserve the original theorem numbering and label boundaries; if later inserted into LaTeX, author remains **Kwon Dominicus** and edits must be section-delimited with commented `-----` separators as per project practice.
- Original PDF and any existing Zenodo version remain **unchanged**; the audit has no mandate to amend an archival DOI release without explicit author control.
- A source-dependent prospective G7 gate should check the four proposals against *actual submitted/current LaTeX section files*, with draft version provenance and dependency closure, before claiming a **revised** F2 formal-proof audit pass.

## 6. Final G6 verdict and next checkpoint

```text
CASE: FAS-F2-G6-REVISION-SCOPE-001
MATHEMATICAL_VERDICT: MIXED — intended T4.7/P5.13 source claims supportable under explicit scope; D2 witness consistent after annotation completion; §8 fixed-J strict-weakness implication DISPROVED_AS_UNQUALIFIED
DSD_AUDIT_VERDICT: PASS_WITH_REFINEMENT
REVISION_NEED: MANUSCRIPT_CLARIFICATION_4_OPEN (1 logic-strength correction + 2 premise/quantifier clarifications + 1 source-data specification completion)
PROPOSED_EN_AND_KO_DRAFTS: written / NOT_APPLIED
NEW_G6_EXECUTABLE_COMPUTATION: none; previously executed case evidence cited
FULL_NUMBERED_SOURCE_ITEMS_WITH_AUDIT_EVIDENCE: 69 / 69
PREVIOUS_G5_REMARK_AUDITS: 5 / 5
MATHEMATICAL_MODEL_CLASS_INCONSISTENCY_FOUND: no
F2_FULL_PAPER_FPA: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
DSD_METHOD_FAMILY_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-G7-REVISION-INTEGRATION-READINESS-001 / NOT_STARTED
```

**G6 is closed as an audit of correction requirements. The four manuscript edit actions remain OPEN** until a versioned, author-controlled source edit and subsequent source-by-source re-audit.

Notion individual G6 audit case: https://app.notion.com/p/40081f51e7fa8122b038e43866d4b1c8
