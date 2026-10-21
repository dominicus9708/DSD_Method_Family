#!/usr/bin/env python3
r"""Finite source-typed test of F2 Corollary 6.24, not a universal proof.

Usage at DSD_Method_Family repo root on Windows:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c624_assignment_domain.py
Optional first argument: output JSON path. Standard library only.
"""
import sys, json
from pathlib import Path
from itertools import permutations, product, combinations

SHA="8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"

def form(name, material, Q):
    # Fixed B and F2. Values are pointed singleton {0}, with assigned 0 distinct
    # from no partial graph edge. All unmentioned primitive predicates are false.
    M=set(material); K={"lam","mu"}
    assert set(Q)==K and all(set(q)<=M for q in Q.values())
    d=dict(name=name,B={"s0"},field="F2",material=M,kind=K,expr={"h"},
      cfg={"p"},role={"r"},mat={"h":M},act={"p":M},
      ae={"h":{a:"s0" for a in M}},ap={"p":{a:"s0" for a in M}},
      Adm={"h"},Des={"h"},Res={("h","h")},Real={("h","p")},
      AC={"p"},LC={"p"},BC={"p"},V={k:{0} for k in K},
      zero={k:0 for k in K},Q={k:set(v) for k,v in Q.items()},
      negligible=set(),Role={("p",a,k,"r") for a in M for k in K})
    # Primitive I, II, III and the IV-defined witness/active material set.
    assert d["Des"]<=d["Adm"] and all((e,e) in d["Res"] for e in d["Adm"])
    assert all(h in d["Adm"] and d["mat"][h]<=d["mat"][H] and
      all(d["ae"][h][a]==d["ae"][H][a] for a in d["mat"][h])
      for H,h in d["Res"])
    assert all(d["act"][p]<=d["mat"][h] and all(
      d["ap"][p][a]==d["ae"][h][a] for a in d["act"][p])
      for h,p in d["Real"])
    d["Psi"]={p:p in d["AC"] and p in d["LC"] and p in d["BC"]
       and any((H,h) in d["Res"] and h in d["Des"] and (h,p) in d["Real"]
         for H,h in product(d["expr"],repeat=2)) for p in d["cfg"]}
    d["Kdes"]={p for p in d["cfg"] if d["Psi"][p]}
    d["Astar"]=set().union(*(d["act"][p] for p in d["Kdes"]))
    # Axiom V regime-global partial assignment.
    assert all(q<=d["Astar"] for q in d["Q"].values())
    d["q"]={(a,k):0 for k in K for a in d["Q"][k]}
    d["Gamma"]={k:{(a,0) for a in d["Q"][k]} for k in K}
    # Clause VI and VII; W=F2, terms freely supplied on admitted C.
    d["U"]={(p,a,k,0,"r") for p,a,k in product(d["cfg"],M,K)}
    d["C"]={c for c in d["U"] if d["Psi"][c[0]] and
       c[1] in d["act"][c[0]] and (c[1],0) in d["Gamma"][c[2]]
       and (c[0],c[1],c[2],c[4]) in d["Role"]}
    d["T"]={c:(0 if c[2]=="lam" else 1) for c in d["C"]}
    d["Dcomp"]={frozenset(s) for n in range(len(d["C"])+1)
        for s in combinations(sorted(d["C"]),n)}
    d["Comp"]={s:sum(d["T"][c] for c in s)%2 for s in d["Dcomp"]}
    assert len(d["C"])==sum(map(len,d["Q"].values()))
    assert set(d["T"])==d["C"] and d["Comp"][frozenset()]==0
    return d

def compare(L,M):
    if len(L["material"])!=len(M["material"]) or len(L["kind"])!=len(M["kind"]):
        return []
    out=[]
    for fm,tk in product(permutations(sorted(M["material"])),
                         permutations(sorted(M["kind"]))):
        f=dict(zip(sorted(L["material"]),fm))
        t=dict(zip(sorted(L["kind"]),tk))
        E5=all((a in L["Q"][k])==(f[a] in M["Q"][t[k]])
          for a,k in product(L["material"],L["kind"]))
        E6=all(((a,0) in L["Gamma"][k])==((f[a],0) in M["Gamma"][t[k]])
          for a,k in product(L["material"],L["kind"]))
        assert E5==E6  # Graph projections and singleton pointed bijections.
        # E1, E2-E4, E7 and E8 match for any f,t in this chosen fixture.
        assert all(L["ae"]["h"][a]==M["ae"]["h"][f[a]] for a in L["material"])
        assert all((("p",a,k,"r") in L["Role"])==
          (("p",f[a],t[k],"r") in M["Role"])
          for a,k in product(L["material"],L["kind"]))
        if E5:
            mapped={(p,f[a],t[k],v,r):L["T"][(p,a,k,v,r)]
                     for p,a,k,v,r in L["C"]}
            assert set(mapped)==M["C"]
            E9=all(value==M["T"][c] for c,value in mapped.items()) # J=id_F2.
        else:E9=None # No E1-E8-induced channel bijection.
        out.append(dict(material_map=f,kind_map=t,E5=E5,E6=E6,E9=E9,
                        strict=(E5 and E6 and E9 is True)))
    return out

def run():
    L=form("L",["a","b"],{"lam":{"a"},"mu":{"a"}})
    M=form("M",["a","b"],{"lam":{"a"},"mu":{"b"}})
    P=form("P",["a","b"],{"lam":{"a"},"mu":{"a"}})
    X=form("X",["a","b","c"],{"lam":{"a"},"mu":{"b"}})
    bad,positive,empty=compare(L,M),compare(L,P),compare(L,X)
    deg=lambda d:sorted(sum(a in d["Q"][k] for k in d["kind"])
                         for a in d["material"])
    assert len(bad)==len(positive)==4 and len(empty)==0
    assert all(not r["E5"] and not r["E6"] for r in bad)
    assert sum(r["E5"] for r in positive)==2
    assert sum(r["strict"] for r in positive)==1
    assert deg(L)==[0,2] and deg(M)==[1,1]
    assert len(L["q"])==len(M["q"])==2 and len(L["C"])==len(M["C"])==2
    assert sorted(map(len,L["Q"].values()))==sorted(map(len,M["Q"].values()))==[1,1]
    assert ("b","mu") not in L["q"] and M["q"][("b","mu")]==0
    assert L["Comp"][frozenset(L["C"])]==M["Comp"][frozenset(M["C"])]==1
    return dict(audit_id="FAS-F2-C6.24-001",source_sha256=SHA,
       all_checks_passed=True,primitive_axioms=["I","II","III","V"],
       closure_clauses=["IV","VI","VII"],nonvacuous_candidates=4,
       nonvacuous_all_E5_fail=True,nonvacuous_all_E6_fail=True,
       same_kind_domain_sizes=[1,1],same_total_assignment_edges=2,
       material_incidence_degrees_L=deg(L),material_incidence_degrees_M=deg(M),
       admitted_channels_each=2,equal_composites_without_domain_isomorphism=True,
       positive_candidates=4,positive_E5_passes=2,positive_strict_isomorphisms=1,
       empty_candidate_case=0,defined_zero_not_undefined=True,
       negative_comparison_rows=bad,positive_comparison_rows=positive,
       finite_not_general_proof=True,external_validation=False)

def main():
    result=run()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (
      Path(__file__).resolve().parent.parent/"results"/"c624_assignment_domain.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print("C6.24 PASS: 4 domain-bijection pairs all fail; 2/4 positive E5 maps")
    print("OUTPUT:",out)

if __name__=="__main__":main()
