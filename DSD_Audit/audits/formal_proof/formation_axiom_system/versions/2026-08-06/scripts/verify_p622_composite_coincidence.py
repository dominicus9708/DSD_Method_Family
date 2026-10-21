#!/usr/bin/env python3
r"""F2 P6.22: exact finite typed witness of composite coincidence with non-isomorphism.

The mathematical model has field R and W=R; Python computes only exact displayed
rational/integer term values and finite source-typed relations, not every real.
From cloned DSD_Method_Family repository root (Windows):
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_p622_composite_coincidence.py
Optional first argument overrides the result JSON path. Standard library only.
"""
from itertools import combinations
from pathlib import Path
import json
import sys

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'

def J(v):
    return v  # Prescribed id_R BEFORE choosing the compared nonempty families.

def make(label, roles, terms):
    assert set(roles) == set(terms)
    d = dict(label=label, B={'s'}, field='R', material={'a'}, expression={'h'},
             configuration={'p'}, kinds={'lambda'}, role_labels=set(roles),
             mat={'h':{'a'}}, act={'p':{'a'}},
             anchor_h={'h':{'a':'s'}}, anchor_p={'p':{'a':'s'}},
             adm_expr={'h'}, des_expr={'h'}, restrictions={('h','h')},
             realizations={('h','p')}, adm_cfg={'p'}, lc={'p'}, bc={'p'},
             V={'lambda':{0}}, zero={'lambda':0}, assignments={('a','lambda'):0},
             negligible=set(), role_rel={('p','a','lambda',r) for r in roles},
             W='R')
    d['term_values'] = dict(terms)
    return d

def witness(d,p):
    return p in d['adm_cfg'] and p in d['lc'] and p in d['bc'] and any(
       (H,h) in d['restrictions'] and h in d['des_expr'] and (h,p) in d['realizations']
       for H in d['expression'] for h in d['expression'])

def validate_primitive(d):
    # Axiom I: expression describability implies admission.
    assert d['des_expr'] <= d['adm_expr']
    # Axiom II: soundness and admitted-expression identity restriction.
    for H,h in d['restrictions']:
        assert d['mat'][h] <= d['mat'][H]
        assert all(d['anchor_h'][h][a] == d['anchor_h'][H][a] for a in d['mat'][h])
        assert h in d['adm_expr']
    assert all((h,h) in d['restrictions'] for h in d['adm_expr'])
    # Axiom III: soundness of realization and anchor restriction.
    for h,p in d['realizations']:
        assert d['act'][p] <= d['mat'][h]
        assert all(d['anchor_p'][p][a] == d['anchor_h'][h][a] for a in d['act'][p])
    # Axiom V: regime-global partial assignment with domain in A*.
    astar = set().union(*(d['act'][p] for p in d['configuration'] if witness(d,p)))
    assert all(a in astar and v in d['V'][k] for (a,k),v in d['assignments'].items())
    assert all(d['zero'][k] in d['V'][k] for k in d['kinds'])
    assert all(p in d['configuration'] and a in d['material'] and k in d['kinds']
               and r in d['role_labels'] for p,a,k,r in d['role_rel'])
    assert d['negligible'] == set()  # E7 norm/threshold demands are not triggered.
    return True

def close(d):
    validate_primitive(d)
    d['Psi'] = {p:witness(d,p) for p in d['configuration']}
    d['Kdes'] = {p for p in d['configuration'] if d['Psi'][p]}
    d['Astar'] = set().union(*(d['act'][p] for p in d['Kdes']))
    d['Descfg'] = dict(d['Psi'])
    d['A'] = set(d['Astar'])
    d['Gamma'] = {(a,k,v) for (a,k),v in d['assignments'].items()}
    d['U'] = {(p,a,k,v,r) for p in d['configuration'] for a in d['material']
              for k in d['kinds'] for v in d['V'][k] for r in d['role_labels']}
    d['C'] = {c for c in d['U'] if d['Psi'][c[0]]
              and c[1] in d['act'][c[0]] and (c[1],c[2],c[3]) in d['Gamma']
              and (c[0],c[1],c[2],c[4]) in d['role_rel']}
    d['Chan'] = {c:(c in d['C']) for c in d['U']}
    d['T'] = {c:d['term_values'][c[4]] for c in d['C']}
    assert set(d['T']) == d['C']  # Stage VII T total precisely on admitted C.
    d['Dcomp'] = {frozenset(s) for n in range(len(d['C'])+1)
                  for s in combinations(sorted(d['C']),n)}
    d['Comp'] = {F:sum(d['T'][c] for c in F) for F in d['Dcomp']}
    return d

def trace(d,c):
    p,a,k,v,r=c
    return {(H,h,p,a,k,v,r) for H,h in d['restrictions']
            if h in d['des_expr'] and (h,p) in d['realizations']
            and p in d['adm_cfg'] and p in d['lc'] and p in d['bc']
            and a in d['act'][p] and (a,k,v) in d['Gamma']
            and (p,a,k,r) in d['role_rel']}

def verify():
    # The same support/base, formation kernel, pointed value and assigned zero.
    L=close(make('L', ['rho0'], {'rho0':0}))
    M=close(make('M', ['rho_plus','rho_minus'], {'rho_plus':1,'rho_minus':-1}))
    assert L['B']==M['B'] and L['field']==M['field']=='R'
    assert L['Psi']==M['Psi']=={'p':True}
    assert L['assignments']==M['assignments']=={('a','lambda'):0}
    assert L['Gamma']==M['Gamma']=={('a','lambda',0)}
    assert len(L['C'])==1 and len(M['C'])==2
    assert all((c in d['C']) == bool(trace(d,c)) for d in (L,M) for c in d['U'])
    assert all(len(trace(d,c))==1 for d in (L,M) for c in d['C'])
    FL=frozenset(L['C'])
    FM=frozenset(M['C'])
    assert FL and FM and FL in L['Dcomp'] and FM in M['Dcomp']
    assert J(L['Comp'][FL])==M['Comp'][FM]==0
    assert J(0)==0 and J(1+(-1))==J(1)+J(-1)
    assert all(J(a+b)==J(a)+J(b) for a in range(-3,4) for b in range(-3,4))
    assert L['Comp'][frozenset()]==M['Comp'][frozenset()]==0
    assert len(L['role_labels'])==1 and len(M['role_labels'])==2
    assert len(L['C'])!=len(M['C'])  # No strict channel bijection exists.
    assert all(M['Comp'][frozenset({c})]!=0 for c in M['C'])
    assert any(v==0 for v in L['term_values'].values())
    assert all(c in d['T'] for d in (L,M) for c in d['C'])
    return dict(case_id='FAS-F2-P6.22-001',source_sha256=SOURCE_SHA,
        compared_field='R',prescribed_J='identity on R (fixed before families)',
        primitive_axioms=['I','II','III','V'],derived_clauses=['IV','VI','VII'],
        source_admitted_channels=len(L['C']),target_admitted_channels=len(M['C']),
        source_roles=len(L['role_labels']),target_roles=len(M['role_labels']),
        source_nonempty_family_size=len(FL),target_nonempty_family_size=len(FM),
        source_composite=L['Comp'][FL],target_composite=M['Comp'][FM],
        composite_equality=True,strict_isomorphism_possible=False,
        trace_membership_equivalences=len(L['U'])+len(M['U']),
        defined_zero_assignment=True,nonempty_families=True,
        empty_family_not_used_in_definition=True,
        every_target_singleton_composite_nonzero=True,
        finite_arithmetic_not_full_real_vector_space_verification=True,
        independent_external_validation=False,all_checks_passed=True)

def main():
    result=verify()
    out=(Path(sys.argv[1]) if len(sys.argv)>1 else
         Path(__file__).resolve().parent.parent/'results'/'p622_composite_coincidence.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('P6.22 finite primitive/closure/composite witness PASS:',result)
    print('OUTPUT',out)
if __name__=='__main__':main()
