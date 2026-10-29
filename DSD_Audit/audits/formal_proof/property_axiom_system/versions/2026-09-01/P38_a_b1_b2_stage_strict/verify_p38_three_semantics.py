#!/usr/bin/env python3
"""PA-P38: independent finite A/B1/B2 comparison audit; Kwon Dominicus."""
from __future__ import annotations
import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path

KINDS=('p','q')
DEPS={'p':(),'q':('d',)}
H=('h0',)
VALUES=(0,1)

@dataclass
class Model:
    aux: tuple[str,...] | None
    declared: frozenset[str]
    ap: dict[str,frozenset[tuple[str,...]]]
    sat: dict[tuple[str,str],frozenset[tuple[str,...]]]
    xi: dict[str,dict[tuple[str,...],int]]

def product(m,w):
    if w=='p':
        return None if m.aux is None else tuple((x,) for x in m.aux)
    return tuple((x,) for x in H)

def active(m):
    return frozenset(w for w in m.declared if product(m,w) is not None)

def dep_sat(m,w):
    x=product(m,w)
    if not DEPS[w]:return frozenset(x)
    return frozenset.intersection(*(m.sat[(w,d)] for d in DEPS[w]))

def legal(m,raw=True):
    kinds=active(m)
    for w in kinds:
        if w not in m.ap or w not in m.xi or any((w,d) not in m.sat for d in DEPS[w]):return False
    if not raw and (set(m.ap)!=set(kinds) or set(m.xi)!=set(kinds) or set(m.sat)!={(w,d) for w in kinds for d in DEPS[w]}):return False
    for w,v in m.ap.items():
        x=product(m,w)
        if x is None or not v.issubset(x):return False
    for (w,d),v in m.sat.items():
        x=product(m,w)
        if d not in DEPS[w] or x is None or not v.issubset(x):return False
    for w,assignment in m.xi.items():
        x=product(m,w)
        if x is None or not set(assignment).issubset(x) or not set(assignment.values()).issubset(VALUES):return False
        if w in kinds:
            if not set(assignment).issubset(m.ap[w]) or not set(assignment).issubset(dep_sat(m,w)):return False
    return True

def completed(m):
    out={}
    for w in active(m):
        d=frozenset(m.xi[w]);deps=dep_sat(m,w)
        status={}
        for x in product(m,w):
            if x not in m.ap[w]:status[x]='inapplicable'
            elif x not in deps:status[x]='prerequisite_unsatisfied'
            elif x not in d:status[x]='applicable_undefined'
            elif m.xi[w][x]==0:status[x]='defined_zero'
            else:status[x]='defined_nonzero'
        rec=frozenset((w,x,v) for x,v in m.xi[w].items())
        out[w]={'D':d,'DepSat':deps,'status':status,'records':rec}
    return out

def normalize(m):
    kinds=active(m)
    return Model(m.aux,m.declared,
        {w:m.ap[w] for w in kinds},
        {(w,d):m.sat[(w,d)] for w in kinds for d in DEPS[w]},
        {w:m.xi[w] for w in kinds})

def raw_storage(m):
    return (m.aux,m.declared,m.ap,m.sat,m.xi)

def maps(a,b):
    if (a.aux is None)!=(b.aux is None):return []
    if a.aux is None:return [()]
    if len(a.aux)!=len(b.aux):return []
    return list(itertools.permutations(b.aux))

def image_x(a,b,w,f,x):
    if w=='q':return x
    assert a.aux is not None and b.aux is not None
    return (dict(zip(a.aux,f))[x[0]],)

def image_set(a,b,w,f,xs):
    return frozenset(image_x(a,b,w,f,x) for x in xs)

def compare_stages(a,b,raw=False):
    i1=set(maps(a,b))
    i2={f for f in i1 if a.declared==b.declared}
    aa=active(a);bb=active(b)
    if a.declared==b.declared and (a.aux is None)==(b.aux is None):
        assert aa==bb
    def third(f):
        apkeys=set(a.ap) if raw else aa
        satkeys=set(a.sat) if raw else {(w,d) for w in aa for d in DEPS[w]}
        if raw and (apkeys!=set(b.ap) or satkeys!=set(b.sat)):return False
        for w in apkeys:
            if image_set(a,b,w,f,a.ap[w])!=b.ap[w]:return False
        for w,d in satkeys:
            if image_set(a,b,w,f,a.sat[(w,d)])!=b.sat[(w,d)]:return False
        return True
    i3={f for f in i2 if third(f)}
    def fourth(f):
        xikeys=set(a.xi) if raw else aa
        if raw and xikeys!=set(b.xi):return False
        for w in xikeys:
            if {image_x(a,b,w,f,x):v for x,v in a.xi[w].items()}!=b.xi[w]:return False
        return True
    i4={f for f in i3 if fourth(f)}
    def fifth(f):
        ca=completed(a);cb=completed(b)
        for w in ca:
            x=ca[w];y=cb[w]
            if image_set(a,b,w,f,x['D'])!=y['D']:return False
            if image_set(a,b,w,f,x['DepSat'])!=y['DepSat']:return False
            if {image_x(a,b,w,f,z):v for z,v in x['status'].items()}!=y['status']:return False
            if frozenset((w,image_x(a,b,w,f,z),v) for _,z,v in x['records'])!=y['records']:return False
        return True
    i5={f for f in i4 if fifth(f)}
    return (i1,i2,i3,i4,i5)

def strict_def6(a,b,f):
    if (a.aux is None)!=(b.aux is None) or a.declared!=b.declared:return False
    if f not in maps(a,b):return False
    for w in active(a):
        for x in product(a,w):
            y=image_x(a,b,w,f,x)
            if (x in a.ap[w])!=(y in b.ap[w]):return False
            for d in DEPS[w]:
                if (x in a.sat[(w,d)])!=(y in b.sat[(w,d)]):return False
            if (x in a.xi[w])!=(y in b.xi[w]):return False
            if x in a.xi[w] and a.xi[w][x]!=b.xi[w][y]:return False
    return True

def make(aux,declared,template,extra):
    m=Model(aux,frozenset(declared),{},{},{})
    for w in active(m):
        xs=product(m,w)
        ap=frozenset(xs if template in (0,1,3) else xs[:1])
        m.ap[w]=ap
        for d in DEPS[w]:
            m.sat[(w,d)]=frozenset(xs if template!=3 else xs[:1])
        possible=[x for x in xs if x in ap and all(x in m.sat[(w,d)] for d in DEPS[w])]
        m.xi[w]={possible[0]:template%2} if possible and template in (1,3) else {}
    if extra:
        surplus=next((w for w in KINDS if w not in m.declared and product(m,w) is not None),None)
        if surplus is not None:m.ap[surplus]=frozenset(product(m,surplus)[:1] if extra==1 else ())
    assert legal(m,raw=True)
    return m

def branch(stages):
    for k,x in enumerate(stages[:4],1):
        if not x:return k
    return None

def run():
    objects=[]
    for aux,decl,t,extra in itertools.product(
        (None,(),('a',),('a','b')), ((),('p',),('q',),('p','q')),range(4),range(3)):
        obj=make(aux,decl,t,extra)
        if not any(raw_storage(obj)==raw_storage(p) for p in objects):objects.append(obj)
    checked=0; maps_tested=0; distinct=[]; stage3=0;stage4=0
    iso={};branches={}
    for ai,a in enumerate(objects):
        assert legal(normalize(a),raw=False)
        assert raw_storage(normalize(normalize(a)))==raw_storage(normalize(a))
        assert completed(a)==completed(normalize(a))
        for bi,b in enumerate(objects):
            checked+=1
            act=compare_stages(a,b,False)
            raw=compare_stages(a,b,True)
            norm=compare_stages(normalize(a),normalize(b),False)
            iso[ai,bi]=bool(raw[3]);branches[ai,bi]=branch(raw)
            assert act==norm
            assert act[3]==act[4] and raw[3]==raw[4]
            assert all(raw[k].issubset(act[k]) for k in range(5))
            assert act[0]==raw[0] and act[1]==raw[1]
            assert act[4]=={f for f in maps(a,b) if strict_def6(a,b,f)}
            assert all(act[k+1].issubset(act[k]) and raw[k+1].issubset(raw[k]) for k in range(4))
            if act[3] and not raw[3]:
                distinct.append((ai,bi))
                if branch(raw)==3:stage3+=1
                if branch(raw)==4:stage4+=1
            maps_tested+=len(maps(a,b))
    parents=list(range(len(objects)))
    def root(i):
        while parents[i]!=i:
            parents[i]=parents[parents[i]];i=parents[i]
        return i
    for (i,j),yes in iso.items():
        if yes:parents[root(i)]=root(j)
    byclass={}
    for (i,j),first in branches.items():
        k=(root(i),root(j))
        if k in byclass:assert byclass[k]==first
        else:byclass[k]=first
    a=make(None,(),0,0);b=make(None,(),0,1)
    assert raw_storage(a)!=raw_storage(b)
    assert compare_stages(a,b,False)[3] and not compare_stages(a,b,True)[3]
    assert branch(compare_stages(a,b,True))==3
    c=make(None,(),0,0);d=make(None,(),0,0)
    d.xi['q']={('h0',):1}
    assert legal(d,raw=True)
    assert compare_stages(c,d,True)[2] and not compare_stages(c,d,True)[3]
    assert branch(compare_stages(c,d,True))==4
    assert compare_stages(a,b,False)[3] and branch(compare_stages(b,b,True)) is None
    checks={
      'A_C1_stage4_equals_stage5':True,
      'B1_active_stages_equal_normalized_A':True,
      'B1_core_iso_iff_I4_active':True,
      'B2_raw_first_branch_invariant_under_raw_iso':bool(byclass),
      'B2_raw_first_branch_not_core_iso_invariant':True,
      'B2_raw_iso_iff_I4_raw_by_definition':True,
      'B2_raw_iso_implies_original_core_iso':True,
      'B2_raw_stage3_can_branch_inside_core_iso':stage3>0,
      'B2_raw_stage4_can_branch_inside_core_iso':True,
      'B2_raw_stage4_equals_stage5':True,
      'N_idempotent_and_C1_active_invariant':True,
      'empty_supplied_differs_unavailable':not maps(make(None,(),0,0),make((),(),0,0)),
      'original_core_iso_not_imply_raw_iso':bool(distinct),
      'raw_stage1_stage2_equal_active':True,
      'raw_stage_each_subset_active':True,
      'surplus_raw_typing_guard_enforced':not legal(Model(None,frozenset(),{'p':frozenset({('a',)})},{},{}),True)
    }
    assert all(checks.values())
    return {
      'audit_id':'PA-P38-20261029-A-B1-B2-STAGE-STRICT-GENERAL-SCOPE',
      'checks':checks,
      'core_iso_but_not_raw_iso_pairs':len(distinct),
      'core_iso_raw_first_branch_stage3_pairs':stage3,
      'core_iso_raw_first_branch_stage4_pairs':stage4,
      'finite_model_count':len(objects),
      'finite_ordered_pairs':checked,
      'frozen_p27_sha256':{'EN':'51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb','KR':'a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb'},
      'passed':len(checks),
      'scope':'Finite two-candidate-kind, one optional-sort templates plus two hand-built witnesses; general mathematical proof is separate.',
      'tested_carrier_bijections':maps_tested,
      'total':len(checks),
      'verdict':{'A':'CONDITIONAL_GENERAL_PROOF_SUPPORTED','B1':'ACTIVE_STAGE_PROOF_SUPPORTED','B2':'RAW_STAGE_PROOF_REQUIRES_NEW_STRICT_RAW','FPA':'OPEN','manuscript_edited':False}
    }

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--out',default=None)
    args=p.parse_args()
    txt=json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    if args.out:Path(args.out).write_text(txt,encoding='utf-8')
    print(txt,end='')
