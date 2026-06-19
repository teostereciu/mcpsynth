"""
Advanced agentic synthesizer using pychomsky with an expanded toolset.

Adds Glob, Grep, Edit, and optional Bash to the basic read/write loop,
giving models SOTA-level codebase exploration and editing capabilities:

  - glob        — find files by pattern without reading them
  - grep        — search file contents by regex across the workspace
  - edit_file   — targeted string replacement (no full-file rewrites needed)
  - bash        — run shell commands in the workspace (optional, off by default)

Wrapper selection (same as AgenticChomsky):
  - "*anthropic*" → GCPVertexAnthropicChatWrapper  (streaming via stream=True)
  - "azure-*"     → AzureOpenAIChatWrapper
  - "*gemini*"    → GoogleGenAIWrapper
  - anything else → EbayLLMChatWrapper

Reasoning configuration:
  - Gemini: pass thinking_budget= (tokens) or thinking_level= ('low'|'medium'|'high')
  - Anthropic: extended thinking attempted via model_kwargs; may need gateway support
  - GPT: no explicit param; reasoning is built-in

Speed notes:
  - Glob/Grep let the model find relevant docs without reading all 164 files
  - Larger max_tokens per turn means fewer turns for code generation
  - thinking_budget=0 disables Gemini thinking for maximum speed

Usage:
    synth = AdvancedAgenticChomsky(
        model="gcp-chat-completions-chat-gemini-2.5-pro-sandbox",
        thinking_level="high",   # Gemini reasoning
    )
    synth = AdvancedAgenticChomsky(
        model="gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox",
    )
    result = synth.synthesize(task_prompt, api_docs)
"""

import re
import subprocess
import time
import tempfile
from pathlib import Path
from typing import List, Dict, Any, Optional

from benchmark.synthesizers import BaseSynthesizer, Document, SynthesisResult


# Context window sizes (in tokens) by model name.
# Used to auto-configure compaction aggressiveness.
MODEL_CONTEXT_WINDOWS: Dict[str, int] = {
    # Azure GPT — 128K
    "azure-chat-completions-gpt-4o-2024-05-13-sandbox":          128_000,
    "azure-chat-completions-gpt-4o-mini-2024-07-18-sandbox":     128_000,
    "azure-chat-completions-gpt-5-chat-2025-08-07-sandbox":      128_000,
    "azure-chat-completions-gpt-5-1-chat-2025-11-13-sandbox":    128_000,
    "azure-chat-completions-gpt-5-2-chat-2025-12-11-sandbox":    128_000,
    "azure-chat-completions-o1-mini-2024-09-12-sandbox":         128_000,
    # Azure GPT — 200K
    "azure-chat-completions-o3-mini-2025-01-31-sandbox":         200_000,
    "azure-chat-completions-o4-mini-2025-04-16-sandbox":         200_000,
    # Azure GPT — 400K
    "azure-chat-completions-gpt-5-2025-08-07-sandbox":           400_000,
    "azure-chat-completions-gpt-5-mini-2025-08-07-sandbox":      400_000,
    "azure-chat-completions-gpt-5-nano-2025-08-07-sandbox":      400_000,
    "azure-chat-completions-gpt-5-1-2025-11-13-sandbox":         400_000,
    "azure-chat-completions-gpt-5-2-2025-12-11-sandbox":         400_000,
    # Azure GPT — 1M
    "azure-chat-completions-gpt-4-1-2025-04-14-sandbox":       1_000_000,
    "azure-chat-completions-gpt-4-1-mini-2025-04-14-sandbox":  1_000_000,
    "azure-chat-completions-gpt-4-1-nano-2025-04-14-sandbox":  1_000_000,
    # Gemini — 1M
    "gcp-chat-completions-chat-gemini-2.0-flash-001-sandbox":  1_000_000,
    "gcp-chat-completions-chat-gemini-2.0-flash-lite-001-sandbox": 1_000_000,
    "gcp-chat-completions-chat-gemini-2.5-flash-sandbox":      1_000_000,
    "gcp-chat-completions-chat-gemini-2.5-pro-sandbox":        1_000_000,
    "gcp-chat-completions-chat-gemini-3-flash-preview-sandbox": 1_000_000,
    "gcp-chat-completions-chat-gemini-3.1-flash-lite-preview-sandbox": 1_000_000,
    "gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox": 1_000_000,
    # Anthropic Claude — 200K
    "gcp-chat-completions-anthropic-claude-3.5-sonnet-v2-sandbox": 200_000,
    "gcp-chat-completions-anthropic-claude-3.7-sonnet-sandbox":    200_000,
    "gcp-chat-completions-anthropic-claude-sonnet-4-sandbox":      200_000,
    "gcp-chat-completions-anthropic-claude-sonnet-4.5-sandbox":    200_000,
    "gcp-chat-completions-anthropic-claude-haiku-4.5-sandbox":     200_000,
    "gcp-chat-completions-anthropic-claude-opus-4-sandbox":        200_000,
    "gcp-chat-completions-anthropic-claude-opus-4.5-sandbox":      200_000,
    # Anthropic Claude — 1M
    "gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox":  1_000_000,
    "gcp-chat-completions-anthropic-claude-opus-4.6-sandbox":    1_000_000,
    "gcp-chat-completions-anthropic-claude-opus-4.7-sandbox":    1_000_000,
}

# Maximum output tokens per model.
# Some models (especially *-chat-* variants) have lower output caps than their
# full counterparts. Requesting more than the cap causes the Azure API to
# reject the call; pychomsky's streaming wrapper drops the error silently,
# producing zero chunks and "No generation chunks were returned".
MODEL_MAX_OUTPUT_TOKENS: Dict[str, int] = {
    # gpt-5-2-chat and gpt-5-1-chat variants cap at 16K output
    "azure-chat-completions-gpt-5-2-chat-2025-12-11-sandbox": 16_384,
    "azure-chat-completions-gpt-5-1-chat-2025-11-13-sandbox": 16_384,
    "azure-chat-completions-gpt-5-chat-2025-08-07-sandbox":   16_384,
}


# Compaction settings keyed by context tier.
# (keep_full_turns, trim_to_chars) — None means no compaction.
_COMPACT_SETTINGS = {
    128_000: (4, 1_000),
    200_000: (6, 2_000),
    400_000: (8, 4_000),
    1_000_000: None,   # large enough — skip compaction entirely
}


def _compact_settings_for(context_window: int):
    """Return (keep_full_turns, trim_to) for the given context window size."""
    for threshold in sorted(_COMPACT_SETTINGS):
        if context_window <= threshold:
            return _COMPACT_SETTINGS[threshold]
    return None  # larger than all known thresholds


def _min_turn_interval(model: str) -> float:
    """Minimum seconds between LLM calls to stay under rate limits.

    Anthropic Claude via Vertex is capped at 6 req/min (10s between calls).
    All other models (Gemini 60-300 req/min, Azure 180 req/min) need no delay.
    """
    return 11.0 if "anthropic" in model else 0.0


def _extract_token_usage(response, messages: list) -> tuple[int, int]:
    """Extract (input_tokens, output_tokens) from an LLM response.

    Handles multiple formats:
    - Anthropic: usage_metadata object with input_tokens/output_tokens attrs
    - Azure/OpenAI streaming: response_metadata["token_usage"] with prompt_tokens/completion_tokens
    - Azure/OpenAI non-streaming: usage_metadata dict with prompt_tokens/completion_tokens
    - Fallback: character-count estimation, separately for input and output

    Azure streaming does not include completion token counts unless
    stream_options.include_usage is set, so input and output are estimated
    independently — whichever is missing falls back to char-count estimation.
    """
    in_tok = out_tok = 0

    # 1. Try response_metadata["token_usage"] — Azure streaming puts usage here
    meta = getattr(response, "response_metadata", None) or {}
    if isinstance(meta, dict):
        tu = meta.get("token_usage") or meta.get("usage") or {}
        if isinstance(tu, dict):
            in_tok  = tu.get("prompt_tokens",     tu.get("input_tokens",  0))
            out_tok = tu.get("completion_tokens", tu.get("output_tokens", 0))

    # 2. Try usage_metadata (dict or object) — Anthropic and non-streaming Azure
    if in_tok == 0 and out_tok == 0:
        usage = getattr(response, "usage_metadata", None)
        if isinstance(usage, dict):
            in_tok  = usage.get("input_tokens",  0) or usage.get("prompt_tokens",    0)
            out_tok = usage.get("output_tokens", 0) or usage.get("completion_tokens", 0)
        elif usage is not None:
            in_tok  = getattr(usage, "input_tokens",  None) or getattr(usage, "prompt_tokens",    0)
            out_tok = getattr(usage, "output_tokens", None) or getattr(usage, "completion_tokens", 0)

    # 3. Fall back independently for whichever is still zero.
    #    Azure streaming often reports input tokens but not output tokens.
    if in_tok == 0:
        total_input_chars = sum(
            len(str(getattr(m, "content", "") or ""))
            for m in messages
        )
        in_tok = max(1, total_input_chars // 4)

    if out_tok == 0:
        # Count text content + tool call arguments (tool-call turns have empty content)
        content_chars = len(str(getattr(response, "content", "") or ""))
        tool_calls = getattr(response, "tool_calls", []) or []
        tool_args_chars = sum(len(str(tc.get("args", {}))) for tc in tool_calls)
        out_tok = max(1, (content_chars + tool_args_chars) // 4)

    return int(in_tok), int(out_tok)


SYSTEM_PROMPT = """\
You are an expert software engineer building MCP server implementations from API documentation.

Your workspace contains:
- TASK.md  — requirements and deliverables (read this first)
- docs/    — API endpoint documentation files

Tools available:
  read_file(path)
    — Read a file. Use for TASK.md and individual doc files.

  list_directory(path)
    — List directory contents. Use once to survey docs/.

  glob(pattern)
    — Find files by name pattern. Use to locate docs for a domain without reading them.
      e.g. glob("docs/api_*message*.md"), glob("docs/api_*stream*.md")

  grep(pattern, path, file_pattern)
    — Search file contents by regex across many files at once.
      Use to extract endpoint URLs, parameter names, or HTTP methods without reading full files.
      e.g. grep("^## ", "docs", "*.md") to list all endpoint titles
           grep("POST /api/v1", "docs", "*.md") to find all POST endpoints
           grep("scheduled", "docs", "*.md") to find scheduling-related endpoints

  write_file(path, content)
    — Write a new file. Use for each generated_tools/*.py module and deliverables.

  edit_file(path, old_str, new_str)
    — Replace exact text in an existing file. Use to add functions to an already-written
      module instead of rewriting the whole file.
      e.g. after writing generated_tools/messages.py, use edit_file to append a new function.

Workflow:
1. Read TASK.md, then glob("docs/*.md") to survey available docs.
2. Per domain: grep to find relevant docs → read_file → write_file/edit_file immediately.
3. Repeat for each domain. Never accumulate more than 2 unread docs before writing.
4. Finish with server.py and requirements.txt (or package.json for TypeScript).

Write all deliverables to files — do not describe code in text.\
"""

TASK_PROMPT = "Read TASK.md, then use glob+grep to survey the docs, then process each domain with read→write alternation. Use edit_file to extend existing modules rather than rewriting them."

TOOLS = [
    {
        "name": "read_file",
        "description": "Read a file from the workspace.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "list_directory",
        "description": "List files in a directory.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a file. Creates parent directories as needed.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "edit_file",
        "description": (
            "Replace the first occurrence of old_str with new_str in a file. "
            "old_str must match exactly (including whitespace). "
            "Use this for targeted edits instead of rewriting the whole file."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_str": {"type": "string", "description": "Exact string to replace"},
                "new_str": {"type": "string", "description": "Replacement string"},
            },
            "required": ["path", "old_str", "new_str"],
        },
    },
    {
        "name": "glob",
        "description": (
            "Find files matching a glob pattern. Returns matching paths relative to workspace. "
            "Example patterns: 'docs/api_*message*.md', 'generated_tools/*.py'"
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Glob pattern to match"},
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "grep",
        "description": (
            "Search file contents by regex pattern. Returns matching lines with file:line format. "
            "Use to find specific endpoints, parameters, or patterns across many docs."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Regex pattern to search for"},
                "path": {"type": "string", "description": "Directory or file to search in (default: '.')"},
                "file_pattern": {"type": "string", "description": "Glob pattern to filter files (default: '*.md')"},
            },
            "required": ["pattern"],
        },
    },
]

TOOLS_WITH_BASH = TOOLS + [
    {
        "name": "bash",
        "description": (
            "Run a shell command in the workspace directory. "
            "Use sparingly — e.g. to check Python syntax, list installed packages, or validate imports. "
            "Timeout: 30s. Output capped at 3000 chars."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Shell command to execute"},
            },
            "required": ["command"],
        },
    },
]


class AdvancedAgenticChomsky(BaseSynthesizer):

    def __init__(
        self,
        model: str = "gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox",
        max_turns: int = 100,
        max_tokens: int = 32000,
        chgw_endpoint: str = None,
        enable_bash: bool = False,
        # Context window — auto-detected from model name if not set.
        # Controls how aggressively old tool messages are compacted.
        context_window: Optional[int] = None,
        # Gemini reasoning
        thinking_budget: Optional[int] = None,
        thinking_level: Optional[str] = None,
        include_thoughts: Optional[bool] = None,
    ):
        self.model = model
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.chgw_endpoint = chgw_endpoint
        self.enable_bash = enable_bash
        self.context_window = context_window or MODEL_CONTEXT_WINDOWS.get(model, 128_000)
        self.thinking_budget = thinking_budget
        self.thinking_level = thinking_level
        self.include_thoughts = include_thoughts

    @property
    def name(self) -> str:
        return f"advanced_chomsky_{self.model.replace('/', '_')}"

    @property
    def description(self) -> str:
        return f"Advanced tool loop via pychomsky ({self.model})"

    def get_config(self) -> Dict[str, Any]:
        return {
            **super().get_config(),
            "model": self.model,
            "max_turns": self.max_turns,
            "max_tokens": self.max_tokens,
            "enable_bash": self.enable_bash,
            "context_window": self.context_window,
            "thinking_budget": self.thinking_budget,
            "thinking_level": self.thinking_level,
        }

    def _make_llm(self):
        kwargs = {"model_name": self.model}
        if self.chgw_endpoint:
            kwargs["chgw_endpoint"] = self.chgw_endpoint

        if "anthropic" in self.model:
            from pychomsky.chchat.anthropicvertex import GCPVertexAnthropicChatWrapper
            extra = {}
            if self.thinking_budget is not None:
                extra["thinking"] = {"type": "enabled", "budget_tokens": self.thinking_budget}
            return GCPVertexAnthropicChatWrapper(
                max_tokens=self.max_tokens,
                temperature=1.0 if self.thinking_budget else 0.2,
                stream=True,
                **kwargs,
                **extra,
            )
        elif self.model.startswith("azure-"):
            from pychomsky.chchat.azureopenai import AzureOpenAIChatWrapper
            max_out = min(self.max_tokens, MODEL_MAX_OUTPUT_TOKENS.get(self.model, self.max_tokens))
            llm = AzureOpenAIChatWrapper(
                max_completion_tokens=max_out,
                temperature=0.2,
                streaming=True,
                **kwargs,
            )
            llm.streaming = True
            return llm
        elif "gemini" in self.model:
            from pychomsky.chchat.googlegenai import GoogleGenAIWrapper
            return GoogleGenAIWrapper(
                max_tokens=self.max_tokens,
                temperature=0.2,
                thinking_budget=self.thinking_budget,
                thinking_level=self.thinking_level,
                include_thoughts=self.include_thoughts,
                **kwargs,
            )
        else:
            from pychomsky.chchat import EbayLLMChatWrapper
            return EbayLLMChatWrapper(
                max_tokens=self.max_tokens,
                temperature=0.2,
                streaming=True,
                **kwargs,
            )

    def synthesize(self, task_prompt: str, api_docs: List[Document], source_dir: Path | None = None, **_kwargs) -> SynthesisResult:
        from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

        start_time = time.time()
        tools = TOOLS_WITH_BASH if self.enable_bash else TOOLS

        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            (workspace / "TASK.md").write_text(task_prompt)
            if source_dir is not None:
                (workspace / "source").symlink_to(Path(source_dir).resolve())
            else:
                docs_dir = workspace / "docs"
                docs_dir.mkdir()
                for doc in api_docs:
                    filename = doc.metadata.get("filename", Path(doc.path).name)
                    (docs_dir / filename).write_text(doc.content)

            thinking_info = ""
            if self.thinking_budget is not None:
                thinking_info = f" thinking_budget={self.thinking_budget}"
            elif self.thinking_level is not None:
                thinking_info = f" thinking_level={self.thinking_level}"
            compact = _compact_settings_for(self.context_window)
            compact_info = f" compact=off" if compact is None else f" compact={compact[0]}turns/{compact[1]}chars"
            print(f"[{self.model}]{thinking_info}{compact_info} ctx={self.context_window//1000}K docs={len(api_docs)}", flush=True)

            llm = self._make_llm()
            llm_with_tools = llm.bind_tools(tools)

            messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=TASK_PROMPT),
            ]
            turn = 0
            total_input_tokens = 0
            total_output_tokens = 0

            for _ in range(self.max_turns):
                turn += 1
                response = None
                last_error: Exception | None = None
                for attempt in range(3):
                    try:
                        response = self._stream_with_timeout(llm_with_tools, messages, timeout=120)
                        if response is not None:
                            last_error = None
                            break  # success
                        wait = 30 * (attempt + 1)
                        print(f"[turn {turn}] stream timeout (attempt {attempt+1}/3), retrying in {wait}s", flush=True)
                        time.sleep(wait)
                    except (TypeError, ValueError) as e:
                        # TypeError: pychomsky yields plain error strings on gateway errors
                        # ValueError: model does not support streaming (e.g. "No generation chunks were returned")
                        last_error = e
                        wait = 30 * (attempt + 1)
                        print(f"[turn {turn}] stream error (attempt {attempt+1}/3), retrying in {wait}s: {e}", flush=True)
                        response = None
                        time.sleep(wait)
                else:
                    err_msg = f": {last_error}" if last_error else ""
                    print(f"[turn {turn}] failed after 3 attempts, stopping{err_msg}", flush=True)
                    break

                if response is None:
                    print(f"[turn {turn}] no response received", flush=True)
                    break

                in_tok, out_tok = _extract_token_usage(response, messages)
                total_input_tokens  += in_tok
                total_output_tokens += out_tok

                tool_calls = getattr(response, "tool_calls", [])

                if not tool_calls:
                    text = str(getattr(response, "content", "") or "")
                    preview = text[:300].replace("\n", " ")
                    print(f"[turn {turn}] done — {preview}", flush=True)
                    break

                messages.append(response)

                for tc in tool_calls:
                    name = tc["name"]
                    args = tc["args"]
                    tc_id = tc["id"]
                    hint = args.get("path", args.get("pattern", args.get("command", "")))
                    print(f"[turn {turn}]  {name}({hint})", flush=True)
                    result = self._execute_tool(workspace, name, args)
                    # Gemini requires name in ToolMessage (function_response.name);
                    # harmless for other models.
                    messages.append(ToolMessage(content=result, tool_call_id=tc_id, name=name))

                compact = _compact_settings_for(self.context_window)
                if compact is not None:
                    messages = self._compact_messages(messages, keep_full_turns=compact[0], trim_to=compact[1])

                interval = _min_turn_interval(self.model)
                if interval > 0:
                    time.sleep(interval)

            files = self._collect_output_files(workspace)

        synthesis_time = time.time() - start_time
        print(
            f"done  turns={turn} files={len(files)} "
            f"tokens={total_input_tokens:,}in/{total_output_tokens:,}out "
            f"time={synthesis_time:.1f}s",
            flush=True,
        )

        return SynthesisResult(
            code=files.get("generated_tools/__init__.py", ""),
            metadata={
                "model": self.model,
                "num_turns": turn,
                "files_written": list(files.keys()),
                "multi_file_structure": files,
            },
            token_usage={
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
            },
            synthesis_time=synthesis_time,
            cost_estimate=None,
        )

    def _stream_with_timeout(self, llm, messages: list, timeout: float = 120):
        """Stream LLM response with a wall-clock timeout.

        Returns the accumulated response, or None if the stream timed out.
        Raises TypeError if pychomsky yields a gateway error string.
        """
        import threading

        result = [None]
        exc = [None]

        def _run():
            try:
                response = None
                for chunk in llm.stream(messages):
                    response = chunk if response is None else response + chunk
                result[0] = response
            except (TypeError, ValueError) as e:
                exc[0] = e

        t = threading.Thread(target=_run, daemon=True)
        t.start()
        t.join(timeout=timeout)

        if exc[0] is not None:
            raise exc[0]
        if t.is_alive():
            return None  # timed out — caller will retry
        return result[0]

    def _compact_messages(self, messages: list, keep_full_turns: int = 2, trim_to: int = 500) -> list:
        """Truncate ToolMessage content for older turns to keep context small.

        Keeps the last `keep_full_turns` worth of tool messages at full length;
        older tool messages are trimmed to `trim_to` chars.
        """
        from langchain_core.messages import ToolMessage

        tool_indices = [i for i, m in enumerate(messages) if isinstance(m, ToolMessage)]
        keep_last_n = keep_full_turns * 4  # assume up to 4 tool calls per turn
        to_trim = tool_indices[:-keep_last_n] if len(tool_indices) > keep_last_n else []

        if not to_trim:
            return messages

        compacted = []
        for i, m in enumerate(messages):
            if i in to_trim and len(m.content) > trim_to:
                compacted.append(ToolMessage(
                    content=m.content[:trim_to] + "\n[truncated for context]",
                    tool_call_id=m.tool_call_id,
                    name=getattr(m, "name", None),  # preserve name for Gemini
                ))
            else:
                compacted.append(m)

        print(f"  [compact] trimmed {len(to_trim)} old tool messages to {trim_to} chars", flush=True)
        return compacted

    def _execute_tool(self, workspace: Path, name: str, inputs: dict) -> str:
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
                new_content = content.replace(old_str, inputs["new_str"], 1)
                target.write_text(new_content, encoding="utf-8")
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
                if not self.enable_bash:
                    return "Error: bash is disabled."
                result = subprocess.run(
                    inputs["command"],
                    shell=True,
                    cwd=str(workspace),
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                output = (result.stdout + result.stderr).strip()
                return output[:3000] + "\n[truncated]" if len(output) > 3000 else output or "(no output)"

            return f"Error: unknown tool {name}"
        except subprocess.TimeoutExpired:
            return "Error: command timed out after 30s"
        except Exception as e:
            return f"Error: {e}"

    def _collect_output_files(self, workspace: Path) -> Dict[str, str]:
        files = {}
        for path in sorted(workspace.rglob("*")):
            if not path.is_file():
                continue
            rel = str(path.relative_to(workspace))
            if rel == "TASK.md" or rel.startswith("docs/") or rel.startswith("source/"):
                continue
            files[rel] = path.read_text(encoding="utf-8")
        return files
