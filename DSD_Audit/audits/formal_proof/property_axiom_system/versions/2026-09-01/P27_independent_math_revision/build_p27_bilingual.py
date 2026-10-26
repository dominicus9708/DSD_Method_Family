#!/usr/bin/env python3
"""Deterministic P27 manuscript repairs. Runs from any working directory.

Default inputs: adjacent original P26 EN/KR TeX; output: --out directory.
NO published files or archived P26 files are changed.
"""
from pathlib import Path
import argparse, hashlib, json, re

FILES={'EN':'DSD_Property_Axiom_System_EN_P26_REVISED.tex','KR':'DSD_Property_Axiom_System_KR_P26_REVISED.tex'}

def sha(s: bytes): return hashlib.sha256(s).hexdigest()

def replace_exact(s, old, new, tag):
    assert s.count(old)==1, f'{tag}: expected one exact match, found {s.count(old)}'
    return s.replace(old,new,1)

def build(lang, source):
    s=source
    if lang=='EN':
        old=r'''A forward property map \(\Phi:A\to B\) is a \emph{property embedding} when every auxiliary carrier map is injective and, for every \(\varpi\in\Pi_A\) whose profile is available in \(A\) and every source input \(x\in X_{A,\varpi}\),
\[
\begin{aligned}
x\in\Ap_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Ap_{B,\varpi},\\
x\in\Sat_{A,\varpi,d}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Sat_{B,\varpi,d},\\
x\in D_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in D_{B,\varpi},
\end{aligned}
\]
and the value-preservation equation of (F5) holds on the assignment domain.'''
        new=r'''A forward property map \(\Phi:A\to B\) is a \emph{property embedding} when every auxiliary carrier map is injective and, for every \(\varpi\in\Pi_A\) whose profile is available in \(A\) and every source input \(x\in X_{A,\varpi}\), the following hold:
\[
\begin{aligned}
\text{(E1)}\quad x\in\Ap_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Ap_{B,\varpi},\\
\text{(E2)}\quad x\in\Sat_{A,\varpi,d}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Sat_{B,\varpi,d}
\quad\text{for every }d\in\delta_L(\varpi),\\
\text{(E3)}\quad x\in D_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in D_{B,\varpi}.
\end{aligned}
\]
The value-preservation equation of (F5) also holds on the source assignment domain.
In particular, if \(\delta_L(\varpi)=\varnothing\), (E2) is vacuous but (E1) and (E3) remain mandatory.'''
        s=replace_exact(s,old,new,'EN-Def6.3')
        old=r'''For a finite zero-bearing property model, define the summary
\[
\mathfrak S(A):=
\left(
|\Pi_A|,
\left\{
\bigl(|D_{A,\varpi}|,N^0_{A,\varpi},N^{\neq0}_{A,\varpi}\bigr)
:\varpi\in\Pi_A
\right\}
\right),
\]
where \(N^0_{A,\varpi}\) and \(N^{\neq0}_{A,\varpi}\) are the numbers of defined zero and defined nonzero inputs for \(\varpi\).
The property labels remain associated with their triples; only cross-property correlations among input locations are forgotten.'''
        new=r'''For a property-finite full property model \(A\) whose declared kinds all have available profiles and designated zero elements, that is,
\(\Pi_A\subseteq\PiZero\) and every \(\varpi\in\Pi_A\) has an available profile, define the label-retaining summary
\[
\mathfrak S(A):=
\left(
|\Pi_A|,
\left\{
\bigl(\varpi,|D_{A,\varpi}|,N^0_{A,\varpi},N^{\neq0}_{A,\varpi}\bigr)
:\varpi\in\Pi_A
\right\}
\right),
\]
where \(N^0_{A,\varpi}\) and \(N^{\neq0}_{A,\varpi}\) count the inputs assigned zero and nonzero values, respectively, for \(\varpi\).
The explicit kind label in each tuple retains the association between each property and its counts, while cross-property correlations among input locations are forgotten.
For kinds without a designated zero or without an available profile, this particular summary is not defined without an additional convention.'''
        s=replace_exact(s,old,new,'EN-Def9.1')
    else:
        old=r'''순방향 속성 사상 \(\Phi:A\to B\)가 모든 보조 운반체 사상에서 단사이고, \(A\)에서 선언되고 프로파일을 이용할 수 있는 모든 \(\varpi\in\Pi_A\)의 각 출발 입력 \(x\in X_{A,\varpi}\)에 대하여
\[
\begin{aligned}
x\in\Ap_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Ap_{B,\varpi},\\
x\in\Sat_{A,\varpi,d}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Sat_{B,\varpi,d},\\
x\in D_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in D_{B,\varpi},
\end{aligned}
\]
를 만족하며 할당 정의역에서 (F5)의 값 보존 등식이 성립하면 \(\Phi\)를 \emph{속성 매장}이라 한다.'''
        new=r'''순방향 속성 사상 \(\Phi:A\to B\)의 모든 보조 운반체 사상이 단사이고, \(A\)에서 선언되며 프로파일이 이용 가능한 모든 \(\varpi\in\Pi_A\)와 각 출발 입력 \(x\in X_{A,\varpi}\)에 대해 다음을 모두 만족하면 \(\Phi\)를 \emph{속성 매장}이라 한다.
\[
\begin{aligned}
\text{(E1)}\quad x\in\Ap_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Ap_{B,\varpi},\\
\text{(E2)}\quad x\in\Sat_{A,\varpi,d}
&\Longleftrightarrow
\phi_{\varpi}(x)\in\Sat_{B,\varpi,d}
\quad\text{모든 }d\in\delta_L(\varpi)\text{에 대해},\\
\text{(E3)}\quad x\in D_{A,\varpi}
&\Longleftrightarrow
\phi_{\varpi}(x)\in D_{B,\varpi}.
\end{aligned}
\]
또한 출발 할당 정의역에서 (F5)의 값 보존 등식을 만족한다.
특히 \(\delta_L(\varpi)=\varnothing\)이면 (E2)는 공허하게 참이지만 (E1)과 (E3)은 여전히 반드시 성립해야 한다.'''
        s=replace_exact(s,old,new,'KR-Def6.3')
        old=r'''유한한 0 보유 속성 모형에 대하여 요약
\[
\mathfrak S(A):=
\left(
|\Pi_A|,
\left\{
\bigl(|D_{A,\varpi}|,N^0_{A,\varpi},N^{\neq0}_{A,\varpi}\bigr)
:\varpi\in\Pi_A
\right\}
\right)
\]
을 정의한다.
여기서 \(N^0_{A,\varpi}\)와 \(N^{\neq0}_{A,\varpi}\)는 각각 \(\varpi\)에서 정의된 0 입력과 정의된 비영 입력의 수이다.
속성 표지는 각 삼중항과 연결된 채 유지하며, 입력 위치 사이의 속성 간 상관관계만 잊는다.'''
        new=r'''선언된 속성 종류가 모두 이용 가능한 프로파일과 지정된 영(0)을 갖는 속성 유한 완전 모형 \(A\), 즉
\(\Pi_A\subseteq\PiZero\)이고 모든 \(\varpi\in\Pi_A\)의 프로파일이 이용 가능한 경우, 속성 표지를 보존하는 요약
\[
\mathfrak S(A):=
\left(
|\Pi_A|,
\left\{
\bigl(\varpi,|D_{A,\varpi}|,N^0_{A,\varpi},N^{\neq0}_{A,\varpi}\bigr)
:\varpi\in\Pi_A
\right\}
\right)
\]
을 정의한다.
여기서 \(N^0_{A,\varpi}\)와 \(N^{\neq0}_{A,\varpi}\)는 각각 \(\varpi\)에서 값이 영과 비영으로 할당된 입력 수이다.
각 튜플의 속성 표지는 해당 속성과 집계값의 연결을 보존하지만, 입력 위치 사이의 속성 간 상관관계는 잊는다.
지정된 영이 없거나 프로파일이 이용 불가능한 속성에 대해서는 추가 규약 없이 이 요약을 정의하지 않는다.'''
        s=replace_exact(s,old,new,'KR-Def9.1')
    assert len(re.findall(r'\\section\{',s))==16
    assert len(re.findall(r'\\begin\{(?:definition|theorem|proposition|corollary|countermodel|construction|remark)\}',s))==56
    assert s.count(r'\label{')==36
    assert s.count(r'\begin{axiom}')==2 and s.count(r'\begin{closureclause}')==1
    assert r'\author{Kwon Dominicus' in s
    assert s.count(r'\text{(E1)}')==1 and s.count(r'\text{(E3)}')==1
    return s

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source-dir',type=Path,default=Path(__file__).resolve().parent.parent/'DSD_Property_P26_Revision')
    ap.add_argument('--out',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    report={}
    for lang,n in FILES.items():
        orig=(args.source_dir/n).read_bytes()
        src=orig.decode('utf-8')
        result=build(lang,src)
        newname=f'DSD_Property_Axiom_System_{lang}_P27_REVISED.tex'
        out=(args.out/newname)
        out.write_text(result,encoding='utf-8')
        report[lang]={'original_sha256':sha(orig),'revised_sha256':sha(out.read_bytes()),'total_sections':13,'appendices':3,'numbered_items':56,'labels':36}
        # Section-based isolation: only §6 and §9 must change.
        o=list(re.finditer(r'\\section\{',src)); a=list(re.finditer(r'\\section\{',result))
        assert len(o)==len(a)==16
        delta=[i+1 for i in range(16) if src[o[i].start():o[i+1].start() if i+1<16 else len(src)]!=result[a[i].start():a[i+1].start() if i+1<16 else len(result)]]
        assert delta==[6,9],delta
        report[lang]['changed_sections']=delta
        assert src[:o[0].start()]==result[:a[0].start()]
    (args.out/'P27_SOURCE_DIFFERENTIAL_AUDIT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()