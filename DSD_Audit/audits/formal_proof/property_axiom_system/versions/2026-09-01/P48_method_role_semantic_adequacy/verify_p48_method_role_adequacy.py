#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P48 role adequacy vs PAS semantics. Author: Kwon Dominicus.
Finite audit model ONLY, not an empirical study or full theorem formalization.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
EN=ROOT/"P27_independent_math_revision"/"DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR=ROOT/"P27_independent_math_revision"/"DSD_Property_Axiom_System_KR_P27_REVISED.tex"
P47=ROOT/"P47_predecision_exit_and_negative_controls"/"P47_PREDECISION_EXIT_EVIDENCE_LEDGER.json"
P46=ROOT/"P46_choice_invariants_branching"/"P46_SHARED_VS_BRANCHING_LEDGER.json"
P45=ROOT/"P45_semantics_predecision_comparison"/"P45_SEMANTIC_COMPARISON_DECISION_LEDGER.json"
LEDGER=HERE/"P48_ROLE_FIT_EVIDENCE_LEDGER.json"
INPUT=("a",)
CANDIDATES={
    "p":{"profile":("h",),"values":(0,),"deps":("d",)},
    "q":{"profile":("h",),"values":(0,),"deps":()},
    "r":{"profile":("u",),"values":(0,),"deps":()},
}
CARRIERS={"h":{INPUT[0]}}

def product_available(kind: str) -> bool:
    info=CANDIDATES.get(kind)
    return bool(info is not None and all(t in CARRIERS for t in info["profile"]))

def basic_model():
    return {"declared":{"p"},"ap":{"p":{INPUT}},"sat":{("p","d"):{INPUT}},"xi":{"p":{}}}

def normalize(model):
    active={k for k in model["declared"] if product_available(k)}
    return {"declared":set(model["declared"]),
            "ap":{k:deepcopy(v) for k,v in model["ap"].items() if k in active},
            "sat":{(k,d):deepcopy(v) for (k,d),v in model["sat"].items() if k in active},
            "xi":{k:deepcopy(v) for k,v in model["xi"].items() if k in active}}

def active_status(model):
    z=normalize(model)
    if INPUT not in z["ap"].get("p",set()): return "inapplicable"
    if INPUT not in z["sat"].get(("p","d"),set()): return "unsatisfied"
    if INPUT not in z["xi"].get("p",{}): return "applicable_undefined"
    return "defined"

def type_check(model):
    for kind in (set(model["ap"])|set(model["xi"])|
                 {k for (k,_) in model["sat"]}):
        if not product_available(kind):return False
    for kind in model["declared"]:
        if not product_available(kind):continue
        if kind not in model["ap"] or kind not in model["xi"]:return False
        for d in CANDIDATES[kind]["deps"]:
            if (kind,d) not in model["sat"]:return False
        dom=set(model["xi"][kind])
        if not dom.issubset(model["ap"][kind]):return False
        if any(not dom.issubset(model["sat"][(kind,d)]) for d in CANDIDATES[kind]["deps"]):return False
    return True

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path)
    args=p.parse_args()
    led=json.loads(LEDGER.read_text(encoding="utf-8"))
    v47=json.loads(P47.read_text(encoding="utf-8"))
    v46=json.loads(P46.read_text(encoding="utf-8"))
    v45=json.loads(P45.read_text(encoding="utf-8"))
    P=basic_model()
    Q=deepcopy(P)
    Q["ap"]["q"]=set()
    R=deepcopy(P)
    R["xi"]["q"]={}
    invalid=deepcopy(P)
    invalid["ap"]["r"]=set()
    promoted=deepcopy(Q)
    promoted["declared"].add("q")
    # A separate evidence ledger may differ without modifying the raw PAS P.
    sources=("record-source-A","record-source-B")
    same_core=normalize(P)==normalize(Q)
    different_raw=P!=Q
    # Typed index-preserving B2 compares presence, rather than defaulting absent to empty.
    raw_stage3_equal=P["ap"]==Q["ap"] and P["sat"]==Q["sat"]
    default_empty_equal=all(P["ap"].get(key,set())==Q["ap"].get(key,set())
                            for key in set(P["ap"])|set(Q["ap"]))
    first_observer=active_status(P)
    second_observer=active_status(Q)
    # Two raw models in the same N fiber are undistinguishable by any Tbar(N(.)).
    tests={
      "frozen_EN_sha256":sha256(EN.read_bytes()).hexdigest()==led["frozen_P27_sha256"]["EN"],
      "frozen_KR_sha256":sha256(KR.read_bytes()).hexdigest()==led["frozen_P27_sha256"]["KR"],
      "P47_sha256_agrees":v47["fixed_source_sha256"]==led["frozen_P27_sha256"],
      "P46_sha256_agrees":v46["P27_sha256"]==led["frozen_P27_sha256"],
      "P45_sha256_agrees":v45["frozen_P27_sha256"]==led["frozen_P27_sha256"],
      "method_source_roles_five":len(led["method_needs"])==5,
      "source_provenance_contains_primary_and_methods":len(led["source_provenance"])>=10 and
          {x["id"] for x in led["source_provenance"]}>={"P27","P47","METHODS","SPEC","DESIGN","AUDIT"},
      "role_comparison_not_implied_raw_required":all(
          x["raw_requirement"]!="PAS_RAW_ALWAYS_REQUIRED" for x in led["method_needs"]),
      "three_alternatives_unchosen":{x["id"] for x in led["semantic_options"]}=={"A","B1","B2"} and
          all(not x["selected"] for x in led["semantic_options"]),
      "five_conditional_claims":len(led["conditional_math"])==5 and
          {x["id"] for x in led["conditional_math"]}=={f"M48-{i}" for i in range(1,6)},
      "conditional_claims_have_proof_and_scope":all(x["proof"] and x["preconditions"] for x in led["conditional_math"]),
      "six_unsettled_decision_boundaries":len(led["decision_boundaries"])==6 and
          {x["id"] for x in led["decision_boundaries"]}=={f"Q{i}" for i in range(1,7)},
      "P_is_valid_typed":type_check(P),
      "Q_is_valid_hypothetical_typed_B":type_check(Q),
      "raw_profile_unavailable_rejected":not type_check(invalid),
      "same_active_normalization":same_core,
      "different_raw_presentations":different_raw,
      "raw_key_exists_only_in_Q":"q" not in P["ap"] and "q" in Q["ap"],
      "raw_B2_index_sensitive_stage3_distinguishes":not raw_stage3_equal,
      "implicit_empty_coercion_changes_raw_result":default_empty_equal,
      "active_strict_sees_same_active_core":same_core,
      "active_status_undefined_both":first_observer==second_observer=="applicable_undefined",
      "raw_presence_observer_different":("q" in P["ap"])!=("q" in Q["ap"]),
      "raw_assignment_index_can_differ_without_active_change":
          normalize(P)==normalize(R) and P["xi"]!=R["xi"],
      "two_evidence_sources_distinct":sources[0]!=sources[1],
      "same_raw_does_not_determine_independent_source":
          P==deepcopy(P) and sources[0]!=sources[1],
      "naive_activation_of_Q_rejected":type_check(Q) and not type_check(promoted),
      "static_model_has_no_activation_operator":led["decision_boundaries"][4]["state"]=="NOT_DERIVED_FROM_STATIC_P27",
      "source_edit_not_authorized":led["verdict"]["P27_source_modified"] is False,
      "choice_deferred_and_fpa_open":led["verdict"]["selection"]=="DEFERRED" and led["verdict"]["FPA"]=="OPEN",
      "external_practical_validation_not_claimed":"not been measured" in led["verdict"]["claim_limit"],
    }
    expected=led["finite_fixture"]["expected"]
    observations={
      "same_active_normalization":same_core,
      "distinct_raw_presentation":different_raw,
      "raw_stage3_index_sensitive_distinguishes":not raw_stage3_equal,
      "raw_stage3_default_empty_equates":default_empty_equal,
      "active_stage_comparison_equates":same_core,
      "active_status_observer_equal":first_observer==second_observer,
      "raw_presence_observer_differs":("q" in P["ap"])!=("q" in Q["ap"]),
      "external_source_labels_not_recoverable_from_identical_raw":sources[0]!=sources[1],
      "naive_q_promotion_invalid_without_active_Xi_or_Ap":not type_check(promoted),
    }
    tests["finite_observations_match_predeclared_expectations"]=observations==expected
    result={"audit_id":led["audit_id"],"checked":len(tests),"passed":sum(tests.values()),
            "checks":tests,"finite_observations":observations,
            "limit":"task-relative logical example, not external-domain evaluation",
            "source_edited":False,"semantics_choice":"DEFERRED","property_FPA":"OPEN"}
    out=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(out,encoding="utf-8")
    else: print(out,end="")
    if not all(tests.values()):raise SystemExit("P48 ROLE ADMISSIBILITY AUDIT FAILED")
if __name__=="__main__":main()
