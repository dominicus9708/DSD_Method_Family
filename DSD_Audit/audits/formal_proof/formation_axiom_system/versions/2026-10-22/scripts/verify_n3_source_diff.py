#!/usr/bin/env python3
r"""Reproduce F2 2026-10-22 source diff. Requires `pip install pymupdf`.
Run: python verify_n3_source_diff.py OLD_PDF NEW_PDF [OUTPUT_JSON]
"""
import collections
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path
import fitz
OLD='8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'
NEW='af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe'
KINDS={'Definition':12,'Theorem':14,'Proposition':16,'Corollary':14,'Lemma':2,'Countermodel':6,'Remark':5}
PAT=re.compile(r'^\s*(Definition|Theorem|Proposition|Corollary|Lemma|Countermodel|Remark)\s+(\d+\.\d+)\s*\(([^)]*)\)\.')

def pdf(path,digest,pages):
    data=Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest()==digest
    d=fitz.open(stream=data,filetype='pdf');assert len(d)==pages
    text='\n'.join(p.get_text('text') for p in d)
    lines=[v.strip() for v in text.splitlines() if v.strip() and not re.fullmatch(r'\s*\d{1,2}\s*',v)]
    heads=[]
    for p in d:
        for ln in p.get_text('text',sort=True).splitlines():
            m=PAT.match(ln)
            if m:heads.append(m.groups())
    assert len(heads)==69 and dict(collections.Counter(x[0] for x in heads))==KINDS
    return lines,heads

def run(old,new):
    a,A=pdf(old,OLD,33);b,B=pdf(new,NEW,34)
    assert [(x[0],x[1]) for x in A]==[(x[0],x[1]) for x in B]
    changed=[(x,y) for x,y in zip(A,B) if x[2]!=y[2]]
    assert len(changed)==1 and changed[0][0][1]=='5.13'
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    ops=sm.get_opcodes()
    pairs=[(tag,' '.join(a[i:j]),' '.join(b[k:l]),(i,j,k,l)) for tag,i,j,k,l in ops if tag!='equal']
    scope=['date','Theorem 4.7 preamble','Theorem 4.7 proof','Proposition 5.13','Section 7.3 D2','Section 8']
    assert len(pairs)==6
    tests=[('2026.08.06','2026.10.22'),('residual primitive constraints','equivalent residualized'),('other primitive axioms','other five'),('Zero-extension of the term map','Conditional channel-membership'),('horizontal relation','row–column convention'),('strictly weaker','no unconditional implication ordering')]
    for (tag,prior,later,coords),(lo,hi) in zip(pairs,tests):
        assert lo in prior and hi in later,(coords,lo,hi)
    same=sum(j-i for tag,i,j,k,l in ops if tag=='equal')
    assert same==1820
    return {'case':'FAS-F2-20261022-N3-MANUSCRIPT-DEPENDENCY-REGRESSION-001',
      'source_old_sha256':OLD,'source_new_sha256':NEW,'numbered_headings':69,
      'unchanged_heading_ids':67,'changed_heading_id':'Proposition 5.13',
      'unchanged_normalized_text_lines':same,'source_changes':scope,
      'substantive_changed_regions':5,'cover_date_change':True,
      'outside_named_regions_text_identical':True,
      'mathematical_proofs_reestablished_by_text_diff':False,
      'full_F2_paper_FPA':'OPEN','external_independent_validation':'not_established'}

def main():
    assert len(sys.argv) in (3,4),'usage: script OLD_PDF NEW_PDF [OUTPUT_JSON]'
    out=run(sys.argv[1],sys.argv[2]);p=Path(sys.argv[3]) if len(sys.argv)==4 else Path(__file__).resolve().parents[1]/'results/n3_source_diff.json'
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('N3_SOURCE_DIFF_PASS; 69 headings; 67 unchanged; 5 edited regions; 1820 matching lines')
if __name__=='__main__':main()
