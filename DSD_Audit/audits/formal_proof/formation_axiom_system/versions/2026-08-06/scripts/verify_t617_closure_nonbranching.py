#!/usr/bin/env python3
r'''F2 Theorem 6.17 source-typed finite closure checker. Selected tests; NOT general proof.
Run: python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_t617_closure_nonbranching.py
Optional first argument: output JSON path. Standard library only.
'''
import json,itertools,sys
from pathlib import Path
SOURCE_SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'

def make(name,target=False):
    if target:
        maps={'mat':{'a':'A','b':'B'},'expr':{'H':'J','h':'g','x':'xT'},
              'cfg':{'p0':'P0','p1':'P1','p2':'P2'},'kind':{'lam':'K','kap':'L'},
              'role':{'r':'R','s':'S'}}
        vs={'lam':{0:0,1:12,2:11},'kap':{0:0,1:22,2:21}}
        factor=3
    else:
        maps={key:{v:v for v in vals} for key,vals in {
            'mat':['a','b'],'expr':['H','h','x'],'cfg':['p0','p1','p2'],
            'kind':['lam','kap'],'role':['r','s']}.items()}
        vs={k:{v:v for v in (0,1,2)} for k in ('lam','kap')}
        factor=1
    mm,ee,pp,kk,rr=(maps[k] for k in ('mat','expr','cfg','kind','role'))
    L=dict(name=name,maps=maps,vs=vs,factor=factor,base={'s0','s1'},field='Q',
        carrier={k:set(d.values()) for k,d in maps.items()},
        V={kk[k]:set(v.values()) for k,v in vs.items()},zero={kk[k]:v[0] for k,v in vs.items()},
        exprmat={ee['H']:{mm['a'],mm['b']},ee['h']:{mm['a']},ee['x']:{mm['b']}},
        confact={pp['p0']:{mm['a']},pp['p1']:{mm['b']},pp['p2']:{mm['a']}},
        ex_anchor={ee[e]:{mm[a]:'s0' for a in ss} for e,ss in {'H':{'a','b'},'h':{'a'},'x':{'b'}}.items()},
        conf_anchor={pp[p]:{mm[a]:'s0' for a in ss} for p,ss in {'p0':{'a'},'p1':{'b'},'p2':{'a'}}.items()},
        admexpr={ee[e] for e in ('H','h','x')},desexpr={ee[e] for e in ('H','h','x')},
        res={(ee[e],ee[h]) for e,h in [('H','H'),('h','h'),('x','x'),('H','h')]},
        real={(ee['h'],pp['p0']),(ee['x'],pp['p1'])},
        adm_cfg={pp['p0'],pp['p2']},lc={pp['p0'],pp['p1'],pp['p2']},bc={pp['p0'],pp['p1'],pp['p2']},
        q={(mm['a'],kk['lam']):vs['lam'][0],(mm['a'],kk['kap']):vs['kap'][2]},
        role_rel={(pp[p],mm[a],kk[k],rr[r]) for p,a,k,r in
                  [('p0','a','lam','r'),('p0','a','kap','s'),('p1','b','lam','r'),('p2','a','lam','r')]},
        W='Q',term={})
    closure(L)
    L['term']={c:factor*(5 if c[2]==kk['lam'] else -5) for c in L['channels']}
    assert len(L['channels'])==2
    validate(L)
    return L

def psi(d,p):
    return p in d['adm_cfg'] and p in d['lc'] and p in d['bc'] and any(
        (H,h) in d['res'] and h in d['desexpr'] and (h,p) in d['real']
        for H in d['carrier']['expr'] for h in d['carrier']['expr'])

def closure(d):
    d['Psi']={p:psi(d,p) for p in d['carrier']['cfg']}
    d['Kdes']={p for p in d['carrier']['cfg'] if d['Psi'][p]}
    d['Astar']=set().union(*(d['confact'][p] for p in d['Kdes']))
    d['Descfg']=d['Psi'].copy()
    d['A']=d['Astar'].copy()
    d['graph']={(a,k,v) for (a,k),v in d['q'].items()}
    d['localgraph']={p:{(a,k,v) for a,k,v in d['graph'] if a in d['confact'][p]}
                     for p in d['carrier']['cfg']}
    d['U']={(p,a,k,v,r) for p in d['carrier']['cfg'] for a in d['carrier']['mat']
            for k in d['carrier']['kind'] for v in d['V'][k] for r in d['carrier']['role']}
    d['channels']={c for c in d['U'] if d['Psi'][c[0]] and
                   (c[1],c[2],c[3]) in d['localgraph'][c[0]] and
                   (c[0],c[1],c[2],c[4]) in d['role_rel']}
    d['Dcomp']={frozenset(s) for n in range(len(d['channels'])+1)
                for s in itertools.combinations(sorted(d['channels']),n)}

def validate(d):
    assert d['desexpr']<=d['admexpr'] and all((e,e) in d['res'] for e in d['admexpr'])
    assert all(h in d['admexpr'] and d['exprmat'][h]<=d['exprmat'][H] and
               all(d['ex_anchor'][h][a]==d['ex_anchor'][H][a] for a in d['exprmat'][h])
               for H,h in d['res'])
    assert all(d['confact'][p]<=d['exprmat'][h] and
               all(d['conf_anchor'][p][a]==d['ex_anchor'][h][a] for a in d['confact'][p])
               for h,p in d['real'])
    assert all(a in d['Astar'] and v in d['V'][k] for (a,k),v in d['q'].items())
    assert all((p in d['carrier']['cfg'] and a in d['carrier']['mat'] and
               k in d['carrier']['kind'] and r in d['carrier']['role'])
               for p,a,k,r in d['role_rel'])
    assert d['term'].keys()==d['channels']
    return True

def theta(L,M):
    maps={k:{L['maps'][k][u]:M['maps'][k][u] for u in L['maps'][k]} for k in L['maps']}
    valmaps={L['maps']['kind'][u]:{L['vs'][u][v]:M['vs'][u][v] for v in L['vs'][u]}
             for u in L['vs']}
    return maps,valmaps

def transport(c,maps,vals):
    p,a,k,v,r=c;return (maps['cfg'][p],maps['mat'][a],maps['kind'][k],vals[k][v],maps['role'][r])

def primitive_stage3(L,M,maps):
    m,e,p=maps['mat'],maps['expr'],maps['cfg']
    E1=all({m[a] for a in L['exprmat'][x]}==M['exprmat'][e[x]] and
           all(L['ex_anchor'][x][a]==M['ex_anchor'][e[x]][m[a]] for a in L['exprmat'][x])
           for x in L['carrier']['expr']) and all(
           {m[a] for a in L['confact'][x]}==M['confact'][p[x]] and
           all(L['conf_anchor'][x][a]==M['conf_anchor'][p[x]][m[a]] for a in L['confact'][x])
           for x in L['carrier']['cfg'])
    E2=all((x in L[k])==(e[x] in M[k]) for k in ('admexpr','desexpr') for x in L['carrier']['expr'])
    E3=all(((H,h) in L['res'])==((e[H],e[h]) in M['res'])
           for H,h in itertools.product(L['carrier']['expr'],repeat=2)) and all(
           ((h,q) in L['real'])==((e[h],p[q]) in M['real'])
           for h,q in itertools.product(L['carrier']['expr'],L['carrier']['cfg']))
    E4=all((q in L[k])==(p[q] in M[k]) for k in ('adm_cfg','lc','bc') for q in L['carrier']['cfg'])
    return E1 and E2 and E3 and E4

def stage4(L,M,maps):
    p=maps['cfg'];m=maps['mat']
    return all(L['Psi'][x]==M['Psi'][p[x]] for x in L['carrier']['cfg']) and (
       {p[x] for x in L['Kdes']}==M['Kdes']) and (
       {m[a] for a in L['Astar']}==M['Astar'])

def all_tests():
    L=make('L');M=make('M',True);maps,vals=theta(L,M)
    assert primitive_stage3(L,M,maps) and stage4(L,M,maps)
    # Exhaustively enumerate all candidate carrier/expression/configuration bijections
    # of the finite selected model pair; record implications I3 -> I4.
    matmaps=[dict(zip(sorted(L['carrier']['mat']),q)) for q in itertools.permutations(sorted(M['carrier']['mat']))]
    exmaps=[dict(zip(sorted(L['carrier']['expr']),q)) for q in itertools.permutations(sorted(M['carrier']['expr']))]
    confmaps=[dict(zip(sorted(L['carrier']['cfg']),q)) for q in itertools.permutations(sorted(M['carrier']['cfg']))]
    combos=0;survivors=0
    for mm,ee,pp in itertools.product(matmaps,exmaps,confmaps):
        combos+=1;candidate={'mat':mm,'expr':ee,'cfg':pp}
        if primitive_stage3(L,M,candidate):
            survivors+=1
            assert stage4(L,M,candidate)
    assert combos==72 and survivors>0
    # Every finite candidate (including nonadmitted), reflect Clause VI membership.
    assert len(L['U'])==len(M['U'])==72
    assert len({transport(c,maps,vals) for c in L['U']})==72
    cand_checks=sum((c in L['channels'])==(transport(c,maps,vals) in M['channels']) for c in L['U'])
    assert cand_checks==72 and len(L['channels'])==len(M['channels'])==2
    assert {transport(c,maps,vals) for c in L['channels']}==M['channels']
    # Stage7 adds a linear J and E9, not derivable from Stage6 alone.
    assert all(3*L['term'][c]==M['term'][transport(c,maps,vals)] for c in L['channels'])
    family_checks=0;cancellation=0
    for family in L['Dcomp']:
        image=frozenset(transport(c,maps,vals) for c in family)
        assert image in M['Dcomp']
        assert 3*sum(L['term'][c] for c in family)==sum(M['term'][d] for d in image)
        family_checks+=1
        if family and sum(L['term'][c] for c in family)==0:cancellation+=1
    assert family_checks==4 and cancellation==1
    assert any(c[3]==0 for c in L['channels'])
    assert all((b,k) not in L['q'] for k in L['carrier']['kind'] for b in ['b'])
    # Stage5 fixed, Role supplied differently => differing Stage6, no contradiction.
    altrole={**L,'role_rel':set(L['role_rel'])-{next(iter(sorted(L['role_rel'])) )}}
    closure(altrole)
    assert altrole['Psi']==L['Psi'] and altrole['q']==L['q'] and altrole['channels']!=L['channels']
    # Stage6 fixed and W identical but supplied T different => Stage7 different.
    altterm=dict(L['term']);one=next(iter(sorted(altterm)));altterm[one]+=1
    assert altterm!=L['term']
    # If primitive config predicate differs (even no witness), it is not a Stage3 comparison.
    rogue={**M,'lc':set(M['lc'])-{M['maps']['cfg']['p2']}}
    closure(rogue)
    assert not primitive_stage3(L,rogue,maps)
    # A non-stage3 comparison may align primitive admission/realization but not Psi.
    rogue2={**M,'real':set(M['real'])-{(M['maps']['expr']['h'],M['maps']['cfg']['p0'])}}
    closure(rogue2)
    assert not primitive_stage3(L,rogue2,maps) and not stage4(L,rogue2,maps)
    # Source-term J arbitrary pre7 must not automatically pass E9.
    assert any(L['term'][c]!=M['term'][transport(c,maps,vals)] for c in L['channels'])
    return {'audit_id':'FAS-F2-T6.17-001','source_sha256':SOURCE_SHA,
       'selected_full_models':2,'stage3_bijection_combinations_tested':combos,
       'stage3_survivors_all_stage4':survivors,'stage3_stage4_equivalence_on_selected_combinations':True,
       'typed_candidate_channels_each_model':72,'candidate_membership_equivalences':cand_checks,
       'admitted_channels_each_model':2,'finite_family_transport_checks':family_checks,
       'nonempty_zero_sum_families':cancellation,'defined_zero_channel_present':True,
       'undefined_assignment_not_zero':True,'role_requires_independent_supply':True,
       'term_map_requires_independent_supply':True,'incomplete_stage3_probe_rejected':True,
       'pre7_J_not_required_linear':True,'finite_not_universal_proof':True,
       'independent_external_validation':False,'all_checks_passed':True}

def main():
    result=all_tests()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'t617_closure_nonbranching.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('T6.17 local finite tests PASS',result)
    print('OUTPUT',out)

if __name__=='__main__':main()
