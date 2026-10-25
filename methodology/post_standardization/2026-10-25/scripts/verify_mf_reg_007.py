#!/usr/bin/env python3
"""MF-REG-20261025-007 — 22 archived A/F/G score-row evidence-gated audit.
Author: Kwon Dominicus. Does not reproduce historical complete proof/model.
"""
from __future__ import annotations
import argparse
import copy
from datetime import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import fitz

EXPECTED_SHA = {
 'formation': ('af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe', 34),
 'property': ('03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c', 23),
 'aggregation': ('9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d', 23),
}
ORIG = {
 'protocol': ('85b4263ad47cd10acd2230add542f381bd5d6a05', '5ac926aa40594126b42dac99762ff33fe87450f1'),
 'precommit': ('00e4afd77d7f10855f6c4d62eacbeaa154c3a2ce','a59810b90b2b93a0e3b63ba7f23dc59178bef566'),
 'result': ('21b54077a7fe48f690b7528b2ad0025d6b8a1325','7e5d071936d52655886a8a91141785cf7ed580f9'),
}


def hashblob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def source_check(paths):
    checks={}
    for k, p in paths.items():
        data=Path(p).read_bytes()
        with fitz.open(p) as doc:
            npages=len(doc)
            txt=' '.join(page.get_text().lower() for page in doc)
        sha=hashlib.sha256(data).hexdigest()
        anchor=({'formation':'proposition 5.13','property':'property','aggregation':'aggregation'}[k] in txt)
        checks[k]={'sha256':sha,'pages':npages,'locked':(sha,npages)==EXPECTED_SHA[k], 'text_anchor':anchor}
    return checks


def status(ok, reason, signal=None):
    return {'status':'PASS' if ok else 'FAIL','why':reason, 'signal':signal}


def blocked(reason):
    return {'status':'BLOCKED_EVIDENCE','why':reason,'signal':None}


def compute(q, b):
    h=q['historic_source_identity'];t=q['frozen_task'];post=q['frozen_postprocessing'];opt=q['optional_ledger'];sc=q['frozen_result_scope']
    cb=b['channel_ledger'];pr=b['property_ledger'];d=b['descriptor'];side=b['sidecars']
    f=b['selected_channel_support'];g=b['selected_property_support']
    fs=[sum(cb[k]['term'][i] for k in f) for i in (0,1)]
    ps=[sum(pr[k]['term'][i] for k in g) for i in (0,1)]
    avg=[Fraction(n,len(f)) for n in fs]
    avgtexts=[str(x) for x in avg]
    oriids=all(h[{'protocol':'original_protocol','precommit':'original_precommit','result':'original_result'}[k]]['verified_original_commit'] and (h[{'protocol':'original_protocol','precommit':'original_precommit','result':'original_result'}[k]]['commit'],h[{'protocol':'original_protocol','precommit':'original_precommit','result':'original_result'}[k]]['blob'])==ORIG[k] for k in ORIG)
    pre=datetime.fromisoformat(h['original_precommit']['timestamp_utc'].replace('Z','+00:00'))
    result=datetime.fromisoformat(h['original_result']['timestamp_utc'].replace('Z','+00:00'))
    chronology=pre<result and h['original_result']['direct_parent']==h['original_precommit']['commit']
    source_eq=t['formation_background_id']=='B-AGG-001' and t['property_model_id']=='A-AGG-001' and t['source_interface_id']=='AGG-CH-001-SOURCE-v1'
    policy=t['support_sidecar_required'] and t['negative_status_sidecar_required']
    labels=t['F']==f and t['G']==g
    sv=(all(cb[k]['admitted'] and cb[k]['selected'] for k in f) and all(pr[k]['in_defined_carrier'] and pr[k]['selected'] for k in g))
    ch=dict((k, {'value':cb[k]['term'],'status':cb[k]['status'],'provenance':cb[k]['provenance']}) for k in f)
    prop=dict((k, {'value':pr[k]['term'],'status':pr[k]['status'],'typed_inputs':pr[k]['typed_inputs'],'kind':pr[k]['kind'],'provenance':pr[k]['provenance']}) for k in g)
    neg=dict((k, {'value':pr[k]['term'],'status':pr[k]['status'],'typed_inputs':pr[k]['typed_inputs'],'kind':pr[k]['kind'],'provenance':pr[k]['provenance']}) for k in b['negative_property_status_sidecar'])
    side_ok=side['H_channel']==ch and side['H_property']==prop and side['negative_property']==neg
    fvalid=sv and fs==[1,4] and ps==[3,2] and side_ok and d['formation']['value']==fs and d['property']['value']==ps
    prior=q['prior_separate_audits']; prior_coverage=(prior['005']['passed']==24 and prior['006']['passed']==18 and len(set(prior['005']['row_ids']+prior['006']['row_ids']))==42 and prior['005']['original_row_result_blob']=='485d30075b52085df2f8a68e222446e79f49a845' and prior['006']['original_row_result_blob']=='773e9a3f3a4176dcb758985e34b543a2ab9d6af0')
    interface_ok=fvalid and source_eq and labels and policy and t['domain']=='finite' and opt['countable_extension']=='NOT_REQUESTED'
    bounded=(not sc['source_identity_claim'] and not sc['support_reconstruction_claim'] and not sc['global_injectivity_claim'] and not sc['external_validation_claim'] and sc['claim_scope']=='FINITE_AGGREGATES_COMBINED_DESCRIPTOR_SEPARATE_AVERAGE_ONLY')
    rows={
    'A1':status(oriids,'Original protocol/precommit/result SHA-and-blob identities must match connector-verified Git history.',oriids),
    'A2':status(t['id']=='AGG-CH-001' and t['version']==1,'Frozen original task identifier and version.',[t['id'],t['version']]),
    'A3':status(t['claim_level']=='COMBINED_STATIC_DESCRIPTOR','No post-result change of single primary claim level.',t['claim_level']),
    'A4':status(source_eq,'Both frozen source model IDs and original interface ID match.',source_eq),
    'A5':status(labels,'Original selected finite channel and property supports match copied prior input.',[f,g]),
    'A6':status(t['operator_id']=='AGG-SUM-v1' and t['W']=='R^2' and t['U']=='R^2' and t['output']=='R^2 x R^2','Original declared sum-operator ID and coordinate/output types preserved.',t['operator_id']),
    'A7':status(policy and side_ok,'Required actual full typed status and provenance sidecars available.',side_ok),
    'A8':status(chronology and oriids,'Git-result commit direct parent is old precommit, created 44 sec later; bounds only captured commit chain.',(result-pre).total_seconds()),
    'F1':status(avgtexts==['1/3','4/3'] and post['average']==avgtexts,'Exact Fraction arithmetic on three admitted channels, not float rounding.',avgtexts),
    'F2':status(post['id']=='EQUAL_WEIGHT_CHANNEL_AVERAGE-v1' and post['separate'] is True,'Postprocessing has separately frozen readout ID and type.',post['id']),
    'F3':status(not post['core_replaced'] and fs!=[float(v) for v in avg] and d['formation']['operator']=='FINITE_UNNORMALIZED_SUM','Normalized average does not replace finite direct component sum.',[fs,avgtexts]),
    'F4':status(opt['countable_extension']=='NOT_REQUESTED' and not d['countable_extension_requested'],'No illicit countable extension.',opt['countable_extension']),
    'F5':status(opt['collision']=='COLLISION_NOT_TESTED' and b['optional_ledgers']['collision']=='COLLISION_NOT_TESTED','Historic collision ledger preserved as untested despite separate limited 006 witness.',opt['collision']),
    'F6':status(opt['injectivity']=='INJECTIVITY_NOT_TESTED' and b['optional_ledgers']['injectivity']=='INJECTIVITY_NOT_TESTED','No injectivity promotion.',opt['injectivity']),
    'F7':status(opt['reconstruction']=='RECONSTRUCTION_NOT_CLAIMED' and b['optional_ledgers']['reconstruction']=='RECONSTRUCTION_NOT_CLAIMED','No source reconstruction claim.',opt['reconstruction']),
    'F8':status(opt['static_stability']=='NOT_REQUESTED' and opt['specialized_readout']=='NOT_REQUESTED','No dynamic/stability or specialized readout promoted.',[opt['static_stability'],opt['specialized_readout']]),
    'G1':status(interface_ok and prior_coverage and sc['terminal']=='AGGREGATION_TASK_ESTABLISHED','Conditional task terminal bounded by verified finite inputs; prior B/C D/E historical row evidence is separate.',interface_ok and prior_coverage),
    'G2':status(interface_ok and prior_coverage and bounded and sc['conformance']=='AGGREGATION_PROTOCOL_CONFORMANT','Finite-case protocol conformance under frozen scope and separate row attestations, not global method certification.',interface_ok and prior_coverage and bounded),
    'G3':status(sc['method_gain']=='AGGREGATION_METHOD_GAIN_NOT_ASSESSED','Method gain neither approved nor rejected.',sc['method_gain']),
    'G4':status(bounded and fs==[1,4] and ps==[3,2] and avgtexts==['1/3','4/3'],'Maximum supported claim restricted to finite F/G sums, descriptor and separately declared average.',bounded)
    }
    for label,field in [('G5','G5_protocol_revision_not_required'),('G6','G6_shared_core_reopening_not_required')]:
        attest=q['governance_external_attestation'].get(field)
        if not isinstance(attest,dict) or not attest.get('independent_evidence_digest'):
            rows[label]=blocked('Historical result says no revision/reopening, but no independently verifiable governance approval or signed evidence was supplied. Do not promote an archived assertion to a fresh positive check.')
        else:
            rows[label]=blocked('Unverified attestation shape; independent governance record needs a separate review, not this frozen case.')
    assert set(rows)==set(q['expected_rows']) and len(rows)==22
    return rows,{'formation_sum':fs,'property_sum':ps,'exact_average':avgtexts,
                 'historical_git_parent_direct':chronology,'git_result_offset_seconds':(result-pre).total_seconds(),
                 'sidecars_equal_original_sources':side_ok,'finite_interface_ok':interface_ok,
                 'bounded_claim':bounded,'prior_BCDE_row_ref_verified':prior_coverage}


def run(q, b, source):
    rows,signals=compute(q,b)
    failures=[k for k,v in rows.items() if v['status']=='FAIL']
    blocked_rows=[k for k,v in rows.items() if v['status']=='BLOCKED_EVIDENCE']
    source_ok=all(x['locked'] and x['text_anchor'] for x in source.values())
    if not source_ok or failures:outcome='FAIL_WITH_EVIDENCE'
    elif blocked_rows:outcome='PASS_WITH_BOUNDARY_AND_GOVERNANCE_EVIDENCE_OPEN'
    else:outcome='PASS_WITH_BOUNDARY'
    passes=sum(v['status']=='PASS' for v in rows.values())
    return {'audit_id':q['audit_id'],'verdict':outcome,'rows':rows,'signals':signals,'source_locks':source,
            'counts':{'A_pass':sum(rows[k]['status']=='PASS' for k in rows if k.startswith('A')),
                      'F_pass':sum(rows[k]['status']=='PASS' for k in rows if k.startswith('F')),
                      'G_pass':sum(rows[k]['status']=='PASS' for k in rows if k.startswith('G')),
                      'original_007_rows_total':22,'original_007_rows_pass':passes,'original_007_rows_blocked':len(blocked_rows),
                      'original_007_rows_failed':len(failures),'previous_distinct_BCDE_rows_passed':42,
                      'cumulative_distinct_original_rows_passed':42+passes,'remaining_governance_rows_unverified':blocked_rows,
                      'historical_64_of_64_archived_not_reused_as_new_score':True},
            'old_pdf_pair_replay':'BLOCKED_SOURCE_NOT_AVAILABLE',
            'historical_64_row_result_unchanged':True,
            'independent_external_evaluator_increment':0}


def main():
    a=argparse.ArgumentParser()
    a.add_argument('--fixtures',required=True);a.add_argument('--source-006-fixtures',required=True)
    for k in ('formation','property','aggregation'):a.add_argument('--'+k,required=True)
    a.add_argument('--output',required=True);a.add_argument('--negative-output',required=True)
    args=a.parse_args()
    data=Path(args.fixtures).read_bytes();q=json.loads(data)
    previous=Path(args.source_006_fixtures).read_bytes()
    assert hashblob(previous)==q['source_006_fixture']['blob'] and hashlib.sha256(previous).hexdigest()==q['source_006_fixture']['sha256']
    assert q['audit_id']=='MF-REG-20261025-007'
    source=source_check({k:getattr(args,k) for k in ('formation','property','aggregation')})
    b=json.loads(previous)
    result=run(q,b,source);result['frozen_fixture_sha256']=hashlib.sha256(data).hexdigest()
    # Negative controls: actively falsify substantive rows and hash source, and prevent fake G5 auto-promotion.
    attacks=[
        ('NC1_wrong_task_version', lambda z:z['frozen_task'].update(version=2),'A2'),
        ('NC2_wrong_aggsum_operator',lambda z:z['frozen_task'].update(operator_id='AVG-v1'),'A6'),
        ('NC3_false_F_average',lambda z:z['frozen_postprocessing'].update(average=['0','0']),'F1'),
        ('NC4_illicit_collision_claim',lambda z:z['optional_ledger'].update(collision='COLLISION_WITNESS_ESTABLISHED'),'F5'),
        ('NC5_wrong_terminal',lambda z:z['frozen_result_scope'].update(terminal='AGGREGATION_TASK_BLOCKED'),'G1'),
        ('NC6_unbounded_identity_claim',lambda z:z['frozen_result_scope'].update(source_identity_claim=True),'G4'),
        ('NC7_false_governance_true',lambda z:z['governance_external_attestation'].update(G5_protocol_revision_not_required=True),'G5')
    ]
    tested=[]
    for name,fn,target in attacks:
        w=copy.deepcopy(q);fn(w);row=run(w,b,source)['rows'][target]
        ok=row['status']==('BLOCKED_EVIDENCE' if target=='G5' else 'FAIL')
        tested.append({'id':name,'target_original_row':target,'detected':ok,'actual_status':row['status']})
    wrongsrc=copy.deepcopy(source);wrongsrc['formation']['locked']=False
    sourceguard=run(q,b,wrongsrc)['verdict']=='FAIL_WITH_EVIDENCE'
    tested.append({'id':'NC8_bad_formation_sha','target_original_row':None,'detected':sourceguard,'actual_status':'FAIL_WITH_EVIDENCE' if sourceguard else 'UNEXPECTED_PASS'})
    neg={'audit_id':'MF-REG-20261025-007-NC','mutations':tested,'detected_count':sum(x['detected'] for x in tested),
         'total_count':len(tested),'immutable_frozen_fixture_unchanged':Path(args.fixtures).read_bytes()==data,
         'immutable_006_fixture_unchanged':Path(args.source_006_fixtures).read_bytes()==previous}
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
    Path(args.negative_output).write_text(json.dumps(neg,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({'verdict':result['verdict'],'counts':result['counts'], 'negative_controls':str(neg['detected_count'])+'/'+str(neg['total_count'])},ensure_ascii=False))
    if result['verdict']!='PASS_WITH_BOUNDARY_AND_GOVERNANCE_EVIDENCE_OPEN' or neg['detected_count']!=neg['total_count']:
        raise SystemExit(1)

if __name__=='__main__':main()
