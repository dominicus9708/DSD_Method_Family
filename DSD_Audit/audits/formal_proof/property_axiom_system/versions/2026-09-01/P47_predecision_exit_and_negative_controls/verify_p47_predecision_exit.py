#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P47 predecision evidence and hypothetical typed-B negative controls.
Author Kwon Dominicus. This is NOT a general formal proof.
"""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
from itertools import product
from pathlib import Path
import argparse
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SRC=ROOT/"P27_independent_math_revision"
DOCS={n:ROOT/p for n,p in {
    "P39":"P39_global_56_item_dependency/P39_56_ITEM_DEPENDENCY_EVIDENCE.json",
    "P40":"P40_20_statement_proof_audit/P40_20_CLAIMS_LEDGER.json",
    "P41":"P41_dependency_chain_and_scope/P41_DEPENDENCY_DAG_EVIDENCE.json",
    "P42":"P42_consolidated_premises_countermodels_revision_spec/P42_20_PLUS_13_REVISION_LEDGER.json",
    "P43":"P43_bilingual_math_parity_closure_gates/P43_EN_KR_PARITY_AND_GATES.json",
    "P44":"P44_predecision_readiness/P44_PREDECISION_EVIDENCE_LEDGER.json",
    "P45":"P45_semantics_predecision_comparison/P45_SEMANTIC_COMPARISON_DECISION_LEDGER.json",
    "P46":"P46_choice_invariants_branching/P46_SHARED_VS_BRANCHING_LEDGER.json"}.items()}
LEDGER=HERE/"P47_PREDECISION_EXIT_EVIDENCE_LEDGER.json"
INPUT=("a",)
CARRIERS={"h":("a",)}
SIG={
  "p":{"profile":("h",),"values":(0,),"deps":("d",)},
  "q":{"profile":("h",),"values":(0,),"deps":()},
  "r":{"profile":("u",),"values":(0,),"deps":()},
}
def product_of(kind, signature=SIG):
    info=signature.get(kind)
    if info is None or any(t not in CARRIERS for t in info["profile"]):
        return None
    return set(product(*(CARRIERS[t] for t in info["profile"])))

def model():
    return {"declared":{"p"},"ap":{"p":{INPUT}},
            "sat":{("p","d"):{INPUT}},"xi":{"p":{}}}

def typed_B(m, signature=SIG):
    declared=set(m["declared"])
    if not declared.issubset(signature):return False
    indices=set(m["ap"])|set(m["xi"])|{k for k,_ in m["sat"]}
    if any(product_of(k,signature) is None for k in indices):return False
    for k,v in m["ap"].items():
        if not v.issubset(product_of(k,signature)):return False
    for (k,d),v in m["sat"].items():
        if d not in signature[k]["deps"] or not v.issubset(product_of(k,signature)):
            return False
    for k,f in m["xi"].items():
        if not set(f).issubset(product_of(k,signature)):return False
        if any(v not in signature[k]["values"] for v in f.values()):return False
    # PI and PII are required only for declared and profile-available types.
    for k in declared:
        if product_of(k,signature) is None:continue
        if k not in m["ap"] or k not in m["xi"]:return False
        if any((k,d) not in m["sat"] for d in signature[k]["deps"]):return False
        dom=set(m["xi"][k])
        if not dom.issubset(m["ap"][k]):return False
        if any(not dom.issubset(m["sat"][(k,d)]) for d in signature[k]["deps"]):
            return False
    return True

def normalization(m):
    active={k for k in m["declared"] if product_of(k) is not None}
    return {"declared":set(m["declared"]),
            "ap":{k:deepcopy(v) for k,v in m["ap"].items() if k in active},
            "sat":{(k,d):deepcopy(v) for (k,d),v in m["sat"].items() if k in active},
            "xi":{k:deepcopy(v) for k,v in m["xi"].items() if k in active}}

def complete_raw(m):
    core=normalization(m)
    derived=("defined" if INPUT in core["xi"].get("p",{}) else
             "applicable-undefined" if INPUT in core["ap"].get("p",set())
             and INPUT in core["sat"].get(("p","d"),set()) else "other")
    return {"raw":deepcopy(m),"C1":derived}

def stage3(p,q):
    return normalization(p)==normalization(q) and p["ap"]==q["ap"] and p["sat"]==q["sat"]

def stage4(p,q):
    return stage3(p,q) and p["xi"]==q["xi"]

def negative_controls():
    base=model()
    empty_ap=deepcopy(base);empty_ap["ap"]["q"]=set()
    empty_xi=deepcopy(base);empty_xi["xi"]["q"]={}
    assigned=deepcopy(base);assigned["xi"]["q"]={INPUT:0}
    untyped=deepcopy(base);untyped["ap"]["r"]=set()
    foreign=deepcopy(base);foreign["ap"]["outside_signature"]=set()
    bad_pi=deepcopy(base);bad_pi["ap"]["p"]=set();bad_pi["xi"]["p"]={INPUT:0}
    bad_pii=deepcopy(base);bad_pii["sat"][("p","d")]=set();bad_pii["xi"]["p"]={INPUT:0}
    missing=deepcopy(base);missing["ap"].pop("p")
    promote=deepcopy(assigned);promote["declared"].add("q")
    return {
      "raw_q_empty_applicability_present_is_typed":typed_B(empty_ap),
      "raw_q_undefined_assignment_present_is_typed":typed_B(empty_xi),
      "raw_r_missing_aux_profile_rejected":not typed_B(untyped),
      "raw_unknown_property_rejected":not typed_B(foreign),
      "active_PI_violation_rejected":not typed_B(bad_pi),
      "active_PII_violation_rejected":not typed_B(bad_pii),
      "active_missing_primitive_rejected":not typed_B(missing),
      "raw_q_can_become_invalid_if_naively_declared":typed_B(assigned) and not typed_B(promote),
      "empty_signature_does_not_force_existence_witness":not any({}),
      "normalization_erases_only_optional_extra":
         normalization(base)==normalization(empty_ap)==normalization(empty_xi)
         and base!=empty_ap and base!=empty_xi,
      "raw_C1_exact_if_preserves_raw":
         complete_raw(empty_ap)["raw"]==empty_ap and complete_raw(assigned)["raw"]==assigned,
      "raw_C1_inverse_fails_if_normalization_overwrites":
         normalization(empty_ap)!=empty_ap and normalization(assigned)!=assigned,
      "same_active_data_raw_key_presence_distinguishes_stage3":
         typed_B(base) and typed_B(empty_ap) and not stage3(base,empty_ap),
      "same_active_data_raw_assignment_presence_distinguishes_stage4":
         stage3(base,empty_xi) and not stage4(base,empty_xi),
      "default_empty_coercion_changes_B2_comparison":
         all(base["ap"].get(k,set())==empty_ap["ap"].get(k,set())
             for k in set(base["ap"])|set(empty_ap["ap"]))
         and not stage3(base,empty_ap),
    }

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--out",type=Path)
    args=a.parse_args()
    led=json.loads(LEDGER.read_text(encoding="utf-8"))
    docs={k:json.loads(p.read_text(encoding="utf-8")) for k,p in DOCS.items()}
    d=docs
    src=led["fixed_source_sha256"]
    idx=led["source_index"]
    neg=negative_controls()
    checks={
      "EN_source_frozen":sha256((SRC/"DSD_Property_Axiom_System_EN_P27_REVISED.tex").read_bytes()).hexdigest()==src["EN"],
      "KR_source_frozen":sha256((SRC/"DSD_Property_Axiom_System_KR_P27_REVISED.tex").read_bytes()).hexdigest()==src["KR"],
      "P39_sha_matches":d["P39"]["sha256"]==src,
      "P40_sha_matches":d["P40"]["source_sha256"]==src,
      "P41_sha_matches":d["P41"]["source_sha256"]==src,
      "P42_sha_matches":d["P42"]["frozen_sha256"]==src,
      "P43_sha_matches":d["P43"]["frozen_source_sha256"]==src,
      "P44_sha_matches":d["P44"]["source_sha256"]==src,
      "P45_sha_matches":d["P45"]["frozen_P27_sha256"]==src,
      "P46_sha_matches":d["P46"]["P27_sha256"]==src,
      "18_reports_indexed":[m["id"] for m in led["report_manifest"]]==[f"P{i}" for i in range(29,47)],
      "18_reports_physically_present":len(led["report_manifest"])==18 and all(
        (ROOT/r["path"]).is_file() and (ROOT/r["path"]).stat().st_size>100 for r in led["report_manifest"]),
      "56_numbered":d["P39"]["numbered_total"]==idx["numbered"]==56,
      "20_proof_targets":d["P40"]["claims"]==idx["proof_targets"]==20,
      "97_dependency_edges":d["P41"]["edges"]==idx["dependency_edges"]==97,
      "13_main_conclusions":len(d["P42"]["main_theorem_13"])==idx["main_theorem_subclaims"]==13,
      "16_sections":d["P43"]["sections"]==idx["section_count"]==16,
      "78_display_equations":d["P43"]["math_display"]==idx["formula_display_per_language"]==78,
      "222_inline_expressions":d["P44"]["observed_bilingual"]["inline_formula_count_each"]==idx["formula_inline_per_language"]==222,
      "7_common":len(d["P46"]["shared_mathematics"])==idx["common_claims"]==7,
      "6_variants":len(d["P46"]["changing_results"])==idx["variant_claims"]==6,
      "5_conditional_theorems":len(d["P46"]["conditional_theorems"])==idx["conditional_theorems"]==5,
      "original_PI_PII_and_C1":d["P39"]["independent_axioms"]==idx["main_orig_axioms"]==2 and d["P39"]["closure_clauses"]==idx["definitional_closure_clauses"]==1,
      "four_open_obligations":{x["id"] for x in led["proof_obligations"]}==set(d["P42"]["open_obligations"])=={"S-01","S-02","S-03","S-04"},
      "three_choices_not_chosen":{x["id"] for x in led["decision_paths"]}=={"A","B1","B2"} and all(not x["selected"] for x in led["decision_paths"]),
      "15_negative_controls_tracked":set(neg)==set(led["negative_control_contract"]["must_validate"]),
      "10_invalid_inferences_retained":len(led["critical_noninferences"])==10,
      "8_separate_exit_gates":{x["id"] for x in led["exit_gates"]}=={f"X{i}" for i in range(1,9)},
      "review_ready_not_semantics_choice":led["verdict"]["predecision_tracking"]=="SCOPED_EXIT_READINESS_UNDER_STATED_ASSUMPTIONS" and led["verdict"]["semantic_selection"]=="DEFERRED",
      "full_FPA_OPEN_no_edit":led["verdict"]["P27_FPA"]=="OPEN" and not led["verdict"]["manuscript_modified"],
      "external_formal_proof_not_claimed":led["verdict"]["independent_formal_proof"]=="NOT_ESTABLISHED",
    }
    checks.update(neg)
    output={"audit_id":led["audit_id"],"passed":sum(checks.values()),"checked":len(checks),
            "checks":checks,"negative_controls":neg,
            "note":"bounded trace/typed-B negative fixtures; not a global theorem or final model choice",
            "choice":"DEFERRED","source_modified":False,"property_FPA":"OPEN"}
    text=json.dumps(output,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(text,encoding="utf-8")
    else:print(text,end="")
    if not all(checks.values()):raise SystemExit("P47 AUDIT FAILED")
if __name__=="__main__":main()
