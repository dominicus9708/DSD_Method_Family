# DSD Audit — Collatz proof architecture full audit

```text
STATUS: COMPLETED
AUDIT_ID: DSD-AUDIT-20260907-MATH-001
TITLE: Collatz proof architecture full analysis and audit
DOMAIN: Mathematics / Number theory / Dynamical arithmetic
DATE: 2026-09-07
AUDITOR_OR_AGENT: ChatGPT GPT-5.6 Sol with exact-arithmetic reconstruction
RELATED_SOURCE_OR_CASE: dominicus9708/Math-verification, collatz/
METHODOLOGY_VERSION: DSD separated audit framework, repository main as of 2026-09-07
```

---

## 1. DSD interface lock

```text
FORMATION_LAYER: not required as a mathematical axiom layer; structural language only
PROPERTY_CORE: not required as a mathematical axiom layer
STATIC_AGGREGATION_LAYER: used descriptively for aggregate-vs-pointwise audit
DYNAMICS_LAYER: used descriptively for orbit-transition lineage
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: exact discrete dynamical-system / number-theory protocol
SOURCE_VERSIONS:
  - DSD_Method_Family/DSD_Audit/README.md
  - DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md
  - DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md
  - Math-verification main audited through commit 13fcbb21bd9d4ddbf03b64b2668f023bdbd690ea
```

DSD Analysis/Audit is used only as an audit and decomposition framework. Mathematical validity remains governed by ordinary proof standards.

---

## 2. Audit question

```text
PRIMARY_QUESTION:
Which parts of the current Collatz proof program are mathematically established within their stated scope, which are conditional or finite only, which bridges remain open, and does the current architecture constitute a complete proof?

QUESTIONS_NOT_BEING_DECIDED:
- authorship or priority of historical external results;
- peer-review decisions for internal notes;
- whether an unknown future theorem could complete one of the open bridges;
- philosophical validity of DSD as a replacement for mathematical proof (it is not used that way here).
```

---

## 3. Scope

```text
TARGET_SCOPE:
Current Collatz proof architecture in dominicus9708/Math-verification, emphasizing universal minimal-counterexample, first-crossing/Farey, root-Hensel, recursive-sufficiency/COV, and R1/R2 renewal routes.

TIME_SCOPE:
Repository state through 2026-09-07; external computational status checked on 2026-09-07.

DESCRIPTIVE_RESOLUTION:
Exact integers, exact rational intervals, parity words, dyadic residue classes, 2-adic inverse limits, finite exhaustive certificates, and explicitly labeled aggregate/statistical statements.

INCLUDED_MATERIAL:
Published-floor spine; Farey cells; first-cell start bounds; root-Hensel theorems; 1024-block rotation cap; Ansari dependency audit; COV-1; inverse-limit ghost criterion; eventually-periodic ghost theorem; R1/R2 dichotomy; external-literature audit matrix; failed-route regression notes.

EXCLUDED_MATERIAL:
Unrelated Collatz visualizations or exploratory code not used by current proof architecture.

EXTERNAL_STANDARD:
Universal mathematical proof with exact preservation of hypotheses and quantifiers; finite computation is finite evidence unless a separate theorem globalizes it.

ASSUMPTIONS:
Frozen paper-facing computational baseline B_pub=2^71 from Barina 2025. Current live frontier beyond this is treated separately as time-sensitive operational evidence.
```

---

## 4. Original source preservation

### Internal principal source

- Repository: `dominicus9708/Math-verification`
- Current synthesis: `collatz/notes/2026-09-07-full-proof-architecture-analysis-and-status.md`
- Cross-check: `collatz/src/2026_09_07_full_core_audit_regression.py`

### External computational source

Published:

- David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI `10.1007/s11227-025-07337-0`.
- Published result: convergence verified below the `2^71` frontier.

Current operational snapshot retrieved on 2026-09-07:

- `https://pcbarina.fit.vutbr.cz/`
- reports convergence below `2075 * 2^60`.
- This newer value is not silently substituted into frozen published-floor theorems.

### Current external problem status

Web review on 2026-09-07 found no accepted universal proof or counterexample. A September 5, 2026 Lean-checked positive-density/log-time result explicitly states that the full Collatz conjecture remains open. This does not alter the internal universal pointwise obligations.

---

## 5. Evidence status

### ESTABLISHED_WITHIN_SCOPE

1. Shortcut-map affine parity identity.
2. Published-floor minimal-counterexample implication `N>2^71`.
3. Minimality prefix inequality and resulting narrow first-crossing strip.
4. Exact first Farey cell
   `(A0,q0)=(114208327604,72057431991)`.
5. Exact two-cell list through `(217976794617,137528045312)`.
6. First-cell buffered bound `N<2^72`.
7. Root full-Hensel maximality theorem for the original minimal start.
8. Published-floor root-safe transition: depth 195, first envelope failure `(196,124)`.
9. Correction-only barrier: scalar correction alone cannot close the full first cell.
10. Exact 1024-block rotation maximum bound and resulting first-cell cap
    `N<1365*2^61`.
11. Exact reduction of the first-cell top-11-bit source alphabet to 341 blocks.
12. Exact finite m44 selector computations within their enumerated families.
13. COV-1 dyadic/inverse-limit parameter theorem.
14. Eventual stabilization of least residues iff the inverse-limit parameter is a nonnegative ordinary integer.
15. Eventually-periodic coefficient-surviving symbolic paths are negative rational ghosts.
16. R1/R2 renewal coefficient-stopping dichotomy as a structural split.

### UNDETERMINED_OR_INSUFFICIENT

1. Emptiness of the 341-block first-cell same-integer intersection.
2. Complete depth-195 nested root-max survivor intersection.
3. Universal exclusion of all later Farey strip cells.
4. Universal recursion of `36N_0+27` (`COV_1`).
5. General higher removed-layer `COV_n` theorem.
6. Repaired Ansari ternary recursive-sufficiency coverage.
7. `V33` as an unconditional global minimal-counterexample floor.
8. Genuinely aperiodic coefficient-surviving positive-natural exclusion.
9. Complete R1 and R2 elimination.
10. Full Collatz conjecture.

### OUT_OF_SCOPE

1. Claiming that DSD itself proves a number-theory theorem without domain mathematics.
2. Priority/novelty adjudication for all external literature.

---

## 6. DSD object status

```text
FORMATION_STATUS:
Not used as a proof prerequisite. Parity-prefix construction is fully described as ordinary discrete mathematics.

PROPERTY_STATUS:
Exact properties (parity, correction, residue, valuation counts) are explicitly defined.

STATIC_ANALYTIC_STATUS:
Aggregate correction and finite-count summaries are valid only at their declared resolution.

DYNAMIC_STATUS:
Orbit transition identities and renewal lineage are explicit; some global transition bridges remain open.

STATUS_SIDE_INFORMATION:
The project contains historical notes with legacy stronger scopes. Current dependency audits supersede those scopes without deleting historical records.
```

---

## 7. Selection and exclusion

### Available proof routes

1. Universal minimal-counterexample / Farey first-crossing route.
2. Recursive-sufficiency / ternary COV route.
3. Renewal R1/R2 route.
4. Statistical/Fourier/finite-state auxiliary routes.

### Selected current universal target

The audit supports prioritizing the **same-integer first-cell transfer** because it is an exact finite-address obligation:

\[
341\text{ root blocks}
\cap
\text{nested root-Hensel constraints through 195}
\cap
\text{first-cell terminal extension}.
\]

### Excluded as standalone closure mechanisms

- scalar correction only;
- measure-zero or density decay;
- finite-depth survivor counts;
- fixed finite-state quotient without injective reconstruction;
- arbitrary later-block Hensel maximality;
- `V33` without repaired coverage.

### Post-hoc change check

Failures found in earlier routes were preserved as explicit regression rules rather than removed to make surviving cases look stronger. This passes the DSD post-hoc exclusion safeguard.

---

## 8. Bridge declarations

### Bridge B1 — published computation to minimal-counterexample floor

```text
SOURCE_LAYER: external exhaustive computation
DOMAIN: positive integers below 2^71
CODOMAIN: hypothetical minimal counterexample
ASSUMPTION: Barina 2025 verified frontier accepted as external computational theorem
JUSTIFICATION: all smaller starts converge; 2^71 itself is even and maps below the verified floor
STATUS: JUSTIFIED
```

### Bridge B2 — minimality to prefix lower bound

```text
DOMAIN: original minimal counterexample orbit
CODOMAIN: parity-count inequality
ASSUMPTION: any smaller positive iterate converges
JUSTIFICATION: direct minimality argument
STATUS: JUSTIFIED
```

### Bridge B3 — Farey strip to first cell equality

```text
DOMAIN: q/A in narrow strip
CODOMAIN: A=A0
JUSTIFICATION: unavailable
STATUS: UNSUPPORTED
```

Only `A>=A0` is established.

### Bridge B4 — aggregate correction to first-cell source cap

```text
DOMAIN: all first-crossing words
CODOMAIN: scalar upper start bound
ASSUMPTION: mechanical word termwise maximizes correction
JUSTIFICATION: exact rotation-block maximum
STATUS: JUSTIFIED FOR THE CAP
```

### Bridge B5 — aggregate correction to cell emptiness

```text
DOMAIN: scalar correction upper bound
CODOMAIN: no same-integer start exists
JUSTIFICATION: missing dyadic address
STATUS: UNSUPPORTED
```

### Bridge B6 — root Hensel alternate word to smaller start

```text
DOMAIN: original root prefix, same full-Hensel class
CODOMAIN: exact smaller merging start N-Delta
ASSUMPTION: 0<Delta<N
JUSTIFICATION: affine identity and divisibility
STATUS: JUSTIFIED
```

### Bridge B7 — arbitrary later block to root-minimality Hensel rule

```text
JUSTIFICATION: root minimality no longer applies to arbitrary later state
STATUS: CONTRADICTED by prior regression
```

### Bridge B8 — finite COV witnesses to one natural parameter

```text
DOMAIN: for every L exists k_L
CODOMAIN: exists one k for every L
JUSTIFICATION: quantifier swap unavailable
STATUS: UNSUPPORTED
```

### Bridge B9 — nested COV residues to 2-adic inverse limit

```text
JUSTIFICATION: exact compatible residues
STATUS: JUSTIFIED
```

### Bridge B10 — 2-adic inverse limit to ordinary natural

```text
JUSTIFICATION: eventual stabilization of least nonnegative representatives
STATUS: JUSTIFIED iff stabilization is proved
```

### Bridge B11 — finite m44 selector closure to universal V33 floor

```text
ASSUMPTION: repaired ternary recursive-sufficiency coverage
STATUS: CONDITIONALLY_JUSTIFIED
```

### Bridge B12 — measure/density decay to emptiness

```text
JUSTIFICATION: no atom-floor/injective pointwise bridge
STATUS: UNSUPPORTED
```

---

## 9. Proposition layers

### Fact

- Exact algebraic identities and exact finite certificate outputs.
- Published computational frontier.
- Current live operational frontier snapshot.
- Historical counterexamples to invalid proof mechanisms.

### Inference

- Minimal counterexample must obey prefix and Hensel constraints.
- First-cell start is confined to the current cap.
- Eventually-periodic coefficient survivors are not positive ordinary starts.

### Norm

- Universal Collatz proof requires universal pointwise coverage or an equivalent theorem.
- Finite/density evidence is not universal proof without a bridge.

### Decision

- Current repository verdict is partial, not complete.
- The 341-block same-integer transfer is the highest-value immediate universal experiment.
- Later strip cells and aperiodic R2 must remain visible as separate global obligations.

---

## 10. Transition and lineage audit

| Step | Prior state/evidence | Transition | Next conclusion | Identity preserved? | Status |
|---|---|---|---|---:|---|
| 1 | Barina published floor | minimal-counterexample selection | `N>2^71` | yes | JUSTIFIED |
| 2 | minimal `N` | smaller iterate argument | all iterates `>=N` | yes | JUSTIFIED |
| 3 | prefix inequality | log/Farey encoding | narrow `q/A` strip | yes | JUSTIFIED |
| 4 | narrow strip | Farey neighbors | `A>=A0` | yes | JUSTIFIED |
| 5 | `A>=A0` | choose first cell | `A=A0` | no | UNSUPPORTED if universalized |
| 6 | first cell | buffered co-order | `N<2^72` | yes | JUSTIFIED |
| 7 | first-cell words | 1024-block aggregation | `N<1365*2^61` | address aggregated | JUSTIFIED for scalar cap |
| 8 | scalar cap | infer emptiness | no starts | no | UNSUPPORTED |
| 9 | root prefix | Hensel merge credit | root-max obligation through 195 | yes | JUSTIFIED |
| 10 | later block | reuse root minimality | later-block max | no | CONTRADICTED |
| 11 | finite COV levels | varying witnesses | one natural witness | no | UNSUPPORTED |
| 12 | nested COV residues | inverse limit | `k_infty in Z_2` | yes | JUSTIFIED |
| 13 | stabilized residues | ordinary reconstruction | `k_infty in N_0` | yes | JUSTIFIED |
| 14 | periodic survivor | fixed-point sign | negative rational ghost | yes | JUSTIFIED |
| 15 | finite selector layers | Ansari coverage | universal V33 | conditional | CONDITIONALLY_JUSTIFIED |

---

## 11. Alternative describabilities

### Alternative A — density/statistical description

Compatible with Tao-style almost-all results and Fourier transport.

Evidence against universal closure:

- exceptional set need not be empty;
- current proof target is a single hypothetical minimal ordinary integer.

Excluded as standalone universal proof: **yes**.

### Alternative B — finite-state quotient

Useful if the quotient is a right-congruence preserving every future obligation.

Evidence against naive fixed quotient:

- explicit state-aliasing regressions in the repository;
- unbounded 3-adic memory witnesses for mixed reverse compatibility.

Excluded as naive fixed-resolution closure: **yes**.

### Alternative C — exact same-integer address transfer

Compatible with all current safe lemmas and retains root identity.

Excluded: **no**.

This is the selected next target.

---

## 12. Aggregation and reconstruction

```text
OUTPUT_EQUALITY_CHECK:
Exact affine endpoint identities pass.

SUPPORT_EQUALITY_CHECK:
Aggregate correction bounds do not preserve exact dyadic support.

DECOMPOSITION_RETENTION_CHECK:
1024-block rotation bound intentionally loses address decomposition.

INJECTIVITY_ESTABLISHED:
Parity word <-> dyadic residue mod 2^k is injective at fixed depth.
Finite-state coarse quotients are not generally injective.

COLLISION_WITNESS:
Repository contains explicit FSM/mod-64 aliasing regressions.

KERNEL_OR_INFORMATION_LOSS_CHECK:
Major open point: correction aggregation discards the same-integer address needed for cell closure.

RECONSTRUCTION_CLAIM:
Valid only when exact nested residue lineage is retained or eventual stabilization is proved.
```

---

## 13. Witnesses and counterexamples

```text
MINIMAL_POSITIVE_WITNESS:
None; no Collatz counterexample is known.

MINIMAL_COUNTEREXAMPLE:
Hypothetical object only.

BOUNDARY_CASES:
- first Farey cell A0,q0
- root-Hensel safe/fail transition 195/196
- first-cell cap boundary 1365*2^61
- periodic ghost examples -1 and -5

FINITE_EXHAUSTIVE_RANGE:
COV-1 first-crossing certificate through binary depth 38; recorded 150,456,308 words, zero paradoxical within that finite range.

UNTESTED_REGION:
Arbitrary depth; later Farey cells; 341-block same-integer depth-195 intersection; genuinely aperiodic survivor boundary.
```

---

## 14. Contradiction audit

```text
DEFINITION_CONTRADICTION:
No new definition contradiction found in the current safe core.

TRANSITION_CONTRADICTION:
Historical arbitrary later-block Hensel maximality is invalid and remains withdrawn.

STRUCTURAL_CONTRADICTION:
No new contradiction found in Farey/root-Hensel/1024-block core after independent exact reconstruction.

CLAIM_CONTRADICTION_OR_OVERREACH:
Historical unconditional V33/current-resonance interpretations exceed the now-audited coverage basis. They are legacy scope overclaims, corrected by later dependency notes.

OMISSION:
A complete proof would still need later strip cells and the genuinely aperiodic coefficient-survival branch even after first-cell closure.
```

---

## 15. Eight-axis summary

| Axis | Audit result |
|---|---|
| D — Describability | CONFIRMED: main objects and assumptions are explicit. |
| R — Resolution | PARTIALLY_CONFIRMED: current notes distinguish exact, aggregate, finite, and density scales better; some historical files predate this discipline. |
| S — Selection | CONFIRMED with warning: selected subproblems are legitimate but not exhaustive. |
| E — Exclusion | PARTIALLY_CONFIRMED: exact exclusions pass; finite/density universalization is prohibited. |
| T — Transition | UNDETERMINED globally: same-integer correction/address bridge and ternary coverage remain open. |
| C — Consistency | PARTIALLY_CONFIRMED: current status is coherent; legacy stronger scopes require precedence rules. |
| N — Norm | CONFIRMED: ordinary mathematical proof standard is explicit. |
| O — Outcome | PARTIALLY_CONFIRMED: strong partial reductions, no complete proof. |

---

## 16. Final verdict

```text
VERDICT: PARTIALLY_CONFIRMED

VERDICT_BASIS:
The current architecture contains several exact, independently reproducible intermediate theorems and correctly downgraded failed mechanisms, but material universal bridges remain open.

MAXIMUM_SUPPORTED_CLAIM:
A hypothetical minimal positive counterexample above the published floor is heavily constrained; in the earliest universal first-crossing cell it must lie in a 341-block top-address region and satisfy nested root-Hensel maximality through depth 195, while eventually-periodic coefficient-survivor symbolic tails are excluded from positive ordinary integers.

UNSUPPORTED_OR_UNRESOLVED_CLAIMS:
- first cell is the only possible first crossing;
- 341-block same-integer intersection is empty;
- V33 is an unconditional universal floor;
- COV-1 or all COV_n are closed;
- all genuinely aperiodic coefficient-survivors are non-natural;
- full Collatz conjecture is proved.

EXTERNAL_DOMAIN_VERDICT:
Collatz remains open.

DSD_STRUCTURAL_AUDIT_VERDICT:
Current proof architecture passes as a disciplined partial-reduction program, not as a complete proof.

CORRESPONDENCE_AND_LIMITS:
DSD audit findings correspond directly to mathematical dependency/lineage issues, but DSD labels do not establish unresolved mathematical bridges.
```

---

## 17. Reproducibility and traceability

```text
REQUIRED_SOURCES:
- Math-verification/collatz notes cited by the current synthesis
- 2026_09_07_full_core_audit_regression.py
- Barina 2025 published paper
- official Barina project frontier page snapshot for live sensitivity only

REVIEW_OR_EXECUTION_ORDER:
1. published-floor/Farey certificate
2. root-safe Hensel certificate
3. correction-only barrier certificate
4. 1024-block start-cap certificate
5. 2026-09-07 full core audit regression
6. COV/R1/R2 dependency notes

REPOSITORY_AND_PATH:
- dominicus9708/Math-verification/collatz/
- dominicus9708/DSD_Method_Family/DSD_Audit/

COMMIT_SHA:
Math synthesis commit: 13fcbb21bd9d4ddbf03b64b2668f023bdbd690ea
Core audit regression commit: 9405390bb107c3dd6584bcb2fd4967ec137773a5

ENVIRONMENT:
Python exact integer/Fraction arithmetic for reconstructed certificates.

DEPENDENCIES:
Python standard library for the full core regression.

INPUTS:
Fixed published floor, exact rational cell constants, exact parity/correction formulae.

RANDOM_SEED:
Not applicable.

TOLERANCE:
None in certificate assertions; no floating-point proof comparison.

GENERATED_OUTPUTS:
PASS/FAIL regression output and current status documents.

RELATED_NOTION_PAGE:
Not modified in this audit.
```

Repository combined status on the audited latest Math-verification head returned no attached status checks. Thus reproducibility is script-based but not presently CI-enforced.

---

## 18. Follow-up

- [x] Independent exact reconstruction of main published-floor/Farey transition
- [x] Independent exact reconstruction of root-safe depth 195
- [x] Independent exact reconstruction of the 1024-block maximum inequality
- [x] Separate published floor from current live operational frontier
- [ ] Build address-preserving transfer for the 341 first-cell root blocks
- [ ] Compute/characterize the depth-195 same-integer intersection
- [ ] Develop a uniform later-Farey-cell theorem
- [ ] Eliminate genuinely aperiodic coefficient-survival natural starts
- [ ] Repair or replace the general ternary `COV_n` coverage theorem
- [ ] Add CI enforcement for lightweight core audit regressions

---

## 19. Revision and migration log

```text
REVISION_DATE: 2026-09-07
PREVIOUS_DSD_INTERFACE_PROFILE: legacy integrated DSD analysis/audit records in Math-verification
CURRENT_DSD_INTERFACE_PROFILE: separated DSD Audit framework
CHANGED_SCOPE:
Reclassifies historical universal selector-floor claims after the Ansari coverage audit and incorporates the 2026-09-06 first-cell 1024-block reduction.

NEW_SOURCE:
Current official Barina project live frontier snapshot; current DSD General Audit Framework.

MIGRATION_STATUS: COMPLETED

LEGACY_TERMINOLOGY:
Historical SAFE labels remain in old files but are scope-qualified by current dependency audits.

CHANGED_VERDICT:
No full-proof verdict. Current architecture = PARTIALLY_CONFIRMED.

REASON:
Exact intermediate results survive, but coverage, same-integer, later-strip, and aperiodic-survivor bridges remain unresolved.
```
