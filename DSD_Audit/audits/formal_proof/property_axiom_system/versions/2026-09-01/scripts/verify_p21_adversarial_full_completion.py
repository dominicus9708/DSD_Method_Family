#!/usr/bin/env python3
"""P21 non-edit adversarial tests of frozen P20 full C1 reference, not paper proof."""
import json,sys
from pathlib import Path
from dataclasses import replace
import verify_p20_full_c1_inverse as p20
import verify_p17_typed_reference_validator as ref

checks={}
evidence={}
def test(name,fn):
    try:
        r=fn()
        checks[name]=bool(r)
        assert checks[name],name
    except Exception:
        raise

def raises(error,fn):
    try:fn()
    except error:return True
    return False

a=p20.comp_prop(p20.make_model())
test("baseline_full_valid",lambda:p20.full_is_valid(a))
test("baseline_roundtrip",lambda:p20.red_prop(a)==a.primitive)
test("same_value_duplicate_graph_typed",lambda:ref.validate(p20.kinds_baseline(),ref.Premodel({"u":("x",)},("p",),{"p":{("x",)}},{("p","d1"):{("x",)},("p","d2"):{("x",)}},{"p":[(("x",),1),(("x",),1)]}))["classification"]=="admitted_core")
duplicate=p20.make_model()
duplicate.prem.xi["p"]=[(("x",),1),(("x",),1)]
test("same_value_graph_comp_preserves_semantic_assignment",lambda:p20.comp_prop(duplicate).defined_records==a.defined_records)
test("same_value_graph_roundtrip_not_presentation_equal",lambda:p20.red_prop(p20.comp_prop(duplicate))!=duplicate)
evidence["duplicate_graph"]="P20 canonicalizes iterable assignment graph to dict: extensional content retained, raw presentation not identical."
bad=p20.make_model()
bad.prem.xi["p"]=[(("x",),1),(("x",),2)]
test("conflicting_graph_refused",lambda:raises(ValueError,lambda:p20.comp_prop(bad)))
original=p20.make_model()
full=p20.comp_prop(original)
original.prem.xi["p"][("x",)]=2
test("source_mutation_isolated_from_full",lambda:full.primitive.prem.xi["p"][("x",)]==1)
test("source_mutation_full_still_valid",lambda:p20.full_is_valid(full))
test("source_mutation_changes_future_completion",lambda:p20.comp_prop(original)!=full)
full2=p20.comp_prop(p20.make_model())
full2.primitive.prem.xi["p"][("x",)]=2
test("nested_frozen_dataclass_not_immutable",lambda:full2.primitive.prem.xi["p"][("x",)]==2)
test("nested_primitive_mutation_invalidates_derived_full",lambda:not p20.full_is_valid(full2))
test("reduction_rejects_mutated_nested_primitive",lambda:raises(ValueError,lambda:p20.red_prop(full2)))
# External alias of mutable typed carrier object is not deep-copied: confirmed limitation.
class MutableValue:
    def __init__(self):self.payload=1
    def __hash__(self):return id(self)
    def __eq__(self,other):return self is other
    def __repr__(self):return "mutable-typed-input"
m=MutableValue()
s=ref.Signature({"h":frozenset({m})},frozenset(),{"p":ref.Kind(("h",),frozenset({0,1}))},frozenset())
model=ref.Premodel({},("p",),{"p":{(m,)}},{},{"p":{(m,):1}})
q=p20.Primitive("StageVI-anchor",s,model)
com=p20.comp_prop(q)
m.payload=99
test("mutable_element_alias_retained",lambda:next(iter(com.primitive.signature.inherited["h"])) is m and m.payload==99)
test("mutable_element_full_still_valid",lambda:p20.full_is_valid(com))
evidence["mutable_element"]="Completion snapshots container maps, not deep immutable copies of hashable mutable typed carrier elements."
# Shared mutable signature dictionary is likewise aliased.
sig=dict(com.primitive.signature.kinds)
test("signature_is_mapping_not_frozen",lambda:isinstance(com.primitive.signature.kinds,dict))
# Corrupt each independent derived object coordinate.
for field,replacement in [
 ("domains",{}),("dep_satisfied",{}),("status",{}),
 ("unavailable_kinds",frozenset()),("defined_records",frozenset())]:
 baseline=p20.comp_prop(p20.make_model())
 tampered=replace(baseline,**{field:replacement})
 # unavailable set frozenset() differs from source baseline
 test("tamper_"+field+"_invalid",lambda tampered=tampered:not p20.full_is_valid(tampered))
 test("tamper_"+field+"_cannot_reduce",lambda tampered=tampered:raises(ValueError,lambda:p20.red_prop(tampered)))
# Metadata policies.
ign=p20.make_model(policy="ignore")
ign.prem.ap["undeclared"]={("surplus",)}
c=p20.comp_prop(ign)
test("ignored_surplus_preserved",lambda:p20.red_prop(c).prem.ap["undeclared"]=={("surplus",)})
rej=p20.make_model(policy="reject")
rej.prem.ap["undeclared"]={("surplus",)}
test("rejected_surplus_fails",lambda:raises(ValueError,lambda:p20.comp_prop(rej)))
# Explicit Python NaN does not have ordinary reflexive set-element equality.
n=float("nan")
test("nan_nonreflexive",lambda:n!=n)
evidence["nan"]="NaN is not a safe substitute for an ordinary source value-carrier element with mathematical equality."
# Stage VI is only a string marker, not a validated Formation object.
test("stageVI_anchor_plain_string",lambda:isinstance(a.primitive.stage_vi_anchor,str))
evidence["stageVI"]="This model stores an anchor string and does not validate a complete inherited Formation Stage-VI descriptor."
# malformed serialization that leads to uncaught TypeError in legacy typed checker
mal=p20.make_model()
mal.prem.aux["u"]=([1],)
test("nonhashable_carrier_causes_TypeError",lambda:raises(TypeError,lambda:p20.comp_prop(mal)))
evidence["malformed_input"]="P20 inherited P17's incomplete defensive input validation."
out={"case":"PA-P21-20260901-FULL-COMPLETION-ADVERSARIAL-SERIALIZATION-001",
"source_pdf_sha256":"03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c",
"checks_count":len(checks),"checks":checks,"all_expected_observations_reproduced":all(checks.values()),
"evidence":evidence,"original_P20_or_other_Python_edited":False,"source_Theorem_3_7_disproved":False,"full_property_FPA":"OPEN"}
dest=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/"results/p21_full_completion_adversarial.json"
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
print("P21 EXPECTED OBSERVATIONS PASS",len(checks))
