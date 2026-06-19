"""Zendesk MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

from .groups import groups_create, groups_delete, groups_list, groups_show, groups_update
from .help_center import (
    hc_articles_archive,
    hc_articles_create_in_section,
    hc_articles_list,
    hc_articles_show,
    hc_articles_update,
    hc_search,
    hc_unified_search,
)
from .organizations import (
    organizations_create,
    organizations_delete,
    organizations_list,
    organizations_show,
    organizations_update,
)
from .search import search_count, search_list
from .tickets import tickets_create, tickets_delete, tickets_list, tickets_list_recent, tickets_show, tickets_update
from .users import users_create, users_delete, users_list, users_search, users_show, users_update

mcp = FastMCP("zendesk")

# Tickets
mcp.tool()(tickets_create)
mcp.tool()(tickets_show)
mcp.tool()(tickets_update)
mcp.tool()(tickets_delete)
mcp.tool()(tickets_list)
mcp.tool()(tickets_list_recent)

# Users
mcp.tool()(users_create)
mcp.tool()(users_show)
mcp.tool()(users_update)
mcp.tool()(users_delete)
mcp.tool()(users_list)
mcp.tool()(users_search)

# Organizations
mcp.tool()(organizations_create)
mcp.tool()(organizations_show)
mcp.tool()(organizations_update)
mcp.tool()(organizations_delete)
mcp.tool()(organizations_list)

# Groups
mcp.tool()(groups_create)
mcp.tool()(groups_show)
mcp.tool()(groups_update)
mcp.tool()(groups_delete)
mcp.tool()(groups_list)

# Search
mcp.tool()(search_list)
mcp.tool()(search_count)

# Help Center
mcp.tool()(hc_articles_list)
mcp.tool()(hc_articles_show)
mcp.tool()(hc_articles_create_in_section)
mcp.tool()(hc_articles_update)
mcp.tool()(hc_articles_archive)
mcp.tool()(hc_search)
mcp.tool()(hc_unified_search)
