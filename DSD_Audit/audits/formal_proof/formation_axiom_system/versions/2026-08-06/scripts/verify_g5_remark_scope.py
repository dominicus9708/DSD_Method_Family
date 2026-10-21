#!/usr/bin/env python3
r"""Reproducible finite evidence for original Formation F2 five Remarks.
This does not certify the general mathematical statements.
Windows repo-root usage:
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_g5_remark_scope.py
Optional first argument: JSON output destination.
"""
import hashlib
import json
import sys
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


def r31():
    # Each example meets the *other* typed primitive condition only;
    # neither is falsely labeled a full model satisfying both axioms.
    E = {'x'}
    i_holds = lambda des, adm: des <= adm
    ii_holds = lambda adm, res: all((h, h) in res for h in adm) and all(
        h in adm for H, h in res)
    example_I_only = {'des': set(), 'adm': {'x'}, 'res': set()}
    example_II_only = {'des': {'x'}, 'adm': set(), 'res': set()}
    assert E == {'x'}
    assert i_holds(example_I_only['des'], example_I_only['adm'])
    assert not ii_holds(example_I_only['adm'], example_I_only['res'])
    assert ii_holds(example_II_only['adm'], example_II_only['res'])
    assert not i_holds(example_II_only['des'], example_II_only['adm'])
    return {'I_without_II_typed_witness': True,
            'II_without_I_typed_witness': True,
            'these_are_not_full_original_models': True}


def r32():
    des, adm, res = {'h'}, {'h'}, {('h', 'h')}
    assert des <= adm and ('h', 'h') in res
    def psi(realize, gates):
        return all(gates) and any(H == h == 'h' and h in des and
                                  (h, 'p') in realize for H, h in res)
    assert not psi(set(), (True, True, True))
    assert not psi({('h', 'p')}, (True, False, True))
    assert psi({('h', 'p')}, (True, True, True))
    return {'identity_Res_available_from_I_II': True,
            'witness_without_realization_not_sufficient': True,
            'witness_without_three_gates_not_sufficient': True,
            'H_equal_h_can_support_full_Psi': True}


def r34():
    # Derived IV, VI, VII for one primitive core. Primitive carrier data held fixed;
    # supplied post-VI T changes freely, so uniqueness is explicitly relative.
    def closure(term):
        E, P, M = {'h'}, {'p'}, {'a'}
        q = {'a': 0}
        res, real = {('h', 'h')}, {('h', 'p')}
        role = {('p', 'a', 'lambda', 'r')}
        K = {p for p in P if any(h in E and (h, p) in real for H, h in res)}
        astar = M if K else set()
        assert set(q) <= astar
        C = {(p, a, 'lambda', q[a], rho) for p, a, lam, rho in role if p in K}
        T = {c: term for c in C}
        families = [set(), set(C)]
        comp = [sum(T[c] for c in family) for family in families]
        return (sorted(K), sorted(astar), sorted(C), comp)
    first, again, second = closure(1), closure(1), closure(2)
    assert first == again
    assert first[:3] == second[:3] and first[3] != second[3]
    return {'same_supplied_data_unique_derived_closure': True,
            'post_VI_term_data_not_uniquely_determined_by_primitive_core': True,
            'first_nonempty_composite': first[3][1],
            'second_nonempty_composite': second[3][1]}


def r69():
    # Full source: E={h}, P={p}, mat(h)=act(p)={a}, Res and Realize,
    # describable h and three gates; q(a)=0; its A*={a}.
    source = {'expressions': {'h'}, 'configurations': {'p'},
              'des': {'h'}, 'res': {('h', 'h')}, 'real': {('h', 'p')},
              'gates': (True, True, True), 'qdomain': {'a'},
              'active': {'p': {'a'}}}
    def closure(z):
        K = {p for p in z['configurations'] if all(z['gates']) and
             any(h in z['des'] and (h, p) in z['real'] for H, h in z['res'])}
        A = set().union(*(z['active'][p] for p in K)) if K else set()
        return K, A, z['qdomain'] <= A
    assert closure(source) == ({'p'}, {'a'}, True)
    reduced = dict(source, expressions=set(), des=set(), res=set(), real=set(),
                   qdomain=set())
    assert closure(reduced) == (set(), set(), True)
    # Valid reduced full model, yet target full model reflects Psi(p)=True and
    # source model has Psi(p)=False; witness reflection fails.
    assert 'p' in closure(source)[0] and 'p' not in closure(reduced)[0]
    # Arbitrary retention of old q(a) after removing all witnesses is not a model.
    incorrectly_retained = dict(reduced, qdomain={'a'})
    assert closure(incorrectly_retained) == (set(), set(), False)
    return {'source_full_model_consistent': True,
            'witness_removed_full_reduct_not_witness_reflecting': True,
            'retained_q_outside_new_Astar_invalid': True,
            'not_every_induced_subset_forms_submodel': True}


def r613():
    material = {'a', 'b'}
    anchor = {'a': 'N', 'b': 'S'}
    edges = {('a', 'b')}
    target_anchor = {'x': 'N', 'y': 'S'}
    target_edges = {('x', 'y')}
    def anchored_isomorphism(f):
        return set(f) == material and set(f.values()) == set(target_anchor) and all(
            anchor[a] == target_anchor[f[a]] for a in material) and {
            (f[a], f[b]) for a, b in edges} == target_edges
    assert anchored_isomorphism({'a': 'x', 'b': 'y'})
    assert not anchored_isomorphism({'a': 'y', 'b': 'x'})
    assert anchor != target_anchor
    return {'changed_internal_coordinate_names_allowed': True,
            'same_external_support_anchors_preserved': True,
            'anchor_incompatible_permutation_rejected': True,
            'material_incidence_preserved': True}


def main():
    outcomes = {'Remark 3.1': r31(), 'Remark 3.2': r32(),
                'Remark 3.4': r34(), 'Remark 6.9': r69(),
                'Remark 6.13': r613()}
    assert len(outcomes) == 5
    out = {'case': 'FAS-F2-G5-REMARK-SCOPE-001',
           'source_pdf_sha256': SOURCE_SHA,
           'remarks_tested': len(outcomes), 'selected_fixtures': outcomes,
           'scope': 'bounded exact fixtures plus separate source logic; not general theorem proof',
           'full_F2': 'OPEN', 'external_independent_validation': False}
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).resolve().parents[1] / 'results/g5_remark_scope.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(out, sort_keys=True, indent=2, ensure_ascii=False) + '\n'
    path.write_text(data, encoding='utf-8')
    print(json.dumps({'remarks_tested': len(outcomes),
                      'assertions': sum(len(d) for d in outcomes.values()),
                      'outcome': 'ALL_SELECTED_FIXTURES_PASS'}, sort_keys=True))


if __name__ == '__main__':
    main()
