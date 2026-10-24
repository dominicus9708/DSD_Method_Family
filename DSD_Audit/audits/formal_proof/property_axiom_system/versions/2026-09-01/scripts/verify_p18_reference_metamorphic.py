#!/usr/bin/env python3
"""P18 independent metamorphic audit of the P17 reference typed validator.

Does not import original Property_Axiom_System src; tests P17 checker itself.
Kwon Dominicus, source paper EN 2026-09-01. Bounded regressions, not ZFC proof.
python verify_p18_reference_metamorphic.py OUTPUT_JSON
"""
from __future__ import annotations
from itertools import product
from pathlib import Path
import json
import sys
import verify_p17_typed_reference_validator as ref

SOURCE="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

def schema():
    return ref.Signature({"h":frozenset({"h0"})},frozenset({"u","v"}),{
      "p":ref.Kind(("u","v"),frozenset({0,1,2}),frozenset({"d1","d2"}),0,True),
      "q":ref.Kind(("v","u"),frozenset({0,1,2}),frozenset(),None,False),
      "r":ref.Kind(("u","u"),frozenset({0,1,2}),frozenset({"d1"})),
      "hkind":ref.Kind(("h","u"),frozenset({0,1,2}),frozenset())},
      frozenset({"d1","d2"}))

def model():
    return ref.Premodel({"u":("a","b"),"v":("v1","v2")},
         ("p","q","r","hkind"),
         {"p":{("a","v1"),("b","v2")},
          "q":{("v1","a"),("v2","b")},
          "r":{("a","a"),("b","a")},
          "hkind":{("h0","a")}},
         {("p","d1"):{("a","v1"),("b","v2")},
          ("p","d2"):{("a","v1")},
          ("r","d1"):{("a","a")}},
         {"p":{("a","v1"):0},
          "q":{("v1","a"):2},
          "r":{("a","a"):1},
          "hkind":{("h0","a"):2}})

def mutate(m, **kw):
    return ref.Premodel(kw.get("aux",dict(m.aux)),kw.get("declared",m.declared),
              kw.get("ap",dict(m.ap)),kw.get("sat",dict(m.sat)),kw.get("xi",dict(m.xi)))

def remap(s,m,swap):
    supply={sort:tuple(swap.get(sort,{}).get(z,z) for z in xs) for sort,xs in m.aux.items()}
    def M(k,x):
        return tuple(swap.get(t,{}).get(z,z) for z,t in zip(x,s.kinds[k].profile))
    return ref.Premodel(supply,m.declared,
       {k:{M(k,x) for x in a} for k,a in m.ap.items()},
       {(k,d):{M(k,x) for x in vals} for (k,d),vals in m.sat.items()},
       {k:{M(k,x):z for x,z in a.items()} for k,a in m.xi.items()})

def audit():
    s=schema();base=model();tests={}
    def ok(name,condition):
        assert condition,name
        tests[name]=True
    def classification(name,mod,expected):
        got=ref.validate(s,mod)["classification"]
        ok(name,got==expected)
    ok("baseline_valid",ref.validate(s,base)["classification"]=="admitted_core")
    bc=ref.completion(s,base)
    ok("baseline_zero_status",bc["p"]["statuses"][repr(("a","v1"))]=="defined-zero")
    ok("baseline_nonzero",bc["r"]["statuses"][repr(("a","a"))]=="defined-value")
    ok("two_prerequisites_intersection_excludes_second",("b","v2") in base.sat["p","d1"]
       and ("b","v2") not in base.sat["p","d2"])
    ok("typed_order_matters",("a","v1") in ref.product(s,base,"p")
       and ("a","v1") not in ref.product(s,base,"q")
       and ("v1","a") in ref.product(s,base,"q"))
    ok("repeated_coordinate_product",len(ref.product(s,base,"r"))==4)
    ok("inherited_coordinate_is_preserved",("h0","a") in ref.product(s,base,"hkind"))
    swap={"u":{"a":"b","b":"a"},"v":{"v1":"v2","v2":"v1"}}
    transported=remap(s,base,swap)
    classification("relabel_is_still_core",transported,"admitted_core")
    after=ref.completion(s,transported)
    for k in base.declared:
        for x,label in bc[k]["statuses"].items():
            # Recover source tuple from repr only through table of all source product inputs.
            x0=next(z for z in ref.product(s,base,k) if repr(z)==x)
            xx=tuple(swap.get(t,{}).get(v,v) for v,t in zip(x0,s.kinds[k].profile))
            ok("relabel_status_"+k+"_"+str(len([t for t in tests if t.startswith("relabel_status_"+k)])),
               after[k]["statuses"][repr(xx)]==label)
    ok("relabel_preserves_kind_domains",all(bc[k]["domain"]==after[k]["domain"] for k in base.declared))
    ok("relabel_preserves_prerequisite_regions",all(bc[k]["prerequisites_met"]==after[k]["prerequisites_met"] for k in base.declared))
    wrong_order=mutate(base,ap={**base.ap,"p":{("v1","a")}})
    classification("misordered_p_product_invalid",wrong_order,"invalid_presentation")
    wrong_arity=mutate(base,ap={**base.ap,"p":{("a",)}})
    classification("wrong_arity_invalid",wrong_arity,"invalid_presentation")
    for name,coordinate in (
        ("missing_ap","ap"),("missing_sat","sat"),("missing_xi","xi")):
        if coordinate=="ap":d=dict(base.ap);del d["p"]
        elif coordinate=="sat":d=dict(base.sat);del d["p","d2"]
        else:d=dict(base.xi);del d["p"]
        classification(name+"_invalid",mutate(base,**{coordinate:d}),"invalid_presentation")
    xi_bad=dict(base.xi);xi_bad["p"]={("a","v1"):999}
    classification("bad_codomain_invalid",mutate(base,xi=xi_bad),"invalid_presentation")
    xi_bad=dict(base.xi);xi_bad["p"]=[(("a","v1"),0),(("a","v1"),1)]
    classification("nonfunctional_graph_invalid",mutate(base,xi=xi_bad),"invalid_presentation")
    xi_bad=dict(base.xi);xi_bad["p"]={("a","v1"):0,("b","v2"):1}
    cm2=mutate(base,xi=xi_bad)
    classification("PII_only_violation_typed_premodel",cm2,"typed_premodel")
    ok("PII_only_violation_pi_true",ref.validate(s,cm2)["pi"] and not ref.validate(s,cm2)["pii"])
    try:ref.completion(s,cm2)
    except ValueError:ok("C1_refuses_PII_premodel",True)
    else:raise AssertionError("C1 should refuse PII premodel")
    ap_bad=dict(base.ap);ap_bad["p"]=set()
    cm1=mutate(base,ap=ap_bad)
    classification("PI_only_violation_typed_premodel",cm1,"typed_premodel")
    ok("PI_only_violation_pii_true",not ref.validate(s,cm1)["pi"] and ref.validate(s,cm1)["pii"])
    try:ref.completion(s,cm1)
    except ValueError:ok("C1_refuses_PI_premodel",True)
    else:raise AssertionError("C1 should refuse PI premodel")
    no_dep=mutate(base,declared=("q",),ap={"q":set(ref.product(s,base,"q"))},
                 sat={},xi={"q":{("v1","a"):2}})
    classification("empty_dependency_set_vacuous",no_dep,"admitted_core")
    ok("empty_dep_completes_full_product",ref.completion(s,no_dep)["q"]["prerequisites_met"]==4)
    # Unlike 'supplied empty', absent carrier leaves no typed product, therefore
    # a declared profile using it has a kind-level unavailable status.
    empty=ref.Premodel({"u":("a",),"v":()},("p",),{"p":set()},
        {("p","d1"):set(),("p","d2"):set()},{"p":{}})
    unavailable=ref.Premodel({"u":("a",)},("p",),{}, {}, {})
    classification("supplied_empty_valid",empty,"admitted_core")
    classification("unavailable_kind_valid",unavailable,"admitted_core")
    ok("no_product_vs_defined_empty",ref.product(s,unavailable,"p") is None
       and ref.product(s,empty,"p")==frozenset())
    ok("C1_kind_level_unavailable",ref.completion(s,unavailable)["p"]["kind_status"]=="profile-unavailable")
    ok("C1_empty_is_available",ref.completion(s,empty)["p"]["kind_status"]=="available")
    extra=mutate(base,ap={**base.ap,"not_declared":{("wrong",)}})
    classification("surplus_ignored",extra,"admitted_core")
    ok("surplus_strict_rejected",ref.validate(s,extra,"reject")["classification"]=="invalid_presentation")
    # Repeated correction itself should not change primitive values: reference
    # completion returns derived coordinates only.
    before=json.dumps({"aux":base.aux,"ap":{p:sorted(list(a)) for p,a in base.ap.items()},
         "xi":{p:sorted(list(a.items())) for p,a in base.xi.items()}},sort_keys=True)
    ref.completion(s,base)
    afterdata=json.dumps({"aux":base.aux,"ap":{p:sorted(list(a)) for p,a in base.ap.items()},
         "xi":{p:sorted(list(a.items())) for p,a in base.xi.items()}},sort_keys=True)
    ok("C1_does_not_mutate_primitives",before==afterdata)
    return {"case":"PA-P18-20260901-DIFFERENTIAL-VALIDATOR-METAMORPHIC-AUDIT-001",
     "locked_pdf_sha256":SOURCE,"number_checks":len(tests),"checks":tests,
     "all_metamorphic_checks_pass":True,
     "general_machine_proof":False,"original_p17_or_legacy_src_modified":False,
     "author_pdf_tex_zenodo_modified":False,"FPA":"OPEN"}

if __name__=="__main__":
    obj=audit()
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/"results/p18_reference_metamorphic.json"
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf8")
    print("P18 METAMORPHIC PASS",obj["number_checks"])
