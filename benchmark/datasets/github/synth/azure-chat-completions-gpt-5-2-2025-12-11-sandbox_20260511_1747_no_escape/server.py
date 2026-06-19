import inspect
from typing import Any, Callable, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    actions_runs,
    actions_workflows,
    branch_protection,
    contents,
    issue_comments,
    issues,
    pull_request_reviews,
    pull_requests,
    releases,
    repos,
    search,
    webhooks,
)


mcp = FastMCP("github-rest")


def _register_module_functions(module, prefix: str = "") -> None:
    for name, fn in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        tool_name = f"{prefix}{name}" if prefix else name
        mcp.tool(name=tool_name)(fn)


# Register tools (no generic passthrough)
_register_module_functions(issues)
_register_module_functions(issue_comments)
_register_module_functions(pull_requests)
_register_module_functions(pull_request_reviews)
_register_module_functions(repos)
_register_module_functions(contents)
_register_module_functions(branch_protection)
_register_module_functions(actions_workflows)
_register_module_functions(actions_runs)
_register_module_functions(releases)
_register_module_functions(search)
_register_module_functions(webhooks)


if __name__ == "__main__":
    mcp.run()
