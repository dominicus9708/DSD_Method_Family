#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P46 source-protected finite branching comparison, Kwon Dominicus.
A raw extension is conditional: typed surplus keys are hypothetical.
Passing these checks is NOT a formal proof over arbitrary sets.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from itertools import product
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SRC=ROOT/"P27_independent_math_revision"
EN=SRC/"DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR=SRC/"DSD_Property_Axiom_System_KR_P27_REVISED.tex"
EXPECTED=HERE/"P46_SHARED_VS_BRANCHING_LEDGER.json"
P45=ROOT/"P45_semantics_predecision_comparison"/"P45_SEMANTIC_COMPARISON_DECISION_LEDGER.json"
P44=ROOT/"P44_predecision_readiness"/"P44_PREDECISION_EVIDENCE_LEDGER.json"
P42=ROOT/"P42_consolidated_premises_countermodels_revision_spec"/"P42_20_PLUS_13_REVISION_LEDGER.json"

@dataclass(frozen=True)
class Raw:
    core: int
    extra_ap: str
    extra_xi: str

CORE=tuple(range(4))
EXTRA_AP=("absent","empty","full")
EXTRA_XI=("absent","empty","assign")
INF=5  # internally 5; represents infinity, not P27 Stage 5.

def active_at(p: Raw,q: Raw,k: int) -> bool:
    if k==1: return True
    if (p.core==0)!=(q.core==0): return False
    if k==2: return True
    if (p.core>=2)!=(q.core>=2): return False
    if k==3: return True
    if (p.core==3)!=(q.core==3): return False
    return True

def raw_at(p: Raw,q: Raw,k: int) -> bool:
    if k==1: return True
    if not active_at(p,q,2): return False
    if k==2: return True
    if not active_at(p,q,3) or p.extra_ap != q.extra_ap: return False
    if k==3: return True
    if not active_at(p,q,4) or p.extra_xi != q.extra_xi: return False
    return True

def first_branch(p: Raw,q: Raw,comparator) -> int:
    for k in range(1,5):
        if not comparator(p,q,k):
            return k
    return INF

def typed_valid(p: Raw) -> bool:
    # inherited one-point product {("a",)}, candidate q always undeclared
    # and therefore its optional surplus coordinates are outside PI/PII.
    product_x={("a",)}
    q_ap = {"absent":None,"empty":set(),"full":product_x}[p.extra_ap]
    q_xi = {"absent":None,"empty":{},"assign":{("a",):0}}[p.extra_xi]
    if q_ap is not None and not q_ap <= product_x: return False
    if q_xi is not None:
        if not set(q_xi).issubset(product_x): return False
        if not all(v==0 for v in q_xi.values()): return False
    p_app = product_x if p.core >= 2 else set()
    p_dom = product_x if p.core == 3 else set()
    return p_dom <= p_app and p_dom <= product_x

def count_keys(items) -> dict[str,int]:
    count=Counter(items)
    return {str(k):v for k,v in sorted(count.items())}

def branch_name(b: int) -> str:
    return "infinity" if b==INF else str(b)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    ledger=json.loads(EXPECTED.read_text(encoding="utf-8"))
    p45=json.loads(P45.read_text(encoding="utf-8"))
    p44=json.loads(P44.read_text(encoding="utf-8"))
    p42=json.loads(P42.read_text(encoding="utf-8"))
    P=tuple(Raw(c,a,x) for c,a,x in product(CORE,EXTRA_AP,EXTRA_XI))
    pairs=tuple(product(P,P))
    counts_act=Counter()
    counts_raw=Counter()
    joint=Counter()
    raw_earlier=0
    raw_later=0
    act_strict_but_not_raw=0
    strict_raw=0
    strict_act=0
    for p,q in pairs:
        b_act=first_branch(p,q,active_at)
        b_raw=first_branch(p,q,raw_at)
        ka,kb=branch_name(b_act),branch_name(b_raw)
        counts_act[ka]+=1
        counts_raw[kb]+=1
        joint[f"{ka}/{kb}"]+=1
        raw_earlier += b_raw<b_act
        raw_later += b_raw>b_act
        strict_raw += b_raw==INF
        strict_act += b_act==INF
        act_strict_but_not_raw += b_act==INF and b_raw != INF
    expected=ledger["finite_expected"]
    counts_act=dict(counts_act)
    counts_raw=dict(counts_raw)
    joint=dict(joint)
    checks={
        "P27_EN_SHA256_unchanged":hashlib.sha256(EN.read_bytes()).hexdigest()==ledger["P27_sha256"]["EN"],
        "P27_KR_SHA256_unchanged":hashlib.sha256(KR.read_bytes()).hexdigest()==ledger["P27_sha256"]["KR"],
        "P44_P27_SHA_consistent":p44["source_sha256"]==ledger["P27_sha256"],
        "P45_P27_SHA_consistent":p45["frozen_P27_sha256"]==ledger["P27_sha256"],
        "P42_P27_SHA_consistent":p42["frozen_sha256"]==ledger["P27_sha256"],
        "seven_common_claims":len(ledger["shared_mathematics"])==7,
        "six_variable_claims":len(ledger["changing_results"])==6,
        "five_conditional_theorems":len(ledger["conditional_theorems"])==5,
        "all_key_proofs_recorded":all(t["proof"] and t["necessary"] for t in ledger["conditional_theorems"]),
        "36_models":len(P)==expected["model_count"]==36,
        "models_distinct":len(set(P))==len(P),
        "every_surplus_typed":all(typed_valid(p) for p in P),
        "four_active_cores":len(set(p.core for p in P))==expected["active_core_count"]==4,
        "nine_variants_each":all(sum(p.core==i for p in P)==expected["raw_variants_per_active_core"]==9 for i in CORE),
        "1296_ordered_pairs":len(pairs)==expected["ordered_pairs"]==1296,
        "active_first_branch_histogram":counts_act==expected["beta_active"],
        "raw_first_branch_histogram":counts_raw==expected["beta_raw"],
        "joint_first_branch_histogram":joint==expected["joint_beta"],
        "raw_candidate_subset_active_all_stages":all(
            not raw_at(p,q,k) or active_at(p,q,k)
            for p,q in pairs for k in range(1,6)),
        "nested_active_stages":all(
            not active_at(p,q,k+1) or active_at(p,q,k)
            for p,q in pairs for k in range(1,5)),
        "nested_raw_stages":all(
            not raw_at(p,q,k+1) or raw_at(p,q,k)
            for p,q in pairs for k in range(1,5)),
        "active_stage4_equals_stage5":all(
            active_at(p,q,4)==active_at(p,q,5) for p,q in pairs),
        "raw_stage4_equals_stage5":all(
            raw_at(p,q,4)==raw_at(p,q,5) for p,q in pairs),
        "raw_branch_never_later":raw_later==0,
        "raw_branch_strict_earlier":raw_earlier==expected["raw_earlier_than_active_pairs"]==396,
        "raw_strict_implies_active_strict":all(
            first_branch(p,q,raw_at)!=INF or first_branch(p,q,active_at)==INF
            for p,q in pairs),
        "active_not_implies_raw_strict":act_strict_but_not_raw==expected["active_strict_but_not_raw_strict_pairs"]==288,
        "raw_strict_classes_in_singleton_fixture":strict_raw==expected["raw_strict_class_count"]==36,
        "active_strict_class_pairs":strict_act==324,
        "active_strict_classes_in_singleton_fixture":len(set(p.core for p in P))==expected["active_strict_class_count"]==4,
        "108_stage_4_vs_3_cases":joint["4/3"]==108,
        "216_active_iso_raw_stage3_cases":joint["infinity/3"]==216,
        "72_active_iso_raw_stage4_cases":joint["infinity/4"]==72,
        "semantics_not_selected":ledger["chosen_semantics"]=="DEFERRED",
        "all_S01_S04_preserved":set(p42["open_obligations"])=={"S-01","S-02","S-03","S-04"},
        "FPA_OPEN_unmodified":not ledger["verdict"]["source_changed"] and ledger["verdict"]["full_fpa"]=="OPEN",
        "no_options_discarded":ledger["verdict"]["options_discarded"]==[],
        "outside_independent_verification_not_claimed":ledger["verdict"]["external_independent_validation"]=="NOT_ESTABLISHED",
    }
    result={
        "audit_id":ledger["audit_id"],
        "passed":sum(checks.values()),"checked":len(checks),"checks":checks,
        "finite_histograms":{"active":counts_act,"raw":counts_raw,"joint":joint,
            "raw_earlier":raw_earlier,"raw_later":raw_later,
            "active_strict_not_raw":act_strict_but_not_raw},
        "mathematical_scope":"conditional general arguments are in the audit; finite check is only a typed singleton fixture",
        "source_modified":False,"choice":"DEFERRED","FPA":"OPEN"
    }
    rendered=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(rendered,encoding="utf-8")
    else:
        print(rendered,end="")
    if not all(checks.values()):
        raise SystemExit("P46 AUDIT REGRESSION FAILED")
if __name__=="__main__":
    main()
