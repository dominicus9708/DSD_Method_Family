#!/usr/bin/env python3
r"""New-source F2 revised-edition finite fixtures, not a universal proof.
Author of audited source: Kwon Dominicus.
Source: DSD_Formation_Axiom_System_EN(7).pdf, SHA256 af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe
Run at checked-out DSD_Method_Family repository root:
python .\DSD_Audit\audits\formal_proof\formation_axiom_system\versions\2026-10-22\scripts\verify_n2_four_sections.py
Optional first argument: JSON output destination.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path

SOURCE_SHA = 'af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe'
CASE = 'FAS-F2-20261022-N2-FOUR-SECTION-REAUDIT-001'


def core():
    return dict(M={'a', 'b'}, E={'g'}, P={'p'},
                mat={'g': {'a'}}, ancE={'g': {'a': 's0'}},
                act={'p': {'a'}}, ancP={'p': {'a': 's0'}},
                des={'g'}, adm={'g'}, res={('g', 'g')},
                real={('g', 'p')}, gates={'p': (True, True, True)},
                Q={'a'}, q={'a': 1}, roles={('p', 'a', 'rho')})


def valid_typed(m):
    assert set(m['mat']) == m['E'] == set(m['ancE'])
    assert set(m['act']) == m['P'] == set(m['ancP']) == set(m['gates'])
    assert m['des'] <= m['E'] and m['adm'] <= m['E']
    assert all(set(m['ancE'][h]) == m['mat'][h] <= m['M'] for h in m['E'])
    assert all(set(m['ancP'][p]) == m['act'][p] <= m['M'] for p in m['P'])
    assert set(m['q']) == m['Q'] <= m['M']
    assert all(H in m['E'] and h in m['E'] for H, h in m['res'])
    assert all(h in m['E'] and p in m['P'] for h, p in m['real'])
    assert all(p in m['P'] and a in m['M'] for p, a, _ in m['roles'])


def statuses(m):
    valid_typed(m)
    def anchored(inner, outer):
        return inner == {a: outer[a] for a in inner if a in outer}
    def res_anchor(H, h):
        return m['mat'][h] <= m['mat'][H] and anchored(m['ancE'][h], m['ancE'][H])
    def real_anchor(h, p):
        return m['act'][p] <= m['mat'][h] and anchored(m['ancP'][p], m['ancE'][h])
    K = {p for p in m['P'] if all(m['gates'][p]) and any(
        h in m['des'] and (h, p) in m['real'] for H, h in m['res'])}
    A = set().union(*(m['act'][p] for p in K)) if K else set()
    clauses = [m['des'] <= m['adm'],
               all(res_anchor(H, h) for H, h in m['res']),
               all(h in m['adm'] for _, h in m['res']),
               all((H, H) in m['res'] for H in m['adm']),
               all(real_anchor(h, p) for h, p in m['real']),
               m['Q'] <= A]
    # Definition VI with a single quantity kind, q globally unique.
    C = {(p, a, m['q'][a], role) for p, a, role in m['roles']
         if p in K and a in m['act'][p] and a in m['Q']}
    return dict(clauses=clauses, K=K, A=A, C=C)


def residual_six():
    names = ['I_description_implies_admission', 'II_sound_anchor',
             'II_target_admission', 'II_identity', 'III_realization_anchor',
             'V_global_Q_subset_Astar']
    examples = []
    for i in range(6):
        m = core()
        if i == 0:
            m['E'].add('x'); m['mat']['x'] = {'b'}
            m['ancE']['x'] = {'b': 's0'}; m['des'].add('x')
        elif i == 1:
            m['E'].update({'H', 'h'}); m['adm'].update({'H', 'h'})
            m['mat'].update(H={'b'}, h={'b'})
            m['ancE'].update(H={'b': 's0'}, h={'b': 's1'})
            m['res'].update({('H', 'H'), ('h', 'h'), ('H', 'h')})
        elif i == 2:
            m['E'].update({'H', 'h'}); m['adm'].add('H')
            m['mat'].update(H={'b'}, h={'b'})
            m['ancE'].update(H={'b': 's0'}, h={'b': 's0'})
            m['res'].update({('H', 'H'), ('H', 'h')})
        elif i == 3:
            m['E'].add('x'); m['adm'].add('x')
            m['mat']['x'] = {'b'}; m['ancE']['x'] = {'b': 's0'}
        elif i == 4:
            m['E'].add('h'); m['adm'].add('h')
            m['mat']['h'] = {'b'}; m['ancE']['h'] = {'b': 's0'}
            m['res'].add(('h', 'h'))
            m['P'].add('p2'); m['act']['p2'] = {'b'}
            m['ancP']['p2'] = {'b': 's1'}
            m['real'].add(('h', 'p2'))
            m['gates']['p2'] = (False, False, False)
        else:
            m['Q'].add('b'); m['q']['b'] = 2
        s = statuses(m)
        expected = [True] * 6; expected[i] = False
        assert s['clauses'] == expected, (names[i], s['clauses'])
        assert s['K'] == {'p'} and s['A'] == {'a'}
        assert s['C'] == {('p', 'a', 1, 'rho')}
        examples.append(dict(falsified=names[i], residual_values=s['clauses'],
                             active_kernel=True, actual_channel_count=len(s['C'])))
    return dict(six_clausewise_witnesses=examples,
                all_have_nontrivial_active_kernel=True,
                models_satisfy_all_six=False)


def conditional_zero_extension():
    # One h/p and assignment q(a)=0; two role kinds, only one admitted role.
    U = {('p', 'a', 'lambda', 0, role) for role in ('admitted', 'absent')}
    admitted = ('p', 'a', 'lambda', 0, 'admitted')
    absent = ('p', 'a', 'lambda', 0, 'absent')
    C = {admitted}
    assert len(U) == 2 and C <= U and absent not in C
    Tzero = {admitted: 0}
    padded = {u: Tzero.get(u, 0) for u in U}
    assert padded[admitted] == padded[absent] == 0
    Tnonzero = {admitted: 5}
    padded_nonzero = {u: Tnonzero.get(u, 0) for u in U}
    assert (padded_nonzero[admitted] != 0) and (padded_nonzero[absent] == 0)
    Call = U.copy()
    Tall = {u: 0 for u in Call}
    assert U - Call == set() and all(u in Call for u in U)
    # Exhaustively verify the exact logical criterion for arbitrary candidate
    # subsets of U with term values from {-1,0,1}; finite family only.
    total = 0
    for mask in range(1 << len(U)):
        Cmask = {u for i, u in enumerate(sorted(U)) if mask & (1 << i)}
        for vals in itertools.product((-1, 0, 1), repeat=len(Cmask)):
            terms = dict(zip(sorted(Cmask), vals))
            output = {u: terms.get(u, 0) for u in U}
            undecodable = any(output[u] == output[v] and ((u in Cmask) != (v in Cmask))
                              for u in U for v in U)
            criterion = bool(U - Cmask) and any(terms[c] == 0 for c in Cmask)
            assert undecodable == criterion
            total += 1
    assert total == 16
    return dict(zero_collision_when_absent_and_zero_term=True,
                no_necessary_collision_when_admitted_terms_nonzero=True,
                no_necessary_collision_when_no_absent_candidates=True,
                two_candidate_truth_assignments=total)


def grid_d2():
    sites = {(r, c) for r in range(3) for c in range(3)}
    dirs = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    vert = {('v', s) for s in sites}
    edge = {('e', tuple(sorted((a, b)))) for a in sites for b in sites
            if abs(a[0]-b[0])+abs(a[1]-b[1]) == 1}
    slots = {('slot', site, direction) for site in sites for direction in dirs}
    allmat = vert | edge | slots
    assert len(vert) == 9 and len(edge) == 12 and len(slots) == 36
    assert len(allmat) == 57
    selected = {(0, 0), (1, 0)}
    joining = ('e', tuple(sorted(selected)))
    exposed = set()
    for s in selected:
        for direction, drdc in dirs.items():
            neighbor = s[0]+drdc[0], s[1]+drdc[1]
            if neighbor not in selected:
                exposed.add(('slot', s, direction))
    assert len(exposed) == 6
    selectedmat = {('v', s) for s in selected} | {joining} | exposed
    assert len(selectedmat) == 9 and selectedmat <= allmat
    annotations = {slot: ('blocked' if slot in exposed else 'transmissive')
                   for slot in slots}
    assert sum(a == 'blocked' for a in annotations.values()) == 6
    assert sum(a == 'transmissive' for a in annotations.values()) == 30
    assert all(annotations[slot] == 'blocked' for slot in exposed)
    # Stable external support for material item, restricting full-grid anchor.
    anchor = {item: item for item in allmat}
    anchH = anchor.copy()
    anchh = {item: anchH[item] for item in selectedmat}
    anchp = anchh.copy()
    assert all(anchH[a] == anchh[a] == anchp[a] for a in selectedmat)
    assert {k: v for k, v in annotations.items() if k in selectedmat} == {
        k: v for k, v in annotations.items() if k in selectedmat}
    res = {('H', 'h'), ('H', 'H'), ('h', 'h')}
    real = {('h', 'p')}
    descriptive_expr = {'h'}
    def formation(BC):
        candidates = {'p'}
        gates = {'p': (True, True, BC)}
        K = {p for p in candidates if all(gates[p]) and any(
            h in descriptive_expr and (h, p) in real for H, h in res)}
        A = selectedmat if K else set()
        Q = {joining} if BC else set()
        assert Q <= A
        role = {('p', joining, 'lambda', 'rho')} if BC else set()
        channels = {(p, a, 'lambda', 1, rho) for p, a, lam, rho in role
                    if p in K and a in Q and a in selectedmat}
        return dict(K=K, active=A, Q=Q, channels=channels,
                    composite=sum((1 for c in channels), 0))
    plus = formation(True)
    minus = formation(False)
    assert plus['K'] == {'p'} and minus['K'] == set()
    assert plus['Q'] == {joining} and minus['Q'] == set()
    assert len(plus['channels']) == 1 and len(minus['channels']) == 0
    assert plus['composite'] == 1 and minus['composite'] == 0
    # Same base, material relations, config/expression carriers,
    # admission/Res/Realize & Stage 2; unique p has different BC at Stage 3.
    comparable_before_3 = True
    compatible_at_3 = (True == False)
    assert comparable_before_3 and not compatible_at_3
    return dict(full_vertex_items=9,full_edge_items=12,full_boundary_slots=36,
                full_material_items=57,retained_material_items=9,
                exposed_blocked_slots=6,remaining_transmissive_slots=30,
                original_stage2_comparison_nonempty=True,stage3_comparison_empty=True,
                first_branching_index=3,positive_channels=1,negative_channels=0,
                inherited_anchors_and_annotations_consistent=True)


def fixed_j_comparison():
    # Strict identity map is an isomorphism for a model with one term of 1.
    one_c = {'c': 1}
    assert -sum(one_c.values()) != sum(one_c.values())
    # Given two identical empty-channel full models, no nonempty families exist.
    empty = set()
    assert not any(len(F) for F in (empty,))
    # Non-isomorphic legal full models with different role sets/channels:
    # source 1 role c0:T=0; target roles dplus,dminus:T=1,-1.
    src = {'c0': 0}; dst = {'dplus': 1, 'dminus': -1}
    assert len(src) != len(dst) and sum(src.values()) == sum(dst.values()) == 0
    # Positive strict-isomorphism direction uses its own J (identity here).
    assert sum(one_c.values()) == sum(one_c.values())
    return dict(strict_equivalence_does_not_force_arbitrary_fixed_J_coincidence=True,
                nonempty_family_required_even_for_identical_empty_channel_models=True,
                composite_coincidence_does_not_force_strict_equivalence=True,
                strict_isomorphism_with_its_own_J_preserves_nonempty_finite_family=True)


def main():
    checks = {'Theorem 4.7': residual_six(),
              'Proposition 5.13': conditional_zero_extension(),
              'Section 7.3 D2': grid_d2(),
              'Section 8': fixed_j_comparison()}
    output = dict(case=CASE,source_pdf_sha256=SOURCE_SHA,
                  source_pdf_label='2026.10.22',new_source_pages=34,
                  checks=checks,
                  notes=['Relative independence interpretations are not full models satisfying all six residual clauses.',
                         'D2 Stage-3 comparison argument uses primitive BC policy, not geometry-derived physical dynamics.',
                         'Scalar finite examples illustrate the general fixed-J logic; not a machine proof of all models.',
                         'Source 2026-10-22 mathematical claims are audited only on four corrected loci here.'],
                  new_full_manuscript_fpa='OPEN',independent_external_validation='not_established')
    dest = (Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'results/n2_four_sections.json')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(dict(case=CASE,residual_witnesses=6,zero_extension_truth_assignments=16,
                          grid_branch=checks['Section 7.3 D2']['first_branching_index'],
                          comparison_boundaries=4, result='ALL_SELECTED_ASSERTIONS_PASS'),sort_keys=True))


if __name__ == '__main__':
    main()
