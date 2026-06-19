#!/usr/bin/env python3
"""
Run synthesis on a benchmark dataset using the Agent SDK.

The agent reads TASK.md and docs/, then writes all deliverables
(server.py, requirements.txt or package.json, and tool implementation files)
to an output directory inside the dataset folder.

Usage:
    # Synthesize Zulip with default Claude model (direct Anthropic API)
    uv run python benchmark/scripts/synthesize.py zulip

    # Specify output directory name (default: synth/<model-slug>_<timestamp>)
    uv run python benchmark/scripts/synthesize.py zulip --output demo_apr_3

    # Use a different model
    uv run python benchmark/scripts/synthesize.py zulip --model claude-opus-4-5-20251101

    # Route through OpenRouter (any model OpenRouter supports)
    uv run python benchmark/scripts/synthesize.py zulip \\
        --model google/gemini-2.5-pro --openrouter

    uv run python benchmark/scripts/synthesize.py stripe \\
        --model anthropic/claude-sonnet-4-5 --openrouter

    # List available datasets
    uv run python benchmark/scripts/synthesize.py --list

Environment:
    ANTHROPIC_API_KEY   Required for direct Anthropic usage
    OPENROUTER_API_KEY  Required when --openrouter is set
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Allow running from project root or benchmark/
ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

# Load .env from project root if present (before any other imports that read env vars)
_env_file = ROOT / ".env"
if _env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(_env_file)

from benchmark.synthesizers import Document


DATASETS_DIR = Path(__file__).parent.parent / "datasets"

# Directories inside a dataset that are not output targets
INPUT_DIRS = {"docs", "source", "tests"}
SKIP_PREFIXES = {"[archive]", "[deprecated]"}


def find_datasets() -> dict[str, Path]:
    datasets = {}
    for d in sorted(DATASETS_DIR.iterdir()):
        if not d.is_dir():
            continue
        if any(d.name.startswith(p) for p in SKIP_PREFIXES):
            continue
        if (d / "TASK.md").exists():
            datasets[d.name] = d
    return datasets


def list_datasets():
    datasets = find_datasets()
    print("Available datasets:\n")
    for name, path in datasets.items():
        docs_dir = path / "docs"
        ndocs = len(list(docs_dir.glob("*.md"))) if docs_dir.exists() else 0
        print(f"  {name:25s}  {ndocs} docs")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize an MCP server from a benchmark dataset.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("dataset", nargs="?", help="Dataset name (e.g. zulip, stripe, github)")
    parser.add_argument("--list", action="store_true", help="List available datasets and exit")
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-5-20251101",
        help="Model ID (default: claude-sonnet-4-5-20251101)",
    )
    parser.add_argument(
        "--openrouter",
        action="store_true",
        help="Route through OpenRouter (requires OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--vllm",
        action="store_true",
        help="Route through a self-hosted vLLM server (OpenAI-compatible API)",
    )
    parser.add_argument(
        "--vllm-url",
        default="http://localhost:8000/v1",
        metavar="URL",
        help="Base URL of the vLLM server (default: http://localhost:8000/v1)",
    )
    parser.add_argument(
        "--bash",
        action="store_true",
        help="Enable bash tool in advanced mode (default: off)",
    )
    parser.add_argument(
        "--thinking-level",
        choices=["low", "medium", "high"],
        help="Gemini reasoning level (advanced mode only)",
    )
    parser.add_argument(
        "--thinking-budget",
        type=int,
        help="Gemini thinking budget in tokens (advanced mode only; 0 = disable)",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=50,
        help="Max agent turns (default: 50; advanced default: 100)",
    )
    parser.add_argument(
        "--no-docs",
        action="store_true",
        help="Run synthesis without providing any API docs (zero-knowledge condition)",
    )
    parser.add_argument(
        "--docs",
        action="store_true",
        help="Force docs-based synthesis (default; use --source to opt into source-tree condition)",
    )
    parser.add_argument(
        "--source",
        action="store_true",
        help="Use source/ directory instead of docs/ (open-source API condition)",
    )
    parser.add_argument(
        "--mutated",
        action="store_true",
        help="Use docs_mutated/ instead of docs/ (run mutate_docs.py first)",
    )
    parser.add_argument(
        "--task",
        default="TASK.md",
        help="Task file to use relative to the dataset directory (default: TASK.md)",
    )
    parser.add_argument(
        "--output",
        help="Output directory name inside the dataset folder (default: _synth_<model-slug>)",
    )
    args = parser.parse_args()

    # Model aliases — short names for common OpenRouter model IDs
    MODEL_ALIASES: dict[str, str] = {
        "sonnet": "anthropic/claude-sonnet-4-5",
        "haiku":  "anthropic/claude-haiku-4-5",
        "opus":   "anthropic/claude-opus-4-5",
        "gemini25": "google/gemini-2.5-pro",
        "gemini25flash": "google/gemini-2.5-flash",
    }
    args.model = MODEL_ALIASES.get(args.model.lower(), args.model)

    if args.list:
        list_datasets()
        return

    if not args.dataset:
        parser.print_help()
        sys.exit(1)

    datasets = find_datasets()
    if args.dataset not in datasets:
        print(f"Error: unknown dataset '{args.dataset}'")
        print(f"Run with --list to see available datasets.")
        sys.exit(1)

    dataset_dir = datasets[args.dataset]

    # Detect source/docs availability early (needed for task file selection and output naming)
    source_dir = dataset_dir / "source"
    docs_dir = dataset_dir / ("docs_mutated" if args.mutated else "docs")
    has_source = source_dir.exists() and any(source_dir.iterdir())
    has_docs = docs_dir.exists() and any(docs_dir.glob("*.md"))

    # Auto-select TASK_source.md when using source condition and no explicit --task given
    task_filename = args.task
    if (
        args.task == "TASK.md"
        and args.source
        and has_source
        and not args.no_docs
        and not args.mutated
        and (dataset_dir / "TASK_source.md").exists()
    ):
        task_filename = "TASK_source.md"

    task_file = dataset_dir / task_filename
    if not task_file.exists():
        print(f"Error: task file not found: {task_file}")
        sys.exit(1)
    task_prompt = task_file.read_text()

    # Resolve output directory
    model_slug = args.model.split("/")[-1]  # "minimax-m2.5:free" from "minimax/minimax-m2.5:free"
    model_slug = model_slug.replace(":", "-").replace(".", "-")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    if args.output:
        # If the caller gives an explicit name, put it under synth/ unless it's
        # an absolute path or already contains a directory separator.
        output_name = args.output
        if "/" in output_name or output_name.startswith(os.sep):
            output_dir = Path(output_name)
        else:
            output_dir = dataset_dir / "synth" / output_name
    else:
        suffix = "_nodocs" if args.no_docs else ("_mutated" if args.mutated else ("_docs" if args.docs else ""))
        if task_filename != "TASK.md":
            task_slug = Path(task_filename).stem.lower().replace("task_", "").replace("task", "")
            if task_slug:
                suffix += f"_{task_slug}"
        output_dir = dataset_dir / "synth" / f"{model_slug}_{timestamp}{suffix}"

    if output_dir.exists():
        print(f"Output directory already exists: {output_dir}")
        answer = input("Overwrite? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)

    if args.no_docs:
        api_docs = []
        source_dir_for_synth = None
        task_prompt = (
            "NOTE: No API documentation is available for this task — the docs/ directory is empty. "
            "Ignore any references to documentation files in the task below. "
            "Use your general knowledge of the API to implement as many tools as you can.\n\n"
        ) + task_prompt
        print("Input:      none (--no-docs)")
    elif args.source and has_source and not args.mutated:
        # Source-tree condition (opt-in via --source): pass source/ as a directory symlink.
        # Do not load into memory — the agent will navigate the tree with glob/grep/read.
        api_docs = []
        source_dir_for_synth = source_dir
        print(f"Input:      source/ (source tree at {source_dir})")
    else:
        source_dir_for_synth = None
        if not has_docs:
            print(f"Error: no docs found in {docs_dir} and no source/ directory present")
            sys.exit(1)
        print("Loading docs...", end=" ", flush=True)
        api_docs = [Document.from_file(f) for f in sorted(docs_dir.glob("*.md"))]
        print(f"{len(api_docs)} docs loaded")

    print()
    ndocs_display = f"{len(api_docs)} docs" if api_docs else ("source tree" if has_source else "no docs")
    print(f"Dataset:    {args.dataset}  ({ndocs_display})")
    if args.vllm:
        backend = f"  [vLLM @ {args.vllm_url}]"
    elif args.openrouter:
        backend = "  [OpenRouter]"
    else:
        backend = ""
    print(f"Model:      {args.model}{backend}")
    print(f"Max turns:  {args.max_turns}")
    print(f"Output:     {output_dir}")
    print()
    print("Starting agent...", flush=True)

    if args.vllm:
        from benchmark.synthesizers.agentic_vllm import AgenticVLLM
        synth = AgenticVLLM(
            model=args.model,
            base_url=args.vllm_url,
            max_turns=args.max_turns,
            enable_bash=args.bash,
        )
    elif args.openrouter:
        from benchmark.synthesizers.agentic_openrouter_raw import AgenticOpenRouterRaw
        synth = AgenticOpenRouterRaw(model=args.model, max_turns=args.max_turns, enable_bash=args.bash)
    else:
        from benchmark.synthesizers.agentic_openrouter import AgenticOpenRouter
        synth = AgenticOpenRouter(model=args.model, max_turns=args.max_turns, enable_bash=args.bash)

    result = synth.synthesize(task_prompt, api_docs, source_dir=source_dir_for_synth)

    # Write output files
    output_dir.mkdir(parents=True, exist_ok=True)
    files = result.metadata.get("multi_file_structure", {})
    for rel_path, content in files.items():
        out = output_dir / rel_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")

    # Persist synthesis metadata
    condition = "nodocs" if args.no_docs else ("mutated" if args.mutated else "docs")
    meta = {
        "dataset": args.dataset,
        "model": args.model,
        "condition": condition,
        "synthesis_time": result.synthesis_time,
        "token_usage": result.token_usage,
        "cost_estimate": result.cost_estimate,
        "timestamp": timestamp,
    }
    (output_dir / "synthesis_meta.json").write_text(json.dumps(meta, indent=2))

    # Summary
    print()
    print("=" * 50)
    print(f"Output:  {output_dir}")
    if files:
        print(f"Files:   {', '.join(files.keys())}")
    else:
        print("Files:   NONE — synthesis produced no output files")
    if result.token_usage:
        u = result.token_usage
        print(f"Tokens:  {u.get('input_tokens', 0):,} in / {u.get('output_tokens', 0):,} out", end="")
        cache_read = u.get("cache_read_input_tokens", 0)
        if cache_read:
            print(f"  ({cache_read:,} cache read)", end="")
        print()
    if result.cost_estimate is not None:
        print(f"Cost:    ${result.cost_estimate:.4f}")
    if result.synthesis_time:
        print(f"Time:    {result.synthesis_time:.1f}s")
    print("=" * 50)

    if not files:
        print("ERROR: synthesis failed — no files written. Check logs above for stream errors.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
