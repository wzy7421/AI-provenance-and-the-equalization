# Data availability wording

## Current repository state — use this wording now

> A public repository containing the data-release schema, codebook and synthetic demonstration files is available at https://github.com/wzy7421/AI-provenance-and-the-equalization. The current repository does **not** contain the empirical participant-level datasets used for the reported analyses. Verified de-identified analysis datasets and reproducibility materials will replace the synthetic demonstration files before any claim of full public data availability is made.

Do **not** write “all data are publicly available” while the repository contains only the schema/demo package.

## Final verified public release — use only after replacement and validation

> De-identified participant-level and decision-level data, the data dictionary, study materials and analysis code supporting the reported results are publicly available at https://github.com/wzy7421/AI-provenance-and-the-equalization. The repository separates writer-, rater- and evaluator–message decision-level analysis units and documents the four-study production-to-reception design.

If some fields cannot be shared for privacy, contractual or re-identification reasons, replace the sentence above with a precise statement naming what is shared, what is restricted and why.

## Recommended archival step

For a submitted or accepted article, create a versioned GitHub release and archive that release in a DOI-granting repository such as Zenodo. Then cite the archived DOI in the manuscript rather than relying only on a mutable GitHub branch.

## Minimum checks before switching to the final wording

- Participant-flow counts reconcile with recruitment and randomization records.
- Study 1 rater counts and any escalation rule reconcile with rating logs.
- Study 2 fixed-text provenance comparisons are verified item-by-item.
- Study 3 evaluator–message allocation topology and the fitted-model object producing the reported probability-scale contrasts are verified.
- Study 4 policy scripts, timing and matched-message implementation are verified.
- No direct identifiers or high-risk free text remain in public files.
- The released analysis code reproduces the manuscript tables/figures from the released or documented analysis data.
