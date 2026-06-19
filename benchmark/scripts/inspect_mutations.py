#!/usr/bin/env python3
"""
Measure mutation adherence for a synthesized MCP server.

For each mutation pair (original → mutated), checks whether the synthesized
server adopted the mutated parameter name (doc-grounded) or the original name
(parametric knowledge).

Detection strategy: search all synthesized .py/.ts files for the mutated name
as a quoted string key (e.g. "filter_spec"), which indicates use in an HTTP
request dict. Also reports presence as a Python/TS identifier (function param
or variable) to distinguish interface adoption from HTTP-layer adoption.

Usage:
    uv run python benchmark/scripts/inspect_mutations.py zulip azure-..._mutated
    uv run python benchmark/scripts/inspect_mutations.py github azure-..._mutated --json
    uv run python benchmark/scripts/inspect_mutations.py --all   # all datasets with mutations.json
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


def collect_source_files(synth_dir: Path) -> list[Path]:
    """Collect all synthesized source files (.py, .ts)."""
    files = []
    for pattern in ["*.py", "**/*.py", "*.ts", "src/**/*.ts"]:
        for f in synth_dir.glob(pattern):
            if f.is_file() and f not in files:
                files.append(f)
    return files


def check_mutation_adoption(
    name: str,
    source_files: list[Path],
) -> dict:
    """
    Check whether `name` appears in the source files as:
    - a quoted string key (HTTP layer): "name" or 'name'
    - a Python/TS identifier (tool interface): as a bare word in function params
    """
    # Quoted string key pattern: "name" or 'name' not followed by : (to avoid docstrings)
    # We want dict keys like {"filter_spec": val} or params["filter_spec"]
    quoted_pattern = re.compile(
        r'(?:\"' + re.escape(name) + r'\"|\''+  re.escape(name) + r'\')',
    )
    # Identifier pattern: word boundary around name (function param, variable)
    identifier_pattern = re.compile(r'\b' + re.escape(name) + r'\b')

    quoted_hits: list[str] = []   # (file, line_no, line)
    identifier_hits: list[str] = []

    for fpath in source_files:
        try:
            text = fpath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            # Skip comments and docstrings
            if stripped.startswith("#") or stripped.startswith('"""') or stripped.startswith("'''"):
                continue
            if quoted_pattern.search(line):
                quoted_hits.append(f"{fpath.name}:{i}: {stripped[:120]}")
            elif identifier_pattern.search(line):
                identifier_hits.append(f"{fpath.name}:{i}: {stripped[:120]}")

    return {
        "quoted_hits": quoted_hits,      # strong signal: in HTTP dict keys
        "identifier_hits": identifier_hits,  # weaker signal: in identifiers/params
        "adopted_http": len(quoted_hits) > 0,
        "adopted_interface": len(identifier_hits) > 0,
    }


def inspect_synth(dataset: str, impl: str, verbose: bool = False) -> dict:
    dataset_dir = DATASETS_DIR / dataset
    synth_dir = dataset_dir / "synth" / impl

    mutations = load_mutations(dataset_dir)
    if not mutations:
        return {"error": f"No mutations.json found in {dataset_dir}"}

    source_files = collect_source_files(synth_dir)
    if not source_files:
        return {"error": f"No source files found in {synth_dir}"}

    results = []
    for m in mutations:
        original = m["original"]
        mutated = m["mutated"]

        mutated_info = check_mutation_adoption(mutated, source_files)
        original_info = check_mutation_adoption(original, source_files)

        adopted = mutated_info["adopted_http"] or mutated_info["adopted_interface"]
        # If both appear, it's ambiguous — synthesizer may have aliased or partially adopted
        both = (mutated_info["adopted_http"] or mutated_info["adopted_interface"]) and \
               (original_info["adopted_http"] or original_info["adopted_interface"])

        results.append({
            "original": original,
            "mutated": mutated,
            "adopted": adopted,
            "adopted_http": mutated_info["adopted_http"],
            "adopted_interface": mutated_info["adopted_interface"],
            "original_still_present": original_info["adopted_http"] or original_info["adopted_interface"],
            "both_present": both,
            "mutated_http_hits": mutated_info["quoted_hits"] if verbose else len(mutated_info["quoted_hits"]),
            "mutated_id_hits": mutated_info["identifier_hits"] if verbose else len(mutated_info["identifier_hits"]),
            "original_http_hits": original_info["quoted_hits"] if verbose else len(original_info["quoted_hits"]),
            "original_id_hits": original_info["identifier_hits"] if verbose else len(original_info["identifier_hits"]),
        })

    n_adopted = sum(1 for r in results if r["adopted"])
    n_http = sum(1 for r in results if r["adopted_http"])
    adherence_rate = n_adopted / len(results) if results else 0.0
    http_adherence_rate = n_http / len(results) if results else 0.0

    return {
        "dataset": dataset,
        "impl": impl,
        "n_mutations": len(mutations),
        "n_adopted": n_adopted,
        "n_adopted_http": n_http,
        "adherence_rate": round(adherence_rate, 3),
        "http_adherence_rate": round(http_adherence_rate, 3),
        "mutations": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure mutation adherence for a synthesized MCP server.",
        epilog=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("dataset", nargs="?", help="Dataset name (e.g. zulip, github)")
    parser.add_argument("impl", nargs="?", help="Implementation directory name inside synth/")
    parser.add_argument("--all", action="store_true", dest="all_datasets",
                        help="Inspect all datasets that have mutations.json, latest mutated synth")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output raw JSON")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show individual hit lines")
    args = parser.parse_args()

    if args.all_datasets:
        all_results = []
        for dataset_dir in sorted(DATASETS_DIR.iterdir()):
            if not (dataset_dir / "mutations.json").exists():
                continue
            synth_dir = dataset_dir / "synth"
            if not synth_dir.exists():
                continue
            # Find latest mutated synth dir (exclude _patched copies)
            mutated_dirs = sorted(
                [d for d in synth_dir.iterdir()
                 if d.is_dir() and "_mutated" in d.name and not d.name.endswith("_patched")],
                key=lambda d: d.name,
            )
            if not mutated_dirs:
                print(f"  {dataset_dir.name}: no mutated synth found", file=sys.stderr)
                continue
            latest = mutated_dirs[-1]
            result = inspect_synth(dataset_dir.name, latest.name, verbose=args.verbose)
            all_results.append(result)

        if args.json_out:
            print(json.dumps(all_results, indent=2))
        else:
            print(f"\n{'Dataset':<15} {'Mutations':<12} {'Adopted':<10} {'HTTP adopted':<14} {'Adherence':>10}  {'HTTP adherence':>14}")
            print("-" * 80)
            for r in all_results:
                if "error" in r:
                    print(f"{r.get('dataset','?'):<15}  ERROR: {r['error']}")
                    continue
                print(
                    f"{r['dataset']:<15} {r['n_mutations']:<12} {r['n_adopted']:<10} "
                    f"{r['n_adopted_http']:<14} {r['adherence_rate']:>9.0%}  {r['http_adherence_rate']:>13.0%}"
                )
            print()
            for r in all_results:
                if "error" in r:
                    continue
                print(f"\n{r['dataset']} ({r['impl']}):")
                for m in r["mutations"]:
                    status = "✓" if m["adopted"] else "✗"
                    http = " [HTTP]" if m["adopted_http"] else ""
                    iface = " [iface]" if m["adopted_interface"] and not m["adopted_http"] else ""
                    both = " [BOTH-PRESENT]" if m["both_present"] else ""
                    print(f"  {status} {m['original']:20s} → {m['mutated']:25s}{http}{iface}{both}")
        return

    if not args.dataset or not args.impl:
        parser.error("Provide dataset and impl, or use --all")

    result = inspect_synth(args.dataset, args.impl, verbose=args.verbose)

    if args.json_out:
        print(json.dumps(result, indent=2))
        return

    if "error" in result:
        print(f"ERROR: {result['error']}")
        sys.exit(1)

    print(f"\nDataset:   {result['dataset']}")
    print(f"Impl:      {result['impl']}")
    print(f"Adherence: {result['n_adopted']}/{result['n_mutations']} mutations adopted  ({result['adherence_rate']:.0%})")
    print(f"HTTP layer:{result['n_adopted_http']}/{result['n_mutations']} adopted in HTTP dict keys  ({result['http_adherence_rate']:.0%})")
    print()
    print(f"{'':3} {'original':20s}  {'mutated':25s}  {'HTTP':5}  {'iface':6}  {'orig still?':11}")
    print("-" * 80)
    for m in result["mutations"]:
        http = "yes" if m["adopted_http"] else "no"
        iface = "yes" if m["adopted_interface"] else "no"
        orig = "YES" if m["original_still_present"] else "no"
        status = "✓" if m["adopted"] else "✗"
        print(f"{status}  {m['original']:20s}  {m['mutated']:25s}  {http:5}  {iface:6}  {orig}")
        if args.verbose and m.get("mutated_http_hits"):
            for hit in (m["mutated_http_hits"] or [])[:3]:
                print(f"     HTTP: {hit}")
        if args.verbose and m.get("mutated_id_hits"):
            for hit in (m["mutated_id_hits"] or [])[:3]:
                print(f"     IFACE:{hit}")


if __name__ == "__main__":
    main()
