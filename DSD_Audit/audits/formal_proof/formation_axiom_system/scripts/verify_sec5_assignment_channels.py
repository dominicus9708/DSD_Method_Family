#!/usr/bin/env python3
"""FAS-F2-G3-SEC5-001: finite typed-source fixtures for Section 5.

Independent mathematics is written in the accompanying result; finite assertions
are not proof of universally quantified original propositions.

Windows 11 from root of repository:
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec5_assignment_channels.py
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

SOURCE_SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
LAMBDA='lambda'
ZERO=Fraction(0)


def form_model(material, values, roles, terms, *, describable=True):
    """One-describable-configuration full typed Formation instance.

    materials: tuple; values: partial one-regime-global q with codomain Q;
    roles: (material, role) pairs; terms: (material, role)->rational W vector.
    Full source validity is checked for all generated primitive/derived data.
    """
    M=tuple(material)
    assert len(set(M))==len(M)
    assert set(values)<=set(M)
    assert set(roles)<=set(itertools.product(M,{r for _,r in roles}))
    assert all(a in values and (a,r) in roles for a,r in terms)
    assert len({(a,r) for a,r in roles})==len(roles)
    expr='h'; cfg='p'; support='s'; E={expr}; P={cfg}
    mat={expr:frozenset(M)}; active={cfg:frozenset(M)}
    anch_expr={a:support for a in M}; anch_cfg=dict(anch_expr)
    admexpr={expr:True}; desexpr={expr:describable}
    restrictions={(expr,expr)}
    realizations={(expr,cfg)}
    gates={cfg:(True,True,True)}
    assert (not desexpr[expr] or admexpr[expr])
    assert all(mat[h]<=mat[H] and {a:anch_expr[a] for a in mat[h]}==anch_expr
               for H,h in restrictions)
    assert all(active[p]<=mat[h] and anch_cfg=={a:anch_expr[a] for a in active[p]}
               for h,p in realizations)
    assert all(not admexpr[h] or (h,h) in restrictions for h in E)
    Psi={p:any((H,h) in restrictions and desexpr[h] and (h,p) in realizations
               and all(gates[p]) for H,h in restrictions) for p in P}
    K={p for p in P if Psi[p]}
    Astar=set().union(*(active[p] for p in K)) if K else set()
    assert set(values)<=Astar  # Primitive Axiom V
    q=dict(values)
    Q=set(q)
    local_Q={p:Q&set(active[p]) for p in K}
    local_graph={p:{(a,q[a]) for a in local_Q[p]} for p in K}
    roles_full={(cfg,a,LAMBDA,r) for a,r in roles}
    chan={(p,a,LAMBDA,v,r) for p in K for a,v in local_graph[p]
          for pp,aa,ll,r in roles_full if p==pp and a==aa and ll==LAMBDA}
    assert all(a in Q and v==q[a] and p in K and (p,a,LAMBDA,r) in roles_full
               for p,a,_,v,r in chan)
    T={(p,a,LAMBDA,v,r):Fraction(terms.get((a,r),0)) for p,a,_,v,r in chan}
    def comp(family):
        F=set(family)
        assert F<=chan
        return sum((T[c] for c in F),ZERO)
    assert comp(set())==ZERO
    return {'materials':M,'Q':Q,'q':q,'K':K,'Astar':Astar,'C':chan,
            'U':{(p,a,LAMBDA,v,r) for p in P for a in M for v in (ZERO,Fraction(1,4),Fraction(2))
                 for r in ('r1','r2','r3','absent')},
            'T':T,'Comp':comp,'witness_count':sum(Psi.values()),'roles':roles_full,
            'local_graph':local_graph,'local_Q':local_Q,'act':active,'mat':mat}


def audit_status():
    M=('zero','small','large','missing')
    q={'zero':ZERO,'small':Fraction(1,4),'large':Fraction(2)}
    roles={('zero','r1'),('zero','r2'),('zero','r3'),('small','r1'),('missing','r1')}
    terms={('zero','r1'):1,('zero','r2'):-1,('zero','r3'):0,('small','r1'):0}
    a=form_model(M,q,roles,terms)
    p='p'; Q=a['local_Q'][p]
    U=set(M)-Q
    Z={x for x in Q if q[x]==0}
    N={x for x in Q if q[x]!=0 and abs(q[x])<=1}
    B={x for x in Q if q[x]!=0 and abs(q[x])>1}
    assert (U,Z,N,B)==({'missing'},{'zero'},{'small'},{'large'})
    assert U.isdisjoint(Z) and U.isdisjoint(N) and Z.isdisjoint(N)
    assert set.union(U,Z,N,B)==set(M)
    assert set.union(U,Z,N)!=set(M) # the statuses need not exhaust
    # q is genuinely partial; z receives 0 while missing x does not receive a value.
    assert 'missing' not in a['q']
    padded={x:q.get(x,ZERO) for x in M}
    assert padded['missing']==padded['zero']==ZERO
    assert ('p','zero',LAMBDA,ZERO,'r1') in a['C']
    assert ('p','zero',LAMBDA,ZERO,'r2') in a['C']
    assert ('p','zero',LAMBDA,ZERO,'r3') in a['C']
    assert ('p','small',LAMBDA,Fraction(1,4),'r1') in a['C']
    assert not any(c[1] in ('missing','large') for c in a['C'])
    return {'assignment_status':{'undefined':len(U),'defined_zero':len(Z),
                                 'defined_nonzero_small':len(N),'defined_nonzero_large':len(B)},
            'nonexhaustive_U_Z_N':True,'zero_padding_collision':True,
            'role_multiplicity_distinct_channels':3,'defined_zero_supports_channels':True,
            'defined_nonzero_without_role_gives_no_channel':True,
            'undefined_even_with_role_gives_no_channel':True,'channels':len(a['C'])}


def audit_empty_q_and_undefined_term():
    a=form_model(('a',),{},set(),{})
    assert a['K']=={'p'} and a['Astar']=={'a'} and len(a['C'])==0
    assert a['Comp'](set())==ZERO
    assert 'p' in a['K'] and 'a' not in a['Q']
    assert len(a['U'])>0
    assert all(c not in a['T'] for c in a['U'])
    b=form_model(('a',),{'a':ZERO},set(),{})
    assert b['K'] and not b['C'] # defined assignment without role
    return {'describable_without_assignment':True,'describable_without_channels':True,
            'empty_channels_composable_families':1,'empty_composite_is_defined_zero':True,
            'absent_term_is_undefined':True,'defined_value_without_role_no_channel':True}


def audit_noninjective():
    a=form_model(('a',),{'a':ZERO},{('a','r1'),('a','r2'),('a','r3')},
                 {('a','r1'):1,('a','r2'):-1,('a','r3'):0})
    c1=('p','a',LAMBDA,ZERO,'r1'); c2=('p','a',LAMBDA,ZERO,'r2');c3=('p','a',LAMBDA,ZERO,'r3')
    assert a['C']=={c1,c2,c3}
    f1={c1,c2};f2={c3}
    assert f1!=f2 and a['Comp'](f1)==a['Comp'](f2)==ZERO
    allfamily=[frozenset(x for k,x in enumerate((c1,c2,c3)) if mask&(1<<k))
               for mask in range(8)]
    values={f:a['Comp'](f) for f in allfamily}
    collisions=sum(values[u]==values[v] for i,u in enumerate(allfamily) for v in allfamily[i+1:])
    assert collisions>0
    return {'source_F1_distinct_F2':f1!=f2,'F1_sum':'0','F2_sum':'0',
            'channel_count':len(a['C']),'finite_families_enumerated':len(allfamily),
            'unordered_distinct_family_equal_composite_pairs':collisions}


def audit_zero_extension_nuance():
    # Collision is genuine if both the absent candidate and admitted zero term exist.
    a=form_model(('a',),{'a':ZERO},{('a','r1')},{('a','r1'):0})
    ca=('p','a',LAMBDA,ZERO,'r1'); missing=('p','a',LAMBDA,ZERO,'absent')
    assert ca in a['C'] and a['T'][ca]==ZERO and missing in a['U']-a['C']
    pad=lambda model,c:model['T'].get(c,ZERO)
    assert pad(a,ca)==pad(a,missing)==ZERO
    # Legal full model with absent channels but *every admitted term nonzero*.
    b=form_model(('a',),{'a':ZERO},{('a','r1')},{('a','r1'):1})
    assert ca in b['C'] and missing in b['U']-b['C']
    assert all(b['T'][c]!=ZERO for c in b['C'])
    assert all((pad(b,c)!=ZERO)==(c in b['C']) for c in b['U'])
    # A nonzero-valued admitted assignment is allowed to have zero component term;
    # term-zero and quantity-zero are logically independent.
    c=form_model(('a',),{'a':Fraction(2)},{('a','r1')},{('a','r1'):0})
    assert any(channel[3]!=ZERO and c['T'][channel]==ZERO for channel in c['C'])
    return {'absent_plus_admitted_zero_collision':True,
            'legal_countermodel_with_zero_extension_value_detecting_membership':True,
            'zero_term_need_not_have_zero_assignment':True,
            'status_of_source_prop_5_13':'conditional interpretation valid; blanket universal loses-membership claim needs explicit qualification'}


def main():
    output={'case':'FAS-F2-G3-SEC5-001','source_sha256':SOURCE_SHA,
            'source_items':{'definition':1,'propositions':10,'corollaries':2,'countermodels':1},
            'assignment_status':audit_status(),
            'empty_domain_and_empty_channels':audit_empty_q_and_undefined_term(),
            'noninjective_composition':audit_noninjective(),
            'zero_extension_scope':audit_zero_extension_nuance(),
            'evidence_scope':'selected full typed 1-configuration models plus all 2^3 finite channel subsets; not arbitrary model proof',
            'external_independent_validation':False,'whole_F2':'OPEN'}
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'results/sec5_assignment_channels.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(output,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status_channels':output['assignment_status']['channels'],
                      'composite_family_count':output['noninjective_composition']['finite_families_enumerated'],
                      'collisions':output['noninjective_composition']['unordered_distinct_family_equal_composite_pairs'],
                      'prop5_13_countermodel':output['zero_extension_scope']['legal_countermodel_with_zero_extension_value_detecting_membership']},sort_keys=True))
if __name__=='__main__':main()
