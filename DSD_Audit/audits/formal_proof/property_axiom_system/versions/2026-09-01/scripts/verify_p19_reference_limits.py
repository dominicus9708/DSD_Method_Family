#!/usr/bin/env python3
"""P19 independent negative controls of the P17 typed-reference validator.

Outputs reproducible finite audit JSON; does not modify P17, original
Property_Axiom_System/src, the user's PDF, or Zenodo.
Windows (DSD_Method_Family root):
 python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/verify_p19_reference_limits.py OUTPUT_JSON
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import verify_p17_typed_reference_validator as ref

SOURCE_SHA="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

def changed(m, **kv):
    return ref.Premodel(kv.get("aux",dict(m.aux)),kv.get("declared",m.declared),
                        kv.get("ap",dict(m.ap)),kv.get("sat",dict(m.sat)),
                        kv.get("xi",dict(m.xi)))

def observe_validate(s,m):
    try:
        v=ref.validate(s,m)
        return {"outcome":"return","classification":v["classification"],
                "errors":v.get("errors",[])}
    except Exception as e:
        return {"outcome":"exception","exception_class":type(e).__name__}

def audit():
    s=ref.default_sig()
    m=ref.baseline()
    tests={}
    witnesses={}
    def assert_case(name,condition,detail=""):
        assert condition, (name,detail)
        tests[name]=True
    v=observe_validate(s,m)
    assert_case("baseline_core_valid",v["classification"]=="admitted_core",v)
    # These are Python-type/container robustness controls, NOT mathematical
    # ZFC-type counterexamples. A reference checker should ideally reject
    # unknown data with a controlled diagnostic rather than raising.
    unhashable=changed(m,aux={"u":([1],)})
    r=observe_validate(s,unhashable)
    assert_case("unhashable_aux_element_raises",r.get("exception_class")=="TypeError",r)
    witnesses["unhashable_aux_element"]=r

    malformed_decls=changed(m,declared=None)
    r=observe_validate(s,malformed_decls)
    assert_case("none_declarations_raises",r.get("exception_class")=="TypeError",r)
    witnesses["none_declarations"]=r

    for field in ("ap","sat","xi"):
        r=observe_validate(s,changed(m,**{field:None}))
        assert_case("none_"+field+"_raises",r.get("exception_class")=="TypeError",r)
        witnesses["none_"+field]=r

    overlap=ref.Signature({"u":frozenset({"inherited"})},frozenset({"u"}),s.kinds,s.dep_kinds)
    r=observe_validate(overlap,m)
    assert_case("overlap_inherited_aux_rejected",r["classification"]=="invalid_presentation" and
                "sort_overlap" in r["errors"],r)
    s_bad=ref.Signature({"h":("h0",)},s.aux_sorts,s.kinds,s.dep_kinds)
    r=observe_validate(s_bad,m)
    assert_case("nonset_inherited_carrier_rejected",r["classification"]=="invalid_presentation" and
                "inherited_not_set" in r["errors"],r)

    bad_graph=changed(m,xi={"p":[(("x",),0,1)]})
    r=observe_validate(s,bad_graph)
    assert_case("malformed_graph_handled",r["classification"]=="invalid_presentation" and
                "invalid_assignment_graph" in r["errors"],r)

    # Two genuine, distinct admitted cores have different assigned values,
    # while the P17 "completion" function returns only status and counts.
    a=changed(m,xi={"p":{("x",):1}})
    b=changed(m,xi={"p":{("x",):2}})
    va=observe_validate(s,a);vb=observe_validate(s,b)
    ca=ref.completion(s,a);cb=ref.completion(s,b)
    assert_case("distinct_cores_both_admitted",
                va["classification"]=="admitted_core" and vb["classification"]=="admitted_core")
    assert_case("C1_summary_same_for_different_nonzero_values",
                a.xi!=b.xi and ca==cb)
    assert_case("reference_completion_has_no_exact_defined_record_values",
                set(ca["p"])=={"kind_status","domain","prerequisites_met","statuses"} and
                not any(k in ca["p"] for k in ("records","assignments","Xi")))
    witnesses["C1_noninjective_summary"]={
        "primitive_values":[1,2],
        "same_completion_summary":ca==cb,
        "logical_status":"reference completion output not a full CompProp model"
    }

    # Even if the mathematical carrier contains two different hashable objects,
    # using repr(tuple) as a dictionary key can erase one object's status.
    class SameRepr:
        def __repr__(self):
            return "IDENTICAL"
    obj1,obj2=SameRepr(),SameRepr()
    sig=ref.Signature({"h":frozenset({obj1,obj2})},frozenset(),
                      {"p":ref.Kind(("h",),frozenset({0,1}))},frozenset())
    M=ref.Premodel({},("p",),{"p":{(obj1,),(obj2,)}},
                   {},{"p":{(obj1,):0,(obj2,):1}})
    v=observe_validate(sig,M)
    assert_case("distinct_same_repr_elements_well_typed",v["classification"]=="admitted_core",v)
    co=ref.completion(sig,M)
    assert_case("same_repr_status_key_collision",
                len(ref.product(sig,M,"p"))==2 and len(co["p"]["statuses"])==1)
    witnesses["repr_key_collision"]={
        "input_product_cardinality":len(ref.product(sig,M,"p")),
        "status_dictionary_entry_count":len(co["p"]["statuses"])
    }

    # Larger arity and fixed ordered typed profiles: successful positive bound,
    # not an assertion of generalized proof over every schema.
    arity=("h","u","h","u","h")
    sig5=ref.Signature({"h":frozenset({"H0","H1"})},frozenset({"u"}),
        {"p":ref.Kind(arity,frozenset({0,1}),frozenset())},frozenset())
    m5=ref.Premodel({"u":("U0","U1")},("p",),{},
        {},{})
    X=ref.product(sig5,m5,"p")
    m5.ap={"p":set(X)}
    m5.xi={"p":{("H0","U0","H1","U1","H0"):1}}
    v=observe_validate(sig5,m5)
    assert_case("five_coordinates_typed_and_admitted",
                len(X)==32 and v["classification"]=="admitted_core",v)
    co5=ref.completion(sig5,m5)
    assert_case("five_coordinates_all_statuses_counted",len(co5["p"]["statuses"])==32)

    # Conservative source policy: extra metadata may be ignored, or explicitly
    # rejected by a stricter input serialization rule.
    extra=changed(m,ap={"p":{("x",)},"ghost-kind":{("ghost",)}})
    a0=observe_validate(s,extra)
    a1=ref.validate(s,extra,surplus="reject")
    assert_case("surplus_ignore_mode_admits",a0["classification"]=="admitted_core")
    assert_case("surplus_reject_mode_detects",
                a1["classification"]=="invalid_presentation" and
                "surplus_primitive_metadata" in a1["errors"])
    assert_case("surplus_both_modes_distinct",a0["classification"]!=a1["classification"])

    # Primitive carriers remain unchanged by a successful summary completion,
    # but that output is insufficient for the source's CompProp/RedProp inverse.
    original_primitives=(dict(m.aux),m.declared,dict(m.ap),dict(m.sat),dict(m.xi))
    ref.completion(s,m)
    assert_case("completion_does_not_modify_original_primitives",
                original_primitives==(m.aux,m.declared,m.ap,m.sat,m.xi))

    assert len(tests)>=18,tests
    return {
       "case":"PA-P19-20260901-REFERENCE-VALIDATOR-LIMITS-AND-RELEASE-GATE-001",
       "source_pdf_sha256":SOURCE_SHA,
       "expected_observations_count":len(tests),
       "expected_observations":tests,
       "witnesses":witnesses,
       "all_expected_observations_reproduced":all(tests.values()),
       "P17_original_reference_modified":False,
       "P19_negative_input_crashes_mean_source_axiom_false":False,
       "P17_summary_completion_equivalent_to_full_CompProp":False,
       "P17_completion_return_injective_on_primitive_cores":False,
       "global_machine_checked_full_FPA":False,
       "original_manuscript_and_original_experiment_modified":False,
       "full_property_FPA":"OPEN"
    }

if __name__=="__main__":
    r=audit()
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/"results/p19_reference_limits.json"
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("P19 EXPECTED LIMITATION CHECKS PASS",r["expected_observations_count"])
