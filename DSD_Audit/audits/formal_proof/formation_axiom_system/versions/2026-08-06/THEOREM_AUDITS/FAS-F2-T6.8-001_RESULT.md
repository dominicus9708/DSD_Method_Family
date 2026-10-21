# FAS-F2-T6.8-001 — Embedding preservation and reflection / 형성 임베딩의 보존·반영

**2026-10-19 KST · Formal Proof Audit (FPA v0.1) · Author-project internal source-bound mathematical review, not independent external validation**

```text
AUDIT_ID: FAS-F2-T6.8-001
PARENT_METHOD: DSD Audit (one of the established 22)
FROZEN_SOURCE: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf (33 pages)
ATTACHED_PDF_SHA256: 8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a
SOURCE_LOCATION: Theorem 6.8, printed page 17
PRIMARY_DEPENDENCIES: Definition 6.2, Proposition 6.3, Definition 6.4, Closure Clauses IV and VI, Closure Clause VII
PRECOMMIT_COMMIT: d80b9306b0f780374262e2132160013d94d646f4
PYTHON_COMMIT: 9b2ddd734bef5e7319fd2b47906ad7218ace863a
FINITE_JSON_COMMIT: 28109d6d4f5154926de0cc1f7e06cf81581fadb1
MATHEMATICAL_VERDICT: PROVED_IN_DECLARED_BACKGROUND
DSD_AUDIT_VERDICT: PASS_WITH_BOUNDARY
REVISION_NEED: NONE
FOUND_MANDATORY_NEW_ASSUMPTION: no
FOUND_VALID_COUNTERMODEL_TO_EXACT_THEOREM: no
F2_FULL_PAPER: NOT_COMPLETE
INDEPENDENT_EXTERNAL_REPLICATION: not_established
ORIGINAL_PDF_ZENODO: unchanged
METHOD_FAMILY_INTERNAL_STANDARDIZATION: 22/22 unchanged
NEXT: FAS-F2-P6.11-001 / NOT_STARTED
```

## 1. Frozen original statement and proper scope

The source's exact statement: "A formation embedding preserves and reflects configuration describability and admitted-channel membership on its image. It also preserves every finite composite under the induced channel injection."

For a source model L, target M, formation embedding Phi:L→M, and source candidate configuration p or source candidate channel c, this is the following **on-image** statement:
- Psi_L(p) iff Psi_M(f_P(p)); equivalently Des_cfg,L(p) iff Des_cfg,M(f_P(p)), using Clause IV.
- c in C_L iff Phi-hat(c) in C_M for every well-typed c in U_L, not only previously admitted c.
- For every finite S subset C_L, J(Comp_L(S))=Comp_M(Phi-hat[S]).

It does *not* assert surjectivity onto all target channels, or reflect arbitrary target candidates not arising from U_L. It also does not assert that the assigned quantity value v equals the channel term T(c), or that source-admissible channels can be padded with zeros outside the declared domain.

## 2. Stepwise general mathematical derivation (not based on finite enumeration)

### 2.1 Configuration describability
Proposition 6.3 (forward preservation) gives Psi_L(p) => Psi_M(f_P(p)).
Definition 6.4 explicitly requires the additional witness-reflection implication Psi_M(f_P(p)) => Psi_L(p).
Consequently Psi_L(p) iff Psi_M(f_P(p)); Clause IV identifies this predicate with configuration describability in each model. No independent existence or uniqueness assumption on formation witnesses is introduced.

### 2.2 Admitted channel membership in both directions
Fix any c=(p,a,lambda,v,rho) in the source typed candidate-channel universe U_L. Its image is the typed candidate Phi-hat(c)=(f_P(p),f_M(a),tau_Lambda(lambda),I_lambda(v),tau_R(rho)) in U_M.

Clause VI defines source membership in C_L by the conjunction:
(1) Des_cfg,L(p);
(2) (a,v) in Gamma_L,lambda (the assignment graph at the relevant configuration/restriction, per the source notation);
(3) Role_L(p,a,lambda,rho).

Condition (1) is equivalent in both directions to its image under §2.1. Condition (2) is equivalent under reflection/preservation of assignment graphs (R4), with I_lambda typed and zero-preserving; the graph's relevant configuration restriction commutes by the declared map where applicable. Condition (3) is equivalent by (R5). Thus the conjunction is equivalent in both directions, i.e.
```text
forall c in U_L:
  c in C_L  <=>  Phi-hat(c) in C_M.
```
The forward direction already follows from Proposition 6.3. The reverse direction is genuinely dependent on R4, R5, and the separate witness-reflection clause. Source Theorem 6.8 does not infer it for a merely forward, nonembedding map.

### 2.3 Induced injection and finite composite
Suppose source channels c=(p,a,lambda,v,rho), c'=(p',a',lambda',v',rho') have the same image tuple. Because f_P, f_M, tau_Lambda, tau_R are injective, p=p', a=a', lambda=lambda', rho=rho'. Since I_lambda is injective on V_L,lambda for that now-fixed lambda, equality of the fourth image coordinate entails v=v'. Hence c=c' and Phi-hat restricted to C_L is injective.

For any finite S subset C_L, the image Phi-hat[S] is a finite subset C_M without duplicate-channel collisions. By linearity of J and (F6):
```text
J(Comp_L(S))
  = J(sum_{c in S} T_L(c))
  = sum_{c in S} J(T_L(c))
  = sum_{c in S} T_M(Phi-hat(c))
  = sum_{d in Phi-hat[S]} T_M(d)
  = Comp_M(Phi-hat[S]).
```
The empty-S case follows from J(0_WL)=0_WM; an admitted zero-assignment channel still has its ordinary T-term and is not discarded. This derivation is exactly the final conditional conclusion of Proposition 6.3 after the embedding premises supply channel injectivity.

## 3. Adversarial model boundaries and finite run

Two nondegenerate finite typed Formation models were constructed in an in-session local Python test. Source L has expression h, configurations pg/pb, one assigned material a with q(a)=0, two roles r1/r2 for pg, and no witness for pb. Target M contains correctly mapped H, GOOD/BAD, and additional disjoint expression/configuration X/EXTRA and material B with q(B)=1. Both models satisfy the instantiated expression admission, restriction identities, material/anchor inheritance, realization, configuration closure, active-assignment domain and channel admission conditions. Term map has T(pg,r1)=3, T(pg,r2)=-2, independent of q(a)=0; target terms on source images match under J=id, with an extra nonimage channel term 17.

Selection-dependent local results:
- 8/8 typed source candidate channel membership equivalences passed.
- 2/2 source admitted channels mapped injectively into target; 3 target admitted channels total, 1 target-only channel, with no requirement of surjectivity.
- All 4 finite subsets of the two admitted source channels satisfy the finite composition identity, including the empty family and the cancelling/partially cancelling possibilities.
- The defined zero q(a)=0 remains a legal admitted channel value while neither source term equals q(a) in general.

**Critical adversarial comparison:** add target-only expression SHADOW, a valid identity restriction and realization into BAD, without changing any source-indexed primitive relation. Both full models remain well-formed. The source pb is not describable, yet its image BAD becomes describable through the target-only witness, thereby generating a target channel not present in the source. All checked forward conditions and on-image primitive predicate/relation/assignment/role reflection continue to hold, but the *separate witness-reflection requirement of Definition 6.4 fails*. Thus this modified map is not a Formation embedding. It does NOT disprove the exact Theorem 6.8. It is a concrete demonstration why witness reflection cannot be silently deleted or subsumed by R1–R5.

[Finite verification script](../scripts/verify_t68_embedding_reflection.py) and [finite-test result JSON](../results/t68_embedding_reflection.json) are stored for rerun. From the DSD_Method_Family repository root on Windows:
```powershell
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t68_embedding_reflection.py
```
The source code is standard-library Python, output to sibling results/t68_embedding_reflection.json (or caller-supplied first CLI output path). The in-session local tests passed, but no separate external evaluator has rerun the committed GitHub version; the JSON is an internal recorded finite witness, not machine-certified general mathematics.

## 4. Source/audit decision gates

- G01 locked source/version: PASS, attached PDF SHA-256 computed in current runtime; any Zenodo byte identity remains unverified.
- G02 noncircularity: PASS, uses source definitions, Closure IV/VI/VII and previously independently scoped Proposition 6.3.
- G03 types/quantifiers: PASS_WITH_BOUNDARY, channel reflection is for candidates in U_L *on their induced image*; injection proof uses indexed I_lambda only after tau_Lambda equality.
- G04 primitive/closure status: PASS, no new primitive axiom added.
- G05 premise/inference: PASS, two implications for Psi and three reflected channel conjuncts; finite sums require injection.
- G06 uniqueness/existence: PASS_WITH_BOUNDARY; no trace uniqueness, no target-surjectivity, no inverse embedding asserted.
- G07 countermodels: PASS, target-only witness example violates *embedding premise* rather than theorem.
- G08 finite vs general: PASS_WITH_BOUNDARY; selected finite examples supplement, not establish, universal derivation.
- G09 transport/reflection: PASS, preserves Definition 6.4's independent witness-reflection obligation.
- G10 imported background: PASS, ordinary set/vector algebra and declared typed model conditions.
- G11 cross-paper: PASS_WITH_BOUNDARY, no unexamined strict-isomorphism or external bridge claim promoted.
- G12 integrity and external evaluator: PASS, internal and external validation kept separate.

## 5. Bounded result and continuation

**Scoped Theorem 6.8: MATHEMATICAL_VERDICT=PROVED_IN_DECLARED_BACKGROUND; DSD_AUDIT_VERDICT=PASS_WITH_BOUNDARY; REVISION_NEED=NONE.** The boundary indicates the original image-relative embedding hypotheses, source full models, separate witness reflection, and finite verification limits, NOT an identified unfinished step.

Nothing in this audit requires changing the original English PDF or Zenodo. The separately logged Theorem 4.7 clause-scope wording clarification remains live.

Stop here under the theorem-sized FPA timeout-prevention rule. Next dependency-oriented case: Definition 6.10 + Proposition 6.11 ("Strict formation isomorphism as bijective embedding"), **FAS-F2-P6.11-001 / NOT_STARTED**. The F2 whole-paper verdict remains OPEN and external independent verification is not established.

[Notion synchronized Theorem 6.8 audit](https://app.notion.com/p/3fe81f51e7fa812f83c3c7cc3bd5266d)
