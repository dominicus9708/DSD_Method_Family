#!/usr/bin/env python3
"""Finite Section 4.3 witness/relation check for Formation Axiom System.

Python 3.10+ standard library only. No general proof assistant claim.
Run from DSD_Method_Family repository root:
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec43.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\sec43_witnesses.json
"""
import argparse
import json
from pathlib import Path


def admission_not_sufficient():
    # §4.3 Countermodel 4.9: the identity restriction is mandatory under Axiom II.
    return dict(material=['a'], support=['s0'],
                expressions={'x': {'mat': ['a'], 'anchor': {'a': 's0'}}},
                configurations={'p0': {'act': ['a'], 'anchor': {'a': 's0'}}},
                admission=['x'], describable=[], conf_adm=[],
                local=[], boundary=[], restrictions=[['x', 'x']], realizations=[],
                q={}, roles=[], scalar_field='R', term_space='zero')


def nontransitive_restriction():
    # Positive channel kernel g0/p, plus three distinct inert admitted expressions.
    return dict(material=['a', 'b'], support=['s0'],
                expressions={name: {'mat': [mat], 'anchor': {mat: 's0'}}
                             for name, mat in [('g0','a'), ('H','b'), ('h','b'), ('t','b')]},
                configurations={name: {'act': [mat], 'anchor': {mat: 's0'}}
                                for name, mat in [('p','a'), ('p_blocked','b'), ('p_nowitness','b')]},
                admission=['g0','H','h','t'], describable=['g0'],
                conf_adm=['p','p_nowitness'], local=['p','p_nowitness'],
                boundary=['p','p_nowitness'],
                restrictions=[['g0','g0'],['H','H'],['h','h'],['t','t'],['H','h'],['h','t']],
                realizations=[['g0','p']], q={'a': 1},
                roles=[['p','a','lambda','rho']], scalar_field='R', term_space='R')


def restrict(f, A):
    return {a:f[a] for a in A if a in f}


def validate(m):
    es, ps = m['expressions'], m['configurations']
    admitted, des = set(m['admission']), set(m['describable'])
    M = set(m['material']); B = set(m['support'])
    assert admitted <= set(es) and des <= set(es)
    for key,e in es.items():
        assert set(e['mat']) <= M and set(e['anchor']) == set(e['mat'])
        assert set(e['anchor'].values()) <= B
    for p in ps.values():
        assert set(p['act']) <= M and set(p['anchor']) == set(p['act'])
        assert set(p['anchor'].values()) <= B
    assert all(set(m[k]) <= set(ps) for k in ('conf_adm','local','boundary'))
    assert set(m['q']) <= M
    assert all(H in es and h in es for H,h in m['restrictions'])
    assert all(h in es and p in ps for h,p in m['realizations'])
    assert all(p in ps and a in M for p,a,lam,rho in m['roles'])
    assert des <= admitted  # Axiom I
    # Empty material relation signature. Inheritance of such records is vacuous.
    for H,h in m['restrictions']:
        assert set(es[h]['mat']) <= set(es[H]['mat'])
        assert es[h]['anchor'] == restrict(es[H]['anchor'], es[h]['mat'])
        assert h in admitted
    for H in admitted:
        assert [H,H] in m['restrictions']
    for h,p in m['realizations']:
        assert set(ps[p]['act']) <= set(es[h]['mat'])
        assert ps[p]['anchor'] == restrict(es[h]['anchor'], ps[p]['act'])
    conf = set(m['conf_adm']) & set(m['local']) & set(m['boundary'])
    witness = {p: [[H,h] for H,h in m['restrictions']
                   if h in des and [h,p] in m['realizations']] for p in ps}
    K = sorted(p for p in conf if witness[p])
    A = sorted(set(a for p in K for a in ps[p]['act']))
    assert set(m['q']) <= set(A)  # Axiom V; no q on inactive item
    channels = [[p,a,lam,m['q'][a],rho] for p in K for a in ps[p]['act']
                for pp,aa,lam,rho in m['roles'] if pp==p and aa==a and a in m['q']]
    if channels:
        assert m['term_space'] == 'R'
    # W={0}, T:empty ->{0} or W=R and each channel term 1.
    composites = {'empty':0,'all_channels':len(channels)}
    for x in es:
        assert (x in admitted or x not in des)  # Cor 4.8
    # Lemma 4.10: for every composable restriction pair (H,h),(h,g),
    # nested material, anchor composite, induced relations; no transitivity claimed.
    twostep=[]
    for H,h in m['restrictions']:
        for h2,g in m['restrictions']:
            if h2 != h: continue
            assert set(es[g]['mat']) <= set(es[h]['mat']) <= set(es[H]['mat'])
            assert es[g]['anchor'] == restrict(es[H]['anchor'], es[g]['mat'])
            twostep.append([H,h,g])
    # Cor 4.11: direct chain H->h->g vs all finite chains (including n=0).
    paths=[[x] for x in es]
    for _ in range(len(es)):
        paths += [path+[g] for path in list(paths) if len(path)<=len(es)
                  for h,g in m['restrictions'] if path[-1]==h and g not in path]
    for path in paths:
        H,g=path[0],path[-1]
        assert set(es[g]['mat']) <= set(es[H]['mat'])
        assert es[g]['anchor'] == restrict(es[H]['anchor'],es[g]['mat'])
    # Lemma 4.13: all restriction-realization compositions.
    material_realizations=[]
    for H,h in m['restrictions']:
        for h2,p in m['realizations']:
            if h2!=h: continue
            assert set(ps[p]['act']) <= set(es[h]['mat']) <= set(es[H]['mat'])
            assert ps[p]['anchor'] == restrict(es[H]['anchor'],ps[p]['act'])
            material_realizations.append([H,h,p])
    # Cor 4.14 both disjoint obstruction scenarios.
    for p in ps:
        if p not in conf or not witness[p]:
            assert p not in K
    return dict(axioms={'I':True,'II':True,'III':True,'V':True},
                admitted=sorted(admitted),describable=sorted(des),K_des=K,A_star=A,
                channels=channels,composites=composites,
                restriction_pairs=len(m['restrictions']),
                checked_two_step_pairs=len(twostep), checked_finite_chains=len(paths),
                checked_restriction_realization_pairs=len(material_realizations),
                not_describable_configs=sorted(set(ps)-set(K)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    cm49=admission_not_sufficient(); b49=validate(cm49)
    assert cm49['admission'] == ['x'] and not cm49['describable']
    assert ['x','x'] in cm49['restrictions'] and b49['channels']==[]
    assert b49['K_des']==[] and b49['not_describable_configs']==['p0']
    cm412=nontransitive_restriction(); b412=validate(cm412)
    assert ['H','h'] in cm412['restrictions'] and ['h','t'] in cm412['restrictions']
    assert ['H','t'] not in cm412['restrictions']
    assert b412['K_des']==['p'] and b412['A_star']==['a']
    assert b412['channels']==[['p','a','lambda',1,'rho']]
    assert sorted(b412['not_describable_configs'])==['p_blocked','p_nowitness']
    assert 'p_nowitness' in cm412['conf_adm'] and 'p_blocked' not in cm412['conf_adm']
    output=dict(audit_id='FAS-F2-SEC4.3-001', source_pdf_sha256='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a',
                source_sections=['4.8','4.9','4.10','4.11','4.12','4.13','4.14'],
                countermodel_4_9=b49, nontransitive_proposition_4_12=b412,
                proof_coverage='finite witnesses plus universal reasoning recorded separately',
                independent_external_validation=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PASS: 4.9 admitted-not-describable, identity restriction preserved')
    print('PASS: 4.12 nontransitive Res with active channel')
    print('PASS: 4.10/4.11/4.13 restricted-anchor inheritance checks')
    print('PASS: 4.8/4.14 edge and obstruction fixtures')
    print('OUTPUT:',args.output)


if __name__=='__main__': main()
