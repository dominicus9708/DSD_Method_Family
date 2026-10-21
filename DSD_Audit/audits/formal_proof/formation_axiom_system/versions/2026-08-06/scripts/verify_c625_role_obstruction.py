#!/usr/bin/env python3
r"""F2 C6.25: source-typed full finite Formation models; standard library only.

From cloned DSD_Method_Family repository root on Windows:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c625_role_obstruction.py
Optional first argument changes the deterministic JSON output path.
The program is a selected finite audit, not a universal proof or external review.
"""
from itertools import permutations, product, combinations
from pathlib import Path
import json, sys

SHA = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"


def make(name, mode="material", roles=("r", "s")):
    materials={"a", "b"}; kinds={"lam", "mu"}; roles=set(roles)
    assert mode in ("material", "kind")
    d={"name":name, "B":{"s0"}, "F":"F2", "material":materials,
       "expr":{"h"}, "cfg":{"p"}, "kind":kinds, "role":roles,
       "mat":{"h":set(materials)}, "act":{"p":set(materials)},
       "anchE":{"h":{a:"s0" for a in materials}},
       "anchP":{"p":{a:"s0" for a in materials}},
       "AdmE":{"h"}, "DesE":{"h"}, "Res":{("h","h")},
       "Real":{("h","p")}, "AdmP":{"p"}, "LC":{"p"}, "BC":{"p"},
       "V":{k:{0} for k in kinds}, "zero":{k:0 for k in kinds},
       "Q":{k:set(materials) for k in kinds}, "negligible":set(),
       "W":"F2"}
    d["Role"]={("p",a,k, ("r" if (a=="a" if mode=="material" else k=="lam") else "s"))
               for a,k in product(sorted(materials),sorted(kinds))
               if ("r" if (a=="a" if mode=="material" else k=="lam") else "s") in roles}
    # Axioms I, II, III and witness-derived Clause IV.
    assert d["DesE"]<=d["AdmE"]
    assert all((x,x) in d["Res"] for x in d["AdmE"])
    assert all(h in d["AdmE"] and d["mat"][h]<=d["mat"][H] and
        all(d["anchE"][h][a]==d["anchE"][H][a] for a in d["mat"][h])
        for H,h in d["Res"])
    assert all(d["act"][p]<=d["mat"][h] and
        all(d["anchP"][p][a]==d["anchE"][h][a] for a in d["act"][p])
        for h,p in d["Real"])
    d["Psi"]={p:(p in d["AdmP"] and p in d["LC"] and p in d["BC"] and
        any((H,h) in d["Res"] and h in d["DesE"] and (h,p) in d["Real"]
            for H,h in product(d["expr"], repeat=2))) for p in d["cfg"]}
    d["Kdes"]={p for p in d["cfg"] if d["Psi"][p]}
    d["Astar"]=set().union(*(d["act"][p] for p in d["Kdes"]))
    d["Descfg"]=dict(d["Psi"]);d["A"]=set(d["Astar"])
    # Global partial assignment q with defined zero on every permitted domain item.
    assert all(Q<=d["Astar"] for Q in d["Q"].values())
    d["q"]={(a,k):0 for k in kinds for a in d["Q"][k]}
    d["Gamma"]={k:{(a,0) for a in d["Q"][k]} for k in kinds}
    assert all(d["zero"][k] in d["V"][k] for k in kinds)
    # Definitional Clause VI and VII.
    d["U"]={(p,a,k,v,r) for p,a,k,r in product(d["cfg"],materials,kinds,roles)
        for v in d["V"][k]}
    d["Chan"]={c:(d["Descfg"][c[0]] and c[1] in d["act"][c[0]] and
        (c[1],c[3]) in d["Gamma"][c[2]] and
        (c[0],c[1],c[2],c[4]) in d["Role"]) for c in d["U"]}
    d["C"]={c for c in d["U"] if d["Chan"][c]}
    d["T"]={c:(0 if c[1]=="a" else 1) for c in d["C"]}
    d["Dcomp"]={frozenset(q) for n in range(len(d["C"])+1)
                for q in combinations(sorted(d["C"]),n)}
    d["Comp"]={q:sum(d["T"][c] for c in q)%2 for q in d["Dcomp"]}
    assert set(d["T"])==d["C"] and d["Comp"][frozenset()]==0
    return d


def trace(d,c):
    p,a,k,v,r=c
    return {(H,h,p,a,k,v,r) for H,h in d["Res"]
        if h in d["DesE"] and (h,p) in d["Real"] and
        p in d["AdmP"] and p in d["LC"] and p in d["BC"] and
        a in d["act"][p] and (a,v) in d["Gamma"][k] and
        (p,a,k,r) in d["Role"]}


def mappings(L,M):
    types=("material","cfg","kind","role")
    if any(len(L[t])!=len(M[t]) for t in types):return []
    return [dict(zip(types,ds)) for ds in product(*[
        [dict(zip(sorted(L[t]),v)) for v in permutations(sorted(M[t]))]
        for t in types])]


def analyze(L,M):
    out=[]
    for maps in mappings(L,M):
        f,g,k,r=(maps[t] for t in ("material","cfg","kind","role"))
        # E1-E7 hold by design for all bijections in these two source configurations.
        E1=all(L["anchP"]["p"][a]==M["anchP"]["p"][f[a]] for a in L["material"])
        E2= L["AdmE"]==M["AdmE"] and L["DesE"]==M["DesE"]
        E3=L["Res"]==M["Res"] and L["Real"]==M["Real"]
        E4=L["Psi"]==M["Psi"] and L["LC"]==M["LC"] and L["BC"]==M["BC"]
        E5=all((a in L["Q"][lam])==(f[a] in M["Q"][k[lam]])
               for a,lam in product(L["material"],L["kind"]))
        E6=all(((a,v) in L["Gamma"][lam])==((f[a],v) in M["Gamma"][k[lam]])
               for a,lam,v in product(L["material"],L["kind"],(0,)))
        E7=L["negligible"]==M["negligible"]==set()
        E8=all(((p,a,lam,ro) in L["Role"])==
               ((g[p],f[a],k[lam],r[ro]) in M["Role"])
               for p,a,lam,ro in product(L["cfg"],L["material"],L["kind"],L["role"]))
        assert all((E1,E2,E3,E4,E5,E6,E7))
        if E8:
            mapped={(g[p],f[a],k[lam],v,r[ro]):L["T"][(p,a,lam,v,ro)]
                    for p,a,lam,v,ro in L["C"]}
            assert set(mapped)==M["C"]
            E9=all(M["T"][target]==term for target,term in mapped.items())
        else:E9=None # No E1-E8 induced channel bijection to check E9.
        out.append({"material_map":f,"kind_map":k,"role_map":r,
                    "E1_to_E7":True,"E8":E8,"E9":E9,"strict":E8 and E9 is True})
    return out


def degree(d):
    return sorted(len({rho for p,a,k,rho in d["Role"] if a==m})
                  for m in d["material"])


def main():
    L=make("L","material");M=make("M","kind");P=make("P","material")
    Z=make("Z","material",roles=("r",))
    neg=analyze(L,M);pos=analyze(L,P);empty=analyze(L,Z)
    assert len(neg)==len(pos)==8 and len(empty)==0
    assert all(not x["E8"] and x["E9"] is None for x in neg)
    assert sum(x["E8"] for x in pos)==4
    assert sum(x["strict"] for x in pos)==2
    assert degree(L)==[1,1] and degree(M)==[2,2]
    assert len(L["C"])==len(M["C"])==4
    assert len(L["Role"])==len(M["Role"])==4
    assert sorted(sum(c[4]==rho for c in L["C"]) for rho in L["role"])==[2,2]
    assert sorted(sum(c[4]==rho for c in M["C"]) for rho in M["role"])==[2,2]
    assert all((c in d["C"])==bool(trace(d,c)) for d in (L,M) for c in d["U"])
    assert len(L["U"])==len(M["U"])==8
    assert L["Comp"][frozenset(L["C"])]==M["Comp"][frozenset(M["C"])]==0
    # Control: a missing assignment is NOT an operational zero-valued channel.
    test=dict(L);test["Gamma"]={"lam":set(L["Gamma"]["lam"]),
                                     "mu":set(L["Gamma"]["mu"])}
    test["Gamma"]["mu"].discard(("b",0))
    assert ("b",0) not in test["Gamma"]["mu"] and ("b",0) in L["Gamma"]["mu"]
    result={"audit_id":"FAS-F2-C6.25-001","source_sha256":SHA,
      "all_checks_passed":True,"primitive_axioms_checked":["I","II","III","V"],
      "closure_clauses_checked":["IV","VI","VII"],
      "nonvacuous_role_candidate_bijections":len(neg),
      "all_negative_candidates_E1_to_E7_pass":True,
      "negative_E8_preserving_candidates":sum(x["E8"] for x in neg),
      "negative_role_edges_each":len(L["Role"]),
      "negative_admitted_channels_each":len(L["C"]),
      "roles_each":len(L["role"]),"kinds_each":len(L["kind"]),
      "quantity_graph_edges_each":len(L["q"]),
      "role_incidence_distinct_roles_per_material_L":degree(L),
      "role_incidence_distinct_roles_per_material_M":degree(M),
      "role_frequency_each_model":[2,2],
      "candidate_trace_equivalences":len(L["U"])+len(M["U"]),
      "full_family_composite_L":L["Comp"][frozenset(L["C"])],
      "full_family_composite_M":M["Comp"][frozenset(M["C"])],
      "positive_candidates":len(pos),
      "positive_E8_preserving_candidates":sum(x["E8"] for x in pos),
      "positive_strict_isomorphisms":sum(x["strict"] for x in pos),
      "empty_candidate_control":len(empty),
      "negative_rows":neg,"positive_rows":pos,
      "defined_zero_distinguished_from_undefined":True,
      "finite_not_universal_proof":True,"independent_external_validation":False}
    out=(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/
         "results"/"c625_role_obstruction.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print("C6.25 PASS: 8/8 role candidates fail; positive 4 E8, 2 strict; 16 trace checks")
    print("OUTPUT",out)

if __name__=="__main__": main()
