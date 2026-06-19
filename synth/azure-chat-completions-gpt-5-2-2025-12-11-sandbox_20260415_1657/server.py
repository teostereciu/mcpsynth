from __future__ import annotations

import inspect
from typing import Any, Callable, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    groups,
    help_center_articles,
    help_center_categories,
    help_center_sections,
    macros,
    organizations,
    satisfaction_ratings,
    search,
    tickets,
    users,
    views,
)


mcp = FastMCP("zendesk")


def _register_module_tools(module, prefix: str | None = None) -> None:
    for name, fn in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        tool_name = f"{prefix}_{name}" if prefix else name
        mcp.tool(name=tool_name)(fn)


_register_module_tools(tickets, "tickets")
_register_module_tools(users, "users")
_register_module_tools(organizations, "orgs")
_register_module_tools(groups, "groups")
_register_module_tools(search, "search")
_register_module_tools(macros, "macros")
_register_module_tools(views, "views")
_register_module_tools(satisfaction_ratings, "csat")
_register_module_tools(help_center_categories, "hc_categories")
_register_module_tools(help_center_sections, "hc_sections")
_register_module_tools(help_center_articles, "hc_articles")


if __name__ == "__main__":
    mcp.run()
