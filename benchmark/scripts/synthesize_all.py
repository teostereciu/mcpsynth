#!/usr/bin/env python3
"""
Synthesize all (or selected) datasets with a single command.

Usage:
    # Synthesize all datasets
    uv run python benchmark/scripts/synthesize_all.py

    # Only specific datasets
    uv run python benchmark/scripts/synthesize_all.py --datasets jira zendesk twilio

    # Override the model
    uv run python benchmark/scripts/synthesize_all.py \\
        --model azure-chat-completions-gpt-5-2-2025-12-11-sandbox

Default model: azure-chat-completions-gpt-5-2-2025-12-11-sandbox
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
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

DATASETS_DIR = Path(__file__).parent.parent / "datasets"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

DEFAULT_MODEL = "azure-chat-completions-gpt-5-2-2025-12-11-sandbox"

ALL_DATASETS = [
    "adyen",
    "ebay_buy",
    "ebay_commerce",
    "ebay_sell",
    "github",
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


def run_synthesis(model: str, dataset: str, output_dir: Path, no_docs: bool = False, mutated: bool = False) -> dict:
    """Synthesize using synthesize.py."""
    synth_script = Path(__file__).parent / "synthesize.py"
    cmd = [
        sys.executable, str(synth_script),
        dataset,
        "--model", model,
        "--output", str(output_dir),
    ]
    if no_docs:
        cmd.append("--no-docs")
    if mutated:
        cmd.append("--mutated")

    start = time.time()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=7200,
            cwd=str(ROOT),
        )
        elapsed = time.time() - start
        stdout = proc.stdout + proc.stderr

        input_tokens = output_tokens = 0
        m = re.search(r"tokens=([\d,]+)in/([\d,]+)out", stdout)
        if m:
            input_tokens = int(m.group(1).replace(",", ""))
            output_tokens = int(m.group(2).replace(",", ""))

        synthesis_ok = proc.returncode == 0
        # Double-check: even if exit 0, flag as failed if no server.py was produced
        has_output = (output_dir / "server.py").exists() or (output_dir / "build" / "index.js").exists()
        if synthesis_ok and not has_output:
            synthesis_ok = False

        error_snippet = None
        if not synthesis_ok:
            # Extract the most useful part of stderr/stdout for diagnosis
            error_snippet = stdout[-3000:]

        return {
            "model": model,
            "dataset": dataset,
            "output_dir": str(output_dir),
            "synthesis_ok": synthesis_ok,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "synthesis_time": elapsed,
            "error": error_snippet,
        }
    except subprocess.TimeoutExpired:
        return {
            "model": model, "dataset": dataset, "output_dir": str(output_dir),
            "synthesis_ok": False, "input_tokens": 0, "output_tokens": 0,
            "synthesis_time": time.time() - start, "error": "timeout",
        }
    except Exception as e:
        return {
            "model": model, "dataset": dataset, "output_dir": str(output_dir),
            "synthesis_ok": False, "input_tokens": 0, "output_tokens": 0,
            "synthesis_time": time.time() - start, "error": str(e),
        }


def print_sep(char: str = "=", width: int = 70) -> None:
    print(char * width)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synthesize benchmark datasets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--datasets", nargs="+", default=ALL_DATASETS,
        metavar="DATASET",
        help="Dataset(s) to synthesize (default: all)",
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL,
        help=f"Model ID for synthesis (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--no-docs",
        action="store_true",
        help="Run synthesis without providing any API docs (zero-knowledge condition)",
    )
    parser.add_argument(
        "--mutated",
        action="store_true",
        help="Run synthesis using mutated docs (renamed parameters condition)",
    )
    parser.add_argument(
        "--output-dir", default=str(OUTPUT_DIR),
        help="Directory for synthesis_results.json (default: benchmark/output/)",
    )
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path = out_dir / "synthesis_results.json"

    existing: list[dict] = []
    if results_path.exists():
        try:
            existing = json.loads(results_path.read_text())
        except Exception:
            existing = []
    results = list(existing)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    model = args.model

    for dataset in args.datasets:
        dataset_dir = DATASETS_DIR / dataset
        if not dataset_dir.exists():
            print(f"[SKIP] Unknown dataset: {dataset}")
            continue

        print_sep()
        print(f"Dataset: {dataset}  |  model: {model}")
        print_sep()

        slug = model.replace(":", "-").replace(".", "-")
        suffix = "_nodocs" if args.no_docs else ("_mutated" if args.mutated else "")
        impl_dir = dataset_dir / "synth" / f"{slug}_{timestamp}{suffix}"
        print(f"Output dir: {impl_dir.name}")
        print("Synthesizing ...", flush=True)

        synth_result = run_synthesis(model, dataset, impl_dir, no_docs=args.no_docs, mutated=args.mutated)
        status = "OK" if synth_result["synthesis_ok"] else "FAILED"
        print(
            f"Synthesis {status}  "
            f"tokens={synth_result['input_tokens']:,}in/"
            f"{synth_result['output_tokens']:,}out  "
            f"time={synth_result['synthesis_time']:.0f}s"
        )
        if not synth_result["synthesis_ok"]:
            snippet = (synth_result.get("error") or "")
            # Show last few lines, which usually contain the most useful error info
            lines = [l for l in snippet.splitlines() if l.strip()]
            tail = "\n    ".join(lines[-8:]) if lines else "(no output captured)"
            print(f"  FAILED — last lines:\n    {tail}")

        entry = {**synth_result, "timestamp": timestamp}
        results = [
            r for r in results
            if not (r["model"] == model and r["dataset"] == dataset
                    and r.get("timestamp") == timestamp)
        ]
        results.append(entry)
        results_path.write_text(json.dumps(results, indent=2))

    print_sep()
    print("SUMMARY")
    print_sep("-")
    for r in results:
        if r.get("timestamp") != timestamp:
            continue
        status = "OK" if r.get("synthesis_ok") else "FAILED"
        print(
            f"  {r['dataset']:<20} {status:<8} "
            f"{r.get('input_tokens', 0):>8,}in / {r.get('output_tokens', 0):>8,}out  "
            f"{r.get('synthesis_time', 0):.0f}s"
        )
    print(f"\nResults: {results_path}")


if __name__ == "__main__":
    main()
