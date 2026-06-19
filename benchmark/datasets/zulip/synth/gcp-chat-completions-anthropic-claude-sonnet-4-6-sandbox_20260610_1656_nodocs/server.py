"""
Zulip MCP Server
================
Exposes comprehensive Zulip REST API coverage as MCP tools over stdio.

Required environment variables:
    ZULIP_EMAIL   — bot or user email address
    ZULIP_API_KEY — API key
    ZULIP_SITE    — Zulip instance URL (e.g. https://your-org.zulipchat.com)
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.messages           import register_message_tools
from generated_tools.streams            import register_stream_tools
from generated_tools.topics             import register_topic_tools
from generated_tools.users              import register_user_tools
from generated_tools.reactions          import register_reaction_tools
from generated_tools.scheduled_messages import register_scheduled_message_tools
from generated_tools.drafts             import register_draft_tools
from generated_tools.uploads            import register_upload_tools
from generated_tools.realm              import register_realm_tools
from generated_tools.webhooks           import register_webhook_tools
from generated_tools.typing             import register_typing_tools
from generated_tools.events             import register_event_tools

mcp = FastMCP(
    name="zulip",
    instructions=(
        "This server exposes the Zulip REST API as MCP tools. "
        "Use it to send and manage messages, streams, topics, users, reactions, "
        "scheduled messages, drafts, file uploads, and organisation settings. "
        "Authentication is via HTTP Basic Auth using ZULIP_EMAIL and ZULIP_API_KEY "
        "environment variables against the ZULIP_SITE instance."
    ),
)

# Register all domain tool groups
register_message_tools(mcp)
register_stream_tools(mcp)
register_topic_tools(mcp)
register_user_tools(mcp)
register_reaction_tools(mcp)
register_scheduled_message_tools(mcp)
register_draft_tools(mcp)
register_upload_tools(mcp)
register_realm_tools(mcp)
register_webhook_tools(mcp)
register_typing_tools(mcp)
register_event_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
