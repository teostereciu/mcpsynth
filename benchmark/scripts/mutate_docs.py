#!/usr/bin/env python3
"""
Apply parameter name mutations to API documentation for contamination testing.

Creates a mutated copy of a dataset's docs/ folder with parameter names renamed.
The synthesizer then reads mutated docs; if the output uses mutated names it was
reading the docs. If output uses original names, it relied on parametric memory.

Usage:
    uv run python benchmark/scripts/mutate_docs.py github
    uv run python benchmark/scripts/mutate_docs.py github --spec path/to/mutations.json
    uv run python benchmark/scripts/mutate_docs.py github --show   # dry-run: print substitution counts
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
DATASETS_DIR = Path(__file__).parent.parent / "datasets"


def apply_mutations(text: str, mutations: list[dict]) -> tuple[str, dict[str, int]]:
    """Apply all mutations to text using whole-word replacement. Returns (new_text, counts)."""
    counts = {}
    for m in mutations:
        orig = re.escape(m["original"])
        pattern = rf"\b{orig}\b"
        matches = len(re.findall(pattern, text))
        if matches:
            text = re.sub(pattern, m["mutated"], text)
            counts[m["original"]] = matches
    return text, counts


def mutate_dataset(dataset: str, spec_path: Path | None, dry_run: bool) -> None:
    dataset_dir = DATASETS_DIR / dataset
    docs_dir = dataset_dir / "docs"
    out_dir = dataset_dir / "docs_mutated"

    if not docs_dir.exists():
        print(f"Error: {docs_dir} does not exist")
        sys.exit(1)

    # Load mutation spec
    if spec_path is None:
        spec_path = dataset_dir / "mutations.json"
    if not spec_path.exists():
        print(f"Error: mutation spec not found at {spec_path}")
        sys.exit(1)

    spec = json.loads(spec_path.read_text())
    mutations = spec["mutations"]

    print(f"Dataset:   {dataset}")
    print(f"Spec:      {spec_path.name}")
    print(f"Mutations: {len(mutations)}")
    for m in mutations:
        print(f"  {m['original']} → {m['mutated']}")
    print()

    doc_files = sorted(docs_dir.rglob("*.md"))
    total_counts: dict[str, int] = {}

    if not dry_run:
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)

    for doc_file in doc_files:
        text = doc_file.read_text()
        mutated_text, counts = apply_mutations(text, mutations)

        for k, v in counts.items():
            total_counts[k] = total_counts.get(k, 0) + v

        if not dry_run:
            rel = doc_file.relative_to(docs_dir)
            out_file = out_dir / rel
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(mutated_text)

    print("Substitution counts across all docs:")
    for orig, count in sorted(total_counts.items(), key=lambda x: -x[1]):
        mutated = next(m["mutated"] for m in mutations if m["original"] == orig)
        print(f"  {orig:20s} → {mutated:20s}  ({count} occurrences)")

    unmatched = [m["original"] for m in mutations if m["original"] not in total_counts]
    if unmatched:
        print(f"\nWarning: no matches found for: {', '.join(unmatched)}")

    if not dry_run:
        print(f"\nOutput: {out_dir}  ({len(doc_files)} files)")
    else:
        print("\n(dry run — no files written)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Mutate API docs for contamination testing")
    parser.add_argument("dataset", help="Dataset name (e.g. github)")
    parser.add_argument("--spec", type=Path, help="Path to mutations.json (default: <dataset>/mutations.json)")
    parser.add_argument("--show", action="store_true", help="Dry run: show substitution counts without writing files")
    args = parser.parse_args()

    mutate_dataset(args.dataset, args.spec, dry_run=args.show)


if __name__ == "__main__":
    main()
