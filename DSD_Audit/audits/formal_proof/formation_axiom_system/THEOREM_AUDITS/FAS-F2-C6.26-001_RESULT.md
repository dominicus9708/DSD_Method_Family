# FAS-F2-C6.26-001 — Channel-cardinality obstruction / 채널 수 장애

**2026-10-20 KST · Existing DSD Audit / Formal Proof Audit v0.1 · One source-bound corollary, not a whole-manuscript certification**

```text
AUDIT_CASE: FAS-F2-C6.26-001
SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, supplied 33 pp
SOURCE_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCUS: Section 6.5 Corollary 6.26, printed p.24
PREREQUISITE: Corollary 6.12 and Definition 6.10 E1–E9; Clause VI for C
PRECOMMIT_COMMIT: b52c46bf24077d891e44cac2487593b844ced066
PYTHON_FINAL_COMMIT: 4dfe6f3cffa73d7dfb31dc61edb7fb1490267c22
PYTHON_FINAL_GIT_BLOB_SHA: 5eee91f7f09a617906558467510e124dee2bd33f
PYTHON_FINAL_SHA256: 83aab72820a9961f4538fbd3b920c8f9494ae2d0275a3d633aaef40366fa130b
JSON_COMMIT: 98c126c897f24cae3af9526923222eef45dbe473
JSON_GIT_BLOB_SHA: 2b08002eeba3756d1d463f23561ff99ee06d6f7f
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
FPA_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
NEXT: FAS-F2-T7.1-001 / NOT_STARTED
F2_WHOLE_PAPER: OPEN
INDEPENDENT_EXTERNAL_VALIDATION: not_established
SOURCE_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
```

## 1. Exact original corollary and general proof

Source §6.5, printed p.24: **“Corollary 6.26 (Channel-cardinality obstruction). If |C_L| ≠ |C_M|, then no strict base-fixed formation isomorphism exists.”**

The claim applies to two **full formation descriptors** over a fixed pair (B,F), with **C_L,C_M the actually admitted-channel sets produced by Closure Clause VI**. It is NOT a claim about candidate channels U, the number of role labels, family multiplicities, trace-witness counts or equality of the composite values.

Suppose for contradiction that a strict base-fixed formation isomorphism `Phi:Sigma_L→Sigma_M` existed. Definition 6.10 provides typed carrier/kind/role/zero-preserving value bijections and an F-linear term isomorphism satisfying E1–E9. **Corollary 6.12**, previously audited in its own FPA, then induces a **bijection** `hatPhi_C:C_L→C_M`, because E1–E8 preserve and reflect the defining conjuncts of Clause VI. Set cardinality is preserved by a bijection, so `|C_L|=|C_M|`, contradicting the hypothesis. Hence no strict formation isomorphism exists.

This conclusion holds for **any set-sized admitted-channel sets, finite or infinite**: by definition, different cardinalities mean no bijection. No new primitive axiom, finiteness premise, or numerical aggregation rule is required. It also follows as a necessary-condition instance of T6.23, but using C6.12 gives a direct structural proof.

**Careful limits of inference:** Equal `|C|` is only necessary, not sufficient for strict isomorphism. Different `|C|` does not specify which primitive difference caused channel loss, and does **not** by itself prove the first branching index `b=6`; earlier stage comparisons might already have failed. Nor can a zero-valued term or empty composite be substituted for an absent channel. The channel set C is determined by genuine describability, defined global assignment and role relation, rather than arbitrarily supplied cardinality.

## 2. Source-compatible full Formation model witness with nonempty typed comparisons

Construct two full Formation models over the **same** fixed base `Supp(B)={s0}` and field `F=F2`, empty material-record relational signature, and identical primitive carriers:

```text
M_B={a}, E_B={h}, P_B={p}, Lambda={lam}, R={r,s}
mat(h)=act(p)={a}, anch_h(a)=anch_p(a)=s0
Adm_expr(h)=Des_expr(h)=true
Res(h,h)=Realize(h,p)=true
Adm_cfg(p)=LC(p)=BC(p)=true
V_lam={0}, pointed zero 0
Q_lam={a}, q_lam(a)=0 (DEFINED)
Lambda_delta=empty
```

Primitive Formation Axiom I (expression admission), II (identity restriction/sound anchors), III (realization/material-active/anchor soundness), and V (global partial assignment domain inside A*, value correctly typed) all hold. Clause IV yields `Psi(p)=true`, `K_des={p}`, `A*=A={a}`.

The ONLY difference between the two primitive inputs is their role relation:

```text
L: Role(p,a,lam,r).                   C_L={(p,a,lam,0,r)}.
M: Role(p,a,lam,r), Role(p,a,lam,s). C_M={(p,a,lam,0,r),(p,a,lam,0,s)}.
```

Both have **two role labels** in their role carriers, **two candidate operational channels** in their U carrier and defined global zero assignment. Clause VI determines the admitted C exactly as displayed, so `|C_L|=1` and `|C_M|=2`. Hence the source's strict-isomorphism obstruction holds even though all base carrier **cardinalities are equal**, and role-map candidate bijections **do exist** (two permutations of {r,s}); this is not a vacuous no-candidate comparison.

Both models additionally supply `W=F2`, and `T(c)=0` for each admitted c. Clause VII produces `Dcomp=P_fin(C)` and all finite sums, including the empty-family sum zero. The full-family composite on L and M is **0 on both sides**; identical numerical aggregation does not repair the missing channel bijection. Every admitted channel has one actual restriction–realization trace `(h,h,p,a,lam,0,rho)`. The omitted channel in L is **absent**, not present with a component value 0.

There are precisely two role-label candidate maps (identity and swap), with all source E1–E7 clauses compatible in the selected pair; both fail E8 and hence do not induce a valid admitted-channel bijection for E9. The mathematical proof of C6.26 **does not need** this separate E8 diagnosis; it uses the cardinality inequality and C6.12 alone.

## 3. Additional adversarial limits and exact reproducibility

The local standard-library Python script constructs **five source-typed full models**, not simply stipulated channel sets:

| Tested model/pair | Observed boundary |
|---|---|
| L role=r vs M roles=r,s | C sizes **1 vs 2**, same ambient carrier sizes, all 2 role-map comparisons fail E8 |
| Z Role empty vs L Role=r | C sizes **0 vs 1**, empty-channel and empty composite are legal |
| L vs exact P copy | C sizes **1 vs 1**, 1 genuine strict-isomorphic comparison |
| L vs Q same Role, but supplied T(c)=1 | C sizes **1 vs 1**, but **no strict iso**: F2's one-dimensional unique linear isomorphism `J=id` cannot transport 0 to 1 |
| All five model channel candidate carriers | Each U has size 2; **10/10** Clause VI admitted-channel iff Formation trace nonempty comparisons pass |

All models contain defined assignment `q_lam(a)=0`; the presence of a zero assigned value is kept separate from the presence of a Role tuple and a T value. All primitive I/II/III/V and closure IV/VI/VII checks are executed from model declarations. The equal-channel-number Q control explicitly falsifies the **converse** `|C_L|=|C_M| ⇒ strict isomorphism`.

- [Source-locked prospective precommit](FAS-F2-C6.26-001_PRECOMMIT.md).
- [Executed exact portable Python script](../scripts/verify_c626_channel_cardinality.py).
- [Executed deterministic finite result JSON](../results/c626_channel_cardinality.json).

**Execution provenance unusually strong in this case:** The locally executed 7,716-byte Python script (also re-executed with warnings treated as errors) has SHA-256 `83aab72820a9961f4538fbd3b920c8f9494ae2d0275a3d633aaef40366fa130b` and Git blob SHA1 `5eee91f7f09a617906558467510e124dee2bd33f`. The code was uploaded into the existing GitHub script location, fetched back, and its remote blob SHA **matched the locally executed exact bytes**. The executed local JSON similarly matched the remote Git blob SHA `2b08002eeba3756d1d463f23561ff99ee06d6f7f`. This establishes reproducibility of the **exact committed code/results in this runtime**, though **no separate third-party fresh-checkout execution or external peer validation** has been established.

Windows 11 command from the cloned repository root:

```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c626_channel_cardinality.py
```

Default output: `DSD_Audit/audits/formal_proof/formation_axiom_system/results/c626_channel_cardinality.json`; optional first positional argument overrides the output location. Standard-library Python only.

## 4. FPA v0.1 gates and verdict

- G01 **PASS** source identity: supplied 33-page PDF checksum verified; precise original p.24 claim locked. Do not infer Zenodo byte identity.
- G02 **PASS** exact statement/scope: admitted-channel set cardinality inequality, no finite-only restriction.
- G03 **PASS** typed set/class validity: source strict E1–E9 and C6.12 induced channel bijection, same fixed (B,F).
- G04 **PASS** primitive/closure discipline: source I/II/III/V and IV/VI/VII with q value 0 defined and actual Role-dependent channel construction.
- G05 **PASS** general mathematical inference: existence of a strict map would give a bijection, contradicting unequal cardinalities.
- G06 **PASS_WITH_BOUNDARY** necessary vs sufficient: equal cardinality does **not** imply strict equivalence; no branch-index claim.
- G07 **PASS** adversarial: full legal models 1-vs-2 and 0-vs-1, same-U/same-role-cardinality nonvacuity, 1-vs-1 term mismatch and strict-positive control.
- G08 **PASS_WITH_BOUNDARY** finite/general separation: five finite toy models and ten trace assertions are not a universal enumeration; general proof is the separate bijection argument.
- G09 **PASS** finite composition: missing channel is not zero term; equal aggregate outputs insufficient.
- G10 **PASS** mathematical background: ordinary sets, cardinality preservation under bijections and F2 vector space.
- G11 **PASS_WITH_BOUNDARY** downstream: source Section7 Theorem7.1 and later construction/independence claims have NOT been audited and are NOT promoted.
- G12 **PASS** execution/status: exact committed Python and JSON Git blobs match locally run source; no external independent review.

**MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND.**
**DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY.**
**REVISION_NEED: NONE.**

The boundary is limited to source full Formation descriptors and precision of the necessary/not-sufficient assertion, with selected finite execution limits; it is **not a proof gap**. Historical nonurgent Theorem 4.7 wording-scope clarification stays independently open. Original PDF/Zenodo are not changed, and DSD Method Family internal method standardization **22/22** stays unchanged. **F2 whole-paper FPA remains OPEN.**

**Next scoped case (NOT_STARTED): `FAS-F2-T7.1-001`**, Theorem 7.1 *Existence of a full formation model*, source §7.1 printed pp.24–25. Begin with its own prospective precommit; do not use this single corollary to certify later Section 7.
