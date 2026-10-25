#!/usr/bin/env python3
"""MF-REG-20261025-005: archived AGG-CH-001 exact original B/C rows.
Author: Kwon Dominicus. Replays 24 B/C predicates, NOT historic full 64.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import fitz

EXPECTED_B = [f'B{i}' for i in range(1, 13)]
EXPECTED_C = [f'C{i}' for i in range(1, 13)]


def check_sources(packet, paths):
    verified = {}
    source_text = {}
    for key, filename in paths.items():
        content = Path(filename).read_bytes()
        with fitz.open(filename) as doc:
            pages = len(doc)
            text = ' '.join(page.get_text() for page in doc)
        lock = packet['source_files'][key]
        digest = hashlib.sha256(content).hexdigest()
        verified[key] = dict(sha256=digest, page_count=pages,
                             source_locked=digest == lock['sha256'] and pages == lock['pages'])
        source_text[key] = text.lower()
    anchors = {
        'formation.P5.13': 'proposition 5.13' in source_text['formation'],
        'formation.finite_component_sum': 'finite sum' in source_text['formation'],
        'property.typed_property_domain': 'typed' in source_text['property'] and 'undefined' in source_text['property'],
        'static.property_channel_handoff': 'property' in source_text['aggregation'] and 'channel' in source_text['aggregation'],
    }
    return verified, anchors


def evaluate_rows(packet):
    channel = packet['channels']
    prop = packet['properties']
    fs = packet['selected_channel_support']
    gs = packet['selected_property_support']

    # Calculate declared coordinate sums without taking the old result as an input.
    fsum = [sum(channel[x]['term'][i] for x in fs if channel[x]['term'] is not None) for i in range(2)]
    gsum = [sum(prop[x]['term'][i] for x in gs if prop[x]['term'] is not None) for i in range(2)]
    f_good = all(channel[x]['admitted'] and channel[x]['selected'] and channel[x]['term'] is not None for x in fs)
    g_good = all(prop[x]['in_defined_carrier'] and prop[x]['selected'] and prop[x]['term'] is not None for x in gs)
    c0 = channel['c0']; cx = channel['cX']; u1 = prop['u1']; i2 = prop['i2']
    rows = {
        'B1': channel['c1']['admitted'] and 'c1' in fs,
        'B2': channel['c2']['admitted'] and 'c2' in fs,
        'B3': c0['admitted'] and 'c0' in fs,
        'B4': not cx['admitted'] and 'cX' not in fs,
        'B5': c0['admitted'] and c0['term'] == [0,0] and c0['status'] == 'CHANNEL_PRESENT_TERM_DEFINED_ZERO',
        'B6': not cx['admitted'] and cx['term'] is None and cx['zero_extended'] is False,
        'B7': channel['c1']['term'] == [2,1] and channel['c1']['provenance'] == 'CH-TERM-01',
        'B8': channel['c2']['term'] == [-1,3] and channel['c2']['provenance'] == 'CH-TERM-02',
        'B9': c0['term'] == [0,0] and c0['provenance'] == 'CH-TERM-00',
        'B10': f_good and fsum == [1,4] == packet['formation_expected_sum'],
        'B11': packet['formation_core_operator'] == 'FINITE_UNNORMALIZED_SUM' and packet['formation_output_type'] == 'R^2',
        'B12': f_good and fsum == [1,4] and all(channel[x]['status'].startswith('CHANNEL_PRESENT_') for x in fs),
        'C1': prop['i1']['in_defined_carrier'] and prop['i1']['selected'] and prop['i1']['term'] is not None,
        'C2': i2['in_defined_carrier'] and i2['selected'] and i2['term'] is not None,
        'C3': prop['i0']['in_defined_carrier'] and prop['i0']['selected'] and prop['i0']['term'] == [0,0] and prop['i0']['status'] == 'PROPERTY_DEFINED_ZERO',
        'C4': u1['status'] == 'PROPERTY_APPLICABLE_UNDEFINED' and 'u1' in packet['negative_property_status_sidecar'] and u1['term'] is None,
        'C5': not u1['in_defined_carrier'] and not u1['selected'] and 'u1' not in gs,
        'C6': not u1['zero_padded'] and u1['term'] is None,
        'C7': i2['typed_inputs'] == ['x1','x2'] and i2['kind'] == 'p_binary',
        'C8': packet['allocation']['single_channel_selector'] is None and packet['allocation']['inferred_canonical_owner'] is None,
        'C9': prop['i1']['term'] == [4,0] and prop['i1']['provenance'] == 'PROP-01',
        'C10': i2['term'] == [-1,2] and i2['provenance'] == 'PROP-02',
        'C11': prop['i0']['term'] == [0,0] and prop['i0']['provenance'] == 'PROP-00',
        'C12': g_good and gsum == [3,2] == packet['property_expected_sum'] and packet['property_core_operator'] == 'FINITE_UNNORMALIZED_SUM',
    }
    assert list(rows) == packet['expected_row_ids'] == EXPECTED_B + EXPECTED_C
    return {k:bool(v) for k,v in rows.items()}, {'formation_sum':fsum, 'property_sum':gsum,
                'selected_channel_support':fs, 'selected_property_support':gs,
                'c0_admitted_zero':c0['admitted'] and c0['term'] == [0,0],
                'cX_absent':not cx['admitted'] and cx['term'] is None,
                'u1_undefined_not_in_carrier':u1['term'] is None and not u1['in_defined_carrier']}


def run(packet, paths):
    source, anchors = check_sources(packet, paths)
    rows, derived = evaluate_rows(packet)
    passed = all(z['source_locked'] for z in source.values()) and all(anchors.values()) and all(rows.values())
    return {'audit_id':packet['audit_id'], 'author':packet['author'], 'source_lock':source,
            'source_anchors':anchors, 'row_verdicts':rows, 'derived':derived,
            'counts':{'selected_original_rows':len(rows), 'passed_original_rows':sum(rows.values()),
                      'blocked_or_failed_original_rows':len(rows)-sum(rows.values()),
                      'remaining_original_AGG_CH_001_rows_not_executed':40,
                      'historical_orig_64_result_reused_as_new_check':0},
            'verdict':'PASS_WITH_BOUNDARY' if passed else 'FAIL_WITH_EVIDENCE',
            'direct_old_to_new_paper_pdf_comparison':'BLOCKED_SOURCE_NOT_AVAILABLE',
            'scope':'Only original 24 B/C scoring rows of the AGG-CH-001 64-row precommit; current Formation, Property and Static Aggregation source identity locked. No full original 64, independence or external validation.'}


def mutate(packet, paths):
    scenarios = [
        ('NC01_c0_not_admitted', lambda q: q['channels']['c0'].update(admitted=False), 'B3'),
        ('NC02_cX_falsely_zero_extended', lambda q: q['channels']['cX'].update(zero_extended=True,term=[0,0]), 'B6'),
        ('NC03_c1_wrong_component_term', lambda q: q['channels']['c1'].update(term=[2,2]), 'B7'),
        ('NC04_u1_undefined_changed_to_zero', lambda q: q['properties']['u1'].update(status='PROPERTY_DEFINED_ZERO',term=[0,0]), 'C4'),
        ('NC05_i2_input_order_swapped', lambda q: q['properties']['i2'].update(typed_inputs=['x2','x1']), 'C7'),
        ('NC06_property_pdf_hash_corrupt', lambda q: q['source_files']['property'].update(sha256='0'*64), None),
    ]
    results=[]
    for name, change, expected_failure_row in scenarios:
        q=copy.deepcopy(packet)
        change(q)
        observed=run(q,paths)
        row_failed = expected_failure_row is None or observed['row_verdicts'][expected_failure_row] is False
        results.append({'name':name, 'specific_failure_detected':row_failed,
                        'rejected':observed['verdict']=='FAIL_WITH_EVIDENCE' and row_failed,
                        'failure_row':expected_failure_row})
    return results


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--fixtures',required=True)
    for k in ('formation','property','aggregation'):p.add_argument('--'+k,required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--negative-output',required=True)
    a=p.parse_args()
    fixture_bytes=Path(a.fixtures).read_bytes()
    packet=json.loads(fixture_bytes)
    assert packet['audit_id']=='MF-REG-20261025-005'
    paths={k:getattr(a,k) for k in ('formation','property','aggregation')}
    report=run(packet,paths)
    control=mutate(packet,paths)
    report['original_fixture_sha256']=hashlib.sha256(fixture_bytes).hexdigest()
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
    negative={'audit_id':'MF-REG-20261025-005-NC','controls':control,
              'rejected':sum(c['rejected'] for c in control),'total':len(control),
              'original_fixture_byte_identical':Path(a.fixtures).read_bytes()==fixture_bytes}
    Path(a.negative_output).write_text(json.dumps(negative,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({'verdict':report['verdict'],'count':report['counts'],
                      'negative_rejected':negative['rejected'],'negative_total':negative['total']},ensure_ascii=False))
    if report['verdict']!='PASS_WITH_BOUNDARY' or negative['rejected']!=negative['total']:
        raise SystemExit(1)

if __name__=='__main__': main()
