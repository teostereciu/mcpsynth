#!/usr/bin/env python3
"""
Run agent-based evaluation on a synthesized MCP server or CLI tool.

The agent (Gemini 2.5 Pro or Azure GPT-4.1) is given natural-language tasks
defined in tasks.yaml, uses the server/CLI tools to complete them, and an
LLM judge scores each result.

Usage:
    # Evaluate an MCP server (default mode)
    uv run python benchmark/scripts/eval_agent.py zulip claude-sonnet-4-5-20251101_20260415_1234

    # Evaluate a synthesized CLI tool
    uv run python benchmark/scripts/eval_agent.py zulip_cli my_synth_dir --mode cli

    # Evaluate with a different agent model
    uv run python benchmark/scripts/eval_agent.py zulip _synth_... \\
        --model azure-chat-completions-gpt-4-1-2025-04-14-sandbox

    # Skip LLM judge (faster, heuristic-only)
    uv run python benchmark/scripts/eval_agent.py zulip _synth_... --no-judge

    # Limit to specific task tags
    uv run python benchmark/scripts/eval_agent.py zulip _synth_... --tags read write

    # Output results as JSON
    uv run python benchmark/scripts/eval_agent.py zulip _synth_... --json

Environment:
    No extra env vars needed — pychomsky picks up eBay internal credentials.
    Dataset-specific API credentials must be set (e.g. ZULIP_API_KEY).
"""

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

_env_file = ROOT / ".env"
if _env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(_env_file)

from benchmark.agent import AgentHarness, Task
from benchmark.agent.harness import DEFAULT_MODEL, SECONDARY_MODEL, DEFAULT_JUDGE_MODEL


DATASETS_DIR = Path(__file__).parent.parent / "datasets"


def load_tasks(dataset_dir: Path, tags: list[str] | None = None) -> list[Task]:
    """Load tasks from tasks.yaml in the dataset directory.

    Substitutes environment variables in prompt and expected fields so agents
    see concrete values (e.g. 'teostereciu/test-synth-mcp') rather than
    placeholder names (e.g. 'GITHUB_TEST_REPO').
    """
    import os
    import yaml

    tasks_file = dataset_dir / "tasks.yaml"
    if not tasks_file.exists():
        print(f"Error: no tasks.yaml found at {tasks_file}")
        sys.exit(1)

    raw = yaml.safe_load(tasks_file.read_text())
    tasks = []
    for item in raw.get("tasks", []):
        from string import Template
        prompt = Template(item["prompt"]).safe_substitute(os.environ)
        expected = Template(item["expected"]).safe_substitute(os.environ) if item.get("expected") else None
        task = Task(
            id=item["id"],
            prompt=prompt,
            expected=expected,
            tags=item.get("tags", []),
        )
        if tags:
            if not any(t in task.tags for t in tags):
                continue
        tasks.append(task)
    return tasks


def find_impl_dir(dataset_dir: Path, impl_name: str) -> Path:
    """Resolve the implementation directory.

    Checks synth/<impl_name> first, then <impl_name> directly.
    """
    for candidate in [dataset_dir / "synth" / impl_name, dataset_dir / impl_name]:
        if candidate.exists():
            return candidate
    print(f"Error: implementation directory not found: {dataset_dir / 'synth' / impl_name}")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Run agent evaluation on an MCP server implementation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("dataset", help="Dataset name (e.g. zulip, stripe)")
    parser.add_argument("impl", help="Implementation directory name inside the dataset folder")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Agent model (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--judge-model",
        default=DEFAULT_JUDGE_MODEL,
        help=f"Judge model (default: {DEFAULT_JUDGE_MODEL})",
    )
    parser.add_argument(
        "--no-judge",
        action="store_true",
        help="Skip LLM judge; use heuristic success detection only",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=15,
        help="Max agent turns per task (default: 15)",
    )
    parser.add_argument(
        "--tags",
        nargs="+",
        help="Only run tasks with these tags",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON",
    )
    parser.add_argument(
        "--output",
        help="Write JSON results to this file (implies --json)",
    )
    parser.add_argument(
        "--mode",
        choices=["mcp", "cli"],
        default="mcp",
        help="Evaluation mode: 'mcp' for MCP server (default), 'cli' for synthesized CLI tool",
    )
    args = parser.parse_args()

    dataset_dir = DATASETS_DIR / args.dataset
    if not dataset_dir.exists():
        print(f"Error: dataset not found: {dataset_dir}")
        sys.exit(1)

    impl_dir = find_impl_dir(dataset_dir, args.impl)
    tasks = load_tasks(dataset_dir, tags=args.tags)

    if not tasks:
        print("No tasks found (check tasks.yaml and --tags filter).")
        sys.exit(0)

    judge_model = None if args.no_judge else args.judge_model
    harness = AgentHarness(
        model=args.model,
        max_turns=args.max_turns,
        judge_model=judge_model,
        mode=args.mode,
    )

    print(f"Dataset:  {args.dataset}")
    print(f"Impl:     {impl_dir}")
    print(f"Mode:     {args.mode}")
    print(f"Model:    {args.model}")
    print(f"Judge:    {judge_model or 'none (heuristic)'}")
    print(f"Tasks:    {len(tasks)}")
    print()

    results = []
    start_all = time.time()

    for i, task in enumerate(tasks, 1):
        print(f"[{i}/{len(tasks)}] {task.id}: {task.prompt[:80]}...", flush=True)
        task_start = time.time()
        result = harness.run_task(task, impl_dir)
        elapsed = time.time() - task_start

        verdict = result.verdict  # "pass" / "fail" / "undefined"
        status = {"pass": "PASS", "fail": "FAIL", "undefined": "UNDEF"}[verdict]
        reliable_tag = "" if result.judge_reliable else "  [HEURISTIC]"
        print(
            f"  {status}  turns={result.num_turns}  calls={result.num_tool_calls}"
            f"  errors={result.num_errors}{reliable_tag}  ({elapsed:.1f}s)",
            flush=True,
        )
        if result.error:
            print(f"  ERROR: {result.error}", flush=True)
        if result.judge_reasoning:
            reason = f"  [{result.failure_reason}]" if result.failure_reason else ""
            print(f"  Judge: {result.judge_reasoning}{reason}", flush=True)
        print()

        results.append(result)

    total_elapsed = time.time() - start_all
    total = len(results)
    n_pass = sum(1 for r in results if r.verdict == "pass")
    n_fail = sum(1 for r in results if r.verdict == "fail")
    n_undef = sum(1 for r in results if r.verdict == "undefined")
    scoreable = [r for r in results if r.verdict != "undefined"]
    pass_rate = n_pass / len(scoreable) if scoreable else 0.0

    # Synthesis quality: SERVER_SUFFICIENT from judge (Option A rubric).
    # Excludes tasks where server_sufficient is None (ENVIRONMENT, TASK_AMBIGUOUS, judge unreliable).
    n_sufficient = sum(1 for r in results if r.server_sufficient is True)
    n_insufficient = sum(1 for r in results if r.server_sufficient is False)
    n_suff_unknown = sum(1 for r in results if r.server_sufficient is None)
    synthesis_assessable = n_sufficient + n_insufficient
    synthesis_pass_rate = n_sufficient / synthesis_assessable if synthesis_assessable else 0.0

    heuristic_count = sum(1 for r in results if not r.judge_reliable)

    # Breakdown by failure reason for fails and undefineds
    fail_reasons: dict[str, int] = {}
    for r in results:
        if r.failure_reason and r.failure_reason != "NONE":
            fail_reasons[r.failure_reason] = fail_reasons.get(r.failure_reason, 0) + 1

    print("=" * 50)
    print(f"Results:  {n_pass} pass  {n_fail} fail  {n_undef} undefined  (total {total})")
    print(f"Pass rate (scoreable):  {n_pass}/{len(scoreable)} ({100*pass_rate:.0f}%)")
    if synthesis_assessable:
        print(f"Synthesis pass rate:    {n_sufficient}/{synthesis_assessable} ({100*synthesis_pass_rate:.0f}%)  [SERVER_SUFFICIENT]")
    if fail_reasons:
        reasons_str = "  ".join(f"{k}={v}" for k, v in sorted(fail_reasons.items()))
        print(f"Failure reasons:  {reasons_str}")
    if heuristic_count:
        print(f"Warning:  {heuristic_count} task(s) used heuristic fallback (judge unreliable)")
    print(f"Time:     {total_elapsed:.1f}s")
    print("=" * 50)

    if args.json_output or args.output:
        output_data = {
            "dataset": args.dataset,
            "impl": args.impl,
            "mode": args.mode,
            "model": args.model,
            "judge_model": judge_model,
            "summary": {
                "total": total,
                "pass": n_pass,
                "fail": n_fail,
                "undefined": n_undef,
                "scoreable": len(scoreable),
                "pass_rate": round(pass_rate, 4),
                "synthesis_pass_rate": round(synthesis_pass_rate, 4) if synthesis_assessable else None,
                "n_server_sufficient": n_sufficient,
                "n_server_insufficient": n_insufficient,
                "n_server_sufficient_unknown": n_suff_unknown,
                "failure_reasons": fail_reasons,
            },
            "tasks": [
                {
                    "id": r.task_id,
                    "verdict": r.verdict,
                    "success": r.success,
                    "failure_reason": r.failure_reason,
                    "server_sufficient": r.server_sufficient,
                    "judge_reliable": r.judge_reliable,
                    "num_turns": r.num_turns,
                    "num_tool_calls": r.num_tool_calls,
                    "num_errors": r.num_errors,
                    "final_answer": r.final_answer,
                    "judge_reasoning": r.judge_reasoning,
                    "error": r.error,
                    "tool_calls": [
                        {
                            "name": tc.name,
                            "arguments": tc.arguments,
                            "result": tc.result,
                            "error": tc.error,
                        }
                        for tc in r.tool_calls
                    ],
                }
                for r in results
            ],
        }

        if args.output:
            out_path = Path(args.output)
            out_path.write_text(json.dumps(output_data, indent=2, ensure_ascii=False))
            print(f"\nResults written to {out_path}")
        else:
            print(json.dumps(output_data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
