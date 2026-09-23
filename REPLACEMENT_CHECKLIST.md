# Final replacement checklist

This repository is intentionally set up so the synthetic demo can be replaced without changing the public repository URL used in the manuscript.

## 1. Freeze the empirical source records

Before export, reconcile the final analysis population against recruitment, eligibility, randomization, non-completion, technical-loss and missing-outcome records.

## 2. Create de-identified release tables

Create these files under `data/final/`:

1. `study1_writer_level.csv`
2. `study1_rater_level.csv`
3. `study2_decision_level.csv`
4. `study3_writer_level.csv`
5. `study3_decision_level.csv`
6. `study4_decision_level.csv`

Use opaque IDs only. Do not release names, email addresses, phone numbers, IP addresses, exact street addresses, raw device fingerprints or any other direct identifier.

## 3. Preserve analysis-unit separation

People, messages, ratings and evaluator–message decisions are distinct units. Do not merge them into one flat table in a way that creates pseudo-replication or obscures the dependence structure.

## 4. Reconcile manuscript-critical quantities

### Study 1
- 4,608 analysed writers.
- Randomized unaided versus AI-assisted assignment.
- Continuous pre-treatment baseline advocacy capacity.
- Advocacy Quality Index construction and factual-fidelity rule.
- Rater-level records sufficient to verify reliability and any escalation.

### Study 2
- 3,456 analysed evaluators.
- Fixed substantive claim text within message item.
- Hidden versus truthful visible AI provenance.
- 0–100 support allocation and binary approval.

### Study 3
- 3,456 analysed writers.
- 6,912 analysed evaluators.
- 27,648 evaluator–message decisions.
- Unaided/baseline, AI/staged and AI/visible regimes.
- Realized evaluator–message crossing, message nesting, order and connectivity.
- Final fitted-model object/code that generates the reported marginal probabilities, net equalization and gap-level conversion loss.

### Study 4
- 4,608 analysed evaluators.
- Generic disclosure, neutral matched disclosure, human-control/responsibility attestation and staged review.
- Support, approval and merit-accuracy outcomes.
- Policy timing and within-item text identity.

## 5. Replace demo files

Keep `data/demo/` only if you want a teaching example. If retained, leave the filenames and `synthetic_demo = 1` flag unchanged so they can never be confused with the empirical release.

## 6. Run validation

```bash
python scripts/validate_release.py
```

Resolve every ERROR before public release. WARNINGS should be reviewed against the final protocol and analysis objects.

## 7. Freeze a release

Create a tagged release (for example `v1.0.0`) after manuscript/data reconciliation. Archive that exact release in a DOI-granting repository if the target journal expects a persistent research-data identifier.
