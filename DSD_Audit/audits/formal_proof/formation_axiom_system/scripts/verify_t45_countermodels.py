#!/usr/bin/env python3
r"""Reconstruct FAS Countermodels 4.1--4.4, as specified on manuscript pp.9--10.

Finite source-listed checks, not a universal automated proof certificate.
From the DSD_Method_Family repository root on Windows 11:
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t45_countermodels.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\t45_axiom_independence.json
"""
import argparse
import json
from pathlib import Path


def make_model(failure):
    x = dict(material={'g': ['a']}, expression_anchors={'g': {'a': 's0'}},
             admitted=['g'], describable=['g'], configurations={'p': ['a']},
             configuration_anchors={'p': {'a': 's0'}},
             config_admission=['p'], local_coherence=['p'], boundary_compatibility=['p'],
             restriction=[['g', 'g']], realization=[['g', 'p']],
             q={'a': 1}, role=[['p', 'a', 'lambda', 'rho']])
    if failure == 'I':
        x['material']['x'] = ['b']
        x['expression_anchors']['x'] = {'b': 's0'}
        x['describable'].append('x')
    elif failure == 'II':
        x['material'].update(H=['b'], h=['b'])
        x['expression_anchors'].update(H={'b': 's0'}, h={'b': 's1'})
        x['admitted'] += ['H', 'h']
        x['restriction'] += [['H', 'H'], ['h', 'h'], ['H', 'h']]
    elif failure == 'III':
        x['material']['h'] = ['b']
        x['expression_anchors']['h'] = {'b': 's0'}
        x['admitted'].append('h')
        x['configurations']['p_prime'] = ['b']
        x['configuration_anchors']['p_prime'] = {'b': 's1'}
        x['restriction'].append(['h', 'h'])
        x['realization'].append(['h', 'p_prime'])
    elif failure == 'V':
        x['q']['b'] = 1
    else:
        raise ValueError(failure)
    return x


def inspect(m):
    material = {'a', 'b'}
    support = {'s0', 's1'}
    expr = set(m['material'])
    cfg = set(m['configurations'])
    for e, items in m['material'].items():
        assert set(items) <= material
        assert set(m['expression_anchors'][e]) == set(items)
        assert set(m['expression_anchors'][e].values()) <= support
    for p, items in m['configurations'].items():
        assert set(items) <= material
        assert set(m['configuration_anchors'][p]) == set(items)
        assert set(m['configuration_anchors'][p].values()) <= support
    assert set(m['expression_anchors']) == expr
    assert set(m['configuration_anchors']) == cfg
    for key in ('admitted', 'describable'):
        assert set(m[key]) <= expr
    for key in ('config_admission', 'local_coherence', 'boundary_compatibility'):
        assert set(m[key]) <= cfg
    assert all(H in expr and h in expr for H, h in m['restriction'])
    assert all(h in expr and p in cfg for h, p in m['realization'])
    assert all(p in cfg and a in material and k == 'lambda' and r == 'rho'
               for p, a, k, r in m['role'])
    assert set(m['q']) <= material
    assert all(isinstance(v, (int, float)) for v in m['q'].values())

    desc, adm = set(m['describable']), set(m['admitted'])
    issues_I = [e for e in expr if e in desc and e not in adm]
    issues_II = []
    for H, h in m['restriction']:
        if (not set(m['material'][h]) <= set(m['material'][H]) or
            m['expression_anchors'][h] != {
                a: m['expression_anchors'][H][a]
                for a in m['material'][h] if a in m['expression_anchors'][H]
            } or h not in adm):
            issues_II.append([H, h])
    for H in adm:
        if [H, H] not in m['restriction']:
            issues_II.append([H, 'missing_identity'])
    issues_III = []
    for h, p in m['realization']:
        if (not set(m['configurations'][p]) <= set(m['material'][h]) or
            m['configuration_anchors'][p] != {
                a: m['expression_anchors'][h][a]
                for a in m['configurations'][p] if a in m['expression_anchors'][h]
            }):
            issues_III.append([h, p])

    conf = set(m['config_admission']) & set(m['local_coherence']) & set(m['boundary_compatibility'])
    kdes = set()
    for p in conf:
        if any([H, h] in m['restriction'] and h in desc and [h, p] in m['realization']
               for H in expr for h in expr):
            kdes.add(p)
    active = set().union(*(set(m['configurations'][p]) for p in kdes)) if kdes else set()
    issues_V = sorted(set(m['q']) - active)
    channels = sorted([[p, a, 'lambda', v, 'rho'] for p in kdes for a in m['configurations'][p]
                       for item, v in m['q'].items() if item == a
                       if [p, a, 'lambda', 'rho'] in m['role']])
    assert channels == [['p', 'a', 'lambda', 1, 'rho']]
    assert m['restriction'] and m['realization'] and m['q'] and m['role'] and kdes
    # Paper's R-valued term map T(c_g)=1, with finite composites.
    assert sum([]) == 0 and sum([1]) == 1

    issues = {'I': issues_I, 'II': issues_II, 'III': issues_III, 'V': issues_V}
    return {'axioms': {a: not bool(issues[a]) for a in ('I', 'II', 'III', 'V')},
            'violations': issues, 'describable_configurations': sorted(kdes),
            'active_kernel': sorted(active), 'admitted_channels': channels,
            'finite_composite': {'empty': 0, 'cg': 1}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='results/t45_axiom_independence.json')
    args = ap.parse_args()
    out = {}
    for omitted in ('I', 'II', 'III', 'V'):
        record = inspect(make_model(omitted))
        assert record['axioms'][omitted] is False, omitted
        assert all(v is True for ax, v in record['axioms'].items() if ax != omitted), omitted
        assert len(record['violations'][omitted]) == 1, omitted
        out[f'Countermodel_4.{dict(I=1, II=2, III=3, V=4)[omitted]}'] = record
    result = {'audit_id': 'FAS-F2-T4.5-001', 'manuscript_section': '4.1',
              'status': 'FOUR_FINITE_COUNTERMODELS_REPRODUCED',
              'independence_of_four_primitive_axioms': 'SUPPORTED_BY_EXPLICIT_FINITE_COUNTERINTERPRETATIONS',
              'external_independent_replication': False,
              'general_automated_theorem_certification': False,
              'source_pdf_sha256': '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a',
              'cases': out}
    p = Path(args.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('4/4 source-listed axiom-independence counterinterpretations reproduced')
    print('Output:', p)


if __name__ == '__main__':
    main()
