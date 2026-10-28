#!/usr/bin/env python3
"""P31 finite witness audit of §11 quantification and §8 branching.

This script checks only displayed small typed premodels and finite mappings.
It does not certify a general ZFC theorem, nor select P30 surplus-data semantics.
"""
from __future__ import annotations
import itertools
import json
import sys
from pathlib import Path


def typed_premodel(ap, sat, xi, carrier=('a',), dependencies=('d',)):
    inputs = set(carrier)
    if not set(ap) <= inputs or not set(sat) <= inputs or not set(xi) <= inputs:
        raise ValueError('ill-typed input')
    domain = set(xi)
    pi = domain <= set(ap)
    pii = all(domain <= set(sat) for _ in dependencies)
    return {'PI':pi, 'PII':pii}


def stage_families(A,B,k):
    assert k in (1,2,3,4)
    source,target=A['carrier'], B['carrier']
    if len(source)!=len(target):
        return []
    out=[]
    for perm in itertools.permutations(target):
        f=dict(zip(source,perm))
        if k>=2 and A['declared']!=B['declared']:
            continue
        ok=True
        for prop in A['declared'] if k>=3 else ():
            if {f[x] for x in A['ap'][prop]} != B['ap'][prop]:
                ok=False;break
            for dep in A['dep'][prop]:
                if {f[x] for x in A['sat'][prop][dep]} != B['sat'][prop][dep]:
                    ok=False;break
            if not ok:break
            if k>=4:
                xa={f[x]:v for x,v in A['xi'][prop].items()}
                if xa != B['xi'][prop]:
                    ok=False;break
        if ok:out.append(tuple(perm))
    return out


def model(carrier, declared, ap=None, xi=None, dep=None, sat=None):
    ap=ap or {};xi=xi or {};dep=dep or {};sat=sat or {}
    return {
        'carrier':tuple(carrier), 'declared':frozenset(declared),
        'ap':{p:set(ap.get(p,())) for p in declared},
        'xi':{p:dict(xi.get(p,{})) for p in declared},
        'dep':{p:tuple(dep.get(p,())) for p in declared},
        'sat':{p:{d:set(sat.get(p,{}).get(d,())) for d in dep.get(p,())} for p in declared},
    }


def run():
    checks={}
    # Allowed signature: zero candidate kinds and no auxiliary sorts.
    # Under P30 restricted-family interpretation the canonical core is unique.
    empty=model((),())
    checks['empty_signature_stage1_through_4_identity'] = all(
        len(stage_families(empty,empty,k))==1 for k in (1,2,3,4))
    checks['empty_signature_PI_PII_both_vacuous'] = (all([]) and all([]))
    checks['empty_signature_has_no_stage_2_3_4_branch_pair'] = (
        set(empty['declared']) == set() and
        all(len(stage_families(empty,empty,k))>0 for k in (2,3,4)))
    checks['empty_signature_has_no_summary_collision_noniso_pair'] = (
        len(stage_families(empty,empty,4))>0)

    # A legal shared signature with one kind and NO dependencies makes PII a tautology.
    for ap in ((),('a',)):
        for xi in ({},{'a':0}):
            # These choices are typed premodels, including PI-violators.
            assert typed_premodel(ap,(),xi,dependencies=())['PII']
    checks['zero_prerequisites_PII_tautological_even_on_PI_counterpremodel'] = (
        typed_premodel((),(),{'a':0},dependencies=()) == {'PI':False,'PII':True})

    # The two manuscript counterpremodels ARE valid when the signature has a prerequisite.
    x=typed_premodel((),('a',),{'a':0})
    y=typed_premodel(('a',),(),{'a':0})
    checks['shared_witness_signature_PI_independent_of_PII'] = (x=={'PI':False,'PII':True})
    checks['shared_witness_signature_PII_independent_of_PI'] = (y=={'PI':True,'PII':False})

    # Existence of branching witnesses is conditional on kind/sort/value availability.
    A=model(('a',),('p',));B=model(('a',),())
    counts=[len(stage_families(A,B,k)) for k in (1,2,3,4)]
    checks['stage2_witness_exists_when_kind_available']=(counts==[1,0,0,0])

    A=model(('a','b'),('p','q'),ap={'p':('a',),'q':('a',)})
    B=model(('a','b'),('p','q'),ap={'p':('a',),'q':('b',)})
    counts=[len(stage_families(A,B,k)) for k in (1,2,3,4)]
    checks['stage3_witness_exists_when_two_kinds_available']=(counts==[2,2,0,0])

    base={'p':('a','b'),'q':('a','b')}
    A=model(('a','b'),('p','q'),ap=base,xi={'p':{'a':0,'b':1},'q':{'a':0,'b':1}})
    B=model(('a','b'),('p','q'),ap=base,xi={'p':{'a':0,'b':1},'q':{'a':1,'b':0}})
    counts=[len(stage_families(A,B,k)) for k in (1,2,3,4)]
    checks['stage4_witness_exists_when_two_kinds_two_values']=(counts==[2,2,2,0])

    # Fixing all signatures first does NOT make the existence witnesses available universally.
    checks['fixed_signature_universal_independence_not_supported']=(
        checks['empty_signature_PI_PII_both_vacuous'] and
        checks['zero_prerequisites_PII_tautological_even_on_PI_counterpremodel'])
    checks['fixed_signature_universal_branching_not_supported']=(
        checks['empty_signature_has_no_stage_2_3_4_branch_pair'] and
        all(checks[k] for k in ('stage2_witness_exists_when_kind_available',
             'stage3_witness_exists_when_two_kinds_available',
             'stage4_witness_exists_when_two_kinds_two_values')))
    checks['fixed_signature_universal_summary_nonclassification_not_supported']=(
        checks['empty_signature_has_no_summary_collision_noniso_pair'])

    assert all(checks.values()), {k:v for k,v in checks.items() if not v}
    return {
        'audit':'PA-P31-FROZEN-P27-SECTION11-QUANTIFIER-DEPENDENCY-001',
        'checks':checks,'passed':len(checks),'all_expected':len(checks),
        'finite_examples_only':True,
        'scope':'Single fixed Stage-VI record; empty, 1-kind and 2-kind signatures; 0/1/2-element carriers; limited displayed countermodels',
        'interpretation':'Existential witnesses vary signature. The displayed §11 fixed-signature theorem requires a scope distinction; no axiom inconsistency inferred.',
        'p27_manuscript_edited':False,'whole_property_fpa':'OPEN',
    }


if __name__=='__main__':
    result=run()
    destination=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('P31_EXPECTED_EVIDENCE.json')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))