#!/usr/bin/env python3
r"""FAS-F2-T6.14-001: finite E1-E9 strict-equivalence verifier.

Finite selected source-typed models only; NOT a universal mathematical proof.
From cloned DSD_Method_Family root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t614_strict_equivalence.py
An optional first argument selects output JSON. Standard library only.
"""
import json
import sys
from itertools import product, combinations
from pathlib import Path

SOURCE_SHA="8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"
TYPES=("material","expr","cfg","kinds","roles")
ORIG={"material":("a","b","u"),"expr":("e0","e1","e2"),
      "cfg":("p0","p1","p2"),"kinds":("metric","other"),"roles":("r0","r1")}
VAL={"metric":(-1,0,1),"other":(0,2,3)}
SUP={"e0":("a","b"),"e1":("a",),"e2":("b",)}
ACT={"p0":("a",),"p1":("b",),"p2":("a",)}
RES={("e0","e0"),("e1","e1"),("e2","e2"),("e0","e1"),("e0","e2")}
REAL={("e1","p0"),("e2","p1")}
Q={("a","metric"):1,("b","metric"):0,("a","other"):2}
ROLES={("p0","a","metric","r0"),("p0","a","metric","r1"),
       ("p1","b","metric","r0"),("p0","a","other","r1")}
TERM={("p0","a","metric",1,"r0"):3,("p0","a","metric",1,"r1"):-3,
      ("p1","b","metric",0,"r0"):0,("p0","a","other",2,"r1"):4}

def model(name, labels, labels_v, factor):
    ix={k:dict(zip(ORIG[k],labels[k])) for k in TYPES}
    iv={k:dict(zip(VAL[k],labels_v[k])) for k in VAL}
    m=lambda a: ix["material"][a]
    e=lambda a: ix["expr"][a]
    p=lambda a: ix["cfg"][a]
    k=lambda a: ix["kinds"][a]
    r=lambda a: ix["roles"][a]
    z={"name":name,"ix":ix,"iv":iv,"factor":factor,
       "B":"B_s0_s1","F":"R","material_signature":(),
       "carrier":{t:set(ix[t].values()) for t in TYPES},
       "V":{k(a):set(iv[a].values()) for a in VAL},
       "zero":{k(a):iv[a][0] for a in VAL},
       "mat":{e(x):{m(a) for a in aset} for x,aset in SUP.items()},
       "act":{p(x):{m(a) for a in aset} for x,aset in ACT.items()},
       "res":{(e(x),e(y)) for x,y in RES},
       "real":{(e(x),p(y)) for x,y in REAL},
       "admexpr":set(ix["expr"].values()),"desexpr":set(ix["expr"].values()),
       "admcfg":{p("p0"),p("p1")},
       "lc":set(ix["cfg"].values()),"bc":set(ix["cfg"].values()),
       "q":{(m(a),k(kind)):iv[kind][v] for (a,kind),v in Q.items()},
       "role":{(p(a),m(b),k(c),r(d)) for a,b,c,d in ROLES},
       "negligible":{k("metric")},
       "size":{(k("metric"),iv["metric"][v]):abs(v) for v in VAL["metric"]},
       "delta":{k("metric"):2},
       "term":{(p(a),m(b),k(c),iv[c][v],r(d)):factor*t
               for (a,b,c,v,d),t in TERM.items()}}
    z["anchor_mat"]={x:{a:"s0" for a in A} for x,A in z["mat"].items()}
    z["anchor_act"]={x:{a:"s0" for a in A} for x,A in z["act"].items()}
    return z

def psi(z,p):
    return p in z["admcfg"] and p in z["lc"] and p in z["bc"] and any(
        h in z["desexpr"] and (h,p) in z["real"] for H,h in z["res"])

def C(z):
    return {(p,a,k,z["q"][(a,k)],r) for p,a,k,r in z["role"]
            if psi(z,p) and (a,k) in z["q"]}

def valid_core(z):
    e=z["carrier"]["expr"];p=z["carrier"]["cfg"]
    assert z["desexpr"]<=z["admexpr"]<=e
    assert all((a,a) in z["res"] for a in z["admexpr"])
    assert all(H in e and h in e and z["mat"][h]<=z["mat"][H] and all(
        z["anchor_mat"][h][a]==z["anchor_mat"][H][a] for a in z["mat"][h])
        for H,h in z["res"])
    assert all(x in e and y in p and z["act"][y]<=z["mat"][x] and all(
        z["anchor_mat"][x][a]==z["anchor_act"][y][a] for a in z["act"][y])
        for x,y in z["real"])
    active=set().union(*(z["act"][a] for a in p if psi(z,a)))
    assert all(a in active and v in z["V"][k] for (a,k),v in z["q"].items())
    assert all(z["zero"][k] in z["V"][k] for k in z["V"])
    assert set(z["term"])==C(z)
    assert len(C(z))==4
    return True

def arrow(A,B):
    f={t:{A["ix"][t][x]:B["ix"][t][x] for x in ORIG[t]} for t in TYPES}
    I={A["ix"]["kinds"][k]:{
        A["iv"][k][v]:B["iv"][k][v] for v in VAL[k]} for k in VAL}
    return {"A":A,"B":B,"f":f,"I":I,"J":B["factor"]/A["factor"]}

def ident(A):
    return {"A":A,"B":A,
            "f":{t:{x:x for x in A["carrier"][t]} for t in TYPES},
            "I":{k:{x:x for x in A["V"][k]} for k in A["V"]},"J":1}

def inverse(x):
    return {"A":x["B"],"B":x["A"],
            "f":{t:{v:k for k,v in a.items()} for t,a in x["f"].items()},
            "I":{x["f"]["kinds"][k]:{v:u for u,v in a.items()}
                 for k,a in x["I"].items()},"J":1/x["J"]}

def compose(g,f):
    assert f["B"] is g["A"]
    return {"A":f["A"],"B":g["B"],"J":g["J"]*f["J"],
            "f":{t:{k:g["f"][t][v] for k,v in a.items()}
                 for t,a in f["f"].items()},
            "I":{k:{v:g["I"][f["f"]["kinds"][k]][w] for v,w in a.items()}
                 for k,a in f["I"].items()}}

def image(c,x):
    p,a,k,v,r=c;f=x["f"]
    return (f["cfg"][p],f["material"][a],f["kinds"][k],x["I"][k][v],f["roles"][r])

def check(x):
    A,B=x["A"],x["B"];f=x["f"];I=x["I"];J=x["J"]
    assert A["B"]==B["B"] and A["F"]==B["F"] and J!=0
    for t in TYPES:
        assert set(f[t])==A["carrier"][t] and set(f[t].values())==B["carrier"][t]
        assert len(set(f[t].values()))==len(f[t])
    for k in A["V"]:
        assert set(I[k])==A["V"][k] and set(I[k].values())==B["V"][f["kinds"][k]]
        assert len(set(I[k].values()))==len(I[k])
        assert I[k][A["zero"][k]]==B["zero"][f["kinds"][k]]
    E1=all({f["material"][a] for a in A["mat"][e]}==B["mat"][f["expr"][e]] and
           all(A["anchor_mat"][e][a]==B["anchor_mat"][f["expr"][e]][f["material"][a]]
               for a in A["mat"][e]) for e in A["carrier"]["expr"]) and all(
           {f["material"][a] for a in A["act"][p]}==B["act"][f["cfg"][p]] and
           all(A["anchor_act"][p][a]==B["anchor_act"][f["cfg"][p]][f["material"][a]]
               for a in A["act"][p]) for p in A["carrier"]["cfg"])
    E2=all((e in A[t])==(f["expr"][e] in B[t])
           for t in ("admexpr","desexpr") for e in A["carrier"]["expr"])
    E3=all(((u,v) in A["res"])==((f["expr"][u],f["expr"][v]) in B["res"])
           for u,v in product(A["carrier"]["expr"],repeat=2)) and all(
           ((e,p) in A["real"])==((f["expr"][e],f["cfg"][p]) in B["real"])
           for e,p in product(A["carrier"]["expr"],A["carrier"]["cfg"]))
    E4=all((p in A[t])==(f["cfg"][p] in B[t])
           for t in ("admcfg","lc","bc") for p in A["carrier"]["cfg"]) and all(
           psi(A,p)==psi(B,f["cfg"][p]) for p in A["carrier"]["cfg"])
    E5=all(((a,k) in A["q"])==((f["material"][a],f["kinds"][k]) in B["q"])
           for a,k in product(A["carrier"]["material"],A["carrier"]["kinds"]))
    E6=all(((a,k) in A["q"] and A["q"][(a,k)]==v)==
           ((f["material"][a],f["kinds"][k]) in B["q"] and
            B["q"][(f["material"][a],f["kinds"][k])]==I[k][v])
           for k in A["V"] for a in A["carrier"]["material"] for v in A["V"][k])
    E7=all((k in A["negligible"])==(f["kinds"][k] in B["negligible"]) and
           (k not in A["negligible"] or
            (A["delta"][k]==B["delta"][f["kinds"][k]] and all(
             A["size"][(k,v)]==B["size"][(f["kinds"][k],I[k][v])]
             for v in A["V"][k]))) for k in A["V"])
    E8=all(((p,a,k,r) in A["role"])==
           ((f["cfg"][p],f["material"][a],f["kinds"][k],f["roles"][r]) in B["role"])
           for p,a,k,r in product(A["carrier"]["cfg"],A["carrier"]["material"],
                                  A["carrier"]["kinds"],A["carrier"]["roles"]))
    E9={image(c,x) for c in C(A)}==C(B) and all(
        J*A["term"][c]==B["term"][image(c,x)] for c in C(A))
    e=dict(zip(("E1","E2","E3","E4","E5","E6","E7","E8","E9"),
               (E1,E2,E3,E4,E5,E6,E7,E8,E9)))
    assert all(e.values()),f'{A["name"]}->{B["name"]}: {e}'
    return e

def main():
    L=model("L",dict(zip(TYPES,(("a","b","u"),("e0","e1","e2"),
      ("p0","p1","p2"),("metric","other"),("r0","r1")))),
      {"metric":(-1,0,1),"other":(0,2,3)},1)
    M=model("M",dict(zip(TYPES,(("A","B","U"),("E0","E1","E2"),
      ("P0","P1","P2"),("mu","nu"),("R0","R1")))),
      {"metric":(1,0,-1),"other":(0,7,8)},2)
    N=model("N",dict(zip(TYPES,(("X","Y","Z"),("F0","F1","F2"),
      ("Q0","Q1","Q2"),("kappa","xi"),("S0","S1")))),
      {"metric":(-1,0,1),"other":(0,4,5)},-6)
    for z in (L,M,N):valid_core(z)
    f,g=arrow(L,M),arrow(M,N);h=compose(g,f)
    checks=0
    for z in (L,M,N):
        check(ident(z));checks+=1
    for x in (f,g,h):
        for y in (x,inverse(x),compose(inverse(x),x),compose(x,inverse(x))):
            check(y);checks+=1
    assert h["I"]["metric"][-1]==-1 and h["J"]==-6
    assert inverse(f)["I"]["mu"][1]==-1
    for x in (f,g,h):
        assert compose(inverse(x),x)["f"]==ident(x["A"])["f"]
        assert compose(x,inverse(x))["f"]==ident(x["B"])["f"]
    ch=sorted(C(L));subsets=[set(t) for k in range(len(ch)+1) for t in combinations(ch,k)]
    assert len(subsets)==16
    for x in (f,h):
        for F in subsets:
            assert x["J"]*sum(L["term"][c] for c in F)==sum(
                x["B"]["term"][image(c,x)] for c in F)
    # Negative premise check: a different zero image is not strict.
    bad=dict(f); bad["I"]={k:dict(v) for k,v in f["I"].items()}
    bad["I"]["metric"][0]=1
    failed=False
    try:check(bad)
    except AssertionError:failed=True
    assert failed
    result={"case_id":"FAS-F2-T6.14-001","source_sha256":SOURCE_SHA,
            "selected_core_models":3,"core_closure_fixture_checks_passed":True,
            "admitted_channels_per_model":4,"reflexivity_identities":3,
            "e1_e9_checked_maps":checks,"inverse_strict_maps":3,
            "left_right_inverse_composites":6,"transitivity_composites":1,
            "finite_channel_subsets":16,"finite_composite_equalities":32,
            "nontrivial_indexed_value_inverse":True,
            "nontrivial_J_composite":"-6",
            "zero_preservation_invalid_premise_detected":True,
            "finite_checks_not_general_proof":True,
            "independent_external_verification":False,
            "all_checks_passed":True}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (
        Path(__file__).resolve().parent.parent/"results"/"t614_strict_equivalence.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("T6.14 finite checks PASS; 3 descriptors, 15 strict comparison checks, 32 finite composites")
    print("OUTPUT",out)

if __name__=="__main__":main()
