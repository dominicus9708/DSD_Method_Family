#!/usr/bin/env python3
"""MF-REG-20261025-006: D/E 18 historically frozen AGG-CH-001 scoring rows.
Author: Kwon Dominicus. Does not certify all 64 rows or old/new PDF parity.
"""
import argparse,copy,hashlib,json
from pathlib import Path
import fitz

def vsum(register,names):
    assert all(isinstance(register[k]['term'],list) and len(register[k]['term'])==2 for k in names)
    return [sum(register[k]['term'][i] for k in names) for i in (0,1)]

def check(packet,paths):
    source={}
    anchors={}
    for k,p in paths.items():
        digest=hashlib.sha256(Path(p).read_bytes()).hexdigest()
        with fitz.open(p) as doc:
            n=len(doc)
            txt=' '.join(page.get_text().lower() for page in doc)
        expect=packet['source_files'][k]
        source[k]={'pages':n,'sha256':digest,'verified':n==expect['pages'] and digest==expect['sha256']}
        if k=='formation':
            anchors['formation.conditional_zero_loss']='proposition 5.13' in txt
            anchors['formation.finite_composition']='proposition 5.14' in txt
        elif k=='property': anchors['property.typed_and_undefined']='typed' in txt and 'undefined' in txt
        else: anchors['static.aggregation_source']='aggregation' in txt and 'property' in txt

    c,pr=packet['channel_ledger'],packet['property_ledger']
    f,g=packet['selected_channel_support'],packet['selected_property_support']
    d,sc,cl=packet['descriptor'],packet['sidecars'],packet['claim_interface']
    fc,pc=d['formation'],d['property']
    fsum,psum=vsum(c,f),vsum(pr,g)
    hc={k:{'value':c[k]['term'],'status':c[k]['status'],'provenance':c[k]['provenance']} for k in f}
    hp={k:{'value':pr[k]['term'],'status':pr[k]['status'],'typed_inputs':pr[k]['typed_inputs'],'kind':pr[k]['kind'],'provenance':pr[k]['provenance']} for k in g}
    hn={k:{'value':pr[k]['term'],'status':pr[k]['status'],'typed_inputs':pr[k]['typed_inputs'],'kind':pr[k]['kind'],'provenance':pr[k]['provenance']} for k in packet['negative_property_status_sidecar']}
    ch_ok,pr_ok,neg_ok=sc.get('H_channel')==hc,sc.get('H_property')==hp,sc.get('negative_property')==hn
    fv=(all(c[k]['admitted'] and c[k]['selected'] and c[k]['term'] is not None for k in f) and fc['operator']=='FINITE_UNNORMALIZED_SUM' and fc['support']==f and fc['source_id']=='B-AGG-001')
    pv=(all(pr[k]['selected'] and pr[k]['in_defined_carrier'] and pr[k]['term'] is not None for k in g) and pc['operator']=='FINITE_UNNORMALIZED_SUM' and pc['support']==g and pc['source_id']=='A-AGG-001')
    val=fc['value']==fsum and pc['value']==psum
    roles=d['ordered_coordinates']==['formation','property'] and d['source_relation']=='DISTINCT_TYPED_COORDINATES'
    fminus=[k for k in f if k!='c0']
    witness=(c['c0']['admitted'] and c['c0']['term']==[0,0] and fminus!=f and all(c[k]['admitted'] for k in fminus) and vsum(c,fminus)==fsum)
    u1=pr['u1']
    undef=u1['status']=='PROPERTY_APPLICABLE_UNDEFINED' and u1['term'] is None and not u1['in_defined_carrier'] and 'u1' not in g
    rows={
      'D1':val and [fsum,psum]==[[1,4],[3,2]],
      'D2':d['ordered_coordinates'][0]=='formation' and fc['family']=='F' and fc['support']==f,
      'D3':d['ordered_coordinates'][1]=='property' and pc['family']=='G' and pc['support']==g,
      'D4':roles and fc['source_id']!=pc['source_id'] and fc['family']!=pc['family'],
      'D5':ch_ok and pr_ok and all(c[k]['provenance'] for k in f) and all(pr[k]['provenance'] for k in g),
      'D6':d['domain']=='FINITE' and fv and pv,
      'D7':not d['countable_extension_requested'] and d['domain']=='FINITE',
      'D8':fv and pv and val and roles and d['combined_claim']=='COMBINED_STATIC_DESCRIPTOR_ESTABLISHED',
      'E1':ch_ok,
      'E2':pr_ok,
      'E3':neg_ok and 'u1' in packet['negative_property_status_sidecar'],
      'E4':c['c0']['admitted'] and c['c0']['term']==[0,0] and c['c0']['status']=='CHANNEL_PRESENT_TERM_DEFINED_ZERO' and 'c0' in f and sc.get('H_channel',{}).get('c0',{}).get('status')=='CHANNEL_PRESENT_TERM_DEFINED_ZERO',
      'E5':not c['cX']['admitted'] and c['cX']['term'] is None and 'cX' not in f and c['cX']['status']=='CHANNEL_ABSENT' and 'cX' not in sc.get('H_channel',{}),
      'E6':pr['i0']['term']==[0,0] and pr['i0']['status']=='PROPERTY_DEFINED_ZERO' and sc.get('H_property',{}).get('i0',{}).get('status')=='PROPERTY_DEFINED_ZERO',
      'E7':undef and sc.get('negative_property',{}).get('u1',{}).get('status')=='PROPERTY_APPLICABLE_UNDEFINED' and sc.get('negative_property',{}).get('u1',{}).get('value') is None,
      'E8':cl['source_identity_from_aggregate'] is False and witness,
      'E9':cl['support_identity_from_aggregate'] is False and cl['reconstruction_from_aggregate'] is False and witness,
      'E10':ch_ok and pr_ok and neg_ok and cl['channel_support_required'] and cl['property_support_required'] and cl['negative_status_required']
    }
    assert list(rows)==packet['expected_rows']
    rows={k:bool(v) for k,v in rows.items()}
    ok=all(x['verified'] for x in source.values()) and all(anchors.values()) and all(rows.values())
    return {'audit_id':packet['audit_id'],'verdict':'PASS_WITH_BOUNDARY' if ok else 'FAIL_WITH_EVIDENCE',
            'source_lock':source,'source_anchors':anchors,'row_results':rows,
            'derived':{'formation_sum':fsum,'property_sum':psum,'combined':[fsum,psum],
                       'support_witness':{'F_original':f,'F_without_admitted_zero':fminus,
                           'sum_original':fsum,'sum_without_zero':vsum(c,fminus),
                           'different_support_same_output':bool(witness)},
                       'sidecar_status':{'channel':bool(ch_ok),'property':bool(pr_ok),'negative':bool(neg_ok)},
                       'historical_collision_ledger':packet['optional_ledgers']['collision']},
            'counts':{'original_D_rows_pass':sum(v for k,v in rows.items() if k.startswith('D')),
                      'original_E_rows_pass':sum(v for k,v in rows.items() if k.startswith('E')),
                      'original_rows_rerun_this_audit':18,'original_rows_pass':sum(rows.values()),
                      'prior_005_distinct_BC_rows':24,'cumulative_distinct_original_rows_005_006_if_pass':42 if ok else None,
                      'remaining_A_F_G_rows_not_reexecuted':22,'historical_64_reused_as_new_pass':0},
            'old_formation_pdf_direct_comparison':'BLOCKED_SOURCE_NOT_AVAILABLE',
            'independent_validation_increment':0,
            'boundary':'Historical D/E 18 score rows only; auxiliary original-channel algebraic witness does not modify COLLISION_NOT_TESTED in archived AGG-CH-001.'}

def main():
    ap=argparse.ArgumentParser()
    for name in ('fixtures','formation','property','aggregation','output','negative-output'):
        ap.add_argument('--'+name,required=True)
    opt=ap.parse_args()
    b=Path(opt.fixtures).read_bytes()
    p=json.loads(b)
    assert p['audit_id']=='MF-REG-20261025-006' and len(p['expected_rows'])==18 and p['expected_each_row_pass']
    paths={name:getattr(opt,name) for name in ('formation','property','aggregation')}
    result=check(p,paths)
    changes=[
      ('NC1_corrupt_combined_property_coordinate',lambda q:q['descriptor']['property'].update(value=[3,3]),'D1'),
      ('NC2_swap_coordinate_roles',lambda q:q['descriptor'].update(ordered_coordinates=['property','formation']),'D2'),
      ('NC3_erase_H_channel_c0',lambda q:q['sidecars']['H_channel'].pop('c0'),'E1'),
      ('NC4_drop_undefined_sidecar',lambda q:q['sidecars']['negative_property'].clear(),'E3'),
      ('NC5_admitted_zero_reclassified_absent',lambda q:q['channel_ledger']['c0'].update(admitted=False,status='CHANNEL_ABSENT'),'E4'),
      ('NC6_promote_reconstruction_from_aggregate',lambda q:q['claim_interface'].update(reconstruction_from_aggregate=True),'E9'),
      ('NC7_corrupt_formation_sha',lambda q:q['source_files']['formation'].update(sha256='0'*64),None),
    ]
    negatives=[]
    for name,mutate,row in changes:
        x=copy.deepcopy(p);mutate(x)
        r=check(x,paths)
        failure=(r['row_results'].get(row) is False) if row else not r['source_lock']['formation']['verified']
        negatives.append({'id':name,'target_row':row,'specific_target_failed':failure,
                          'rejected':r['verdict']=='FAIL_WITH_EVIDENCE' and failure})
    neg={'audit_id':'MF-REG-20261025-006-NC',
         'fixture_sha256':hashlib.sha256(b).hexdigest(),
         'immutable_fixture_unchanged':Path(opt.fixtures).read_bytes()==b,
         'controls':negatives,'detected':sum(t['rejected'] for t in negatives),
         'total':len(negatives)}
    Path(opt.output).write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    Path(opt.negative_output).write_text(json.dumps(neg,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'verdict':result['verdict'],'counts':result['counts'],'negative':f"{neg['detected']}/{neg['total']}"}))
    if result['verdict']!='PASS_WITH_BOUNDARY' or neg['detected']!=neg['total']:raise SystemExit(1)
if __name__=='__main__':main()
