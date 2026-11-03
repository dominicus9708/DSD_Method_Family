#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PA-P45 deterministic finite audit of semantic decision alternatives.
Author: Kwon Dominicus. NOT a machine proof of the general set-theoretic results.
Fixed one-point inherited carrier and no auxiliary carriers; raw surplus is
allowed ONLY under an explicitly hypothetical typed-B extension.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
import argparse
import hashlib
import json
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
P27=ROOT/"P27_independent_math_revision"
EN=P27/"DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR=P27/"DSD_Property_Axiom_System_KR_P27_REVISED.tex"
P44=ROOT/"P44_predecision_readiness"/"P44_PREDECISION_EVIDENCE_LEDGER.json"
LEDGER=HERE/"P45_SEMANTIC_COMPARISON_DECISION_LEDGER.json"
EXPECTED=HERE/"P45_EXPECTED_EVIDENCE.json"

@dataclass(frozen=True)
class Raw:
    active: int
    # q is never declared. It may have typed surplus raw primitive coords.
    q_ap: str
    q_xi: str

AP=("absent","empty","full")
XI=("absent","empty","assign")

def normalized(raw: Raw) -> int:
    """A-only active core. p is not declared in case 0, declared in 1-3."""
    return raw.active

def include(canonical: int) -> Raw:
    return Raw(canonical,"absent","absent")

def active_declaration(core:int) -> bool:
    return core!=0

def active_ap(core:int) -> bool:
    return core in (2,3)

def active_assignment(core:int) -> bool:
    return core==3

def derivation(core:int) -> tuple[str,str]:
    status=("undeclared","inapplicable","undefined","defined-zero")[core]
    return (status,"q-undeclared")

def welltyped_and_axioms(raw:Raw) -> bool:
    # one legal product input ('a',) and shared value carrier {0}.
    assert raw.active in range(4)
    assert raw.q_ap in AP and raw.q_xi in XI
    input_product={("a",)}
    q_ap=set() if raw.q_ap=="empty" else input_product if raw.q_ap=="full" else None
    q_xi={} if raw.q_xi=="empty" else {("a",):0} if raw.q_xi=="assign" else None
    if q_ap is not None and not q_ap <= input_product:
        return False
    if q_xi is not None and (not set(q_xi) <= input_product or any(v!=0 for v in q_xi.values())):
        return False
    # Active p has no prerequisite kinds, hence DepSat is full product.
    domain_p = input_product if active_assignment(raw.active) else set()
    app_p = input_product if active_ap(raw.active) else set()
    pi = domain_p <= app_p
    pii = domain_p <= input_product
    return pi and pii

def completion(raw: Raw) -> tuple[Raw,tuple[str,str]]:
    # Raw inclusion is exact; deterministic derived content sees active only.
    return (raw, derivation(normalized(raw)))

def reduction(full:tuple[Raw,tuple[str,str]]) -> Raw:
    return full[0]

def i_active(core1:int, core2:int, k:int) -> bool:
    if k==1: return True
    if active_declaration(core1)!=active_declaration(core2):return False
    if k==2:return True
    if active_ap(core1)!=active_ap(core2):return False
    if k==3:return True
    if active_assignment(core1)!=active_assignment(core2):return False
    if k==4:return True
    return derivation(core1)==derivation(core2)

def i_raw(p:Raw,q:Raw,k:int) -> bool:
    if k==1:return True
    if not i_active(p.active,q.active,2):return False
    if k==2:return True
    if not i_active(p.active,q.active,3) or p.q_ap!=q.q_ap:return False
    if k==3:return True
    if not i_active(p.active,q.active,4) or p.q_xi!=q.q_xi:return False
    if k==4:return True
    return derivation(p.active)==derivation(q.active)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    expected=json.loads(EXPECTED.read_text(encoding="utf-8"))
    ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
    p44=json.loads(P44.read_text(encoding="utf-8"))
    cores=tuple(range(4))
    b=tuple(Raw(core,ap,xi) for core,ap,xi in product(cores,AP,XI))
    pairs=tuple(product(b,b))
    equal_normalization=[(p,q) for p,q in pairs if normalized(p)==normalized(q)]
    same_core_distinct=[(p,q) for p,q in equal_normalization if p!=q]
    raw3=[(p,q) for p,q in same_core_distinct if i_raw(p,q,2) and not i_raw(p,q,3)]
    raw4=[(p,q) for p,q in same_core_distinct if i_raw(p,q,3) and not i_raw(p,q,4)]
    raw5=[(p,q) for p,q in pairs if i_raw(p,q,4) and not i_raw(p,q,5)]
    fiber_sizes=Counter(normalized(p) for p in b)
    # An active-only observer must be constant on each normalization fiber.
    active_status_constant=all(derivation(normalized(p))==derivation(normalized(q))
                              for p,q in equal_normalization)
    # Raw key-presence is not such an observer.
    raw_key_nonfactor=any((p.q_ap=="absent")!=(q.q_ap=="absent")
                          for p,q in equal_normalization)
    checks={
      "EN_P27_frozen_SHA256": hashlib.sha256(EN.read_bytes()).hexdigest()==ledger["frozen_P27_sha256"]["EN"],
      "KR_P27_frozen_SHA256": hashlib.sha256(KR.read_bytes()).hexdigest()==ledger["frozen_P27_sha256"]["KR"],
      "P44_P27_frozen_identical":p44["source_sha256"]==ledger["frozen_P27_sha256"],
      "P45_ledger_audit_id":ledger["audit_id"]==expected["audit_id"],
      "P45_seven_conditional_math_results":{x["id"] for x in ledger["formal_results"]}==
          {"R1_SPLIT_RETRACTION","R2_QUOTIENT","R3_FACTOR","R4_ACTIVE_BLINDNESS",
           "R5_STRICT_REFINEMENT","R6_C1_EXACT","R7_STAGE_COMPARISON"},
      "P45_six_independent_decision_axes":len(ledger["decision_axes"])==6,
      "options_remain_A_B1_B2":{x["id"] for x in p44["alternatives"]}==
          set(ledger["core_definitions"]) & {"A","B1","B2"},
      "36_typed_raw_presentations":len(b)==expected["raw_presentations"]==36 and
          len(set(b))==len(b) and all(welltyped_and_axioms(p) for p in b),
      "4_distinct_active_cores":len(set(map(normalized,b)))==expected["active_cores"]==4,
      "9_raw_variants_per_core":set(fiber_sizes.values())=={expected["raw_variants_per_core"]}=={9},
      "1296_ordered_pairs":len(pairs)==expected["ordered_pairs"]==1296,
      "324_equal_normalization_pairs":len(equal_normalization)==expected["equal_normalization_pairs"]==324,
      "288_distinct_raw_same_core":len(same_core_distinct)==expected["raw_distinct_same_core_pairs"]==288,
      "216_raw_stage3_same_core_branch":len(raw3)==expected["raw_stage3_branch_same_core_pairs"]==216,
      "72_raw_stage4_same_core_branch":len(raw4)==expected["raw_stage4_branch_same_core_pairs"]==72,
      "stage3_plus_stage4_exactly_distinct_pairs":len(raw3)+len(raw4)==len(same_core_distinct),
      "raw_stage5_no_extra_branch":len(raw5)==expected["raw_stage5_extra_branch_pairs"]==0,
      "active_stage4_equals_stage5":all(i_active(p.active,q.active,4)==i_active(p.active,q.active,5) for p,q in pairs),
      "raw_strict_implies_active_strict":all(not i_raw(p,q,4) or i_active(p.active,q.active,4) for p,q in pairs),
      "active_strict_does_not_imply_raw_strict":any(i_active(p.active,q.active,4) and not i_raw(p,q,4) for p,q in pairs),
      "N_compose_i_identity":all(normalized(include(a))==a for a in cores),
      "canonical_inclusion_is_injective":len(set(include(a) for a in cores))==len(cores),
      "normalization_noninjective":len(b)>len(set(map(normalized,b))),
      "raw_C1_exact_reduction_inverse":all(reduction(completion(p))==p for p in b),
      "raw_C1_exact_full_inverse":all(completion(reduction(completion(p)))==completion(p) for p in b),
      "raw_C1_derived_factors_through_N":active_status_constant,
      "raw_key_query_does_not_factor_through_N":raw_key_nonfactor,
      "active_observer_indistinguishable_in_fiber":all(i_active(p.active,q.active,4) for p,q in equal_normalization),
      "A_B1_B2_decision_deferred":ledger["audit_verdict"]["decision"]=="DEFERRED" and
         ledger["audit_verdict"]["alternatives_discarded"]==[],
      "P27_unmodified_and_property_FPA_open": not ledger["audit_verdict"]["P27_manuscripts_edited"] and
         ledger["audit_verdict"]["full_property_FPA"]=="OPEN",
    }
    result={
      "audit_id":ledger["audit_id"],
      "passed":sum(checks.values()),"checked":len(checks),"checks":checks,
      "fixture":{"raw_presentations":len(b),"normalized_cores":len(cores),
                 "fiber_sizes":dict(fiber_sizes),"ordered_pairs":len(pairs),
                 "same_active_pairs":len(equal_normalization),
                 "raw_distinct_same_core_pairs":len(same_core_distinct),
                 "raw_first_stage3_pairs":len(raw3),"raw_first_stage4_pairs":len(raw4)},
      "limit":"one fixed inherited singleton; B surplus admissibility is a conditional audit assumption",
      "not_formal_proof_of_all_models":True,
      "selection":"DEFERRED","full_property_FPA":"OPEN"
    }
    output=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(output,encoding="utf-8")
    else: print(output,end="")
    if not all(checks.values()):
        raise SystemExit("P45 semantic fixture or source audit FAILED")
if __name__=="__main__":
    main()
