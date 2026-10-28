#!/usr/bin/env python3
"""Source-locked PA-P35 FPA obligation ledger. Not a ZFC proof checker.
Kwon Dominicus. No P27 manuscript modifications.
Run from DSD_Method_Family root:
python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/P35_integrated_fpa_closure_ledger/verify_p35_fpa_ledger.py --out DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/P35_integrated_fpa_closure_ledger/replay/P35_LEDGER_RESULT.json
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

SHA = {
    'EN': '51c194ec33f802a2061b68b3521fdb831f0f754a0386fa72f8e89a39efff7bdb',
    'KR': 'a643ea619f9594142bfc09b9f486c948cf0a85679a3b2a8a43bc731a1e108fbb',
}
BLOCKERS = {
    'S-01': {
        'items': [5, 6, 7, 9], 'status': 'SEMANTIC_CONVENTION_NOT_FIXED',
        'question': 'Restrict primitive families to active declared available profiles, or retain surplus raw presentations with separate core comparison?',
    },
    'S-02': {
        'items': [10], 'status': 'EXPLICIT_TYPED_PREMISE_REQUIRED',
        'question': 'Does finite primitive presentation expressly inherit all Def2.5 typed-premodel constraints beyond PI/PII?',
    },
    'S-03': {
        'items': [9], 'status': 'I_K_SOURCE_EQUIVALENCE_NOT_CERTIFIED',
        'depends_on': ['S-01'],
        'question': 'Is Def7.1 stage-comparison over active primitive coordinates (P33 proof) rather than all raw coordinates?',
    },
    'S-04': {
        'items': [3, 11, 12], 'status': 'UNIVERSAL_FIXED_SIGNATURE_VERSION_DISPROVED',
        'question': 'Separate universal per-fixed-signature structural claims from existential family-level witnesses.',
    },
}
ITEMS = {
    1: 'DEFINITIONAL_SUPPORTED', 2: 'AXIOM_CONTENT_SUPPORTED',
    3: 'BLOCKED_S04', 4: 'DEFINITIONAL_STATUS_SUPPORTED',
    5: 'CONDITIONAL_S01', 6: 'CONDITIONAL_S01', 7: 'CONDITIONAL_S01',
    8: 'CONDITIONAL_FIXED_REPRESENTATION_SIGNATURE',
    9: 'CONDITIONAL_S01_S03', 10: 'CONDITIONAL_S02',
    11: 'BLOCKED_S04', 12: 'BLOCKED_S04', 13: 'SUPPORTED_FIXED_STAGEVI_INTERFACE',
}

def main(root):
    checks, source_lock = {}, {}
    for lang in ('EN', 'KR'):
        p = root / 'P27_independent_math_revision' / ('DSD_Property_Axiom_System_%s_P27_REVISED.tex' % lang)
        raw = p.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        s = raw.decode('utf-8')
        checks[lang + '_source_frozen_SHA256_match'] = sha == SHA[lang]
        start = s.find(r'\label{thm:main}')
        assert start >= 0, 'missing main theorem'
        tail = s[start:]
        k, z = tail.find(r'\begin{enumerate}'), tail.find(r'\end{enumerate}')
        assert k >= 0 and z > k
        item_count = len(re.findall(r'\\item\s+', tail[k:z]))
        checks[lang + '_main_theorem_has_13_items'] = item_count == 13
        i = s.find(r'\label{def:premodel}')
        j = s.find(r'\end{definition}', i)
        block = s[i:j] if i >= 0 and j > i else ''
        checks[lang + '_Def2_5_not_required_source_present'] = (
            ('is required.' in block and 'If' in block) if lang == 'EN'
            else '요구하지 않는다' in block
        )
        checks[lang + '_section11_has_fixed_base'] = (
            'Fix a Stage-VI DSD formation record' in tail[:220]
            if lang == 'EN' else (r'\FVI' in tail[:220] and r'\Sprop' in tail[:220])
        )
        source_lock[lang] = {'source_bytes': len(raw), 'main_theorem_items': item_count, 'sha256': sha}

    with (root/'P32_surplus_primitive_semantics'/'P32_EXPECTED_EVIDENCE.json').open(encoding='utf-8') as f:
        p32 = json.load(f)
    with (root/'P34_fixed_signature_quantifier_scope'/'P34_FIXED_SIGNATURE_EVIDENCE.json').open(encoding='utf-8') as f:
        p34 = json.load(f)
    checks['P32_17_finite_conditional_expectations_pass'] = p32['passed'] == 17 and p32['check_count'] == 17 and all(p32['checks'].values())
    checks['P32_semantics_not_decided'] = p32['source_policy_not_fixed'] is True
    checks['P34_15_finite_conditional_expectations_pass'] = p34['passed'] == 15 and p34['total'] == 15 and all(p34['checks'].values())
    checks['P34_quantifier_counterexample_still_open'] = p34['claims']['fixed_signature_universal_3_11_12'] == 'DISPROVED_BY_EMPTY_SIGNATURE'
    checks['P34_refers_to_same_frozen_P27'] = p34['frozen_p27_source_sha256'] == SHA
    checks['dependency_S03_requires_S01'] = BLOCKERS['S-03']['depends_on'] == ['S-01']
    checks['exactly_13_distinct_theorem_items'] = set(ITEMS) == set(range(1, 14))
    checks['four_unresolved_source_obligation_clusters'] = set(BLOCKERS) == {'S-01', 'S-02', 'S-03', 'S-04'}
    assert all(checks.values()), 'P35 source/evidence mismatch: ' + str([k for k,v in checks.items() if not v])
    result = {
        'audit_id': 'PA-P35-20261029-INTEGRATED-FPA-CLOSURE-LEDGER',
        'source_lock': source_lock,
        'item_statuses': {str(k): v for k,v in ITEMS.items()},
        'unresolved_clusters': BLOCKERS,
        'unresolved_clusters_count': len(BLOCKERS),
        'independent_blocker_branches': [['S-01','S-03'], ['S-02'], ['S-04']],
        'checks': checks, 'passed_checks': sum(checks.values()), 'check_count': len(checks),
        'no_new_mathematical_proof_from_this_script': True,
        'audit_readiness': 'SOURCE_LOCKED_DEPENDENCY_LEDGER_COMPLETE__AUTHOR_SCOPE_DECISION_OPEN',
        'manuscript_edited': False, 'whole_property_fpa': 'OPEN',
        'closure_rule': 'P27 FPA not CLOSED on frozen literal source; first finish review, then batch-revise and re-audit final revised paper before CLOSED.',
        'external_review': 'NOT_ESTABLISHED',
    }
    return result

if __name__ == '__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--versions-root', type=Path, default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--out', type=Path)
    opts=ap.parse_args()
    result=main(opts.versions_root)
    body=json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2)+'\n'
    if opts.out:
        opts.out.parent.mkdir(parents=True,exist_ok=True)
        opts.out.write_text(body,encoding='utf-8')
    print('P35 SOURCE AND PRIOR EVIDENCE LOCK PASS:',result['passed_checks'],'/',result['check_count'])
    print('FPA status:',result['whole_property_fpa'],'; unresolved clusters:',result['unresolved_clusters_count'])
