# Data directory

## Important status

The current `demo/` files are **synthetic demonstration data**. They mirror the intended schema and broad qualitative direction of the manuscript but are not the empirical study records.

## Intended final files

| File | Analysis unit | Expected size from manuscript | Purpose |
|---|---|---:|---|
| `final/study1_writer_level.csv` | writer/message | 4,608 | AI access × continuous baseline capacity; claim-quality analysis |
| `final/study1_rater_level.csv` | rater × message | realized count to be verified | Quality dimensions, factual-fidelity adjudication, reliability |
| `final/study2_decision_level.csv` | evaluator–message decision | 3,456 | Fixed-text hidden vs visible provenance support/approval |
| `final/study3_writer_level.csv` | writer/message | 3,456 | Writer assignment and baseline capacity |
| `final/study3_decision_level.csv` | evaluator–message decision | 27,648 | Linked production–reception regimes and conversion-loss estimands |
| `final/study4_decision_level.csv` | evaluator–message decision | 4,608 | Provenance-policy mitigation and merit-accuracy outcomes |

## Key conceptual separation

- **Baseline advocacy capacity (C):** continuous, pre-treatment, task-relevant measured construct.
- **Structural-position variables (Z):** separate variables used for heterogeneity/distributional incidence; not proxies for C.
- **Claim quality (Q):** production-stage outcome, not the same scale as support or approval.
- **Support (S):** 0–100 gatekeeper allocation outcome.
- **Approval (Y):** binary gatekeeper decision.
- **Provenance (D):** reception-stage displayed provenance policy.

Do not infer a causal mediation pathway from C/Q to S/Y unless the final analysis explicitly identifies it. The manuscript's primary linked claim concerns regime-level outcome equalization and provenance-dependent conversion loss.

See `codebook.csv` for the release schema.
