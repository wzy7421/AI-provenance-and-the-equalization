# Analysis scripts

## Current status

At present this directory contains `validate_release.py`, which checks the structure of the intended de-identified empirical release. It does **not** reproduce the manuscript's statistical estimates or figures.

## Required final reproducibility scope

Before the manuscript states that analysis code is publicly available, add the actual executed scripts used to generate the reported results.

At minimum, the final code should reproduce:

1. **Study 1** — standardized claim-quality estimates, the capacity-related quality-gap change and Figure 2.
2. **Study 2** — fixed-text provenance support/approval contrasts and Figure 3.
3. **Study 3** — the final logistic-regression workflow, two-way writer/message × evaluator cluster-robust covariance, marginal standardization, delta-method uncertainty, the reported net-equalization and conversion-loss contrasts, and Figure 4.
4. **Study 4** — policy-arm support contrasts, reported descriptive safeguard comparisons and Figure 5.
5. Any Holm-adjusted P values or other multiplicity procedures that appear in the final manuscript.

## Reproducibility principle

Every number described as a model estimate in the manuscript should be traceable to one executable analysis path. In particular, Study 3 should not mix outputs from a crossed mixed-effects model with outputs from a separate fixed-effects logistic model.

A top-level `99_reproduce_all.*` script is recommended so reviewers can regenerate all manuscript outputs in a documented order.
