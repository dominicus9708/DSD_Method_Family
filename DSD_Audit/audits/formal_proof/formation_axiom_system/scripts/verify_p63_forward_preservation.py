#!/usr/bin/env python3
"""Source-bound FAS-F2-P6.3-FORWARD-001 finite fixtures (not a universal proof).
Source: Kwon Dominicus, DSD_Formation_Axiom_System_EN(5).pdf, pp.15-16.
Windows repo-root command:
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_p63_forward_preservation.py
Optional first argument: alternate JSON output file.
"""
import itertools, json, sys
from pathlib import Path
from fractions import Fraction as Q

SOURCE_SHA="8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"
Z=Q(0)
LAMBDA="lambda"

def model(material, expressions=("h",), configurations=("p",), *, mat=None, act=None,
          descriptive=None, admitted=None, gates=None, res=None, real=None,
          q=None, roles=None, terms=None):
    M,E,P=set(material),set(expressions),set(configurations)
    mat={h:set((mat or {}).get(h,M)) for h in E}
    act={p:set((act or {}).get(p,M)) for p in P}
    desc=E if descriptive is None else set(descriptive)
    adm=E if admitted is None else set(admitted)
    gates={p:(True,True,True) for p in P} if gates is None else gates
    res={(h,h) for h in adm} if res is None else set(res)
    real={(h,p) for h in E for p in P} if real is None else set(real)
    q={a:Q(v) for a,v in (q or {}).items()}
    roles=set(roles or [])  # (configuration,material,role); one lambda
    assert desc<=adm<=E and set(q)<=M and set(gates)==P
    assert all(mat[h]<=M for h in E) and all(act[p]<=M for p in P)
    assert all((h,h) in res for h in adm)
    assert all(H in E and h in adm and mat[h]<=mat[H] for H,h in res)
    assert all(h in E and p in P and act[p]<=mat[h] for h,p in real)
    assert all(p in P and a in M for p,a,r in roles)
    # Anchors are the unique constant map to the fixed external support {s};
    # material internal relational signature is empty in all these fixtures.
    psi={p:all(gates[p]) and any(h in desc and (h,p) in real
            for H,h in res) for p in P}
    K={p for p in P if psi[p]}
    A=set().union(*(act[p] for p in K)) if K else set()
    assert set(q)<=A  # Primitive Axiom V
    graph={p:{(a,q[a]) for a in act[p]&set(q)} for p in P}
    C={(p,a,LAMBDA,v,r) for p in K for a,v in graph[p]
       for rp,ra,r in roles if rp==p and ra==a}
    terms=terms or {}
    T={c:Q(terms.get((c[0],c[1],c[4]),0)) for c in C}
    return dict(M=M,E=E,P=P,mat=mat,act=act,adm=adm,desc=desc,
                gates=gates,res=res,real=real,q=q,roles=roles,
                K=K,A=A,psi=psi,C=C,T=T)

def forward(L,M,fm,fe,fp,tr,*,I=1,J=1):
    assert set(fm)==L["M"] and set(fm.values())<=M["M"]
    assert set(fe)==L["E"] and set(fe.values())<=M["E"]
    assert set(fp)==L["P"] and set(fp.values())<=M["P"]
    assert {r for _,_,r in L["roles"]}<=set(tr)
    I,J=Q(I),Q(J)
    # F1 material/active inclusions and anchor preservation (constant 's').
    assert all({fm[a] for a in L["mat"][h]}<=M["mat"][fe[h]] for h in L["E"])
    assert all({fm[a] for a in L["act"][p]}<=M["act"][fp[p]] for p in L["P"])
    # F2; source true gates/predicates imply target true.
    assert all(h not in L["adm"] or fe[h] in M["adm"] for h in L["E"])
    assert all(h not in L["desc"] or fe[h] in M["desc"] for h in L["E"])
    assert all(all(not x or y for x,y in zip(L["gates"][p],
                         M["gates"][fp[p]])) for p in L["P"])
    # F3 relations preserved; F4 global graph; F5 roles.
    assert all((fe[H],fe[h]) in M["res"] for H,h in L["res"])
    assert all((fe[h],fp[p]) in M["real"] for h,p in L["real"])
    assert all(fm[a] in M["q"] and M["q"][fm[a]]==I*v for a,v in L["q"].items())
    assert all((fp[p],fm[a],tr[r]) in M["roles"] for p,a,r in L["roles"])
    # Independently derived source Proposition 6.3 clauses (i)-(iii).
    assert all(not L["psi"][p] or M["psi"][fp[p]] for p in L["P"])
    assert {fm[a] for a in L["A"]}<=M["A"]
    def phi(c):
        p,a,lam,v,r=c
        assert lam==LAMBDA
        return fp[p],fm[a],LAMBDA,I*v,tr[r]
    image={c:phi(c) for c in L["C"]}
    assert all(d in M["C"] for d in image.values())  # typed F6
    assert all(J*L["T"][c]==M["T"][d] for c,d in image.items())  # F6
    C=sorted(L["C"])
    rows=[]
    for mask in range(1<<len(C)):
        F={c for k,c in enumerate(C) if mask&(1<<k)}
        D={image[c] for c in F}
        x=J*sum((L["T"][c] for c in F),Z)
        y=sum((M["T"][d] for d in D),Z)
        if len(D)==len(F): assert x==y
        rows.append(dict(mask=mask,source_family=len(F),image_set=len(D),
                         source_mapped_sum=str(x),target_image_set_sum=str(y),
                         equality=x==y))
    return dict(source_channels=len(L["C"]),target_channels=len(M["C"]),
       globally_injective=len(set(image.values()))==len(image),families=rows,
       forward_Psi=True,forward_Astar=True,forward_channels=True,F6=True)

def test():
    L=model(("a","b"),q={"a":0,"b":0},roles={("p","a","r"),("p","b","r")},
            terms={("p","a","r"):1,("p","b","r"):1})
    collapse=forward(L,model(("x",),q={"x":0},roles={("p","x","r")},
                        terms={("p","x","r"):1}),
                     {"a":"x","b":"x"},{"h":"h"},{"p":"p"},{"r":"r"})
    assert not collapse["globally_injective"] and not collapse["families"][3]["equality"]
    assert collapse["families"][3]["source_mapped_sum"]=="2"
    assert collapse["families"][3]["target_image_set_sum"]=="1"
    good=forward(L,model(("u","v"),q={"u":0,"v":0},
                   roles={("p","u","r"),("p","v","r")},
                   terms={("p","u","r"):2,("p","v","r"):2}),
                 {"a":"u","b":"v"},{"h":"h"},{"p":"p"},{"r":"r"},J=2)
    assert good["globally_injective"] and all(x["equality"] for x in good["families"])
    # Injectivity globally sufficient, not necessary: zero-valued collapsed fiber.
    ZL=model(("a","b"),q={"a":0,"b":0},roles={("p","a","r"),("p","b","r")})
    zero=forward(ZL,model(("x",),q={"x":0},roles={("p","x","r")}),
                 {"a":"x","b":"x"},{"h":"h"},{"p":"p"},{"r":"r"})
    assert not zero["globally_injective"] and all(x["equality"] for x in zero["families"])
    # Target may have additional witnesses: no reflection follows from F1-F6.
    X=model(("a",),descriptive=set(),real=set())
    Y=model(("a","extra"),expressions=("h","k"),
            configurations=("p","p-extra"),mat={"h":{"a"},"k":{"extra"}},
            act={"p":{"a"},"p-extra":{"extra"}},
            real={("h","p"),("k","p-extra")})
    reverse=forward(X,Y,{"a":"a"},{"h":"h"},{"p":"p"},{})
    assert not X["psi"]["p"] and Y["psi"]["p"] and X["A"]==set() and Y["A"]=={"a","extra"}
    # Nonempty K_des but empty channel domain is consistent.
    empty=forward(model(("a",)),model(("x",)),
                  {"a":"x"},{"h":"h"},{"p":"p"},{})
    assert empty["source_channels"]==0 and len(empty["families"])==1
    # A target may have additional accepted channels beyond the source image.
    S=model(("a",),q={"a":0},roles={("p","a","r")},terms={("p","a","r"):1})
    T=model(("x","y"),q={"x":0,"y":0},
            roles={("p","x","r"),("p","y","s")},
            terms={("p","x","r"):1,("p","y","s"):3})
    extra=forward(S,T,{"a":"x"},{"h":"h"},{"p":"p"},{"r":"r"})
    assert extra["source_channels"]==1 and extra["target_channels"]==2
    assert all(x["equality"] for x in extra["families"])
    cases=dict(noninjective_nonzero_collapse=collapse,injective_J_twice=good,
               noninjective_zero_fiber=zero,target_only_witness=reverse,
               no_channels=empty,target_additional_channel=extra)
    counts={name:len(c["families"]) for name,c in cases.items()}
    assert sum(counts.values())==16 and len(cases)==6
    return dict(case="FAS-F2-P6.3-FORWARD-001",source_sha256=SOURCE_SHA,
       full_formation_F2="OPEN",independent_external_validation=False,
       source_pdf_zenodo_unchanged=True,typed_fixture_model_pairs=6,
       finite_families_checked=16,fixture_family_counts=counts,fixtures=cases,
       mathematical_proof_is_not_from_finite_tests=True)

def main():
    obj=test()
    out=(Path(sys.argv[1]) if len(sys.argv)>1 else
        Path(__file__).resolve().parents[1]/"results/p63_forward_preservation.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(obj,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps(dict(typed_model_pairs=6,finite_families_checked=16,
       countermodel=not obj["fixtures"]["noninjective_nonzero_collapse"]["families"][3]["equality"],
       injective_all_pass=all(x["equality"] for x in obj["fixtures"]["injective_J_twice"]["families"]),
       noninjective_zero_all_pass=all(x["equality"] for x in obj["fixtures"]["noninjective_zero_fiber"]["families"])),
       sort_keys=True))
if __name__=="__main__": main()
