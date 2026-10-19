# DSD Audit Domain Protocols / DSD 감사 분야별 프로토콜

This directory contains field-specific extensions of the **DSD General Audit Framework**.

이 디렉터리는 DSD 감사의 공통 골격에 각 분야의 기존 검증 기준을 추가하는 전용 위치입니다.

## Operating rule / 운영 원칙

The common DSD audit frame traces describability, resolution, selection, exclusion, transition, consistency, norms, and outcome.
It does not replace the audited field's own standards.

Every domain protocol should define:

1. the external standards used by the field;
2. which common DSD audit axes apply without modification;
3. additional fields required by the domain;
4. DSD analogies or reductions that must not be made;
5. minimal witness, counterexample, or boundary-case format;
6. domain-specific verdict vocabulary when needed;
7. the relation between the external-domain verdict and DSD structural audit verdict.

## Planned protocol groups / 기본 분류

```text
protocols/
├─ mathematics/
├─ science/
├─ law/
├─ software/
├─ ai/
├─ history_media/
├─ administration_organization/
└─ README.md
```

Directories are created when the first real protocol or audit in that domain is added.

## Minimum domain additions / 분야별 최소 추가 항목

### Mathematics / 수학
- exact definitions, axioms, theorem statement
- proof-step justification
- counterexamples and boundary cases
- finite computation vs. general proof

### Science / 과학
- hypothesis, model, observation, experiment separation
- measurement uncertainty and descriptive resolution
- alternative hypotheses
- reproducibility and external data
- constitutive assumptions and bridges where used

### Law and institutions / 법·제도
- historically available information
- fact/evidence/inference/norm/judgment separation
- procedural authority and burden/standard of proof
- competing describable possibilities

### Software and algorithms / 소프트웨어·알고리즘
- specification, implementation, environment, output separation
- input domain and exception handling
- branch/state transitions
- versions, dependencies, deterministic/seeded reproduction

### AI / AI
- input, prompt, tools, references, evaluation data, output separation
- observable process claims vs. unobservable internal-state claims
- benchmark/sample selection
- hallucination, omission, bias, reproducibility

### History, documents, media / 역사·문헌·언론
- primary vs. secondary sources
- historical information state vs. later knowledge
- quotation, omission, selection bias
- competing interpretations and irreducible uncertainty

### Administration, organization, policy / 행정·조직·정책
- authority and information flow
- available options and exclusion criteria
- facts vs. policy goals and norms
- hindsight bias

## Result format / 결과 형식

Every domain audit ends with three separate summaries:

1. **External-domain verdict**
2. **DSD structural audit verdict**
3. **Correspondence and limits**

Do not combine them into a single success percentage or validation rate.

## Active mathematics protocol / 시행 준비된 수학 프로토콜 (2026-10-19)
- [FPA v0.1 — Formal Proof Audit](mathematics/FORMAL_PROOF_AUDIT_v0.1.md): theorem-level proof-obligation and countermodel audit, using the target domain's mathematical standards rather than DSD-internal success as a truth criterion.
- [Formation F2 first case](../audits/formal_proof/formation_axiom_system/README.md): **prepared, not executed**. No mathematical theorem verdict issued.
- Notion: https://app.notion.com/p/3fe81f51e7fa81afb612fa69387cdeee

This specialized Audit protocol does not create an independent 23rd method, re-open the 22/22 internal build, or imply external independent validation.
