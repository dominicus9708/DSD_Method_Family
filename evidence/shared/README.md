# Shared Method-Family Evidence / 방법군 공통 규율 증거

This folder records evidence for **shared operating disciplines** that may be reused across multiple DSD methods.

It does **not** directly validate the correctness, performance, or usefulness of every method.

## Shared rule families / 공통 규율군

- status discipline: absence, undefinedness, inapplicability, prerequisite failure, and defined zero remain distinct when the selected interface distinguishes them;
- bridge discipline: cross-layer and cross-domain mappings require explicit justification;
- minimum-layer discipline: use only the DSD layers required by the task;
- aggregate/reconstruction discipline: equal aggregate does not imply equal support, decomposition, cause, or history without a reconstruction basis;
- specialization restraint: removing optional specialization withdraws specialization-dependent claims without inventing defaults;
- failure / NO_GAIN preservation: negative, null, non-correspondence, and indeterminate results remain valid records;
- strongest-baseline discipline: comparison must not rely only on a weak strawman baseline;
- precommit / anti-post-hoc discipline: locked criteria or predictions are not silently rewritten after reveal.

## Required record fields

```text
EVIDENCE_SCOPE_CLASS: shared_method_family
SHARED_RULES_SUPPORTED:
SOURCE_RECORDS:
METHODS_DIRECTLY_TESTED:
METHODS_NOT_DIRECTLY_VALIDATED:
TRANSFER_LIMIT:
REPRODUCIBILITY_RECORD:
```

A shared rule should later be re-tested inside each method whose task interface materially changes how that rule operates.
