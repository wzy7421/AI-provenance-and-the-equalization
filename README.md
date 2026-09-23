# AI provenance and the equalization of institutional self-advocacy

Repository for the manuscript **“AI provenance and the equalization of institutional self-advocacy.”**

> **Current repository status: release schema + synthetic demonstration data only.**
>
> The current public files are a release template, codebook and small synthetic examples that mirror the intended analysis structure. They are **not** the empirical participant-level or decision-level datasets used for the manuscript and cannot reproduce the reported numerical estimates. Do not cite this repository as containing the final empirical data until the files listed under **Final empirical release** and the corresponding analysis scripts have been added and validated.

## Study architecture

| Study | Analysed people | Core design | Primary unit / outcome |
|---|---:|---|---|
| Study 1 | 4,608 writers | Randomized AI access × continuous baseline advocacy capacity; US/UK × consumer/workplace | Writer/message; Advocacy Quality Index and capacity-related quality-gap change |
| Study 2 | 3,456 evaluators | Byte-identical claim text; hidden vs truthful visible AI provenance | Evaluator–message decision; 0–100 incentivized support allocation |
| Study 3 | 3,456 writers + 6,912 evaluators | Linked production–reception pipeline; 27,648 decisions | Evaluator–message decision; net staged-provenance equalization and gap-level conversion loss |
| Study 4 | 4,608 evaluators | Generic, neutral matched, human-control/responsibility attestation, staged review | Evaluator–message decision; average support mitigation and merit-accuracy safeguard |

## Repository layout

```
.
├── README.md
├── DATA_AVAILABILITY.md
├── CODE_AVAILABILITY.md
├── REPLACEMENT_CHECKLIST.md
├── data/
│   ├── README.md
│   ├── release_manifest.csv
│   ├── codebook.csv
│   ├── demo/
│   │   ├── study1_synthetic_demo.csv
│   │   ├── study2_synthetic_demo.csv
│   │   ├── study3_synthetic_demo.csv
│   │   └── study4_synthetic_demo.csv
│   └── final/
│       └── README.md
└── scripts/
    ├── README.md
    └── validate_release.py
```

## Final empirical release

Before the manuscript states that empirical data and reproducibility code are publicly available, the repository should contain verified, de-identified versions of:

- `data/final/study1_writer_level.csv`
- `data/final/study1_rater_level.csv`
- `data/final/study2_decision_level.csv`
- `data/final/study3_writer_level.csv`
- `data/final/study3_decision_level.csv`
- `data/final/study4_decision_level.csv`

and executable analysis scripts that reproduce the manuscript's reported estimates, tables and figures from those release files.

The final Study 3 analysis must reproduce, from a single documented fitted-model workflow, the reported marginal approval probabilities and the 12.55-percentage-point staged-provenance equalization, 7.12-percentage-point visible-provenance equalization and 5.43-percentage-point gap-level conversion loss.

## Synthetic demo files

Files under `data/demo/` are intentionally synthetic. They should retain the `synthetic_demo = 1` marker and must never be renamed or presented as empirical observations.

## Validation

After placing verified empirical files in `data/final/`, run:

```bash
python scripts/validate_release.py
```

The validator checks release structure, required columns, key manuscript counts, allowed treatment labels and obvious accidental inclusion of synthetic/demo or direct-identifier fields. Passing the structural validator does **not** establish statistical reproducibility; the released analysis scripts must also reproduce the manuscript outputs.

## Manuscript availability statements

See:

- [DATA_AVAILABILITY.md](DATA_AVAILABILITY.md)
- [CODE_AVAILABILITY.md](CODE_AVAILABILITY.md)

Each file contains wording for both the current placeholder state and the final verified public release. Use only wording that matches the repository's actual contents at the time of submission.

## Archival release

For submission or acceptance, freeze the verified repository state as a versioned GitHub release and archive that exact release in a DOI-granting repository such as Zenodo. Cite the immutable archived version in the final manuscript when available.
