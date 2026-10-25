#!/usr/bin/env python3
"""MF-REG-20261025-004: source-locked Comparison T2/T3 archived fixtures.
Author: Kwon Dominicus. Bounded replay, NOT the original 40-gate full protocol.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import fitz


def evaluate(t):
    src = set(t['src_nodes'])
    tgt = set(t['tgt_nodes'])
    f = t['map']
    values = list(f.values())
    injective = len(set(values)) == len(values) and set(f) == src and set(values) <= tgt
    surjective = set(values) == tgt
    src_edges = {tuple(x) for x in t['src_edges']}
    tgt_edges = {tuple(x) for x in t['tgt_edges']}
    forward = all((f[a], f[b]) in tgt_edges for a, b in src_edges)
    statuses = all(t['src_status'][a] == t['tgt_status'][b] for a, b in f.items())
    unmapped = [v for v in t['tgt_nodes'] if v not in set(values)]

    if t['kind'] == 'direct_injective_non_surjective':
        direct = injective and forward and statuses and t['bridge'] is None
        return {'injective': injective, 'surjective_full_target': surjective,
                'preserved_src_edges': forward, 'preserved_mapped_status': statuses,
                'unmapped_target_nodes': unmapped,
                'strict_equivalence_under_frozen_criterion': direct and surjective,
                'correspondence_class': 'DIRECT_CORRESPONDENCE' if direct else 'UNDETERMINED',
                'structural_equivalence_result': 'no' if not surjective else 'undetermined',
                'terminal': 'COMPARISON_RESOLVED' if direct else 'COMPARISON_BLOCKED',
                'conformance': 'CONFORMANT' if direct else 'NONCONFORMANT',
                'gain': 'NOT_ASSESSED'}
    if t['kind'] == 'supplied_encoding_equivalence':
        bridge = t['bridge']
        supplied = isinstance(bridge, dict) and bridge.get('source') == 'supplied_e' \
                   and all(bridge.get(a) == b for a, b in f.items())
        inv = {v: k for k, v in f.items()}
        backward = injective and surjective and all((inv[x], inv[y]) in src_edges for x,y in tgt_edges)
        encoded = supplied and injective and surjective and forward and backward and statuses
        labels_differ = all(a != b for a, b in f.items())
        return {'injective': injective, 'surjective_full_target': surjective,
                'preserved_src_edges': forward, 'preserved_inverse_edges': backward,
                'preserved_mapped_status': statuses, 'literal_label_equality': not labels_differ,
                'explicit_bridge_used': supplied,
                'correspondence_class': 'ENCODED_CORRESPONDENCE' if encoded else 'UNDERDETERMINED_CORRESPONDENCE',
                'structural_equivalence_result': 'equivalent_under_supplied_encoding_only' if encoded else 'undetermined',
                'terminal': 'COMPARISON_RESOLVED' if encoded else 'COMPARISON_BLOCKED',
                'conformance': 'CONFORMANT' if encoded else 'NONCONFORMANT',
                'gain': 'NOT_ASSESSED'}
    raise ValueError('Unrecognized case kind: ' + t['kind'])


def run(packet, pdf):
    expected = packet['formation']
    digest = hashlib.sha256(Path(pdf).read_bytes()).hexdigest()
    with fitz.open(pdf) as doc:
        pages = len(doc)
        txt = ' '.join(page.get_text() for page in doc)
    locked = digest == expected['sha256'] and pages == expected['pages']
    anchors = {x: x in txt for x in ('Definition 6.15', 'Theorem 6.16', 'Proposition 6.22')}
    records = []
    for case in packet['tasks']:
        actual = evaluate(case)
        checks = {field: actual.get(field) == value for field, value in case['expected'].items()}
        records.append({'case': case['case'], 'id': case['id'], 'observed': actual,
                        'expected': case['expected'], 'field_match': checks,
                        'pass': all(checks.values()) and set(actual) == set(case['expected'])})
    all_ok = locked and all(anchors.values()) and all(r['pass'] for r in records)
    return {'audit_id': packet['id'], 'verdict': 'PASS_WITH_BOUNDARY' if all_ok else 'FAIL_WITH_EVIDENCE',
            'source': {'sha256': digest, 'pages': pages, 'matched_frozen_version': locked},
            'source_anchors': anchors, 'case_results': records,
            'counts': {'cases': len(records), 'cases_passed': sum(r['pass'] for r in records),
                       'fields': sum(len(r['field_match']) for r in records),
                       'fields_passed': sum(sum(r['field_match'].values()) for r in records)},
            'historical_full_gate_replay': {x['method']:'NOT_EXECUTED' for x in packet['historical_protocol_score_registry']},
            'historic_result_counts_prior_only': {x['method']:x['historic_passed'] for x in packet['historical_protocol_score_registry']},
            'old_formation_pdf_direct_replay': 'BLOCKED_SOURCE_NOT_AVAILABLE',
            'limits': packet['limits']}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fixtures', required=True)
    p.add_argument('--formation', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--negative-output', required=True)
    a = p.parse_args()
    raw = Path(a.fixtures).read_bytes()
    packet = json.loads(raw)
    assert packet['id'] == 'MF-REG-20261025-004'
    assert len(packet['tasks']) == 2 and {x['id'] for x in packet['tasks']} == {'T2','T3'}
    result = run(packet, a.formation)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    attacks = [
        ('NC1-false-T2-surjective','T2','expected','surjective_full_target',True),
        ('NC2-false-T2-strict','T2','expected','strict_equivalence_under_frozen_criterion',True),
        ('NC3-remove-T3-bridge','T3','bridge',None,None),
        ('NC4-false-T3-direct','T3','expected','correspondence_class','DIRECT_CORRESPONDENCE'),
        ('NC5-false-paper-hash',None,'formation','sha256','0'*64),
    ]
    controls = []
    for name, case_id, section, key, value in attacks:
        altered = copy.deepcopy(packet)
        if section=='formation': altered['formation'][key]=value
        else:
            c = next(t for t in altered['tasks'] if t['id']==case_id)
            if section=='bridge': c['bridge']=None
            else: c['expected'][key]=value
        detected = run(altered,a.formation)['verdict'] == 'FAIL_WITH_EVIDENCE'
        controls.append({'id':name, 'mutation_detected':detected})
    neg = {'audit_id':packet['id']+'-NEG', 'immutable_fixture_sha256':hashlib.sha256(raw).hexdigest(),
           'controls':controls, 'detected':sum(x['mutation_detected'] for x in controls),
           'total':len(controls), 'immutable_source_unchanged':Path(a.fixtures).read_bytes()==raw}
    Path(a.negative_output).write_text(json.dumps(neg,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'result':result['verdict'],'counts':result['counts'],
                      'negative_controls':f"{neg['detected']}/{neg['total']}"}))
    if result['verdict'] != 'PASS_WITH_BOUNDARY' or neg['detected'] != len(controls):
        raise SystemExit(1)

if __name__ == '__main__':
    main()
