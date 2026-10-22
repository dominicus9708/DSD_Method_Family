# PA-P1-P4-20260901-001 — Source-bound typed core / independence / partial-status / completion audit

**Audit executed:** 2026-10-22 KST. Original manuscript author: **Kwon Dominicus**.
Locked English manuscript `DSD_Property_Axiom_System_EN(4).pdf` (printed 2026.09.01, 23 PDF pages, 157854 bytes), SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
Precommitted requirements: [P1_TYPED_PREMODEL_PRECOMMIT.md](P1_TYPED_PREMODEL_PRECOMMIT.md), frozen before mathematical evaluation.

## 1. P1 type-and-scope audit of §§2.1–2.5, printed pp6–8

The shared property signature is `S_prop` over fixed inherited `F_L^{≤6}` with disjoint inherited/auxiliary input sorts, fixed inherited carriers, candidate property kinds `hatPi`, *finite nonempty ordered* typed profile `sigma(varpi)`, value carrier `Z(varpi)`, optional designated zero, prerequisite-kind universe `Delta` and *finite* prerequisite profile `delta(varpi)`. There is **no** universal axis/normal/line carrier.
A property premodel supplies a **partial** auxiliary-carrier map `Xaux_A`, declarations `Pi_A⊆hatPi`, and only for **declared kinds with an available profile** the primitive `Ap_A,varpi⊆X_A,varpi`, `Sat_A,varpi,d⊆X_A,varpi`, and partial `Xi_A,varpi:X_A,varpi ⇀ Z_varpi`.
Type check: every defined pair belongs to a properly typed product; product coordinate order is not silently symmetrized. Empty supplied carriers may produce empty products without producing ill-typed values. Property assignment is **not** inherited Formation `q_L,lambda` and cannot change admitted Stage-VI channels.
Verdict **PASS_WITH_BOUNDARY** for these typed definitions. The later morphism uses of *declared yet profile-unavailable* kinds require a further check (see P5-P7 result).

## 2. P2 primitive axioms and §4 residual non-derivability, printed pp8–11

- PI: `Dom(Xi_A,varpi)⊆Ap_A,varpi`.
- PII: `Dom(Xi_A,varpi)⊆DepSat_A,varpi = ⋂_{d∈delta(varpi)} Sat_A,varpi,d`; when `delta(varpi)=∅`, `DepSat=X_A,varpi` by the explicit empty-intersection convention.
- No converse `Ap⊆Dom(Xi)` or `DepSat⊆Dom(Xi)` is required; permitted partiality is genuine.
- For common one-point well-typed input `X(u)={x}`, one property, `delta(varpi)={d}`, and `Xi(x)=1`:
  - Countermodel 4.1 `Ap=∅`, `Sat_d={x}`: PI false; PII true.
  - Countermodel 4.2 `Ap={x}`, `Sat_d=∅`: PI true; PII false.
  - Both are **typed premodels**, not full admitted models satisfying *both* primitive axioms; therefore they legitimately witness the independence of each residual axiom relative to typing/C1.
- Proposition 4.5 empty `Xi` with both `Ap=DepSat={x}` witnesses both failed converses while PI and PII hold.

Verdict **SUPPORTED** for the concrete non-derivability argument of Theorem 4.3, Proposition 4.4/4.5, Corollary 4.6. Cannot promote finitely executed test cases to a general formal assistant proof.

## 3. P3 complete input statuses, printed p9

For declared `varpi` with an available profile and typed input x:
1. `x∉Ap` ⇒ inapplicable;
2. `x∈Ap\DepSat` ⇒ prerequisite-unsatisfied;
3. `x∈Ap∩DepSat\Dom(Xi)` ⇒ applicable-undefined;
4. `x∈Dom(Xi)` ⇒ defined, including designated zero vs nonzero only for zero-bearing property kinds.

PI+PII imply the last domain lies in `Ap∩DepSat`, so the four applicable-profile cases are disjoint and exhaustive for each typed input; **undeclared** and **profile unavailable** are two distinct kind-level statuses before any `x∈X_A,varpi` exists. Defined zero must never be inferred from undefinedness. If a property kind has no designated zero, the source's defined-zero/nonzero refinement is not imposed.

Verdict **SUPPORTED** for status separation with explicit typing.

## 4. P4 Clause C1 and Theorem 3.7, printed pp9–10

Clause C1 computes `D_A,varpi=Dom(Xi_A,varpi)`, finite-prerequisite satisfaction intersections, deterministic status predicates and complete record set `R_prop_A={(varpi,x,Xi_A,varpi(x)) : x∈D_A,varpi}`. Theorem 3.7's inverse laws follow **definitionally** because primitive reduction forgets exactly these coordinates and every full model requires their recomputation from primitives:
- `RedProp(CompProp(P))=P`;
- `CompProp(RedProp(A))=A`.
This is unique *relative to* the primitive core and the shared typed signature, **not** uniqueness of a primitive core for a given Stage-VI base. It does not introduce recursion, well-foundedness, or totality.
Theorem 8.1's empty declaration gives one trivial full extension for any shared signature. Theorem 8.4's finite compatible data complete by C1; it is a *sufficiency construction* and not a classification of all inputs.

Verdict **SUPPORTED_IN_DECLARED_SCOPE**; **no P1–P4 correction needed in the directly reviewed text**.

## 5. Executed reproducibility evidence, independently scoped

The existing software `dominicus9708/Property_Axiom_System` was **not edited**. Before execution the software repo recorded immutable source blob IDs under `audits/2026-09-01/PA-P1-P4-ORIGINAL-CODE-REPLAY_PRECOMMIT.md`, commit `60867f848dd301dce94daf0ddb17de0aab832812`.
Fresh, actual GitHub Actions execution [run #39733865420](https://github.com/dominicus9708/Property_Axiom_System/actions/runs/39733865420) on that commit **completed success**:
- Python 3.12 job `119674906726`: `Reproduce finite witnesses=success`, `Run unit tests=success`, **7/7 tests**.
- Python 3.10 job `119674906804`: same two success steps, **7/7 tests**.
- Both job logs show `PI countermodel isolates Primitive Axiom I=true`, `PII countermodel isolates Primitive Axiom II=true`, `One-input witness satisfies both primitive axioms=true`, and `Status separation matches the displayed five-state finite witness=true`.
- CI writes generated data in its runner but does not add GitHub artifact uploads or new committed JSON files. Previous `results/` files are original saved fixtures, not artifacts manufactured by this observed run.
- The finite status test's five input statuses do **not** exhaust kind-level undeclared/profile-unavailable states; those are checked by the source-level typed definitions above.

**CAUTION:** a successful CI suite does not machine-prove all set-theoretic theorems. Existing original scripts and all expected constants remained unchanged.

## 6. Outcome and next

```text
AUDIT_CASE: PA-P1-P4-20260901-001
P1_TYPED_PREMODEL: PASS_WITH_BOUNDARY (later map guards separately audited)
P2_PRIMITIVE_AXIOM_INDEPENDENCE: SUPPORTED
P3_DEFINEDNESS_AND_STATUS_SEPARATION: SUPPORTED
P4_UNIQUE_EXPLICIT_COMPLETION_AND_REDUCTION: SUPPORTED_IN_DECLARED_SCOPE
P1_TO_P4_NEW_DIRECT_CONTRADICTION: none
EXISTING_ORIGINAL_SCRIPT_MODIFIED: no
NEW_ACTIONS_RUN: 39733865420 / success
PYTHON_3_10: PASS / 7/7 unit tests
PYTHON_3_12: PASS / 7/7 unit tests
FPA_ENTIRE_PROPERTY_PAPER: OPEN
BILINGUAL_PARITY: UNVERIFIED
EXTERNAL_INDEPENDENT_VALIDATION: not_established
NEXT: PA-P5-P7-20260901-COMPARISON-001 / prospectively locked
```
