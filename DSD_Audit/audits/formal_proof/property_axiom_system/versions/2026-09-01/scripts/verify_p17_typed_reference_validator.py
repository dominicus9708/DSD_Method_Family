#!/usr/bin/env python3
"""P17: independent typed-premodel validator + frozen original witness differential.

Kwon Dominicus, General Property Axiom System EN, manuscript 2026-09-01.
Usage: python verify_p17_typed_reference_validator.py OUTPUT.json --original-src PATH_TO_ORIGINAL/src
A run WITHOUT --original-src is explicitly self-tests only, not a completed P17.
"""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PAPER_SHA="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

@dataclass(frozen=True)
class Kind:
    profile: tuple[str,...]
    values: frozenset[Any]
    deps: frozenset[str]=frozenset()
    zero: Any=None
    zero_bearing: bool=False

@dataclass(frozen=True)
class Signature:
    inherited: dict[str,frozenset[Any]]
    aux_sorts: frozenset[str]
    kinds: dict[str,Kind]
    dep_kinds: frozenset[str]

@dataclass
class Premodel:
    aux: dict[str,tuple[Any,...]]
    declared: tuple[str,...]
    ap: dict[str,set[tuple[Any,...]]]
    sat: dict[tuple[str,str],set[tuple[Any,...]]]
    xi: dict[str,Any]

def unique(xs):
    return len(set(xs))==len(xs)

def signature_errors(s):
    e=[]
    if set(s.inherited)&s.aux_sorts:e.append("sort_overlap")
    for v in s.inherited.values():
        if not isinstance(v,frozenset):e.append("inherited_not_set")
    for p,k in s.kinds.items():
        if not k.profile:e.append("empty_profile")
        if any(t not in set(s.inherited)|s.aux_sorts for t in k.profile):e.append("unknown_profile_sort")
        if not k.deps<=s.dep_kinds:e.append("unknown_prerequisite_kind")
        if k.zero_bearing and k.zero not in k.values:e.append("zero_outside_value_carrier")
    return sorted(set(e))

def product(s,m,p):
    """None means unavailable; frozenset() means available EMPTY typed product."""
    cs=[]
    for t in s.kinds[p].profile:
        if t in s.inherited:cs.append(s.inherited[t])
        elif t in m.aux:cs.append(frozenset(m.aux[t]))
        else:return None
    return frozenset(itertools.product(*cs))

def as_function(raw):
    if isinstance(raw,dict):return dict(raw),[]
    v={};e=[]
    for x,z in raw:
        if x in v and v[x]!=z:e.append("nonfunctional_assignment")
        v[x]=z
    return v,e

def validate(s,m,surplus="ignore"):
    if surplus not in ("ignore","reject"):raise ValueError("Surplus policy must be ignore or reject")
    e=signature_errors(s)
    if set(m.aux)-s.aux_sorts:e.append("unknown_aux_sort")
    for v in m.aux.values():
        if not isinstance(v,tuple) or not unique(v):e.append("carrier_not_set_coded")
    if not unique(m.declared):e.append("duplicate_declaration")
    if set(m.declared)-set(s.kinds):e.append("unknown_declared_kind")
    if e:return {"classification":"invalid_presentation","errors":sorted(set(e)),"pi":None,"pii":None}
    typed=[]; allowed_ap=set();allowed_sat=set();allowed_xi=set()
    for p in set(m.declared):
        X=product(s,m,p)
        if X is None:continue
        typed.append((p,X));allowed_ap.add(p);allowed_xi.add(p)
        if p not in m.ap:e.append("missing_applicability")
        if p not in m.xi:e.append("missing_assignment_coordinate")
        for d in s.kinds[p].deps:
            allowed_sat.add((p,d))
            if (p,d) not in m.sat:e.append("missing_prerequisite_coordinate")
        if p in m.ap and any(not isinstance(x,tuple) or x not in X for x in m.ap[p]):
            e.append("applicability_outside_product")
        for d in s.kinds[p].deps:
            if (p,d) in m.sat and any(not isinstance(x,tuple) or x not in X for x in m.sat[p,d]):
                e.append("prerequisite_outside_product")
        if p in m.xi:
            try:
                assignments,err=as_function(m.xi[p]);e+=err
                if any(not isinstance(x,tuple) or x not in X for x in assignments):
                    e.append("assignment_input_outside_product")
                if any(z not in s.kinds[p].values for z in assignments.values()):
                    e.append("assignment_value_outside_carrier")
            except (TypeError,ValueError,KeyError):e.append("invalid_assignment_graph")
    if surplus=="reject" and (set(m.ap)-allowed_ap or set(m.sat)-allowed_sat or set(m.xi)-allowed_xi):
        e.append("surplus_primitive_metadata")
    if e:return {"classification":"invalid_presentation","errors":sorted(set(e)),"pi":None,"pii":None}
    pi=pii=True
    for p,X in typed:
        a,_=as_function(m.xi[p]);D=set(a)
        pi=pi and D<=m.ap[p]
        satisfied=set(X)
        for d in s.kinds[p].deps:satisfied &= m.sat[p,d]
        pii=pii and D<=satisfied
    return {"classification":"admitted_core" if pi and pii else "typed_premodel",
            "errors":[],"pi":pi,"pii":pii}

def completion(s,m):
    if validate(s,m)["classification"]!="admitted_core":
        raise ValueError("C1 applies only to a well-typed PI/PII-sound core")
    out={}
    for p in m.declared:
        X=product(s,m,p)
        if X is None:out[p]={"kind_status":"profile-unavailable"};continue
        xi,_=as_function(m.xi[p]);D=set(xi);dep=set(X)
        for d in s.kinds[p].deps:dep &= m.sat[p,d]
        statuses={}
        for x in X:
            if x not in m.ap[p]:z="inapplicable"
            elif x not in dep:z="prerequisite-unsatisfied"
            elif x not in D:z="applicable-undefined"
            elif s.kinds[p].zero_bearing:z="defined-zero" if xi[x]==s.kinds[p].zero else "defined-nonzero"
            else:z="defined-value"
            statuses[repr(x)]=z
        out[p]={"kind_status":"available","domain":len(D),"prerequisites_met":len(dep),"statuses":statuses}
    return out

def default_sig():
    return Signature({"h":frozenset({"h0","h1"})},frozenset({"u","v"}),{
      "p":Kind(("u",),frozenset({0,1,2}),frozenset({"d"}),0,True),
      "q":Kind(("u","u"),frozenset({0,1,2})),
      "mixed":Kind(("h","u"),frozenset({0,1,2}),frozenset({"d"})),
      "unavailable":Kind(("v",),frozenset({0,1,2}))},frozenset({"d"}))

def baseline():
    return Premodel({"u":("x",)},("p",),{"p":{("x",)}},{("p","d"):{("x",)}},{"p":{("x",):0}})

def changed(m,**kw):
    return Premodel(kw.get("aux",dict(m.aux)),kw.get("declared",m.declared),
       kw.get("ap",dict(m.ap)),kw.get("sat",dict(m.sat)),kw.get("xi",dict(m.xi)))

def self_tests():
    s=default_sig();m=baseline();tests={}
    def expect(name,si,mi,cls="invalid_presentation",err=None,policy="ignore"):
        r=validate(si,mi,policy)
        if r["classification"]!=cls or (err is not None and err not in r["errors"]):
            raise AssertionError((name,r,cls,err))
        tests[name]=cls
    expect("valid",s,m,"admitted_core")
    assert completion(s,m)["p"]["statuses"]["('x',)"]=="defined-zero"
    tests["C1_zero_record"]="admitted_core"
    expect("ghost_application",s,changed(m,ap={"p":{("ghost",)}}),err="applicability_outside_product")
    expect("ghost_prerequisite",s,changed(m,sat={("p","d"):{("ghost",)}}),err="prerequisite_outside_product")
    expect("wrong_tuple_arity",s,changed(m,ap={"p":{("x","x")}}),err="applicability_outside_product")
    expect("out_of_domain_assignment",s,changed(m,xi={"p":{("ghost",):0}}),err="assignment_input_outside_product")
    expect("out_of_value_carrier",s,changed(m,xi={"p":{("x",):99}}),err="assignment_value_outside_carrier")
    expect("nonfunctional_graph",s,changed(m,xi={"p":[(("x",),0),(("x",),1)]}),err="nonfunctional_assignment")
    expect("missing_application",s,changed(m,ap={}),err="missing_applicability")
    expect("missing_prerequisite",s,changed(m,sat={}),err="missing_prerequisite_coordinate")
    expect("missing_assignment",s,changed(m,xi={}),err="missing_assignment_coordinate")
    expect("unknown_kind",s,changed(m,declared=("p","unknown")),err="unknown_declared_kind")
    expect("unknown_aux_sort",s,changed(m,aux={"u":("x",),"rogue":("z",)}),err="unknown_aux_sort")
    expect("duplicate_carrier_presentation",s,changed(m,aux={"u":("x","x")}),err="carrier_not_set_coded")
    expect("duplicate_declared_label",s,changed(m,declared=("p","p")),err="duplicate_declaration")
    for name,k,err in [
        ("empty_profile",Kind((),frozenset({0,1})),"empty_profile"),
        ("unknown_profile",Kind(("alien",),frozenset({0,1})),"unknown_profile_sort"),
        ("bad_prerequisite_kind",Kind(("u",),frozenset({0,1}),frozenset({"alien"})),"unknown_prerequisite_kind"),
        ("zero_outside_carrier",Kind(("u",),frozenset({1,2}),frozenset({"d"}),0,True),"zero_outside_value_carrier")]:
        ss=Signature(s.inherited,s.aux_sorts,{**s.kinds,"p":k},s.dep_kinds)
        expect(name,ss,m,err=err)
    cm1=changed(m,ap={"p":set()})
    cm2=changed(m,sat={("p","d"):set()})
    expect("typed_CM_PI_failure",s,cm1,"typed_premodel")
    expect("typed_CM_PII_failure",s,cm2,"typed_premodel")
    for name,cm in [("no_C1_for_CM_PI",cm1),("no_C1_for_CM_PII",cm2)]:
        try:completion(s,cm)
        except ValueError:tests[name]="expected_refusal"
        else:raise AssertionError(name)
    empty=changed(m,aux={"u":()},ap={"p":set()},sat={("p","d"):set()},xi={"p":{}})
    missing=changed(m,aux={},ap={},sat={},xi={})
    expect("supplied_empty_product",s,empty,"admitted_core")
    expect("unavailable_profile",s,missing,"admitted_core")
    assert product(s,empty,"p")==frozenset() and product(s,missing,"p") is None
    tests["unavailable_vs_empty"]="distinguished"
    inherited=changed(m,declared=("mixed",),ap={"mixed":{("h0","x")}},
                      sat={("mixed","d"):{("h0","x")}},xi={"mixed":{("h0","x"):2}})
    expect("inherited_mixed_sort",s,inherited,"admitted_core")
    repeated=changed(m,declared=("q",),ap={"q":{("x","x")}},
                      sat={},xi={"q":{("x","x"):1}})
    expect("repeated_sort",s,repeated,"admitted_core")
    surplus=changed(m,ap={"p":{("x",)},"q":{("x","x")}})
    expect("surplus_ignore",s,surplus,"admitted_core")
    expect("surplus_reject",s,surplus,"invalid_presentation","surplus_primitive_metadata","reject")
    return tests

def import_original(src):
    p=Path(src)/"property_axiom_reproduction.py"
    if not p.exists():raise FileNotFoundError(p)
    spec=importlib.util.spec_from_file_location("property_axiom_original_p17",p)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module

def differential(original):
    # EIGHT constructor functions: 4 single models, 3 pairs, 1 triple = 13 models.
    f=[("CM4.1",original.construct_pi_countermodel()),
       ("CM4.2",original.construct_pii_countermodel()),
       ("one_input",original.construct_one_input_model()),
       ("status",original.construct_status_witness())]
    for name,group in [
        ("stage2",original.construct_stage2_branch()),
        ("stage3",original.construct_stage3_branch()),
        ("stage4",original.construct_stage4_branch()),
        ("forward_chain",original.construct_forward_map_chain()[:3])]:
        for i,v in enumerate(group):f.append((name+"_"+str(i),v))
    assert len(f)==13
    findings={}
    for name,o in f:
        kinds={p:Kind(tuple(q.profile),frozenset({0,1,2}),frozenset(q.prerequisites),
                      q.zero,q.zero_bearing) for p,q in o.signature.items()}
        aux=frozenset(t for k in kinds.values() for t in k.profile)
        dep=frozenset(d for k in kinds.values() for d in k.deps)
        sig=Signature({},aux,kinds,dep)
        model=Premodel(dict(o.auxiliary_carriers),tuple(o.declarations),
                       dict(o.applicability),dict(o.prerequisite_satisfaction),dict(o.assignments))
        v=validate(sig,model)
        intended="typed_premodel" if name.startswith("CM4.") else "admitted_core"
        if v["classification"]!=intended:raise AssertionError((name,v,intended))
        if intended=="admitted_core":completion(sig,model)
        findings[name]=v["classification"]
    return findings

def run(original_src):
    own=self_tests()
    x=differential(import_original(original_src)) if original_src else None
    return {"case":"PA-P17-20260901-INDEPENDENT-TYPED-REFERENCE-VALIDATOR-001",
     "source_pdf_sha256":PAPER_SHA,"self_tests_count":len(own),"self_tests":own,
     "differential_executed":bool(original_src),
     "original_constructor_functions":8 if x else None,
     "original_concrete_models_checked":len(x) if x else 0,
     "original_differential":x,
     "surplus_metadata_policies":["ignore","reject"],
     "machine_proved_universal_property_axioms":False,
     "author_pdf_tex_zenodo_or_original_code_modified":False,"FPA":"OPEN"}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("output",nargs="?")
    p.add_argument("--original-src",default=None)
    a=p.parse_args()
    r=run(a.original_src)
    out=Path(a.output) if a.output else Path(__file__).resolve().parent.parent/"results/p17_typed_reference_validator.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print("P17 REFERENCE VALIDATOR",r["self_tests_count"],"self tests;",
          r["original_concrete_models_checked"],"actual original models")
