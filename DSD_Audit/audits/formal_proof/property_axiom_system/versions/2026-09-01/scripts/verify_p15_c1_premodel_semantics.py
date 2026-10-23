#!/usr/bin/env python3
"""P15 bounded independent truth-table audit of C1-relative independence.

Paper: Kwon Dominicus, Property Axiom System (English 2026-09-01).
The all-set sizes <=3 are finite demonstrations, NOT general formal proof.
Only outputs JSON to given path; never edits original Property_Axiom_System code.
Usage: python verify_p15_c1_premodel_semantics.py [output.json]
"""
from __future__ import annotations
from itertools import combinations, product
from pathlib import Path
import json
import sys

PAPER_SHA="03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"

def powerset(xs):
    xs=tuple(xs)
    return tuple(frozenset(z) for n in range(len(xs)+1) for z in combinations(xs,n))

def predicate_sets(X,Ap,Dep,D):
    return {
      "inapplicable":X-Ap,
      "prerequisite_unsatisfied":Ap-Dep,
      "applicable_undefined":(Ap&Dep)-D,
      "defined":D
    }

def check(X,Ap,Dep,D):
    S=predicate_sets(X,Ap,Dep,D)
    union=frozenset().union(*S.values())
    names=tuple(S)
    pairwise_disjoint=all(not(S[a]&S[b]) for i,a in enumerate(names) for b in names[i+1:])
    axiom_i=D<=Ap
    axiom_ii=D<=Dep
    assert union==X
    assert pairwise_disjoint==(axiom_i and axiom_ii), (X,Ap,Dep,D,S)
    return {
      "axiom_i":axiom_i,
      "axiom_ii":axiom_ii,
      "exclusive":pairwise_disjoint,
      "status_multiplicity":max((sum(x in s for s in S.values()) for x in X),default=0)
    }

def evaluate():
    totals={}
    for n in range(4):
        X=frozenset(range(n))
        subs=powerset(X)
        t={"premodels":0,"both_axioms":0,"status_partitions":0,
           "at_least_one_primitive_violation":0,"overlap_witnesses":0}
        for Ap,Dep,D in product(subs,repeat=3):
            r=check(X,Ap,Dep,D)
            t["premodels"]+=1
            t["both_axioms"]+=int(r["axiom_i"] and r["axiom_ii"])
            t["status_partitions"]+=int(r["exclusive"])
            t["at_least_one_primitive_violation"]+=int(not (r["axiom_i"] and r["axiom_ii"]))
            t["overlap_witnesses"]+=int(r["status_multiplicity"]>1)
        assert t["premodels"]==8**n
        assert t["both_axioms"]==t["status_partitions"]==5**n
        assert t["at_least_one_primitive_violation"]==t["overlap_witnesses"]==8**n-5**n
        totals[str(n)]=t
    X=frozenset(("x",))
    cm1={"Ap":frozenset(),"Dep":X,"D":X}
    cm2={"Ap":X,"Dep":frozenset(),"D":X}
    witnesses={}
    for name,m in (("countermodel_4_1",cm1),("countermodel_4_2",cm2)):
        p=predicate_sets(X,**m)
        r=check(X,**m)
        active=sorted(k for k,v in p.items() if "x" in v)
        assert active==(
            ["defined","inapplicable"] if name.endswith("4_1")
            else ["defined","prerequisite_unsatisfied"]
        )
        assert not r["exclusive"]
        witnesses[name]={"axiom_i":r["axiom_i"],"axiom_ii":r["axiom_ii"],
                         "active_status_predicates":active}
    assert not witnesses["countermodel_4_1"]["axiom_i"]
    assert witnesses["countermodel_4_1"]["axiom_ii"]
    assert witnesses["countermodel_4_2"]["axiom_i"]
    assert not witnesses["countermodel_4_2"]["axiom_ii"]
    assert sum(x["premodels"] for x in totals.values())==585
    assert sum(x["status_partitions"] for x in totals.values())==156
    return {
      "case":"PA-P15-20260901-C1-COUNTERMODEL-SEMANTICS-001",
      "source_pdf_sha256":PAPER_SHA,
      "range":"all subsets Ap,DepSat,D of X, cardinalities 0,1,2,3",
      "per_cardinality":totals,
      "total_premodels_checked":585,
      "total_partition_models":156,
      "total_overlapping_premodels":429,
      "countermodels":witnesses,
      "raw_status_predicates_unique_by_definition_on_each_premodel":True,
      "exclusive_status_partition_iff_pi_and_pii_in_tested_universe":True,
      "literal_C1_full_core_only_extended_to_premodels_automatically":False,
      "fully_general_proof_assistant_verification":False,
      "original_Python_modified":False,
      "author_manuscript_modified":False,
      "FPA":"OPEN"
    }

if __name__=="__main__":
    result=evaluate()
    if len(sys.argv)>1:
        p=Path(sys.argv[1])
    else:
        p=Path(__file__).resolve().parent.parent/"results/p15_c1_premodel_semantics.json"
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("P15 C1 status/premodel audit PASS",
          result["total_premodels_checked"],"premodels",
          result["total_partition_models"],"partitioned",
          result["total_overlapping_premodels"],"overlapping")
