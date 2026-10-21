#!/usr/bin/env python3
r"""Source-typed selected checks for F2 Theorem 7.1 (not a universal proof).

Windows at cloned DSD_Method_Family root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t71_full_model_existence.py
Optional first argument chooses output JSON path. Standard library only.
"""
from itertools import product, combinations
from fractions import Fraction
from pathlib import Path
import hashlib, json, sys

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
VALUE_ZERO = ('V_lambda', '0')
TERM_ZERO = ('W', '0')
assert VALUE_ZERO != TERM_ZERO  # Typed zeros need not be equal as objects.


def construct(field, support, assign=True):
    assert field in ('F2', 'Q') and len(support) > 0
    anchor = sorted(support)[0]
    d = dict(field=field, B=set(support), material={'a'}, expr={'h'}, cfg={'p'},
             signature=set(), material_relations=set(),
             mat={'h': {'a'}}, act={'p': {'a'}},
             anch_e={'h': {'a': anchor}}, anch_p={'p': {'a': anchor}},
             adm_expr={'h'}, des_expr={'h'}, res={('h', 'h')},
             real={('h', 'p')}, adm_cfg={'p'}, lc={'p'}, bc={'p'},
             kind={'lambda'}, V={'lambda': {VALUE_ZERO}},
             distinguished_zero={'lambda': VALUE_ZERO},
             negligible=set(), role={'rho'},
             role_rel={('p', 'a', 'lambda', 'rho')})
    # All primitives are source-typed and set-sized; no hidden material relations.
    assert d['des_expr'] <= d['adm_expr']   # Primitive Axiom I
    assert all((h, h) in d['res'] for h in d['adm_expr'])
    assert all(h in d['adm_expr'] and d['mat'][h] <= d['mat'][H] and
               all(d['anch_e'][h][a] == d['anch_e'][H][a] for a in d['mat'][h])
               for H, h in d['res'])     # Primitive Axiom II
    assert all(d['act'][p] <= d['mat'][h] and
               all(d['anch_p'][p][a] == d['anch_e'][h][a] for a in d['act'][p])
               for h, p in d['real'])    # Primitive Axiom III
    assert all(v in d['B'] for h in d['expr'] for v in d['anch_e'][h].values())
    # Exact source witness for Psi; Closure IV is its deterministic expansion.
    d['psi'] = {p: (p in d['adm_cfg'] and p in d['lc'] and p in d['bc'] and
                    any((H, h) in d['res'] and h in d['des_expr'] and
                        (h, p) in d['real'] for H, h in product(d['expr'], repeat=2)))
                for p in d['cfg']}
    d['des_cfg'] = dict(d['psi'])
    d['Kdes'] = {p for p in d['cfg'] if d['des_cfg'][p]}
    d['Astar'] = set().union(*(d['act'][p] for p in d['Kdes']))
    d['A'] = set(d['Astar'])
    d['Q'] = {'lambda': {'a'} if assign else set()}
    d['q'] = {('a', 'lambda'): VALUE_ZERO} if assign else {}
    assert all(Q <= d['Astar'] for Q in d['Q'].values())   # Primitive Axiom V
    assert all(a in d['Q'][k] and v in d['V'][k] for (a, k), v in d['q'].items())
    assert all(d['distinguished_zero'][k] in d['V'][k] for k in d['kind'])
    d['gamma'] = {k: {(a, d['q'][(a, k)]) for a in d['Q'][k]} for k in d['kind']}
    d['U'] = {(p, a, k, v, rho) for p in d['cfg'] for a in d['material']
              for k in d['kind'] for v in d['V'][k] for rho in d['role']}
    d['C'] = {c for c in d['U'] if d['des_cfg'][c[0]] and
              (c[1], c[3]) in d['gamma'][c[2]] and c[1] in d['act'][c[0]] and
              (c[0], c[1], c[2], c[4]) in d['role_rel']}
    d['Chan'] = {c: c in d['C'] for c in d['U']}  # Closure VI
    d['W'] = {TERM_ZERO}  # Zero F-vector space for any field F.
    d['T'] = {c: TERM_ZERO for c in d['C']}
    d['Dcomp'] = {frozenset(seq) for n in range(len(d['C']) + 1)
                  for seq in combinations(sorted(d['C']), n)}
    d['Comp'] = {family: TERM_ZERO for family in d['Dcomp']}  # finite zero sums
    assert set(d['T']) == d['C'] and d['Comp'][frozenset()] == TERM_ZERO
    assert d['Dcomp'] == ({frozenset(), frozenset(d['C'])} if d['C'] else {frozenset()})
    return d


def trace(d, c):
    p, a, k, v, rho = c
    return {(H, h, p, a, k, v, rho) for H, h in d['res']
            if h in d['des_expr'] and (h, p) in d['real'] and
            p in d['adm_cfg'] and p in d['lc'] and p in d['bc'] and
            (a, v) in d['gamma'][k] and a in d['act'][p] and
            (p, a, k, rho) in d['role_rel']}


def check_zero_vector_space(field):
    # The proof for *all* field scalars is symbolic: a·0W=0W, 0W+0W=0W.
    # The following representative samples do not purport to enumerate Q.
    samples = [0, 1] if field == 'F2' else [Fraction(0), Fraction(1),
                                              Fraction(-1), Fraction(2, 3)]
    plus = lambda x, y: TERM_ZERO
    scalar_action = lambda alpha, x: TERM_ZERO
    z = TERM_ZERO
    assert all(plus(z, z) == z and scalar_action(a, z) == z for a in samples)
    assert all(scalar_action(a+b, z) == plus(scalar_action(a, z), scalar_action(b, z))
               for a, b in product(samples, repeat=2))
    assert all(scalar_action(a*b, z) == scalar_action(a, scalar_action(b, z))
               for a, b in product(samples, repeat=2))
    assert all(plus(scalar_action(a, z), scalar_action(a, z)) == scalar_action(a, plus(z, z))
               for a in samples)
    return len(samples)


def check():
    entries = []
    for field, n in product(('F2', 'Q'), (1, 3)):
        d = construct(field, ['s'+str(i) for i in range(n)])
        only = ('p', 'a', 'lambda', VALUE_ZERO, 'rho')
        assert d['psi'] == {'p': True} and d['Kdes'] == {'p'}
        assert d['Astar'] == d['A'] == {'a'}
        assert d['Q']['lambda'] == {'a'} and d['q'][('a', 'lambda')] == VALUE_ZERO
        assert d['negligible'] == set()
        assert d['U'] == d['C'] == {only}
        assert trace(d, only) == {('h', 'h', 'p', 'a', 'lambda', VALUE_ZERO, 'rho')}
        assert d['T'][only] == TERM_ZERO
        assert d['Dcomp'] == {frozenset(), frozenset({only})}
        assert all(v == TERM_ZERO for v in d['Comp'].values())
        scalars = check_zero_vector_space(field)
        # Removing the *assignment*, while preserving other primitives,
        # is a different legal full model with empty C, NOT a T7.1 refutation.
        alt = construct(field, ['s'+str(i) for i in range(n)], assign=False)
        assert len(alt['C']) == 0 and len(alt['Dcomp']) == 1
        assert len(alt['U']) == 1 and trace(alt, only) == set()
        # Removing identity restriction breaks Primitive Axiom II in THIS
        # construction. It says nothing about alternate constructions.
        identity_required = all((h, h) in d['res'] for h in d['adm_expr'])
        assert identity_required and not all((h, h) in set() for h in d['adm_expr'])
        entries.append(dict(field=field, support_size=n, anchor=sorted(d['B'])[0],
              material_count=1, expression_count=1, configuration_count=1,
              primitive_axioms=['I', 'II', 'III', 'V'],
              closure_clauses=['IV', 'VI', 'VII'],
              psi_witness_count=1, operational_candidates=1,
              admitted_channels=1, valid_trace_witnesses=1,
              finite_channel_families=2, composites_zero=2,
              zero_space_scalar_samples=scalars, typed_zeros_distinct=True,
              alternative_without_q_is_full_model_with_empty_C=True))
    return dict(audit_id='FAS-F2-T7.1-001',source_sha256=SOURCE_SHA,
      all_checks_passed=True, selected_fields=['F2', 'Q'],
      support_sizes=[1,3], selected_instances=len(entries),
      full_model_validity_checks=4, total_admitted_channels=4,
      total_trace_witnesses=4, total_finite_family_checks=8,
      total_legal_alternative_empty_C_models=4,
      arbitrary_field_general_proof_separate_from_selected_checks=True,
      external_independent_validation=False, cases=entries)


def main():
    result = check()
    output = (Path(sys.argv[1]) if len(sys.argv)>1 else
       Path(__file__).resolve().parent.parent/'results'/'t71_full_model_existence.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+'\n',encoding='utf8')
    print('T7.1 full-model finite proof-audit checks PASS:', result['selected_instances'])
    print('OUTPUT', output)

if __name__ == '__main__':
    main()
