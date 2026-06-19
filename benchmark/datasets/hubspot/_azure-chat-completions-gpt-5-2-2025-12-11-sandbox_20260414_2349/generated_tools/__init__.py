"""HubSpot MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from . import associations, companies, contacts, deals, owners, pipelines, properties, tickets, search

mcp = FastMCP("hubspot-crm")


def _register(module) -> None:
    for name in dir(module):
        if name.startswith("_"):
            continue
        obj = getattr(module, name)
        if callable(obj):
            mcp.tool(name=name)(obj)


for _mod in (contacts, companies, deals, tickets, owners, pipelines, properties, associations, search):
    _register(_mod)
