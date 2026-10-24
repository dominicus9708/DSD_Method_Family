#!/usr/bin/env python3
"""P20 full primitive-preserving C1 completion/reduction finite audit.

Paper: Kwon Dominicus, DSD Property Axiom System English (2026-09-01).
P17 is imported ONLY for independent typed-core admission; its summary
completion() is never used. This does not implement the whole Stage VI model.
Usage from DSD_Method_Family root:
 python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/verify_p20_full_c1_inverse.py OUTPUT_JSON
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import json
import sys
import verify_p17_typed_reference_validator as ref

SOURCE_SHA="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

@dataclass(frozen=True)
class Primitive:
    stage_vi_anchor: str
    signature: ref.Signature
    prem: ref.Premodel
    surplus_policy: str="reject"

@dataclass(frozen=True)
class Completion:
    primitive: Primitive
    domains: dict[str,frozenset]
    dep_satisfied: dict[str,frozenset]
    status: dict[str,dict[tuple,str]]
    unavailable_kinds: frozenset[str]
    defined_records: frozenset[tuple]

def snapshot(p):
    """Clone built-in containers WITHOUT relabelling typed elements via repr."""
    m=p.prem
    return Primitive(p.stage_vi_anchor,p.signature,ref.Premodel(
        {k:tuple(v) for k,v in m.aux.items()}, tuple(m.declared),
        {k:set(v) for k,v in m.ap.items()},
        {k:set(v) for k,v in m.sat.items()},
        {k:dict(ref.as_function(v)[0]) for k,v in m.xi.items()}),
        p.surplus_policy)

def comp_prop(p):
    """Admitted cores only. Retain all exact primitive values and typed records."""
    validity=ref.validate(p.signature,p.prem,surplus=p.surplus_policy)
    if validity["classification"]!="admitted_core":
        raise ValueError(("C1 requires admitted typed primitive core",validity))
    p=snapshot(p)
    s,m=p.signature,p.prem
    domains={};deps={};statuses={};unavailable=set();records=set()
    for k in m.declared:
        X=ref.product(s,m,k)
        if X is None:
            unavailable.add(k)
            continue
        assign,_=ref.as_function(m.xi[k])
        D=frozenset(assign)
        dep=frozenset(X)
        for d in s.kinds[k].deps:
            dep=dep & frozenset(m.sat[k,d])
        assert D<=m.ap[k] and D<=dep
        domains[k]=D;deps[k]=dep
        label={}
        for x in X:
            if x not in m.ap[k]:state="inapplicable"
            elif x not in dep:state="prerequisite-unsatisfied"
            elif x not in D:state="applicable-undefined"
            elif s.kinds[k].zero_bearing:
                state="defined-zero" if assign[x]==s.kinds[k].zero else "defined-nonzero"
            else:state="defined"
            label[x]=state
        statuses[k]=label
        for x,z in assign.items():
            records.add((k,x,z))
    return Completion(p,domains,deps,statuses,frozenset(unavailable),frozenset(records))

def full_is_valid(a):
    if not isinstance(a,Completion):return False
    try:
        # Derived object has **no freedom** to add or remove status records.
        expected=comp_prop(a.primitive)
        return a==expected
    except (ValueError,TypeError,KeyError):return False

def red_prop(a):
    if not full_is_valid(a):
        raise ValueError("Not a legitimate, fully C1-completed property model")
    # Retain every primitive coordinate, but not the derived ones.
    return snapshot(a.primitive)

def kinds_baseline():
    return ref.Signature({"h":frozenset({"H0","H1"})},frozenset({"u","v"}),{
        "p":ref.Kind(("u",),frozenset({0,1,2}),frozenset({"d1","d2"}),0,True),
        "q":ref.Kind(("u","u"),frozenset({0,1,2})),
        "m":ref.Kind(("h","u","h"),frozenset({0,1,2})),
        "unavailable":ref.Kind(("v",),frozenset({0,1,2}))},frozenset({"d1","d2"}))

def make_model(value=1,variant="baseline",policy="reject"):
    s=kinds_baseline()
    m=ref.Premodel({"u":("x","y")},("p","q","m","unavailable"),
        {"p":{("x",),("y",)},"q":{("x","y"),("x","x")},
         "m":{("H0","x","H1")}},
        {("p","d1"):{("x",),("y",)},("p","d2"):{("x",)}},
        {"p":{("x",):value},"q":{("x","y"):1},
         "m":{("H0","x","H1"):2}})
    if variant=="baseline":pass
    elif variant=="supplied_empty":
        m.aux["v"]=()
        m.ap["unavailable"]=set()
        m.xi["unavailable"]={}
    elif variant=="two_value_changes":
        m.xi["p"]={("x",):value}
    else:raise ValueError(variant)
    return Primitive("frozen-stage-VI-alpha",s,m,policy)

def main():
    checks={}; cases={}
    def ok(name,predicate):
        assert predicate,name
        checks[name]=True
    def roundtrip(name,p):
        a=comp_prop(p)
        ok(name+"_RedComp_P",red_prop(a)==p)
        ok(name+"_CompRed_A",comp_prop(red_prop(a))==a)
        ok(name+"_fully_admitted",full_is_valid(a))
        ok(name+"_full_defined_records_exact",
           len(a.defined_records)==sum(len(z) for z in p.prem.xi.values()))
        return a
    a=roundtrip("baseline",make_model())
    ok("baseline_stage_VI_anchor_retained",a.primitive.stage_vi_anchor=="frozen-stage-VI-alpha")
    ok("baseline_two_prerequisites_intersection",
       a.dep_satisfied["p"]==frozenset({("x",)}))
    ok("baseline_undefined_applicable_differentiated",
       a.status["p"][("y",)]=="prerequisite-unsatisfied")
    ok("baseline_repeated_profile_values_exact",
       ("q",("x","y"),1) in a.defined_records)
    ok("baseline_mixed_inherited_aux_exact",
       ("m",("H0","x","H1"),2) in a.defined_records)
    ok("unavailable_kind_distinct",a.unavailable_kinds==frozenset({"unavailable"}))
    b=roundtrip("different_nonzero_value",make_model(value=2))
    ok("different_nonzero_values_do_not_collapse",a!=b and a.defined_records!=b.defined_records)
    ok("value_1_exact_record",("p",("x",),1) in a.defined_records)
    ok("value_2_exact_record",("p",("x",),2) in b.defined_records)
    c=roundtrip("supplied_empty_vs_unavailable",make_model(variant="supplied_empty"))
    ok("supplied_empty_kind_available", "unavailable" not in c.unavailable_kinds
       and c.domains["unavailable"]==frozenset()
       and ref.product(c.primitive.signature,c.primitive.prem,"unavailable")==frozenset())
    ok("supplied_empty_distinct_from_undefined",c!=a)
    # Source C1 retains primitive inputs even where zero prerequisite kinds.
    s=kinds_baseline()
    empty_deps=ref.Premodel({"u":("x","y")},("q",),
        {"q":{("x","x")}}, {},{"q":{("x","x"):0}})
    d=roundtrip("zero_prerequisites",Primitive("F6-alpha",s,empty_deps))
    ok("zero_dep_means_full_profile",d.dep_satisfied["q"]==ref.product(s,empty_deps,"q"))
    # Full status keys are actual typed tuples; Python repr collisions are irrelevant.
    class SameRepr:
        def __repr__(self):return "identical"
    u,v=SameRepr(),SameRepr()
    sx=ref.Signature({"h":frozenset({u,v})},frozenset(),{
        "p":ref.Kind(("h",),frozenset({0,1,2}))},frozenset())
    mx=ref.Premodel({},("p",),{"p":{(u,),(v,)}}, {},
                   {"p":{(u,):1,(v,):2}})
    e=roundtrip("distinct_same_repr",Primitive("F6-two-reprs",sx,mx))
    ok("same_repr_two_status_keys_retained",len(e.status["p"])==2)
    ok("same_repr_two_defined_records_retained",len(e.defined_records)==2)
    # Refuse C1 on typed premodels failing one axiom.
    for name,kwargs in (
      ("pi_violated",{"ap":{"p":set(),"q":{("x","y"),("x","x")},
                              "m":{("H0","x","H1")}}}),
      ("pii_violated",{"xi":{"p":{("y",):1},"q":{("x","y"):1},
                               "m":{("H0","x","H1"):2}}})):
        p=make_model()
        for k,z in kwargs.items():setattr(p.prem,k,z)
        valid=ref.validate(p.signature,p.prem)
        ok(name+"_typed_premodel",valid["classification"]=="typed_premodel")
        try:comp_prop(p)
        except ValueError:ok(name+"_completion_refused",True)
        else:raise AssertionError(name+" not refused")
    # Reject a tampered/full-model derived coordinate.
    mutated_status={k:dict(v) for k,v in a.status.items()}
    mutated_status["p"][("x",)]="fabricated"
    corrupt=Completion(a.primitive,a.domains,a.dep_satisfied,mutated_status,
                       a.unavailable_kinds,a.defined_records)
    ok("tampered_derived_status_detected",not full_is_valid(corrupt))
    try:red_prop(corrupt)
    except ValueError:ok("tampered_full_model_reduction_refused",True)
    else:raise AssertionError("Tampered completed model was reduced")
    altered_records=Completion(a.primitive,a.domains,a.dep_satisfied,a.status,
                               a.unavailable_kinds,frozenset())
    ok("tampered_defined_records_detected",not full_is_valid(altered_records))
    # Optional incidental metadata policy: strict means reject it;
    # ignore mode preserves the extra primitive data exactly on reduction.
    extra=make_model(policy="ignore")
    extra.prem.ap["ghostkind"]={("extra",)}
    ex=roundtrip("surplus_metadata_ignored_and_preserved",extra)
    ok("surplus_coordinate_preserved",
       ex.primitive.prem.ap["ghostkind"]=={("extra",)})
    strict=make_model(policy="reject")
    strict.prem.ap["ghostkind"]={("extra",)}
    try:comp_prop(strict)
    except ValueError:ok("surplus_metadata_strictly_refused",True)
    else:raise AssertionError("Surplus strict admission was not rejected")
    # An explicit primitive-coordinate change must never be hidden by the
    # derived summary; independent full objects remain different.
    snap=red_prop(a)
    snap.prem.xi["p"][("x",)]=0
    z=comp_prop(snap)
    ok("changing_primitive_changes_exact_completion",z!=a and ("p",("x",),0) in z.defined_records)
    ok("primitive_reference_identity_preserved",
       red_prop(a).stage_vi_anchor==a.primitive.stage_vi_anchor)
    assert all(checks.values())
    cases={"baseline_exact_records":len(a.defined_records),
           "same_repr_exact_records":len(e.defined_records),
           "five_distinct_admitted_full_models_tested":True,
           "value1_value2_cores_remain_distinct":True}
    return {"case":"PA-P20-20260901-FULL-C1-REFERENCE-COMPLETION-AND-REDUCTION-001",
      "locked_pdf_sha256":SOURCE_SHA,
      "checks":checks,"checks_count":len(checks),"all_checks_pass":True,"witness_summary":cases,
      "source_axioms_formalized_for_all_ZFC_sets":False,
      "reference_full_StageVI_model_implemented":False,
      "original_P17_legacy_Python_author_pdf_tex_Zenodo_modified":False,
      "full_property_FPA":"OPEN"}

if __name__=="__main__":
    res=main()
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/"results/p20_full_c1_inverse.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(res,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("P20 FULL C1 INVERSE BOUNDED AUDIT PASS",res["checks_count"])
