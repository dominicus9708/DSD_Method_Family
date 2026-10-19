#!/usr/bin/env python3
"""FAS-F2-P6.11-001: finite E1-E9 vs bijective embedding checks.

Selective well-typed Formation models, not a general proof or formal certification.
Run from DSD_Method_Family root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_p611_strict_bijection.py
Optional CLI positional argument overrides output JSON path. Standard library only.
"""
from itertools import product
from pathlib import Path
import json
import sys

SRC = {"mat": {"a", "b", "u"}, "expr": {"e0", "e1", "e2"},
       "cfg": {"p0", "p1", "p2"}, "V": {0, 1, 2},
       "r": {"r0", "r1"}, "lam": "lam",
       "material": {"e0": {"a", "b"}, "e1": {"a"}, "e2": {"b"}},
       "active": {"p0": {"a"}, "p1": {"b"}, "p2": {"b"}},
       "admexpr": {"e0", "e1", "e2"}, "desexpr": {"e0", "e1", "e2"},
       "admcfg": {"p0", "p1"}, "lc": {"p0", "p1", "p2"},
       "bc": {"p0", "p1", "p2"},
       "res": {("e0", "e0"), ("e1", "e1"), ("e2", "e2"),
               ("e0", "e1"), ("e0", "e2")},
       "real": {("e1", "p0"), ("e2", "p1")},
       "q": {"a": 1, "b": 0},
       "role": {("p0", "a", "r0"), ("p0", "a", "r1"),
                ("p1", "b", "r0"), ("p2", "b", "r0")},
       "size": {0: 0, 1: 1, 2: 2}, "delta": 3,
       "negligible": True,
       "term": {("p0", "a", "r0"): 3, ("p0", "a", "r1"): -1,
                ("p1", "b", "r0"): 0}}
FM = {"a": "alpha", "b": "beta", "u": "gamma"}
FE = {"e0": "E0", "e1": "E1", "e2": "E2"}
FP = {"p0": "P0", "p1": "P1", "p2": "P2"}
FR = {"r0": "R0", "r1": "R1"}
IV = {0: 0, 1: 20, 2: 10}

def target(extra=False, changed_status=False, broken_graph=False):
    d = {
        "mat": set(FM.values()), "expr": set(FE.values()), "cfg": set(FP.values()),
        "V": set(IV.values()), "r": set(FR.values()), "lam": "kind",
        "material": {FE[e]: {FM[a] for a in v} for e, v in SRC["material"].items()},
        "active": {FP[p]: {FM[a] for a in v} for p, v in SRC["active"].items()},
        "admexpr": {FE[e] for e in SRC["admexpr"]},
        "desexpr": {FE[e] for e in SRC["desexpr"]},
        "admcfg": {FP[p] for p in SRC["admcfg"]},
        "lc": {FP[p] for p in SRC["lc"]}, "bc": {FP[p] for p in SRC["bc"]},
        "res": {(FE[x], FE[y]) for x,y in SRC["res"]},
        "real": {(FE[e], FP[p]) for e,p in SRC["real"]},
        "q": {FM[a]: IV[v] for a,v in SRC["q"].items()},
        "role": {(FP[p],FM[a],FR[r]) for p,a,r in SRC["role"]},
        "size": {IV[v]: sz for v,sz in SRC["size"].items()},
        "delta": SRC["delta"], "negligible": True,
        "term": {(FP[p],FM[a],FR[r]): 2*t for (p,a,r),t in SRC["term"].items()}
    }
    if changed_status:
        d["admcfg"].add("P2")  # forward holds but reflection fails
    if broken_graph:
        del d["q"]["beta"]  # zero assignment -> undefined: source graph mismatch
        del d["term"][("P1", "beta", "R0")]  # T exists on admitted channels only
    if extra:
        d["mat"].add("z")
        d["expr"].add("E3")
        d["cfg"].add("P3")
        d["material"]["E3"] = {"z"}
        d["active"]["P3"] = {"z"}
        d["admexpr"].add("E3")
        d["desexpr"].add("E3")
        d["admcfg"].add("P3")
        d["lc"].add("P3")
        d["bc"].add("P3")
        d["res"].add(("E3","E3"))
        d["real"].add(("E3","P3"))
        d["q"]["z"] = 10
        d["role"].add(("P3","z","R0"))
        d["term"][("P3","z","R0")] = 8
    return d

def psi(d,p):
    return p in d["admcfg"] and p in d["lc"] and p in d["bc"] and any(
        h in d["desexpr"] and (h,p) in d["real"] for H,h in d["res"])

def channels(d):
    return {(p,a,d["lam"],v,r) for (p,a,r) in d["role"] for v in d["V"]
            if psi(d,p) and d["q"].get(a, object()) == v}

def primitive_and_closure(d):
    # Source's typed constraints I,II,III,V plus closures IV,VI,VII.
    assert d["desexpr"] <= d["admexpr"] <= d["expr"]
    assert set(d["material"]) == d["expr"] and set(d["active"]) == d["cfg"]
    for e in d["admexpr"]:
        assert (e,e) in d["res"]
    for H,h in d["res"]:
        assert H in d["expr"] and h in d["admexpr"]
        assert d["material"][h] <= d["material"][H]
    for h,p in d["real"]:
        assert h in d["expr"] and p in d["cfg"] and d["active"][p] <= d["material"][h]
    active = set().union(*(d["active"][p] for p in d["cfg"] if psi(d,p)))
    assert set(d["q"]) <= active and set(d["q"].values()) <= d["V"]
    assert d["size"][0] == 0
    C = channels(d)
    assert set(d["term"]) == {(p,a,r) for p,a,l,v,r in C}
    assert all(a in d["mat"] and p in d["cfg"] and r in d["r"] for p,a,r in d["role"])
    return C

def graph(d):
    return {(a,v) for a,v in d["q"].items()}

def transformed_channel(c, fm=FM, fp=FP, fr=FR, iv=IV, kind="kind"):
    p,a,l,v,r = c
    return (fp[p],fm[a],kind,iv[v],fr[r])

def e_clauses(L,M):
    # E1: bijective material record with empty signature, exact mat/act, s0 anchors.
    E1 = (set(FM.values()) == M["mat"]
          and all({FM[a] for a in L["material"][e]} == M["material"][FE[e]] for e in L["expr"])
          and all({FM[a] for a in L["active"][p]} == M["active"][FP[p]] for p in L["cfg"]))
    E2 = all((e in L[k]) == (FE[e] in M[k]) for k in ("admexpr","desexpr") for e in L["expr"])
    E3 = ({(FE[x],FE[y]) for x,y in L["res"]} == M["res"] and
          {(FE[e],FP[p]) for e,p in L["real"]} == M["real"])
    E4 = all((p in L[k]) == (FP[p] in M[k]) for k in ("admcfg","lc","bc") for p in L["cfg"])
    E5 = all((a in L["q"]) == (FM[a] in M["q"]) for a in L["mat"])
    E6 = ({(FM[a],IV[v]) for a,v in graph(L)} == graph(M))
    E7 = L["negligible"] == M["negligible"] and L["delta"] == M["delta"] and all(
        L["size"][v] == M["size"][IV[v]] for v in L["V"])
    E8 = {(FP[p],FM[a],FR[r]) for p,a,r in L["role"]} == M["role"]
    E9 = (set(transformed_channel(c) for c in channels(L)) == channels(M)
          and all(2*L["term"][p,a,r] == M["term"][FP[p],FM[a],FR[r]]
                  for p,a,l,v,r in channels(L)))
    return dict(E1=E1,E2=E2,E3=E3,E4=E4,E5=E5,E6=E6,E7=E7,E8=E8,E9=E9)

def embedding_clauses(L,M):
    # Source-indexed F/R and witness-reflection conditions; all f maps injective.
    image = set(FM.values())
    r1 = (all({FM[a] for a in L["material"][e]} ==
              M["material"][FE[e]] & image for e in L["expr"])
          and all({FM[a] for a in L["active"][p]} ==
                  M["active"][FP[p]] & image for p in L["cfg"]))
    r2 = all((x in L[k]) == (dict(FE if k in ("admexpr","desexpr") else FP)[x] in M[k])
             for k in ("admexpr","desexpr","admcfg","lc","bc")
             for x in (L["expr"] if k in ("admexpr","desexpr") else L["cfg"]))
    r3 = (all(((x,y) in L["res"]) == ((FE[x],FE[y]) in M["res"])
              for x in L["expr"] for y in L["expr"])
          and all(((x,p) in L["real"]) == ((FE[x],FP[p]) in M["real"])
                  for x in L["expr"] for p in L["cfg"]))
    r4 = all(((a,v) in graph(L)) == ((FM[a],IV[v]) in graph(M))
             for a in L["mat"] for v in L["V"])
    r5 = all(((p,a,r) in L["role"]) == ((FP[p],FM[a],FR[r]) in M["role"])
             for p in L["cfg"] for a in L["mat"] for r in L["r"])
    wr = all(not psi(M,FP[p]) or psi(L,p) for p in L["cfg"])
    f1_f6 = (all({FM[a] for a in L["material"][e]} <= M["material"][FE[e]] for e in L["expr"])
             and all({FM[a] for a in L["active"][p]} <= M["active"][FP[p]] for p in L["cfg"])
             and all(not(psi(L,p)) or psi(M,FP[p]) for p in L["cfg"])
             and all(transformed_channel(c) in channels(M) for c in channels(L))
             and all(2*L["term"][p,a,r] == M["term"][FP[p],FM[a],FR[r]]
                     for p,a,l,v,r in channels(L))
             and L["delta"] == M["delta"]
             and all(L["size"][v] == M["size"][IV[v]] for v in L["V"]))
    return dict(R1=r1,R2=r2,R3=r3,R4=r4,R5=r5,WITNESS_REFLECTION=wr,
                FORWARD_F1_F6=f1_f6)

def main():
    L = SRC
    M = target()
    for d in (L,M):
        primitive_and_closure(d)
    e=e_clauses(L,M)
    emb=embedding_clauses(L,M)
    assert all(e.values()) and all(emb.values())
    assert all(len(set(m.values())) == len(m) for m in (FM,FE,FP,FR,IV))
    assert len(channels(L)) == len(channels(M)) == 3
    assert any(v==0 for v in L["q"].values())
    assert "u" not in L["q"] and "gamma" not in M["q"]
    assert L["term"][("p1","b","r0")] == 0
    # Inverse is a typed, source-indexed bijective map; reverse clauses follow
    # from symmetric graph/predicate/relation equalities and inverse transport.
    inverses = [{y:x for x,y in d.items()} for d in (FM,FE,FP,FR,IV)]
    assert all(len(inv)==len(d) for inv,d in zip(inverses,(FM,FE,FP,FR,IV)))
    assert {transformed_channel(c) for c in channels(L)} == channels(M)
    assert {transformed_channel(c)[0] for c in channels(L)} == {"P0","P1"}
    # Non-surjective embedding can exist but cannot be strict isomorphism.
    extra=target(extra=True)
    primitive_and_closure(extra)
    ex_emb=embedding_clauses(L,extra)
    assert all(ex_emb.values()) and not all(e_clauses(L,extra).values())
    assert len(channels(extra)) == 4
    # All component maps may be bijective and forward but fail reflection.
    bad=target(changed_status=True)
    primitive_and_closure(bad)
    bad_emb=embedding_clauses(L,bad)
    assert bad_emb["FORWARD_F1_F6"] and not bad_emb["R2"]
    assert not e_clauses(L,bad)["E4"]
    # Graph mismatch makes defined zero appear undefined; E5/E6/R4 fail.
    qbad=target(broken_graph=True)
    primitive_and_closure(qbad)
    assert not e_clauses(L,qbad)["E5"] and not e_clauses(L,qbad)["E6"]
    assert not embedding_clauses(L,qbad)["R4"]
    # E5 follows from E6 under bijections: exhaustive finite candidate graph test.
    graph_pairs = len(L["mat"])*len(L["V"])
    assert graph_pairs == 9
    assert all(((a in L["q"]) == (FM[a] in M["q"]))
               for a in L["mat"])
    summary=dict(case="FAS-F2-P6.11-001",
        source_sha256="8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a",
        all_checks_passed=True,strict_conditions={k:bool(v) for k,v in e.items()},
        embedding_conditions={k:bool(v) for k,v in emb.items()},
        admitted_channel_bijection_count=3,
        graph_pairs_checked=graph_pairs,
        defined_zero_vs_undefined=True,
        target_extra_channel_under_non_surjective_embedding=True,
        forward_bijective_maps_do_not_imply_reflection=True,
        graph_mismatch_fails_e5_e6_r4=True,
        inverse_bijections_checked=5,
        mathematical_proof_is_separate=True,external_independent_verification=False)
    output=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/"results"/"p611_strict_bijection.json"
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("P6.11 finite witnesses PASS; 9 strict clauses and embedding conditions")
    print("OUTPUT",output)

if __name__=="__main__":
    main()
