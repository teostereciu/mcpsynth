"""
Agentic synthesizer using a self-hosted vLLM endpoint.

Uses the OpenAI client pointed at a vLLM server and runs a manual
tool-calling loop with read_file / list_directory / write_file /
edit_file / glob / grep tools. Works with any model vLLM serves that
supports tool calling.

vLLM must be started with tool calling enabled, e.g.:
    vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \\
        --enable-auto-tool-choice \\
        --tool-call-parser deepseek_r1 \\
        --host 0.0.0.0 --port 8000

Common tool-call parsers: deepseek_r1, hermes, mistral, llama3_json

Usage:
    synth = AgenticVLLM(model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B")
    result = synth.synthesize(task_prompt, api_docs)

    # Custom endpoint
    synth = AgenticVLLM(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        base_url="http://my-gpu-server:8000/v1",
    )

    # Via synthesize.py CLI (--vllm flag routes to this class):
    uv run python benchmark/scripts/synthesize.py github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B --vllm

    uv run python benchmark/scripts/synthesize.py github \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \\
        --vllm --vllm-url http://my-gpu-server:8000/v1
"""

import json
import re
import subprocess
import time
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

import openai

from benchmark.synthesizers import BaseSynthesizer, Document, SynthesisResult


# Context window sizes by model name fragment (case-insensitive substring match).
# Add entries here as you test new models. Models not listed default to 128K.
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
# None = skip compaction entirely (for very large context models).
_COMPACT_SETTINGS = {
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


# Tool definitions in OpenAI function-calling format
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
4. Finish with server.py, requirements.txt, SCENARIO_SOLUTIONS.md.

Write all deliverables to files — do not describe code in text.\
"""

TASK_PROMPT = "Read TASK.md, then use glob+grep to survey the docs, then process each domain with read→write alternation. Use edit_file to extend existing modules rather than rewriting them."


class AgenticVLLM(BaseSynthesizer):
    """Agentic tool-calling synthesizer backed by a self-hosted vLLM server.

    Communicates via the OpenAI-compatible API that vLLM exposes at /v1.
    """

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:8000/v1",
        max_turns: int = 100,
        max_tokens: int = 16_000,
        context_window: Optional[int] = None,
        enable_bash: bool = False,
        timeout: float = 300.0,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.context_window = context_window or _context_window(model)
        self.enable_bash = enable_bash
        # vLLM ignores the API key but the openai client requires a non-empty value
        self._client = openai.OpenAI(
            api_key="vllm",
            base_url=self.base_url,
            timeout=timeout,
        )

    @property
    def name(self) -> str:
        slug = self.model.split("/")[-1].replace(":", "-").replace(".", "-")
        return f"agentic_vllm_{slug}"

    @property
    def description(self) -> str:
        return f"Raw tool loop via vLLM ({self.model} @ {self.base_url})"

    def get_config(self) -> Dict[str, Any]:
        return {
            **super().get_config(),
            "model": self.model,
            "base_url": self.base_url,
            "max_turns": self.max_turns,
            "max_tokens": self.max_tokens,
            "context_window": self.context_window,
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
        compact = _compact_settings(self.context_window)
        compact_info = "off" if compact is None else f"{compact[0]}turns/{compact[1]}chars"
        print(
            f"[{self.model}] ctx={self.context_window // 1000}K compact={compact_info} docs={len(api_docs)}",
            flush=True,
        )

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

            messages: List[Dict] = [{"role": "user", "content": TASK_PROMPT}]
            token_usage = {"input_tokens": 0, "output_tokens": 0}
            turn = 0

            # Qwen3 and Qwen3.5 default to thinking mode; disable it for synthesis
            # to avoid bloated reasoning traces and tool-call parser interference.
            extra_body = {}
            if "qwen3" in self.model.lower():
                extra_body["chat_template_kwargs"] = {"enable_thinking": False}

            for _ in range(self.max_turns):
                try:
                    response = self._client.chat.completions.create(
                        model=self.model,
                        max_tokens=self.max_tokens,
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
                    print(f"[turn {turn}] done (finish_reason={choice.finish_reason})", flush=True)
                    break

                # Append the assistant message with its tool calls
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

                # Execute each tool call and append individual tool result messages
                for tc in msg.tool_calls:
                    try:
                        inputs = json.loads(tc.function.arguments)
                    except json.JSONDecodeError:
                        inputs = {}
                    result = self._execute_tool(workspace, tc.function.name, inputs)
                    print(
                        f"[turn {turn}]  {tc.function.name}"
                        f"({inputs.get('path', inputs.get('pattern', ''))})",
                        flush=True,
                    )
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": result,
                    })

                if compact is not None:
                    messages = self._compact_messages(messages, keep_full_turns=compact[0], trim_to=compact[1])

            files = self._collect_output_files(workspace)

        synthesis_time = time.time() - start_time
        u = token_usage
        print(
            f"done  turns={turn} "
            f"tokens={u['input_tokens']:,}in/{u['output_tokens']:,}out "
            f"time={synthesis_time:.1f}s",
            flush=True,
        )

        return SynthesisResult(
            code=files.get("generated_tools/__init__.py", ""),
            metadata={
                "model": self.model,
                "base_url": self.base_url,
                "num_turns": turn,
                "files_written": list(files.keys()),
                "multi_file_structure": files,
            },
            token_usage=token_usage,
            synthesis_time=synthesis_time,
        )

    def _compact_messages(self, messages: list, keep_full_turns: int, trim_to: int) -> list:
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
                if not self.enable_bash:
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
