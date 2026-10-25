# PA-P23-20260901-SOURCE-FAITHFUL-FINITE-STAGEVI-TO-PROPERTY — audit result

**Status:** COMPLETE / finite-source-domain scope only (2026-10-25 KST).
**Author:** Kwon Dominicus.
**Frozen preregistration:** [P23 plan](P23_REAL_STAGEVI_TYPED_DESCRIPTOR_REGRESSION_PRECOMMIT.md), authored before tests.
**Original Property source:** \`DSD_Property_Axiom_System_EN(4).pdf\`, 2026.09.01, 23 pages, SHA256 \`03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c\`.
**Revised Formation source:** \`DSD_Formation_Axiom_System_EN.pdf\` / original new-edition EN(7), dated 2026.10.22, 34 pages, SHA256 \`af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe\`.

## 1. What the original sources actually supply

Formation v4.5 §§2.2–3.2 (printed pp.4–9): (B,F), material signature/carrier and induced material relations; candidate expression/configuration classes; material/active subsets and anchors; supplied expression admission/description; restriction and realization primitive relations; supplied configuration admission/coherence/boundary predicates; quantity kinds with pointed values, regime-global partial assignment, roles. Primitive Axioms I/II/III/V impose constraints; Closure IV determines describable configurations and A*, Closure VI determines admitted operational channels from actual assignment graph and role, with identity \`(p,a,lambda,v,rho)\`. Formation trace \`Tr(c)\` is derived witness data and not a sixth channel-coordinate; \`c in C iff Tr(c) nonempty\` is Theorem 3.6. Stage VII supplies term space/map only AFTER Stage VI.

Property original §§2.1–2.5 (printed pp.6–8): the fixed Stage-VI formation truncation is inherited unchanged. General shared property input sorts may be Formation-inherited or auxiliary, with explicitly ordered mixed profiles. Unavailable auxiliary sort is different from an available empty sort; source says some primitive coordinates are **not required** if a profile is unavailable, which does **not automatically ban surplus coordinates**.

## 2. New independent P23 finite constructor

[Python source](scripts/verify_p23_typed_stagevi_adapter.py) builds an explicitly supplied finite \`FormationInput\`, independently validates selected typed forms of Axioms I/II/III/V and induced material restrictions, derives configuration describability and active material, computes regime-global partial assignment graphs, all candidate-channel tuples, admitted channels and independently reconstructed witness-trace sets. It then supplies inherited type-carriers to a separate typed property test implementation, verifies applicability/preconditions/partial assignment axioms, and distinguishes defined zero and unavailable profiles. Unlike P22's purely synthetic one-channel fixture, the P23 channels are derived by the source-style primitive/closure chain.

The finite witness has two material items with an incidence relation, three expression candidates including an unsuccessful candidate, two candidate configurations including one unsuccessful candidate, a proper and identity restriction, a realization, one quantity-kind and one defined-zero assignment. **Two distinct restriction witnesses lead to a single admitted five-coordinate channel**. The failed candidates remain in the full Stage-VI record.

The independent typed Property bridge refuses stale inherited carriers, stale formation records and mutated derived/trace coordinates. It identifies a crucial distinction: source \`StageVI\` full record can differ despite identical \`CL\` when a failed candidate changes, so binding the property layer merely to channels or a literal string cannot certify identity of the whole formation truncation.

### Corrected auxiliary-coordinate policy

While internally reverse-auditing P23, an initial reference policy was stronger than the source: it rejected all surplus primitive coordinates for unavailable profiles, even though the manuscript says these coordinates are not required, not unconditionally forbidden. P23 was amended **before final closure** to separate explicit \`ignore\` / \`reject\` representation policies. A new positive observation accepts redundant unavailable-sort coordinates under \`ignore\`, and a separate negative observation rejects them under explicit \`reject\`. These are implementation policies, **not new source axioms**. Source P20/P22 and the original property paper are unchanged.

## 3. Actual execution and audit trail

Final new independent checks: **29 positive observations and 26 expected-negative rejections = 55 expected observations reproduced**. Rejections include an unadmitted described expression, missing identity restriction, non-admitted restriction target, anchor/material/induced-relation violation, unrealizable active material, quantity assignment outside A*, nonfunctional or out-of-carrier assignment, malformed role or source support, stale inherited property carrier, altered formation digest, typed profile arity error, property PI/PII violations, nonfunctional property assignments, invalid Stage-VII term-domain, and explicit surplus reject policy.

- [Original completed 53-check CI #40186191770](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40186191770): Python 3.10 and 3.12 both success, 28 positive + 25 expected negative, plus P20 and P22 prior archives re-run exactly.
- Updated surplus-policy checks changed the detailed JSON 53 → 55. [#40186285274](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40186285274) and [#40186337891](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40186337891) failed on **expected stale archive equality**, not on the new 55 assertions. The latter run preserves exact newly generated JSON in logs for both versions; both generated documents were independently compared and matched.
- [Final archived full JSON CI #40186378248](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40186378248): Python 3.10 and 3.12 both **completed/success**, each independently regenerated 29 positive + 26 negative flags, and reported \`P23 ARCHIVED FULL JSON EXACT MATCH\`, \`P20 LEGACY FULL JSON REPLAY EXACT\`, and \`P22 PREVIOUS REGRESSION FULL JSON REPLAY EXACT\`.
- Final complete stored evidence: [results/p23_typed_stagevi_adapter.json](results/p23_typed_stagevi_adapter.json).
- P20/P22 original code untouched; workflow verifies preserved P22 Git blob \`f67469a2bf42953866c64e6faf68a6ad2bb532e3\`.

## 4. Boundary and mathematical verdict

**SUPPORTED IN RESTRICTED FINITE SOURCE GRAMMAR:**
- A valid source-style Formation primitive + closure chain can supply derived admitted Stage-VI channels and Formation witness traces consistently to ordered typed inherited Property profiles.
- Stage-VII term-value changes do not rewrite Stage-VI identity; defined zero is not undefined and candidate failure is not an admitted zero channel.
- Full Stage-VI record binding detects differences concealed by comparing only admitted \`CL\`, including failed candidates and altered material annotations.
- Property PI/PII and explicit C1-style status determinations are consistently computable in the exercised admitted finite cases.
- Original P20/P22 regression stored results continue to reproduce on both Python versions.

**NOT ESTABLISHED:**
- This is a finite independent typed subset of the source's general ZFC set-coded formation framework. Its material relation signature is deliberately restricted (a finite incidence relation plus string-typed annotations). It does NOT implement every possible material signature, external-codomain map, \`Lambda_delta\` negligible-status structure, all optional primitive interfaces, all stage projection maps, or strict formation embeddings/isomorphisms.
- The source's v4.5 detailed D2 (57/9/6 boundary construction) was **not** recreated by P23; refer to separate FAS N2 evidence.
- The fingerprint is deterministic for the restricted frozen typed data representation; it is NOT a canonical encoding theorem for arbitrary ZFC formation descriptors.
- A changed predecessor Stage VI record requires corresponding rebinding, but this is not proof that all formation updates automatically invalidate all property values in a physical model.
- No full arbitrary-set formal verification, EN/KR original manuscript pair update, external review, or Zenodo new-version publication was performed.

**Unresolved original Property manuscript defects:** printed §6 Definition6.1/source-profile availability in F3–F5 (guard G) and Theorem6.8 shorthand (bijective embedding alone does not imply strict isomorphism, missing S2/S3); Theorem4.3 ‘relative to C1’ premodel-scope issue. Existing typed-premodel PI/PII independence is supported, but the printed qualifier is OPEN. Both complete Formation and Property FPA remain **OPEN**. Do not promote 55 finite checks into all-case mathematical proof.

## 5. Next preregistered non-edit source audit

[P24 prospective audit plan](P24_PROPERTY_SECTION6_CONDITIONS_PROOF_PRECOMMIT.md) will directly assess the two still-OPEN §6 printed source conditions with proof obligations and countermodels, preserving the original manuscript unchanged until a separate revision decision.

\`\`\`text
P23: COMPLETED / 29 POSITIVE + 26 EXPECTED NEGATIVE FINITE OBSERVATIONS
PYTHON_3_10_AND_3_12: SUCCESS
P23_ARCHIVED_FULL_JSON_REPLAY: EXACT / ACTIONS 40186378248
P20_P22_PRIOR_FULL_JSON_REPLAY: EXACT / SAME ACTIONS
NEW_FORMATION_V45_STAGEVI_TO_PROPERTY: FINITE_TYPED_SOURCE_DOMAIN COMPATIBLE
FULL_ARBITRARY_FORMATION_TYPED_ADAPTER: NOT IMPLEMENTED
PROPERTY_SECTION6_GAPS: 2 OPEN
PROPERTY_THEOREM4_3_RELATIVE_C1: OPEN
FORMATION_WHOLE_FPA: OPEN
PROPERTY_WHOLE_FPA: OPEN
P24: PREREGISTERED / NOT_EXECUTED
ORIGINAL_MANUSCRIPTS_AND_ZENODO: UNCHANGED
\`\`\`

Windows 11 replay from the existing \`DSD_Method_Family\` checkout root, using an output path in the repository's existing result directory:

\`\`\`powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p23_typed_stagevi_adapter.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p23_typed_stagevi_adapter.json
\`\`\`
