"""Agent harness: ReAct loop that drives an LLM to use MCP tools or a CLI tool.

Uses pychomsky (eBay internal gateway) to access:
  - Gemini 2.5 Pro  (primary)
  - Azure GPT-4.1   (secondary)

The harness runs one task at a time: connects to the MCP server (or CLI tool),
converts tool schemas to LLM tool format, and runs a tool-calling loop until
the model stops calling tools or max_turns is reached.

Modes:
  "mcp" (default) — connects to an MCP server via stdio (MCPServerSession)
  "cli"           — wraps a synthesized CLI tool with a run_command tool (CLIServerSession)
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .models import Task, TaskResult, ToolCall
from .mcp_server import MCPServerSession
from .cli_session import CLIServerSession


# ---------------------------------------------------------------------------
# Default models (pychomsky internal names)
# ---------------------------------------------------------------------------
DEFAULT_MODEL = "gcp-chat-completions-chat-gemini-2.5-pro-sandbox"
SECONDARY_MODEL = "azure-chat-completions-gpt-4-1-2025-04-14-sandbox"
DEFAULT_JUDGE_MODEL = "gcp-chat-completions-chat-gemini-3-flash-preview-sandbox"

SYSTEM_PROMPT = """\
You are an autonomous agent completing tasks by calling API tools. You MUST use the \
provided tools — do not answer from prior knowledge or describe what you would do. \
Call tools to get real data and take real actions.

Rules:
1. Always call at least one tool before giving a final answer.
2. Use results from earlier tool calls to inform later ones.
3. When a task contains an ALL_CAPS name like GITHUB_TEST_REPO, ADYEN_MERCHANT_ACCOUNT, \
   ZULIP_EMAIL, etc. — pass that exact string as the argument value. Do NOT ask what it \
   means, do NOT wait for clarification. Just pass "GITHUB_TEST_REPO" (or whatever the \
   name is) directly to the tool. The server handles resolution.
4. When done, summarize what the tools returned.

Never say "I cannot" or "I would need". Never ask for clarification. Just call the tools.
"""

CLI_SYSTEM_PROMPT = """\
You are an autonomous agent completing tasks using a CLI tool. You have access to a \
single tool, run_command, which runs commands against a synthesized CLI script. \
You MUST use run_command — do not answer from prior knowledge or describe what you would do.

Rules:
1. Start by discovering the CLI's interface (e.g. pass --help or -h to run_command).
2. Always call run_command at least once before giving a final answer.
3. Use results from earlier calls to inform later ones.
4. When a task contains an ALL_CAPS name like ZULIP_EMAIL, pass that exact string as \
   the argument value. The CLI handles resolution.
5. When done, summarize what the CLI returned.

Never say "I cannot" or "I would need". Never ask for clarification. Just call run_command.
"""


class AgentHarness:
    """Runs a ReAct agent loop against a live MCP server or synthesized CLI tool.

    Args:
        model: pychomsky model name (default: Gemini 2.5 Pro sandbox)
        max_turns: maximum agent loop iterations
        max_tokens: max tokens per LLM response
        judge_model: model for LLM-as-judge verification (None = no judge)
        request_delay: seconds to wait between LLM calls (rate limiting)
        mode: "mcp" (default) or "cli" — selects MCPServerSession vs CLIServerSession
    """

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        max_turns: int = 10,
        max_tokens: int = 8192,
        judge_model: str | None = DEFAULT_JUDGE_MODEL,
        request_delay: float = 1.0,
        mode: str = "mcp",
    ):
        self.model = model
        self.max_turns = max_turns
        self.max_tokens = max_tokens
        self.judge_model = judge_model
        self.request_delay = request_delay
        if mode not in ("mcp", "cli"):
            raise ValueError(f"mode must be 'mcp' or 'cli', got {mode!r}")
        self.mode = mode

    def _make_llm(self, model: str):
        """Instantiate the appropriate pychomsky wrapper for the given model."""
        kwargs = {"model_name": model}

        if "anthropic" in model:
            from pychomsky.chchat.anthropicvertex import GCPVertexAnthropicChatWrapper
            return GCPVertexAnthropicChatWrapper(
                max_tokens=self.max_tokens,
                temperature=0.0,
                stream=True,
                **kwargs,
            )
        elif model.startswith("azure-"):
            from pychomsky.chchat.azureopenai import AzureOpenAIChatWrapper
            llm = AzureOpenAIChatWrapper(
                max_completion_tokens=self.max_tokens,
                temperature=0.0,
                streaming=True,
                **kwargs,
            )
            llm.streaming = True
            return llm
        elif "gemini" in model:
            from pychomsky.chchat.googlegenai import GoogleGenAIWrapper
            return GoogleGenAIWrapper(
                max_tokens=self.max_tokens,
                temperature=0.0,
                **kwargs,
            )
        else:
            from pychomsky.chchat import EbayLLMChatWrapper
            return EbayLLMChatWrapper(
                max_tokens=self.max_tokens,
                temperature=0.0,
                streaming=True,
                **kwargs,
            )

    def _mcp_tools_to_llm_format(self, mcp_tools: list[dict]) -> list[dict]:
        """Convert MCP tool list to Anthropic-format tool dicts for pychomsky bind_tools.

        All pychomsky wrappers accept Anthropic format (input_schema).
        """
        return [
            {
                "name": t["name"],
                "description": t["description"],
                "input_schema": t.get("input_schema") or {"type": "object", "properties": {}},
            }
            for t in mcp_tools
        ]

    def _stream_with_timeout(self, llm, messages: list, timeout: float = 120):
        """Stream LLM response with a wall-clock timeout. Returns response or None."""
        import threading

        result = [None]
        exc = [None]

        def _run():
            try:
                response = None
                for chunk in llm.stream(messages):
                    response = chunk if response is None else response + chunk
                result[0] = response
            except Exception as e:
                exc[0] = e

        t = threading.Thread(target=_run, daemon=True)
        t.start()
        t.join(timeout=timeout)

        if exc[0] is not None:
            raise exc[0]
        if t.is_alive():
            return None  # timed out
        return result[0]

    def run_task(self, task: Task, server_dir: str | Path) -> TaskResult:
        """Run a single task against the MCP server at server_dir.

        Args:
            task: the Task to complete
            server_dir: directory containing server.py or build/index.js

        Returns:
            TaskResult with tool call trajectory, success verdict, and reasoning.
        """
        from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

        tool_calls: list[ToolCall] = []
        final_answer = ""
        num_turns = 0

        session_cls = CLIServerSession if self.mode == "cli" else MCPServerSession
        system_prompt = CLI_SYSTEM_PROMPT if self.mode == "cli" else SYSTEM_PROMPT

        try:
            with session_cls(server_dir) as server:
                mcp_tools = server.list_tools()
                if not mcp_tools:
                    return TaskResult(
                        task_id=task.id,
                        success=False,
                        error="Server returned no tools",
                    )

                llm_tools = self._mcp_tools_to_llm_format(mcp_tools)
                llm = self._make_llm(self.model)
                llm_with_tools = llm.bind_tools(llm_tools)

                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=task.prompt),
                ]

                for _ in range(self.max_turns):
                    num_turns += 1

                    response = None
                    for attempt in range(3):
                        try:
                            response = self._stream_with_timeout(llm_with_tools, messages, timeout=120)
                            if response is not None:
                                break
                            wait = 20 * (attempt + 1)
                            print(f"  [turn {num_turns}] timeout (attempt {attempt+1}/3), retry in {wait}s", flush=True)
                            time.sleep(wait)
                        except Exception as e:
                            wait = 20 * (attempt + 1)
                            print(f"  [turn {num_turns}] error (attempt {attempt+1}/3), retry in {wait}s: {e}", flush=True)
                            time.sleep(wait)

                    if response is None:
                        break

                    calls = getattr(response, "tool_calls", [])
                    if not calls:
                        # Agent is done — extract final answer
                        content = getattr(response, "content", "")
                        if isinstance(content, list):
                            # Some models return list of content blocks
                            text_parts = [
                                b.get("text", "") if isinstance(b, dict) else str(b)
                                for b in content
                            ]
                            final_answer = " ".join(text_parts).strip()
                        else:
                            final_answer = str(content or "").strip()
                        break

                    messages.append(response)

                    for tc in calls:
                        name = tc["name"]
                        args = tc.get("args", {})
                        tc_id = tc.get("id") or name  # Gemini sometimes omits id

                        print(f"  [turn {num_turns}] {name}({_summarize_args(args)})", flush=True)
                        try:
                            result = server.call_tool(name, args)
                        except Exception as e:
                            result = {"error": str(e)}

                        is_error = isinstance(result, dict) and "error" in result
                        tool_calls.append(ToolCall(name=name, arguments=args, result=result, error=is_error))

                        result_text = json.dumps(result) if not isinstance(result, str) else result
                        # Gemini requires the tool name in ToolMessage; harmless for other models
                        messages.append(ToolMessage(content=result_text, tool_call_id=tc_id, name=name))

                    if self.request_delay > 0:
                        time.sleep(self.request_delay)

        except FileNotFoundError as e:
            return TaskResult(task_id=task.id, success=False, error=str(e))
        except Exception as e:
            return TaskResult(
                task_id=task.id,
                success=False,
                tool_calls=tool_calls,
                num_turns=num_turns,
                error=str(e),
            )

        # Determine success
        success, reasoning, failure_reason, _, reliable, server_sufficient = self._judge(
            task, tool_calls, final_answer, mcp_tools
        )

        return TaskResult(
            task_id=task.id,
            success=success,
            tool_calls=tool_calls,
            final_answer=final_answer,
            judge_reasoning=reasoning,
            failure_reason=failure_reason,
            judge_reliable=reliable,
            server_sufficient=server_sufficient,
            num_turns=num_turns,
        )

    def _judge(
        self,
        task: Task,
        tool_calls: list[ToolCall],
        final_answer: str,
        available_tools: list[dict],
    ) -> tuple[bool, str, str, dict[str, int | None], bool, bool | None]:
        """Determine task success.

        Returns (success, reasoning, failure_reason, rubric_scores, reliable, server_sufficient).

        rubric_scores keys: tool_selection, param_quality, result_interpretation, task_completion
        Each is 0-2 or None if not scored.
        reliable is False when the rubric could not be parsed and heuristic was used.
        server_sufficient is True/False/None based on the judge's SERVER_SUFFICIENT answer.
        """
        no_scores: dict[str, int | None] = {
            "tool_selection": None, "param_quality": None,
            "result_interpretation": None, "task_completion": None,
        }

        # LLM-as-judge (rubric-based)
        if self.judge_model:
            return self._llm_judge(task, tool_calls, final_answer, available_tools)

        # Heuristic fallback: at least one successful tool call
        successful = [tc for tc in tool_calls if not tc.error]
        if successful:
            return True, "Agent made at least one successful tool call.", "", no_scores, False, None
        return False, "No successful tool calls made.", "", no_scores, False, None

    def _llm_judge(
        self,
        task: Task,
        tool_calls: list[ToolCall],
        final_answer: str,
        available_tools: list[dict],
    ) -> tuple[bool, str, str, dict[str, int | None], bool, bool | None]:
        """Use an LLM to judge whether the agent completed the task.

        Returns (success, reasoning, failure_reason, rubric_scores, reliable, server_sufficient).

        Three questions asked of the judge:
          1. OUTCOME: did the agent complete the task? (PASS/FAIL)
          2. SERVER_SUFFICIENT: did the server have everything needed, independent of agent behavior?
          3. FAILURE_CAUSE (if FAIL): where did it break?

        failure_reason codes:
          TOOL_COVERAGE         - no tool for the required operation
          TOOL_DOCUMENTATION    - tool exists but poor naming/descriptions caused agent to miss or misuse it
          TOOL_SCHEMA           - tool schema has wrong param types, missing fields, or malformed response
          TOOL_IMPLEMENTATION   - tool ran but returned wrong, incomplete, or malformed data
          AGENT_REASONING       - server adequate; agent hallucinated or ignored correct results [confound]
          TASK_AMBIGUOUS        - task prompt unclear [confound]
          ENVIRONMENT           - server crash, network failure, missing credentials [confound]
        """
        from langchain_core.messages import HumanMessage, SystemMessage

        no_scores: dict[str, int | None] = {
            "tool_selection": None, "param_quality": None,
            "result_interpretation": None, "task_completion": None,
        }

        trajectory = _format_trajectory(tool_calls, final_answer)
        tool_list = _format_tool_list(available_tools)
        expected_hint = f"\nExpected answer content: {task.expected}" if task.expected else ""

        judge_prompt = f"""\
Task given to agent:
{task.prompt}{expected_hint}

Tools available in this MCP server:
{tool_list}

Agent trajectory:
{trajectory}

Answer the following three questions.

1. OUTCOME: Did the agent complete the task correctly?
   PASS if the final answer correctly addresses the task based on real tool results.
   FAIL if the task was not completed, completed incorrectly, or the agent could not use the tools.

2. FAILURE_CAUSE: If FAIL, what caused it? Choose the single best fit:
   TOOL_COVERAGE      - no tool exists in the server for the required operation
   TOOL_DOCUMENTATION - a relevant tool exists but poor naming, descriptions, or undocumented parameters
                        caused the agent to miss it, call the wrong one, or pass wrong values.
                        Use this when a capable agent would have succeeded with clearer tool design.
   TOOL_SCHEMA        - tool schema has structural problems: wrong param types, missing required fields,
                        or a response format the agent cannot parse
   TOOL_IMPLEMENTATION - tool ran but returned wrong, incomplete, or malformed data; includes runtime
                        crashes and exceptions inside the tool
   AGENT_REASONING    - server was adequate; agent hallucinated values or ignored a correct tool result.
                        Reserve for unambiguous hallucinations only. If the agent was confused by poor
                        tool design, use TOOL_DOCUMENTATION instead. Assume the agent is competent.
   TASK_AMBIGUOUS     - the task prompt itself was unclear or underspecified [measurement confound]
   ENVIRONMENT        - server crash on startup, network failure, or missing credentials [measurement confound]
   NONE               - use if OUTCOME is PASS

3. SERVER_SUFFICIENT: Setting aside what the agent did, did this server have everything needed to
   complete the task if used correctly?
   YES     - a tool exists, its schema is correct, it returns valid data, and its name/description
             are clear enough for a competent agent to find and use it
   NO      - any of the above conditions fail (missing tool, broken schema, bad implementation,
             or so poorly described that no competent agent could use it)
   UNKNOWN - ENVIRONMENT or TASK_AMBIGUOUS prevented a fair assessment

Respond in exactly this format (no extra text, no markdown):
OUTCOME: PASS or FAIL
FAILURE_CAUSE: <code from list above, or NONE if PASS>
SERVER_SUFFICIENT: YES, NO, or UNKNOWN
REASON: <one sentence explaining the outcome>
"""

        judge_llm = self._make_llm(self.judge_model)
        system = SystemMessage(content=(
            "You are an objective judge evaluating an AI agent's task completion. "
            "Follow the output format exactly. Do not add any extra text or markdown."
        ))

        for attempt in range(2):
            try:
                response = self._stream_with_timeout(
                    judge_llm,
                    [system, HumanMessage(content=judge_prompt)],
                    timeout=60,
                )
                content = str(getattr(response, "content", "") or "").strip()
                success, reason, failure_reason, server_sufficient, parsed_ok = _parse_judge_response(content)
                if parsed_ok:
                    return success, reason, failure_reason, no_scores, True, server_sufficient
                if attempt == 0:
                    continue
            except Exception as e:
                if attempt == 0:
                    continue
                successful = [tc for tc in tool_calls if not tc.error]
                heuristic_pass = bool(successful)
                return (
                    heuristic_pass,
                    f"Judge failed ({e}); heuristic: {len(successful)} successful calls.",
                    "",
                    no_scores,
                    False,
                    None,
                )

        # Both attempts produced incomplete parse — heuristic fallback
        successful = [tc for tc in tool_calls if not tc.error]
        heuristic_pass = bool(successful)
        return (
            heuristic_pass,
            f"Judge parse incomplete after 2 attempts; heuristic: {len(successful)} successful calls.",
            "",
            no_scores,
            False,
            None,
        )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _summarize_args(args: dict, max_len: int = 80) -> str:
    """Format tool call args for logging."""
    s = ", ".join(f"{k}={repr(v)}" for k, v in (args or {}).items())
    return s[:max_len] + "..." if len(s) > max_len else s


def _format_tool_list(tools: list[dict]) -> str:
    """Format available MCP tools for the judge prompt."""
    if not tools:
        return "(no tools available)"
    lines = []
    for t in tools:
        desc = (t.get("description") or "").split("\n")[0][:120]
        lines.append(f"  - {t['name']}: {desc}")
    return "\n".join(lines)


def _parse_judge_response(content: str) -> tuple[bool, str, str, bool | None, bool]:
    """Parse the structured judge response.

    Expected format:
        OUTCOME: PASS or FAIL
        FAILURE_CAUSE: <code or NONE>
        SERVER_SUFFICIENT: YES, NO, or UNKNOWN
        REASON: <text>

    Returns (success, reason, failure_reason, server_sufficient, parsed_ok).
    parsed_ok is False if any required field was missing.
    """
    outcome: bool | None = None
    failure_reason = ""
    server_sufficient: bool | None = None
    reason = ""

    for line in content.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip().upper()
        val = val.strip()
        val_upper = val.upper()

        if key == "OUTCOME":
            outcome = "PASS" in val_upper
        elif key == "FAILURE_CAUSE":
            failure_reason = "" if "NONE" in val_upper else val_upper.split()[0]
        elif key == "SERVER_SUFFICIENT":
            if "UNKNOWN" in val_upper:
                server_sufficient = None
            elif "YES" in val_upper:
                server_sufficient = True
            elif "NO" in val_upper:
                server_sufficient = False
        elif key == "REASON":
            reason = val

    parsed_ok = outcome is not None and reason != ""
    return (outcome or False), reason, failure_reason, server_sufficient, parsed_ok


def _format_trajectory(tool_calls: list[ToolCall], final_answer: str) -> str:
    """Format tool call history for the judge prompt."""
    lines = []
    for i, tc in enumerate(tool_calls, 1):
        args_str = json.dumps(tc.arguments, ensure_ascii=False)[:200]
        result_str = (
            json.dumps(tc.result, ensure_ascii=False)[:300]
            if not isinstance(tc.result, str)
            else tc.result[:300]
        )
        lines.append(f"Step {i}: {tc.name}({args_str})")
        lines.append(f"  Result: {result_str}")
    if final_answer:
        lines.append(f"\nFinal answer: {final_answer[:500]}")
    return "\n".join(lines) if lines else "(no tool calls)"
