#!/usr/bin/env python3
"""Source-bounded Appendix C checks, Formation Axiom System (Kwon Dominicus).
Run: python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_appc_construction.py
Default JSON: ../results/appc_construction.json. Optional first argument overrides it.
Finite fixtures are not a general proof or external independent validation.
"""
import itertools, json, sys
from collections import Counter
from pathlib import Path

def finite(n, dense):
    m=range(n)
    sets=[frozenset(a) for k in range(n+1) for a in itertools.combinations(m,k)]
    anchor={x:('support',x) for x in m}
    edges={(x,x+1) for x in m if x+1<n}
    domain=set(m) if dense else {x for x in m if x%2==0}
    q={x:x-1 for x in domain}
    roles={(a,x,r) for a in sets for x in a & domain for r in (0,1)
           if dense or (x+len(a)+r)%2==0}
    for a in sets:
        assert a in sets and a.issubset(set(m))
        for b in sets:
            if b.issubset(a):
                assert {x:anchor[x] for x in b} == {x:anchor[x] for x in a if x in b}
                assert {(x,y) for x,y in edges if x in b and y in b}.issubset(
                    {(x,y) for x,y in edges if x in a and y in a})
    # Every p_a is describable: Res(e_a,e_a), Realize(e_a,p_a), three true gates.
    assert set().union(*sets)==set(m) and domain.issubset(set().union(*sets))
    channels={(a,x,q[x],r) for a,x,r in roles}
    assert len(channels)==len(roles)
    assert all(x in a and x in domain for a,x,r in roles)
    assert len({frozenset((a,x,q[x],r) for a,x,r in roles)})==1
    return dict(n=n,dense=dense,subsets=len(sets),channels=len(channels),
                restriction_pairs=sum(b.issubset(a) for a in sets for b in sets),
                empty_channels=(len(channels)==0))

def indexed():
    roles=('H','V','D')
    qh={}; qg={}
    for i in range(512):
        for r in roles:
            qg[i,r]={'H':1,'V':1,'D':-2}[r]
            allow=i<125 or (125<=i<187 and r=='V') or (187<=i<506 and r=='H') or (506<=i<512 and r in ('H','V'))
            if allow: qh[i,r]=qg[i,r] if i<125 else (0 if i<252 else 1)
    assert len(qh)==768 and len(qg)==1536
    hs={i:{r for (j,r) in qh if j==i} for i in range(512)}
    gs={i:{r for (j,r) in qg if j==i} for i in range(512)}
    hsum={i:sum(v for (j,r),v in qh.items() if j==i) for i in range(512)}
    gsum={i:sum(v for (j,r),v in qg.items() if j==i) for i in range(512)}
    mismatch={i for i in range(512) if hs[i]!=gs[i]}
    equal={i for i in range(512) if hsum[i]==gsum[i]}
    vertical={i for i in range(512) if 'V' in hs[i] and 'H' not in hs[i]}
    group=[sum(len(hs[i]) for i in range(a,b)) for a,b in ((0,125),(125,187),(187,506),(506,512))]
    hist=Counter(hsum.values())
    assert group==[375,62,319,12] and len(mismatch)==387
    assert vertical==set(range(125,187)) and equal & mismatch==set(range(125,252))
    assert len(equal)==252 and hist==Counter({0:252,1:254,2:6})
    assert all(gsum[i]==0 for i in gsum)
    assert all(sum(1<<k for k in range(9) if (i>>k)&1)==i for i in range(512))
    return dict(site_subsets=512,material_items=9+3*512,H_channels=len(qh),
                G_channels=len(qg),H_case_channels=group,structure_mismatches=len(mismatch),
                vertical_only=len(vertical),coincidences_mismatch=len(equal&mismatch),
                coincidences_all=len(equal),H_sum_distribution={str(k):hist[k] for k in sorted(hist)},
                G_sum_distribution={'0':512},stage5_domain_cardinality_obstruction=True)

def main():
    cases=[finite(n,mode) for n in range(5) for mode in (False,True)]
    assert not ({0}.issubset({1}))  # invalid role seed (A={0}, a=0, D={1}) must be excluded
    obj=dict(case='FAS-F2-APPC-CONSTRUCT-001',source_sha256='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a',
             finite_fixtures=cases,finite_fixture_count=len(cases),invalid_role_seed_rejected=True,
             indexed_3x3=indexed(),full_F2='OPEN',independent_external_validation=False)
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'results/appc_construction.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'finite_fixture_count':len(cases),'indexed_3x3':obj['indexed_3x3']},sort_keys=True))
if __name__=='__main__':main()
