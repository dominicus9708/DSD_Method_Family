# FAS-F2-SEC6.2-C6.6-C6.7-001 — Category and formation-submodel preorder

**2026-10-19 KST · FPA v0.1 · One bounded two-corollary source audit; author-project internal mathematical review, NOT independent external certification.**

```text
AUDIT_CASE: FAS-F2-SEC6.2-C6.6-C6.7-001
PARENT_METHOD: DSD Audit (existing method of 22)
SOURCE_FILE: DSD_Formation_Axiom_System_EN(5).pdf (33 pp)
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: §6.2, printed p.17
PRIOR_DEPENDENCY: FAS-F2-T6.5-001 / PROVED_IN_DECLARED_BACKGROUND
PRECOMMIT_COMMIT: aaaaee5ea100a4915ecd25a5bd44ceca4509ecd8
PYTHON_COMMIT: 7fc37cafa0a5033c648b110df9908bad55b91d3b
JSON_COMMIT: 4972e91fcb397acf9b7a0ab290e06c62121d172e
COROLLARY_6_6_MATH: PROVED_IN_DECLARED_BACKGROUND
COROLLARY_6_7_MATH: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
CRITICAL_PROOF_GAP: none_found_in_scoped_claims
NEXT: FAS-F2-T6.8-001 / NOT_STARTED
WHOLE_F2_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_VALIDATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

## A. Exact frozen source claims

**Corollary 6.6 (Category of formation models).** With the comparison base and scalar field `(B,F)` fixed, full DSD formation models are objects, forward formation maps are arrows, and they form the *possibly large* category `Form_(B,F)`. Restricting arrows to formation embeddings but retaining precisely the same objects gives a *wide* subcategory `EmbForm_(B,F)`.

**Corollary 6.7 (Formation-submodel preorder).** `L ≼_form M` is defined by `L` being an actual formation submodel of `M` per Definition 6.4: component mappings are literal inclusions and jointly constitute a formation embedding. The relation is reflexive and transitive. Antisymmetry and totality are NOT claimed.

The dependency is Definition 6.1 for full typed objects, Definition 6.2 for forward maps, Definition 6.4 for formation embeddings and *inclusion* submodels, and Theorem 6.5 for identities and composition. The basis for these corollaries is ordinary set-theoretic category/function logic, not a DSD assumption of a pre-existing category/preorder.

## B. General mathematical proof, independent of selected finite fixtures

### B1. Corollary 6.6: category axioms

1. **Objects and Hom data.** Fix `(B,F)` and the source-declared typed interfaces. Every object is an individually set-coded full formation model. For two objects `L,M`, each candidate arrow is a finite tuple `(f_M,f_E,f_P,tau_Lambda,tau_R,{I_lambda},J)` of set functions between the declared set-sized carrier sorts, constrained by F1–F6. These are set-coded typed function tuples, and for fixed `L,M` their collection is a set under the background set-theoretic convention. The class of all objects may be proper. The source therefore calls the resulting category *possibly large*, not small.
2. **Identities.** Theorem 6.5 states each full model admits its componentwise identity forward formation map. Hence every object has an identity arrow.
3. **Composition.** For `Phi:L→M`, `Theta:M→N`, the source's componentwise `Theta∘Phi` is a forward map again by Theorem 6.5. The indexed assignment-value map is correctly `I_lambda^(Theta∘Phi)=I^(Theta)_(tau_Lambda^Phi(lambda))∘I_lambda^Phi`; `J^(Theta∘Phi)=J^Theta∘J^Phi`. No illegal type/quantity index crossing is introduced.
4. **Left/right units.** At every component (including correctly indexed families), `id_M∘Phi=Phi=Phi∘id_L` by elementary function identities, using componentwise equality of morphisms. Theorem 6.5's identity maps are the actual componentwise functions.
5. **Associativity.** For composable `Phi:L→M`, `Theta:M→N`, `Omega:N→P`, `Omega∘(Theta∘Phi)=(Omega∘Theta)∘Phi` componentwise. In particular, for each lambda the indexed `I` expression reduces on either parenthesization to `I^Omega_(tau^Theta(tau^Phi(lambda))) ∘ I^Theta_(tau^Phi(lambda)) ∘ I^Phi_lambda`. This follows from associativity of ordinary function composition, not from any finite enumeration.
6. **Wide subcategory.** Every formation embedding is, by Definition 6.4, already a forward map, so its Hom collection is included in the forward Hom collection. By Theorem 6.5 the identity arrow is an embedding and embeddings are closed under composition. Since objects are **not restricted**, `EmbForm_(B,F)` is a wide subcategory. No inference that *every* forward map is an embedding is allowed.

These steps prove precisely Corollary 6.6 in the source's declared ZFC-relative, definable-class/metatheoretic setting. They do not establish an internal object representing the proper class of all models as a ZFC set; such an object is not asserted.

### B2. Corollary 6.7: literal inclusion preorder

1. For any full model `L`, Theorem 6.5 makes `id_L:L→L` a formation embedding. Its components are literal inclusions of each sort into itself. By Definition 6.4, `L ≼_form L`. Hence reflexivity.
2. If `L ≼_form M` and `M ≼_form N`, each witnessed by a **literal componentwise inclusion** formation embedding, their composite `L→N` is a formation embedding by Theorem 6.5. Composites of the literal inclusions are the literal inclusions into N, respecting fixed (B,F); hence `L ≼_form N`. Thus transitivity.
3. This argument does NOT replace actual subset inclusions with arbitrary isomorphic images or just an embedding's existence. The relation is a preorder as stated. There is no asserted antisymmetry, comparability, or identity of objects up to mutual embeddability.

No primitive axiom change, missing hypothesis or additional lemma is required beyond the previously audited Theorem 6.5 and the source definitions.

## C. Adversarial finite checks (supplement, not universal proof)

Reproducible files:
- [Python](../scripts/verify_c66_c67.py)
- [Saved JSON](../results/c66_c67_category_preorder.json)
- [Prospective criteria](FAS-F2-SEC6.2-C6.6-C6.7-001_PRECOMMIT.md)

Command in cloned `dominicus9708/DSD_Method_Family` repo root:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c66_c67.py
```
Default output is the repository-relative `DSD_Audit/audits/formal_proof/formation_axiom_system/results/c66_c67_category_preorder.json`. Accepts an optional explicit CLI output path.

Fixture design: four full *degenerate* Formation models with nested finite material carriers of sizes 1,2,3,4; empty material-record relational signature, candidate expression/configuration classes, quantity kinds and roles; no channels; zero-dimensional term space `W={0}`. Primitive Axioms I–III/V and closure IV/VI/VII hold vacuously, including `Comp(emptyset)=0`. The material maps are arbitrary set maps for forward arrows; they are embeddings iff injective for this restricted fixture family.

Local deterministic execution:
| Tested obligation in finite class | Completed assertions |
|---|---:|
| Left and right unit laws for enumerated Hom sets | 494 |
| Associativity of all A→B→C→D combinations | 1,152 |
| Composition among triple injective embeddings | 288 |
| Inclusion-submodel reflexivity | 4 |
| Inclusion-submodel transitivity where premises true | 20 |

Adversarial cases:
- The injective renaming map from single material `{u}` to `{v}` is an embedding but **NOT** a componentwise literal inclusion, and hence does **not** establish `X ≼_form Y`; a source-legal witness refuting a tempting overbroad interpretation.
- A map from two materials `{a,b}` to a single `{a}` is forward in the empty-signature instance but not injective, hence **NOT** an embedding. This distinguishes the large category from the wide embedding subcategory.
- Zero admitted channels cause no breach of category/preorder laws; absence is not a zero-valued admitted channel.

The fixtures exercise only a narrowly chosen legal subclass. They do not computationally exhaust all source models with nonempty primitive relations, typed nontrivial assignment/value maps, or term maps. Universal category and preorder proofs are the preceding mathematical arguments, not their empirical fixture counts. Independent replication has not been performed.

## D. Formal-audit gates and revision decision

- G01 source lock: **PASS**; the attached source PDF's SHA-256 was checked; Zenodo byte identity not assumed.
- G02 dependency/noncircularity: **PASS**, depends on existing T6.5 and definitions, not on either desired corollary.
- G03 Hom typing/class size: **PASS_WITH_BOUNDARY**, each descriptor set-coded, all objects may be proper class.
- G04 primitive vs derived: **PASS**, category/preorder built from definitions rather than primitive axioms.
- G05 category/preorder proof: **PASS**, all category laws and reflexive/transitive closure shown.
- G06 existence/uniqueness: **PASS_WITH_BOUNDARY**, no smallness of object collection or skeletal uniqueness asserted.
- G07 counterinterpretation: **PASS**, embeddings need not be literal inclusions; forward maps need not be embeddings.
- G08 computational versus mathematical proof: **PASS_WITH_BOUNDARY**, narrow finite subclass only.
- G09 composition/embedding scope: **PASS**, preserves the literal inclusion requirement and indexed map typing.
- G10 outside background: **PASS_WITH_BOUNDARY**, metatheoretic class vocabulary allowed by §2, not internal ZFC proper-class set.
- G11 dependency impacts: **PASS**, no upgrade of unreviewed T6.8 or later results.
- G12 status/external evaluator: **PASS**, author-internal proof audit is not external certification.

**Final scoped verdict for both corollaries:** `PROVED_IN_DECLARED_BACKGROUND / PASS_WITH_BOUNDARY / REVISION_NEED=NONE`.

`WITH_BOUNDARY` refers to the original fixed-base/full-model category scope, large-class bookkeeping and the difference between arbitrary embeddings and literal inclusion submodels. It does **not** signify an incomplete proof for either source corollary. No release of new F2/Zenodo version is justified on this finding alone.

**Checkpoint:** end this bounded two-corollary unit. Next anticipated case: `FAS-F2-T6.8-001`, Theorem 6.8 embedding preservation/reflection, NOT_STARTED. Full F2 paper audit OPEN. Previously recorded Theorem 4.7 clarification issue remains separate.
