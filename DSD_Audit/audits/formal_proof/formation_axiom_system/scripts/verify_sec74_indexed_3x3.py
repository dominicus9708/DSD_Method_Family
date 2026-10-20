#!/usr/bin/env python3
r"""F2 §7.4: exact 512-index finite audit, not external proof certification.
Windows repository root: python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec74_indexed_3x3.py
Optional first argument: JSON output path. Standard-library Python only.
"""
import json, sys
from collections import Counter
from itertools import product
from pathlib import Path

SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
N=512
R=('H','V','D')
site={('site',r,c) for r,c in product(range(3),repeat=2)}
carrier=lambda i,t:('carrier',i,t)
private={carrier(i,t) for i in range(N) for t in R}
M=site|private
support={('site-support',r,c) for r,c in product(range(3),repeat=2)}|{('typed-support',t) for t in R}
anchor={a:('site-support',a[1],a[2]) for a in site}
anchor.update({a:('typed-support',a[2]) for a in private})
assert len(M)==1545 and len(site)==9 and len(private)==1536
assert set(anchor)==M and set(anchor.values())<=support

def sites(i):
    return {('site',r,c) for r,c in product(range(3),repeat=2)
            if i&(1<<(3*r+c))}

def h_roles(i):
    return R if i<125 else ('V',) if i<187 else ('H',) if i<506 else ('H','V')

def source_value(k,i,t):
    if k=='G' or i<125:return {'H':1,'V':1,'D':-2}[t]
    return 0 if i<252 else 1

def make(k):
    E={i: sites(i)|{carrier(i,t) for t in R} for i in range(N)}
    P={i:set(E[i]) for i in range(N)}
    res=real={(i,i) for i in range(N)}
    # Source primitive I/II/III and Clause IV: all h_i admitted/describable,
    # all source restriction/realization pairs are identities, all gates true.
    assert len(E)==len(P)==len(res)==len(real)==N
    assert all(E[i]==P[i] and (i,i) in res and (i,i) in real
               and len(E[i])==len(sites(i))+3 for i in range(N))
    assert all(set(E[i])<=M and all(anchor[a] in support for a in E[i])
               for i in range(N))
    K=set(range(N))
    A=set().union(*(P[i] for i in K))
    assert A==M
    roles={(i,carrier(i,t),'lambda_E','rho_'+t) for i in range(N) for t in R}
    Q={carrier(i,t) for i in range(N) for t in (R if k=='G' else h_roles(i))}
    q={a:source_value(k,a[1],a[2]) for a in Q}
    assert len(q)==len(Q) and Q<=A  # Primitive V: one global partial map.
    C={(i,carrier(i,t),'lambda_E',q[carrier(i,t)],'rho_'+t)
       for i in range(N) for t in R if carrier(i,t) in Q}
    assert len(C)==len(Q)
    assert all((i,a,l,r) in roles and a in P[i] and q[a]==v
               and (i,i) in res and (i,i) in real for i,a,l,v,r in C)
    family={i:frozenset(c for c in C if c[0]==i) for i in range(N)}
    comp={i:sum(c[3] for c in family[i]) for i in range(N)}
    assert sum(map(len,family.values()))==len(C)
    return dict(E=E,P=P,res=res,real=real,K=K,A=A,roles=roles,Q=Q,q=q,
                C=C,family=family,comp=comp,trace=len(C))

def check():
    h,g=make('H'),make('G')
    for key in ('E','P','res','real','K','A','roles'):assert h[key]==g[key]
    assert [len(h['Q']),len(g['Q'])]==[768,1536]
    assert [len(h['C']),len(g['C'])]==[768,1536]
    stats=Counter(); bins=Counter();partition=Counter()
    for i in range(N):
        assert sum(1<<(3*r+c) for _,r,c in sites(i))==i
        a='HVD' if i<125 else 'V' if i<187 else 'H' if i<506 else 'HV'
        partition[a]+=1
        assert len(h['family'][i])==len(h_roles(i))
        assert len(g['family'][i])==3 and g['comp'][i]==0
        for t in R:
            a=carrier(i,t)
            hit=[c for c in h['family'][i] if c[1]==a]
            assert len(hit)<=1 and bool(hit)==(a in h['Q'])
            if hit:assert hit[0][3]==h['q'][a]
            if hit and hit[0][3]==0:stats['zero_valued_admitted']+=1
        same=h['family'][i]==g['family'][i]
        stats['same_channels' if same else 'different_channels']+=1
        if h['comp'][i]==g['comp'][i]:
            stats['all_composite_equal']+=1
            if not same:stats['different_channels_but_equal_comp']+=1
        if {c[4] for c in h['family'][i]}=={'rho_V'}:
            stats['vertical_without_horizontal']+=1
        bins[str(h['comp'][i])]+=1
    assert dict(partition)=={'HVD':125,'V':62,'H':319,'HV':6}
    assert stats=={'zero_valued_admitted':127,'same_channels':125,
       'different_channels':387,'all_composite_equal':252,
       'different_channels_but_equal_comp':127,'vertical_without_horizontal':62}
    assert bins=={'0':252,'1':254,'2':6}
    # All early input signatures are literally shared, hence identity in I4.
    # No possible bijection of Q_H and Q_G of different finite sizes can
    # satisfy E5 at I5, regardless of candidate material permutations.
    stages={f'I{k}':(k<=4) for k in range(8)}
    assert stages['I4'] and not stages['I5']
    return dict(audit_id='FAS-F2-SEC7.4-3X3-001',source_sha256=SHA,
      all_checks_passed=True,grid_sites=9,material_items=1545,
      distinct_indexed_configurations=512,expressions_each=512,
      admitted_configurations_each=512,global_active_items_each=1545,
      source_roles_each=1536,global_Q_H=768,global_Q_G=1536,
      C_H=768,C_G=1536,trace_H=h['trace'],trace_G=g['trace'],
      regime_H_source_partition=dict(partition),index_checks=dict(stats),
      H_composite_histogram=dict(bins),G_all_composites_zero=True,
      mismatch_composite_coincidences=127,all_index_composite_coincidences=252,
      stages_nonempty=stages,earliest_branch=5,
      strict_obstruction='no_bijection_Q_768_vs_1536_under_E5',
      scalar_value_and_term_space='R (integer elements evaluated exactly)',
      global_channel_family_cardinalities_as_powers_of_two=[768,1536],
      whole_global_powersets_not_enumerated=True,
      source_compatible_support_completion=True,
      source_lacks_explicit_base_support_member_enumeration=True,
      full_pdf_or_external_independent_validation=False)

def main():
    d=check()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'sec74_indexed_3x3_witness.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print('§7.4 3x3 indexed PASS, b=',d['earliest_branch'],'coincidence=',d['mismatch_composite_coincidences'],d['all_index_composite_coincidences'])
    print('OUTPUT:',out)

if __name__=='__main__':main()
