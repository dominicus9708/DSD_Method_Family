#!/usr/bin/env python3
r"""Selected finite audits of F2 Corollary 7.4, not a universal proof.

Windows, from the cloned DSD_Method_Family repository root:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c74_arbitrarily_large_finite.py
An optional first argument selects the JSON output path. Standard library only.
"""
import json
import sys
from itertools import combinations, product
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


def subsets(items):
    ordered = sorted(items)
    return [frozenset(s) for k in range(len(ordered)+1)
            for s in combinations(ordered,k)]


def model(n, field, pattern):
    assert 1 <= n <= 6 and field in ('F2','Q')
    assert pattern in ('full','partial','empty')
    M = frozenset('a'+str(i) for i in range(n))
    alpha = {a:'s' for a in M}
    powers = subsets(M)
    E = {A:('e',tuple(sorted(A))) for A in powers}
    P = {A:('p',tuple(sorted(A))) for A in powers}
    res = {(A,Z) for A,Z in product(powers,repeat=2) if Z <= A}
    realize = set(res)
    assert all((A,A) in res for A in powers)
    assert all(Z <= A and {a:alpha[a] for a in Z} ==
               {a:alpha[a] for a in A if a in Z} for A,Z in res)
    desc = {A: (A,A) in res and (A,A) in realize for A in powers}
    assert all(desc.values())
    Astar = frozenset().union(*(A for A in powers if desc[A]))
    assert Astar == M
    D = (set(M) if pattern=='full' else
         {a for a in M if int(a[1:]) % 2 == 0} if pattern=='partial' else set())
    q = {a:0 for a in D}
    gamma = {(a,0) for a in D}
    lam,rho='lam','rho'
    seed = ({(M,a,lam,rho) for a in M} if pattern=='full' else
            {(frozenset({a}),a,lam,rho) for a in D} if pattern=='partial' else set())
    assert all(a in A and a in D for A,a,k,r in seed)
    role = {(P[A],a,k,r) for A,a,k,r in seed}
    U = {(P[A],a,lam,0,rho) for A in powers for a in M}
    C = {c for c in U if frozenset(c[0][1]) in powers and
         c[1] in frozenset(c[0][1]) and (c[1],c[3]) in gamma and
         (c[0],c[1],c[2],c[4]) in role}
    expected = {(P[A],a,k,q[a],r) for A,a,k,r in seed}
    assert C == expected and len(C)==len(seed)
    # Clause VII: free F-vector space basis, finite subset sums.
    ordered = sorted(C)
    basis = {c: tuple(int(j==i) for j in range(len(C)))
             for i,c in enumerate(ordered)}
    families = [frozenset(s) for s in subsets(C)]
    comp = {family:tuple(sum(basis[c][i] for c in family)
          for i in range(len(C))) for family in families}
    assert len(families)==(1 << len(C))
    assert len(set(comp.values()))==len(families)
    assert comp[frozenset()] == tuple(0 for _ in C)
    assert all(comp[frozenset({c})]==basis[c] for c in C)
    if pattern=='full':
        assert len(C)==n and len(D)==n
    return {'n':n,'field':field,'pattern':pattern,'material':n,
        'support_size':1,'expression_count':len(E),'configuration_count':len(P),
        'restriction_pairs':len(res),'realization_pairs':len(realize),
        'globally_defined_assignment_count':len(q),'role_seed_count':len(seed),
        'candidate_channels':len(U),'admitted_channels':len(C),
        'free_vector_dimension':len(C),'finite_family_count':len(families),
        'distinct_composite_vectors':len(set(comp.values())),
        'all_source_axioms_and_closures_pass':True}


def run():
    records = [model(n,f,pattern) for n in range(1,7)
               for f in ('F2','Q') for pattern in ('full','partial')]
    records += [model(1,f,'empty') for f in ('F2','Q')]
    assert len(records)==26
    full = [r for r in records if r['pattern']=='full']
    assert all(r['expression_count']==2**r['n'] and
               r['configuration_count']==2**r['n'] and
               r['admitted_channels']==r['n'] for r in full)
    assert len({r['n'] for r in full}) == 6
    noniso_pairs = sum(n!=m for n in range(1,7) for m in range(n+1,7))
    assert noniso_pairs==15
    assert all(r['free_vector_dimension']==r['admitted_channels'] and
               r['finite_family_count']==2**r['admitted_channels']
               for r in records)
    assert all(r['admitted_channels']==r['role_seed_count'] for r in records)
    # Same cardinality does not imply equivalence: one model can have Q=M
    # while another has Q=empty; E5 disallows strict isomorphism.
    assert model(1,'F2','full')['globally_defined_assignment_count'] == 1
    assert model(1,'F2','empty')['globally_defined_assignment_count'] == 0
    return {'audit_id':'FAS-F2-C7.4-001','source_sha256':SOURCE_SHA,
        'all_checks_passed':True,'tested_model_instances':len(records),
        'material_sizes_tested':list(range(1,7)),
        'fields_tested':['F2','Q'],'patterns':['full','partial','empty_at_n1'],
        'different_material_size_nonisomorphic_pairs_per_field':noniso_pairs,
        'sum_admitted_channels':sum(r['admitted_channels'] for r in records),
        'sum_finite_families':sum(r['finite_family_count'] for r in records),
        'same_size_full_vs_empty_assignment_not_strict':True,
        'counterexample_to_anchor_injectivity_requirement':True,
        'universal_unbounded_n_argument_is_mathematical_not_finite_computation':True,
        'independent_external_validation':False,'cases':records}


def main():
    r=run()
    output = Path(sys.argv[1]) if len(sys.argv)>1 else (
        Path(__file__).resolve().parent.parent/'results'/'c74_arbitrarily_large_finite.json')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(r,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('C7.4 PASS:',r['tested_model_instances'],'finite model/field instances')
    print('OUTPUT:',output)


if __name__=='__main__':
    main()
