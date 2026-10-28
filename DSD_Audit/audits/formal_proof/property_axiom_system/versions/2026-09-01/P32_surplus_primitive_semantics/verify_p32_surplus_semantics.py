#!/usr/bin/env python3
"""P32 finite discriminators for surplus primitive coordinate semantics.

These are conditional presentations, NOT claims that P27 author admits extended
presentations. All claims stay within the fixed illustrative finite signature.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

# Fixed inherited sort h={a}; shared candidate p profile (h), prerequisite=none.
# Tuple representation of inherited typed input x = (a,).
TYPED_INPUT = ('a',)
CANDIDATES = frozenset({'p'})


def presentation(*, declared=(), ap=None, sat=None, xi=None):
    ap = {} if ap is None else ap
    sat = {} if sat is None else sat
    xi = {} if xi is None else xi
    return {
        'declared': frozenset(declared),
        'ap': {k:frozenset(v) for k,v in ap.items()},
        'sat': {k:frozenset(v) for k,v in sat.items()},
        'xi': {k:tuple(sorted(v.items())) for k,v in xi.items()},
    }


def active(p):
    # In this fixed signature p is profile-available, and has no prerequisites.
    return frozenset(p['declared'] & CANDIDATES)


def normal(p):
    kinds = active(p)
    return presentation(
        declared=p['declared'],
        ap={k:p['ap'][k] for k in kinds if k in p['ap']},
        sat={k:p['sat'][k] for k in kinds if k in p['sat']},
        xi={k:dict(p['xi'][k]) for k in kinds if k in p['xi']},
    )


def is_well_typed_active(p):
    if not p['declared'] <= CANDIDATES:
        return False
    for k in active(p):
        if k not in p['ap'] or k not in p['xi']:
            return False
        if not p['ap'][k] <= frozenset({TYPED_INPUT}):
            return False
        domain = {x for x,_ in p['xi'][k]}
        if not domain <= frozenset({TYPED_INPUT}):
            return False
        if not domain <= p['ap'][k]:
            return False
    return True


def completion(p):
    assert is_well_typed_active(p), 'C1 applies only to well-typed PI/PII cores'
    derived = {}
    for kind in active(p):
        domain = frozenset(x for x,_ in p['xi'][kind])
        derived[kind] = {'domain':domain, 'record':p['xi'][kind]}
    # *** exact raw primitive coordinates remain unchanged ***
    return {'primitive':p, 'derived':derived}


def reduction(full):
    return full['primitive']


def strict_identity_core_iso(a,b):
    # S1-S3 all hold, h inherited identity; active comparison only.
    x,y=normal(a),normal(b)
    return x==y


def same_stage3_raw(a,b):
    # A literal comparison of raw stage-3 relation families.
    return a['ap']==b['ap'] and a['sat']==b['sat']


def run():
    a=presentation()
    b=presentation(ap={'p':{TYPED_INPUT}}) # surplus *undeclared* kind
    checks={}
    checks['shared_signature_has_one_candidate_and_inherited_typed_input']=len(CANDIDATES)==1 and TYPED_INPUT==('a',)
    checks['both_undeclared_profiles_have_no_active_kinds']=not active(a) and not active(b)
    checks['raw_surplus_models_differ']=a!=b
    checks['raw_surplus_input_is_well_typed_if_treated_as_extra']=b['ap']['p']<=frozenset({TYPED_INPUT})
    checks['canonical_restriction_equal']=normal(a)==normal(b)
    checks['strict_identity_core_iso_conditional_extended_class']=strict_identity_core_iso(a,b)
    checks['raw_stage3_records_differ']=not same_stage3_raw(a,b)
    checks['normalization_idempotent']=normal(normal(a))==normal(a) and normal(normal(b))==normal(b)
    checks['normalization_is_noninjective']=normal(a)==normal(b) and a!=b
    checks['exact_C1_reduction_works_if_surplus_retained']=reduction(completion(a))==a and reduction(completion(b))==b
    checks['canonicalizing_completion_would_break_raw_inverse']=normal(reduction(completion(b)))!=b
    checks['C1_derived_data_unchanged_by_normalization']=completion(a)['derived']==completion(b)['derived']==completion(normal(b))['derived']
    checks['raw_relation_stage3_vs_strict_core_comparison_disagree']=strict_identity_core_iso(a,b) and not same_stage3_raw(a,b)
    # Active nonempty controls: absent required primitive is distinct from explicitly empty.
    missing=presentation(declared={'p'})
    empty=presentation(declared={'p'},ap={'p':set()},xi={'p':{}})
    checks['missing_required_active_coordinate_rejected']=not is_well_typed_active(missing)
    checks['explicit_empty_active_coordinate_admitted']=is_well_typed_active(empty)
    checks['C1_empty_domain_on_explicit_empty']=completion(empty)['derived']['p']['domain']==frozenset()
    # Core raw data preservation is logically independent of strict comparison semantics.
    checks['raw_complete_descriptor_difference_does_not_imply_active_nonisomorphism']=a!=b and strict_identity_core_iso(a,b)
    assert all(checks.values()),{k:v for k,v in checks.items() if not v}
    return {
        'audit_id':'PA-P32-20261028-SURPLUS-PRIMITIVE-SEMANTICS',
        'scope':'finite conditional source discriminator; no user manuscript modified',
        'source_policy_not_fixed':True,
        'check_count':len(checks),
        'passed':sum(checks.values()),
        'checks':checks,
        'conclusion':'Exact C1 inverse survives under primitive-preserving extended-presentation semantics; strict identity core isomorphism ignores optional undeclared data. If raw stage3 families are compared literally, stage comparison differs. Canonical normalization idempotent but not injective, so cannot silently substitute for exact primitive retention.',
        'mathematical_verdict':'PRESENTATION_SCOPE_AMBIGUOUS / AXIOMS_NOT_REFUTED / C1_CONDITIONAL_PROOF',
        'revision_need':'SPECIFY_ACTIVE_PRIMITIVE_COORDINATE_DOMAIN_AND_RELATION_TO_DESCRIPTORS',
        'whole_FPA':'OPEN'
    }

if __name__=='__main__':
    data=run()
    if len(sys.argv)>1:
        path=Path(sys.argv[1]);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2))
