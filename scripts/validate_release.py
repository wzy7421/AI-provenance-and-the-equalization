#!/usr/bin/env python3
"""Structural validator for the final de-identified release.

This script does not validate statistical estimates. It checks only release
structure, fixed manuscript counts, required columns, treatment labels and
obvious accidental inclusion of synthetic/demo or direct-identifier fields.
"""

from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / "data" / "final"

SPECS = {
    "study1_writer_level.csv": {
        "rows": 4608,
        "required": {
            "writer_id", "country", "context", "vignette_id", "message_id",
            "assignment_ai", "baseline_capacity_C", "advocacy_quality_z",
            "unsupported_assertion"
        },
        "cats": {"assignment_ai": {"unaided", "ai_assisted"}},
        "unique": ["writer_id", "message_id"],
    },
    "study1_rater_level.csv": {
        "rows": None,
        "required": {
            "rater_id", "message_id", "actionability", "argument_quality",
            "clarity", "coherence", "factual_completeness", "specificity"
        },
        "cats": {},
        "unique": [],
    },
    "study2_decision_level.csv": {
        "rows": 3456,
        "required": {
            "evaluator_id", "message_id", "country", "context", "provenance",
            "support_0_100", "approval"
        },
        "cats": {"provenance": {"hidden", "visible"}},
        "unique": ["evaluator_id"],
    },
    "study3_writer_level.csv": {
        "rows": 3456,
        "required": {
            "writer_id", "message_id", "baseline_capacity_C",
            "production_assignment", "country", "context"
        },
        "cats": {"production_assignment": {"unaided", "ai_assisted"}},
        "unique": ["writer_id", "message_id"],
    },
    "study3_decision_level.csv": {
        "rows": 27648,
        "required": {
            "decision_id", "evaluator_id", "writer_id", "message_id",
            "vignette_id", "baseline_capacity_C", "production_assignment",
            "provenance_policy", "approval"
        },
        "cats": {
            "production_assignment": {"unaided", "ai_assisted"},
            "provenance_policy": {"baseline", "staged", "visible"},
        },
        "unique": ["decision_id"],
        "expected_unique": {"evaluator_id": 6912, "writer_id": 3456, "message_id": 3456},
    },
    "study4_decision_level.csv": {
        "rows": 4608,
        "required": {
            "decision_id", "evaluator_id", "message_id", "country", "context",
            "policy_arm", "support_0_100", "approval", "merit_accuracy"
        },
        "cats": {"policy_arm": {"generic", "neutral", "attestation", "staged"}},
        "unique": ["decision_id", "evaluator_id"],
    },
}

FORBIDDEN_HEADER_TERMS = {
    "name", "full_name", "email", "phone", "telephone", "ip", "ip_address",
    "street_address", "home_address", "exact_address"
}

def load_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames or [], rows

def main():
    errors = 0
    warnings = 0

    if not FINAL.exists():
        print("ERROR: data/final/ does not exist. Add verified empirical release files first.")
        return 1

    for filename, spec in SPECS.items():
        path = FINAL / filename
        print(f"\n[{filename}]")
        if not path.exists():
            print("ERROR: missing file")
            errors += 1
            continue

        header, rows = load_csv(path)
        hset = set(header)
        missing = spec["required"] - hset
        if missing:
            print("ERROR: missing required columns:", ", ".join(sorted(missing)))
            errors += 1

        forbidden = hset & FORBIDDEN_HEADER_TERMS
        if forbidden:
            print("ERROR: possible direct-identifier columns:", ", ".join(sorted(forbidden)))
            errors += 1

        if "synthetic_demo" in hset:
            bad = [r for r in rows if str(r.get("synthetic_demo", "")).strip() not in {"", "0", "false", "False"}]
            if bad:
                print("ERROR: synthetic_demo flag is present in final data")
                errors += 1

        if spec["rows"] is not None and len(rows) != spec["rows"]:
            print(f"ERROR: expected {spec['rows']} records from manuscript, found {len(rows)}")
            errors += 1
        else:
            print(f"records: {len(rows)}")

        for col, allowed in spec.get("cats", {}).items():
            if col in hset:
                vals = {str(r.get(col, "")).strip() for r in rows if str(r.get(col, "")).strip()}
                unexpected = vals - allowed
                if unexpected:
                    print(f"ERROR: unexpected {col} labels: {sorted(unexpected)}")
                    errors += 1

        for col in spec.get("unique", []):
            if col in hset:
                vals = [r.get(col, "") for r in rows]
                if "" in vals or None in vals:
                    print(f"ERROR: blank {col}")
                    errors += 1
                elif len(vals) != len(set(vals)):
                    print(f"ERROR: {col} is not unique")
                    errors += 1

        for col, expected_n in spec.get("expected_unique", {}).items():
            if col in hset:
                n = len({r.get(col, "") for r in rows if r.get(col, "") != ""})
                if n != expected_n:
                    print(f"ERROR: expected {expected_n} unique {col}, found {n}")
                    errors += 1

        if filename == "study1_rater_level.csv":
            print("WARNING: realized rater-level record count is intentionally not hard-coded; verify against rating/escalation logs.")
            warnings += 1

    print(f"\nValidation complete: {errors} error(s), {warnings} warning(s).")
    if errors:
        print("Do not describe the empirical data as publicly verified until all errors are resolved.")
        return 1
    print("Structural checks passed. Statistical reproduction and source-record reconciliation are still required.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
