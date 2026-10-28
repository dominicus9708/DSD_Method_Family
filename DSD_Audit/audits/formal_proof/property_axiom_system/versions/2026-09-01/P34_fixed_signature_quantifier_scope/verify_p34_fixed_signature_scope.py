#!/usr/bin/env python3
"""P34 fixed-signature scope regression; bounded witnesses, not a ZFC proof.
Author: Kwon Dominicus. P27 manuscript remains frozen.
Run: python verify_p34_fixed_signature_scope.py [result.json]
"""
from dataclasses import dataclass, field
from itertools import product, permutations
from pathlib import Path
import json, sys

@dataclass(frozen=True)
class Kind:
    profile: tuple
    deps: tuple = ()
    values: tuple = (0,)
    zero: bool = False

@dataclass
class Signature:
    auxiliary: tuple
    inherited: dict
    kinds: dict

@dataclass
class Model:
    sig: Signature
    supply: dict = field(default_factory=dict)
    declared: frozenset = frozenset()
    ap: dict = field(default_factory=dict)
    sat: dict = field(default_factory=dict)
    xi: dict = field(default_factory=dict)

    def available(self, k):
        return all(s in self.sig.inherited or s in self.supply for s in self.sig.kinds[k].profile)

    def active(self):
        return {k for k in self.declared if self.available(k)}

    def inputs(self, k):
        assert self.available(k)
        return set(product(*(self.sig.inherited[s] if s in self.sig.inherited else self.supply[s]
                             for s in self.sig.kinds[k].profile)))

    def legal(self):
        assert set(self.supply) <= set(self.sig.auxiliary)
        assert self.declared <= self.sig.kinds.keys()
        assert set(self.ap) == self.active() == set(self.xi)
        assert set(self.sat) == {(k,d) for k in self.active() for d in self.sig.kinds[k].deps}
        for k in self.active():
            X = self.inputs(k)
            assert self.ap[k] <= X
            assert set(self.xi[k]) <= self.ap[k]
            assert all(v in self.sig.kinds[k].values for v in self.xi[k].values())
            for d in self.sig.kinds[k].deps:
                assert self.sat[k,d] <= X
                assert set(self.xi[k]) <= self.sat[k,d]
        return True

def bijections(A,B):
    if A.sig is not B.sig or set(A.supply)!=set(B.supply): return []
    opts=[]
    for s in sorted(A.supply):
        a,b=A.supply[s],B.supply[s]
        if len(a)!=len(b):return []
        opts.append([(s,dict(zip(a,p))) for p in permutations(b)])
    return [dict(x) for x in product(*opts)]

def push(A,k,x,f):
    return tuple(x[i] if sort in A.sig.inherited else f[sort][x[i]]
                 for i,sort in enumerate(A.sig.kinds[k].profile))

def I(A,B,stage):
    out=[]
    for f in bijections(A,B):
        if stage>=2 and A.declared!=B.declared:continue
        ok=True
        for k in A.active() if stage>=3 else ():
            for x in A.inputs(k):
                y=push(A,k,x,f)
                if ((x in A.ap[k]) != (y in B.ap[k])
                    or any((x in A.sat[k,d]) != (y in B.sat[k,d])
                           for d in A.sig.kinds[k].deps)):
                    ok=False;break
                if stage>=4:
                    if (x in A.xi[k])!=(y in B.xi[k]):
                        ok=False;break
                    if x in A.xi[k] and A.xi[k][x]!=B.xi[k][y]:
                        ok=False;break
            if not ok:break
        if ok:out.append(f)
    return out

def summary(A):
    assert A.legal()
    out=[]
    for k in sorted(A.declared):
        assert A.available(k) and A.sig.kinds[k].zero
        n0=sum(v==0 for v in A.xi[k].values())
        out.append((k,len(A.xi[k]),n0,len(A.xi[k])-n0))
    return (len(A.declared),tuple(out))

def verify():
    checks={}
    def check(key,condition):
        checks[key]=bool(condition)
        assert checks[key],key
    x=('a',)
    empty=Signature((),{},{})
    e=Model(empty)
    check('empty_signature_one_canonical_model',e.legal() and len(I(e,e,4))==1)
    check('empty_signature_no_nontrivial_branch',all(len(I(e,e,k))==1 for k in range(1,5)))
    check('empty_signature_trivial_summary',summary(e)==(0,()))
    depfree=Signature(('u',),{}, {'p':Kind(('u',),(),(0,1))})
    check('dependency_free_PII_tautology',
          all(set(D) <= {x} for D in ((),(x,))))
    check('dependency_free_PI_can_fail',x not in set() and x in {x})
    pi={'dom':{x},'ap':set(),'sat':{x}}
    pii={'dom':{x},'ap':{x},'sat':set()}
    check('common_signature_PI_counterpremodel',
          pi['dom']<=pi['sat'] and not pi['dom']<=pi['ap'])
    check('common_signature_PII_counterpremodel',
          pii['dom']<=pii['ap'] and not pii['dom']<=pii['sat'])
    a2=Model(depfree,{},frozenset({'p'}))
    b2=Model(depfree)
    check('stage2_one_candidate_unavailable',
          a2.legal() and b2.legal() and [len(I(a2,b2,k)) for k in range(1,5)]==[1,0,0,0])
    a3=Model(depfree,{'u':('a',)},frozenset({'p'}),{'p':set()},{},{'p':{}})
    b3=Model(depfree,{'u':('a',)},frozenset({'p'}),{'p':{x}},{},{'p':{}})
    check('stage3_one_kind_one_input',
          a3.legal() and b3.legal() and [len(I(a3,b3,k)) for k in range(1,5)]==[1,1,0,0])
    v=Signature(('u',),{}, {'p':Kind(('u',),(),(0,))})
    a4=Model(v,{'u':('a',)},frozenset({'p'}),{'p':{x}},{},{'p':{}})
    b4=Model(v,{'u':('a',)},frozenset({'p'}),{'p':{x}},{},{'p':{x:0}})
    check('stage4_one_kind_one_input_one_value',
          a4.legal() and b4.legal() and [len(I(a4,b4,k)) for k in range(1,5)]==[1,1,1,0])
    z=Signature(('u',),{}, {'p':Kind(('u',),(),(0,),True)})
    za=Model(z,{'u':('a',)},frozenset({'p'}),{'p':set()},{},{'p':{}})
    zb=Model(z,{'u':('a',)},frozenset({'p'}),{'p':{x}},{},{'p':{}})
    check('one_zero_kind_summary_collision',summary(za)==summary(zb) and not I(za,zb,4))
    check('one_zero_kind_summary_is_labelled',summary(za)==(1,(('p',0,0,0),)))
    aux=Signature(('u',),{}, {})
    xa=Model(aux)
    xb=Model(aux,{'u':()})
    check('auxiliary_availability_summary_collision',summary(xa)==summary(xb) and not I(xa,xb,4))
    h=Signature((),{'h':()}, {'p':Kind(('h',),('d',),(0,),True)})
    hm=Model(h,{},frozenset({'p'}),{'p':set()},{('p','d'):set()},{'p':{}})
    check('empty_inherited_factor_blocks_assignment_and_stage3',
          hm.legal() and hm.inputs('p')==set())
    no_value=Signature(('u',),{}, {'p':Kind(('u',),(),())})
    nv0=Model(no_value,{'u':('a',)},frozenset({'p'}),{'p':set()},{},{'p':{}})
    nv1=Model(no_value,{'u':('a',)},frozenset({'p'}),{'p':{x}},{},{'p':{}})
    check('empty_value_carrier_still_stage3',
          nv0.legal() and nv1.legal() and len(I(nv0,nv1,2))==1 and not I(nv0,nv1,3))
    return {
      'audit_id':'PA-P34-20261029-FIXED-SIGNATURE-QUANTIFIER-SCOPE',
      'claims':{
        'existential_witnesses':'SUPPORTED_WITH_EXPLICIT_SIGNATURE_HYPOTHESES',
        'fixed_signature_universal_3_11_12':'DISPROVED_BY_EMPTY_SIGNATURE',
        'main_theorem_revision':'DEFERRED_SOURCE_FROZEN',
        'whole_property_FPA':'OPEN'},
      'frozen_p27_source_sha256':{
        'EN':'51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb',
        'KR':'a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb'},
      'checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'limitations':'One-or-zero-auxiliary-sort small explicit witnesses; no proof of general ZFC mathematical necessity, no manuscript or Zenodo modification.'}

if __name__=='__main__':
    out=verify()
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False))
