# Data availability wording

## Current repository state — manuscript-safe wording now

> A public repository containing the data-release schema, data dictionary and synthetic demonstration files is available at https://github.com/wzy7421/AI-provenance-and-the-equalization. The current public repository does not contain the empirical participant-level or evaluator–message datasets used for the reported analyses. Verified de-identified analysis datasets will be released only after participant-flow reconciliation, disclosure-risk review and reproducibility checks are complete.

Use this version while `data/final/` does not contain the verified empirical release.

Do **not** state that de-identified participant-level or decision-level empirical data are publicly available while the repository contains only the schema/demo package.

## Final verified public release — use only after upload and validation

> De-identified participant-level, rater-level and evaluator–message decision-level data supporting the reported analyses are publicly available at https://github.com/wzy7421/AI-provenance-and-the-equalization. The repository includes the data dictionary and separates writer/message, rater and evaluator–message decision units across the four studies.

If some fields cannot be shared because of consent, privacy, contractual or re-identification constraints, replace the statement above with a precise description of what is public, what is restricted and how qualified researchers can request access, if applicable.

## Conditions for switching to the final wording

Do not switch to the final wording until all of the following are true:

- `data/final/` contains the six verified empirical release files listed in the repository README.
- Recruitment, randomization, exclusion and analysed-sample counts reconcile with source records.
- Study 1 rater-level records reproduce the reported reliability and any rater-escalation rule.
- Study 2 fixed-text provenance comparisons are verified item-by-item.
- Study 3 writer/message and evaluator decision records reproduce the realized allocation topology and all reported marginal probability contrasts.
- Study 4 policy-arm records reproduce the reported support, approval and merit-accuracy summaries.
- Direct identifiers and high-risk free text have been removed or appropriately transformed.
- The released analysis code reproduces the manuscript's main numerical results and figures.

## Recommended persistent archive

After verification, create a tagged GitHub release and archive that exact release in a DOI-granting repository such as Zenodo. Prefer citing the archived DOI rather than relying only on a mutable branch URL.
