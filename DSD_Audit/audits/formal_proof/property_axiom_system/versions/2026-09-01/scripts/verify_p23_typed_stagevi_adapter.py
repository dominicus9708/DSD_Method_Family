#!/usr/bin/env python3
"""P23 independent typed finite Formation Stage-VI to Property audit.
This is a restricted finite constructor, not a complete arbitrary Formation
descriptor/strict-isomorphism decision procedure or ZFC formal proof.

Windows (from DSD_Method_Family root):
 python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/scripts/verify_p23_typed_stagevi_adapter.py OUTPUT_JSON
"""
from __future__ import annotations
from dataclasses import dataclass, fields, replace
from itertools import product
from hashlib import sha256
from pathlib import Path
import json, sys

FORM_SHA = "af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe"
PROP_SHA = "03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

class Invalid(ValueError): pass

def require(flag, tag):
    if not flag: raise Invalid(tag)

def unique(xs):
    return len(xs) == len(set(xs))

def mapping(pairs):
    require(unique(tuple(k for k,v in pairs)), "duplicate_mapping_key")
    return dict(pairs)

def canonical(x):
    if hasattr(x, "__dataclass_fields__"):
        return (type(x).__name__,tuple((f.name,canonical(getattr(x,f.name))) for f in fields(x)))
    if isinstance(x, (tuple, list)):
        return tuple(canonical(v) for v in x)
    if isinstance(x, frozenset):
        return ("SET",tuple(sorted((canonical(v) for v in x),key=repr)))
    require(type(x) in (str,int,bool,type(None)), "noncanonical_mutable_or_untyped_element")
    return x

def fingerprint(x):
    return sha256(repr(canonical(x)).encode("utf8")).hexdigest()

@dataclass(frozen=True)
class Material:
    name:str
    typ:str
    support:str
    annotation:str

@dataclass(frozen=True)
class Expression:
    name:str
    material:frozenset[str]
    anchors:tuple[tuple[str,str],...]
    relations:frozenset[tuple[str,str,str]]

@dataclass(frozen=True)
class Configuration:
    name:str
    active:frozenset[str]
    anchors:tuple[tuple[str,str],...]
    relations:frozenset[tuple[str,str,str]]

@dataclass(frozen=True)
class Quantity:
    name:str
    values:frozenset[int]
    zero:int
    assignment:tuple[tuple[str,int],...]

@dataclass(frozen=True)
class FormationInput:
    base:str
    scalar_field:str
    support:frozenset[str]
    material:tuple[Material,...]
    material_relations:frozenset[tuple[str,str,str]]
    expressions:tuple[Expression,...]
    configurations:tuple[Configuration,...]
    admitted_expr:frozenset[str]
    described_expr:frozenset[str]
    restrictions:frozenset[tuple[str,str]]
    realizations:frozenset[tuple[str,str]]
    admitted_cfg:frozenset[str]
    local_coherent:frozenset[str]
    boundary_compatible:frozenset[str]
    quantities:tuple[Quantity,...]
    roles:frozenset[str]
    role_rel:frozenset[tuple[str,str,str,str]]

@dataclass(frozen=True)
class StageVI:
    primitive:FormationInput
    psi:frozenset[str]
    active_describable:frozenset[str]
    assignment_graphs:tuple[tuple[str,tuple[tuple[str,int],...]],...]
    candidate_channels:tuple[tuple[str,str,str,int,str],...]
    channels:tuple[tuple[str,str,str,int,str],...]
    traces:tuple[tuple[tuple[str,str,str,int,str],tuple[tuple[str,str,str,str,str,int,str],...]],...]

def induced(rs, mat):
    return frozenset((r,a,b) for r,a,b in rs if a in mat and b in mat)

def build(f:FormationInput):
    # Finite audited grammar uses canonical str labels and integer value carriers.
    canonical(f)
    require(f.base and f.scalar_field, "missing_fixed_background")
    require(unique(tuple(m.name for m in f.material)), "material_not_a_set")
    mats={m.name:m for m in f.material}
    require(all(m.typ and m.support in f.support for m in f.material), "material_type_support")
    require(all(a in mats and b in mats for _,a,b in f.material_relations), "material_relations_untyped")
    require(unique(tuple(e.name for e in f.expressions)), "expression_not_a_set")
    require(unique(tuple(p.name for p in f.configurations)), "configuration_not_a_set")
    E={e.name:e for e in f.expressions}
    P={p.name:p for p in f.configurations}
    def check_anchors(obj, subset):
        a=mapping(obj.anchors)
        require(set(a)==set(subset), "anchor_domain")
        require(all(a[k]==mats[k].support for k in a), "anchor_source_support")
        require(obj.relations==induced(f.material_relations,subset), "induced_material_relation")
        return a
    for e in f.expressions:
        require(set(e.material)<=set(mats), "expression_material_carrier")
        check_anchors(e,e.material)
    for p in f.configurations:
        require(set(p.active)<=set(mats), "configuration_material_carrier")
        check_anchors(p,p.active)
    require(f.admitted_expr<=set(E) and f.described_expr<=set(E), "expression_predicate_type")
    require(f.described_expr<=f.admitted_expr, "primitive_axiom_I")
    require(f.admitted_cfg<=set(P) and f.local_coherent<=set(P) and f.boundary_compatible<=set(P),
            "configuration_predicate_type")
    require(all(H in E and h in E for H,h in f.restrictions),"restriction_type")
    require(all(h in E and p in P for h,p in f.realizations),"realization_type")
    for H,h in f.restrictions:
        e0,e1=E[H],E[h]
        require(e1.material<=e0.material, "axiom_II_subset")
        require(mapping(e1.anchors)=={a:v for a,v in e0.anchors if a in e1.material}, "axiom_II_anchor")
        require(e1.relations==induced(e0.relations,e1.material), "axiom_II_induced_relation")
        require(h in f.admitted_expr, "axiom_II_target_admission")
    require(all((h,h) in f.restrictions for h in f.admitted_expr),"axiom_II_identity")
    for h,p in f.realizations:
        e,c=E[h],P[p]
        require(c.active<=e.material, "axiom_III_subset")
        require(mapping(c.anchors)=={a:v for a,v in e.anchors if a in c.active}, "axiom_III_anchor")
        require(c.relations==induced(e.relations,c.active), "axiom_III_induced_relation")
    K=frozenset(p for p in P if
        p in f.admitted_cfg and p in f.local_coherent and p in f.boundary_compatible and
        any(h in f.described_expr and (h,p) in f.realizations for H,h in f.restrictions))
    active=frozenset(a for p in K for a in P[p].active)
    require(unique(tuple(q.name for q in f.quantities)), "quantity_not_a_set")
    Q={q.name:q for q in f.quantities}
    graphs={}
    for q in f.quantities:
        require(q.zero in q.values, "pointed_value_zero")
        a=mapping(q.assignment)
        require(set(a)<=set(active), "primitive_axiom_V_domain")
        require(set(a.values())<=set(q.values), "primitive_axiom_V_codomain")
        graphs[q.name]=tuple(sorted(a.items()))
    require(unique(tuple(f.roles)), "role_carrier")
    require(all(p in P and a in mats and l in Q and r in f.roles
                for p,a,l,r in f.role_rel), "role_relation_type")
    U=tuple((p,a,l,v,r) for p,a,l,r in product(sorted(P),sorted(mats),sorted(Q), sorted(f.roles))
            for v in sorted(Q[l].values))
    C=tuple(sorted((p,a,l,v,r) for p,a,l,v,r in U
            if p in K and a in P[p].active and (a,v) in graphs[l] and (p,a,l,r) in f.role_rel))
    tr=[]
    for c in U:
        p,a,l,v,r=c
        witnesses=tuple(sorted((H,h,p,a,l,v,r) for H,h in f.restrictions
            if h in f.described_expr and (h,p) in f.realizations
            and p in f.admitted_cfg and p in f.local_coherent and p in f.boundary_compatible
            and a in P[p].active and (a,v) in graphs[l] and (p,a,l,r) in f.role_rel))
        require((c in C)==bool(witnesses), "theorem_3_6_trace_equivalence")
        tr.append((c,witnesses))
    return StageVI(f,K,active,tuple((l,graphs[l]) for l in sorted(graphs)),U,C,tuple(tr))

def valid_stage(s):
    try: return s==build(s.primitive)
    except (Invalid,TypeError,KeyError): return False

def inherited_carriers(s):
    f=s.primitive
    return tuple(sorted((
        ("material",frozenset(m.name for m in f.material)),
        ("candidate_expression",frozenset(e.name for e in f.expressions)),
        ("candidate_configuration",frozenset(p.name for p in f.configurations)),
        ("describable_configuration",s.psi),
        ("channel",frozenset(s.channels)),
        ("candidate_channel",frozenset(s.candidate_channels)),
        ("quantity_kind",frozenset(q.name for q in f.quantities)),
    )))

@dataclass(frozen=True)
class PropertyKind:
    name:str
    profile:tuple[str,...]
    values:frozenset[int]
    dependencies:frozenset[str]
    zero:int|None=None

@dataclass(frozen=True)
class PropertyInput:
    bound_formation_fingerprint:str
    inherited:tuple[tuple[str,frozenset],...]
    kinds:tuple[PropertyKind,...]
    aux_sorts:frozenset[str]
    aux:tuple[tuple[str,tuple[str,...]],...]
    declared:frozenset[str]
    applicability:tuple[tuple[str,frozenset[tuple]],...]
    satisfied:tuple[tuple[tuple[str,str],frozenset[tuple]],...]
    assignments:tuple[tuple[str,tuple[tuple[tuple,int],...]],...]
    surplus_policy:str="ignore"  # no-required primitive != source-forbidden surplus

def property_baseline(s, empty=False):
    c=s.channels[0] if s.channels else None
    ap=frozenset({(c,"x"),(c,"y")}) if c else frozenset()
    sat=frozenset({(c,"x")}) if c else frozenset()
    assign=(((c,"x"),0),) if c else ()
    return PropertyInput(fingerprint(s.primitive),inherited_carriers(s),
        (PropertyKind("signal",("channel","aux"),frozenset({0,1,2}),frozenset({"d"}),0),
         PropertyKind("unsupplied",("pending",),frozenset({0,1}),frozenset())),frozenset({"aux","pending"}),
        (("aux",("x","y")),) + ((("pending",()),) if empty else ()),
        frozenset({"signal","unsupplied"}),
        (("signal",ap),) + ((("unsupplied",frozenset()),) if empty else ()),
        ((("signal","d"),sat),), (("signal",assign),) + ((("unsupplied",()),) if empty else ()))

def complete(s,p):
    require(valid_stage(s),"invalid_stage_VI_derived_record")
    require(p.bound_formation_fingerprint==fingerprint(s.primitive),"formation_full_record_identity")
    require(p.inherited==inherited_carriers(s),"inherited_carrier_equality")
    ins=dict(p.inherited)
    require(set(ins).isdisjoint(p.aux_sorts),"inherited_aux_sort_collision")
    kinds=mapping(tuple((k.name,k) for k in p.kinds))
    require(p.declared<=set(kinds),"undeclared_unknown_kind")
    aux=mapping(p.aux)
    require(set(aux)<=set(p.aux_sorts) and all(unique(v) for v in aux.values()),"aux_supply")
    ap=mapping(p.applicability)
    sat=mapping(p.satisfied)
    ass=mapping(p.assignments)
    require(p.surplus_policy in ("ignore","reject"),"surplus_policy")
    allowed_ap=set(); allowed_sat=set(); allowed_ass=set()
    states={}
    for k in p.declared:
        kind=kinds[k]
        require(bool(kind.profile) and set(kind.profile)<=set(ins)|set(p.aux_sorts),"typed_profile")
        if kind.zero is not None:
            require(kind.zero in kind.values,"zero_outside_property_values")
        if any(a not in ins and a not in aux for a in kind.profile):
            states[k]="unavailable"
            continue
        X=frozenset(product(*(sorted(ins[a] if a in ins else aux[a],key=repr) for a in kind.profile)))
        allowed_ap.add(k); allowed_ass.add(k)
        for d in kind.dependencies: allowed_sat.add((k,d))
        require(k in ap and k in ass,"primitive_coordinate_required")
        require(ap[k]<=X,"applicability_type")
        for d in kind.dependencies:
            require((k,d) in sat and sat[k,d]<=X,"prerequisite_type")
        xi=mapping(ass[k])
        require(set(xi)<=X and set(xi.values())<=set(kind.values),"assignment_type")
        D=frozenset(xi)
        require(D<=ap[k],"property_axiom_PI")
        prereq=frozenset(X)
        for d in kind.dependencies: prereq=prereq & sat[k,d]
        require(D<=prereq,"property_axiom_PII")
        ss={}
        for x in X:
            if x not in ap[k]: ss[x]="inapplicable"
            elif x not in prereq:ss[x]="prerequisite-unsatisfied"
            elif x not in D:ss[x]="applicable-undefined"
            elif kind.zero is not None:ss[x]="defined-zero" if xi[x]==kind.zero else "defined-nonzero"
            else:ss[x]="defined"
        states[k]=ss
    if p.surplus_policy=="reject":
        require(set(ap)<=allowed_ap and set(ass)<=allowed_ass and set(sat)<=allowed_sat,
                "surplus_primitive_coordinates_rejected_by_declared_policy")
    return states

def compose_after_stageVI(s,terms):
    require(set(terms)==set(s.channels),"stage_VII_term_domain")
    return sum(terms.values())

def formation_fixture():
    relations=frozenset({("incident","a","b")})
    expr=(Expression("H",frozenset({"a","b"}),(("a","sA"),("b","sB")),relations),
          Expression("h",frozenset({"a"}),(("a","sA"),),frozenset()),
          Expression("unused",frozenset({"b"}),(("b","sB"),),frozenset()))
    cfg=(Configuration("p",frozenset({"a"}),(("a","sA"),),frozenset()),
         Configuration("failed",frozenset({"b"}),(("b","sB"),),frozenset()))
    return FormationInput("base","Q",frozenset({"sA","sB"}),
        (Material("a","vertex","sA","blue"),Material("b","edge","sB","blocked")),
        relations,expr,cfg,frozenset({"H","h"}),frozenset({"h"}),
        frozenset({("H","H"),("h","h"),("H","h")}),frozenset({("h","p")}),
        frozenset({"p","failed"}),frozenset({"p","failed"}),frozenset({"p","failed"}),
        (Quantity("heat",frozenset({0,1,2}),0,(("a",0),)),),
        frozenset({"observe"}),frozenset({("p","a","heat","observe"),("p","b","heat","observe")}))

def main():
    checks={}; negative={}
    def check(tag,condition):
        checks[tag]=bool(condition); assert condition,tag
    def rejects(fn):
        try:fn()
        except (Invalid,TypeError,KeyError,ValueError):return True
        return False
    def reject(tag,fn):
        negative[tag]=rejects(fn); assert negative[tag],tag
    f=formation_fixture()
    s=build(f)
    ch=s.channels[0]
    check("full_source_finite_stageVI_record_retained",s.primitive==f)
    check("candidate_expressions_include_failed",len(f.expressions)==3 and "unused" not in f.admitted_expr)
    check("candidate_configurations_include_failed",len(f.configurations)==2 and s.psi==frozenset({"p"}))
    check("axioms_I_II_III_V_source_fixture_admitted",valid_stage(s))
    check("stageVI_five_tuple",len(ch)==5 and ch==("p","a","heat",0,"observe"))
    check("derived_active_material",s.active_describable==frozenset({"a"}))
    check("one_global_assignment_graph_exact",s.assignment_graphs==( ("heat",(("a",0),)), ))
    check("failed_candidate_channel_absent",all(c[0]!="failed" for c in s.channels))
    check("two_witnesses_one_operational_channel",len(dict(s.traces)[ch])==2 and len(s.channels)==1)
    check("trace_history_not_added_to_channel_identity",all(len(t)==7 for t in dict(s.traces)[ch]) and len(ch)==5)
    check("every_derived_channel_has_trace",all(bool(dict(s.traces)[c]) for c in s.channels))
    check("candidate_unadmitted_has_empty_trace",any(not t for c,t in s.traces if c not in s.channels))
    p=property_baseline(s)
    states=complete(s,p)
    check("inherited_carriers_exact_full_record",p.inherited==inherited_carriers(s))
    check("mixed_ordered_profile",p.kinds[0].profile==("channel","aux"))
    check("defined_zero_of_formed_channel",states["signal"][(ch,"x")]=="defined-zero")
    check("dependency_unsatisfied_distinct_from_undefined",states["signal"][(ch,"y")]=="prerequisite-unsatisfied")
    check("unavailable_aux_sort_not_empty",states["unsupplied"]=="unavailable")
    full=property_baseline(s,empty=True)
    statesfull=complete(s,full)
    check("supplied_empty_aux_profile_valid",statesfull["unsupplied"]=={})
    check("unavailable_distinguished_from_available_empty",statesfull["unsupplied"]!=states["unsupplied"])
    surplus=replace(p,applicability=p.applicability+(("unsupplied",frozenset()),))
    check("unavailable_surplus_ignored_when_no_source_prohibition",
          complete(s,surplus)["unsupplied"]=="unavailable")
    reject("unavailable_surplus_policy_reject",
           lambda:complete(s,replace(surplus,surplus_policy="reject")))
    check("stageVII_map_not_stageVI_identity",compose_after_stageVI(s,{ch:4})==4 and compose_after_stageVI(s,{ch:8})==8 and valid_stage(s))
    # Non-describable candidate is still part of full Stage-VI, even if admitted-channel set unchanged.
    f_alt=replace(f,expressions=f.expressions[:-1]+(replace(f.expressions[-1],name="unused2"),))
    s_alt=build(f_alt)
    check("candidate_history_and_failed_objects_preserved",s_alt.channels==s.channels and fingerprint(s_alt.primitive)!=fingerprint(f))
    reject("changed_failed_candidate_requires_rebinding",lambda:complete(s_alt,p))
    f_val=replace(f,quantities=(replace(f.quantities[0],assignment=(("a",2),)),))
    s_val=build(f_val)
    check("new_formation_value_changes_channel",s_val.channels!=s.channels and s_val.channels[0][3]==2)
    reject("changed_value_old_inherited_signature_rejected",lambda:complete(s_val,p))
    check("rebind_on_changed_formation_success",complete(s_val,property_baseline(s_val))["signal"][(s_val.channels[0],"x")]=="defined-zero")
    f_empty=replace(f,quantities=(replace(f.quantities[0],assignment=()),))
    s_empty=build(f_empty)
    check("undefined_assignment_removes_channel_not_creates_zero",len(s_empty.channels)==0)
    check("empty_channel_inherited_carrier_valid",complete(s_empty,property_baseline(s_empty))["signal"]=={})
    f_norole=replace(f,role_rel=frozenset())
    check("missing_role_removes_channel",len(build(f_norole).channels)==0)
    # Reject incorrect stage representations even when their five-tuple records look plausible.
    reject("tampered_derived_channel_injection",lambda:complete(replace(s,channels=(ch,("failed","b","heat",0,"observe"))),p))
    reject("tampered_derived_trace",lambda:complete(replace(s,traces=()),p))
    reject("tampered_derived_describable",lambda:complete(replace(s,psi=frozenset({"p","failed"})),p))
    reject("changed_material_support_old_binding",lambda:complete(build(replace(f,material=(replace(f.material[0],annotation="red"),f.material[1]))),p))
    # Distinct primitive axioms and typing failures.
    reject("primitive_I_description_without_admission",lambda:build(replace(f,described_expr=frozenset({"h","unused"}))))
    reject("primitive_II_missing_identity",lambda:build(replace(f,restrictions=frozenset({("H","H"),("H","h")}))))
    reject("primitive_II_missing_target_admission",lambda:build(replace(f,admitted_expr=frozenset({"H"}),described_expr=frozenset())))
    reject("primitive_II_invalid_subset",lambda:build(replace(f,restrictions=f.restrictions|{("h","H")})))
    reject("primitive_II_bad_anchor",lambda:build(replace(f,expressions=(f.expressions[0],replace(f.expressions[1],anchors=(("a","sB"),)),f.expressions[2]))))
    reject("primitive_III_bad_active_subset",lambda:build(replace(f,realizations=f.realizations|{("h","failed")})))
    reject("material_relations_not_induced",lambda:build(replace(f,expressions=(replace(f.expressions[0],relations=frozenset()),)+f.expressions[1:])))
    reject("primitive_V_domain_outside_active_union",lambda:build(replace(f,quantities=(replace(f.quantities[0],assignment=(("b",0),)),))))
    reject("primitive_V_nonfunctional_assignment",lambda:build(replace(f,quantities=(replace(f.quantities[0],assignment=(("a",0),("a",2))),))))
    reject("primitive_V_value_outside_value_space",lambda:build(replace(f,quantities=(replace(f.quantities[0],assignment=(("a",99),)),))))
    reject("role_relation_wrong_sort",lambda:build(replace(f,role_rel=f.role_rel|{("other","a","heat","observe")})))
    reject("material_support_wrong_type",lambda:build(replace(f,material=(replace(f.material[0],support="missing"),f.material[1]))))
    reject("inherited_carrier_wrong",lambda:complete(s,replace(p,inherited=tuple((k,v) if k!="channel" else (k,frozenset()) for k,v in p.inherited))))
    reject("formation_digest_wrong",lambda:complete(s,replace(p,bound_formation_fingerprint="F6-string-only")))
    reject("mixed_profile_arity_wrong",lambda:complete(s,replace(p,applicability=(("signal",frozenset({("x",)})),))))
    reject("property_PI_broken",lambda:complete(s,replace(p,applicability=(("signal",frozenset()),))))
    reject("property_PII_broken",lambda:complete(s,replace(p,satisfied=((("signal","d"),frozenset()),))))
    reject("property_conflicting_assignment_graph",lambda:complete(s,replace(p,assignments=(("signal",(((ch,"x"),0),((ch,"x"),1))),))))
    reject("stageVII_term_wrong_domain",lambda:compose_after_stageVI(s,{("p","a","heat",99,"observe"):9}))
    check("source_paper_section6_two_gaps_not_claimed_fixed",True)
    check("source_paper_C1_relative_scope_not_claimed_fixed",True)
    require(len(checks)>20 and len(negative)>15,"insufficient_coverage")
    return {"case":"PA-P23-20260901-FORMATION-V45-TYPED-STAGEVI-ADAPTER-001",
        "formation_pdf_sha256":FORM_SHA,"property_pdf_sha256":PROP_SHA,
        "positive_checks":checks,"expected_negative_checks":negative,
        "positive_count":len(checks),"expected_negative_count":len(negative),
        "all_expected_observations_reproduced":all(checks.values()) and all(negative.values()),
        "finite_source_faithful_restricted_constructor":True,
        "full_ZFC_or_arbitrary_StageVI_models_proved":False,
        "full_material_signature_all_relations_exhaustively_modeled":False,
        "D2_57_9_6_directly_reproduced":False,
        "source_section6_two_gaps":"OPEN","source_theorem4_3_C1_scope":"OPEN",
        "original_manuscripts_and_predecessor_scripts_edited":False,
        "full_formation_FPA":"OPEN","full_property_FPA":"OPEN"}

if __name__=="__main__":
    report=main()
    output=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("p23_result.json")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf8")
    print("P23 FINITE OBSERVATIONS:",report["positive_count"],"positive,",report["expected_negative_count"],"negative")
    print("P23 FULL PAPER AUDIT: OPEN")
