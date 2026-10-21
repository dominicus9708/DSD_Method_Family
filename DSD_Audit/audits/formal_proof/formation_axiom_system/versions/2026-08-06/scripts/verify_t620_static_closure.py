#!/usr/bin/env python3
r"""Selected finite source-typed audit checks for F2 Theorem 6.20 (not a universal proof).
Run from cloned repository root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t620_static_closure.py
Optional first CLI argument is output JSON path. Standard library only.
"""
from itertools import product, combinations
from pathlib import Path
import json,sys
SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'

def core():
    return dict(base={'s0','s1'},field='Q',material={'a','b'},expr={'H','h','x'},cfg={'p0','p1','p2'},
      kind={'lam','nu'},roles={'r','s'},mat={'H':{'a','b'},'h':{'a'},'x':{'b'}},
      act={'p0':{'a'},'p1':{'b'},'p2':{'a'}},anch_e={'H':{'a':'s0','b':'s1'},'h':{'a':'s0'},'x':{'b':'s1'}},
      anch_p={'p0':{'a':'s0'},'p1':{'b':'s1'},'p2':{'a':'s0'}},adm_expr={'H','h','x'},
      des_expr={'h','x'},res={('H','H'),('h','h'),('x','x'),('H','h')},
      real={('h','p0'),('x','p1')},adm_cfg={'p0','p2'},lc={'p0','p1','p2'},bc={'p0','p1','p2'},
      V={'lam':{0,1,2},'nu':{0,2,3}},zero={'lam':0,'nu':0},
      q={('a','lam'):0,('a','nu'):2},role_rel={('p0','a','lam','r'),('p0','a','nu','s'),('p1','b','lam','r')},
      negligible={'lam'},size={('lam',v):abs(v) for v in (0,1,2)},delta={'lam':3})

def psi(d,p):
    return p in d['adm_cfg'] and p in d['lc'] and p in d['bc'] and any(
       (H,h) in d['res'] and h in d['des_expr'] and (h,p) in d['real']
       for H,h in product(d['expr'],repeat=2))

def trace(d,c):
    p,a,k,v,r=c
    return {(H,h,p,a,k,v,r) for H,h in d['res'] if h in d['des_expr']
      and (h,p) in d['real'] and p in d['adm_cfg'] and p in d['lc'] and p in d['bc']
      and a in d['act'][p] and d['q'].get((a,k),object())==v and (p,a,k,r) in d['role_rel']}

def closure(d,term):
    e=dict(d)
    e['Psi']={p:psi(d,p) for p in d['cfg']}
    e['Kdes']={p for p in d['cfg'] if e['Psi'][p]}
    e['Astar']=set().union(*(d['act'][p] for p in e['Kdes']))
    e['Descfg']=dict(e['Psi']);e['A']=set(e['Astar'])
    e['Gamma']={(a,k,v) for (a,k),v in d['q'].items()}
    e['U']={(p,a,k,v,r) for p,a,k,r in product(d['cfg'],d['material'],d['kind'],d['roles'])
        for v in d['V'][k]}
    e['Chan']={c:bool(e['Psi'][c[0]] and (c[1],c[2],c[3]) in e['Gamma'] and
        c[1] in d['act'][c[0]] and (c[0],c[1],c[2],c[4]) in d['role_rel']) for c in e['U']}
    e['C']={c for c in e['U'] if e['Chan'][c]}
    assert set(term)==e['C']
    e['W']='Q';e['T']=dict(term)
    e['Dcomp']={frozenset(s) for n in range(len(e['C'])+1) for s in combinations(sorted(e['C']),n)}
    e['Comp']={F:sum(e['T'][c] for c in F) for F in e['Dcomp']}
    return e

def primitive_ok(d):
    assert d['des_expr'] <= d['adm_expr']
    assert all((H,H) in d['res'] for H in d['adm_expr'])
    assert all(h in d['adm_expr'] and d['mat'][h]<=d['mat'][H] and
      all(d['anch_e'][h][a]==d['anch_e'][H][a] for a in d['mat'][h]) for H,h in d['res'])
    assert all(d['act'][p]<=d['mat'][h] and
      all(d['anch_p'][p][a]==d['anch_e'][h][a] for a in d['act'][p]) for h,p in d['real'])
    A=set().union(*(d['act'][p] for p in d['cfg'] if psi(d,p)))
    assert all(a in A and v in d['V'][k] for (a,k),v in d['q'].items())
    assert all(d['zero'][k] in d['V'][k] for k in d['kind'])
    assert all(d['size'][(k,v)]==0 if v==d['zero'][k] else d['size'][(k,v)]>0
               for k in d['negligible'] for v in d['V'][k])
    return True

def stages(e):
    blocks=[{'base':e['base'],'field':e['field'],'material':e['material'],'expr':e['expr'],
      'cfg':e['cfg'],'mat':e['mat'],'act':e['act'],'anch_e':e['anch_e'],'anch_p':e['anch_p'],
      'kind':e['kind'],'roles':e['roles'],'V':e['V'],'zero':e['zero']},
      {'adm_expr':e['adm_expr'],'des_expr':e['des_expr']},{'res':e['res']},
      {'real':e['real'],'adm_cfg':e['adm_cfg'],'lc':e['lc'],'bc':e['bc']},
      {'Psi':e['Psi'],'Astar':e['Astar'],'Descfg':e['Descfg'],'Kdes':e['Kdes'],'A':e['A']},
      {'q':e['q'],'Gamma':e['Gamma'],'negligible':e['negligible'],'size':e['size'],'delta':e['delta']},
      {'role_rel':e['role_rel'],'U':e['U'],'Chan':e['Chan'],'C':e['C']},
      {'W':e['W'],'T':e['T'],'Dcomp':e['Dcomp'],'Comp':e['Comp']}]
    return [tuple(blocks[:k+1]) for k in range(8)]

def check():
    d=core();primitive_ok(d)
    e=closure(d,{('p0','a','lam',0,'r'):5,('p0','a','nu',2,'s'):-5})
    e2=closure(d,dict(e['T']))
    assert e==e2
    assert e['Kdes']=={'p0'} and e['Astar']=={'a'}
    assert len(e['U'])==72 and len(e['C'])==2
    assert e['Comp'][frozenset()]==0 and any(F and v==0 for F,v in e['Comp'].items())
    all_iff=sum((c in e['C'])==bool(trace(e,c)) for c in e['U'])
    assert all_iff==72
    admitted_trace_sizes=sorted(len(trace(e,c)) for c in e['C'])
    assert admitted_trace_sizes==[2,2],admitted_trace_sizes
    assert ('b','lam') not in e['q'] and ('a','lam') in e['q'] and e['q'][('a','lam')]==0
    assert all(c not in e['T'] for c in e['U']-e['C'])
    s=stages(e)
    reductions=sum(int(s[k][:i+1]==s[j][:i+1] and s[j][:i+1]==s[i])
        for k in range(8) for j in range(k+1) for i in range(j+1))
    assert reductions==120 and len(s)==8
    term_alt=dict(e['T']);term_alt[('p0','a','lam',0,'r')]=7
    alt=closure(d,term_alt)
    assert stages(e)[:7]==stages(alt)[:7] and e['Comp']!=alt['Comp']
    changed=dict(d);changed['role_rel']=set(d['role_rel'])-{('p0','a','nu','s')}
    role_model=closure(changed,{('p0','a','lam',0,'r'):5})
    assert stages(e)[:6]==stages(role_model)[:6] and e['C']!=role_model['C']
    J=lambda v:2*v
    et=closure(d,{c:J(v) for c,v in e['T'].items()})
    Jtransport=sum(J(e['Comp'][F])==et['Comp'][F] for F in e['Dcomp'])
    assert Jtransport==4 and e['C']==et['C']
    return dict(case='FAS-F2-T6.20-001',source_sha256=SHA,all_checks_passed=True,
     primitive_axioms_checked=['I','II','III','V'],derived_clauses=['IV','VI','VII'],
     core_count=1,duplicate_same_input_closure_equal=True,
     candidates_trace_checked=all_iff,admitted_channels=len(e['C']),
     trace_sizes_for_admitted_channels=admitted_trace_sizes,
     defined_zero_assignment_distinct_from_undefined=True,nonadmitted_candidates_without_T=True,
     coherent_reduction_index_triples=reductions,empty_and_cancellation_composites=True,
     independent_role_changes_stage6=True,independent_T_changes_stage7=True,
     strict_identity_and_term_scaling_composites=Jtransport,
     source_previous_theorems_not_reproved_by_this_test=True,
     finite_checks_are_not_universal_proof=True,external_independent_verification=False)

def main():
    v=check()
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'t620_static_closure.json'
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('T6.20 finite static-closure check PASS:',v['candidates_trace_checked'],'candidates;',v['coherent_reduction_index_triples'],'reduction triples')
    print('OUTPUT:',p)
if __name__=='__main__': main()
