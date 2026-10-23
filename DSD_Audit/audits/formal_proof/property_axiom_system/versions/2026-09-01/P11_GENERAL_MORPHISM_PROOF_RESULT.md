# PA-P11-20260901-UNIVERSAL-MORPHISM-PROOF-001 — general symbolic audit of formation-fixed property maps

**Executed:** 2026-10-23 KST. **Original author:** Kwon Dominicus.
**Source:** \`DSD_Property_Axiom_System_EN(4).pdf\`, printed 2026.09.01, 23 PDF pp; exact SHA256 \`03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c\`.
**Precommit:** [P11_UNIVERSAL_MORPHISM_PROOF_PRECOMMIT.md](P11_UNIVERSAL_MORPHISM_PROOF_PRECOMMIT.md) before the present audit.
**Direct source crosscheck:** Definition 2.1 (printed p6), Definitions 2.3–2.5 (p7–8), PI/PII and C1 (p8–9), Definitions 6.1,6.3,6.7,6.10 and results 6.2,6.4,6.6,6.8,6.9,6.11 (p12–14), Definition 7.1 through Theorem 7.5 (p15). Original PDF not edited.

## A. Source vs conditional statement (critical)

Let \`Av_A(varpi)\` mean that **each carrier in the finite ordered profile** \`sigma(varpi)=(s_1,...,s_m)\` is *supplied* (and inherited carriers already fixed). An **available empty** auxiliary carrier \`X_A(s)=∅\` is supplied and is not an unavailable sort; its product may be empty. An **unavailable** auxiliary carrier has no \`X_A(s)\` at all.

The paper itself makes \`Av_A(varpi)\` essential in Definition 2.5, but its Definition 6.1 **literally** says \`(F3) for every varpi∈Pi_A\` and writes \`phi_varpi:X_A,varpi→X_B,varpi\`. F4 then has a dangling/unqualified \`varpi\`, and F5 refers to \`D_A,varpi\` without explicitly restoring the available-profile guard. A legal source model can declare a kind with unavailable profile. In that case the typed product and primitive relation coordinates are **undefined, not empty**.

The following **conditional general proofs require the clarified map convention G**, not the unrestricted literal F3:
> G: (F3)–(F5) and the per-input reflection conditions in Definition 6.3 apply only to \`varpi∈Pi_A\` with \`Av_A(varpi)\`. Under F1 and a shared signature, \`Av_B(varpi)\` then holds automatically, so every referenced product is defined. Kinds declared but unavailable in A carry no source relation/assignment coordinates.

**Scope verdict:** As written, all-model forward-map category theorem 6.2 needs the guard G; after adding it, its intended proof is valid. This is a *logical qualification proven externally to the literal source wording*, NOT a claim that the PDF already contains G.

## B. Lemma 1 — availability transport

Given forward sort maps \`phi_s:X_A(s)→X_B(s)\` for every A-supplied auxiliary sort, F1 ensures the same sort is supplied in B. Inherited-sort carriers are shared and mapped by identity. Hence for any \`varpi∈Pi_A\` with \`Av_A(varpi)\`, every factor of
\`X_A,varpi = prod_{i=1}^m X_A(s_i)\` exists in both models, and the map
\`phi_varpi((x_i)_i)=(phi_{s_i}(x_i))_i\` exists uniquely as a set function. Neither source nor target product is assigned a value if some factor is unavailable. If a supplied factor is empty, both product and induced map are still well-typed (with empty domain).

**Proved:** for arbitrary finite \`m≥1\` (and also valid for m=0 were it to be used), repeated/mixed/inherited coordinates, with no injectivity or surjectivity assumption.

## C. Lemma 2 — functorial product-map identity

For composable auxiliary maps \`phi:A→B\`, \`psi:B→C\`, and each source-declared available \`varpi\`,
\`\`\`
(psi∘phi)_varpi(x_1,...,x_m)
  = ((psi_{s_i}∘phi_{s_i})(x_i))_{i=1}^m
  = psi_varpi(phi_varpi(x_1,...,x_m)).
\`\`\`
Thus \`(psi∘phi)_varpi=psi_varpi∘phi_varpi\`; the product induced by identity sort maps is identity. Repeated-sort coordinates are not identified; e.g. profile \`(u,u)\` remains a two-coordinate product. Mixed profile \`(u,v)\` is not swapped to \`(v,u)\`. Inherited component maps are identities.

**Proved:** as equality of functions on each available source typed product, independent of its finite cardinality.

## D. Proposition — guarded F1–F5 maps form a possibly large category

Given guarded maps \`A→B→C\`:
- F1: \`AvailSort(A)⊆AvailSort(B)⊆AvailSort(C)\`.
- F2: \`Pi_A⊆Pi_B⊆Pi_C\`.
- On each \`varpi∈Pi_A\` available in A, \`phi_varpi(Ap_A)⊆Ap_B\` and \`psi_varpi(Ap_B)⊆Ap_C\`. Lemma 2 yields \`(psi∘phi)_varpi(Ap_A)⊆Ap_C\`. Same for every prerequisite \`d∈delta(varpi)\`, including \`delta(varpi)=∅\` (no F4 obligations).
- If \`x∈D_A,varpi\` then F5 supplies \`phi_varpi(x)∈D_B,varpi\` and equality \`Xi_B(phi_varpi(x))=Xi_A(x)\`; a second F5 yields \`psi_varpi(phi_varpi(x))∈D_C,varpi\` and equality with \`Xi_A(x)\`. No converse/totality assumed and **assigned zero remains a defined value**.
- On identity maps every condition is satisfied. Associativity is associativity of ordinary set functions.

Therefore guarded forward maps are closed under identities/composition. With fixed set-sized signature each individual \`Hom(A,B)\` consists of set-indexed families of set maps and is a **set**, though the object family across all models may be a proper class; hence *possibly large category* is appropriate.

**General verdict:** theorem 6.2 **PROVED UNDER EXPLICIT G**; \`SOURCE_AS_WRITTEN = CONDITION_MISSING\` for all admitted source models.

## E. Embeddings / inclusion preorder

For an embedding, injectivity of sort components is stable under composition. For each source-declared profile-available \`varpi\` and typed \`x\`, if relation membership is reflected as a biconditional \`x∈R_A iff phi_varpi(x)∈R_B\` for \`R=Ap,Sat_d,D\`, and the analogous B→C reflection holds, chaining equivalences gives \`x∈R_A iff (psi∘phi)_varpi(x)∈R_C\`. F5 supplies the defined values; no target-to-source declaration equality is used. Consequently guarded embeddings form a **wide subcategory**.

Literal carrier inclusions compose, so the source's \`≼\` is reflexive/transitive (preorder) under this same scope; no antisymmetry is needed for the published result. Having an extra target-declared kind is permitted in an embedding and does not force an extra declaration in A.

**General verdict:** propositions 6.4 and theorem 6.6 **PROVED UNDER G**, not under undefined products.

## F. Strict S1–S4 and the *minimal* sufficient repair

The source's strict-isomorphism notion is **Definition 6.7 S1–S4**, not mere componentwise carrier bijectivity.
If \`A→B\` is a guarded **embedding** with:
1. \`phi_s\` bijective for all A-available sorts (**S1**);
2. availability-sort sets equal (**S2**);
3. property declaration sets equal (**S3**);
then source/target typed input products are both available or both unavailable per kind. For each available kind, the induced \`phi_varpi\` is bijective (finite product of bijections, even if empty).
Since reflection gives \`x∈R_A iff phi_varpi(x)∈R_B\`, every target input \`y\` has a unique preimage and the inverse maps preserve/reflect \`Ap,Sat_d,D\`. On \`D_B\`, value preservation reverses because \`Xi_B(phi_varpi(x))=Xi_A(x)\`. Hence **the inverse is itself a guarded embedding**.

Thus (S4) is **derivable** from embedding + (S1–S3), assuming Definition 6.3's source reflection on all available typed inputs. This is **a redundancy/clarification insight**, not a contradiction: Definition 6.7 may safely state S4 explicitly. What cannot be omitted is S2/S3. Specifically, a carrierwise bijective embedding with \`Pi_A⊊Pi_B\` violates S3, and one with \`AvailSort(A)⊊AvailSort(B)\` violates S2, even when every existing component map is bijective.

Therefore full S1–S4 maps include identities, inverse maps, and composites and strict property equivalence is reflexive, symmetric, transitive. **Theorem 6.8's first assertion survives; the bare “exactly the bijective property embeddings” shorthand is mathematically incomplete on its natural carrierwise reading.**

**General verdict:** strict equivalence relation **PROVED UNDER G + S1–S4**. Characterization as simply carrierwise-bijective embedding **DISPROVED** (P9A/P10 explicit legal models).

## G. Preservation of C1, stage comparisons and representations

A strict map preserves the **full primitive coordinates**, so:
- \`D_A,varpi\` maps onto \`D_B,varpi\`;
- \`DepSat_A,varpi=⋂_{d∈delta(varpi)}Sat_A,varpi,d\` maps onto the target intersection, including empty \`delta\` where \`DepSat_A=X_A,varpi\`;
- the status partition and complete typed record triples \`(varpi,x,z)\` map bijectively, with labels/ordered inputs and values retained.
This proves Proposition 6.9 **under G+S1–S4** without any universal finite cardinality assumption.

Stage comparison families \`I_k\` contain **all** compatible carrier-bijection families. Nestedness is cumulative by definition; \`I4=I5\` follows since all Stage-5 data are functions of primitives under C1. This holds even with a *supplied empty* auxiliary carrier: the product is genuinely empty and no new arbitrary completion data exist. Strict comparison at Stage4 is equivalent to S1–S4 strict maps (with availability and declaration set checks), and inverse/prepost-composition of bijection families establishes symmetry/invariance. Do not replace \`I_k\` with a single chosen forward map.

For optional representation packages, a strict core isomorphism does NOT determine encoding equality automatically. Under the **additional** Definition 6.10 equal active representation labels, corresponding selected record-tuple domains and commuting encoding maps, inverse/composition preserve the equality; Theorem 6.11's equivalence claim is valid **on that represented scope**. No claim is made that every core strict map admits such a lift.

## H. Failure search / boundaries from source alone

- **Declared but profile unavailable:** legal as Def2.5, but literal F3 undefined. Confirmed source-level condition gap P5-A, no surprise empty-set substitution.
- **Available carrier = empty set:** defined and differs from unavailable. The induced typed product can be empty, and relations/maps on it are empty; category/strict proof above still applies.
- **Two independent prerequisite kinds:** F4 preserves each set separately, so the intersection is preserved; embedding reflects each and strict bijections transport the full intersection.
- **Mixed/repeated profiles:** composition identity is coordinatewise and does not permute kinds or coordinate slots.
- **Value zero and nonzero:** treated by domain membership and exact equality, never conflated with undefinedness.
- **No third universal counterexample obtained from this proof check.** This is not an assertion that none exists.
- **Full formal verification status:** these are independently constructed human-readable mathematical derivations of the *conditional* theorems. They have NOT been compiled into Lean/Coq/Isabelle or otherwise machine-checked, and external review is not established.

## P11 outcome

\`\`\`text
CASE: PA-P11-20260901-UNIVERSAL-MORPHISM-PROOF-001
GENERAL_PROFILE_AVAILABILITY_LEMMA: PROVED
GENERAL_PRODUCT_COMPOSITION: PROVED
FORWARD_CATEGORY: PROVED_CONDITIONAL_ON_G
EMBEDDING_WIDE_SUBCATEGORY: PROVED_CONDITIONAL_ON_G
INCLUSION_PREORDER: PROVED_CONDITIONAL_ON_G
STRICT_EQUIVALENCE_RELATION: PROVED_CONDITIONAL_ON_G_AND_S1_S4
S4_DERIVABLE_FROM_EMBEDDING_PLUS_S1_S3: YES (under G and full reflection)
BIJECTIVE_CARRIER_COMPONENTS_IMPLY_STRICT_ISO: FALSE
C1_COMPLETION_AND_I4_I5: PROVED_UNDER_STRICT_SOURCE_PRESERVATION
OPTIONAL_REPRESENTATION_EQUIVALENCE: PROVED_ON_EXPLICIT_LIFT_SCOPE
PAPER_DEF6_1_LITERAL_F3_F5_SCOPE: CONDITION_MISSING
PAPER_TH6_8_BARE_BIJECTIVE_EMBEDDING_SHORTCUT: CONDITION_MISSING
UNIVERSAL_MACHINE_FORMALIZATION: NOT_PERFORMED
EXTERNAL_INDEPENDENT_VALIDATION: NOT_ESTABLISHED
AUTHOR_PDF_TEX_ZENODO_ORIGINAL_PYTHON_CHANGED: NO
WHOLE_PROPERTY_FPA: OPEN
\`\`\`

**Next source-only gate:** controlled boundary check on *available-but-empty vs unavailable*, inherited-sort identity and ≥2 prerequisite sets; then revisit which prior proof statuses can be upgraded from conditional to complete only if the missing hypotheses are made part of the actual manuscript. Do not undertake author source edits as part of this mathematical audit.
