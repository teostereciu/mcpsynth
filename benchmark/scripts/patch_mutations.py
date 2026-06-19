#!/usr/bin/env python3
"""
Patch a synthesized MCP server to fix the HTTP layer for mutated parameter names.

The mutation experiment introduces plausible-but-wrong parameter names into the
API docs. A synthesizer that reads the docs will use the mutated names in both:
  1. The MCP tool interface  (what the agent sees)        -- keep as-is
  2. HTTP request dict keys  (what the real API receives) -- fix back to original

This script replaces quoted string occurrences of mutated names (e.g. "filter_spec")
with the original names (e.g. "narrow") in the HTTP layer, while leaving Python/TS
identifiers (function params, variables) untouched so the tool interface is preserved.

Produces server_patched.py (and patched copies of generated_tools/*.py) alongside
the originals. Does not modify originals in-place.

Usage:
    uv run python benchmark/scripts/patch_mutations.py zulip azure-..._mutated
    uv run python benchmark/scripts/patch_mutations.py notion azure-..._mutated --dry-run
    uv run python benchmark/scripts/patch_mutations.py --all
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

DATASETS_DIR = Path(__file__).parent.parent / "datasets"


def load_mutations(dataset_dir: Path) -> list[dict]:
    mutations_file = dataset_dir / "mutations.json"
    if not mutations_file.exists():
        return []
    data = json.loads(mutations_file.read_text())
    return data.get("mutations", [])


def patch_file(
    src: Path,
    dst: Path,
    mutations: list[dict],
    dry_run: bool = False,
) -> list[str]:
    """
    Replace quoted string keys of mutated names with original names.

    Only replaces when the mutated name appears as a quoted string
    (e.g. "filter_spec" or 'filter_spec'), NOT as a bare identifier.
    This fixes HTTP dict keys while preserving function parameter names.

    Returns list of changes made.
    """
    text = src.read_text(encoding="utf-8", errors="ignore")
    changes = []

    for m in mutations:
        original = m["original"]
        mutated = m["mutated"]

        # Match quoted string: "mutated" or 'mutated'
        # Replace with same quote style + original name
        double_pattern = re.compile(r'"' + re.escape(mutated) + r'"')
        single_pattern = re.compile(r"'" + re.escape(mutated) + r"'")

        new_text = double_pattern.sub(f'"{original}"', text)
        new_text = single_pattern.sub(f"'{original}'", new_text)

        if new_text != text:
            n_double = len(double_pattern.findall(text))
            n_single = len(single_pattern.findall(text))
            changes.append(
                f"  {mutated!r} → {original!r}  ({n_double} double-quoted, {n_single} single-quoted replacements)"
            )
            text = new_text

    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")

    return changes


def patch_synth(
    dataset: str,
    impl: str,
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    dataset_dir = DATASETS_DIR / dataset
    synth_dir = dataset_dir / "synth" / impl

    mutations = load_mutations(dataset_dir)
    if not mutations:
        return {"error": f"No mutations.json in {dataset_dir}"}

    # Collect all Python/TS source files
    source_files = []
    for pattern in ["*.py", "**/*.py", "*.ts", "src/**/*.ts"]:
        for f in synth_dir.glob(pattern):
            if f.is_file() and f not in source_files:
                source_files.append(f)

    if not source_files:
        return {"error": f"No source files in {synth_dir}"}

    all_changes: dict[str, list[str]] = {}
    total_changes = 0

    for src in source_files:
        # Compute destination path: same relative path but in a _patched subdir
        rel = src.relative_to(synth_dir)
        # Write patched files alongside originals with _patched suffix on the synth dir name
        patched_dir = synth_dir.parent / (impl + "_patched")
        dst = patched_dir / rel

        changes = patch_file(src, dst, mutations, dry_run=dry_run)
        if changes:
            all_changes[str(rel)] = changes
            total_changes += len(changes)
            if verbose or dry_run:
                print(f"\n  {rel}:")
                for c in changes:
                    print(c)

    # Copy non-source files (grounding.json, requirements.txt, etc.) unchanged
    if not dry_run:
        patched_dir = synth_dir.parent / (impl + "_patched")
        for f in synth_dir.rglob("*"):
            if f.is_file() and f.suffix not in (".py", ".ts"):
                rel = f.relative_to(synth_dir)
                dst = patched_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(f.read_bytes())

    return {
        "dataset": dataset,
        "impl": impl,
        "patched_impl": impl + "_patched",
        "files_patched": len(all_changes),
        "total_replacements": total_changes,
        "changes": all_changes,
        "dry_run": dry_run,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Patch synthesized MCP server HTTP layer to restore original param names.",
        epilog=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("dataset", nargs="?", help="Dataset name (e.g. zulip, notion)")
    parser.add_argument("impl", nargs="?", help="Implementation directory name inside synth/")
    parser.add_argument("--all", action="store_true", dest="all_datasets",
                        help="Patch all datasets with mutations.json, latest mutated synth")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing files")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show individual changes per file")
    parser.add_argument("--json", action="store_true", dest="json_out")
    args = parser.parse_args()

    if args.all_datasets:
        results = []
        for dataset_dir in sorted(DATASETS_DIR.iterdir()):
            if not (dataset_dir / "mutations.json").exists():
                continue
            synth_dir = dataset_dir / "synth"
            if not synth_dir.exists():
                continue
            mutated_dirs = sorted(
                [d for d in synth_dir.iterdir() if d.is_dir() and "_mutated" in d.name],
                key=lambda d: d.name,
            )
            if not mutated_dirs:
                continue
            latest = mutated_dirs[-1]
            print(f"\nPatching {dataset_dir.name} / {latest.name} ...", flush=True)
            result = patch_synth(dataset_dir.name, latest.name, dry_run=args.dry_run, verbose=args.verbose)
            results.append(result)
            if "error" in result:
                print(f"  ERROR: {result['error']}")
            else:
                status = "[DRY RUN] " if args.dry_run else ""
                print(f"  {status}{result['files_patched']} files patched, {result['total_replacements']} replacements")
                if not args.dry_run:
                    print(f"  Output: synth/{result['patched_impl']}")

        if args.json_out:
            print(json.dumps(results, indent=2))
        return

    if not args.dataset or not args.impl:
        parser.error("Provide dataset and impl, or use --all")

    print(f"\nPatching {args.dataset} / {args.impl} ...", flush=True)
    result = patch_synth(args.dataset, args.impl, dry_run=args.dry_run, verbose=args.verbose)

    if args.json_out:
        print(json.dumps(result, indent=2))
        return

    if "error" in result:
        print(f"ERROR: {result['error']}")
        sys.exit(1)

    status = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{status}Results:")
    print(f"  Files patched:     {result['files_patched']}")
    print(f"  Total replacements:{result['total_replacements']}")
    if not args.dry_run:
        print(f"  Output dir:        synth/{result['patched_impl']}")

    for fpath, changes in result["changes"].items():
        print(f"\n  {fpath}:")
        for c in changes:
            print(c)


if __name__ == "__main__":
    main()
