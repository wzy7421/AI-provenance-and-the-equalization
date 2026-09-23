# Code availability wording

## Current repository state — manuscript-safe wording now

> A public repository containing the release validator and reproducibility-file structure is available at https://github.com/wzy7421/AI-provenance-and-the-equalization. The complete analysis code used to generate the manuscript's reported statistical estimates and figures is not yet included in the public repository.

Use this wording while `scripts/` contains only release-validation or template material.

Do **not** state that the analysis code supporting the reported results is publicly available until the executable scripts that reproduce the manuscript outputs have been uploaded and checked.

## Final verified public release — use only after analysis scripts are present

> Analysis code used to reproduce the statistical analyses, reported contrasts, tables and figures in this article is publicly available at https://github.com/wzy7421/AI-provenance-and-the-equalization.

The final public code should reproduce at minimum:

- Study 1 claim-quality estimates, capacity-gap change and Figure 2;
- Study 2 support and approval contrasts and Figure 3;
- Study 3 marginal approval probabilities, net outcome equalization, gap-level conversion loss, capacity-specific conversion loss and Figure 4;
- Study 4 support contrasts, descriptive safeguard analyses and Figure 5;
- any reported multiplicity adjustment and manuscript tables derived from the released data.

## Recommended script organization

A clear final layout is:

```
scripts/
  00_session_info.*
  01_prepare_analysis_data.*
  10_study1_analysis.*
  20_study2_analysis.*
  30_study3_analysis.*
  40_study4_analysis.*
  90_make_figures.*
  99_reproduce_all.*
  validate_release.py
```

Use the actual language and filenames from the executed analysis. Do not create placeholder scripts and describe them as reproducing results.
