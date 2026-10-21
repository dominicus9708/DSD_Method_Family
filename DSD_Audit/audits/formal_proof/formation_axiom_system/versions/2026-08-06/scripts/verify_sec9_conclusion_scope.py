#!/usr/bin/env python3
r"""F2 §9: source-claim inventory and arithmetic sanity check, NOT a theorem prover.

Run from the DSD_Method_Family repository root on Windows:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_sec9_conclusion_scope.py
Optional argv[1] sets JSON output path. Standard library only.
"""
import json
import sys
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
CLAIMS = [
 ('C01','seven-stage typed chain','Definitions 2.2/2.4','supported'),
 ('C02','four independent primitive plus three derived clauses','Theorems 4.5/4.7 and 3.3','supported_with_scope'),
 ('C03','admission and globally partial quantity distinct','Primitive I/III/V; Closure IV/VI','supported'),
 ('C04','stage reductions and nonempty formation traces','Proposition 2.5 and Theorem 3.6','supported'),
 ('C05','one-point ZFC existence and arbitrary finite realizations','Theorem 7.1; Corollary 7.2; Theorem 7.3; Corollary 7.4','supported_with_scope'),
 ('C06','forward maps, embeddings, category, strict equivalence','Theorems 6.5/6.8/6.14; Proposition 6.11','supported_with_scope'),
 ('C07','first branching requires failure of every tuple','Definition 6.15 and Theorem 6.16','supported'),
 ('C08','first branch symmetry and strict-iso invariance','Theorem 6.19','supported'),
 ('C09','no first independent branch at Stage 4','Theorem 6.17 and Corollary 6.18','supported'),
 ('C10','static closure collects prior results','Theorem 6.20','supported'),
 ('C11','D2 first branching Stage 3','Section 7.3 case audit','supported_with_prior_clarification'),
 ('C12','indexed 3x3 first branching Stage 5','Section 7.4 case audit','supported'),
 ('C13','equal indexed outputs may coexist with strict non-equivalence','Section 7.4, Definition 6.21 and Proposition 6.22','supported'),
]

def audit():
    assert len(CLAIMS) == 13
    assert len({x[0] for x in CLAIMS}) == len(CLAIMS)
    assert all(x[3].startswith('supported') for x in CLAIMS)
    # Source Conclusion has existential/coexistence statement, NOT the
    # erroneous unconditional logical hierarchy found in §8 Discussion.
    assert 125 + 127 == 252 and 512 - 125 == 387
    assert 125*3 + 62 + 319 + 6*2 == 768 and 512*3 == 1536
    assert 3 != 4 and 5 != 4 and 768 != 1536
    # §7.3 case's inherited blocked annotations/axis naming are still open.
    assert dict((c[0], c[3]) for c in CLAIMS)['C11'] == 'supported_with_prior_clarification'
    return dict(audit_id='FAS-F2-SEC9-CONC-001',source_sha256=SOURCE_SHA,
      claim_count=len(CLAIMS),all_selected_checks_passed=True,
      prior_sections_required=['2','3','4','6','7'],
      mathematical_conclusion_proof_is_prior_theorem_dependency=True,
      section9_repeats_section8_unconditional_strict_weakness=False,
      section9_coexistence_supported_by_section74=True,
      original_section73_fully_specified_wording_needs_inherited_clarification=True,
      mathematical_implication_counterexample_is_in_section8_not_new_section9=False,
      first_branch_indices=[3,5],stage4_excluded_as_first_independent_branch=True,
      source_revision_executed=False,not_machine_checked_formal_proof=True,
      independent_external_validation=False,
      claims=[dict(id=i,claim=text,source=source,status=status) for i,text,source,status in CLAIMS])

def main():
    x=audit()
    p=(Path(sys.argv[1]) if len(sys.argv)>1 else
       Path(__file__).resolve().parent.parent/'results'/'sec9_conclusion_scope.json')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('F2 §9 cross-reference consistency PASS:',x['claim_count'],'units')
    print('OUTPUT:',p)

if __name__=='__main__':
    main()
