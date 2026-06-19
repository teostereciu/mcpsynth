"""Mastodon MCP Server — entry point.

Runs over stdio using FastMCP. All tools are registered from domain modules
in generated_tools/.

Environment variables required:
    MASTODON_BASE_URL       — e.g. https://mastodon.social
    MASTODON_ACCESS_TOKEN   — OAuth 2.0 Bearer token
"""

from mcp.server.fastmcp import FastMCP

# Import all domain modules
from generated_tools import (
    statuses,
    accounts,
    timelines,
    notifications,
    lists,
    search,
    media,
    instance,
    bookmarks,
    favourites,
    blocks_mutes,
    filters,
    follow_requests,
    polls,
    tags,
    trends,
    conversations,
    scheduled_statuses,
    preferences,
    announcements,
    markers,
    suggestions,
    reports,
    domain_blocks,
    featured_tags,
)

mcp = FastMCP(
    name="mastodon",
    instructions=(
        "MCP server for the Mastodon REST API. "
        "Provides tools for posting statuses, managing accounts, reading timelines, "
        "handling notifications, searching content, managing lists, bookmarks, "
        "favourites, media uploads, filters, polls, tags, trends, and more. "
        "Requires MASTODON_BASE_URL and MASTODON_ACCESS_TOKEN environment variables."
    ),
)

# Register all domain tools
statuses.register(mcp)
accounts.register(mcp)
timelines.register(mcp)
notifications.register(mcp)
lists.register(mcp)
search.register(mcp)
media.register(mcp)
instance.register(mcp)
bookmarks.register(mcp)
favourites.register(mcp)
blocks_mutes.register(mcp)
filters.register(mcp)
follow_requests.register(mcp)
polls.register(mcp)
tags.register(mcp)
trends.register(mcp)
conversations.register(mcp)
scheduled_statuses.register(mcp)
preferences.register(mcp)
announcements.register(mcp)
markers.register(mcp)
suggestions.register(mcp)
reports.register(mcp)
domain_blocks.register(mcp)
featured_tags.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
