#!/usr/bin/env python3
"""FAS F2 source-label inventory, not a mathematical proof.

Requires PyMuPDF: python -m pip install pymupdf
Run from the cloned DSD_Method_Family root:
  python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_f2_claim_inventory.py --pdf "PATH_TO_ORIGINAL_PDF"
JSON is saved under the established results/ folder.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import fitz

SOURCE_SHA='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
ROOT='DSD_Audit/audits/formal_proof/formation_axiom_system/'
EVIDENCE={
 'G0':'SECTION_AUDITS/FAS-F2-G0-001_RESULT.md',
 'T3.3':'THEOREM_AUDITS/FAS-F2-T3.3-001_RESULT.md',
 'T3.6':'THEOREM_AUDITS/FAS-F2-T3.6-001_RESULT.md',
 'T4.5':'THEOREM_AUDITS/FAS-F2-T4.5-001_RESULT.md',
 'T4.7':'THEOREM_AUDITS/FAS-F2-T4.7-001_RESULT.md',
 'S4.3':'SECTION_AUDITS/FAS-F2-SEC4.3-001_RESULT.md',
 'S5':'SECTION_AUDITS/FAS-F2-G3-SEC5-001_RESULT.md',
 'T6.5':'THEOREM_AUDITS/FAS-F2-T6.5-001_RESULT.md',
 'S6.6-6.7':'SECTION_AUDITS/FAS-F2-SEC6.2-C6.6-C6.7-001_RESULT.md',
 'T6.8':'THEOREM_AUDITS/FAS-F2-T6.8-001_RESULT.md',
 'P6.11':'THEOREM_AUDITS/FAS-F2-P6.11-001_RESULT.md',
 'C6.12':'SECTION_AUDITS/FAS-F2-C6.12-001_RESULT.md',
 'T6.14':'THEOREM_AUDITS/FAS-F2-T6.14-001_RESULT.md',
 'T6.16':'THEOREM_AUDITS/FAS-F2-T6.16-001_RESULT.md',
 'T6.17':'THEOREM_AUDITS/FAS-F2-T6.17-001_RESULT.md',
 'C6.18':'SECTION_AUDITS/FAS-F2-C6.18-001_RESULT.md',
 'T6.19':'THEOREM_AUDITS/FAS-F2-T6.19-001_RESULT.md',
 'T6.20':'THEOREM_AUDITS/FAS-F2-T6.20-001_RESULT.md',
 'P6.22':'THEOREM_AUDITS/FAS-F2-P6.22-001_RESULT.md',
 'T6.23':'THEOREM_AUDITS/FAS-F2-T6.23-001_RESULT.md',
 'C6.24':'THEOREM_AUDITS/FAS-F2-C6.24-001_RESULT.md',
 'C6.25':'THEOREM_AUDITS/FAS-F2-C6.25-001_RESULT.md',
 'C6.26':'THEOREM_AUDITS/FAS-F2-C6.26-001_RESULT.md',
 'T7.1':'THEOREM_AUDITS/FAS-F2-T7.1-001_RESULT.md',
 'C7.2':'THEOREM_AUDITS/FAS-F2-C7.2-001_RESULT.md',
 'T7.3':'THEOREM_AUDITS/FAS-F2-T7.3-001_RESULT.md',
 'C7.4':'THEOREM_AUDITS/FAS-F2-C7.4-001_RESULT.md',
}
# The case IDs below are from original result reports, not guessed from nearby sections.
GROUPS={
 'G0':['D2.1','D2.2','D2.3','D2.4','P2.5'],
 'T3.3':['T3.3'], 'T3.6':['D3.5','T3.6'],
 'T4.5':['X4.1','X4.2','X4.3','X4.4','T4.5'],
 'T4.7':['P4.6','T4.7'],
 'S4.3':['C4.8','X4.9','L4.10','C4.11','P4.12','L4.13','C4.14'],
 'S5':['D5.1','P5.2','C5.3','P5.4','P5.5','P5.6','C5.7','P5.8','P5.9','X5.10','P5.11','P5.12','P5.13','P5.14'],
 'T6.5':['D6.1','D6.2','D6.4','T6.5'],
 'S6.6-6.7':['C6.6','C6.7'], 'T6.8':['T6.8'],
 'P6.11':['D6.10','P6.11'], 'C6.12':['C6.12'],
 'T6.14':['T6.14'], 'T6.16':['D6.15','T6.16'],
 'T6.17':['T6.17'], 'C6.18':['C6.18'],
 'T6.19':['T6.19'], 'T6.20':['T6.20'],
 'P6.22':['D6.21','P6.22'], 'T6.23':['T6.23'],
 'C6.24':['C6.24'], 'C6.25':['C6.25'], 'C6.26':['C6.26'],
 'T7.1':['T7.1'], 'C7.2':['C7.2'], 'T7.3':['T7.3'], 'C7.4':['C7.4'],
}
KIND={'Definition':'D','Theorem':'T','Proposition':'P','Corollary':'C',
      'Lemma':'L','Countermodel':'X','Remark':'R'}
# These are not marked as directly proved/reviewed just for being referenced.
CONTEXT={'P6.3':'T6.5','R3.4':'T3.3'}
PATTERN=re.compile(r'^\s*(Definition|Theorem|Proposition|Corollary|Lemma|Countermodel|Remark)\s+(\d+\.\d+)\s*\(([^)]*)\)\.')

def run(pdf):
    raw=Path(pdf).read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    if digest != SOURCE_SHA: raise ValueError('Immutable original PDF SHA256 mismatch: '+digest)
    grouped={}
    for case,labels in GROUPS.items():
        for label in labels:
            if label in grouped: raise ValueError('Duplicate source row evidence: '+label)
            grouped[label]=case
    found=[]
    doc=fitz.open(stream=raw,filetype='pdf')
    for page_no,page in enumerate(doc,1):
        for line in page.get_text('text',sort=True).splitlines():
            match=PATTERN.match(line)
            if not match: continue
            kind,num,title=match.groups()
            label=KIND[kind]+num
            case=grouped.get(label)
            context=CONTEXT.get(label)
            status=('definition_typed_review' if kind=='Definition' else 'explicit_mathematical_audit') if case else ('context_only' if context else 'no_explicit_audit_found')
            cited=case or context
            found.append({'label':label,'source_heading':kind+' '+num,
                          'title':title,'kind':kind,'pdf_page':page_no,
                          'printed_page':page_no,'status':status,
                          'case_id':cited,'evidence_path':ROOT+EVIDENCE[cited] if cited else None})
    labels=[x['label'] for x in found]
    if len(labels)!=69 or len(set(labels))!=69: raise AssertionError('Expected exactly 69 distinct source headings')
    if set(labels)-(set(grouped)|set(CONTEXT)) != {'R3.1','R3.2','R6.9','R6.13'} or (set(grouped)|set(CONTEXT))-set(labels):
        raise AssertionError('Unexpected unsupported or missing source-label mapping')
    if len(doc)!=33: raise AssertionError('Original page count changed')
    counts=dict(sorted(Counter(r['kind'] for r in found).items()))
    status_counts=dict(sorted(Counter(r['status'] for r in found).items()))
    assert counts=={'Corollary':14,'Countermodel':6,'Definition':12,'Lemma':2,'Proposition':16,'Remark':5,'Theorem':14}
    assert status_counts=={'context_only':2,'definition_typed_review':12,'explicit_mathematical_audit':51,'no_explicit_audit_found':4}
    direct_files=sorted({EVIDENCE[case] for case in GROUPS})
    return {'case':'FAS-F2-G4-CLAIM-INVENTORY-001', 'source_sha256':SOURCE_SHA,
      'source_pdf_pages':len(doc),'source_headings':len(found),'source_kind_counts':counts,
      'coverage_status_counts':status_counts,'direct_evidence_case_count':len(direct_files),
      'direct_result_paths':[ROOT+v for v in direct_files],
      'claim_rows':found, 'independent_external_validation':False,
      'full_F2_audit':'OPEN','coverage_not_a_proof_certificate':True,
      'scope_note':'Context citations or a nearby audited theorem do not establish a separately executed direct claim audit.'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pdf',required=True,help='Exact original 33-page Formation Axiom System PDF')
    p.add_argument('--output',default=str(Path(__file__).resolve().parents[1]/'results/f2_claim_inventory.json'))
    args=p.parse_args()
    obj=run(args.pdf)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(obj,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'source_headings':obj['source_headings'],'kinds':obj['source_kind_counts'],
      'statuses':obj['coverage_status_counts'],'direct_evidence_cases':obj['direct_evidence_case_count']},ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()
