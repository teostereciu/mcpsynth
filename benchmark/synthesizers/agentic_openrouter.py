"""
Agentic OpenRouter synthesizer using the Claude Agent SDK.

Runs the Claude Code agent loop (via claude-agent-sdk) with the working directory
set to a temporary workspace containing TASK.md and docs/. The agent uses built-in
file tools (Read, Write, Glob, Grep) to explore docs and write deliverables.

OpenRouter support: the Agent SDK spawns the Claude Code CLI, which respects
ANTHROPIC_BASE_URL. Set that to https://openrouter.ai/api/v1 and provide an
OPENROUTER_API_KEY to route through OpenRouter. Note that model names must use
OpenRouter's format (e.g. "anthropic/claude-sonnet-4-5", "google/gemini-2.5-pro").

Required env vars:
    ANTHROPIC_API_KEY      - Anthropic key (direct), OR
    OPENROUTER_API_KEY     - OpenRouter key (set USE_OPENROUTER=1 to activate)

Usage:
    # Direct Anthropic:
    synth = AgenticOpenRouter(model="claude-sonnet-4-5-20251101")

    # Via OpenRouter:
    synth = AgenticOpenRouter(model="google/gemini-2.5-pro", use_openrouter=True)

    result = synth.synthesize(task_prompt, api_docs)
"""

import asyncio
import os
import sys
import time
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

from benchmark.synthesizers import BaseSynthesizer, Document, SynthesisResult


SYSTEM_PROMPT = """\
You are an expert software engineer building MCP server implementations from API documentation.

Your workspace contains:
- TASK.md  — requirements and deliverables (read this first)
- docs/    — API endpoint documentation files

Workflow:
1. Read TASK.md to understand what to build and what files to deliver
2. Use Glob to list docs/, then read a representative sample across all API domains
3. Write all deliverable files (generated_tools/, server.py, SCENARIO_SOLUTIONS.md, requirements.txt)

Read docs before writing code — base your implementation on the actual API docs.
Sample 3-5 endpoints per domain to understand patterns, then generalize.\
"""

TASK_PROMPT = "Read TASK.md, explore the docs/, then write all deliverables specified in TASK.md."


class AgenticOpenRouter(BaseSynthesizer):
    """
    Synthesizer using the Claude Agent SDK with a file-system workspace.

    The Agent SDK runs the Claude Code CLI with cwd set to a temp directory
    containing TASK.md and docs/. The agent reads docs and writes output files
    using built-in Read/Write/Glob/Grep tools, then we collect the results.

    For non-Anthropic models via OpenRouter, pass use_openrouter=True — this
    overrides ANTHROPIC_BASE_URL and ANTHROPIC_API_KEY in the CLI environment.
    """

    def __init__(
        self,
        model: str = "claude-sonnet-4-5-20251101",
        max_turns: int = 100,
        use_openrouter: bool = False,
        enable_bash: bool = False,
    ):
        self.model = model
        self.max_turns = max_turns
        self.use_openrouter = use_openrouter
        self.enable_bash = enable_bash

    @property
    def name(self) -> str:
        return f"agentic_sdk_{self.model.replace('/', '_')}"

    @property
    def description(self) -> str:
        via = "OpenRouter" if self.use_openrouter else "Anthropic"
        return f"Claude Agent SDK agentic loop via {via} ({self.model})"

    def get_config(self) -> Dict[str, Any]:
        return {
            **super().get_config(),
            "model": self.model,
            "max_turns": self.max_turns,
            "use_openrouter": self.use_openrouter,
            "enable_bash": self.enable_bash,
        }

    def synthesize(
        self,
        task_prompt: str,
        api_docs: List[Document],
        source_dir: Path | None = None,
        **_kwargs,
    ) -> SynthesisResult:
        start_time = time.time()

        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)

            # Populate workspace
            (workspace / "TASK.md").write_text(task_prompt)
            if source_dir is not None:
                # Source-tree condition: symlink the full repo into workspace/source/
                # so the agent can navigate it with glob/grep/read without copying GBs.
                (workspace / "source").symlink_to(Path(source_dir).resolve())
                print(f"[sdk] model={self.model} input=source_tree({source_dir})", flush=True)
            else:
                docs_dir = workspace / "docs"
                docs_dir.mkdir()
                for doc in api_docs:
                    filename = doc.metadata.get("filename", Path(doc.path).name)
                    (docs_dir / filename).write_text(doc.content)
                print(f"[sdk] model={self.model} docs={len(api_docs)}", flush=True)

            result = asyncio.run(self._run_agent(workspace))

            files = self._collect_output_files(workspace)

        synthesis_time = time.time() - start_time

        usage = self._extract_usage(result)
        print(
            f"[sdk] done turns={result.num_turns} "
            f"tokens={usage['input_tokens']}in/{usage['output_tokens']}out "
            f"cost=${result.total_cost_usd or 0:.4f} "
            f"files={len(files)} time={synthesis_time:.1f}s",
            flush=True,
        )

        return SynthesisResult(
            code=self._combine_generated_tools(files),
            metadata={
                "model": self.model,
                "num_turns": result.num_turns,
                "session_id": result.session_id,
                "is_error": result.is_error,
                "files_written": list(files.keys()),
                "multi_file_structure": files,
            },
            token_usage=self._extract_usage(result),
            synthesis_time=synthesis_time,
            cost_estimate=result.total_cost_usd,
        )

    async def _run_agent(self, workspace: Path) -> ResultMessage:
        env = {}
        if self.use_openrouter:
            env["ANTHROPIC_BASE_URL"] = "https://openrouter.ai/api"
            env["ANTHROPIC_API_KEY"] = os.environ["OPENROUTER_API_KEY"]
            # Pass model via env vars (documented as "passed to provider as-is")
            # rather than ClaudeAgentOptions.model which goes through CLI validation
            env["ANTHROPIC_MODEL"] = self.model
            env["ANTHROPIC_CUSTOM_MODEL_OPTION"] = self.model
            env["ANTHROPIC_CUSTOM_MODEL_OPTION_NAME"] = self.model

        options = ClaudeAgentOptions(
            system_prompt=SYSTEM_PROMPT,
            model=self.model if not self.use_openrouter else None,
            max_turns=self.max_turns,
            cwd=str(workspace),
            permission_mode="acceptEdits",
            allowed_tools=["Read", "Write", "Glob", "Grep", "Edit"] + (["Bash"] if self.enable_bash else []),
            # No user/project settings — fully isolated run
            setting_sources=None,
            env=env,
            # Surface CLI stderr so errors aren't silently swallowed
            debug_stderr=sys.stderr,
        )

        print("[sdk] spawning CLI...", flush=True)
        turn = 0
        result = None
        async for message in query(prompt=TASK_PROMPT, options=options):
            if isinstance(message, ResultMessage):
                result = message
            elif hasattr(message, "content"):
                turn += 1
                tool_calls = [b for b in message.content if hasattr(b, "name")]
                if tool_calls:
                    print(f"[turn {turn}]", flush=True)
                    for block in tool_calls:
                        path = block.input.get("path", block.input.get("pattern", ""))
                        print(f"  {block.name}({path})", flush=True)
                else:
                    print(f"[turn {turn}] (text response)", flush=True)
                    for block in message.content:
                        if hasattr(block, "text"):
                            preview = block.text[:300].replace("\n", " ")
                            print(f"  > {preview}", flush=True)

        if result is None:
            raise RuntimeError("Agent SDK returned no ResultMessage")

        return result

    def _collect_output_files(self, workspace: Path) -> Dict[str, str]:
        """Collect all files written by the agent (excluding inputs)."""
        files = {}
        for path in sorted(workspace.rglob("*")):
            if not path.is_file():
                continue
            rel = str(path.relative_to(workspace))
            if rel == "TASK.md" or rel.startswith("docs/") or rel.startswith("source/"):
                continue
            files[rel] = path.read_text(encoding="utf-8")
        return files

    def _extract_usage(self, result: ResultMessage) -> Dict[str, int]:
        """
        Extract token counts from ResultMessage.usage.

        The CLI emits cumulative session totals as total_input_tokens /
        total_output_tokens, plus per-last-turn input_tokens / output_tokens
        and prompt-cache breakdowns. Prefer the cumulative totals.
        """
        u = result.usage or {}
        return {
            # Cumulative session totals (preferred)
            "input_tokens": u.get("total_input_tokens", u.get("input_tokens", 0)),
            "output_tokens": u.get("total_output_tokens", u.get("output_tokens", 0)),
            # Cache breakdowns (may be 0 on non-Anthropic backends)
            "cache_creation_input_tokens": u.get("cache_creation_input_tokens", 0),
            "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
        }

    def _combine_generated_tools(self, files: Dict[str, str]) -> str:
        """Return __init__.py as the primary code artifact; callers use multi_file_structure."""
        return files.get("generated_tools/__init__.py", "")
