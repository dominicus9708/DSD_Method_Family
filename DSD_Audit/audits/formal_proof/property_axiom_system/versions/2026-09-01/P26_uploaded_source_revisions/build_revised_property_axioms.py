#!/usr/bin/env python3
"""Preserve originals; deterministic section-granular EN/KR property paper repairs.
Run (Windows, from same folder as the two uploaded EN/KR source TeX files):
 python build_revised_property_axioms.py --en "DSD_Property_Axiom_System_EN(3).tex" --kr "DSD_Property_Axiom_System_KR(3).tex" --out "P26_revised"
Author: Kwon Dominicus. This is NOT a universal ZFC proof.
"""
import argparse, json, re, hashlib
from pathlib import Path


def replace_once(s, label, before, after, manifest):
    count = s.count(before)
    if count != 1:
        raise RuntimeError(f'{label}: expected one source occurrence, got {count}')
    manifest.append(label)
    return s.replace(before, after, 1)


def main(en_path: Path, kr_path: Path, output: Path):
    output.mkdir(parents=True, exist_ok=True)
    data = {}
    edits = {}
    for lang, source in [('EN', en_path), ('KR', kr_path)]:
        original = source.read_text('utf-8')
        s = original
        labels = []
        R = lambda label, old, new: replace_once(s, label, old, new, labels)
        def change(label, before, after):
            nonlocal s
            s = replace_once(s, label, before, after, labels)
        if lang == 'EN':
            change('ABSTRACT_STRICT',
                'strict Stage-VI-fixed, signature-fixed property isomorphisms are exactly the bijective embeddings;',
                'strict Stage-VI-fixed, signature-fixed property isomorphisms are exactly the bijective embeddings with matching auxiliary-sort availability and property-kind declarations;')
            change('TH43_SCOPE',
                'Relative to the shared typed background and Definitional Closure Clause~C1, Primitive Axioms~I and II are mutually non-derivable.',
                'Relative to the shared typed-premodel background, Primitive Axioms~I and II are mutually non-derivable.')
            change('TH43_PROOF',
                'Both are well typed under the same one-input signature.\n\\end{proof}',
                'Both are well typed under the same one-input signature.\nNeither countermodel is a primitive property core because each violates one of the axioms.\nDefinitional Closure Clause~C1 applies conditionally to admitted primitive cores satisfying both axioms and is not a premise imposed on these typed counterpremodels.\n\\end{proof}')
            change('DEF61_F3',
                r'\item For every \(\varpi\in\Pi_A\), the product map induced by its profile,',
                r'\item For every \(\varpi\in\Pi_A\) whose profile is available in \(A\), the product map induced by its profile,')
            change('DEF61_F4',
                r'\item For every \(d\in\delta_L(\varpi)\),' + '\n' + r'\[' + '\n' + r'\phi_{\varpi}',
                r'\item For every such \(\varpi\) and every \(d\in\delta_L(\varpi)\),' + '\n' + r'\[' + '\n' + r'\phi_{\varpi}')
            change('DEF61_F5',
                r'\item If \(x\in D_{A,\varpi}\), then \(\phi_{\varpi}(x)\in D_{B,\varpi}\) and',
                r'\item For every such \(\varpi\), if \(x\in D_{A,\varpi}\), then \(\phi_{\varpi}(x)\in D_{B,\varpi}\) and')
            change('DEF61_GUARD_EXPLANATION',
                '\\end{enumerate}\n\\end{definition}\n\nForward maps preserve successful property data',
                '\\end{enumerate}\nThe qualification ``such \\(\\varpi\\)\'\' in (F4)--(F5) refers to the source-declared, profile-available kinds in (F3).\nCondition (F1) ensures each such source profile is also available in the target.\nNo product-map condition is imposed for a declared kind with an unavailable source profile.\n\\end{definition}\n\nForward maps preserve successful property data')
            change('PROP62_PROOF',
                'Identity maps satisfy (F1)--(F5) immediately.\nFor composition, availability and declaration inclusions compose, product maps compose coordinatewise, and images of applicability and prerequisite-satisfaction sets remain included by transitivity of set inclusion.\nValue preservation follows by applying (F5) first to the inner and then to the outer map.',
                'Identity maps satisfy (F1)--(F5) for each source-declared, profile-available kind; unavailable source profiles impose no product-map condition.\nFor composition, availability and declaration inclusions compose.\nBy (F1)--(F2), a kind declared with an available profile in the first source remains declared with an available profile in the intermediate target, so its induced product maps compose coordinatewise.\nApplicability and prerequisite-satisfaction images remain included by transitivity of set inclusion.\nValue preservation follows by applying (F5) first to the inner and then to the outer map.')
            change('DEF63_GUARD',
                r'when every auxiliary carrier map is injective and, for every source input \(x\in X_{A,\varpi}\),',
                r'when every auxiliary carrier map is injective and, for every \(\varpi\in\Pi_A\) whose profile is available in \(A\) and every source input \(x\in X_{A,\varpi}\),')
            change('TH68_CONDITION',
                'Equivalently, strict property isomorphisms are exactly the bijective property embeddings.',
                'Equivalently, they are exactly the property embeddings satisfying (S1)--(S3): bijective available auxiliary carrier maps, equal available auxiliary-sort sets, and equal declared property-kind sets; (S4) follows under these hypotheses.')
            change('TH68_PROOF',
                'The identity embedding is bijective, giving reflexivity.\nIf \\(\\Phi:A\\to B\\) is a strict isomorphism, its inverse carrier bijections preserve and reflect every primitive relation because the embedding conditions are biconditional; value preservation reverses by substitution, giving symmetry.\nThe composite of two bijective embeddings is a bijective embedding, giving transitivity.',
                'The identity embedding has bijective components and matching auxiliary-sort availability and declaration sets, hence is strict.\nSuppose an embedding \\(\\Phi:A\\to B\\) satisfies (S1)--(S3).\nBy (S1)--(S2), the auxiliary carrier bijections have inverses over precisely the same available sorts, while inherited carrier maps are identities.\nBy (S3), the declared kinds coincide, and profile availability agrees because the supplied sorts agree.\nFor every common declared kind with available profile, the induced product map is bijective.\nThe embedding biconditionals for applicability, each prerequisite and assignment-domain membership reverse under the inverse product map; value preservation (F5) reverses on the reflected assignment domains by substitution.\nFor unavailable profiles neither direction requires product-map conditions.\nThus the inverse family is an embedding, proving (S4).\nThe identity, inverse and composition of strict isomorphisms preserve these conditions, proving reflexivity, symmetry and transitivity.')
            change('TH111_ITEM7',
                'Strict Stage-VI-fixed, signature-fixed property isomorphism is exactly bijective property embedding and is an equivalence relation.',
                'Strict Stage-VI-fixed, signature-fixed property isomorphism is exactly property embedding satisfying the bijective-carrier, equal-availability and equal-declaration requirements (S1)--(S3); the inverse condition (S4) follows, and strict equivalence is an equivalence relation.')
            change('AGGREGATION_SCOPE',
                'Aggregate equality is consequently weaker than strict property equivalence unless a reconstruction theorem is supplied.',
                'Equality of separately chosen aggregate outputs alone does not generally reconstruct strict property equivalence; a stronger conclusion requires source-aware reconstruction or injectivity hypotheses.\nNo unconditional comparison in the converse direction is asserted for arbitrarily and independently chosen external bridges.')
        else:
            change('ABSTRACT_STRICT',
                '단계 VI 고정·시그니처 고정의 엄격한 속성 동형사상은 정확히 전단사 매장이며,',
                '단계 VI 고정·시그니처 고정의 엄격한 속성 동형사상은 사용 가능한 보조 종류 집합과 선언된 속성 종류 집합이 일치하는 전단사 매장이며,')
            change('TH43_SCOPE',
                '공유 유형화 배경과 정의적 폐쇄 조항 C1에 상대적으로 원시 공리 I과 II는 서로 도출되지 않는다.',
                '공유 유형화 예비모형 배경에서 원시 공리 I과 II는 서로 도출되지 않는다.')
            change('TH43_PROOF',
                '둘 다 동일한 한 입력 시그니처 아래에서 올바르게 유형화되어 있다.\n\\end{proof}',
                '둘 다 동일한 한 입력 시그니처 아래에서 올바르게 유형화되어 있다.\n각 반모형은 두 공리 중 하나를 위반하므로 원시 속성 핵심이 아니다.\n정의적 폐쇄 조항 C1은 두 공리를 모두 충족하는 허용된 원시 핵심에 조건부로 적용되며, 여기의 유형화 반예비모형에 부과한 전제가 아니다.\n\\end{proof}')
            change('DEF61_F3',
                r'\item 모든 \(\varpi\in\Pi_A\)에 대하여 그 프로파일이 유도하는 곱사상',
                r'\item \(A\)에서 선언되고 프로파일을 이용할 수 있는 모든 \(\varpi\in\Pi_A\)에 대하여 그 프로파일이 유도하는 곱사상')
            change('DEF61_F4',
                r'\item 모든 \(d\in\delta_L(\varpi)\)에 대하여' + '\n' + r'\[' + '\n' + r'\phi_{\varpi}',
                r'\item 그러한 모든 \(\varpi\)와 각각의 \(d\in\delta_L(\varpi)\)에 대하여' + '\n' + r'\[' + '\n' + r'\phi_{\varpi}')
            change('DEF61_F5',
                r'\item \(x\in D_{A,\varpi}\)이면 \(\phi_{\varpi}(x)\in D_{B,\varpi}\)이고',
                r'\item 그러한 모든 \(\varpi\)에 대하여 \(x\in D_{A,\varpi}\)이면 \(\phi_{\varpi}(x)\in D_{B,\varpi}\)이고')
            change('DEF61_GUARD_EXPLANATION',
                '\\end{enumerate}\n\\end{definition}\n\n순방향 사상은 성공적으로 정의된 속성 자료',
                '\\end{enumerate}\n(F4)--(F5)에서 ``그러한 \\(\\varpi\\)\'\'는 (F3)의 출발 모형에서 선언되고 프로파일을 이용할 수 있는 속성 종류를 가리킨다.\n(F1)은 그러한 출발 프로파일이 목표 모형에서도 이용 가능함을 보장한다.\n출발 프로파일을 이용할 수 없는 선언 종류에는 곱사상 조건을 부과하지 않는다.\n\\end{definition}\n\n순방향 사상은 성공적으로 정의된 속성 자료')
            change('PROP62_PROOF',
                '항등사상은 (F1)--(F5)를 즉시 만족한다.\n합성의 경우 가용성과 선언의 포함관계는 합성되고, 곱사상은 좌표별로 합성되며, 적용 가능 집합과 선행조건 충족 집합의 상은 집합 포함의 추이성에 의해 여전히 포함된다.\n값 보존은 안쪽 사상에 먼저 (F5)를 적용하고 이어 바깥 사상에 적용하면 얻어진다.',
                '항등사상은 출발 모형에서 선언되고 프로파일을 이용할 수 있는 속성 종류에 대해 (F1)--(F5)를 만족한다.\n이용할 수 없는 출발 프로파일에는 곱사상 조건이 없다.\n합성의 경우 가용성과 선언의 포함관계는 합성된다.\n(F1)--(F2)에 따라 처음 출발 모형에서 선언되고 프로파일을 이용할 수 있는 종류는 중간 목표에서도 선언되고 이용 가능하므로 곱사상은 좌표별로 합성된다.\n적용 가능 집합과 선행조건 충족 집합의 상은 집합 포함의 추이성에 의해 여전히 포함된다.\n값 보존은 안쪽 사상에 먼저 (F5)를 적용하고 이어 바깥 사상에 적용하면 얻어진다.')
            change('DEF63_GUARD',
                r'모든 보조 운반체 사상에서 단사이고, 모든 출발 입력 \(x\in X_{A,\varpi}\)에 대하여',
                r'모든 보조 운반체 사상에서 단사이고, \(A\)에서 선언되고 프로파일을 이용할 수 있는 모든 \(\varpi\in\Pi_A\)의 각 출발 입력 \(x\in X_{A,\varpi}\)에 대하여')
            change('TH68_CONDITION',
                '동등하게, 엄격한 속성 동형사상은 정확히 전단사 속성 매장이다.',
                '동등하게, 엄격한 속성 동형사상은 (S1)--(S3), 즉 이용 가능한 보조 운반체 사상의 전단사성, 보조 종류 가용성 집합의 일치 및 선언된 속성 종류 집합의 일치를 만족하는 속성 매장과 정확히 일치하며, 이때 (S4)가 따라온다.')
            change('TH68_PROOF',
                '항등 매장은 전단사이므로 반사성이 성립한다.\n\\(\\Phi:A\\to B\\)가 엄격한 동형사상이면 매장 조건이 쌍조건이므로 역운반체 전단사도 모든 원시 관계를 보존하고 반영한다. 값 보존 등식도 대입으로 역방향에 성립하므로 대칭성이 얻어진다.\n두 전단사 매장의 합성은 전단사 매장이므로 추이성이 성립한다.',
                '항등 매장은 성분별 전단사이고 보조 종류 가용성 및 선언 집합이 일치하므로 엄격하다.\n(S1)--(S3)을 만족하는 매장 \\(\\Phi:A\\to B\\)를 취하자.\n(S1)--(S2)에 따라 이용 가능한 보조 운반체의 전단사에는 역함수가 있고 양쪽의 이용 가능 종류 집합이 같다. 상속 운반체 사상은 항등사상이다.\n(S3)에 의해 선언 종류 집합이 일치하고, 가용 종류 집합이 같으므로 프로파일 이용 가능성도 일치한다.\n따라서 양쪽에서 선언되고 프로파일을 이용할 수 있는 각 종류의 유도 곱사상은 전단사이다.\n적용 가능성, 각 선행조건 충족 집합 및 할당 정의역에 대한 매장의 쌍조건은 역곱사상에 대입해도 성립하고, (F5)의 값 보존 등식도 반영된 할당 정의역에서 대입으로 역방향 보존된다.\n프로파일을 이용할 수 없는 종류에 대해서는 어느 방향에서도 곱사상 조건을 요구하지 않는다.\n그러므로 역사상족 역시 매장이 되어 (S4)가 성립한다.\n항등·역·합성은 이 조건들을 보존하므로 엄격한 속성 동형은 반사적·대칭적·추이적이다.')
            change('TH111_ITEM7',
                '엄격한 단계 VI 고정·시그니처 고정 속성 동형사상은 정확히 전단사 속성 매장이며 동치관계를 이룬다.',
                '엄격한 단계 VI 고정·시그니처 고정 속성 동형사상은 전단사 운반체·가용성 집합 일치·선언 집합 일치의 (S1)--(S3)을 만족하는 속성 매장과 정확히 일치하며 역매장 조건 (S4)가 따라오고 동치관계를 이룬다.')
            change('AGGREGATION_SCOPE',
                '따라서 별도의 복원 정리가 주어지지 않는 한 집계 동일성은 엄격한 속성 동치보다 약하다.',
                '따라서 별도로 선택한 집계 출력의 동일성만으로는 일반적으로 엄격한 속성 동치를 복원할 수 없으며, 더 강한 결론에는 원천 구조를 고려한 복원 또는 단사성 가정이 필요하다.\n서로 독립적으로 임의 선택한 외부 다리에 대해서는 반대 방향의 무조건적 함의를 주장하지 않는다.')
        # Existing % ---------- Section comments remain intact, add explicit updated-section separators.
        for num in [4, 6, 9, 11]:
            marker = re.search(r'(?m)^% -+Section '+str(num)+r'\.', s)
            if marker is None:
                raise RuntimeError(f'{lang}: missing section {num} delimiter')
            scoped = re.search(r'(?m)^\\section\{[^\n]+\}\n\\label\{[^\n]+\}\n', s[marker.start():])
            if scoped is None:
                raise RuntimeError(f'{lang}: cannot locate section {num} header and label')
            insert_at = marker.start() + scoped.end()
            s = s[:insert_at] + f'% ----- P26 audited revision (Section {num}) -----\n' + s[insert_at:]
        # Section counts, mathematical environment identity and exact labels invariant.
        envs = r'\\begin\{(?:theorem|definition|proposition|corollary|countermodel|construction|remark)\}'
        assert len(re.findall(envs, original)) == len(re.findall(envs, s)) == 56
        assert len(re.findall(r'\\section\{', s)) == 16
        assert len(re.findall(r'\\begin\{axiom\}', s)) == 2
        assert len(re.findall(r'\\begin\{closureclause\}', s)) == 1
        assert re.findall(r'\\label\{([^}]+)\}', original) == re.findall(r'\\label\{([^}]+)\}', s)
        assert '\\author{Kwon Dominicus' in s
        assert s.endswith('\\end{document}\n') or s.endswith('\\end{document}')
        fname = f'DSD_Property_Axiom_System_{lang}_P26_REVISED.tex'
        (output/fname).write_text(s,'utf-8')
        edits[lang] = labels
        data[lang] = {'input':str(source),'original_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                      'revised_file':fname,'revised_sha256':hashlib.sha256(s.encode()).hexdigest(),
                      'original_numbered_items':56,'revised_numbered_items':56,
                      'changed_sections':[4,6,9,11], 'metadata_and_labels_preserved':True}
    assert edits['EN'] == edits['KR'], (edits['EN'],edits['KR'])
    result={'author':'Kwon Dominicus','status':'revised EN/KR candidate; not published / entire FPA open',
            'matching_edit_operation_ids':edits['EN'], 'sources':data,'original_files_modified':False}
    (output/'P26_EDIT_MANIFEST.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n','utf-8')
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--en',type=Path,required=True)
    p.add_argument('--kr',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    main(a.en,a.kr,a.out)
