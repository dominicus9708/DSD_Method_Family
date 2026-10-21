#!/usr/bin/env python3
r"""Selected finite stage-comparison enumerator for F2 Theorem 6.16.

This checks selected legal-typed Formation core fixtures, not a universal proof.
The same ambient tuple population is filtered by S1-S8; J arbitrary until S8.
Run from the cloned repository root:
  python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_t616_branching.py
Optional first positional argument: output JSON path.
"""
from itertools import permutations, product
from pathlib import Path
import json, sys

SOURCE_SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


def fixture(name, **kw):
    z = dict(name=name, base={'s0','s1'}, field='F2',mat={'a'},expr={'e0','e1'},cfg={'p'},kind={'k'},rolekind={'r'},
       sup={'e0':{'a'},'e1':{'a'}},active={'p':{'a'}},anchore={'e0':{'a':'s0'},'e1':{'a':'s0'}},anchorp={'p':{'a':'s0'}},
       admexpr={'e0','e1'},desexpr={'e0','e1'},adm_cfg={'p'},lc={'p'},bc={'p'},
       res={('e0','e0'),('e1','e1')},real={('e0','p')}, q={},roles=set(),
       V={'k':{0,1}}, zero={'k':0},negligible={'k'},size={('k',0):0,('k',1):1},delta={'k':1},
       Wdim=1, term={})
    z.update(kw)
    return z


def witness(z,p):
    return p in z['adm_cfg'] and p in z['lc'] and p in z['bc'] and any(
        h in z['desexpr'] and (h,p) in z['real'] for H,h in z['res'])


def channels(z):
    return {(p,a,k,z['q'][(a,k)],r) for p,a,k,r in z['roles']
            if witness(z,p) and (a,k) in z['q']}


def core(z):
    assert z['field']=='F2' and z['base']=={'s0','s1'}
    assert z['desexpr']<=z['admexpr']<=z['expr']
    for e in z['admexpr']:
        assert (e,e) in z['res']
    for H,h in z['res']:
        assert h in z['admexpr'] and H in z['expr'] and z['sup'][h]<=z['sup'][H]
        assert all(z['anchore'][h][a]==z['anchore'][H][a] for a in z['sup'][h])
    for h,p in z['real']:
        assert z['active'][p]<=z['sup'][h]
        assert all(z['anchorp'][p][a]==z['anchore'][h][a] for a in z['active'][p])
    Astar=set().union(*(z['active'][p] for p in z['cfg'] if witness(z,p)))
    assert all(a in Astar and v in z['V'][k] for (a,k),v in z['q'].items())
    assert all((p in z['cfg'] and a in z['mat'] and k in z['kind'] and r in z['rolekind'])
        for p,a,k,r in z['roles'])
    assert set(z['term'])==channels(z) and 1<=z['Wdim']<=2
    assert all((v==0) == (z['size'][k,v]==0) for k in z['negligible'] for v in z['V'][k])
    return True


def bijections(x,y):
    if len(x)!=len(y):return []
    a,b=sorted(x),sorted(y)
    return [dict(zip(a,q)) for q in permutations(b)]


def ambient(L,M):
    # The same FULL tuples are used at every stage; J arbitrary until S8.
    sorts=[bijections(L[k],M[k]) for k in ('mat','expr','cfg','kind','rolekind')]
    if any(not t for t in sorts):return []
    result=[]
    for mm,ee,pp,kk,rr in product(*sorts):
        kindmaps=[]
        for k in sorted(L['kind']):
            source,target=sorted(L['V'][k]),sorted(M['V'][kk[k]])
            possible=[j for j in bijections(source,target)
                      if j[L['zero'][k]]==M['zero'][kk[k]]]
            kindmaps.append([(k,j) for j in possible])
        for chosen in product(*kindmaps):
            iv=dict(chosen)
            wsrc=range(1<<L['Wdim']);wtgt=range(1<<M['Wdim'])
            for vals in product(wtgt,repeat=len(wsrc)):
                result.append(dict(mm=mm,ee=ee,pp=pp,kk=kk,rr=rr,iv=iv,
                    J=dict(zip(wsrc,vals))))
    return result


def img_channel(c,t):
    p,a,k,v,r=c
    return (t['pp'][p],t['mm'][a],t['kk'][k],t['iv'][k][v],t['rr'][r])


def stage_bits(L,M,t):
    m,e,p,k,r=(t[x] for x in ('mm','ee','pp','kk','rr'))
    E1=all({m[a] for a in L['sup'][x]}==M['sup'][e[x]] and
        all(L['anchore'][x][a]==M['anchore'][e[x]][m[a]] for a in L['sup'][x])
        for x in L['expr']) and all({m[a] for a in L['active'][x]}==M['active'][p[x]] and
        all(L['anchorp'][x][a]==M['anchorp'][p[x]][m[a]] for a in L['active'][x]) for x in L['cfg'])
    E2=all((x in L[q])==(e[x] in M[q]) for q in ('admexpr','desexpr') for x in L['expr'])
    E3r=all(((u,v) in L['res'])==((e[u],e[v]) in M['res']) for u,v in product(L['expr'],repeat=2))
    E3real=all(((x,y) in L['real'])==((e[x],p[y]) in M['real']) for x,y in product(L['expr'],L['cfg']))
    E4prim=all((x in L[q])==(p[x] in M[q]) for q in ('adm_cfg','lc','bc') for x in L['cfg'])
    E4derived=all(witness(L,x)==witness(M,p[x]) for x in L['cfg'])
    E5=all(((a,ki) in L['q'])==((m[a],k[ki]) in M['q']) for a,ki in product(L['mat'],L['kind']))
    E6=all(((a,ki) in L['q'] and L['q'][(a,ki)]==v)==
        ((m[a],k[ki]) in M['q'] and M['q'][(m[a],k[ki])]==t['iv'][ki][v])
        for ki in L['kind'] for a in L['mat'] for v in L['V'][ki])
    E7=all((ki in L['negligible'])==(k[ki] in M['negligible']) and
        (ki not in L['negligible'] or (L['delta'][ki]==M['delta'][k[ki]] and all(
         L['size'][ki,v]==M['size'][k[ki],t['iv'][ki][v]] for v in L['V'][ki]))) for ki in L['kind'])
    E8=all(((x,a,ki,ri) in L['roles'])==((p[x],m[a],k[ki],r[ri]) in M['roles'])
        for x,a,ki,ri in product(L['cfg'],L['mat'],L['kind'],L['rolekind']))
    jc=t['J']
    linear=(len(set(jc.values()))==len(jc)==(1<<M['Wdim'])
        and jc[0]==0 and all(jc[x^y]==(jc[x]^jc[y]) for x,y in product(jc,repeat=2)))
    E9=all(img_channel(c,t) in channels(M) and jc[L['term'][c]]==M['term'][img_channel(c,t)]
        for c in channels(L)) and {img_channel(c,t) for c in channels(L)}==channels(M)
    sourceK={x for x in L['cfg'] if witness(L,x)}
    targetK={x for x in M['cfg'] if witness(M,x)}
    Kdes={p[x] for x in sourceK}==targetK
    return (E1,E2,E3r,E3real and E4prim,E4derived and Kdes,E5 and E6 and E7,E8,linear and E9)


def compare(L,M):
    core(L);core(M)
    population=ambient(L,M)
    levels=[set() for _ in range(8)]
    individual=[]
    for i,t in enumerate(population):
        bits=stage_bits(L,M,t)
        individual.append(bits)
        passed=True
        for st in range(8):
            passed=passed and bits[st]
            if passed:levels[st].add(i)
    assert all(levels[i+1]<=levels[i] for i in range(7))
    count=[len(x) for x in levels]
    b=next((k for k,n in enumerate(count) if n==0),None)
    assert (b is None)==bool(count[-1])
    if b is not None:
        assert all(n>0 for n in count[:b]) and all(n==0 for n in count[b:])
    assert levels[4]==levels[3], 'I3=I4 on selected full model fixture'
    return {'ambient_count':len(population),'stage_counts':count,'b':b,
            'bad_early_candidates_in_success_pair':sum(not all(bits) for bits in individual) if count[7] else 0}


def main():
    baseline=fixture('baseline')
    targets={
       'strict_iso':baseline,
       'anchor_stage0':fixture('anchor_stage0',anchore={'e0':{'a':'s1'},'e1':{'a':'s1'}},anchorp={'p':{'a':'s1'}}),
       'admission_stage1':fixture('admission_stage1',admexpr={'e0'},desexpr={'e0'},res={('e0','e0')}),
       'restriction_stage2':fixture('restriction_stage2'),
       'realization_stage3':fixture('realization_stage3',real=set()),
       'qgraph_stage5':fixture('qgraph_stage5'),
       'role_stage6':fixture('role_stage6',q={('a','k'):0}),
       'term_space_stage7':fixture('term_space_stage7',Wdim=2),
    }
    sources={key:fixture('source_'+key) for key in targets}
    sources['restriction_stage2']['res'].add(('e0','e1'))
    sources['qgraph_stage5']['q']={('a','k'):0}
    sources['role_stage6']['q']={('a','k'):0}
    sources['role_stage6']['roles']={('p','a','k','r')}
    sources['role_stage6']['term']={('p','a','k',0,'r'):0}
    cases={name:compare(sources[name],target) for name,target in targets.items()}
    expected={'strict_iso':None,'anchor_stage0':0,'admission_stage1':1,
      'restriction_stage2':2,'realization_stage3':3,'qgraph_stage5':5,
      'role_stage6':6,'term_space_stage7':7}
    assert {key:v['b'] for key,v in cases.items()}==expected, (cases,expected)
    strict=cases['strict_iso'];assert strict['stage_counts'][0]>strict['stage_counts'][-1]
    assert strict['bad_early_candidates_in_success_pair']>0
    results={'audit_id':'FAS-F2-T6.16-001','source_sha256':SOURCE_SHA,
        'typed_selected_cases':cases,'expected_first_branch':expected,
        'all_56_stage_inclusions_checked':True,
        'all_8_final_nonempty_equivalences_checked':True,
        'stage4_equals_stage3_observed_in_selected_legal_models':True,
        'strict_pair_contains_bad_individual_tuple_but_still_compatible':True,
        'full_model_exhaustiveness_not_claimed':True,
        'finite_checks_not_general_proof':True,
        'independent_external_validation':False,'all_checks_passed':True}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else (Path(__file__).resolve().parent.parent/
        'results'/'t616_first_branching.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(results,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('FAS-F2-T6.16-001 PASS: 8 cases, first indices', {k:v['b'] for k,v in cases.items()})
    print('OUTPUT',out)

if __name__=='__main__':main()
