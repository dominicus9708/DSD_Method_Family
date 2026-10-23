# PA-P9A-20260901-FINITE-MORPHISM-EXHAUSTIVE-001 — preregistered finite map model checker

**Prospective, unexecuted lock.** Audit date: 2026-10-23 KST; paper author Kwon Dominicus.
Source exact English PDF `DSD_Property_Axiom_System_EN(4).pdf`, 23 pages, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.

## Premodel search space
Use **one auxiliary sort** `u`; two ordered, fixed property-kind labels `p,q`; each profile `(u)`, pointed values `{0,1}`, one contextual prerequisite `d` (singleton prerequisite set). Fix arbitrary common Formation Stage VI record and identical shared signature; only vary Property extension data. The auxiliary sort is either (i) *unavailable* or (ii) *available with one element* `x`. In unavailable models each candidate kind is either declared (but no property-coordinate data) or undeclared. In available models each candidate kind is undeclared or carries all legal `Ap⊆{x}`, `Sat_d⊆{x}`, and optional assignment `Xi(x)∈{0,1}`, respecting PI+PII. Predict family count **4 + 7² = 53 legal full cores**; confirm enumeration rather than force expected outputs.
Only evaluate bijections with the fixed single-element interpretation, so the auxiliary carrier map is the identity for present-to-present, and empty component map for unavailable sources. “Strict” means S1–S4, including equality of available-sort set and declaration set.
The model checker will **not** implement the manuscript's full general many-sorted universe. Report only the finite family.

## Prior-to-run obligations
1. Enumerate all 53 legal cores and count pairs with repaired well-typed forward map, embedding, componentwise-carrier-bijective embedding, and strict-isomorphism.
2. Find executable legal cores with bijective carrier map / embedding but distinct declaration sets, so strict isomorphism fails (P5-B).
3. Show an explicitly legal declared-unavailable source model where the source's literal “for every declared ϖ” F3 product is undefined; assess identity typing at that point, not silently treating undefined as empty.
4. Exhaustively check identity, composition and inverse for all *well-typed* source-guarded forward maps, embeddings and strict isomorphisms on the 53 finite legal cores. Preserve target declaration inclusions and inherited fixed Formation background.
5. Compute all Stage-1 to Stage-5 bijection comparison sets for 53² model pairs with exact primitive stages; independently check `I4=I5`, nesting, strict-iso iff nonempty `I4`, symmetry and invariance for this finite family, and demonstrate first branch at stages 1–4 if models exist.
6. Check that case results are not being inferred from existing `Property_Axiom_System` 7-unit-test suite; that suite checks separate finite witnesses and has newly observed CI run #39733865420, but does **not** test these declared-unavailable model edges.
7. Archive executed Python + JSON in current new general-Property FPA version `scripts/`, `results/` (distinct from software repo); re-execute locally and verify hashes/blob identity after GitHub upload.
8. The mathematical recommendation will be explicitly conditional on the finite model search; no universal theorem is proven merely by 53 finite cores. No edit to author PDF/TeX/Zenodo or original experimental Python.
9. If general theorem has a further issue requiring beyond-this-scope proofs, mark OPEN for later 56-item inventory and separately preregister. No code output inventing.

```text
PRECOMMIT: PA-P9A-20260901-FINITE-MORPHISM-EXHAUSTIVE-001
PROGRAM: NOT_EXECUTED
MATHEMATICAL_VERDICT: NOT_REVIEWED
FPA_FULL: OPEN
```
