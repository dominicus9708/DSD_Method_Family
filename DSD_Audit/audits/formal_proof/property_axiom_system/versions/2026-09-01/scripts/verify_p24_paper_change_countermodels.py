#!/usr/bin/env python3
"""P24 finite countermodels for Property PDF 2026-09-01 §§4,6.
This only tests finite typed witnesses; mathematical arguments in P24 report
are separate from the executable. Does not change original manuscript.
Usage from DSD_Method_Family root:
  python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/verify_p24_paper_change_countermodels.py OUTPUT.json
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import json,sys

PAPER_SHA="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

@dataclass(frozen=True)
class Premodel:
    """One fixed shared typed signature: sorts u and v, one kind k of profile (u)."""
    available:tuple[tuple[str,tuple[str,...]],...]
    declared:frozenset[str]
    ap:tuple[tuple[str,frozenset[tuple[str,...]]],...]
    sat:tuple[tuple[str,frozenset[tuple[str,...]]],...]
    xi:tuple[tuple[str,tuple[tuple[tuple[str,...],int],...]],...]

def premodel(available=(), declared=(), ap=(), sat=(), xi=()):
    return Premodel(tuple(available),frozenset(declared),tuple(ap),tuple(sat),tuple(xi))

def unique(t):return len(t)==len(set(t))
def dictionary(pairs):
    k=[k for k,v in pairs]
    if not unique(k):raise ValueError("duplicate label")
    return dict(pairs)

def scope(A):
    aux=dictionary(A.available)
    if any(s not in ("u","v") or not unique(v) for s,v in aux.items()):
        raise ValueError("invalid supplied carrier")
    if not A.declared<=frozenset({"k"}):raise ValueError("wrong declaration")
    ap=dictionary(A.ap);sat=dictionary(A.sat);xi=dictionary(A.xi)
    X=frozenset((x,) for x in aux["u"]) if "u" in aux else None
    if X is not None and "k" in A.declared:
        if not ("k" in ap and "k" in sat and "k" in xi):raise ValueError("missing property primitive")
        for carrier in (ap["k"],sat["k"]):
            if not carrier<=X:raise ValueError("typed input violation")
        pairs=xi["k"]
        if not unique(tuple(x for x,z in pairs)):raise ValueError("nonfunctional xi")
        if not all(x in X and z in (0,1) for x,z in pairs):
            raise ValueError("xi outside carrier")
    pi= X is None or "k" not in A.declared or set(x for x,z in xi["k"])<=ap["k"]
    pii=X is None or "k" not in A.declared or set(x for x,z in xi["k"])<=sat["k"]
    return (aux, X, pi, pii)

def full_model(A):
    aux,X,pi,pii=scope(A)
    return pi and pii

def map_object(A,B,images=()):
    """maps of available source carriers, using sorted supplied function graph."""
    maps=dictionary(images)
    a,xA,_,_=scope(A)
    b,xB,_,_=scope(B)
    if not set(a)<=set(b) or not A.declared<=B.declared:return None
    if set(maps)!=set(a):return None
    for s,graph in maps.items():
        if not unique(tuple(k for k,v in graph)):return None
        d=dict(graph)
        if set(d)!=set(a[s]) or not set(d.values())<=set(b[s]):return None
    return maps

def forward(A,B,images=()):
    if not(full_model(A) and full_model(B)):return False
    maps=map_object(A,B,images)
    if maps is None:return False
    a,X,_,_=scope(A)
    if "k" in A.declared and X is not None:
        im=maps["u"]
        f=lambda x:(dict(im)[x[0]],)
        apA=dictionary(A.ap)["k"];apB=dictionary(B.ap)["k"]
        satA=dictionary(A.sat)["k"];satB=dictionary(B.sat)["k"]
        xiA=dict(dictionary(A.xi)["k"]);xiB=dict(dictionary(B.xi)["k"])
        if not all(f(x) in apB for x in apA):return False
        if not all(f(x) in satB for x in satA):return False
        if not all(f(x) in xiB and xiB[f(x)]==z for x,z in xiA.items()):return False
    return True

def embedding(A,B,images=()):
    if not forward(A,B,images):return False
    maps=map_object(A,B,images)
    if not all(unique(tuple(v for k,v in graph)) for graph in maps.values()):return False
    a,X,_,_=scope(A)
    if "k" in A.declared and X is not None:
        f=lambda x:(dict(maps["u"])[x[0]],)
        for key in ("ap","sat"):
            ca=dictionary(getattr(A,key))["k"]
            cb=dictionary(getattr(B,key))["k"]
            if not all((x in ca)==(f(x) in cb) for x in X):return False
        xa=dict(dictionary(A.xi)["k"])
        xb=dict(dictionary(B.xi)["k"])
        if not all((x in xa)==(f(x) in xb) for x in X):return False
    return True

def bijective_embedding(A,B,images=()):
    if not embedding(A,B,images):return False
    maps=map_object(A,B,images)
    a,_,_,_=scope(A);b,_,_,_=scope(B)
    return all(set(v for k,v in maps[s])==set(b[s]) for s in a)

def strict(A,B,images=()):
    """Print's S1--S3 + S4's inverse check, not mere bijective embedding."""
    if not bijective_embedding(A,B,images):return False
    aa,_,_,_=scope(A);bb,_,_,_=scope(B)
    if set(aa)!=set(bb) or A.declared!=B.declared:return False
    ims=map_object(A,B,images)
    inverse=tuple((s,tuple(sorted((v,k) for k,v in graph))) for s,graph in ims.items())
    return embedding(B,A,inverse)

def main():
    passed={}
    def test(key,condition):
        passed[key]=bool(condition)
        assert condition,key
    # Well-typed and admitted models may declare a kind with an unavailable profile.
    U=premodel(declared=("k",))
    V=premodel(available=(("u",("y",)),),declared=("k",),
        ap=(("k",frozenset()),),sat=(("k",frozenset()),),xi=(("k",()),))
    test("unavailable_declared_is_admitted",full_model(U))
    test("unavailable_product_not_empty",scope(U)[1] is None)
    test("available_one_element_product",scope(V)[1]==frozenset({("y",)}))
    test("unguarded_F3_source_expression_is_undefined",scope(U)[1] is None and "k" in U.declared)
    test("unguarded_identity_F3_also_undefined",full_model(U) and scope(U)[1] is None)
    test("guarded_identity_exists_for_unavailable",forward(U,U,()))
    test("guarded_U_to_V_forward",forward(U,V,()))
    test("guarded_U_to_V_embedding",embedding(U,V,()))
    test("unavailable_U_V_not_strict",not strict(U,V,()))
    # Empty but supplied: exists and is not the same as unavailable.
    E=premodel(available=(("u",()),),declared=("k",),
        ap=(("k",frozenset()),),sat=(("k",frozenset()),),xi=(("k",()),))
    test("available_empty_product_is_empty_set",scope(E)[1]==frozenset())
    test("available_empty_distinct_unavailable",scope(E)[1]!=scope(U)[1])
    test("E_to_E_bijective_embedded",bijective_embedding(E,E,(("u",()),)))
    test("E_to_E_strict",strict(E,E,(("u",()),)))
    # Independent S2 counterexample, no kinds declared, extra available u in B.
    A2=premodel()
    B2=premodel(available=(("u",("y",)),))
    test("S2_extra_available_sort_model_welltyped",full_model(A2) and full_model(B2))
    test("S2_extra_available_sort_bijective_embedding",bijective_embedding(A2,B2,()))
    test("S2_extra_available_sort_not_strict",not strict(A2,B2,()))
    # Independent S3 counterexample, same sort availability, target additional declaration.
    A3=premodel(available=(("u",("x",)),))
    B3=premodel(available=(("u",("y",)),),declared=("k",),
        ap=(("k",frozenset()),),sat=(("k",frozenset()),),xi=(("k",()),))
    g=(("u",(("x","y"),)),)
    test("S3_target_extra_declaration_admitted",full_model(A3) and full_model(B3))
    test("S3_target_extra_declaration_bijective_embedding",bijective_embedding(A3,B3,g))
    test("S3_target_extra_declaration_not_strict",not strict(A3,B3,g))
    # Positive symmetry, identity, transitivity of corrected strict relation.
    C=premodel(available=(("u",("z",)),),declared=("k",),
        ap=(("k",frozenset({("z",)})),),sat=(("k",frozenset({("z",)})),),
        xi=(("k",((("z",),1),)),))
    D=premodel(available=(("u",("w",)),),declared=("k",),
        ap=(("k",frozenset({("w",)})),),sat=(("k",frozenset({("w",)})),),
        xi=(("k",((("w",),1),)),))
    E2=premodel(available=(("u",("t",)),),declared=("k",),
        ap=(("k",frozenset({("t",)})),),sat=(("k",frozenset({("t",)})),),
        xi=(("k",((("t",),1),)),))
    cd=(("u",(("z","w"),)),); dc=(("u",(("w","z"),)),)
    de=(("u",(("w","t"),)),); ce=(("u",(("z","t"),)),)
    test("strict_reflexivity",strict(C,C,(("u",(("z","z"),)),)))
    test("strict_symmetry_forward",strict(C,D,cd))
    test("strict_symmetry_reverse",strict(D,C,dc))
    test("strict_transitivity_first",strict(D,E2,de))
    test("strict_transitivity_composite",strict(C,E2,ce))
    test("value_preservation",dict(dictionary(C.xi)["k"])[("z",)]==dict(dictionary(D.xi)["k"])[("w",)])
    # Negative preserving domain/value requirement
    N=replace(D,xi=(("k",((("w",),0),)),))
    test("bijective_carrier_map_not_value_preservation",not embedding(C,N,cd))
    test("S4_auto_given_equal_declarations_and_availability_in_finite_cases",
         strict(C,D,cd)==(bijective_embedding(C,D,cd) and set(dict(C.available))==set(dict(D.available))
                            and C.declared==D.declared))
    # Typed countermodels P I/II independent, never full C1 cores.
    A0=premodel(available=(("u",("x",)),),declared=("k",),
        ap=(("k",frozenset()),),sat=(("k",frozenset({("x",)})),),
        xi=(("k",((("x",),1),)),))
    B0=premodel(available=(("u",("x",)),),declared=("k",),
        ap=(("k",frozenset({("x",)})),),sat=(("k",frozenset()),),
        xi=(("k",((("x",),1),)),))
    test("PA_I_false_II_true_typed_premodel",scope(A0)[2:]==(False,True))
    test("PA_I_true_II_false_typed_premodel",scope(B0)[2:]==(True,False))
    test("C1_not_admissible_for_countermodel_I",not full_model(A0))
    test("C1_not_admissible_for_countermodel_II",not full_model(B0))
    test("both_good_full_core",full_model(C))
    assert all(passed.values())
    return {"case":"PA-P24-20260901-SOURCE-PAPER-REVISION-COUNTERMODELS-001",
            "source_sha256":PAPER_SHA, "checks":passed, "checks_count":len(passed),
            "all_expected_observations_reproduced":True,
            "source_required_changes":["Def6.1_F3_to_F5_profile_availability",
                                       "Theorem6.8_bijective_embedding_missing_S2_S3",
                                       "Theorem4.3_C1_relative_scope_clarification"],
            "source_abstract_Th11_1_downstream_revision_needed":True,
            "not_full_ZFC_formalization":True,"original_pdf_tex_zenodo_edited":False,
            "overall_property_FPA":"OPEN"}

if __name__=="__main__":
    result=main()
    dst=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("p24_result.json")
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print("P24 SOURCE REVISION COUNTERMODELS",result["checks_count"],"EXPECTED OBSERVATIONS PASS")
