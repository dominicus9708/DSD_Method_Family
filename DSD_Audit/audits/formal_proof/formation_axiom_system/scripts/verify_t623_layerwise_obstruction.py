#!/usr/bin/env python3
r"""Reproducible selected finite models for F2 Theorem 6.23. Standard library only.

Source version: DSD_Formation_Axiom_System_EN(5).pdf, SHA-256 frozen in PDF_SHA.
These selected examples DO NOT prove the universal first-order logical theorem.
Cand already requires bijective components and an F2-linear term isomorphism.
From a cloned DSD_Method_Family root on Windows:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t623_layerwise_obstruction.py
Optional first CLI argument changes the JSON output path.
"""
from itertools import permutations, product
from pathlib import Path
import json, sys

PDF_SHA = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"

def model(tag, role_labels=("r0","r1"), active=("r0",), value=None,
          has_q=True, anchor="s0", negligible=False):
    if value is None:
        value={r:0 for r in active if has_q}
    d=dict(tag=tag, field="F2", base={"s0","s1"},
       material={"a"}, expr={"h"}, cfg={"p"}, kind={"k"}, role=set(role_labels),
       mat={"h":{"a"}},act={"p":{"a"}},anch_e={"h":{"a":anchor}},
       anch_p={"p":{"a":anchor}},adm_e={"h"},des_e={"h"},
       res={("h","h")},real={("h","p")},adm_p={"p"},lc={"p"},bc={"p"},
       V={"k":{0}},zero={"k":0},q={("a","k"):0} if has_q else {},
       negligible={"k"} if negligible else set(),
       size={("k",0):0} if negligible else {}, delta={"k":1} if negligible else {},
       roles={("p","a","k",r) for r in active},W={0,1})
    d["psi"]={p:p in d["adm_p"] and p in d["lc"] and p in d["bc"]
         and any((H,h) in d["res"] and h in d["des_e"] and (h,p) in d["real"]
            for H,h in product(d["expr"],repeat=2)) for p in d["cfg"]}
    d["Kdes"]={p for p,yes in d["psi"].items() if yes}
    d["Astar"]=set().union(*(d["act"][p] for p in d["Kdes"]))
    d["gamma"]={(a,k,v) for (a,k),v in d["q"].items()}
    d["U"]={(p,a,k,v,r) for p in d["cfg"] for a in d["material"]
       for k in d["kind"] for v in d["V"][k] for r in d["role"]}
    d["C"]={c for c in d["U"] if d["psi"][c[0]] and c[1] in d["act"][c[0]]
       and (c[1],c[2],c[3]) in d["gamma"] and (c[0],c[1],c[2],c[4]) in d["roles"]}
    d["T"]={c:value[c[4]] for c in d["C"]}
    # Primitive Axioms I, II, III, V and definitionally produced IV,VI,VII.
    assert d["des_e"]<=d["adm_e"]
    assert all((h,h) in d["res"] for h in d["adm_e"])
    assert all(h in d["adm_e"] and d["mat"][h]<=d["mat"][H]
       and all(d["anch_e"][h][a]==d["anch_e"][H][a] for a in d["mat"][h])
       for H,h in d["res"])
    assert all(d["act"][p]<=d["mat"][h] and all(
       d["anch_p"][p][a]==d["anch_e"][h][a] for a in d["act"][p])
       for h,p in d["real"])
    assert all(a in d["Astar"] and v in d["V"][k] for (a,k),v in d["q"].items())
    assert all(p in d["cfg"] and a in d["material"] and k in d["kind"]
       and r in d["role"] for p,a,k,r in d["roles"])
    assert all(d["zero"][k] in d["V"][k] for k in d["kind"])
    assert set(d["T"])==d["C"] and all(x in d["W"] for x in d["T"].values())
    if negligible:
       assert d["size"][("k",0)]==0 and d["delta"]["k"]>0
    return d

def candidates(L,M):
    sorts=("material","expr","cfg","kind","role")
    if any(len(L[s])!=len(M[s]) for s in sorts):
        return []
    maps=[[dict(zip(sorted(L[s]),q)) for q in permutations(sorted(M[s]))]
       for s in sorts]
    # All other maps are uniquely typed: singleton pointed value 0 -> 0;
    # one-dimensional F2-linear isomorphism J(0)=0,J(1)=1.
    return [dict(zip(sorts,group)) for group in product(*maps)]

def status(L,M,p):
    a,e,c,k,r=(p[x] for x in ("material","expr","cfg","kind","role"))
    E1=all({a[x] for x in L["mat"][h]}==M["mat"][e[h]] and
       all(L["anch_e"][h][x]==M["anch_e"][e[h]][a[x]] for x in L["mat"][h])
       for h in L["expr"]) and all(
       {a[x] for x in L["act"][q]}==M["act"][c[q]] and
       all(L["anch_p"][q][x]==M["anch_p"][c[q]][a[x]] for x in L["act"][q])
       for q in L["cfg"])
    E2=all((h in L[t])==(e[h] in M[t]) for t in ("adm_e","des_e") for h in L["expr"])
    E3=all(((h,g) in L["res"])==((e[h],e[g]) in M["res"])
       for h,g in product(L["expr"],repeat=2)) and all(
       ((h,q) in L["real"])==((e[h],c[q]) in M["real"])
       for h,q in product(L["expr"],L["cfg"]))
    E4=all((q in L[t])==(c[q] in M[t]) for t in ("adm_p","lc","bc")
       for q in L["cfg"]) and all(L["psi"][q]==M["psi"][c[q]] for q in L["cfg"])
    E5=all(((x,lam) in L["q"])==((a[x],k[lam]) in M["q"])
       for x,lam in product(L["material"],L["kind"]))
    E6=all(((x,lam,0) in L["gamma"])==((a[x],k[lam],0) in M["gamma"])
       for x,lam in product(L["material"],L["kind"]))
    E7=all((lam in L["negligible"])==(k[lam] in M["negligible"]) and (
       lam not in L["negligible"] or (
       L["delta"][lam]==M["delta"][k[lam]] and
       L["size"][(lam,0)]==M["size"][(k[lam],0)])) for lam in L["kind"])
    E8=all(((q,x,lam,role) in L["roles"])==
       ((c[q],a[x],k[lam],r[role]) in M["roles"])
       for q,x,lam,role in product(L["cfg"],L["material"],L["kind"],L["role"]))
    first=(E1,E2,E3,E4,E5,E6,E7,E8)
    if all(first):
        mapped={(c[q],a[x],k[lam],0,r[role]):L["T"][(q,x,lam,v,role)]
                for q,x,lam,v,role in L["C"]}
        E9=set(mapped)==M["C"] and all(mapped[z]==M["T"][z] for z in mapped)
    else:
        E9=None  # E9 presupposes a channel bijection induced by E1–E8.
    return list(first)+(E9,)

def evaluate(L,M):
    rows=[status(L,M,p) for p in candidates(L,M)]
    strict=any(all(row) for row in rows)
    fail=all(any(v is False for v in row) for row in rows)
    assert strict== (not fail)
    return dict(candidates=len(rows),strict=strict,universal_failure=fail,
       failed_indices=[[i+1 for i,v in enumerate(row) if v is False] for row in rows],
       condition_rows=rows,fully_strict_candidates=sum(all(row) for row in rows))

def main():
    L=model("L")
    models={
      "strict_positive":model("same"),
      "anchor_E1":model("anchor",anchor="s1"),
      "assignment_E5_E6":model("unassigned",has_q=False),
      "negligible_E7":model("metric",negligible=True),
      "role_E8":model("role2",active=("r0","r1"),value={"r0":0,"r1":1}),
      "terms_E8_or_E9":model("terms",value={"r0":1}),
      "no_candidates_role_size":model("noCand",role_labels=("r0",))}
    records={k:evaluate(L,v) for k,v in models.items()}
    assert len(records)==7 and sum(v["candidates"] for v in records.values())==12
    assert records["strict_positive"]["fully_strict_candidates"]==1
    assert records["strict_positive"]["failed_indices"]==[[],[8]]
    assert all(x==[8] for x in records["role_E8"]["failed_indices"])
    assert records["terms_E8_or_E9"]["failed_indices"]==[[9],[8]]
    assert records["no_candidates_role_size"]["universal_failure"]
    assert records["no_candidates_role_size"]["candidates"]==0
    # Abstract truth vectors: ∀Phi ∃i not E_i, but NOT ∃i ∀Phi not E_i.
    vectors=[[False]+[True]*8,[True,False]+[True]*7]
    assert all(not all(row) for row in vectors)
    assert not any(all(not row[i] for row in vectors) for i in range(9))
    result=dict(audit_id="FAS-F2-T6.23-001",source_pdf_sha256=PDF_SHA,
      all_checks_passed=True,case_count=7,candidate_comparisons=12,
      nonvacuous_failed_model_pairs=5,empty_candidate_pairs=1,
      strict_positive_pairs=1,case_details=records,
      abstract_quantifier_swap_truth_vectors=vectors,
      abstract_truth_vectors_not_full_formation_models=True,
      Cand_requires_linear_isomorphism_J_at_entry=True,
      primitive_axioms_checked=["I","II","III","V"],
      closure_clauses_checked=["IV","VI","VII"],
      finite_tests_are_not_general_proof=True,external_independent_validation=False)
    out=(Path(sys.argv[1]) if len(sys.argv)>1 else
      Path(__file__).resolve().parent.parent/"results"/"t623_layerwise_obstruction.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("T6.23 finite checks PASS: 7 pairs, 12 typed candidates")
    print("OUTPUT",out)
if __name__=="__main__":
    main()
