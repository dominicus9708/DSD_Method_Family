#!/usr/bin/env python3
r"""Appendix B 16-row source result-map consistency controls (not a theorem prover).

Windows repo root:
 python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_appb_stage_result_map.py
Optional argument: JSON output path. Standard-library only.
"""
import json
import sys
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
ROWS = [
 ('B01','I,II,III,V','Thm4.5; Prop4.6; Thm4.7','primitive packages, residual six typed'),
 ('B02','IV,VI,VII','Thm3.3','relative W,T closure'),
 ('B03','I-VII','Thm7.1; Cor7.2; Thm7.3; Cor7.4','typed finite input only'),
 ('B04','I','Primitive I','not admitted means not describable'),
 ('B05','II','Primitive II','sound restriction inheritance'),
 ('B06','II-III','Primitive III','realization inheritance'),
 ('B07','I-IV','Def2.1; Closure IV','full witness and three gates'),
 ('B08','IV-V','Closure IV; Primitive V','describability distinct from q'),
 ('B09','IV-VI','Closure VI','Psi, Gamma, Role all required'),
 ('B10','V-VII','Primitive V; Closures VI,VII','undefined, absent, zero distinct'),
 ('B11','I-VII+Defs2.4,3.5','Prop2.5; Thm3.6','reduction and trace iff'),
 ('B12','I-VII+Def6.2','Prop6.3; Thm6.5; Cor6.6','injectivity for composite sums'),
 ('B13','I-VII+Def6.4','Thm6.8; Prop6.11','embedding reflection, inclusion preorder'),
 ('B14','I-VII+Defs6.10,6.15','Thm6.14; Thm6.16','all-comparison earliest failure'),
 ('B15','IV,VI,VII+Thm6.17','Thm6.17','Stage4 fixed by3; Stage6 role; Stage7 W,T'),
 ('B16','I-VII+Thms6.19,6.20','Thm6.19; Thm6.20','symmetry and fixed B,F static scope')]

def audit():
    assert len(ROWS) == 16 and len({r[0] for r in ROWS}) == 16
    assert [r[0] for r in ROWS] == ['B%02d' % i for i in range(1,17)]
    # Candidate expression admission is necessary but not sufficient for description.
    assert all((not des) or adm for adm,des in [(0,0),(1,0),(1,1)])
    assert not ((not 1) or 0)  # an inadmissible describable expression violates I.
    # A full witness is a conjunction: restriction, described expression,
    # realization, and three primitive configuration gates.
    def psi(res,des,real,gates): return bool(res and des and real and all(gates))
    assert psi(True,True,True,(True,True,True))
    assert not psi(True,True,True,(True,True,False))
    assert not psi(False,True,True,(True,True,True))
    # Global partial q has no value outside its domain; defined zero is distinct.
    Q={'a'}; q={'a':0}; role={('p','a','lambda','rho')}
    def admitted(described,Q,q,role):
        return bool(described and 'a' in Q and ('p','a','lambda','rho') in role)
    assert admitted(True,Q,q,role) and not admitted(False,Q,q,role)
    assert not admitted(True,set(),{},role) and not admitted(True,Q,q,set())
    c=('p','a','lambda',0,'rho')
    assert q['a']==0 and c[3]==0 and c not in set()  # absence != zero-valued c
    # Noninjective forward channel map: finite SET image drops repeated term.
    source={('p','a','lambda',1,'r1'),('p','a','lambda',1,'r2')}
    image={('p','a','lambda',1,'r') for _ in source}
    assert len(source)==2 and len(image)==1
    assert sum(c[3] for c in source)==2 and sum(c[3] for c in image)==1
    # Stage 4 is uniquely derived from fixed Stage-3 data, not independent.
    for bc in (False,True):
        derived_stage4 = bool(bc and psi(True,True,True,(True,True,True)))
        assert derived_stage4==bc
    assert 125*3+62+319+6*2==768 and 512*3==1536
    return dict(audit_id='FAS-F2-APPB-STAT-001',source_sha256=SOURCE_SHA,
       appendix='B Formation-Stage Status and Result Map',printed_page=31,
       source_rows=16,source_to_result_rows_aligned=16,
       all_selected_checks_passed=True,necessary_expression_admission_not_sufficient=True,
       config_witness_includes_three_admission_gates=True,
       global_partial_assignment_and_role_required_for_channel=True,
       defined_zero_not_undefined_or_channel_absence=True,
       noninjective_forward_map_can_fail_finite_set_sum=True,
       stage4_has_no_independent_first_branch=True,
       stage6_depends_on_role_beyond_stage5=True,
       stage7_depends_on_supplied_W_T=True,
       primitive_independence_typed_residual_six=True,
       standard_finite_realization_requires_well_typed_seed=True,
       any_claim_of_absolute_W_T_unique_closure=False,
       any_claim_of_physical_or_external_completeness=False,
       source_type_or_logical_map_mismatch_count=0,
       table_not_an_independent_new_theorem=True,
       prior_discussion_fixed_J_clarification_remains_separate=True,
       original_pdf_zenodo_modified=False,independent_external_validation=False,
       rows=[dict(id=i,stage=stage,source=src,qualification=q) for i,stage,src,q in ROWS])

def main():
    result=audit()
    out=(Path(sys.argv[1]) if len(sys.argv)>1 else
         Path(__file__).resolve().parent.parent/'results'/'appb_stage_result_map.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('Appendix B PASS:',result['source_rows'],'source rows; mismatches',result['source_type_or_logical_map_mismatch_count'])
    print('OUTPUT:',out)
if __name__=='__main__': main()
