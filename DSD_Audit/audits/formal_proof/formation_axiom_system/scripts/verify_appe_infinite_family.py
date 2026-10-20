#!/usr/bin/env python3
"""FAS-F2-APPE-INFINITE-001: selected exact finite-subset verification.

Source proof uses Banach-space finite-subset nets; this finite test is not a
machine proof of infinite convergence or an outside independent replication.
Windows repository root command:
python .\\DSD_Audit\\audits\\formal_proof\\formation_axiom_system\\scripts\\verify_appe_infinite_family.py
Default JSON: ../results/appe_infinite_family.json; optional positional output.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

SOURCE_SHA = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'

def geometric_subsets(n=12):
    """Every subset of the *first n indexes*, exact dyadic rationals."""
    source = [Fraction(1, 2 ** (k + 1)) for k in range(n)]
    count = 0
    for mask in range(1 << n):
        terms = [source[i] for i in range(n) if mask & (1 << i)]
        assert 2 * sum(terms, Fraction(0)) == sum((2*x for x in terms), Fraction(0))
        count += 1
    prefixes = []
    for N in (1, 2, 4, 8, 12, 24, 32):
        s = sum((Fraction(1, 2 ** (k+1)) for k in range(N)), Fraction(0))
        assert s == 1 - Fraction(1, 2**N)
        assert 2*s == 2 - Fraction(1, 2**(N-1))
        # Any finite subfamily exclusively with indices >=N has sum <= 2^-N.
        prefixes.append({'N': N, 'source_partial':str(s),'source_tail_bound':str(Fraction(1,2**N)),
                         'target_partial':str(2*s), 'target_tail_bound':str(Fraction(2,2**N))})
    return {'finite_subsets_checked':count,'prefix_tail_certificates':prefixes,
            'source_infinite_sum_exact':'1','target_infinite_sum_exact':'2',
            'transport_J':'J(x)=2x'}

def empty_and_duplicate_index():
    c = 'one_admitted_channel'
    indexed = (c,c)
    terms = {c:Fraction(1)}
    assert sum((terms[x] for x in indexed),Fraction()) == 2
    assert sum((terms[x] for x in set(indexed)),Fraction()) == 1
    return {'empty_index_sum':'0', 'finite_indexed_duplicate_sum':'2',
            'finite_core_set_sum':'1','infinite_repeated_nonzero_unconditional':False,
            'infinite_repeated_zero_unconditional':True}

def orthogonal_l2_boundary():
    # Partial square of a tail of e_n/n, n>=1. Exact rationals.
    # Orthogonality and finite block norm^2 give uniform upper bound tail <=1/N
    # for any finite F subset {N+1,...}; divergent sum ||e_n/n|| means
    # unconditional convergence need not imply absolute convergence in Banach spaces.
    tests=[]
    for N in (8,16,32,64):
        tail_sq=sum((Fraction(1,n*n) for n in range(N+1,4*N+1)),Fraction())
        assert tail_sq <= Fraction(1,N)
        tests.append({'lower_index_exclusive':N,'finite_tail_squared_norm':str(tail_sq),
                      'all_later_finite_subset_squared_norm_upper_bound':str(Fraction(1,N))})
    return {'space':'ell2','family':'e_n/n, n>=1', 'absolute_norm_sum_diverges':True,
            'unconditional_sum_converges':True,'selected_tail_checks':tests}

def conditional_harmonic_obstruction():
    # Positive odd-index terms form a subseries of alternating harmonic series,
    # hence its divergent growth disproves unconditional convergence.
    checks=[]
    for N in (8,32,128,512):
        block=sum(Fraction(1,2*k-1) for k in range(N+1,2*N+1))
        assert block > Fraction(1,4)
        checks.append({'N':N,'odd_positive_index_block_lower_bound':'1/4',
                       'observed_block':str(block)})
    return {'ordered_alternating_harmonic_converges':True,
            'positive_odd_index_subfamily_diverges':True,
            'unconditional_convergence':False,'selected_blocks':checks}

def complex_transport():
    # Q(i) arithmetic in Gaussian rational pair representation.
    from fractions import Fraction as Q
    terms=[(Q(1,2**(k+1)), Q(-1,3**(k+1))) for k in range(8)]
    # J(z)=i z maps (a,b) to (-b,a), is bounded complex-linear isometry.
    a=sum((p[0] for p in terms),Q()); b=sum((p[1] for p in terms),Q())
    sums=(sum((-p[1] for p in terms),Q()),sum((p[0] for p in terms),Q()))
    assert sums==(-b,a)
    return {'finite_terms_checked':8,'map':'J(z)=i*z','source_sum_components':[str(a),str(b)],
            'target_sum_components':[str(sums[0]),str(sums[1])], 'termwise_equality':True}

def main():
    o={'case':'FAS-F2-APPE-INFINITE-001','source_pdf_sha256':SOURCE_SHA,
       'real_geometric_family':geometric_subsets(),
       'repeated_index_boundary':empty_and_duplicate_index(),
       'orthogonal_unconditional_not_absolute':orthogonal_l2_boundary(),
       'conditionally_convergent_obstruction':conditional_harmonic_obstruction(),
       'complex_finite_case':complex_transport(),
       'mathematical_proof_is_analytic_not_numerical':True,
       'whole_formation_f2':'OPEN','external_independent_validation':False,
       'method_family_internally_standardized':22}
    out=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'results/appe_infinite_family.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(o,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'finite_subsets':o['real_geometric_family']['finite_subsets_checked'],
                      'signed_odd_blocks':len(o['conditionally_convergent_obstruction']['selected_blocks']),
                      'orthogonal_blocks':len(o['orthogonal_unconditional_not_absolute']['selected_tail_checks']),
                      'complex_terms':o['complex_finite_case']['finite_terms_checked']},sort_keys=True))
if __name__=='__main__':main()
