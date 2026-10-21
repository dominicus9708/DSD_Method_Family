#!/usr/bin/env python3
r"""F2 T6.19 finite symmetry/representative-invariance checker (source-typed toy fixtures).
This fixture does NOT prove the universal theorem and is NOT a full Formation model census.
From the DSD_Method_Family repository root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t619_symmetry.py
Optional argument: output JSON path. Standard library only.
"""
from itertools import permutations, product
import json, sys
from pathlib import Path

SHA="8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"

def model(label, anchor="s0", adm=(0,1), restricted=False, realization=True,
          q=False, role=False, term=0, wdim=1):
    # F2 vector-space elements 0,...,2**wdim-1 with xor addition.
    return dict(label=label, material={"a"+label}, expr={"e0"+label,"e1"+label},
        cfg={"p"+label}, kind={"k"+label}, rolekind={"r"+label},
        support={"e0"+label:{"a"+label},"e1"+label:{"a"+label}},
        active={"p"+label:{"a"+label}},anchor=anchor,
        admexpr={"e"+str(i)+label for i in adm},desexpr={"e"+str(i)+label for i in adm},
        res={("e"+str(i)+label,"e"+str(i)+label) for i in adm} |
           ({("e0"+label,"e1"+label)} if restricted else set()),
        real=({("e0"+label,"p"+label)} if realization else set()),
        admcfg={"p"+label},lc={"p"+label},bc={"p"+label},
        assignment=({("a"+label,"k"+label):0} if q else {}),
        roles=({("p"+label,"a"+label,"k"+label,"r"+label)} if role else set()),
        zero={"k"+label:0},values={"k"+label:{0,1}},
        negligible={"k"+label},size={("k"+label,0):0,("k"+label,1):1},
        delta={"k"+label:1},term=term,wdim=wdim)

def psi(d,p):
    return p in d['admcfg'] and p in d['lc'] and p in d['bc'] and any(
        h in d['desexpr'] and (h,p) in d['real'] for H,h in d['res'])

def channels(d):
    return {(p,a,k,d['assignment'][(a,k)],r) for p,a,k,r in d['roles']
            if psi(d,p) and (a,k) in d['assignment']}

def bijections(A,B):
    if len(A)!=len(B):return []
    return [dict(zip(sorted(A),v)) for v in permutations(sorted(B))]

def candidates(L,M):
    sorts=[bijections(L[t],M[t]) for t in ('material','expr','cfg','kind','rolekind')]
    for fmat,fexpr,fcfg,fkind,frole in product(*sorts):
        # Both pointed spaces are the two element space {0,1}, uniquely mapped.
        value={next(iter(L['kind'])):{0:0,1:1}}
        for outcomes in product(range(1<<M['wdim']),repeat=(1<<L['wdim'])):
            yield dict(mat=fmat,expr=fexpr,cfg=fcfg,kind=fkind,role=frole,
                       value=value,J=dict(enumerate(outcomes)))

def image_channel(c,t):
    p,a,k,v,r=c
    return (t['cfg'][p],t['mat'][a],t['kind'][k],t['value'][k][v],t['role'][r])

def bits(L,M,t):
    m,e,p,k,r=(t[name] for name in ('mat','expr','cfg','kind','role'))
    E1=(all({m[a] for a in L['support'][x]}==M['support'][e[x]] for x in L['expr'])
        and all({m[a] for a in L['active'][x]}==M['active'][p[x]] for x in L['cfg'])
        and L['anchor']==M['anchor'])
    E2=all((x in L[key])==(e[x] in M[key]) for key in ('admexpr','desexpr') for x in L['expr'])
    E3r=all(((x,y) in L['res'])==((e[x],e[y]) in M['res']) for x,y in product(L['expr'],repeat=2))
    E3real=all(((x,y) in L['real'])==((e[x],p[y]) in M['real']) for x,y in product(L['expr'],L['cfg']))
    E4=all((x in L[key])==(p[x] in M[key]) for key in ('admcfg','lc','bc') for x in L['cfg'])
    E4derived=all(psi(L,x)==psi(M,p[x]) for x in L['cfg'])
    E5=all(((a,ki) in L['assignment'])==((m[a],k[ki]) in M['assignment']) for a,ki in product(L['material'],L['kind']))
    E6=all(((a,ki) in L['assignment'] and L['assignment'][(a,ki)]==v)==
           ((m[a],k[ki]) in M['assignment'] and M['assignment'][(m[a],k[ki])]==t['value'][ki][v])
           for a,ki,v in product(L['material'],L['kind'],(0,1)))
    E7=all((ki in L['negligible'])==(k[ki] in M['negligible']) and
           (ki not in L['negligible'] or (L['delta'][ki]==M['delta'][k[ki]] and
           all(L['size'][(ki,v)]==M['size'][(k[ki],t['value'][ki][v])] for v in (0,1)))) for ki in L['kind'])
    E8=all(((x,a,ki,ri) in L['roles'])==((p[x],m[a],k[ki],r[ri]) in M['roles'])
           for x,a,ki,ri in product(L['cfg'],L['material'],L['kind'],L['rolekind']))
    J=t['J']; linear=(len(set(J.values()))==len(J)==(1<<M['wdim']) and J[0]==0 and
                    all(J[x^y]==(J[x]^J[y]) for x,y in product(J,repeat=2)))
    CL,CM=channels(L),channels(M)
    E9=({image_channel(c,t) for c in CL}==CM and all(
        image_channel(c,t) in CM and J[L['term']]==M['term'] for c in CL))
    return (E1,E2,E3r,E3real and E4,E4derived,E5 and E6 and E7,E8,linear and E9)

def profile(L,M):
    ct=[0]*8;pre7_noninvertible=False;strict=False
    for t in candidates(L,M):
        b=bits(L,M,t)
        ok=True
        for j in range(8):
            ok=ok and b[j]
            ct[j]+=int(ok)
        if all(b[:7]) and len(set(t['J'].values()))!=len(t['J']):
            pre7_noninvertible=True
        strict |=all(b)
    assert all(ct[j+1]<=ct[j] for j in range(7))
    assert ct[3]==ct[4]
    first=next((j for j,n in enumerate(ct) if n==0),None)
    return dict(stage_counts=ct,b=first,pre7_noninvertible_survives=pre7_noninvertible,strict=bool(strict))

def reverse_tuple(t, L, M, final_stage=False):
    rev={key:{v:k for k,v in t[key].items()}
         for key in ('mat','expr','cfg','kind','role')}
    rev['value']={t['kind'][ki]:{v:u for u,v in vi.items()}
                  for ki,vi in t['value'].items()}
    if final_stage:
        rev['J']={v:u for u,v in t['J'].items()}
        assert len(rev['J'])==len(t['J'])
    else:
        # Source proof: arbitrary J need NOT be invertible until Stage 7.
        rev['J']={u:0 for u in range(1<<M['wdim'])}
    return rev

def test():
    cases={
      'strict_iso':(model('L'),model('M')),
      'anchor_stage0':(model('L'),model('M',anchor='s1')),
      'admission_stage1':(model('L'),model('M',adm=(0,))),
      'restriction_stage2':(model('L',restricted=True),model('M')),
      'realization_stage3':(model('L'),model('M',realization=False)),
      'assignment_stage5':(model('L',q=True),model('M')),
      'role_stage6':(model('L',q=True,role=True),model('M',q=True)),
      'term_stage7':(model('L'),model('M',wdim=2)),
      'strict_nonzero_channel':(model('L',q=True,role=True,term=1),model('M',q=True,role=True,term=1))}
    expected=dict(strict_iso=None,anchor_stage0=0,admission_stage1=1,
          restriction_stage2=2,realization_stage3=3,assignment_stage5=5,
          role_stage6=6,term_stage7=7,strict_nonzero_channel=None)
    records={};pre7_count=0;stage_equivalences=0;renamed=0;explicit_inverses=0
    for name,(L,M) in cases.items():
        f=profile(L,M);r=profile(M,L)
        for t in candidates(L,M):
            prefix=True
            for k,ok in enumerate(bits(L,M,t)):
                prefix=prefix and ok
                if prefix:
                    inv=reverse_tuple(t,L,M,final_stage=(k==7))
                    assert all(bits(M,L,inv)[:k+1]), (name,k,t,inv)
                    explicit_inverses+=1
        # Changing both representatives only renames typed carriers; anchors are FIXED.
        # The exact generated representative is determined from the SOURCE fields.
        def rep(d,label):
            old=d['label'];first='e0'+old;second='e1'+old
            return model(label,anchor=d['anchor'],adm=tuple(i for i in (0,1) if 'e'+str(i)+old in d['admexpr']),
                 restricted=(first,second) in d['res'],realization=bool(d['real']),
                 q=bool(d['assignment']),role=bool(d['roles']),term=d['term'],wdim=d['wdim'])
        La=rep(L,'X');Ma=rep(M,'Y');g=profile(La,Ma)
        assert f['b']==r['b']==g['b']==expected[name], (name,f,r,g)
        assert all((x>0)==(y>0)==(z>0) for x,y,z in zip(f['stage_counts'],r['stage_counts'],g['stage_counts']))
        assert profile(La,L)['strict'] and profile(M,Ma)['strict']
        stage_equivalences+=8;renamed+=8
        pre7_count+=int(f['pre7_noninvertible_survives'])
        records[name]={'forward':f,'reverse':r,'strict_representative_replacement':g}
    assert records['term_stage7']['forward']['stage_counts'][6]>0
    assert records['term_stage7']['reverse']['stage_counts'][6]>0
    assert records['term_stage7']['forward']['stage_counts'][7]==0
    assert records['strict_iso']['forward']['pre7_noninvertible_survives']
    assert records['strict_nonzero_channel']['forward']['strict']
    return dict(audit_id='FAS-F2-T6.19-001',source_sha256=SHA,all_checks_passed=True,
        typed_selected_cases=len(cases),stage_nonemptiness_bidirectional_checks=stage_equivalences,
        strict_representative_stage_checks=renamed,explicit_reverse_tuple_witnesses=explicit_inverses,
        pre7_noninvertible_J_examples=pre7_count,
        typed_renaming_is_strict_in_selected_fixtures=True,full_case_records=records,
        finite_not_general_proof=True,external_independent_validation=False)

def main():
    result=test();out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'t619_symmetry.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('T6.19 finite symmetric/strict representative profiles PASS:',result['typed_selected_cases'])
    print('OUTPUT:',out)

if __name__=='__main__':main()
