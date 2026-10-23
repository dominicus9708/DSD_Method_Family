#!/usr/bin/env python3
"""P12 source-bound finite negative controls for optional representations/aggregates.

Kwon Dominicus, General Property Axiom System, manuscript 2026-09-01.
Checks exact Def 5.4, 6.10/6.11 and §9.2 type conditions in examples.
Does not claim an all-model theorem or change any original experiment script.
Usage: python verify_p12_representation_aggregate.py [output_json]
"""
from itertools import permutations
from pathlib import Path
import json, sys

SHA = "03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"
PROFILES = {"p": ("u",), "q": ("u","u")}
REPS = {"j": (1, (0, 1)), "k": (2, (0, 1))}

def make_core(carrier, phi_from_baseline):
    # Primitive applicability and two prerequisite sets are all the typed input
    # products. Only the partial Xi graphs below are selectively defined.
    phi = phi_from_baseline
    vals = {
      "p": {(phi["a"],):0, (phi["b"],):2},
      "q": {(phi["a"],phi["b"]):7}}
    universe = {
      "p": {(x,) for x in carrier},
      "q": {(x,y) for x in carrier for y in carrier}
    }
    assert all(set(vals[k]) <= universe[k] for k in PROFILES)
    return {"carrier": tuple(carrier), "universe": universe, "Xi": vals}

def records(A):
    return frozenset((k,x,z) for k in PROFILES for x,z in A["Xi"][k].items())

def map_record(r, phi):
    k,x,z = r
    return (k, tuple(phi[v] for v in x), z)

def strict_core(A,B,phi):
    return (len(phi) == len(A["carrier"]) and set(phi) == set(A["carrier"])
        and set(phi.values()) == set(B["carrier"]) and len(set(phi.values()))==len(phi)
        and all({tuple(phi[v] for v in x) for x in A["universe"][k]} == B["universe"][k]
                for k in PROFILES)
        and {map_record(r,phi) for r in records(A)} == records(B))

def package(active, selected=None, encoded=None):
    selected=selected or {}
    encoded=encoded or {}
    assert set(selected)<=set(active) and set(encoded)<=set(active)
    P={}
    for j in active:
        ys=frozenset(selected.get(j,()))
        n,E=REPS[j]
        assert all(len(y)==n for y in ys)
        enc=dict(encoded.get(j,{}))
        assert set(enc)==ys and all(z in E for z in enc.values())
        P[j]=(ys,enc)
    return P

def lift(A,B,phi,PA,PB):
    if not strict_core(A,B,phi) or set(PA)!=set(PB):
        return False
    for j in PA:
        YA,EA=PA[j]; YB,EB=PB[j]
        transported={tuple(map_record(r,phi) for r in y) for y in YA}
        if transported!=YB:
            return False
        if any(EA[y]!=EB[tuple(map_record(r,phi) for r in y)] for y in YA):
            return False
    return True

def transported_package(P,phi):
    new={}
    for j,(ys,enc) in P.items():
        Z={tuple(map_record(r,phi) for r in y):z for y,z in enc.items()}
        new[j]=(frozenset(Z),Z)
    return new

def reversed_map(phi):
    return {v:k for k,v in phi.items()}

def composed(f,g):
    return {k:g[f[k]] for k in f}

def summarize_pattern(d):
    return tuple(sorted((k, len(v),sum(z==0 for z in v.values()),
                        sum(z!=0 for z in v.values())) for k,v in d.items()))

def run():
    a={"a":"a","b":"b"}; ab={"a":"A","b":"B"}
    bc={"A":"C","B":"D"}
    ac=composed(ab,bc)
    A=make_core(("a","b"),a)
    B=make_core(("A","B"),ab)
    C=make_core(("C","D"),ac)
    assert strict_core(A,B,ab) and strict_core(B,C,bc) and strict_core(A,C,ac)
    ra=sorted(records(A),key=repr)
    p0=next(r for r in ra if r[0]=="p" and r[2]==0)
    p2=next(r for r in ra if r[0]=="p" and r[2]==2)
    qr=next(r for r in ra if r[0]=="q")
    Yj=((p0,),(p2,))
    Yk=((p0,qr),(qr,qr))
    P=package(("j","k"),{"j":Yj,"k":Yk},
              {"j":{(p0,):0,(p2,):1},"k":{(p0,qr):1,(qr,qr):0}})
    PB=transported_package(P,ab)
    PC=transported_package(P,ac)
    mismatch={j:(ys,dict(enc)) for j,(ys,enc) in PB.items()}
    y=next(iter(mismatch["j"][0]))
    mismatch["j"][1][y]=1-mismatch["j"][1][y]
    dropped={j:(ys,dict(enc)) for j,(ys,enc) in PB.items()}
    dropped["k"]=(frozenset(),{})
    checks={
       "base_core_strict_iso_A_B_C":strict_core(A,B,ab) and strict_core(B,C,bc),
       "representation_identity":lift(A,A,a,P,P),
       "representation_inverse":lift(A,B,ab,P,PB) and
                         lift(B,A,reversed_map(ab),PB,P),
       "representation_composition":lift(A,B,ab,P,PB) and
                         lift(B,C,bc,PB,PC) and lift(A,C,ac,P,PC),
       "repeated_record_tuple_and_mixed_kind_labels":(qr,qr) in P["k"][0] and
                         (p0,qr) in P["k"][0],
       "same_core_different_encoding_not_rep_isomorphic":
                         strict_core(A,B,ab) and not lift(A,B,ab,P,mismatch),
       "different_selected_record_domains_prevent_lift":
                         not lift(A,B,ab,P,dropped),
       "different_active_representation_labels_prevent_lift":
                         not lift(A,B,ab,P,{"j":PB["j"]}),
       "inactive_empty_package_vacuous":lift(A,B,ab,package(()),package(())),
       "active_empty_selected_domain_vacuous":
                         lift(A,B,ab,package(("j",)),package(("j",))),
       "active_vs_inactive_distinguished":
                         not lift(A,B,ab,package(()),package(("j",))),
    }
    # Downstream aggregators Theta are external choices. A and A can be
    # identical cores and nevertheless have different aggregate values.
    sumA=sum(0 for r in records(A))
    sumB=sum(1 for r in records(A))
    checks["core_iso_does_not_imply_arbitrary_aggregate_equal"] = (
        strict_core(A,A,a) and sumA!=sumB)
    # Equal property-labelled counts and equal constant-Theta aggregate can
    # occur for non-isomorphic two-kind one-sort primitive assignment graphs.
    patternsA={"s":{0:0,1:1},"t":{0:0,1:1}}
    patternsB={"s":{0:0,1:1},"t":{0:1,1:0}}
    iso_patterns=False
    for perm in permutations((0,1)):
        if all({perm[x]:z for x,z in patternsA[k].items()}==patternsB[k]
               for k in patternsA):
            iso_patterns=True
    same_counts = summarize_pattern(patternsA)==summarize_pattern(patternsB)
    aggA=sum(0 for k in patternsA for x in patternsA[k])
    aggB=sum(0 for k in patternsB for x in patternsB[k])
    checks["equal_aggregate_can_hide_nonisomorphic_cores"] = (
        same_counts and aggA==aggB and not iso_patterns)
    # An equivariant bridge is sufficient for aggregate equality on a
    # strict-isomorphism-transported finite support, if aggregation respects
    # corresponding permutations; it does NOT supply a converse.
    thetaA={r:(1 if r[0]=="p" else 2) for r in records(A)}
    thetaB={map_record(r,ab):z for r,z in thetaA.items()}
    checks["transported_equivariant_bridge_yields_aggregate_equality"] = (
       sum(thetaA.values())==sum(thetaB.values()) and
       all(thetaA[r]==thetaB[map_record(r,ab)] for r in thetaA))
    assert all(checks.values()),checks
    return {
      "case":"PA-P12-20260901-REPRESENTATION-AGGREGATE-EDGE-001",
      "source_pdf_sha256":SHA,
      "cases":len(checks),
      "checks":checks,
      "source_6_10_rep_signature_labels":list(REPS),
      "two_representation_arities":[1,2],
      "core_strict_equivalence_implies_representation_lift":False,
      "core_strict_equivalence_implies_independent_aggregate_equality":False,
      "aggregate_equality_implies_core_strict_equivalence":False,
      "source_general_machine_proof_completed":False,
      "original_experiment_modified":False,"manuscript_modified":False,
      "full_FPA":"OPEN"}
if __name__=="__main__":
    obj=run()
    path=(Path(sys.argv[1]) if len(sys.argv)>1 else
          Path(__file__).resolve().parent.parent/"results/p12_representation_aggregate.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("P12 representation and aggregation bounded checks PASS:",obj["cases"])
