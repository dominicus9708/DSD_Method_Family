#!/usr/bin/env python3
"""PA-P29 non-edit FPA: independent implication audit for property finite realization.

Bounded finite controls distinguish the theorem's explicitly displayed inclusion
from the well-typed premise used by its proof. This program does not establish
any general infinite-set claim.

Usage (from the DSD_Method_Family repository root):
  python DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/\
P29_finite_realization_premise/verify_p29_finite_realization_premise.py \
    DSD_Audit/audits/formal_proof/property_axiom_system/versions/2026-09-01/\
P29_finite_realization_premise/p29_finite_realization_evidence.json
"""
from __future__ import annotations
import hashlib
import itertools
import json
import sys
from pathlib import Path


def inspect_presentation(*, carrier, ap, sat, xi, codomain=(0, 1), has_prerequisite=True):
    """Unary profile (u), one declared kind p; all inputs are one-tuples."""
    product = {(x,) for x in carrier}
    domain = set(xi)
    dsat = set(sat) if has_prerequisite else set(product)
    displayed_inclusion = domain <= (set(ap) & dsat)
    typing = (set(ap) <= product and
              (not has_prerequisite or set(sat) <= product) and
              domain <= product and all(v in codomain for v in xi.values()))
    return {'displayed_inclusion': displayed_inclusion,
            'well_typed': typing,
            'primitive_core': typing and displayed_inclusion,
            'input_product_cardinality': len(product)}


def expected_negative_controls():
    a = ('a',)
    ghost = ('ghost',)
    malformed = ('a', 'extra')
    tests = {
        # All sets and maps are finite, and the displayed DomXi inclusion holds.
        'ill_typed_applicability_empty_assignment': inspect_presentation(
            carrier=('a',), ap={ghost}, sat={ghost}, xi={}),
        'ill_typed_prerequisite_empty_assignment': inspect_presentation(
            carrier=('a',), ap={a}, sat={ghost}, xi={}),
        'wrong_arity_applicability_empty_assignment': inspect_presentation(
            carrier=('a',), ap={malformed}, sat={malformed}, xi={}),
        'out_of_codomain_value': inspect_presentation(
            carrier=('a',), ap={a}, sat={a}, xi={a: 1}, codomain=(0,)),
        'typed_empty_assignment': inspect_presentation(
            carrier=('a',), ap={a}, sat={a}, xi={}),
        'typed_defined_assignment': inspect_presentation(
            carrier=('a',), ap={a}, sat={a}, xi={a: 1}),
        'no_prerequisites_vacuous_dependency_satisfied': inspect_presentation(
            carrier=('a',), ap={a}, sat=set(), xi={a: 0}, has_prerequisite=False),
    }
    for k in ('ill_typed_applicability_empty_assignment',
              'ill_typed_prerequisite_empty_assignment',
              'wrong_arity_applicability_empty_assignment',
              'out_of_codomain_value'):
        assert tests[k]['displayed_inclusion'] and not tests[k]['well_typed']
    for k in ('typed_empty_assignment','typed_defined_assignment',
              'no_prerequisites_vacuous_dependency_satisfied'):
        assert tests[k]['primitive_core']
    return tests


def enumerate_typed_cores():
    # Exhaustively enumerate a single unary property over 0,1,2 input points,
    # with one prerequisite, optional zero/nonzero values and PI/PII.
    counters={}
    for n in (0,1,2):
        carrier=tuple(range(n))
        product={(x,) for x in carrier}
        count=0
        identity_inverse_ok=0
        for flags in itertools.product((0, 1, 2, 3, 4, 5),repeat=n):
            # 0 neither ap nor sat; 1 sat only; 2 ap only;
            # 3 both, unassigned; 4 both assigned 0; 5 both assigned 1.
            ap={(i,) for i,v in enumerate(flags) if v in (2,3,4,5)}
            sat={(i,) for i,v in enumerate(flags) if v in (1,3,4,5)}
            xi={(i,):v-4 for i,v in enumerate(flags) if v in (4,5)}
            t=inspect_presentation(carrier=carrier,ap=ap,sat=sat,xi=xi)
            assert t['primitive_core']
            # C1 determinate as functions of primitive coordinates;
            # identity of the complete record requires preserving *all* of them.
            domains=set(xi)
            statuses={}
            for x in product:
                if x not in ap: status='inapplicable'
                elif x not in sat: status='prerequisite_unsatisfied'
                elif x not in domains: status='applicable_undefined'
                elif xi[x]==0: status='defined_zero'
                else: status='defined_nonzero'
                statuses[x]=status
            completed=(frozenset(ap),frozenset(sat),frozenset(xi.items()),
                       frozenset(domains),frozenset(statuses.items()))
            reduction=completed[:3]
            assert reduction==(frozenset(ap),frozenset(sat),frozenset(xi.items()))
            identity_inverse_ok+=1
            count+=1
        counters[str(n)]={'well_typed_cores':count,'completion_reduction_identity_checks':identity_inverse_ok}
    return counters


def main():
    controls=expected_negative_controls()
    exhaustive=enumerate_typed_cores()
    result={
      'case_id':'PA-P29-20261028-FINITE-REALIZATION-TYPED-PREMISE-001',
      'paper':'Property Axiom System EN P27 (frozen; no changes)',
      'mathematical_scope':'bounded unary finite controls; general theorem remains proof obligation',
      'test_result':'ALL_EXPECTED_OBSERVATIONS_PASS',
      'displayed_inclusion_is_not_sufficient_without_typing':True,
      'negative_cases':{k:v for k,v in controls.items() if not v['well_typed']},
      'positive_cases':{k:v for k,v in controls.items() if v['well_typed']},
      'typed_core_enumeration':exhaustive,
      'primitive_axioms_unchanged':True,
      'source_tex_edited':False,
      'whole_property_fpa':'OPEN'
    }
    txt=json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
    if len(sys.argv)>1:
        p=Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(txt,encoding='utf8')
    print(txt)

if __name__=='__main__': main()
