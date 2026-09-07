# DSD Audit / DSD 감사

This folder is the dedicated home for **DSD Audit**, separated from **DSD Analysis** while remaining interoperable with it.

이 폴더는 **DSD 분석론**과 구분하여 **DSD 감사**의 방법론·기록·프로토콜·향후 알고리즘화 계획을 관리하는 전용 위치입니다.

## Distinction from DSD Analysis / DSD 분석론과의 구분

- **DSD Analysis / DSD 분석론**: decomposes, compares, and reinterprets structures.
- **DSD Audit / DSD 감사**: retraces an analysis, calculation, judgment, or record under an explicit scope, interface lock, procedure, evidence basis, and verdict rule.

An analysis result is not automatically an audit pass, and an audit failure does not automatically imply that the audited object is false in every sense.

## Shared DSD interface / 공유 DSD 인터페이스

The paper-facing DSD layer model remains shared and is maintained at:

- [`../methodology/DSD_INTERFACE_PROFILE.md`](../methodology/DSD_INTERFACE_PROFILE.md)

DSD Audit uses that profile when Formation, General Property, Static Aggregation, Dynamics, or optional specialization materially affects a case.

## Folder structure / 폴더 구조

```text
DSD_Audit/
├─ README.md
├─ methodology/
│  ├─ GENERAL_AUDIT_FRAMEWORK.md
│  ├─ AUDIT_RECORDING_STANDARD.md
│  └─ AUDIT_ALGORITHMIZATION_ROADMAP.md
├─ templates/
│  └─ AUDIT_CASE_TEMPLATE.md
├─ protocols/
│  └─ README.md
└─ audits/
   ├─ README.md
   ├─ methodology/
   └─ mathematics/
      └─ README.md
```

Current domain navigation:

- [`audits/README.md`](audits/README.md) — audit-record policy and domain layout
- [`audits/mathematics/README.md`](audits/mathematics/README.md) — current mathematics audit index; currently includes the Collatz `MATH-001..007` sequence

Domain indexes are navigation aids. Historical audit records remain at their original paths unless an explicit migration is required.

## Operating rule / 운영 원칙

1. Lock the audit question, scope, time, descriptive resolution, and external standard.
2. Lock the DSD interface profile and exact source revisions when DSD formal layers matter.
3. Preserve original claims and sources before reinterpretation.
4. Separate audit evidence status from DSD object status.
5. Record selections and exclusions.
6. Record material bridges, aggregation/reconstruction assumptions, transition classes, and lineage requirements.
7. Preserve alternatives, witnesses, counterexamples, and unresolved regions.
8. End with external-domain verdict, DSD structural audit verdict, limits, and reproducibility information.

## Historical paths / 기존 경로

Older audit methodology and records may still exist in previous repository locations. They are preserved as historical/legacy paths and should not be silently rewritten. New audit methodology and new audit cases should use this `DSD_Audit/` structure.
