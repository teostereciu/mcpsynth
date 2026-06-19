"""Data models for the agent harness."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Task:
    """A task for the agent to complete using MCP tools."""
    id: str
    prompt: str
    # Optional: expected answer for rule-based scoring (None = LLM-as-judge only)
    expected: str | None = None
    # Optional: tags for grouping/filtering (e.g. ["read", "write", "multi-step"])
    tags: list[str] = field(default_factory=list)


@dataclass
class ToolCall:
    """A single tool call made during agent execution."""
    name: str
    arguments: dict[str, Any]
    result: Any  # parsed JSON result or string
    error: bool = False  # True if the tool returned an error dict


# Failure reasons that indicate the tool is not at fault — result is undefined for tool quality.
# TOOL_DOCUMENTATION is intentionally excluded: poor descriptions that misled the agent
# are a tool quality signal and should count as fail, not undefined.
_UNDEFINED_REASONS = {"AGENT_REASONING", "TASK_AMBIGUOUS", "ENVIRONMENT"}


@dataclass
class TaskResult:
    """Result of running an agent on a single task.

    Two orthogonal quality signals:

    verdict (agent success):
      "pass"      - agent completed the task successfully
      "fail"      - tool-related failure (TOOL_DOCUMENTATION, TOOL_SCHEMA, TOOL_IMPLEMENTATION, TOOL_COVERAGE)
      "undefined" - cannot draw conclusions about tool quality (AGENT_REASONING,
                    TASK_AMBIGUOUS, ENVIRONMENT, or unreliable judge)

    server_sufficient (synthesis quality):
      True   - the server had the right tools, correct schemas, and working implementations
               to complete the task (regardless of whether the agent succeeded)
      False  - the server was missing a tool, had a broken schema, or a faulty implementation
      None   - cannot determine (ENVIRONMENT, TASK_AMBIGUOUS, or judge unreliable)
    """
    task_id: str
    success: bool  # True iff verdict == "pass"
    tool_calls: list[ToolCall] = field(default_factory=list)
    final_answer: str = ""
    judge_reasoning: str = ""
    failure_reason: str = ""  # TOOL_COVERAGE | TOOL_DOCUMENTATION | TOOL_SCHEMA | TOOL_IMPLEMENTATION | AGENT_REASONING | TASK_AMBIGUOUS | ENVIRONMENT | ""
    judge_reliable: bool = True  # False if judge response could not be parsed and heuristic was used
    # Synthesis quality: did the server have what was needed, regardless of agent behaviour?
    server_sufficient: bool | None = None
    num_turns: int = 0
    error: str = ""  # harness-level error (server crash, timeout, etc.)

    @property
    def verdict(self) -> str:
        """Three-way verdict for tool-quality analysis."""
        if self.success:
            return "pass"
        if not self.judge_reliable:
            return "undefined"
        if self.failure_reason in _UNDEFINED_REASONS:
            return "undefined"
        return "fail"

    @property
    def num_tool_calls(self) -> int:
        return len(self.tool_calls)

    @property
    def num_errors(self) -> int:
        return sum(1 for tc in self.tool_calls if tc.error)
