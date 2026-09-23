# AI provenance and the equalization of institutional self-advocacy

Repository for the manuscript **“AI provenance and the equalization of institutional self-advocacy.”**

> **Repository status (important): SCHEMA + SYNTHETIC DEMONSTRATION DATA ONLY.**  
> The files currently stored here are a release template and small synthetic examples designed to mirror the **structure and qualitative direction** of the four-study programme. They are **not the empirical participant-level data** used for the manuscript and must not be used to verify or reproduce the reported numerical estimates. Replace the demo files with the verified de-identified analysis datasets before making a manuscript claim that the empirical data are publicly available.

## Study architecture

| Study | Analysed people | Core design | Primary unit / outcome |
|---|---:|---|---|
| Study 1 | 4,608 writers | Randomized AI access × continuous baseline advocacy capacity; US/UK × consumer/workplace | Writer/message; Advocacy Quality Index and capacity-related quality-gap change |
| Study 2 | 3,456 evaluators | Byte-identical claim text; hidden vs truthful visible AI provenance | Evaluator–message decision; 0–100 incentivized support allocation |
| Study 3 | 3,456 writers + 6,912 evaluators | Linked crossed production–reception pipeline; 27,648 decisions | Evaluator–message decision; net staged-provenance equalization and gap-level conversion loss |
| Study 4 | 4,608 evaluators | Generic, neutral matched, human-control/responsibility attestation, staged review | Evaluator–message decision; average support mitigation and merit-accuracy safeguard |

The manuscript distinguishes **baseline advocacy capacity** from structural-position variables and treats provenance policy as a reception-stage intervention. The central linked quantity is **distributional expression-to-outcome conversion loss**: the amount by which visible AI provenance attenuates an otherwise equalizing AI-assistance regime in downstream gatekeeper decisions.

## Repository layout

```
.
├── README.md
├── DATA_AVAILABILITY.md
├── REPLACEMENT_CHECKLIST.md
├── data/
│   ├── README.md
│   ├── release_manifest.csv
│   ├── codebook.csv
│   └── demo/
│       ├── study1_synthetic_demo.csv
│       ├── study2_synthetic_demo.csv
│       ├── study3_synthetic_demo.csv
│       └── study4_synthetic_demo.csv
└── scripts/
    └── validate_release.py
```

## Intended final release

Before submission or public-data claims, replace the synthetic demo with verified, de-identified study files using the stable filenames below:

- `data/final/study1_writer_level.csv`
- `data/final/study1_rater_level.csv`
- `data/final/study2_decision_level.csv`
- `data/final/study3_writer_level.csv`
- `data/final/study3_decision_level.csv`
- `data/final/study4_decision_level.csv`

The exact realized record counts, exclusions, missingness, rater escalation, allocation topology and fitted-model basis must be reconciled against the immutable recruitment, randomization, event-log and analysis records before release.

## Synthetic demo files

The files under `data/demo/` are intentionally small and include `synthetic_demo = 1`. They reflect only the study logic and broad directional pattern:

- Study 1: AI assistance produces larger illustrative gains at lower baseline advocacy capacity.
- Study 2: visible AI provenance is associated with lower illustrative support/approval for fixed text.
- Study 3: staged provenance shows stronger illustrative equalization than visible provenance.
- Study 4: staged review and the bundled human-control/responsibility attestation show illustrative mitigation relative to generic disclosure.

**The demo values do not reproduce the manuscript estimates and should never be cited as empirical results.**

## Validation

After placing final files in `data/final/`, run:

```bash
python scripts/validate_release.py
```

The validator checks required columns, expected study-level record counts where they are fixed by the manuscript, allowed treatment labels and accidental inclusion of the synthetic-demo flag.

## Data availability wording

See [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md) for manuscript-safe wording for the current placeholder stage and for the final verified public release.

## Repository link

Stable repository URL:

`https://github.com/wzy7421/AI-provenance-and-the-equalization`

Raw-file links can be added after the final datasets replace the demo files.

## Citation

Until the manuscript is published, cite the manuscript title and this repository URL. Add the final article DOI and an archived release DOI (for example, Zenodo) when available.
