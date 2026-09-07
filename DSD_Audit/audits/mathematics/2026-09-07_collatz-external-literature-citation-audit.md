# DSD Audit — Collatz external-literature absorption and citation policy

STATUS: COMPLETED

```text
AUDIT_ID: DSD-AUDIT-20260907-MATH-002
TITLE: Collatz external-literature absorption and citation policy audit
DOMAIN: Mathematics / number theory / proof-audit methodology
DATE: 2026-09-07
AUDITOR_OR_AGENT: ChatGPT with repository-level DSD audit workflow
RELATED_SOURCE_OR_CASE: dominicus9708/Math-verification collatz external-literature corpus
METHODOLOGY_VERSION: DSD General Audit Framework current on 2026-09-07
```

## 1. Audit question

Can the external Collatz literature already used by the project be partitioned into reproducible citation classes so that valid theorems are retained, conditional results remain conditional, and failed proof hinges are preserved as anti-pattern citations rather than silently deleted?

Secondary question: were any previously imported sources still marked safe despite an unfinished reproduction audit or stale paper version?

## 2. Scope

Included:

- established external theorems actually cited by the Collatz repository;
- external conjectures used as conditional proof gates;
- recent claimed complete proofs that received explicit DSD hinge audits;
- the Cerdà 2-adic survival-set series where an earlier reproduction item was pending;
- current Nwankpa v9 and Niu 2026 updates.

Excluded:

- every Collatz manuscript not yet used by the repository;
- blanket truth/falsity judgments on portions of a paper outside the audited hinge;
- a claim that completion of the literature audit constitutes a proof of Collatz.

External standard: ordinary mathematical proof validity, source-version fidelity, quantifier preservation, exact domain/codomain preservation, and reproducible counterexample or theorem reconstruction.

## 3. Evidence status

### ESTABLISHED_WITHIN_SCOPE

1. The repository had a 2026-09-06 master A/B/C/D absorption matrix.
2. Several failed claimed-proof mechanisms have exact counterexamples or formal hinge defects preserved in separate commits.
3. Cerdà's finite valuation-cylinder / exact half-decay theorem can be independently reconstructed.
4. Nwankpa v9 still uses an invalid `SCC has exit -> every trajectory exits` liveness bridge; its own current text says the terminal edge at `S11` is representative-specific (`x=8`).
5. Niu 2026 explicitly separates three unconditional theorems from a numerical/conjectural observation and does not claim Collatz/CST closure.

### UNDETERMINED_OR_INSUFFICIENT

- Any theorem in an external paper not covered by the recorded claim-unit audit.
- The mathematical truth of open conjectures retained under class B.

### OUT_OF_SCOPE

- Exhaustive review of all Collatz literature worldwide.

## 4. Selection and exclusion audit

The selected policy is claim-level, not paper-level.

A source is not removed merely because its global proof fails. Instead:

```text
A = positive prior art
B = conditional/open prior art
C = split/partial absorption
D = rejected proof mechanism / negative control
FINITE_ONLY = bounded computation or finite observation
```

Post-hoc change check: failed sources are not excluded from the bibliography to make the project appear stronger. Their failed hinges remain visible and are converted into regression rules.

Verdict: **JUSTIFIED.**

## 5. Bridge audit

### Bridge LIT-1 — external theorem -> internal lemma

Requirement: hypotheses, quantifiers, domain, and conclusion must be preserved.

Status: JUSTIFIED only for class A claim units.

### Bridge LIT-2 — external conditional theorem -> unconditional closure

Status: PROHIBITED unless the additional hypothesis is independently proved.

### Bridge LIT-3 — failed external hinge -> internal anti-pattern

Requirement: failure must be localized by explicit counterexample, quotient defect, or quantifier mismatch.

Status: JUSTIFIED for the audited Nwankpa, Moon, fixed-window, spectral-gap and Ansari hinge examples.

### Bridge LIT-4 — finite evidence -> universal theorem

Status: PROHIBITED without a separate proof.

## 6. Material re-audit changes on 2026-09-07

### Cerdà survival measure

Previous status: `PROVISIONALLY SAFE / REPRODUCTION AUDIT PENDING`.

New status: **SAFE WITHIN RESTRICTED SURVIVAL DEFINITION**.

Independent reason: a finite valuation itinerary `(k_0,...,k_m)` determines one disjoint cylinder of relative odd-Haar mass `2^{-(k_0+...+k_m)}`. Summing over every further `k_i>=2` gives one-half conditional mass per step and therefore exact `2^{-N}` decay.

The terminal upgrades `measure zero -> emptiness` and `restricted escape -> ordinary convergence` remain prohibited.

Matching Math-verification commit: `2ac8fc96c597ede92ccb95c7f192e05fe1bbba40`.

### Nwankpa current version

Previous audit source: v6.

Current source: v9 (22 October 2025).

New status: **D — CURRENT VERSION RE-AUDITED**.

Material failure: the current state graph contains representative-dependent branches; `S11` reaches the terminal state only for `x=8`; graph reachability to `S11` does not imply every actual integer trajectory reaches `8`. An SCC with an exit can admit infinite internal walks.

Matching Math-verification commit: `fa404b6b3265cec6e40881220b7891e599e0af93`.

### Niu 2026

Previous status: absent from the formal ledger.

New status: **A + FINITE/CONJECTURAL split**.

Safe claims: exact parity-cylinder count, analytic fixed-length paradoxical enumeration, bounded-length density-zero theorem.

Not imported: CST, universal all-length best-approximation conjecture.

Matching Math-verification commit: `1bafc5d5d2d6b6d91bc523311c9d4768ab0be95f`.

## 7. Anti-pattern citation rules

The following failures are retained as explicit negative controls:

```text
AP-1 almost-all/density -> universal pointwise
AP-2 coarse finite state -> faithful deterministic quotient
AP-3 existential good path -> inevitable actual path
AP-4 quotient-depth bound -> fixed universal orbit window
AP-5 averaged/spectral contraction -> pathwise deterministic contraction
AP-6 symbolic or 2-adic survivor -> positive ordinary integer
AP-7 auxiliary decomposition -> universal coverage
AP-8 residue representative -> actual-integer quantity without invariance
```

These are methodological regression constraints, not claims that every source exhibiting one pattern has no valid theorem anywhere else.

## 8. Eight-axis summary

| Axis | Audit result |
|---|---|
| D — Describability | Claim units and source versions are explicitly identifiable. |
| R — Resolution | Paper-level, theorem-level, finite-computation and global-hinge layers are separated. |
| S — Selection | Both favorable and failed sources remain in the corpus. |
| E — Exclusion | No failed source is silently erased; unusable bridges are excluded by reason. |
| T — Transition | Import bridges and forbidden upgrades are explicit. |
| C — Consistency | New v9/Niu/Cerdà updates remove the known stale/pending statuses. |
| N — Norm | Ordinary mathematical validity remains the external standard; DSD does not replace it. |
| O — Outcome | Citation bookkeeping for the currently imported corpus is complete. |

## 9. Final verdict

```text
VERDICT: CONFIRMED WITH CLAIM-LEVEL SPLIT CLASSIFICATION
MAXIMUM_SUPPORTED_CLAIM:
The external literature currently imported or explicitly audited by the Collatz repository has a traceable citation status as of 2026-09-07. Known pending/stale items were resolved or updated.

UNSUPPORTED_OR_UNRESOLVED_CLAIMS:
That every Collatz publication has been audited; that class-B hypotheses are true; that failed global proofs contain no valid local lemmas; that the Collatz conjecture is solved.

EXTERNAL_DOMAIN_VERDICT:
Mathematically valid claim units may be cited positively; invalid or unsupported hinges may be cited only as localized negative controls.

DSD_STRUCTURAL_AUDIT_VERDICT:
CONFIRMED. The policy preserves source lineage, quantifiers, alternatives, failures, and reconstruction boundaries.
```

## 10. Reproducibility and traceability

Primary Math-verification ledger:

`collatz/notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md`

Ledger commit:

`3ffa3d0415055b53e9de42970c7e9a947dbb6570`

Key historical/current commits:

- `887fba789d43fa16d702c14528398cc07632cd71` — master literature absorption matrix;
- `006b095fb5259c985930094aa823d9a0af54b91a` — established literature comparison + Moon mod-64 audit;
- `422e9048f8253e29b25aaf4b2cda6582cb4aaec1` — Moon exact aliasing certificate;
- `0b2122a1bd81175ab6be5bc7ecf372aa714317e4` — fixed-block mechanism audit;
- `4359ac9214824b18c3ad4a8d5d516182e8eab1bf` — exact fixed-window counterexample;
- `4f8614fe2dabd4f22d577a10d39a05fce4b86e3a` — spectral annealed/pathwise audit;
- `17c1aa8988f034c02c029dc6ff2954007f81a12a` — Cerdà first partial audit;
- `2ac8fc96c597ede92ccb95c7f192e05fe1bbba40` — Cerdà reproduction completion;
- `173b62cd3bf37886989e8399fef53a6346c7b30b` — Nwankpa v6 audit;
- `096dd1fd634621c5faada4c7ffbe40fd64d32431` — FSM quotient regression;
- `fa404b6b3265cec6e40881220b7891e599e0af93` — Nwankpa v9 re-audit;
- `1bafc5d5d2d6b6d91bc523311c9d4768ab0be95f` — Niu 2026 positive/split audit;
- `df0a6550e5a1ec2e1cdd67feae8c0f0128e325dd` — Ansari-dependent global-floor downgrade.

Revision policy: future new literature additions require a new claim-unit record; this audit should not be silently expanded retroactively.