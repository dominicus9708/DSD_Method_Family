# 02. DSD Audit / DSD 감사

Status: **established**

Role: retrace an analysis, calculation, judgment, process, or record under explicit scope, interface, evidence, procedure, and verdict rules.

Canonical existing module: [`../../DSD_Audit/`](../../DSD_Audit/).

This directory is a registry wrapper only. The dedicated audit module is intentionally not moved.

Primary checks:
- scope and version lock;
- evidence provenance and selection/exclusion;
- DSD object status vs audit evidence status;
- missing or implicit bridges;
- unsupported reconstruction from aggregates;
- transition and lineage obligations;
- reproducibility and unresolved regions.

An analysis result is not automatically an audit pass.
