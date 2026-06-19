#!/usr/bin/env python3
"""
Standalone vLLM synthesis script.

Runs synthesis on a benchmark dataset using a self-hosted vLLM server.
Designed to run from a separate workspace — no benchmark package required,
only `openai` and optionally `python-dotenv`.

Usage:
    python synthesize_vllm.py <dataset_dir> --model <model_id> [options]

    # Basic usage (docs condition, localhost vLLM)
    python synthesize_vllm.py /path/to/datasets/github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B

    # Custom vLLM URL
    python synthesize_vllm.py /path/to/datasets/stripe \\
        --model Qwen/Qwen3-72B --url http://my-gpu-server:8000/v1

    # No-docs condition
    python synthesize_vllm.py /path/to/datasets/github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --no-docs

    # Mutated docs condition
    python synthesize_vllm.py /path/to/datasets/github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --mutated

    # Specify output directory explicitly
    python synthesize_vllm.py /path/to/datasets/github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --output my_run

    # Enable bash tool
    python synthesize_vllm.py /path/to/datasets/github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --bash

Requirements:
    pip install openai
    pip install python-dotenv  # optional, for .env file support

vLLM must be started with tool calling enabled, e.g.:
    vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \\
        --enable-auto-tool-choice \\
        --tool-call-parser deepseek_r1 \\
        --host 0.0.0.0 --port 8000

Common tool-call parsers: deepseek_r1, hermes, mistral, llama3_json
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import openai


# ---------------------------------------------------------------------------
# Context window lookup (add new models here as you test them)
# ---------------------------------------------------------------------------

_CONTEXT_WINDOWS: Dict[str, int] = {
    "deepseek-r1-0528":     163_840,
    "deepseek-r1":          131_072,
    "deepseek-v3":          131_072,
    "deepseek-v2.5":        128_000,
    "kimi-k2":              131_072,
    "moonshot":             131_072,
    "qwen3-72b":            131_072,
    "qwen3-32b":            131_072,
    "qwen2.5-72b":          131_072,
    "qwen2.5-32b":          131_072,
    "llama-3.3-70b":        131_072,
    "llama-3.1-70b":        131_072,
    "llama-3.1-405b":       131_072,
    "mistral-large":        131_072,
}

# Compaction settings per context tier: (keep_full_turns, trim_to_chars).
# None = no compaction (for very large context models).
_COMPACT_SETTINGS = {
    32_768:  (2, 500),
    128_000: (4, 1_000),
    200_000: (6, 2_000),
    1_000_000: None,
}


def _context_window(model: str) -> int:
    model_lower = model.lower()
    for fragment, size in _CONTEXT_WINDOWS.items():
        if fragment in model_lower:
            return size
    return 128_000


def _compact_settings(context_window: int):
    for threshold in sorted(_COMPACT_SETTINGS):
        if context_window <= threshold:
            return _COMPACT_SETTINGS[threshold]
    return None


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

TOOLS: List[Dict] = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the workspace.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": "List files in a directory.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file. Creates parent directories as needed.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Replace the first occurrence of old_str with new_str in a file. "
                "old_str must match exactly (including whitespace). "
                "Use for targeted edits instead of rewriting the whole file."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_str": {"type": "string", "description": "Exact string to replace"},
                    "new_str": {"type": "string", "description": "Replacement string"},
                },
                "required": ["path", "old_str", "new_str"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "glob",
            "description": (
                "Find files matching a glob pattern. Returns matching paths relative to workspace. "
                "Example: glob('docs/api_*message*.md')"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string", "description": "Glob pattern to match"},
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grep",
            "description": (
                "Search file contents by regex pattern. Returns matching lines with file:line format. "
                "Use to find endpoints, parameters, or patterns across many docs."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string", "description": "Regex pattern to search for"},
                    "path": {"type": "string", "description": "Directory or file to search in (default: '.')"},
                    "file_pattern": {"type": "string", "description": "Glob to filter files (default: '*.md')"},
                },
                "required": ["pattern"],
            },
        },
    },
]

TOOLS_WITH_BASH = TOOLS + [
    {
        "type": "function",
        "function": {
            "name": "bash",
            "description": (
                "Run a shell command in the workspace directory. "
                "Use sparingly — e.g. to check Python syntax or validate imports. "
                "Timeout: 30s. Output capped at 3000 chars."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Shell command to execute"},
                },
                "required": ["command"],
            },
        },
    },
]

SYSTEM_PROMPT = """\
You are an expert software engineer building MCP server implementations from API documentation.

Your workspace contains:
- TASK.md  — requirements and deliverables (read this first)
- docs/    — API endpoint documentation files

Tools available:
  read_file(path)            — Read a file. Use for TASK.md and individual doc files.
  list_directory(path)       — List directory contents. Use once to survey docs/.
  glob(pattern)              — Find files by name pattern (e.g. glob("docs/api_*stream*.md")).
  grep(pattern, path, file_pattern) — Search file contents by regex across many files.
  write_file(path, content)  — Write a new file.
  edit_file(path, old_str, new_str) — Replace exact text in an existing file.
  bash(command)              — Run a shell command in the workspace (if enabled).

Workflow:
1. Read TASK.md, then glob("docs/*.md") to survey available docs.
2. Per domain: grep to find relevant docs → read_file → write_file/edit_file immediately.
3. Repeat for each domain. Never accumulate more than 2 unread docs before writing.
4. Finish with server.py and requirements.txt (or package.json for TypeScript).

Write all deliverables to files — do not describe code in text.\
"""

TASK_PROMPT = "Read TASK.md, then use glob+grep to survey the docs, then process each domain with read→write alternation. Use edit_file to extend existing modules rather than rewriting them."


# ---------------------------------------------------------------------------
# Tool executor
# ---------------------------------------------------------------------------

def execute_tool(workspace: Path, name: str, inputs: dict, enable_bash: bool = False) -> str:
    try:
        if name == "read_file":
            target = workspace / inputs["path"]
            if not target.exists():
                return f"Error: not found: {inputs['path']}"
            content = target.read_text(encoding="utf-8")
            return content[:20_000] + "\n[truncated]" if len(content) > 20_000 else content

        elif name == "list_directory":
            target = workspace / inputs["path"]
            if not target.is_dir():
                return f"Error: not a directory: {inputs['path']}"
            return "\n".join(
                f"{'d' if e.is_dir() else 'f'}  {e.name}" for e in sorted(target.iterdir())
            )

        elif name == "write_file":
            target = workspace / inputs["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(inputs["content"], encoding="utf-8")
            return f"wrote {len(inputs['content'])} chars to {inputs['path']}"

        elif name == "edit_file":
            target = workspace / inputs["path"]
            if not target.exists():
                return f"Error: not found: {inputs['path']}"
            content = target.read_text(encoding="utf-8")
            old_str = inputs["old_str"]
            if old_str not in content:
                return f"Error: old_str not found in {inputs['path']}"
            target.write_text(content.replace(old_str, inputs["new_str"], 1), encoding="utf-8")
            return f"edited {inputs['path']}"

        elif name == "glob":
            matches = sorted(workspace.glob(inputs["pattern"]))
            if not matches:
                return "No matches found."
            return "\n".join(str(p.relative_to(workspace)) for p in matches if p.is_file())

        elif name == "grep":
            pattern = inputs["pattern"]
            search_path = workspace / inputs.get("path", ".")
            file_pattern = inputs.get("file_pattern", "*.md")
            results = []
            for f in sorted(search_path.rglob(file_pattern)):
                try:
                    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                        if re.search(pattern, line):
                            results.append(f"{f.relative_to(workspace)}:{i}: {line}")
                            if len(results) >= 200:
                                results.append("[truncated at 200 matches]")
                                return "\n".join(results)
                except Exception:
                    continue
            return "\n".join(results) if results else "No matches found."

        elif name == "bash":
            if not enable_bash:
                return "Error: bash is disabled."
            proc = subprocess.run(
                inputs["command"],
                shell=True,
                cwd=str(workspace),
                capture_output=True,
                text=True,
                timeout=30,
            )
            output = (proc.stdout + proc.stderr).strip()
            return output[:3000] + "\n[truncated]" if len(output) > 3000 else output or "(no output)"

        return f"Error: unknown tool {name}"
    except subprocess.TimeoutExpired:
        return "Error: command timed out after 30s"
    except Exception as e:
        return f"Error: {e}"


def compact_messages(messages: list, keep_full_turns: int, trim_to: int) -> list:
    """Trim content of old tool result messages to keep context within limits."""
    tool_result_indices = [
        i for i, m in enumerate(messages)
        if m.get("role") == "tool"
    ]
    to_trim = (
        set(tool_result_indices[:-keep_full_turns])
        if len(tool_result_indices) > keep_full_turns
        else set()
    )

    if not to_trim:
        return messages

    compacted = []
    trimmed = 0
    for i, m in enumerate(messages):
        if i not in to_trim:
            compacted.append(m)
            continue
        content = m.get("content", "")
        if isinstance(content, str) and len(content) > trim_to:
            m = {**m, "content": content[:trim_to] + "\n[truncated for context]"}
            trimmed += 1
        compacted.append(m)

    if trimmed:
        print(f"  [compact] trimmed {trimmed} old tool results to {trim_to} chars", flush=True)
    return compacted


# ---------------------------------------------------------------------------
# Main synthesis loop
# ---------------------------------------------------------------------------

def synthesize(
    task_prompt: str,
    docs_dir: Optional[Path],
    model: str,
    base_url: str,
    max_turns: int,
    max_tokens: int,
    enable_bash: bool,
    context_window: Optional[int] = None,
    timeout: float = 300.0,
) -> dict:
    """Run the agentic synthesis loop. Returns a dict with files, token_usage, timing."""
    ctx = context_window or _context_window(model)
    compact = _compact_settings(ctx)
    compact_info = "off" if compact is None else f"{compact[0]}turns/{compact[1]}chars"

    ndocs = len(list(docs_dir.glob("*.md"))) if docs_dir else 0
    print(
        f"[{model}] compact={compact_info} ctx={ctx // 1000}K docs={ndocs}",
        flush=True,
    )

    tools = TOOLS_WITH_BASH if enable_bash else TOOLS
    client = openai.OpenAI(api_key="vllm", base_url=base_url, timeout=timeout)

    extra_body = {}
    if "qwen3" in model.lower():
        extra_body["chat_template_kwargs"] = {"enable_thinking": False}

    start_time = time.time()

    with tempfile.TemporaryDirectory() as tmpdir:
        workspace = Path(tmpdir)
        (workspace / "TASK.md").write_text(task_prompt)

        if docs_dir is not None:
            ws_docs = workspace / "docs"
            ws_docs.mkdir()
            for f in sorted(docs_dir.glob("*.md")):
                (ws_docs / f.name).write_text(f.read_text(encoding="utf-8"), encoding="utf-8")

        messages: List[Dict] = [{"role": "user", "content": TASK_PROMPT}]
        token_usage = {"input_tokens": 0, "output_tokens": 0}
        turn = 0

        for _ in range(max_turns):
            try:
                response = client.chat.completions.create(
                    model=model,
                    max_tokens=max_tokens,
                    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
                    tools=tools,
                    tool_choice="auto",
                    **({"extra_body": extra_body} if extra_body else {}),
                )
            except Exception as e:
                print(f"[turn {turn + 1}] API error: {e}", flush=True)
                break

            if response.usage:
                token_usage["input_tokens"] += response.usage.prompt_tokens
                token_usage["output_tokens"] += response.usage.completion_tokens

            turn += 1
            choice = response.choices[0]
            msg = choice.message

            if not msg.tool_calls:
                summary = (msg.content or "")[:120].replace("\n", " ")
                print(f"[turn {turn}] done — {summary}", flush=True)
                break

            messages.append({
                "role": "assistant",
                "content": msg.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,
                        },
                    }
                    for tc in msg.tool_calls
                ],
            })

            for tc in msg.tool_calls:
                try:
                    inputs = json.loads(tc.function.arguments)
                except json.JSONDecodeError:
                    inputs = {}
                result_str = execute_tool(workspace, tc.function.name, inputs, enable_bash)
                label = inputs.get("path", inputs.get("pattern", inputs.get("command", "")))
                print(f"[turn {turn}]  {tc.function.name}({label})", flush=True)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result_str,
                })

            if compact is not None:
                messages = compact_messages(messages, keep_full_turns=compact[0], trim_to=compact[1])

        # Collect all output files (skip TASK.md and docs/)
        files = {}
        for path in sorted(workspace.rglob("*")):
            if not path.is_file():
                continue
            rel = str(path.relative_to(workspace))
            if rel == "TASK.md" or rel.startswith("docs/"):
                continue
            files[rel] = path.read_text(encoding="utf-8")

    elapsed = time.time() - start_time
    u = token_usage
    print(
        f"done  turns={turn} "
        f"tokens={u['input_tokens']:,}in/{u['output_tokens']:,}out "
        f"time={elapsed:.1f}s",
        flush=True,
    )

    return {"files": files, "token_usage": token_usage, "synthesis_time": elapsed, "turns": turn}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Standalone vLLM synthesis script for benchmark datasets.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "dataset_dir",
        help="Path to the dataset directory (must contain TASK.md and docs/)",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Model ID as served by vLLM (e.g. deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)",
    )
    parser.add_argument(
        "--url",
        default="http://localhost:8000/v1",
        metavar="URL",
        help="Base URL of the vLLM server (default: http://localhost:8000/v1)",
    )
    parser.add_argument(
        "--no-docs",
        action="store_true",
        help="Zero-knowledge condition: run without providing any API docs",
    )
    parser.add_argument(
        "--mutated",
        action="store_true",
        help="Use docs_mutated/ instead of docs/ (mutated condition)",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=100,
        help="Maximum agent turns (default: 100)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16_000,
        help="Max tokens per model response (default: 16000)",
    )
    parser.add_argument(
        "--context-window",
        type=int,
        help="Override context window size in tokens (auto-detected from model name if omitted)",
    )
    parser.add_argument(
        "--bash",
        action="store_true",
        help="Enable bash tool (off by default)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=300.0,
        help="HTTP timeout per API call in seconds (default: 300)",
    )
    parser.add_argument(
        "--output",
        help=(
            "Output directory name. "
            "If it contains a path separator or starts with /, used as-is. "
            "Otherwise created under <output-dir>/<dataset>/ or <dataset_dir>/synth/. "
            "Default: <model-slug>_<timestamp>[_nodocs|_mutated]"
        ),
    )
    parser.add_argument(
        "--output-dir",
        metavar="DIR",
        help=(
            "Base output directory. When set, output goes to "
            "<DIR>/<dataset>/<model-slug>_<timestamp> instead of "
            "<dataset_dir>/synth/<model-slug>_<timestamp>."
        ),
    )
    parser.add_argument(
        "--env",
        metavar="FILE",
        help="Path to a .env file to load before running (e.g. /path/to/.env)",
    )
    args = parser.parse_args()

    # Optional .env loading
    if args.env:
        env_path = Path(args.env)
        if not env_path.exists():
            print(f"Error: .env file not found: {env_path}", file=sys.stderr)
            sys.exit(1)
        try:
            from dotenv import load_dotenv
            load_dotenv(env_path)
        except ImportError:
            # Manual parse if python-dotenv not installed
            for line in env_path.read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

    # Resolve dataset directory
    dataset_dir = Path(args.dataset_dir).resolve()
    if not dataset_dir.is_dir():
        print(f"Error: dataset directory not found: {dataset_dir}", file=sys.stderr)
        sys.exit(1)

    task_file = dataset_dir / "TASK.md"
    if not task_file.exists():
        print(f"Error: TASK.md not found in {dataset_dir}", file=sys.stderr)
        sys.exit(1)

    task_prompt = task_file.read_text()

    # Resolve docs directory
    if args.no_docs:
        docs_dir = None
        condition = "nodocs"
        task_prompt = (
            "NOTE: No API documentation is available for this task — the docs/ directory is empty. "
            "Ignore any references to documentation files in the task below. "
            "Use your general knowledge of the API to implement as many tools as you can.\n\n"
        ) + task_prompt
        print("Input:      none (--no-docs)")
    else:
        docs_subdir = "docs_mutated" if args.mutated else "docs"
        condition = "mutated" if args.mutated else "docs"
        docs_dir = dataset_dir / docs_subdir
        if not docs_dir.exists() or not any(docs_dir.glob("*.md")):
            print(f"Error: no .md files found in {docs_dir}", file=sys.stderr)
            sys.exit(1)
        ndocs = len(list(docs_dir.glob("*.md")))
        print(f"Loading docs... {ndocs} docs loaded")

    # Determine output directory
    model_slug = args.model.split("/")[-1].replace(":", "-").replace(".", "-")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    dataset_name = dataset_dir.name

    base_dir = Path(args.output_dir) / dataset_name if args.output_dir else dataset_dir / "synth"
    suffix = f"_{condition}" if condition != "docs" else ""
    auto_name = f"{model_slug}_{timestamp}{suffix}"

    if args.output:
        if "/" in args.output or args.output.startswith(os.sep):
            output_dir = Path(args.output)
        else:
            output_dir = base_dir / args.output
    else:
        output_dir = base_dir / auto_name

    if output_dir.exists():
        print(f"Output directory already exists: {output_dir}")
        answer = input("Overwrite? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)

    print()
    print(f"Dataset:    {dataset_name}  ({condition})")
    print(f"Model:      {args.model}  [vLLM @ {args.url}]")
    print(f"Max turns:  {args.max_turns}")
    print(f"Output:     {output_dir}")
    print()
    print("Starting agent...", flush=True)

    result = synthesize(
        task_prompt=task_prompt,
        docs_dir=docs_dir,
        model=args.model,
        base_url=args.url,
        max_turns=args.max_turns,
        max_tokens=args.max_tokens,
        enable_bash=args.bash,
        context_window=args.context_window,
        timeout=args.timeout,
    )

    files = result["files"]
    token_usage = result["token_usage"]
    synthesis_time = result["synthesis_time"]

    # Write output files
    output_dir.mkdir(parents=True, exist_ok=True)
    for rel_path, content in files.items():
        out = output_dir / rel_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")

    # Persist synthesis metadata (same format as synthesize.py)
    meta = {
        "dataset": dataset_name,
        "model": args.model,
        "condition": condition,
        "synthesis_time": synthesis_time,
        "token_usage": token_usage,
        "cost_estimate": None,
        "timestamp": timestamp,
        "vllm_url": args.url,
        "turns": result["turns"],
    }
    (output_dir / "synthesis_meta.json").write_text(json.dumps(meta, indent=2))

    print()
    print("=" * 50)
    print(f"Output:  {output_dir}")
    if files:
        print(f"Files:   {', '.join(files.keys())}")
    else:
        print("Files:   NONE — synthesis produced no output files")
    u = token_usage
    print(f"Tokens:  {u['input_tokens']:,} in / {u['output_tokens']:,} out")
    print(f"Time:    {synthesis_time:.1f}s")
    print("=" * 50)

    if not files:
        print("ERROR: synthesis failed — no files written.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
