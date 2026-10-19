#!/usr/bin/env python3
"""Finite typed-formation sanity witnesses for FAS-F2-T6.5-001.
NOT a universal proof or independent formal certification.
Run: python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_t65_forward_composition.py
Pass an optional output path as the first CLI argument.
"""
import json
import sys
from pathlib import Path
VALUE_SET=(0,1,2,3)

def model(level,label):
    m=tuple('abc'[:level]);e=tuple('e%d'%i for i in range(level))
    p=tuple('p%d'%i for i in range(level))
    mat={x:set(m[i:]) for i,x in enumerate(e)}
    act={x:set(m[i:]) for i,x in enumerate(p)}
    return dict(name=label,material=set(m),expr=set(e),cfg=set(p),mat=mat,act=act,
        anchor_e={x:{a:'s0' for a in mat[x]} for x in e},
        anchor_p={x:{a:'s0' for a in act[x]} for x in p},
        adm_expr=set(e),des_expr=set(e),adm_cfg=set(p),lc=set(p),bc=set(p),
        res={(x,x) for x in e},real={(x,y) for x,y in zip(e,p)},
        q={a:i+1 for i,a in enumerate(m)},
        role={('p%d'%i,a,'lambda','rho') for i,a in enumerate(m)})

def psi(m,p):
    return p in m['adm_cfg'] and p in m['lc'] and p in m['bc'] and any(
        h in m['des_expr'] and (h,p) in m['real'] for H,h in m['res'])

def channels(m):
    return {(p,a,'lambda',m['q'][a],'rho') for p,a,lam,rho in m['role']
        if psi(m,p) and a in m['act'][p] and a in m['q']}

def verify_model(m):
    assert m['des_expr']<=m['adm_expr']
    for x in m['adm_expr']:assert (x,x) in m['res']
    for H,h in m['res']:
        assert h in m['adm_expr'] and m['mat'][h]<=m['mat'][H]
        assert m['anchor_e'][h]=={a:m['anchor_e'][H][a] for a in m['mat'][h]}
    for h,p in m['real']:
        assert m['act'][p]<=m['mat'][h]
        assert m['anchor_p'][p]=={a:m['anchor_e'][h][a] for a in m['act'][p]}
    active=set().union(*(m['act'][p] for p in m['cfg'] if psi(m,p))) if m['cfg'] else set()
    assert set(m['q'])<=active and set(m['q'].values())<=set(VALUE_SET)

def phi(L,M,fm=None,fe=None,fp=None):
    fm,fe,fp=fm or {},fe or {},fp or {}
    return dict(S=L,T=M,fm={a:fm.get(a,a) for a in L['material']},
        fe={a:fe.get(a,a) for a in L['expr']},fp={a:fp.get(a,a) for a in L['cfg']})

def image_channel(f,c):
    p,a,la,v,rho=c
    return (f['fp'][p],f['fm'][a],la,v,rho)

def check_forward(f):
    L,M=f['S'],f['T'];fm,fe,fp=f['fm'],f['fe'],f['fp']
    assert set(fm.values())<=M['material'] and set(fe.values())<=M['expr'] and set(fp.values())<=M['cfg']
    for e in L['expr']:
        assert {fm[a] for a in L['mat'][e]}<=M['mat'][fe[e]]
        assert all(L['anchor_e'][e][a]==M['anchor_e'][fe[e]][fm[a]] for a in L['mat'][e])
    for p in L['cfg']:
        assert {fm[a] for a in L['act'][p]}<=M['act'][fp[p]]
        assert all(L['anchor_p'][p][a]==M['anchor_p'][fp[p]][fm[a]] for a in L['act'][p])
    for typ,cmap in [('adm_expr',fe),('des_expr',fe),('adm_cfg',fp),('lc',fp),('bc',fp)]:
        assert {cmap[x] for x in L[typ]}<=M[typ]
    assert {(fe[a],fe[b]) for a,b in L['res']}<=M['res']
    assert {(fe[a],fp[b]) for a,b in L['real']}<=M['real']
    assert all(M['q'].get(fm[a])==v for a,v in L['q'].items())
    assert {(fp[p],fm[a],la,rho) for p,a,la,rho in L['role']}<=M['role']
    assert all(image_channel(f,c) in channels(M) for c in channels(L))
    # Here I_lambda and J are identities; the supplied T(c)=10+v.
    assert all(10+c[3]==10+image_channel(f,c)[3] for c in channels(L))
    return True

def check_embedding(f):
    check_forward(f)
    L,M=f['S'],f['T'];fm,fe,fp=f['fm'],f['fe'],f['fp']
    for m in (fm,fe,fp):assert len(set(m.values()))==len(m)
    for e in L['expr']:
        assert {fm[a] for a in L['mat'][e]}==M['mat'][fe[e]]&set(fm.values())
    for p in L['cfg']:
        assert {fm[a] for a in L['act'][p]}==M['act'][fp[p]]&set(fm.values())
    for typ,cmap in [('adm_expr',fe),('des_expr',fe),('adm_cfg',fp),('lc',fp),('bc',fp)]:
        assert all((x in L[typ])==(cmap[x] in M[typ]) for x in cmap)
    for x in L['expr']:
        for y in L['expr']:
            assert ((x,y) in L['res'])==((fe[x],fe[y]) in M['res'])
    for x in L['expr']:
        for p in L['cfg']:
            assert ((x,p) in L['real'])==((fe[x],fp[p]) in M['real'])
    for a in L['material']:assert L['q'].get(a)==M['q'].get(fm[a])
    for p in L['cfg']:
        for a in L['material']:
            assert ((p,a,'lambda','rho') in L['role'])==((fp[p],fm[a],'lambda','rho') in M['role'])
        assert not psi(M,fp[p]) or psi(L,p),'witness reflection necessary'
    return True

def compose(f,g):
    assert f['T'] is g['S']
    return phi(f['S'],g['T'],{k:g['fm'][v] for k,v in f['fm'].items()},
        {k:g['fe'][v] for k,v in f['fe'].items()},
        {k:g['fp'][v] for k,v in f['fp'].items()})

def main():
    L,M,N=[model(k,name) for k,name in [(1,'L'),(2,'M'),(3,'N')]]
    for m in (L,M,N):verify_model(m)
    f=phi(L,M);g=phi(M,N);h=compose(f,g)
    assert check_embedding(f) and check_embedding(g) and check_embedding(h)
    assert check_embedding(phi(L,L))
    assert all(image_channel(h,c)==image_channel(g,image_channel(f,c)) for c in channels(L))
    C=model(2,'C_two_channels');C['q']={'a':1,'b':1}
    D=model(1,'D_one_channel')
    for m in (C,D):verify_model(m)
    c=phi(C,D,{'a':'a','b':'a'},{'e0':'e0','e1':'e0'},{'p0':'p0','p1':'p0'})
    assert check_forward(c)
    assert len(channels(C))==2 and len(channels(D))==1
    srcsum=sum(10+x[3] for x in channels(C))
    imsum=sum(10+x[3] for x in {image_channel(c,x) for x in channels(C)})
    assert srcsum==22 and imsum==11
    assert check_forward(compose(c,phi(D,M)))
    # The source is undescribable, while an extra, non-image target witness
    # produces the described target configuration; R1-R5 still hold on image.
    W=model(1,'W');W['real']=set();W['q']={};W['role']=set()
    V=model(2,'V');V['mat']['e1']={'a','b'}
    V['anchor_e']['e1']={'a':'s0','b':'s0'}
    V['real']={('e1','p0')};V['q']={'b':2}
    V['role']={('p0','b','lambda','rho')}
    for m in (W,V):verify_model(m)
    w=phi(W,V)
    assert check_forward(w)
    expected_failure=False
    try:check_embedding(w)
    except AssertionError as e:expected_failure='witness reflection necessary' in str(e)
    assert expected_failure
    result={
        'audit_id':'FAS-F2-T6.5-001',
        'source_sha256':'8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a',
        'all_fixture_assertions_passed':True,
        'finite_test_not_universal_proof':True,
        'nested_embeddings_L_M_N':True,
        'identity_embedding':True,
        'two_step_embedding_composition':True,
        'channel_composition_identity':True,
        'noninjective_forward_composition':True,
        'noninjective_source_channels':2,
        'noninjective_target_channels':1,
        'noninjective_source_composite':srcsum,
        'noninjective_image_composite':imsum,
        'image_intersection_r1_tested':True,
        'witness_reflection_not_redundant':True}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'t65_forward_composition.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('T6.5 finite witnesses PASS: identity, embeddings, composition, noninjective boundary, witness reflection')
    print('OUTPUT:',out)
if __name__=='__main__':main()
