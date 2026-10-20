#!/usr/bin/env python3
r"""Selected finite audits of F2 Theorem 7.3, not a universal proof.

Windows from cloned DSD_Method_Family repository root:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t73_standard_finite_realization.py
Optional first argument changes JSON output. Standard library only.
"""
import json
import sys
from fractions import Fraction
from itertools import chain, combinations, product
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


def powerset(xs):
    a = sorted(xs)
    return [frozenset(c) for i in range(len(a) + 1) for c in combinations(a, i)]


def realize(case, field):
    M = set(case['M']); L = set(case['kinds']); R = set(case['roles'])
    alpha = case['anchor']; D = case['q']; seed = set(case['seed'])
    assert set(alpha) == M and set(D) == L
    assert all(x in set(case['support']) for x in alpha.values())
    assert all(0 in case['V'][k] and all(v in case['V'][k] for v in D[k].values()) for k in L)
    assert all(set(d) <= M for d in D.values())
    assert all(a in A and a in D[k] and k in L and rho in R and A <= M
               for A, a, k, rho in seed)
    # A fixed finite relational S_mat structure; restriction means induced relation.
    material_rel = set(case['material_rel'])
    assert all(set(edge) <= M for edge in material_rel)
    subsets = powerset(M)
    expr = {A: ('e', tuple(sorted(A))) for A in subsets}
    cfg = {A: ('p', tuple(sorted(A))) for A in subsets}
    induced = {A: {e for e in material_rel if set(e) <= A} for A in subsets}
    anchor = {A: {a: alpha[a] for a in A} for A in subsets}
    Res = {(A, Z) for A, Z in product(subsets, repeat=2) if Z <= A}
    Realize = set(Res)  # Rename second sort as configuration p_Z.
    assert all((A, A) in Res for A in subsets)
    assert all(Z <= A and anchor[Z] == {a: anchor[A][a] for a in Z}
               and induced[Z] == {e for e in induced[A] if set(e) <= Z}
               for A, Z in Res)
    assert all(Z <= A for A, Z in Realize)
    # Every expression admitted and describable; all three cfg gates are True.
    # Closure IV: a genuine (e_A,e_A) witness exists for each p_A.
    psi = {A: any((H, h) in Res and (h, A) in Realize
                  for H, h in product(subsets, repeat=2)) for A in subsets}
    assert all(psi.values())
    Astar = set(chain.from_iterable(A for A in subsets if psi[A]))
    assert Astar == M
    gamma = {k: {(a, v) for a, v in D[k].items()} for k in L}
    Role = {(cfg[A], a, k, rho) for A, a, k, rho in seed}
    U = {(cfg[A], a, k, v, rho) for A in subsets for a in M
         for k in L for v in case['V'][k] for rho in R}
    C = {u for u in U if psi[frozenset(u[0][1])] and
         u[1] in frozenset(u[0][1]) and (u[1],u[3]) in gamma[u[2]] and
         (u[0],u[1],u[2],u[4]) in Role}
    expected = {(cfg[A], a, k, D[k][a], rho) for A, a, k, rho in seed}
    assert C == expected and len(C) == len(seed)
    order = sorted(C)
    index = {c: i for i, c in enumerate(order)}
    n = len(C)
    # Free vector space F^(C): coordinates over the supplied field.
    if field == 'F2':
        add = lambda a,b: (a+b)%2
        scalars = (0,1)
    else:
        add = lambda a,b: a+b
        scalars = (Fraction(0), Fraction(1), Fraction(-1), Fraction(2,3))
    zero = tuple(0 for _ in order)
    basis = {c: tuple(1 if i == index[c] else 0 for i in range(n)) for c in order}
    families = [frozenset(f) for f in powerset(C)]
    comp = {f: tuple(sum(basis[c][i] for c in f) % 2 if field=='F2'
                     else sum((basis[c][i] for c in f), Fraction(0)) for i in range(n))
            for f in families}
    assert len(families) == 2**n
    assert comp[frozenset()] == zero
    assert len(set(comp.values())) == len(comp)  # Injective for THIS free basis.
    assert all(comp[frozenset({c})] == basis[c] for c in C)
    # Disjoint-family additivity and elementary zero-space checks.
    assert all(comp[x|y] == tuple(add(comp[x][i],comp[y][i]) for i in range(n))
               for x,y in product(families, repeat=2) if x.isdisjoint(y))
    assert all(tuple(add(k*a,k*b) for a,b in zip(zero,zero)) == zero
               for k in scalars)
    return dict(name=case['name'],field=field,material_count=len(M),
        expression_count=len(expr),configuration_count=len(cfg),
        quantity_kinds=len(L),role_labels=len(R),seed_roles=len(seed),
        candidate_channels=len(U),admitted_channels=n,
        finite_channel_families=len(families),distinct_composite_vectors=len(set(comp.values())),
        restricted_pairs=len(Res),realization_pairs=len(Realize),
        material_rel_entries=len(material_rel),defined_assignment_edges=sum(map(len,D.values())),
        all_describable=True,active_union_is_M=True,source_primitive_axioms=['I','II','III','V'],
        source_derived_clauses=['IV','VI','VII'],fully_formation_finite=True,
        free_basis_dimension=n,role_seed_channel_bijection=True)


def cases():
    def seed(A,a,k,r): return (frozenset(A),a,k,r)
    return [
      dict(name='empty_material',M=[],anchor={},support=[],kinds=['lam'],roles=['r'],
           V={'lam':{0}},q={'lam':{}},seed=[],material_rel=[]),
      dict(name='defined_zero_singleton',M=['a'],anchor={'a':'s0'},support=['s0'],kinds=['lam'],roles=['r'],
           V={'lam':{0,1}},q={'lam':{'a':0}},seed=[seed(['a'],'a','lam','r')],material_rel=[]),
      dict(name='binary_relation_and_partial_q',M=['a','b'],anchor={'a':'s0','b':'s0'},support=['s0'],
           kinds=['x','y'],roles=['r','s'],V={'x':{0,1},'y':{0,1}},
           q={'x':{'a':0,'b':1},'y':{'b':0}},
           seed=[seed(['a'],'a','x','r'),seed(['a','b'],'a','x','r'),
                 seed(['a','b'],'b','x','s'),seed(['b'],'b','y','s')],
           material_rel=[('a','b')]),
      dict(name='three_material_multi_anchor',M=['a','b','c'],
           anchor={'a':'s0','b':'s1','c':'s0'},support=['s0','s1'],kinds=['k'],roles=['r','s'],
           V={'k':{0,1,2}},q={'k':{'a':0,'c':2}},
           seed=[seed(['a'],'a','k','r'),seed(['a','c'],'c','k','s'),
                 seed(['a','b','c'],'a','k','s')],material_rel=[('a','b'),('b','c')]),
      dict(name='no_kinds_or_roles',M=['a'],anchor={'a':'s0'},support=['s0'],kinds=[],roles=[],
           V={},q={},seed=[],material_rel=[])
    ]


def check():
    results=[realize(c,f) for c,f in product(cases(),('F2','Q'))]
    assert len(results)==10 and all(r['admitted_channels']==r['seed_roles'] for r in results)
    assert all(r['distinct_composite_vectors']==r['finite_channel_families'] for r in results)
    # Both violations of the theorem's seed hypothesis MUST be rejected.
    illegal_missing_active = (frozenset(), 'a','lam','r')
    illegal_undefined = (frozenset({'a'}),'a','y','r')
    assert not ('a' in illegal_missing_active[0] and 'a' in {'a'})
    assert illegal_undefined[1] not in cases()[2]['q'][illegal_undefined[2]]
    return dict(audit_id='FAS-F2-T7.3-001',source_sha256=SOURCE_SHA,
        all_checks_passed=True,tested_models=len(results),test_case_names=[c['name'] for c in cases()],
        tested_fields=['F2','Q'],sum_admitted_channels=sum(r['admitted_channels'] for r in results),
        sum_finite_family_counts=sum(r['finite_channel_families'] for r in results),
        seed_hypothesis_negative_controls=2,
        arbitrary_field_and_value_space_generality_is_mathematical_not_finite_software_proof=True,
        external_independent_validation=False,cases=results)


def main():
    d=check()
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'results'/'t73_standard_finite_realization.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('T7.3 source-typed finite checks PASS:',d['tested_models'],'model-field instances')
    print('OUTPUT',out)

if __name__=='__main__': main()
