"""
Agentic synthesizer using pychomsky (eBay internal LLM gateway).

Runs a manual tool-calling loop using pychomsky's LangChain-compatible wrappers.
The wrapper is selected automatically based on model name:
  - "*anthropic*" → GCPVertexAnthropicChatWrapper  (Claude on GCP Vertex)
  - "azure-*"     → AzureOpenAIChatWrapper          (GPT models on Azure)
  - "*gemini*"    → GoogleGenAIWrapper               (Gemini on GCP)
  - anything else → EbayLLMChatWrapper               (internal Lilium models)

Note: all wrappers use Anthropic-format tool dicts (input_schema). OpenAI format
does NOT work with GoogleGenAIWrapper despite it using convert_to_openai_tool internally.

Required env vars:  none (pychomsky picks up eBay internal credentials automatically)
Optional:           pass chgw_endpoint= to override the default gateway URL

Usage:
    synth = AgenticChomsky(model="gcp-chat-completions-anthropic-claude-sonnet-4.5-sandbox")
    result = synth.synthesize(task_prompt, api_docs)
"""

import time
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from benchmark.synthesizers import BaseSynthesizer, Document, SynthesisResult


SYSTEM_PROMPT = """\
You are an expert software engineer building MCP server implementations from API documentation.

Your workspace contains:
- TASK.md  — requirements and deliverables (read this first)
- docs/    — API endpoint documentation files

Workflow:
1. Read TASK.md to understand what to build and what files to deliver
2. Use list_directory to list docs/, then read a representative sample across all API domains
3. Write all deliverable files (generated_tools/, server.py, SCENARIO_SOLUTIONS.md, requirements.txt)

Read docs before writing code — base your implementation on the actual API docs.
Sample 3-5 endpoints per domain to understand patterns, then generalize.
You MUST use the write_file tool to output all deliverables. Do not describe code in text.\
"""

TASK_PROMPT = "Read TASK.md, explore the docs/, then write all deliverables specified in TASK.md."

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
]


class AgenticChomsky(BaseSynthesizer):

    def __init__(
        self,
        model: str = "gcp-chat-completions-anthropic-claude-sonnet-4.5-sandbox",
        max_turns: int = 50,
        max_tokens: int = 16000,
        chgw_endpoint: str = None,
    ):
        self.model = model
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.chgw_endpoint = chgw_endpoint

    @property
    def name(self) -> str:
        return f"agentic_chomsky_{self.model.replace('/', '_')}"

    @property
    def description(self) -> str:
        return f"Raw tool loop via pychomsky eBay gateway ({self.model})"

    def get_config(self) -> Dict[str, Any]:
        return {
            **super().get_config(),
            "model": self.model,
            "max_turns": self.max_turns,
            "max_tokens": self.max_tokens,
        }

    def _make_llm(self):
        """Instantiate the appropriate pychomsky wrapper based on model name prefix."""
        kwargs = {"model_name": self.model}
        if self.chgw_endpoint:
            kwargs["chgw_endpoint"] = self.chgw_endpoint

        if "anthropic" in self.model:
            from pychomsky.chchat.anthropicvertex import GCPVertexAnthropicChatWrapper
            return GCPVertexAnthropicChatWrapper(
                max_tokens=self.max_tokens,
                temperature=0.2,
                stream=True,  # constructor reads "stream", not "streaming"
                **kwargs,
            )
        elif self.model.startswith("azure-"):
            from pychomsky.chchat.azureopenai import AzureOpenAIChatWrapper
            llm = AzureOpenAIChatWrapper(
                max_completion_tokens=self.max_tokens,
                temperature=0.2,
                streaming=True,
                **kwargs,
            )
            llm.streaming = True  # override hardcoded False inside the wrapper
            return llm
        elif "gemini" in self.model:
            from pychomsky.chchat.googlegenai import GoogleGenAIWrapper
            return GoogleGenAIWrapper(
                max_tokens=self.max_tokens,
                temperature=0.2,
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

            print(f"[{self.model}] docs={len(api_docs)}", flush=True)

            llm = self._make_llm()
            llm_with_tools = llm.bind_tools(TOOLS)

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
                for attempt in range(3):
                    try:
                        response = self._stream_with_timeout(llm_with_tools, messages, timeout=120)
                        if response is not None:
                            break  # success
                        wait = 30 * (attempt + 1)
                        print(f"[turn {turn}] stream timeout (attempt {attempt+1}/3), retrying in {wait}s", flush=True)
                        time.sleep(wait)
                    except TypeError as e:
                        wait = 30 * (attempt + 1)
                        print(f"[turn {turn}] gateway error (attempt {attempt+1}/3), retrying in {wait}s: {e}", flush=True)
                        response = None
                        time.sleep(wait)
                else:
                    print(f"[turn {turn}] failed after 3 attempts, stopping", flush=True)
                    break

                if response is None:
                    print(f"[turn {turn}] no response received", flush=True)
                    break

                usage = getattr(response, "usage_metadata", None)
                if isinstance(usage, dict):
                    total_input_tokens += usage.get("input_tokens", 0)
                    total_output_tokens += usage.get("output_tokens", 0)

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
                    print(f"[turn {turn}]  {name}({args.get('path', '')})", flush=True)
                    result = self._execute_tool(workspace, name, args)
                    # Gemini requires name in ToolMessage (function_response.name);
                    # harmless for other models.
                    messages.append(ToolMessage(content=result, tool_call_id=tc_id, name=name))

                messages = self._compact_messages(messages)

                if "anthropic" in self.model:
                    time.sleep(11.0)

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
            except TypeError as e:
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

        Keeps the system message, human message, and the last `keep_full_turns`
        AI+Tool turn pairs at full length. Everything older is trimmed to `trim_to` chars.
        """
        from langchain_core.messages import ToolMessage

        # Find indices of ToolMessages to potentially trim
        tool_indices = [i for i, m in enumerate(messages) if isinstance(m, ToolMessage)]

        # Keep the last keep_full_turns * (avg tools per turn) tool messages intact
        # Rough heuristic: keep last N tool messages full, trim the rest
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

        trimmed_count = len(to_trim)
        if trimmed_count:
            print(f"  [compact] trimmed {trimmed_count} old tool messages to {trim_to} chars", flush=True)
        return compacted

    def _execute_tool(self, workspace: Path, name: str, inputs: dict) -> str:
        try:
            target = workspace / inputs["path"]
            if name == "read_file":
                if not target.exists():
                    return f"Error: not found: {inputs['path']}"
                content = target.read_text(encoding="utf-8")
                return content[:20_000] + "\n[truncated]" if len(content) > 20_000 else content
            elif name == "list_directory":
                if not target.is_dir():
                    return f"Error: not a directory: {inputs['path']}"
                return "\n".join(
                    f"{'d' if e.is_dir() else 'f'}  {e.name}" for e in sorted(target.iterdir())
                )
            elif name == "write_file":
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(inputs["content"], encoding="utf-8")
                return f"wrote {len(inputs['content'])} chars to {inputs['path']}"
            return f"Error: unknown tool {name}"
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
