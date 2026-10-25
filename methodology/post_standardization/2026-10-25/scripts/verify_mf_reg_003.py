#!/usr/bin/env python3
"""MF-REG-20261025-003: seven preserved historical fixtures, bounded source rebase.
Author: Kwon Dominicus. NOT an old-vs-new PDF or full method-protocol replay.
"""
import argparse, copy, hashlib, json
from fractions import Fraction
from pathlib import Path
import fitz


def calc(c):
    kind=c['kind']
    if kind=='typed_graph_strict':
        a,b,f=c['left'],c['right'],c['map']
        bij=set(f)==set(a['nodes']) and set(f.values())==set(b['nodes']) and len(f)==len(set(f.values()))
        inverse={v:k for k,v in f.items()}
        edge1={tuple(f[k] for k in e) for e in a['edges']}=={tuple(e) for e in b['edges']}
        edge2={tuple(inverse[k] for k in e) for e in b['edges']}=={tuple(e) for e in a['edges']}
        sts1=dict(zip(a['nodes'],a['status'])); sts2=dict(zip(b['nodes'],b['status']))
        status=all(sts1[k]==sts2[v] for k,v in f.items())
        strict=bij and edge1 and edge2 and status
        return dict(bijective=bij,edge_forward_preserved=edge1,edge_inverse_preserved=edge2,
                    status_preserved=status,strict_equivalent=strict,
                    correspondence_class='STRICT_EQUIVALENT' if strict else 'UNDETERMINED',
                    terminal='COMPARISON_RESOLVED' if strict else 'COMPARISON_UNDERDETERMINED')
    if kind=='aggregate_vs_support':
        x,y=sum(c['left']),sum(c['right']);bij=len(c['left'])==len(c['right'])
        assert not bij  # cardinality witness closes only the negative case
        return dict(left_sum=x,right_sum=y,aggregate_equal=x==y,bijective_support_map_possible=bij,
                    strict_equivalent=False,correspondence_class='NONCORRESPONDENCE',terminal='COMPARISON_RESOLVED')
    if kind=='combined_static':
        assert set(c['absent_channels']).isdisjoint(c['channels'])
        assert set(c['undefined_property']).isdisjoint(c['property'])
        def total(data,names):return [sum(data[k][i] for k in names) for i in range(2)]
        x=total(c['channels'],c['selected_channels']);y=total(c['property'],c['selected_property'])
        return dict(comp=x,agg=y,descriptor=[x,y],
                    channel_average=[str(Fraction(v,len(c['selected_channels']))) for v in x],
                    zero_channel_distinct_from_absence=any(v==[0,0] for v in c['channels'].values()) and bool(c['absent_channels']),
                    property_defined_zero_distinct_from_undefined=any(v==[0,0] for v in c['property'].values()) and bool(c['undefined_property']),
                    terminal='AGGREGATION_TASK_ESTABLISHED')
    if kind=='purpose_safe_drop_detail':
        src=c['data'];out={k:[v[i] for i in c['retained_indices']] for k,v in src.items()}
        collisions=[];safe=True;keys=list(src)
        for i,x in enumerate(keys):
            for y in keys[i+1:]:
                same=out[x]==out[y];purpose=(src[x][0],src[x][2])==(src[y][0],src[y][2])
                if same:collisions.append([x,y])
                if same and not purpose:safe=False
        old=sum(map(len,src.values()));new=sum(map(len,out.values()))
        return dict(out=out,safe_collisions=collisions,required_distinctions_preserved=safe,
                    original_cost=old,reduced_cost=new,strict_reduction=new<old,
                    terminal='COMPRESSION_TASK_ESTABLISHED' if safe and new<old else 'COMPRESSION_BLOCKED')
    if kind=='bounded_readout_fiber':
        v={k:sum(x) for k,x in c['data'].items()}
        good=[k for k,x in v.items() if x==c['observed_readout']];bad=[k for k in v if k not in good]
        return dict(readouts=v,compatible=good,excluded=bad,unique_within_class=len(good)==1,
                    set_outcome='RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS' if len(good)==1 else 'RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE',
                    terminal='RECONSTRUCTION_TASK_ESTABLISHED' if good else 'RECONSTRUCTION_TASK_UNDERDETERMINED')
    if kind=='bounded_prior_marker_transition':
        good=[k for k,v in c['data'].items() if v['marker']==c['observed_marker'] and v['transition_to_C']]
        return dict(compatible=good,excluded=[k for k in c['data'] if k not in good],unique_within_class=len(good)==1,
                    global_historical_unique_claim=False,
                    set_outcome='RECONSTRUCTION_SET_UNIQUE_WITHIN_DECLARED_CLASS' if len(good)==1 else 'RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE',
                    terminal='RECONSTRUCTION_TASK_ESTABLISHED' if good else 'RECONSTRUCTION_TASK_UNDERDETERMINED')
    if kind=='complete_interface_collision':
        assert c['interface_complete_for_claim']
        v={k:sum(x) for k,x in c['data'].items()}; good=[k for k,x in v.items() if x==c['observed_readout']]
        collision=len(good)>1 and len({tuple(c['data'][k]) for k in good})>1
        return dict(readouts=v,compatible=good,distinct_sources_same_readout=collision,
                    unrecoverable_on_declared_interface=collision and c['interface_complete_for_claim'],
                    globally_unrecoverable_claim=False,
                    set_outcome='RECONSTRUCTION_SET_MULTIPLE_COMPATIBLE' if collision else 'RECONSTRUCTION_SET_UNDETERMINED',
                    terminal='RECONSTRUCTION_TASK_ESTABLISHED' if collision else 'RECONSTRUCTION_TASK_UNDERDETERMINED')
    raise ValueError(kind)


def verify(f,paths):
    source={};formation=''
    for k,p in paths.items():
        sha=hashlib.sha256(Path(p).read_bytes()).hexdigest()
        with fitz.open(p) as d:
            count=len(d)
            if k=='formation':formation=' '.join(' '.join(x.get_text().split()) for x in d)
        expected=f['source_locks'][k]
        source[k]=sha==expected['sha256'] and count==expected['pages']
    anchors={q: q in formation for q in ('Proposition 5.13','This loss is not asserted for every formation model',
                                        'Proposition 5.14','Proposition 6.22','Corollary 6.26','independently prescribed J')}
    cases={};num=0;matched=0
    for item in f['cases']:
        got=calc(item);want=item['expected'];check={key:got.get(key)==value for key,value in want.items()}
        num+=len(check);matched+=sum(check.values())
        cases[item['id']]={'historical_case':item['original_case'],'method':item['method'],
                           'replayed':got,'expected':want,'field_checks':check,
                           'pass':all(check.values()) and set(got)==set(want),
                           'old_source_PDF_to_new_source_PDF':'BLOCKED_SOURCE_NOT_AVAILABLE'}
    passed=all(source.values()) and all(anchors.values()) and all(x['pass'] for x in cases.values())
    return {'audit_id':f['id'],'decision':'ARCHIVED_FIXTURE_REPLAY_PASS_WITH_BOUNDARY' if passed else 'FAIL_OR_BLOCKED_WITH_EVIDENCE',
            'source_locks':source,'formation_source_anchors':anchors,'cases':cases,
            'counts':{'cases_passed':sum(x['pass'] for x in cases.values()),'cases_total':len(cases),
                      'fields_matched':matched,'fields_total':num,'source_locks_passed':sum(source.values()),
                      'direct_old_vs_new_PDF_cases':0},
            'scope':'7 historical finite subcases from 4 methods; NOT complete scoring-gate reruns, formal proof or independent evaluation'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--fixtures',required=True);ap.add_argument('--output',required=True)
    ap.add_argument('--negative-output')
    for k in ('formation','property','aggregation','dynamics'):ap.add_argument('--'+k,required=True)
    a=ap.parse_args(); f=json.loads(Path(a.fixtures).read_text(encoding='utf-8'))
    paths={k:getattr(a,k) for k in ('formation','property','aggregation','dynamics')}
    result=verify(f,paths)
    Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    if a.negative_output:
        samples=[('wrong_T4_iso','CMP-T4','strict_equivalent',True),
                 ('erase_zero_absence','AGG-001','zero_channel_distinct_from_absence',False),
                 ('false_unique_fiber','RECON-A','unique_within_class',True)]
        control=[]
        for name,case,field,value in samples:
            bad=copy.deepcopy(f);next(x for x in bad['cases'] if x['id']==case)['expected'][field]=value
            control.append({'name':name,'rejected':verify(bad,paths)['decision']!='ARCHIVED_FIXTURE_REPLAY_PASS_WITH_BOUNDARY'})
        bad=copy.deepcopy(f);bad['source_locks']['formation']['sha256']='0'*64
        control.append({'name':'wrong_formation_sha','rejected':verify(bad,paths)['decision']!='ARCHIVED_FIXTURE_REPLAY_PASS_WITH_BOUNDARY'})
        Path(a.negative_output).write_text(json.dumps(control,indent=2)+'\n',encoding='utf-8')
        if not all(x['rejected'] for x in control):raise SystemExit(1)
    print(json.dumps(result['counts'],sort_keys=True))
    if result['decision']!='ARCHIVED_FIXTURE_REPLAY_PASS_WITH_BOUNDARY':raise SystemExit(1)
if __name__=='__main__':main()
