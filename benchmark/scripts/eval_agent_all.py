#!/usr/bin/env python3
"""
Run agent evaluation across all (or selected) datasets and implementations.

For each dataset, finds synthesis output directories (dirs starting with "_")
and runs the agent harness (Gemini 2.5 Pro + LLM judge) against each one.
Results are written to benchmark/output/ as JSON and a markdown summary.

Usage:
    # Evaluate all datasets, auto-discover synthesis dirs for a model
    uv run python benchmark/scripts/eval_agent_all.py \\
        --model gcp-chat-completions-chat-gemini-2.5-pro-sandbox

    # Only specific datasets
    uv run python benchmark/scripts/eval_agent_all.py \\
        --datasets zulip openweathermap --model <synth-model>

    # Point at explicit impl dirs (one per dataset)
    uv run python benchmark/scripts/eval_agent_all.py \\
        --datasets zulip openweathermap \\
        --impl-dirs benchmark/datasets/zulip/_mydir \\
                    benchmark/datasets/openweathermap/_mydir

    # Only tasks with certain tags
    uv run python benchmark/scripts/eval_agent_all.py \\
        --model <synth-model> --tags read write

    # Use a different agent model
    uv run python benchmark/scripts/eval_agent_all.py \\
        --model <synth-model> --agent azure-chat-completions-gpt-4-1-2025-04-14-sandbox

    # Skip LLM judge (heuristic scoring only — faster)
    uv run python benchmark/scripts/eval_agent_all.py \\
        --model <synth-model> --no-judge

Environment:
    No extra vars needed for the agent itself — pychomsky uses eBay internal creds.
    Dataset-specific API credentials (e.g. ZULIP_API_KEY) must be set.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

_env_file = ROOT / ".env"
if _env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(_env_file)

import yaml

from benchmark.agent import AgentHarness, Task
from benchmark.agent.harness import DEFAULT_MODEL as DEFAULT_AGENT_MODEL

DATASETS_DIR = Path(__file__).parent.parent / "datasets"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

ALL_DATASETS = [
    "adyen",
    "ebay_buy",
    "ebay_commerce",
    "ebay_sell",
    "github",
    "google_sheets",
    "google_workspace",
    "hubspot",
    "jira",
    "notion",
    "openweathermap",
    "shopify",
    "slack",
    "stripe",
    "tiktok_shop",
    "twilio",
    "zendesk",
    "zulip",
]


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def find_impl_dir(dataset: str, synth_model: str) -> Path | None:
    """Find the most-recent synthesis output dir for (dataset, synth_model).

    Looks in datasets/<dataset>/synth/ for dirs whose name contains the model slug.
    """
    synth_dir = DATASETS_DIR / dataset / "synth"
    if not synth_dir.exists():
        return None
    slug = synth_model.split("/")[-1].replace(":", "-").replace(".", "-")
    candidates = sorted(
        (d for d in synth_dir.iterdir() if d.is_dir() and slug in d.name),
        key=lambda d: d.name,
    )
    return candidates[-1] if candidates else None


def load_tasks(dataset_dir: Path, tags: list[str] | None = None) -> list[Task]:
    tasks_file = dataset_dir / "tasks.yaml"
    if not tasks_file.exists():
        return []
    raw = yaml.safe_load(tasks_file.read_text())
    tasks = []
    for item in raw.get("tasks", []):
        task = Task(
            id=item["id"],
            prompt=item["prompt"],
            expected=item.get("expected"),
            tags=item.get("tags", []),
        )
        if tags and not any(t in task.tags for t in tags):
            continue
        tasks.append(task)
    return tasks


# ---------------------------------------------------------------------------
# Per-dataset evaluation
# ---------------------------------------------------------------------------

def evaluate_dataset(
    dataset: str,
    impl_dir: Path,
    harness: AgentHarness,
    tags: list[str] | None,
) -> dict:
    """Run the agent harness on all tasks for one dataset × impl."""
    dataset_dir = DATASETS_DIR / dataset
    tasks = load_tasks(dataset_dir, tags=tags)

    if not tasks:
        return {
            "dataset": dataset,
            "impl": impl_dir.name,
            "skipped": True,
            "skip_reason": "no tasks.yaml or no matching tasks",
            "passed": 0, "total": 0, "pass_rate": 0.0,
            "task_results": [],
        }

    task_results = []
    for i, task in enumerate(tasks, 1):
        print(f"  [{i}/{len(tasks)}] {task.id}: {task.prompt[:70].rstrip()}...", flush=True)
        t0 = time.time()
        result = harness.run_task(task, impl_dir)
        elapsed = time.time() - t0
        status = "PASS" if result.success else "FAIL"
        print(
            f"    {status}  turns={result.num_turns}  calls={result.num_tool_calls}"
            f"  errors={result.num_errors}  ({elapsed:.1f}s)",
            flush=True,
        )
        if result.error:
            print(f"    ERROR: {result.error}", flush=True)

        task_results.append({
            "id": task.id,
            "success": result.success,
            "num_turns": result.num_turns,
            "num_tool_calls": result.num_tool_calls,
            "num_errors": result.num_errors,
            "final_answer": result.final_answer[:500] if result.final_answer else "",
            "judge_reasoning": result.judge_reasoning,
            "harness_error": result.error,
        })

    passed = sum(1 for r in task_results if r["success"])
    total = len(task_results)
    return {
        "dataset": dataset,
        "impl": impl_dir.name,
        "skipped": False,
        "skip_reason": None,
        "passed": passed,
        "total": total,
        "pass_rate": round(passed / total, 4) if total else 0.0,
        "task_results": task_results,
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def write_markdown_report(
    results: list[dict],
    agent_model: str,
    synth_model: str | None,
    output_path: Path,
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Agent Evaluation Results",
        f"",
        f"Generated: {timestamp}",
        f"Agent model: `{agent_model}`",
    ]
    if synth_model:
        lines.append(f"Synthesis model: `{synth_model}`")
    lines += ["", "## Summary", ""]
    lines.append("| Dataset | Impl | Passed | Total | Pass% |")
    lines.append("|---------|------|--------|-------|-------|")

    total_passed = total_tasks = 0
    for r in results:
        if r.get("skipped"):
            lines.append(f"| {r['dataset']} | {r.get('impl', '?')} | — | — | SKIP |")
        else:
            pct = f"{100 * r['pass_rate']:.0f}%"
            lines.append(
                f"| {r['dataset']} | {r.get('impl', '?')} "
                f"| {r['passed']} | {r['total']} | {pct} |"
            )
            total_passed += r["passed"]
            total_tasks += r["total"]

    if total_tasks:
        overall_pct = f"{100 * total_passed / total_tasks:.1f}%"
        lines += [
            "",
            f"**Overall: {total_passed}/{total_tasks} ({overall_pct})**",
        ]

    lines += ["", "## Per-Dataset Task Breakdown", ""]
    for r in results:
        if r.get("skipped"):
            continue
        lines.append(f"### {r['dataset']} (`{r.get('impl', '?')}`)")
        lines.append("")
        lines.append("| Task | Pass | Turns | Tool Calls | Errors |")
        lines.append("|------|------|-------|------------|--------|")
        for t in r.get("task_results", []):
            status = "✓" if t["success"] else "✗"
            lines.append(
                f"| {t['id']} | {status} | {t['num_turns']}"
                f" | {t['num_tool_calls']} | {t['num_errors']} |"
            )
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run agent evaluation across all datasets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--model",
        help="Synthesis model slug used to auto-discover impl dirs",
    )
    parser.add_argument(
        "--agent",
        default=DEFAULT_AGENT_MODEL,
        help=f"Agent model (default: {DEFAULT_AGENT_MODEL})",
    )
    parser.add_argument(
        "--judge",
        default=DEFAULT_AGENT_MODEL,
        help="Judge model (default: same as --agent)",
    )
    parser.add_argument(
        "--no-judge", action="store_true",
        help="Skip LLM judge; heuristic scoring only",
    )
    parser.add_argument(
        "--datasets", nargs="+", default=ALL_DATASETS,
        help="Datasets to evaluate (default: all)",
    )
    parser.add_argument(
        "--impl-dirs", nargs="+", metavar="DIR",
        help="Explicit impl dirs, one per dataset (in the same order as --datasets)",
    )
    parser.add_argument(
        "--tags", nargs="+",
        help="Only run tasks with these tags",
    )
    parser.add_argument(
        "--max-turns", type=int, default=15,
        help="Max agent turns per task (default: 15)",
    )
    parser.add_argument(
        "--output-dir", default=str(OUTPUT_DIR),
        help="Directory for output files (default: benchmark/output/)",
    )
    parser.add_argument(
        "--output-name",
        help="Base name for output files (default: agent_eval_<timestamp>)",
    )
    args = parser.parse_args()

    if not args.model and not args.impl_dirs:
        parser.error("Provide --model (to auto-discover impl dirs) or --impl-dirs.")

    if args.impl_dirs and len(args.impl_dirs) != len(args.datasets):
        parser.error(
            f"--impl-dirs must have the same number of entries as --datasets "
            f"({len(args.datasets)} datasets, {len(args.impl_dirs)} dirs given)"
        )

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    base_name = args.output_name or f"agent_eval_{timestamp}"
    json_path = out_dir / f"{base_name}.json"
    md_path = out_dir / f"{base_name}.md"

    judge_model = None if args.no_judge else args.judge
    harness = AgentHarness(
        model=args.agent,
        max_turns=args.max_turns,
        judge_model=judge_model,
    )

    print(f"Agent model:  {args.agent}")
    print(f"Judge model:  {judge_model or 'none (heuristic)'}")
    print(f"Synth model:  {args.model or '(explicit dirs)'}")
    print(f"Datasets:     {len(args.datasets)}")
    print(f"Output:       {out_dir}")
    print()

    all_results = []
    start_all = time.time()

    for idx, dataset in enumerate(args.datasets):
        dataset_dir = DATASETS_DIR / dataset
        if not dataset_dir.exists():
            print(f"[SKIP] Unknown dataset: {dataset}")
            continue

        # Resolve impl dir
        if args.impl_dirs:
            impl_dir = Path(args.impl_dirs[idx])
        else:
            impl_dir = find_impl_dir(dataset, args.model)

        print(f"{'='*60}")
        if impl_dir is None:
            print(f"[SKIP] {dataset}: no impl dir found for model '{args.model}'")
            all_results.append({
                "dataset": dataset, "impl": None, "skipped": True,
                "skip_reason": f"no impl dir for {args.model}",
                "passed": 0, "total": 0, "pass_rate": 0.0, "task_results": [],
            })
            continue

        if not impl_dir.exists():
            print(f"[SKIP] {dataset}: impl dir does not exist: {impl_dir}")
            all_results.append({
                "dataset": dataset, "impl": str(impl_dir), "skipped": True,
                "skip_reason": "impl dir not found",
                "passed": 0, "total": 0, "pass_rate": 0.0, "task_results": [],
            })
            continue

        print(f"Dataset: {dataset}  |  impl: {impl_dir.name}", flush=True)
        print()

        result = evaluate_dataset(dataset, impl_dir, harness, tags=args.tags)
        all_results.append(result)

        pct = f"{100*result['pass_rate']:.0f}%" if not result["skipped"] else "SKIP"
        print(f"  => {result.get('passed', 0)}/{result.get('total', 0)} ({pct})")
        print()

        # Write intermediate results after each dataset
        json_path.write_text(json.dumps({
            "agent_model": args.agent,
            "judge_model": judge_model,
            "synth_model": args.model,
            "timestamp": timestamp,
            "results": all_results,
        }, indent=2, ensure_ascii=False))

    elapsed = time.time() - start_all

    # Final JSON
    output_data = {
        "agent_model": args.agent,
        "judge_model": judge_model,
        "synth_model": args.model,
        "timestamp": timestamp,
        "total_elapsed_s": round(elapsed, 1),
        "results": all_results,
    }
    json_path.write_text(json.dumps(output_data, indent=2, ensure_ascii=False))

    # Markdown report
    write_markdown_report(all_results, args.agent, args.model, md_path)

    # Final summary
    non_skipped = [r for r in all_results if not r.get("skipped")]
    total_passed = sum(r["passed"] for r in non_skipped)
    total_tasks = sum(r["total"] for r in non_skipped)
    overall_pct = f"{100*total_passed/total_tasks:.1f}%" if total_tasks else "n/a"

    print("=" * 60)
    print(f"Overall:  {total_passed}/{total_tasks} ({overall_pct})")
    print(f"Time:     {elapsed:.1f}s")
    print(f"JSON:     {json_path}")
    print(f"Report:   {md_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
