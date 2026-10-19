#!/usr/bin/env python3
"""Deterministic, finite witness checks for FAS-F2-T3.6-001.

This verifies finite model instances, not the universally quantified theorem.
Only stdlib; Python >=3.9. Follows the declared typed Formation primitives.
"""
import hashlib
import json
from itertools import product
from pathlib import Path
import sys

VALUES = (-1, 0, 1)
LAMBDA = 'lambda'
ROLE = 'rho'


def sample(name, witnesses=('g',), described=True, conf=True,
           assigned=True, role=True, qvalue=1, zero=False, empty=False):
    """Provide primitive data; all derived data must be recomputed, not assumed."""
    if empty:
        return dict(name=name, materials=set(), expressions={}, configurations={},
                    admitted=set(), described=set(), restrictions=set(), realized=set(),
                    q={}, roles=set(), value_space=set(VALUES), roles_carrier={ROLE})
    es = {g: {'mat': {'a'}, 'anch': {'a': 's0'}} for g in witnesses}
    configs = {'p': {'act': {'a'}, 'anch': {'a': 's0'}, 'adm': conf, 'lc': conf, 'bc': conf}}
    r = {(g, g) for g in es}
    real = {(g, 'p') for g in es} if described else set()
    q = {'a': (0 if zero else qvalue)} if assigned else {}
    # If p is not describable, Q must be empty to satisfy Axiom V.
    if not described or not conf:
        q = {}
    return dict(name=name, materials={'a'}, expressions=es, configurations=configs,
                admitted=set(es), described=set(es), restrictions=r, realized=real,
                q=q, roles={('p', 'a', LAMBDA, ROLE)} if role else set(),
                value_space=set(VALUES), roles_carrier={ROLE})


def audit(m):
    E, P = m['expressions'], m['configurations']
    adm, dex = m['admitted'], m['described']
    res, real, q = m['restrictions'], m['realized'], m['q']
    assert dex <= adm, 'Axiom I'
    assert res <= set(product(E, E))
    assert real <= set(product(E, P))
    assert all((g, g) in res for g in adm), 'Axiom II identity restriction'
    for h, g in res:
        assert g in adm, 'Axiom II admitted target'
        assert E[g]['mat'] <= E[h]['mat'], 'Axiom II subset'
        assert E[g]['anch'] == {a: E[h]['anch'][a] for a in E[g]['mat']}, 'Axiom II anchor'
    for g, p in real:
        assert P[p]['act'] <= E[g]['mat'], 'Axiom III subset'
        assert P[p]['anch'] == {a: E[g]['anch'][a] for a in P[p]['act']}, 'Axiom III anchor'

    def confadm(p):
        return P[p]['adm'] and P[p]['lc'] and P[p]['bc']

    witness = {p: [(H, h) for (H, h) in res
                   if h in dex and (h, p) in real and confadm(p)] for p in P}
    des_cfg = {p for p in P if witness[p]}  # Clause IV
    a_star = set().union(*(P[p]['act'] for p in des_cfg)) if des_cfg else set()
    assert set(q) <= a_star, 'Axiom V'
    assert set(q.values()) <= m['value_space']

    U = set(product(P, m['materials'], {LAMBDA}, m['value_space'], m['roles_carrier']))

    def assignment_graph_for(p):
        return {(a, v) for a, v in q.items() if a in P[p]['act']}

    def admitted(c):
        p, a, lam, v, rho = c
        return (p in des_cfg and (a, v) in assignment_graph_for(p)
                and (p, a, lam, rho) in m['roles'])

    C = {c for c in U if admitted(c)}  # Clause VI

    def traces(c):
        p, a, lam, v, rho = c
        return {(H, h, p, a, lam, v, rho) for (H, h) in witness[p]
                if (a, v) in assignment_graph_for(p)
                and (p, a, lam, rho) in m['roles']}

    # Post-VI term map is supplied only over admitted channels, with no
    # prescribed relation between q(a)=0 and T(c)=0.
    T = {c: (7 if c[3] == 0 else c[3] * 3) for c in C}
    assert set(T) == C
    checked = 0
    for c in U:
        tr = traces(c)
        assert (c in C) == bool(tr), f'Equivalence violated: {m["name"]}, {c}'
        if tr:
            assert c in T and sum(T[x] for x in {c}) == T[c], 'Clause VII singleton'
        else:
            assert c not in T, 'Absent channel assigned a term'
        checked += 1
    return {'case': m['name'], 'candidate_channels': len(U), 'admitted_channels': len(C),
            'trace_witnesses': sum(len(traces(c)) for c in U),
            'witnesses_for_admitted': [len(traces(c)) for c in sorted(C)],
            'candidate_equivalences_checked': checked,
            'q_defined_zero_count': sum(1 for val in q.values() if val == 0),
            'singleton_compositions_checked': len(C), 'passed': True}


def main():
    fixtures = [
        sample('A_single_sound_witness'),
        sample('B_two_sound_witnesses_one_channel', witnesses=('g', 'h')),
        sample('C_no_realization_witness', described=False),
        sample('D_describable_but_undefined_assignment', assigned=False),
        sample('E_role_missing', role=False),
        sample('F_defined_zero_with_component_term_seven', zero=True),
        sample('G_empty_candidate_universe', empty=True),
        sample('H_configuration_coherence_blocked', conf=False),
    ]
    results = [audit(model) for model in fixtures]
    assert results[0]['admitted_channels'] == 1
    assert results[1]['admitted_channels'] == 1 and results[1]['trace_witnesses'] == 2
    assert results[2]['admitted_channels'] == 0
    assert results[3]['admitted_channels'] == 0
    assert results[4]['admitted_channels'] == 0
    assert results[5]['admitted_channels'] == 1 and results[5]['q_defined_zero_count'] == 1
    assert results[6]['candidate_channels'] == 0
    assert results[7]['admitted_channels'] == 0
    summary = {'case_id': 'FAS-F2-T3.6-001', 'source_sha256':
               '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a',
               'test_scope': 'finite illustrative structures only; universal mathematical proof is separate',
               'fixtures': len(results),
               'candidate_channels_checked': sum(x['candidate_equivalences_checked'] for x in results),
               'singleton_compositions_checked': sum(x['singleton_compositions_checked'] for x in results),
               'all_passed': all(x['passed'] for x in results), 'results': results}
    b = json.dumps(summary, sort_keys=True, indent=2, ensure_ascii=False) + '\n'
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / 'results' / 't36_trace_witnesses.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(b)
    print(f'{summary["fixtures"]}/8 fixtures PASS; '
          f'{summary["candidate_channels_checked"]} candidate equivalences; '
          f'{summary["singleton_compositions_checked"]} singleton composites')
    print('JSON_SHA256', hashlib.sha256(b.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
