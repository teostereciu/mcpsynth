import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues


mcp = FastMCP("github-rest")


grounding: Dict[str, Dict[str, str]] = {}


def _register(tool_name: str, func, doc: str, endpoint: str):
    mcp.tool(name=tool_name)(func)
    grounding[tool_name] = {"doc": doc, "endpoint": endpoint}


_register(
    "list_my_issues",
    list_my_issues,
    doc="docs/api_issues-issues.md",
    endpoint="GET /issues",
)


def main():
    mcp.run_stdio()


if __name__ == "__main__":
    main()
