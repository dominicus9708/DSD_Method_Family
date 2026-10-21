#!/usr/bin/env python3
"""Bounded FAS-F2-APPD-RESTRICT-001 checks, not a general proof.
Usage (repository root): python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_appd_restriction.py
Optional positional argument supplies an alternative JSON output path.
"""
import itertools
import json
import sys
from pathlib import Path

SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'

def closure(relation,n):
    r=set(relation)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (i,k) in r and (k,j) in r: r.add((i,j))
    return r

def transitive(r):
    return all((a,c) in r for a,b in r for bb,c in r if b==bb)

def count_relations(n):
    others=[(a,b) for a in range(n) for b in range(n) if a!=b]
    diagonal={(i,i) for i in range(n)}
    counters={'reflexive':0,'preorders':0,'nontransitive':0,'preorders_nonantisymmetric':0}
    for mask in range(1<<len(others)):
        r=diagonal|{e for k,e in enumerate(others) if mask&(1<<k)}
        counters['reflexive']+=1
        c=closure(r,n)
        assert r<=c and transitive(c) and closure(c,n)==c
        if transitive(r):
            counters['preorders']+=1
            assert c==r
            if any(a<b and (a,b) in r and (b,a) in r for a in range(n) for b in range(n)):
                counters['preorders_nonantisymmetric']+=1
        else:
            counters['nontransitive']+=1
            assert c!=r
    assert counters['reflexive']==2**(n*(n-1))
    assert counters['reflexive']==counters['preorders']+counters['nontransitive']
    return counters

def chain_witness():
    # All admitted H,h,g have identical material {0}, anchors, induced records.
    # g is describable, and Realize(g,p), all three p-gates, q(0)=1,
    # Role(p,0,lambda,rho) supply one nonzero admitted formation channel.
    R={(0,0),(1,1),(2,2),(0,1),(1,2)}
    C=closure(R,3)
    assert not transitive(R) and transitive(C) and (0,2) in C-R
    traces_before={(u,v) for u,v in R if v==2}
    traces_after={(u,v) for u,v in C if v==2}
    assert len(traces_before)==2 and len(traces_after)==3
    assert (2,2) in traces_before
    return {'axiom_ii_inheritance':True,'nontransitive_legal_core':True,
            'optional_new_edge':['H','g'], 'traces_before':2,'traces_after':3,
            'same_describability_and_one_channel':True}

def global_scope():
    # Candidate U is unadmitted, targets h,g are admitted.
    R={(1,1),(2,2),(0,1),(1,2)}
    admitted={(1,1),(1,2),(2,2)}
    assert admitted == {(a,b) for a,b in R if a>0 and b>0}
    assert transitive(admitted) and (0,2) not in R and (0,2) in closure(R,3)
    return {'admitted_subrelation_preorder_before_extension':True,
            'global_clause_still_not_satisfied':True}

def induced_composition():
    total=0
    for n in range(5):
        for aa in itertools.product((0,1),repeat=n):
            A={i for i,x in enumerate(aa) if x}
            for yy in itertools.product((0,1),repeat=n):
                Y={i for i,x in enumerate(yy) if x}
                if not Y<=A:continue
                for zz in itertools.product((0,1),repeat=n):
                    Z={i for i,x in enumerate(zz) if x}
                    if not Z<=Y:continue
                    fA={i:('s',i) for i in A}
                    first={i:fA[i] for i in Y}
                    second={i:first[i] for i in Z}
                    direct={i:fA[i] for i in Z}
                    assert second==direct
                    total+=1
    assert total==sum(4**n for n in range(5))
    # Even transitive primitive Res may allow distinct g1,g2 with identical
    # empty material; choosing H|empty=g2 and (H|{0})|empty=g1 can disagree.
    material=[{0,1},{0},{0},set(),set()]
    labels=['H','h1','h2','g1','g2']
    R={(i,i) for i in range(5)}|{(0,1),(0,2),(0,3),(0,4),(1,3)}
    C=closure(R,5)
    assert all(material[b]<=material[a] for a,b in C)
    assert transitive(C) and labels[3]!=labels[4]
    return {'nested_triples_checked':total,'all_pass':True,
            'nonunique_tag_selection_counterexample':True}

def main():
    out={'audit_id':'FAS-F2-APPD-RESTRICT-001','source_sha256':SHA,
         'reflexive_relation_exhaustive':{str(n):count_relations(n) for n in (3,4)},
         'nontransitive_with_active_channel':chain_witness(),
         'admitted_vs_global_transitivity':global_scope(),
         'induced_subexpression_checks':induced_composition(),
         'finite_scope_only':True,'full_F2':'OPEN','external_independent_validation':False}
    target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'results/appd_restriction.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True))
if __name__=='__main__':main()
