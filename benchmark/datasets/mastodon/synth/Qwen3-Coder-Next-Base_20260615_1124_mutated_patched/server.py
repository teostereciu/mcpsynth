#!/usr/bin/env python3
"""
Mastodon MCP Server
"""

from mcp.server.fastmcp import FastMCP

# Import domains
from mcp_server.statuses import mcp as statuses_mcp
from mcp_server.accounts import mcp as accounts_mcp
from mcp_server.timelines import mcp as timelines_mcp
from mcp_server.notifications import mcp as notifications_mcp
from mcp_server.search import mcp as search_mcp
from mcp_server.lists import mcp as lists_mcp
from mcp_server.media import mcp as media_mcp
from mcp_server.instance import mcp as instance_mcp
from mcp_server.scheduled_statuses import mcp as scheduled_statuses_mcp
from mcp_server.push import mcp as push_mcp
from mcp_server.polls import mcp as polls_mcp
from mcp_server.reports import mcp as reports_mcp

# Initialize the main MCP server
mcp = FastMCP("mastodon")


# Register tools from all domains
@statuses_mcp.tool()
def register_statuses_tools():
    """Register all status tools."""
    pass

@accounts_mcp.tool()
def register_accounts_tools():
    """Register all account tools."""
    pass

@timelines_mcp.tool()
def register_timelines_tools():
    """Register all timeline tools."""
    pass

@notifications_mcp.tool()
def register_notifications_tools():
    """Register all notification tools."""
    pass

@search_mcp.tool()
def register_search_tools():
    """Register all search tools."""
    pass

@lists_mcp.tool()
def register_lists_tools():
    """Register all list tools."""
    pass

@media_mcp.tool()
def register_media_tools():
    """Register all media tools."""
    pass

@instance_mcp.tool()
def register_instance_tools():
    """Register all instance tools."""
    pass

@scheduled_statuses_mcp.tool()
def register_scheduled_statuses_tools():
    """Register all scheduled status tools."""
    pass

@push_mcp.tool()
def register_push_tools():
    """Register all push notification tools."""
    pass

@polls_mcp.tool()
def register_polls_tools():
    """Register all poll tools."""
    pass

@reports_mcp.tool()
def register_reports_tools():
    """Register all report tools."""
    pass


# Main entry point
if __name__ == "__main__":
    # Run the server over stdio
    mcp.run(transport="stdio")
