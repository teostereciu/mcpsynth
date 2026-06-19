#!/usr/bin/env python3
"""
Score the grounding.json manifest produced alongside a synthesized MCP server.

Checks:
  1. Coverage    — fraction of implemented tools with a grounding entry
  2. Doc exists  — whether the cited doc file exists in the dataset docs/ folder
  3. Doc accuracy — LLM judge: does the cited doc actually describe the tool?

Usage:
    uv run python benchmark/scripts/eval_grounding.py github azure-chat-completions-gpt-5-2-..._20260513_1428
    uv run python benchmark/scripts/eval_grounding.py zulip azure-... --no-judge
    uv run python benchmark/scripts/eval_grounding.py notion azure-... --judge-model gcp-chat-completions-chat-gemini-3-flash-preview-sandbox
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

_env_file = ROOT / ".env"
if _env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(_env_file)

from benchmark.agent.harness import DEFAULT_JUDGE_MODEL

DATASETS_DIR = Path(__file__).parent.parent / "datasets"


# ---------------------------------------------------------------------------
# Tool name extraction
# ---------------------------------------------------------------------------

def extract_tool_names(synth_dir: Path) -> list[str]:
    """Extract registered tool names from server.py or src/index.ts."""
    server_py = synth_dir / "server.py"
    index_ts = synth_dir / "src" / "index.ts"

    if server_py.exists():
        return _extract_python_tools(server_py)
    elif index_ts.exists():
        return _extract_ts_tools(index_ts)
    return []


def _extract_python_tools(path: Path) -> list[str]:
    text = path.read_text()
    # @mcp.tool() / @app.tool() decorator followed by def name(
    names = re.findall(
        r'@(?:mcp|app|server)\.tool\(\s*\)\s*(?:async\s+)?def\s+(\w+)',
        text,
    )
    if names:
        return names
    # @mcp.tool(name="foo") explicit name
    names = re.findall(
        r'@(?:mcp|app|server)\.tool\(\s*name\s*=\s*["\'](\w+)["\']',
        text,
    )
    if names:
        return names
    # Programmatic registration: mcp.tool()(function_name)
    names = re.findall(
        r'(?:mcp|app|server)\.tool\(\s*\)\s*\(\s*(\w+)\s*\)',
        text,
    )
    return names


def _extract_ts_tools(path: Path) -> list[str]:
    text = path.read_text()
    # server.tool("name", ...) or server.addTool({ name: "name", ... })
    names = re.findall(r'(?:server|app)\.tool\(\s*["\'](\w+)["\']', text)
    if not names:
        names = re.findall(r'name\s*:\s*["\'](\w+)["\']', text)
    return names


# ---------------------------------------------------------------------------
# LLM judge
# ---------------------------------------------------------------------------

def _make_llm(model: str, chomsky: bool):
    if chomsky:
        if "anthropic" in model:
            from pychomsky.chchat.anthropicvertex import GCPVertexAnthropicChatWrapper
            return GCPVertexAnthropicChatWrapper(model_name=model, max_tokens=512, temperature=0.0, stream=True)
        elif model.startswith("azure-"):
            from pychomsky.chchat.azureopenai import AzureOpenAIChatWrapper
            llm = AzureOpenAIChatWrapper(model_name=model, max_completion_tokens=512, temperature=0.0, streaming=True)
            llm.streaming = True
            return llm
        elif "gemini" in model:
            from pychomsky.chchat.googlegenai import GoogleGenAIWrapper
            return GoogleGenAIWrapper(model_name=model, max_tokens=512, temperature=0.0)
        else:
            from pychomsky.chchat import EbayLLMChatWrapper
            return EbayLLMChatWrapper(model_name=model, max_tokens=512, temperature=0.0, streaming=True)
    else:
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model=model, max_tokens=512, temperature=0.0)  # type: ignore


def _judge_entry(
    tool_name: str,
    doc_text: str,
    endpoint: str,
    llm,
) -> tuple[bool, str]:
    """Ask judge: does this doc actually describe this tool/endpoint?"""
    from langchain_core.messages import HumanMessage, SystemMessage

    prompt = f"""\
Tool name: {tool_name}
Claimed endpoint: {endpoint}
Documentation file content (may be truncated):
---
{doc_text[:10000]}
---

Does this documentation file describe the API operation implemented by the tool above?

Answer YES if:
- The doc covers the resource/operation indicated by the tool name and endpoint, OR
- The doc is a multi-operation reference for the same resource (e.g. a single file covering create/retrieve/update for PaymentIntents is valid for any of those tools)

Answer NO only if the doc is clearly about a different resource or operation entirely.

Respond in exactly this format:
MATCH: YES or NO
REASON: <one sentence>"""

    system = SystemMessage(content="You are a precise technical auditor. Follow the output format exactly.")
    try:
        response = llm.invoke([system, HumanMessage(content=prompt)])
        content = str(getattr(response, "content", "")).strip()
        match = bool(re.search(r"MATCH:\s*YES", content, re.IGNORECASE))
        reason_m = re.search(r"REASON:\s*(.+)", content)
        reason = reason_m.group(1).strip() if reason_m else content[:120]
        return match, reason
    except Exception as e:
        return False, f"Judge error: {e}"


# ---------------------------------------------------------------------------
# Main scoring
# ---------------------------------------------------------------------------

def score_grounding(
    dataset: str,
    impl: str,
    judge_model: str | None,
    chomsky: bool,
) -> dict:
    dataset_dir = DATASETS_DIR / dataset
    synth_dir = dataset_dir / "synth" / impl
    grounding_file = synth_dir / "grounding.json"

    result: dict = {"dataset": dataset, "impl": impl}

    # --- grounding.json present? ---
    if not grounding_file.exists():
        result["error"] = "grounding.json not found"
        return result

    try:
        grounding: dict = json.loads(grounding_file.read_text())
    except json.JSONDecodeError as e:
        result["error"] = f"grounding.json parse error: {e}"
        return result

    # --- coverage ---
    tool_names = extract_tool_names(synth_dir)
    if tool_names:
        implemented = set(tool_names)
        manifested = set(grounding.keys())
        result["tool_count"] = len(implemented)
        result["manifest_count"] = len(manifested)
        result["coverage"] = round(len(manifested & implemented) / len(implemented), 3)
        result["missing_from_manifest"] = sorted(implemented - manifested)
        result["extra_in_manifest"] = sorted(manifested - implemented)
    else:
        result["tool_count"] = None
        result["coverage"] = None

    # --- per-entry scoring ---
    llm = _make_llm(judge_model, chomsky) if judge_model else None
    entries = []
    n_exist = 0
    n_accurate = 0

    for tool_name, entry in grounding.items():
        doc_rel = entry.get("doc", "")
        endpoint = entry.get("endpoint", "")
        doc_path = dataset_dir / doc_rel
        doc_exists = doc_path.exists()
        if doc_exists:
            n_exist += 1

        entry_result: dict = {
            "tool": tool_name,
            "doc": doc_rel,
            "endpoint": endpoint,
            "doc_exists": doc_exists,
            "accurate": None,
            "judge_reason": None,
        }

        if llm and doc_exists:
            accurate, reason = _judge_entry(tool_name, doc_path.read_text(), endpoint, llm)
            entry_result["accurate"] = accurate
            entry_result["judge_reason"] = reason
            if accurate:
                n_accurate += 1

        entries.append(entry_result)

    result["entries"] = entries

    n = len(entries)
    result["doc_exists_rate"] = round(n_exist / n, 3) if n else None
    result["accuracy_rate"] = round(n_accurate / n_exist, 3) if (llm and n_exist) else None

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Score grounding.json for a synthesized MCP server")
    parser.add_argument("dataset", help="Dataset name (e.g. github, zulip)")
    parser.add_argument("impl", help="Implementation directory name inside synth/")
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL, help="LLM judge model")
    parser.add_argument("--no-judge", action="store_true", help="Skip LLM accuracy check")
    parser.add_argument("--chomsky", action="store_true", help="Use pychomsky gateway")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output raw JSON")
    args = parser.parse_args()

    judge_model = None if args.no_judge else args.judge_model
    result = score_grounding(args.dataset, args.impl, judge_model, args.chomsky)

    if args.json_out:
        print(json.dumps(result, indent=2))
        return

    # Human-readable summary
    print(f"\nDataset:  {result['dataset']}")
    print(f"Impl:     {result['impl']}")

    if "error" in result:
        print(f"ERROR:    {result['error']}")
        return

    if result.get("coverage") is not None:
        print(f"\nCoverage: {result['coverage']:.0%}  ({result['manifest_count']}/{result['tool_count']} tools manifested)")
        if result["missing_from_manifest"]:
            print(f"  Missing: {', '.join(result['missing_from_manifest'][:10])}")
        if result["extra_in_manifest"]:
            print(f"  Extra:   {', '.join(result['extra_in_manifest'][:10])}")

    print(f"Doc exists rate: {result['doc_exists_rate']:.0%}" if result.get("doc_exists_rate") is not None else "Doc exists rate: n/a")
    if result.get("accuracy_rate") is not None:
        print(f"Doc accuracy:    {result['accuracy_rate']:.0%}  (judge: {judge_model})")
    elif judge_model is None:
        print("Doc accuracy:    skipped (--no-judge)")

    print(f"\n{'Tool':<35} {'Doc exists':<12} {'Accurate':<10} Doc")
    print("-" * 90)
    for e in result["entries"]:
        exists = "yes" if e["doc_exists"] else "NO"
        accurate = ("yes" if e["accurate"] else "NO") if e["accurate"] is not None else "—"
        print(f"{e['tool']:<35} {exists:<12} {accurate:<10} {e['doc']}")


if __name__ == "__main__":
    main()
