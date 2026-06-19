"""Pluggable synthesis implementations."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class Document:
    """A single documentation file."""
    path: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_file(cls, filepath: Path) -> "Document":
        return cls(
            path=str(filepath),
            content=filepath.read_text(encoding="utf-8"),
            metadata={"filename": filepath.name},
        )


@dataclass
class SynthesisResult:
    """Result from a synthesis run."""
    code: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    token_usage: Optional[Dict[str, int]] = None
    synthesis_time: Optional[float] = None
    cost_estimate: Optional[float] = None

    def save(self, output_path: Path) -> None:
        output_path.write_text(self.code, encoding="utf-8")


class BaseSynthesizer(ABC):
    """Abstract base class for all synthesizers."""

    @abstractmethod
    def synthesize(self, task_prompt: str, api_docs: List[Document], **kwargs) -> SynthesisResult:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass


def __getattr__(name: str):
    if name == "AgenticOpenRouter":
        from .agentic_openrouter import AgenticOpenRouter
        return AgenticOpenRouter
    if name == "AgenticOpenRouterRaw":
        from .agentic_openrouter_raw import AgenticOpenRouterRaw
        return AgenticOpenRouterRaw
    if name == "AgenticVLLM":
        from .agentic_vllm import AgenticVLLM
        return AgenticVLLM
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Document", "SynthesisResult", "BaseSynthesizer",
    "AgenticOpenRouter", "AgenticOpenRouterRaw", "AgenticVLLM",
]
